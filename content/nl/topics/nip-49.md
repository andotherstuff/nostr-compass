---
title: "NIP-49: Private Key Encryption"
date: 2026-03-11
translationOf: /en/topics/nip-49.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Key Management
  - Security
---

NIP-49 definieert hoe een client de privésleutel van een gebruiker kan versleutelen met een wachtwoord en het resultaat kan coderen als een `ncryptsec`-string. Het doel is draagbaarheid met sterkere standaardinstellingen dan het opslaan van een rauwe `nsec`, terwijl de versleutelde sleutel toch eenvoudig tussen clients verplaatsbaar blijft.

## Hoe Het Werkt

De client begint met de rauwe 32-byte secp256k1 privésleutel, niet een hex- of bech32-string. Het leidt een tijdelijke symmetrische sleutel af van het wachtwoord van de gebruiker met scrypt, met een willekeurig salt per sleutel en een aanpasbare werkfactor opgeslagen als `LOG_N`. Vervolgens versleutelt het de privésleutel met XChaCha20-Poly1305, voegt versie- en sleutelafhandelingsmetadata toe, en bech32-codeert het resultaat onder het `ncryptsec`-voorvoegsel.

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

Het bovenstaande event is een voorbeeldcontainer, geen NIP-49 vereiste. NIP-49 standaardiseert het versleutelde sleutelformaat zelf, niet een specifiek event kind voor publicatie ervan. Clients kunnen een `ncryptsec` lokaal opslaan, synchroniseren via app-specifieke opslag, of presenteren als een back-upexport.

## Beveiligingsmodel

NIP-49 doet twee dingen tegelijk. Het zet een gebruikerswachtwoord om in een goede versleutelingssleutel, en het vertraagt brute-force herstelpogingen met een geheugen-intensieve KDF. De werkfactor is belangrijk. Hogere `LOG_N`-waarden maken ontsleuteling trager voor legitieme gebruikers, maar verhogen ook de kosten van offline raden voor aanvallers.

Het formaat draagt ook een eenbyte-vlag die beschrijft of de sleutel ooit onveilig is behandeld voordat deze werd versleuteld. Dit verandert de ciphertekst zelf niet, maar geeft clients een manier om een nieuw gegenereerde beschermde back-up te onderscheiden van een sleutel die al in platte tekst was rondgestuurd voordat deze werd verpakt.

## Implementatienotities

- Wachtwoorden worden genormaliseerd naar Unicode NFKC voor sleutelafleiding, zodat hetzelfde wachtwoord consistent kan worden ingevoerd over clients heen.
- XChaCha20-Poly1305 gebruikt een 24-byte nonce en geauthenticeerde versleuteling, zodat manipulatie van de ciphertekst netjes faalt tijdens ontsleuteling.
- De symmetrische sleutel moet worden genulsteld en verwijderd na gebruik.
- De specificatie raadt af om versleutelde sleutels naar publieke relays te posten, omdat het verzamelen van veel versleutelde sleutels de offline kraakpositie van een aanvaller verbetert.

## Implementaties

- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Voegt aanmeldcompatibiliteit toe met NIP-49 versleutelde privésleutels

---

**Primaire bronnen:**
- [NIP-49 Specificatie](https://github.com/nostr-protocol/nips/blob/master/49.md)
- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - Client-side aanmeldflow met NIP-49

**Vermeld in:**
- [Newsletter #13: Formstr](/en/newsletters/2026-03-11-newsletter/#formstr)
- [Newsletter #13: NIP Deep Dive](/en/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-49-private-key-encryption)

**Zie ook:**
- [NIP-46: Nostr Connect](/nl/topics/nip-46/)
- [NIP-55: Android Signer Application](/nl/topics/nip-55/)
