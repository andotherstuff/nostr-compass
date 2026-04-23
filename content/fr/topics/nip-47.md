---
title: "NIP-47 : Nostr Wallet Connect"
date: 2025-12-17
translationOf: /en/topics/nip-47.md
translationDate: 2026-04-22
draft: false
categories:
  - Wallet
  - Lightning
---

NIP-47 définit Nostr Wallet Connect, un protocole permettant à une application Nostr de communiquer avec un service de portefeuille Lightning distant sans exposer les identifiants principaux du portefeuille à chaque client.

## Fonctionnement

Un service de portefeuille publie un événement remplaçable de kind `13194` décrivant les méthodes et modes de chiffrement qu'il supporte. Un client se connecte en utilisant un URI `nostr+walletconnect://` contenant la clé publique du service de portefeuille, un ou plusieurs relais, et un secret dédié à cette connexion. Les requêtes sont envoyées comme événements de kind `23194` et les réponses reviennent comme événements de kind `23195`.

## Commandes et notifications

Les méthodes courantes incluent `pay_invoice`, `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance` et `get_info`. Les services de portefeuille peuvent aussi envoyer des notifications comme `payment_received`, `payment_sent` et `hold_invoice_accepted`.

La spécification a accumulé plusieurs méthodes optionnelles au fil du temps, mais un nettoyage récent a supprimé les méthodes de paiement `multi_`. En pratique, l'interopérabilité est meilleure lorsque les clients s'en tiennent aux commandes annoncées par l'événement info du portefeuille au lieu de supposer un large ensemble de méthodes.

## Cas d'utilisation

- **Zapping** - Envoyer des sats aux publications, profils ou créateurs de contenu
- **Paiements** - Payer des factures Lightning depuis n'importe quelle application Nostr
- **Séparation de l'UX portefeuille** - Utiliser un seul service de portefeuille à travers plusieurs clients Nostr

## Notes de sécurité et d'interopérabilité

L'URI de connexion contient un secret dédié que le client utilise pour la signature et le chiffrement. Cela donne à chaque application sa propre identité de portefeuille, ce qui facilite la révocation et la confidentialité. Un portefeuille peut plafonner les dépenses, désactiver des méthodes ou révoquer une connexion sans affecter les autres.

NIP-44 est désormais le mode de chiffrement préféré. La spécification documente encore le repli NIP-04 pour les anciennes implémentations, les clients doivent donc inspecter le tag `encryption` annoncé par le portefeuille au lieu de supposer que chaque portefeuille a migré.

---

**Sources principales :**
- [NIP-47 Specification](https://github.com/nostr-protocol/nips/blob/master/47.md)
- [PR #1913: Hold Invoice Support](https://github.com/nostr-protocol/nips/pull/1913)
- [PR #2210: Simplification](https://github.com/nostr-protocol/nips/pull/2210)

**Mentionné dans :**
- [Newsletter #1 : News](/fr/newsletters/2025-12-17-newsletter/)
- [Newsletter #2 : Releases](/fr/newsletters/2025-12-24-newsletter/)
- [Newsletter #3 : December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #8 : NIP Deep Dive](/fr/newsletters/2026-02-04-newsletter/)
- [Newsletter #10 : NIP Updates](/fr/newsletters/2026-02-18-newsletter/)
- [Newsletter #19 : synchronisation wallet native de ShockWallet](/en/newsletters/2026-04-22-newsletter/)

**Voir aussi :**
- [NIP-57 : Zaps](/fr/topics/nip-57/)
