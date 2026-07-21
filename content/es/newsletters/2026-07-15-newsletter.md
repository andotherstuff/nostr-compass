---
title: "Nostr Compass #31"
date: 2026-07-15
publishDate: 2026-07-15
draft: false
type: newsletters
translationOf: /en/newsletters/2026-07-15-newsletter.md
translationDate: 2026-07-15
description: "Vector v0.4.0 retira Marmot para chats grupales a favor del protocolo abierto Concord y lanza Concord v2 días después, Amethyst fusiona su propia implementación limpia de Concord, Sonar se separa de Bitchat con una alpha multiplataforma y una especificación de paquetes de stickers, Divine Mobile 1.0.16 incorpora cifrado en reposo y procedencia ProofMode, Bitchat 1.7.0 añade voz push-to-talk en vivo, y MDK v0.9.4 acota el inicio de sesión con firmante externo."
---

Bienvenidos de vuelta a Nostr Compass, su guía semanal sobre Nostr.

**Esta semana:** [Vector v0.4.0](#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later) retira [Marmot](/es/topics/marmot/) como transporte predeterminado para Chats Grupales a favor de [Concord](/es/topics/concord-protocol/), un protocolo de comunidad abierto con licencia MIT también utilizado por Armada de Soapbox, y lanza Concord v2 cuatro días después con un selector de comandos con barra para bots, un temporizador de autodestrucción y badges NIP-58. [Amethyst fusiona su propia implementación limpia de Concord, compatible a nivel de protocolo](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities), la misma semana. [Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec) se separa de Bitchat con una alpha multiplataforma y es la fuente de especificación citada para la propuesta de kinds de paquetes de stickers de esta semana. [Divine Mobile 1.0.16](#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance) incorpora un editor de video más profundo, cifrado en reposo y procedencia ProofMode que sobrevive a las descargas de clips con marca de agua. [Bitchat v1.7.0](#bitchat-v170-adds-live-push-to-talk-voice-for-dms-and-the-public-mesh) añade voz push-to-talk en vivo para DMs y push-to-talk firmado en la malla pública. [MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence) acota el inicio de sesión con firmante externo y añade persistencia de borradores, continuando su pase de endurecimiento la misma semana en que Vector se aleja de la especificación para chat grupal.

Los lanzamientos etiquetados traen [n_cord v1.1](#n_cord-v11-adds-nsec-bunker-support) con soporte para NSEC Bunker, [cdk v0.17.3](#cdk-v0173-adds-nip-47-wallet-service-support-across-cdk-cdk-nwc-and-cdk-ffi) con soporte de servicio de billetera NIP-47 en cdk, cdk-nwc y cdk-ffi, [Coop Mobile v0.2.4](#coop-mobile-v024-improves-nostr-connect-and-adds-ncryptsec1-import) con mejoras en Nostr Connect e importación ncryptsec1, [Nmail v0.14.0](#nmail-v0140-ships-on-macos-with-scheduled-send-and-push-notifications) llegando a macOS con envío programado, [Nostrord v2.2.0](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages) con un interruptor maestro de DM, [Nostr WoT 0.3.86](#nostr-wot-0386-hardens-key-backups-and-signing-prompts) endureciendo respaldos de claves al formato NIP-49, [Keep Android v1.1.8](#keep-android-v118-adds-first-run-frost-onboarding) con incorporación FROST de primer uso, [Noscall v0.6.0](#noscall-v060-adds-a-cashu-wallet-and-relay-based-push-notifications) con una billetera Cashu y notificaciones push basadas en relay, [Kubo](#kubo-ships-tablet-mode-and-group-chat-photos) con modo tableta y fotos en chats grupales, y [Nostr Codex Phone v0.2.9](#nostr-codex-phone-v029-adds-gitdiffread-file-helper-requests) con solicitudes auxiliares de git, diff y lectura de archivos.

En el lado no publicado, [Amethyst](#amethyst-lets-accounts-nickname-contacts-with-encrypted-nip-85-cards) permite a las cuentas asignar apodos a contactos con tarjetas NIP-85 cifradas en 54 PRs fusionados, [Zap Cooking](#zap-cooking-ships-my-kitchen-phase-3-and-fixes-an-ndk-pool-quorum-bug) lanza la Fase 3 de My Kitchen y corrige un error de quórum del pool NDK, [Kehto](#kehto-streams-outbox-reads-before-relay-discovery) transmite lecturas de outbox antes de que termine el descubrimiento de relay, [Wired y TAO](#wired-and-tao-add-nip-57-creator-revenue-sharing) añaden reparto de ingresos de creador con NIP-57, [Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout) reconstruye su bandeja de pedidos del comerciante alrededor de pago efímero como invitado, [Buzz](#buzz-hardens-channel-creator-provisioning-around-kind-39002) endurece el aprovisionamiento del creador de canal en 240 PRs fusionados, y [Nostr Docs](#nostr-docs-adopts-a-nip-49-signer-with-multi-account-and-qr-pairing) adopta un firmante NIP-49 con múltiples cuentas y emparejamiento QR. Recién rastreados esta semana: [OpenDiscord v1.0.1](#opendiscord-v101-launches-as-a-discord-style-client-on-nostr), [Auditable Voting v0.1.140](#auditable-voting-v01140-aligns-organiser-voter-and-audit-proxy-roles), y la selección Discovery [Cambium v0.3.2](#cambium-v032-pairs-with-heartwood-as-a-keyless-nip-55-signer), un firmante NIP-55 sin claves que redirige a un compañero de hardware Heartwood.

El repositorio de NIPs no fusiona nada en la última semana y abre seis propuestas: [kind:10011 conjuntos de seguimiento favoritos](#open-kind10011-favorite-follow-sets), una [unidad cifrada privada que extiende NIP-4E](#open-private-encrypted-drive-extends-nip-4e), [NIP-DA compartición privada de datos con permisos](#open-nip-da-permissioned-private-data-sharing), [kinds de paquetes de stickers 10031 y 30031](#open-sticker-pack-kinds-10031-and-30031), [fijación de mensajes NIP-29](#open-nip-29-message-pinning-with-kind9010-and-kind39005), y una [reestructuración del descubrimiento de relay NIP-66](#open-nip-66-relay-discovery-restructure). El Deep Dive cubre [NIP-99 y la extensión de comercio Gamma Markets](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension).

---

## Historias principales

### Vector v0.4.0 mueve los Chats Grupales de Marmot a Concord, y Amethyst lanza su propio cliente Concord días después

[Vector](https://github.com/VectorPrivacy/Vector) es un mensajero Nostr construido alrededor de un cliente de binario único enfocado en privacidad para DMs y chats grupales. [Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) reescribe el motor de mensajería de la aplicación en una biblioteca compartida `vector-core` y, en el mismo lanzamiento, retira [Marmot](/es/topics/marmot/) (MLS-sobre-Nostr) como transporte predeterminado para Chats Grupales a favor de [Concord](/es/topics/concord-protocol/), un protocolo de comunidad cifrado de extremo a extremo; el historial existente de grupos Marmot no se transfiere, y las notas del lanzamiento indican a los usuarios respaldar cualquier dato de grupo Marmot antes de actualizar. Las propias notas de lanzamiento de Vector describen Concord como "nuestro protocolo de mensajería personalizado", pero las [especificaciones CORD-01 a CORD-07](https://github.com/concord-protocol/concord) subyacentes se publican por separado, con licencia MIT, y ya están implementadas fuera de Vector: el cliente estilo Discord de Soapbox, [Armada](https://gitlab.com/soapbox-pub/armada), construye su función de Comunidades sobre la misma especificación Concord, y un día después, [Amethyst fusionó su propia implementación limpia y compatible a nivel de protocolo](https://github.com/vitorpamplona/amethyst/pull/3566), cubierta en detalle a continuación. El mismo lanzamiento de Vector añade enrutamiento opcional por Tor para todo el tráfico, inicio de sesión con firmante remoto [NIP-46](/es/topics/nip-46/) por QR o URI bunker pegada, múltiples cuentas con un conmutador dentro de la aplicación, y paquetes de emojis personalizados compartidos entre clientes. La eliminación de mensajes remueve un mensaje para ambos lados en DMs y chats grupales, y Vector deliberadamente mantiene la clave de firma efímera en lugar de seguir el flujo estándar de eliminación [NIP-17](/es/topics/nip-17/), una desviación motivada por privacidad que el proyecto señala explícitamente en las notas del lanzamiento. Cuatro días después, [v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1) lanza **Concord v2**, descrito como una versión con mejoras importantes de privacidad y estabilidad para Comunidades manteniendo las existentes funcionando, junto con un selector de comandos con barra estilo Discord para bots con parámetros tipados, un temporizador de autodestrucción por chat, y un sistema de badges NIP-58 para cazadores de errores. El alejamiento de Marmot para chat grupal ocurre la misma semana en que [MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence) a continuación continúa invirtiendo en la especificación.

### Amethyst lanza una implementación limpia de Concord para comunidades cifradas de extremo a extremo

[Amethyst](https://github.com/vitorpamplona/amethyst) es un cliente Nostr rico en funciones para Android y multiplataforma. [PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566) añade una implementación completa de [Concord](/es/topics/concord-protocol/) (CORD-01 a CORD-07) cubriendo comunidades sin servidor y cifradas de extremo a extremo: planos de control, chat e invitados envueltos con gift-wrap, sobre relay ordinarios, con cumplimiento de roles, expulsiones y baneos enraizados en el propietario que cada cliente verifica localmente en lugar de confiar en un servidor, y re-cifrado para cortar acceso a miembros eliminados. El código de protocolo y criptografía reside en `quartz/`, los modelos de estado y vista en `commons/`, y las pantallas y navegación en `amethyst/` para Android, con verbos CLI delgados bajo `cli/`; todavía no hay interfaz de escritorio, ya que la lógica compartida reside en `quartz`/`commons` para que Desktop la adopte después. La implementación es de sala limpia: construida a partir de las especificaciones CORD públicas y constantes de protocolo observadas, bajo la propia licencia MIT de Amethyst, distinta del código base AGPL-3.0 de Armada. Los valores de vectores de prueba propios de Armada fueron portados a las pruebas unitarias de Quartz para confirmar que ambos clientes realmente interoperan a nivel de protocolo, dando a Concord tres implementaciones independientes en días: Vector lanzando primero, Armada como cliente de referencia de Soapbox, y ahora la construcción desde la especificación de Amethyst.

### Sonar se separa de Bitchat con una alpha multiplataforma y una especificación de paquetes de stickers

[Sonar](https://sonarprivacy.xyz/) es un mensajero y billetera con malla Bluetooth más Nostr desarrollado a partir de Bitchat, con DMs grupales Marmot interoperables con White Noise. El código vive en [hedwig-corp/bitchat-to-sonar](https://github.com/hedwig-corp/bitchat-to-sonar). [v0.1-alpha.7](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.7) añade ventaneo acotado de transcripción estilo Signal para que el rendimiento de apertura y desplazamiento se mantenga local-first, sincroniza el estado de descubrimiento cercano entre pares, y corrige subidas de medios Blossom que fallaban por manejo de content-type y estado HTTP; la precedente [alpha.6](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.6) drenó eventos Marmot en vivo para una actualización más rápida del chat y cerró brechas de paridad de funciones entre Android e iOS en llamadas, mensajería, billetera y push. Sonar también es la fuente de especificación citada para [PR #2410](#open-sticker-pack-kinds-10031-and-30031), que registra kinds de eventos de paquetes de stickers bajo la propia especificación "Sonar Stickers" del proyecto, dando a este lanzamiento un enlace directo al trabajo de protocolo de esta semana.

### Divine Mobile 1.0.16 incorpora un editor de video más profundo, cifrado en reposo y procedencia ProofMode

[Divine](https://github.com/divinevideo/divine-mobile) es un cliente de videos cortos construido sobre Nostr con curación de feed por Web-of-Trust. [v1.0.16](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.16), el primer lanzamiento etiquetado desde el #30, añade transiciones de clips, reproducción inversa, un grabador de voz en off y marcadores de ritmo en la línea de tiempo al editor de video, junto con un control de ajuste de feed que permite al usuario deslizar para ajustar recomendaciones directamente en lugar de dejarlas a señales opacas de interacción. El lanzamiento también activa el cifrado en reposo para datos locales, añade subidas en segundo plano que sobreviven a la suspensión de la aplicación, y lleva los datos de procedencia [ProofMode](/es/topics/proofmode/) al descargar un clip con marca de agua para que la atestación de creación humana no se pierda en tránsito. Divine también incluye nuevas protecciones para cuentas de menores de 16 años y expande la localización a 17 idiomas y 284 cadenas traducidas.

### Bitchat v1.7.0 añade voz push-to-talk en vivo para DMs y la malla pública

[Bitchat](https://github.com/permissionlesstech/bitchat) es una aplicación de chat con malla Bluetooth con una pasarela opcional hacia relay Nostr. [v1.7.0](https://github.com/permissionlesstech/bitchat/releases/tag/v1.7.0), lanzado la noche que se publicó el #30, añade voz push-to-talk en vivo en [PR #1403](https://github.com/permissionlesstech/bitchat/pull/1403) que transmite audio mientras el remitente mantiene presionado el botón y retrocede a una nota de voz si el flujo se interrumpe, más push-to-talk firmado en la malla pública en [PR #1406](https://github.com/permissionlesstech/bitchat/pull/1406) para que las ráfagas de voz en vivo en el canal compartido de la malla lleven autenticación del remitente. El lanzamiento también repara la rotación de peer-ID reenlazando el vínculo en un re-anuncio verificado, reconociendo al mismo par bajo su nuevo ID ([PR #1401](https://github.com/permissionlesstech/bitchat/pull/1401)), y los mensajes directos a un par actualmente inalcanzable ahora se ponen en cola con entrega store-and-forward en lugar de fallar directamente ([PR #1415](https://github.com/permissionlesstech/bitchat/pull/1415)). Esto continúa directamente desde la cobertura del #30 del trabajo de [NIP-13](/es/topics/nip-13/) proof-of-work y pasarela mesh-a-Nostr de v1.6.0.

### MDK v0.9.4 acota el inicio de sesión con firmante externo y añade persistencia de borradores

[MDK](https://github.com/marmot-protocol/mdk) es el SDK de referencia para el protocolo [Marmot](/es/topics/marmot/), la capa de mensajería MLS-sobre-Nostr que el #30 cubrió marcando su especificación como adoptada. [v0.9.4](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.4) acota los pasos de directorio consultivo que un cliente recorre durante el inicio de sesión con firmante externo en [PR #793](https://github.com/marmot-protocol/mdk/pull/793), previniendo un bucle de reintento sin límite cuando un firmante remoto es lento o no responde. El mismo lanzamiento añade persistencia de borradores de mensajes y enlaces de perfil a sitio web en [PR #812](https://github.com/marmot-protocol/mdk/pull/812), continuando el pase de endurecimiento incremental que MDK ha ejecutado desde el corte de v0.9.0.

---

## Lanzamientos etiquetados

### n_cord v1.1 añade soporte para NSEC Bunker

[n_cord](https://github.com/0n4t3/n_cord) es un cliente de chat con tecnología Nostr inspirado en Discord e IRC. [v1.1](https://github.com/0n4t3/n_cord/releases/tag/v1.1) añade soporte para NSEC Bunker [NIP-46](/es/topics/nip-46/) junto con una corrección de error en el manejo de respuestas.

### cdk v0.17.3 añade soporte de servicio de billetera NIP-47 en cdk, cdk-nwc y cdk-ffi

[cdk](https://github.com/cashubtc/cdk) es un kit de desarrollo de Cashu; este lanzamiento es solo Bitcoin/Lightning en la mayoría de aspectos, pero [v0.17.3](https://github.com/cashubtc/cdk/releases/tag/v0.17.3) añade soporte de servicio [NIP-47](/es/topics/nip-47/) (Nostr Wallet Connect) con un crate de servicio NWC dedicado, integración de billetera, enlaces FFI para `cdk-ffi`, y cobertura de pruebas de extremo a extremo, dando a las billeteras Cashu construidas sobre cdk una superficie estándar de Nostr Wallet Connect.

### Coop Mobile v0.2.4 mejora Nostr Connect y añade importación ncryptsec1

[Coop Mobile](https://git.reya.su/reya/coop-mobile) es un cliente de mensajería privada [NIP-17](/es/topics/nip-17/) para plataformas móviles. [v0.2.4](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.4) mejora su flujo de [NIP-46](/es/topics/nip-46/) Nostr Connect, corrige un indicador de carga que se quedaba permanentemente en algunas conexiones, y añade soporte de importación para el formato de clave cifrada [NIP-49](/es/topics/nip-49/) `ncryptsec1` junto con una pantalla de importación de identidad rediseñada.

### Nmail v0.14.0 llega a macOS con envío programado y notificaciones push

[Nmail](https://github.com/nogringo/nostr-mail-client) es un cliente de correo construido sobre Nostr; [v0.14.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.14.0) lleva la aplicación a macOS, añade envío programado con un buzón de Programados dedicado para mensajes en cola, y añade notificaciones push. El lanzamiento también cambia la resolución de identificadores Nostr de la libreta de direcciones al resolutor [NIP-05](/es/topics/nip-05/) de NDK en lugar de una implementación propia.

### Nostrord v2.2.0 añade un interruptor maestro de DM y mensajes directos más ricos

[Nostrord](https://github.com/nostrord/nostrord) es un cliente de chat grupal basado en relay [NIP-29](/es/topics/nip-29/) para Android, iOS, web y escritorio. [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) añade un interruptor maestro para deshabilitar todas las funciones de mensajes directos a la vez ([PR #175](https://github.com/nostrord/nostrord/pull/175)) y lanza "mensajes directos más ricos" ([PR #186](https://github.com/nostrord/nostrord/pull/186)), continuando desde la cobertura del #30 sobre el lanzamiento que consolidó el pool de relay y detectó WebSockets zombi.

### Nostr WoT 0.3.86 endurece los respaldos de claves y las solicitudes de firma

[Nostr WoT](https://github.com/nostr-wot/nostr-wot-extension) es una extensión de navegador que vincula una identidad Nostr con una billetera Lightning. [v0.3.86](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.3.86) mueve los respaldos de claves cifradas al formato estándar [NIP-49](/es/topics/nip-49/), hace que las solicitudes de firma muestren el evento completo y todas las etiquetas en lugar de un resumen, verifica los datos del relay contra su firma, y deja de exponer la identidad activa al cambiar de cuenta. La extensión también elimina el permiso de navegador `scripting` no utilizado.

### Keep Android v1.1.8 añade incorporación FROST de primer uso

[Keep](https://github.com/privkeyio/keep-android) es un firmante Android construido sobre fragmentos de clave FROST de umbral. [v1.1.8](https://github.com/privkeyio/keep-android/releases/tag/v1.1.8) añade un flujo de primer uso que explica los fragmentos de clave FROST y permite al nuevo usuario elegir una política de firma de Manual, Básica o Automática antes de que llegue la primera solicitud de firma, la primera incorporación del lado Android para el modelo de firma de umbral del crate keep-mobile subyacente.

### Noscall v0.6.0 añade una billetera Cashu y notificaciones push basadas en relay

[Noscall](https://github.com/sanah9/noscall) es una aplicación de llamadas de audio y video seguras construida sobre Nostr. [v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release) añade una billetera Cashu con alcance de cuenta con saldos multi-mint, envío y recepción de ecash, y pago y recepción Lightning con persistencia de cotizaciones. El lanzamiento también migra las notificaciones push de Android de Firebase Cloud Messaging a una ruta de entrega basada en relay Nostr a través de UnifiedPush, y mejora la fiabilidad de VoIP de iOS y push APNs durante reintentos de inicio de sesión.

### Kubo lanza modo tableta y fotos en chats grupales

[Kubo](https://github.com/JeroenOnNostr/kubo) es una plataforma de video Nostr segura para niños con curación de feed por Web-of-Trust. [kubo-v2026.07.05](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v2026.07.05) añade un diseño de cuadrícula para tableta opcional para el feed infantil y soporte para adjuntar fotos a mensajes de chat grupal, además de correcciones para el botón de registro que se ocultaba detrás del teclado en pantalla en Android.

### Nostr Codex Phone v0.2.9 añade solicitudes auxiliares de git/diff/lectura de archivos

[Nostr Codex Phone](https://github.com/tidley/nostr-codex-phone) es una superficie de control móvil para un trabajador de asistente de codificación local que se comunica a través de DMs cifrados de Nostr. [v0.2.9](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.9) añade acciones de herramientas OpenCode móviles incluyendo solicitudes auxiliares de git, diff, lectura de archivos, estado e historial, mejoras de fijación y búsqueda de sesión, y un control de detención de tareas, junto con un envoltorio de subida cifrada a [Blossom](/es/topics/blossom/) que se lanzó en la v0.2.8 anterior.

### GitWorkshop v3.0.3 corrige refs recién anunciadas en el explorador de repositorios, y lanza su primera compilación para Android

[GitWorkshop](https://github.com/DanConwayDev/gitworkshop) es una interfaz web git-sobre-Nostr para explorar y revisar repositorios NIP-34. [v3.0.3](https://github.com/DanConwayDev/gitworkshop/releases/tag/v3.0.3) corrige las vistas de ramas, etiquetas, commits y exploración de código que fallaban al resolver una ref que un repositorio anuncia después de que el explorador ya la ha cargado, junto con limpieza de tiempos de flujo de CI, confirmado directamente contra la etiqueta y el historial de commits. La misma semana, GitWorkshop publicó su primera compilación nativa para Android en [Zapstore](https://zapstore.dev), comenzando en v3.0.0 y alcanzando v3.0.3 en horas; la interfaz web sigue siendo la interfaz principal, y el paquete Android trae la misma exploración de repositorios NIP-34 a un teléfono por primera vez.

### Bitcoin-Safe llega a Flathub, destacando su plugin Nostr Sync & Chat

[Bitcoin-Safe](https://bitcoin-safe.org) es una billetera Bitcoin de autocustodia construida alrededor de flujos de trabajo con firmantes de hardware. El proyecto [publicó un paquete en Flathub](https://flathub.org/apps/org.bitcoin_safe.BitcoinSafe) esta semana, su primera lista en una tienda de aplicaciones Linux convencional. El lanzamiento en Flathub pone el plugin Sync & Chat de Bitcoin-Safe frente a una audiencia más amplia: el plugin usa mensajes directos [NIP-17](/es/topics/nip-17/), a través de la propia biblioteca [bitcoin-nostr-chat](https://github.com/andreasgriffin/bitcoin-nostr-chat) del proyecto, para sincronizar etiquetas de billetera entre los dispositivos de un usuario y para enviar y recibir PSBTs para co-firma multisig remota entre participantes de confianza. La capa Nostr en sí se lanzó antes, en [2.0.0](https://github.com/andreasgriffin/bitcoin-safe/releases/tag/2.0.0) (2026-06-29), que rediseñó la firma de transacciones alrededor de un tipo de conexión "Compartir via Chat & Sync" junto con QR, USB y Bluetooth. La noticia de esta semana es el empaquetado en Flathub que pone esa función existente frente a una audiencia Linux convencional por primera vez.

---

## Cambios no publicados

### Amethyst permite a las cuentas asignar apodos a contactos con tarjetas NIP-85 cifradas

Más allá de la [implementación de Concord](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities) cubierta anteriormente, Amethyst fusionó 54 otros PRs en la última semana. El principal entre ellos es [PR #3548](https://github.com/vitorpamplona/amethyst/pull/3548), que permite a una cuenta asignar un apodo a cualquier otro usuario publicando su propia tarjeta de contacto kind 30382 [NIP-85](/es/topics/nip-85/) sobre ellos. El apodo, una nota privada, y cualquier mapeo personalizado de código corto de emoji [NIP-30](/es/topics/nip-30/) viven dentro del contenido cifrado con [NIP-44](/es/topics/nip-44/) de la tarjeta, de modo que solo la cuenta firmante puede leerlos, y las tarjetas se sincronizan a través del conjunto extendido de relay outbox de la cuenta al iniciar sesión e incrementalmente después. Los feeds, chats y menciones renderizan el apodo en lugar del nombre de visualización público, con una tarjeta de apodo accesible al tocar en la página de perfil encima del nombre real del usuario.

### Zap Cooking lanza la Fase 3 de My Kitchen y corrige un error de quórum del pool NDK

[Zap Cooking](https://github.com/zapcooking/frontend) es una aplicación de compartición de recetas y comunidad culinaria construida sobre Nostr. Fusionó 43 PRs continuando su función de planificación de comidas "My Kitchen", incorporando generación de listas de compras, un selector de recetas y una cuadrícula de planificación semanal en esta fase. El mismo conjunto de cambios corrige un error de quórum de preparación del pool de conexiones de [NDK](https://github.com/nostr-dev-kit/ndk) (Nostr Development Kit) que podía dejar lecturas de relay esperando más allá del punto en que un quórum de relay ya había respondido.

### Kehto transmite lecturas de outbox antes del descubrimiento de relay

[Kehto](https://github.com/kehto/web) es un runtime web temprano para applets Nostr [NIP-5D](/es/topics/nip-5d/), o "napplets". Fusionó 26 PRs. [PR #193](https://github.com/kehto/web/pull/193) corrige lecturas de outbox que anteriormente esperaban a que la carga de listas de relay [NIP-65](/es/topics/nip-65/) terminara antes de abrir cualquier relay, de modo que una carga de lista de relay que nunca se resolvía podía bloquear tanto la entrega de eventos como los tiempos de espera de consulta; la corrección abre hints de relay validados inmediatamente y transmite resultados mientras se descubren los relay de escritura. Un segundo cambio ([PR #196](https://github.com/kehto/web/pull/196)) alinea la página de auditoría de identidad del proyecto con NAP-SHELL, el contrato de ciclo de vida de la plataforma Napplet, parte del mismo trabajo de alineación de protocolo visible en otros lugares del lanzamiento `napplet/web` de esta semana.

### Wired y TAO añaden reparto de ingresos de creador con NIP-57

[Wired](https://github.com/smolgrrr/Wired) y [TAO](https://github.com/smolgrrr/TAO) son clientes gemelos de redes sociales enfocados en libertad de expresión construidos sobre Nostr, compartiendo la misma lista de PRs; ambos fusionaron [PR #121](https://github.com/smolgrrr/Wired/pull/121), que implementa reparto de ingresos de creador [NIP-57](/es/topics/nip-57/) para que los zaps enviados a una publicación puedan dividirse automáticamente entre contribuyentes más allá del autor original. Esto continúa la cobertura del #30 del par elevando su señal de proof-of-work a 21 bits como trabajo no publicado.

### Conduit Mono reconstruye la bandeja de pedidos del comerciante alrededor de pago efímero como invitado

[Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) es un protocolo de mercado adyacente a las listas de clasificados [NIP-99](/es/topics/nip-99/). [PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174) añade pago como invitado usando una clave efímera generada por el navegador: el invitado envía un pedido cifrado y un reporte de pago al comerciante usando esa clave de un solo uso, y el comerciante hace seguimiento fuera de banda por teléfono o correo, de modo que el comprador nunca necesita una identidad de bandeja de entrada durable. [PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175) reconstruye la bandeja de pedidos del comerciante alrededor de un modelo único de estado de pedido compartido, separando roles de comprador y comerciante y requiriendo un código de seguimiento y transportista antes de que un pedido físico o mixto pueda pasar a enviado. El flujo de pago del proyecto se basa en mensajes privados [NIP-17](/es/topics/nip-17/), cifrado [NIP-44](/es/topics/nip-44/) y gift wrap [NIP-59](/es/topics/nip-59/). El [NIP Deep Dive](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension) de esta semana cubre las convenciones de [Gamma Markets](/es/topics/gamma-markets/) hacia las que este mismo problema de estado de pedido apunta.

### Buzz endurece el aprovisionamiento del creador de canal alrededor de kind 39002

[Buzz](https://github.com/block/buzz) es una plataforma de comunicación de mente colectiva que conecta agentes de IA y humanos sobre Nostr. Fusionó 240 PRs en la última semana, continuando su arco de endurecimiento de la capa de relay desde la cobertura del #30 sobre métricas de turno de agente kind 44200. La corrección de esta semana ([PR #1830](https://github.com/block/buzz/pull/1830)) trata al creador de un canal como miembro antes de que la lógica de aprovisionamiento de canal kind 39002 se ejecute, cerrando una condición de carrera donde el propio canal del creador podía rechazarlo durante la configuración.

### Nostr Docs adopta un firmante NIP-49 con múltiples cuentas y emparejamiento QR

[Nostr Docs](https://github.com/formstr-hq/nostr-docs) es una aplicación de documentos colaborativos nativa de Nostr. Fusionó 5 PRs, el notable ([PR #50](https://github.com/formstr-hq/nostr-docs/pull/50)) adoptando el paquete `@formstr/signer` para autenticación completa [NIP-49](/es/topics/nip-49/) con cambio de múltiples cuentas y emparejamiento QR, reemplazando una ruta de firma propia anterior.

### También publicado

Correcciones menores de interoperabilidad de firmantes y fiabilidad aterrizaron en varios proyectos rastreados en la última semana sin suficiente superficie nueva para sus propios párrafos: [ngit-cli](https://github.com/DanConwayDev/ngit-cli), un cliente de línea de comandos para una alternativa a GitHub basada en Nostr, lanza [v2.6.3](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.6.3) haciendo que `ngit init` dé orientación de configuración accionable en lugar de pedir repetidamente un nsec; [Manent](https://github.com/dtonon/manent), una aplicación privada de notas y archivos cifrados construida sobre Nostr, lanza [v1.4.1](https://github.com/dtonon/manent/releases/tag/v1.4.1) corrigiendo el inicio de sesión con firmante Android roto cuando Amber devuelve un pubkey hexadecimal y mejorando el desplazamiento del inicio de sesión bunker; [NoorNote](https://github.com/77elements/noornote), un cliente Nostr delgado y libre de servicios Google, lanza [v1.2.8](https://github.com/77elements/noornote/releases/tag/v1.2.8) corrigiendo notificaciones perdidas de grupos Nostrord y añadiendo un interruptor de alerta de publicación propia; [Bray](https://github.com/forgesworn/bray), un servidor MCP Nostr consciente de confianza para agentes de IA y humanos, lanza [v1.34.0](https://github.com/forgesworn/bray/releases/tag/v1.34.0) enviando metadatos de nombre de cliente en conexiones bunker [NIP-46](/es/topics/nip-46/); [Lumilumi](https://github.com/TsukemonoGit/lumilumi), un cliente web Nostr, cachea listas de relay [NIP-65](/es/topics/nip-65/) en almacenamiento local para respaldo sin conexión; [Earthly](https://github.com/moogmodular/earthly), una aplicación de ciudad y comunidad local basada en Nostr, añade búsqueda geográfica [NIP-50](/es/topics/nip-50/); y [lnbits](https://github.com/lnbits/lnbits), un sistema de billetera y cuentas Lightning gratuito y de código abierto, lanza [PR #3925](https://github.com/lnbits/lnbits/pull/3925) haciendo que `send_nostr_dm` publique de forma no bloqueante dentro de un lanzamiento por lo demás enfocado en Lightning.

---

## Recién rastreados y descubiertos

### OpenDiscord v1.0.1 se lanza como un cliente estilo Discord sobre Nostr

[OpenDiscord](https://github.com/sofia-gros/open-discord) es un cliente de servidores y canales estilo Discord construido sobre Nostr con permisos basados en roles y lobbies de voz WebRTC/SFU. [v1.0.1](https://github.com/sofia-gros/open-discord/releases/tag/v1.0.1) es el primer lanzamiento con instalador etiquetado del proyecto.

### Auditable Voting v0.1.140 alinea los roles de organizador, votante y proxy de auditoría

[Auditable Voting](https://github.com/tidley/auditable-voting) es un shell de votación solo de cliente sobre Nostr. [v0.1.140](https://github.com/tidley/auditable-voting/releases/tag/v0.1.140) alinea los roles de organizador, votante y proxy de auditoría con el evento exacto de definición de cuestionario público firmado por el organizador, cerrando una brecha donde un proxy de auditoría podía actuar sobre cuentas generadas obsoletas o estado persistido de un trabajador u organizador diferente.

### Cambium v0.3.2 se empareja con Heartwood como un firmante NIP-55 sin claves

[Cambium](https://github.com/forgesworn/cambium) es la selección Discovery de este número: un firmante Android [NIP-55](/es/topics/nip-55/) que no guarda material de clave privada propio, redirigiendo cada solicitud de firma sobre [NIP-46](/es/topics/nip-46/) a un firmante de hardware Heartwood compañero. El proyecto comparte la organización de GitHub `forgesworn` con el proyecto rastreado Bray, y el propio Heartwood fue cubierto en el #30 lanzando el puente de firma relay-a-serial con el que ahora habla el lado Android de Cambium. [v0.3.2](https://github.com/forgesworn/cambium) pule la hoja de aprobación para advertir en vivo cuando la identidad seleccionada difiere del enlace existente de la aplicación y mueve las escrituras del registro de actividad a una única cola no bloqueante.

### También lanzados esta semana: echoes, Dispatch y Linky

Tres lanzamientos más merecen mención esta semana. [echoes](https://github.com/Lwb89dev/echoes) es una aplicación de notas offline-first y cifrada de extremo a extremo que se sincroniza privadamente sobre Nostr. [Dispatch](https://github.com/freecritter/dispatch) es un organizador de viajes local-first donde cada guardado se cifra con [NIP-44](/es/topics/nip-44/) y se respalda sobre Nostr bajo una clave dedicada y no vinculable, y su lanzamiento [v0.3.0](https://github.com/freecritter/dispatch) añade inicio de sesión Amber [NIP-55](/es/topics/nip-55/) para que la aplicación nunca toque la clave privada del usuario directamente. [Linky](https://github.com/hynek-jina/linky) combina contactos y DMs de Nostr con pagos Lightning y Cashu en una sola aplicación web progresiva.

---

## Trabajo de protocolo y actualizaciones de NIP

No se fusionaron PRs en el [repositorio de NIPs](https://github.com/nostr-protocol/nips) en la última semana. Se abrieron seis propuestas.

### Abierta: kind:10011 conjuntos de seguimiento favoritos

[PR #2413](https://github.com/nostr-protocol/nips/pull/2413), de fiatjaf, añade kind:10011 conjuntos de seguimiento favoritos. Refleja el patrón existente donde kind:10012 (conjuntos de relay favoritos) tiene etiquetas `a` apuntando a conjuntos de relay kind:30002, extendiendo el mismo mecanismo de favoritos a conjuntos de seguimiento kind:30000 para que un cliente pueda marcar una lista de seguimiento curada sin reemplazar su propia lista de contactos.

### Abierta: unidad cifrada privada que extiende NIP-4E

[PR #2412](https://github.com/nostr-protocol/nips/pull/2412), del equipo Form*, propone un evento genérico de Metadata, kind 34578, distinguido por una etiqueta de identificador `d` y una etiqueta de subtipo `t`, junto con un sistema de archivos cifrado privado construido encima que ya está implementado en el propio cliente Form* Drive, todavía experimental. Un registro de archivo es un evento de Metadata con `t=files`: los blobs de archivo viven en servidores [Blossom](/es/topics/blossom/) mientras que solo un índice cifrado reside en relay, y cada fragmento de archivo obtiene su propio par de claves efímero con cifrado [NIP-44](/es/topics/nip-44/) v2 derivado por HKDF. Un evento compañero de Clave de Cifrado Desacoplada guarda una clave simétrica por unidad contra la que se descifran los metadatos de cada archivo, y se basa explícitamente en [NIP-4E](/es/topics/nip-4e/), el borrador de abstracción de almacenamiento aún abierto de fiatjaf ([PR #1647](https://github.com/nostr-protocol/nips/pull/1647), abierto desde diciembre de 2024).

Esa única clave por unidad significa que una clave filtrada expone los metadatos de cada archivo en la unidad, no solo uno, ya que los pares de claves efímeros por archivo solo varían la clave de cifrado de fragmento, no la clave de descifrado de metadatos; no existe todavía ninguna ruta de rotación o revocación más allá de publicar un nuevo evento de Metadata advirtiendo que eventos más antiguos pueden perderse. Una segunda propuesta más estrecha alcanza la misma idea subyacente de NIP-4E desde un ángulo diferente: [PR #2361](https://github.com/nostr-protocol/nips/pull/2361), de fiatjaf, desacopla claves de identidad y cifrado dentro de la mensajería [NIP-17](/es/topics/nip-17/) específicamente, abierto desde el 1 de junio. Ambos PRs están sin fusionar, dejando esto como una esquina activa y disputada del espacio de diseño. Form* dice que el cliente Drive es experimental con una actualización próxima.

### Abierta: NIP-DA compartición privada de datos con permisos

[PR #2411](https://github.com/nostr-protocol/nips/pull/2411), de JAFairweather, es un nuevo borrador NIP-DA para compartición privada de datos con permisos a través de concesiones de datos con alcance. Cada usuario mantiene un registro cifrado y autoritativo por alcance en relay, y el acceso se otorga entregando privadamente la clave simétrica de ese alcance dentro de un gift wrap [NIP-59](/es/topics/nip-59/), de modo que los relay almacenan solo texto cifrado y nunca saben quién otorgó acceso a quién; una revocación es simplemente una rotación de clave, sin necesidad de reescribir la copia de cada consumidor. El autor lo posiciona como distinto de los DMs [NIP-17](/es/topics/nip-17/) (que pueden llevar una instantánea de datos pero no actualizaciones en vivo ni revocación) y de las listas privadas NIP-51 (que no llevan material de clave), y cita dos implementaciones independientes, una biblioteca de referencia en JavaScript y un CLI en Go sobre go-nostr, probadas cruzadas contra relay.damus.io, nos.lol y relay.primal.net.

### Abierta: kinds de paquetes de stickers 10031 y 30031

[PR #2410](https://github.com/nostr-protocol/nips/pull/2410), de vincenzopalazzo, registra kind 30031 (paquetes de stickers direccionables) y kind 10031 (la lista de paquetes de stickers de un usuario) en la tabla de Event Kinds, especificados por el formato "Sonar Stickers" que [Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec) lanza esta semana. Los kinds se sitúan deliberadamente un espacio por encima de los kinds de emoji personalizados [NIP-30](/es/topics/nip-30/) 30030 y 10030 para que un cliente no pueda confundir un paquete de stickers con un conjunto de emojis; los bytes de imagen de stickers viven en servidores HTTPS compatibles con [Blossom](/es/topics/blossom/), y las referencias de stickers enviados llevan un hash en texto plano para que un paquete direccionable editado no pueda cambiar silenciosamente la apariencia de stickers ya enviados en mensajes antiguos. Un PR compañero registra los mismos kinds en el proyecto separado `registry-of-kinds`.

### Abierta: fijación de mensajes NIP-29 con kind:9010 y kind:39005

[PR #2379](https://github.com/nostr-protocol/nips/pull/2379), de Anderson-Juhasc, añade fijación de mensajes a grupos basados en relay [NIP-29](/es/topics/nip-29/): kind:9010 `update-pin-list` es un evento de moderación que lleva la lista completa de eventos fijados como etiquetas `e` en orden de visualización, de modo que un solo evento puede fijar, desfijar, reordenar o limpiar el conjunto fijado, y kind:39005 es un espejo generado por el relay que expone la última lista aceptada. El diseño reemplaza un enfoque anterior de pares agregar/eliminar de [PR #1163](https://github.com/nostr-protocol/nips/pull/1163) después de retroalimentación de revisión, y elige los números de kind 9010/39005 porque 9009 y 39003 han sido reclamados desde entonces por `create-invite` y roles de grupo. Anderson-Juhasc también mantiene [Nostrord](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages), cuyo [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) se lanza esta misma semana.

### Abierta: reestructuración del descubrimiento de relay NIP-66

[PR #2241](https://github.com/nostr-protocol/nips/pull/2241), de VincenzoImp, es una reestructuración sustancial del descubrimiento de relay [NIP-66](/es/topics/nip-66/). Reemplaza la prosa suelta de "Otras etiquetas incluyen" con una sección estructurada de Etiquetas Indexadas, añade una etiqueta `W` que refleja el campo `attributes` de NIP-11 para filtrado de descubrimiento de relay, añade una etiqueta de etiqueta `l` usando espacios de nombres estandarizados (`ISO-639-1`, `ISO-3166-1`, `IANA-asn`, `IANA-tz`, `nip66.label.city`), y organiza etiquetas de RTT, SSL/TLS, red, geográficas, DNS y HTTP en secciones dedicadas junto con una nueva tabla de Tipos de Verificación. También corrige eventos de ejemplo rotos que tenían nombres de campo incorrectos, un `kind` faltante y nombres de tipo de verificación inválidos, y cierra el [issue #2171](https://github.com/nostr-protocol/nips/issues/2171). Todos los cambios mantienen compatibilidad hacia atrás ya que cada etiqueta añadida es opcional.

---

## NIP Deep Dive: NIP-99 y la extensión de comercio Gamma Markets

[NIP-15](/es/topics/nip-15/), la especificación original del Mercado Nostr, es heredada a estas alturas: modelaba un puesto de comerciante (kind 30017) con productos (kind 30018) archivados debajo, y los clientes que alguna vez corrieron sobre ella, Shopstr entre ellos, se han trasladado desde entonces a las listas de clasificados [NIP-99](/es/topics/nip-99/) como la especificación activa. NIP-99 en sí es un solo evento direccionable, kind 30402 para una lista activa o kind 30403 para un borrador, sin necesidad de crear un puesto primero. Deja todo más allá de la lista indefinido: costo de envío, estado del pedido, recibos, reseñas, y una forma de agrupar varias listas bajo una sola tienda, exactamente las partes de NIP-15 que nunca se transfirieron. [Gamma Markets](/es/topics/gamma-markets/) llena ese vacío, y es la capa de comercio moderna que vale la pena entender hoy.

### El vacío que NIP-99 deja abierto

El campo `content` de una lista NIP-99 lleva una descripción en Markdown, `price` y `location` están directamente en el evento, y las etiquetas `t` la hacen buscable como contenido ordinario de hashtag. Como es direccionable por la tupla pubkey, kind y etiqueta `d`, un vendedor edita una lista en su lugar publicando una nueva versión con la misma etiqueta `d`:

```json
{
  "kind": 30402,
  "content": "Vintage mechanical keyboard, Cherry MX Blue switches, barely used.",
  "tags": [
    ["d", "keyboard-mx-blue-01"],
    ["title", "Vintage Mechanical Keyboard"],
    ["summary", "Cherry MX Blue, barely used"],
    ["published_at", "1752537600"],
    ["location", "NYC"],
    ["price", "100", "USD"],
    ["t", "electronics"]
  ]
}
```

Esa es la especificación completa: un anuncio clasificado firmado y actualizable. Cada cliente que implementa NIP-99 para comercio electrónico real, más allá de un clasificado puntual, terminó inventando sus propias convenciones privadas para envío, mensajes de pedido y reseñas. Dos clientes NIP-99 podían renderizar correctamente una lista y aun así no tener una forma compartida de completar un pago entre ellos.

### Gamma Markets: estandarizando lo que NIP-99 dejó fuera

Gamma Markets es el nombre que un grupo de trabajo de desarrolladores de mercados Nostr, los equipos detrás de Shopstr, Cypher, Plebeian Market y Conduit Market, dieron a un conjunto compartido de convenciones de comercio electrónico construidas sobre el evento kind 30402 existente de NIP-99. La especificación está enlazada desde el documento canónico de NIP-99 a través de [PR #1784](https://github.com/nostr-protocol/nips/pull/1784) y se mantiene en su propio repositorio, [GammaMarkets/market-spec](https://github.com/GammaMarkets/market-spec).

Gamma Markets añade dos kinds independientes adyacentes a las listas. Kind 30405 agrupa múltiples listas en una colección de productos, referenciando cada una con una etiqueta `a` explícita:

```json
{
  "kind": 30405,
  "content": "Summer sale picks",
  "tags": [
    ["d", "summer-picks"],
    ["title", "Summer Sale"],
    ["a", "30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["shipping_option", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

Kind 30406 define una opción de envío con precios por país y reglas opcionales de costo basadas en peso o distancia:

```json
{
  "kind": 30406,
  "content": "Standard Regional Shipping",
  "tags": [
    ["d", "standard-regional"],
    ["title", "Standard Shipping"],
    ["price", "5.99", "USD"],
    ["country", "US"],
    ["service", "standard"],
    ["duration", "24", "72", "H"],
    ["weight-max", "30", "kg"]
  ]
}
```

La creación de pedidos, solicitudes de pago, actualizaciones de estado y envío, y recibos de pago viajan como mensajes privados ordinarios envueltos con gift-wrap [NIP-17](/es/topics/nip-17/), divididos en tres kinds por rol, no por re-envolver el transporte: kind 14 lleva comunicación libre entre comprador y comerciante, kind 16 lleva cada transición de estado del pedido (una etiqueta `type` de 1 a 4 marca creación de pedido, solicitud de pago, actualización de estado o actualización de envío), y kind 17 lleva el recibo de pago del comprador. Un mensaje de creación de pedido se ve así antes del gift-wrapping:

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

Calificar una compra completada es un kind direccionable separado, 31555, que apunta a la lista que reseña:

```json
{
  "kind": 31555,
  "content": "Arrived fast, exactly as described.",
  "tags": [
    ["d", "a:30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["rating", "1", "thumb"],
    ["rating", "1.0", "quality"],
    ["rating", "0.9", "delivery"]
  ]
}
```

Llevar los mensajes de pedido sobre NIP-17 significa que un pago de Gamma Markets usa el mismo transporte de mensajes privados que los clientes ya tienen para DMs, en lugar de un kind de mensaje de pedido a medida.

La decisión de diseño central de la especificación es que nada se hereda en cascada. Una lista que pertenece a una colección la referencia explícitamente con una etiqueta `a` en lugar de heredar automáticamente las opciones de envío o la descripción de la colección, y una opción de envío que una lista usa se referencia de la misma forma explícita. Esa es una reversión deliberada del modelo de puesto de NIP-15, donde un producto heredaba silenciosamente la moneda y la tabla de envío que su puesto padre definía. La compensación es más etiquetado explícito en cada lista, a cambio de que la configuración completa de una lista sea siempre legible desde el evento mismo, sin necesidad de resolver primero un objeto padre.

### Dónde aparece esto en la práctica

El trabajo de [Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout) de esta semana se sitúa en el mismo territorio de mensajes de pedido que Gamma Markets estandariza: el pago como invitado con clave efímera de [PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174) y la reconstrucción de la bandeja de pedidos del comerciante de [PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175) resuelven el problema de estado de pedido comprador/comerciante que los mensajes kind 14, 16 y 17 de Gamma Markets formalizan; Conduit Mono ejecuta su propio modelo de estado de pedido junto a esos kinds, sin adoptarlos directamente. Shopstr, uno de los cuatro proyectos que escribieron la especificación, también mantuvo su propia plomería de comercio en movimiento la última semana: [PR #568](https://github.com/shopstr-eng/shopstr/pull/568) extrae la lógica duplicada de gift-wrap NIP-17 en un módulo compartido, y [PR #567](https://github.com/shopstr-eng/shopstr/pull/567) lleva su parser de autenticación HTTP [NIP-98](/es/topics/nip-98/) a cobertura completa de pruebas, mantenimiento en exactamente las capas de mensajería y autenticación de las que un flujo de pedidos de Gamma Markets depende para llegar al comprador y comerciante de forma segura.

NIP-15 perdió el rol de tienda al estandarizar un puesto y un producto, y luego dejó pagos, envío, reseñas y estado de pedido como problema de la aplicación. Gamma Markets llena la mayor parte de esa superficie faltante sin tocar la forma de lista única de NIP-99, construyendo sobre la pila de DM existente de Nostr, NIP-17, en lugar de inventar una nueva capa de mensajería.

---

Eso es todo por esta semana. Si estás construyendo algo o tienes noticias para compartir, contáctanos via DM NIP-17 o encuéntranos en Nostr.
