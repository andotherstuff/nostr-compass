---
title: "NIP-03: Atestações OpenTimestamps para events"
date: 2026-10-28
translationOf: /en/topics/nip-03.md
translationDate: 2026-10-28
draft: false
categories:
  - Protocol
---

A NIP-03 descreve como publicar uma prova [OpenTimestamps](https://opentimestamps.org/) para um event Nostr. A prova serve como evidência de que o event já existia no momento de um determinado bloco do Bitcoin.

**Aviso:** a especificação atual está rotulada como `draft`, `optional` e `unrecommended`. Segundo o cabeçalho, ela é vulnerável a um ataque específico e precisa de uma atualização. O texto não descreve o ataque. Trate o formato como referência histórica e não o adote em trabalhos novos até que a especificação seja revisada.

## Como funciona

Cada prova é publicada como um event separado de kind 1040. A tag `e` indica o id do event alvo, acompanhado de uma URL de relay, e a tag `k` registra o kind do event alvo. Como digest, a prova OpenTimestamps deve provar o próprio id do event alvo. O id não passa por um novo hash.

O `content` contém o arquivo `.ots` completo, codificado em base64, com pelo menos uma atestação do Bitcoin. A especificação recomenda exatamente uma atestação e nenhuma atestação pendente, já que estas acrescentam bytes sem ajudar na verificação.

Um verificador busca o event de kind 1040, decodifica o conteúdo e confere a prova com o Bitcoin. Uma prova válida mostra que o id do event já estava comprometido no bloco atestado. Com isso, fica estabelecido um limite máximo para o momento de criação do event, independente do valor `created_at` informado pelo próprio autor. Isso não mostra que o conteúdo do event seja verdadeiro.

## Histórico

Um [commit de 11 de outubro de 2023](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e) mudou o lugar onde as provas ficam. Antes dele, a prova era um campo `ots` anexado ao próprio event. Depois dele, cada prova passou a ser um event separado de kind 1040 que aponta para o seu alvo.

## Fontes primárias

- [Especificação atual da NIP-03](https://github.com/nostr-protocol/nips/blob/master/03.md)
- [Commit de 11 de outubro de 2023 que moveu as provas para events de kind 1040](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e)

## Mencionado nas newsletters

- [Newsletter #46 (2026-10-28): outubro de 2023, events trazem evidências e pedidos de trabalho](/pt/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)

## Veja também

- [NIP-01: Protocolo básico](/pt/topics/nip-01/)
