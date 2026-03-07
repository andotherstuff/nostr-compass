---
title: 'NIP-24: Campos Extras de Metadados'
date: 2025-12-17
draft: false
categories:
- Protocol
- Identity
translationOf: /en/topics/nip-24.md
translationDate: '2026-03-07'
---

NIP-24 define campos opcionais adicionais para metadados do usuário kind 0 além do nome básico, sobre e imagem.

## Campos extras de metadados

- **display_name**: um nome alternativo maior e com caracteres mais ricos que `name`
- **website**: um URL da web relacionado ao autor do evento
- **banner**: URL para uma imagem ampla (~1024x768) para exibição opcional em segundo plano
- **bot**: booleano que indica que o conteúdo é total ou parcialmente automatizado
- **aniversário**: Objeto com campos opcionais de ano, mês e dia

A especificação também marca dois campos mais antigos como obsoletos: `displayName` deve se tornar `display_name` e `username` deve se tornar `name`. Os clientes ainda os veem, portanto, um analisador tolerante ajuda na compatibilidade com versões anteriores, mesmo que um escritor não deva emiti-los.

## Tags padrão

O NIP-24 também padroniza tags de uso geral:
- `r`: referência de URL da Web
- `i`: identificador externo
- `title`: Nome para vários tipos de eventos
- `t`: Hashtag (deve ser minúscula)

## Por que é importante

O NIP-24 trata principalmente de convergência. Esses campos e tags já apareciam nos clientes, então a especificação lhes dá nomes e significados consistentes. Isso reduz incompatibilidades pequenas, mas irritantes, como clientes discordando sobre se um banner reside em `banner` ou em alguma chave específica do aplicativo.

Um ponto prático para os implementadores é que kind 0 continua sendo um caminho ativo na maioria dos clientes. Os metadados extras devem permanecer leves. Se um campo precisar de seu próprio padrão de busca ou ciclo de atualização independente, ele provavelmente pertencerá a um evento separado kind, em vez de metadados de perfil inchados.

---

**Fontes primárias:**
- [Especificação NIP-24](https://github.com/nostr-protocol/nips/blob/master/24.md)

**Mencionado em:**
- [Boletim informativo nº 1: atualizações do NIP](/pt/newsletters/2025-12-17-newsletter/#nip-updates)

**Veja também:**
- [NIP-01: Protocolo Básico](/pt/topics/nip-01/)
