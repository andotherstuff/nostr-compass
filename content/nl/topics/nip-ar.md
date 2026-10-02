---
title: "Buzz NIP-AR: Kanaalartefacten"
date: 2026-09-30
translationOf: /en/topics/nip-ar.md
translationDate: 2026-10-02
draft: false
categories:
  - Project Proposals
  - Collaboration
---

NIP-AR is de **projectspecifieke** specificatie van Buzz voor kanaalartefacten. Het label betekent hier niet dat ze is overgenomen door de `nostr-protocol/nips`-repository of door andere relays.

## Artefactmodel {#artifact-model}

Een artefact is een bewerkbaar record met een stabiele `d`-identiteit, één thuiskanaal in een `h`-tag en revisies als volledige momentopnamen die via `prev` aan elkaar zijn gekoppeld. Een relay accepteert een bewerking alleen als `prev` de huidige kop noemt. Twee concurrerende revisies kunnen daardoor niet allebei de volgende kop worden. De implementatie van Buzz gebruikt kind `45010` voor artefacten en een door de relay ondertekende kind `45011`-markering wanneer een artefact uit een kanaal wordt verplaatst. Het bronkanaal ziet de verwijdering zonder via die markering de bestemming te leren kennen.

De [merge van de Buzz-specificatie](https://github.com/block/buzz/pull/7791) beschrijft het model, en de [merge van de relay-implementatie](https://github.com/block/buzz/pull/7919) meldt tests voor conflictafhandeling, geschiedenisquery's, verplaatsingen en kanaalmachtigingen. Die merges leggen het gedrag van de projectbroncode vast, geen algemene Nostr-standaard of garantie voor een publieke uitrol.

---

**Primaire bronnen:**
- [Merge van de Buzz-specificatie voor kanaalartefacten](https://github.com/block/buzz/pull/7791)
- [Merge van de Buzz-implementatie voor kanaalartefacten](https://github.com/block/buzz/pull/7919)

**Genoemd in:**
- [Nieuwsbrief #42: kanaalartefacten van Buzz](/nl/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
