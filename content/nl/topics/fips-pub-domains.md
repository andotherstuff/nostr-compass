---
title: "FIPS Public Domains"
date: 2026-09-30
translationOf: /en/topics/fips-pub-domains.md
translationDate: 2026-10-02
draft: false
categories:
  - Protocol
  - Networking
  - Identity
---

fips-pub-domains is een vroege implementatie om vertrouwde internetdomeinnamen om te zetten naar diensten op de [FIPS](/nl/topics/fips/)-mesh. Het publiceert ondertekende Nostr-claims, maar een handtekening bewijst alleen wie een claim heeft gedaan. Een client moet ook DNS- of DNSSEC-bewijs, een vertrouwde getuige of een eerder vastgepinde koppeling controleren voordat hij de indiener als eigenaar van het domein behandelt.

## Verificatie en offline gebruik {#verification-and-offline-use}

De [eerste release](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.1.0) voegde de claim, de resolver-daemon en de Android-integratie toe. [Versie 0.2.0](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.0) kan een DNSSEC-bewijs aan een claim koppelen, zodat een client die alleen een mesh-relay ziet een nog niet eerder gezien ondertekend domein kan verifiëren tegen de rootsleutels van DNS. Het ondersteunt ook meer dan één geverifieerde server voor een domein. [Versie 0.2.1](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.1) herstelde de meegeleverde serverunit en liet die zonder root draaien; bestaande installaties hebben de vervangende unit nodig.

De [testnotities](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md) van het project beschrijven gevallen met twee nodes en met alleen een mesh-relay. Het zijn tests die door de beheerders zijn gerapporteerd, geen bewijs van een bredere uitrol. Het [NIP-DB-voorstel](https://github.com/nostr-protocol/nips/pull/2487) staat open, en de kindnummers voor events in het concept zijn plaatshouders en geen toegewezen Nostr-kinds.

---

**Primaire bronnen:**
- [Repository en README](https://github.com/fr34aky/fips-pub-domains)
- [Releases 0.1.0–0.2.1](https://github.com/fr34aky/fips-pub-domains/releases)
- [Voorgestelde NIP-DB](https://github.com/nostr-protocol/nips/pull/2487)
- [Testnotities](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**Genoemd in:**
- [Nieuwsbrief #42: fips-pub-domains](/nl/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)

**Zie ook:**
- [FIPS](/nl/topics/fips/)
