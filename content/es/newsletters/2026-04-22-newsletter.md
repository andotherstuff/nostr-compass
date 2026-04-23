---
title: 'Nostr Compass #19'
date: 2026-04-22
translationOf: /en/newsletters/2026-04-22-newsletter.md
translationDate: 2026-04-22
draft: false
type: newsletters
---

Bienvenido de nuevo a Nostr Compass, tu guía semanal de Nostr.

**Esta semana:** [Amethyst](https://github.com/vitorpamplona/amethyst) avanzó fuerte en cumplimiento de [Marmot](/es/topics/marmot/), comunidades [NIP-72](/es/topics/nip-72/), objetivos de zap [NIP-75](/es/topics/nip-75/) y salas de audio sobre MoQ. [TollGate](https://github.com/OpenTollGate/tollgate) estabilizó acceso a internet de pago por uso sobre Nostr y [Cashu](/es/topics/cashu/) con [v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0). [nostream](https://github.com/Cameri/nostream) cerró una semana de trabajo de relay en torno a [NIP-45](/es/topics/nip-45/), [NIP-62](/es/topics/nip-62/), compresión, endurecimiento de consultas y paridad completa con [NIP-11](/es/topics/nip-11/). También destacaron el paquete de repositorios de Forgesworn, la sincronización de cartera Lightning de ShockWallet y los análisis de [NIP-72](/es/topics/nip-72/) y [NIP-57](/es/topics/nip-57/).

## Noticias principales

### Amethyst lanza cumplimiento MIP de Marmot, comunidades NIP-72, objetivos de zap y salas de audio con MoQ

[Amethyst](https://github.com/vitorpamplona/amethyst) fusionó 57 PRs centradas en interoperabilidad de [Marmot](/es/topics/marmot/), gestión de comunidades [NIP-72](/es/topics/nip-72/), objetivos de zap [NIP-75](/es/topics/nip-75/) en pantallas [NIP-53](/es/topics/nip-53/) y una nueva superficie de audio en tiempo real sobre Media over QUIC. El trabajo incluye alineación con formatos wire de MIP-01 y MIP-05, soporte para MIP-00 KeyPackage Relay List, correcciones de framing y descifrado MLS, una CLI `amy` para operaciones de grupos, creación y moderación de comunidades, leaderboard de top zappers y una nueva pantalla de Public Chats para salas públicas de audio.

### TollGate v0.1.0 estabiliza internet de pago por uso sobre Nostr y Cashu

[TollGate](https://github.com/OpenTollGate/tollgate) publicó [v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0), fijando una primera referencia estable para vender conectividad por minutos o megabytes a cambio de tokens ecash de [Cashu](/es/topics/cashu/). La arquitectura separa una capa de protocolo basada en TIP-01 y TIP-02, una capa de interfaz con HTTP-01 a HTTP-03 y NOSTR-01, y una capa de medio descrita por WIFI-01 para captive portals y clientes pagadores.

### nostream fusiona 53 PRs para NIP-45, NIP-62, compresión y endurecimiento de consultas

[nostream](https://github.com/Cameri/nostream) añadió soporte de `COUNT` para [NIP-45](/es/topics/nip-45/), anunció right-to-vanish de [NIP-62](/es/topics/nip-62/), amplió el esquema de filtros para tags en mayúscula y añadió compresión gzip y xz para import/export. Además, mejoró el rendimiento del traductor de filtros a SQL, corrigió un fallo en matching de pubkeys en allowlists y denylists, añadió desempate determinista en `upsertMany`, limitó la confianza en `X-Forwarded-For` y alcanzó paridad completa con [NIP-11](/es/topics/nip-11/).

## Lanzamientos de esta semana

### Primal Android lanza pestaña Explore, verificación NIP-05 y reproductor de audio

[Primal Android](https://github.com/PrimalHQ/primal-android-app) añadió una nueva pestaña Explore, editor de feeds basado en la DSL de búsqueda avanzada de Primal, verificación [NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md) y un reproductor de audio embebido. También conectó el escáner QR de cartera con emparejamiento [NIP-46](/es/topics/nip-46/).

### strfry añade métricas Prometheus para la ruta de escritura y corrige el sobre AUTH de NIP-42

[strfry](https://github.com/hoytech/strfry) añadió métricas Prometheus para escrituras, logging por conexión y compresión, volvió configurable el límite de tags por filtro y corrigió sus respuestas de AUTH para ajustarse a [NIP-42](/es/topics/nip-42/), usando el sobre `OK` en lugar de `NOTICE`.

### Shopstr endurece la seguridad del storefront en 13 PRs

[Shopstr](https://github.com/shopstr-eng/shopstr) fusionó una serie de correcciones de seguridad que cierran JavaScript almacenado en enlaces de storefront, XSS reflejado en políticas HTML, una API sin autenticación para borrar eventos cacheados, lectura no autenticada de mensajes, fallos SSRF y errores funcionales en cola de publish y descuentos de carrito.

### Nostria v3.1.26 a v3.1.28 añaden reproducción de música en segundo plano en Android

[Nostria](https://github.com/nostria-app/nostria) añadió reproducción de música en segundo plano en Android con controles en la barra de notificaciones y pantalla de bloqueo, y los releases posteriores endurecieron esa nueva superficie del servicio multimedia.

### Wisp v0.18.0-beta añade Normie Mode, feed For You y configuración de grupos NIP-29

[Wisp](https://github.com/barrydeen/wisp) orientó esta versión a usuarios menos nativos de Bitcoin con Normie Mode, onboarding renovado y feed For You. En el lado de protocolo añadió configuración de grupos [NIP-29](/es/topics/nip-29/) para flags, invites, roles y AUTH, además de broadcasting a inbox relays [NIP-65](/es/topics/nip-65/) de pubkeys mencionadas.

### NoorNote v0.8.4 añade Scheduled Posts y zaps en live streams

[NoorNote](https://github.com/77elements/noornote) añadió publicaciones programadas a través de un relay operado por el proyecto, zaps de un toque desde tarjetas de live stream vía [NIP-53](/es/topics/nip-53/) y correcciones de duplicación en timelines largas de Android.

### topaz v0.0.2 lanza un relay Nostr para Android

[topaz](https://github.com/fiatjaf/topaz) apareció como un relay Nostr ejecutable en teléfonos Android. El alcance por ahora es acotado, pero la idea es usar el teléfono como relay personal siempre disponible.

### StableKraft v1.0.0 lanza la primera versión estable de su PWA de música y podcasts

[StableKraft](https://github.com/ChadFarrow/stablekraft-app) llegó a [v1.0.0](https://github.com/ChadFarrow/stablekraft-app/releases/tag/v1.0.0) como una PWA Next.js para descubrir, organizar y reproducir música obtenida desde feeds de podcasts, usando Nostr para auth y funciones sociales y Lightning para pagos V4V. La semana también mejoró la ingesta de feeds y acortó ventanas de reparseo nocturno.

### NipLock lanza un gestor de contraseñas basado en NIP-17

[NipLock](https://gitworkshop.dev/npub1z5jf78uhd68znuwwwu926th55rzd0wy8nd9clkr03cx22mwme0jqazk56h/relay.ngit.dev/passwd) almacena credenciales como mensajes directos [NIP-17](/es/topics/nip-17/) enviados de la clave del usuario a sí misma, de modo que se sincronicen entre dispositivos autenticados con la misma clave. Soporta firma con `nsec`, extensiones de navegador y [Amber](https://github.com/greenart7c3/Amber) vía [NIP-46](/es/topics/nip-46/).

### flotilla-budabit pule su superficie de repositorios NIP-34

El fork [flotilla-budabit](https://github.com/Pleb5/flotilla-budabit) siguió mejorando controles de discusión de repositorios, pestañas sticky, carga de anuncios desde relays GRASP y sincronización del estado de patches aplicados por maintainers en su flujo git-over-Nostr.

### rx-nostr 3.7.2 a 3.7.4 añaden verificador por defecto y argumentos opcionales

[rx-nostr](https://github.com/penpenpng/rx-nostr) añadió un verificador Schnorr por defecto, corrigió un uso defectuoso de `@noble/curves` en su paquete crypto y permitió crear instancias con `createRxNostr()` sin configuración obligatoria.

### Keep Android v1.0.0 lanza builds reproducibles y cero trackers

[Keep](https://github.com/privkeyio/keep-android) llegó a [v1.0.0](https://github.com/privkeyio/keep-android/releases/tag/v1.0.0) tras añadir receta de build reproducible, sustituir Google ML Kit por ZXing para eliminar dependencias de Google Play Services y publicar un escaneo de Exodus Privacy sin trackers. También añadió un manifiesto `zapstore.yaml` para distribuir el APK en Zapstore.

### Flotilla 1.7.3 y 1.7.4 añaden envoltura kind-9 para salas NIP-29 más ricas

[Flotilla](https://gitea.coracle.social/coracle/flotilla) empezó a envolver contenido no orientado a chat dentro de kind `9` para preservar el contexto de la sala [NIP-29](/es/topics/nip-29/). Los releases también añadieron encuestas, login [NIP-46](/es/topics/nip-46/) mediante Aegis, support de share para invites, room mentions, borradores y vídeo en llamadas.

### WoT Relay v0.2.1 migra el eventstore a LMDB

[WoT Relay](https://github.com/bitvora/wot-relay) migró su eventstore a LMDB, reajustó la carga inicial del grafo de confianza y actualizó dependencias criptográficas y metadatos [NIP-11](/es/topics/nip-11/) para el release.

### Suite Formstr: revisión de seguridad en Pollerama, i18n en Forms y soporte RRULE en Calendar

La suite de Formstr fusionó 26 PRs entre Pollerama, Forms y Nostr Calendar. Pollerama endureció gestión de claves y parsing de perfiles; Forms añadió soporte para audio/vídeo, i18n e importador de Google Forms; y Nostr Calendar lanzó v1.3.0 y v1.4.0 con múltiples RRULE, fechas flotantes en UTC según RFC 5545, eventos compartidos y preferencias de notificación, todo sobre [NIP-52](/es/topics/nip-52/).

### También lanzaron: notedeck, nostr.blue, cliprelay, Captain's Log

Otros proyectos publicaron releases iterativos sin una sola gran novedad: [notedeck](https://github.com/damus-io/notedeck) mejoró renderizado de columnas y relay pools, [nostr.blue](https://github.com/patrickulrich/nostr.blue) actualizó Dioxus y destrabó Android, [cliprelay](https://github.com/tajava2006/cliprelay) ajustó sincronización de portapapeles y [Captain's Log](https://github.com/nodetec/comet) añadió detección de vida de relays de sync.

## En desarrollo

### whitenoise-rs se refactoriza hacia vistas de cuenta con alcance de sesión

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) continuó su refactor por fases desde singletons globales hacia `AccountSession` por cuenta, moviendo handles de relay, drafts, settings, operaciones de mensajes, lectura y escritura de grupos, membresía, push notifications, key packages y dispatch de eventos a superficies propias de cada sesión.

### La app White Noise añade UI de bloqueo/desbloqueo, salida de grupo y avisos offline

[White Noise](https://github.com/marmot-protocol/whitenoise) añadió controles para bloquear y desbloquear usuarios, salir y eliminar grupos desde la app y mostrar avisos offline cuando el daemon no puede alcanzar sus relays. También afinó la eliminación de key packages legacy durante migraciones.

### MDK añade soporte de invites entre versiones mixtas y convergencia de SelfUpdate

[MDK](https://github.com/marmot-protocol/mdk) mejoró compatibilidad entre clientes Marmot con distintas versiones calculando `RequiredCapabilities` como LCD de las capacidades de invitados y alineando el formato wire de SelfUpdate. También reforzó validación de depletion admin, almacenamiento en memoria y acceso a propuestas requeridas por grupo.

### nostter añade cifrado NIP-44 a listas de personas, bookmarks y mutes

[nostter](https://github.com/SnowCait/nostter) siguió migrando de [NIP-04](/es/topics/nip-04/) a [NIP-44](/es/topics/nip-44/) al cifrar mute lists, bookmarks y people lists, y eliminó una ruta legacy de migración kind-30000 que ya no hacía falta.

### zap.cooking lanza puntuación Nourish y un hilo de comentarios reutilizable

[zap.cooking](https://github.com/zapcooking/frontend) añadió un módulo Nourish para puntuar recetas por ejes nutricionales y refactorizó su módulo de comentarios hacia un `CommentThread` reutilizable, junto con mejoras de escalado, subida de medios y pestañas de replies.

### ridestr extrae un coordinador compartido de pasajeros

[ridestr](https://github.com/variablefate/ridestr) refactorizó pantallas Compose y extrajo la lógica de protocolo de rider y driver hacia un coordinador compartido `:common`, además de añadir un receptor de driver ping kind `3189`.

### Blossom propone cabecera BUD-01 Sunset para expiración de blobs

[Blossom](https://github.com/hzrd149/blossom) abrió una propuesta para añadir una cabecera `Sunset` a BUD-01, de modo que un servidor pueda anunciar cuándo dejará de servir un blob y los clientes puedan planificar retención limitada sin descubrirla solo cuando llegue un 404.

## Proyectos nuevos

### Forgesworn publica un toolkit criptográfico de 29 repositorios para Nostr

[Forgesworn](https://github.com/forgesworn) lanzó un conjunto amplio de repositorios TypeScript alrededor de firma, identidad, attestations, web of trust y APIs pagadas. Destacan `nsec-tree` para subidentidades deterministas, `Heartwood` como signer [NIP-46](/es/topics/nip-46/) sobre Raspberry Pi, `Signet` para verificación de identidad, `nostr-attestations` para credenciales y `toll-booth` / `toll-booth-dvm` para monetizar APIs sobre Lightning y [NIP-90](/es/topics/nip-90/).

### ShockWallet lanza sincronización de cartera Lightning nativa de Nostr y conexiones multi-node

[ShockWallet](https://github.com/shocknet/wallet2) usa Nostr como transporte para conectarse a nodos Lightning autocustodiados mediante `nprofile`. El proyecto sigue empujando sincronización de estado multi-dispositivo basada en eventos específicos de aplicación y una superficie coherente entre web, Android e iOS.

### Los issues de Nostrability migran a git sobre Nostr tras la censura de GitHub

[Nostrability](https://gitworkshop.dev/elsat@habla.news/nostrability/issues) movió su workflow de issues a infraestructura git-over-Nostr después de que GitHub eliminara la organización sin respuesta posterior. La idea es mantener los informes de interoperabilidad dentro de infraestructura nativa de Nostr.

### nowhere codifica sitios web completos en fragments URL y enruta pedidos por Nostr

[nowhere](https://github.com/5t34k/nowhere) serializa un sitio entero dentro del fragmento `#` de la URL, lo comprime y lo firma, de modo que el host nunca vea el contenido porque los navegadores no envían fragments a servidores. Para tipos de sitio que necesitan comunicación viva, como store o forum, el tráfico pasa por relays Nostr con cifrado [NIP-44](/es/topics/nip-44/).

### Nuevas superficies pequeñas: relayk.it y Brainstorm Search

[relayk.it](https://relayk.it) apareció como cliente de descubrimiento de relays construido con Shakespeare y ejecutado íntegramente en el navegador, mientras [Brainstorm Search](https://brainstorm.world) ofrece una UI de búsqueda Nostr de página única orientada a descubrir contenido en la red.

## Trabajo de protocolo y especificación

### Actualizaciones de NIP

La semana trajo nuevas propuestas en el repositorio de NIPs alrededor de [NIP-67](/es/topics/nip-67/) para completitud de `EOSE`, NIP-5D para applets web, subgrupos y permisos explícitos en [NIP-29](/es/topics/nip-29/), un campo `access_control` en [NIP-11](/es/topics/nip-11/), attestations de reputación de agentes para mercados de [NIP-90](/es/topics/nip-90/) y la continuación del trabajo sobre datos privados de localización y cambios de `marmot-ts`.

## NIP Deep Dive: NIP-72 (comunidades moderadas)

[NIP-72](https://github.com/nostr-protocol/nips/blob/master/72.md) define comunidades temáticas moderadas en las que cualquiera puede enviar contenido, pero solo las publicaciones aprobadas por un moderador aparecen en la vista comunitaria. La comunidad se define con un evento kind `34550`, los envíos la referencian mediante una etiqueta `a` y los moderadores publican eventos kind `4549` para aprobarlos. El modelo es transparente, auditable y bifurcable, a diferencia de [NIP-29](/es/topics/nip-29/), donde el relay controla tanto la membresía como la moderación.

## NIP Deep Dive: NIP-57 (zaps)

[NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md) define cómo adjuntar pagos Lightning a identidades y contenido Nostr mediante solicitudes kind `9734` y recibos kind `9735`. El punto central sigue siendo la validación: los clientes deben comprobar firma, monto de invoice, description hash y `preimage` antes de tratar un recibo como un zap real. Sobre esa base descansan tanto zaps privados y anónimos como sistemas de objetivos de zap de [NIP-75](/es/topics/nip-75/).
