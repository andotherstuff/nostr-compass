---
title: "NIP-02: Lista de Seguidos"
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-02 define los eventos kind 3, que almacenan tu lista de seguidos. Este mecanismo simple impulsa el grafo social que hace posibles las líneas de tiempo.

## Estructura

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

Cada etiqueta `p` tiene cuatro posiciones: el nombre de la etiqueta, la pubkey seguida (hex), una URL de relay opcional como pista, y un "petname" opcional (un apodo local). La pista del relay indica a otros clientes dónde encontrar los eventos de ese usuario. El petname te permite asignar nombres memorables a contactos sin depender de sus nombres de perfil autodeclarados.

## Comportamiento Reemplazable

El kind 3 está en el rango reemplazable (0, 3, 10000-19999), por lo que los relays solo guardan la última versión por pubkey. Cuando sigues a alguien nuevo, tu cliente publica un kind 3 completamente nuevo que contiene todos tus seguidos más el nuevo. Esto significa que las listas de seguidos deben estar completas cada vez; no puedes publicar actualizaciones incrementales.

## Construyendo Líneas de Tiempo

Para construir un feed de inicio, los clientes obtienen el kind 3 del usuario, extraen todas las pubkeys de las etiquetas `p`, luego se suscriben a eventos kind 1 de esos autores:

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

El relay devuelve las notas coincidentes y el cliente las renderiza. Las pistas de relay en el kind 3 ayudan a los clientes a saber qué relays consultar para cada usuario seguido.

## Petnames e Identidad

El campo petname habilita un esquema de nombres descentralizado. En lugar de confiar en cualquier nombre que un usuario declare en su perfil, puedes asignar tu propia etiqueta. Un cliente podría mostrar "alice (Mi Hermana)" donde "alice" viene de su perfil kind 0 y "Mi Hermana" es tu petname. Esto proporciona contexto que los nombres de usuario globales no pueden.

## Consideraciones Prácticas

Debido a que los eventos kind 3 son reemplazables y deben estar completos, los clientes deben preservar las etiquetas desconocidas al actualizar. Si otro cliente agregó etiquetas que tu cliente no entiende, sobrescribir ciegamente perdería esos datos. Agrega nuevos seguidos en lugar de reconstruir desde cero.

---

**Fuentes primarias:**
- [Especificación NIP-02](https://github.com/nostr-protocol/nips/blob/master/02.md)

**Mencionado en:**
- [Boletín #2: Análisis Profundo de NIP](/es/newsletters/2025-12-24-newsletter/#nip-02-follow-list)

**Ver también:**
- [NIP-01: Protocolo Básico](/es/topics/nip-01/)
