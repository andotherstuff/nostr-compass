---
title: 'Nostr Compass #8'
date: 2026-02-04
translationOf: /en/newsletters/2026-02-04-newsletter.md
translationDate: 2026-02-04
draft: false
type: newsletters
---

Bienvenido de nuevo a Nostr Compass, tu guía semanal de Nostr.

**Esta semana:** rust-nostr lanza un importante rediseño de API con 21 PRs reformulando la arquitectura del SDK. Nostria 3.0 se lanza con navegación de panel dual, gestión de listas y una renovación completa de la interfaz. Vector añade aceleración SIMD logrando mejoras de velocidad de 65x-184x y lanza soporte del protocolo [Marmot](/es/topics/marmot/) para mensajería grupal cifrada. Frostr trae firma de umbral a iOS vía TestFlight. Damus implementa pistas de relay [NIP-19 (Entidades Codificadas en Bech32)](/es/topics/nip-19/) para descubrimiento de contenido entre relays. Primal Android añade cifrado NWC y exportación de transacciones de billetera. nostr-tools y NDK reciben mejoras de confiabilidad. NIP-82 (Aplicaciones de Software) se expande para cubrir el 98% de plataformas de dispositivos. El repositorio de NIPs fusiona soporte de facturas hold para [NIP-47 (Nostr Wallet Connect)](/es/topics/nip-47/). Nuevas propuestas de protocolo incluyen NIP-74 para podcasting, NIP-DB para bases de datos de eventos en navegador, y una suite de Filtros TRUSTed para curación de contenido descentralizada. Nuevos proyectos incluyen Instagram to Nostr v2 para migración de contenido, Pod21 lanzando un marketplace descentralizado de impresión 3D, Clawstr introduciendo comunidades gestionadas por agentes de IA, y Shosho y NosCall expandiendo capacidades de streaming en vivo y videollamadas.

## Noticias

### rust-nostr Lanza Mayor Rediseño de API

