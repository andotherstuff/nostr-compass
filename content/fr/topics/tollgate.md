---
title: "TollGate : Internet pay-per-use sur Nostr et Cashu"
date: 2026-04-22
translationOf: /en/topics/tollgate.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocols
---

TollGate est un protocole pour vendre un accès réseau en échange de paiements petits et fréquents sous forme d'actifs au porteur. Un appareil capable de contrôler la connectivité, comme un routeur WiFi, un switch Ethernet ou un partage Bluetooth, agit comme un TollGate qui annonce ses tarifs, accepte des tokens ecash [Cashu](/fr/topics/cashu/) et gère les sessions. Les clients paient exactement les minutes ou les mégaoctets qu'ils consomment. Il n'y a ni comptes, ni abonnements, ni KYC.

## Fonctionnement

TollGate sépare les responsabilités en trois couches. La couche protocole définit les formes d'événements et la sémantique de paiement. La couche interface définit comment le client et le gate échangent ces événements. La couche medium décrit le lien physique qui transporte le trafic payant. Un TollGate fonctionnel combine une spécification de chaque couche, et certaines interfaces passent par des relays Nostr tandis que d'autres passent par HTTP simple.

Au niveau du protocole, [TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md) définit trois événements de base : un kind Advertisement qui liste les prix et les mints acceptés, un kind Session qui suit ce que le client a payé et ce qu'il a consommé, et un kind Notice pour la messagerie hors bande. [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) ajoute les paiements Cashu par-dessus, de sorte qu'un client puisse racheter des tokens ecash provenant de n'importe quel mint annoncé par le TollGate et recevoir en retour du crédit de session.

Au niveau de l'interface, [HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md) à HTTP-03 définissent la surface HTTP pour les appareils sur des systèmes d'exploitation restrictifs qui ne peuvent pas facilement ouvrir des connexions WebSocket vers des relays arbitraires, et [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md) définit le transport par relay Nostr pour les clients qui le peuvent. Au niveau du medium, [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md) décrit comment une configuration WiFi captive portal identifie et route les clients payants.

Parce que l'actif de paiement est un token au porteur plutôt qu'un identifiant, le client n'a pas besoin d'un accès internet préalable pour le produire. Un token Cashu dans un wallet local suffit à lui seul pour acheter la première minute de connectivité, après quoi le client peut recharger avec d'autres tokens si nécessaire. Les TollGates peuvent aussi acheter de l'uplink les uns aux autres, ce qui étend la portée au-delà d'un seul opérateur.

## Pourquoi c'est important

Le WiFi payant conventionnel repose sur des comptes, des captive portals et des cartes de paiement, chacun ajoutant de la friction et une trace de données. Le modèle de TollGate transforme la connectivité en commodité qu'un routeur quelconque peut vendre à n'importe quel client payant sans savoir qui il est. Cette abstraction permet à des opérateurs indépendants de fixer leurs propres prix, d'accepter leurs mints préférés et de concurrencer sur la couverture et la qualité plutôt que sur l'enfermement propriétaire.

La [release v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0) est le premier snapshot tagué de ces spécifications. Elle ne standardise pas chaque détail, mais fixe suffisamment de surface pour que des firmwares de routeur, des wallets clients et des revendeurs multi-hop puissent commencer à construire contre une référence stable.

---

**Sources principales :**
- [Release TollGate v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)
- [TIP-01 : événements de base](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md)
- [TIP-02 : paiements Cashu](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md)
- [HTTP-01 à HTTP-03](https://github.com/OpenTollGate/tollgate/tree/v0.1.0)
- [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md)
- [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md)
- [Dépôt TollGate](https://github.com/OpenTollGate/tollgate)

**Mentionné dans :**
- [Newsletter #19 : TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/)

**Voir aussi :**
- [Cashu](/fr/topics/cashu/)
- [NIP-60 : Wallet Cashu](/fr/topics/nip-60/)
