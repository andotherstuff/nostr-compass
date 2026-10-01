---
title: "Buzz NIP-AR : Artefacts de canal"
date: 2026-09-30
draft: false
categories:
  - Project Proposals
  - Collaboration
translationOf: /en/topics/nip-ar.md
translationDate: 2026-10-01
---

NIP-AR est la spécification des artefacts de canal de Buzz, **propre au projet**. Cette désignation ne signifie pas qu'elle a été adoptée par le dépôt `nostr-protocol/nips` ou par d'autres relay.

## Modèle d'artefact

Un artefact est un enregistrement modifiable doté d'une identité `d` stable, rattaché à un seul canal dans un tag `h`, et dont les révisions sont des instantanés complets reliés par `prev`. Un relay n'accepte une modification que si `prev` désigne la version de tête actuelle. Deux révisions concurrentes ne peuvent donc pas toutes deux devenir la prochaine version de tête. L'implémentation de Buzz utilise le kind `45010` pour les artefacts et un marqueur de kind `45011` signé par le relay lorsqu'un artefact quitte un canal. Le canal source voit le retrait sans que ce marqueur lui révèle la destination.

La [fusion de la spécification de Buzz](https://github.com/block/buzz/pull/7791) décrit le modèle, et la [fusion de l'implémentation du relay](https://github.com/block/buzz/pull/7919) fait état de tests portant sur la gestion des conflits, les requêtes d'historique, les déplacements et les permissions des canaux. Ces fusions établissent le comportement du code source du projet, et non une norme générale de Nostr ou une garantie de déploiement public.

---

**Sources primaires :**
- [Fusion de la spécification des artefacts de canal de Buzz](https://github.com/block/buzz/pull/7791)
- [Fusion de l'implémentation des artefacts de canal de Buzz](https://github.com/block/buzz/pull/7919)

**Mentionné dans :**
- [Lettre d'information #42 : artefacts de canal de Buzz](/fr/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
