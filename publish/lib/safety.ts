// Safety helpers: input validation, durable atomic writes, and fenced locks.
import { mkdir, open, readFile, readlink, rename, rm, symlink, unlink } from "node:fs/promises";
import { dirname, join } from "node:path";
import { randomUUID } from "node:crypto";

const NUMBER_PATTERN = /^[1-9][0-9]{0,4}$/;
export function validateNumber(input: string): number {
  if (typeof input !== "string" || !NUMBER_PATTERN.test(input)) throw new Error(`Invalid newsletter number "${input}". Expected a positive integer (1-99999), no leading zeroes.`);
  return parseInt(input, 10);
}
export async function writeAtomic(path: string, contents: string | Uint8Array): Promise<void> {
  await mkdir(dirname(path), { recursive: true }); const tmp = `${path}.tmp.${process.pid}.${randomUUID()}`; const file = await open(tmp, "wx", 0o600);
  try { await file.writeFile(contents); await file.sync(); } finally { await file.close(); }
  await rename(tmp, path);
  try { const directory = await open(dirname(path), "r"); try { await directory.sync(); } finally { await directory.close(); } } catch { /* unsupported directory fsync */ }
}

type LockOwner = { schema_version: 1; token: string; pid: number; process_start: string; created_at: string };
async function processStart(pid: number): Promise<string | undefined> {
  try { const raw = await readFile(`/proc/${pid}/stat`, "utf8"); const end = raw.lastIndexOf(")"); return end < 0 ? undefined : raw.slice(end + 2).trim().split(/\s+/)[19]; }
  catch { return undefined; }
}

// The lock is an atomic symlink to a fully written immutable owner record. We
// deliberately never auto-reclaim a stale lock: that avoids the TOCTOU window
// where a reclaimer can remove a newly acquired lease. A reconciler may remove
// it only while no worker is admitted and after independently checking owner.
export class IssueLock {
  private released = false;
  private constructor(private path: string, private ownerPath: string, private token: string) {}
  static async acquire(issue: number, outDir: string, name = ".lock"): Promise<IssueLock> {
    const issueDir = join(outDir, String(issue)); const owners = join(issueDir, ".lock-owners"); await mkdir(owners, { recursive: true });
    const token = randomUUID(); const ownerPath = join(owners, `${token}.json`); const start = await processStart(process.pid);
    if (!start) throw new Error("Cannot establish process identity for fenced lock");
    const owner: LockOwner = { schema_version: 1, token, pid: process.pid, process_start: start, created_at: new Date().toISOString() };
    await writeAtomic(ownerPath, JSON.stringify(owner));
    const path = join(issueDir, name); const deadline = Date.now() + (name === ".journal-lock" ? 5_000 : 0);
    for (;;) {
      try { await symlink(join(".lock-owners", `${token}.json`), path); break; }
      catch (error) {
        if ((error as NodeJS.ErrnoException).code !== "EEXIST" || Date.now() >= deadline) {
          await rm(ownerPath, { force: true });
          if ((error as NodeJS.ErrnoException).code === "EEXIST") throw new Error(`Another operation owns fenced lock ${path}; automatic stale reclaim is forbidden.`);
          throw error;
        }
        await Bun.sleep(10);
      }
    }
    return new IssueLock(path, ownerPath, token);
  }
  async release(): Promise<void> {
    if (this.released) return;
    const target = await readlink(this.path);
    if (target !== join(".lock-owners", `${this.token}.json`)) throw new Error(`Refusing to release lock no longer owned by this process: ${this.path}`);
    const owner = JSON.parse(await readFile(this.ownerPath, "utf8")) as LockOwner;
    if (owner.token !== this.token || owner.pid !== process.pid || owner.process_start !== await processStart(process.pid)) throw new Error(`Refusing to release lock with mismatched fencing identity: ${this.path}`);
    await unlink(this.path); await rm(this.ownerPath, { force: true }); this.released = true;
  }
}
