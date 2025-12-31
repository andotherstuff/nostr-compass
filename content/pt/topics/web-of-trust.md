---
title: "Web of Trust"
date: 2025-12-31
translationOf: /en/topics/web-of-trust.md
translationDate: 2025-12-31
draft: false
categories:
  - Confiança
  - Grafo Social
---

Web of Trust (WoT) é um modelo de confiança descentralizado onde a reputação e a confiabilidade são derivadas das relações do grafo social em vez de autoridades centrais.

## Como Funciona

No Nostr, Web of Trust aproveita o grafo de seguimento (listas de contatos NIP-02) e eventos de denúncia para calcular pontuações de confiança:

1. **Construção do Grafo**: Um grafo direcionado é construído a partir de pubkeys, eventos e seus relacionamentos (seguimentos, silenciados, denúncias)
2. **Atribuição de Pesos**: Pesos iniciais são atribuídos a pubkeys conhecidas como confiáveis (por exemplo, aquelas com identificadores NIP-05 verificados)
3. **Propagação Iterativa**: Pontuações de confiança fluem através da rede usando algoritmos similares ao PageRank
4. **Resistência a Sybil**: Se um atacante cria muitas contas falsas, a confiança passada para elas é dividida pelo número de falsas

## Propriedades Principais

- **Descentralizado**: Nenhuma autoridade central determina a reputação
- **Personalizado**: A confiança pode ser calculada da perspectiva de cada usuário com base em quem ele segue
- **Resistente a Sybil**: Fazendas de bots não conseguem facilmente manipular o sistema devido à diluição de confiança
- **Componível**: Pode ser aplicado a filtragem de spam, moderação de conteúdo, admissão em relays e diretórios de pagamento

## Aplicações no Nostr

- **Filtragem de Spam**: Relays podem usar WoT para filtrar conteúdo de baixa confiança
- **Descoberta de Conteúdo**: Exibir conteúdo de contas confiáveis pela sua rede
- **Diretórios de Pagamento**: Busca de endereços Lightning com prevenção de falsificação de identidade
- **Políticas de Relay**: Relays WoT aceitam apenas notas de pubkeys confiáveis
- **Moderação Descentralizada**: Comunidades podem curar com base em pontuações de confiança

## Implementações

Vários projetos implementam Web of Trust para Nostr:
- **Nostr.Band Trust Rank**: Pontuação estilo PageRank para a rede
- **WoT Relays**: Relays que filtram por distância social
- **DCoSL**: Protocolo para sistemas de reputação descentralizados
- **Noswot**: Pontuação de confiança baseada em seguimentos e denúncias

---

**Fontes principais:**
- [Nostr.Band Trust Rank](https://trust.nostr.band/)
- [Protocolo DCoSL](https://github.com/wds4/DCoSL)
- [Noswot](https://codeberg.org/weex/noswot)

**Mencionado em:**
- [Newsletter #3: Resumo de Dezembro](/pt/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Veja também:**
- [NIP-02: Lista de Seguidos](/pt/topics/nip-02/)
