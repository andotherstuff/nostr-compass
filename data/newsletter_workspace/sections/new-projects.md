## New Projects

### cvm-registry

[cvm-registry caches ContextVM service discovery](https://gitworkshop.dev/npub1nng5mxkdh2mu593twukfr7j3fk5wxfy0v8ujf0e5g8nwwtzlphhqksqpew/relay.ngit.dev/cvm-registry), using a curator allowlist and explicit fresh or expired catalog states to help users assess service listings. This static discovery dashboard makes catalog age visible, but its restaurant demonstration does not invoke services, make payments or settle transactions.

### Nostr Workshop

[Nostr Workshop's phone milestone](https://npub1nhf36h08krl0ts8r9amkwq5eq9mjhq82kz7dxcfza2hmlkqdhn3qt2t4q6.nsite.lol/) provides phone-oriented learning tasks, a signer bridge and encrypted key backups, with published results updating task progress. The browser signer holds the unlocked private key in plaintext per-tab sessionStorage until Lock; lasting use calls for transferring the encrypted backup to a dedicated signer. The newer source milestone is not attested to the listed APK.

### Nostella

[Nostella's experimental relay mesh authenticates forwarded requests](https://relay.ngit.dev/npub1600yr4qg5vcfp7svf6ysj0008tn7aphnu0gjs6lw5hjn74n0laasjx889v/nostella.git) and gives them stable identities to stop recursive amplification. Bounded forwarding to ordinary relays preserves filters and limits. Remote results arrive after the local end-of-stored-events signal, so clients that close their subscription at that signal miss those results.

### nope-mcp

[nope-mcp adds connector metadata and default open-license filtering](https://gitworkshop.dev/npub1r30l8j4vmppvq8w23umcyvd3vct4zmfpfkn4c7h2h057rmlfcrmq9xt9ma/relay.ngit.dev/amb-mcp) to educational-resource search across Nostr relays, exposing it through a public MCP interface without signing or mutation tools. Resources missing license tags are excluded by default.

### Vitals

[Vitals implements owner-authorized monitoring sessions](https://npub1zzndrnyy0cf6n4m3y5flcndavp08p05cesmacqylq6r6ca8pldhshda6w9.nsite.lol/), with a Linux daemon sending ephemeral machine reports encrypted using [NIP-44, Nostr's encrypted-message format](/en/topics/nip-44/). Five-minute keepalives extend a seven-minute session timeout. Closing the browser sends no signed stop, leaving monitoring to expire by timeout; the daemon is a prototype.

### grasp-go-proxy

[grasp-go-proxy exposes Nostr repository discovery to Go tooling](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/grasp-go-proxy.git), resolving npub, naddr and [NIP-05 human-readable identifiers](/en/topics/nip-05/) for [NIP-34 Git repository announcements](/en/topics/nip-34/) into go-import metadata pointing at existing Git hosts.


### Keythra

[Keythra adds a Mac-mediated remote signer](https://github.com/gmkbenjamin/keythra/commit/155eec9bc635cc1f2cbc37302d461e45caaa49ab) using [NIP-46, Nostr's remote-signing protocol](/en/topics/nip-46/), forwarding authorized applications' requests to an iPhone or local authenticator. Each signing, encryption or decryption operation requests user verification, with event IDs derived from approved fields. This remains a prototype source milestone: the Mac bridge must stay running, Nostr keys remain in software storage.

writer_model: actual=openai-codex/gpt-6.1-sol, receipt=/opt/data/task-artifacts/compass-direct-2026-10-07/writer-new_projects/receipt.json; final root edits verified in assembled draft 4f46a95e8d1bad2c63d2e7b67b35c387bded0c07ac10b97c6ca12298922f354b

GATE: PENDING REVIEW
