---
title: "NIP-44 : Payloads chiffrés"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Cryptography
  - Privacy
---

NIP-44 définit un standard de chiffrement versionné pour les payloads Nostr, remplaçant le schéma de chiffrement défaillant de NIP-04 par des primitives cryptographiques modernes.

## Fonctionnement

NIP-44 version 2 utilise un processus de chiffrement en plusieurs étapes :

1. **Accord de clés** : ECDH (secp256k1) entre les clés publiques de l'expéditeur et du destinataire produit un secret partagé
2. **Dérivation de clés** : HKDF-extract avec SHA256 et salt `nip44-v2` crée une clé de conversation
3. **Clés par message** : HKDF-expand dérive la clé ChaCha, le nonce et la clé HMAC à partir d'un nonce aléatoire
4. **Rembourrage** : Le contenu est rembourré pour masquer la longueur du message
5. **Chiffrement** : ChaCha20 chiffre le contenu rembourré
6. **Authentification** : HMAC-SHA256 assure l'intégrité du message

Le résultat est un payload base64 versionné qui s'insère dans un événement Nostr signé ordinaire. La spécification exige que les clients valident la signature NIP-01 de l'événement extérieur avant de déchiffrer le payload NIP-44 intérieur.

## Choix cryptographiques

- **ChaCha20** plutôt qu'AES : plus rapide, meilleure résistance aux attaques multi-clés
- **HMAC-SHA256** plutôt que Poly1305 : les MACs polynomiaux sont plus faciles à falsifier
- **SHA256** : cohérent avec les primitives Nostr existantes
- **Format versionné** : permet les futures mises à niveau d'algorithmes

## Propriétés de sécurité

- **Chiffrement authentifié** : les messages ne peuvent pas être altérés
- **Masquage de longueur** : le rembourrage obscurcit la taille du message
- **Clés de conversation** : la même clé pour les conversations continues réduit le calcul
- **Audité** : l'audit de sécurité Cure53 n'a trouvé aucune vulnérabilité exploitable

## Notes d'implémentation

NIP-44 n'est pas un remplacement direct des payloads NIP-04. Il définit un format de chiffrement, pas un type d'événement de message direct. Les protocoles tels que [NIP-17](/fr/topics/nip-17/) et [NIP-59](/fr/topics/nip-59/) définissent comment les payloads chiffrés sont utilisés dans les flux de messages réels.

L'entrée en texte clair est du texte UTF-8 d'une longueur de 1 à 65535 octets. C'est une contrainte réelle pour les implémenteurs : si votre application doit chiffrer des blobs binaires arbitraires, vous avez besoin d'un encodage supplémentaire ou d'un format de conteneur différent.

## Limitations

NIP-44 ne fournit pas :
- **Forward secrecy** : les clés compromises exposent les messages passés
- **Post-compromise security** : récupération après compromission de clés
- **Déniabilité** : les messages sont signés de manière prouvable par des clés spécifiques
- **Masquage des métadonnées** : l'architecture des relais limite la confidentialité

Pour les besoins de haute sécurité, NIP-104 (double ratchet) ou les protocoles basés sur MLS comme Marmot offrent des garanties plus fortes.

## Historique

La révision 3 de NIP-44 a été fusionnée en décembre 2023 suite à un audit de sécurité indépendant de Cure53. Elle constitue la base cryptographique des DMs privés NIP-17 et du gift wrapping NIP-59.

---

**Sources principales :**
- [Spécification NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [Implémentations de référence NIP-44](https://github.com/paulmillr/nip44)
- [Rapport d'audit Cure53](https://cure53.de/audit-report_nip44-implementations.pdf)

**Mentionné dans :**
- [Newsletter #4 : Analyse approfondie NIP](/en/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)
- [Newsletter #3 : Décembre 2023](/en/newsletters/2025-12-31-newsletter/#december-2023-ecosystem-maturation)
- [Newsletter #3 : Décembre 2024](/en/newsletters/2025-12-31-newsletter/#december-2024-protocol-advancement)
- [Newsletter #12 : Marmot](/en/newsletters/2026-03-04-newsletter/#marmot-development-kit-ships-first-public-release)

**Voir aussi :**
- [NIP-04 : Messages directs chiffrés (obsolète)](/fr/topics/nip-04/)
- [NIP-17 : Messages directs privés](/fr/topics/nip-17/)
- [NIP-59 : Gift Wrap](/fr/topics/nip-59/)
- [NIP-104 : Chiffrement Double Ratchet](/fr/topics/nip-104/)
- [MLS : Message Layer Security](/fr/topics/mls/)
