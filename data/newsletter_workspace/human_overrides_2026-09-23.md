# Human overrides — 2026-09-23

These inclusions preserve direct user requests that an earlier weekly pass missed. Stage 5 must treat both as mandatory and must not silently drop them on resume.

## MintRadar

- Include MintRadar as a Top Story or equivalent project update.
- Explain that MintRadar is a privacy-first Cashu mint dashboard using Nostr for mint discovery and community review identities.
- Primary queued event: https://njump.to/nevent1qqs9hwth0rgsprqaml9xuuve2s47x08w2ltjujgwwr4zyqw0qjptecqpzamhxue69uhhyetvv9ujuurjd9kkzmpwdejhgtczyqt40x2js6hcc27delgn5vqwn3qtcjn8uas3rrzmxe2hxsrvdvmmcqcyqqqqqqgyqg6ap
- Current source: https://github.com/hroomnik007/MintRadar
- Current-window milestones include NIP-87 announcement persistence, same-operator detection through NUT-06 pubkeys, shareable comparison URLs, and Nostr `naddr` deep links.

## fips-initramfs 0.1.0

- Include the first fips-initramfs release as a Top Story or alongside fips2go.
- Explain that it places a FIPS mesh node inside initramfs so an operator can unlock a LUKS-encrypted root over an npub-addressed mesh before the normal system boots.
- Primary release: https://github.com/jmcorgan/fips-initramfs/releases/tag/v0.1.0
- Date the release as 2026-09-06 and identify it as a user-requested catch-up item, not an in-window release.
- Preserve the release's security caveats: the initramfs contains the node key, remote unlock sends the passphrase through SSH over FIPS, and console unlock remains available.

GATE: PASS (two direct-user catch-up items have primary sources, selection placement, date constraints, and durable Stage 5 instructions)