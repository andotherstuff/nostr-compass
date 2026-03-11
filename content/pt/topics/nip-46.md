---
title: 'NIP-46: Nostr Connect'
date: 2025-12-17
draft: false
categories:
- Signing
- Protocol
translationOf: /en/topics/nip-46.md
translationDate: 2026-03-11
---

NIP-46 define assinatura remota sobre Nostr relays. Um cliente se comunica com um assinante separado, geralmente chamado de bunker, portanto, a assinatura das chaves pode ficar fora do aplicativo que o usuário está usando ativamente.

## Como funciona

1. O cliente gera um par de chaves local usado apenas para a sessão do bunker.
2. A conexão é estabelecida com um URI `bunker://` ou `nostrconnect://`.
3. Cliente e signatário trocam eventos de solicitação e resposta criptografados kind `24133` por meio de relays.
4. Após a conexão, o cliente chama `get_public_key` para saber o usuário real pubkey para o qual está assinando.

## Métodos de conexão

- **bunker://** - Conexão iniciada pelo signatário
- **nostrconnect://** - Conexão iniciada pelo cliente via código QR ou link direto

Os fluxos `nostrconnect://` incluem um segredo compartilhado obrigatório para que o cliente possa verificar se a primeira resposta realmente veio do signatário pretendido. Isso evita a falsificação de conexão simples.

## Operações Suportadas

- `sign_event` - Assine um evento arbitrário
- `get_public_key` - Recupera o pubkey do usuário do signatário
- `nip04_encrypt/decrypt` - Operações de criptografia NIP-04
- `nip44_encrypt/decrypt` - operações de criptografia NIP-44
- `switch_relays` - Peça ao signatário um conjunto de relays atualizado

Muitas implementações também usam cadeias de permissão como `sign_event:1` ou `nip44_encrypt` durante a configuração para que o signatário possa aprovar um escopo restrito em vez de acesso total.

## Modelo de relay e confiança

O NIP-46 remove as chaves privadas do cliente, mas não remove a confiança do signatário. O signatário pode aprovar, negar ou atrasar solicitações e vê todas as operações que o cliente solicita que ele execute. A escolha do relay também é importante porque o protocolo depende da entrega de solicitação e resposta através de relays que ambos os lados podem alcançar.

O método `switch_relays` existe para que o signatário possa mover a sessão para um conjunto de relays diferente ao longo do tempo. Os clientes que o ignoram funcionarão de forma menos confiável quando as preferências do signatário relay mudarem.

---

**Fontes primárias:**
- [Especificação NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md)

**Mencionado em:**
- [Boletim informativo nº 1: Mudanças notáveis no código](/pt/newsletters/2025-12-17-newsletter/#amethyst-android)
- [Boletim informativo nº 3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Boletim informativo nº 7: Primal Android se torna um centro de assinatura completo](/pt/newsletters/2026-01-07-newsletter/#primal-android-becomes-a-full-signing-hub)
- [Boletim informativo nº 15: Eventos colaborativos NDK e tempo limite NIP-46](/pt/newsletters/2026-03-04-newsletter/#ndk-collaborative-events-and-nip-46-timeout)

**Veja também:**
- [NIP-55: Signatário do Android](/pt/topics/nip-55/)
