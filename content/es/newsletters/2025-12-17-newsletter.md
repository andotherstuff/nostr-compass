---
title: 'Nostr Compass #1'
date: 2025-12-17
publishDate: 2025-12-15
draft: false
type: newsletters
translationOf: /en/newsletters/2025-12-17-newsletter.md
translationDate: 2025-12-26
---

Bienvenido a Nostr Compass, un boletín semanal dedicado al ecosistema del protocolo Nostr. Nuestra misión es mantener informados a desarrolladores, operadores de relays y constructores sobre desarrollos importantes en toda la red. Documentamos la evolución del protocolo con precisión técnica, neutralidad y profundidad, cubriendo desde propuestas de NIP hasta lanzamientos de clientes y mejores prácticas de implementación.

Nostr Compass está inspirado en [Bitcoin Optech](https://bitcoinops.org/), cuyo trabajo dedicado durante años avanzando el conocimiento técnico de Bitcoin estableció el estándar para boletines enfocados en protocolos. Estamos agradecidos por su ejemplo y esperamos aportar el mismo rigor al ecosistema Nostr.

Este número inaugural establece nuestro formato semanal. Cada miércoles te traeremos actualizaciones de NIP, notas de lanzamiento, destacados de desarrollo y guías técnicas. Ya sea que estés construyendo un cliente, operando un relay o contribuyendo al protocolo, Nostr Compass pretende ser tu fuente confiable sobre lo que está sucediendo en el ecosistema.

## ¿Qué es Nostr?

*Dado que este es nuestro primer número, comenzamos con una introducción sobre cómo funciona Nostr. Los lectores habituales pueden [saltar adelante](#noticias).*

Nostr (Notes and Other Stuff Transmitted by Relays) es un protocolo descentralizado para redes sociales y mensajería. A diferencia de las plataformas tradicionales, Nostr no tiene servidor central, ninguna empresa lo controla y no tiene un punto único de fallo. Los usuarios poseen su identidad a través de pares de claves criptográficas, y el contenido fluye a través de servidores relay independientes que cualquiera puede ejecutar.

**Cómo funciona:** Los usuarios generan un par de claves (una clave privada llamada nsec y una clave pública llamada npub). La clave privada firma mensajes llamados "eventos", y la clave pública sirve como tu identidad. Los eventos se envían a relays, que los almacenan y reenvían a otros usuarios. Debido a que controlas tus claves, puedes cambiar entre clientes o relays sin perder tu identidad o seguidores.

**Por qué importa:** Nostr proporciona resistencia a la censura a través de la diversidad de relays (si un relay te banea, otros aún pueden servir tu contenido), portabilidad (tu identidad funciona en cualquier aplicación Nostr) e interoperabilidad (todos los clientes Nostr hablan el mismo protocolo). No hay algoritmo decidiendo qué ves, sin anuncios y sin recolección de datos.

**El ecosistema hoy:** Nostr soporta microblogging (como Twitter/X), contenido largo (como Medium), mensajes directos, mercados, streaming en vivo y más. Los clientes incluyen Damus (iOS), Amethyst (Android), Primal, Coracle y docenas más. La integración con Lightning Network permite pagos instantáneos a través de "zaps". El protocolo continúa evolucionando a través de NIPs (Nostr Implementation Possibilities), especificaciones impulsadas por la comunidad que extienden la funcionalidad.

## Noticias {#news}

**NIP-BE Fusionado: Soporte para Bluetooth Low Energy** - Una nueva capacidad significativa [aterrizó en el protocolo](https://github.com/nostr-protocol/nips/pull/1979). [NIP-BE](/es/topics/nip-be/) especifica cómo las aplicaciones Nostr pueden comunicarse y sincronizarse sobre Bluetooth Low Energy. Esto permite que las aplicaciones capaces de funcionar sin conexión sincronicen datos entre dispositivos cercanos sin conectividad a internet. La especificación adapta los patrones de relay WebSocket a las restricciones de BLE, usando compresión DEFLATE y mensajería fragmentada para manejar los tamaños MTU pequeños de BLE (20-256 bytes). Los dispositivos negocian roles basándose en la comparación de UUID, con el UUID más alto convirtiéndose en el servidor GATT.

**MIP-05: Notificaciones Push que Preservan la Privacidad** - El [Protocolo Marmot](/es/topics/marmot/) publicó [MIP-05](/es/topics/mip-05/) ([especificación](https://github.com/marmot-protocol/mips/blob/main/mip-05.md)), una especificación para notificaciones push que mantienen la privacidad. Los sistemas push tradicionales requieren que los servidores conozcan los tokens de dispositivo e identidades de usuario; MIP-05 resuelve esto encriptando tokens de dispositivo con ECDH+HKDF y ChaCha20-Poly1305, usando claves efímeras para prevenir la correlación. Un protocolo gossip de tres eventos (kinds 447-449) sincroniza tokens encriptados entre miembros del grupo, y las notificaciones usan gift wrapping de [NIP-59](/es/topics/nip-59/) con tokens señuelo para ocultar tamaños de grupo. Esto permite a WhiteNoise y otros clientes Marmot entregar notificaciones oportunas sin comprometer la privacidad del usuario.

**Blossom BUD-10: Nuevo Esquema URI** - El protocolo de medios [Blossom](/es/topics/blossom/) está obteniendo un esquema URI personalizado vía [BUD-10](/es/topics/bud-10/) ([especificación](https://github.com/hzrd149/blossom/blob/master/buds/10.md)). El nuevo formato `blossom:<sha256>.ext` incorpora hash de archivo, extensión, tamaño, múltiples hints de servidor y pubkeys de autor para descubrimiento de servidor [BUD-03](/es/topics/bud-03/). Esto hace que los enlaces de blob sean más resilientes que las URLs HTTP estáticas al permitir fallback automático entre servidores.

**Actualizaciones del Mercado Shopstr** - El mercado nativo de Nostr [implementó Nostr Wallet Connect](https://github.com/shopstr-eng/shopstr/pull/202) ([NIP-47](/es/topics/nip-47/)) para pagos, [añadió expiración de listados](https://github.com/shopstr-eng/shopstr/pull/203) usando [NIP-40](/es/topics/nip-40/), e introdujo [códigos de descuento](https://github.com/shopstr-eng/shopstr/pull/210) para vendedores.

## Actualizaciones de NIP {#nip-updates}

Cambios recientes al [repositorio de NIPs](https://github.com/nostr-protocol/nips):

**Nuevos NIPs:**
- **[NIP-BE](/es/topics/nip-be/)** - Mensajería Bluetooth Low Energy y sincronización de dispositivos ([#1979](https://github.com/nostr-protocol/nips/pull/1979))
- **[NIP-63](/es/topics/nip-63/)** - Estándar de Paywall/Contenido Premium para manejar contenido con acceso restringido dentro del protocolo ([#2156](https://github.com/nostr-protocol/nips/pull/2156))

**Cambios Significativos:**
- **[NIP-24](/es/topics/nip-24/)** - Añadido array opcional `languages` a metadatos de usuario Kind 0, permitiendo a los usuarios especificar múltiples idiomas preferidos usando etiquetas IETF BCP 47 para mejor descubrimiento de contenido y coincidencia de relay ([#2159](https://github.com/nostr-protocol/nips/pull/2159))
- **[NIP-69](/es/topics/nip-69/)** - Añadido soporte de expiración de órdenes para trading P2P con etiquetas `expires_at` y `expiration` ([#2118](https://github.com/nostr-protocol/nips/pull/2118))
- **[NIP-59](/es/topics/nip-59/)** - Los eventos gift wrap ahora pueden ser eliminados vía solicitudes NIP-09/NIP-62 ([#2131](https://github.com/nostr-protocol/nips/pull/2131))
- **[NIP-51](/es/topics/nip-51/)** - Eliminadas etiquetas de hashtag y URL de marcadores genéricos; hashtags ahora usan kind 30015 ([#2133](https://github.com/nostr-protocol/nips/pull/2133))
- **[NIP-18](/es/topics/nip-18/)** - Mejorados los reposts genéricos para eventos reemplazables con soporte de etiqueta `a` ([#2132](https://github.com/nostr-protocol/nips/pull/2132))
- **[NIP-17](/es/topics/nip-17/)** - Redacción refinada y añadido soporte de reacción kind 7 a DMs ([#2098](https://github.com/nostr-protocol/nips/pull/2098))
- **[NIP-11](/es/topics/nip-11/)** - Añadido campo `self` para identificación de clave pública del relay ([#1764](https://github.com/nostr-protocol/nips/pull/1764))

## Profundización en NIP: NIP-01 y NIP-19 {#nip-deep-dive-nip-01-and-nip-19}

Para este número inaugural, cubrimos dos NIPs fundamentales que todo desarrollador de Nostr debería entender. Consulta nuestras páginas de temas para [NIP-01](/es/topics/nip-01/) y [NIP-19](/es/topics/nip-19/).

### NIP-01: Protocolo Básico

[NIP-01](/es/topics/nip-01/) define el protocolo central. Todo en Nostr se construye sobre esta especificación.

**Los eventos** son el único tipo de objeto. Cada evento contiene:
- `id`: Hash SHA256 del evento serializado (el identificador único del evento)
- `pubkey`: La clave pública del creador (hex de 32 bytes, secp256k1)
- `created_at`: Marca de tiempo Unix
- `kind`: Entero que categoriza el tipo de evento
- `tags`: Array de arrays para metadatos
- `content`: La carga útil (la interpretación depende del kind)
- `sig`: Firma Schnorr probando que la pubkey creó este evento

**Los kinds** determinan cómo los relays almacenan eventos:
- Eventos regulares (1, 2, 4-44, 1000-9999): Almacenados normalmente, todas las versiones se mantienen
- Eventos reemplazables (0, 3, 10000-19999): Solo se mantiene el más reciente por pubkey
- Eventos efímeros (20000-29999): No almacenados, solo reenviados a suscriptores
- Eventos direccionables (30000-39999): Más reciente por combinación de pubkey + kind + etiqueta `d`

Kind 0 son metadatos de usuario (perfil), kind 1 es una nota de texto (la publicación básica), kind 3 es la lista de seguidos.

**Kind 1: Notas de Texto** son el corazón del Nostr social. Un evento kind 1 es una publicación corta, similar a un tweet. El campo `content` contiene el texto del mensaje (texto plano, aunque los clientes a menudo renderizan markdown). Las etiquetas permiten respuestas, menciones y referencias:

```json
{
  "id": "<32-byte-hex>",
  "pubkey": "<32-byte-hex>",
  "created_at": 1734480000,
  "kind": 1,
  "content": "¡Hola Nostr! Mira el trabajo de @jb55 en Damus.",
  "tags": [
    ["e", "<replied-to-event-id>", "wss://relay.example.com", "reply"],
    ["p", "<jb55-pubkey>"]
  ],
  "sig": "<64-byte-hex>"
}
```

La etiqueta `e` con marcador "reply" indica que esto es una respuesta (ver [NIP-10](/es/topics/nip-10/) para convenciones de hilos). La etiqueta `p` menciona a un usuario, permitiendo a los clientes notificarle y renderizar su nombre en lugar de la pubkey cruda. Los clientes obtienen el evento kind 0 del usuario mencionado para obtener su nombre de pantalla e imagen.

Para construir una línea de tiempo, un cliente se suscribe a eventos kind 1 de pubkeys seguidas: `["REQ", "feed", {"kinds": [1], "authors": ["<pubkey1>", "<pubkey2>", ...], "limit": 50}]`. El relay devuelve notas coincidentes, y el cliente las renderiza cronológicamente.

**Los eventos direccionables** (30000-39999) funcionan como eventos reemplazables pero usan una etiqueta `d` como identificador adicional. El relay mantiene solo la última versión de cada combinación pubkey + kind + d-tag. Esto permite artículos editables, listados de productos, o cualquier caso donde necesites múltiples elementos reemplazables por usuario.

**Las etiquetas** son arrays donde el primer elemento es el nombre de la etiqueta. Las etiquetas estándar de una sola letra (`e`, `p`, `a`, `d`, `t`) son indexadas por relays para consultas eficientes. Por ejemplo, `["e", "<event-id>"]` referencia otro evento, `["p", "<pubkey>"]` referencia un usuario.

**Comunicación Cliente-Relay** usa conexiones WebSocket con arrays JSON como mensajes. El primer elemento identifica el tipo de mensaje.

De cliente a relay:
- `["EVENT", <event>]` - Publica un evento al relay
- `["REQ", <sub-id>, <filter>, ...]` - Suscribirse a eventos que coincidan con el/los filtro(s)
- `["CLOSE", <sub-id>]` - Terminar una suscripción

De relay a cliente:
- `["EVENT", <sub-id>, <event>]` - Entrega un evento que coincide con tu suscripción
- `["EOSE", <sub-id>]` - "Fin de eventos almacenados" - el relay ha enviado todos los coincidentes históricos y ahora solo enviará nuevos eventos conforme lleguen
- `["OK", <event-id>, <true|false>, <message>]` - Reconoce si un evento fue aceptado o rechazado (y por qué)
- `["NOTICE", <message>]` - Mensaje legible por humanos del relay

El flujo de suscripción: el cliente envía `REQ` con un ID de suscripción y filtro, el relay responde con mensajes `EVENT` coincidentes, luego envía `EOSE` para señalar que está al día con el historial. Después de `EOSE`, cualquier nuevo mensaje `EVENT` es en tiempo real. El cliente envía `CLOSE` cuando termina.

**Los filtros** especifican qué eventos recuperar. Un objeto filtro puede incluir: `ids` (IDs de evento), `authors` (pubkeys), `kinds` (tipos de evento), `#e`/`#p`/`#t` (valores de etiqueta), `since`/`until` (marcas de tiempo), y `limit` (máximo de resultados). Todas las condiciones dentro de un filtro usan lógica AND. Puedes incluir múltiples filtros en un `REQ`, y se combinan con lógica OR - útil para obtener diferentes tipos de evento en una suscripción.

### NIP-19: Identificadores Codificados en Bech32

[NIP-19](/es/topics/nip-19/) define los formatos amigables para humanos que ves en todas partes en Nostr: npub, nsec, note, y más. Estos no se usan en el protocolo mismo (que usa hex), pero son esenciales para compartir y mostrar.

**¿Por qué bech32?** Las claves hex crudas son propensas a errores al copiar y difíciles de distinguir visualmente. La codificación bech32 añade un prefijo legible y suma de verificación. Puedes distinguir inmediatamente un `npub` (clave pública) de un `nsec` (clave privada) o `note` (ID de evento).

**Formatos básicos** codifican valores crudos de 32 bytes:
- `npub` - Clave pública (tu identidad, segura para compartir)
- `nsec` - Clave privada (mantener en secreto, usada para firmar)
- `note` - ID de evento (referencia un evento específico)

Ejemplo: La pubkey hex `3bf0c63fcb93463407af97a5e5ee64fa883d107ef9e558472c4eb9aaaefa459d` se convierte en `npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`.

**Identificadores compartibles** incluyen metadatos usando codificación TLV (Type-Length-Value):
- `nprofile` - Perfil con hints de relay (ayuda a los clientes a encontrar al usuario)
- `nevent` - Evento con hints de relay, pubkey de autor y kind
- `naddr` - Referencia de evento direccionable (pubkey + kind + d-tag + relays)

Estos resuelven un problema clave: si alguien comparte un ID de nota, ¿cómo sabes qué relay lo tiene? Un `nevent` agrupa el ID de evento con relays sugeridos, haciendo más confiable compartir.

**Importante:** Nunca uses formatos bech32 en el protocolo mismo. Los eventos, mensajes de relay y respuestas NIP-05 deben usar hex. Bech32 es puramente para interfaces humanas: visualización, copiar/pegar, códigos QR y URLs.

## Lanzamientos {#releases}

**Amber v4.0.4** - La aplicación firmadora de Android corrige un NullPointerException, mejora el rendimiento en la pantalla de actividad y añade traducciones para algunos tipos de evento. El lanzamiento anterior v4.0.3 añadió UI renovada de encriptación/desencriptación, exportación/importación de cuentas, manejo de relay por cuenta, soporte de ping bunker y reporte de errores. [Lanzamiento](https://github.com/greenart7c3/Amber/releases/tag/v4.0.4)

**Coracle 0.6.28** - Lanzamiento de corrección de errores para el cliente web. Corregidos feeds de temas, manejo de imágenes cuando imgproxy está deshabilitado, y linkificación de fuentes de resaltado que no son enlaces. [Lanzamiento](https://github.com/coracle-social/coracle/releases/tag/0.6.28)

**Flotilla v1.6.2** - El cliente de comunidades estilo Discord corrige scroll modal y problemas de estilo. Lanzamientos anteriores en este ciclo añadieron insignias y sonidos opcionales para notificaciones, renderizado de enlaces mejorado, escaneo de códigos QR para enlaces de invitación, y configuración simplificada de billetera. [Lanzamiento](https://github.com/coracle-social/flotilla/releases/tag/1.6.2)

**nak v0.17.2** - La herramienta de línea de comandos Nostr añadió un nuevo comando `nip` para búsqueda rápida de referencia NIP, más correcciones para manejo de repositorio git y procesamiento de eventos stdin. [Lanzamiento](https://github.com/fiatjaf/nak/releases/tag/v0.17.2)

**White Noise v0.2.1** - Lanzamiento mayor para la aplicación de mensajería encriptada basada en MLS añadiendo compartir imágenes vía Blossom, sincronización en segundo plano, notificaciones push, localización en 8 idiomas, y gestión de miembros de grupo. [Lanzamiento](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**Amethyst v1.04.2** - Lanzamiento con nuevas características introduciendo listas/packs de seguidos, nuevos filtros de línea de tiempo, galería de imágenes, y compresión de video H.265 (archivos 50% más pequeños). Migración completa a Kotlin Multiplatform. [Lanzamiento](https://github.com/vitorpamplona/amethyst/releases/tag/v1.04.2)

**Mostro v0.15.5** - Actualización de la plataforma de trading P2P con soporte de expiración de órdenes NIP-69 y respuestas mejoradas de historial de operaciones. [Lanzamiento](https://github.com/MostroP2P/mostro/releases/tag/v0.15.5)

**Nosflare v8.9.26** - Relay Nostr serverless construido en infraestructura Cloudflare. Este lanzamiento entrega un hotfix crítico que aborda un error que podía causar fallos de websocket, asegurando conexiones más estables para usuarios y aplicaciones que dependen del relay. [Lanzamiento](https://github.com/Spl0itable/nosflare/releases/tag/v8.9.26)

**Noscall v0.4.1** - Aplicación de llamadas de audio y video seguras basada en Nostr. Este lanzamiento mejora la UI pop-up en la página Me y corrige varios problemas conocidos, resultando en mejor estabilidad y confiabilidad de llamadas. [Lanzamiento](https://github.com/sanah9/noscall/releases/tag/v0.4.1-release)

**Gitplaza v0.25.0** - Cliente de escritorio Nostr enfocado en actividad relacionada con Git. Este lanzamiento introduce un filtro de kind avanzado para el feed del inbox, incluye zaps regulares en filtros, y simplifica el formato de texto de pestañas. Las mejoras de rendimiento optimizan la carga del árbol de comentarios, reducen consultas innecesarias a base de datos, y usan ramas de comentarios en caché para visualización más rápida. [Lanzamiento](https://codeberg.org/dluvian/gitplaza/releases/tag/v0.25.0)

## Cambios notables de código y documentación {#notable-code-and-documentation-changes}

### Damus (iOS) {#damus-ios}

Enfoque en estabilidad con correcciones de crashes y UI: [corrección de salto de cursor](https://github.com/damus-io/damus/pull/3377) para la vista de composición, [rediseño de interfaz NostrDB](https://github.com/damus-io/damus/pull/3366) usando tipos `~Copyable` de Swift para seguridad de transacciones, [estabilidad de UI de hilos](https://github.com/damus-io/damus/pull/3341) corrigiendo reinstanciación de barra de acciones, [congelación de lista de silenciados](https://github.com/damus-io/damus/pull/3346) por ciclos de AttributeGraph, y [crash de perfil](https://github.com/damus-io/damus/pull/3334) por limpieza de transacciones entre hilos. También añadió directrices [AGENTS.md](https://github.com/damus-io/damus/pull/3293) para agentes de código IA.

### Notedeck (Escritorio/Móvil) {#notedeck-desktop-mobile}

[Almacenamiento seguro de claves](https://github.com/damus-io/notedeck/pull/1191) mueve nsec al almacén seguro del SO con migración automática. [Filtrado de notas futuras](https://github.com/damus-io/notedeck/pull/1201) oculta eventos fechados 24+ horas adelante (anti-spam). [Copia de nevent](https://github.com/damus-io/notedeck/pull/1183) ahora incluye hints de relay. También: [adición rápida de columna de perfil](https://github.com/damus-io/notedeck/pull/1212), [navegación por teclado](https://github.com/damus-io/notedeck/pull/1208), [optimización de carga de medios](https://github.com/damus-io/notedeck/pull/1210).

### Amethyst (Android) {#amethyst-android}

Soporte de [firma remota NIP-46](https://github.com/vitorpamplona/amethyst/pull/1555) para Nostr Connect. [Organización de marcadores](https://github.com/vitorpamplona/amethyst/pull/1586) con gestión de listas públicas/privadas. [Corrección de compatibilidad strfry](https://github.com/vitorpamplona/amethyst/pull/1596) para casos extremos de análisis de info de relay.

### Primal (Android) {#primal-android}

[Deep links de Nostr Connect](https://github.com/PrimalHQ/primal-android-app/pull/788) para URLs `nostrconnect://`. [Inicio de sesión remoto](https://github.com/PrimalHQ/primal-android-app/pull/787) vía escaneo QR para conexiones bunker. [Corrección de condición de carrera de conexión](https://github.com/PrimalHQ/primal-android-app/pull/783).

### White Noise (Mensajería Encriptada) {#white-noise-encrypted-messaging}

[Corrección de retención de datos de app](https://github.com/marmot-protocol/whitenoise/pull/890) desactiva auto-backup de Android para privacidad. [Comportamiento de scroll de chat](https://github.com/marmot-protocol/whitenoise/pull/861) preserva la posición al leer historial.

### Zeus (Billetera Lightning) {#zeus-lightning-wallet}

[Pagos paralelos NIP-47](https://github.com/ZeusLN/zeus/pull/3407) para mayor rendimiento en zaps por lotes.

## Mejores Prácticas para Desarrolladores

**Valida Eventos Auth de Forma Defensiva** - go-nostr corrigió un [panic en validación NIP-42](https://github.com/nbd-wtf/go-nostr/pull/182) cuando faltaba la etiqueta relay. Siempre verifica las etiquetas requeridas antes de acceder a ellas, incluso en flujos auth donde esperas eventos bien formados.

**Limita Tasa por Estado de Autenticación** - khatru añadió [limitación de tasa basada en NIP-42](https://github.com/fiatjaf/khatru/pull/57), permitiendo a los relays aplicar diferentes límites para conexiones autenticadas vs anónimas. Considera límites escalonados basados en estado auth en lugar de restricciones generales.

**Usa Paginación por Cursor para Listas** - Blossom [reemplazó paginación basada en fecha](https://github.com/hzrd149/blossom/pull/65) con paginación basada en cursor en el endpoint `/list`. La paginación basada en fecha falla cuando items comparten timestamps; los cursores proporcionan iteración confiable.

**Validación de Esquema para Tipos de Evento** - El proyecto [nostrability/schemata](https://github.com/nostrability/schemata) proporciona esquemas JSON para validar eventos compatibles con NIP. Considera integrar validación de esquema en desarrollo para detectar eventos malformados antes de que lleguen a los relays.

---

Eso es todo por esta semana. ¿Construyendo algo? ¿Tienes noticias para compartir? ¿Quieres que cubramos tu proyecto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contáctanos vía NIP-17 DM</a> o encuéntranos en Nostr.
