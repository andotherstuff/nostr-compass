---
title: "BUD-05: Blossom Media Optimization"
date: 2026-11-18
draft: false
categories: ["NIPs"]
---

BUD-05 is an optional draft in the Blossom specifications. It defines `PUT /media`, where a client uploads binary content and the server converts or optimizes it. The server uses the `Content-Type` and `Content-Length` headers to decide how to process the upload. A successful 200 or 201 response returns a blob descriptor for the resulting file. Server policy decides which media the server accepts, so a server can reject an upload.

Recent merges in the Wisp client affect how clients check transformed media. In merged [#697](https://github.com/barrydeen/wisp/pull/697), Wisp compares any supplied `sha256` value with the file it fetched. Media produced by BUD-05 transforms can leave that value out. Merged [#688](https://github.com/barrydeen/wisp/pull/688) adds BUD-10 `blossom:` URIs. Wisp tries the hinted servers first and then the user's configured servers, and it hashes the fetched bytes before using the media URL. That guarantee applies only to Wisp's own fetch. A later, separate fetch of the same URL is not covered. The same group of merges also added BOLT11 amount and description checks for zaps in [#687](https://github.com/barrydeen/wisp/pull/687). None of these changes has appeared in a Wisp release.

**Primary sources:**
- [BUD-05 specification](https://raw.githubusercontent.com/hzrd149/blossom/master/buds/05.md)
- [Wisp #697: sha256 check on fetched media](https://github.com/barrydeen/wisp/pull/697)
- [Wisp #688: BUD-10 blossom: URIs](https://github.com/barrydeen/wisp/pull/688)
- [Wisp #687: BOLT11 commitment verification](https://github.com/barrydeen/wisp/pull/687)

**Mentioned in:**
- [Newsletter #49](/en/newsletters/2026-11-18-newsletter/#barrydeen-wisp)

**See also:**
- [Blossom](/en/topics/blossom/)
- [BUD-04: Mirroring](/en/topics/bud-04/)
- [NIP-57: Lightning zaps](/en/topics/nip-57/)
