---
title: "NIP-BE: Bluetooth Low Energy"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Connectiviteit
---

NIP-BE specificeert hoe Nostr-applicaties kunnen communiceren en synchroniseren via Bluetooth Low Energy, waardoor offline-capabele apps data kunnen synchroniseren tussen apparaten in de buurt zonder internetverbinding.

## GATT Structuur

Gebruikt een Nordic UART Service met twee karakteristieken:
- **Write characteristic** - Client stuurt data naar server
- **Read characteristic** - Server stuurt data naar client (via notificaties)

## Berichtframing

BLE heeft kleine payload-limieten (20-256 bytes afhankelijk van versie), dus berichten worden:
- Gecomprimeerd met DEFLATE
- Opgesplitst in chunks met een 2-byte index en final-batch vlag
- Beperkt tot maximaal 64KB

## Rolonderhandeling

Apparaten vergelijken geadverteerde UUID's bij ontdekking:
- Hogere UUID wordt GATT-server (relay-rol)
- Lagere UUID wordt GATT-client
- Vooraf bepaalde UUID's bestaan voor single-role apparaten

## Synchronisatie

Gebruikt half-duplex communicatie met standaard Nostr-berichttypes (`EVENT`, `EOSE`, `NEG-MSG`) om datasync te coördineren over intermitterende verbindingen.

## Gebruiksscenario's

- Offline event-synchronisatie tussen apparaten in de buurt
- Mesh-stijl berichtpropagatie zonder internet
- Backup-connectiviteit wanneer netwerk niet beschikbaar is

---

**Primaire bronnen:**
- [NIP-BE Specificatie](https://github.com/nostr-protocol/nips/blob/master/BE.md)

**Vermeld in:**
- [Nieuwsbrief #1: Nieuws](/nl/newsletters/2025-12-17-newsletter/#news)
