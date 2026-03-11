---
title: 'NIP-17: Mensagens Diretas Privadas'
date: 2025-12-17
draft: false
categories:
- Privacy
- Messaging
translationOf: /en/topics/nip-17.md
translationDate: 2026-03-11
---

NIP-17 define mensagens diretas privadas usando embalagem de presente NIP-59 para privacidade do remetente. Ao contrário dos DMs NIP-04, que expõem o remetente no evento externo, o NIP-17 esconde o remetente de relays e de observadores casuais.

## Como funciona

As mensagens são agrupadas em várias camadas de criptografia:
1. O conteúdo real da mensagem reside em um evento de boato de kind 14.
2. Um selo criptografa esse conteúdo para o destinatário.
3. Um gift wrap criptografa o selo novamente e o publica a partir de um par de chaves descartável.

O gift wrap externo usa um par de chaves aleatório e descartável para que relays e os observadores não possam determinar quem enviou a mensagem.

## Estrutura da mensagem

- **kind 14** - O conteúdo real do DM dentro das camadas agrupadas
- **Kind 1059** - O evento externo gift wrap publicado nos relays
- Usa criptografia NIP-44 para payloads dentro do fluxo de empacotamento
- A especificação foi refinada para melhor suportar recursos interativos de DM, como reações

## Modelo de segurança e confiança

- Os relays não podem ver o remetente (oculto pelo par de chaves descartável do gift wrap)
- O destinatário está visível (no `p` tag do gift wrap)
- Os carimbos de data e hora das mensagens são aleatórios em uma janela
- Nenhum encadeamento visível ou agrupamento de conversas no relay

O destinatário ainda saberá quem enviou a mensagem depois de desembrulhá-la. O NIP-17 oculta a identidade do remetente da rede, não do outro participante. Essa é uma distinção importante quando as pessoas a descrevem como "DMs privados".

## Por que é importante

Os DMs NIP-04 criptografam o conteúdo, mas deixam os metadados visíveis:
- O remetente pubkey é público
- O destinatário pubkey está no `p` tag
- Os carimbos de data e hora são exatos

O NIP-17 oculta o remetente ao custo de uma implementação mais complexa.

Essa complexidade proporciona uma melhoria real na privacidade. Um relay ainda pode ver que uma mensagem empacotada é endereçada a um destinatário, mas não pode construir diretamente um gráfico remetente-destinatário a partir de metadados de eventos externos como faz com mensagens kind 4.

## Notas de interoperabilidade

O NIP-17 também define listas relay da caixa de entrada para mensagens privadas. Os clientes podem publicar um evento kind 10050 para que os remetentes saibam quais relays direcionar para entrega DM. Manter o roteamento DM relay separado do roteamento de conteúdo público ajuda a evitar a publicação de tráfego privado em lugares errados.

---

**Fontes primárias:**
- [Especificação NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md)
- [PR #2098](https://github.com/nostr-protocol/nips/pull/2098) - limpeza de texto e atualização de suporte de reação

**Mencionado em:**
- [Boletim informativo nº 1: atualizações do NIP](/pt/newsletters/2025-12-17-newsletter/#nip-updates)
- [Boletim informativo nº 2: Notícias](/pt/newsletters/2025-12-24-newsletter/#news)
- [Boletim informativo nº 3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Boletim informativo nº 3: Mudanças notáveis no código](/pt/newsletters/2025-12-31-newsletter/#shopstr-marketplace)
- [Boletim informativo nº 5: Notícias](/pt/newsletters/2026-01-13-newsletter/#news)

**Veja também:**
- [NIP-04: Mensagens diretas criptografadas (obsoletas)](/pt/topics/nip-04/)
- [NIP-44: cargas criptografadas](/pt/topics/nip-44/)
- [NIP-59: Gift Wrap](/pt/topics/nip-59/)
