---
title: "Nostr Compass #38"
date: 2026-09-02
publishDate: 2026-09-02
translationOf: /en/newsletters/2026-09-02-newsletter.md
translationDate: 2026-09-02
draft: false
type: newsletters
description: "Voca 1.0 lleva la lectura verificada de Nostr a una aplicación de texto a voz sin conexión, nostream amplía el enrutamiento de trabajos y la autenticación del lado del relay, Napstr publica catálogos de audio basados en Tor, MDK 0.9.17 reduce el coste de mantenimiento de grupos, los NIPs principales incorporan una indicación de paginación y tags de destacados junto con totales de transacciones NWC, y el análisis detallado de NIPs explica los reposts y las reacciones."
---

Bienvenidos de nuevo a [Nostr Compass](https://nostrcompass.org), su guía semanal de Nostr.

**Esta semana:** [Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) 1.0 lleva notas verificadas de Nostr y suscripciones de formato largo a un lector Android sin conexión que lee artículos en voz alta; [nostream](https://github.com/cameri/nostream) amplía el enrutamiento de trabajos del lado del relay y el funcionamiento autenticado; [NDK for Dart](https://github.com/relaystr/ndk) corrige negentropy y la duración de solicitudes a múltiples relays; [Divine Mobile](https://github.com/divinevideo/divine-mobile) hace deterministas la eliminación y la firma de mensajes envueltos; [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay) protege de forma predeterminada las bandejas de entrada de gift wrap; [Amethyst](https://github.com/vitorpamplona/amethyst) incorpora destacados portátiles; y [Mostro](https://github.com/MostroP2P/mostro) verifica las órdenes firmadas antes de su filtro de spam. [Napstr](https://github.com/lnbits/napstr) publica catálogos de audio y señales de actividad de seeders en Nostr mientras transfiere archivos mediante Tor. Los lanzamientos incluyen [MDK](https://github.com/marmot-protocol/mdk) y [pakstr](https://git.nostrdev.com/stuff/pakstr); el trabajo de protocolo incorpora una indicación de paginación de [NIP-67](/es/topics/nip-67/) y un esquema de tags para destacados de [NIP-84](/es/topics/nip-84/) en el [repositorio de NIPs](https://github.com/nostr-protocol/nips), mientras [Nostr Wallet Connect](https://github.com/nostr-wallet-connect/nwc) añade totales de transacciones; y el análisis detallado de NIPs recorre los reposts y las reacciones a través de sus estructuras de event y sus implementaciones actuales.

## Historias destacadas

### Voca 1.0 lee en voz alta notas verificadas de Nostr y suscripciones en Android

[Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) es un lector Android sin conexión que lee en voz alta artículos, PDF, archivos Markdown y notas de Nostr con la propia voz de texto a voz del teléfono, mientras la frase pronunciada permanece resaltada en la página. Su [lanzamiento 1.0](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en), [publicado el 2026-08-27](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) con su propia [clave de proyecto](https://njump.me/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu), convierte a Nostr en una fuente de primera clase: pegue la dirección de una nota, un identificador de event, un npub, un perfil o un enlace web común que contenga una entidad Nostr, y la aplicación decodifica la referencia, obtiene de los relays el event firmado y lee el texto del autor en lugar de la página web construida a su alrededor.

Dos comportamientos verificados definen la integración con Nostr, ambos descritos en el [anuncio firmado de Voca 1.0](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en). Primero, cada event obtenido se comprueba frente a su id recalculado y su firma Schnorr BIP-340 antes de guardarlo, usando los relays de arranque, la lista de relays [NIP-65](/es/topics/nip-65/) del autor (un event kind `10002` firmado y reemplazable donde un autor enumera los relays en los que lee y escribe) y las indicaciones incluidas en la propia referencia, de modo que un relay puede negarse a responder, pero no poner palabras en boca de un autor. Segundo, añadir el npub de un autor coloca sus artículos de formato largo [NIP-23](/es/topics/nip-23/) (publicaciones direccionables kind `30023` con títulos, resúmenes e imágenes) en una única bandeja de entrada del dispositivo junto a los feeds RSS y Atom. La actualización 1.1.0, [anunciada el 2026-08-28](https://gitworkshop.dev/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu/voca) y publicada en [Zapstore](https://zapstore.dev) el 2026-08-29, sincroniza el desplazamiento frase por frase, suaviza los documentos largos y recupera el widget de la pantalla de inicio tras el desplazamiento manual, el cambio de tamaño, los reinicios del proceso y las actualizaciones.


### nostream amplía el enrutamiento DVM del lado del relay y el funcionamiento autenticado

Tras el [trabajo de ingesta de tareas del 19 de agosto](/en/newsletters/2026-08-19-newsletter/#nostream-adds-a-relay-monitor-and-mints-invite-codes), [nostream](https://github.com/cameri/nostream), una implementación de relay en TypeScript, [almacena y sirve events de manejadores de aplicaciones NIP-89](https://github.com/cameri/nostream/pull/737). [NIP-89](/es/topics/nip-89/) (descubrimiento de manejadores de aplicaciones) utiliza recomendaciones kind `31989` e información de manejadores kind `31990`, ambas ya dentro del intervalo parametrizado y reemplazable, para que un cliente pueda consultar esos kinds y recibir un reemplazo cuando coincida un tag `d`. El relay no publica información de manejadores para sus propios workers.

Los trabajos pendientes de [NIP-90](/es/topics/nip-90/) (data vending machine) ahora [llegan a un proceso worker y regresan como events de resultado](https://github.com/cameri/nostream/pull/734). Si todo va bien, el relay firma un resultado kind 6000-6999 con su propia clave. Un tiempo de espera agotado o un fallo del worker marca el trabajo como fallido en lugar de dejarlo como enviado.

Las sesiones autenticadas y las llamadas HTTP de administración se sitúan en límites distintos. [NIP-42](/es/topics/nip-42/) (autenticación de clientes ante relays) [registra la pubkey autenticada por socket](https://github.com/cameri/nostream/pull/716), puede exigir AUTH antes de que los clientes publiquen events y anuncia ese requisito en el documento [NIP-11](/es/topics/nip-11/) (información del relay), con ambos controles desactivados de forma predeterminada. Por separado, [las rutas API de administración pueden aceptar autorización HTTP firmada con NIP-98](https://github.com/cameri/nostream/pull/730). [NIP-98](/es/topics/nip-98/) (autenticación HTTP con events firmados) permanece desactivado hasta que un operador lo habilita e indica las pubkeys permitidas.

### NDK for Dart corrige negentropy, la duración de solicitudes a múltiples relays y la verificación de firmas

Una ejecución de [NIP-77](/es/topics/nip-77/) (conciliación de conjuntos mediante negentropy) en [NDK](https://github.com/relaystr/ndk), un kit de desarrollo en Dart para Nostr, devolvía conjuntos erróneos de elementos disponibles y necesarios sin generar errores porque el códec no hablaba la versión v1 del protocolo [negentropy](/es/topics/negentropy/). La [corrección de la codificación v1](https://github.com/relaystr/ndk/pull/722) devuelve ahora los ids que posee el relay y los ids que todavía necesita.

Los filtros idénticos enviados a distintos relays [se estaban fusionando en una única solicitud](https://github.com/relaystr/ndk/pull/705). Las solicitudes con el mismo filtro ahora permanecen separadas cuando apuntan a distintos relays o tienen distinta duración, por lo que una consulta breve no puede mezclar events de otro relay en el resultado ni dejar bloqueada una suscripción activa.

El mismo kit [verifica una firma una sola vez y conserva ese resultado](https://github.com/relaystr/ndk/pull/726). Una entrega duplicada posterior ya no consume otra comprobación ni sobrescribe el event verificado almacenado.

### Divine Mobile hace deterministas la eliminación y la firma de mensajes directos envueltos

Los events kind `5` envueltos de [NIP-09](/es/topics/nip-09/) (solicitud de eliminación de event) dirigidos a un mensaje nunca se aplicaban en [Divine Mobile](https://github.com/divinevideo/divine-mobile), un cliente móvil de vídeos cortos que publica mediante Nostr. El cliente [ahora resuelve cada eliminación respecto al mensaje indicado](https://github.com/divinevideo/divine-mobile/pull/8174), en lugar de considerar ya procesado todo lo que no sea una reacción. Una segunda [solicitud de eliminar para todos mientras la primera aún estaba en curso](https://github.com/divinevideo/divine-mobile/pull/8164) desaparecía sin errores y sin ningún kind `5` en la red; ahora cada eliminación simultánea se publica.

Tras el lanzamiento 1.0.22 ya cubierto, enviar dos veces en un segundo el mismo texto 1:1 de [NIP-17](/es/topics/nip-17/) (mensajes directos privados con gift wrap) [creaba un único id de rumor](https://github.com/divinevideo/divine-mobile/pull/8163), por lo que el segundo envío desaparecía; ahora cada envío lleva un token dentro del rumor de [NIP-59](/es/topics/nip-59/) (gift wrap) para que los ids sean distintos.

Un llamante que ya había firmado un event kind `4` o kind `5` [conservaba esa firma](https://github.com/divinevideo/divine-mobile/pull/8173), en lugar de que se añadiera después un tag de cliente, lo que cambiaba el id y hacía que los relays rechazaran el event por no ser válido.

### Conduit Relay refuerza su bandeja de entrada protegida con NIP-42

Los gift wraps kind `1059` se almacenan para un destinatario. [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay), un relay en Go que conserva esos wraps en una bandeja protegida para el destinatario, [adopta de forma predeterminada el modo de aplicación obligatoria](https://github.com/Conduit-BTC/conduit-relay/pull/8): una consulta kind `1059` debe presentar autenticación [NIP-42](/es/topics/nip-42/) como ese destinatario o el relay rechaza la solicitud. Los filtros de varios kinds, comodines, recuentos y [negentropy](/es/topics/negentropy/) sobre esos wraps están `restricted`, por lo que otro AUTH no puede convertirlos en un volcado de la bandeja de entrada ajena.

La misma [incorporación de la bandeja de entrada protegida](https://github.com/Conduit-BTC/conduit-relay/pull/8) exige un id de event canónico en el event AUTH transmitido y acepta un event NIP-42 válido en los demás aspectos, tenga o no vacío el `content`. El modo de solo desafío sigue ofreciendo AUTH sin bloquear la lectura; el modo desactivado permite el acceso libre. El valor predeterminado de la biblioteca es el modo de aplicación obligatoria.

### Amethyst incorpora destacados NIP-84 y corrige dos rutas de fallo frente a relays

Tras el [trabajo de autorización de Blossom de la semana pasada](/en/newsletters/2026-08-26-newsletter/#amethyst-moves-blossom-authorization-off-image-loading-threads), [Amethyst](https://github.com/vitorpamplona/amethyst), un cliente Android de Nostr, publica [v1.14.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.14.0) con [NIP-84](/es/topics/nip-84/) (destacados portátiles). Un pasaje seleccionado se convierte en un event kind `9802` desde el editor, un feed de destacados o al compartirlo con la aplicación.

El lanzamiento añade controles de eliminación y archivado de canales [NIP-29](/es/topics/nip-29/) ([PR #3812](https://github.com/vitorpamplona/amethyst/pull/3812)) y mide el comportamiento de los relays a través del tráfico que el cliente ya genera; después amplía esas pruebas [NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) con comprobaciones de streaming, lectura, escritura y URL ([PR #3836](https://github.com/vitorpamplona/amethyst/pull/3836), [PR #3857](https://github.com/vitorpamplona/amethyst/pull/3857)). Amethyst también elimina una vulnerabilidad de colisión de hash en SharedKeyCache y compara códigos de autenticación de mensajes en tiempo constante ([PR #3833](https://github.com/vitorpamplona/amethyst/pull/3833)), corrige una condición de carrera que podía perder la entrega de AUTH durante la conexión ([PR #3838](https://github.com/vitorpamplona/amethyst/pull/3838)), divide el bloqueo del estado de las suscripciones para acabar con una cola de ANR ([PR #3851](https://github.com/vitorpamplona/amethyst/pull/3851)) y compara todos los filtros de suscripción en lugar de solo el primero ([PR #3856](https://github.com/vitorpamplona/amethyst/pull/3856)).

[El boletín #36 ya cubrió estos cambios de autenticación de relays, copias de seguridad y chats públicos](/en/newsletters/2026-08-19-newsletter/#amethyst-rebuilds-its-relay-authentication-decision-flow); v1.14.0 los publica ahora juntos. Los bloqueos suaves de Concord cierran brechas de autoridad detectadas por una auditoría ([PR #3885](https://github.com/vitorpamplona/amethyst/pull/3885)). La autenticación de relays tiene un flujo de permisos rediseñado ([PR #3899](https://github.com/vitorpamplona/amethyst/pull/3899)), espera la resolución del desafío en lugar de agotar el tiempo ([PR #3905](https://github.com/vitorpamplona/amethyst/pull/3905)), configura las cuentas nuevas para autenticarse de forma predeterminada ([PR #3931](https://github.com/vitorpamplona/amethyst/pull/3931)), respeta esa preferencia en relays ajenos al conjunto habitual de la cuenta ([PR #3937](https://github.com/vitorpamplona/amethyst/pull/3937)) y conserva las concesiones de sesión entre reconexiones ([PR #3955](https://github.com/vitorpamplona/amethyst/pull/3955)). Un flujo guiado de primer inicio y de Ajustes facilita encontrar las copias de seguridad de las claves ([PR #3909](https://github.com/vitorpamplona/amethyst/pull/3909)), el relleno histórico de pruebas Cashu y la paginación del historial evitan que se trunquen los saldos de la cartera ([PR #3941](https://github.com/vitorpamplona/amethyst/pull/3941)), y ahora se pueden silenciar los chats públicos ([PR #3939](https://github.com/vitorpamplona/amethyst/pull/3939)).

Después de ese tag, las [listas de confianza](https://github.com/vitorpamplona/amethyst/pull/3983) de los kinds `30392` a `30395` se indexan mediante [NIP-50](/es/topics/nip-50/) (búsqueda de texto completo) solo por título, por lo que una lista mencionada en el texto se puede encontrar sin indexar los ids hexadecimales de sus miembros. Los rechazos de carteras recibidos mediante [NIP-47](/es/topics/nip-47/) (Nostr Wallet Connect) [ahora muestran su error en lugar de parecer un toque que no hizo nada](https://github.com/vitorpamplona/amethyst/pull/3987), incluidos `QUOTA_EXCEEDED` y `RESTRICTED`, además de un tiempo de espera cuando la cartera nunca responde.

### Mostro valida las órdenes firmadas antes del trabajo costoso y conserva los events de auditoría de órdenes

Tras la [base de depósito en garantía Cashu de v0.18.1](/en/newsletters/2026-08-12-newsletter/#mostro-0181-starts-a-cashu-escrow-path-and-hardens-the-daemon), [Mostro](https://github.com/MostroP2P/mostro), un daemon de intercambio entre pares que coordina órdenes mediante Nostr, etiquetó [v0.18.5](https://github.com/MostroP2P/mostro/releases/tag/v0.18.5), que usa de forma predeterminada [NIP-44](/es/topics/nip-44/) (cifrado de payload) para el transporte y mantiene gift wrap como opción explícita.

El lanzamiento vincula los tiempos de espera del estado de espera al momento de toma registrado para que no se penalice la fianza de un creador según el reloj equivocado ([PR #879](https://github.com/MostroP2P/mostro/pull/879)), envía como máximo una vez cada pago al comprador de una orden liquidada ([PR #881](https://github.com/MostroP2P/mostro/pull/881)) y procesa esos pagos mediante esperas acotadas y no bloqueantes de `send_payment` ([PR #883](https://github.com/MostroP2P/mostro/pull/883)). Un intento de cambio para pagar al ganador de la penalización por tiempo agotado ([PR #875](https://github.com/MostroP2P/mostro/pull/875)) se revirtió antes de publicar el mismo tag ([PR #885](https://github.com/MostroP2P/mostro/pull/885)). Mostro también deja de volver a publicar cada hora y al iniciarse un libro de órdenes pendientes sin cambios ([PR #888](https://github.com/MostroP2P/mostro/pull/888)), y sus events de disputas kind `38386` ahora llevan un tag `created_at` para su ordenación posterior ([PR #878](https://github.com/MostroP2P/mostro/pull/878)).

Después de ese tag, una [comprobación de firma se ejecuta ahora antes del filtro de spam](https://github.com/MostroP2P/mostro/pull/892). Un id de event no compromete `sig`, por lo que una copia del kind `14` de una víctima con una firma dañada podía ocupar el espacio de repetición y descartar silenciosamente el mensaje válido; el daemon verifica primero y descarta un wrap no válido en lugar de advertir y continuar.

Los events de auditoría de comisiones kind `8383` llevaban una marca de tiempo de vencimiento de 15 días según [NIP-40](/es/topics/nip-40/). Ahora [mantienen un vencimiento de un año](https://github.com/MostroP2P/mostro/pull/924), acorde con su función de registro público de pagos. En un nodo con Cashu habilitado, tomar una orden [pide al vendedor mediante Nostr que bloquee un depósito en garantía 2 de 3](https://github.com/MostroP2P/mostro/pull/830), publica el event de orden en espera y omite la creación de una factura Lightning retenida. Esto completa la ruta de solicitud; no resuelve por sí solo todos los casos de cierre de depósitos ni de abuso del mercado.

### Napstr publica catálogos de audio en Nostr y transfiere archivos mediante Tor

[Napstr](https://github.com/lnbits/napstr) es un cliente de escritorio para compartir audio que publica en Nostr catálogos consultables y seeders activos, y después transfiere los archivos mediante un proceso Tor incluido, sin alternativa de IP directa. [La versión 0.2.0](https://github.com/lnbits/napstr/releases/tag/v0.2.0) mantiene públicos los perfiles y los metadatos del catálogo, y mantiene fuera de los relays las solicitudes, las credenciales de transferencia, el contenido de los archivos y las direcciones IP de los pares.

El descubrimiento utiliza dos kinds de events direccionables en el [repositorio de Napstr](https://github.com/lnbits/napstr). Las entradas de catálogo kind `30421` identifican un archivo mediante su resumen SHA-256, nombre base público, tamaño y formato de audio, y un autor retira un archivo sustituyendo esa coordenada por un marcador de eliminación. Las señales de actividad de disponibilidad kind `30422` caducan tras diez minutos y enumeran los ids de archivos que el autor está dispuesto a distribuir, por lo que una fila del catálogo solo está activa mientras una señal no vencida siga conteniendo ese resumen.

La conversación pública utiliza [NIP-C7](/es/topics/nip-c7/) (mensajes de chat kind 9) en lugar de un grupo propiedad de un relay. El [repositorio de Napstr](https://github.com/lnbits/napstr) define una sala pública compartida y una conversación por pista vinculada al resumen del archivo. Esos mensajes son firmados y públicos. No contienen direcciones onion, credenciales de transferencia ni bytes de archivos.

Una descarga empieza como una negociación mediante [NIP-17](/es/topics/nip-17/) (mensajes directos privados con gift wrap). El [repositorio de Napstr](https://github.com/lnbits/napstr) envuelve una solicitud, una oferta o un rechazo dentro de un rumor kind `14`, por lo que los relays no ven el nombre de host onion v3 temporal ni la capacidad de un solo uso que devuelve una oferta aceptada. Tor, incluido con la aplicación, transfiere después los bytes mediante esa dirección onion, verifica el resumen SHA-256 completo y vuelve a validar el audio antes de permitir reproducir el archivo.

La [comparación entre v0.1.7 y v0.2.0](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0) añade colecciones de audiolibros y Napstrfy, un complemento Android opcional. Los manifiestos kind `30423` enumeran capítulos ordenados que siguen siendo archivos de catálogo comunes, por lo que un cliente que ignore la colección aún puede obtener cada capítulo. Napstr crea para ello una carpeta local Audiobooks de forma no destructiva. Napstrfy se vincula a una aplicación de escritorio en ejecución mediante un código QR de un solo uso y después busca y solicita descargas mediante los servicios Nostr y Tor ya existentes en esa aplicación, sin recibir su clave secreta.

La misma [comparación](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0) agota el tiempo de una vinculación con el complemento que no se completa. Un seeder copia y calcula el hash del archivo compartido antes de servir bytes, escribe los datos entrantes en un archivo temporal privado, limita los destinos de audiolibros a un subdirectorio real de la carpeta Napstr e interrumpe la operación si ese destino cambia durante la transferencia.

## Lanzamientos

### MDK v0.9.17: los KeyPackages más recientes, actividad de miembros y envíos duraderos

[El boletín #37 cubrió MDK 0.9.14 y 0.9.15](/en/newsletters/2026-08-26-newsletter/#mdk-v0914-and-v0915-keypackage-selection-epoch-gap-recovery-and-split-relay-roles), incluido el cambio en el [repositorio de MDK](https://github.com/marmot-protocol/mdk) desde la selección del KeyPackage más antiguo hacia el paquete válido más reciente del perfil actual, las barreras de recuperación de desfases de epoch, la limpieza de cuentas y la separación entre relays de descubrimiento y operativos. Esas correcciones siguen siendo la base de los dos lanzamientos posteriores, por lo que un paquete obsoleto ya no bloquea a un miembro que ya haya publicado uno utilizable.

[Los events de miembros y administradores ahora hacen avanzar la lista de chats](https://github.com/marmot-protocol/mdk/pull/1551) igual que un mensaje nuevo: el texto de vista previa, el orden, los recuentos de no leídos y los marcadores de lectura se actualizan cuando las personas se unen, se marchan o cambian de rol, y el actor local del sistema no se trata como un perfil de Nostr. Las reconexiones y los reinicios [reutilizan una identidad de envío para un texto saliente duradero que se vuelve a intentar](https://github.com/marmot-protocol/mdk/pull/1516), por lo que el mismo mensaje de grupo no se publica dos veces.

Los dos lanzamientos posteriores se concentran en el coste de mantener saludables los grupos grandes. [La versión 0.9.16](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.16) [mide la divergencia de epoch desde el epoch actual en lugar de una marca máxima](https://github.com/marmot-protocol/mdk/pull/1559), mantiene accesibles para su obtención los events entrantes rechazados ([PR #1565](https://github.com/marmot-protocol/mdk/pull/1565)), limita la reversión de repetición al estado canónico del grupo ([PR #1563](https://github.com/marmot-protocol/mdk/pull/1563)) e introduce [marmot-c](https://github.com/marmot-protocol/mdk/pull/1545), una ABI de C generada mediante macros sobre los bindings de UniFFI que permite a los hosts integrar el motor directamente. [La versión 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.17) combina después los recorridos de admisión de pases en [un solo recorrido de miembros en lugar de uno por cada miembro](https://github.com/marmot-protocol/mdk/pull/1617), [comprueba si el estado de un grupo está en disputa sin sembrar todo el grafo histórico](https://github.com/marmot-protocol/mdk/pull/1620), [reduce el coste de sondeo inactivo del barrido diferido](https://github.com/marmot-protocol/mdk/pull/1621) y [aplica la lectura por lotes de componentes a los tres puntos de proyección que omitió la primera pasada](https://github.com/marmot-protocol/mdk/pull/1622). Los artefactos correspondientes [marmot-c 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/marmotc-v0.9.17) y [WN Agent 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/wn-agent-v0.9.17) se compilan desde el mismo commit, por lo que quienes integran el motor reciben a la vez las rutas de mantenimiento más económicas.


### pakstr v0.16.0: identificadores kind-32267 al publicar

Tras el [proceso de publicación en Zapstore de las versiones 0.13.0 a 0.15.0 de la semana pasada](/en/newsletters/2026-08-26-newsletter/#pakstr-0130-through-0150-makes-zapstore-publication-explicit), [pakstr](https://git.nostrdev.com/stuff/pakstr), una CLI que empaqueta una aplicación web en un APK Android firmado y lo publica con una clave Nostr, [registra los IDs de events de aplicación kind `32267`](https://git.nostrdev.com/stuff/pakstr/pulls/67) que consulta, publica o reemplaza. [La versión 0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0) imprime tanto el ID anterior como el nuevo cuando unos metadatos de listado obsoletos provocan una nueva publicación, de modo que un editor puede confirmar qué event de listado está activo en el relay.

El mismo [registro de identificadores](https://git.nostrdev.com/stuff/pakstr/pulls/67) anota el ID encontrado durante la consulta antes de cualquier reemplazo y después el ID del event que se publicó, por lo que una reutilización sin cambios aparece como un ID repetido. Ese es el cambio etiquetado en [0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0); los comportamientos de Content-Digest, publicación antes de la carga y validación del editor ya se incluyeron en los tags anteriores.

## Cambios sin publicar

### Zap Cooking limita los relays del bunker y firma los endpoints de pago

Recargar una sesión de bunker en [Zap Cooking](https://github.com/zapcooking/frontend), un sitio de recetas basado en events de formato largo de Nostr, publicaba antes la conversación cifrada de [NIP-46](/es/topics/nip-46/) (firma remota mediante relays) en todos los relays que ya utilizaba la página. [Limitar el tráfico del firmante a los propios relays del bunker](https://github.com/zapcooking/frontend/pull/633) aplica ahora esa restricción al restaurar una sesión y al vincular mediante nostrconnect, el flujo de conexión iniciado por el firmante, igual que en la ruta de inicio de sesión mediante URL del bunker. Rechaza instalar un conjunto vacío de relays desde un registro almacenado con formato incorrecto, por lo que los relays que solo alojan recetas ya no averiguan que la misma pubkey mantiene activa una sesión de bunker.

[La autenticación HTTP firmada](https://github.com/zapcooking/frontend/pull/630) protege ahora el chat de pago del asistente de cocina, la introducción del recetario y las actualizaciones de recetas restringidas mediante [NIP-98](/es/topics/nip-98/) (autenticación HTTP con un event de Nostr firmado). El servidor lee el cuerpo de la solicitud una vez, verifica la firma frente a ese payload exacto y toma la identidad del event de autenticación verificado en lugar de una clave pública incluida en el cuerpo. La vista previa del chat sigue funcionando sin cabecera, mientras que una firma presente pero no válida se rechaza y la introducción del recetario siempre requiere una firma. Actualizar una receta restringida ahora también exige que la clave verificada coincida con el autor almacenado; a cualquier otra persona se le indica que la receta no existe, por lo que el endpoint no confirma qué registros de pago existen.

### nostrord repara los mensajes directos envueltos y los enlaces compartidos a events

Tras la [v2.9.0 de la semana pasada](/en/newsletters/2026-08-26-newsletter/#nostrord-v290-relay-scoped-group-state-and-media), [nostrord](https://github.com/nostrord/nostrord), un cliente multiplataforma para comunidades alojadas en relays, incorporó correcciones de entrega para que un mensaje directo privado con gift wrap de [NIP-17](/es/topics/nip-17/) enviado desde un dispositivo llegue a la misma cuenta en otros dispositivos. [Publicar de forma independiente la copia del remitente](https://github.com/nostrord/nostrord/pull/295) evita que la primera aceptación del wrap del destinatario por un relay descarte la copia que obtienen otros dispositivos. El mismo cambio vuelve a enviar un wrap tras completarse la autenticación ante relays de [NIP-42](/es/topics/nip-42/) y marca el envío como correcto con la primera aceptación de un relay para que un host que falle no pueda bloquear a los demás. [Reintentar los gift wraps aparcados](https://github.com/nostrord/nostrord/pull/297) cuyo descifrado de [NIP-59](/es/topics/nip-59/) (gift wrap) falló se hace ahora con un temporizador, por lo que un bunker que permanece conectado ya no deja esos mensajes mi... [truncated]

Una respuesta de [NIP-C7](/es/topics/nip-c7/) (mensajes de chat kind `9`) repite su elemento padre como un puntero `nevent` inicial de [NIP-19](/es/topics/nip-19/) (entidades codificadas en bech32) junto al tag `q`. [Eliminar ese puntero padre inicial](https://github.com/nostrord/nostrord/pull/292) cuando abre el cuerpo e identifica el padre de la respuesta permite que la fila se muestre como una sola cita de respuesta, mientras que un puntero situado a mitad del cuerpo o que constituye todo el cuerpo sigue mostrándose como una tarjeta de cita. [Los enlaces a events citados ahora codifican `nevent`](https://github.com/nostrord/nostrord/pull/293) con el autor, el kind y el relay del que se leyó la cita, de modo que otro cliente pueda obtener un event de [NIP-29](/es/topics/nip-29/) (grupos administrados por relays) compartido en un mensaje directo, en lugar de un identificador de nota simple sin indicaciones de consulta.

## Actualizaciones de NIPs y trabajo en especificaciones de protocolo

### Posibilidades de implementación de Nostr

Esta semana se incorporaron dos cambios de especificaciones al [repositorio principal de NIPs](https://github.com/nostr-protocol/nips).

[NIP-67](/es/topics/nip-67/) define indicaciones que un relay puede añadir a un mensaje `EOSE` (fin de events almacenados) para que un cliente sepa si debe seguir paginando. La [indicación `"auth"` incorporada](https://github.com/nostr-protocol/nips/pull/2371) añade un tercer valor junto a `finish` y `more`: un relay ahora puede indicar que podrían aparecer más events almacenados si el usuario se autentica, y debe enviar el desafío `AUTH` de [NIP-42](/es/topics/nip-42/) (autenticación ante el relay) antes del `EOSE` que contiene la indicación. La [adición correspondiente a NIP-42](https://github.com/nostr-protocol/nips/pull/2371) define el mismo flujo desde el lado del cliente, por lo que un cliente que recibe un `EOSE` con `auth` ya tiene el desafío que necesita responder.

[NIP-84](/es/topics/nip-84/) (destacados portátiles, los events kind `9802` para los que Amethyst incorporó compatibilidad más arriba) [incorporó una actualización del esquema de tags](https://github.com/nostr-protocol/nips/pull/2454): los destacados ahora pueden señalar su fuente con tags `i` estructurados según [NIP-73](/es/topics/nip-73/) (identificadores de contenido externo), además de tags `a`/`e` para events de Nostr y tags `r` para todo lo demás; y los destacados de citas pasaron de un MUST a un SHOULD al mostrarse como un repost con cita.

### Nostr Wallet Connect

Una respuesta `list_transactions` puede indicar cuántas transacciones coinciden con la solicitud, no cuántas filas devolvió la página actual. El [`total_count` opcional incorporado](https://github.com/nostr-wallet-connect/nwc/pull/4) en NWC-05 (la extensión de historial de la cartera) del [repositorio de extensiones NWC](https://github.com/nostr-wallet-connect/nwc) añade ese campo a la respuesta utilizada con [NIP-47](/es/topics/nip-47/) (control remoto cifrado de carteras mediante Nostr).

El [commit que añade `total_count`](https://github.com/nostr-wallet-connect/nwc/commit/ff3e49a47d040075edc46ee42fc0e33f10f1ef67) lo documenta como un entero opcional: el número total de transacciones que coinciden con los filtros de la solicitud.

El [commit que excluye la paginación del recuento](https://github.com/nostr-wallet-connect/nwc/commit/06315e735f744b1afd3df0b57436fdce8a7bfc2e) indica que este total excluye la paginación, por lo que cuenta todas las transacciones coincidentes de todas las páginas.

## Análisis detallado de NIPs: Reposts y reacciones

Un contacto puede volver a presentar una nota existente a sus seguidores y puede adjuntar un «me gusta», «no me gusta» o emoji compacto sin escribir una respuesta. [NIP-18](/es/topics/nip-18/) (reposts) publica esa redistribución como su propio event firmado. [NIP-25](/es/topics/nip-25/) (reacciones) publica la respuesta compacta como otro event firmado. Ambos siguen siendo archivos `draft` `optional` en la [especificación canónica de reposts](https://github.com/nostr-protocol/nips/blob/master/18.md) y la [especificación canónica de reacciones](https://github.com/nostr-protocol/nips/blob/master/25.md): están presentes en el repositorio de NIPs y los clientes los implementan, pero todavía están etiquetados como no definitivos.

### Reposts (NIP-18)

Los seguidores reciben un puntero firmado hacia una nota de texto kind 1 que alguien ya publicó cuando un cliente escribe un event kind 6. [La especificación de reposts](https://github.com/nostr-protocol/nips/blob/master/18.md) establece `kind` en 6, coloca en `content` el JSON convertido en cadena de esa nota (se permite un `content` vacío, pero no se recomienda), exige un tag `e` cuyo valor sea el `id` de la nota y cuya tercera entrada sea la URL de un relay del que se pueda obtener la nota, y dice que el event SHOULD incluir también un tag `p` con la `pubkey` del autor original. Un repost de un event de [NIP-70](/es/topics/nip-70/) (events protegidos) SHOULD mantener vacío `content` para no copiar el payload protegido al nuevo event.

Una cita es una referencia dentro de otro event, no un envoltorio kind 6. Cuando un cliente menciona un `nevent`, `note` o `naddr` de [NIP-21](/es/topics/nip-21/) (URI `nostr:`), debe convertir esa mención en un tag `q` con la forma `["q", "<event-id> or <event-address>", "<relay-url>", "<pubkey-if-a-regular-event>"]`. Los [tags de reposts con cita](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts) mantienen esas referencias fuera de los hilos de respuestas y permiten que los clientes obtengan y cuenten las citas de una publicación.

Kind 6 está reservado para notas kind 1. Un repost genérico kind 16 puede envolver cualquier kind de event excepto kind 1. SHOULD incluir un tag `k` cuyo valor sea el kind convertido en cadena del event interno. Cuando ese event interno sea reemplazable, el repost genérico SHOULD añadir un tag `a` con la coordenada `kind:pubkey:d-tag`; si falta ese tag `a`, el repost apunta a una versión específica y `content` debe contener la cadena JSON completa de esa versión. [Las reglas de reposts genéricos](https://github.com/nostr-protocol/nips/blob/master/18.md#generic-reposts) evitan que los events de formato largo, direccionables y otros que no son notas se publiquen como si fueran kind 1.

El siguiente event kind 6 es un repost real recuperado de `wss://relay.damus.io` en el momento de preparar el boletín ([abrir el event](https://njump.me/nevent1qqs88k8xgv2d3d3yymawaa24f22a0kqqvknpur0p05vq9e5r4y74xjspz3mhxue69uhhyetvv9ujuerpd46hxtnfdu7elvca)):

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

Su `kind` es 6, el tag `e` apunta a la nota que se volvió a publicar, el tag `p` identifica al autor de esa nota y `content` contiene el event kind 1 original convertido en cadena JSON. Este event recuperado de un relay omite la indicación de relay que la [especificación NIP-18](https://github.com/nostr-protocol/nips/blob/master/18.md) marca como obligatoria, lo que ilustra por qué los lectores y clientes deben validar los events reales y admitir productores que omitan campos.

### Reacciones (NIP-25)

Una publicación puede reunir «me gusta», «no me gusta» y emojis firmados sin que esas marcas entren en el hilo de respuestas. [La especificación de reacciones](https://github.com/nostr-protocol/nips/blob/master/25.md) define esa marca como un event kind 7 cuyo `content` MUST contener el valor de la reacción. `+` o una cadena vacía MUST interpretarse como un «me gusta» o voto positivo. `-` MUST interpretarse como un «no me gusta» o voto negativo. Un emoji o un shortcode de [NIP-30](/es/topics/nip-30/) (emoji personalizado) SHOULD NOT interpretarse como «me gusta» o «no me gusta», y un cliente MAY mostrar ese emoji en la publicación.

El objetivo está en los tags, no se deduce de `content`. MUST haber un tag `e` establecido en el `id` del event objetivo, y ese tag SHOULD incluir una indicación de relay; no se recomiendan tags `e` adicionales y, si aparecen, el `id` objetivo debe ser el último. SHOULD haber un tag `p` para el autor objetivo, el último si aparecen varios tags `p`. Un objetivo direccionable SHOULD recibir también un tag `a` con coordenadas `kind:pubkey:d-tag`. Los tags `e` y `a` SHOULD incluir indicaciones de relay y pubkey, los tags `p` SHOULD incluir indicaciones de relay, y un tag `k` MAY contener el kind convertido en cadena del event al que se reaccionó. [Esas reglas de tags](https://github.com/nostr-protocol/nips/blob/master/25.md#tags) permiten que un cliente obtenga el objetivo y notifique a su autor a partir únicamente del event de reacción.

Un cliente MAY colocar un único `:shortcode:` en `content` y un tag `emoji` que asocie ese shortcode a una URL de imagen, según las [reglas de reacciones con emojis personalizados](https://github.com/nostr-protocol/nips/blob/master/25.md#custom-emoji-reaction). Si el objetivo no es un event nativo de Nostr, la reacción MUST ser kind 17 y MUST llevar tags `k` e `i` de [NIP-73](/es/topics/nip-73/) (IDs de contenido externo), como en las [reglas de reacciones a contenido externo](https://github.com/nostr-protocol/nips/blob/master/25.md#external-content-reactions). Kind 17 es una reacción a un sitio web, episodio de podcast u otro objeto externo. No es una reacción entre events kind 7 ni es un repost.

El siguiente event kind 7 es una reacción real recuperada de `wss://relay.damus.io` en el momento de preparar el boletín ([abrir el event](https://njump.me/nevent1qqsytac63l00k7kyaphkfwqqn94wglmx78v6zhqtytg65w5k957luccpz3mhxue69uhhyetvv9ujuerpd46hxtnfdus63jym)):

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

Su `content` es `+`, el «me gusta» convencional de [NIP-25](https://github.com/nostr-protocol/nips/blob/master/25.md). El tag `e` identifica el event al que se reaccionó; el tag `a` añade su coordenada direccionable; el tag `p` identifica a su autor; y el tag opcional `k` registra como cadena el kind del objetivo.

### Implementaciones actuales en clientes

[Amethyst](https://github.com/vitorpamplona/amethyst), un cliente Android de Nostr, define el [tipo de event de repost](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip18Reposts/RepostEvent.kt) y el [tipo de event de reacción](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip25Reactions/ReactionEvent.kt) en su capa de protocolo actual.

[Snort](https://github.com/v0l/snort), un cliente web de Nostr, implementa [funciones auxiliares de NIP-18 que incluyen el manejo de tags de enlaces de citas](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip18.ts) y [crea tags de reacción a events de NIP-25](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip25.ts).

[Ditto](https://github.com/soapbox-pub/ditto), un servidor Mastodon y relay de Nostr combinados, [publica reposts genéricos kind 16 con un tag `k` y una coordenada `a` en objetivos direccionables](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/components/RepostMenu.tsx) y [aplica la semántica de reacciones kind 7 tratando el último tag `e` como el event objetivo](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/lib/nostrEvents.ts).

### Cómo funcionan juntos

Un event kind 6 o kind 16 redistribuye un event existente a los feeds de los seguidores de quien hace el repost, ya sea insertando el JSON de ese event o apuntando a una coordenada reemplazable. Un tag `q` marca una cita dentro de otro event para que la reconstrucción del hilo pueda contar las referencias sin tratar el event que cita como una respuesta, que es la distinción trazada en la [sección de reposts con cita](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts). Un event kind 7 deja el event original en su lugar y adjunta únicamente el valor de la reacción junto con los tags del objetivo, según el contrato de la [especificación de reacciones](https://github.com/nostr-protocol/nips/blob/master/25.md). Por tanto, los clientes que obtienen una pubkey ven los reposts de esa pubkey como nuevos events kind 6 o 16 y las opiniones de esa pubkey como events kind 7 en las publicaciones de otras personas.

---

Envíe un mensaje directo NIP-17 para compartir un proyecto o una noticia mediante el [proyecto Nostr Compass](https://github.com/andotherstuff/nostr-compass).
