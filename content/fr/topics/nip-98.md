---
title: "NIP-98 : HTTP Auth"
date: 2026-03-25
translationOf: /en/topics/nip-98.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-98 définit l'authentification HTTP utilisant des événements Nostr. Il permet aux serveurs de vérifier l'identité Nostr d'un client sur des requêtes HTTP standard sans mots de passe, clés API ou flux OAuth.

## Fonctionnement

Lorsqu'un client a besoin d'authentifier une requête HTTP, il crée un événement kind 27235. Cet événement contient l'URL cible et la méthode HTTP dans ses tags, liant l'authentification à une requête spécifique.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1742860800,
  "kind": 27235,
  "tags": [
    ["u", "https://files.example.com/upload"],
    ["method", "POST"],
    ["payload", "<sha256-hash-of-request-body>"]
  ],
  "content": "",
  "sig": "<128-char hex>"
}
```

Le client signe cet événement, l'encode en base64, et l'envoie dans l'en-tête HTTP `Authorization` avec le schéma `Nostr` :

```
Authorization: Nostr <base64-encoded-signed-event>
```

Le serveur décode l'événement, vérifie la signature, contrôle que l'URL et la méthode correspondent à la requête réelle, et confirme que l'horodatage est récent. Si toutes les vérifications passent, le serveur sait quelle pubkey Nostr a effectué la requête.

Le tag optionnel `payload` contient un hachage SHA-256 du corps de la requête, ce qui empêche la réutilisation de l'événement d'authentification avec un contenu différent. La vérification de l'horodatage (les serveurs rejettent typiquement les événements de plus de quelques minutes) empêche les attaques par rejeu.

## Cas d'utilisation

Les serveurs Blossom utilisent NIP-98 pour authentifier les téléversements et suppressions de fichiers, liant les médias stockés à une identité Nostr spécifique. Les services d'hébergement de fichiers l'utilisent pour appliquer des quotas de téléversement par pubkey. Toute API HTTP qui a besoin d'identifier un utilisateur Nostr sans maintenir son propre système de comptes peut accepter les en-têtes NIP-98 comme preuve d'identité.

---

**Sources principales :**
- [Spécification NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) - HTTP Auth

**Mentionné dans :**
- [Newsletter #15](/fr/newsletters/2026-03-25-newsletter/)
