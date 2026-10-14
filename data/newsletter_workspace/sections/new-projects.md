## New Projects

### Submarine

[Submarine 0.1.0](https://github.com/nogringo/submarine/releases/tag/v0.1.0) releases a password manager whose encrypted vaults sync over Nostr. It supports external signers and retains concurrent item versions, with Bitwarden JSON import and export. Changes are saved locally before waiting for relay acceptance. Android, desktop and CLI downloads accompany the release. The project calls it young and advises a proven manager for critical passwords; the tagged protocol specification is still empty. Its [web storage](https://github.com/nogringo/submarine/blob/v0.1.0/apps/app/README.md) keeps the encryption key alongside the protected data.

### cl-marmot

[cl-marmot](https://github.com/modus-lisp/cl-marmot/blob/5dd9dea97ece82b0e4cc08f0c893397fbb333a5b/README.md) adds a Common Lisp implementation of MLS group chat over Nostr. October 9 code adds competing-commit convergence and encrypted Blossom attachments, with author-reported interoperability tests against MDK’s wn command-line client. The implementation is unaudited, and account keys and message logs lack encryption at rest. Timed convergence windows, replay beyond the rollback horizon and disbanding remain unimplemented; the inspected harness uses disposable local relays.

### nalgorithm Android

[nalgorithm's Android release](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.0) builds a preference-ranked Nostr feed and a background audio digest that can be played offline. Users choose hosted, Lightning-priced inference or own-key inference requested from the phone; these are separate routes. Login supports Amber through remote signing. Follow-up releases [repair own-key ranking and follow-list discovery](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.1), then [preserve likes from working relays when another relay fails](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.2) and improve digest recovery. [Version 1.0.3](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.3) reorders model setup and reports missing connection-test inputs.

writer_model: direct-codex

GATE: PASS (source-owner content review; full publication receipts are separate)
