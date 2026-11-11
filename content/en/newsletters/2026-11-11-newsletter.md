---
title: 'Nostr Compass #48'
date: 2026-11-11
publishDate: 2026-11-11
draft: false
type: newsletters
---

This week [Marmot](/en/topics/marmot/), the encrypted-group messaging protocol, ran through the [bitcoin++ Seoul hackathon](/en/newsletters/2026-11-11-newsletter/#marmot-projects-at-bitcoin-seoul), where the winning project coordinated hardware signers over a Marmot group. [Nostur](/en/newsletters/2026-11-11-newsletter/#nostur) added polls, which this issue's [deep dive on NIP-88](/en/newsletters/2026-11-11-newsletter/#nip-deep-dive-nip-88-polls) (Nostr polls) explains. [Chama](/en/newsletters/2026-11-11-newsletter/#chama) changed how trades lock escrow, and [Route96](/en/newsletters/2026-11-11-newsletter/#route96) merged media-server security fixes. [LNbits](/en/newsletters/2026-11-11-newsletter/#lnbits) operators should upgrade and rotate keys after a vulnerability put funds at risk. Elsewhere, relays gained a [rate-limit backoff hint](https://github.com/nostr-protocol/nips/pull/2498), and wallet-connection, Concord and Marmot specs moved.

## Top Stories

### Marmot projects at bitcoin++ Seoul

[bitcoin++ Seoul](https://btcpp.dev/seoul), a privacy-themed Bitcoin developer conference held 5 and 6 November, ran a hackathon whose [gallery](https://btcpp.dev/seoul/hackathon) lists 20 projects, several of them built on [Marmot](/en/topics/marmot/) encrypted groups. [BlackIce](https://github.com/rademenezbtc/blackice) took first place and the Best Use of the Marmot Protocol award. In it, Frostsnap hardware wallets jointly sign Bitcoin payments to silent-payment addresses (reusable addresses that keep each payment private), coordinating over a Marmot group. [mdk squared](https://github.com/samthomson/mdk-squared) earned an honorable mention for controlling mining air purifiers through a Marmot channel, and [iLCHON](https://github.com/dongguri-jun/ilchon), which matches bitcoin trades only between people who have met, won Best Beginner Hack.

Other Marmot entries include [Kimchi](https://github.com/ye0man/kimchi) for splitting bills with [Cashu](/en/topics/cashu/) ecash, [SatsRoadMarket](https://github.com/shroominic/satsroadmarket) for private marketplace negotiation, [Quiet Ledger](https://github.com/murdawkmedia/quiet-ledger) for invoices, an open [pull request adding chat to Shroud](https://github.com/CypherCommons/shroud/pull/233), a silent-payment wallet, and [kiss-bdk](https://github.com/kkdao/kiss-bdk), a multi-signer silent-payment wallet. Most depend on marmot-ts 0.9.0, the TypeScript Marmot library. All are [hackathon code](https://github.com/marmot-protocol/awesome-marmot/compare/57d5bb868aa7...e0a960475372): test networks only, unaudited, often with keys or group state stored unencrypted. White Noise, the Marmot messenger, rejects mdk squared's KeyPackages, the keys a device publishes so others can add it to a group.

## Tagged Releases

### LNbits

[LNbits](https://github.com/lnbits/lnbits), the Lightning wallet and accounts server, shipped [v1.7.0](https://github.com/lnbits/lnbits/releases/tag/v1.7.0) on 10 November as a security release, then [v1.7.1](https://github.com/lnbits/lnbits/releases/tag/v1.7.1) the next day to rotate auth keys. The project's [upgrade guidance](https://news.lnbits.com/news/lnbits-1-7-0-security-update) says a vulnerability found on 8 November affects every earlier version and that funds on those versions are at risk of theft. Upgrading alone does not revoke access an attacker may already hold, so operators should also reset user wallet keys, replace funding-source credentials and recreate connections for extensions such as the [Nostr Wallet Connect](/en/topics/nip-47/) provider, LNDHub and Bolt Cards. Full exploit details will follow in a separate report. The same release ships [NIP-17](/en/topics/nip-17/) notifications, covered when [the change merged](/en/newsletters/2026-10-28-newsletter/), alongside two-factor login, on-chain wallets and BOLT12 payments.

### Nostur

Nostur, an iOS and macOS client, adds polls in [1.35.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.35.0). Users can create polls, vote, find polls in Search and filter results by everyone, Web of Trust or follows. Polls follow [NIP-88](/en/topics/nip-88/) (Nostr polls), and Nostur also keeps your own polls and their loaded votes locally in case relays drop them. The release also adds an in-app browser where Nostr web apps can request signatures from your account, with approval prompts and per-site permissions, so the private key is not shared.

### Monostr

Monostr, a Nostr client built around Monero tips, builds in Tor in [v0.34.0](https://github.com/schmidt1024/monostr/releases/tag/v0.34.0). It is off by default. When switched on, relays, images, uploads and the tip watcher see a Tor exit node, not your IP address. Onion relays can join your relay list.

### Chama

Chama, a peer-to-peer bitcoin trading app with ecash escrow, closes the final open item from its security audit in [v6.4.34](https://github.com/jesuspirate/chama/releases/tag/v6.4.34). For trades created from 1 December 2026, [the funder's app sends only its own share of the escrow](https://github.com/jesuspirate/chama/pull/116) and sends the other two after the counterparty accepts, so a refused lock no longer hands the seller and arbiter two of three shares. Until the counterparty accepts, the funder can reclaim the sats. The withheld shares only apply when the counterparty runs 6.4.34 or later; otherwise the app writes the old lock.

### Zapstore

Zapstore, the Nostr-based Android app store, shipped [2.0.2](https://github.com/zapstore/zapstore/releases/tag/2.0.2) through [2.0.4](https://github.com/zapstore/zapstore/releases/tag/2.0.4) in three days. Listings now say "Claimed by the developer", "Unclaimed app" or "From the catalog" in place of a raw ownership proof. When Vertex, a [Web of Trust](/en/topics/web-of-trust/) scoring service, will not answer a personal trust check, Zapstore falls back to people you follow who follow that key.

### Manent

Manent, a private notes app that stores encrypted notes on Nostr relays, released [v3.1.0](https://github.com/dtonon/manent/releases/tag/v3.1.0). Tall images and videos in the note list are capped at 60% of the screen height with space reserved before loading, so the list stops jumping. Voice notes on Linux no longer need ffmpeg, because the app writes the WAV file itself.

### Streets

Streets, a Japanese web client, separates relay budgets in [v1.24.0](https://github.com/eyemono-moe/streets/releases/tag/v1.24.0). The 30-connection limit now applies only to outbox relay selection, the model where a client reads each author's posts from the relays that author lists under [NIP-65](/en/topics/nip-65/) (relay list metadata). Relays you name explicitly no longer count against it, and total connections are capped at 60.

### NoorNote

NoorNote, a desktop Nostr client, checks Lightning invoices before paying a zap in [v1.9.10](https://github.com/77elements/noornote/releases/tag/v1.9.10). The app now decodes the invoice the recipient's server returns and [refuses one that asks for more than the requested amount](https://github.com/77elements/noornote/pull/8). It also [stops sending zap requests to non-https callback URLs](https://github.com/77elements/noornote/pull/7), where the signed request would land in server logs. A description-hash check that had made many [NIP-57](/en/topics/nip-57/) (Lightning zaps) payments fail now only logs a warning. The release also adds expiring notes under [NIP-40](/en/topics/nip-40/) (expiration timestamps).

### Infans

Infans, an Android baby tracker that backs up and syncs between parents through encrypted Nostr events, fixes disappearing timers in [v2.4.3](https://github.com/TurkeyNostr/infans/releases/tag/v2.4.3). When a relay reconnected and replayed an old stop event, a sleep or feeding timer could die on one parent's phone while still running on the other's. The app now tolerates 60 seconds of clock skew and drops duplicate events.

### Amber

Amber, an Android app that holds Nostr keys and signs for other apps, adds a local relay in [v7.0.0-pre3](https://github.com/greenart7c3/Amber/releases/tag/v7.0.0-pre3), a pre-release. When switched on under Settings → Relays (it is off by default), a WebSocket relay at ws://127.0.0.1:7777 lets [NIP-46](/en/topics/nip-46/) (remote signing) clients on the same phone reach the bunker without public relays. Desktop users now approve or deny relay authentication requests per relay, with an "All relays" choice and a whitelist of clients. One account failing relay authentication no longer aborts it for the others.

### Keep Android

Keep Android, a [FROST](/en/topics/frost/) threshold signer, fixes several leaks in [v1.4.0](https://github.com/privkeyio/keep-android/releases/tag/v1.4.0). Its NIP-46 bunker lists up to 100 connected apps. When that list was full, the oldest app was evicted but its approvals and connect secret stayed live; a full list now refuses the new app. Approving an app's own [NIP-55](/en/topics/nip-55/) (Android signer) request could also approve a peer's co-sign request for the same event without a prompt. An unreadable proxy setting no longer falls back to a direct connection that exposes your IP address.

### nostr-social-graph

nostr-social-graph, a library that builds follow and mute graphs for [Web of Trust](/en/topics/web-of-trust/) scoring, changes its snapshot format in [v4.0.0](https://github.com/mmalmi/nostr-social-graph/releases/tag/v4.0.0), after [Newsletter #45](/en/newsletters/2026-10-21-newsletter/) covered 3.0.0. Snapshots now keep follow and mute event IDs, timestamps, empty lists and completeness. Older readers cannot load v4, so consumers should upgrade before importing new snapshots. An optional `publicGraphSync` entry adds bounded catch-up over [NIP-77](/en/topics/nip-77/) (Negentropy set reconciliation), with signature verification and a fallback to ordinary requests. On 10 November, [v4.1.0](https://github.com/mmalmi/nostr-social-graph/releases/tag/v4.1.0) updates follow distances in place after each follow and unfollow, so callers no longer recompute them. Lookups of unknown keys also stop growing memory.

### MDK

MDK, the SDK and runtime for [Marmot](/en/topics/marmot/) encrypted groups, released [v0.15.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.15.0) together with [MarmotKit](https://github.com/marmot-protocol/mdk/releases/tag/marmotkit-v0.15.0) bindings for iOS, macOS and Android. Creating a group or inviting someone now adds every device of each account. It follows last week's nightlies, covered in [Newsletter #47](/en/newsletters/2026-11-04-newsletter/). A group copy that became unrecoverable rejoins through an admin device. New groups whose founding devices all run 0.15 cannot invite 0.14 clients, and migrated databases cannot be downgraded, so the [release notes](https://github.com/marmot-protocol/mdk/blob/v0.15.0/docs/release/0.15.0.md) advise keeping a copy first.

### Vector

Vector, a private messenger built on Nostr, shipped [v0.5.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.5.0) and [v0.5.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.5.1). Deleting a DM now removes your copies from relays with your own key and asks the recipient's Vector to delete theirs. When the relays a contact reads DMs from could not be reached, DMs fell back to your own relays and showed as Sent; they now fail and say why. v0.5.1 stops Vector's defaults from replacing a DM relay list at login. Upgrading deletes communities still on version 1 of Concord, Vector's encrypted-community protocol, along with their history.

## In Development

### Route96

Route96, a media server for [Blossom](/en/topics/blossom/) (hash-addressed media storage) and [NIP-96](/en/topics/nip-96/) (HTTP file storage) uploads, merged security fixes on 8 November that are not yet in a tagged release. The server now [verifies the signature on a Nostr auth event before reading its tags](https://github.com/v0l/route96/pull/106). It also [refuses playlist and reference media before handing an upload to ffmpeg](https://github.com/v0l/route96/pull/109), which could otherwise make the server fetch local files or internal URLs. Uploaded files are now [served with browser content-sniffing disabled and a sandboxing Content-Security-Policy](https://github.com/v0l/route96/pull/102). [Newsletter #45](/en/newsletters/2026-10-21-newsletter/#route96) covered its path and hash uploads.

## New Projects

### SplitNut

[SplitNut](https://github.com/rademenezbtc/splitnut), from BlackIce's author, runs a stock [Cashu](/en/topics/cashu/) mint whose signing keys are split two-of-three across guardians who coordinate in a [Marmot](/en/topics/marmot/) group. The repository appeared on 7 November and builds on MDK 0.8.0. It is an unaudited experiment, so keep real funds out of it.

### Moranduba

[Moranduba](https://github.com/vzsoares/moranduba) is a Flutter group chat with end-to-end encrypted video calls and screen sharing, built on Marmot. It vendors MDK 0.8.0 with three local patches and shipped [v0.5.0 through v0.8.0](https://github.com/vzsoares/moranduba/releases) between 8 and 9 November.

## Protocol and Spec Work

### NIP-01 relays can tell clients how long to back off

A [merged NIP-01 change](https://github.com/nostr-protocol/nips/pull/2498) adds an optional last parameter to the `OK` and `CLOSED` relay messages in [NIP-01](/en/topics/nip-01/) (the base relay protocol). The parameter's meaning depends on the message prefix, and only `rate-limited` defines one: a positive integer of milliseconds, such as `"2500"`, that the client should wait before sending the same message type again. The value may be approximate, and its absence does not mean the client may retry at once. Its authors chose a delay over a timestamp to avoid clock skew.

### NIP-47 logout method proposed

An open pull request adds a [`logout` method](https://github.com/nostr-protocol/nips/pull/2537) to [NIP-47](/en/topics/nip-47/), the Nostr Wallet Connect spec for controlling a wallet over Nostr. After a logout, the wallet must not honor further requests from that connection key and should answer them with an `UNAUTHORIZED` error. Clients should send it when the user disconnects. The stated motivation is limiting damage when a connection URL leaks.

### Logout mirrored in the NWC specs repository

The same author opened a matching [logout draft in the Nostr Wallet Connect specs](https://github.com/nostr-wallet-connect/nwc/pull/13). It goes further: the wallet must durably revoke the key before replying and reject any later request signed by it, including backdated ones. Every connection gets permission to call it, and wallets must list it among their advertised methods, so a client can tell whether disconnecting revokes the key.

### Push registration for wallet notifications

A separate open NWC draft defines [`register_push` and `unregister_push`](https://github.com/nostr-wallet-connect/nwc/pull/15), letting a client hand the wallet service a Web Push endpoint, which UnifiedPush distributors can also serve. The service then delivers payment notifications directly, without holding push-provider credentials.

### Concord merges Roles, private channels and voice

Concord is a protocol for encrypted Nostr communities. Its [Channels, Roles and Voice](https://github.com/concord-protocol/concord/pull/25) proposal, covered in the October 21 issue ([Newsletter #45](/en/newsletters/2026-10-21-newsletter/)) while still open, has now merged. It adds Discord-style roles, including an `@everyone` role, ranked in order; channel categories; per-channel permissions; private channels encrypted to a channel key; peer-to-peer voice; timeouts; and raid lockdown. The author names Vector as the reference implementation.

### Concord joins authenticate the community root

A [Concord proposal](https://github.com/concord-protocol/concord/pull/23) covered in the August 19 issue ([Newsletter #36](/en/newsletters/2026-08-19-newsletter/)) has now merged. A joining member must decrypt the community's founding metadata with the keys it received, and confirm it came from the owner, before saving the join. The author says Vector and Armada, another Concord client, already did this, so it was not a live vulnerability.

### Marmot: moved devices keep trusting the old group until the first Commit

[Marmot](/en/topics/marmot/), the end-to-end encrypted group messaging protocol built on MLS and Nostr, merged five device-group and departure changes between 4 and 9 November. A user's linked devices share an MLS group of their own, the device group. Under [the first change](https://github.com/marmot-protocol/marmot/pull/498), a device moving to a new device group keeps its original group trusted until its first authenticated Commit, the MLS message that changes membership or keys, is selected in the destination. A confirmed Welcome alone does not switch trust.

### Marmot: reset a local device group without losing chats

A device link can disappear from a device group's roster. The [fix](https://github.com/marmot-protocol/marmot/pull/499) is a user-controlled local reset followed by fresh code-confirmed pairing. Chats, account identity and shared-state authority survive. The reset discards this device's old continuity, so a mistaken reset can lose it.

### Marmot: inactive sibling devices

After 30 days of caught-up inactivity, a device [marks a sibling device `inactive`](https://github.com/marmot-protocol/marmot/pull/500). At 90 days, unless the user has turned on "keep while inactive", it removes the sibling with an ordinary removal Commit. By then the sibling's KeyPackages, the keys a device publishes so others can add it, have usually expired.

### Marmot: last active admin cannot leave

Under a [departure rule](https://github.com/marmot-protocol/marmot/pull/501), a leaving admin repeats its step-down while another admin remains. If it is the last active admin, the leave stays blocked in a `Leaving` state and generates nothing new. The user can cancel a blocked leave locally.

### Marmot: admins step down before leaving

A refused or lost step-down could stall a leave. A [follow-up](https://github.com/marmot-protocol/marmot/pull/502) puts a departing admin into `Leaving` once it durably records the leave, before step-down, and sends its SelfRemove once it is off the admin list. Clients must not accept a leave from the last active admin.

### Marmot drafts one-shot agent decisions

An open draft [specifies one-shot agent decisions](https://github.com/marmot-protocol/marmot/pull/503): a software agent in an encrypted group asks one question and gets one answer, as ordinary encrypted group messages. The agent posts a request with options, the answer is a separate message, and the runtime confirms it accepted that answer with a receipt.

### NIP-D9 proposes events that resist deletion

An open [NIP-D9 proposal](https://github.com/nostr-protocol/nips/pull/2531) lets an author mark a regular event with a `no_delete` tag, exempting it from that author's own [NIP-09](/en/topics/nip-09/) (deletion requests) and [NIP-62](/en/topics/nip-62/) (request to vanish) requests, even if the request arrives first. Expiration still applies, and replaceable kinds and profiles are not eligible. Supporters pointed to whistleblowers whose keys could be seized and used to erase their posts. Two commenters objected in the thread, one arguing that relays cannot act as a stateful database and the other asking about users who want everything deleted. It remains unmerged and contested.

## NIP Deep Dive: NIP-88 (Polls)

[NIP-88: Polls](/en/topics/nip-88/) lets anyone post a public poll that any client can count from events on ordinary relays, without a poll service. It builds a poll from two event kinds: a kind 1068 poll and kind 1018 responses. The [spec text](https://github.com/nostr-protocol/nips/blob/master/88.md) is marked draft and optional. It first landed from [PR #1346](https://github.com/nostr-protocol/nips/pull/1346), was removed on the same September 2024 day it was renumbered to 88, and returned through [PR #1507](https://github.com/nostr-protocol/nips/pull/1507), merged in January 2025. Later commits to the file were editorial.

### A poll and a vote

In the [spec](https://github.com/nostr-protocol/nips/blob/master/88.md), the question sits in `content`. Each `option` tag pairs a short alphanumeric ID with a label, `relay` tags name where responses should go, `polltype` picks `singlechoice` (the default) or `multiplechoice`, and `endsAt` sets the cutoff as a Unix timestamp. A response carries an `e` tag for the poll and one `response` tag per chosen option ID.

The poll below was posted from [Amethyst](https://github.com/vitorpamplona/amethyst), an Android Nostr client, and retrieved from wss://nos.lol, and its ID and signature verify under [NIP-01](/en/topics/nip-01/) rules. Its `endsAt` of 1794808500 closes it at 05:55 UTC on 16 November 2026. It also carries a [NIP-13](/en/topics/nip-13/) `nonce` tag with a difficulty target of 20, and the ID begins with 21 zero bits. NIP-88 lists proof of work only as an optional curation signal for results.

```json
{
  "kind": 1068,
  "id": "000006187b131293f1de84a41c39dfac9c8bbd88300d176154cf141e15440d0f",
  "pubkey": "7055fc42c9a638ab56ad057016a2deface97b5eece31a3a7a46727ad847899e5",
  "created_at": 1794291666,
  "tags": [
    [
      "polltype",
      "singlechoice"
    ],
    [
      "option",
      "1Pb66M",
      "coke/pepsi"
    ],
    [
      "option",
      "hIy0lG",
      "sprite/starry 🍋‍🟩🍋"
    ],
    [
      "option",
      "HAxvzm",
      "MOUNTAIN DEW BAJA BLAST"
    ],
    [
      "option",
      "xEn4mB",
      "orange soda (fanta/crush/etc) 🍊"
    ],
    [
      "option",
      "0Dnt8f",
      "root beer"
    ],
    [
      "option",
      "tUI7MV",
      "other/comment 💬"
    ],
    [
      "relay",
      "wss://nos.lol/"
    ],
    [
      "relay",
      "wss://relay.pleb.one/"
    ],
    [
      "relay",
      "wss://basspistol.org/"
    ],
    [
      "relay",
      "wss://nostr21.com/"
    ],
    [
      "relay",
      "wss://relay.letsfo.com/"
    ],
    [
      "endsAt",
      "1794808500"
    ],
    [
      "t",
      "FunPoll"
    ],
    [
      "t",
      "funpoll"
    ],
    [
      "t",
      "Polls"
    ],
    [
      "t",
      "polls"
    ],
    [
      "t",
      "Poll"
    ],
    [
      "t",
      "poll"
    ],
    [
      "client",
      "Amethyst"
    ],
    [
      "nonce",
      "2007re",
      "20"
    ]
  ],
  "content": "secret new weekly poll 📊\n\npick your soda 🥤\n\n\n\n#FunPoll #Polls #Poll",
  "sig": "cf652a538cd3dcc335a081d86d9791f3e2e927f416ddd06a20ec1b1b94e8e35670b15b7ecd26557a0f2ba580381b07f569cb4cb56bd9b65e183a79867fbd4b5f"
}
```

The response below, also verified, votes for option `hIy0lG` 156 seconds after the poll was created. Its `e` tag adds a relay hint and the poll author's pubkey, and a `p` tag names that author. The [spec example](https://github.com/nostr-protocol/nips/blob/master/88.md) uses a bare `e` tag, and clients differ on whether they add `p`.

```json
{
  "kind": 1018,
  "id": "b5721199f633a57c71684281cfca62e6536b685e6c86577ee030acf51e352ad1",
  "pubkey": "1408bad049bab8a38b976075affe413c3521bbeef62cc4ce3555299f4971f2ca",
  "created_at": 1794291822,
  "tags": [
    [
      "e",
      "000006187b131293f1de84a41c39dfac9c8bbd88300d176154cf141e15440d0f",
      "wss://basspistol.org/",
      "7055fc42c9a638ab56ad057016a2deface97b5eece31a3a7a46727ad847899e5"
    ],
    [
      "p",
      "7055fc42c9a638ab56ad057016a2deface97b5eece31a3a7a46727ad847899e5",
      "wss://nos.lol/"
    ],
    [
      "response",
      "hIy0lG"
    ],
    [
      "client",
      "Amethyst"
    ]
  ],
  "content": "",
  "sig": "d87759ad690a3aba378dfe36045935d57cb3ef0804b47ef31ce16234247343f73a14ba6685a2517571467f8fee30aed7852034090e6a36d3ac93e5bffce84fad"
}
```

### What the spec says about counting

[NIP-88](https://github.com/nostr-protocol/nips/blob/master/88.md) tells a client to count one response per pubkey, choosing the one with the largest timestamp within the poll limits. For `singlechoice`, the first `response` tag is the vote. For `multiplechoice`, the first tag naming each ID counts. The spec's example query sets `until` to the poll's end time and advises poll authors to pick relays that reject backdated events and ignore deletion requests for votes. It does not say how to break a tie between two responses with the same timestamp.

### Tradeoffs and zap polls

Every vote is a signed public event, so NIP-88 offers no ballot secrecy. Tallies depend on which relays a client reads, and nothing stops one person with many keys from voting many times. The spec's [curation section](https://github.com/nostr-protocol/nips/blob/master/88.md) lets clients count only voters in a kind 30000 follow set, or weigh responses with proof of work and Web of Trust scores.

Kind 6969 zap polls are an older experimental format, never merged, in which votes are zaps; today NIP-69 is peer-to-peer trading. Amethyst and Wisp still handle them, and Wisp [tallies zap receipts per option](https://github.com/barrydeen/wisp-ios/blob/914febaf597fc044a680ead632931009b21d641a/PollTallyRepository.swift#L268-L274).

### How four clients tally

Amethyst's [PollResponsesCache at commit 4fb2919](https://github.com/vitorpamplona/amethyst/blob/4fb29192d502542f714e1526ac229378617922fe/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/model/nip88Polls/PollResponsesCache.kt#L169-L220) keeps one vote per author and replaces it only with a strictly newer response. [PollTallyPolicy](https://github.com/vitorpamplona/amethyst/blob/4fb29192d502542f714e1526ac229378617922fe/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/model/nip88Polls/PollTallyPolicy.kt#L57-L63) drops responses created after `endsAt` and, as an extra rule, responses older than the poll itself. Single-choice tallies [read only the first declared option](https://github.com/vitorpamplona/amethyst/blob/4fb29192d502542f714e1526ac229378617922fe/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/model/nip88Polls/PollTallyPolicy.kt#L77-L81). Polls get proof of work only when the account's NIP-13 settings enable mining.

noStrudel's [poll helper at commit 25cb0e2](https://github.com/hzrd149/nostrudel/blob/25cb0e27af39eed10245680a7c28c4f0b49eb731/src/helpers/nostr/polls.ts#L21-L37) also keeps the latest vote per pubkey and skips late responses. noStrudel departs from the spec on single choice. Its [applesauce helper](https://github.com/hzrd149/applesauce/blob/961979353a39dded606cd1a8eeedaf66c46b272c/packages/common/src/helpers/poll.ts#L86-L99) discards any response naming more than one valid option, where the spec counts the first.

Coracle tallies through [welshman's Poll reader](https://github.com/coracle-social/welshman/blob/aa655bd6aae025bcc082af08c65c76cbc80a6432/packages/domain/src/kinds/Poll.ts#L51-L79), from Coracle's Nostr toolkit, which takes the first tag and the latest vote per pubkey. In [Coracle's poll view](https://github.com/coracle-social/coracle/blob/81581be7d1dec59e274dea2d65096ad5774c7eab/src/app/shared/NoteContentKind1068.svelte#L26-L31), `endsAt` disables voting, but the response query has no `until` and the tally applies no cutoff, so a late re-vote could replace an on-time one. That reading comes from source, not a live test.

Wisp for iOS [keeps the latest vote per voter](https://github.com/barrydeen/wisp-ios/blob/914febaf597fc044a680ead632931009b21d641a/PollTallyRepository.swift#L206-L232) and drops late votes only when it has already cached the poll event.

All four follow the spec's [latest-vote-per-pubkey rule](https://github.com/nostr-protocol/nips/blob/master/88.md), so the poll above should show the same winner in each while every voter casts one clean vote before the deadline. Late responses and single-choice responses with extra tags are where the totals can split. These descriptions reflect source at the linked commits, not confirmed release behavior.

This week [Nostur 1.35.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.35.0) shipped poll creation and voting on iOS and macOS, described under [Tagged Releases](/en/newsletters/2026-11-11-newsletter/#nostur).
