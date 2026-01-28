---
title: "NIP-66 : Découverte et surveillance de la disponibilité des relais"
date: 2026-01-21
translationOf: /en/topics/nip-66.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Relays
---

NIP-66 standardise la publication des données de surveillance des relais sur Nostr. Les services de surveillance testent continuellement les relais pour leur disponibilité, latence, conformité au protocole et NIPs supportés, publiant les résultats comme événements kind 30166.

## Fonctionnement

Les moniteurs vérifient la disponibilité des relais en se connectant et en envoyant des abonnements de test. Les mesures de latence suivent le temps de connexion, le temps de réponse aux abonnements et le délai de propagation des événements. Les tests de conformité au protocole vérifient que le comportement du relais correspond aux spécifications, détectant les bugs d'implémentation ou les déviations intentionnelles.

La vérification du support des NIP va au-delà des déclarations [NIP-11](/fr/topics/nip-11/) en testant réellement si les fonctionnalités annoncées fonctionnent correctement. Si un relais prétend supporter la recherche [NIP-50](/fr/topics/nip-50/) mais que les requêtes de recherche échouent, les moniteurs omettront NIP-50 de la liste vérifiée. Cela fournit la vérité terrain sur les capacités des relais.

Les événements kind 30166 utilisent l'URL du relais comme tag `d`, les rendant des événements remplaçables paramétrés. Chaque moniteur publie un événement par relais, mis à jour au fur et à mesure que les mesures changent. Plusieurs moniteurs peuvent suivre le même relais, fournissant redondance et validation croisée.

Les tags de temps aller-retour (rtt) mesurent la latence pour différentes opérations :
- `rtt open` : Établissement de la connexion WebSocket
- `rtt read` : Temps de réponse aux abonnements
- `rtt write` : Vitesse de publication des événements

Toutes les valeurs sont en millisecondes. Les clients utilisent ces métriques pour préférer les relais à faible latence pour les opérations sensibles au temps.

Les informations géographiques aident les clients à sélectionner des relais proches pour une meilleure latence et résistance à la censure. Le tag `geo` contient le code pays, le nom du pays et la région. Le tag `network` distingue les relais clearnet des services cachés Tor ou des points de terminaison I2P.

## Cas d'utilisation

Les données de surveillance alimentent les sélecteurs de relais dans les clients, les sites web explorateurs et les systèmes d'évaluation de la confiance. En fournissant le statut des relais en temps réel indépendamment de l'auto-déclaration des relais, NIP-66 permet une sélection éclairée des relais.

Combiné avec [NIP-11](/fr/topics/nip-11/) (capacités auto-déclarées) et les Attestations de confiance des relais (évaluation de la confiance), l'écosystème évolue vers une sélection de relais basée sur les données plutôt que sur des valeurs par défaut codées en dur.

---

**Sources primaires :**
- [Spécification NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) - Standard de découverte et surveillance de la disponibilité des relais

**Mentionné dans :**
- [Newsletter #6 : Analyse approfondie des NIP](/fr/newsletters/2026-01-21-newsletter/#nip-deep-dive-nip-11-and-nip-66)

**Voir aussi :**
- [NIP-11 : Document d'information du relais](/fr/topics/nip-11/)
- [Attestations de confiance des relais](/fr/topics/trusted-relay-assertions/)
