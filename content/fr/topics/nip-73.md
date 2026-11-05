---
title: "NIP-73 : identifiants de contenu externe"
date: 2026-02-04
draft: false
translationOf: /en/topics/nip-73.md
translationDate: 2026-11-05
categories:
  - Protocol
  - Discovery
  - Metadata
---

NIP-73 définit une manière standard de référencer du contenu externe dans les événements Nostr. Il utilise des tags `i` pour l'identifiant lui-même et des tags `k` pour le type d'identifiant, ce qui permet aux clients de regrouper les discussions autour d'un même livre, site web, épisode de podcast, lieu, hashtag ou objet de blockchain. La [spécification actuelle](https://github.com/nostr-protocol/nips/blob/master/73.md) est marquée comme brouillon et facultative.

## Fonctionnement {#how-it-works}

Un événement utilisant NIP-73 inclut un tag `i` contenant un identifiant externe normalisé et un tag `k` qui nomme la famille d'identifiants. Les clients peuvent interroger les relais sur un sujet précis via `i` ou sur une famille entière via `k`. NIP-73 n'ajoute aucun kind d'événement qui lui soit propre. Ce sont les commentaires, les avis et d'autres événements qui portent les tags.

Fragment de tags, et non un événement complet :

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

Une page web place son URL normalisée dans `i` et définit `k` à `web`. La spécification couvre plusieurs familles d'identifiants, notamment :

- les URL web normalisées sans fragment
- les ISBN pour les livres
- les ISAN pour les films
- les DOI
- les geohashes et les codes ISO 3166 de pays ou de subdivision
- les GUID de flux, d'épisode et d'éditeur de podcast
- les hashtags
- les identifiants de transaction et d'adresse de blockchain

## Règles de normalisation {#normalization-rules}

La correspondance repose sur des chaînes identiques, la spécification fixe donc une forme écrite unique pour chaque famille. Exemples tirés de la spécification :

- les geohashes utilisent `geo:<value>` et doivent être en minuscules
- les codes de pays et de subdivision utilisent `iso3166:<code>` et doivent être en majuscules
- les ISBN omettent les tirets
- les DOI sont en minuscules
- les URL web perdent leur fragment
- les hachages de transaction blockchain utilisent l'hexadécimal en minuscules

La normalisation fixe la manière d'écrire un identifiant donné. Elle ne fusionne pas les alias. Les ISBN propres à une édition et les URL qui se normalisent en chaînes différentes restent des identifiants distincts, de sorte que la discussion sur un même livre ou article peut encore se répartir entre plusieurs valeurs `i`.

## Indications d'URL {#url-hints}

Un tag `i` peut inclure une indication d'URL facultative comme troisième élément du tableau, c'est-à-dire la deuxième valeur après le nom du tag. Un client dépourvu de rendu personnalisé pour ce type d'identifiant peut utiliser l'indication comme lien de repli.

Fragment de tag : `["i", "isbn:9780765382030", "<url-hint>"]`

C'est l'auteur qui choisit l'indication. Elle ne fait pas partie de l'identité, ne prouve aucune propriété et ne désigne aucun site canonique.

## Confiance et contexte {#trust-and-context}

Deux événements portant le même identifiant se retrouvent dans la même conversation, et l'identifiant partagé n'établit rien de plus. Un événement signé identifie son auteur. Il n'authentifie pas le livre, le site ou l'éditeur de podcast qu'il référence, et il ne montre pas qui les contrôle.

Le sens d'un tag `i` dépend de l'événement. Dans les commentaires [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md), les majuscules `I`/`K` marquent la portée racine et les minuscules `i`/`k` marquent le parent. Cette structure de fil provient de NIP-22, et NIP-73 ne définit aucun kind de commentaire. [NIP-39](https://github.com/nostr-protocol/nips/blob/master/39.md) utilise `i` pour les identités externes dans les profils, si bien que les tags `i` ne désignent pas tous un sujet NIP-73.

Les assertions de confiance (Trusted Assertions) de [NIP-85](/fr/topics/nip-85/) peuvent aussi cibler des identifiants NIP-73 tels que des livres, des sites web, des hashtags et des lieux.

## Implémentations {#implementations}

Le fichier [nip73.rs au commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs) de rust-nostr analyse les préfixes connus pour produire un `ExternalContentId` typé et convertit une indication facultative en URL typée. Il n'écrit le troisième élément du tag que lorsqu'une indication existe. Ses tests conservent des ISBN avec tirets : l'analyseur retire le préfixe et stocke le reste sans appliquer la normalisation de la spécification, si bien que l'analyse typée ne garantit pas des chaînes canoniques. Il exclut les identifiants de chaîne de la famille, en associant `ethereum:100:tx:<hash>` à `ethereum:tx`. Cette révision ne comporte pas de variante `iso3166` pour les pays.

Le fichier [DisplayExternalId.kt au commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt) d'Amethyst oriente les identifiants de geohash, de hashtag et d'URL vers des affichages dédiés et présente les autres types pris en charge sous forme de puce de portée générique. Une URL ouvre la route de fil propre à l'application pour cette page. Lorsque les aperçus sont désactivés, le rendu normal affiche une simple puce de lien et ne demande aucun aperçu. Lorsque les aperçus sont activés, la récupération d'un aperçu manquant peut contacter le site cible. Aucun des deux fichiers ne montre le comportement d'une version publiée.

---

**Sources primaires :**
- [Spécification NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Ajoute les codes ISO 3166 de pays et de subdivision
- [rust-nostr nip73.rs au commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs)
- [Amethyst DisplayExternalId.kt au commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt)

**Mentionné dans :**
- [Newsletter #47 : analyse approfondie d'un NIP](/fr/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)
- [Newsletter #45](/en/newsletters/2026-10-21-newsletter/#feather)
- [Newsletter #43](/en/newsletters/2026-10-07-newsletter/#protocol-and-spec-work)
- [Newsletter #37 : août 2025](/en/newsletters/2026-08-26-newsletter/#august-2025)
- [Newsletter #8 : mises à jour des NIP](/en/newsletters/2026-02-04-newsletter/#nip-updates)
- [Newsletter #10 : analyse approfondie de NIP-85](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Newsletter #36 : commentaires (NIP-22)](/en/newsletters/2026-08-19-newsletter/#comments-nip-22)
- [Newsletter #38 : analyse approfondie d'un NIP](/en/newsletters/2026-09-02-newsletter/#reactions-nip-25)
- [Newsletter #40 : filtres podcast-medium de NIP-73](/en/newsletters/2026-09-16-newsletter/#nip-73-proposes-podcast-medium-filters)
- [Newsletter #42 : contenu externe, septembre 2024](/en/newsletters/2026-09-30-newsletter/#september-2024-posts-acquire-richer-context)

**Voir aussi :**
- [NIP-31 : gestion des kinds d'événements inconnus](/fr/topics/nip-31/)
- [NIP-22 : commentaire](/fr/topics/nip-22/)
- [NIP-39 : identités externes dans les profils](/fr/topics/nip-39/)
- [NIP-85 : assertions de confiance](/fr/topics/nip-85/)
