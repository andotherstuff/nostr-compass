---
title: 'Nostr Compass #21'
date: 2026-05-06
publishDate: 2026-05-06
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-06-newsletter.md
translationDate: 2026-05-13
description: 'Marmot Protocol lanza MDK 0.8.0 con primitivas de notificación MIP-05 y paquetes de claves direccionables; LaWallet NWC lanza v0.10.0 con el monorepo completo, panel de administración, Wallet para usuarios finales y un nuevo esquema LightningAddress a NWCConnection; Amethyst Nests se estabiliza con relay keep-alive, suscripciones con conciencia del ciclo de vida, continuidad de audio en refresco JWT e indicadores de hablantes visibles; ngit lanza v2.4.2 y v2.4.3 corrigiendo la detección del servidor GRASP y el filtrado de eventos de estado multi-remoto; GRAIN v0.5.4 trae endurecimiento de producción; Mostro Core v0.10.1 sigue al módulo de protocolo de chat P2P v0.10.0 de la semana pasada con artefactos de lanzamiento firmados con PGP; Clave v0.2.0 introduce soporte multi-cuenta en iOS; nostream añade soporte de relay para Marmot Protocol y reacciones NIP-25; Sprout lanza Desktop v0.0.4 y v0.0.5 junto con autenticación de agente NIP-OA para membresía NIP-43 y un sidecar de emparejamiento efímero; Angor 0.2.21 lanza flujos de app compactos; Routstrd integra Hermes para clientes daemon; micro-vpn-ansible se une al conjunto de repos NIP-34 rastreados. Dos inmersiones profundas en NIP cubren NIP-34 (git stuff) y NIP-53 (Actividades en Vivo).'
---

Bienvenido de nuevo a Nostr Compass, tu guía semanal de Nostr.

