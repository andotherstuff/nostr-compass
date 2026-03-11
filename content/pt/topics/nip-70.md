---
title: 'NIP-70: Eventos Protegidos'
date: 2026-03-11
translationOf: /en/topics/nip-70.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Relay
  - Access Control
---

O NIP-70 define uma forma de autores marcarem um evento como protegido com a tag simples `[["-"]]`. Um evento protegido só pode ser aceito quando um relay escolhe suportar esse comportamento e verifica que o publicador autenticado é a mesma pubkey do autor do evento.

## Como funciona

A regra central é curta. Se um evento contém a tag `[["-"]]`, um relay deve rejeitá-lo por padrão. Um relay que queira suportar eventos protegidos deve primeiro executar o fluxo `AUTH` do [NIP-42](/pt/topics/nip-42/) e confirmar que o cliente autenticado está publicando o próprio evento.

Isso faz do NIP-70 uma regra de autoridade de publicação, não uma regra de criptografia. O conteúdo ainda pode ser legível. O que muda é quem pode colocar esse evento em um relay que respeita a tag. Isso permite que relays suportem feeds semi-fechados e outros contextos em que autores querem que um relay se recuse a republicações de terceiros.

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

## Implicações do fluxo AUTH

Eventos protegidos só são úteis quando relays realmente aplicam a identidade do autor no momento da publicação. É por isso que o NIP-70 depende tão diretamente do [NIP-42](/pt/topics/nip-42/). Um relay que aceita eventos `[["-"]]` sem uma verificação de auth correspondente está tratando a tag como decoração, não como política.

## Comportamento do relay e limites

O NIP-70 não promete que o conteúdo ficará contido para sempre. Qualquer destinatário ainda pode copiar o que vê e publicar um novo evento em outro lugar. A especificação só dá aos relays uma maneira padronizada de respeitar a intenção do autor e rejeitar a republicação direta de eventos protegidos.

É por isso que o trabalho de acompanhamento importa. O [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) estende a regra para reposts que incorporam eventos protegidos, fechando um bypass fácil em que o evento original permanecia protegido, mas o evento de encapsulamento não.

## Implementações

- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - Adiciona suporte de auth NIP-42 para eventos protegidos
- [strfry PR #176](https://github.com/hoytech/strfry/pull/176) - Rejeita reposts que incorporam eventos protegidos
- [SNSTR v0.3.3](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.3) - Adiciona suporte auxiliar ligado ao tratamento de eventos protegidos

---

**Fontes primárias:**
- [Especificação do NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md)
- [PR #1030](https://github.com/nostr-protocol/nips/pull/1030) - Adicionou o NIP-70 ao repositório de NIPs
- [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) - Rejeita reposts que incorporam eventos protegidos
- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - Implementação de relay para auth NIP-42 e eventos protegidos

**Mencionado em:**
- [Newsletter #13: Atualizações de NIP](/pt/newsletters/2026-03-11-newsletter/)
- [Newsletter #13: Aprofundamento NIP](/pt/newsletters/2026-03-11-newsletter/)

**Veja também:**
- [NIP-42: Autenticação de Cliente](/pt/topics/nip-42/)
- [NIP-11: Documento de Informações do Relay](/pt/topics/nip-11/)
