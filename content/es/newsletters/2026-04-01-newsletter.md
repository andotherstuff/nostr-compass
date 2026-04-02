---
title: 'Nostr Compass #16'
date: 2026-04-01
translationOf: /en/newsletters/2026-04-01-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Bienvenido de nuevo a Nostr Compass, tu guía semanal de Nostr.

**Esta semana:** [Amethyst](https://github.com/vitorpamplona/amethyst) lanza [v1.07.0](#amethyst-lanza-notas-fijadas-gestión-de-relays-y-request-to-vanish) con notas fijadas, gestión de relays vía [NIP-86](/es/topics/nip-86/), y soporte de [NIP-62](/es/topics/nip-62/) Request to Vanish. [NIP-5A](#nip-5a-se-fusiona-trayendo-sitios-web-estáticos-a-nostr) (Static Websites) se fusiona en el repositorio de NIPs, definiendo cómo alojar sitios web bajo pares de claves Nostr usando almacenamiento [Blossom](/es/topics/blossom/). [Flotilla](https://gitea.coracle.social/coracle/flotilla) lanza [v1.7.0](#flotilla-v170-añade-salas-de-voz-e-inicio-de-sesión-con-email) con salas de voz, login con email/contraseña, y DMs con proof-of-work. [White Noise](https://github.com/marmot-protocol/whitenoise) corrige churn de relays en [v2026.3.23](#white-noise-corrige-churn-de-relays-y-amplía-los-controles-del-cliente), [nospeak](https://github.com/psic4t/nospeak) lanza su [1.0.0](#nospeak-se-lanza-como-un-mensajero-privado-10) como mensajero cifrado sin registro. [Nymchat](https://github.com/Spl0itable/NYM) [adopta Marmot](#nymchat-lanza-chats-de-grupo-impulsados-por-marmot) para chats de grupo cifrados con MLS con fallback a NIP-17. [Calendar by Form*](https://github.com/formstr-hq/nostr-calendar) alcanza [v1.0.0](#calendar-by-form-v100) con listas privadas de calendario e importación ICS, [Amber](https://github.com/greenart7c3/Amber) añade [recuperación por mnemónico y whitelisting de autenticación de relay NIP-42](#amber-v502-a-v504), y la [especificación Marmot](#marmot-mueve-keypackages-a-eventos-direccionables-y-ajusta-las-notificaciones-push) mueve los KeyPackages a eventos direccionables mientras ajusta el formato de notificaciones push MIP-05.

## Noticias

### Amethyst lanza notas fijadas, gestión de relays y Request to Vanish

[Amethyst](https://github.com/vitorpamplona/amethyst), el cliente Android mantenido por vitorpamplona, lanzó seis versiones en tres días, desde [v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) hasta [v1.07.5](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.5). El conjunto principal de funciones abarca seis superficies de protocolo: notas fijadas, una pantalla dedicada de feed de encuestas, soporte de [NIP-62](/es/topics/nip-62/) (Request to Vanish) para solicitar la eliminación completa de eventos de los relays, [NIP-86](/es/topics/nip-86/) (Relay Management API) desde dentro del cliente, evaluaciones de [NIP-66](/es/topics/nip-66/) (Relay Discovery and Liveness Monitoring) en la pantalla de información del relay, y visualización de información de miembros de [NIP-43](/es/topics/nip-43/) (Relay Access Metadata and Requests).

[NIP-86](/es/topics/nip-86/) define una interfaz JSON-RPC para operadores de relays, permitiendo a los clientes enviar comandos administrativos como banear pubkeys, permitir pubkeys y listar usuarios baneados sobre una API estandarizada. Amethyst ahora expone esto directamente en su UI de gestión de relays, así que los usuarios que ejecutan sus propios relays pueden administrarlos desde el mismo cliente que usan para publicar. [PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039) reemplaza el antiguo diálogo de entrada hex para banear y permitir pubkeys con un diálogo interactivo de búsqueda de usuarios.

v1.07.2 añadió subidas desde teclado GIF y corrigió una regresión de firma donde las respuestas de rechazo de Amber se interpretaban mal porque versiones antiguas de Amber devolvían una cadena vacía para el campo `rejected` ([PR #2042](https://github.com/vitorpamplona/amethyst/pull/2042)). v1.07.5 corrige un crash en la subida de imágenes. Los lanzamientos [v1.06.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.2) y [v1.06.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.3) a principios de la semana añadieron un selector de tipo de encuesta para encuestas de elección única vs. múltiple, drag-to-seek en barras de progreso de vídeo, y mejoras de publicación anónima.

### NIP-5A se fusiona, trayendo sitios web estáticos a Nostr

[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md) (Static Websites) se fusionó vía [PR #1538](https://github.com/nostr-protocol/nips/pull/1538), definiendo cómo alojar sitios web estáticos bajo pares de claves Nostr. La especificación usa dos kinds de evento: kind `15128` para un sitio raíz, uno por pubkey, y kind `35128` para sitios nombrados identificados por una etiqueta `d`. Cada manifiesto mapea rutas URL a hashes SHA256, con etiquetas `server` opcionales apuntando a hosts de almacenamiento [Blossom](/es/topics/blossom/) donde viven los archivos reales.

El modelo de hosting funciona así: un autor construye un sitio estático, sube los archivos a uno o más servidores Blossom, y luego publica un evento de manifiesto firmado que mapea rutas a hashes de contenido. Un servidor host recibe solicitudes web, resuelve la pubkey del autor desde el subdominio, obtiene el manifiesto desde la lista de relays [NIP-65](/es/topics/nip-65/) del autor, y sirve los archivos descargando los blobs correspondientes desde Blossom. El sitio permanece bajo el control del autor porque solo esa clave puede firmar un manifiesto actualizado. El servidor host es reemplazable porque cualquier servidor que entienda NIP-5A puede servir el mismo sitio desde el mismo manifiesto.

La especificación se construye sobre infraestructura que ya existía. [nsite](https://github.com/lez/nsite), la implementación host de referencia de NIP-5A construida por lez, y [nsite-manager](https://github.com/hzrd149/nsite-manager), la UI de gestión de hzrd149, ya estaban funcionando antes de que el NIP se fusionara. La fusión hace oficiales los kinds de evento y las reglas de resolución de URL, lo que da a segundas y terceras implementaciones un objetivo estable.

### White Noise corrige churn de relays y amplía los controles del cliente

[White Noise](https://github.com/marmot-protocol/whitenoise), el mensajero privado construido sobre el protocolo [Marmot](/es/topics/marmot/), lanzó [v2026.3.23](https://github.com/marmot-protocol/whitenoise/releases/tag/v2026.3.23) el 25 de marzo. El trabajo principal es estabilidad de relays. El login ya no espera a que termine cada publicación de lista de relays antes de continuar, porque la publicación de listas ahora usa lógica de quorum y reintenta el resto en segundo plano. Las operaciones puntuales de fetch y publish usan sesiones efímeras acotadas de relay en lugar de quedarse en el pool de larga duración, las sesiones restauradas recuperan su ruta de refresh de grupos después del arranque, y la app ahora expone diagnósticos e inspección de estado de relay a través de [PR #495](https://github.com/marmot-protocol/whitenoise/pull/495) y [PR #502](https://github.com/marmot-protocol/whitenoise/pull/502).

El mismo lanzamiento cambia cómo se comportan las conversaciones. [PR #468](https://github.com/marmot-protocol/whitenoise/pull/468) añade threading de respuestas NIP-C7 con etiquetas `q` y referencias `nostr:nevent`, [PR #471](https://github.com/marmot-protocol/whitenoise/pull/471) y [PR #512](https://github.com/marmot-protocol/whitenoise/pull/512) mantienen visibles los mensajes eliminados como marcadores de eliminado en lugar de quitarlos silenciosamente, [PR #478](https://github.com/marmot-protocol/whitenoise/pull/478) añade un flujo de reporte de errores en la app usando reportes anónimos con [NIP-44](/es/topics/nip-44/) (Encrypted Payloads), y [PR #486](https://github.com/marmot-protocol/whitenoise/pull/486) añade chat de soporte directamente en el cliente. Los controles de mensajes orientados al usuario también aterrizaron en la misma ventana: [PR #532](https://github.com/marmot-protocol/whitenoise/pull/532) archiva chats, [PR #541](https://github.com/marmot-protocol/whitenoise/pull/541) añade mute y unmute con duraciones configurables, y [PR #535](https://github.com/marmot-protocol/whitenoise/pull/535) añade ajustes de notificaciones. [PR #539](https://github.com/marmot-protocol/whitenoise/pull/539) es trabajo preparatorio de registro push, conectando el registro APNs en iOS y la detección de Play Services en Android para que el registro pueda construirse encima. Del lado backend, el [MDK](https://github.com/marmot-protocol/mdk) (Marmot Development Kit) añadió primitivas de notificaciones push MIP-05 y un constructor de solicitudes de notificación ([PR #235](https://github.com/marmot-protocol/mdk/pull/235), [PR #238](https://github.com/marmot-protocol/mdk/pull/238)), mientras [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) añadió persistencia de registro de notificaciones push ([PR #688](https://github.com/marmot-protocol/whitenoise-rs/pull/688)), correcciones de cancelación de tareas en segundo plano ([PR #696](https://github.com/marmot-protocol/whitenoise-rs/pull/696)), y recuperación de key packages al iniciar ([PR #693](https://github.com/marmot-protocol/whitenoise-rs/pull/693)).

### Nostr VPN alcanza v0.3.0 con sincronización de roster e invite v2

[Siguiendo la cobertura de lanzamiento de la semana pasada](/es/newsletters/2026-03-25-newsletter/#nostr-vpn-se-lanza-como-alternativa-a-tailscale), [nostr-vpn](https://github.com/mmalmi/nostr-vpn), la VPN peer-to-peer que usa relays Nostr para señalización y WireGuard para túneles cifrados, continuó su ritmo rápido de lanzamientos, publicando versiones hasta [v0.3.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.3). El salto de versión trae dos cambios disruptivos: el formato de invitación pasa a v2 (0.3.0 aún puede importar invitaciones v1, pero builds más antiguas no pueden importar invitaciones v2), y se añadió sincronización de roster firmada por administrador al protocolo de señalización. Los peers de versiones mixtas aún pueden conectarse en la capa mesh, pero los peers antiguos no participarán en la sincronización del roster.

La adición de sincronización de roster inicia el movimiento hacia una red gestionada. Un nodo administrador ahora puede empujar cambios de membresía a todos los peers, de modo que añadir o quitar un dispositivo de la red mesh no requiere que cada peer actualice manualmente su configuración. Las versiones v0.2.x durante la misma semana abordaron problemas específicos de despliegue: [v0.2.22](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.22) a [v0.2.28](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.28) corrigieron gestión de servicios Windows, añadieron scripts de build Android, y refinaron el flujo de emparejamiento LAN.

### nospeak se lanza como un mensajero privado 1.0

[nospeak](https://github.com/psic4t/nospeak), un mensajero privado construido sobre Nostr, lanzó su versión [1.0.0](https://github.com/psic4t/nospeak/releases/tag/v1.0.0) el 27 de marzo. El proyecto incluye conversaciones uno a uno y de grupo, gestión de contactos, y una arquitectura auto-alojable. Los chats uno a uno usan [NIP-17](/es/topics/nip-17/) (Private Direct Messages), que combina [NIP-59](/es/topics/nip-59/) (Gift Wrap) con [NIP-44](/es/topics/nip-44/) (Encrypted Payloads) para ocultar el remitente a los relays. Para medios, los archivos se cifran del lado del cliente con AES-256-GCM antes de subirlos a servidores Blossom. El lanzamiento también se distribuye como imagen de contenedor para auto-hosting.

### Flotilla v1.7.0 añade salas de voz e inicio de sesión con email

[Flotilla](https://gitea.coracle.social/coracle/flotilla), el cliente estilo Discord de hodlbod para [NIP-29](/es/topics/nip-29/) (Relay-based Groups) construido alrededor del modelo "relays as groups", lanzó [v1.7.0](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.0) y [v1.7.1](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.1) el 30 y 31 de marzo. La funcionalidad principal son las salas de voz, contribuidas por mplorentz. Los usuarios ahora pueden unirse a llamadas de voz dentro de canales de grupo, con un diálogo de unión ([PR #109](https://gitea.coracle.social/coracle/flotilla/pulls/109)) que les permite seleccionar un dispositivo de entrada de audio y elegir si quieren entrar a la llamada de voz o solo ver el chat de texto. El diálogo resuelve un problema de UX de la iteración anterior: entrar a una sala con voz habilitada forzaba antes la activación del micrófono incluso cuando el usuario solo quería leer mensajes o revisar ajustes de la sala.

El mismo lanzamiento añade login con email y contraseña como alternativa a autenticación basada en claves Nostr, proof-of-work en DMs, edición de DMs, onboarding y ajustes de relay rediseñados, detección de soporte Blossom vía `supported_nips`, mejoras de badges de notificación, fallback de notificaciones push Android, y correcciones de subida de archivos en Android. v1.7.1 sigue con una corrección para el fallback de registro de pomade al usar un firmante offline.

Hodlbod también está construyendo [Caravel](https://gitea.coracle.social/coracle/caravel), un gestor de hosting y panel para relays zooid, que registró 40 commits esta semana en desarrollo inicial.

### Nymchat lanza chats de grupo impulsados por Marmot

[Nymchat](https://github.com/Spl0itable/NYM) (también conocido como NYM, Nostr Ynstant Messenger), el cliente de chat efímero conectado con Bitchat, anunció que todos los nuevos chats de grupo ahora usan el protocolo [Marmot](/es/topics/marmot/) para mensajería cifrada con MLS. La integración usa kinds `443`, `444` y `445` para key packages, mensajes welcome y mensajes de grupo respectivamente, proporcionando forward secrecy, seguridad post-compromise y fuga cero de metadatos. Si un receptor no puede usar MLS, Nymchat recurre a su ruta anterior de chats grupales [NIP-17](/es/topics/nip-17/) (Private Direct Messages), que sigue estando cifrada de extremo a extremo pero carece de las propiedades de árbol ratchet de MLS.

Las series v3.55 y v3.56 de esta semana se enfocaron en casos límite de chats grupales: carga en dispositivos nuevos, comportamiento de salida, enrutamiento de notificaciones y conteo de badges no leídos. El mismo ciclo también corrigió una vulnerabilidad XSS por HTML sin escapar y añadió bloqueo de palabras clave y frases extendido a apodos de usuario. Esto convierte a Nymchat en otro cliente Marmot que se suma a [White Noise](#white-noise-corrige-churn-de-relays-y-amplía-los-controles-del-cliente) y [OpenChat](#openchat-v024-a-v030), ampliando el conjunto de apps que pueden intercambiar mensajes grupales cifrados con MLS sobre el mismo protocolo.

## Lanzamientos

### Calendar by Form* v1.0.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), la app de calendario descentralizada construida sobre [NIP-52](/es/topics/nip-52/) (Calendar Events), alcanzó [v1.0.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.0.0) el 29 de marzo. El lanzamiento añade listas privadas de calendario usando eventos Nostr cifrados (kind `32123`) con auto-cifrado [NIP-44](/es/topics/nip-44/) (Encrypted Payloads), de modo que los usuarios puedan organizar eventos en colecciones privadas sin exponer la agrupación a los relays. El mismo lanzamiento añade manejo de intents ICS para importar datos de calendario desde otras aplicaciones y solicitudes de invitación para compartir eventos entre usuarios.

### Amber v5.0.2 a v5.0.4

[Amber](https://github.com/greenart7c3/Amber), la app firmante [NIP-55](/es/topics/nip-55/) (Android Signer Application), lanzó tres point releases: [v5.0.2](https://github.com/greenart7c3/Amber/releases/tag/v5.0.2), [v5.0.3](https://github.com/greenart7c3/Amber/releases/tag/v5.0.3) y [v5.0.4](https://github.com/greenart7c3/Amber/releases/tag/v5.0.4). La adición más visible es el login con frase mnemónica de recuperación ([PR #358](https://github.com/greenart7c3/Amber/pull/358)), que permite a los usuarios restaurar su firmante desde una seed phrase BIP39 en lugar de requerir la cadena nsec o ncryptsec en bruto. [PR #357](https://github.com/greenart7c3/Amber/pull/357) añade una whitelist de autenticación de relay [NIP-42](/es/topics/nip-42/), para que los usuarios puedan restringir qué relays están autorizados a solicitar autenticación del cliente. [PR #353](https://github.com/greenart7c3/Amber/pull/353) añade selección de alcance de cifrado para permisos de descifrado, permitiendo a los usuarios conceder acceso de descifrado solo NIP-04 o solo NIP-44 en lugar de un permiso total. v5.0.4 corrige un bug donde el rechazo no respetaba los permisos acotados de cifrado y descifrado y mejora el rendimiento al recibir múltiples solicitudes de bunker.

### Aegis v0.4.0

[Aegis](https://github.com/ZharlieW/Aegis), el firmante multiplataforma, lanzó [v0.4.0](https://github.com/ZharlieW/Aegis/releases/tag/v0.4.0) el 26 de marzo. El lanzamiento añade modos de autorización Full y Selective en Ajustes y corrige múltiples problemas de escaneo de QR. Los commits de seguimiento [d4f799f](https://github.com/ZharlieW/Aegis/commit/d4f799fe51dd82968d54f72ac77f2de29d0cfe6b), [3313af9](https://github.com/ZharlieW/Aegis/commit/3313af92e55e449ebc98fbd91a085bd444d716e7), [3b214e4](https://github.com/ZharlieW/Aegis/commit/3b214e4176f5dbe7f18690d0996e69dd151fe00f), y [e4f40b6](https://github.com/ZharlieW/Aegis/commit/e4f40b6f1f48c2dae1bb5e4246df26c26dba419e) continúan el mismo trabajo con controles de selección por lotes, estadísticas reutilizables de selección en lote, APIs de selección por grupo completo, y estadísticas de uso por permiso en la página de permisos de la app.

### Schemata v0.2.7 a v0.3.0

[Schemata](https://github.com/nostrability/schemata), las definiciones JSON Schema para validar kinds de eventos Nostr, lanzó cuatro versiones desde [v0.2.7](https://github.com/nostrability/schemata/releases/tag/v0.2.7) hasta [v0.3.0](https://github.com/nostrability/schemata/releases/tag/v0.3.0) con 21 PRs fusionados. El lanzamiento v0.3.0 trae correcciones de consistencia de patrones a través de URLs de relay, IDs hex, tipos MIME y cadenas BOLT-11 ([PR #126](https://github.com/nostrability/schemata/pull/126)), patrones centralizados de URL de relay ([PR #117](https://github.com/nostrability/schemata/pull/117)), schemas base de tipo bech32 para [NIP-19](/es/topics/nip-19/) ([PR #118](https://github.com/nostrability/schemata/pull/118)), y validación para eventos de spell kind 777 ([PR #125](https://github.com/nostrability/schemata/pull/125)). El pipeline de lanzamiento ahora publica una nota kind `1` en Nostr en cada release ([PR #120](https://github.com/nostrability/schemata/pull/120)), así que el proyecto se anuncia a sí mismo a través del protocolo que valida. Schemata ahora soporta una docena de lenguajes más allá del paquete canónico JS/TS: Rust, Go, Python, Kotlin, Java, Swift, Dart, PHP, C#/.NET, C++, Ruby y C.

Junto a Schemata, el equipo publicó [schemata-codegen](https://github.com/nostrability/schemata-codegen), un generador experimental de código que adopta un enfoque diferente al mismo problema de validación. Mientras los paquetes validadores de Schemata requieren una dependencia de runtime de JSON Schema, schemata-codegen convierte schemas directamente en construcciones nativas tipadas del lenguaje (tuplas tipadas de tags, interfaces de kind y validadores de runtime), eliminando la necesidad de una biblioteca validadora en tiempo de ejecución. La [comparación codegen-vs-validators](https://github.com/nostrability/schemata-codegen/blob/main/CODEGEN-VS-VALIDATORS.md) documenta cuándo encaja cada enfoque.

### BigBrotr v6.5.0 a v6.5.4

[BigBrotr](https://github.com/BigBrotr/bigbrotr), la plataforma de analíticas de relays, lanzó cinco versiones desde [v6.5.0](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.5.0) hasta [v6.5.4](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.5.4). El lanzamiento v6.5.0 centraliza la validación de URLs de relay con una función factory `parse_relay_url()` y añade comprobación de longitud de URL y saneamiento de rutas. La infraestructura de monitoreo también recibió correcciones: los eventos de anuncio ahora incluyen etiquetas de ubicación geohash (siguiendo [NIP-52](/es/topics/nip-52/)), y se añadió protección de timeout a las pruebas de metadatos Geo/Net [NIP-66](/es/topics/nip-66/) que no tenían plazo y podían colgarse indefinidamente. [PR #410](https://github.com/BigBrotr/bigbrotr/pull/410) actualiza PostgreSQL de 16 a 18, lo que trae el subsistema de I/O asíncrona y mayor throughput de WAL al pipeline de analíticas de relays.

### El relay de Vertex Lab añade búsqueda de perfiles NIP-50

[Vertex Lab](https://vertexlab.io), el equipo detrás de [npub.world](https://github.com/vertex-lab/npub.world) y el motor Web of Trust [Vertex](https://vertexlab.io/docs), anunció que `wss://relay.vertexlab.io` ahora soporta [NIP-50](/es/topics/nip-50/) (Search) para consultas de perfiles. NIP-50 extiende el filtro estándar `REQ` de Nostr con un campo `search`, permitiendo a los clientes enviar consultas de búsqueda de texto completo a relays que soportan indexación. Añadir búsqueda de perfiles a un relay que ya sirve datos de Web of Trust significa que los clientes conectados a `relay.vertexlab.io` pueden descubrir usuarios por nombre o descripción sin un servicio de búsqueda separado.

### Hashtree v0.2.17 y v0.2.18 lanzan mesh WebRTC e Iris Desktop

[Hashtree](https://github.com/mmalmi/hashtree), el sistema de almacenamiento de blobs direccionados por contenido de mmalmi que publica raíces de Merkle en Nostr, lanzó [v0.2.17](https://github.com/mmalmi/hashtree/releases/tag/v0.2.17) y [v0.2.18](https://github.com/mmalmi/hashtree/releases/tag/v0.2.18) el 31 de marzo. Los dos lanzamientos coronan un sprint de 30 commits que añade tres capacidades distintas. Primero, el crate `hashtree-webrtc` (renombrado a `hashtree-network` en v0.2.18) añade distribución peer-to-peer de blobs basada en WebRTC con señalización mesh unificada a través del CLI Rust, el harness de simulación y el cliente TypeScript. Segundo, el pipeline de lanzamiento ahora construye artefactos Windows (zip del CLI e instalador de Iris), llevando cobertura multiplataforma a macOS, Linux y Windows. Tercero, ambos lanzamientos empaquetan Iris Desktop 0.1.0, el cliente social Nostr de mmalmi, como assets AppImage, .deb e instalador Windows junto al CLI de hashtree. [Hashtree fue cubierto por primera vez en Newsletter #10](/es/newsletters/2026-02-18-newsletter/) cuando se lanzó como un store compatible con [Blossom](/es/topics/blossom/) basado en filesystem. La capa WebRTC es el primer paso hacia distribución de contenido peer-to-peer sin depender de servidores Blossom centralizados.

### Nostr Mail Client v0.7.0 a v0.7.2

[Nostr Mail Client](https://github.com/nogringo/nostr-mail-client), el cliente estilo correo construido con Flutter sobre identidades Nostr, lanzó [v0.7.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.0), [v0.7.1](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.1) y [v0.7.2](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.2) en tres días. El trabajo de producto visible se centró en onboarding ([PR #9](https://github.com/nogringo/nostr-mail-client/pull/9)) y edición de perfil ([PR #10](https://github.com/nogringo/nostr-mail-client/pull/10)), que son piezas básicas para cualquier cliente que intente presentar Nostr como un buzón. Las versiones posteriores empaquetaron ese trabajo en nuevas builds Android y Linux.

### Wisp v0.14.0 a v0.16.1

[Wisp](https://github.com/barrydeen/wisp), el cliente Nostr Android, lanzó 13 versiones más desde [v0.14.0-beta](https://github.com/barrydeen/wisp/releases/tag/v0.14.0-beta) hasta [v0.16.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.3-beta). El trabajo de esta semana incluye correcciones de JSON rumor NIP-17 ([PR #385](https://github.com/barrydeen/wisp/pull/385)), badges de repost en tarjetas de galería ([PR #383](https://github.com/barrydeen/wisp/pull/383)), detalles expandibles de reacciones ([PR #382](https://github.com/barrydeen/wisp/pull/382)), sets persistentes de emoji ([PR #381](https://github.com/barrydeen/wisp/pull/381)), y controles de autoplay de vídeo ([PR #380](https://github.com/barrydeen/wisp/pull/380)). El más reciente [v0.16.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.3-beta) también corrige shortcodes de emoji personalizados con guiones y etiquetas de emoji faltantes.

### Primal Android 3.0.17

[Primal Android](https://github.com/PrimalHQ/primal-android-app) lanzó [3.0.17](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.17) el 24 de marzo. [PR #1000](https://github.com/PrimalHQ/primal-android-app/pull/1000) mapea tipos de WalletException a códigos de error en respuestas NWC, dando a clientes [NIP-47](/es/topics/nip-47/) información estructurada de fallos en lugar de errores genéricos. [PR #995](https://github.com/PrimalHQ/primal-android-app/pull/995) corrige votos zap de encuestas apareciendo como Top Zaps, y [PR #998](https://github.com/PrimalHQ/primal-android-app/pull/998) oculta el balance de billetera y botones de acción cuando no hay billetera configurada.

### OpenChat v0.2.4 a v0.3.0

[OpenChat](https://github.com/DavidGershony/openChat), el cliente de chat basado en Avalonia construido sobre el stack [Marmot](/es/topics/marmot/), lanzó seis versiones desde [v0.2.4](https://github.com/DavidGershony/openChat/releases/tag/v0.2.4) hasta [v0.3.0](https://github.com/DavidGershony/openChat/releases/tag/v0.3.0) en cuatro días. El log de commits cuenta la historia de un cliente llenando los huecos entre "Marmot funciona" y "alguien puede usar esto diariamente". Aterrizó la autenticación de relay [NIP-42](/es/topics/nip-42/), seguida de una UI selector de relay con filtrado de eventos duplicados. Los mensajes de voz ganaron pausa, reanudación, seek y visualización de tiempo. La ruta del firmante se endureció: se corrigieron las conexiones Amber con un formato URI [NIP-46](/es/topics/nip-46/) actualizado, el WebSocket se reconecta automáticamente antes de enviar solicitudes, y las solicitudes Amber duplicadas ahora se capturan comprobando respuestas repetidas. Del lado de almacenamiento, Linux y macOS recibieron almacenamiento seguro AES-256-GCM con claves respaldadas por archivo, y la obtención de metadatos de usuario ahora usa descubrimiento de relay [NIP-65](/es/topics/nip-65/) y guarda resultados en caché en una base de datos local.

### Igloo Signer 1.1

[Igloo](https://github.com/FROSTR-ORG/igloo-ios-prototype), el firmante threshold iOS [FROST](/es/topics/frost/) del proyecto FROSTR, lanzó [v1.1](https://github.com/FROSTR-ORG/igloo-ios-prototype/releases/tag/v1.1) el 28 de marzo. Las firmas FROST (Flexible Round-Optimized Schnorr Threshold) permiten a un grupo de firmantes controlar colectivamente un par de claves Nostr, donde cualquier t-de-n participantes puede firmar un evento sin que ninguna parte tenga la clave privada completa. Igloo es una de las primeras implementaciones móviles de este enfoque para Nostr.

### nak v0.19.3 y v0.19.4

[nak](https://github.com/fiatjaf/nak), el toolkit de línea de comandos Nostr de fiatjaf, lanzó [v0.19.3](https://github.com/fiatjaf/nak/releases/tag/v0.19.3) y [v0.19.4](https://github.com/fiatjaf/nak/releases/tag/v0.19.4) el 26 y 30 de marzo. Ambos lanzamientos corrigen condiciones de panic: [PR #118](https://github.com/fiatjaf/nak/pull/118) reemplaza `strings.Split` con `strings.Cut` para prevenir un posible acceso fuera de rango, y [PR #119](https://github.com/fiatjaf/nak/pull/119) previene la misma clase de panic en el parseo de flags curl.

### Flora v0.3.0

[Flora](https://github.com/shawnyeager/flora-extension), una extensión Chrome para grabación y compartición de pantalla descentralizada en Nostr, lanzó [v0.3.0](https://github.com/shawnyeager/flora-extension/releases/tag/v0.3.0). El lanzamiento añade compartición privada de vídeo cifrado con modos público, no listado y privado. Las grabaciones privadas se cifran con AES-256-GCM y se entregan a los destinatarios vía [NIP-17](/es/topics/nip-17/) (Private Direct Messages), de modo que la grabación nunca toca un servidor en texto claro.

### YakiHonne Mobile 2.0.3

[YakiHonne](https://github.com/YakiHonne/mobile-app), el cliente móvil Nostr, lanzó [2.0.3](https://github.com/YakiHonne/mobile-app/releases/tag/YakiHonne-2.0.3) con reseñas de relays y solicitudes de unión, respuestas anidadas ampliadas, auto-traducción de notas, y soporte NWC multi-relay.

## Actualizaciones de Proyectos

### Zap Cooking añade zap polls y verificación de pagos Branta

[Zap Cooking](https://github.com/zapcooking/frontend), la plataforma de recetas y contenido, fusionó 11 PRs esta semana enfocadas en contenido interactivo y flujos de pago. [PR #277](https://github.com/zapcooking/frontend/pull/277) añade zap polls (kind 6969), donde los usuarios votan enviando sats y pueden ver listas de votantes con fotos de perfil. [PR #274](https://github.com/zapcooking/frontend/pull/274) rediseña la UX de encuestas para que la interfaz de voto se integre de forma más natural en el feed.

[PR #276](https://github.com/zapcooking/frontend/pull/276) añade escaneo QR basado en cámara al flujo Send Payment e integra [Branta](https://branta.pro/), un servicio de verificación que comprueba si un destino de pago es legítimo antes del envío. Branta revisa destinos de pago contra phishing, address swaps e intercepciones man-in-the-middle antes de enviar. En la implementación de Zap Cooking, un nombre y logo de plataforma verificados por Branta aparecen directamente en el flujo de pago, y los códigos QR habilitados para Branta pueden llevar parámetros `branta_id` y `branta_secret` para que la billetera pueda verificar el destino desde el propio código escaneado.

### diVine sienta bases para búsqueda unificada y endurece la entrega de vídeo

[diVine](https://github.com/divinevideo/divine-mobile), el cliente de vídeos cortos, pasó la semana ajustando búsqueda, navegación del feed, recuperación de reproducción y comportamiento de subida. [PR #2540](https://github.com/divinevideo/divine-mobile/pull/2540) sienta la base para una pantalla de búsqueda unificada, con secciones agrupadas para Videos, People y Tags. [PR #2623](https://github.com/divinevideo/divine-mobile/pull/2623) endurece la paginación a través de feeds de perfil, inbox, notificaciones, listas Discover, classic vines, búsqueda y feeds de grid componibles moviéndolos a un controlador compartido de paginación.

La entrega de vídeo también recibió varias correcciones concretas. [PR #2643](https://github.com/divinevideo/divine-mobile/pull/2643) reintenta fuentes derivadas alojadas por Divine en orden y recurre al blob crudo antes de mostrar un error de reproducción, de modo que fallos transitorios en una fuente no maten la reproducción inmediatamente. [PR #2634](https://github.com/divinevideo/divine-mobile/pull/2634) mantiene las subidas reanudables en la ruta propiedad de Divine cuando la detección de capacidades falla transitoriamente, reduciendo subidas rotas por fallos breves de red. [PR #2637](https://github.com/divinevideo/divine-mobile/pull/2637) también cambia la compuerta de contenido sensible para que los vídeos solo queden estrictamente bloqueados por etiquetas de advertencia reales, no solo por etiquetas de advertencia suministradas por el creador.

### Shopstr añade storefronts personalizados y Milk Market sigue enviando trabajo de marketplace

[Shopstr](https://github.com/shopstr-eng/shopstr), el marketplace basado en Nostr, fusionó [PR #245](https://github.com/shopstr-eng/shopstr/pull/245) añadiendo storefronts personalizados. Esto da a los vendedores una superficie inicial más distintiva en lugar de forzar cada listado a la misma presentación genérica.

[Milk Market](https://github.com/shopstr-eng/milk-market), un marketplace dedicado a la leche, continuó con optimizaciones de storefront ([PR #18](https://github.com/shopstr-eng/milk-market/pull/18)), recuperación de cuenta ([PR #17](https://github.com/shopstr-eng/milk-market/pull/17)), beef splits ([PR #15](https://github.com/shopstr-eng/milk-market/pull/15)), y correcciones de tipado de herramientas MCP ([PR #16](https://github.com/shopstr-eng/milk-market/pull/16)).

### Notedeck añade efectos de sonido y extiende su actualizador hacia Android

[Notedeck](https://github.com/damus-io/notedeck), el cliente de escritorio del equipo Damus, fusionó [PR #1412](https://github.com/damus-io/notedeck/pull/1412) añadiendo un subsistema de efectos de sonido con sonidos de interacción de UI usando rodio, y [PR #1399](https://github.com/damus-io/notedeck/pull/1399) con actualizaciones de Agentium incluyendo un flag de título CLI y carpetas de sesión colapsables. Un [PR #1417](https://github.com/damus-io/notedeck/pull/1417) abierto propone auto-actualización APK vía Nostr/Zapstore en Android, construyendo sobre [el trabajo de actualizador nativo de Nostr de Notedeck de Newsletter #14](/es/newsletters/2026-03-18-newsletter/#notedeck-mueve-el-descubrimiento-de-versiones-a-nostr).

### Nostria añade pistas de relay en reposts y alineación con NIP-98

[Nostria](https://github.com/nostria-app/nostria) fusionó [PR #583](https://github.com/nostria-app/nostria/pull/583) añadiendo pistas de relay [NIP-18](/es/topics/nip-18/) (Reposts) a etiquetas `e` de repost para eventos kind 6 y kind 16, [PR #582](https://github.com/nostria-app/nostria/pull/582) alineando la autenticación HTTP de Brainstorm (kind 27235) con las etiquetas requeridas de [NIP-98](/es/topics/nip-98/) (HTTP Auth), y [PR #576](https://github.com/nostria-app/nostria/pull/576) añadiendo pruebas de validación de schemas Schemata. El cambio NIP-98 significa que Nostria puede autenticarse ante servicios externos usando el mismo formato de autenticación HTTP que otros clientes usan.

### Nostr-Doc añade empaquetado de escritorio y trabajo offline-first

[Nostr-Doc](https://github.com/formstr-hq/nostr-docs), el editor colaborativo de Form*, tuvo una semana ocupada de empaquetado y trabajo de editor. [commit fcdc00a](https://github.com/formstr-hq/nostr-docs/commit/fcdc00a564c8d76f094c586b06efce07592a60e4) añade una app de escritorio, [commit 3977a8e](https://github.com/formstr-hq/nostr-docs/commit/3977a8eb2e62b84a67de756c2776e14de8470927) inicia trabajo de app nativa, y [commit 413a030](https://github.com/formstr-hq/nostr-docs/commit/413a030f5b47fb8e32a5dff81bcef557ad9b5869) empuja la app hacia comportamiento offline-first. Del lado del editor, [commit 1855ce8](https://github.com/formstr-hq/nostr-docs/commit/1855ce86ee83ad504e14e47d9c339baffb114786) añade guardado con Ctrl+S, advertencias de guardado, correcciones de preview de enlaces y renderizado corregido de texto tachado.

### rust-nostr optimiza el parseo NIP-21 y añade soporte NIP-62 del lado relay

[rust-nostr](https://github.com/rust-nostr/nostr) fusionó ocho PRs. El más notable es [PR #1308](https://github.com/rust-nostr/nostr/pull/1308), que optimiza el parseo de URI [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) en `PublicKey::parse` alineándolo con el rendimiento estándar de parseo bech32. Antes, los URI NIP-21 tardaban aproximadamente el doble que las claves bech32 en bruto. El proyecto también tiene cuatro PRs abiertos añadiendo soporte específico de relay para [NIP-62](/es/topics/nip-62/) (Request to Vanish) a través de los backends memory, LMDB, SQLite y database test ([PR #1315](https://github.com/rust-nostr/nostr/pull/1315), [PR #1316](https://github.com/rust-nostr/nostr/pull/1316), [PR #1317](https://github.com/rust-nostr/nostr/pull/1317), [PR #1318](https://github.com/rust-nostr/nostr/pull/1318)).

### nostr-tools añade control de relay bunker y corrige parseo multi-relay NIP-47

[nostr-tools](https://github.com/nbd-wtf/nostr-tools) fusionó [PR #530](https://github.com/nbd-wtf/nostr-tools/pull/530) añadiendo `skipSwitchRelays` a BunkerSignerParams para gestión manual de relays, y [PR #529](https://github.com/nbd-wtf/nostr-tools/pull/529) corrigiendo el parseo de cadenas de conexión [NIP-47](/es/topics/nip-47/) (Nostr Wallet Connect) para soportar múltiples relays como permite la especificación.

### Nostrability integra datos de auditoría Sherlock y publica visión general de Schemata

[Nostrability](https://github.com/nostrability/nostrability), el tracker de interoperabilidad para clientes Nostr, fusionó 14 PRs. [PR #306](https://github.com/nostrability/nostrability/pull/306) integra estadísticas de escaneo Sherlock en el dashboard. Sherlock es la herramienta de auditoría automatizada de Nostrability que se conecta a clientes Nostr, captura los eventos que publican, y valida cada evento contra las definiciones JSON Schema de Schemata para detectar violaciones de especificación. El dashboard ahora muestra tasas de fallo de schema por cliente ([PR #315](https://github.com/nostrability/nostrability/pull/315)) para que los desarrolladores puedan ver qué kinds de evento su cliente implementa mal. [PR #323](https://github.com/nostrability/nostrability/pull/323) renueva el flujo de publicación Nostr para que los anuncios de release corran como un job separado que no puede ser cancelado por pasos previos de CI.

elsat también publicó [Schemata for nostr devs](https://njump.me/naddr1qvzqqqr4gupzq96n3hp2vfmf6z2y8uvvxl97xk86kkalnqghx4p25lzl79c76a7yqy2hwumn8ghj7un9d3shjtnyv9kh2uewd9hj7qgwwaehxw309ahx7uewd3hkctcqz4fnx4rkw3x57nrcwdn8zt22xd982jehfptsgqtrww) el 30 de marzo, describiendo cómo encajan schemata, schemata-codegen y Sherlock y dando números actuales de cobertura: 179 schemas de kinds de evento a través de 65 NIPs, 154 schemas de tags, 13 mensajes de protocolo y 310 eventos de ejemplo.

### Nalgorithm añade generación de digest y caché local de puntuaciones

[Nalgorithm](https://github.com/jooray/nalgorithm), un nuevo proyecto de feed Nostr ordenado por relevancia, inició desarrollo público esta semana. [commit cf6c501](https://github.com/jooray/nalgorithm/commit/cf6c501e754ef95a1b4fecc1a76288471a101f43) establece la web app inicial que obtiene publicaciones de follows y las puntúa contra un prompt de preferencias definido por el usuario. [commit 8e931b6](https://github.com/jooray/nalgorithm/commit/8e931b6ae85d470e73603752134ff49b7ba4bb86) añade una herramienta CLI de digest que convierte las publicaciones mejor clasificadas en un resumen hablado, mientras [commit 4cb9c63](https://github.com/jooray/nalgorithm/commit/4cb9c635489a9a3429e8d71f3861dc2a11624153) añade caché de puntuaciones basada en archivos y evolución incremental del prompt aprendida a partir de likes recientes. [commit c2edfb8](https://github.com/jooray/nalgorithm/commit/c2edfb8b89fadbe0028c3f5729bda7e23b2e3c03) también deja de guardar en caché puntuaciones fallback de lotes fallidos, de modo que un fallo transitorio de scoring no aplaste permanentemente el ranking de una publicación.

### TENEX añade vector store RAG y arranque MCP dirigido

[TENEX](https://github.com/tenex-chat/tenex), el framework de agentes nativo de Nostr que conecta agentes a canales Nostr vía Telegram, fusionó siete PRs esta semana. [PR #101](https://github.com/tenex-chat/tenex/pull/101) añade una abstracción conectable de vector store con backends SQLite-vec, LanceDB y Qdrant, dando a los agentes retrieval-augmented generation sin bloquearse a una sola base de datos vectorial. [PR #102](https://github.com/tenex-chat/tenex/pull/102) hace que el arranque MCP sea dirigido: solo se inician servidores MCP cuyas herramientas un agente realmente usa, en lugar de lanzar todos los servidores ansiosamente en la primera ejecución. [PR #100](https://github.com/tenex-chat/tenex/pull/100) añade una herramienta `send_message` para que agentes con bindings de canal Telegram puedan empujar mensajes de forma proactiva en lugar de solo responder a mensajes entrantes. [PR #106](https://github.com/tenex-chat/tenex/pull/106) evita un spawn de subproceso que disparaba una preasignación de memoria de 9 GB de Bun/JSC leyendo `.git/HEAD` directamente en lugar de ejecutar `git branch`.

### Dart NDK mueve el firmante Amber y añade Alby Go 1-click

[Dart NDK](https://github.com/relaystr/ndk), el Nostr development kit para Flutter, lanzó 11 PRs fusionados. [PR #525](https://github.com/relaystr/ndk/pull/525) mueve el soporte de firmante Amber al paquete ndk_flutter, y [PR #552](https://github.com/relaystr/ndk/pull/552) añade conexión one-click a billetera Alby Go en la app de ejemplo. [PR #502](https://github.com/relaystr/ndk/pull/502) añade un script install.sh para el CLI, y [PR #523](https://github.com/relaystr/ndk/pull/523) elimina la dependencia del verificador Rust en favor de manejo nativo de assets.

## Trabajo de Protocolo y Especificación

### Marmot mueve KeyPackages a eventos direccionables y ajusta las notificaciones push

La [especificación Marmot](https://github.com/marmot-protocol/marmot) fusionó cuatro PRs que cambian cómo el protocolo maneja material de claves y membresía de grupo. [PR #54](https://github.com/marmot-protocol/marmot/pull/54) migra los eventos KeyPackage de `kind:443` regular a `kind:30443` direccionable con una etiqueta `d`, eliminando la necesidad de borrar eventos [NIP-09](/es/topics/nip-09/) durante la rotación de claves. Los eventos direccionables se sobrescriben en su lugar, haciendo que la rotación sea autocontenida. [PR #57](https://github.com/marmot-protocol/marmot/pull/57) permite a usuarios no administradores confirmar propuestas SelfRemove (salida voluntaria de grupo), y [PR #62](https://github.com/marmot-protocol/marmot/pull/62) exige que los administradores renuncien a su estatus de admin antes de usar SelfRemove, previniendo que un admin desaparezca mientras aún mantiene privilegios elevados.

[PR #61](https://github.com/marmot-protocol/marmot/pull/61) ajusta el formato de notificaciones push [MIP-05](/es/topics/mip-05/), haciendo explícitos la codificación base64 de blob único, el versionado, el formato wire del token y el uso de claves x-only. El efecto es una única representación wire definida para blobs de tokens y claves x-only a través de especificación, bibliotecas cliente y backends de apps. La implementación de estos cambios de especificación aterrizó en el stack White Noise esta semana y está cubierta en la [sección anterior de White Noise v2026.3.23](#white-noise-corrige-churn-de-relays-y-amplía-los-controles-del-cliente).

### NIP Updates

Cambios recientes al [repositorio de NIPs](https://github.com/nostr-protocol/nips):

**Fusionados:**

- **[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md): Static Websites** ([PR #1538](https://github.com/nostr-protocol/nips/pull/1538)): Define eventos de manifiesto kind `15128` (sitio raíz) y kind `35128` (sitio nombrado) para alojar sitios web estáticos bajo pares de claves Nostr usando almacenamiento Blossom. Ver el [deep dive abajo](#nip-deep-dive-nip-5a-sitios-web-estáticos).

- **[NIP-30](/es/topics/nip-30/) (Custom Emoji): Permitir guiones en shortcodes** ([PR #2297](https://github.com/nostr-protocol/nips/pull/2297)): Actualiza la descripción de shortcode para incluir guiones. Los shortcodes con guiones se han usado en la práctica desde que se introdujo el NIP, así que la especificación ahora documenta el uso actual.

**PRs Abiertos y Discusiones:**

- **NIP-C1: Agent TUI Messages** ([PR #2295](https://github.com/nostr-protocol/nips/pull/2295)): Propone un formato estructurado de mensajes para que los agentes envíen elementos de UI interactivos a través de DMs cifrados, incluyendo payloads tipados `text`, `buttons`, `card` y `table`. El borrador mantiene todo dentro del contenido JSON de DMs existentes de [NIP-17](/es/topics/nip-17/) y [NIP-04](/es/topics/nip-04/). No define un nuevo kind de evento, y usa un formato simple de callback string para respuestas de botones.

- **NIP-95: Hybrid Peer-to-Peer Relay Protocol** ([PR #2293](https://github.com/nostr-protocol/nips/pull/2293)): Propone un modelo híbrido de relay donde los relays siguen siendo autoritativos pero también pueden coordinar distribución peer-to-peer de eventos recientes sobre WebRTC. El borrador introduce mensajes de relay como `PEER_REGISTER`, `PEER_REQUEST` y `PEER_OFFER`, con clientes estables actuando como Super Peers y el relay actuando como nodo semilla y fallback.

- **NIP-B9: Zap Poll Events** ([PR #2284](https://github.com/nostr-protocol/nips/pull/2284)): Reabre la antigua idea de NIP-69 zap-poll ahora que [NIP-88](https://github.com/nostr-protocol/nips/blob/master/88.md) (Polls) cubre encuestas gratuitas. El borrador usa definiciones de encuesta kind `6969` y zaps kind `9734` como votos, convirtiéndolo en un sistema de encuestas pagadas con resistencia económica a Sybil. Complementa las encuestas gratuitas de una-clave-un-voto.

- **NIP-AD: Super Zap** ([PR #2289](https://github.com/nostr-protocol/nips/pull/2289)): Propone una convención donde los zaps enviados a la pubkey de un relay o a la pubkey de un cliente se muestran como notas promocionales especializadas, convirtiendo efectivamente los recibos de zap en una superficie publicitaria. Los operadores de relay y clientes publicarían perfiles con `lud16`, obtendrían esos recibos, extraerían el contenido incrustado de descripciones de zap, y opcionalmente fijarían umbrales mínimos de sats para suprimir spam.

- **NIP-XX: Agent Reputation Attestations** ([PR #2285](https://github.com/nostr-protocol/nips/pull/2285)): Propone kind `30085` como evento reemplazable parametrizado para atestaciones estructuradas de reputación sobre agentes Nostr. El borrador evita una puntuación global única haciendo que la reputación dependa del observador, añade decaimiento temporal para que las atestaciones antiguas pierdan peso, soporta valoraciones negativas con requisitos de evidencia, y esboza tanto puntuación ponderada simple como puntuación por diversidad de grafo para una mejor resistencia Sybil.

- **NIP-XX: Paid API Service Announcements** ([PR #2291](https://github.com/nostr-protocol/nips/pull/2291)): Propone eventos direccionables kind `31402` para anunciar APIs HTTP pagadas, con Nostr manejando descubrimiento y el pago a través de HTTP 402. El borrador está orientado a tags para que los relays puedan filtrar por métodos de pago, precios y capacidades sin parsear contenido JSON, y permite request y response schemas opcionales para que clientes o agentes puedan autogenerar llamadas.

- **NIP-XX: Key Derivation from LNURL-auth via SplitSig** ([PR #2294](https://github.com/nostr-protocol/nips/pull/2294)): Propone derivar un par de claves Nostr a partir de una firma ECDSA LNURL-auth combinada con un nonce aleatorio del lado cliente. La fórmula de derivación es `nsec = SHA256(ecdsa_signature || nonce)`. El servidor ve la firma ECDSA (inherente al handshake LNURL-auth) pero nunca ve el nonce, y el navegador genera el nonce pero no controla la firma. Ninguna pieza por sí sola puede derivar el nsec. El resultado pretendido es que la misma billetera Lightning produzca la misma clave Nostr a través de dispositivos, con la billetera como ancla de recuperación y ningún servidor capaz de reconstruir la clave privada.

- **[NIP-55](/es/topics/nip-55/): Documentar campo rejected** ([PR #2290](https://github.com/nostr-protocol/nips/pull/2290)): Documenta el campo `rejected` para respuestas de firmantes basadas en intent, formalizando el comportamiento que [la corrección de Amethyst v1.07.x](#amethyst-lanza-notas-fijadas-gestión-de-relays-y-request-to-vanish) tuvo que sortear.

## NIP Deep Dive: NIP-5A (Static Websites)

[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md) define cómo alojar sitios web estáticos bajo pares de claves Nostr, usando dos kinds de evento e infraestructura existente de almacenamiento de blobs para convertir eventos firmados en páginas web servidas. La [especificación](https://github.com/nostr-protocol/nips/blob/master/5A.md) se fusionó el 25 de marzo vía [PR #1538](https://github.com/nostr-protocol/nips/pull/1538).

El modelo usa kind `15128` para un sitio raíz, uno por pubkey, y kind `35128` para sitios nombrados identificados por una etiqueta `d`. Cada manifiesto mapea rutas URL absolutas a hashes SHA256. Aquí hay un manifiesto de sitio raíz:

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["path", "/favicon.ico", "fedcba0987654321fedcba0987654321fedcba0987654321fedcba0987654321"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["description", "A static website hosted on Nostr"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

El flujo de servicio funciona en tres pasos. Un servidor host recibe una solicitud HTTP, extrae la pubkey del autor desde el subdominio (ya sea un npub para sitios raíz o una pubkey codificada en base36 para sitios nombrados), obtiene la lista de relays del autor vía [NIP-65](/es/topics/nip-65/), y consulta el manifiesto del sitio. Una vez encontrado el manifiesto, el servidor resuelve la ruta solicitada a un hash de contenido, descarga el blob correspondiente desde el servidor o servidores Blossom listados en las etiquetas `server`, y lo devuelve.

El formato DNS del subdominio está especificado de forma estricta. Los sitios raíz usan el npub estándar como subdominio. Los sitios nombrados usan una codificación base36 de 50 caracteres de la pubkey en bruto seguida del valor de la etiqueta `d`, todo en una sola etiqueta DNS. Debido a que las etiquetas DNS están limitadas a 63 caracteres y la codificación base36 siempre ocupa 50, la etiqueta `d` queda limitada a 13 caracteres. La especificación también exige que las etiquetas `d` coincidan con `^[a-z0-9-]{1,13}$` y no terminen con guion, previniendo ambigüedades de resolución DNS.

Usar hashes de contenido significa que el mismo sitio puede servirse desde distintos servidores host, y la integridad del archivo es verificable sin confiar en el servidor. Un servidor host no necesita almacenar archivos por sí mismo. Los obtiene bajo demanda desde Blossom usando los hashes del manifiesto. Eso significa que el autor controla qué se sirve, el servidor Blossom almacena los archivos en bruto, y el servidor host solo conecta ambos. Cualquiera de estos tres componentes puede reemplazarse de forma independiente.

Las implementaciones existentes incluyen [nsite](https://github.com/lez/nsite), el servidor host que resuelve manifiestos y sirve archivos, y [nsite-manager](https://github.com/hzrd149/nsite-manager), una UI para construir y publicar manifiestos. La especificación también añadió una etiqueta `source` para enlazar al repositorio del código fuente del sitio, y la actualización de README fusionada por separado en [PR #2286](https://github.com/nostr-protocol/nips/pull/2286) registró tanto kind `15128` como `35128` en el índice de kinds del NIP.

## NIP Deep Dive: NIP-62 (Request to Vanish)

[NIP-62](https://github.com/nostr-protocol/nips/blob/master/62.md) define kind `62` como una solicitud a relays para eliminar todos los eventos de la pubkey que la solicita. La [especificación](https://github.com/nostr-protocol/nips/blob/master/62.md) tiene motivación legal: en jurisdicciones con leyes de derecho al olvido, disponer de una solicitud de eliminación estandarizada y firmada da a los operadores de relays una señal clara para actuar.

```json
{
  "id": "a7b8c9d0e1f23456789012345678901234567890abcdef1234567890abcdef12",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1743465600,
  "kind": 62,
  "tags": [
    ["relay", "wss://relay.example.com"]
  ],
  "content": "Requesting deletion of all events from this relay.",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

La especificación separa solicitudes de desaparición dirigidas y globales. Una solicitud dirigida incluye etiquetas `relay` específicas identificando qué relays deben actuar. Una solicitud global usa la cadena literal `ALL_RELAYS` como valor de la etiqueta relay, pidiendo a cada relay que vea el evento que elimine todos los eventos de esa pubkey. Los relays que cumplan también deben asegurar que los eventos eliminados no puedan volver a re-publicarse en ese relay, haciendo que la eliminación quede pegajosa.

NIP-62 va más allá de [NIP-09](/es/topics/nip-09/) (Event Deletion) tanto en alcance como en intención. NIP-09 permite borrar eventos individuales, y los relays MAY cumplir. NIP-62 solicita la eliminación de todo, y la especificación dice que los relays MUST cumplir si su URL está etiquetada. También pide a los relays borrar eventos [NIP-59](/es/topics/nip-59/) (Gift Wrap) que tengan una p-tag con la pubkey solicitante, lo que significa que los DMs entrantes se limpian junto con los propios eventos del usuario. Publicar una eliminación NIP-09 contra una solicitud de desaparición NIP-62 no tiene efecto: una vez que desapareces, no puedes des-desaparecer borrando la solicitud de desaparición.

Esta semana, [Amethyst v1.07.0](#amethyst-lanza-notas-fijadas-gestión-de-relays-y-request-to-vanish) lanzó soporte del lado del cliente para NIP-62, permitiendo a los usuarios iniciar solicitudes de desaparición desde la app. Del lado relay, [rust-nostr](https://github.com/rust-nostr/nostr) tiene cuatro PRs abiertos añadiendo soporte NIP-62 a través de los backends memory, LMDB, SQLite y database test ([PR #1315](https://github.com/rust-nostr/nostr/pull/1315), [PR #1316](https://github.com/rust-nostr/nostr/pull/1316), [PR #1317](https://github.com/rust-nostr/nostr/pull/1317), [PR #1318](https://github.com/rust-nostr/nostr/pull/1318)). Esto coloca el trabajo de soporte en clientes y relays en la misma semana.

El diseño del protocolo plantea una tensión práctica. La propuesta de valor de Nostr incluye resistencia a la censura, lo que significa que los relays no deberían poder impedir la publicación. NIP-62 introduce un caso donde un relay MUST impedir la republicación de una pubkey específica. Las dos propiedades coexisten porque la solicitud está auto-dirigida: estás pidiendo la eliminación de tus propios eventos, no de los de otra persona. La propiedad de resistencia a la censura permanece intacta para todos excepto para la persona que explícitamente decidió salir.

---

Eso es todo por esta semana. ¿Estás construyendo algo o tienes noticias que compartir? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Escríbenos vía DM [NIP-17](/es/topics/nip-17/) (Private Direct Messages)</a> o encuéntranos en Nostr.
