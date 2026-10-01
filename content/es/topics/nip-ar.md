---
title: "Buzz NIP-AR: Artefactos de canal"
date: 2026-09-30
draft: false
categories:
  - Project Proposals
  - Collaboration
translationOf: /en/topics/nip-ar.md
translationDate: 2026-10-01
---

NIP-AR es la especificación de artefactos de canal **específica del proyecto** Buzz. Esta denominación no significa que haya sido adoptada por el repositorio `nostr-protocol/nips` ni por otros relays.

## Modelo de artefactos

Un artefacto es un registro editable con una identidad `d` estable, un único canal de pertenencia indicado en una tag `h` y revisiones que contienen instantáneas completas enlazadas mediante `prev`. Un relay acepta una edición solo si `prev` identifica la revisión vigente. Por lo tanto, dos revisiones en competencia no pueden convertirse ambas en la siguiente revisión vigente. La implementación de Buzz utiliza el kind `45010` para los artefactos y un marcador de kind `45011` firmado por el relay cuando un artefacto se traslada fuera de un canal. El canal de origen ve la eliminación sin conocer el destino a partir de ese marcador.

La [integración de la especificación de Buzz](https://github.com/block/buzz/pull/7791) describe el modelo, y la [integración de la implementación del relay](https://github.com/block/buzz/pull/7919) informa de pruebas sobre la gestión de conflictos, las consultas del historial, los traslados y los permisos de canal. Estas integraciones establecen el comportamiento del código fuente del proyecto, no un estándar general de Nostr ni una garantía de despliegue público.

---

**Fuentes primarias:**
- [Integración de la especificación de artefactos de canal de Buzz](https://github.com/block/buzz/pull/7791)
- [Integración de la implementación de artefactos de canal de Buzz](https://github.com/block/buzz/pull/7919)

**Mencionado en:**
- [Boletín #42: Artefactos de canal de Buzz](/es/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
