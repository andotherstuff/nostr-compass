---
title: "NIP-A3: Alvos de Pagamento"
date: 2026-09-09
translationOf: /en/topics/nip-a3.md
translationDate: 2026-09-11
draft: false
categories:
  - Protocol
  - Payments
---

O NIP-A3 define uma forma portátil de uma conta Nostr publicar endereços de pagamento para múltiplas redes e serviços. Um evento substituível de kind `10133` carrega uma ou mais tags `payto`.

## Como Funciona

Cada tag tem a forma `["payto", "<tipo>", "<endereço>"]`. O tipo é em letras minúsculas, como `bitcoin`, `lightning` ou `monero`. Os clientes podem validar formatos conhecidos e renderizar uma URI de pagamento nativa quando existir uma; tipos desconhecidos recorrem ao esquema de URI `payto:` da RFC 8905.

O evento declara destinos, não um pagamento concluído nem um zap Nostr. Os clientes ainda decidem quais tipos de pagamento suportam, como validar um endereço e com que clareza exibir o destino antes de entregá-lo a uma carteira.

## Implementações

- O [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041) oferece uma entrega de pagamento opcional (opt-in) quando reconhece um alvo compatível.
- O [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851) mapeia tipos de alvo permitidos para URIs de pagamento.
- O [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98) valida alvos Monero e consulta os relays do autor.

---

**Fontes primárias:**
- [Especificação do NIP-A3](https://github.com/nostr-protocol/nips/blob/master/A3.md)
- [RFC 8905: The payto URI Scheme](https://www.rfc-editor.org/rfc/rfc8905.html)

**Mencionado em:**
- [Newsletter #39: Alvos de pagamento do NIP-A3 chegam a três clientes](/pt/newsletters/2026-09-09-newsletter/#nip-a3-payment-targets-reach-three-clients)

**Veja também:**
- [NIP-47: Nostr Wallet Connect](/pt/topics/nip-47/)
