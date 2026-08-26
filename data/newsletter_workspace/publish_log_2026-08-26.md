# Compass publication log — 2026-08-26

Issue: Nostr Compass #37
Draft PR: https://github.com/andotherstuff/nostr-compass/pull/139
Deployed page: https://nostrcompass.org/en/newsletters/2026-08-26-newsletter/

## Publication prerequisites

- `prepublish_refresh_2026-08-26.md` ends in an evidence-bearing `GATE: PASS`.
- `final_delta_refresh_2026-08-26.md` records a 16:32 UTC start and a 16:46 UTC final cutoff fetch, and ends in an evidence-bearing `GATE: PASS`.
- `handoff_2026-08-26.md` records five evidence-backed Stage 7 review artifacts, verified outreach receipts for seven eligible recipients, and relay readback of all seven invitations.
- Publication began after the Wednesday 16:00 UTC clock gate.
- The newsletter frontmatter was changed to `draft: false` and the production Hugo/Pagefind build passed before merge.

## Merge and deployment

- PR #139 squash-merged into `main` at `2026-08-26T16:57:47Z` as commit `1acecf4`.
- GitHub Pages workflow https://github.com/andotherstuff/nostr-compass/actions/runs/32991457973 completed successfully on `main`, including the deploy job.
- The deployed canonical URL returned HTTP 200 and contained `Nostr Compass #37`.

## Nostr publication

- Kind 30023 event ID: `4bfd7f91186fdcf81af57d3c585e80102372d9a62d03ba199ce170d8316a9980`
  - `d` tag `newsletter-37`, `published_at` `1787763698` (`2026-08-26T17:01:38Z`)
  - Banner image `https://image.nostr.build/fbf98ad0d8f84fd6b60fd920c0364df3549ea7a2e0ca16a159202a2cd87b8baf.png`
- Kind 1 event ID: `f595842931c116e3b07e9fe50d249b02996908235f86df2c49b1fc357d766837`
  - Created at `1787763754` (`2026-08-26T17:02:34Z`)
- Article: https://njump.me/naddr1qvzqqqr4gupzqa6e2nmnzsgjfzdy520vdy4hywr06c9ue6crpr2zxyq749uu275qqyxhwumn8ghj7mn0wvhxcmmvqyt8wumn8ghj7un9d3shjtnswf5k6ctv9ehx2aqprpmhxue69uhhyetvv9ujuumwdae8gtnnda3kjctvqy2hwumn8ghj7un9d3shjtnwdaehgu3wdejhgqqddejhwumvv468getj95enwd439wn
- Announcement: https://njump.me/nevent1qqs0t9vy9ycuz9hrkplflegdyjds9xtfpq34lpkl93ymrlp404mxsdcpp4mhxue69uhkummn9ekx7mqpzemhxue69uhhyetvv9ujuurjd9kkzmpwdejhgq3qwav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq9uz5dq

Both signed events were recovered from public relays and archived to the untracked local store
at `data/newsletter_workspace/published/2026-08-26_30023.json` and
`data/newsletter_workspace/published/2026-08-26_1.json`. Both pass `nak verify`.

Independent exact-ID readback after broadcast:

| Relay | kind 30023 | kind 1 |
|-------|-----------|--------|
| `wss://relay.primal.net` | exact | exact |
| `wss://nos.lol` | exact | exact |
| `wss://ditto.pub/relay` | exact | exact |
| `wss://relay.nostr.net` | exact | exact |
| `wss://nostr.mom` | exact | exact |
| `wss://relay.mostr.pub` | exact | exact |
| `wss://nostr-pub.wellorder.net` | exact | not returned |

Six relays returned both events by exact ID and a seventh returned the article. The
`naddr` relay hints (`nos.lol`, `relay.primal.net`, `relay.snort.social`,
`relay.nostr.net`) match the hint set used for #35.

## Open item

`data/compass_relays.txt` is absent from the repository. `PublishAgent.md` names it as the
single source of truth for the broadcast set and requires a fail-fast when it is missing, so
the configured target list for this publication could not be read from the repository and was
reconstructed from post-broadcast relay evidence instead. The file needs to be committed
before the next publication.

GATE: PASS (PR #139 merged; GitHub Pages deploy passed; canonical page HTTP 200 with issue title; kind 30023 and kind 1 both recovered by exact ID from six independent relays and archived with valid signatures)
