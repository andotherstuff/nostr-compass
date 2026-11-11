# Compass publication log: 2026-11-11

Issue: Nostr Compass #48
Draft PR: https://github.com/andotherstuff/nostr-compass/pull/199
Deployed page: https://nostrcompass.org/en/newsletters/2026-11-11-newsletter/

## Publication prerequisites

- Newsletter source: https://github.com/andotherstuff/nostr-compass/commit/d8ae5955f393902684b77e777482ba49e50bae0b

## Merge and deployment

- PR #199 merged into `main` as commit `2edd989`.
- GitHub Pages workflow https://github.com/andotherstuff/nostr-compass/actions/runs/43058133312 concluded `success`.
- The canonical URL returned HTTP 200 and contained `Nostr Compass #48`.

## Nostr publication

- Kind 30023 event ID: `b8480a9cb0fb56453570811952133897a7daf4a659e42f4e57bf9130d852b731`
  - `d` tag `newsletter-48`, `published_at` `1794414743` (2026-11-11T16:32:23Z)
  - Banner image https://image.nostr.build/fbf98ad0d8f84fd6b60fd920c0364df3549ea7a2e0ca16a159202a2cd87b8baf.png
- Kind 1 event ID: `1123475910dd119b187de278eca8eb8c700756c1a84981a5f9ce5331e2633f39`
  - Created at `1794414761` (2026-11-11T16:32:41Z)
- Article: https://njump.me/naddr1qvzqqqr4gupzqa6e2nmnzsgjfzdy520vdy4hywr06c9ue6crpr2zxyq749uu275qqyxhwumn8ghj7mn0wvhxcmmvqyt8wumn8ghj7un9d3shjtnswf5k6ctv9ehx2aqprpmhxue69uhhyetvv9ujuumwdae8gtnnda3kjctvqy2hwumn8ghj7un9d3shjtnwdaehgu3wdejhgqqddejhwumvv468getj956rs6ur60s
- Announcement: https://njump.me/nevent1qgs8wk257uc5zyjgnf9znmrf9dersm7kp0xwkqcg6s33q84f08zh4qqpp4mhxue69uhkummn9ekx7mqpzemhxue69uhhyetvv9ujuurjd9kkzmpwdejhgqpqzy35wkgsm5gekxraufuwe28t33cqw4kp4pycrf0eeefnrcnr8uus88g3ur

### Broadcast fan-out

`publish/config/relays.json` configures 12 targets. The article was accepted by 9 and the announcement by 9.

Rejections and failures:

- article, `wss://relay.mostr.pub`: socket: Unexpected server response: 301
- article, `wss://nos.lol`: timeout waiting for OK
- article, `wss://nostr.mom`: timeout waiting for OK
- announcement, `wss://relay.mostr.pub`: socket: Unexpected server response: 301
- announcement, `wss://nos.lol`: timeout waiting for OK
- announcement, `wss://nostr.mom`: timeout waiting for OK

`wss://nos.lol` is also an `naddr` hint relay, so that hint will not resolve there until the event is rebroadcast.

`wss://sendit.nosflare.com` is a write-only NIP-66 blaster; acceptance counts as fan-out and is excluded from readback evidence.

### Independent readback

Exact-id queries against the 11 durable configured relays after broadcast:

- both events returned by 7: `wss://relay.primal.net`, `wss://relay.snort.social`, `wss://relay.nostr.net`, `wss://offchain.pub`, `wss://nostr.data.haus`, `wss://wot.nostr.party`, `wss://relay.nostr.com`
- neither event returned by: `wss://nos.lol`, `wss://nostr.mom`, `wss://relay.mostr.pub`, `wss://nostr.oxtr.dev`

GATE: PASS (merge and deploy verified; article accepted by 9/12 and announcement by 9/12 configured relays; exact-id readback article=7, announcement=7, floor=5)
