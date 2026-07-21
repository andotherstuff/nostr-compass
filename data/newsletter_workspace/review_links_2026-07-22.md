# LinkCheck Review — 2026-07-22 draft

File checked: `content/en/newsletters/2026-07-22-newsletter.md` (draft: true)
Method: extracted all external http(s) URLs (deduped, 47 unique), `curl -sL -o /dev/null -w '%{http_code}'` with one retry per failure; internal `/en/topics/<slug>/` links mapped to `content/en/topics/<slug>.md`; PR `#NNNN` mentions checked for markdown-link wrapping; release-version mentions checked for link coverage.

## External link table (47 unique URLs)

| HTTP | URL |
|---|---|
| 200 | https://github.com/barrydeen/wisp |
| 200 | https://github.com/barrydeen/wisp/releases/tag/v1.2.0 |
| 200 | https://github.com/Cameri/nostream |
| 200 | https://github.com/Cameri/nostream/pull/676 |
| 200 | https://github.com/Cameri/nostream/pull/702 |
| 200 | https://github.com/greenart7c3/Amber |
| 200 | https://github.com/greenart7c3/Amber/releases/tag/v6.3.0 |
| 200 | https://github.com/hedwig-corp/bitchat-to-sonar |
| 200 | https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.11 |
| 200 | https://github.com/jmcorgan/fips |
| 200 | https://github.com/jmcorgan/fips/releases/tag/v0.4.1 |
| 200 | https://github.com/mmalmi/fips-ts |
| 200 | https://github.com/mmalmi/fips-ts/releases |
| 200 | https://github.com/mmalmi/nostr-pubsub |
| 200 | https://github.com/mmalmi/nostr-pubsub/releases |
| 200 | https://github.com/mmalmi/nostr-social-graph |
| 200 | https://github.com/mmalmi/nostr-social-graph/releases/tag/v2.0.0 |
| 200 | https://github.com/nostrord/nostrord |
| 200 | https://github.com/nostrord/nostrord/pull/188 |
| 200 | https://github.com/nostrord/nostrord/pull/192 |
| 200 | https://github.com/nostrord/nostrord/pull/195 |
| 200 | https://github.com/nostrord/nostrord/releases/tag/v2.3.0 |
| 200 | https://github.com/nostr-protocol/nips |
| 200 | https://github.com/nostr-protocol/nips/pull/2252 |
| 200 | https://github.com/nostr-protocol/nips/pull/2303 |
| 200 | https://github.com/nostr-protocol/nips/pull/2319 |
| 200 | https://github.com/nostr-protocol/nips/pull/2375 |
| 200 | https://github.com/nostr-protocol/nips/pull/2379 |
| 200 | https://github.com/nostr-protocol/nips/pull/2380 |
| 200 | https://github.com/nostr-protocol/nips/pull/2383 |
| 200 | https://github.com/nostr-protocol/nips/pull/2413 |
| 200 | https://github.com/nostr-protocol/nips/pull/2416 |
| 200 | https://github.com/nostr-protocol/nips/pull/2417 |
| 200 | https://github.com/nostr-protocol/nips/pull/2418 |
| 200 | https://github.com/nostr-protocol/nips/pull/2419 |
| 200 | https://github.com/nostr-wallet-connect/nwc |
| 200 | https://github.com/tajava2006/cliprelay |
| 200 | https://github.com/vitorpamplona/amethyst |
| 200 | https://github.com/vitorpamplona/amethyst/pull/3650 |
| 200 | https://github.com/vitorpamplona/amethyst/pull/3653 |
| 200 | https://github.com/vitorpamplona/amethyst/pull/3654 |
| 200 | https://github.com/zapstore/zapstore |
| 200 | https://github.com/zapstore/zapstore/releases/tag/1.1.0 |
| 403* | https://njump.me/nevent1qqsr4awwnfndnnz77zanjxarw6nd0uld0ckayxp2navz0u9tzzwfweqpzamhxue69uhhyetvv9ujuurjd9kkzmpwdejhgtczyquwq70hxz22lzytw65rnnjewg0lj8a74khxa8h9j47q38pdnqy3kqcyqqqqqqgz8083u |
| 200 | https://stack.iris.to/ |
| 200 | https://zapstore.dev |

