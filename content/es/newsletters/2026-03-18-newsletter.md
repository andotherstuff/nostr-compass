---
title: 'Nostr Compass #14'
date: 2026-03-18
translationOf: /en/newsletters/2026-03-18-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Bienvenido de nuevo a Nostr Compass, tu guía semanal de Nostr.

**Esta semana:** [Amethyst](https://github.com/vitorpamplona/amethyst) implementa soporte completo de métodos [NIP-47](/es/topics/nip-47/) (Nostr Wallet Connect), [Alby Hub](https://github.com/getAlby/hub) añade soporte de múltiples relays en [v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6), [Amber](https://github.com/greenart7c3/Amber) lanza [v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3) con Tor integrado y permisos de firmante más granulares, y [Zeus](https://github.com/ZeusLN/zeus) elimina una ruta riesgosa de keysend NWC en [PR #3835](https://github.com/ZeusLN/zeus/pull/3835). [Notedeck](https://github.com/damus-io/notedeck) lanza un actualizador firmado en [v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2) que descubre versiones a través de eventos [NIP-94](/es/topics/nip-94/) (File Metadata), mientras [Damus](https://github.com/damus-io/damus) corrige estado obsoleto de [NIP-65](/es/topics/nip-65/) (Relay List Metadata), [Nostrability Outbox](https://github.com/nostrability/outbox) revisa sus resultados de benchmark con datos corregidos, y [Primal iOS](https://github.com/PrimalHQ/primal-ios-app) prueba suscripciones directas a relays para DMs. [Primal Android](https://github.com/PrimalHQ/primal-android-app) lanza [3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7), [Route96](https://github.com/v0l/route96) lanza [v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0), [OpenChat](https://github.com/DavidGershony/openChat) sigue ajustando la interoperabilidad con Marmot en [v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11), [Pika](https://github.com/sledtools/pika) consolida su runtime en [pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1), y [Nostria](https://github.com/nostria-app/nostria) añade filtrado Web of Trust con [NIP-85](/es/topics/nip-85/) (Trusted Assertions). El repositorio de NIPs fusiona el marcado Djot para [NIP-54](/es/topics/nip-54/) (Wiki) y un límite de entrada de 5000 caracteres para [NIP-19](/es/topics/nip-19/) (Bech32-Encoded Entities).

## Noticias

### El soporte de Wallet Connect se amplía, y los clientes de billetera ajustan rutas de fallo

[Amethyst](https://github.com/vitorpamplona/amethyst), el cliente Android mantenido por vitorpamplona, fusionó [PR #1828](https://github.com/vitorpamplona/amethyst/pull/1828), que acerca su implementación de [NIP-47](/es/topics/nip-47/) a la cobertura completa del protocolo. El parche añade `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance`, `get_info`, métodos de hold invoice, soporte de keysend con registros TLV, descubrimiento de capacidades vía kind `13194`, y eventos de notificación en kind `23197` con [NIP-44](/es/topics/nip-44/) (Encrypted Payloads). Esto da al cliente una superficie NWC mucho más amplia sin depender de extensiones específicas de cada app.

El stack de billeteras circundante se movió en la misma dirección. [Alby Hub](https://github.com/getAlby/hub), el nodo Lightning auto-custodiado y servicio de billetera detrás de muchos despliegues NWC, lanzó [v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6) con soporte de múltiples relays y flujos de conexión y swap más simples. [Zeus](https://github.com/ZeusLN/zeus), la billetera Lightning móvil, fusionó [PR #3835](https://github.com/ZeusLN/zeus/pull/3835) eliminando el soporte de keysend NWC después de identificar una ruta silenciosa de drenaje de fondos en ese flujo, mientras también corregía el manejo de eventos pendientes y actividad Cashu. La conectividad de billeteras en Nostr se está ampliando, y los implementadores están eliminando flujos que son difíciles de asegurar.

### Notedeck mueve el descubrimiento de versiones a Nostr

[Siguiendo la cobertura de Notedeck de la semana pasada](/en/newsletters/2026-03-11-newsletter/), [Notedeck](https://github.com/damus-io/notedeck), el cliente de escritorio nativo del equipo Damus, lanzó [v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2) después de fusionar [PR #1326](https://github.com/damus-io/notedeck/pull/1326). El nuevo actualizador se suscribe a eventos de versión kind `1063` firmados, coincide con la plataforma local, descarga el binario referenciado, y verifica su hash SHA256 antes de instalar. Los metadatos de versión ya no tienen que venir de la API de GitHub o un sitio web del proyecto. Una pubkey de versión de confianza y una conexión a relay son suficientes.

El mismo parche añade un CLI `notedeck-release` que publica esos eventos desde artefactos de versión de GitHub, lo que significa que el pipeline de versiones ahora tiene una ruta de publicación nativa de Nostr además de una ruta de descubrimiento nativa de Nostr. También acerca el modelo de actualizador de Damus y Notedeck al flujo de versiones firmadas publicadas por relay de Zapstore: la herramienta `zsp` de Zapstore ya maneja activos de software como eventos kind `1063` o `3063`, así que esta ruta no está bloqueada a un solo cliente o publicador. El resto del release candidate es trabajo práctico de escritorio: columnas de follows, "Ver Como Usuario" en perfiles, soporte de [NIP-59](/es/topics/nip-59/) (Gift Wrap), estadísticas de notas en tiempo real, y manejo de limitaciones de [NIP-11](/es/topics/nip-11/) (Relay Information Document), pero el actualizador es la parte que probablemente sobrevivirá a este ciclo de versión.

### El estado del relay se acerca al comportamiento en tiempo de ejecución

[Damus](https://github.com/damus-io/damus) fusionó [PR #3665](https://github.com/damus-io/damus/pull/3665), reemplazando un ID de evento de lista de relays almacenado obsoleto con una consulta directa a la base de datos para el último evento kind `10002`. Cuando el valor antiguo quedaba obsoleto, las operaciones de añadir y eliminar relays podían recurrir a listas bootstrap o de un año de antigüedad, lo que hacía que algunos cambios de relay parecieran exitosos mientras dejaban el estado activo sin cambiar. [PR #3690](https://github.com/damus-io/damus/pull/3690) corrige una segunda ruta de fallo eliminando estado `lock.mdb` obsoleto durante la compactación LMDB para que la app no se bloquee con `SIGBUS` en el siguiente arranque.

[Primal iOS](https://github.com/PrimalHQ/primal-ios-app) abrió [PR #194](https://github.com/PrimalHQ/primal-ios-app/pull/194), que se suscribe directamente a los relays de escritura [NIP-04](/es/topics/nip-04/) (Encrypted Direct Messages) de un interlocutor mientras una conversación está abierta, manteniendo el servidor de caché como respaldo. [Nostur](https://github.com/nostur-com/nostur-ios-public) abrió [PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53), que combina puntuación aleatoria de relays, filtrado de actividad [NIP-66](/es/topics/nip-66/) de nostr.watch, y muestreo de Thompson para cambiar la selección de relays de una heurística fija a una política aprendida. Los clientes han tratado la elección de relay como datos de configuración durante mucho tiempo. Más apps ahora lo tratan como estado en vivo que necesita lógica de medición y reparación.

## Lanzamientos

### Primal Android 3.0.7

[Primal Android](https://github.com/PrimalHQ/primal-android-app), el cliente Android de Primal, lanzó [3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7) con un nuevo ciclo de encuestas y billetera. [PR #945](https://github.com/PrimalHQ/primal-android-app/pull/945) añade votación en encuestas basada en zaps, [PR #948](https://github.com/PrimalHQ/primal-android-app/pull/948) pagina la carga de votos para que las encuestas más grandes sigan siendo usables, y [PR #965](https://github.com/PrimalHQ/primal-android-app/pull/965) obtiene recibos de zap para todas las transacciones. El mismo lanzamiento también etiqueta eventos soportados con metadatos de cliente [NIP-89](/es/topics/nip-89/) (Recommended Application Handlers) en [PR #968](https://github.com/PrimalHQ/primal-android-app/pull/968), lo que ayuda a los clientes downstream a atribuir orígenes de eventos de forma más limpia.

### Amber v4.1.3

[Siguiendo la cobertura de Amber de la semana pasada](/en/newsletters/2026-03-11-newsletter/), [Amber](https://github.com/greenart7c3/Amber), la app firmante Android para flujos [NIP-55](/es/topics/nip-55/) (Android Signer Application), lanzó [v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3). El lanzamiento se construye sobre su reciente trabajo de autenticación de relay [NIP-42](/es/topics/nip-42/) con más endurecimiento operacional: [PR #327](https://github.com/greenart7c3/Amber/pull/327) añade Tor integrado junto al soporte de Orbot, [PR #324](https://github.com/greenart7c3/Amber/pull/324) reemplaza permisos de cifrado gruesos basados en NIP con reglas específicas por tipo de contenido, y [PR #336](https://github.com/greenart7c3/Amber/pull/336) elimina permisos de red de la variante offline mientras [PR #335](https://github.com/greenart7c3/Amber/pull/335) añade verificaciones CI para mantenerlo así. [PR #322](https://github.com/greenart7c3/Amber/pull/322) también mueve el almacenamiento de PIN a DataStore cifrado.

Este lanzamiento ajusta el límite del firmante en sí. Esto es útil para cualquier flujo Android que entregue claves reales o decisiones de autenticación de relay a Amber, porque la parte difícil no es solo lo que el firmante puede hacer. También es cuán estrechamente puede ser acotado.

### Route96 v0.6.0

[Siguiendo la cobertura de Route96 de la semana pasada](/en/newsletters/2026-03-11-newsletter/), [Route96](https://github.com/v0l/route96), el servidor de medios que soporta Blossom y [NIP-96](/es/topics/nip-96/) (HTTP File Storage), lanzó [v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0). El lanzamiento mueve la configuración y el estado de whitelist a la base de datos con recarga en caliente y añade políticas de retención para archivos fríos o envejecidos. También añade un endpoint `GET /user/files` más rico además de seguimiento de estadísticas de archivo para descargas y egress, lo que da a los operadores más visibilidad sobre cómo se usa su servidor de almacenamiento.

### OpenChat v0.1.0-alpha.11

[Siguiendo la cobertura de OpenChat de la semana pasada](/en/newsletters/2026-03-11-newsletter/), [OpenChat](https://github.com/DavidGershony/openChat), el cliente de chat basado en Avalonia construido sobre el stack Marmot, lanzó [v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11) después de una semana de trabajo rápido de protocolo. [Commit c33895d](https://github.com/DavidGershony/openChat/commit/c33895d6b1a198f01b9b01a7be974bdce033fb9c) envuelve eventos Welcome en gift wrap [NIP-59](/es/topics/nip-59/) y elimina los shims antiguos de normalización de etiquetas MIP-00, [commit 2738ff4](https://github.com/DavidGershony/openChat/commit/2738ff428154f60f50debb8f2a53662d427b28f1) completa la auditoría de cumplimiento MIP-02, y [commit 8e470cf](https://github.com/DavidGershony/openChat/commit/8e470cf7945bced010168c8229d73d67db638b9f) hace lo mismo para el cifrado de mensajes de grupo MIP-03. [Commit 129ca37](https://github.com/DavidGershony/openChat/commit/129ca37e264efaa2d1a8b04fe95cd72e5e212547) también consolida el manejo de NIP-44 en la implementación compartida de marmot-cs, reduciendo el riesgo de divergencia criptográfica del lado del cliente.

### nak v0.19.0 y v0.19.1

[nak](https://github.com/fiatjaf/nak), el toolkit de línea de comandos para Nostr de fiatjaf, lanzó [v0.19.0](https://github.com/fiatjaf/nak/releases/tag/v0.19.0) y [v0.19.1](https://github.com/fiatjaf/nak/releases/tag/v0.19.1). La serie 0.19 añade una UI de foro de grupo en [commit 5f4efdb](https://github.com/fiatjaf/nak/commit/5f4efdbc69a36fc80ea3f97b2cdee1db6a7c5b47), cambia las ediciones de metadatos de grupo a un flujo de reemplazo completo en [commit da0b753](https://github.com/fiatjaf/nak/commit/da0b75337198010687aceb6a07bbae67407faee3), y reemplaza el manejo anterior de `no-text` con `supported_kinds` en [commit bef67d3](https://github.com/fiatjaf/nak/commit/bef67d35d259e0450debf0fd870e1a937a2406bf). Para implementadores de grupos, esto mantiene el CLI alineado con la dirección en que se mueven las especificaciones y clientes de grupo.

## Actualizaciones de Proyectos

### Amethyst

[Siguiendo la cobertura de Amethyst de la semana pasada](/en/newsletters/2026-03-11-newsletter/), [Amethyst](https://github.com/vitorpamplona/amethyst), el cliente Android con una de las superficies de protocolo más amplias en Nostr, siguió construyendo sobre su trabajo de billetera y relay después del parche NIP-47. [PR #1853](https://github.com/vitorpamplona/amethyst/pull/1853) añade consultas COUNT de [NIP-45](/es/topics/nip-45/) (Event Counting) a través de las pantallas de gestión de relays, para que los usuarios puedan ver cuántos eventos tiene realmente cada relay para feed principal, notificaciones, DMs y datos de índice. [PR #1849](https://github.com/vitorpamplona/amethyst/pull/1849) añade subidas de archivos cifrados para chats [NIP-17](/es/topics/nip-17/) (Private Direct Messages), con una ruta de reintento para subidas sin cifrar cuando un host de almacenamiento rechaza la versión cifrada.

[PR #1791](https://github.com/vitorpamplona/amethyst/pull/1791) también trae login completo de bunker de escritorio [NIP-46](/es/topics/nip-46/) (Nostr Connect) con un indicador de latido, lo que importa porque los fallos de firma remota a menudo se sienten como roturas aleatorias de UI desde el lado del usuario. El cliente muestra si el firmante está vivo y cuán recientemente respondió, mientras también hace obvio cuando la sesión actual usa un bunker.

### Nostria

[Nostria](https://github.com/nostria-app/nostria), el cliente multiplataforma construido alrededor de un stack local-first, fusionó [PR #561](https://github.com/nostria-app/nostria/pull/561) añadiendo filtrado Web of Trust para feeds y respuestas en hilos. La funcionalidad usa los datos de clasificación del servicio de confianza existente y los expone tanto como filtro de feed como filtro de respuestas, ocultando autores cuya clasificación no supera el umbral mientras preserva la estructura del hilo cuando hay descendientes de confianza presentes. Esto da a los usuarios una capa intermedia entre "mostrar a todos" y curación hardcodeada basada en listas.

La misma semana también trajo [PR #563](https://github.com/nostria-app/nostria/pull/563), que añade filtrado de contenido y soporte de reposts a la página de resumen. Fuera de la lista de PRs rastreados, Nostria también ha estado completando más de su superficie de usuario avanzado. Ahora soporta el último servicio Web of Trust de Brainstorm con registro en la app, junto con flujos de enviar y recibir dinero en DMs usando NWC e invoices BOLT-11. También añade manejo nativo de GIFs a través del NIP de emoji y una ruta de importación RSS más robusta para músicos que puede recoger splits Lightning existentes de feeds de podcast. Nostria está tratando clasificación, medios, pagos y publicación como una superficie de app conectada.

### Nostur

[Nostur](https://github.com/nostur-com/nostur-ios-public), el cliente iOS mantenido por nostur-com, abrió [PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53) para cambiar el enrutamiento outbox de un plan fijo a una política con puntuación. El parche añade puntuación aleatoria de relays, filtrado de actividad de relays [NIP-66](/es/topics/nip-66/) con un feed en caché de nostr.watch, y muestreo de Thompson para que los datos de éxito y fallo de relay cambien las selecciones futuras. El diseño mantiene una válvula de seguridad cuando demasiados relays serían filtrados y preserva los relays `.onion`. Este es uno de los ejemplos actuales más claros de un cliente tratando la selección de relays como un sistema adaptativo.

### Nostrability Outbox

[Siguiendo el informe anterior de benchmarks Outbox](/es/newsletters/2026-03-04-newsletter/#el-modelo-outbox-bajo-la-lupa), [Nostrability Outbox](https://github.com/nostrability/outbox), el proyecto de benchmarks y análisis enfocado en enrutamiento de clientes con [NIP-65](/es/topics/nip-65/) y [NIP-66](/es/topics/nip-66/), pasó la semana ajustando sus propias afirmaciones. [PR #35](https://github.com/nostrability/outbox/pull/35) reemplaza resultados inflados de Thompson-sampling con un re-benchmark completo a través de 1.511 ejecuciones y recomienda la variante `CG3` para enrutamiento estilo NDK. [PR #43](https://github.com/nostrability/outbox/pull/43) añade comparaciones de decay y casos de uso, corrige un bug de envenenamiento de caché de `0 follows`, y luego re-ejecuta el dataset Telluride después de fijar los TTLs de caché.

Esto no es trabajo de producto en el sentido habitual, pero importa para autores de clientes porque los números del proyecto ahora son más precisos y menos halagüeños en los lugares donde previamente habían sobreestimado. El resultado corregido sigue siendo útil. La selección aleatoria sigue superando al enrutamiento puramente determinista en los casos que Outbox le importan, el aprendizaje estilo Thompson puede mejorar materialmente la cobertura cuando los clientes persisten historial útil de relay, y el filtrado de actividad [NIP-66](/es/topics/nip-66/) elimina tiempo perdido en relays muertos. El trabajo también se está convirtiendo en propuestas concretas de implementación, incluyendo [NDK #387](https://github.com/nostr-dev-kit/ndk/pull/387), [Nostur #53](https://github.com/nostur-com/nostur-ios-public/pull/53), [Amethyst #1833](https://github.com/vitorpamplona/amethyst/pull/1833), [rust-nostr #1282](https://github.com/rust-nostr/nostr/pull/1282), [welshman #53](https://github.com/coracle-social/welshman/pull/53), y [applesauce #54](https://github.com/hzrd149/applesauce/pull/54) más [applesauce #55](https://github.com/hzrd149/applesauce/pull/55).

### Backend de White Noise

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs), el backend Rust usado por White Noise y otras herramientas Marmot, fusionó dos parches de endurecimiento de límites alrededor del manejo de medios Blossom. [PR #637](https://github.com/marmot-protocol/whitenoise-rs/pull/637) impone HTTPS en URLs de Blossom y añade un timeout de subida, mientras [PR #642](https://github.com/marmot-protocol/whitenoise-rs/pull/642) limita las descargas de blob a `100 MiB` para bloquear que descargas de medios sobredimensionados se conviertan en una ruta de denegación de servicio. Para software de mensajería privada, las URLs de medios son una de las interfaces más agudas entre la lógica de aplicación cifrada y la infraestructura de red no confiable. Esta semana el equipo ajustó ese borde.

### rust-nostr

[rust-nostr](https://github.com/rust-nostr/nostr), la biblioteca de protocolo Rust, fusionó [PR #1280](https://github.com/rust-nostr/nostr/pull/1280) añadiendo constructores de conveniencia para `LocalRelayBuilderNip42`. Los nuevos helpers de lectura y escritura dan a las configuraciones de relay embebido y pruebas una forma más clara de convertir la política de autenticación [NIP-42](/es/topics/nip-42/) en código. Este es un parche de biblioteca pequeño, pero importa para equipos construyendo relays locales o integrados en apps que necesitan autenticación activada sin repetir boilerplate cada vez.

### Pika

[Siguiendo la cobertura anterior de Pika](/es/newsletters/2026-03-04-newsletter/), [Pika](https://github.com/sledtools/pika), la app de mensajería basada en Marmot, lanzó [pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1) y [pikachat-v1.1.1](https://github.com/sledtools/pika/releases/tag/pikachat-v1.1.1) con un ciclo de lanzamiento enfocado en la convergencia del runtime. [PR #542](https://github.com/sledtools/pika/pull/542) introduce una fachada de runtime Marmot compartida para el CLI y sidecar, con el host de la app moviéndose a la misma superficie. [PR #556](https://github.com/sledtools/pika/pull/556) ajusta el ciclo de vida del agente OpenClaw y el estado de provisioning, mientras [PR #600](https://github.com/sledtools/pika/pull/600) añade restauración desde respaldo y seguridad de recuperación más estricta para entornos gestionados.

La superficie directa orientada al usuario aquí es más pequeña que en el último artículo sobre Pika, pero el cambio arquitectónico es significativo. Mover la lógica de grupo, medios, llamadas y sesión detrás de un runtime compartido reduce la posibilidad de que la app y el daemon diverjan a medida que el stack Marmot crece.

## Actualizaciones de NIPs

Cambios recientes al [repositorio de NIPs](https://github.com/nostr-protocol/nips):

**Fusionados:**

- **[NIP-54](/es/topics/nip-54/) (Wiki): Cambio de Asciidoc a Djot** ([PR #2242](https://github.com/nostr-protocol/nips/pull/2242)): El contenido wiki en kind `30818` ahora usa Djot como formato de marcado canónico. El texto fusionado añade comportamiento explícito de wikilinks, ejemplos de merge-request para kind `818`, ejemplos de redirección para kind `30819`, y ejemplos de normalización para scripts no latinos en etiquetas `d`. Esto da a los implementadores un objetivo de parseo más limpio que Asciidoc y elimina una ruta más de especificación que dependía de un toolchain centrado en Ruby.

- **[NIP-19](/es/topics/nip-19/) (Bech32-Encoded Entities): Añadir límite de entrada** ([PR #2264](https://github.com/nostr-protocol/nips/pull/2264)): La especificación ahora recomienda limitar las cadenas de entidades codificadas en Bech32 a 5000 caracteres. Este es un cambio pequeño con valor real para parsers, porque las cadenas NIP-19 ahora aparecen en flujos QR, deep links, hojas de compartir, y entrada pegada por usuarios a través de muchos clientes.

**PRs Abiertos y Discusiones:**

- **Archivo de Clave Nostr para [NIP-49](/es/topics/nip-49/) (Private Key Encryption)** ([PR #2269](https://github.com/nostr-protocol/nips/pull/2269)): Propone un formato de archivo `.nostrkey` para exportación e importación de claves cifradas con contraseña. Si se fusiona, daría a los clientes una ruta de respaldo basada en archivos más normal que copiar cadenas `ncryptsec` en bruto.

- **Consistencia del estado de membresía para [NIP-43](/es/topics/nip-43/) (Relay Access Metadata and Requests)** ([PR #2267](https://github.com/nostr-protocol/nips/pull/2267)): Añade una sección aclarando que los relays deberían mantener un estado de membresía autoritativo por pubkey. Esto simplificaría la lógica de clientes de grupo alrededor de cambios de membresía e historial reproducido.

- **Guía de eliminación para [NIP-17](/es/topics/nip-17/) (Private Direct Messages)** ([PR #2260](https://github.com/nostr-protocol/nips/pull/2260)): Propone una ruta concreta para editar y eliminar mensajes privados a través de eventos de eliminación envueltos en gift wrap. El trabajo aún está abierto, pero los autores de clientes necesitan una respuesta aquí si NIP-17 va a reemplazar completamente los flujos de DM más antiguos.

- **URI de share-intent para [NIP-222](/es/topics/nip-222/)** ([PR #2266](https://github.com/nostr-protocol/nips/pull/2266)): El borrador estandarizaría cómo las apps móviles y de escritorio entregan contenido compartido a un cliente Nostr. Este es uno de los bordes de interoperabilidad más ásperos en los flujos actuales de app a app.

## NIP Deep Dive: NIP-94 (File Metadata)

[NIP-94](/es/topics/nip-94/) define kind `1063` como un evento de metadatos de primera clase para un archivo. La [especificación](https://github.com/nostr-protocol/nips/blob/master/94.md) da al evento su propio `content` legible por humanos más etiquetas legibles por máquinas para URL de descarga, tipo MIME, hashes, dimensiones, previsualizaciones, respaldos y pistas del servicio de almacenamiento. Esto importa porque el archivo se vuelve consultable en relays como su propio objeto. Un cliente no tiene que extraer metadatos del contenido circundante para entender qué es el archivo.

```json
{
  "id": "6a92ef8d7c3a1b5d4e8f9a0b1c2d3e4f567890abcdef1234567890abcdef1234",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1742342400,
  "kind": 1063,
  "tags": [
    ["url", "https://downloads.example.org/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["m", "application/gzip"],
    ["x", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["ox", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["size", "48392011"],
    ["dim", "0x0"],
    ["magnet", "magnet:?xt=urn:btih:00112233445566778899aabbccddeeff00112233"],
    ["i", "00112233445566778899aabbccddeeff00112233"],
    ["blurhash", "LEHV6nWB2yk8pyo0adR*.7kCMdnj"],
    ["thumb", "https://downloads.example.org/notedeck/v0.8.0-rc2/thumb.png", "bbccddeeff00112233445566778899aabbccddeeff0011223344556677889900"],
    ["image", "https://downloads.example.org/notedeck/v0.8.0-rc2/screenshot.png", "ccddeeff00112233445566778899aabbccddeeff001122334455667788990011"],
    ["summary", "Signed macOS release artifact for Notedeck v0.8.0-rc2"],
    ["alt", "Notedeck desktop release archive"],
    ["fallback", "https://mirror.example.net/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["service", "nip96"]
  ],
  "content": "Notedeck macOS universal build",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

Las etiquetas hacen más trabajo del que aparentan a primera vista. `x` identifica el archivo servido, mientras `ox` identifica el archivo original antes de cualquier transformación del lado del servidor. Las etiquetas de previsualización permiten a los clientes construir índices de archivos navegables sin descargar el activo completo, y `summary` puede llevar un extracto breve junto a ellos. `fallback` da una segunda fuente cuando la URL principal falla, y `service` sugiere el protocolo de almacenamiento detrás del archivo, como [NIP-96](/es/topics/nip-96/) u otro host. NIP-94 por lo tanto se sitúa debajo de las publicaciones sociales y por encima del almacenamiento en bruto. Describe el archivo, no la conversación alrededor del archivo.

Por eso el actualizador de Notedeck de esta semana es interesante. [PR #1326](https://github.com/damus-io/notedeck/pull/1326) usa eventos kind `1063` firmados para el descubrimiento de versiones de software, luego verifica el binario descargado contra el SHA256 publicado. La misma forma de evento puede describir un artefacto de software o una subida de medios. NIP-94 es lo suficientemente antiguo como para ser estable, pero aún tiene espacio para crecer porque más proyectos están tratando los eventos de metadatos como un transporte para máquinas, no solo como decoración para personas.

## NIP Deep Dive: NIP-54 (Wiki)

[NIP-54](/es/topics/nip-54/) define kind `30818` como un evento de artículo wiki. La [especificación](https://github.com/nostr-protocol/nips/blob/master/54.md) trata la etiqueta `d` como el tema normalizado del artículo y permite que muchos autores publiquen entradas para el mismo tema. El cuerpo del artículo vive en `content`, mientras las etiquetas manejan identidad normalizada, título de visualización, resúmenes, y referencias a versiones anteriores. Esto significa que NIP-54 no es solo un formato de contenido. También es un problema de recuperación y clasificación, porque cada cliente aún tiene que decidir qué versión del artículo mostrar.

```json
{
  "id": "8c94e5d1f2a300112233445566778899aabbccddeeff00112233445566778899",
  "pubkey": "00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff",
  "created_at": 1742342400,
  "kind": 30818,
  "tags": [
    ["d", "nostr-wiki"],
    ["title", "Nostr Wiki"],
    ["summary", "Djot-formatted reference article about Nostr wiki events"],
    ["a", "30818:11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff:nostr-wiki", "wss://relay.example.org", "fork"],
    ["e", "11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff", "wss://relay.example.org", "fork"]
  ],
  "content": "Nostr is a [protocol][] for carrying events across relays.\n\n[protocol]: nostr:nevent1example",
  "sig": "33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889900112233cc44dd55ee66ff77889900aabbccddeeff00112233445566778899001122"
}
```

La fusión de esta semana cambia el marcado canónico de Asciidoc a Djot en [PR #2242](https://github.com/nostr-protocol/nips/pull/2242). Esto importa para implementadores porque Djot tiene una especificación standalone más ajustada y una historia de parser más simple entre lenguajes. El texto fusionado también aclara cómo resuelven los wikilinks de estilo referencia, cómo los merge requests usan kind `818`, cómo las redirecciones usan kind `30819`, y cómo debería comportarse la normalización de etiquetas `d` para scripts no latinos. Esas son las partes que hacen que dos clientes independientes coincidan en a qué artículo apunta un enlace.

NIP-54 también se sitúa en un lugar inusual en el protocolo. Un cliente wiki necesita renderizado de contenido, pero también necesita política de clasificación. Reacciones, listas de relays, listas de contactos, y señales de deferencia explícita, todo alimenta qué artículo gana para un tema dado. El cambio a Djot no resuelve ese problema de clasificación, pero sí elimina una de las ambigüedades de parser que estaba debajo. Por eso la fusión importa ahora: el cambio trata menos sobre un formato de prosa más bonito y más sobre hacer que el comportamiento wiki multi-cliente sea más fácil de implementar consistentemente.

¿Estás construyendo algo, o quieres que lo cubramos? Escríbenos vía DM [NIP-17](/es/topics/nip-17/) en Nostr a `npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923`.
