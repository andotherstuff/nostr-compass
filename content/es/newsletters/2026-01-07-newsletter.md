---
title: 'Nostr Compass #4'
date: 2026-01-07
publishDate: 2026-01-07
draft: false
type: newsletters
---

Bienvenidos de nuevo a Nostr Compass, tu guía semanal del ecosistema del protocolo Nostr.

**Esta semana:** Primal Android implementa firma remota [NIP-46](/es/topics/nip-46/) y soporte para firmante local [NIP-55](/es/topics/nip-55/), convirtiéndolo en un centro de firma completo para otras aplicaciones Android. El equipo del [Protocolo Marmot](/es/topics/marmot/) abordó hallazgos de una auditoría de seguridad con 18 PRs fusionados que fortalecen la mensajería cifrada basada en [MLS](/es/topics/mls/). Citrine alcanza la v1.0 y Applesauce lanza la v5.0 en toda su suite de bibliotecas. TENEX desarrolla supervisión de agentes de IA en Nostr, y Jumble agrega agrupación inteligente de relays. Una corrección en la especificación NIP-55 aclara los campos de retorno de `nip44_encrypt`, y un PR de [NIP-50](/es/topics/nip-50/) propone extensiones de expresiones de consulta para búsqueda avanzada. En nuestra sección de profundización, explicamos [NIP-04](/es/topics/nip-04/) y [NIP-44](/es/topics/nip-44/): por qué el cifrado heredado tiene fallas de seguridad y cómo el reemplazo moderno las corrige.

## Noticias

