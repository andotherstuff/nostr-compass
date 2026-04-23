---
title: "NIP-5D: Nostr Web Applets"
date: 2026-04-08
translationOf: /en/topics/nip-5d.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Hosting
---

NIP-5D define un protocolo `postMessage` para aplicaciones web aisladas ("napplets") que se ejecutan en iframes y se comunican con una aplicación anfitriona ("shell"). Extiende [NIP-5A](/es/topics/nip-5a/) (sitios web estáticos) con una capa de comunicación en runtime que da a las web apps acceso a funcionalidad de Nostr sin exponer la clave privada del usuario.

## Cómo funciona

Una aplicación shell carga una napplet en un iframe aislado. La napplet se comunica con el shell mediante la API `postMessage` del navegador usando un protocolo de mensajes estructurado. El shell proporciona a la napplet firma Nostr, acceso a relay y contexto de usuario a través de este canal de mensajes. El sandbox del iframe evita que la napplet acceda directamente a la clave privada del usuario, por lo que el shell actúa como guardián de todas las operaciones Nostr.

## Casos de uso

- **Apps Nostr interactivas**: Construir apps que leen y escriben eventos Nostr sin exigir que los usuarios peguen su nsec
- **Marketplace de apps**: Distribuir aplicaciones web interactivas mediante eventos Nostr
- **Extensiones aisladas**: Añadir funcionalidad a clientes Nostr mediante napplets de terceros

---

**Fuentes primarias:**
- [NIP-5D PR #2303](https://github.com/nostr-protocol/nips/pull/2303) - propuesta de Nostr Web Applets

**Mencionado en:**
- [Boletín #17](/en/newsletters/2026-04-08-newsletter/)

**Ver también:**
- [NIP-5A (sitios web estáticos)](/es/topics/nip-5a/)
- [NIP-5C (Scrolls)](/es/topics/nip-5c/)
