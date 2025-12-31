---
title: 'Nostr Compass #3'
date: 2025-12-31
publishDate: 2025-12-31
translationOf: /en/newsletters/2025-12-31-newsletter.md
translationDate: 2025-12-31
draft: false
type: newsletters
---

Bienvenido de nuevo a Nostr Compass, tu guía semanal del ecosistema del protocolo Nostr.

**Esta semana:** Al cerrar 2025, miramos hacia atrás a cinco años de hitos de diciembre en la evolución de Nostr. Desde el primer lanzamiento del cliente de fiatjaf en diciembre de 2020, pasando por la donación fundamental de Jack Dorsey de 14 BTC en diciembre de 2022, hasta la proliferación de NIP-55 signer este mes y la aceleración de caché de 162x de NDK, diciembre ha marcado consistentemente puntos de inflexión para el protocolo. Este número especial traza la historia técnica a través de cada diciembre, documentando el crecimiento del protocolo desde dos relays experimentales hasta más de 2,500 nodos en 50 países. Además: El módulo de escritorio de Amethyst toma forma a través de Quartz, Notedeck obtiene mensajería, Citrine aloja aplicaciones web, y NIP-54 corrige la internacionalización para scripts no latinos.

## Resumen de Diciembre: Cinco Años de Diciembres de Nostr

Nostr cumple cinco años este año. fiatjaf inició el protocolo el 7 de noviembre de 2020, y cada diciembre desde entonces ha marcado una fase distinta en su evolución: desde prueba de concepto hasta movimiento global hasta ecosistema de producción. Este es un retrospectivo técnico de diciembre de 2020 hasta diciembre de 2025, los años formativos que establecieron la base de Nostr y catalizaron su momento de explosión.

### Diciembre 2020: Génesis

