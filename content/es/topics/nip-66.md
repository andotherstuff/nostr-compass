---
title: "NIP-66: Descubrimiento de Relays y Monitoreo de Disponibilidad"
date: 2026-01-21
translationOf: /en/topics/nip-66.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Relays
---

NIP-66 estandariza la publicación de datos de monitoreo de relays en Nostr. Los servicios de monitoreo prueban continuamente los relays para disponibilidad, latencia, cumplimiento del protocolo y NIPs soportados, publicando resultados como eventos kind 30166.

## Cómo Funciona

Los monitores verifican la disponibilidad de relays conectándose y enviando suscripciones de prueba. Las mediciones de latencia rastrean el tiempo de conexión, tiempo de respuesta de suscripción y retraso de propagación de eventos. Las pruebas de cumplimiento del protocolo verifican que el comportamiento del relay coincida con las especificaciones, detectando bugs de implementación o desviaciones intencionales.

La verificación de soporte de NIPs va más allá de las declaraciones de [NIP-11](/es/topics/nip-11/) probando realmente si las funciones anunciadas funcionan correctamente. Si un relay declara soporte de búsqueda [NIP-50](/es/topics/nip-50/) pero las consultas de búsqueda fallan, los monitores omitirán NIP-50 de la lista verificada. Esto proporciona la verdad básica sobre las capacidades del relay.

Los eventos kind 30166 usan la URL del relay como tag `d`, haciéndolos eventos reemplazables parametrizados. Cada monitor publica un evento por relay, actualizado conforme cambian las mediciones. Múltiples monitores pueden rastrear el mismo relay, proporcionando redundancia y validación cruzada.

Los tags de tiempo de ida y vuelta (rtt) miden latencia para diferentes operaciones:
- `rtt open`: Establecimiento de conexión WebSocket
- `rtt read`: Tiempo de respuesta de suscripción
- `rtt write`: Velocidad de publicación de eventos

Todos los valores están en milisegundos. Los clientes usan estas métricas para preferir relays de baja latencia para operaciones sensibles al tiempo.

La información geográfica ayuda a los clientes a seleccionar relays cercanos para mejor latencia y resistencia a la censura. El tag `geo` contiene código de país, nombre de país y región. El tag `network` distingue relays clearnet de servicios ocultos Tor o endpoints I2P.

## Casos de Uso

Los datos de monitoreo alimentan selectores de relays en clientes, sitios web exploradores y sistemas de evaluación de confianza. Al proporcionar estado de relay en tiempo real independiente del auto-reporte del relay, NIP-66 permite selección informada de relays.

Combinado con [NIP-11](/es/topics/nip-11/) (capacidades auto-reportadas) y Trusted Relay Assertions (evaluación de confianza), el ecosistema avanza hacia selección de relays basada en datos en lugar de depender de valores predeterminados codificados.

---

**Fuentes primarias:**
- [Especificación NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) - Estándar de descubrimiento de relays y monitoreo de disponibilidad

**Mencionado en:**
- [Newsletter #6: Análisis Profundo de NIPs](/es/newsletters/2026-01-21-newsletter/#nip-deep-dive-nip-11-and-nip-66)

**Ver también:**
- [NIP-11: Documento de Información de Relay](/es/topics/nip-11/)
- [Trusted Relay Assertions](/es/topics/trusted-relay-assertions/)
