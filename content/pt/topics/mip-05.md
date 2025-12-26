---
title: "MIP-05: Notificações Push que Preservam Privacidade"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
  - Protocol
translationOf: /en/topics/mip-05.md
translationDate: 2025-12-26
---

MIP-05 define um protocolo para notificações push que mantém a privacidade do usuário, resolvendo o problema de que sistemas tradicionais de push requerem que servidores conheçam tokens de dispositivo e identidades de usuários.

## Como Funciona

- Tokens de dispositivo são criptografados com ECDH+HKDF e ChaCha20-Poly1305
- Chaves efêmeras previnem correlação entre notificações
- Um protocolo de fofoca de três eventos (kinds 447-449) sincroniza tokens criptografados entre membros do grupo
- Tokens falsos via gift wrapping NIP-59 escondem tamanhos de grupo

## Garantias de Privacidade

- Servidores de notificação push não podem identificar usuários
- Membresia de grupo não é revelada por padrões de notificação
- Tokens de dispositivo não podem ser correlacionados entre mensagens

## Tipos de Evento

- **Kind 447**: Publicação de token de dispositivo criptografado
- **Kind 448**: Solicitação de sincronização de token
- **Kind 449**: Resposta de sincronização de token

---

**Fontes primárias:**
- [PR MIP-05](https://github.com/marmot-protocol/marmot/pull/18)

**Mencionado em:**
- [Newsletter #1: Notícias](/pt/newsletters/2025-12-17-newsletter/#news)

**Veja também:**
- [Protocolo Marmot](/pt/topics/marmot/)
- [NIP-59: Gift Wrap](/pt/topics/nip-59/)
