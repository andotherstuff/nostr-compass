---
title: "NIP-02 : Liste de suivi"
date: 2025-12-24
translationOf: /en/topics/nip-02.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Social
---

NIP-02 définit les événements kind 3, qui stockent la liste de suivi d'un utilisateur. Cet événement sert de base aux fils d'actualité, aux notifications de réponses et à de nombreuses stratégies de sélection de relais.

## Fonctionnement

Un événement kind 3 contient des tags `p` listant les pubkeys suivies :

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

Chaque tag `p` possède quatre positions : le nom du tag, la pubkey suivie (hex), une URL de relais optionnelle en indice, et un « petname » optionnel (un surnom local). L'indice de relais indique aux autres clients où trouver les événements de cet utilisateur. Le petname permet d'attribuer des noms mémorables à ses contacts sans dépendre des noms d'affichage qu'ils se sont eux-mêmes attribués.

## Comportement remplaçable

Le kind 3 appartient à la plage remplaçable (0, 3, 10000-19999), les relais ne conservent donc que la dernière version par pubkey. Lorsque vous suivez une nouvelle personne, votre client publie un nouveau kind 3 complet contenant tous vos abonnements plus le nouveau. La liste de suivi doit donc être complète à chaque fois ; il n'est pas possible de publier des mises à jour incrémentales.

## Pourquoi c'est important

Pour construire un fil d'actualité, les clients récupèrent le kind 3 de l'utilisateur, extraient toutes les pubkeys des tags `p`, puis s'abonnent aux événements kind 1 de ces auteurs :

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

Le relais renvoie les notes correspondantes et le client les affiche. Les indices de relais dans le kind 3 aident les clients à savoir quels relais interroger pour chaque utilisateur suivi.

Cet événement est aussi le premier endroit où apparaît un état social obsolète. Si le dernier kind 3 d'un utilisateur est absent des relais interrogés, son fil peut sembler vide même si ses abonnements existent toujours ailleurs. Les clients qui fusionnent les résultats de plusieurs relais s'en sortent généralement mieux que ceux qui font confiance à un seul relais.

## Petnames et identité

Le champ petname permet un système de nommage décentralisé. Plutôt que de faire confiance au nom qu'un utilisateur revendique dans son profil, vous pouvez attribuer votre propre étiquette. Un client pourrait afficher « alice (Ma Sœur) » où « alice » provient de son profil kind 0 et « Ma Sœur » est votre petname. Cela fournit un contexte que les noms d'utilisateur globaux ne peuvent pas offrir.

## Notes d'interopérabilité

Parce que les événements kind 3 sont remplaçables et doivent être complets, les clients devraient préserver les tags inconnus lors des mises à jour. Si un autre client a ajouté des tags que le vôtre ne comprend pas, les écraser aveuglément entraînerait une perte de données.

La même prudence s'applique aux indices de relais et aux petnames. Ce sont des champs optionnels, mais les supprimer à l'écriture peut silencieusement dégrader l'expérience d'un autre client. Un chemin de mise à jour sûr consiste à : charger le dernier kind 3 connu, modifier uniquement les tags compris, conserver le reste, puis republier l'événement complet.

---

**Sources principales :**
- [Spécification NIP-02](https://github.com/nostr-protocol/nips/blob/master/02.md)

**Mentionné dans :**
- [Newsletter #2 : NIP Deep Dive](/en/newsletters/2025-12-24-newsletter/#nip-02-follow-list)

**Voir aussi :**
- [NIP-01 : Protocole de base](/fr/topics/nip-01/)
- [NIP-10 : Threading des notes textuelles](/fr/topics/nip-10/)
- [NIP-65 : Métadonnées de liste de relais](/fr/topics/nip-65/)
