---
title: "NIP-CD: comandos de barra"
date: 2026-10-28
translationOf: /en/topics/nip-cd.md
translationDate: 2026-10-28
draft: false
categories:
  - Protocol
---

O NIP-CD define comandos de barra (slash commands). Um serviço publica um comando, e qualquer pessoa pode invocá-lo como texto simples no conteúdo de qualquer event Nostr. Trata-se de uma especificação opcional em rascunho. O NIP-CD foi incorporado em 21 de outubro de 2026 com o título Commands, depois de uma proposta anterior, e passou a se chamar Slash Commands quando as listas opcionais de comandos instalados foram incorporadas, em 27 de outubro de 2026.

## Como funciona

Um comando é definido por um event de kind 31992. As tags obrigatórias informam a palavra de acionamento sem a barra, um título e uma descrição de uso. Tags `arg` ordenadas declaram argumentos posicionais, com tipos como pubkey, event, relay, number, enum ou text. Com tags `s`, é possível limitar quais events acionam o comando por kind, relay, autor ou tag. Esses escopos funcionam como um filtro: valores do mesmo tipo são alternativas, e todo tipo presente precisa corresponder.

Uma invocação é um texto que começa no índice 0 do conteúdo de um event, como `/ban` seguido de argumentos, e não contém tags. Ao acrescentar um qualificador no formato `@nostr:npub1...`, a invocação se dirige a um único executor. Sem qualificador, qualquer comando cujo gatilho corresponda e cujo escopo inclua o event pode agir, de modo que uma única mensagem pode acionar vários serviços.

O suporte nos clientes é opcional. Eles podem oferecer preenchimento automático, seletores de argumentos e chips renderizados. Os clientes não devem exigir o próprio suporte antes de enviar uma invocação, e devem enviar como conteúdo comum o texto que não puder ser interpretado.

Em grupos baseados em relay, definições e invocações vão para o relay do grupo. No uso por difusão, as definições vão para as outboxes dos executores, e as invocações, para as inboxes dos executores.

## Listas de comandos instalados

Cada usuário pode manter uma lista opcional de kind 10992, conforme o NIP-51, com tags `a` que apontam para definições de comando de kind 31992 pela pubkey do executor e pelo valor `d`, com uma dica de relay opcional. Os clientes deveriam usar a lista para o preenchimento automático e os chips renderizados. O que a lista registra é uma preferência de exibição e descoberta do usuário. Ela não autoriza nenhum executor, e a invocação em texto simples funciona sem ela. Esta parte da especificação foi incorporada em 27 de outubro de 2026 por meio do PR #2525. O merge não mostra quais clientes implementaram a lista.

## Fontes primárias

- [Especificação NIP-CD](https://github.com/nostr-protocol/nips/blob/master/CD.md)
- [Merge do NIP-CD em 21 de outubro de 2026](https://github.com/nostr-protocol/nips/commit/7b5ea85479c0b4efce3c246abefa1dae8f8f91e4)
- [PR #2525 das listas de comandos instalados, incorporado em 27 de outubro de 2026](https://github.com/nostr-protocol/nips/pull/2525)
- [Commit de 26 de outubro de 2026 do PR #2525, feito no branch dele antes do merge](https://github.com/nostr-protocol/nips/commit/0142de0384210d69074c089448ef5bc303faef37)
- [Merge das listas de comandos instalados no NIP-CD em 27 de outubro de 2026](https://github.com/nostr-protocol/nips/commit/400d157c53264b8e58c7b3cdbd21ef546fb7a157)

## Mencionado em
- [Newsletter #46: NIP-CD define comandos invocados como texto simples](/pt/newsletters/2026-10-28-newsletter/#nip-cd-defines-commands-invoked-as-plain-text) Newsletters

- [Newsletter #46: NIP-CD adiciona listas opcionais de comandos instalados](/pt/newsletters/2026-10-28-newsletter/#nip-cd-adds-optional-installed-command-lists) Newsletters

- [Newsletter #46 (2026-10-28): outubro de 2026, significados compartilhados de consultas e serviços acionados por texto](/pt/newsletters/2026-10-28-newsletter/#october-2026-shared-query-meanings-and-text-triggered-services)

## Veja também

- [NIP-01: protocolo básico](/pt/topics/nip-01/)
