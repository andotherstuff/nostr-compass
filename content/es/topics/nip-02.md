---
title: "NIP-02: Lista de Seguidos"
date: 2025-12-24
translationOf: /en/topics/nip-02.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Social
---

NIP-02 define los eventos kind 3, que almacenan la lista de seguidos de un usuario. Este evento es la entrada base para feeds de inicio, notificaciones de respuestas y muchas estrategias de selección de relays.

## Cómo Funciona

Un evento kind 3 contiene etiquetas `p` que listan las pubkeys seguidas:

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

Cada etiqueta `p` tiene cuatro posiciones: el nombre de la etiqueta, la pubkey seguida (hex), una URL de relay opcional como pista, y un "petname" opcional (un apodo local). La pista del relay indica a otros clientes dónde encontrar los eventos de ese usuario. El petname permite asignar nombres memorables a contactos sin depender de sus nombres de perfil autodeclarados.

## Comportamiento Reemplazable

El kind 3 está en el rango reemplazable (0, 3, 10000-19999), por lo que los relays solo guardan la última versión por pubkey. Cuando sigues a alguien nuevo, tu cliente publica un kind 3 completamente nuevo que contiene todos tus seguidos más el nuevo. Esto significa que las listas de seguidos deben estar completas cada vez; no se pueden publicar actualizaciones incrementales.

## Por Qué Importa

Para construir un feed de inicio, los clientes obtienen el kind 3 del usuario, extraen todas las pubkeys de las etiquetas `p`, luego se suscriben a eventos kind 1 de esos autores:

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

El relay devuelve las notas coincidentes y el cliente las renderiza. Las pistas de relay en el kind 3 ayudan a los clientes a saber qué relays consultar para cada usuario seguido.

Este evento también es donde aparece primero el estado social obsoleto. Si el kind 3 más reciente de un usuario falta en los relays que consultas, su feed puede parecer vacío aunque sus seguidos aún existan en otro lugar. Los clientes que combinan resultados de múltiples relays generalmente se recuperan mejor que los clientes que confían en un solo relay.

## Petnames e Identidad

El campo petname habilita un esquema de nombres descentralizado. En lugar de confiar en cualquier nombre que un usuario declare en su perfil, puedes asignar tu propia etiqueta. Un cliente podría mostrar "alice (Mi Hermana)" donde "alice" viene de su perfil kind 0 y "Mi Hermana" es tu petname. Esto proporciona contexto que los nombres de usuario globales no pueden.

## Notas de Interoperabilidad

Debido a que los eventos kind 3 son reemplazables y deben estar completos, los clientes deben preservar las etiquetas desconocidas al actualizar. Si otro cliente añadió etiquetas que tu cliente no entiende, sobrescribir ciegamente perdería esos datos.

La misma precaución aplica a las pistas de relay y petnames. Son campos opcionales, pero descartarlos al escribir puede silenciosamente empeorar la experiencia de otro cliente. Una ruta de actualización segura es: cargar el kind 3 conocido más reciente, modificar solo las etiquetas que entiendes, conservar el resto, luego republicar el evento completo.

---

**Fuentes primarias:**
- [Especificación NIP-02](https://github.com/nostr-protocol/nips/blob/master/02.md)

**Mencionado en:**
- [Boletín #2: Análisis Profundo de NIP](/es/newsletters/2025-12-24-newsletter/#nip-02-follow-list)

**Ver también:**
- [NIP-01: Protocolo Básico](/es/topics/nip-01/)
- [NIP-10: Hilos de Notas de Texto](/es/topics/nip-10/)
- [NIP-65: Metadatos de Lista de Relays](/es/topics/nip-65/)
