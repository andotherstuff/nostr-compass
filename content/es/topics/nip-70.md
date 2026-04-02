---
title: "NIP-70: Eventos Protegidos"
date: 2026-03-11
translationOf: /en/topics/nip-70.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Relay
  - Access Control
---

NIP-70 define una forma para que los autores marquen un evento como protegido con la simple etiqueta `[["-"]]`. Un evento protegido solo puede ser aceptado cuando un relay elige soportar ese comportamiento y verifica que el publicador autenticado es la misma pubkey que el autor del evento.

## Cómo Funciona

La regla central es breve. Si un evento contiene la etiqueta `[["-"]]`, un relay debería rechazarlo por defecto. Un relay que quiera soportar eventos protegidos debe primero ejecutar el flujo `AUTH` de [NIP-42](/es/topics/nip-42/) y confirmar que el cliente que se autenticó está publicando su propio evento.

Esto hace de NIP-70 una regla de autoridad de publicación, no una regla de cifrado. El contenido aún puede ser legible. Lo que cambia es quién puede colocar ese evento en un relay que respete la etiqueta. Esto permite a los relays soportar feeds semi-cerrados y otros contextos donde los autores quieren que un relay rechace la republicación por terceros.

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

## Implicaciones del Flujo AUTH

Los eventos protegidos son útiles solo cuando los relays realmente aplican la identidad del autor en el momento de publicación. Por eso NIP-70 depende tan directamente de [NIP-42](/es/topics/nip-42/). Un relay que acepta eventos `[["-"]]` sin una verificación de autenticación coincidente está tratando la etiqueta como decoración, no como política.

## Comportamiento del Relay y Límites

NIP-70 no promete que el contenido permanecerá contenido para siempre. Cualquier destinatario aún puede copiar lo que ve y publicar un nuevo evento en otro lugar. La especificación solo da a los relays una forma estándar de respetar la intención del autor y rechazar la republicación directa de eventos protegidos.

Por eso el trabajo de seguimiento importa. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) extiende la regla a reposts que incrustan eventos protegidos, cerrando un bypass fácil donde el evento original permanecía protegido pero el evento envoltorio no.

## Implementaciones

- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - Soporte de autenticación NIP-42 para eventos protegidos
- [strfry PR #176](https://github.com/hoytech/strfry/pull/176) - Rechaza reposts que incrustan eventos protegidos
- [SNSTR v0.3.3](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.3) - Añade soporte auxiliar vinculado al manejo de eventos protegidos

---

**Fuentes primarias:**
- [Especificación NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md)
- [PR #1030](https://github.com/nostr-protocol/nips/pull/1030) - NIP-70 añadido al repositorio de NIPs
- [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) - Rechazar reposts que incrustan eventos protegidos
- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - Implementación de relay para autenticación NIP-42 y eventos protegidos

**Mencionado en:**
- [Newsletter #13: Actualizaciones de NIPs](/en/newsletters/2026-03-11-newsletter/#nip-updates)
- [Newsletter #13: NIP Deep Dive](/en/newsletters/2026-03-11-newsletter/#nip-deep-dive-nip-70-protected-events)

**Ver también:**
- [NIP-42: Autenticación de Clientes](/es/topics/nip-42/)
- [NIP-11: Documento de Información del Relay](/es/topics/nip-11/)
