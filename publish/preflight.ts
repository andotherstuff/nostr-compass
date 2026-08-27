#!/usr/bin/env bun
// Bunker preflight. Triggers exactly one Amber approval to discover the
// signing pubkey. Updates config/author.json with both the npub and the hex
// pubkey on success. Refuses to overwrite a previously-set author unless
// --rotate is passed.

if (process.env.COMPASS_PUBLISH_INVOCATION !== "manual") {
  console.error("Refusing to run. Set COMPASS_PUBLISH_INVOCATION=manual.");
  process.exit(2);
}

import { join } from "node:path";
import { readFile } from "node:fs/promises";
import { spawn } from "node:child_process";
import { preflightBunker } from "./lib/bunker.ts";
import { writeAtomic } from "./lib/safety.ts";

const AUTHOR_PATH = join(import.meta.dir, "config/author.json");

function nakEncodeNpub(hex: string): Promise<string> {
  return new Promise((resolve, reject) => {
    const child = spawn("nak", ["encode", "npub", hex], { stdio: ["ignore", "pipe", "pipe"] });
    const out: Buffer[] = [];
    child.stdout.on("data", (c: Buffer) => out.push(c));
    child.on("close", (code) =>
      code === 0
        ? resolve(Buffer.concat(out).toString("utf8").trim())
        : reject(new Error(`nak encode npub exited ${code}`)),
    );
    child.on("error", reject);
  });
}

async function main() {
  const rotate = process.argv.includes("--rotate");
  const author = JSON.parse(await readFile(AUTHOR_PATH, "utf8")) as {
    npub: string;
    pubkey_hex: string;
  };

  console.log(`PREFLIGHT  current author config:`);
  console.log(`           npub:        ${author.npub}`);
  console.log(`           pubkey_hex:  ${author.pubkey_hex}`);
  console.log(`           sending throwaway sign request via Amber...`);
  console.log(`           (this is NOT broadcast; pairing test only)`);
  console.log("");

  const got = await preflightBunker();
  const npub = await nakEncodeNpub(got);

  console.log(`✓ bunker signed as ${got}`);
  console.log(`✓ npub:            ${npub}`);
  console.log("");

  if (author.pubkey_hex === "PENDING_PREFLIGHT") {
    await writeAtomic(
      AUTHOR_PATH,
      JSON.stringify(
        {
          _comment: author && (author as any)._comment,
          npub,
          pubkey_hex: got,
        },
        null,
        2,
      ),
    );
    console.log(`✓ author.json updated`);
  } else if (author.pubkey_hex !== got) {
    if (!rotate) {
      throw new Error(
        `Bunker signs as ${got} but author.json has ${author.pubkey_hex}. ` +
          `Pass --rotate to overwrite, or fix the bunker URI.`,
      );
    }
    await writeAtomic(
      AUTHOR_PATH,
      JSON.stringify({ npub, pubkey_hex: got }, null, 2),
    );
    console.log(`✓ author.json rotated to new pubkey`);
  } else {
    console.log(`✓ author.json already matches; no update needed`);
  }
}

main().catch((e) => {
  console.error("");
  console.error(`✗ preflight failed: ${(e as Error).message}`);
  process.exit(1);
});
