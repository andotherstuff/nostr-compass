---
title: "NIP-02: Volglijst"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Sociaal
---

NIP-02 definieert kind 3 events, die je volglijst opslaan. Dit eenvoudige mechanisme voedt de sociale graaf die tijdlijnen mogelijk maakt.

## Structuur

Een kind 3 event bevat `p` tags die gevolgde pubkeys opsommen:

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

Elke `p` tag heeft vier posities: de tagnaam, de gevolgde pubkey (hex), een optionele relay URL-hint, en een optionele "petname" (een lokale bijnaam). De relay-hint vertelt andere clients waar ze de events van die gebruiker kunnen vinden. De petname laat je gedenkwaardige namen toewijzen aan contacten zonder te vertrouwen op hun zelf-gedeclareerde weergavenamen.

## Vervangbaar Gedrag

Kind 3 valt in het vervangbare bereik (0, 3, 10000-19999), dus relays houden alleen de laatste versie per pubkey bij. Wanneer je iemand nieuws volgt, publiceert je client een volledig nieuw kind 3 dat al je volgers bevat plus de nieuwe. Dit betekent dat volglijsten elke keer compleet moeten zijn; je kunt geen incrementele updates publiceren.

## Tijdlijnen Bouwen

Om een home-feed te construeren, haalt de client het kind 3 van de gebruiker op, extraheert alle `p` tag pubkeys, en abonneert zich dan op kind 1 events van die auteurs:

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

De relay retourneert overeenkomende nota's en de client rendert ze. De relay-hints in kind 3 helpen clients te weten welke relays te bevragen voor elke gevolgde gebruiker.

## Petnames en Identiteit

Het petname-veld maakt een gedecentraliseerd naamgevingsschema mogelijk. In plaats van te vertrouwen op welke naam een gebruiker ook claimt in hun profiel, kun je je eigen label toewijzen. Een client zou kunnen weergeven "alice (Mijn Zus)" waar "alice" komt van haar kind 0 profiel en "Mijn Zus" is je petname. Dit biedt context die globale gebruikersnamen niet kunnen bieden.

## Praktische Overwegingen

Omdat kind 3 events vervangbaar zijn en compleet moeten zijn, moeten clients onbekende tags behouden bij het updaten. Als een andere client tags heeft toegevoegd die jouw client niet begrijpt, zou blind overschrijven die data verliezen. Voeg nieuwe volgers toe in plaats van helemaal opnieuw te bouwen.

---

**Primaire bronnen:**
- [NIP-02 Specificatie](https://github.com/nostr-protocol/nips/blob/master/02.md)

**Vermeld in:**
- [Nieuwsbrief #2: NIP Diepgaand](/nl/newsletters/2025-12-24-newsletter/#nip-02-follow-list)

**Zie ook:**
- [NIP-01: Basisprotocol](/nl/topics/nip-01/)
