## Newly Discovered

### Nail brings email onto Nostr as gift-wrapped events

[Nail](https://github.com/formstr-hq/nail) is an MIT-licensed mail bridge and web client from the Formstr team, the group behind [Formstr](https://github.com/formstr-hq/nostr-forms) and [nostr-calendar](https://github.com/formstr-hq/nostr-calendar). It went to launch on 18 August with [PR #7](https://github.com/formstr-hq/nail/pull/7), a 22-file change that added `k` tags to mail events, key recovery in settings, and a welcome message. Its deployment runs at [mailstr.app](https://mailstr.app), which serves the bridge's own `_smtp` [NIP-05](/en/topics/nip-05/) record, the DNS-based scheme that maps a name at a domain to a Nostr public key.

The mail itself is a Nostr event. The client's [constants](https://github.com/formstr-hq/nail/blob/main/client/src/lib/nostr/constants.ts) define a kind `1301` mail rumor carried inside a kind `1059` [NIP-59](/en/topics/nip-59/) gift wrap, so a message reaches its recipient through the same metadata-hiding envelope used for private direct messages. Delivery relays come from a kind `10050` [NIP-17](/en/topics/nip-17/) inbox list with a kind `10002` [NIP-65](/en/topics/nip-65/) relay list behind it, folders are kind `1985` [NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) labels under a `mail` namespace, and client settings live in a kind `30078` [NIP-78](/en/topics/nip-78/) application-data event. Attachments larger than 60,000 bytes go to [Blossom](/en/topics/blossom/) instead of into the event, because [NIP-44](/en/topics/nip-44/) caps encrypted plaintext at 65,535 bytes. An address is an npub at a domain, and a local domain with no NIP-05 record is treated as a mailbox that does not exist.

The bridge half is a Node LMTP server that runs beside a [mailcow](https://github.com/mailcow/mailcow-dockerized) deployment without patching it: Postfix routes matching domains to the bridge, and the bridge injects replies back through SMTP. That design forces an honest answer to the hardest question in an email bridge, which is what a `From` header proves. Nail's [receive path](https://github.com/formstr-hq/nail/blob/main/client/src/lib/mail/receive.ts) grades every message into one of four provenance states: the configured bridge sealed it and refuses to relay a sender it did not verify upstream, the user sealed it themselves, the address's NIP-05 record resolves to the sealing key, or nothing corroborates the header at all. In that last case the interface falls back to the sealing public key, which is the only identity the event can actually prove. Bridge API calls are authenticated with [NIP-98](/en/topics/nip-98/) signed HTTP events.

### nwc-kit keeps a wallet-connect client on one encryption version

[nwc-kit](https://github.com/forgesworn/nwc-kit) is a TypeScript client for [NIP-47](/en/topics/nip-47/) Nostr Wallet Connect, published under the MIT license on 13 August. Its stated scope is narrow in a way that is itself the design: NIP-47 core only, [NIP-44](/en/topics/nip-44/) version 2 encryption only with no fallback to the older NIP-04 scheme, and authenticated wallet responses. Refusing to decrypt an older-format response removes the downgrade path that a dual-scheme client has to keep open.

Two applications adopted it within a day of publication. [Bray 3.0.0](https://github.com/forgesworn/bray/releases/tag/v3.0.0) and [Toll Booth 6.0.0](https://github.com/forgesworn/toll-booth/releases/tag/v6.0.0) both list the adoption as a breaking change, and Toll Booth deleted its own payer credential flow in the process. The library reached [version 0.1.7](https://github.com/forgesworn/nwc-kit/releases/tag/v0.1.7) the following day.

### Glow stores wallet labels on relays under a passkey-derived identity

[Glow](https://breez.technology/glow/) is a Breez self-custodial Lightning wallet. Passkey login derives a Nostr identity, and wallet labels list from and save to relays under that identity, with byte-identical duplicates collapsed across partial relay coverage.

GATE: PASS
