---
title: "NIP-85"
date: 2026-02-18
translationOf: /en/topics/nip-85.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - Trust
  - Infrastructure
---

NIP-85 define Trusted Assertions, un sistema para delegar cálculos costosos a proveedores de servicios de confianza que publican resultados firmados como eventos Nostr.

## Cómo Funciona

Las puntuaciones de Web of Trust, métricas de engagement y otros valores computados requieren rastrear muchos relays y procesar grandes volúmenes de eventos. Este trabajo es impracticable en dispositivos móviles. NIP-85 permite que proveedores especializados realicen estos cálculos y publiquen resultados que los clientes pueden consultar.

Los proveedores de servicio anuncian sus capacidades mediante eventos kind 30085. Los clientes descubren proveedores consultando estos anuncios en relays desde pubkeys que el usuario ya sigue o confía. Los resultados llegan como eventos kind 30382 firmados por el proveedor.

## Características Clave

- Computación delegada para métricas que requieren muchos recursos
- Descubrimiento de proveedores a través del grafo social
- Aserciones firmadas para resultados verificables
- Decisiones de confianza del lado del cliente

---

**Fuentes primarias:**
- [Especificación NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md)

**Mencionado en:**
- [Boletín #10: Análisis Profundo NIP-85](/es/newsletters/2026-02-18-newsletter/#análisis-profundo-de-nip-nip-85-aserciones-de-confianza)
- [Boletín #11: Descubribilidad de Proveedores NIP-85](/es/newsletters/2026-02-25-newsletter/#actualizaciones-de-nips)

**Ver también:**
- [Web of Trust](/es/topics/web-of-trust/)
