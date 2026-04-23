---
title: 'NIP-5C: Scrolls (programas WASM)'
date: 2026-04-08
draft: false
categories:
  - Protocol
translationOf: /en/topics/nip-5c.md
translationDate: 2026-04-22
---

NIP-5C, antes NIP-A5, define convenções para publicar, descobrir e executar programas WebAssembly, chamados de scrolls, no Nostr. Binários WASM são armazenados como eventos Nostr, permitindo que qualquer cliente os busque e execute em um runtime sandboxed.

## Como funciona

Desenvolvedores publicam programas WASM como eventos Nostr contendo o binário compilado. Clientes descobrem esses programas por meio de consultas Nostr padrão, baixam o binário WASM do evento e o executam em um runtime WebAssembly sandboxed. O sandbox impede que scrolls acessem diretamente o sistema hospedeiro, limitando-os às capacidades que o runtime fornece explicitamente.

## Casos de uso

- **Compute portátil**: executar programas em qualquer cliente que suporte execução WASM
- **Distribuição descentralizada de apps**: publicar e descobrir aplicações sem app stores
- **Ferramentas componíveis**: encadear scrolls para fluxos de trabalho complexos

## Demo

Um [demo app](https://nprogram.netlify.app/) mostra scrolls rodando no navegador, com programas de exemplo publicados como eventos Nostr.

---

**Fontes primárias:**
- [NIP-5C PR #2281](https://github.com/nostr-protocol/nips/pull/2281) - proposta Scrolls (programas WASM)

**Mencionado em:**
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/)
- [Newsletter #19: proposta NIP-5D de applets](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-5D: Web Applets](/pt/topics/nip-5d/)
- [NIP-5A: Sites estáticos](/pt/topics/nip-5a/)
