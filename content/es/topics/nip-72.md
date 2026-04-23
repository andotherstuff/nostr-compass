---
title: "NIP-72: Comunidades Moderadas"
date: 2026-03-25
translationOf: /en/topics/nip-72.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Communities
---

NIP-72 define comunidades moderadas en Nostr. Las comunidades proporcionan una forma de organizar publicaciones alrededor de un tema o grupo compartido, con moderadores que aprueban contenido antes de que sea visible para los miembros.

## Cómo funciona

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

Comparado con los grupos basados en relay de [NIP-29](/es/topics/nip-29/), donde el relay es la autoridad tanto para membresía como para moderación, NIP-72 vive en eventos Nostr normales. Cualquier relay que transporte kinds `34550`, `4549` y los kinds de envío puede servir una comunidad, y la moderación es visible y bifurcable. El tradeoff es que los envíos no aprobados solo quedan ocultos en la capa de renderizado del cliente, así que NIP-29 sigue siendo mejor cuando el spam no debe llegar a la red en absoluto.

## Implementaciones

- [noStrudel](https://github.com/hzrd149/nostrudel) tiene soporte de larga data para comunidades NIP-72, incluyendo una cola de envíos pendientes para moderadores.
- [Amethyst](https://github.com/vitorpamplona/amethyst) añadió creación y gestión de comunidades de primera clase en [PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468): creación de la definición de comunidad kind `34550`, adición de moderadores y relay hints, envío de publicaciones con una etiqueta `a` y gestión de aprobaciones pendientes mediante eventos kind `4549`.

---

**Fuentes primarias:**
- [Especificación NIP-72](https://github.com/nostr-protocol/nips/blob/master/72.md) - Comunidades Moderadas
- [Amethyst PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) - creación y moderación de comunidades NIP-72

**Mencionado en:**
- [Newsletter #15](/es/newsletters/2026-03-25-newsletter/)

- [Newsletter #19: soporte de comunidades en Amethyst](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NIP Deep Dive](/en/newsletters/2026-04-22-newsletter/)

**Ver también:**
- [NIP-29: Grupos basados en relay](/es/topics/nip-29/)
