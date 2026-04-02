---
title: "NIP-43 : Métadonnées d'accès aux relays et demandes"
date: 2026-03-18
translationOf: /en/topics/nip-43.md
translationDate: 2026-04-01
draft: false
categories:
  - Protocol
  - Relay
  - Access Control
---

NIP-43 définit comment les relays publient des informations d'appartenance et comment les utilisateurs demandent l'admission, des invitations ou le retrait de relays restreints. Il donne au contrôle d'accès des relays une surface d'événements standard au lieu de forcer chaque relay privé ou semi-privé à inventer son propre protocole d'adhésion.

## Comment ça fonctionne

La spécification combine plusieurs kinds d'événements :

- kind `13534` publie une liste d'appartenance au relay
- kind `8000` annonce qu'un membre a été ajouté
- kind `8001` annonce qu'un membre a été retiré
- kind `28934` permet à un utilisateur de soumettre une demande d'adhésion avec un code de réclamation
- kind `28935` permet à un relay de retourner un code d'invitation sur demande
- kind `28936` permet à un utilisateur de demander la révocation de son propre accès

L'état d'appartenance n'est intentionnellement pas dérivé d'un seul événement. Un client peut avoir besoin de consulter à la fois les événements d'appartenance signés par le relay et les propres événements du membre avant de déterminer si l'accès est actuel.

## Pourquoi c'est important

NIP-43 donne aux relays restreints un moyen standard d'exprimer l'admission et l'état d'appartenance. Cela est important pour les systèmes de groupes, les communautés sur invitation et les relays qui ont besoin d'un processus d'intégration lisible par les machines sans recourir à des formulaires web hors bande ou des flux manuels d'opérateur.

La clarification ouverte dans [PR #2267](https://github.com/nostr-protocol/nips/pull/2267) précise un point pratique : les relays devraient maintenir un état d'appartenance autoritaire unique par pubkey. Cela aide les clients à éviter les historiques de rejeu ambigus où un ancien événement d'ajout ou de retrait peut être mal interprété comme l'état actuel.

## Notes d'interopérabilité

NIP-43 dépend du relay annonçant son support via son document [NIP-11](/fr/topics/nip-11/). Les demandes d'adhésion, d'invitation et de départ ne devraient être envoyées qu'aux relays qui déclarent explicitement supporter ce NIP.

Parce que les événements se situent simultanément dans les espaces contrôlés par le relay et par l'utilisateur, les implémentations ont besoin de règles de conflit claires. C'est pourquoi la clarification de l'état d'appartenance est plus importante qu'elle ne le paraît au premier abord.

---

**Sources principales :**
- [Spécification NIP-43](https://github.com/nostr-protocol/nips/blob/master/43.md)
- [PR #2267](https://github.com/nostr-protocol/nips/pull/2267) - Clarification de la gestion de l'état d'appartenance

**Mentionné dans :**
- [Newsletter #14 : Mises à jour des NIP](/fr/newsletters/2026-03-18-newsletter/#mises-à-jour-des-nip)

**Voir aussi :**
- [NIP-11 : Document d'information du relay](/fr/topics/nip-11/)
- [NIP-42 : Authentification des clients auprès des relays](/fr/topics/nip-42/)
