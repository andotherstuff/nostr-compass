---
title: "Nostr Compass #30"
date: 2026-07-08
publishDate: 2026-07-08
translationOf: /en/newsletters/2026-07-08-newsletter.md
translationDate: 2026-07-08
draft: false
type: newsletters
description: "Marmot marca la especificación como adoptada y MDK publica de v0.9.0 a v0.9.3 con bindings de MarmotKit y avatares de grupo cifrados, Mostro lanza Transport v2 sobre NIP-44, Bitchat añade prueba de trabajo NIP-13 y un gateway de malla a Nostr, y rust-nostr incorpora expiración NIP-40 a los builders de gift wrap y DM privados."
---

Bienvenidos de nuevo a Nostr Compass, vuestra guía semanal de Nostr.

**Esta semana:** la [especificación de Marmot queda marcada como adoptada](#marmot-marks-the-spec-adopted-and-mdk-cuts-v09x) en 42 archivos mientras MDK publica de v0.9.0 a v0.9.3 con avatares de grupo cifrados, soporte para firmantes externos y bindings de MarmotKit para iOS y Android. [Mostro lanza Transport v2](#mostro-v0180-and-mobile-v130-ship-transport-v2-on-nip-44) sobre mensajes directos NIP-44, con barreras antispam y una ventana de coexistencia tanto en mostrod v0.18.0 como en Mobile v1.3.0. [Bitchat 1.6.0 añade prueba de trabajo NIP-13](#bitchat-160-adds-nip-13-proof-of-work-and-an-opt-in-mesh-to-nostr-gateway) a los mensajes de canales geohash, un gateway opcional de malla a Nostr que permite a un solo teléfono conectado enlazar a toda una multitud, bundles de prekeys, verificación transitiva y grupos privados cifrados gestionados por su creador. [Amber](#amber-v623-scopes-profile-subscriptions-and-adds-a-tor-status-notification) limita las suscripciones de perfil por cuenta, obtiene las listas de relays NIP-65 antes que los metadatos del perfil y añade una notificación en vivo del estado de Tor con una acción de reinicio. [rust-nostr](#rust-nostr-adds-nip-40-expiration-to-gift-wrap-and-private-dm-builders) añade expiración NIP-40 a los builders de gift wrap y DM NIP-17, anclada al timestamp aleatorio del wrap. [Amethyst](#amethyst-spends-the-week-hardening-negentropy-sync-and-adding-nip-50-search) integra 43 PR de refuerzo de la sincronización negentropy, infraestructura de búsqueda de texto completo NIP-50 y kinds para sectores especializados. [Nostrord publica v2.0.0 y v2.1.0](#nostrord-v200-and-v210-fold-the-relay-pool-and-heal-zombie-websockets) con un pool de relays unificado, detección de WebSockets zombis y una separación completa de caché con disco primero. También llegan [Ngit v2.6.2](#ngit-v262-stops-duplicate-pr-status-events-on-default-branch-push), [Jumble v26.7.1](#jumble-v2671-makes-blossom-the-default-upload-service-in-a-dm-focused-cut), [Applesauce signers 6.2.2](#applesauce-signers-622-drops-an-nbunksec-dependency), [Bray v1.33.0](#bray-v1330-cli-picks-up-a-bunker-profile-persona-and-tor-outbound), [Deepmarks 1.0.0](#deepmarks-100-hardens-the-nostr-bookmarking-surface), [Bitcredit Core v0.5.13](#bitcredit-core-v0513-unencrypts-block-metadata-on-the-nostr-wire), [Coop Mobile v0.2.4](#coop-mobile-v023-and-v024), [Granary v11.0](#granary-v110-adds-nip-71-video-event-support), [Nostr-relay v0.0.244](#nostr-relay-v00244-adds-a-firestore-backend), [Manent v1.4.0](#manent-v140-fixes-nip-42-auth-and-adds-media-clipboard-flows), [Routstrd v0.3.7](#routstrd-v037-makes-the-nostr-event-store-the-persistent-source-of-truth), [Nymchat 1.0.1](#nymchat-101-launches-as-a-progressive-web-app-on-nip-17) y [21Meetup 1.1.0](#21meetup-110-launches-nostr-signed-attendance-badges), mientras [SafeBox da la Fase 3 por prácticamente terminada](#safebox-publishes-a-phase-3-progress-report-and-a-freebsd-jail-runbook), junto con una guía de despliegue en una jail de FreeBSD y OpenETR, un spin-off para documentos electrónicos transferibles. El repositorio de NIPs integra una [armonización del nombre entre NIP-51 y NIP-37](#merged-nip-51-and-nip-37-align-the-kind-10013-name) y abre cinco propuestas: [NIP-AD Nostr Web Addresses](#open-nip-ad-nostr-web-addresses-via-well-known-lookup), [gestión de claims de códigos de invitación en NIP-86](#open-nip-86-claim-management-for-invite-codes), un [formato de color HSL para roles](#open-role-color-as-h-s-l-tuple), [procedencia de medios acreditada por hardware en NIP-80](#open-nip-80-hardware-attested-media-provenance) y una [corrección de la paginación en NIP-01](#open-nip-01-pagination-hardening). Los análisis en profundidad cubren [NIP-13 (prueba de trabajo)](#nip-deep-dive-nip-13-proof-of-work) y [NIP-40 (timestamp de expiración)](#nip-deep-dive-nip-40-expiration-timestamp).

---

## Historias principales

### Marmot marca la especificación como adoptada y MDK publica v0.9.x

El [repositorio del protocolo Marmot](https://github.com/marmot-protocol/marmot) integró la [PR #170](https://github.com/marmot-protocol/marmot/pull/170) el 3 de julio y cambió 42 archivos de `Status: draft for internal review` (y `experimental draft`) a `Status: adopted`. El título del README dejó de presentar el repositorio como un trabajo en curso y pasó a ser "Marmot Protocol" como texto adoptado; los documentos de la era MIP se replantearon como la versión obsoleta del protocolo; y la sección "Review Status" ("This is not adopted spec text yet") se convirtió en "Review Guidance" para editar la especificación vigente. La etiqueta `v2` desaparece: expresiones de contraste con MIP como "new in v2" y "the v2 spec keeps" pasan a ser "this spec" y "under this spec". Dos documentos conservan deliberadamente el estado de borrador: `implementation-model.md` sigue siendo no normativo y el documento de la función multidispositivo continúa como borrador.

El mismo repositorio incorporó la [PR #171](https://github.com/marmot-protocol/marmot/pull/171), que alinea las invariantes de política de administración, membresía y cambios de rol. La comprobación transversal que impide que un Remove deje al grupo sin admin se expresa ahora como propiedad de cada epoch resultante, evaluada respecto al conjunto de admins del epoch anterior cuando un commit no incluye una actualización de la política. La regla de ramas candidatas de Convergence se endurece: "validates" significa la validez completa del commit, incluidas las comprobaciones transversales del epoch resultante, por lo que un commit que viola una invariante no puede crear una arista candidata en ninguna rama. Las notificaciones de estado derivadas de un commit sustituido DEBEN retirarse cuando la selección de rama lo reemplaza, cerrando en la especificación el fallo por el que un cambio de nombre perdedor aparecía como mensaje de sistema correcto. Una nueva sección "Realizing removal" de `member-departure.md` define la entrada primaria (el commit canónico aceptado que elimina tu última leaf) y la alternativa para clientes que nunca aplicaron ese commit: la evidencia autenticada posterior a la expulsión produce ahora `SelfEvicted`, conservando como inactiva la copia del grupo eliminado. Después, la [PR #236](https://github.com/marmot-protocol/marmot/pull/236) endureció la validación en el límite de wire: fija la vida aceptable de KeyPackage en 84 días más una hora de margen, añade una tabla de cardinalidad de tags Nostr para `h` de grupo, `p` de gift wrap, `e` y `relays` de welcome y tags de KeyPackage, y aclara que ids y metadatos de eventos Nostr no verificados no constituyen evidencia fiable de routing, replay ni telemetría.

Más abajo en la cadena, el [workspace de MDK](https://github.com/marmot-protocol/mdk) publicó [v0.9.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.0) el 6 de julio con una actualización de versión de todo el workspace, seguida de [v0.9.1](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.1), [v0.9.2](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.2) y [v0.9.3](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.3) durante los dos días siguientes. v0.9.0 rota entradas obsoletas del keyring al crear una nueva base SQLite e impone validar antes de mutar en toda la capa de almacenamiento. v0.9.1 encamina cada conexión saliente por un único punto de control de seguridad del host mediante la [PR #732](https://github.com/marmot-protocol/mdk/pull/732), cerrando los fallos en los que distintos call sites alcanzaban la red con validaciones diferentes. v0.9.3 expone avatares de grupo cifrados en los bindings uniffi mediante `download_group_image` e `image_hash_hex` en la [PR #771](https://github.com/marmot-protocol/mdk/pull/771), añade soporte para firmantes externos y declara `wn-opencode` listo para producción mediante la [PR #781](https://github.com/marmot-protocol/mdk/pull/781). Junto a estas versiones, MarmotKit publica bindings de iOS y Android para cada versión: MarmotKit.xcframework y bindings Swift en iOS, y bindings Kotlin con bibliotecas JNI en Android, generados a partir de un hash de commit fijo de MDK. Un nuevo canal de versiones de wn-agent ofrece instaladores de shell que fijan WN Agent a un tag inmutable para que las apps obtengan el agente actual con un solo comando `curl`.

### Mostro v0.18.0 y Mobile v1.3.0 lanzan Transport v2 sobre NIP-44

Mostro es el protocolo de compraventa peer-to-peer de Bitcoin que ejecuta libros de órdenes, escrow y resolución de disputas sobre eventos Nostr, coordinado por un daemon (`mostrod`) con el que los clientes se comunican mediante DM cifrados. Hasta esta semana, el protocolo wire entre clientes y mostrod era Transport v1. [Mostro v0.18.0](https://github.com/MostroP2P/mostro/releases/tag/v0.18.0) incorpora Transport v2 sobre mensajes directos [NIP-44](/es/topics/nip-44/), con barreras antispam y recepción dual en el servidor. La [PR #776](https://github.com/MostroP2P/mostro/pull/776) contiene el cambio wire de la Fase 1; la [PR #780](https://github.com/MostroP2P/mostro/pull/780) añade las barreras antispam de la Fase 2; y la [PR #785](https://github.com/MostroP2P/mostro/pull/785) hace que la versión interna siga al transporte activo, permitiendo que clientes v2 y v1 coexistan durante la migración. La [PR #782](https://github.com/MostroP2P/mostro/pull/782) corrige además un tag informativo NIP-33 al renombrar `protocol_versions` como `protocol_version`. La versión incorpora también una ruta unificada de cotización en vivo de Fase 4 con caché y control de antigüedad ([PR #783](https://github.com/MostroP2P/mostro/pull/783)), y El Toque como proveedor de cruces fiat para los pares cubanos CUP y MLC ([PR #778](https://github.com/MostroP2P/mostro/pull/778)). La [PR #779](https://github.com/MostroP2P/mostro/pull/779) notifica a la parte penalizada cuando una disputa le quita la fianza; antes el usuario solo veía que faltaba saldo.

[Mostro Mobile v1.3.0](https://github.com/MostroP2P/mobile/releases/tag/v1.3.0) es la mitad cliente de la migración. La [PR #613](https://github.com/MostroP2P/mobile/pull/613) migra la app a Riverpod 3.x; la Fase A ([PR #620](https://github.com/MostroP2P/mobile/pull/620)) añade recepción dual de mensajes NIP-44 en el isolate principal y en segundo plano; la Fase B de la [PR #624](https://github.com/MostroP2P/mobile/pull/624) añade envío dual; la [PR #632](https://github.com/MostroP2P/mobile/pull/632) lo vuelve a aplicar tras el cambio a Riverpod 3.x; y la Fase C de la [PR #637](https://github.com/MostroP2P/mobile/pull/637) finaliza la migración. La versión amplía también los métodos de pago africanos: la [PR #625](https://github.com/MostroP2P/mobile/pull/625) añade la kwacha malauí y la [PR #627](https://github.com/MostroP2P/mobile/pull/627) incorpora KES, MZN, TZS, UGX, ZAR y ZMW, además de ampliar NGN. El flujo de restauración espera ahora a que el nodo tenga conectividad, y el tratamiento según la causa distingue entre pérdida de fianza por disputa y por timeout.

### Bitchat 1.6.0 añade prueba de trabajo NIP-13 y un gateway opcional de malla a Nostr

[Bitchat 1.6.0](https://github.com/permissionlesstech/bitchat/releases/tag/v1.6.0) es la app de chat en malla Bluetooth que usa Nostr para sus canales geohash y la entrega de DM. La [PR #1382](https://github.com/permissionlesstech/bitchat/pull/1382) añade [NIP-13 (prueba de trabajo)](/es/topics/nip-13/) a los mensajes salientes de canales geohash, eventos efímeros kind 20000: cada envío mina un tag `["nonce", "<value>", "<target>"]` antes de publicar, con un objetivo de 8 bits cero iniciales. Eso supone una media de 256 hashes y tarda menos de un milisegundo en un Mac serie M. Los eventos entrantes con PoW validada relajan el límite por remitente, de modo que el spammer paga cómputo por mensaje sin que un remitente normal perciba el coste. El alcance es deliberadamente estrecho: solo los mensajes kind 20000 minan PoW; los heartbeats de presencia kind 20001, las notas de ubicación kind 1 y los DM no cambian.

La [PR #1384](https://github.com/permissionlesstech/bitchat/pull/1384) añade el modo gateway, un enlace ascendente opcional de la malla a Nostr para canales geohash. Cuando un usuario solo en malla, sin internet ni relay accesible, envía un mensaje y otro peer anuncia la capacidad `.gateway`, el evento kind 20000 firmado se envuelve en un nuevo sobre TLV `MessageType.nostrCarrier = 0x28` y se dirige a un gateway. Ese peer publica el evento en Nostr por cuenta del remitente y retransmite a la malla el tráfico entrante con el TTL predeterminado. El uplink usa la ruta del sobre courier, dirigida y retransmitida en varios saltos; el downlink usa broadcast. El evento se firma antes de salir del remitente, por lo que el gateway decide si publicarlo pero no puede falsificar la atribución. La motivación son desastres y protestas donde basta un teléfono conectado para dar a toda la multitud un uplink Nostr operativo.

La misma versión incorpora otro bloque de trabajo relacionado. La [PR #1381](https://github.com/permissionlesstech/bitchat/pull/1381) añade bundles de prekeys para un primer contacto asíncrono con forward secrecy mediante courier mail: se puede escribir a un peer offline y entregar el mensaje a la malla sin un handshake Noise en vivo. La [PR #1380](https://github.com/permissionlesstech/bitchat/pull/1380) añade verificación transitiva: alguien que ha completado el handshake Noise con un contacto ya verificado queda avalado sobre esa sesión, propagando la confianza un salto cada vez. La [PR #1383](https://github.com/permissionlesstech/bitchat/pull/1383) añade grupos privados cifrados gestionados por su creador; la [PR #1376](https://github.com/permissionlesstech/bitchat/pull/1376) detecta, muestra y canjea tokens ecash Cashu con `/pay`; y la [PR #1379](https://github.com/permissionlesstech/bitchat/pull/1379) añade un tablón geohash persistente y firmado sobre la sincronización de malla. La [PR #1372](https://github.com/permissionlesstech/bitchat/pull/1372) amplía store-and-forward con couriers abiertos, routing spray-and-wait, outbox persistente y seis horas de historial público. Bitchat 1.5.4 se publicó [al principio de la semana](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.4) con la corrección integral de favoritos de la [PR #1367](https://github.com/permissionlesstech/bitchat/pull/1367), que limpia duplicados en la lista de peers, la sincronización Nostr y la corrupción de claves `/fav`.

---

## Versiones etiquetadas

### Amber v6.2.3 limita las suscripciones de perfil y añade una notificación del estado de Tor

[Amber v6.2.3](https://github.com/greenart7c3/Amber/releases/tag/v6.2.3) mejora rendimiento y corrección en el firmante Android [NIP-46](/es/topics/nip-46/). Añade un intervalo configurable para obtener perfiles, con opciones nunca y siempre ([PR #492](https://github.com/greenart7c3/Amber/pull/492)); muestra la foto en el selector de cuenta; y limita las suscripciones de perfil a la cuenta actual, evitando que un firmante multicuentas mantenga suscripciones para cuentas inactivas. El parser de permisos bunker trata explícitamente los errores. Corrige además varias infracciones de StrictMode: DiskReadViolation en el log `onSuccess` de Coil, acceso al keystore al cargar la cuenta en el hilo principal, lecturas del nombre y foto de la cuenta y construcción anticipada de `KeyPair()` en login y registro. Tras v6.2.3, la [PR #493](https://github.com/greenart7c3/Amber/pull/493) reordenó el arranque para obtener la lista de relays [NIP-65](/es/topics/nip-65/) antes de los metadatos del perfil; la [PR #494](https://github.com/greenart7c3/Amber/pull/494) convirtió la notificación de Tor en un indicador vivo con reinicio; y la [PR #495](https://github.com/greenart7c3/Amber/pull/495) activó Android Lint con warnings como errores en todo el código.

### Jumble v26.7.1 convierte Blossom en el servicio de subida predeterminado en una versión centrada en DM

[Jumble v26.7.1](https://github.com/CodyTseng/jumble/releases/tag/v26.7.1) es una versión del cliente web centrada en mensajes directos y medios. Rediseña los ajustes de subida y establece [Blossom](/es/topics/blossom/) como servicio predeterminado en lugar de NIP-96. Los DM reciben menú móvil, mejores acciones en escritorio, botón para ir al último mensaje, reacciones por pulsación larga y reintento de envíos fallidos. También mejora el editor de emojis personalizados, el tamaño de burbujas para facturas y contenido incrustado, el orden y scroll de DM, la inserción de emojis, la copia de texto y el arrastre de archivos. Corrige la orientación de imágenes al eliminar metadatos y añade descargas Linux ARM64.

### Applesauce signers 6.2.2 elimina una dependencia de nbunksec

[applesauce-signers@6.2.2](https://github.com/hzrd149/applesauce/releases/tag/applesauce-signers%406.2.2) sustituye la dependencia `@sandwichfarm/encoded-entities` por un helper integrado de [nbunksec](/es/topics/nip-46/) mediante el [commit d654349](https://github.com/hzrd149/applesauce/commit/d654349). La codificación de sesiones bunker [NIP-46](/es/topics/nip-46/) ya no necesita la biblioteca externa, reduciendo una superficie de supply chain para clientes que consumen el paquete.

### Ngit v2.6.2 evita eventos de estado de PR duplicados al hacer push a la rama predeterminada

[Ngit v2.6.2](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.6.2) corrige el CLI git-over-Nostr. `git push` a la rama predeterminada deja de publicar estados duplicados de merge/applied para PR ya aplicadas, porque la detección consulta ahora el estado Nostr del repositorio anterior al push, fuente de verdad en el lado [NIP-34](/es/topics/nip-34/). El heurístico previo dependía de internals de git. Los repositorios activos dejan así de emitir eventos kind 1621 duplicados.

### El CLI Bray v1.33.0 incorpora perfil bunker, persona y salida por Tor

[Bray v1.33.0](https://github.com/forgesworn/bray/releases/tag/v1.33.0) añade a `bunker --profile <name>` una clave de conexión estable automática y fallback de relay; `bunker --persona <name>` firma como una identidad derivada de un árbol nsec; y todas las peticiones HTTP pueden pasar por un proxy SOCKS de Tor. La versión suma subcomandos de wallet para NWC [NIP-47](/es/topics/nip-47/), operaciones de administración de grupos [NIP-29](/es/topics/nip-29/), verbos NIP-86 y helpers de outbox [NIP-65](/es/topics/nip-65/). Los verbos de publicación incorporan `--jsonl`, `--csv`, `--tsv`, `req`, `event`, `publish-raw`, `bunker sign` y `--relay` por comando. El trabajo de seguridad cubre zeroisation de secretos, bearer auth y rate limits HTTP, y validación SSRF de URLs de relays. El tarball npm ocupa 533.844 bytes y su build reproducible idéntico se verificó en dos runners CI independientes.

### Deepmarks 1.0.0 endurece la superficie de marcadores Nostr

[Deepmarks 1.0.0](https://github.com/ostermayer/deepmarks-public/releases/tag/v1.0.0) es un hito de seguridad para un servicio público de marcadores Nostr, donde cada marcador sigue siendo un evento firmado. La API y el worker pueden alcanzar Redis interno, el relay del bunker y metadatos cloud, por lo que la defensa SSRF es crítica. La versión corrige un bypass con literales IPv6 en `isPrivateIp`: `[::1]`, `[fd00::1]` y `[::ffff:10.0.0.4]` se clasificaban como públicos. Ahora elimina corchetes y reduce IPv6 compatible o mapeado a IPv4 antes de comprobar rangos privados. Los perfiles `kind:0` externos se verifican en el sink para impedir que un relay hostil falsifique `nip05` o `lud16`; las URLs se validan por esquema en cada render para bloquear tags `d` `javascript:` o `data:` en marcadores `kind:39701`. Los recibos de zap sobreviven a una caída temporal del bunker: el handler reclama el zap pendiente atómicamente, finaliza tras firmar y libera el claim si falla. El drenaje de `/publish` usa `BLMOVE` hacia una lista por worker con recuperación condicionada por heartbeat, preservando eventos firmados aunque el worker caiga tras responder 202.

### Bitcredit Core v0.5.13 deja sin cifrar los metadatos de bloque en el wire de Nostr

[Bitcredit Core v0.5.13](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.13) elimina una capa de cifrado de los eventos públicos del protocolo de letras de crédito. Los metadatos de bloque (id, hash y firma) quedan sin cifrar; solo los datos del bloque siguen cifrados con la clave de la letra. Las apps nuevas procesan cadenas antiguas, pero las antiguas no procesan cadenas nuevas. Añade una función para obtener la cadena y publicación con umbral optimista: al aceptar un relay, por defecto, los demás reciben el evento asíncronamente, sin bloquear por el más lento.

### Coop Mobile v0.2.3 y v0.2.4

[Coop Mobile](https://git.reya.su/reya/coop-mobile) publicó [v0.2.3](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.3) el 4 de julio y [v0.2.4](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.4) el 7. El cliente Android de DM [NIP-17](/es/topics/nip-17/) añade imágenes y enlaces inline, adjuntos, dictado y confirmación al eliminar contactos. v0.2.4 corrige un indicador bloqueado, mejora el handshake Nostr Connect y añade importación `ncryptsec1`, el formato de clave privada cifrada [NIP-49](/es/topics/nip-49/), con una pantalla de importación rediseñada.

### Granary v11.0 añade soporte para eventos de vídeo NIP-71

[Granary v11.0](https://github.com/snarfed/granary/releases/tag/v11.0) es la biblioteca de conversión multiprotocolo que impulsa Bridgy Fed. Los eventos de vídeo [NIP-71](/es/topics/nip-71/) (kinds 21, 22, 34235 y 34236) se convierten ahora en notas ActivityStreams 1 con adjuntos; extrae `imeta`, duración, `published_at` y `alt` como `displayName` alternativo. En la API, `sign` pasa a llamarse `hash_and_sign`; `verify` y el constructor `Nostr` lanzan `ValueError` al fallar; y `Nostr.query` omite correctamente el desafío AUTH [NIP-42](/es/topics/nip-42/) sin `privkey`. Otra corrección evita fallos cuando un objeto Nostr `article` carece de `id`.

### Nostr-relay v0.0.244 añade un backend Firestore

[mattn/nostr-relay v0.0.244](https://github.com/mattn/nostr-relay/releases/tag/v0.0.244) añade Firestore mediante la [PR #12](https://github.com/mattn/nostr-relay/pull/12), ofreciendo a operadores del relay una base serverless gestionada de Google Cloud junto a los backends existentes.

### Manent v1.4.0 corrige AUTH NIP-42 y añade flujos de portapapeles multimedia

[Manent v1.4.0](https://github.com/dtonon/manent/releases/tag/v1.4.0) es una app de notas y archivos cifrados sobre Nostr con cifrado [NIP-44](/es/topics/nip-44/), firmantes [NIP-46](/es/topics/nip-46/) y [NIP-55](/es/topics/nip-55/), routing outbox [NIP-65](/es/topics/nip-65/) y Blossom. Corrige AUTH [NIP-42](/es/topics/nip-42/), subidas Blossom a hosts `http://` y el flujo de compresión. Ahora permite copiar y pegar imágenes, arrastrar archivos, recortar y girar imágenes, reproducir vídeos y gifs y grabar vídeo con una pulsación larga. En Linux, el portapapeles primario funciona con clic central. También optimiza carga y scroll.

### Routstrd v0.3.7 convierte el almacén de eventos Nostr en la fuente de verdad persistente

[Routstrd v0.3.7](https://github.com/routstr/routstrd/releases/tag/v0.3.7) es el daemon local de la red descentralizada de inferencia de IA Routstr, que descubre proveedores con kind 38421 y reseñas LGTM con kind 38425. `routstrd update` descarga binarios de routstrd y cocod y reinicia limpiamente los daemons. `refreshNostrEvents()` se ejecuta al arrancar y cada 21 minutos. `@routstr/sdk` pasa de 0.3.12 a 0.3.15, elimina ProviderRegistry en favor de `DiscoveryAdapter`, limpia modelos de proveedores desaparecidos y trata el almacén de eventos como fuente persistente, eliminando el TTL erróneo de 210 minutos. En reembolsos Xcashu prueba primero los tokens de devolución, reintenta los 404 tres veces cada dos minutos y trata 425 Too Early sin lanzar error.

### Nymchat 1.0.1 se lanza como Progressive Web App sobre NIP-17

[Nymchat 1.0.1](https://github.com/Spl0itable/NYM), también NYM o Nostr Ynstant Messenger, es una PWA y app iOS/Android para chat efímero sobre Nostr conectada con Bitchat. Usa kind 20000 en canales geohash, kind 23333 en canales con nombre y gift wraps [NIP-17](/es/topics/nip-17/) kind 1059 para privados y grupos, con claves efímeras rotatorias y recuperación post-compromiso. Permite identidad efímera por sesión o persistente mediante extensiones [NIP-07](/es/topics/nip-07/), firmante remoto [NIP-46](/es/topics/nip-46/) o nsec. El cifrado local opcional usa contraseña, PIN, passkey o biometría mediante WebAuthn PRF o PBKDF2, sin escribir la clave en claro. Las llamadas usan gift wraps para señalización y WebRTC para medios. Las reacciones usan [NIP-25](https://github.com/nostr-protocol/nips/blob/master/25.md), los emojis [NIP-30](/es/topics/nip-30/), y Cloudflare Pages Functions actúa como proxy de privacidad.

### 21Meetup 1.1.0 lanza insignias de asistencia firmadas con Nostr

[21Meetup 1.1.0](https://github.com/louisthecat86/Einundzwanzig-Meetup-App) es una app Flutter para la comunidad alemana Einundzwanzig que registra asistencia con NFC y QR rotatorios. Cada insignia es un evento Nostr kind 21000 firmado por el organizador con Schnorr BIP-340. El QR cambia cada 10 segundos y el NFC exige proximidad, impidiendo acuñación remota. Una puntuación de confianza se calcula localmente y puede mostrarse como QR en intercambios peer-to-peer. Se orienta a reputación en comunidades Bitcoin, pero cualquier lector puede verificar los eventos.

### Nostrord v2.0.0 y v2.1.0 unifican el pool de relays y curan WebSockets zombis

[Nostrord v2.0.0](https://github.com/nostrord/nostrord/releases/tag/v2.0.0) es una versión mayor del cliente KMP/WASM compatible con NIP-29, NIP-42, NIP-44, NIP-46, NIP-57, NIP-65 y NIP-98. [v2.0.1](https://github.com/nostrord/nostrord/releases/tag/v2.0.1) llegó un día después mediante la [PR #166](https://github.com/nostrord/nostrord/pull/166): los paquetes 2.0.0 fallaban al iniciar con `NoClassDefFoundError: java/sql/DriverManager` porque la imagen jlink no incluía `java.sql`, dependencia de SQLDelight. La corrección añade el módulo y encamina el envío optimista por la red en lugar de limitarse a cachearlo, además de mejorar teclado y scroll en web móvil.

[v2.1.0](https://github.com/nostrord/nostrord/releases/tag/v2.1.0) llegó el 7 de julio con la unificación del pool ([PR #176](https://github.com/nostrord/nostrord/pull/176)). El socket NIP-29 separado entra en el pool común; un scheduler reconecta todos los relays; AUTH [NIP-42](/es/topics/nip-42/) tiene reintentos acotados; la publicación falla de forma segura y reintenta cuando se exige auth; se cierran carreras de tormentas de peticiones; las listas kind 10009 se agrupan por relay; y `mux_chat` cubre todos los grupos unidos y se recupera si un relay descarta la suscripción. La UI sustituye la fila "Sending..." por iconos inline y ofrece Retry al atascarse el historial. La [PR #179](https://github.com/nostrord/nostrord/pull/179) detecta WebSockets zombis en Android: `lastInboundAtMs` se actualiza con cada frame, `markDead()` activa la ruta normal de reconexión y `probeLiveness()` exige respuesta en cinco segundos. También impide escribir mensajes optimistas en caché persistente antes de confirmar la entrega. [v2.1.1](https://github.com/nostrord/nostrord/releases/tag/v2.1.1) añadió actuals de iOS, tests nativos e iconos mediante la [PR #178](https://github.com/nostrord/nostrord/pull/178).

---

## Cambios aún no publicados

### rust-nostr añade expiración NIP-40 a builders de gift wrap y DM privados

[rust-nostr integró la PR #1384](https://github.com/rust-nostr/nostr/pull/1384), que añade una opción `expiration` a `GiftWrapBuilder` y `PrivateDirectMessageBuilder`. La biblioteca recibe una `Duration`: el tag [NIP-40](/es/topics/nip-40/) se ancla al `created_at` aleatorio del gift wrap, desacoplándolo del envío real. Un timestamp absoluto filtraría la hora de envío al observador, por lo que la biblioteca construye el tag internamente. Va en el gift wrap, no en el seal kind 13, que [NIP-59](/es/topics/nip-59/) exige sin tags. NIP-17 transmite el mismo valor desde `PrivateDirectMessageBuilder`. El cambio cierra el [issue #1381](https://github.com/rust-nostr/nostr/issues/1381) con el patrón de builder usado para `extra_tags`. La [PR #1387](https://github.com/rust-nostr/nostr/pull/1387) integra además `nostr-relay-builder` en `nostr-sdk`.

### Amethyst dedica la semana a reforzar negentropy y añadir búsqueda NIP-50

La [rama main de Amethyst](https://github.com/vitorpamplona/amethyst) integró 43 PR en tres frentes. En sincronización negentropy entre geode y strfry, el fallo refused-window deja de provocar bucles de división y retrocede limpiamente ([PR #3480](https://github.com/vitorpamplona/amethyst/pull/3480)); `negentropyKmp` pasa a v1.1.1 ([PR #3475](https://github.com/vitorpamplona/amethyst/pull/3475)); llega un benchmark de un millón de eventos con espejo de paridad strfry ([PR #3478](https://github.com/vitorpamplona/amethyst/pull/3478)); y benchmarks de producción entran en CI con más optimizaciones ([PR #3458](https://github.com/vitorpamplona/amethyst/pull/3458), [PR #3466](https://github.com/vitorpamplona/amethyst/pull/3466)). Colecciones concurrentes lock-free sustituyen el mutex por relay y se corrige el threading UDP ([PR #3459](https://github.com/vitorpamplona/amethyst/pull/3459)).

El segundo frente es la búsqueda de texto completo [NIP-50](/es/topics/nip-50/). Una interfaz `SearchableEvent` permite llevar metadatos de índice ([PR #3452](https://github.com/vitorpamplona/amethyst/pull/3452)); las extensiones NIP-50 se eliminan antes de consultar SQLite FTS para no pasar sintaxis del servidor al motor local ([PR #3464](https://github.com/vitorpamplona/amethyst/pull/3464)); y se centralizan los relays de búsqueda predeterminados ([PR #3446](https://github.com/vitorpamplona/amethyst/pull/3446)).

El tercero integra sectores especializados: eventos Birdstar de detección de aves kind 2473 ([PR #3473](https://github.com/vitorpamplona/amethyst/pull/3473)) y estados de tarjetas de memoria PS1 como eventos firmados kind 38192 ([PR #3482](https://github.com/vitorpamplona/amethyst/pull/3482)). Completan la semana una firma personalizada automática ([PR #3450](https://github.com/vitorpamplona/amethyst/pull/3450)), notificaciones de escritorio rediseñadas ([PR #3457](https://github.com/vitorpamplona/amethyst/pull/3457)), bloqueo de privacidad en Messages ([PR #3432](https://github.com/vitorpamplona/amethyst/pull/3432)), escritura local en `NostrServer.ingest` con omisión de verificación por envío ([PR #3469](https://github.com/vitorpamplona/amethyst/pull/3469)) y contratos `equals`/`hashCode` corregidos en OpenTimestamps ([PR #3477](https://github.com/vitorpamplona/amethyst/pull/3477)).

### Buzz sigue reforzando el relay y define kind 44200 para métricas de turnos de agentes

[Buzz](https://github.com/block/buzz), antes Sprout, integró 123 PR entre el 1 y el 7 de julio. La [PR #1441](https://github.com/block/buzz/pull/1441) define métricas cifradas y duraderas NIP-AM de turnos de agentes como kind 44200, archivadas como eventos firmados en el relay del usuario. Le siguen un archivo local ([PR #1555](https://github.com/block/buzz/pull/1555)), eliminación atómica del kind ([PR #1562](https://github.com/block/buzz/pull/1562)) y el nombre del modelo en la emisión para distinguir cada turno ([PR #1564](https://github.com/block/buzz/pull/1564)).

El segundo frente es el rendimiento del relay. Se aplaza el dispatch posterior al commit y se evita clonar para verificar ([PR #1453](https://github.com/block/buzz/pull/1453)); se agrupan round trips de ingest y fan-out, reduciendo p99 entre 7 y 16% y p999 entre 29 y 53% ([PR #1454](https://github.com/block/buzz/pull/1454)); las consultas multifiltro tienen concurrencia acotada ([PR #1457](https://github.com/block/buzz/pull/1457)); y los frames WebSocket salientes se agrupan ([PR #1464](https://github.com/block/buzz/pull/1464)). Los admins pueden configurar iconos por comunidad servidos mediante [NIP-11](/es/topics/nip-11/) ([PR #1463](https://github.com/block/buzz/pull/1463)); los propietarios borran mensajes de sus agentes con eventos kind 5 ([PR #1519](https://github.com/block/buzz/pull/1519)); OpenTelemetry acompaña a Prometheus ([PR #1398](https://github.com/block/buzz/pull/1398)); y el registro de nombres git pasa a Postgres ([PR #1432](https://github.com/block/buzz/pull/1432)).

### Divine Video conecta la verificación de firmas del relay y extrae NostrConnect

La [app móvil de Divine Video](https://github.com/divinevideo/divine-mobile) integró 97 PR. La [PR #5774](https://github.com/divinevideo/divine-mobile/pull/5774) verifica firmas de eventos entrantes; la [PR #5828](https://github.com/divinevideo/divine-mobile/pull/5828) cifra el token push FCM en el evento de baja kind 3080; y la [PR #5831](https://github.com/divinevideo/divine-mobile/pull/5831) fragmenta la REQ de borrado kind 5 para usuarios con mucho historial. La [PR #5826](https://github.com/divinevideo/divine-mobile/pull/5826) extrae `NostrConnectCoordinator` para el flujo `nostrconnect://`, preparando la refactorización de auth del [issue #4741](https://github.com/divinevideo/divine-mobile/issues/4741). La [PR #5709](https://github.com/divinevideo/divine-mobile/pull/5709) mapea reposts kind 16 cuando falta `notification_type`.

### Zap Cooking corrige el login bunker NIP-46 y añade búsqueda de recetas NIP-50

El [frontend de Zap Cooking](https://github.com/zapcooking/frontend) integró 18 PR. La [PR #503](https://github.com/zapcooking/frontend/pull/503) corrige el login bunker con handshake explícito, tratamiento de authUrl y errores visibles. La [PR #495](https://github.com/zapcooking/frontend/pull/495) añade auth NIP-98 a subidas de imagen y texto para atribuirlas a una pubkey. La [PR #483](https://github.com/zapcooking/frontend/pull/483) incorpora búsqueda NIP-50 mediante el relay nostrarchives sin índice del cliente. También muestra notas citadas y medios directamente ([PR #491](https://github.com/zapcooking/frontend/pull/491)), añade previews y tamaños de hashtags ([PR #492](https://github.com/zapcooking/frontend/pull/492)), consultas de varias palabras ([PR #482](https://github.com/zapcooking/frontend/pull/482)) y tarjetas sociales generadas en servidor ([PR #494](https://github.com/zapcooking/frontend/pull/494)).

### swift-nostr-client v0.6.0 avanza hacia una primera versión estable

[yysskk/swift-nostr-client](https://github.com/yysskk/swift-nostr-client) publicó [v0.6.0](https://github.com/yysskk/swift-nostr-client/releases/tag/v0.6.0) junto a 30 PR. La biblioteca se acerca a una API estable para clientes Swift que no enlazan MDK ni MarmotKit.

### Nostr Applet Protocol (NAPS) endurece el routing y fanout de NAP-OUTBOX

NAPS tuvo una semana de limpieza, sobre todo en [NAP-OUTBOX](https://github.com/napplet/naps/pull/32): menos routing controlado por el caller, menos detalles de relays filtrados y un resultado de evento compartido con hints y sidecars de recursos, enlazado con [NAP-RESOURCE](https://github.com/napplet/naps/pull/80). Las reglas explícitas de fanout a outbox, inbox y relay reducen la ambigüedad y mejoran la interoperabilidad.

### El toolchain de Napplet refuerza la alineación con el protocolo y lanza su CLI

Los paquetes Napplet pasan de un SDK útil a un toolchain más cohesionado: soporte de consultas [NAP-COUNT](https://github.com/napplet/web/pull/104), ciclo de vida de [OUTBOX](https://github.com/napplet/web/pull/112) controlado por runtime y sidecars [RelayEventResult](https://github.com/napplet/web/pull/108). También mejoran el registro CVM, envelopes de error DM, contexto de sesión MEDIA, contadores LISTS, resultados COMMON y el esquema htree: RESOURCE. El nuevo [@napplet/cli](https://github.com/napplet/web/pull/103) añade descubrimiento de configuración, planes de despliegue, firma, subidas Blossom y manifiestos. El [prelude inyectable por el host](https://github.com/napplet/web/pull/127) y la [preparación para JSR](https://github.com/napplet/web/pull/145) facilitan inyectar, publicar y verificar el stack.

### primal-android amplía la superficie del firmante remoto

[Primal Android](https://github.com/PrimalHQ/primal-android-app) integró 18 PR. La [PR #1075](https://github.com/PrimalHQ/primal-android-app/pull/1075) implementa `switch_relays` y `logout` para el rol de firmante remoto NIP-46. La [PR #1083](https://github.com/PrimalHQ/primal-android-app/pull/1083) añade migraciones locales tras la splash y la [PR #1080](https://github.com/PrimalHQ/primal-android-app/pull/1080) precarga el feed de notas. El resto pule barras de Home, hints de Explore y perfiles.

### Wisp añade selector multicuentas y tests del parser de Blossom

[Wisp](https://github.com/barrydeen/wisp) integró 9 PR. La [PR #604](https://github.com/barrydeen/wisp/pull/604) añade selector multicuentas con cancelación explícita. La [PR #613](https://github.com/barrydeen/wisp/pull/613) prueba `Blossom.parseServerList`. La [PR #574](https://github.com/barrydeen/wisp/pull/574) rehace la hoja de zap para iOS; la [PR #605](https://github.com/barrydeen/wisp/pull/605) convierte el historial en una hoja deslizable; la [PR #611](https://github.com/barrydeen/wisp/pull/611) reconoce hashtags Unicode; la [PR #609](https://github.com/barrydeen/wisp/pull/609) mantiene la paginación del feed y muestra galerías inline; y la [PR #603](https://github.com/barrydeen/wisp/pull/603) conserva líneas vacías antes de perfiles y hashtags inline.

### TAO y Wired elevan la señal PoW a 21 bits y muestran raíces con PoW reciente

[smolgrrr/TAO](https://github.com/smolgrrr/TAO) y [smolgrrr/Wired](https://github.com/smolgrrr/Wired) integraron los mismos 13 PR. La [PR #84](https://github.com/smolgrrr/TAO/pull/84) eleva el objetivo de prueba de trabajo predeterminado a 21 bits cero iniciales; la [PR #80](https://github.com/smolgrrr/TAO/pull/80) muestra raíces del feed con PoW reciente para ordenar por trabajo NIP-13, no solo por antigüedad. La [PR #75](https://github.com/smolgrrr/TAO/pull/75) recupera el selector de emojis y la [PR #65](https://github.com/smolgrrr/TAO/pull/65) añade previews del primer frame. Es el segundo cliente de la semana que usa NIP-13 como filtro principal, junto con Bitchat.

### keep-android pule la UX NIP-46 e incorpora una corrección TOCTOU

[privkeyio/keep-android](https://github.com/privkeyio/keep-android) publicó [v1.1.5](https://github.com/privkeyio/keep-android/releases/tag/v1.1.5) con 13 PR y [v1.1.6](https://github.com/privkeyio/keep-android/releases/tag/v1.1.6) el 8 de julio, fijando keep core v0.5.0. Keep es una bóveda de identidad móvil, descrita como CustID en el [número #29](/en/newsletters/2026-07-01-newsletter/#custid-launches-as-a-mobile-identity-vault-with-nip-46-and-nfc-challenge-flow). v1.1.5 pule el desafío [NIP-46](/es/topics/nip-46/). v1.1.6 cierra una carrera TOCTOU en `set_active_share`, muestra URL y método en la aprobación HTTP [NIP-98](/es/topics/nip-98/) y hace que el chequeo RNG devuelva error en vez de panic. Un test instrumentado cubre el kill switch NIP-55. Las funciones CLI v0.5.0 (desbloqueo threshold-OPRF, DKG por software y wallets HD FROST) aún no se exponen en Android.

### Heartwood lanza el puente de firma de relay a serial

[forgesworn/heartwood v0.7.0](https://github.com/forgesworn/heartwood/releases/tag/v0.7.0) entrega el puente relay-a-serial para el data plane HSM del firmante serial de Bray. La [PR #11](https://github.com/forgesworn/heartwood/pull/11) contiene el puente; la [PR #13](https://github.com/forgesworn/heartwood/pull/13) añade cobertura de frames y corrige el offset de `read_frame`; y la [PR #14](https://github.com/forgesworn/heartwood/pull/14) extrae el codec a la crate compartida `heartwood-frame`.

### SafeBox publica un informe de Fase 3 y una guía para jail de FreeBSD

[SafeBox](https://github.com/trbouma/safebox) es una bóveda privada portátil sobre Nostr que combina Nostr Wallet Connect [NIP-47](/es/topics/nip-47/), nAuth, nembed y transferencia de registros mediada por relays mediante QR y NFC. Un [informe de julio de 2026](https://github.com/trbouma/safebox/blob/main/docs/PROGRESS-REPORT-2026-07.md) publicado el día 6 marca la Fase 3 como prácticamente terminada: 49 commits desde abril, hasta 1.136 en total, y cuatro compromisos de ingeniería mayormente cumplidos. El siguiente paso es un piloto acotado; un proveedor de telecomunicaciones bajo NDA estudia un piloto de historiales médicos.

El trabajo concreto incluye colas para acciones NWC mutables que evitan carreras de proofs, protección de proofs tras melts Lightning fallidos, renovación proactiva de listeners NWC y callbacks LNURL con orígenes canónicos, JSON y CORS explícitos. El intercambio QR/NFC ganó un flujo unificado para modos presentados por receptor, remitente y entre dispositivos, con KEM y protección replay mediante Open Quantum Safe. El commit [`6866dae`](https://github.com/trbouma/safebox/commit/6866dae) añade una [guía de jail FreeBSD y build de liboqs](https://github.com/trbouma/safebox/blob/main/docs/devops/freebsd-jail-from-scratch.md) y una [especificación de appliance FreeBSD](https://github.com/trbouma/safebox/blob/main/docs/devops/SAFEBOX-FREEBSD-APPLIANCE-SPEC.md), con snapshots ZFS, aislamiento, servicios `rc.d`, proxy inverso y rollback en FreeBSD/ARM.

El informe anuncia además [OpenETR](https://github.com/trbouma/openetr), un spin-off que aplica control criptográfico y registros portátiles a conocimientos de embarque, recibos de almacén, pagarés y certificados electrónicos transferibles. El repositorio sumó 7 commits el 7 de julio: [`ea612a9`](https://github.com/trbouma/openetr/commit/ea612a9) separa attestation del registro; [`ca153a3`](https://github.com/trbouma/openetr/commit/ca153a3) trata mandato frente a efecto; y [`ba84b61`](https://github.com/trbouma/openetr/commit/ba84b61) compara formatos de credenciales verificables.

---

## Trabajo de protocolo y actualizaciones de NIPs

### Integrado: NIP-51 y NIP-37 alinean el nombre del kind 10013

La [PR #2404](https://github.com/nostr-protocol/nips/pull/2404) corrige solo la prosa. En [NIP-37](/es/topics/nip-37/), kind 10013 se llama `Relay List for Private Content`; en [NIP-51](/es/topics/nip-51/) bajo `Draft relays` tenía otro nombre. NIP-51 adopta ahora el de NIP-37. No cambia el wire ni los tags, pero evita ocultar que ambas especificaciones describen el mismo kind.

### Abierto: NIP-AD Nostr Web Addresses mediante consulta .well-known

La [PR #2406](https://github.com/nostr-protocol/nips/pull/2406) sucede a la cerrada #2393 con un borrador completo en [`AD.md`](https://github.com/nostr-protocol/nips/blob/2f4b09335c54a993d483bc220195e3f4a33df1ec/AD.md). NIP-AD define URLs web con contraparte Nostr opcional. Ante `https://golf.com/players`, un cliente pide `https://golf.com/.well-known/nostr.json?ad=/players`, que devuelve un objeto JSON que asigna rutas a pares `{filter, relays}`. El filtro es NIP-01 y la lista indica qué relays consultar. Con `"limit": 1` resuelve a un evento; sin él, a una lista. Un navegador sigue mostrando HTML en la misma ruta canónica. Los casos de uso incluyen nombres de grupos [NIP-29](/es/topics/nip-29/) que resuelven a kind 39000, búsquedas nsite [NIP-5A](/es/topics/nip-5a/), feeds con `{"ids": [...]}`, render nativo de URLs de eventos y blogs Nostr accesibles dentro y fuera del protocolo. El diseño permite que el resolver sea un archivo estático.

### Abierto: gestión de claims NIP-86 para códigos de invitación

La [PR #2408](https://github.com/nostr-protocol/nips/pull/2408) propone tres métodos para [NIP-86](/es/topics/nip-86/): `listclaims` (params `[]`, devuelve códigos [NIP-43](/es/topics/nip-43/)), `createclaim` (params `[claim]`, devuelve `true`) y `deleteclaim` (params `[claim]`, devuelve `true`). NIP-86 permite administrar usuarios y roles, pero no invitaciones. Un admin podría crear un código ligado a un rol, cobrar antes de crear la identidad, entregarlo y dejar que un bot escuche el evento claim kind 28935 para asignar automáticamente el rol. Todo el flujo quedaría dentro del RPC de gestión del relay.

### Abierto: color de rol como tupla (h, s, l)

La [PR #2402](https://github.com/nostr-protocol/nips/pull/2402) cambia el color de rol de [NIP-43](/es/topics/nip-43/) de un único `hue` a una tupla `hue`, `saturation` y `lightness`. Se admiten strings vacíos para que los clientes elijan valores coherentes; se recomienda indicar solo `hue` salvo colores específicos. En NIP-86, `createrole` y `editrole` reciben ahora `[id, label, description, [h, s, l], order]`. Con solo hue, distintos clientes escogían saturación y luminosidad diferentes y mostraban el mismo rol con intensidades distintas.

### Abierto: procedencia multimedia acreditada por hardware en NIP-80

La [PR #2409](https://github.com/nostr-protocol/nips/pull/2409) abre NIP-80, un formato de procedencia anclado al hardware de captura. La cámara firma cada foto y publica la prueba identificada por el contenido, de modo que sobrevive a la eliminación de metadatos, el realojamiento y las retiradas. Define kind 1080 para attestations de captura; 1081 para derivaciones como resize, crop, recompresión o redacción; 1082 para revocaciones; 11080 para anuncios de dispositivos; 31080 para endorsements; y 31081 para conjuntos de dispositivos anónimos, experimental. Reutiliza tags `x` NIP-94, `imeta` [NIP-92](/es/topics/nip-92/), descubrimiento [NIP-65](/es/topics/nip-65/), almacenamiento [Blossom](/es/topics/blossom/) y anclaje temporal opcional [NIP-03](https://github.com/nostr-protocol/nips/blob/master/03.md). Empareja una clave BIP-340 con ECDSA de hardware porque los secure elements habituales aún no generan BIP-340. La attestation no prueba que la escena sea real, sino que esa imagen procede de ese dispositivo aproximadamente a esa hora y solo sufrió cambios declarados. La especificación prohíbe reducir el resultado a una insignia "auténtico". El prototipo [OpenVeilCam](https://github.com/PrarthanaPurohit/OpenVeilCam), runtime Rust para Raspberry Pi con ATECC608, se actualiza para publicar estos kinds y verificarlos.

### Abierto: endurecimiento de la paginación NIP-01

La [PR #2407](https://github.com/nostr-protocol/nips/pull/2407) añade "Pagination & limits" a NIP-01. Un relay que imponga `limit` máximo DEBE fijarlo por encima del mayor número de eventos con un mismo `created_at`, evitando que un segundo llene la página. Los clientes que paginan hacia atrás DEBEN repetir con `until = oldest`, inclusive, y deduplicar por `id`; terminan cuando una ronda no aporta ids nuevos. Si toda la página comparte timestamp, DEBEN reintentar ese segundo con mayor `limit`. Si el relay lo recorta y sigue devolviendo un único segundo, DEBEN avanzar con `until = oldest - 1`, aceptando pérdidas, o abortar. La paginación normal NO DEBE indicar `limit`; elevarlo para vaciar un segundo atascado es la excepción. Esto evita omitir o reprocesar eventos con timestamps duplicados.

---

## Análisis en profundidad: NIP-13 (prueba de trabajo)

[NIP-13](/es/topics/nip-13/) define una prueba de trabajo para eventos Nostr. El spam es trivial en una red pública de relays: cualquiera genera un keypair e inunda un tema sin coste económico. NIP-13 permite imponer un coste computacional por evento que un spammer paga en conjunto, mientras un remitente normal lo paga una vez por mensaje. Relays y clientes pueden exigir o favorecer eventos con cierta dificultad.

### El mecanismo

El autor elige una dificultad en bits y mina el id del evento, el hash sha256 del evento serializado, hasta obtener al menos ese número de bits cero iniciales. Como el id incluye `created_at`, tags y contenido, hay que cambiar algo para recorrer el espacio de hashes. NIP-13 define el tag `nonce`:

```
["nonce", "<nonce_value>", "<target_bits>"]
```

`nonce_value` es cualquier string elegido por el minero; `target_bits` es la dificultad comprometida. El verificador cuenta los bits cero iniciales del id y los compara con `target_bits`. El tag formula una afirmación; el conteo real la confirma.

La cantidad de bits cero de una salida sha256 aleatoria sigue una distribución geométrica: cada bit duplica el trabajo esperado. 8 bits promedian 256 hashes, 20 bits cerca de un millón y 28 bits unos 268 millones. El objetivo de 8 bits de Bitchat tarda menos de un milisegundo. Los 21 bits de TAO y Wired rondan dos millones de hashes por post, rápidos en un portátil pero caros para una granja de bots. NIP-13 no impone dificultad; cada relay y cliente decide.

### Evento de ejemplo

Una nota kind 1 mínima minada con NIP-13 es:

```json
{
  "id": "000000000e9d97a1ab09fc381030b346cdd7a1a8a6f27c9c88f68c8b9d0f6c8a",
  "pubkey": "82341f882b6eabcd2ba7f1ef90aad961cf074af15b9ef44a09f9d2a8fbfbe6a2",
  "created_at": 1720368000,
  "kind": 1,
  "tags": [
    ["nonce", "72847", "28"]
  ],
  "content": "hello, this cost me 28 bits of PoW",
  "sig": "b1a5c9c74cff59f8a48e5c3b3d8e1c8e7e2c1d4a8e2b9f7d1c3e8b4f6a2c8d1e9f4b3c7a1d8e5b2f9c6a3d7e1b8f4c9a2d6e3b7f1c8a4d9e2b5f8c1a7d4e6b9f3c2"
}
```

El `id` comienza por siete ceros hexadecimales, 28 bits, igual que `target_bits`. El minero varió `nonce_value` hasta cumplir el objetivo. El verificador hashea el evento serializado, confirma los bits y verifica la firma. NIP-13 no añade campos, sino el tag y la restricción sobre el id.

### Dónde se utiliza

Bitchat 1.5.4 usa PoW de 8 bits en mensajes geohash kind 20000: mina antes de publicar y relaja el rate limit para eventos entrantes válidos. TAO y Wired usan 21 bits como umbral y muestran raíces con PoW reciente para ordenar el timeline. [cagliostr](https://github.com/mattn/algia) lo exige en el relay. NoStrudel ofrece minado en cliente. Damus y Amethyst calculan los bits al mostrar eventos. Coracle permite minar y filtrar. NDK y nostr-tools ofrecen helpers a bibliotecas.

La propiedad decisiva es que PoW no puede falsificarse: `target_bits` solo prueba algo si el id tiene esos ceros, y falsificarlo exige repetir el trabajo. Por eso Bitchat puede relajar límites sin confiar en el remitente. PoW tampoco compromete al minero con una pubkey o contenido concretos; un spammer aún puede minar 8 bits, pero paga un coste real. NIP-13 convierte el problema de spam de "imposible" en "cuantificable" y deja que cada cliente fije su precio.

---

## Análisis en profundidad: NIP-40 (timestamp de expiración)

[NIP-40](/es/topics/nip-40/) define un tag `expiration` que indica a relays y clientes que un evento debe considerarse caducado tras un timestamp Unix. Los eventos Nostr son por lo demás permanentes: incluso un borrado NIP-09 puede no retirar el original. NIP-40 deja al autor declarar al publicar que el evento tendrá vida corta y pide a relays y clientes dejar de servirlo o mostrarlo.

### El mecanismo

El autor añade un tag `expiration`:

```
["expiration", "<unix_timestamp>"]
```

El timestamp está en segundos Unix. Un relay PUEDE rechazar al ingerir eventos ya caducados, PUEDE dejar de servirlos y DEBERÍA respetar la expiración. Un cliente DEBERÍA ocultarlos. NIP-40 no obliga a borrar ni invalida la semántica de eventos protegidos NIP-70; es una indicación y un contrato blando.

El tag vive en el propio evento o, en mensajería envuelta, en el wrap externo. El evento sigue firmado y quien lo tenga puede leerlo. NIP-40 coordina la expectativa de que deje de aparecer tras el plazo, útil para posts efímeros, anuncios temporales, notas de eventos en vivo y DM NIP-17 que no deberían permanecer.

### Interacción con gift wrap

La [PR #1384](https://github.com/rust-nostr/nostr/pull/1384) de rust-nostr muestra cómo interactúa NIP-40 con gift wrap [NIP-59](/es/topics/nip-59/). NIP-59 define dos capas: un seal kind 13 firmado por la clave real del remitente y un gift wrap kind 1059 firmado por una clave efímera. Ambas usan `created_at` aleatorio hasta 48 horas anterior al envío real para ocultar el momento exacto. El seal debe tener tags vacíos.

Por eso `expiration` debe ir en el gift wrap, no en el seal, y anclarlo al envío real rompería la privacidad temporal: si el caller pasa un timestamp absoluto, un observador resta el TTL y recupera la hora real. rust-nostr recibe una `Duration` y calcula `expiration = wrap.created_at + duration` dentro de la biblioteca. Como `created_at` ya está aleatorizado, la expiración hereda esa aleatoriedad.

### Evento de ejemplo

Un ejemplo mínimo NIP-40 en una nota kind 1:

```json
{
  "id": "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b",
  "pubkey": "82341f882b6eabcd2ba7f1ef90aad961cf074af15b9ef44a09f9d2a8fbfbe6a2",
  "created_at": 1720368000,
  "kind": 1,
  "tags": [
    ["expiration", "1720454400"]
  ],
  "content": "this note expires in 24 hours",
  "sig": "d2e5b8a1c4f7b0d3e6a9c2f5b8d1e4a7c0f3b6d9e2a5c8f1b4d7e0a3c6f9b2d5e8a1c4f7b0d3e6a9c2f5b8d1e4a7c0f3b6d9e2a5c8f1b4d7e0a3c6f9b2d5e8a1"
}
```

`created_at` es la publicación; el tag indica dejar de servir el evento 86.400 segundos después. Un relay compatible deja de devolverlo en REQs tras `1720454400` y un cliente lo oculta.

### Dónde se utiliza

Los builders de rust-nostr (`GiftWrapBuilder`, `PrivateDirectMessageBuilder`) exponen expiración como `Duration`. NDK ofrece un helper para notas y DM. nostr-tools incluye `getExpiration` e `isExpired`. strfry, nostr-rs-relay, khatru y otros relays respetan NIP-40 al procesar REQ. Damus, Amethyst, noStrudel, Coracle y Primal filtran eventos caducados. Clientes en vivo como zap.stream usan NIP-40 en chats kind 1311 para que no persistan tras el stream.

NIP-40 encaja porque es opcional por evento y no exige despliegue coordinado. El autor puede añadirlo hoy; un relay que lo respeta mantiene un conjunto más limpio; uno que lo ignora no empeora; y un cliente compatible cumple la voluntad del autor. El cambio de rust-nostr recalca que la ubicación importa tanto como la presencia: en un gift wrap NIP-59, el tag va en la capa cuyo timestamp ya está aleatorizado y la API impide filtrar accidentalmente el momento real.

---

Esto es todo por esta semana. ¿Estáis construyendo algo o tenéis noticias que compartir? Contactad por DM NIP-17 o encontradnos en Nostr.
