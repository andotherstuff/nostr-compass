---
title: 'NIP-52: Eventos do calendário'
date: 2026-01-28
draft: false
categories:
- NIP
- Calendar
- Events
translationOf: /en/topics/nip-52.md
translationDate: '2026-03-07'
---

NIP-52 define eventos de calendário, calendários e RSVPs no Nostr. Ele oferece aos clientes uma maneira padrão de publicar eventos baseados em tempo ou data sem inventar um modelo de evento personalizado para cada aplicativo.

## Tipos de eventos

### kind 31922: evento de calendário baseado em data

Use kind `31922` para eventos de dia inteiro ou de vários dias onde o horário não importa.

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

### kind 31923: evento de calendário baseado em tempo

Use kind `31923` para eventos com horários de início e término precisos.

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

Os eventos baseados em tempo também exigem um ou mais `D` tags, cada um contendo o carimbo de data/hora Unix com granularidade diária para os dias em que o evento se estende. Esse tag existe para que relays e os clientes possam indexar por dia sem analisar cada carimbo de data/hora completo.

## Calendário e suporte RSVP

O kind `31924` é um calendário, uma lista endereçável de eventos do calendário. O kind `31925` é um RSVP que aponta para um evento específico do calendário com um `a` tag e opcionalmente para uma revisão específica com um `e` tag.

Os eventos kind `31925` permitem que os usuários respondam com:

- `accepted` - Participará
- `declined` - Não comparecerá
- `tentative` - Pode participar

RSVPs também podem incluir valores `fb` de `free` ou `busy`, o que adiciona contexto de agendamento além do status de atendimento.

## Notas de implementação

- **Endereçável**: eventos e calendários podem ser atualizados sem criar duplicatas
- **Suporte para fuso horário**: eventos baseados em horário podem usar identificadores de fuso horário da IANA
- **Dados de localização**: as tags podem incluir locais legíveis, links e geohashes
- **Solicitações colaborativas**: os autores do evento podem solicitar inclusão na agenda de outra pessoa marcando-a

Eventos recorrentes estão intencionalmente fora do escopo. A especificação envia regras de recorrência para os clientes, o que mantém a indexação do lado relay simples e evita os casos extremos usuais do calendário em torno de alterações e exceções no horário de verão.

## Por que é importante

O NIP-52 faz mais do que descrever uma reunião. Ele separa a definição do evento, a associação ao calendário e as respostas dos participantes em diferentes eventos kinds. Isso possibilita que um aplicativo publique um evento, outro agregue calendários e um terceiro gerencie o estado de RSVP sem que todos os três compartilhem o mesmo back-end.

---

**Fontes primárias:**
- [Especificação NIP-52](https://github.com/nostr-protocol/nips/blob/master/52.md)
- [PR #1752: Tag de carimbo de data/hora com granularidade de dia](https://github.com/nostr-protocol/nips/pull/1752)

**Mencionado em:**
- [Boletim informativo nº 7: Rascunho do aplicativo Notedeck Calendar](/pt/newsletters/2026-01-28-newsletter/#notedeck-progress-calendar-app-and-ux-polish)
- [Boletim Informativo nº 10: Atualizações do NIP](/pt/newsletters/2026-02-18-newsletter/#nip-updates)
- [Boletim informativo nº 10: Aprofundamento do NIP](/pt/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-52-calendar-events)

**Veja também:**
- [NIP-22: Comentário](/pt/topics/nip-22/)
- [NIP-51: Listas](/pt/topics/nip-51/)
