---
title: "NAP-WEBRTC: Napplet Data Channels"
date: 2026-11-18
draft: false
categories: ["NIPs"]
---

NAP-WEBRTC is a napplet draft contract for WebRTC data channels between peers, with the host shell authenticating signaling. NAPs are napplet draft contracts, not accepted NIPs.

Merged [#145](https://github.com/napplet/naps/pull/145) is development on `nap-webrtc`, not yet integrated into `master`. It merges into base proposal [#59](https://github.com/napplet/naps/pull/59), which is still open. It changes an open draft branch, and `master` has not accepted it. Napplets can request ordering and retransmission behavior, and the shell reports the settings it applied. A separate `sendBytes` call sends binary payloads, encoded as base64 on the wire. The shell advertises payload size limits and provides advisory statistics. Peer identity MUST be the signaling key that the shell authenticated, and unauthenticated payloads are not delivered. The pull request body says that neither the base proposal nor this addition has an implementation.

**Primary sources:**
- [napplet/naps PR #145](https://github.com/napplet/naps/pull/145)
- [napplet/naps PR #59: base NAP-WEBRTC proposal](https://github.com/napplet/naps/pull/59)

**Mentioned in:**
- [Newsletter #49](/en/newsletters/2026-11-18-newsletter/#napplet-naps-145)

**See also:**
- [NAP-NEIGHBOR](/en/topics/nap-neighbor/)
- [NIP-01: Basic protocol](/en/topics/nip-01/)
