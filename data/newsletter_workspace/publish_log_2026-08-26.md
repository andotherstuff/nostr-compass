# Compass publication log — 2026-08-26

Issue: Nostr Compass #37
Draft PR: https://github.com/andotherstuff/nostr-compass/pull/139
Deployed page: https://nostrcompass.org/en/newsletters/2026-08-26-newsletter/

## Publication prerequisites

- Pre-publication refresh (`prepublish_refresh_2026-08-26.md`): ends in GATE: PASS
- Final delta refresh (`final_delta_refresh_2026-08-26.md`): ends in GATE: PASS
- Stage 8 review handoff (`handoff_2026-08-26.md`): ends in GATE: PASS

## Merge and deployment

- PR #139 squash-merged into `main` at `2026-08-26T16:57:47Z` as commit `1acecf4`.
- GitHub Pages workflow https://github.com/andotherstuff/nostr-compass/actions/runs/32992017015 concluded `success`.
- The canonical URL returned HTTP 200 and contained `Nostr Compass #37`.

## Nostr publication

- **Replaced after first publication.** The addressable event was re-signed and rebroadcast at 2026-08-27T08:10:03Z on the same `d` tag, so the event id below differs from the one recorded at first publication. `published_at` is preserved.

- Kind 30023 event ID: `e0511f5695af97a5fdc066b5377fd0a3b155383f0c24bee451b1a22ceefeaafc`
  - `d` tag `newsletter-37`, `published_at` `1787763698` (2026-08-26T17:01:38Z)
  - Banner image https://image.nostr.build/fbf98ad0d8f84fd6b60fd920c0364df3549ea7a2e0ca16a159202a2cd87b8baf.png
- Kind 1 event ID: `f595842931c116e3b07e9fe50d249b02996908235f86df2c49b1fc357d766837`
  - Created at `1787763754` (2026-08-26T17:02:34Z)
- Article: https://njump.me/naddr1qvzqqqr4gupzqa6e2nmnzsgjfzdy520vdy4hywr06c9ue6crpr2zxyq749uu275qqyxhwumn8ghj7mn0wvhxcmmvqyt8wumn8ghj7un9d3shjtnswf5k6ctv9ehx2aqprpmhxue69uhhyetvv9ujuumwdae8gtnnda3kjctvqy2hwumn8ghj7un9d3shjtnwdaehgu3wdejhgqqddejhwumvv468getj95enwd439wn
- Announcement: https://njump.me/nevent1qgs8wk257uc5zyjgnf9znmrf9dersm7kp0xwkqcg6s33q84f08zh4qqpp4mhxue69uhkummn9ekx7mqpzemhxue69uhhyetvv9ujuurjd9kkzmpwdejhgqpq7k2cg2f3cytw8vr7nljs6fymq2vkjzprt7rd7tzfk87r2ltkdqmsnfvvd2
- Signed events and receipts: `publish/out/37/`; ledger entry in `publish/published.json`.

### Broadcast fan-out

`publish/config/relays.json` configures 12 targets. The article was accepted by 11 and the announcement by 11.

Rejections and failures:

- article, `wss://relay.snort.social`: socket: WebSocket connection to 'wss://relay.snort.social/' failed: Expected 101 status code
- announcement, `wss://relay.snort.social`: socket: WebSocket connection to 'wss://relay.snort.social/' failed: Expected 101 status code

`wss://relay.snort.social` is also an `naddr` hint relay, so that hint will not resolve there until the event is rebroadcast.

`wss://sendit.nosflare.com` is a write-only NIP-66 blaster; acceptance counts as fan-out and is excluded from readback evidence.

### Independent readback

Exact-id queries against the 10 durable configured relays after broadcast:

- both events returned by 10: `wss://nos.lol`, `wss://relay.primal.net`, `wss://relay.nostr.net`, `wss://nostr.mom`, `wss://offchain.pub`, `wss://nostr.data.haus`, `wss://relay.mostr.pub`, `wss://wot.nostr.party`, `wss://nostr.oxtr.dev`, `wss://relay.nostr.com`

The signed events are archived to the untracked local store at `data/newsletter_workspace/published/2026-08-26_30023.json` and `data/newsletter_workspace/published/2026-08-26_1.json`, byte-identical to `publish/out/37/event.json` and `publish/out/37/announcement.json`.

GATE: PASS (merge and deploy verified; article accepted by 11/12 and announcement by 11/12 configured relays; both events recovered by exact id from 10 durable relays)
