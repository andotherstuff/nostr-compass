---
title: 'Nostr Compass #17'
date: 2026-04-08
translationOf: /en/newsletters/2026-04-08-newsletter.md
translationDate: 2026-04-09
draft: false
type: newsletters
---

Bienvenido de nuevo a Nostr Compass, tu guía semanal de Nostr.

**Esta semana:** [Amethyst](https://github.com/vitorpamplona/amethyst) lanza [v1.08.0](#amethyst-lanza-arti-tor-y-fusiona-mls-y-marmot-puros-en-kotlin) con integración de Arti Tor y una UI de Shorts rediseñada, mientras fusiona implementaciones puras en Kotlin de [MLS](/es/topics/mls/) y [Marmot](/es/topics/marmot/) en su librería [Quartz](/es/topics/quartz/). [Nostur](https://github.com/nostur-com/nostur-ios-public) lanza [v1.27.0](#nostur-v1270-añade-grabación-de-vídeo-y-respuestas-privadas) con grabación de vídeo, perfiles con GIF animados y respuestas privadas. [Shosho](https://github.com/r0d8lsh0p/shosho-releases) lanza [v0.15.0](#shosho-v0150-lanza-shows-y-carrusel-vertical-de-vídeo) con Shows (información personalizada de live stream conectada a OBS) y un carrusel vertical de vídeo al estilo TikTok. [Nymchat](https://github.com/Spl0itable/NYM) [revierte Marmot y lanza chats grupales NIP-17 mejorados](#nymchat-revierte-marmot-y-lanza-chats-grupales-nip-17-mejorados) con claves efímeras rotativas. [Nostr VPN](https://github.com/mmalmi/nostr-vpn) lanza [soporte de exit node y empaquetado para Umbrel](#nostr-vpn-lanza-soporte-de-exit-node-y-empaquetado-para-umbrel) a lo largo de seis releases. [Amber](https://github.com/greenart7c3/Amber) salta a [v6.0.0-pre1](#amber-v600-pre1-añade-claves-de-firma-nip-46-por-conexión) con claves de firma [NIP-46](/es/topics/nip-46/) por conexión y actualizaciones dentro de la app mediante Zapstore. [Notedeck](https://github.com/damus-io/notedeck) alcanza [v0.10.0-beta](#notedeck-v0100-beta-lanza-autoactualización-con-zapstore) con autoactualización de APK vía Zapstore, y [NIP-58](/es/topics/nip-58/) (Badges) recibe una [migración de kind](#actualizaciones-de-nips). Dos análisis en profundidad de NIP cubren [NIP-17](/es/topics/nip-17/) (Private Direct Messages) y [NIP-46](/es/topics/nip-46/) (Nostr Remote Signing).

## Noticias principales

### Amethyst lanza Arti Tor y fusiona MLS y Marmot puros en Kotlin

[Amethyst](https://github.com/vitorpamplona/amethyst), el cliente Android mantenido por vitorpamplona, lanzó cuatro releases desde [v1.07.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.3) hasta [v1.08.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.08.0) y fusionó un gran lote de trabajo aún no publicado en su librería [Quartz](/es/topics/quartz/) (el módulo Nostr compartido de Kotlin Multiplatform). El release principal es v1.08.0 "Arti Tor", que migra la conectividad Tor de la app desde la librería Tor basada en C a [Arti](https://gitlab.torproject.org/tpo/core/arti), la implementación en Rust del Tor Project. La migración aborda crashes aleatorios que ocurrían con los bindings anteriores de C Tor. Arti es el reemplazo a largo plazo del Tor Project para la base de código en C, escrito desde cero en Rust para seguridad de memoria y async I/O.

El release v1.07.3 rediseñó la UI de Shorts, reemplazando el diseño paginado por feeds de borde a borde para imágenes, shorts y vídeos largos. El mismo release migró badges a kind `10008` y bookmarks a kind `10003`, alineándose con la migración de kind de [NIP-58](/es/topics/nip-58/) [fusionada esta semana](#actualizaciones-de-nips). v1.07.4 corrigió un problema en el manejo de secretos de Nostr Wallet Connect, y v1.07.5 corrigió un crash en la subida de imágenes.

En main, pero todavía no en un release etiquetado, el equipo escribió una implementación completa en Kotlin tanto de [MLS](/es/topics/mls/) como del protocolo [Marmot](/es/topics/marmot/), reemplazando la necesidad de bindings nativos de bibliotecas C/Rust. [PR #2147](https://github.com/vitorpamplona/amethyst/pull/2147) añade la capa central de mensajería grupal Marmot MLS, [PR #2149](https://github.com/vitorpamplona/amethyst/pull/2149) añade la UI de chat grupal, [PR #2146](https://github.com/vitorpamplona/amethyst/pull/2146) añade procesadores de mensajes entrantes y salientes con un gestor de suscripciones, [PR #2141](https://github.com/vitorpamplona/amethyst/pull/2141) añade persistencia del estado de grupos MLS y gestión de rotación de KeyPackage, [PR #2150](https://github.com/vitorpamplona/amethyst/pull/2150) añade una suite completa de tests de MLS con firma de GroupInfo mejorada, y [PR #2158](https://github.com/vitorpamplona/amethyst/pull/2158) añade seguimiento del estado de publicación de KeyPackage. [PR #2166](https://github.com/vitorpamplona/amethyst/pull/2166) añade una implementación pura en Kotlin de secp256k1 para operaciones criptográficas de Nostr, reemplazando la dependencia de la biblioteca nativa en C. Combinado con la implementación MLS en Kotlin, [Quartz](/es/topics/quartz/) puede ejecutar firma Nostr y mensajería grupal Marmot sin ningún binding nativo, lo que abre la puerta a objetivos de Kotlin Multiplatform, incluyendo iOS.

El equipo también está construyendo soporte para [NIP-AC](/en/topics/nip-ac/) (P2P Voice and Video Calls): [PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143) añade una suite completa de tests para la máquina de estados de llamadas NIP-AC, y [PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164) evita que ofertas de llamada obsoletas se disparen de nuevo después de reiniciar la app.

### Nostur v1.27.0 añade grabación de vídeo y respuestas privadas

[Nostur](https://github.com/nostur-com/nostur-ios-public), el cliente Nostr para iOS, lanzó [v1.27.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/v1.27.0) el 2 de abril. El release añade grabación de vídeo dentro de la app con recorte antes de subir, de modo que los usuarios puedan capturar clips cortos, ajustarlos a la duración deseada y publicarlos sin salir del cliente. El soporte para GIF animados se extiende a fotos de perfil y banner, y también se añadió renderizado de WebP animado. Una nueva integración con Shortcuts permite a los usuarios enviar publicaciones de Nostr desde automatizaciones de Apple Shortcuts. El release también añade respuestas privadas y corrige problemas de compatibilidad de DMs que afectaban la entrega de mensajes entre Nostur y otros clientes.

### Shosho v0.15.0 lanza Shows y carrusel vertical de vídeo

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), la app de live streaming sobre Nostr, lanzó [v0.15.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.0) y [v0.15.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.1) el 7 de abril. La función principal es Shows: los streamers pueden configurar información personalizada del show antes de salir en vivo y conectar su show a OBS o a cualquier codificador externo. Esto separa los metadatos de "qué estoy transmitiendo" del acto de entrar en directo, de modo que los streamers puedan preparar títulos, descripciones y productos antes de empezar a emitir. El mismo release añade un carrusel vertical de vídeo al estilo TikTok para deslizar entre lives, clips y replays en un feed a pantalla completa, y Quick Add para publicar clips de vídeo y añadir productos directamente desde una página de perfil. v0.15.1 corrige un bug por el que el teclado ocultaba el campo de entrada del chat del live stream.

## Lanzamientos de esta semana

### Notedeck v0.10.0-beta lanza autoactualización con Zapstore

[Notedeck](https://github.com/damus-io/notedeck), el cliente de escritorio y móvil del equipo Damus, lanzó [v0.10.0-beta.1](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.1) y [v0.10.0-beta.2](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.2) como prereleases de prueba para autoactualización de APK. [PR #1417](https://github.com/damus-io/notedeck/pull/1417) añade autoactualización de APK a través del actualizador Nostr/Zapstore en Android, construyendo sobre el [trabajo de descubrimiento de actualizaciones nativo de Nostr cubierto en Newsletter #14](/en/newsletters/2026-03-18-newsletter/#notedeck-moves-release-discovery-onto-nostr). El flujo de actualización descubre nuevos releases a través de eventos Nostr publicados en relays, luego descarga el APK desde donde el desarrollador lo aloje (GitHub releases, Blossom CDN u otras fuentes), verifica el hash SHA-256 contra el evento Nostr firmado y lo instala. [PR #1438](https://github.com/damus-io/notedeck/pull/1438) corrige un bug en la pantalla de bienvenida donde los botones Login y CreateAccount volvían inmediatamente hacia atrás, y [PR #1424](https://github.com/damus-io/notedeck/pull/1424) corrige desbordamiento de texto en la vista de sesión de Agentium AI.

### Amber v6.0.0-pre1 añade claves de firma NIP-46 por conexión

[Amber](https://github.com/greenart7c3/Amber), la app firmante [NIP-55](/es/topics/nip-55/) (Android Signer Application), lanzó [v6.0.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.0-pre1) el 4 de abril. El cambio más importante son las claves de firma por conexión para el protocolo bunker [NIP-46](/es/topics/nip-46/) (Nostr Remote Signing). En lugar de usar un único keypair para todas las conexiones bunker, Amber ahora genera una clave distinta para cada cliente conectado. Si una conexión de cliente se ve comprometida, el atacante no puede suplantar al firmante frente a otros clientes.

[PR #377](https://github.com/greenart7c3/Amber/pull/377) añade comprobación e instalación de actualizaciones dentro de la app vía Zapstore, uniéndose a [Notedeck](#notedeck-v0100-beta-lanza-autoactualización-con-zapstore) en la adopción de distribución de apps nativa de Nostr. [PR #375](https://github.com/greenart7c3/Amber/pull/375) maneja los fallos de AndroidKeyStore de forma elegante mostrando una advertencia a los usuarios en lugar de crashear, y [PR #371](https://github.com/greenart7c3/Amber/pull/371) añade limpieza de base de datos con límites de tamaño y truncado de contenido para evitar crecimiento ilimitado del almacenamiento. El prerelease también incluye la whitelist de auth de relay [NIP-42](/es/topics/nip-42/) y el login con frase mnemónica de recuperación del [ciclo v5.0.x cubierto la semana pasada](/en/newsletters/2026-04-01-newsletter/#amber-v502-through-v504).

### Nostria lanza app móvil nativa

[Nostria](https://github.com/nostria-app/nostria), el cliente Nostr multiplataforma mantenido por SondreB, lanzó una app móvil nativa para Android con ocho releases desde [v3.1.11](https://github.com/nostria-app/nostria/releases/tag/v3.1.11) hasta [v3.1.18](https://github.com/nostria-app/nostria/releases/tag/v3.1.18). La capacidad nueva más importante es el soporte nativo de firmante local para firmantes como [Amber](https://github.com/greenart7c3/Amber) y Aegis. También hay [instaladores de escritorio](https://www.nostria.app/download) para Linux, macOS y Windows. [PR #610](https://github.com/nostria-app/nostria/pull/610) reduce la presión de memoria del feed con límites adaptativos de runtime y limpieza de URLs de preview. v3.1.14 corrige la integración con Brainstorm, un proveedor de [Web of Trust](/es/topics/web-of-trust/). v3.1.15 se centra en mejoras de música. La nueva app Android está disponible en [Zapstore](https://zapstore.dev/apps/app.nostria).

### diVine 1.0.8 lanza subidas reanudables y DMs

[diVine](https://github.com/divinevideo/divine-mobile), el cliente de vídeo de formato corto, lanzó [1.0.8](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.8) con 87 PRs fusionados. Las subidas reanudables permiten a los creadores retomar subidas interrumpidas bloque por bloque en lugar de reiniciar desde cero en una conexión inestable. El release añade ajustes de calidad y bitrate de vídeo, doble toque para dar like y mejoras en DMs. [PR #2722](https://github.com/divinevideo/divine-mobile/pull/2722) añade un plugin de cámara para macOS para captura de vídeo de escritorio, y [PR #2820](https://github.com/divinevideo/divine-mobile/pull/2820) migra el sistema de notificaciones a una arquitectura BLoC con enriquecimiento y agrupación. El equipo también reemplazó stickers y arte de categorías generados por AI con SVGs de OpenMoji ([PR #2844](https://github.com/divinevideo/divine-mobile/pull/2844), [PR #2842](https://github.com/divinevideo/divine-mobile/pull/2842)).

### Manent v1.3.0 añade difuminado de notas sensibles y auth NIP-42

[Manent](https://github.com/dtonon/manent), la app privada de notas cifradas y almacenamiento de archivos, lanzó [v1.3.0](https://github.com/dtonon/manent/releases/tag/v1.3.0) el 2 de abril. Los usuarios ahora pueden marcar notas como sensibles para difuminarlas en la vista de lista, manteniendo el contenido privado oculto durante el desplazamiento casual. El release también añade soporte para [NIP-42](/es/topics/nip-42/) (Authentication of Clients to Relays), permitiendo a Manent autenticarse en relays que lo exigen antes de aceptar eventos. Manent almacena todos los datos cifrados en relays Nostr usando el keypair del usuario, así que el soporte NIP-42 amplía el conjunto de relays que puede usar para almacenamiento.

### Wisp v0.17.0 a v0.17.3 añaden zaps en live streams y backup de billetera

[Wisp](https://github.com/barrydeen/wisp), el cliente Nostr para Android, lanzó seis releases desde [v0.16.2-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.2-beta) hasta [v0.17.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.17.3-beta) con 44 PRs fusionados. El release v0.17.0 añade avisos de seguridad para backup de billetera y mejoras de UX para zaps. [v0.17.1](https://github.com/barrydeen/wisp/releases/tag/v0.17.1-beta) añade visibilidad del chat de live stream entre plataformas y funcionalidad de zaps en live streams. [PR #423](https://github.com/barrydeen/wisp/pull/423) añade auto-búsqueda de perfiles, una animación de zap exitoso y mejoras en el estado de usuario. [PR #426](https://github.com/barrydeen/wisp/pull/426) corrige un crash por falta de memoria en `computeId` para eventos con listas grandes de tags. Los releases v0.16.x añadieron autocompletado de shortcode de emoji, mejoras de UI para chats grupales y filtrado de usuarios bloqueados en todas las rutas de notificaciones.

### Mostro lanza deep links, tipos de cambio de Nostr y una corrección de pagos duplicados

[Mostro](https://github.com/MostroP2P/mostro), el exchange peer-to-peer de Bitcoin construido sobre Nostr, recibió actualizaciones tanto en su daemon de servidor como en su cliente móvil esta semana. Del lado del servidor, [PR #692](https://github.com/MostroP2P/mostro/pull/692) evita que escrituras obsoletas de órdenes provoquen pagos duplicados, un bug que podía hacer que un vendedor recibiera el pago dos veces por la misma operación. [PR #693](https://github.com/MostroP2P/mostro/pull/693) usa actualizaciones dirigidas para escrituras de dev_fee en lugar de sobrescribir la orden completa.

[Mostro Mobile](https://github.com/MostroP2P/mobile), el cliente Flutter, lanzó [v1.2.3](https://github.com/MostroP2P/mobile/releases/tag/v1.2.3) el 3 de abril. El release maneja deep links de distintas instancias de Mostro, de modo que los usuarios puedan tocar enlaces que enruten al servidor de exchange correcto. [PR #498](https://github.com/MostroP2P/mobile/pull/498) detecta DMs de admin y disputa en el pipeline de notificaciones en segundo plano, y la app ahora obtiene tipos de cambio desde Nostr con fallback HTTP/cache. [PR #560](https://github.com/MostroP2P/mobile/pull/560) corrige un bug de bloqueo en la conexión al relay que impedía a la app alcanzar relays bajo ciertas condiciones de red.

### Unfiltered v1.0.12 añade hashtags y comentarios

[Unfiltered](https://github.com/dmcarrington/unfiltered), un cliente Nostr enfocado en contenido visual, lanzó [v1.0.12](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.12). [PR #69](https://github.com/dmcarrington/unfiltered/pull/69) añade soporte para hashtags y [PR #72](https://github.com/dmcarrington/unfiltered/pull/72) añade la capacidad de escribir y mostrar comentarios en publicaciones. [PR #71](https://github.com/dmcarrington/unfiltered/pull/71) corrige problemas de navegación con múltiples imágenes por publicación.

### Primal Android lanza uso compartido de billetera entre múltiples cuentas y auto-reconexión del firmante remoto

[Primal](https://github.com/PrimalHQ/primal-android-app), el cliente Nostr para Android, lanzó un release el 7 de abril. La actualización añade uso compartido de billetera entre múltiples cuentas y un menú overflow con eliminación de billetera en Dev Tools. El firmante remoto ahora se reconecta automáticamente cuando cae la conexión, y el servicio de billetera recibió su propia lógica de auto-reconexión. Entre las correcciones están que los votos zap de encuestas ya no aparecen como Top Zaps, la prevención de crashes por opciones vacías en encuestas, el ocultamiento del balance de billetera cuando no existe ninguna y el mapeo de tipos WalletException a códigos de error en respuestas NWC.

### Titan v0.1.0 lanza navegador nativo nsite:// con registro de nombres en Bitcoin

[Titan](https://github.com/btcjt/titan), un navegador nativo de escritorio para la web de Nostr, lanzó [v0.1.0](https://github.com/btcjt/titan/releases/tag/v0.1.0) el 7 de abril. Titan resuelve URLs `nsite://` buscando nombres legibles por humanos registrados en Bitcoin, consultando relays Nostr para los eventos de contenido del sitio y renderizando páginas obtenidas desde servidores [Blossom](/es/topics/blossom/). El resultado es una experiencia de navegación web sin DNS, sin certificados TLS y sin proveedores de hosting. Los nombres se registran a través de una [interfaz web](https://npub1hmq6xuqnplk5lw0h3700cujmx5gymqn5wrn42u6432r6ntzumezqc3marw.nsite.lol/register) vinculada a transacciones de Bitcoin. El release inicial se distribuye como `.dmg` de macOS (ARM, con soporte Rosetta 2 para Intel) e incluye soporte para entorno de desarrollo Nix.

### Bikel v1.5.0 lanza servicio nativo en primer plano para teléfonos de-Googled

[Bikel](https://github.com/Mnpezz/bikel), un tracker de ciclismo descentralizado que convierte recorridos en datos de infraestructura pública usando Nostr, lanzó [v1.5.0](https://github.com/Mnpezz/bikel/releases/tag/v1.5.0) el 4 de abril. El release migra desde Expo TaskManager dependiente de GMS a un servicio nativo personalizado en primer plano, asegurando seguimiento confiable de recorridos en segundo plano en LineageOS, GrapheneOS y otras variantes Android de-Googled. El Bikel Bot ganó una arquitectura de doble bolsillo con recolección autónoma de eCash mediante Cashu nutzaps. v1.4.3 y v1.4.2 corrigen la sincronización del tracking en segundo plano para entornos Android no estándar, y la app añade toggles para puntos de mapa de aparcabicis OSM.

### Sprout añade soporte para NIP-01, NIP-23 y NIP-33

[Sprout](https://github.com/block/sprout), una plataforma de comunicación de Block con relay Nostr integrado, lanzó [desktop/v0.1.0-rc7](https://github.com/block/sprout/releases/tag/desktop/v0.1.0-rc7) el 6 de abril. Esta semana el equipo añadió soporte para artículos kind `30023` de [NIP-23](/en/topics/nip-23/) (Long-form Content), eventos reemplazables parametrizados de [NIP-33](/en/topics/nip-33/) con reemplazo claveado por tag `d`, y notas de texto kind `1` y listas de follows kind `3` de [NIP-01](/es/topics/nip-01/)/[NIP-02](/en/topics/nip-02/). El release también añade un sistema adaptativo de temas IDE con 54 temas, mejoras de UX para historial de workflows y ejecuciones de agentes, y una limpieza de la barra lateral de miembros.

### mesh-llm v0.56.0 lanza protocolo de configuración distribuida

[mesh-llm](https://github.com/michaelneale/mesh-llm), un sistema distribuido de inferencia LLM que usa keypairs Nostr para identidad de nodo, lanzó [v0.56.0](https://github.com/michaelneale/mesh-llm/releases/tag/v0.56.0) el 7 de abril. El release añade un protocolo de configuración distribuida con semántica de ownership, cuantización asimétrica de KV cache (claves Q8_0 con valores Q4) para reducir el uso de memoria, almacenamiento en keychain del sistema para keystores de identidad, streaming fluido de chat con cola de mensajes, y correcciones para el layout fullscreen y el particionado de KV cache con flash attention.

### Nostr VPN lanza soporte de exit node y empaquetado para Umbrel

[Nostr VPN](https://github.com/mmalmi/nostr-vpn), una VPN peer-to-peer que usa relays Nostr para señalización y WireGuard para túneles cifrados, lanzó seis releases desde [v0.3.0](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.0) hasta [v0.3.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.6) esta semana. El ciclo v0.3.x añade soporte de exit node en Windows y macOS, permitiendo que peers enruten tráfico de internet a través de otros nodos de la red. La propagación de invites y aliases ahora se sincroniza sobre Nostr, así que los usuarios pueden compartir acceso a la red sin coordinación fuera de banda. Los releases añaden empaquetado para Umbrel en despliegues autoalojados, NAT punch-through usando endpoints públicos recordados, limpieza automática de exit nodes obsoletos y una especificación de protocolo publicada. El proyecto también estabilizó el manejo de rutas en macOS con default routes autorreparables y reparación de underlay, y añadió una build Android vía Tauri. Hay builds disponibles para macOS (Apple Silicon e Intel), Linux (AppImage y .deb), Windows y Android.

### Nymchat revierte Marmot y lanza chats grupales NIP-17 mejorados

[Nymchat](https://github.com/Spl0itable/NYM), el cliente de chat con capacidad MLS, lanzó 14 releases desde [v3.56.261](https://github.com/Spl0itable/NYM/releases/tag/3.56.261) hasta [v3.58.274](https://github.com/Spl0itable/NYM/releases/tag/v3.58.274). El cambio más significativo es un giro de protocolo: [v3.57.261](https://github.com/Spl0itable/NYM/releases/tag/v3.57.261) añadió chats grupales Marmot MLS, pero [v3.58.268](https://github.com/Spl0itable/NYM/releases/tag/v3.58.268) revirtió a [NIP-17](/es/topics/nip-17/) porque el soporte multidispositivo de Marmot aún no está terminado, lo que causaba problemas con la sincronización del estado del chat grupal entre dispositivos. v3.58.271 introduce chats grupales NIP-17 mejorados con claves efímeras rotativas para todos los mensajes, diseñadas para prevenir ataques de timing y correlación. La semana también trajo un sistema de amigos con control granular de ajustes ([v3.58.262](https://github.com/Spl0itable/NYM/releases/tag/v3.58.262)), sincronización de mensajes de chat grupal MLS en ajustes cifrados de la app, y múltiples correcciones de conectividad con relays.

### nak v0.19.5 añade Blossom multi-servidor y publicación outbox

[nak](https://github.com/fiatjaf/nak), el toolkit de línea de comandos Nostr de fiatjaf, lanzó [v0.19.5](https://github.com/fiatjaf/nak/releases/tag/v0.19.5). El comando `blossom` ahora acepta múltiples flags `--server` para subir a varios servidores [Blossom](/es/topics/blossom/) en una sola llamada. Un nuevo comando `key` amplía claves parciales rellenando con ceros por la izquierda. El comando `event` gana un flag `--outbox` para publicar eventos a través del modelo outbox, y `fetch` ahora sale con código de error cuando no se devuelve ningún evento.

## En desarrollo

### White Noise añade previews con thumbhash y puente de registro push

[White Noise](https://github.com/marmot-protocol/whitenoise), el mensajero privado construido sobre el protocolo [Marmot](/es/topics/marmot/), fusionó cinco PRs. [PR #549](https://github.com/marmot-protocol/whitenoise/pull/549) reemplaza previews de imagen con blurhash por thumbhash, un algoritmo más nuevo que produce imágenes placeholder más nítidas con un payload más pequeño (normalmente menos de 30 bytes frente a los ~50-100 bytes de blurhash) mientras preserva la proporción y distribución de color de la imagen original. Blurhash se mantiene como fallback para contenido antiguo. [PR #548](https://github.com/marmot-protocol/whitenoise/pull/548) actualiza whitenoise-rs y añade el puente de registro push [MIP-05](/es/topics/mip-05/), conectando el [trabajo de especificación de notificaciones push de la semana pasada](/en/newsletters/2026-04-01-newsletter/#marmot-moves-keypackages-to-addressable-events-and-tightens-push-notifications) con el cliente. [PR #493](https://github.com/marmot-protocol/whitenoise/pull/493) añade paginación basada en cursor para mensajes de chat, reemplazando la estrategia anterior de carga por un enfoque guiado por scroll.

### Route96 añade configuración dinámica de etiquetas y limpieza de zero-egress

[Route96](https://github.com/v0l/route96), el servidor de medios [Blossom](/es/topics/blossom/) de v0l, fusionó tres PRs. [PR #80](https://github.com/v0l/route96/pull/80) añade configuración dinámica del modelo de etiquetas vía la API de admin, permitiendo a los operadores cambiar modelos de clasificación de contenido sin reiniciar el servidor. [PR #82](https://github.com/v0l/route96/pull/82) añade campos de configuración de etiquetas a la UI de admin. [PR #79](https://github.com/v0l/route96/pull/79) añade una política de limpieza de archivos zero-egress que elimina automáticamente archivos que nunca se han descargado, manteniendo bajos los costes de almacenamiento para los operadores.

### Snort lanza endurecimiento de seguridad e invoices de pago para DVM

[Snort](https://github.com/v0l/snort), el cliente web, lanzó dos releases esta semana con una auditoría de seguridad integral. Las correcciones incluyen verificación de firma Schnorr, protección frente a falsificación de mensajes de relay [NIP-46](/es/topics/nip-46/) (evitando que atacantes inyecten solicitudes de firma a través de relays comprometidos), mejoras en cifrado de PIN y eliminación de la confianza en delegación NIP-26. Las ganancias de rendimiento vienen de verificación Schnorr por lotes en WASM, rutas con lazy loading, traducciones precompiladas y eliminación de verificación doble por evento. [PR #618](https://github.com/v0l/snort/pull/618) añade la visualización de invoice requerido por pago para kind `7000` de [NIP-90](/en/topics/nip-90/) (Data Vending Machine), de modo que cuando un DVM responde con un requisito de pago, Snort renderiza el invoice Lightning directamente en el feed.

### Damus mejora la compactación de LMDB

[Damus](https://github.com/damus-io/damus), el cliente iOS, fusionó [PR #3719](https://github.com/damus-io/damus/pull/3719) que añade compactación automática programada de LMDB, evitando que la base de datos local crezca sin límite con el tiempo. [PR #3663](https://github.com/damus-io/damus/pull/3663) mejora BlurOverlayView para que parezca protector en lugar de roto.

### Captain's Log añade indexación de tags y sincronización de notas

[Captain's Log](https://github.com/nodetec/captains-log) (Comet), la herramienta de escritura long-form nativa de Nostr de Nodetec, fusionó cuatro PRs esta semana. [PR #156](https://github.com/nodetec/captains-log/pull/156) añade indexación de tags y soporte de sincronización entre notas, [PR #157](https://github.com/nodetec/captains-log/pull/157) refactoriza la sincronización de notas y el manejo de tags, y [PR #159](https://github.com/nodetec/captains-log/pull/159) corrige la sincronización de notas enviadas a la papelera para que las notas eliminadas permanezcan eliminadas entre dispositivos.

### Relatr v0.2.x rediseña su sistema de plugins con marketplace nativo de Nostr para validadores

[Relatr](https://github.com/ContextVM/relatr), un motor de puntuación de [Web of Trust](/es/topics/web-of-trust/) que calcula rankings de confianza a partir de la distancia en el grafo social y validadores configurables, lanzó la familia v0.2.x con un rediseño completo del sistema de plugins. Los validadores ahora se escriben en Elo, un lenguaje portable de expresiones funcionales bifurcado para soportar capacidades de múltiples pasos orquestadas por el host (consultas Nostr, búsquedas en el grafo social, resolución NIP-05). Los plugins se publican como eventos Nostr kind `765`, haciendo que la distribución sea nativa de la red de relays. Un nuevo [plugin marketplace](https://relatr.net) permite a operadores descubrir, instalar y ponderar validadores desde el navegador, con un CLI (`relo`) para autoría y publicación local. La arquitectura está aislada: los plugins solo pueden invocar capacidades que el host proporcione explícitamente, así que un validador malicioso no puede escapar de su ámbito definido. Las instancias de Relatr ahora pueden gestionarse desde el sitio web, con visibilidad completa de qué plugins componen el algoritmo de puntuación y sus pesos individuales.

### Shopstr mejora la navegación móvil y el control de acceso

[Shopstr](https://github.com/shopstr-eng/shopstr), el marketplace nativo de Nostr para comprar y vender con Bitcoin, empujó 158 commits en su app principal y el proyecto complementario [Milk Market](https://github.com/shopstr-eng/milk-market) esta semana. Las correcciones incluyen mejoras en el layout de comunidades en móvil, comportamiento de cerrar menú al navegar y autocierre de dropdowns. Las rutas protegidas ya no pueden abrirse vía URL directa sin iniciar sesión, y la lógica de coincidencia de slugs ahora maneja correctamente múltiples coincidencias exactas.

### Pollerama añade notificaciones, búsqueda de películas y UI de valoración

[Pollerama](https://github.com/formstr-hq/nostr-polls), una app de encuestas, sondeos y ratings sociales construida sobre Nostr, añadió notificaciones de hilos, una función de búsqueda de películas y una revisión de la UI de valoración. El release también corrige problemas de carga del feed y actualiza versiones de dependencias.

### Purser construye daemon de pagos nativo de Nostr con cifrado Marmot

[Purser](https://github.com/EthnTuttle/purser), un daemon de pagos nativo de Nostr diseñado como reemplazo de Zaprite, fusionó nueve PRs esta semana construyendo su arquitectura central. El proyecto usa MLS de [Marmot](/es/topics/marmot/) vía MDK para mensajería cifrada entre comerciante y cliente, con Strike y Square como proveedores de pagos. Esta semana aterrizaron carga de config y catálogo, validación de esquema de mensajes, la capa de comunicación MDK, implementaciones de proveedores Strike y Square, un motor de polling, limitación anti-spam, persistencia de pagos pendientes y el pipeline de procesamiento de órdenes. Los 99 tests ahora ejercitan operaciones MLS reales de mdk-core después de que el equipo eliminara mock MLS en favor de cifrado real en modo local.

### Vector refactoriza adjuntos de DMs y añade edición de perfil

[Vector](https://github.com/VectorPrivacy/Vector), el mensajero Nostr centrado en privacidad construido con Tauri, fusionó [PR #55](https://github.com/VectorPrivacy/Vector/pull/55) refactorizando el frontend. El descifrado y guardado de adjuntos de DM se movió a la librería vector-core, y la app ahora soporta edición de perfil. La flag de cancelación de subida quedó correctamente conectada a través de TauriSendCallback, y se limpiaron callbacks de preview de adjuntos sin uso.

## Trabajo de protocolo y especificación

### Actualizaciones de NIPs

Cambios recientes en el [repositorio de NIPs](https://github.com/nostr-protocol/nips):

**Fusionados:**

- **[NIP-58](/es/topics/nip-58/) (Badges): Profile Badges pasan a kind 10008, Badge Sets a kind 30008** ([PR #2276](https://github.com/nostr-protocol/nips/pull/2276)): Migra Profile Badges desde kind `30008` a kind `10008` (un evento reemplazable, uno por pubkey) e introduce kind `30008` para Badge Sets. Antes, Profile Badges usaba el mismo kind (`30008`) que las definiciones de Badge, lo que los convertía en eventos reemplazables parametrizados claveados por un tag `d`. El nuevo kind `10008` es un evento reemplazable simple: uno por pubkey, sin necesidad de tag `d`. Los clientes consultan un único evento reemplazable por usuario en lugar de escanear eventos reemplazables parametrizados. Amethyst v1.07.3 ya distribuye esta migración.

- **[NIP-34](/es/topics/nip-34/) (Git Stuff): Añadir listas de follows relacionadas con git** ([PR #2130](https://github.com/nostr-protocol/nips/pull/2130)): Añade convenciones de listas de follows para seguimiento de repositorios y issues de NIP-34. Los usuarios publican follow sets kind `30000` con tags `d` como `git-repos` o `git-issues` que contienen referencias de tag `a` a repositorios (kind `30617`) que quieren seguir. Los clientes pueden suscribirse a estos follow sets para mostrar actividad de repositorios en el feed de un usuario, de forma similar a como funcionan las listas de contactos kind `3` para pubkeys.

**PRs abiertos y discusiones:**

- **NIP-AC: P2P Voice and Video Calls over WebRTC** ([PR #2301](https://github.com/nostr-protocol/nips/pull/2301)): Amplía el NIP-100 original (implementado por 0xChat) con tres cambios: migración a cifrado [NIP-44](/es/topics/nip-44/) envuelto en gift wraps [NIP-59](/es/topics/nip-59/) para eliminar fugas de metadatos, un flujo WebRTC especificado para la configuración de llamadas de voz y vídeo (offer, answer, candidatos ICE), y un modelo mesh de llamadas grupales donde cada peer establece una conexión WebRTC directa con todos los demás peers. La especificación no es retrocompatible con NIP-100. Amethyst ya está construyendo contra ella, con una suite de tests para la máquina de estados de llamadas ([PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143)) y manejo de ofertas de llamada obsoletas ([PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164)) aterrizando esta semana.

- **[NIP-340](/en/topics/nip-340/) (FROST Quorum)** ([PR #2299](https://github.com/nostr-protocol/nips/pull/2299)): Propone convenciones para firma threshold de [FROST](/es/topics/frost/) (Flexible Round-Optimized Schnorr Threshold) en Nostr. FROST permite que un grupo de firmantes controle colectivamente una identidad Nostr donde cualquier subconjunto t-de-n puede firmar eventos sin reconstruir la clave privada completa. El NIP define cómo coordinar rondas de firma, distribuir key shares y publicar eventos firmados de forma threshold, construyendo sobre el trabajo del firmante Igloo del [proyecto FROSTR](/en/newsletters/2026-04-01-newsletter/#igloo-signer-11).

- **[NIP-5D](/en/topics/nip-5d/) (Nostr Web Applets)** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): Define un protocolo `postMessage` para aplicaciones web aisladas ("napplets") que corren en iframes y se comunican con una aplicación anfitriona ("shell"). El shell proporciona a la napplet firma Nostr, acceso a relay y contexto de usuario mediante una API estructurada de mensajes, mientras el sandbox del iframe evita acceso directo a claves. Esto extiende el modelo de hosting de sitios web estáticos de [NIP-5A](/en/topics/nip-5a/) hacia aplicaciones interactivas que pueden leer y escribir eventos Nostr. El NIP está en desarrollo activo con una implementación de runtime funcional.

- **[NIP-5C](/en/topics/nip-5c/) (Scrolls)** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): Renombrado desde la propuesta anterior NIP-A5. Define convenciones para publicar y descubrir programas WebAssembly en Nostr. Los binarios WASM se almacenan como eventos Nostr, y los clientes pueden descargarlos y ejecutarlos en un runtime aislado. Una [demo app](https://nprogram.netlify.app/) muestra scrolls corriendo en el navegador, con programas de ejemplo publicados como eventos Nostr que cualquier cliente puede obtener y ejecutar.

- **[NIP-85](/es/topics/nip-85/) (Trusted Assertions): Aclaraciones** ([PR #2304](https://github.com/nostr-protocol/nips/pull/2304)): Ajusta el lenguaje de la especificación alrededor de múltiples claves y relays por proveedor de servicio, aclarando cómo deberían manejar los clientes afirmaciones de proveedores que operan a través de varios pubkeys o endpoints de relay.

- **[NIP-24](/es/topics/nip-24/) (Extra Metadata Fields): `published_at` para eventos reemplazables** ([PR #2300](https://github.com/nostr-protocol/nips/pull/2300)): Generaliza el tag `published_at` de [NIP-23](/en/topics/nip-23/) (Long-form Content) a todos los eventos reemplazables y direccionables. El tag es solo de visualización: si `published_at` es igual a `created_at`, los clientes muestran el evento como "created" en ese momento; si difieren (porque el evento fue actualizado), los clientes pueden mostrar "updated" en su lugar. Esto permite que perfiles kind `0` muestren fechas de "joined at" y que otros eventos reemplazables preserven su marca de tiempo de publicación original a través de actualizaciones. Una propuesta complementaria de [NIP-51](/es/topics/nip-51/) ([PR #2302](https://github.com/nostr-protocol/nips/pull/2302)) añade el mismo tag a eventos de listas.

- **[NIP-59](/es/topics/nip-59/) (Gift Wrap): kind efímero de gift wrap** ([PR #2245](https://github.com/nostr-protocol/nips/pull/2245)): Añade kind `21059` como contraparte efímera del gift wrap kind `1059` existente. Los eventos efímeros (kinds `20000`-`29999`) siguen la semántica de [NIP-01](/es/topics/nip-01/): no se espera que los relays los almacenen y pueden descartarlos tras la entrega. Esto permite a las aplicaciones enviar mensajes envueltos en gift wrap que desaparecen de los relays una vez entregados, reduciendo requisitos de almacenamiento para mensajería de alto volumen mientras conservan el mismo modelo de cifrado de tres capas que los DMs regulares de [NIP-17](/es/topics/nip-17/).

### OpenSats anuncia la decimosexta ola de grants de Nostr

[OpenSats](https://opensats.org) anunció su [decimosexta ola de grants de Nostr](https://opensats.org/blog/sixteenth-wave-of-nostr-grants) el 8 de abril, financiando cuatro grants por primera vez y una renovación. [Amethyst Desktop](https://github.com/vitorpamplona/amethyst/tree/main/desktopApp) recibe financiación para que el colaborador Robert Nagy construya una app de escritorio independiente sobre los módulos [Quartz](/es/topics/quartz/) y Commons, llevando el conjunto de funciones del cliente Android a interfaces guiadas por ratón con conexiones persistentes a relays. [Nostr Mail](https://github.com/nogringo/nostr-mail) recibe financiación para construir un sistema completo de email sobre Nostr usando eventos kind `1301` envueltos en gift wraps [NIP-59](/es/topics/nip-59/), con un cliente Flutter y servidores puente SMTP para compatibilidad con Gmail/Outlook. [Nostrord](https://github.com/Nostrord/nostrord) recibe financiación para un cliente grupal basado en relay [NIP-29](/en/topics/nip-29/) en Kotlin Multiplatform con mensajería grupal estilo Discord, moderación e hilos. [Nurunuru](https://github.com/tami1A84/null--nostr) recibe financiación para construir una versión nativa iOS del cliente Nostr enfocado en japonés, modelado sobre la interfaz familiar de LINE, con login biométrico basado en passkeys para el onboarding. HAMSTR recibió una renovación de grant (financiado por primera vez en la [undécima ola](https://opensats.org/blog/eleventh-wave-of-nostr-grants#hamstr)).

## NIP en profundidad: NIP-17 (Private Direct Messages)

[NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md) define el estándar actual para mensajes directos privados en Nostr. Reemplaza el esquema más antiguo de [NIP-04](/es/topics/nip-04/) (Encrypted Direct Messages), que filtraba metadatos (remitente, receptor y timestamps eran visibles en los relays) y usaba una construcción de cifrado más débil. NIP-17 combina [NIP-44](/es/topics/nip-44/) (Encrypted Payloads) para el cifrado con [NIP-59](/es/topics/nip-59/) (Gift Wrap) para proteger metadatos, creando un sistema de tres capas donde los relays no pueden ver quién habla con quién.

El protocolo usa tres kinds de evento apilados uno dentro de otro. La capa más interna es el mensaje real, un evento kind `14` sin firma:

```json
{
  "id": "a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744108800,
  "kind": 14,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef", "wss://inbox.example.com"],
    ["subject", "Project update"]
  ],
  "content": "The new relay config is deployed. Let me know if you see any issues.",
  "sig": ""
}
```

El evento kind `14` es deliberadamente unsigned (`sig` vacío). La especificación describe esto como una forma de proporcionar negabilidad, pero en la práctica la protección es limitada. El seal kind `13` que envuelve el rumor está firmado por la clave real del remitente. Un receptor puede mostrar el seal firmado a un tercero, probando que el remitente se comunicó con él, incluso sin revelar el contenido del mensaje. Con pruebas de conocimiento cero, un receptor puede probar el contenido exacto del mensaje sin revelar su propia clave privada. El rumor unsigned es como una carta sin firmar dentro de un sobre firmado: la firma del sobre vincula al remitente con el contenido. La verdadera negabilidad requeriría autenticación simétrica (como los HMAC de Signal), lo cual es incompatible con el modelo descentralizado de relay de Nostr, donde los mensajes deben ser autoautenticables. Las fortalezas reales de NIP-17 son la privacidad de metadatos y el secreto del contenido, no la negabilidad.

Este mensaje unsigned se envuelve luego en un seal kind `13`, firmado por el remitente real y cifrado con [NIP-44](/es/topics/nip-44/) para el receptor:

```json
{
  "id": "b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744022400,
  "kind": 13,
  "tags": [],
  "content": "<nip44-encrypted kind 14 payload>",
  "sig": "e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4"
}
```

El seal no tiene tags, así que incluso si se descifrara no revelaría al receptor. El seal está firmado por la clave real del remitente, lo que permite al receptor autenticar el mensaje comprobando que el `pubkey` del seal coincide con el `pubkey` del kind `14` interno.

El seal se envuelve después en un gift wrap kind `1059`, firmado por una clave aleatoria desechable y dirigido al receptor:

```json
{
  "id": "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2",
  "pubkey": "9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba",
  "created_at": 1744065600,
  "kind": 1059,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef"]
  ],
  "content": "<nip44-encrypted kind 13 payload>",
  "sig": "fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210"
}
```

El `pubkey` del gift wrap es una clave aleatoria generada solo para este mensaje, y `created_at` se aleatoriza hasta dos días hacia el pasado. Esta es la capa más externa que los relays ven realmente: un mensaje de un pubkey desconocido dirigido al receptor, con un timestamp que no refleja cuándo se envió realmente el mensaje. El timestamp aleatorizado protege frente a análisis posteriores de eventos almacenados, pero un adversario conectado activamente a relays aún puede observar cuándo apareció por primera vez el gift wrap, así que esta defensa se limita a observadores pasivos que consultan datos del relay más tarde. Como el pubkey es aleatorio y el timestamp es falso, los relays no pueden determinar el remitente real. Para leer el mensaje, el receptor descifra el gift wrap usando su propia clave y el pubkey aleatorio, encuentra el seal dentro, descifra el seal usando su propia clave y el pubkey del remitente tomado del seal, y encuentra dentro el mensaje kind `14`.

NIP-17 no proporciona forward secrecy. Todos los mensajes se cifran usando el keypair estático de Nostr (mediante la derivación de claves de NIP-44 a partir de las claves del remitente y el receptor). Si una clave privada se ve comprometida, todo mensaje pasado y futuro cifrado para esa clave puede descifrarse. Es un tradeoff deliberado: como el cifrado depende solo del nsec, un usuario que haga backup de su nsec puede recuperar todo su historial de mensajes desde cualquier relay que aún almacene los gift wraps. Protocolos como MLS (usado por [Marmot](/es/topics/marmot/)) proporcionan forward secrecy mediante rotación de material de claves, pero al coste de requerir sincronización de estado y de hacer imposible la recuperación histórica de mensajes después de la rotación de claves.

NIP-17 también define kind `15` para mensajes de archivo cifrados, que añade tags `file-type`, `encryption-algorithm`, `decryption-key` y `decryption-nonce` para que el receptor pueda descifrar un archivo adjunto cifrado con AES-GCM antes de subirse a un servidor Blossom. Kind `10050` se usa para publicar la lista preferida de relays de DM del usuario, para que los remitentes sepan dónde entregar gift wraps. El conjunto de tags `pubkey` + `p` en un mensaje define una sala de chat; añadir o eliminar un participante crea una sala nueva con historial limpio.

Las implementaciones cubren a la mayoría de los clientes principales. [nospeak](https://github.com/psic4t/nospeak) usa NIP-17 para toda la mensajería uno a uno. [Flotilla](https://gitea.coracle.social/coracle/flotilla) usa NIP-17 para sus DMs con proof-of-work. [Amethyst](https://github.com/vitorpamplona/amethyst), [Primal](https://github.com/PrimalHQ/primal-android-app), [Nostur](https://github.com/nostur-com/nostur-ios-public), [Damus](https://github.com/damus-io/damus), [noStrudel](https://github.com/hzrd149/nostrudel) y [Coracle](https://github.com/coracle-social/coracle) implementan NIP-17 como su protocolo principal de DM. La especificación también soporta mensajes que desaparecen estableciendo un tag `expiration` en el gift wrap.

## NIP en profundidad: NIP-46 (Nostr Remote Signing)

[NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md) define un protocolo para separar la clave privada del usuario de la aplicación cliente. En lugar de pegar un nsec en una web app, el usuario ejecuta un firmante remoto (también llamado "bunker") que guarda la clave privada y responde a solicitudes de firma a través de relays Nostr. El cliente nunca ve la clave privada. Esto reduce la superficie de ataque: un cliente comprometido puede solicitar firmas, pero no puede extraer la propia clave.

El protocolo usa kind `24133` tanto para solicitudes como para respuestas, cifradas con [NIP-44](/es/topics/nip-44/) (Encrypted Payloads). Un cliente genera un `client-keypair` desechable para la sesión y se comunica con el firmante remoto mediante mensajes cifrados con NIP-44 etiquetados con los pubkeys de ambos. Aquí hay una solicitud de firma de un cliente a un firmante remoto:

```json
{
  "id": "aa11bb22cc33dd44ee55ff6677889900aabbccdd11223344556677889900aabb",
  "pubkey": "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86",
  "created_at": 1744108800,
  "kind": 24133,
  "tags": [
    ["p", "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52"]
  ],
  "content": "<nip44-encrypted JSON-RPC request>",
  "sig": "1122334455667788990011223344556677889900aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff0011223344556677"
}
```

El `content` cifrado contiene una estructura similar a JSON-RPC:

```json
{
  "id": "random-request-id-1",
  "method": "sign_event",
  "params": ["{\"kind\":1,\"content\":\"Hello from remote signing\",\"tags\":[],\"created_at\":1744108800}"]
}
```

El firmante remoto descifra la solicitud, la presenta al usuario para su aprobación (o la aprueba automáticamente según los permisos configurados), firma el evento con la clave privada del usuario y devuelve el evento firmado en una respuesta:

```json
{
  "id": "bb22cc33dd44ee55ff6677889900aabb11223344556677889900aabbccddeeff",
  "pubkey": "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52",
  "created_at": 1744108801,
  "kind": 24133,
  "tags": [
    ["p", "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86"]
  ],
  "content": "<nip44-encrypted JSON-RPC response>",
  "sig": "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
}
```

Las conexiones pueden iniciarse desde cualquiera de los dos lados. Un firmante remoto proporciona una URL `bunker://` que contiene su pubkey e información de relay. Un cliente proporciona una URL `nostrconnect://` con su pubkey de cliente, relays y un secreto para verificación de conexión. El parámetro `secret` evita suplantación de conexión: solo la parte que recibió la URL fuera de banda puede completar el handshake.

Se definen ocho métodos: `connect` para establecer la sesión, `sign_event` para firmar eventos, `get_public_key` para conocer el pubkey del usuario, `ping` para keepalive, `nip04_encrypt`/`nip04_decrypt` para cifrado legacy, `nip44_encrypt`/`nip44_decrypt` para cifrado actual, y `switch_relays` para gestión de relays. La migración de relay la maneja el firmante remoto, que puede mover la conexión a nuevos relays con el tiempo sin romper la sesión.

Los clientes solicitan capacidades específicas en el momento de conexión mediante un sistema de permisos. Una cadena de permisos como `nip44_encrypt,sign_event:1,sign_event:14` solicita acceso a cifrado NIP-44 y acceso de firma solo para eventos kind `1` y kind `14`. El firmante remoto puede aceptar, rechazar o modificar estos permisos. Esto significa que un cliente web para leer y publicar notas podría recibir solo permiso `sign_event:1`, mientras que un cliente de DM podría recibir también permisos `sign_event:14` y `nip44_encrypt`.

[Amber](https://github.com/greenart7c3/Amber) implementa NIP-46 en Android, y su [v6.0.0-pre1](#amber-v600-pre1-añade-claves-de-firma-nip-46-por-conexión) de esta semana añade claves de firma por conexión para aislar clientes entre sí. [nsec.app](https://github.com/nicktee/nsecapp) (antes Nostr Connect) proporciona un bunker basado en web. [nostr-tools](https://github.com/nbd-wtf/nostr-tools) incluye `BunkerSigner` para clientes JavaScript, y [el PR #530 de la semana pasada](/en/newsletters/2026-04-01-newsletter/#nostr-tools-adds-bunker-relay-control-and-fixes-nip-47-multi-relay-parsing) añadió `skipSwitchRelays` para gestión manual de relays. El protocolo también soporta desafíos de auth: cuando un firmante remoto necesita autenticación adicional (contraseña, biometría o token hardware), responde con una `auth_url` que el cliente abre en un navegador para que el usuario la complete.

---

Eso es todo por esta semana. ¿Estás construyendo algo o tienes noticias para compartir? Envíanos un DM en Nostr o encuéntranos en [nostrcompass.org](https://nostrcompass.org).
