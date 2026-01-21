---
title: 'Nostr Compass #6'
date: 2026-01-21
publishDate: 2026-01-21
draft: false
type: newsletters
---

Bienvenido de nuevo a Nostr Compass, tu guía semanal sobre Nostr.

**Esta semana:** Bitchat reemplaza C Tor con la implementación Rust Arti para mejor confiabilidad y rendimiento. nostrdb-rs obtiene consultas de plegado en streaming que permiten operaciones de base de datos sin asignación de memoria. Listr recibe una refactorización mayor con migración a NDK 3 beta y mantenimiento asistido por IA después de un año de inactividad. Zeus envía 17 PRs fusionados enfocados en correcciones de [NIP-47](/es/topics/nip-47/) (Nostr Wallet Connect para control remoto de Lightning) y mejoras de Cashu, mientras que Primal Android añade flujos de respaldo de billetera y soporte de [NIP-92](/es/topics/nip-92/) (dimensiones de medios para proporciones de aspecto adecuadas). Un nuevo borrador de NIP propone [Aserciones de Confianza de Relays](/es/topics/trusted-relay-assertions/) para puntuación estandarizada de confianza de relays.

## Noticias

### Bitchat Migra a Rust Arti para Soporte de Tor

Bitchat ha migrado de C Tor a [Arti](https://gitlab.torproject.org/tpo/core/arti), la implementación en Rust del protocolo Tor. El [PR #958](https://github.com/permissionlesstech/bitchat/pull/958) elimina la dependencia de C Tor e integra Arti, aportando garantías de seguridad de memoria y mejor confiabilidad. El cambio elimina intentos de despertar inactivos que causaban reinicios del servicio en primer plano, un problema de larga data con la implementación en C.

**Lo que esto significa para los usuarios:** Mensajería cifrada más estable con menos desconexiones, especialmente en dispositivos móviles. La implementación en Rust reduce riesgos de fallas y drenaje de batería por intentos constantes de reconexión.

Arti es una reescritura completa de Tor en Rust, desarrollada por el Proyecto Tor para proporcionar mejor seguridad a través de la seguridad de memoria y facilitar la integración en aplicaciones. Para Bitchat, las propiedades de seguridad de memoria reducen la superficie de ataque al manejar mensajes cifrados y conexiones de relay. La migración sigue la reciente [auditoría de seguridad Cure53](/es/newsletters/2026-01-13-newsletter/#bitchat-completes-cure53-security-audit) del equipo (cubierta en Newsletter #5), continuando sus mejoras de seguridad.

El PR también introduce cobertura de pruebas integral para ChatViewModel y BLEService, elimina código muerto y estabiliza la suite de pruebas. Las mejoras de confiabilidad de la malla Bluetooth Low Energy acompañan los cambios de Tor, abordando fallos en transferencias grandes. Juntos, estos cambios mejoran la resiliencia de Bitchat para escenarios de red en malla fuera de línea donde Tor proporciona conectividad a internet junto con comunicación BLE local.


### Listr Revitalizado con Mantenimiento Potenciado por IA

JeffG anunció una refactorización mayor de [Listr](https://github.com/erskingardner/listr), la aplicación de gestión de listas Nostr disponible en [listr.lol](https://listr.lol), después de que el proyecto había estado inactivo por más de un año. Usando asistencia de IA, completó una actualización integral incluyendo migración a [NDK](https://github.com/nostr-dev-kit/ndk) 3 beta, actualizaciones a las últimas versiones de Svelte y Vite, y todas las dependencias actualizadas. La refactorización añade soporte de primera clase para seguir packs, implementa paginación para listas que exceden 50 elementos, y corrige numerosos errores que se habían acumulado durante el período inactivo.

**Lo que esto significa para los usuarios:** Listr está de vuelta en línea con rendimiento mejorado y nuevas características para gestionar listas de seguimiento, colecciones de contenido y curación de temas. La corrección de paginación hace que las listas grandes sean realmente utilizables.

JeffG señaló que sin asistencia de IA, este trabajo de mantenimiento probablemente nunca habría ocurrido, evitando que el proyecto fuera abandonado. Listr permite la curación de contenido en Nostr, permitiendo a los usuarios crear, gestionar y compartir listas de perfiles, temas y recursos. La actualización mantiene la aplicación compatible con los estándares Nostr actuales y las expectativas de los clientes a medida que la gestión de listas se vuelve más central para el descubrimiento de contenido en el protocolo.


## Actualizaciones de NIP

Cambios recientes en el [repositorio de NIPs](https://github.com/nostr-protocol/nips):

**Fusionados:**

- **[NIP-29](/es/topics/nip-29/)** (Grupos basados en relay) - Aclaración de Clave de Relay ([#2190](https://github.com/nostr-protocol/nips/pull/2190) - fusionado) aclara que la clave de relay es la URL del relay en sí, no una pubkey. La especificación ahora establece explícitamente "La clave de relay es la URL WebSocket del relay (ej., wss://groups.example.com)" para evitar confusión. Esto afecta cómo los clientes identifican qué relay hospeda un grupo dado, asegurando que los grupos sean apropiadamente atribuidos a sus relays de hospedaje.

**PRs Abiertos y Discusiones:**

- **Aserciones de Confianza de Relays** - Un borrador de NIP propone estandarizar la puntuación de confianza de relays a través de eventos kind 30385 que contienen puntuaciones de confianza (0-100) computadas a partir de métricas de [NIP-66](/es/topics/nip-66/) (descubrimiento y monitoreo de relays), reputación del operador e informes de usuarios. La especificación divide la confianza en componentes de confiabilidad (tiempo de actividad, latencia), calidad (TLS, documentación, verificación del operador) y accesibilidad (jurisdicción, barreras, riesgo de vigilancia). La verificación del operador incluye firmas criptográficas vía [NIP-11](/es/topics/nip-11/) (documentos de información de relay), registros DNS TXT y archivos .well-known. Los usuarios declaran proveedores de aserciones confiables vía eventos kind 10385, permitiendo a los clientes consultar múltiples proveedores para perspectivas diversas. La propuesta complementa el descubrimiento de [NIP-66](/es/topics/nip-66/) con evaluación, ayudando a [NIP-46](/es/topics/nip-46/) (firma remota/Nostr Connect) a evaluar la confiabilidad del relay en URIs de conexión.

- **Criptografía Post-Cuántica** - El [PR #2185](https://github.com/nostr-protocol/nips/pull/2185) (abierto) continúa evolucionando desde que el [Newsletter #5](/es/newsletters/2026-01-13-newsletter/#nip-updates) introdujo la propuesta de algoritmos resistentes a computación cuántica. La discusión de esta semana se enfocó en detalles de implementación para cripto-agilidad: cómo los clientes manejan firmas duales durante la migración, compatibilidad hacia atrás para clientes antiguos e implicaciones de rendimiento de firmas resistentes a cuántica más grandes. Los contribuidores debatieron si mandar solo ML-DSA-44 o soportar múltiples algoritmos (ML-DSA-44, Falcon-512, Dilithium) para flexibilidad. El consenso se inclina hacia un enfoque por fases: firmas cuánticas opcionales inicialmente, volviéndose obligatorias solo después de soporte amplio del cliente y emergencia de amenaza cuántica real.


## Análisis Profundo de NIP: NIP-11 y NIP-66

Esta semana examinamos dos NIPs que trabajan juntos para permitir el descubrimiento y evaluación de relays: NIP-11 define cómo los relays se describen a sí mismos, y NIP-66 estandariza cómo medimos el comportamiento del relay. Juntos forman la fundación para sistemas de evaluación de confianza de relays.

### [NIP-11](/es/topics/nip-11/): Documento de Información de Relay

[NIP-11](https://github.com/nostr-protocol/nips/blob/master/11.md) define un documento JSON que los relays sirven sobre HTTP para describir sus capacidades, políticas e información del operador. Cuando un cliente se conecta a `wss://relay.example.com`, puede obtener `https://relay.example.com` (reemplazando `wss://` con `https://`) para recuperar el documento de información del relay.

El documento usa negociación de contenido HTTP estándar con el encabezado `Accept: application/nostr+json`. Esto permite a los relays servir su sitio web normal a navegadores mientras proporcionan metadatos legibles por máquina a clientes Nostr. La respuesta incluye nombre y versión del software del relay, información de contacto del operador (pubkey, email, contacto alternativo), NIPs soportados y parámetros operacionales como requisitos de pago o restricciones de contenido.

Importante, los documentos NIP-11 básicos son JSON sin firmar servidos sobre HTTPS, dependiendo únicamente de certificados TLS para autenticidad. Esto significa que cualquiera que controle el servidor web del relay puede modificar el documento, haciendo que las afirmaciones del operador sean inverificables. La propuesta de Aserciones de Confianza de Relays aborda esta brecha introduciendo atestaciones firmadas a través del campo `self` pubkey del relay, permitiendo prueba criptográfica de identidad del operador similar a cómo los relays usan eventos firmados para mecanismos de autenticación.

```json
{
  "name": "relay.example.com",
  "description": "Un relay público de propósito general",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "contact": "admin@example.com",
  "supported_nips": [1, 2, 4, 9, 11, 12, 16, 20, 22],
  "software": "git+https://github.com/relay/relay.git",
  "version": "1.2.3",
  "limitation": {
    "max_message_length": 16384,
    "max_subscriptions": 20,
    "max_filters": 100,
    "max_limit": 5000,
    "max_subid_length": 100,
    "min_prefix": 4,
    "max_event_tags": 2000,
    "max_content_length": 8196,
    "min_pow_difficulty": 0,
    "auth_required": false,
    "payment_required": false
  },
  "payments_url": "https://relay.example.com/payments",
  "fees": {
    "admission": [{"amount": 5000, "unit": "msats"}],
    "subscription": [{"amount": 1000, "unit": "msats", "period": 2592000}],
    "publication": []
  }
}
```

El objeto `limitation` dice a los clientes qué restricciones impone el relay. `max_message_length` limita el tamaño del marco WebSocket, `max_subscriptions` limita las suscripciones REQ concurrentes por conexión, `max_filters` limita filtros por REQ, y `max_limit` restringe cuántos eventos puede solicitar un solo filtro. Estos parámetros ayudan a los clientes a adaptar su comportamiento a las capacidades del relay, evitando desconexiones por exceder límites.

La información de pago aparece en `fees` y `payments_url`. Los relays pueden cobrar por admisión (acceso único), suscripción (acceso recurrente) o publicación (tarifas por evento). El `payments_url` apunta a detalles sobre métodos de pago, típicamente facturas Lightning o mints de ecash. Los relays pagos usan estos campos para comunicar precios antes de que los clientes intenten autenticación.

El array `supported_nips` permite a los clientes descubrir capacidades del relay. Si un relay lista [NIP-50](/es/topics/nip-50/), los clientes saben que pueden enviar consultas de búsqueda de texto completo. Si aparece [NIP-42](/es/topics/nip-42/), los clientes deben esperar desafíos de autenticación. Esta publicidad declarativa de capacidades permite mejora progresiva: los clientes pueden usar características avanzadas donde estén disponibles mientras se degradan elegantemente en relays con soporte limitado.

La información del operador construye responsabilidad. El campo `pubkey` identifica al operador del relay en Nostr, permitiendo comunicación directa vía DMs de [NIP-17](/es/topics/nip-17/) o menciones públicas. El email de `contact` proporciona un respaldo fuera del protocolo. Juntos, estos campos ayudan a los usuarios a alcanzar operadores para reportes de abuso, solicitudes de acceso o problemas técnicos.

Los documentos [NIP-11](/es/topics/nip-11/) son auto-reportados: los relays describen lo que afirman soportar, no necesariamente lo que realmente hacen. Aquí es donde NIP-66 se vuelve importante.

### [NIP-66](/es/topics/nip-66/): Descubrimiento de Relay y Monitoreo de Actividad

[NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) estandariza la publicación de datos de monitoreo de relays en Nostr. Los servicios de monitoreo prueban continuamente relays para disponibilidad, latencia, cumplimiento de protocolo y NIPs soportados. Publican resultados como eventos kind 30166, proporcionando estado del relay en tiempo real independiente del auto-reporte del relay.

Los monitores verifican disponibilidad del relay conectándose y enviando suscripciones de prueba. Las mediciones de latencia rastrean tiempo de conexión, tiempo de respuesta de suscripción y retraso de propagación de eventos. Las pruebas de cumplimiento de protocolo verifican que el comportamiento del relay coincida con las especificaciones, capturando errores de implementación o desviaciones intencionadas. La verificación de soporte de NIP va más allá de las afirmaciones de [NIP-11](/es/topics/nip-11/) probando realmente si las características anunciadas funcionan correctamente.

```json
{
  "id": "a34b5c7d89e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7",
  "pubkey": "4e2d0bc6f8e7c3a5b9f1d2e3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4",
  "created_at": 1736784000,
  "kind": 30166,
  "tags": [
    ["d", "wss://relay.example.com"],
    ["rtt", "open", "143", "1736784000"],
    ["rtt", "read", "89", "1736784000"],
    ["rtt", "write", "92", "1736784000"],
    ["nips", "1", "2", "4", "9", "11", "12"],
    ["geo", "US", "United States", "New York"],
    ["other", "network", "clearnet"],
    ["other", "payment_required", "false"],
    ["other", "auth_required", "false"]
  ],
  "content": "{\"last_check\": 1736784000, \"checks\": 8760}",
  "sig": "8b9c4d5e6a7f8b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b"
}
```

La etiqueta `d` contiene la URL del relay, haciendo de este un evento reemplazable parametrizado. Cada monitor publica un evento por relay, actualizado a medida que cambian las mediciones. Múltiples monitores pueden rastrear el mismo relay, proporcionando redundancia y validación cruzada. Los clientes consultan múltiples pubkeys de monitores para obtener perspectivas diversas sobre la salud del relay.

Las etiquetas de tiempo de ida y vuelta (rtt) miden latencia para diferentes operaciones. `rtt open` rastrea el establecimiento de conexión WebSocket, `rtt read` mide tiempo de respuesta de suscripción, y `rtt write` prueba velocidad de publicación de eventos. Todos los valores están en milisegundos. Los clientes usan estas métricas para preferir relays de baja latencia para operaciones sensibles al tiempo o despriorizar relays lentos.

La etiqueta `nips` lista soporte de NIP realmente verificado, no solo soporte afirmado. Los monitores prueban cada NIP ejercitando su funcionalidad. Si un relay afirma búsqueda de [NIP-50](/es/topics/nip-50/) en su documento [NIP-11](/es/topics/nip-11/) pero las consultas de búsqueda fallan, los monitores omitirán NIP-50 de la lista verificada. Esto proporciona verdad fundamental sobre capacidades del relay.

La información geográfica ayuda a los clientes a seleccionar relays cercanos para mejor latencia y resistencia a censura. La etiqueta `geo` contiene código de país, nombre de país y región. La etiqueta `network` distingue relays clearnet de servicios ocultos Tor o endpoints I2P. Juntas, estas etiquetas permiten diversidad geográfica: los clientes pueden conectarse a relays en múltiples jurisdicciones para resistir censura regional.

Los datos del monitor potencian selectores de relay en clientes, sitios web exploradores y la propuesta de Aserciones de Confianza de Relays. Al combinar documentos auto-reportados de [NIP-11](/es/topics/nip-11/) con datos medidos de [NIP-66](/es/topics/nip-66/) y aserciones de confianza computadas, el ecosistema se mueve hacia selección informada de relays en lugar de depender de valores predeterminados codificados o recomendaciones de boca en boca.

## Lanzamientos

### 0xchat v1.5.3 - Características Mejoradas de Mensajería

[0xchat v1.5.3](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.3-release) trae mejoras significativas al cliente de mensajería Nostr estilo Telegram. El lanzamiento aborda problemas de cumplimiento de [NIP-55](/es/topics/nip-55/) (aplicación firmante de Android) que estaban impidiendo la firma apropiada de eventos a través de firmantes externos como Amber. El cumplimiento completo significa que 0xchat ahora delega correctamente operaciones de firma, mejorando la seguridad al mantener las claves privadas aisladas.

La actualización integra tanto FileDropServer como BlossomServer como opciones de almacenamiento de medios predeterminadas, dando a los usuarios redundancia para cargas de archivos. [Blossom](https://github.com/hzrd149/blossom) proporciona almacenamiento direccionado por contenido donde los archivos son referenciados por sus hashes SHA-256, asegurando integridad y permitiendo deduplicación a través de la red. El guardado automático de borradores para Momentos previene pérdida de datos al componer contenido de formato largo, abordando quejas de usuarios sobre publicaciones perdidas durante cambios de aplicación o interrupciones de conectividad.

La integración de billetera Cashu recibe pulido con filtrado automático de pruebas que elimina tokens gastados de la vista de billetera. Esto resuelve la confusa UX donde los usuarios veían pruebas inválidas junto con ecash válido, haciendo que los cálculos de saldo fueran poco confiables. El filtrado ocurre del lado del cliente, manteniendo privacidad mientras mejora la experiencia de pago para transacciones peer-to-peer dentro de chats.

### Amber v4.1.0 Pre-lanzamientos - Renovación de UI

[Amber v4.1.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.0-pre1) hasta [v4.1.0-pre3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.0-pre3) introducen una interfaz rediseñada para el popular firmante de eventos Android. La pantalla de inicio de sesión ahora muestra claramente qué aplicación está solicitando permisos de firma, abordando confusión del usuario sobre flujos de autorización. La nueva pantalla de eventos proporciona inspección detallada de qué datos las aplicaciones quieren firmar, permitiendo a los usuarios tomar decisiones de seguridad informadas antes de aprobar operaciones.

La gestión de permisos recibe atención significativa con una interfaz renovada que muestra exactamente qué capacidades se han otorgado a cada aplicación conectada. Los usuarios pueden revocar permisos específicos sin desconectarse completamente, permitiendo control de grano fino sobre delegación de firma. Los contadores de relay refactorizados usando la biblioteca quartz actualizada proporcionan estadísticas en tiempo real sobre rendimiento de eventos y desempeño del relay. Las conexiones bunker de [NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md) (Nostr Connect) ahora muestran mensajes de error detallados cuando las conexiones fallan, reemplazando errores de tiempo de espera crípticos con diagnósticos accionables.

## Cambios notables de código y documentación

*Estos son pull requests fusionados y desarrollos en etapa temprana que vale la pena rastrear. Algunos son características experimentales que pueden evolucionar antes del lanzamiento.*

### Zeus (Billetera Lightning con Nostr Wallet Connect)

Zeus fusionó 17 pull requests esta semana, fortaleciendo su posición como implementación líder de [NIP-47](/es/topics/nip-47/) Nostr Wallet Connect. Las correcciones más significativas abordan problemas de consistencia de datos y cumplimiento de protocolo que estaban causando problemas de interoperabilidad con clientes Nostr.

**Corrección de Historial de Transacciones** - El [PR #3542](https://github.com/ZeusLN/zeus/pull/3542) resuelve un error crítico donde las listas de transacciones NWC mostraban entradas incorrectas o duplicadas. El problema ocurría cuando Zeus almacenaba en caché datos de transacciones sin manejar apropiadamente actualizaciones de eventos, causando que los usuarios vieran transacciones fantasma o pagos faltantes. La corrección implementa deduplicación apropiada de eventos e invalidación de caché, asegurando que el historial de transacciones refleje con precisión el estado del nodo Lightning.

**Cumplimiento de Protocolo** - El [PR #3548](https://github.com/ZeusLN/zeus/pull/3548) aborda respuestas incompletas de `getInfo` que rompían compatibilidad con clientes esperando cumplimiento completo de NIP-47. Algunos clientes Nostr fallaban al recibir respuestas parciales sin campos como `block_height` o `network`. El PR asegura que todos los campos requeridos retornen con valores predeterminados sensatos incluso cuando la implementación Lightning subyacente no los proporciona, mejorando la compatibilidad de Zeus a través del ecosistema.

**Resiliencia de Conexión** - El [PR #3543](https://github.com/ZeusLN/zeus/pull/3543) implementa notificaciones de tiempo de espera para conexiones Nostr estancadas. Previamente, los usuarios esperaban indefinidamente cuando las conexiones de relay caían silenciosamente. Ahora Zeus muestra mensajes de tiempo de espera claros después de 30 segundos de inactividad, permitiendo a los usuarios reintentar o cambiar relays. El [PR #3541](https://github.com/ZeusLN/zeus/pull/3541) añade validación de backend para prevenir activación de NWC en implementaciones Lightning incompatibles, capturando errores de configuración antes de que causen fallas en tiempo de ejecución.

**Condición de Carrera de Cashu** - El [PR #3531](https://github.com/ZeusLN/zeus/pull/3531) corrige un error de concurrencia en la gestión de tokens Cashu donde operaciones simultáneas de mint podían corromper la base de datos de tokens. La condición de carrera ocurría cuando múltiples hilos actualizaban conteos de tokens sin bloqueo apropiado, ocasionalmente resultando en saldos incorrectos. La corrección añade protección de mutex alrededor de secciones críticas, asegurando actualizaciones atómicas al estado de tokens.

### Primal Android (Cliente)

Primal Android envió 12 PRs fusionados con mejoras significativas a seguridad de billetera y manejo de medios. La implementación de respaldo de billetera aborda una de las características más solicitadas, mientras que el soporte de NIP-92 mejora la experiencia visual a través de la aplicación.

**Sistema de Respaldo de Billetera** - Una serie de cuatro PRs ([#844](https://github.com/PrimalHQ/primal-android-app/pull/844), [#845](https://github.com/PrimalHQ/primal-android-app/pull/845), [#846](https://github.com/PrimalHQ/primal-android-app/pull/846), [#848](https://github.com/PrimalHQ/primal-android-app/pull/848)) implementa funcionalidad integral de respaldo de frase semilla. Los usuarios ahora pueden exportar su mnemónico de 12 palabras a través de un flujo seguro que previene capturas de pantalla, muestra estado de respaldo en el tablero de billetera y guía a usuarios existentes a través de la migración. La implementación sigue estándares BIP-39 e incluye validación para prevenir que los usuarios pierdan fondos debido a registro incorrecto de frases.

**Dimensiones de Medios (NIP-92)** - El [PR #718](https://github.com/PrimalHQ/primal-android-app/pull/718) implementa soporte de [NIP-92](/es/topics/nip-92/) para proporciones de aspecto apropiadas de imagen y video. Sin metadatos de dimensiones, los clientes deben descargar imágenes para determinar su tamaño, causando saltos de diseño mientras se carga el contenido. NIP-92 añade etiquetas `dim` (como `["dim", "1920x1080"]`) a eventos de metadatos de archivo, permitiendo a Primal reservar espacio correcto antes de descargar medios. Esto elimina reflujos molestos en galerías de imágenes y mejora el rendimiento percibido.

**Confiabilidad de Firmante Remoto** - El [PR #841](https://github.com/PrimalHQ/primal-android-app/pull/841) corrige problemas de conexión de [NIP-46](/es/topics/nip-46/) donde prefijos `wss://` faltantes causaban fallos silenciosos. El PR valida URIs de relay durante la configuración de conexión bunker, añadiendo el prefijo de protocolo automáticamente cuando los usuarios pegan dominios desnudos. El [PR #843](https://github.com/PrimalHQ/primal-android-app/pull/843) aborda un error de threading donde condiciones de red pobres causaban que las respuestas se publicaran como notas raíz, rompiendo el flujo de conversación. La corrección asegura que los IDs de eventos padre persistan a través de interrupciones de red.

### Protocolo Marmot: White Noise (Biblioteca de Chat Grupal Cifrado)

White Noise, la biblioteca Rust que potencia los chats grupales cifrados del [Protocolo Marmot](/es/topics/marmot/), fusionó seis PRs mejorando experiencia de usuario y seguridad. Los cambios acercan a Marmot a la paridad de características con aplicaciones de mensajería convencionales mientras mantiene su arquitectura que prioriza privacidad.

**Confirmaciones de Lectura** - El [PR #433](https://github.com/marmot-protocol/whitenoise-rs/pull/433) y [#436](https://github.com/marmot-protocol/whitenoise-rs/pull/436) implementan rastreo de lectura de mensajes para conversaciones grupales. El sistema almacena posiciones de lectura por usuario por grupo dentro de un solo dispositivo, permitiendo insignias de conteo no leídas. La implementación usa marcas de tiempo monotónicas para rastrear la posición del último mensaje leído para cada conversación. Esta característica fundamental permite indicadores de UI mostrando conteos de mensajes no leídos por conversación.

**Fijado de Conversaciones** - El [PR #442](https://github.com/marmot-protocol/whitenoise-rs/pull/442) añade fijado persistente de conversaciones a través de un campo `pin_order` en la tabla de unión `accounts_groups` que vincula cuentas a grupos. Las conversaciones fijadas mantienen su posición en la parte superior de listas de chat sin importar actividad de mensajes, coincidiendo con expectativas de usuarios de Signal y WhatsApp. La implementación usa ordenamiento entero para permitir fijados ilimitados con clasificación determinística.

**Resolución Determinística de Commits (MIP-03)** - El [PR #152](https://github.com/marmot-protocol/mdk/pull/152) (abierto) implementa la Propuesta de Mejora de Marmot 03, resolviendo el problema crítico de condiciones de carrera de commit en chats grupales distribuidos. Cuando múltiples miembros envían cambios de estado de grupo (agregar/remover miembros, cambiar permisos) simultáneamente, los clientes podían divergir en ordenamiento de commits, fragmentando el grupo en estados incompatibles. MIP-03 introduce instantáneas de época y selección determinística de ganador: el commit con la marca de tiempo `created_at` más temprana gana, con ID de evento lexicográfico como desempate. Esto permite a todos los clientes converger en el mismo estado a través de rollback y reproducción, manteniendo coherencia del grupo incluso durante particiones de red.

**Endurecimiento de Seguridad** - El [PR #443](https://github.com/marmot-protocol/whitenoise-rs/pull/443) previene copiado innecesario de secretos criptográficos usando referencias en `resolve_group_image_path`. Esto reduce la ventana para ataques de memoria donde los secretos podrían ser recuperados de asignaciones heap liberadas. El [PR #438](https://github.com/marmot-protocol/whitenoise-rs/pull/438) permite cifrado de base de datos SQLCipher a través de parámetros de keyring, protegiendo historial de mensajes en reposo. La integración de keyring permite almacenamiento seguro de claves en keychains de plataforma en lugar de archivos de configuración.

### nostrdb-rs (Biblioteca de Base de Datos) - PR Abierto

**Implementación de Consultas en Streaming** - El [PR #58](https://github.com/damus-io/nostrdb-rs/pull/58) (abierto) propone consultas de plegado en streaming para permitir operaciones de base de datos sin asignación de memoria. La implementación añadiría métodos `fold`, `try_fold`, `count`, `any`, `all` y `find_map` que procesarían resultados de base de datos uno a la vez sin materializar conjuntos de resultados enteros en vectores. Este enfoque reduciría el consumo de memoria y permitiría terminación temprana para patrones de consulta comunes.

La implementación técnica expone callbacks de resultados de consulta de bajo nivel (`ndb_query_visit`) como visitantes Rust con estado que mapean variantes `ControlFlow` a acciones de visitante C. Una vez fusionado, el código de aplicación se leerá como lógica de iterador mientras se ejecuta cerca de la capa de base de datos. Por ejemplo, contar notas coincidentes transmitiría a través de resultados en lugar de recolectarlos, y `find_map` retornaría el primer resultado útil sin procesar filas restantes.

nostrdb potencia Damus y Notedeck, clientes iOS/macOS y de escritorio respectivamente. Las consultas en streaming permitirían patrones eficientes como paginación, filtrado condicional y verificaciones de existencia. El PR cambia 3 archivos con +756 adiciones y -32 eliminaciones, una refactorización sustancial de la capa de consulta. Los usuarios de aplicaciones basadas en nostrdb-rs verían uso reducido de memoria al navegar líneas de tiempo grandes o buscar a través de bases de datos extensas de eventos.

### nak (Herramienta CLI)

nak, la herramienta Nostr de línea de comandos de fiatjaf, fusionó seis PRs enfocados en mejoras del sistema de compilación y nueva funcionalidad. El [PR #91](https://github.com/fiatjaf/nak/pull/91) implementa una característica de espejo Blossom, permitiendo a nak servir como espejo para servidores de medios Blossom. [Blossom](/es/topics/blossom/) es un protocolo de almacenamiento de medios direccionado por contenido que funciona junto con eventos Nostr.

Los PRs restantes abordan compatibilidad del sistema de compilación a través de plataformas Windows, macOS y Linux, permitiendo soporte de sistema de archivos FUSE para montar eventos Nostr como directorios locales.

### Damus (Cliente iOS) - PRs Abiertos

Damus tiene 11 PRs abiertos explorando mejoras arquitectónicas significativas. Aunque estos no se han fusionado todavía, señalan direcciones importantes para el desarrollo del cliente Nostr iOS, particularmente en torno a privacidad, eficiencia de sincronización y optimización de datos móviles.

**Integración de Tor** - El [PR #3535](https://github.com/damus-io/damus/pull/3535) incorpora el cliente Tor Arti directamente en Damus, permitiendo conexiones anónimas de relay sin dependencias externas. A diferencia de enfoques de Orbot o Tor Browser, incorporar Arti proporciona integración sin costuras con sandboxing de iOS y límites de ejecución en segundo plano. La implementación Rust aporta seguridad de memoria a la anonimización de red, reduciendo superficie de ataque comparada con C Tor. Los usuarios podrían alternar modo Tor por relay o globalmente, con el cliente manejando gestión de circuitos transparentemente.

**Protocolo de Sincronización Negentropy** - El [PR #3536](https://github.com/damus-io/damus/pull/3536) implementa Negentropy, un protocolo de reconciliación de conjuntos que mejora radicalmente la eficiencia de sincronización. En lugar de descargar todos los eventos desde la última conexión, Negentropy intercambia huellas compactas (árboles Merkle) para identificar exactamente qué eventos difieren entre cliente y relay. Para usuarios siguiendo cientos de pubkeys, esto reduce ancho de banda de sincronización de megabytes a kilobytes. La implementación se integra con RelayPool y SubscriptionManager, permitiendo sincronización eficiente automática a través de todos los relays conectados.

**Modo de Datos Bajo** - El [PR #3549](https://github.com/damus-io/damus/pull/3549) añade características de conservación de datos celulares respondiendo a retroalimentación de usuarios sobre consumo de ancho de banda. El modo deshabilita carga automática de imágenes, precarga de video y reduce límites de suscripción. Los usuarios en conexiones medidas pueden navegar contenido de texto sin temor a exceder límites de datos. La implementación respeta configuraciones de modo de datos bajo de iOS y proporciona controles granulares para diferentes tipos de medios.

**Optimizaciones de Base de Datos** - El [PR #3548](https://github.com/damus-io/damus/pull/3548) reelabora el almacenamiento de instantáneas de nostrdb para consultas más rápidas y uso reducido de disco. La optimización cambia cómo las instantáneas de base de datos persisten a disco, mejorando tanto rendimiento de lectura como amplificación de escritura. Esto aborda quejas de drenaje de batería de usuarios con bases de datos grandes de eventos.

---

Eso es todo por esta semana. ¿Construyendo algo? ¿Tienes noticias para compartir? ¿Quieres que cubramos tu proyecto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contáctanos vía DM NIP-17</a> o encuéntranos en Nostr.
