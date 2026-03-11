---
title: "NIP-39: Externe identiteiten in profielen"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Identity
---

NIP-39 definieert hoe gebruikers externe identiteitsclaims aan hun Nostr-profielen koppelen met `i` tags. Deze tags verbinden een Nostr pubkey met accounts op externe platforms zoals GitHub, Twitter, Mastodon of Telegram.

## Hoe het werkt

Gebruikers publiceren identiteitsclaims in kind 10011 events als `i` tags. Elke tag bevat een `platform:identity`-waarde plus een proof pointer waarmee een client de claim kan verifiëren:

```json
{
  "kind": 10011,
  "tags": [
    ["i", "github:username", "gist-id"],
    ["i", "twitter:handle", "tweet-id"]
  ]
}
```

Clients reconstrueren de proof-URL op basis van het platform en de proof-waarde, en controleren daarna of de externe post de `npub` van de gebruiker bevat. Daardoor blijft de claim overdraagbaar tussen clients zonder een centrale verifier nodig te hebben.

## Bewijsmodel

Het belangrijke detail is dat NIP-39 controle over twee identiteiten tegelijk bewijst: de Nostr-sleutel en het externe account. Als een van beide kanten van dat bewijs verdwijnt, wordt de verificatie zwakker. Een verwijderde gist of tweet maakt het historische event niet ongeldig, maar verwijdert wel het live bewijs waarop de meeste clients vertrouwen.

Een ander nuttig implementatiedetail is de fetch-strategie. Omdat claims nu buiten kind 0 leven, kunnen clients beslissen of ze die alleen op profiel-detailpagina's opvragen, alleen voor gevolgde gebruikers, of helemaal niet. Dat voorkomt extra belasting op het toch al drukke kind 0-pad.

## Implementaties

- [Amethyst PR #1747](https://github.com/vitorpamplona/amethyst/pull/1747) - publiceert externe identiteiten als aparte kind 10011-events
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - voegt een expliciete verwijzing naar kind 10011 toe aan de NIP-set

## Huidige status

Volgens de huidige spec leven identiteitsclaims in aparte kind 10011 events in plaats van in kind 0 metadata. Die scheiding kwam voort uit de bredere inspanning om kind 0 profile fetches slanker te maken.

---

**Primaire bronnen:**
- [NIP-39: Externe identiteiten in profielen](https://github.com/nostr-protocol/nips/blob/master/39.md)
- [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) - Verplaatste identiteitsclaims uit kind 0
- [PR #2256](https://github.com/nostr-protocol/nips/pull/2256) - Voegde een expliciete verwijzing naar kind 10011 toe

**Vermeld in:**
- [Nieuwsbrief #9: NIP-updates](/nl/newsletters/2026-02-11-newsletter/#nip-updates)
- [Nieuwsbrief #12: Amethyst](/nl/newsletters/2026-03-04-newsletter/#amethyst-nip-39-nip-c0-nip-66)
- [Nieuwsbrief #13: NIP-updates](/nl/newsletters/2026-03-11-newsletter/#nip-updates)

**Zie ook:**
- [NIP-05: DNS-gebaseerde verificatie](/nl/topics/nip-05/)
