## In Development

### Nenya marketplace library

[Nenya](https://github.com/Erya-Labs/Nenya) is a new library for a non-custodial Nostr marketplace focused on commissioned digital media with Bitcoin settlement. The repository is pre-release, so its event and settlement interfaces may still change.

Client developers import the [Nenya library](https://github.com/Erya-Labs/Nenya) into Nostr applications to expose compatible listings and transactions. Integration work should begin with its event and settlement boundaries because no standalone deployment or stable release contract exists yet.

### GitHub-to-Nostr CI bridging

[gh-ngit-ci-bridge](https://github.com/felixfelix-bot/gh-ngit-ci-bridge) is an early bridge that watches GitHub commits associated with configured identities and turns them into signed Nostr build evidence for NIP-34 workflows. The repository is pre-release, and its integration contract may still change.

The [gh-ngit-ci-bridge repository](https://github.com/felixfelix-bot/gh-ngit-ci-bridge) connects conventional GitHub activity with Nostr-native CI coordination without changing the original forge workflow. Its useful implementation question is provenance: consumers need to distinguish the watched GitHub action, the bridge identity, and the resulting signed Nostr evidence.

### noscall encrypts voice attachments

[noscall’s encrypted voice-attachment commit](https://github.com/sanah9/noscall/commit/3f0b9ef7cf0fbc6e0dced58240c32bb84ed6fea4) adds a concrete privacy feature for voice communication. The source-verified change supports encrypted voice attachments, reducing the need to expose recorded media as plaintext when attaching it to a call or messaging flow.

### relayer restores notifier fan-out across processes

[relayer pull request #167](https://github.com/fiatjaf/relayer/pull/167) has merged a notifier fix for deployments where several relay processes share one database. The patch restores live fan-out across those processes, addressing the case where an event persisted successfully but connected clients on another process did not receive the corresponding live notification.

Taken with the shared-database work in [nostr-relay v0.0.266](https://github.com/mattn/nostr-relay/releases/tag/v0.0.266), the relayer fix gives multi-process operators a clear test target: publish through one process, subscribe through another, and confirm both persistence and immediate delivery. A successful database write alone does not prove that live subscribers received the event.

writer_model: preferred=gemini-3.1-pro, actual=openai-codex/gpt-5.6-sol, receipt=data/newsletter_workspace/writer_receipt_2026-09-16.json

GATE: PENDING REVIEW
