---
title: "Proposta NIP-FE: Comandos de relay por HTTP"
date: 2026-09-30
translationOf: /en/topics/nip-fe.md
translationDate: 2026-10-02
draft: false
categories:
  - Project Proposals
  - Relays
---

O Amethyst usa o rótulo provisório NIP-FE para comandos de relay por HTTP em seu trabalho no relay Geode e no cliente Quartz. O rótulo não é um NIP atribuído nem evidência de adoção entre relays Nostr.

## Transporte

Em vez de abrir uma conexão WebSocket, o cliente envia por POST um único frame `REQ`, `COUNT` ou `EVENT` para um endpoint HTTP do relay. A resposta transmite frames do relay como JSON delimitado por quebras de linha. O cliente precisa distinguir uma resposta concluída de um stream interrompido, e uma solicitação autenticada continua usando a autorização HTTP assinada do Nostr. O transporte muda a forma como os comandos chegam a um relay; ele não muda a assinatura nem o conteúdo do event subjacente.

A [implementação incorporada](https://github.com/vitorpamplona/amethyst/pull/4231) do Amethyst adiciona a rota do Geode, o suporte no cliente Quartz, limites de corpo e de concorrência e testes de enquadramento e autorização. É evidência de implementação no código-fonte, e não prova de que relays independentes implementaram a mesma proposta.

## Colisão de nomes

Um [pull request em rascunho não relacionado no repositório de NIPs](https://github.com/nostr-protocol/nips/pull/2488) também usa **NIP-FE**, desta vez para feeds privados construídos sobre um envelope proposto para múltiplos destinatários. Esse trabalho está aberto e descreve um problema diferente do transporte HTTP do Amethyst. Nenhum dos dois usos provisórios estabelece que o rótulo foi atribuído a uma especificação aceita; os leitores devem identificar a proposta por sua fonte e seu assunto.

---

**Fontes primárias:**
- [PR de implementação no Geode e no Quartz do Amethyst](https://github.com/vitorpamplona/amethyst/pull/4231)
- [Repositório do Amethyst](https://github.com/vitorpamplona/amethyst)
- [Rascunho aberto de feeds privados que também usa NIP-FE](https://github.com/nostr-protocol/nips/pull/2488)

**Mencionado em:**
- [Newsletter #42: comandos de relay do Amethyst](/pt/newsletters/2026-09-30-newsletter/#amethyst-repairs-encrypted-group-interoperability)
