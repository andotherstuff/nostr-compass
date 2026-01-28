---
title: "Negentropy: Protocolo de Reconciliação de Conjuntos"
date: 2026-01-28
translationOf: /en/topics/negentropy.md
translationDate: 2026-01-28
draft: false
categories:
  - Protocol
  - Sync
---

Negentropy é um protocolo de reconciliação de conjuntos que permite sincronização eficiente entre clientes Nostr e relays identificando eventos faltantes sem transferir o conjunto de dados completo.

## Como Funciona

Em vez de solicitar todos os eventos que correspondem a um filtro, negentropy permite que clientes comparem seu conjunto local de eventos contra o conjunto de um relay e identifiquem apenas as diferenças. Isso é realizado através de um protocolo de múltiplas rodadas:

1. **Fingerprinting**: Cliente e relay calculam cada um uma impressão digital de seus conjuntos de eventos
2. **Comparação**: Impressões digitais são trocadas e comparadas
3. **Reconciliação**: Apenas IDs de eventos faltantes são identificados e transferidos

## Por Que Importa

Sincronização Nostr tradicional usa filtros `since` baseados em timestamp, que podem perder eventos devido a:
- Desvio de relógio entre cliente e relay
- Múltiplos eventos com timestamps idênticos
- Eventos chegando fora de ordem

Negentropy resolve esses problemas comparando conjuntos reais de eventos em vez de depender de timestamps.

## Casos de Uso

- **Recuperação de DM**: Clientes podem detectar e buscar mensagens diretas faltantes mesmo com timestamps antigos
- **Sincronização de Feed**: Garante sincronização completa de timeline entre relays
- **Sincronização Offline**: Recupera eficientemente após períodos de desconexão

## Implementação

Negentropy requer suporte do relay. Clientes tipicamente o implementam como um mecanismo de recuperação de fallback em vez de substituir assinaturas REQ padrão, degradando graciosamente quando relays não suportam o protocolo.

## Relacionados

- [NIP-01](/pt/topics/nip-01/) - Protocolo Básico
