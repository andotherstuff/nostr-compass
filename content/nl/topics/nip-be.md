---
title: "NIP-BE: Bluetooth Low Energy"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Connectiviteit
---

NIP-BE specificeert hoe Nostr-applicaties via Bluetooth Low Energy kunnen communiceren en synchroniseren, zodat offline-capabele apps gegevens kunnen synchroniseren tussen apparaten in elkaars buurt zonder internetverbinding.

## Hoe het werkt

NIP-BE hergebruikt gewone Nostr-berichtframes over BLE in plaats van een apart eventmodel te bedenken. Apparaten adverteren een BLE-service plus een apparaat-UUID, vergelijken UUID's wanneer ze elkaar tegenkomen, en bepalen dan op deterministische wijze welke kant de GATT-server wordt en welke kant de GATT-client.

De GATT-service gebruikt een Nordic UART-achtige vorm met één write characteristic en één read/notify characteristic. Dat houdt het transport eenvoudig genoeg voor beperkte mobiele stacks, terwijl het nog steeds gewone Nostr-berichten kan dragen.

## Berichtframing

BLE heeft kleine payloadlimieten, dus NIP-BE comprimeert berichten met DEFLATE, splitst ze op in geïndexeerde chunks en verstuurt slechts één bericht tegelijk. De specificatie beperkt berichten tot 64 KB, wat een nuttige herinnering is dat dit transport bedoeld is voor synchronisatie en lokale verspreiding, niet voor bulkoverdracht.

## Synchronisatiemodel

Nadat een verbinding tot stand is gebracht, gebruiken peers een half-duplex syncstroom op basis van [NIP-77](https://github.com/nostr-protocol/nips/blob/master/77.md) negentropy-berichten zoals `NEG-OPEN`, `NEG-MSG`, `EVENT` en `EOSE`. Die ontwerpkeuze is belangrijk, omdat implementaties zo bestaande relay-synclogica kunnen hergebruiken in plaats van een BLE-specifiek replicatie-algoritme te bouwen.

De half-duplexregel sluit ook aan op de realiteit van instabiele BLE-verbindingen. Onderbroken short-range verbindingen werken beter wanneer elke kant precies weet wie aan de beurt is om te spreken.

## Waarom het belangrijk is

NIP-BE geeft Nostr-applicaties een pad naar local-first networking. Twee telefoons kunnen notities of relaystatus direct synchroniseren wanneer ze dicht bij elkaar zijn, zelfs als geen van beide een werkende internetverbinding heeft. Dat maakt BLE nuttig voor censuurbestendigheid, rampsituaties en sociale apps met beperkte connectiviteit.

De beperkingen zijn net zo belangrijk: BLE-bandbreedte is laag, verbindingen zijn kortstondig en grote geschiedenissen passen niet goed. In de praktijk is NIP-BE het meest geschikt voor incrementele synchronisatie en verspreiding van berichten in de buurt, niet voor volledige archiefreplicatie.

---

**Primaire bronnen:**
- [NIP-BE-specificatie](https://github.com/nostr-protocol/nips/blob/master/BE.md)
- [PR #1979](https://github.com/nostr-protocol/nips/pull/1979)

**Vermeld in:**
- [Nieuwsbrief #1: Nieuws](/en/newsletters/2025-12-17-newsletter/#news)
- [Nieuwsbrief #3: Decemberoverzicht](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Zie ook:**
- [NIP-01: Basic Protocol](/nl/topics/nip-01/)
