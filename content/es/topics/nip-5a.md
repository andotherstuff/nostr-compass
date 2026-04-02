---
title: "NIP-5A: Sitios Web Estáticos"
date: 2026-04-01
translationOf: /en/topics/nip-5a.md
translationDate: 2026-04-01
draft: false
categories:
  - Protocol
  - Hosting
---

NIP-5A define cómo alojar sitios web estáticos bajo claves Nostr. Los autores de sitios publican eventos de manifiesto firmados que mapean rutas URL a hashes SHA256 de contenido, y los servidores host resuelven esos manifiestos para servir los archivos del sitio desde almacenamiento Blossom.

## Cómo Funciona

La especificación usa dos kinds de evento. Kind `15128` es un manifiesto de sitio raíz, uno por pubkey, que sirve como el sitio web predeterminado para esa clave. Kind `35128` es un manifiesto de sitio nombrado, identificado por una etiqueta `d`, que actúa como un subdominio. Cada manifiesto contiene etiquetas `path` que mapean rutas URL absolutas a hashes SHA256 de los archivos que deben servirse.

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

Un servidor host recibe una solicitud HTTP, extrae la pubkey del autor del subdominio, obtiene el manifiesto del sitio de la lista de relays del autor, resuelve la ruta solicitada a un hash de contenido, y descarga el blob correspondiente del servidor o servidores Blossom listados en las etiquetas `server`.

## Resolución de URL

Los sitios raíz usan el npub como subdominio. Los sitios nombrados usan una codificación base36 de 50 caracteres de la pubkey en bruto seguida del valor de la etiqueta `d`, todo en una sola etiqueta DNS. Dado que las etiquetas DNS están limitadas a 63 caracteres y la pubkey en base36 siempre usa 50, los identificadores de sitio nombrado están limitados a 13 caracteres.

## Implementaciones

- [nsite](https://github.com/lez/nsite) - Servidor host que resuelve manifiestos NIP-5A y sirve archivos
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - UI para construir y publicar manifiestos de sitio

---

**Fuentes primarias:**
- [Especificación NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md)
- [PR #1538](https://github.com/nostr-protocol/nips/pull/1538) - Propuesta original y fusión
- [nsite](https://github.com/lez/nsite) - Implementación de referencia del host
- [nsite-manager](https://github.com/hzrd149/nsite-manager) - UI de publicación y gestión

**Mencionado en:**
- [Newsletter #16: NIP-5A se fusiona](/es/newsletters/2026-04-01-newsletter/#nip-5a-se-fusiona-trayendo-sitios-web-estáticos-a-nostr)
- [Newsletter #16: NIP Deep Dive](/es/newsletters/2026-04-01-newsletter/#nip-deep-dive-nip-5a-sitios-web-estáticos)

**Ver también:**
- [Blossom](/es/topics/blossom/)
- [NIP-65: Relay List Metadata](/es/topics/nip-65/)
- [NIP-96: HTTP File Storage](/es/topics/nip-96/)
