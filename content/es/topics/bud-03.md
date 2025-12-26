---
title: "BUD-03: Lista de Servidores del Usuario"
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-03 define cómo los usuarios publican sus servidores Blossom preferidos, habilitando a los clientes a descubrir dónde subir y recuperar los archivos de medios de un usuario.

## Cómo Funciona

Los usuarios publican un evento kind 10063 listando sus servidores Blossom. Los clientes pueden entonces:
- Subir medios a los servidores preferidos del usuario
- Descubrir dónde encontrar los blobs de un usuario dada su pubkey

Esto habilita el descubrimiento basado en autor como alternativa a incrustar URLs de servidor directamente en el contenido.

---

**Fuentes primarias:**
- [Especificación BUD-03](https://github.com/hzrd149/blossom/blob/master/buds/03.md)

**Ver también:**
- [Protocolo Blossom](/es/topics/blossom/)
- [NIP-51: Listas](/es/topics/nip-51/)
