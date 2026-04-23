---
title: 'NIP-04: Mensagens diretas criptografadas (obsoleta)'
date: 2025-12-31
draft: false
categories:
  - Privacy
  - Messaging
translationOf: /en/topics/nip-04.md
translationDate: 2026-04-22
---

NIP-04 define mensagens diretas criptografadas usando eventos kind 4 e um segredo compartilhado derivado por ECDH. Foi o primeiro esquema de DM do Nostr, mas hoje é tecnologia legada, e o trabalho novo em mensagens privadas migrou para a NIP-17.

## Como funciona

Mensagens usam eventos kind 4 com este fluxo básico:

1. O remetente deriva um segredo compartilhado com ECDH em secp256k1.
2. O plaintext é criptografado com AES-256-CBC.
3. O evento inclui uma tag `p` nomeando o destinatário.
4. O ciphertext é codificado em base64 e armazenado em `content` junto com o IV.

O próprio evento continua sendo um evento Nostr assinado normal, então relays conseguem ver os metadados externos mesmo sem conseguir ler o plaintext.

## Limites de segurança e privacidade

NIP-04 tem deficiências importantes de privacidade:

- **Vazamento de metadados** - a pubkey do remetente fica publicamente visível em toda mensagem
- **Sem privacidade do remetente** - qualquer pessoa consegue ver quem está mandando mensagem para quem
- **Timestamps exatos** - o timing da mensagem não é randomizado
- **Tratamento não padrão de chaves** - o esquema usa apenas a coordenada X do ponto ECDH, o que dificultou corretude entre bibliotecas e deixou pouco espaço para evolução do protocolo

A própria especificação alerta explicitamente que ela não chega perto do estado da arte em comunicação criptografada.

## Por que foi substituída

NIP-04 criptografa o conteúdo da mensagem, mas não esconde o grafo social. Operadores de relay ainda conseguem ver quem enviou o evento, quem o recebe e quando ele foi publicado. Esse volume de metadados basta para mapear conversas mesmo sem descriptografar o payload.

A NIP-17 resolve isso combinando criptografia de payload da NIP-44 com gift wrapping da NIP-59, o que esconde o remetente de relays e observadores casuais. Implementações novas devem tratar a NIP-04 como compatibilidade apenas.

## Status de implementação

Clientes e signers legados ainda expõem métodos de encrypt e decrypt da NIP-04 porque conversas antigas e apps mais velhos ainda circulam. Essa camada de compatibilidade importa para migração, mas construir recursos novos em cima de eventos kind 4 geralmente significa carregar adiante os limites antigos de privacidade.

---

**Fontes primárias:**
- [Especificação NIP-04](https://github.com/nostr-protocol/nips/blob/master/04.md)

**Mencionado em:**
- [Newsletter #4: NIP Deep Dive](/pt/newsletters/2026-01-07-newsletter/)
- [Newsletter #3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/)
- [Newsletter #19: migração do nostter para NIP-44](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-44: cargas criptografadas](/pt/topics/nip-44/)
- [NIP-17: Mensagens Diretas Privadas](/pt/topics/nip-17/)
- [NIP-59: Gift Wrap](/pt/topics/nip-59/)
