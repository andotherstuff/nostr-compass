# Owner refresh notes — 2026-09-09

## 2026-09-09T06:12:01Z — ngit v3 and GitWorkshop v4 coordinated release

### User submission (verbatim)

[Tidy Llama] I’ve just launched ngit v3 and GitWorkshop v4 🎓 This is my biggest coordinated release yet, bringing CI, private repositories, forge-free software releases and much more. GRASP is the powerhouse behind ngit, and the launch also includes ngit-grasp v3, the first ngit-ci 0.1 release and an entirely new docs site. https://ngit.dev/v3

### Required refresh disposition

Treat this as a time-sensitive owner-submitted candidate for Nostr Compass #39. Verify the launch page and primary release/repository sources for ngit v3, GitWorkshop v4, ngit-grasp v3, ngit-ci 0.1, GRASP, CI, private repositories, forge-free releases, and the new documentation site. Add the verified material to the current newsletter and synchronized section artifacts if it passes the Nostr scope, relevance, continuity, and source gates; otherwise record an explicit source-backed skip decision before the final-delta gate.

### Disposition — INCLUDE

The primary launch page returned HTTP 200 and verifies the coordinated versions and features. Each linked source repository (`ngit`, `ngit-grasp`, `ngit-ci`, and `GitWorkshop`) also returned HTTP 200. This is directly Nostr-relevant git collaboration infrastructure and clears continuity because the last ngit and GitWorkshop coverage predates the major-version suite, first CI release, practical private-repository workflow, and forge-free signed release publishing. Added to triage and Stage 4 selection as the lead story; section and assembled-draft synchronization remain required.

## 2026-09-09T07:09:29Z — fips2go

### User submission (verbatim)

[Tidy Llama] Add this to compass too.https://zapstore.dev/apps/naddr1qqgx7un89enxjurn9eskuerjda5kgqgcwaehxw309aex2mrp0yh85ctswd6x7un99ejx2aszyqs9vy2xh4p6zygk35qepsja6w7mnl4j3nnyvjgyg079gxnm83e0yqcyqqq8uzclek0pe

### Disposition — INCLUDE

The submitted address decodes to kind 32267, pubkey `20561146bd43a111168d0190c25dd3bdb9feb28ce646490443fc541a7b3c72f2`, identifier `org.fips.android`, with relay hint `wss://relay.zapstore.dev`. Exact relay readback recovered signed app event `ec767c0bf69d17b032e1c9a33db329aadfd729f854f03e5bb9b8b330df852ec0`; its repository and current v0.3.4 release resolve through the authenticated GitHub API. The app renders its FIPS secp256k1 node identity as an `npub`, resolves and pings peers by `npub`, and can give selected Nostr clients access to relay or service endpoints on `.fips` names. Include it in News as a newly tracked Android FIPS app and update the existing FIPS topic page.
