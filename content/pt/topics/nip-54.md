---
title: 'NIP-54: Wiki'
date: 2025-12-31
draft: false
categories:
- Protocol
- Content
translationOf: /en/topics/nip-54.md
translationDate: '2026-03-07'
---

NIP-54 define kind `30818` para artigos estilo wiki no Nostr. Vários autores podem publicar entradas para o mesmo tópico, portanto, os clientes precisam de heurísticas de classificação e confiança em vez de uma única página canônica.

## Como funciona

Os artigos Wiki são identificados por um `d` tag normalizado que representa o tópico. Várias pessoas podem publicar entradas com o mesmo tópico normalizado, criando um wiki aberto sem um editor central.

**Normalização de tags D:**
- Letras minúsculas que possuem variantes de maiúsculas e minúsculas
- Converter espaços em branco em hífens
- Remover pontuação e símbolos
- Recolher hífens repetidos e cortar hífens iniciais ou finais
- Preservar letras e números não-ASCII

Essa regra de normalização é importante para a interoperabilidade. Se dois clientes normalizarem o mesmo título de maneira diferente, eles consultarão tópicos diferentes e fragmentarão o conjunto de artigos.

## Formato do conteúdo

A especificação mesclada usa marcação Asciidoc com dois recursos extras:

- **Wikilinks** (`[[target page]]`) - Links para outros artigos wiki no Nostr
- **Nostr links** - Referências a perfis ou eventos conforme NIP-21

Foi proposta uma mudança para Djot, mas não substituiu o Asciidoc no NIP canônico em março de 2026.

## Seleção de artigos

Quando existem várias versões de um artigo, os clientes podem priorizar com base em:

1. Reações (NIP-25) indicando aprovação da comunidade
2. Listas de relay (NIP-51) para classificação de fontes
3. Listas de contactos (NIP-02) formando redes de recomendação

Na prática, isto significa que o NIP-54 não é apenas um formato de conteúdo. É também um problema de política do cliente. Dois clientes podem mostrar "melhores" artigos diferentes para o mesmo tópico, enquanto ambos permanecem em conformidade com as especificações.

## Recursos colaborativos

- **Forking** - Crie versões derivadas de artigos
- **Solicitações de mesclagem** (kind 818) - Propor alterações em artigos existentes
- **Redirecionamentos** (kind 30819) - Aponte tópicos antigos para novos
- **Marcadores de deferência** - Indicam versões preferidas do artigo

Bifurcações e marcadores de deferência permitem que os autores reconheçam versões melhores sem excluir seu próprio trabalho. Isso é importante em uma rede onde revisões antigas podem permanecer disponíveis em muitos relays.

---

**Fontes primárias:**
- [Especificação NIP-54](https://github.com/nostr-protocol/nips/blob/master/54.md)
- [PR #2177: Normalização d-tag internacionalizada](https://github.com/nostr-protocol/nips/pull/2177)

**Mencionado em:**
- [Boletim informativo nº 3: Atualizações do NIP](/pt/newsletters/2025-12-31-newsletter/#nip-updates)
- [Boletim informativo nº 15: PRs abertos](/pt/newsletters/2026-03-04-newsletter/#open-prs-and-project-updates)

**Veja também:**
- [NIP-51: Listas](/pt/topics/nip-51/)
- [NIP-02: Lista de Seguidores](/pt/topics/nip-02/)
