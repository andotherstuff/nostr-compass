---
title: "NIP-33: Eventos Reemplazables Parametrizados (Eventos Direccionables)"
date: 2026-03-11
translationOf: /en/topics/nip-33.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-33 originalmente definió los eventos reemplazables parametrizados, una clase de eventos donde solo un evento por tupla `(pubkey, kind, d-tag)` es retenido por los relays. El concepto ha sido renombrado desde entonces a "eventos direccionables" e incorporado en [NIP-01](/es/topics/nip-01/). El documento NIP-33 ahora redirige a NIP-01 pero sigue siendo una referencia común en bases de código y documentación.

## Cómo Funciona

Un evento direccionable usa un kind en el rango `30000-39999`. Cada evento lleva una etiqueta `d` cuyo valor, junto con la pubkey del autor y el número de kind, forma una dirección única. Cuando un relay recibe un nuevo evento que coincide con una tupla `(pubkey, kind, d-tag)` existente, reemplaza el evento más antiguo con el más nuevo (por `created_at`). Esto hace que los eventos direccionables sean útiles para estado mutable: perfiles, configuraciones, datos de aplicaciones, listados clasificados y estructuras similares donde solo importa la última versión.

Los clientes referencian eventos direccionables con etiquetas `a` en el formato `<kind>:<pubkey>:<d-tag>`, opcionalmente seguido de una pista de relay.

## Usos Comunes

- Kind `30023` artículos de formato largo
- Kind `30078` datos específicos de aplicación (usado por NIP-78)
- Kind `31923` eventos de calendario (NIP-52)
- Kind `31990` recomendaciones de manejadores (NIP-89)
- Kind `30009` definiciones de insignias (NIP-58)
- Kind `31991` configuraciones de ejecución de agentes (Notedeck Agentium)

## Relación con NIP-01

NIP-33 fue fusionado en NIP-01 como parte de un esfuerzo de consolidación. La especificación de NIP-01 ahora define tres categorías de retención de eventos: eventos regulares (se mantienen tal cual), eventos reemplazables (uno por `(pubkey, kind)`), y eventos direccionables (uno por `(pubkey, kind, d-tag)`). NIP-33 sigue siendo una forma abreviada válida para el concepto de evento direccionable.

---

**Fuentes primarias:**
- [NIP-33 (redirección)](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [Especificación NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) - Sección de eventos direccionables

**Mencionado en:**
- [Newsletter #13: Notedeck](/en/newsletters/2026-03-11-newsletter/#notedeck-adds-nip-11-relay-limits-and-agentium-features)

**Ver también:**
- [NIP-01: Protocolo Básico](/es/topics/nip-01/)
