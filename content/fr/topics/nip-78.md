---
title: "NIP-78 : Données spécifiques aux applications"
date: 2026-05-14
draft: false
translationOf: /en/topics/nip-78.md
translationDate: 2026-05-13
categories:
  - NIPs
  - Data Storage
---

NIP-78 définit un kind d'événement standard permettant aux applications de stocker des données arbitraires pour le compte d'un utilisateur via des événements Nostr, permettant la synchronisation d'état entre appareils sans serveur centralisé.

## Fonctionnement

Le kind d'événement central est 30078, un événement remplaçable paramétré. La balise `d` est une chaîne d'identifiant définie par l'application qui délimite l'espace de stockage à une application et un usage spécifiques.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1747180800,
  "kind": 30078,
  "tags": [
    ["d", "myapp-settings"]
  ],
  "content": "{\"theme\":\"dark\",\"fontSize\":14}",
  "sig": "<128-char hex>"
}
```

Une application publie un événement 30078 avec une balise `d` unique (par exemple `tamagostrich-pet-state` ou `amethyst-settings`) et le contenu JSON ou texte qu'elle doit persister. Comme 30078 est remplaçable et délimité par la balise `d`, mettre à jour l'état stocké signifie publier un nouvel événement avec la même balise `d`; le relais ne conserve que la dernière version.

## Synchronisation entre appareils

Tout client connaissant la clé publique d'un utilisateur et la balise `d` de l'application peut récupérer l'état actuel depuis l'ensemble de relais de l'utilisateur et le reconstruire sur n'importe quel appareil. L'utilisateur possède les données car elles résident dans des événements signés par sa paire de clés, stockés sur des relais de sa liste de relais [NIP-65](/fr/topics/nip-65/).

## Données privées vs. publiques

Pour les données d'application privées, le champ de contenu peut être chiffré avec [NIP-44](/fr/topics/nip-44/) avant publication, de sorte que le relais ne stocke que du texte chiffré que seul le détenteur de la clé peut déchiffrer. Les données d'application publiques peuvent être stockées non chiffrées pour que d'autres clients puissent les lire et les afficher.

## Format du contenu

NIP-78 laisse délibérément le format du contenu ouvert; les applications choisissent leur propre schéma. La convention courante est de préfixer les balises `d` avec le nom de l'application pour éviter les collisions entre les apps utilisant le même relais.

## Implémentations

- [Tamagostrich](https://github.com/Negr087/tamagostrich) — synchronisation de l'état de l'animal de compagnie entre appareils via des événements `tamagostrich-pet-state` kind:30078
- [Wisp](https://github.com/barrydeen/wisp-android) — sauvegarde de portefeuille kind:30078 et synchronisation des paramètres de sécurité entre appareils; abonnements outbox fusionnés en un seul REQ utilisant le filtre d'auteur NIP-78
- [NosPress](https://github.com/nostrapps/nospress) — état d'orchestration CMS stocké dans des événements NIP-78
- Plusieurs implémentations de synchronisation de paramètres de clients Nostr (Amethyst, autres)

---

**Sources primaires :**
- [Spécification NIP-78](https://github.com/nostr-protocol/nips/blob/master/78.md)
- [Tamagostrich](https://github.com/Negr087/tamagostrich) — implémentation en production

**Mentionné dans :**
- [Newsletter #22 : NIP-78 Deep Dive](/fr/newsletters/2026-05-14-newsletter/#nip-deep-dive-nip-78-app-specific-data)
- [Newsletter #22 : Tamagostrich](/fr/newsletters/2026-05-14-newsletter/#tamagostrich-launches-a-decentralized-nip-78-tamagotchi-with-sats-rewards)

**Voir aussi :**
- [NIP-51 : Listes](/fr/topics/nip-51/)
- [NIP-44 : Chiffrement versionné](/fr/topics/nip-44/)
- [NIP-65 : Métadonnées de liste de relais](/fr/topics/nip-65/)
