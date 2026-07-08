---
title: 'Nostr Compass #25'
date: 2026-06-03
publishDate: 2026-06-03
draft: false
type: newsletters
translationOf: /en/newsletters/2026-06-03-newsletter.md
translationDate: 2026-07-01
---

Amber 6.2.0 estrena el cifrado NIP-44 v3 por delante de la especificación. Mostro aterriza la base para el escrow liquidado con Cashu a través de ocho PRs, envolviendo el Cashu Development Kit existente como un segundo backend de liquidación junto a Lightning. Los podcasts NIP-F4 se fusionan tras 27 meses de debate. fiatjaf abre una propuesta controvertida de desacoplamiento de claves NIP-17 que reabre el argumento arquitectónico bunker-contra-Marmot. Amethyst aterriza etiquetado de hashtags NIP-32, una pantalla de podcast dedicada y zaps en cadena a través de 52 PRs no publicados.

## Historias principales

### Amber 6.2.0: cifrado NIP-44 v3 publicado

[Amber v6.2.0](https://github.com/greenart7c3/Amber/releases/tag/v6.2.0), publicado el 1 de junio, añade [soporte de cifrado NIP-44 v3](https://github.com/greenart7c3/Amber/pull/448) con una pantalla dedicada de aprobación, vista previa de intent, vista previa de bunker, registro de historial y rechazo automático para solicitudes inválidas. El lanzamiento también registra [autoridades ContentProvider NIP-44 v3](https://github.com/greenart7c3/Amber/commit/8b93340) para que otras apps Android puedan solicitar cifrado v3 junto con la ruta v2 existente. NIP-44 en sí es la especificación de payload cifrado versionada usada por los DMs privados [NIP-17](/es/topics/nip-17/), el tráfico de bunker NIP-46 y otras primitivas Nostr; v3 en Amber es un opt-in junto a v2, señalizado por un método de firmador separado para que los clientes del lado receptor puedan negociar el algoritmo explícitamente. El PR correspondiente en el repo NIPs aún no ha aterrizado, por lo que Amber está desplegando v3 por delante del consenso del protocolo, con el formato de cable y la autoridad ContentProvider registrados para la integración de clientes downstream.

Las sesiones NIP-46 ahora auto-aceptan solicitudes ping en la conexión, eliminando el prompt en el primer viaje de ida y vuelta tras el emparejamiento. El método de firmador `sign_message` fue eliminado por completo tras haber sido obsoleto y sin uso.

Como Amber es el firmador Android dominante, cada cliente downstream que quiera v3 tiene que apuntar al formato de cable de Amber hasta que aterrice el PR de NIPs. Eso le da a Amber voz implícita sobre la especificación final de v3 hasta que el protocolo se ponga al día. El intercambio es real: v3 en producción permite a Amber recopilar retroalimentación de implementación para el eventual NIP, a costa de un punto de referencia temporal de implementación única que otros clientes ahora tienen que igualar.

### Mostro: integración de escrow Cashu mediante CDK

grunch aterrizó ocho PRs en MostroP2P esta semana integrando las primitivas multisig P2PK existentes de Cashu (NUT-10 y NUT-11) como un segundo backend de liquidación junto a Lightning en el intercambio de Bitcoin P2P coordinado por Nostr. Las primitivas criptográficas son de Cashu; el trabajo es andamiaje de integración y un nuevo trait de backend de escrow. [Mostro core v0.12.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.12.0), publicado el 30 de mayo, añade los [tipos de protocolo para escrow multisig 2-de-3](https://github.com/MostroP2P/mostro-core/pull/150), firmas P_M por prueba y permite eventos de escrow a través de la validación de respuesta. La arquitectura está documentada en [PR #756](https://github.com/MostroP2P/mostro/pull/756) y usa claves de intercambio por orden clarificadas en [PR #757](https://github.com/MostroP2P/mostro/pull/757).

La implementación se desplegó a través de seis PRs de seguimiento en un solo día. [F2 (PR #758)](https://github.com/MostroP2P/mostro/pull/758) añadió la configuración, el modo escrow y el arranque condicional. La siguiente rebanada, [F3 (PR #760)](https://github.com/MostroP2P/mostro/pull/760), definió un trait `EscrowBackend` con una implementación Lightning y un stub Cashu, permitiendo a Mostro cambiar de backend de liquidación sin cambiar la máquina de estado de la orden. [F4 (PR #759)](https://github.com/MostroP2P/mostro/pull/759) envolvió [CDK](https://github.com/cashubtc/cdk) (el Cashu Development Kit) para operaciones de mint y wallet. El trabajo de base de datos en [F5 (PR #761)](https://github.com/MostroP2P/mostro/pull/761) añadió bloqueos de escrow compare-and-swap y consultas active-locked. [F6 (PR #762)](https://github.com/MostroP2P/mostro/pull/762) construyó una mint contenerizada en un trabajo de CI dedicado para pruebas end-to-end de escrow. El flujo de Mostro ya usa DMs envueltos en gift wrap NIP-59 para la coordinación de órdenes sobre el relay, por lo que el escrow Cashu encaja como una segunda opción de liquidación junto a Lightning sin tocar el protocolo de cable.

## Lanzamientos

### ngit v2.5.0: fallback GRASP y fetches de git perezosos

[ngit v2.5.0](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.5.0) cambia el comportamiento por defecto de `git push pr/<branch>` y `ngit send` para producir un kind PR para nuevas propuestas cuando el repositorio tiene al menos un servidor GRASP registrado. Anteriormente esto solo se activaba para commits sobredimensionados de más de 60 KB o commits que contenían submódulos. Cuando un PR no puede empujarse a los servidores GRASP del repositorio, ngit ahora recae en el enrutado GRASP-06 a través de los servidores declarados. La bandera `ngit send --git-server` o `git push -o git-server=<url>` permite a los contribuyentes apuntar a una URL git personalizada o servidor GRASP explícitamente.

Los republicados de `ngit init` ahora preservan los tags desconocidos de los anuncios existentes, para que los tags añadidos por una versión futura de ngit o una herramienta de terceros sobrevivan al republicado. Una advertencia amarilla lista los tags arrastrados, y `--clean` los elimina bajo demanda. `ngit pr apply`, `ngit pr checkout` y `ngit pr list` consultan los servidores git perezosamente y comparten un único helper de fetch, por lo que checkout ya no obtiene incondicionalmente cuando el commit ya está local. `ngit pr checkout` también intenta URLs de clonado proporcionadas por el remitente desde el evento PR como respaldo cuando los servidores git declarados del repo no llevan el tip del PR, coincidiendo con el comportamiento existente en `ngit pr apply`. ngit es la implementación de referencia de [NIP-34](/es/topics/nip-34/) para colaboración git sobre Nostr, y v2.5.0 hace de GRASP la ruta de primera clase para los nuevos contribuyentes.

### Jumble v26.5.7: eliminación de EXIF y conteos de zap validados

[Jumble v26.5.7](https://github.com/CodyTseng/jumble/releases/tag/v26.5.7) añade dos cambios que afectan directamente a la privacidad del usuario y a la integridad de los datos. La ubicación EXIF y los identificadores de cámara ahora se eliminan de las subidas de imágenes antes de que salgan del cliente, cerrando una superficie de fuga de metadatos de larga data que afectaba a cada imagen publicada desde Jumble. Los conteos de zap ahora se computan solo desde recibos criptográficamente validados, corrigiendo conteos inflados de eventos zap malformados que habían permitido a los atacantes exagerar los totales de zap en las notas. El lanzamiento también añade verificación de identidad del remitente para DMs [NIP-17](/es/topics/nip-17/), cerrando una superficie de suplantación donde un remitente podía falsificar su `pubkey` en el sello.

### nostr-calendar v1.6.0: manejo de RSVP y participantes duplicados

[nostr-calendar v1.6.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.6.0) aterriza el flujo RSVP de Formstr ([PR #169](https://github.com/formstr-hq/nostr-calendar/pull/169)) y evita participantes duplicados en las invitaciones a eventos ([PR #168](https://github.com/formstr-hq/nostr-calendar/pull/168)). La opción `waitForAll` en la función publish ahora por defecto es false para que la UI no se bloquee en relays lentos ([PR #170](https://github.com/formstr-hq/nostr-calendar/pull/170)). [PR #157](https://github.com/formstr-hq/nostr-calendar/pull/157) estrenó los dos borradores de propuesta NIP de Formstr para programación de citas y reservas.

### Sprout 0.3.6: Sprout × mesh-llm y secciones de canal

[Sprout v0.3.6](https://github.com/block/sprout/releases/tag/v0.3.6) es el titular de una serie de seis lanzamientos de v0.3.1 a v0.3.6 esta semana. La integración in-process de Sprout × mesh-llm aterriza en [PR #798](https://github.com/block/sprout/pull/798), permitiendo a Sprout servir y consumir nodos mesh-llm mediante admisión de relay. Las secciones de canal definidas por el usuario se sincronizan entre dispositivos mediante Nostr en [PR #792](https://github.com/block/sprout/pull/792), y las secciones de canal llegan a móvil con sincronización de relay en [PR #800](https://github.com/block/sprout/pull/800). Las notificaciones conscientes de hilo con controles de follow y silencio mutables llegan en [PR #761](https://github.com/block/sprout/pull/761).

Los adjuntos de tipo de archivo arbitrario con tarjetas de descarga llegaron en [PR #810](https://github.com/block/sprout/pull/810), expandiendo Sprout más allá de los adjuntos solo de imagen. Móvil ganó una pestaña de feed social Pulse ([PR #772](https://github.com/block/sprout/pull/772)) y pulido de Pulse a través de las superficies de feed, composición y filtro ([PR #796](https://github.com/block/sprout/pull/796)).

### NostrBotKit v0.5.0: chat de grupo Marmot en un framework de bots Rust

[NostrBotKit v0.5.0](https://codeberg.org/Tuxor/NostrBotKit/src/branch/main/CHANGELOG.md), publicado el 24 de mayo en Codeberg, añade soporte de [Marmot](/es/topics/marmot/) (MLS-sobre-Nostr, [NIP-104](https://github.com/nostr-protocol/nips/pull/2014)) al framework de bots Rust auto-alojado. Cuando se configura `marmot: true`, el bot publica sus key packages MLS (kind 443, 30443, 10051), acepta invitaciones a grupos automáticamente y escucha mensajes en los grupos a los que se ha unido. Dos nuevos tipos de comando, `dm_marmot` y `dm_marmot_npub`, permiten a los bots enviar mensajes a grupos Marmot nombrados o chats Marmot 1:1 mediante trabajos cron o webhooks. Para evitar bucles de retroalimentación con otros bots, los bots de NostrBotKit solo responden a mensajes explícitamente dirigidos a ellos mediante `/command` o `@botname/command`. Los adjuntos cifrados usando MIP-04 se descifran automáticamente y se resuben mediante Blossom o NIP-96, y la base de datos de estado MLS se cifra con una clave derivada de la clave privada del bot. NostrBotKit es el primer framework Rust en publicar soporte de bots NIP-104, abriendo el despliegue de bots cifrados con Marmot a un perfil de operador diferente al de la ruta TypeScript existente.

### noscrypt v0.1.14: lanzamiento firmado de biblioteca de criptografía

[noscrypt v0.1.14](https://github.com/vnuge/noscrypt/releases/tag/v0.1.14) es un lanzamiento de seguridad de la biblioteca de criptografía en C usada por varios clientes Nostr para primitivas secp256k1, NIP-04 y NIP-44. El lanzamiento se distribuye con [descargas firmadas con PGP](https://www.vaughnnugent.com/resources/software/modules/noscrypt) verificables contra la clave pública del mantenedor. Los clientes downstream que empaqueten noscrypt deben validar la firma antes de integrar.

### Chama v1.3.0: nuevo escrow P2P nativo de Nostr con Fedimint

[Chama v1.3.0](https://github.com/jesuspirate/chama/releases/tag/v1.3.0), publicado el 1 de junio, es el titular de una serie de cuatro lanzamientos para un nuevo cliente de escrow P2P nativo de Nostr que usa ecash Fedimint y compartición de secretos Shamir 2-de-3 para la liquidación. El proyecto se distribuye en [getchama.app](https://getchama.app) y funciona sin servidor. v1.3.0 introduce "heal that sticks" (re-difusión exitosa y curación de intercambios que sobreviven a los reinicios de sesión) y emparejamiento de pay-rail, donde las Chamas orientadas a EEUU muestran primero los rails de pago de EEUU. El trabajo base multi-unidad para storefronts aterrizó a través de [v1.2.11](https://github.com/jesuspirate/chama/releases/tag/v1.2.11) (esquema multi-unidad) y [v1.2.12](https://github.com/jesuspirate/chama/releases/tag/v1.2.12) (contador de stock de storefront + endurecimiento de recuperación del puente nativo Fedimint). Chama se une a Mostro y Shopstr en la categoría de marketplaces Nostr, distinguida por su arquitectura sin servidor y su liquidación de escrow basada en Fedimint.

## Cambios sin publicar

### Amethyst: etiquetado de hashtags NIP-32, pantalla de podcast, pistas de música

Amethyst fusionó 52 PRs y 411 commits esta semana sin cortar una etiqueta de lanzamiento. La adición funcional más grande es [PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111), que implementa etiquetado de hashtags [NIP-32](/es/topics/nip-32/) y un feed de hashtags basado en etiquetas usando eventos kind 1985 con tags de namespace `L` y etiqueta `l`. Esto reemplaza el frágil mecanismo de coincidencia de texto `#tag` con un modelo de descubrimiento basado en etiquetadores donde los usuarios pueden seguir a npubs de etiquetadores específicos de la misma forma que siguen a creadores de contenido. [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) añade una pantalla dedicada de podcast con lista de episodios y reproductor en línea, aterrizando a los pocos días de la fusión de la especificación de podcast [NIP-F4](/es/topics/nip-f4/). [PR #3071](https://github.com/vitorpamplona/amethyst/pull/3071) añade un feed Software Apps con filtrado por lista de follow, y [PR #3067](https://github.com/vitorpamplona/amethyst/pull/3067) añade soporte para pistas de música y playlists mediante conjuntos [NIP-51](/es/topics/nip-51/).

Los firmadores efímeros para subidas de posts anónimos aterrizan en [PR #3123](https://github.com/vitorpamplona/amethyst/pull/3123), permitiendo a los usuarios publicar de forma anónima sin exponer su clave de identidad a los servicios de subida. Un watchdog de auto-curación de Tor con pruebas de integración contra Arti v2.3.0 llega en [PR #3053](https://github.com/vitorpamplona/amethyst/pull/3053), fortaleciendo el enrutado Tor de Amethyst durante caídas de red transitorias. Los zaps en cadena y un filtro NIP-05 para usuarios que regresan desde Gemini aterrizan en [PR #3052](https://github.com/vitorpamplona/amethyst/pull/3052), ampliando la superficie de zap más allá de Lightning a pagos de Bitcoin en cadena.

### Shopstr: validación de URLs de vista previa OpenGraph

[PR #504](https://github.com/shopstr-eng/shopstr/pull/504) valida las URLs de vista previa OpenGraph antes de renderizarlas en los listados del marketplace, cerrando una potencial superficie XSS donde vendedores maliciosos podían incrustar contenido con scripts mediante metadatos OG diseñados. Las tiendas alojadas en Shopstr muestran vistas previas OG para enlaces externos, y las URLs no validadas permiten a un atacante inyectar contenido arbitrario en la UI de la tienda.

## Actualizaciones de NIP y trabajo de especificación de protocolo

### NIP-F4 (Podcasts) se fusiona tras dos años

[PR #1093](https://github.com/nostr-protocol/nips/pull/1093) se fusionó el 28 de mayo, dos años y tres meses después de que fiatjaf abriera el borrador original. NIP-F4 define los episodios de podcast como eventos kind 54 con tags `imeta` para metadatos del archivo de audio (URL, tipo mime, código de idioma ISO, URLs de respaldo, bandera de servicio NIP-96, bitrate, duración), un tag `title`, tags opcionales `image` y `description`, y tags `t` para etiquetas de tema. La especificación mantiene deliberadamente RSS como la fuente de verdad: los episodios pueden llevar un tag `i` que referencie el GUID del podcast RSS, permitiendo a los clientes Nostr enlazar a feeds de podcast existentes sin duplicar el alojamiento de audio. El largo debate en el hilo del PR (con el co-autor de podcast-namespace Dave Jones, Alex Gleason y Mike Terenzio) se resolvió en un modelo de coexistencia donde Nostr proporciona la capa social sobre RSS mientras RSS mantiene la capa de distribución. La pantalla de podcast del [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) de Amethyst aterriza a los pocos días de la fusión de la especificación, y el trabajo del selector de GIF de Jumble también incluye andamiaje temprano para adjuntos de podcast.

### Desacoplamiento de claves NIP-17 (PR #2361)

fiatjaf abrió [PR #2361](https://github.com/nostr-protocol/nips/pull/2361) el 1 de junio, proponiendo que NIP-17 separe la clave de identidad de la clave de cifrado. Los destinatarios anuncian su clave de cifrado en un nuevo evento kind 10044, y los remitentes usan esa clave anunciada (cuando está presente) para el sello interno del gift-wrap, recayendo en la clave de identidad del destinatario solo cuando el anuncio está ausente. El PR también añade un tag `n` al sello llevando la pubkey de cifrado del remitente, para que los receptores puedan derivar la clave de conversación correcta sin descifrado por prueba y error contra cada clave retirada. La motivación declarada es la UX de bunker: bajo el diseño actual, un usuario de bunker debe hacer un viaje de ida y vuelta a cada DM recibido a través del firmador para descifrar, ya que la clave de cifrado es la clave de identidad guardada por el firmador. Desacoplar permite al cliente mantener la clave de cifrado localmente mientras mantiene la clave de identidad en el bunker para firmas.

La propuesta atrajo la revisión más polémica de la semana. Cody Tseng (Jumble) la apoya como la ruta más fácil para la interoperabilidad de DMs entre clientes. Vitor Pamplona (Amethyst) objeta por dos motivos: añade un nuevo secreto de descifrado de larga duración fuera del bunker, y los clientes que no lo distribuyan fallarán silenciosamente al descifrar mensajes de clientes que sí lo hacen, sin ruta de degradación porque la ruptura está en la capa del sello. Pamplona argumenta que el problema ya está resuelto correctamente por los key packages de [Marmot](/es/topics/marmot/) y la rotación de épocas, y que retrofit de separación de claves en la especificación base NIP-17 crea el tipo de fallo de interoperabilidad que Marmot tardó dos años en diseñar. La respuesta de fiatjaf tiene tres partes: el desacoplamiento es opcional por destinatario, la corrección del tag n aborda la preocupación del descifrado por prueba y error, y la alternativa es mantener la UX de bunker rota mientras Telegram se come el caso de uso de la mensajería. El hilo permanece abierto sin decisión de fusión y es la discusión NIP más observada del trimestre.

### Flujo de pago NIP-Silent Payments (PR #2362)

[silentius-satoshi abrió PR #2362](https://github.com/nostr-protocol/nips/pull/2362) el 1 de junio como complemento del más amplio [borrador de NIP Nostr Silent Payments (PR #2355)](https://github.com/nostr-protocol/nips/pull/2355). El NIP de flujo de pago define kind 8352 para notificaciones de recepción de silent payment (entregadas mediante gift wrap [NIP-59](/es/topics/nip-59/) para que el enlace del recibo no sea públicamente observable) y kind 10353 para una caché UTXO cifrada que se sincroniza entre dispositivos para la misma wallet Silent Payments. El par juntos permiten a un pagador señalizar un pago a una dirección Silent Payments usando primitivas nativas de Nostr sin exponer el enlace on-chain en la capa de relay abierta.

### NIP-PIP Perfect IP Packets (PR #2364)

[RandyMcMillan abrió PR #2364](https://github.com/nostr-protocol/nips/pull/2364) el 1 de junio como borrador. Introduce un transporte de árbol de paquetes con tres nuevos kinds direccionables: 39078 lleva el manifiesto, 39079 lleva slices individuales y 39080 lleva solicitudes de reparación. La especificación define un formato de cable donde los archivos grandes se dividen en slices direccionables, con manifiestos describiendo el árbol de slices y solicitudes de reparación permitiendo a los receptores pedir slices faltantes. Se aplica estado de borrador temprano, y la propuesta aún no ha atraído revisión de mantenedores.

### Espacios en vivo de audio/vídeo NIP-29 (PR #2238)

[PR #2238](https://github.com/nostr-protocol/nips/pull/2238) se fusionó el 28 de mayo, extendiendo los grupos basados en relay [NIP-29](/es/topics/nip-29/) con soporte de espacios en vivo de audio y vídeo. Los grupos ahora pueden referenciar una sesión activa de espacio en vivo, permitiendo a los eventos de actividad en vivo estilo [NIP-53](/es/topics/nip-53/) anclarse en un contexto de grupo NIP-29.

### Múltiples pistas de audio en vídeo NIP-71 (PR #2255)

[PR #2255](https://github.com/nostr-protocol/nips/pull/2255) se fusionó el 28 de mayo, añadiendo tags `imeta` de pista de audio a los eventos de vídeo NIP-71. El nuevo formato lleva URL, hash, tipo mime, tag de idioma (con ISO-639-1 más bandera de versión original), URLs de respaldo, señal de servicio NIP-96, bitrate y duración. Esto habilita streaming solo de audio (video podcasts), cambio de resolución con audio estable, múltiples pistas de idioma y almacenamiento reducido cuando los servidores no incrustan audio directamente en archivos de vídeo. Los clientes deben comprobar la disponibilidad de pistas de audio antes de asumir comportamiento de pista única.

### Gift wrap efímero NIP-59 (PR #2245)

[PR #2245](https://github.com/nostr-protocol/nips/pull/2245) se fusionó el 28 de mayo, añadiendo kind 21059 como contraparte efímera del gift wrap kind 1059 existente. La semántica coincide con el envoltorio estándar NIP-59 pero sigue las reglas de eventos efímeros por NIP-01 (los relays los descartan tras la difusión y no los persisten). Esto permite a las apps elegir persistencia según los requisitos: los indicadores de escritura y pings de presencia se benefician de lo efímero, mientras que el historial de DMs necesita persistencia.

### Kind específico de aplicación NIP-78 (PR #2292)

[PR #2292](https://github.com/nostr-protocol/nips/pull/2292) se fusionó el 28 de mayo, reclasificando los datos específicos de aplicación NIP-78 como un kind direccionable normal, descartando el rango separado anterior. Esto simplifica la semántica de reemplazabilidad y alinea NIP-78 con el modelo de evento direccionable usado por otros NIPs de estado de aplicación.

### Aclaraciones NIP-85 (PR #2304)

[PR #2304](https://github.com/nostr-protocol/nips/pull/2304) se fusionó el 28 de mayo con pequeñas mejoras al lenguaje alrededor de múltiples claves y relays por proveedor de servicio en [NIP-85](/es/topics/nip-85/) Trusted Assertions, clarificando la ruta de rotación de clave de operador para los servicios de aserción de relay.

### Gestión de conexión de relay NIP-01 de una línea (PR #2307)

[PR #2307](https://github.com/nostr-protocol/nips/pull/2307) se fusionó el 28 de mayo, añadiendo una sola frase a NIP-01 sobre cómo los clientes deben manejar los tiempos de vida de las conexiones de relay. La corrección aborda una brecha de larga duración donde los clientes diferían en si mantener las conexiones WebSocket abiertas tras la obtención, llevando a pérdida silenciosa de mensajes en relays que descartan conexiones inactivas.

### Restricción de chat kind 9 NIP-C7 (PR #2310)

[PR #2310](https://github.com/nostr-protocol/nips/pull/2310) se fusionó el 28 de mayo, restringiendo las vistas de chat NIP-C7 solo a mensajes kind 9. Esto separa el chat efímero de las publicaciones de timeline kind 1 en clientes que implementan superficies de chat estilo NIP-C7.

### Simplificación NIP-55 (PR #2363)

[PR #2363](https://github.com/nostr-protocol/nips/pull/2363) de greenart7c3, abierto el 1 de junio, simplifica la especificación de aplicación de firmador Android. Vitor Pamplona firmó como "Looks good" y fiatjaf preguntó si está listo para fusionar. El cambio prepara el camino para el registro de autoridad ContentProvider NIP-44 v3 que Amber publicó esta semana.

### NIP-44 v3 (implementación de Amber por delante de la especificación)

Amber publicó NIP-44 v3 en v6.2.0 con ocho commits implementando la actualización de cifrado y el registro de autoridad ContentProvider, pero el PR de especificación en el repo NIPs aún no ha aterrizado. NIP-44 en sí define un formato de payload cifrado versionado usado dentro de eventos firmados; el v2 existente (en producción desde 2024) usa ECDH secp256k1, HKDF, padding, ChaCha20, HMAC-SHA256 y base64. El formato de cable v3 añade un nuevo byte de versión (0x03) por delante del nonce, permitiendo a los clientes receptores negociar el algoritmo explícitamente. La implementación de Amber incluye rechazo automático para solicitudes v3 inválidas, una pantalla dedicada de aprobación distinta de las aprobaciones v2 y registro de texto plano por dirección para el historial. Hasta que el PR de NIPs se fusione, v3 se mantiene como una extensión específica de Amber. Trátalo como una señal prospectiva, no como una señalización estable a nivel de protocolo.

## NIP deep dive: NIP-32 (Etiquetado)

[NIP-32](/es/topics/nip-32/) define una forma estructurada para que cualquier actor Nostr etiquete eventos, pubkeys, relays, URLs o temas usando eventos direccionables kind 1985 con un vocabulario de etiquetas con namespace. La especificación introduce dos nuevos tags: `L` denota un namespace de etiqueta, y `l` denota una etiqueta dentro de ese namespace. Los tags target de etiqueta (`e`, `p`, `a`, `r` o `t`) especifican qué se está etiquetando. El requisito de namespace evita que múltiples sistemas de etiquetas colisionen: una etiqueta `spam` en `nip28.moderation` lleva semántica diferente a una etiqueta `spam` en `relay-report`.

La elección de diseño que hace que NIP-32 sea útil más allá de la moderación es que las etiquetas son aserciones, no verdad a nivel de protocolo. Un evento kind 1985 dice solo que una pubkey particular etiquetó a un objetivo particular en un namespace particular. El modelo de confianza se delega al cliente: cada cliente elige a qué etiquetadores honrar, qué namespaces leer y qué comodidad UI dar a cada etiqueta. La misma primitiva lleva advertencias de contenido, asignación de licencia, tags de idioma ISO-639-1 en notas kind 1, tags geográficos ISO-3166-2, clasificación de contenido, sugerencias distribuidas de moderación y puntuaciones de reputación.

El [PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111) de Amethyst esta semana es el mayor despliegue hasta ahora. Añade etiquetado de hashtags mediante NIP-32 y un feed de hashtags basado en etiquetas, permitiendo a los usuarios navegar por etiquetas asignadas por etiquetadores de confianza. El mecanismo anterior de coincidencia de texto `#tag` que originalmente impulsó el descubrimiento de hashtags en Nostr permanece como respaldo para notas no etiquetadas. El modelo de hashtag como etiqueta significa que la misma nota puede ser descubrible bajo múltiples etiquetas asignadas por diferentes etiquetadores, y los usuarios pueden silenciar o impulsar etiquetadores específicos sin afectar a las notas subyacentes.

El auto-etiquetado también está soportado. Un autor puede adjuntar tags `L` y `l` directamente a sus propias notas kind 1 para declarar idioma, ubicación y tema. Una nota etiquetada `["L", "ISO-639-1"], ["l", "en", "ISO-639-1"]` se auto-identifica como inglés y puede ser filtrada por clientes conscientes del idioma sin infraestructura de etiquetado de terceros.

Ejemplo de evento de etiqueta NIP-32 etiquetando una nota kind 1 como inglés y asignándole una etiqueta de moderación:

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748908800,
  "kind": 1985,
  "tags": [
    ["L", "ISO-639-1"],
    ["l", "en", "ISO-639-1"],
    ["L", "nip28.moderation"],
    ["l", "approve", "nip28.moderation"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3", "wss://relay.example.com"]
  ],
  "content": "Labeled as English-language content approved for NIP-28 chat moderation",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

El despliegue de Amethyst combinado con el reciente trabajo de Trusted Relay Assertions sugiere que NIP-32 se está convirtiendo en el sustrato estándar para cualquier patrón de "aserción impulsada por el usuario sobre un objetivo" en Nostr. La siguiente prueba es si los propios etiquetadores desarrollan jerarquías de confianza: si los usuarios seguirán a npubs de etiquetadores específicos de la misma forma que siguen a creadores de contenido.

## NIP deep dive: NIP-F4 (Podcasts)

[NIP-F4](https://github.com/nostr-protocol/nips/blob/master/F4.md) se fusionó esta semana, dos años y tres meses después de que fiatjaf abriera el borrador original (PR #1093). El prefijo F es simple numeración hexadecimal: NIP-F0 a NIP-FF usan el mismo espacio hex de 1 byte que NIP-0A a NIP-0D, con el rango hex superior sirviendo como desbordamiento ahora que el rango decimal 01-99 se está llenando. NIP-F4 define cómo los podcasts publican episodios y metadatos como eventos Nostr mientras mantienen RSS como una capa complementaria para el propio archivo de audio.

La elección arquitectónica central es que cada podcast es su propio par de claves Nostr. La especificación abre con esto directamente: "each podcast is its own Nostr keypair". Esto permite a los podcasts combinar su presencia de podcasting con una presencia normal de microblogging kind 0 / kind 1, y permite a un podcast cambiar de propiedad con el tiempo mediante traspaso de claves o firma compartida estilo MuSig2. Cuatro kinds de evento llevan la capa de publicación:

- **`kind:10154`**: metadatos de podcast reemplazables. Lleva tags `title`, `image`, `description`, `website` opcionales, y tags `p` opcionales marcando autores con un `role` de `host`, `cohost` o `editor`.
- **`kind:10164`**: contra-reclamación del autor. El ejemplo en la especificación usa kind `10064` (una errata abierta para corrección), pero el encabezado y el texto circundante lo identifican como `kind:10164`. Los usuarios listan las pubkeys de podcast que autorizan, para que los clientes puedan verificar los tags `p` en `kind:10154` contra una reclamación equivalente del supuesto autor. Sin esto, un podcast podría etiquetar falsamente a cualquiera como host.
- **`kind:54`**: eventos de episodio autorizados directamente por la pubkey del podcast. Los tags incluyen `title`, `image` opcional, `description` y uno o más tags `audio`. Cada tag `audio` es `["audio", "<audio-url>", "<optional_media_type>"]`. La especificación anota "otros campos importantes a especificar aquí más tarde tras un mayor descubrimiento", y la forma fusionada es deliberadamente mínima.
- **`kind:10054`**: una lista de podcasts favoritos estilo [NIP-51](/es/topics/nip-51/), permitiendo a los usuarios marcar qué podcasts siguen.

El debate del hilo alrededor de la fusión involucró al co-autor de Podcasting 2.0 [Dave Jones](https://github.com/daveajones), [Alex Gleason](https://github.com/alexgleason), [Mike Terenzio](https://github.com/mterenzio), [Pablo F7z](https://github.com/pablof7z) y [staab](https://github.com/staab). Jones argumentó fuertemente contra cualquier intento de reemplazar RSS: "It's been tried many times and always fails", citando JSONfeed, XMPP, AMP, la API de Twitter y la migración fallida de Spotify. Terenzio reencuadró la propuesta como una capa social sobre RSS, manteniendo RSS mismo como la capa de distribución. fiatjaf accedió a dar un paso atrás y dejar madurar la propuesta: "I agree with everything you said but I still think we can pull it off, let's stop here for a while". Dos años después, la especificación fusionada aterriza más cerca de la coexistencia que del reemplazo.

Tres preguntas de diseño permanecen explícitas en la especificación fusionada:

- La errata `kind:10164` (el ejemplo muestra `10064`) necesita reconciliación antes de que los clientes puedan interoperar de forma segura.
- El descubrimiento a nivel de episodio sin enlace GUID RSS queda abierto. La especificación fusionada no tiene tag `i`, ni formato `podcast:item:guid`, ni mecanismo de puente RSS. Los clientes que quieran puentear un catálogo RSS existente en eventos kind 54 deben definir la convención de puente ellos mismos.
- El stub de "otros campos importantes" en la definición de `kind:54` deja bitrate, duración, idioma, punteros de transcripción, capítulos y metadatos por segmento como territorio abierto para propuestas de seguimiento.

El [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) de Amethyst aterriza una pantalla dedicada de podcast con lista de episodios y reproductor en línea a los pocos días de la fusión, la primera implementación importante de cliente. Jumble publicó andamiaje temprano de adjuntos de podcast junto con su selector de GIF. Wavlake sigue siendo la plataforma de podcasts nativa de Nostr más grande y tendrá que decidir si alinear sus eventos de pista de música kind 31337 existentes con el modelo de episodio kind 54 de NIP-F4.

Ejemplo de evento de episodio kind 54 NIP-F4, coincidiendo con el conjunto mínimo de tags de la especificación fusionada:

```json
{
  "id": "55807e7d5cd90d0303d7dce7397f996fdbaed8697903f326c7cf8ad999b9de3d",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748995200,
  "kind": 54,
  "tags": [
    ["title", "Episode 42: Why RSS Won"],
    ["image", "https://podcast.example.com/ep42-cover.jpg"],
    ["description", "Dave Jones and fiatjaf on protocol coexistence and the social layer."],
    ["audio", "https://podcast.example.com/audio/ep42.mp3", "audio/mpeg"]
  ],
  "content": "In this episode we discuss the two-year journey of NIP-F4 from draft to merge, and why coexistence with RSS turned out to be the right architectural choice.",
  "sig": "abc123def456789012345678901234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef01234567"
}
```

PR #1093 estuvo abierto durante 27 meses, muy por encima de la duración abierta mediana de los PRs de NIPs fusionados. La siguiente prueba para NIP-F4 es si la errata del kind 10164 se reconcilia, si emergen convenciones de descubrimiento de episodios y de puente RSS por parte de los implementadores, y si los hosts principales de podcast publican bajo pares de claves por podcast como recomienda la especificación.
