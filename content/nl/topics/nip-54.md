---
title: "NIP-54: Wiki"
date: 2025-12-31
translationOf: /en/topics/nip-54.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Inhoud
---

NIP-54 definieert kind `30818` voor wiki-achtige artikelen op Nostr. Meerdere auteurs kunnen items over hetzelfde onderwerp publiceren, dus clients hebben rangschikkings- en vertrouwensheuristieken nodig in plaats van een enkele canonieke pagina.

## Hoe Het Werkt

Wiki-artikelen worden geïdentificeerd door een genormaliseerde `d` tag die het onderwerp vertegenwoordigt. Meerdere mensen kunnen items met hetzelfde genormaliseerde onderwerp publiceren, waardoor een open wiki zonder centrale redactie ontstaat.

**D-tag-normalisatie:**
- Zet letters met hoofdletter- en kleinelettervarianten om naar lowercase
- Zet witruimte om in koppeltekens
- Verwijder leestekens en symbolen
- Voeg herhaalde koppeltekens samen en verwijder leidende of afsluitende koppeltekens
- Behoud niet-ASCII-letters en cijfers

Die normalisatieregel is belangrijk voor interoperabiliteit. Als twee clients dezelfde titel anders normaliseren, vragen ze verschillende onderwerpen op en raakt de verzameling artikelen gefragmenteerd.

## Contentformaat

De samengevoegde specificatie gebruikt Asciidoc-markup met twee extra functies:

- **Wikilinks** (`[[target page]]`) - Links naar andere wiki-artikelen op Nostr
- **Nostr-links** - Verwijzingen naar profielen of events volgens NIP-21

Er is een overstap naar Djot voorgesteld, maar die heeft Asciidoc in de canonieke NIP per maart 2026 nog niet vervangen.

## Artikelselectie

Wanneer er meerdere versies van een artikel bestaan, kunnen clients prioriteren op basis van:

1. Reacties (NIP-25) die goedkeuring uit de gemeenschap aangeven
2. Relay-lijsten (NIP-51) voor bronrangschikking
3. Contactlijsten (NIP-02) die aanbevelingsnetwerken vormen

In de praktijk betekent dit dat NIP-54 niet alleen een contentformaat is. Het is ook een client-beleidsprobleem. Twee clients kunnen verschillende "beste" artikelen voor hetzelfde onderwerp tonen en toch allebei aan de specificatie voldoen.

## Collaboratieve Functies

- **Forking** - Afgeleide versies van artikelen maken
- **Merge requests** (kind 818) - Wijzigingen op bestaande artikelen voorstellen
- **Redirects** (kind 30819) - Oude onderwerpen naar nieuwe verwijzen
- **Deference markers** - Voorkeursversies van artikelen aangeven

Forks en deference markers laten auteurs betere versies erkennen zonder hun eigen werk te verwijderen. Dat is belangrijk in een netwerk waar oude revisies op veel relays beschikbaar kunnen blijven.

---

**Primaire bronnen:**
- [NIP-54-specificatie](https://github.com/nostr-protocol/nips/blob/master/54.md)
- [PR #2177: Geinternationaliseerde d-tag-normalisatie](https://github.com/nostr-protocol/nips/pull/2177)

**Vermeld in:**
- [Nieuwsbrief #3: NIP-updates](/en/newsletters/2025-12-31-newsletter/#nip-updates)
- [Nieuwsbrief #15: Open PR's](/en/newsletters/2026-03-04-newsletter/#open-prs-and-project-updates)

**Zie ook:**
- [NIP-51: Lijsten](/nl/topics/nip-51/)
- [NIP-02: Volglijst](/nl/topics/nip-02/)
