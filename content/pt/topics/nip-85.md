---
title: 'NIP-85: Asserções Confiáveis'
date: 2026-02-18
draft: false
categories:
- NIP
- Trust
- Infrastructure
translationOf: /en/topics/nip-85.md
translationDate: '2026-03-07'
---

O NIP-85 define Asserções Confiáveis, um sistema para delegar cálculos caros a provedores de serviços confiáveis ​​que publicam resultados assinados como eventos Nostr.

## Como funciona

Pontuações Web of Trust, métricas de engajamento e outros valores computados exigem o rastreamento de muitos relays e o processamento de grandes volumes de eventos. Este trabalho é impraticável em dispositivos móveis. O NIP-85 permite que provedores especializados realizem esses cálculos e publiquem resultados que os clientes podem consultar.

Asserções confiáveis ​​são eventos endereçáveis. O `d` tag identifica o assunto que está sendo pontuado, e o evento kind identifica que tipo de assunto é: pubkeys (30382), eventos regulares (30383), eventos endereçáveis ​​(30384) e identificadores NIP-73 (30385).

Os usuários declaram em quais provedores confiam por meio kind 10040. Essas listas de provedores podem ser públicas no tags ou criptografadas no conteúdo do evento com [NIP-44](/pt/topics/nip-44/), o que é importante quando um usuário não deseja publicar suas entradas de confiança abertamente.

## Por que é importante

O insight útil do NIP-85 é que ele padroniza resultados, não algoritmos. Dois provedores podem publicar um `rank` tag para o mesmo pubkey enquanto usam fórmulas Web of Trust diferentes, manipulação de mudo, cobertura relay ou heurística anti-spam. Os clientes permanecem interoperáveis ​​porque o formato do resultado corresponde mesmo quando o cálculo não corresponde.

Isso é mais adequado para Nostr do que fingir que haverá um serviço de classificação canônica. Os usuários escolhem em quais afirmações confiam.

## Modelo de confiança

Os provedores de serviços devem assinar seus próprios eventos de asserção, e a especificação recomenda diferentes chaves de serviço para diferentes algoritmos ou pontos de vista específicos do usuário. Isso evita que um provedor reduza sistemas de classificação não relacionados em uma identidade opaca.

A confiança ainda permanece local. A saída assinada prova qual provedor publicou uma pontuação, não que a pontuação esteja correta. Os clientes precisam de uma política sobre quais chaves de provedor usar, de quais relays buscar e como lidar com afirmações conflitantes.

## Notas de interoperabilidade

O NIP-85 vai além de pessoas e postos. O kind 30385 permite que os provedores classifiquem identificadores externos NIP-73, como livros, sites, hashtags e locais. Isso cria um caminho para dados interoperáveis ​​de reputação e engajamento em torno de assuntos fora da própria Nostr.

---

**Fontes primárias:**
- [Especificação NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #2223](https://github.com/nostr-protocol/nips/pull/2223) - Orientação para descoberta do provedor de serviços

**Mencionado em:**
- [Boletim informativo nº 10: Aprofundamento do NIP-85](/pt/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [Boletim informativo nº 11: Descoberta do provedor de serviços NIP-85](/pt/newsletters/2026-02-25-newsletter/#nip-updates)
- [Boletim informativo nº 12: Recapitulação do protocolo](/pt/newsletters/2026-03-04-newsletter/)

**Veja também:**
- [NIP-44: cargas criptografadas](/pt/topics/nip-44/)
- [NIP-73: IDs de conteúdo externo](/pt/topics/nip-73/)
- [Web of Trust](/pt/topics/web-of-trust/)
