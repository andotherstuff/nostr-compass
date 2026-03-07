---
title: 'NIP-44: cargas criptografadas'
date: 2025-12-31
draft: false
categories:
- NIP
- Cryptography
- Privacy
translationOf: /en/topics/nip-44.md
translationDate: '2026-03-07'
---

NIP-44 define um padrão de criptografia versionado para Nostr payloads, substituindo o esquema de criptografia falho NIP-04 por primitivas criptográficas modernas.

## Como funciona

O NIP-44 versão 2 usa um processo de criptografia em várias etapas:

1. **Acordo de Chave**: ECDH (secp256k1) entre as chaves públicas do remetente e do destinatário produz um segredo compartilhado
2. **Derivação de chave**: extração HKDF com SHA256 e salt `nip44-v2` cria uma chave de conversa
3. **Chaves por mensagem**: HKDF-expand deriva chave ChaCha, nonce e chave HMAC de um nonce aleatório
4. **Preenchimento**: o conteúdo é preenchido para ocultar o comprimento da mensagem
5. **Criptografia**: ChaCha20 criptografa o conteúdo preenchido
6. **Autenticação**: HMAC-SHA256 fornece integridade de mensagem

A saída é um payload base64 versionado que entra em um evento Nostr normal assinado. A especificação exige que os clientes validem a assinatura do evento NIP-01 externo antes de descriptografar o NIP-44 payload interno.

## Escolhas criptográficas

- **ChaCha20** sobre AES: resistência a ataques multi-teclas mais rápida e melhor
- **HMAC-SHA256** sobre Poly1305: MACs polinomiais são mais fáceis de falsificar
- **SHA256**: Consistente com as primitivas Nostr existentes
- **Formato versionado**: permite atualizações futuras de algoritmos

## Propriedades de segurança

- **Criptografia autenticada**: as mensagens não podem ser adulteradas
- **Ocultação do comprimento**: o preenchimento obscurece o tamanho da mensagem
- **Chaves de conversação**: a mesma chave para conversas contínuas reduz o cálculo
- **Auditado**: a auditoria de segurança Cure53 não encontrou vulnerabilidades exploráveis

## Notas de implementação

O NIP-44 não é um substituto imediato para o NIP-04 payloads. Ele define um formato de criptografia, não um evento de mensagem direta kind. Protocolos como [NIP-17](/pt/topics/nip-17/) e [NIP-59](/pt/topics/nip-59/) definem como payloads criptografados são usados ​​em fluxos de mensagens reais.

A entrada de texto simples é texto UTF-8 com comprimento de 1 a 65.535 bytes. Essa é uma restrição real para os implementadores: se seu aplicativo precisar criptografar blobs binários arbitrários, você precisará de uma codificação adicional ou de um formato de contêiner diferente.

## Limitações

O NIP-44 não fornece:
- **Sigilo de encaminhamento**: chaves comprometidas expõem mensagens anteriores
- **Segurança pós-comprometimento**: recuperação após comprometimento de chave
- **Negabilidade**: as mensagens são comprovadamente assinadas por chaves específicas
- **Ocultação de metadados**: a arquitetura de relay limita a privacidade

Para necessidades de alta segurança, protocolos NIP-104 (catraca dupla) ou baseados em MLS como Marmot oferecem garantias mais fortes.

## História

A revisão 3 do NIP-44 foi fundida em dezembro de 2023 após uma auditoria de segurança independente Cure53. Ele forma a base criptográfica para DMs privados NIP-17 e embalagens de presente NIP-59.

---

**Fontes primárias:**
- [Especificação NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [Implementações de referência NIP-44](https://github.com/paulmillr/nip44)
- [Relatório de auditoria Cure53](https://cure53.de/audit-report_nip44-implementations.pdf)

**Mencionado em:**
- [Boletim informativo nº 4: Aprofundamento do NIP](/pt/newsletters/2026-01-07-newsletter/#nip-44-versioned-encryption)
- [Boletim informativo nº 3: dezembro de 2023](/pt/newsletters/2025-12-31-newsletter/#december-2023-ecosystem-maturation)
- [Boletim informativo nº 3: dezembro de 2024](/pt/newsletters/2025-12-31-newsletter/#december-2024-protocol-advancement)
- [Boletim Informativo nº 12: Marmot](/pt/newsletters/2026-03-04-newsletter/#marmot-development-kit-ships-first-public-release)

**Veja também:**
- [NIP-04: Mensagens diretas criptografadas (obsoleto)](/pt/topics/nip-04/)
- [NIP-17: Mensagens Diretas Privadas](/pt/topics/nip-17/)
- [NIP-59: Gift Wrap](/pt/topics/nip-59/)
- [NIP-104: criptografia de catraca dupla](/pt/topics/nip-104/)
- [MLS: Message Layer Security](/pt/topics/mls/)
