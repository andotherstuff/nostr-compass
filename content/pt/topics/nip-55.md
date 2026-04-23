---
title: 'NIP-55: Android Signer Application'
date: 2025-12-17
draft: false
categories:
  - Signing
  - Mobile
translationOf: /en/topics/nip-55.md
translationDate: 2026-04-22
---

NIP-55 define como apps Android pedem operações de assinatura e criptografia a uma signer application separada. Ela dá a clientes Android uma alternativa nativa a extensões de navegador e bunkers remotos.

## Como funciona

A NIP-55 usa dois mecanismos do Android:

- **Intents** para fluxos em foreground com aprovação explícita do usuário
- **Content resolvers** para fluxos em background depois que o usuário concede permissão persistente

O fluxo de conexão usual começa com `get_public_key`. O signer retorna tanto a pubkey do usuário quanto o nome do pacote do signer, e o cliente deve armazenar ambos em cache. Repetir `get_public_key` em loops de background é um erro comum de implementação que a spec alerta explicitamente para evitar.

## Operações principais

- **get_public_key** - recupera a pubkey do usuário e o nome do pacote do signer
- **sign_event** - assina um evento Nostr
- **nip04_encrypt/decrypt** - criptografa ou descriptografa mensagens NIP-04
- **nip44_encrypt/decrypt** - criptografa ou descriptografa mensagens NIP-44
- **decrypt_zap_event** - descriptografa payloads de eventos relacionados a zap

## Notas de segurança e UX

A NIP-55 mantém as chaves no dispositivo, mas ainda depende dos limites entre apps do Android e do tratamento de permissões do signer. O suporte a content resolver oferece uma UX muito mais suave do que prompts repetidos com intent, mas somente depois que o usuário concedeu aprovação durável àquele cliente.

Para apps web no Android, a NIP-55 é menos ergonômica do que a NIP-46. Fluxos baseados em navegador não conseguem receber responses diretas em background da mesma forma que apps Android nativos conseguem, então muitas implementações recorrem a callback URLs, transferência por clipboard ou colagem manual.

---

**Fontes primárias:**
- [Especificação NIP-55](https://github.com/nostr-protocol/nips/blob/master/55.md)

**Mencionado em:**
- [Newsletter #1: Lançamentos](/pt/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: Notícias](/pt/newsletters/2025-12-24-newsletter/)
- [Newsletter #2: Atualizações de NIP](/pt/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/)
- [Newsletter #4: Atualizações de NIP](/pt/newsletters/2026-01-07-newsletter/)
- [Newsletter #11: NIP Deep Dive](/pt/newsletters/2026-02-25-newsletter/)
- [Newsletter #13: Samizdat v1.0.0-alpha](/en/newsletters/2026-03-11-newsletter/)

**Veja também:**
- [NIP-46: Nostr Connect](/pt/topics/nip-46/)
