---
title: "NIP-66: Relay-Ontdekking en Liveness-Monitoring"
date: 2026-01-21
translationOf: /en/topics/nip-66.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Relays
---

NIP-66 standaardiseert het publiceren van relay-monitoringdata naar Nostr. Monitoringdiensten testen continu relays op beschikbaarheid, latentie, protocolnaleving en ondersteunde NIP's, en publiceren resultaten als kind 30166 events.

## Hoe Het Werkt

Monitors controleren relay-beschikbaarheid door verbinding te maken en testabonnementen te versturen. Latentiemetingen volgen verbindingstijd, abonnementsresponstijd en event-propagatievertraging. Protocolvalevingtesten verifiëren of relay-gedrag overeenkomt met specificaties, wat implementatiebugs of opzettelijke afwijkingen detecteert.

NIP-ondersteuningsverificatie gaat verder dan [NIP-11](/nl/topics/nip-11/) claims door daadwerkelijk te testen of geadverteerde functies correct werken. Als een relay [NIP-50](/nl/topics/nip-50/) zoekondersteuning claimt maar zoekopdrachten falen, zullen monitors NIP-50 weglaten uit de geverifieerde lijst. Dit biedt ground truth over relay-capaciteiten.

Kind 30166 events gebruiken de relay URL als de `d` tag, waardoor het geparametriseerde vervangbare events zijn. Elke monitor publiceert één event per relay, bijgewerkt wanneer metingen veranderen. Meerdere monitors kunnen dezelfde relay volgen, wat redundantie en kruisvalidatie biedt.

Round-trip time (rtt) tags meten latentie voor verschillende operaties:
- `rtt open`: WebSocket-verbindingsopbouw
- `rtt read`: Abonnementsresponstijd
- `rtt write`: Event-publicatiesnelheid

Alle waarden zijn in milliseconden. Clients gebruiken deze metrieken om relays met lage latentie te prefereren voor tijdgevoelige operaties.

Geografische informatie helpt clients nabije relays te selecteren voor betere latentie en censuurbestendigheid. De `geo` tag bevat landcode, landnaam en regio. De `network` tag onderscheidt clearnet relays van Tor hidden services of I2P endpoints.

## Toepassingen

Monitordata voedt relay-selectoren in clients, explorer-websites en vertrouwensevaluatiesystemen. Door realtime relay-status te bieden onafhankelijk van relay zelfrapportage, maakt NIP-66 geïnformeerde relay-selectie mogelijk.

Gecombineerd met [NIP-11](/nl/topics/nip-11/) (zelfgerapporteerde capaciteiten) en Trusted Relay Assertions (vertrouwensevaluatie), beweegt het ecosysteem naar datagedreven relay-selectie in plaats van te vertrouwen op hardgecodeerde defaults.

---

**Primaire bronnen:**
- [NIP-66 Specificatie](https://github.com/nostr-protocol/nips/blob/master/66.md) - Relay-ontdekking en liveness-monitoringstandaard

**Vermeld in:**
- [Nieuwsbrief #6: NIP Deep Dive](/nl/newsletters/2026-01-21-newsletter/#nip-deep-dive-nip-11-and-nip-66)

**Zie ook:**
- [NIP-11: Relay Information Document](/nl/topics/nip-11/)
- [Trusted Relay Assertions](/nl/topics/trusted-relay-assertions/)
