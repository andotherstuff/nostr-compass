---
title: 'Nostr Compass #11'
date: 2026-02-25
translationOf: /en/newsletters/2026-02-25-newsletter.md
translationDate: 2026-02-25
draft: false
type: newsletters
---

Bienvenido de nuevo a Nostr Compass, tu guía semanal de Nostr.

**Esta semana:** [White Noise v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0) trae mensajería en tiempo real y soporte para el firmante Amber con más de 160 mejoras fusionadas. [diVine 1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5) corrige problemas de reproducción de vídeo y añade eventos de visualización Kind 22236 para análisis de creadores. [Pika](https://github.com/sledtools/pika), [Ridestr](https://github.com/variablefate/ridestr) y [Unfiltered](https://github.com/dmcarrington/unfiltered) lanzan actualizaciones. [FIPS](https://github.com/jmcorgan/fips) lanza una implementación en Rust funcional de redes de malla nativas de Nostr. Notecrumbs recibe correcciones de estabilidad para las vistas previas de enlaces de damus.io. [ContextVM](https://contextvm.org) conecta Nostr con el Model Context Protocol. Los nuevos proyectos incluyen [Burrow](https://github.com/CentauriAgent/burrow) para mensajería cifrada con MLS entre agentes de IA y humanos, y [Nostria Signer](https://github.com/nostria-app/nostria-signer-extension) para gestión de bóveda e identidad basada en navegador. Los análisis profundos cubren la firma Android de NIP-55 y la sincronización de billeteras Cashu de NIP-60.

## Noticias

### Mejoras de Estabilidad en Notecrumbs

[Notecrumbs](https://github.com/damus-io/notecrumbs), la API de Nostr y servidor web que impulsa las vistas previas de enlaces de damus.io, recibió una serie de correcciones que abordan problemas de confiabilidad.

Una [corrección de concurrencia](https://github.com/damus-io/notecrumbs/commit/3f201f63ea49) reemplazó el mecanismo de deduplicación en vuelo con canales watch. Dos llamantes que solicitaban la misma nota podían convertirse ambos en buscadores, llevando a un bloqueo cuando uno completaba antes de que el otro se suscribiera a la notificación. Los canales watch con operaciones atómicas aseguran que solo un buscador se ejecute mientras otros esperan el resultado.

La [limitación de tasa](https://github.com/damus-io/notecrumbs/commit/b0d0bf5a2f17) implementa una defensa de dos capas contra el martilleo de relays. Cuando los usuarios acceden repetidamente a la misma nota, el sistema ahora aplica debounce a las solicitudes de relay con una ventana de enfriamiento de 5 minutos. Esta protección se extiende a todos los tipos de [NIP-19](/es/topics/nip-19/) y feeds de perfil, previniendo spam proporcional a los relays durante tráfico intenso.

El commit de [mejoras de rendimiento](https://github.com/damus-io/notecrumbs/commit/38670b3972b6) movió las búsquedas de datos secundarios a tareas tokio en segundo plano. Las páginas ahora se renderizan instantáneamente con datos en caché en lugar de bloquearse en tiempos de espera secuenciales de relay que podían sumar hasta 7.5 segundos. Una actualización a nostrdb 0.10.0 acompañó estas correcciones.

### ContextVM: MCP sobre Nostr

[ContextVM](https://contextvm.org) es un conjunto de herramientas que conectan Nostr y el [Model Context Protocol](https://modelcontextprotocol.io/) (MCP). Commits recientes han introducido la nueva especificación [CEP-8](https://docs.contextvm.org/spec/ceps/cep-8/) que habilita pagos, y han estado impulsando mejoras del [SDK](https://github.com/ContextVM/sdk) durante febrero.

El SDK proporciona transportes de cliente y servidor TypeScript para MCP sobre Nostr. Los desarrolladores pueden exponer servidores MCP a través de la red Nostr y los clientes pueden conectarse a ellos. Los relays actúan como un bus de mensajes ciego, solo enrutando eventos cifrados ciegamente. Los clientes sin soporte nativo de Nostr se conectan a través de una capa proxy. La biblioteca maneja la gestión de relays y la firma criptográfica para autenticación de eventos. Funciona tanto en entornos Node.js como de navegador.

[CVMI](https://github.com/ContextVM/cvmi) proporciona un CLI para descubrimiento de servidores e invocación de métodos. [Relatr](https://github.com/ContextVM/relatr) calcula puntuaciones de confianza personalizadas a partir de la distancia del grafo social combinada con validación de perfil.

ContextVM se posiciona como una capa puente: los servidores MCP existentes obtienen interoperabilidad con Nostr mientras mantienen sus transportes convencionales.

### White Noise Documenta la Búsqueda Descentralizada de Usuarios

Una [publicación de blog de jgmontoya](https://blog.jgmontoya.com/2026/02/22/user-search.html) detalla cómo [White Noise](https://github.com/marmot-protocol/whitenoise) maneja la búsqueda de usuarios a través de la red descentralizada de relays.

La distribución de perfiles crea el desafío: a diferencia de los mensajeros centralizados con bases de datos unificadas, los perfiles de Nostr se dispersan a través de docenas de relays sin índice central. White Noise resuelve esto mediante una arquitectura productor-consumidor que se ejecuta en paralelo.

Un proceso productor expande continuamente el grafo social hacia afuera desde los follows del usuario, obteniendo listas de follows a distancias crecientes y encolando pubkeys descubiertas para resolución de perfil. El consumidor resuelve coincidencias a través de cinco niveles de costo creciente: tabla de usuarios local (más rápido), perfiles en caché de búsquedas anteriores, relays conectados, listas de relays de usuario por [NIP-65](/es/topics/nip-65/), y consultas directas a relays declarados por el usuario (más lento).

Búsquedas en frío toman aproximadamente 3 segundos mientras que búsquedas en caliente desde caché bajan a alrededor de 10 milisegundos. Para nuevos usuarios sin grafos sociales establecidos, el sistema inyecta nodos bootstrap bien conectados para asegurar la funcionalidad de búsqueda. La membresía de grupo proporciona una señal social implícita junto a los follows explícitos.

La instrumentación resultó crítica para la optimización, señala el autor. Sin métricas, las mejoras eran conjeturas.

### FIPS: Redes de Malla Nativas de Nostr

[FIPS](https://github.com/jmcorgan/fips) (Free Internetworking Peering System) es una implementación Rust funcional de una red de malla auto-organizada que usa pares de claves Nostr (secp256k1) como identidades de nodo. La [documentación de diseño](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md) acompaña al código funcional.

El protocolo aborda la independencia de infraestructura: los nodos se descubren entre sí automáticamente sin servidores centrales o autoridades de certificados. Un árbol de expansión proporciona enrutamiento basado en coordenadas mientras los filtros bloom propagan información de alcanzabilidad, permitiendo a los nodos tomar decisiones de reenvío con solo conocimiento local. El agnosticismo de transporte significa que el mismo protocolo funciona sobre UDP, Ethernet, Bluetooth, radio LoRa, o cualquier medio capaz de datagramas.

Dos capas de cifrado protegen el tráfico. El cifrado de capa de enlace (patrón Noise IK) asegura la comunicación salto a salto entre vecinos con autenticación mutua y secreto hacia adelante. El cifrado de capa de sesión (patrón Noise XK) proporciona protección de extremo a extremo contra enrutadores intermedios, donde solo el destino puede descifrar la carga útil. Esto imita cómo TLS protege el tráfico HTTP incluso al atravesar redes no confiables.

La arquitectura usa un árbol de expansión de "incrustación codiciosa" para enrutamiento. Cada nodo recibe coordenadas basadas en su posición relativa a la raíz del árbol y el padre. Los paquetes se enrutan codiciosamente hacia coordenadas más cercanas al destino, con filtros bloom anunciando puntos finales alcanzables. Cuando el enrutamiento codicioso falla (mínimos locales), los nodos pueden recurrir a rutas basadas en árbol.

La implementación Rust ya incluye transporte UDP con descubrimiento de filtro bloom. El trabajo futuro se dirige a la integración de relays Nostr para arranque de pares.

## Lanzamientos

Esta semana trajo lanzamientos a través de infraestructura de relay y aplicaciones cliente, con nuevos proyectos también entrando al espacio.

### HAVEN v1.2.0

[HAVEN](https://github.com/bitvora/haven), el relay personal todo-en-uno que agrupa cuatro funciones de relay con un servidor de medios [Blossom](/es/topics/blossom/), lanzó [v1.2.0](https://github.com/bitvora/haven/releases/tag/v1.2.0). Este lanzamiento va más allá de la etapa RC [cubierta la semana pasada](/es/newsletters/2026-02-18-newsletter/#haven-v120-rc3).

El soporte multi-npub permite que una sola instancia de HAVEN sirva a varias identidades Nostr mediante lista blanca, con nueva funcionalidad de lista negra para control de acceso. Un sistema de respaldo reescrito usa formato JSONL portable, con un comando `haven restore` para importar notas desde archivos JSONL. La integración de almacenamiento en la nube añade banderas `--to-cloud` y `--from-cloud` para gestión de respaldo remoto.

Mejoras de [Web of Trust](/es/topics/web-of-trust/) incluyen niveles de profundidad configurables para cálculos de confianza e intervalos de actualización automática de 24 horas con optimización sin bloqueos que reduce la sobrecarga de memoria. Configuración de user-agent para solicitudes de relay y ajustes de timeout de Blastr configurables completan el lanzamiento, junto a exportación de datos a JSONL comprimido.

### White Noise v0.3.0

[White Noise](https://github.com/marmot-protocol/whitenoise), la app de mensajería cifrada basada en [MLS](/es/topics/mls/) que implementa el protocolo [Marmot](/es/topics/marmot/), lanzó [v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0) con más de 160 mejoras fusionadas.

Este lanzamiento trae mensajería en tiempo real mediante conexiones de streaming en lugar de sondeo, por lo que los mensajes llegan instantáneamente. El soporte para Amber ([NIP-55](/es/topics/nip-55/)) significa que las claves privadas nunca necesitan tocar la app. Compartir imágenes ahora funciona con seguimiento de progreso de subida y marcadores de posición blurhash mientras carga. La visualización a pantalla completa soporta pellizcar para hacer zoom.

Mensajería grupal recibió mejoras de confiabilidad con listas de chat mostrando nombres de remitentes y cifrado [MLS](/es/topics/mls/) asegurando secreto hacia adelante. La búsqueda de usuarios se expande hacia afuera desde los follows hasta cuatro grados de separación con resultados llegando en streaming a medida que se encuentran.

Un cambio disruptivo reinicia todos los datos locales al actualizar debido a cambios en el protocolo Marmot y el cambio a almacenamiento local cifrado. Los usuarios deben respaldar claves nsec antes de actualizar.

### diVine 1.0.5

[diVine](https://github.com/divinevideo/divine-mobile), el cliente de vídeo corto en bucle construido sobre archivos restaurados de Vine, lanzó [1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5) con extensas correcciones de reproducción de vídeo y un nuevo sistema de análisis descentralizado.

Los problemas de reproducción de vídeo dominaron las correcciones: pausa fantasma, audio dual entre vídeos, destello negro entre miniaturas y primeros fotogramas, y crashes de reproductor desechado están todos resueltos. Un reproductor de vídeo agrupado ahora maneja el feed de Inicio para reproducción consistente.

Eventos de visualización efímeros Kind 22236 habilitan análisis de creadores y recomendaciones. El sistema rastrea fuentes de tráfico junto a conteos de bucles mientras filtra auto-visualizaciones. Fugas de ruta de archivo local en etiquetas imeta de evento Nostr se corrigen con URLs canónicas de Blossom construidas en el lado del cliente por especificación BUD-01.

Mejoras de firmante remoto [NIP-46](/es/topics/nip-46/) incluyen conexiones de relay paralelizadas y soporte de URL de callback. Android reconecta conexiones WebSocket al reanudar la app después de aprobación del firmante.

### Coracle 0.6.30

[Coracle](https://github.com/coracle-social/coracle), el cliente Nostr basado en web enfocado en gestión de relay y moderación de [Web of Trust](/es/topics/web-of-trust/), lanzó [0.6.30](https://github.com/coracle-social/coracle/releases/tag/0.6.30) con soporte de miniaturas de vídeo, mejorando la navegación de medios en feeds.

### Nostur v1.26.0

[Nostur](https://github.com/nostur-com/nostur-ios-public), el cliente Nostr para iOS, lanzó [v1.26.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.26.0) con una nueva sección de feed de Transmisiones en Vivo y una pantalla de Ajustes rediseñada. Los GIFs ahora pueden alojarse en servidores de medios Blossom, reduciendo la dependencia de servicios centralizados. La integración de GIFs de Klipy proporciona respaldo cuando Tenor no está disponible. Encabezados de año en conversaciones de DM y visualización de conteo de menciones completan los cambios de cara al usuario.

Herramientas de desarrollador y apps CLI también recibieron actualizaciones esta semana.

### nak v0.18.5

[nak](https://github.com/fiatjaf/nak), la navaja suiza de línea de comandos de fiatjaf para Nostr, lanzó [v0.18.5](https://github.com/fiatjaf/nak/releases/tag/v0.18.5) con un nuevo subcomando `nak profile` para obtener y mostrar perfiles de usuario. El comando `git clone` ahora soporta nombres [NIP-05](/es/topics/nip-05/) en URIs `nostr://`, habilitando clonación de repositorios por identificadores legibles por humanos.

### Pika v0.5.3

[Pika](https://github.com/sledtools/pika), el mensajero cifrado con [MLS](/es/topics/mls/) para iOS, Android y escritorio construido sobre el protocolo [Marmot](/es/topics/marmot/), lanzó [v0.5.3](https://github.com/sledtools/pika/releases/tag/pikachat-v0.5.3). Commits recientes añaden subida de archivos y soporte de medios de arrastrar y soltar a la app de escritorio, junto a correcciones de despliegue en Cloudflare Workers.

Pika usa un núcleo Rust que posee toda la lógica de negocio mientras iOS (SwiftUI) y Android (Kotlin) actúan como capas delgadas de UI renderizando instantáneas de estado. MDK (Marmot Development Kit) proporciona la implementación MLS. El proyecto señala estado alfa y advierte contra uso para cargas de trabajo sensibles.

### Ridestr v0.2.6

[Ridestr](https://github.com/variablefate/ridestr), la plataforma descentralizada de viajes compartidos con pagos Cashu, lanzó [v0.2.6](https://github.com/variablefate/ridestr/releases/tag/v0.2.6). Este lanzamiento corrige problemas de accesibilidad de TalkBack y resuelve bugs donde los conductores desaparecían de la lista cercana al cambiar métodos de pago o donde los conteos de conductor seleccionado no se actualizaban cuando los conductores se desconectaban.

La función "Send to All" ahora es "Broadcast RoadFlare" con correcciones para fallos silenciosos en instalaciones frescas de conductor. Ridestr implementa escrow HTLC para pagos de viaje sin confianza y sincronización de billetera [NIP-60](/es/topics/nip-60/) entre dispositivos.

### Unfiltered v1.0.6

[Unfiltered](https://github.com/dmcarrington/unfiltered), la app de compartir fotos estilo Instagram para Android, lanzó [v1.0.6](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.6) con búsqueda mejorada de usuarios y reconexión automática de relay cada 60 segundos.

Construido con Kotlin y Jetpack Compose, Unfiltered usa bindings de rust-nostr y servidores compatibles con Blossom para alojamiento de imágenes. La integración con Amber ([NIP-55](/es/topics/nip-55/)) maneja la gestión segura de claves. La app muestra publicaciones de cuentas seguidas en orden cronológico sin algoritmos ni anuncios.

Dos nuevos proyectos de mensajería y firma también se lanzaron esta semana.

### Burrow: Mensajería MLS para Agentes de IA

[Burrow](https://github.com/CentauriAgent/burrow) es un mensajero que implementa el protocolo [Marmot](/es/topics/marmot/) para comunicación cifrada con MLS sin números de teléfono ni servidores centralizados. Tanto usuarios humanos como agentes de IA pueden participar.

Un daemon CLI de Rust puro con modo de salida JSONL maneja la integración con sistemas automatizados. Una app Flutter multiplataforma cubre Android, iOS, Linux, macOS y Windows. Los adjuntos de medios se cifran junto a los mensajes, y WebRTC maneja llamadas de audio y vídeo con servidores TURN configurables.

Burrow superpone cifrado MLS sobre infraestructura Nostr. La identidad usa pares de claves Nostr (secp256k1) mientras los KeyPackages MLS se publican como eventos kind 443. Los mensajes se cifran con [NIP-44](/es/topics/nip-44/) como eventos kind 445, y las invitaciones de bienvenida usan gift-wrapping de [NIP-59](/es/topics/nip-59/).

Integración con [OpenClaw](https://openclaw.ai) habilita la participación de agentes de IA con acceso completo a herramientas. Listas de control de acceso con registro de auditoría gestionan permisos de contactos y grupos. Esta combinación posiciona a Burrow para escenarios de mensajería agente-a-agente y agente-a-humano que requieren cifrado de nivel Signal sobre infraestructura descentralizada.

### Extensión Nostria Signer

[Nostria Signer](https://github.com/nostria-app/nostria-signer-extension) es una extensión de navegador basada en Chromium que proporciona gestión de bóveda e identidad para usuarios de Nostr.

Múltiples bóvedas conteniendo múltiples cuentas permiten a los usuarios organizar identidades para diferentes contextos. La internacionalización incluye soporte de idiomas RTL. Construido con Angular y TypeScript (79.2% del código), funciona tanto como extensión de navegador como Aplicación Web Progresiva.

Nostria Signer implementa [NIP-07](/es/topics/nip-07/) para firma de extensión de navegador, habilitando a clientes Nostr basados en web solicitar firmas de eventos sin acceder directamente a claves privadas. Migración automática de billetera maneja actualizaciones distribuidas a través de la Chrome Web Store. Los usuarios también pueden cargar lateralmente desde la carpeta `dist/extension`.

Los desarrolladores enfatizan el estado experimental: los usuarios deben gestionar sus propias frases de recuperación secreta ya que los desarrolladores no pueden restaurar acceso a claves perdidas.

## Actualizaciones de Proyectos

### Formstr Migra a Nueva Organización

[Formstr](https://github.com/formstr-hq/nostr-forms), la alternativa a Google Forms en Nostr, migró su repositorio de `abh3po/nostr-forms` a la organización `formstr-hq`. Este receptor de beca OpenSats continúa desarrollo en la nueva ubicación.

### PRs Abiertos Notables

Trabajo en progreso a través de proyectos Nostr:

- **Modelo Outbox de Damus** ([PR #3602](https://github.com/damus-io/damus/pull/3602)): Plan de implementación para el modelo de relay gossip/outbox en iOS. Este cambio arquitectónico mejora la entrega de mensajes publicando a los relays donde los destinatarios realmente leen.

- **Notificaciones Multiplataforma de Notedeck** ([PR #1296](https://github.com/damus-io/notedeck/pull/1296)): Sistema de notificaciones nativo para el cliente de escritorio Damus cubriendo FCM de Android, macOS y Linux.

- **Actualización Cashu v3 de NDK** ([PR #370](https://github.com/nostr-dev-kit/ndk/pull/370)): Actualiza la integración de billetera del Nostr Development Kit a cashu-ts v3.

- **Cashu Offline de Zeus** ([PR #3742](https://github.com/ZeusLN/zeus/pull/3742)): Envío y recepción de ecash offline para la billetera Lightning Zeus.

- **Entrega Digital Cifrada de Shopstr** ([PR #231](https://github.com/shopstr-eng/shopstr/pull/231)): Añade entrega cifrada para bienes digitales con soporte de peso dinámico para artículos físicos.

## Actualizaciones de NIPs

Cambios recientes al [repositorio de NIPs](https://github.com/nostr-protocol/nips):

**Fusionados Esta Semana:**

- **[Descubribilidad de Proveedor de Servicio NIP-85](https://github.com/nostr-protocol/nips/pull/2223)**: La especificación de [NIP-85](/es/topics/nip-85/) ahora incluye orientación sobre cómo los clientes descubren proveedores de aserciones de confianza. Cuando un cliente necesita puntuaciones de [Web of Trust](/es/topics/web-of-trust/) u otras métricas computadas, puede consultar relays por anuncios kind 30085 de proveedores que el usuario ya sigue o confía.

- **[NIP-29 Elimina Grupos No Gestionados](https://github.com/nostr-protocol/nips/pull/2229)**: La especificación de chat grupal de [NIP-29](/es/topics/nip-29/) eliminó el soporte para grupos no gestionados (donde cualquier miembro podía añadir a otros). Todos los grupos NIP-29 ahora requieren gestión del lado del relay con roles de admin explícitos, simplificando implementaciones y reduciendo vectores de spam.

- **[NIP-11 Elimina Campos Deprecados](https://github.com/nostr-protocol/nips/pull/2231)**: Los documentos de información de relay de [NIP-11](/es/topics/nip-11/) ya no incluyen los campos deprecados `software` y `version`. Las implementaciones deberían eliminarlos de sus respuestas.

- **[NIP-39 Mueve Etiquetas de Identidad](https://github.com/nostr-protocol/nips/pull/2227)**: Reclamaciones de identidad externa (etiquetas `i` de [NIP-39](/es/topics/nip-39/) para GitHub, Twitter, etc.) se movieron de perfiles kind 0 a eventos dedicados kind 30382. Esto separa la verificación de identidad de los metadatos de perfil.

**Progreso de NIPs para Agentes de IA:**

Cuatro NIPs enfocados en IA continúan desarrollo activo. Desde la [cobertura de la semana pasada](/es/newsletters/2026-02-18-newsletter/#llegan-los-nips-para-agentes-de-ia):

- **[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220)** (actualizado 19 feb): Define identidad de agente con kind 4199 para definiciones de agente y kind 4201 para prompting ("nudges"). Los agentes pueden referenciar metadatos de archivo [NIP-94](/es/topics/nip-94/) para descripciones extendidas.

- **[NIP-XX: AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226)** (actualizado 18 feb): Estandariza mensajería conversacional con siete kinds de evento efímeros (25800-25806) para estado, deltas de streaming, prompts, respuestas, llamadas de herramientas, errores y cancelación. Eventos "AI Info" kind 31340 permiten a los agentes anunciar modelos y capacidades soportadas.

- **[NIP-AC: DVM Agent Coordination](https://github.com/nostr-protocol/nips/pull/2228)** (abierto 18 feb): Extiende [NIP-90](/es/topics/nip-90/) para flujos de trabajo de agentes autónomos. Añade latidos para descubrimiento de agentes, revisiones de trabajos para seguimiento de calidad, escrow de datos para compromiso de resultados, cadenas de flujo de trabajo para pipelines de múltiples pasos, y licitación de enjambre para selección competitiva de proveedores. Una implementación de referencia corre en 2020117.xyz.

- **[NIP-AD: MCP Server Announcements](https://github.com/nostr-protocol/nips/pull/2221)** (abierto 12 feb): Estandariza el anuncio de servidores y habilidades del Model Context Protocol en Nostr. Ya en uso en la plataforma TENEX.

**Otros PRs Abiertos:**

- **[NIP-144: Service Authorization Protocol](https://github.com/nostr-protocol/nips/pull/2232)**: Define cómo los clientes prueban identidad y permisos a proveedores de servicio en Nostr.

- **[NIP-DC: Nostr Webxdc](https://github.com/nostr-protocol/nips/pull/2230)**: alexgleason propone integrar Webxdc (aplicaciones web descentralizadas) con eventos Nostr.

## Análisis Profundo de NIP: NIP-55 (Aplicación Firmante de Android)

[NIP-55](https://github.com/nostr-protocol/nips/blob/master/55.md) define cómo los clientes Nostr de Android solicitan operaciones criptográficas de aplicaciones firmantes dedicadas. Con [White Noise v0.3.0](#white-noise-v030) y [Unfiltered v1.0.6](#unfiltered-v106) ambos añadiendo soporte para Amber esta semana, el protocolo de firma Android merece examen.

**Canales de Comunicación:**

NIP-55 habilita firma entre apps mediante dos mecanismos. Intents proporcionan aprobación manual del usuario con retroalimentación visual para operaciones de una sola vez. Content Resolvers habilitan firma automatizada cuando los usuarios otorgan permisos persistentes, permitiendo a las apps firmar en segundo plano sin solicitudes repetidas.

La comunicación usa el esquema URI personalizado `nostrsigner:`. Un cliente inicia contacto con:

```
nostrsigner:<base64-encoded-event>?type=sign_event&callbackUrl=myapp://callback
```

**Operaciones Soportadas:**

La especificación define siete métodos criptográficos: firma de eventos (`sign_event`), recuperación de clave pública (`get_public_key`), cifrado/descifrado [NIP-04](/es/topics/nip-04/), cifrado/descifrado [NIP-44](/es/topics/nip-44/), y descifrado de evento zap (`decrypt_zap_event`).

**Modelo de Permisos:**

Los clientes llaman a `get_public_key` una vez para establecer una relación de confianza, recibiendo el nombre de paquete del firmante y la pubkey del usuario. La especificación manda que los clientes guarden estos valores y nunca llamen a `get_public_key` de nuevo, previniendo ataques de fingerprinting.

Para solicitudes de firma, los usuarios pueden aprobar una vez u otorgar "recordar mi elección" para operaciones en segundo plano. Si los usuarios rechazan consistentemente operaciones, el firmante retorna un estado "rechazado", previniendo solicitudes repetidas.

**Implementaciones:**

[Amber](https://github.com/greenart7c3/amber) es el firmante NIP-55 principal para Android. Los clientes que soportan NIP-55 incluyen [Amethyst](https://github.com/vitorpamplona/amethyst), [White Noise](#white-noise-v030), [Unfiltered](#unfiltered-v106), y otros. Aplicaciones web no pueden recibir directamente respuestas del firmante y deben usar URLs de callback u operaciones de portapapeles.

**Relación con Otros NIPs de Firma:**

NIP-55 complementa [NIP-07](/es/topics/nip-07/) (extensiones de navegador) y [NIP-46](/es/topics/nip-46/) (firma remota sobre relays). Donde NIP-07 maneja navegadores de escritorio y NIP-46 maneja firma entre dispositivos, NIP-55 proporciona integración Android nativa con latencia mínima.

## Análisis Profundo de NIP: NIP-60 (Billetera Cashu)

[NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md) define cómo las billeteras ecash de [Cashu](/es/topics/cashu/) almacenan estado en relays Nostr, habilitando sincronización de billetera entre aplicaciones. Con [Ridestr v0.2.6](#ridestr-v026) usando NIP-60 para sincronización de billetera entre dispositivos, el protocolo merece examen.

**Kinds de Evento:**

NIP-60 usa cuatro tipos de evento. El kind reemplazable 17375 almacena configuración de billetera incluyendo URLs de mint y una clave privada dedicada para recibir pagos ecash P2PK. Eventos de token (kind 7375) contienen pruebas criptográficas no gastadas, mientras el historial de gastos (kind 7376) registra transacciones para transparencia del usuario. Un kind opcional 7374 rastrea cotizaciones de pago de mint.

**Arquitectura de Billetera:**

El estado de la billetera vive en relays, haciéndolo accesible entre aplicaciones. El evento de billetera de un usuario contiene referencias cifradas a mints Cashu y una clave privada específica de billetera separada de la identidad Nostr del usuario. Esta separación importa: la clave de billetera maneja operaciones ecash mientras la clave Nostr maneja funciones sociales.

```json
{
  "kind": 17375,
  "content": "<configuración-de-billetera-cifrada-nip44>",
  "tags": [["d", "cashu-wallet"]]
}
```

**Gestión de Pruebas:**

Pruebas Cashu son instrumentos al portador. Una vez gastada, una prueba se vuelve inválida. NIP-60 gestiona esto mediante un mecanismo de rollover: al gastar, los clientes crean un nuevo evento de token con pruebas no gastadas restantes y eliminan el original via [NIP-09](/es/topics/nip-09/). IDs de token destruidos van en un campo `del` para seguimiento de estado.

Los clientes deberían validar periódicamente pruebas contra mints para detectar credenciales previamente gastadas. Se permiten múltiples eventos de token por mint, y los eventos de historial de gastos ayudan a los usuarios rastrear transacciones aunque son opcionales.

**Modelo de Seguridad:**

Todos los datos sensibles usan cifrado [NIP-44](/es/topics/nip-44/). La clave privada de billetera nunca aparece en texto plano. Como los relays almacenan blobs cifrados sin entender sus contenidos, el estado de la billetera permanece privado incluso en relays no confiables.

**Implementaciones:**

Billeteras que soportan NIP-60 incluyen [Nutsack](https://github.com/gandlafbtc/nutsack) y [eNuts](https://github.com/cashubtc/eNuts). Clientes como [Ridestr](#ridestr-v026) usan NIP-60 para sincronización entre dispositivos, permitiendo a los usuarios recargar en escritorio y gastar desde móvil sin transferencias manuales.

---

Eso es todo por esta semana. Estás construyendo algo o tienes noticias que compartir. <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Escríbenos vía DM [NIP-17](/es/topics/nip-17/)</a> o encuéntranos en Nostr.
