---
title: "NIP-10: Tekstnota Threading"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Sociaal
---

NIP-10 specificeert hoe kind 1 nota's naar elkaar verwijzen om reply-threads te vormen. Dit begrijpen is essentieel voor het bouwen van gespreksweergaven.

## Het Probleem

Wanneer iemand reageert op een nota, moeten clients weten: Waarop is dit een reactie? Wat is de root van het gesprek? Wie moet genotificeerd worden? NIP-10 beantwoordt deze vragen via `e` tags (event-referenties) en `p` tags (pubkey-vermeldingen).

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
  "content": "Goed punt! Ik ben het ermee eens.",
  "sig": "b7d3f..."
}
```

De `root` marker wijst naar de originele nota die de thread startte. De `reply` marker wijst naar de specifieke nota die wordt beantwoord. Als je direct reageert op de root, gebruik alleen `root` (geen `reply` tag nodig). Het onderscheid is belangrijk voor rendering: de `reply` bepaalt inspringing in een threadweergave, terwijl `root` alle replies groepeert.

## Threading-regels

- **Directe reply naar root:** Eén `e` tag met `root` marker
- **Reply op een reply:** Twee `e` tags, één `root` en één `reply`
- De `root` blijft constant door de thread; `reply` verandert op basis van waarop je reageert

## Pubkey Tags voor Notificaties

Neem `p` tags op voor iedereen die genotificeerd moet worden. Minimaal, tag de auteur van de nota waarop je reageert. Conventie is om ook alle `p` tags van het parent-event op te nemen (zodat iedereen in het gesprek op de hoogte blijft), plus alle gebruikers die je @vermeldt in je content.

## Relay-hints

De derde positie in `e` en `p` tags kan een relay URL bevatten waar dat event of de content van die gebruiker gevonden kan worden. Dit helpt clients de gerefereerde content op te halen zelfs als ze niet verbonden zijn met de originele relay.

## Verouderde Positionele Tags

Vroege Nostr-implementaties leidden betekenis af uit tagpositie in plaats van markers: eerste `e` tag was root, laatste was reply, middelste waren vermeldingen. Deze aanpak is verouderd omdat het ambiguïteit creëert. Als je `e` tags ziet zonder markers, zijn ze waarschijnlijk van oudere clients. Moderne implementaties moeten altijd expliciete markers gebruiken.

## Threadweergaven Bouwen

Om een thread weer te geven, haal het root-event op, vraag dan alle events op met een `e` tag die naar die root verwijst:

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

Sorteer resultaten op `created_at` en gebruik `reply` markers om de boomstructuur te bouwen. Events waarvan de `reply` naar de root wijst zijn top-level replies; events waarvan de `reply` naar een andere reply wijst zijn geneste antwoorden.

---

**Primaire bronnen:**
- [NIP-10 Specificatie](https://github.com/nostr-protocol/nips/blob/master/10.md)

**Vermeld in:**
- [Nieuwsbrief #2: NIP Diepgaand](/nl/newsletters/2025-12-24-newsletter/#nip-10-tekstnota-threading)

**Zie ook:**
- [NIP-01: Basisprotocol](/nl/topics/nip-01/)
