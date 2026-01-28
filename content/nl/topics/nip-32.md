---
title: "NIP-32: Labeling"
date: 2026-01-21
translationOf: /en/topics/nip-32.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-32 definieert een standaard voor het toevoegen van labels aan Nostr events, gebruikers en andere entiteiten. Labels bieden gestructureerde metadata die clients kunnen gebruiken voor categorisatie, contentwaarschuwingen, reputatiesystemen en moderatie.

## Hoe Het Werkt

Labels gebruiken kind 1985 events met een `L` tag die de label-namespace definieert en `l` tags die specifieke labels binnen die namespace toepassen. De gelabelde entiteit wordt gerefereerd via standaard tags zoals `e` (events), `p` (pubkeys) of `r` (relay URL's).

```json
{
  "kind": 1985,
  "tags": [
    ["L", "content-warning"],
    ["l", "nsfw", "content-warning"],
    ["e", "<event_id>"]
  ],
  "content": "Bevat expliciete beelden"
}
```

Het namespace-systeem voorkomt labelconflicten. Een "spam" label in de "ugc-moderation" namespace heeft andere semantiek dan "spam" in de "relay-report" namespace. Dit maakt het mogelijk dat meerdere labelsystemen naast elkaar bestaan zonder interferentie.

## Toepassingen

Contentmoderatiesystemen gebruiken labels om spam, illegale content of beleidsschendingen te markeren. Reputatiesystemen koppelen vertrouwensscores of verificatiestatus aan pubkeys. Mediaplatforms passen contentwaarschuwingen toe (NSFW, geweld, spoilers). Relay-operators gebruiken labels voor beroepen en geschillenbeslechting.

Het Trusted Relay Assertions-voorstel gebruikt NIP-32 labels voor relay-beroepen. Wanneer operators vertrouwensscores betwisten, publiceren ze kind 1985 events met `L` = `relay-appeal` en labeltypes zoals "spam", "censorship" of "score".

Clientimplementaties variëren in hoe ze labels consumeren. Sommige clients behandelen labels van gevolgde gebruikers als aanbevelingen, terwijl andere gespecialiseerde labeldiensten bevragen. Het gedecentraliseerde ontwerp laat gebruikers kiezen welke labelers ze vertrouwen.

---

**Primaire bronnen:**
- [NIP-32 Specificatie](https://github.com/nostr-protocol/nips/blob/master/32.md) - Labelingstandaard

**Vermeld in:**
- [Nieuwsbrief #6: NIP Updates](/nl/newsletters/2026-01-21-newsletter/#nip-updates)

**Zie ook:**
- [Trusted Relay Assertions](/nl/topics/trusted-relay-assertions/)
- [NIP-51: Lijsten](/nl/topics/nip-51/)
