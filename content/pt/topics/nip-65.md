---
title: 'NIP-65: Metadados de lista de relays'
date: 2026-01-13
draft: false
categories:
  - Protocol
  - Discovery
translationOf: /en/topics/nip-65.md
translationDate: 2026-04-22
---

NIP-65 define eventos kind `10002` que anunciam quais relays um usuário prefere para leitura e escrita. Esses metadados ajudam outros usuários e clientes a localizar seu conteúdo na rede distribuída de relays, habilitando o outbox model, que distribui carga e melhora resistência à censura.

## Estrutura

Uma lista de relays é um evento replaceable, kind `10002`, contendo tags `r` para cada relay que o usuário quer anunciar. O evento substitui qualquer lista de relays anterior da mesma pubkey.

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

Cada tag `r` contém uma URL WebSocket de relay e um marcador opcional indicando como o usuário interage com aquele relay. O marcador `read` significa que o usuário consome eventos desse relay, então outros deveriam publicar lá para alcançá-lo. O marcador `write` significa que o usuário publica nesse relay, então outros deveriam assinar ali para ver o conteúdo do usuário. Omitir o marcador indica leitura e escrita.

O campo `content` é vazio em eventos de lista de relays.

## O outbox model

NIP-65 habilita um padrão descentralizado de distribuição de conteúdo chamado outbox model. Em vez de todo mundo publicar e ler nos mesmos relays centrais, usuários publicam em seus próprios relays preferidos e clientes descobrem dinamicamente onde encontrar o conteúdo de cada usuário.

Quando Alice quer encontrar os posts de Bob, o cliente dela primeiro busca o evento kind `10002` de Bob em qualquer relay que o tenha. Em seguida, extrai os relays que Bob marcou para `write`, porque é ali que ele publica. O cliente dela assina esses relays para receber os eventos de Bob. Quando Alice quer enviar uma mensagem direta a Bob, o cliente procura os relays `read` dele e publica a mensagem lá.

Clientes que seguem o outbox model mantêm conexões com relays listados nos eventos NIP-65 dos usuários seguidos. À medida que descobrem novas contas, conectam-se dinamicamente a novos relays. Relays que aparecem nas listas de múltiplos usuários seguidos ganham prioridade, já que conectar a eles atende uma parte maior do grafo social do usuário.

Essa arquitetura melhora a resistência à censura porque nenhum relay único precisa armazenar ou servir o conteúdo de todos. Se um relay sai do ar ou bloqueia um usuário, o conteúdo dele continua disponível nos outros relays listados.

## Por que importa

NIP-65 transforma seleção de relay de um padrão hardcoded do cliente em metadados de roteamento publicados pelo usuário. Isso permite que clientes se adaptem aos hábitos reais de publicação e leitura de cada conta em vez de assumir que todos usam o mesmo conjunto de relays.

Também desloca complexidade para os clientes. Para usar bem o outbox model, um cliente precisa de cache de relay, lógica de retry e fallback quando uma lista de relays está ausente ou desatualizada. A spec melhora a discoverability, mas não elimina a necessidade de boas heurísticas de seleção de relay.

## Relação com relay hints

NIP-65 complementa os relay hints espalhados por outros NIPs. Quando você marca alguém com `['p', 'pubkey', 'wss://hint.relay']`, o hint diz aos clientes onde procurar por aquela referência específica. NIP-65 fornece a lista autoritativa e controlada pelo usuário de relays preferidos, enquanto hints oferecem atalhos embutidos em eventos individuais para descoberta mais rápida.

Para mensagens privadas, NIP-65 não conta toda a história. O roteamento de conteúdo público usa kind `10002`, mas stacks modernas de mensagens privadas frequentemente dependem de metadados separados de inbox, como listas de relays da [NIP-17](/pt/topics/nip-17/), para que usuários mantenham o roteamento de DMs distinto dos relays de postagem pública.

## Boas práticas

Mantenha sua lista de relays atualizada, porque entradas desatualizadas apontando para relays mortos tornam você mais difícil de encontrar. Inclua pelo menos dois ou três relays para redundância, para que, se um relay sair do ar, seu conteúdo continue acessível nos demais.

Evite listar relays demais. Quando você lista dez ou quinze relays, todo cliente que quiser buscar seu conteúdo precisa conectar a todos eles, deixando a experiência mais lenta e aumentando a carga na rede. Uma lista focada de três a cinco relays bem escolhidos serve melhor do que uma lista exaustiva que pesa sobre todos que seguem você.

Misture relays de uso geral com relays especializados que você utiliza. Por exemplo, você pode listar um relay geral popular como `wss://relay.damus.io`, um relay focado em sua região geográfica e um relay de uma comunidade específica da qual você participa.

---

**Fontes primárias:**
- [Especificação NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md)

**Mencionado em:**
- [Newsletter #5: NIP Deep Dive](/pt/newsletters/2026-01-13-newsletter/)
- [Newsletter #12: benchmarks do outbox model](/pt/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: broadcasting para inbox relays no Wisp](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-11: Relay Information](/pt/topics/nip-11/)
- [NIP-17: Mensagens Diretas Privadas](/pt/topics/nip-17/)
