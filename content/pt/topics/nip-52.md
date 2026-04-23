---
title: 'NIP-52: Eventos de calendário'
date: 2026-01-28
draft: false
categories:
  - NIP
  - Calendar
  - Events
translationOf: /en/topics/nip-52.md
translationDate: 2026-04-22
---

NIP-52 define eventos de calendário, calendários e RSVPs no Nostr. Ela dá a clientes uma forma padrão de publicar eventos baseados em data ou horário sem precisar inventar um modelo customizado para cada app.

## Kinds de evento

### Kind 31922: evento de calendário baseado em data

Use o kind `31922` para eventos de dia inteiro ou multi-dia em que horário de relógio não importa.

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

### Kind 31923: evento de calendário baseado em horário

Use o kind `31923` para eventos com horário preciso de início e fim.

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

Eventos baseados em horário também exigem uma ou mais tags `D`, cada uma contendo o timestamp Unix em granularidade de dia para os dias abrangidos pelo evento. Essa tag existe para que relays e clientes possam indexar por dia sem ter de fazer parse de todo timestamp completo.

## Suporte a calendário e RSVP

O kind `31924` é um calendário, uma lista endereçável de eventos de calendário. O kind `31925` é um RSVP que aponta de volta para um evento específico de calendário com uma tag `a` e, opcionalmente, para uma revisão específica com uma tag `e`.

Eventos kind `31925` permitem que usuários respondam com:

- `accepted` - vai participar
- `declined` - não vai participar
- `tentative` - talvez participe

RSVPs também podem incluir valores `fb` de `free` ou `busy`, adicionando contexto de agenda além do status de presença.

## Notas de implementação

- **Endereçável**: eventos e calendários podem ser atualizados sem criar duplicatas
- **Suporte a timezone**: eventos baseados em horário podem usar identificadores IANA de timezone
- **Dados de localização**: tags podem incluir localizações legíveis por humanos, links e geohashes
- **Requests colaborativos**: autores de eventos podem pedir inclusão em calendários de outras pessoas tagueando esse calendário

Eventos recorrentes ficam intencionalmente fora do escopo. A spec empurra regras de recorrência para os clientes, o que mantém a indexação do lado do relay simples e evita casos de borda habituais de calendários, como horário de verão e exceções.

## Por que importa

A NIP-52 faz mais do que descrever uma reunião. Ela separa definição do evento, membership do calendário e responses de participantes em kinds de evento diferentes. Isso permite que um app publique um evento, outro agregue calendários e um terceiro gerencie estado de RSVP sem que os três compartilhem o mesmo backend.

---

**Fontes primárias:**
- [Especificação NIP-52](https://github.com/nostr-protocol/nips/blob/master/52.md)
- [PR #1752: tag de timestamp com granularidade de dia](https://github.com/nostr-protocol/nips/pull/1752)

**Mencionado em:**
- [Newsletter #7: rascunho do app de calendário do Notedeck](/pt/newsletters/2026-01-28-newsletter/)
- [Newsletter #10: Atualizações de NIP](/pt/newsletters/2026-02-18-newsletter/)
- [Newsletter #10: NIP Deep Dive](/pt/newsletters/2026-02-18-newsletter/)
- [Newsletter #13: Calendar by Form* v0.2.0](/en/newsletters/2026-03-11-newsletter/)

**Veja também:**
- [NIP-22: Comment](/pt/topics/nip-22/)
- [NIP-51: Lists](/pt/topics/nip-51/)
