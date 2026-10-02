---
title: "NIP-FI do Buzz: Asserções de identidade federada"
date: 2026-09-30
translationOf: /en/topics/nip-fi.md
translationDate: 2026-10-02
draft: false
categories:
  - Project Proposals
  - Identity
  - Relays
---

O NIP-FI é a especificação de asserções de identidade federada **específica do projeto** Buzz. O nome não implica adoção pelo repositório `nostr-protocol/nips` nem interoperabilidade com relays fora do Buzz.

## Entrada HTTP

Para solicitações HTTP protegidas no modo de aplicação, o Buzz combina uma asserção de identidade federada com um event de autorização assinado do NIP-98. A chave pública Nostr comprovada pela assinatura HTTP precisa corresponder à chave nomeada na asserção. Evidências ausentes, divergentes ou não verificáveis são rejeitadas. O Buzz usa essa combinação para ligar a decisão de autorização de um emissor de identidade externo à chave Nostr que faz a solicitação.

A [revisão da especificação do projeto](https://github.com/block/buzz/pull/7254) define o modelo de aplicação. A [implementação incorporada de entrada HTTP](https://github.com/block/buzz/pull/7264) cobre as superfícies HTTP protegidas do Buzz, incluindo os caminhos de ponte de relay, mídia, workflow e Git. O merge relata testes no código-fonte; ele não significa que outro relay Nostr implemente a mesma política.

---

**Fontes primárias:**
- [Revisão da especificação NIP-FI do Buzz](https://github.com/block/buzz/pull/7254)
- [Implementação de entrada HTTP do Buzz](https://github.com/block/buzz/pull/7264)

**Mencionado em:**
- [Newsletter #42: controles de identidade do Buzz](/pt/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
