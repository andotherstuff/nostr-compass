# Publication-day targeted outreach plan: 2026-07-29

Generated: 2026-07-29 13:49 UTC
Updated: 2026-07-29 14:34 UTC
Issue: Nostr Compass #33
Review PR: https://github.com/andotherstuff/nostr-compass/pull/118
Podcast invitation: Riverside Logbook session, Thursday, 30 July 2026 at 16:00 UTC

## Scope

This artifact records dry-run plans only. The Wednesday 14:00 UTC refresh must not invoke Amber, sign events, or send DMs. The 16:00 publication worker may execute the reviewed targeted plans after its publication gates pass.

### Initial refresh additions

Command: `COMPASS_PUBLISH_INVOCATION=manual bun publish/dm-outreach.ts 33 --pr-url <PR> --podcast-url <URL> --podcast-time <TIME> --only Kairos --only 'Shosho publisher' --only 'wksantiago maintainer' --only 'Routstrd project account' --only Mill`

Result: 5 unique planned recipients, all NIP-17, 0 sent.

Receipt: `publish/out/dm-outreach-33-kairos-shosho-publisher-wksantiago-maintainer-routstrd-project-account-mill-plan.json`

### Audit additions: Bray and Buzz Desktop

Primary identity evidence:

- Bray's repository links `https://forgesworn.dev`. Its live NIP-05 document at `https://forgesworn.dev/.well-known/nostr.json` maps `_` and `darren` to hex pubkey `da19f1cd34beca44be74da4b306d9d1dd86b6343cef94ce22c49c6f59816e5bd`, encoded as `npub1mgvlrnf5hm9yf0n5mf9nqmvarhvxkc6remu5ec3vf8r0txqkuk7su0e7q2`. Bray and Darren therefore share one recipient.
- Buzz Desktop belongs to Block's `block/buzz` repository. The pre-existing Block Open Source key in `data/npubs.yml`, `npub16l0ck0s5zened29dsaqtqm6z0t4fmk2mwtszw64fz7fppcnls8mss3yj9s`, decodes successfully and was independently recovered as a kind 0 Block Open Source profile from `wss://nos.lol` and `wss://purplepag.es`. Buzz Desktop and the Block maintainer alias share one recipient.
- `data/npubs.yml` retains the existing `no_dm` list; no exclusion was removed or bypassed.

Command: `COMPASS_PUBLISH_INVOCATION=manual bun publish/dm-outreach.ts 33 --pr-url <PR> --podcast-url <URL> --podcast-time <TIME> --only 'Buzz Desktop' --only 'block maintainer' --only Bray --only 'Darren maintainer'`

Result: 2 unique planned recipients after project/maintainer de-duplication, both NIP-17, 0 sent.

Receipt: `publish/out/dm-outreach-33-buzz-desktop-block-maintainer-bray-darren-maintainer-plan.json`

## Publication handoff

The publication worker should review the two targeted plan receipts, then run each exact scope with `--really-send` only after the 16:00 UTC clock gate, refresh PASS, PR/deployment gates, and Amber authorization all pass. It must not resend the full issue campaign.

GATE: PASS (two dry-run receipts verified; 7 unique targeted recipients planned across the refresh, 0 DMs sent, `no_dm` preserved, checked 2026-07-29T14:34:24Z)
