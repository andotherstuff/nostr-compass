import { expect, test } from "bun:test";
import { nip19 } from "nostr-tools";
import { buildPodcastInvitation } from "./podcast-invite.ts";

test("public Logbook invitation visibly mentions and p-tags every unique participant", () => {
  const first = nip19.npubEncode("1".repeat(64));
  const second = nip19.npubEncode("2".repeat(64));
  const event = buildPodcastInvitation(40, "https://nostrcompass.org/en/newsletters/2026-09-16-newsletter/", "https://logbook.example/#/login", [second, first, first], 123);
  const ordered = [first, second].sort();
  expect(event.kind).toBe(1);
  expect(event.created_at).toBe(123);
  expect(event.tags).toEqual(ordered.map((npub) => ["p", (nip19.decode(npub).data as string)]));
  expect(event.content).toContain(`Participants: ${ordered.map((npub) => `nostr:${npub}`).join(" ")}`);
  expect(event.content).toContain("leave a short voice note in Logbook whenever it suits you");
});
