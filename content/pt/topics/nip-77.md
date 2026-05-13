---
title: "NIP-77: Reconciliação Negentropy"
date: 2026-05-14
draft: false
translationOf: /en/topics/nip-77.md
translationDate: 2026-05-13
categories:
  - NIPs
  - Sync
---

NIP-77 define como os relays e clientes Nostr utilizam o protocolo de reconciliação de conjuntos [Negentropy](/pt/topics/negentropy/) para sincronizar eficientemente conjuntos de eventos, encontrando quais eventos estão faltando em cada lado sem reenviar o conjunto de dados completo.

## Como funciona

A reconciliação Negentropy é executada sobre uma conexão WebSocket usando um tipo de mensagem dedicado. O cliente e o relay trocam impressões digitais de intervalo compactas sobre seus conjuntos de eventos ordenados, convergindo apenas nos intervalos que diferem. Uma vez identificadas as diferenças, apenas os IDs de eventos ausentes (e então os eventos ausentes em si) são transferidos.

NIP-77 padroniza o enquadramento de mensagens para que qualquer cliente e relay que implemente a especificação possa negociar uma sessão de sincronização eficiente. O protocolo usa os tipos de mensagem `NEG-OPEN`, `NEG-MSG` e `NEG-CLOSE` sobre a conexão WebSocket Nostr existente.

## Por que é importante

A sincronização Nostr tradicional usa filtros `since` baseados em timestamps, que podem perder eventos devido à deriva do relógio, eventos com timestamps idênticos ou eventos chegando fora de ordem. Negentropy compara conjuntos de eventos reais em vez de depender de timestamps, fornecendo uma sincronização completa e comprovável em significativamente menos viagens de ida e volta do que o polling ingênuo.

Isso é especialmente útil para:
- Clientes móveis se atualizando após ficarem offline
- Replicação de relay para relay
- Sincronização de relay local (como no agregador de relay do Citrine)

## Implementações

- [Citrine](https://github.com/greenart7c3/Citrine) — [PR #139](https://github.com/greenart7c3/Citrine/pull/139) adicionou suporte NIP-77 para sincronização eficiente por reconciliação de conjuntos no nó relay Android
- [strfry](https://github.com/hoytech/strfry) — suporte Negentropy do lado do relay
- [nostr-tools](https://github.com/nbd-wtf/nostr-tools) — implementação Negentropy do lado do cliente

---

**Fontes primárias:**
- [Especificação NIP-77](https://github.com/nostr-protocol/nips/blob/master/77.md)
- [Protocolo Negentropy](https://github.com/hoytech/negentropy)

**Mencionado em:**
- [Newsletter #22: Citrine v3.0.0-pre1](/pt/newsletters/2026-05-14-newsletter/#citrine-v300-pre1-lands-built-in-tor-and-relay-aggregation)

**Veja também:**
- [Negentropy](/pt/topics/negentropy/)
