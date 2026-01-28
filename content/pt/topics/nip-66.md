---
title: "NIP-66: Descoberta de Relay e Monitoramento de Disponibilidade"
date: 2026-01-21
translationOf: /en/topics/nip-66.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Relays
---

NIP-66 padroniza a publicação de dados de monitoramento de relay no Nostr. Serviços de monitoramento testam continuamente relays para disponibilidade, latência, conformidade de protocolo e NIPs suportados, publicando resultados como eventos kind 30166.

## Como Funciona

Monitores verificam disponibilidade de relay conectando e enviando assinaturas de teste. Medições de latência rastreiam tempo de conexão, tempo de resposta de assinatura e atraso de propagação de evento. Testes de conformidade de protocolo verificam se o comportamento do relay corresponde às especificações, capturando bugs de implementação ou desvios intencionais.

Verificação de suporte a NIP vai além das declarações [NIP-11](/pt/topics/nip-11/) testando de fato se recursos anunciados funcionam corretamente. Se um relay alega suporte a busca [NIP-50](/pt/topics/nip-50/) mas consultas de busca falham, monitores omitirão NIP-50 da lista verificada. Isso fornece a verdade fundamental sobre capacidades de relay.

Eventos kind 30166 usam a URL do relay como tag `d`, tornando-os eventos substituíveis parametrizados. Cada monitor publica um evento por relay, atualizado conforme medições mudam. Múltiplos monitores podem rastrear o mesmo relay, fornecendo redundância e validação cruzada.

Tags de tempo de ida e volta (rtt) medem latência para diferentes operações:
- `rtt open`: Estabelecimento de conexão WebSocket
- `rtt read`: Tempo de resposta de assinatura
- `rtt write`: Velocidade de publicação de evento

Todos os valores são em milissegundos. Clientes usam essas métricas para preferir relays de baixa latência para operações sensíveis ao tempo.

Informação geográfica ajuda clientes a selecionar relays próximos para melhor latência e resistência à censura. A tag `geo` contém código de país, nome de país e região. A tag `network` distingue relays clearnet de serviços ocultos Tor ou endpoints I2P.

## Casos de Uso

Dados de monitoramento alimentam seletores de relay em clientes, websites exploradores e sistemas de avaliação de confiança. Ao fornecer status de relay em tempo real independente de auto-relato do relay, NIP-66 permite seleção informada de relay.

Combinado com [NIP-11](/pt/topics/nip-11/) (capacidades auto-relatadas) e Trusted Relay Assertions (avaliação de confiança), o ecossistema se move em direção à seleção de relay orientada por dados em vez de depender de padrões codificados.

---

**Fontes primárias:**
- [Especificação NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) - Padrão de descoberta de relay e monitoramento de disponibilidade

**Mencionado em:**
- [Newsletter #6: Mergulho Profundo em NIP](/pt/newsletters/2026-01-21-newsletter/#nip-deep-dive-nip-11-and-nip-66)

**Veja também:**
- [NIP-11: Documento de Informação de Relay](/pt/topics/nip-11/)
- [Trusted Relay Assertions](/pt/topics/trusted-relay-assertions/)
