---
title: 'NIP-55: Aplicativo de Assinante Android'
date: 2025-12-17
draft: false
categories:
- Signing
- Mobile
translationOf: /en/topics/nip-55.md
translationDate: 2026-03-11
---

O NIP-55 define como os aplicativos Android solicitam operações de assinatura e criptografia de um aplicativo assinante separado. Oferece aos clientes Android uma alternativa nativa para extensões de navegador e bunkers remotos.

## Como funciona

O NIP-55 usa dois mecanismos Android:

- **Intents** para fluxos em primeiro plano com aprovação explícita do usuário
- **Resolvedores de conteúdo** para fluxos em segundo plano depois que o usuário concede permissão persistente

O fluxo de conexão normal começa com `get_public_key`. O signatário retorna o usuário pubkey e o nome do pacote do signatário, e espera-se que o cliente armazene ambos em cache. Repetir `get_public_key` em loops de segundo plano é um erro de implementação comum contra o qual a especificação alerta explicitamente.

## Principais operações

- **get_public_key** - Recupera o pubkey do usuário e o nome do pacote do assinante
- **sign_event** - Assine um evento Nostr
- **nip04_encrypt/decrypt** - Criptografa ou descriptografa mensagens NIP-04
- **nip44_encrypt/decrypt** - Criptografa ou descriptografa mensagens NIP-44
- **decrypt_zap_event** - Descriptografar evento relacionado ao zap payloads

## Notas de segurança e UX

O NIP-55 mantém as chaves no dispositivo, mas ainda depende dos limites do aplicativo Android e do tratamento de permissões do assinante. O suporte ao resolvedor de conteúdo oferece uma experiência do usuário muito mais suave do que solicitações repetidas de intenção, mas somente depois que o usuário concede aprovação durável a esse cliente.

Para aplicativos da web no Android, o NIP-55 é menos ergonômico que o NIP-46. Os fluxos baseados em navegador não podem receber respostas diretas em segundo plano da mesma forma que os aplicativos Android nativos, portanto, muitas implementações recorrem a URLs de retorno de chamada, transferência da área de transferência ou colagem manual.

---

**Fontes primárias:**
- [Especificação NIP-55](https://github.com/nostr-protocol/nips/blob/master/55.md)

**Mencionado em:**
- [Boletim Informativo nº 1: Lançamentos](/pt/newsletters/2025-12-17-newsletter/#releases)
- [Boletim informativo nº 2: Notícias](/pt/newsletters/2025-12-24-newsletter/#news)
- [Boletim informativo nº 2: Atualizações do NIP](/pt/newsletters/2025-12-24-newsletter/#nip-updates)
- [Boletim informativo nº 3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Boletim informativo nº 7: Atualizações do NIP](/pt/newsletters/2026-01-07-newsletter/#nip-updates)
- [Boletim informativo nº 11: Aprofundamento do NIP](/pt/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-55-android-signer-application)

**Veja também:**
- [NIP-46: Nostr Connect](/pt/topics/nip-46/)
