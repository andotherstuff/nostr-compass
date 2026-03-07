---
title: "Web of Trust"
date: 2025-12-31
translationOf: /en/topics/web-of-trust.md
translationDate: 2026-03-07
draft: false
categories:
  - Confiance
  - Graphe social
---

Web of Trust (WoT) est un modèle de confiance décentralisé où la réputation et la fiabilité sont dérivées des relations du graphe social plutôt que d'autorités centrales.

## Comment ça fonctionne

Dans Nostr, Web of Trust part généralement du graphe de suivi défini dans [NIP-02: Follow List](/fr/topics/nip-02/) et ajoute parfois des masquages, des signalements ou des signaux d'identité vérifiée. Un client ou un service choisit une ou plusieurs pubkeys de départ auxquelles il fait déjà confiance, puis propage cette confiance vers l'extérieur dans le graphe.

1. **Construction du graphe** : Construire un graphe orienté des suivis et d'éventuels signaux négatifs
2. **Sélection des seeds** : Partir des pubkeys auxquelles l'observateur fait déjà confiance
3. **Propagation du score** : Propager le rang dans le graphe avec un algorithme comme PageRank ou une variante
4. **Seuils et normalisation** : Limiter la profondeur, atténuer les comptes avec peu de signal et normaliser le score final pour l'affichage ou le filtrage

L'algorithme exact n'est pas standardisé. Deux systèmes WoT peuvent tous deux être valides tout en produisant des classements différents parce qu'ils utilisent des seeds différents, une profondeur de graphe différente, des règles de décroissance différentes ou des traitements distincts des masquages et des signalements.

## Pourquoi c'est important

WoT donne à Nostr un moyen de classer et de filtrer sans service central de modération. Un graphe de confiance personnalisé est plus difficile à manipuler qu'un simple nombre d'abonnés, parce que les faux comptes ont toujours besoin qu'un flux de confiance leur parvienne depuis le réseau existant de l'observateur.

L'envers du décor, c'est le démarrage à froid. Si vous ne suivez personne, un WoT personnalisé n'a presque aucune base pour classer quoi que ce soit. Beaucoup de produits règlent ce problème avec des listes de départ, des fournisseurs de confiance par défaut ou des scores précalculés venus de services externes.

## Applications dans Nostr

- **Filtrage du spam** : Les relays peuvent utiliser WoT pour filtrer le contenu peu fiable
- **Découverte de contenu** : Faire remonter le contenu des comptes auxquels votre réseau fait confiance
- **Annuaires de paiement** : Recherche d'adresses Lightning avec prévention de l'usurpation d'identité
- **Politiques de relay** : Les relays WoT n'acceptent que les notes de pubkeys de confiance
- **Modération décentralisée** : Les communautés peuvent sélectionner le contenu selon des scores de confiance

## Notes d'implémentation

Comme les calculs WoT exigent d'explorer de grandes parties du réseau, beaucoup de clients ne les font pas localement. [NIP-85: Trusted Assertions](/fr/topics/nip-85/) existe en partie pour cette raison : il donne aux clients un moyen de consommer des calculs WoT tiers signés quand le calcul local coûte trop cher.

Les implémentations existantes répondent aussi à des questions différentes. Un rang de confiance global est utile pour la découverte et la résistance au spam à l'échelle du réseau. Un score local personnalisé est meilleur pour répondre à "montre-moi les comptes auxquels mon graphe ferait confiance". Lire un nombre WoT sans savoir quel modèle l'a produit reste une source fréquente de confusion.

---

**Sources principales :**
- [NIP-02: Follow List](https://github.com/nostr-protocol/nips/blob/master/02.md)
- [NIP-85: Trusted Assertions](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [Nostr.Band Trust Rank](https://trust.nostr.band/)
- [Protocole DCoSL](https://github.com/wds4/DCoSL)
- [Noswot](https://codeberg.org/weex/noswot)

**Mentionné dans :**
- [Newsletter #3 : Récapitulatif de Décembre](/fr/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Voir aussi :**
- [NIP-02: Liste de Suivi](/fr/topics/nip-02/)
