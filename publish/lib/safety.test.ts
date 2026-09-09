import { describe, expect, test } from "bun:test";
import { lstat, mkdtemp, readFile, readlink } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { IssueLock } from "./safety.ts";

describe("IssueLock", () => {
  test("publishes a complete immutable owner before the atomic lock symlink", async () => {
    const out = await mkdtemp(join(tmpdir(), "compass-lock-")); const lock = await IssueLock.acquire(1, out);
    const path = join(out, "1", ".lock"); expect((await lstat(path)).isSymbolicLink()).toBe(true);
    const owner = JSON.parse(await readFile(join(out, "1", await readlink(path)), "utf8")); expect(owner.pid).toBe(process.pid); expect(owner.token).toBeTruthy();
    await lock.release(); await expect(lstat(path)).rejects.toThrow();
  });
  test("competing owners cannot reclaim or delete a live lease", async () => {
    const out = await mkdtemp(join(tmpdir(), "compass-lock-race-")); const first = await IssueLock.acquire(2, out);
    const contenders = await Promise.allSettled([IssueLock.acquire(2, out), IssueLock.acquire(2, out)]);
    expect(contenders.every((result) => result.status === "rejected")).toBe(true);
    expect((await lstat(join(out, "2", ".lock"))).isSymbolicLink()).toBe(true);
    await first.release(); const next = await IssueLock.acquire(2, out); await next.release();
  });
  test("unknown stale-looking lock state fails closed rather than racing reclamation", async () => {
    const out = await mkdtemp(join(tmpdir(), "compass-lock-stale-")); const first = await IssueLock.acquire(3, out);
    await expect(IssueLock.acquire(3, out)).rejects.toThrow("automatic stale reclaim is forbidden");
    await first.release();
  });
});
