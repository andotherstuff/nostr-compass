---
title: 'NIP-07: Signatário da extensão do navegador'
date: 2026-01-28
draft: false
categories:
- NIP
- Signing
- Security
translationOf: /en/topics/nip-07.md
translationDate: '2026-03-07'
---

O NIP-07 define uma interface padrão para extensões de navegador para fornecer recursos de assinatura para clientes Nostr baseados na web, mantendo as chaves privadas seguras na extensão em vez de expô-las a sites.

## Como funciona

As extensões do navegador injetam um objeto `window.nostr` que os aplicativos da web podem usar:

```javascript
// Get public key
const pubkey = await window.nostr.getPublicKey();

// Sign an event
const signedEvent = await window.nostr.signEvent(unsignedEvent);

// Encrypt (NIP-04, legacy)
const ciphertext = await window.nostr.nip04.encrypt(pubkey, plaintext);

// Decrypt (NIP-04, legacy)
const plaintext = await window.nostr.nip04.decrypt(pubkey, ciphertext);

// NIP-44 methods (modern, if supported)
// const ciphertext = await window.nostr.nip44.encrypt(pubkey, plaintext);
// const plaintext = await window.nostr.nip44.decrypt(pubkey, ciphertext);
```

## Modelo de segurança

- **Isolamento de chave**: as chaves privadas nunca saem da extensão
- **Aprovação do usuário**: as extensões podem solicitar cada solicitação de assinatura
- **Controle de domínio**: as extensões podem restringir quais sites podem solicitar assinaturas

O NIP-07 melhora a custódia das chaves, mas não remove a confiança da própria extensão. Uma extensão mal-intencionada ou comprometida ainda pode assinar algo errado, vazar metadados ou conceder permissões de maneira muito ampla.

## Notas de interoperabilidade

A parte mais difícil do NIP-07 não é o formato da API. É variação de capacidade. Algumas extensões suportam apenas `getPublicKey()` e `signEvent()`. Outros também expõem `nip04`, `nip44` ou métodos opcionais mais recentes. Os aplicativos da Web precisam de detecção de recursos e alternativas razoáveis, em vez de assumir que cada signatário injetado se comporta da mesma maneira.

A UX de aprovação do usuário também muda o comportamento. Um site que espera silenciosamente acesso em segundo plano pode funcionar com uma extensão e parecer quebrado com outra que solicita cada solicitação. Bons aplicativos NIP-07 tratam a assinatura como um limite de permissão interativo.

## Status de implementação

As extensões NIP-07 populares incluem:
- **Alby** – Carteira Lightning com assinatura Nostr
- **nos2x** - Assinante leve do Nostr
- **Flamingo** - Extensão Nostr rica em recursos

## Limitações

- Somente navegador (sem suporte móvel)
- Requer instalação de extensão
- Cada extensão possui UX diferente para aprovações

Para assinatura entre dispositivos ou dispositivos móveis, o NIP-46 e o ​​NIP-55 geralmente são mais adequados.

---

**Fontes primárias:**
- [Especificação NIP-07](https://github.com/nostr-protocol/nips/blob/master/07.md)
- [PR #2233](https://github.com/nostr-protocol/nips/pull/2233) - Proposta `peekPublicKey()`

**Mencionado em:**
- [Boletim informativo nº 7: Atualizações do NIP](/pt/newsletters/2026-01-28-newsletter/#nip-updates)
- [Boletim informativo nº 8: Notícias](/pt/newsletters/2026-02-04-newsletter/#news)
- [Boletim informativo nº 11: Notícias](/pt/newsletters/2026-02-25-newsletter/#news)

**Veja também:**
- [NIP-04: Mensagens diretas criptografadas (obsoletas)](/pt/topics/nip-04/)
- [NIP-44: cargas criptografadas](/pt/topics/nip-44/)
- [NIP-46: Conexão Nostr](/pt/topics/nip-46/)
- [NIP-55: aplicativos de signatário Android](/pt/topics/nip-55/)
