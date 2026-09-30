# Merged PR review, N–Z — September 30

Reviewed every merged PR title for these repositories in the immutable September 21–29 project update, then inspected the primary PR descriptions for the material candidates. Exact URLs remain in `project_activity_decisions_2026-09-30.json`.

| Repository | Verdict | Evidence and reason |
|---|---|---|
| nostr-protocol/nips | Include | Merged NIP-39 proof text and claim types, NIP-86 invitation management, and NIP-51 collision correction are distinct specification changes. The other event-kind registry and formatting changes are minor or folded into these. |
| nostr-wot/nostr-wot-extension | Skip separate PR story | Current substantive NWC connection and wallet fixes are covered by the tagged release series; theme changes are lower impact. |
| Origami74/myco | Skip separate PR story | The account, signer, app update, and relay changes are covered by the 0.8.0–0.8.1 tagged release pair. |
| penpenpng/rx-nostr | Skip | Default relay-tag filter fix is narrow; the other changes are tests and API refactoring without an independently material user story. |
| permissionlesstech/bitchat | Skip | Much of the security and transport work concerns the project's Bluetooth/geohash mesh rather than a distinct Nostr relay behavior this window. |
| relaystr/ndk | Skip separate PR story | NIP-46 response and Blossom authorization changes are covered by the new dev-tag series; other work is narrower. |
| routstr/routstrd | Skip | `nostr-sync` status and provider routing provide no independently explained change to Nostr event delivery this week. |
| saiy2k/nostr-components | Include | A new public Nostr Atlas site and the signed NIP-39 claim and profile-enrichment path are distinct from previous coverage. |
| shocknet/Lightning.Pub | Skip | This is Lightning service and debit-session work; no new Nostr application surface is established by the merged PRs. |
| shocknet/wallet2 | Skip | Intents, overlays, and dashboard checkpoint are generic wallet UI work without Nostr-specific behavior. |
| shopstr-eng/shopstr | Skip | Search relay refresh is configuration maintenance; the payout and MCP work lack a distinct Nostr interaction worth covering. |
| SnowCait/nostter | Include | Real signer capability gates, pin author/relay hints, and NIP-01 replaceable-event ordering change Nostr client behavior. Much of the 100-PR auth migration is internal support. |
| SnowCait/snowflare | Skip | Dependency-lock checks are CI maintenance. |
| tcheeric/nostr-java | Include | Blossom hosting tools expose a new Nostr media workflow through the Java SDK; preserving event-tag values in publishing also protects protocol fidelity. |
| TsukemonoGit/lumilumi | Skip | Custom-emoji and YouTube fixes are narrow, with no broader release or interoperability evidence. |
| vitorpamplona/amethyst | Include | Marmot/White Noise reactions, deletion and edit interoperability, Cordn group runtime, NIP-FE relay commands, and backup conflict handling are material merged changes. Release availability is not assumed. |
| zapcooking/frontend | Include | Lazarus replaces the account backup design with relay-history recovery; other merged PoW and attachment work merits source-level mention if it passes final review. |
| zeSchlausKwab/napplet-soy | Skip separate PR story | The only merged PR is CI repair, while current user-facing work is covered by the soyLI tagged release. |
| ZeusLN/zeus | Skip | NWC configuration crash and NIP-05 case fixes are narrow amid a Lightning-heavy set of changes; no independently material Nostr milestone. |
