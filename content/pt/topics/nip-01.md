---
title: 'NIP-01: Protocolo Básico'
date: 2025-12-17
draft: false
categories:
  - Protocol
translationOf: /en/topics/nip-01.md
translationDate: 2026-04-22
---

NIP-01 define o modelo base de eventos e o protocolo de relay sobre os quais o restante do Nostr se apoia. Se um cliente, relay ou biblioteca fala Nostr, tudo começa aqui.

## Como funciona

Eventos são o único tipo de objeto no Nostr. Perfis, notas, reações, listas de relay e muitos payloads específicos de aplicações usam o mesmo envelope de sete campos:

- **id**: hash SHA256 do evento serializado, identificador único
- **pubkey**: chave pública do criador, 32 bytes em hex, secp256k1
- **created_at**: timestamp Unix
- **kind**: inteiro que categoriza o tipo de evento
- **tags**: array de arrays para metadados
- **content**: o payload, cuja interpretação depende do kind
- **sig**: assinatura Schnorr que prova autenticidade

O `id` do evento é o hash SHA256 dos dados serializados do evento, não um identificador arbitrário. Isso importa na prática: mudar qualquer campo, inclusive ordem de tags ou timestamp, produz um evento diferente e exige uma nova assinatura.

## Kinds

Kinds determinam como relays armazenam e tratam eventos:

- **Eventos regulares** (1, 2, 4-44, 1000-9999): armazenados normalmente, todas as versões são mantidas
- **Eventos replaceable** (0, 3, 10000-19999): apenas o mais recente por pubkey é mantido
- **Eventos efêmeros** (20000-29999): não são armazenados, apenas encaminhados a assinantes
- **Eventos endereçáveis** (30000-39999): o mais recente por combinação de pubkey, kind e tag `d`

Kinds centrais incluem 0, metadados do usuário, 1, nota de texto, e 3, lista de follows.

## Comunicação cliente-relay

Clientes se comunicam com relays por conexões WebSocket usando arrays JSON:

**Cliente para relay:**
- `["EVENT", <event>]` - publica um evento
- `["REQ", <sub-id>, <filter>, ...]` - assina eventos
- `["CLOSE", <sub-id>]` - encerra uma assinatura

**Relay para cliente:**
- `["EVENT", <sub-id>, <event>]` - entrega evento correspondente
- `["EOSE", <sub-id>]` - fim dos eventos armazenados, a partir daí o fluxo segue ao vivo
- `["OK", <event-id>, <true|false>, <message>]` - confirmação de aceitação ou rejeição
- `["NOTICE", <message>]` - mensagem legível por humanos

Na prática, a maior parte dos NIPs de nível mais alto não altera a camada de transporte. Eles definem novos kinds, tags ou regras de interpretação, mas continuam usando as mesmas mensagens `EVENT`, `REQ` e `CLOSE` da NIP-01.

## Filtros

Filtros especificam quais eventos recuperar, com campos como `ids`, `authors`, `kinds`, `#e`, `#p`, `#t`, `since`, `until` e `limit`. Condições dentro de um único filtro usam lógica AND. Múltiplos filtros dentro de um `REQ` usam lógica OR.

## Notas de interoperabilidade

Dois detalhes causam muitos bugs de implementação. Primeiro, clientes devem tratar responses de relay como eventualmente consistentes, não globalmente ordenadas, porque diferentes relays podem devolver diferentes subconjuntos do histórico. Segundo, eventos replaceable e endereçáveis significam que o conceito de mais recente faz parte do modelo do protocolo, então clientes precisam de regras determinísticas para escolher o evento válido mais novo quando vários relays discordam.

---

**Fontes primárias:**
- [Especificação NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Mencionado em:**
- [Newsletter #1: NIP Deep Dive](/pt/newsletters/2025-12-17-newsletter/)
- [Newsletter #19: proposta de hint de completude EOSE da NIP-67](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-19: Entidades codificadas em Bech32](/pt/topics/nip-19/)
- [Kind Registry](/en/kind-registry/)
