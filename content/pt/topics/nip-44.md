---
title: 'NIP-44: cargas criptografadas'
date: 2025-12-31
draft: false
categories:
  - NIP
  - Cryptography
  - Privacy
translationOf: /en/topics/nip-44.md
translationDate: 2026-04-22
---

NIP-44 define um padrão versionado de criptografia para payloads do Nostr, substituindo o esquema falho da NIP-04 por primitivas criptográficas modernas.

## Como funciona

A versão 2 da NIP-44 usa um processo de criptografia em várias etapas:

1. **Key agreement**: ECDH, secp256k1, entre chaves públicas do remetente e do destinatário produz um segredo compartilhado
2. **Key derivation**: HKDF-extract com SHA256 e salt `nip44-v2` cria uma conversation key
3. **Per-message keys**: HKDF-expand deriva chave ChaCha, nonce e chave HMAC a partir de um nonce aleatório
4. **Padding**: o conteúdo recebe padding para esconder o comprimento da mensagem
5. **Encryption**: ChaCha20 criptografa o conteúdo com padding
6. **Authentication**: HMAC-SHA256 fornece integridade da mensagem

A saída é um payload base64 versionado que vai dentro de um evento Nostr assinado normal. A spec exige que clientes validem a assinatura externa do evento NIP-01 antes de descriptografar o payload interno NIP-44.

## Escolhas criptográficas

- **ChaCha20** em vez de AES: mais rápido, com melhor resistência a ataques multi-key
- **HMAC-SHA256** em vez de Poly1305: MACs polinomiais são mais fáceis de falsificar
- **SHA256**: consistente com as primitivas existentes do Nostr
- **Formato versionado**: permite upgrades futuros de algoritmo

## Propriedades de segurança

- **Authenticated encryption**: mensagens não podem ser adulteradas
- **Length hiding**: padding obscurece o tamanho da mensagem
- **Conversation keys**: usar a mesma chave para conversas contínuas reduz custo computacional
- **Auditado**: a auditoria de segurança da Cure53 não encontrou vulnerabilidades exploráveis

## Notas de implementação

A NIP-44 não é um substituto drop-in para payloads da NIP-04. Ela define um formato de criptografia, não um kind de evento de mensagem direta. Protocolos como [NIP-17](/pt/topics/nip-17/) e [NIP-59](/pt/topics/nip-59/) definem como payloads criptografados são usados em fluxos reais de mensagens.

A entrada plaintext é texto UTF-8 com comprimento entre 1 e 65535 bytes. Essa é uma limitação real para implementadores: se sua aplicação precisa criptografar blobs binários arbitrários, você precisa de uma codificação adicional ou de um formato de contêiner diferente.

## Limitações

A NIP-44 não fornece:
- **Forward secrecy**: chaves comprometidas expõem mensagens antigas
- **Post-compromise security**: recuperação após comprometimento de chave
- **Deniability**: mensagens são comprovadamente assinadas por chaves específicas
- **Metadata hiding**: a arquitetura de relay limita a privacidade

Para necessidades de segurança alta, a NIP-104, double ratchet, ou protocolos baseados em MLS como Marmot oferecem garantias mais fortes.

## História

A revisão 3 da NIP-44 foi mergeada em dezembro de 2023 após uma auditoria independente da Cure53. Ela forma a base criptográfica para DMs privadas da NIP-17 e gift wrapping da NIP-59.

---

**Fontes primárias:**
- [Especificação NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md)
- [Implementações de referência da NIP-44](https://github.com/paulmillr/nip44)
- [Relatório de auditoria da Cure53](https://cure53.de/audit-report_nip44-implementations.pdf)

**Mencionado em:**
- [Newsletter #4: NIP Deep Dive](/pt/newsletters/2026-01-07-newsletter/)
- [Newsletter #3: dezembro de 2023](/pt/newsletters/2025-12-31-newsletter/)
- [Newsletter #3: dezembro de 2024](/pt/newsletters/2025-12-31-newsletter/)
- [Newsletter #12: Marmot](/pt/newsletters/2026-03-04-newsletter/)
- [Newsletter #13: Vector](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19: migração do nostter para NIP-44](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: nowhere criptografa tráfego Nostr](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-04: Mensagens diretas criptografadas (obsoleta)](/pt/topics/nip-04/)
- [NIP-17: Mensagens Diretas Privadas](/pt/topics/nip-17/)
- [NIP-59: Gift Wrap](/pt/topics/nip-59/)
- [NIP-104: criptografia double ratchet](/pt/topics/nip-104/)
- [MLS: Message Layer Security](/pt/topics/mls/)
