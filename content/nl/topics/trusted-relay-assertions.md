---
title: "Trusted Relay Assertions"
date: 2026-01-21
translationOf: /en/topics/trusted-relay-assertions.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Relays
---

Trusted Relay Assertions is het idee om ondertekende externe evaluaties van relays op Nostr te publiceren, zodat clients relays kunnen kiezen met meer context dan alleen zelfgerapporteerde metadata. De huidige gestandaardiseerde bouwsteen is [NIP-85: Trusted Assertions](/nl/topics/nip-85/), die definieert hoe gebruikers providers vertrouwen en hoe providers ondertekende berekende resultaten publiceren.

## Hoe het werkt

Relayselectie heeft drie lagen. [NIP-11: Relay Information Document](/nl/topics/nip-11/) beschrijft wat een relay over zichzelf zegt. [NIP-66: Relay Discovery and Liveness Monitoring](/nl/topics/nip-66/) beschrijft wat waarnemers kunnen meten, zoals beschikbaarheid en latency. Trusted relay assertions proberen de resterende kloof te vullen: wat een derde partij uit die data concludeert, en of een client besluit die conclusie te vertrouwen.

In het bredere NIP-85-model wijzen gebruikers vertrouwde providers aan met kind `10040` events, en providers publiceren ondertekende addressable assertion events. Een relay-scoringapplicatie heeft dan nog twee dingen nodig waar clients het over eens zijn: hoe een relay als subject wordt geïdentificeerd, en welke result tags de score en het ondersteunende bewijs vertegenwoordigen.

Dat onderscheid is belangrijk omdat het transport en de trust delegation zijn gestandaardiseerd, maar het relay-specifieke scoringmodel nog steeds een applicatiepatroon is. Verschillende providers kunnen legitiem van mening verschillen over wat een relay betrouwbaar maakt.

## Vertrouwensmodel

Relay trust scores zijn geen objectieve feiten. De ene provider kan prioriteit geven aan uptime en write throughput, een andere aan juridische jurisdictie, moderatiebeleid of operatoridentiteit, en een derde vooral aan weerstand tegen surveillance. Een bruikbare client moet laten zien wie de score heeft geproduceerd, niet alleen de score zelf.

Hier komt ook [Web of Trust](/nl/topics/web-of-trust/) in beeld. Als een client bepaalde mensen of diensten al vertrouwt, kan die relayevaluaties uit diezelfde sociale omgeving verkiezen in plaats van te doen alsof er één wereldwijde ranking bestaat.

## Waarom het belangrijk is

Voor [NIP-46](/nl/topics/nip-46/) remote signers, wallet connections, of elke app die onbekende relays aanbeveelt, kunnen externe relayevaluaties blinde vertrouwen in defaults verminderen. Gecombineerd met [NIP-65](/nl/topics/nip-65/) relay lists kunnen clients onderscheid maken tussen "welke relays gebruik ik" en "welke relays vertrouw ik voor deze taak".

De belangrijkste correctheidskanttekening is de scope. De nieuwsbriefdekking van januari 2026 beschreef relay trust scoring als een apart voorstel, maar de gemergde standaard in de NIPs-repository is het bredere formaat van [NIP-85: Trusted Assertions](/nl/topics/nip-85/). Relay scoring blijft een use case boven op dat model, niet een apart afgerond relay-trust wire format.

---

**Primaire bronnen:**
- [NIP-85 Specification](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #1534: Trusted Assertions](https://github.com/nostr-protocol/nips/pull/1534)

**Vermeld in:**
- [Newsletter #6: News](/en/newsletters/2026-01-21-newsletter/#trusted-relay-assertions-a-new-approach-to-relay-trust)
- [Newsletter #6: NIP Updates](/en/newsletters/2026-01-21-newsletter/#nip-updates)
- [Newsletter #7: NIP Updates](/en/newsletters/2026-01-28-newsletter/#nip-updates)

**Zie ook:**
- [NIP-11: Relay Information Document](/nl/topics/nip-11/)
- [NIP-66: Relay Discovery and Liveness Monitoring](/nl/topics/nip-66/)
- [NIP-85: Trusted Assertions](/nl/topics/nip-85/)
- [Web of Trust](/nl/topics/web-of-trust/)
