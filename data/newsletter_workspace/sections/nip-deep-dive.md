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

writer_model: direct-codex

GATE: PENDING REVIEW
