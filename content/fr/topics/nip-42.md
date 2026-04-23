---
title: "NIP-42 : Authentification des clients auprès des relais"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-42 définit comment les clients s'authentifient auprès des relais. Les relais peuvent exiger une authentification pour fournir un contrôle d'accès, prévenir les abus ou implémenter des services de relais payants.

## Fonctionnement

Le flux d'authentification commence lorsqu'un relais envoie un message `AUTH` au client. Ce message contient une chaîne de défi que le client doit signer. Le client crée un événement d'authentification kind 22242 contenant le défi et le signe avec sa clé privée. Le relais vérifie la signature et le défi, puis accorde l'accès.

```json
{
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com"],
    ["challenge", "random-challenge-string"]
  ],
  "content": "",
  "pubkey": "<client_pubkey>",
  "created_at": 1736784000,
  "sig": "<signature>"
}
```

Le défi empêche les attaques par rejeu. L'URL du relais dans les tags empêche le même événement signé d'être réutilisé sur différents relais.

## Notes de protocole

L'authentification a une portée limitée à la connexion. Un défi reste valide pour la durée de la connexion, ou jusqu'à ce que le relais en envoie un nouveau. L'événement signé est éphémère et ne doit pas être diffusé comme un événement normal.

La spécification définit également des préfixes d'erreur lisibles par les machines. `auth-required:` signifie que le client ne s'est pas encore authentifié. `restricted:` signifie qu'il s'est authentifié, mais que cette pubkey n'a toujours pas la permission pour l'action demandée.

## Cas d'utilisation

Les relais payants utilisent NIP-42 pour vérifier les abonnés avant d'accorder l'accès. Les relais privés l'utilisent pour limiter les lectures ou écritures aux pubkeys approuvées. Cela améliore également la limitation de débit, car les relais peuvent suivre le comportement par clé authentifiée plutôt que par adresse IP.

Combiné avec les métadonnées [NIP-11](/fr/topics/nip-11/), les clients peuvent découvrir si un relais prend en charge NIP-42 avant de tenter des requêtes protégées. En pratique, le support reste inégal, donc les clients ont besoin d'un chemin de repli lorsqu'un relais annonce NIP-42 mais gère incorrectement les événements protégés.

---

**Sources principales :**
- [Spécification NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) - Authentification des clients auprès des relais

**Mentionné dans :**
- [Newsletter #6 : Documents d'information des relais](/fr/newsletters/2026-01-21-newsletter/)
- [Newsletter #9 : Test de statut de relais Marmot](/fr/newsletters/2026-02-11-newsletter/)
- [Newsletter #10 : Nostr MCP Server](/fr/newsletters/2026-02-18-newsletter/)
- [Newsletter #19 : strfry AUTH](/en/newsletters/2026-04-22-newsletter/)

**Voir aussi :**
- [NIP-11 : Document d'information du relais](/fr/topics/nip-11/)
- [NIP-50 : Capacité de recherche](/fr/topics/nip-50/)
