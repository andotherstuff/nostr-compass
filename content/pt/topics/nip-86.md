---
title: "NIP-86: API de Gerenciamento de Relay"
date: 2026-04-01
translationOf: /en/topics/nip-86.md
translationDate: 2026-04-01
draft: false
categories:
  - Relays
  - Protocol
---

NIP-86 define uma interface JSON-RPC para gerenciamento de relay, permitindo que clientes autorizados enviem comandos administrativos para relays através de uma API padronizada. Operadores de relay podem banir ou permitir pubkeys, gerenciar listas de acesso e consultar o estado do relay sem ferramentas específicas do relay.

## Como Funciona

A API de gerenciamento usa requisições JSON-RPC via HTTP no mesmo URI que o endpoint websocket do relay. Requisições usam o content type `application/nostr+json+rpc` e autenticam com um evento assinado [NIP-98](/pt/topics/nip-98/) (HTTP Auth) no header `Authorization`. O relay verifica a pubkey solicitante contra sua lista de administradores antes de executar comandos.

Métodos disponíveis incluem banir e permitir pubkeys, listar usuários banidos e consultar configuração do relay. A interface padronizada significa que uma única implementação de cliente pode gerenciar qualquer relay compatível com NIP-86.

## Implementações

- [Amethyst](https://github.com/vitorpamplona/amethyst) - Cliente Android com interface de gerenciamento de relay NIP-86 (v1.07.0+)

---

**Fontes primárias:**
- [Especificação NIP-86](https://github.com/nostr-protocol/nips/blob/master/86.md)
- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - Suporte a NIP-86 do lado do cliente
- [PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039) - Diálogo de busca de usuários para gerenciamento de relay

**Mencionado em:**
- [Newsletter #16: Amethyst lança gerenciamento de relay](/pt/newsletters/2026-04-01-newsletter/#amethyst-lança-notas-fixadas-gerenciamento-de-relay-e-request-to-vanish)

**Veja também:**
- [NIP-11: Relay Information Document](/pt/topics/nip-11/)
- [NIP-98: HTTP Auth](/pt/topics/nip-98/)
- [NIP-42: Authentication of Clients to Relays](/pt/topics/nip-42/)
