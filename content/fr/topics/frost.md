---
title: "FROST (Flexible Round-Optimized Schnorr Threshold Signatures)"
date: 2025-12-31
translationOf: /en/topics/frost.md
translationDate: 2026-03-07
draft: false
categories:
  - Cryptography
  - Protocol
---

FROST (Flexible Round-Optimized Schnorr Threshold Signatures) est un schéma de signature à seuil qui permet à un groupe de produire une signature Schnorr valide sans qu'aucun participant ne détienne la clé privée complète.

## Fonctionnement

FROST permet la signature T-sur-N. Tout sous-ensemble atteignant le seuil peut coopérer pour produire une signature pour la clé publique du groupe.

Le protocole de signature utilise deux tours :

1. **Tour d'engagement** : chaque participant génère et partage des engagements cryptographiques
2. **Tour de signature** : les participants combinent leurs signatures partielles en une signature agrégée finale

Le résultat final se vérifie comme une signature Schnorr ordinaire. Les vérificateurs voient une seule signature sous une seule clé publique, pas une liste de cosignataires.

## Notes de sécurité

La gestion des nonces est critique. La RFC est explicite : les nonces de signature sont à usage unique. Leur réutilisation peut compromettre le matériel de clé.

La RFC ne standardise pas non plus la génération distribuée de clés. Elle spécifie le protocole de signature lui-même et inclut la génération de clés par tiers de confiance uniquement en annexe. En pratique, la sécurité d'un déploiement FROST dépend à la fois du flux de signature et de la manière dont les parts ont été créées et stockées.

## Cas d'utilisation dans Nostr

Dans le contexte de Nostr, FROST peut supporter :

- **Gouvernance par quorum** : les groupes peuvent partager un nsec via des schémas T-sur-N, où les membres peuvent se représenter eux-mêmes ou déléguer à des conseils
- **Administration multi-signature** : modération communautaire nécessitant plusieurs signatures d'administrateurs
- **Gestion décentralisée des clés** : distribution de la confiance entre plusieurs parties pour les opérations critiques

## Statut

FROST est spécifié dans la [RFC 9591](https://datatracker.ietf.org/doc/rfc9591/), publiée sur le flux IRTF en juin 2024. Cela donne au protocole une spécification publique stable, mais ce n'est pas une RFC sur le parcours de standardisation IETF.

---

**Sources principales :**
- [RFC 9591: FROST Protocol](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST Paper (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [Zcash Foundation Rust Implementation](https://github.com/ZcashFoundation/frost)

**Mentionné dans :**
- [Newsletter #3 : Dépôt NIPs](/fr/newsletters/2025-12-31-newsletter/#nips-repository)
- [Newsletter #8](/fr/newsletters/2026-02-04-newsletter/)
- [Newsletter #10](/fr/newsletters/2026-02-18-newsletter/)

**Voir aussi :**
- [NIP-46 : Nostr Connect](/fr/topics/nip-46/)
- [NIP-55 : Android Signer Application](/fr/topics/nip-55/)
