---
title: "TollGate: Pay-per-use Internet Over Nostr and Cashu"
date: 2026-04-22
translationOf: /en/topics/tollgate.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocols
---

TollGate is een protocol voor het verkopen van netwerktoegang in ruil voor kleine, frequente betalingen met bearer assets. Een apparaat dat connectiviteit kan afschermen, zoals een WiFi-router, een Ethernet-switch of een Bluetooth-tether, fungeert als een TollGate die prijzen adverteert, [Cashu](/nl/topics/cashu/) ecash tokens accepteert en sessies beheert. Klanten betalen precies voor de minuten of megabytes die ze verbruiken. Er zijn geen accounts, geen abonnementen en geen KYC.

## Hoe Het Werkt

TollGate splitst verantwoordelijkheden in drie lagen. De protocollaag definieert de event-vormen en betalingssemantiek. De interfacelaag definieert hoe klant en gate die events uitwisselen. De mediumlaag beschrijft de fysieke link die het betaalde verkeer draagt. Een werkende TollGate combineert een specificatie uit elke laag, en sommige interfaces draaien over Nostr relays terwijl andere over plain HTTP draaien.

Op de protocollaag definieert [TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md) drie basisevents: een Advertisement kind dat prijzen en geaccepteerde mints opsomt, een Session kind dat bijhoudt hoeveel de klant heeft betaald en verbruikt, en een Notice kind voor out-of-band messaging. [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) legt Cashu-betalingen daarbovenop, zodat een klant ecash tokens van elke mint die de TollGate adverteert kan inwisselen en daarvoor sessiecredit ontvangt.

Op de interfacelaag definiëren [HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md) tot en met HTTP-03 het HTTP-oppervlak voor apparaten op beperkende besturingssystemen die niet eenvoudig WebSocket-verbindingen naar willekeurige relays kunnen openen, en [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md) definieert het Nostr-relaytransport voor clients die dat wel kunnen. Op de mediumlaag beschrijft [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md) hoe een captive-portal WiFi-opzet betalende klanten identificeert en routeert.

Omdat het betaalmiddel een bearer token is in plaats van een credential, heeft de klant geen voorafgaande internettoegang nodig om die te produceren. Een Cashu-token in een lokale wallet volstaat om de eerste minuut connectiviteit te kopen, waarna de klant zo nodig met meer tokens kan opwaarderen. TollGates kunnen ook uplink van elkaar kopen, zodat het bereik verder gaat dan een enkele operator.

## Waarom Het Belangrijk Is

Conventionele betaalde WiFi steunt op accounts, captive portals en betaalkaarten, die elk frictie en een dataspoor creëren. Het model van TollGate verandert connectiviteit in een commodity die elke router aan elke betalende klant kan verkopen zonder te weten wie die klant is. Die abstractie laat onafhankelijke operators hun eigen prijzen bepalen, hun eigen voorkeurmints accepteren en concurreren op dekking en kwaliteit in plaats van lock-in.

De [v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0) is de eerste getagde snapshot van deze specificaties. Die standaardiseert niet elk detail, maar fixeert genoeg van het oppervlak dat routerfirmware, clientwallets en multi-hop resellers tegen een stabiele referentie kunnen bouwen.

---

**Primaire bronnen:**
- [TollGate v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)
- [TIP-01: Base Events](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md)
- [TIP-02: Cashu payments](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md)
- [HTTP-01 through HTTP-03](https://github.com/OpenTollGate/tollgate/tree/v0.1.0)
- [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md)
- [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md)
- [TollGate repository](https://github.com/OpenTollGate/tollgate)

**Vermeld in:**
- [Newsletter #19: TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/)

**Zie ook:**
- [Cashu](/nl/topics/cashu/)
- [NIP-60: Cashu Wallet](/nl/topics/nip-60/)
