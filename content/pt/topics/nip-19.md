---
title: 'NIP-19: Entidades codificadas em Bech32'
date: 2025-12-17
draft: false
categories:
- Protocol
- Identity
translationOf: /en/topics/nip-19.md
translationDate: '2026-03-07'
---

O NIP-19 define formatos amigáveis ​​para compartilhar identificadores Nostr. Essas strings codificadas em bech32 são usadas para exibição e compartilhamento, mas nunca são usadas no próprio protocolo (que usa hexadecimal).

## Como funciona

Chaves hexadecimais brutas são propensas a erros de cópia e visualmente indistinguíveis. A codificação Bech32 adiciona um prefixo e uma soma de verificação legíveis por humanos, deixando claro que tipo de dados você está vendo e detectando muitos erros de cópia.

Os formulários básicos codificam um único valor de 32 bytes:

- **npub** - Chave pública (sua identidade, segura para compartilhar)
- **nsec** - Chave privada (manter segredo, usada para assinatura)
- **nota** - ID do evento (refere-se a um evento específico)

Exemplo: O hexadecimal pubkey `3bf0c63f...` torna-se `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

Os formulários estendidos usam codificação TLV para que possam transportar dicas de pesquisa junto com o próprio identificador:

- **nprofile** - Perfil com dicas de relay
- **nevent** - Evento com dicas de relay, autor pubkey e kind
- **naddr** - Referência de evento endereçável com pubkey, kind, `d` tag e dicas de relay

## Por que é importante

As dicas de relay não são autoritativas, mas geralmente decidem se um cliente pode buscar um evento compartilhado na primeira tentativa. É por isso que `nevent`, `nprofile` e `naddr` são geralmente melhores formatos de compartilhamento do que valores simples `note` ou `npub` quando o conteúdo reside fora do conjunto de relays atual do destinatário.

Outra distinção prática é a estabilidade. `note` aponta para um ID de evento imutável, enquanto `naddr` aponta para um evento endereçável que pode ser substituído ao longo do tempo. Para conteúdo longo, calendários ou anúncios de repositório, `naddr` geralmente é o tipo de link correto.

## Notas de implementação

- Use bech32 apenas para interfaces humanas: exibir, copiar/colar, códigos QR, URLs
- Nunca use formatos bech32 em mensagens de protocolo, eventos ou respostas NIP-05
- Toda comunicação de protocolo deve usar codificação hexadecimal
- Ao gerar nevent/nprofile/naddr, inclua dicas de relay para melhor descoberta
- Trate `nsec` como material secreto em todos os lugares. Um cliente nunca deve exibi-lo por padrão, registrá-lo ou incluí-lo nas exportações de suporte

---

**Fontes primárias:**
- [Especificação NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md)

**Mencionado em:**
- [Boletim informativo nº 1: Aprofundamento do NIP](/pt/newsletters/2025-12-17-newsletter/#nip-19-bech32-encoded-identifiers)
- [Boletim informativo nº 3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Boletim informativo nº 3: Mudanças notáveis no código](/pt/newsletters/2025-12-31-newsletter/#damus-ios)
- [Boletim informativo nº 4: Suporte para dicas de relay](/pt/newsletters/2026-01-07-newsletter/)
- [Boletim informativo nº 8: Damus iOS](/pt/newsletters/2026-02-04-newsletter/#damus-ios)
- [Boletim Informativo nº 11: notecrumbs](/pt/newsletters/2026-02-25-newsletter/)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
- [NIP-10: Tópicos de resposta](/pt/topics/nip-10/)
