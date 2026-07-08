---
title: "CLINK : Interface Lightning commune pour les clés Nostr"
date: 2026-06-17
draft: false
translationOf: /en/topics/clink.md
translationDate: 2026-07-01
categories:
  - Payments
  - Lightning
---

CLINK (Common Lightning Interface for Nostr Keys) est un format de demande de paiement proposé qui permet à un expéditeur de payer n'importe quelle identité à clé Nostr via une interface noffer unique. Un noffer CLINK encode la clé publique Nostr du destinataire ainsi que suffisamment de métadonnées de routage pour que le portefeuille de l'expéditeur puisse construire un paiement Lightning, un paiement on-chain ou une future primitive de règlement qui aboutit au destinataire. Le destinataire publie un noffer par identité, et les expéditeurs le paient sans savoir si le portefeuille destinataire règle via Lightning, on-chain ou une autre voie.

## Comment ça marche

Un noffer CLINK est une demande de paiement structurée que le portefeuille de l'expéditeur décode en une instruction de paiement concrète. Le noffer transporte :

- La clé publique Nostr du destinataire comme racine d'identité canonique
- Un ou plusieurs points de terminaison de paiement (URI de nœud Lightning, indice de dérivation d'adresse on-chain, futures voies)
- Des métadonnées optionnelles pour le paiement (mémo, montant, expiration)
- Une signature du destinataire liant le noffer à son identité Nostr

Un portefeuille émetteur qui prend en charge CLINK lit le noffer, choisit la voie qu'il peut servir (un portefeuille exclusivement Lightning paie le point de terminaison Lightning, un portefeuille multi-voies choisit le chemin le moins cher), et soumet le paiement. Le portefeuille du destinataire accuse réception en publiant ou en récupérant l'événement d'achèvement correspondant, la clé publique Nostr servant d'identité durable à travers les voies.

## Pourquoi une interface à clé Nostr

LNURL et BOLT-12 existent déjà comme formats de demande de paiement Lightning, et Bitcoin dispose d'un format d'adresse bien connu pour le règlement on-chain. CLINK ne remplace ni l'un ni l'autre. Il ajoute une couche enracinée dans une clé Nostr afin qu'un expéditeur puisse adresser un destinataire par son identité Nostr et laisser le portefeuille déterminer quelle voie sous-jacente utiliser. Un utilisateur qui change de fournisseur Lightning, ouvre une nouvelle mint ou migre son portefeuille on-chain republie son noffer avec la même clé Nostr, et les expéditeurs n'ont pas besoin de mettre à jour leurs carnets d'adresses.

Pour Zeus Pay (qui génère un noffer CLINK pour chaque compte), cela signifie qu'un expéditeur peut payer n'importe quel utilisateur Zeus par sa seule clé Nostr. Pour le pilote de zap on-chain d'Amethyst, la machine à états de vérification CLINK confirme que le noffer signé on-chain correspond au pubkey Nostr revendiqué dans la demande de zap, fermant ainsi une voie de falsification contre les zaps on-chain non signés.

## Implémentations

- [Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) intègre la prise en charge du paiement noffer CLINK, Zeus Pay générant un noffer CLINK pour chaque compte afin qu'un expéditeur puisse payer n'importe quel utilisateur Zeus par sa seule clé Nostr
- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) intègre un pilote CLINK pour la vérification des zaps on-chain avec une machine à états de vérification et un pilote de revérification ([PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039), [PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177), [PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182))

---

**Sources primaires :**
- [Notes de version Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) - Livraison du noffer CLINK
- [Amethyst PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039) - Machine à états de vérification des zaps on-chain NIP-BC et pilote de revérification
- [Amethyst PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177) - Implémente CLINK (Common Lightning Interface for Nostr Keys)
- [Amethyst PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182) - Ajoute le support kotlinx-serialization pour les DTO du protocole CLINK

**Mentionné dans :**
- [Newsletter #27 : Amethyst v1.12.0 intègre les portefeuilles Cashu, les nutzaps, un pilote CLINK et l'auto-réparation Tor](/fr/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Newsletter #27 : Zeus v13.1.0-rc1 livre les noffers CLINK et le NWC sans file d'attente](/fr/newsletters/2026-06-17-newsletter/#zeus-v1310-rc1-ships-clink-noffers-and-queue-less-nwc)

**Voir aussi :**
- [NIP-57 : Zaps](/fr/topics/nip-57/)
- [NIP-47 : Nostr Wallet Connect](/fr/topics/nip-47/)
