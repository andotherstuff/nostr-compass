---
title: "ContextVM"
date: 2026-02-25
translationOf: /en/topics/contextvm.md
translationDate: 2026-03-07
draft: false
categories:
  - Infrastructure
  - AI
  - Protocol
---

ContextVM est un protocole et un ensemble d'outils pour transporter le trafic MCP (Model Context Protocol) sur Nostr. Il permet aux clients et serveurs MCP de se trouver mutuellement et d'échanger des messages signés sans dépendre d'un registre central, de noms de domaine ou d'OAuth.

## Fonctionnement

Le SDK ContextVM fournit des transports client et serveur en TypeScript pour MCP sur Nostr. Les serveurs MCP existants peuvent conserver leurs transports habituels tandis qu'une passerelle les expose à Nostr, et les clients sans support natif de Nostr peuvent se connecter via une couche proxy.

Les relais servent de bus de messages. Ils routent les événements, tandis que la signature et le chiffrement assurent l'authentification des points d'accès et la confidentialité du transport.

## Composants

**SDK** : bibliothèque TypeScript avec transports client/serveur, support proxy et fonctionnalité passerelle pour relier les serveurs MCP locaux à Nostr.

**CVMI** : interface en ligne de commande pour la découverte de serveurs et l'invocation de méthodes.

**Relatr** : service de notation de confiance calculant des scores personnalisés à partir de la distance dans le graphe social et de la validation des profils.

## Pourquoi c'est important

ContextVM est un pont de transport, pas un remplacement de MCP lui-même. C'est important car cela réduit le coût d'adoption : un serveur MCP existant peut devenir accessible via Nostr sans réécrire son schéma d'outils ou sa logique métier.

Les travaux récents sur ContextVM ont aussi introduit la livraison éphémère pour le trafic gift-wrapped. C'est utile pour les appels d'outils et les réponses intermédiaires où le stockage durable sur les relais est inutile et peut créer une exposition supplémentaire à la vie privée.

## Notes d'interopérabilité

En février et mars 2026, le projet est passé de l'implémentation vers la standardisation. L'équipe a ouvert des propositions NIP pour MCP JSON-RPC sur Nostr et pour une variante éphémère de gift wrap. Même si ces propositions évoluent, elles clarifient la frontière du protocole : MCP reste la couche applicative, Nostr gère la découverte et le transport.

---

**Sources principales :**
- [Site web ContextVM](https://contextvm.org)
- [ContextVM SDK](https://github.com/ContextVM/sdk)
- [CVMI CLI](https://github.com/ContextVM/cvmi)
- [Relatr](https://github.com/ContextVM/relatr)
- [NIP PR #2245: Ephemeral Gift Wrap](https://github.com/nostr-protocol/nips/pull/2245)
- [NIP PR #2246: MCP JSON-RPC over Nostr](https://github.com/nostr-protocol/nips/pull/2246)

**Mentionné dans :**
- [Newsletter #11 : ContextVM News](/fr/newsletters/2026-02-25-newsletter/#contextvm-mcp-over-nostr)
- [Newsletter #12](/fr/newsletters/2026-03-04-newsletter/)

**Voir aussi :**
- [NIP-90 : Data Vending Machines](/fr/topics/nip-90/)
