---
title: "Marmot-Protokoll"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot ist ein Protokoll für Ende-zu-Ende-verschlüsselte Gruppennachrichten auf Nostr. Es kombiniert die Identität und das Relay-Netzwerk von Nostr mit MLS für Gruppen-Schlüsselmanagement, Forward Secrecy und Post-Compromise-Sicherheit.

## Wie es funktioniert

Marmot verwendet Nostr für Identität, Relay-Transport und Event-Verteilung und schichtet dann MLS für Gruppen-Mitgliedschaftsänderungen und Nachrichtenverschlüsselung darüber. Anders als [NIP-17](/de/topics/nip-17/), das sich auf Eins-zu-Eins-Nachrichten konzentriert, ist Marmot für Gruppen gebaut, bei denen Mitglieder im Laufe der Zeit beitreten, austreten oder Schlüssel rotieren.

## Warum es wichtig ist

MLS gibt Marmot Eigenschaften, die Nostrs Direktnachrichten-Schemata allein nicht bieten: Gruppenstatusentwicklung, Semantik zur Mitgliederentfernung und Wiederherstellung nach Kompromittierung durch spätere Schlüsselaktualisierungen.

Diese Arbeitsteilung ist die nützliche Erkenntnis. Nostr löst Identität und Transport in einem offenen Netzwerk. MLS löst authentifizierte Gruppen-Schlüsselvereinbarung. Marmot ist die Verbindungsschicht dazwischen.

## Implementierungsstatus

Das Protokoll bleibt experimentell, hat aber nun mehrere Implementierungen und aktive Anwendungsnutzung. MDK ist der wichtigste Rust-Referenz-Stack, `marmot-ts` bringt das Modell zu TypeScript, und Anwendungen wie White Noise, Pika und Vector verwenden Marmot-kompatible Komponenten.

Aktuelle Arbeit konzentriert sich auf Härtung und Interoperabilität. Audit-getriebene Fixes landeten Anfang 2026, und MIP-03 führte deterministische Commit-Auflösung ein, sodass Clients konvergieren können, wenn konkurrierende Gruppenstatusänderungen über Relays aufeinandertreffen.

---

**Primärquellen:**
- [Marmot Protocol Repository](https://github.com/marmot-protocol/marmot)
- [NIP-104: MLS-based Encrypted Group Chats](/de/topics/nip-104/)
- [Marmot Development Kit](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)

**Erwähnt in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: Releases](/en/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #4](/en/newsletters/2026-01-07-newsletter/)
- [Newsletter #7](/en/newsletters/2026-01-28-newsletter/)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**Siehe auch:**
- [MLS (Message Layer Security)](/de/topics/mls/)
- [MIP-05: Privacy-Preserving Push Notifications](/de/topics/mip-05/)
- [NIP-17: Private Direct Messages](/de/topics/nip-17/)
- [NIP-59: Gift Wrap](/de/topics/nip-59/)
