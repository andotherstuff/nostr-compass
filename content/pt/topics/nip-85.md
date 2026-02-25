---
title: "NIP-85"
date: 2026-02-18
translationOf: /en/topics/nip-85.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - Trust
  - Infrastructure
---

NIP-85 define Trusted Assertions, um sistema para delegar cálculos custosos a provedores de serviço confiáveis que publicam resultados assinados como eventos Nostr.

## Como Funciona

Pontuações de Web of Trust, métricas de engajamento e outros valores computados exigem rastrear muitos relays e processar grandes volumes de eventos. Esse trabalho é impraticável em dispositivos móveis. NIP-85 permite que provedores especializados realizem esses cálculos e publiquem resultados que clientes podem consultar.

Provedores de serviço anunciam suas capacidades via eventos kind 30085. Clientes descobrem provedores consultando esses anúncios em relays de pubkeys que o usuário já segue ou confia. Resultados chegam como eventos kind 30382 assinados pelo provedor.

## Principais Funcionalidades

- Computação delegada para métricas de alto custo
- Descoberta de provedores através do grafo social
- Asserções assinadas para resultados verificáveis
- Decisões de confiança no lado do cliente

---

**Fontes primárias:**
- [Especificação NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md)

**Mencionado em:**
- [Compass #10: Deep Dive NIP-85](/pt/newsletters/2026-02-18-newsletter/#deep-dive-de-nip-nip-85-trusted-assertions)
- [Compass #11: Descoberta de Provedores NIP-85](/pt/newsletters/2026-02-25-newsletter/#atualizações-de-nips)

**Veja também:**
- [Web of Trust](/pt/topics/web-of-trust/)
