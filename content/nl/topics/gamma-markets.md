---
title: "Gamma Markets"
date: 2026-07-15
draft: false
translationOf: /en/topics/gamma-markets.md
translationDate: 2026-07-15
categories:
  - Commerce
  - Marketplace
  - Protocol
---

Gamma Markets is een set e-commerceconventies die direct bovenop [NIP-99](/nl/topics/nip-99/)-advertenties is gebouwd, gezamenlijk ontwikkeld door een werkgroep van Nostr-marktplaatsontwikkelaars: de teams achter Shopstr, Cypher, Plebeian Market en Conduit Market. Het vult de conventies voor verzending, bestelstroom, collecties en recensies in die NIP-99 zelf ongedefinieerd laat.

## Hoe het werkt

Gamma Markets voegt vijf eventkinds toe rond het bestaande kind `30402`-advertentie-event van NIP-99, zonder de vorm van dat event te veranderen:

- **Kind 30405** - productcollecties, die meerdere advertenties groeperen via `a`-tags
- **Kind 30406** - verzendopties, met prijzen per land en optionele kostenregels op basis van gewicht of afstand
- **Kind 16** - bestelberichten: aanmaken (type 1), betalingsverzoeken (type 2), statusupdates (type 3) en verzendupdates (type 4)
- **Kind 14** - algemene communicatie tussen koper en verkoper
- **Kind 17** - betalingsbonnen
- **Kind 31555** - productrecensies, geadresseerd aan een specifieke verkoper-pubkey en advertentie-`d`-tag

De betalingsvoorkeuren van een verkoper worden verklaard via een `payment_preference`-tag op hun kind `0`-profielmetadata, en clients ontdekken compatibele apps via [NIP-89](/nl/topics/nip-89/)-applicatieaanbevelingen. Bestelcommunicatie bouwt voort op [NIP-17](/nl/topics/nip-17/) privéberichten, zonder een eigen nieuw versleutelingsschema.

De bepalende ontwerpkeuze van de specificatie is dat niets doorsijpelt: een advertentie die bij een collectie hoort, of die een verzendoptie gebruikt, verwijst er expliciet naar met een `a`-tag in plaats van de instellingen van de ouder automatisch te erven. Dat is een bewuste afwijking van het oudere [NIP-15](/nl/topics/nip-15/)-kraammodel, waar een product stilzwijgend de valuta en verzendtabel van zijn kraam erfde.

### Voorbeeld: aanmaken van een bestelling (kind 16, type 1)

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

## Waarom het van belang is

NIP-99 alleen standaardiseert enkel de advertentie zelf, een ondertekende, adresseerbare advertentie. Voor Gamma Markets vond elke client die echte e-commerce op NIP-99 bouwde zijn eigen privéconventies uit voor verzending, afrekenen en recensies, wat betekende dat twee NIP-99-conforme clients elk een advertentie correct konden weergeven maar geen gedeelde manier hadden om samen een bestelling af te ronden. Gamma Markets dicht dat gat zonder het NIP-99-advertentieformaat zelf aan te raken, zodat bestaande NIP-99-advertenties zonder aanpassing geldig blijven.

## Implementaties

- [Shopstr](https://github.com/shopstr-eng/shopstr) - Nostr-marktplaats, een van de vier projecten die de specificatie schreven
- [Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) - marktplaatsprotocol dat zijn eigen bestelstatus- en afrekenstroom bouwt in dezelfde ontwerpruimte

---

**Primaire bronnen:**
- [Gamma Markets-specificatierepository](https://github.com/GammaMarkets/market-spec)
- [NIP-99 e-commerce use case-uitbreiding, PR #1784](https://github.com/nostr-protocol/nips/pull/1784) - samengevoegde link van het canonieke NIP-99-document naar de Gamma Markets-specificatie

**Genoemd in:**
- [Newsletter #31: NIP Deep Dive: NIP-99 en de Gamma Markets-handelsuitbreiding](/nl/newsletters/2026-07-15-newsletter/#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension)

**Zie ook:**
- [NIP-99: Classified Listings](/nl/topics/nip-99/)
- [NIP-15: Nostr Marketplace](/nl/topics/nip-15/)
- [NIP-17: Private Direct Messages](/nl/topics/nip-17/)