**Esta semana:** [Marmot Protocol](https://github.com/marmot-protocol) lanza [MDK 0.8.0](#mdk-080-añade-primitivas-de-notificación-mip-05-y-paquetes-de-claves-direccionables) con las primeras primitivas de notificación MIP-05, paquetes de claves [NIP-51 (Listas)](/es/topics/nip-51/) direccionables y una revisión de seguridad mejorada. [LaWallet NWC](https://github.com/lawalletio/lawallet-nwc) lanza [v0.10.0](#lawallet-nwc-v0100-lanza-el-monorepo-completo-y-wallet-para-usuarios-finales) como el mayor lanzamiento desde la financiación de OpenSats. [Amethyst](https://github.com/vitorpamplona/amethyst) realiza un [sprint de estabilidad de Nests](#amethyst-estabiliza-nests-con-keep-alive-resiliencia-jwt-y-suscripciones-de-ciclo-de-vida). [ngit](https://github.com/DanConwayDev/ngit-cli) lanza [v2.4.2](#ngit-v242-y-v243-corrigen-detección-del-servidor-grasp-y-eventos-de-estado-multi-remoto) y [v2.4.3](#ngit-v242-y-v243-corrigen-detección-del-servidor-grasp-y-eventos-de-estado-multi-remoto). [GRAIN](https://github.com/0ceanSlim/grain) lanza [v0.5.4](#grain-v054-trae-endurecimiento-de-producción-y-una-corrección-silenciosa-de-pérdida-de-datos). [Mostro Core](https://github.com/MostroP2P/mostro-core) lanza [v0.10.1](#mostro-core-v0101-añade-artefactos-de-lanzamiento-firmados-con-pgp). [Clave](https://github.com/clave-mobile) lanza [v0.2.0](#clave-v020-lanza-multi-cuenta-en-ios-con-firma-nip-46-nostr-connect).

## Historias principales

### MDK 0.8.0 añade primitivas de notificación MIP-05 y paquetes de claves direccionables

[MDK](https://github.com/marmot-protocol/mdk), la biblioteca principal en Rust para el protocolo [Marmot](/es/topics/marmot/), lanzó [v0.8.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.8.0) el 4 de mayo. Esta versión incluye los primeros bloques de construcción de notificaciones MIP-05, mueve los paquetes de claves MIP-00 a eventos direccionables para que el paquete de claves de un usuario pueda reemplazarse en su lugar, mejora la compatibilidad de grupo de versiones mixtas, amplía la cobertura UniFFI para bindings móviles y refuerza las rutas de validación. Las primitivas MIP-05 incluyen auxiliares de índice de hoja añadidos en [PR #235](https://github.com/marmot-protocol/mdk/pull/235), que dan a los clientes posteriores suficiente información para entregar notificaciones push por destinatario sin exponer la estructura del grupo. [PR #273](https://github.com/marmot-protocol/mdk/pull/273) restaura la publicación de mdk-core en crates.io, y [PR #269](https://github.com/marmot-protocol/mdk/pull/269) expone el módulo test_util detrás de una característica Cargo `test-utils`.

### LaWallet NWC v0.10.0 lanza el monorepo completo y Wallet para usuarios finales

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc), la implementación [NIP-47](/es/topics/nip-47/) Nostr Wallet Connect del equipo de LaWallet, lanzó [v0.10.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v0.10.0) el 30 de abril. Es el mayor lanzamiento desde que el proyecto recibió financiación de OpenSats. Incluye el monorepo completo, el panel de administración completo, una Wallet para usuarios finales, un registro de actividad completo, branding dinámico y el nuevo esquema `LightningAddress 1→N` y `NWCConnection` que desbloquea el enrutamiento NWC por dirección. La Wallet para el usuario lanzada en [PR #191](https://github.com/lawalletio/lawallet-nwc/pull/191) cubre incorporación, inicio, envío/recepción, escaneo, monedas, un feed de actividad y una caché sin conexión.

### Amethyst estabiliza Nests con keep-alive, resiliencia JWT y suscripciones de ciclo de vida

[Amethyst](https://github.com/vitorpamplona/amethyst), el cliente Android con muchas funciones, continuó el trabajo de sala de audio [NIP-53](/es/topics/nip-53/) Nests cubierto en el boletín [#20](/es/newsletters/2026-04-29-newsletter/#amethyst-advances-nests-audio-rooms-with-moq-interop-testing) con un sprint de estabilidad. La corrección de brecha de audio en [PR #2733](https://github.com/vitorpamplona/amethyst/pull/2733) superpone la nueva adquisición de credenciales con el flujo activo durante el refresco JWT, para que el oyente no escuche un corte cuando rota el token. Un nuevo mecanismo keep-alive en [PR #2730](https://github.com/vitorpamplona/amethyst/pull/2730) reconecta relays desconectados sin requerir acción manual del usuario, y [PR #2728](https://github.com/vitorpamplona/amethyst/pull/2728) reemplaza el `KeyDataSourceSubscription` heredado con `LifecycleAwareKeyDataSourceSubscription`. [PR #2724](https://github.com/vitorpamplona/amethyst/pull/2724) añade un indicador de anillo exterior animado que resalta al participante que habla en sesiones con múltiples hablantes.

### ngit v2.4.2 y v2.4.3 corrigen detección del servidor GRASP y eventos de estado multi-remoto

[ngit](https://github.com/DanConwayDev/ngit-cli), la herramienta de línea de comandos y plugin `git` para la colaboración [NIP-34](/es/topics/nip-34/), lanzó [v2.4.2](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.2) el 28 de abril y [v2.4.3](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.3) el 1 de mayo. v2.4.2 corrige un desajuste de normalización de URL donde `repo_grasps` mantenía nombres de host normalizados pero la comparación se hacía contra URLs de clonación completas. v2.4.3 corrige una ambigüedad de evento de estado que surgía cuando un repositorio tiene múltiples remotos `nostr://` compartiendo el mismo identificador.

### GRAIN v0.5.4 trae endurecimiento de producción y una corrección silenciosa de pérdida de datos

[GRAIN](https://github.com/0ceanSlim/grain), la biblioteca relay y cliente Nostr basada en Go, lanzó [v0.5.4](https://github.com/0ceanSlim/grain/releases/tag/v0.5.4) el 30 de abril. La versión acumula seis correcciones desde v0.5.3, incluyendo un bug silencioso de pérdida de datos en el inicio rápido de Docker que anteriormente descartaba eventos cuando el contenedor se reiniciaba, y un bug de corrección de la capa de almacenamiento en lecturas de eventos direccionables.

### Mostro Core v0.10.1 añade artefactos de lanzamiento firmados con PGP

[Mostro Core](https://github.com/MostroP2P/mostro-core), la biblioteca Rust que proporciona funcionalidad peer-to-peer para el daemon Mostro, lanzó [v0.10.1](https://github.com/MostroP2P/mostro-core/releases/tag/v0.10.1) el 28 de abril como seguimiento del [módulo de protocolo de chat P2P v0.10.0 de la semana pasada](/es/newsletters/2026-04-29-newsletter/#mostro-core-v0100-and-mostro-mobile-v125-adopt-nip-59-dual-key-gift-wrap). La nueva versión añade artefactos de lanzamiento firmados con PGP y un flujo `verify-release`.

## Lanzamientos etiquetados

### Clave v0.2.0 lanza multi-cuenta en iOS con firma NIP-46 (Nostr Connect)

[Clave](https://github.com/clave-mobile), la app de firma remota [NIP-46](/es/topics/nip-46/) para iOS cubierta en [#20](/es/newsletters/2026-04-29-newsletter/#clave-brings-nip-46-remote-signing-to-ios-via-apns), lanzó [v0.2.0](https://github.com/clave-mobile/clave/releases) el 5 de mayo. La mayor actualización hasta ahora introduce soporte multi-cuenta: Clave ahora puede albergar hasta cuatro cuentas en un dispositivo, con un selector de un toque y aislamiento por cuenta.

### Wisp lanza trabajo de estabilidad v1.0.3 → v1.0.5

[Wisp](https://github.com/barrydeen/wisp), el cliente Android que [se graduó de beta en #20](/es/newsletters/2026-04-29-newsletter/#wisp-v100-graduates-from-beta), lanzó [v1.0.3](https://github.com/barrydeen/wisp/releases/tag/v1.0.3), [v1.0.4](https://github.com/barrydeen/wisp/releases/tag/v1.0.4) y [v1.0.5](https://github.com/barrydeen/wisp/releases/tag/v1.0.5) el 4 de mayo con trabajo de estabilidad.

### Amber 6.1.0-pre1 lanza correcciones de diseño y estabilidad

[Amber](https://github.com/greenart7c3/Amber), la app firmadora Android para [NIP-55 (Aplicación firmadora Android)](/es/topics/nip-55/) y [NIP-46](/es/topics/nip-46/), lanzó [v6.1.0-pre1](https://github.com/greenart7c3/Amber/releases) con un pase de diseño en el flujo de conexión de nueva app y varias correcciones de fallos reportados.

### Routstr Core v0.4.3 mejora el manejo de pagos, reembolsos y reportes de uso

[Routstr Core](https://github.com/Routstr/routstr-core), la capa de inferencia descentralizada, lanzó [v0.4.3](https://github.com/Routstr/routstr-core/releases) como pre-lanzamiento el 1 de mayo.

### Nostria v3.1.37 a v3.1.41 añaden Marcadores Web y un tema Auto

[Nostria](https://github.com/nostria-app/nostria), el cliente Nostr multiplataforma, lanzó [v3.1.37 a v3.1.41](https://github.com/nostria-app/nostria/releases) el 30 de abril y el 4 de mayo. Las versiones añaden soporte [NIP-B0 (Marcadores Web)](/es/topics/nip-b0/), un tema "Auto" que sigue la configuración del dispositivo y visualización de PDF en la app.

## Cambios no publicados

### Sprout lanza Desktop v0.0.4 y v0.0.5 junto con autenticación de agente NIP-OA y el sidecar relay de emparejamiento

[Sprout](https://github.com/block/sprout), el cliente Nostr de Block con relay integrado, lanzó [Sprout Desktop v0.0.4](https://github.com/block/sprout/releases) el 5 de mayo y [v0.0.5](https://github.com/block/sprout/releases) el 6 de mayo, junto con aproximadamente 80 PRs fusionados. El cambio principal en [PR #471](https://github.com/block/sprout/pull/471) conecta la autenticación de agente NIP-OA al flujo de membresía NIP-43 del relay. Un nuevo relay sidecar efímero para emparejamiento de dispositivos NIP-AB llega en [PR #467](https://github.com/block/sprout/pull/467) como `sprout-pair-relay`.

### nostream añade soporte de relay Marmot y reacciones NIP-25

[nostream](https://github.com/Cameri/nostream), la implementación de relay Node.js, fusionó una semana productiva de adiciones de protocolo. El soporte de relay Marmot Protocol que cubre los MIPs 00 al 03 llega en [PR #602](https://github.com/Cameri/nostream/pull/602). Las adiciones de protocolo menores: soporte de reacciones [NIP-25](/es/topics/nip-25/) en [PR #589](https://github.com/Cameri/nostream/pull/589).

### strfry añade observabilidad por conexión y reduce el límite nofiles

[strfry](https://github.com/hoytech/strfry), el relay Nostr en C++, fusionó 14 PRs orientados a la observabilidad e higiene operativa. El cambio principal es [PR #218](https://github.com/hoytech/strfry/pull/218), que añade observabilidad de salida pendiente por conexión y un límite de contrapresión configurable.

### Damus reemplaza los GIFs de Tenor con un proxy Purple y lanza UX de compactación

[Damus](https://github.com/damus-io/damus), el cliente iOS de Nostr, fusionó [PR #3737](https://github.com/damus-io/damus/pull/3737) reemplazando la integración de GIFs Tenor con un proxy [Damus Purple](https://damus.io/purple/).

### routstrd-auth: un Routstrd dockerizado para equipos con auth NIP-98 y RBAC por npub

[routstrd-auth](https://github.com/Routstr/routstrd-auth), creado el 27 de abril por el equipo de Routstr, es una variante dockerizada de Routstrd para implementaciones en equipos multiusuario. El cambio principal es un sistema granular de control de acceso basado en roles por npub con roles `admin` y `user`, y endpoints de cliente que adoptan autenticación HTTP [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md).

### Routstrd integra Hermes para clientes daemon y modo remoto

[Routstrd](https://github.com/routstr/routstrd), el daemon local que orquesta clientes de inferencia Routstr, fusionó [PR #22](https://github.com/routstr/routstrd/pull/22) añadiendo integración con [Hermes Agent](https://github.com/NousResearch/hermes-agent).

### whitenoise-rs lanza aislamiento de base de datos por cuenta y actualizaciones de propuestas

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs), la biblioteca Rust principal para el mensajero White Noise, fusionó [PR #796](https://github.com/marmot-protocol/whitenoise-rs/pull/796) moviendo tablas de proyección de mensajes a bases de datos por cuenta, y [PR #791](https://github.com/marmot-protocol/whitenoise-rs/pull/791) añadiendo actualizaciones de propuestas para que los grupos puedan extender su funcionalidad.

### Angor 0.2.21 lanza flujos de app compactos junto con endurecimiento del proveedor de claves y cambio de red

[Angor](https://github.com/block-core/angor), la plataforma de crowdfunding Bitcoin con perfiles de fundadores publicados en Nostr, lanzó [Angor 0.2.21](https://github.com/block-core/angor/releases) el 6 de mayo.

## Recién rastreados y descubiertos

### BitMacro Signer: un bunker NIP-46 autoalojable con cifrado de claves del lado del cliente

[BitMacro Signer](https://github.com/bitmacro/bitmacro-signer) es una herramienta de firma Nostr autoalojable que gestiona claves privadas usando el modelo de bunker [NIP-46](/es/topics/nip-46/). El firmador cifra las claves en el cliente antes del almacenamiento para que el lado del servidor nunca tenga texto en claro.

El descubrimiento de repos NIP-34 de esta semana trajo 26 nuevos anuncios de repositorio, de los cuales cuatro destacan.

### gnostr: una implementación de git construida directamente sobre Nostr

[gnostr](https://github.com/gnostr-org/gnostr) es una implementación de git construida directamente sobre Nostr, distinta de `git-remote-nostr` en que incluye sus propios comandos de árbol de trabajo como cliente de control de versiones nativo de Nostr desde cero.

### nostr-archive: una especificación de archivo con contenido direccionado en Nostr y Blossom

[nostr-archive](https://gitworkshop.dev/nostr-archive/nostr-archive) es una especificación borrador e implementación de referencia para archivos con contenido direccionado en Nostr y Blossom.

### flower-cache: un servidor de caché local de Blossom

[flower-cache](https://gitworkshop.dev/flower-cache/flower-cache) es un servidor de caché local de Blossom, útil para clientes que quieren un espejo local activo del conjunto de blobs de un servidor Blossom remoto.

### micro-vpn-ansible: playbooks de Ansible para despliegue de VPN sobre NIP-34

[micro-vpn-ansible](https://gitworkshop.dev/npub1mu9fsh42uh48trncevdpju8cyv3mxmj9qj3rdjqc46zc324c6hys9ctsnc/relay.ngit.dev/micro-vpn-ansible) es una pequeña colección de playbooks de Ansible para desplegar una micro VPN, alojada como repositorio NIP-34.

## Trabajo de protocolo

### Actualizaciones de NIP

- **Un mercado de hashrate sin intermediarios sobre Nostr** ([borrador de propuesta](https://njump.me/nevent1qqsqd2478wqugjh9ur9lenw9la0wd987h6jcc0tma4kkuat4xceymvszypxxmj0zcqtwqm34f48gzulrg99daaczllhtqun7xsldkh8neua2jhr32rf)): Borrador de NIP anónimo que argumenta que los actores actuales del mercado de hashrate son todos intermediarios con custodia que someten a los usuarios a KYC. La propuesta esboza un mercado peer-to-peer de hashrate sobre eventos Nostr.
- **Feeds curados: una alternativa más simple a los feeds DVM** ([borrador de propuesta](https://njump.me/nevent1qqsqj55kvu28uyq2jr6nfwx20mv7c0vkm0vxkgx0zzrnanfp4wwv8nczyzm7669svt0xkjsju50a22zurc0qa589z2xd4yatzx6p2z64a5e0cyxz3e3)): Un borrador argumenta que las Máquinas de Vending de Datos [NIP-90](/es/topics/nip-90/) fueron diseñadas como un mercado de cómputo de propósito general, y el modelo de solicitud/respuesta es más pesado de lo necesario cuando un cliente solo quiere una lista direccionable de IDs de eventos.
- **Colores de perfil: identidad visual determinista** ([borrador de propuesta](https://njump.me/nevent1qqsy3tj7mn3r7wczmc52aknf5ym43lj3rrhd3sfprzvc6qydsq62wrgzyzjk8j56zmt5fwv088l5y84hqq4gags3grvuznlu4zmyt54w34cccyxenp3)): Un nuevo borrador de NIP para derivar colores deterministas y legibles de un pubkey de Nostr para identidad visual consistente entre clientes.
- **NIPs de seguimiento Namecoin: anclar identidad, relays, TLS y reputación** ([clúster de borradores](https://njump.me/nevent1qqsydpjnaj2netmv0h5mlm2j6zpk8u50yvc9pqth3ly8pzuwy22720szypp3shk7edn43y5zfvdr0ftl8eq8l00zaknjqx3c9xuv7ja8ck60q7uupzs)): Un clúster separable de borradores de NIP que mueven partes del stack de Nostr existente a registros anclados en Namecoin.

## Inmersión profunda en NIP: NIP-34 (git stuff)

[NIP-34](/es/topics/nip-34/) define kinds de eventos para alojar repositorios git, parches, pull requests, issues y estado de fusión en relays Nostr. Es el estándar que convierte Nostr en una capa de coordinación para la colaboración de código.

Un repositorio se anuncia como un evento direccionable kind `30617` cuyo tag `d` es un identificador en kebab-case. Los parches usan kind `1617` y llevan la salida de `git format-patch` en el cuerpo del contenido. Los pull requests usan kind `1618`. Los issues usan kind `1621` con contenido markdown. Los eventos de estado mueven un hilo entre Abierto (`1630`), Aplicado/Fusionado o Resuelto (`1631`), Cerrado (`1632`) y Borrador (`1633`).

## Inmersión profunda en NIP: NIP-53 (Actividades en Vivo)

[NIP-53](/es/topics/nip-53/) define la superficie estándar de eventos para actividades en vivo en Nostr: transmisiones en vivo, espacios de reunión persistentes, eventos de conferencia programados, presencia de oyentes y el canal de chat en vivo que vincula los mensajes de chat a un registro de actividad en vivo específico.

Una transmisión en vivo se anuncia como un evento direccionable kind `30311`. NIP-53 separa el espacio persistente del evento programado que se celebra en su interior. Un kind `30312` Meeting Space define una sala, y un kind `30313` Conference Event representa una reunión programada o en curso en esa sala.

La superficie de actividades en vivo de Nostr es intencionalmente delgada: NIP-53 anuncia la actividad, mientras otros NIPs manejan preocupaciones adyacentes. Los zaps a transmisiones en vivo usan recibos de zap [NIP-57 (Zaps)](/es/topics/nip-57/), los objetivos de recaudación de fondos usan metas de zap [NIP-75 (Metas de Zap)](/es/topics/nip-75/), y las grabaciones de video pueden republicarse como eventos de video [NIP-71 (Eventos de Video)](/es/topics/nip-71/).

---

Eso es todo por esta semana. Si estás construyendo algo o tienes noticias que compartir, envíanos un DM en Nostr o encuéntranos en [nostrcompass.org](https://nostrcompass.org).
