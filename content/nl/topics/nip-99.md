---
title: "NIP-99: Rubrieksadvertenties"
date: 2026-03-11
translationOf: /en/topics/nip-99.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Commerce
  - Marketplaces
---

NIP-99 definieert adresseerbare classified-listing-events voor goederen, diensten, banen, verhuur en andere aanbiedingen. Het geeft marketplace-apps een eenvoudiger eventmodel dan de oudere marketplace-specificatie van [NIP-15](/nl/topics/nip-15/), en daarom bouwen veel huidige commerce-clients op NIP-99 voort.

## Hoe het werkt

Actieve listings gebruiken kind `30402`, terwijl drafts of inactieve listings kind `30403` gebruiken. De pubkey van de auteur is de verkoper of maker van de aanbieding. Het veld `content` bevat de menselijk leesbare beschrijving in Markdown, terwijl de tags gestructureerde velden bevatten zoals titel, samenvatting, prijs, locatie en status.

```json
{
  "id": "b3e392b11f5d4f28321cedd09303a748acfd0487aea5a7450b3481c60b6e4f87",
  "pubkey": "a695f6b60119d9521934a691347d9f78e8770b56da16bb255ee286ddf9fda919",
  "created_at": 1741699200,
  "kind": 30402,
  "tags": [
    ["d", "shopstr-handmade-wallet-001"],
    ["title", "Handmade leather wallet"],
    ["summary", "Brown bifold wallet with Bitcoin and Nostr branding"],
    ["published_at", "1741699200"],
    ["location", "Austin, TX"],
    ["price", "75000", "SAT"],
    ["status", "active"],
    ["t", "merch"],
    ["t", "bitcoin"]
  ],
  "content": "Full listing description in Markdown, shipping details, and contact terms.",
  "sig": "4a5c7e8f9012ab34cd56ef7890ab12cd34ef56ab78cd90ef12ab34cd56ef78900112233445566778899aabbccddeeff00112233445566778899aabbccddeeff"
}
```

Het event is adresseerbaar, zodat een verkoper de listing kan bijwerken terwijl dezelfde identiteitstuple van pubkey, kind en `d` tag behouden blijft. Daardoor zijn listingrevisies schoner voor clients dan telkens een volledig nieuw onveranderlijk note publiceren voor elke prijs- of statuswijziging.

## Waarom het belangrijk is

De kracht van NIP-99 is dat het ruimte laat voor verschillende marketplace-ontwerpen en tegelijk de kernvorm van de listing standaardiseert. De ene client kan zich richten op lokale classifieds, een andere op abonnementen en weer een andere op wereldwijde productcatalogi. Als ze het eens zijn over de eventstructuur, kunnen verkopers een keer publiceren en toch enige zichtbaarheid tussen clients krijgen.

Die flexibiliteit verklaart ook waarom huidige marketplace-projecten hiervoor kiezen. De specificatie is gestructureerd genoeg om zoeken en weergeven te ondersteunen, maar dwingt niet elke app in een enkele escrow-, verzending- of betaalworkflow.

## Implementatienotities

- `price` tags kunnen een eenmalige of terugkerende betaling beschrijven door een optioneel frequentieveld toe te voegen.
- `t` tags fungeren als categorieen of zoekwoorden.
- `image` tags laten clients galerijweergaven renderen zonder de Markdown-body te parseren.
- Een listing kan met `e` of `a` tags naar gerelateerde events of documenten linken wanneer een marketplace rijkere productcontext wil bieden.

## Implementaties

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Nostr-marketplace die NIP-99-listings gebruikt met agentgerichte MCP-endpoints
- [Milk Market](https://github.com/shopstr-eng/milk-market) - voedselmarketplace gebouwd op dezelfde listinglaag met gemengde betaalopties

---

**Primaire bronnen:**
- [NIP-99 Specification](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - MCP-commerce-endpoints boven op NIP-99-listings
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - abonnementen en multi-merchant-checkout boven op marketplace-listings

**Vermeld in:**
- [Nieuwsbrief #13: Shopstr and Milk Market Open MCP Commerce Surfaces](/nl/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces)

**Zie ook:**
- [NIP-15: Marketplace Offers](/nl/topics/nip-15/)
- [NIP-47: Nostr Wallet Connect](/nl/topics/nip-47/)
- [NIP-60: Cashu Wallet](/nl/topics/nip-60/)
