---
title: "FROST (Flexible Round-Optimized Schnorr Threshold Signatures)"
date: 2025-12-31
translationOf: /en/topics/frost.md
translationDate: 2025-12-31
draft: false
categories:
  - Cryptographie
  - Protocole
---

FROST (Flexible Round-Optimized Schnorr Threshold Signatures) est un schéma de signature à seuil qui permet à un groupe de participants de produire collaborativement des signatures Schnorr valides sans qu'aucune partie ne détienne la clé privée complète.

## Fonctionnement

FROST permet la signature à seuil T-sur-N, où T participants parmi N détenteurs de clés au total doivent coopérer pour produire une signature valide. Le protocole fonctionne en deux tours :

1. **Tour d'engagement** : Chaque participant génère et partage des engagements cryptographiques
2. **Tour de signature** : Les participants combinent leurs signatures partielles en une signature agrégée finale

La signature résultante est indiscernable d'une signature Schnorr standard, maintenant la compatibilité ascendante avec les systèmes de vérification existants.

## Propriétés clés

- **Sécurité à seuil** : Aucun participant ne peut signer seul ; T parties doivent coopérer
- **Efficacité des tours** : Seulement deux tours de communication requis pour signer
- **Protection contre la falsification** : Des techniques novatrices protègent contre les attaques sur les schémas à seuil antérieurs
- **Agrégation de signatures** : Plusieurs signatures se combinent en une seule signature compacte
- **Confidentialité** : Les signatures finales ne révèlent pas quels T participants ont signé

## Cas d'utilisation dans Nostr

Dans le contexte de Nostr, FROST permet :

- **Gouvernance par quorum** : Les groupes peuvent partager un nsec via des schémas T-sur-N, où les membres peuvent se représenter eux-mêmes ou déléguer à des conseils
- **Administration multi-signature** : Modération communautaire nécessitant plusieurs signatures d'administrateurs
- **Gestion décentralisée des clés** : Distribution de la confiance entre plusieurs parties pour les opérations critiques

## Standardisation

FROST a été standardisé sous le nom RFC 9591 en juin 2024, intitulé "The Flexible Round-Optimized Schnorr Threshold (FROST) Protocol for Two-Round Schnorr Signatures".

---

**Sources principales :**
- [RFC 9591: FROST Protocol](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST Paper (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [University of Waterloo CrySP](https://crysp.uwaterloo.ca/software/frost/)
- [Zcash Foundation Rust Implementation](https://github.com/ZcashFoundation/frost)

**Mentionné dans :**
- [Newsletter #3 : Dépôt NIPs](/fr/newsletters/2025-12-31-newsletter/#nips-repository)

**Voir aussi :**
- [Proposition NIP-XX Quorum](https://github.com/nostr-protocol/nips/pull/2179)
