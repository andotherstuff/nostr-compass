---
title: "FROST (Flexible Round-Optimized Schnorr Threshold Signatures)"
date: 2025-12-31
translationOf: /en/topics/frost.md
translationDate: 2025-12-31
draft: false
categories:
  - Cryptografie
  - Protocol
---

FROST (Flexible Round-Optimized Schnorr Threshold Signatures) is een drempelhandtekeningschema dat een groep deelnemers in staat stelt om gezamenlijk geldige Schnorr-handtekeningen te produceren zonder dat een enkele partij de volledige privésleutel bezit.

## Hoe het werkt

FROST maakt T-van-N drempelondertekening mogelijk, waarbij T deelnemers van in totaal N sleutelhouders moeten samenwerken om een geldige handtekening te produceren. Het protocol werkt in twee rondes:

1. **Commitment-ronde**: Elke deelnemer genereert en deelt cryptografische commitments
2. **Handtekeningronde**: Deelnemers combineren hun gedeeltelijke handtekeningen tot een definitieve geaggregeerde handtekening

De resulterende handtekening is niet te onderscheiden van een standaard Schnorr-handtekening, waardoor achterwaartse compatibiliteit met bestaande verificatiesystemen behouden blijft.

## Belangrijke eigenschappen

- **Drempelbeveiliging**: Geen enkele deelnemer kan alleen ondertekenen; T partijen moeten samenwerken
- **Ronde-efficiëntie**: Slechts twee communicatierondes nodig voor ondertekening
- **Bescherming tegen vervalsing**: Nieuwe technieken beschermen tegen aanvallen op eerdere drempelschema's
- **Handtekeningaggregatie**: Meerdere handtekeningen worden gecombineerd tot één compacte handtekening
- **Privacy**: Eindhandtekeningen onthullen niet welke T deelnemers hebben ondertekend

## Gebruiksscenario's in Nostr

In de context van Nostr maakt FROST het volgende mogelijk:

- **Quorum-governance**: Groepen kunnen een nsec delen via T-van-N-schema's, waarbij leden zichzelf kunnen vertegenwoordigen of aan raden kunnen delegeren
- **Multi-handtekeningbeheer**: Gemeenschapsmoderatie die meerdere beheerdershandtekeningen vereist
- **Gedecentraliseerd sleutelbeheer**: Verdeling van vertrouwen over meerdere partijen voor kritieke operaties

## Standaardisatie

FROST werd in juni 2024 gestandaardiseerd als RFC 9591, getiteld "The Flexible Round-Optimized Schnorr Threshold (FROST) Protocol for Two-Round Schnorr Signatures".

---

**Primaire bronnen:**
- [RFC 9591: FROST Protocol](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST Paper (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [University of Waterloo CrySP](https://crysp.uwaterloo.ca/software/frost/)
- [Zcash Foundation Rust Implementation](https://github.com/ZcashFoundation/frost)

**Vermeld in:**
- [Newsletter #3: NIPs Repository](/nl/newsletters/2025-12-31-newsletter/#nips-repository)

**Zie ook:**
- [NIP-XX Quorum-voorstel](https://github.com/nostr-protocol/nips/pull/2179)
