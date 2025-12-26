---
title: "NIP-29: Relay-basierte Gruppen"
date: 2025-12-24
draft: false
categories:
  - Social
  - Groups
---

NIP-29 definiert Relay-basierte Gruppen, bei denen ein Relay die Gruppenmitgliedschaft, Berechtigungen und Nachrichtensichtbarkeit verwaltet.

## Gruppenzugriffs-Tags

- **private**: Nur Mitglieder können Gruppennachrichten lesen
- **closed**: Beitrittsanfragen werden ignoriert (nur auf Einladung)
- **hidden**: Relay verbirgt Gruppenmetadaten vor Nicht-Mitgliedern, sodass die Gruppe nicht auffindbar ist
- **restricted**: Nur Mitglieder können Nachrichten an die Gruppe schreiben

Diese Tags können kombiniert werden. Eine Gruppe kann `restricted` (schreibbeschränkt) sein, aber nicht `hidden` (immer noch auffindbar). Das Weglassen eines Tags aktiviert das gegenteilige Verhalten: kein `private` bedeutet, jeder kann lesen, kein `closed` bedeutet, Beitrittsanfragen werden berücksichtigt.

## Funktionsweise

Das Relay ist die Autorität für Gruppenoperationen:
- Pflegt die Mitgliederliste und Rollen
- Setzt Schreibberechtigungen durch
- Kontrolliert, was Nicht-Mitglieder sehen können

Clients senden Gruppennachrichten an das Relay, das die Mitgliedschaft validiert, bevor es sie akzeptiert.

## Privatsphäre-Überlegungen

- `hidden`-Gruppen bieten den stärksten Schutz vor Auffindbarkeit: Sie erscheinen nicht in Suchen oder Relay-Listen
- `private`-Gruppen verbergen den Nachrichteninhalt vor Nicht-Mitgliedern
- `closed`-Gruppen ignorieren einfach Beitrittsanfragen; kombinieren Sie mit `private` oder `hidden` für stärkere Zugangskontrolle
- `restricted` kontrolliert, wer schreiben kann, unabhängig vom Lesezugriff

---

**Primärquellen:**
- [NIP-29 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/29.md)

**Erwähnt in:**
- [Newsletter #2: NIP-Updates](/de/newsletters/2025-12-24-newsletter/#nip-updates)
