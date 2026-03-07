---
title: 'BUD-10: Esquema URI Blossom'
date: 2025-12-17
draft: false
categories:
- Media
- Protocol
translationOf: /en/topics/bud-10.md
translationDate: '2026-03-07'
---

BUD-10 define o esquema `blossom:` URI, uma referência de blob portátil que pode transportar dicas de servidor, dicas de autor e tamanho esperado junto com o hash do arquivo.

## Formato URI

```
blossom:<sha256>.<ext>?xs=<server>&as=<pubkey>&sz=<bytes>
```

A especificação requer um hash SHA-256 de 64 caracteres minúsculos e uma extensão de arquivo. Se a extensão for desconhecida, os clientes deverão recorrer a `.bin`.

## Como funciona a resolução

Os clientes devem resolver um URI `blossom:` em etapas:

1. Experimente qualquer dica do servidor `xs` na ordem em que aparecem
2. Se o autor `as` pubkeys estiver presente, busque a lista de servidores [BUD-03](/pt/topics/bud-03/) de cada autor e experimente esses servidores
3. Utilize servidores conhecidos ou cache local, se necessário

Essa ordem é útil porque permite que um remetente anexe dicas imediatas para recuperação rápida, ao mesmo tempo que fornece aos destinatários um caminho de recuperação se essas dicas ficarem obsoletas.

## Por que é importante

Os URIs `blossom:` funcionam mais como links magnéticos do que URLs de mídia comuns. Eles descrevem qual blob buscar e incluem pistas sobre onde encontrá-lo, em vez de presumir que um host permanecerá disponível para sempre.

O campo opcional `sz` adiciona uma verificação de integridade concreta além do hash. Os clientes podem verificar o tamanho esperado antes ou depois do download, o que ajuda a detectar transferências incompletas e melhora a experiência do usuário para mídias grandes.

---

**Fontes primárias:**
- [Especificação BUD-10](https://github.com/hzrd149/blossom/blob/master/buds/10.md)
- [Repositório Blossom](https://github.com/hzrd149/blossom)

**Mencionado em:**
- [Boletim informativo nº 1: Notícias](/pt/newsletters/2025-12-17-newsletter/#news)

**Veja também:**
- [Protocolo Blossom](/pt/topics/blossom/)
- [BUD-03: Lista de servidores de usuários](/pt/topics/bud-03/)
