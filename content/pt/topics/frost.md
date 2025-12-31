---
title: "FROST (Flexible Round-Optimized Schnorr Threshold Signatures)"
date: 2025-12-31
translationOf: /en/topics/frost.md
translationDate: 2025-12-31
draft: false
categories:
  - Criptografia
  - Protocolo
---

FROST (Flexible Round-Optimized Schnorr Threshold Signatures) é um esquema de assinaturas de limiar que permite a um grupo de participantes produzir colaborativamente assinaturas Schnorr válidas sem que nenhuma parte individual possua a chave privada completa.

## Como funciona

FROST permite assinatura de limiar T-de-N, onde T participantes de um total de N detentores de chaves devem cooperar para produzir uma assinatura válida. O protocolo opera em duas rodadas:

1. **Rodada de compromisso**: Cada participante gera e compartilha compromissos criptográficos
2. **Rodada de assinatura**: Os participantes combinam suas assinaturas parciais em uma assinatura agregada final

A assinatura resultante é indistinguível de uma assinatura Schnorr padrão, mantendo compatibilidade retroativa com os sistemas de verificação existentes.

## Propriedades principais

- **Segurança de limiar**: Nenhum participante individual pode assinar sozinho; T partes devem cooperar
- **Eficiência de rodadas**: Apenas duas rodadas de comunicação são necessárias para assinar
- **Proteção contra falsificação**: Técnicas inovadoras protegem contra ataques a esquemas de limiar anteriores
- **Agregação de assinaturas**: Múltiplas assinaturas se combinam em uma única assinatura compacta
- **Privacidade**: As assinaturas finais não revelam quais T participantes assinaram

## Casos de uso no Nostr

No contexto do Nostr, FROST permite:

- **Governança por quórum**: Grupos podem compartilhar um nsec através de esquemas T-de-N, onde membros podem se representar ou delegar a conselhos
- **Administração multi-assinatura**: Moderação comunitária exigindo múltiplas assinaturas de administradores
- **Gestão descentralizada de chaves**: Distribuição de confiança entre múltiplas partes para operações críticas

## Padronização

FROST foi padronizado como RFC 9591 em junho de 2024, intitulado "The Flexible Round-Optimized Schnorr Threshold (FROST) Protocol for Two-Round Schnorr Signatures".

---

**Fontes principais:**
- [RFC 9591: FROST Protocol](https://datatracker.ietf.org/doc/rfc9591/)
- [FROST Paper (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [University of Waterloo CrySP](https://crysp.uwaterloo.ca/software/frost/)
- [Zcash Foundation Rust Implementation](https://github.com/ZcashFoundation/frost)

**Mencionado em:**
- [Newsletter #3: Repositório de NIPs](/pt/newsletters/2025-12-31-newsletter/#nips-repository)

**Veja também:**
- [Proposta NIP-XX Quorum](https://github.com/nostr-protocol/nips/pull/2179)
