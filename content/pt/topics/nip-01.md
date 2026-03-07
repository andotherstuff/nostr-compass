---
title: 'NIP-01: Protocolo Básico'
date: 2025-12-17
draft: false
categories:
- Protocol
translationOf: /en/topics/nip-01.md
translationDate: '2026-03-07'
---

NIP-01 define o modelo de evento base e o protocolo relay nos quais o restante do Nostr se baseia. Se um cliente, relay ou biblioteca fala Nostr, começa aqui.

## Como funciona

Eventos são o único tipo de objeto no Nostr. Perfis, notas, reações, listas relay e muitos payloads específicos de aplicativos usam o mesmo envelope de sete campos:

- **id**: hash SHA256 do evento serializado (identificador exclusivo)
- **pubkey**: a chave pública do criador (hexadecimal de 32 bytes, secp256k1)
- **created_at**: carimbo de data/hora Unix
- **kind**: Número inteiro categorizando o tipo de evento
- **tags**: Matriz de matrizes para metadados
- **conteúdo**: O payload (a interpretação depende de kind)
- **sig**: assinatura Schnorr comprovando autenticidade

O evento `id` é o hash SHA256 dos dados do evento serializado, não um identificador arbitrário. Na prática, isso é importante: alterar qualquer campo, incluindo um pedido ou carimbo de data/hora tag, produz um evento diferente e requer uma nova assinatura.

## Tipos

Os tipos determinam como relays armazena e trata eventos:

- **Eventos regulares** (1, 2, 4-44, 1000-9999): Armazenados normalmente, todas as versões mantidas
- **Eventos substituíveis** (0, 3, 10000-19999): apenas o mais recente por pubkey é mantido
- **Eventos efêmeros** (20000-29999): Não armazenados, apenas encaminhados aos assinantes
- **Eventos endereçáveis** (30000-39999): Últimos por combinação pubkey + kind + `d` tag

O núcleo kinds inclui: 0 (metadados do usuário), 1 (nota de texto) e 3 (lista a seguir).

## Comunicação cliente-relay

Os clientes se comunicam com relays por meio de conexões WebSocket usando matrizes JSON:

**Cliente da relay:**
- `["EVENT", <event>]` - Publicar um evento
- `["REQ", <sub-id>, <filter>, ...]` - Inscreva-se em eventos
- `["CLOSE", <sub-id>]` - Encerrar uma assinatura

**Retransmitir para o cliente:**
- `["EVENT", <sub-id>, <event>]` - Entregar evento correspondente
- `["EOSE", <sub-id>]` - Fim dos eventos armazenados (agora transmitido ao vivo)
- `["OK", <event-id>, <true|false>, <message>]` - Aceitar/rejeitar reconhecimento
- `["NOTICE", <message>]` - Mensagem legível por humanos

Na prática, a maioria dos NIPs de nível superior não altera a camada de transporte. Eles definem novos eventos kinds, tags ou regras de interpretação enquanto ainda usam as mesmas mensagens `EVENT`, `REQ` e `CLOSE` do NIP-01.

## Filtros

Os filtros especificam quais eventos recuperar, com campos incluindo `ids`, `authors`, `kinds`, `#e`/`#p`/`#t`, `since`, `until` e `limit`. As condições dentro de um filtro usam a lógica AND. Vários filtros dentro de um `REQ` usam lógica OR.

## Notas de interoperabilidade

Dois detalhes causam muitos bugs de implementação. Primeiro, os clientes devem tratar as respostas relay como eventualmente consistentes, não ordenadas globalmente, porque diferentes relays podem retornar diferentes subconjuntos de histórico. Segundo, eventos substituíveis e endereçáveis ​​significam que "mais recente" faz parte do modelo de protocolo, portanto, os clientes precisam de regras determinísticas para escolher o evento válido mais recente quando vários relays discordam.

---

**Fontes primárias:**
- [Especificação NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Mencionado em:**
- [Boletim informativo nº 1: Aprofundamento do NIP](/pt/newsletters/2025-12-17-newsletter/#nip-deep-dive-nip-01-and-nip-19)

**Veja também:**
- [NIP-19: Entidades codificadas em Bech32](/pt/topics/nip-19/)
- [Registro de tipo](/en/kind-registry/)
