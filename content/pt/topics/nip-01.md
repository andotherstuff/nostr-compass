---
title: "NIP-01: Protocolo Básico"
date: 2025-12-17
draft: false
categories:
  - Protocol
translationOf: /en/topics/nip-01.md
translationDate: 2025-12-26
---

NIP-01 define o protocolo fundamental para o Nostr, estabelecendo as estruturas de dados e padrões de comunicação sobre os quais todas as outras NIPs são construídas.

## Eventos

Eventos são o único tipo de objeto no Nostr. Cada pedaço de dado, desde uma atualização de perfil até uma postagem de texto ou uma reação, é representado como um evento com esta estrutura:

- **id**: Hash SHA256 do evento serializado (identificador único)
- **pubkey**: Chave pública do criador (hex de 32 bytes, secp256k1)
- **created_at**: Timestamp Unix
- **kind**: Inteiro categorizando o tipo de evento
- **tags**: Array de arrays para metadados
- **content**: O conteúdo (interpretação depende do kind)
- **sig**: Assinatura Schnorr provando autenticidade

## Kinds

Os kinds determinam como os relays armazenam e manipulam eventos:

- **Eventos regulares** (1, 2, 4-44, 1000-9999): Armazenados normalmente, todas as versões são mantidas
- **Eventos substituíveis** (0, 3, 10000-19999): Apenas o mais recente por pubkey é mantido
- **Eventos efêmeros** (20000-29999): Não armazenados, apenas encaminhados para assinantes
- **Eventos endereçáveis** (30000-39999): Mais recente por combinação de pubkey + kind + tag `d`

Os kinds principais incluem: 0 (metadados do usuário), 1 (nota de texto), 3 (lista de seguidos).

## Comunicação Cliente-Relay

Os clientes se comunicam com relays através de conexões WebSocket usando arrays JSON:

**Cliente para relay:**
- `["EVENT", <event>]` - Publicar um evento
- `["REQ", <sub-id>, <filter>, ...]` - Assinar eventos
- `["CLOSE", <sub-id>]` - Encerrar uma assinatura

**Relay para cliente:**
- `["EVENT", <sub-id>, <event>]` - Entregar evento correspondente
- `["EOSE", <sub-id>]` - Fim dos eventos armazenados (agora transmitindo ao vivo)
- `["OK", <event-id>, <true|false>, <message>]` - Confirmação de aceite/rejeição
- `["NOTICE", <message>]` - Mensagem legível por humanos

## Filtros

Filtros especificam quais eventos recuperar, com campos incluindo: `ids`, `authors`, `kinds`, `#e`/`#p`/`#t` (valores de tags), `since`/`until` e `limit`. Condições dentro de um filtro usam lógica AND; múltiplos filtros em um `REQ` combinam com lógica OR.

---

**Fontes primárias:**
- [Especificação NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Mencionado em:**
- [Newsletter #1: Análise Profunda de NIP](/pt/newsletters/2025-12-17-newsletter/#nip-deep-dive-nip-01-and-nip-19)

**Veja também:**
- [NIP-19: Entidades Codificadas em Bech32](/pt/topics/nip-19/)
- [Registro de Kinds](/pt/kind-registry/)
