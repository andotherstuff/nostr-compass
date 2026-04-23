---
title: 'NIP-90: Data Vending Machines'
date: 2026-02-25
draft: false
categories:
  - NIP
  - DVM
translationOf: /en/topics/nip-90.md
translationDate: 2026-04-22
---

NIP-90 define Data Vending Machines, ou DVMs, um protocolo para solicitar e entregar trabalho computacional pago sobre Nostr.

## Como funciona

Clientes publicam requests de jobs na faixa `5000-5999`. Cada request pode incluir uma ou mais tags `i` para inputs, tags `param` para settings específicos do job, uma tag `output` para o formato esperado, um teto de `bid` e relay hints indicando onde replies devem aparecer. Provedores de serviço respondem com um kind de resultado correspondente na faixa `6000-6999`, sempre `1000` acima do kind do request.

Resultados incluem o request original, a pubkey do cliente e, opcionalmente, uma tag `amount` ou uma invoice. Provedores também podem enviar eventos de feedback kind `7000`, como `payment-required`, `processing`, `partial`, `error` ou `success`, o que dá a clientes uma forma de mostrar progresso antes de o resultado final chegar.

## Pagamento e privacidade

O protocolo intencionalmente deixa a lógica de negócio em aberto. Um provedor pode pedir pagamento antes de começar o trabalho, depois de devolver uma amostra ou apenas após entregar o resultado completo. Essa flexibilidade importa porque jobs de DVM vão de transformações baratas de texto a trabalho caro em GPU, e provedores não assumem o mesmo risco de pagamento.

Se um cliente quiser inputs privados, o request pode mover dados `i` e `param` para um `content` criptografado e marcar o evento com uma tag `encrypted` mais a tag `p` do provedor. Isso protege prompts ou material-fonte contra observadores em relays, mas também significa que o cliente precisa mirar um provedor específico em vez de fazer um request aberto ao mercado.

## Notas de interoperabilidade

A NIP-90 suporta encadeamento de jobs por meio de tags `i` com input type `job`, então um resultado pode alimentar um request posterior. Isso torna possíveis fluxos em múltiplas etapas sem inventar uma camada separada de orquestração.

A descoberta de provedores fica fora do loop de request e response em si. A spec aponta para anúncios da [NIP-89: Recommended Application Handlers](/pt/topics/nip-89/) para divulgar kinds de job suportados, e é assim que clientes podem descobrir vendors antes de publicar um request.

---

**Fontes primárias:**
- [Especificação NIP-90](https://github.com/nostr-protocol/nips/blob/master/90.md)

**Mencionado em:**
- [Newsletter #11: coordenação de agentes DVM com NIP-AC](/pt/newsletters/2026-02-25-newsletter/)
- [Newsletter #19: toll-booth-dvm da Forgesworn](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: proposta Agent Reputation Attestations](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-89: Recommended Application Handlers](/pt/topics/nip-89/)
