// Safety helpers: input validation, atomic writes, and per-newsletter locks.
// Same primitives as ~/blog/publish/lib/safety.ts, narrowed to Compass's
// "newsletter number" identifier scheme.

import { writeFile, rename, mkdir, open, stat, unlink } from "node:fs/promises";
import { dirname, join } from "node:path";

// Compass newsletters are identified by issue number (positive integer).
const NUMBER_PATTERN = /^[1-9][0-9]{0,4}$/;

export function validateNumber(input: string): number {
  if (typeof input !== "string" || !NUMBER_PATTERN.test(input)) {
    throw new Error(
      `Invalid newsletter number "${input}". Expected a positive integer (1-99999), no leading zeroes.`,
    );
  }
  return parseInt(input, 10);
}

export async function writeAtomic(
  path: string,
  contents: string | Uint8Array,
): Promise<void> {
  await mkdir(dirname(path), { recursive: true });
  const tmp = `${path}.tmp.${process.pid}.${Date.now()}`;
  await writeFile(tmp, contents);
  await rename(tmp, path);
}

export class IssueLock {
  private path: string;
  private released = false;

  private constructor(path: string) {
    this.path = path;
  }

  static async acquire(issue: number, outDir: string): Promise<IssueLock> {
    const issueDir = join(outDir, String(issue));
    await mkdir(issueDir, { recursive: true });
    const lockPath = join(issueDir, ".lock");
    try {
      const fh = await open(lockPath, "wx");
      await fh.write(`pid=${process.pid} ts=${Date.now()}\n`);
      await fh.close();
      return new IssueLock(lockPath);
    } catch (e) {
      if ((e as NodeJS.ErrnoException).code === "EEXIST") {
        if (await isLockStale(lockPath)) {
          await rmIfExists(lockPath);
          return IssueLock.acquire(issue, outDir);
        }
        throw new Error(
          `Another publish run is in progress for issue ${issue} (lockfile ${lockPath}). ` +
            `Remove the lockfile manually if no other run is active.`,
        );
      }
      throw e;
    }
  }

  async release(): Promise<void> {
    if (this.released) return;
    this.released = true;
    await rmIfExists(this.path);
  }
}

async function isLockStale(path: string): Promise<boolean> {
  try {
    const s = await stat(path);
    return Date.now() - s.mtimeMs > 30 * 60 * 1000;
  } catch {
    return false;
  }
}

async function rmIfExists(path: string): Promise<void> {
  try {
    await unlink(path);
  } catch {
    /* already gone */
  }
}
