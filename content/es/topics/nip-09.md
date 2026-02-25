---
title: "NIP-09"
date: 2026-02-25
translationOf: /en/topics/nip-09.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - Protocol
---

NIP-09 define Eliminación de Eventos, un mecanismo para que los usuarios soliciten que los relays eliminen sus eventos previamente publicados.

## Cómo Funciona

Los usuarios publican eventos kind 5 conteniendo etiquetas `e` que referencian los IDs de evento que quieren eliminar. Los relays que soportan NIP-09 deberían dejar de servir los eventos referenciados y pueden eliminarlos del almacenamiento.

La eliminación es una solicitud, no una garantía. Los relays pueden ignorar solicitudes de eliminación, y los eventos pueden haberse propagado ya a relays que no soportan eliminación. Los usuarios no deberían confiar en NIP-09 para la eliminación de contenido sensible a privacidad.

## Características Clave

- Eventos de solicitud de eliminación kind 5
- Referencian eventos eliminados por ID via etiquetas e
- Campo de razón opcional para contexto de eliminación
- Cumplimiento del relay es voluntario

---

**Fuentes primarias:**
- [Especificación NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md)

**Mencionado en:**
- [Newsletter #11: Análisis Profundo NIP-60](/es/newsletters/2026-02-25-newsletter/#análisis-profundo-de-nip-nip-60-billetera-cashu)

**Ver también:**
- [NIP-60: Billetera Cashu](/es/topics/nip-60/)
