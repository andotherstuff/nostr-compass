---
title: "NIP-4E : Découplage du chiffrement et de l'identité"
date: 2026-07-15
translationOf: /en/topics/nip-4e.md
translationDate: 2026-07-15
draft: false
categories:
  - NIP
  - Protocol
  - Encryption
---

NIP-4E est un brouillon ouvert, proposé par fiatjaf, pour le partage de données privées entre les propres appareils d'un utilisateur sans que chaque appareil détienne la clé d'identité Nostr principale de cet utilisateur. Il n'est pas fusionné et reste une proposition `draft`/`optional`.

## Le problème qu'il adresse

De nombreux NIPs existants, y compris les listes NIP-51 et les portefeuilles Cashu NIP-60, chiffrent les données d'un utilisateur vers lui-même en utilisant la clé d'identité afin de pouvoir les relire plus tard sur n'importe quel appareil. Cela ne fonctionne plus lorsque la clé d'identité n'est pas directement accessible, par exemple lorsqu'un signeur distant est protégé par des parts de seuil FROST, MuSig2, ou une enclave sécurisée hébergée, puisque le chiffrement et le déchiffrement nécessitent alors un aller-retour vers ce signeur à chaque fois. Cela rend également le chiffrement hors ligne impossible chaque fois que la clé de signature réside dans un bunker distant.

## Fonctionnement

NIP-4E sépare une « clé client » par appareil d'une « clé de chiffrement » partagée qui n'est pas la clé d'identité de l'utilisateur :

1. Le premier client qu'un utilisateur configure génère une paire de clés de chiffrement aléatoire et annonce sa moitié publique dans un event `kind:10044` signé par la clé d'identité de l'utilisateur.
2. Tout autre client souhaitant chiffrer ou déchiffrer des données pour cet utilisateur calcule son secret partagé Diffie-Hellman par rapport à la clé de chiffrement annoncée plutôt que par rapport à la clé d'identité.
3. Lorsqu'un second appareil installe un nouveau client, ce client génère sa propre « clé client » locale et publie une annonce `kind:4454` (également signée par la clé d'identité de l'utilisateur) demandant au premier client de partager la clé de chiffrement avec lui.
4. Le client original détecte la nouvelle annonce `kind:4454`, chiffre la clé de chiffrement partagée vers la clé du nouveau client en utilisant [NIP-44](/fr/topics/nip-44/), et la publie pour que le nouveau client puisse la déchiffrer et l'utiliser par la suite.

Le résultat est que le chiffrement et le déchiffrement ne nécessitent jamais de solliciter le signeur de la clé d'identité une fois qu'un client détient la clé de chiffrement partagée localement, et une configuration de signeur distant (FROST, MuSig2, enclave hébergée) peut être utilisée pour l'identité tandis que le chiffrement ordinaire reste rapide et fonctionne hors ligne.

## Pourquoi c'est important

NIP-4E est cité comme fondation pour d'autres propositions qui ont besoin d'une clé symétrique à l'échelle d'un drive ou d'un compte sans dépendre d'un signeur distant pour chaque appel de chiffrement/déchiffrement, y compris une proposition de drive privé chiffré ([PR #2412](https://github.com/nostr-protocol/nips/pull/2412)) et une version plus ciblée de la même idée spécifique à NIP-17 ([PR #2361](https://github.com/nostr-protocol/nips/pull/2361)). Les deux restent ouvertes aux côtés de NIP-4E lui-même, faisant de ceci un domaine actif et non stabilisé du protocole plutôt qu'un composant de base achevé.

---

**Sources primaires :**
- [Brouillon NIP-4E, PR #1647](https://github.com/nostr-protocol/nips/pull/1647)

**Mentionné dans :**
- [Bulletin #31 : Ouvert : un drive privé chiffré étend NIP-4E](/fr/newsletters/2026-07-15-newsletter/#open-private-encrypted-drive-extends-nip-4e)

**Voir aussi :**
- [NIP-44 : Charges utiles chiffrées](/fr/topics/nip-44/)
- [NIP-17 : Messages privés directs](/fr/topics/nip-17/)
- [NIP-46 : Nostr Connect](/fr/topics/nip-46/)
- [FROST](/fr/topics/frost/)
