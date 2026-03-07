---
title: FROST (Assinaturas de Limite Schnorr Otimizadas para Rodadas Flexíveis)
date: 2025-12-31
draft: false
categories:
- Cryptography
- Protocol
translationOf: /en/topics/frost.md
translationDate: '2026-03-07'
---

FROST (Flexible Round-Optimized Schnorr Threshold Signatures) é um esquema de assinatura de limite que permite que um grupo produza uma assinatura Schnorr válida sem que nenhum participante possua a chave privada completa.

## Como funciona

FROST permite assinatura T-of-N. Qualquer conjunto limite de participantes pode cooperar para produzir uma assinatura para a chave pública do grupo.

O protocolo de assinatura usa duas rodadas:

1. **Rodada de Compromisso**: Cada participante gera e compartilha compromissos criptográficos
2. **Rodada de Assinaturas**: Os participantes combinam suas assinaturas parciais em uma assinatura agregada final

A saída final é verificada como uma assinatura Schnorr comum. Os verificadores veem uma assinatura sob uma chave pública, não uma lista de fiadores.

## Notas de segurança

O manuseio do Nonce é crítico. A RFC é explícita que a assinatura de nonces é de uso único. A reutilização pode vazar material chave.

A RFC também não padroniza a geração distribuída de chaves. Ele especifica o próprio protocolo de assinatura e inclui a geração de chaves de revendedor confiável apenas como um apêndice. Na prática, a segurança de uma implantação FROST depende tanto do fluxo de assinatura quanto de como os compartilhamentos foram criados e armazenados.

## Casos de uso no Nostr

No contexto do Nostr, a FROST pode apoiar:

- **Governança de Quorum**: os grupos podem compartilhar um nsec por meio de esquemas T-of-N, onde os membros podem se representar ou delegar em conselhos
- **Administração multi-sig**: moderação da comunidade que requer múltiplas assinaturas de administrador
- **Gerenciamento descentralizado de chaves**: distribuição de confiança entre várias partes para operações críticas

## Status

FROST é especificado em [RFC 9591](https://datatracker.ietf.org/doc/rfc9591/), publicado no fluxo IRTF em junho de 2024. Isso dá ao protocolo uma especificação pública estável, mas não é um RFC de rastreamento de padrões IETF.

---

**Fontes primárias:**
- [RFC 9591: Protocolo FROST](https://datatracker.ietf.org/doc/rfc9591/)
- [Papel FROST (IACR)](https://eprint.iacr.org/2020/852.pdf)
- [Implementação de ferrugem da Fundação Zcash](https://github.com/ZcashFoundation/frost)

**Mencionado em:**
- [Boletim informativo nº 3: Repositório NIPs](/pt/newsletters/2025-12-31-newsletter/#nips-repository)
- [Boletim informativo nº 8](/pt/newsletters/2026-02-04-newsletter/)
- [Boletim informativo nº 10](/pt/newsletters/2026-02-18-newsletter/)

**Veja também:**
- [NIP-46: Nostr Connect](/pt/topics/nip-46/)
- [NIP-55: Aplicativo de Assinante Android](/pt/topics/nip-55/)
