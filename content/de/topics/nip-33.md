---
title: "NIP-33: Parametrisierte ersetzbare Events (adressierbare Events)"
date: 2026-03-11
translationOf: /en/topics/nip-33.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-33 definierte ursprünglich parametrisierte ersetzbare Events, eine Event-Klasse, bei der Relays nur ein Event pro Tupel `(pubkey, kind, d-tag)` behalten. Das Konzept wurde inzwischen in „adressierbare Events" umbenannt und in [NIP-01](/de/topics/nip-01/) integriert. Das NIP-33-Dokument verweist jetzt auf NIP-01, bleibt aber in Codebasen und Dokumentation eine gebräuchliche Referenz.

## Wie es funktioniert

Ein adressierbares Event verwendet einen kind im Bereich `30000-39999`. Jedes Event trägt ein `d`-Tag, dessen Wert zusammen mit dem pubkey des Autors und der kind-Nummer eine eindeutige Adresse bildet. Wenn ein Relay ein neues Event empfängt, das zu einem vorhandenen Tupel `(pubkey, kind, d-tag)` passt, ersetzt es das ältere Event durch das neuere (nach `created_at`). Das macht adressierbare Events nützlich für veränderbaren Zustand: Profile, Einstellungen, App-Konfigurationen, Kleinanzeigen und ähnliche Strukturen, bei denen nur die neueste Version zählt.

Clients referenzieren adressierbare Events mit `a`-Tags im Format `<kind>:<pubkey>:<d-tag>`, optional gefolgt von einem Relay-Hinweis.

## Häufige Einsatzfälle

- Kind `30023` Langformartikel
- Kind `30078` app-spezifische Daten (verwendet von NIP-78)
- Kind `31923` Kalender-Events (NIP-52)
- Kind `31990` Handler-Empfehlungen (NIP-89)
- Kind `30009` Badge-Definitionen (NIP-58)
- Kind `31991` Agent-Run-Konfigurationen (Notedeck Agentium)

## Beziehung zu NIP-01

NIP-33 wurde im Rahmen einer Konsolidierung in NIP-01 integriert. Die NIP-01-Spezifikation definiert jetzt drei Kategorien für Event-Aufbewahrung: reguläre Events (werden unverändert behalten), ersetzbare Events (eins pro `(pubkey, kind)`) und adressierbare Events (eins pro `(pubkey, kind, d-tag)`). NIP-33 bleibt eine gültige Kurzform für das Konzept adressierbarer Events.

---

**Primärquellen:**
- [NIP-33 (Weiterleitung)](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [NIP-01 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/01.md) - Abschnitt zu adressierbaren Events

**Erwähnt in:**
- [Newsletter #13: Notedeck](/de/newsletters/2026-03-11-newsletter/#notedeck-adds-nip-11-relay-limits-and-agentium-features)

**Siehe auch:**
- [NIP-01: Grundlegendes Protokoll](/de/topics/nip-01/)
