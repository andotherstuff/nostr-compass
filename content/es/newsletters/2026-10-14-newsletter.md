---
title: "Nostr Compass #44"
date: 2026-10-14
publishDate: 2026-10-14
draft: false
type: newsletters
description: "Amethyst para escritorio, correcciones de seguridad de Amber, archivos adjuntos privados, instalaciones de software autenticadas, y advertencias de contenido y estado."
translationOf: /en/newsletters/2026-10-14-newsletter.md
translationDate: 2026-10-15
---

**[Amethyst](#amethyst)** lleva su interfaz de Android al escritorio y añade compatibilidad nativa con Wayland. **[Amber](#amber)** corrige la revocación de permisos, el borrado de secretos copiados y un cambio de configuración que podía provocar la pérdida de claves. **[Keep](#keep-android)** refuerza los permisos de firma automática, mientras que **[MDK](#mdk)** incorpora archivos adjuntos privados en streaming y la puesta al día de mensajes empezando por los más antiguos. **[Zap Cooking](#zap-cooking)** integra medidas de protección para las modificaciones de las listas de seguidos y la membresía autenticada. A continuación se ofrecen los [detalles de las versiones](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0), junto con cambios del protocolo y mecanismos de estado público.

## Noticias principales

### Amethyst

[Amethyst v1.18.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.18.0) lleva al escritorio la interfaz compartida del cliente social para Android, con feeds personalizados, paneles para ventanas anchas, bloqueos opcionales, contenido multimedia cifrado y [subidas a Blossom](/es/topics/blossom/). Las puntuaciones de proveedores de [NIP-85, afirmaciones de confianza](/es/topics/nip-85/), se indexan localmente para solicitudes, notificaciones e insignias, con proveedores y umbrales seleccionados por el usuario.

La [versión v1.19.0 de hoy](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0) añade compatibilidad nativa con Wayland y compresión de vídeo en escritorio mediante FFmpeg y ffprobe, instalados por separado. Las correcciones del almacenamiento de claves resuelven las solicitudes repetidas de acceso al llavero y los fallos del llavero de Linux. Se añade la visualización de colecciones de calendario y confirmaciones de asistencia, y la interfaz de inicio de sesión de Android incorpora la [firma remota NIP-46](/es/topics/nip-46/). La apertura en paralelo de sobres cifrados precede a la indexación en serie, y se corrigen la reconexión a relay y la gestión de las listas de relay de los autores de los feeds. El [cliente de relay respeta la espera por limitación de solicitudes](https://github.com/vitorpamplona/amethyst/pull/4422) antes de reanudar las suscripciones o publicaciones.

El [cambio en los relay de proveedores de confianza](https://github.com/vitorpamplona/amethyst/pull/4437) trata los relay de proveedores de la lista kind 10040 del usuario como relay propios y de confianza. Estas conexiones utilizan una ruta directa de forma predeterminada; para usar Tor hay que activar el ajuste de relay de confianza. La [autenticación de relay NIP-42](/es/topics/nip-42/) del cliente principal puede revelar la clave pública del usuario a estos relay.

### Amber

[Amber 6.6.9](https://github.com/greenart7c3/Amber/releases/tag/v6.6.9) corrige tres fallos de seguridad en el firmante Nostr para Android. Los [permisos revocados](https://github.com/greenart7c3/Amber/security/advisories/GHSA-8f7m-9g64-vrjw) ya no persisten por una condición de carrera en la caché, y los rechazos explícitos prevalecen sobre el estado de plena confianza. Para los [secretos copiados](https://github.com/greenart7c3/Amber/security/advisories/GHSA-g62f-m6pm-jv9p), el sistema programa el borrado del portapapeles al cabo de 60 segundos, incluso si se termina el proceso; el contenido sigue siendo legible durante ese intervalo, y también puede borrarse texto copiado posteriormente. Al cambiar [«requerir que el dispositivo esté desbloqueado»](https://github.com/greenart7c3/Amber/security/advisories/GHSA-wv7c-hq2j-ppc5), se conserva la antigua clave de envoltura hasta que finaliza la migración de secretos, aunque las claves perdidas anteriormente siguen perdidas. La versión corrige las aprobaciones de nostrconnect con varias solicitudes y responde a través de los relay especificados en la URI. Los usuarios de 6.6.8 y versiones anteriores deberían actualizar.

### Keep Android

[Keep Android v1.3.0](https://github.com/privkeyio/keep-android/releases/tag/v1.3.0), un [firmante de umbral FROST](/es/topics/frost/), añade generación distribuida de claves en el dispositivo y recuperación autenticada de operaciones interrumpidas con fragmentos de clave. También admite dispositivos sin compatibilidad con StrongBox. Con la firma de umbral, los dispositivos participantes conservan fragmentos del secreto de firma y cooperan para producir una firma; los pasos de configuración y recuperación determinan qué dispositivos pueden participar.

La [versión 1.3.1](https://github.com/privkeyio/keep-android/releases/tag/v1.3.1) impide que la firma automática se imponga a rechazos recordados, permisos de preguntar, aprobaciones caducadas o fallos en la lectura de permisos. La caducidad elimina la aprobación en segundo plano, pero conserva las denegaciones. La [migración de políticas por aplicación](https://github.com/privkeyio/keep-android/pull/532) traslada los permisos al almacén gestionado por el núcleo y conserva las decisiones más restrictivas.

### Chama

[Chama v6.4.21](https://github.com/jesuspirate/chama/releases/tag/v6.4.21) [autentica el puente nativo de la cartera](https://github.com/jesuspirate/chama/pull/29) utilizado por su aplicación de operaciones comerciales mediadas por Nostr, desactiva en producción la redirección del puente basada en URL y valida los importes de los pagos. También se niega a borrar una cartera cuyo contenido no se puede leer.

La [versión 6.4.22](https://github.com/jesuspirate/chama/releases/tag/v6.4.22) refuerza la reproducción frente a event de terceros ajenos, comprueba las relaciones de sucesión, rechaza los conjuntos de árbitros vacíos y deriva el momento del reembolso de la hora LOCK firmada. Sus cambios de consenso se aplican a los event CREATE firmados a partir del 1 de noviembre de 2026; las protecciones del cliente se aplican de inmediato. Las notas de la versión mantienen las salvedades sobre las federaciones seleccionadas por los anuncios y los pagos de importes ínfimos. Los [cambios posteriores en el firmante y la recuperación](https://github.com/jesuspirate/chama/releases/tag/v6.4.23) añaden lectores de semillas protegidas y bloqueos tardíos recuperables, mientras que [v6.4.24](https://github.com/jesuspirate/chama/releases/tag/v6.4.24) mejora las listas de operaciones extensas.

### Zap Cooking

El cliente de recetas y red social [Zap Cooking integra medidas de protección para las modificaciones de las listas de seguidos](https://github.com/zapcooking/frontend/pull/795) frente a lecturas incompletas, obsoletas o que muestran una reducción inesperada. Las acciones de seguimiento comparten una única vía de actualización protegida que conserva los tag y el contenido existentes. La identidad del firmante se comprueba antes de la publicación. Su [corrección de la autorización de membresía](https://github.com/zapcooking/frontend/pull/802) utiliza la clave pública que firma la solicitud autenticada. Se [eliminó una ruta que exponía un secreto administrativo](https://github.com/zapcooking/frontend/pull/801); el despliegue sigue requiriendo la rotación del secreto, algo que un cambio integrado por sí solo no puede garantizar. Las [correcciones posteriores de hilos y marcadores](https://github.com/zapcooking/frontend/pull/833) conservan la raíz real de las respuestas y recuperan las escrituras fallidas de marcadores. Los [campos de tag de las recetas](https://github.com/zapcooking/frontend/pull/836) ya no envían las pulsaciones de teclas a servicios de búsqueda de perfiles o NIP-50 ni abandonan el editor con cambios sin guardar.

## Versiones etiquetadas

### MDK

[MDK v0.13.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.13.0), el entorno de ejecución para los [grupos cifrados de Marmot](/es/topics/marmot/), añade archivos adjuntos privados en streaming y reanudables, con indicación del progreso y cancelación. También envía [denuncias NIP-56](/es/topics/nip-56/) privadas al operador del despliegue mediante [envolturas de regalo NIP-59](/es/topics/nip-59/), omitiendo los identificadores de mensajes, grupos y relay. La puesta al día procesa lotes de hasta 256 event empezando por los más antiguos y conserva los rechazos CLOSED de los relay. El enrutamiento SOCKS5 abarca los relay, el contenido multimedia y los servicios de descubrimiento, sin recurrir a una conexión directa como alternativa.

La [guía de la versión](https://github.com/marmot-protocol/mdk/blob/v0.13.0/docs/release/0.13.0.md) exige que los enlaces de lenguaje, las cabeceras y los artefactos nativos se actualicen conjuntamente. Los esquemas de las bases de datos avanzan de 101 a 107 sin posibilidad de volver a una versión anterior. El almacenamiento de secretos del anfitrión requiere una migración. MarmotKit y los artefactos de C son estables; WN Agent sigue siendo una versión preliminar y los crates del espacio de trabajo no están publicados en crates.io. El historial que llega con más de cinco [épocas MLS](/es/topics/mls/) de retraso puede seguir sin poder descifrarse sin que se muestre un aviso de historial incompleto, y los clientes de agente autenticados conservan el acceso a toda la API.

La versión también [reintenta los guardados de perfiles, listas de seguidos y listas de relay que quedan pendientes tras el primer acuse de recibo](https://github.com/marmot-protocol/mdk/pull/2228); estos reintentos en segundo plano no sobreviven a un reinicio. La [búsqueda de invitaciones comprueba la eliminación y la caducidad de KeyPackage en los relay de descubrimiento](https://github.com/marmot-protocol/mdk/pull/2211), cuyas respuestas no pueden demostrar que el destinatario siga conservando el material privado de su KeyPackage. Los [destinos de las reacciones a actividades](https://github.com/marmot-protocol/mdk/pull/2187) ahora se derivan de forma coherente de actores autenticados y de commits individuales del grupo; el historial antiguo sin actor sigue incompleto.

Los trabajos posteriores en master [cierran las suscripciones a relay que quedaban abiertas y paginan las reproducciones de activación, limitadas a 500 events](https://github.com/marmot-protocol/mdk/pull/2274). La [recuperación de brechas entre épocas](https://github.com/marmot-protocol/mdk/pull/2298) obtiene los 256 events más recientes de un relay cuya comparación ha fallado, sin certificar que el historial esté completo. [Los commits de autoactualización reintentan el envío a todos los relay del grupo que quedaron pendientes](https://github.com/marmot-protocol/mdk/pull/2275). Las nuevas comprobaciones de advertencia abarcan las [épocas obsoletas conocidas](https://github.com/marmot-protocol/mdk/pull/2273) y los [commits aún pendientes de enviar a relay](https://github.com/marmot-protocol/mdk/pull/2288); los usuarios pueden aceptar el riesgo, por lo que estas comprobaciones no garantizan que un grupo no pueda bifurcarse.

Las [descargas de archivos adjuntos bloqueadas por falta de almacenamiento](https://github.com/marmot-protocol/mdk/pull/2249) conservan el progreso reanudable cuando el espacio libre es insuficiente. Las descargas explícitas de gran tamaño usan un archivo como destino, y el almacenamiento provisional y los puntos de control requieren un espacio libre de aproximadamente cinco a seis veces el tamaño del cuerpo. Las [vistas previas verificadas de events públicos](https://github.com/marmot-protocol/mdk/pull/2304) incorporan una caché de cuenta cifrada y de tamaño limitado, mientras que los [resultados que solo contienen KeyPackage obsoletos](https://github.com/marmot-protocol/mdk/pull/2305) pasan a distinguirse de las consultas incompletas a relay. Estos son cambios posteriores en el código fuente que requieren una adopción correspondiente por parte de la aplicación anfitriona; las vistas previas por ID de event procedentes de obtenciones completadas no vuelven a comprobar si ha habido eliminaciones posteriores.

Los puentes de agentes también [limitan la salida del backend](https://github.com/marmot-protocol/mdk/pull/2103) para evitar que las respuestas demasiado grandes agoten la memoria, y [aceptan la respuesta de eliminación real del conector](https://github.com/marmot-protocol/mdk/pull/2301). El texto ya entregado sigue entregado cuando un límite de salida detiene un turno.

### Myco

[Myco v0.11.0](https://github.com/Origami74/myco/releases/tag/v0.11.0) añade conexiones USB entre teléfonos u ordenadores de escritorio con fips y adopta [el formato de manifiesto propuesto actualmente en NIP-5D](https://github.com/Origami74/myco/pull/135), con hashes firmados de los artefactos y los iconos. Los teléfonos antiguos aún pueden emparejarse, pero necesitan actualizarse para abrir estas napplets. Sus [cambios en la política de descarga](https://github.com/Origami74/myco/pull/133) distinguen entre destinos HTTP de Internet, de la red de malla y configurados por el usuario. Las indicaciones proporcionadas por el autor y las redirecciones no pueden sondear redes locales bajo la política de Internet, mientras que los destinos configurados por el usuario siguen sin restricciones. El cliente de software también [descubre blobs en los servidores Blossom BUD-03 del autor](https://github.com/Origami74/myco/pull/134). Esto mejora el descubrimiento de artefactos, pero expone el tráfico de instalación a esos servidores. Estos cambios en HTTP no establecen protecciones equivalentes para las conexiones WebSocket. Las [comprobaciones de disponibilidad en la malla cercana](https://github.com/Origami74/myco/pull/132) consultan a los pares para localizar blobs sin descargarlos ni contactar con servidores Blossom públicos. Estas solicitudes HEAD limitadas requieren permiso para usar la malla; un recuento de poseedores no demuestra que el artefacto completo siga disponible.

La versión también [consulta en paralelo a los servidores DNS de origen](https://github.com/Origami74/myco/pull/137) para evitar que los tiempos de espera de los operadores en itinerancia bloqueen las consultas de relay y artefactos. Las publicaciones de la bandeja de salida se dirigen a todos los relay de escritura enumerados, y los envíos a los destinos más lentos se completan en segundo plano. La malla por Internet sigue desactivada de forma predeterminada, y las imágenes de la web no se conservan entre reinicios.

### Unfiltered

[Unfiltered 1.0.13](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.13) añade listas de relay de lectura y escritura y enrutamiento de bandeja de salida a su cliente fotográfico para Android. Sus [notas de la versión](https://njump.me/nevent1qqsy8287ykdstql8ec2udgr8slj3czzkkdkjjc36xwn4lnjrrhggfwgu8dmj2) describen las funciones de los relay, y las cuentas sin una lista comienzan con tres relay públicos predeterminados. La función de proximidad utiliza geohashes de baja precisión y celdas adyacentes; añadir la ubicación a una publicación es opcional y está desactivado de forma predeterminada. Esas tags siguen revelando una zona públicamente. El resultado de publicación inspeccionado significa que se ha puesto en cola para un socket, sin que se haya confirmado aún la aceptación por parte del relay.

### monostr

[monostr 0.17.0](https://github.com/schmidt1024/monostr/releases/tag/v0.17.0) permite a los usuarios recibir propinas en Monero mediante un monitor personal, mientras que [0.18.0](https://github.com/schmidt1024/monostr/releases/tag/v0.18.0) oculta de forma predeterminada los importes de las propinas y los nombres de los remitentes en las notificaciones de las nuevas configuraciones. Las imágenes requieren un toque para cargarse de forma predeterminada, y los recuentos opcionales de Primal y las tags de cliente están desactivados. Un monitor alojado sigue conociendo todos los pagos entrantes a la cartera registrada mediante su clave privada de visualización. Los recibos públicos conservan el destinatario, la hora y la publicación referenciada incluso cuando los importes están ocultos.

### Grocery

[Grocery 1.0.2](https://github.com/Marc26z/nostr-grocery/releases/tag/v1.0.2) combina listas de la compra compartidas y cifradas con identidades de Nostr respaldadas por passkeys y un chat de Marmot para cada lista. Es posible unirse a las listas pegando una clave al portador, que concede permisos de lectura y edición. El inicio de sesión con passkey depende de que el navegador y el proveedor admitan la extensión de función seudoaleatoria de WebAuthn; las tags de miembros siguen siendo visibles para los relay. La [versión 1.0.3](https://github.com/Marc26z/nostr-grocery/releases/tag/v1.0.3) conserva las listas al volver a abrir la aplicación almacenando su contenido descifrado en una caché local, lo que corrige los casos en los que solo se conservaba la clave hasta que un relay volvía a entregar la lista.

### Roadstr

[Roadstr 1.1.0](https://github.com/roadstrapp/roadstr-app/releases/tag/v1.1.0) lee los kinds 1315/1316 de otro cliente Roadstr con sus periodos de validez y reglas de confirmación previstos. Un códec compacto conserva informes firmados reconstruibles para un puente experimental entre radio MeshCore y relay. La publicación compatible y la transmisión por radio están desactivadas de forma predeterminada, y se solicita consentimiento antes de compartir. Los informes por radio exponen la posición, la hora y la clave pública firmante a cualquiera que se encuentre dentro del alcance. Las pruebas utilizaron radios simuladas; el hardware real, Android BLE y la publicación en relay públicos siguen sin verificarse.

### OUTKAST

[OUTKAST 1.1.3](https://github.com/Lwb89dev/outkast/releases/tag/v1.1.3) mejora los comentarios en artículos y el tratamiento de publicaciones citadas en su cliente para Android. Los comentarios en artículos usan kind 1111 con el artículo como raíz y el comentario como padre, mientras que las respuestas a notas ordinarias siguen siendo kind 1. El descubrimiento de citas acepta tanto tags q como menciones e antiguas que contienen enlaces; las citas recién publicadas añaden tags q. Si la publicación falla, se revierten las reacciones optimistas.

### Bookshelf

[Bookshelf 0.1.28](https://github.com/decent-newsroom/bookshelf-app/releases/tag/v0.1.28) describe la [lectura de índices anidados](https://njump.me/nevent1qqs8pukgjrnuzryv0z67lze2y0jsshepdckuss25qggvwn5skxqfa7gslzul0) de publicaciones kind-30040 que contienen tanto capítulos como índices secundarios en el orden establecido por el editor. Las copias sin conexión conservan esa jerarquía y los marcadores vinculados a cada aparición. La actualización obtiene las revisiones actuales por coordenada, pero conserva la descarga anterior cuando los resultados están incompletos, son más antiguos o la operación falla. La retransmisión conserva los descendientes firmados originales. La expansión limitada y las ramas parciales legibles impiden que una estructura incompleta se presente como un libro terminado.

### Ditto

[Ditto 2.45.0](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.45.0) sustituye Global por Descubrir en sus fuentes de contenido. Descubrir se nutre de las personas seguidas por las cuentas que sigue el usuario y ordena las publicaciones según las conexiones compartidas, excluyendo al propio usuario y a las cuentas que ya sigue. Los usuarios que no han iniciado sesión y las cuentas que no siguen a nadie ven en su lugar una red inicial seleccionada. Esto cambia el alcance del descubrimiento predeterminado a un entorno social cercano; la resistencia al spam y la fiabilidad de esas cuentas siguen siendo cuestiones aparte.

### Postr

[Postr 1.1.2](https://njump.me/nevent1qqsf4uu87v5r7awyfhktjqnuc9m6xzfngpvr7gj37zca05sx7lk03vqy4wq7x) mantiene las identidades de los perfiles seleccionados vinculadas a las menciones al guardar borradores y publicar. El editor inmoviliza la cuenta, el texto, las menciones y los archivos adjuntos durante la firma y el envío, y retiene los elementos compartidos entrantes hasta que finaliza esa operación. Los reintentos conservan el event firmado original, incluidas las publicaciones pendientes más antiguas. Escribir un nombre después de @ no basta: los usuarios deben seleccionar un perfil, y las identidades que ya se hayan perdido en borradores antiguos deben seleccionarse de nuevo.

### Nostrautica

[Nostrautica Android 0.11.0](https://github.com/jooray/nostrautica/releases/tag/android-v0.11.0) vincula las comunidades con sus encuentros. La aprobación para un encuentro vinculado también puede conceder la pertenencia a la comunidad sin una segunda aprobación; el formulario de inscripción lo indica y permite a los solicitantes optar por no unirse a la comunidad. Quienes ya asisten reciben una invitación que pueden aceptar con un toque. Los encuentros conservan sus propios participantes, emparejamientos y chat, mientras que la comunidad muestra sus encuentros. Las notas de la versión describen la compatibilidad con coordinadores distintos para encuentros y comunidades, sin acreditar pruebas independientes de interoperabilidad o cifrado.

### Minibits

[Minibits v0.4.4 beta 1](https://github.com/minibits-cash/minibits_wallet/releases/tag/v0.4.4-beta.1) corrige el procesamiento de pagos de [Nostr Wallet Connect](/es/topics/nip-47/) en Android, que podía detenerse mientras la cartera estaba en segundo plano y acumular operaciones hasta provocar un fallo de aplicación que no responde. La versión nativa reúne cinco meses de cambios anteriores distribuidos mediante actualizaciones inalámbricas. [La versión 0.4.5 beta 1](https://github.com/minibits-cash/minibits_wallet/releases/tag/v0.4.5-beta.1) corrige las transferencias NFC de Android a iOS; las futuras actualizaciones inalámbricas requieren esta versión. Estas correcciones se describen en las notas de las versiones; el procesamiento en segundo plano sigue dependiendo de las restricciones del ciclo de vida impuestas por el teléfono.

### NoorNote

[NoorNote v1.9.0](https://github.com/77elements/noornote/releases/tag/v1.9.0) permite publicar recetas desde su editor de artículos, abrir paquetes de recetas compartidos y explorar recetas de autores a los que se sigue. Las tarjetas de sitios web y las cuadrículas de perfiles que se trataron la semana pasada ya se incluyen en esta versión, junto con la gestión de los límites de frecuencia de los relay y los enlaces directos `nostr:` de Android. Los enlaces a sitios web siguen siendo algo distinto de la verificación del contenido de un sitio; acceder mediante una pasarela expone a esa pasarela la solicitud realizada al hacer clic.

### Gittr

[Gittr v1.0.2](https://github.com/arbadacarbaYK/gittr/releases/tag/v1.0.2) empaqueta su forja Git sobre Nostr para Android y utiliza Amber mediante la [firma remota de NIP-46](/es/topics/nip-46/). El APK abre la aplicación alojada existente `gittr.space`, por lo que los usuarios siguen dependiendo del código para el navegador que esta sirve y de su disponibilidad. La firma mediante extensiones del navegador no está disponible dentro de este contenedor; el autoalojamiento sigue siendo un despliegue Git independiente.

### Dart NDK

[Dart NDK 0.11.0, versión de desarrollo cero](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.0) incorpora a una versión preliminar el [gestor de consentimiento de autenticación](https://github.com/relaystr/ndk/pull/862) del kit de herramientas para Dart y Flutter, así como el cambio de relay del firmante NIP-46. Estos cambios se trataron la semana pasada como trabajo integrado y ahora se han publicado. El firmante puede seguir una lista de relay de sustitución, que las aplicaciones deben conservar de forma persistente. [La versión de desarrollo uno](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.1) añade compatibilidad con identificadores NIP que contienen letras en la información de los relay. Ambas versiones incluyen cambios de integración que rompen la compatibilidad.

### Cambium

[Cambium v0.9.0](https://github.com/forgesworn/cambium/releases/tag/v0.9.0) ofrece a las aplicaciones nativas de Android [cuatro opciones de aprobación](https://github.com/forgesworn/cambium/pull/32): una vez, una hora, un día o indefinidamente. Los permisos se delimitan por operación y por kind del event. Cambium reenvía las solicitudes a un firmante de hardware Heartwood mediante firma remota; Heartwood sigue decidiendo qué solicitudes firma. Las aprobaciones de sitios web siguen siendo de un solo uso. Los firmantes emparejados incorporan controles de prueba y reconexión, actualizaciones compatibles del relay de transporte y diagnósticos con información sensible ocultada. En [NIP-55, firma en Android](/es/topics/nip-55/), los lotes conservan el orden de las solicitudes y los rechazos individuales, con consentimiento visible de un solo uso para los intents reutilizados ambiguos.

### Grain

[Grain v0.8.1](https://github.com/0ceanSlim/grain/releases/tag/v0.8.1) corrige la [autenticación de relay mediante NIP-42](/es/topics/nip-42/) de su biblioteca cliente en Go para aplicaciones que atienden a varios usuarios. Cada `UserContext` posee conexiones autenticadas privadas, preferencias de relay y mecanismos para mantener conexiones abiertas; el conjunto compartido nunca se autentica. La biblioteca valida los ID y las firmas entrantes, comprueba las coincidencias con las suscripciones y serializa correctamente los filtros de tag y tiempo. Los clientes que realizan llamadas autenticadas deben migrar a `UserContext`. El almacenamiento y el servicio de los relay no cambian, y la autenticación sigue requiriendo un desafío al abrirse la conexión.

### Nmail

[Nmail v0.18.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.18.0), un cliente de correo cifrado, coloca a los remitentes desconocidos en Solicitudes y a los bloqueados en Spam. La aceptación y el bloqueo se sincronizan entre dispositivos. Los remitentes ya presentes en la bandeja de entrada necesitan aceptación, con la opción Aceptar todos disponible; Spam permanece en silencio y las solicitudes pendientes evitan alertas repetidas del mismo remitente. Las respuestas utilizan la identidad receptora. La gestión de relay privados, las comprobaciones del bloqueo del dispositivo antes de copiar códigos de sincronización, los temas compartidos, una conservación más completa de los contactos y un instalador para Windows acompañan a las correcciones de restauración del buzón tras un restablecimiento o un inicio de sesión.

### Meiso

[Meiso v1.5.0](https://github.com/higedamc/meiso/releases/tag/v1.5.0) incorpora comentarios cifrados e indicadores de elementos no leídos a su gestor de tareas sincronizado mediante Nostr. Los comentarios utilizan event direccionables de kind 35002 con [cifrado NIP-44](/es/topics/nip-44/), manteniendo su asociación con la tarea dentro del texto cifrado. La versión [corrige los envíos sin conexión](https://github.com/higedamc/meiso/pull/212), la puesta al día al reconectar, el inicio con relay guardados y la propagación de listas vacías. También impide que una sincronización parcial elimine tareas. Las funciones de elementos no leídos y puesta al día no añaden un servicio de notificaciones cuando la aplicación está cerrada.

### Haps

[Haps v0.1.13](https://github.com/mmalmi/haps/releases/tag/v0.1.13), un instalador de software experimental, exige de forma predeterminada una auditoría de la versión exacta procedente de la [red de confianza](/es/topics/web-of-trust/) del usuario. Las auditorías pueden comparar el código fuente fijado y los artefactos recompilados, y mantenerse privadas o publicarse. [La versión 0.1.14](https://github.com/mmalmi/haps/releases/tag/v0.1.14) pide a los usuarios que confirmen el publicador al instalar usando solo el nombre; la automatización debe especificar uno. Las auditorías aportan pruebas, pero los programas nativos y las recetas de compilación siguen ejecutándose sin un entorno aislado. El requisito de auditoría puede omitirse para una operación; las comprobaciones de firma, integridad y confirmación del publicador se mantienen.

### Sidecar

[Sidecar v1.16.0](https://github.com/dmnyc/sidecar/releases/tag/v1.16.0) añade [descubrimiento y reproducción de transmisiones en directo](https://github.com/dmnyc/sidecar/pull/479) a su cliente social en forma de extensión del navegador, con chat firmado, reacciones y zaps. Los marcadores de transmisiones guardados admiten copias de seguridad cifradas de la cuenta y su restauración, y el silenciamiento privado de notificaciones permite a los usuarios controlar las alertas. La búsqueda incorpora controles para seguir y silenciar; también se incluyen cambios en el bloqueo automático y la actualización del historial de la cartera.

### Ants

La interfaz de búsqueda [Ants v0.7.0](https://github.com/dergigi/ants/releases/tag/v0.7.0) [dirige las búsquedas estructuradas](https://github.com/dergigi/ants/pull/316) a los relay de escritura anunciados por los autores y a los relay de lectura de los usuarios mencionados mediante [listas de relay NIP-65](/es/topics/nip-65/), sin iniciar sesión. El descubrimiento limita la cantidad de identidades y relay consultados, y se detiene al cancelarse o agotarse el tiempo de espera. Si faltan listas, se mantiene el enrutamiento alternativo. Las consultas de texto siguen utilizando [relay de búsqueda NIP-50](/es/topics/nip-50/) verificados.

### soyLI

[soyLI v0.27.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.27.0), una herramienta de publicación y reproducción de napplets para las [aplicaciones NIP-5D propuestas](/es/topics/nip-5d/), añade atajos de teclado y propuestas sin bifurcaciones mediante GRASP, un servicio de alojamiento Git, con comprobaciones de la revisión exacta en los reintentos. Su [versión v0.26.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.26.0) distribuye versiones firmadas a relay de salida verificados después de la publicación principal; la eliminación lleva un registro de los destinos en los que se intentó publicar, pero no puede retirar copias desconocidas. [La versión 0.26.1](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.26.1) eleva a 100 MiB los límites de lectura, reproducción y revisión, mientras mantiene un límite de 25 MiB para las nuevas compilaciones y la publicación. Posteriormente, los [metadatos de presentación directos](https://github.com/zeSchlausKwab/napplet-soy/pull/14) sitúan las portadas y los clips de los autores directamente en los manifiestos firmados, prescindiendo del event complementario. Los trabajos antiguos congelados siguen siendo compatibles; esta extensión versionada de Soy requiere lectores compatibles y no forma parte de la especificación NIP-5D fijada.

### nostream

El servidor relay [nostream v3.3.0](https://github.com/cameri/nostream/releases/tag/v3.3.0) añade sondas de [monitorización de relays mediante NIP-66](/es/topics/nip-66/) para medir los tiempos de ida y vuelta de lectura y escritura de WebSocket, detectar la autenticación opcional y descubrir destinos de replicación. Advierte cuando el comportamiento observado no coincide con la [información del relay según NIP-11](/es/topics/nip-11/). Las respuestas OK sujetas a límites de frecuencia pueden incluir un quinto elemento opcional con un tiempo de espera en milisegundos antes de reintentar. La [versión 3.4.0](https://github.com/cameri/nostream/releases/tag/v3.4.0) añade a las [respuestas CLOSED](https://github.com/cameri/nostream/pull/821) un cuarto elemento con un tiempo de espera en milisegundos cuando los límites de mensajes por IP rechazan `REQ` o `COUNT`. Incluye el [núcleo de reconciliación por negentropía para PostgreSQL](https://github.com/cameri/nostream/pull/809) y un inventario ordenado de event; los mensajes del protocolo de comunicación del relay y el anuncio de capacidades de [NIP-77](/es/topics/nip-77/) siguen siendo trabajos independientes.

### Bark

[Bark v1.3.15](https://github.com/forgesworn/bark/releases/tag/v1.3.15) incorpora controles de teclado para las aprobaciones de firma remota, una revisión explícita del event y de la identidad, y [uno, cinco o diez minutos para decidir](https://github.com/forgesworn/bark/pull/52). La validación en segundo plano rechaza las decisiones caducadas y las solicitudes en cola; si falla la entrega de una decisión, la ventana emergente permanece abierta para volver a intentarlo. La [versión 1.3.17](https://github.com/forgesworn/bark/releases/tag/v1.3.17) habilita la [firma en el navegador mediante NIP-07](/es/topics/nip-07/) en cuanto se completa la negociación inicial con el firmante, mientras continúan los diagnósticos opcionales. Restablece los puentes en las pestañas existentes tras las actualizaciones.

### Mostro

[Mostro v0.19.3](https://github.com/MostroP2P/mostro/releases/tag/v0.19.3) responde a solicitudes autenticadas por identidad sobre la reputación del propio usuario, incluso sin una orden abierta. La plataforma de intercambio entre pares envía las respuestas de forma privada a la clave de operación solicitante, y un [comando de CLI ya integrado](https://github.com/MostroP2P/mostro-cli/pull/203) permite realizar esa consulta. La importación de reputación sigue siendo una función preliminar cuyas importaciones no están implementadas; los operadores deben dejarla desactivada. Un [trabajo integrado posteriormente](https://github.com/MostroP2P/mostro/pull/1057) publica el margen del guardián de los fondos en custodia de Lightning y rechaza las configuraciones inseguras; su mínimo de 18 bloques presupone el ajuste predeterminado de LND para el vencimiento de las retenciones.

### Elisym

[El módulo commerce 0.11.0 de Elisym](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.11.0) admite comisiones descontadas de los ingresos del comerciante, con un tag firmado en el perfil de la tienda que declara la compatibilidad con pagos divididos y el rechazo de las tiendas incompatibles cuando se aplica una comisión. El [trabajo de administración ya integrado](https://github.com/elisymlabs/elisym/pull/170) lee pedidos y anuncios de relays de Nostr. Solicita la clave secreta de la tienda, lo que exige confiar en el código servido al navegador y en las extensiones; la administración local sigue disponible. El despliegue alojado y la activación de comisiones en mainnet siguen sin verificarse. [Merchant-node 0.10.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/merchant-node%400.10.0) actualiza su libro contable sin permitir volver a una versión anterior.

### Routstrd

[Routstrd v0.4.16](https://github.com/Routstr/routstrd/releases/tag/v0.4.16) evita que una recarga de [Nostr Wallet Connect](/es/topics/nip-47/) cuyo tiempo de espera ha vencido genere inmediatamente otra factura pagable. [Comprueba la operación de acuñación existente](https://github.com/Routstr/routstrd/pull/144) hasta que el pago se completa o falla; si el estado no está disponible, la recarga permanece en pausa. La pasarela de inferencia habilita proveedores según su etiqueta de reseña de Nostr, y las etiquetas experimentales requieren una aceptación explícita. La [versión 0.4.17](https://github.com/Routstr/routstrd/releases/tag/v0.4.17) incluye el SDK que lo hace posible. La protección frente a operaciones pendientes de liquidación permanece en memoria, por lo que reiniciar el demonio elimina esa protección.

### Buzz

[Buzz para escritorio 0.5.28](https://github.com/block/buzz/releases/tag/desktop-v0.5.28) permite al personal autenticado [explorar y moderar todas las comunidades](https://github.com/block/buzz/pull/8027) de un relay sin cambiar de conexión. Las acciones administrativas conservan la comunidad revisada, el relay y el firmante; si la autenticación está desactivada, la consola sigue disponible para lectura. Por separado, un [trabajo del relay ya integrado](https://github.com/block/buzz/pull/8197) oculta en las consultas y en la entrega en tiempo real los event de eliminación correctamente etiquetados correspondientes a registros privados de autor. Esa corrección del servidor requiere un despliegue y no cubre las copias ya divulgadas ni los registros históricos de eliminación sin etiquetar.

### Earthly

[Earthly v0.1.21](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.21) permite a los usuarios [incrustar conjuntos públicos de datos cartográficos de Nostr en sitios web](https://github.com/zeSchlausKwab/earthly/pull/35), con una vista previa y controles de apariencia y de posición inicial de la cámara. Su integración con Maps MCP crea y publica mapas desde el chat y después genera enlaces para compartirlos o insertarlos. La integración sigue siendo una prueba piloto personal con un complemento conectado. Las inserciones admiten conjuntos de datos incluidos directamente de hasta 300 elementos geográficos y 48 KiB; se excluyen los conjuntos privados, no publicados y respaldados por blobs.

### Milk Market

[La versión móvil v0.3.0 de Milk Market](https://github.com/shopstr-eng/self-sown/releases/tag/mobile-v0.3.0) incorpora editores completos de diseño de tiendas a su aplicación para vendedores, con las mismas secciones y campos que el editor web. El diseño de la página de cada producto puede prevalecer sobre las opciones de tema y secciones, incluidos los metadatos y las imágenes para redes sociales. La versión añade comprobaciones para mantener alineadas las configuraciones móvil y web. La [versión 0.3.1](https://github.com/shopstr-eng/self-sown/releases/tag/mobile-v0.3.1) corrige el contraste de la tarjeta de vista previa móvil; las descargas para Android se adjuntan a las versiones, y la disponibilidad para iOS es a través de TestFlight.

### Zeus

[Zeus v13.2.3](https://github.com/ZeusLN/zeus/releases/tag/v13.2.3) incluye la [corrección de las comisiones de enrutamiento de LDK](https://github.com/ZeusLN/zeus/pull/4353) comentada la semana pasada, que ya se ha publicado. Su servicio Nostr Wallet Connect basado en LDK puede incluir las comisiones de enrutamiento notificadas en las respuestas y en los registros de gastos. Las comprobaciones de presupuesto siguen cubriendo el importe de la factura antes de la liquidación, con las comisiones redondeadas descontadas después y un límite independiente de 1.000 satoshis para las comisiones de enrutamiento. La versión también actualiza el LND integrado e incluye correcciones de seguridad de rust-lightning; la validación en dispositivos NWC en funcionamiento sigue sin verificarse. La posterior [eliminación de Zaplocker ya integrada](https://github.com/ZeusLN/zeus/pull/4933) retira su flujo de certificación y canje mediante Nostr. Actualizar mientras ese servidor todavía retiene pagos elimina la posibilidad de canjearlos; los remitentes deben esperar al vencimiento de la factura de retención y al reembolso. Esa retirada no forma parte de v13.2.3; su despliegue depende de desactivar el servidor y avisar a los usuarios existentes.

## En desarrollo

### nosvelte

[La corrección del verificador de event de nosvelte](https://github.com/akiomik/nosvelte/pull/162) compara el ID proporcionado de un event con el hash canónico de sus campos antes de verificar la firma. Anteriormente, el verificador predeterminado de la biblioteca de Svelte aceptaba campos correctamente firmados con un ID sustituido, lo que permitía que el contenido ocupara la identidad de otro event e interfiriera con la gestión de reemplazos. El cambio integrado se aplica a las rutas de solicitud y envío de la versión uno que utilizan el verificador predeterminado; no certifica la exportación heredada ni los verificadores personalizados conforme al [formato de event de NIP-01](/es/topics/nip-01/). Una [corrección posterior del filtrado de solicitudes](https://github.com/akiomik/nosvelte/pull/171) comprueba y copia los campos de los event del relay antes de cotejarlos. Los datos malformados ya no pueden finalizar la suscripción del proveedor predeterminado ni descartar su siguiente event válido. Los clientes del motor proporcionados por quien realiza la llamada pueden conservar el comportamiento anterior de cotejo de las dependencias.

### nostter

nostter [restringe las indicaciones de relay proporcionadas externamente](https://github.com/SnowCait/nostter/pull/2684) a URL de WebSocket seguras y rechaza los nombres de host locales y las direcciones IP no globales. Los relays locales seleccionados por la cuenta y las URL de firmantes remotos conservan sus rutas existentes; la revinculación de DNS queda fuera de la comprobación. El cliente web también [lee las cargas útiles experimentales separadas de advertencia de contenido](https://github.com/SnowCait/nostter/pull/2680) solo después de que el lector pulse Mostrar, comprobando el ID del event referenciado, la coincidencia del autor y un tag `k` que coincida con el kind del event original. Las reacciones y las respuestas se dirigen al event original. Estos cambios integrados no modifican su formato actual de publicación [NIP-36](/es/topics/nip-36/).

### Coracle

[El editor de listas de Coracle](https://github.com/coracle-social/coracle/pull/679) restablece la edición y la eliminación al esperar a que termine la decodificación asíncrona antes de renderizar el formulario. Anteriormente, al editar se perdían los campos de la lista y ni el guardado ni la eliminación publicaban un event.

### Routstr Core

[El código fuente de la versión actual 0.5.0 de Routstr Core](https://github.com/Routstr/routstr-core/releases/tag/v0.5.0) [deja de registrar claves privadas de Nostr generadas automáticamente](https://github.com/Routstr/routstr-core/pull/812) y [conserva la identidad pública del primer arranque](https://github.com/Routstr/routstr-core/pull/818). [Los anuncios de proveedores](https://github.com/Routstr/routstr-core/pull/823) excluyen localhost y las direcciones HTTP literales privadas o de enlace local; no se resuelven los nombres de host para esta comprobación. El tag actual incluye trabajo integrado después de su fecha de publicación registrada, el 7 de octubre, por lo que los binarios y despliegues históricos siguen sin verificarse. Los registros expuestos anteriormente siguen requiriendo una revisión por parte del operador.

### Alby Hub

[El cambio de autorización de facturas de Alby Hub](https://github.com/getAlby/hub/pull/2629) limita la liquidación y la cancelación a las facturas creadas por la aplicación solicitante. La cartera autoalojada ofrece conexiones de aplicaciones mediante [NIP-47, Nostr Wallet Connect](/es/topics/nip-47/); la capacidad de una conexión para gestionar sus facturas no debe otorgarle autoridad sobre las facturas de otra aplicación. Por separado, una [corrección de privacidad para conexiones aisladas](https://github.com/getAlby/hub/pull/2621) elimina la dirección Lightning de la cartera principal de los flujos de éxito del navegador para conexiones aisladas.

### nak

[El comando relay integrado en nak](https://github.com/fiatjaf/nak/pull/222) comprueba los tiempos de conexión, lectura y escritura y la información del relay, y después imprime events de descubrimiento de kind 30166 sin firmar. Pasar esos resultados por una tubería a `nak event` aporta la firma y la publicación, lo que permite la [monitorización programada de relays mediante NIP-66](/es/topics/nip-66/) con la misma herramienta de terminal. Las respuestas de autenticación o restricción observadas prevalecen sobre la información anunciada por el relay. Las pruebas de escritura usan un event efímero firmado con una clave desechable; los anuncios de monitores de kind 10166 siguen siendo una operación independiente.

### Kehto

[La verificación de manifiestos de Kehto](https://github.com/kehto/web/pull/277) comprueba los manifiestos firmados actuales de un solo artefacto y los bytes del artefacto antes de la ejecución, manteniendo separado el análisis del formato heredado. El shell de napplet también [verifica los manejadores recomendados](https://github.com/kehto/web/pull/294), consulta a los usuarios sobre los conflictos con las opciones guardadas y consume una URL de invocación aceptada para evitar entregas repetidas. La verificación de manifiestos comprueba la identidad del publicador y los bytes del artefacto; no demuestra que el código de la aplicación sea seguro. [Las instantáneas del mando de juego](https://github.com/kehto/web/pull/297) ahora se ajustan al foco y la visibilidad. Los marcos de Paja/playground bloquean el acceso nativo directo al mando de juego, HID y USB antes de que se ejecute el código de la aplicación, dejando el acceso mediado a cargo del host. Los consumidores necesitan los paquetes correspondientes del host; la disponibilidad del shell es una capacidad independiente. Un [cambio posterior en la admisión de Paja](https://github.com/kehto/web/pull/305) advierte sobre los dominios experimentales obligatorios que no están disponibles, pero permite la carga; esos dominios siguen sin exponer APIs ni concesiones de permisos.

### napplet SDK

[El SDK de napplet implementa la invocación basada en URI y la entrega retenida](https://github.com/napplet/web/pull/228). [Los metadatos de publicación se conservan en el HTML independiente](https://github.com/napplet/web/pull/226), y [las referencias opcionales de aplicaciones](https://github.com/napplet/web/pull/239) vinculan los manifiestos con listados firmados y capturas de pantalla sin cambiar los hashes de los artefactos. El formato de referencia de aplicaciones sigue siendo una propuesta. Las pruebas del shell de referencia dejan el descubrimiento, la instalación y la verificación de firmas en producción a cargo de los hosts.

### rust-nostr

La biblioteca de Nostr para Rust [rust-nostr conserva el progreso parcial de las descargas junto con los errores terminales de los relays](https://github.com/nostrdevkit/nostr/pull/1483). El relay que ha fallado permanece en el conjunto de fallidos, por lo que quienes llaman a la biblioteca pueden usar los events ya recibidos sin perder la evidencia de que la sincronización se detuvo antes de tiempo.

### Pensieve

[La corrección de seguridad de la conciliación de Pensieve](https://github.com/andotherstuff/pensieve/pull/92) sigue a su [trabajo sobre la exclusión de events faltantes](https://github.com/andotherstuff/pensieve/pull/90). Las herramientas de relay y archivo vuelven a solicitar los IDs exactos que faltan antes de clasificar los fallos, evitando que los tramos finales omitidos por los límites de las consultas se conviertan en exclusiones falsas. El cómputo de las pausas se realiza por tarea, y los events ya archivados se gestionan por separado. Una tarea completada puede conservar registros explícitos de events faltantes; la finalización por sí sola no demuestra que el archivo esté completo.

[La conciliación continua de Premium Primal](https://github.com/andotherstuff/pensieve/pull/84) se habilitó el 12 de octubre. El [registro de despliegue](https://github.com/andotherstuff/pensieve/pull/93) del operador indica que ambos binarios corregidos se desplegaron y que las pausas basadas en fallos se habilitaron el 13 de octubre. La posterior [reutilización de exclusiones](https://github.com/andotherstuff/pensieve/pull/95) reutiliza únicamente exclusiones originales demostradas para el mismo relay y una ventana superpuesta, y excluye las reutilizaciones encadenadas y los IDs recién incorporados a la mezcla; su [despliegue quedó registrado esa tarde](https://github.com/andotherstuff/pensieve/pull/97). La [comprobación previa del archivo y la corrección del bloqueo de la caché](https://github.com/andotherstuff/pensieve/pull/98) se [desplegaron el 14 de octubre](https://github.com/andotherstuff/pensieve/pull/99). Una [corrección posterior de la prioridad de reutilización](https://github.com/andotherstuff/pensieve/pull/103) está integrada, pero aún no consta como desplegada en su registro de origen.

### njump

El visor web de Nostr [njump restaura los valores predeterminados de relay incorporados](https://github.com/fiatjaf/njump/pull/173) cuando no se proporciona un archivo que los sustituya. También [aísla los renderizadores de Markdown concurrentes](https://github.com/fiatjaf/njump/pull/171) y [las cabeceras de respuesta durante los tiempos de espera agotados](https://github.com/fiatjaf/njump/pull/169), corrigiendo condiciones de carrera que podían provocar el cierre del proceso al renderizar events citados de formato largo o atender solicitudes concurrentes. Son cambios del servidor ya integrados; el despliegue en producción sigue sin verificarse.

### Nostr Components

[La corrección de la firma de zap de Nostr Components](https://github.com/saiy2k/nostr-components/pull/187) detiene el flujo de pago cuando el firmante seleccionado se niega a firmar. Los widgets sociales integrables ya no sustituyen la identidad por una identidad anónima aleatoria tras el rechazo. Su [agregación de recibos](https://github.com/saiy2k/nostr-components/pull/197) valida los [recibos de zap de NIP-57](/es/topics/nip-57/) antes de eliminar duplicados de las copias de los relays, las facturas y los IDs de solicitud.

### rx-nostr

En la biblioteca cliente reactiva, [los cambios de verificación de la versión cuatro de rx-nostr](https://github.com/penpenpng/rx-nostr/pull/207) comprueban de manera uniforme la estructura canónica de los events, los IDs y las firmas en JavaScript y WebAssembly. Una lista vacía de condiciones de solicitud no coincide con nada y se completa; el envío heredado informa de un fallo cuando no tiene destino. Los observadores de publicación no pueden cambiar la resolución, y los descendientes de solicitudes liberados no pueden reiniciarse. [Los segmentos de consulta finitos](https://github.com/penpenpng/rx-nostr/pull/213) permiten que las consultas hacia atrás se completen una vez que hayan terminado todos los segmentos proporcionados. Estos cambios se incluyen en [4.0.0 beta 2](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%404.0.0-beta.2), una versión preliminar con cambios incompatibles en la API.

### eHagaki

El cliente social [eHagaki añade la entrega por etapas desde la bandeja de salida](https://github.com/Lokuyow/ehagaki/pull/268), fijando los relays de destino del autor antes de firmar. Su flujo de publicaciones sensibles envía a cada relay la carga útil antes de la estructura que la referencia, utilizando la confirmación del propio relay; si solo se entrega correctamente la carga útil, se conserva el editor. Un [escaneo completo del historial de publicaciones](https://github.com/Lokuyow/ehagaki/pull/312) guarda los resultados verificados de forma incremental. Los intervalos ambiguos permanecen sin confirmar incluso cuando el escaneo se muestra como completado, con un control de información explicativo. [La compatibilidad con el relay local Citrine](https://github.com/Lokuyow/ehagaki/pull/315) conserva los intervalos de navegación verificados y archiva los events firmados exactos tras una publicación externa exitosa. Las confirmaciones locales no convierten un envío externo fallido en uno exitoso, y esto no añade ninguna cola de publicación sin conexión. [La gestión de archivos multimedia subidos](https://github.com/Lokuyow/ehagaki/pull/321) permite listar y eliminar imágenes y vídeos subidos a servidores NIP-96 y Blossom compatibles. Una [migración posterior de la base de datos](https://github.com/Lokuyow/ehagaki/pull/325) restablece los datos de visualización en caché y el historial de publicaciones, pero conserva los borradores y las solicitudes de eliminación. También impide que los resultados antiguos de sincronización en cola vuelvan a llenar el historial después de vaciarlo.

### Formstr

[La corrección de Formstr para el resultado del envío](https://github.com/formstr-hq/nostr-forms/pull/508) rechaza una respuesta a un formulario cuando ningún relay la acepta. La aplicación de formularios de Nostr muestra los resultados de los relays y permite reintentar el envío conservando las respuestas rellenadas. Los webhooks y las páginas de confirmación esperan a que se acepte el envío, y el SDK incorpora la misma comprobación. Una confirmación de recepción de un relay sigue sin equivaler a una garantía de almacenamiento a largo plazo, pero un fallo total de publicación ya no produce un mensaje de éxito.

### Auditable Voting

[Auditable Voting añade la agrupación opcional de papeletas mediante un proceso de trabajo privado](https://github.com/tidley/auditable-voting/pull/35). Las definiciones firmadas por el organizador seleccionan la identidad del proceso de trabajo, los relays de DM y un umbral o plazo de publicación. Los votantes envían [papeletas con envoltura de regalo NIP-17](/es/topics/nip-17/) y autentican los acuses de recibo frente a ese proceso de trabajo; las delegaciones deben autorizar tanto la puesta en cola como la publicación. Las papeletas publicadas utilizan la identidad del proceso de trabajo. Este puede leer los envíos, y los lotes publicados al vencer el plazo pueden ser pequeños. Si no se resuelve ninguna ruta privada válida, el cliente inspeccionado recurre al envío público. Se trata de trabajo de desarrollo ya integrado.

### MintRadar

[MintRadar añade alertas opcionales con envoltura de regalo](https://github.com/hroomnik007/MintRadar/pull/122) sobre problemas con las operaciones de mint o melt, software obsoleto y pérdida de compatibilidad con esas operaciones. Su directorio de casas de moneda Cashu [conecta los controles de la lista de seguimiento](https://github.com/hroomnik007/MintRadar/pull/123) con esos ajustes de notificación y los confirma tras la respuesta del servidor. Las reservas atómicas impiden que comprobaciones simultáneas envíen la misma alerta, y una publicación fallida en los relays libera la reserva para permitir un nuevo intento. Los [mensajes privados NIP-17](/es/topics/nip-17/) protegen el contenido de las notificaciones; la aceptación por parte de un relay no confirma que el destinatario las haya leído.

### Nostr Docs

[La migración de Nostr Docs a un relay local](https://github.com/formstr-hq/nostr-docs/pull/65) canaliza las lecturas y escrituras del editor colaborativo de Markdown a través de un Web Worker con una caché de event en IndexedDB y una bandeja de salida para reintentos. Los títulos de los documentos y los tag se conservan tras las recargas, y las ediciones sucesivas de metadatos reciben marcas de tiempo crecientes para que dos ediciones en un mismo segundo sigan siendo distintas. El almacenamiento existente de claves de cifrado permanece intacto. La alternativa que recurre al conjunto de conexiones de red carece de la durabilidad de la bandeja de salida del worker, y aceptar una publicación en cola no demuestra que un relay la haya aceptado.

### Pakstr

[El firmante local nativo de Pakstr](https://git.nostrdev.com/stuff/pakstr/pulls/105) permite que el contenedor de su aplicación Android cree una cuenta de Nostr en el dispositivo. La clave permanece en la capa nativa, cifrada con una clave de envoltura protegida por Android Keystore. Los resultados de la firma se verifican antes de devolverlos a la aplicación web. El contenedor admite la [firma en el navegador mediante NIP-07](/es/topics/nip-07/) y solicitudes cifradas. La selección del firmante se abre solo cuando es necesaria y coordina las solicitudes simultáneas.

### Nostr WoT SDK

La biblioteca de red de confianza [Nostr WoT SDK amplía el consentimiento de autenticación](https://github.com/nostr-wot/nostr-wot-sdk/pull/15) a solicitantes nativos y remotos tipados. Las denegaciones almacenadas se comprueban antes de mostrar solicitudes de consentimiento, y el consentimiento reutilizable queda vinculado al transporte solicitante y al destino. Las solicitudes web siguen siendo de un solo uso por defecto. Sus [cargas gestionadas a Blossom](https://github.com/nostr-wot/nostr-wot-sdk/pull/13) validan bytes inmutables, permiten la cancelación y se detienen cuando cambia la sesión activa, con autenticación vinculada al servidor y restricciones de redirección.

### NosTube

[NosTube v0.2.49](https://github.com/flox1an/nostube/releases/tag/v0.2.49) proporciona instaladores de escritorio. Por separado, el trabajo de servidor ya integrado [añade publicación programada duradera](https://github.com/flox1an/nostube/pull/126). Los event se firman antes de su hora prevista, se almacenan en SQLite y los publica un proceso de trabajo que se pone al día tras un periodo de inactividad. Su [flujo de edición y eliminación](https://github.com/flox1an/nostube/pull/124) lleva un registro de las marcas de eliminación, la entrega a réplicas y la limpieza de archivos propios. La [configuración inicial](https://github.com/flox1an/nostube/pull/134) distingue el firmante del navegador del usuario de una clave de canal gestionada por el servidor. Los blobs históricos sin propietario quedan fuera de la limpieza automática.

### diVine

[diVine 1.0.24](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.24) añade colaboración privada en clips con créditos y comprobaciones de procedencia firmada de la captura o edición. Los subtítulos traducidos seleccionados por el espectador se sustituyen por los originales mientras la traducción está pendiente o sin verificar. Estas comprobaciones de procedencia no garantizan que una grabación no haya sido editada.

Los [cambios de enrutamiento](https://github.com/divinevideo/divine-mobile/pull/9884) del cliente de vídeos cortos consultan los relays de la bandeja de entrada de los destinatarios para los mensajes de chat de texto y vídeo, y conservan los resultados de entrega inciertos. La [gestión de copias para el remitente](https://github.com/divinevideo/divine-mobile/pull/10006) permite que los mensajes de grupo de los propios usuarios aparezcan en sus otros dispositivos; las copias descartadas anteriormente requieren volver a importar la cuenta. Los [envíos parciales a grupos cancelados](https://github.com/divinevideo/divine-mobile/pull/10031) conservan registros con el texto «No se envió a todos»; la cancelación es definitiva y esos registros no permiten reintentos. La creación de grupos y el reconocimiento de nuevas salas iniciadas por otros participantes siguen [sujetos a una opción desactivada por defecto](https://github.com/divinevideo/divine-mobile/pull/10020).

Los cambios posteriores en la rama principal [mantienen fuera de la caché temporal las copias interrumpidas de restauración de la base de datos](https://github.com/divinevideo/divine-mobile/pull/10118) y [conservan las publicaciones programadas, las denuncias en cola, las ediciones de perfil y los registros de chats eliminados durante la reconstrucción](https://github.com/divinevideo/divine-mobile/pull/10115). Los [plazos de envío incluyen la reconexión a los relays](https://github.com/divinevideo/divine-mobile/pull/10127), lo que reduce de 160 a 137 segundos el umbral de reintento de los envíos abandonados. Las [consultas del indexador a las bandejas de entrada utilizan un conjunto de conexiones separado y limitado](https://github.com/divinevideo/divine-mobile/pull/10116) para evitar esperar detrás de las lecturas del feed, y los [controles de seguimiento conservan la acción elegida](https://github.com/divinevideo/divine-mobile/pull/10147) si la lista de contactos cambia antes de la confirmación. Estas integraciones posteriores dejan menos tiempo para recibir la confirmación del relay durante las reconexiones lentas; las reparaciones de la base de datos no pueden restaurar datos perdidos anteriormente. Las [copias opcionales de grabaciones](https://github.com/divinevideo/divine-mobile/pull/10110), añadidas más tarde, permiten conservar los clips recién grabados mediante copias de seguridad en la galería de Android e iOS. Las copias sin procedencia firmada muestran una advertencia y no pueden volver a importarse; esta función está desactivada por defecto y requiere almacenamiento adicional.

### Conduit

Las aplicaciones de comercio de [Conduit incorporan una bandeja de entrada compartida y duradera](https://github.com/Conduit-BTC/conduit-mono/pull/616), que mantiene la entrega y recuperación de mensajes cifrados entre Market y Merchant. La aceptación por parte de los relays del destinatario se conserva aunque falle la copia para el propio remitente, y la recuperación reutiliza los mismos bytes para evitar un segundo envío semánticamente equivalente. Las [carteras compartidas respaldadas por un firmante](https://github.com/Conduit-BTC/conduit-mono/pull/635) conectan ambas aplicaciones. Esa vía de recuperación confía al firmante el texto en claro de recuperación; la integración del código fuente por sí sola no demuestra ni un despliegue activo ni pruebas de aceptación con fondos. Las [autorizaciones independientes de relay](https://github.com/Conduit-BTC/conduit-mono/pull/645) se conservan cuando varias rutas de cuenta comparten una URL. Desactivar una ruta ya no borra otra lista firmada de relays ni otra autorización de bandeja de entrada, y las lecturas que requieren autenticación o están incompletas mantienen un resultado de no disponibilidad. El [enrutador de pagos integrado](https://github.com/Conduit-BTC/conduit-mono/pull/613) divide un único pago de financiación aprobado por el comprador en pagos Lightning al comerciante y al proveedor, seguidos de la comisión de Conduit, con conciliación de la intención exacta y recuperación cifrada a través de la bandeja de entrada compartida de Nostr. La ejecución en producción y en preproducción sigue desactivada; que el proveedor complete su parte no demuestra que el receptor haya reclamado los fondos ni que el pago se haya dado por concluido.

### Bitcredit

[El cifrado de persistencia de Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1041) protege las claves de identidad, empresa y letras de cambio de su aplicación de letras de cambio electrónicas, incluida la cola de reenvío de Nostr, mediante la frase mnemónica de la identidad personal. La inicialización requiere una frase mnemónica coincidente. La [gestión de instancias](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1043) permite que las instancias de testnet y mainnet mantengan sus suscripciones de Nostr en segundo plano de forma independiente en un mismo dispositivo.

## Nuevos proyectos

### Submarine

[Submarine 0.1.0](https://github.com/nogringo/submarine/releases/tag/v0.1.0) presenta un gestor de contraseñas cuyas bóvedas cifradas se sincronizan a través de Nostr. Admite firmantes externos y conserva versiones simultáneas de los elementos, con importación y exportación de JSON de Bitwarden. Los cambios se guardan localmente antes de esperar la aceptación del relay. La versión incluye descargas para Android, escritorio y CLI. El proyecto se describe como incipiente y recomienda un gestor probado para las contraseñas críticas; la especificación del protocolo correspondiente a esta versión etiquetada sigue vacía. Su [almacenamiento web](https://github.com/nogringo/submarine/blob/v0.1.0/apps/app/README.md) guarda la clave de cifrado junto a los datos protegidos.

### cl-marmot

[cl-marmot](https://github.com/modus-lisp/cl-marmot/blob/5dd9dea97ece82b0e4cc08f0c893397fbb333a5b/README.md) incorpora una implementación en Common Lisp de chat grupal MLS a través de Nostr. El código del 9 de octubre añade convergencia entre commits en competencia y archivos adjuntos cifrados en Blossom, con pruebas de interoperabilidad frente al cliente de línea de comandos wn de MDK, según informa su autor. La implementación no ha sido auditada, y las claves de las cuentas y los registros de mensajes carecen de cifrado en reposo. Siguen sin implementarse las ventanas temporizadas de convergencia, la reproducción más allá del horizonte de reversión y la disolución de grupos; el entorno de pruebas inspeccionado utiliza relays locales desechables.

### nalgorithm Android

[La versión de nalgorithm para Android](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.0) genera un feed de Nostr ordenado según las preferencias y un resumen de audio en segundo plano que puede reproducirse sin conexión. Los usuarios eligen entre inferencia alojada, con tarifas en Lightning, o inferencia con clave propia solicitada desde el teléfono; son vías independientes. El inicio de sesión admite Amber mediante firma remota. Las versiones posteriores [corrigen la clasificación con clave propia y la detección de la lista de seguidos](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.1), y después [conservan los «me gusta» de los relays que funcionan cuando falla otro relay](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.2) y mejoran la recuperación de los resúmenes. [La versión 1.0.3](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.3) reorganiza la configuración del modelo e informa de los datos que faltan para probar la conexión.

## Trabajo sobre protocolos y especificaciones

### Endpoints autenticados de napplet

En las especificaciones NAP para aplicaciones napplet, [los identificadores de endpoints NAP-INC](https://github.com/napplet/naps/pull/104), incorporados el 9 de octubre, sustituyen los nombres de manejadores sin más por identificadores autenticados. Los nombres iguales de distintos publicadores ya no identifican al mismo par. El entorno de ejecución sigue mediando en la comunicación, y los manifiestos raíz o de instantánea no necesitan una coordenada `d` con nombre.

### Recomendaciones de manejadores en enlaces de invocación

[La recomendación en enlaces de invocación](https://github.com/napplet/naps/pull/99), también incorporada el 9 de octubre, permite incluir una recomendación opcional de manejador mediante `#naddr`. Un shell puede ofrecer búsqueda e instalación, con la resolución habitual como alternativa. Las preferencias guardadas y la política del shell tienen prioridad. Por tanto, un manejador recomendado aporta una pista para su descubrimiento sin sustituir la elección existente del usuario ni transferir al remitente del enlace la autoridad para instalar.

### Aceptación de la entrega y trabajo de la aplicación

[Los cambios en el anuncio de intenciones y la entrega](https://github.com/napplet/naps/pull/91) derivan los roles y las intenciones del mismo manifiesto verificado, utilizando identificadores seguros para el publicador. La aceptación de la entrega ya no depende de que la aplicación de origen siga en ejecución. Una respuesta `ok: true` acepta la responsabilidad de la entrega; no significa que haya terminado el trabajo de la aplicación de destino. El comportamiento de reintento y reinicio sigue siendo una política del entorno de ejecución conforme a este cambio incorporado a la especificación.

### Cadenas de acciones de Cyberspace

[Las reglas revisadas de las cadenas de Cyberspace](https://github.com/arkin0x/cyberspace/pull/48) hacen que una bifurcación invalide una cadena de acciones firmadas desde su origen y exigen que los clientes confirmen la cabecera vigente antes de firmar otra acción. El mundo respaldado por Nostr añade [140 cadenas sintéticas firmadas](https://github.com/arkin0x/cyberspace/pull/49) con dictámenes normativos para las implementaciones. [Las reglas de atribución de copias](https://github.com/arkin0x/cyberspace/pull/47) utilizan referencias `q` al objeto original y notifican a su autor las remezclas públicas; las copias selladas omiten esa notificación. Se trata de especificaciones del proyecto ya incorporadas, sin que se haya verificado la cobertura de los verificadores desplegados.

### Confirmaciones de persistencia de los relays

[La propuesta abierta sobre persistencia](https://github.com/nostr-protocol/nips/pull/2496) introduce confirmaciones de persistencia, consultas PROOF y atestaciones opcionales de relay firmadas de kind 1797. Una firma permite atribuir a un relay una afirmación de almacenamiento; no demuestra que la retención continúe. Las consultas también revelan qué events interesan al cliente.

### Mensajes fijados compartidos para grupos de Marmot

[La propuesta abierta de Marmot para fijar mensajes](https://github.com/marmot-protocol/marmot/pull/434) define un estado compartido autenticado para un máximo de 64 referencias a mensajes, con permisos para miembros y administradores. Los cambios efectivos requieren un Commit de MLS y una transición de época, y cada hoja de miembro resultante debe admitir la función. Fijar mensajes no copia sus cuerpos ni prolonga su retención, por lo que los destinos no disponibles siguen sin resolverse. Los datos de prueba proporcionados presuponen un estado autenticado; no demuestran procesamiento criptográfico ni convergencia entre clientes.

## Análisis en profundidad de NIP: NIP-36 y NIP-38

### Advertencias de contenido antes de mostrarlo

[NIP-36, contenido sensible](/es/topics/nip-36/), permite a los autores añadir un tag `content-warning` a un event, con la opción de incluir un motivo. Un cliente puede ocultar el contenido hasta que el lector decida revelarlo. La [especificación](https://github.com/nostr-protocol/nips/blob/master/36.md) deja la interfaz a criterio de los clientes y permite tags de etiquetado adicionales. Añadir una advertencia no cambia quién puede leer el event. En una publicación pública, los relays y otros clientes siguen recibiendo su contenido.

[El analizador de tags de advertencia de Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt) reconoce el tag y considera no especificado un motivo ausente o en blanco. [El editor de publicaciones de Coracle](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/views/NoteCreate.svelte) escribe el motivo en el tag; su [vista de contenido](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte) respeta la configuración de contenido sensible del lector y ofrece una acción para revelarlo. [La vista de notas de noStrudel](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx) aplica su propia preferencia de advertencias y su estado de expansión antes de mostrar la interfaz de advertencia.

[NIP-36](https://github.com/nostr-protocol/nips/blob/master/36.md) no cifra los events ni exige ocultarlos. La ausencia de advertencia no dice nada sobre el contenido; los clientes deciden cómo afectan las advertencias a las vistas previas y a los controles para revelar el contenido.

### Estado del perfil y caducidad

[NIP-38, estados de usuario](/es/topics/nip-38/), utiliza events direccionables de kind 30315. El autor, el kind y el tag `d` identifican una coordenada de estado; `general` y `music` tienen significados definidos. Un event más reciente sustituye al estado anterior en esa coordenada, mientras que un valor `d` distinto permanece separado. El contenido vacío borra un estado. La [especificación](https://github.com/nostr-protocol/nips/blob/master/38.md) también permite referencias a URL, perfiles, events y direcciones.

Este event firmado de [NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) muestra un estado general caducado. Se conserva la ortografía original del autor.

```json
{
  "kind": 30315,
  "id": "8848719ae347e705afbbdbfa3a9f5dcca5dd31c4f39182503bf84de5e362bcf4",
  "pubkey": "f13fdeecd852acebaa77dbc18806a051eaa7ea2214c157a3495982d7535a77f3",
  "created_at": 1791983702,
  "tags": [
    [
      "d",
      "general"
    ],
    [
      "expiration",
      "1791984600"
    ]
  ],
  "content": "I'm listening 📩 on 3 ralys",
  "sig": "b5c98a578773f0199cb833d4b916aac115f2b13474a61e81fdca7316b848d397d7d8ad86d299abee4721f404b7b8a1af26e8c53143457ad14d2fb933b21daf85"
}
```

[El modelo de estados de Damus](https://github.com/damus-io/damus/blob/4a94f666d7e159e380e10b4dbbb2967d1688709e/damus/Features/Status/Models/UserStatus.swift) gestiona estados generales y musicales con caducidad. [El servicio de estados de Nostria](https://github.com/nostria-app/nostria/blob/e861946f4ef4e70f3ec49997a4be27615b9b6f5e/src/app/services/user-status.service.ts) ignora los valores vacíos o caducados y publica estados musicales utilizando la duración de la pista; sus suscripciones habituales solicitan únicamente los tipos general y musical. [Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip38UserStatus/UserStatusEvent.kt) conserva el identificador `d` al borrar un estado. Por lo tanto, los tipos personalizados requieren acuerdos que van más allá de la estructura compartida de transmisión.

Los estados son declaraciones públicas de sus autores. No demuestran que alguien esté en línea ni que haya escuchado una pista. Publicar música o disponibilidad puede revelar hábitos, y la caducidad opcional limita la visualización de información desactualizada sin prometer su eliminación. [NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) sigue siendo una especificación opcional en fase de borrador, al igual que NIP-36. Los clientes pueden implementar cualquiera de las dos de forma independiente, y sus ajustes de visualización determinan lo que ven los lectores.
