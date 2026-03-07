---
title: "ContextVM"
date: 2026-02-25
translationOf: /en/topics/contextvm.md
translationDate: 2026-03-07
draft: false
categories:
  - Infrastructure
  - AI
  - Protocol
---

ContextVM es un protocolo y conjunto de herramientas para transportar tráfico MCP (Model Context Protocol) sobre Nostr. Permite que clientes y servidores MCP se encuentren e intercambien mensajes firmados sin depender de un registro central, dominios u OAuth.

## Cómo Funciona

El SDK de ContextVM proporciona transportes TypeScript de cliente y servidor para MCP sobre Nostr. Los servidores MCP existentes pueden permanecer en sus transportes normales mientras un gateway los expone a Nostr, y los clientes sin soporte nativo de Nostr pueden conectarse a través de una capa proxy.

Los relays actúan como bus de mensajes. Enrutan eventos, mientras que la firma y el cifrado proporcionan autenticación y privacidad de transporte a los endpoints.

## Componentes

**SDK**: Biblioteca TypeScript con transportes de cliente/servidor, soporte de proxy y funcionalidad de gateway para conectar servidores MCP locales a Nostr.

**CVMI**: Interfaz de línea de comandos para descubrimiento de servidores e invocación de métodos.

**Relatr**: Servicio de puntuación de confianza que calcula puntuaciones personalizadas a partir de la distancia en el grafo social y la validación de perfiles.

## Por Qué Es Importante

ContextVM es un puente de transporte, no un reemplazo de MCP en sí. Eso importa porque reduce el costo de adopción: un servidor MCP existente puede ganar accesibilidad en Nostr sin reescribir su esquema de herramientas o lógica de negocio.

El trabajo reciente de ContextVM también impulsó la entrega efímera para tráfico gift-wrapped. Eso es útil para llamadas a herramientas y respuestas intermedias donde el almacenamiento duradero en relays es innecesario y puede crear exposición adicional de privacidad.

## Notas de Interoperabilidad

En febrero y marzo de 2026, el proyecto pasó de la implementación hacia la estandarización. El equipo abrió propuestas NIP para MCP JSON-RPC sobre Nostr y para una variante efímera de gift wrap. Aunque esas propuestas cambien, muestran el límite del protocolo con mayor claridad: MCP sigue siendo la capa de aplicación, Nostr maneja el descubrimiento y el transporte.

---

**Fuentes primarias:**
- [Sitio web de ContextVM](https://contextvm.org)
- [SDK de ContextVM](https://github.com/ContextVM/sdk)
- [CVMI CLI](https://github.com/ContextVM/cvmi)
- [Relatr](https://github.com/ContextVM/relatr)
- [NIP PR #2245: Gift Wrap Efímero](https://github.com/nostr-protocol/nips/pull/2245)
- [NIP PR #2246: MCP JSON-RPC sobre Nostr](https://github.com/nostr-protocol/nips/pull/2246)

**Mencionado en:**
- [Boletín #11: Noticias de ContextVM](/es/newsletters/2026-02-25-newsletter/#contextvm-mcp-over-nostr)
- [Boletín #12](/es/newsletters/2026-03-04-newsletter/)

**Ver también:**
- [NIP-90: Data Vending Machines](/es/topics/nip-90/)
