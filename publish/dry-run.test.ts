import { expect, test } from "bun:test";
import { mkdtemp, readdir, unlink, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";

test("dry-run parses and validates the real source without crossing a mutation boundary", async () => {
  const root = await mkdtemp(join(tmpdir(), "compass-zero-mutation-"));
  const out = join(root, "out");
  const issue = 99999; const source = `/tmp/${issue}publish.md`;
  const cover = JSON.parse(await Bun.file(join(import.meta.dir, "config/cover.json")).text());
  const tldr = "One two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty twentyone";
  await writeFile(source, `Nostr Compass #${issue}\n\n${tldr}\n\n${cover.banner_url}\n\nA fully linked publication body.\n`);
  try {
    const result = Bun.spawnSync([process.execPath, join(import.meta.dir, "publish.ts"), String(issue), "--stage", "parse", "--dry-run"], {
      env: { ...process.env, COMPASS_OUT_DIR: out }, stdout: "pipe", stderr: "pipe",
    });
    expect(result.exitCode).toBe(0);
    expect(new TextDecoder().decode(result.stdout)).toContain("executing read-only validation preview");
    expect(new TextDecoder().decode(result.stdout)).toContain("tldr=21 words");
    await expect(readdir(out)).rejects.toThrow();
  } finally { await unlink(source); }
});

test("dry-run rejects an invalid source while leaving the output tree absent", async () => {
  const root = await mkdtemp(join(tmpdir(), "compass-invalid-preview-")); const out = join(root, "out");
  const issue = 99998; const source = `/tmp/${issue}publish.md`;
  const cover = JSON.parse(await Bun.file(join(import.meta.dir, "config/cover.json")).text());
  await writeFile(source, `Nostr Compass #${issue}\n\nToo short.\n\n${cover.banner_url}\n\nBody.\n`);
  try {
    const result = Bun.spawnSync([process.execPath, join(import.meta.dir, "publish.ts"), String(issue), "--stage", "parse", "--dry-run"], { env: { ...process.env, COMPASS_OUT_DIR: out }, stdout: "pipe", stderr: "pipe" });
    expect(result.exitCode).not.toBe(0);
    expect(new TextDecoder().decode(result.stderr)).toContain("TL;DR has 2 words");
    await expect(readdir(out)).rejects.toThrow();
  } finally { await unlink(source); }
});
