---
title: "NIP-29: Grupos Basados en Relay"
date: 2025-12-24
draft: false
categories:
  - Social
  - Groups
---

NIP-29 define grupos basados en relay, donde un relay gestiona la membresía del grupo, permisos y visibilidad de mensajes.

## Etiquetas de Acceso a Grupos

- **private**: Solo los miembros pueden leer los mensajes del grupo
- **closed**: Las solicitudes de unión se ignoran (solo por invitación)
- **hidden**: El relay oculta los metadatos del grupo de los no miembros, haciendo el grupo no descubrible
- **restricted**: Solo los miembros pueden escribir mensajes al grupo

Estas etiquetas se pueden combinar. Un grupo puede ser `restricted` (escritura limitada) pero no `hidden` (todavía descubrible). Omitir una etiqueta habilita el comportamiento opuesto: sin `private` significa que cualquiera puede leer, sin `closed` significa que las solicitudes de unión se respetan.

## Cómo Funciona

El relay es la autoridad para las operaciones del grupo:
- Mantiene la lista de miembros y roles
- Aplica los permisos de escritura
- Controla lo que los no miembros pueden ver

Los clientes envían mensajes de grupo al relay, que valida la membresía antes de aceptarlos.

## Consideraciones de Privacidad

- Los grupos `hidden` proporcionan la protección de descubrimiento más fuerte: no aparecen en búsquedas ni listados de relay
- Los grupos `private` ocultan el contenido de los mensajes de los no miembros
- Los grupos `closed` simplemente ignoran las solicitudes de unión; combínalo con `private` o `hidden` para un control de acceso más fuerte
- `restricted` controla quién puede escribir, independiente del acceso de lectura

---

**Fuentes primarias:**
- [Especificación NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md)

**Mencionado en:**
- [Boletín #2: Actualizaciones de NIP](/es/newsletters/2025-12-24-newsletter/#nip-updates)
