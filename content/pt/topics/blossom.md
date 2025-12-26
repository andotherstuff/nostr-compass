---
title: "Protocolo Blossom"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
translationOf: /en/topics/blossom.md
translationDate: 2025-12-26
---

Blossom é um protocolo de hospedagem de mídia para Nostr que fornece armazenamento de arquivos descentralizado com URLs endereçáveis por conteúdo.

## Como Funciona

Arquivos são armazenados em servidores Blossom e endereçados pelo seu hash SHA256. Isso significa:
- O mesmo arquivo sempre tem a mesma URL em todos os servidores
- Arquivos podem ser recuperados de qualquer servidor que os tenha
- Clientes podem verificar integridade do arquivo checando o hash

## Recursos

- Armazenamento endereçável por conteúdo
- Redundância em múltiplos servidores
- Descoberta de autor via BUD-03
- Esquema de URI personalizado via BUD-10
- Paginação baseada em cursor no endpoint `/list`

---

**Fontes primárias:**
- [Repositório Blossom](https://github.com/hzrd149/blossom)

**Mencionado em:**
- [Newsletter #1: Notícias](/pt/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: Mudanças de Código Notáveis](/pt/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)

**Veja também:**
- [BUD-03: Lista de Servidores do Usuário](/pt/topics/bud-03/)
- [BUD-10: Esquema de URI Blossom](/pt/topics/bud-10/)
