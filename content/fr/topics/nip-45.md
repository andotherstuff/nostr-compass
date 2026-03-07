---
title: "NIP-45 : Comptage d'événements"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-03-07
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45 définit comment les clients demandent aux relais de compter les événements correspondant à un filtre sans transférer les événements eux-mêmes. Il réutilise la syntaxe de filtre NIP-01, de sorte qu'un client peut souvent transformer un `REQ` existant en requête `COUNT` avec les mêmes filtres.

## Fonctionnement

Un client envoie une requête `COUNT` avec un ID d'abonnement et un filtre :

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

Le relais répond avec un comptage :

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

Cela évite de télécharger des centaines ou des milliers d'événements juste pour afficher un nombre. Si un client envoie plusieurs filtres dans une seule requête `COUNT`, le relais les agrège en un seul résultat, de la même manière que plusieurs filtres `REQ` sont combinés par OU.

## Comptage approximatif HyperLogLog

Depuis février 2026, NIP-45 prend en charge le comptage approximatif HyperLogLog (HLL) ([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). Les relais peuvent marquer un résultat comme approximatif, et pour la déduplication inter-relais ils peuvent retourner 256 registres HLL aux côtés du comptage :

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<512-char hex string>"}]
```

HLL résout un problème fondamental : compter les événements distincts à travers plusieurs relais. Si le relais A rapporte 50 réactions et le relais B en rapporte 40, le total n'est pas 90 car de nombreux événements existent sur les deux relais. Les clients fusionnent les valeurs HLL en prenant la valeur maximale à chaque position de registre, ce qui donne une estimation à l'échelle du réseau sans télécharger les événements bruts.

La spécification fixe le nombre de registres à 256 pour l'interopérabilité. Cela maintient la charge utile légère et rend la mise en cache côté relais praticable, car chaque relais calcule la même disposition de registres pour le même filtre éligible.

## Notes d'interopérabilité

HLL n'est défini que pour les filtres avec un attribut de tag, car l'offset utilisé pour construire les registres est dérivé de la première valeur taguée dans le filtre. La spécification identifie aussi un petit ensemble de requêtes canoniques, incluant les réactions, les reposts, les citations, les réponses, les commentaires et le nombre de followers. Ce sont les comptages les plus faciles à précalculer ou mettre en cache pour les relais.

## Pourquoi c'est important

Le nombre de followers, de réactions et de réponses sont les principaux cas d'utilisation. Sans NIP-45, les clients doivent soit faire confiance à la vue locale d'un seul relais, soit télécharger tous les événements correspondants et les dédupliquer localement. NIP-45 garde le comptage dans le relais, et HLL rend les comptages multi-relais praticables sans transformer un relais en autorité centrale.

---

**Sources principales :**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)

**Mentionné dans :**
- [Newsletter #9 : NIP Deep Dive](/en/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-45-event-counting-and-hyperloglog)
- [Newsletter #9 : NIP Updates](/en/newsletters/2026-02-11-newsletter/#nip-updates)
- [Newsletter #12 : Five Years of Nostr Februaries](/en/newsletters/2026-03-04-newsletter/)

**Voir aussi :**
- [NIP-11 : Relay Information Document](/fr/topics/nip-11/)
