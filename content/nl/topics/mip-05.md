---
title: "MIP-05: Privacybehoudende pushnotificaties"
date: 2025-12-17
translationDate: 2026-03-07
translationOf: /en/topics/mip-05.md
draft: false
categories:
  - Privacy
  - Berichten
  - Protocol
---

MIP-05 definieert een pushnotificatieprotocol voor Marmot-clients dat privacy probeert te behouden in een omgeving waarin gewone mobiele pushsystemen meestal apparaattokens en accountrelaties blootleggen.

## Hoe het werkt

- Apparaattokens worden versleuteld met ECDH+HKDF en ChaCha20-Poly1305
- Ephemeral keys voorkomen correlatie tussen notificaties
- Een gossip-protocol met drie events (kinds 447-449) synchroniseert versleutelde tokens tussen groepsleden
- Decoy tokens via NIP-59 gift wrapping verhullen groepsgroottes

## Privacymodel

- Pushnotificatieservers kunnen gebruikers niet identificeren
- Groepslidmaatschap wordt niet onthuld door notificatiepatronen
- Apparaattokens kunnen niet over berichten heen worden gecorreleerd

De concrete verbetering is dat de pushprovider ondoorzichtige delivery tokens ziet, geen directe koppeling van groepslid aan apparaat. Dat maakt notificaties niet in absolute zin anoniem, maar het beperkt wel hoeveel de pushlaag standaard te weten komt.

## Event-kinds

- **Kind 447**: Publicatie van versleuteld apparaattoken
- **Kind 448**: Verzoek om tokensynchronisatie
- **Kind 449**: Antwoord op tokensynchronisatie

## Afwegingen

MIP-05 voegt privacy toe door extra coördinatiewerk toe te voegen. Clients moeten versleutelde tokenstatus tussen groepsleden synchroniseren, en decoy tokens vergroten bewust de overhead van berichten.

Dat betekent dat implementers een balans moeten vinden tussen afleverbetrouwbaarheid en metadatabescherming. Het protocol is juist nuttig omdat het push behandelt als een privacyprobleem, niet alleen als transportgemak.

---

**Primaire bronnen:**
- [MIP-05-specificatie](https://github.com/marmot-protocol/marmot/blob/master/05.md)
- [MIP-05-PR](https://github.com/marmot-protocol/marmot/pull/18)
- [White Noise v0.2.1-release](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**Vermeld in:**
- [Nieuwsbrief #1: Nieuws](/en/newsletters/2025-12-17-newsletter/#news)
- [Nieuwsbrief #3: Decemberoverzicht](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Zie ook:**
- [Marmot Protocol](/nl/topics/marmot/)
- [NIP-59: Gift Wrap](/nl/topics/nip-59/)
