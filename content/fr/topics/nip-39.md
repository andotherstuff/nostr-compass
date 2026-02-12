---
title: "NIP-39 : Identités externes dans les profils"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Identity
---

NIP-39 définit comment les utilisateurs attachent des revendications d'identité externes à leurs profils Nostr en utilisant des tags `i`. Ces tags lient une pubkey Nostr à des comptes sur des plateformes externes comme GitHub, Twitter ou des domaines DNS.

## Fonctionnement

Chaque revendication d'identité prend la forme d'un tag `i` contenant un identifiant de plateforme et une URL de preuve. Le compte externe renvoie vers la pubkey Nostr, établissant une vérification bidirectionnelle :

```json
{
  "tags": [
    ["i", "github:username", "https://gist.github.com/username/proof"],
    ["i", "twitter:handle", "https://twitter.com/handle/status/proof_tweet_id"]
  ]
}
```

Pour vérifier une revendication, un client récupère l'URL de preuve et confirme qu'elle contient la pubkey Nostr de l'utilisateur. Ce mécanisme crée un réseau de connexions d'identité sans nécessiter de services de vérification centralisés.

## Changements récents

En février 2026, la [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) a extrait ces tags d'identité des événements kind 0 (métadonnées utilisateur) vers un kind 10011 dédié. Ce déplacement fait partie de la campagne d'allègement du kind 0 de vitorpamplona, motivée par une faible adoption. Presque aucun client n'implémentait la vérification des tags `i`, pourtant chaque récupération de kind 0 transportait cette surcharge. Le nouveau kind 10011 permet aux clients intéressés de récupérer les revendications d'identité séparément.

---

**Sources principales :**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)

**Mentionné dans :**
- [Newsletter #9 : Mises à jour des NIP](/fr/newsletters/2026-02-11-newsletter/#mises-à-jour-des-nip)

**Voir aussi :**
- [NIP-05 : Vérification par domaine DNS](/fr/topics/nip-05/)
