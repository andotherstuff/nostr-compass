# Compass publication log — 2026-09-23

Issue: Nostr Compass #41
Draft PR: https://github.com/andotherstuff/nostr-compass/pull/177
Deployed page: https://nostrcompass.org/en/newsletters/2026-09-23-newsletter/

## Publication prerequisites

- Quality composite: `/opt/data/compass-worktrees/2026-09-23/publish/out/41/quality-composite.json` (6561fec54899b48901406a07d650d184aacb4ced59c598bf828977829d31dcba)
- Feedback snapshot: `publish/out/41/quality/feedback.json` (8c003784d038be182a242564c13687be522eaef4b28a0b6d54b753b2502c38a5)
- Edition authorization: `publish/out/41/quality/authorization.json` (373767f0c229c39e538caa8167e4652ea846c8f44a254cca6f4634f3b5b4ebcf)

## Merge and deployment

- PR #177 squash-merged into `main` as commit `7bb4eb1`.
- GitHub Pages workflow https://github.com/andotherstuff/nostr-compass/actions/runs/35958588406 concluded `success`.
- The canonical URL returned HTTP 200 and contained `Nostr Compass #41`.

## Nostr publication

- Kind 30023 event ID: `f673e9a69be03b0f4e3a55019ed3427c7e503ef3c340e51d5a02c0f616ae1018`
  - `d` tag `newsletter-41`, `published_at` `1790226581` (2026-09-24T05:09:41Z)
  - Banner image https://image.nostr.build/fbf98ad0d8f84fd6b60fd920c0364df3549ea7a2e0ca16a159202a2cd87b8baf.png
- Kind 1 event ID: `465146ddf28be408347133d9249393123a2b121134102caecaa1ead23a9c44d6`
  - Created at `1790226591` (2026-09-24T05:09:51Z)
- Article: https://njump.me/naddr1qvzqqqr4gupzqa6e2nmnzsgjfzdy520vdy4hywr06c9ue6crpr2zxyq749uu275qqyxhwumn8ghj7mn0wvhxcmmvqyt8wumn8ghj7un9d3shjtnswf5k6ctv9ehx2aqprpmhxue69uhhyetvv9ujuumwdae8gtnnda3kjctvqy2hwumn8ghj7un9d3shjtnwdaehgu3wdejhgqqddejhwumvv468getj956rzuc2pfw
- Announcement: https://njump.me/nevent1qgs8wk257uc5zyjgnf9znmrf9dersm7kp0xwkqcg6s33q84f08zh4qqpp4mhxue69uhkummn9ekx7mqpzemhxue69uhhyetvv9ujuurjd9kkzmpwdejhgqpqgeg5dh0j30jqsdr3x0vjfyunzgazkys3xsgzetk2584dyw5ugntqmavxxz
- Signed events and receipts: `publish/out/41/`; ledger entry in `publish/published.json`.

### Broadcast fan-out

`publish/config/relays.json` configures 12 targets. The article was accepted by 9 and the announcement by 9.

Rejections and failures:

- article, `wss://relay.mostr.pub`: socket: WebSocket connection to 'wss://relay.mostr.pub/' failed: Expected 101 status code
- article, `wss://offchain.pub`: Policy violated and pubkey is not in our web of trust.
- article, `wss://wot.nostr.party`: socket: WebSocket connection to 'wss://wot.nostr.party/' failed: Expected 101 status code
- announcement, `wss://relay.mostr.pub`: socket: WebSocket connection to 'wss://relay.mostr.pub/' failed: Expected 101 status code
- announcement, `wss://wot.nostr.party`: socket: WebSocket connection to 'wss://wot.nostr.party/' failed: Expected 101 status code
- announcement, `wss://relay.snort.social`: timeout waiting for OK

`wss://relay.snort.social` is also an `naddr` hint relay, so that hint will not resolve there until the event is rebroadcast.

`wss://sendit.nosflare.com` is a write-only NIP-66 blaster; acceptance counts as fan-out and is excluded from readback evidence.

### Independent readback

Exact-id queries against the 11 durable configured relays after broadcast:

- both events returned by 7: `wss://nos.lol`, `wss://relay.primal.net`, `wss://relay.nostr.net`, `wss://nostr.mom`, `wss://nostr.data.haus`, `wss://nostr.oxtr.dev`, `wss://relay.nostr.com`
- only the article returned by `wss://relay.snort.social`
- only the announcement returned by `wss://offchain.pub`
- neither event returned by: `wss://relay.mostr.pub`, `wss://wot.nostr.party`

The signed events are archived to the untracked local store at `data/newsletter_workspace/published/2026-09-23_30023.json` and `data/newsletter_workspace/published/2026-09-23_1.json`, byte-identical to `publish/out/41/event.json` and `publish/out/41/announcement.json`.

GATE: PASS (merge and deploy verified; article accepted by 9/12 and announcement by 9/12 configured relays; exact-id readback article=8, announcement=8, floor=5)
