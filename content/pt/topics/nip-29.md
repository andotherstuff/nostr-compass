---
title: 'NIP-29: Grupos baseados em relay'
date: 2025-12-24
draft: false
categories:
- Social
- Groups
translationOf: /en/topics/nip-29.md
translationDate: 2026-03-11
---

NIP-29 define grupos baseados em relay, onde um relay gerencia membros de grupos, permissões e visibilidade de mensagens.

## Como funciona

Os grupos são codificados por um host relay mais um ID de grupo, e o relay é a autoridade para associação e moderação. Os eventos criados pelo usuário enviados para um grupo carregam um `h` tag com o ID do grupo. Os metadados gerados por relay usam eventos endereçáveis ​​assinados pela própria chave do relay.

O evento principal de metadados é kind 39000, enquanto kinds 39001 a 39003 descreve administradores, membros e funções suportadas. As ações de moderação acontecem por meio de eventos da série 9000, como `put-user`, `remove-user`, `edit-metadata` e `create-invite`.

## Modelo de acesso

- **privado**: somente membros podem ler mensagens de grupo
- **fechado**: solicitações de adesão são ignoradas, a menos que relay use manipulação de código de convite
- **oculto**: o Relay oculta os metadados do grupo de não-membros, tornando o grupo impossível de ser descoberto
- **restrito**: Somente membros podem escrever mensagens para o grupo

Estes tags são independentes. Um grupo pode ser lido por todos, mas gravável apenas pelos membros, ou totalmente oculto para não-membros. Essa separação é importante porque os clientes não devem tratar "privado" como uma abreviação geral para todas as regras de acesso.

## Modelo de confiança

O NIP-29 não é um protocolo de grupo confiável. A hospedagem relay decide quais eventos de moderação são válidos, quais funções existem, se as listas de membros são visíveis e se mensagens antigas ou fora de contexto são aceitas. Um cliente pode verificar assinaturas e referências de linha do tempo, mas ainda depende da política relay para o estado real do grupo.

Isso torna a migração e a bifurcação possíveis, mas não automáticas. O mesmo id de grupo pode existir em relays diferentes com históricos ou regras diferentes, portanto a URL relay faz parte da identidade do grupo na prática.

## Notas úteis de implementação

- Os clientes devem tratar a URL relay como a chave do host do grupo. Um esclarecimento de janeiro de 2026 tornou isso explícito nas especificações e removeu a ambigüidade sobre o uso de pubkey.
- O estado do grupo é reconstruído a partir do histórico de moderação, enquanto os eventos relay da série 39000 são instantâneos informativos desse estado
- As referências da linha do tempo `previous` existem para evitar a relay fora de contexto em bifurcações relay, não apenas para melhorar o threading da UI

---

**Fontes primárias:**
- [Especificação NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md)
- [PR #2106](https://github.com/nostr-protocol/nips/pull/2106) - Esclarecidos `private`, `closed` e `hidden`
- [PR #2190](https://github.com/nostr-protocol/nips/pull/2190) - URL relay esclarecido como a chave relay
- [PR #2111](https://github.com/nostr-protocol/nips/pull/2111) - Adicionados `unallowpubkey` e `unbanpubkey`

**Mencionado em:**
- [Boletim informativo nº 2: Atualizações do NIP](/pt/newsletters/2025-12-24-newsletter/#nip-updates)
- [Boletim informativo nº 3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Boletim informativo nº 6: Atualizações do NIP](/pt/newsletters/2026-01-21-newsletter/#nip-updates)
- [Boletim Informativo nº 11: Atualizações do NIP](/pt/newsletters/2026-02-25-newsletter/#nip-updates)
- [Boletim Informativo nº 12: Atualizações do NIP](/pt/newsletters/2026-03-04-newsletter/#nip-updates)

**Veja também:**
- [NIP-11: Documento de Informações do Relay](/pt/topics/nip-11/)
