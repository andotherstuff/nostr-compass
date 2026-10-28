---
title: "NIP-CD: Slash Commands"
date: 2026-10-28
draft: false
categories:
  - Protocol
---

NIP-CD defines slash commands. A service publishes a command, and anyone can invoke it as plain text in the content of any Nostr event. NIP-CD is an optional draft specification. It was merged on October 21, 2026 under the title Commands after an earlier proposal, and it was retitled Slash Commands when optional installed-command lists were merged on October 27, 2026.

## How It Works

A kind 31992 event defines a command. Required tags give the trigger word without a slash, a title and a usage description. Ordered `arg` tags declare positional arguments, with types such as pubkey, event, relay, number, enum or text. `s` tags limit which events trigger the command by kind, relay, author or tag. These scopes work like a filter: values of the same type are alternatives, and every type that is present must match.

An invocation is text that starts at index 0 of an event's content, such as `/ban` followed by arguments, and it carries no tags. Adding a qualifier of the form `@nostr:npub1...` targets a single executor. Without a qualifier, every command whose trigger matches and whose scope includes the event can act, so one message may trigger several services.

Client support is optional. Clients may offer autocomplete, argument pickers and rendered chips. They must not require their own support before sending an invocation, and they must send text that fails to parse as ordinary content.

For relay-based groups, definitions and invocations go to the group relay. For broadcast use, definitions go to executor outboxes and invocations go to executor inboxes.

## Installed Command Lists

A user may maintain an optional kind 10992 list, following NIP-51, containing `a` tags that point to kind 31992 command definitions by executor pubkey and `d` value, with an optional relay hint. Clients should use the list for autocomplete and rendered chips. The list records a user's display and discovery preference. It does not authorize an executor, and plain-text invocation works without it. This part of the specification was merged on October 27, 2026 through PR #2525. The merge does not show which clients have implemented the list.

## Primary Sources

- [NIP-CD specification](https://github.com/nostr-protocol/nips/blob/master/CD.md)
- [October 21, 2026 merge of NIP-CD](https://github.com/nostr-protocol/nips/commit/7b5ea85479c0b4efce3c246abefa1dae8f8f91e4)
- [PR #2525 for installed-command lists, merged October 27, 2026](https://github.com/nostr-protocol/nips/pull/2525)
- [October 26, 2026 commit from PR #2525, made on its branch before the merge](https://github.com/nostr-protocol/nips/commit/0142de0384210d69074c089448ef5bc303faef37)
- [October 27, 2026 merge of installed-command lists into NIP-CD](https://github.com/nostr-protocol/nips/commit/400d157c53264b8e58c7b3cdbd21ef546fb7a157)

## Mentioned in
- [Newsletter #46: NIP-CD defines commands invoked as plain text](/en/newsletters/2026-10-28-newsletter/#nip-cd-defines-commands-invoked-as-plain-text) Newsletters

- [Newsletter #46: NIP-CD adds optional installed command lists](/en/newsletters/2026-10-28-newsletter/#nip-cd-adds-optional-installed-command-lists) Newsletters

- [Newsletter #46 (2026-10-28): October 2026, shared query meanings and text-triggered services](/en/newsletters/2026-10-28-newsletter/#october-2026-shared-query-meanings-and-text-triggered-services)

## See Also

- [NIP-01: Basic Protocol](/en/topics/nip-01/)
