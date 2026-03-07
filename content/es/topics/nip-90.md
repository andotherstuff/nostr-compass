---
title: "NIP-90: Data Vending Machines"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - DVM
---

NIP-90 define Data Vending Machines (DVMs), un protocolo para solicitar y entregar trabajo computacional pagado a través de Nostr.

## Cómo funciona

Los clientes publican eventos de solicitud de trabajo en el rango `5000-5999`. Cada solicitud puede incluir una o más etiquetas `i` para entradas, etiquetas `param` para configuraciones específicas del trabajo, una etiqueta `output` para el formato esperado, un techo `bid`, e indicaciones de relay para dónde deberían aparecer las respuestas. Los proveedores de servicio responden con un kind de resultado correspondiente en el rango `6000-6999`, siempre `1000` por encima del kind de la solicitud.

Los resultados incluyen la solicitud original, la pubkey del cliente, y opcionalmente una etiqueta `amount` o factura. Los proveedores también pueden enviar eventos de retroalimentación kind `7000` como `payment-required`, `processing`, `partial`, `error` o `success`, lo que da a los clientes una forma de mostrar progreso antes de que llegue el resultado final.

## Pago y privacidad

El protocolo deja la lógica de negocio abierta de forma intencional. Un proveedor puede solicitar pago antes de iniciar el trabajo, después de devolver una muestra, o después de entregar el resultado completo. Esa flexibilidad importa porque los trabajos DVM van desde transformaciones de texto baratas hasta trabajo GPU costoso, y los proveedores no asumen todos el mismo riesgo de pago.

Si un cliente quiere entradas privadas, la solicitud puede mover datos `i` y `param` al `content` cifrado y marcar el evento con una etiqueta `encrypted` más la etiqueta `p` del proveedor. Eso protege prompts o material fuente de observadores en los relays, pero también significa que el cliente debe dirigirse a un proveedor específico en lugar de transmitir una solicitud abierta al mercado.

## Notas de interoperabilidad

NIP-90 soporta encadenamiento de trabajos a través de etiquetas `i` con tipo de entrada `job`, de modo que un resultado puede alimentar una solicitud posterior. Eso hace posibles flujos de múltiples pasos sin inventar una capa de orquestación separada.

El descubrimiento de proveedores está fuera del bucle de solicitud/respuesta. La especificación apunta a anuncios de [NIP-89: Recommended Application Handlers](/es/topics/nip-89/) para publicitar kinds de trabajo soportados, que es cómo los clientes pueden descubrir proveedores antes de publicar una solicitud.

---

**Fuentes primarias:**
- [Especificación NIP-90](https://github.com/nostr-protocol/nips/blob/master/90.md)

**Mencionado en:**
- [Newsletter #11: NIP-AC DVM Agent Coordination](/en/newsletters/2026-02-25-newsletter/#nip-updates)

**Ver también:**
- [NIP-89: Recommended Application Handlers](/es/topics/nip-89/)
