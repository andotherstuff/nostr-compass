---
title: "Voorgestelde NIP-DB: Koppelingen tussen domeinen en diensten"
date: 2026-09-30
translationOf: /en/topics/nip-db.md
translationDate: 2026-10-02
draft: false
categories:
  - Proposals
  - Networking
  - Identity
---

NIP-DB is een **open voorstel** om een gewoon internetdomein te koppelen aan een dienst die via een sleutel wordt geadresseerd. De event-kinds en formuleringen staan nog ter beoordeling; deze pagina presenteert het niet als een geaccepteerde Nostr-specificatie.

## Verificatiemodel {#verification-model}

Een serverende sleutel kan een ondertekende claim publiceren die het domein en de dienst noemt. Het voorstel beschrijft optioneel DNS- of DNSSEC-bewijs, attesteringen van getuigen en een zonerecord voor namen onder het domein. Een handtekening bewijst welke sleutel een claim heeft gepubliceerd, maar niet dat die sleutel het domein beheert. Een client moet de koppeling verifiëren met DNS-bewijs, een vertrouwde getuige of een eerder vastgepinde sleutel voordat hij die gebruikt om een naam om te zetten.

[fips-pub-domains](/nl/topics/fips-pub-domains/) is de referentie-implementatie van de auteur voor de FIPS-mesh. De gedocumenteerde tests met twee nodes en met alleen een mesh zijn door de beheerder gerapporteerd implementatiebewijs. Ze beslechten de lopende beoordeling van het voorstel niet en tonen geen bredere uitrol aan.

---

**Primaire bronnen:**
- [Open pull request voor NIP-DB](https://github.com/nostr-protocol/nips/pull/2487)
- [Concept van de auteur en plaatshouders voor event-kinds](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/nip.md)
- [Referentie-implementatie en tests](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**Genoemd in:**
- [Nieuwsbrief #42: publieke domeinen](/nl/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)
- [Nieuwsbrief #42: voorgestelde NIP-DB](/nl/newsletters/2026-09-30-newsletter/#nip-db-proposes-verified-domain-names-for-key-addressed-services)
