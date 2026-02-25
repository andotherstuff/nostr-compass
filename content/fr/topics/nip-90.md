---
title: "NIP-90"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - DVM
---

NIP-90 définit Data Vending Machines (DVMs), un protocole de marché pour demander et payer un travail computationnel sur Nostr.

## Comment ça fonctionne

Les clients publient des événements de requête de tâche (kinds 5000-5999) spécifiant le travail nécessaire. Les fournisseurs de services surveillent les requêtes correspondant à leurs capacités et publient les résultats après avoir terminé le calcul. Le paiement se fait via Lightning ou d'autres mécanismes négociés dans le flux de tâches.

Les kinds de tâches définissent différents types de calcul : génération de texte, génération d'images, traduction, découverte de contenu, et plus. Chaque kind spécifie le format d'entrée/sortie attendu.

## Fonctionnalités clés

- Marché de calcul décentralisé
- Système de types de tâches basé sur les kinds
- Concurrence des fournisseurs sur le prix et la qualité
- Extensible pour de nouveaux types de calcul

---

**Sources principales :**
- [Spécification NIP-90](https://github.com/nostr-protocol/nips/blob/master/90.md)

**Mentionné dans :**
- [Newsletter #11 : NIP-AC DVM Agent Coordination](/fr/newsletters/2026-02-25-newsletter/#nip-updates)

**Voir aussi :**
- [NIP-85 : Trusted Assertions](/fr/topics/nip-85/)
