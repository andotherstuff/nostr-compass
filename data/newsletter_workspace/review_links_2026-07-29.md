# Newsletter #33 link review

Generated: 2026-07-29T16:15:40Z
Target: `content/en/newsletters/2026-07-29-newsletter.md`

## Execution

- Probed 131 unique external URLs with `curl -L --compressed`, retries, a 25-second request timeout, and expected access-control responses accepted.
- External failures: 0/131.
- Resolved all 25 unique internal topic targets on disk.
- Resolved all 27 GitHub release-tag links through the GitHub GraphQL API.
- Resolved all 37 cited NIP files through the canonical `nostr-protocol/nips` repository.
- `git diff --check`: PASS.

## Rendered backlinks

After the Mosaico heading changed, `check_topic_backlinks.py` correctly found one stale NIP-29 fragment. `content/en/topics/nip-29.md` was updated to the new production anchor. The final minified-Hugo check passes with 25 topic pages, Primary sources blocks on all 25, and 34 rendered newsletter backlinks.

GATE: PASS (131/131 external URLs reachable; 25 topic targets and 34 rendered backlinks valid at 2026-07-29T16:15:40Z)
