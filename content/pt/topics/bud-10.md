---
title: "BUD-10: Esquema de URI Blossom"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
translationOf: /en/topics/bud-10.md
translationDate: 2025-12-26
---

BUD-10 define um esquema de URI personalizado para Blossom que incorpora todas as informações necessárias para recuperar um arquivo de qualquer servidor disponível.

## Formato da URI

```
blossom:<sha256>.<ext>?size=<bytes>&server=<url>&server=<url>&pubkey=<hex>
```

Componentes:
- **sha256**: Hash do arquivo (obrigatório)
- **ext**: Extensão do arquivo
- **size**: Tamanho do arquivo em bytes
- **server**: Uma ou mais dicas de servidor
- **pubkey**: Pubkeys de autor para descoberta de servidor BUD-03

## Benefícios

- Mais resiliente que URLs HTTP estáticas
- Fallback automático através de múltiplos servidores
- Descoberta baseada em autor via dicas de pubkey
- Auto-verificável (hash garante integridade)

---

**Fontes primárias:**
- [PR BUD-10](https://github.com/hzrd149/blossom/pull/84)

**Mencionado em:**
- [Newsletter #1: Notícias](/pt/newsletters/2025-12-17-newsletter/#news)

**Veja também:**
- [Protocolo Blossom](/pt/topics/blossom/)
- [BUD-03: Lista de Servidores do Usuário](/pt/topics/bud-03/)
