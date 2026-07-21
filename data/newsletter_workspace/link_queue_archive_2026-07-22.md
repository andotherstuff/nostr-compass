# Compass Link Queue

Rolling accumulator for project links/notes sent in the Marmot Compass chat
during the week, ahead of the Tuesday intake deadline. Append a new
`## <ISO 8601 UTC timestamp>` section per incoming chat message; keep each
message's content verbatim underneath (this preserves the natural
"project name + supporting links" structure IntakeAgent already expects from
a `/newsletter` prompt body).

Consumed automatically by the `compass-tuesday-intake` cron job as Stage 1
IntakeAgent input each Tuesday, then archived to
`link_queue_archive_<target-date>.md` and reset to empty so next week starts
clean. Do not delete this file; if it's missing the cron just treats the
queue as empty for that run.

---

## Resolved — folded into published issue #31 (2026-07-15), per standing policy: links that arrive before publish always update the current issue, never hold for next week

- https://sonarprivacy.xyz/ — confirmed to be Sonar's own marketing site (same project already covered as this issue's lead story, hedwig-corp/bitchat-to-sonar). Added as the primary link on the Sonar section; no separate item needed.
- Form* NIP-FS / NIP-Metadata / Decoupled Encryption Key submission — folded into this issue's "Open: private encrypted drive extends NIP-4E" protocol-work item, including the competing PR #2361 note, the spec-drift finding, and the single-drive-key security caveat. Not held for next Tuesday.

---

## 2026-07-16T20:30:00Z

Iris Stack: A Freedom Tech Toolkit — https://stack.iris.to/

Coverage check requested against `data/projects.yml`. The page is a client-rendered
SPA; the project list lives in `assets/index-*.js`. Repos it links, and their
tracking status as of 2026-07-16:

Already tracked:
- https://github.com/hzrd149/blossom — tracked as "Blossom" (projects.yml:6098)
- https://github.com/mmalmi/nostr-double-ratchet — tracked (projects.yml:4501)
- https://github.com/mmalmi/hashtree — tracked as "Hashtree" (projects.yml:5509)
- https://github.com/mmalmi/nostr-social-graph — tracked (projects.yml:4849)
- FIPS — tracked at upstream https://github.com/jmcorgan/fips (projects.yml:5433).
  The Iris Stack page links mmalmi/fips, which the GitHub API confirms is a fork of
  jmcorgan/fips (227 stars upstream, fork has 2). Existing tracking is correct;
  do not repoint to the fork.

Not tracked — candidates for #32, all pushed within the last 48h:
- https://github.com/irislib/iris-stack — "Architecture and process-level integration
  lab for the permissionless [stack]" (pushed 2026-07-16)
- https://github.com/mmalmi/iris-kit — "Shared Iris application and identity packages"
  (pushed 2026-07-16)
- https://github.com/mmalmi/nostr-pubsub — "Transport-neutral Nostr pubsub for FIPS,
  relays, and browsers" (pushed 2026-07-16)
- https://github.com/mmalmi/fips-ts — "Browser TypeScript FIPS — Noise IK/XK over
  secp256k1, WebRTC datachannels" (pushed 2026-07-16)
- https://github.com/mmalmi/fips-tcp — "Reliable ordered TCP streams over
  authenticated FIPS service datagrams" (pushed 2026-07-15)

Each still needs the per-PR Nostr-surface gate applied at triage. nostr-pubsub and
fips-ts name Nostr/secp256k1 surfaces directly; fips-tcp looks like transport
plumbing and may fail the gate on its own.

## 2026-07-20T00:00:00Z

Interesting for next edition — https://njump.to/nevent1qqsr4awwnfndnnz77zanjxarw6nd0uld0ckayxp2navz0u9tzzwfweqpzamhxue69uhhyetvv9ujuurjd9kkzmpwdejhgtczyquwq70hxz22lzytw65rnnjewg0lj8a74khxa8h9j47q38pdnqy3kqcyqqqqqqgz8083u

## 2026-07-21T14:05:34Z

https://nostrautica.cypherpunk.today/

## 2026-07-21T14:05:49Z

https://stack.iris.to/

(Duplicate of the 2026-07-16T20:30:00Z Iris Stack entry above, which already carries the full repo-by-repo coverage check. IntakeAgent: dedup against that entry, use its notes.)
