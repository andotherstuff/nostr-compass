---
title: "NIP-44: Versleutelde Payloads"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - Cryptography
  - Privacy
---

NIP-44 definieert een versiegebonden encryptiestandaard voor Nostr-payloads, die het gebrekkige NIP-04-encryptieschema vervangt door moderne cryptografische primitiven.

## Hoe Het Werkt

NIP-44 versie 2 gebruikt een meerstaps encryptieproces:

1. **Sleuteluitwisseling**: ECDH (secp256k1) tussen de publieke sleutels van afzender en ontvanger produceert een gedeeld geheim
2. **Sleutelafleiding**: HKDF-extract met SHA256 en salt `nip44-v2` creëert een gesprekssleutel
3. **Per-bericht Sleutels**: HKDF-expand leidt een ChaCha-sleutel, nonce en HMAC-sleutel af uit een willekeurige nonce
4. **Padding**: Inhoud krijgt padding om de berichtlengte te verbergen
5. **Encryptie**: ChaCha20 versleutelt de gepadde inhoud
6. **Authenticatie**: HMAC-SHA256 zorgt voor berichtintegriteit

De uitvoer is een versiegebonden base64-payload die in een normaal ondertekend Nostr-event gaat. De specificatie vereist dat clients eerst de buitenste NIP-01-eventhandtekening valideren voordat ze de binnenste NIP-44-payload ontsleutelen.

## Cryptographic Choices

- **ChaCha20** boven AES: sneller, met betere weerstand tegen multi-key-aanvallen
- **HMAC-SHA256** boven Poly1305: polynomiale MACs zijn makkelijker te vervalsen
- **SHA256**: consistent met bestaande Nostr-primitieven
- **Versiegebonden Formaat**: maakt toekomstige algoritme-upgrades mogelijk

## Security Properties

- **Authenticated Encryption**: berichten kunnen niet ongemerkt worden aangepast
- **Lengteverhulling**: padding verbergt de berichtgrootte
- **Gesprekssleutels**: dezelfde sleutel voor doorlopende gesprekken vermindert rekenwerk
- **Geaudit**: de Cure53-beveiligingsaudit vond geen exploiteerbare kwetsbaarheden

## Implementatienotities

NIP-44 is geen drop-in vervanging voor NIP-04-payloads. Het definieert een encryptieformaat, geen direct-message-event kind. Protocollen zoals [NIP-17](/nl/topics/nip-17/) en [NIP-59](/nl/topics/nip-59/) definiëren hoe versleutelde payloads in echte berichtstromen worden gebruikt.

De plaintext-invoer is UTF-8-tekst met een lengte van 1 tot 65535 bytes. Dat is een echte beperking voor implementers: als je applicatie willekeurige binaire blobs moet versleutelen, heb je extra encoding of een ander containerformaat nodig.

## Beperkingen

NIP-44 biedt geen:
- **Forward Secrecy**: gecompromitteerde sleutels leggen eerdere berichten bloot
- **Post-Compromise Security**: herstel na sleutelcompromittering
- **Ontkenbaarheid**: berichten zijn aantoonbaar ondertekend door specifieke sleutels
- **Metadata-verhulling**: relay-architectuur beperkt privacy

Voor hoge beveiligingseisen bieden NIP-104 (double ratchet) of MLS-gebaseerde protocollen zoals Marmot sterkere garanties.

## History

NIP-44 revisie 3 werd in december 2023 gemerged na een onafhankelijke Cure53-beveiligingsaudit. Het vormt de cryptografische basis voor NIP-17 private DMs en NIP-59 gift wrapping.

---

**Primaire bronnen:**
- [NIP-44 Specification](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [NIP-44-reference implementations](https://github.com/paulmillr/nip44)
- [Cure53-auditrapport](https://cure53.de/audit-report_nip44-implementations.pdf)

**Vermeld in:**
- [Newsletter #4: NIP Deep Dive](/nl/newsletters/2026-01-07-newsletter/)
- [Newsletter #3: December 2023](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #3: December 2024](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #12: Marmot](/nl/newsletters/2026-03-04-newsletter/)
- [Newsletter #13: Vector](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19: nostter NIP-44 migration](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: nowhere encrypts Nostr traffic](/en/newsletters/2026-04-22-newsletter/)

**Zie ook:**
- [NIP-04: Encrypted Direct Messages (verouderd)](/nl/topics/nip-04/)
- [NIP-17: Private Direct Messages](/nl/topics/nip-17/)
- [NIP-59: Gift Wrap](/nl/topics/nip-59/)
- [NIP-104: Double Ratchet Encryption](/nl/topics/nip-104/)
- [MLS: Message Layer Security](/nl/topics/mls/)
