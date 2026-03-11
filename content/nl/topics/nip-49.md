---
title: "NIP-49: Encryptie van privésleutels"
date: 2026-03-11
translationOf: /en/topics/nip-49.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Key Management
  - Security
---

NIP-49 definieert hoe een client de privésleutel van een gebruiker met een wachtwoord kan versleutelen en het resultaat als een `ncryptsec`-string kan coderen. Het doel is portabiliteit met sterkere standaardinstellingen dan het opslaan van een ruwe `nsec`, terwijl de versleutelde sleutel toch eenvoudig tussen clients kan worden verplaatst.

## Hoe het werkt

De client begint met de ruwe secp256k1 privésleutel van 32 bytes, niet met een hex- of bech32-string. Daarna leidt hij met scrypt een tijdelijke symmetrische sleutel af uit het wachtwoord van de gebruiker, met een willekeurige salt per sleutel en een instelbare werkfactor opgeslagen als `LOG_N`. Vervolgens versleutelt hij de privésleutel met XChaCha20-Poly1305, voegt versionering en metadata over sleutelafhandeling toe, en codeert het resultaat als bech32 onder het prefix `ncryptsec`.

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

Het event hierboven is een voorbeeldcontainer, geen vereiste van NIP-49. NIP-49 standaardiseert het formaat van de versleutelde sleutel zelf, niet een apart event kind om die sleutel te publiceren. Clients kunnen een `ncryptsec` lokaal opslaan, via app-specifieke opslag synchroniseren of als back-up export tonen.

## Beveiligingsmodel

NIP-49 doet twee dingen tegelijk. Het zet een gebruikerswachtwoord om in een echte encryptiesleutel en het vertraagt brute-force herstelpogingen met een memory-hard KDF. De werkfactor doet ertoe. Hogere `LOG_N`-waarden maken ontsleutelen trager voor legitieme gebruikers, maar verhogen ook de kosten van offline gokken voor aanvallers.

Het formaat bevat ook een flag van een byte die beschrijft of de sleutel ooit onveilig is behandeld voor de encryptie. Dat verandert de ciphertext zelf niet, maar geeft clients een manier om onderscheid te maken tussen een nieuw gegenereerde beschermde back-up en een sleutel die eerder al als plaintext rondzwierf voordat hij werd ingepakt.

## Implementatienotities

- Wachtwoorden worden naar Unicode NFKC genormaliseerd voor de sleutelafleiding, zodat hetzelfde wachtwoord op clients consistent kan worden ingevoerd.
- XChaCha20-Poly1305 gebruikt een nonce van 24 bytes en geauthenticeerde versleuteling, zodat manipulatie van de ciphertext netjes faalt tijdens het ontsleutelen.
- De symmetrische sleutel moet na gebruik worden gewist en weggegooid.
- De specificatie raadt niet aan versleutelde sleutels op publieke relays te publiceren, omdat het verzamelen van veel versleutelde sleutels de offline kraakpositie van een aanvaller verbetert.

## Implementaties

- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - voegt signup-compatibiliteit toe met via NIP-49 versleutelde privésleutels

---

**Primaire bronnen:**
- [NIP-49-specificatie](https://github.com/nostr-protocol/nips/blob/master/49.md)
- [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) - client-side signup-flow met NIP-49

**Vermeld in:**
- [Nieuwsbrief #13: Formstr](/nl/newsletters/2026-03-11-newsletter/#formstr)
- [Nieuwsbrief #13: NIP-verdieping](/nl/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-49-private-key-encryption)

**Zie ook:**
- [NIP-46: Nostr Connect](/nl/topics/nip-46/)
- [NIP-55: Android Signer Application](/nl/topics/nip-55/)
