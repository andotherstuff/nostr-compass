# Compass publication log — 2026-09-16

Issue: Nostr Compass #40
Draft PR: https://github.com/andotherstuff/nostr-compass/pull/173
Deployed page: https://nostrcompass.org/en/newsletters/2026-09-16-newsletter/

## Publication prerequisites

- Quality composite: `/opt/data/compass-worktrees/2026-09-16/publish/out/40/quality-composite.json` (8e5e7c3c9297188776b89ab5631314d021a91090ab9ed6464e13ede36f0f4fe3)
- Feedback snapshot: `publish/out/40/quality/feedback.json` (daeb00bb96f0e597ef437a1e843cb5d828ae8c0a02efe45bce3c24da86d34c40)
- Edition authorization: `publish/out/40/quality/authorization.json` (d6a16d178246b11c5a1bd7567c0ebe0b2834cc735e5fc07eefdf55ae2f6c7a7d)

## Merge and deployment

- PR #173 squash-merged into `main` as commit `cb9729c`.
- GitHub Pages workflow https://github.com/andotherstuff/nostr-compass/actions/runs/35139224061 concluded `success`.
- The canonical URL returned HTTP 200 and contained `Nostr Compass #40`.

## Nostr publication

- Kind 30023 event ID: `7647da0a7f60325c88f03b12e837b392113dd41d7b8bd5018aaeadd3f61973db`
  - `d` tag `newsletter-40`, `published_at` `1789586104` (2026-09-16T19:15:04Z)
  - Banner image https://image.nostr.build/fbf98ad0d8f84fd6b60fd920c0364df3549ea7a2e0ca16a159202a2cd87b8baf.png
- Kind 1 event ID: `f44e2aff5f667382cceaabb1c812b4d39989fff4a9a2a01857251b3e4aa7368d`
  - Created at `1789586139` (2026-09-16T19:15:39Z)
- Article: https://njump.me/naddr1qvzqqqr4gupzqa6e2nmnzsgjfzdy520vdy4hywr06c9ue6crpr2zxyq749uu275qqyxhwumn8ghj7mn0wvhxcmmvqyt8wumn8ghj7un9d3shjtnswf5k6ctv9ehx2aqprpmhxue69uhhyetvv9ujuumwdae8gtnnda3kjctvqy2hwumn8ghj7un9d3shjtnwdaehgu3wdejhgqqddejhwumvv468getj956rq0atz6r
- Announcement: https://njump.me/nevent1qgs8wk257uc5zyjgnf9znmrf9dersm7kp0xwkqcg6s33q84f08zh4qqpp4mhxue69uhkummn9ekx7mqpzemhxue69uhhyetvv9ujuurjd9kkzmpwdejhgqpq738z4l6lveec9n824wcusy456wvcnll54x32qxzhy5dnuj48x6xs24e2se
- Signed events and receipts: `publish/out/40/`; ledger entry in `publish/published.json`.

### Broadcast fan-out

`publish/config/relays.json` configures 12 targets. The article was accepted by 11 and the announcement by 11.

Rejections and failures:

- article, `wss://wot.nostr.party`: socket: WebSocket connection to 'wss://wot.nostr.party/' failed: Expected 101 status code
- announcement, `wss://wot.nostr.party`: socket: WebSocket connection to 'wss://wot.nostr.party/' failed: Expected 101 status code

`wss://sendit.nosflare.com` is a write-only NIP-66 blaster; acceptance counts as fan-out and is excluded from readback evidence.

### Independent readback

Exact-id queries against the 11 durable configured relays after broadcast:

- both events returned by 10: `wss://nos.lol`, `wss://relay.primal.net`, `wss://relay.snort.social`, `wss://relay.nostr.net`, `wss://nostr.mom`, `wss://offchain.pub`, `wss://nostr.data.haus`, `wss://relay.mostr.pub`, `wss://nostr.oxtr.dev`, `wss://relay.nostr.com`
- neither event returned by: `wss://wot.nostr.party`

The signed events are archived to the untracked local store at `data/newsletter_workspace/published/2026-09-16_30023.json` and `data/newsletter_workspace/published/2026-09-16_1.json`, byte-identical to `publish/out/40/event.json` and `publish/out/40/announcement.json`.

GATE: PASS (merge and deploy verified; article accepted by 11/12 and announcement by 11/12 configured relays; exact-id readback article=10, announcement=10, floor=5)
