---
title: Web of Trust
date: 2025-12-31
draft: false
categories:
- Trust
- Social Graph
translationOf: /en/topics/web-of-trust.md
translationDate: '2026-03-07'
---

Web of Trust (WoT) é um modelo de confiança descentralizado em que reputação e confiabilidade são derivadas de relações no grafo social, e não de autoridades centrais.

## Como funciona

No Nostr, o Web of Trust geralmente começa a partir do grafo de follows em [NIP-02: Follow List](/pt/topics/nip-02/) e às vezes adiciona mutes, reports ou sinais de identidade verificados. Um cliente ou serviço escolhe uma ou mais pubkeys-semente nas quais já confia e então propaga a confiança pelo grafo.

1. **Construção do grafo**: construir um grafo direcionado com follows e sinais negativos opcionais
2. **Seleção de sementes**: começar com pubkeys nas quais o observador já confia
3. **Propagação da pontuação**: propagar o ranking pelo grafo com um algoritmo como PageRank ou uma variante
4. **Cortes e normalização**: limitar a profundidade do grafo, reduzir o peso de contas com pouco sinal e normalizar a pontuação final para exibição ou filtragem

O algoritmo exato não é padronizado. Dois sistemas WoT podem ser válidos e ainda produzir classificações diferentes porque usam sementes, profundidade de grafo, regras de decaimento ou tratamento diferente para mutes e reports.

## Por que é importante

O WoT dá ao Nostr uma forma de classificar e filtrar sem um serviço central de moderação. Um grafo de confiança personalizado é mais difícil de manipular do que uma contagem bruta de seguidores porque contas falsas ainda precisam que a confiança flua até elas a partir da rede existente do observador.

O outro lado é o problema de partida a frio. Se você não segue ninguém, um WoT personalizado quase não tem base para classificar nada. Muitos produtos lidam com isso distribuindo follows iniciais, listas padrão de provedores confiáveis ou pontuações pré-computadas de serviços externos.

## Aplicações em Nostr

- **Filtragem de spam**: os relays podem usar WoT para filtrar conteúdo de baixa confiança
- **Descoberta de conteúdo**: exiba conteúdo de contas confiáveis da sua rede
- **Diretórios de pagamento**: busca de endereço Lightning com prevenção contra impersonação
- **Políticas de relay**: relays baseados em WoT aceitam apenas notas de pubkeys confiáveis
- **Moderação descentralizada**: as comunidades podem fazer curadoria com base em pontuações de confiança

## Notas de implementação

Como os cálculos de WoT exigem acompanhar grandes partes da rede, muitos clientes não os calculam localmente. [NIP-85: Asserções confiáveis](/pt/topics/nip-85/) existe em parte por esse motivo: ele oferece aos clientes uma forma de consumir cálculos de WoT assinados por terceiros quando a computação local é cara demais.

As implementações existentes também respondem a diferentes questões. Uma classificação de confiança global é útil para descoberta e resistência a spam em toda a rede. Uma pontuação local personalizada é melhor para "mostre-me contas nas quais meu grafo confiaria". Ler um número WoT sem saber qual modelo o produziu é uma fonte comum de confusão.

---

**Fontes primárias:**
- [NIP-02: Lista de Seguidores](https://github.com/nostr-protocol/nips/blob/master/02.md)
- [NIP-85: Asserções confiáveis](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [Classificação de confiança Nostr.Band](https://trust.nostr.band/)
- [Protocolo DCoSL](https://github.com/wds4/DCoSL)
- [Noswot](https://codeberg.org/weex/noswot)

**Mencionado em:**
- [Boletim informativo nº 3: Recapitulação de dezembro](/pt/newsletters/2025-12-31-newsletter/#resumo-de-dezembro-cinco-anos-de-dezembros-do-nostr)

**Veja também:**
- [NIP-02: Lista de Seguidores](/pt/topics/nip-02/)
