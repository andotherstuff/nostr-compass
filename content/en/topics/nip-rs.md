---
title: 'Buzz Draft NIP-RS: Cross-Device Read State Sync'
date: 2026-10-28
draft: false
---

**Status:** This is a draft proposal specific to the Buzz project. NIP-RS is not an accepted official NIP. The label comes from Buzz project documentation, and the official NIPs repository has not assigned or approved it.

## Purpose

NIP-RS lets the devices of a single user share where that user has read up to. Each installation publishes a `kind:30078` addressable event. Its `d` tag is `read-state:` followed by a random slot ID, and its content is NIP-44 encrypted to the user's own key. The plaintext maps context IDs to timestamp frontiers, each meaning that everything at or before that time has been read. The draft does not publish read receipts and does not reveal what other people have read.

## Limits

Frontiers are best-effort hints about recent activity. They do not form a complete history of read messages. Manual-unread overrides, including tombstone floors, follow a separate durable contract. Loading the full override state depends on relay ordering and capacity behavior that a client cannot fully verify, so an arbitrary relay may not return complete unread state. Context IDs mostly carry meaning only within one client family.

An open pull request, #8639, proposes moving Buzz clients to a `buzz_v1` NIP-11 capability backed by a private authenticated HTTP API, disabled by default. Relays without that capability would keep NIP-RS.

## Primary sources

- [Buzz NIP-RS draft: Cross-Device Read State Sync (pinned revision)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-RS.md)
- [Buzz pull request #8639: read state through a relay capability (open)](https://github.com/block/buzz/pull/8639)

## See also

- [NIP-44](/en/topics/nip-44/)
- [NIP-78](/en/topics/nip-78/)

**Mentioned in:**

- [Newsletter #46: Buzz](/en/newsletters/2026-10-28-newsletter/#buzz)
