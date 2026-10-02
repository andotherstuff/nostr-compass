---
title: "Buzz NIP-FI: Gefedereerde identiteitsverklaringen"
date: 2026-09-30
translationOf: /en/topics/nip-fi.md
translationDate: 2026-10-02
draft: false
categories:
  - Project Proposals
  - Identity
  - Relays
---

NIP-FI is de **projectspecifieke** specificatie van Buzz voor gefedereerde identiteitsverklaringen. De naam impliceert geen adoptie door de `nostr-protocol/nips`-repository en geen interoperabiliteit met relays buiten Buzz.

## HTTP-toegang {#http-ingress}

Voor beschermde HTTP-verzoeken in de handhavingsmodus koppelt Buzz een gefedereerde identiteitsverklaring aan een door NIP-98 ondertekend autorisatie-event. De openbare Nostr-sleutel die door de HTTP-handtekening wordt bewezen, moet overeenkomen met de sleutel die in de verklaring wordt genoemd. Ontbrekend, niet-overeenkomend of niet-verifieerbaar bewijs wordt geweigerd. Buzz gebruikt deze koppeling om de autorisatiebeslissing van een externe identiteitsuitgever te verbinden met de Nostr-sleutel die het verzoek doet.

De [revisie van de projectspecificatie](https://github.com/block/buzz/pull/7254) definieert het handhavingsmodel. De [gemergede implementatie voor HTTP-toegang](https://github.com/block/buzz/pull/7264) dekt de beschermde HTTP-oppervlakken van Buzz, waaronder de paden voor de relaybrug, media, workflows en Git. De merge meldt broncodetests; ze betekent niet dat een andere Nostr-relay hetzelfde beleid implementeert.

---

**Primaire bronnen:**
- [Revisie van de Buzz NIP-FI-specificatie](https://github.com/block/buzz/pull/7254)
- [Implementatie van HTTP-toegang in Buzz](https://github.com/block/buzz/pull/7264)

**Genoemd in:**
- [Nieuwsbrief #42: identiteitscontroles van Buzz](/nl/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
