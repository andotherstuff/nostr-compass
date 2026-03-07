---
title: Protocolo Blossom
date: 2025-12-17
draft: false
categories:
- Media
- Protocol
translationOf: /en/topics/blossom.md
translationDate: '2026-03-07'
---

Blossom é um protocolo de hospedagem de mídia para Nostr que armazena blobs em servidores HTTP comuns e os endereça por hash SHA-256 em vez de IDs atribuídos ao servidor.

## Como funciona

Os servidores Blossom expõem uma pequena interface HTTP para recuperação, upload e gerenciamento de blob. O identificador canônico é o hash do arquivo, portanto, o mesmo blob mantém o mesmo endereço em todos os servidores compatíveis.

- `GET /<sha256>` recupera um blob por hash
- `PUT /upload` carrega um blob
- Eventos kind `24242` Nostr autorizam uploads e ações de gerenciamento
- Os eventos kind `10063`, definidos em [BUD-03](/pt/topics/bud-03/), permitem que os usuários publiquem seus servidores preferidos

Como o hash é o identificador, os clientes podem verificar a integridade localmente após o download e podem tentar outro servidor sem alterar a referência subjacente.

## Por que é importante

Blossom separa o armazenamento de blobs de eventos sociais. Uma nota ou perfil pode apontar para uma mídia sem vinculá-la ao design de URL de um host.

Isso também altera o tratamento de falhas. Se um servidor desaparecer, os clientes podem buscar o mesmo hash de um espelho, cache ou servidor descoberto através da lista do autor [BUD-03](/pt/topics/bud-03/). Essa é uma melhoria prática em relação aos sistemas de mídia onde a URL original do host é o único localizador.

## Notas de interoperabilidade

Blossom é modular. O comportamento principal de recuperação e upload reside no BUD-01 e BUD-02, enquanto o espelhamento, a otimização de mídia, a autorização e o compartilhamento de URI são divididos em BUDs separados.

Essa divisão permite que os clientes implementem o mínimo necessário para a interoperabilidade básica e, em seguida, adicionem peças opcionais, como dicas de URI [BUD-10](/pt/topics/bud-10/) ou cache local à medida que o suporte amadurece.

---

**Fontes primárias:**
- [Repositório Blossom](https://github.com/hzrd149/blossom)
- [BUD-01: Requisitos do servidor e recuperação de blob](https://github.com/hzrd149/blossom/blob/master/buds/01.md)
- [BUD-02: upload e gerenciamento de blobs](https://github.com/hzrd149/blossom/blob/master/buds/02.md)
- [Guia de cache local Blossom](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md)

**Mencionado em:**
- [Boletim informativo nº 1: Notícias](/pt/newsletters/2025-12-17-newsletter/#news)
- [Boletim informativo nº 2: Mudanças notáveis no código](/pt/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)
- [Boletim informativo nº 10: Surge a camada de cache local Blossom](/pt/newsletters/2026-02-18-newsletter/#blossom-local-cache-layer-emerges)

**Veja também:**
- [BUD-03: Lista de servidores de usuários](/pt/topics/bud-03/)
- [BUD-10: Esquema URI Blossom](/pt/topics/bud-10/)
