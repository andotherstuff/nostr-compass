---
title: "NAP-NEIGHBOR: Peer-Carried Neighborhoods (Proposed)"
date: 2026-11-18
draft: false
categories: ["NIPs"]
---

NAP-NEIGHBOR is an open draft napplet proposal, [#146](https://github.com/napplet/naps/pull/146). NAPs are napplet draft contracts, not accepted NIPs. The proposal gives each napplet opaque neighborhood addresses for the relay, outbox, resource and upload domains. Traffic for these addresses travels over the user's own peers. Each user has their own view of their peers. The host manages the neighborhood and keeps each napplet's addresses separate. Sharing proximity information and napplet updates is optional.

A neighborhood has no membership list and no privacy boundary. Any peer can pass ordinary Nostr events on to others. The specifications that consume these addresses would need scheme changes, and upload use would need defined destinations. No transport implementation has been verified, and nothing guarantees delivery or reach. The companion registry change [#147](https://github.com/napplet/naps/pull/147) is part of this proposal. NAP-NEIGHBOR follows the mesh drafts [#122](https://github.com/napplet/naps/pull/122) and [#123](https://github.com/napplet/naps/pull/123), which were retracted.

**Primary sources:**
- [napplet/naps PR #146: NAP-NEIGHBOR](https://github.com/napplet/naps/pull/146)
- [napplet/naps PR #147: registry change](https://github.com/napplet/naps/pull/147)

**Mentioned in:**
- [Newsletter #49](/en/newsletters/2026-11-18-newsletter/#napplet-naps-146)

**See also:**
- [NIP-65: Relay list metadata](/en/topics/nip-65/)
- [Blossom](/en/topics/blossom/)
- [NAP-WEBRTC](/en/topics/nap-webrtc/)
