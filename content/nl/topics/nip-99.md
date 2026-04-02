---
title: "NIP-99: Classified Listings"
date: 2026-03-11
translationOf: /en/topics/nip-99.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Commerce
  - Marketplaces
---

NIP-99 definieert addressable classified-listing events voor goederen, diensten, banen, verhuur en andere aanbiedingen. Het geeft marktplaatsapps een eenvoudiger eventmodel dan de oudere [NIP-15](/nl/topics/nip-15/) marktplaatsspecificatie, wat verklaart waarom veel huidige commerceapplicaties op NIP-99 bouwen.

## Hoe Het Werkt

Actieve advertenties gebruiken kind `30402`, terwijl concepten of inactieve advertenties kind `30403` gebruiken. De auteur-pubkey is de verkoper of aanbiedingsmaker. Het `content`-veld bevat de leesbare beschrijving in Markdown, en de tags bevatten gestructureerde velden zoals titel, samenvatting, prijs, locatie en status.

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

Het event is addressable, zodat een verkoper de advertentie kan bijwerken terwijl dezelfde identiteitstuple van pubkey, kind en `d` tag behouden blijft. Dat maakt advertentierevisies schoner voor clients dan het publiceren van een geheel nieuwe onveranderlijke note voor elke prijs- of statuswijziging.

## Waarom Het Belangrijk Is

De kracht van NIP-99 is dat het ruimte laat voor verschillende marktplaatsontwerpen terwijl de kern-advertentievorm wordt gestandaardiseerd. De ene client kan zich richten op lokale advertenties, een andere op abonnementen, en weer een andere op wereldwijde productcatalogi. Als ze het allemaal eens zijn over de eventstructuur, kunnen verkopers eenmalig publiceren en toch enige cross-clientzichtbaarheid krijgen.

Die flexibiliteit verklaart ook waarom huidige marktplaatsprojecten het verkiezen. De specificatie is gestructureerd genoeg om zoeken en weergave te ondersteunen, maar dwingt niet elke app in één enkele escrow-, verzend- of betalingsworkflow.

## Implementatienotities

- `price` tags kunnen eenmalige of terugkerende betalingen beschrijven door een optioneel frequentieveld toe te voegen.
- `t` tags fungeren als categorieën of zoektrefwoorden.
- `image` tags laten clients galerijweergaven renderen zonder de Markdown-body te parsen.
- Een advertentie kan linken naar gerelateerde events of documenten met `e` of `a` tags wanneer een marktplaats rijkere productcontext wil bieden.

## Implementaties

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Nostr-marktplaats met NIP-99 advertenties en agent-gerichte MCP-eindpunten
- [Milk Market](https://github.com/shopstr-eng/milk-market) - Voedselmarktplaats gebouwd op dezelfde advertentielaag met gemixte betaalopties

---

**Primaire bronnen:**
- [NIP-99 Specificatie](https://github.com/nostr-protocol/nips/blob/master/99.md)
- [Shopstr PR #234](https://github.com/shopstr-eng/shopstr/pull/234) - MCP-commerceëindpunten bovenop NIP-99 advertenties
- [Milk Market PR #10](https://github.com/shopstr-eng/milk-market/pull/10) - Abonnements- en multi-merchant checkout bovenop marktplaatsadvertenties

**Vermeld in:**
- [Newsletter #13: Shopstr and Milk Market Open MCP Commerce Surfaces](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces)

**Zie ook:**
- [NIP-15: Marketplace Offers](/nl/topics/nip-15/)
- [NIP-47: Nostr Wallet Connect](/nl/topics/nip-47/)
- [NIP-60: Cashu Wallet](/nl/topics/nip-60/)
