---
title: "Web of Trust"
date: 2025-12-31
translationOf: /en/topics/web-of-trust.md
translationDate: 2025-12-31
draft: false
categories:
  - Confiance
  - Graphe Social
---

Web of Trust (WoT) est un modèle de confiance décentralisé où la réputation et la fiabilité sont dérivées des relations du graphe social plutôt que d'autorités centrales.

## Comment Ça Fonctionne

Dans Nostr, Web of Trust exploite le graphe de suivi (listes de contacts NIP-02) et les événements de signalement pour calculer des scores de confiance :

1. **Construction du Graphe** : Un graphe orienté est construit à partir des pubkeys, événements et leurs relations (suivis, masqués, signalements)
2. **Attribution des Poids** : Des poids initiaux sont attribués aux pubkeys connues comme fiables (par ex., celles avec des identifiants NIP-05 vérifiés)
3. **Propagation Itérative** : Les scores de confiance se propagent à travers le réseau en utilisant des algorithmes similaires à PageRank
4. **Résistance Sybil** : Si un attaquant crée de nombreux faux comptes, la confiance qui leur est transmise est divisée par le nombre de faux

## Propriétés Clés

- **Décentralisé** : Aucune autorité centrale ne détermine la réputation
- **Personnalisé** : La confiance peut être calculée du point de vue de chaque utilisateur en fonction de qui il suit
- **Résistant aux Sybil** : Les fermes de bots ne peuvent pas facilement manipuler le système en raison de la dilution de confiance
- **Composable** : Peut être appliqué au filtrage de spam, à la modération de contenu, à l'admission aux relays et aux annuaires de paiement

## Applications dans Nostr

- **Filtrage de Spam** : Les relays peuvent utiliser WoT pour filtrer le contenu à faible confiance
- **Découverte de Contenu** : Afficher le contenu des comptes auxquels votre réseau fait confiance
- **Annuaires de Paiement** : Recherche d'adresses Lightning avec prévention de l'usurpation d'identité
- **Politiques de Relay** : Les relays WoT n'acceptent que les notes des pubkeys de confiance
- **Modération Décentralisée** : Les communautés peuvent curatorer en fonction des scores de confiance

## Implémentations

Plusieurs projets implémentent Web of Trust pour Nostr :
- **Nostr.Band Trust Rank** : Notation de style PageRank pour le réseau
- **WoT Relays** : Relays filtrant par distance sociale
- **DCoSL** : Protocole pour les systèmes de réputation décentralisés
- **Noswot** : Notation de confiance basée sur les suivis et signalements

---

**Sources principales :**
- [Nostr.Band Trust Rank](https://trust.nostr.band/)
- [Protocole DCoSL](https://github.com/wds4/DCoSL)
- [Noswot](https://codeberg.org/weex/noswot)

**Mentionné dans :**
- [Newsletter #3 : Récapitulatif de Décembre](/fr/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Voir aussi :**
- [NIP-02: Liste de Suivi](/fr/topics/nip-02/)
