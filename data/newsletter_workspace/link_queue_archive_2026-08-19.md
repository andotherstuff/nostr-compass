## 2026-08-13T08:52:43Z — Glow

- Source: https://breez.technology/glow/
- Editorial note: Apparently, Glow is using Nostr for some wallet metadata stuff, so add it to our projects and include for the next newsletter.
- Prep (verified 2026-08-13): Canonical repositories are https://github.com/breez/glow-web (PWA) and https://github.com/breez/glow-app (native iOS/Android wrapper). Source inspection at glow-web commit `488fe66bb37bfd6f83ba99a4ce8255e35f0332d9` shows passkey-derived wallet labels being listed from and saved to Nostr relays in `src/services/passkeyService.ts`. Glow has been added to `data/projects.yml`; triage its Nostr-backed wallet-label metadata as a Newly Discovered project for the next newsletter.

## 2026-08-14T10:44:59Z — Cambium

- Source: https://github.com/forgesworn/cambium
- Editorial note: For next week.
- Prep (verified 2026-08-14): Cambium is already tracked in `data/projects.yml` as an active Android NIP-55 signer that holds no private key material and proxies signing requests over NIP-46 to a companion Heartwood hardware signer. GitHub describes the same architecture; the repository's current default-branch head is `984dfd3bb0ece45314e18cec47b6da9c1dcc303f` (2026-08-14). Triage its current activity for next week's issue.
