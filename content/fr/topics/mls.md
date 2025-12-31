---
title: "MLS (Message Layer Security)"
date: 2025-12-31
translationOf: /en/topics/mls.md
translationDate: 2025-12-31
draft: false
categories:
  - Cryptographie
  - Protocole
  - Messagerie
  - Confidentialité
---

Message Layer Security (MLS) est un protocole standardisé par l'IETF pour la messagerie de groupe chiffrée de bout en bout. Il fournit un établissement efficace de clés avec confidentialité persistante et sécurité post-compromission pour des groupes allant de deux à des milliers de participants.

## Fonctionnement

MLS utilise une structure d'accord de clés basée sur un arbre appelée TreeKEM :

1. **Paquets de clés** : Chaque participant publie un paquet de clés contenant son identité et ses clés de chiffrement
2. **État du groupe** : Un arbre à cliquet maintient l'état cryptographique du groupe
3. **Commits** : Les membres mettent à jour l'arbre lors de l'adhésion, du départ ou de la rotation des clés
4. **Chiffrement des messages** : Le contenu est chiffré à l'aide de clés dérivées du secret partagé du groupe

## Propriétés de sécurité clés

- **Confidentialité persistante** : Les messages passés restent sécurisés même si les clés actuelles sont compromises
- **Sécurité post-compromission** : Les messages futurs redeviennent sécurisés après la rotation des clés
- **Authentification des membres** : Tous les membres du groupe sont vérifiés cryptographiquement
- **Fonctionnement asynchrone** : Les membres peuvent rejoindre/quitter sans que tous les participants soient en ligne
- **Évolutivité** : Efficace pour des groupes jusqu'à 50 000 participants

## Standardisation

- **RFC 9420** (juillet 2023) : Spécification du protocole MLS de base
- **RFC 9750** (avril 2025) : Architecture MLS pour l'intégration système

## Adoption dans Nostr

Plusieurs applications Nostr utilisent MLS pour la messagerie de groupe sécurisée :

- **KeyChat** : Application de messagerie chiffrée basée sur MLS pour mobile et bureau
- **White Noise** : Messagerie privée utilisant MLS avec intégration du protocole Marmot
- **Marmot Protocol** : Extension Nostr fournissant un chiffrement de groupe basé sur MLS

MLS offre des garanties de sécurité plus fortes que NIP-04 ou NIP-44 seuls, particulièrement pour les discussions de groupe où les membres rejoignent et quittent dynamiquement.

## Adoption dans l'industrie

Au-delà de Nostr, MLS est adopté par :
- Google Messages (RCS avec MLS via GSMA Universal Profile 3.0)
- Apple Messages (support RCS annoncé pour MLS)
- Cisco WebEx, Wickr, Matrix

---

**Sources principales :**
- [RFC 9420: MLS Protocol](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: MLS Architecture](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS Working Group](https://datatracker.ietf.org/wg/mls/about/)
- [MLS Protocol Website](https://messaginglayersecurity.rocks/)

**Mentionné dans :**
- [Newsletter #3 : Sorties](/fr/newsletters/2025-12-31-newsletter/#releases)

**Voir aussi :**
- [Marmot Protocol](/fr/topics/marmot/)
- [MIP-05 : Notifications Push Préservant la Confidentialité](/fr/topics/mip-05/)
- [NIP-17 : Messages Directs Privés](/fr/topics/nip-17/)
- [NIP-44 : Charges Utiles Chiffrées](/fr/topics/nip-44/)
