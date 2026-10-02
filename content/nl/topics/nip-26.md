---
title: "NIP-26: Gedelegeerd ondertekenen van events"
date: 2026-09-30
translationOf: /en/topics/nip-26.md
translationDate: 2026-10-02
draft: false
categories:
  - NIPs
  - Identity
---

NIP-26 beschrijft een manier waarop één Nostr-sleutel een andere sleutel kan machtigen om een beperkte reeks events te ondertekenen. De huidige specificatie is gemarkeerd als **draft** en **unrecommended**, dus ze legt een eerder ontwerp vast en is geen advies voor een nieuwe integratie.

## Hoe het werkt {#how-it-works}

De accountsleutel ondertekent een delegatietoken dat de gedelegeerde sleutel en de voorwaarden noemt. De voorwaarden kunnen event-kinds en `created_at`-tijden beperken. De gedelegeerde ondertekent het event met zijn eigen sleutel en voegt het token toe in een `delegation`-tag. Een lezer moet zowel de handtekening van het event als het delegatietoken tegen die voorwaarden verifiëren. Relays die het schema ondersteunen, kunnen ook op delegator zoeken.

Met dit model kan een applicatie publiceren zonder de primaire ondertekeningssleutel van het account te bezitten. De extra validatie en de zoekvereisten voor relays verklaren waarom implementaties een gewone handtekening op een event niet als voldoende bewijs van een gedelegeerde identiteit kunnen behandelen. De [huidige specificatie](https://github.com/nostr-protocol/nips/blob/master/26.md) markeert de aanpak uitdrukkelijk als unrecommended.

---

**Primaire bronnen:**
- [NIP-26-specificatie en huidige status](https://github.com/nostr-protocol/nips/blob/master/26.md)
- [Tekst over gedelegeerd ondertekenen uit september 2022](https://github.com/nostr-protocol/nips/commit/b62aa418d)

**Genoemd in:**
- [Nieuwsbrief #42: september 2022](/nl/newsletters/2026-09-30-newsletter/#september-2022-chat-and-delegated-actions-enter-the-specifications)
