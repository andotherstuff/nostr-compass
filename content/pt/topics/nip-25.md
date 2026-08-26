---
title: "NIP-25: Reações"
date: 2026-07-29
translationOf: /en/topics/nip-25.md
translationDate: 2026-08-26
draft: false
categories:
  - Protocol
  - Social
---

O NIP-25 define reações como eventos kind `7`. Ele dá aos clientes uma forma de evento compartilhada para anexar um emoji ou outra reação breve a uma nota, um artigo, um anúncio classificado ou outro evento referenciado.

## Como funciona

Um evento de reação carrega seu texto de reação em `content` e referencia o alvo pela tag `e` do evento alvo. Quando o alvo é endereçável, a reação inclui também sua tag `a`. Ela inclui ainda tags `p` para o autor do evento referenciado, o que permite a relays e clientes rotear notificações sem inferir os destinatários a partir do conteúdo do evento.

A reação padrão é `+`, então clientes podem tratar um conteúdo de reação vazio como resposta positiva. Outros emoji são valores de reação válidos. A especificação também permite `-` para uma reação negativa, que o acréscimo de julho de 2022 adicionou após a introdução original.

Clientes devem preservar a referência ao alvo e as tags de autor ao criar uma reação. Uma reação é um evento assinado comum, então pode viajar por assinaturas normais de relay e ser renderizada por qualquer cliente que reconheça o kind `7`.

## Implementações

O NIP-25 é amplamente implementado por clientes e bibliotecas Nostr como parte da interação comum com notas. Seu modelo simples de kind e tags permite aos clientes exibir contagens, reações individuais e notificações sem um protocolo de transporte separado.

---

**Fontes primárias:**
- [NIP-25 Specification](https://github.com/nostr-protocol/nips/blob/master/25.md)
- [Commit de introdução](https://github.com/nostr-protocol/nips/commit/dcbd504639d20d1b0ae6bb837609710645781b88)
- [Acréscimo de voto negativo](https://github.com/nostr-protocol/nips/commit/89bb08ba8683)

**Mencionado em:**
- [Newsletter #33: Seis anos de julhos do Nostr](/pt/newsletters/2026-07-29-newsletter/#seis-anos-de-julhos-do-nostr)
- [Newsletter #37: Marmot](/pt/newsletters/2026-08-26-newsletter/#marmot)

**Veja também:**
- [NIP-01: Basic Protocol](/pt/topics/nip-01/)
- [NIP-10: Text Note Threading](/pt/topics/nip-10/)
