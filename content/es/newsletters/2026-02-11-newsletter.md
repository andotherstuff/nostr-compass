---
title: 'Nostr Compass #9'
date: 2026-02-11
translationOf: /en/newsletters/2026-02-11-newsletter.md
translationDate: 2026-02-12
draft: false
type: newsletters
---

Bienvenido de nuevo a Nostr Compass, tu guía semanal de Nostr.

**Esta semana:** Mostro lanza su primera beta pública tras tres años de desarrollo, llevando el intercambio P2P de Bitcoin a móviles vía Nostr. OpenSats otorga su decimosexta ronda de grants de Bitcoin, con Minibits Wallet recibiendo renovación para su billetera Cashu integrada con Nostr. **Zapstore alcanza su versión estable 1.0**, marcando la maduración de la tienda de aplicaciones Android descentralizada. Coracle 0.6.29 añade temas y comentarios en highlights. Igloo Desktop v1.0.3 incorpora endurecimiento de seguridad para firma de umbral Frostr. Amber v4.1.2-pre1 migra a arquitectura Flow. Angor alcanza v0.2.5 con interfaz de financiación renovada y configuración de servidor de imágenes NIP-96. NostrPress se lanza como herramienta que convierte perfiles Nostr en blogs estáticos. Antiprimal publica un gateway compatible con estándares que conecta el servidor cache propietario de Primal con NIPs estándar de Nostr. Primal Android fusiona 18 PRs expandiendo la infraestructura NWC con soporte de doble billetera, registro de auditoría y el método `lookup_invoice`. diVine lanza feeds de video API-first. El SDK TypeScript de Marmot separa su app de chat de referencia en un repositorio independiente y comienza la migración a ts-mls v2. El repositorio de NIPs fusiona conteo aproximado HyperLogLog para NIP-45 y extrae etiquetas de identidad del kind 0. Varias propuestas de vitorpamplona inician una reducción sistemática de eventos de metadatos kind 0. Nuevas propuestas de protocolo incluyen Nostr Relay Connect para traversal de NAT y Nostr Web Tokens para claims web firmados. El análisis profundo de esta semana cubre el nuevo conteo aproximado HyperLogLog de NIP-45 para métricas de eventos entre relays y el protocolo de almacenamiento de archivos HTTP de NIP-96, ahora obsoleto en favor de Blossom, mientras proyectos transitan entre ambos estándares de medios.

## Noticias

### Mostro Lanza Primera Beta Pública

