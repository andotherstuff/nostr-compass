---
title: "NIP-19: Bech32-kodierte Entitäten"
date: 2025-12-17
translationOf: /en/topics/nip-19.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Identity
---

NIP-19 definiert menschenfreundliche Formate zum Teilen von Nostr-Identifikatoren. Diese bech32-kodierten Zeichenketten werden für Anzeige und Weitergabe verwendet, aber nie im Protokoll selbst, das Hex verwendet.

## Wie es funktioniert

Rohe Hex-Keys sind fehleranfällig beim Kopieren und visuell kaum zu unterscheiden. Die Bech32-Kodierung fügt ein menschenlesbares Präfix und eine Prüfsumme hinzu. Dadurch wird klar, welche Art von Daten vorliegt, und viele Kopierfehler werden erkannt.

Die Grundformen kodieren jeweils einen einzelnen 32-Byte-Wert:

- **npub** - Public Key, also deine Identität, sicher zum Teilen
- **nsec** - Private Key, geheim halten, wird zum Signieren verwendet
- **note** - Event-ID, verweist auf ein bestimmtes Event

Beispiel: Der Hex-Pubkey `3bf0c63f...` wird zu `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

Die erweiterten Formen verwenden TLV-Kodierung, damit sie zusätzlich Lookup-Hints neben dem Identifikator selbst transportieren können:

- **nprofile** - Profil mit Relay-Hints
- **nevent** - Event mit Relay-Hints, Author Pubkey und Kind
- **naddr** - Addressable-Event-Referenz mit Pubkey, Kind, `d`-Tag und Relay-Hints

## Warum es wichtig ist

Relay-Hints sind nicht autoritativ, entscheiden aber oft darüber, ob ein Client ein geteiltes Event beim ersten Versuch abrufen kann. Deshalb sind `nevent`, `nprofile` und `naddr` meist bessere Formate zum Teilen als ein nacktes `note` oder `npub`, wenn Inhalte außerhalb des aktuellen Relay-Sets des Empfängers liegen.

Ein weiterer praktischer Unterschied ist die Stabilität. `note` zeigt auf eine unveränderliche Event-ID, während `naddr` auf ein addressable Event zeigt, das im Laufe der Zeit ersetzt werden kann. Für Longform-Inhalte, Kalender oder Repository-Ankündigungen ist `naddr` meist der richtige Link-Typ.

## Implementierungshinweise

- Verwende Bech32 nur in Interfaces für Menschen: Anzeige, Copy/Paste, QR-Codes, URLs
- Verwende Bech32-Formate niemals in Protokollnachrichten, Events oder NIP-05-Antworten
- Jede Protokollkommunikation muss Hex-Kodierung verwenden
- Wenn du `nevent`, `nprofile` oder `naddr` erzeugst, füge Relay-Hints für bessere Discoverability hinzu
- Behandle `nsec` überall als geheimes Material. Ein Client sollte es niemals standardmäßig anzeigen, loggen oder in Support-Exporten mitgeben

---

**Primärquellen:**
- [NIP-19 Specification](https://github.com/nostr-protocol/nips/blob/master/19.md)

**Erwähnt in:**
- [Newsletter #1: NIP Deep Dive](/en/newsletters/2025-12-17-newsletter/#nip-19-bech32-encoded-identifiers)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/#damus-ios)
- [Newsletter #4: Relay Hint Support](/en/newsletters/2026-01-07-newsletter/)
- [Newsletter #8: Damus iOS](/en/newsletters/2026-02-04-newsletter/#damus-ios)
- [Newsletter #11: notecrumbs](/en/newsletters/2026-02-25-newsletter/)

**Siehe auch:**
- [NIP-01: Basic Protocol](/de/topics/nip-01/)
- [NIP-10: Reply Threads](/de/topics/nip-10/)
