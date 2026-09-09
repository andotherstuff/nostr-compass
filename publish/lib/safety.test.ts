import { describe, expect, test } from "bun:test";
import { mkdtemp, mkdir, utimes, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { IssueLock } from "./safety.ts";

describe("IssueLock", () => {
  test("does not steal an old lock owned by a live local PID", async () => {
    const out = await mkdtemp(join(tmpdir(), "compass-lock-"));
    const dir = join(out, "1"); await mkdir(dir);
    const path = join(dir, ".lock");
    await writeFile(path, `pid=${process.pid} ts=1\n`);
    const old = new Date(Date.now() - 31 * 60 * 1000); await utimes(path, old, old);
    expect(IssueLock.acquire(1, out)).rejects.toThrow("Another publish run");
  });

  test("malformed locks fail closed", async () => {
    const out = await mkdtemp(join(tmpdir(), "compass-lock-"));
    const dir = join(out, "2"); await mkdir(dir);
    const path = join(dir, ".lock");
    await writeFile(path, "not a lock\n");
    const old = new Date(Date.now() - 31 * 60 * 1000); await utimes(path, old, old);
    expect(IssueLock.acquire(2, out)).rejects.toThrow("Another publish run");
  });
});
