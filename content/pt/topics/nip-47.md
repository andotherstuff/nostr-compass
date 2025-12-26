---
title: "NIP-47: Nostr Wallet Connect"
date: 2025-12-17
draft: false
categories:
  - Wallet
  - Lightning
translationOf: /en/topics/nip-47.md
translationDate: 2025-12-26
---

NIP-47 define um protocolo para conectar aplicações Nostr a carteiras Lightning, permitindo pagamentos sem expor credenciais da carteira para cada aplicativo.

## Como Funciona

Uma carteira (como Zeus) executa um serviço NWC que escuta solicitações de pagamento em relays Nostr específicos. Apps se conectam usando uma string de conexão que inclui a pubkey da carteira e informações do relay. Solicitações de pagamento e respostas são criptografadas entre o app e a carteira.

## Casos de Uso

- **Zapping** - Enviar sats para posts, perfis ou criadores de conteúdo
- **Pagamentos** - Pagar invoices Lightning de qualquer app Nostr
- **Assinaturas** - Pagamentos recorrentes para conteúdo premium

## Recursos Principais

- **Controles de orçamento** - Definir limites de gastos por conexão
- **Relays personalizados** - Usar seu próprio relay para comunicação da carteira
- **Pagamentos paralelos** - Processar múltiplos zaps simultaneamente para operações em lote

---

**Fontes primárias:**
- [Especificação NIP-47](https://github.com/nostr-protocol/nips/blob/master/47.md)

**Mencionado em:**
- [Newsletter #1: Notícias](/pt/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: Lançamentos](/pt/newsletters/2025-12-24-newsletter/#releases)

**Veja também:**
- [NIP-57: Zaps](/pt/topics/nip-57/)
