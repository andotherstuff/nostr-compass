---
title: 'NIP-51: Listas'
date: 2025-12-17
draft: false
categories:
- Protocol
- Social
translationOf: /en/topics/nip-51.md
translationDate: '2026-03-07'
---

O NIP-51 define lista de eventos para organização de usuários, eventos, relays, hashtags e outras referências. É o protocolo principal para marcadores, listas de mudo, conjuntos de acompanhamento, conjuntos relay e várias outras coleções selecionadas pelo usuário.

## Listas e conjuntos padrão

- **Listas padrão** usam eventos substituíveis kinds, como listas de mudo kind `10000`, marcadores kind `10003` e pesquisa kind `10007` relays.
- **Conjuntos** usam kinds endereçáveis ​​com `d` tags, como conjuntos de acompanhamento kind `30000`, conjuntos de marcadores kind `30003` e conjuntos de emoji kind `30030`.

A distinção é importante no comportamento do cliente. As listas padrão implicam uma lista canônica por usuário e kind. Os conjuntos implicam muitas coleções nomeadas, portanto os clientes devem preservar o `d` tag de cada lista.

## Estrutura

As listas usam tags para fazer referência ao conteúdo:

- `p` tags para pubkeys
- `e` tags para eventos
- `a` tags para eventos endereçáveis
- `t` tags para hashtags
- `word` tags para palavras silenciadas
- `relay` tags para URLs relay na lista orientada a relay kinds

Algumas listas kinds têm formas tag permitidas mais estreitas do que outras. Por exemplo, listas orientadas a relay usam `relay` tags, enquanto espera-se que os marcadores apontem para notas ou eventos endereçáveis. Os clientes que tratam cada lista NIP-51 como tags de formato livre arbitrário perderão a interoperabilidade.

## Público x Privado

As listas podem ter tags públicos e itens privados. Os itens privados são serializados como um array JSON que espelha a estrutura `tags`, criptografados e armazenados no evento `content`. A especificação atual usa NIP-44 para este modelo de autocriptografia, com NIP-04 apenas como compatibilidade legada.

Essa divisão permite que os usuários publiquem um shell de lista visível enquanto ocultam algumas entradas. Uma lista de marcadores pode permanecer pública enquanto notas privadas ou marcadores privados permanecem em conteúdo criptografado.

## Tipos úteis

- **Kind 10000**: lista de silenciamento para pubkeys, tópicos, hashtags e palavras silenciadas
- **Kind 10003**: marcadores para notas e conteúdo endereçável
- **kind 10007**: pesquisa preferida relays
- **kind 30002**: conjuntos relay para grupos relay nomeados
- **Kind 30006**: conjuntos de curadoria de imagens
- **kind 39089**: pacotes iniciais para pacotes de acompanhamento compartilháveis

Mudanças recentes nas especificações moveram as hashtags de marcadores genéricos para conjuntos de interesse e adicionaram kind `30006` para curadoria de imagens. Ambas as alterações reduzem a ambiguidade na forma como os clientes interpretam o conteúdo da lista.

---

**Fontes primárias:**
- [Especificação NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md)

**Mencionado em:**
- [Boletim informativo nº 1: atualizações do NIP](/pt/newsletters/2025-12-17-newsletter/#nip-updates)
- [Boletim informativo nº 2: Atualizações do NIP](/pt/newsletters/2025-12-24-newsletter/#nip-updates)
- [Boletim informativo nº 4: Aprofundamento do NIP](/pt/newsletters/2026-01-13-newsletter/#nip-deep-dive-nip-51-and-nip-65)
- [Boletim informativo nº 8: njump adiciona suporte NIP-51](/pt/newsletters/2026-02-04-newsletter/#njump)

**Veja também:**
- [NIP-02: Lista de Seguidores](/pt/topics/nip-02/)
