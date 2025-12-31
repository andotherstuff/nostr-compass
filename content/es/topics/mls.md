---
title: "MLS (Message Layer Security)"
date: 2025-12-31
translationOf: /en/topics/mls.md
translationDate: 2025-12-31
draft: false
categories:
  - Criptografía
  - Protocolo
  - Mensajería
  - Privacidad
---

Message Layer Security (MLS) es un protocolo estandarizado por el IETF para mensajería grupal con cifrado de extremo a extremo. Proporciona establecimiento eficiente de claves con secreto hacia adelante y seguridad post-compromiso para grupos que van desde dos hasta miles de participantes.

## Cómo funciona

MLS utiliza una estructura de acuerdo de claves basada en árboles llamada TreeKEM:

1. **Paquetes de claves**: Cada participante publica un paquete de claves que contiene su identidad y claves de cifrado
2. **Estado del grupo**: Un árbol ratchet mantiene el estado criptográfico del grupo
3. **Commits**: Los miembros actualizan el árbol al unirse, salir o rotar claves
4. **Cifrado de mensajes**: El contenido se cifra usando claves derivadas del secreto compartido del grupo

## Propiedades de seguridad clave

- **Secreto hacia adelante**: Los mensajes pasados permanecen seguros incluso si las claves actuales se ven comprometidas
- **Seguridad post-compromiso**: Los mensajes futuros vuelven a ser seguros después de la rotación de claves
- **Autenticación de membresía**: Todos los miembros del grupo son verificados criptográficamente
- **Operación asíncrona**: Los miembros pueden unirse/salir sin que todos los participantes estén en línea
- **Escalabilidad**: Eficiente para grupos de hasta 50,000 participantes

## Estandarización

- **RFC 9420** (julio 2023): Especificación del protocolo MLS central
- **RFC 9750** (abril 2025): Arquitectura MLS para integración de sistemas

## Adopción en Nostr

Varias aplicaciones de Nostr utilizan MLS para mensajería grupal segura:

- **KeyChat**: Aplicación de mensajería cifrada basada en MLS para móvil y escritorio
- **White Noise**: Mensajería privada usando MLS con integración del protocolo Marmot
- **Marmot Protocol**: Extensión de Nostr que proporciona cifrado grupal basado en MLS

MLS ofrece garantías de seguridad más fuertes que NIP-04 o NIP-44 por sí solos, particularmente para chats grupales donde los miembros se unen y salen dinámicamente.

## Adopción en la industria

Más allá de Nostr, MLS está siendo adoptado por:
- Google Messages (RCS con MLS vía GSMA Universal Profile 3.0)
- Apple Messages (soporte RCS anunciado para MLS)
- Cisco WebEx, Wickr, Matrix

---

**Fuentes principales:**
- [RFC 9420: MLS Protocol](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: MLS Architecture](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS Working Group](https://datatracker.ietf.org/wg/mls/about/)
- [MLS Protocol Website](https://messaginglayersecurity.rocks/)

**Mencionado en:**
- [Newsletter #3: Lanzamientos](/es/newsletters/2025-12-31-newsletter/#releases)

**Ver también:**
- [Marmot Protocol](/es/topics/marmot/)
- [MIP-05: Notificaciones Push que Preservan la Privacidad](/es/topics/mip-05/)
- [NIP-17: Mensajes Directos Privados](/es/topics/nip-17/)
- [NIP-44: Cargas Útiles Cifradas](/es/topics/nip-44/)
