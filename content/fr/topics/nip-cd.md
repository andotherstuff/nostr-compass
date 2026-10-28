---
title: "NIP-CD : commandes slash"
date: 2026-10-28
translationOf: /en/topics/nip-cd.md
translationDate: 2026-10-28
draft: false
categories:
  - Protocol
---

NIP-CD définit des commandes slash. Un service publie une commande, que n'importe qui peut ensuite invoquer sous forme de texte brut dans le contenu de n'importe quel event Nostr. NIP-CD est une spécification optionnelle à l'état de brouillon. Après une proposition antérieure, elle a été fusionnée le 21 octobre 2026 sous le titre Commands, puis renommée Slash Commands lors de la fusion des listes optionnelles de commandes installées, le 27 octobre 2026.

## Fonctionnement

Un event de kind 31992 définit une commande. Des tags obligatoires indiquent le mot déclencheur sans barre oblique, un titre et une description d'utilisation. Des tags `arg` ordonnés déclarent les arguments positionnels, avec des types tels que pubkey, event, relay, number, enum ou text. Quant aux tags `s`, ils limitent les events susceptibles de déclencher la commande, par kind, relay, auteur ou tag. Ces portées fonctionnent comme un filtre : les valeurs d'un même type sont des alternatives, et chaque type présent doit correspondre.

Une invocation est un texte qui commence à l'index 0 du contenu d'un event, par exemple `/ban` suivi d'arguments, et elle ne porte aucun tag. L'ajout d'un qualificatif de la forme `@nostr:npub1...` cible un seul exécuteur. Sans qualificatif, toute commande dont le déclencheur correspond et dont la portée inclut l'event peut agir ; un même message peut donc déclencher plusieurs services.

La prise en charge par les clients est optionnelle. Ceux-ci peuvent proposer l'autocomplétion, des sélecteurs d'arguments et des puces affichées. Ils ne doivent pas exiger leur propre prise en charge avant l'envoi d'une invocation, et un texte qui ne peut pas être analysé doit être envoyé comme contenu ordinaire.

Pour les groupes basés sur un relay, définitions et invocations sont envoyées au relay du groupe. En diffusion, les définitions vont dans les outboxes des exécuteurs et les invocations dans leurs inboxes.

## Listes de commandes installées

Un utilisateur peut tenir une liste optionnelle de kind 10992, conforme à NIP-51, contenant des tags `a` qui pointent vers des définitions de commandes de kind 31992 au moyen de la pubkey de l'exécuteur et de la valeur `d`, avec un indice de relay facultatif. Les clients devraient utiliser cette liste pour l'autocomplétion et les puces affichées. Elle consigne une préférence d'affichage et de découverte propre à l'utilisateur. Aucun exécuteur n'est autorisé par cette liste, et l'invocation en texte brut fonctionne sans elle. Cette partie de la spécification a été fusionnée le 27 octobre 2026 via la PR #2525. La fusion n'indique pas quels clients ont implémenté la liste.

## Sources primaires

- [Spécification NIP-CD](https://github.com/nostr-protocol/nips/blob/master/CD.md)
- [Fusion de NIP-CD du 21 octobre 2026](https://github.com/nostr-protocol/nips/commit/7b5ea85479c0b4efce3c246abefa1dae8f8f91e4)
- [PR #2525 pour les listes de commandes installées, fusionnée le 27 octobre 2026](https://github.com/nostr-protocol/nips/pull/2525)
- [Commit du 26 octobre 2026 issu de la PR #2525, effectué sur sa branche avant la fusion](https://github.com/nostr-protocol/nips/commit/0142de0384210d69074c089448ef5bc303faef37)
- [Fusion des listes de commandes installées dans NIP-CD le 27 octobre 2026](https://github.com/nostr-protocol/nips/commit/400d157c53264b8e58c7b3cdbd21ef546fb7a157)

## Mentionné dans
- [Newsletter #46 : NIP-CD définit des commandes invoquées en texte brut](/fr/newsletters/2026-10-28-newsletter/#nip-cd-defines-commands-invoked-as-plain-text) Newsletters

- [Newsletter #46 : NIP-CD ajoute des listes optionnelles de commandes installées](/fr/newsletters/2026-10-28-newsletter/#nip-cd-adds-optional-installed-command-lists) Newsletters

- [Newsletter #46 (2026-10-28) : octobre 2026, significations de requêtes partagées et services déclenchés par du texte](/fr/newsletters/2026-10-28-newsletter/#october-2026-shared-query-meanings-and-text-triggered-services)

## Voir aussi

- [NIP-01 : protocole de base](/fr/topics/nip-01/)
