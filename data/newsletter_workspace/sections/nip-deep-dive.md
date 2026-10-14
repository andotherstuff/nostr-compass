## NIP Deep Dive: NIP-36 and NIP-38

### Content warnings before display

[NIP-36, sensitive content](/en/topics/nip-36/), lets authors add a `content-warning` tag to an event, optionally including a reason. A client may hide the content until the reader chooses to reveal it. The [specification](https://github.com/nostr-protocol/nips/blob/master/36.md) leaves the interface to clients and permits supplemental label tags. Adding a warning does not change who can read the event. In a public post, relays and other clients still receive its content.

[Amethyst's warning-tag parser](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt) recognizes the tag and treats a missing or blank reason as unspecified. [Coracle's composer](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/views/NoteCreate.svelte) writes the reason into the tag; its [content view](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte) respects the reader's sensitive-content setting and offers a reveal action. [noStrudel's note view](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx) applies its own warning preference and expanded state before showing the warning interface.

[NIP-36](https://github.com/nostr-protocol/nips/blob/master/36.md) does not encrypt events or require concealment. An absent warning says nothing about the content; clients decide how warnings affect previews and reveal controls.

### Profile status and expiration

[NIP-38, user statuses](/en/topics/nip-38/), uses addressable kind 30315 events. The author, kind and `d` tag identify a status coordinate; `general` and `music` have defined meanings. A newer event replaces the previous status at that coordinate, while a different `d` value remains separate. Empty content clears a status. The [specification](https://github.com/nostr-protocol/nips/blob/master/38.md) also permits references to URLs, profiles, events and addresses.

This signed [NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) event shows an expired general status. The author's original spelling is preserved.

```json
{
  "kind": 30315,
  "id": "8848719ae347e705afbbdbfa3a9f5dcca5dd31c4f39182503bf84de5e362bcf4",
  "pubkey": "f13fdeecd852acebaa77dbc18806a051eaa7ea2214c157a3495982d7535a77f3",
  "created_at": 1791983702,
  "tags": [
    [
      "d",
      "general"
    ],
    [
      "expiration",
      "1791984600"
    ]
  ],
  "content": "I'm listening 📩 on 3 ralys",
  "sig": "b5c98a578773f0199cb833d4b916aac115f2b13474a61e81fdca7316b848d397d7d8ad86d299abee4721f404b7b8a1af26e8c53143457ad14d2fb933b21daf85"
}
```

[Damus's status model](https://github.com/damus-io/damus/blob/4a94f666d7e159e380e10b4dbbb2967d1688709e/damus/Features/Status/Models/UserStatus.swift) handles general and music statuses with expiration. [Nostria's status service](https://github.com/nostria-app/nostria/blob/e861946f4ef4e70f3ec49997a4be27615b9b6f5e/src/app/services/user-status.service.ts) ignores empty or expired values and publishes music statuses using track duration; its normal subscriptions request only general and music types. [Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip38UserStatus/UserStatusEvent.kt) preserves the `d` identifier when clearing a status. Custom types therefore need agreement beyond the shared wire structure.

Statuses are public author statements. They do not prove online presence or that somebody listened to a track. Publishing music or availability can disclose habits, and optional expiration limits stale display without promising deletion. [NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) remains a draft, optional specification, as does NIP-36. Clients can implement either independently, with their display settings determining what readers see.

writer_model: direct-codex

GATE: PASS (source-owner content review; full publication receipts are separate)
