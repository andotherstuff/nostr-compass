---
title: 'NIP-53: Atividades ao vivo'
date: 2026-04-15
draft: false
categories:
  - Protocol
  - Live Streaming
translationOf: /en/topics/nip-53.md
translationDate: 2026-04-22
---

NIP-53 define o formato padrão de evento para metadados de live streaming no Nostr. Uma stream é anunciada como um evento endereçável kind `30311`, para que clientes possam descobri-la, mostrar seu estado atual e ligar o chat de volta ao contexto da stream.

## Como funciona

Cada stream usa um evento kind `30311` com uma tag `d` como identificador estável. O evento normalmente inclui título e texto de resumo, uma tag `streaming` com a URL de reprodução e uma tag `status` (`planned`, `live` ou `ended`). Como este é um evento endereçável, atualizações substituem metadados anteriores para o mesmo valor `d`, em vez de criar uma trilha ilimitada de eventos.

O evento pode incluir tags de tópico (`t`), referências de participantes (`p`) e campos opcionais de contagem de participantes. O chat ao vivo é carregado por eventos kind `1311` que referenciam a stream com uma tag `a`, o que mantém as mensagens de chat vinculadas a um registro específico de atividade ao vivo.

## Implementações

- [Shosho](https://github.com/r0d8lsh0p/shosho-releases) publica metadados de live stream e chat em torno de transmissões ao vivo nativas de Nostr.
- [Zap.stream](https://zap.stream/) usa eventos Nostr para descoberta e interação com streams.
- [WaveFunc](https://github.com/zeSchlausKwab/wavefunc) usa eventos de chat ao vivo kind `1311` em seu contexto de rádio na internet.
- [Amethyst](https://github.com/vitorpamplona/amethyst) conectou metas de zap [NIP-75](/pt/topics/nip-75/) à tela Live Activities via [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469): cada live stream passa a carregar um cabeçalho de meta de arrecadação com barra de progresso, botão de zap com um toque e ranking dos principais zappers calculado a partir de recibos de zap kind `9735` vinculados ao evento kind `30311` da stream. O [PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) adiciona proof of agreement e builders de evento para NIP-53, e o [PR #2486](https://github.com/vitorpamplona/amethyst/pull/2486) lança uma tela dedicada de feed de Live Streams com filtragem e descoberta.
- [NoorNote v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4) adiciona zaps com um toque em cards de live stream, onde os sats aparecem na sobreposição de chat da stream via NIP-53.

---

**Fontes primárias:**
- [Especificação NIP-53](https://github.com/nostr-protocol/nips/blob/master/53.md)
- [Amethyst PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) - cabeçalho de meta de live stream e ranking de top zappers
- [Amethyst PR #2491](https://github.com/vitorpamplona/amethyst/pull/2491) - proof of agreement e builders de evento para NIP-53

**Mencionado em:**
- [Newsletter #18: lançamento do WaveFunc](/en/newsletters/2026-04-15-newsletter/)
- [Newsletter #19: metas de zap em live streams no Amethyst](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: NoorNote v0.8.4](/en/newsletters/2026-04-22-newsletter/)

**Veja também:**
- [NIP-29: Grupos baseados em relay](/pt/topics/nip-29/)
- [NIP-75: Metas de zap](/pt/topics/nip-75/)
- [NIP-57: Zaps](/pt/topics/nip-57/)
- [NIP-C7: Mensagens de chat](/pt/topics/nip-c7/)
