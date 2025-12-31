---
title: "NIP-44: Encrypted Payloads"
date: 2025-12-31
translationOf: /en/topics/nip-44.md
translationDate: 2025-12-31
draft: false
categories:
  - NIP
  - Criptografia
  - Privacidade
---

NIP-44 define um padrão de criptografia versionado para payloads do Nostr, substituindo o esquema de criptografia falho do NIP-04 com primitivas criptográficas modernas.

## Como Funciona

NIP-44 versão 2 usa um processo de criptografia de múltiplas etapas:

1. **Acordo de Chaves**: ECDH (secp256k1) entre as chaves públicas do remetente e destinatário produz um segredo compartilhado
2. **Derivação de Chaves**: HKDF-extract com SHA256 e salt `nip44-v2` cria uma chave de conversa
3. **Chaves Por Mensagem**: HKDF-expand deriva a chave ChaCha, nonce e chave HMAC de um nonce aleatório
4. **Preenchimento**: O conteúdo é preenchido para ocultar o tamanho da mensagem
5. **Criptografia**: ChaCha20 criptografa o conteúdo preenchido
6. **Autenticação**: HMAC-SHA256 fornece integridade da mensagem

## Escolhas Criptográficas

- **ChaCha20** sobre AES: Mais rápido, melhor resistência a ataques multi-chave
- **HMAC-SHA256** sobre Poly1305: MACs polinomiais são mais fáceis de falsificar
- **SHA256**: Consistente com as primitivas existentes do Nostr
- **Formato Versionado**: Permite futuras atualizações de algoritmos

## Propriedades de Segurança

- **Criptografia Autenticada**: Mensagens não podem ser adulteradas
- **Ocultação de Tamanho**: Preenchimento obscurece o tamanho da mensagem
- **Chaves de Conversa**: Mesma chave para conversas contínuas reduz computação
- **Auditado**: Auditoria de segurança da Cure53 não encontrou vulnerabilidades exploráveis

## Limitações

NIP-44 não fornece:
- **Forward Secrecy**: Chaves comprometidas expõem mensagens passadas
- **Post-Compromise Security**: Recuperação após comprometimento de chaves
- **Negabilidade**: Mensagens são provavelmente assinadas por chaves específicas
- **Ocultação de Metadados**: Arquitetura de relays limita privacidade

Para necessidades de alta segurança, NIP-104 (double ratchet) ou protocolos baseados em MLS como Marmot oferecem garantias mais fortes.

## História

NIP-44 revisão 3 foi mesclado em dezembro de 2023 após uma auditoria de segurança independente da Cure53. Forma a base criptográfica para os DMs privados do NIP-17 e o gift wrapping do NIP-59.

---

**Fontes primárias:**
- [Especificação NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [Implementações de Referência NIP-44](https://github.com/paulmillr/nip44)
- [Relatório de Auditoria Cure53](https://cure53.de/audit-report_nip44-implementations.pdf)

**Mencionado em:**
- [Newsletter #3: Dezembro 2023](/pt/newsletters/2025-12-31-newsletter/#december-2023-ecosystem-maturation)
- [Newsletter #3: Dezembro 2024](/pt/newsletters/2025-12-31-newsletter/#december-2024-protocol-advancement)

**Veja também:**
- [NIP-04: Mensagens Diretas Criptografadas (obsoleto)](/pt/topics/nip-04/)
- [NIP-17: Mensagens Diretas Privadas](/pt/topics/nip-17/)
- [NIP-59: Gift Wrap](/pt/topics/nip-59/)
- [NIP-104: Criptografia Double Ratchet](/pt/topics/nip-104/)
- [MLS: Message Layer Security](/pt/topics/mls/)
