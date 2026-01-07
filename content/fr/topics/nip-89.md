---
title: "NIP-89 : Gestionnaires d'applications recommandés"
date: 2026-01-07
draft: false
categories:
  - Discovery
  - Clients
  - Protocol
---

NIP-89 définit comment les applications peuvent annoncer leurs capacités et comment les utilisateurs peuvent recommander des applications qui gèrent des types d'événements spécifiques.

## Types d'événements

- **kind 31990** - Gestionnaire d'application (publié par les développeurs d'applications)
- **kind 31989** - Recommandation d'application (publiée par les utilisateurs)

## Comment ça fonctionne

1. **Les applications** publient des événements de gestionnaire décrivant quels types d'événements elles supportent et comment ouvrir le contenu
2. **Les utilisateurs** recommandent les applications qu'ils utilisent pour des types d'événements spécifiques
3. **Les clients** interrogent les recommandations pour offrir la fonctionnalité "ouvrir dans..." pour les types d'événements inconnus

## Gestionnaire d'application

```json
{
  "id": "<event-id>",
  "pubkey": "<app-developer-pubkey>",
  "created_at": 1736200000,
  "kind": 31990,
  "tags": [
    ["d", "<app-identifier>"],
    ["k", "30023"],
    ["web", "https://app.example.com/a/<bech32>", "naddr"],
    ["ios", "appname://open/<bech32>"]
  ],
  "content": "{\"name\": \"My App\", \"picture\": \"...\"}",
  "sig": "<signature>"
}
```

Les tags `k` spécifient les types d'événements supportés. Les modèles d'URL utilisent `<bech32>` comme espace réservé pour les entités encodées NIP-19.

## Recommandation utilisateur

```json
{
  "id": "<event-id>",
  "pubkey": "<user-pubkey>",
  "created_at": 1736200000,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:app-pubkey:identifier", "wss://relay", "web"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

Le tag `d` est le type d'événement recommandé. Plusieurs tags `a` peuvent recommander différentes applications pour différentes plateformes.

## Cas d'utilisation

- Découvrir des applications pouvant afficher des articles longs (kind 30023)
- Trouver des clients supportant des types d'événements spécifiques
- Fonctionnalité "ouvrir dans..." inter-clients
- Détecter les capacités des clients pour le support du chiffrement

---

**Sources principales :**
- [Spécification NIP-89](https://github.com/nostr-protocol/nips/blob/master/89.md)

**Mentionné dans :**
- [Newsletter #4 : Analyse approfondie des NIP](/fr/newsletters/2026-01-07-newsletter/#nip-44-chiffrement-versionné)

**Voir aussi :**
- [NIP-19 : Entités encodées Bech32](/fr/topics/nip-19/)
