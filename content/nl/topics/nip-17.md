---
title: "NIP-17: Privé Directe Berichten"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Berichten
---

NIP-17 definieert privé directe berichten met NIP-59 gift wrapping voor afzenderprivacy. In tegenstelling tot NIP-04 DMs die de afzender blootstellen, verbergen NIP-17 berichten wie het bericht heeft verzonden. De ontvanger blijft zichtbaar in de buitenste gift wrap.

## Hoe Het Werkt

Berichten worden verpakt in meerdere encryptielagen:
1. De daadwerkelijke berichtinhoud (kind 14)
2. Een seal die de inhoud versleutelt naar de ontvanger
3. Een gift wrap die de identiteit van de afzender verbergt

De buitenste gift wrap gebruikt een willekeurig, wegwerp sleutelpaar zodat relays en waarnemers niet kunnen bepalen wie het bericht heeft verzonden.

## Berichtstructuur

- **Kind 14** - De daadwerkelijke DM-inhoud (binnen de seal)
- Gebruikt NIP-44 encryptie voor de inhoud
- Ondersteunt reacties (kind 7) binnen DM-gesprekken

## Privacygaranties

- Relays kunnen de afzender niet zien (verborgen door het wegwerp sleutelpaar van de gift wrap)
- Ontvanger is zichtbaar (in de `p` tag van de gift wrap)
- Berichttijdstempels zijn gerandomiseerd binnen een venster
- Geen zichtbare threading of gespreksgroepering op de relay

## Vergelijking met NIP-04

NIP-04 DMs versleutelen inhoud maar laten metadata zichtbaar:
- Afzender pubkey is openbaar
- Ontvanger pubkey is in de `p` tag
- Tijdstempels zijn exact

NIP-17 verbergt de afzender ten koste van complexere implementatie.

---

**Primaire bronnen:**
- [NIP-17 Specificatie](https://github.com/nostr-protocol/nips/blob/master/17.md)

**Vermeld in:**
- [Nieuwsbrief #1: NIP Updates](/nl/newsletters/2025-12-17-newsletter/#nip-updates)
- [Nieuwsbrief #2: Nieuws](/nl/newsletters/2025-12-24-newsletter/#news)

**Zie ook:**
- [NIP-59: Gift Wrap](/nl/topics/nip-59/)
