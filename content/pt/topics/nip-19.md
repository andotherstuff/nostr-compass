---
title: "NIP-19: Entidades Codificadas em Bech32"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identity
translationOf: /en/topics/nip-19.md
translationDate: 2025-12-26
---

NIP-19 define formatos amigáveis para humanos para compartilhar identificadores Nostr. Essas strings codificadas em bech32 são usadas para exibição e compartilhamento, mas nunca são usadas no próprio protocolo (que usa hex).

## Por que Bech32?

Chaves hex brutas são propensas a erros ao copiar e visualmente indistinguíveis. A codificação bech32 adiciona um prefixo legível por humanos e checksum, tornando imediatamente claro que tipo de dado você está olhando.

## Formatos Básicos

Estes codificam valores brutos de 32 bytes:

- **npub** - Chave pública (sua identidade, seguro compartilhar)
- **nsec** - Chave privada (mantenha em segredo, usada para assinar)
- **note** - ID de evento (referencia um evento específico)

Exemplo: A pubkey hex `3bf0c63f...` se torna `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

## Identificadores Compartilháveis

Estes usam codificação TLV (Type-Length-Value) para incluir metadados:

- **nprofile** - Perfil com dicas de relay (ajuda clientes a encontrar o usuário)
- **nevent** - Evento com dicas de relay, pubkey do autor e kind
- **naddr** - Referência de evento endereçável (pubkey + kind + tag d + relays)

Estes resolvem o problema de descoberta: quando alguém compartilha um ID de nota, como os clientes sabem qual relay o tem? Ao incluir dicas de relay no identificador, links compartilhados se tornam mais confiáveis.

## Notas de Implementação

- Use bech32 apenas para interfaces humanas: exibição, copiar/colar, QR codes, URLs
- Nunca use formatos bech32 em mensagens de protocolo, eventos ou respostas NIP-05
- Toda comunicação de protocolo deve usar codificação hex
- Ao gerar nevent/nprofile/naddr, inclua dicas de relay para melhor descoberta

---

**Fontes primárias:**
- [Especificação NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md)

**Mencionado em:**
- [Newsletter #1: Análise Profunda de NIP](/pt/newsletters/2025-12-17-newsletter/#nip-19-bech32-encoded-identifiers)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
- [NIP-21: Esquema de URI nostr:](https://github.com/nostr-protocol/nips/blob/master/21.md)
