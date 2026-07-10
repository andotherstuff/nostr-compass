---
title: "NIP-82: Software-applicaties"
date: 2026-06-17
draft: false
categories:
  - Discovery
  - Apps
translationOf: /en/topics/nip-82.md
translationDate: 2026-07-01
---

NIP-82 definieert een software-applicatie-event zodat Nostr-clients applicaties (Android APK's, iOS-apps, web-apps, desktop-binaries) kunnen weergeven als first-class objecten in feeds en discovery-oppervlakken. De specificatie vervangt de oudere aanpak waarbij apps werden beschreven via generieke kind 1-notes of [NIP-89](/nl/topics/nip-89/) handler-aanbevelingen door een specifiek, gestructureerd event dat applicatiemetadata, screenshots, repositorylinks en auteursidentiteit meedraagt.

## Hoe het werkt

Een NIP-82 software-applicatie is een enkel vervangbaar event dat wordt geadresseerd door de auteurs-pubkey en een `d`-tag. Het event bevat:

- `name`-, `description`-, `icon`- en `image`-tags voor weergave
- `repository`- en `web`-tags voor bron- en homepage-URL's
- Een `platforms`-tag die de ondersteunde targets opsomt (android, ios, web, linux, macos, windows)
- `download`-tags voor elke platformspecifieke binary of web-URL
- `screenshots`-tags die afbeeldings-URL's van de applicatie-screenshots bevatten
- `t`-onderwerptags voor categorisatie
- Een `version`-tag voor de huidige gepubliceerde versie

Een client die door een NIP-82-feed bladert, kan de applicatiekaart tonen, linken naar de canonieke repository en screenshots naar voren brengen zonder terug te vallen op het scrapen van een Nostr long-form post of een externe app-store. De auteurs-pubkey is de bron van waarheid voor de applicatie, zodat een client kan verifiëren dat de uitgever overeenkomt met de verwachte ontwikkelaarsidentiteit voordat een downloadlink wordt gepromoot.

## Feed-semantiek

NIP-82-events zijn adresseerbaar, dus elke applicatie heeft één canoniek vervangbaar event per auteur. Een ontwikkelaar die een nieuwe versie publiceert, vervangt het vorige event ter plekke, en abonnees zien de update zonder event-geschiedenis te hoeven beheren. Clients die een changelog willen tonen, kunnen zich abonneren op het adresseerbare event en versie-updates weergeven als activiteit op het applicatie-oppervlak.

De specificatie sluit aan bij [NIP-89](/nl/topics/nip-89/) (Application Handlers): een NIP-82-event beschrijft de applicatie als een artefact, terwijl een NIP-89-event beschrijft dat de applicatie specifieke event-kinds kan verwerken. Clients kunnen het ene zonder het andere gebruiken, maar het paar biedt een discovery-oppervlak (NIP-82) en een delegatie-oppervlak (NIP-89) die samen werken.

## Implementaties

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) levert een speciale NIP-82 software-applicatiefeed met een detailscherm, auteursinformatie en screenshots ([PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036), [PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078), [PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200))

---

**Primaire bronnen:**
- [NIP-82 Specificatie](https://github.com/nostr-protocol/nips/blob/master/82.md)
- [Amethyst PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036) - Ondersteuning voor NIP-82 software-applicaties toegevoegd met een speciale feed
- [Amethyst PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078) - Speciaal detailscherm voor NIP-82 software-apps toegevoegd
- [Amethyst PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200) - NIP-82 software-app-UI verbeterd met auteursinformatie en screenshots

**Genoemd in:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/nl/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**Zie ook:**
- [NIP-89: Application Handlers](/nl/topics/nip-89/)
