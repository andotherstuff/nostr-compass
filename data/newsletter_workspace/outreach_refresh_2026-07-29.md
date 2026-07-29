# Publication-day targeted outreach dry run

Generated: 2026-07-29T14:12:17Z
Issue: Nostr Compass #33
Review PR: https://github.com/andotherstuff/nostr-compass/pull/118
Podcast invitation: Logbook nsite, Thursday, 30 July at 16:00 UTC

## Scope

The publication-day refresh introduced Kairos, Shosho 1.0.0, Keep's Android signer changes, Routstrd's bind-default change, and Mill's backup draft. Primary evidence resolved the following de-duplicated NIP-17 recipients:

- Kairos + LWB maintainer: `npub1vjxq75czca0nswp2f5kgtfyzhynuccdjs29q098rd3kv09k7s6nq39hh7v`
- Mill + 0ceanSlim maintainer: `npub1zmc6qyqdfnllhnzzxr5wpepfpnzcf8q6m3jdveflmgruqvd3qa9sjv7f60`
- Routstrd project account: `npub130mznv74rxs032peqym6g3wqavh472623mt3z5w73xq9r6qqdufs7ql29s`
- Shosho publisher: `npub1sh0spghk4yvy2d2v35kelw45qq4msk6zykaw4ds047e9slzs8r4qr7q2xa`
- Keep / wksantiago maintainer: `npub1h3fzzzeq60acjvnyvw34rpn5clkaueteffmkt3ln4ygekg9lcm0qhw96sj`

## Execution

The targeted dry run selected exactly five unique recipients and wrote:

`publish/out/dm-outreach-33-kairos-shosho-publisher-wksantiago-maintainer-routstrd-project-account-mill-plan.json`

The plan records `really_send: false`; no DM was signed or sent. The 14:00 UTC refresh job is prohibited from invoking Amber or creating signed events, so the 16:00 publication worker must review this plan and perform any approved targeted send before publication. The full issue campaign must not be resent. `data/npubs.yml` `no_dm` exclusions remain active.

GATE: PASS (targeted dry-run plan contains five de-duplicated NIP-17 recipients; zero messages signed or sent)
