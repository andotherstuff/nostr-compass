---
title: "NIP-46: Nostr Connect"
date: 2025-12-17
draft: false
categories:
  - Ondertekening
  - Protocol
---

NIP-46 definieert remote signing, waarmee een signer-applicatie sleutels kan behouden terwijl clients handtekeningen aanvragen via Nostr-relays.

## Hoe Het Werkt

1. Signer genereert een verbindings-URI (`bunker://` of `nostrconnect://`)
2. Gebruiker plakt de URI in een client
3. Client stuurt ondertekeningsverzoeken als versleutelde events naar de relay van de signer
4. Signer vraagt gebruiker om goedkeuring, retourneert ondertekende events

## Verbindingsmethoden

- **bunker://** - Signer-geïnitieerde verbinding
- **nostrconnect://** - Client-geïnitieerde verbinding via QR-code of deep link

## Ondersteunde Bewerkingen

- `sign_event` - Onderteken een willekeurig event
- `get_public_key` - Haal de publieke sleutel van de signer op
- `nip04_encrypt/decrypt` - NIP-04 encryptie bewerkingen
- `nip44_encrypt/decrypt` - NIP-44 encryptie bewerkingen

---

**Primaire bronnen:**
- [NIP-46 Specificatie](https://github.com/nostr-protocol/nips/blob/master/46.md)

**Vermeld in:**
- [Nieuwsbrief #1: Noemenswaardige Codewijzigingen](/nl/newsletters/2025-12-17-newsletter/#amethyst-android)

**Zie ook:**
- [NIP-55: Android Signer](/nl/topics/nip-55/)
