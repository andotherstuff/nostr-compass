---
title: "NIP-62: Vanish Requests"
date: 2026-01-13
translationDate: 2026-03-07
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-62 definieert vanish requests, een mechanisme waarmee gebruikers relays kunnen verzoeken hun content te verwijderen. Relays zijn niet verplicht die verzoeken te honoreren, maar ondersteuning voor NIP-62 geeft gebruikers meer controle over hun gepubliceerde data en biedt een gestandaardiseerde manier om verwijderingsintentie over het netwerk te signaleren.

## Hoe Het Werkt

Een vanish request is een kind 62 event dat is ondertekend door de gebruiker die zijn content verwijderd wil hebben. Het verzoek kan specifieke events targeten door hun ID's op te nemen in `e` tags, of het kan verwijdering van alle content van die pubkey verzoeken door de `e` tags helemaal weg te laten.

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

Het veld `content` bevat optioneel een leesbare reden voor het verwijderingsverzoek. Relay hints in de `e` tags laten relays zien waar de oorspronkelijke events zijn gepubliceerd, al kunnen relays verzoeken honoreren ongeacht of ze de opgegeven events hebben.

## Relaygedrag

Relays die NIP-62 ondersteunen, zouden de opgegeven events uit hun opslag moeten verwijderen en ze niet langer aan subscribers moeten serveren. Het vanish request zelf kan bewaard blijven als registratie dat verwijdering is verzocht, wat helpt voorkomen dat verwijderde events opnieuw van andere relays worden geïmporteerd.

Wanneer een vanish request alle `e` tags weglaat, interpreteren relays dit als een verzoek om alle events van die pubkey te verwijderen. Dit is een ingrijpendere actie en relays kunnen daar anders mee omgaan, bijvoorbeeld door de pubkey als "vanished" te markeren en voortaan geen events van die pubkey meer te accepteren of te serveren.

Relays zijn niet verplicht NIP-62 te ondersteunen. Het Nostr-netwerk is gedecentraliseerd en elke relay-operator bepaalt zijn eigen beleid voor databehoud. Gebruikers moeten er niet van uitgaan dat hun content overal wordt verwijderd alleen omdat ze een vanish request hebben gepubliceerd.

## Waarom Het Belangrijk Is

NIP-62 geeft clients en relay-operators een gedeeld verwijderingssignaal dat verder gaat dan ad-hoc moderatie-API's of relay-specifieke dashboards. Een gebruiker kan een enkel ondertekend verzoek publiceren en vervolgens elke relay zelf laten beslissen hoe die het verwerkt.

De praktische grens is reikwijdte. Een vanish request heeft alleen effect op relays die het zien, het ondersteunen en ervoor kiezen het te honoreren. Het trekt geen screenshots, lokale databases, archieven van derden of opnieuw gepubliceerde kopieën terug die al buiten de controle van de relay vallen.

## Privacyoverwegingen

Vanish requests zijn een best-effort mechanisme voor verwijdering, geen garantie op privacy. Zelfs na het publiceren van een vanish request kunnen kopieën van de content elders in het netwerk blijven bestaan, onder meer op andere relays die NIP-62 niet ondersteunen, in lokale caches op clientapparaten, in archieven of zoekmachines van derden en in back-ups.

Het verzoek zelf is ook een ondertekend Nostr event, wat betekent dat het deel wordt van je publieke record. Iedereen die het vanish request ziet, weet dat je iets hebt verwijderd, ook als ze niet kunnen zien wat er is verwijderd.

Voor content die privé moet blijven, kun je beter encrypted messaging zoals [NIP-17](/nl/topics/nip-17/) gebruiken dan vertrouwen op verwijdering achteraf.

## Interop-opmerkingen

NIP-62 vult [NIP-09](/nl/topics/nip-09/) aan. NIP-09 is het algemene event voor verwijderingsverzoeken dat overal in Nostr wordt gebruikt, terwijl NIP-62 relays een sterker, op vanish gericht signaal geeft dat specifieke events of de volledige contentset van een pubkey kan omvatten. Implementaties kunnen beide ondersteunen, en de database backends van rust-nostr bieden nu configuratie rond die grens van handhaving.

---

**Primaire bronnen:**
- [NIP-62 Specification](https://github.com/nostr-protocol/nips/blob/master/62.md)

**Vermeld in:**
- [Nieuwsbrief #5: Opmerkelijke codewijzigingen](/en/newsletters/2026-01-13-newsletter/#rust-nostr-library)
- [Nieuwsbrief #10: rust-nostr](/en/newsletters/2026-03-04-newsletter/#rust-nostr-nip-62-request-to-vanish)

**Zie ook:**
- [NIP-09: Event Deletion Request](/nl/topics/nip-09/)
- [NIP-17: Private Direct Messages](/nl/topics/nip-17/)
