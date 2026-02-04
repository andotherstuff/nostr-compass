---
title: "NIP-73 (Geoetiquetas)"
date: 2026-02-04
description: "NIP-73 define etiquetado de ubicación para eventos de Nostr usando coordenadas geográficas e identificadores."
---

NIP-73 especifica cómo adjuntar datos de ubicación geográfica a eventos de Nostr. Esto habilita descubrimiento y filtrado de contenido basado en ubicación.

## Cómo Funciona

Los datos de ubicación se agregan a eventos vía etiquetas `g` (geohash). La codificación geohash representa latitud y longitud como una sola cadena, con precisión determinada por la longitud de la cadena. Cadenas más largas indican ubicaciones más precisas.

Los eventos pueden incluir múltiples etiquetas geohash a diferentes niveles de precisión, permitiendo a los clientes consultar a varias granularidades. Una publicación etiquetada con un geohash de 6 caracteres cubre aproximadamente una manzana de ciudad, mientras que un geohash de 4 caracteres cubre una ciudad pequeña.

## Formato de Etiqueta

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

Actualizaciones recientes a NIP-73 ([PR #2205](https://github.com/nostr-protocol/nips/pull/2205)) agregaron soporte para códigos de país ISO 3166, permitiendo que eventos sean etiquetados con ubicación a nivel de país sin requerir coordenadas precisas:

```json
{
  "tags": [
    ["g", "US", "countryCode"]
  ]
}
```

## Implementaciones

- Clientes conscientes de ubicación usan NIP-73 para check-ins y descubrimiento local
- Filtros de relay pueden restringir o priorizar contenido por geografía
- Aplicaciones de mapeo muestran notas geoetiquetadas

## Fuentes Primarias

- [Especificación NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Agrega códigos de país ISO 3166

## Mencionado En

- [Boletín #8 (2026-02-04)](/es/newsletters/2026-02-04-newsletter/) - Soporte de códigos de país fusionado
