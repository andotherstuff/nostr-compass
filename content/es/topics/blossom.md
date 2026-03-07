---
title: "Protocolo Blossom"
date: 2025-12-17
translationOf: /en/topics/blossom.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---

Blossom es un protocolo de alojamiento de medios para Nostr que almacena blobs en servidores HTTP ordinarios y los direcciona por hash SHA-256 en lugar de IDs asignados por el servidor.

## Cómo Funciona

Los servidores Blossom exponen una interfaz HTTP pequeña para recuperación, subida y gestión de blobs. El identificador canónico es el hash del archivo, por lo que el mismo blob mantiene la misma dirección en cada servidor compatible.

- `GET /<sha256>` recupera un blob por hash
- `PUT /upload` sube un blob
- Los eventos Nostr kind `24242` autorizan subidas y acciones de gestión
- Los eventos kind `10063`, definidos en [BUD-03](/es/topics/bud-03/), permiten a los usuarios publicar sus servidores preferidos

Como el hash es el identificador, los clientes pueden verificar la integridad localmente después de la descarga y pueden intentar con otro servidor sin cambiar la referencia subyacente.

## Por Qué Es Importante

Blossom separa el almacenamiento de blobs de los eventos sociales. Una nota o perfil puede apuntar a medios sin vincularlos al diseño de URL de un solo host.

Esto también cambia el manejo de fallos. Si un servidor desaparece, los clientes pueden obtener el mismo hash de un mirror, una caché o un servidor descubierto a través de la lista [BUD-03](/es/topics/bud-03/) del autor. Eso es una mejora práctica respecto a sistemas de medios donde la URL del host original es el único localizador.

## Notas de Interoperabilidad

Blossom es modular. El comportamiento básico de recuperación y subida reside en BUD-01 y BUD-02, mientras que el mirroring, la optimización de medios, la autorización y el compartir URIs se dividen en BUDs separados.

Esa separación permite a los clientes implementar lo mínimo necesario para interoperabilidad básica, y luego añadir piezas opcionales como las pistas URI de [BUD-10](/es/topics/bud-10/) o caché local conforme el soporte madura.

---

**Fuentes primarias:**
- [Repositorio de Blossom](https://github.com/hzrd149/blossom)
- [BUD-01: Requisitos de servidor y recuperación de blobs](https://github.com/hzrd149/blossom/blob/master/buds/01.md)
- [BUD-02: Subida y gestión de blobs](https://github.com/hzrd149/blossom/blob/master/buds/02.md)
- [Guía de caché local de Blossom](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md)

**Mencionado en:**
- [Boletín #1: Noticias](/es/newsletters/2025-12-17-newsletter/#news)
- [Boletín #2: Cambios Notables de Código y Documentación](/es/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)
- [Boletín #10: Emerge la capa de caché local de Blossom](/es/newsletters/2026-02-18-newsletter/#blossom-local-cache-layer-emerges)

**Ver también:**
- [BUD-03: Lista de Servidores del Usuario](/es/topics/bud-03/)
- [BUD-10: Esquema URI de Blossom](/es/topics/bud-10/)
