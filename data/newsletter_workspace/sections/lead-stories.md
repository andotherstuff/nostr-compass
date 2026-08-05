## Top Stories

### nostr-mill 1.6.0 puts signing consent and account recovery in the browser

[nostr-mill 1.6.0](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0) is an embeddable browser account picker and signer. It now asks for consent by event kind and shows decoded content and tags before signing, with time-limited grants and a permissions manager. Its optional Google onboarding stores a PIN-encrypted key in the user's Drive app-data folder, supports multiple identities, and can export a [NIP-49](/en/topics/nip-49/) (encrypted private-key format) `ncryptsec`.

The [experimental relay backup](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0) derives a strong recovery phrase with scrypt and HKDF, wraps the key as `ncryptsec`, verifies fetched events, and requires a relay quorum before recovery. [NIP-55](/en/topics/nip-55/) (Android signer intents) login now uses Amber's clipboard return path, and [NIP-46](/en/topics/nip-46/) (relay-mediated remote signing) connections are quiet by default. Branding controls and responsive permission screens round out the release without changing existing integrations unless an operator opts in.

### nostrord 2.5.0 gives relay groups stable, relay-specific identities

[nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) is a cross-platform client for relay-hosted communities. It now derives a [NIP-29](/en/topics/nip-29/) (relay-managed groups) identity from both group ID and host relay, scopes membership and admin badges the same way, accepts group `naddr` deep links, and synchronizes private-group threads across devices.

The [release](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) also adds a [NIP-56](/en/topics/nip-56/) (report events) moderation inbox, Amber login through NIP-55, rate-limit backoff for NIP-46 signer traffic, [NIP-84](/en/topics/nip-84/) (portable highlights) rendering, and media uploads through Blossom or [NIP-96](/en/topics/nip-96/) (HTTP file storage). Thread replies gain richer content and admin deletion, while desktop keychain and mobile keyboard fixes keep those protocol features usable.

### Primal Android 3.5.25 updates remote signing and follow-list filtering

[Primal Android 3.5.25](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.25) is a mobile Nostr client with feeds, search, and remote signing. It updates its remote signer for current protocol behavior, adds a follow mute list, opens search from Explore, repairs stalled relay connections automatically, rejects invalid follow-list entries, and refreshes fallback relay URLs. Feed prefetching, lower memory use, and a 100 MB cache ceiling reduce the cost of keeping those feeds current.

### Nostur 1.30.2 expands private replies and media in direct messages

[Nostur 1.30.2](https://github.com/nostur-com/nostur-ios-public/releases/tag/527) is an Apple-platform Nostr client. It always exposes the private-reply action, adds per-conversation DM media caches with limits and clearing controls, improves name and tag completion in posts and chats, shows referenced messages in live chat, and includes the room title in chat notifications. Feed pagination and nested-reply fixes address retrieval and conversation rendering regressions.

### Chama 5.7.0 adds arbiter records and cached trade recovery

[Chama 5.7.0](https://github.com/jesuspirate/chama/releases/tag/v5.7.0) coordinates peer trades and arbitration through signed Nostr event chains. It displays an arbiter's locked amount, bond tenure, and funding outpoint; records when a backup replaced an absent arbiter; and defines dormant kind `38136` fault attestations that require both principals' signatures. An explicit repair retries incomplete relay histories against the durable device cache and republishes recovered events, while failed publishes queue for the next connection. The release also prevents cross-device duplicate arbiter-premium payments by treating the author's kind `38113` event as the payment record.

### Auditable Voting 0.1.165 restores delegated ballot delivery

[Auditable Voting 0.1.165](https://github.com/tidley/auditable-voting/releases/tag/v0.1.165) conducts verifiable ballots while separating voter credentials from ballot contents. It restores delegated blind-ballot issuance through authenticated delegation delivery and control-DM backfill, keeps blind-credential direct messages on configured private relays, and updates the audit proxy to 0.1.52.

### Sandstr lets newcomers test-drive Nostr clients with mock data

[Sandstr](https://sandstr.app/) provides interactive browser simulations of Nostr clients so a newcomer can compare their interfaces before installing one or creating a keypair. The August 3 launch from [Swarmstr creator ptrio42](https://github.com/ptrio42/swarmstr.com) includes reference-verified reproductions of Damus, Amethyst, Primal, Snort, YakiHonne, Coracle, and Wisp, plus clearly labeled early previews of Gossip, Keychat, and Olas. Everything runs locally against mock data, so the simulations do not generate keys, connect to relays, or impersonate the projects they demonstrate. Each simulation links onward to the real client's website and source repository, making Sandstr an onboarding and interface-comparison tool rather than another Nostr client. It shows how feeds, profiles, threads, direct messages, search, zaps, and relay controls feel without asking a first-time user to make an identity or security decision up front.


### mineracks signer pairs a browser extension with a desktop bunker

[mineracks signer](https://github.com/mineracks/mineracks-signer) provides two signing surfaces from the same project. Its browser extension implements [NIP-07](/en/topics/nip-07/) so web applications can request signatures without receiving the private key, while the desktop application exposes a [NIP-46](/en/topics/nip-46/) remote signer for clients that communicate through relays.

The project's [desktop 0.1.0 release](https://github.com/mineracks/mineracks-signer/releases/tag/desktop-v0.1.0) stores key material using NIP-49 encrypted-key encoding. The same codebase therefore supports local browser signing and relay-mediated desktop signing without exposing an unencrypted key to either client.

GATE: PASS
