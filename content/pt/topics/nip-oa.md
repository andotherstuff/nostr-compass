---
title: 'Rascunho NIP-OA do Buzz: Atestação do Proprietário'
date: 2026-10-28
translationOf: /en/topics/nip-oa.md
translationDate: 2026-10-28
draft: false
---

**Status:** Esta é uma proposta em rascunho específica do projeto Buzz. A NIP-OA não é uma NIP oficial aceita. O rótulo vem da documentação do projeto Buzz, e o repositório oficial de NIPs não o atribuiu nem o aprovou.

## Finalidade

A NIP-OA define uma tag opcional `auth` que permite que uma chave de proprietário autorize uma chave de agente a publicar events. A autoria do event continua sendo da chave do agente. Uma tag válida vale apenas como evidência de autorização e não permite que o agente se passe pelo proprietário.

## Mecanismo

Com uma assinatura Schnorr, o proprietário assina um hash com separação de domínio que vincula a pubkey do agente a uma string de condições exata. As condições podem exigir um kind de event e definir limites para o `created_at` autodeclarado. O agente pode reutilizar a tag em seus events, desde que cada event atenda às condições. Os verificadores primeiro validam o event básico e, em seguida, conferem a assinatura do proprietário e cada uma das condições.

## Limites

Uma string de condições vazia não acrescenta nenhuma restrição. Como as cláusulas de timestamp restringem um campo controlado pelo agente, elas não oferecem expiração baseada no horário real. Quem precisar garantir a atualidade tem de verificá-la separadamente. Publicar a tag abertamente vincula as chaves do proprietário e do agente.

## Fontes primárias

- [Rascunho NIP-OA do Buzz: Atestação do Proprietário (revisão fixada)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-OA.md)

## Veja também

- [NIP-01](/pt/topics/nip-01/)

**Mencionado em:**

- [Newsletter #46: Buzz](/pt/newsletters/2026-10-28-newsletter/#buzz)
