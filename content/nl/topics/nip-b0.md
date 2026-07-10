---
title: "NIP-B0: Web-bookmarks"
date: 2026-05-28
draft: false
categories:
  - Protocol
  - Social
translationOf: /en/topics/nip-b0.md
translationDate: 2026-07-01
---

NIP-B0 definieert een geparameteriseerd vervangbaar event (kind 39701) dat web-bookmarks publiceert als first-class Nostr-events. Het voorstel stelt gebruikers in staat samengestelde bookmark-collecties op te bouwen die kunnen worden ontdekt, gezapt en opnieuw gepubliceerd via clients zonder afhankelijk te zijn van een centrale bookmark-dienst.

## Hoe het werkt

Een bookmark is een kind 39701-event waarvan de `d`-tag de canonieke URL is van de gemarkeerde pagina. Vervangbare semantiek stelt de auteur in staat de eigen bookmark voor die URL bij te werken (opnieuw taggen, de titel aanpassen, als verouderd markeren) zonder duplicate events te produceren. Het content-veld bevat de notitie van de auteur over de bookmark; tags bevatten titel, beschrijving, afbeelding en `t`-onderwerptags voor discovery.

```json
{
  "kind": 39701,
  "tags": [
    ["d", "https://example.com/an-article-worth-saving"],
    ["title", "Article Title"],
    ["t", "nostr"],
    ["t", "protocol"],
    ["published_at", "1717000000"]
  ],
  "content": "Useful primer on the topic.",
  "pubkey": "...",
  "sig": "..."
}
```

De `d`-tag identificeert de bookmark uniek per auteur, zodat twee gebruikers dezelfde URL kunnen bookmarken met hun eigen annotaties en tag-sets.

## Discovery en curatie

Omdat elke bookmark een first-class event is, kan elke Nostr-client een feed van bookmarks weergeven door zich te abonneren op kind 39701-events, gefilterd op tags of auteurs. Op curatoren gedreven workflows worden vanzelfsprekend: een curator publiceert een lijst met bookmarks, lezers volgen de pubkey van de curator, en de bookmarks stromen door elke relay die ze draagt. Er is geen centrale directory.

## Implementaties

- [deepmarks-public](https://github.com/ostermayer/deepmarks-public), een referentie-webclient met een drie-boxarchitectuur (curator, indexer, viewer) en een tier-systeem gefinancierd door directe NIP-57 zaps naar de curator. Implementeert NIP-B0 naast NIP-07, NIP-46, NIP-57, NIP-44, NIP-98, NIP-65 en Blossom BUD-01/BUD-04 voor bestandsopslag.

## Vertrouwens- en beveiligingsnotities

- Bookmarks zijn standaard openbaar; publiceer op deze manier geen privé-leeslijsten
- Herpublicatie is afhankelijk van relays die de events blijven dragen; kortstondige relays laten bookmarks vallen
- De `published_at`-tag is door de uitgever geclaimd, niet verifieerbaar

---

**Primaire bronnen:**
- [Voorgestelde NIP-B0 specificatie](https://github.com/nostr-protocol/nips/pull/2089), volgt het voorgestelde kind 39701 web-bookmark-event
- [deepmarks-public](https://github.com/ostermayer/deepmarks-public), referentie-implementatie met curator-tier-systeem

**Genoemd in:**
- [Newsletter #24: deepmarks NIP-B0 bookmarks with curator-monetized publishing](/nl/newsletters/2026-05-28-newsletter/#deepmarks-nip-b0-bookmarks-with-curator-monetized-publishing)
- [Newsletter #27: Also shipped](/nl/newsletters/2026-06-17-newsletter/#also-shipped)

**Zie ook:**
- [NIP-57: Lightning Zaps](/nl/topics/nip-57/)
- [NIP-65: Relay List Metadata](/nl/topics/nip-65/)
