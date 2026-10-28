---
title: "NIP-06: Derivação de chaves a partir de mnemônico"
date: 2026-10-28
translationOf: /en/topics/nip-06.md
translationDate: 2026-10-28
draft: false
categories: ["Identity", "Keys"]
---

A NIP-06 descreve como derivar um par de chaves Nostr a partir de uma frase-semente mnemônica. O [texto oficial atual da NIP-06](https://github.com/nostr-protocol/nips/blob/master/06.md) está marcado como rascunho e opcional e traz este aviso:

> __Aviso__ `unrecommended`: prefira uma única nsec

Esta página aborda a NIP-06 por compatibilidade histórica. Ela não recomenda adotar a derivação por semente.

## Como funciona

De acordo com a [especificação atual](https://github.com/nostr-protocol/nips/blob/master/06.md), o BIP39 é usado para gerar as palavras mnemônicas e derivar delas uma semente binária. Em seguida, o BIP32 deriva as chaves pelo caminho `m/44'/1237'/<account>'/0/0`, em que 1237 é a entrada do Nostr na SLIP44. Um cliente básico pode usar a conta 0. Ao incrementar o valor da conta, obtêm-se outras chaves a partir da mesma semente. Duas implementações só reproduzem a mesma identidade quando concordam nas etapas de derivação e usam as codificações corretas para o resultado.

## Vetores de teste

Um [commit de 12 de outubro de 2023](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b) adicionou dois vetores de teste: um construído a partir de um mnemônico de 12 palavras e outro a partir de um mnemônico de 24 palavras. Cada um lista a chave privada e a chave pública esperadas em hex, junto com as codificações nsec e npub correspondentes. Os desenvolvedores podem usar os vetores para fazer a verificação cruzada de implementações. Os vetores nada dizem sobre a custódia de chaves. Eles também não certificam segurança nem garantem interoperabilidade universal.

## Veja também

- [NIP-01](/pt/topics/nip-01/)

**Fontes primárias:**

- [NIP-06 (atual)](https://github.com/nostr-protocol/nips/blob/master/06.md)
- [Commit que adicionou os vetores de teste da NIP-06 (12 de outubro de 2023)](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b)

**Mencionado em:**

- [Newsletter #46](/pt/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)
