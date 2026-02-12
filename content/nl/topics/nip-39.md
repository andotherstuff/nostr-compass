---
title: "NIP-39: Externe Identiteiten in Profielen"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Identity
---

NIP-39 definieert hoe mensen externe identiteitsclaims koppelen aan hun Nostr-profielen met `i` tags. Die tags verbinden Nostr pubkey met accounts op externe platformen zoals GitHub, Twitter of DNS-domeinen.

## Werking

Identiteitsclaims worden gepubliceerd als `i` tags. Elke tag bevat platformidentifier en proof-URL waar het externe account teruglinkt naar de Nostr pubkey, waardoor bidirectionele verificatie ontstaat:

```json
{
  "tags": [
    ["i", "github:username", "https://gist.github.com/username/proof"],
    ["i", "twitter:handle", "https://twitter.com/handle/status/proof_tweet_id"]
  ]
}
```

Toepassingen verifiëren claims door de proof-URL op te halen en te controleren of die de Nostr pubkey van de eigenaar bevat. Zo ontstaat een web van identiteitsverbindingen zonder gecentraliseerde verificatiediensten.

## Recente Wijzigingen

Per februari 2026 heeft [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) identity tags geextraheerd uit kind 0 (gebruikersmetadata) events naar toegewijde kind 10011. De verplaatsing was onderdeel van vitorpamplona's kind 0 afslankingscampagne, gemotiveerd door lage adoptie: bijna geen toepassingen implementeerden `i` tag-verificatie, terwijl elke kind 0-fetch de overhead droeg. De nieuwe kind 10011 laat geinteresseerde toepassingen identiteitsclaims apart ophalen.

---

**Primaire bronnen:**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)

**Vermeld in:**
- [Nieuwsbrief #9: NIP-Updates](/nl/newsletters/2026-02-11-newsletter/#nip-updates)

**Zie ook:**
- [NIP-05: DNS-Gebaseerde Verificatie](/nl/topics/nip-05/)
