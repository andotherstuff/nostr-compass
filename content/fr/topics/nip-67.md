---
title: "NIP-67 : Indice de complétude EOSE"
date: 2026-04-22
translationOf: /en/topics/nip-67.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-67 est une proposition ouverte qui étend le message `EOSE` existant dans [NIP-01](/fr/topics/nip-01/) avec un troisième élément optionnel indiquant si le relay a livré tous les événements stockés correspondant au filtre. L'objectif est de remplacer l'heuristique peu fiable que les clients utilisent aujourd'hui pour décider si un abonnement est épuisé ou interrompu par une limite côté relay.

## Le problème

`EOSE` marque la frontière entre les événements stockés et les événements en temps réel, mais ne fournit aucune information sur la complétude. En pratique, les relays imposent un plafond par abonnement, souvent entre 300 et 1000 événements, indépendant du `limit` demandé par le client. Un client qui demande les 500 dernières notes à un relay plafonné à 300 reçoit 300 événements et un `EOSE`, sans moyen de distinguer « c'est tout » de « nous nous sommes arrêtés en chemin ». Le contournement actuel consiste à comparer le nombre d'événements au `limit` du client et à paginer par précaution, ce qui fait à la fois manquer des événements quand le plafond est inférieur à la limite demandée et gaspille un aller-retour quand le plafond est un multiple du nombre réel de correspondances.

Les égalités en bordure aggravent encore le problème. Paginer avec `until = oldest_created_at` risque soit de manquer soit de récupérer en double des événements qui partagent le plus ancien horodatage du lot, selon la manière dont le relay compare les timestamps.

## Le changement

NIP-67 ajoute un troisième élément optionnel à `EOSE` :

```
["EOSE", "<subscription_id>", "finish"]   // tous les événements stockés correspondants ont été livrés
["EOSE", "<subscription_id>"]             // aucune revendication de complétude (hérité)
```

Seul le signal positif est spécifié. Un relay qui annonce le support de NIP-67 mais omet l'indice indique qu'il y en a davantage. Un relay qui n'annonce pas ce support retombe sur l'heuristique existante, donc le changement reste rétrocompatible avec tous les clients et relays actuels.

Les clients qui savent que leur relay supporte NIP-67 peuvent arrêter la pagination dès qu'ils voient `"finish"`, éviter l'aller-retour supplémentaire obligatoire quand le plafond correspond exactement au jeu de résultats, et afficher à l'utilisateur une complétude exacte.

## Statut

La proposition est [ouverte sous la PR #2317](https://github.com/nostr-protocol/nips/pull/2317) contre le dépôt NIPs.

---

**Sources principales :**
- [PR #2317 : NIP-67 EOSE Completeness Hint](https://github.com/nostr-protocol/nips/pull/2317)
- [Spécification NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Mentionné dans :**
- [Newsletter #19 : mises à jour NIP](/en/newsletters/2026-04-22-newsletter/)

**Voir aussi :**
- [NIP-01 : flux du protocole de base](/fr/topics/nip-01/)
- [NIP-11 : document d'information du relay](/fr/topics/nip-11/)
