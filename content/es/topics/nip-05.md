---
title: "NIP-05 (Verificación de Dominio)"
date: 2026-02-04
description: "NIP-05 habilita identificadores legibles para humanos para claves públicas de Nostr mediante verificación de dominio."
---

NIP-05 mapea claves públicas de Nostr a identificadores de internet legibles para humanos como `usuario@ejemplo.com`. Esto proporciona una forma de verificar identidad a través de propiedad de dominio sin requerir confianza en una autoridad central.

## Cómo Funciona

Un usuario reclama un identificador agregando un campo `nip05` a sus metadatos de perfil. El identificador sigue el formato `nombre@dominio`. Los clientes verifican el reclamo obteniendo `https://dominio/.well-known/nostr.json` y comprobando que el nombre mapea a la pubkey del usuario.

El archivo JSON en la ruta well-known contiene un objeto `names` mapeando nombres locales a pubkeys hexadecimales:

```json
{
  "names": {
    "alice": "abc123...",
    "bob": "def456..."
  }
}
```

Cuando la verificación tiene éxito, los clientes pueden mostrar el identificador en lugar de o junto con el npub. Algunos clientes muestran una marca de verificación u otro indicador para identificadores verificados.

## Pistas de Relay

El archivo `nostr.json` puede opcionalmente incluir un objeto `relays` mapeando pubkeys a arrays de URLs de relay. Esto ayuda a los clientes a descubrir dónde encontrar eventos de un usuario particular.

## Implementaciones

La mayoría de los clientes principales soportan verificación NIP-05:
- Damus, Amethyst, Primal muestran identificadores verificados
- Muchos servicios de relay ofrecen identificadores NIP-05 como característica
- Existen numerosos proveedores de NIP-05 gratuitos y de pago

## Fuentes Primarias

- [Especificación NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md)

## Mencionado En

- [Boletín #8 (2026-02-04)](/es/newsletters/2026-02-04-newsletter/) - PR requiriendo minúsculas para claves hex y nombres
