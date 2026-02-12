---
title: "NIP-45: Contagem de Eventos"
date: 2026-02-11
translationOf: /en/topics/nip-45.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-45 define como aplicações pedem a relays a contagem de eventos que correspondem a um filtro sem transferir os eventos em si. A aplicação envia mensagem COUNT com a mesma sintaxe de filtro que REQ, e o relay responde com a contagem.

## Como Funciona

A aplicação envia requisição COUNT com ID de subscrição e filtro:

```json
["COUNT", "<subscription_id>", {"kinds": [7], "#e": ["<event_id>"]}]
```

O relay responde com a contagem:

```json
["COUNT", "<subscription_id>", {"count": 238}]
```

Isso evita baixar centenas ou milhares de eventos apenas para exibir um número.

## Contagem Aproximada HyperLogLog

Em fevereiro de 2026, NIP-45 passou a suportar contagem aproximada HyperLogLog (HLL) ([PR #1561](https://github.com/nostr-protocol/nips/pull/1561)). Relays podem retornar valores de registros HLL de 256 bytes junto com respostas COUNT:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

HLL resolve problema fundamental: contar eventos distintos em múltiplos relays. Se o relay A reporta 50 reações e o relay B reporta 40, o total não é 90 porque muitos eventos existem em ambos os relays. Registros HLL de múltiplos relays podem ser mergeados tomando o valor máximo em cada posição de registro, deduplicando automaticamente pela rede.

Com 256 registros, o erro padrão é aproximadamente 5,2%. Correções HyperLogLog++ melhoram a precisão em cardinalidades pequenas abaixo de ~200 eventos. Até dois eventos de reação consomem mais largura de banda que o payload HLL de 256 bytes, tornando isso eficiente em qualquer contagem acima de números triviais.

A spec fixa a quantidade de registros em 256 por interoperabilidade entre todas as implementações de relay.

## Casos de Uso

Métricas sociais (contagens de seguidores, reações, reposts) são a aplicação principal. Sem HLL, a opção é consultar relay único "confiável" (centralizando os dados) ou baixar todos os eventos de todos os relays e deduplicar localmente (desperdiçando largura de banda). HLL fornece contagens cross-relay aproximadas com 256 bytes de overhead por relay.

---

**Fontes primárias:**
- [NIP-45: Event Counting](https://github.com/nostr-protocol/nips/blob/master/45.md)
- [PR #1561: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)

**Mencionado em:**
- [Newsletter #9: Deep Dive de NIP](/pt/newsletters/2026-02-11-newsletter/#deep-dive-de-nip-nip-45-contagem-de-eventos-e-hyperloglog)
- [Newsletter #9: Atualizações de NIPs](/pt/newsletters/2026-02-11-newsletter/#atualizações-de-nips)

**Veja também:**
- [NIP-11: Documento de Informação de Relay](/pt/topics/nip-11/)
