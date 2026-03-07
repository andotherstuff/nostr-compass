---
title: 'MIP-05: Notificações push que preservam a privacidade'
date: 2025-12-17
draft: false
categories:
- Privacy
- Messaging
- Protocol
translationOf: /en/topics/mip-05.md
translationDate: '2026-03-07'
---

MIP-05 define um protocolo de notificação push para clientes Marmot que tenta preservar a privacidade em um ambiente onde sistemas push móveis comuns geralmente expõem tokens de dispositivos e relacionamentos de contas.

## Como funciona

- Os tokens do dispositivo são criptografados com ECDH+HKDF e ChaCha20-Poly1305
- Chaves efêmeras evitam correlação entre notificações
- Um protocolo de fofoca de três eventos (kinds 447-449) sincroniza tokens criptografados entre membros do grupo
- Tokens chamariz via embrulho de presente NIP-59 ocultam tamanhos de grupo

## Modelo de privacidade

- Os servidores de notificação push não conseguem identificar os usuários
- A associação ao grupo não é revelada pelos padrões de notificação
- Os tokens do dispositivo não podem ser correlacionados entre mensagens

A melhoria concreta é que o provedor push vê tokens de entrega opacos, e não um mapa direto do membro do grupo para o dispositivo. Isso não torna as notificações anônimas em sentido absoluto, mas reduz o quanto a camada push aprende por padrão.

## Tipos de eventos

- **kind 447**: publicação de token de dispositivo criptografado
- **kind 448**: solicitação de sincronização de token
- **kind 449**: resposta de sincronização de token

## Compensações

MIP-05 adiciona privacidade adicionando trabalho de coordenação. Os clientes precisam sincronizar o estado do token criptografado entre os membros do grupo, e os tokens chamariz aumentam a sobrecarga da mensagem propositalmente.

Isso significa que os implementadores precisam equilibrar a confiabilidade da entrega com a proteção de metadados. O protocolo é útil precisamente porque trata o push como um problema de privacidade, e não apenas como uma conveniência de transporte.

---

**Fontes primárias:**
- [Especificação MIP-05](https://github.com/marmot-protocol/marmot/blob/master/05.md)
- [MIP-05 PR](https://github.com/marmot-protocol/marmot/pull/18)
- [versão White Noise v0.2.1](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**Mencionado em:**
- [Boletim informativo nº 1: Notícias](/pt/newsletters/2025-12-17-newsletter/#news)
- [Boletim informativo nº 3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Veja também:**
- [Protocolo Marmot](/pt/topics/marmot/)
- [NIP-59: Gift Wrap](/pt/topics/nip-59/)
