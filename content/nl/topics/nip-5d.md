---
title: "NIP-5D: Nostr Web Applets"
date: 2026-04-08
translationOf: /en/topics/nip-5d.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Hosting
---

NIP-5D definieert een `postMessage`-protocol voor sandboxed webapplicaties ("napplets") die in iframes draaien en communiceren met een hostapplicatie ("shell"). Het breidt [NIP-5A](/nl/topics/nip-5a/) (Static Websites) uit met een runtime-communicatielaag die webapps toegang geeft tot Nostr-functionaliteit zonder de private key van de gebruiker bloot te stellen.

## Hoe Het Werkt

Een shellapplicatie laadt een napplet in een sandboxed iframe. De napplet communiceert met de shell via de `postMessage` API van de browser met een gestructureerd message-protocol. De shell levert de napplet Nostr-signing, relaytoegang en gebruikerscontext via dat messagekanaal. De iframe-sandbox voorkomt dat de napplet direct toegang krijgt tot de private key van de gebruiker, zodat de shell als gatekeeper voor alle Nostr-operaties fungeert.

## Gebruiksscenario's

- **Interactieve Nostr-apps**: Apps bouwen die Nostr-events lezen en schrijven zonder dat gebruikers hun nsec hoeven te plakken
- **App marketplace**: Interactieve webapplicaties distribueren via Nostr-events
- **Sandboxed extensions**: Functionaliteit aan Nostr-clients toevoegen via third-party napplets

---

**Primaire bronnen:**
- [NIP-5D PR #2303](https://github.com/nostr-protocol/nips/pull/2303) - Nostr Web Applets proposal

**Vermeld in:**
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/)

**Zie ook:**
- [NIP-5A (Static Websites)](/nl/topics/nip-5a/)
- [NIP-5C (Scrolls)](/nl/topics/nip-5c/)
