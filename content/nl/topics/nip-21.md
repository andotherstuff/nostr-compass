---
title: "NIP-21: nostr: URI-schema"
date: 2026-04-22
translationOf: /en/topics/nip-21.md
translationDate: 2026-04-23
draft: false
categories:
  - Protocol
  - Interoperabiliteit
---

NIP-21 definieert het `nostr:` URI-schema, een standaardmanier waarop applicaties, websites en besturingssystemen interesse kunnen registreren in het openen van Nostr-identificatie zoals `npub`, `nprofile`, `nevent` en `naddr` via welke Nostr-client de gebruiker als handler heeft ingesteld.

## Hoe het werkt

Een `nostr:` URI is het schema-prefix gevolgd door een van de [NIP-19](/nl/topics/nip-19/) bech32-identificaties behalve `nsec`. Clients en besturingssystemen behandelen het schema op dezelfde manier als `mailto:` of `tel:`: registratie als handler stelt de gebruiker in staat om op een `nostr:` link ergens in het systeem te klikken en deze in hun gekozen Nostr-client te openen.

Voorbeelden uit de specificatie:

- `nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9` wijst naar een gebruikersprofiel
- `nostr:nprofile1...` wijst naar een gebruikersprofiel met ingebedde relayhinten
- `nostr:nevent1...` wijst naar een specifieke event met relayhinten
- `nostr:naddr1...` wijst naar een geparameteriseerde vervangbare event (zoals een artikel met lange vorm)

## HTML-pagina's koppelen aan Nostr-entiteiten

NIP-21 specificeert ook twee nuttige `<link>` -conventies voor webpagina's die overeenkomen met Nostr-entiteiten. Een pagina die dezelfde inhoud bevat als een Nostr-event (bijvoorbeeld een blogpost weergegeven uit een [NIP-23](/nl/topics/nip-23/) `kind:30023` artikel) kan een `<link rel="alternate">` bevatten die naar de Nostr-URI wijst. Een profielpagina kan een `<link rel="me">` of `<link rel="author">` bevatten die naar een `nprofile` wijst om Nostr-gebaseerd auteurschap te beweren.

## Waarom het belangrijk is

Het schema is de interoperabiliteitslaag waarmee elke Nostr-identifier een werkende link buiten de UI van een enkele client wordt. Browserextensies, mobiele OS-handlers en desktopshells kunnen allemaal `nostr:` URI's doorsturen naar welke client de gebruiker ook heeft geïnstalleerd, wat het mogelijk maakt om een profiel of event te delen door een URI overal in te plakken zonder het vermogen te verliezen om deze op een Nostr-native manier te openen.

## Implementaties

Ondersteuning voor `nostr:` URI's is breed verdeeld over het client-ecosysteem, inclusief de belangrijkste web-, mobiele en desktopclients van Nostr. Browserextensies zoals [nos2x](https://github.com/fiatjaf/nos2x) en [Alby](https://github.com/getAlby/lightning-browser-extension) verwerken URI-registratie op desktopbrowsers.

---

**Primaire bronnen:**

- [NIP-21-specificatie](https://github.com/nostr-protocol/nips/blob/master/21.md)

**Genoemd in:**

- [Nieuwsbrief #19: Nostrability migreert naar NIP-34](/nl/newsletters/2026-04-22-newsletter/#nostrability-migreert-naar-nip-34-en-opent-19-per-nip-interop-trackers)

**Zie ook:**

- [NIP-19: bech32-gecodeerde entiteiten](/nl/topics/nip-19/)
- [NIP-23: Inhoud met lange vorm](/nl/topics/nip-23/)
