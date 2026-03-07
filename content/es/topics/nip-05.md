---
title: "NIP-05: Verificación de Dominio"
date: 2026-02-04
translationOf: /en/topics/nip-05.md
translationDate: 2026-03-07
draft: false
description: "NIP-05 habilita identificadores legibles para humanos para claves públicas de Nostr mediante verificación de dominio."
categories:
  - Identity
  - Discovery
---

NIP-05 mapea claves públicas de Nostr a identificadores de internet legibles para humanos como `user@example.com`. Proporciona a los usuarios una pista de identidad respaldada por DNS que los clientes pueden verificar por HTTPS.

## Cómo Funciona

Un usuario reclama un identificador añadiendo un campo `nip05` a sus metadatos de perfil. El identificador sigue el formato `name@domain`. Los clientes verifican el reclamo obteniendo `https://domain/.well-known/nostr.json` y comprobando que el nombre mapea a la pubkey del usuario.

El archivo JSON en la ruta well-known contiene un objeto `names` que mapea nombres locales a pubkeys hexadecimales:

```json
{
  "names": {
    "alice": "abc123...",
    "bob": "def456..."
  }
}
```

Cuando la verificación tiene éxito, los clientes pueden mostrar el identificador en lugar de o junto con el npub. Algunos clientes muestran un indicador de verificación, mientras que otros muestran el identificador como texto plano y dejan las decisiones de confianza al lector.

## Modelo de Confianza

NIP-05 no es un registro global de nombres de usuario. Demuestra control de un nombre de dominio y la ruta de un servidor web, no identidad legal ni continuidad de cuenta a largo plazo. Si un propietario de dominio cambia el mapeo después, los clientes verificarán el nuevo mapeo a menos que conserven estado previo.

Eso hace que NIP-05 sea útil para descubrimiento y reputación, pero más débil de lo que los usuarios suelen asumir. Un buen cliente debe tratarlo como control de dominio verificado, no como prueba de que una persona u organización es quien dice ser.

## Pistas de Relay

El archivo `nostr.json` puede opcionalmente incluir un objeto `relays` que mapea pubkeys a arrays de URLs de relay. Esto ayuda a los clientes a descubrir dónde encontrar eventos de un usuario particular.

## Notas de Interoperabilidad

El requisito de minúsculas importa más de lo que parece. Los nombres o pubkeys con mayúsculas mixtas pueden funcionar en una implementación y fallar en otra, por lo que los clientes actuales deben esperar nombres en minúsculas y claves hex en minúsculas en `nostr.json`.

Otro detalle práctico es el nombre especial `_`, que permite a un dominio mapear la forma de identificador simple como `_@example.com` o simplemente `example.com` en clientes que lo soportan. No todos los clientes exponen esa forma de la misma manera, así que los usuarios obtienen los resultados más consistentes con identificadores explícitos `name@domain`.

## Estado de Implementación

La mayoría de los clientes principales soportan verificación NIP-05:
- Damus, Amethyst, Primal muestran identificadores verificados
- Muchos servicios de relay ofrecen identificadores NIP-05 como característica
- Existen numerosos proveedores de NIP-05 gratuitos y de pago

---

**Fuentes primarias:**
- [Especificación NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md)
- [PR #2208](https://github.com/nostr-protocol/nips/pull/2208) - requisito de minúsculas para nombres y claves hex

**Mencionado en:**
- [Boletín #8: Actualizaciones de NIP](/es/newsletters/2026-02-04-newsletter/#nip-updates)

**Ver también:**
- [NIP-01: Protocolo Básico](/es/topics/nip-01/)
- [NIP-65: Metadatos de Lista de Relays](/es/topics/nip-65/)
