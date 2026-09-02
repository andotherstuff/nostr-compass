# Compass publication log — 2026-09-02

Issue: Nostr Compass #38
Draft PR: https://github.com/andotherstuff/nostr-compass/pull/147
Deployed page: https://nostrcompass.org/en/newsletters/2026-09-02-newsletter/

## Publication prerequisites

- Pre-publication refresh (`prepublish_refresh_2026-09-02.md`): ends in GATE: PASS
- Final delta refresh (`final_delta_refresh_2026-09-02.md`): ends in GATE: PASS
- Stage 8 review handoff (`handoff_2026-09-02.md`): ends in GATE: PASS

## Merge and deployment

- PR #147 squash-merged into `main` at `2026-09-02T18:23:04Z` as commit `dd65e37`.
- GitHub Pages workflow https://github.com/andotherstuff/nostr-compass/actions/runs/33667905446 concluded `success`.
- The canonical URL returned HTTP 200 and contained `Nostr Compass #38`.

## Nostr publication

- Kind 30023 event ID: `63463380321b0428fdf0bb3afed4dbd88ed994fe174901c9a0f55de63e1e90df`
  - `d` tag `newsletter-38`, `published_at` `1788373608` (2026-09-02T18:26:48Z)
  - Banner image https://image.nostr.build/fbf98ad0d8f84fd6b60fd920c0364df3549ea7a2e0ca16a159202a2cd87b8baf.png
- Kind 1 event ID: `cb446335eaceed3265060488a2e1fa3cc51e4b8b3947f8b19b62c37d3e04afc4`
  - Created at `1788373704` (2026-09-02T18:28:24Z)
- Article: https://njump.me/naddr1qvzqqqr4gupzqa6e2nmnzsgjfzdy520vdy4hywr06c9ue6crpr2zxyq749uu275qqyxhwumn8ghj7mn0wvhxcmmvqyt8wumn8ghj7un9d3shjtnswf5k6ctv9ehx2aqprpmhxue69uhhyetvv9ujuumwdae8gtnnda3kjctvqy2hwumn8ghj7un9d3shjtnwdaehgu3wdejhgqqddejhwumvv468getj95ens6075e2
- Announcement: https://njump.me/nevent1qgs8wk257uc5zyjgnf9znmrf9dersm7kp0xwkqcg6s33q84f08zh4qqpp4mhxue69uhkummn9ekx7mqpzemhxue69uhhyetvv9ujuurjd9kkzmpwdejhgqpqedzxxd02emknyegxqjy29c068nz3ujut89rl3vvmvtph60sy4lzqnryl6r
- Signed events and receipts: `publish/out/38/`; ledger entry in `publish/published.json`.

### Broadcast fan-out

`publish/config/relays.json` configures 12 targets. The article was accepted by 12 and the announcement by 12.

Every configured target accepted both events.

`wss://sendit.nosflare.com` is a write-only NIP-66 blaster; acceptance counts as fan-out and is excluded from readback evidence.

### Independent readback

Exact-id queries against the 11 durable configured relays after broadcast:

- both events returned by 11: `wss://nos.lol`, `wss://relay.primal.net`, `wss://relay.snort.social`, `wss://relay.nostr.net`, `wss://nostr.mom`, `wss://offchain.pub`, `wss://nostr.data.haus`, `wss://relay.mostr.pub`, `wss://wot.nostr.party`, `wss://nostr.oxtr.dev`, `wss://relay.nostr.com`

The signed events are archived to the untracked local store at `data/newsletter_workspace/published/2026-09-02_30023.json` and `data/newsletter_workspace/published/2026-09-02_1.json`, byte-identical to `publish/out/38/event.json` and `publish/out/38/announcement.json`.

GATE: PASS (merge and deploy verified; article accepted by 12/12 and announcement by 12/12 configured relays; both events recovered by exact id from 11 durable relays)
