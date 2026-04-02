---
title: "Bitcredit"
date: 2026-03-25
translationOf: /en/topics/bitcredit.md
translationDate: 2026-04-01
draft: false
categories:
  - Finance
  - Commerce
  - Infrastructure
---

Bitcredit é um sistema de trade finance baseado em e-bills para empresas. O site público apresenta o Bitcredit Core como software para emitir, endossar, pagar e gerenciar letras de câmbio eletrônicas, enquanto o repositório open-source implementa uma camada de transporte Nostr junto com a lógica de negócios e crates de persistência.

## Como Funciona

Bitcredit modela crédito comercial como letras de câmbio eletrônicas, ou ebills. Um comprador emite uma ebill com uma data de vencimento futura, o portador pode endossá-la para outra empresa, e o portador final pode solicitar o pagamento no vencimento.

O site do Bitcredit também descreve um caminho de liquidez baseado em mint. Em vez de esperar pelo vencimento, um portador pode solicitar uma oferta de um mint Bitcredit, receber ecash imediatamente e então usar esse ecash para pagar fornecedores ou trabalhadores.

## Notas de Implementação

O repositório `Bitcredit-Core` divide o sistema em múltiplos crates Rust. `bcr-ebill-core` trata do modelo de dados, `bcr-ebill-api` contém a lógica de negócios, `bcr-ebill-persistence` trata do armazenamento, e `bcr-ebill-transport` fornece a API de transporte de rede com uma implementação Nostr.

Essa arquitetura importa porque Bitcredit não é apenas um site ou fluxo de carteira. É um sistema de documentos empresariais com transporte, estado e lógica de liquidação separados em componentes reutilizáveis, incluindo um entrypoint WASM para deployments web.

## Trabalho Recente

O Compass cobriu Bitcredit pela primeira vez em março de 2026 quando a `v0.5.3` adicionou campos de API para ações de pagamento e estado de letras, e corrigiu o tratamento de endereço de assinatura para signatários anônimos. O lançamento seguinte, `v0.5.4`, continuou esse trabalho de API adaptando `BitcreditBillResult`, refinando estado de pagamento e aceitação, e adicionando tratamento mais explícito para campos opcionais.

Essas mudanças são pequenas comparadas com o conceito mais amplo do Bitcredit, mas mostram para onde a implementação está se movendo: melhor ergonomia de frontend, estado de ciclo de vida de letras mais claro, e melhor tratamento para fluxos de assinatura anônimos ou ao portador.

---

**Fontes primárias:**
- [Site do Bitcredit](https://www.bit.cr/)
- [Bitcredit: Como funciona](https://www.bit.cr/how-it-works)
- [Repositório Bitcredit-Core](https://github.com/BitcreditProtocol/Bitcredit-Core)
- [Índice de documentação do Bitcredit-Core](https://github.com/BitcreditProtocol/Bitcredit-Core/blob/master/docs/index.md)
- [Bitcredit v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3)
- [Bitcredit v0.5.4](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.4)
- [PR #846: Improve Status Flags and Add Payment Actions](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846)
- [PR #849: Fix signing address and signatory for anon signers](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849)

**Mencionado em:**
- [Newsletter #13: Bitcredit v0.5.3](/en/newsletters/2026-03-11-newsletter/#bitcredit-v053)
