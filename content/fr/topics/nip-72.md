---
title: "NIP-72 : Communautés modérées"
date: 2026-03-25
translationOf: /en/topics/nip-72.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Communities
---

NIP-72 définit les communautés modérées sur Nostr. Les communautés fournissent un moyen d'organiser les publications autour d'un sujet ou groupe partagé, avec des modérateurs qui approuvent le contenu avant qu'il ne devienne visible pour les membres.

## Fonctionnement

Une communauté est définie par un événement kind 34550 publié par son créateur. Cet événement contient le nom de la communauté, la description, les règles et une liste de pubkeys de modérateurs. L'événement utilise un format d'événement remplaçable (plage de kinds 30000-39999), de sorte que la définition de la communauté peut être mise à jour au fil du temps.

```json
{
  "kind": 34550,
  "tags": [
    ["d", "example-community"],
    ["name", "Example Community"],
    ["description", "A community for discussing examples"],
    ["p", "<moderator_pubkey>", "", "moderator"],
    ["relay", "wss://relay.example.com", "moderator"]
  ],
  "content": "",
  "pubkey": "<creator_pubkey>",
  "created_at": 1742860800,
  "sig": "<signature>"
}
```

Les utilisateurs soumettent des publications à une communauté en taguant leurs événements avec un tag `a` pointant vers la définition de la communauté. Ces publications ne sont pas encore visibles pour les lecteurs de la communauté. Un modérateur examine la soumission et, si elle est approuvée, publie un événement d'approbation kind 4549 qui encapsule la publication originale. Les clients qui affichent la communauté ne montrent que les publications qui ont un événement d'approbation correspondant d'un modérateur reconnu.

Ce modèle d'approbation signifie que les communautés filtrent en lecture, pas en écriture. N'importe qui peut soumettre une publication, mais seules les publications approuvées apparaissent dans le flux de la communauté. Les modérateurs agissent comme des curateurs plutôt que comme des gardiens des données sous-jacentes.

## Considérations

Comme les événements d'approbation sont des événements Nostr séparés, les décisions de modération sont transparentes et vérifiables. Une publication rejetée par une communauté peut toujours être approuvée par une autre. Le même contenu peut exister dans plusieurs communautés avec une modération indépendante.

Le support des relays est important pour le fonctionnement des communautés. Les clients doivent interroger à la fois la définition de la communauté et les événements d'approbation, ce qui nécessite des relays qui indexent ces kinds d'événements efficacement.

Comparé aux groupes basés sur relay [NIP-29](/fr/topics/nip-29/), où le relay fait autorité à la fois sur l'appartenance et sur la modération, NIP-72 vit dans des événements Nostr ordinaires. Tout relay qui transporte les kinds `34550`, `4549` et les kinds de soumission peut servir une communauté, et la modération y est visible et forkable. Le compromis est que les soumissions non approuvées ne sont masquées qu'au niveau du rendu client, ce qui fait de NIP-29 un meilleur choix quand le spam doit rester hors du fil.

## Implémentations

- [noStrudel](https://github.com/hzrd149/nostrudel) supporte depuis longtemps les communautés NIP-72, y compris une file d'attente de soumissions en attente pour les modérateurs.
- [Amethyst](https://github.com/vitorpamplona/amethyst) a ajouté la création et la gestion complètes de communautés dans [PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) : définition de communauté kind `34550`, ajout de modérateurs et de relay hints, soumission de posts avec tag `a`, et gestion des approbations en attente via les événements kind `4549`.

---

**Sources principales :**
- [Spécification NIP-72](https://github.com/nostr-protocol/nips/blob/master/72.md) - Communautés modérées
- [Amethyst PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) - Création et modération de communautés NIP-72

**Mentionné dans :**
- [Newsletter #15](/fr/newsletters/2026-03-25-newsletter/)
- [Newsletter #19 : support des communautés dans Amethyst](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19 : deep dive NIP](/en/newsletters/2026-04-22-newsletter/)

**Voir aussi :**
- [NIP-29 : Groupes basés sur les relays](/fr/topics/nip-29/)
