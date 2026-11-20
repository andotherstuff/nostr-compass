---
title: "BUD-04: Blossom Mirroring"
date: 2026-11-18
draft: false
categories: ["NIPs"]
---

BUD-04 is an optional draft in the Blossom specifications. It defines `PUT /mirror`, which lets a client give a server the URL of a blob hosted somewhere else. The receiving server then fetches that blob and stores it. The server makes an outbound request to an address the client chose, so the endpoint can be used for server-side request forgery (SSRF). The defining document says to prevent this by validating the URL and its destination and by restricting outbound connections.

A [merged specification change](https://github.com/hzrd149/blossom/commit/4c467fe8d483ad0c3dda784707dfee4436793650) makes this guidance explicit. Servers should accept mirror URLs only over HTTP or HTTPS. They should also block internal, loopback, private and link-local destinations for both IPv4 and IPv6. These checks apply to the IP address the server connects to after DNS resolution, and the server repeats them on every redirect. An upload authorization does not replace this protection. The new text is normative SHOULD guidance. It does not show that any server has implemented it, and it does not verify that any deployment is protected.

**Primary sources:**
- [BUD-04 specification](https://raw.githubusercontent.com/hzrd149/blossom/master/buds/04.md)
- [Blossom commit 4c467fe: SSRF guidance for mirroring](https://github.com/hzrd149/blossom/commit/4c467fe8d483ad0c3dda784707dfee4436793650)

**Mentioned in:**
- [Newsletter #49](/en/newsletters/2026-11-18-newsletter/#flox1an-nostube)

**See also:**
- [Blossom](/en/topics/blossom/)
- [BUD-05: Media optimization](/en/topics/bud-05/)
- [BUD-11: Delegation](/en/topics/bud-11/)
