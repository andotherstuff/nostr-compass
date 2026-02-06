---
title: 'Nostr Compass #7'
date: 2026-01-28
translationOf: /en/newsletters/2026-01-28-newsletter.md
translationDate: 2026-01-28
draft: false
type: newsletters
---

Bienvenido de nuevo a Nostr Compass, tu guía semanal de Nostr.

**Esta semana:** Ridestr trae viajes compartidos descentralizados a Nostr con pagos en [Cashu](/es/topics/cashu/) y ubicación cifrada compartida. Pomade introduce recuperación basada en correo electrónico para firmantes multisig. Damus lanza [negentropy](/es/topics/negentropy/) para sincronización confiable de mensajes directos. La aplicación de escritorio de Amethyst añade búsqueda, marcadores y zaps. Amber v4.1.1 muestra puntuaciones de confianza de relays. Marmot fusiona MIP-03 y construye una aplicación de chat de referencia en TypeScript. diVine añade autenticación QR mediante [NIP-46](/es/topics/nip-46/) y soporte para menciones. Nuevas propuestas de NIP abordan la gestión de comunidades, sincronización basada en secuencias y almacenamiento cifrado de archivos. También echamos un vistazo a cinco años de eneros en Nostr, trazando la evolución del protocolo desde un puñado de primeros adoptantes en 2021 hasta el lanzamiento explosivo de Damus en la App Store en 2023 y el ecosistema de clientes madurando en 2025.

## Noticias

### Ridestr Trae Viajes Compartidos Descentralizados a Nostr

