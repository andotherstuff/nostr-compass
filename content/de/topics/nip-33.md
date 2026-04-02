---
title: "NIP-33: Parameterized Replaceable Events (Addressable Events)"
date: 2026-03-11
translationOf: /en/topics/nip-33.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-33 definierte ursprünglich parametrisierte ersetzbare Events, eine Klasse von Events, bei der Relays pro `(pubkey, kind, d-tag)`-Tupel nur ein Event vorhalten. Das Konzept wurde inzwischen in „Addressable Events" umbenannt und in [NIP-01](/de/topics/nip-01/) integriert. Das NIP-33-Dokument leitet nun auf NIP-01 weiter, bleibt aber eine gängige Referenz in Codebases und Dokumentation.

## Funktionsweise

Ein Addressable Event verwendet einen Kind im Bereich `30000-39999`. Jedes Event trägt einen `d`-Tag, dessen Wert zusammen mit dem Pubkey des Autors und der Kind-Nummer eine eindeutige Adresse bildet. Wenn ein Relay ein neues Event erhält, das einem bestehenden `(pubkey, kind, d-tag)`-Tupel entspricht, ersetzt es das ältere Event durch das neuere (nach `created_at`). Das macht Addressable Events nützlich für veränderlichen Zustand: Profile, Einstellungen, App-Konfigurationen, Kleinanzeigen und ähnliche Strukturen, bei denen nur die neueste Version zählt.

Clients referenzieren Addressable Events mit `a`-Tags im Format `<kind>:<pubkey>:<d-tag>`, optional gefolgt von einem Relay-Hint.

## Häufige Verwendungen

- Kind `30023` Langform-Artikel
- Kind `30078` App-spezifische Daten (verwendet von NIP-78)
- Kind `31923` Kalenderevents (NIP-52)
- Kind `31990` Handler-Empfehlungen (NIP-89)
- Kind `30009` Badge-Definitionen (NIP-58)
- Kind `31991` Agent-Run-Konfigurationen (Notedeck Agentium)

## Verhältnis zu NIP-01

NIP-33 wurde im Rahmen einer Konsolidierung in NIP-01 integriert. Die NIP-01-Spezifikation definiert nun drei Event-Aufbewahrungskategorien: reguläre Events (unverändert aufbewahrt), ersetzbare Events (eines pro `(pubkey, kind)`) und adressierbare Events (eines pro `(pubkey, kind, d-tag)`). NIP-33 bleibt ein gängiges Kürzel für das Addressable-Event-Konzept.

---

**Primärquellen:**
- [NIP-33 (Weiterleitung)](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [NIP-01-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/01.md) - Abschnitt Addressable Events

**Erwähnt in:**
- [Newsletter #13: Notedeck](/en/newsletters/2026-03-11-newsletter/#notedeck-adds-nip-11-relay-limits-and-agentium-features)

**Siehe auch:**
- [NIP-01: Basic Protocol](/de/topics/nip-01/)
