---
title: 'NIP-18: republicações'
date: 2025-12-17
draft: false
categories:
- Social
- Protocol
translationOf: /en/topics/nip-18.md
translationDate: '2026-03-07'
---

O NIP-18 define como repassar eventos, semelhante aos retuítes em outras plataformas.

## Como funciona

Uma repostagem é um evento kind 6 (para notas kind 1) ou kind 16 (repostagem genérica) contendo:
- `e` tag referenciando o evento repostado
- `p` tag referenciando o autor original
- Opcionalmente, o evento original completo no campo `content`

O kind 6 é específico para notas de texto. O kind 16 existe para que os clientes possam repassar outros tipos de eventos sem fingir que tudo é uma nota kind 1.

## Notas de interoperabilidade

Suporte aprimorado para repostagem de eventos substituíveis com suporte `a` tag. Isso permite repostagens de eventos endereçáveis ​​(kinds 30000-39999) para referenciá-los por seu endereço, em vez de por um ID de evento específico.

Essa distinção é importante porque os eventos endereçáveis ​​podem ser atualizados ao longo do tempo. A repostagem por coordenada `a` permite que os clientes apontem para a versão atual de um evento endereçável, enquanto a repostagem por ID de evento congela uma instância histórica específica.

## Por que é importante

As republicações são mais do que um botão de compartilhamento da IU. Eles fazem parte de como o conteúdo se move através dos gráficos sociais, como os clientes contam o engajamento e como os dados de dicas do relay se propagam pela rede. Se um cliente manipular incorretamente o repost tags, a reconstrução do thread e a busca de eventos podem falhar de maneiras sutis.

---

**Fontes primárias:**
- [Especificação NIP-18](https://github.com/nostr-protocol/nips/blob/master/18.md)
- [PR #2132](https://github.com/nostr-protocol/nips/pull/2132) - `a` tag suporte para republicações genéricas

**Mencionado em:**
- [Boletim informativo nº 1: atualizações do NIP](/pt/newsletters/2025-12-17-newsletter/#nip-updates)
- [Boletim informativo nº 8: Notícias](/pt/newsletters/2026-02-04-newsletter/#news)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
- [NIP-10: Threading de notas de texto](/pt/topics/nip-10/)
