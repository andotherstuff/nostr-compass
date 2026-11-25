# Compass publication log for 2026-11-25

Nostr Compass #50 published on the website and on Nostr.

- [Newsletter PR](https://github.com/andotherstuff/nostr-compass/pull/204) merged as `1bfb40b0f37f96218f96ef6b03f4564076e4b590`.
- [GitHub Pages deployment](https://github.com/andotherstuff/nostr-compass/actions/runs/45651211259) succeeded for that commit.
- [Canonical newsletter](https://nostrcompass.org/en/newsletters/2026-11-25-newsletter/) returned HTTP 200 and contained the published edition.
- Published Markdown SHA-256 `7e39a7f7b461d50626aa19494881734086d76f6d7c8148fbdfe0502ca2513d1d`.

## Nostr publication

- The [article](https://njump.me/naddr1qvzqqqr4gupzqa6e2nmnzsgjfzdy520vdy4hywr06c9ue6crpr2zxyq749uu275qqyt8wumn8ghj7un9d3shjtnswf5k6ctv9ehx2aqprpmhxue69uhhyetvv9ujuumwdae8gtnnda3kjctvqy2hwumn8ghj7un9d3shjtnwdaehgu3wdejhgqg4waehxw309aex2mrp0yhxg6t5w3hjuur4vgqq6mn9waekcet5w3jhytf4xq7gxgdh) has kind 30023, `d` tag `newsletter-50` and event ID `3671f19eefd2f055c97c6e81e6077cbcd07e67a2a045d63a6612d5bfc2a49d01`. Its published time is 2026-11-25 16:09:29 UTC.
- The [announcement](https://njump.me/nevent1qvzqqqqqqypzqa6e2nmnzsgjfzdy520vdy4hywr06c9ue6crpr2zxyq749uu275qqyxhwumn8ghj7mn0wvhxcmmvqyt8wumn8ghj7un9d3shjtnswf5k6ctv9ehx2aqprpmhxue69uhhyetvv9ujuumwdae8gtnnda3kjctvqy2hwumn8ghj7un9d3shjtnwdaehgu3wdejhgqpqcw4ct82fr9tr88ez64esp36puhregc96ruvqvfn74s87sc67f9ssyuzdq8) has kind 1 and event ID `c3ab859d491956339f22d57300c741e5c79460ba1f1806267eac0fe8635e4961`. It was created at 2026-11-25 16:19:30 UTC.

## Relay verification

- The article received 6 positive acknowledgements across 15 targets. Exact signed-event readback succeeded on 5 durable relays, including 3 from the configured list.
  - `wss://relay.primal.net`, `wss://relay.snort.social`, `wss://relay.nostr.net`, `wss://relay.ditto.pub`, `wss://relay.illuminodes.com`
- The announcement received 13 positive acknowledgements across 15 targets. Exact signed-event readback succeeded on 11 durable relays, including 9 from the configured list.
  - `wss://nos.lol`, `wss://relay.primal.net`, `wss://relay.snort.social`, `wss://relay.nostr.net`, `wss://nostr.mom`, `wss://offchain.pub`, `wss://nostr.data.haus`, `wss://wot.nostr.party`, `wss://relay.nostr.com`, `wss://relay.ditto.pub`, `wss://relay.illuminodes.com`

The readbacks matched each event ID, signature and signed field. Write-only blaster acknowledgements count toward fan-out acceptance.

GATE: PASS (website deployed, article readback 5, announcement readback 11, durable relay floor 5).
