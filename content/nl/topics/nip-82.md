---
title: "Voorgestelde NIP-82 (niet toegekend): catalogus van softwaretoepassingen"
date: 2026-06-17
lastmod: 2026-10-28
translationOf: /en/topics/nip-82.md
translationDate: 2026-10-28
draft: false
categories:
  - Proposals
  - Apps
---

De catalogus van softwaretoepassingen die op deze pagina wordt beschreven, is een voorstel dat nog wordt beoordeeld. Een geaccepteerde NIP is het niet. Het voorstel staat in [pull request #2526 van nostr-protocol/nips](https://github.com/nostr-protocol/nips/pull/2526), met de titel „Zapstore spec”. Op het moment van de laatste update van deze pagina is die pull request open en niet gemerged, en bevat de officiële master-branch van de NIPs geen bestand `82.md`. „NIP-82” is het label dat het voorstel voor zichzelf gebruikt. Het is geen officieel NIP-nummer. Event-kinds, tags en gedrag kunnen vóór een eventuele merge nog veranderen. Volgens de pull request vervangt deze de eerdere [pull request #1336](https://github.com/nostr-protocol/nips/pull/1336).

## Voorgestelde event-kinds

Het concept verdeelt een softwarecatalogus over verschillende soorten events:

- **Kind 32267, applicatie:** een adresseerbaar event dat een app beschrijft.
- **Kind 30063, release:** een adresseerbaar event voor één versie van die app. Het verwijst naar de assets van die versie.
- **Kind 3063, asset:** een gewoon event dat één downloadbaar bestand beschrijft.
- **Kind 30267, curatie:** een adresseerbare lijst die een curator publiceert om apps te groeperen of aan te bevelen.
- **Kind 30509, koppeling van ondertekeningscertificaat:** een adresseerbaar event dat een X.509-certificaat, zoals een APK-ondertekeningscertificaat, koppelt aan de Nostr-sleutel die software publiceert, zodat clients weten welke certificaten die publisher beheert. De tag `d` ervan is de SHA-256-hash van het DER-gecodeerde certificaat. Het event bevat een handtekening die met de privésleutel van het certificaat is gemaakt en een vervaltijd als Unix-tijdstempel, en kan de koppeling optioneel als ingetrokken markeren.
- **Kind 10067, relaylijst:** een vervangbare lijst van relays waar catalogus-events te vinden zijn.

## Platform, integriteit en geldigheid

Asset-events bevatten platform- en runtime-identificatoren, zodat een client alleen de bestanden kan tonen die bij een apparaat passen. Daarnaast bevat elk asset een bestandshash. Daarmee kan een client controleren of de gedownloade bytes overeenkomen met wat de publisher heeft ondertekend. Voor Android-pakketten neemt het concept de vingerafdruk van het ondertekeningscertificaat op. Een installer kan die vergelijken met het certificaat van een al geïnstalleerde app voordat hij een update aanbiedt. Voordat ze een Android-pakket installeren, horen clients (SHOULD) het event van kind 30509 op te halen aan de hand van de certificaathash. Ze horen de certificaathandtekening ervan te verifiëren tegen het in de APK ingebedde certificaat en tegen de publisher van het asset, en te controleren dat het bewijs niet verlopen of ingetrokken is.

## Grenzen van vertrouwen

Een geldige handtekening toont alleen aan dat een bepaalde sleutel een event heeft gepubliceerd. Ze bewijst niet dat de sleutel van de echte ontwikkelaar is, dat de software veilig is of dat de lijst van een curator te vertrouwen is. Over willekeurige publishers geeft het voorstel geen enkele garantie. Op welke publisher- en curatorsleutels ze vertrouwen, moeten clients en gebruikers zelf beslissen. Deze pagina claimt geen beveiligingsaudit en geen interoperabiliteit in productie.

## Verhouding tot NIP-89

Handler-events uit [NIP-89](/nl/topics/nip-89/) maken bekend welke applicaties welke event-kinds kunnen afhandelen. Dit voorstel beschrijft de softwareartefacten en waar je ze kunt verkrijgen, dus de twee behandelen afzonderlijke kwesties.

---

**Primaire bronnen:**
- [nostr-protocol/nips PR #2526: Zapstore spec](https://github.com/nostr-protocol/nips/pull/2526) (open, niet gemerged; vervangt [PR #1336](https://github.com/nostr-protocol/nips/pull/1336))

**Vermeld in:**
- [Nieuwsbrief #27: verslag van de release van Amethyst v1.12.0 (historische referentie)](/en/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Nieuwsbrief #46: catalogus van softwaretoepassingen voorgesteld als NIP-82](/nl/newsletters/2026-10-28-newsletter/#software-application-catalog-proposed-as-nip-82)

**Zie ook:**
- [NIP-89: applicatiehandlers](/nl/topics/nip-89/)
