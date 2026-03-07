---
title: "FIPS"
date: 2026-02-25
translationOf: /en/topics/fips.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Networking
  - Infrastructure
---

FIPS (Free Internetworking Peering System) est un protocole de réseau maillé auto-organisé qui utilise des paires de clés secp256k1 de type Nostr comme identités de noeud.

## Fonctionnement

FIPS vise à faire fonctionner le réseau pair-à-pair sans serveurs centraux ni autorités de certification. Les noeuds découvrent leurs voisins, construisent un état de routage et transfèrent les paquets en utilisant uniquement des connaissances locales.

La conception combine un arbre couvrant avec des données d'accessibilité par filtres de Bloom. Chaque noeud obtient des coordonnées relatives à l'arbre, puis route de manière gloutonne vers la destination. Si le routage glouton échoue, l'arbre fournit quand même un chemin de repli.

Deux couches de chiffrement protègent le trafic. Le chiffrement de couche liaison (pattern Noise IK) sécurise la communication saut par saut entre voisins. Le chiffrement de couche session (pattern Noise XK) fournit une protection de bout en bout contre les routeurs intermédiaires.

## Pourquoi c'est important

FIPS réutilise le même modèle de clés que les développeurs Nostr connaissent déjà, mais l'applique au routage de paquets plutôt qu'aux événements sociaux. Cela lui donne un modèle d'identité simple : l'identité réseau est la clé cryptographique, pas une allocation IP ou une chaîne de certificats.

La conception indépendante du transport est aussi importante. Le même modèle de routage et d'identité peut, en principe, fonctionner sur UDP, Ethernet, Bluetooth ou LoRa, ce qui rend FIPS intéressant pour les environnements réseau hostiles ou peu fiables.

## État de l'implémentation

Comme couvert dans Compass, l'implémentation Rust actuelle inclut déjà un transport UDP fonctionnel et la découverte par filtre de Bloom. Le bootstrapping par relais est encore un travail futur, donc aujourd'hui le protocole est davantage un substrat réseau qu'un remplacement de relais Nostr achevé.

---

**Sources principales :**
- [Dépôt FIPS](https://github.com/jmcorgan/fips)
- [Documentation de conception](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md)

**Mentionné dans :**
- [Newsletter #11 : FIPS News](/fr/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking)
- [Newsletter #12](/fr/newsletters/2026-03-04-newsletter/)

**Voir aussi :**
- [Protocole Marmot](/fr/topics/marmot/)
