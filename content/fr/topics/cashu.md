---
title: "Cashu : Protocole Ecash"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-01-28
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu est un protocole ecash chaumien construit sur Bitcoin et le Lightning Network, permettant des paiements privés, instantanés et à faibles frais grâce à des tokens cryptographiques.

## Fonctionnement

Cashu utilise des signatures aveugles pour créer des tokens ecash intraçables :

1. **Frappe** : Les utilisateurs déposent du Bitcoin/Lightning auprès d'un mint et reçoivent des tokens masqués
2. **Dépense** : Les tokens peuvent être transférés de pair à pair sans l'intervention du mint
3. **Rachat** : Les destinataires échangent les tokens auprès du mint contre du Bitcoin/Lightning

Le mint ne peut pas lier les dépôts aux rachats grâce au processus de masquage, fournissant de fortes garanties de confidentialité.

## Propriétés clés

- **Confidentialité** : Le mint ne peut pas suivre les transferts de tokens entre utilisateurs
- **Instantané** : Les transferts se font hors ligne, aucune confirmation blockchain nécessaire
- **Faibles frais** : Pas de frais on-chain pour les transferts de tokens
- **Custodial** : Les utilisateurs font confiance au mint pour honorer les rachats

## Intégration Nostr

Cashu s'intègre avec Nostr de plusieurs façons :

- **Nutzaps** : Tokens ecash envoyés comme zaps avec une confidentialité renforcée
- **Séquestre** : Séquestre de paiement basé sur HTLC pour des services comme le covoiturage
- **Portefeuilles** : Les portefeuilles natifs Nostr stockent des tokens Cashu chiffrés sur les relais
- **[NIP-87](/fr/topics/nip-87/)** : Découverte et avis de mints via Nostr

## Modèle de confiance

Contrairement au Bitcoin en auto-conservation, Cashu nécessite de faire confiance aux opérateurs de mint. Les utilisateurs devraient :
- Utiliser des mints réputés et bien évalués
- Garder de petits soldes appropriés au niveau de confiance
- Comprendre que les mints peuvent faire un exit-scam ou se déconnecter, emportant les fonds avec eux

## Voir aussi

- [NIP-87](/fr/topics/nip-87/) - Recommandations de mints Cashu
- [NIP-60](/fr/topics/nip-60/) - Portefeuille Nostr