El primer mes completo de existencia de Nostr vio a fiatjaf lanzar [Branle](https://github.com/fiatjaf/branle), el primer cliente del protocolo, construido con Quasar (Vue.js) y absurd-sql para almacenamiento local. fiatjaf ya había establecido la arquitectura central: usuarios identificados por claves públicas secp256k1, todas las publicaciones firmadas criptográficamente, relays sirviendo como almacenamiento simple que no se comunican entre sí. Uno o dos relays experimentales servían a un puñado de primeros adoptantes coordinándose en el grupo de Telegram [@nostr_protocol](https://t.me/nostr_protocol), que se había lanzado el 16 de noviembre. La [documentación original](https://fiatjaf.com/nostr.html) describía "el protocolo abierto más simple que es capaz de crear una red social global resistente a la censura," una premisa que tomaría dos años más en probarse.

### Diciembre 2021: Desarrollo Temprano

El 31 de diciembre de 2021, Nostr llegó a la [portada de Hacker News](https://news.ycombinator.com/item?id=29749061) con 110 puntos y 138 comentarios, enviado por Cameri. Esto marcó la primera exposición significativa del protocolo a la comunidad de desarrolladores más amplia. La red funcionaba con aproximadamente siete relays con menos de 1,000 usuarios. Branle recibió actualizaciones incluyendo importación de clave privada (31 de diciembre) y soporte multi-relay. Un cliente de línea de comandos, noscl, proporcionaba interacción basada en terminal. Las especificaciones del protocolo existían en la documentación de fiatjaf, aunque el [repositorio formal de NIPs](https://github.com/nostr-protocol/nips) no se crearía hasta mayo de 2022. El protocolo era, como lo describió fiatjaf, "un trabajo en progreso."

### Diciembre 2022: El Punto de Inflexión

Diciembre de 2022 transformó a Nostr de un experimento de nicho en un movimiento mainstream. El catalizador llegó el 15 de diciembre, cuando Jack Dorsey donó [14.17171699 BTC](https://www.coindesk.com/tech/2022/12/15/jack-dorsey-gives-decentralized-social-network-nostr-14-btc-in-funding) (~$245,000-$250,000) a fiatjaf después de descubrir el protocolo y declarar que era "100 por ciento lo que queríamos de Bluesky, pero no fue desarrollado por una empresa." El 16 de diciembre, fiatjaf anunció la división de fondos con el desarrollador de Damus William Casarin (jb55), y Dorsey verificó su cuenta de Nostr (npub: `npub1sg6plzptd64u62a878hep2kev88swjh3tw00gjsfl8f237lmu63q0uf63m`). El financiamiento legitimó el proyecto de la noche a la mañana.

La misma semana, el caos de Twitter aceleró la adopción. Del 14 al 15 de diciembre vio suspensiones de periodistas prominentes del New York Times, CNN y Washington Post. El 18 de diciembre, Twitter [anunció prohibiciones](https://techcrunch.com/2022/12/18/twitter-wont-let-you-post-your-facebook-instagram-and-mastodon-handles/) a cuentas que promocionaban Nostr, Mastodon y otras plataformas. La política se revirtió al día siguiente después de la reacción negativa. El éxodo llevó a los usuarios a explorar alternativas.

El desarrollo del protocolo se aceleró. El 16 de diciembre, se fusionó [NIP-19](/es/topics/nip-19/) ([#57](https://github.com/nostr-protocol/nips/pull/57)), introduciendo identificadores codificados en bech32 (npub, nsec, note, nprofile, nevent) que hacían las claves legibles por humanos y distinguibles. El repositorio de NIPs registró más de 36 commits ese mes, incluyendo actualizaciones de NIP-40 y NIP-07. Los clientes proliferaron: Damus llenó su beta de TestFlight en horas, Astral bifurcó Branle para creación de perfiles, Snort se lanzó como un cliente web "rápido y resistente a la censura," y Vitor Pamplona comenzó el desarrollo de Amethyst. Alby v1.22.1 "Kemble's Cascade of Stars" se envió el 22 de diciembre con soporte para NIP-19. Para el 7 de diciembre, Nostr tenía aproximadamente 800 usuarios con perfiles; cuando Damus llegó a la App Store el 31 de enero de 2023, se abrieron las compuertas, impulsando el crecimiento a más de 315,000 usuarios para junio de 2023.

### Diciembre 2023: Maduración del Ecosistema

Diciembre de 2023 marcó un punto de inflexión crítico para la seguridad del protocolo Nostr. El 20 de diciembre, se fusionó la [revisión 3 de NIP-44](https://github.com/nostr-protocol/nips/pull/746) después de una auditoría de seguridad independiente de Cure53 (NOS-01) que identificó 10 problemas en las implementaciones de TypeScript, Go y Rust, incluyendo ataques de timing y preocupaciones de forward secrecy. La especificación actualizada reemplazó el cifrado defectuoso de [NIP-04](/es/topics/nip-04/) con ChaCha20 y HMAC-SHA256, estableciendo la base criptográfica que ahora sustenta los DMs privados de [NIP-17](/es/topics/nip-17/) y el gift wrapping de [NIP-59](/es/topics/nip-59/). La misma semana, [OpenSats anunció su cuarta oleada de grants](https://opensats.org/blog/nostr-grants-december-2023) el 21 de diciembre, financiando siete proyectos incluyendo Lume, noStrudel, ZapThreads, y una auditoría independiente de NIP-44. Esto siguió a la [primera oleada en julio de 2023](https://opensats.org/blog/nostr-grants-july-2023) que había financiado Damus, Coracle, Iris, y otros, llevando la asignación total del Fondo Nostr a aproximadamente $3.4 millones a través de 39 grants.

El mes también expuso tensiones de sostenibilidad en el ecosistema. El 28 de diciembre, William Casarin (jb55) [publicó en Stacker News](https://stacker.news/items/368863) que 2024 sería "probablemente el último año de Damus," citando que "los clientes de nostr no generan dinero" después de que las restricciones de Apple sobre zaps en la aplicación limitaron severamente el potencial de ingresos. El equipo de Damus había rechazado previamente financiamiento de VC. Mientras tanto, [Nostr Wallet Connect v0.4.1](https://github.com/getAlby/nostr-wallet-connect/releases/tag/0.4.1) se envió el 26 de diciembre, extendiendo [NIP-47](/es/topics/nip-47/) con métodos `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance`, y `get_info`, sentando las bases para las integraciones de wallets que se convertirían en estándar en todos los clientes.

### Diciembre 2024: Avance del Protocolo

Diciembre de 2024 abrió con el [lanzamiento Alpha de Notedeck](https://damus.io/notedeck/) el 30 de noviembre, el cliente de escritorio basado en Rust del equipo Damus con una interfaz multi-columna con soporte para múltiples cuentas. Construido para Linux, macOS y Windows (Android planificado para 2025), Notedeck se envió inicialmente a suscriptores de Damus Purple y representó una expansión estratégica más allá de iOS. Dos semanas después, [OpenSats anunció su novena oleada de grants](https://opensats.org/blog/9th-wave-of-nostr-grants) el 16 de diciembre, financiando AlgoRelay (el primer relay algorítmico para feeds personalizados), Pokey (app Android con mesh Bluetooth para internet restringido), Nostr Safebox (almacenamiento de tokens Cashu con [NIP-60](/es/topics/nip-60/)), y LumiLumi (cliente web ligero y accesible), llevando la asignación total del Fondo Nostr a aproximadamente $9 millones, un aumento del 67% año tras año.

El mes vio una maduración significativa de clientes en todo el ecosistema. [Gossip 0.13.0](https://github.com/mikedilger/gossip/releases/tag/v0.13.0) llegó el 23 de diciembre con soporte de File Metadata ([NIP-92](/es/topics/nip-92/)/[NIP-94](/es/topics/nip-94/)), integración de Blossom, y búsqueda en relay con [NIP-50](/es/topics/nip-50/). [Coracle 0.5.0](https://github.com/coracle-social/coracle/releases/tag/0.5.0) se envió el 12 de diciembre con onboarding rediseñado e integración de nostr-editor. El desarrollo del protocolo se mantuvo activo con 30 pull requests enviados entre el 9 y el 22 de diciembre (10 fusionados), incluyendo reescrituras de [NIP-46](/es/topics/nip-46/) para usar solo cifrado NIP-44 y trabajo continuo en [NIP-104](/es/topics/nip-104/) para cifrado double ratchet al nivel de Signal. Las estadísticas de red mostraron más de 224,000 eventos diarios de pubkeys confiables, crecimiento de 4x año tras año en nuevos perfiles con listas de contactos, y un aumento del 50% en eventos de escritura pública.

### Diciembre 2025: Expansión del Ecosistema

Diciembre de 2025 trajo maduración continua del protocolo y expansión del ecosistema. El 21 de diciembre, [OpenSats anunció su decimocuarta oleada de grants de Nostr](https://opensats.org/blog/fourteenth-wave-of-nostr-grants), financiando tres proyectos: YakiHonne (un cliente multiplataforma con portal de creadores para contenido de formato largo e integración de pagos Cashu/Nutzaps), Quartz (biblioteca Kotlin Multiplatform de Vitor Pamplona que impulsa Amethyst y permitirá una versión iOS), y Nostr Feedz (integración bidireccional RSS-a-Nostr por PlebOne). Las renovaciones de grants fueron para Dart NDK y nostr-relay de Mattn.

La evolución del protocolo continuó con [NIP-BE](/es/topics/nip-be/) (mensajería Bluetooth Low Energy, [#1979](https://github.com/nostr-protocol/nips/pull/1979)) fusionado en noviembre, habilitando sincronización offline de dispositivos. [NIP-A4](/es/topics/nip-a4/) (Mensajes Públicos, kind 24, [#1988](https://github.com/nostr-protocol/nips/pull/1988)) llegó más tarde en el mes, definiendo mensajes de pantalla de notificación que usan tags `q` para evitar complicaciones de threading. [NIP-29](/es/topics/nip-29/) recibió clarificación mayor ([#2106](https://github.com/nostr-protocol/nips/pull/2106)), introduciendo el tag `hidden` para grupos verdaderamente privados e invisibles. La especificación de [NIP-55](/es/topics/nip-55/) también vio refinamiento ([#2166](https://github.com/nostr-protocol/nips/pull/2166)), abordando un error común de implementación donde los desarrolladores llamaban `get_public_key` desde procesos en segundo plano.

En el lado del cliente, [Primal Android se convirtió en un signer NIP-55 completo](/es/newsletters/2025-12-24-newsletter/#news) a través de ocho PRs fusionados implementando `LocalSignerContentProvider`, uniéndose a Amber y Aegis como opciones de firma en Android. La [biblioteca NDK logró consultas de caché 162x más rápidas](/es/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes) (de ~3,690ms a ~22ms) eliminando escrituras duplicadas y búsquedas innecesarias de caché LRU ([PR #371](https://github.com/nostr-dev-kit/ndk/pull/371), [PR #372](https://github.com/nostr-dev-kit/ndk/pull/372)). Shopstr introdujo [Zapsnags](/es/newsletters/2025-12-24-newsletter/#news) para ventas flash vía zaps. White Noise envió notificaciones push que preservan la privacidad con [MIP-05](/es/topics/mip-05/). Consulta [Newsletter #1](/es/newsletters/2025-12-17-newsletter/) y [Newsletter #2](/es/newsletters/2025-12-24-newsletter/) para cobertura completa.

---

Hace cinco años, fiatjaf lanzó Branle a un puñado de usuarios a través de dos relays experimentales. Hoy, el protocolo soporta más de 140 clientes, más de 2,500 relays en 50 países, y una creciente red de confianza que vincula cientos de miles de keypairs. El patrón de diciembre de lanzamientos importantes continuó este mes con mensajería Bluetooth, proliferación de signers en Android, y grants de infraestructura que señalan inversión sostenida en herramientas multiplataforma.

## Noticias

**Amethyst Desktop Toma Forma** - El grant de Quartz de la decimocuarta oleada de OpenSats ya está produciendo resultados. [PR #1625](https://github.com/vitorpamplona/amethyst/pull/1625) crea un módulo completo `:desktopApp` para Amethyst usando Compose Multiplatform, con pantallas de inicio de sesión y feed global funcionales en Desktop JVM. La arquitectura convierte el módulo `:commons` a Kotlin Multiplatform con una estructura de source set limpia (`commonMain`, `jvmAndroid`, `androidMain`, `jvmMain`), permitiendo componentes de UI compartidos entre Android y escritorio mientras deja las decisiones específicas de plataforma a cada target. Esto sienta las bases para la eventual versión iOS a través del mismo enfoque Kotlin Multiplatform.

**Amethyst Respuestas de Voz** - Una entrega navideña de davotoula: [PR #1622](https://github.com/vitorpamplona/amethyst/pull/1622) añade pantallas dedicadas de respuesta de voz con visualización de forma de onda, soporte para re-grabar, selección de servidor de medios, e indicadores de progreso de carga. Los usuarios ahora pueden responder tanto a mensajes de voz raíz como a respuestas de voz con audio.

**Notedeck Añade Mensajería** - Notedeck, el cliente de escritorio de Damus, ganó una función de mensajes en [PR #1223](https://github.com/damus-io/notedeck/pull/1223), expandiéndose más allá de la navegación del timeline hacia comunicación directa.

**Citrine Aloja Aplicaciones Web** - Citrine ahora puede [alojar aplicaciones web](https://github.com/greenart7c3/Citrine/pull/81), convirtiendo tu teléfono en un servidor web Nostr local-first. Un [PR #85](https://github.com/greenart7c3/Citrine/pull/85) separado añade reconexión automática y broadcasting de eventos cuando la conectividad de red regresa, con cobertura de pruebas completa a través de niveles de API de Android.

**Registro de Kits de Desarrollo de Nostrability** - El rastreador de [Developer Kits & Tooling](https://github.com/nostrability/nostrability/issues/264) mantiene un registro curado de SDKs, bibliotecas y herramientas de desarrollo a través de lenguajes (TypeScript, Rust, Python, Go, Dart, Swift, y más). Si eres nuevo en el desarrollo de Nostr, este es un punto de partida útil para encontrar el toolkit adecuado para tu stack.

## Actualizaciones de NIPs

Cambios recientes al [repositorio de NIPs](https://github.com/nostr-protocol/nips):

- **[NIP-54](/es/topics/nip-54/)** - Corrección crítica de internacionalización para normalización de d-tag wiki ([#2177](https://github.com/nostr-protocol/nips/pull/2177)). Las reglas anteriores convertían todos los caracteres no ASCII a `-`, rompiendo el soporte para japonés, chino, árabe, cirílico y otros scripts. La especificación actualizada preserva las letras UTF-8, aplica minúsculas solo a caracteres con variantes de mayúsculas, e incluye ejemplos completos: `"ウィキペディア"` permanece `"ウィキペディア"`, `"Москва"` se convierte en `"москва"`, y scripts mixtos como `"日本語 Article"` se normalizan a `"日本語-article"`.

## Lanzamientos

**Zapstore 1.0-rc1** - La tienda de aplicaciones sin permisos basada en Nostr envía el [primer release candidate](https://github.com/zapstore/zapstore/releases/tag/1.0-rc1) de su nueva arquitectura, presentando una actualización completa de UI, gestor de paquetes reescrito con mejor manejo de errores, App Stacks para descubrimiento curado, pantallas de perfil rediseñadas, verificación de actualizaciones en segundo plano, y desplazamiento infinito en listas de lanzamientos.

**KeyChat v1.38.1** - La aplicación de mensajería cifrada basada en MLS [añade soporte UnifiedPush](https://github.com/keychat-io/keychat-app/releases/tag/v1.38.1%2B6489) para notificaciones push de Android y Linux, más autenticación biométrica para operaciones de privacidad. Disponible para Android, Windows, macOS y Linux.

**Alby Go v2.0.0** - El compañero de wallet Lightning móvil [envía un rediseño visual](https://github.com/getAlby/go/releases/tag/v2.0.0) con nuevo logo, paleta de colores actualizada, libreta de direcciones rediseñada, y teclado de entrada de cantidades mejorado. BTC Map ahora es accesible desde la pantalla de inicio, y las descripciones de transacciones aparecen en notificaciones.

**nak v0.17.4** - La herramienta de línea de comandos Nostr de fiatjaf [lanzada](https://github.com/fiatjaf/nak/releases/tag/v0.17.4), siguiendo la corrección de restricción de LMDB Linux de v0.17.3 de la semana pasada.

## Cambios notables de código y documentación

*Pull requests abiertos y trabajo en etapa temprana que vale la pena seguir.*

### Damus (iOS)

[NIP-19 relay hints](https://github.com/damus-io/damus/pull/3477) implementa consumo de relay hints para obtención de eventos. Cuando los usuarios abren enlaces nevent, nprofile, o naddr, Damus ahora extrae relay hints de los datos TLV bech32 y se conecta a relays efímeros para obtener contenido que no está en el pool de relays del usuario. La implementación incluye limpieza con conteo de referencias para prevenir condiciones de carrera durante búsquedas concurrentes. [Detección de URL de imagen](https://github.com/damus-io/damus/pull/3474) convierte automáticamente URLs de imagen pegadas en miniaturas de vista previa en el compositor, con insignia de posición de carrusel para múltiples imágenes. [Conversión de pegado npub](https://github.com/damus-io/damus/pull/3473) transforma strings npub/nprofile pegados en enlaces de mención con resolución de perfil asíncrona.

### Amethyst (Android)

[Payment targets](https://github.com/vitorpamplona/amethyst/pull/1627) añade una interfaz de evento para splits de zap NIP-57, permitiendo que las publicaciones especifiquen múltiples destinatarios que comparten zaps entrantes (útil para colaboraciones, reparto de ingresos, o dar propinas tanto a creadores de contenido como a las herramientas que usan). [Documentación de paridad de características de Quartz](https://github.com/vitorpamplona/amethyst/pull/1624) añade una tabla detallada que rastrea qué características están implementadas a través de los targets Android, Desktop JVM, e iOS, notando que iOS carece de criptografía central (`Secp256k1Instance`), serialización JSON, y estructuras de datos.

### Notedeck (Desktop)

[Reconstrucción de filtro de timeline](https://github.com/damus-io/notedeck/pull/1226) corrige un bug donde las cuentas dejadas de seguir seguían apareciendo en feeds. Los filtros de timeline se construían una vez desde la lista de contactos y nunca se actualizaban; la corrección añade rastreo de `contact_list_timestamp` y un método `invalidate()` para activar reconstrucciones cuando cambia el estado de seguimiento.

### Citrine (Android Relay)

[ContentProvider API](https://github.com/greenart7c3/Citrine/pull/86) expone la base de datos de eventos del relay local a otras apps Android vía `ContentResolver`. A diferencia de la interfaz WebSocket (que requiere que las apps mantengan una conexión persistente y hablen el protocolo relay de Nostr), ContentProvider ofrece acceso directo síncrono a la base de datos a través del mecanismo IPC nativo de Android. Las apps externas pueden consultar eventos por ID, pubkey, kind, o rango de fechas, insertar nuevos eventos con validación, y eliminar eventos sin gestionar conexiones de socket.

### rust-nostr (Library)

[Soporte de NIP-40 a nivel de relay](https://github.com/rust-nostr/nostr/pull/1183) añade manejo de expiración a nivel del relay builder. Los eventos expirados ahora son rechazados antes del almacenamiento y filtrados antes de enviar a clientes, eliminando la necesidad de que cada implementación de base de datos maneje verificaciones de expiración independientemente.

### nak (CLI)

[Blossom mirror](https://github.com/fiatjaf/nak/pull/91) implementa funcionalidad de mirroring de blobs para la herramienta de línea de comandos.

### Mostro (P2P Trading)

[Dev fee audit events](https://github.com/MostroP2P/mostro/pull/559) añade pistas de auditoría transparentes para pagos al fondo de desarrollo a través de eventos Nostr kind 8383. La implementación publica eventos de auditoría no bloqueantes después de pagos de fees exitosos, incluyendo detalles de orden y hashes de pago mientras excluye pubkeys de comprador/vendedor por privacidad.

### MDK (Marmot Development Kit)

Tres correcciones de auditoría de seguridad llegaron: [Verificación de autor](https://github.com/marmot-protocol/mdk/pull/40) obliga a que los pubkeys de rumor coincidan con las credenciales del remitente MLS, previniendo ataques de suplantación. [KeyPackage identity binding](https://github.com/marmot-protocol/mdk/pull/41) verifica que la identidad de credencial coincida con los firmantes de eventos. [Validación de actualización de admin](https://github.com/marmot-protocol/mdk/pull/42) previene sets de admin vacíos y asignaciones de admin a no miembros.

### Shopstr (Marketplace)

[HODL invoice escrow](https://github.com/shopstr-eng/shopstr/pull/217) implementa un sistema de pago que minimiza la confianza para bienes físicos. La arquitectura usa `makeHoldInvoice` de Alby para bloquear fondos del comprador en su propia wallet, con liquidación activada solo después de la verificación de inventario del comerciante. El protocolo de handshake fluye a través de DMs cifrados [NIP-17](/es/topics/nip-17/): el comprador envía solicitud de orden, el comerciante responde con HODL invoice, el comprador paga (fondos bloqueados), el comerciante confirma stock y envío, luego la liquidación libera los fondos. El soporte de carrito multi-comerciante divide pagos entre vendedores.

### Jumble (Web Client)

[Modo de descubrimiento por relay](https://github.com/CodyTseng/jumble/pull/713) añade un toggle para ocultar publicaciones de usuarios seguidos en relays específicos, habilitando feeds de descubrimiento basados en idioma (ej., nostr.band/lang/*). La característica filtra publicaciones donde el pubkey del autor aparece en la lista de seguidos del usuario, persistiendo el estado del toggle por URL de relay en localStorage.

### White Noise (Encrypted Messaging)

[Reintento de carga de medios](https://github.com/marmot-protocol/whitenoise/pull/937) añade opciones de reintento para cargas fallidas. [Advertencias de edición de perfil](https://github.com/marmot-protocol/whitenoise/pull/927) alerta a usuarios sobre cambios de perfil. En el backend, [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs/pull/422) corrige una condición de carrera en la creación de AccountGroup.

### npub.cash (Lightning Address Service)

[Reescritura v3](https://github.com/cashubtc/npubcash-server/pull/40) migra a Bun para el monorepo y servidor, añade soporte SQLite, elimina compatibilidad v1, implementa LUD-21, y añade actualizaciones de mint quote en tiempo real.

### nostr-java (Library)

[v1.1.1](https://github.com/tcheeric/nostr-java/releases/tag/v1.1.1) envía refactorizaciones de manejo de WebSocket y robustez de pruebas mejorada a través de [dos PRs](https://github.com/tcheeric/nostr-java/pull/499).

### NIPs Repository

[Migración de NIP-54 a Djot](https://github.com/nostr-protocol/nips/pull/2180) propone un cambio separado a la especificación wiki: cambiar el formato de contenido de Asciidoc a Djot, un lenguaje de marcado ligero con sintaxis más limpia. El PR introduce enlaces de estilo referencia para wikilinks, haciendo las referencias cruzadas entre artículos wiki más legibles en forma de fuente. [NIP-XX Quorum](https://github.com/nostr-protocol/nips/pull/2179) introduce gobernanza de multi-firma umbral para grupos Nostr usando FROST (Flexible Round-Optimized Schnorr Threshold signatures). Un Quorum es un nsec compartido entre miembros a través de un esquema T-de-N donde los miembros pueden representarse a sí mismos o delegar a un consejo de representantes. Cuando el consejo cambia, el viejo nsec queda obsoleto y uno nuevo es distribuido—el acto final de cualquier consejo es firmar el evento de transición de gobernanza. La especificación define membresía (pública o privada), elecciones y encuestas (votos populares, votos de no confianza), "leyes" opcionales en lenguaje natural, y crucialmente, ontologías de quorum donde los quorums pueden ser miembros de otros quorums, habilitando estructuras jerárquicas como localidades uniéndose a cuerpos regionales. Los casos de uso abarcan desarrollo de código fuente, juntas directivas de empresas, HOAs, y comunidades moderadas.

---

Eso es todo por esta semana y este año. ¿Construyendo algo? ¿Tienes noticias para compartir? ¿Quieres que cubramos tu proyecto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contáctanos vía NIP-17 DM</a> o encuéntranos en Nostr.
