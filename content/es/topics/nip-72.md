---
title: "NIP-72: Comunidades Moderadas"
date: 2026-03-25
translationOf: /en/topics/nip-72.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Communities
---

NIP-72 define comunidades moderadas en Nostr. Las comunidades proporcionan una forma de organizar publicaciones alrededor de un tema o grupo compartido, con moderadores que aprueban contenido antes de que sea visible para los miembros.

## Cómo Funciona

Una comunidad se define por un evento kind 34550 publicado por su creador. Este evento contiene el nombre de la comunidad, descripción, reglas y una lista de pubkeys de moderadores. El evento usa un formato de evento reemplazable (rango kind 30000-39999), por lo que la definición de la comunidad puede actualizarse con el tiempo.

```json
{
  "kind": 34550,
  "tags": [
    ["d", "example-community"],
    ["name", "Example Community"],
    ["description", "A community for discussing examples"],
    ["p", "<moderator_pubkey>", "", "moderator"],
    ["relay", "wss://relay.example.com", "moderator"]
  ],
  "content": "",
  "pubkey": "<creator_pubkey>",
  "created_at": 1742860800,
  "sig": "<signature>"
}
```

Los usuarios envían publicaciones a una comunidad etiquetando sus eventos con una etiqueta `a` que apunta a la definición de la comunidad. Estas publicaciones aún no son visibles para los lectores de la comunidad. Un moderador revisa el envío y, si lo aprueba, publica un evento de aprobación kind 4549 que envuelve la publicación original. Los clientes que muestran la comunidad solo presentan publicaciones que tienen un evento de aprobación correspondiente de un moderador reconocido.

Este modelo de aprobación significa que las comunidades tienen filtrado de lectura, no restricción de escritura. Cualquiera puede enviar una publicación, pero solo las publicaciones aprobadas aparecen en el feed de la comunidad. Los moderadores actúan como curadores en lugar de guardianes de los datos subyacentes.

## Consideraciones

Dado que los eventos de aprobación son eventos Nostr separados, las decisiones de moderación son transparentes y auditables. Una publicación rechazada por una comunidad aún puede ser aprobada por otra. El mismo contenido puede existir en múltiples comunidades con moderación independiente.

El soporte de relay importa para la funcionalidad de comunidades. Los clientes necesitan consultar tanto la definición de la comunidad como los eventos de aprobación, lo que requiere relays que indexen estos kinds de evento eficientemente.

---

**Fuentes primarias:**
- [Especificación NIP-72](https://github.com/nostr-protocol/nips/blob/master/72.md) - Comunidades Moderadas

**Mencionado en:**
- [Newsletter #15](/es/newsletters/2026-03-25-newsletter/)
