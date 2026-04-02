---
title: "NIP-43: Metadados e Requisições de Acesso ao Relay"
date: 2026-03-18
translationOf: /en/topics/nip-43.md
translationDate: 2026-04-01
draft: false
categories:
  - Protocol
  - Relay
  - Access Control
---

NIP-43 define como relays publicam informações de membros e como usuários solicitam admissão, convites ou remoção de relays restritos. Ele dá ao controle de acesso de relay uma superfície de evento padrão em vez de forçar cada relay privado ou semi-privado a inventar seu próprio protocolo de entrada.

## Como Funciona

A spec combina vários kinds de evento:

- kind `13534` publica uma lista de membros do relay
- kind `8000` anuncia que um membro foi adicionado
- kind `8001` anuncia que um membro foi removido
- kind `28934` permite que um usuário envie uma requisição de entrada com um código de reivindicação
- kind `28935` permite que um relay retorne um código de convite sob demanda
- kind `28936` permite que um usuário solicite que seu próprio acesso seja revogado

O estado de membros intencionalmente não é derivado de um único evento. Um cliente pode precisar consultar tanto os eventos de membros assinados pelo relay quanto os próprios eventos do membro antes de decidir se o acesso é atual.

## Por Que Importa

NIP-43 dá a relays restritos uma forma padrão de expressar estado de admissão e membros. Isso importa para sistemas de grupo, comunidades somente por convite, e relays que precisam de onboarding legível por máquina sem recorrer a formulários web fora de banda ou fluxos manuais de operador.

A clarificação aberta no [PR #2267](https://github.com/nostr-protocol/nips/pull/2267) torna um ponto prático mais preciso: relays devem manter um estado de membros autoritativo por pubkey. Isso ajuda clientes a evitar históricos de replay ambíguos onde um evento antigo de adição ou remoção pode ser mal interpretado como estado atual.

## Notas de Interoperabilidade

NIP-43 depende do relay anunciar suporte através de seu documento [NIP-11](/pt/topics/nip-11/). Requisições de entrada, requisições de convite e requisições de saída só devem ser enviadas para relays que explicitamente declarem suportar este NIP.

Como os eventos existem em espaços controlados pelo relay e pelo usuário ao mesmo tempo, implementações precisam de regras claras de conflito. É por isso que a clarificação do estado de membros importa mais do que parece à primeira vista.

---

**Fontes primárias:**
- [Especificação NIP-43](https://github.com/nostr-protocol/nips/blob/master/43.md)
- [PR #2267](https://github.com/nostr-protocol/nips/pull/2267) - Clarificação do tratamento de estado de membros

**Mencionado em:**
- [Newsletter #14: Atualizações de NIPs](/pt/newsletters/2026-03-18-newsletter/#atualizações-de-nips)

**Veja também:**
- [NIP-11: Relay Information Document](/pt/topics/nip-11/)
- [NIP-42: Authentication of Clients to Relays](/pt/topics/nip-42/)
