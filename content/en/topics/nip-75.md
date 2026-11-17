---
title: "NIP-75: Zap Goals"
date: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-75 defines a public fundraising goal that users can zap toward. A goal event states a target in millisatoshis and lists the relays where its [NIP-57](/en/topics/nip-57/) zap receipts should be published. Clients show progress by adding up valid receipts that reference the goal. The signed goal records a request and does not show that any money has arrived.

## How it works

A zap goal is a regular `kind:9041` event, not an addressable one, and its `.content` holds the human-readable description.

The two required tags are:

- `amount`: the target in millisatoshis.
- `relays`: a single tag that holds several relay URLs as separate values.

The optional tags are:

- `closed_at`: a timestamp that sets which receipts count toward the goal.
- `image` and `summary`: display metadata.
- `r` or `a`: a link to an external URL or to an addressable event.
- `zap`: one or more beneficiary pubkeys, using NIP-57 Appendix G zap splits.

## Example event

The event below is a real signed goal retrieved from nos.lol and relay.damus.io. Its id matches the hash of the canonical serialized event, and its BIP-340 signature verifies against the author's pubkey. The content identifies it as a qiqstr QA test and asks readers to ignore it, so it appears here only as a format example and makes no request for donations.

```json
{
  "kind": 9041,
  "id": "499444115e01a11ae3663d594b7bd35f731997b8ede46a86aa9a1184c892e03a",
  "pubkey": "cfdd4a9981b235b8b585480b752fe5be0207be3dfebca0ff5326d7c465646866",
  "created_at": 1794805859,
  "tags": [
    [
      "amount",
      "1000000"
    ],
    [
      "relays",
      "wss://relay.primal.net",
      "wss://vitor.nostr1.com",
      "wss://relay.damus.io",
      "wss://nos.lol"
    ],
    [
      "emoji",
      "100_yeet",
      "https://poster.place/client/emoji/reactions/100_yeet.png"
    ]
  ],
  "content": "qiqstr QA zap goal test, please ignore  :100_yeet:",
  "sig": "1745910f6935c83a2cd1761cb7c905010659bdb6d4999bc86f9aeac0fd4fa017027bd5fa7b000b5ab3242e5963f164bfa24ecda8235e04fd92d3a5c82d172a76"
}
```

- The `amount` of `1000000` millisatoshis is a target of 1,000 sats.
- The single `relays` tag lists four relay URLs.
- The `emoji` tag tells clients how to draw the `:100_yeet:` shortcode in the content and has no payment meaning.
- The event has no `closed_at`, `image`, `summary`, link or beneficiary tags.
- `pubkey` identifies the author and `created_at` is the signed timestamp. `id` is the hash of the canonical serialized event, and `sig` is the author's BIP-340 signature over that id.

## Zapping a goal

To zap a goal directly, a client puts the goal's id in an `e` tag of the zap request. It MUST also copy the goal's relays into the request's `relays` tag, which sends the receipt to the relays where readers of the goal will look for it.

An addressable event, such as a live stream, can point to a goal with a `goal` tag that holds the goal's event id and an optional relay hint. When a user zaps that addressable event, clients SHOULD put the goal id in the zap request's `e` tag. Relay hints only help clients find events; they establish no trust and confirm no payment.

## Counting progress

Progress is the total of zap receipts that reference the goal and pass NIP-57 validation. Validation checks that the bolt11 invoice amount matches the request and that the receipt comes from the right zap provider for the right target. A client should count each receipt once and ignore receipts for other events.

NIP-75 does not define a complete tallying algorithm. A client that reaches only some of the goal's relays may show a total that is too low.

Receipts published after `closed_at` SHOULD NOT count toward progress. This is a counting rule for clients only: wallets can still pay after that time, nothing is refunded, and relays do not treat `closed_at` as a [NIP-40](/en/topics/nip-40/) expiration.

## Safety and privacy

Clients should:

- treat the description as untrusted text and never run HTML from it;
- treat remote images as untrusted content;
- refuse to show a malformed `amount` or timestamp as funded progress;
- put limits on relay subscriptions and media downloads.

Goals are public. Anyone can read a goal's author, description and target, along with whatever matching zap receipts the queried relays return. Each receipt carries the signed zap request, so public receipts can link the key that signed that request, and the zapped amount, to a specific fundraiser. That linkage has limits: the signing key does not prove who paid the invoice, pseudonymous or anonymous zap requests do not name the sender, and a reader sees only the receipts available on the relays they query.

## Implementations

Each entry below describes source code at a pinned commit as of the 2026-11-17 research cutoff; the Amethyst commit is dated that same day. The entries cover code paths only and make no claims about builds, installed versions or live payments.

