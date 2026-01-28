---
title: "NIP-07: Signatário de Extensão de Navegador"
date: 2026-01-28
translationOf: /en/topics/nip-07.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Signing
  - Security
---

NIP-07 define uma interface padrão para extensões de navegador fornecerem capacidades de assinatura para clientes Nostr baseados em web, mantendo chaves privadas seguras na extensão em vez de expô-las a websites.

## Como Funciona

Extensões de navegador injetam um objeto `window.nostr` que aplicativos web podem usar:

```javascript
// Obter chave pública
const pubkey = await window.nostr.getPublicKey();

// Assinar um evento
const signedEvent = await window.nostr.signEvent(unsignedEvent);

// Criptografar (NIP-04, legado)
const ciphertext = await window.nostr.nip04.encrypt(pubkey, plaintext);

// Descriptografar (NIP-04, legado)
const plaintext = await window.nostr.nip04.decrypt(pubkey, ciphertext);

// Métodos NIP-44 (moderno, se suportado)
// const ciphertext = await window.nostr.nip44.encrypt(pubkey, plaintext);
// const plaintext = await window.nostr.nip44.decrypt(pubkey, ciphertext);
```

## Modelo de Segurança

- **Isolamento de Chave**: Chaves privadas nunca deixam a extensão
- **Aprovação do Usuário**: Extensões podem solicitar confirmação para cada pedido de assinatura
- **Controle de Domínio**: Extensões podem restringir quais sites podem solicitar assinaturas

## Implementações

Extensões NIP-07 populares incluem:
- **Alby** - Carteira Lightning com assinatura Nostr
- **nos2x** - Signatário Nostr leve
- **Flamingo** - Extensão Nostr rica em recursos

## Limitações

- Apenas navegador (sem suporte móvel)
- Requer instalação de extensão
- Cada extensão tem UX diferente para aprovações

## Alternativas

- [NIP-46](/pt/topics/nip-46/) - Assinatura remota via relays Nostr
- [NIP-55](/pt/topics/nip-55/) - Signatário local Android

## Relacionados

- [NIP-44](/pt/topics/nip-44/) - Criptografia moderna (substituindo NIP-04)
- [NIP-46](/pt/topics/nip-46/) - Assinatura Remota
