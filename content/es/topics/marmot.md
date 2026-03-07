---
title: "Protocolo Marmot"
date: 2025-12-17
translationOf: /en/topics/marmot.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot es un protocolo para mensajería grupal cifrada de extremo a extremo en Nostr. Combina la identidad y red de relays de Nostr con MLS para gestión de claves de grupo, forward secrecy y seguridad post-compromiso.

## Cómo Funciona

Marmot usa Nostr para identidad, transporte por relays y distribución de eventos, y luego superpone MLS para cambios de membresía grupal y cifrado de mensajes. A diferencia de [NIP-17](/es/topics/nip-17/), que se centra en mensajería uno a uno, Marmot está construido para grupos donde los miembros se unen, salen o rotan claves con el tiempo.

## Por Qué Es Importante

MLS le da a Marmot propiedades que los esquemas de mensajes directos de Nostr no proporcionan por sí solos: evolución del estado del grupo, semántica de eliminación de miembros y recuperación después de un compromiso a través de actualizaciones posteriores de claves.

Esa división del trabajo es la idea útil. Nostr resuelve identidad y transporte en una red abierta. MLS resuelve el acuerdo autenticado de claves de grupo. Marmot es la capa de unión entre ambos.

## Estado de Implementación

El protocolo sigue siendo experimental, pero ahora tiene múltiples implementaciones y uso activo en aplicaciones. MDK es el stack de referencia principal en Rust, `marmot-ts` lleva el modelo a TypeScript, y aplicaciones como White Noise, Pika y Vector han estado usando componentes compatibles con Marmot.

El trabajo reciente se ha centrado en endurecimiento e interoperabilidad. Las correcciones impulsadas por auditoría se integraron a principios de 2026, y MIP-03 introdujo la resolución determinista de commits para que los clientes puedan converger cuando cambios concurrentes de estado de grupo compiten a través de relays.

---

**Fuentes primarias:**
- [Repositorio del Protocolo Marmot](https://github.com/marmot-protocol/marmot)
- [NIP-104: Chats Grupales Cifrados basados en MLS](/es/topics/nip-104/)
- [Marmot Development Kit](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)

**Mencionado en:**
- [Boletín #1: Noticias](/es/newsletters/2025-12-17-newsletter/#news)
- [Boletín #1: Lanzamientos](/es/newsletters/2025-12-17-newsletter/#releases)
- [Boletín #4](/es/newsletters/2026-01-07-newsletter/)
- [Boletín #7](/es/newsletters/2026-01-28-newsletter/)
- [Boletín #12](/es/newsletters/2026-03-04-newsletter/)

**Ver también:**
- [MLS (Message Layer Security)](/es/topics/mls/)
- [MIP-05: Notificaciones Push que Preservan la Privacidad](/es/topics/mip-05/)
- [NIP-17: Mensajes Directos Privados](/es/topics/nip-17/)
- [NIP-59: Gift Wrap](/es/topics/nip-59/)
