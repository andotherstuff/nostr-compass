---
title: "NIP-87 : Découverte des mints Ecash"
date: 2026-01-07
draft: false
categories:
  - Ecash
  - Discovery
  - Protocol
---

NIP-87 définit comment les mints ecash (Cashu et Fedimint) peuvent s'annoncer sur Nostr, et comment les utilisateurs peuvent recommander des mints à d'autres.

## Types d'événements

- **kind 38172** - Annonce de mint Cashu (publiée par les opérateurs de mint)
- **kind 38173** - Annonce Fedimint (publiée par les opérateurs de mint)
- **kind 38000** - Recommandation de mint (publiée par les utilisateurs)

## Comment ça fonctionne

1. **Les opérateurs de mint** publient l'URL de leur mint, les fonctionnalités supportées et le réseau (mainnet/testnet)
2. **Les utilisateurs** qui font confiance à un mint publient des recommandations avec des avis optionnels
3. **Les autres utilisateurs** interrogent les recommandations des personnes qu'ils suivent pour découvrir des mints de confiance

## Annonce de mint Cashu

```json
{
  "id": "<event-id>",
  "pubkey": "<mint-operator-pubkey>",
  "created_at": 1736200000,
  "kind": 38172,
  "tags": [
    ["d", "<mint-pubkey>"],
    ["u", "https://mint.example.com"],
    ["nuts", "1,2,3,4,5,6,7"],
    ["n", "mainnet"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

Le tag `nuts` liste les NUTs supportés (spécifications de Notation, Usage et Terminologie pour Cashu).

## Recommandations des utilisateurs

```json
{
  "id": "<event-id>",
  "pubkey": "<recommender-pubkey>",
  "created_at": 1736200000,
  "kind": 38000,
  "tags": [
    ["k", "38172"],
    ["d", "<mint-identifier>"],
    ["a", "38172:mint-pubkey:<d-tag>", "wss://relay"]
  ],
  "content": "J'utilise ce mint depuis des mois, très fiable",
  "sig": "<signature>"
}
```

Les utilisateurs peuvent inclure des avis dans le champ `content` et pointer vers des événements d'annonce de mint spécifiques.

---

**Sources principales :**
- [Spécification NIP-87](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Mentionné dans :**
- [Newsletter #4 : Versions](/fr/newsletters/2026-01-07-newsletter/#versions)

**Voir aussi :**
- [NIP-60 : Portefeuille Cashu](/fr/topics/nip-60/)
