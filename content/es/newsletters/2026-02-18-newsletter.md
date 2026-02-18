---
title: 'Nostr Compass #10'
date: 2026-02-18
translationOf: /en/newsletters/2026-02-18-newsletter.md
translationDate: 2026-02-18
draft: false
type: newsletters
---

Bienvenido de nuevo a Nostr Compass, tu guía semanal de Nostr.

**Esta semana:** Una capa de caché local para Blossom toma forma mientras proyectos independientes convergen en el acceso offline a medios para Android. Alby lanza un [sandbox para desarrolladores NWC](https://sandbox.albylabs.com) para construir y probar integraciones de Nostr Wallet Connect sin arriesgar fondos reales. Propuestas en competencia para la comunicación de agentes de IA en Nostr llegan en la misma semana de dos autores distintos. fiatjaf elimina campos no utilizados de [NIP-11](https://github.com/nostr-protocol/nips/pull/1946), eliminando políticas de retención, códigos de país, política de privacidad y etiquetas de preferencia comunitaria que los operadores de relay nunca adoptaron. [NIP-85](https://github.com/nostr-protocol/nips/pull/2223) fusiona guía de descubrimiento de proveedores de servicios para Aserciones de Confianza. Una nueva etiqueta `D` en [NIP-52](https://github.com/nostr-protocol/nips/pull/1752) habilita indexación de marca temporal con granularidad de día en eventos de calendario. Los nuevos proyectos incluyen [Mapnolia](https://github.com/zeSchlausKwab/mapnolia) para distribución descentralizada de teselas de mapa, [Pika](https://github.com/sledtools/pika) para mensajería cifrada con MLS, [Keep](https://github.com/privkeyio/keep-android) para firma de umbral FROST en Android, [Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree) para almacenamiento direccionado por contenido con integración Nostr, y [Prism](https://github.com/hardran3/Prism) para compartir contenido en Nostr desde cualquier app Android. [Primal Android](https://github.com/PrimalHQ/primal-android-app) fusiona 11 PRs de NWC añadiendo soporte de billetera dual y ciclo de vida automático del servicio. [Mostro Mobile](https://github.com/MostroP2P/mobile) lanza una [billetera Lightning integrada](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2) mediante integración NWC. [Notedeck](https://github.com/damus-io/notedeck) se prepara para su lanzamiento en Android App Store, mientras HAVEN alcanza [v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3) con soporte multi-npub y respaldo en la nube. Los análisis profundos de esta semana cubren el sistema de Aserciones de Confianza de NIP-85 para delegar cálculos de Web of Trust a proveedores de servicios, y el protocolo de Eventos de Calendario de NIP-52 tras su actualización de indexación con granularidad de día.

## Noticias

### Emerge una Capa de Caché Local para Blossom

Múltiples proyectos independientes están convergiendo en el mismo problema: el acceso offline a medios [Blossom](/es/topics/blossom/) en dispositivos móviles.

[Morganite](https://github.com/greenart7c3/Morganite), una nueva app Android de greenart7c3 (el desarrollador detrás de [Amber](https://github.com/greenart7c3/amber) y [Citrine](https://github.com/greenart7c3/Citrine)), implementa caché del lado del cliente para medios Blossom. Los usuarios pueden acceder a imágenes y archivos vistos anteriormente sin conexión de red.

[Aerith](https://github.com/hardran3/Aerith) lanzó [v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2) con etiquetado de imágenes, operaciones masivas de espejado/etiquetado/eliminación, filtrado por etiqueta y tipo de archivo, más soporte inicial de caché local para Blossom. Aerith es una interfaz de gestión para usuarios que almacenan medios en múltiples servidores Blossom y necesitan organizar y espejar sus blobs.

Una nueva [guía de implementación de caché local](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md) en la especificación de Blossom documenta el almacenamiento de blobs del lado del cliente, mientras que [Prism](https://github.com/hardran3/Prism) (del mismo desarrollador que Aerith) añade integración de subida a Blossom a su flujo de compartir-a-Nostr en Android. Cuatro proyectos independientes convergieron en el mismo problema esta semana: una app de caché dedicada, un gestor de medios, una especificación de referencia y una herramienta de compartir con integración Blossom, todos implementando almacenamiento local persistente más allá del simple subir y recuperar.

### Sandbox NWC para Desarrolladores de Alby

[Alby](https://sandbox.albylabs.com) lanzó un entorno sandbox para desarrolladores que trabajan con [Nostr Wallet Connect (NIP-47)](/es/topics/nip-47/). El sandbox proporciona un servicio de billetera NWC alojado donde los desarrolladores pueden crear conexiones de prueba y enviar pagos simulados sin conectarse a una billetera Lightning real, mientras observan el ciclo completo de solicitud/respuesta de eventos NWC en tiempo real. Los desarrolladores generan una cadena de conexión `nostr+walletconnect://` desde el sandbox y la pasan a su cliente. El sandbox entonces muestra los eventos de solicitud kind 23194 y respuesta kind 23195 resultantes a medida que fluyen entre el cliente y el servicio de billetera.

Esto reduce la barrera para nuevas integraciones NWC. Anteriormente, las pruebas requerían una billetera Lightning personal o un servicio NWC auto-alojado. El sandbox abstrae eso, dando a los desarrolladores un ciclo de retroalimentación inmediato para implementar los métodos `pay_invoice`, `get_balance`, `make_invoice`, `lookup_invoice` y `list_transactions` contra un endpoint NWC activo.

### Llegan los NIPs para Agentes de IA

Las propuestas de comunicación para agentes de IA en Nostr aparecieron con pocos días de diferencia, abordando el problema desde ángulos distintos.

[NIP-XX: AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226) de joelklabo define un protocolo completo para la interacción de agentes de IA: kinds de evento para prompts, respuestas, deltas de streaming, actualizaciones de estado, telemetría de herramientas, errores, cancelaciones y descubrimiento de capacidades. Un evento de descubrimiento `ai.info` (kind 31340, reemplazable) permite a los agentes anunciar sus modelos soportados, herramientas con esquemas, soporte de streaming y límites de tasa. La propuesta de joelklabo incluye correlación de ejecuciones mediante ID de prompt, gestión de sesión, reconciliación de streams con ordenamiento por secuencia, y orientación de [NIP-59](/es/topics/nip-59/) para privacidad de metadatos.

[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220) de pablof7z adopta un enfoque diferente, definiendo kinds para la instanciación de agentes: definiciones y lecciones. Estos son los tipos de evento que pablof7z utiliza en [TENEX](https://github.com/tenex-chat/tenex), el sistema de aprendizaje autónomo construido sobre Nostr. Una propuesta complementaria, [NIP-AD: MCP Server and Skill Announcements](https://github.com/nostr-protocol/nips/pull/2221), también de pablof7z, define eventos para anunciar servidores [Model Context Protocol](https://modelcontextprotocol.io/) y habilidades en Nostr. Se soportan comentarios [NIP-22](/es/topics/nip-22/), para que la comunidad pueda discutir y valorar servidores MCP directamente en Nostr.

NIP-XX cubre la comunicación completa entre agentes mientras NIP-AE y NIP-AD abordan la identidad y el descubrimiento de herramientas. Estas propuestas podrían converger en un estándar unificado o coexistir como capas complementarias.

## Lanzamientos

### HAVEN v1.2.0-rc3

[HAVEN](https://github.com/bitvora/haven), el relay personal todo-en-uno que agrupa cuatro funciones de relay con un servidor de medios [Blossom](/es/topics/blossom/), alcanzó [v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3). Este release candidate añade soporte para múltiples npubs, permitiendo que una sola instancia de HAVEN sirva a varias identidades Nostr. Los RC anteriores añadieron indicadores `--from-cloud` y `--to-cloud` para respaldo en la nube (RC2) y corrigieron un bug de doble conteo en Web of Trust (RC1).

### Mostro Mobile v1.2.0: Billetera Lightning Integrada

[Mostro Mobile](https://github.com/MostroP2P/mobile), el cliente móvil para el exchange P2P de Bitcoin [Mostro](https://github.com/MostroP2P/mostro) ([v1.1.0 cubierto la semana pasada](/es/newsletters/2026-02-11-newsletter/#mostro-lanza-primera-beta-pública)), lanzó [v1.2.0](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2) con una billetera Lightning integrada mediante integración completa de [NWC (NIP-47)](/es/topics/nip-47/). Compradores y vendedores ya no necesitan cambiar de app para gestionar facturas. La app detecta facturas hold para vendedores y las paga automáticamente a través de la billetera conectada, mientras los compradores obtienen generación automática de facturas. El lanzamiento sigue a [v1.1.1](https://github.com/MostroP2P/mobile/releases/tag/v1.1.1%2B1) de principios de semana, que añadió soporte multi-nodo de Mostro con un registro curado de instancias de confianza, obtención de metadatos kind 0 para visualización de nodos, gestión personalizada de nodos por pubkey, y fallback automático cuando el nodo seleccionado queda fuera de línea.

En el lado del servidor, [Mostro v0.16.2](https://github.com/MostroP2P/mostro/releases/tag/v0.16.2) llegó con correcciones para pagos duplicados de comisiones de desarrollo, limitación de tasa en el endpoint RPC de validación de contraseña, y limpieza adecuada de disputas en cancelaciones cooperativas.

Un nuevo proyecto complementario, [mostro-skill](https://github.com/MostroP2P/mostro-skill), permite a agentes operar en Mostro a través de Nostr.

### Aerith v0.2

[Aerith](https://github.com/hardran3/Aerith), el gestor de imágenes [Blossom](/es/topics/blossom/), lanzó [v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2) con etiquetas de imagen para organizar medios, operaciones masivas de espejado/etiquetado/eliminación entre servidores, filtrado por etiqueta y tipo de archivo, más soporte inicial de caché local. Consulta la [sección de Noticias](#emerge-una-capa-de-caché-local-para-blossom) para el contexto de la tendencia más amplia de caché local.

### Mapnolia: Teselas de Mapa Descentralizadas sobre Nostr

[Mapnolia](https://github.com/zeSchlausKwab/mapnolia) es un nuevo servidor de datos geoespaciales que divide archivos de mapas [PMTiles](https://github.com/protomaps/PMTiles) en regiones geográficas y las anuncia en Nostr para su descubrimiento descentralizado. Publica eventos reemplazables parametrizados kind 34444 en relays Nostr que contienen un índice completo de fragmentos de teselas de mapa con metadatos de capa, regiones geohash, referencias de archivos y detalles del servidor [Blossom](/es/topics/blossom/).

Los clientes descubren y recuperan datos de mapa a través de la red Nostr en lugar de servidores de teselas centralizados, con eventos de anuncio que contienen suficientes metadatos para solicitar solo las regiones geográficas necesarias desde los servidores Blossom listados. Mapnolia es el primer proyecto en llevar la distribución de datos geoespaciales a Nostr, abriendo posibilidades para aplicaciones de mapeo con capacidad offline.

### Pika: Mensajería Cifrada Basada en Marmot

[Pika](https://github.com/sledtools/pika) es una nueva app de mensajería cifrada de extremo a extremo para iOS y Android que usa el protocolo [Marmot](/es/topics/marmot/), el cual superpone [Messaging Layer Security (MLS)](/es/topics/mls/) sobre relays Nostr. La arquitectura separa las responsabilidades en un núcleo Rust (`pika_core`) que gestiona el estado MLS y el cifrado/descifrado de mensajes sobre relays Nostr, con capas nativas de UI en SwiftUI (iOS) y Kotlin (Android). El estado fluye de forma unidireccional: la UI despacha acciones al actor Rust, que muta el estado y emite instantáneas con números de revisión de vuelta a la UI via UniFFI y bindings JNI.

Pika se une a un campo creciente de mensajeros MLS-sobre-Nostr junto a [White Noise](https://github.com/marmot-protocol/whitenoise), [Vector](https://github.com/VectorPrivacy) y [0xchat](https://0xchat.com). Todos usan relays Nostr como capa de transporte para el texto cifrado MLS, manteniendo a los operadores de relay sin posibilidad de leer el contenido de los mensajes. Pika usa el Marmot Development Kit (MDK) para su implementación MLS y nostr-sdk para la conectividad con relays.

### Keep: Firma de Umbral [FROST](/es/topics/frost/) para Android

[Keep](https://github.com/privkeyio/keep-android) es una nueva aplicación Android para firma de umbral [FROST](/es/topics/frost/) donde ningún dispositivo individual posee la clave privada completa. Implementa [NIP-55](/es/topics/nip-55/) (Android Signer) y [NIP-46](/es/topics/nip-46/) (firma remota), para que los clientes Nostr compatibles puedan solicitar firmas mientras el material de clave permanece distribuido entre dispositivos. Las configuraciones predeterminadas son 2-de-3 y 3-de-5, aunque se soporta cualquier umbral t-de-n.

La ceremonia de generación distribuida de claves (DKG) de Keep se ejecuta sobre relays Nostr usando kinds de evento personalizados: kind 21101 para anuncios de grupo, kind 21102 para polinomios de compromiso de la ronda 1 (difundidos públicamente), y kind 21103 para shares de secreto de la ronda 2 (cifrados punto a punto con [NIP-44](/es/topics/nip-44/) entre participantes). El escalar de clave privada del grupo nunca se computa ni ensambla en ningún lugar durante el DKG. Cada dispositivo posee solo su evaluación del polinomio, y cualquier t shares pueden producir una firma Schnorr válida a través de un protocolo de dos rondas de comprometer-luego-firmar. La firma de 64 bytes resultante es indistinguible de una firma Schnorr de un solo firmante. Bajo el capó, Keep usa el crate `frost-secp256k1-tr` de la Zcash Foundation con ajuste Taproot, de modo que la clave pública del grupo funciona directamente como un npub de Nostr.

Keep se une a la familia de proyectos [Frostr](https://frostr.org) junto a [Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop), [Igloo for Android](https://github.com/FROSTR-ORG/igloo-android), [Frost2x](https://github.com/FROSTR-ORG/frost2x) e [Igloo for iOS](https://github.com/FROSTR-ORG/igloo-ios), ampliando las opciones de gestión de claves de umbral en Nostr.

### Prism: Comparte Cualquier Cosa en Nostr desde Android

[Prism](https://github.com/hardran3/Prism) es una nueva app Android (Kotlin/Jetpack Compose, API 26+) que se registra como destino de compartir del sistema, permitiendo a los usuarios publicar texto, URLs, imágenes y vídeo en Nostr desde cualquier app de su teléfono. Las URLs compartidas pasan por un eliminador de parámetros de seguimiento antes de componerse en notas. Prism obtiene metadatos OpenGraph para generar vistas previas enriquecidas de enlaces y renderiza referencias nativas de Nostr (`note1`, `nevent1`) de forma inline.

El motor de programación usa un enfoque híbrido `AlarmManager`/`WorkManager` para evitar las optimizaciones de batería de Android: AlarmManager gestiona la temporización precisa de activación mientras que tareas expeditas de WorkManager aseguran la entrega, con reintento exponencial para escenarios offline. Las subidas de medios pasan por servidores [Blossom](/es/topics/blossom/) configurables con generación de miniaturas para imágenes y fotogramas de vídeo. Toda la firma de eventos se delega a firmantes externos [NIP-55](/es/topics/nip-55/) como [Amber](https://github.com/greenart7c3/amber), con soporte multi-cuenta para cambiar entre identidades. Prism también soporta publicaciones [NIP-84 (Highlights)](/es/topics/nip-84/). Del mismo desarrollador que [Aerith](#aerith-v02).

### Hashtree: Almacenamiento Direccionado por Contenido con Integración Nostr

[Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree) es un sistema de almacenamiento de blobs direccionado por contenido basado en el sistema de archivos que publica raíces Merkle en Nostr para crear direcciones mutables npub/ruta. El sistema usa "almacenamiento simple" que funciona con cualquier almacén clave-valor, dividiendo el contenido en bloques de 2MB optimizados para subidas a [Blossom](/es/topics/blossom/). A diferencia de BitTorrent, no se necesita computación activa de pruebas Merkle, solo almacenar y recuperar blobs por hash.

La integración con Nostr permite URLs de repositorios git como `htree://npub.../repo-name` para clonar repositorios, con comandos como `htree publish mydata <hash>` para publicar hashes de contenido en direcciones `npub.../mydata`. El CLI integral soporta modos de almacenamiento cifrado (predeterminado) y público, anclaje de contenido, subida a servidores Blossom y gestión de identidades Nostr. Cada elemento almacenado es bytes crudos o un nodo de árbol, proporcionando una base para la distribución descentralizada de contenido a través de la red de relays de Nostr.

### Espy: Captura de Paleta de Colores en Shakespeare

[Espy](https://espy.you), construido sobre la plataforma [Shakespeare](https://soapbox.pub/tools/shakespeare/), permite a los usuarios capturar paletas de colores de fotos y compartirlas como eventos Nostr. Shakespeare es un constructor de apps impulsado por IA que autentica a los usuarios via extensiones de navegador NIP-07 y proporciona conectividad integrada a relays Nostr, para que los desarrolladores lancen apps sin implementar su propia gestión de claves o pool de relays. Espy extrae colores dominantes de la entrada de la cámara en tarjetas de paleta compartibles descubribles a través de feeds estándar de Nostr.

### Flotilla 1.6.4

[Flotilla](https://gitea.coracle.social/coracle/flotilla), el cliente Nostr estilo Discord de hodlbod que organiza relays como grupos, lanzó [1.6.4](https://gitea.coracle.social/coracle/flotilla/releases/tag/1.6.4). La familia de proyectos Coracle ha migrado de GitHub a una [instancia Gitea](https://gitea.coracle.social/coracle) auto-alojada. Este lanzamiento añade notificaciones push via NIP-9a y un flujo de recepción de billetera, además de listados clasificados y soporte de URL de espacio. Las mejoras de interfaz incluyen modales y gestión de notificaciones mejorados. El silenciado de salas y los márgenes seguros en móvil completan los cambios, junto a correcciones para subidas de imágenes en Safari y detalles de eventos de calendario.

### Shosho v0.12.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), la app de streaming en vivo para móvil con integración Nostr, lanzó [v0.12.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.12.0). Este lanzamiento añade Clips de vídeo con respuestas integradas en el reproductor y emojis personalizados. La protección de hilos bloquea el spam de menciones indirectas, y una nueva función de compartir QR permite a los usuarios intercambiar perfiles offline. Un nuevo modo de reproducción horizontal da a los streams una experiencia de visualización estilo Twitch, y la pantalla de exploración ahora muestra clips de creadores junto a streams en vivo.

### Granary v10.0

[Granary](https://github.com/snarfed/granary), una biblioteca de traducción de la web social que convierte datos entre Nostr, Bluesky, ActivityPub y otras plataformas a un formato común, lanzó [v10.0](https://github.com/snarfed/granary/releases/tag/v10.0) con cambios disruptivos. El lanzamiento cambia los IDs de ActivityStreams 1 predeterminados de Nostr de bech32 a hex y añade soporte ampliado de Nostr incluyendo análisis de menciones [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) y etiquetas de artículo. Una nueva opción de salida múltiple en los conversores permite a los desarrolladores traducir entre protocolos en lote.

### Nostr MCP Server v3.0.0

[Nostr MCP Server](https://github.com/AustinKelsay/nostr-mcp-server), un servidor [Model Context Protocol](https://modelcontextprotocol.io/) que permite a agentes de IA interactuar con la red Nostr, lanzó [v3.0.0](https://github.com/AustinKelsay/nostr-mcp-server/releases/tag/v3.0.0). Este lanzamiento mayor añade acciones sociales (follows, reacciones, reposts, respuestas) y gestión de lista de relays con soporte [NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md) más autenticación opcional [NIP-42](/es/topics/nip-42/). La mensajería directa via [NIP-17](/es/topics/nip-17/) y [NIP-44](/es/topics/nip-44/) también es nueva. El lanzamiento se complementa con las [propuestas de NIP para agentes de IA](#llegan-los-nips-para-agentes-de-ia) de esta semana como herramientas prácticas para agentes que operan en Nostr.

### Aegis v0.3.8

[Aegis](https://github.com/ZharlieW/Aegis), el firmante Nostr multiplataforma, lanzó [v0.3.8](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.8) con soporte multilingüe en la UI y un gestor de actualizaciones incrementales para su navegador de apps Nostr integrado. El nuevo mecanismo de actualización computa diferencias incrementales contra el estado local, manteniendo el directorio integrado de apps web de Nostr actualizado con menor uso de ancho de banda. El lanzamiento también introduce caché de material de clave de 5 minutos para reducir las consultas a la base de datos al firmar múltiples eventos consecutivos.

### SNSTR v0.3.1

[SNSTR](https://github.com/AustinKelsay/snstr) (Secure Nostr Software Toolkit for Renegades), una biblioteca TypeScript para el protocolo Nostr, lanzó [v0.3.1](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.1). El lanzamiento añade guardas de verificación de paquete que aseguran que todos los puntos de entrada estén incluidos en los tarballs de npm, con aplicación en CI en Node y Bun. [v0.3.0](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.0) se lanzó la misma semana.

### Citrine v2.0.0-pre1

[Citrine](https://github.com/greenart7c3/Citrine), el relay Android de Nostr de greenart7c3, lanzó [v2.0.0-pre1](https://github.com/greenart7c3/Citrine/releases/tag/v2.0.0-pre1) con mejoras de rendimiento a través de índices de base de datos optimizados y mejor gestión de corrutinas de Kotlin. El lanzamiento también mejora el soporte para alojar apps web, con cada app ejecutándose ahora en su propio puerto.

## Actualizaciones de Proyectos

### Primal Android: Expansión de Infraestructura NWC

[Primal Android](https://github.com/PrimalHQ/primal-android-app) fusionó 11 PRs relacionados con NWC esta semana, continuando la construcción [iniciada hace dos semanas](/es/newsletters/2026-02-04-newsletter/#primal-android-lanza-cifrado-nwc). Este lote añade soporte de NWC para billetera dual, inicio/parada automática del servicio vinculada a notificaciones del backend, enrutamiento de conexión por tipo de billetera y limpieza adecuada de datos al eliminar una billetera. El servicio NWC ahora gestiona su propio ciclo de vida basado en el estado de la conexión de la billetera, reduciendo la intervención manual del usuario.

### Notedeck: Preparación para Android App Store

[Notedeck](https://github.com/damus-io/notedeck), el cliente Nostr multiplataforma del equipo [Damus](https://github.com/damus-io/damus), fusionó la [preparación para el lanzamiento en Android App Store](https://github.com/damus-io/notedeck/pull/1287) esta semana. El PR añade un plan de cumplimiento de UGC (Contenido Generado por el Usuario) requerido por Google Play, incluyendo una pantalla de aceptación de Términos de Servicio, bloqueo de usuarios via menús contextuales y ajustes, funcionalidad [NIP-56 (Reporting)](/es/topics/nip-56/) que publica eventos de reporte en relays, y una sección de ajustes de Contenido y Seguridad. Se añadió infraestructura de build para generar APKs firmados y AABs (Android App Bundles) para lanzamiento via nuevos objetivos de Makefile. Un documento EULA establece un requisito de edad de 17+ y avisos específicos de Nostr sobre contenido descentralizado. Las características de cumplimiento en sí se lanzan en PRs de seguimiento; esta fusión sienta las bases de documentación y firma.

En el lado iOS de Damus, se corrigió un [spinner de carga infinita](https://github.com/damus-io/damus/pull/3593) donde el spinner persistía indefinidamente después de que el contenido ya había cargado.

### Nostria: Relays de Descubrimiento y Correcciones de DM

[Nostria](https://github.com/nostria-app/nostria), el cliente Nostr multiplataforma enfocado en escala global, fusionó 9 PRs esta semana. El más destacado añade [auto-inicialización de Relays de Descubrimiento](https://github.com/nostria-app/nostria/pull/460) para búsqueda de perfiles, dando a los nuevos usuarios conectividad de relay funcional sin configuración manual. Otras correcciones abordan el [ajuste de texto en DMs](https://github.com/nostria-app/nostria/pull/466), [relleno de viewport en vídeo a pantalla completa](https://github.com/nostria-app/nostria/pull/479), [extracción de metadatos de artículo en vistas previas de repost](https://github.com/nostria-app/nostria/pull/481) y [resolución de URI nostr: en notificaciones](https://github.com/nostria-app/nostria/pull/458).

### Camelus: Migración a Riverpod v3

[Camelus](https://github.com/camelus-hq/camelus), el cliente Nostr basado en Flutter, fusionó 5 PRs esta semana centrados en una [migración de API a Riverpod v3](https://github.com/camelus-hq/camelus/pull/158) y [refactorización de feed genérico](https://github.com/camelus-hq/camelus/pull/159). Un [caché de notas embebidas](https://github.com/camelus-hq/camelus/pull/161) evita solicitudes redundantes a relays para notas citadas.

## Actualizaciones de NIPs

Cambios recientes al [repositorio de NIPs](https://github.com/nostr-protocol/nips):

**Fusionados:**

- **[NIP-85: Descubrimiento de Proveedores de Servicio](https://github.com/nostr-protocol/nips/pull/2223)**: vitorpamplona añadió orientación sobre el descubrimiento por parte del cliente de proveedores de servicios de [NIP-85 Trusted Assertions](/es/topics/trusted-relay-assertions/), incluyendo sugerencias de relay y claves de servicio específicas por algoritmo. Consulta el [análisis profundo a continuación](#análisis-profundo-de-nip-nip-85-aserciones-de-confianza) para cobertura completa.

- **[NIP-11: Limpieza de Información de Relay](https://github.com/nostr-protocol/nips/pull/1946)**: fiatjaf eliminó `privacy_policy`, el array `retention`, `relay_countries` y el bloque de preferencias de comunidad de [NIP-11](/es/topics/nip-11/). Los operadores de relay rara vez poblaban estos campos y los clientes no actuaban sobre ellos.

- **[NIP-52: Etiqueta de Marca Temporal con Granularidad de Día](https://github.com/nostr-protocol/nips/pull/1752)**: staab añadió una etiqueta `D` requerida a los eventos de calendario basados en tiempo de [NIP-52](/es/topics/nip-52/) (kind 31923) que representa la marca temporal Unix con granularidad de día, calculada como `floor(unix_seconds / 86400)`. Múltiples etiquetas `D` cubren eventos de varios días, permitiendo una indexación temporal eficiente sin analizar marcas temporales completas.

- **[NIP-47: Simplificación](https://github.com/nostr-protocol/nips/pull/2210)**: El PR de simplificación [discutido en el Boletín #9](/es/newsletters/2026-02-11-newsletter/) se fusionó esta semana, eliminando `multi_pay_invoice` y `multi_pay_keysend` de [NIP-47 (Nostr Wallet Connect)](/es/topics/nip-47/). Consulta el [Boletín #8](/es/newsletters/2026-02-04-newsletter/#análisis-profundo-de-nip-nip-47-nostr-wallet-connect) para el análisis profundo completo del protocolo NWC.

**PRs Abiertos y Discusiones:**

- **[NIP-74: Podcasts](https://github.com/nostr-protocol/nips/pull/2211)**: Cubierto en el [Boletín #8](/es/newsletters/2026-02-04-newsletter/), esta propuesta de especificación de podcasts generó acalorada discusión esta semana. staab señaló que ya existen al menos tres estándares de podcast en competencia, y derekross apuntó a una implementación existente de seis meses con apps y podcasts activos. El camino a seguir requiere convergencia entre implementaciones antes de que se pueda asignar un número de NIP.

- **[NIP-XX: AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226)**: joelklabo propone un protocolo completo de comunicación para agentes de IA con kinds de evento para prompts, respuestas, streaming, telemetría de herramientas, errores y descubrimiento de capacidades. Consulta la [sección de Noticias](#llegan-los-nips-para-agentes-de-ia) para cobertura de todas las propuestas de IA de esta semana.

- **[NIP-PNS: Private Note Storage](https://github.com/nostr-protocol/nips/pull/1893)**: El sistema de notas privadas de jb55 define eventos kind 1080 para almacenar notas personales cifradas en relays sin revelar quién las escribió. El esquema deriva un par de claves seudónimo determinista desde el nsec del usuario via HKDF: `pns_key = hkdf_extract(ikm=device_key, salt="nip-pns")`, luego genera un par de claves secp256k1 a partir de esa clave derivada. Una segunda derivación produce una clave de cifrado simétrica: `pns_nip44_key = hkdf_extract(ikm=pns_key, salt="nip44-v2")`. Las notas internas se cifran con [NIP-44](/es/topics/nip-44/) v2 usando esta clave y se publican bajo la pubkey seudónima, de modo que los relays ven eventos kind 1080 de una identidad no vinculada a la clave principal del usuario. A diferencia de los gift wraps de [NIP-59](/es/topics/nip-59/), PNS no es vulnerable a spam (la clave seudónima es determinista, no aleatoria) y no lleva metadatos públicos (no se necesitan etiquetas `p` ya que no hay destinatario). Esta semana, jb55 publicó hallazgos de la implementación de PNS en el backend Rust de Notedeck (módulo `enostr::pns`). Identificó que la llamada `hkdf_extract` de la spec es ambigua porque HKDF del RFC 5869 tiene dos fases (Extract y Expand) que producen salidas diferentes, y la mayoría de las bibliotecas esperan ambas. Aclaró que `pns_nip44_key` omite el acuerdo de clave ECDH normal de NIP-44 y se usa directamente como clave de conversación, un detalle que los implementadores necesitan saber ya que la mayoría de las bibliotecas NIP-44 usan ECDH por defecto. También señaló una variable indefinida en la implementación de referencia de TypeScript. El PR, originalmente de abril de 2025, está siendo implementado activamente.

- **[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220)**: pablof7z define cuatro kinds de evento para la identidad de agentes en Nostr, extraídos de su trabajo en [TENEX](https://github.com/tenex-chat/tenex). La plantilla base es kind 4199 (Agent Definition), que lleva título, descripción de rol, instrucciones del sistema, declaraciones de herramientas y versión. Los modificadores de comportamiento viven en kind 4201 (Agent Nudge), que usa etiquetas `only-tool`, `allow-tool` y `deny-tool` para el control de capacidades en tiempo de ejecución. Los agentes publican lo que aprenden como eventos kind 4129 (Agent Lesson), categorizados y vinculados de vuelta a la definición padre via etiquetas `e`, refinables a través de hilos de comentarios [NIP-22](/es/topics/nip-22/). La verificación de propiedad usa kind 14199, un evento reemplazable donde los operadores humanos listan las pubkeys de sus agentes, estableciendo una cadena bidireccional cuando se compara con la etiqueta `p` del perfil kind 0 del agente.

- **[NIP-AD: MCP Server and Skill Announcements](https://github.com/nostr-protocol/nips/pull/2221)**: pablof7z define eventos para anunciar servidores [Model Context Protocol](https://modelcontextprotocol.io/) y habilidades individuales en Nostr. Los anuncios de servidores MCP llevan la URL del endpoint del servidor y la versión de protocolo soportada junto a una lista de herramientas disponibles con sus esquemas de entrada. Se soportan comentarios [NIP-22](/es/topics/nip-22/) en los anuncios de servidor, para que la comunidad pueda discutir y valorar servidores MCP directamente en Nostr.

- **[NIP-73: OSM Tag Kind](https://github.com/nostr-protocol/nips/pull/2224)**: DestBro propone añadir identificadores de OpenStreetMap a [NIP-73 (External Content IDs)](/es/topics/nip-73/), que estandariza cómo los eventos Nostr hacen referencia a contenido externo como libros (ISBN), películas (ISAN), feeds de podcasts (GUID), geohashes y URLs via etiquetas `i` y `k`. El kind de OSM propuesto permitiría que los eventos referencien características específicas del mapa (edificios, carreteras, parques) por su ID de nodo u objeto de OpenStreetMap, conectando el contenido de Nostr con la base de datos geográfica abierta.

- **[NIP-XX: Responsive Image Variants](https://github.com/nostr-protocol/nips/pull/2219)**: woikos propone extender los eventos de metadatos de archivo [NIP-94](/es/topics/nip-94/) con etiquetas para variantes de imagen responsiva a diferentes resoluciones. Los clientes podrían seleccionar la variante apropiada según el tamaño de pantalla y las condiciones de red, reduciendo el ancho de banda para usuarios móviles que ven imágenes de alta resolución alojadas en servidores [Blossom](/es/topics/blossom/).

## Análisis Profundo de NIP: NIP-85 (Aserciones de Confianza)

[NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md) define un sistema para delegar cálculos costosos a proveedores de servicios de confianza que publican resultados firmados como eventos Nostr. Las puntuaciones de Web of Trust y las métricas de engagement requieren rastrear muchos relays y procesar grandes volúmenes de eventos, un trabajo que es impracticable en dispositivos móviles. La [fusión de esta semana](https://github.com/nostr-protocol/nips/pull/2223) añadió orientación sobre el proceso de descubrimiento de estos proveedores por parte del cliente.

**Delegación:**

Calcular la puntuación de Web of Trust de un usuario requiere rastrear grafos de seguimiento con múltiples saltos a través de muchos relays, y computar conteos precisos de seguidores implica deduplicar en toda la red de relays. Los dispositivos móviles y los clientes de navegador no pueden realizar estas operaciones, sin embargo los resultados son esenciales para el filtrado de spam y la clasificación de contenido. NIP-85 cierra esta brecha permitiendo a los usuarios designar proveedores de confianza para ejecutar los cálculos y publicar resultados como eventos estándar de Nostr.

**Diseño del Protocolo:**

NIP-85 usa cuatro kinds de evento para aserciones sobre diferentes tipos de sujetos. Las aserciones de usuario (kind 30382) llevan conteo de seguidores, conteos de publicaciones/respuestas/reacciones, montos de zap, rango normalizado (0-100), temas comunes y horas activas:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30382,
  "tags": [
    ["d", "e88a691e98d9987c964521dff60025f60700378a4879180dcbbb4a5027850411"],
    ["rank", "89"],
    ["followers", "4521"],
    ["first_created_at", "1609459200"],
    ["post_cnt", "1283"],
    ["reply_cnt", "647"],
    ["reactions_cnt", "8920"],
    ["zap_amt_recd", "850000"],
    ["zap_amt_sent", "320000"],
    ["zap_cnt_recd", "412"],
    ["zap_cnt_sent", "198"],
    ["zap_avg_amt_day_recd", "1150"],
    ["zap_avg_amt_day_sent", "430"],
    ["reports_cnt_recd", "2"],
    ["reports_cnt_sent", "0"],
    ["t", "nostr"],
    ["t", "bitcoin"],
    ["active_hours_start", "14"],
    ["active_hours_end", "22"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Las aserciones de evento (kind 30383) califican notas individuales con conteo de comentarios, conteo de citas, reposts, reacciones y datos de zap:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30383,
  "tags": [
    ["d", "<target event id>"],
    ["rank", "72"],
    ["comment_cnt", "45"],
    ["quote_cnt", "12"],
    ["repost_cnt", "89"],
    ["reaction_cnt", "310"],
    ["zap_cnt", "23"],
    ["zap_amount", "125000"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Para eventos direccionables (artículos de formato largo, páginas wiki), el kind 30384 aplica las mismas métricas de engagement a todas las versiones colectivamente. El kind 30385 califica identificadores externos (libros, películas, sitios web, ubicaciones, hashtags) referenciados a través de [NIP-73 (External Content IDs)](/es/topics/nip-73/), que estandariza cómo los eventos Nostr hacen referencia a contenido externo via etiquetas `i` y `k`:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30385,
  "tags": [
    ["d", "isbn:9780765382030"],
    ["k", "isbn"],
    ["rank", "94"],
    ["comment_cnt", "67"],
    ["reaction_cnt", "203"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Cada aserción es un evento direccionable reemplazable donde la etiqueta `d` contiene el sujeto: una pubkey, ID de evento, dirección de evento o identificador NIP-73. Los proveedores de servicios firman estos eventos con sus propias claves, y los clientes los evalúan basándose en relaciones de confianza.

**Descubrimiento de Proveedores:**

Los usuarios declaran qué proveedores de aserciones confían publicando eventos kind 10040. Cada entrada especifica el tipo de aserción con la pubkey del proveedor y una sugerencia de relay, más variantes de algoritmo opcionales:

```json
{
  "id": "<event hash>",
  "pubkey": "<user pubkey>",
  "created_at": 1739836800,
  "kind": 10040,
  "tags": [
    ["30382:rank", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30382:rank", "3d842afe...", "wss://nostr.wine"],
    ["30382:zap_amt_sent", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30383:rank", "4fd5e210...", "wss://nip85.nostr.band"]
  ],
  "content": "",
  "sig": "<user signature>"
}
```

Los usuarios pueden cifrar la lista de etiquetas en `.content` usando [NIP-44](/es/topics/nip-44/) para mantener privadas sus preferencias de proveedor. Los clientes construyen una lista de proveedores verificando qué proveedores confían las cuentas a las que siguen, creando una capa de reputación descentralizada para los propios proveedores de aserciones.

**Modelo de Seguridad:**

Los proveedores deben usar claves de servicio diferentes para algoritmos distintos, y una clave única por usuario cuando los algoritmos son personalizados, evitando la correlación cruzada de consultas entre usuarios. Cada clave de servicio recibe un evento de metadatos kind 0 que describe el comportamiento del algoritmo, dando a los usuarios transparencia sobre en qué están confiando. Los eventos de aserción solo deben actualizarse cuando los datos subyacentes cambian realmente, evitando tráfico innecesario en los relays y permitiendo a los clientes cachear resultados con confianza.

**Adopción Actual:**

NIP-85 formaliza un patrón que ya estaba emergiendo de forma informal. El servidor de caché de Primal calcula métricas de engagement y puntuaciones de Web of Trust. [Antiprimal](https://gitlab.com/soapbox-pub/antiprimal), cubierto en el [Boletín #9](/es/newsletters/2026-02-11-newsletter/#antiprimal-gateway-compatible-con-estándares-al-cache-de-primal), conecta estos cálculos a clientes Nostr estándar usando kinds de evento NIP-85. [Nostr.band](https://nostr.band) opera el relay `wss://nip85.nostr.band` referenciado en los propios ejemplos de la spec, sirviendo eventos de aserción para los datos de su índice de búsqueda. En el lado del cliente, [Amethyst](https://github.com/vitorpamplona/amethyst) (desarrollado por vitorpamplona, quien también escribió este NIP) tiene soporte experimental de Aserciones de Confianza en su biblioteca `quartz`, analizando eventos de aserción y declaraciones de proveedores de servicio. [Vertex](https://vertexlab.io) calcula métricas similares de Web of Trust pero [eligió un enfoque diferente](https://vertexlab.io/blog/dvms_vs_nip_85/), usando una API directa en lugar de eventos NIP-85, citando el problema de descubrimiento y la sobrecarga computacional de las arquitecturas basadas en aserciones. Con NIP-85, cualquier cliente puede consumir aserciones de cualquier proveedor a través de un formato de evento estándar, y los proveedores compiten en precisión mientras los usuarios eligen a quién confiar.

## Análisis Profundo de NIP: NIP-52 (Eventos de Calendario)

[NIP-52](https://github.com/nostr-protocol/nips/blob/master/52.md) define eventos de calendario en Nostr, dando a los clientes una forma estándar de representar y descubrir ocurrencias en momentos específicos o entre momentos. La [fusión de la etiqueta D](https://github.com/nostr-protocol/nips/pull/1752) de esta semana añadió indexación con granularidad de día, completando una pieza que faltaba en la infraestructura de consultas de la spec.

**Dos Tipos de Evento:**

NIP-52 separa los eventos de calendario en dos kinds basados en la precisión temporal. Los eventos basados en fecha (kind 31922) representan ocurrencias de todo el día como festivos o festivales de varios días. Usan cadenas de fecha ISO 8601 en sus etiquetas `start` y `end` opcionales, sin consideración de zona horaria:

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1735689600,
  "kind": 31922,
  "content": "Annual celebration of Bitcoin's genesis block",
  "tags": [
    ["d", "bitcoin-independence-day-2026"],
    ["title", "Bitcoin Independence Day"],
    ["start", "2026-01-03"],
    ["end", "2026-01-04"],
    ["location", "Worldwide"],
    ["g", "u4pruydqqv"],
    ["t", "bitcoin"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["r", "https://bitcoinindependenceday.com"]
  ],
  "sig": "<event creator signature>"
}
```

Los eventos basados en tiempo (kind 31923) representan momentos específicos con marcas temporales Unix en sus etiquetas `start` y `end` opcionales, más identificadores de zona horaria IANA (`start_tzid`, `end_tzid`) para visualización. Ambos kinds son eventos reemplazables parametrizados, por lo que los organizadores actualizan los detalles publicando un nuevo evento con la misma etiqueta `d`.

**Calendarios y RSVPs:**

Los eventos kind 31924 definen calendarios como colecciones, referenciando eventos via etiquetas `a` que apuntan a eventos kind 31922 o 31923 por sus coordenadas de dirección:

```json
{
  "id": "<event hash>",
  "pubkey": "<calendar owner pubkey>",
  "created_at": 1739836800,
  "kind": 31924,
  "content": "Nostr community events worldwide",
  "tags": [
    ["d", "nostr-community-calendar"],
    ["title", "Nostr Community Events"],
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["a", "31922:<organizer-pubkey>:bitcoin-independence-day-2026"]
  ],
  "sig": "<calendar owner signature>"
}
```

Los usuarios pueden mantener múltiples calendarios (personal, trabajo, comunidad) y los clientes pueden suscribirse a calendarios de pubkeys específicas. Los eventos de calendario pueden incluir una etiqueta `a` que referencia un calendario para solicitar inclusión, habilitando la gestión colaborativa de calendarios donde múltiples usuarios contribuyen eventos a calendarios que no poseen.

Los RSVPs usan kind 31925, donde los usuarios publican su estado de asistencia junto a un indicador opcional de libre/ocupado:

```json
{
  "id": "<event hash>",
  "pubkey": "<attendee pubkey>",
  "created_at": 1739836800,
  "kind": 31925,
  "content": "Looking forward to it",
  "tags": [
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["e", "<kind 31923 event id>", "wss://relay.example.com"],
    ["d", "<unique-rsvp-id>"],
    ["status", "accepted"],
    ["fb", "busy"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com"]
  ],
  "sig": "<attendee signature>"
}
```

Los valores válidos de `status` son "accepted", "declined", "tentative", y la etiqueta opcional `fb` marca al usuario como libre u ocupado para ese período. Los eventos RSVP referencian la etiqueta `a` del evento de calendario y llevan la etiqueta `p` del organizador, para que el cliente del organizador pueda agregar respuestas de múltiples relays.

**La Adición de la Etiqueta D:**

Antes de la fusión de esta semana, los clientes que consultaban eventos en un rango de fechas tenían que obtener todos los eventos de una pubkey o calendario y filtrar en el lado del cliente. La nueva etiqueta `D` requerida en los eventos basados en tiempo (kind 31923) contiene una marca temporal Unix con granularidad de día calculada como `floor(unix_seconds / 86400)`. Los eventos de varios días llevan múltiples etiquetas `D`, una por día. Los relays ahora pueden indexar eventos por día y responder a consultas filtradas de forma eficiente, convirtiendo lo que era un problema de filtrado en el cliente en una búsqueda de índice en el relay.

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1739836800,
  "kind": 31923,
  "content": "Monthly meetup for Nostr developers in Austin",
  "tags": [
    ["d", "nostr-meetup-2026"],
    ["title", "Nostr Developer Meetup"],
    ["summary", "Talks and demos from local Nostr builders"],
    ["image", "https://example.com/meetup-banner.jpg"],
    ["start", "1740067200"],
    ["end", "1740078000"],
    ["start_tzid", "America/New_York"],
    ["end_tzid", "America/New_York"],
    ["D", "20139"],
    ["location", "Bitcoin Commons, Austin TX"],
    ["g", "9v6knb2pg"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["p", "<speaker-pubkey>", "wss://relay.example.com", "speaker"],
    ["t", "nostr"],
    ["t", "meetup"],
    ["r", "https://bitcoincommons.com"]
  ],
  "sig": "<event creator signature>"
}
```

El valor `D` de `20139` es igual a `floor(1740067200 / 86400)`, situando este evento el 20 de febrero de 2025. Los clientes que consultan por "todos los eventos de esta semana" envían un filtro con el rango `D` correspondiente, y los relays devuelven solo los eventos coincidentes.

**Decisiones de Diseño:**

NIP-52 omite intencionalmente los eventos recurrentes. La spec deja las reglas de recurrencia (RRULE de iCalendar) completamente fuera, delegando esa complejidad a los clientes. Un organizador publica eventos individuales para cada ocurrencia, manteniendo el modelo de datos en el relay simple. Las etiquetas de participante llevan roles opcionales ("host", "speaker", "attendee"), y las etiquetas de ubicación pueden incluir etiquetas geohash `g` para consultas espaciales junto a direcciones legibles por humanos.

**Implementaciones:**

[Flockstr](https://github.com/zmeyer44/flockstr) es el cliente de calendario principal construido sobre NIP-52. [Coracle](https://gitea.coracle.social/coracle/coracle) muestra eventos de calendario en su feed social. La adición de la etiqueta `D` de esta semana habilita la indexación temporal en el relay que ambos clientes pueden usar para reducir el ancho de banda al consultar eventos en un rango de fechas específico.

---

Eso es todo por esta semana. ¿Estás construyendo algo o tienes noticias que compartir? ¿Quieres que cubramos tu proyecto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Escríbenos vía DM [NIP-17](/es/topics/nip-17/)</a> o encuéntranos en Nostr.
