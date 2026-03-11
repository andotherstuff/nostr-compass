---
title: "NIP-66: Relay-ontdekking en liveness-monitoring"
date: 2026-01-21
translationOf: /en/topics/nip-66.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Relays
---

NIP-66 standaardiseert het publiceren van relay-monitoringdata naar Nostr. Monitoringdiensten testen relays continu op beschikbaarheid, latentie, protocolnaleving en ondersteunde NIP's, en publiceren de resultaten als kind 30166 events.

## Hoe het werkt

Monitors controleren de beschikbaarheid van relays door verbinding te maken en testabonnementen te versturen. Latentiemetingen volgen verbindingstijd, responstijd op abonnementen en event-propagatievertraging. Protocolnalevingstests verifiëren dat relay-gedrag overeenkomt met de specificaties, en leggen implementatiebugs of opzettelijke afwijkingen bloot.

Verificatie van NIP-ondersteuning gaat verder dan claims in [NIP-11](/nl/topics/nip-11/) doordat monitors echt testen of geadverteerde functies correct werken. Als een relay bijvoorbeeld [NIP-50](/nl/topics/nip-50/) zoekondersteuning claimt maar zoekopdrachten mislukken, laten monitors NIP-50 weg uit de geverifieerde lijst. Dat geeft een feitelijk beeld van relay-capaciteiten.

Kind 30166 events gebruiken de relay-URL als `d` tag, waardoor ze parameterized replaceable events zijn. Elke monitor publiceert één event per relay, bijgewerkt zodra metingen veranderen. Meerdere monitors kunnen dezelfde relay volgen, wat redundantie en kruisvalidatie oplevert.

Round-trip time (rtt) tags meten latentie voor verschillende bewerkingen:
- `rtt open`: WebSocket-verbindingsopbouw
- `rtt read`: responstijd op abonnementen
- `rtt write`: snelheid van event-publicatie

Alle waarden staan in milliseconden. Clients gebruiken deze metrieken om relays met lage latentie te verkiezen voor tijdgevoelige bewerkingen.

Geografische informatie helpt clients om nabije relays te selecteren voor betere latentie en meer censuurbestendigheid. De `geo` tag bevat landcode, landnaam en regio. De `network` tag onderscheidt clearnet-relays van Tor hidden services of I2P-endpoints.

## Waarom het belangrijk is

NIP-66 maakt relay-kwaliteit van anekdote tot machineleesbare data. Een client hoeft niet alleen te vertrouwen op het eigen [NIP-11](/nl/topics/nip-11/) document van een relay of op een hardcoded allowlist. Hij kan gemeten uptime, gemeten latentie en geteste feature-ondersteuning van één of meer monitors vergelijken.

Dat is het belangrijkst voor relay-selectie onder het outbox-model. Wanneer clients dynamisch verbinding maken met veel relays, leggen dode of verkeerd geconfigureerde relays direct kosten op in de vorm van tragere feed loads en meer mislukte fetches.

## Toepassingen

Monitordata voedt relay-selectoren in clients, explorer-websites en trust-evaluatiesystemen. Doordat NIP-66 realtime relay-status biedt los van zelfrapportage door de relay zelf, maakt het geïnformeerde relay-selectie mogelijk.

Gecombineerd met [NIP-11](/nl/topics/nip-11/) (zelfgerapporteerde capaciteiten) en Trusted Relay Assertions (trust-evaluatie) beweegt het ecosysteem richting datagedreven relay-selectie in plaats van te leunen op hardcoded defaults.

## Vertrouwensmodel

NIP-66 creëert geen enkele gezaghebbende monitor. Meerdere monitors kunnen resultaten voor dezelfde relay publiceren, en clients kunnen die naast elkaar leggen. Dat ontwerp vermindert de afhankelijkheid van het oordeel van één operator, maar het betekent ook dat clients een beleid nodig hebben voor welke metingen zij vertrouwen wanneer resultaten conflicteren.

---

**Primaire bronnen:**
- [NIP-66-specificatie](https://github.com/nostr-protocol/nips/blob/master/66.md) - Standaard voor relay-ontdekking en liveness-monitoring

**Vermeld in:**
- [Nieuwsbrief #6: NIP Deep Dive](/nl/newsletters/2026-01-21-newsletter/#nip-deep-dive-nip-11-and-nip-66)

**Zie ook:**
- [NIP-11: Relay Information Document](/nl/topics/nip-11/)
- [NIP-65: Relay List Metadata](/nl/topics/nip-65/)
- [Trusted Relay Assertions](/nl/topics/trusted-relay-assertions/)
