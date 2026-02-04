---
title: "NIP-73 (Geotags)"
date: 2026-02-04
description: "NIP-73 define marcação de localização para eventos Nostr usando coordenadas geográficas e identificadores."
---

NIP-73 especifica como anexar dados de localização geográfica a eventos Nostr. Isso permite descoberta e filtragem de conteúdo baseada em localização.

## Como Funciona

Dados de localização são adicionados a eventos via tags `g` (geohash). A codificação geohash representa latitude e longitude como uma única string, com precisão determinada pelo comprimento da string. Strings mais longas indicam localizações mais precisas.

Eventos podem incluir múltiplas tags geohash em diferentes níveis de precisão, permitindo que clientes consultem em várias granularidades. Um post marcado com um geohash de 6 caracteres cobre aproximadamente um quarteirão, enquanto um geohash de 4 caracteres cobre uma pequena cidade.

## Formato de Tag

```json
{
  "tags": [
    ["g", "u4pruydqqvj", "geohash"],
    ["g", "u4pruyd", "geohash"],
    ["g", "u4pru", "geohash"]
  ]
}
```

## Códigos de País

Atualizações recentes ao NIP-73 ([PR #2205](https://github.com/nostr-protocol/nips/pull/2205)) adicionaram suporte para códigos de país ISO 3166, permitindo que eventos sejam marcados com localização em nível de país sem exigir coordenadas precisas:

```json
{
  "tags": [
    ["g", "US", "countryCode"]
  ]
}
```

## Implementações

- Clientes com consciência de localização usam NIP-73 para check-ins e descoberta local
- Filtros de relay podem restringir ou priorizar conteúdo por geografia
- Aplicações de mapeamento exibem notas geotagueadas

## Fontes Primárias

- [Especificação NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Adiciona códigos de país ISO 3166

## Mencionado Em

- [Newsletter #8 (2026-02-04)](/pt/newsletters/2026-02-04-newsletter/) - Suporte a código de país mergeado
