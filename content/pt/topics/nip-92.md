---
title: "NIP-92: Media Attachments"
date: 2025-12-31
translationOf: /en/topics/nip-92.md
translationDate: 2025-12-31
draft: false
categories:
  - Mídia
  - Protocolo
---

NIP-92 permite que os usuários anexem arquivos de mídia a eventos do Nostr incluindo URLs junto com tags de metadados em linha que descrevem esses recursos.

## Como Funciona

1. O usuário coloca URLs de mídia diretamente no conteúdo do evento (por exemplo, em uma nota de texto kind 1)
2. Uma tag `imeta` (metadados em linha) correspondente fornece detalhes sobre cada URL
3. Os clientes podem substituir URLs imeta por visualizações enriquecidas com base nos metadados
4. Os metadados geralmente são gerados automaticamente quando os arquivos são enviados durante a composição

## A Tag imeta

Cada tag `imeta` deve ter uma `url` e pelo menos outro campo. Os campos suportados incluem:

- `url` - A URL da mídia (obrigatório)
- `m` - Tipo MIME do arquivo
- `dim` - Dimensões da imagem (largura x altura)
- `blurhash` - Blurhash para geração de visualização prévia
- `alt` - Texto alternativo para acessibilidade
- `x` - Hash SHA-256 (de NIP-94)
- `fallback` - URLs alternativas se a principal falhar

## Exemplo

```json
["imeta",
  "url https://example.com/image.jpg",
  "m image/jpeg",
  "dim 1920x1080",
  "blurhash LKO2?U%2Tw=w]~RBVZRi}^Xu%LRj"
]
```

---

**Fontes primárias:**
- [Especificação NIP-92](https://github.com/nostr-protocol/nips/blob/master/92.md)

**Mencionado em:**
- [Boletim #3: Resumo de Dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Veja também:**
- [NIP-94: Metadados de Arquivo](/pt/topics/nip-94/)
