# Compass publication log: 2026-11-18

Issue: Nostr Compass #49 (published retrospectively on 2026-11-20)
PR: https://github.com/andotherstuff/nostr-compass/pull/202
Deployed page: https://nostrcompass.org/en/newsletters/2026-11-18-newsletter/

## Publication prerequisites

- Newsletter source: https://github.com/andotherstuff/nostr-compass/commit/f84ebc980b4dfc3b5f879c99f9e4b0cbb0325713

## Merge and deployment

- PR #202 merged into `main` as commit `560b12f`.
- GitHub Pages workflow https://github.com/andotherstuff/nostr-compass/actions/runs/44802666303 concluded `success`.
- The canonical URL returned HTTP 200 and contained `Nostr Compass #49`.

## Nostr publication

- Kind 30023 event ID: `bf8f23e7a75e18ddd2fb21db0e7bce2e9ecb5bef151757c5ff5a51f0516eac0b`
  - `d` tag `newsletter-49`, `published_at` `1795208476` (2026-11-20T21:01:16Z)
  - Banner image https://image.nostr.build/fbf98ad0d8f84fd6b60fd920c0364df3549ea7a2e0ca16a159202a2cd87b8baf.png
  - Content is 324,214 bytes, which is larger than the message limit of most configured relays.
- Kind 1 event ID: `46e9744f841fe1df74b608117cc3ada2372eee15a8f32fd9bce6c42d7c23ed26`
  - Created at `1795210715` (2026-11-20T21:38:35Z)
- Article: https://njump.me/naddr1qvzqqqr4gupzqa6e2nmnzsgjfzdy520vdy4hywr06c9ue6crpr2zxyq749uu275qqyt8wumn8ghj7un9d3shjtnswf5k6ctv9ehx2aqpz3mhxue69uhhyetvv9ujuerpd46hxtnfduq3samnwvaz7tmjv4kxz7fwwdhx7un59eek7cmfv9kqz9thwden5te0wfjkccte9ejxjar5duh8qatzqqxkuethwdkx2ar5v4ez6dpeyxxy9m
- Announcement: https://njump.me/nevent1qqsyd6t5f7zplcwlwjmqsytucwk6ydewac263ue0mx7wd3pd0s376fspzemhxue69uhhyetvv9ujuurjd9kkzmpwdejhgqg5waehxw309aex2mrp0yhxgctdw4eju6t0qgs8wk257uc5zyjgnf9znmrf9dersm7kp0xwkqcg6s33q84f08zh4qqd7vhvk

### Broadcast fan-out

`publish/config/relays.json` configures 12 targets; `wss://nostr-01.yakihonne.com` and `wss://nostr-02.yakihonne.com` were added as supplemental targets. The article was accepted by 3 of 14 and the announcement by 11 of 14.

Article rejections and failures:

- `wss://wot.nostr.party`: content is too large: 324222, max is 65535
- `wss://nos.lol`, `wss://nostr.mom`, `wss://offchain.pub`, `wss://nostr.data.haus`, `wss://nostr.oxtr.dev`, `wss://relay.nostr.com`, `wss://nostr-01.yakihonne.com`, `wss://nostr-02.yakihonne.com`: closed without OK
- `wss://relay.nostr.net`: opening handshake timed out
- `wss://relay.mostr.pub`: Unexpected server response: 301

Because of the article size, it was also sent to relays that accept larger messages: `wss://relay.damus.io`, `wss://relay.ditto.pub` and `wss://relay.illuminodes.com`. The `naddr` hints point at `wss://relay.primal.net`, `wss://relay.damus.io`, `wss://relay.snort.social` and `wss://relay.ditto.pub`.

Announcement failures:

- `wss://relay.nostr.net`: opening handshake timed out
- `wss://relay.mostr.pub`: Unexpected server response: 301
- `wss://nostr.oxtr.dev`: Unexpected server response: 502

`wss://sendit.nosflare.com` is a write-only NIP-66 blaster; acceptance counts as fan-out and is excluded from readback evidence.

### Independent readback

Exact-id queries after broadcast, with id, signature and every field compared:

- article returned by 5: `wss://relay.primal.net`, `wss://relay.snort.social` (configured), `wss://relay.damus.io`, `wss://relay.ditto.pub`, `wss://relay.illuminodes.com` (supplemental)
- announcement returned by 9: `wss://nos.lol`, `wss://relay.primal.net`, `wss://relay.snort.social`, `wss://nostr.mom`, `wss://offchain.pub`, `wss://wot.nostr.party`, `wss://relay.nostr.com` (configured), `wss://nostr-01.yakihonne.com`, `wss://nostr-02.yakihonne.com` (supplemental)

GATE: PASS (merge and deploy verified; exact-id readback article=5, announcement=9, floor=5). The article reached the floor only with supplemental large-message relays; 2 configured relays hold it.
