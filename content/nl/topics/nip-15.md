---
title: "NIP-15: Nostr Marketplace"
date: 2026-01-28
translationOf: /en/topics/nip-15.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Commerce
  - Marketplace
---

NIP-15 definieert een protocol voor gedecentraliseerde marktplaatsen op Nostr, waarmee verkopers producten kunnen aanbieden en kopers aankopen kunnen doen met Bitcoin en Lightning.

## Hoe het werkt

### Merchant Stalls (Kind 30017)

Verkopers maken stalls aan als adresseerbare events:

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

Producten worden binnen stalls gepubliceerd:

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

1. De koper bekijkt producten uit meerdere stalls
2. De koper stuurt een versleuteld orderbericht naar de verkoper
3. De verkoper antwoordt met een Lightning invoice
4. De koper betaalt de invoice
5. De verkoper verzendt het product

## Waarom het belangrijk is

- **Gedecentraliseerd**: Geen centrale marktplaatsexploitant
- **Interoperabel**: Elke NIP-15 client kan elke verkoper tonen
- **Privé**: Orders zijn versleuteld tussen koper en verkoper
- **Bitcoin-native**: Lightning-betalingen zijn ingebouwd

De praktische winst is portabiliteit. Een verkoper kan catalogusdata één keer publiceren en meerdere clients die laten weergeven, zonder vast te zitten aan één marketplace-frontend.

## Afwegingen

NIP-15 standaardiseert listings, niet vertrouwen. Kopers moeten nog steeds bepalen of een verkoper legitiem is, of de voorraad echt is en hoe geschillen worden afgehandeld. Het protocol geeft gemeenschappelijke datastructuren en een berichtstroom, maar reputatie en fulfillment blijven problemen op applicatieniveau.

Betalingen en verzending zijn ook maar deels gestandaardiseerd. Een client kan stalls en producten begrijpen en toch nog aangepaste logica nodig hebben voor invoices, orderstatus of tracking van leveringen.

## Implementatiestatus

- **Plebeian Market** - Volwaardige NIP-15 marketplace
- **Shopstr** - Permissionless Bitcoin commerce
- **Amethyst** - Geïntegreerde productvermeldingen in de sociale feed

---

**Primaire bronnen:**
- [NIP-15 Specification](https://github.com/nostr-protocol/nips/blob/master/15.md)

**Vermeld in:**
- [Nieuwsbrief #7: January 2024 Protocol Hardening](/en/newsletters/2026-01-28-newsletter/#january-2024-protocol-hardening)

**Zie ook:**
- [NIP-44: Encrypted Payloads](/nl/topics/nip-44/)
- [NIP-57: Lightning Zaps](/nl/topics/nip-57/)
