---
title: "NIP-63: Paywall / Contenido Premium"
date: 2025-12-17
translationOf: /en/topics/nip-63.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Monetization
---

NIP-63 es un estándar propuesto para manejar contenido restringido dentro del protocolo Nostr, permitiendo a los creadores requerir pago antes de revelar contenido.

## Cómo Funciona

Los creadores de contenido pueden publicar eventos donde el contenido completo está cifrado u oculto detrás de un paywall. Después de la verificación del pago, el contenido se desbloquea para el usuario que pagó.

La propuesta se centra intencionalmente en la superficie de protocolo para contenido premium, no en imponer un único canal de pago o modelo de negocio. Eso lo mantiene flexible, pero también significa que billeteras, clientes y editores aún necesitan ponerse de acuerdo en el flujo de desbloqueo en la práctica.

## Por Qué Importa

Sin un formato compartido, cada sistema de paywall en Nostr se convierte en su propio silo. Un NIP común permitiría que un cliente publique contenido premium y otro cliente entienda que el contenido está restringido, qué se debe pagar y cuándo debe revelarse.

Eso no garantiza portabilidad todavía. NIP-63 sigue siendo una propuesta en el [PR #2156](https://github.com/nostr-protocol/nips/pull/2156), por lo que las implementaciones aún pueden divergir mientras el diseño está en discusión.

## Casos de Uso

- Artículos solo para suscriptores
- Contenido multimedia premium
- Eventos de pago por ver
- Acceso exclusivo a creadores

## Consideraciones

Los metadatos del paywall pueden ser públicos incluso cuando el contenido premium no lo es. Eso da a los clientes información suficiente para presentar una oferta, pero también significa que la existencia de contenido de pago es visible para cualquiera que pueda leer el evento.

Los creadores también necesitan pensar en lo que sucede después del desbloqueo. Una vez que el texto plano se muestra a un usuario que pagó, el protocolo no puede impedir que ese usuario lo copie en otro lugar.

---

**Fuentes primarias:**
- [Propuesta NIP-63 (PR #2156)](https://github.com/nostr-protocol/nips/pull/2156)

**Mencionado en:**
- [Newsletter #1: Actualizaciones de NIP](/en/newsletters/2025-12-17-newsletter/#nip-updates)

**Ver también:**
- [NIP-57: Zaps](/es/topics/nip-57/)
