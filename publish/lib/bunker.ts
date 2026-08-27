// NIP-46 bunker client — single persistent session per pipeline run.
//
// History: this module used to shell out to `nak event --connect-as ...` per
// signature. Every invocation did a fresh NIP-46 connect handshake. Multi-step
// runs (sign + announce) re-handshook each time, multiplying transient
// Amber/relay latency. See ~/blog/publish/BUNKER.md for the full writeup.
//
// Now: one in-process `BunkerSigner` (from nostr-tools) held as a module-level
// singleton. One connect, many signs over the same open relay subscription.
//
// Compass uses ITS OWN bunker config (separate npub from blog/towardsliberty):
//   ~/.config/compass-publish/bunker.json
//   ~/.config/compass-publish/client_key
//
// Security properties preserved from the previous implementation:
//   - Bunker URI never appears in argv (no child process spawned).
//   - bunker.json is auto-chmod'd to 0600 on read.
//   - Error messages strip any bunker:// occurrences before logging.

import { readFile, mkdir, stat, chmod } from "node:fs/promises";
import { join } from "node:path";
import { homedir } from "node:os";
import { BunkerSigner, parseBunkerInput } from "nostr-tools/nip46";
import { SimplePool } from "nostr-tools/pool";
import { generateSecretKey } from "nostr-tools/pure";
import { hexToBytes, bytesToHex } from "@noble/hashes/utils.js";
import { writeFile } from "node:fs/promises";

const BUNKER_CONFIG = join(homedir(), ".config", "compass-publish", "bunker.json");
const CLIENT_KEY_FILE = join(homedir(), ".config", "compass-publish", "client_key");

type BunkerConfig = { bunker_uri: string };

export type UnsignedEvent = {
  kind: number;
  content: string;
  tags: string[][];
  created_at: number;
};

export type SignedEvent = UnsignedEvent & {
  id: string;
  pubkey: string;
  sig: string;
};

async function readBunkerConfig(): Promise<BunkerConfig> {
  let s;
  try {
    s = await stat(BUNKER_CONFIG);
  } catch {
    throw new Error(
      `Bunker config not found at ${BUNKER_CONFIG}. ` +
        `Create it with: { "bunker_uri": "bunker://..." }`,
    );
  }
  const mode = s.mode & 0o777;
  if (mode & 0o077) {
    await chmod(BUNKER_CONFIG, 0o600);
  }
  const raw = await readFile(BUNKER_CONFIG, "utf8");
  let parsed;
  try {
    parsed = JSON.parse(raw) as BunkerConfig;
  } catch {
    throw new Error(`Bunker config at ${BUNKER_CONFIG} is not valid JSON.`);
  }
  if (
    !parsed.bunker_uri ||
    typeof parsed.bunker_uri !== "string" ||
    !parsed.bunker_uri.startsWith("bunker://")
  ) {
    throw new Error(
      `bunker.json must contain {"bunker_uri": "bunker://..."}. ` +
        `Refusing to use a non-bunker secret (would bypass remote signer).`,
    );
  }
  return parsed;
}

async function getOrGenerateClientKey(): Promise<Uint8Array> {
  try {
    const raw = (await readFile(CLIENT_KEY_FILE, "utf8")).trim();
    if (raw.length === 64) return hexToBytes(raw);
  } catch {
    /* fall through */
  }
  const sk = generateSecretKey();
  const hex = bytesToHex(sk);
  await mkdir(join(homedir(), ".config", "compass-publish"), { recursive: true });
  await writeFile(CLIENT_KEY_FILE, hex + "\n", { mode: 0o600 });
  await chmod(CLIENT_KEY_FILE, 0o600);
  return sk;
}

