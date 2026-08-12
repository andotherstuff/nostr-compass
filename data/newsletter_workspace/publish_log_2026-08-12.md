# Compass publication log — 2026-08-12

Issue: Nostr Compass #35
Draft PR: https://github.com/andotherstuff/nostr-compass/pull/133
Deployed page: https://nostrcompass.org/en/newsletters/2026-08-12-newsletter/

## Publication prerequisites

- Owner approval was recorded on Kanban before publication.
- `prepublish_refresh_2026-08-12.md` ends in an evidence-bearing `GATE: PASS`.
- `final_delta_refresh_2026-08-12.md` began after 14:30 UTC, includes the mandatory post-15:30 cutoff, and ends in an evidence-bearing `GATE: PASS`.
- Publication began after the Wednesday 16:00 UTC clock gate.
- The newsletter frontmatter was changed to `draft: false`, the production build passed, PR #133 was normalized to one commit, force-with-lease updated, marked ready, and its GitHub build check passed.

## Merge and deployment

- PR #133 squash-merged at `2026-08-12T16:06:39Z`.
- GitHub Pages workflow https://github.com/andotherstuff/nostr-compass/actions/runs/31615932627 completed successfully, including the deploy job.
- The deployed canonical URL returned HTTP 200 and contained `Nostr Compass #35`.

## Nostr publication

- Kind 30023 event ID: `cc64af74394bbce58fee0ad28e5b1cf2476afd10ab8e0a314eaac44a526a3bb9`
- Kind 1 event ID: `177a8fd90fed7105b3e2d486b307ce3eea098128541b0ffbda474ca2a17ec4da`
- Article: https://njump.me/naddr1qvzqqqr4gupzqa6e2nmnzsgjfzdy520vdy4hywr06c9ue6crpr2zxyq749uu275qqyxhwumn8ghj7mn0wvhxcmmvqyt8wumn8ghj7un9d3shjtnswf5k6ctv9ehx2aqprpmhxue69uhhyetvv9ujuumwdae8gtnnda3kjctvqy2hwumn8ghj7un9d3shjtnwdaehgu3wdejhgqqddejhwumvv468getj95en2zlnrpf
- Announcement: https://njump.me/nevent1qvzqqqqqqypzqa6e2nmnzsgjfzdy520vdy4hywr06c9ue6crpr2zxyq749uu275qqyxhwumn8ghj7mn0wvhxcmmvqyt8wumn8ghj7un9d3shjtnswf5k6ctv9ehx2aqprpmhxue69uhhyetvv9ujuumwdae8gtnnda3kjctvqy2hwumn8ghj7un9d3shjtnwdaehgu3wdejhgqpqzaaglkg0a4cstvlz6jrtxp7w8m4qnqfg2sdsl776gax29gt7cndqn765z0

Both signed events received positive `OK` receipts from all 12 configured broadcast targets, including the write-only NIP-66 blaster at `sendit.nosflare.com`. Independent readback then recovered the exact kind 30023 and kind 1 IDs from all 11 durable configured relays; the blaster was excluded from readback evidence.

GATE: PASS (PR #133 merged; GitHub Pages deploy passed; canonical page HTTP 200 with issue title; kind 30023 and kind 1 received 12/12 broadcast acceptances and exact-ID independent readback from 11/11 durable relays)
