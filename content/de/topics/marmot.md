---
title: "Marmot Protocol"
date: 2025-12-17
translationOf: /en/topics/marmot.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot ist ein Protokoll für Ende-zu-Ende-verschlüsselte Gruppenkommunikation auf Nostr. Es kombiniert Nostr-Identitäten und das Relay-Netzwerk mit MLS für Gruppen-Schlüsselverwaltung, Forward Secrecy und Post-Compromise Security.

## Funktionsweise

Marmot nutzt Nostr für Identität, Relay-Transport und Event-Verteilung und legt darüber MLS für Änderungen an der Gruppenmitgliedschaft und für die Nachrichtenverschlüsselung. Anders als [NIP-17](/de/topics/nip-17/), das sich auf One-to-One-Messaging konzentriert, ist Marmot für Gruppen gebaut, in denen Mitglieder beitreten, austreten oder ihre Schlüssel im Lauf der Zeit rotieren.

## Warum das wichtig ist

MLS gibt Marmot Eigenschaften, die Nostr-DM-Schemata allein nicht bieten: Evolution des Gruppenstatus, Semantik für Mitgliederentfernung und Erholung nach einer Kompromittierung durch spätere Key Updates.

Diese Arbeitsteilung ist der entscheidende Punkt. Nostr löst Identität und Transport in einem offenen Netzwerk. MLS löst authentifizierte Gruppen-Schlüsselvereinbarung. Marmot ist die Klebeschicht dazwischen.

## Implementierungsstand

Das Protokoll bleibt experimentell, hat inzwischen aber mehrere Implementierungen und echten App-Einsatz. [MDK](https://github.com/marmot-protocol/mdk) ist der wichtigste Rust-Referenz-Stack, [marmot-ts](https://github.com/marmot-protocol/marmot-ts) bringt das Modell nach TypeScript, und Anwendungen wie [White Noise](https://github.com/marmot-protocol/whitenoise), [Amethyst](https://github.com/vitorpamplona/amethyst), Pika und Vector haben Marmot-kompatible Komponenten verwendet.

Aktuelle Arbeit konzentriert sich auf Härtung und Interop. Audit-getriebene Fixes wurden Anfang 2026 ausgeliefert, und MIP-03 führte deterministische Commit-Auflösung ein, damit Clients konvergieren können, wenn konkurrierende Änderungen am Gruppenstatus über Relays gegeneinander laufen.

Im April 2026 brachte Amethyst sein eingebettetes MDK in Einklang mit den Wire-Formaten von MIP-01 und MIP-05: [PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) fügte VarInt-Encoding für TLS-artige Längenpräfixe und Roundtrip-Validierung gegen MDK-Testvektoren hinzu, [PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) fügte MIP-00 KeyPackage Relay List-Unterstützung hinzu, und [PR #2436](https://github.com/vitorpamplona/amethyst/pull/2436) schloss verbleibende Lücken bei Admin-Gates und Media Handling, die Cross-Client-Tests gegen White Noise aufgedeckt hatten. [PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466) korrigierte MLS-Commit-Framing, sodass verschlüsselte Welcome-Bytes mit dem Output von mdk-core übereinstimmen, und [PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471) behob einen Outer-Layer-Decryption-Bug, der zu State-Divergenz zwischen Co-Admins führte. Das Follow-up [PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493) fügt umfassende Validierung der MLS-Commit-Kryptographie hinzu, und [PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) liefert `amy`, eine CLI für Marmot- und MLS-Gruppenoperationen auf Basis der Amethyst-Implementierung.

MDK lieferte [PR #261](https://github.com/marmot-protocol/mdk/pull/261), um `RequiredCapabilities` einer Gruppe als LCD der Invitee-Fähigkeiten zu berechnen, was Mixed-Version-Invites zwischen Amethyst und White Noise freischaltet, [PR #262](https://github.com/marmot-protocol/mdk/pull/262), um Invitee-KeyPackages zu parsen, bevor der Signer des Erstellers persistiert wird, [PR #264](https://github.com/marmot-protocol/mdk/pull/264), um das SelfUpdate-Wire-Format implementationsübergreifend zu vereinheitlichen, und [PR #265](https://github.com/marmot-protocol/mdk/pull/265), um einen `group_required_proposals`-Accessor bereitzustellen.

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) befindet sich mitten in einem mehrphasigen Refactor von globalen Singletons zu account-spezifischen `AccountSession`-Views: [PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743) schuf das Grundgerüst für `AccountSession` und `AccountManager`, und Folgephasen migrierten Relay-Handles, Drafts und Settings, Message-Ops, Group Read und Write, Membership, Push Notifications, KeyPackage-Reads, Group Creation und mit [PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770) nun auch session-scoped Event-Dispatch. [marmot-ts PR #68](https://github.com/marmot-protocol/marmot-ts/pull/68) migriert den TypeScript-Client auf addressable kind-`30443`-KeyPackages.

---

**Primärquellen:**
- [Marmot Protocol Repository](https://github.com/marmot-protocol/marmot)
- [MLS Protocol](https://messaginglayersecurity.rocks/)
- [Marmot Development Kit (MDK)](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)
- [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)
- [White Noise client](https://github.com/marmot-protocol/whitenoise)
- [Amethyst PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) - MIP-01/MIP-05 wire format alignment
- [Amethyst PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) - MIP-00 KeyPackage Relay List
- [Amethyst PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) - Amy CLI

**Erwähnt in:**
- [Newsletter #1: News](/de/newsletters/2025-12-17-newsletter/)
- [Newsletter #1: Releases](/de/newsletters/2025-12-17-newsletter/)
- [Newsletter #4](/de/newsletters/2026-01-07-newsletter/)
- [Newsletter #7](/de/newsletters/2026-01-28-newsletter/)
- [Newsletter #12](/de/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: Amethyst MIP compliance](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: MDK interop work](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: whitenoise-rs session refactor](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [MLS (Message Layer Security)](/de/topics/mls/)
- [MIP-05: Privacy-Preserving Push Notifications](/de/topics/mip-05/)
- [NIP-17: Private Direct Messages](/de/topics/nip-17/)
- [NIP-59: Gift Wrap](/de/topics/nip-59/)
