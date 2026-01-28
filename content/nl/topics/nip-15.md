---
title: "NIP-15: Nostr Marketplace"
date: 2026-01-28
translationOf: /en/topics/nip-15.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Commerce
  - Marketplace
---

NIP-15 definieert een protocol voor gedecentraliseerde marktplaatsen op Nostr, waarmee handelaren producten kunnen aanbieden en kopers aankopen kunnen doen met Bitcoin en Lightning.

## Hoe Het Werkt

### Handelaarskraampjes (Kind 30017)

Handelaren creëren kraampjes als adresseerbare events:

```json
{
  "kind": 30017,
  "tags": [
    ["d", "my-stall"],
    ["name", "Bob's Electronics"],
    ["description", "Kwaliteit tweedehands elektronica"],
    ["currency", "sat"],
    ["shipping", "{...verzendopties...}"]
  ]
}
```

### Producten (Kind 30018)

Producten worden binnen kraampjes geplaatst:

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

## Aankoopproces

1. Koper bladert door producten over meerdere kraampjes
2. Koper stuurt versleuteld bestelverzoek naar handelaar
3. Handelaar reageert met Lightning-factuur
4. Koper betaalt factuur
5. Handelaar verstuurt product

## Belangrijke Kenmerken

- **Gedecentraliseerd**: Geen centrale marktplaatsoperator
- **Interoperabel**: Elke NIP-15 client kan bij elke handelaar bladeren
- **Privé**: Bestellingen zijn versleuteld tussen koper en verkoper
- **Bitcoin-native**: Lightning-betalingen ingebouwd

## Implementaties

- **Plebeian Market** - Volledig uitgeruste NIP-15 marktplaats
- **Shopstr** - Toestemmingsloze Bitcoin-handel
- **Amethyst** - Geïntegreerde productlistings in sociale feed

## Gerelateerd

- [NIP-44](/nl/topics/nip-44/) - Versleutelde berichten voor bestellingen
- [NIP-57](/nl/topics/nip-57/) - Lightning Zaps
