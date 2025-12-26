---
title: "NIP-10: Hilos de Notas de Texto"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-10 especifica cómo las notas kind 1 se referencian entre sí para formar hilos de respuestas. Entender esto es esencial para construir vistas de conversación.

## El Problema

Cuando alguien responde a una nota, los clientes necesitan saber: ¿A qué es esto una respuesta? ¿Cuál es la raíz de la conversación? ¿Quién debe ser notificado? NIP-10 responde estas preguntas a través de etiquetas `e` (referencias a eventos) y etiquetas `p` (menciones de pubkey).

## Etiquetas Marcadas (Preferido)

Los clientes modernos usan marcadores explícitos en las etiquetas `e`:

```json
{
  "id": "f9c2e...",
  "pubkey": "a3b9c...",
  "created_at": 1734912345,
  "kind": 1,
  "tags": [
    ["e", "abc123...", "wss://relay.example.com", "root"],
    ["e", "def456...", "wss://relay.example.com", "reply"],
    ["p", "91cf9..."],
    ["p", "14aeb..."]
  ],
  "content": "¡Buen punto! Estoy de acuerdo.",
  "sig": "b7d3f..."
}
```

El marcador `root` apunta a la nota original que inició el hilo. El marcador `reply` apunta a la nota específica que se está respondiendo. Si respondes directamente a la raíz, usa solo `root` (no se necesita etiqueta `reply`). La distinción importa para el renderizado: el `reply` determina la indentación en una vista de hilo, mientras que `root` agrupa todas las respuestas juntas.

## Reglas de Hilos

- **Respuesta directa a la raíz:** Una etiqueta `e` con marcador `root`
- **Respuesta a una respuesta:** Dos etiquetas `e`, una `root` y una `reply`
- El `root` permanece constante a lo largo del hilo; `reply` cambia según a qué estés respondiendo

## Etiquetas Pubkey para Notificaciones

Incluye etiquetas `p` para todos los que deben ser notificados. Como mínimo, etiqueta al autor de la nota a la que estás respondiendo. La convención es también incluir todas las etiquetas `p` del evento padre (para que todos en la conversación se mantengan al tanto), más cualquier usuario que @menciones en tu contenido.

## Pistas de Relay

La tercera posición en las etiquetas `e` y `p` puede contener una URL de relay donde se puede encontrar ese evento o el contenido del usuario. Esto ayuda a los clientes a obtener el contenido referenciado incluso si no están conectados al relay original.

## Etiquetas Posicionales Obsoletas

Las implementaciones tempranas de Nostr inferían el significado de la posición de la etiqueta en lugar de los marcadores: la primera etiqueta `e` era la raíz, la última era la respuesta, las del medio eran menciones. Este enfoque está obsoleto porque crea ambigüedad. Si ves etiquetas `e` sin marcadores, probablemente son de clientes antiguos. Las implementaciones modernas siempre deben usar marcadores explícitos.

## Construyendo Vistas de Hilo

Para mostrar un hilo, obtén el evento raíz, luego consulta todos los eventos con una etiqueta `e` que referencie esa raíz:

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

Ordena los resultados por `created_at` y usa los marcadores `reply` para construir la estructura de árbol. Los eventos cuyo `reply` apunta a la raíz son respuestas de nivel superior; los eventos cuyo `reply` apunta a otra respuesta son respuestas anidadas.

---

**Fuentes primarias:**
- [Especificación NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md)

**Mencionado en:**
- [Boletín #2: Análisis Profundo de NIP](/es/newsletters/2025-12-24-newsletter/#nip-10-text-note-threading)

**Ver también:**
- [NIP-01: Protocolo Básico](/es/topics/nip-01/)
