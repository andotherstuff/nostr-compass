import { expect, test } from "bun:test";
import { finalizeEvent, generateSecretKey, getPublicKey } from "nostr-tools/pure";
import { resolveNip17Inbox } from "./inbox-relays.ts";

const secret = generateSecretKey(); const pubkey = getPublicKey(secret);
test("uses only a valid signed kind-10050 inbox declaration", async () => {
  const event = finalizeEvent({ kind: 10050, created_at: 1, tags: [["relay", "wss://inbox.one"], ["relay", "https://bad"], ["relay", "wss://inbox.one"]], content: "" }, secret);
  const query = async (_relays: string[], filter: any) => { expect(filter).toEqual({ kinds: [10050], authors: [pubkey], limit: 1 }); return event; };
  expect(await resolveNip17Inbox(pubkey, ["wss://index"], query)).toEqual(["wss://inbox.one"]);
});
test("fails closed instead of silently falling back to NIP-04", async () => {
  await expect(resolveNip17Inbox(pubkey, ["wss://index"], async () => undefined)).rejects.toThrow("no published NIP-17");
  const other = finalizeEvent({ kind: 10050, created_at: 1, tags: [["relay", "wss://inbox"]], content: "" }, generateSecretKey());
  await expect(resolveNip17Inbox(pubkey, ["wss://index"], async () => other)).rejects.toThrow("identity/signature");
});
