---
title: "Protocole Blossom"
date: 2025-12-17
translationOf: /en/topics/blossom.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---

Blossom est un protocole d'hébergement média pour Nostr qui stocke des blobs sur des serveurs HTTP ordinaires et les adresse par hash SHA-256 plutôt que par des identifiants assignés par le serveur.

## Fonctionnement

Les serveurs Blossom exposent une interface HTTP restreinte pour la récupération, le téléversement et la gestion des blobs. L'identifiant canonique est le hash du fichier, de sorte qu'un même blob conserve la même adresse sur tous les serveurs conformes.

- `GET /<sha256>` récupère un blob par son hash
- `PUT /upload` téléverse un blob
- les événements Nostr de kind `24242` autorisent les téléversements et les actions de gestion
- les événements de kind `10063`, définis dans [BUD-03](/fr/topics/bud-03/), permettent aux utilisateurs de publier leurs serveurs préférés

Comme le hash sert d'identifiant, les clients peuvent vérifier l'intégrité localement après téléchargement et tenter un autre serveur sans modifier la référence sous-jacente.

## Pourquoi c'est important

Blossom sépare le stockage des blobs des événements sociaux. Une note ou un profil peut pointer vers un média sans lier ce média au schéma d'URL d'un seul hébergeur.

Cela change aussi la gestion des pannes. Si un serveur disparaît, les clients peuvent récupérer le même hash depuis un miroir, un cache ou un serveur découvert via la liste [BUD-03](/fr/topics/bud-03/) de l'auteur. C'est une amélioration concrète par rapport aux systèmes média où l'URL de l'hébergeur d'origine est le seul localisateur.

## Notes d'interopérabilité

Blossom est modulaire. Le comportement de base pour la récupération et le téléversement est défini dans BUD-01 et BUD-02, tandis que la réplication, l'optimisation média, l'autorisation et le partage d'URI sont répartis dans des BUD séparés.

Cette séparation permet aux clients d'implémenter le minimum nécessaire pour l'interopérabilité de base, puis d'ajouter des éléments optionnels comme les indications URI [BUD-10](/fr/topics/bud-10/) ou la mise en cache locale au fur et à mesure que le support mûrit.

---

**Sources principales :**
- [Dépôt Blossom](https://github.com/hzrd149/blossom)
- [BUD-01 : Exigences serveur et récupération de blobs](https://github.com/hzrd149/blossom/blob/master/buds/01.md)
- [BUD-02 : Téléversement et gestion de blobs](https://github.com/hzrd149/blossom/blob/master/buds/02.md)
- [Guide du cache local Blossom](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md)

**Mentionné dans :**
- [Newsletter #1 : Actualités](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2 : Changements notables de code et documentation](/en/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)
- [Newsletter #10 : La couche de cache local Blossom émerge](/en/newsletters/2026-02-18-newsletter/#blossom-local-cache-layer-emerges)

**Voir aussi :**
- [BUD-03 : Liste de serveurs utilisateur](/fr/topics/bud-03/)
- [BUD-10 : Schéma URI Blossom](/fr/topics/bud-10/)
