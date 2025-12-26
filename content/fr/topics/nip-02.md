---
title: "NIP-02 : Liste d'abonnements"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-02 définit les événements kind 3, qui stockent votre liste d'abonnements. Ce mécanisme simple alimente le graphe social qui rend les timelines possibles.

## Structure

Un événement kind 3 contient des tags `p` listant les clés publiques suivies :

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

Chaque tag `p` a quatre positions : le nom du tag, la clé publique suivie (hex), une indication de relais URL optionnelle, et un « petname » optionnel (un surnom local). L'indication de relais dit aux autres clients où trouver les événements de cet utilisateur. Le petname vous permet d'assigner des noms mémorables aux contacts sans vous fier à leurs noms d'affichage auto-déclarés.

## Comportement remplaçable

Le Kind 3 tombe dans la plage remplaçable (0, 3, 10000-19999), donc les relais ne gardent que la dernière version par clé publique. Quand vous suivez quelqu'un de nouveau, votre client publie un nouveau kind 3 complet contenant tous vos abonnements plus le nouveau. Cela signifie que les listes d'abonnements doivent être complètes à chaque fois ; vous ne pouvez pas publier de mises à jour incrémentales.

## Construction des timelines

Pour construire un flux d'accueil, les clients récupèrent le kind 3 de l'utilisateur, extraient toutes les clés publiques des tags `p`, puis s'abonnent aux événements kind 1 de ces auteurs :

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

Le relais renvoie les notes correspondantes, et le client les affiche. Les indications de relais dans le kind 3 aident les clients à savoir quels relais interroger pour chaque utilisateur suivi.

## Petnames et identité

Le champ petname permet un schéma de nommage décentralisé. Plutôt que de faire confiance au nom qu'un utilisateur revendique dans son profil, vous pouvez assigner votre propre étiquette. Un client pourrait afficher « alice (Ma Sœur) » où « alice » vient de son profil kind 0 et « Ma Sœur » est votre petname. Cela fournit un contexte que les noms d'utilisateur globaux ne peuvent pas offrir.

## Considérations pratiques

Parce que les événements kind 3 sont remplaçables et doivent être complets, les clients devraient préserver les tags inconnus lors de la mise à jour. Si un autre client a ajouté des tags que votre client ne comprend pas, écraser aveuglément perdrait ces données. Ajoutez les nouveaux abonnements plutôt que de reconstruire à partir de zéro.

---

**Sources principales :**
- [Spécification NIP-02](https://github.com/nostr-protocol/nips/blob/master/02.md)

**Mentionné dans :**
- [Newsletter #2 : Analyse approfondie NIP](/fr/newsletters/2025-12-24-newsletter/#nip-02-follow-list)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)

