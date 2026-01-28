---
title: "NIP-58: Insignias"
date: 2026-01-28
translationOf: /en/topics/nip-58.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Identity
  - Reputation
---

NIP-58 define un sistema de insignias para Nostr, permitiendo a emisores crear insignias y otorgarlas a usuarios quienes pueden luego mostrarlas en sus perfiles.

## Cómo Funciona

### Definición de Insignia (Kind 30009)

Los emisores crean definiciones de insignias como eventos direccionables:

```json
{
  "kind": 30009,
  "tags": [
    ["d", "early-adopter"],
    ["name", "Adoptante Temprano"],
    ["description", "Se unió antes de 2024"],
    ["image", "https://example.com/badge.png"],
    ["thumb", "https://example.com/badge-thumb.png"]
  ]
}
```

### Otorgamiento de Insignia (Kind 8)

Los emisores otorgan insignias a usuarios:

```json
{
  "kind": 8,
  "tags": [
    ["a", "30009:issuer-pubkey:early-adopter"],
    ["p", "recipient-pubkey"]
  ]
}
```

### Visualización de Insignia (Kind 30008)

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

## Casos de Uso

- **Membresía de comunidad**: Probar membresía en grupos o comunidades
- **Logros**: Reconocer contribuciones o hitos
- **Verificación**: Atestaciones de terceros (empleado, creador, etc.)
- **Control de acceso**: Restringir contenido o funciones basado en posesión de insignia

## Modelo de Confianza

El valor de la insignia depende completamente de la reputación del emisor. Cualquiera puede crear insignias, por lo que los clientes deben:
- Mostrar información del emisor prominentemente
- Permitir a usuarios filtrar por emisores confiables
- No tratar insignias como autoritativas sin contexto

## Relacionado

- [NIP-51](/es/topics/nip-51/) - Listas
- [Web de Confianza](/es/topics/web-of-trust/)
