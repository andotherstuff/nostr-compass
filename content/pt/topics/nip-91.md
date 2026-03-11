---
title: 'NIP-91: Operador AND para Filtros'
date: 2026-03-04
draft: false
categories:
- NIP
- Protocol
translationOf: /en/topics/nip-91.md
translationDate: 2026-03-11
---

NIP-91 adiciona semântica de filtro AND para arrays de tags em assinaturas de relay do Nostr. Ele foi mesclado em 2026-03-03 depois que implementações apareceram em vários relays.

## O problema

O sistema de filtros do Nostr ([NIP-01](/pt/topics/nip-01/)) combina vários valores dentro de um único filtro de tag usando lógica OR. Se um cliente especificar dois valores de tag `p` em um filtro, o relay retornará eventos que correspondam a qualquer uma das duas pubkeys. Não havia como solicitar eventos que fizessem referência às duas pubkeys ao mesmo tempo.

Isso forçou os clientes a buscar eventos em excesso dos relays e filtrar localmente, aumentando o uso da largura de banda e o tempo de processamento.

## Como funciona

NIP-91 introduz semântica AND para arrays de tags. Quando um cliente precisa de eventos que correspondam a todos os valores de tag especificados, ele pode optar por correspondência por interseção em vez do comportamento de união padrão.

Isso é importante para consultas como "eventos que marcam ambos os participantes de uma conversa" ou "eventos que carregam dois rótulos obrigatórios ao mesmo tempo". Antes dessa mudança, os relays só podiam responder com o superconjunto mais amplo e deixar a interseção precisa para o cliente.

## Por que é importante

Os filtros AND tornam os índices do lado do relay mais úteis. Os clientes podem pedir ao relay um conjunto de resultados menor e já relevante, o que reduz a largura de banda e o pós-processamento local. O ganho aparece mais em clientes móveis e em consultas sobre grandes conjuntos de dados ricos em tags.

## Notas de interoperabilidade

No momento do merge, existiam implementações funcionais em nostr-rs-relay, satellite-node, worker-relay e applesauce. A proposta era anteriormente numerada como NIP-119 antes da renumeração.

Os clientes ainda devem esperar suporte misto enquanto a adoção pelos relays avança. Um fallback prático é manter o antigo caminho de interseção no lado do cliente para relays que ainda não implementaram a nova semântica.

---

**Fontes primárias:**
- [Especificação NIP-91](https://github.com/nostr-protocol/nips/blob/master/91.md)
- [PR #1365](https://github.com/nostr-protocol/nips/pull/1365)

**Mencionado em:**
- [Boletim Informativo nº 12: Atualizações do NIP](/pt/newsletters/2026-03-04-newsletter/#atualizacoes-de-nips)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
