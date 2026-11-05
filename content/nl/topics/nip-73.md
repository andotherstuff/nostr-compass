---
title: "NIP-73: Externe content-ID's"
date: 2026-02-04
draft: false
translationOf: /en/topics/nip-73.md
translationDate: 2026-11-05
categories:
  - Protocol
  - Discovery
  - Metadata
---

NIP-73 definieert een standaardmanier om binnen Nostr-events naar externe content te verwijzen. Het gebruikt `i`-tags voor de identifier zelf en `k`-tags voor het type identifier, zodat clients discussies kunnen groeperen rond hetzelfde boek, dezelfde website, podcastaflevering, locatie of hashtag of hetzelfde blockchainobject. De [huidige specificatie](https://github.com/nostr-protocol/nips/blob/master/73.md) is gemarkeerd als draft en optioneel.

## Hoe het werkt {#how-it-works}

Een event dat NIP-73 gebruikt, bevat een `i`-tag met een genormaliseerde externe identifier en een `k`-tag die de identifierfamilie benoemt. Clients kunnen relays via `i` bevragen op één exact onderwerp of via `k` op een hele familie. NIP-73 voegt geen eigen event kind toe. Reacties, recensies en andere events dragen de tags.

Tagfragment, geen volledig event:

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

Een webpagina zet haar genormaliseerde URL in `i` en stelt `k` in op `web`. De specificatie behandelt verschillende identifierfamilies, waaronder:

- genormaliseerde web-URL's zonder fragment
- ISBN's voor boeken
- ISAN's voor films
- DOI's
- geohashes en ISO 3166-codes voor landen of onderverdelingen
- GUID's van podcastfeeds, afleveringen en uitgevers
- hashtags
- identifiers van blockchaintransacties en -adressen

## Normalisatieregels {#normalization-rules}

Matching hangt af van identieke strings, dus de specificatie legt per familie één schrijfwijze vast. Voorbeelden uit de specificatie:

- geohashes gebruiken `geo:<value>` en moeten in kleine letters staan
- land- en onderverdelingscodes gebruiken `iso3166:<code>` en moeten in hoofdletters staan
- ISBN's laten koppeltekens weg
- DOI's staan in kleine letters
- web-URL's laten fragmenten weg
- hashes van blockchaintransacties gebruiken hex in kleine letters

Normalisatie legt vast hoe één identifier wordt geschreven. Ze voegt geen aliassen samen. Editiespecifieke ISBN's en URL's die naar verschillende strings normaliseren, blijven afzonderlijke identifiers, dus de discussie over één boek of artikel kan nog steeds verspreid raken over meerdere `i`-waarden.

## URL-hints {#url-hints}

Een `i`-tag kan als derde array-element een optionele URL-hint bevatten, de tweede waarde na de tagnaam. Een client zonder eigen renderer voor dat identifiertype kan de hint als terugvallink gebruiken.

Tagfragment: `["i", "isbn:9780765382030", "<url-hint>"]`

De auteur kiest de hint. Die maakt geen deel uit van de identiteit, bewijst geen eigendom en wijst geen canonieke site aan.

## Vertrouwen en context {#trust-and-context}

Twee events met dezelfde identifier komen in hetzelfde gesprek terecht, en meer stelt de gedeelde identifier niet vast. Een ondertekend event identificeert zijn auteur. Het authenticeert niet het boek, de site of de podcastuitgever waarnaar het verwijst, en het laat niet zien wie die beheert.

Wat een `i`-tag betekent, hangt af van het event. In reacties volgens [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md) markeren de hoofdletters `I`/`K` de rootscope en de kleine letters `i`/`k` de parent. Die threadstructuur komt uit NIP-22, en NIP-73 definieert geen kind voor reacties. [NIP-39](https://github.com/nostr-protocol/nips/blob/master/39.md) gebruikt `i` voor externe identiteiten in profielen, dus niet elke `i`-tag is een NIP-73-onderwerp.

[NIP-85](/nl/topics/nip-85/) Trusted Assertions kunnen ook NIP-73-identifiers als doel hebben, zoals boeken, websites, hashtags en locaties.

## Implementaties {#implementations}

Het bestand [nip73.rs bij commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs) van rust-nostr parseert bekende prefixen naar een getypeerde `ExternalContentId` en zet een optionele hint om in een getypeerde URL. Het schrijft het derde tag-element alleen als er een hint is. De tests behouden ISBN's met koppeltekens: de parser verwijdert het prefix en slaat de rest op zonder de normalisatie uit de specificatie toe te passen, dus getypeerd parsen garandeert geen canonieke strings. Chain-ID's blijven buiten de familie: `ethereum:100:tx:<hash>` wordt afgebeeld op `ethereum:tx`. Die revisie heeft geen `iso3166`-variant voor landen.

Het bestand [DisplayExternalId.kt bij commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt) van Amethyst stuurt geohash-, hashtag- en URL-identifiers naar speciale weergaven en toont andere ondersteunde typen als generieke scopechip. Een URL opent de eigen threadroute van de app voor die pagina. Met uitgeschakelde previews toont de normale weergave een eenvoudige linkchip en vraagt ze geen preview op. Met ingeschakelde previews kan het ophalen van een ontbrekende preview contact maken met de doelsite. Geen van beide bestanden laat zien hoe een uitgebrachte versie zich gedraagt.

---

**Primaire bronnen:**
- [NIP-73-specificatie](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Voegt ISO 3166-codes voor landen en onderverdelingen toe
- [rust-nostr nip73.rs bij commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs)
- [Amethyst DisplayExternalId.kt bij commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt)

**Genoemd in:**
- [Nieuwsbrief #47: NIP-verdieping](/nl/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)
- [Nieuwsbrief #45](/en/newsletters/2026-10-21-newsletter/#feather)
- [Nieuwsbrief #43](/en/newsletters/2026-10-07-newsletter/#protocol-and-spec-work)
- [Nieuwsbrief #37: augustus 2025](/en/newsletters/2026-08-26-newsletter/#august-2025)
- [Nieuwsbrief #8: NIP-updates](/en/newsletters/2026-02-04-newsletter/#nip-updates)
- [Nieuwsbrief #10: NIP-85-verdieping](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Nieuwsbrief #36: Reacties (NIP-22)](/en/newsletters/2026-08-19-newsletter/#comments-nip-22)
- [Nieuwsbrief #38: NIP-verdieping](/en/newsletters/2026-09-02-newsletter/#reactions-nip-25)
- [Nieuwsbrief #40: NIP-73-filters voor podcastmedium](/en/newsletters/2026-09-16-newsletter/#nip-73-proposes-podcast-medium-filters)
- [Nieuwsbrief #42: externe content in september 2024](/en/newsletters/2026-09-30-newsletter/#september-2024-posts-acquire-richer-context)

**Zie ook:**
- [NIP-31: Omgaan met onbekende event kinds](/nl/topics/nip-31/)
- [NIP-22: Reactie](/nl/topics/nip-22/)
- [NIP-39: Externe identiteiten in profielen](/nl/topics/nip-39/)
- [NIP-85: Trusted Assertions](/nl/topics/nip-85/)
