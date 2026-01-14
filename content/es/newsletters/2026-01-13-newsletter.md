---
title: 'Nostr Compass #5'
date: 2026-01-13
publishDate: 2026-01-13
draft: false
type: newsletters
---

Bienvenido de nuevo a Nostr Compass, tu guía semanal sobre Nostr.

**Esta semana:** Bitchat se somete a una auditoría de seguridad profesional realizada por Cure53, la misma firma que auditó Signal y [NIP-44](/es/topics/nip-44/), con más de 17 PRs ya fusionados que corrigen hallazgos críticos. [NIP-71](/es/topics/nip-71/) se fusiona, trayendo eventos de video direccionables al protocolo. Un NIP de criptografía post-cuántica abre la discusión sobre cómo preparar Nostr para el futuro contra ataques cuánticos. Amethyst v1.05.0 incluye listas de marcadores, notas de voz y una versión temprana para escritorio, mientras que Nostur v1.25.3 mejora los DMs de [NIP-17](/es/topics/nip-17/) con reacciones y respuestas. En noticias de bibliotecas, rust-nostr expande el soporte de [NIP-62](/es/topics/nip-62/) en los backends SQLite y LMDB, y NDK corrige un error en el seguimiento de suscripciones.

## Noticias

### Bitchat Completa la Auditoría de Seguridad de Cure53

Bitchat, el mensajero cifrado para iOS que combina Nostr con Cashu, se ha sometido a una auditoría de seguridad profesional realizada por Cure53, una de las firmas de seguridad más respetadas de la industria. Cure53 anteriormente auditó Signal, Mullvad VPN, y notablemente la especificación de cifrado [NIP-44](/es/topics/nip-44/) que sustenta la mensajería privada moderna de Nostr.

La auditoría encontró más de 12 problemas de seguridad (BCH-01-002 hasta BCH-01-013). El equipo de Bitchat respondió con más de 17 pull requests. Las correcciones clave incluyen:

