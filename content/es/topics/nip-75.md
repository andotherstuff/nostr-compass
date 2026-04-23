---
title: "NIP-75: Objetivos de zap"
date: 2026-04-22
translationOf: /en/topics/nip-75.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
---

NIP-75 define un evento de objetivo de recaudación al que los usuarios pueden hacer zap. Un objetivo declara una cantidad meta en millisatoshis y una lista de relays donde se contabilizan los recibos de zap para ese objetivo. Cualquier zap de [NIP-57](/es/topics/nip-57/) que haga referencia al evento del objetivo cuenta para su progreso.

## Cómo funciona

Un objetivo de zap es un evento `kind:9041`. El `.content` es una descripción legible por humanos. Las etiquetas requeridas son `amount` (objetivo en millisats) y `relays` (la lista de relays usada para contabilizar recibos de zap). Las etiquetas opcionales incluyen `closed_at` para cerrar el conteo en un timestamp dado, `image` y `summary`. El objetivo también puede incluir una etiqueta `r` o `a` que apunte a una URL externa o a un evento direccionable, y puede llevar múltiples pubkeys beneficiarias mediante etiquetas de zap-split tomadas del apéndice G de NIP-57.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1776500000,
  "kind": 9041,
  "tags": [
    ["relays", "wss://alicerelay.example.com", "wss://bobrelay.example.com"],
    ["amount", "210000"],
    ["image", "<image url>"],
    ["summary", "Nostrasia travel expenses"]
  ],
  "content": "Nostrasia travel expenses",
  "sig": "<128-char hex>"
}
```

Los clientes vinculan un zap a un objetivo incluyendo una etiqueta `e` que apunta al evento del objetivo dentro de la solicitud de zap. El progreso del objetivo es la suma de los montos de los recibos de zap coincidentes en los relays que el objetivo especificó. Cuando se establece `closed_at`, los recibos de zap publicados después de ese timestamp no cuentan.

## Implementaciones

- [Amethyst](https://github.com/vitorpamplona/amethyst) ahora renderiza barras de progreso del objetivo y botones de zap de un toque dentro de cabeceras de live stream mediante [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469), que conecta NIP-75 con la pantalla de Live Activities de NIP-53.

---

**Fuentes primarias:**
- [Especificación NIP-75](https://github.com/nostr-protocol/nips/blob/master/75.md)
- [Amethyst PR #2469: top zappers y cabecera de objetivo de live stream](https://github.com/vitorpamplona/amethyst/pull/2469)

**Mencionado en:**
- [Boletín #19: objetivos de zap de live stream en Amethyst](/en/newsletters/2026-04-22-newsletter/)
- [Boletín #19: análisis de NIP-57](/en/newsletters/2026-04-22-newsletter/)

**Ver también:**
- [NIP-57: Lightning Zaps](/es/topics/nip-57/)
- [NIP-53: Actividades en vivo](/es/topics/nip-53/)
