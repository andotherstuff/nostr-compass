---
title: "Trusted Relay Assertions"
date: 2026-01-21
draft: false
categories:
  - Protocol
  - Relays
---

Trusted Relay Assertions is een concept NIP voorstel voor het standaardiseren van relay trust scoring en reputatiebeheer. De specificatie introduceert kind 30385 events waarin assertion providers trust scores publiceren berekend uit waargenomen metriek, operator reputatie en gebruiksrapportages.

## Hoe Het Werkt

Het voorstel vult een gat in het relay ecosysteem. Terwijl [NIP-11](/nl/topics/nip-11/) bepaalt wat relays over zichzelf claimen en [NIP-66](/nl/topics/nip-66/) meet wat we observeren, standardiseert Trusted Relay Assertions wat we concluderen over relay betrouwbaarheid.

Assertion providers berekenen scores over drie dimensies. Betrouwbaarheid meet beschikbaarheid, herstelingsnelheid, consistentie en latentie. Kwaliteit evalueert beleidsdocumentatie, TLS veiligheid en operator verantwoording. Toegankelijkheid beoordeelt toegangsbarrières, jurisdictie vrijheid en surveillancerisico. Een overall trust score (0-100) combineert deze componenten met gewichten: 40% betrouwbaarheid, 35% kwaliteit, 25% toegankelijkheid.

Elke assertion omvat vertrouwensniveaus (laag, gemiddeld, hoog) gebaseerd op observatieaantallen. Operator verificatie gebruikt meerdere methoden: cryptografisch bewijs via ondertekende NIP-11 documenten, DNS TXT records of .well-known bestanden. De spec integreert Web of Trust via operator trust scores. Beleidsclassificatie helpt gebruikers geschikte relays te vinden: open, gemodereerd, curated of gespecialiseerd.

Gebruikers declareren vertrouwde assertion providers via kind 10385 events. Clients bevragen meerdere providers en vergelijken scores. Het voorstel omvat een appeals proces waar relay operators scores kunnen aanvechten met [NIP-32](/nl/topics/nip-32/) labeling events.

## Use Cases

Voor [NIP-46](/nl/topics/nip-46/) remote signers helpen trust assertions gebruikers onbekende relays in verbindingsURI's geïnformeerd te evalueren voordat verbindingen worden geaccepteerd. Gecombineerd met [NIP-65](/nl/topics/nip-65/) relay lijsten, kunnen clients geïnformeerde relay selectiebeslissingen nemen gebaseerd op zowel gebruikersvoorkeur als derde partij trust evaluaties.

De specificatie complementeert bestaande relay discovery mechanismen. [NIP-66](/nl/topics/nip-66/) biedt discovery (wat bestaat), dit voorstel voegt evaluatie (wat goed is) toe. Samen enableren zij geïnformeerde relay selectie in plaats van te vertrouwen op hardcoded defaults of mondeling aanbevelingen.

---

**Primaire bronnen:**
- [Draft NIP Document](https://nostr.com/nevent1qqsqjymvcp6ch3ps3fqsxljf6j8u3adz64ucw8npnzuj3cn6dekn0gspz9mhxue69uhkummnw3ezumrpdejz7qg3waehxw309ahx7um5wgh8w6twv5hsyga3qg) - Kind 30817 event die de specificatie voorstelt

**Vermeld in:**
- [Newsletter #6: Nieuws](/nl/newsletters/2026-01-21-newsletter/#trusted-relay-assertions-a-new-approach-to-relay-trust)
- [Newsletter #6: NIP Updates](/nl/newsletters/2026-01-21-newsletter/#nip-updates)

**Zie ook:**
- [NIP-11: Relay Informatiedocument](/nl/topics/nip-11/)
- [NIP-66: Relay Discovery en Liveness Monitoring](/nl/topics/nip-66/)
- [NIP-32: Labeling](/nl/topics/nip-32/)
