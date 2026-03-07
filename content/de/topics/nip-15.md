---
title: "NIP-15: Nostr Marktplatz"
date: 2026-01-28
translationOf: /en/topics/nip-15.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Commerce
  - Marketplace
---

NIP-15 definiert ein Protokoll für dezentrale Marktplätze auf Nostr. Es ermöglicht Händlern, Produkte zu listen, und Käufern, Einkäufe mit Bitcoin und Lightning zu tätigen.

## Wie es funktioniert

### Merchant Stalls (Kind 30017)

Händler erstellen Stalls als addressable Events:

```json
{
  "kind": 30017,
  "tags": [
    ["d", "my-stall"],
    ["name", "Bob's Electronics"],
    ["description", "Quality used electronics"],
    ["currency", "sat"],
    ["shipping", "{...shipping options...}"]
  ]
}
```

### Products (Kind 30018)

Produkte werden innerhalb von Stalls gelistet:

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

1. Der Käufer durchsucht Produkte in mehreren Stalls
2. Der Käufer sendet eine verschlüsselte Bestellnachricht an den Händler
3. Der Händler antwortet mit einer Lightning-Invoice
4. Der Käufer bezahlt die Invoice
5. Der Händler versendet das Produkt

## Warum es wichtig ist

- **Dezentralisiert**: Kein zentraler Marktplatzbetreiber
- **Interoperabel**: Jeder NIP-15-Client kann jeden Händler durchsuchen
- **Privat**: Bestellungen sind zwischen Käufer und Verkäufer verschlüsselt
- **Bitcoin-native**: Lightning-Zahlungen sind eingebaut

Der praktische Gewinn ist Portabilität. Ein Händler kann Katalogdaten einmal veröffentlichen und sie dann von mehreren Clients darstellen lassen, statt an ein einziges Marktplatz-Frontend gebunden zu sein.

## Tradeoffs

NIP-15 standardisiert Listings, nicht Vertrauen. Käufer müssen weiter selbst entscheiden, ob ein Händler legitim ist, ob der Bestand real ist und wie Streitfälle behandelt werden. Das Protokoll liefert gemeinsame Datenstrukturen und einen gemeinsamen Nachrichtenfluss, aber Reputation und Fulfillment bleiben Probleme auf Anwendungsebene.

Auch Zahlungen und Versand sind nur teilweise standardisiert. Ein Client kann Stalls und Produkte verstehen und trotzdem eigene Logik für Invoices, Bestellstatus oder Tracking brauchen.

## Implementierungsstatus

- **Plebeian Market** - Full-featured NIP-15 marketplace
- **Shopstr** - Permissionless Bitcoin commerce
- **Amethyst** - Integrated product listings in social feed

---

**Primärquellen:**
- [NIP-15 Specification](https://github.com/nostr-protocol/nips/blob/master/15.md)

**Erwähnt in:**
- [Newsletter #7: January 2024 Protocol Hardening](/en/newsletters/2026-01-28-newsletter/#january-2024-protocol-hardening)

**Siehe auch:**
- [NIP-44: Encrypted Payloads](/de/topics/nip-44/)
- [NIP-57: Lightning Zaps](/de/topics/nip-57/)
