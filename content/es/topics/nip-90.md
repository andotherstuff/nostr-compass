---
title: "NIP-90"
date: 2026-02-25
translationOf: /en/topics/nip-90.md
translationDate: 2026-02-25
draft: false
categories:
  - NIP
  - DVM
---

NIP-90 define Data Vending Machines (DVMs), un protocolo de mercado para solicitar y pagar por trabajo computacional en Nostr.

## Cómo Funciona

Los clientes publican eventos de solicitud de trabajo (kinds 5000-5999) especificando el trabajo necesario. Los proveedores de servicio monitorean solicitudes que coincidan con sus capacidades y publican resultados después de completar la computación. El pago ocurre a través de Lightning u otros mecanismos negociados en el flujo de trabajo.

Los kinds de trabajo definen diferentes tipos de computación: generación de texto, generación de imágenes, traducción, descubrimiento de contenido, y más. Cada kind especifica el formato de entrada/salida esperado.

## Características Clave

- Mercado de computación descentralizado
- Sistema de tipo de trabajo basado en kind
- Competencia de proveedores en precio y calidad
- Extensible para nuevos tipos de computación

---

**Fuentes primarias:**
- [Especificación NIP-90](https://github.com/nostr-protocol/nips/blob/master/90.md)

**Mencionado en:**
- [Newsletter #11: Coordinación de Agentes DVM NIP-AC](/es/newsletters/2026-02-25-newsletter/#actualizaciones-de-nips)

**Ver también:**
- [NIP-85: Aserciones de Confianza](/es/topics/nip-85/)
