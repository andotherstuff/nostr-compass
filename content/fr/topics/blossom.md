---
title: "Protocole Blossom"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

Blossom est un protocole d'hébergement média pour Nostr qui fournit un stockage de fichiers décentralisé avec des URLs adressables par contenu.

## Fonctionnement

Les fichiers sont stockés sur les serveurs Blossom et adressés par leur hash SHA256. Cela signifie :
- Le même fichier a toujours la même URL sur tous les serveurs
- Les fichiers peuvent être récupérés depuis n'importe quel serveur qui les possède
- Les clients peuvent vérifier l'intégrité du fichier en vérifiant le hash

## Fonctionnalités

- Stockage adressable par contenu
- Redondance multi-serveurs
- Découverte d'auteur via BUD-03
- Schéma URI personnalisé via BUD-10
- Pagination par curseur sur l'endpoint `/list`

---

**Sources principales :**
- [Dépôt Blossom](https://github.com/hzrd149/blossom)

**Mentionné dans :**
- [Newsletter #1 : Actualités](/fr/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2 : Changements notables de code](/fr/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)

**Voir aussi :**
- [BUD-03 : Liste de serveurs utilisateur](/fr/topics/bud-03/)
- [BUD-10 : Schéma URI Blossom](/fr/topics/bud-10/)

