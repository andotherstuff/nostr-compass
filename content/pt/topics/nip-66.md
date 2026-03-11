---
title: 'NIP-66: Descoberta de relay e monitoramento de atividade'
date: 2026-01-21
draft: false
categories:
- NIPs
- Relays
translationOf: /en/topics/nip-66.md
translationDate: 2026-03-11
---

NIP-66 padroniza a publicação de dados de monitoramento relay para Nostr. Os serviços de monitoramento testam continuamente os relays quanto à disponibilidade, latência, conformidade de protocolo e NIPs suportados, publicando resultados como eventos kind 30166.

## Como funciona

Os monitores verificam a disponibilidade do relay conectando e enviando assinaturas de teste. As medições de latência rastreiam o tempo de conexão, o tempo de resposta da assinatura e o atraso de propagação de eventos. Os testes de conformidade do protocolo verificam se o comportamento do relay corresponde às especificações, detectando bugs de implementação ou desvios intencionais.

A verificação de suporte NIP vai além das reivindicações [NIP-11](/pt/topics/nip-11/), testando realmente se os recursos anunciados funcionam corretamente. Se um relay reivindicar suporte de pesquisa [NIP-50](/pt/topics/nip-50/), mas as consultas de pesquisa falharem, os monitores omitirão o NIP-50 da lista verificada. Isso fornece informações básicas sobre os recursos do relay.

Os eventos kind 30166 usam a URL relay como `d` tag, tornando-os eventos substituíveis parametrizados. Cada monitor publica um evento por relay, atualizado conforme as medições mudam. Vários monitores podem rastrear o mesmo relay, fornecendo redundância e validação cruzada.

Tempo de ida e volta (rtt) tags mede a latência para diferentes operações:
- `rtt open`: estabelecimento de conexão WebSocket
- `rtt read`: Tempo de resposta da assinatura
- `rtt write`: Velocidade de publicação do evento

Todos os valores estão em milissegundos. Os clientes usam essas métricas para preferir relays de baixa latência para operações urgentes.

As informações geográficas ajudam os clientes a selecionar relays próximo para melhor latência e resistência à censura. O `geo` tag contém o código do país, o nome do país e a região. O `network` tag distingue o clearnet relays dos serviços ocultos Tor ou endpoints I2P.

## Por que é importante

O NIP-66 transforma a qualidade relay de anedota em dados legíveis por máquina. Um cliente não precisa mais confiar apenas no documento [NIP-11](/pt/topics/nip-11/) do próprio relay ou em uma lista de permissões codificada. Ele pode comparar o tempo de atividade medido, a latência medida e o suporte a recursos testados de um ou mais monitores.

Isso é mais importante para a seleção de relays no modelo outbox. Quando os clientes se conectam dinamicamente a muitos relays, relays inativos ou mal configurados impõem um custo direto em carregamentos de feed mais lentos e mais buscas com falha.

## Casos de uso

O monitoramento de dados alimenta os seletores relay em clientes, sites exploradores e sistemas de avaliação de confiança. Ao fornecer o status relay em tempo real, independente do autorrelato de relay, o NIP-66 permite a seleção informada de relay.

Combinado com [NIP-11](/pt/topics/nip-11/) (capacidades auto-relatadas) e Trusted Relay Assertions (avaliação de confiança), o ecossistema avança em direção à seleção de relays baseada em dados, em vez de depender de padrões codificados.

## Modelo de confiança

O NIP-66 não cria um único monitor oficial. Vários monitores podem publicar resultados para o mesmo relay e os clientes podem compará-los. Esse design reduz a dependência do julgamento de um operador, mas também significa que os clientes precisam de uma política em cujas medições confiem quando os resultados entram em conflito.

---

**Fontes primárias:**
- [Especificação NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) - Padrão de descoberta de relay e monitoramento de atividade

**Mencionado em:**
- [Boletim informativo nº 6: Aprofundamento do NIP](/pt/newsletters/2026-01-21-newsletter/#nip-deep-dive-nip-11-and-nip-66)

**Veja também:**
- [NIP-11: Documento de Informações do Relay](/pt/topics/nip-11/)
- [NIP-65: Metadados da Lista de Relays](/pt/topics/nip-65/)
- [Trusted Relay Assertions](/pt/topics/trusted-relay-assertions/)
