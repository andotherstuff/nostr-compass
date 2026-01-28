---
title: "NIP-15: Nostr Marktplatz"
date: 2026-01-28
translationOf: /en/topics/nip-15.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Commerce
  - Marketplace
---

NIP-15 definiert ein Protokoll für dezentralisierte Marktplätze auf Nostr, das es Händlern ermöglicht, Produkte anzubieten und Käufern, Einkäufe mit Bitcoin und Lightning zu tätigen.

## Funktionsweise

### Händler-Stände (Kind 30017)

Händler erstellen Stände als adressierbare Events:

```json
{
  "kind": 30017,
  "tags": [
    ["d", "my-stall"],
    ["name", "Bobs Elektronik"],
    ["description", "Qualitäts-Gebraucht-Elektronik"],
    ["currency", "sat"],
    ["shipping", "{...Versandoptionen...}"]
  ]
}
```

### Produkte (Kind 30018)

Produkte werden innerhalb von Ständen aufgelistet:

```json
{
  "kind": 30018,
  "tags": [
    ["d", "product-123"],
    ["stall_id", "my-stall"],
    ["name", "Raspberry Pi 4"],
    ["price", "50000"],
    ["quantity", "5"],
    ["images", "https://..."]
  ]
}
```

## Kaufablauf

1. Käufer durchsucht Produkte über mehrere Stände
2. Käufer sendet verschlüsselte Bestellnachricht an Händler
3. Händler antwortet mit Lightning-Invoice
4. Käufer bezahlt Invoice
5. Händler versendet Produkt

## Hauptfunktionen

- **Dezentralisiert**: Kein zentraler Marktplatzbetreiber
- **Interoperabel**: Jeder NIP-15-Client kann jeden Händler durchsuchen
- **Privat**: Bestellungen sind zwischen Käufer und Verkäufer verschlüsselt
- **Bitcoin-nativ**: Lightning-Zahlungen integriert

## Implementierungen

- **Plebeian Market** - Voll ausgestatteter NIP-15-Marktplatz
- **Shopstr** - Erlaubnisfreier Bitcoin-Handel
- **Amethyst** - Integrierte Produktlistungen im sozialen Feed

## Verwandt

- [NIP-44](/de/topics/nip-44/) - Verschlüsselte Nachrichten für Bestellungen
- [NIP-57](/de/topics/nip-57/) - Lightning Zaps
