---
title: "Aserciones de Confianza de Relays"
date: 2026-01-21
translationOf: /en/topics/trusted-relay-assertions.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Relays
---

Aserciones de Confianza de Relays es la idea de publicar evaluaciones firmadas de terceros sobre relays en Nostr para que los clientes puedan elegir relays con más contexto que solo los metadatos auto-reportados. El bloque de construcción estandarizado actual es [NIP-85: Trusted Assertions](/es/topics/nip-85/), que define cómo los usuarios confían en proveedores y cómo los proveedores publican resultados computados firmados.

## Cómo funciona

La selección de relay tiene tres capas. [NIP-11: Relay Information Document](/es/topics/nip-11/) cubre lo que un relay dice sobre sí mismo. [NIP-66: Relay Discovery and Liveness Monitoring](/es/topics/nip-66/) cubre lo que los observadores pueden medir, como disponibilidad y latencia. Las aserciones de confianza de relays intentan llenar el vacío restante: lo que un tercero concluye a partir de esos datos, y si un cliente decide confiar en esa conclusión.

En el modelo más amplio de NIP-85, los usuarios nombran proveedores de confianza con eventos kind `10040`, y los proveedores publican eventos de aserción direccionables firmados. Una aplicación de puntuación de relays necesitaría entonces dos piezas adicionales en las que los clientes estén de acuerdo: cómo se identifica un relay como sujeto, y qué etiquetas de resultado representan la puntuación y su evidencia de soporte.

Esa distinción es relevante porque el transporte y la delegación de confianza están estandarizados, pero el modelo de puntuación específico de relays sigue siendo un patrón de aplicación. Diferentes proveedores pueden legítimamente discrepar sobre qué hace a un relay confiable.

## Modelo de confianza

Las puntuaciones de confianza de relays no son hechos objetivos. Un proveedor puede priorizar el tiempo de actividad y el rendimiento de escritura, otro puede priorizar la jurisdicción legal, la política de moderación o la identidad del operador, y un tercero puede importarle más la resistencia a la vigilancia. Un cliente útil debería mostrar quién produjo la puntuación, no solo la puntuación misma.

Aquí es también donde [Web of Trust](/es/topics/web-of-trust/) entra en juego. Si un cliente ya confía en ciertas personas o servicios, puede preferir evaluaciones de relays provenientes de ese mismo vecindario social en lugar de pretender que existe un ranking global único.

## Por qué importa

Para firmantes remotos de [NIP-46](/es/topics/nip-46/), conexiones de wallet, o cualquier aplicación que sugiera relays desconocidos, las evaluaciones de terceros sobre relays pueden reducir la confianza ciega en valores por defecto. Combinado con listas de relays de [NIP-65](/es/topics/nip-65/), los clientes pueden separar "qué relays uso" de "en qué relays confío para esta tarea."

La principal advertencia de corrección es el alcance. La cobertura del newsletter de enero 2026 describió la puntuación de confianza de relays como una propuesta dedicada, pero el estándar fusionado en el repositorio de NIPs es el formato más amplio de [NIP-85: Trusted Assertions](/es/topics/nip-85/). La puntuación de relays sigue siendo un caso de uso construido sobre ese modelo, no un formato de cable de confianza de relays finalizado por separado.

---

**Fuentes primarias:**
- [Especificación NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #1534: Trusted Assertions](https://github.com/nostr-protocol/nips/pull/1534)

**Mencionado en:**
- [Newsletter #6: News](/en/newsletters/2026-01-21-newsletter/#trusted-relay-assertions-a-new-approach-to-relay-trust)
- [Newsletter #6: NIP Updates](/en/newsletters/2026-01-21-newsletter/#nip-updates)
- [Newsletter #7: NIP Updates](/en/newsletters/2026-01-28-newsletter/#nip-updates)

**Ver también:**
- [NIP-11: Relay Information Document](/es/topics/nip-11/)
- [NIP-66: Relay Discovery and Liveness Monitoring](/es/topics/nip-66/)
- [NIP-85: Trusted Assertions](/es/topics/nip-85/)
- [Web of Trust](/es/topics/web-of-trust/)
