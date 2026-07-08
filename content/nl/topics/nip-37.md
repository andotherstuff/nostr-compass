---
title: "NIP-37: Draft Wraps"
date: 2026-07-01
draft: false
categories:
  - NIP
  - Drafts
  - Privacy
translationOf: /en/topics/nip-37.md
translationDate: 2026-07-01
---

NIP-37 definieert een versleuteld opslag-event voor niet-ondertekende concept-events van elk type. Een gebruiker die een long-form artikel opstelt, een aankomend agenda-event of een bericht dat zij later willen versturen, kan het concept opslaan op relays onder een kind `31234`-event, versleuteld voor de eigen sleutel met [NIP-44](/nl/topics/nip-44/). Het concept is herstelbaar vanuit elke client die de sleutel van de gebruiker in bezit heeft, en dezelfde NIP definieert een afzonderlijk `kind:10013`-lijstevent dat de relays benoemt waarop de gebruiker zijn privéconcepten wil opslaan.

## Hoe het werkt

Een draft wrap is een geparameteriseerd vervangbaar event van kind `31234`. Het niet-ondertekende concept-event wordt naar JSON geserialiseerd, NIP-44-versleuteld voor de eigen publieke sleutel van de ondertekenaar, en in `.content` geplaatst. Een `k`-tag verklaart het kind van het concept zodat een client concepten kan groeperen per event-type. Een `d`-tag bevat de concept-identifier zodat de wrap kan worden vervangen naarmate het concept zich ontwikkelt, en een NIP-40 `expiration`-tag wordt aanbevolen zodat oude concepten automatisch verlopen.

```json
{
  "kind": 31234,
  "tags": [
    ["d", "<identifier>"],
    ["k", "<kind of the draft event>"],
    ["expiration", "<unix-timestamp>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

Een leeggemaakt `.content`-veld geeft aan dat het concept is verwijderd.

## Checkpoints

Kind `1234` definieert checkpoints die toebehoren aan een bovenliggend `kind:31234`-event. Checkpoints bevatten een `a`-tag die verwijst naar het bovenliggende concept en stellen een client in staat om revisiegeschiedenis op te slaan naast het meest recente concept.

```json
{
  "kind": 1234,
  "tags": [
    ["a", "31234:<pubkey>:<identifier>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

## Relay-lijst voor privé-inhoud (kind 10013)

Kind `10013` is een vervangbaar event waarvan de tags de relays opsommen waarop de gebruiker privé-inhoud wil opslaan, inclusief draft wraps. Clients die kind `31234` publiceren, ZOUDEN moeten publiceren naar relays die vermeld staan in het kind `10013`-event van de gebruiker. Dit scheidt de relay-set die gebruikt wordt voor openbaar posten (NIP-65) van de relay-set die gebruikt wordt voor privé-inhoudsopslag, zodat een gebruiker privéconcepten kan vastzetten op een kleine set vertrouwde relays zonder die set bloot te geven in hun openbare outbox.

## Implementaties

- [Notedeck](https://github.com/damus-io/notedeck) - slaat privé-sync-relays op als een kind-10013-lijst (toegevoegd 2026-06)

---

**Primaire bronnen:**
- [NIP-37 Specificatie](https://github.com/nostr-protocol/nips/blob/master/37.md)
- [Notedeck-commit die privé-sync-relays opslaat als kind-10013](https://github.com/damus-io/notedeck) - Damus-team adopteert de specificatie voor desktop sync-relay-beheer

**Genoemd in:**
- [Newsletter #29: Notedeck](/nl/newsletters/2026-07-01-newsletter/#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments)

**Zie ook:**
- [NIP-44: Versioned Encryption](/nl/topics/nip-44/)
- [NIP-65: Relay List Metadata](/nl/topics/nip-65/)
