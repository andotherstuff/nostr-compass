---
title: 'NIP-45: Contagem de Eventos'
date: 2026-02-11
draft: false
categories:
- NIPs
- Protocol
translationOf: /en/topics/nip-45.md
translationDate: '2026-03-07'
---

O NIP-45 define como os clientes pedem ao relays para contar os eventos que correspondem a um filtro sem transferir eles próprios os eventos correspondentes. Ele reutiliza a sintaxe do filtro NIP-01, para que um cliente muitas vezes possa transformar uma solicitação `REQ` existente em uma solicitação `COUNT` com os mesmos filtros.

## Como funciona

Um cliente envia uma solicitação `COUNT` com um ID de assinatura e filtro:

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

O relay responde com uma contagem:

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

Isso evita o download de centenas ou milhares de eventos apenas para exibir um número. Se um cliente enviar vários filtros em uma solicitação `COUNT`, o relay os agregará em um único resultado, assim como vários filtros `REQ` são submetidos a operação OR juntos.

## Contagem aproximada do HyperLogLog

A partir de fevereiro de 2026, o NIP-45 oferece suporte à contagem aproximada do HyperLogLog (HLL) ([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). Os relays podem marcar um resultado como aproximado e, para desduplicação cruzada relay, eles podem retornar 256 registros HLL junto com a contagem:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<512-char hex string>"}]
```

A HLL resolve um problema fundamental: contar eventos distintos em vários relays. Se relay A relatar 50 reações e relay B relatar 40, o total não será 90 porque existem muitos eventos em ambos relays. Os clientes mesclam os valores HLL obtendo o valor máximo em cada posição de registro, o que fornece uma estimativa para toda a rede sem baixar os eventos brutos.

A especificação fixa a contagem de registros em 256 para interoperabilidade. Isso mantém o payload pequeno e torna o cache do lado relay prático porque cada relay calcula o mesmo layout de registro para o mesmo filtro elegível.

## Notas de interoperabilidade

HLL é definido apenas para filtros com atributo tag, pois o deslocamento usado para construir os registros é derivado do primeiro valor marcado no filtro. A especificação também apresenta um pequeno conjunto de consultas canônicas, incluindo reações, republicações, citações, respostas, comentários e contagens de seguidores. Essas são as contagens mais fáceis para relays pré-calcular ou armazenar em cache.

## Por que é importante

Contagens de seguidores, contagens de reações e contagens de respostas são os principais casos de uso. Sem o NIP-45, os clientes devem confiar na visualização local de uma única relay ou baixar todos os eventos correspondentes e desduplicá-los localmente. O NIP-45 continua contando dentro do relay, e a HLL torna práticas as contagens multi-relay sem transformar um relay na autoridade.

---

**Fontes primárias:**
- [NIP-45: Contagem de Eventos](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: Resposta de relay do HyperLogLog](https://github.com/nostr-protocol/nips/pull/1561)

**Mencionado em:**
- [Boletim informativo nº 9: Aprofundamento do NIP](/pt/newsletters/2026-02-11-newsletter/#nip-deep-dive-nip-45-event-counting-and-hyperloglog)
- [Boletim informativo nº 9: Atualizações do NIP](/pt/newsletters/2026-02-11-newsletter/#nip-updates)
- [Boletim informativo nº 12: Cinco anos de fevereiro de Nostr](/pt/newsletters/2026-03-04-newsletter/)

**Veja também:**
- [NIP-11: Documento de Informações do Relay](/pt/topics/nip-11/)
