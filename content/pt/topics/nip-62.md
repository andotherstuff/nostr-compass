---
title: 'NIP-62: Vanish Requests'
date: 2026-01-13
draft: false
categories:
  - Privacy
  - Protocol
translationOf: /en/topics/nip-62.md
translationDate: 2026-04-22
---

NIP-62 define vanish requests, eventos kind `62` que pedem a relays específicos que apaguem todos os eventos da pubkey solicitante. O request é direcionado ao relay por padrão, e também pode ser transmitido como um request global usando o valor especial de tag `ALL_RELAYS`.

## Como funciona

Um vanish request é um evento kind `62` assinado pela pubkey que quer seu histórico removido. A lista de tags precisa incluir pelo menos um valor `relay` nomeando o relay que deve agir sobre o pedido.

```json
{
  "id": "a7b8c9d0e1f23456789012345678901234567890abcdef1234567890abcdef12",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1743465600,
  "kind": 62,
  "tags": [
    ["relay", "wss://relay.example.com"]
  ],
  "content": "Requesting deletion of all events from this relay.",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

O campo `content` pode incluir um motivo ou aviso legal ao operador do relay. Clientes devem enviar o evento diretamente aos relays alvo em vez de publicá-lo amplamente, a menos que o usuário pretenda fazer um vanish request para toda a rede.

## Comportamento do relay

Relays que veem um vanish request e encontram sua própria service URL em uma tag `relay` precisam apagar completamente quaisquer eventos daquela pubkey até o `created_at` do request. A spec também diz que relays devem apagar eventos [NIP-59](/pt/topics/nip-59/) que tenham uma tag `p` apontando para a pubkey desaparecida, para que DMs recebidas sejam removidas junto dos eventos do próprio usuário.

O relay também precisa garantir que esses eventos apagados não possam ser retransmitidos de volta para o relay. Ele pode manter o vanish request assinado para fins de registro.

## Requests globais

Para solicitar apagamento em todo relay que vir o evento, o valor da tag passa a ser `ALL_RELAYS`, em maiúsculas:

```json
{
  "kind": 62,
  "pubkey": "<32-byte-hex-pubkey>",
  "tags": [
    ["relay", "ALL_RELAYS"]
  ],
  "content": "Global vanish request"
}
```

Clientes devem transmitir essa forma para o maior número possível de relays.

## Por que importa

NIP-62 dá a clientes e operadores de relay um sinal compartilhado de exclusão que vai além de APIs de moderação ad hoc ou dashboards específicos de relay. Um usuário pode publicar um request assinado e deixar cada relay processá-lo com o mesmo formato de evento.

Ela também vai além da [NIP-09](/pt/topics/nip-09/). NIP-09 apaga eventos individuais e relays podem cumprir. NIP-62 pede a relays tagueados que apaguem tudo daquela pubkey e impeçam que esses eventos sejam reimportados.

## Implementações

- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - suporte a vanish request do lado do cliente
- [rust-nostr PR #1315](https://github.com/rust-nostr/nostr/pull/1315) - suporte no backend de memória
- [rust-nostr PR #1316](https://github.com/rust-nostr/nostr/pull/1316) - suporte no backend LMDB
- [rust-nostr PR #1317](https://github.com/rust-nostr/nostr/pull/1317) - suporte no backend SQLite
- [rust-nostr PR #1318](https://github.com/rust-nostr/nostr/pull/1318) - cobertura de testes de banco para suporte a vanish específico por relay
- [nostream PR #544](https://github.com/Cameri/nostream/pull/544) - adiciona right-to-vanish NIP-62 à lista de features anunciadas

---

**Fontes primárias:**
- [Especificação NIP-62](https://github.com/nostr-protocol/nips/blob/master/62.md)
- [Amethyst v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) - suporte a vanish do lado do cliente
- [rust-nostr PR #1315](https://github.com/rust-nostr/nostr/pull/1315)
- [rust-nostr PR #1316](https://github.com/rust-nostr/nostr/pull/1316)
- [rust-nostr PR #1317](https://github.com/rust-nostr/nostr/pull/1317)
- [rust-nostr PR #1318](https://github.com/rust-nostr/nostr/pull/1318)
- [nostream PR #544](https://github.com/Cameri/nostream/pull/544)

**Mencionado em:**
- [Newsletter #5: Mudancas notaveis no codigo](/pt/newsletters/2026-01-13-newsletter/)
- [Newsletter #12: rust-nostr](/pt/newsletters/2026-03-04-newsletter/)
- [Newsletter #16: Amethyst lanca suporte a NIP-62](/pt/newsletters/2026-04-01-newsletter/)
- [Newsletter #16: NIP Deep Dive](/pt/newsletters/2026-04-01-newsletter/)
- [Newsletter #19: suporte a NIP-62 no nostream](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-09: Request de exclusão de evento](/pt/topics/nip-09/)
- [NIP-17: Mensagens Diretas Privadas](/pt/topics/nip-17/)
- [NIP-59: Gift Wrap](/pt/topics/nip-59/)
