---
title: 'Nostr Compass #29'
date: 2026-07-01
publishDate: 2026-07-01
translationOf: /en/newsletters/2026-07-01-newsletter.md
translationDate: 2026-08-27
draft: false
type: newsletters
---

Bienvenidos de nuevo a Nostr Compass, vuestra guía semanal de Nostr.

**Esta semana:** [FIPS v0.4.0](#fips-v040-ships-nym-mixnet-transport-mdns-discovery-and-a-data-plane-overhaul) incorpora transporte mediante la mixnet de Nym, descubrimiento mDNS opcional en la LAN, cambio de claves sin interrupciones pese a pérdidas y una renovación del plano de datos, todo compatible a nivel de wire con v0.3.0. [Whitenoise Linux](#whitenoise-linux-surfaces-as-a-desktop-marmot-client) aparece como cliente Marmot de escritorio en Rust y Slint, con una propuesta de protocolo para trasladar los efectos de mensaje a un event kind 9 específico. [CustID v0.1.10-beta](#custid-launches-as-a-mobile-identity-vault-with-nip-46-and-nfc-challenge-flow) se lanza como bóveda de identidad móvil respaldada por hardware que actúa como firmante remoto NIP-46 y responde por NFC a desafíos de acceso físico. [myco](#myco-launches-peer-to-peer-nsite-sharing-over-the-fips-mesh) estrena el intercambio entre pares de nsites sobre la malla FIPS, con un nuevo transporte BLE L2CAP en v0.1.0. [Nostr Codex Phone](#nostr-codex-phone-launches-as-a-mobile-control-surface-for-a-local-codex-worker-over-nostr) se lanza como superficie de control para Android de un asistente de programación Codex local mediante DMs cifrados de Nostr. [La línea aún no publicada de Amethyst](#amethyst-builds-nip-89-aware-ui-a-git-repositories-feed-and-a-napplet-browser-discover-section) añade análisis de handlers de aplicaciones NIP-89, un feed de repositorios Git para NIP-34 y una sección Discover para nSites y napplets. [Notedeck](#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments) incorpora NIP-37, NIP-52 y NIP-22 en una semana. [Applesauce](#applesauce-ships-12-sub-packages-in-a-coordinated-62x-cut) publica 12 versiones coordinadas de subpaquetes con helpers nbunksec para NIP-46 y una actualización de cartera a Cashu-ts v4. [Meiso v1.4.0](#meiso-v140-ships-shared-key-collaborative-lists-that-replace-mls-for-task-sharing) incorpora listas colaborativas con clave compartida sobre el kind 35000 direccionable. El repositorio de NIPs fusionó cinco PRs, incluidos un event de roles de relay, la eliminación del límite de 65.535 bytes de NIP-44, la semántica de forks de NIP-34, los metadatos de cliente NIP-46 y un método `signevent` de NIP-86. Los análisis detallados abordan [NIP-86 (API de gestión de relays)](#nip-deep-dive-nip-86-relay-management-api) y [NIP-89 (handlers de aplicaciones recomendados)](#nip-deep-dive-nip-89-recommended-application-handlers).

---

## Historias principales

### FIPS v0.4.0 incorpora transporte por la mixnet de Nym, descubrimiento mDNS y una renovación del plano de datos

[FIPS](https://github.com/jmcorgan/fips) es una red en malla privada, autoorganizada y entre pares para Nostr, donde los nodos se descubren y enrutan tráfico sin infraestructura central. [FIPS v0.4.0](https://github.com/jmcorgan/fips/releases/tag/v0.4.0) incorpora transporte mediante la mixnet de Nym, descubrimiento mDNS opcional en la LAN, una renovación del plano de datos, cambio de claves sin interrupciones pese a la pérdida de paquetes, una TUI `fipstop` reescrita sobre un harness de snapshots de renderizado, un plano de observabilidad fuera de la ruta crítica, y nuevos objetivos de empaquetado apk para OpenWrt y flake para Nix. Todo mantiene compatibilidad a nivel de wire con v0.3.0, de modo que las mallas mixtas interoperan durante una actualización gradual. Dos nuevos transportes para el descubrimiento de peers vertebran la versión. Un nuevo [transporte saliente por la mixnet de Nym](https://github.com/jmcorgan/fips/releases/tag/v0.4.0) enruta el tráfico FIPS mediante un proxy SOCKS5 `nym-socks5-client` y lo mezcla en la red de tráfico de cobertura de [Nym](https://nymtech.net/), para impedir que observadores de nivel de enlace correlacionen qué peers de la malla se comunican. Un directorio `examples/sidecar-nostr-mixnet-relay/` demuestra un relay Nostr accesible mediante un enlace FIPS conectado de extremo a extremo a través de la mixnet. El descubrimiento mDNS / DNS-SD opcional en la LAN permite que los nodos del mismo enlace local se encuentren sin configurar direcciones ni usar STUN; anuncian y adoptan peers mediante un registro de servicio estándar cuando `node.discovery.lan.enabled: true`.

El plano de datos se rediseñó para aumentar el rendimiento de un solo nodo. El cifrado y descifrado de cada peer se ejecutan ahora en tareas worker específicas fuera del bucle de recepción, por lo que un peer ocupado no puede serializar la criptografía de todo el nodo. La ruta de envío de Linux usa generic segmentation offload y un socket UDP conectado cuando están disponibles; la ruta crítica de recepción evita las copias de buffer que antes hacía por paquete; y macOS incorpora recepción por lotes con `recvmsg_x`, equivalente al procesamiento por lotes con `recvmmsg` de Linux introducido en v0.3.0. Toda la superficie de lectura `show_*` de `fipsctl` y `fipstop` sirve ahora desde un snapshot por tick, publicado en un `ArcSwap` sin locks desde la tarea de aceptación de control, así que las consultas de operadores responden con rapidez aunque el bucle de recepción del nodo esté ocupado. Una nueva consulta `show_metrics` limitada a contadores, expuesta como `fipsctl stats metrics`, permite que Prometheus recopile métricas sin coste en la ruta crítica.

El cambio de claves de sesión FMP y FSP ya no causa interrupciones ante pérdida y reordenación de paquetes en ninguna dirección: los frames entrantes se autentican contra la sesión pendiente antes de que el cambio marcado por el bit K la promueva, de modo que un frame obsoleto o falsificado no puede desbaratar el cambio; la retransmisión del mensaje 1 de rekey queda acotada; el heartbeat que detecta enlaces caídos tiene en cuenta el rekey; y las carreras por iniciación simultánea en enlaces de alta latencia se desincronizan mediante jitter simétrico. La TUI `fipstop` se reconstruyó sobre un harness de snapshots de renderizado que compara la cuadrícula de texto exacta y el estilo de cada celda de todas las vistas con salidas preparadas del socket de control. También llegan nuevos objetivos de empaquetado: un `.apk` de OpenWrt para OpenWrt 25+ —compilado sin SDK, reutilizando la compilación cruzada `.ipk` existente y el payload del sistema de archivos instalado— y un `flake.nix` en la raíz del proyecto que compila desde el código fuente los cuatro binarios (`fips`, `fipsctl`, `fips-gateway`, `fipstop`) en Nix/NixOS con el toolchain fijado.

### Whitenoise Linux aparece como cliente Marmot de escritorio

[Whitenoise Linux](https://relay.ngit.dev/npub1ven4zk8xxw873876gx8y9g9l9fazkye9qnwnglcptgvfwxmygscqsxddfh/darkmatter-linux.git) es un cliente [Marmot](/es/topics/marmot/) de escritorio: mensajería de grupos MLS sobre relays Nostr, empaquetada como un único binario Rust con una interfaz Slint que guarda todos los secretos en una bóveda cifrada con contraseña.

El hilo más relevante de esta semana propone transportar los efectos de mensaje de Whitenoise como un event kind 9 específico que referencia el mensaje padre. El formato de wire actual añade al final del cuerpo del mensaje un marcador como `dmfx:sparkle`, lo que contamina el texto para cualquier renderer que desconozca la convención. Trasladar los efectos a su propio event mantiene limpio el texto del mensaje y abre una cuestión de diseño que afrontará toda la pila Marmot: convenciones dentro del cuerpo o events sidecar para funciones enriquecidas opcionales.

### CustID se lanza como bóveda de identidad móvil con NIP-46 y un flujo de desafíos NFC

[CustID v0.1.10-beta](https://zapstore.dev/apps/naddr1qq9rzqtdwfshxwf0wccsygqv94d2qg37755z67q9yjz6q60lcejldsc3ttak83333gjqgyvf3aqpsgqqqyf6w24n0c) es la primera beta pública de CustID, una bóveda de identidad móvil construida sobre Nostr y el protocolo SISTR. CustID almacena varias identidades Nostr en almacenamiento seguro respaldado por hardware, actúa como firmante remoto [NIP-46](/es/topics/nip-46/) para otros clientes y responde a desafíos de acceso físico y en línea mediante NFC y códigos QR.

La beta ofrece todas las funciones previstas para el firmante NIP-46 y el flujo de desafío-respuesta NFC; los flujos de acceso con pruebas de conocimiento cero quedan como objetivo futuro. Esta versión también elimina la capa keep-alive [NIP-65](/es/topics/nip-65/) en segundo plano de la app, que abría un WebSocket por perfil y por relay de lectura e ingería kinds que el cliente descartaba inmediatamente. Ahora solo se mantienen activos en segundo plano los sockets NIP-46 que transportan notificaciones de solicitudes de firma, la corrección que hace viable ejecutar CustID como bunker para otros clientes en un teléfono.

### myco se lanza para compartir nsites entre pares sobre la malla FIPS

[myco v0.1.0](https://github.com/Origami74/myco/releases/tag/v0.1.0) abrió esta semana, el 27 de junio, y alcanzó v0.1.0 el 1 de julio. myco es una app Android en Rust que instala aplicaciones de personas cercanas: intercambio entre pares de [nsites](/es/topics/nip-5a/) sobre una malla FIPS, mediante cualquier transporte que admita la malla (UDP, TCP, Tor, Bluetooth) y con funcionamiento totalmente offline. El diseño empareja directamente FIPS como sustrato de transporte con el formato de events de sitios web estáticos de NIP-5A como payload, lo que permite que una app distribuida como nsite pase entre peers de la malla sin depender de relays ni HTTP.

v0.1.0 añade una ruta de radio Bluetooth L2CAP para que dos teléfonos con FIPS instalado puedan conectarse como peers por BLE sin ninguna red, además de una prueba de velocidad por peer y el intercambio activado por NFC desde el bottom sheet Circle de la app. myco también está publicada en Zapstore para su instalación directa.

### Nostr Codex Phone se lanza como superficie de control móvil de un worker Codex local mediante Nostr

[Nostr Codex Phone v0.1.122](https://github.com/tidley/nostr-codex-phone) se lanza esta semana como cliente Android que controla un worker local del asistente de programación Codex mediante mensajes directos cifrados de Nostr. La app admite varias sesiones de repositorios, transcripción de voz, sesiones enrutadas de workers, subidas de medios a Blossom y respuestas habladas opcionales, de modo que un desarrollador que ejecute un worker Codex en casa pueda enviar solicitudes desde el teléfono allí donde este tenga acceso a relays.

El proyecto es hermano directo de [CodeDeck](/en/newsletters/2026-06-24-newsletter/#codedeck-remote-agentic-coding-over-nostr), lanzado en el número 28. Ambos llevan los flujos de programación agéntica al transporte de Nostr mediante DMs cifrados, y ambos tratan Nostr como la capa de emparejamiento y mensajería que permite a un teléfono acceder a un worker doméstico sin abrir agujeros en la red. Nostr como plano de control para agentes locales se está convirtiendo en un patrón consolidado.

### Coop Mobile publica sus primeras builds versionadas

[Coop Mobile v0.2.1](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.1) y [v0.2.2](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.2) llegaron esta semana como las primeras builds versionadas de Coop Mobile, un cliente Android de mensajes directos cifrados [NIP-17](/es/topics/nip-17/). Las dos versiones refuerzan la resistencia a fallos al analizar mensajes y manejar códigos QR, y borran todos los datos almacenados al cerrar sesión.

### Amethyst desarrolla una interfaz compatible con NIP-89, un feed de repositorios Git y una sección Discover de napplets

La rama principal de [Amethyst](https://github.com/vitorpamplona/amethyst) incorporó varias superficies nuevas esta semana. Un [feed de repositorios Git](https://github.com/vitorpamplona/amethyst/pull/3406) convierte los repos [NIP-34](/es/topics/nip-34/) en una categoría navegable del timeline de Android, filtrable por comunidad y autor, junto con un [navegador git smart-HTTP](https://github.com/vitorpamplona/amethyst/pull/3415) que lee el contenido y los commits del repo sin salir de la app. El host de napplets recibió una [sección Discover](https://github.com/vitorpamplona/amethyst/pull/3409) que enumera aplicaciones web seleccionadas, además de nSites y napplets seguidos, a partir de events de handlers [NIP-89](/es/topics/nip-89/) y events de sitios [NIP-5A](/es/topics/nip-5a/). La visualización de notas ahora [revela qué app Nostr creó un event](https://github.com/vitorpamplona/amethyst/pull/3422) mediante tags NIP-89. En sincronización, llega la [compatibilidad con negentropy NIP-77](https://github.com/vitorpamplona/amethyst/pull/3434), con reconciliación en streaming y ventanas automáticas de `created_at` para sortear los límites de resultados de los relays, reduciendo el ancho de banda necesario para mantener sincronizados grandes conjuntos locales de events con un relay.

### Buzz v0.3.38 refuerza la superficie de ataque del relay y añade selección de modelos independiente del proveedor

[Buzz v0.3.38](https://github.com/block/buzz/releases/tag/v0.3.38) refuerza la [superficie de ataque del relay](https://github.com/block/buzz/pull/1369) que Buzz expone al publicar personas, equipos, agentes gestionados y declaraciones de propietario NIP-OA como events Nostr firmados. Un relay de Buzz es un registro público de las identidades Nostr del equipo y de su estado; esta versión endurece la validación de entradas y la protección contra replay en los kinds conocidos que define Buzz. También generaliza la selección de modelos para que un equipo de Buzz pueda usar cualquier proveedor para el que Buzz disponga de adaptadores, incluido un nuevo backend Databricks AI Gateway v2.

### Notedeck implementa relays de sincronización privada NIP-37, calendario NIP-52 y comentarios NIP-22

[Notedeck](https://github.com/damus-io/notedeck), el cliente de escritorio nativo en Rust del equipo de Damus, incorporó tres implementaciones de protocolo en una semana. Los relays de sincronización privada ahora persisten como una lista [NIP-37](/es/topics/nip-37/) de kind `10013`, que separa el conjunto de relays de contenido privado del usuario de su outbox público NIP-65. El panel de calendario `horizon` lee events [NIP-52](/es/topics/nip-52/) desde nostrdb y recibió un rediseño de tres paneles. El panel `headway` añadió un modelo de event de comentarios [NIP-22](/es/topics/nip-22/) en el kind `1111`, el kind que NIP-22 define para la superficie unificada de comentarios que sustituye el encadenado de respuestas NIP-10.



### Applesauce incorpora sesiones NIP-46 nbunksec y actualiza la cartera a Cashu v4

[Applesauce](https://github.com/hzrd149/applesauce), el toolkit modular de Nostr para firmantes, relays, carteras y contenido, publicó una [versión coordinada 6.2.x](https://github.com/hzrd149/applesauce/releases) de sus subpaquetes. El paquete de firmantes obtuvo helpers para importar y exportar `nbunksec`, tratando una sesión bunker [NIP-46](/es/topics/nip-46/) como artefacto portable que puede trasladarse entre clientes. El paquete de cartera actualizó sus bindings de [Cashu](/es/topics/nip-60/) a `@cashu/cashu-ts` v4, donde los importes de proofs pasan a ser objetos de valor `Amount` y cambia la API de decodificación de tokens.

---

## Versiones etiquetadas

### mostro-core v0.14.0

[mostro-core v0.14.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.0) incorpora la siguiente iteración del protocolo de la red de intercambio P2P de dinero fiat [Mostro](/es/topics/nip-69/). La versión sucede a [v0.13.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.2) y llega junto con [mostro-cli v0.16.0](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.0), que adopta el nuevo core. Tres PRs fusionados llegaron al repositorio core esta semana; el resto de la pila —el daemon mostro y Mostro mobile— sigue la versión v0.14.0 del crate de tipos compartidos.

### ngit v2.6.1

[ngit v2.6.1](https://github.com/DanConwayDev/ngit-cli), la CLI canónica de git sobre Nostr para repositorios [NIP-34](/es/topics/nip-34/), implementa la [semántica de forks GRASP-06 de NIP-34](https://github.com/nostr-protocol/nips/pull/2395) fusionada esta semana, que sustituye el tag `personal-fork` por un tag `u` en los events de estado del repo.

### mesh-llm v0.72.0 y v0.72.1

[mesh-llm](https://github.com/Mesh-LLM/mesh-llm), el componente de inferencia de la pila ContextVM que ejecuta LLMs de código abierto tras una superficie JSON-RPC direccionable por Nostr, publicó [v0.72.0](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.0) y [v0.72.1](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.1), con una corrección para un fallo del procesamiento por lotes ante prompts individuales grandes y la migración del puente MCP para abandonar helpers obsoletos.

### Meiso v1.4.0 incorpora listas colaborativas con clave compartida que sustituyen MLS para compartir tareas

[Meiso v1.4.0](https://github.com/higedamc/meiso/releases/tag/v1.4.0) introduce un modelo de listas colaborativas con clave compartida que sustituye el anterior intercambio de tareas basado en MLS por un diseño más sencillo de events direccionables. Cada lista compartida genera una clave Nostr específica que se distribuye a sus miembros; las tareas son events direccionables de kind `35000`, identificados por `d=task-id` y con contenido autocifrado mediante [NIP-44](/es/topics/nip-44/); y los relays aplican Last-Write-Wins por tarea. El diseño renuncia al forward secrecy y a la seguridad posterior al compromiso de MLS a cambio de una implementación de cliente más sencilla y resolución de conflictos a nivel de relay.

### Cordn 0.3.2

[Cordn 0.3.2](https://github.com/Cordn-msg/cordn) incorpora una línea «more-private-coordinator» que elimina las pubkeys efímeras de remitentes al publicar mensajes de grupo y refuerza el flujo de solicitudes de ingreso frente a nuevas solicitudes obsoletas. Cordn es la pila de mensajería basada en MLS tratada en el [lanzamiento del CVM ad hoc de Cordn del número 28](/en/newsletters/2026-06-24-newsletter/#cordn-ad-hoc-cvm-a-browser-based-mls-coordinator); esta versión es la actualización correspondiente del lado del coordinador.

---

## Cambios aún no publicados

### diVine impulsa 108 PRs fusionados de pulido posterior al lanzamiento

[diVine](https://github.com/divinevideo/divine-mobile), el cliente de vídeos breves en bucle que recupera Vine, atraviesa una intensa etapa de pulido posterior al lanzamiento. El trabajo visible para Nostr esta semana es una ronda de estabilidad del flujo de conexión [NIP-46](/es/topics/nip-46/) que traslada los fallos de `nostrconnect://` a códigos de motivo estructurados.

### Zap Cooking continúa la corrección transversal de NIP-46 y la renovación del compositor

[Zap Cooking](https://github.com/zapcooking/frontend) es un cliente para compartir recetas en Nostr, donde las recetas se publican como events Nostr de formato largo. El trabajo de esta semana continúa la corrección transversal de [NIP-46](/es/topics/nip-46/) y la renovación del compositor tratadas como trabajo aún no publicado en el [número 28](/en/newsletters/2026-06-24-newsletter/#unreleased-changes).

### Conduit refuerza el flujo de anuncios y la corrección del marketplace

[Conduit](https://github.com/Conduit-BTC/conduit-mono) es un monorepo de marketplace con tres aplicaciones sobre Nostr: mercado de compradores, portal de comerciantes y creador de tiendas. El trabajo de esta semana continúa el impulso a la corrección del marketplace tratado en la [cobertura del lanzamiento del número 28](/en/newsletters/2026-06-24-newsletter/#conduit-hardens-the-marketplace-mvp-and-switches-to-its-public-relay-by-default), sobre la [oleada comercial de NIP-99](/es/topics/nip-99/) que protagonizó la vertiente de protocolo del número anterior.

### Pollerama v1.12 a v1.13.1 añaden selección del client tag, pestañas de perfil y límites a los hilos

[Pollerama](https://github.com/formstr-hq/nostr-polls), un cliente Nostr para Android centrado en encuestas y notas con una potente capa de descubrimiento basada en la web of trust, publicó v1.12.0, v1.13.0 y v1.13.1 en Zapstore esta semana. Los usuarios ya pueden elegir qué client tag se adjunta a las notas y encuestas que crean, ya sea de una lista predeterminada o introduciendo uno propio. Las cadenas de comentarios y respuestas muy anidadas se detienen ahora tras varios niveles y enlazan al hilo completo en la página de la nota. Las páginas de perfil abren de forma predeterminada en Notes, divididas en una pestaña Posts y otra Conversations. Se corrigió un fallo de persistencia de follows por el que las cuentas recién seguidas desaparecían al reiniciar la app, y los botones para seguir ahora muestran el progreso.

### getwired.app y get-tao.app corrigen el flujo de envío confess de NIP-13

[getwired.app](https://github.com/smolgrrr/Wired) y [get-tao.app](https://github.com/smolgrrr/TAO), que comparten un flujo de publicación anónima que añade proof-of-work NIP-13 para frenar el spam en el momento del envío, corrigieron el [flujo de envío confess](https://github.com/smolgrrr/Wired/pull/57) para que la UX durante el minado de PoW sea coherente.

### nostui añade una pestaña de timeline de menciones

[nostui](https://github.com/akiomik/nostui), un cliente Nostr de terminal en Rust, añadió una [pestaña de timeline de menciones](https://github.com/akiomik/nostui/pull/463) que presenta en una vista específica de la TUI los events de kind 1 que incluyen un tag con la pubkey activa.

### Heartwood incorpora URIs bunker NIP-46 por identidad y un puente de firma en modo HSM

[Heartwood](https://github.com/forgesworn/heartwood) es un firmante [NIP-46](/es/topics/nip-46/) en el que la clave de firma nunca llega al cliente: este se comunica mediante NIP-46 con un pequeño relay, y el relay usa un protocolo de frames serie para comunicarse con un dispositivo de hardware conectado que realiza la firma. Esta semana el proyecto incorporó un [puente de firma entre relay y puerto serie](https://github.com/forgesworn/heartwood/pull/11) y [conexiones bunker por identidad](https://github.com/forgesworn/heartwood/pull/16), de modo que un solo dispositivo de hardware con varias identidades expone una URI bunker distinta para cada una.

### Refactorización de autenticación y firmantes de Nostter

[Nostter](https://github.com/SnowCait/nostter) rediseñó esta semana su [capa de autenticación y firmantes](https://github.com/SnowCait/nostter/pulls?q=is%3Amerged+auth), trasladando el estado de sesión a una única signal y extrayendo el despacho de firmantes a módulos de estrategia. La dirección es una abstracción limpia de firmantes donde la extensión web NIP-07, el bunker remoto NIP-46 y el nsec sin procesar comparten una sola ruta de código.

### Dart NDK extrae el firmante NIP-07 y aleatoriza las marcas de tiempo NIP-59

[Dart NDK](https://github.com/relaystr/dart_ndk) trasladó su firmante [NIP-07](/es/topics/nip-07/) fuera del paquete core y a `ndk_flutter` —donde reside el WebView de Flutter—, y [aleatorizó las marcas de tiempo de sus gift wraps NIP-59](https://github.com/relaystr/dart_ndk/pull/667) para reforzar la protección de los mensajes cifrados frente a la correlación temporal.

### Milk Market añade páginas de tienda NIP-23 y procesamiento de pagos con Square

[Milk Market](https://github.com/shopstr-eng/milk-market), el escaparate de marketplace del equipo de Shopstr, añadió a cada tienda una página de blog respaldada por los events de formato largo [NIP-23](/es/topics/nip-23/) del vendedor, con secciones editables y una ruta directa a la configuración del blog. Esa misma semana incorporó [Square](https://github.com/shopstr-eng/milk-market/pull/30) como procesador de pagos alternativo para vendedores y la compra automática de etiquetas de envío para pedidos pagados.

### Calendar by Formstr publica una app para iOS

[Calendar by Formstr](https://github.com/formstr-hq/nostr-calendar) fusionó esta semana el [PR #159 IOS App](https://github.com/formstr-hq/nostr-calendar/pull/159), llevando a iOS el cliente de calendario [NIP-52](/es/topics/nip-52/). El [PR #197](https://github.com/formstr-hq/nostr-calendar/pull/197) corrige el análisis de fechas de calendario en hora local, y el [PR #201](https://github.com/formstr-hq/nostr-calendar/pull/201) añade un flujo E2E de Playwright activado mediante una etiqueta `run-tests`.

### cagliostr aplica NIP-22, NIP-09 por coordenada y proof-of-work NIP-13

[cagliostr](https://github.com/mattn/cagliostr), una implementación de relay en Go, reforzó esta semana tres rutas de aplicación de reglas: [proof-of-work NIP-13 configurable](https://github.com/mattn/cagliostr/pull/7) para events entrantes, [eliminación NIP-09 por coordenada direccionable](https://github.com/mattn/cagliostr/pull/8) para que los events reemplazables puedan eliminarse mediante su tag `a` —algo inaccesible solo con la eliminación por id del event—, y [límites configurables de timestamp NIP-22](https://github.com/mattn/cagliostr/pull/9) que rechazan events fechados demasiado lejos en el pasado o el futuro.

---

## Proyectos recién rastreados y descubiertos

La [suite de bienestar Vanderwarker](https://git.vanderwarker.family/wellbeing) publica telemetría del mundo físico como events Nostr bajo una clave de firma compartida del publicador. Consta de cinco apps hermanas: [Holy Fit](https://git.vanderwarker.family/wellbeing/holyfit-android) es un contador de pasos que ancla datos de actividad física en Nostr como `kind:30078`; [Nunlock](https://git.vanderwarker.family/wellbeing/nunlock-android) publica un contador diario de desbloqueos del teléfono; [Saint Stream](https://git.vanderwarker.family/wellbeing/saintstream-android) publica la reproducción multimedia actual como User Status; [Sister Charge](https://git.vanderwarker.family/wellbeing/sistercharge-android) publica el nivel, voltaje y temperatura de la batería cada 15 minutos; y [Cellibacy](https://git.vanderwarker.family/wellbeing/cellibacy-android) publica el uso diario de datos. Las cinco aparecieron en Zapstore entre el 24 y el 30 de junio.

[ntrack v0.1.9](https://github.com/f321x/ntrack/releases/tag/v0.1.9) es una app Android serverless para compartir ubicación en directo de forma cifrada, construida en Rust y Slint y publicada el 29 de junio. Es hermana de [Haven](https://github.com/mehmetefeumit/Haven-App), la app para compartir ubicaciones basada en [Marmot](/es/topics/marmot/) tratada en el [número 28](/en/newsletters/2026-06-24-newsletter/#haven-launches-private-location-sharing-on-marmot), pero usa una arquitectura de transporte distinta: DMs cifrados de Nostr transportan las actualizaciones de ubicación, mientras Haven emplea mensajes de grupo Marmot.

[NostrAppShell](https://git.nostrdev.com/stuff/NostrAppShell) es un scaffold incipiente de shell de aplicaciones para construir apps Nostr. El proyecto publicó esta semana su primera documentación dirigida a usuarios.

[NIPs by Pollerama](https://nips.pollerama.fun) —repositorio [abh3po/better-nips](https://github.com/abh3po/better-nips), creado el 2026-06-29— es un nuevo cliente para los NIPs `kind:30817` creados por la comunidad de [NostrHub](https://nostrhub.io), presentado como una superficie alternativa a nostrhub.io ponderada por confianza. Cada NIP `kind:30817` tiene su propia URL compartible (`#/nip/<naddr>`), con renderizado Markdown completo y los event kinds que define. El cliente ofrece tres feeds: Following, Web of Trust —follows de follows— y Global, cada uno ordenable por aprobaciones ponderadas por confianza o por novedad. Las aprobaciones se publican como labels [NIP-32](/es/topics/nip-32/) en el kind `1985`, con tags `["L","nostrhub"]` y `["l","approve","nostrhub"]`, además de un tag `a` que apunta a la dirección del NIP objetivo y un tag `client` que anuncia `better-nips`. Es exactamente la forma de event que firma NostrHub, por lo que las aprobaciones son compatibles entre ambos clientes. La aprobación de un follow directo pesa más en el ranking que la de un follow de segundo grado.

La pila de firma usa [`@formstr/signer`](https://www.npmjs.com/package/@formstr/signer), con un modal de inicio de sesión completo que cubre [NIP-07](/es/topics/nip-07/), bunker y nostrconnect de [NIP-46](/es/topics/nip-46/), ncryptsec de [NIP-49](/es/topics/nip-49/) y firmante Android [NIP-55](/es/topics/nip-55/); las sesiones vuelven a conectarse silenciosamente al recargar. La capa de red se ejecuta mediante [`@formstr/local-relay`](https://www.npmjs.com/package/@formstr/local-relay), un Web Worker que reparte el outbox [NIP-65](/es/topics/nip-65/) del usuario entre relays para que un gran conjunto de web of trust no se propague a un único relay. La posición de diseño es que todos los NIPs comunitarios —alojados en NostrHub, en `better-nips` o en futuros clientes— son iguales a nivel de protocolo; el ranking procede del grafo social, no de la selección de moderadores. Esto encaja directamente con el flujo de labels NIP-32 que abordó el análisis detallado del [número 25](/en/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-32-labeling).

Esta semana aparecieron dos nuevos grupos de repos [NIP-34](/es/topics/nip-34/). [Vidstr](https://git.shakespeare.diy/npub14rg4vrt2v374q95ezeeydu3hkdhmzglcj950mggacap4x0lv0gyq04wun7/vidstr.git) es un cliente Nostr centrado en vídeo, y un [grupo de nostrapps.com](wss://gitnostr.com) publica tres proyectos hermanos: [verdana](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/verdana.git), una VM de napps para escritorio; [hallway](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/hallway.git), un cliente de comunidades personalizable; y [napps](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/napps.git), una especificación y runtime de microapps HTML. El grupo discurre en paralelo al trabajo de [napplets](/es/topics/nip-5d/) tratado en la historia principal del número anterior.

---

## Trabajo de protocolo y actualizaciones de NIPs

### Fusionado: NIP-44 elimina el límite de payload de 65.535 bytes

El [PR #1907](https://github.com/nostr-protocol/nips/pull/1907) se fusionó el 28 de junio tras permanecer abierto desde 2024-09. El cambio elimina el límite superior de 65.535 bytes para el payload en texto plano de un sobre de cifrado versionado [NIP-44](/es/topics/nip-44/) y lo eleva a un máximo de 4 GiB (`uint32_max`). NIP-44 codifica la longitud del payload como un `uint16` en el formato de wire, algo que la especificación original exigía estrictamente para la interoperabilidad; el cambio fusionado adopta un campo de longitud mayor indicado en el byte de versión, de modo que las implementaciones v2 conservan la compatibilidad a nivel de wire y las v3+ transportan la longitud ampliada. Los clientes que usan NIP-44 para mensajes directos [NIP-17](/es/topics/nip-17/), gift wraps [NIP-59](/es/topics/nip-59/), payloads de firmantes remotos [NIP-46](/es/topics/nip-46/) o cualquier otro mensaje Nostr cifrado con NIP-44 ya pueden intercambiar events individuales mayores de 64 KiB sin dividirlos en la capa de aplicación.

### Fusionado: NIP-86 obtiene un método signevent y un event de roles de relay

El [PR #2389](https://github.com/nostr-protocol/nips/pull/2389) añade un método `signevent` a la API JSON-RPC de gestión de relays [NIP-86](/es/topics/nip-86/), que permite a un administrador pedir al relay que firme un event con la propia pubkey del relay. El [PR #2390](https://github.com/nostr-protocol/nips/pull/2390) complementario define un event de roles de relay: un event reemplazable que publica un relay para declarar sus administradores y moderadores. Juntos permiten que los clientes NIP-86 consulten la lista de administradores de un relay y verifiquen que una solicitud autenticada procede de un administrador vigente, sin confianza fuera de banda. Más abajo se analizan ambos cambios en detalle.

### Fusionado: NIP-34 sustituye personal-fork por `u` para GRASP-06

El [PR #2395](https://github.com/nostr-protocol/nips/pull/2395) se fusionó el 24 de junio y sustituye el tag `personal-fork` de [NIP-34](/es/topics/nip-34/) en los events de estado de repos (`kind:30618`) por un tag `u` —de «upstream»—, alineando el formato de wire con la semántica de forks GRASP-06 que implementa la suite GitWorkshop. El cambio cierra el [PR #2384](https://github.com/nostr-protocol/nips/pull/2384) (`NIP-34: remove maintainers to solve expiry issues`), que proponía otra corrección de la semántica de forks. La dirección fusionada es la que implementa ngit v2.6.x, por lo que la especificación fusionada y la CLI de referencia quedan alineadas. Los repos existentes que usan `personal-fork` siguen interoperando; los nuevos repos y la línea ngit v2.6 publican el tag `u`.

### Fusionado: metadatos de cliente NIP-46, ya en upstream tras su llegada a Amber

El [PR #2381](https://github.com/nostr-protocol/nips/pull/2381) se fusionó el 23 de junio y añade metadatos opcionales de cliente a la solicitud `connect` de [NIP-46](/es/topics/nip-46/), lo que permite que un cliente publique su nombre, una URL de icono y una URL de página principal al conectar con el firmante. [Amber v6.2.2](https://github.com/greenart7c3/Amber/releases/tag/v6.2.2) incorporó la extensión de metadatos la semana anterior, según la [cobertura del número 28](/en/newsletters/2026-06-24-newsletter/#amber-v622-implements-nip-46-client-metadata); esta semana el NIP upstream alcanza a la implementación ya publicada.

### Abierto: claves deterministas de wrapper NIP-17 basadas en epochs

Los [PR #2397](https://github.com/nostr-protocol/nips/pull/2397) y [PR #2396](https://github.com/nostr-protocol/nips/pull/2396) abordan dos propuestas convergentes de claves de wrap NIP-17. El PR #2397 propone que la clave de firma efímera usada para crear un gift wrap [NIP-59](/es/topics/nip-59/) se derive de forma determinista de una seed por conversación vinculada a un epoch temporal aproximado, de modo que un destinatario que conozca la clave de conversación pueda predecir a qué pubkeys suscribirse. La especificación actual exige una clave aleatoria nueva por wrap, lo que imposibilita esa predicción. El PR #2396 es el cambio complementario: los wraps de una conversación dada deberían firmarse directamente con la clave de conversación para que la pubkey del wrap sirva también como identificador de la conversación. Juntos trazan un camino hacia conversaciones NIP-17 filtrables sin filtrar metadatos. Ambos siguen abiertos y en discusión.

### Abierto: NIP-59 debería rechazar en el relay los events seal de kind 13

El [PR #2399](https://github.com/nostr-protocol/nips/pull/2399) propone que los relays rechacen los events de kind 13 —el seal interno de un gift wrap [NIP-59](/es/topics/nip-59/)— cuando aparezcan en el nivel superior de una solicitud de publicación, porque un event seal solo tiene sentido dentro de un wrap y un seal filtrado expone la pubkey del destinatario. El [issue #2398](https://github.com/nostr-protocol/nips/issues/2398) complementario va más lejos y sostiene que el seal debería redefinirse como kind efímero —los kinds efímeros NIP-01 no se almacenan en relays—, lo que reforzaría la regla a nivel de protocolo y eliminaría la dependencia de la política de cada relay.

### Abierto: estados de grupos NIP-29

El [PR #2372](https://github.com/nostr-protocol/nips/pull/2372) añade a [NIP-29](/es/topics/nip-29/) —grupos basados en relays— una semántica explícita de estados de grupo, que define qué significa que un grupo sea abierto, cerrado, público, privado o archivado, y cómo interactúan las transiciones de estado con los events de miembros. La propuesta incorpora a la especificación del relay semánticas que hasta ahora eran específicas de cada cliente.

### Abierto: compatibilidad opcional con varios maintainers en NIP-34

El [PR #2324](https://github.com/nostr-protocol/nips/pull/2324) es la propuesta complementaria al [PR #2395](https://github.com/nostr-protocol/nips/pull/2395) fusionado —la semántica de forks GRASP-06 tratada arriba—. El PR #2324 añade compatibilidad opcional con varios maintainers a los events de anuncio de repos [NIP-34](/es/topics/nip-34/) (`kind:30617`), permitiendo que un repositorio declare más de una pubkey de maintainer canónico mediante tags `maintainer` repetidos. Los clientes consideran entonces oficiales los patches e issues firmados por cualquier maintainer declarado, lo que resuelve la carencia histórica por la que los repos NIP-34 con varios maintainers deben canalizarlo todo por una sola pubkey o recurrir a coordinación fuera del protocolo.

### Abierto: operador AND de NIP-91 para filtros, propuesta abierta y no fusionada

El [PR #2252](https://github.com/nostr-protocol/nips/pull/2252) es la propuesta de operador AND para los [filtros](/es/topics/nip-01/) de Nostr, que reabre un diseño debatido por primera vez en el anterior [PR #1365](https://github.com/nostr-protocol/nips/pull/1365), ya cerrado. Ya existen implementaciones en [nostr-rs-relay](https://github.com/v0l/nostr-rs-relay), applesauce, [Amethyst](https://github.com/vitorpamplona/amethyst) y worker-relay, pero el PR de la especificación sigue abierto.

### Cerradas: cuatro NIPs comerciales de pats2sats

Esta semana se cerraron cuatro propuestas comerciales sobre Nostr: Escrow ([#2334](https://github.com/nostr-protocol/nips/pull/2334)), Reservations ([#2335](https://github.com/nostr-protocol/nips/pull/2335)), una extensión de anuncios de marketplace [NIP-99](/es/topics/nip-99/) ([#2346](https://github.com/nostr-protocol/nips/pull/2346)) y un perfil de anuncios de alojamiento ([#2333](https://github.com/nostr-protocol/nips/pull/2333)). Esa misma superficie comercial se consolida ahora en [Gamma Market Spec](https://github.com/GammaMarkets/market-spec), un repositorio de extensiones propio del proyecto que se compone sobre los anuncios de marketplace NIP-99 con semánticas de pedidos, checkout, escrow y disputas. Compass ya rastrea este repositorio junto con Marmot y Blossom como repo de especificación de protocolo externo al propio repositorio de NIPs; entre sus PRs abiertos esta semana están la aclaración de atribución de clientes ([#11](https://github.com/GammaMarkets/market-spec/pull/11)), un tag supersedes para cambios en la identidad de productos ([#8](https://github.com/GammaMarkets/market-spec/pull/8)) y semántica para reseñas de comerciantes ([#7](https://github.com/GammaMarkets/market-spec/pull/7)).

### Abierto: vinculación de identidades Bitcoin

Esta semana se abrieron dos propuestas para vincular identidades Bitcoin con identidades Nostr: una [dirección de pago silencioso de Bitcoin NIP-352](https://github.com/nostr-protocol/nips/pull/2392) y una [prueba de vinculación de identidad Bitcoin-OTC](https://github.com/nostr-protocol/nips/pull/2401).

---

## Análisis detallado de NIP: NIP-86 (API de gestión de relays)

[NIP-86](/es/topics/nip-86/) define una interfaz JSON-RPC para gestionar relays, que permite a clientes autorizados enviar comandos administrativos a relays mediante una API estandarizada. Un único cliente puede gestionar cualquier relay compatible con NIP-86 sin herramientas específicas para cada uno. Dos fusiones de la especificación esta semana —[PR #2389](https://github.com/nostr-protocol/nips/pull/2389) y [PR #2390](https://github.com/nostr-protocol/nips/pull/2390)— cierran el círculo entre events firmados por relays y administradores declarados por relays.

### El transporte

Una solicitud de gestión NIP-86 es un HTTP POST dirigido a la misma URI desde la que el relay sirve conexiones WebSocket, con `Content-Type: application/nostr+json+rpc`. El cuerpo de la solicitud es un documento JSON con esta forma:

```json
{
  "method": "<method-name>",
  "params": [<arg1>, <arg2>, ...]
}
```

La autenticación usa en el header `Authorization` un event firmado de autenticación HTTP [NIP-98](/es/topics/nip-98/). El relay verifica que la pubkey firmante esté en su lista de administradores antes de ejecutar el método. La respuesta del relay es un documento JSON con esta forma:

```json
{
  "result": <return-value>,
  "error": "<error-string-if-any>"
}
```

### Los métodos que existían antes de esta semana

El conjunto de métodos preexistente cubre bloqueos de pubkeys (`banpubkey`, `allowpubkey`, `listbannedpubkeys`), bloqueos de events (`banevent`, `allowevent`, `listbannedevents`), metadatos del relay (`changerelayname`, `changerelaydescription`, `changerelayicon`), gestión de la lista de pubkeys permitidas (`allowkind`, `disallowkind`, `listallowedkinds`) y un método `stats` que devuelve estadísticas del relay. La forma se aproxima deliberadamente a un servicio JSON-RPC estándar, para que un cliente pueda superponer bindings tipados.

### Qué cambió esta semana

El [PR #2389](https://github.com/nostr-protocol/nips/pull/2389) añade un método `signevent` a la especificación. El método recibe como argumento una plantilla parcial de event —kind, tags y content— y pide al relay que firme y devuelva un event completo con la propia pubkey del relay en el campo `pubkey`. Es la condición previa para que un relay publique events sobre sí mismo a nivel de protocolo: los anuncios de pubkeys bloqueadas, los metadatos del relay y el nuevo event de roles de relay descrito a continuación exigen que el relay firme con la clave controlada por su operador, pero la mayoría de los operadores no quieren guardar una clave privada en su cliente administrativo.

El [PR #2390](https://github.com/nostr-protocol/nips/pull/2390) define un event de roles de relay: un event reemplazable parametrizado que publica un relay —firmado con su propia pubkey mediante `signevent`— para declarar las pubkeys de sus administradores y moderadores con semánticas de roles explícitas. Un cliente compatible con NIP-86 puede obtener el event de roles de cualquier relay rastreado, construir la lista de administradores a partir de los tags del event y validar que una solicitud NIP-86 autenticada procede de un administrador actual, sin confianza fuera de banda ni configuración específica del relay. Los dos PRs cierran juntos el círculo: `signevent` es el mecanismo y los roles de relay son el primer event kind construido sobre él.

### Ejemplo de solicitud NIP-86

Una solicitud completa `banpubkey` de NIP-86 tiene este aspecto:

```json
{
  "method": "banpubkey",
  "params": [
    "<64-char-hex-pubkey-to-ban>",
    "spam"
  ]
}
```

con un header `Authorization` que transporta un event firmado NIP-98:

```json
{
  "id": "5e1c2f9e1d3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c",
  "pubkey": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
  "created_at": 1782824400,
  "kind": 27235,
  "tags": [
    ["u", "https://relay.example.com/"],
    ["method", "POST"],
    ["payload", "<sha256-of-request-body>"]
  ],
  "content": "",
  "sig": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100"
}
```

La pubkey firmante debe figurar en el conjunto de administradores del relay —ahora declarado en el event de roles del relay—; el tag `u` debe coincidir con la URL HTTPS del relay; y el tag `payload` debe coincidir con el SHA-256 del cuerpo JSON de la solicitud. El relay devuelve:

```json
{
  "result": true,
  "error": null
}
```

### Implementaciones

- [Amethyst](https://github.com/vitorpamplona/amethyst) incluye una interfaz de gestión de relays NIP-86 en Android (v1.07.0+).
- Entre los relays de referencia que implementan la especificación están [strfry](https://github.com/hoytech/strfry), [khatru](https://github.com/fiatjaf/khatru) y varias implementaciones menores enlazadas por la especificación desde su sección `Implementation Status`.

Los clientes compatibles con NIP-86 empezarán a tratar el event de roles de relay como fuente canónica de la lista de administradores del relay cuando las implementaciones adopten los cambios `signevent` y Relay Roles.

---

## Análisis detallado de NIP: NIP-89 (handlers de aplicaciones recomendados)

[NIP-89](/es/topics/nip-89/) define dos event kinds reemplazables parametrizados: `kind:31990`, el handler de aplicación que publica el desarrollador de una app, y `kind:31989`, la recomendación que publica un usuario sobre una app que utiliza. Juntos permiten que los clientes descubran aplicaciones capaces de manejar un event kind desconocido sin coordinación fuera de banda: un lector de formato largo que encuentre un event `kind:30030` que no maneje de forma nativa puede consultar el grafo NIP-89 en busca de handlers y ofrecer al usuario un flujo «Open in...» hacia una app publicada que sí lo haga. NIP-89 es la infraestructura original para el mismo problema de enrutamiento entre apps que el trabajo de napplets/napps presente en este número amplía ahora hacia applets componibles nativos de Nostr.

### El event de handler de aplicación (`kind:31990`)

El desarrollador de una app publica uno o varios events de handler que describen qué event kinds admite la app y cómo abrir una entidad Nostr en ella:

```json
{
  "id": "8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b",
  "pubkey": "c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2",
  "created_at": 1782824400,
  "kind": 31990,
  "tags": [
    ["d", "longform-reader-v1"],
    ["k", "30023"],
    ["k", "30024"],
    ["web", "https://reader.example.com/a/<bech32>", "naddr"],
    ["ios", "longformreader://open/<bech32>"],
    ["android", "longformreader://open/<bech32>"]
  ],
  "content": "{\"name\": \"Longform Reader\", \"picture\": \"https://reader.example.com/icon.png\", \"about\": \"A native reader for NIP-23 longform.\"}",
  "sig": "1f2e3d4c5b6a798877665544332211000ffeeddccbbaa99887766554433221100ffeeddccbbaa99887766554433221100ffeeddccbbaa9988776655443322110a"
}
```

El tag `d` identifica el handler —para que pueda reemplazarse—, cada tag `k` declara un event kind que maneja la app, y cada tag de plataforma (`web`, `ios`, `android`, ...) proporciona una plantilla de URL con `<bech32>` como placeholder de una entidad codificada mediante [NIP-19](/es/topics/nip-19/) que el cliente llamante sustituye al abrirla. Un solo event de handler puede anunciar varios kinds compatibles si comparten el mismo patrón de enrutamiento, lo que mantiene compacto el descubrimiento de apps y evita un event de handler por kind.

### El event de recomendación de usuario (`kind:31989`)

Un usuario publica una recomendación que declara qué apps utiliza para un event kind determinado:

```json
{
  "id": "9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d",
  "pubkey": "d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3",
  "created_at": 1782824500,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com", "web"],
    ["a", "31990:e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6:reader-pro", "wss://relay.example.com", "ios"]
  ],
  "content": "",
  "sig": "2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6"
}
```

El tag `d` contiene el event kind recomendado. Cada tag `a` es un puntero de dirección NIP-01 a un event de handler `kind:31990`, junto con el relay sugerido y la plataforma a la que se aplica la recomendación. Una misma recomendación puede enumerar varias apps para distintas plataformas.

### El client tag y el compromiso de privacidad

NIP-89 también define un tag `client` opcional que cualquier app publicadora puede adjuntar a los events que crea:

```
["client", "Longform Reader", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com"]
```

Esto permite que cualquier cliente que muestre el event revele de qué app procede, consulte metadatos más completos del handler y respete las indicaciones de renderizado declaradas por este. La especificación también señala explícitamente el coste de privacidad: un cliente que emite un tag `client` en cada event publica la identidad del software del usuario, lo que revela patrones de uso con el tiempo. La especificación recomienda que los clientes permitan desactivarlo.

El [PR #3422](https://github.com/vitorpamplona/amethyst/pull/3422) de Amethyst analiza y muestra los tags `t`, `i`, `a` y `client` de NIP-89 al presentar events, revelando directamente en el timeline qué app creó una nota.

### Cómo funciona en la práctica el flujo de descubrimiento

Un cliente que recibe un event kind desconocido sigue estos pasos. (1) Consulta en el grafo de follows del usuario events `kind:31989` con un tag `d` que coincida con el event kind. (2) Resuelve cada tag `a` recomendado hasta su event de handler `kind:31990`. (3) Elige el handler cuya plantilla de URL `web`, `ios` o `android` coincida con la plataforma actual. (4) Sustituye en la plantilla de URL la codificación `bech32` de la entidad. (5) Ofrece al usuario la URL resultante como opción «Open in...». El flujo está filtrado socialmente: un cliente que consulte events de handlers arbitrarios en relays no confiables podría redirigir a los usuarios a apps maliciosas, así que partir de personas a las que sigue el usuario es una opción predeterminada más segura que tratar por igual a todos los handlers publicados.

### NIP-89 y la capa napplet

La sección Discover de Amethyst, el runtime host de napplets y la visualización de client tags construyen juntos una superficie completa de consumo de NIP-89 en Android. La especificación napplet, lanzada en el número anterior, amplía los posibles destinos de esos events de handlers NIP-89: applets en sandbox que ejecutan un runtime componible nativo de Nostr sobre Nostr y Blossom. NIP-89 es el grafo de descubrimiento y enrutamiento; el runtime napplet es uno de los objetivos de ejecución a los que puede apuntar.

---

*Comentarios, correcciones y proyectos que se nos hayan escapado: abrid un issue en [github.com/andotherstuff/nostr-compass](https://github.com/andotherstuff/nostr-compass) o contactad con nosotros mediante un DM NIP-17 en npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923.*
