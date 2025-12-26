---
title: "Protocolo Marmot"
date: 2025-12-17
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot es un protocolo para mensajería grupal encriptada de extremo a extremo construido sobre Nostr, usando el estándar Message Layer Security (MLS) para forward secrecy y seguridad post-compromiso.

## Cómo Funciona

Marmot extiende Nostr con encriptación basada en MLS para chats grupales. A diferencia de los DMs de NIP-17 que son uno a uno, Marmot maneja comunicación grupal segura donde los miembros pueden unirse y salir mientras se mantienen las garantías de encriptación.

## Características Clave

- Forward secrecy y seguridad post-compromiso vía MLS
- Gestión de claves de grupo para membresía dinámica
- Notificaciones push que preservan la privacidad vía MIP-05

---

**Fuentes primarias:**
- [Repositorio del Protocolo Marmot](https://github.com/marmot-protocol/marmot)

**Mencionado en:**
- [Boletín #1: Noticias](/es/newsletters/2025-12-17-newsletter/#news)
- [Boletín #1: Lanzamientos](/es/newsletters/2025-12-17-newsletter/#releases)

**Ver también:**
- [MIP-05: Notificaciones Push que Preservan la Privacidad](/es/topics/mip-05/)
- [NIP-17: Mensajes Directos Privados](/es/topics/nip-17/)
- [NIP-59: Gift Wrap](/es/topics/nip-59/)
