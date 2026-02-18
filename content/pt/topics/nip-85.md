---
title: "NIP-85: Trusted Assertions"
date: 2026-02-18
translationOf: /en/topics/trusted-relay-assertions.md
translationDate: 2026-02-18
draft: false
categories:
  - Protocol
  - Relays
---

O NIP-85 define um sistema para delegar cálculos custosos a provedores de serviço confiáveis que publicam resultados assinados como eventos Nostr. Pontuações de Web of Trust e métricas de engajamento exigem rastrear muitos relays e processar grandes volumes de eventos, trabalho que é impraticável em dispositivos móveis e clientes de navegador.

## Como Funciona

O NIP-85 usa quatro kinds de evento para asserções sobre diferentes tipos de sujeito:

- **Kind 30382**: Asserções de usuário — contagem de seguidores, posts, respostas, reações, volumes de zap, rank normalizado (0-100), tópicos comuns e horas ativas
- **Kind 30383**: Asserções de evento — avalia notas individuais com contagem de comentários, citações, reposts, reações e dados de zap
- **Kind 30384**: Asserções de evento endereçável — aplica métricas de engajamento em todas as versões de artigos de forma longa e páginas wiki coletivamente
- **Kind 30385**: Asserções de identificador externo — avalia identificadores externos (livros, filmes, sites, locais, hashtags) referenciados via [NIP-73](/pt/topics/nip-73/)

Cada asserção é um evento endereçável substituível onde a tag `d` contém o sujeito: um pubkey, ID de evento, endereço de evento ou identificador NIP-73. Provedores de serviço assinam esses eventos com suas próprias chaves, e clientes os avaliam com base nas relações de confiança.

## Descoberta de Provedores

Usuários declaram quais provedores de asserção confiam publicando eventos kind 10040. Cada entrada especifica o tipo de asserção com o pubkey do provedor e dica de relay, mais variantes de algoritmo opcionais. Usuários podem criptografar a lista de tags em `.content` usando [NIP-44](/pt/topics/nip-44/) para manter suas preferências de provedor privadas.

Clientes constroem uma lista de provedores verificando quais provedores as contas que seguem confiam, criando uma camada de reputação descentralizada para os próprios provedores de asserção.

## Modelo de Segurança

Provedores devem usar chaves de serviço diferentes para algoritmos distintos, e uma chave única por usuário quando os algoritmos são personalizados, evitando correlação cruzada de consultas entre usuários. Cada chave de serviço recebe um evento de metadados kind 0 descrevendo o comportamento do algoritmo. Eventos de asserção só devem ser atualizados quando os dados subjacentes realmente mudam, permitindo que clientes armazenem resultados em cache com segurança.

## Adoção

O NIP-85 formaliza um padrão que já estava surgindo de forma informal. O servidor de cache do Primal computa métricas de engajamento e pontuações de Web of Trust. [Antiprimal](https://gitlab.com/soapbox-pub/antiprimal) faz bridge desses cálculos para clientes Nostr padrão usando kinds de evento NIP-85. [Nostr.band](https://nostr.band) opera o relay `wss://nip85.nostr.band` referenciado nos próprios exemplos da spec. [Amethyst](https://github.com/vitorpamplona/amethyst) tem suporte experimental a Trusted Assertions em sua biblioteca `quartz`.

---

**Fontes primárias:**
- [Especificação NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md)

**Mencionado em:**
- [Compass #10: Atualizações de NIPs](/pt/newsletters/2026-02-18-newsletter/#atualizações-de-nips)
- [Compass #10: Deep Dive NIP-85](/pt/newsletters/2026-02-18-newsletter/#deep-dive-de-nip-nip-85-trusted-assertions)

**Veja também:**
- [NIP-11: Documento de Informações de Relay](/pt/topics/nip-11/)
- [NIP-73: IDs de Conteúdo Externo](/pt/topics/nip-73/)
