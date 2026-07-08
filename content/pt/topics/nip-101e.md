---
title: "NIP-101e: Treinos Fitness"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-101e.md
translationDate: 2026-07-01
categories:
  - Fitness
  - Discovery
---

NIP-101e define um formato de evento de treino para que aplicativos de rastreamento fitness publiquem, compartilhem e descubram sessões de treino no Nostr. A especificação usa eventos de kind 1301 que carregam métricas da sessão (distância, duração, elevação, frequência cardíaca, calorias, cadência de ciclismo, app de origem) em tags estruturadas, para que um cliente possa renderizar o treino como um card estruturado com métricas exibidas em suas unidades apropriadas.

## Como funciona

Um treino NIP-101e é um evento de kind 1301 com tags estruturadas para cada métrica capturada pelo aplicativo de origem. Tags comuns incluem:

- `type` para a modalidade do treino (corrida, bike, natação, musculação, etc.)
- `distance` com valor e unidade
- `duration` em segundos
- `elevation_gain` com valor e unidade
- Timestamps `start` e `end`
- `heart_rate` (média e máxima)
- `calories` para o gasto energético
- `source` nomeando o aplicativo publicador
- Tags de tópico `t` para descoberta por hashtag

O campo `content` carrega uma nota opcional escrita pelo usuário (o equivalente à legenda que um usuário anexaria a um upload no Strava). Clientes que reconhecem kind 1301 renderizam as métricas estruturadas como um card de treino; clientes que não reconhecem recorrem a exibir o campo `content` como uma nota comum.

## Descoberta e semântica de feed

Eventos NIP-101e são eventos de feed normais, então um treino publicado por um usuário aparece nas linhas do tempo de seus seguidores como qualquer outro post. Clientes com visualizações dedicadas de treino podem se inscrever em kind 1301 com filtros de autor ou hashtag para construir superfícies de diário de treinos, placares de líderes ou feeds de desafios comunitários. A pubkey do autor é a identidade canônica para o treino, então um aplicativo de terceiros lendo os treinos de outro usuário herda as mesmas suposições de confiança que qualquer outro feed Nostr.

## Implementações

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) traz renderização de treinos kind 1301 com uma métrica em destaque, uma grade de estatísticas, exibição de velocidade específica para ciclismo e badges de origem ([PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184), refatorado em [PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226))

---

**Fontes primárias:**
- [Especificação NIP-101e](https://github.com/nostr-protocol/nips/blob/master/101e.md)
- [Amethyst PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184) - Adiciona suporte a treinos fitness NIP-101e (Kind 1301)
- [Amethyst PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226) - Redesenha a exibição de treinos com métrica em destaque e grade de estatísticas

**Mencionado em:**
- [Newsletter #27: Amethyst v1.12.0 traz carteiras Cashu, nutzaps, um driver CLINK e auto-recuperação Tor](/pt/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
