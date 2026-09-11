---
title: "Nostr Compass #39"
date: 2026-09-09
publishDate: 2026-09-09
translationOf: /en/newsletters/2026-09-09-newsletter.md
translationDate: 2026-09-11
draft: false
type: newsletters
description: "Nostr Compass #39 sigue los flujos de trabajo de git firmados, la publicación desde el navegador, las retransmisiones en directo autoalojadas, el consentimiento de relays comunitarios, los eventos privados, los lanzamientos enfocados y el contrato de enlaces NIP-21/NIP-27."
---

Bienvenidos de nuevo a [Nostr Compass](https://nostrcompass.org), tu guía semanal de Nostr.

**Esta semana:** [ngit y GitWorkshop](https://ngit.dev/v3) llevan los flujos de trabajo de git firmados a Nostr y [Blossom](/es/topics/blossom/), [nsite-clay](https://github.com/jooray/nsite-clay) hace recuperable la publicación desde el navegador, y [Wingman App](https://github.com/OtherStuffAI/wm-app) une la navegación, la firma local, la autenticación y los archivos. [Shosho y Livelier](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0) conectan retransmisiones autoalojadas con Nostr, [Communitator](https://github.com/dyne/communitator) hace que las plantillas de relays sean inspeccionables antes de firmar, [cal.emre.xyz](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743) publica franjas de citas, y [Plektos](https://github.com/derekross/plektos/pull/16) cifra eventos privados. Los lanzamientos etiquetados añaden trabajo de recuperación y privacidad en [Vector](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4), [Primal Android](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27), [LibreNostr](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) y [SkateSpots](https://zapstore.dev/apps/org.skatespots.app). El trabajo de desarrollo abarca el renderizado de [NIP-27](/es/topics/nip-27/), las preferencias de relays firmadas en [Conduit](https://github.com/Conduit-BTC/conduit-mono/pull/397), los objetivos de pago de [NIP-A3](/es/topics/nip-a3/) y los espejos de Blossom. Los cambios fusionados en el [repositorio de NIPs](https://github.com/nostr-protocol/nips) aclaran las suscripciones solo en directo y los datos de aplicación autenticados. Nuestro análisis en profundidad explica cómo los enlaces de [NIP-21](/es/topics/nip-21/) y las referencias de NIP-27 transportan perfiles y eventos de Nostr entre aplicaciones.

## Historias principales

### Los flujos de trabajo de git firmados llevan la CI, los repositorios privados y los lanzamientos a Nostr

El [lanzamiento de la v3 del 8 de septiembre](https://ngit.dev/v3) reúne ngit, GitWorkshop, ngit-grasp y ngit-ci en un único flujo de trabajo firmado. [ngit](https://ngit.dev/ngit.git) transporta ramas, parches y pull requests como eventos de [NIP-34](/es/topics/nip-34/), mientras que [GitWorkshop](https://ngit.dev/gitworkshop.git) proporciona la interfaz de revisión. El lanzamiento añade ngit-ci 0.1, un servicio de integración continua autoalojado cuyas instrucciones y resultados viajan como eventos firmados de Nostr, de modo que las comprobaciones pueden ejecutarse en hardware controlado por el mantenedor junto con la revisión del código.

La misma versión da a [ngit-grasp v3](https://ngit.dev/ngit-grasp.git) repositorios privados mediante la extensión de repositorios privados GRASP-08 y hace explícita la autoridad del mantenedor. Los registros de lanzamientos firmados pueden apuntar a recursos en [Blossom](/es/topics/blossom/), manteniendo tanto los metadatos de los lanzamientos como los archivos direccionados por contenido fuera de una forja alojada. El [nuevo sitio de documentación](https://ngit.dev/v3) reúne los componentes de cliente, repositorios privados, CI y web.

### nsite-clay hace recuperable la publicación desde el navegador

Una [corrección del aviso del firmante del 31 de agosto](https://github.com/jooray/nsite-clay/commit/064a0c5350f1e2b107f7d8f1de00ad75ef2e69d8), la [recuperación de publicaciones](https://github.com/jooray/nsite-clay/commit/d1ad514f8068eec2e007059dc62a5b6f1d240ae0) y los [controles de edición del 2 de septiembre](https://github.com/jooray/nsite-clay/commit/8f9d7d140dd3cd3e1db8726781fcd852041713f7) convierten a [nsite-clay](https://github.com/jooray/nsite-clay) en una herramienta de publicación en el navegador para un sitio de una sola página. Un usuario edita el modelo de objetos del documento directamente, serializa el resultado, lo sube como un blob de [Blossom](/es/topics/blossom/) direccionado por contenido y republica el manifiesto [NIP-5A](/es/topics/nip-5a/) del sitio. No se requiere compilación local ni servidor.

El [publicador en el navegador](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/deploy.html) ahora hace que las publicaciones fallidas sean recuperables y reduce los avisos repetidos del firmante, mientras que la [guía de edición](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/guide.html) documenta el ciclo. El resultado sigue siendo un sitio NIP-5A ordinario para las pasarelas existentes.

### Wingman App une navegación, firma y archivos

El trabajo de septiembre añade [selectores de archivos](https://github.com/OtherStuffAI/wm-app/commit/b0c9c03d317573adeafa92b1a56d696ad399e3ec), [publicación de perfiles](https://github.com/OtherStuffAI/wm-app/commit/f2343add8493625d62a1eb7fb76002ceab73f704), [restauración segura del firmante y la sesión](https://github.com/OtherStuffAI/wm-app/commit/4e278d96eb9258b89dc8b9639eac7bde3ac475c6) y [compilaciones móviles probadas](https://github.com/OtherStuffAI/wm-app/commit/60456ec0a8b4ed26ecde53812a61f95dc0bd22ac) a [Wingman App](https://github.com/OtherStuffAI/wm-app). Su capa de Flutter inyecta un proveedor de [NIP-07](/es/topics/nip-07/) en las páginas abiertas dentro de la aplicación, mientras que Flight Deck y Drive, respaldado por Tower, proporcionan una superficie de trabajo y un espacio de archivos junto al navegador.

Wingman firma las peticiones HTTP autenticadas usando [NIP-98](/es/topics/nip-98/). La [implementación de la petición](https://github.com/OtherStuffAI/wm-app/blob/67ed27d216e528da5bb431322bd10ac15553796f/crates/wmapp-core/src/auth/nip98.rs) construye el evento que un servidor verifica antes de responder, dando a una identidad instalada una ruta de aprobación coherente para acciones de relays, firma en aplicaciones web y archivos.

### Shosho incorpora las transmisiones autoalojadas de Livelier

[Shosho 1.1.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0) se publicó el 1 de septiembre con soporte para [Livelier](https://github.com/r0d8lsh0p/livelier), cuya [actualización de atribución del 31 de agosto](https://github.com/r0d8lsh0p/livelier/commit/7d8abb875770289502b55c3d947987db08e206dc) identifica el puente y la fuente de Owncast en los perfiles puenteados. Livelier observa el directorio público de Owncast, comprueba si una transmisión de video está en vivo y luego publica un evento [NIP-53](/es/topics/nip-53/) direccionable `kind:30311`. El descubrimiento viaja sobre Nostr mientras el video permanece en el servidor del transmisor.

El chat cruza el puente como eventos `kind:1311`. El [diseño del puente](https://github.com/r0d8lsh0p/livelier) abre una conexión del lado de la fuente solo mientras un lector de Nostr está suscrito, etiqueta las identidades derivadas y envía el chat transitorio a un relay que lo elimina después de tres horas. El relay de descubrimiento acepta escrituras de eventos en vivo solo desde la clave del puente; el relay de chat usa [autenticación NIP-42](/es/topics/nip-42/) y [banderas de eventos protegidos NIP-70](/es/topics/nip-70/).

### Communitator hace inspeccionables las plantillas de relays antes de firmar

La [serie de lanzamiento del 31 de agosto](https://github.com/dyne/communitator/commit/520edd33a253ca3249993172fd1003c80bfd9b7c) otorga a [Communitator](https://github.com/dyne/communitator) plantillas canónicas para listas de relays de kind `10002`, servidores Blossom de kind `10063` y bandejas de entrada de mensajes privados de kind `10050`. Antes de que un firmante se conecte, la aplicación muestra endpoints normalizados, permisos de lectura y escritura, kinds de eventos, relays de publicación fijos y destinos.

El [flujo de firma y publicación acotado](https://github.com/dyne/communitator/commit/2bd04c8fab292e73fe9a4ada250c64358aee8501) separa la conexión de la aplicación. Cada evento se firma por separado, una ejecución usa como máximo cuatro conexiones WebSocket, y un destino solo cuenta después de un `OK` positivo de [NIP-01](/es/topics/nip-01/). Los resultados distinguen entre entrega completa, parcial, fallida y cancelada. Las plantillas compartidas siguen siendo recomendaciones no confiables; la [superficie de consentimiento](https://github.com/dyne/communitator#security-and-consent) explica la observabilidad de relays y de red.

### cal.emre.xyz publica disponibilidad de citas con NIP-52

El repositorio público se abrió con un [commit inicial del 2 de septiembre](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743), seguido de un [anuncio firmado del manejador el 3 de septiembre](https://njump.me/6fead386f0f401c2d8641ef842ccc2ade5abb4e45d61bfd7f3872b43db04cdac) para [cal.emre.xyz](https://cal.emre.xyz). Un anfitrión publica su disponibilidad como un evento `kind:31923` de [NIP-52](/es/topics/nip-52/); un invitado publica un RSVP `kind:31925`.

Lee los eventos del anfitrión y los RSVPs de ocupado aceptados desde los relays, excluye los intervalos de tiempo que se solapan y mantiene los eventos de Nostr como el registro de programación sin copiarlos a una base de datos separada. Los anfitriones pueden firmar con [NIP-07](/es/topics/nip-07/), [NIP-46](/es/topics/nip-46/) o una clave local; los invitados pueden generar una clave separada. Su [repositorio](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743) también expone el `naddr` resultante y enlaces de calendario, con el correo electrónico deshabilitado por defecto.

### Plektos convierte los eventos privados en un solo canal cifrado

La [implementación de eventos privados del 2 de septiembre](https://github.com/derekross/plektos/pull/12) convierte cada reunión de [Plektos](https://github.com/derekross/plektos) en un canal privado dentro de una comunidad cifrada de [Concord](/es/topics/concord-protocol/). La lista de invitados, el registro de RSVPs, el tablero de inscripciones, el hilo, las contribuciones, las imágenes de portada, las ediciones y las eliminaciones se cifran juntas; una invitación lleva solo la clave de ese evento y no se publica ningún evento de calendario en texto plano.

La [auditoría de ciclo de vida del 6 de septiembre](https://github.com/derekross/plektos/pull/14) ancla el id de definición del evento para búsqueda directa cuando existen más de 500 wraps, manteniendo un respaldo paginado. Los paquetes de invitación expiran 30 días después de que termina un evento y pueden deshabilitarse, pero alguien que ya obtuvo una clave de canal puede conservarla. Una [reparación de seguridad del analizador](https://github.com/derekross/plektos/pull/16) separada hace que los identificadores [NIP-19](/es/topics/nip-19/) de tipo-longitud-valor (TLV) mal formados fallen en lugar de atrapar al analizador.

## Lanzamientos etiquetados

### Vector 0.4.4 hace más segura la recuperación de comunidades cifradas

[Vector 0.4.4](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4) se publicó el 31 de agosto con correcciones de recuperación de comunidades, rotación de claves, moderación y enrutamiento de respuestas. La refundación cierra una comunidad asaltada a la ruta de invitación usada por los atacantes; la membresía de reemplazo sustituye el estado local obsoleto; y un miembro inalcanzable ya no congela la lista. Las rotaciones vacías se rechazan, las promociones preservan a los miembros en línea, y las operaciones se niegan a ejecutarse cuando los miembros requeridos no pueden ser contactados.

El [lanzamiento](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4) también persiste las eliminaciones y expulsiones de moderadores, vuelve a cifrar el libro de visitas tras un cambio de contraseña, vincula las respuestas de notificaciones a su conversación después de reiniciar, y usa solo rutas multijugador verificadas. Estos son controles de recuperación, no revocación de claves ya obtenidas.

### Primal Android 3.5.27 verifica la identidad del firmante y de la billetera

[Primal Android 3.5.27](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27) se publicó el 3 de septiembre después de que [la verificación de identidad del firmante](https://github.com/PrimalHQ/primal-android-app/pull/1108) y [la autenticación de solicitudes de billetera](https://github.com/PrimalHQ/primal-android-app/pull/1105) se fusionaran el 31 de agosto. La firma local rechaza una solicitud cuya identidad no coincide con la cuenta retenida, y las solicitudes entrantes de [NIP-47](/es/topics/nip-47/) se autentican antes de procesarse. El enrutamiento de encuestas con zaps también envía los votos al autor de la encuesta cuando esta aparece en una respuesta.

### GRAIN 0.8.0-rc2 cierra una vía de aceptado pero no almacenado

[GRAIN 0.8.0-rc2](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2) se publicó el 7 de septiembre después de que un fallo de almacenamiento permitiera un `OK` antes de que su escritor asíncrono de la base de datos LMDB detectara que la capacidad de almacenamiento estaba llena. El relay ahora advierte al 80 y 95 por ciento, rechaza nuevos eventos al 97 por ciento dejando espacio para eliminaciones, e informa de fallos del escritor posteriores a la aceptación. La retención recorre primero los más antiguos, el cierre maneja mensajes tardíos y los filtros inválidos ya no descartan a sus hermanos válidos.

La [publicación](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2) también corrobora los anuncios de monitores de kind `10166` y los informes de relay de kind `30166`, expulsa informes obsoletos, mantiene los relays configurados como respaldo y reporta límites en vivo y autenticación en [NIP-11](/es/topics/nip-11/) en lugar de ceros estáticos.

### LibreNostr 0.5.0–0.5.2 hace que el enrutamiento por Tor falle de forma cerrada

[LibreNostr 0.5.0](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) se publicó el 7 de septiembre con un modo Orbot que enruta relays, zaps, subidas, medios, reproducción y vistas previas a través de un único puerto SOCKS, además de una reparación para un fallo en la hoja de zaps. Si Orbot o el proxy no están disponibles, las conexiones se detienen en lugar de filtrarse a una ruta directa. La [versión 0.5.1](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.1) evita que las búsquedas [NIP-50](/es/topics/nip-50/) lentas retrasen los resultados locales; [0.5.2](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.2) reemplaza el diseño recursivo de hilos y repara el ordenamiento de hilos.

El [comportamiento de fallo cerrado](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) se aplica a cada superficie de red enumerada por la publicación, y se requiere un reinicio porque esos clientes son de larga duración. Las versiones de parche preservan esa decisión mientras limitan fallos ajenos de búsqueda, profundidad de pila y diseño.

### SkateSpots añade una vía de relay en el dispositivo

La [publicación firmada del 8 de septiembre en Zapstore](https://zapstore.dev/apps/org.skatespots.app) añade un relay Citrine opcional a SkateSpots. Los spots, crews, mensajes y datos del mapa pueden cargarse localmente; las publicaciones se encolan sin conexión; y el teléfono conserva una copia local. El contenido existente de stash y mensajes permanece cifrado de extremo a extremo. Las verificaciones de pago requieren importes de factura y recibos de zap emitidos por el proveedor antes de conceder acceso o contar contribuciones.

El [relay local](https://zapstore.dev/apps/org.skatespots.app) es una opción de almacenamiento y continuidad, no un reemplazo de todos los relays remotos. Permite que un skater siga trabajando durante un período desconectado y luego reconcilie la actividad firmada, mientras que los cambios de pago impiden que un recibo autoescrito se convierta en prueba de liquidación.

### Whistle 1.8.15 repara la recuperación del ciclo de vida de grupos cifrados

[Whistle 1.8.15](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15) se publicó el 3 de septiembre después de que una reparación del ciclo de vida de Android impidiera que los contenedores de estado a nivel de ruta destruyeran las suscripciones de relay y las actualizaciones de ubicación de toda la aplicación. Sus notas de publicación también describen el estado de conexión actualizado tras el bloqueo o el modo doze y una acumulación de 501 eventos recuperada en el caso observado.

El [error](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15) vinculaba la propiedad de un servicio de larga duración a una pantalla de corta duración. Mantener viva la instancia con alcance de actividad y comprobar el socket antes de una lectura única hace menos probable que la navegación ordinaria de Android y la suspensión en segundo plano parezcan un grupo vacío.

### TWENTY ONE Companion 1.12.0 separa los DMs cifrados del chat heredado

[TWENTY ONE Companion 1.12.0](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0) se publicó el 5 de septiembre con DMs envueltos en regalo según [NIP-17](/es/topics/nip-17/). La bandeja de entrada cifrada está separada del chat de espacios antiguo, que permanece distinto porque esos mensajes nunca fueron cifrados y no pueden migrarse. Los PDF y videos están soportados sujetos a la política del relay, y los ocultamientos personales se sincronizan sin convertirse en baneos de moderador.

La [separación visible](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0) es parte del modelo de seguridad. Llamar al historial antiguo una bandeja de entrada segura tergiversaría su procedencia, mientras que migrarlo silenciosamente sugeriría un cifrado que no existía cuando fue escrito.

### ZapStore 1.1.2 valida ids de eventos y rotación de certificados

[ZapStore 1.1.2](https://github.com/zapstore/zapstore/releases/tag/1.1.2) se publicó el 4 de septiembre con validación de id de evento según NIP-01: el cliente recalcula el id de un evento entrante y rechaza las discrepancias antes de usarlo. La publicación también identifica paquetes instalados fuera de ZapStore. En el servidor, la [retención de hash de certificado](https://github.com/zapstore/relay/pull/8) preserva las etiquetas `apk_certificate_hash` repetidas para que la rotación de claves de firma de Android pueda mantener un linaje aprobado.

La [verificación del id de evento](https://github.com/zapstore/zapstore/releases/tag/1.1.2) impide que un relay o caché cambie etiquetas o contenido manteniendo el id antiguo. El indicador de fuente del instalador aporta procedencia separada cuando un paquete de Android con el mismo id de aplicación provino de otro canal.

### Amber 6.6.1 mantiene las respuestas del firmante atribuibles

[Amber 6.6.1](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1) se publicó el 4 de septiembre después de que se corrigiera el análisis de permisos para tolerar un `kind` opcional ausente, y las solicitudes de firma rechazadas comenzaron a devolver su id de solicitud original. Las aplicaciones que llaman pueden asociar un rechazo con la operación enviada. La publicación también actualiza los valores predeterminados del firmante remoto y añade un relay indexador.

En conjunto, estas [correcciones](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1) preservan la atribución en ambas direcciones: un registro de permiso sigue siendo utilizable cuando falta un campo opcional, y un rechazo permanece vinculado a la solicitud que lo causó. Los cambios en los relays predeterminados afectan el descubrimiento, pero no reemplazan la decisión de autorización local del firmante.

## En desarrollo

### Zap Cooking renderiza referencias NIP-27 con pistas de relays

[La fusión del 4 de septiembre](https://github.com/zapcooking/frontend/pull/665) hace que [Zap Cooking](https://github.com/zapcooking/frontend) renderice referencias `nostr:npub` y `nostr:nprofile` en artículos, recetas, vistas previas del editor y vistas de impresión. Los identificadores no válidos permanecen como texto, la resolución no es bloqueante, y el editor muestra una vista previa del Markdown que se firmará. Cuando existe información de relays, un `npub` simple se convierte en un `nprofile` con relays de outbox y una etiqueta `p` correspondiente.

Esa misma semana se corrigieron [las lecturas de kind `30023` con alcance de autor](https://github.com/zapcooking/frontend/commit/6a379c680727bb49074a4ff85f070b404dba97a7), se añadieron [relays de búsqueda NIP-50 verificados](https://github.com/zapcooking/frontend/commit/1802e8d7e95ed482209d09e03c834c2d9adfc1ea) con deduplicación y protecciones contra consultas obsoletas, y se repararon [las llamadas de billetera NIP-47](https://github.com/zapcooking/frontend/pull/705) después de que cambios en las dependencias rompieran los saldos y el historial.

### Conduit reconcilia las preferencias firmadas de relays y Blossom

[Conduit](https://github.com/Conduit-BTC/conduit-mono) fusionó la [edición de preferencias de Blossom](https://github.com/Conduit-BTC/conduit-mono/pull/374) el 2 de septiembre y la [reconciliación de preferencias firmadas](https://github.com/Conduit-BTC/conduit-mono/pull/397) el 7 de septiembre. Market y Merchant conservan la lista de relays de kind `10002` y la declaración de bandeja de entrada de kind `10050` válidas más recientes, preservan una lista firmada utilizable cuando un evento más nuevo está mal formado, distinguen una lista vacía explícita de una consulta no disponible, y no reemplazan los relays declarados fallidos con valores predeterminados del código.

El [editor de kind `10063`](https://github.com/Conduit-BTC/conduit-mono/pull/374) permite al usuario cargar, reordenar, revisar, firmar externamente, publicar y leer de vuelta una lista ordenada de servidores de medios HTTPS sin contactar esos servidores ni insertar un valor predeterminado no declarado.

### Los objetivos de pago de NIP-A3 llegan a tres clientes

Del 1 al 3 de septiembre, [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041), [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851) y [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98) implementaron los objetivos de pago de kind `10133` de NIP-A3. Amethyst ofrece una transferencia opcional solo cuando existe un objetivo compatible y no lo convierte en un zap; Grimoire utiliza un registro fijo antes de construir los URI de billetera; Pollerama valida direcciones de Monero y obtiene la lista de relays del autor antes de consultar los objetivos. Cada cliente sigue necesitando un método de pago permitido, una ruta de relays y una visualización precisa.

### Ditto amplía el respaldo de Blossom y las incrustaciones en vivo

[Ditto](https://github.com/soapbox-pub/ditto) fusionó [un amplio respaldo y espejado de Blossom](https://github.com/soapbox-pub/ditto/commit/1e35a0705c28f706eb40d1f99aedef3105cf6f07) el 6 de septiembre. Los avatares, insignias, banners, imágenes de comunidades, emoji personalizados e iconos de aplicaciones ahora prueban los servidores declarados con el mismo hash de blob; las subidas de espejado usan un token de autorización BUD-11 estándar. Un [cambio del 4 de septiembre](https://github.com/soapbox-pub/ditto/commit/e2a29004a65122470179c83d6ded8336a5c10dfa) añadió incrustaciones compactas de transmisiones en vivo `kind:30311`.

## Trabajo de Protocolo y Especificaciones

### Nostr Implementation Possibilities

[NIP-01](/es/topics/nip-01/) ahora aclara [el filtro `limit: 0`](https://github.com/nostr-protocol/nips/pull/2460), fusionado el 4 de septiembre. Un relay DEBE devolver cero eventos almacenados, DEBE enviar `EOSE` cuando se completan las consultas iniciales y DEBE mantener la suscripción activa para nuevos eventos coincidentes. Los clientes pueden abrir una suscripción solo en vivo con un único campo de filtro conservando el historial local. La aclaración registra un comportamiento compatible en varias implementaciones de relays y relays públicos.

[NIP-78](/es/topics/nip-78/) incorporó un [requisito de autenticación para datos de aplicación](https://github.com/nostr-protocol/nips/pull/2458), fusionado el 3 de septiembre. Los relays DEBERÍAN exigir autenticación [NIP-42](/es/topics/nip-42/) para los kinds `78` y `30078` y DEBERÍAN servirlos únicamente al autor autenticado del evento. Eso es un DEBERÍA, no una garantía de confidencialidad: los clientes no pueden tratar relays arbitrarios como almacenamiento privado. La fusión también desaconseja los kinds personalizados de datos de aplicación como intercambio público genérico.

[NIP-AC](/es/topics/nip-ac/) se abrió el 4 de septiembre como una [propuesta de señalización WebRTC](https://github.com/nostr-protocol/nips/pull/2461) explícitamente abierta. Utiliza kinds efímeros provisionales para ping, solicitudes de conexión, ofertas, respuestas y candidatos ICE, direccionados con `p` y agrupados por una etiqueta `e` de sesión; el kind `30600` admite el descubrimiento. Los relays DEBERÍAN difundir y NO DEBEN almacenar esos eventos de señalización mientras los pares se conectan directamente. Los números siguen siendo provisionales, los clientes DEBERÍAN usar [listas de relays NIP-65](/es/topics/nip-65/), y las aplicaciones que necesiten confidencialidad DEBERÍAN cifrar el contenido de ofertas, respuestas y candidatos con [NIP-44](/es/topics/nip-44/).

## Análisis en Profundidad de NIP: Enlaces URI y Referencias en el Texto de Eventos

Un identificador de Nostr necesita un significado transportable antes de que otra aplicación pueda abrirlo. [NIP-21](/es/topics/nip-21/) coloca un identificador [NIP-19](/es/topics/nip-19/) después del esquema URI `nostr:`, dando a navegadores, sistemas operativos y aplicaciones una forma única y despachable. [NIP-27](/es/topics/nip-27/) define qué significa ese mismo URI dentro del `content` legible de un evento. NIP-21 cruza una frontera de aplicaciones; NIP-27 mantiene una referencia a un perfil o evento dentro de la prosa firmada. Ninguno crea un kind de evento ni cambia los mensajes de los relays; las [dos especificaciones](https://github.com/nostr-protocol/nips/tree/master) definen únicamente el comportamiento de enlazado y renderizado.

### Despacho de URI y semántica de NIP-19

La [gramática de NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) es `nostr:` seguido de una entidad bech32 de NIP-19. `nsec` está excluido porque codifica una clave privada. No hay componente de autoridad, ruta o consulta, así que un enlace conforme es `nostr:npub1...`, no `nostr://npub1...`. Una plataforma o cliente puede registrarse como el manejador; la especificación no elige la aplicación instalada ni define una alternativa web.

El prefijo indica al cliente qué decodificar. `npub` lleva una clave pública y `note` un id de evento. `nprofile` añade pistas opcionales de relays a un perfil; `nevent` añade relays, autor y kind a un id de evento; y `naddr` lleva el autor, el kind y el identificador `d` de un evento direccionable, con relays opcionales. Estas formas usan los [campos type-length-value de NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md). Las pistas estrechan el descubrimiento pero no prueban ni la posesión por parte del relay ni el control del autor. Cada evento obtenido sigue necesitando un recálculo del id y una verificación de firma.

La forma de perfil en la [especificación de NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) es:

```
nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9
```

[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) también define puentes HTML: una página que sirve un evento de Nostr puede poner su `naddr` en `<link rel="alternate">`, y un perfil puede poner un `nprofile` en `<link rel="me">` o `<link rel="author">`.

### Renderizado de NIP-27 y etiquetas opcionales

[NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) se aplica al contenido legible de eventos, como notas de kind `1` y artículos de kind `30023`. Un compositor puede mostrar `@name`, pero publica `nostr:nprofile1...` en la cadena firmada. Un lector escanea la URI, decodifica su entidad NIP-19, obtiene el objetivo y puede renderizar un nombre, tarjeta, vista previa o enlace local. Si la decodificación falla, la URI permanece como texto ordinario. El contenido en bruto no debe reescribirse: cambiarlo cambia la serialización de NIP-01, el id y la firma.

Las referencias de contenido y las etiquetas tienen trabajos relacionados pero distintos. [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) describe las etiquetas opcionales `p` y `e` y la etiqueta `q` de [NIP-18](/es/topics/nip-18/). Un cliente puede mostrar una referencia sin crear una notificación ni una relación de hilo; el descubrimiento de citas debería escribir tanto la URI como una etiqueta `q`. La [implementación del 4 de septiembre de Zap Cooking](https://github.com/zapcooking/frontend/pull/665) sigue esa división conservando la URI mientras añade pistas de relays y una etiqueta `p` correspondiente. Añadir `p` o `q` no hace privada la URI, y NIP-27 no tiene un modo de mención oculta.

El siguiente [evento de kind `1`](https://njump.me/note1e0my422kylehy2g4ax4d98vsthdvnvy702yq3f6eguedjr0256as200k6a) se recuperó de `wss://nos.lol` y se verificó antes de su inclusión como referencia concreta de NIP-27. Su `content` contiene un `naddr` para un evento direccionable independiente de la versión. La decodificación produce kind `30402`, autor `91036d...310a`, el identificador `d` del libro de trabajo y una pista `wss://nos.lol/`. Las etiquetas `q`, `p`, `t`, `zap` y `client` son elecciones de la aplicación, no requisitos de NIP-27.

```json
{
  "id": "cbf64aa95627f3722915e9aad29d905ddac9b09e7a8808a7594732d90deaa6bb",
  "pubkey": "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
  "created_at": 1788953511,
  "kind": 1,
  "tags": [
    [
      "p",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/"
    ],
    [
      "t",
      "archetype"
    ],
    [
      "q",
      "30402:91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a:Archetype-Workbook-Companion-Meet-your-King-Warrioir-Magician-Lover-today-oejbwe",
      "wss://nos.lol/"
    ],
    [
      "zap",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/",
      "0.9"
    ],
    [
      "zap",
      "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
      "wss://relay.nostr.band/",
      "0.1"
    ],
    [
      "client",
      "Amethyst"
    ]
  ],
  "content": "You can check, read and use this Workbook already! You can also support and get it for few sats and support us in this project.\n\nI hope it'll help you in your Archetype Journey :)\n\n#archetype\n\nnostr:naddr1qpgyzunrdpjhg7tsv5k4wmmjdd3x7mmt94pk7mtsv9hxjmmw94xk2et594uk7atj949kjmn894tkzunjd9hkju3df4skw6trd9skut2vdamx2u3dw3hkgcte94hk26nzwajszrnhwden5te0dehhxtnvdakz7q3qjypkmmqcaetrcpld4m27la946cch2hrk7qr8xjehsu5j5h3uxy9qxpqqqpmvyqnrm7n",
  "sig": "aa9592e7c773271b9e9f980c8a7e17fda2ffd5a4483a1789e5dd4c4a83018ac576c5202b21b33b08770dcabe023f93998a41f1a0be4bf00e36cdde611d07915e"
}
```

### Confianza, comportamiento ante fallos e implementaciones de clientes

Un lector seguro encuentra un token `nostr:` completo, valida bech32, decodifica NIP-19, rechaza `nsec`, ignora los tipos TLV desconocidos y deja intacto el texto malformado o demasiado largo. `npub` y `nprofile` conducen a consultas de perfiles; `note` y `nevent` identifican eventos inmutables; `naddr` selecciona el evento direccionable válido más reciente para su kind, autor y etiqueta `d`. Las pistas de relays reducen la búsqueda pero no amplían la confianza. Según las [reglas de eventos de NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md), el cliente verifica el id de un `nevent` obtenido y comprueba la firma de cada candidato `naddr` antes de aplicar las reglas de reemplazo de eventos direccionables.

Las vistas previas en línea son una decisión del cliente con costes de privacidad y de recursos. Obtener cada referencia revela los intereses del lector y puede crear una tormenta de consultas, por lo que los clientes pueden usar una caché, aplazar las obtenciones hasta que sean visibles, limitar la concurrencia y exigir un clic para medios desconocidos. Según [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md), una vista previa debe permanecer diferenciada del texto firmado del autor actual. El fallo debe ser visible como texto sin resolver o como una tarjeta no disponible, no tratado silenciosamente como contenido verificado.

La confianza también cambia según el tipo de identificador. Un `nevent` nombra bytes inmutables, por lo que un cliente puede rechazar un evento obtenido cuyo id serializado difiera del id solicitado. Un `naddr` nombra una coordenada reemplazable, por lo que un cliente debe verificar cada candidato y aplicar las reglas de eventos direccionables antes de decidir qué versión mostrar. Una pista de relay es útil para la primera consulta en cualquiera de los casos, pero no es un respaldo del relay ni del contenido devuelto. La [definición TLV de NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md) proporciona los datos necesarios para hacer esas comprobaciones explícitas.

[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) define un enlace portátil que puede abrirse desde fuera de Nostr, mientras que NIP-27 hace que ese mismo enlace sea duradero dentro del texto firmado. Un cliente que implementa solo NIP-21 puede abrir un URI pegado pero no renderizar referencias incrustadas. El soporte completo de NIP-27 añade escaneo, decodificación segura, política de obtención, renderizado local y una elección explícita sobre las etiquetas de notificación y cita. El URI compartido mantiene esas capas interoperables sin obligar a los clientes a presentarlas de forma idéntica. [Damus](https://github.com/damus-io/damus) modela las referencias en línea como menciones tipadas. Su [código de menciones](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/Mentions.swift) asigna `npub` y `nprofile` a referencias de perfil, `note` y `nevent` a referencias de eventos, y `naddr` a referencias de direcciones; [NostrLink](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/NostrLink.swift) las dirige al destino apropiado. [Primal Android](https://github.com/PrimalHQ/primal-android-app) [analiza el esquema y las formas pegadas](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/domain/nostr/src/commonMain/kotlin/net/primal/domain/nostr/utils/NostrUriUtils.kt), valida bech32 y extrae las pistas de relays, y luego [asigna las referencias a modelos de contenido de notas](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/app/src/main/kotlin/net/primal/android/notes/feed/model/NoteNostrUriUi.kt). [Zap Cooking](https://github.com/zapcooking/frontend/pull/665) renderiza las mismas referencias en artículos, recetas, vistas previas del editor y vistas de impresión.

---

Envía un DM de NIP-17 para compartir un proyecto o una noticia a través del [proyecto Nostr Compass](https://github.com/andotherstuff/nostr-compass).
