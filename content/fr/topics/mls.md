---
title: "MLS (Message Layer Security)"
date: 2025-12-31
translationOf: /en/topics/mls.md
translationDate: 2026-03-07
draft: false
categories:
  - Cryptography
  - Protocol
  - Messaging
  - Privacy
---

Message Layer Security (MLS) est un protocole IETF pour la messagerie de groupe chiffrée de bout en bout. Il fournit la confidentialité persistante et la sécurité post-compromission pour des groupes dont la composition peut évoluer au fil du temps.

## Fonctionnement

MLS utilise une structure d'accord de clés basée sur un arbre appelée TreeKEM :

1. **Key Packages** : chaque participant publie un paquet de clés contenant son identité et ses clés de chiffrement
2. **État du groupe** : un arbre à cliquet maintient l'état cryptographique du groupe
3. **Commits** : les membres mettent à jour l'arbre lors de l'adhésion, du départ ou de la rotation des clés
4. **Chiffrement des messages** : le contenu est chiffré à l'aide de clés dérivées du secret partagé du groupe

## Pourquoi c'est important

MLS résout un problème que le chiffrement par paires ne résout pas bien : maintenir la cohérence de l'appartenance au groupe et de l'état de chiffrement lorsque des membres rejoignent, quittent ou font tourner leurs clés de manière asynchrone.

Sa structure arborescente est l'idée pratique. Les mises à jour n'exigent pas que chaque participant renégocie bilatéralement avec tous les autres, donc le protocole passe mieux à l'échelle que les schémas de clés de groupe ad hoc.

## Standardisation

- **RFC 9420** (juillet 2023) : spécification du protocole MLS de base
- **RFC 9750** (avril 2025) : architecture MLS pour l'intégration système

## Adoption dans Nostr

Plusieurs applications Nostr utilisent MLS pour la messagerie de groupe sécurisée :

- **KeyChat** : application de messagerie chiffrée basée sur MLS pour mobile et bureau
- **White Noise** : messagerie privée utilisant MLS avec intégration du protocole Marmot
- **Marmot Protocol** : extension Nostr fournissant un chiffrement de groupe basé sur MLS

MLS offre des garanties de sécurité de groupe plus fortes que [NIP-04](/fr/topics/nip-04/) ou [NIP-44](/fr/topics/nip-44/) seuls, en particulier lorsque la composition du groupe change fréquemment.

## Compromis

MLS n'est pas un produit de messagerie complet. Les applications ont encore besoin d'identité, de transport, de résistance au spam, de stockage et de gestion des conflits autour du protocole.

C'est pourquoi les projets Nostr comme Marmot ajoutent des règles supplémentaires par-dessus MLS. La cryptographie est standardisée, mais le protocole applicatif environnant reste déterminant pour l'interopérabilité.

---

**Sources principales :**
- [RFC 9420: MLS Protocol](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: MLS Architecture](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS Working Group](https://datatracker.ietf.org/wg/mls/about/)
- [MLS Protocol Website](https://messaginglayersecurity.rocks/)

**Mentionné dans :**
- [Newsletter #3 : Sorties](/fr/newsletters/2025-12-31-newsletter/#releases)
- [Newsletter #10](/fr/newsletters/2026-02-18-newsletter/)
- [Newsletter #12](/fr/newsletters/2026-03-04-newsletter/)

**Voir aussi :**
- [Protocole Marmot](/fr/topics/marmot/)
- [MIP-05 : Notifications push préservant la vie privée](/fr/topics/mip-05/)
- [NIP-17 : Messages directs privés](/fr/topics/nip-17/)
- [NIP-44 : Charges utiles chiffrées](/fr/topics/nip-44/)
