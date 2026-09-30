# Compass #42 prose review

Draft: `content/en/newsletters/2026-09-30-newsletter.md`

Snapshot SHA-256: `08440bb4505bc8a32ac3b907f1a6cf2b4917ab82873ddc3998ba39c47e28e705`

Reviewer: Codex same-family editorial audit, 2026-09-29. This report is not an independent model review.

## Executed checks on this exact draft

- `/opt/data/.local/bin/bun /opt/data/tmp/compass-shaka/src/index.ts scan content/en/newsletters/2026-09-30-newsletter.md`: **85/100 PASS**, 7,251 words, 0 cardinal sins, 0 banned constructions, 0 AI tells, 0 dash violations, and 0 hedging. It reports three instances of `unlock` at lines 96 and 98. Those describe Cambium's literal device-unlock feature, so the proposed “enable” or “reveal” replacements would change the product meaning. Its three rhythm suggestions at lines 114, 124, and 152 are nonblocking. The isolated scanner path was used because `shaka` is absent from this Codex shell.
- `python3 scripts/check_newsletter_style.py content/en/newsletters/2026-09-30-newsletter.md`: **PASS** for Compass filler phrases, opaque security link anchors, and specification H3 structure.
- `python3 scripts/check_newsletter_paragraph_links.py content/en/newsletters/2026-09-30-newsletter.md`: **PASS**; each prose paragraph includes a repository or primary-source link.
- `rg -n -i '\brather than\b|\bclearly\b|The contrast with|\[(GHSA|CVE)-|—' content/en/newsletters/2026-09-30-newsletter.md`: zero matches.
- `git diff --check`: zero whitespace errors.

The previous PASS snapshot used SHA-256 `59b121d6714eba62590ad48afae4c828dc4c0fcf134c68350bb85c97cf4498c7`. Five Markdown topic links were removed from H3 headings to restore clean Hugo anchors. The body first-mention inventory below remains valid; all listed checks were rerun on the SHA above.

## Project first-mention inventory

The opening **This week** paragraph is navigation; the inventory checks first mentions in each H2 body's prose. Every featured item has a one-sentence description, including newly introduced projects and historical examples.

| Section | Projects checked | Result |
| --- | --- | --- |
| Top Stories | Holoboard, fips-pub-domains, Marmot MDK, Myco; secondary FIPS, fips2go, Amber | PASS. FIPS is described as an encrypted mesh using Nostr for discovery; fips2go as its phone client; Amber as an Android signer. |
| Tagged Releases | nostream, Nostr double ratchet, Scramble, Amber, FIPS, napplet.soy/soyLI, Dart NDK, Mostro Core, Cambium, Bray, Mafrend, Sonar, Elisym, Flotilla, Ditto, Iris Chat, LibreNostr, Newlay, ngit-grasp, Armada, deed; secondary Heartwood, Sapwood, Tenna | PASS. Each featured release opens with its product role. Heartwood is a hardware key, Sapwood the board's enrollment interface, and Tenna a host app embedding Armada. |
| In Development | Amethyst, Divine, Buzz, Conduit, Mostro, Elisym, nostter, Pensieve, ContextVM, Cyberspace, Wisp, Cordn, Nostr Atlas, nostr-java, Zap Cooking, Opal, WatchTower, Hubstr Blossom, Meshstr, Dossier; secondary White Noise, Geode, Quartz, strfry, Omarchy | PASS. White Noise is named as another Marmot messenger, Geode as a relay, Quartz as a client, strfry as a Nostr relay, and Omarchy as a Linux environment. |
| Protocol and Spec Work | fips-pub-domains, FIPS, Roadstr | PASS. The reference implementation, the encrypted key-addressed FIPS mesh (line 288), and road-condition-reporting clients (line 302) are explained. |
| Six Years of Nostr Septembers | BUber, Loquaz, Damus | PASS. Their first mentions explain ride matching, desktop chat, and Nostr social-client roles. |

Generic software, operating systems, and distribution platforms such as PostgreSQL, Android, Tor, F-Droid, and GitHub were excluded from the Compass project-feature inventory.

## NIP first-mention inventory by section

The first prose paragraph containing each listed identifier describes its purpose in plain language. Open project-proposal labels (`NIP-DB`, `NIP-FE`, `NIP-AR`, `NIP-FI`) remain identified as proposals, not accepted numbered NIPs.

| Section | Identifiers checked | Result |
| --- | --- | --- |
| Top Stories | NIP-17, NIP-04, NIP-DB | PASS. Private gift wraps, legacy direct-message encryption, and the domain-binding proposal receive context. |
| Tagged Releases | No NIP identifiers in the assembled section. | PASS. |
| In Development | NIP-17, NIP-FE, NIP-AR, NIP-98, NIP-FI, NIP-46, NIP-59, NIP-01, NIP-22, NIP-39, NIP-78, NIP-13, NIP-92, NIP-86, NIP-94, NIP-77, NIP-04, NIP-07 | PASS. The former gaps at lines 176, 240, 256, 260, and 266 now identify gift-wrapped messages, application-specific data events, file metadata events, event-set reconciliation, and legacy encrypted direct messages. |
| Protocol and Spec Work | NIP-39, NIP-86, NIP-43, NIP-51, NIP-DB, NIP-40 | PASS. NIP-43 is described as restricted-relay membership and admission; NIP-40 as an event-expiration timestamp. |
| Six Years of Nostr Septembers | NIP-28, NIP-26, NIP-24, NIP-65, NIP-84, NIP-34, NIP-73, NIP-42, NIP-47, NIP-51, NIP-39 | PASS. Historical first-use clauses explain each identifier's function. |

GATE: PASS