- **[Amethyst](https://github.com/vitorpamplona/amethyst)** creates goals. At commit `d48764f`, [NewGoalViewModel.kt](https://github.com/vitorpamplona/amethyst/blob/d48764fab810e5c4fb966d19cf4c7a905e38c0f7/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/screen/loggedIn/home/nip75Goals/NewGoalViewModel.kt#L55) accepts a positive whole number of sats and multiplies it by 1,000 to get millisatoshis. It fills `relays` with the user's current outbox relays, can add a deadline, image, summary and website, and then signs and broadcasts the goal. Earlier, in April 2026, [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) added goal progress bars and zap buttons to [NIP-53](/en/topics/nip-53/) live-stream headers.
- **[NosTube](https://github.com/flox1an/nostube)** shows the goal linked to a stream, or the host's newest open goal when the stream has none. It displays the target and receipt-based progress, and it passes the goal's relays to its zap button. At commit `0467076`, its [goal parser](https://github.com/flox1an/nostube/blob/04670761805c5c19c76844658e92e1629cae6960/packages/core/src/zap-goal.ts#L35) checks:
  - the kind;
  - the shape of the id and pubkey;
  - an amount of at least 1,000 millisatoshis.

  The parser allows only HTTPS images, keeps at most ten unique relay hints and does not check signatures itself. [Progress calculation](https://github.com/flox1an/nostube/blob/04670761805c5c19c76844658e92e1629cae6960/packages/core/src/zap-goal.ts#L80) drops receipts after `closed_at` and passes the rest to a receipt validator, whose own code is outside the cited evidence. The [goal bar](https://github.com/flox1an/nostube/blob/04670761805c5c19c76844658e92e1629cae6960/apps/web/src/components/live/ZapGoalBar.tsx#L15) hides the zap button once a goal is closed or when the author has no Lightning address.
- **[Coracle](https://github.com/coracle-social/coracle)** displays goals. At commit `20cd3da`, its note renderer [sends kind 9041](https://github.com/coracle-social/coracle/blob/20cd3daa0bd438c1be68a79f72d6e06578f46e1b/src/app/shared/NoteContent.svelte#L105) to a [goal component](https://github.com/coracle-social/coracle/blob/20cd3daa0bd438c1be68a79f72d6e06578f46e1b/src/app/shared/NoteContentKind9041.svelte#L11) that shows the amount in sats, an optional deadline and the description. The cited code does not establish that Coracle creates goals, tallies receipts or routes zaps to goal relays.

## History

NIP-75 was merged on 2023-09-01 in commit [08bd050598](https://github.com/nostr-protocol/nips/commit/08bd050598), "NIP-75: Zap Goals (#757)", by Alejandro. It builds on NIP-57 zap requests and receipts by adding a target and a way to group zaps under one goal.

---

**Primary sources:**
- [NIP-75 Specification (pinned)](https://github.com/nostr-protocol/nips/blob/999f9bfbf5fe00d5c2711fd24badb4e56748c9bc/75.md)
- [NIP-75 merge commit 08bd050598](https://github.com/nostr-protocol/nips/commit/08bd050598)
- [Amethyst NewGoalViewModel.kt at d48764f](https://github.com/vitorpamplona/amethyst/blob/d48764fab810e5c4fb966d19cf4c7a905e38c0f7/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/screen/loggedIn/home/nip75Goals/NewGoalViewModel.kt#L55)
- [Amethyst PR #2469: live stream top zappers and goal header](https://github.com/vitorpamplona/amethyst/pull/2469)
- [NosTube zap-goal.ts at 0467076](https://github.com/flox1an/nostube/blob/04670761805c5c19c76844658e92e1629cae6960/packages/core/src/zap-goal.ts#L35)
- [NosTube useZapGoals.ts at 0467076](https://github.com/flox1an/nostube/blob/04670761805c5c19c76844658e92e1629cae6960/apps/web/src/hooks/useZapGoals.ts#L64)
- [Coracle NoteContentKind9041.svelte at 20cd3da](https://github.com/coracle-social/coracle/blob/20cd3daa0bd438c1be68a79f72d6e06578f46e1b/src/app/shared/NoteContentKind9041.svelte#L11)

**Mentioned in:**
- [Newsletter #19: Amethyst live stream zap goals](/en/newsletters/2026-04-22-newsletter/#amethyst-ships-marmot-mip-compliance-nip-72-communities-zap-goals-and-moq-audio-rooms)
- [Newsletter #19: NIP Deep Dive on NIP-57](/en/newsletters/2026-04-22-newsletter/#nip-deep-dive-nip-57-zaps)
- [Newsletter #49: NIP Deep Dive on public goals and peer-to-peer orders](/en/newsletters/2026-11-18-newsletter/#nip-deep-dive-public-goals-and-peer-to-peer-orders)

**See also:**
- [NIP-57: Lightning Zaps](/en/topics/nip-57/)
- [NIP-53: Live Activities](/en/topics/nip-53/)
- [NIP-40: Expiration Timestamp](/en/topics/nip-40/)
