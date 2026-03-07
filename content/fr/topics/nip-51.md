---
title: "NIP-51 : Listes"
date: 2025-12-17
translationOf: /en/topics/nip-51.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Social
---

NIP-51 définit les événements de liste pour organiser les utilisateurs, événements, relais, hashtags et autres références. C'est le protocole principal pour les signets, les listes de mutes, les ensembles de suivi, les ensembles de relais et plusieurs autres collections gérées par les utilisateurs.

## Listes standard et ensembles

- Les **listes standard** utilisent des kinds d'événements remplaçables comme le kind `10000` pour les listes de mutes, le kind `10003` pour les signets et le kind `10007` pour les relais de recherche.
- Les **ensembles** utilisent des kinds adressables avec des tags `d`, comme le kind `30000` pour les ensembles de suivi, le kind `30003` pour les ensembles de signets et le kind `30030` pour les ensembles d'emojis.

La distinction compte dans le comportement des clients. Les listes standard impliquent une seule liste canonique par utilisateur et par kind. Les ensembles impliquent plusieurs collections nommées, les clients doivent donc préserver le tag `d` de chaque liste.

## Structure

Les listes utilisent des tags pour référencer le contenu :

- Tags `p` pour les clés publiques
- Tags `e` pour les événements
- Tags `a` pour les événements adressables
- Tags `t` pour les hashtags
- Tags `word` pour les mots mutés
- Tags `relay` pour les URLs de relais dans les kinds de listes orientés relais

Certains kinds de listes ont des formes de tags plus restreintes que d'autres. Par exemple, les listes orientées relais utilisent des tags `relay`, tandis que les signets sont censés pointer vers des notes ou des événements adressables. Les clients qui traitent chaque liste NIP-51 comme des tags libres arbitraires perdront en interopérabilité.

## Public vs privé

Les listes peuvent avoir des tags publics et des éléments privés. Les éléments privés sont sérialisés comme un tableau JSON qui reproduit la structure des `tags`, chiffré et stocké dans le `content` de l'événement. La spécification actuelle utilise NIP-44 pour ce modèle d'auto-chiffrement, avec NIP-04 uniquement comme compatibilité ancienne.

Cette séparation permet aux utilisateurs de publier une enveloppe de liste visible tout en masquant certaines entrées. Une liste de signets peut rester publique tandis que les notes ou signets privés restent dans le contenu chiffré.

## Kinds utiles

- **Kind 10000** : liste de mutes pour les clés publiques, fils, hashtags et mots mutés
- **Kind 10003** : signets pour les notes et le contenu adressable
- **Kind 10007** : relais de recherche préférés
- **Kind 30002** : ensembles de relais pour les groupes de relais nommés
- **Kind 30006** : ensembles de curation d'images
- **Kind 39089** : starter packs pour les lots de suivi partageables

Des changements récents de la spécification ont déplacé les hashtags hors des signets génériques vers les ensembles d'intérêts, et ajouté le kind `30006` pour la curation d'images. Ces deux changements réduisent l'ambiguïté dans l'interprétation du contenu des listes par les clients.

---

**Sources principales :**
- [NIP-51 Specification](https://github.com/nostr-protocol/nips/blob/master/51.md)

**Mentionné dans :**
- [Newsletter #1 : NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2 : NIP Updates](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #4 : NIP Deep Dive](/en/newsletters/2026-01-13-newsletter/#nip-deep-dive-nip-51-and-nip-65)
- [Newsletter #8 : njump Adds NIP-51 Support](/en/newsletters/2026-02-04-newsletter/#njump)

**Voir aussi :**
- [NIP-02 : Follow List](/fr/topics/nip-02/)
