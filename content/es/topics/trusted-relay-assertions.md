---
title: "Aserciones de Confianza de Relays"
date: 2026-01-21
draft: false
categories:
  - Protocol
  - Relays
---

Aserciones de Confianza de Relays es una propuesta de borrador de NIP para estandarizar la puntuación de confianza de relays y gestión de reputación. La especificación introduce eventos kind 30385 donde proveedores de aserciones publican puntuaciones de confianza computadas a partir de métricas observadas, reputación del operador e informes de usuarios.

## Cómo Funciona

La propuesta llena un vacío en el ecosistema de relays. Mientras [NIP-11](/es/topics/nip-11/) define lo que los relays afirman sobre sí mismos y [NIP-66](/es/topics/nip-66/) mide lo que observamos, Aserciones de Confianza de Relays estandariza lo que concluimos sobre la confiabilidad del relay.

Los proveedores de aserciones computan puntuaciones a través de tres dimensiones. Confiabilidad mide disponibilidad, velocidad de recuperación, consistencia y latencia. Calidad evalúa documentación de políticas, seguridad TLS y responsabilidad del operador. Accesibilidad evalúa barreras de acceso, libertad jurisdiccional y riesgo de vigilancia. Una puntuación de confianza general (0-100) combina estos componentes con pesos: 40% confiabilidad, 35% calidad, 25% accesibilidad.

Cada aserción incluye niveles de confianza (bajo, medio, alto) basados en conteos de observaciones. La verificación del operador usa múltiples métodos: prueba criptográfica vía documentos NIP-11 firmados, registros DNS TXT o archivos .well-known. La especificación integra Web of Trust a través de puntuaciones de confianza del operador. La clasificación de políticas ayuda a los usuarios a encontrar relays apropiados: abierto, moderado, curado o especializado.

Los usuarios declaran proveedores de aserciones confiables vía eventos kind 10385. Los clientes consultan múltiples proveedores y comparan puntuaciones. La propuesta incluye un proceso de apelaciones donde los operadores de relay pueden disputar puntuaciones usando eventos de etiquetado de [NIP-32](/es/topics/nip-32/).

## Casos de Uso

Para firmantes remotos de [NIP-46](/es/topics/nip-46/), las aserciones de confianza ayudan a los usuarios a evaluar relays desconocidos incorporados en URIs de conexión antes de aceptar conexiones. Combinado con listas de relay de [NIP-65](/es/topics/nip-65/), los clientes pueden tomar decisiones informadas de selección de relay basadas tanto en preferencias del usuario como en evaluaciones de confianza de terceros.

La especificación complementa los mecanismos de descubrimiento de relays existentes. [NIP-66](/es/topics/nip-66/) proporciona descubrimiento (qué existe), esta propuesta añade evaluación (qué es bueno). Juntos permiten selección informada de relays en lugar de depender de valores predeterminados codificados o recomendaciones de boca en boca.

---

**Fuentes primarias:**
- [Documento de Borrador de NIP](https://nostr.com/nevent1qqsqjymvcp6ch3ps3fqsxljf6j8u3adz64ucw8npnzuj3cn6dekn0gspz9mhxue69uhkummnw3ezumrpdejz7qg3waehxw309ahx7um5wgh8w6twv5hsyga3qg) - Evento kind 30817 proponiendo la especificación

**Mencionado en:**
- [Newsletter #6: Noticias](/es/newsletters/2026-01-21-newsletter/#trusted-relay-assertions-a-new-approach-to-relay-trust)
- [Newsletter #6: Actualizaciones de NIP](/es/newsletters/2026-01-21-newsletter/#nip-updates)

**Ver también:**
- [NIP-11: Documento de Información de Relay](/es/topics/nip-11/)
- [NIP-66: Descubrimiento de Relay y Monitoreo de Actividad](/es/topics/nip-66/)
- [NIP-32: Etiquetado](/es/topics/nip-32/)
