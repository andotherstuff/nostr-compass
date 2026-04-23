---
title: "Cashu : protocole ecash"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-04-22
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu est un protocole ecash chaumien construit sur Bitcoin et Lightning. Les utilisateurs détiennent des tokens au porteur émis par un mint, puis transfèrent ces tokens sans exposer l'intégralité du graphe de paiement au mint.

## Fonctionnement

Cashu utilise des signatures aveugles pour émettre des tokens ecash :

1. **Frappe** : les utilisateurs déposent du Bitcoin/Lightning auprès d'un mint et reçoivent des tokens masqués
2. **Dépense** : les tokens peuvent être transférés de pair à pair sans l'intervention du mint
3. **Rachat** : les destinataires échangent les tokens auprès du mint contre du Bitcoin/Lightning

Le mint signe des secrets masqués, de sorte qu'il peut vérifier les tokens ultérieurement sans avoir vu les secrets originaux au moment de l'émission. Cela rompt le lien direct entre dépôt et rachat au sein du mint.

## Sécurité et modèle de confiance

Cashu améliore la confidentialité des paiements, mais le système reste custodial. Un mint peut refuser les rachats, se déconnecter ou perdre les fonds de garantie.

Les preuves Cashu sont des instruments au porteur. Quiconque contrôle la preuve peut la dépenser. La gestion des preuves s'apparente donc davantage à de l'argent liquide qu'à un solde de compte : la sauvegarde, la compromission de l'appareil ou la fuite de tokens en clair ont des conséquences immédiates.

## Intégration Nostr

Cashu s'intègre à Nostr de plusieurs façons :

- **Nutzaps** : tokens ecash envoyés comme zaps avec une confidentialité renforcée
- **Séquestre** : séquestre de paiement basé sur HTLC pour des services comme le covoiturage
- **Portefeuilles** : les portefeuilles natifs Nostr stockent des tokens Cashu chiffrés sur les relais
- **[NIP-87](/fr/topics/nip-87/)** : découverte et avis de mints via Nostr
- **[TollGate](/fr/topics/tollgate/)** : protocole d'accès réseau pay-per-use qui accepte des tokens ecash Cashu pour la connectivité, défini dans [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) à partir de la [release v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)

## Compromis

Cashu est rapide parce que les transferts se font hors chaîne et souvent hors mint jusqu'au rachat. Le compromis porte sur l'interopérabilité et la confiance.

En pratique, les utilisateurs ont souvent besoin du même mint, ou d'un échange ou pont entre mints. C'est pourquoi les applications Nostr combinent fréquemment Cashu avec la découverte de mints, la synchronisation de portefeuilles et les systèmes d'avis.

---

**Sources principales :**
- [Dépôt NUTs Cashu](https://github.com/cashubtc/nuts)
- [NUT-00 : Cryptographie et modèles](https://github.com/cashubtc/nuts/blob/main/00.md)
- [Spécification NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md)
- [Spécification NIP-87](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Mentionné dans :**
- [Newsletter #7](/fr/newsletters/2026-01-28-newsletter/)
- [Newsletter #11](/fr/newsletters/2026-02-25-newsletter/)
- [Newsletter #19 : TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/)

**Voir aussi :**
- [NIP-60 : Portefeuille Cashu](/fr/topics/nip-60/)
- [NIP-87 : Recommandations de mints Cashu](/fr/topics/nip-87/)
- [TollGate](/fr/topics/tollgate/)
