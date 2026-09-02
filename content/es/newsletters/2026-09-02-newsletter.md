---
title: "Nostr Compass #38"
date: 2026-09-02
translationOf: /en/newsletters/2026-09-02-newsletter.md
translationDate: 2026-09-02
draft: false
type: newsletters
---

Bienvenidos de nuevo a [Nostr Compass](https://nostrcompass.org), su guía semanal de Nostr.

**Esta semana:** [Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) 1.0 incorpora notas verificadas de Nostr y suscripciones de formato largo a un lector Android sin conexión que lee artículos en voz alta; [nostream](https://github.com/cameri/nostream) amplía el enrutamiento de trabajos del lado del relay y el funcionamiento autenticado; [NDK for Dart](https://github.com/relaystr/ndk) corrige la negentropy y la duración de las solicitudes a varios relays; [Divine Mobile](https://github.com/divinevideo/divine-mobile) hace deterministas la eliminación y la firma de mensajes encapsulados; [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay) protege de forma predeterminada las bandejas de entrada de gift wrap; [Amethyst](https://github.com/vitorpamplona/amethyst) estrena resaltados portátiles; y [Mostro](https://github.com/MostroP2P/mostro) verifica las órdenes firmadas antes de aplicar su filtro de spam. [Napstr](https://github.com/lnbits/napstr) publica catálogos de audio y señales de actividad de seeders mediante Nostr, mientras transfiere los archivos a través de Tor. Los lanzamientos incluyen [MDK](https://github.com/marmot-protocol/mdk) y [pakstr](https://git.nostrdev.com/stuff/pakstr); el trabajo sobre el protocolo incorpora una indicación de paginación de [NIP-67](/es/topics/nip-67/) y un esquema de tags para resaltados de [NIP-84](/es/topics/nip-84/) en el [repositorio de NIPs](https://github.com/nostr-protocol/nips), mientras [Nostr Wallet Connect](https://github.com/nostr-wallet-connect/nwc) añade totales de transacciones; y la sección en profundidad sobre NIPs recorre los reposts y las reacciones mediante sus estructuras de event y sus implementaciones actuales.

## Noticias destacadas

### Voca 1.0 lee en voz alta notas verificadas de Nostr y suscripciones en Android

[Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) es un lector Android sin conexión que lee artículos, PDF, archivos Markdown y notas de Nostr con la voz de texto a voz del propio teléfono, mientras mantiene iluminada en la página la oración que está pronunciando. Su [lanzamiento 1.0](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en), [publicado el 2026-08-27](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) con su propia [clave de proyecto](https://njump.me/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu), convierte Nostr en una fuente de primer nivel: basta con pegar la dirección de una nota, un identificador de event, un npub, un perfil o un enlace web corriente que contenga una entidad de Nostr para que la aplicación decodifique la referencia, obtenga el event firmado de los relays y lea el texto del autor en lugar de la página web construida a su alrededor.

Dos comportamientos verificados definen la integración con Nostr, ambos descritos en el [anuncio firmado de Voca 1.0](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en). Primero, antes de persistir cada event obtenido, se contrasta con su id recalculado y con su firma Schnorr BIP-340 mediante los relays de arranque, la lista de relays [NIP-65](/es/topics/nip-65/) del autor (un event kind `10002`, firmado y reemplazable, en el que un autor enumera los relays que lee y en los que escribe) y las indicaciones incluidas en la propia referencia. Así, un relay puede negarse a responder, pero no poner palabras en boca de un autor. Segundo, añadir el npub de un autor incorpora sus artículos de formato largo [NIP-23](/es/topics/nip-23/) (publicaciones addressable kind `30023` con títulos, resúmenes e imágenes) a una única bandeja de entrada en el dispositivo, junto con los feeds RSS y Atom. La actualización 1.1.0, [anunciada el 2026-08-28](https://gitworkshop.dev/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu/voca) y publicada en [Zapstore](https://zapstore.dev) el 2026-08-29, sincroniza el desplazamiento oración por oración, suaviza los documentos largos y recupera el widget de la pantalla de inicio después del desplazamiento manual, el cambio de tamaño, los reinicios del proceso y las actualizaciones.

### nostream amplía el enrutamiento DVM del lado del relay y el funcionamiento autenticado

Tras el [trabajo del 19 de agosto sobre la recepción de trabajos](/en/newsletters/2026-08-19-newsletter/#nostream-adds-a-relay-monitor-and-mints-invite-codes), [nostream](https://github.com/cameri/nostream), una implementación de relay en TypeScript, [almacena y sirve events de controladores de aplicaciones NIP-89](https://github.com/cameri/nostream/pull/737). [NIP-89](/es/topics/nip-89/) (descubrimiento de controladores de aplicaciones) emplea recomendaciones kind `31989` e información de controladores kind `31990`, ambas ya dentro del intervalo parametrizado y reemplazable, por lo que un cliente puede consultar esos kinds y recibir un reemplazo cuando coincide un tag `d`. El relay no publica información de controladores para sus propios workers.

Los trabajos pendientes de [NIP-90](/es/topics/nip-90/) (data vending machine) ahora [llegan a un proceso worker y regresan como result events](https://github.com/cameri/nostream/pull/734). Si todo va bien, el relay firma un resultado kind 6000-6999 con su propia clave. Un tiempo de espera agotado o un fallo del worker marca el trabajo como fallido en lugar de dejarlo enviado.

Las sesiones autenticadas y las llamadas HTTP de administración se sitúan en límites distintos. [NIP-42](/es/topics/nip-42/) (autenticación de clientes ante relays) [registra el pubkey autenticado por socket](https://github.com/cameri/nostream/pull/716), puede exigir AUTH antes de que los clientes publiquen events y anuncia ese requisito en el documento [NIP-11](/es/topics/nip-11/) (información del relay); ambos controles están desactivados de forma predeterminada. Por separado, [las rutas de la API de administración pueden aceptar autorización HTTP firmada con NIP-98](https://github.com/cameri/nostream/pull/730). [NIP-98](/es/topics/nip-98/) (autenticación HTTP con events firmados) permanece desactivado hasta que un operador lo habilite y especifique los pubkeys permitidos.

### NDK for Dart corrige la negentropy, la duración de las solicitudes a varios relays y la verificación de firmas

Una ejecución de [NIP-77](/es/topics/nip-77/) (reconciliación de conjuntos mediante negentropy) en [NDK](https://github.com/relaystr/ndk), un kit de desarrollo en Dart para Nostr, devolvía conjuntos have y need incorrectos sin emitir ningún error porque el códec no hablaba la versión 1 del protocolo [negentropy](/es/topics/negentropy/). La [corrección de la codificación v1](https://github.com/relaystr/ndk/pull/722) ahora devuelve los ids que posee el relay y los que aún necesita.

Los filtros idénticos enviados a relays distintos [se estaban combinando en una sola solicitud](https://github.com/relaystr/ndk/pull/705). Las solicitudes con el mismo filtro ahora permanecen separadas cuando se dirigen a relays diferentes o tienen duraciones distintas, de modo que una consulta breve no puede mezclar en el resultado events de otro relay ni dejar bloqueada una suscripción activa.

El mismo kit [verifica una firma una vez y conserva el resultado](https://github.com/relaystr/ndk/pull/726). La entrega posterior de un duplicado ya no consume otra comprobación ni sobrescribe el event verificado almacenado.

### Divine Mobile hace deterministas la eliminación y la firma de mensajes directos encapsulados

Los events kind `5` encapsulados de [NIP-09](/es/topics/nip-09/) (solicitud de eliminación de event) que apuntaban a un mensaje nunca se aplicaban en [Divine Mobile](https://github.com/divinevideo/divine-mobile), un cliente móvil de vídeos cortos que publica mediante Nostr. El cliente [ahora resuelve cada eliminación contra el mensaje indicado](https://github.com/divinevideo/divine-mobile/pull/8174), en vez de tratar como ya procesado todo lo que no sea una reacción. Una segunda [solicitud de eliminación para todos mientras la primera seguía en curso](https://github.com/divinevideo/divine-mobile/pull/8164) antes desaparecía sin errores y sin un kind `5` en la red; ahora cada eliminación simultánea se publica.

Tras el lanzamiento 1.0.22 cubierto anteriormente, enviar dos veces en un segundo el mismo texto 1:1 de [NIP-17](/es/topics/nip-17/) (DM privados con gift wrap) [generaba un único rumor id](https://github.com/divinevideo/divine-mobile/pull/8163), por lo que el segundo envío desaparecía; ahora cada envío lleva un token dentro del rumor de [NIP-59](/es/topics/nip-59/) (gift wrap) para que los ids sean distintos.

Quien ya hubiera firmado un event kind `4` o kind `5` [conservaba esa firma](https://github.com/divinevideo/divine-mobile/pull/8173), en vez de que después se añadiera un client tag que cambiaba el id y provocaba que los relays rechazaran el event por no ser válido.

### Conduit Relay refuerza su bandeja de entrada protegida con NIP-42

Los gift wraps kind `1059` se almacenan para un destinatario. [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay), un relay en Go que conserva esos wraps en una bandeja protegida para el destinatario, [usa de forma predeterminada el modo enforce](https://github.com/Conduit-BTC/conduit-relay/pull/8): una consulta kind `1059` debe presentar autenticación [NIP-42](/es/topics/nip-42/) como ese destinatario, o el relay rechaza la solicitud. Los filtros de varios kinds, los comodines, los recuentos y la [negentropy](/es/topics/negentropy/) sobre esos wraps están `restricted`, de modo que otro AUTH no pueda convertirlos en un volcado de la bandeja de entrada ajena.

La misma [incorporación de la bandeja protegida](https://github.com/Conduit-BTC/conduit-relay/pull/8) exige un event id canónico en el event AUTH transmitido y acepta un event NIP-42 válido tanto si `content` está vacío como si no. El modo challenge-only sigue ofreciendo AUTH sin bloquear la lectura; disabled permite el acceso libre. El valor predeterminado de la biblioteca es enforce.

### Amethyst incorpora resaltados NIP-84 y corrige dos rutas de fallo relacionadas con relays

Tras el [trabajo de la semana pasada sobre autorización de Blossom](/en/newsletters/2026-08-26-newsletter/#amethyst-moves-blossom-authorization-off-image-loading-threads), [Amethyst](https://github.com/vitorpamplona/amethyst), un cliente Android de Nostr, publica [v1.14.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.14.0) con [NIP-84](/es/topics/nip-84/) (resaltados portátiles). Un pasaje seleccionado se convierte en un event kind `9802` desde el editor, un feed de resaltados o una acción de compartir en la aplicación.

El lanzamiento añade controles de eliminación y archivado de canales [NIP-29](/es/topics/nip-29/) ([PR #3812](https://github.com/vitorpamplona/amethyst/pull/3812)) y mide el comportamiento de los relays mediante el tráfico que el cliente ya genera; después amplía esas sondas [NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) con comprobaciones de streaming, lectura, escritura y URL ([PR #3836](https://github.com/vitorpamplona/amethyst/pull/3836), [PR #3857](https://github.com/vitorpamplona/amethyst/pull/3857)). Amethyst también elimina una vulnerabilidad de colisión de hashes en SharedKeyCache y compara los códigos de autenticación de mensajes en tiempo constante ([PR #3833](https://github.com/vitorpamplona/amethyst/pull/3833)), corrige una condición de carrera que podía perder la entrega de AUTH al conectarse ([PR #3838](https://github.com/vitorpamplona/amethyst/pull/3838)), distribuye el bloqueo del estado de las suscripciones para acabar con una cadena de ANR ([PR #3851](https://github.com/vitorpamplona/amethyst/pull/3851)) y compara todos los filtros de suscripción, no solo el primero ([PR #3856](https://github.com/vitorpamplona/amethyst/pull/3856)).

[El boletín #36 ya cubrió estos cambios en autenticación de relays, copias de seguridad y chats públicos](/en/newsletters/2026-08-19-newsletter/#amethyst-rebuilds-its-relay-authentication-decision-flow); v1.14.0 ahora los publica juntos. Los soft bans de Concord cierran vacíos de autoridad detectados por una auditoría ([PR #3885](https://github.com/vitorpamplona/amethyst/pull/3885)). La autenticación de relays cuenta con un flujo de permisos rediseñado ([PR #3899](https://github.com/vitorpamplona/amethyst/pull/3899)), espera a que se resuelva el desafío en vez de agotar el tiempo ([PR #3905](https://github.com/vitorpamplona/amethyst/pull/3905)), configura las cuentas nuevas para autenticarse de forma predeterminada ([PR #3931](https://github.com/vitorpamplona/amethyst/pull/3931)), respeta esa preferencia en relays ajenos al conjunto habitual de la cuenta ([PR #3937](https://github.com/vitorpamplona/amethyst/pull/3937)) y conserva las concesiones de sesión entre reconexiones ([PR #3955](https://github.com/vitorpamplona/amethyst/pull/3955)). Un proceso guiado para el primer inicio y Ajustes facilita encontrar las copias de seguridad de las claves ([PR #3909](https://github.com/vitorpamplona/amethyst/pull/3909)); la reposición de proofs de Cashu y la paginación del historial evitan que se trunquen los saldos de la wallet ([PR #3941](https://github.com/vitorpamplona/amethyst/pull/3941)); y ahora pueden silenciarse los chats públicos ([PR #3939](https://github.com/vitorpamplona/amethyst/pull/3939)).

Después de ese tag, las [listas de confianza](https://github.com/vitorpamplona/amethyst/pull/3983) de los kinds `30392` a `30395` se indexan con [NIP-50](/es/topics/nip-50/) (búsqueda de texto completo) solo por título, de modo que una lista mencionada en el texto pueda encontrarse sin indexar los ids hexadecimales de sus miembros. Los rechazos de la wallet recibidos mediante [NIP-47](/es/topics/nip-47/) (Nostr Wallet Connect) [ahora muestran el error en lugar de parecer un toque que no hizo nada](https://github.com/vitorpamplona/amethyst/pull/3987), incluidos `QUOTA_EXCEEDED` y `RESTRICTED`, además de un tiempo de espera cuando la wallet nunca responde.

### Mostro valida las órdenes firmadas antes del trabajo costoso y conserva los events de auditoría de órdenes

Tras la [base de escrow Cashu de v0.18.1](/en/newsletters/2026-08-12-newsletter/#mostro-0181-starts-a-cashu-escrow-path-and-hardens-the-daemon), [Mostro](https://github.com/MostroP2P/mostro), un daemon de intercambio entre pares que coordina órdenes mediante Nostr, publicó [v0.18.5](https://github.com/MostroP2P/mostro/releases/tag/v0.18.5), que usa de forma predeterminada [NIP-44](/es/topics/nip-44/) (cifrado del payload) para el transporte y mantiene gift wrap como una opción que debe activarse explícitamente.

El lanzamiento vincula los tiempos de espera del estado pendiente al momento registrado de la toma, para que la fianza de un maker no se recorte según el reloj equivocado ([PR #879](https://github.com/MostroP2P/mostro/pull/879)); envía el pago al comprador de cada orden liquidada una sola vez como máximo ([PR #881](https://github.com/MostroP2P/mostro/pull/881)); y procesa esos pagos mediante esperas `send_payment` limitadas y no bloqueantes ([PR #883](https://github.com/MostroP2P/mostro/pull/883)). Un cambio que intentaba pagar al ganador del recorte por tiempo agotado ([PR #875](https://github.com/MostroP2P/mostro/pull/875)) se revirtió antes de publicar el mismo tag ([PR #885](https://github.com/MostroP2P/mostro/pull/885)). Mostro también deja de volver a publicar un libro de órdenes pendientes sin cambios cada hora y al arrancar ([PR #888](https://github.com/MostroP2P/mostro/pull/888)), y sus dispute events kind `38386` ahora llevan un tag `created_at` para su ordenación posterior ([PR #878](https://github.com/MostroP2P/mostro/pull/878)).

Después de ese tag, ahora [se comprueba la firma antes del filtro de spam](https://github.com/MostroP2P/mostro/pull/892). Un event id no compromete `sig`, por lo que una copia del kind `14` de una víctima con una firma rota podía ocupar el espacio de repetición y descartar en silencio el mensaje válido; el daemon verifica primero y descarta un wrap no válido en vez de advertir y continuar.

Los events kind `8383` de auditoría de comisiones llevaban una caducidad de 15 días según [NIP-40](/es/topics/nip-40/) (marca temporal de expiración). Ahora [mantienen una caducidad de un año](https://github.com/MostroP2P/mostro/pull/924), acorde con su función de registro público de pagos. En un nodo con Cashu habilitado, tomar una orden [pide al vendedor mediante Nostr que bloquee un escrow 2 de 3](https://github.com/MostroP2P/mostro/pull/830), publica el waiting order event y omite la creación de una Lightning hold invoice. Esto completa la ruta de la solicitud, pero por sí solo no resuelve todos los casos de escrow ni de abuso del mercado.

### Napstr publica catálogos de audio en Nostr y transfiere archivos mediante Tor

[Napstr](https://github.com/lnbits/napstr) es un cliente de escritorio para compartir audio que publica catálogos consultables y seeders activos en Nostr, y después transfiere los archivos mediante un proceso Tor incluido, sin alternativa que use la IP directa. La [versión 0.2.0](https://github.com/lnbits/napstr/releases/tag/v0.2.0) mantiene públicos los perfiles y los metadatos del catálogo, y deja fuera de los relays las solicitudes, las credenciales de transferencia, el contenido de los archivos y las direcciones IP de los pares.

El descubrimiento emplea dos kinds de events addressable en el [repositorio de Napstr](https://github.com/lnbits/napstr). Las entradas de catálogo kind `30421` identifican un archivo por su resumen SHA-256, su nombre base público, su tamaño y su formato de audio; un autor retira un archivo reemplazando esa coordenada con un marcador de eliminado. Las señales de actividad de disponibilidad kind `30422` caducan tras diez minutos y enumeran los ids de archivo que el autor está dispuesto a distribuir, de modo que una fila del catálogo solo está activa mientras una señal sin caducar siga conteniendo ese resumen.

La conversación pública usa [NIP-C7](/es/topics/nip-c7/) (mensajes de chat kind 9) en lugar de un grupo controlado por un relay. El [repositorio de Napstr](https://github.com/lnbits/napstr) define una sala pública compartida y un debate por pista vinculado al resumen del archivo. Esos mensajes son firmados y públicos. No contienen direcciones onion, credenciales de transferencia ni bytes de archivos.

Una descarga comienza como una negociación por [NIP-17](/es/topics/nip-17/) (DM privados con gift wrap). El [repositorio de Napstr](https://github.com/lnbits/napstr) encapsula una solicitud, una oferta o un rechazo dentro de un rumor kind `14`, de modo que los relays no ven el nombre de host onion v3 temporal ni la capability de un solo uso que devuelve una oferta aceptada. A continuación, el Tor incluido transfiere los bytes mediante esa onion, verifica el resumen SHA-256 completo y vuelve a validar el audio antes de permitir la reproducción del archivo.

La [comparación entre v0.1.7 y v0.2.0](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0) añade colecciones de audiolibros y Napstrfy, un acompañante opcional para Android. Los manifests kind `30423` enumeran capítulos ordenados que siguen siendo archivos corrientes del catálogo, por lo que un cliente que ignore la colección aún puede obtener cada capítulo. Napstr crea para este fin una carpeta local Audiobooks sin destruir contenido. Napstrfy se empareja con un escritorio en ejecución mediante un código QR de un solo uso y después busca y solicita descargas a través de los servicios Nostr y Tor ya existentes en ese escritorio, sin recibir la clave secreta del equipo.

La misma [comparación](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0) agota el tiempo de una conexión con el acompañante que no se completa. Un seeder copia y calcula el hash del archivo compartido antes de servir sus bytes, escribe los datos entrantes en un archivo temporal privado, limita los destinos de audiolibros a un descendiente real de la carpeta de Napstr y aborta si ese destino cambia durante la transferencia.

## Lanzamientos

### MDK v0.9.17: los KeyPackages más recientes, actividad de miembros y envíos duraderos

[El boletín #37 cubrió MDK 0.9.14 y 0.9.15](/en/newsletters/2026-08-26-newsletter/#mdk-v0914-and-v0915-keypackage-selection-epoch-gap-recovery-and-split-relay-roles), incluido el cambio en el [repositorio de MDK](https://github.com/marmot-protocol/mdk) que sustituyó la selección del KeyPackage válido más antiguo por el paquete más reciente y válido del perfil actual, las barreras de recuperación de saltos de epoch, la limpieza de cuentas y la separación entre relays de descubrimiento y operativos. Esas correcciones siguen siendo la base de los dos lanzamientos posteriores, por lo que un paquete obsoleto ya no bloquea a un miembro que ya haya publicado uno utilizable.

[Los events de miembros y administración ahora hacen avanzar la lista de chats](https://github.com/marmot-protocol/mdk/pull/1551) igual que un mensaje nuevo: el texto de vista previa, el orden, los recuentos de no leídos y los marcadores de lectura se actualizan cuando las personas se unen, salen o cambian de función, y el actor local del sistema no se trata como un perfil de Nostr. Las reconexiones y los reinicios [reutilizan una única identidad de envío para reintentar un texto saliente duradero](https://github.com/marmot-protocol/mdk/pull/1516), de modo que el mismo mensaje de grupo no se publique dos veces.

Los dos lanzamientos posteriores se centran en el coste de mantener sanos los grupos grandes. La [versión 0.9.16](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.16) [mide la divergencia de epoch desde el epoch actual en lugar de usar un valor máximo histórico](https://github.com/marmot-protocol/mdk/pull/1559), mantiene disponibles para su obtención los inbound events rechazados ([PR #1565](https://github.com/marmot-protocol/mdk/pull/1565)), limita la reversión de replay al estado canónico del grupo ([PR #1563](https://github.com/marmot-protocol/mdk/pull/1563)) e introduce [marmot-c](https://github.com/marmot-protocol/mdk/pull/1545), una ABI de C generada mediante macros sobre los bindings de UniFFI que permite a los hosts integrar el motor directamente. Después, la [versión 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.17) agrupa los análisis de admisión en [un recorrido de miembros en vez de uno por cada miembro](https://github.com/marmot-protocol/mdk/pull/1617), [comprueba si el estado de un grupo está disputado sin cargar todo el grafo del historial](https://github.com/marmot-protocol/mdk/pull/1620), [reduce el coste de consulta inactiva del barrido deferred-peel](https://github.com/marmot-protocol/mdk/pull/1621) y [aplica la lectura de componentes por lotes a los tres puntos de proyección que omitió la primera pasada](https://github.com/marmot-protocol/mdk/pull/1622). Los artefactos correspondientes de [marmot-c 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/marmotc-v0.9.17) y [WN Agent 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/wn-agent-v0.9.17) se compilan desde el mismo commit, de modo que quienes los integran reciben conjuntamente las rutas de mantenimiento menos costosas.

### pakstr v0.16.0: identificadores kind-32267 al publicar

Tras el [pipeline de publicación en Zapstore de las versiones 0.13.0 a 0.15.0 de la semana pasada](/en/newsletters/2026-08-26-newsletter/#pakstr-0130-through-0150-makes-zapstore-publication-explicit), [pakstr](https://git.nostrdev.com/stuff/pakstr), una CLI que empaqueta una aplicación web en un APK de Android firmado y lo publica con una clave de Nostr, [registra los ids de los application events kind `32267`](https://git.nostrdev.com/stuff/pakstr/pulls/67) que busca, publica o reemplaza. La [versión 0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0) muestra tanto el id anterior como el nuevo cuando unos metadatos obsoletos del listado provocan una nueva publicación, para que el publisher pueda confirmar qué listing event está activo en el relay.

El mismo [registro de identificadores](https://git.nostrdev.com/stuff/pakstr/pulls/67) anota el id encontrado durante la búsqueda antes de cualquier reemplazo y después el id del event que llegó, por lo que una reutilización sin cambios aparece como un id repetido. Ese es el cambio etiquetado en [0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0); el comportamiento de Content-Digest, publicación antes de la carga y validación del publisher ya se había publicado en los tags anteriores.

## Cambios aún no publicados

### Zap Cooking limita los relays del bunker y firma los endpoints de pago

Al recargar una sesión de bunker en [Zap Cooking](https://github.com/zapcooking/frontend), un sitio de recetas construido sobre events de formato largo de Nostr, antes se publicaba la conversación cifrada de [NIP-46](/es/topics/nip-46/) (firma remota mediante relays) en todos los relays que ya usaba la página. [Limitar el tráfico del signer a los propios relays del bunker](https://github.com/zapcooking/frontend/pull/633) ahora aplica esa restricción al restaurar la sesión y durante el emparejamiento nostrconnect, el flujo de conexión iniciado por el signer, igual que en la ruta de acceso mediante una URL de bunker. Se niega a instalar un conjunto de relays vacío desde un registro almacenado con formato incorrecto, por lo que los relays que solo alojan recetas ya no descubren que el mismo pubkey mantiene una sesión de bunker activa.

La [autenticación HTTP firmada](https://github.com/zapcooking/frontend/pull/630) ahora protege el chat de pago del asistente de cocina, la introducción del recetario y las actualizaciones de recetas restringidas mediante [NIP-98](/es/topics/nip-98/) (autenticación HTTP con un event firmado de Nostr). El servidor lee una sola vez el cuerpo de la solicitud, verifica la firma contra ese payload exacto y obtiene la identidad del auth event verificado, en vez de una clave pública proporcionada en el cuerpo. La vista previa del chat sigue funcionando sin cabecera, mientras que una firma presente pero no válida se rechaza y la introducción del recetario siempre exige una firma. Actualizar una receta restringida ahora también requiere que la clave verificada coincida con el autor almacenado; a cualquier otra persona se le indica que la receta no existe, por lo que el endpoint no confirma qué registros de pago existen.

### nostrord corrige los DM encapsulados y los enlaces de events compartidos

Tras la [v2.9.0 de la semana pasada](/en/newsletters/2026-08-26-newsletter/#nostrord-v290-relay-scoped-group-state-and-media), [nostrord](https://github.com/nostrord/nostrord), un cliente multiplataforma para comunidades alojadas en relays, incorporó correcciones de entrega para que un DM [NIP-17](/es/topics/nip-17/) (DM privado con gift wrap) enviado desde un dispositivo llegue a la misma cuenta en otro. [Publicar de forma independiente la copia propia del remitente](https://github.com/nostrord/nostrord/pull/295) impide que la primera aceptación del wrap del destinatario por un relay descarte la copia que obtienen otros dispositivos. El mismo cambio vuelve a enviar un wrap después de que termine [NIP-42](/es/topics/nip-42/) (autenticación del cliente ante relays), y marca el envío como correcto tras la primera aceptación de un relay para que un host que falle no bloquee a los demás. [Reintentar los gift wraps aparcados](https://github.com/nostrord/nostrord/pull/297) cuya descodificación [NIP-59](/es/topics/nip-59/) (gift wrap) falló ahora sucede mediante un temporizador, por lo que un bunker que permanece conectado ya no deja esos mensajes sin... [truncado]

Una respuesta [NIP-C7](/es/topics/nip-c7/) (mensajes de chat kind `9`) repite su mensaje padre como puntero `nevent` [NIP-19](/es/topics/nip-19/) (entidades codificadas en bech32) al principio, junto al tag `q`. [Eliminar ese puntero inicial al mensaje padre](https://github.com/nostrord/nostrord/pull/292) cuando abre el cuerpo e identifica al padre de la respuesta permite que la fila se muestre como una única cita de respuesta, mientras que un puntero en mitad del cuerpo o uno que constituya todo el cuerpo sigue apareciendo como una tarjeta de cita. [Los enlaces a events citados ahora codifican `nevent`](https://github.com/nostrord/nostrord/pull/293) con el autor, el kind y el relay del que se leyó la cita, de modo que otro cliente pueda obtener un event [NIP-29](/es/topics/nip-29/) (grupos administrados por relays) compartido en un DM, en vez de recibir un identificador de nota desnudo sin indicaciones para localizarlo.

## Actualizaciones de NIPs y trabajo sobre especificaciones del protocolo

### Nostr Implementation Possibilities

Esta semana se incorporaron dos cambios de especificaciones en el [repositorio principal de NIPs](https://github.com/nostr-protocol/nips).

[NIP-67](/es/topics/nip-67/) define indicaciones que un relay puede añadir a un mensaje `EOSE` (fin de los events almacenados) para que un cliente sepa si debe seguir paginando. La [indicación `"auth"` incorporada](https://github.com/nostr-protocol/nips/pull/2371) añade un tercer valor junto a `finish` y `more`: ahora un relay puede señalar que podrían hacerse visibles más events almacenados si el usuario se autentica, y debe enviar el desafío `AUTH` de [NIP-42](/es/topics/nip-42/) (autenticación de relay) antes del `EOSE` que lleva la indicación. La [adición correspondiente a NIP-42](https://github.com/nostr-protocol/nips/pull/2371) define el mismo flujo desde el lado del cliente, de modo que un cliente que recibe un `EOSE` con `auth` ya dispone del desafío que debe responder.

[NIP-84](/es/topics/nip-84/) (resaltados portátiles, los events kind `9802` cuya compatibilidad incorporó Amethyst más arriba) [añadió una actualización del esquema de tags](https://github.com/nostr-protocol/nips/pull/2454): ahora los resaltados pueden marcar su fuente con tags `i` estructurados según [NIP-73](/es/topics/nip-73/) (identificadores de contenido externo), además de tags `a`/`e` para events de Nostr y tags `r` para todo lo demás; asimismo, al mostrarlos como un quote repost, los resaltados de citas pasaron de MUST a SHOULD.

### Nostr Wallet Connect

Una respuesta `list_transactions` puede indicar cuántas transacciones coinciden con la solicitud, no cuántas filas devolvió la página actual. El [`total_count` opcional incorporado](https://github.com/nostr-wallet-connect/nwc/pull/4) en NWC-05 (la extensión del historial de la wallet) dentro del [repositorio de extensiones de NWC](https://github.com/nostr-wallet-connect/nwc) añade ese campo a la respuesta usada con [NIP-47](/es/topics/nip-47/) (control remoto cifrado de la wallet mediante Nostr).

El [commit que añade `total_count`](https://github.com/nostr-wallet-connect/nwc/commit/ff3e49a47d040075edc46ee42fc0e33f10f1ef67) lo documenta como un entero opcional: el número total de transacciones que coinciden con los filtros de la solicitud.

El [commit que excluye la paginación del recuento](https://github.com/nostr-wallet-connect/nwc/commit/06315e735f744b1afd3df0b57436fdce8a7bfc2e) indica que este total excluye la paginación, por lo que cuenta todas las transacciones coincidentes en todas las páginas.

## NIPs en profundidad: Reposts y reacciones

Un contacto puede volver a poner una nota existente ante sus seguidores y adjuntar un «me gusta», «no me gusta» o emoji compacto sin escribir una respuesta. [NIP-18](/es/topics/nip-18/) (reposts) publica esa redistribución como su propio event firmado. [NIP-25](/es/topics/nip-25/) (reacciones) publica la respuesta compacta como un event firmado independiente. Ambos siguen siendo archivos `draft` `optional` en la [especificación canónica de reposts](https://github.com/nostr-protocol/nips/blob/master/18.md) y la [especificación canónica de reacciones](https://github.com/nostr-protocol/nips/blob/master/25.md): están presentes en el repositorio de NIPs y los implementan los clientes, pero continúan marcados como no definitivos.

### Reposts (NIP-18)

Los seguidores reciben un puntero firmado a una nota de texto kind 1 que alguien ya publicó cuando un cliente escribe un event kind 6. La [especificación de reposts](https://github.com/nostr-protocol/nips/blob/master/18.md) establece `kind` en 6, coloca en `content` el JSON serializado de esa nota (se permite un `content` vacío, aunque no se recomienda), exige un tag `e` cuyo valor sea el `id` de la nota y cuya tercera entrada sea la URL de un relay donde pueda obtenerse, e indica que el event SHOULD incluir también un tag `p` con el `pubkey` del autor original. Un repost de un event de [NIP-70](/es/topics/nip-70/) (events protegidos) SHOULD mantener `content` vacío para no copiar el payload protegido al nuevo event.

Una cita es una referencia dentro de algún otro event, no un envoltorio kind 6. Cuando un cliente menciona un `nevent`, `note` o `naddr` de [NIP-21](/es/topics/nip-21/) (URI `nostr:`), debe convertir esa mención en un tag `q` con la forma `["q", "<event-id> or <event-address>", "<relay-url>", "<pubkey-if-a-regular-event>"]`. Los [tags de quote repost](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts) mantienen esas citas fuera de los hilos de respuestas y permiten que los clientes obtengan y cuenten las citas de una publicación.

Kind 6 está reservado para notas kind 1. Un repost genérico kind 16 puede envolver cualquier event kind distinto de kind 1. SHOULD incluir un tag `k` cuyo valor sea el kind serializado del event interior. Cuando ese event interior sea reemplazable, el repost genérico SHOULD añadir un tag `a` con la coordenada `kind:pubkey:d-tag`; si falta ese tag `a`, el repost apunta a una versión concreta y `content` debe contener la cadena JSON completa de esa versión. Las [reglas de reposts genéricos](https://github.com/nostr-protocol/nips/blob/master/18.md#generic-reposts) evitan que los events de formato largo, addressable y otros que no sean notas se publiquen como si fueran kind 1.

El siguiente event kind 6 es un repost real recuperado de `wss://relay.damus.io` durante el montaje ([abrir el event](https://njump.me/nevent1qqs88k8xgv2d3d3yymawaa24f22a0kqqvknpur0p05vq9e5r4y74xjspz3mhxue69uhhyetvv9ujuerpd46hxtnfdu7elvca)):

```json
{
  "kind": 6,
  "id": "73d8e64314d8b62426faeef5554a95d7d80065a61e0de17d1802e683a93d534a",
  "pubkey": "a60e79e0edad5100d7543b669e513dbc1c2170e8e9b74fdb8e971afd1e0e6813",
  "created_at": 1787768621,
  "tags": [
    [
      "e",
      "38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976"
    ],
    [
      "p",
      "34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095"
    ],
    [
      "client",
      "Primal iOS"
    ]
  ],
  "content": "{\"pubkey\":\"34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095\",\"sig\":\"8c0271f7b438083ce491c391335598e0cbceee0758177cf98f7894531033cb5153704b01009590f3d4e9cdfadd5bbf73fc5eea54186fcbac6d30744e0e6c1cd6\",\"id\":\"38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976\",\"tags\":[[\"r\",\"https:\/\/stacker.news\/items\/1555439\"],[\"client\",\"Damus\"]],\"created_at\":1787766056,\"content\":\"🚨 Attention CLN (Core Lightning) node runners 🚨\n\nhttps:\/\/stacker.news\/items\/1555439\",\"kind\":1}",
  "sig": "b6b97fa377cfdb651e2850f65f2ccb12ca0724c0de0fc0e39e9721f850abdfd31f5d5567517a51d988145c2a2de9ae9540b02eecf7352e554022870d5e8c64a5"
}
```

Su `kind` es 6, el tag `e` apunta a la nota republicada, el tag `p` identifica al autor de esa nota y `content` contiene el event kind 1 original como JSON serializado. Este event recuperado de un relay omite la indicación del relay que la [especificación NIP-18](https://github.com/nostr-protocol/nips/blob/master/18.md) marca como obligatoria, lo que ilustra por qué los lectores y clientes deben validar los events reales y admitir productores que omiten campos.

### Reacciones (NIP-25)

Una publicación puede acumular «me gusta», «no me gusta» y emoji firmados sin que esas marcas entren en el hilo de respuestas. La [especificación de reacciones](https://github.com/nostr-protocol/nips/blob/master/25.md) define esa marca como un event kind 7 cuyo `content` MUST contener el valor de la reacción. `+` o una cadena vacía MUST interpretarse como un «me gusta» o voto positivo. `-` MUST interpretarse como un «no me gusta» o voto negativo. Un emoji o un shortcode de [NIP-30](/es/topics/nip-30/) (emoji personalizado) SHOULD NOT interpretarse como un «me gusta» o «no me gusta», y un cliente MAY mostrar ese emoji en la publicación.

El objetivo está en los tags, no se deduce de `content`. MUST haber un tag `e` establecido en el `id` del event objetivo, y ese tag SHOULD incluir una indicación de relay; no se recomiendan tags `e` adicionales y, si aparecen, el `id` objetivo debe ser el último. SHOULD haber un tag `p` para el autor objetivo, el último si aparecen varios tags `p`. Un objetivo addressable SHOULD recibir además un tag `a` con coordenadas `kind:pubkey:d-tag`. Los tags `e` y `a` SHOULD incluir indicaciones de relay y pubkey, los tags `p` SHOULD incluir indicaciones de relay y un tag `k` MAY contener el kind serializado del event que recibió la reacción. [Esas reglas de tags](https://github.com/nostr-protocol/nips/blob/master/25.md#tags) permiten a un cliente obtener el objetivo y notificar a su autor solo a partir del reaction event.

Un cliente MAY poner un único `:shortcode:` en `content` y un tag `emoji` que asocie ese shortcode con la URL de una imagen, según las [reglas de reacciones con emoji personalizados](https://github.com/nostr-protocol/nips/blob/master/25.md#custom-emoji-reaction). Si el objetivo no es un event nativo de Nostr, la reacción MUST ser kind 17 y MUST incluir los tags `k` e `i` de [NIP-73](/es/topics/nip-73/) (ids de contenido externo), como establecen las [reglas de reacciones a contenido externo](https://github.com/nostr-protocol/nips/blob/master/25.md#external-content-reactions). Kind 17 es una reacción a un sitio web, un episodio de podcast u otro objeto externo. No es una reacción de event a event kind 7 ni un repost.

El siguiente event kind 7 es una reacción real recuperada de `wss://relay.damus.io` durante el montaje ([abrir el event](https://njump.me/nevent1qqsytac63l00k7kyaphkfwqqn94wglmx78v6zhqtytg65w5k957luccpz3mhxue69uhhyetvv9ujuerpd46hxtnfdus63jym)):

```json
{
  "kind": 7,
  "id": "45f71a8fdefb7ac4e86f64b800996ae47f66f1d9a15c0b22d1aa3a962d3dfe63",
  "pubkey": "0755cc2b972c3cbcae36913109c50b36b3fe110fa38a76dc37d1f01c5305496a",
  "created_at": 1787768605,
  "tags": [
    [
      "e",
      "519de32071d71bb2ab8b71a07e03eb9a256b6a59f9b08877b156c80966d5c320"
    ],
    [
      "a",
      "34236:5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb:2ddda68516f4729d3ef55a1eb01fe028253393212493a34816ad8eb79f97a3b7"
    ],
    [
      "p",
      "5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb"
    ],
    [
      "k",
      "34236"
    ],
    [
      "client",
      "Divine",
      "31990:d95aa8fc0eff8e488952495b8064991d27fb96ed8652f12cdedc5a4e8b5ae540:divine-mobile",
      "wss://relay.divine.video"
    ]
  ],
  "content": "+",
  "sig": "3c081756c7a73e2ee8aa10fadf3b5009390d5ac9a72078ba03701c42af91022ef275df7cb17724689a23dca4e29ff1a7cd5e3a24135d021983e2726a28b00b1e"
}
```

Su `content` es `+`, el «me gusta» convencional de [NIP-25](https://github.com/nostr-protocol/nips/blob/master/25.md). El tag `e` identifica el event que recibió la reacción; el tag `a` añade su coordenada addressable; el tag `p` identifica a su autor; y el tag `k` opcional registra como cadena el kind del objetivo.

### Implementaciones actuales en clientes

[Amethyst](https://github.com/vitorpamplona/amethyst), un cliente Android de Nostr, define el [tipo de repost event](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip18Reposts/RepostEvent.kt) y el [tipo de reaction event](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip25Reactions/ReactionEvent.kt) en su capa de protocolo actual.

[Snort](https://github.com/v0l/snort), un cliente web de Nostr, implementa [helpers de NIP-18 que incluyen la gestión de tags de enlaces de citas](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip18.ts) y [crea tags de reacciones a events NIP-25](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip25.ts).

[Ditto](https://github.com/soapbox-pub/ditto), un servidor Mastodon y relay de Nostr combinado, [publica reposts genéricos kind 16 con un tag `k` y una coordenada `a` en objetivos addressable](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/components/RepostMenu.tsx) y [aplica la semántica de las reacciones kind 7 tratando el último tag `e` como event objetivo](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/lib/nostrEvents.ts).

### Cómo funcionan conjuntamente

Un event kind 6 o kind 16 redistribuye un event existente en los feeds de los seguidores de quien hace el repost, ya sea incorporando el JSON de ese event o apuntando a una coordenada reemplazable. Un tag `q` marca una cita dentro de otro event para que la reconstrucción del hilo pueda contar las referencias sin tratar el event que cita como respuesta, que es la separación descrita en la [sección sobre quote reposts](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts). Un event kind 7 deja en su sitio el event original y adjunta únicamente el valor de la reacción y los tags del objetivo, tal como establece la [especificación de reacciones](https://github.com/nostr-protocol/nips/blob/master/25.md). Por tanto, los clientes que obtienen un pubkey ven los reposts de ese pubkey como nuevos events kind 6 o 16 y sus opiniones como events kind 7 sobre las publicaciones de otras personas.

---

Envíe un DM NIP-17 para compartir un proyecto o una noticia mediante el [proyecto Nostr Compass](https://github.com/andotherstuff/nostr-compass).
