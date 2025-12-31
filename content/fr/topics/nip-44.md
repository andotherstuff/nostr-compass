---
title: "NIP-44: Encrypted Payloads"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2025-12-31
draft: false
categories:
  - NIP
  - Cryptographie
  - Confidentialité
---

NIP-44 définit un standard de chiffrement versionné pour les payloads Nostr, remplaçant le schéma de chiffrement défaillant de NIP-04 par des primitives cryptographiques modernes.

## Comment Ça Fonctionne

NIP-44 version 2 utilise un processus de chiffrement en plusieurs étapes :

1. **Accord de Clés** : ECDH (secp256k1) entre les clés publiques de l'expéditeur et du destinataire produit un secret partagé
2. **Dérivation de Clés** : HKDF-extract avec SHA256 et salt `nip44-v2` crée une clé de conversation
3. **Clés Par Message** : HKDF-expand dérive la clé ChaCha, nonce et clé HMAC d'un nonce aléatoire
4. **Rembourrage** : Le contenu est rembourré pour masquer la longueur du message
5. **Chiffrement** : ChaCha20 chiffre le contenu rembourré
6. **Authentification** : HMAC-SHA256 assure l'intégrité du message

## Choix Cryptographiques

- **ChaCha20** plutôt qu'AES : Plus rapide, meilleure résistance aux attaques multi-clés
- **HMAC-SHA256** plutôt que Poly1305 : Les MACs polynomiaux sont plus faciles à falsifier
- **SHA256** : Cohérent avec les primitives Nostr existantes
- **Format Versionné** : Permet les futures mises à niveau d'algorithmes

## Propriétés de Sécurité

- **Chiffrement Authentifié** : Les messages ne peuvent pas être altérés
- **Masquage de Longueur** : Le rembourrage obscurcit la taille du message
- **Clés de Conversation** : La même clé pour les conversations continues réduit le calcul
- **Audité** : L'audit de sécurité Cure53 n'a trouvé aucune vulnérabilité exploitable

## Limitations

NIP-44 ne fournit pas :
- **Forward Secrecy** : Les clés compromises exposent les messages passés
- **Post-Compromise Security** : Récupération après compromission de clés
- **Déniabilité** : Les messages sont probablement signés par des clés spécifiques
- **Masquage des Métadonnées** : L'architecture des relays limite la confidentialité

Pour les besoins de haute sécurité, NIP-104 (double ratchet) ou les protocoles basés sur MLS comme Marmot offrent des garanties plus fortes.

## Histoire

NIP-44 révision 3 a été fusionné en décembre 2023 suite à un audit de sécurité indépendant de Cure53. Il constitue la base cryptographique pour les DMs privés NIP-17 et le gift wrapping NIP-59.

---

**Sources primaires :**
- [Spécification NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [Implémentations de Référence NIP-44](https://github.com/paulmillr/nip44)
- [Rapport d'Audit Cure53](https://cure53.de/audit-report_nip44-implementations.pdf)

**Mentionné dans :**
- [Newsletter #3 : Décembre 2023](/fr/newsletters/2025-12-31-newsletter/#december-2023-ecosystem-maturation)
- [Newsletter #3 : Décembre 2024](/fr/newsletters/2025-12-31-newsletter/#december-2024-protocol-advancement)

**Voir aussi :**
- [NIP-04: Encrypted Direct Messages (obsolète)](/fr/topics/nip-04/)
- [NIP-17: Messages Directs Privés](/fr/topics/nip-17/)
- [NIP-59: Gift Wrap](/fr/topics/nip-59/)
- [NIP-104: Double Ratchet Encryption](/fr/topics/nip-104/)
- [MLS: Message Layer Security](/fr/topics/mls/)
