---
title: "NIP-FB: Scheduled Tasks"
date: 2026-11-18
draft: false
categories: ["NIPs"]
---

NIP-FB is a proposed NIP for scheduled tasks. It is open and unmerged as nostr-protocol/nips#2546 and is not an accepted NIP. It is a separate proposal from nostr-protocol/nips#2545. Recurring work is stored as Nostr events, and the user's own devices or an optional runner agree on which one performs each run.

A task is a kind 34817 event. Its schedule is a POSIX cron expression evaluated in an IANA time zone. Private task state records claims and completions. Each device must opt in before it executes tasks. To claim a run, a device first waits a random delay. It then reads from and writes to a majority of the user's NIP-65 write relays and waits 20 seconds for competing claims to settle. The draft also has rules for daylight saving transitions and for runs that were missed.

An optional public runner, named in a `p` tag, can decrypt and execute a task. The runner signs its output with its own key and must confirm that the requester authorized it.

The claim process lowers the chance of duplicate runs. The proposal does not guarantee exactly-once or transactional execution. The Quartz library contains building blocks related to this design, but no complete scheduler built on them has been confirmed.

**Primary sources:**
- [nostr-protocol/nips#2546](https://github.com/nostr-protocol/nips/pull/2546)

**Mentioned in:**
- [Newsletter #49 (2026-11-18)](/en/newsletters/2026-11-18-newsletter/#vitorpamplona-quartz)

**See also:**
- [NIP-65: Relay List Metadata](/en/topics/nip-65/)
- [NIP-01: Basic Protocol](/en/topics/nip-01/)
