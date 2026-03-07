---
title: "BUD-10 : Schéma URI Blossom"
date: 2025-12-17
translationOf: /en/topics/bud-10.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---

BUD-10 définit le schéma URI `blossom:`, une référence portable de blob qui peut contenir des indications de serveur, des indications d'auteur et une taille attendue en plus du hash du fichier.

## Format URI

```
blossom:<sha256>.<ext>?xs=<server>&as=<pubkey>&sz=<bytes>
```

La spécification exige un hash SHA-256 en minuscules de 64 caractères et une extension de fichier. Si l'extension est inconnue, les clients doivent se rabattre sur `.bin`.

## Fonctionnement de la résolution

Les clients doivent résoudre une URI `blossom:` par étapes :

1. Essayer les indications de serveur `xs` dans l'ordre où elles apparaissent
2. Si des clés publiques d'auteur `as` sont présentes, récupérer la liste de serveurs [BUD-03](/fr/topics/bud-03/) de chaque auteur et essayer ces serveurs
3. Se rabattre sur les serveurs connus ou le cache local si nécessaire

Cet ordre est utile car il permet à l'expéditeur de fournir des indications immédiates pour une récupération rapide, tout en donnant au destinataire un chemin de secours si ces indications deviennent obsolètes.

## Pourquoi c'est important

Les URI `blossom:` fonctionnent davantage comme des liens magnet que comme des URL média ordinaires. Elles décrivent quel blob récupérer et incluent des indices sur où le trouver, au lieu de supposer qu'un hébergeur unique restera disponible indéfiniment.

Le champ optionnel `sz` ajoute une vérification d'intégrité concrète au-delà du hash. Les clients peuvent vérifier la taille attendue avant ou après le téléchargement, ce qui aide à détecter les transferts incomplets et améliore l'expérience utilisateur pour les fichiers volumineux.

---

**Sources principales :**
- [Spécification BUD-10](https://github.com/hzrd149/blossom/blob/master/buds/10.md)
- [Dépôt Blossom](https://github.com/hzrd149/blossom)

**Mentionné dans :**
- [Newsletter #1 : Actualités](/en/newsletters/2025-12-17-newsletter/#news)

**Voir aussi :**
- [Protocole Blossom](/fr/topics/blossom/)
- [BUD-03 : Liste de serveurs utilisateur](/fr/topics/bud-03/)
