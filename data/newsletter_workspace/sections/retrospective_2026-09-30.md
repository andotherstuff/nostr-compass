## Six Years of Nostr Septembers

The last September issue is a chance to trace how Nostr moved from sketches to a larger set of interoperable tools. A [2021 ride-matching prototype](https://github.com/arcbtc/buber/commit/7a66d400f2) used signed events to coordinate a service; five years later, [identity proof wording](https://github.com/nostr-protocol/nips/commit/0046368a7) and [list-kind collisions](https://github.com/nostr-protocol/nips/commit/6631b3eb1) are the sort of details maintainers are resolving. In between, clients learned to present conversations, media and recovery in ways ordinary people can use. The dated sources below show stages in that progression. They do not establish that every experiment launched or that each old design remains recommended.

### September 2021: early experiments with useful shapes

A [September 4 BUber commit](https://github.com/arcbtc/buber/commit/7a66d400f2) explored a taxi-matching concept using Nostr events. It showed how a signed, relay-carried request could coordinate people without assigning the whole service to one server. The source is a concept, and it does not establish a launched ride service.

Later that month, [Loquaz's September 23 source](https://github.com/emeceve/loquaz/commit/d885d93d22) offered a desktop chat prototype. That was another early attempt to make relay messages feel like an ordinary application. The source does not establish finished end-to-end encryption or a production messenger; the lasting thread is the search for a usable conversation interface on top of simple events. BUber tested ride matching, and Loquaz tested chat; both used signed events before common client patterns had settled. Those trials laid out two recurring problems for later clients: coordinating through relays and presenting events as a usable conversation.

### September 2022: chat and delegated actions enter the specifications

The [September 10 NIP-28 change](https://github.com/nostr-protocol/nips/commit/3423a6dfb) described public chat channels with messages and metadata that clients could interpret together. [NIP-28](/en/topics/nip-28/) made a shared room an explicit protocol subject and gave clients a common channel convention.

On September 23, [NIP-26](/en/topics/nip-26/)'s [delegated-signing text](https://github.com/nostr-protocol/nips/commit/b62aa418d) documented a way for one key to authorize another to sign limited events. It captured an important 2022 design question: how to use a Nostr identity without handing the primary key to every application. [NIP-26 is now marked unrecommended](https://github.com/nostr-protocol/nips/blob/master/26.md), so this is a record of an experiment, not advice for new integrations. Its later status shows how the signing model has moved: a specification can preserve a useful problem statement even when the proposed answer is retired.

### September 2023: clients grow up around relay discovery and metadata

Damus is a Nostr social client. Its [September 21 changelog](https://github.com/damus-io/damus/blob/master/CHANGELOG.md#16-18---2023-09-21) recorded work on its local Nostr database, search, and hashtag navigation. Those changes made a busy social feed easier to browse and recover on a phone; the dated changelog is evidence for that client release, not for every later Damus capability.

The protocol details were moving too. A [September 26 change](https://github.com/nostr-protocol/nips/commit/44c21c9d8) to [NIP-24](/en/topics/nip-24/) clarified optional profile metadata fields, while [NIP-65's September 29 change](https://github.com/nostr-protocol/nips/commit/3b5d3ca67) addressed relay URI normalization and deduplication. [NIP-65](/en/topics/nip-65/) tells clients how to publish the relays they use for reading and writing; consistent URI treatment helps those lists point to the same relay even when strings differ in harmless ways. That small convention moved client design toward reliable discovery: finding a person's events depends on knowing where they are published.

### September 2024: posts acquire richer context

[Damus's September 22 release notes](https://github.com/damus-io/damus/blob/master/CHANGELOG.md#1101---2024-09-22) described support for [NIP-84](/en/topics/nip-84/) highlights and comments. NIP-84 gives readers a way to quote and discuss a passage of long-form material. The client work shows how a protocol idea became something people could use while reading.

Meanwhile, [NIP-34](/en/topics/nip-34/) received a [September 20 change](https://github.com/nostr-protocol/nips/commit/ea36ec9ed) refining issue subjects and labels for git collaboration over Nostr, and [NIP-73](/en/topics/nip-73/) received a [change that day](https://github.com/nostr-protocol/nips/commit/79786bb7b) refining external content identifiers. These are separate specification changes: one helps a repository's issues retain structure, while the other lets an event refer to material outside Nostr. Both extend the meaning a client can preserve when content travels between communities, repositories and other media.

### September 2025: access controls and payment context become more precise

A [September 6 NIP-42 revision](https://github.com/nostr-protocol/nips/commit/4c5d5fff9) addressed multi-user relay authentication. [NIP-42](/en/topics/nip-42/) lets a relay challenge a client to prove which Nostr key is making a request; the update mattered for services that serve more than one authenticated account through the same connection.

A [September 15 NIP-47 update](https://github.com/nostr-protocol/nips/commit/400d975da) added optional payment metadata to Nostr Wallet Connect requests. [NIP-47](/en/topics/nip-47/) lets an app ask a wallet to perform actions over Nostr. More context can make a wallet interaction understandable, but the metadata may expose payer details, so clients and wallets still need to treat it as sensitive. The change illustrates how interoperability work now included what a recipient can learn, not just whether a request can be delivered.

### September 2026: interoperability details meet public identity

This September, a [merged NIP-51 change](https://github.com/nostr-protocol/nips/commit/6631b3eb1) moved the follow-set event kind away from a collision. [NIP-51](/en/topics/nip-51/) defines lists that a person can maintain and share; unique event kinds let clients distinguish one list type from another. An earlier Compass issue discussed the proposal, while the September merge is the status change.

A second [merged change to NIP-39](https://github.com/nostr-protocol/nips/commit/0046368a7) clarified proof text and added more ways to associate an external account with a Nostr identity. [NIP-39](/en/topics/nip-39/) is about checkable identity claims, not a central identity registry. Together, the two merges show current protocol work concentrating on the small details that determine whether independent clients interpret the same identity and list events correctly. They also show a shift from inventing new event categories toward reducing ambiguity in existing ones.

Across these six Septembers, the pattern is a progression from proving that a [signed event can describe an application request](https://github.com/arcbtc/buber/commit/7a66d400f2) to asking how a [client verifies a claim about a person](https://github.com/nostr-protocol/nips/commit/0046368a7). The old prototypes matter because they expose the questions that later specifications and clients had to answer: who signs, where an event is found, what it means, and how someone knows whether to trust it. That is also why a small, precise protocol correction can matter as much as a new interface.