El SDK [rust-nostr](https://github.com/rust-nostr/nostr) experimentó una reformulación significativa de arquitectura esta semana con 21 PRs fusionados introduciendo cambios incompatibles en toda la biblioteca. El rediseño afecta APIs centrales de las que dependen la mayoría de los desarrolladores de Rust.

[PR #1245](https://github.com/rust-nostr/nostr/pull/1245) rediseña APIs de notificación, mientras [PR #1244](https://github.com/rust-nostr/nostr/pull/1244) reemplaza `RelayNotification::Shutdown` con `RelayStatus::Shutdown` para un manejo de estado más limpio. Las APIs de firmante ahora se alinean con otros patrones del SDK vía [PR #1243](https://github.com/rust-nostr/nostr/pull/1243). Los métodos de Client y Relay recibieron limpieza en [PR #1242](https://github.com/rust-nostr/nostr/pull/1242), y las opciones de cliente ahora usan un patrón builder ([PR #1241](https://github.com/rust-nostr/nostr/pull/1241)).

Las APIs de envío de mensajes fueron rediseñadas en [PR #1240](https://github.com/rust-nostr/nostr/pull/1240), la desuscripción REQ en [PR #1239](https://github.com/rust-nostr/nostr/pull/1239), y la eliminación de relay en [PR #1229](https://github.com/rust-nostr/nostr/pull/1229). Un [PR abierto #1246](https://github.com/rust-nostr/nostr/pull/1246) añade soporte para APIs de bloqueo para completar el rediseño.

Los cambios traen consistencia al SDK pero requerirán esfuerzo de migración de proyectos existentes. Los desarrolladores que construyen sobre rust-nostr deberían revisar el changelog cuidadosamente antes de actualizar.

### Instagram to Nostr v2 Habilita Migración de Contenido

Una nueva herramienta permite a los creadores migrar su contenido existente de plataformas centralizadas a Nostr. [Instagram to Nostr v2](https://github.com/primalpaul1/instagram-to-nostr-v2) soporta importación desde Instagram, TikTok, Twitter y Substack sin requerir acceso a las claves privadas del usuario.

La herramienta aborda una barrera común de incorporación: usuarios reacios a empezar de cero en una nueva plataforma pueden ahora preservar su historial de contenido. También soporta regalar cuentas Nostr a nuevos usuarios o proponer contenido a cuentas existentes, haciéndola útil para ayudar a otros a transicionar al protocolo.

### Pod21: Red Descentralizada de Impresión 3D

[Pod21](https://github.com/gobrrrme/Pod21) ([pod21.com](https://pod21.com)) conecta operadores de impresoras 3D con compradores usando Nostr para coordinación de marketplace. La plataforma incluye un bot de DM compatible con [NIP-17 (Mensajes Directos Privados)](/es/topics/nip-17/) que maneja interacciones de marketplace, permitiendo a compradores solicitar impresiones y negociar con fabricantes a través de mensajes directos cifrados.

Los fabricantes listan su capacidad y características de impresión; los compradores navegan listados e inician órdenes vía el bot. La arquitectura sigue un patrón similar a otras aplicaciones de comercio Nostr: descubrimiento basado en relay, mensajería cifrada para coordinación de órdenes, y Lightning para liquidación. Pod21 se une a Ridestr y Shopstr como aplicaciones Nostr coordinando transacciones del mundo real a través del protocolo.

### Clawstr: Red Social de Agentes de IA

[Clawstr](https://github.com/clawstr/clawstr) se lanza como una plataforma inspirada en Reddit donde agentes de IA crean y gestionan comunidades en Nostr. La plataforma permite a agentes autónomos establecer comunidades temáticas, curar contenido e interactuar con usuarios. Las comunidades funcionan como subreddits pero con moderadores y curadores de IA guiando las discusiones. La arquitectura usa el protocolo abierto de Nostr para interacciones agente-a-agente y agente-a-humano, estableciendo un nuevo modelo para formación de comunidades en redes sociales descentralizadas.

## Lanzamientos

### Ridestr v0.2.0: Lanzamiento RoadFlare

[Ridestr](https://github.com/variablefate/ridestr) lanzó [v0.2.0](https://github.com/variablefate/ridestr/releases/tag/v0.2.0), denominado el "Lanzamiento RoadFlare", introduciendo redes de viaje compartido personales. La característica permite a los pasajeros agregar conductores favoritos a una red de confianza. Los conductores aprueban seguidores y comparten ubicaciones cifradas, permitiendo a los pasajeros ver cuando conductores de confianza están en línea y cerca. Las solicitudes de viaje van directamente a conductores conocidos.

La confiabilidad de pagos mejoró con recuperación automática de depósito, mejor sincronización de billetera entre dispositivos, y procesamiento de pagos más rápido vía polling progresivo. [PR #37](https://github.com/variablefate/ridestr/pull/37) añade la infraestructura de Fase 5-6 soportando estas características. [v0.2.1](https://github.com/variablefate/ridestr/releases/tag/v0.2.1) siguió con correcciones para bugs del diálogo de pago y el flujo "Agregar a Favoritos" post-viaje.

### Nostria 3.0

[Nostria](https://github.com/nostria-app/nostria), el cliente multiplataforma de sondreb construido para escala global, lanzó la versión 3.0 con una renovación completa de UI, nuevo logo, y cientos de correcciones. El lanzamiento representa un ciclo de desarrollo intensivo de seis semanas.

La navegación de panel dual es el mayor cambio de UX, permitiendo a usuarios de escritorio reducir el cambio de contexto al moverse entre listas, detalles e hilos. Una nueva sección Home proporciona una visión general de todas las características disponibles, y todas las pantallas comparten barra de herramientas, diseño y funcionalidad unificados.

La gestión de listas es la actualización de característica más significativa, integrándose en toda la aplicación. Los usuarios pueden gestionar listas de perfiles y filtrar contenido en cualquier característica: Streams, Música o Feeds. ¿Cansado del spam en hilos? Filtra por favoritos para ver solo sus respuestas. Quick Zaps añade zapping de un toque con valores configurables. Copy/Screenshot genera capturas de pantalla al portapapeles para compartir eventos en cualquier lugar. Muted Words ahora filtra en campos de perfil (name, display_name, NIP-05), permitiendo a usuarios bloquear todos los perfiles de bridge con una sola palabra prohibida. Configuración se volvió buscable para cambios de configuración más rápidos.

El lanzamiento añade renderizado de solicitudes de pago BOLT11 y BOLT12, selección de tamaño de texto y fuente, y mensajería "Nota para Uno Mismo" en la sección de Mensajes con renderizado de contenido referenciado como artículos y eventos. El nuevo diálogo de Compartir permite compartir rápidamente vía correo electrónico, sitios web o mensajes directos a múltiples destinatarios. Características adicionales incluyen conjuntos de emoji personalizados, Intereses (listas de hashtags como feeds dinámicos), Marcadores, Feeds de Relay Públicos, y personalización completa del menú incluyendo qué opción abre el icono de Nostria.

Disponible en Android, iOS, Windows y web en [nostria.app](https://www.nostria.app/).

### Applesauce v5.1.0

La suite de bibliotecas [Applesauce](https://github.com/hzrd149/applesauce) de hzrd149 lanzó v5.1.0 en todos los paquetes. [applesauce-signers](https://github.com/hzrd149/applesauce/releases/tag/applesauce-signers%405.1.0) añade soporte para métodos `switch_relays` y `ping` en firmantes remotos Nostr Connect, útil para gestionar conexiones de firmantes programáticamente. [applesauce-loaders](https://github.com/hzrd149/applesauce/releases/tag/applesauce-loaders%405.1.0) introduce `loadAsyncMap` para carga asíncrona paralela. [applesauce-react](https://github.com/hzrd149/applesauce/releases/tag/applesauce-react%405.1.0) añade argumentos de padding a `useAction().run()`. [applesauce-core](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.1.0) actualiza el mapeo de evento a store para manejar strings directamente sin requerir `onlyEvents`.

### nak v0.18.3

[nak](https://github.com/fiatjaf/nak) (Nostr Army Knife) de fiatjaf alcanzó [v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3) con correcciones de estabilidad de mattn. El lanzamiento previene panics cuando URLs de mint carecen del separador `://`, valida errores de dateparser antes de usar valores de fecha, y maneja casos límite en el parseo de etiquetas de desafío AUTH. Estas correcciones defensivas hacen el CLI más resiliente al procesar entradas malformadas.

### Aegis v0.3.7

[Aegis](https://github.com/ZharlieW/Aegis), el firmante de escritorio multiplataforma, lanzó [v0.3.7](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.7) añadiendo soporte de Navegador de Apps Nostr con firma [NIP-07 (Interfaz de Extensión de Navegador)](/es/topics/nip-07/). El lanzamiento registra eventos de cifrado [NIP-04 (Mensajes Directos Cifrados)](/es/topics/nip-04/) y [NIP-44 (Cifrado Versionado)](/es/topics/nip-44/), permitiendo a usuarios rastrear qué aplicaciones solicitan operaciones de cifrado. El segmento de navegador ahora filtra por plataforma para mostrar solo apps web.

### Bitchat v1.5.1 (iOS)

[Bitchat](https://github.com/permissionlesstech/bitchat), la app de mensajería con capacidad offline usando Nostr y mesh Bluetooth, lanzó [v1.5.1](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.1) con endurecimiento de seguridad para iOS. [PR #1012](https://github.com/permissionlesstech/bitchat/pull/1012) valida firmas de eventos Nostr antes de procesar, rechaza giftwraps y paquetes incrustados inválidos, limita cargas sobredimensionadas, y bloquea IDs de remitente de anuncio BLE falsificados. [PR #998](https://github.com/permissionlesstech/bitchat/pull/998) corrige autenticación de mesh BLE de iOS vinculando IDs de remitente a UUIDs de conexión, previniendo suplantación de identidad en la red mesh. [PR #972](https://github.com/permissionlesstech/bitchat/pull/972) añade limitación de tasa de notificaciones para prevenir inundaciones de descubrimiento de peers cuando múltiples dispositivos mesh están cerca.

### KeyChat v1.39.2

[KeyChat](https://github.com/keychat-io/keychat-app) lanzó [v1.39.2](https://github.com/keychat-io/keychat-app/releases/tag/v1.39.2%2B6495) añadiendo soporte [NIP-47](/es/topics/nip-47/) Nostr Wallet Connect vía [PR #148](https://github.com/keychat-io/keychat-app/pull/148). Los usuarios pueden ahora conectar billeteras Lightning externas para pagos dentro de la app de mensajería. El lanzamiento también añade notificaciones de escritorio macOS.

### Nostrmo v3.5.0

[Nostrmo](https://github.com/haorendashu/nostrmo), el cliente Flutter multiplataforma, lanzó [v3.5.0](https://github.com/haorendashu/nostrmo/releases/tag/3.5.0) reformulando su sistema de feeds. La actualización reemplaza feeds fijos con alternativas personalizables: Feed General, Feed de Menciones y Feed de Relay, cada uno configurable a través de nuevas páginas de edición. El lanzamiento implementa soporte del modelo outbox para mejor enrutamiento de eventos y expande la funcionalidad de relay local con límites de tamaño configurables y soporte de suscripción.

### Shosho v0.11.1

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), la app de streaming en vivo para Nostr, lanzó [v0.11.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.11.1) con capacidades de grabación y VOD. La actualización añade indicadores de presencia de sala mostrando quién está viendo streams, conversaciones de chat en hilos para mejor organización de discusiones, y soporte Nostr Connect en iOS vía [NIP-46](/es/topics/nip-46/). Los streamers pueden ahora guardar sus transmisiones para visualización posterior mientras mantienen interacciones de chat en tiempo real con su audiencia.

### NosCall v0.5.0

[NosCall](https://github.com/sanah9/noscall), la app de llamadas de audio y video para Nostr, lanzó [v0.5.0](https://github.com/sanah9/noscall/releases/tag/v0.5.0-release) con grupos de contactos para organizar llamadas por categoría, gestión de relay para optimización de conexión, y configuración de servidor ICE configurable para mejor traversal de NAT. El lanzamiento también añade soporte de modo oscuro. NosCall usa Nostr para señalización y coordinación de llamadas, habilitando llamadas peer-to-peer sin servidores centralizados.

### diVine 1.0.4

[diVine](https://github.com/divinevideo/divine-mobile), el cliente de video de formato corto en bucle de rabble, lanzó [1.0.4](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.4) como pre-lanzamiento alpha de Android antes de su envío a Zapstore. El lanzamiento se enfoca en probar gestión de claves Nostr, incluyendo importación de nsec, firma remota [NIP-46 (Nostr Connect)](/es/topics/nip-46/) con nsecBunker y Amber, y manejo de URLs nostrconnect://. El equipo está solicitando feedback sobre compatibilidad de relays e interoperabilidad de video con otros clientes. [PR #1265](https://github.com/divinevideo/divine-mobile/pull/1265) corrige el manejo de rutas de archivo iOS que causaba que clips de video se volvieran inutilizables después de actualizaciones de app almacenando rutas relativas en lugar de rutas absolutas de contenedor. [PR #1251](https://github.com/divinevideo/divine-mobile/pull/1251) corrige problemas de navegación al ver perfiles desde comentarios.

### Zeus v0.12.2

[Zeus](https://github.com/ZeusLN/zeus) lanzó [v0.12.2](https://github.com/ZeusLN/zeus/releases/tag/v0.12.2) como lanzamiento estable, consolidando las [correcciones NWC cubiertas en ediciones anteriores](/es/newsletters/2026-01-28-newsletter/#zeus-v0122-beta---nwc-fixes).

### Frostr Igloo iOS TestFlight

[Frostr](https://github.com/FROSTR-ORG) ([frostr.org](https://frostr.org/)) lanzó [Igloo para iOS](https://github.com/FROSTR-ORG/igloo-ios) en [TestFlight](https://testflight.apple.com/join/72hjQe3J), expandiendo firma de umbral a dispositivos Apple. Frostr usa firmas FROST (Flexible Round-Optimized Schnorr Threshold) para dividir claves nsec en shares distribuidos entre dispositivos, habilitando firma k-de-n con tolerancia a fallos. Los usuarios que se unen en "modo demo" participan en un experimento de firma de umbral 2-de-2 en vivo, demostrando las capacidades de coordinación en tiempo real del protocolo. El lanzamiento iOS se une a [Igloo para Android](https://github.com/FROSTR-ORG/igloo-android) (v0.1.2), que se lanzó en diciembre con soporte [NIP-55 (Firmante Android)](/es/topics/nip-55/) para solicitudes de firma entre apps. Ambos clientes móviles complementan [Igloo desktop](https://github.com/FROSTR-ORG/igloo-desktop) y la extensión de navegador [Frost2x](https://github.com/FROSTR-ORG/frost2x).

## Actualizaciones de Proyectos

### Damus Implementa Pistas de Relay NIP-19

[Damus](https://github.com/damus-io/damus) fusionó [PR #3477](https://github.com/damus-io/damus/pull/3477), implementando consumo de pistas de relay [NIP-19](/es/topics/nip-19/) para obtención de eventos. La característica habilita ver notas en relays no incluidos en el pool configurado del usuario extrayendo pistas de referencias [NIP-10 (Hilos de Respuesta)](/es/topics/nip-10/), [NIP-18 (Reposts)](/es/topics/nip-18/) y NIP-19. La implementación usa conexiones de relay efímeras con limpieza contada por referencia, evitando expansión permanente del pool de relays.

Correcciones adicionales incluyen parseo de facturas Lightning ([PR #3566](https://github.com/damus-io/damus/pull/3566)), carga de vista de billetera ([PR #3554](https://github.com/damus-io/damus/pull/3554)), timing de lista de relays ([PR #3553](https://github.com/damus-io/damus/pull/3553)), y precarga de perfiles para reducir "popping" visual ([PR #3550](https://github.com/damus-io/damus/pull/3550)). Un [borrador PR #3590](https://github.com/damus-io/damus/pull/3590) muestra soporte de DM privado [NIP-17](/es/topics/nip-17/) en progreso.

### Primal Android Lanza Cifrado NWC

[Primal Android](https://github.com/PrimalHQ/primal-android-app) tuvo una semana muy activa con 18 PRs fusionados enfocados en infraestructura de billetera. La app ahora se integra con Spark, el protocolo Lightning auto-custodiado de Lightspark. [PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874) añade soporte de cifrado NWC, mientras [PR #872](https://github.com/PrimalHQ/primal-android-app/pull/872) envía eventos de info NWC cuando se establecen conexiones.

[PR #870](https://github.com/PrimalHQ/primal-android-app/pull/870) habilita exportación CSV para transacciones de billetera, útil para contabilidad e impuestos. [PR #716](https://github.com/PrimalHQ/primal-android-app/pull/716) añade un cambiador de cuenta local en el Editor de Notas. Múltiples correcciones de restauración de billetera ([PR #876](https://github.com/PrimalHQ/primal-android-app/pull/876), [PR #875](https://github.com/PrimalHQ/primal-android-app/pull/875), [PR #873](https://github.com/PrimalHQ/primal-android-app/pull/873)) abordan casos límite para usuarios con configuraciones de billetera no-Spark.

### SDK TypeScript de Marmot Añade Historial de Mensajes

La implementación TypeScript del protocolo [Marmot](https://github.com/marmot-protocol/marmot) continúa en desarrollo. [PR #38](https://github.com/marmot-protocol/marmot-ts/pull/38) de hzrd149 implementa persistencia de historial de mensajes con paginación para la aplicación de chat de referencia, mientras [PR #39](https://github.com/marmot-protocol/marmot-ts/pull/39) mejora la ergonomía de la biblioteca.

En el lado Rust, [PR #161](https://github.com/marmot-protocol/mdk/pull/161) implementa manejo de estado reintentable para preservar contexto de mensajes en fallos, y [PR #164](https://github.com/marmot-protocol/mdk/pull/164) cambia a std::sync::Mutex para evitar panics de tokio con SQLite. El backend whitenoise-rs añade [integración con Amber](https://github.com/marmot-protocol/whitenoise-rs/pull/418) ([PR #418](https://github.com/marmot-protocol/whitenoise-rs/pull/418)), [actualiza a MDK y nostr-sdk 0.44](https://github.com/marmot-protocol/whitenoise-rs/pull/467) ([PR #467](https://github.com/marmot-protocol/whitenoise-rs/pull/467)), e introduce streaming de notificaciones en tiempo real vía [PR #460](https://github.com/marmot-protocol/whitenoise-rs/pull/460) con tipos de evento NewMessage y GroupInvite.

### HAVEN Añade Refresco Periódico de WoT

[HAVEN](https://github.com/bitvora/haven), el relay personal, fusionó [PR #108](https://github.com/bitvora/haven/pull/108) añadiendo refresco periódico de [Web of Trust](/es/topics/web-of-trust/). La característica asegura que las puntuaciones de confianza se mantengan actualizadas a medida que evolucionan los grafos sociales de los usuarios, mejorando la precisión del filtrado de spam con el tiempo.

### nostr-tools

[nostr-tools](https://github.com/nbd-wtf/nostr-tools), la biblioteca principal de JavaScript, recibió múltiples mejoras esta semana. Los commits incluyen una [corrección para parseo de hashtags después de saltos de línea](https://github.com/nbd-wtf/nostr-tools/commit/c2423f7f31853d97fef2e3d649204cec328e81d5) en menciones [NIP-27 (Referencias de Notas de Texto)](/es/topics/nip-27/), [poda automática de objetos de relay rotos con seguimiento de inactividad](https://github.com/nbd-wtf/nostr-tools/commit/ab802c8dbe35d29feb732ba54e82a346c21c32e2) para limpieza de conexiones, [eliminación de cola de mensajes](https://github.com/nbd-wtf/nostr-tools/commit/be9b91318fea6a0cb154b8734a15b50a4c1e7638) para optimización de rendimiento de hilo único, y [exportaciones de archivos fuente](https://github.com/nbd-wtf/nostr-tools/commit/05b1fba5113182ac0aa3c72d1f511cd956a7c139) para mejores imports de TypeScript.

### NDK

[NDK](https://github.com/nostr-dev-kit/ndk) lanzó [beta.71](https://github.com/nostr-dev-kit/ndk/commit/26abea24726ed844fdd091744ac9f768f1a530a0) con una [corrección para reconexión después de ciclos de suspensión/despertar del dispositivo y manejo de conexiones obsoletas](https://github.com/nostr-dev-kit/ndk/commit/33e759508bc656dc45d3d77c741edf581af323f3), abordando problemas de confiabilidad para aplicaciones móviles.

### Notedeck

[Notedeck](https://github.com/damus-io/notedeck), el cliente de escritorio del equipo Damus, tiene un [PR abierto #1279](https://github.com/damus-io/notedeck/pull/1279) añadiendo un visor [NIP-34 (Colaboración Git)](/es/topics/nip-34/). Esto habilitaría navegar repositorios git, parches e issues publicados en relays de Nostr directamente dentro del cliente, haciendo de Notedeck un potencial front-end para flujos de trabajo basados en ngit.

### njump

[njump](https://github.com/fiatjaf/njump), el gateway web de Nostr, añadió soporte para dos tipos de evento [NIP-51 (Listas)](/es/topics/nip-51/) vía [PR #152](https://github.com/fiatjaf/njump/pull/152). El gateway ahora renderiza kind:30000 Follow Sets, que son agrupaciones categorizadas de usuarios que los clientes pueden mostrar en diferentes contextos, y kind:39089 Starter Packs, que son colecciones de perfiles curadas diseñadas para compartir y seguimiento grupal. Estas adiciones permiten a njump mostrar listas curadas por la comunidad cuando usuarios comparten enlaces nevent.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), el cliente Android, corrigió un bug que prevenía compartir video desde la vista del reproductor ([PR #1695](https://github.com/vitorpamplona/amethyst/pull/1695)). La opción "Compartir video" estaba fallando al aparecer porque el parámetro de contenido no se estaba pasando al componente de botones de control. Los usuarios pueden ahora compartir contenido de video de Nostr a otras apps directamente desde el reproductor. [PR #1693](https://github.com/vitorpamplona/amethyst/pull/1693) corrige crashes de deserialización Jackson JSON que ocurrían al parsear ciertos eventos malformados.

### Jumble

[Jumble](https://github.com/CodyTseng/jumble), el cliente web enfocado en navegación de feeds de relay, añadió cargas de archivos de audio vía portapapeles en [PR #743](https://github.com/CodyTseng/jumble/pull/743). Los usuarios pueden ahora pegar archivos de audio directamente en el editor de publicaciones, que los sube a servidores de medios configurados e incrusta la URL en la nota. La característica refleja la funcionalidad existente de pegado de imágenes.

### Flotilla

[Flotilla](https://github.com/coracle-social/flotilla), el cliente de comunidades [NIP-29 (Grupos Basados en Relay)](/es/topics/nip-29/) de hodlbod, lanzó notificaciones vía [PR #270](https://github.com/coracle-social/flotilla/pull/270). La actualización refactoriza el sistema de alertas de polling basado en anchor a notificaciones pull locales para web y notificaciones push para móvil. La arquitectura implementa el estándar propuesto NIP-9a (ver [PR #2194](https://github.com/nostr-protocol/nips/pull/2194) abajo), donde usuarios registran callbacks de webhook con relays y reciben cargas de eventos cifradas cuando los filtros coinciden.

### Formstr

[Formstr](https://github.com/abh3po/nostr-forms), la aplicación de formularios nativa de Nostr, añadió importación de formularios y soporte de formularios cifrados en [PR #422](https://github.com/abh3po/nostr-forms/pull/422). Los usuarios pueden ahora importar formularios existentes mediante un enlace de respuesta o desde otras instancias de Formstr. La característica de cifrado permite a creadores de formularios restringir respuestas para que solo destinatarios designados puedan leer los envíos, útil para encuestas que recolectan información sensible.

### Pollerama

[Pollerama](https://github.com/abh3po/nostr-polls) ([pollerama.fun](https://pollerama.fun)), construido sobre [nostr-tools](https://github.com/nbd-wtf/nostr-tools), añadió compartir encuestas vía DM [NIP-17](/es/topics/nip-17/) en [PR #141](https://github.com/abh3po/nostr-polls/pull/141) y [PR #142](https://github.com/abh3po/nostr-polls/pull/142). Los usuarios pueden ahora compartir encuestas directamente a contactos a través de mensajes directos cifrados.

### Nostrability Schemata

[Nostrability schemata](https://github.com/nostrability/schemata), la colección de esquemas de verificación JSON para eventos Nostr, añadió cobertura de [NIP-59 (Gift Wrap)](/es/topics/nip-59/) vía [PR #59](https://github.com/nostrability/schemata/pull/59). La actualización incluye esquemas para eventos kind 13 (seal) y kind 1059 (gift wrap), complementando la cobertura existente de esquema [NIP-17](/es/topics/nip-17/).

### Vector

[Vector](https://github.com/VectorPrivacy/Vector), el mensajero de escritorio enfocado en privacidad usando [NIP-17](/es/topics/nip-17/), [NIP-44](/es/topics/nip-44/) y [NIP-59](/es/topics/nip-59/) para cifrado sin metadatos, fusionó [PR #39](https://github.com/VectorPrivacy/Vector/pull/39) introduciendo optimizaciones de rendimiento aceleradas por SIMD. La codificación hex corre 65x más rápido, la generación de vista previa de imágenes hasta 38x más rápida, y las búsquedas de mensajes 184x más rápidas vía indexación de búsqueda binaria. El PR añade intrínsecos NEON ARM64 para Apple Silicon y AVX2/SSE2 x86_64 con detección en tiempo de ejecución para Windows y Linux. El uso de memoria bajó con structs de mensaje reducidos de 472 a 128 bytes y almacenamiento de npub cortado en 99.6% mediante interning.

Vector v0.3.0 (diciembre 2025) integró [MDK (Marmot Development Kit)](https://github.com/marmot-protocol/mdk) para mensajería grupal basada en protocolo MLS, trayendo grupos cifrados de extremo a extremo con secreto hacia adelante al cliente. El compartir archivos MIP-04 ahora maneja adjuntos imeta para grupos MLS, diseñado para interoperabilidad con [White Noise](/es/newsletters/2026-01-28-newsletter/#marmot-protocol-updates). El lanzamiento también introdujo una plataforma Mini Apps con juegos multijugador P2P basados en WebXDC, una tienda de apps descentralizada llamada The Nexus, integración de billetera PIVX para pagos en la app, edición de mensajes con seguimiento completo de historial, y reducción de memoria 4x durante subidas de imágenes.

## Actualizaciones de NIPs

Cambios recientes al [repositorio de NIPs](https://github.com/nostr-protocol/nips):

**Fusionados:**

- **[NIP-47: Soporte de Facturas Hold](https://github.com/nostr-protocol/nips/pull/1913)** - [NIP-47 (Nostr Wallet Connect)](/es/topics/nip-47/) ahora soporta facturas hold, habilitando flujos de trabajo de pago avanzados donde los receptores deben liquidar o cancelar pagos explícitamente. El PR añade tres nuevos métodos RPC: `make_hold_invoice` crea una factura hold usando una preimagen pre-generada y hash de pago, `settle_hold_invoice` reclama el pago proporcionando la preimagen original, y `cancel_hold_invoice` rechaza el pago usando su hash de pago. Una nueva notificación `hold_invoice_accepted` se dispara cuando un pagador bloquea el pago. Esto habilita casos de uso como contenido de pago-para-desbloquear, sistemas de escrow de marketplace, y control de acceso por pago. Las implementaciones ya están en marcha en [Alby Hub](https://github.com/getAlby/hub/pull/1298), [Alby JS-SDK](https://github.com/getAlby/js-sdk/pull/382) y [dart NDK](https://github.com/relaystr/ndk/pull/147).

- **[NIP-05: Requisito de Minúsculas](https://github.com/nostr-protocol/nips/pull/2208)** - [NIP-05 (Verificación de Dominio)](/es/topics/nip-05/) ahora requiere explícitamente minúsculas tanto para claves públicas hex como para nombres locales en el archivo `nostr.json`. Esto era implícito en la especificación pero no estaba declarado, causando problemas de interoperabilidad cuando algunas implementaciones usaban mayúsculas mixtas mientras otras normalizaban a minúsculas. Los clientes validando identificadores NIP-05 deberían ahora rechazar cualquier respuesta `nostr.json` que contenga caracteres mayúsculas en claves o nombres.

- **[NIP-73: Códigos de País](https://github.com/nostr-protocol/nips/pull/2205)** - [NIP-73 (Geoetiquetas)](/es/topics/nip-73/) ahora soporta códigos de país ISO 3166 como alternativa a geohashes. Los eventos pueden incluir etiquetas `["g", "US", "countryCode"]` para indicar ubicación a nivel de país sin requerir coordenadas precisas. Esto habilita filtrado y descubrimiento de contenido basado en país para aplicaciones donde la ubicación exacta es innecesaria o indeseable. El PR también añadió un ejemplo de geohash faltante a la documentación de la especificación.

**PRs Abiertos y Discusiones:**

- **[NIP-82: Aplicaciones de Software](https://github.com/nostr-protocol/nips/pull/1336)** - franzap anunció una actualización mayor a esta especificación borrador, que define cómo se distribuyen aplicaciones de software vía Nostr usando eventos de lanzamiento kind 30063. La actualización ahora cubre aproximadamente el 98% de las plataformas de dispositivos globalmente, incluyendo macOS, Linux, Windows, FreeBSD, entornos WASM, extensiones de VS Code, extensiones de Chrome, y Web Bundles/PWAs. El equipo se está enfocando ahora en soporte para Android, PWA e iOS, invitando a desarrolladores a converger en este estándar compartido. Zapstore planea migrar al nuevo formato en las próximas semanas.

- **[NIP-74: Podcasts](https://github.com/nostr-protocol/nips/pull/2211)** - Define eventos direccionables para programas de podcast (kind 30074) y episodios (kind 30075). Los programas incluyen metadatos como título, descripción, categorías e imágenes de portada. Los episodios referencian su programa padre e incluyen URLs de enclosure, duraciones y marcadores de capítulos. La especificación se integra con estándares de metadatos Podcasting 2.0 e incluye etiquetas de valor para monetización V4V (valor-por-valor) vía Lightning. Plataformas como [transmit.fm](https://transmit.fm), una plataforma de publicación de podcasts nativa de Nostr, pueden publicar directamente a relays usando este formato, permitiendo a podcasters distribuir contenido sin intermediarios.

- **[NIP-FR: Notas Solo-Amigos](https://github.com/nostr-protocol/nips/pull/2207)** - Propone un mecanismo para publicar notas visibles solo para una lista de amigos definida por el usuario, utilizando una clave simétrica compartida llamada ViewKey. El autor cifra notas (kind 2044) con el ViewKey usando NIP-44. El ViewKey se distribuye a cada amigo una sola vez mediante [NIP-59 (Gift Wrap)](/es/topics/nip-59/). Los amigos que poseen el ViewKey pueden descifrar y leer las notas; todos los demás solo ven texto cifrado. Cuando el autor elimina a un amigo, el ViewKey se rota: se genera una nueva clave y se redistribuye a todos los amigos restantes vía gift wrap, asegurando que el amigo eliminado pierda acceso a publicaciones futuras. Este enfoque separa el cifrado de contenido (simétrico, eficiente) de la distribución de claves (asimétrica, por amigo), manteniendo el protocolo liviano mientras habilita una característica de privacidad frecuentemente solicitada.

- **[NIP-DB: Interfaz de Base de Datos de Eventos Nostr en Navegador](https://nostrhub.io/e/1a451c1581888215ae5c311d36c8a7c7d9e5e81f1f4010de4afaf7fcbd553e90)** ([spec](https://github.com/hzrd149/nostr-bucket/blob/master/nip.md)) - Propone una interfaz estándar `window.nostrdb` para extensiones de navegador que proporcionan almacenamiento local de eventos Nostr. La API incluye métodos para agregar eventos, consultar por ID o filtro, contar coincidencias, y suscribirse a actualizaciones. Las aplicaciones web pueden usar esta interfaz para leer de eventos cacheados localmente sin hacer solicitudes a relays, reduciendo ancho de banda y latencia. La extensión de navegador [nostr-bucket](https://github.com/hzrd149/nostr-bucket) de hzrd149 proporciona una implementación de referencia, inyectando la interfaz en todas las pestañas del navegador. Una [biblioteca polyfill](https://github.com/hzrd149/window.nostrdb.js) compañera implementa la misma API usando IndexedDB para entornos sin la extensión.

- **[Filtros TRUSTed](https://nostrhub.io/e/237667820943d1c8bbe7ab7732623ae51b337f177776ece439d4a8be84708eb7)** - Una suite de cinco propuestas relacionadas para curación de contenido descentralizada, construyendo sobre el merged [PR de Trusted Assertions #1534](https://github.com/nostr-protocol/nips/pull/1534) de vitorpamplona. La especificación central introduce eventos kind 17570 para declarar Preferencias de Proveedor de Confianza, permitiendo a usuarios especificar qué servicios confían para filtrado y clasificación de eventos. Los proveedores de confianza publican aserciones (kind 37571), estadísticas (kind 37572), y clasificaciones (kind 37573) a las que los clientes pueden suscribirse. El sistema usa una arquitectura de plugins con etiquetas W/w para especificar tipos de filtros y transformaciones. Esto habilita operaciones computacionalmente costosas como detección de spam, puntuación de reputación, y clasificación de contenido para ejecutarse en infraestructura dedicada mientras los usuarios mantienen control sobre qué proveedores confían. La suite incluye especificaciones separadas para presets de filtros, clasificaciones de usuarios, eventos confiados, y definiciones de plugins.

- **[NIP-9a: Notificaciones Push](https://github.com/nostr-protocol/nips/pull/2194)** - hodlbod propone un estándar para notificaciones push basadas en relay usando eventos de registro kind 30390. Los usuarios crean un registro que contiene filtros para eventos que quieren recibir y una URL de callback webhook. El registro se cifra a la pubkey del relay (de su campo `self` NIP-11). Cuando ocurren eventos coincidentes, los relays envían POST al callback con el ID del evento (en texto plano para deduplicación) y el evento mismo (cifrado con NIP-44 al usuario). Esta arquitectura permite a los relays enviar notificaciones push mientras protege el contenido de eventos de servidores push intermediarios. El [PR #270](https://github.com/coracle-social/flotilla/pull/270) de Flotilla implementa este estándar.

- **[Catallax](https://github.com/SigmaEnterprise/Catallax)** - Propone un protocolo de trabajo por contrato descentralizado con escrow usando eventos kind 33400. El sistema define tres roles: árbitros anuncian disponibilidad y términos, patrones crean tareas financiadas con Bitcoin en escrow, y agentes libres completan trabajo para reclamar pago. Los árbitros resuelven disputas cuando es necesario. El protocolo habilita coordinación de trabajo freelance sin confianza donde los fondos se bloquean hasta que los entregables son aceptados o el arbitraje concluye.

## Análisis Profundo de NIP: NIP-47 (Nostr Wallet Connect)

[NIP-47](/es/topics/nip-47/) define Nostr Wallet Connect (NWC), un protocolo para control remoto de billeteras Lightning usando Nostr como capa de comunicación. Con la adición de soporte de facturas hold esta semana, NWC ahora cubre el rango completo de operaciones Lightning.

El protocolo funciona a través de un intercambio simple. Una aplicación de billetera publica un evento "wallet info" (kind 13194) describiendo sus capacidades. Las aplicaciones cliente envían solicitudes cifradas (kind 23194) pidiendo a la billetera realizar operaciones como pagar facturas, crear facturas, o verificar saldos. La billetera responde con resultados cifrados (kind 23195).

NWC usa cifrado [NIP-44](/es/topics/nip-44/) entre el cliente y la billetera, con un par de claves dedicado para operaciones de billetera, manteniéndolo separado de la identidad principal de Nostr del usuario. Esta separación significa que comprometer una conexión NWC no expone la identidad Nostr del usuario.

**Métodos Soportados:**

La especificación define métodos para operaciones Lightning centrales: `pay_invoice` envía pagos, `make_invoice` genera facturas para recibir, `lookup_invoice` verifica estado de pago, `get_balance` retorna el saldo de la billetera, y `list_transactions` proporciona historial de pagos. El recientemente fusionado `pay_keysend` habilita pagos sin facturas, y `hold_invoice` soporta pagos condicionales.

**Eventos de Ejemplo:**

El servicio de billetera publica un evento info (kind 13194) anunciando sus capacidades:

```json
{
  "kind": 13194,
  "pubkey": "<pubkey del servicio de billetera>",
  "content": "pay_invoice get_balance make_invoice lookup_invoice list_transactions notifications",
  "tags": [
    ["encryption", "nip44_v2"],
    ["notifications", "payment_received payment_sent"]
  ],
  "created_at": "<timestamp unix>",
  "id": "<hash del evento>",
  "sig": "<firma del servicio de billetera>"
}
```

Un cliente envía una solicitud cifrada (kind 23194) para pagar una factura:

```json
{
  "kind": 23194,
  "pubkey": "<pubkey efímera del cliente del secreto URI de conexión>",
  "content": "<cifrado NIP-44: {\"method\": \"pay_invoice\", \"params\": {\"invoice\": \"lnbc50n1...\"}}>",
  "tags": [
    ["p", "<pubkey del servicio de billetera>"],
    ["encryption", "nip44_v2"]
  ],
  "created_at": "<timestamp unix>",
  "id": "<hash del evento>",
  "sig": "<firma de clave efímera del cliente>"
}
```

El servicio de billetera responde (kind 23195) con el resultado del pago:

```json
{
  "kind": 23195,
  "pubkey": "<pubkey del servicio de billetera>",
  "content": "<cifrado NIP-44: {\"result_type\": \"pay_invoice\", \"result\": {\"preimage\": \"...\"}, \"error\": null}>",
  "tags": [
    ["p", "<pubkey efímera del cliente>"],
    ["e", "<id del evento de solicitud>"]
  ],
  "created_at": "<timestamp unix>",
  "id": "<hash del evento>",
  "sig": "<firma del servicio de billetera>"
}
```

La etiqueta `e` en la respuesta referencia la solicitud original, permitiendo a los clientes emparejar respuestas con sus solicitudes.

**Facturas Hold:**

El [PR #1913](https://github.com/nostr-protocol/nips/pull/1913) de esta semana añadió soporte de facturas hold, habilitando pagos estilo escrow. A diferencia de facturas estándar donde el receptor reclama el pago inmediatamente liberando la preimagen, las facturas hold permiten al receptor diferir esta decisión. Cuando un pagador envía a una factura hold, los fondos se bloquean a lo largo de la ruta de pago. El receptor entonces elige liquidar (liberar la preimagen y reclamar fondos) o cancelar (rechazar pago, retornando fondos al pagador). Si ninguna acción ocurre, el pago expira y los fondos retornan automáticamente. El PR añade tres métodos NWC: `make_hold_invoice`, `settle_hold_invoice` y `cancel_hold_invoice`, más una notificación `hold_invoice_accepted`. Este mecanismo potencia aplicaciones como el escrow de viajes compartidos de Ridestr y resolución de disputas de marketplace.

**Implementaciones Actuales:**

Las billeteras principales soportan NWC: Zeus, Alby, y Primal (desde el [PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874) de esta semana) todos implementan soporte del lado de billetera. Del lado del cliente, Damus, Amethyst, y la mayoría de clientes Nostr principales pueden conectarse a billeteras NWC para zapping y pagos.

El protocolo habilita una separación de responsabilidades: los usuarios pueden ejecutar su billetera en un dispositivo mientras interactúan con Nostr desde otro, con relays de Nostr sirviendo como canal de comunicación. Esta arquitectura significa que los clientes móviles no necesitan mantener fondos directamente, mejorando la seguridad al mantener la infraestructura de billetera separada de los clientes sociales.

**Consideraciones de Seguridad:**

Las conexiones NWC deben tratarse como sensibles. Mientras el cifrado protege el contenido de los mensajes, la pubkey de billetera y el secreto de conexión deben guardarse. Las aplicaciones deben permitir a los usuarios revocar conexiones y establecer límites de gasto. El protocolo soporta restricciones de capacidad, para que las billeteras puedan limitar qué operaciones puede realizar una conexión particular.

## Análisis Profundo de NIP: NIP-59 (Gift Wrap)

[NIP-59](/es/topics/nip-59/) define un protocolo para encapsular cualquier evento Nostr en múltiples capas de cifrado, ocultando la identidad del remitente de relays y observadores. Las propuestas de esta semana para notas solo-amigos (NIP-FR) y notificaciones push (NIP-9a) ambas dependen del gift wrapping, haciéndolo un primitivo de privacidad fundamental que vale la pena entender.

**Las Tres Capas:**

El gift wrapping usa tres estructuras anidadas:

1. **Rumor** (evento sin firmar): El contenido original como evento Nostr sin firma. El rumor no puede enviarse directamente a relays porque los relays rechazan eventos sin firmar.

2. **Seal** (kind 13): El rumor se cifra usando [NIP-44](/es/topics/nip-44/) y se coloca en un evento kind 13. El seal SÍ está firmado por la clave del autor real. Esta es la prueba criptográfica de autoría.

3. **Gift Wrap** (kind 1059): El seal se cifra y coloca en un evento kind 1059 firmado por un par de claves aleatorio de un solo uso. El gift wrap incluye una etiqueta `p` para enrutamiento al destinatario.

**Un Malentendido Común: Negabilidad**

La especificación menciona que los rumores sin firmar proporcionan "negabilidad", pero esto es engañoso. La capa seal SÍ está firmada por el autor real. Cuando el destinatario descifra el gift wrap y luego el seal, tiene prueba criptográfica de quién envió el mensaje. El destinatario podría incluso construir una prueba de conocimiento cero revelando la identidad del remitente sin exponer su propia clave privada.

Lo que gift wrap realmente proporciona es **privacidad del remitente frente a observadores**: los relays y terceros no pueden determinar quién envió el mensaje porque solo ven el gift wrap firmado por una clave aleatoria. Pero el destinatario siempre sabe, y puede probarlo.

**Eventos de Ejemplo:**

Aquí está la estructura completa de tres capas de la especificación (enviando "¿Vas a la fiesta esta noche?"):

El rumor (sin firmar, no puede publicarse a relays):
```json
{
  "created_at": 1691518405,
  "content": "¿Vas a la fiesta esta noche?",
  "tags": [],
  "kind": 1,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "id": "9dd003c6d3b73b74a85a9ab099469ce251653a7af76f523671ab828acd2a0ef9"
}
```

El seal (kind 13, firmado por autor real, contiene rumor cifrado):
```json
{
  "kind": 13,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "content": "AqBCdwoS7/tPK+QGkPCadJTn8FxGkd24iApo3BR9/M0uw6n4RFAFSPAKKMgkzVMo...",
  "created_at": 1703015180,
  "tags": [],
  "id": "28a87d7c074d94a58e9e89bb3e9e4e813e2189f285d797b1c56069d36f59eaa7",
  "sig": "02fc3facf6621196c32912b1ef53bac8f8bfe9db51c0e7102c073103586b0d29..."
}
```

El gift wrap (kind 1059, firmado por clave efímera aleatoria, contiene seal cifrado):
```json
{
  "kind": 1059,
  "pubkey": "18b1a75918f1f2c90c23da616bce317d36e348bcf5f7ba55e75949319210c87c",
  "content": "AhC3Qj/QsKJFWuf6xroiYip+2yK95qPwJjVvFujhzSguJWb/6TlPpBW0CGFwfuf...",
  "created_at": 1703021488,
  "tags": [["p", "166bf3765ebd1fc55decfe395beff2ea3b2a4e0a8946e7eb578512b555737c99"]],
  "id": "5c005f3ccf01950aa8d131203248544fb1e41a0d698e846bd419cec3890903ac",
  "sig": "35fabdae4634eb630880a1896a886e40fd6ea8a60958e30b89b33a93e6235df7..."
}
```

Nótese: la `pubkey` del seal es el autor real (`611df01...`), mientras que la `pubkey` del gift wrap es una clave de un solo uso aleatoria (`18b1a75...`). Los relays solo ven el gift wrap, por lo que no pueden atribuir el mensaje al autor real.

**Qué Protege Cada Capa:**

El rumor está sin firmar y no puede publicarse a relays directamente. El seal está firmado por el autor real y prueba autoría al destinatario. El gift wrap está firmado por una clave aleatoria de un solo uso, ocultando al autor real de relays y observadores. Solo el destinatario puede descifrar a través de ambas capas para alcanzar el contenido original y verificar la firma del autor en el seal.

**Aplicaciones Actuales:**

[NIP-17 (Mensajes Directos Privados)](/es/topics/nip-17/) usa gift wrap para DMs cifrados, reemplazando el esquema anterior NIP-04. El propuesto NIP-FR (notas solo para amigos) usa gift wrapping para distribuir ViewKeys a amigos, quienes luego descifran notas cifradas con esas claves. NIP-9a (notificaciones push) cifra cargas de notificación usando principios de gift wrap.

**Protección de Metadatos:**

Las marcas de tiempo deben aleatorizarse para frustrar análisis de timing. Los relays deben requerir AUTH antes de servir eventos kind 1059 y solo servirlos al destinatario marcado. Al enviar a múltiples destinatarios, crear gift wraps separados para cada uno.

---

Eso es todo por esta semana. ¿Construyendo algo? ¿Tienes noticias que compartir? ¿Quieres que cubramos tu proyecto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contáctanos vía DM NIP-17</a> o encuéntranos en Nostr.
