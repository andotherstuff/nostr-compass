---
title: 'Negentropy: Definir protocolo de reconciliação'
date: 2026-01-28
draft: false
categories:
- Protocol
- Sync
translationOf: /en/topics/negentropy.md
translationDate: '2026-03-07'
---

Negentropy é um protocolo de reconciliação de conjunto para descobrir quais eventos um lado possui e o outro não, sem reenviar o conjunto de dados completo.

## Como funciona

Em vez de solicitar cada evento que corresponda a um filtro, a negentropia compara dois conjuntos classificados e restringe apenas os intervalos que diferem. O protocolo troca resumos de intervalos compactos e recorre a listas de ID explícitas apenas quando necessário.

1. **Ordenação**: Ambos os lados classificam os registros por carimbo de data/hora e depois por ID
2. **Comparação de intervalos**: eles trocam impressões digitais por intervalos de registros
3. **Refinamento**: intervalos incompatíveis são divididos até que os IDs ausentes reais sejam limpos

## Por que é importante

A sincronização Nostr tradicional usa filtros `since` baseados em carimbo de data/hora, que podem perder eventos devido a:
- Desvio de clock entre cliente e relay
- Vários eventos com carimbos de data/hora idênticos
- Eventos chegando fora de ordem

Negentropy resolve esses problemas comparando conjuntos de eventos reais em vez de confiar em carimbos de data/hora.

## Uso prático

- **Recuperação de DM**: os clientes podem detectar e buscar mensagens diretas perdidas, mesmo com carimbos de data/hora antigos
- **Feed Sync**: Garante a sincronização completa da linha do tempo em relays
- **Sincronização offline**: recupera com eficiência após períodos de desconexão

O detalhe útil da implementação é que muitos clientes não substituem assinaturas normais pela negentropia. Eles o usam como um caminho de reparo. Damus, por exemplo, manteve o carregamento normal do DM e adicionou negentropia na atualização manual para recuperar mensagens que o fluxo normal perderia.

## Compensações

Negentropy requer suporte de ambos os lados e adiciona complexidade de protocolo além do uso padrão do `REQ`. É mais útil quando a correção é mais importante do que o esforço mínimo de implementação.

Em ambientes mistos, os clientes ainda precisam de um comportamento de fallback elegante porque nem todo relay oferece suporte ao protocolo.

---

**Fontes primárias:**
- [Repositório de protocolo Negentropy](https://github.com/hoytech/negentropy)
- [Damus PR #3536](https://github.com/damus-io/damus/pull/3536)
- [Damus PR #3547](https://github.com/damus-io/damus/pull/3547)

**Mencionado em:**
- [Boletim informativo nº 6: Damus envia negentropia para sincronização confiável de DM](/pt/newsletters/2026-01-28-newsletter/#damus-ships-negentropy-for-reliable-dm-syncing)
- [Boletim informativo nº 12](/pt/newsletters/2026-03-04-newsletter/)

**Veja também:**
- [NIP-01: Fluxo de protocolo básico](/pt/topics/nip-01/)
