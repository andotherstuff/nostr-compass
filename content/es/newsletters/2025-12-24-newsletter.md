---
title: 'Nostr Compass #2'
date: 2025-12-24
publishDate: 2025-12-24
draft: false
type: newsletters
translationOf: /en/newsletters/2025-12-24-newsletter.md
translationDate: 2025-12-26
---

Bienvenido de nuevo a Nostr Compass, tu guía semanal del ecosistema del protocolo Nostr.

**Esta semana:** Tres implementaciones de firmadores [NIP-55](/es/topics/nip-55/) reciben actualizaciones: Amber añade caché de rendimiento, Aegis obtiene soporte para URI `nostrsigner:`, y Primal Android se une a ellos como firmador local completo. Shopstr introduce "Zapsnags" para ventas flash vía zaps. Mostro añade un fondo de desarrollo. Cuatro actualizaciones de NIP aterrizan incluyendo Mensajes Públicos (kind 24) y mejoras de privacidad de grupos. Las consultas de caché de NDK se aceleran 162x, Applesauce añade reacciones y soporte de billetera NIP-60, y Tenex introduce arquitectura RAL para delegación de agentes IA. En nuestra profundización, explicamos [NIP-02](/es/topics/nip-02/) (listas de seguidos) y [NIP-10](/es/topics/nip-10/) (hilos de respuestas), especificaciones fundamentales para construir líneas de tiempo sociales y conversaciones.

## Noticias {#news}

