---
title: 'NIP-45: Contagem de eventos'
date: 2026-02-11
draft: false
categories:
  - NIPs
  - Protocol
translationOf: /en/topics/nip-45.md
translationDate: 2026-04-22
---

NIP-45 define como clientes pedem a relays para contar eventos que correspondem a um filtro sem transferir os próprios eventos correspondentes. Ele reutiliza a sintaxe de filtros da NIP-01, então um cliente geralmente pode transformar um `REQ` existente em um request `COUNT` com os mesmos filtros.

## Como funciona

Um cliente envia um request `COUNT` com um subscription ID e um filtro:

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

O relay responde com uma contagem:

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

Isso evita baixar centenas ou milhares de eventos apenas para exibir um número. Se um cliente envia múltiplos filtros em um request `COUNT`, o relay os agrega em um único resultado, assim como múltiplos filtros em `REQ` são combinados com OR.

## Contagem aproximada com HyperLogLog

Desde fevereiro de 2026, a NIP-45 suporta contagem aproximada com HyperLogLog, ou HLL, ([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). Relays podem marcar um resultado como aproximado e, para deduplicação entre relays, retornar 256 registradores HLL junto da contagem:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<512-char hex string>"}]
```

HLL resolve um problema fundamental: contar eventos distintos em múltiplos relays. Se o relay A reporta 50 reações e o relay B reporta 40, o total não é 90 porque muitos eventos existem em ambos os relays. Clientes mesclam valores HLL tomando o valor máximo em cada posição de registrador, o que dá uma estimativa para toda a rede sem baixar os eventos brutos.

A spec fixa a quantidade de registradores em 256 para interoperabilidade. Isso mantém o payload pequeno e torna o cache do lado do relay prático, porque todo relay computa o mesmo layout de registradores para o mesmo filtro elegível.

## Notas de interoperabilidade

HLL só é definido para filtros com um atributo de tag, porque o offset usado para construir os registradores é derivado do primeiro valor tagueado no filtro. A spec também destaca um pequeno conjunto de consultas canônicas, incluindo reações, reposts, quotes, replies, comments e follower counts. Essas são as contagens mais fáceis para relays pré-computarem ou colocarem em cache.

## Por que importa

Follower counts, reaction counts e reply counts são os principais casos de uso. Sem a NIP-45, clientes precisam confiar na visão local de um único relay ou baixar todos os eventos correspondentes e deduplicá-los localmente. NIP-45 mantém a contagem dentro do relay, e HLL torna contagens multi-relay viáveis sem transformar um relay em autoridade.

---

## Implementações

- [nostream](https://github.com/Cameri/nostream) adicionou suporte a `COUNT` no [PR #522](https://github.com/Cameri/nostream/pull/522), permitindo que clientes perguntem quantos eventos correspondem a um filtro sem buscá-los.

---

**Fontes primárias:**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: resposta de relay com HyperLogLog](https://github.com/nostr-protocol/nips/pull/1561)
- [nostream PR #522](https://github.com/Cameri/nostream/pull/522) - suporte a NIP-45 COUNT

**Mencionado em:**
- [Newsletter #9: NIP Deep Dive](/pt/newsletters/2026-02-11-newsletter/)
- [Newsletter #9: Atualizações de NIP](/pt/newsletters/2026-02-11-newsletter/)
- [Newsletter #12: Five Years of Nostr Februaries](/pt/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: suporte a NIP-45 no nostream](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-11: Relay Information Document](/pt/topics/nip-11/)
