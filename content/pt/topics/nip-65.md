---
title: 'NIP-65: Metadados da Lista de Relays'
date: 2026-01-13
draft: false
categories:
- Protocol
- Discovery
translationOf: /en/topics/nip-65.md
translationDate: '2026-03-07'
---

NIP-65 define eventos kind 10002 que anunciam quais relays um usuário prefere para leitura e escrita. Esses metadados ajudam outros usuários e clientes a localizar seu conteúdo na rede distribuída de relays, habilitando o "modelo outbox" que distribui a carga e melhora a resistência à censura.

## Estrutura

Uma lista de relays é um evento substituível (kind 10002) contendo `r` tags para cada relay que o usuário deseja anunciar. O evento substitui qualquer lista de relays anterior do mesmo pubkey.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "sig1234..."
}
```

Cada `r` tag contém uma URL WebSocket de relay e um marcador opcional que indica como o usuário interage com aquele relay. O marcador `read` significa que o usuário consome eventos deste relay, portanto outros deverão publicar lá para chegar ao usuário. O marcador `write` significa que o usuário publica neste relay, portanto outros devem se inscrever lá para ver o conteúdo do usuário. A omissão do marcador indica leitura e gravação.

O campo `content` fica vazio para eventos de lista de relays.

## O Modelo Outbox

O NIP-65 permite um padrão de distribuição de conteúdo descentralizado chamado "modelo outbox". Em vez de todos publicarem e lerem nos mesmos relays centrais, os usuários publicam nos relays de sua preferência, e os clientes descobrem dinamicamente onde encontrar o conteúdo de cada usuário.

Quando Alice deseja encontrar as postagens de Bob, seu cliente primeiro busca o evento kind 10002 de Bob em qualquer relay que o possua. Ela então extrai os relays que Bob marcou com `write`, já que é nesses relays que ele publica. O cliente dela passa a assinar esses relays para receber os eventos de Bob. Quando Alice deseja enviar uma mensagem direta a Bob, seu cliente procura os relays marcados com `read` e publica a mensagem neles.

Os clientes que seguem o modelo outbox mantêm conexões com os relays listados nos eventos NIP-65 das contas que acompanham. À medida que descobrem novas contas, eles se conectam dinamicamente a novos relays. Relays que aparecem nas listas de vários usuários seguidos recebem prioridade, porque conectar-se a eles atende uma parcela maior do grafo social do usuário.

Essa arquitetura melhora a resistência à censura porque nenhum relay precisa armazenar ou servir o conteúdo de todos. Se um relay ficar offline ou bloquear um usuário, seu conteúdo permanece disponível nos outros relays listados.

## Por que é importante

NIP-65 altera a seleção de relays de um padrão de cliente codificado para metadados de roteamento publicados pelo usuário. Isso permite que os clientes se adaptem aos hábitos reais de publicação e leitura de cada conta, em vez de presumir que todos usam o mesmo conjunto de relays.

Também transfere a complexidade para os clientes. Para usar bem o modelo outbox, um cliente precisa de cache de relays, lógica de nova tentativa e comportamento de fallback quando uma lista de relays está ausente ou obsoleta. A especificação melhora a capacidade de descoberta, mas não elimina a necessidade de boas heurísticas de seleção de relays.

## Relação com Dicas de Relay

O NIP-65 complementa as dicas de relay encontradas em outros NIPs. Quando você marca alguém com `["p", "pubkey", "wss://hint.relay"]`, a dica informa aos clientes onde procurar aquela referência específica. O NIP-65 fornece a lista autoritativa de relays preferidos controlada pelo usuário, enquanto as dicas oferecem atalhos incorporados em eventos individuais para uma descoberta mais rápida.

Para mensagens privadas, o NIP-65 não conta a história completa. O roteamento de conteúdo público usa kind 10002, mas as pilhas modernas de mensagens privadas geralmente dependem de metadados de caixa de entrada separados, como as listas de relay do [NIP-17](/pt/topics/nip-17/), para que os usuários possam manter o roteamento de DM separado dos relays usados para postagem pública.

## Melhores práticas

Mantenha sua lista de relays atualizada, porque entradas obsoletas apontando para relays extintos tornam você mais difícil de encontrar. Inclua pelo menos dois ou três relays para redundância, para que, se um relay ficar offline, seu conteúdo permaneça acessível pelos outros.

Evite listar muitos relays. Quando você lista dez ou quinze relays, cada cliente que deseja buscar seu conteúdo deve se conectar a todos eles, tornando sua experiência mais lenta e aumentando a carga na rede. Uma lista focada de três a cinco relays bem escolhidos é melhor para você do que uma lista exaustiva que sobrecarrega todos que o seguem.

Misture relays de uso geral com qualquer relay especializado que você usar. Por exemplo, você pode listar um relay geral popular como `wss://relay.damus.io`, um relay focado em sua região geográfica e um relay para uma comunidade específica da qual você participa.

---

**Fontes primárias:**
- [Especificação NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md)

**Mencionado em:**
- [Boletim informativo nº 5: Aprofundamento do NIP](/pt/newsletters/2026-01-13-newsletter/#nip-65-relay-list-metadata)
- [Boletim informativo nº 10: Benchmarks do Modelo Outbox](/pt/newsletters/2026-03-04-newsletter/)

**Veja também:**
- [NIP-11: Informações do Relay](/pt/topics/nip-11/)
- [NIP-17: Mensagens Diretas Privadas](/pt/topics/nip-17/)
