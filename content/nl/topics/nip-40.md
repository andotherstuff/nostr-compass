---
title: "NIP-40: Verlooptijdstempel"
date: 2025-12-17
translationDate: 2026-03-07
translationOf: /en/topics/nip-40.md
draft: false
categories:
  - Protocol
---

NIP-40 definieert een `expiration`-tag die relays vertelt wanneer een event moet worden verwijderd.

## Hoe het werkt

Events bevatten een `expiration`-tag met een Unix-tijdstempel:

```json
["expiration", "1734567890"]
```

Na dit tijdstip moeten relays het event verwijderen en weigeren het nog te serveren.

## Waarom het belangrijk is

- Ephemeral content die na een vaste tijd moet verdwijnen
- Tijdgebonden aanbiedingen of aankondigingen
- Verloop van vermeldingen in marktplaatsen, zoals Shopstr
- Het verlagen van relay-opslagvereisten

Expiration is een bewaarrichtlijn, geen herroepingssysteem. Het helpt relaygedrag rond verouderde content op elkaar af te stemmen, maar het garandeert geen verwijdering zodra een andere relay, client of archief het event al heeft gekopieerd.

## Vertrouwens- en beveiligingsnotities

- Relays zijn niet verplicht expiration te respecteren, al doen de meeste dat wel
- Clients moeten niet vertrouwen op expiration voor het verwijderen van beveiligingskritieke content
- Zodra content door een andere client is opgehaald, kan die worden gecachet of opnieuw gepubliceerd
- Expiration verbergt niet dat een event heeft bestaan. Event ids, citaten of kopieën buiten relays kunnen nog steeds blijven bestaan nadat het tijdstip is verstreken

---

**Primaire bronnen:**
- [NIP-40 Specificatie](https://github.com/nostr-protocol/nips/blob/master/40.md)

**Vermeld in:**
- [Nieuwsbrief #1: Nieuws](/en/newsletters/2025-12-17-newsletter/)
- [Nieuwsbrief #3: Opmerkelijke codewijzigingen](/en/newsletters/2025-12-31-newsletter/)

**Zie ook:**
- [NIP-01: Basisprotocol](/nl/topics/nip-01/)
