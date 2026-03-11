---
title: "NIP-70: Eventos protegidos"
date: 2026-03-11
translationOf: /en/topics/nip-70.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Relay
  - Access Control
---

NIP-70 define una forma para que los autores marquen un evento como protegido con la etiqueta simple `[["-"]]`. Un evento protegido solo puede aceptarse cuando un relay decide soportar ese comportamiento y verifica que el publicador autenticado es la misma pubkey que el autor del evento.

## Cómo funciona

La regla central es corta. Si un evento contiene la etiqueta `[["-"]]`, un relay debería rechazarlo por defecto. Un relay que quiera soportar eventos protegidos debe ejecutar primero el flujo `AUTH` de [NIP-42](/es/topics/nip-42/) y confirmar que el cliente autenticado está publicando su propio evento.

Eso convierte a NIP-70 en una regla de autoridad de publicación, no en una regla de cifrado. El contenido puede seguir siendo legible. Lo que cambia es quién puede colocar ese evento en un relay que respeta la etiqueta. Esto permite a los relays soportar feeds semicerrados y otros contextos en los que los autores quieren que un relay rechace la republicación por terceros.

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

## Implicaciones del flujo AUTH

Los eventos protegidos solo son útiles cuando los relays realmente aplican la identidad del autor en el momento de publicación. Por eso NIP-70 depende tan directamente de [NIP-42](/es/topics/nip-42/). Un relay que acepta eventos `[["-"]]` sin una comprobación de auth correspondiente está tratando la etiqueta como decoración, no como política.

## Comportamiento y límites del relay

NIP-70 no promete que el contenido vaya a mantenerse contenido para siempre. Cualquier destinatario aún puede copiar lo que ve y publicar un nuevo evento en otro lugar. La especificación solo da a los relays una forma estándar de respetar la intención del autor y rechazar la republicación directa de eventos protegidos.

Por eso importa el trabajo de seguimiento. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) amplía la regla a los reposts que incrustan eventos protegidos, cerrando una vía sencilla de evasión en la que el evento original seguía protegido pero el evento envoltorio no.

## Implementaciones

- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - Añadió soporte de auth NIP-42 para eventos protegidos
- [strfry PR #176](https://github.com/hoytech/strfry/pull/176) - Rechaza reposts que incrustan eventos protegidos
- [SNSTR v0.3.3](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.3) - Añade soporte auxiliar ligado al manejo de eventos protegidos

---

**Fuentes primarias:**
- [Especificación de NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md)
- [PR #1030](https://github.com/nostr-protocol/nips/pull/1030) - Añadió NIP-70 al repositorio de NIPs
- [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) - Rechaza reposts que incrustan eventos protegidos
- [strfry PR #156](https://github.com/hoytech/strfry/pull/156) - Implementación de relay para auth NIP-42 y eventos protegidos

**Mencionado en:**
- [Newsletter #13: Actualizaciones de NIPs](/es/newsletters/2026-03-11-newsletter/#actualizaciones-de-nips)
- [Newsletter #13: Profundización NIP](/es/newsletters/2026-03-11-newsletter/#profundizacion-nip-nip-70-eventos-protegidos)

**Ver también:**
- [NIP-42: Autenticación de clientes](/es/topics/nip-42/)
- [NIP-11: Documento de información del relay](/es/topics/nip-11/)
