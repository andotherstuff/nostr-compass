---
title: "NIP-19: Bech32-kodierte Entitäten"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identity
---

NIP-19 definiert menschenfreundliche Formate zum Teilen von Nostr-Identifikatoren. Diese bech32-kodierten Zeichenketten werden zur Anzeige und zum Teilen verwendet, werden aber niemals im Protokoll selbst verwendet (das Hex verwendet).

## Warum Bech32?

Rohe Hex-Schlüssel sind fehleranfällig beim Kopieren und visuell nicht unterscheidbar. Die Bech32-Kodierung fügt ein menschenlesbares Präfix und eine Prüfsumme hinzu, wodurch sofort klar wird, welche Art von Daten Sie betrachten.

## Grundformate

Diese kodieren rohe 32-Byte-Werte:

- **npub** - Öffentlicher Schlüssel (Ihre Identität, sicher zum Teilen)
- **nsec** - Privater Schlüssel (geheim halten, zum Signieren verwendet)
- **note** - Event-ID (verweist auf ein bestimmtes Event)

Beispiel: Der Hex-Pubkey `3bf0c63f...` wird zu `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

## Teilbare Identifikatoren

Diese verwenden TLV-Kodierung (Type-Length-Value), um Metadaten einzuschließen:

- **nprofile** - Profil mit Relay-Hinweisen (hilft Clients, den Benutzer zu finden)
- **nevent** - Event mit Relay-Hinweisen, Autor-Pubkey und Kind
- **naddr** - Adressierbarer Event-Verweis (Pubkey + Kind + d-Tag + Relays)

Diese lösen das Entdeckungsproblem: Wenn jemand eine Notiz-ID teilt, woher wissen Clients, welches Relay sie hat? Durch das Bündeln von Relay-Hinweisen in den Identifikator werden geteilte Links zuverlässiger.

## Implementierungshinweise

- Verwenden Sie Bech32 nur für menschliche Schnittstellen: Anzeige, Kopieren/Einfügen, QR-Codes, URLs
- Verwenden Sie niemals Bech32-Formate in Protokollnachrichten, Events oder NIP-05-Antworten
- Alle Protokollkommunikation muss Hex-Kodierung verwenden
- Beim Generieren von nevent/nprofile/naddr, schließen Sie Relay-Hinweise für bessere Auffindbarkeit ein

---

**Primärquellen:**
- [NIP-19 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/19.md)

**Erwähnt in:**
- [Newsletter #1: NIP Deep Dive](/de/newsletters/2025-12-17-newsletter/#nip-19-bech32-encoded-identifiers)

**Siehe auch:**
- [NIP-01: Basisprotokoll](/de/topics/nip-01/)
- [NIP-21: nostr: URI-Schema](https://github.com/nostr-protocol/nips/blob/master/21.md)
