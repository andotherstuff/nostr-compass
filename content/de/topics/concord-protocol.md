---
title: "Concord-Protokoll"
date: 2026-07-15
translationOf: /en/topics/concord-protocol.md
translationDate: 2026-07-15
draft: false
categories:
  - Protocol
  - Messaging
---

Concord ist ein offenes, MIT-lizenziertes Protokoll für Ende-zu-Ende-verschlüsselte Communities und Kanäle auf Nostr, definiert durch die [CORD-01- bis CORD-07-Spezifikationen](https://github.com/concord-protocol/concord). [Vector](https://github.com/VectorPrivacy/Vector) hat es ab v0.4.0 als Standard-Transport für seine Group-Chats-Funktion übernommen und nennt es in den eigenen Release Notes „our custom messaging protocol", doch die Spezifikation selbst wird getrennt von Vector veröffentlicht und hat bereits unabhängige Implementierungen.

## Funktionsweise

Concord zerlegt das, was ein Discord-artiger Community-Server normalerweise tut, in Teile, die niemandem vertrauen müssen: Relays speichern ausschließlich verschlüsselte Blobs, die an rotierende Labels adressiert sind; den Schlüssel eines Raums zu besitzen macht jemanden zum Mitglied; und die Autorität über Rollen, Kicks und Bans ist ein signiertes Roster, das in der Identität des Eigentümers verwurzelt ist und das jeder Client lokal verifiziert, anstatt einem Server zu vertrauen. Jedes dauerhafte Event nutzt denselben dreischichtigen Umschlag: einen kind-1059-Wrap, signiert mit dem abgeleiteten Stream-Key der Ebene, der einen Seal enthält, signiert mit dem echten Schlüssel des Autors, der wiederum einen unsignierten Rumor enthält, der das funktionale Event trägt. Ein Chat-Nachrichten-Rumor ist ein einfaches kind-9-Event:

```json
{
  "kind": 9,
  "pubkey": "<author>",
  "content": "Hey chat!",
  "tags": [
    ["channel", "<channel_id>"],
    ["epoch", "0"]
  ]
}
```

Control-, Chat- und Guestbook-Verkehr erhalten jeweils ihre eigene [NIP-59](/de/topics/nip-59/) Gift-Wrapped-Ebene, sodass ein Relay, das alle drei hält, eine Control-Nachricht nicht von einer Chat-Nachricht oder einem Gästebuch-Eintrag unterscheiden kann, ohne den Raumschlüssel zu besitzen. Die Spezifikation ist in sieben CORD-Dokumente aufgeteilt: Private Streams (01), Communities und Mitgliedschaft (02), Kanäle (03), Rollen (04), Einladungen (05), Rekeying und Re-Founding zum Ausschluss entfernter Mitglieder (06) sowie Audio/Video über einen Blind-Token-Broker (07). Die Mitgliedschaft selbst hat keine serverseitige Liste: Wer die Ebene entschlüsseln kann, ist Mitglied, und jemanden wirklich zu entfernen bedeutet, die Community auf einen neuen Schlüssel-Epoch zu rollen und diesen nur den Verbliebenen zu übergeben, anstatt eine Zeile aus einer Tabelle zu löschen.

## Unterschiede zu Marmot

Concord und [Marmot](/de/topics/marmot/) lösen verschlüsseltes Gruppen-Messaging auf Nostr mit unterschiedlicher Kryptographie für unterschiedliche Gruppenformen, und der Vergleich des Concord-Projekts ist explizit bezüglich der Aufteilung: Marmot legt [MLS](/de/topics/mls/) über Nostr für Forward Secrecy und Post-Compromise Security, unter Verwendung von Pro-Gerät-Key-Packages und geordneten Commits, die die gesamte Gruppe im Gleichschritt voranbringen. Das bietet starke Garantien, zu Kosten, die mit Mitgliedschaftsänderungen skalieren, gut geeignet für kleine, hochsensible Gruppen, in denen Beitritte und Abgänge selten sind. Concord gibt stattdessen jedem Mitglied denselben Raumschlüssel und führt ein Rekeying des gesamten Raums bei Entfernung durch, anstatt pro Commit zu ratcheten, und tauscht damit einige der kryptographischen Garantien von MLS gegen ein Modell, das günstig bleibt, wenn eine Community auf Hunderte oder Tausende von gelegentlichen Mitgliedern mit hoher Fluktuation wächst, genau die Form, die Discord-artige Communities tatsächlich annehmen.

## Warum Vector gewechselt hat

Vectors eigene [v0.4.0 Release Notes](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) beschreiben Concord nur als „our custom messaging protocol" für Group Chats, ohne die Begründung direkt zu nennen. Die Passung zur veröffentlichten Begründung von Concord ist dennoch klar: Group Chats in einem Client wie Vector sind genau der Fall mit großer, offener, häufig wechselnder Mitgliedschaft, in dem der Pro-Gerät-MLS-State von Marmot zum teureren Weg wird, und Concords asynchrones, jederzeit beitretbares Design ist genau für diesen Fall gebaut. [Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) hat Marmot für Group Chats zugunsten von Concord abgelöst, und bestehende Marmot-Gruppenverläufe wurden beim Wechsel nicht übernommen. [v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1) lieferte vier Tage später „Concord v2" mit Datenschutz- und Stabilitätsverbesserungen. Innerhalb derselben Woche [mergte Amethyst seine eigene Clean-Room-, drahtkompatible Concord-Implementierung](https://github.com/vitorpamplona/amethyst/pull/3566), und Soapbox' Discord-artiger Client [Armada](https://gitlab.com/soapbox-pub/armada) baut sein Communities-Feature bereits auf derselben Spezifikation als Referenzimplementierung auf. Drei unabhängige Clients, die innerhalb von Tagen auf eine offene Spezifikation konvergieren, sind ein schneller Weg zu echter Client-übergreifender Interoperabilität, lohnenswert zu verfolgen im Vergleich dazu, wie viel vom Rest der Nostr-Gruppen-Chat-Clients auf Marmot bleibt.

## Implementierungen

- [Vector](https://github.com/VectorPrivacy/Vector) - Single-Binary, datenschutzorientierter Nostr-Messenger; erster ausgelieferter Concord-Client, in v0.4.0
- [Armada](https://gitlab.com/soapbox-pub/armada) (Soapbox) - Discord-artiger Community-Client; Referenzimplementierung, Backend im separaten `armada-relay`-Repository
- [Amethyst](https://github.com/vitorpamplona/amethyst) - funktionsreicher Android- und Multiplattform-Nostr-Client; Clean-Room-Reimplementierung, drahtkompatibel mit Armada ([PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566))

---

**Primärquellen:**
- [Concord-Protokoll-Spezifikationen (CORD-01 bis CORD-07)](https://github.com/concord-protocol/concord)
- [Vector v0.4.0 Release Notes](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0)
- [Vector v0.4.1 Release Notes](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1)
- [Amethyst PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566)

**Erwähnt in:**
- [Newsletter #31: Vector v0.4.0 moves Group Chats from Marmot to Concord, and Amethyst ships its own Concord client days later](/de/newsletters/2026-07-15-newsletter/#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later)
- [Newsletter #31: Amethyst ships a clean-room Concord implementation for end-to-end encrypted communities](/de/newsletters/2026-07-15-newsletter/#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities)

**Siehe auch:**
- [Marmot-Protokoll](/de/topics/marmot/)
- [MLS (Message Layer Security)](/de/topics/mls/)
- [NIP-46: Nostr Connect](/de/topics/nip-46/)
