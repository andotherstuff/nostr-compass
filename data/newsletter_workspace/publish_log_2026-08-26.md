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
- Pipeline ledger: `publish/published.json` records issue 37; signed events and receipts are under `publish/out/37/`.

### Broadcast fan-out

`publish/config/relays.json` configures twelve targets. Both events received `OK`
from eleven of them. `wss://relay.snort.social` failed at the WebSocket handshake
(`Expected 101 status code`) for the article and the announcement, so the relay was
unreachable during the run rather than rejecting either event. It remains one of the
four `naddr` hint relays, so that hint will not resolve there until the event is
rebroadcast.

`wss://sendit.nosflare.com` is a write-only NIP-66 blaster; its `OK` counts as
fan-out acceptance and is excluded from readback evidence.

### Independent readback

Every one of the ten durable configured relays that accepted the broadcast returned
both events by exact ID on an independent query:

`wss://nos.lol`, `wss://relay.primal.net`, `wss://relay.nostr.net`,
`wss://nostr.mom`, `wss://offchain.pub`, `wss://nostr.data.haus`,
`wss://relay.mostr.pub`, `wss://wot.nostr.party`, `wss://nostr.oxtr.dev`,
`wss://relay.nostr.com`.

The signed events were also archived to the untracked local store at
`data/newsletter_workspace/published/2026-08-26_30023.json` and
`data/newsletter_workspace/published/2026-08-26_1.json`; both are byte-identical to
`publish/out/37/event.json` and `publish/out/37/announcement.json` and both pass
`nak verify`.

GATE: PASS (PR #139 merged; GitHub Pages deploy passed; canonical page HTTP 200 with issue title; both events accepted by 11/12 configured relays and recovered by exact ID from all 10 durable accepting relays)
