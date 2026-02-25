---
title: "NIP-90"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - DVM
---

NIP-90 definiert Data Vending Machines (DVMs), ein Marktplatz-Protokoll für das Anfordern und Bezahlen von Rechenarbeit auf Nostr.

## Funktionsweise

Clients veröffentlichen Job-Anfrage-Events (kinds 5000-5999), die die benötigte Arbeit spezifizieren. Service Provider überwachen Anfragen, die ihren Fähigkeiten entsprechen, und veröffentlichen Ergebnisse nach Abschluss der Berechnung. Die Bezahlung erfolgt über Lightning oder andere im Job-Ablauf ausgehandelte Mechanismen.

Job-Kinds definieren verschiedene Berechnungstypen: Textgenerierung, Bildgenerierung, Übersetzung, Content-Discovery und mehr. Jeder Kind spezifiziert das erwartete Eingabe-/Ausgabeformat.

## Hauptmerkmale

- Dezentraler Rechenmarktplatz
- Kind-basiertes Job-Typsystem
- Provider-Wettbewerb nach Preis und Qualität
- Erweiterbar für neue Berechnungstypen

---

**Primärquellen:**
- [NIP-90 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/90.md)

**Erwähnt in:**
- [Newsletter #11: NIP-AC DVM Agent Coordination](/de/newsletters/2026-02-25-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-85: Trusted Assertions](/de/topics/nip-85/)
