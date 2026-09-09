import { verifyEvent } from "nostr-tools/pure";
import type { SignedEvent } from "./bunker.ts";
import { queryNewest, type MinimalEvent } from "./relays.ts";

export type InboxQuery = (relays: string[], filter: { kinds: number[]; authors: string[]; limit?: number }) => Promise<MinimalEvent | undefined>;
export async function resolveNip17Inbox(recipientHex: string, indexerRelays: string[], query: InboxQuery = queryNewest): Promise<string[]> {
  const relayList = await query(indexerRelays, { kinds: [10050], authors: [recipientHex], limit: 1 });
  if (!relayList) throw new Error("recipient has no published NIP-17 kind 10050 DM inbox relay list");
  if (relayList.kind !== 10050 || relayList.pubkey !== recipientHex || !verifyEvent(relayList as unknown as SignedEvent)) throw new Error("recipient kind 10050 DM inbox declaration failed identity/signature validation");
  const relays = [...new Set(relayList.tags.filter((tag) => tag[0] === "relay" && tag.length >= 2).map((tag) => tag[1]).filter((relay) => relay.startsWith("wss://") || relay.startsWith("ws://")))].slice(0, 3);
  if (relays.length === 0) throw new Error("recipient kind 10050 has no valid DM inbox relay URI");
  return relays;
}
