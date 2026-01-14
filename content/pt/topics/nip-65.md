---
title: "NIP-65: Metadados de Lista de Relays"
date: 2026-01-13
draft: false
categories:
  - Protocol
  - Discovery
---

O NIP-65 define eventos kind 10002 que anunciam quais relays um usuário prefere para leitura e escrita. Esses metadados ajudam outros usuários e clientes a localizar seu conteúdo através da rede distribuída de relays, habilitando o "modelo outbox" que distribui a carga e melhora a resistência à censura.

## Estrutura

Uma lista de relays é um evento substituível (kind 10002) contendo tags `r` para cada relay que o usuário deseja anunciar. O evento substitui qualquer lista de relays anterior da mesma pubkey.

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

Cada tag `r` contém uma URL WebSocket de relay e um marcador opcional indicando como o usuário interage com aquele relay. O marcador `read` significa que o usuário consome eventos deste relay, então outros devem publicar lá para alcançar o usuário. O marcador `write` significa que o usuário publica neste relay, então outros devem se inscrever lá para ver o conteúdo do usuário. Omitir o marcador indica tanto leitura quanto escrita.

O campo `content` está vazio para eventos de lista de relays.

## O Modelo Outbox

O NIP-65 habilita um padrão de distribuição de conteúdo descentralizado chamado "modelo outbox". Em vez de todos publicarem e lerem dos mesmos relays centrais, os usuários publicam em seus próprios relays preferidos e os clientes descobrem dinamicamente onde encontrar o conteúdo de cada usuário.

Quando Alice quer encontrar os posts de Bob, seu cliente primeiro busca o evento kind 10002 de Bob de qualquer relay que o tenha. Ela então extrai os relays que Bob marcou para `write`, já que esses são onde ele publica. Seu cliente se inscreve nesses relays para os eventos de Bob. Quando Alice quer enviar a Bob uma mensagem direta, seu cliente procura pelos relays `read` dele e publica a mensagem lá.

Clientes que seguem o modelo outbox mantêm conexões com relays listados nos eventos NIP-65 de seus usuários seguidos. Conforme descobrem novas contas, eles se conectam dinamicamente a novos relays. Relays que aparecem nas listas de múltiplos usuários seguidos são priorizados, já que conectar-se a eles serve mais do grafo social do usuário.

Essa arquitetura melhora a resistência à censura porque nenhum relay único precisa armazenar ou servir o conteúdo de todos. Se um relay ficar offline ou bloquear um usuário, seu conteúdo permanece disponível em seus outros relays listados.

## Relação com Dicas de Relay

O NIP-65 complementa as dicas de relay encontradas em outros NIPs. Quando você marca alguém com `["p", "pubkey", "wss://hint.relay"]`, a dica informa aos clientes onde procurar aquela referência específica. O NIP-65 fornece a lista autoritativa de relays preferidos controlada pelo usuário, enquanto as dicas oferecem atalhos incorporados em eventos individuais para descoberta mais rápida.

## Melhores Práticas

Mantenha sua lista de relays atualizada, já que entradas desatualizadas apontando para relays extintos tornam você mais difícil de encontrar. Inclua pelo menos dois ou três relays para redundância, para que se um relay ficar offline, seu conteúdo permaneça acessível através dos outros.

Evite listar muitos relays. Quando você lista dez ou quinze relays, cada cliente que quer buscar seu conteúdo deve se conectar a todos eles, diminuindo sua experiência e aumentando a carga através da rede. Uma lista focada de três a cinco relays bem escolhidos serve você melhor do que uma lista exaustiva que sobrecarrega todos que o seguem.

Misture relays de propósito geral com quaisquer relays especializados que você usa. Por exemplo, você pode listar um relay popular de propósito geral como `wss://relay.damus.io`, um relay focado em sua região geográfica e um relay para uma comunidade específica da qual você participa.

---

**Fontes primárias:**
- [Especificação NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md)

**Mencionado em:**
- [Newsletter #5: Aprofundamento em NIPs](/pt/newsletters/2026-01-13-newsletter/#nip-65-relay-list-metadata)

**Veja também:**
- [NIP-11: Informações do Relay](/pt/topics/nip-11/)
