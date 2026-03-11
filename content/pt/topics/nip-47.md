---
title: 'NIP-47: Nostr Wallet Connect'
date: 2025-12-17
draft: false
categories:
- Wallet
- Lightning
translationOf: /en/topics/nip-47.md
translationDate: 2026-03-11
---

O NIP-47 define o Nostr Wallet Connect, um protocolo para permitir que um aplicativo Nostr se comunique com um serviço remoto de carteira Lightning sem expor as credenciais principais da carteira a todos os clientes.

## Como funciona

Um serviço de carteira publica um evento informativo kind `13194` substituível descrevendo os métodos e modos de criptografia que ele suporta. Um cliente se conecta usando um URI `nostr+walletconnect://` que contém o serviço de carteira pubkey, um ou mais relays e um segredo dedicado para essa conexão. As solicitações são enviadas como eventos kind `23194` e as respostas retornam como eventos kind `23195`.

## Comandos e notificações

Os métodos comuns incluem `pay_invoice`, `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance` e `get_info`. Os serviços de carteira também podem enviar notificações push, como `payment_received`, `payment_sent` e `hold_invoice_accepted`.

A especificação originalmente desenvolveu vários métodos opcionais ao longo do tempo, mas a limpeza recente removeu os métodos de pagamento `multi_`. Na prática, a interoperabilidade é melhor quando os clientes seguem os comandos anunciados pelo evento info da carteira, em vez de assumir um amplo conjunto de métodos.

## Casos de uso

- **Zapping** - Envie sats para postagens, perfis ou criadores de conteúdo
- **Pagamentos** - Pague faturas Lightning de qualquer aplicativo Nostr
- **Separação UX da carteira** - Use um serviço de carteira para vários clientes Nostr

## Notas de segurança e interoperabilidade

O URI de conexão contém um segredo dedicado que o cliente usa para assinatura e criptografia. Isso dá a cada aplicativo sua própria identidade de carteira, o que ajuda tanto na revogação quanto na privacidade. Uma carteira pode limitar gastos, desabilitar métodos ou revogar uma conexão sem afetar outra.

NIP-44 é agora o modo de criptografia preferido. A especificação ainda documenta o substituto do NIP-04 para implementações mais antigas, então os clientes precisam inspecionar o `encryption` tag anunciado da carteira em vez de presumir que todas as carteiras foram migradas.

---

**Fontes primárias:**
- [Especificação NIP-47](https://github.com/nostr-protocol/nips/blob/master/47.md)
- [PR #1913: Suporte para retenção de fatura](https://github.com/nostr-protocol/nips/pull/1913)
- [PR #2210: Simplificação](https://github.com/nostr-protocol/nips/pull/2210)

**Mencionado em:**
- [Boletim informativo nº 1: Notícias](/pt/newsletters/2025-12-17-newsletter/#news)
- [Boletim Informativo nº 2: Lançamentos](/pt/newsletters/2025-12-24-newsletter/#releases)
- [Boletim informativo nº 3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Boletim informativo nº 8: Aprofundamento do NIP](/pt/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-47-nostr-wallet-connect)
- [Boletim Informativo nº 10: Atualizações do NIP](/pt/newsletters/2026-02-18-newsletter/#nip-updates)

**Veja também:**
- [NIP-57: Zaps](/pt/topics/nip-57/)
