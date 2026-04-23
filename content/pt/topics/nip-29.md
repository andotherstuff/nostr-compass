---
title: 'NIP-29: Grupos baseados em relay'
date: 2025-12-24
draft: false
categories:
  - Social
  - Groups
translationOf: /en/topics/nip-29.md
translationDate: 2026-04-22
---

NIP-29 define grupos baseados em relay, em que um relay gerencia membership, permissões e visibilidade de mensagens do grupo.

## Como funciona

Grupos são identificados por um host de relay somado a um group id, e o relay é a autoridade para membership e moderação. Eventos criados por usuários e enviados para um grupo carregam uma tag `h` com o group id. Metadados gerados pelo relay usam eventos endereçáveis assinados pela própria chave do relay.

O evento central de metadados é o kind 39000, enquanto os kinds 39001 até 39003 descrevem admins, membros e papéis suportados. Ações de moderação acontecem por meio de eventos da série 9000, como `put-user`, `remove-user`, `edit-metadata` e `create-invite`.

## Modelo de acesso

- **private**: apenas membros podem ler mensagens do grupo
- **closed**: requests de entrada são ignorados, a menos que o relay use tratamento por invite code
- **hidden**: o relay esconde os metadados do grupo de não membros, tornando-o indiscoverable
- **restricted**: apenas membros podem escrever mensagens no grupo

Essas tags são independentes. Um grupo pode ser legível por todos e gravável só por membros, ou totalmente oculto a não membros. Essa separação importa porque clientes não devem tratar private como um atalho genérico para toda regra de acesso.

## Modelo de confiança

NIP-29 não é um protocolo de grupo trustless. O relay hospedando o grupo decide quais eventos de moderação são válidos, quais papéis existem, se listas de membros são visíveis e se mensagens antigas ou fora de contexto são aceitas. Um cliente pode verificar assinaturas e referências da timeline, mas ainda depende da política do relay para o estado real do grupo.

Isso torna migração e fork possíveis, mas não automáticos. O mesmo group id pode existir em relays diferentes com históricos ou regras diferentes, então a URL do relay faz parte da identidade prática do grupo.

## Notas úteis de implementação

- Clientes devem tratar a URL do relay como a chave do host do grupo. Uma clarificação de janeiro de 2026 deixou isso explícito na spec e removeu ambiguidade sobre uso de pubkey no lugar
- O estado do grupo é reconstruído a partir do histórico de moderação, enquanto eventos da série 39000 são snapshots informativos desse estado
- Referências `previous` na timeline existem para impedir rebroadcasts fora de contexto entre forks de relay, não apenas para melhorar threading de UI

## Trabalho recente na spec

- [PR #2310](https://github.com/nostr-protocol/nips/pull/2310) e as [notas de release do Flotilla 1.7.3/1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4) propõem encapsulamento em kind 9 de tipos de conteúdo que não são chat, como eventos de calendário, enquetes e outros payloads, para preservar o contexto da sala quando esses objetos são enviados a um grupo.
- [PR #2319](https://github.com/nostr-protocol/nips/pull/2319) estende a spec com uma hierarquia de subgrupos para que um único grupo hospede vários canais paralelos sem precisar criar grupos independentes no mesmo relay; o identificador do subgrupo se apoia na tag `h` existente, preservando mensagens com uma única tag `h` para clientes antigos.
- [PR #2316](https://github.com/nostr-protocol/nips/pull/2316) define permissões explícitas no evento de papéis kind 39003, para que cada papel passe a ser um conjunto nomeado de operações concedidas, como invite, add-user, remove-user, edit-metadata, delete-event e add-permission, com expiração opcional.

## Implementações

- [Flotilla](https://gitea.coracle.social/coracle/flotilla) é o principal cliente NIP-29 do hodlbod; [1.7.3](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.3) e [1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4) lançaram encapsulamento em kind 9, enquetes, login [NIP-46](/pt/topics/nip-46/) via esquema de URL do Aegis, compartilhamento nativo de invites para spaces, room mentions, colagem de imagem da área de transferência no mobile, drafts e vídeo em chamadas.
- [Wisp](https://github.com/barrydeen/wisp) adicionou configuração de grupos NIP-29 para flags, invites, papéis e prompts AUTH no [PR #471](https://github.com/barrydeen/wisp/pull/471) e reforçou a sequência de AUTH antes de eventos de grupo `9021`, `9007` e `9009` no [PR #478](https://github.com/barrydeen/wisp/pull/478).

---

**Fontes primárias:**
- [Especificação NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md)
- [PR #2106](https://github.com/nostr-protocol/nips/pull/2106) - clarifica `private`, `closed` e `hidden`
- [PR #2190](https://github.com/nostr-protocol/nips/pull/2190) - clarifica a URL do relay como chave do relay
- [PR #2111](https://github.com/nostr-protocol/nips/pull/2111) - adiciona `unallowpubkey` e `unbanpubkey`
- [PR #2310](https://github.com/nostr-protocol/nips/pull/2310) - encapsulamento kind 9 para conteúdo não chat
- [PR #2319](https://github.com/nostr-protocol/nips/pull/2319) - spec de subgrupos
- [PR #2316](https://github.com/nostr-protocol/nips/pull/2316) - permissões explícitas de papel em kind 39003
- [Flotilla 1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4)
- [Wisp PR #471](https://github.com/barrydeen/wisp/pull/471) - configuração de grupos NIP-29

**Mencionado em:**
- [Newsletter #2: Atualizações de NIP](/pt/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/)
- [Newsletter #6: Atualizações de NIP](/pt/newsletters/2026-01-21-newsletter/)
- [Newsletter #11: Atualizações de NIP](/pt/newsletters/2026-02-25-newsletter/)
- [Newsletter #12: Atualizações de NIP](/pt/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: Flotilla 1.7.3/1.7.4](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: configuração NIP-29 no Wisp](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: Atualizações de NIP, subgrupos e permissões de papel](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-11: Relay Information Document](/pt/topics/nip-11/)
