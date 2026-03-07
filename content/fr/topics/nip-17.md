---
title: "NIP-17 : Messages directs privés"
date: 2025-12-17
translationOf: /en/topics/nip-17.md
translationDate: 2026-03-07
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-17 définit les messages directs privés utilisant l'emballage cadeau NIP-59 pour la confidentialité de l'expéditeur. Contrairement aux DMs NIP-04 qui exposent l'expéditeur dans l'événement externe, NIP-17 cache l'expéditeur des relais et des observateurs occasionnels.

## Fonctionnement

Les messages sont enveloppés dans plusieurs couches de chiffrement :
1. Le contenu réel du message se trouve dans un événement rumor de kind 14.
2. Un sceau chiffre ce contenu pour le destinataire.
3. Un emballage cadeau chiffre à nouveau le sceau et le publie depuis une paire de clés jetable.

L'emballage cadeau externe utilise une paire de clés jetable aléatoire pour que les relais et observateurs ne puissent pas déterminer qui a envoyé le message.

## Structure du message

- **Kind 14** - Le contenu réel du DM à l'intérieur des couches d'emballage
- **Kind 1059** - L'événement emballage cadeau externe publié sur les relais
- Utilise le chiffrement NIP-44 pour les charges utiles à l'intérieur du flux d'emballage
- La spécification a été affinée pour mieux supporter les fonctionnalités DM interactives comme les réactions

## Sécurité et modèle de confiance

- Les relais ne peuvent pas voir l'expéditeur (caché par la paire de clés jetable de l'emballage cadeau)
- Le destinataire est visible (dans le tag `p` de l'emballage cadeau)
- Les horodatages des messages sont randomisés dans une fenêtre
- Pas de threading ou de regroupement de conversation visible sur le relais

Le destinataire apprend toujours qui a envoyé le message après l'avoir déballé. NIP-17 cache l'identité de l'expéditeur du réseau, pas de l'autre participant. C'est une distinction importante quand on le décrit comme des "DMs privés".

## Pourquoi c'est important

Les DMs NIP-04 chiffrent le contenu mais laissent les métadonnées visibles :
- La clé publique de l'expéditeur est publique
- La clé publique du destinataire est dans le tag `p`
- Les horodatages sont exacts

NIP-17 cache l'expéditeur au prix d'une implémentation plus complexe.

Cette complexité achète une amélioration réelle de la confidentialité. Un relais peut toujours voir qu'un message emballé est adressé à un destinataire, mais il ne peut pas directement construire un graphe expéditeur-destinataire à partir des métadonnées de l'événement externe comme il le peut avec les messages kind 4.

## Notes d'interopérabilité

NIP-17 définit aussi des listes de relais de boîte de réception pour la messagerie privée. Les clients peuvent publier un événement kind 10050 pour que les expéditeurs sachent quels relais cibler pour la livraison des DMs. Séparer le routage des relais DM du routage de contenu public aide à éviter de publier du trafic privé aux mauvais endroits.

---

**Sources principales :**
- [Spécification NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md)
- [PR #2098](https://github.com/nostr-protocol/nips/pull/2098) - nettoyage de formulation et mise à jour du support des réactions

**Mentionné dans :**
- [Newsletter #1 : NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2 : News](/en/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #3 : December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #3 : Notable Code Changes](/en/newsletters/2025-12-31-newsletter/#shopstr-marketplace)
- [Newsletter #5 : News](/en/newsletters/2026-01-13-newsletter/#news)

**Voir aussi :**
- [NIP-04 : Messages directs chiffrés (obsolète)](/fr/topics/nip-04/)
- [NIP-44 : Encrypted Payloads](/fr/topics/nip-44/)
- [NIP-59 : Gift Wrap](/fr/topics/nip-59/)
