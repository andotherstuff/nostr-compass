---
title: "Keycast : signature à distance Nostr en équipe"
date: 2026-05-21
draft: false
translationOf: /en/topics/keycast.md
translationDate: 2026-07-01
categories:
  - Signing
  - Security
  - Teams
---

Keycast est un serveur de signature à distance NIP-46 auto-hébergé conçu pour les équipes. Il stocke les clés privées Nostr chiffrées au repos dans SQLite, génère des chaînes de connexion NIP-46 bunker, et exécute des processus signataires qui approuvent ou refusent les demandes de signature à distance selon des politiques configurables par clé. Le projet est maintenu par l'organisation Marmot Protocol.

## Comment ça marche

Le serveur comporte quatre composants principaux : une API Axum qui gère la gestion d'équipe et l'authentification HTTP NIP-98, une interface web SvelteKit qui utilise NIP-07 pour l'authentification, un gestionnaire de signataires qui surveille les lignes d'autorisation et engendre un `signer_daemon` par autorisation, et une base de données SQLite avec migrations.

Les membres de l'équipe se connectent via leur extension navigateur NIP-07. L'application web demande un événement d'auth HTTP NIP-98 signé localement par l'extension, puis envoie cet en-tête d'auth à l'API. L'API vérifie l'événement, extrait le pubkey, et contrôle l'appartenance à l'équipe. Les clés stockées sont chiffrées avec un fichier racine `master.key` qui doit être monté séparément de l'image et jamais commité.

Le daemon signataire déchiffre la clé stockée et la clé bunker au démarrage, se connecte aux relais configurés, et appelle `Authorization::validate_policy` avant d'approuver chaque demande de signature NIP-46. Les politiques spécifient quels kinds d'événements une connexion bunker particulière est autorisée à signer.

## Audit de sécurité (mai 2026)

Un audit de sécurité achevé en mai 2026 a traité des problèmes d'authentification, de permissions, d'intégrité des données et de dépendances. Changements clés :

- L'auth NIP-98 exige désormais exactement une balise `u` et une balise `method`, rejette les horodatages périmés ou futurs, et valide les hachages `payload` du corps de la requête
- `ALLOWED_PUBKEYS` est analysé strictement et appliqué côté serveur ; le frontend expose `/api/config?pubkey=<hex>` pour que le navigateur puisse vérifier le statut d'autorisation sans recevoir la liste complète du serveur
- Les politiques vides refusent par défaut les demandes de signature/chiffrement/déchiffrement ; la création de politique rejette les configurations de permissions inconnues ou malformées
- Les connexions SQLite activent l'application des clés étrangères ; la suppression d'équipe ne perd plus les données de jointure de permissions avant le nettoyage
- La protection des routes côté serveur couvre désormais les routes imbriquées de l'application telles que `/teams/:id`
- Les réponses web définissent les en-têtes CSP, frame, content-type, referrer, permissions et HSTS
- Une migration SQL normalise l'ancien JSON de permissions allowed-kinds de `{"sign":[...]}` vers `{"allowed_kinds":[...]}` au démarrage

L'audit signale les éléments résiduels dans [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md) à traiter avant de confier au déploiement de vraies clés d'équipe.

## Déploiement

Le déploiement Docker Compose monte `master.key` dans les conteneurs API et signataire, exécute les conteneurs avec un UID/GID non-root et un système de fichiers racine en lecture seule, et utilise les étiquettes Caddy pour router `/api/*` vers l'API et le reste vers l'application web. L'image publiée à `ghcr.io/marmot-protocol/keycast` est étiquetée `master`, `latest` et `sha-<commit>`.

---

**Sources primaires :**
- [Dépôt Keycast](https://github.com/marmot-protocol/keycast)
- [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md) - Résultats de l'audit de sécurité de mai 2026

**Mentionné dans :**
- [Newsletter #23 : Audit de sécurité Keycast terminé](/fr/newsletters/2026-05-21-newsletter/#keycast-security-audit-complete)

**Voir aussi :**
- [NIP-46 : Signature à distance Nostr](/fr/topics/nip-46/)
- [NIP-07 : Signataire d'extension navigateur](/fr/topics/nip-07/)
- [Marmot Protocol](/fr/topics/marmot/)
