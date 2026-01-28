---
title: "NIP-52: Eventos de Calendario"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52 define tipos de eventos para funcionalidad de calendario en Nostr, habilitando programación, RSVPs y coordinación de eventos.

## Tipos de Eventos

### Kind 31922: Evento de Calendario Basado en Fecha
Para eventos que abarcan uno o más días sin horarios específicos:

```json
{
  "kind": 31922,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Meetup Nostr"],
    ["start", "2026-02-15"],
    ["end", "2026-02-15"],
    ["location", "Austin, TX"]
  ]
}
```

### Kind 31923: Evento de Calendario Basado en Hora
Para eventos con horas de inicio y fin específicas:

```json
{
  "kind": 31923,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Llamada Semanal"],
    ["start", "1706900400"],
    ["end", "1706904000"],
    ["start_tzid", "America/New_York"]
  ]
}
```

## Soporte RSVP

Los eventos kind 31925 permiten a los usuarios responder a eventos de calendario:

- `accepted` - Asistirá
- `declined` - No asistirá
- `tentative` - Podría asistir

## Características

- **Direccionable**: Los eventos pueden actualizarse sin crear duplicados
- **Soporte de zona horaria**: Manejo adecuado de zonas horarias vía identificadores IANA
- **Ubicación**: Lugares de reunión físicos o virtuales
- **Recurrencia**: Soporte para eventos recurrentes (extensión propuesta)

## Relacionado

- [NIP-22](/es/topics/nip-22/) - Comentarios (para discusiones de eventos de calendario)
- [NIP-51](/es/topics/nip-51/) - Listas (para colecciones de calendario)
