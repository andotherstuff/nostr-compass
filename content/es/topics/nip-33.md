---
title: "NIP-33: Eventos reemplazables parametrizados (eventos direccionables)"
date: 2026-03-11
translationOf: /en/topics/nip-33.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Protocol
---

NIP-33 definió originalmente los eventos reemplazables parametrizados, una clase de eventos en la que los relays conservan solo un evento por tupla `(pubkey, kind, d-tag)`. Desde entonces, el concepto pasó a llamarse "eventos direccionables" y se integró en [NIP-01](/es/topics/nip-01/). El documento de NIP-33 ahora redirige a NIP-01, pero sigue siendo una referencia común en bases de código y documentación.

## Cómo funciona

Un evento direccionable usa un kind en el rango `30000-39999`. Cada evento lleva una etiqueta `d` cuyo valor, junto con la pubkey del autor y el número de kind, forma una dirección única. Cuando un relay recibe un nuevo evento que coincide con una tupla `(pubkey, kind, d-tag)` existente, reemplaza el evento anterior por el más nuevo (según `created_at`). Esto hace que los eventos direccionables sean útiles para estado mutable: perfiles, ajustes, configuraciones de apps, anuncios clasificados y estructuras similares en las que solo importa la versión más reciente.

Los clientes hacen referencia a los eventos direccionables con etiquetas `a` en el formato `<kind>:<pubkey>:<d-tag>`, opcionalmente seguidas de una pista de relay.

## Usos comunes

- Artículos de formato largo kind `30023`
- Datos específicos de aplicación kind `30078` (usados por NIP-78)
- Eventos de calendario kind `31923` (NIP-52)
- Recomendaciones de handlers kind `31990` (NIP-89)
- Definiciones de insignias kind `30009` (NIP-58)
- Configuraciones de ejecución de agentes kind `31991` (Notedeck Agentium)

## Relación con NIP-01

NIP-33 se fusionó en NIP-01 como parte de un esfuerzo de consolidación. La especificación de NIP-01 ahora define tres categorías de retención de eventos: eventos regulares (se conservan tal cual), eventos reemplazables (uno por `(pubkey, kind)`) y eventos direccionables (uno por `(pubkey, kind, d-tag)`). NIP-33 sigue siendo una abreviatura válida para el concepto de evento direccionable.

---

**Fuentes primarias:**
- [NIP-33 (redirección)](https://github.com/nostr-protocol/nips/blob/master/33.md)
- [Especificación de NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) - Sección de eventos direccionables

**Mencionado en:**
- [Newsletter #13: Notedeck](/es/newsletters/2026-03-11-newsletter/#notedeck-anade-limites-de-relay-nip-11-y-funciones-de-agentium)

**Ver también:**
- [NIP-01: Protocolo básico](/es/topics/nip-01/)
