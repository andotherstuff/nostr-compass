---
title: "NIP-72: Moderated Communities"
date: 2026-03-25
translationOf: /en/topics/nip-72.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Communities
---

NIP-72 definieert gemodereerde gemeenschappen op Nostr. Gemeenschappen bieden een manier om berichten te organiseren rond een gedeeld onderwerp of groep, met moderatoren die inhoud goedkeuren voordat deze zichtbaar wordt voor leden.

## Hoe Het Werkt

Een gemeenschap wordt gedefinieerd door een kind 34550 event gepubliceerd door de maker. Dit event bevat de gemeenschapsnaam, beschrijving, regels en een lijst van moderator-pubkeys. Het event gebruikt een replaceable event-formaat (kind 30000-39999 bereik), zodat de gemeenschapsdefinitie in de loop der tijd kan worden bijgewerkt.

```json
{
  "kind": 34550,
  "tags": [
    ["d", "example-community"],
    ["name", "Example Community"],
    ["description", "A community for discussing examples"],
    ["p", "<moderator_pubkey>", "", "moderator"],
    ["relay", "wss://relay.example.com", "moderator"]
  ],
  "content": "",
  "pubkey": "<creator_pubkey>",
  "created_at": 1742860800,
  "sig": "<signature>"
}
```

Gebruikers dienen berichten in bij een gemeenschap door hun events te taggen met een `a` tag die verwijst naar de gemeenschapsdefinitie. Deze berichten zijn nog niet zichtbaar voor gemeenschapslezers. Een moderator beoordeelt de inzending en publiceert, indien goedgekeurd, een kind 4549 goedkeuringsevent dat het oorspronkelijke bericht omhult. Clients die de gemeenschap weergeven tonen alleen berichten die een bijbehorend goedkeuringsevent hebben van een erkende moderator.

Dit goedkeuringsmodel betekent dat gemeenschappen leesgefilterd zijn, niet schrijfbeperkt. Iedereen kan een bericht indienen, maar alleen goedgekeurde berichten verschijnen in de gemeenschapsfeed. Moderatoren fungeren als curatoren in plaats van poortwachters van de onderliggende data.

## Overwegingen

Omdat goedkeuringsevents afzonderlijke Nostr-events zijn, zijn moderatiebeslissingen transparant en controleerbaar. Een bericht dat door de ene gemeenschap wordt afgewezen, kan nog steeds door een andere worden goedgekeurd. Dezelfde inhoud kan in meerdere gemeenschappen bestaan met onafhankelijke moderatie.

Relay-ondersteuning is belangrijk voor gemeenschapsfunctionaliteit. Clients moeten zowel de gemeenschapsdefinitie als goedkeuringsevents opvragen, wat relays vereist die deze event kinds efficiënt indexeren.

---

**Primaire bronnen:**
- [NIP-72 Specificatie](https://github.com/nostr-protocol/nips/blob/master/72.md) - Moderated Communities

**Vermeld in:**
- [Newsletter #15](/nl/newsletters/2026-03-25-newsletter/)
