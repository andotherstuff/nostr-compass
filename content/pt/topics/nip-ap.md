---
title: "Buzz NIP-AP: personas de agente"
date: 2026-10-21
translationOf: /en/topics/nip-ap.md
translationDate: 2026-10-28
draft: false
categories: ["NIPs"]
---

O Buzz NIP-AP é uma especificação em rascunho do projeto Buzz, fora dos NIPs aceitos em nostr-protocol/nips.

Ele define events de persona de kind 30175, que são definições endereçáveis para instanciar um agente de IA, identificadas por um slug `d` em texto puro. Já o kind 30178 contém uma projeção do catálogo da equipe. Relays que implementam a especificação restringem o acesso aos dois kinds: os autores leem os próprios events, e os demais leitores só veem um event em consultas, entrega ao vivo, buscas, contagens ou consultas por id se ele contiver `["shared", "true"]`. Compartilhar uma equipe expõe a projeção e as instruções incorporadas de cada membro, inclusive de membros cujas personas não foram compartilhadas. Essa restrição controla o acesso sem criptografar o conteúdo; o operador do relay continua podendo lê-lo.

Fonte primária: a [especificação NIP-AP](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md) no repositório do Buzz.

## Fontes primárias

- [Buzz NIP-AP: personas de agente](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md)

## Mencionado em

- [Newsletter #46 (2026-10-28): buzz](/pt/newsletters/2026-10-28-newsletter/#buzz)

- [Newsletter 45](/en/newsletters/2026-10-21-newsletter/#buzz)