[Ridestr](https://github.com/variablefate/ridestr) está desarrollando una aplicación de viajes compartidos peer-to-peer construida completamente sobre Nostr, permitiendo transacciones directas entre conductores y pasajeros con pagos en Bitcoin y [Cashu](/es/topics/cashu/). El protocolo utiliza tipos de eventos personalizados (30173, 3173-3175, 30180/30181) para coordinar viajes mientras mantiene la privacidad a través de divulgación progresiva de ubicación y cifrado [NIP-44](/es/topics/nip-44/).

El sistema funciona mediante un flujo cuidadosamente coreografiado: los conductores transmiten disponibilidad usando ubicaciones codificadas en geohash (~5km de precisión) mediante eventos kind 30173, los pasajeros solicitan viajes con estimaciones de tarifa a través de kind 3173, y los pagos se aseguran usando tokens de depósito HTLC antes de que comience el viaje. La privacidad de ubicación se preserva mediante divulgación progresiva, donde los detalles de recogida solo se revelan cuando los conductores llegan y los destinos se comparten después de la verificación del PIN. Toda la comunicación entre las partes usa cifrado [NIP-44](/es/topics/nip-44/) para privacidad.

Ridestr implementa seguridad de pagos a través de depósito HTLC con firmas P2PK. Cuando un pasajero acepta la oferta de un conductor, bloquea tokens [Cashu](/es/topics/cashu/) con un hash de pago que solo el conductor puede reclamar después de completar el viaje. El protocolo actualmente opera con arquitectura de mint único, requiriendo que pasajeros y conductores usen el mismo mint de [Cashu](/es/topics/cashu/). La implementación Android basada en Kotlin del proyecto maneja verificación de pruebas y recuperación de pruebas obsoletas a través de verificaciones de estado NUT-07.

Ridestr aborda desafíos que la mayoría de las aplicaciones Nostr evitan: coordinación de ubicación en tiempo real, depósito de pagos con resolución de disputas y sistemas de reputación para interacciones en el mundo físico. El proyecto está en beta y demuestra que el modelo de eventos de Nostr puede soportar mercados de servicios peer-to-peer, no solo compartir contenido.

### Pomade Lanza Sistema de Recuperación Alpha para Firmantes Multisig

[Pomade](https://github.com/coracle-social/pomade), desarrollado por hodlbod, se construye sobre el ecosistema existente de [FROSTR](https://github.com/FROSTR-ORG) para proporcionar un servicio de firma de umbral enfocado en la recuperación. Usando firmas [FROST](/es/topics/frost/) (Flexible Round-Optimized Schnorr Threshold) a través de la biblioteca @frostr/bifrost, Pomade añade flujos de recuperación basados en correo electrónico sobre la criptografía de umbral. El sistema fragmenta la clave secreta del usuario usando Shamir Secret Sharing, distribuyendo fragmentos a través de múltiples firmantes independientes con un umbral configurable (2-de-3, 3-de-5, etc.).

El protocolo opera completamente sobre Nostr usando un único tipo de evento (28350) con cargas útiles cifradas con [NIP-44](/es/topics/nip-44/). Al firmar, el cliente solicita firmas parciales de al menos `threshold` firmantes, luego las agrega en una firma Schnorr válida. Para cifrado, los firmantes colaboran para derivar secretos compartidos vía ECDH sin que ninguna parte individual conozca la clave completa.

La recuperación funciona a través de dos métodos de autenticación: basado en contraseña (usando argon2id con la pubkey del firmante como sal) o OTP por correo electrónico. Para prevenir ataques MITM durante la recuperación OTP, cada firmante genera su propio código de verificación con un prefijo proporcionado por el cliente, requiriendo que los usuarios se autentiquen independientemente con cada firmante. El protocolo requiere prueba de trabajo en eventos de registro (20+ bits según [NIP-13](/es/topics/nip-13/)) para prevenir spam.

El modelo de confianza es explícito: si `threshold` firmantes se confabulan, pueden robar la clave. Los proveedores de correo electrónico tienen confianza total ya que pueden interceptar OTPs. Los usuarios no pueden recuperar independientemente su clave secreta completa; hacerlo requiere cooperación de `threshold` firmantes. El protocolo está diseñado para incorporar nuevos usuarios no familiarizados con la gestión de claves, con la recomendación explícita de que los usuarios migren a auto-custodia una vez cómodos. Pomade advierte sobre potencial "pérdida de claves, robo, denegación de servicio o fuga de metadatos" dado su estado alpha no auditado.

## Lanzamientos

### Damus Lanza Negentropy para Sincronización Confiable de DMs

[Damus v1.13](https://github.com/damus-io/damus/tree/v1.13) lanza la implementación de negentropy [que previsualizamos como PR abierto la semana pasada](/es/newsletters/2026-01-21-newsletter/#damus-ios-client---open-prs). [PR #3536](https://github.com/damus-io/damus/pull/3536) añade soporte base de [negentropy](/es/topics/negentropy/) a la capa de red, habilitando reconciliación de conjuntos con relays que soportan el protocolo. Un [PR #3547](https://github.com/damus-io/damus/pull/3547) complementario añade sincronización de DMs al deslizar para refrescar que usa negentropy para recuperar mensajes faltantes cuando las suscripciones REQ estándar fallan.

La implementación sigue un enfoque conservador: la carga normal de DMs continúa sin cambios, con [negentropy](/es/topics/negentropy/) disponible como mecanismo de recuperación cuando los usuarios refrescan manualmente. Las pruebas automatizadas demuestran la corrección generando un DM con una marca de tiempo antigua que las consultas estándar perderían, luego usando sincronización [negentropy](/es/topics/negentropy/) para recuperarlo exitosamente. Aunque el soporte de [negentropy](/es/topics/negentropy/) requiere relays compatibles, la implementación maneja elegantemente entornos de relays mixtos usando el protocolo donde esté disponible.

### Amber v4.1.1 - Puntuaciones de Confianza de Relays

[Amber v4.1.1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.1) lanza la visualización de puntuaciones de confianza de relays ([PR #289](https://github.com/greenart7c3/Amber/pull/289)), implementando los conceptos de evaluación de relays discutidos en [la cobertura de Trusted Relay Assertions de la semana pasada](/es/newsletters/2026-01-21-newsletter/#nip-updates). Las puntuaciones de confianza ahora aparecen en la página de Relays y para solicitudes de conexión NostrConnect, ayudando a los usuarios a evaluar la confiabilidad de relays antes de autorizar conexiones. El lanzamiento también incluye una interfaz rediseñada de login/eventos/permisos y soporte para el método `switch_relays`. Las mejoras de rendimiento almacenan en caché las operaciones de keystore, abordando reportes de tiempos de carga de 20+ segundos en dispositivos antiguos.

### nak v0.18.2 - Integración MCP

[nak](https://github.com/fiatjaf/nak) (Nostr Army Knife) de fiatjaf [v0.18.2](https://github.com/fiatjaf/nak/releases/tag/v0.18.2) añade soporte para [Model Context Protocol](https://nostrify.dev/mcp) vía `nak mcp`, permitiendo a agentes de IA buscar personas en Nostr, publicar notas, mencionar usuarios y leer contenido usando el modelo outbox. El lanzamiento también introduce un [instalador de una línea](https://github.com/fiatjaf/nak/blob/master/install.sh) (`curl -sSL https://raw.githubusercontent.com/fiatjaf/nak/master/install.sh | sh`) que descarga binarios pre-compilados, eliminando el requisito de la cadena de herramientas Go para usuarios finales. El modo bunker ahora soporta sockets Unix y `switch_relays`.

### Zeus v0.12.2 Beta - Correcciones NWC

[Zeus v0.12.2-beta1](https://github.com/ZeusLN/zeus/releases) lanza múltiples correcciones NWC abordando problemas cubiertos en [la cobertura de Zeus de la semana pasada](/es/newsletters/2026-01-21-newsletter/#zeus-lightning-wallet-with-nostr-wallet-connect).

## Actualizaciones de Proyectos

### Amethyst Desktop - Fase 2A Lanzada

[Amethyst](https://github.com/vitorpamplona/amethyst) lanzó [la Fase 2A de su aplicación de escritorio](https://github.com/vitorpamplona/amethyst/pull/1676), añadiendo Búsqueda, Marcadores, Zaps, vistas de Hilos y contenido de formato largo (Lecturas) a la experiencia de escritorio. Un [PR #1683](https://github.com/vitorpamplona/amethyst/pull/1683) complementario añade retroalimentación transparente de transmisión de eventos para que los usuarios ahora vean el estado por relay en tiempo real mientras sus eventos se propagan a través de la red, facilitando el diagnóstico de problemas de conectividad.

### Progreso de Notedeck: Aplicación de Calendario y Pulido de UX

El cliente de escritorio [Notedeck](https://github.com/damus-io/notedeck) del equipo Damus fusionó el comportamiento de auto-ocultar barra de herramientas ([PR #1268](https://github.com/damus-io/notedeck/pull/1268)) que responde a la velocidad de desplazamiento para más espacio de pantalla en vistas móviles. Un [borrador PR #1271](https://github.com/damus-io/notedeck/pull/1271) añade una aplicación completa de Calendario [NIP-52](/es/topics/nip-52/) con vistas de mes/semana/día/agenda, soporte RSVP y comentarios [NIP-22](/es/topics/nip-22/) en eventos de calendario, actualmente con feature-flag para pruebas.

### Jumble Añade Modo Comunidad

[Jumble](https://github.com/CodyTseng/jumble), el cliente web enfocado en relays, añadió [modo comunidad](https://github.com/CodyTseng/jumble/pull/738) y soporte para [presets de conjuntos de relays vía variables de entorno](https://github.com/CodyTseng/jumble/pull/736), facilitando el despliegue de instancias temáticas como [nostr.moe](https://nostr.moe/).

### Panel de Órdenes de Shopstr

[Shopstr](https://github.com/shopstr-eng/shopstr) reemplazó su gestión de órdenes basada en chat con un [Panel de Órdenes](https://github.com/shopstr-eng/shopstr/pull/219) dedicado. La nueva interfaz proporciona una vista centralizada para que los comerciantes rastreen el estado de órdenes, marquen mensajes como leídos y gestionen el cumplimiento sin desplazarse por hilos de chat. La actualización deprecia el caché IndexedDB en favor de APIs de estado de órdenes del lado del servidor y revisa cómo se etiquetan los DMs de órdenes para mejor filtrado.

### Formstr Añade Preguntas en Cuadrícula

[Formstr](https://github.com/abh3po/nostr-forms), la aplicación de formularios nativa de Nostr, añadió [preguntas en cuadrícula](https://github.com/abh3po/nostr-forms/pull/419) y [reescribió su SDK](https://github.com/abh3po/nostr-forms/pull/410) con soporte para incrustación. Una [corrección para firmantes no-[NIP-07](/es/topics/nip-07/)](https://github.com/abh3po/nostr-forms/pull/418) resolvió problemas para usuarios con bunker o firmantes locales intentando enviar formularios con su identidad.

### nostr-tools Actualiza Dependencias Criptográficas

[nostr-tools](https://github.com/nbd-wtf/nostr-tools), la biblioteca principal de JavaScript, [actualizó a @noble/curves v2.0.1](https://github.com/nbd-wtf/nostr-tools/pull/520), abordando cambios de API incompatibles en 27 archivos y adoptando las últimas bibliotecas noble auditadas. fiatjaf también añadió soporte `switch_relays` a [NIP-46](/es/topics/nip-46/), permitiendo a clientes bunker cambiar conexiones de relay dinámicamente.

### Zeus Trabajando en Reseñas de Mints NIP-87

[Zeus](https://github.com/ZeusLN/zeus) tiene un [PR abierto para reseñas de mints [NIP-87](/es/topics/nip-87/)](https://github.com/ZeusLN/zeus/pull/3576), permitiendo a los usuarios descubrir y reseñar mints de [Cashu](/es/topics/cashu/) filtrados por seguidos de Nostr. Las reseñas incluyen calificaciones con estrellas y pueden enviarse anónimamente o con el nsec del usuario.

### Camelus Lanza Soporte Completo de DM

[Camelus](https://github.com/camelus-hq/camelus), un cliente Android basado en Flutter construido con Dart NDK para rendimiento móvil eficiente en batería, añadió mensajería directa completa con más de 20 commits esta semana. La actualización incluye categorías de chat, fechas de mensajes, interfaz de envío optimista, funcionalidad de nota para uno mismo y manejo adecuado de relays de DM.

### Actualizaciones del Protocolo Marmot

La resolución determinista de commits MIP-03 [que cubrimos como PR abierto la semana pasada](/es/newsletters/2026-01-21-newsletter/#marmot-protocol-white-noise-encrypted-group-chat-library) ahora se ha fusionado. [MDK PR #152](https://github.com/marmot-protocol/mdk/pull/152) asegura que todos los chats grupales basados en [MLS](/es/topics/mls/) converjan al mismo estado cuando llegan múltiples commits válidos para la misma época.

Un [PR de especificación #28](https://github.com/marmot-protocol/marmot/pull/28) complementario añade requisitos de ciclo de vida de init_key abordando vacíos de las auditorías de implementación: el material de clave privada de mensajes Welcome debe ser eliminado de forma segura después del procesamiento (zerización, limpieza de almacenamiento), y los nuevos miembros deben realizar auto-actualizaciones dentro de 24 horas para secreto hacia adelante.

El SDK de TypeScript ([marmot-ts](https://github.com/marmot-protocol/marmot-ts)) está construyendo una aplicación de chat de referencia. [PR #37](https://github.com/marmot-protocol/marmot-ts/pull/37) añade creación/listado de grupos, gestión de paquetes de claves con flujos de publicar/transmitir/eliminar, e invitaciones por código QR. Un [PR abierto #38](https://github.com/marmot-protocol/marmot-ts/pull/38) por hzrd149 implementa persistencia de historial de mensajes con paginación. El backend whitenoise-rs fusionó 15 PRs esta semana incluyendo soporte multi-idioma ([PR #455](https://github.com/marmot-protocol/whitenoise-rs/pull/455)) y referencias de medios MIP-04 v2 ([PR #450](https://github.com/marmot-protocol/whitenoise-rs/pull/450)).

### diVine Añade Funciones de Integración con Nostr

[diVine](https://github.com/divinevideo/divine-mobile), la aplicación de video de formato corto, continúa la rápida integración con Nostr.

Los PRs abiertos incluyen autenticación por código QR [NIP-46](/es/topics/nip-46/) ([PR #1019](https://github.com/divinevideo/divine-mobile/pull/1019)) y mensajería directa cifrada [NIP-17](/es/topics/nip-17/) ([PR #834](https://github.com/divinevideo/divine-mobile/pull/834)). La actividad de esta semana se centró en [soporte de menciones](https://github.com/divinevideo/divine-mobile/pull/1098) convirtiendo URIs `nostr:` y @menciones a enlaces de perfil clicables, [avatares de respaldo de Classic Viners](https://github.com/divinevideo/divine-mobile/pull/1097) usando perfiles de Nostr, y herramientas de edición de video incluyendo [dibujo](https://github.com/divinevideo/divine-mobile/pull/1056), [filtros](https://github.com/divinevideo/divine-mobile/pull/1053) y [stickers](https://github.com/divinevideo/divine-mobile/pull/1050).

## Actualizaciones de NIPs

Cambios recientes al [repositorio de NIPs](https://github.com/nostr-protocol/nips):

**Fusionados:**

- **[Trusted Relay Assertions](https://github.com/nostr-protocol/nips/pull/1534)** - La propuesta para estandarizar puntuaciones de confianza de relays [que cubrimos la semana pasada](/es/newsletters/2026-01-21-newsletter/#nip-updates) fue fusionada. La especificación define eventos kind 30385 para aserciones de confianza de relay con puntuación en fiabilidad, calidad y accesibilidad. La discusión previa a la fusión se centró en si las puntuaciones de confianza deben ser "globales" (calculadas una vez para todos los usuarios) o "personalizadas" (relativas al grafo social de cada observador). Algoritmos estilo PageRank como [Trust Rank de nostr.band](https://trust.nostr.band/) y [GrapeRank](https://github.com/Pretty-Good-Freedom-Tech/graperank-nodejs) resisten ataques sybil dividiendo cualquier rango pasado a través de cuentas falsas por el tamaño de la granja de bots.

**PRs Abiertos y Discusiones:**

- **Communikeys** - Una [propuesta comprehensiva](https://nostrhub.io) para gestión de comunidades que usa npubs existentes como identificadores de comunidad en lugar de enfoques basados en relays. Cualquier npub puede convertirse en comunidad publicando un evento kind 10222; las publicaciones apuntan a comunidades vía eventos kind 30222. El control de acceso usa badges [NIP-58](/es/topics/nip-58/), permitiendo gestión de membresía delegada con almacenamiento frío para claves de comunidad.

- **[NIP-CF: Changes Feed](https://github.com/nostr-protocol/nips/pull/2196)** - Un borrador proponiendo sincronización de eventos basada en secuencia como alternativa a filtros `since` basados en marcas de tiempo. El problema: la sincronización estándar de Nostr usando marcas de tiempo `since` puede perder eventos cuando múltiples eventos comparten la misma marca de tiempo con precisión de segundo, los relojes del cliente y relay divergen, o el checkpointing es impreciso. NIP-CF resuelve esto haciendo que los relays asignen números de secuencia monotónicamente crecientes a eventos almacenados, proporcionando ordenamiento total estricto. Los clientes solicitan cambios desde un número de secuencia específico y reciben eventos en orden garantizado, con checkpointing preciso que nunca pierde eventos. La propuesta también soporta modo en vivo/continuo donde las suscripciones permanecen abiertas después de la sincronización inicial para actualizaciones en tiempo real.

- **[NIP-XX: Encrypted File Sync](https://github.com/nostr-protocol/nips/pull/1947)** - Un protocolo que define kinds 30800 (archivos cifrados), 30801 (índices de bóveda) y 30802 (documentos compartidos) para sincronizar contenido cifrado entre dispositivos usando relays de Nostr. El protocolo permite que aplicaciones de toma de notas local-first proporcionen sincronización cifrada de extremo a extremo sin servidores centralizados. Los contenidos de archivos, rutas, nombres y estructura de carpetas están todos cifrados usando auto-cifrado [NIP-44](/es/topics/nip-44/), por lo que los relays almacenan blobs que no pueden leer. Los adjuntos binarios como imágenes usan servidores [Blossom](/es/topics/blossom/) con cifrado del lado del cliente. Kind 30802 permite compartir documentos entre usuarios cifrando a la clave pública del destinatario.

## Cinco Años de Eneros en Nostr

[El newsletter del mes pasado](/es/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers) trazó los hitos de diciembre de Nostr desde el primer lanzamiento de cliente de fiatjaf hasta la donación catalítica de Jack Dorsey. Esta retrospectiva registra lo que sucedió cada enero desde 2021 hasta 2025, enfocándose en desarrollos técnicos verificados.

### Enero 2021: Desarrollo Temprano

El tercer mes de Nostr vio desarrollo continuo en Branle, el cliente Vue.js de fiatjaf que se había lanzado en diciembre de 2020. Un pequeño grupo de primeros adoptantes, probablemente menos de 15 personas, se coordinaban a través del grupo de Telegram [@nostr_protocol](https://t.me/nostr_protocol) (creado el 16 de noviembre de 2020), probando el protocolo en uno o dos relays experimentales. El cliente de línea de comandos noscl proporcionaba interacción basada en terminal.

La base técnica ya estaba establecida: usuarios identificados por claves públicas secp256k1, publicaciones firmadas criptográficamente con firmas Schnorr, y relays sirviendo como almacenamiento simple que no se comunican entre sí. Esta fue criptografía deliberadamente nativa de Bitcoin, una elección de diseño que moldearía patrones de adopción años después.

### Enero 2022: Descubrimiento por Desarrolladores

Enero 2022 abrió con Nostr todavía vibrando por su [primera aparición en Hacker News](https://news.ycombinator.com/item?id=29749061) (31 de diciembre de 2021), que generó 110 puntos y 138 comentarios. Al momento de esa publicación, solo alrededor de siete relays alimentaban toda la red, con comentaristas notando que "el spam no es un problema todavía porque nostr es súper nuevo y nadie lo usa aún". Robert C. Martin ("Uncle Bob") había respaldado a Nostr como potencialmente "la solución final para comunicación social". La discusión continuó en enero, con desarrolladores debatiendo arquitectura de relays versus P2P verdadero, resistencia a la censura versus moderación, y si la simplicidad podría escalar.

La publicación de HN provocó una ola de nuevas implementaciones. El mismo Uncle Bob comenzó [more-speech](https://github.com/unclebob/more-speech), un cliente de escritorio Clojure, el 18 de enero. La biblioteca [go-nostr](https://github.com/nbd-wtf/go-nostr) de fiatjaf (creada en enero 2021) y el cliente de línea de comandos [noscl](https://github.com/fiatjaf/noscl) proporcionaban herramientas Go, mientras [nostr-tools](https://github.com/nbd-wtf/nostr-tools) ofrecía soporte JavaScript. Para diciembre 2022, aproximadamente 800 perfiles tenían biografías. Branle seguía siendo el cliente web principal, recibiendo actualizaciones incluyendo importación de clave privada y soporte multi-relay. Los desafíos técnicos eran evidentes: las claves hexadecimales de 64 caracteres resultaban poco intuitivas, los retrasos de mensajes frustraban a los usuarios, y la comunidad cuestionaba si la arquitectura podría manejar tráfico a escala de Twitter.

### Enero 2023: El Despegue

Enero 2023 transformó a Nostr de experimento a movimiento. Damus, el cliente iOS de William Casarin (jb55), luchó contra el proceso de aprobación de la App Store de Apple. Rechazado el 1 de enero, rechazado de nuevo el 26 de enero, fue finalmente [aprobado el 31 de enero](https://www.coindesk.com/tech/2023/02/01/decentralized-social-media-project-nostrs-damus-gets-listed-on-apple-app-store). Esa aprobación desencadenó una cascada: Damus alcanzó inmediatamente el #10 en Redes Sociales de EE.UU. Jack Dorsey [lo llamó](https://web.archive.org/web/20240304043638/https://www.theblock.co/post/207448/nostr-based-decentralized-twitter-alternative-damus-goes-live-on-apple-app-store) "un hito para los protocolos abiertos".

Ocho días antes, el 23 de enero, [Edward Snowden anunció](https://x.com/Snowden/status/1617623779626352640) su presencia en Nostr: "Una de las cosas geniales de Nostr... más allá de la resistencia a la censura, es que no estás limitado a 280 caracteres". Su respaldo como denunciante de la NSA tenía peso en círculos conscientes de la privacidad, y los usuarios inmediatamente comenzaron a enviarle zaps de sats vía Lightning.

Los clientes web competían para incorporar la afluencia. [Snort](https://github.com/v0l/snort), creado por kieran en diciembre 2022, emergió como un cliente React repleto de funciones; el 13 de enero, Snort integró registro NIP-05 vía la API de Nostr Plebs, permitiendo a nuevos usuarios reclamar identidades legibles por humanos durante la incorporación. [Iris](https://iris.to), desarrollado a tiempo completo por Martti Malmi (un colaborador temprano de Bitcoin que recibió la segunda transacción de Bitcoin de Satoshi), ofrecía interfaces web y móvil con identidades NIP-05 gratuitas en iris.to. [Astral](https://github.com/monlovesmango/astral), construido por monlovesmango con Quasar (Vue.js) como fork de Branle, se enfocaba en gestión de relays con su función de agrupación de relays que permitía a usuarios organizar relays en conjuntos para publicación y filtrado. Las betas de TestFlight para clientes iOS se llenaban en horas, y Amethyst dominaba Android.

La infraestructura luchaba por mantener el ritmo. Todos los relays eran operados por entusiastas pagando de su bolsillo. Los relays de pago usando micropagos Lightning creaban filtrado natural de spam pero introducían fricción de acceso. [Damus fue retirado de la App Store de China](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/) solo dos días después de la aprobación, supuestamente por solicitud del principal vigilante de internet de China.

### Enero 2024: Endurecimiento del Protocolo

Enero 2024 se enfocó en estandarización del protocolo y construcción de comunidad. [Nostr PHX](https://www.nostrphx.com/events) inició el año con un meetup el 5 de enero en Phoenix, reuniendo a cypherpunks locales. Este fue el primero de muchos eventos comunitarios ese año incluyendo BTC Prague (junio), Nostriga en Riga (agosto), y Nostrasia.

El desarrollo de protocolo más significativo fue [NIP-59 (Gift Wrap)](https://github.com/nostr-protocol/nips/pull/716) siendo fusionado el 29 de enero, proporcionando protección de metadatos para comunicaciones cifradas. Gift Wrap se construye sobre el [estándar de cifrado NIP-44](https://github.com/paulmillr/nip44) (que había sido [auditado por Cure53](https://cure53.de/audit-report_nip44-implementations.pdf) en diciembre 2023) para ocultar la identidad del remitente de los relays. El protocolo envuelve mensajes cifrados dentro de un evento exterior firmado por un par de claves aleatorio de uso único. Los relays solo ven la pubkey desechable, mientras la identidad real del remitente está enterrada en la carga útil cifrada que solo el destinatario puede descifrar. Esto previene que operadores de relays y observadores de red aprendan quién está enviando mensajes a quién. Las marcas de tiempo también pueden aleatorizarse para derrotar análisis de timing.

El ecosistema se expandió más allá de las redes sociales. [Plebeian Market](https://plebeian.market) se volvió completamente nativo de Nostr con cumplimiento de [NIP-15](/es/topics/nip-15/), habilitando carritos de compra entre puestos y un navegador de puestos para descubrir comerciantes. [Shopstr](https://github.com/shopstr-eng/shopstr) emergió como un mercado sin permisos facilitando comercio en Bitcoin. [Zap.stream](https://zap.stream/), construido por kieran, trajo streaming en vivo a Nostr con pagos Lightning a 21 sats/minuto. Las herramientas de desarrollo maduraron con [NDK](https://github.com/nostr-dev-kit/ndk) proporcionando abstracciones TypeScript y [rust-nostr](https://github.com/rust-nostr/nostr) ofreciendo bindings Rust. [Zeus v0.8.1](https://blog.zeusln.com/new-release-zeus-v0-8-1/) lanzó con importación de contactos Nostr y LND persistente, sentando las bases para integración de Nostr Wallet Connect en versiones posteriores.

Sin embargo, la sostenibilidad de infraestructura [seguía siendo desafiante](https://arxiv.org/abs/2402.05709). Investigación académica de este período encontró que el 95% de los relays luchaban por cubrir costos operativos, con 20% experimentando tiempo de inactividad significativo. La tarifa de admisión para relays de pago promediaba menos de 1,000 sats (~$0.45), insuficiente para sostener operaciones.

*Una nota sobre estafas: El "Nostr Assets Protocol" y el token "$NOSTR" asociado que se lanzó alrededor de esta época [fueron públicamente denunciados por fiatjaf](https://www.aicoin.com/en/article/377704) como "100% fraudulentos" y "una estafa de afinidad" sin conexión con el protocolo Nostr real.*

### Enero 2025: Maduración de Clientes

Enero 2025 vio desarrollo continuo de clientes en todo el ecosistema. [Nostur 1.17.0](https://www.nobsbitcoin.com/nostur-v1-17-0/) lanzó el 13 de enero con sincronización entre dispositivos para estados de lectura, soporte de inicio de sesión multi-firma [FROST](/es/topics/frost/), y rendimiento optimizado de base de datos local. Amethyst continuó su transición al modelo outbox, compilando automáticamente conjuntos de relays basados en listas de seguidos en lugar de requerir configuración manual.

Los clientes principales comenzaron a alejarse de [NIP-04](/es/topics/nip-04/) para mensajes directos, migrando hacia [NIP-17](/es/topics/nip-17/) y el propuesto [NIP-104](/es/topics/nip-104/) para cifrado mejorado y protección de metadatos. El modelo Gossip (comunicación outbox/inbox) ganó adopción mientras el ecosistema convergía hacia patrones de uso de relays más eficientes. Observadores de la industria predijeron que este sería el año en que Nostr transicionaría de protocolo de nicho a reconocimiento mainstream, con una potencial migración de plataforma de alto perfil que podría duplicar la actividad diaria.

### Enero 2026: Seguridad e Infraestructura de Firma

Enero 2026 trajo avances significativos en seguridad e infraestructura de firma. [Primal Android 2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) lanzó firma remota [NIP-46](/es/topics/nip-46/) y soporte de firmante local [NIP-55](/es/topics/nip-55/), uniéndose a Amber y Aegis como un hub de firma completo para otras aplicaciones Android. [Bitchat completó una auditoría de seguridad de Cure53](https://github.com/permissionlesstech/bitchat/pulls), la misma firma que auditó Signal y NIP-44, con más de 17 PRs corrigiendo hallazgos críticos incluyendo limpieza de secretos DH y problemas de seguridad de hilos. Tanto Bitchat como Damus migraron de C Tor a Rust Arti para mejor confiabilidad y seguridad de memoria.

El trabajo de protocolo continuó con [NIP-71](https://github.com/nostr-protocol/nips/pull/1669) (eventos de video direccionables) fusionándose y un NIP de criptografía post-cuántica abriendo discusión sobre preparar Nostr para el futuro contra ataques cuánticos. El borrador de Trusted Relay Assertions propuso estandarizar puntuaciones de confianza de relays a través de atestaciones firmadas. El [Protocolo Marmot](https://github.com/marmot-protocol/mdk) endureció su mensajería cifrada basada en [MLS](/es/topics/mls/) con 18 PRs fusionados abordando hallazgos de auditoría.

Las aplicaciones del mundo real se expandieron con [Ridestr](https://github.com/variablefate/ridestr) desarrollando viajes compartidos descentralizados usando depósito [Cashu](/es/topics/cashu/) y cifrado [NIP-44](/es/topics/nip-44/), y [Pomade](https://github.com/coracle-social/pomade) añadiendo flujos de recuperación basados en correo electrónico a firma de umbral [FROST](/es/topics/frost/). Damus lanzó [negentropy](/es/topics/negentropy/) para sincronización confiable de DMs, mientras la aplicación de escritorio de Amethyst alcanzó la Fase 2A con búsqueda, marcadores y zaps.

### Mirando Hacia Adelante

Seis años de eneros revelan la evolución de Nostr desde desarrollo temprano (2021) a descubrimiento público (2022) a crecimiento explosivo (2023) a endurecimiento del protocolo (2024) a maduración de clientes (2025) a infraestructura de seguridad (2026). El patrón es familiar para cualquiera que haya observado protocolos abiertos crecer: años de construcción silenciosa, una explosión repentina cuando las condiciones se alinean, luego el trabajo más largo de hacer todo confiable. Lo que comenzó con siete relays y un hilo de Hacker News es ahora infraestructura auditada con aplicaciones reales. La pregunta para 2027: cuando alguien solicite un viaje, envíe un mensaje cifrado, o recupere una clave perdida usando Nostr, ¿sabrán siquiera que lo están usando?

---

Eso es todo por esta semana. ¿Construyendo algo? ¿Tienes noticias que compartir? ¿Quieres que cubramos tu proyecto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contáctanos vía DM NIP-17</a> o encuéntranos en Nostr.
