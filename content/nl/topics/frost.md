---
title: "FROST (Flexible Round-Optimized Schnorr Threshold Signatures)"
date: 2025-12-31
translationOf: /en/topics/frost.md
translationDate: 2026-03-07
draft: false
categories:
  - Cryptografie
  - Protocol
---

FROST (Flexible Round-Optimized Schnorr Threshold Signatures) is een threshold signature scheme waarmee een groep samen een geldige Schnorr-signature kan produceren zonder dat een deelnemer de volledige private key bezit.

## Hoe het werkt

FROST maakt T-of-N-signing mogelijk. Elke threshold-groep van deelnemers kan samenwerken om een signature te produceren voor de public key van de groep.

Het signing protocol gebruikt twee rondes:

1. **Commitment-ronde**: Elke deelnemer genereert en deelt cryptografische commitments
2. **Signature-ronde**: Deelnemers combineren hun partial signatures tot een definitieve aggregate signature

De uiteindelijke output verifieert als een gewone Schnorr-signature. Verifiers zien een signature onder een public key, niet een lijst van medeondertekenaars.

## Beveiligingsnotities

Nonce handling is kritisch. De RFC stelt expliciet dat signing nonces eenmalig mogen worden gebruikt. Hergebruik kan key material lekken.

De RFC standaardiseert distributed key generation ook niet. De specificatie behandelt het signing protocol zelf en bevat trusted-dealer key generation alleen als appendix. In de praktijk hangt de veiligheid van een FROST-deployment af van zowel de signing flow als van de manier waarop shares zijn aangemaakt en opgeslagen.

## Gebruiksscenario's in Nostr

In de context van Nostr kan FROST het volgende ondersteunen:

- **Quorum-governance**: Groepen kunnen een nsec delen via T-of-N-schema's, waarbij leden zichzelf kunnen vertegenwoordigen of aan councils kunnen delegeren
- **Multi-sig-administratie**: Community-moderatie waarvoor meerdere admin signatures nodig zijn
- **Gedecentraliseerd key management**: Vertrouwen verdelen over meerdere partijen voor kritieke operaties

## Status

FROST is gespecificeerd in [RFC 9591](https://datatracker.ietf.org/doc/rfc9591/), gepubliceerd in juni 2024 via de IRTF-stroom. Dat geeft het protocol een stabiele publieke specificatie, maar het is geen IETF standards-track RFC.

---

**Primaire bronnen:**
- [RFC 9591: FROST Protocol](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST-paper (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [Zcash Foundation Rust-implementatie](https://github.com/ZcashFoundation/frost)

**Vermeld in:**
- [Newsletter #3: NIPs Repository](/en/newsletters/2025-12-31-newsletter/#nips-repository)
- [Newsletter #8](/en/newsletters/2026-02-04-newsletter/)
- [Newsletter #10](/en/newsletters/2026-02-18-newsletter/)

**Zie ook:**
- [NIP-46: Nostr Connect](/nl/topics/nip-46/)
- [NIP-55: Android Signer Application](/nl/topics/nip-55/)
