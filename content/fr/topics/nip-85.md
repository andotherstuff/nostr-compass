---
title: "NIP-85"
date: 2026-02-18
translationOf: /en/topics/nip-85.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - Trust
  - Infrastructure
---

NIP-85 définit Trusted Assertions, un système pour déléguer des calculs coûteux à des fournisseurs de services de confiance qui publient des résultats signés comme événements Nostr.

## Comment ça fonctionne

Les scores de Web of Trust, les métriques d'engagement et d'autres valeurs calculées nécessitent le parcours de nombreux relays et le traitement de grands volumes d'événements. Ce travail est impraticable sur les appareils mobiles. NIP-85 permet aux fournisseurs spécialisés d'effectuer ces calculs et de publier des résultats que les clients peuvent interroger.

Les fournisseurs de services annoncent leurs capacités via des événements kind 30085. Les clients découvrent les fournisseurs en interrogeant ces annonces depuis les pubkeys que l'utilisateur suit déjà ou en qui il a confiance. Les résultats arrivent comme événements kind 30382 signés par le fournisseur.

## Fonctionnalités clés

- Calcul délégué pour les métriques gourmandes en ressources
- Découverte de fournisseurs via le graphe social
- Assertions signées pour des résultats vérifiables
- Décisions de confiance côté client

---

**Sources principales :**
- [Spécification NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md)

**Mentionné dans :**
- [Newsletter #10 : Approfondissement NIP-85](/fr/newsletters/2026-02-18-newsletter/#approfondissement-nip--nip-85-trusted-assertions)
- [Newsletter #11 : Découvrabilité du fournisseur de services NIP-85](/fr/newsletters/2026-02-25-newsletter/#nip-updates)

**Voir aussi :**
- [Web of Trust](/fr/topics/web-of-trust/)
