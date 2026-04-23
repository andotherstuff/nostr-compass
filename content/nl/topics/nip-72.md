---
title: "NIP-72: Moderated Communities"
date: 2026-03-25
translationOf: /en/topics/nip-72.md
translationDate: 2026-04-22
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

Vergeleken met [NIP-29](/nl/topics/nip-29/) relay-based groups, waar de relay de autoriteit is voor zowel lidmaatschap als moderatie, leeft NIP-72 in gewone Nostr-events. Elke relay die kinds `34550`, `4549` en de submission kinds draagt kan een gemeenschap bedienen, en moderatie is zichtbaar en forkable. De tradeoff is dat niet-goedgekeurde submissions alleen op de client-renderlaag verborgen worden, dus NIP-29 blijft geschikter wanneer spam volledig van de wire moet blijven.

## Implementaties

- [noStrudel](https://github.com/hzrd149/nostrudel) heeft al langer NIP-72 community-ondersteuning, inclusief een pending submission queue voor moderatoren.
- [Amethyst](https://github.com/vitorpamplona/amethyst) voegde first-class creation en management van communities toe in [PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468): het authoren van de kind `34550` community definition, het toevoegen van moderatoren en relay hints, het indienen van posts met een `a`-tag en het beheren van pending approvals via kind `4549`-events.

---

**Primaire bronnen:**
- [NIP-72 Specificatie](https://github.com/nostr-protocol/nips/blob/master/72.md) - Moderated Communities
- [Amethyst PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) - NIP-72 community creation and moderation

**Vermeld in:**
- [Newsletter #15](/nl/newsletters/2026-03-25-newsletter/)
- [Newsletter #19: Amethyst community support](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NIP Deep Dive](/en/newsletters/2026-04-22-newsletter/)

**Zie ook:**
- [NIP-29: Relay-based Groups](/nl/topics/nip-29/)
