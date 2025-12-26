---
title: "MIP-05: Privacy-behoudende Push-notificaties"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Berichten
  - Protocol
---

MIP-05 definieert een protocol voor push-notificaties die gebruikersprivacy behouden, en lost het probleem op dat traditionele push-systemen vereisen dat servers apparaat-tokens en gebruikersidentiteiten kennen.

## Hoe Het Werkt

- Apparaat-tokens worden versleuteld met ECDH+HKDF en ChaCha20-Poly1305
- Tijdelijke sleutels voorkomen correlatie tussen notificaties
- Een drie-event gossip-protocol (kinds 447-449) synchroniseert versleutelde tokens over groepsleden
- Decoy-tokens via NIP-59 gift wrapping verbergen groepsgroottes

## Privacygaranties

- Push-notificatieservers kunnen gebruikers niet identificeren
- Groepslidmaatschap wordt niet onthuld door notificatiepatronen
- Apparaat-tokens kunnen niet worden gecorreleerd over berichten

## Event Kinds

- **Kind 447**: Versleutelde apparaat-token publicatie
- **Kind 448**: Token-synchronisatieverzoek
- **Kind 449**: Token-synchronisatieantwoord

---

**Primaire bronnen:**
- [MIP-05 PR](https://github.com/marmot-protocol/marmot/pull/18)

**Vermeld in:**
- [Nieuwsbrief #1: Nieuws](/nl/newsletters/2025-12-17-newsletter/#news)

**Zie ook:**
- [Marmot Protocol](/nl/topics/marmot/)
- [NIP-59: Gift Wrap](/nl/topics/nip-59/)
