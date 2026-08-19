# Review: LinkChecker — Newsletter #36 (2026-08-19)

## External links

Every distinct external URL in the draft was requested with
`curl -o /dev/null -sw '%{http_code}' -L --max-time 25`, run 2026-08-18 from the Compass
workspace. Extraction: `grep -oE "https?://[^)\" ]+" <draft> | sed 's/[.,]$//' | sort -u`.

- Distinct external URLs: **165**
- HTTP 200 after redirects: **165**
- Non-200: **0**

The nine URLs added with the Nail section on 2026-08-18 were checked in the same pass and all returned 200.

The set covers GitHub release tags, pull requests, security advisories, specification files
in `nostr-protocol/nips`, the Concord and Marmot specification repositories, two relay
endpoints cited as the source of the recovered event examples, and the Glow product page.

## Internal links

- Topic targets referenced: 27 (`blossom` plus 26 NIP pages). Every `content/en/topics/<slug>.md`
  exists; zero missing.
- Newsletter targets referenced: `2026-07-15-newsletter` and `2026-08-12-newsletter`. Both exist.
- Rendered backlink fragments verified against the production HTML by
  `scripts/check_topic_backlinks.py`, which resolves each `#fragment` against the ids in
  `public/en/newsletters/2026-08-19-newsletter/index.html`.

## Repeated destinations

Ten destinations appear more than once. Each repeat is a deliberate cross-section reference,
not an accidental duplicate: the Amethyst repository is cited as an implementation in four
different sections, the NIP-58 and NIP-22 specification files are cited once per deep-dive
paragraph that makes a claim about the spec, `divine-mobile/releases/tag/1.0.20` is cited in
its own release writeup and again as NIP-58 implementation evidence, and `nos.lol` and
`relay.primal.net` are cited once per recovered event example. No two different projects share
a destination and no anchor text points at an unrelated URL.

GATE: PASS (165/165 external links HTTP 200 on 2026-08-18; 27/27 topic targets and 2/2 newsletter targets exist; 27/27 rendered backlink fragments resolve; 10 repeated destinations all accounted for as intentional cross-references)
