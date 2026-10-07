## In Development

### Dart NDK

Dart NDK, a Dart and Flutter Nostr toolkit, adds [authentication consent controls](https://github.com/relaystr/ndk/pull/862) for relays and Blossom servers. Without an explicit policy or consent handler, relay operations stop authenticating automatically as the logged account and default Blossom writes use throwaway keys. Signed events still identify their authors. Its [NIP-46 relay switching](https://github.com/relaystr/ndk/pull/851) follows a signer's replacement relay list; applications must persist the updated connection. These are merged changes, with no tagged release established.

### MintRadar

MintRadar, a Cashu mint directory with signed Nostr reviews, [restricts shared-link relay hints](https://github.com/hroomnik007/MintRadar/commit/be94d29852963fca47570d974b997e4ab57e1915) to three known relays plus its defaults, and caps account-list connections at ten public secure-WebSocket hosts. Its new [server profile index](https://github.com/hroomnik007/MintRadar/commit/f6e5e07d354f2e0ba380e709119c33b91d810890) supplies reviewer names when browser lookup finds none; internet identifiers remain labeled as claims until separately verified. These are main-branch changes, with deployment unverified.

### LNbits

LNbits, a Lightning service with Nostr notifications, [lets WASM extensions request user notifications](https://github.com/lnbits/lnbits/pull/4222) under an explicit permission. The host selects the current user or invocation wallet owner and their saved Nostr, email or Telegram settings; extensions cannot supply an arbitrary recipient. This is merged development work, and a queued response does not guarantee delivery.

### Zeus

Zeus, a Lightning wallet, [repairs LDK routing-fee reporting](https://github.com/ZeusLN/zeus/pull/4353) used by [Nostr Wallet Connect](/en/topics/nip-47/), allowing responses and connection spending to include the reported fee. Budget checks still cover the invoice amount before settlement and debit rounded fees afterward; the service uses a separate 1,000-satoshi routing-fee cap. This is merged source work, with no release established in the window.

### Pollerama

[Pollerama](https://pollerama.fun), a Nostr polls and feeds client, [repairs encrypted-message delivery](https://github.com/formstr-hq/nostr-polls/pull/249) by waiting for relay-authentication acknowledgement before replaying subscriptions on relay.formstr.app. Its local-relay library discards signing results from replaced sockets and directs outgoing gift-wrapped messages to the recipient's declared inbox relays.

### Nostur

Nostur, an iOS Nostr client, [adds kind 16 generic repost support](https://github.com/nostur-com/nostur-ios-public/commit/74e5fbe12ad983af0dad1c37257a726f68df35d6) across feeds, rendering and event references, so reposts of other event types can resolve their original content. A [saved-repost repair](https://github.com/nostur-com/nostur-ios-public/commit/f286a8c8c01ccdf2febe2d566f7bce443ae26daa) restores missing target links when those reposts are reopened, validating embedded events before using them. Existing repost counts are preserved.

### Gittr

Gittr, a Nostr-based Git platform, [repairs Settings deletion requests that could fail to reach Amber](https://github.com/arbadacarbaYK/gittr/commit/92a25de1ec8bb58f945711c66e5f1ed54f2df82f). Subscriptions measure their wait from the current signer-connection pause, and a saved signer identity can proceed to signing when the initial connection warmup finds no open socket. This repairs signer contact; it does not establish that deletion has completed across relays.

### NosTube

NosTube, a Nostr video client, [adds a separate instance build](https://github.com/flox1an/nostube/commit/296ef99bed50771ea3d2a11c08343575608d222b) that loads server configuration before starting the app and limits its video catalog to configured creators and sources. [Signer and wallet connections](https://github.com/flox1an/nostube/commit/1b02423abdfc4f26b1b74081e2ab396310ac1ba6) retain their own relay access. [Admin routes](https://github.com/flox1an/nostube/commit/047ec6ad9af2ef487a3bce2f9510f8a0d35da2a1) are served by nostube-server. Search remains disabled in this initial instance variant.

### eHagaki

eHagaki, a Nostr client, [stores content-warning bodies separately](https://github.com/Lokuyow/ehagaki/pull/284) in verified kind 36 payloads before publishing the original event structure. [Only compatible clients](https://github.com/Lokuyow/ehagaki/pull/294) retrieve and display those bodies; the warning does not encrypt them. [Local history search](https://github.com/Lokuyow/ehagaki/pull/290) now streams its first 50 matches while scanning continues, then reports the exact total.

### Nostr Components

Nostr Components, a web-component toolkit, [adds signed profile and relay records and URL-activity APIs](https://github.com/saiy2k/nostr-components/pull/164). Zap capability stays unknown until checked, and ingestion stores an event only after a sweep relay returns it. These changes are merged development work; deployment remains pending.

### Holoboard

Holoboard, a paid Nostr note-promotion board, [preserves unfinished promotion payments](https://github.com/ptrio42/holoboard.space/commit/55b26ff3f06846a8ca15bac9ad28ff0c56157650) when users return to editing or switch notes. Earlier invoices remain available for explicit resume, and late wallet replies update their own payment record. Unconfirmed payments retain a warning that they may already have succeeded. Issued invoices remain payable; returning to the editor neither cancels them nor refunds a payment. Failed browser storage leaves a visible notice.

### Milk Market

Milk Market, a Nostr marketplace, adds [mobile seller shipping](https://github.com/shopstr-eng/self-sown/pull/33), [return labels and optional activity alerts](https://github.com/shopstr-eng/self-sown/pull/34), and [native catalog editing](https://github.com/shopstr-eng/self-sown/pull/36). Return labels preserve outbound tracking and order status; uncertain label purchases keep their duplicate-prevention records. Catalog editors reject stale or wrong-owner edits and protect sold stock from duplicate retries. Server push remains disabled unless explicitly configured.

### NYM

NYM, a Nostr chat client, changes [notification handling](https://github.com/Spl0itable/NYM/commit/c2488e4052c646b1d0a3bbc944b23518ad355dec) so service-worker notification clicks reopen the relevant private, group or location conversation, with page notifications as a fallback. Unread in-app toasts held while a sheet was open remain eligible after their ordinary timeout. System notifications still require permission and browser support.

[Client AI consent and account-deletion changes](https://github.com/Spl0itable/NYM/commit/5c36b87cc05e850ba9ffb2b20d7416d8f7cf1aa2) add prompts before bot processing and translation; bot consent can also enable translation. Requests may share conversation or channel context, including other people’s recent messages and approximate location, with the service and selected model providers. Deletion attempts cover usable saved identities and local wiping, but public relay copies, inaccessible identities and external backups can remain, and some server-cleanup errors are not surfaced. Closed-app ringing is opt-in for one identity per phone.

### Nostr Inspect

Nostr Inspect, an event-inspection tool formerly called Nostr Events Monitor, adds [browser-side signature and content-ID checks](https://github.com/Catrya/nostr-inspect/pull/26), [address lookup and relay-copy status](https://github.com/Catrya/nostr-inspect/pull/28), plus [exact-event or latest-address sharing](https://github.com/Catrya/nostr-inspect/pull/30). Latest means the newest valid copy observed from queried relays, which may withhold other copies. [Shared search filters](https://github.com/Catrya/nostr-inspect/pull/31) run ordinary searches on opening; streaming needs a user start. The [rename](https://github.com/Catrya/nostr-inspect/pull/32) resets existing browser settings and repeats the walkthrough once. These changes are merged source work.

### Bark

Bark, a browser extension using [NIP-46](/en/topics/nip-46/) remote signing, [serializes signer handshakes](https://github.com/forgesworn/bark/pull/47) so concurrent requests wait for the existing attempt. Each handshake keeps its own signer; superseded work cannot clear a replacement connection or return its signer. Failed candidates close, stale relay-health results are ignored, and the current signer can still request approval. This is merged recovery work; live Heartwood hardware-signer acceptance remains unverified.

### NoorNote

NoorNote, a Nostr client, adds [website-manifest cards](https://github.com/77elements/noornote/commit/f516a76eea45995452c96d0904b029218c2937ea) with normal note interactions, a Websites profile tab and named-site address routing. [Unsupported-event cards](https://github.com/77elements/noornote/commit/e4cdb976503712bbec452a67de1fff29eaf1281e) gain navigation and copy/raw-event menus. Website support is display-side development: it neither publishes sites nor adds manifests to ordinary feed filters. Gateway and source links open on user clicks; the client does not automatically fetch or validate website contents.

### Wisp

Wisp, a Nostr client, adds [Android signature verification before delivery and deduplication](https://github.com/barrydeen/wisp/pull/665), preventing invalid events with matching IDs from hiding valid posts. Verification uses bounded workers and fails closed; authentication also fences stale identities. The write queue remains unbounded.

### Meiso

Meiso, a task app, adds [automatic synchronization safeguards in 1.4.1](https://github.com/higedamc/meiso/pull/180): failed reads no longer become empty lists, publishing requires a successful session fetch, and large list shrinkage needs confirmation. Failed sends remain pending synchronization. Manual sync bypasses these guards, and local tasks absent remotely for 24 hours can still be deleted without causal deletion tracking.

### ZapTracker

ZapTracker, a publishing dashboard, adds source-level [RSS and Atom publishing](https://github.com/pratik227/zap_dashboard/pull/136) as articles or short posts, plus [media and self-thread export/import](https://github.com/pratik227/zap_dashboard/pull/137). Automatic publishing requires the app to remain open with a signer and handles at most three new items per feed; backlog publishing is manual. Deduplication is account-local, so clearing history can permit repeats.

### Formstr Drive

Formstr Drive, an encrypted file-sharing app, moves files into [single encrypted Blossom blobs](https://github.com/formstr-hq/formstr-drive/pull/69) and adds [range previews and key-separated sharing links](https://github.com/formstr-hq/formstr-drive/pull/72). Partial previews require server range support. Folder-share creation remains unwired, and old sharing links are intentionally incompatible, although old blobs remain readable.

### Safebox Acorn

Safebox Acorn, a wallet component, adds a [validated private-message reader and recipient inbox routing](https://github.com/trbouma/safebox-acorn/commit/2b20845816615a71d6577aa130a0550972669dc7) using [NIP-17](/en/topics/nip-17/), Nostr's private messaging protocol. Landed code checks envelope signatures and author/recipient agreement, separates payment envelopes from ordinary chat, and reports absent routes explicitly. Ambiguous sends require checking before resending. Retrieval stops at 100 outer events, including excluded payment envelopes.

### Minibits

Minibits, an ecash wallet, adds [persistent NIP-17 conversations for text, ecash and payment requests](https://github.com/minibits-cash/minibits_wallet/commit/ca896f364ba7a6a51f387af94d2094648133cbf5), with unread indicators and unknown-contact requests. Separate sender copies and message deduplication prevent outgoing funds from being counted as incoming. Conversations display at most 500 messages without paging; relay acceptance leaves delivery and reading unconfirmed.

### LaWallet

LaWallet, a wallet service, merges an [OAuth 2.1 MCP interface for balance, invoice and payment tools](https://github.com/lawalletio/lawallet-nwc/pull/327), with explicit permissions and daily connection budgets. A companion [listener-secret safeguard](https://github.com/lawalletio/lawallet-nwc/pull/326) restricts stored-secret fallback to the configured origin. Pending and unknown payments remain accounted for, but concurrent grants lack a global exactly-once guarantee, and fee reserves do not enforce a total fee cap.

### Zap Cooking

Zap Cooking, a recipe-sharing client, makes [Fresh the default feed](https://github.com/zapcooking/frontend/pull/785), with an isolated relay connection and public 14-day access. Deeper history and topic access request [NIP-42](/en/topics/nip-42/) relay authentication lazily, limiting unsolicited identity disclosure. Merged [comment interoperability changes](https://github.com/zapcooking/frontend/pull/767) preserve root and parent relationships when reading and replying. Relay policy controls access; reply counters still omit some comments.

Later main changes route [reactions, comments and zap-receipt requests](https://github.com/zapcooking/frontend/pull/791), plus [reposts and lists](https://github.com/zapcooking/frontend/pull/792), through authors' write relays, recipient read relays and the app list. Lists omit recipient fan-out; group events stay on Pantry. Routing failure can still fall back to the pool. Extension and remote-signer relay login gets one attempt per account, relay and page load; reconnects may remain logged out until reload. Pantry and local keys are exempt. Members also gain [topic-labeled day and month archives](https://github.com/zapcooking/frontend/pull/793), subject to relay access and paging limits.

### Kehto / Paja

Kehto's Paja transport, for [ContextVM remote tool calls over Nostr](/en/topics/contextvm/), adds [bounded oversized transfers and streaming progress](https://github.com/kehto/web/pull/265). Server identity and typed request tokens prevent chunks or progress from attaching to the wrong concurrent request; completed transfers require matching byte length and hash. Idle probes monitor streams, while the final response or deadline determines completion.

### Notedeck

Notedeck, a desktop Nostr client, lets its Dave AI-agent conversations exceed individual note limits through [UTF-8-safe signed multipart messages and reassembly](https://github.com/damus-io/notedeck/commit/a3551845a504711641b95829bda36ae02a6a2789). Readers check authorship and part completeness before reconstructing messages. Older devices display separate parts; reconstruction requires every part locally.

### diVine

diVine, a video-sharing client, adds [author-checked comment deletion across pages, reconnects and live updates](https://github.com/divinevideo/divine-mobile/pull/9751) using [NIP-09](/en/topics/nip-09/), Nostr's deletion-request protocol. Merged code waits for a relay acknowledgement before reporting deletion success and caches the user's deletion requests for offline reads. A two-second lookup timeout leaves comments visible, and live filtering requires a comment-kind tag.

### Conduit

Conduit's public Nostr reader/writer adds [verification against detached canonical signed fields](https://github.com/Conduit-BTC/conduit-mono/pull/606), separating relay provenance from mutable events. [Relay settings](https://github.com/Conduit-BTC/conduit-mono/pull/638) permit another explicit edit and review while an earlier signed update awaits confirmation; exact retry preserves unsigned drafts, with counts behind “Confirmation details.” Signing and publication still serialize, with independent relay-list and inbox checkpoints. Observed provenance is not exhaustive relay coverage; external-signer behavior and public-relay convergence remain unverified.

### Buzz

Buzz, a community relay, adds [community-scoped federation enforcement](https://github.com/block/buzz/pull/8028): the request host selects the community, which must authorize the issuer before signing-key retrieval, and the assertion audience must match that community. Merged [shadow-mode evaluation](https://github.com/block/buzz/pull/8034) records would-deny outcomes across HTTP, WebSocket and audio without denying admission or closing observed sessions. Enforcement requires operator-supplied community configuration; shadow metrics exclude some earlier refusals.

Merged work keeps [agent-to-agent replies inside threads](https://github.com/block/buzz/pull/8124) and [retries uncertain sibling-agent authorization lookups](https://github.com/block/buzz/pull/7216) while denying the current event. An optional [read-state/sidebar API](https://github.com/block/buzz/pull/7906) remains disabled by default: database operators can read its plaintext state, and it does not synchronize with legacy read-state events. [Deletion cleanup](https://github.com/block/buzz/pull/8128) purges retention-free read-state and heartbeat rows with their mentions; ordinary deleted history remains soft-deleted.

writer_model: actual=openai-codex/gpt-6.1-sol, receipt=/opt/data/task-artifacts/compass-direct-2026-10-07/writer-in_development/receipt.json; final root edits verified in assembled draft 4f46a95e8d1bad2c63d2e7b67b35c387bded0c07ac10b97c6ca12298922f354b

GATE: PENDING REVIEW
