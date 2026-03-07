---
title: "MLS (Message Layer Security)"
date: 2025-12-31
translationOf: /en/topics/mls.md
translationDate: 2026-03-07
draft: false
categories:
  - Cryptography
  - Protocol
  - Messaging
  - Privacy
---

Message Layer Security (MLS) es un protocolo IETF para mensajería grupal cifrada de extremo a extremo. Proporciona forward secrecy y seguridad post-compromiso para grupos cuya membresía puede cambiar con el tiempo.

## Cómo Funciona

MLS usa una estructura de acuerdo de claves basada en árboles llamada TreeKEM:

1. **Paquetes de claves**: Cada participante publica un paquete de claves con su identidad y claves de cifrado
2. **Estado del grupo**: Un árbol ratchet mantiene el estado criptográfico del grupo
3. **Commits**: Los miembros actualizan el árbol al unirse, salir o rotar claves
4. **Cifrado de mensajes**: El contenido se cifra usando claves derivadas del secreto compartido del grupo

## Por Qué Es Importante

MLS resuelve un problema que el cifrado por pares no resuelve bien: mantener la membresía de grupo y el estado de cifrado coherentes cuando los miembros se unen, salen o rotan claves de forma asíncrona.

Su estructura de árbol es la idea práctica. Las actualizaciones no requieren que cada participante renegocie por pares con todos los demás, por lo que el protocolo escala mucho mejor que los esquemas ad hoc de claves de grupo.

## Estandarización

- **RFC 9420** (julio 2023): Especificación del protocolo MLS central
- **RFC 9750** (abril 2025): Arquitectura MLS para integración de sistemas

## Adopción en Nostr

Varias aplicaciones Nostr usan MLS para mensajería grupal segura:

- **KeyChat**: Aplicación de mensajería cifrada basada en MLS para móvil y escritorio
- **White Noise**: Mensajería privada usando MLS con integración del protocolo Marmot
- **Marmot Protocol**: Extensión de Nostr que proporciona cifrado grupal basado en MLS

MLS ofrece garantías de seguridad de grupo más fuertes que [NIP-04](/es/topics/nip-04/) o [NIP-44](/es/topics/nip-44/) por sí solos, especialmente cuando la membresía cambia con frecuencia.

## Compensaciones

MLS no es un producto de mensajería completo. Las aplicaciones aún necesitan identidad, transporte, resistencia al spam, almacenamiento y manejo de conflictos alrededor del protocolo.

Por eso los proyectos Nostr como Marmot añaden reglas adicionales sobre MLS. La criptografía está estandarizada, pero el protocolo de aplicación circundante aún importa para la interoperabilidad.

---

**Fuentes primarias:**
- [RFC 9420: MLS Protocol](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: MLS Architecture](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS Working Group](https://datatracker.ietf.org/wg/mls/about/)
- [MLS Protocol Website](https://messaginglayersecurity.rocks/)

**Mencionado en:**
- [Boletín #3: Lanzamientos](/es/newsletters/2025-12-31-newsletter/#releases)
- [Boletín #10](/es/newsletters/2026-02-18-newsletter/)
- [Boletín #12](/es/newsletters/2026-03-04-newsletter/)

**Ver también:**
- [Protocolo Marmot](/es/topics/marmot/)
- [MIP-05: Notificaciones Push que Preservan la Privacidad](/es/topics/mip-05/)
- [NIP-17: Mensajes Directos Privados](/es/topics/nip-17/)
- [NIP-44: Cargas Útiles Cifradas](/es/topics/nip-44/)
