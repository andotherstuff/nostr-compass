---
title: 'NIP-67: Hint de completude do EOSE'
date: 2026-04-22
draft: false
categories:
  - NIPs
translationOf: /en/topics/nip-67.md
translationDate: 2026-04-22
---

NIP-67 é uma proposta aberta que estende a mensagem `EOSE` existente em [NIP-01](/pt/topics/nip-01/) com um terceiro elemento opcional indicando se o relay entregou todos os eventos armazenados que correspondem ao filtro. A intenção é substituir a heurística pouco confiável que clientes usam hoje para decidir se uma assinatura se esgotou ou foi cortada por um limite do lado do relay.

## O problema

`EOSE` marca a fronteira entre eventos armazenados e eventos em tempo real, mas não carrega nenhuma informação sobre completude. Na prática, relays impõem um limite por assinatura, normalmente entre 300 e 1000 eventos, independente do `limit` pedido pelo cliente. Um cliente que pede as últimas 500 notas a um relay limitado a 300 recebe 300 eventos e um `EOSE`, sem ter como distinguir entre "isso é tudo" e "paramos no meio do caminho". O contorno atual é comparar a contagem de eventos ao `limit` do cliente e paginar defensivamente, o que tanto perde eventos quando o limite do relay é menor que o solicitado quanto desperdiça uma ida e volta quando o limite é múltiplo do número real de correspondências.

Empates na fronteira pioram isso. Paginar com `until = oldest_created_at` arrisca perder ou buscar em duplicidade eventos que compartilham o timestamp mais antigo do lote, dependendo de como o relay compara timestamps.

## A mudança

NIP-67 adiciona um terceiro elemento opcional ao `EOSE`:

```
["EOSE", "<subscription_id>", "finish"]   // todos os eventos armazenados correspondentes foram entregues
["EOSE", "<subscription_id>"]             // nenhuma afirmação de completude, legado
```

Apenas o sinal positivo é especificado. Um relay que anuncia suporte a NIP-67 mas omite o hint está dizendo que há mais. Um relay que não anuncia suporte cai na heurística existente, então a mudança é compatível com versões anteriores para todos os clientes e relays atuais.

Clientes que sabem que seu relay suporta NIP-67 podem parar de paginar assim que virem `"finish"`, evitar a ida e volta extra obrigatória quando o limite coincide exatamente com o conjunto de resultados e mostrar ao usuário uma informação correta de completude.

## Status

A proposta está [aberta como PR #2317](https://github.com/nostr-protocol/nips/pull/2317) no repositório de NIPs.

---

**Fontes primárias:**
- [PR #2317: NIP-67 EOSE Completeness Hint](https://github.com/nostr-protocol/nips/pull/2317)
- [Especificação NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)

**Mencionado em:**
- [Newsletter #19: Atualizações de NIP](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-01: fluxo básico do protocolo](/pt/topics/nip-01/)
- [NIP-11: Relay Information Document](/pt/topics/nip-11/)
