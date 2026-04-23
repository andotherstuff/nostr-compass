---
title: "Protocolo Marmot"
date: 2025-12-17
translationOf: /en/topics/marmot.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmot es un protocolo para mensajería grupal cifrada de extremo a extremo en Nostr. Combina la identidad y red de relays de Nostr con MLS para gestión de claves de grupo, forward secrecy y seguridad post-compromiso.

## Cómo funciona

Marmot usa Nostr para identidad, transporte por relays y distribución de eventos, y luego superpone MLS para cambios de membresía grupal y cifrado de mensajes. A diferencia de [NIP-17](/es/topics/nip-17/), que se centra en mensajería uno a uno, Marmot está construido para grupos donde los miembros se unen, salen o rotan claves con el tiempo.

## Por qué importa

MLS le da a Marmot propiedades que los esquemas de mensajes directos de Nostr no proporcionan por sí solos: evolución del estado del grupo, semántica de eliminación de miembros y recuperación después de un compromiso a través de actualizaciones posteriores de claves.

Esa división del trabajo es la idea útil. Nostr resuelve identidad y transporte en una red abierta. MLS resuelve el acuerdo autenticado de claves de grupo. Marmot es la capa de unión entre ambos.

## Estado de implementación

El protocolo sigue siendo experimental, pero ahora tiene múltiples implementaciones y uso activo en aplicaciones. [MDK](https://github.com/marmot-protocol/mdk) es el stack de referencia principal en Rust, [marmot-ts](https://github.com/marmot-protocol/marmot-ts) lleva el modelo a TypeScript, y aplicaciones como [White Noise](https://github.com/marmot-protocol/whitenoise), [Amethyst](https://github.com/vitorpamplona/amethyst), Pika y Vector han estado usando componentes compatibles con Marmot.

El trabajo reciente se ha centrado en endurecimiento e interoperabilidad. Las correcciones impulsadas por auditoría se integraron a principios de 2026, y MIP-03 introdujo la resolución determinista de commits para que los clientes puedan converger cuando cambios concurrentes de estado de grupo compiten a través de relays.

En abril de 2026, Amethyst alineó su MDK embebido con los formatos wire de MIP-01 y MIP-05: [PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) añadió codificación VarInt de prefijos de longitud estilo TLS y validación de ida y vuelta contra vectores de test de MDK, [PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) añadió soporte para MIP-00 KeyPackage Relay List y [PR #2436](https://github.com/vitorpamplona/amethyst/pull/2436) cerró los huecos restantes de admin-gate y manejo de medios detectados por pruebas cross-client contra White Noise. [PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466) corrigió el framing de commits MLS para que los bytes de welcome cifrados coincidan con la salida de mdk-core, y [PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471) arregló un bug de descifrado de capa externa que causaba divergencia de estado entre co-admins. El siguiente [PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493) añade validación integral de criptografía de commits MLS, y [PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) lanza `amy`, una interfaz CLI para operaciones de grupos Marmot y MLS impulsada por la implementación de Amethyst.

MDK integró [PR #261](https://github.com/marmot-protocol/mdk/pull/261) para calcular `RequiredCapabilities` de un grupo como el LCD de las capacidades de los invitados, lo que desbloquea invites entre versiones mixtas de Amethyst y White Noise, [PR #262](https://github.com/marmot-protocol/mdk/pull/262) para parsear key packages de invitados antes de persistir el signer del creador, [PR #264](https://github.com/marmot-protocol/mdk/pull/264) para converger el formato wire de SelfUpdate entre implementaciones y [PR #265](https://github.com/marmot-protocol/mdk/pull/265) para exponer un accesor `group_required_proposals`.

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) está en medio de un refactor por fases desde singletons globales hacia vistas `AccountSession` por cuenta: [PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743) estableció la base de `AccountSession` y `AccountManager`, y las fases posteriores han migrado handles de relay, drafts y settings, operaciones de mensajes, lectura y escritura de grupos, membresía, notificaciones push, lecturas de key packages, creación de grupos y, a partir de [PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770), despacho de eventos con alcance de sesión. [marmot-ts PR #68](https://github.com/marmot-protocol/marmot-ts/pull/68) migra el cliente TypeScript a key packages direccionables kind `30443`.

---

**Fuentes primarias:**
- [Repositorio del Protocolo Marmot](https://github.com/marmot-protocol/marmot)
- [MLS Protocol](https://messaginglayersecurity.rocks/)
- [Marmot Development Kit](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)
- [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)
- [White Noise client](https://github.com/marmot-protocol/whitenoise)
- [Amethyst PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) - alineación de formato wire MIP-01/MIP-05
- [Amethyst PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) - MIP-00 KeyPackage Relay List
- [Amethyst PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) - CLI Amy

**Mencionado en:**
- [Boletín #1: Noticias](/es/newsletters/2025-12-17-newsletter/)
- [Boletín #1: Lanzamientos](/es/newsletters/2025-12-17-newsletter/)
- [Boletín #4](/es/newsletters/2026-01-07-newsletter/)
- [Boletín #7](/es/newsletters/2026-01-28-newsletter/)
- [Boletín #12](/es/newsletters/2026-03-04-newsletter/)
- [Boletín #19: cumplimiento MIP en Amethyst](/en/newsletters/2026-04-22-newsletter/)
- [Boletín #19: trabajo de interop en MDK](/en/newsletters/2026-04-22-newsletter/)
- [Boletín #19: refactor de sesión en whitenoise-rs](/en/newsletters/2026-04-22-newsletter/)

**Ver también:**
- [MLS (Message Layer Security)](/es/topics/mls/)
- [MIP-05: Notificaciones Push que Preservan la Privacidad](/es/topics/mip-05/)
- [NIP-17: Mensajes Directos Privados](/es/topics/nip-17/)
- [NIP-59: Gift Wrap](/es/topics/nip-59/)
