---
title: 'Rascunho NIP-RS do Buzz: Sincronização do Estado de Leitura entre Dispositivos'
date: 2026-10-28
translationOf: /en/topics/nip-rs.md
translationDate: 2026-10-28
draft: false
---

**Status:** Esta é uma proposta em rascunho específica do projeto Buzz. A NIP-RS não é uma NIP oficial aceita. O rótulo vem da documentação do projeto Buzz, e o repositório oficial de NIPs não o atribuiu nem o aprovou.

## Finalidade

A NIP-RS permite que os dispositivos de um mesmo usuário compartilhem até onde esse usuário já leu. Cada instalação publica um event endereçável `kind:30078`. Sua tag `d` é `read-state:` seguido de um ID de slot aleatório, e seu conteúdo é criptografado com NIP-44 para a própria chave do usuário. No texto em claro, IDs de contexto são mapeados para fronteiras de timestamp, e cada uma delas indica que tudo o que está naquele horário ou antes dele foi lido. O rascunho não publica confirmações de leitura nem revela o que outras pessoas leram.

## Limites

As fronteiras são indicações de melhor esforço sobre a atividade recente. Elas não formam um histórico completo das mensagens lidas. As substituições manuais para não lido, incluindo pisos de tombstone, seguem um contrato durável separado. Carregar o estado completo dessas substituições depende do comportamento de ordenação e de capacidade do relay, que um cliente não consegue verificar totalmente; por isso, um relay arbitrário pode não retornar o estado completo de não lidos. Na maior parte dos casos, os IDs de contexto só têm significado dentro de uma única família de clientes.

Um pull request aberto, o #8639, propõe migrar os clientes do Buzz para uma capacidade NIP-11 `buzz_v1` apoiada por uma API HTTP privada e autenticada, desativada por padrão. Relays sem essa capacidade continuariam usando a NIP-RS.

## Fontes primárias

- [Rascunho NIP-RS do Buzz: Sincronização do Estado de Leitura entre Dispositivos (revisão fixada)](https://github.com/block/buzz/blob/646ef8abf9bc5ac3e698826b38811033537a4806/docs/nips/NIP-RS.md)
- [Pull request #8639 do Buzz: estado de leitura por meio de uma capacidade do relay (aberto)](https://github.com/block/buzz/pull/8639)

## Veja também

- [NIP-44](/pt/topics/nip-44/)
- [NIP-78](/pt/topics/nip-78/)

**Mencionado em:**

- [Newsletter #46: Buzz](/pt/newsletters/2026-10-28-newsletter/#buzz)
