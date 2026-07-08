---
title: "NIP-82: Aplicaciones de software"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-82.md
translationDate: 2026-07-01
categories:
  - Discovery
  - Apps
---

NIP-82 define un evento de aplicación de software para que los clientes de Nostr puedan mostrar aplicaciones (APKs de Android, apps de iOS, aplicaciones web, binarios de escritorio) como objetos de primera clase en feeds y superficies de descubrimiento. La especificación reemplaza el enfoque anterior de describir aplicaciones mediante notas genéricas de kind 1 o recomendaciones de manejador [NIP-89](/es/topics/nip-89/) con un evento dedicado y estructurado que transporta metadatos de la aplicación, capturas de pantalla, enlaces al repositorio e identidad del autor.

## Cómo funciona

Una aplicación de software NIP-82 es un único evento reemplazable direccionado por pubkey del autor y tag `d`. El evento transporta:

- Tags `name`, `description`, `icon`, `image` para visualización
- Tags `repository` y `web` para las URLs del código fuente y la página principal
- Tag `platforms` que enumera los objetivos soportados (android, ios, web, linux, macos, windows)
- Tags `download` para cada binario o URL web específico de plataforma
- Tags `screenshots` que transportan URLs de imágenes para las capturas de pantalla de la aplicación
- Tags de tópico `t` para categorización
- Tag `version` para la versión actual publicada

Un cliente que navega un feed NIP-82 puede mostrar la tarjeta de la aplicación, enlazar al repositorio canónico y mostrar capturas de pantalla sin recurrir al scraping de una publicación de formato largo de Nostr o de una tienda de aplicaciones de terceros. La pubkey del autor es la fuente de verdad para la aplicación, por lo que un cliente puede verificar que el publicador coincide con la identidad esperada del desarrollador antes de promocionar un enlace de descarga.

## Semántica del feed

Los eventos NIP-82 son direccionables, por lo que cada aplicación tiene un evento reemplazable canónico por autor. Un desarrollador que publica una nueva versión reemplaza el evento anterior en su lugar, y los suscriptores ven la actualización sin gestionar historial de eventos. Los clientes que quieran un registro de cambios pueden suscribirse al evento direccionable y mostrar los incrementos de versión como actividad en la superficie de la aplicación.

La especificación se compone con [NIP-89](/es/topics/nip-89/) (Manejadores de aplicación): un evento NIP-82 describe la aplicación como un artefacto, mientras que un evento NIP-89 describe que la aplicación puede manejar kinds de evento específicos. Los clientes pueden usar uno sin el otro, pero la pareja proporciona una superficie de descubrimiento (NIP-82) y una superficie de delegación (NIP-89) que funcionan juntas.

## Implementaciones

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) incorpora un feed dedicado a aplicaciones de software NIP-82 con una pantalla de detalle, información del autor y capturas de pantalla ([PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036), [PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078), [PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200))

---

**Fuentes primarias:**
- [Especificación NIP-82](https://github.com/nostr-protocol/nips/blob/master/82.md)
- [Amethyst PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036) - Añadir soporte de Aplicaciones de Software NIP-82 con feed dedicado
- [Amethyst PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078) - Añadir pantalla de detalle dedicada para aplicaciones de software NIP-82
- [Amethyst PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200) - Mejorar la UI de aplicaciones de software NIP-82 con información del autor y capturas de pantalla

**Mencionado en:**
- [Boletín #27: Amethyst v1.12.0 incorpora wallets Cashu, nutzaps, un driver CLINK y auto-reparación de Tor](/es/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**Véase también:**
- [NIP-89: Manejadores de aplicación](/es/topics/nip-89/)
