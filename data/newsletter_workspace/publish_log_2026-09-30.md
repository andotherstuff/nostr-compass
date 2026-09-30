# Compass publication log — 2026-09-30

Issue: Nostr Compass #42
Draft PR: https://github.com/andotherstuff/nostr-compass/pull/183
Deployed page: https://nostrcompass.org/en/newsletters/2026-09-30-newsletter/

## Publication prerequisites

- Quality composite: `/opt/data/compass-worktrees/2026-09-30/publish/out/42/quality-composite.json` (866df241bee9fcc2652b8c45cba7caee09f740ce2e7ce653e2a3a9a57f90ce7d)
- Feedback snapshot: `publish/out/42/quality/feedback.json` (aeb856122bdb1a379d37d05ede3ff819eec0cfd6f6b4d8243dc9d9bcf8ae2c29)
- Edition authorization: `publish/out/42/quality/authorization.json` (f61fc3eb3fbaaa9a51db20c54ccc0896f70fb47cecf84308a2366009d153dc8b)

## Merge and deployment

- PR #183 squash-merged into `main` as commit `460ddba`.
- GitHub Pages workflow https://github.com/andotherstuff/nostr-compass/actions/runs/36747787225 concluded `success`.
- The canonical URL returned HTTP 200 and contained `Nostr Compass #42`.

## Nostr publication

- Kind 30023 event ID: `c5b2646bc6c0ac4c7a7667b1ceb4234040e761c55484f2d8727449e40bb9008d`
  - `d` tag `newsletter-42`, `published_at` `1790787490` (2026-09-30T16:58:10Z)
  - Banner image https://image.nostr.build/fbf98ad0d8f84fd6b60fd920c0364df3549ea7a2e0ca16a159202a2cd87b8baf.png
- Kind 1 event ID: `ffc5cdf6e7385d56f5287a139a6a2d41fbfd9ce61ca2e83b86bf55e195a4f2b1`
  - Created at `1790787598` (2026-09-30T16:59:58Z)
- Article: https://njump.me/naddr1qvzqqqr4gupzqa6e2nmnzsgjfzdy520vdy4hywr06c9ue6crpr2zxyq749uu275qqyxhwumn8ghj7mn0wvhxcmmvqyt8wumn8ghj7un9d3shjtnswf5k6ctv9ehx2aqprpmhxue69uhhyetvv9ujuumwdae8gtnnda3kjctvqy2hwumn8ghj7un9d3shjtnwdaehgu3wdejhgqqddejhwumvv468getj956ryqhfy4e
- Announcement: https://njump.me/nevent1qgs8wk257uc5zyjgnf9znmrf9dersm7kp0xwkqcg6s33q84f08zh4qqpp4mhxue69uhkummn9ekx7mqpzemhxue69uhhyetvv9ujuurjd9kkzmpwdejhgqpqllzumah88pw4dafg0gfe563dg8alm88xrj3wswuxha27r9dy72cssuerhn
- Signed events and receipts: `publish/out/42/`; ledger entry in `publish/published.json`.

### Broadcast fan-out

`publish/config/relays.json` configures 18 targets. The article was accepted by 8 and the announcement by 16.

Rejections and failures:

- article, `wss://nos.lol`: invalid: event too large: 116599
- article, `wss://nostr.mom`: invalid: event too large: 116599
- article, `wss://relay.nostr.com`: invalid: event too large: 116599
- article, `wss://nostr.data.haus`: invalid: event too large: 116599
- article, `wss://relay.mostr.pub`: socket: WebSocket connection to 'wss://relay.mostr.pub/' failed: Expected 101 status code
- article, `wss://wot.nostr.party`: socket: WebSocket connection to 'wss://wot.nostr.party/' failed: Expected 101 status code
- article, `wss://offchain.pub`: invalid: event too large: 116599
- article, `wss://nostr.bitcoiner.social`: invalid: event too large: 116599
- article, `wss://relay.damus.io`: socket: WebSocket connection to 'wss://relay.damus.io/' failed: Expected 101 status code
- article, `wss://relay.nostr.wirednet.jp`: invalid: event too large: 116599
- announcement, `wss://wot.nostr.party`: socket: WebSocket connection to 'wss://wot.nostr.party/' failed: Expected 101 status code
- announcement, `wss://relay.mostr.pub`: socket: WebSocket connection to 'wss://relay.mostr.pub/' failed: Expected 101 status code

`wss://nos.lol` is also an `naddr` hint relay, so that hint will not resolve there until the event is rebroadcast.

`wss://sendit.nosflare.com` is a write-only NIP-66 blaster; acceptance counts as fan-out and is excluded from readback evidence.

### Independent readback

Exact-id queries against the 17 durable configured relays after broadcast:

- both events returned by 6: `wss://relay.primal.net`, `wss://relay.snort.social`, `wss://relay.nostr.net`, `wss://nostr.oxtr.dev`, `wss://relay.ditto.pub`, `wss://relay.nos.social`
- only the announcement returned by `wss://nos.lol`
- only the announcement returned by `wss://nostr.mom`
- only the announcement returned by `wss://offchain.pub`
- only the announcement returned by `wss://nostr.data.haus`
- only the announcement returned by `wss://relay.nostr.com`
- only the announcement returned by `wss://nostr.bitcoiner.social`
- only the announcement returned by `wss://relay.nostr.wirednet.jp`
- neither event returned by: `wss://relay.mostr.pub`, `wss://wot.nostr.party`, `wss://relay.noswhere.com`, `wss://relay.damus.io`

The signed events are archived to the untracked local store at `data/newsletter_workspace/published/2026-09-30_30023.json` and `data/newsletter_workspace/published/2026-09-30_1.json`, byte-identical to `publish/out/42/event.json` and `publish/out/42/announcement.json`.

GATE: PASS (merge and deploy verified; article accepted by 8/18 and announcement by 16/18 configured relays; exact-id readback article=6, announcement=13, floor=5)
