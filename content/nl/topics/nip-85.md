---
title: "NIP-85: Trusted Assertions"
date: 2026-02-18
translationOf: /en/topics/nip-85.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Trust
  - Infrastructure
---

NIP-85 definieert Trusted Assertions, een systeem voor het delegeren van dure berekeningen aan vertrouwde serviceproviders die ondertekende resultaten publiceren als Nostr-events.

## Hoe Het Werkt

Web of Trust-scores, engagement-metrics en andere berekende waarden vereisen het crawlen van veel relays en het verwerken van grote eventvolumes. Dit werk is onpraktisch op mobiele apparaten. NIP-85 laat gespecialiseerde providers deze berekeningen uitvoeren en resultaten publiceren die clients kunnen opvragen.

Trusted Assertions zijn adresseerbare events. De `d` tag identificeert het onderwerp dat wordt gescoord, en de event kind identificeert welk soort onderwerp het is: pubkeys (30382), reguliere events (30383), adresseerbare events (30384) en NIP-73-identifiers (30385).

Gebruikers verklaren welke providers ze vertrouwen via kind 10040. Die providerlijsten kunnen openbaar in tags staan of versleuteld in de event-inhoud met [NIP-44](/nl/topics/nip-44/), wat van belang is wanneer een gebruiker zijn trust-inputs niet openlijk wil publiceren.

## Waarom Het Belangrijk Is

Het bruikbare inzicht in NIP-85 is dat het outputs standaardiseert, niet algoritmen. Twee providers kunnen allebei een `rank` tag publiceren voor dezelfde pubkey terwijl ze verschillende Web of Trust-formules, mute-afhandeling, relaydekking of anti-spam-heuristieken gebruiken. Clients blijven interoperabel omdat het resultaatformaat overeenkomt, ook wanneer de berekening dat niet doet.

Dat past beter bij Nostr dan doen alsof er een enkele canonieke rankingservice zal zijn. Gebruikers kiezen wiens assertions ze vertrouwen.

## Trustmodel

Serviceproviders moeten hun eigen assertion-events ondertekenen, en de specificatie raadt verschillende service keys aan voor verschillende algoritmen of gebruikersspecifieke gezichtspunten. Dat voorkomt dat een provider ongerelateerde rankingsystemen laat samenvallen in een enkele ondoorzichtige identiteit.

Trust blijft lokaal. Ondertekende output bewijst welke provider een score heeft gepubliceerd, niet dat de score correct is. Clients hebben beleid nodig voor welke provider keys ze gebruiken, van welke relays ze ophalen en hoe ze met conflicterende assertions omgaan.

## Interop-opmerkingen

NIP-85 gaat verder dan mensen en posts. Kind 30385 laat providers NIP-73 externe identifiers scoren, zoals boeken, websites, hashtags en locaties. Dat schept een pad voor interoperabele reputatie- en engagementdata rond onderwerpen buiten Nostr zelf.

---

**Primaire bronnen:**
- [NIP-85 Specification](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #2223](https://github.com/nostr-protocol/nips/pull/2223) - Richtlijnen voor vindbaarheid van serviceproviders

**Vermeld in:**
- [Newsletter #10: NIP-85 Deep Dive](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Newsletter #11: NIP-85 Service Provider Discoverability](/en/newsletters/2026-02-25-newsletter/#nip-updates)
- [Newsletter #12: Protocol Recap](/en/newsletters/2026-03-04-newsletter/)

**Zie ook:**
- [NIP-44: Encrypted Payloads](/nl/topics/nip-44/)
- [NIP-73: External Content IDs](/nl/topics/nip-73/)
- [Web of Trust](/nl/topics/web-of-trust/)