[Mostro](https://github.com/MostroP2P/mostro), el exchange peer-to-peer de Bitcoin construido sobre Nostr, lanzó su [app móvil v1.1.0](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0), la primera beta pública del proyecto tras tres años de desarrollo. La app permite intercambiar Bitcoin directamente usando Nostr para la coordinación de órdenes, con Lightning para la liquidación y ningún intermediario custodio.

El lanzamiento introduce notificaciones push con mejor fiabilidad en segundo plano en Android, un sistema de logging opcional que permite capturar y compartir datos de diagnóstico cuando surgen problemas, actualizaciones de relay más fluidas usando inicialización aditiva, y refinamientos de interfaz de Fase 2 con soporte de internacionalización. La app está disponible en [Zapstore](https://zapstore.dev) y como [descarga directa de GitHub](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0).

Mostro se une a Shopstr y Plebeian Market como aplicación de comercio nativa de Nostr, con la distinción de que se enfoca en la coordinación del intercambio fiat-a-Bitcoin. El [daemon de Mostro](https://github.com/MostroP2P/mostro) subyacente maneja el emparejamiento de órdenes y la resolución de disputas a través de relays Nostr.

### Decimosexta Ronda de Grants de Bitcoin de OpenSats

[OpenSats](https://opensats.org/blog/sixteenth-wave-of-bitcoin-grants) anunció grants para 17 proyectos de código abierto. Lo destacado para Nostr: [Minibits Wallet](https://github.com/minibits-cash/minibits_wallet), la billetera Android de [Cashu](/es/topics/cashu/) con soporte de eventos de billetera [NIP-60](/es/topics/nip-60/) e integración de nutzap, recibió renovación de grant. Minibits usa eventos Nostr para almacenar el estado de tokens ecash, haciendo respaldos de billetera portables entre dispositivos a través de sincronización por relay.

### NostrPress: De Perfil Nostr a Blog Estático

[NostrPress](https://github.com/besoeasy/NostrPress) ([blog.besoeasy.com](https://blog.besoeasy.com)) es una herramienta nueva que convierte un perfil Nostr en un blog completamente estático desplegable en cualquier lugar. Tras publicar artículos en Nostr a través de cualquier cliente, NostrPress genera un sitio web independiente a partir de esos eventos, con alojamiento local de medios y feeds RSS.

Construido con Nunjucks templating y JavaScript, NostrPress produce sitios con cero dependencia de plataforma. La salida generada es HTML/CSS plano que puede alojarse en cualquier servidor de archivos estáticos, GitHub Pages, Netlify o un VPS personal. La herramienta se une a [Npub.pro](https://github.com/nostrband/nostrsite) y [Servus](https://github.com/servus-social/servus) como opciones para convertir contenido Nostr en sitios web tradicionales.

### Antiprimal: Gateway Compatible con Estándares al Cache de Primal

[antiprimal](https://gitlab.com/soapbox-pub/antiprimal) ([antiprimal.net](https://antiprimal.net)), un nuevo proyecto de Alex Gleason y el equipo Soapbox, es un gateway WebSocket que conecta el servidor cache propietario de Primal con mensajes del protocolo estándar de Nostr. Primal ofrece funciones como estadísticas de eventos, búsqueda de contenido y cálculos de Web of Trust a través de `wss://cache.primal.net/v1`, pero el acceso requiere un formato de mensaje propietario con un campo `cache` no estándar que clientes Nostr normales no pueden usar. Antiprimal traduce solicitudes NIP estándar al formato de Primal y convierte las respuestas de vuelta.

El gateway soporta consultas COUNT de [NIP-45](/es/topics/nip-45/) (reacciones, respuestas, reposts, conteos de zap, conteos de seguidores), búsqueda [NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md), información de relay [NIP-11](/es/topics/nip-11/), y [NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md) Trusted Assertions para datos precalculados de Web of Trust de Primal. Un bot acompañante publica eventos NIP-85 kind 30382 (estadísticas de usuario) y kind 30383 (engagement de evento) a relays configurables. El proyecto está construido con TypeScript sobre Bun y usa la biblioteca Nostrify. Creado el 6 de febrero, acumula 53 commits en sus primeros tres días de desarrollo y está en línea en antiprimal.net.

### Ikaros: Gateway de Mensajería de Agentes de IA para Signal y Nostr

[Ikaros](https://gitlab.com/soapbox-pub/ikaros), un nuevo proyecto del equipo Soapbox, es un gateway de mensajería que permite a agentes de IA comunicarse a través de DMs cifrados tanto de Signal como de Nostr. El puente usa el [Agent Client Protocol](https://agentclientprotocol.org) (ACP) para conectar cualquier asistente de IA compatible con ACP a redes de mensajería reales. Tres pull requests constituyen la construcción inicial del proyecto esta semana.

El primer PR ([#1](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/1)) implementa un adaptador completo de DM cifrado [NIP-04](/es/topics/nip-04/) con soporte de envío/recepción, buffering de respuestas con flush explícito al completar, formatos de clave privada `nsec` y hex, publicación multi-relay con reconexión automática, y un asistente de configuración interactivo. El adaptador usa nostr-tools v2.23.0 y actualiza el ACP SDK a v0.14.1.

El segundo PR ([#2](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/2)) corrige una pérdida silenciosa de mensajes causada por condición de carrera en la actualización de sesión. Notificaciones entrantes que llegaban antes de que la sesión estuviera registrada en el mapa se perdían, y la corrección almacena esas notificaciones en buffer para reproducirlas cuando el registro se completa. El tercer PR ([#3](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/3)) añade metadatos de nombre de usuario y grupo/UUID de Signal a interacciones con el agente, para que el agente de IA sepa con quién habla y en qué grupo. El proyecto abre un nuevo espacio de diseño donde agentes de IA direccionables vía DMs de Nostr pueden ser contactados desde Signal, o viceversa.

### Campaña de Reducción del Kind 0

vitorpamplona abrió una serie de PRs esta semana proponiendo la extracción sistemática de datos de eventos kind 0 (metadatos de usuario) hacia kinds de evento dedicados. La campaña aborda un problema creciente, ya que eventos kind 0 han acumulado campos con el tiempo que la mayoría de clientes no usa, inflando el tamaño de cada consulta de perfil.

El [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) (fusionado) mueve etiquetas de identidad (etiquetas `i`) del kind 0 a un nuevo kind 10011, dado que la adopción de estas etiquetas ha sido mínima. Otro PR ([#2213](https://github.com/nostr-protocol/nips/pull/2213)) propone mover la verificación [NIP-05](/es/topics/nip-05/) al kind 10008, lo que permitiría a usuarios tener múltiples identificadores NIP-05 y filtrar eventos por dirección NIP-05. Un tercer PR ([#2217](https://github.com/nostr-protocol/nips/pull/2217)) propone extraer direcciones Lightning (lud06/lud16) a un nuevo kind, evitando que todos los usuarios de kind 0 carguen campos relacionados con zap que solo importan a clientes con integración Lightning.

Las propuestas han reavivado la discusión sobre la estructura general del kind 0, incluyendo el [PR #1770](https://github.com/nostr-protocol/nips/pull/1770), la propuesta de larga data para reemplazar JSON stringificado en el contenido del kind 0 con etiquetas estructuradas.

### Soporte de NIP-70 en Relays es Crítico para la Seguridad de Mensajería Cifrada

La implementación White Noise del protocolo [Marmot](/es/topics/marmot/) ha [identificado una brecha crítica](https://blog.jgmontoya.com/2026/02/10/nip70-relay-status.html) en el soporte de relays para [NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md) (Eventos Protegidos) y [NIP-42](/es/topics/nip-42/) (Autenticación). Las pruebas revelaron que relays públicos principales, incluyendo Damus, Primal y nos.lol, rechazan eventos protegidos directamente con errores `blocked: event marked as protected` en lugar de iniciar el desafío de autenticación requerido.

Esto rompe una función de seguridad clave. NIP-70 permite la eliminación segura de KeyPackages MLS gastados, previniendo ataques de "recopilar ahora, descifrar después". Al no contar con soporte de relays, protocolos de mensajería cifrada no pueden proteger a usuarios de un futuro compromiso de claves. White Noise ha desactivado NIP-70 por defecto en respuesta, manteniendo bandera opcional para usuarios con relays que lo soporten.

**Llamado a la acción para operadores de relays:** Implementen el flujo completo de autenticación NIP-42. Al recibir eventos protegidos, desafíen a clientes a probar la propiedad, luego acepten escrituras validadas. Rechazar eventos protegidos sin autenticación rompe las garantías de seguridad del protocolo de las que dependen aplicaciones de mensajería cifrada.

## Lanzamientos

### Coracle 0.6.29

[Coracle](https://github.com/coracle-social/coracle) ([coracle.social](https://coracle.social)), el cliente web de hodlbod, publicó [0.6.29](https://github.com/coracle-social/coracle/releases/tag/0.6.29). El lanzamiento añade visualización de temas y comentarios en highlights kind 9802. Un nuevo elemento de navegación de listas da acceso rápido a listas curadas por el usuario desde la interfaz principal. Bajo el capó, Coracle se actualizó a la nueva versión de Welshman, la biblioteca Nostr compartida que gestiona el manejo de relays y eventos de Coracle. La lista de relays por defecto fue renovada, y el rastreo de errores Glitchtip fue eliminado del código.

### Igloo Desktop v1.0.3

[Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop), la aplicación de firma de umbral y gestión de claves basada en [FROST](/es/topics/frost/), publicó [v1.0.3](https://github.com/FROSTR-ORG/igloo-desktop/releases/tag/v1.0.3) con endurecimiento de seguridad extensivo. El lanzamiento introduce validación IPC, aislamiento Electron, y verificaciones de relay con protección contra SSRF (server-side request forgery). Un nuevo flujo de onboarding e importación de shares simplifica la distribución de claves, la planificación de relays ahora incluye normalización y fusión por prioridad, y la arquitectura de API Electron basada en preload mejora la frontera de seguridad entre el renderer y el proceso principal. Un sistema keep-alive para el firmante mantiene la estabilidad de sesiones de firma de umbral, y mejoras de UX en la recuperación reducen la fricción de la restauración de claves.

### Amber v4.1.2-pre1

[Amber](https://github.com/greenart7c3/Amber), el firmante de eventos Android, lanzó [v4.1.2-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.2-pre1) corrigiendo la visualización ausente de puntuación de confianza de relay introducida en v4.1.1, resolviendo problemas de parseo JSON para solicitudes de cifrado/descifrado no-Nostr, y migrando el modelo de cuenta de LiveData a Flow para gestión de estado más predecible. El lanzamiento cambia secretos bunker a UUIDs completos y actualiza al plugin Gradle 9.

### Mostro Mobile v1.1.0 y Daemon v0.16.1

Consulta la [sección de Noticias arriba](#mostro-lanza-primera-beta-pública) para la cobertura completa del lanzamiento móvil. En el lado del servidor, el [daemon de Mostro](https://github.com/MostroP2P/mostro) publicó [v0.16.1](https://github.com/MostroP2P/mostro/releases/tag/v0.16.1), añadiendo publicación automática de metadatos NIP-01 kind 0 al iniciar (vía [PR #575](https://github.com/MostroP2P/mostro/pull/575)), para que el daemon ahora anuncie su identidad a la red cuando se conecta. La documentación del cálculo de comisiones de desarrollo fue corregida en [PR #571](https://github.com/MostroP2P/mostro/pull/571).

### Angor v0.2.5

[Angor](https://github.com/block-core/angor) ([angor.io](https://angor.io)), el protocolo de financiación P2P descentralizado construido sobre Bitcoin y Nostr, publicó [v0.2.5](https://github.com/block-core/angor/releases/tag/v0.2.5) con tres PRs fusionados. El [PR #649](https://github.com/block-core/angor/pull/649) rediseña la sección de gestión de Fondos (V2), reemplazando el diseño anterior con nueva interfaz para rastrear UTXOs individuales y posiciones de inversión. La renovación del InvoiceView en [PR #651](https://github.com/block-core/angor/pull/651) trae estilos de botón actualizados, diálogos cerrables, un nuevo comando "Copiar Dirección", soporte de cancelación para monitoreo de direcciones y mejor manejo del flujo de inversión. Servidores de imágenes [NIP-96](/es/topics/nip-96/) ([spec](https://github.com/nostr-protocol/nips/blob/master/96.md)) configurables en ajustes se añaden en [PR #652](https://github.com/block-core/angor/pull/652), permitiendo a usuarios elegir qué endpoint de subida de medios maneja sus imágenes y documentación de proyecto. La versión [v0.2.4](https://github.com/block-core/angor/releases/tag/v0.2.4) se publicó la semana anterior.

### Ridestr v0.2.2 y v0.2.3

[Ridestr](https://github.com/variablefate/ridestr), la plataforma de viaje compartido descentralizada [cubierta la semana pasada](/es/newsletters/2026-02-04-newsletter/#ridestr-v020-lanzamiento-roadflare), continuó su rápida iteración con [v0.2.2](https://github.com/variablefate/ridestr/releases/tag/v0.2.2) (Hotfix de Pago Bridge) y [v0.2.3](https://github.com/variablefate/ridestr/releases/tag/v0.2.3) tras el v0.2.0 "Lanzamiento RoadFlare". El hotfix v0.2.2 aborda un bug donde pagos bridge de [Cashu](/es/topics/cashu/) cross-mint estaban auto-cancelando viajes mientras el pago aún se procesaba o eventualmente tendría éxito, previniendo cancelaciones prematuras de viaje en liquidaciones lentas. Corrige parpadeo de UI y hitboxes táctiles rotos en el botón "mi ubicación". La versión v0.2.3 incluye correcciones de bugs adicionales. Ambos lanzamientos incluyen APKs separados para Ridestr (app de pasajero) y Drivestr (app de conductor).

### Nostr PHP 1.9.4

[Nostr PHP](https://github.com/nostrver-se/nostr-php) ([nostr-php.dev](https://nostr-php.dev)), la biblioteca auxiliar de PHP para el protocolo Nostr, publicó [1.9.4](https://github.com/nostrver-se/nostr-php/releases/tag/1.9.4) añadiendo propiedad configurable de `timeout` a la clase de solicitud (en [PR #106](https://github.com/nostrver-se/nostr-php/pull/106)). Esto permite a desarrolladores establecer duraciones de timeout personalizadas para conexiones de relay y solicitudes de mensajes, previniendo bloqueos indefinidos cuando un relay no responde o tarda en contestar.

### Zapstore v1.0.0

[Zapstore](https://github.com/zapstore/zapstore/releases/tag/1.0.0) ([zapstore.dev](https://zapstore.dev)), la tienda de aplicaciones Android construida sobre Nostr, **alcanzó su hito de versión estable 1.0** esta semana tras meses de release candidates.

El lanzamiento 1.0 incluye mejoras de estabilidad críticas, entre ellas manejo del estado del botón de instalación que asegura que Eliminar aparezca inmediatamente después de completar la instalación, mensajes de error amigables con detalles técnicos expandibles, y un botón "Reportar problema" que envía DMs cifrados vía Nostr usando claves efímeras. Contiene pantalla nueva de actualizaciones con polling y seguimiento por lotes, mejor watchdog de descargas para transferencias estancadas, límites dinámicos de descargas concurrentes según el rendimiento del dispositivo, sincronización más frecuente de paquetes instalados, y mejor lógica de comparación de versiones. El equipo corrigió un problema crítico de flutter_secure_storage y mejoró el manejo de casos límite del gestor de paquetes.

Este hito marca la maduración de la primera plataforma dedicada de distribución de apps de Nostr, permitiendo a desarrolladores publicar aplicaciones Android directamente a usuarios sin el control de acceso de tiendas de apps centralizadas.

### ZSP v0.3.1

[ZSP](https://github.com/zapstore/zsp), la herramienta CLI en Go del equipo [Zapstore](https://github.com/zapstore/zapstore) que reemplaza las herramientas de publicación anteriores para firmar y subir apps Android a relays Nostr, lanzó [v0.3.1](https://github.com/zapstore/zsp/releases/tag/v0.3.1). ZSP maneja la adquisición de APK desde GitHub, GitLab, Codeberg, F-Droid o archivos locales, luego parsea metadatos, firma eventos Nostr (vía clave privada, bunker [NIP-46](/es/topics/nip-46/) o extensión de navegador [NIP-07](/es/topics/nip-07/)), y sube artefactos a servidores [Blossom](/es/topics/blossom/). La versión añade modo offline completo para vinculación de keystore sin conexión de red, cabeceras `Content-Digest` en subidas a Blossom para cumplimiento del protocolo, detección corregida de APK arm64-v8a desde repositorios F-Droid, correcciones de parámetros de consulta trailing de GitLab, y soporte completo de archivos `.env` para configuración.

### Damus iOS 1.17

[Damus](https://github.com/damus-io/damus), el cliente iOS de Nostr, se actualizó a la versión 1.17 (en [PR #3606](https://github.com/damus-io/damus/pull/3606)). El lanzamiento corrige un problema de RelayPool donde conexiones se cerraban tras liberar reservas efímeras (vía [PR #3605](https://github.com/damus-io/damus/pull/3605)), lo que podía causar que suscripciones se interrumpieran inesperadamente. Resuelve un bug donde la línea de tiempo de favoritos no mostraba eventos al cambiar entre pestañas (en [PR #3603](https://github.com/damus-io/damus/pull/3603)).

### nak v0.18.3

[nak](https://github.com/fiatjaf/nak), el Nostr army knife CLI, publicó [v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3) con tres correcciones de estabilidad: prevención de panic cuando etiquetas de desafío AUTH son nil o demasiado cortas, verificación de errores de dateparser antes de usar el valor parseado, y manejo de URLs de mint Cashu que carecen del separador `://`.

### Mi: Relay Local en el Navegador

[Mi](https://git.shakespeare.diy/npub1scvyzz02ayma34hesz62pdrd5nhsmxp74hjq8msmfs9khh3r3drsnw68d8/mi.git) ([mi.shakespeare.wtf](https://mi.shakespeare.wtf)), nueva MiniApp de [Shakespeare](https://shakespeare.wtf), es un relay local en el navegador que archiva eventos Nostr del usuario en IndexedDB. Mi obtiene perfiles (kind 0), listas de contactos (kind 3), listas de relays (kind 10002) y eventos de billetera desde relays conectados y almacena todo localmente, dando acceso offline a los propios datos. Construido con React y nostr-tools 2.15.0.

### Agora v1.0.2

[Agora](https://gitlab.com/soapbox-pub/agora) ([agora.spot](https://agora.spot)), plataforma de activismo y recaudación de fondos descentralizada del equipo Soapbox, publicó [v1.0.2](https://gitlab.com/soapbox-pub/agora/-/releases/v1.0.2) con APK Android disponible para instalación directa. Primera mención de Agora en Compass. Lanzada el 17 de enero con declaración de misión: "Únete al movimiento global por la libertad. Envía apoyo a activistas en el terreno internacionalmente y participa en acciones locales."

La plataforma se centra en un mapa mundial donde usuarios exploran por país, crean "acciones" geoetiquetadas (protestas, campañas, organización comunitaria) y las discuten en hilos de comentarios. Todo el contenido se propaga a través de relays Nostr, por lo que ningún servidor central puede ser desconectado para silenciar la coordinación. Agora soporta múltiples idiomas con paridad de traducción verificada por CI, integra servidores de medios [Blossom](/es/topics/blossom/) para subidas, e incluye búsqueda, navegación por hashtags con alternancia global/regional, perfiles de usuario y sistemas de reacciones. El lanzamiento v1.0.2 es la build Android actual, disponible como descarga directa de APK.

### xonos v0.1.6

[xonos](https://codeberg.org/xonos/xonos), el cliente experimental de Nostr en 3D construido con el motor de juego Bevy, publicó [v0.1.6](https://codeberg.org/xonos/xonos/releases/tag/v0.1.6). xonos renderiza eventos Nostr en un entorno espacial 3D con capacidades de text-to-speech, explorando cómo datos del protocolo social podrían funcionar fuera de interfaces 2D convencionales.

## Actualizaciones de Proyectos

### Primal Android Expande Infraestructura NWC

[Primal Android](https://github.com/PrimalHQ/primal-android-app) fusionó 18 PRs esta semana, continuando la construcción NWC [iniciada la semana pasada](/es/newsletters/2026-02-04-newsletter/#primal-android-lanza-cifrado-nwc). El [PR #883](https://github.com/PrimalHQ/primal-android-app/pull/883) añade soporte para conexiones NWC en ambas billeteras (Spark y externa), y el [PR #879](https://github.com/PrimalHQ/primal-android-app/pull/879) implementa el método NWC `lookup_invoice` para verificar el estado de pagos.

El registro de auditoría de solicitud-respuesta NWC para depuración de interacciones de billetera llega en [PR #880](https://github.com/PrimalHQ/primal-android-app/pull/880). El soporte multi-cuenta para `PrimalNwcService` se incorpora en [PR #877](https://github.com/PrimalHQ/primal-android-app/pull/877), permitiendo a usuarios con múltiples perfiles mantener conexiones de billetera separadas. La limpieza periódica de retenciones de presupuesto expiradas en [PR #882](https://github.com/PrimalHQ/primal-android-app/pull/882) previene que reservas de pago obsoletas bloqueen operaciones de billetera.

El trabajo de UI incluye rediseños de la pantalla de actualización de billetera ([PR #889](https://github.com/PrimalHQ/primal-android-app/pull/889)), FAQ de actualización de billetera ([PR #885](https://github.com/PrimalHQ/primal-android-app/pull/885)), configuración de dirección Lightning durante onboarding ([PR #888](https://github.com/PrimalHQ/primal-android-app/pull/888)), y corrección para transacciones de zap que aparecían como pagos regulares en tipos no-Lightning ([PR #887](https://github.com/PrimalHQ/primal-android-app/pull/887)).

### diVine Lanza Feeds de Video API-First

[diVine](https://github.com/divinevideo/divine-mobile), el cliente de video de formato corto, fusionó 19 PRs esta semana, orientándose hacia arquitectura API-first. Los feeds de video API-first llegan en [PR #1468](https://github.com/divinevideo/divine-mobile/pull/1468), y endpoints API de tendencias, recientes y home en [PR #1466](https://github.com/divinevideo/divine-mobile/pull/1466). La indexación de controladores de video específicos para renderizado eficiente de feeds se implementa en [PR #1433](https://github.com/divinevideo/divine-mobile/pull/1433).

El manejo de perfiles mejoró con un patrón cache-plus-fresh para ver otros perfiles en [PR #1440](https://github.com/divinevideo/divine-mobile/pull/1440), reduciendo tiempos de carga mientras asegura datos actualizados. El equipo envió correcciones de notificaciones ([PR #1437](https://github.com/divinevideo/divine-mobile/pull/1437)), refactorización del flujo de comentarios ([PR #1431](https://github.com/divinevideo/divine-mobile/pull/1431)), y deslizamiento de pestañas en la pantalla de Notificaciones ([PR #1388](https://github.com/divinevideo/divine-mobile/pull/1388)).

### White Noise: Unificación de Keyring y Búsqueda de Usuarios

El backend [White Noise](https://github.com/marmot-protocol/whitenoise-rs) para el protocolo [Marmot](/es/topics/marmot/) fusionó 4 PRs esta semana. Dos PRs mejoraron el manejo de keyring: el [PR #468](https://github.com/marmot-protocol/whitenoise-rs/pull/468) hace el identificador del servicio de keyring configurable vía `WhitenoiseConfig`, y el [PR #475](https://github.com/marmot-protocol/whitenoise-rs/pull/475) unifica la implementación en un solo crate `keyring-core` con almacenes nativos de plataforma, reemplazando código fragmentado específico por plataforma. Por separado, el [PR #470](https://github.com/marmot-protocol/whitenoise-rs/pull/470) añade funcionalidad de búsqueda de usuarios.

### Marmot TS Extrae la App de Chat de Referencia

El SDK TypeScript de [Marmot](/es/topics/marmot/) ([marmot-ts](https://github.com/marmot-protocol/marmot-ts)) fusionó el [PR #40](https://github.com/marmot-protocol/marmot-ts/pull/40), eliminando la aplicación de chat de referencia integrada y separándola en un repositorio independiente: [marmots-web-chat](https://github.com/marmot-protocol/marmots-web-chat). El nuevo repositorio, creado el 6 de febrero, es implementación de referencia del SDK TypeScript de Marmot con su propio pipeline CI, vista de chat con pestañas y sistema de build independiente. La separación permite al SDK enfocarse en asuntos de biblioteca mientras la app de chat itera en UX de forma independiente.

Un PR abierto ([#41](https://github.com/marmot-protocol/marmot-ts/pull/41)) migra marmot-ts a ts-mls v2.0.0, trayendo API rediseñada con objetos de contexto unificados, nuevas utilidades de manejo de mensajes (creación de eventos, lectura, deserialización), helpers de metadatos de key package, y soporte de eventos de eliminación.

### Actualizaciones de Alby Hub

[Alby Hub](https://github.com/getAlby/hub) fusionó 5 PRs esta semana. La adición de Alby CLI a la interfaz de la tienda de apps llega en [PR #2049](https://github.com/getAlby/hub/pull/2049). El manejo de datos de zap inválidos en la lista de transacciones se corrige en [PR #2033](https://github.com/getAlby/hub/pull/2033), y el método `ListTransactions` no utilizado de la interfaz LNClient se elimina en [PR #2046](https://github.com/getAlby/hub/pull/2046).

### Notedeck Lanza Dashboard y Agentium

[Notedeck](https://github.com/damus-io/notedeck), el cliente Nostr multiplataforma de Damus, fusionó 6 PRs esta semana. La app de dashboard inicial llega en [PR #1247](https://github.com/damus-io/notedeck/pull/1247). Agentium, un entorno de desarrollo multi-agente que transforma el asistente de IA Dave en un sistema con modos de IA duales y gestión de agentes basada en escenas, se introduce en [PR #1293](https://github.com/damus-io/notedeck/pull/1293). Un compositor de mensajes multilínea con keybindings estilo Signal llega en [PR #1276](https://github.com/damus-io/notedeck/pull/1276), y mejoras de rendimiento de medios en [PR #1278](https://github.com/damus-io/notedeck/pull/1278). PRs abiertos a destacar incluyen [infraestructura outbox](https://github.com/damus-io/notedeck/pull/1288) y [planificación de App Git](https://github.com/damus-io/notedeck/pull/1289) [NIP-34](/es/topics/nip-34/).

### Agora Lanza Mayor Renovación de UI

[Agora](https://gitlab.com/soapbox-pub/agora) fusionó 7 PRs esta semana junto a su lanzamiento v1.0.2. El más grande es [PR #106](https://gitlab.com/soapbox-pub/agora/-/merge_requests/106), cerrando 11 tareas de UI en ajustes, edición de perfil, interacciones de mapa, resultados de búsqueda, filtrado de comentarios y gestión de servidor Blossom. La fusión desactivó botones de reacción para usuarios no autenticados (que antes obtenían fallos silenciosos al intentar reaccionar a posts en el mapa), corrigió el paneo de mapa en la línea de fecha, y añadió texto coincidente en negrita en resultados de búsqueda.

Conteos de comentarios bajo posts del feed y en páginas de hilos llegan en [PR #108](https://gitlab.com/soapbox-pub/agora/-/merge_requests/108). El reintento automático en fallos de carga de eventos con botón de recarga explícito cuando reintentos se agotan se añade en [PR #107](https://gitlab.com/soapbox-pub/agora/-/merge_requests/107). La navegación de hashtags pasa a alcance global por defecto en [PR #104](https://gitlab.com/soapbox-pub/agora/-/merge_requests/104), ya que el alcance por país anterior frecuentemente retornaba cero resultados.

Un paso CI que verifica paridad de traducción en todos los idiomas, fallando el build si alguna clave carece de valor, se incorpora en [PR #109](https://gitlab.com/soapbox-pub/agora/-/merge_requests/109). El recorte de notas grandes en feeds para preservar el ritmo de scroll llega en [PR #110](https://gitlab.com/soapbox-pub/agora/-/merge_requests/110), y la corrección de un problema de zoom en iOS móvil al comentar acciones causado por tamaños de fuente pequeños en [PR #111](https://gitlab.com/soapbox-pub/agora/-/merge_requests/111).

### Clawstr Lanza CLI y Botones de Lightning Zap

[Clawstr](https://gitlab.com/soapbox-pub/clawstr), la plataforma inspirada en Reddit donde agentes de IA crean y gestionan comunidades en Nostr, fusionó 3 PRs esta semana. En [PR #11](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/11), todos los comandos manuales de nak en definiciones de habilidades del agente de IA se reemplazan con el nuevo paquete `@clawstr/cli` (`npx -y @clawstr/cli@latest`), eliminando la construcción manual de eventos JSON a favor de comandos CLI y añadiendo operaciones de billetera (init, balance, zap, npc) y búsqueda de texto completo [NIP-50](/es/topics/nip-50/).

La página de documentación "Para Humanos" y el componente `ProfileZapDialog` llegan en [PR #13](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/13). El botón de zap aparece en páginas de perfil cuando el usuario tiene dirección Lightning configurada y funciona sin login, usando LNURL-pay directamente con cantidades preestablecidas de sats y visualización de código QR. La documentación del comando `wallet sync` en [PR #12](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/12) explica cómo pagos a direcciones Lightning son retenidos por NPC hasta que agentes sincronizan explícitamente sus billeteras.

## Actualizaciones de NIPs

Cambios recientes al [repositorio de NIPs](https://github.com/nostr-protocol/nips):

**Fusionados:**

- **[NIP-45: Respuesta HyperLogLog de Relay](https://github.com/nostr-protocol/nips/pull/1561)** - [NIP-45 (Conteo de Eventos)](/es/topics/nip-45/) ahora soporta conteo aproximado HyperLogLog (HLL). Relays pueden retornar valores de registro HLL de 256 bytes junto a respuestas COUNT. Al fusionar estos registros de múltiples relays, clientes computan cardinalidad aproximada sin descargar conjuntos completos de eventos. El caso de uso principal son conteos de seguidores y reacciones sin depender de un único relay como fuente autoritativa. Incluso dos eventos de reacción consumen más ancho de banda que el payload HLL de 256 bytes. Correcciones HyperLogLog++ mejoran la precisión en cardinalidades pequeñas.

- **[NIP-39: Etiquetas de Identidad Movidas del Kind 0](https://github.com/nostr-protocol/nips/pull/2216)** - Las etiquetas de claim de identidad (etiquetas `i`) de [NIP-39](/es/topics/nip-39/) han sido extraídas de eventos de metadatos kind 0 a un nuevo kind dedicado 10011. La razón: casi ningún cliente soporta estas etiquetas, por lo que añaden tamaño a cada consulta de kind 0 sin proporcionar valor. Primer PR de la serie de extracción del kind 0 de vitorpamplona (ver [sección de Noticias](#campaña-de-reducción-del-kind-0)).

**PRs Abiertos y Discusiones:**

- **[NIP-XX: Nostr Relay Connect (NRC)](https://github.com/nostr-protocol/nips/pull/2214)** - woikos propone un protocolo para acceder a relays Nostr a través de tunneling cifrado vía relay de rendez-vous público. El mecanismo permite acceso a relays detrás de NAT o firewalls, incluyendo relays personales ejecutándose en servidores domésticos o dispositivos móviles. El tunneling usa eventos kind 24891/24892 con cifrado [NIP-44](/es/topics/nip-44/) vía relay de rendez-vous que no puede descifrar el tráfico. Aplicación práctica: cualquier cliente Nostr puede exponer almacenamiento local (IndexedDB, SQLite) como endpoint de relay para sincronización entre dispositivos. La semántica estándar de NIP-01 (REQ, EVENT, CLOSE, COUNT) pasa a través del túnel de forma transparente. Existen implementaciones de referencia en Go (ORLY Relay) y TypeScript (Smesh).

- **[Nostr Web Tokens (NWT)](https://github.com/nostr-protocol/nips/pull/2187)** - pippellia-btc propone Nostr Web Tokens, formato de evento Nostr para transmitir claims firmados entre partes web, inspirado en JSON Web Tokens (JWTs). NWT puede representar tanto [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) (HTTP Auth) como [eventos de autorización Blossom](/es/topics/blossom/), dando a clientes flexibilidad en cómo y por cuánto tiempo los tokens permanecen válidos. Hay biblioteca de referencia en Go disponible. La [explicación en video](https://github.com/pippellia-btc/nostr-web-tokens) y la [comparación detallada](https://github.com/pippellia-btc/nostr-web-tokens?tab=readme-ov-file#comparisons) con NIP-98 y Blossom Auth están enlazadas en el PR.

- **[Simplificación de NIP-47](https://github.com/nostr-protocol/nips/pull/2210)** - rolznz propone eliminar los métodos `multi_` de [NIP-47 (Nostr Wallet Connect)](/es/topics/nip-47/), que eran complejos de implementar y no ganaron adopción. El PR reduce duplicación en cifrado y manejo de compatibilidad hacia atrás, limpiando la spec tras la [adición de facturas hold de la semana pasada](/es/newsletters/2026-02-04-newsletter/#actualizaciones-de-nips).

- **[NIP-05: Mover a Kind de Evento Propio](https://github.com/nostr-protocol/nips/pull/2213)** - vitorpamplona propone mover la verificación NIP-05 del kind 0 a nuevo kind 10008, habilitando múltiples identificadores NIP-05 por usuario y filtrado por dirección NIP-05. Parte de la campaña de reducción del kind 0.

- **[NIP-57: Direcciones Lightning del Kind 0](https://github.com/nostr-protocol/nips/pull/2217)** - vitorpamplona propone extraer lud06/lud16 (direcciones Lightning) del kind 0 a kind de evento dedicado según [NIP-57](/es/topics/nip-57/), continuando el esfuerzo de reducción del kind 0.

- **[Hiperpersonalización de Perfiles](https://github.com/nostr-protocol/nips/pull/2165)** - fiatjaf propone capacidades extendidas de personalización de perfil más allá de lo que el kind 0 soporta actualmente.

## Análisis Profundo de NIP: NIP-45 (Conteo de Eventos) y HyperLogLog

[NIP-45](/es/topics/nip-45/) ([spec](https://github.com/nostr-protocol/nips/blob/master/45.md)) define cómo clientes pueden pedir a relays que cuenten eventos que coincidan con un filtro sin transferir los eventos en sí. La fusión de [soporte HyperLogLog](https://github.com/nostr-protocol/nips/pull/1561) esta semana añade estructura de datos probabilística que resuelve un problema fundamental: cómo contar cosas a través de múltiples relays independientes.

**El Problema:**

Contar eventos en un único relay es simple: envía solicitud COUNT, recibe un número. Contar a través de la red es más difícil. Si el relay A reporta 50 reacciones y el relay B reporta 40, el total no es 90 porque muchos eventos existen en ambos relays. Al no descargar todos los eventos para deduplicar, el cliente no puede calcular el conteo real.

**HyperLogLog:**

HyperLogLog (HLL) es un algoritmo probabilístico que estima el número de elementos distintos en un conjunto usando cantidad fija de memoria. La implementación de NIP-45 usa 256 registros de un byte cada uno, consumiendo exactamente 256 bytes sin importar cuántos eventos se cuenten. El algoritmo funciona examinando la representación binaria de cada ID de evento y rastreando la posición de ceros iniciales. Eventos cuyos IDs comienzan con muchos ceros son estadísticamente raros, por lo que su ocurrencia indica un conjunto grande.

**Cómo Funciona en NIP-45:**

Un relay que responde a solicitud COUNT puede incluir un campo `hll` conteniendo valores de registro codificados en base64:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

El cliente recolecta valores HLL de múltiples relays y los fusiona tomando el valor máximo en cada posición de registro. El HLL fusionado representa la unión de todos los conjuntos de eventos a través de relays, manejando la deduplicación automáticamente. La estimación final de cardinalidad se calcula a partir de registros fusionados.

**Precisión:**

El error estándar con 256 registros es aproximadamente 5.2%. Para un conteo real de 1,000, la estimación típicamente caerá entre 948 y 1,052. Para conteos más grandes, el error relativo se mantiene constante: un conteo real de 100,000 estimará aproximadamente entre 94,800 y 105,200. Correcciones HyperLogLog++ mejoran la precisión para cardinalidades pequeñas (menores a ~200), donde el algoritmo básico tiende a sobreestimar.

**Por Qué Importa:**

Métricas sociales (conteos de seguidores, conteos de reacciones, conteos de reposts) son función central de clientes de redes sociales. El cliente que no cuente con HLL debe consultar un único relay "de confianza" (centralizando el conteo) o descargar todos los eventos de todos los relays (desperdiciando ancho de banda). HLL permite obtener buen conteo aproximado de múltiples relays con overhead total de 256 bytes por relay, sin importar el conteo real. Incluso dos eventos de reacción consumen más ancho de banda que un payload HLL completo.

La spec fija el número de registros en 256 para interoperabilidad. Todos los relays producen valores HLL que clientes pueden fusionar, sin importar qué implementación de relay ejecuten. Esta estandarización significa que el cliente puede implementar soporte HLL una vez y beneficiarse de cada relay que lo soporte.

**Estado Actual:**

El PR fue abierto por fiatjaf y había estado en discusión durante varios meses antes de fusionarse esta semana. Implementaciones de relay necesitarán añadir computación HLL a sus manejadores COUNT. Implementaciones de clientes necesitarán añadir fusión HLL a su lógica de agregación de conteos.

## Análisis Profundo de NIP: NIP-96 (Almacenamiento de Archivos HTTP) y la Transición a Blossom

[NIP-96](/es/topics/nip-96/) ([spec](https://github.com/nostr-protocol/nips/blob/master/96.md)) definió cómo clientes Nostr suben, descargan y gestionan archivos en servidores de medios HTTP. Ahora marcado como "no recomendado" en favor de [Blossom](/es/topics/blossom/) (alojamiento de medios basado en BUD), NIP-96 sigue siendo relevante esta semana porque Angor v0.2.5 [añadió configuración de servidor NIP-96](#angor-v025) y ZSP v0.3.1 [sube a servidores Blossom](#zsp-v031), ilustrando la transición de protocolo en curso.

**Cómo Funciona NIP-96:**

El cliente descubre las capacidades de un servidor de archivos consultando `/.well-known/nostr/nip96.json`, que retorna la URL de API, tipos de contenido soportados, límites de tamaño y transformaciones de medios disponibles:

```json
{
  "api_url": "https://file-server.example/api",
  "download_url": "https://cdn.example/files",
  "content_types": ["image/jpeg", "video/webm", "audio/*"],
  "plans": {
    "free": {
      "is_nip98_required": true,
      "max_byte_size": 10485760,
      "media_transformations": {
        "image": ["resizing"]
      }
    }
  }
}
```

Para subir, el cliente envía POST `multipart/form-data` a la URL de API con cabecera de autorización [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) (evento Nostr firmado que prueba la identidad del uploader). El servidor retorna estructura de metadatos de archivo [NIP-94](/es/topics/nip-94/) conteniendo la URL del archivo, hashes SHA-256 original y transformado, tipo MIME y dimensiones:

```json
{
  "status": "success",
  "nip94_event": {
    "tags": [
      ["url", "https://cdn.example/files/<hash>.png"],
      ["ox", "<original-file-hash>"],
      ["x", "<transformed-file-hash>"],
      ["m", "image/png"],
      ["dim", "800x600"]
    ]
  }
}
```

Las descargas usan solicitudes GET a `<api_url>/<sha256-hash>`, con parámetros de consulta opcionales para transformaciones del lado del servidor como redimensionamiento de imágenes (`?w=320`). La eliminación usa DELETE con auth NIP-98, y solo el uploader original puede eliminar sus archivos. Un endpoint de listado retorna resultados paginados de subidas del usuario.

Cada usuario declara sus servidores de subida preferidos publicando eventos kind 10096, permitiendo a clientes seleccionar automáticamente el servidor correcto sin configuración manual.

**Por Qué Fue Obsoletado:**

NIP-96 ataba URLs de archivos a servidores específicos. Si `files.example.com` dejaba de funcionar, cada nota Nostr que referenciaba las URLs de ese servidor perdía sus medios. El servidor era la dirección, y la dirección era frágil.

[Blossom](/es/topics/blossom/) (Blobs Stored Simply on Mediaservers) invierte esto haciendo del hash SHA-256 del contenido del archivo el identificador canónico. Una URL de Blossom luce como `https://blossom.example/<sha256>.png`, pero cualquier servidor Blossom que aloje el mismo archivo lo sirve en la misma ruta de hash. Si un servidor desaparece, el cliente consulta otro servidor por el mismo hash. El direccionamiento por contenido hace datos portables entre servidores por defecto.

Blossom simplifica la API. NIP-96 usaba subidas multipart form con respuestas JSON, políticas de transformación y endpoint de descubrimiento. Blossom usa PUT simple para subidas, GET para descargas y eventos Nostr firmados (no cabeceras HTTP) para autorización. La especificación de Blossom se divide en documentos modulares: BUD-01 cubre protocolo de servidor, autorización y recuperación, BUD-02 cubre subida de blobs, BUD-03 cubre servidores de usuarios, y BUD-04 cubre espejeo entre servidores.

La obsolescencia ocurrió en septiembre 2025 vía [PR #2047](https://github.com/nostr-protocol/nips/pull/2047), que marcó NIP-96 como "no recomendado" en el índice de NIPs.

**La Transición en la Práctica:**

Servidores como nostr.build y void.cat soportaban NIP-96 y han añadido o migrado a endpoints Blossom. Cada cliente está en distinta etapa de adopción. El lanzamiento v0.2.5 de Angor esta semana añadió configuración de servidor NIP-96 para imágenes de proyecto, mientras el lanzamiento v0.3.1 de ZSP sube artefactos exclusivamente a servidores Blossom con cabeceras `Content-Digest` para cumplimiento del protocolo. Amethyst y Primal soportan subidas Blossom. La coexistencia probablemente continuará hasta que implementaciones restantes de NIP-96 completen su migración.

**Qué Se Mantiene:**

Eventos kind 10096 de preferencia de servidor siguen siendo útiles para la selección de servidor Blossom. Metadatos de archivo NIP-94 (eventos kind 1063) siguen describiendo propiedades de archivos con independencia de qué protocolo de subida los creó. El hashing SHA-256 que NIP-96 usaba para URLs de descarga se convirtió en la base del direccionamiento por contenido de Blossom. El diseño de NIP-96 informó lo que Blossom simplificó: la lección fue que el alojamiento de medios en red descentralizada requiere almacenamiento direccionado por contenido para igualar la resistencia a la censura de la capa de relays.

---

Eso es todo por esta semana. Envíanos noticias, sugerencias de cobertura o información sobre tu proyecto. <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Escríbenos vía DM NIP-17</a> o encuéntranos en Nostr.
