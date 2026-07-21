# Compass Link Queue

Rolling accumulator for project links/notes sent in the Marmot Compass chat
during the week, ahead of the Tuesday intake deadline. Append a new
`## <ISO 8601 UTC timestamp>` section per incoming chat message; keep each
message's content verbatim underneath (this preserves the natural
"project name + supporting links" structure IntakeAgent already expects from
a `/newsletter` prompt body).

Consumed automatically by the `compass-tuesday-intake` cron job as Stage 1
IntakeAgent input each Tuesday, then archived to
`link_queue_archive_<target-date>.md` and reset to empty so next week starts
clean. Do not delete this file; if it's missing the cron just treats the
queue as empty for that run.

---

## 2026-07-14T10:53:00Z

Bitcoin-Safe — latest release. Reference: enables label sync, signers chat,
and remote multisig PSBT signing via nostr (currently via NIP-17), plus
exploring ways to implement Marmot in the future. Available today via
Flathub.
- https://Bitcoin-Safe.org
- https://flathub.org/en-GB/apps/org.bitcoin_safe.BitcoinSafe

Other links for this edition:
- https://github.com/hedwig-corp/bitchat-to-sonar
- https://github.com/coracle-social/n8n-nodes-nostr
- https://git.iris.to/#/npub1xdhnr9mrv47kkrn95k6cwecearydeh8e895990n3acntwvmgk2dsdeeycm/iris-drive
- https://zapstore.dev/apps/naddr1qqxkz6fwv9kx76rpdvhxkctfqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcpzp9mlxmjnp880dztdrewcg5hzuuyay659k6mlc5ejfe9muhgcccknqvzqqqr7pvt80jjp
- https://github.com/sofia-gros/open-discord
- https://primal.net/e/nevent1qqsqttye0cuj22ex58slj657dandvjzn5vnywqp39f0u53h9rktu8zck9gc3e
- https://tidley.github.io/auditable-voting/?role=auditor&q=q_70201bbedaf5
- https://cypherpunk.today/nostrautica/docs/
