---
title: "Buzz NIP-FA: Federated identity adapter"
date: 2026-10-21
draft: false
categories: ["NIPs"]
---

Buzz NIP-FA is a draft, optional specification from the Buzz project. It sits outside the accepted NIPs of the official nostr-protocol/nips repository.

It defines a provider-neutral HTTP contract between a Nostr client and an enterprise identity adapter. After a browser login, the adapter holds a session for the user. It issues project-local Buzz NIP-FI assertions that bind the user to a Nostr key, which the client proves it controls with [NIP-98](/en/topics/nip-98/). The [operator chooses each assertion's lifetime](https://github.com/block/buzz/pull/8934), which must respect the issuer's maximum_assertion_age accepted by the relay, and exp cannot exceed the adapter session expiry. The chosen lifetime bounds how long a revoked key could still reconnect after a relay restart, and clients must not reject an assertion solely because of its lifetime. NIP-FI and the official NIPs are unchanged. Login uses an S256 handoff challenge and a loopback callback on `127.0.0.1` or `[::1]` that receives a single-use code. Upstream systems such as OIDC or SAML stay behind the adapter. Finding which relays require enterprise identity is left to other specifications.

Primary source: the [NIP-FA specification](https://github.com/block/buzz/blob/main/docs/nips/NIP-FA.md) in the Buzz repository.

## Agent credentials

Buzz merged a [NIP-FA draft for owner-authorized agent credentials](https://github.com/block/buzz/pull/9015), defining grant, assertion and revocation routes for agents an owner has authorized through NIP-OA. A grant comes from an RFC 8693 token exchange that pairs the owner's session with a [NIP-98](/en/topics/nip-98/) proof from the agent. For an assertion, the agent presents the grant as a Bearer token alongside its own proof, and clients check the assertion's `iss` against the grant's issuer. Agent proofs are single-use and belong only to the grant and assertion routes. Revocation runs on the owner's session with no agent proof; it revokes the agent key and its grants and disconnects the agent. Adapter policy decides grant lifetime. Unsupported authorization conditions are refused, and a revoked key cannot re-enroll. NIP-FA is a Buzz specification, not an accepted NIP. The merge is in source only, with no claim of production activation, a released build or interoperability.

## Primary sources

- [Buzz NIP-FA: Federated Identity Adapter](https://github.com/block/buzz/blob/main/docs/nips/NIP-FA.md)

- [Owner-authorized agent credential routes](https://github.com/block/buzz/pull/9015)

## Mentioned in

- [Newsletter #47: Buzz agent credentials](/en/newsletters/2026-11-04-newsletter/#buzz-defines-owner-authorized-agent-credential-routes)


- [Newsletter 45](/en/newsletters/2026-10-21-newsletter/#buzz)
