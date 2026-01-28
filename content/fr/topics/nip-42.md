---
title: "NIP-42 : Authentification des clients auprès des relais"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-42 définit comment les clients s'authentifient auprès des relais. Les relais peuvent exiger une authentification pour fournir un contrôle d'accès, prévenir les abus ou implémenter des services de relais payants.

## Fonctionnement

Le flux d'authentification commence lorsqu'un relais envoie un message AUTH au client. Ce message contient une chaîne de défi que le client doit signer. Le client crée un événement d'authentification kind 22242 contenant le défi et le signe avec sa clé privée. Le relais vérifie la signature et le défi, puis accorde l'accès.

```json
{
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com"],
    ["challenge", "chaine-de-defi-aleatoire"]
  ],
  "content": "",
  "pubkey": "<pubkey_client>",
  "created_at": 1736784000,
  "sig": "<signature>"
}
```

Le défi empêche les attaques par rejeu : les clients doivent signer des défis frais pour chaque tentative d'authentification. L'URL du relais dans les tags garantit que les tokens d'authentification ne peuvent pas être réutilisés sur différents relais.

## Cas d'utilisation

Les relais payants utilisent NIP-42 pour vérifier les abonnés avant d'accorder l'accès. Après authentification, les relais peuvent vérifier le statut de paiement ou l'expiration de l'abonnement. Les relais privés restreignent l'accès aux pubkeys approuvées, créant des communautés fermées ou une infrastructure de relais personnelle.

La limitation de débit devient plus efficace avec l'authentification. Les relais peuvent suivre les taux de requêtes par pubkey authentifiée plutôt que par adresse IP, prévenant les abus tout en supportant les utilisateurs légitimes derrière des IP partagées. La prévention du spam s'améliore lorsque les relais exigent l'authentification pour publier des événements.

Certains relais utilisent NIP-42 pour l'analyse, suivant quels utilisateurs accèdent à quel contenu sans nécessiter de comptes centralisés. Combiné avec les métadonnées [NIP-11](/fr/topics/nip-11/), les clients découvrent si les relais nécessitent une authentification avant de tenter des connexions.

---

**Sources primaires :**
- [Spécification NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) - Authentification des clients auprès des relais

**Voir aussi :**
- [NIP-11 : Document d'information du relais](/fr/topics/nip-11/)
- [NIP-50 : Capacité de recherche](/fr/topics/nip-50/)
