---
title: "Nostr Compass #34"
date: 2026-08-05
publishDate: 2026-08-05
translationOf: /en/newsletters/2026-08-05-newsletter.md
translationDate: 2026-08-06
draft: false
type: newsletters
description: "Sandstr ofrece recorridos con datos simulados por clientes de Nostr, nostr-mill añade consentimiento de firma por evento, y nostrord amplía los grupos alojados en relays. Los análisis en profundidad cubren la búsqueda en relays y los destacados portátiles."
---

Bienvenidos de nuevo a [Nostr Compass](https://github.com/andotherstuff/nostr-compass), tu guía semanal de Nostr.

**Esta semana:** [Sandstr](https://sandstr.app/) permite a los recién llegados explorar clientes de Nostr simulados sin crear claves ni instalar una aplicación. [nostr-mill](https://github.com/0ceanSlim/nostr-mill) añade consentimiento del firmante por evento y recuperación de claves entre clientes, mientras que [nostrord](https://github.com/nostrord/nostrord) amplía los grupos alojados en relays, los firmantes, la moderación, las subidas y los destacados. El trabajo de protocolo abarca los formatos de eventos de Nostr, las conexiones de monedero, el descubrimiento de relays, los napplets, Marmot y Concord; los análisis en profundidad explican la búsqueda asistida por relays y los destacados portátiles.

## Historias Principales

### nostr-mill 1.6.0 lleva el consentimiento de firma y la recuperación de cuentas al navegador

[nostr-mill 1.6.0](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0) es un selector de cuentas y firmante integrable en el navegador. Ahora solicita consentimiento por kind de evento y muestra el contenido y las etiquetas decodificados antes de firmar, con permisos de duración limitada y un gestor de permisos. La versión también corrige un error de primera sesión que permitía firmar sin preguntar en las categorías configuradas para solicitar confirmación cada vez. Su incorporación opcional mediante Google puede importar un `nsec` existente, almacena la clave cifrada en la carpeta de datos de aplicación de Drive del usuario, admite múltiples identidades y puede exportar un `ncryptsec` en formato [NIP-49](/es/topics/nip-49/) (formato de clave privada cifrada).

La [copia de seguridad experimental en relays](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0) deriva una frase de recuperación robusta con scrypt y HKDF, envuelve la clave como `ncryptsec`, verifica los eventos recuperados y exige un quórum de relays antes de la recuperación. El inicio de sesión mediante [NIP-55](/es/topics/nip-55/) (intents de firmante en Android) ahora usa la ruta de retorno por portapapeles de Amber, y las conexiones [NIP-46](/es/topics/nip-46/) (firma remota mediada por relays) son silenciosas por defecto. Los controles de marca y las pantallas de permisos adaptables completan la versión sin cambiar las integraciones existentes salvo que el operador lo active.

### nostrord 2.5.0 da a los grupos de relays identidades estables y específicas del relay

[nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) es un cliente multiplataforma para comunidades alojadas en relays. Ahora deriva una identidad [NIP-29](/es/topics/nip-29/) (grupos gestionados por relays) a partir del ID de grupo y del relay anfitrión, delimita la membresía y las insignias de administrador del mismo modo, acepta enlaces profundos `naddr` de grupo y sincroniza los hilos de grupos privados entre dispositivos.

La [versión](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) también añade una bandeja de moderación con [NIP-56](/es/topics/nip-56/) (eventos de denuncia), inicio de sesión con Amber a través de NIP-55, retroceso ante límites de velocidad para el tráfico del firmante NIP-46, renderizado de [NIP-84](/es/topics/nip-84/) (destacados portátiles) con reintentos para referencias no resueltas, y subidas de medios a través de Blossom o [NIP-96](/es/topics/nip-96/) (almacenamiento HTTP de archivos). El inicio de sesión con Google ahora respalda la clave antes de crear la cuenta y confirma las desconexiones. Las respuestas en hilos ganan contenido más rico y borrado por administradores, mientras que las correcciones del llavero de escritorio y del teclado móvil mantienen utilizables esas funciones de protocolo.

### Primal Android 3.5.25 actualiza la firma remota y el filtrado de listas de seguimiento

[Primal Android 3.5.25](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.25) es un cliente móvil de Nostr con feeds, búsqueda y firma remota. Actualiza su firmante remoto para el comportamiento actual del protocolo, añade una lista de silenciados de seguidos, abre la búsqueda desde Explorar, repara automáticamente las conexiones de relay estancadas, expone los tiempos de espera de las peticiones en la interfaz, rechaza entradas no válidas en la lista de seguidos y actualiza las URL de relay de reserva. La precarga de feeds, el menor uso de memoria y un límite de caché de 100 MB reducen el coste de mantener esos feeds al día. Las notas con una sola imagen ahora usan todo el ancho del contenido, y los controles de perfil y la precarga de medios reciben correcciones menores de interacción y ordenación.

### Nostur 1.30.2 amplía las respuestas privadas y los medios en mensajes directos

[Nostur 1.30.2](https://github.com/nostur-com/nostur-ios-public/releases/tag/527) es un cliente de Nostr para plataformas Apple. Siempre expone la acción de respuesta privada, añade cachés de medios por conversación con límites y controles de borrado, mejora el autocompletado de nombres y etiquetas en publicaciones y chats, muestra los mensajes referenciados en el chat en vivo e incluye el título de la sala en las notificaciones del chat. Las correcciones de paginación del feed y de respuestas anidadas abordan regresiones de recuperación y renderizado de conversaciones.

### Chama 5.7.0 añade registros de árbitros y recuperación de intercambios en caché

[Chama 5.7.0](https://github.com/jesuspirate/chama/releases/tag/v5.7.0) coordina intercambios entre pares y arbitraje mediante cadenas de eventos de Nostr firmados. Muestra el importe bloqueado de un árbitro, la antigüedad de su fianza y su outpoint de financiación; registra cuándo un suplente reemplazó a un árbitro ausente; y define los eventos dormidos de kind `38136` de atestación de fallos que requieren las firmas de ambos principales. Una reparación explícita reintenta los historiales de relay incompletos contra la caché duradera del dispositivo y republica los eventos recuperados, mientras que las publicaciones fallidas se encolan para la próxima conexión. La versión también evita pagos duplicados entre dispositivos de la prima de árbitro tratando el evento de kind `38113` del autor como el registro de pago.

### Auditable Voting 0.1.165 restablece la entrega de papeletas delegadas

[Auditable Voting 0.1.165](https://github.com/tidley/auditable-voting/releases/tag/v0.1.165) realiza votaciones verificables separando las credenciales del votante del contenido de la papeleta. Restablece la emisión delegada de papeletas ciegas mediante entrega autenticada de delegaciones y reposición de DMs de control, mantiene los mensajes directos de credenciales ciegas en los relays privados configurados y actualiza el proxy de auditoría a 0.1.52.

### Sandstr permite a los recién llegados probar clientes de Nostr con datos simulados

[Sandstr](https://sandstr.app/) ofrece simulaciones interactivas en el navegador de clientes de Nostr para que un recién llegado pueda comparar sus interfaces antes de instalar uno o crear un par de claves. Su lanzamiento del 3 de agosto incluye reproducciones verificadas contra la referencia de Damus, Amethyst, Primal, Snort, YakiHonne, Coracle y Wisp, además de vistas previas tempranas claramente etiquetadas de Gossip, Keychat y Olas. Todo se ejecuta localmente contra datos simulados, por lo que las simulaciones no generan claves ni se conectan a relays. Cada simulación enlaza al sitio web y al repositorio de código del cliente real, lo que convierte a Sandstr en una herramienta de incorporación y comparación de interfaces en lugar de otro cliente de Nostr. Muestra cómo se sienten los feeds, los perfiles, los hilos, los mensajes directos, la búsqueda, los zaps y los controles de relay sin pedir a un usuario primerizo que tome una decisión de identidad o seguridad por adelantado.


### mineracks signer combina una extensión de navegador con un bunker de escritorio

[mineracks signer](https://github.com/mineracks/mineracks-signer) ofrece dos superficies de firma desde el mismo proyecto. Su extensión de navegador implementa [NIP-07](/es/topics/nip-07/) para que las aplicaciones web puedan solicitar firmas sin recibir la clave privada, mientras que la aplicación de escritorio expone un firmante remoto [NIP-46](/es/topics/nip-46/) para clientes que se comunican a través de relays.

La [versión de escritorio 0.1.0](https://github.com/mineracks/mineracks-signer/releases/tag/desktop-v0.1.0) del proyecto almacena el material de claves con la codificación de claves cifradas de NIP-49 y mantiene la clave descifrada dentro del proceso de Rust en lugar de pasarla a la interfaz. Cada solicitud muestra la aplicación que llama y la acción solicitada, mientras que la aprobación automática por aplicación es opcional y revocable. La primera compilación de escritorio admite Apple Silicon pero no los Mac con Intel.

## Versiones

### Jumble 26.8.1 añade controles de prueba de trabajo y vistas previas de comentarios

[Jumble 26.8.1](https://github.com/CodyTseng/jumble/releases/tag/v26.8.1) es un cliente de Nostr web y de escritorio. Recuerda la dificultad de la prueba de trabajo para publicar, muestra insignias de trabajo verificado, previsualiza los comentarios enlazados sobre el contenido externo, guarda imágenes desde el visor a pantalla completa y expande las biografías de perfil largas bajo demanda. Las notificaciones de reacciones ahora descartan los kinds de evento no admitidos, los avisos de desconexión de relay son menos ruidosos, se actualizaron los relays por defecto y se corrigió un conflicto de reproducción automática de medios.

### nostr-calendar 2.1.0 restablece la vinculación del firmante en formularios privados

[nostr-calendar 2.1.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v2.1.0) publica calendarios, eventos y respuestas de formularios como datos de Nostr. Vincula los envíos de formularios privados al firmante activo, guarda los eventos duplicados intencionados en los relays, corrige la obtención desde relays, analiza las fechas del calendario en hora local y añade notificaciones de la aplicación además de un cliente iOS. La corrección del firmante evita que una identidad obsoleta produzca una respuesta cifrada inutilizable.

### Manent 2.0.0 añade etiquetado y búsqueda para notas guardadas

[Manent 2.0.0](https://github.com/dtonon/manent/releases/tag/v2.0.0) es un archivo personal para notas de Nostr firmadas. Añade etiquetas locales y búsqueda, permitiendo al lector organizar y recuperar los eventos guardados sin modificar su contenido firmado.

### nosvelte 0.6.1 cierra las suscripciones vacías tras el EOSE

[nosvelte 0.6.1](https://github.com/akiomik/nosvelte/releases/tag/v0.6.1) proporciona componentes y hooks reactivos de Svelte para datos de relay. Las búsquedas vacías ahora se resuelven al llegar el End of Stored Events, la cancelación cierra el `REQ` subyacente, los reintentos limpian los errores obsoletos y los hooks de lista devuelven su valor vacío documentado. También reconoce los eventos direccionables independientemente de dónde aparezca su etiqueta `d`, sustituye los metadatos y artículos reemplazados, desduplica las reacciones por ID de evento y conserva todos los eventos del primer lote de un relay.

## Cambios sin publicar

### NMP vincula la admisión al relay a las declaraciones y amplía las consultas de grupo

[NMP](https://github.com/pablof7z/nmp) es un kit de herramientas de TypeScript para construir aplicaciones de Nostr e interfaces de grupos respaldados por relays. El [PR #1254](https://github.com/pablof7z/nmp/pull/1254) hace que la admisión al relay siga al propietario de la declaración que la autoriza, manteniendo la decisión de permisos vinculada al estado firmado de Nostr. El [PR #1255](https://github.com/pablof7z/nmp/pull/1255) generaliza las consultas de grupos gestionados por relays de [NIP-29](/es/topics/nip-29/) en lugar de asumir una única forma de búsqueda restringida. Ambos cambios están fusionados pero aún no han aparecido en una versión etiquetada.

### Mosaico deriva la identidad de grupo gestionado de los registros del relay

[Mosaico](https://github.com/pablof7z/mosaico) es un cliente de Nostr para explorar y administrar comunidades gestionadas por relays. El [PR #758](https://github.com/pablof7z/mosaico/pull/758) deriva la identidad de un grupo gestionado del relay que aloja sus registros autoritativos. El [PR #757](https://github.com/pablof7z/mosaico/pull/757) observa el registro publicado del grupo al resolver el estado de administración. Esto mantiene distintos a dos grupos con nombres similares en relays diferentes y ofrece a los clientes una fuente respaldada por relay para sus metadatos de gestión.

### Divine aísla los relays lentos durante las consultas multi-relay

[Divine](https://github.com/divinevideo/divine-mobile) es un cliente móvil de vídeo corto que publica y recupera vídeos a través de Nostr. El [PR #6673](https://github.com/divinevideo/divine-mobile/pull/6673) da a cada consulta de relay su propio tiempo de espera en lugar de dejar que una conexión estancada consuma el presupuesto de tiempo de toda una petición. Los resultados de los relays que responden pueden llegar así mientras el punto final lento se abandona de forma independiente. El cambio mejora la recuperación sin tratar un relay como autoritativo para el resultado combinado.

### rust-nostr refuerza el cifrado, los hashes y la reconciliación

[rust-nostr](https://github.com/rust-nostr/nostr) es una biblioteca y kit de herramientas de Rust para clientes, relays e implementaciones del protocolo Nostr. El [PR #1421](https://github.com/rust-nostr/nostr/pull/1421) reduce las asignaciones en su ruta de cifrado versionado de [NIP-44](/es/topics/nip-44/), mientras que el [PR #1423](https://github.com/rust-nostr/nostr/pull/1423) introduce hashes tipados que dificultan mezclar accidentalmente valores de resumen incompatibles. El [commit 21e31c2](https://github.com/rust-nostr/nostr/commit/21e31c28da3dfadedb5fa6e58c712647f16e5f69) evita que un mensaje malformado de reconciliación de conjuntos Negentropy de [NIP-77](/es/topics/nip-77/) desconecte el relay local. El trabajo fusionado refuerza tanto el manejo de cargas cifradas como el comportamiento ante fallos de reconciliación antes de la próxima versión.

### Zeus serializa los pagos NWC antes de cargar los presupuestos de gasto

[Zeus](https://github.com/ZeusLN/zeus) es un monedero móvil de Bitcoin y Lightning que puede exponer operaciones del monedero a través de Nostr Wallet Connect. El [PR #4305](https://github.com/ZeusLN/zeus/pull/4305) cuenta los pagos pendientes contra un presupuesto de [NIP-47](/es/topics/nip-47/) Nostr Wallet Connect en lugar de esperar a la liquidación. El [PR #4303](https://github.com/ZeusLN/zeus/pull/4303) serializa el manejo de pagos para que las solicitudes concurrentes no puedan competir a través del mismo límite de autorización. El par fusionado cierra una brecha de aplicación de presupuestos en la superficie de control Nostr del monedero.

### Nostr Components comparte un único intento de conexión al relay

[Nostr Components](https://github.com/saiy2k/nostr-components) es una biblioteca reutilizable de componentes web para añadir datos e interacciones de Nostr a las aplicaciones. El [PR #105](https://github.com/saiy2k/nostr-components/pull/105) permite que los componentes montados al mismo tiempo compartan un intento de conexión al relay en curso. Cada consumidor sigue recibiendo la conexión resultante, pero los montajes concurrentes ya no abren sockets duplicados mientras el primer apretón de manos está pendiente. El cambio reduce la carga evitable sobre los relays en aplicaciones ensambladas a partir de varios componentes independientes.

## Actualizaciones de NIPs y trabajo de especificación del protocolo

### Formatos de eventos de Nostr y descubrimiento

[El PR de NIP #2430](https://github.com/nostr-protocol/nips/pull/2430) propone paquetes de pegatinas como definiciones direccionables de kind `30031` y los paquetes instalados por un usuario como kind reemplazable `10031`. Cada etiqueta de pegatina lleva un código corto, un hash SHA-256 y un tipo MIME; la imagen permanece en un servidor [NIP-B7](https://github.com/nostr-protocol/nips/blob/master/B7.md) (almacenamiento de blobs Blossom). El borrador abierto estandariza así la identidad e instalación de paquetes sin colocar los bytes de la imagen en los eventos.

[El PR de NIP #2429](https://github.com/nostr-protocol/nips/pull/2429) propone documentos Gopher direccionables de kind `31436`. Cada evento contiene un nodo de texto o menú UTF-8, y los nodos firmados bajo una misma pubkey forman un gopherhole que cualquier puente RFC 1436 respaldado por relay puede servir. La propuesta abierta usa el almacenamiento ordinario de eventos direccionables en lugar de vincular la publicación a un único nombre de host Gopher.

[El PR de NIP #2428](https://github.com/nostr-protocol/nips/pull/2428) propone grupos privados con tickets por época. Un grupo rota las credenciales de membresía entre épocas, y los clientes presentan el ticket de la época actual para participar. El borrador apunta al chat privado sin pedir a un relay que trate un token portador permanente como membresía de por vida.

[El PR de NIP #2425](https://github.com/nostr-protocol/nips/pull/2425), cubierto como propuesta la semana pasada, ha fusionado ahora una aclaración de URI en [NIP-B0](/es/topics/nip-b0/) (marcadores web direccionables). Distingue los prefijos HTTPS omitidos de los esquemas URI explícitos cuando un marcador almacena su destino en la etiqueta `d`, evitando que los clientes reconstruyan un destino ambiguo.

### Pagos y conexiones de monedero

[El PR de NIP #2419](https://github.com/nostr-protocol/nips/pull/2419), cubierto como propuesta en la edición del 22 de julio, ha fusionado ahora un núcleo más reducido de [NIP-47](/es/topics/nip-47/) (Nostr Wallet Connect). Los URI de conexión, el transporte cifrado por relay, el descubrimiento de capacidades, la negociación de cifrado y los métodos comunes permanecen en el NIP; las notificaciones, las facturas retenidas, keysend, el historial de transacciones, los metadatos y el emparejamiento por enlace profundo pasan a un repositorio de extensiones dedicado. Las conexiones existentes siguen siendo compatibles mientras los monederos pueden implementar los contratos opcionales de forma independiente.

[El PR de NWC #2](https://github.com/nostr-wallet-connect/nwc/pull/2), cubierto como propuesta la semana pasada, ha fusionado ahora los métodos de pago BIP-321 en ese repositorio de extensiones. BIP-321 proporciona un URI de pago de Bitcoin común que puede transportar distintos raíles, de modo que quien llama a NWC puede solicitar o enviar un pago sin añadir un nuevo RPC central por cada tipo de instrucción subyacente.

### Capacidades del anfitrión de napplets

[El PR de NAP #95](https://github.com/napplet/naps/pull/95) propone el descubrimiento de catálogos para aplicaciones en sandbox distribuidas por Nostr. Un napplet pregunta a su anfitrión qué aplicaciones y capacidades están disponibles, y el anfitrión devuelve metadatos filtrados por política en lugar de exponer todo su entorno local. El contrato admite decisiones de lanzamiento sin conceder autoridad de ejecución durante el descubrimiento.

[El PR de NAP #33](https://github.com/napplet/naps/pull/33) propone subidas de archivos y blobs mediadas por el shell. Un napplet aporta los bytes y la intención; el anfitrión selecciona un raíl NIP-96 o Blossom, firma la autorización, informa del progreso y devuelve URL, hashes, datos MIME y etiquetas [NIP-94](/es/topics/nip-94/) (metadatos de archivo) listas para adjuntar. Las credenciales de almacenamiento y la autoridad HTTP nunca entran en el napplet.

### Grupos cifrados Marmot

[El PR de Marmot #410](https://github.com/marmot-protocol/marmot/pull/410) fusionó reglas de convergencia y de entrada diferida. Los clientes distinguen un objeto al que le falta una dependencia de época actual de una entrada obsoleta o no válida, lo mantienen elegible para una nueva obtención tras un rechazo de recursos y reintentan cuando otro commit cambia el contexto de descifrado. Un compromiso de estado con separación de dominio ofrece a las pruebas de conformidad un oráculo de convergencia compartido sin añadir un campo de producción al protocolo.

### Planos comunitarios de Concord

[El PR de Concord #14](https://github.com/concord-protocol/concord/pull/14) fusionó los mensajes que desaparecen de CORD-08. Un valor de metadatos de la comunidad fija la duración; los rumores de chat y las envolturas cifradas llevan una etiqueta de [NIP-40](/es/topics/nip-40/) (expiración de eventos), mientras que los eventos de borrado y el aviso de temporizador de kind `1740` están exentos. El temporizador firmado viaja con el estado de la comunidad, aunque el borrado por el relay sigue siendo una solicitud de retención y no una garantía criptográfica de eliminación.

[El PR de Concord #13](https://github.com/concord-protocol/concord/pull/13) fusionó en CORD-04 el fijado resistente a rotaciones. Cada canal tiene una lista de fijados que reemplaza por completo en el plano de control; las entradas llevan el sello firmado original más claves de expansión NIP-44 por mensaje, lo que permite a un miembro nuevo verificar el autor y el texto plano sin recibir una clave de época antigua. Las listas privadas pueden permanecer selladas a una época del canal, los topes acotan el tamaño de la lista y los borrados del autor eliminan fijados sin bifurcar la cadena del plano de control.

## Análisis en profundidad de NIPs

### Capacidad de búsqueda (NIP-50)

[NIP-50](/es/topics/nip-50/), definido en la [especificación principal](https://github.com/nostr-protocol/nips/blob/master/50.md), añade un filtro de búsqueda opcional para los relays. Los filtros ordinarios de Nostr funcionan cuando un cliente ya conoce un autor, un kind de evento, un identificador o una etiqueta; NIP-50 aborda el descubrimiento cuando la entrada es una consulta humana como `best nostr apps`.

El [formato de red de NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md#search-filter-field) añade una cadena `search` a un filtro normal dentro de un mensaje `REQ`. Una petición puede combinar ese campo con `kinds`, `authors`, `ids`, filtros de etiquetas y `limit`, y un REQ puede llevar varios filtros independientes. Un relay que lo admita debería buscar principalmente en el `content` del evento, puede usar otros campos cuando el kind de evento lo haga útil y debería ordenar según su propia puntuación de relevancia antes de aplicar el `limit`. Ese orden difiere del flujo habitual de eventos ordenados del más reciente al más antiguo.

La cadena de consulta puede incluir las [extensiones `key:value`](https://github.com/nostr-protocol/nips/blob/master/50.md#extensions) de la especificación. Nombra `include:spam`, `domain:`, `language:`, `sentiment:` y `nsfw:`; un relay debería ignorar las extensiones que no implemente. Los clientes descubren el soporte declarado a través del campo `supported_nips` de [NIP-11](/es/topics/nip-11/) del relay, pero aún pueden enviar el filtro a otros si están preparados para rechazar respuestas no relacionadas.

La [especificación de NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md) deliberadamente no estandariza la tokenización, el stemming, la clasificación, la detección de idioma, el análisis de sentimiento ni la clasificación de spam. Dos relays conformes pueden devolver eventos y ordenaciones diferentes para la misma consulta. Eso convierte al relay en un proveedor de índices y clasificación, no en una fuente de verdad. La especificación recomienda consultar varios relays compatibles, comprobar si los eventos devueltos satisfacen el caso de uso del cliente y descartar los relays cuyos resultados tengan mala precisión.

Esto difiere del [filtrado exacto de NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md). Un filtro de `authors` o `#t` tiene una semántica de coincidencia determinista que un cliente puede verificar directamente, mientras que una coincidencia de búsqueda puede depender de un índice y de una puntuación opaca. NIP-50 conserva el sobre de eventos firmados y el transporte de relay de NIP-01, pero acepta variación en el recall y la ordenación para hacer posible la recuperación abierta.

El evento siguiente es un resultado de búsqueda ilustrativo que usa los [siete campos de evento de NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures). Los valores hexadecimales repetidos son marcadores de posición y no una firma válida.

```json
{
  "id": "0000000000000000000000000000000000000000000000000000000000000000",
  "pubkey": "1111111111111111111111111111111111111111111111111111111111111111",
  "created_at": 1785888000,
  "kind": 1,
  "tags": [["t", "nostr"]],
  "content": "A comparison of Nostr search relays and their indexes.",
  "sig": "22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
}
```

Los clientes actuales usan el mismo filtro en distintas superficies de descubrimiento. [Nostria](https://github.com/nostria-app/nostria/blob/d291c2ab091c60c36f99c90241e2fd9da1b0c4bc/src/app/services/relays/search-relay.ts) envía búsquedas NIP-50 a relays de búsqueda dedicados, [Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useSearchEvents.ts) busca eventos a través de su pool de relays, y [NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/services/orchestration/SearchOrchestrator.ts) coordina búsquedas respaldadas por relays para la lectura de formato largo. Su distinto manejo de resultados refleja la libertad que NIP-50 deja a relays y clientes.

### Destacados (NIP-84)

[NIP-84](/es/topics/nip-84/), definido por su [especificación principal](https://github.com/nostr-protocol/nips/blob/master/84.md), asigna el kind `9802` a un destacado. Convierte un pasaje seleccionado, o una referencia a un medio no textual, en un evento firmado que puede moverse entre clientes de lectura, sociales y de anotación.

El [`content` del evento](https://github.com/nostr-protocol/nips/blob/master/84.md#format) contiene el texto seleccionado y puede estar vacío cuando la fuente es audio, vídeo u otro medio no textual. Un destacado apunta a una fuente de Nostr con una etiqueta `a` para un evento direccionable o una etiqueta `e` para un evento ordinario; una etiqueta `r` identifica una URL web. Los clientes que producen URL deberían eliminar los parámetros de seguimiento y otros parámetros de consulta no útiles antes de publicar, para que las variantes cosméticas de URL no fragmenten las referencias a la misma fuente.

Las [etiquetas `p`](https://github.com/nostr-protocol/nips/blob/master/84.md#attribution) opcionales atribuyen la fuente a una o más pubkeys de Nostr. Su cuarto valor puede identificar un rol como `author` o `editor`, y una etiqueta `context` puede conservar el texto circundante cuando la selección por sí sola resultaría poco clara. Un destacado con cita añade una etiqueta `comment` en lugar de publicar una segunda nota de kind `1`: la etiqueta `r` de la fuente recibe el marcador `source`, mientras que las pubkeys o URL mencionadas en el comentario llevan `mention`, lo que permite a los renderizadores distinguir la atribución de la respuesta del usuario.

La [definición del kind `9802`](https://github.com/nostr-protocol/nips/blob/master/84.md) convierte a un destacado en un evento regular en lugar de uno reemplazable. Repetir o corregir una selección crea otro evento firmado, y eliminar uno depende del flujo normal de solicitudes de borrado y de la política de retención del relay. La especificación no define desplazamientos de bytes, selectores ni una instantánea canónica del documento, por lo que un cliente puede ser incapaz de reubicar un pasaje después de que su fuente web cambie. Los destacados públicos también revelan intereses de lectura; la anotación privada requiere un diseño separado de cifrado y compartición.

NIP-84 difiere de un [evento de formato largo de NIP-23](https://github.com/nostr-protocol/nips/blob/master/23.md), que publica un artículo completo como kind `30023`; un destacado cita o apunta a material que puede permanecer en otro lugar. También difiere de un [conjunto de marcadores de NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md), que almacena una colección reemplazable de referencias. NIP-84 hace que cada selección sea firmada, atribuible, descubrible y discutible de forma independiente.

Este destacado ilustrativo contiene los [siete campos de evento de NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures). Su identificador y su firma son marcadores de posición.

```json
{
  "id": "3333333333333333333333333333333333333333333333333333333333333333",
  "pubkey": "4444444444444444444444444444444444444444444444444444444444444444",
  "created_at": 1785888000,
  "kind": 9802,
  "tags": [
    ["a", "30023:6666666666666666666666666666666666666666666666666666666666666666:relay-search", "wss://relay.example"],
    ["p", "6666666666666666666666666666666666666666666666666666666666666666", "wss://relay.example", "author"],
    ["context", "Search relays are indexes whose ranking policies can differ."]
  ],
  "content": "ranking policies can differ",
  "sig": "55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555"
}
```

El formato ya cruza las fronteras entre clientes. [nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) añadió renderizado de NIP-84 esta semana, [NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/components/ui/note-rendering/HighlightRenderer.ts) renderiza eventos de destacados en su cliente de formato largo, y [Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useCreateHighlight.ts) los publica a partir del contenido seleccionado. Esas implementaciones cubren la lectura, la creación y el renderizado social sin requerir que un único servicio sea dueño de la anotación.

---

Envía un DM por NIP-17 para compartir un proyecto o noticia a través del [proyecto Nostr Compass](https://github.com/andotherstuff/nostr-compass).
