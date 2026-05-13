---
title: "NIP-78: Dados específicos do aplicativo"
date: 2026-05-14
draft: false
translationOf: /en/topics/nip-78.md
translationDate: 2026-05-13
categories:
  - NIPs
  - Data Storage
---

NIP-78 define um kind de evento padrão para que aplicações armazenem dados arbitrários em nome de um usuário usando eventos Nostr, permitindo sincronização de estado entre dispositivos sem um servidor centralizado.

## Como funciona

O kind de evento central é 30078, um evento substituível parametrizado. A tag `d` é uma string identificadora definida pela aplicação que delimita o slot de armazenamento a uma aplicação e propósito específicos.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1747180800,
  "kind": 30078,
  "tags": [
    ["d", "myapp-settings"]
  ],
  "content": "{\"theme\":\"dark\",\"fontSize\":14}",
  "sig": "<128-char hex>"
}
```

Uma aplicação publica um evento 30078 com uma tag `d` única (por exemplo `tamagostrich-pet-state` ou `amethyst-settings`) e o conteúdo JSON ou texto que precisa persistir. Como 30078 é substituível e delimitado pela tag `d`, atualizar o estado armazenado significa publicar um novo evento com a mesma tag `d`; o relay retém apenas a versão mais recente.

## Sincronização entre dispositivos

Qualquer cliente que conheça a chave pública de um usuário e a tag `d` da aplicação pode buscar o estado atual do conjunto de relays do usuário e reconstruí-lo em qualquer dispositivo. O usuário possui os dados porque eles vivem em eventos assinados pelo seu par de chaves, armazenados em relays da sua lista de relays [NIP-65](/pt/topics/nip-65/).

## Dados privados vs. públicos

Para dados de aplicação privados, o campo de conteúdo pode ser criptografado usando [NIP-44](/pt/topics/nip-44/) antes da publicação, para que o relay armazene apenas texto cifrado que somente o detentor da chave pode descriptografar. Dados de aplicação públicos podem ser armazenados sem criptografia para que outros clientes possam lê-los e exibi-los.

## Formato do conteúdo

NIP-78 deixa deliberadamente o formato do conteúdo em aberto; as aplicações escolhem seu próprio esquema. A convenção comum é prefixar as tags `d` com o nome da aplicação para evitar colisões entre apps que usam o mesmo relay.

## Implementações

- [Tamagostrich](https://github.com/Negr087/tamagostrich) — sincronização de estado de animal de estimação entre dispositivos via eventos `tamagostrich-pet-state` kind:30078
- [Wisp](https://github.com/barrydeen/wisp-android) — backup de carteira kind:30078 e sincronização de configurações de segurança entre dispositivos; assinaturas outbox mescladas em um único REQ usando filtro de autor NIP-78
- [NosPress](https://github.com/nostrapps/nospress) — estado de orquestração CMS armazenado em eventos NIP-78
- Várias implementações de sincronização de configurações de clientes Nostr (Amethyst, outros)

---

**Fontes primárias:**
- [Especificação NIP-78](https://github.com/nostr-protocol/nips/blob/master/78.md)
- [Tamagostrich](https://github.com/Negr087/tamagostrich) — implementação em produção

**Mencionado em:**
- [Newsletter #22: NIP-78 Deep Dive](/pt/newsletters/2026-05-14-newsletter/#nip-deep-dive-nip-78-app-specific-data)
- [Newsletter #22: Tamagostrich](/pt/newsletters/2026-05-14-newsletter/#tamagostrich-launches-a-decentralized-nip-78-tamagotchi-with-sats-rewards)

**Veja também:**
- [NIP-51: Listas](/pt/topics/nip-51/)
- [NIP-44: Criptografia com versão](/pt/topics/nip-44/)
- [NIP-65: Metadados de lista de relays](/pt/topics/nip-65/)
