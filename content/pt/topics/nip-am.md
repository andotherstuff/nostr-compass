---
title: 'Rascunho NIP-AM do Buzz: métricas de turno de agente'
date: 2026-10-28
translationOf: /en/topics/nip-am.md
translationDate: 2026-10-28
draft: false
---

**Situação:** este é um rascunho de proposta específico do projeto Buzz. O NIP-AM não é um NIP oficial aceito. O rótulo vem da documentação do projeto Buzz, e o repositório oficial de NIPs não o atribuiu nem o aprovou.

## Finalidade

O NIP-AM registra o uso de cada turno concluído de um agente de IA. Por turno, o agente publica um event `kind:44200`, que a convenção do Buzz trata como um event regular do tipo append-only, ao qual apenas se acrescentam registros. O conteúdo é criptografado com NIP-44 pelo agente para o dono. Nele ficam os números de uso de tokens junto com IDs de correlação, e quaisquer valores de custo são estimativas. Nenhuma transcrição de conversa é incluída.

## Limites

Tags públicas identificam o dono e o agente, e os relays continuam podendo ver quando os events são publicados. Por isso, o formato não esconde que houve atividade. Um valor de uso ausente significa desconhecido e nunca deve ser contado como zero.

## Proposta de leitores delegados

Um pull request de documentação ainda aberto, o #8582, propõe uma concessão de privilégio mínimo assinada pelo dono. Por essa proposta, o agente publicaria uma cópia criptografada separada para cada leitor ativo, cada uma vinculada ao ID exato do event de concessão. Nenhuma autorização em tempo de execução é alterada pelo pull request. O kind de concessão proposto, `30180`, e o limite de leitores continuam sendo questões em aberto, e a política de revogação também não está definida. A revogação poderia limitar o histórico nos relays e as leituras futuras. Cópias que um leitor já recebeu, porém, ela não consegue apagar.

## Fontes primárias

- [Rascunho NIP-AM do Buzz: métricas de turno de agente (revisão fixada)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-AM.md)
- [Pull request #8582 do Buzz: leitores delegados de métricas (rascunho aberto)](https://github.com/block/buzz/pull/8582)

## Veja também

- [NIP-44](/pt/topics/nip-44/)

**Mencionado em:**

- [Newsletter #46: texto do rascunho NIP-AM para leitores delegados de métricas](/pt/newsletters/2026-10-28-newsletter/#draft-nip-am-text-for-delegated-metric-readers)
- [Newsletter #46: Buzz](/pt/newsletters/2026-10-28-newsletter/#buzz)
