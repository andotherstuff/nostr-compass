# Newsletter #33 consolidated review log

Generated: 2026-07-28 20:15:51 UTC
Target: `content/en/newsletters/2026-07-29-newsletter.md`
State: unpublished (`draft: true`)

## Editorial gates

- PASS — continuity checker compared the draft against all prior English newsletters; repeated NIP-2328/device-pairing coverage was removed.
- PASS — style checker found neither forbidden phrase (`join Shipping This Week with`, `developer-signed release expands the browser`) and no configured filler/slop patterns.
- PASS — every prose paragraph contains a repository or primary-source link.
- PASS — Amethyst 1.13.0 and mandatory Mosaico 0.1.2 coverage remain in Top Stories with verified release/PR sources.
- PASS — protocol coverage includes active NIP, BUD/Blossom, NAP, Marmot/MIP, Gamma, and Concord sources; unsupported standalone NDIP activity is not asserted.
- PASS — Sovereign Engineering discovery checked current/archive cohorts and relay activity using SovEng/SEC/SEC08 identifiers; FIPS coverage was verified against its repository and project update.
- PASS — `Six Years of Nostr Julys` covers 2021–2026 as a progressive narrative rather than a chronology or bullet list.

## Mechanical evidence

- PASS — 26 focused Python checks and 3 Bun publish-mention tests.
- PASS — mention extraction now retains lowercase hyphenated application headings such as `swift-nostr` and `lawallet-nwc` while excluding protocol/history headings.
- PASS — 88 external URLs probed; 0 failures.
- PASS — Hugo/Pagefind production build completed.
- PASS — rendered topic backlink checker: 20 topic pages with Primary sources blocks and 29 newsletter backlinks.
- PASS — `git diff --check`.

## Outreach readiness

- 20 application/project identities resolved automatically after adding the `lawallet-nwc` heading alias.
- `swift-nostr`/`yysskk` and `pakstr`/`ado` remain unresolved after repository, GitHub profile, project-site, NIP-05, and relay-search checks; no npub was guessed.
- Marmot/MDK remains on the explicit `no_dm` list.
- Outreach now requires a dated `--podcast-time` and supports draft-review URLs through `--pr-url`, preventing stale “out now” or “today” wording.

GATE: PASS
