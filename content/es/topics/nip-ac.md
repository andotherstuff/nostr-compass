---
title: "NIP-AC: Llamadas P2P de voz y vídeo"
date: 2026-04-08
translationOf: /en/topics/nip-ac.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Mensajería
---

NIP-AC propone un protocolo para llamadas peer-to-peer de voz y vídeo sobre Nostr. La especificación usa eventos Nostr para la señalización de llamadas (offers, answers y candidatos ICE) y WebRTC para el transporte real de medios, manteniendo descentralizada la configuración de la llamada mientras usa APIs estándar del navegador para audio y vídeo.

## Cómo funciona

Quien llama publica un evento de oferta de llamada que contiene una oferta Session Description Protocol (SDP) de WebRTC, etiquetada con la pubkey del destinatario. El destinatario responde con un evento de respuesta SDP. Ambas partes intercambian eventos de candidatos ICE para negociar la ruta de red. Una vez establecida la conexión WebRTC, el medio fluye directamente entre peers sin participación del relay.

Los eventos de señalización van cifrados para que los relays no puedan observar quién llama a quién. La máquina de estados de la llamada maneja transiciones de offer, answer, reject, busy y hangup.

## Implementaciones

- [Amethyst](https://github.com/vitorpamplona/amethyst) está construyendo soporte NIP-AC con una suite de tests para la máquina de estados de llamadas y manejo de ofertas de llamada obsoletas.

---

**Fuentes primarias:**
- [NIP-AC PR #2301](https://github.com/nostr-protocol/nips/pull/2301) - llamadas P2P de voz y vídeo sobre WebRTC

**Mencionado en:**
- [Nostr Compass #17 (2026-04-08)](/es/newsletters/2026-04-08-newsletter/)

**Ver también:**
- [NIP-44 (Encrypted Payloads)](/es/topics/nip-44/)
