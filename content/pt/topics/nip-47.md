---
title: 'NIP-47: Nostr Wallet Connect'
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
translationOf: /en/topics/nip-47.md
translationDate: 2026-04-22
---

NIP-47 define Nostr Wallet Connect, um protocolo que permite a um app Nostr conversar com um serviço remoto de carteira Lightning sem expor as credenciais principais da carteira a todo cliente.

## Como funciona

Um serviço de carteira publica um evento replaceable kind `13194` com informações sobre os métodos e modos de criptografia que suporta. Um cliente se conecta usando uma URI `nostr+walletconnect://` que contém a pubkey do serviço de carteira, um ou mais relays e um secret dedicado para aquela conexão. Requests são enviados como eventos kind `23194`, e responses retornam como eventos kind `23195`.

## Comandos e notificações

Métodos comuns incluem `pay_invoice`, `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance` e `get_info`. Serviços de carteira também podem enviar notificações como `payment_received`, `payment_sent` e `hold_invoice_accepted`.

A spec originalmente acumulou vários métodos opcionais ao longo do tempo, mas uma limpeza recente removeu os métodos de pagamento `multi_`. Na prática, a interoperabilidade melhora quando clientes se limitam aos comandos anunciados pelo evento de informações da carteira, em vez de assumir um conjunto amplo de métodos.

## Casos de uso

- **Zapping** - enviar sats para posts, perfis ou criadores de conteúdo
- **Pagamentos** - pagar invoices Lightning a partir de qualquer app Nostr
- **Separação de UX da carteira** - usar um serviço de carteira em muitos clientes Nostr

## Notas de segurança e interoperabilidade

A URI de conexão contém um secret dedicado que o cliente usa para assinatura e criptografia. Isso dá a cada app sua própria identidade de carteira, o que ajuda tanto em revogação quanto em privacidade. Uma carteira pode limitar gastos, desabilitar métodos ou revogar uma conexão sem afetar as demais.

A NIP-44 agora é o modo preferido de criptografia. A spec ainda documenta fallback para NIP-04 em implementações mais antigas, então clientes precisam inspecionar a tag `encryption` anunciada pela carteira, em vez de assumir que toda carteira já migrou.

---

**Fontes primárias:**
- [Especificação NIP-47](https://github.com/nostr-protocol/nips/blob/master/47.md)
- [PR #1913: suporte a hold invoice](https://github.com/nostr-protocol/nips/pull/1913)
- [PR #2210: simplificação](https://github.com/nostr-protocol/nips/pull/2210)

**Mencionado em:**
- [Newsletter #1: Notícias](/pt/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: Lançamentos](/pt/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/)
- [Newsletter #8: NIP Deep Dive](/pt/newsletters/2026-02-04-newsletter/)
- [Newsletter #10: Atualizações de NIP](/pt/newsletters/2026-02-18-newsletter/)
- [Newsletter #13: Shopstr e Milk Market abrem superfícies de comércio MCP](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19: sync de carteira nativa em Nostr no ShockWallet](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-57: Zaps](/pt/topics/nip-57/)
