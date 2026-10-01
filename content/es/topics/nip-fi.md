---
title: "Buzz NIP-FI: Aserciones de identidad federada"
date: 2026-09-30
draft: false
categories:
  - Project Proposals
  - Identity
  - Relays
translationOf: /en/topics/nip-fi.md
translationDate: 2026-10-01
---

NIP-FI es la especificación de aserciones de identidad federada **específica del proyecto** Buzz. El nombre no implica su adopción por parte del repositorio `nostr-protocol/nips` ni la interoperabilidad con relays ajenos a Buzz.

## Entrada HTTP

Para las solicitudes HTTP protegidas en modo de aplicación obligatoria, Buzz combina una aserción de identidad federada con un event de autorización firmado conforme a NIP-98. La clave pública de Nostr acreditada mediante la firma HTTP debe coincidir con la clave indicada en la aserción. Las pruebas ausentes, que no coincidan o que no puedan verificarse se rechazan. Buzz utiliza esta combinación para vincular la decisión de autorización de un emisor de identidad externo con la clave de Nostr que realiza la solicitud.

La [revisión de la especificación del proyecto](https://github.com/block/buzz/pull/7254) define el modelo de aplicación obligatoria. La [implementación de entrada HTTP integrada](https://github.com/block/buzz/pull/7264) abarca las interfaces HTTP protegidas de Buzz, incluidas las rutas del puente de relay, de medios, de flujos de trabajo y de Git. La integración informa de pruebas del código fuente; no significa que otro relay de Nostr implemente la misma política.

---

**Fuentes primarias:**
- [Revisión de la especificación NIP-FI de Buzz](https://github.com/block/buzz/pull/7254)
- [Implementación de entrada HTTP de Buzz](https://github.com/block/buzz/pull/7264)

**Mencionado en:**
- [Boletín #42: Controles de identidad de Buzz](/es/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
