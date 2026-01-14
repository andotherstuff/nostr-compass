---
title: "NIP-62: Vanish Requests"
date: 2026-01-13
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-62 definieert vanish requests, een mechanisme waarmee gebruikers kunnen verzoeken dat relays hun content verwijderen. Hoewel relays niet verplicht zijn deze verzoeken te honoreren, geeft ondersteuning voor NIP-62 gebruikers meer controle over hun gepubliceerde data en biedt het een gestandaardiseerde manier om verwijderingsintentie over het netwerk te signaleren.

## Hoe Het Werkt

Een vanish request is een kind 62 event ondertekend door de gebruiker die zijn content verwijderd wil hebben. Het verzoek kan specifieke events targeten door hun ID's op te nemen in `e` tags, of het kan verwijdering van alle content van die pubkey verzoeken door de `e` tags weg te laten.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 62,
  "tags": [
    ["e", "event1234...", "wss://relay.example.com"],
    ["e", "event5678...", "wss://relay.example.com"]
  ],
  "content": "Removing old posts",
  "sig": "sig1234..."
}
```

Het `content` veld bevat optioneel een leesbare reden voor het verwijderingsverzoek. Relay hints in de `e` tags vertellen relays waar de originele events werden gepubliceerd, hoewel relays verzoeken kunnen honoreren ongeacht of ze de gespecificeerde events hebben.

## Relay Gedrag

Relays die NIP-62 ondersteunen moeten de gespecificeerde events uit hun opslag verwijderen en stoppen met ze te serveren aan subscribers. Het vanish request zelf kan worden behouden als bewijs dat verwijdering werd verzocht, wat helpt voorkomen dat verwijderde events opnieuw worden geïmporteerd van andere relays.

Wanneer een vanish request alle `e` tags weglaat, interpreteren relays dit als een verzoek om alle events van die pubkey te verwijderen. Dit is een drastischere actie en relays kunnen dit anders afhandelen, bijvoorbeeld door de pubkey als "vanished" te markeren en te weigeren om zijn events te accepteren of serveren.

Relays zijn niet verplicht NIP-62 te ondersteunen. Het Nostr netwerk is gedecentraliseerd, en elke relay-operator bepaalt zijn eigen dataretentiebeleid. Gebruikers moeten niet aannemen dat hun content overal wordt verwijderd simpelweg omdat ze een vanish request hebben gepubliceerd.

## Privacyoverwegingen

Vanish requests zijn een best-effort verwijderingsmechanisme, geen garantie van privacy. Zelfs na het publiceren van een vanish request kunnen kopieen van de content elders in het netwerk bestaan, waaronder op andere relays die NIP-62 niet ondersteunen, in lokale caches op clientapparaten, in archieven of zoekmachines van derden, en in backups.

Het verzoek zelf is ook een ondertekend Nostr event, wat betekent dat het deel wordt van je publieke record. Iedereen die het vanish request ziet weet dat je iets hebt verwijderd, zelfs als ze niet kunnen zien wat er werd verwijderd.

Voor content die privé moet blijven, overweeg versleutelde berichten te gebruiken zoals [NIP-17](/nl/topics/nip-17/) in plaats van te vertrouwen op verwijdering achteraf.

---

**Primaire bronnen:**
- [NIP-62 Specificatie](https://github.com/nostr-protocol/nips/blob/master/62.md)

**Vermeld in:**
- [Nieuwsbrief #5: Opmerkelijke Codewijzigingen](/nl/newsletters/2026-01-13-newsletter/#rust-nostr-library)
