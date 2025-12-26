---
title: "NIP-11: Informações do Relay"
date: 2025-12-17
draft: false
categories:
  - Relay
  - Protocol
translationOf: /en/topics/nip-11.md
translationDate: 2025-12-26
---

NIP-11 define como os relays expõem metadados sobre si mesmos, incluindo NIPs suportadas, limitações e informações de contato.

## Como Funciona

Os clientes buscam informações do relay fazendo uma requisição HTTP GET para a URL WebSocket do relay com um header `Accept: application/nostr+json`. O relay retorna um documento JSON descrevendo suas capacidades.

## Campos Principais

- **name** - Nome do relay legível por humanos
- **description** - Para que serve o relay
- **supported_nips** - Lista de NIPs implementadas
- **limitation** - Restrições como tamanho máximo de mensagem, autenticação obrigatória, etc.
- **self** - A própria chave pública do relay (novo campo para identidade do relay)

## Casos de Uso

- Clientes podem verificar se um relay suporta recursos necessários antes de conectar
- Serviços de descoberta podem indexar capacidades de relays
- Usuários podem ver políticas do relay antes de publicar

---

**Fontes primárias:**
- [Especificação NIP-11](https://github.com/nostr-protocol/nips/blob/master/11.md)

**Mencionado em:**
- [Newsletter #1: Atualizações de NIP](/pt/newsletters/2025-12-17-newsletter/#nip-updates)
