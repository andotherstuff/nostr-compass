---
title: 'NIP-17: Mensagens Diretas Privadas'
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
translationOf: /en/topics/nip-17.md
translationDate: 2026-04-22
---

NIP-17 define mensagens diretas privadas usando gift wrapping da NIP-59 para privacidade do remetente. Diferente das DMs da NIP-04, que expõem o remetente no evento externo, a NIP-17 esconde o remetente de relays e observadores casuais.

## Como funciona

Mensagens são encapsuladas em múltiplas camadas de criptografia:
1. O conteúdo real da mensagem vive em um rumor event kind 14.
2. Um seal criptografa esse conteúdo para o destinatário.
3. Um gift wrap criptografa o seal novamente e o publica a partir de um keypair descartável.

A camada externa de gift wrap usa um keypair aleatório e descartável para que relays e observadores não consigam determinar quem enviou a mensagem.

## Estrutura da mensagem

- **Kind 14** - o conteúdo real da DM dentro das camadas encapsuladas
- **Kind 1059** - o evento externo de gift wrap publicado nos relays
- Usa criptografia da NIP-44 para os payloads dentro do fluxo de encapsulamento
- A spec foi refinada para suportar melhor recursos interativos de DM, como reações

## Modelo de segurança e confiança

- Relays não conseguem ver o remetente, escondido pelo keypair descartável do gift wrap
- O destinatário fica visível, na tag `p` do gift wrap
- Timestamps das mensagens são randomizados dentro de uma janela
- Não há threading visível nem agrupamento de conversas no relay

O destinatário ainda aprende quem enviou a mensagem depois de desembrulhá-la. NIP-17 esconde a identidade do remetente da rede, não do outro participante. Essa é uma distinção importante quando pessoas a descrevem como DMs privadas.

## Por que importa

DMs da NIP-04 criptografam o conteúdo, mas deixam metadados visíveis:
- a pubkey do remetente é pública
- a pubkey do destinatário aparece na tag `p`
- timestamps são exatos

A NIP-17 esconde o remetente ao custo de uma implementação mais complexa.

Essa complexidade compra uma melhora real de privacidade. Um relay ainda consegue ver que uma mensagem encapsulada é endereçada a um destinatário, mas não consegue construir diretamente um grafo remetente-destinatário a partir dos metadados externos do evento, como acontece com mensagens kind 4.

## Notas de interoperabilidade

A NIP-17 também define listas de inbox relays para mensagens privadas. Clientes podem publicar um evento kind 10050 para que remetentes saibam quais relays mirar para entrega de DMs. Manter o roteamento de DMs separado do roteamento de conteúdo público ajuda a evitar que tráfego privado seja publicado nos lugares errados.

---

**Fontes primárias:**
- [Especificação NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md)
- [PR #2098](https://github.com/nostr-protocol/nips/pull/2098) - limpeza de texto e atualização de suporte a reações

**Mencionado em:**
- [Newsletter #1: Atualizações de NIP](/pt/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: Notícias](/pt/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/)
- [Newsletter #3: Mudancas notaveis no codigo](/pt/newsletters/2025-12-31-newsletter/)
- [Newsletter #5: Notícias](/pt/newsletters/2026-01-13-newsletter/)
- [Newsletter #13: Vector](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19: gerenciador de senhas NipLock](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-04: Mensagens diretas criptografadas (obsoleta)](/pt/topics/nip-04/)
- [NIP-44: cargas criptografadas](/pt/topics/nip-44/)
- [NIP-59: Gift Wrap](/pt/topics/nip-59/)
