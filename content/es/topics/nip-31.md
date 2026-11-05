---
title: "NIP-31: Gestión de kinds de evento desconocidos"
date: 2026-11-04
draft: false
categories:
  - NIPs
  - Protocol
translationOf: /en/topics/nip-31.md
translationDate: 2026-11-05
---

> **Advertencia de estado:** La [especificación NIP-31](https://github.com/nostr-protocol/nips/blob/master/31.md) actual se marca a sí misma como `unrecommended` por ser "unnecessarily bloated" (innecesariamente sobrecargada), y su línea de estado dice draft, unrecommended y optional. Los relays ya contienen eventos que usan esta convención, así que esta página explica cómo los leen los clientes. No recomienda NIP-31 para protocolos nuevos.

NIP-31 define una etiqueta `alt` de nivel superior. La etiqueta contiene un breve resumen en texto plano para kinds de evento personalizados que no están pensados para leerse como notas de texto normales.

## Cómo funciona {#how-it-works}

El autor de un evento de kind personalizado añade una etiqueta `alt` con un texto que una persona pueda leer. Los clientes construidos en torno a kind 1 no tienen que suscribirse a todos los kinds que no reconocen. Aun así, sus usuarios pueden encontrarse con uno de esos eventos cuando una nota lo referencia, y la etiqueta aporta algo de contexto aunque el cliente no implemente ese kind.

Fragmento de etiqueta, no un evento completo:

```
["alt", "<short plaintext summary>"]
```

Una etiqueta legible solo cubre la visualización. No puede emitir un voto, ejecutar una solicitud de monedero ni realizar ninguna otra acción nativa del kind. Para una interacción más rica, la especificación remite a [NIP-89: Recommended Application Handlers](/es/topics/nip-89/).

## Implementaciones {#implementations}

En la [tarjeta de evento desconocido de noStrudel en el commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx), la primera etiqueta `alt` se recorta y se convierte en la etiqueta principal, con una línea opcional `Using <client>`. Un valor ausente o en blanco produce `Unknown event (kind ...)`, y hasta tres líneas de contenido se muestran por separado. El mismo componente resuelve la etiqueta `client` mediante plantillas de handlers NIP-89. Muestra un botón Open cuando existe una dirección compartible y `Open in <client>` cuando se resuelve un enlace de handler válido. La explicación y el envío a una app son controles separados.

[UnknownEventDigest.kt de Amethyst en el commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170) prefiere el contenido que clasifica como prosa y recurre a `alt` en su defecto. Su parser recorta los valores y toma el primer `alt` no vacío. Como resultado, un evento cuyo primer `alt` está en blanco puede recibir aquí una etiqueta distinta que en noStrudel. Ambas descripciones reflejan el código fuente en esos commits. Ninguna confirma cómo se comporta una versión publicada.

## Límites {#limits}

- `alt` es una etiqueta, así que el ID y la firma del evento definidos en [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) la cubren. Una firma válida muestra que el autor publicó la etiqueta. No muestra que la etiqueta sea exacta, así que un resumen puede ser engañoso.
- Las etiquetas son públicas. Un `alt` en un evento con contenido cifrado expone su resumen y puede revelar lo que el contenido oculta.
- Las dos propiedades anteriores provienen del envoltorio de evento de NIP-01. El propio texto de NIP-31 no las establece como requisitos.
- Una etiqueta `alt` de nivel superior es distinta del campo `alt` de descripción de imagen dentro de `imeta`, y los renderizadores los analizan por separado.

---

**Fuentes primarias:**
- [Especificación NIP-31](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [embedded-unknown.tsx de noStrudel en el commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx)
- [UnknownEventDigest.kt de Amethyst en el commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt)

**Mencionado en:**
- [Boletín #47: NIP en profundidad](/es/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)

**Ver también:**
- [NIP-89: Recommended Application Handlers](/es/topics/nip-89/)
- [NIP-73: External Content IDs](/es/topics/nip-73/)
- [NIP-01: Basic protocol flow description](/es/topics/nip-01/)
