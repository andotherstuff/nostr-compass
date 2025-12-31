---
title: "NIP-54: Wiki"
date: 2025-12-31
translationOf: /en/topics/nip-54.md
translationDate: 2025-12-31
draft: false
categories:
  - Protocolo
  - Conteúdo
---

NIP-54 define kind 30818 como um tipo de evento endereçável para criar artigos wiki e entradas de enciclopédia no Nostr. Permite a criação de conteúdo colaborativo e descentralizado onde múltiplos autores podem escrever sobre os mesmos temas.

## Como Funciona

Os artigos wiki são identificados por um `d` tag normalizado (o tópico do artigo). Múltiplas pessoas podem escrever artigos sobre o mesmo assunto, criando uma base de conhecimento descentralizada sem autoridade central.

**Normalização do D Tag:**
- Converter todas as letras para minúsculas
- Converter espaços em hífens
- Remover pontuação e símbolos
- Preservar caracteres não-ASCII e números

## Formato do Conteúdo

Os artigos utilizam marcação Asciidoc com duas características especiais:

- **Wikilinks** (`[[página destino]]`) - Links para outros artigos wiki no Nostr
- **Links Nostr** - Referências a perfis ou eventos conforme NIP-21

## Seleção de Artigos

Quando existem múltiplas versões de um artigo, os clientes priorizam com base em:

1. Reações (NIP-25) indicando aprovação da comunidade
2. Listas de relays (NIP-51) para classificação de fontes
3. Listas de contatos (NIP-02) formando redes de recomendação

## Recursos Colaborativos

- **Bifurcação** - Criar versões derivadas de artigos
- **Solicitações de merge** (kind 818) - Propor alterações em artigos existentes
- **Redirecionamentos** (kind 30819) - Apontar tópicos antigos para novos
- **Marcadores de deferência** - Indicar versões preferidas de artigos

---

**Fontes primárias:**
- [Especificação NIP-54](https://github.com/nostr-protocol/nips/blob/master/54.md)

**Mencionado em:**
- [Boletim #3: Atualizações de NIP](/pt/newsletters/2025-12-31-newsletter/#nip-updates)

**Veja também:**
- [NIP-51: Listas](/pt/topics/nip-51/)
- [NIP-02: Lista de Seguidos](/pt/topics/nip-02/)
