---
title: "NIP-87 : Découvrabilité des mints Ecash"
date: 2026-01-07
translationOf: /en/topics/nip-87.md
translationDate: 2026-03-07
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

## Fonctionnement

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

Le tag `nuts` liste les NUTs supportés (Notation, Usage, and Terminology specs pour Cashu).

Le tag `d` doit être la pubkey Cashu du mint, ce qui donne aux clients un identifiant stable pour la découverte même si le mint modifie ultérieurement ses métadonnées ou republie son annonce.

## Recommandations utilisateur

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
  "content": "I've used this mint for months, very reliable",
  "sig": "<signature>"
}
```

Les utilisateurs peuvent inclure des avis dans le champ `content` et pointer vers des événements d'annonce de mint spécifiques.

Les événements de recommandation sont des événements remplaçables paramétrés. C'est utile car un utilisateur peut réviser une recommandation, mettre à jour son texte d'avis, ou cesser d'endosser un mint sans laisser plusieurs événements de recommandation obsolètes.

## Modèle de confiance

NIP-87 n'indique pas aux clients quel mint est sûr. Il leur fournit un moyen de combiner les métadonnées publiées par l'opérateur avec les recommandations sociales provenant de comptes auxquels l'utilisateur fait déjà confiance.

Cette distinction compte car les requêtes directes d'événements d'annonce de mint peuvent être bruitées ou malveillantes. La spécification avertit explicitement les clients d'utiliser des mesures anti-spam ou des relays de qualité lorsqu'ils contournent les recommandations sociales et interrogent directement les annonces.

## Notes d'interopérabilité

Cashu et Fedimint utilisent des kinds d'annonce différents car ils exposent des détails de connexion différents. Les annonces Cashu publient les URL de mint et les NUTs supportés, tandis que les annonces Fedimint publient des codes d'invitation et les modules de fédération supportés. Un portefeuille qui supporte les deux doit analyser les deux formats.

---

**Sources primaires :**
- [Spécification NIP-87](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Mentionné dans :**
- [Newsletter #4 : Releases](/en/newsletters/2026-01-07-newsletter/#releases)
- [Newsletter #7 : Zeus](/en/newsletters/2026-01-28-newsletter/)

**Voir aussi :**
- [Cashu](/fr/topics/cashu/)
- [NIP-60 : Cashu Wallet](/fr/topics/nip-60/)
