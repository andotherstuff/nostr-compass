---
title: "NIP-22 : Commentaires"
date: 2026-01-28
translationOf: /en/topics/nip-22.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Social
---

NIP-22 définit un standard pour commenter n'importe quel contenu Nostr adressable, permettant des discussions en fil sur les articles, vidéos, événements de calendrier et autres événements adressables.

## Fonctionnement

Les commentaires utilisent des événements kind 1111 avec un `content` en texte brut. Les tags de portée racine sont en majuscules, et les tags de réponse parent sont en minuscules :

```json
{
  "kind": 1111,
  "tags": [
    ["A", "30023:pubkey:article-id", "wss://relay.example"],
    ["K", "30023"],
    ["P", "<root-pubkey>", "wss://relay.example"],
    ["a", "30023:pubkey:article-id", "wss://relay.example"],
    ["e", "<parent-event-id>", "wss://relay.example", "<parent-pubkey>"],
    ["k", "30023"],
    ["p", "<parent-pubkey>", "wss://relay.example"]
  ],
  "content": "Super article !"
}
```

## Structure des tags

- **`A` / `E` / `I`** - Portée racine de la discussion : événement adressable, ID d'événement ou identifiant externe
- **`K`** - Kind ou type de portée racine pour cet élément racine
- **`P`** - Auteur de l'événement racine quand il existe
- **`a` / `e` / `i`** - Parent immédiat auquel on répond
- **`k`** - Kind ou type de portée de l'élément parent
- **`p`** - Auteur de l'élément parent

Pour les commentaires de premier niveau, la racine et le parent pointent généralement vers la même cible. Pour les réponses aux commentaires, la racine reste fixe tandis que les tags parent en minuscules se déplacent vers le commentaire spécifique auquel on répond.

## Notes d'interopérabilité

Les commentaires NIP-22 ne sont pas un remplacement générique des réponses kind 1. La spécification dit explicitement que les commentaires ne doivent pas être utilisés pour répondre aux notes kind 1. Pour les fils note-à-note, les clients doivent continuer à utiliser [NIP-10](/fr/topics/nip-10/).

Une autre distinction utile est la portée. NIP-22 peut ancrer une discussion à des ressources non-note via les tags `I` et `i`, y compris des URLs et d'autres identifiants externes de [NIP-73](/fr/topics/nip-73/). Cela donne aux clients un moyen standard d'attacher des fils de commentaires à des pages web, podcasts ou d'autres objets hors-Nostr.

## Cas d'utilisation

- Discussions d'articles
- Commentaires vidéo
- Discussions sur les événements de calendrier [NIP-52](/fr/topics/nip-52/)
- Pages de discussion wiki
- Commentaires sur des ressources externes identifiées via les tags `I`

---

**Sources principales :**
- [Spécification NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md)

**Mentionné dans :**
- [Newsletter #7 : Notedeck](/en/newsletters/2026-01-28-newsletter/#notedeck)
- [Newsletter #10 : AI Agent NIPs Arrive](/en/newsletters/2026-02-18-newsletter/#ai-agent-nips-arrive)
- [Newsletter #12 : diVine](/en/newsletters/2026-03-04-newsletter/#divine)

**Voir aussi :**
- [NIP-10 : Fils de réponse](/fr/topics/nip-10/)
- [NIP-52 : Événements de calendrier](/fr/topics/nip-52/)
- [NIP-73 : IDs de contenu externe](/fr/topics/nip-73/)
