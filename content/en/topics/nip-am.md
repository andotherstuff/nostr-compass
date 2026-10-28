---
title: 'Buzz Draft NIP-AM: Agent Turn Metrics'
date: 2026-10-28
draft: false
---

**Status:** This is a draft proposal specific to the Buzz project. NIP-AM is not an accepted official NIP. The label comes from Buzz project documentation, and the official NIPs repository has not assigned or approved it.

## Purpose

NIP-AM records usage for each completed AI agent turn. The agent publishes one `kind:44200` event per turn, which Buzz convention treats as a regular append-only event. The content is NIP-44 encrypted from agent to owner. It holds token usage figures together with correlation IDs, and any cost values are estimates. It carries no conversation transcript.

## Limits

Public tags identify the owner and the agent, and relays can still see when events are published. So the format does not hide that activity happened. A missing usage value means unknown and must never be counted as zero.

## Delegated readers proposal

An open documentation pull request, #8582, proposes a least-privilege grant signed by the owner. Under it, the agent would publish a separate encrypted copy for each active reader, each tied to the exact grant event ID. The pull request changes no runtime authorization. The proposed grant kind `30180` and the reader cap are still open questions, and the revocation policy is also unsettled. Revocation could limit relay history and future reads. It cannot erase copies a reader has already received.

## Primary sources

- [Buzz NIP-AM draft: Agent Turn Metrics (pinned revision)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-AM.md)
- [Buzz pull request #8582: delegated metric readers (open draft)](https://github.com/block/buzz/pull/8582)

## See also

- [NIP-44](/en/topics/nip-44/)

**Mentioned in:**

- [Newsletter #46: Draft NIP-AM text for delegated metric readers](/en/newsletters/2026-10-28-newsletter/#draft-nip-am-text-for-delegated-metric-readers)
- [Newsletter #46: Buzz](/en/newsletters/2026-10-28-newsletter/#buzz)
