---
title: "BUD-10 : Schéma URI Blossom"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-10 définit un schéma URI personnalisé pour Blossom qui intègre toutes les informations nécessaires pour récupérer un fichier depuis n'importe quel serveur disponible.

## Format URI

```
blossom:<sha256>.<ext>?size=<bytes>&server=<url>&server=<url>&pubkey=<hex>
```

Composants :
- **sha256** : Hash du fichier (requis)
- **ext** : Extension du fichier
- **size** : Taille du fichier en octets
- **server** : Une ou plusieurs indications de serveur
- **pubkey** : Clés publiques des auteurs pour la découverte de serveur BUD-03

## Avantages

- Plus résilient que les URLs HTTP statiques
- Basculement automatique entre plusieurs serveurs
- Découverte basée sur l'auteur via les indications de clé publique
- Auto-vérifiable (le hash assure l'intégrité)

---

**Sources principales :**
- [PR BUD-10](https://github.com/hzrd149/blossom/pull/84)

**Mentionné dans :**
- [Newsletter #1 : Actualités](/fr/newsletters/2025-12-17-newsletter/#news)

**Voir aussi :**
- [Protocole Blossom](/fr/topics/blossom/)
- [BUD-03 : Liste de serveurs utilisateur](/fr/topics/bud-03/)