\* njump.me 403 is anti-scraping protection of the njump web gateway, not a broken link. Verified alive and content-correct via Firecrawl fetch on 2026-07-21: the nevent resolves to the IndieSats "Pivot: From Platform to Infrastructure" kind:1 note published 2026-07-20 11:50:01 GMT by npub18rs8naesjjhc3zmk4quuuktjrlu3l04d4ehfaev40syfctvcpydsnd97wc — exactly the source the draft's IndieSats lead cites. Not a fix-list item.

Result: **46/47 curl-200; 47/47 verified alive** (njump verified out-of-band).

## Internal topic links (12/12 verified)

| Link | Target file | Status |
|---|---|---|
| /en/topics/fips/ | content/en/topics/fips.md | OK |
| /en/topics/nip-09/ | content/en/topics/nip-09.md | OK |
| /en/topics/nip-11/ | content/en/topics/nip-11.md | OK |
| /en/topics/nip-29/ | content/en/topics/nip-29.md | OK |
| /en/topics/nip-42/ | content/en/topics/nip-42.md | OK |
| /en/topics/nip-43/ | content/en/topics/nip-43.md | OK |
| /en/topics/nip-46/ | content/en/topics/nip-46.md | OK |
| /en/topics/nip-47/ | content/en/topics/nip-47.md | OK |
| /en/topics/nip-51/ | content/en/topics/nip-51.md | OK |
| /en/topics/nip-56/ | content/en/topics/nip-56.md | OK |
| /en/topics/nip-65/ | content/en/topics/nip-65.md | OK |
| /en/topics/nip-66/ | content/en/topics/nip-66.md | OK |

## PR #NNNN mention check

20 distinct PR numbers appear in prose. 19 are wrapped as markdown links (`[PR #NNNN](https://github.com/.../pull/NNNN)`). **2 failures:**

| # | Line | Current text | Suggested text | Reason |
|---|---|---|---|---|
| 1 | 153 | `nostream's PR #702 builds on` | `[nostream's PR #702](https://github.com/Cameri/nostream/pull/702) builds on` | PR #702 mentioned in prose without a markdown link; the PR is already linked elsewhere in the doc and the URL is live (200). |
| 2 | 176 | `nostream's PR #676 is the relay-side machinery` | `[nostream's PR #676](https://github.com/Cameri/nostream/pull/676) is the relay-side machinery` | PR #676 mentioned in prose without a markdown link; URL is live (200). |

## Release version mention check

All tagged-release version strings in section headings/body are linked on first body mention (v6.3.0, v2.3.0, v1.2.0, v0.1.2, v0.1-alpha.11, v0.4.1, nostr-pubsub v0.1.3–v0.5.2, nostr-social-graph 2.0.0). **1 failure:**

| # | Line | Current text | Suggested text | Reason |
|---|---|---|---|---|
| 3 | 74 | `ahead of its v1.13.0 release` | `ahead of its [v1.13.0](https://github.com/vitorpamplona/amethyst/releases) release` (or omit link and keep prose) | "v1.13.0" appears unlinked in body text (also in heading line 72 and line 16/124 as pre-release references). There is no v1.13.0 tag yet (pre-release QA), so link to the releases page is the correct target; alternatively downgrade to unlinked prose "ahead of its next release". Heading-line version mentions are exempt from linking by convention, but body mention on line 74 is a linkable release reference. |

## Fix-list

1. **Line 153** — `nostream's PR #702` → `[nostream's PR #702](https://github.com/Cameri/nostream/pull/702)` (bare PR mention).
2. **Line 176** — `nostream's PR #676` → `[nostream's PR #676](https://github.com/Cameri/nostream/pull/676)` (bare PR mention).
3. **Line 74** — `its v1.13.0 release` → link `v1.13.0` to `https://github.com/vitorpamplona/amethyst/releases` or rephrase to drop the version (unlinked release version mention; tag does not exist yet, so releases-page link is the safe target).

GATE: FAIL — 46/47 external links curl 200 OK (njump 403 is anti-scrape; content verified alive via Firecrawl) and 12/12 internal topic links verified, but 2 bare PR mentions (lines 153, 176) and 1 unlinked release version (line 74) need the fix-list above.
