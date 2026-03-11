---
title: "NIP-59 : Gift Wrap"
date: 2025-12-17
translationOf: /en/topics/nip-59.md
translationDate: 2026-03-11
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-59 définit le gift wrap, un moyen d'encapsuler un événement afin que les relays et les observateurs extérieurs ne puissent pas identifier le véritable expéditeur à partir de l'événement externe qu'ils reçoivent.

## Structure

Un événement gift-wrapped comporte trois couches :

1. **Rumeur** : l'événement cible sans signature.
2. **Sceau** (kind `13`) : la rumeur chiffrée pour le destinataire et signée par le véritable expéditeur.
3. **Gift Wrap** (kind `1059`) : le sceau chiffré à nouveau et signé par une clé aléatoire à usage unique.

Le sceau doit avoir des tags vides. Le gift wrap externe porte généralement le tag `p` du destinataire pour que les relays puissent l'acheminer.

## Ce qu'il dissimule

Le gift wrap dissimule l'expéditeur aux relays et aux observateurs réseau car l'événement externe est signé par une clé jetable. Le destinataire, cependant, peut toujours déchiffrer le sceau interne et identifier quelle clé permanente l'a signé. Le gain en confidentialité est donc la protection des métadonnées sur la couche de transport, pas l'anonymat vis-à-vis du destinataire.

La spécification recommande aussi de randomiser les horodatages du wrapper et, lorsque c'est possible, d'utiliser des relays qui exigent une authentification et ne servent les événements encapsulés qu'au destinataire prévu. Sans ces comportements de relay, les métadonnées du destinataire peuvent quand même fuiter.

## Notes opérationnelles

Le gift wrap n'est pas un protocole de messagerie en soi. D'autres protocoles, comme les systèmes de messagerie privée, l'utilisent comme brique de base.

Les relays peuvent choisir de ne pas stocker les événements encapsulés longtemps car ils ne sont pas utiles publiquement. La spécification permet aussi la preuve de travail sur le wrapper externe lorsque les implémentations souhaitent une résistance supplémentaire au spam.

## Cas d'utilisation

- Messages directs privés (NIP-17)
- Notes réservées aux amis (proposition NIP-FR)
- Charges utiles de notifications push (proposition NIP-9a)
- Tout scénario nécessitant la confidentialité de l'expéditeur vis-à-vis du réseau

---

**Sources principales :**
- [Spécification NIP-59](https://github.com/nostr-protocol/nips/blob/master/59.md)

**Mentionné dans :**
- [Newsletter #8 : Plongée approfondie NIP](/fr/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-59-gift-wrap)
- [Newsletter #1 : Actualités](/fr/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1 : Mises à jour NIP](/fr/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #3 : Récapitulatif de décembre](/fr/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #15 : PRs ouverts](/fr/newsletters/2026-03-04-newsletter/#open-prs-and-project-updates)

**Voir aussi :**
- [NIP-17 : Messages directs privés](/fr/topics/nip-17/)
