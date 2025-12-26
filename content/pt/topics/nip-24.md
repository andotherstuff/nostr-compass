---
title: "NIP-24: Campos de Metadados Extras"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Identity
translationOf: /en/topics/nip-24.md
translationDate: 2025-12-26
---

NIP-24 define campos opcionais adicionais para metadados de usuário kind 0 além do básico name, about e picture.

## Campos de Metadados Extras

- **display_name**: Um nome alternativo, maior, com caracteres mais ricos que `name`
- **website**: Uma URL web relacionada ao autor do evento
- **banner**: URL para uma imagem larga (~1024x768) para exibição opcional de fundo
- **bot**: Booleano indicando que o conteúdo é total ou parcialmente automatizado
- **birthday**: Objeto com campos opcionais de ano, mês e dia

## Tags Padrão

NIP-24 também padroniza tags de propósito geral:
- `r`: Referência de URL web
- `i`: Identificador externo
- `title`: Nome para vários tipos de eventos
- `t`: Hashtag (deve ser minúscula)

---

**Fontes primárias:**
- [Especificação NIP-24](https://github.com/nostr-protocol/nips/blob/master/24.md)

**Mencionado em:**
- [Newsletter #1: Atualizações de NIP](/pt/newsletters/2025-12-17-newsletter/#nip-updates)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
