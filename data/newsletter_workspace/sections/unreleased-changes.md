## In Development

### nostrord keeps group muting synchronized between devices

[nostrord](https://github.com/nostrord/nostrord) is a cross-platform client for relay-managed communities. [PR #250](https://github.com/nostrord/nostrord/pull/250) stores each account's per-group mute choices in a self-encrypted [NIP-78](/en/topics/nip-78/) (application-specific data) kind `30078` event, so a setting made on one device can follow the user to another without revealing the group list to the relay. The replaceable record uses newest-event ordering, listens for live changes, and rolls the interface back when signing or publication fails instead of leaving local state out of sync. Muted groups also stop contributing visible unread totals while retaining their unread position for the next visit.

### Amethyst completes Concord's invite lifecycle

[Amethyst](https://github.com/vitorpamplona/amethyst) is an Android Nostr client whose encrypted-community support implements the Concord protocol. [PR #3888](https://github.com/vitorpamplona/amethyst/pull/3888) lets invite links survive a community refounding by reissuing their bundles at the same addressable coordinates, while a ban check prevents a removed member from using that recovery path. It also implements the encrypted CORD-05 invite list on both the app and `amy` command-line client, adds per-link revocation tombstones, and requires relay confirmation before deleting the only stored signing key that can retire a link. The same work gives `amy` the control-key delivery, refounding, rekeying, and stranded-member recovery paths needed to follow later community epochs.

### Buzz carries each community's appearance across desktop and mobile

[Buzz](https://github.com/block/buzz) is a Nostr-based community workspace with desktop and mobile clients. Merged desktop [PR #3653](https://github.com/block/buzz/pull/3653) and mobile [PR #3767](https://github.com/block/buzz/pull/3767) store each community's theme, accent, and system-mode choice as an encrypted NIP-78 record on that community's relay. Both clients share the same versioned payload and keep identity-scoped local caches, so changing communities or accounts cannot apply the wrong appearance while the relay is unavailable. Replacement ordering, guarded writes, and resubscription after a closed connection let the two clients converge again after reconnecting.

[Buzz Desktop 0.5.10](https://github.com/block/buzz/releases/tag/desktop-v0.5.10) followed before the issue cutoff with a performance and reliability pass. It removes regressions introduced after 0.5.9, accelerates channel loading, bounds initial timeline retention, coalesces read-state persistence, preserves fresh channel timelines, and stops the relay ingest worker from crashing on reactions to project events. It also adds sending a thread message to a channel and narrows desktop search to the intended scope.

GATE: PASS (final-delta claims, continuity, 73/73 live links, prose/style, topic-backlink, and production-build gates passed at 2026-08-12T15:45Z)
