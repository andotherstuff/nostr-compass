---
title: "NIP-37 : Enveloppes de brouillons"
date: 2026-07-01
draft: false
translationOf: /en/topics/nip-37.md
translationDate: 2026-07-01
categories:
  - NIP
  - Drafts
  - Privacy
---

NIP-37 définit un événement de stockage chiffré pour les brouillons d'événements non signés de tout kind. Un utilisateur composant un article long, un événement de calendrier à venir ou un message qu'il souhaite peut-être envoyer plus tard peut stocker le brouillon sur les relais sous un événement de kind `31234`, chiffré avec sa propre clé via [NIP-44](/fr/topics/nip-44/). Le brouillon est récupérable depuis n'importe quel client qui détient la clé de l'utilisateur, et le même NIP définit un événement de liste `kind:10013` distinct qui nomme les relais sur lesquels l'utilisateur souhaite stocker ses brouillons privés.

## Comment ça marche

Une enveloppe de brouillon est un événement remplaçable paramétré de kind `31234`. L'événement brouillon non signé est sérialisé en JSON, chiffré via NIP-44 vers la clé publique du signataire, et placé dans `.content`. Un tag `k` déclare le kind du brouillon afin qu'un client puisse regrouper les brouillons par type d'événement. Un tag `d` porte l'identifiant du brouillon pour que l'enveloppe puisse être remplacée à mesure que le brouillon évolue, et un tag `expiration` NIP-40 est recommandé pour que les vieux brouillons expirent automatiquement.

```json
{
  "kind": 31234,
  "tags": [
    ["d", "<identifier>"],
    ["k", "<kind of the draft event>"],
    ["expiration", "<unix-timestamp>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

Un champ `.content` vidé signale que le brouillon a été supprimé.

## Points de contrôle

Le kind `1234` définit des points de contrôle appartenant à un événement parent `kind:31234`. Les points de contrôle portent un tag `a` pointant vers le brouillon parent et permettent à un client de stocker l'historique des révisions aux côtés du dernier brouillon.

```json
{
  "kind": 1234,
  "tags": [
    ["a", "31234:<pubkey>:<identifier>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

## Liste de relais pour contenu privé (kind 10013)

Le kind `10013` est un événement remplaçable dont les tags listent les relais sur lesquels l'utilisateur souhaite stocker du contenu privé, y compris les enveloppes de brouillons. Les clients publiant kind `31234` DEVRAIENT publier sur les relais listés dans l'événement kind `10013` de l'utilisateur. Cela sépare l'ensemble de relais utilisé pour la publication publique (NIP-65) de l'ensemble de relais utilisé pour le stockage de contenu privé, afin qu'un utilisateur puisse épingler ses brouillons privés à un petit ensemble de relais de confiance sans exposer cet ensemble dans son outbox public.

## Implémentations

- [Notedeck](https://github.com/damus-io/notedeck) - stocke les relais de synchronisation privée sous forme de liste kind-10013 (ajouté en juin 2026)

---

**Sources primaires :**
- [Spécification NIP-37](https://github.com/nostr-protocol/nips/blob/master/37.md)
- [Commit Notedeck stockant les relais de synchronisation privée en kind-10013](https://github.com/damus-io/notedeck) - L'équipe Damus adopte la spécification pour la gestion des relais de synchronisation desktop

**Mentionné dans :**
- [Newsletter #29 : Notedeck](/fr/newsletters/2026-07-01-newsletter/#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments)

**Voir aussi :**
- [NIP-44 : Chiffrement versionné](/fr/topics/nip-44/)
- [NIP-65 : Métadonnées de liste de relais](/fr/topics/nip-65/)
