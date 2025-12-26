---
title: "NIP-55: Android Signer Applicatie"
date: 2025-12-17
draft: false
categories:
  - Ondertekening
  - Mobiel
---

NIP-55 definieert hoe Android-applicaties ondertekeningsbewerkingen kunnen aanvragen bij een speciale signer-app, waardoor gebruikers hun privésleutels op één veilige locatie kunnen houden terwijl ze meerdere Nostr-clients gebruiken.

## Hoe Het Werkt

NIP-55 gebruikt Android's content provider interface om ondertekeningsbewerkingen bloot te stellen. Een signer-app registreert zich als content provider, en andere Nostr-apps kunnen handtekeningen aanvragen zonder ooit direct toegang te krijgen tot de privésleutel.

De flow:
1. Client-app roept de content provider van de signer aan
2. Signer toont goedkeurings-UI aan de gebruiker
3. Gebruiker keurt goed of weigert het verzoek
4. Signer retourneert de handtekening (of weigering) naar de client

## Belangrijke Bewerkingen

- **get_public_key** - Haal de publieke sleutel van de gebruiker op (eenmaal aanroepen tijdens initiële verbinding)
- **sign_event** - Onderteken een Nostr-event
- **nip04_encrypt/decrypt** - Versleutel of ontsleutel NIP-04 berichten
- **nip44_encrypt/decrypt** - Versleutel of ontsleutel NIP-44 berichten

## Verbindingsinitiatie

Een veelgemaakte implementatiefout is het herhaaldelijk aanroepen van `get_public_key` vanuit achtergrondprocessen. De specificatie raadt aan om het slechts eenmaal aan te roepen tijdens de initiële verbindingsopstelling, en het resultaat vervolgens te cachen.

---

**Primaire bronnen:**
- [NIP-55 Specificatie](https://github.com/nostr-protocol/nips/blob/master/55.md)

**Vermeld in:**
- [Nieuwsbrief #1: Releases](/nl/newsletters/2025-12-17-newsletter/#releases)
- [Nieuwsbrief #2: Nieuws](/nl/newsletters/2025-12-24-newsletter/#news)
- [Nieuwsbrief #2: NIP Updates](/nl/newsletters/2025-12-24-newsletter/#nip-updates)

**Zie ook:**
- [NIP-46: Nostr Connect](/nl/topics/nip-46/)
