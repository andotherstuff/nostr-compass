---
title: "NIP-85: Trusted Assertions"
date: 2026-02-18
translationOf: /en/topics/nip-85.md
translationDate: 2026-02-18
draft: false
categories:
  - Protocol
  - Web of Trust
---

NIP-85 define un sistema para delegar cálculos costosos a proveedores de servicios de confianza que publican resultados firmados como eventos Nostr. Las puntuaciones de Web of Trust y las métricas de engagement requieren rastrear muchos relays y procesar grandes volúmenes de eventos, un trabajo impracticable en dispositivos móviles o clientes de navegador.

## Cómo Funciona

Los usuarios designan proveedores de confianza para ejecutar los cálculos y publicar resultados como eventos estándar de Nostr. NIP-85 usa cuatro kinds de evento para aserciones sobre diferentes tipos de sujetos:

- **Kind 30382**: Aserciones de usuario — conteo de seguidores, conteos de publicaciones/respuestas/reacciones, montos de zap, rango normalizado (0-100), temas comunes y horas activas.
- **Kind 30383**: Aserciones de evento — califica notas individuales con conteo de comentarios, conteo de citas, reposts, reacciones y datos de zap.
- **Kind 30384**: Aserciones de eventos direccionables — aplica métricas de engagement a artículos de formato largo y páginas wiki a través de todas las versiones colectivamente.
- **Kind 30385**: Aserciones de identificadores externos — califica contenido externo (libros, películas, sitios web, ubicaciones, hashtags) referenciado a través de [NIP-73](/es/topics/nip-73/).

Cada aserción es un evento reemplazable direccionable donde la etiqueta `d` contiene el sujeto: una pubkey, ID de evento, dirección de evento o identificador NIP-73.

## Descubrimiento de Proveedores

Los usuarios declaran qué proveedores de aserciones confían publicando eventos kind 10040. Cada entrada especifica el tipo de aserción con la pubkey del proveedor y una sugerencia de relay, más variantes de algoritmo opcionales. Los usuarios pueden cifrar la lista de etiquetas en `.content` usando [NIP-44](/es/topics/nip-44/) para mantener privadas sus preferencias de proveedor.

## Modelo de Seguridad

Los proveedores deben usar claves de servicio diferentes para algoritmos distintos, y una clave única por usuario cuando los algoritmos son personalizados, evitando la correlación cruzada de consultas entre usuarios. Cada clave de servicio recibe un evento de metadatos kind 0 que describe el comportamiento del algoritmo. Los eventos de aserción solo deben actualizarse cuando los datos subyacentes cambian realmente.

## Adopción

NIP-85 formaliza un patrón que ya emergía de forma informal. El servidor de caché de Primal calcula métricas de engagement y puntuaciones de Web of Trust. [Antiprimal](https://gitlab.com/soapbox-pub/antiprimal) conecta estos cálculos a clientes Nostr estándar usando kinds de evento NIP-85. [Nostr.band](https://nostr.band) opera `wss://nip85.nostr.band` referenciado en los propios ejemplos de la spec. [Amethyst](https://github.com/vitorpamplona/amethyst) tiene soporte experimental de Aserciones de Confianza en su biblioteca `quartz`.

---

**Fuentes primarias:**
- [Especificación NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md)

**Mencionado en:**
- [Boletín #10: Actualizaciones de NIPs](/es/newsletters/2026-02-18-newsletter/#actualizaciones-de-nips)
- [Boletín #10: Análisis Profundo NIP-85](/es/newsletters/2026-02-18-newsletter/#análisis-profundo-de-nip-nip-85-aserciones-de-confianza)

**Ver también:**
- [Trusted Relay Assertions](/es/topics/trusted-relay-assertions/)
- [NIP-73: External Content IDs](/es/topics/nip-73/)
- [NIP-44: Encrypted Payloads](/es/topics/nip-44/)
