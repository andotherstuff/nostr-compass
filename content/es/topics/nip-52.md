---
title: "NIP-52: Eventos de calendario"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52 define eventos de calendario, calendarios y RSVPs en Nostr. Ofrece a los clientes una forma estándar de publicar eventos basados en fecha o en hora sin inventar un modelo de eventos personalizado para cada aplicación.

## Tipos de eventos

### Kind 31922: Evento de calendario basado en fecha

Se usa kind `31922` para eventos de día completo o de varios días donde la hora exacta no importa.

```json
{
  "kind": 31922,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Nostr Meetup"],
    ["start", "2026-02-15"],
    ["end", "2026-02-16"],
    ["location", "Austin, TX"]
  ]
}
```

### Kind 31923: Evento de calendario basado en hora

Se usa kind `31923` para eventos con horas de inicio y fin precisas.

```json
{
  "kind": 31923,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Weekly Call"],
    ["start", "1706900400"],
    ["end", "1706904000"],
    ["D", "19755"],
    ["start_tzid", "America/New_York"]
  ]
}
```

Los eventos basados en hora también requieren una o más etiquetas `D`, cada una conteniendo el timestamp Unix con granularidad de día para los días que abarca el evento. Esa etiqueta existe para que relays y clientes puedan indexar por día sin parsear cada timestamp completo.

## Soporte de calendario y RSVP

Kind `31924` es un calendario, una lista direccionable de eventos de calendario. Kind `31925` es un RSVP que apunta a un evento de calendario específico con una etiqueta `a` y opcionalmente a una revisión específica con una etiqueta `e`.

Los eventos kind `31925` permiten a los usuarios responder con:

- `accepted` - Asistirá
- `declined` - No asistirá
- `tentative` - Podría asistir

Los RSVPs también pueden incluir valores `fb` de `free` o `busy`, lo que agrega contexto de programación más allá del estado de asistencia.

## Notas de implementación

- **Direccionable**: Los eventos y calendarios pueden actualizarse sin crear duplicados
- **Soporte de zona horaria**: Los eventos basados en hora pueden usar identificadores de zona horaria IANA
- **Datos de ubicación**: Las etiquetas pueden incluir ubicaciones legibles, enlaces y geohashes
- **Solicitudes colaborativas**: Los autores de eventos pueden solicitar inclusión en el calendario de otra persona etiquetándolo

Los eventos recurrentes están intencionalmente fuera del alcance. La especificación delega las reglas de recurrencia a los clientes, lo que mantiene simple la indexación del lado del relay y evita los casos límite habituales de calendario relacionados con cambios de horario de verano y excepciones.

## Por qué importa

NIP-52 hace más que describir una reunión. Separa la definición de evento, la membresía de calendario y las respuestas de asistentes en diferentes kinds de evento. Eso hace posible que una aplicación publique un evento, otra agregue calendarios y una tercera gestione el estado de RSVP sin que las tres compartan el mismo backend.

---

**Fuentes primarias:**
- [Especificación NIP-52](https://github.com/nostr-protocol/nips/blob/master/52.md)
- [PR #1752: Etiqueta de timestamp con granularidad de día](https://github.com/nostr-protocol/nips/pull/1752)

**Mencionado en:**
- [Boletín #7: Borrador de app de calendario en Notedeck](/es/newsletters/2026-01-28-newsletter/#notedeck-progress-calendar-app-and-ux-polish)
- [Boletín #10: Actualizaciones de NIP](/es/newsletters/2026-02-18-newsletter/#nip-updates)
- [Boletín #10: NIP Deep Dive](/es/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-52-calendar-events)

**Ver también:**
- [NIP-22: Comment](/es/topics/nip-22/)
- [NIP-51: Listas](/es/topics/nip-51/)
