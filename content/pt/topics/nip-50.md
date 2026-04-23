---
title: 'NIP-50: Pesquisa'
date: 2025-12-31
draft: false
categories:
- Protocol
- Relay
translationOf: /en/topics/nip-50.md
translationDate: '2026-03-07'
---

NIP-50 define uma capacidade de pesquisa geral para Nostr relays. Ele adiciona consulta em estilo de texto completo aos filtros de correspondência exata do NIP-01.

## Como funciona

O protocolo adiciona um campo `search` para filtrar objetos em mensagens `REQ`:

1. Os clientes enviam uma string de consulta legível, como `best nostr apps`.
2. Os relays interpretam essa consulta em relação aos dados do evento, principalmente no campo `content`.
3. Os resultados são classificados por qualidade de correspondência, não por `created_at`.
4. `limit` se aplica após a classificação por relevância.

Os filtros de pesquisa podem ser combinados com `kinds`, `ids`, autores e outros campos de filtro normais para consultas mais específicas.

## Extensões de pesquisa

Os relays podem suportar opcionalmente estes parâmetros de extensão:

- `include:spam` - Desativa a filtragem de spam padrão
- `domain:<domain>` - Filtra por domínio NIP-05 verificado
- `language:<code>` - Filtra por código de idioma ISO
- `sentiment:<value>` - Filtra por sentimento negativo, neutro ou positivo
- `nsfw:<true/false>` - Inclui ou exclui conteúdo NSFW

Os relays devem ignorar extensões que não suportam, portanto, os clientes precisam tratá-los como dicas e não como garantias.

## Notas de interoperabilidade

- Os clientes devem verificar as capacidades do relay através do campo `supported_nips`
- Recomenda-se a verificação dos resultados do lado do cliente
- Nem todos os relays implementam busca; continua sendo um recurso opcional

Como a classificação é definida pela implementação, a mesma consulta pode retornar conjuntos de resultados diferentes em relays diferentes. Os clientes que se preocupam com o recall devem consultar mais de uma pesquisa relay e mesclar os resultados.

## Por que é importante

Filtros estruturados funcionam bem quando você já conhece o autor, kind ou tag desejado. A busca é para o caso oposto: descoberta. Isso torna o NIP-50 útil para diretórios de aplicativos, arquivos longos e pesquisa de notas públicas, mas também significa que a qualidade da pesquisa depende muito das opções de indexação e filtragem de spam de cada relay.

---

**Fontes primárias:**
- [Especificação NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md)

**Mencionado em:**
- [Boletim informativo nº 3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/)
- [Boletim informativo nº 7: Atualizações do NIP](/pt/newsletters/2026-01-07-newsletter/)

**Veja também:**
- [NIP-11: Informações do Relay](/pt/topics/nip-11/)
