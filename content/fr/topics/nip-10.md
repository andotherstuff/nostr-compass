---
title: "NIP-10 : Threading des notes textuelles"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-10 spécifie comment les notes kind 1 se référencent mutuellement pour former des fils de réponses. Comprendre ceci est essentiel pour construire des vues de conversation.

## Le problème

Quand quelqu'un répond à une note, les clients doivent savoir : À quoi est-ce une réponse ? Quelle est la racine de la conversation ? Qui devrait être notifié ? NIP-10 répond à ces questions à travers les tags `e` (références d'événements) et les tags `p` (mentions de clés publiques).

## Tags marqués (préféré)

Les clients modernes utilisent des marqueurs explicites dans les tags `e` :

```json
{
  "id": "f9c2e...",
  "pubkey": "a3b9c...",
  "created_at": 1734912345,
  "kind": 1,
  "tags": [
    ["e", "abc123...", "wss://relay.example.com", "root"],
    ["e", "def456...", "wss://relay.example.com", "reply"],
    ["p", "91cf9..."],
    ["p", "14aeb..."]
  ],
  "content": "Excellent point ! Je suis d'accord.",
  "sig": "b7d3f..."
}
```

Le marqueur `root` pointe vers la note originale qui a commencé le fil. Le marqueur `reply` pointe vers la note spécifique à laquelle on répond. Si vous répondez directement à la racine, utilisez seulement `root` (pas besoin de tag `reply`). La distinction compte pour l'affichage : le `reply` détermine l'indentation dans une vue de fil, tandis que `root` regroupe toutes les réponses ensemble.

## Règles de threading

- **Réponse directe à la racine :** Un tag `e` avec marqueur `root`
- **Réponse à une réponse :** Deux tags `e`, un `root` et un `reply`
- Le `root` reste constant tout au long du fil ; `reply` change selon ce à quoi vous répondez

## Tags pubkey pour les notifications

Incluez des tags `p` pour tous ceux qui devraient être notifiés. Au minimum, taguez l'auteur de la note à laquelle vous répondez. La convention est aussi d'inclure tous les tags `p` de l'événement parent (pour que tout le monde dans la conversation reste dans la boucle), plus tous les utilisateurs que vous @mentionnez dans votre contenu.

## Indications de relais

La troisième position dans les tags `e` et `p` peut contenir une URL de relais où cet événement ou le contenu de cet utilisateur pourrait être trouvé. Cela aide les clients à récupérer le contenu référencé même s'ils ne sont pas connectés au relais original.

## Tags positionnels dépréciés

Les premières implémentations Nostr déduisaient le sens de la position des tags plutôt que des marqueurs : le premier tag `e` était la racine, le dernier était la réponse, ceux du milieu étaient des mentions. Cette approche est dépréciée car elle crée de l'ambiguïté. Si vous voyez des tags `e` sans marqueurs, ils proviennent probablement de clients plus anciens. Les implémentations modernes devraient toujours utiliser des marqueurs explicites.

## Construction des vues de fil

Pour afficher un fil, récupérez l'événement racine, puis interrogez tous les événements avec un tag `e` référençant cette racine :

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

Triez les résultats par `created_at` et utilisez les marqueurs `reply` pour construire la structure d'arbre. Les événements dont le `reply` pointe vers la racine sont des réponses de premier niveau ; les événements dont le `reply` pointe vers une autre réponse sont des réponses imbriquées.

---

**Sources principales :**
- [Spécification NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md)

**Mentionné dans :**
- [Newsletter #2 : Analyse approfondie NIP](/fr/newsletters/2025-12-24-newsletter/#nip-10-text-note-threading)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)

