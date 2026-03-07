---
title: 'NIP-92: Anexos de mídia'
date: 2025-12-31
draft: false
categories:
- Media
- Protocol
translationOf: /en/topics/nip-92.md
translationDate: '2026-03-07'
---

O NIP-92 permite que os usuários anexem arquivos de mídia a eventos Nostr, incluindo URLs junto com metadados embutidos tags que descrevem esses recursos.

## Como funciona

Os usuários colocam URLs de mídia diretamente no conteúdo do evento, por exemplo, em uma nota de texto kind `1`. Um `imeta` tag correspondente adiciona detalhes legíveis por máquina para esse URL exato. Os clientes podem usar os metadados para renderizar visualizações, reservar espaço de layout e evitar adivinhar as propriedades do arquivo depois que a nota já estiver na tela.

Cada `imeta` tag deve corresponder a uma URL no conteúdo do evento. Os clientes podem ignorar tags que não correspondam, o que fornece às implementações uma regra simples para rejeitar metadados obsoletos ou malformados.

## A tag imeta

Cada `imeta` tag deve possuir um `url` e pelo menos um outro campo. Os campos suportados incluem:

- `url` - O URL da mídia (obrigatório)
- `m` - tipo MIME do arquivo
- `dim` - Dimensões da imagem (largura x altura)
- `blurhash` - Blurhash para geração de visualização
- `alt` - Descrição de texto alternativo para acessibilidade
- `x` - hash SHA-256 (de NIP-94)
- `fallback` - URLs alternativos se o primário falhar

Como `imeta` pode transportar campos de [NIP-94: Metadados de arquivo](/pt/topics/nip-94/), os clientes podem reutilizar o mesmo tipo MIME, dimensões, hash e texto de acessibilidade que já entenderiam para eventos de metadados de arquivo independentes.

## Por que é importante

O benefício mais imediato é uma melhor renderização antes do download. Se `dim` estiver presente, os clientes poderão reservar a quantidade certa de espaço para uma imagem ou vídeo em vez de refluir a linha do tempo após o carregamento do arquivo. Se `blurhash` estiver presente, eles poderão mostrar primeiro uma visualização de baixo custo. Se `alt` estiver presente, o anexo permanecerá utilizável para leitores de tela e usuários com baixa visão.

O NIP-92 também permite que os clientes mantenham a própria postagem como fonte da verdade. A URL permanece em `content`, então os clientes mais antigos ainda mostram um link simples, enquanto os clientes mais novos podem atualizar a mesma nota para um cartão de mídia mais rico.

## Notas de interoperabilidade

NIP-92 são metadados embutidos, não um formato de objeto de mídia separado. Se um cliente precisar de um registro de arquivo reutilizável com seu próprio evento, [NIP-94: File Metadata](/pt/topics/nip-94/) é a melhor opção.

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
- [Primal Android PR #718](https://github.com/PrimalHQ/primal-android-app/pull/718) - Uma implementação de cliente concreta para manipulação de dimensões e proporção de aspecto

**Mencionado em:**
- [Boletim informativo nº 3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Boletim informativo nº 6: Notícias](/pt/newsletters/2026-01-21-newsletter/#news)

**Veja também:**
- [NIP-94: Metadados do arquivo](/pt/topics/nip-94/)
