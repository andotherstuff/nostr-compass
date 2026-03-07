---
title: "NIP-10: Tekstnotitie-threading"
date: 2025-12-24
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Sociaal
---

NIP-10 specificeert hoe kind 1-notities naar elkaar verwijzen om reply-threads te vormen. Dit begrijpen is essentieel voor het bouwen van gespreksweergaven.

## Hoe Het Werkt

Wanneer iemand op een notitie reageert, moeten clients weten: Waarop is dit een reactie? Wat is de root van het gesprek? Wie moet een melding krijgen? NIP-10 beantwoordt deze vragen met `e` tags (eventverwijzingen) en `p` tags (pubkey-vermeldingen).

## Gemarkeerde Tags (Voorkeur)

Moderne clients gebruiken expliciete markers in `e` tags:

```json
{
  "id": "f9c2e...",
  "pubkey": "a3b9c...",
  "created_at": 1734912345,
  "kind": 1,
  "tags": [
    ["e", "abc123...", "wss://relay.example.com", "root"],
    ["e", "def456...", "wss://relay.example.com", "reply"],
    ["p", "91cf9..."],
    ["p", "14aeb..."]
  ],
  "content": "Great point! I agree.",
  "sig": "b7d3f..."
}
```

De `root` marker wijst naar de oorspronkelijke notitie die de thread begon. De `reply` marker wijst naar de specifieke notitie waarop wordt gereageerd. Als je direct op de root reageert, gebruik je alleen `root` en is geen `reply` tag nodig. Dat onderscheid is belangrijk voor rendering: `reply` bepaalt de inspringing in een threadweergave, terwijl `root` alle reacties bij elkaar houdt.

## Threading-regels

- **Directe reactie op de root:** Een `e` tag met de `root` marker
- **Reactie op een reactie:** Twee `e` tags, een `root` en een `reply`
- De `root` blijft in de hele thread gelijk; `reply` verandert afhankelijk van waar je op reageert

## Meldingen en Vermeldingen

Neem `p` tags op voor iedereen die een melding moet krijgen. Tag minimaal de auteur van de notitie waarop je reageert. De conventie is om ook alle `p` tags uit het parent-event over te nemen, zodat iedereen in het gesprek op de hoogte blijft, plus alle gebruikers die je met @ noemt in je content.

## Relay-hints

De derde positie in `e` en `p` tags kan een relay-URL bevatten waar dat event of de content van die gebruiker mogelijk te vinden is. Dit helpt clients om de genoemde content op te halen, zelfs als ze niet met de oorspronkelijke relay verbonden zijn.

## Interop-opmerkingen

Vroege Nostr-implementaties leidden betekenis af uit de tagpositie in plaats van uit markers: de eerste `e` tag was de root, de laatste was de reply en de middelste waren vermeldingen. Deze aanpak is verouderd omdat hij ambiguiteit veroorzaakt. Als je `e` tags zonder markers ziet, komen die waarschijnlijk van oudere clients. Moderne implementaties moeten altijd expliciete markers gebruiken.

Clients moeten nog steeds beide vormen kunnen parsen als ze oudere threads correct willen weergeven. In de praktijk is NIP-10-interoperabiliteit deels een migratieprobleem: producers moeten gemarkeerde tags uitsturen, maar readers moeten oudere positionele vormen blijven accepteren.

## Threadweergaven Bouwen

Om een thread weer te geven, haal je eerst het root-event op en vraag je daarna alle events op met een `e` tag die naar die root verwijst:

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

Sorteer de resultaten op `created_at` en gebruik `reply` markers om de boomstructuur op te bouwen. Events waarvan `reply` naar de root wijst, zijn reacties op het hoogste niveau; events waarvan `reply` naar een andere reactie wijst, zijn geneste antwoorden.

---

**Primaire bronnen:**
- [NIP-10-specificatie](https://github.com/nostr-protocol/nips/blob/master/10.md)

**Vermeld in:**
- [Nieuwsbrief #2: NIP Deep Dive](/nl/newsletters/2025-12-24-newsletter/#nip-10-tekstnotitie-threading)

**Zie ook:**
- [NIP-01: Basic Protocol](/nl/topics/nip-01/)
- [NIP-18: Reposts](/nl/topics/nip-18/)
