---
title: "NIP-43: Relay Access Metadata and Requests"
date: 2026-03-18
translationOf: /en/topics/nip-43.md
translationDate: 2026-04-01
draft: false
categories:
  - Protocol
  - Relay
  - Access Control
---

NIP-43 definiert, wie Relays Mitgliedschaftsinformationen veröffentlichen und wie Nutzer Aufnahme, Einladungen oder Entfernung bei eingeschränkten Relays beantragen. Es gibt der Relay-Zugangskontrolle eine standardisierte Event-Oberfläche, anstatt jedes private oder halbprivate Relay zu zwingen, sein eigenes Beitrittsprotokoll zu erfinden.

## Funktionsweise

Die Spezifikation kombiniert mehrere Event-Kinds:

- Kind `13534` veröffentlicht eine Relay-Mitgliedschaftsliste
- Kind `8000` kündigt an, dass ein Mitglied hinzugefügt wurde
- Kind `8001` kündigt an, dass ein Mitglied entfernt wurde
- Kind `28934` erlaubt einem Nutzer, einen Beitrittsantrag mit einem Claim-Code einzureichen
- Kind `28935` erlaubt einem Relay, auf Anfrage einen Einladungscode zurückzugeben
- Kind `28936` erlaubt einem Nutzer, den Widerruf seines eigenen Zugangs zu beantragen

Der Mitgliedschaftsstatus wird absichtlich nicht aus einem einzigen Event abgeleitet. Ein Client muss möglicherweise sowohl die Relay-signierten Mitgliedschafts-Events als auch die eigenen Events des Mitglieds konsultieren, bevor er entscheidet, ob der Zugang aktuell ist.

## Warum das wichtig ist

NIP-43 gibt eingeschränkten Relays einen Standardweg, Aufnahme- und Mitgliedschaftsstatus auszudrücken. Das ist wichtig für Gruppensysteme, Einladungs-Communities und Relays, die maschinenlesbares Onboarding benötigen, ohne auf externe Webformulare oder manuelle Betreiber-Workflows zurückzugreifen.

Die offene Klarstellung in [PR #2267](https://github.com/nostr-protocol/nips/pull/2267) präzisiert einen praktischen Punkt: Relays sollten einen autoritativen Mitgliedschaftsstatus pro Pubkey führen. Das hilft Clients, mehrdeutige Replay-Historien zu vermeiden, bei denen ein altes Hinzufügen- oder Entfernen-Event als aktueller Status fehlinterpretiert werden kann.

## Interop-Hinweise

NIP-43 setzt voraus, dass das Relay seine Unterstützung über sein [NIP-11](/de/topics/nip-11/)-Dokument ankündigt. Beitrittsanträge, Einladungsanfragen und Austrittsanträge sollten nur an Relays gesendet werden, die explizit angeben, dieses NIP zu unterstützen.

Da die Events gleichzeitig im Relay-kontrollierten und im Nutzer-kontrollierten Raum liegen, benötigen Implementierungen klare Konfliktregeln. Deshalb ist die Klarstellung zum Mitgliedschaftsstatus wichtiger, als sie zunächst erscheint.

---

**Primärquellen:**
- [NIP-43-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/43.md)
- [PR #2267](https://github.com/nostr-protocol/nips/pull/2267) - Klarstellung zur Mitgliedschaftsstatus-Behandlung

**Erwähnt in:**
- [Newsletter #14: NIP-Updates](/de/newsletters/2026-03-18-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-11: Relay Information Document](/de/topics/nip-11/)
- [NIP-42: Authentication of Clients to Relays](/de/topics/nip-42/)
