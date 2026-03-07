---
title: "NIP-55: Android Signer-applicatie"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Ondertekening
  - Mobiel
---

NIP-55 definieert hoe Android-apps ondertekenings- en encryptiebewerkingen aanvragen bij een aparte signer-applicatie. Het geeft Android-clients een native alternatief voor browserextensies en externe bunkers.

## Hoe het werkt

NIP-55 gebruikt twee Android-mechanismen:

- **Intents** voor foreground-flows met expliciete goedkeuring door de gebruiker
- **Content resolvers** voor background-flows nadat de gebruiker blijvende toestemming heeft gegeven

De gebruikelijke verbindingsflow begint met `get_public_key`. De signer retourneert zowel de pubkey van de gebruiker als de pakketnaam van de signer, en de client hoort beide te cachen. `get_public_key` herhalen in background-loops is een veelgemaakte implementatiefout waar de specificatie expliciet voor waarschuwt.

## Belangrijkste bewerkingen

- **get_public_key** - Haal de pubkey van de gebruiker en de pakketnaam van de signer op
- **sign_event** - Onderteken een Nostr-event
- **nip04_encrypt/decrypt** - Versleutel of ontsleutel NIP-04-berichten
- **nip44_encrypt/decrypt** - Versleutel of ontsleutel NIP-44-berichten
- **decrypt_zap_event** - Ontsleutel event-payloads die met zaps samenhangen

## Opmerkingen over beveiliging en UX

NIP-55 houdt sleutels op het apparaat, maar hangt nog steeds af van Android-appgrenzen en hoe de signer permissies afhandelt. Ondersteuning voor content resolvers geeft een veel soepelere UX dan herhaalde intent-prompts, maar pas nadat de gebruiker duurzame toestemming aan die client heeft gegeven.

Voor webapps op Android is NIP-55 minder praktisch dan NIP-46. Browsergebaseerde flows kunnen niet direct background-responses ontvangen zoals native Android-apps dat wel kunnen, waardoor veel implementaties terugvallen op callback-URL's, overdracht via het klembord of handmatig plakken.

---

**Primaire bronnen:**
- [NIP-55-specificatie](https://github.com/nostr-protocol/nips/blob/master/55.md)

**Vermeld in:**
- [Nieuwsbrief #1: Releases](/en/newsletters/2025-12-17-newsletter/#releases)
- [Nieuwsbrief #2: News](/en/newsletters/2025-12-24-newsletter/#news)
- [Nieuwsbrief #2: NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Nieuwsbrief #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Nieuwsbrief #7: NIP Updates](/en/newsletters/2026-01-07-newsletter/#nip-updates)
- [Nieuwsbrief #11: NIP Deep Dive](/en/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-55-android-signer-application)

**Zie ook:**
- [NIP-46: Nostr Connect](/nl/topics/nip-46/)
