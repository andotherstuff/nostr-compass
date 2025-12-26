---
title: "BUD-10: Esquema URI de Blossom"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-10 define un esquema URI personalizado para Blossom que incluye toda la información necesaria para recuperar un archivo de cualquier servidor disponible.

## Formato de URI

```
blossom:<sha256>.<ext>?size=<bytes>&server=<url>&server=<url>&pubkey=<hex>
```

Componentes:
- **sha256**: Hash del archivo (requerido)
- **ext**: Extensión del archivo
- **size**: Tamaño del archivo en bytes
- **server**: Una o más pistas de servidor
- **pubkey**: Pubkeys de autor para descubrimiento de servidor BUD-03

## Beneficios

- Más resiliente que URLs HTTP estáticas
- Fallback automático a través de múltiples servidores
- Descubrimiento basado en autor vía pistas de pubkey
- Auto-verificable (el hash asegura integridad)

---

**Fuentes primarias:**
- [PR de BUD-10](https://github.com/hzrd149/blossom/pull/84)

**Mencionado en:**
- [Boletín #1: Noticias](/es/newsletters/2025-12-17-newsletter/#news)

**Ver también:**
- [Protocolo Blossom](/es/topics/blossom/)
- [BUD-03: Lista de Servidores del Usuario](/es/topics/bud-03/)
