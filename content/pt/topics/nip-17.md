---
title: "NIP-17: Mensagens Diretas Privadas"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
translationOf: /en/topics/nip-17.md
translationDate: 2025-12-26
---

NIP-17 define mensagens diretas privadas usando gift wrapping da NIP-59 para privacidade do remetente. Diferente das DMs NIP-04 que expõem o remetente, as mensagens NIP-17 escondem quem enviou a mensagem. O destinatário permanece visível no gift wrap externo.

## Como Funciona

As mensagens são envolvidas em múltiplas camadas de criptografia:
1. O conteúdo real da mensagem (kind 14)
2. Um selo que criptografa o conteúdo para o destinatário
3. Um gift wrap que esconde a identidade do remetente

O gift wrap externo usa um par de chaves aleatório e descartável para que relays e observadores não possam determinar quem enviou a mensagem.

## Estrutura da Mensagem

- **Kind 14** - O conteúdo real da DM (dentro do selo)
- Usa criptografia NIP-44 para o conteúdo
- Suporta reações (kind 7) dentro de conversas de DM

## Garantias de Privacidade

- Relays não podem ver o remetente (escondido pelo par de chaves descartável do gift wrap)
- Destinatário é visível (na tag `p` do gift wrap)
- Timestamps das mensagens são randomizados dentro de uma janela
- Sem encadeamento visível ou agrupamento de conversas no relay

## Comparação com NIP-04

DMs NIP-04 criptografam conteúdo mas deixam metadados visíveis:
- Pubkey do remetente é pública
- Pubkey do destinatário está na tag `p`
- Timestamps são exatos

NIP-17 esconde o remetente ao custo de implementação mais complexa.

---

**Fontes primárias:**
- [Especificação NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md)

**Mencionado em:**
- [Newsletter #1: Atualizações de NIP](/pt/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2: Notícias](/pt/newsletters/2025-12-24-newsletter/#news)

**Veja também:**
- [NIP-59: Gift Wrap](/pt/topics/nip-59/)
