---
title: "NIP-32: Labeling"
date: 2026-01-21
translationOf: /en/topics/nip-32.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-32 definieert een standaard voor het koppelen van labels aan Nostr events, gebruikers en andere entiteiten. Labels bieden gestructureerde metadata die clients kunnen gebruiken voor categorisatie, contentwaarschuwingen, reputatiesystemen en moderatie.

## Hoe het werkt

Labels gebruiken kind 1985 events met een `L` tag die de label namespace definieert en `l` tags die specifieke labels binnen die namespace toepassen. De gelabelde entiteit wordt verwezen via standaard tags zoals `e` (events), `p` (pubkeys) of `r` (relay-URL's).

```json
{
  "kind": 1985,
  "tags": [
    ["L", "content-warning"],
    ["l", "nsfw", "content-warning"],
    ["e", "<event_id>"]
  ],
  "content": "Contains explicit imagery"
}
```

Het namespace-systeem voorkomt labelconflicten. Een "spam" label in de "ugc-moderation" namespace heeft een andere betekenis dan "spam" in de "relay-report" namespace. Daardoor kunnen meerdere labelsystemen naast elkaar bestaan zonder elkaar te storen.

## Waarom het belangrijk is

De belangrijkste ontwerpkeuze is dat labels beweringen zijn, geen feiten die in het protocol zijn ingebouwd. Een kind 1985 event zegt dat een actor iets in een bepaalde namespace heeft gelabeld. Clients hebben nog steeds een vertrouwensbeleid nodig om te bepalen welke labels ze tonen, verbergen of negeren.

Dat maakt NIP-32 bruikbaar voor veel meer dan moderatie. Dezelfde structuur kan contentwaarschuwingen, verificatiemarkeringen, classificatiesystemen of relay-reputatiedata dragen zonder alle clients tot een gedeelde wereldwijde woordenschat te dwingen.

## Toepassingen

Contentmoderatiesystemen gebruiken labels om spam, illegale content of beleidsschendingen te markeren. Reputatiesystemen koppelen vertrouwensscores of verificatiestatus aan pubkeys. Mediaplatforms passen contentwaarschuwingen toe zoals NSFW, geweld of spoilers. Relay-operators gebruiken labels voor beroepen en geschilafhandeling.

Het Trusted Relay Assertions-voorstel gebruikt NIP-32 labels voor relay-beroepen. Wanneer operators vertrouwensscores betwisten, publiceren ze kind 1985 events met `L = relay-appeal` en labels zoals `spam`, `censorship` of `score`.

## Interop-opmerkingen

Clients verschillen in hoe ze labels gebruiken. Sommige behandelen labels van gevolgde gebruikers als aanbevelingen, terwijl andere gespecialiseerde labeling services bevragen. Het gedecentraliseerde ontwerp laat gebruikers kiezen welke labelers ze vertrouwen, maar het betekent ook dat een label zonder zichtbare vertrouwenscontext misleidend kan zijn.

---

**Primaire bronnen:**
- [NIP-32 Specification](https://github.com/nostr-protocol/nips/blob/master/32.md) - Labelingstandaard

**Vermeld in:**
- [Nieuwsbrief #6: NIP Updates](/en/newsletters/2026-01-21-newsletter/#nip-updates)

**Zie ook:**
- [Trusted Relay Assertions](/nl/topics/trusted-relay-assertions/)
- [NIP-51: Lists](/nl/topics/nip-51/)
