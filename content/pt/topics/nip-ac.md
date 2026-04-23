---
title: 'NIP-AC: Chamadas P2P de voz e vídeo'
date: 2026-04-08
draft: false
categories:
  - Messaging
  - Live Streaming
translationOf: /en/topics/nip-ac.md
translationDate: 2026-04-22
---

NIP-AC propõe um protocolo para chamadas peer-to-peer de voz e vídeo sobre Nostr. A spec usa eventos Nostr para sinalização de chamadas, incluindo offers, answers e ICE candidates, e usa WebRTC para o transporte real de mídia, mantendo a configuração da chamada descentralizada enquanto aproveita APIs padrão de navegador para áudio e vídeo.

## Como funciona

Quem faz a chamada publica um evento de offer contendo uma WebRTC Session Description Protocol, ou SDP, offer, marcada com a pubkey do destinatário. O destinatário responde com um evento SDP answer. As duas partes trocam eventos de ICE candidate para negociar o caminho de rede. Quando a conexão WebRTC é estabelecida, a mídia flui diretamente entre os peers sem participação do relay.

Os eventos de sinalização são criptografados, então os relays não conseguem observar quem está chamando quem. A máquina de estados da chamada lida com transições de offer, answer, reject, busy e hangup.

## Implementações

- [Amethyst](https://github.com/vitorpamplona/amethyst) está construindo suporte a NIP-AC com uma suíte de testes da máquina de estados de chamadas e tratamento de offers antigas.

---

**Fontes primárias:**
- [NIP-AC PR #2301](https://github.com/nostr-protocol/nips/pull/2301) - chamadas P2P de voz e vídeo sobre WebRTC

**Mencionado em:**
- [Nostr Compass #17 (2026-04-08)](/pt/newsletters/2026-04-08-newsletter/)

**Veja também:**
- [NIP-44: cargas criptografadas](/pt/topics/nip-44/)