**Primal Android Se Convierte en Firmador NIP-55** - Construyendo sobre el [soporte de Nostr Connect de la semana pasada](/es/newsletters/2025-12-17-newsletter/#primal-android), Primal ha implementado capacidades completas de firma local a través de ocho pull requests fusionados. La implementación incluye un `LocalSignerContentProvider` completo que expone operaciones de firma a otras apps Android vía la interfaz de content provider de Android, siguiendo la especificación [NIP-55](/es/topics/nip-55/). La arquitectura separa responsabilidades limpiamente: `SignerActivity` maneja flujos de aprobación cara al usuario, `LocalSignerService` gestiona operaciones en segundo plano, y un nuevo sistema de permisos permite a los usuarios controlar qué apps pueden solicitar firmas. Esto hace de Primal una alternativa viable a Amber para usuarios de Android que quieren mantener sus claves en una app mientras usan otras para diferentes experiencias Nostr.

**Shopstr Zapsnags: Ventas Flash vía Lightning** - El mercado nativo de Nostr introdujo ["Zapsnags"](https://github.com/shopstr-eng/shopstr/pull/211), una función de venta flash que permite a los compradores adquirir artículos directamente desde su feed social con un solo zap. La implementación filtra notas kind 1 etiquetadas con `#shopstr-zapsnag` y las renderiza como tarjetas de producto con un botón "Zap para Comprar" en lugar del flujo de carrito estándar. Cuando un comprador zapea, el sistema genera una solicitud de pago usando [NIP-57](/es/topics/nip-57/), consulta el recibo de zap kind 9735 para confirmar el pago, luego encripta la información de envío usando gift wrapping [NIP-17](/es/topics/nip-17/) antes de enviarla de forma privada al vendedor. La función almacena detalles del comprador localmente para compras repetidas e incluye un panel de comerciante para crear listados de venta flash. Es una combinación inteligente de primitivos sociales, de pago y privacidad que demuestra cómo el diseño componible de Nostr permite patrones de comercio novedosos.

**Mostro Introduce Fondo de Desarrollo** - El bot de trading P2P de Bitcoin [NIP-69](/es/topics/nip-69/) [implementó tarifas de desarrollo configurables](https://github.com/MostroP2P/mostro/pull/555) para apoyar el mantenimiento sostenible. Los operadores pueden establecer `dev_fee_percentage` entre 10-100% de la tarifa de trading de Mostro (por defecto 30%), que se enruta automáticamente a un fondo de desarrollo en cada operación exitosa. La implementación añade tres columnas de base de datos (`dev_fee`, `dev_fee_paid`, `dev_fee_payment_hash`) para rastrear contribuciones y valida el porcentaje al inicio del daemon. La documentación técnica en [`docs/DEV_FEE.md`](https://github.com/MostroP2P/mostro/blob/main/docs/DEV_FEE.md) explica el sistema. Este modelo opt-in permite a los operadores apoyar el desarrollo continuo mientras mantienen total transparencia sobre la asignación de tarifas.

## Actualizaciones de NIP {#nip-updates}

Cambios recientes al [repositorio de NIPs](https://github.com/nostr-protocol/nips):

**Nuevos NIPs:**
- **[NIP-A4](/es/topics/nip-a4/) (Mensajes Públicos, kind 24)** - Un nuevo kind para mensajes de pantalla de notificación diseñados para amplio soporte de clientes ([#1988](https://github.com/nostr-protocol/nips/pull/1988)). A diferencia de conversaciones con hilos, estos mensajes no tienen concepto de historial de chat o cadenas de mensajes. Usan etiquetas `q` (citas) en lugar de etiquetas `e` para evitar complicaciones de hilos, haciéndolos ideales para notificaciones públicas simples que aparecen en el feed de notificaciones de un destinatario sin crear estado de conversación.

**Cambios Significativos:**
- **[NIP-29](/es/topics/nip-29/)** - Clarificación mayor de semántica de grupos ([#2106](https://github.com/nostr-protocol/nips/pull/2106)). La etiqueta `closed` ahora significa "incapaz de escribir" (solo lectura para no miembros), desacoplada de la mecánica de unirse. Una nueva etiqueta `hidden` previene que los relays sirvan metadata o eventos de miembros a no miembros, permitiendo grupos verdaderamente privados que son indescubribles sin invitación fuera de banda. La etiqueta `private` controla visibilidad de mensajes mientras permite metadata pública para descubrimiento.
- **[NIP-51](/es/topics/nip-51/)** - Añadido kind 30006 para conjuntos de imágenes curadas ([#2170](https://github.com/nostr-protocol/nips/pull/2170)), siguiendo el patrón de 30004 (artículos) y 30005 (videos). Ya implementado en Nostria.
- **[NIP-55](/es/topics/nip-55/)** - Clarificado inicio de conexión para firmadores Android ([#2166](https://github.com/nostr-protocol/nips/pull/2166)). Los desarrolladores implementando sesiones multi-usuario estaban usando mal `get_public_key` llamándolo desde procesos en segundo plano. La especificación actualizada recomienda llamarlo solo una vez durante la conexión inicial, previniendo un footgun de implementación común.

## Profundización en NIP: NIP-02 y NIP-10 {#nip-deep-dive-nip-02-and-nip-10}

Esta semana cubrimos dos NIPs esenciales para funcionalidad social: cómo los clientes saben a quién sigues y cómo se estructuran las conversaciones en hilos.

### [NIP-02](/es/topics/nip-02/): Lista de Seguidos

[NIP-02](https://github.com/nostr-protocol/nips/blob/master/02.md) define eventos kind 3, que almacenan tu lista de seguidos. Este mecanismo simple potencia el grafo social que hace posibles las líneas de tiempo.

**Estructura:** Un evento kind 3 contiene etiquetas `p` listando pubkeys seguidas:

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

Cada etiqueta `p` tiene cuatro posiciones: el nombre de la etiqueta, la pubkey seguida (hex), un hint de relay URL opcional, y un "petname" opcional (un apodo local). El hint de relay dice a otros clientes dónde encontrar los eventos de ese usuario. El petname te permite asignar nombres memorables a contactos sin depender de sus nombres de pantalla auto-declarados.

**Comportamiento reemplazable:** Kind 3 cae en el rango reemplazable (0, 3, 10000-19999), así que los relays mantienen solo la versión más reciente por pubkey. Cuando sigues a alguien nuevo, tu cliente publica un nuevo kind 3 completo conteniendo todos tus seguidos más el nuevo. Esto significa que las listas de seguidos deben ser completas cada vez; no puedes publicar actualizaciones incrementales.

**Construyendo líneas de tiempo:** Para construir un feed home, los clientes obtienen el kind 3 del usuario, extraen todas las pubkeys de etiquetas `p`, luego se suscriben a eventos kind 1 de esos autores:

```json
["REQ", "home", {"kinds": [1], "authors": ["91cf9...", "14aeb...", "612ae..."], "limit": 50}]
```

El relay devuelve notas coincidentes, y el cliente las renderiza. Los hints de relay en kind 3 ayudan a los clientes a saber qué relays consultar para cada usuario seguido.

**Petnames e identidad:** El campo petname habilita un esquema de nombres descentralizado. En lugar de confiar en cualquier nombre que un usuario reclame en su perfil, puedes asignar tu propia etiqueta. Un cliente podría mostrar "alice (Mi Hermana)" donde "alice" viene de su perfil kind 0 y "Mi Hermana" es tu petname. Esto proporciona contexto que los nombres de usuario globales no pueden.

**Consideraciones prácticas:** Debido a que los eventos kind 3 son reemplazables y deben ser completos, los clientes deberían preservar etiquetas desconocidas al actualizar. Si otro cliente añadió etiquetas que tu cliente no entiende, sobrescribir ciegamente perdería esos datos. Añade nuevos seguidos en lugar de reconstruir desde cero.

### [NIP-10](/es/topics/nip-10/): Hilos de Notas de Texto

[NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md) especifica cómo las notas kind 1 se referencian entre sí para formar hilos de respuestas. Entender esto es esencial para construir vistas de conversación.

**El problema:** Cuando alguien responde a una nota, los clientes necesitan saber: ¿A qué es esto una respuesta? ¿Cuál es la raíz de la conversación? ¿A quién se debe notificar? NIP-10 responde estas preguntas a través de etiquetas `e` (referencias de evento) y etiquetas `p` (menciones de pubkey).

**Etiquetas marcadas (preferidas):** Los clientes modernos usan marcadores explícitos en etiquetas `e`:

```json
{
  "id": "f9c2e...",
  "pubkey": "a3b9c...",
  "created_at": 1734912345,
  "kind": 1,
  "tags": [
    ["e", "abc123...", "wss://relay.example.com", "root"],
    ["e", "def456...", "wss://relay.example.com", "reply"],
    ["p", "91cf9..."],
    ["p", "14aeb..."]
  ],
  "content": "¡Buen punto! Estoy de acuerdo.",
  "sig": "b7d3f..."
}
```

El marcador `root` apunta a la nota original que inició el hilo. El marcador `reply` apunta a la nota específica que se está respondiendo. Si respondes directamente a la raíz, usa solo `root` (no se necesita etiqueta `reply`). La distinción importa para el renderizado: el `reply` determina la indentación en una vista de hilo, mientras que `root` agrupa todas las respuestas juntas.

**Reglas de hilos:**
- Respuesta directa a raíz: Una etiqueta `e` con marcador `root`
- Respuesta a una respuesta: Dos etiquetas `e`, una `root` y una `reply`
- El `root` permanece constante a lo largo del hilo; `reply` cambia según a qué estés respondiendo

**Etiquetas pubkey para notificaciones:** Incluye etiquetas `p` para todos los que deberían ser notificados. Como mínimo, etiqueta al autor de la nota a la que respondes. La convención es también incluir todas las etiquetas `p` del evento padre (para que todos en la conversación estén al tanto), más cualquier usuario que @menciones en tu contenido.

**Hints de relay:** La tercera posición en etiquetas `e` y `p` puede contener una URL de relay donde ese evento o contenido de usuario podría encontrarse. Esto ayuda a los clientes a obtener el contenido referenciado incluso si no están conectados al relay original.

**Etiquetas posicionales deprecadas:** Las implementaciones tempranas de Nostr inferían significado de la posición de etiquetas en lugar de marcadores: la primera etiqueta `e` era raíz, la última era respuesta, las del medio eran menciones. Este enfoque está deprecado porque crea ambigüedad. Si ves etiquetas `e` sin marcadores, probablemente son de clientes antiguos. Las implementaciones modernas siempre deberían usar marcadores explícitos.

**Construyendo vistas de hilo:** Para mostrar un hilo, obtén el evento raíz, luego consulta todos los eventos con una etiqueta `e` referenciando esa raíz:

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

Ordena resultados por `created_at` y usa marcadores `reply` para construir la estructura de árbol. Los eventos cuyo `reply` apunta a la raíz son respuestas de nivel superior; los eventos cuyo `reply` apunta a otra respuesta son respuestas anidadas.

## Lanzamientos {#releases}

**Zeus v0.12.0** - Construyendo sobre el [soporte de pagos paralelos NWC de la semana pasada](/es/newsletters/2025-12-17-newsletter/#zeus), el [lanzamiento mayor](https://github.com/ZeusLN/zeus/releases/tag/v0.12.0) de la billetera Lightning incluye un servicio completo [NIP-47](/es/topics/nip-47/) Nostr Wallet Connect con soporte de relay personalizado y seguimiento de presupuesto. Una [corrección de recarga de presupuesto](https://github.com/ZeusLN/zeus/pull/3455) asegura que las conexiones usen límites actuales. [Copiar dirección Lightning](https://github.com/ZeusLN/zeus/pull/3460) ya no incluye el prefijo `lightning:`, corrigiendo problemas de pegado en campos de perfil Nostr.

**Amber v4.0.6** - El firmador [NIP-55](/es/topics/nip-55/) de Android [añade caché de rendimiento](https://github.com/greenart7c3/Amber/releases/tag/v4.0.6) a operaciones de firma y mejora el manejo de errores al desencriptar contenido malformado. La confiabilidad de conexión mejoró con lógica de reintentos para eventos de conexión de relay, y varias correcciones de crash abordan casos extremos alrededor de URIs `nostrconnect://` inválidos e interacciones de pantalla de permisos.

**nak v0.17.3** - El [último lanzamiento](https://github.com/fiatjaf/nak/releases/tag/v0.17.3) de la herramienta de línea de comandos Nostr restringe builds LMDB a Linux, corrigiendo problemas de compilación multiplataforma.

**Aegis v0.3.4** - El firmador Nostr multiplataforma [añade soporte](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.4) para el esquema URI `nostrsigner:` definido en [NIP-55](/es/topics/nip-55/), coincidiendo con el flujo de conexión de Amber. Los datos de relay local ahora pueden ser importados y exportados para respaldo, y el lanzamiento incluye correcciones de errores para errores de socket de relay y mejoras de UI para la interfaz de relay local.

## Cambios notables de código y documentación {#notable-code-and-documentation-changes}

*Estos son pull requests abiertos y trabajo en etapa temprana, perfectos para obtener retroalimentación antes de fusionarse. Si algo te llama la atención, ¡considera revisar o comentar!*

### Damus (iOS) {#damus-ios}

[Persistencia de lista de silenciados](https://github.com/damus-io/damus/pull/3469) corrige un problema donde las listas de silenciados se borraban en inicio frío. La corrección añade guardas para prevenir sobrescrituras accidentales durante la inicialización de la app. [Temporización de stream de perfil](https://github.com/damus-io/damus/pull/3457) elimina un retraso de ~1 segundo antes de que los perfiles en caché aparecieran. Anteriormente, las vistas esperaban a que las tareas de suscripción reiniciaran; ahora `streamProfile()` inmediatamente devuelve datos en caché de NostrDB, eliminando la ventana donde pubkeys abreviadas e imágenes placeholder se mostraban.

### White Noise (Mensajería Encriptada) {#white-noise-encrypted-messaging}

[Streaming de mensajes en tiempo real](https://github.com/marmot-protocol/whitenoise/pull/919) reemplaza el mecanismo de polling anterior con una arquitectura basada en streams. El nuevo `ChatStreamNotifier` consume el stream de mensajes del SDK Rust directamente, manteniendo orden cronológico y manejando actualizaciones incrementales eficientemente. Las pruebas mostraron mejora significativa en capacidad de respuesta. Una [API de lista de chat](https://github.com/marmot-protocol/whitenoise/pull/921) añade `get_chat_list` para recuperar resúmenes de conversaciones, y una [corrección de ordenamiento estable](https://github.com/marmot-protocol/whitenoise/pull/905) previene loops de reordenamiento de mensajes usando `createdAt` con ID de mensaje como desempate.

### NDK (Librería) {#ndk-library}

Dos pull requests entregaron mejoras dramáticas de rendimiento de caché. [PR #371](https://github.com/nostr-dev-kit/ndk/pull/371) corrigió un bug donde eventos leídos de caché SQLite se escribían inmediatamente de vuelta, causando 100% de escrituras duplicadas al iniciar la app. La corrección añade una guarda `fromCache` e implementa verificación de duplicados O(1) vía un Set en memoria. Para conjuntos de resultados pequeños (<100 eventos), la transferencia JSON directa reemplaza la sobrecarga de codificación binaria. [PR #372](https://github.com/nostr-dev-kit/ndk/pull/372) eliminó llamadas innecesarias a `seenEvent` para eventos en caché. La búsqueda en caché LRU costaba 0.24-0.64ms por evento; para 5,700 eventos en caché, esto añadía ~1.4 segundos de sobrecarga. Resultado: las consultas de caché bajaron de ~3,690ms a ~22ms (162x más rápido).

### rust-nostr (Librería) {#rust-nostr-library}

[Soporte de REQ multi-filtro](https://github.com/rust-nostr/nostr/pull/1176) fue restaurado después de ser eliminado en un refactor previo. El SDK nuevamente acepta `Vec<Filter>` para solicitudes de suscripción, permitiendo consultas eficientes que combinan múltiples condiciones de filtro con lógica OR. [Procedencia de relay](https://github.com/rust-nostr/nostr/pull/1156) fue añadida a métodos `stream_events*`, así que cada evento en stream ahora incluye el `RelayUrl` de donde vino y un `Result` indicando éxito o fallo, útil para rastrear confiabilidad de relay y depurar problemas de conexión. Una [corrección de seguridad](https://github.com/rust-nostr/nostr/pull/1179) eliminó la dependencia `url-fork` siguiendo RUSTSEC-2024-0421, eliminando una vulnerabilidad conocida.

### Applesauce (Librería) {#applesauce-library}

La librería TypeScript que potencia [noStrudel](https://github.com/hzrd149/nostrudel) vio desarrollo significativo esta semana. Nuevos modelos incluyen un [sistema de reacciones](https://github.com/hzrd149/applesauce) y casting de grupos de usuarios. La funcionalidad de billetera se expandió con soporte NIP-60, una pestaña de envío, y herramientas mejoradas de recuperación de tokens. Una nueva propiedad `user.directMessageRelays$` expone configuración de relay DM. Todas las acciones fueron refactorizadas para usar interfaces async (eliminando generadores async), y correcciones de bugs abordaron restauración de contenido encriptado y casos extremos de filtros de eventos basados en tiempo.

### Tenex (Agentes IA) {#tenex-ai-agents}

El [sistema de coordinación multi-agente](https://github.com/tenex-chat/tenex) construido sobre Nostr introdujo arquitectura RAL (Request-Action-Lifecycle) en [cinco PRs fusionados](https://github.com/pablof7z/tenex/pull/38). RAL permite a los agentes pausar cuando delegan tareas y reanudar cuando llegan resultados, con persistencia de estado en alcance de conversación. Las herramientas de delegación (`delegate`, `ask`, `delegate_followup`, `delegate_external`) ahora publican eventos Nostr y retornan señales de parada en lugar de bloquear. El refactor incluye migración a AI SDK v6, infraestructura de testing VCR para grabación determinística de interacciones LLM, y soporte de imágenes multimodal.

---

Eso es todo por esta semana. ¿Construyendo algo? ¿Tienes noticias para compartir? ¿Quieres que cubramos tu proyecto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contáctanos vía NIP-17 DM</a> o encuéntranos en Nostr.
