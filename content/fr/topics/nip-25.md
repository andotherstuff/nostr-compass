---
title: "NIP-25 : Réactions"
date: 2026-07-29
translationOf: /en/topics/nip-25.md
translationDate: 2026-08-26
draft: false
categories:
  - Protocol
  - Social
---

NIP-25 définit les réactions comme des événements kind `7`. Il donne aux clients une forme d'événement partagée pour attacher un emoji ou une autre réaction courte à une note, un article, une annonce classée ou un autre événement référencé.

## Comment ça fonctionne

Un événement de réaction porte son texte de réaction dans `content` et référence la cible via le tag `e` de l'événement cible. Quand la cible est adressable, la réaction inclut aussi son tag `a`. Elle inclut également des tags `p` pour l'auteur de l'événement référencé, ce qui permet aux relays et aux clients d'acheminer les notifications sans déduire les destinataires du contenu de l'événement.

La réaction par défaut est `+`, de sorte que les clients peuvent traiter un contenu de réaction vide comme une réponse positive. D'autres emoji sont des valeurs de réaction valides. La spécification autorise aussi `-` pour une réaction négative, que le complément de juillet 2022 a ajouté après l'introduction initiale.

Les clients devraient préserver la référence à la cible et les tags d'auteur lors de la création d'une réaction. Une réaction est un événement signé ordinaire ; elle peut donc circuler par les souscriptions de relay habituelles et être affichée par tout client qui reconnaît le kind `7`.

## Implémentations

NIP-25 est largement implémenté par les clients et bibliothèques Nostr dans le cadre de l'interaction ordinaire avec les notes. Son modèle simple de kind et de tags permet aux clients d'afficher des compteurs, des réactions individuelles et des notifications sans protocole de transport distinct.

---

**Sources primaires :**
- [NIP-25 Specification](https://github.com/nostr-protocol/nips/blob/master/25.md)
- [Commit d'introduction](https://github.com/nostr-protocol/nips/commit/dcbd504639d20d1b0ae6bb837609710645781b88)
- [Complément sur le vote négatif](https://github.com/nostr-protocol/nips/commit/89bb08ba8683)

**Mentionné dans :**
- [Newsletter #33 : Six mois de juillet dans l'histoire de Nostr](/fr/newsletters/2026-07-29-newsletter/#six-mois-de-juillet-dans-lhistoire-de-nostr)
- [Newsletter #37 : Marmot](/fr/newsletters/2026-08-26-newsletter/#marmot)

**Voir aussi :**
- [NIP-01: Basic Protocol](/fr/topics/nip-01/)
- [NIP-10: Text Note Threading](/fr/topics/nip-10/)
