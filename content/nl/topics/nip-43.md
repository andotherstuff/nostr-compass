---
title: "NIP-43: Relay Access Metadata and Requests"
date: 2026-03-18
translationOf: /en/topics/nip-43.md
translationDate: 2026-04-01
draft: false
categories:
  - Protocol
  - Relay
  - Access Control
---

NIP-43 definieert hoe relays lidmaatschapsinformatie publiceren en hoe gebruikers toelating, uitnodigingen of verwijdering van beperkte relays kunnen aanvragen. Het geeft relay-toegangscontrole een standaard eventsurface in plaats van elke privé of semi-privé relay te dwingen zijn eigen toelatingsprotocol te verzinnen.

## Hoe Het Werkt

De specificatie combineert meerdere event kinds:

- kind `13534` publiceert een relay-lidmaatschapslijst
- kind `8000` kondigt aan dat een lid is toegevoegd
- kind `8001` kondigt aan dat een lid is verwijderd
- kind `28934` laat een gebruiker een toetredingsverzoek indienen met een claimcode
- kind `28935` laat een relay op verzoek een uitnodigingscode retourneren
- kind `28936` laat een gebruiker verzoeken dat zijn eigen toegang wordt ingetrokken

Lidmaatschapsstatus wordt opzettelijk niet afgeleid uit één enkel event. Een client moet mogelijk zowel de relay-ondertekende lidmaatschapsevents als de eigen events van het lid raadplegen voordat wordt bepaald of toegang actueel is.

## Waarom Het Belangrijk Is

NIP-43 geeft beperkte relays een standaardmanier om toelating en lidmaatschapsstatus uit te drukken. Dit is belangrijk voor groepssystemen, uitnodiging-only gemeenschappen en relays die machineleesbare onboarding nodig hebben zonder terug te vallen op out-of-band webformulieren of handmatige operatorworkflows.

De open verduidelijking in [PR #2267](https://github.com/nostr-protocol/nips/pull/2267) verscherpt één praktisch punt: relays moeten één autoritatieve lidmaatschapsstatus per pubkey bijhouden. Dit helpt clients dubbelzinnige replay-geschiedenissen te voorkomen waarbij een oud toevoeg- of verwijderevent verkeerd kan worden gelezen als huidige status.

## Interopnotities

NIP-43 is afhankelijk van het feit dat de relay ondersteuning adverteert via zijn [NIP-11](/nl/topics/nip-11/) document. Toetredingsverzoeken, uitnodigingsverzoeken en vertrekverzoeken mogen alleen worden verstuurd naar relays die expliciet aangeven dit NIP te ondersteunen.

Omdat de events zich tegelijkertijd in relay-gecontroleerde en gebruiker-gecontroleerde ruimtes bevinden, hebben implementaties duidelijke conflictregels nodig. Daarom is de verduidelijking van lidmaatschapsstatus belangrijker dan het op het eerste gezicht lijkt.

---

**Primaire bronnen:**
- [NIP-43 Specificatie](https://github.com/nostr-protocol/nips/blob/master/43.md)
- [PR #2267](https://github.com/nostr-protocol/nips/pull/2267) - Verduidelijking lidmaatschapsstatusafhandeling

**Vermeld in:**
- [Newsletter #14: NIP Updates](/nl/newsletters/2026-03-18-newsletter/#nip-updates)

**Zie ook:**
- [NIP-11: Relay Information Document](/nl/topics/nip-11/)
- [NIP-42: Authentication of Clients to Relays](/nl/topics/nip-42/)
