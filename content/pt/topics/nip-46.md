---
title: 'NIP-46: Nostr Connect'
date: 2025-12-17
draft: false
categories:
  - Signing
  - Protocol
translationOf: /en/topics/nip-46.md
translationDate: 2026-04-22
---

NIP-46 define assinatura remota sobre relays Nostr. Um cliente conversa com um signer separado, frequentemente chamado de bunker, para que as chaves de assinatura possam ficar fora do app que o usuário está usando ativamente.

## Como funciona

1. O cliente gera um keypair local usado apenas para a sessão bunker.
2. A conexão é estabelecida com uma URI `bunker://` ou `nostrconnect://`.
3. Cliente e signer trocam eventos criptografados kind `24133` de request e response por meio de relays.
4. Depois de conectar, o cliente chama `get_public_key` para descobrir a pubkey real do usuário para quem está assinando.

## Métodos de conexão

- **bunker://** - conexão iniciada pelo signer
- **nostrconnect://** - conexão iniciada pelo cliente via QR code ou deep link

Fluxos `nostrconnect://` incluem um shared secret obrigatório para que o cliente possa verificar que a primeira response realmente veio do signer pretendido. Isso evita spoofing simples de conexão.

## Operações suportadas

- `sign_event` - assinar um evento arbitrário
- `get_public_key` - recuperar a pubkey do usuário a partir do signer
- `nip04_encrypt/decrypt` - operações de criptografia NIP-04
- `nip44_encrypt/decrypt` - operações de criptografia NIP-44
- `switch_relays` - pedir ao signer um conjunto atualizado de relays

Muitas implementações também usam strings de permissão como `sign_event:1` ou `nip44_encrypt` durante a configuração, para que o signer possa aprovar um escopo estreito em vez de acesso total.

## Modelo de relay e confiança

NIP-46 tira as chaves privadas do cliente, mas não remove confiança do signer. O signer pode aprovar, negar ou atrasar requests, e vê toda operação que o cliente lhe pede para executar. A escolha de relay também importa porque o protocolo depende de entrega de request e response por relays que ambos os lados conseguem alcançar.

O método `switch_relays` existe para que o signer possa mover a sessão para um conjunto diferente de relays ao longo do tempo. Clientes que o ignoram funcionarão com menos confiabilidade quando as preferências de relay do signer mudarem.

---

**Fontes primárias:**
- [Especificação NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md)

**Mencionado em:**
- [Newsletter #1: Mudancas notaveis no codigo](/pt/newsletters/2025-12-17-newsletter/)
- [Newsletter #3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/)
- [Newsletter #4: Primal Android vira um hub de assinatura completo](/pt/newsletters/2026-01-07-newsletter/)
- [Newsletter #12: NDK Collaborative Events and NIP-46 Timeout](/pt/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: suporte a signer no NipLock](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: signer Heartwood da Forgesworn](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: login NIP-46 com Aegis no Flotilla](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-55: Android Signer](/pt/topics/nip-55/)
