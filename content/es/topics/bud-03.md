---
title: "BUD-03: Lista de Servidores del Usuario"
date: 2025-12-17
translationOf: /en/topics/bud-03.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---

BUD-03 define cómo un usuario publica sus servidores Blossom preferidos, para que los clientes sepan dónde subir blobs y dónde buscar cuando una URL de medios deja de funcionar.

## Cómo Funciona

Los usuarios publican un evento reemplazable kind `10063` con una o más etiquetas `server`. Cada etiqueta contiene una URL completa de servidor Blossom.

Los clientes pueden entonces:
- subir blobs a los servidores preferidos del usuario
- descubrir ubicaciones probables de blobs a partir de la pubkey del autor
- reintentar la recuperación desde los servidores listados cuando una URL antigua falla

## Detalles Útiles para el Lector

El orden de las etiquetas `server` importa. La especificación dice que los usuarios deben listar primero sus servidores más confiables o fiables, y los clientes deben al menos intentar con el primer servidor para las subidas. Eso significa que BUD-03 no es solo un directorio, sino también una señal débil de preferencia.

La guía de recuperación también es práctica: cuando un cliente extrae un hash de blob de una URL, debe usar la última cadena hexadecimal de 64 caracteres en la ruta. Esto ayuda a los clientes a recuperar blobs tanto de URLs Blossom estándar como de URLs estilo CDN no estándar que aún incrustan el hash.

---

**Fuentes primarias:**
- [Especificación BUD-03](https://github.com/hzrd149/blossom/blob/master/buds/03.md)
- [Repositorio de Blossom](https://github.com/hzrd149/blossom)

**Mencionado en:**
- [Boletín #1: Noticias](/es/newsletters/2025-12-17-newsletter/#news)

**Ver también:**
- [Protocolo Blossom](/es/topics/blossom/)
- [NIP-51: Listas](/es/topics/nip-51/)
