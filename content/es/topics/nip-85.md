---
title: "NIP-85: Trusted Assertions"
date: 2026-02-18
translationOf: /en/topics/nip-85.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Trust
  - Infrastructure
---

NIP-85 define Trusted Assertions, un sistema para delegar cálculos costosos a proveedores de servicios de confianza que publican resultados firmados como eventos Nostr.

## Cómo Funciona

Las puntuaciones de Web of Trust, métricas de engagement y otros valores computados requieren rastrear muchos relays y procesar grandes volúmenes de eventos. Este trabajo es impracticable en dispositivos móviles. NIP-85 permite que proveedores especializados realicen estos cálculos y publiquen resultados que los clientes pueden consultar.

Las Trusted Assertions son eventos direccionables. La etiqueta `d` identifica el sujeto que se está puntuando, y el kind del evento identifica qué tipo de sujeto es: pubkeys (30382), eventos regulares (30383), eventos direccionables (30384) e identificadores NIP-73 (30385).

Los usuarios declaran en qué proveedores confían a través de kind 10040. Esas listas de proveedores pueden ser públicas en etiquetas o cifradas en el contenido del evento con [NIP-44](/es/topics/nip-44/), lo cual importa cuando un usuario no quiere publicar sus inputs de confianza abiertamente.

## Por Qué Importa

La idea clave en NIP-85 es que estandariza las salidas, no los algoritmos. Dos proveedores pueden ambos publicar una etiqueta `rank` para la misma pubkey mientras usan diferentes fórmulas de Web of Trust, manejo de silencios, cobertura de relays o heurísticas anti-spam. Los clientes mantienen la interoperabilidad porque el formato del resultado coincide incluso cuando la computación no.

Eso encaja mejor en Nostr que pretender que habrá un único servicio de ranking canónico. Los usuarios eligen en qué aserciones confiar.

## Modelo de Confianza

Los proveedores de servicio deben firmar sus propios eventos de aserción, y la especificación recomienda diferentes claves de servicio para diferentes algoritmos o puntos de vista específicos del usuario. Eso evita que un proveedor colapse sistemas de ranking no relacionados en una única identidad opaca.

La confianza sigue siendo local. La salida firmada prueba qué proveedor publicó una puntuación, no que la puntuación sea correcta. Los clientes necesitan políticas sobre qué claves de proveedor usar, de qué relays obtener datos, y cómo manejar aserciones en conflicto.

## Notas de Interoperabilidad

NIP-85 se extiende más allá de personas y publicaciones. El kind 30385 permite a los proveedores puntuar identificadores externos NIP-73 como libros, sitios web, hashtags y ubicaciones. Eso crea un camino para datos de reputación y engagement interoperables sobre sujetos fuera de Nostr mismo.

---

**Fuentes primarias:**
- [Especificación NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #2223](https://github.com/nostr-protocol/nips/pull/2223) - Guía de descubribilidad de proveedores de servicio

**Mencionado en:**
- [Newsletter #10: Análisis Profundo NIP-85](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Newsletter #11: Descubribilidad de Proveedores NIP-85](/en/newsletters/2026-02-25-newsletter/#nip-updates)
- [Newsletter #12: Recapitulación de Protocolo](/en/newsletters/2026-03-04-newsletter/)

**Ver también:**
- [NIP-44: Payloads Cifrados](/es/topics/nip-44/)
- [NIP-73: IDs de Contenido Externo](/es/topics/nip-73/)
- [Web of Trust](/es/topics/web-of-trust/)
