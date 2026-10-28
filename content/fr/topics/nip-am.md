---
title: "Brouillon NIP-AM de Buzz : métriques de tour d'agent"
date: 2026-10-28
translationOf: /en/topics/nip-am.md
translationDate: 2026-10-28
draft: false
---

**Statut :** il s'agit d'un brouillon de proposition propre au projet Buzz. NIP-AM n'est pas un NIP officiel accepté. Ce libellé provient de la documentation du projet Buzz, et le dépôt officiel des NIPs ne l'a ni attribué ni approuvé.

## Objectif

NIP-AM enregistre la consommation de chaque tour d'agent IA achevé. Pour chaque tour, l'agent publie un event `kind:44200`, que la convention de Buzz traite comme un event régulier en ajout seul (append-only). Le contenu est chiffré avec NIP-44, de l'agent vers le propriétaire. On y trouve les chiffres de consommation de tokens ainsi que des identifiants de corrélation, et toute valeur de coût n'est qu'une estimation. Aucune transcription de la conversation n'y figure.

## Limites

Des tags publics identifient le propriétaire et l'agent, et les relays peuvent toujours voir à quel moment les events sont publiés. Le format ne masque donc pas le fait qu'une activité a eu lieu. Une valeur de consommation manquante signifie « inconnue » et ne doit jamais être comptée comme zéro.

## Proposition de lecteurs délégués

La pull request de documentation #8582, encore ouverte, propose un octroi d'accès à moindre privilège signé par le propriétaire. Dans ce cadre, l'agent publierait une copie chiffrée distincte pour chaque lecteur actif, chacune étant liée à l'ID exact de l'event d'octroi. Aucune autorisation à l'exécution n'est modifiée par cette pull request. Le kind d'octroi proposé, `30180`, et le plafond de lecteurs restent des questions ouvertes, tout comme la politique de révocation, qui n'est pas encore arrêtée. Une révocation pourrait limiter l'historique conservé sur les relays ainsi que les lectures futures. Elle ne peut toutefois pas effacer les copies qu'un lecteur a déjà reçues.

## Sources primaires

- [Brouillon NIP-AM de Buzz : métriques de tour d'agent (révision épinglée)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-AM.md)
- [Pull request Buzz #8582 : lecteurs de métriques délégués (brouillon ouvert)](https://github.com/block/buzz/pull/8582)

## Voir aussi

- [NIP-44](/fr/topics/nip-44/)

**Mentionné dans :**

- [Newsletter #46 : texte du brouillon NIP-AM pour les lecteurs de métriques délégués](/fr/newsletters/2026-10-28-newsletter/#draft-nip-am-text-for-delegated-metric-readers)
- [Newsletter #46 : Buzz](/fr/newsletters/2026-10-28-newsletter/#buzz)
