---
title: "NIP-50: Search"
date: 2025-12-31
translationOf: /en/topics/nip-50.md
translationDate: 2025-12-31
draft: false
categories:
  - Protocolo
  - Relay
---

NIP-50 define uma capacidade de busca generalizada para relays do Nostr, permitindo que clientes realizem buscas de texto completo além de consultas estruturadas por tags ou IDs.

## Como Funciona

O protocolo adiciona um campo `search` aos objetos de filtro em mensagens REQ:

1. Clientes enviam consultas de busca legíveis por humanos (ex., "melhores apps do nostr")
2. Relays interpretam e correspondem consultas contra dados de eventos, principalmente o campo `content`
3. Resultados são ordenados por relevância em vez de ordem cronológica
4. O filtro `limit` é aplicado após a ordenação por relevância

Filtros de busca podem ser combinados com outras restrições como `kinds` e `ids` para consultas mais específicas.

## Extensões de Busca

Relays podem opcionalmente suportar estes parâmetros de extensão:

- `include:spam` - Desativa filtragem de spam padrão
- `domain:<domain>` - Filtra por domínio NIP-05 verificado
- `language:<code>` - Filtra por código de idioma ISO
- `sentiment:<value>` - Filtra por sentimento negativo/neutro/positivo
- `nsfw:<true/false>` - Inclui ou exclui conteúdo NSFW

## Considerações para Clientes

- Clientes devem verificar capacidades do relay via campo `supported_nips`
- Verificação de resultados do lado do cliente é recomendada
- Nem todos os relays implementam busca; continua sendo uma funcionalidade opcional

---

**Fontes primárias:**
- [Especificação NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md)

**Mencionado em:**
- [Newsletter #3: Resumo de Dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Veja também:**
- [NIP-11: Informações do Relay](/pt/topics/nip-11/)
