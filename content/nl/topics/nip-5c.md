---
title: "NIP-5C: Scrolls (WASM Programs)"
date: 2026-04-08
translationOf: /en/topics/nip-5c.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Hosting
---

NIP-5C (voorheen NIP-A5) definieert conventies voor het publiceren, ontdekken en uitvoeren van WebAssembly-programma's ("scrolls") op Nostr. WASM-binaries worden als Nostr-events opgeslagen, zodat elke client ze kan ophalen en uitvoeren in een sandboxed runtime.

## Hoe Het Werkt

Ontwikkelaars publiceren WASM-programma's als Nostr-events die de gecompileerde binary bevatten. Clients ontdekken deze programma's via standaard Nostr-queries, downloaden de WASM-binary uit het event en voeren die uit in een sandboxed WebAssembly-runtime. De sandbox voorkomt dat scrolls direct toegang krijgen tot het hostsysteem en beperkt ze tot de mogelijkheden die de runtime expliciet aanbiedt.

## Gebruiksscenario's

- **Portable compute**: Programma's draaien op elke client die WASM-uitvoering ondersteunt
- **Decentralized app distribution**: Applicaties publiceren en ontdekken zonder app stores
- **Composable tools**: Scrolls aan elkaar koppelen voor complexe workflows

## Demo

Een [demo app](https://nprogram.netlify.app/) laat scrolls in de browser draaien, met voorbeeldprogramma's die als Nostr-events zijn gepubliceerd.

---

**Primaire bronnen:**
- [NIP-5C PR #2281](https://github.com/nostr-protocol/nips/pull/2281) - Scrolls (WASM Programs) proposal

**Vermeld in:**
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/)
- [Newsletter #19: NIP-5D applets proposal](/en/newsletters/2026-04-22-newsletter/)

**Zie ook:**
- [NIP-5D (Web Applets)](/nl/topics/nip-5d/)
- [NIP-5A (Static Websites)](/nl/topics/nip-5a/)