**Primal Android se Convierte en un Centro de Firma Completo** - La [Versión 2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) agrega tanto firma remota [NIP-46](/es/topics/nip-46/) como firma local [NIP-55](/es/topics/nip-55/), convirtiendo a Primal en un firmante completo para otras aplicaciones Nostr. La firma remota vía NIP-46 permite a los usuarios conectarse a servicios bunker a través de relays Nostr, manteniendo las claves completamente fuera de su dispositivo. La firma local vía NIP-55 expone a Primal como un proveedor de contenido de Android, para que aplicaciones como Amethyst o Citrine puedan solicitar firmas sin jamás tocar la clave privada. [Varios PRs de seguimiento](https://github.com/PrimalHQ/primal-android-app/pull/839) corrigieron problemas de compatibilidad con el requisito de pubkey hexadecimal de la especificación NIP-55, y mejoraron el análisis de URIs `nostrconnect://` mal formadas. La versión también incluye pre-caché de medios para un desplazamiento más fluido, tiempos de carga de hilos mejorados y pre-caché de avatares.

**Protocolo Marmot Fortalece la Seguridad Tras Auditoría** - El [Kit de Desarrollo Marmot](https://github.com/marmot-protocol/mdk) (mdk), que implementa mensajería cifrada de extremo a extremo basada en [NIP-104](/es/topics/nip-104/) MLS, recibió extensas correcciones de seguridad esta semana. Dieciocho pull requests fusionados abordaron hallazgos de la auditoría incluyendo: [verificación de hash para imágenes de grupo cifradas](https://github.com/marmot-protocol/mdk/pull/97) para prevenir ataques de sustitución de blobs a nivel de almacenamiento, [paginación para bienvenidas pendientes](https://github.com/marmot-protocol/mdk/pull/110) para prevenir agotamiento de memoria, [filtración de MLS Group ID en mensajes de error](https://github.com/marmot-protocol/mdk/pull/112), y [aplicación de codificación base64](https://github.com/marmot-protocol/mdk/pull/98) para paquetes de claves. La [especificación de Marmot en sí fue actualizada](https://github.com/marmot-protocol/marmot/pull/20) con versionado MIP-04 v2 y mejoras de seguridad. PRs activos continúan abordando reutilización de nonce, zerorizacion de secretos y vectores de contaminación de caché.

**Nostrability Rastrea Soporte de Relay Hints** - Un nuevo [rastreador de compatibilidad de relay hints](https://github.com/nostrability/nostrability/issues/270) documenta cómo los clientes construyen y consumen relay hints en todo el ecosistema. El rastreador revela que mientras la mayoría de los clientes ahora construyen hints según [NIP-10](/es/topics/nip-10/) y [NIP-19](/es/topics/nip-19/), el consumo varía ampliamente: algunos clientes incluyen hints en eventos salientes pero no usan hints entrantes para obtener datos. Seis clientes obtuvieron el estado "Completo" por implementación completa. El rastreador es útil para desarrolladores que verifican interoperabilidad y para usuarios que se preguntan por qué algunos clientes encuentran contenido que otros no pueden.

**Nostria 2.0 Lanza Renovación de Funciones Multiplataforma** - El cliente [Nostria](https://nostria.app) [lanzó la versión 2.0](nostr:naddr1qvzqqqr4gupzp5daxvenwv7ucsglpm5f8vuts530cr0zylllgkwejpzvak0x2kqmqqykummnw3exjcfdxgedqf5p) el 30 de diciembre con adiciones significativas en iOS (TestFlight), Android (Play Store), Web y Windows. La versión agrega soporte nativo de música con creación de listas de reproducción, subida de pistas, pagos a artistas basados en zap, y un reproductor estilo WinAmp con ecualizador funcional. El streaming en vivo obtiene integración con Game API mostrando metadatos enriquecidos durante transmisiones de juegos. Una nueva función de Resumen genera digestos de actividad por hora, día o semana como vistas de línea de tiempo comprimidas. La sección Descubrir ofrece listas curadas para encontrar contenido y perfiles. La publicación de medios se simplifica con generación automática de publicaciones de formato corto para descubrimiento entre clientes. Las conexiones de firmante remoto ahora funcionan vía escaneo de código QR sin configuración manual. El descubrimiento de perfiles aborda un punto de dolor común de Nostr: cuando los usuarios se mueven entre relays sin llevar sus metadatos, Nostria localiza su perfil y lo republica en sus relays actuales. Los suscriptores Premium obtienen integración de canal de YouTube, Memos privados, paneles de analíticas y respaldos automáticos de lista de seguidos con opciones de fusión/restauración.

## Actualizaciones de NIPs

Cambios recientes al [repositorio de NIPs](https://github.com/nostr-protocol/nips):

**Fusionados:**
- **[NIP-55](/es/topics/nip-55/)** - Corregido el campo de retorno para el método `nip44_encrypt` ([#2184](https://github.com/nostr-protocol/nips/pull/2184)). Los firmantes de Android ahora deben devolver la carga útil cifrada en el campo `signature` (coincidiendo con `nip44_decrypt`) en lugar de un campo separado. Esto alinea la especificación con las implementaciones existentes en Amber y Primal.

**PRs Abiertos:**
- **[NIP-50](/es/topics/nip-50/)** - Extensiones de Expresiones de Consulta ([#2182](https://github.com/nostr-protocol/nips/pull/2182)) propone extender la búsqueda NIP-50 con expresiones de consulta estructuradas. El PR agrega operadores como `kind:1`, `author:npub1...`, y combinaciones booleanas (`AND`, `OR`, `NOT`), permitiendo consultas de búsqueda más precisas más allá de la simple coincidencia de texto. Esto permitiría a los clientes construir interfaces de búsqueda avanzadas mientras mantienen compatibilidad hacia atrás con cadenas de búsqueda básicas.

## Profundización en NIPs: NIP-04 y NIP-44

Esta semana cubrimos los estándares de cifrado de Nostr: el heredado NIP-04 que aún encontrarás, y su reemplazo moderno NIP-44 que corrige fallas de seguridad críticas.

### [NIP-04](/es/topics/nip-04/): Mensajes Directos Cifrados (Heredado)

[NIP-04](https://github.com/nostr-protocol/nips/blob/master/04.md) fue el primer intento de Nostr de mensajería cifrada, usando eventos kind 4. Aunque es simple de implementar, tiene debilidades de seguridad conocidas y está deprecado en favor de NIP-44.

**Cómo funciona:** NIP-04 usa ECDH (Diffie-Hellman de Curva Elíptica) para derivar un secreto compartido entre emisor y receptor, luego cifra con AES-256-CBC.

```json
{
  "id": "<event-id>",
  "pubkey": "<sender-pubkey>",
  "created_at": 1736200000,
  "kind": 4,
  "tags": [["p", "<recipient-pubkey>"]],
  "content": "base64-ciphertext?iv=base64-iv",
  "sig": "<signature>"
}
```

El flujo de cifrado:
1. Calcular punto compartido: `shared = ECDH(sender_privkey, recipient_pubkey)`
2. Derivar clave: `key = SHA256(shared_x_coordinate)`
3. Generar IV aleatorio de 16 bytes
4. Cifrar: `ciphertext = AES-256-CBC(key, iv, plaintext)`
5. Formatear contenido: `base64(ciphertext)?iv=base64(iv)`

**Problemas de seguridad:**

- **Sin autenticación:** AES-CBC proporciona confidencialidad pero no integridad. Un atacante que controle un relay podría modificar bits del texto cifrado, causando cambios predecibles en el texto plano (ataques de volteo de bits).
- **IV en claro:** El vector de inicialización se transmite junto al texto cifrado, y el modo CBC con IVs predecibles habilita ataques de texto plano elegido.
- **Sin validación de relleno:** Las implementaciones varían en cómo manejan el relleno PKCS#7, potencialmente habilitando ataques de oráculo de relleno.
- **Exposición de metadatos:** La pubkey del emisor, la pubkey del receptor y la marca de tiempo son todas visibles para los relays.
- **Reutilización de clave:** El mismo secreto compartido se usa para todos los mensajes entre dos partes, para siempre.

**Por qué aún existe:** Muchos clientes y relays antiguos solo soportan NIP-04. Lo encontrarás al interactuar con sistemas heredados. Firmantes como Amber y aplicaciones como Primal aún implementan `nip04_encrypt`/`nip04_decrypt` para compatibilidad hacia atrás.

### [NIP-44](/es/topics/nip-44/): Cifrado Versionado

[NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md) es el estándar de cifrado moderno, diseñado para corregir las fallas conocidas de NIP-04. Una auditoría de seguridad de Cure53 de las implementaciones de NIP-44 identificó 10 problemas (incluyendo ataques de temporización y preocupaciones de secreto hacia adelante) que fueron abordados antes de que la especificación fuera finalizada. Usa ChaCha20-Poly1305 con derivación de clave apropiada y cifrado autenticado.

**Mejoras clave sobre NIP-04:**

| Aspecto            | NIP-04                     | NIP-44                  |
|:-------------------|:---------------------------|:------------------------|
| Cifrador           | AES-256-CBC                | XChaCha20-Poly1305      |
| Autenticación      | Ninguna                    | Poly1305 MAC            |
| Derivación de clave| SHA256(shared_x)           | HKDF con sal            |
| Nonce              | IV de 16 bytes, patrón reutilizado | Nonce aleatorio de 24 bytes |
| Relleno            | PKCS#7 (filtra longitud)   | Rellenado a potencia de 2 |
| Versionado         | Ninguno                    | Prefijo de byte de versión |

**Flujo de cifrado:**

1. **Clave de conversación:** Derivar una clave estable para cada par emisor-receptor:
   ```
   shared_x = ECDH(sender_privkey, recipient_pubkey).x
   conversation_key = HKDF-SHA256(
     ikm = shared_x,
     salt = "nip44-v2",
     info = ""
   )
   ```

2. **Claves de mensaje:** Para cada mensaje, generar un nonce aleatorio de 32 bytes y derivar claves de cifrado/autenticación:
   ```
   keys = HKDF-SHA256(
     ikm = conversation_key,
     salt = nonce,
     info = "nip44-v2"
   )
   chacha_key = keys[0:32]
   chacha_nonce = keys[32:44]
   hmac_key = keys[44:76]
   ```

3. **Rellenar texto plano:** Rellenar a la siguiente potencia de 2 (minimo 32 bytes) para ocultar la longitud del mensaje:
   ```
   padded = [length_u16_be] + [plaintext] + [zeros to next power of 2]
   ```

4. **Cifrar y autenticar:**
   ```
   ciphertext = XChaCha20(chacha_key, chacha_nonce, padded)
   mac = HMAC-SHA256(hmac_key, nonce + ciphertext)
   ```

5. **Formatear carga util:**
   ```
   payload = [version=0x02] + [nonce] + [ciphertext] + [mac]
   content = base64(payload)
   ```

**Byte de versión:** El primer byte (`0x02`) indica la versión de cifrado. Esto permite actualizaciones futuras sin romper mensajes existentes. La versión `0x01` fue un borrador anterior que nunca fue ampliamente desplegado.

**Descifrado:**

1. Decodificar base64, verificar que el byte de versión sea `0x02`
2. Extraer nonce (bytes 1-32), texto cifrado y MAC (últimos 32 bytes)
3. Derivar clave de conversación usando la clave privada del receptor y la clave pública del emisor
4. Derivar claves de mensaje de la clave de conversación y el nonce
5. Verificar MAC antes de descifrar (rechazar si es inválido)
6. Descifrar texto cifrado, extraer prefijo de longitud, devolver texto plano sin relleno

**Propiedades de seguridad:**

- **Cifrado autenticado:** El MAC Poly1305 asegura que cualquier manipulación se detecte antes del descifrado
- **Secreto hacia adelante (parcial):** Cada mensaje usa un nonce único, por lo que comprometer un mensaje no revela otros. Sin embargo, comprometer una clave privada aún revela todos los mensajes pasados (sin ratcheting).
- **Ocultación de longitud:** El relleno a potencia de 2 oscurece la longitud exacta del mensaje
- **Resistencia a ataques de temporización:** Comparación en tiempo constante para verificación de MAC

**Uso en la práctica:** NIP-44 es la capa de cifrado para:
- [NIP-17](/es/topics/nip-17/) mensajes directos privados (dentro de gift wrap)
- [NIP-46](/es/topics/nip-46/) comunicación de firmante remoto
- [NIP-59](/es/topics/nip-59/) cifrado de seal
- [Protocolo Marmot](/es/topics/nip-104/) mensajes de grupo, donde NIP-44 envuelve contenido cifrado con MLS usando una clave derivada del secreto exportador de MLS
- Cualquier aplicación que necesite cifrado seguro punto a punto

**Guía de migración:** Las nuevas aplicaciones deben usar NIP-44 exclusivamente. Para compatibilidad hacia atrás, verifica si el cliente de un contacto soporta NIP-44 (vía metadatos de aplicación [NIP-89](/es/topics/nip-89/) o soporte de relay) antes de recurrir a NIP-04. Al recibir mensajes, intenta primero el descifrado NIP-44, luego recurre a NIP-04 para contenido heredado.

## Lanzamientos

**Primal Android v2.6.18** - El [lanzamiento completo](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) agrega firma remota [NIP-46](/es/topics/nip-46/) y firma local [NIP-55](/es/topics/nip-55/), convirtiendo a Primal en un centro de firma para otras aplicaciones Android. Las mejoras de rendimiento incluyen pre-caché de medios, pre-caché de avatares y carga de hilos más rápida. Las correcciones de errores abordan auto-menciones en biografías, fallos en la galería de medios y respaldos de títulos de stream. En iOS, Primal usa reproducción de audio en segundo plano para mantener la aplicación activa y recibir solicitudes de firma NIP-46; los usuarios pueden cambiar el sonido o silenciarlo completamente en configuración.

**Mostro v0.15.6** - La plataforma de trading P2P de Bitcoin [NIP-69](/es/topics/nip-69/) en su [último lanzamiento](https://github.com/MostroP2P/mostro/releases/tag/v0.15.6) completa la implementación del fondo de desarrollo con eventos de auditoría de Fase 4. Los pagos de tarifas de desarrollo ahora se rastrean vía eventos Nostr kind 38383 publicados después de cada pago exitoso, permitiendo verificación y analíticas de terceros. Los cálculos de montos fueron corregidos para mensajes de comprador/vendedor, y la lógica de premium fue alineada con la implementación de referencia lnp2pbot.

**Aegis v0.3.5** - El firmante multiplataforma [agrega modo oscuro](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.5), visualización mejorada de iconos de aplicación y diseños de UI más limpios. Las correcciones de errores abordan conflictos con iCloud Private Relay en iOS y problemas de análisis de eventos. El lanzamiento también mejora cómo el JSON de eventos se pasa a la función de firma en Rust.

**Citrine v1.0.0** - La aplicación de relay para Android [alcanza la 1.0](https://github.com/greenart7c3/Citrine/releases/tag/v1.0.0). Citrine te permite ejecutar un relay Nostr personal directamente en tu dispositivo Android, útil para caché local, respaldo o como compañero de NIP-55. Esta versión agrega un manejador de reportes de fallos, mejora la eficiencia de consultas de base de datos y actualiza traducciones vía Crowdin.

**Applesauce v5.0.0** - La suite de bibliotecas TypeScript de hzrd149 [lanza una versión mayor](https://github.com/hzrd149/applesauce/releases) con cambios que rompen compatibilidad enfocados en corrección y simplicidad. El paquete core ahora [verifica firmas de eventos por defecto](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.0.0) y renombra métodos de coordenadas para usar terminología de "address" más clara (`parseCoordinate` -> `parseReplaceableAddress`). El paquete relay [reduce los reintentos por defecto de 10 a 3](https://github.com/hzrd149/applesauce/releases/tag/applesauce-relay%405.0.0) e ignora relays inalcanzables por defecto, además agrega `createUnifiedEventLoader` para obtención de eventos más simple. El paquete wallet obtiene [descubrimiento de mints Cashu NIP-87](/es/topics/nip-87/) [](https://github.com/hzrd149/applesauce/releases/tag/applesauce-wallet%405.0.0). Las dependencias directas de `nostr-tools` fueron removidas de los paquetes, reduciendo el tamaño del bundle y conflictos de versiones.

## Cambios notables de código y documentación

*Estos son pull requests abiertos y trabajo en etapa temprana, perfectos para obtener retroalimentación antes de que se fusionen. Si algo te llama la atención, considera revisar o comentar!*

### Damus (iOS)

Una serie de PRs mejoran la experiencia de artículos de formato largo. [Mejoras de UX de lectura](https://github.com/damus-io/damus/pull/3496) agregan una barra de progreso, tiempo estimado de lectura, modo sepia, altura de línea ajustable y modo de enfoque que oculta la navegación mientras se desplaza. [Correcciones de imágenes](https://github.com/damus-io/damus/pull/3489) aseguran que las imágenes en contenido markdown se muestren con proporciones adecuadas al preprocesar imágenes independientes como elementos a nivel de bloque. [Tarjetas de vista previa de formato largo](https://github.com/damus-io/damus/pull/3497) reemplazan texto inline `@naddr1...` con tarjetas de vista previa enriquecidas mostrando título y metadatos del artículo. Una nueva [suite de pruebas de integración de relay](https://github.com/damus-io/damus/pull/3508) agrega 137 pruebas relacionadas con red incluyendo verificación del protocolo [NIP-01](/es/topics/nip-01/) y comportamiento bajo condiciones de red degradadas (simulación 3G).

### Bitchat (Mensajería Cifrada)

Endurecimiento de seguridad en el mensajero iOS Nostr+Cashu. [Limpieza de secreto DH del protocolo Noise](https://github.com/permissionlesstech/bitchat/pull/928) corrige seis ubicaciones donde los secretos compartidos no se estaban poniendo a cero después del acuerdo de claves Diffie-Hellman, restaurando las garantías de secreto hacia adelante. [Seguridad de hilos para colas de recibos de lectura](https://github.com/permissionlesstech/bitchat/pull/929) agrega sincronización de barrera para prevenir condiciones de carrera en NostrTransport. [Optimización del deduplicador de mensajes](https://github.com/permissionlesstech/bitchat/pull/920) mejora el rendimiento con altos volúmenes de mensajes, y [endurecimiento del análisis de cadenas hexadecimales](https://github.com/permissionlesstech/bitchat/pull/919) previene fallos por entrada malformada.

### Frostr (Firma de Umbral)

El protocolo de firma de umbral basado en [FROST](/es/topics/frost/) [agregó visualización de código QR](https://github.com/FROSTR-ORG/igloo-desktop/pull/62) para credenciales de grupo y credenciales de participación durante la incorporación y en la interfaz del firmante. Esto permite una configuración más fácil al distribuir participaciones de clave entre múltiples dispositivos, permitiendo a los usuarios escanear credenciales en lugar de copiar manualmente cadenas largas.

### Marmot mdk (Biblioteca)

Más allá de las correcciones de seguridad mencionadas anteriormente, PRs activos abordan hallazgos restantes de la auditoría: [tipo Secret<T> para zerorizacion](https://github.com/marmot-protocol/mdk/pull/109) introduce un tipo envolvente que automáticamente pone a cero datos sensibles al descartarse, [paginación de consultas de mensajes](https://github.com/marmot-protocol/mdk/pull/111) previene agotamiento de memoria al cargar historial de chat, y [almacenamiento cifrado](https://github.com/marmot-protocol/mdk/pull/102) agrega cifrado en reposo para la base de datos SQLite que almacena el estado del grupo y mensajes.

### Amethyst (Android)

Una semana ocupada de correcciones de estabilidad en el cliente Android. [Análisis JSON tolerante](https://github.com/vitorpamplona/amethyst/commit/2c42796) previene fallos de eventos malformados al hacer que Kotlin Serialization sea más permisivo. La validación de eventos ahora [verifica el tamaño del campo kind](https://github.com/vitorpamplona/amethyst/commit/40f9622) antes de procesar para evitar excepciones de valores sobredimensionados. La UI de puntuación de confianza obtuvo un icono más pequeño para reducir la interferencia visual, y [registro de errores mejorado](https://github.com/vitorpamplona/amethyst/commit/69c53ac) ayuda a diagnosticar problemas de conexión de relay. Las actualizaciones de traducción llegaron vía Crowdin, y varias advertencias de SonarQube fueron abordadas.

### TENEX (Agentes de IA)

El framework de agentes de IA nativo de Nostr vio 81 commits esta semana construyendo capacidades autónomas. El nuevo [sistema de supervisión de agentes](https://github.com/tenex-chat/tenex/pull/48) implementa heurísticas de comportamiento para monitorear acciones de agentes e intervenir cuando sea necesario. [Transparencia de delegación](https://github.com/tenex-chat/tenex/commit/b244c10) agrega registro de intervención de usuario a las transcripciones de delegación, para que los usuarios puedan auditar lo que los agentes hicieron en su nombre. El [registro de proveedores LLM](https://github.com/tenex-chat/tenex/pull/47) fue modularizado para integración más fácil de diferentes backends de IA. El soporte de conversación entre proyectos permite que los agentes mantengan contexto a través de múltiples proyectos basados en Nostr.

### Jumble (Cliente Web)

El cliente web enfocado en relays agregó varias mejoras de experiencia de usuario. [Pool de relay inteligente](https://github.com/CodyTseng/jumble/commit/695f2fe) gestiona conexiones inteligentemente basándose en patrones de uso. [Alternador de feed en vivo](https://github.com/CodyTseng/jumble/commit/917fcd9) permite a los usuarios cambiar entre streaming en tiempo real y actualización manual. [Mostrar automáticamente nuevas notas](https://github.com/CodyTseng/jumble/commit/d1b3a8c) en la parte superior muestra contenido fresco sin requerir recarga de página. [Caché persistente](https://github.com/CodyTseng/jumble/commit/fd9f41c) para el feed de seguidos y notificaciones mejora los tiempos de carga en visitas de retorno. Los usuarios ahora pueden [cambiar relays por defecto](https://github.com/CodyTseng/jumble/commit/53a67d8) a través de configuración.

---

Eso es todo por esta semana. ¿Estás construyendo algo? ¿Tienes noticias para compartir? ¿Quieres que cubramos tu proyecto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contáctanos vía DM NIP-17</a> o encuéntranos en Nostr.
