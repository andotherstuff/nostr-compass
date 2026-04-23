---
title: 'NIP-57: Zaps'
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
  - Social
translationOf: /en/topics/nip-57.md
translationDate: 2026-04-22
---

NIP-57 define zaps, uma forma de anexar pagamentos Lightning a identidades e conteúdo Nostr. Ela padroniza tanto o request de uma invoice habilitada para zap quanto o evento de recibo que carteiras publicam após o pagamento.

## Como funciona

1. O cliente descobre o endpoint LNURL do destinatário a partir dos metadados do perfil ou de uma tag `zap` no evento alvo.
2. O cliente envia um request de zap kind `9734`, assinado, para o callback LNURL do destinatário, não para relays.
3. O usuário paga a invoice.
4. O servidor de carteira do destinatário publica um recibo de zap kind `9735` nos relays listados no request de zap.
5. Clientes validam e exibem o zap.

## Request de zap, kind 9734

O request de zap é um evento assinado que identifica o pagador e o alvo pretendido. Ele normalmente inclui:

- tag `p` com a pubkey do destinatário
- tag `e` com o evento que está recebendo o zap, opcional
- tag `amount` em millisatoshis
- tag `relays` listando onde publicar o recibo

Conteúdo endereçável pode usar uma tag `a` em vez de, ou junto com, uma tag `e`. A tag opcional `k` registra o kind alvo.

## Recibo de zap, kind 9735

Publicado pelo servidor de carteira do destinatário depois da confirmação do pagamento. Ele contém:

- o request de zap original em uma tag `description`
- tag `bolt11` com a invoice paga
- tag `preimage` provando o pagamento

Clientes devem validar o recibo contra a `nostrPubkey` LNURL do destinatário, o valor da invoice e o request de zap original. Um recibo sem essa validação é apenas uma alegação.

## Confiança e tradeoffs

Zaps são úteis porque tornam pagamentos visíveis dentro do grafo social, mas o recibo ainda é criado pela infraestrutura de carteira do destinatário. A própria spec observa que um recibo de zap não é uma prova universal de pagamento. É melhor entendê-lo como uma declaração assinada pela carteira de que uma invoice vinculada a um request de zap foi paga.

Um cliente que valida corretamente deve checar quatro coisas antes de exibir um recibo como zap: a assinatura do recibo corresponde à `nostrPubkey` anunciada na resposta LNURL do destinatário, o valor da invoice `bolt11` corresponde à tag `amount` dentro do request de zap embutido, o description hash da invoice compromete a string do request de zap e a `preimage` gera o `payment_hash` da invoice. Clientes que renderizam contagens agregadas de zap sem realizar essas checagens são trivialmente falsificáveis por um atacante que publique eventos kind `9735` forjados.

## Zaps privados e anônimos

Zaps privados adicionam uma camada de confidencialidade por cima. O remetente pode criptografar o `content` do request de zap para o destinatário e incluir uma tag `anon` no request externo, para que a rede de relays veja o alvo do pagamento mas não consiga ler a nota anexada. Um zap anônimo vai um passo além: o cliente gera um keypair efêmero novo para o próprio request de zap, então o recibo ainda prova que um pagamento aconteceu, mas o destinatário não consegue ligar o zap à pubkey de longa duração do remetente.

## Metas de zap e splits

NIP-57 sustenta o sistema de metas de zap especificado na [NIP-75](/pt/topics/nip-75/). Uma meta é um evento kind `9041` que declara um valor alvo e um conjunto de relays onde os recibos contam, e clientes contabilizam o progresso da meta somando valores `bolt11` validados de eventos kind `9735` correspondentes.

Zap splits, definidos em um apêndice do NIP, permitem que um destinatário publique um perfil kind `0` com múltiplas tags `zap` ponderadas, para que um único pagamento de zap seja dividido atomicamente entre várias pubkeys. [Amethyst](https://github.com/vitorpamplona/amethyst), [Damus](https://github.com/damus-io/damus) e [noStrudel](https://github.com/hzrd149/nostrudel) implementam split-paying end-to-end.

---

**Fontes primárias:**
- [Especificação NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Mencionado em:**
- [Newsletter #1: Notícias](/pt/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: Notícias](/pt/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: Mudancas notaveis no codigo](/pt/newsletters/2025-12-31-newsletter/)
- [Newsletter #9: Atualizações de NIP](/pt/newsletters/2026-02-11-newsletter/)
- [Newsletter #19: NIP Deep Dive](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-47: Nostr Wallet Connect](/pt/topics/nip-47/)
- [NIP-75: Metas de zap](/pt/topics/nip-75/)
- [NIP-53: Atividades ao vivo](/pt/topics/nip-53/)
