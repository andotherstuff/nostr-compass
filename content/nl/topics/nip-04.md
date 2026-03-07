---
title: "NIP-04: Versleutelde directe berichten (verouderd)"
date: 2025-12-31
translationOf: /en/topics/nip-04.md
translationDate: 2026-03-07
draft: false
categories:
  - Privacy
  - Berichtenverkeer
---

NIP-04 definieert versleutelde directe berichten met kind 4 events en een via ECDH afgeleid gedeeld geheim. Het was Nostr's eerste DM-schema, maar het is nu legacy-technologie en nieuw werk rond private messaging is verschoven naar NIP-17.

## Hoe het werkt

Berichten gebruiken kind 4 events met deze basisstroom:

1. De afzender leidt een gedeeld geheim af met secp256k1 ECDH.
2. De plaintext wordt versleuteld met AES-256-CBC.
3. Het event bevat een `p` tag die de ontvanger aanduidt.
4. De ciphertext wordt als base64 gecodeerd en samen met de IV in `content` opgeslagen.

Het event zelf blijft een normaal ondertekend Nostr-event, dus relays kunnen de buitenste metadata zien, ook al kunnen ze de plaintext niet lezen.

## Beveiligings- en privacybeperkingen

NIP-04 heeft aanzienlijke privacytekortkomingen:

- **Metadata-lek** - De pubkey van de afzender is publiek zichtbaar op elk bericht
- **Geen afzenderprivacy** - Iedereen kan zien wie met wie berichten uitwisselt
- **Exacte tijdstempels** - De timing van berichten wordt niet gerandomiseerd
- **Niet-standaard sleutelverwerking** - Het schema gebruikt alleen de X-coordinaat van het ECDH-punt, wat correcte implementatie tussen libraries lastiger maakte en weinig ruimte liet voor protocolontwikkeling

De specificatie waarschuwt expliciet dat het "niet in de buurt komt van de stand van de techniek in versleutelde communicatie".

## Waarom het is vervangen

NIP-04 versleutelt de inhoud van berichten, maar verbergt de sociale graaf niet. Relaybeheerders kunnen nog steeds zien wie het event heeft verstuurd, wie het ontvangt en wanneer het is gepubliceerd. Dat is genoeg metadata om gesprekken in kaart te brengen, zelfs zonder de payload te ontsleutelen.

NIP-17 pakt dit aan door NIP-44 payload encryption te combineren met NIP-59 gift wrapping, wat de afzender verbergt voor relays en willekeurige observatoren. Nieuwe implementaties moeten NIP-04 alleen nog als compatibiliteitslaag behandelen.

## Implementatiestatus

Legacy clients en signers bieden nog steeds NIP-04 encrypt/decrypt-methoden aan, omdat oude gesprekken en oudere apps nog in omloop zijn. Die compatibiliteitslaag is belangrijk voor migratie, maar nieuwe functies bouwen bovenop kind 4 events betekent meestal dat oude privacybeperkingen worden meegenomen.

---

**Primaire bronnen:**
- [NIP-04-specificatie](https://github.com/nostr-protocol/nips/blob/master/04.md)

**Vermeld in:**
- [Nieuwsbrief #4: NIP Deep Dive](/en/newsletters/2026-01-07-newsletter/#nip-04-encrypted-direct-messages-legacy)
- [Nieuwsbrief #3: Decemberoverzicht](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Zie ook:**
- [NIP-44: Versleutelde payloads](/nl/topics/nip-44/)
- [NIP-17: Privé directe berichten](/nl/topics/nip-17/)
- [NIP-59: Gift Wrap](/nl/topics/nip-59/)
