---
title: "NIP-10 : Threading des notes textuelles"
date: 2025-12-24
translationOf: /en/topics/nip-10.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Social
---

NIP-10 spécifie comment les notes kind 1 se référencent mutuellement pour former des fils de réponses. Comprendre ce mécanisme est indispensable pour construire des vues de conversation.

## Fonctionnement

Lorsque quelqu'un répond à une note, les clients doivent savoir : à quoi est-ce une réponse ? Quelle est la racine de la conversation ? Qui doit être notifié ? NIP-10 répond à ces questions via les tags `e` (références d'événements) et les tags `p` (mentions de pubkeys).

## Tags marqués (méthode préférée)

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
  "content": "Great point! I agree.",
  "sig": "b7d3f..."
}
```

Le marqueur `root` pointe vers la note originale qui a lancé le fil. Le marqueur `reply` pointe vers la note spécifique à laquelle on répond. Si la réponse est directement à la racine, utilisez uniquement `root` (pas besoin de tag `reply`). La distinction compte pour le rendu : le `reply` détermine l'indentation dans une vue de fil, tandis que `root` regroupe toutes les réponses ensemble.

## Règles de threading

- **Réponse directe à la racine :** un tag `e` avec le marqueur `root`
- **Réponse à une réponse :** deux tags `e`, un `root` et un `reply`
- Le `root` reste constant tout au long du fil ; `reply` change selon la note à laquelle on répond

## Notifications et mentions

Incluez des tags `p` pour toutes les personnes qui devraient être notifiées. Au minimum, taguez l'auteur de la note à laquelle vous répondez. Par convention, on inclut aussi tous les tags `p` de l'événement parent, pour que tout le monde dans la conversation reste informé, plus tout utilisateur que vous mentionnez avec @ dans votre contenu.

## Indices de relais

La troisième position dans les tags `e` et `p` peut contenir une URL de relais où cet événement ou le contenu de cet utilisateur pourrait être trouvé. Cela aide les clients à récupérer le contenu référencé même s'ils ne sont pas connectés au relais d'origine.

## Notes d'interopérabilité

Les premières implémentations Nostr déduisaient le sens à partir de la position du tag plutôt que des marqueurs : le premier tag `e` était la racine, le dernier la réponse, ceux du milieu des mentions. Cette approche est obsolète car elle crée de l'ambiguïté. Si vous voyez des tags `e` sans marqueurs, ils proviennent probablement de clients anciens. Les implémentations modernes devraient toujours utiliser des marqueurs explicites.

Les clients doivent cependant analyser les deux formats s'ils veulent afficher correctement les anciens fils. En pratique, l'interopérabilité NIP-10 est en partie un problème de migration : les producteurs devraient émettre des tags marqués, mais les lecteurs devraient rester tolérants envers les anciennes formes positionnelles.

## Construction des vues de fil

Pour afficher un fil, récupérez l'événement racine, puis interrogez tous les événements ayant un tag `e` référençant cette racine :

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

Triez les résultats par `created_at` et utilisez les marqueurs `reply` pour construire la structure arborescente. Les événements dont le `reply` pointe vers la racine sont des réponses de premier niveau ; ceux dont le `reply` pointe vers une autre réponse sont des réponses imbriquées.

---

**Sources principales :**
- [Spécification NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md)

**Mentionné dans :**
- [Newsletter #2 : NIP Deep Dive](/en/newsletters/2025-12-24-newsletter/#nip-10-text-note-threading)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)
- [NIP-18 : Reposts](/fr/topics/nip-18/)
