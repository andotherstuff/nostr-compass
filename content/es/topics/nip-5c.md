---
title: "NIP-5C: Scrolls (programas WASM)"
date: 2026-04-08
translationOf: /en/topics/nip-5c.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Hosting
---

NIP-5C (antes NIP-A5) define convenciones para publicar, descubrir y ejecutar programas WebAssembly ("scrolls") en Nostr. Los binarios WASM se almacenan como eventos Nostr, lo que permite que cualquier cliente los obtenga y los ejecute en un runtime aislado.

## Cómo funciona

Los desarrolladores publican programas WASM como eventos Nostr que contienen el binario compilado. Los clientes descubren estos programas mediante consultas Nostr estándar, descargan el binario WASM desde el evento y lo ejecutan en un runtime WebAssembly aislado. El sandbox evita que los scrolls accedan directamente al sistema anfitrión, limitándolos a las capacidades que el runtime proporcione de forma explícita.

## Casos de uso

- **Cómputo portable**: Ejecutar programas en cualquier cliente que soporte ejecución WASM
- **Distribución descentralizada de apps**: Publicar y descubrir aplicaciones sin app stores
- **Herramientas componibles**: Encadenar scrolls para flujos de trabajo complejos

## Demo

Una [demo app](https://nprogram.netlify.app/) muestra scrolls ejecutándose en el navegador, con programas de ejemplo publicados como eventos Nostr.

---

**Fuentes primarias:**
- [NIP-5C PR #2281](https://github.com/nostr-protocol/nips/pull/2281) - propuesta Scrolls (programas WASM)

**Mencionado en:**
- [Boletín #17](/en/newsletters/2026-04-08-newsletter/)
- [Boletín #19: propuesta de applets NIP-5D](/en/newsletters/2026-04-22-newsletter/)

**Ver también:**
- [NIP-5D (Web Applets)](/es/topics/nip-5d/)
- [NIP-5A (sitios web estáticos)](/es/topics/nip-5a/)
