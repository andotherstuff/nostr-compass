---
title: "NIP-04: Mensagens Diretas Criptografadas (Obsoleto)"
date: 2025-12-31
translationOf: /en/topics/nip-04.md
translationDate: 2025-12-31
draft: false
categories:
  - Privacidade
  - Mensagens
---

NIP-04 define mensagens diretas criptografadas usando criptografia AES-256-CBC. Foi o método original para mensagens privadas no Nostr, mas foi descontinuado em favor do NIP-17 devido a limitações significativas de privacidade.

## Como funciona

As mensagens usam eventos de kind 4 com o seguinte esquema de criptografia:
1. Um segredo compartilhado é gerado usando ECDH com a chave pública do destinatário e a chave privada do remetente
2. A mensagem é criptografada com AES-256-CBC
3. O texto cifrado é codificado em base64 com o vetor de inicialização anexado
4. Uma tag `p` identifica a chave pública do destinatário

## Limitações de segurança

NIP-04 tem deficiências significativas de privacidade:

- **Vazamento de metadados** - A pubkey do remetente é publicamente visível em cada mensagem
- **Sem privacidade do remetente** - Qualquer um pode ver quem está enviando mensagens para quem
- **Carimbos de tempo exatos** - O tempo das mensagens não é randomizado
- **Implementação não padrão** - Usa apenas a coordenada X do ponto ECDH em vez do hash SHA256 padrão

A especificação adverte explicitamente que "não chega nem perto do estado da arte em comunicação criptografada".

## Status de descontinuação

NIP-04 está descontinuado em favor do NIP-17, que usa o empacotamento de presente (gift wrapping) do NIP-59 para ocultar a identidade do remetente. Novas implementações devem usar NIP-17 para mensagens privadas.

---

**Fontes principais:**
- [Especificação NIP-04](https://github.com/nostr-protocol/nips/blob/master/04.md)

**Mencionado em:**
- [Newsletter #3: Resumo de Dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Veja também:**
- [NIP-17: Mensagens Diretas Privadas](/pt/topics/nip-17/)
- [NIP-59: Gift Wrap](/pt/topics/nip-59/)
