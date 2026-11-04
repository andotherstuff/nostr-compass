# Compass publication log: 2026-11-04

Issue: Nostr Compass #47
Draft PR: https://github.com/andotherstuff/nostr-compass/pull/196
Deployed page: https://nostrcompass.org/en/newsletters/2026-11-04-newsletter/

## Publication prerequisites

- Newsletter source: https://github.com/andotherstuff/nostr-compass/commit/3fd795bb8c65c71b7f9109da33bdfc344710d532
- Source observations remain partial: eighteen repositories were unavailable, six discovery lookups timed out, and ten heartbeat pages were inaccessible.

## Merge and deployment

- PR #196 merged into `main` as commit `3d75c6e`.
- GitHub Pages workflow https://github.com/andotherstuff/nostr-compass/actions/runs/41910391153 concluded `success`.
- The canonical URL returned HTTP 200 and contained `Nostr Compass #47`.

## Nostr publication

- Kind 30023 event ID: `843f6fc537a8510f65b87ee9091a3b369beb28359d0599098eb1f86a97631809`
  - `d` tag `newsletter-47`, `published_at` `1793825564` (2026-11-04T20:52:44Z)
  - Banner image https://image.nostr.build/fbf98ad0d8f84fd6b60fd920c0364df3549ea7a2e0ca16a159202a2cd87b8baf.png
- Kind 1 event ID: `66f0298f817b1ce6d34154225be416249a40e8709e6d12e94164258b3185faac`
  - Created at `1793825602` (2026-11-04T20:53:22Z)
- Article: https://njump.me/naddr1qvzqqqr4gupzqa6e2nmnzsgjfzdy520vdy4hywr06c9ue6crpr2zxyq749uu275qqyxhwumn8ghj7mn0wvhxcmmvqyt8wumn8ghj7un9d3shjtnswf5k6ctv9ehx2aqprpmhxue69uhhyetvv9ujuumwdae8gtnnda3kjctvqy2hwumn8ghj7un9d3shjtnwdaehgu3wdejhgqqddejhwumvv468getj956rwdxvtcf
- Announcement: https://njump.me/nevent1qgs8wk257uc5zyjgnf9znmrf9dersm7kp0xwkqcg6s33q84f08zh4qqpp4mhxue69uhkummn9ekx7mqpzemhxue69uhhyetvv9ujuurjd9kkzmpwdejhgqpqvmcznrup0vwwd56p2s39heqkyjdyp6rsnek3962pvsjckvv9l2kqwd8y5n

### Broadcast fan-out

`publish/config/relays.json` configures 12 targets. The article was accepted by 11 and the announcement by 11.

Rejections and failures:

- article, `wss://relay.mostr.pub`: socket: Unexpected server response: 301
- announcement, `wss://relay.mostr.pub`: socket: Unexpected server response: 301

`wss://sendit.nosflare.com` is a write-only NIP-66 blaster; acceptance counts as fan-out and is excluded from readback evidence.

### Independent readback

Exact-id queries against the 11 durable configured relays after broadcast:

- both events returned by 10: `wss://nos.lol`, `wss://relay.primal.net`, `wss://relay.snort.social`, `wss://relay.nostr.net`, `wss://nostr.mom`, `wss://offchain.pub`, `wss://nostr.data.haus`, `wss://wot.nostr.party`, `wss://nostr.oxtr.dev`, `wss://relay.nostr.com`
- neither event returned by: `wss://relay.mostr.pub`

GATE: PASS (merge and deploy verified; article accepted by 11/12 and announcement by 11/12 configured relays; exact-id readback article=10, announcement=10, floor=5)
