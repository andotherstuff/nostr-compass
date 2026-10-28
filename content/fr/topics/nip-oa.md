---
title: 'Brouillon Buzz NIP-OA : attestation du propriétaire'
date: 2026-10-28
translationOf: /en/topics/nip-oa.md
translationDate: 2026-10-28
draft: false
---

**Statut :** il s’agit d’une proposition à l’état de brouillon, propre au projet Buzz. NIP-OA n’est pas un NIP officiel accepté. Ce label provient de la documentation du projet Buzz, et le dépôt officiel des NIPs ne l’a ni attribué ni approuvé.

## Objectif

NIP-OA définit un tag `auth` facultatif, grâce auquel une clé propriétaire peut autoriser une clé d’agent à publier des events. L’auteur de l’event reste la clé d’agent. Un tag valide vaut uniquement comme preuve d’autorisation et ne permet pas à l’agent d’usurper l’identité du propriétaire.

## Mécanisme

Au moyen d’une signature Schnorr, le propriétaire signe un hachage à séparation de domaine qui lie la pubkey de l’agent à une chaîne de conditions exacte. Ces conditions peuvent exiger un kind d’event précis et borner le `created_at` autodéclaré. Tant que chaque event respecte les conditions, l’agent peut réutiliser le tag sur ses events. Les vérificateurs valident d’abord l’event de base, puis contrôlent la signature du propriétaire et chacune des conditions.

## Limites

Une chaîne de conditions vide n’ajoute aucune contrainte. Comme les clauses d’horodatage contraignent un champ que l’agent contrôle, elles ne fournissent pas d’expiration fondée sur l’heure réelle. Quiconque a besoin de garantir la fraîcheur doit la vérifier séparément. Publier le tag publiquement relie entre elles les clés du propriétaire et de l’agent.

## Sources primaires

- [Brouillon Buzz NIP-OA : attestation du propriétaire (révision épinglée)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-OA.md)

## Voir aussi

- [NIP-01](/fr/topics/nip-01/)

**Mentionné dans :**

- [Newsletter n° 46 : Buzz](/fr/newsletters/2026-10-28-newsletter/#buzz)
