---
title: "NIP-09: Solicitud de Eliminación de Eventos"
date: 2026-02-25
translationOf: /en/topics/nip-09.md
translationDate: 2026-03-07
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-09 define una forma para que los autores soliciten la eliminación de eventos que publicaron previamente. Es una señal de eliminación del lado del relay, no una función de borrado a nivel de red.

## Cómo Funciona

Los usuarios publican eventos kind 5 que contienen referencias a los eventos que quieren eliminar. Los relays que soportan NIP-09 deben dejar de servir los eventos coincidentes del mismo autor y pueden eliminarlos del almacenamiento.

La eliminación es una solicitud, no una garantía. Los relays pueden ignorar las solicitudes de eliminación, y los eventos pueden haberse propagado ya a relays que no soportan eliminación. Los usuarios no deben confiar en NIP-09 para la eliminación de contenido sensible a la privacidad.

## Por Qué Importa

NIP-09 proporciona a clientes y relays una forma común de expresar "este evento ya no debería aparecer", lo cual es útil para publicaciones accidentales, renovación de estado de billeteras y flujos de moderación. Pero el autor solo puede solicitar la eliminación de sus propios eventos. No es un mecanismo de takedown de propósito general para contenido de terceros.

## Compensaciones

El punto débil es la propagación. Una vez que un evento ha sido replicado a través de múltiples relays, la eliminación se convierte en mejor esfuerzo. Algunos relays lo eliminarán, algunos lo marcarán como tombstone, y algunos seguirán sirviéndolo indefinidamente. Los clientes que presentan la eliminación como definitiva están exagerando lo que el protocolo garantiza.

Otro problema práctico son las referencias. Los usuarios y aplicaciones pueden seguir teniendo el evento eliminado localmente, o citarlo en otro lugar, incluso después de que un relay compatible deje de servirlo.

---

**Fuentes primarias:**
- [Especificación NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md)

**Mencionado en:**
- [Boletín #11: Análisis Profundo NIP-60](/es/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-60-cashu-wallet)
- [Boletín #12: Noticias](/es/newsletters/2026-03-04-newsletter/#news)

**Ver también:**
- [NIP-01: Protocolo Básico](/es/topics/nip-01/)
- [NIP-60: Billetera Cashu](/es/topics/nip-60/)
