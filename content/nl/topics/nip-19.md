---
title: "NIP-19: Bech32-gecodeerde Entiteiten"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identiteit
---

NIP-19 definieert mensvriendelijke formaten voor het delen van Nostr-identifiers. Deze bech32-gecodeerde strings worden gebruikt voor weergave en delen maar worden nooit in het protocol zelf gebruikt (dat gebruikt hex).

## Waarom Bech32?

Ruwe hex-sleutels zijn foutgevoelig om te kopiëren en visueel niet te onderscheiden. Bech32-codering voegt een leesbaar voorvoegsel en checksum toe, waardoor het onmiddellijk duidelijk is naar welk type data je kijkt.

## Basisformaten

Deze coderen ruwe 32-byte waarden:

- **npub** - Publieke sleutel (je identiteit, veilig om te delen)
- **nsec** - Privésleutel (houd geheim, gebruikt voor ondertekenen)
- **note** - Event-ID (verwijst naar een specifiek event)

Voorbeeld: De hex-pubkey `3bf0c63f...` wordt `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

## Deelbare Identifiers

Deze gebruiken TLV (Type-Length-Value) codering om metadata op te nemen:

- **nprofile** - Profiel met relay-hints (helpt clients de gebruiker te vinden)
- **nevent** - Event met relay-hints, auteur-pubkey en kind
- **naddr** - Adresseerbare event-referentie (pubkey + kind + d-tag + relays)

Deze lossen het ontdekkingsprobleem op: wanneer iemand een note-ID deelt, hoe weten clients welke relay het heeft? Door relay-hints in de identifier te bundelen, worden gedeelde links betrouwbaarder.

## Implementatienotities

- Gebruik bech32 alleen voor menselijke interfaces: weergave, kopiëren/plakken, QR-codes, URL's
- Gebruik nooit bech32-formaten in protocolberichten, events of NIP-05 antwoorden
- Alle protocolcommunicatie moet hex-codering gebruiken
- Bij het genereren van nevent/nprofile/naddr, neem relay-hints op voor betere vindbaarheid

---

**Primaire bronnen:**
- [NIP-19 Specificatie](https://github.com/nostr-protocol/nips/blob/master/19.md)

**Vermeld in:**
- [Nieuwsbrief #1: NIP Diepgaand](/nl/newsletters/2025-12-17-newsletter/#nip-19-bech32-gecodeerde-identifiers)

**Zie ook:**
- [NIP-01: Basisprotocol](/nl/topics/nip-01/)
- [NIP-21: nostr: URI Schema](https://github.com/nostr-protocol/nips/blob/master/21.md)
