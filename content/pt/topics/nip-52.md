---
title: "NIP-52: Eventos de Calendário"
date: 2026-01-28
translationOf: /en/topics/nip-52.md
translationDate: 2026-01-28
draft: false
categories:
  - NIP
  - Calendar
  - Events
---

NIP-52 define kinds de evento para funcionalidade de calendário no Nostr, permitindo agendamento, RSVPs e coordenação de eventos.

## Kinds de Evento

### Kind 31922: Evento de Calendário Baseado em Data
Para eventos que abrangem um ou mais dias sem horários específicos:

```json
{
  "kind": 31922,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Encontro Nostr"],
    ["start", "2026-02-15"],
    ["end", "2026-02-15"],
    ["location", "Austin, TX"]
  ]
}
```

### Kind 31923: Evento de Calendário Baseado em Horário
Para eventos com horários específicos de início e fim:

```json
{
  "kind": 31923,
  "tags": [
    ["d", "unique-identifier"],
    ["title", "Chamada Semanal"],
    ["start", "1706900400"],
    ["end", "1706904000"],
    ["start_tzid", "America/New_York"]
  ]
}
```

## Suporte a RSVP

Eventos kind 31925 permitem que usuários respondam a eventos de calendário:

- `accepted` - Irá comparecer
- `declined` - Não irá comparecer
- `tentative` - Pode comparecer

## Recursos

- **Endereçável**: Eventos podem ser atualizados sem criar duplicatas
- **Suporte a Fuso Horário**: Tratamento adequado de fusos horários via identificadores IANA
- **Localização**: Locais de encontro físicos ou virtuais
- **Recorrência**: Suporte para eventos recorrentes (extensão proposta)

## Relacionados

- [NIP-22](/pt/topics/nip-22/) - Comentários (para discussões de eventos de calendário)
- [NIP-51](/pt/topics/nip-51/) - Listas (para coleções de calendário)
