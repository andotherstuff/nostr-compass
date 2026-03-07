---
title: "NIP-19: Bech32-gecodeerde Entiteiten"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Identiteit
---

NIP-19 definieert mensvriendelijke formaten voor het delen van Nostr-identifiers. Deze bech32-gecodeerde strings worden gebruikt voor weergave en delen, maar worden nooit in het protocol zelf gebruikt, dat hex gebruikt.

## Hoe het werkt

Ruwe hex-sleutels zijn foutgevoelig om te kopieren en visueel nauwelijks van elkaar te onderscheiden. Bech32-encodering voegt een leesbaar voorvoegsel en een checksum toe, zodat het duidelijk is naar welk type gegevens je kijkt en veel kopieerfouten worden opgevangen.

De basisvormen coderen een enkele 32-byte waarde:

- **npub** - Public key (je identiteit, veilig om te delen)
- **nsec** - Private key (geheim houden, gebruikt voor signing)
- **note** - Event ID (verwijst naar een specifiek event)

Voorbeeld: De hex-pubkey `3bf0c63f...` wordt `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

De uitgebreide vormen gebruiken TLV-encodering zodat ze lookup hints naast de identifier zelf kunnen meenemen:

- **nprofile** - Profiel met relay hints
- **nevent** - Event met relay hints, author pubkey en kind
- **naddr** - Adresbare event-verwijzing met pubkey, kind, `d` tag en relay hints

## Waarom het belangrijk is

Relay hints zijn niet autoritatief, maar bepalen vaak of een client een gedeeld event in een keer kan ophalen. Daarom zijn `nevent`, `nprofile` en `naddr` meestal betere deelbare formaten dan kale `note`- of `npub`-waarden wanneer content buiten de huidige relay-set van de ontvanger staat.

Een ander praktisch verschil is stabiliteit. `note` verwijst naar een enkele onveranderlijke event-id, terwijl `naddr` verwijst naar een adresseerbaar event dat in de loop van de tijd kan worden vervangen. Voor long-form content, kalenders of repository-aankondigingen is `naddr` meestal het juiste linktype.

## Implementatienotities

- Gebruik bech32 alleen voor menselijke interfaces: weergave, kopieren/plakken, QR-codes, URL's
- Gebruik bech32-formaten nooit in protocolberichten, events of NIP-05-antwoorden
- Alle protocolcommunicatie moet hex-encodering gebruiken
- Neem bij het genereren van nevent/nprofile/naddr relay hints op voor betere vindbaarheid
- Behandel `nsec` overal als geheim materiaal. Een client moet dit nooit standaard tonen, loggen of opnemen in supportexports

---

**Primaire bronnen:**
- [NIP-19 Specificatie](https://github.com/nostr-protocol/nips/blob/master/19.md)

**Vermeld in:**
- [Nieuwsbrief #1: NIP Deep Dive](/en/newsletters/2025-12-17-newsletter/#nip-19-bech32-encoded-identifiers)
- [Nieuwsbrief #3: December-overzicht](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Nieuwsbrief #3: Opmerkelijke codewijzigingen](/en/newsletters/2025-12-31-newsletter/#damus-ios)
- [Nieuwsbrief #4: Ondersteuning voor relay hints](/en/newsletters/2026-01-07-newsletter/)
- [Nieuwsbrief #8: Damus iOS](/en/newsletters/2026-02-04-newsletter/#damus-ios)
- [Nieuwsbrief #11: notecrumbs](/en/newsletters/2026-02-25-newsletter/)

**Zie ook:**
- [NIP-01: Basic Protocol](/nl/topics/nip-01/)
- [NIP-10: Reply Threads](/nl/topics/nip-10/)
