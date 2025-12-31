---
title: "NIP-04: Versleutelde Directe Berichten (Verouderd)"
date: 2025-12-31
translationOf: /en/topics/nip-04.md
translationDate: 2025-12-31
draft: false
categories:
  - Privacy
  - Berichtenverkeer
---

NIP-04 definieert versleutelde directe berichten met AES-256-CBC-versleuteling. Het was de oorspronkelijke methode voor privéberichten op Nostr, maar is verouderd verklaard ten gunste van NIP-17 vanwege aanzienlijke privacybeperkingen.

## Hoe het werkt

Berichten gebruiken kind 4-events met het volgende versleutelingsschema:
1. Een gedeeld geheim wordt gegenereerd met ECDH met de publieke sleutel van de ontvanger en de privésleutel van de afzender
2. Het bericht wordt versleuteld met AES-256-CBC
3. De cijfertekst wordt base64-gecodeerd met de initialisatievector toegevoegd
4. Een `p`-tag identificeert de publieke sleutel van de ontvanger

## Beveiligingsbeperkingen

NIP-04 heeft aanzienlijke privacytekortkomingen:

- **Metadatalek** - De pubkey van de afzender is publiekelijk zichtbaar op elk bericht
- **Geen afzenderprivacy** - Iedereen kan zien wie berichten naar wie stuurt
- **Exacte tijdstempels** - Berichttiming is niet gerandomiseerd
- **Niet-standaard implementatie** - Gebruikt alleen de X-coördinaat van het ECDH-punt in plaats van de standaard SHA256-hash

De specificatie waarschuwt expliciet dat het "niet in de buurt komt van de stand van de techniek in versleutelde communicatie".

## Verouderingsstatus

NIP-04 is verouderd ten gunste van NIP-17, dat NIP-59 gift wrapping gebruikt om de identiteit van de afzender te verbergen. Nieuwe implementaties moeten NIP-17 gebruiken voor privéberichten.

---

**Primaire bronnen:**
- [NIP-04-specificatie](https://github.com/nostr-protocol/nips/blob/master/04.md)

**Vermeld in:**
- [Newsletter #3: December Terugblik](/nl/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Zie ook:**
- [NIP-17: Privé Directe Berichten](/nl/topics/nip-17/)
- [NIP-59: Gift Wrap](/nl/topics/nip-59/)
