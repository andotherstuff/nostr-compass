---
title: 'Nostr Compass #47'
date: 2026-11-04
publishDate: 2026-11-04
draft: false
type: newsletters
translationOf: /en/newsletters/2026-11-04-newsletter.md
translationDate: 2026-11-05
---

Esta semana [Amethyst](/es/newsletters/2026-11-04-newsletter/#amethyst) lanzó napplets integrados en las notas con correcciones derivadas de una [revisión de seguridad de los embebidos](https://github.com/vitorpamplona/amethyst/pull/4710), [Napplets](/es/newsletters/2026-11-04-newsletter/#napplets---web-packages) vinculó la identidad de los applets a puertos por documento y las versiones nightly de [mdk de Marmot](/es/newsletters/2026-11-04-newsletter/#marmot-protocol-mdk) reforzaron la mensajería grupal. Además, hubo cambios en relays, monederos, bibliotecas de firma y apps nuevas, en gran parte en código fusionado que todavía no se ha publicado en ninguna versión.

## Noticias destacadas {#top-stories}

### Amethyst {#amethyst}

Amethyst, el cliente para Android, publicó la [v1.21.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.21.0), que ejecuta napplets integrados en las notas en Android 11+ y en escritorio. Las correcciones de una [revisión de seguridad de los embebidos](https://github.com/vitorpamplona/amethyst/pull/4710) cierran una vía por la que cualquier napplet con acceso a relays podía leer DMs descifrados. Ahora el descifrado requiere un permiso aparte concedido por el usuario y `nostr.signEvent` requiere permiso del firmante, aunque el renderizador Chromium de escritorio sigue sin sandbox. Un [cambio en el cifrado de adjuntos por archivo](https://github.com/vitorpamplona/amethyst/pull/4701) asigna a cada adjunto de mensaje directo privado [NIP-17](/es/topics/nip-17/) una clave y un nonce AES-GCM nuevos, cuando antes los lotes de varios archivos reutilizaban ambos. La descripción del riesgo que da el proyecto procede de un análisis del código sin un exploit reproducido, y los archivos ya enviados no se reparan.

### Marmot Protocol (mdk) {#marmot-protocol-mdk}

mdk, el kit de mensajería cifrada basado en MLS de Marmot para Nostr, publicó prerreleases nightly destinadas solo a pruebas, sin ninguna versión estable en esa línea. En la nightly del 2 de noviembre, [los envíos nuevos esperan detrás de los más antiguos en cola](https://github.com/marmot-protocol/mdk/pull/2849) dentro de un grupo, lo que mantiene en orden las generaciones de cifrado para los miembros que se ponen al día con el historial, aunque esto no garantiza que no se pierdan mensajes. Una [reparación de Welcome perdidos](https://github.com/marmot-protocol/mdk/pull/2936), fusionada y desactivada por defecto, sigue la [regla de heartbeat de Marmot](https://github.com/marmot-protocol/marmot/pull/497) y reenvía exactamente el Welcome conservado una vez que el heartbeat del destinatario muestra actividad al menos diez minutos después de la última publicación del portador. La cadencia del heartbeat o el desfase de reloj pueden retrasar la reparación una hora o más, y su finalización no tiene límite superior. Los [comandos de vinculación de dispositivos](https://github.com/marmot-protocol/mdk/pull/2922) siguen detrás de la función dev-device-groups, desactivada por defecto, y están deshabilitados en producción.

### Napplets - Web Packages {#napplets---web-packages}

Napplets, los paquetes web para applets de Nostr en sandbox, publicó [core 0.37.0](https://github.com/napplet/web/releases/tag/%40napplet/core%400.37.0), [nap 0.36.0](https://github.com/napplet/web/releases/tag/%40napplet/nap%400.36.0) y [shim 0.35.0](https://github.com/napplet/web/releases/tag/%40napplet/shim%400.35.0), que [vinculan la identidad del applet a un MessagePort por documento](https://github.com/napplet/web/pull/302). La identidad verificada (dTag, artifactHash) queda ligada al puerto que se pasa en el hello desde el iframe creado, y todo el tráfico NAP usa ese puerto. Un documento cargado mediante navegación no recibe permisos. Los shells que todavía usan mensajería de Window deben actualizarse, porque no hay ruta de compatibilidad. Código posterior [fija el marco de vista previa a su documento verificado](https://github.com/napplet/web/pull/305) con frame-src 'none'.

## Versiones etiquetadas {#tagged-releases}

### Marble {#marble}

Marble, un cliente beta construido sobre la firma por umbral de Cosign, puede leer relays como feeds en la [0.12.23](https://github.com/sybenx/marble/releases/tag/v0.12.23). Un relay abierto por su dirección muestra su propia descripción y después sus publicaciones, de la más reciente a la más antigua. Los relays favoritos se guardan en una lista kind 10012 y los grupos de relays en conjuntos kind 30002, las mismas listas que usa Jumble. La versión también rediseña las reacciones, con una bandeja de reacciones recientes y los emojis personalizados del propio usuario.

### Sidecar {#sidecar}

Sidecar, una extensión de navegador para publicar notas y destacados de la web, puede borrar de los relays su copia de seguridad del monedero en la [1.16.6](https://github.com/dmnyc/sidecar/releases/tag/v1.16.6). Tras una confirmación, sustituye la copia cifrada por una vacía y pide a los relays que la olviden, sin tocar el monedero conectado. No está garantizado que los relays borren la copia. Desde la [v1.16.5](https://github.com/dmnyc/sidecar/releases/tag/v1.16.5), Sidecar elimina los metadatos EXIF, XMP e IPTC de los JPEG antes de subirlos, y su [cambio en la preparación de subidas](https://github.com/dmnyc/sidecar/pull/572) bloquea cualquier JPEG que no se pueda limpiar.

### Haps {#haps}

Haps publica e instala paquetes nativos bajo claves de Nostr. [Haps 0.1.25](https://github.com/mmalmi/haps/releases/tag/v0.1.25) incluye paquetes para macOS, Linux y Windows con asistentes htree fijados por checksum y un archivo SHA256SUMS que cubre todos los archivos comprimidos. El código de la 0.1.24 [escribe referencias Hashtree versionadas](https://github.com/mmalmi/haps/commit/3dd051cefe9e506886a7f036267950282a179ee8) según el borrador de la especificación Hashtree. Haps 0.1.23 y anteriores no pueden leer los nuevos catálogos sin un catálogo de transición heredado o un instalador o compilación de Cargo actualizados.

### Cosign {#cosign}

Cosign, la biblioteca de firma por umbral detrás de la beta de Marble, incluye una corrección parcial de la unión en la [0.12.9](https://github.com/sybenx/cosign/releases/tag/v0.12.9): unirse a través de un invitador escaneado ahora requiere la contribución de ese invitador y fragmentos de al menos dos remitentes distintos. Las uniones de teléfono a teléfono siguen sin vincular, de modo que a un atacante le siguen bastando dos claves, y las partes de descifrado vacías siguen omitiendo la verificación de pruebas. En la [0.12.8](https://github.com/sybenx/cosign/releases/tag/v0.12.8), un servidor que escribe la lista de miembros todavía puede elegir puntos de participación con secretos conocidos. Los teléfonos solo reciben correcciones a través de una versión de Marble.

### nostream {#nostream}

nostream, un relay en TypeScript respaldado por PostgreSQL, añade [sincronización saliente con pares](https://github.com/cameri/nostream/pull/1043) en la [3.12.0](https://github.com/cameri/nostream/releases/tag/nostream%403.12.0). El worker lee los ámbitos de la información de relay [NIP-11](/es/topics/nip-11/) de cada par, se autentica con la autenticación de cliente [NIP-42](/es/topics/nip-42/) y concilia mediante la sincronización negentropy de [NIP-77](/es/topics/nip-77/), comprobando los eventos obtenidos según ID, firma y ámbito. Los [límites específicos por par](https://github.com/cameri/nostream/pull/1034) solo se aplican después de que un par configurado completa AUTH. Una versión del código fuente no demuestra que ningún relay la haya desplegado.

### diVine {#divine}

diVine, un cliente de vídeos cortos en bucle, publicó la [versión estable 1.0.27 para Android](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.27) con stickers interactivos en vídeos públicos; la disponibilidad en iOS y macOS no está confirmada. Una [reconsulta por debajo de la ventana](https://github.com/divinevideo/divine-mobile/pull/10711), ya fusionada, se ejecuta solo después de que haya terminado la restauración inicial del historial, y lee gift wraps, DMs cifrados [NIP-04](/es/topics/nip-04/) obsoletos y borrados en páginas de 100 mensajes por relay. Recorre cada relay de forma independiente, mientras que el drenado de historial existente comparte un único cursor y puede saltarse el historial más antiguo de un relay con límite. La cobertura es limitada y no recupera el historial completo.

### Whistle {#whistle}

Whistle, una app móvil para compartir ubicación y chatear en grupo, publicó la [2.0.1](https://github.com/sjmcnamara/whistle/releases/tag/v2.0.1), su primera versión pública sobre el protocolo Marmot v2. Los grupos existentes no se pueden trasladar, así que hay que recrearlos y todos los miembros deben actualizar, aunque se conservan las identidades npub. Escanear para unirse sustituye a los códigos y enlaces de invitación. Como problema conocido, los mensajes de chat enviados sin conexión pueden llegar tarde o no llegar, algo que la versión atribuye a MarmotKit; la ubicación compartida no se ve afectada.

## En desarrollo {#in-development}

### Quartz {#quartz}

Quartz, una biblioteca de Nostr en Kotlin Multiplatform, incluyó la [reanudación de suscripciones en vivo tras reconectar](https://github.com/vitorpamplona/quartz/pull/82) en la versión 2.14.0. Cada relay se reanuda desde el created_at entregado más reciente, limitado al reloj del dispositivo, y los filtros de gift wrap retroceden dos días adicionales para cubrir fechas antedatadas. Todavía pueden perderse eventos con marcas de tiempo anteriores que un relay almacenó durante una caída. Las [ventanas negentropy con conteo](https://github.com/vitorpamplona/quartz/pull/85), fusionadas pero sin publicar, comparan un conteo de eventos opcional de [NIP-45](/es/topics/nip-45/) con el conteo local y tratan los conteos de los relays como no fiables.

### Buzz {#buzz}

Buzz fusionó un cambio que [confirma los borrados kind 5 y 9005 en una sola transacción junto con el borrado lógico del objetivo](https://github.com/block/buzz/pull/8944), de modo que un fallo ya no puede aceptar un borrado mientras el objetivo sigue activo. Las filas inconsistentes históricas no se reparan. El perfil móvil de [NIP-RS](/es/topics/nip-rs/), un borrador de Buzz para el estado de lectura entre dispositivos, se ha fusionado y [sincroniza las fronteras de lectura entre dispositivos](https://github.com/block/buzz/pull/8998). En relays más antiguos sin read_state_snapshot, las lecturas locales siguen funcionando y la sincronización entre dispositivos se detiene sin alternativa.

### Alby Hub {#alby-hub}

Alby Hub, un nodo Lightning autocustodiado que da servicio a apps Nostr Wallet Connect [NIP-47](/es/topics/nip-47/), fusionó una [corrección de migración de base de datos](https://github.com/getAlby/hub/pull/2657) que conserva el contador de IDs de cada tabla durante db_migrate o una migración a Postgres. Antes, una app nueva podía reutilizar el ID de una app borrada y heredar sus transacciones y su saldo aislado. No se ha identificado ninguna versión etiquetada ni despliegue que contenga la corrección. Un [cambio de notificaciones](https://github.com/getAlby/hub/pull/2677) aparte aísla los fallos por app, aunque las notificaciones fallidas se siguen descartando sin reintento.

### swift-nostr-client {#swift-nostr-client}

swift-nostr-client, una biblioteca de Nostr en Swift 6, fusionó un cambio incompatible que hace que [RemoteSigner ejecute el handshake de conexión antes de su primer comando](https://github.com/yysskk/swift-nostr/pull/287). El nuevo ajuste connectsAutomatically vale true por defecto, y si el handshake falla el comando no se envía. Como los secretos de firma remota [NIP-46](/es/topics/nip-46/) son de un solo uso, las apps que reanudan una sesión de bunker con un par de claves de cliente guardado deben ponerlo en false, o el primer comando presentará el secreto ya gastado. No se ha etiquetado ninguna versión.

## Proyectos nuevos {#new-projects}

### Trikey {#trikey}

Trikey, un monedero pre-alfa y sin auditar cuya app móvil y cuyo guardián se comunican mediante mensajes cifrados a través de relays de Nostr, resuelve el bloqueo de la app al abrirse en la [versión 0.1.10-alpha](https://njump.me/nevent1qvzqqqr4dupzqpepqn8d9d5jc8r4qf6h7kd7ldpgrpqgdaw8wjwyrxztkjltnfy4qyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpk2jxzja4q4z8avcsc7jqenpuykke49p3z3halm0xtgmn3h6r6judumrxf). Ambas partes guardan ahora un registro, que sobrevive a los reinicios, de los IDs de wrap ya leídos y los omiten antes de cualquier comprobación de firma o descifrado. Las indicaciones de expiración en solicitudes y alertas no garantizan que los relays las borren, y las mediciones de rendimiento del autor se tomaron en un portátil.

### Pacto {#pacto}

Pacto, una app de escritorio para organización comunitaria que ejecuta grupos Marmot heredados junto a DMs NIP-17, publicó la [v0.7.5](https://github.com/covenant-gov/pacto-app/releases/tag/v0.7.5), sin firmar, con edición de mensajes enviados durante un minuto. Sus [correcciones de entrega de DMs](https://github.com/covenant-gov/pacto-app/pull/425) hacen fallar los envíos de inmediato cuando el pool no tiene ningún relay de confianza y enrutan los indicadores de escritura a través de relays de confianza. Pull requests abiertas y sin fusionar añadirían [eventos de escuadra](https://github.com/covenant-gov/pacto-app/pull/488) y [documentos cifrados de escuadra](https://github.com/covenant-gov/pacto-app/pull/490).

### Mialuna {#mialuna}

Mialuna, un cliente de Nostr en Flutter centrado en contenido multimedia, publicó un [anuncio de la versión 0.19.0](https://njump.me/nevent1qvzqqqr4dupzqeyvpafs936l8quz5nfvskjg9wf8e3sm9q52q72wxmrvc7tdap4xqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqk6ltj5kr6mtq8mkyz9rzqxkkrhq9hsjz675e05rwgltwgreddw3npkkez) que añade solicitudes de borrado para las historias propias del usuario cuando caducan. El [commit del registro de cambios](https://github.com/Lwb89dev/mialuna/commit/d0a38cb92dac724e6e7bac6ec8f94a31a378e886) recoge solicitudes de borrado a relays y borrado de medios en Blossom: las cuentas con clave local lo hacen automáticamente y las cuentas de Amber o bunker esperan a que el usuario elija Delete now. El APK y su comportamiento en dispositivos no se han verificado de forma independiente. Las solicitudes de borrado no pueden garantizar que los relays o servidores eliminen los datos.

### whereAreYou {#whereareyou}

whereAreYou, una app de Android que comparte la ubicación dentro de círculos a los que se entra con código QR o enlace de invitación, cifra las coordenadas con AES-256-GCM y las envía a través de relays públicos. Un [commit de firma por miembro](https://github.com/Dzekdrix/whereAreYou/commit/82121d0f13b4d5256b2392383e74640afde3019e) impide que quienes tienen la clave del círculo publiquen haciéndose pasar por otro miembro, y todos los dispositivos deben actualizar. Sobre la [copia de seguridad de identidad en Base45](https://github.com/Dzekdrix/whereAreYou/commit/82e185967dd0115b93472b3d92a4d0393c8751bc), el autor advierte que cualquiera que fotografíe el código QR podría adivinar su código de ocho dígitos sin conexión, según su estimación en decenas de minutos de tiempo de GPU; no se ha publicado ningún benchmark. El código no cuenta con ningún aval de seguridad.

## Trabajo en protocolo y especificaciones {#protocol-and-spec-work}

### Buzz define rutas de credenciales para agentes autorizados por su propietario {#buzz-defines-owner-authorized-agent-credential-routes}

Buzz fusionó un [borrador de NIP-FA](/es/topics/nip-fa/) [para credenciales de agentes autorizados por su propietario](https://github.com/block/buzz/pull/9015), que define rutas de concesión, aserción y revocación para agentes autorizados mediante la atestación de propietario [NIP-OA](/es/topics/nip-oa/). Una concesión surge de un intercambio de tokens RFC 8693 que empareja la sesión del propietario con una prueba de autenticación HTTP [NIP-98](/es/topics/nip-98/) del agente, y la revocación desconecta al agente e impide que su clave vuelva a inscribirse. NIP-FA es una especificación de Buzz fusionada solo en el código fuente, sin ninguna afirmación de activación en producción ni de interoperabilidad.

### Las firmas de eventos poscuánticas obtienen reglas de validación exactas {#post-quantum-event-signatures-gain-exact-validation-rules}

La propuesta abierta de firmas poscuánticas, en discusión desde hace tiempo, incorporó [reglas exactas de validación ML-DSA-44 para eventos de Nostr](https://github.com/nostr-protocol/nips/commit/43104cbff30ae006e907d8ee0ec15c4949d0eef6). Las claves y las firmas tienen longitudes fijas, los verificadores comprueban la firma sobre los 32 bytes en bruto del digest del ID del evento con un contexto vacío, y no se permite ningún algoritmo alternativo. La identidad propuesta no tiene codificación bech32 [NIP-19](/es/topics/nip-19/), y las nuevas firmas no hacen que los payloads cifrados [NIP-44](/es/topics/nip-44/) ni los gift wraps [NIP-59](/es/topics/nip-59/) sean seguros frente a la computación cuántica.

### Una precondición firmada propuesta evita reemplazos de eventos perdidos {#a-proposed-signed-precondition-prevents-lost-event-replacements}

Una pull request abierta de Buzz [propone una precondición firmada NIP-CS local al proyecto](https://github.com/block/buzz/pull/8835) para eventos reemplazables y direccionables, y no es un NIP oficial. La etiqueta firmada indica el ID de la cabeza actual o `none`, y el relay la comprueba de forma atómica bajo un bloqueo de coordenada, rechazando una escritura obsoleta con un OK false o un HTTP 409 sin almacenar nada. Las escrituras sin la etiqueta funcionan como antes, y la etiqueta no ofrece ninguna garantía de compare-and-swap entre relays.

## NIP en profundidad: NIP-31 y NIP-73 {#nip-deep-dive-nip-31-and-nip-73}

Los clientes se encuentran a menudo con contenido que no entienden de forma nativa. [NIP-31: Dealing with Unknown Event Kinds](/es/topics/nip-31/) da una etiqueta legible a un kind de evento desconocido, y [NIP-73: External Content IDs](/es/topics/nip-73/) nombra temas externos a Nostr, como libros o páginas web. Las dos convenciones son especificaciones existentes e independientes ([texto de NIP-31](https://github.com/nostr-protocol/nips/blob/master/31.md), [texto de NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md)).

### NIP-31 está marcado como no recomendado {#nip-31-is-marked-unrecommended}

El [texto actual de NIP-31](https://github.com/nostr-protocol/nips/blob/master/31.md) empieza con una advertencia que lo marca como `unrecommended` por ser "unnecessarily bloated" (innecesariamente sobrecargado), y su línea de estado dice draft, unrecommended y optional. Ya existen en los relays eventos que usan la convención, así que la mecánica que se describe a continuación explica cómo los leen los clientes, sin recomendarla para protocolos nuevos.

### Qué contiene una etiqueta alt {#what-an-alt-tag-carries}

Según la [especificación](https://github.com/nostr-protocol/nips/blob/master/31.md), el autor de un kind personalizado que no está pensado para leerse como texto añade una etiqueta `alt` con un breve resumen en texto plano. No se espera que los clientes centrados en kind 1 soliciten otros kinds, pero los usuarios pueden igualmente referenciar esos eventos desde notas, donde un resumen aporta contexto. Una etiqueta no puede emitir un voto ni ejecutar una solicitud de monedero. Para una interacción más rica, la especificación remite a [NIP-89: Recommended Application Handlers](/es/topics/nip-89/).

Como `alt` es una etiqueta, el ID y la firma del evento de [NIP-01](/es/topics/nip-01/): [Basic protocol flow description](https://github.com/nostr-protocol/nips/blob/master/01.md) la cubren. Una firma válida autentica un resumen controlado por el autor: muestra que el autor publicó la etiqueta, no que sea exacta, así que puede haber resúmenes engañosos. Las etiquetas son públicas, de modo que un `alt` en un evento con contenido cifrado expone su resumen y puede revelar lo que el contenido oculta. Estas propiedades provienen del envoltorio de [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md), fuera del texto normativo de NIP-31. Una etiqueta `alt` de nivel superior también es distinta del campo `alt` de descripción de imagen dentro de `imeta`, y los renderizadores los analizan por separado.

### Cómo leen alt dos clientes {#how-two-clients-read-alt}

En la [tarjeta de evento desconocido de noStrudel en el commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx), la primera etiqueta `alt` se recorta y se convierte en la etiqueta principal, con una línea opcional `Using <client>`. Un valor ausente o en blanco produce `Unknown event (kind ...)`, y hasta tres líneas de contenido se muestran de forma independiente. El mismo componente resuelve la etiqueta `client` mediante plantillas de handlers NIP-89, y muestra Open cuando existe una dirección compartible y `Open in <client>` cuando se resuelve un enlace de handler válido. La explicación y el envío a una app son controles separados.

[UnknownEventDigest.kt de Amethyst en el commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170) prefiere el contenido que clasifica como prosa y recurre a `alt` en su defecto. Su parser recorta los valores y toma el primer `alt` no vacío, así que un evento cuyo primer `alt` está en blanco puede recibir aquí una etiqueta distinta que en noStrudel. Ambas descripciones reflejan el código en esos commits, no un comportamiento confirmado en versiones publicadas.

### Ejemplo: una encuesta con etiqueta alt {#example-a-poll-with-an-alt-label}

La encuesta kind 1068 siguiente se obtuvo de wss://relay.damus.io, y su ID y su firma BIP340 se verifican correctamente según las reglas de [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md). Un renderizador genérico puede mostrar el texto bilingüe de `alt`, mientras que un cliente que entiende encuestas lee las etiquetas `option` y `polltype`.

```json
{
  "kind": 1068,
  "id": "7d1df3922833b47645922de43c2edd83e928a0ad083cee592beeee2b262bb743",
  "pubkey": "5f6dc275f3f9f8752d010a110c226148a9ba3399c5b63a0f469ee93b1394a53e",
  "created_at": 1793626294,
  "tags": [
    [
      "option",
      "z25mgp",
      "Windows"
    ],
    [
      "option",
      "ncddq0",
      "macOS"
    ],
    [
      "option",
      "4wta6q",
      "Linux"
    ],
    [
      "option",
      "p9ykti",
      "UNIX or FreeBSD/NetBSD/OpenBSD"
    ],
    [
      "polltype",
      "singlechoice"
    ],
    [
      "alt",
      "Poll: Which one do you usually use?\n普段どれを使っていますか？"
    ],
    [
      "client",
      "Ditto",
      "31990:781a1527055f74c1f70230f10384609b34548f8ab6a0a6caa74025827f9fdae5:ditto"
    ]
  ],
  "content": "Which one do you usually use?\n普段どれを使っていますか？",
  "sig": "f1378a723c65e83bd3105b593f10767903bde993788cfaf625583466fca21f1ef2be945bb2ca526aa9e898c93d5f1677a2f5ceaf70cb3a59c99f97eb179658fa"
}
```

### Temas y familias de NIP-73 {#nip-73-subjects-and-families}

La [especificación NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md) (draft, optional, sin la marca unrecommended) coloca un tema externo en una etiqueta `i` y su familia de identificadores en una etiqueta `k`, de modo que los clientes pueden consultar un tema exacto o una familia entera. Un libro usa `["i", "isbn:9780765382030"]` con `["k", "isbn"]`, y una página web usa su URL con `k` igual a `web`. NIP-73 no define ningún kind de evento; son otros eventos los que llevan las etiquetas.

### Normalización y pistas de URL {#normalization-and-url-hints}

La coincidencia depende de cadenas idénticas, así que la [especificación](https://github.com/nostr-protocol/nips/blob/master/73.md) fija una forma por familia: URLs normalizadas sin fragmento, ISBN sin guiones, geohashes en minúsculas y códigos ISO 3166 en mayúsculas. Un tercer elemento opcional del array lleva una pista de URL para clientes que no tienen criterio propio sobre el identificador. El autor elige esa pista, y no forma parte de la identidad. Tampoco demuestra propiedad ni designa un sitio canónico.

### Lo que no demuestra un identificador compartido {#what-a-shared-identifier-does-not-prove}

Según [NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md), los identificadores iguales unen conversaciones y no establecen nada más. Un comentario firmado identifica a quien comenta, pero no autentica al editor del libro, del sitio o del podcast ni muestra quién los controla. Los alias, los ISBN específicos de cada edición y las URLs que se normalizan de forma distinta pueden dividir un mismo tema en varios hilos. El contexto importa: [NIP-22](/es/topics/nip-22/): [Comment](https://github.com/nostr-protocol/nips/blob/master/22.md) usa `I`/`K` en mayúsculas para el ámbito raíz y `i`/`k` en minúsculas para el padre, y [NIP-39: External Identities in Profiles](/es/topics/nip-39/) usa `i` para identidades de perfil, así que no toda etiqueta `i` es un tema NIP-73.

### NIP-73 en el código de parsers y renderizadores {#nip-73-in-parser-and-renderer-code}

[nip73.rs de rust-nostr en el commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs) analiza los prefijos conocidos en un `ExternalContentId` tipado y convierte una pista opcional en una URL tipada, emitiendo el tercer elemento de la etiqueta solo cuando hay pista. Sus tests conservan ISBN con guiones: el parser quita el prefijo y almacena el resto sin aplicar la normalización de la especificación, así que el análisis tipado no garantiza cadenas canónicas. Separa los IDs de cadena de la familia, de modo que `ethereum:100:tx:<hash>` se asigna a `ethereum:tx`. Esa revisión no tiene una variante de país `iso3166`.

[DisplayExternalId.kt de Amethyst en el commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt) envía los identificadores de geohash y hashtag a vistas dedicadas. Los identificadores de URL también tienen una vista dedicada, mientras que los demás tipos compatibles van a un chip de ámbito genérico. Una URL abre la ruta de hilo propia de la app para esa página. Con las vistas previas desactivadas, el renderizado normal muestra un chip de enlace simple y no solicita vista previa. Con las vistas previas activadas, obtener una vista previa que falta puede contactar con el sitio de destino. Desactivar las vistas previas evita esa solicitud en el renderizado normal. Ninguno de los dos archivos establece el comportamiento de las versiones publicadas.

### Ejemplo: un comentario sobre una página web {#example-a-comment-on-a-webpage}

Este comentario kind 1111, obtenido de wss://nos.lol, coloca la misma URL de un hilo público de Reddit en sus dos pares `I`/`K` e `i`/`k`, con `web` como familia según [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md) y NIP-73. Su ID y su firma se verifican, lo que identifica a quien escribió el comentario y no dice nada sobre la página enlazada.

```json
{
  "kind": 1111,
  "id": "e4229e38d93fad5d612ae21c401573bf8e87f0462dc2bd653804a252f98a238a",
  "pubkey": "ce5b8496c144a9dcd4990df6e265d9b60a21cde2515f3b206dc67b1c343790a9",
  "created_at": 1793590574,
  "tags": [
    [
      "I",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "K",
      "web"
    ],
    [
      "i",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "k",
      "web"
    ],
    [
      "client",
      "LayerTake"
    ],
    [
      "L",
      "layertake"
    ],
    [
      "l",
      "pin",
      "layertake"
    ],
    [
      "anchor",
      "{\"type\":\"text\",\"exact\":\"tools and systems\",\"prefix\":\"help • 6mo ago u/TheFarSea What \",\"suffix\":\" do you use for tracking and org\"}"
    ]
  ],
  "content": "Like this. I'm making this Public but could be just for me or friends/groups.",
  "sig": "a979389480d6ca919e4ab7b1ba92e532bf281be45c5df222e17d7d4ca62ef07d52c1004c0ce88620663dfac012b306154cfd73b858225764c701c40e3d9b7dfe"
}
```
