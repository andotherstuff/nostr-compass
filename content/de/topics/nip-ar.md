---
title: "Buzz NIP-AR: Kanal-Artefakte"
date: 2026-09-30
draft: false
categories:
  - Project Proposals
  - Collaboration
translationOf: /en/topics/nip-ar.md
translationDate: 2026-10-01
---

NIP-AR ist die **projektspezifische** Spezifikation von Buzz für Kanal-Artefakte. Die Bezeichnung bedeutet hier nicht, dass sie vom Repository `nostr-protocol/nips` oder von anderen relays übernommen wurde.

## Artefaktmodell

Ein Artefakt ist ein bearbeitbarer Datensatz mit einer stabilen `d`-Identität, genau einem Heimatkanal in einem `h`-tag und Revisionen als vollständige Snapshots, die durch `prev` verknüpft sind. Ein relay akzeptiert eine Änderung nur, wenn `prev` den aktuellen Stand bezeichnet. Zwei konkurrierende Revisionen können daher nicht beide zum nächsten aktuellen Stand werden. Die Implementierung von Buzz verwendet kind `45010` für Artefakte und einen vom relay signierten Marker mit kind `45011`, wenn ein Artefakt aus einem Kanal verschoben wird. Der Quellkanal sieht die Entfernung, ohne durch diesen Marker das Ziel zu erfahren.

Der [Merge der Buzz-Spezifikation](https://github.com/block/buzz/pull/7791) beschreibt das Modell, und der [Merge der relay-Implementierung](https://github.com/block/buzz/pull/7919) berichtet über Tests für die Konfliktbehandlung, Verlaufsabfragen, Verschiebungen und Kanalberechtigungen. Diese Merges belegen das Verhalten des Projektquellcodes, nicht einen allgemeinen Nostr-Standard oder eine Garantie für eine öffentliche Bereitstellung.

---

**Primärquellen:**
- [Merge der Buzz-Spezifikation für Kanal-Artefakte](https://github.com/block/buzz/pull/7791)
- [Merge der Buzz-Implementierung für Kanal-Artefakte](https://github.com/block/buzz/pull/7919)

**Erwähnt in:**
- [Newsletter #42: Kanal-Artefakte in Buzz](/de/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