function redact(value: unknown): string {
  const s = value instanceof Error ? value.message : String(value ?? "Unknown bunker error");
  return s.replace(/bunker:\/\/[^\s'"]+/g, "bunker://[REDACTED]");
}

let pool: SimplePool | undefined;
let signer: BunkerSigner | undefined;
let signerReady: Promise<BunkerSigner> | undefined;
let cachedUserPubkey: string | undefined;

async function getSigner(): Promise<BunkerSigner> {
  if (signer && signer.isOpen) return signer;
  if (signerReady) return signerReady;

  signerReady = (async () => {
    const cfg = await readBunkerConfig();
    const clientKey = await getOrGenerateClientKey();
    const bp = await parseBunkerInput(cfg.bunker_uri);
    if (!bp) throw new Error("Failed to parse bunker URI from bunker.json.");

    pool = new SimplePool();
    const s = BunkerSigner.fromBunker(clientKey, bp, {
      pool,
      onauth: (url) => {
        process.stderr.write(
          `              [bunker]: auth challenge from signer, open: ${url}\n`,
        );
      },
    });

    const CONNECT_TIMEOUT_MS = 15_000;
    let connectTimer: ReturnType<typeof setTimeout> | undefined;
    try {
      await Promise.race([
        s.connect(),
        new Promise<never>((_, reject) => {
          connectTimer = setTimeout(
            () =>
              reject(
                new Error(
                  `Bunker connect timed out after ${CONNECT_TIMEOUT_MS}ms.\n` +
                    `  Amber is not responding on the configured relays.\n` +
                    `  Fix: open Amber on the phone (one tap is enough), wait 5s, retry.\n` +
                    `  If that does not work and Amber is foreground, force-stop Amber\n` +
                    `  from Android Settings → Apps → Amber → Force stop, then reopen.`,
                ),
              ),
            CONNECT_TIMEOUT_MS,
          );
        }),
      ]);
    } finally {
      if (connectTimer) clearTimeout(connectTimer);
    }

    cachedUserPubkey = await s.getPublicKey();
    signer = s;
    return s;
  })();

  try {
    return await signerReady;
  } catch (e) {
    signerReady = undefined;
    throw e;
  }
}

export async function signWithBunker(
  unsigned: UnsignedEvent,
  expectedPubkey: string,
): Promise<SignedEvent> {
  const s = await getSigner();

  const SIGN_TIMEOUT_MS = 25_000;
  let timer: ReturnType<typeof setTimeout> | undefined;
  let signed: SignedEvent;
  try {
    signed = (await Promise.race([
      s.signEvent(unsigned as never),
      new Promise<never>((_, reject) => {
        timer = setTimeout(
          () =>
            reject(
              new Error(
                `Bunker sign_event timed out after ${SIGN_TIMEOUT_MS}ms.\n` +
                  `  Connect succeeded but the signer did not respond.\n` +
                  `  Open Amber — there is likely a pending approval dialog.\n` +
                  `  Approve it, then retry.`,
              ),
            ),
          SIGN_TIMEOUT_MS,
        );
      }),
    ])) as SignedEvent;
  } catch (e) {
    throw new Error(redact(e));
  } finally {
    if (timer) clearTimeout(timer);
  }

  if (signed.pubkey !== expectedPubkey) {
    throw new Error(
      `Bunker signed with pubkey ${signed.pubkey} but expected ${expectedPubkey}. ` +
        `Update config/author.json or the bunker URI. Aborting.`,
    );
  }
  if (!signed.id || !signed.sig) {
    throw new Error(`Signed event missing id or sig: ${JSON.stringify(signed)}`);
  }
  return signed;
}

// Preflight signs a throwaway event to discover the signing pubkey without
// committing to a real publish. Returns the pubkey hex it signed as.
// (Compass also uses this to lazily discover author.npub on first run.)
export async function preflightBunker(): Promise<string> {
  await getSigner();
  if (!cachedUserPubkey) {
    throw new Error("Preflight succeeded but no user pubkey was discovered.");
  }
  return cachedUserPubkey;
}

// NIP-44 encrypt via the remote signer (used for NIP-17 seal content and
// for the DM-outreach fallback path). Amber holds the real secret key; we
// never see it locally.
export async function nip44EncryptWithBunker(
  thirdPartyPubkeyHex: string,
  plaintext: string,
): Promise<string> {
  const s = await getSigner();
  try {
    return await s.nip44Encrypt(thirdPartyPubkeyHex, plaintext);
  } catch (e) {
    throw new Error(redact((e as Error).message));
  }
}

// NIP-04 encrypt via the remote signer. Used only as a fallback for
// recipients who have not published a NIP-65 relay list (kind 10002),
// meaning we cannot be confident their client even supports NIP-17 gift
// wraps yet.
export async function nip04EncryptWithBunker(
  thirdPartyPubkeyHex: string,
  plaintext: string,
): Promise<string> {
  const s = await getSigner();
  try {
    return await s.nip04Encrypt(thirdPartyPubkeyHex, plaintext);
  } catch (e) {
    throw new Error(redact((e as Error).message));
  }
}

export function closeRelayPool(poolToClose: {
  relays: Map<string, unknown>;
  close: (relays: string[]) => void;
}): void {
  poolToClose.close([...poolToClose.relays.keys()]);
}

export async function closeBunker(): Promise<void> {
  if (signer) {
    // Remote signers may leave the close handshake pending after every event
    // has already been acknowledged and the audit report is safely written.
    // Bound cleanup so a successful outreach run can terminate normally.
    try {
      await Promise.race([
        signer.close(),
        new Promise<void>((resolve) => setTimeout(resolve, 3_000)),
      ]);
    } catch { /* already closed */ }
  }
  if (pool) {
    try { closeRelayPool(pool); } catch { /* nothing */ }
  }
  signer = undefined;
  signerReady = undefined;
  pool = undefined;
  cachedUserPubkey = undefined;
}
