---
title: 'NIP-90: Máquinas de venda automática de dados'
date: 2026-02-25
draft: false
categories:
- NIP
- DVM
translationOf: /en/topics/nip-90.md
translationDate: '2026-03-07'
---

NIP-90 define Data Vending Machines (DVMs), um protocolo para solicitar e entregar trabalho computacional pago através do Nostr.

## Como funciona

Os clientes publicam eventos de solicitação de trabalho no intervalo `5000-5999`. Cada solicitação pode incluir um ou mais `i` tags para entradas, `param` tags para configurações específicas do trabalho, um `output` tag para o formato esperado, um teto `bid` e dicas de relay para onde as respostas devem aparecer. Os prestadores de serviço respondem com um resultado correspondente kind na faixa `6000-6999`, sempre `1000` superior à solicitação kind.

Os resultados incluem a solicitação original, o pubkey do cliente e, opcionalmente, um `amount` tag ou fatura. Os provedores também podem enviar eventos de feedback kind `7000`, como `payment-required`, `processing`, `partial`, `error` ou `success`, o que oferece aos clientes uma maneira de mostrar o progresso antes que o resultado final chegue.

## Pagamento e privacidade

O protocolo deixa intencionalmente a lógica de negócios aberta. Um fornecedor pode solicitar o pagamento antes do início do trabalho, após devolver uma amostra ou após entregar o resultado completo. Essa flexibilidade é importante porque os trabalhos de DVM variam de transformações de texto baratas a trabalhos caros de GPU, e os provedores nem todos assumem o mesmo risco de pagamento.

Se um cliente desejar entradas privadas, a solicitação poderá mover os dados `i` e `param` para `content` criptografado e marcar o evento com um `encrypted` tag mais o `p` tag do provedor. Isso protege as solicitações ou o material de origem dos observadores da relay, mas também significa que o cliente deve visar um fornecedor específico em vez de transmitir uma solicitação de mercado aberto.

## Notas de interoperabilidade

O NIP-90 suporta encadeamento de trabalhos através de `i` tags com tipo de entrada `job`, para que um resultado possa alimentar uma solicitação posterior. Isso torna possíveis fluxos de várias etapas sem inventar uma camada de orquestração separada.

A descoberta do provedor está fora do próprio loop de solicitação/resposta. A especificação aponta para anúncios [NIP-89: Manipuladores de aplicativos recomendados](/pt/topics/nip-89/) para trabalho com suporte de publicidade kinds, que é como os clientes podem descobrir fornecedores antes de publicar uma solicitação.

---

**Fontes primárias:**
- [Especificação NIP-90](https://github.com/nostr-protocol/nips/blob/master/90.md)

**Mencionado em:**
- [Boletim informativo nº 11: Coordenação do agente NIP-AC DVM](/pt/newsletters/2026-02-25-newsletter/#nip-updates)

**Veja também:**
- [NIP-89: Manipuladores de aplicativos recomendados](/pt/topics/nip-89/)
