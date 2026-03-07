---
title: "BUD-10: Esquema URI de Blossom"
date: 2025-12-17
translationOf: /en/topics/bud-10.md
translationDate: 2026-03-07
draft: false
categories:
  - Media
  - Protocol
---

BUD-10 define el esquema URI `blossom:`, una referencia portable de blob que puede llevar pistas de servidor, pistas de autor y tamaño esperado junto al hash del archivo.

## Formato de URI

```
blossom:<sha256>.<ext>?xs=<server>&as=<pubkey>&sz=<bytes>
```

La especificación requiere un hash SHA-256 en minúsculas de 64 caracteres y una extensión de archivo. Si la extensión es desconocida, los clientes deben recurrir a `.bin`.

## Cómo Funciona la Resolución

Los clientes deben resolver un URI `blossom:` en etapas:

1. Intentar con las pistas de servidor `xs` en el orden en que aparecen
2. Si hay pubkeys de autor `as` presentes, obtener la lista de servidores [BUD-03](/es/topics/bud-03/) de cada autor e intentar esos servidores
3. Recurrir a servidores conocidos o caché local si es necesario

Ese orden es útil porque permite al remitente adjuntar pistas inmediatas para recuperación rápida, mientras sigue dando a los receptores una ruta de recuperación si esas pistas se vuelven obsoletas.

## Por Qué Es Importante

Los URIs `blossom:` funcionan más como enlaces magnet que como URLs de medios ordinarias. Describen qué blob obtener e incluyen pistas sobre dónde encontrarlo, en lugar de asumir que un host permanecerá disponible para siempre.

El campo opcional `sz` añade una verificación de integridad concreta más allá del hash. Los clientes pueden verificar el tamaño esperado antes o después de la descarga, lo que ayuda a detectar transferencias incompletas y mejora la experiencia de usuario para medios grandes.

---

**Fuentes primarias:**
- [Especificación BUD-10](https://github.com/hzrd149/blossom/blob/master/buds/10.md)
- [Repositorio de Blossom](https://github.com/hzrd149/blossom)

**Mencionado en:**
- [Boletín #1: Noticias](/es/newsletters/2025-12-17-newsletter/#news)

**Ver también:**
- [Protocolo Blossom](/es/topics/blossom/)
- [BUD-03: Lista de Servidores del Usuario](/es/topics/bud-03/)
