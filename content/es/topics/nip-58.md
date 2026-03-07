---
title: "NIP-58: Insignias"
date: 2026-01-28
translationOf: /en/topics/nip-58.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Identity
  - Reputation
---

NIP-58 define un sistema de insignias para Nostr. Un evento define la insignia, otro la otorga, y un tercero permite al destinatario elegir si la muestra en su perfil.

## Cómo funciona

### Definición de insignia (Kind 30009)

Los emisores crean definiciones de insignias como eventos direccionables:

```json
{
  "kind": 30009,
  "tags": [
    ["d", "early-adopter"],
    ["name", "Early Adopter"],
    ["description", "Joined before 2024"],
    ["image", "https://example.com/badge.png"],
    ["thumb", "https://example.com/badge-thumb.png"]
  ]
}
```

### Otorgamiento de insignia (Kind 8)

Los emisores otorgan insignias a uno o más usuarios:

```json
{
  "kind": 8,
  "tags": [
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["p", "recipient-pubkey"]
  ]
}
```

### Visualización de insignia (Kind 30008)

Los usuarios eligen qué insignias mostrar en su perfil:

```json
{
  "kind": 30008,
  "tags": [
    ["d", "profile_badges"],
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["e", "award-event-id"]
  ]
}
```

En un evento de insignias de perfil, los clientes deben leer las etiquetas `a` y `e` como pares ordenados. Una etiqueta `a` sin su evento de otorgamiento correspondiente, o una etiqueta `e` sin su definición de insignia correspondiente, debe ser ignorada.

## Casos de uso

- **Membresía de comunidad**: Demostrar membresía en grupos o comunidades
- **Logros**: Reconocer contribuciones o hitos
- **Atestaciones**: Permitir que un tercero avale un rol o estado
- **Control de acceso**: Restringir funciones o espacios usando insignias respaldadas por el emisor

## Modelo de confianza

El valor de una insignia depende completamente de la reputación del emisor. Cualquiera puede crear insignias, así que los clientes deben:

- Mostrar la información del emisor de manera prominente
- Permitir a los usuarios filtrar por emisores confiables
- No tratar las insignias como autoritativas sin contexto

Los otorgamientos de insignias son inmutables y no transferibles. Eso hace a las insignias adecuadas para atestaciones y reconocimientos, pero no para credenciales portátiles en el sentido tokenizado.

## Notas de implementación

Las definiciones de insignias son eventos direccionables, así que los emisores pueden actualizar el arte o las descripciones de la insignia con el tiempo sin cambiar el identificador de la insignia. El evento de otorgamiento es el registro durable que vincula a un destinatario con esa definición en un momento dado.

Los clientes también tienen libertad en la presentación. La especificación permite explícitamente que muestren menos insignias de las que un usuario lista y que elijan el tamaño de miniatura que se ajuste al espacio disponible.

---

**Fuentes primarias:**
- [Especificación NIP-58](https://github.com/nostr-protocol/nips/blob/master/58.md)

**Mencionado en:**
- [Boletín #7: Cinco años de eneros en Nostr](/en/newsletters/2026-01-28-newsletter/)
- [Boletín #15: Cinco años de febreros en Nostr](/en/newsletters/2026-03-04-newsletter/)

**Ver también:**
- [NIP-51: Listas](/es/topics/nip-51/)
- [Web of Trust](/es/topics/web-of-trust/)
