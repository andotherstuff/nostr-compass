---
title: "NIP-44: Versleutelde Payloads"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2025-12-31
draft: false
categories:
  - NIP
  - Cryptografie
  - Privacy
---

NIP-44 definieert een versiebeheerde encryptiestandaard voor Nostr payloads, die het gebrekkige NIP-04 encryptieschema vervangt door moderne cryptografische primitieven.

## Hoe Het Werkt

NIP-44 versie 2 gebruikt een meerstaps encryptieproces:

1. **Sleutelovereenkomst**: ECDH (secp256k1) tussen de publieke sleutels van zender en ontvanger produceert een gedeeld geheim
2. **Sleutelafleiding**: HKDF-extract met SHA256 en salt `nip44-v2` creert een gespreksleutel
3. **Per-bericht Sleutels**: HKDF-expand leidt ChaCha-sleutel, nonce en HMAC-sleutel af van een willekeurige nonce
4. **Padding**: Inhoud wordt opgevuld om berichtlengte te verbergen
5. **Encryptie**: ChaCha20 versleutelt de opgevulde inhoud
6. **Authenticatie**: HMAC-SHA256 biedt berichtintegriteit

## Cryptografische Keuzes

- **ChaCha20** boven AES: Sneller, betere multi-key aanvalsweerstand
- **HMAC-SHA256** boven Poly1305: Polynomiale MACs zijn makkelijker te vervalsen
- **SHA256**: Consistent met bestaande Nostr-primitieven
- **Versiebeheerd Formaat**: Maakt toekomstige algoritme-upgrades mogelijk

## Beveiligingseigenschappen

- **Geauthenticeerde Encryptie**: Berichten kunnen niet worden gemanipuleerd
- **Lengtemaskering**: Padding verbergt berichtgrootte
- **Gespreksleutels**: Dezelfde sleutel voor doorlopende gesprekken vermindert berekening
- **Geauditeerd**: Cure53 beveiligingsaudit vond geen exploiteerbare kwetsbaarheden

## Beperkingen

NIP-44 biedt niet:
- **Forward Secrecy**: Gecompromitteerde sleutels stellen eerdere berichten bloot
- **Post-Compromise Security**: Herstel na sleutelcompromittering
- **Ontkenbaarheid**: Berichten zijn aantoonbaar ondertekend door specifieke sleutels
- **Metadata Verberging**: Relay-architectuur beperkt privacy

Voor hoge beveiligingsbehoeften bieden NIP-104 (Double Ratchet) of MLS-gebaseerde protocollen zoals Marmot sterkere garanties.

## Geschiedenis

NIP-44 revisie 3 werd samengevoegd in december 2023 na een onafhankelijke Cure53 beveiligingsaudit. Het vormt de cryptografische basis voor NIP-17 prive-DMs en NIP-59 gift wrapping.

---

**Primaire bronnen:**
- [NIP-44 Specificatie](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [NIP-44 Referentie-implementaties](https://github.com/paulmillr/nip44)
- [Cure53 Auditrapport](https://cure53.de/audit-report_nip44-implementations.pdf)

**Vermeld in:**
- [Nieuwsbrief #3: December 2023](/nl/newsletters/2025-12-31-newsletter/#december-2023-ecosystem-maturation)
- [Nieuwsbrief #3: December 2024](/nl/newsletters/2025-12-31-newsletter/#december-2024-protocol-advancement)

**Zie ook:**
- [NIP-04: Versleutelde Directe Berichten (verouderd)](/nl/topics/nip-04/)
- [NIP-17: Privé Directe Berichten](/nl/topics/nip-17/)
- [NIP-59: Gift Wrap](/nl/topics/nip-59/)
- [NIP-104: Double Ratchet Encryptie](/nl/topics/nip-104/)
- [MLS: Message Layer Security](/nl/topics/mls/)
