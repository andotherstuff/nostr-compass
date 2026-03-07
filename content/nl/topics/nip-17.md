---
title: "NIP-17: Privé Directe Berichten"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Privacy
  - Berichten
---

NIP-17 definieert private direct messages met NIP-59 gift wrapping voor afzenderprivacy. In tegenstelling tot NIP-04 DMs, die de afzender in het buitenste event zichtbaar maken, verbergt NIP-17 de afzender voor relays en toevallige waarnemers.

## Hoe Het Werkt

Berichten worden in meerdere encryptielagen verpakt:
1. De eigenlijke berichtinhoud staat in een rumor event van kind 14.
2. Een seal versleutelt die inhoud naar de ontvanger.
3. Een gift wrap versleutelt de seal opnieuw en publiceert die vanaf een disposable keypair.

De buitenste gift wrap gebruikt een willekeurig disposable keypair, zodat relays en waarnemers niet kunnen vaststellen wie het bericht heeft verzonden.

## Berichtstructuur

- **Kind 14** - De eigenlijke DM-inhoud binnen de verpakte lagen
- **Kind 1059** - Het buitenste gift wrap-event dat naar relays wordt gepubliceerd
- Gebruikt NIP-44-encryptie voor de payloads binnen de wrapping flow
- De specificatie is verfijnd om interactieve DM-functies zoals reacties beter te ondersteunen

## Beveiligings- en Vertrouwensmodel

- Relays kunnen de afzender niet zien, verborgen door het disposable keypair van gift wrap
- De ontvanger is zichtbaar, in de `p` tag van de gift wrap
- Berichttimestamps worden binnen een venster gerandomiseerd
- Geen zichtbare threading of gespreksgroepering op de relay

De ontvanger leert na het uitpakken nog steeds wie het bericht heeft verzonden. NIP-17 verbergt de identiteit van de afzender voor het netwerk, niet voor de andere deelnemer. Dat onderscheid is belangrijk wanneer mensen het over "private DMs" hebben.

## Waarom Het Belangrijk Is

NIP-04 DMs versleutelen de inhoud, maar laten metadata zichtbaar:
- De pubkey van de afzender is openbaar
- De pubkey van de ontvanger staat in de `p` tag
- Timestamps zijn exact

NIP-17 verbergt de afzender, ten koste van een complexere implementatie.

Die extra complexiteit levert een echte privacyverbetering op. Een relay kan nog steeds zien dat een wrapped message aan een ontvanger is gericht, maar kan niet direct een afzender-ontvanger-grafiek opbouwen uit metadata van het buitenste event, zoals dat wel kan bij kind 4-berichten.

## Interop-Hinweise

NIP-17 definieert ook inbox relay lists voor private messaging. Clients kunnen een kind 10050-event publiceren, zodat afzenders weten naar welke relays ze DM-verkeer moeten sturen. DM-routing gescheiden houden van routing voor publieke content helpt voorkomen dat privéverkeer op de verkeerde plaatsen terechtkomt.

---

**Primaire bronnen:**
- [NIP-17-specificatie](https://github.com/nostr-protocol/nips/blob/master/17.md)
- [PR #2098](https://github.com/nostr-protocol/nips/pull/2098) - opschoning van de formulering en update voor reaction support

**Vermeld in:**
- [Nieuwsbrief #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Nieuwsbrief #2: News](/en/newsletters/2025-12-24-newsletter/#news)
- [Nieuwsbrief #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Nieuwsbrief #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/#shopstr-marketplace)
- [Nieuwsbrief #5: News](/en/newsletters/2026-01-13-newsletter/#news)

**Zie ook:**
- [NIP-04: Versleutelde Direct Messages (Verouderd)](/nl/topics/nip-04/)
- [NIP-44: Encrypted Payloads](/nl/topics/nip-44/)
- [NIP-59: Gift Wrap](/nl/topics/nip-59/)