**Limpieza de Secretos DH del Protocolo Noise** - [PR #928](https://github.com/permissionlesstech/bitchat/pull/928) corrige seis ubicaciones donde los secretos compartidos de Diffie-Hellman no se estaban poniendo a cero después del acuerdo de claves, restaurando las garantías de forward secrecy. Cuando los secretos persisten en memoria más tiempo del necesario, un volcado de memoria o ataque de arranque en frío podría comprometer comunicaciones pasadas.

**Verificación de Firmas** - Múltiples PRs refuerzan las rutas de verificación criptográfica, asegurando que las comprobaciones de autenticidad de mensajes no puedan ser eludidas mediante entradas malformadas.

**Seguridad de Hilos** - [PR #929](https://github.com/permissionlesstech/bitchat/pull/929) añade sincronización de barrera a las colas de confirmación de lectura en NostrTransport, previniendo condiciones de carrera que podrían causar corrupción de datos o fallos bajo altos volúmenes de mensajes.

**Seguridad de Memoria** - [PR #920](https://github.com/permissionlesstech/bitchat/pull/920) optimiza el deduplicador de mensajes para mejor rendimiento con alto volumen de mensajes mientras evita el agotamiento de memoria.

**Validación de Entrada** - [PR #919](https://github.com/permissionlesstech/bitchat/pull/919) refuerza el análisis de cadenas hexadecimales para prevenir fallos por entrada malformada, un vector de ataque común para denegación de servicio.

Bitchat maneja ecash de Cashu, haciendo esencial la revisión de seguridad profesional. La auditoría sigue a la auditoría del Protocolo [Marmot](/es/topics/marmot/) del año pasado y la auditoría de NIP-44 que verificó la capa de cifrado.

## Actualizaciones de NIPs

Cambios recientes en el [repositorio de NIPs](https://github.com/nostr-protocol/nips):

**Fusionados:**

- **[NIP-71](/es/topics/nip-71/)** - Eventos de Video Direccionables ([#1669](https://github.com/nostr-protocol/nips/pull/1669)) introduce los kinds 34235 (video horizontal) y 34236 (video vertical) como eventos direccionables. Una etiqueta `d` requerida proporciona identificadores únicos, para que los metadatos del video puedan actualizarse sin republicar todo el evento. Una etiqueta `origin` opcional rastrea las fuentes de importación. Ya implementado en Amethyst y nostrvine.

**PRs Abiertos:**

- **Criptografía Post-Cuántica** - [PR #2185](https://github.com/nostr-protocol/nips/pull/2185) propone añadir algoritmos criptográficos resistentes a computación cuántica a Nostr. La especificación introduce ML-DSA-44 y Falcon-512 para firmas digitales, dirigidos a "eventos de muy alto valor" como aplicaciones y autoridades en lugar de usuarios individuales. Mientras que el cifrado simétrico de [NIP-44](/es/topics/nip-44/) (ChaCha20) es resistente a computación cuántica, su intercambio de claves usa secp256k1 ECDH que es vulnerable al algoritmo de Shor. La propuesta incluye ML-KEM para acuerdo de claves para abordar esta brecha. Esta es una propuesta en etapa temprana que abre la discusión sobre agilidad criptográfica para la seguridad a largo plazo de Nostr.
- **BOLT12 para NIP-47** - Después de 137 comentarios y amplia discusión, la comunidad decidió que las ofertas BOLT12 merecen su propia especificación en lugar de extender [NIP-47](/es/topics/nip-47/). Las ofertas BOLT12 proporcionan mejoras significativas sobre las facturas BOLT11 incluyendo reutilización, mejor privacidad a través de rutas cegadas e información opcional del pagador. El nuevo NIP definirá métodos como `make_offer`, `pay_offer` y `list_offers` para implementaciones de Nostr Wallet Connect.
- **NIP de Pistas de Audio** - [PR #1043](https://github.com/nostr-protocol/nips/pull/1043) propone los kinds 32100 para pistas musicales y 32101 para episodios de podcast, dando al contenido de audio el mismo tratamiento de primera clase que NIP-71 proporciona para video. Actualmente, plataformas de audio como Wavlake, Zapstr y Stemstr usan cada una formatos de eventos propietarios, fragmentando el ecosistema. Un estándar común permitiría interoperabilidad para que los usuarios puedan descubrir y reproducir audio desde cualquier cliente compatible.
- **NIP-A3 Destinos de Pago Universales** - [PR #2119](https://github.com/nostr-protocol/nips/pull/2119) propone eventos kind 10133 usando URIs `payto:` de RFC-8905 para exponer opciones de pago a través de múltiples redes. En lugar de crear kinds de eventos separados para Bitcoin, Lightning, Cashu o rieles de pago tradicionales, esta abstracción permite a los clientes analizar etiquetas estandarizadas e invocar manejadores de pago nativos. El enfoque es a prueba de futuro ya que los nuevos métodos de pago solo necesitan un esquema de URI `payto:`.

## Análisis Profundo de NIPs: NIP-51 y NIP-65

Esta semana cubrimos dos NIPs que almacenan preferencias del usuario: NIP-51 para organizar contenido, y NIP-65 para organizar conexiones de relay. Ambos usan eventos reemplazables, lo que significa que cada nueva publicación sobrescribe la versión anterior.

### [NIP-51](/es/topics/nip-51/): Listas

[NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md) define múltiples tipos de listas para organizar referencias a eventos, usuarios, hashtags y otro contenido. Amethyst v1.05.0 añade soporte de marcadores, haciendo de este un buen momento para entender cómo funcionan las listas.

La especificación define varios kinds de listas, cada uno sirviendo un propósito diferente. Kind 10000 es tu lista de silenciados para ocultar usuarios, hilos o palabras. Kind 10001 fija eventos para destacar en tu perfil. Kind 30003 almacena marcadores, que es lo que Amethyst ahora soporta. Otros kinds manejan conjuntos de seguidos (30000), colecciones curadas de artículos (30004), intereses de hashtags (30015) y conjuntos de emojis personalizados (30030).

Las listas referencian contenido a través de etiquetas. Una lista de marcadores usa etiquetas `e` para eventos específicos y etiquetas `a` para contenido direccionable como artículos:

```json
{
  "id": "ae3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1736784000,
  "kind": 30003,
  "tags": [
    ["d", "saved-articles"],
    ["e", "abc123def456...", "wss://relay.example"],
    ["a", "30023:author-pubkey:article-id", "wss://relay.example"]
  ],
  "content": "<encrypted-private-bookmarks>",
  "sig": "908a15e46fb4d8675bab026fc230a0e3542bfade63da02d542fb78b2a8513fcd0092619a2c8c1221e581946e0191f2af505dfdf8657a414dbca329186f009262"
}
```

La etiqueta `d` proporciona un identificador único, para que puedas mantener múltiples conjuntos de marcadores como "saved-articles", "read-later" o "favorites" bajo el mismo kind.

Las listas soportan tanto elementos públicos como privados. Los elementos públicos aparecen en el array de etiquetas, visibles para cualquiera que obtenga el evento. Los elementos privados van en el campo `content`, cifrados usando [NIP-44](/es/topics/nip-44/) hacia ti mismo. Esta estructura dual te permite mantener marcadores públicos mientras adjuntas notas privadas, o mantener una lista de silenciados sin revelar a quién has silenciado. Para cifrar hacia ti mismo, usa NIP-44 con tu propia pubkey como destinatario.

Los kinds de la serie 10000 son reemplazables, lo que significa que los relays mantienen solo un evento por pubkey. Los de la serie 30000 son reemplazables parametrizados, permitiendo un evento por combinación de pubkey y etiqueta `d`. En ambos casos, actualizar una lista significa publicar un reemplazo completo; no puedes enviar cambios incrementales. Los clientes deben preservar etiquetas desconocidas al modificar listas para evitar sobrescribir datos añadidos por otras aplicaciones.

### [NIP-65](/es/topics/nip-65/): Metadatos de Lista de Relays

[NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md) define eventos kind 10002 que anuncian qué relays prefiere un usuario para lectura y escritura. Esto ayuda a otros usuarios y clientes a encontrar tu contenido.

```json
{
  "id": "bd2217a96b5835b59f9a6a42d8d8a36f8c9b7d4e5f0a1b2c3d4e5f6a7b8c9d0e1",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1736784000,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "f1c2d3e4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2"
}
```

Cada etiqueta `r` contiene una URL de relay y un marcador opcional. Un marcador `write` designa tu outbox: relays donde publicas tu contenido. Un marcador `read` designa tu inbox: relays donde verificas menciones, respuestas y etiquetas. Omitir el marcador indica ambos.

Cuando Alice quiere encontrar las publicaciones de Bob, su cliente obtiene el kind 10002 de Bob, extrae sus relays de escritura (su outbox) y se suscribe allí. Cuando Alice responde a Bob, su cliente publica en los relays de lectura de él (su inbox) para que vea la mención. Este enrutamiento consciente de relays es el "modelo outbox", y distribuye a los usuarios entre muchos relays en lugar de concentrar a todos en unos pocos servidores centrales.

NIP-65 maneja el enrutamiento de contenido público, pero los mensajes privados usan una lista separada. [NIP-17](/es/topics/nip-17/) define kind 10050 para relays de inbox de DM, usando etiquetas `relay` en lugar de etiquetas `r`. Al enviar a alguien un mensaje privado, los clientes buscan el evento kind 10050 del destinatario y publican el mensaje envuelto cifrado allí. Esta separación mantiene el enrutamiento de DM distinto del enrutamiento de contenido público, y permite a los usuarios especificar diferentes relays para comunicación privada versus pública.

El modelo outbox mejora la resistencia a la censura ya que ningún relay único necesita almacenar o servir el contenido de todos. Los clientes mantienen conexiones con los relays listados en los eventos NIP-65 de sus usuarios seguidos, conectándose dinámicamente a nuevos relays a medida que descubren nuevas cuentas. NIP-65 complementa las pistas de relay encontradas en otros NIPs. Cuando etiquetas a alguien con `["p", "pubkey", "wss://hint.relay"]`, la pista le dice a los clientes dónde buscar esa referencia específica. NIP-65 proporciona la lista autoritativa controlada por el usuario, mientras que las pistas ofrecen atajos incrustados en eventos individuales.

Para mejores resultados, mantén tu lista de relays actualizada ya que las entradas obsoletas te hacen más difícil de encontrar. La especificación recomienda de dos a cuatro relays por categoría. Listar demasiados relays sobrecarga a cada cliente que quiere obtener tu contenido, ralentizando su experiencia y aumentando la carga de red. Los clientes almacenan en caché los eventos NIP-65 y los refrescan periódicamente para mantenerse actualizados a medida que los usuarios actualizan sus preferencias.

## Lanzamientos

**Amethyst v1.05.0** - El popular cliente de Android [lanza una actualización importante](https://github.com/vitorpamplona/amethyst/releases) con varias características destacadas. Las listas de marcadores kind 30003 de [NIP-51](/es/topics/nip-51/) permiten a los usuarios guardar publicaciones para referencia posterior, sincronizándose entre clientes compatibles. Las notas de voz ahora funcionan en DMs y publicaciones regulares con visualización de forma de onda, selección de servidor de medios e indicadores de progreso de carga. Las puntuaciones de [Web of Trust](/es/topics/web-of-trust/) ahora son visibles en la interfaz, ayudando a los usuarios a entender cómo el algoritmo evalúa las cuentas en relación con su grafo social. La migración de base de datos [Quartz](/es/topics/quartz/) mejora el rendimiento de consultas como parte del trabajo de Kotlin Multiplatform financiado por OpenSats. Un lanzamiento temprano para escritorio trae Amethyst a Windows, macOS y Linux a través de Compose Multiplatform, compartiendo la misma base de código que la aplicación de Android. Nuevos flujos de incorporación suavizan la experiencia para usuarios nuevos de Nostr.

**Nostur v1.25.3** - El cliente de iOS y macOS [se enfoca en la mensajería privada](https://github.com/nostur-com/nostur-ios-public/releases) con mejoras de [NIP-17](/es/topics/nip-17/). Las conversaciones de DM ahora soportan reacciones y respuestas, trayendo la interactividad de las publicaciones públicas a los mensajes cifrados. La vista de conversación ha sido rediseñada con mejor threading para que los intercambios de múltiples mensajes sean más fáciles de seguir, y las marcas de tiempo muestran "hace tiempo" en la lista de DM para escaneo rápido. Los usuarios de escritorio obtienen diseños de múltiples columnas para ver múltiples feeds o conversaciones lado a lado. El soporte de firmante remoto [NIP-46](/es/topics/nip-46/) permite a los usuarios mantener sus claves privadas en aplicaciones de firmante dedicadas como Amber o nsec.app. Correcciones adicionales restauran la funcionalidad de DM en iOS 15 e iOS 16, resuelven retrasos en notificaciones y añaden la capacidad de configurar qué relays reciben los DMs publicados.

## Cambios notables de código y documentación

*Estos son pull requests abiertos y trabajo en etapa temprana, perfectos para obtener retroalimentación antes de que se fusionen. Si algo te llama la atención, considera revisar o comentar.*

### Citrine (Relay de Android)

[PR #89](https://github.com/greenart7c3/Citrine/pull/89) corrige una vulnerabilidad de inyección SQL en la aplicación de relay personal de Android. El problema permitía que datos de eventos malformados ejecutaran consultas de base de datos arbitrarias, un fallo serio para cualquier aplicación que almacena y procesa entrada no confiable. La corrección sanitiza correctamente todas las operaciones de base de datos usando consultas parametrizadas. Aún no se ha etiquetado ningún lanzamiento, por lo que los usuarios necesitarán esperar la próxima versión o compilar desde el código fuente. [PR #90](https://github.com/greenart7c3/Citrine/pull/90) optimiza el rendimiento de consultas de ContentProvider con filtrado a nivel de base de datos y paginación, reduciendo la latencia cuando aplicaciones externas como Amethyst acceden a la base de datos de eventos de Citrine a través de la capa de comunicación entre procesos de Android.

### rust-nostr (Biblioteca)

El soporte de [NIP-62](/es/topics/nip-62/) (Solicitudes de Desvanecimiento) se está expandiendo a través de los backends de base de datos de rust-nostr. [PR #1180](https://github.com/rust-nostr/nostr/pull/1180), fusionado hace dos semanas, añadió soporte de NIP-62 a SQLite, manejando solicitudes de desvanecimiento `ALL_RELAYS` ya que la capa de base de datos no conoce URLs de relay específicas. [PR #1210](https://github.com/rust-nostr/nostr/pull/1210) extiende esto al backend LMDB, asegurando que las solicitudes de desvanecimiento se persistan en disco y sobrevivan a reinicios del relay. Una implementación de IndexedDB para entornos de navegador también está en progreso. Juntos, estos cambios dan a los desarrolladores soporte consistente de NIP-62 a través de SQLite, LMDB y pronto almacenamiento del navegador.

### NDK (Nostr Development Kit)

[PR #375](https://github.com/nostr-dev-kit/ndk/pull/375) corrige un error en el sistema de seguimiento de seenEvents. El problema causaba que ciertos patrones de suscripción marcaran incorrectamente eventos como ya vistos, llevando a contenido perdido cuando los usuarios abrían nuevas suscripciones o se reconectaban a relays. La corrección asegura que los eventos se rastreen con precisión a través de los ciclos de vida de las suscripciones, lo cual es particularmente importante para aplicaciones que se suscriben y desuscriben dinámicamente basándose en la navegación del usuario. NDK se actualizó a beta.70 con esta corrección incluida.

### Damus (iOS)

[PR #3515](https://github.com/damus-io/damus/pull/3515) corrige un fallo de inicio que afectaba a usuarios de iOS 17. El problema provenía de un desbordamiento aritmético en `NdbUseLock`, una clase de respaldo usada porque los Swift Mutexes no están disponibles en iOS 17. La corrección reemplaza el enfoque de sincronización anterior con `NSLock`, que está disponible en iOS 17 y maneja las condiciones de carrera restantes correctamente. Los usuarios de iOS 18+ no estaban afectados ya que tienen acceso a la implementación nativa de Swift Mutex.

Por separado, un lote de mejoras para artículos de formato largo llegó via [PR #3509](https://github.com/damus-io/damus/pull/3509). Las barras de progreso de lectura rastrean tu posición a través de los artículos, los tiempos estimados de lectura aparecen en las vistas previas, y el modo sepia con ajustes de altura de línea configurables proporcionan una lectura más cómoda. El modo de enfoque oculta automáticamente la navegación al desplazarse hacia abajo y la restaura al tocar, reduciendo el desorden visual para una lectura sin distracciones. Varias correcciones abordan la visualización de imágenes en contenido markdown y aseguran que los artículos se abran al principio en lugar de a mitad de camino.

### Zap.stream (Transmisión en Vivo)

La integración de chat de YouTube y Kick conecta mensajes de plataformas de streaming externas a Nostr. Los streamers que transmiten simultáneamente a YouTube, Kick y Zap.stream ahora pueden ver todos los mensajes de chat en una vista unificada, con mensajes de cada plataforma apareciendo junto a los comentarios nativos de Nostr. Esto elimina un punto de fricción importante para creadores que quieren usar Nostr para streaming pero no pueden abandonar audiencias en plataformas establecidas. La integración muestra de qué plataforma se originó cada mensaje y maneja el flujo de autenticación para conectar cuentas externas.

### Chachi (Grupos NIP-29)

El cliente de chat grupal [NIP-29](/es/topics/nip-29/) envió seis PRs fusionados esta semana. Una actualización de seguridad aborda [CVE-2026-22029](https://github.com/purrgrammer/chachi/pull/89), una vulnerabilidad XSS en react-router que podría habilitar ataques de redirección abierta; la corrección actualiza a react-router-dom 6.30.0. [PR #92](https://github.com/purrgrammer/chachi/pull/92) añade carga paginada de mensajes para chats grupales, para que las conversaciones largas se carguen incrementalmente en lugar de todas a la vez. [PR #91](https://github.com/purrgrammer/chachi/pull/91) corrige varios errores de NIP-29 incluyendo una condición de carrera que causaba nombres de grupo en blanco en la carga inicial y listas de participantes indefinidas que hacían fallar las vistas de miembros. La cobertura de traducción ahora abarca los 31 idiomas soportados con 1060 claves cada uno.

### 0xchat (Mensajería)

El cliente de mensajería estilo Telegram mejoró el cumplimiento de [NIP-55](/es/topics/nip-55/) al guardar correctamente los nombres de paquetes de firmantes cuando se usan aplicaciones de firma externas, corrigiendo problemas donde la aplicación perdía el rastro de qué firmante usar después de reinicios. El manejo de respuestas NIP-17 ahora incluye correctamente la etiqueta `e` para threading, asegurando que las respuestas aparezcan en el contexto de conversación correcto entre clientes. Las optimizaciones de rendimiento abordan el lag de desplazamiento en listas de mensajes, un punto de dolor común al cargar historiales de chat largos. El autoguardado de borradores previene la pérdida de mensajes si navegas lejos a mitad de composición, y las opciones de almacenamiento de archivos ahora incluyen endpoints predeterminados de FileDropServer y BlossomServer.

### Primal (iOS)

El soporte de firmante remoto [NIP-46](/es/topics/nip-46/) llega a iOS via [PR #184](https://github.com/PrimalHQ/primal-ios-app/pull/184), completando el despliegue multiplataforma que comenzó con Android hace varias semanas. Los usuarios ahora pueden mantener sus claves privadas en servicios bunker dedicados como nsec.app o instancias de nsecBunker autoalojadas, conectándose a través de relays de Nostr para firmar eventos sin exponer las claves a la aplicación cliente. Esta separación mejora la postura de seguridad para usuarios que quieren usar las características de Primal mientras mantienen prácticas de gestión de claves más estrictas. La implementación incluye escaneo de códigos QR para URIs de conexión bunker y maneja el flujo de solicitud/respuesta de NIP-46 sobre mensajes cifrados de relay.

---

Eso es todo por esta semana. ¿Estás construyendo algo? ¿Tienes noticias para compartir? ¿Quieres que cubramos tu proyecto? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Contáctanos via DM de NIP-17</a> o encuéntranos en Nostr.
