---
title: "NIP-90 : Data Vending Machines"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-04-22
draft: false
categories:
  - NIP
  - DVM
---

NIP-90 définit les Data Vending Machines (DVM), un protocole pour demander et livrer du travail informatique payant sur Nostr.

## Fonctionnement

Les clients publient des événements de demande de travail dans la plage `5000-5999`. Chaque demande peut inclure un ou plusieurs tags `i` pour les entrées, des tags `param` pour les paramètres spécifiques au travail, un tag `output` pour le format attendu, un plafond `bid`, et des indications de relais pour préciser où les réponses doivent apparaître. Les fournisseurs de services répondent avec un kind de résultat correspondant dans la plage `6000-6999`, toujours `1000` au-dessus du kind de la demande.

Les résultats incluent la demande originale, la pubkey du client, et optionnellement un tag `amount` ou une facture. Les fournisseurs peuvent aussi envoyer des événements de feedback kind `7000` tels que `payment-required`, `processing`, `partial`, `error` ou `success`, ce qui permet aux clients d'afficher la progression avant l'arrivée du résultat final.

## Paiement et confidentialité

Le protocole laisse intentionnellement la logique commerciale ouverte. Un fournisseur peut demander un paiement avant le début du travail, après avoir renvoyé un échantillon, ou après avoir livré le résultat complet. Cette flexibilité est importante car les travaux DVM vont de transformations de texte peu coûteuses à des tâches GPU coûteuses, et les fournisseurs n'acceptent pas tous le même risque de paiement.

Si un client veut des entrées privées, la demande peut déplacer les données `i` et `param` dans un `content` chiffré et marquer l'événement avec un tag `encrypted` plus le tag `p` du fournisseur. Cela protège les prompts ou le matériel source des observateurs de relais, mais cela signifie aussi que le client doit cibler un fournisseur spécifique au lieu de diffuser une demande de marché ouverte.

## Notes d'interopérabilité

NIP-90 prend en charge le chaînage de travaux via des tags `i` avec le type d'entrée `job`, de sorte qu'un résultat peut alimenter une demande ultérieure. Cela rend possible des flux à plusieurs étapes sans inventer une couche d'orchestration séparée.

La découverte de fournisseurs est en dehors de la boucle requête/réponse elle-même. La spécification renvoie aux annonces [NIP-89 : Recommended Application Handlers](/fr/topics/nip-89/) pour publier les kinds de travaux pris en charge, ce qui permet aux clients de découvrir des fournisseurs avant de publier une demande.

---

**Sources primaires :**
- [Spécification NIP-90](https://github.com/nostr-protocol/nips/blob/master/90.md)

**Mentionné dans :**
- [Newsletter #11 : NIP-AC DVM Agent Coordination](/fr/newsletters/2026-02-25-newsletter/)
- [Newsletter #19 : Forgesworn toll-booth-dvm](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19 : proposition Agent Reputation Attestations](/en/newsletters/2026-04-22-newsletter/)

**Voir aussi :**
- [NIP-89 : Recommended Application Handlers](/fr/topics/nip-89/)
