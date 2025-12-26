---
title: "NIP-A4: Mensajes Públicos"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-A4 define mensajes públicos (kind 24) diseñados para pantallas de notificaciones, con amplio soporte de clientes como objetivo.

## Cómo Funciona

A diferencia de las conversaciones hiladas, estos mensajes no tienen concepto de historial de chat ni cadenas de mensajes. Son mensajes simples de una sola vez destinados a aparecer en el feed de notificaciones de un destinatario.

## Estructura

- Usa etiquetas `q` (citas) en lugar de etiquetas `e` para evitar complicaciones de hilos
- Sin estado de conversación ni historial
- Diseñado para notificaciones públicas simples

## Casos de Uso

- Reconocimientos públicos o menciones destacadas
- Mensajes de difusión a un usuario
- Notificaciones que no necesitan hilos de respuesta

---

**Fuentes primarias:**
- [PR de NIP-A4](https://github.com/nostr-protocol/nips/pull/1988)

**Mencionado en:**
- [Boletín #2: Actualizaciones de NIP](/es/newsletters/2025-12-24-newsletter/#nip-updates)

**Ver también:**
- [NIP-01: Protocolo Básico](/es/topics/nip-01/)
- [NIP-10: Hilos de Notas de Texto](/es/topics/nip-10/)
