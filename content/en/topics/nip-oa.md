---
title: 'Buzz Draft NIP-OA: Owner Attestation'
date: 2026-10-28
draft: false
---

**Status:** This is a draft proposal specific to the Buzz project. NIP-OA is not an accepted official NIP. The label comes from Buzz project documentation, and the official NIPs repository has not assigned or approved it.

## Purpose

NIP-OA defines an optional `auth` tag that lets an owner key authorize an agent key to publish events. The agent key stays the author of the event. A valid tag counts only as evidence of authorization and does not let the agent impersonate the owner.

## Mechanism

The owner signs, with a Schnorr signature, a domain-separated hash that binds the agent pubkey to an exact conditions string. Conditions can require an event kind and set bounds on the self-declared `created_at`. The agent can reuse the tag on its events as long as each event meets the conditions. Verifiers first validate the core event, then check the owner signature and every condition.

## Limits

An empty conditions string adds no constraints. Timestamp clauses constrain a field the agent controls, so they do not give wall-clock expiry. Anyone who needs freshness has to check it separately. Publishing the tag publicly links the owner and agent keys.

## Primary sources

- [Buzz NIP-OA draft: Owner Attestation (pinned revision)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-OA.md)

## See also

- [NIP-01](/en/topics/nip-01/)

**Mentioned in:**

- [Newsletter #46: Buzz](/en/newsletters/2026-10-28-newsletter/#buzz)
