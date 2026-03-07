---
title: "NIP-73 : Identifiants de contenu externe"
date: 2026-02-04
translationOf: /en/topics/nip-73.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Discovery
  - Metadata
---

NIP-73 définit une manière standard de référencer du contenu externe dans les événements Nostr. Il utilise des tags `i` pour l'identifiant lui-même et des tags `k` pour le type d'identifiant, permettant aux clients de regrouper les discussions autour du même livre, site web, épisode de podcast, lieu, hashtag ou objet blockchain.

## Fonctionnement

Un événement utilisant NIP-73 inclut un tag `i` contenant un identifiant externe normalisé et un tag `k` décrivant le type d'identifiant. Les clients peuvent ensuite rechercher tous les événements qui référencent le même sujet.

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

La spécification couvre plusieurs familles d'identifiants, notamment :

- les URL web normalisées sans fragment
- les ISBN pour les livres
- les ISAN pour les films
- les geohashes et les codes pays ou de subdivision ISO 3166
- les GUID de flux, épisodes et éditeurs de podcasts
- les hashtags
- les identifiants de transactions et d'adresses blockchain

## Règles de normalisation

Le détail principal de NIP-73 pour le lecteur est la normalisation. Le même sujet doit correspondre à une seule chaîne canonique, sinon les clients divisent la discussion entre plusieurs identifiants qui désignent la même chose.

Exemples tirés de la spécification :

- les geohashes utilisent `geo:<valeur>` et doivent être en minuscules
- les codes de pays et de subdivision utilisent `iso3166:<code>` et doivent être en majuscules
- les ISBN omettent les tirets
- les URL web suppriment les fragments
- les hashes de transactions blockchain utilisent de l'hexadécimal en minuscules

Cela peut sembler anodin, mais c'est la différence entre une conversation partagée et plusieurs index incompatibles.

## Usages courants

NIP-73 est une couche de référence générale, pas un format de contenu. Un article long format peut pointer vers un ISBN, une critique peut pointer vers un ISAN de film, et un post local peut pointer vers un geohash ou un code pays sans inventer un tag personnalisé à chaque fois.

La spécification permet aussi une indication d'URL optionnelle comme deuxième valeur d'un tag `i`. Cela donne aux clients un lien de repli quand ils n'ont pas de rendu personnalisé pour le type d'identifiant.

## Pourquoi c'est important

Nostr possède déjà de solides références internes pour les événements et les profils. NIP-73 étend cette idée aux éléments extérieurs à Nostr. Une fois les identifiants normalisés, les commentaires, les notes, les passages surlignés et les assertions de confiance peuvent tous s'attacher au même sujet externe à travers différents clients.

C'est aussi pourquoi [NIP-85](/fr/topics/nip-85/) s'appuie sur NIP-73. Les Trusted Assertions peuvent évaluer non seulement les utilisateurs et les événements, mais aussi les identifiants NIP-73 comme les livres, sites web, hashtags et lieux.

---

**Sources primaires :**
- [Spécification NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Ajout des codes pays et de subdivision ISO 3166

**Mentionné dans :**
- [Newsletter #8 : NIP Updates](/en/newsletters/2026-02-04-newsletter/#nip-updates)
- [Newsletter #10 : NIP-85 Deep Dive](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)

**Voir aussi :**
- [NIP-85 : Trusted Assertions](/fr/topics/nip-85/)
