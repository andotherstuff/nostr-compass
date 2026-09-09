import { expect, test } from "bun:test";
import { mkdtemp, readdir } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";

test("dry-run exits before every file, signer, relay, GitHub, and notification mutation boundary", async () => {
  const root = await mkdtemp(join(tmpdir(), "compass-zero-mutation-"));
  const out = join(root, "out");
  const result = Bun.spawnSync([process.execPath, join(import.meta.dir, "publish.ts"), "99999", "--stage", "all", "--dry-run", "--really-merge", "--really-broadcast"], {
    env: { ...process.env, COMPASS_PUBLISH_INVOCATION: "manual", COMPASS_OUT_DIR: out },
    stdout: "pipe", stderr: "pipe",
  });
  expect(result.exitCode).toBe(0);
  expect(new TextDecoder().decode(result.stdout)).toContain("zero mutation preview");
  await expect(readdir(out)).rejects.toThrow();
});