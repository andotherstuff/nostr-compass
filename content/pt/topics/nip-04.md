---
title: 'NIP-04: Mensagens diretas criptografadas (obsoleto)'
date: 2025-12-31
draft: false
categories:
- Privacy
- Messaging
translationOf: /en/topics/nip-04.md
translationDate: '2026-03-07'
---

NIP-04 define mensagens diretas criptografadas usando eventos kind 4 e um segredo compartilhado derivado de ECDH. Foi o primeiro esquema DM da Nostr, mas agora é uma tecnologia legada e o novo trabalho de mensagens privadas foi transferido para o NIP-17.

## Como funciona

As mensagens usam eventos kind 4 com este fluxo básico:

1. O remetente deriva um segredo compartilhado com o ECDH secp256k1.
2. O texto simples é criptografado com AES-256-CBC.
3. O evento inclui um `p` tag nomeando o destinatário.
4. O texto cifrado é codificado como base64 e armazenado em `content` junto com o IV.

O evento em si ainda é um evento Nostr normal assinado, então relays pode ver os metadados externos mesmo que não consiga ler o texto simples.

## Limites de segurança e privacidade

O NIP-04 tem deficiências significativas de privacidade:

- **Vazamento de metadados** - O pubkey do remetente fica visível publicamente em todas as mensagens
- **Sem privacidade do remetente** - Qualquer pessoa pode ver quem está enviando mensagens para quem
- **Carimbos de data e hora exatos** - O tempo da mensagem não é aleatório
- **Manuseio de chave não padrão** - O esquema usa apenas a coordenada X do ponto ECDH, o que dificultou a correção entre bibliotecas e deixou pouco espaço para evolução do protocolo

A especificação alerta explicitamente que "não chega nem perto do que há de mais moderno em comunicação criptografada".

## Por que foi substituído

O NIP-04 criptografa o conteúdo da mensagem, mas não oculta o gráfico social. Os operadores de relay ainda podem ver quem enviou o evento, quem o recebe e quando foi publicado. São metadados suficientes para mapear conversas mesmo sem descriptografar o payload.

O NIP-17 resolve isso combinando a criptografia NIP-44 payload com o embrulho de presente NIP-59, que esconde o remetente dos relays e de observadores aleatórios. Novas implementações devem tratar o NIP-04 apenas como compatibilidade.

## Status de implementação

Clientes e assinantes legados ainda expõem métodos de criptografia/descriptografia NIP-04 porque conversas antigas e aplicativos mais antigos permanecem em circulação. Essa camada de compatibilidade é importante para a migração, mas construir novos recursos sobre os eventos kind 4 geralmente significa levar adiante os antigos limites de privacidade.

---

**Fontes primárias:**
- [Especificação NIP-04](https://github.com/nostr-protocol/nips/blob/master/04.md)

**Mencionado em:**
- [Boletim informativo nº 4: Aprofundamento do NIP](/pt/newsletters/2026-01-07-newsletter/#nip-04-encrypted-direct-messages-legacy)
- [Boletim informativo nº 3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Veja também:**
- [NIP-44: cargas criptografadas](/pt/topics/nip-44/)
- [NIP-17: Mensagens Diretas Privadas](/pt/topics/nip-17/)
- [NIP-59: Gift Wrap](/pt/topics/nip-59/)
