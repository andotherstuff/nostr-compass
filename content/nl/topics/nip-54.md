---
title: "NIP-54: Wiki"
date: 2025-12-31
translationOf: /en/topics/nip-54.md
translationDate: 2025-12-31
draft: false
categories:
  - Protocol
  - Inhoud
---

NIP-54 definieert kind 30818 als een adresseerbaar eventtype voor het maken van wiki-artikelen en encyclopedie-items op Nostr. Het maakt gedecentraliseerde, collaboratieve contentcreatie mogelijk waarbij meerdere auteurs over dezelfde onderwerpen kunnen schrijven.

## Hoe Het Werkt

Wiki-artikelen worden geïdentificeerd door een genormaliseerde `d` tag (het artikelonderwerp). Meerdere mensen kunnen artikelen over hetzelfde onderwerp schrijven, waardoor een gedecentraliseerde kennisbank zonder centrale autoriteit ontstaat.

**D Tag Normalisatie:**
- Alle letters naar kleine letters converteren
- Spaties naar koppeltekens converteren
- Leestekens en symbolen verwijderen
- Niet-ASCII-tekens en cijfers behouden

## Contentformaat

Artikelen gebruiken Asciidoc-markup met twee speciale functies:

- **Wikilinks** (`[[doelpagina]]`) - Links naar andere wiki-artikelen op Nostr
- **Nostr-links** - Verwijzingen naar profielen of events volgens NIP-21

## Artikelselectie

Wanneer meerdere versies van een artikel bestaan, prioriteren clients op basis van:

1. Reacties (NIP-25) die community-goedkeuring aangeven
2. Relay-lijsten (NIP-51) voor bronrangschikking
3. Contactlijsten (NIP-02) die aanbevelingsnetwerken vormen

## Collaboratieve Functies

- **Forking** - Afgeleide versies van artikelen maken
- **Merge-verzoeken** (kind 818) - Wijzigingen aan bestaande artikelen voorstellen
- **Doorverwijzingen** (kind 30819) - Oude onderwerpen naar nieuwe verwijzen
- **Deferentiemarkeringen** - Voorkeurversies van artikelen aangeven

---

**Primaire bronnen:**
- [NIP-54 Specificatie](https://github.com/nostr-protocol/nips/blob/master/54.md)

**Vermeld in:**
- [Nieuwsbrief #3: NIP-updates](/nl/newsletters/2025-12-31-newsletter/#nip-updates)

**Zie ook:**
- [NIP-51: Lijsten](/nl/topics/nip-51/)
- [NIP-02: Volglijst](/nl/topics/nip-02/)
