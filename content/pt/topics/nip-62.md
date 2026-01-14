---
title: "NIP-62: Requisições de Desaparecimento"
date: 2026-01-13
draft: false
categories:
  - Privacy
  - Protocol
---

O NIP-62 define requisições de desaparecimento (vanish requests), um mecanismo para usuários solicitarem que relays excluam seu conteúdo. Embora os relays não sejam obrigados a honrar essas requisições, suportar o NIP-62 dá aos usuários mais controle sobre seus dados publicados e fornece uma maneira padronizada de sinalizar intenção de exclusão através da rede.

## Como Funciona

Uma requisição de desaparecimento é um evento kind 62 assinado pelo usuário que deseja que seu conteúdo seja removido. A requisição pode visar eventos específicos incluindo seus IDs em tags `e`, ou pode solicitar a exclusão de todo o conteúdo daquela pubkey omitindo as tags `e` inteiramente.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 62,
  "tags": [
    ["e", "event1234...", "wss://relay.example.com"],
    ["e", "event5678...", "wss://relay.example.com"]
  ],
  "content": "Removendo posts antigos",
  "sig": "sig1234..."
}
```

O campo `content` opcionalmente contém uma razão legível por humanos para a requisição de exclusão. As dicas de relay nas tags `e` informam aos relays onde os eventos originais foram publicados, embora os relays possam honrar requisições independentemente de terem os eventos especificados.

## Comportamento do Relay

Relays que suportam o NIP-62 devem excluir os eventos especificados de seu armazenamento e parar de servi-los aos assinantes. A requisição de desaparecimento em si pode ser retida como um registro de que a exclusão foi solicitada, o que ajuda a prevenir que eventos excluídos sejam reimportados de outros relays.

Quando uma requisição de desaparecimento omite todas as tags `e`, os relays interpretam isso como uma requisição para remover todos os eventos daquela pubkey. Esta é uma ação mais drástica e os relays podem lidar com ela de forma diferente, por exemplo, marcando a pubkey como "desaparecida" e recusando aceitar ou servir qualquer um de seus eventos dali em diante.

Os relays não são obrigados a suportar o NIP-62. A rede Nostr é descentralizada, e cada operador de relay decide suas próprias políticas de retenção de dados. Os usuários não devem assumir que seu conteúdo será excluído em todos os lugares simplesmente porque publicaram uma requisição de desaparecimento.

## Considerações de Privacidade

Requisições de desaparecimento são um mecanismo de exclusão de melhor esforço, não uma garantia de privacidade. Mesmo após publicar uma requisição de desaparecimento, cópias do conteúdo podem existir em outros lugares da rede, incluindo em outros relays que não suportam o NIP-62, em caches locais em dispositivos clientes, em arquivos ou mecanismos de busca de terceiros, e em backups.

A requisição em si também é um evento Nostr assinado, o que significa que ela se torna parte do seu registro público. Qualquer pessoa que veja a requisição de desaparecimento sabe que você excluiu algo, mesmo que não possa ver o que foi excluído.

Para conteúdo que deve permanecer privado, considere usar mensagens criptografadas como o [NIP-17](/pt/topics/nip-17/) em vez de depender de exclusão após o fato.

---

**Fontes primárias:**
- [Especificação NIP-62](https://github.com/nostr-protocol/nips/blob/master/62.md)

**Mencionado em:**
- [Newsletter #5: Mudanças Notáveis de Código](/pt/newsletters/2026-01-13-newsletter/#rust-nostr-library)
