---
title: "NIP-37: Envolturas de borradores"
date: 2026-07-01
draft: false
translationOf: /en/topics/nip-37.md
translationDate: 2026-07-01
categories:
  - NIP
  - Drafts
  - Privacy
---

NIP-37 define un evento de almacenamiento cifrado para eventos de borrador sin firmar de cualquier kind. Un usuario que redacta un artículo de formato largo, un próximo evento de calendario o un mensaje que puede querer enviar más tarde puede almacenar el borrador en los relays bajo un evento de kind `31234`, cifrado a su propia clave con [NIP-44](/es/topics/nip-44/). El borrador es recuperable desde cualquier cliente que posea la clave del usuario, y el mismo NIP define un evento de lista `kind:10013` separado que nombra los relays en los que el usuario desea almacenar sus borradores privados.

## Cómo funciona

Una envoltura de borrador es un evento parametrizado reemplazable de kind `31234`. El evento borrador sin firmar se convierte a JSON, se cifra con NIP-44 a la clave pública del firmante y se coloca en `.content`. Un tag `k` declara el kind del borrador para que un cliente pueda agrupar borradores por tipo de evento. Un tag `d` transporta el identificador del borrador para que la envoltura pueda ser reemplazada a medida que el borrador evoluciona, y se recomienda un tag `expiration` NIP-40 para que los borradores antiguos caduquen automáticamente.

```json
{
  "kind": 31234,
  "tags": [
    ["d", "<identifier>"],
    ["k", "<kind of the draft event>"],
    ["expiration", "<unix-timestamp>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

Un campo `.content` en blanco indica que el borrador ha sido eliminado.

## Puntos de control

El kind `1234` define puntos de control pertenecientes a un evento padre `kind:31234`. Los puntos de control llevan un tag `a` que apunta al borrador padre y permiten a un cliente almacenar el historial de revisiones junto con el borrador más reciente.

```json
{
  "kind": 1234,
  "tags": [
    ["a", "31234:<pubkey>:<identifier>"]
  ],
  "content": "<nip44Encrypt(JSON.stringify(draft_event))>"
}
```

## Lista de relays para contenido privado (kind 10013)

El kind `10013` es un evento reemplazable cuyos tags listan los relays en los que el usuario quiere almacenar contenido privado, incluidas las envolturas de borradores. Los clientes que publican kind `31234` DEBERÍAN publicar en los relays listados en el evento kind `10013` del usuario. Esto separa el conjunto de relays usados para publicaciones públicas (NIP-65) del conjunto de relays usado para almacenamiento de contenido privado, para que un usuario pueda fijar borradores privados a un conjunto pequeño de relays de confianza sin exponer ese conjunto en su outbox público.

## Implementaciones

- [Notedeck](https://github.com/damus-io/notedeck) - almacena los relays de sincronización privada como una lista kind-10013 (añadido en 2026-06)

---

**Fuentes primarias:**
- [Especificación NIP-37](https://github.com/nostr-protocol/nips/blob/master/37.md)
- [Commit de Notedeck que almacena relays de sincronización privada como kind-10013](https://github.com/damus-io/notedeck) - El equipo de Damus adopta la especificación para la gestión de relays de sincronización en escritorio

**Mencionado en:**
- [Boletín #29: Notedeck](/es/newsletters/2026-07-01-newsletter/#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments)

**Véase también:**
- [NIP-44: Cifrado versionado](/es/topics/nip-44/)
- [NIP-65: Metadatos de lista de relays](/es/topics/nip-65/)
