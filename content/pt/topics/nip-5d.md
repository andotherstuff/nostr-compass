---
title: 'NIP-5D: Nostr Web Applets'
date: 2026-04-08
draft: false
categories:
  - Protocol
translationOf: /en/topics/nip-5d.md
translationDate: 2026-04-22
---

NIP-5D define um protocolo `postMessage` para aplicações web sandboxed, chamadas de napplets, executadas em iframes e conectadas a uma aplicação hospedeira, chamada de shell. Ele estende [NIP-5A](/pt/topics/nip-5a/) com uma camada de comunicação em runtime que dá a apps web acesso a funcionalidades Nostr sem expor a chave privada do usuário.

## Como funciona

Uma aplicação shell carrega um napplet em um iframe sandboxed. O napplet se comunica com o shell por meio da API `postMessage` do navegador usando um protocolo estruturado de mensagens. O shell fornece ao napplet assinatura Nostr, acesso a relay e contexto do usuário por esse canal de mensagens. O sandbox do iframe impede que o napplet acesse diretamente a chave privada do usuário, então o shell atua como guardião de todas as operações Nostr.

## Casos de uso

- **Apps Nostr interativos**: criar apps que leem e escrevem eventos Nostr sem exigir que usuários colem seu nsec
- **Marketplace de apps**: distribuir aplicações web interativas por meio de eventos Nostr
- **Extensões sandboxed**: adicionar funcionalidade a clientes Nostr por meio de napplets de terceiros

---

**Fontes primárias:**
- [NIP-5D PR #2303](https://github.com/nostr-protocol/nips/pull/2303) - proposta Nostr Web Applets

**Mencionado em:**
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/)

**Veja também:**
- [NIP-5A: Sites estáticos](/pt/topics/nip-5a/)
- [NIP-5C: Scrolls](/pt/topics/nip-5c/)
