---
title: "NIP-46: Nostr Connect"
date: 2025-12-17
draft: false
categories:
  - Signing
  - Protocol
translationOf: /en/topics/nip-46.md
translationDate: 2025-12-26
---

NIP-46 define assinatura remota, permitindo que uma aplicação de assinatura mantenha as chaves enquanto clientes solicitam assinaturas através de relays Nostr.

## Como Funciona

1. O assinador gera uma URI de conexão (`bunker://` ou `nostrconnect://`)
2. O usuário cola a URI em um cliente
3. O cliente envia solicitações de assinatura como eventos criptografados para o relay do assinador
4. O assinador solicita aprovação do usuário, retorna eventos assinados

## Métodos de Conexão

- **bunker://** - Conexão iniciada pelo assinador
- **nostrconnect://** - Conexão iniciada pelo cliente via QR code ou deep link

## Operações Suportadas

- `sign_event` - Assinar um evento arbitrário
- `get_public_key` - Recuperar a chave pública do assinador
- `nip04_encrypt/decrypt` - Operações de criptografia NIP-04
- `nip44_encrypt/decrypt` - Operações de criptografia NIP-44

---

**Fontes primárias:**
- [Especificação NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md)

**Mencionado em:**
- [Newsletter #1: Mudanças de Código Notáveis](/pt/newsletters/2025-12-17-newsletter/#amethyst-android)

**Veja também:**
- [NIP-55: Assinador Android](/pt/topics/nip-55/)
