---
title: 'Nostr Compass #13'
date: 2026-03-11
translationOf: /en/newsletters/2026-03-11-newsletter.md
translationDate: 2026-03-11
draft: false
type: newsletters
---

Bienvenido de nuevo a Nostr Compass, tu guía semanal de Nostr.

**Esta semana:** [Shopstr](https://github.com/shopstr-eng/shopstr) y [Milk Market](https://github.com/shopstr-eng/milk-market) añaden superficies MCP para comercio impulsado por agentes, mientras [OAuth Bunker](https://github.com/flox1an/oauth-bunker), [Amber](https://github.com/greenart7c3/Amber) y [strfry](https://github.com/hoytech/strfry) añaden relay-auth y soporte de eventos protegidos de [NIP-42](/es/topics/nip-42/) (Autenticación de clientes a relays) a software de apps, firmantes y relays. [Route96](https://github.com/v0l/route96) lanza dos versiones alrededor de etiquetado de AI, colas de moderación, perceptual hashing y documentación de servidor legible por máquinas. [Samizdat](https://github.com/satsdisco/samizdat), ya disponible en la web, lanzó su primera alpha para Android y después añadió soporte de firmante [NIP-55](/es/topics/nip-55/) (Aplicación firmante de Android). [Formstr](https://github.com/formstr-hq/nostr-forms) añade registro mediante [NIP-49](/es/topics/nip-49/) (Cifrado de clave privada), [Amethyst](https://github.com/vitorpamplona/amethyst) lanza trabajo de resolución [NIP-05](/es/topics/nip-05/) (Verificación de dominio) basado en Namecoin, [Mostro](https://github.com/MostroP2P/mostro) lanza [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4), y el repositorio de NIPs fusiona [NIP-91](/es/topics/nip-91/) (Operador AND para filtros) y guía defensiva para [NIP-66](/es/topics/nip-66/) (Descubrimiento de relays y monitoreo de liveness).

## Noticias

### Shopstr y Milk Market abren superficies MCP para comercio

[Shopstr](https://github.com/shopstr-eng/shopstr), el marketplace peer-to-peer con pagos Lightning y Cashu, fusionó [PR #234](https://github.com/shopstr-eng/shopstr/pull/234) ([commit 94ef7d1](https://github.com/shopstr-eng/shopstr/commit/94ef7d1a4519e8e0158668d13c8cb8684b1d46e2)), añadiendo un servidor MCP con autenticación por API key para gestión de cuentas de agentes. El cambio añade `.well-known/agent.json` para descubrimiento de agentes, endpoints MCP de onboarding y estado, rutas de creación de pedidos y verificación de pagos, herramientas dedicadas de compra y lectura, y una pantalla de ajustes para API keys. [PR #236](https://github.com/shopstr-eng/shopstr/pull/236) amplía eso con acciones del lado del vendedor para mensajes, direcciones, actualizaciones de pedidos y selección de especificaciones de producto. Una corrección de seguridad en [PR #235](https://github.com/shopstr-eng/shopstr/pull/235) reemplaza el hashing de API keys con SHA-256 de una sola iteración por PBKDF2 con sal y 100.000 iteraciones.

Los agentes pueden leer anuncios de [NIP-99](/es/topics/nip-99/) (Anuncios clasificados) y avanzar por el checkout usando los flujos de pago existentes de [NIP-47](/es/topics/nip-47/) (Nostr Wallet Connect) y [NIP-60](/es/topics/nip-60/) (Cashu Wallet) sin raspar páginas ni hacer ingeniería inversa del comportamiento del cliente.

[Milk Market](https://github.com/shopstr-eng/milk-market), un marketplace de comida en Nostr en [milk.market](https://milk.market), incorporó la misma base de MCP y API key en [commit da6c0b4](https://github.com/shopstr-eng/milk-market/commit/da6c0b499494b4e4861c4ff8a220e066c46285b3). [PR #10](https://github.com/shopstr-eng/milk-market/pull/10) añade pedidos por suscripción, cambios de dirección de envío después de la compra y manejo de checkout multi-merchant y multi-moneda para Stripe y otras rutas de pago fiat. Un [PR #11](https://github.com/shopstr-eng/milk-market/pull/11) posterior corrige un bug de inicialización de base de datos al arrancar en el que la tabla de publicaciones fallidas a relays no se creaba en instalaciones nuevas, causando errores 500 en la primera carga. La interfaz orientada a agentes funciona con checkout nativo de Bitcoin en Shopstr o checkout mixto fiat y Bitcoin en Milk Market.

### NIP-42 relay auth en bunker, firmante y relay

[OAuth Bunker](https://github.com/flox1an/oauth-bunker), un bunker de [NIP-46](/es/topics/nip-46/) (Nostr Connect) que conecta proveedores OAuth con firma Nostr, añadió login con [NIP-07](/es/topics/nip-07/) (Firmante de extensión de navegador), selección automática de identidad única y limpieza para identidades eliminadas ([commit f0c7683](https://github.com/flox1an/oauth-bunker/commit/f0c7683cb2374fd9a3ebd1b186055da8abd2c2ff)). Cuando solo existe una identidad, el bunker ahora la selecciona automáticamente en lugar de pedir confirmación. Eliminar una identidad también elimina sus asignaciones y conexiones colgantes. [Commit 6b8796c](https://github.com/flox1an/oauth-bunker/commit/6b8796c6c59c7d48dc1ede92d6de6bf54feb56cc) añade una ruta de configuración `ALWAYS_ALLOWED_KINDS` para usuarios asignados, con kind `30078` de datos específicos de aplicación como valor predeterminado, para que las identidades delegadas puedan escribir en almacenamiento específico de la app sin aprobación por evento.

[Amber](https://github.com/greenart7c3/Amber), el principal firmante [NIP-55](/es/topics/nip-55/) para Android, lanzó [v4.1.3-pre4](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3-pre4) con cuatro pre-releases a lo largo de la semana. [PR #317](https://github.com/greenart7c3/Amber/pull/317) añade manejo de autenticación de relay [NIP-42](/es/topics/nip-42/) para solicitudes kind `22242`. La implementación añade una nueva columna de base de datos que rastrea permisos específicos por relay con un índice único sobre `(pkKey, type, kind, relay)`. Los usuarios ven una pantalla de auth dedicada donde pueden permitir o denegar por relay o en todos los relays con un alcance comodín `*`, y persistir esa elección. Los permisos comodín limpian todas las entradas específicas por relay para un kind. [PR #318](https://github.com/greenart7c3/Amber/pull/318) lo sigue con una refactorización de las pantallas de solicitudes multievento para mostrar detalles en línea usando tarjetas composables en lugar de navegar a una pantalla separada. La release también actualiza los relays de perfil predeterminados, añade visualización de solicitudes en bottom sheet y corrige un crash en dispositivos MediaTek desactivando el keystore StrongBox.

En el lado del relay, [strfry PR #156](https://github.com/hoytech/strfry/pull/156) implementa manejo de auth NIP-42 para [NIP-70](/es/topics/nip-70/) (Eventos protegidos), y [PR #176](https://github.com/hoytech/strfry/pull/176) rechaza reposts que incrustan eventos protegidos.

### Notedeck añade límites de relay NIP-11 y funciones de Agentium

[Notedeck](https://github.com/damus-io/notedeck), el cliente de escritorio nativo del equipo de Damus, fusionó 14 PRs esta semana. [PR #1316](https://github.com/damus-io/notedeck/pull/1316) añade obtención de limitaciones de relay de [NIP-11](/es/topics/nip-11/) (Documento de información del relay), de modo que todos los relays outbox ahora respetan `max_message_length` y `max_subscriptions` del documento de información del relay. La implementación incluye procesamiento de trabajos en segundo plano, exponential backoff con jitter para reintentos de conexión y encabezados HTTP Accept personalizados. [PR #1312](https://github.com/damus-io/notedeck/pull/1312) corrige un bug por el que los DMs a veces no cargaban después de cambiar de cuenta, y [PR #1333](https://github.com/damus-io/notedeck/pull/1333) añade un mecanismo de backoff a la comunicación multicast con relays para evitar spam de difusión en caso de errores.

El subsistema Agentium (la UI integrada de agente de código de Notedeck, llamada internamente "Dave") recibió pegado de imágenes desde el portapapeles, configuraciones de ejecución con nombre que se sincronizan entre dispositivos vía eventos kind `31991` ([NIP-33](/es/topics/nip-33/) (Eventos reemplazables parametrizados)), un creador de git worktree y un selector de modelos para elegir backends por sesión ([PR #1336](https://github.com/damus-io/notedeck/pull/1336)). [PR #1338](https://github.com/damus-io/notedeck/pull/1338) integra `egui_kittest` para pruebas de UI headless, y [PR #1339](https://github.com/damus-io/notedeck/pull/1339) añade una tarjeta de panel que rastrea nuevas creaciones de listas de contactos por cliente. Un [PR #1314](https://github.com/damus-io/notedeck/pull/1314) abierto porta a Notedeck la resolución Namecoin de NIP-05 de Amethyst con búsquedas ElectrumX, enrutamiento Tor SOCKS5 e integración en la barra de búsqueda.

### diVine lanza v1.0.6 con infraestructura de pruebas E2E e importación NIP-49

[diVine](https://github.com/divinevideo/divine-mobile), el cliente de vídeo corto en bucle que restaura archivos de Vine en [divine.video](https://divine.video), lanzó [v1.0.6](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.6) con 127 PRs fusionados. La versión añade importación de cuentas [NIP-49](/es/topics/nip-49/), soporte externo de [NIP-05](/es/topics/nip-05/), manejo de múltiples cuentas, builds para macOS y Linux experimental, y una biblioteca rediseñada de borradores y clips respaldada por almacenamiento local.

En el lado de ingeniería, [PR #1928](https://github.com/divinevideo/divine-mobile/pull/1928) añade una infraestructura completa de pruebas de integración E2E usando Patrol para automatización de UI nativa contra un stack backend Docker (relay, API, Blossom, Postgres, Redis, ClickHouse). Cinco pruebas del recorrido de auth cubren registro, verificación, restablecimiento de contraseña, expiración de sesión y refresh de token. [PR #2105](https://github.com/divinevideo/divine-mobile/pull/2105) cambia la carga de vídeo de HLS-first a MP4 directo con fallback automático a HLS, reduciendo los tiempos de carga de 30-60 segundos a casi instantáneos. [PR #2076](https://github.com/divinevideo/divine-mobile/pull/2076) guarda en caché la respuesta de la API del feed principal en SharedPreferences para mostrarla al instante en arranque en frío. [PR #2104](https://github.com/divinevideo/divine-mobile/pull/2104) impone etiquetas de contenido `ai-generated` como ocultas en los feeds, y [PR #2100](https://github.com/divinevideo/divine-mobile/pull/2100) añade un ajuste de seguridad para mostrar solo vídeos alojados por diVine. La migración de caché de perfiles de Hive a Drift continúa en [PR #1881](https://github.com/divinevideo/divine-mobile/pull/1881), [PR #1883](https://github.com/divinevideo/divine-mobile/pull/1883) y [PR #1903](https://github.com/divinevideo/divine-mobile/pull/1903), reemplazando aproximadamente 1.074 líneas de código Hive por DAOs de Drift.

### Vector v0.3.2 lanza sincronización negentropy NIP-77 y mejoras de MLS

[Vector](https://github.com/VectorPrivacy/Vector), un mensajero de escritorio enfocado en privacidad que usa cifrado de grupo MLS con [NIP-17](/es/topics/nip-17/) (Mensajes directos privados) y cifrado [NIP-44](/es/topics/nip-44/) (Payloads cifrados), lanzó [v0.3.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.2). El cambio principal es negentropy NIP-77 para sincronización de grupos MLS ([commit b06adf4](https://github.com/VectorPrivacy/Vector/commit/b06adf4af2673fb5ac5add01356999ea70628eac)), que recupera mensajes perdidos mucho más rápido usando arranque en paralelo. La release también añade un motor de audio reconstruido con soporte completo para Linux, spoilers de imágenes con vistas previas difuminadas, hipervínculos clicables con rich link previews, pings `@mention` con `@everyone` para admins de grupo, autocompletado de shortcode de emoji, silenciamiento de grupos, tocar para reaccionar sobre reacciones existentes y cargas de archivos cancelables. Vector filtra explícitamente eventos de chat grupal NIP-17 ([commit 2179a51](https://github.com/VectorPrivacy/Vector/commit/2179a51c0449b3a70663a1573195b7945adf58ba)), usando MLS exclusivamente para cifrado de grupos.

## Lanzamientos

### Route96 v0.5.0 y v0.5.1

[Route96](https://github.com/v0l/route96), un servidor de medios que soporta Blossom y [NIP-96](/es/topics/nip-96/) (Almacenamiento HTTP de archivos), lanzó [v0.5.0](https://github.com/v0l/route96/releases/tag/v0.5.0) y [v0.5.1](https://github.com/v0l/route96/releases/tag/v0.5.1). v0.5.0 añade etiquetado automatizado de AI, backfill retroactivo para uploads sin etiquetar, colas de moderación para archivos marcados, rechazo de privacidad basado en EXIF y manejo de hashes prohibidos.

v0.5.1 añade hashes perceptuales de imagen, locality-sensitive hashing para búsqueda de imágenes similares, endpoints batch de admin y un [`SKILL.md`](https://github.com/v0l/route96/releases/tag/v0.5.1) publicado que describe la superficie API de Blossom y NIP-96 del servidor para herramientas de agentes. [PR #58](https://github.com/v0l/route96/pull/58) mueve los workers en segundo plano a tareas Tokio totalmente async, y [commit 97b00a3](https://github.com/v0l/route96/commit/97b00a39e27b07053c2ad335dbf475bacba57bf8) añade backoff para evitar hot loops.

### Samizdat v1.0.0-alpha

[Samizdat](https://github.com/satsdisco/samizdat), un lector y publicador de formato largo disponible en [samizdat.press](https://samizdat.press), lanzó su primera build para Android en [v1.0.0-alpha](https://github.com/satsdisco/samizdat/releases/tag/v1.0.0-alpha). La app abre con una página Press curada de artículos largos de Nostr con navegación por pestañas inferiores entre las vistas Press, Feed, Saved y Write. La build para Android añade almacenamiento nativo de claves mediante cifrado con Android Keystore y desbloqueo biométrico, maneja URIs `nostr:` y deep links de `samizdat.press`, y soporta handoff de firmante mediante el selector de apps de Android (Amber, Primal, etc.) en lugar de requerir importación directa de claves. Pull-to-refresh, manejo de safe area en distintos tamaños de pantalla e integraciones nativas de compartir, portapapeles, hápticos y splash screen ahora forman parte del shell Android en lugar del wrapper web.

[Commit d17308f](https://github.com/satsdisco/samizdat/commit/d17308f3c2e6020e14074fbb1c03a8f60f29a3e6) añade firma [NIP-55](/es/topics/nip-55/) basada en intents para flujos de Amber y Primal, y [commit e29dab8](https://github.com/satsdisco/samizdat/commit/e29dab84f7b58edd621f7b86ed7ca6458f965614) reemplaza un workaround de puente JavaScript por un plugin nativo de Capacitor que usa `startActivityForResult`. La app requiere Android 7.0+ (API 24), se distribuye como APK de depuración en esta alpha y todavía carece de notificaciones push. La publicación depende actualmente de una app firmante, mientras que el login con `nsec` cubre lectura local y acceso a la cuenta.

### Calendar by Form* v0.2.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), una app de calendario descentralizada con compartición privada de eventos [NIP-59](/es/topics/nip-59/) (Gift Wrap) disponible en [calendar.formstr.app](https://calendar.formstr.app), lanzó [v0.2.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.0) con [PR #38](https://github.com/formstr-hq/nostr-calendar/pull/38). La release amplía el manejo de eventos recurrentes para [NIP-52](/es/topics/nip-52/) (Eventos de calendario), y avanza más allá de la base de evento único de v0.1.0. Los cambios subyacentes también tocan almacenamiento local de eventos, manejo de firmante y plumbing de notificaciones Android. Esta es la segunda aplicación activa de la organización Formstr tras la migración del repositorio del mes pasado.

### Mostro v0.16.4

[Mostro](https://github.com/MostroP2P/mostro), el exchange peer-to-peer de Bitcoin construido sobre Nostr, lanzó [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4). Las correcciones de restauración de sesión de disputa ([PR #599](https://github.com/MostroP2P/mostro/pull/599)) y cierre automático ([PR #606](https://github.com/MostroP2P/mostro/pull/606)) [cubiertas la semana pasada](/es/newsletters/2026-03-04-newsletter/) están incluidas. Nuevo en esta release: [PR #625](https://github.com/MostroP2P/mostro/pull/625) añade un campo `days` a eventos de valoración de usuario de kind `38384`, [PR #612](https://github.com/MostroP2P/mostro/pull/612) añade expiración a esos eventos de valoración, y [PR #614](https://github.com/MostroP2P/mostro/pull/614) cambia los eventos de orden para usar ajustes de expiración configurados en vez de una ventana hardcodeada de 24 horas. [PR #622](https://github.com/MostroP2P/mostro/pull/622) añade una comprobación de idempotencia para evitar pagos duplicados de tarifas de desarrollo.

### Mostro Mobile v1.2.1

[Mostro Mobile](https://github.com/MostroP2P/mobile), el cliente Flutter para el exchange P2P Mostro, lanzó [v1.2.1](https://github.com/MostroP2P/mobile/releases/tag/v1.2.1) con 11 nuevas funciones y 11 correcciones de bugs. La release añade renderizado multimedia cifrado en el chat de disputas ([PR #514](https://github.com/MostroP2P/mobile/pull/514)), cierre automático de la UI de disputa cuando las órdenes alcanzan estado terminal ([PR #503](https://github.com/MostroP2P/mobile/pull/503)), escaneo QR para importación de billetera NWC ([commit 12eaee4](https://github.com/MostroP2P/mobile/commit/12eaee4d154fa31b07f82b96819de520e825aee6)), traducciones al francés y manejo de notificaciones push FCM. [PR #496](https://github.com/MostroP2P/mobile/pull/496) corrige un bug de padding de firma Schnorr fijando la dependencia bip340 a v0.2.0.

### 0xchat v1.5.4

[0xchat](https://github.com/0xchat-app/0xchat-app-main), el cliente de mensajería estilo Telegram con soporte de Cashu, lanzó [v1.5.4](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.4-release) centrado en correcciones para Linux de escritorio: iconos de dock en AppImage, renderizado de emoji, congelamientos del menú contextual y bloqueos de la UI al responder o copiar. La release también corrige problemas de upload de imágenes e integración con npub.cash. [PR #49](https://github.com/0xchat-app/0xchat-app-main/pull/49) elimina reconstrucciones innecesarias de la UI al quitar un temporizador de sondeo de 3 segundos que forzaba repintados glassmorphic sin hacer nada, y desbloquea la inicialización de login al cargar la caché de eventos de forma concurrente en lugar de bloquear el arranque de relay, contactos y canales.

### Keep v0.6.0

[Keep](https://github.com/privkeyio/keep-android), un firmante threshold FROST para Android con soporte de [NIP-55](/es/topics/nip-55/) y [NIP-46](/es/topics/nip-46/), lanzó [v0.6.0](https://github.com/privkeyio/keep-android/releases/tag/v0.6.0) y [v0.6.1](https://github.com/privkeyio/keep-android/releases/tag/v0.6.1). v0.6.0 añade coordinación de wallet descriptors y UI de gestión, un flujo de backup/restore con autenticación biométrica ([PR #184](https://github.com/privkeyio/keep-android/pull/184)), recuperación de nsec a partir de threshold shares ([PR #187](https://github.com/privkeyio/keep-android/pull/187)), generación de marcos QR animados multiplataforma vía Rust UniFFI ([PR #188](https://github.com/privkeyio/keep-android/pull/188)) y una pista de auditoría de firma con verificación de cadena ([PR #189](https://github.com/privkeyio/keep-android/pull/189)). v0.6.1 cambia la licencia de AGPL-3.0 a MIT ([PR #191](https://github.com/privkeyio/keep-android/pull/191)).

### njump v0.3.0

[njump](https://github.com/fiatjaf/njump), la gateway estática para ver contenido Nostr en [njump.me](https://njump.me), lanzó [v0.3.0](https://github.com/fiatjaf/njump/releases/tag/v0.3.0) con un cambio disruptivo en el parseo de códigos `note1` y una actualización de la biblioteca Nostr subyacente.

### Roadstr v0.1.1

[Roadstr](https://github.com/jooray/roadstr), una app descentralizada para reportes de eventos en carretera usando Nostr, lanzó su demo inicial [v0.1.1](https://github.com/jooray/roadstr/releases/tag/v0.1.1). La app muestra eventos de carretera en un mapa usando vector tiles de openfreemap.org.

### Bitcredit v0.5.3

[Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core), una aplicación de e-bills con capa de transporte Nostr y relay dedicado en [bit.cr](https://www.bit.cr/), lanzó [v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3). [PR #846](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846) añade campos `payment_actions` y `bill_state` a la API para estado de pago y aceptación, y [PR #849](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849) corrige el manejo de direcciones de firma para firmantes anónimos.

### OpenChat v0.1.0-alpha.3

[OpenChat](https://github.com/DavidGershony/openChat), una aplicación de chat construida sobre las bibliotecas .NET MLS y C# del protocolo Marmot, lanzó [v0.1.0-alpha.3](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.3). La release añade soporte para firmantes externos de Amber y flujos de [NIP-46](/es/topics/nip-46/) ([commit e568d97](https://github.com/DavidGershony/openChat/commit/e568d979fe15eead19172f2eb6f8cf26ca845247)), mueve la persistencia del estado MLS al servicio MLS para eliminar pérdida de datos en ventanas de crash ([commit 4720bc8](https://github.com/DavidGershony/openChat/commit/4720bc8625136a0d5b0e23322bc0c50cd80577e8)) y publica builds para Windows, Linux y Android mediante un nuevo pipeline CI.

### OpenSignal v1.0.0

[OpenSignal](https://github.com/turizspace/opensignal), un trading copilot Kotlin Multiplatform para Nostr, lanzó [v1.0.0](https://github.com/turizspace/OpenSignal/releases/tag/v1.0.0). La release empaqueta módulos KMP compartidos para lógica de dominio, renderizado de gráficos, autenticación y publicación Nostr, soporte de upload Blossom [NIP-96](/es/topics/nip-96/) y hooks de inferencia AI basados en ONNX a través de shells Desktop y Android. La arquitectura publicada también incluye un servicio AI FastAPI para análisis de capturas de gráficos, pipelines de entrenamiento de modelos y un motor de riesgo que produce planes de trading estructurados con tamaños y advertencias. El login soporta tanto claves `nsec` en bruto como firmantes externos, y el flujo de salida termina en publicación de eventos Nostr en lugar de análisis solo local.

## Actualizaciones de proyectos

### Formstr

[Formstr](https://github.com/formstr-hq/nostr-forms), la alternativa a Google Forms sobre Nostr, fusionó [PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) ([commit e9c4fd5](https://github.com/formstr-hq/nostr-forms/commit/e9c4fd5dadfa0b83f1e87d7596eaf35f9fdb7da8)), añadiendo un flujo de registro que usa claves privadas cifradas [NIP-49](/es/topics/nip-49/) (Cifrado de clave privada). Antes de este cambio, los usuarios necesitaban una extensión de navegador [NIP-07](/es/topics/nip-07/) o pegar un `nsec` en bruto para usar Formstr. El nuevo flujo genera un par de claves del lado del cliente, cifra la clave privada con una contraseña elegida por el usuario mediante el esquema scrypt + XChaCha20-Poly1305 de NIP-49 y almacena la cadena `ncryptsec` resultante. Los usuarios pueden volver a iniciar sesión con su contraseña sin instalar una extensión firmante. La gestión de claves se mantiene del lado del cliente en todo momento.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), el cliente Android con muchas funciones, fusionó cuatro PRs que entregan el trabajo de resolución [NIP-05](/es/topics/nip-05/) respaldado por Namecoin que estaba [abierto la semana pasada](/es/newsletters/2026-03-04-newsletter/). [PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734) añade verificación NIP-05 resistente a la censura mediante ElectrumX para identificadores `.bit`, `d/` e `id/`. Cuando Amethyst detecta uno de estos sufijos en un campo NIP-05, consulta un servidor ElectrumX-NMC para el historial de transacciones del nombre, analiza el script `NAME_UPDATE` de la última salida para extraer la pubkey Nostr y rechaza nombres con más de 36.000 bloques de antigüedad (la ventana de expiración de Namecoin). Las conexiones ElectrumX se enrutan por SOCKS5 cuando Tor está habilitado, con selección dinámica de servidor entre endpoints clearnet y `.onion`. Una caché LRU con TTL de una hora evita consultas repetidas a la blockchain.

[PR #1771](https://github.com/vitorpamplona/amethyst/pull/1771) corrige condiciones de carrera y exactitud del resolvedor en ese flujo. [PR #1785](https://github.com/vitorpamplona/amethyst/pull/1785) permite a nuevos usuarios importar una lista de follows durante el registro tanto desde identificadores NIP-05 ordinarios como desde los respaldados por Namecoin. [PR #1786](https://github.com/vitorpamplona/amethyst/pull/1786) añade ajustes personalizados de servidor ElectrumX para que los usuarios puedan elegir qué servidor gestiona sus búsquedas.

### nostr-idb

[nostr-idb](https://github.com/hzrd149/nostr-idb), una biblioteca que proporciona métodos auxiliares para almacenar eventos Nostr en IndexedDB, fusionó [PR #6](https://github.com/hzrd149/nostr-idb/pull/6) añadiendo soporte para filtros de etiquetas AND de [NIP-91](/es/topics/nip-91/). El cambio añade semántica de intersección al emparejamiento de filtros del lado del cliente para que las consultas en IndexedDB puedan requerir todos los valores de etiqueta listados en lugar de cualquiera de ellos. [PR #8](https://github.com/hzrd149/nostr-idb/pull/8) actualiza la biblioteca a la interfaz más reciente de NIP-DB, y un [commit b49b3d3](https://github.com/hzrd149/nostr-idb/commit/b49b3d32c575ff8214dc3fb07675109c2a971972) posterior corrige un deadlock en subscribe y elimina nostr-tools como dependencia de producción.

### Pensieve

[Pensieve](https://github.com/andotherstuff/pensieve), un indexador Nostr orientado a archivo con analítica en ClickHouse, fusionó [PR #8](https://github.com/andotherstuff/pensieve/pull/8) añadiendo aplicación de TTL de caché por entrada y coalescencia de misses por clave para reducir picos de CPU en la API. Los endpoints de series temporales de mayor costo (estadísticas de engagement, actividad por hora, actividad por kind) ahora usan TTLs del lado del servidor de 10 minutos en lugar de disparar tormentas de recálculo sincronizado.

### Blossom

[Blossom](https://github.com/hzrd149/blossom), el protocolo y stack de servidor de alojamiento de medios descentralizado, fusionó dos actualizaciones de autorización BUD-11. [PR #91](https://github.com/hzrd149/blossom/pull/91) mueve la autorización opcional a su propio BUD y aclara el papel de las etiquetas `x` y `server`. [PR #93](https://github.com/hzrd149/blossom/pull/93) limpia el comportamiento de auth específico por endpoint y formaliza el encabezado `X-SHA-256` para verificación de uploads. Ambos PRs consolidan la lógica de auth en BUD-11 y eliminan ambigüedades alrededor del hashing de solicitudes en flujos de upload, borrado y gestión de medios.

## Actualizaciones de NIPs

Cambios recientes en el [repositorio de NIPs](https://github.com/nostr-protocol/nips):

**Fusionados:**

- **[NIP-91](/es/topics/nip-91/) (Operador AND para filtros)** ([PR #1365](https://github.com/nostr-protocol/nips/pull/1365)): Añade semántica de intersección para filtros de etiquetas, permitiendo a los relays responder consultas que requieren todos los valores de etiqueta listados en lugar de cualquiera de ellos. Reduce el postfiltrado del lado del cliente y el ancho de banda en consultas con muchas etiquetas.

- **[NIP-66](/es/topics/nip-66/) (Descubrimiento de relays y monitoreo de liveness): medidas defensivas** ([PR #2240](https://github.com/nostr-protocol/nips/pull/2240)): Tras el [trabajo de benchmark outbox cubierto la semana pasada](/es/newsletters/2026-03-04-newsletter/), la especificación ahora añade advertencias sobre rutas problemáticas para los datos de monitoreo de relays. Los clientes no deben requerir eventos de monitoreo kind `30166` para poder funcionar. Un monitor puede estar equivocado, desactualizado o ser malicioso. Se espera que los clientes contrasten fuentes y eviten cortar grandes partes del grafo de relays de un usuario basándose en un solo feed.

- **[NIP-39](/es/topics/nip-39/) (Identidades externas en perfiles): limpieza del registro kind 10011** ([PR #2256](https://github.com/nostr-protocol/nips/pull/2256)): Añade la referencia de kind `10011` directamente a la especificación, alineándola con la implementación de Amethyst [cubierta la semana pasada](/es/newsletters/2026-03-04-newsletter/).

**PRs abiertos y discusiones:**

- **[NIP-70](/es/topics/nip-70/) (Eventos protegidos): rechazar reposts que incrustan eventos protegidos** ([PR #2251](https://github.com/nostr-protocol/nips/pull/2251)): Si un relay aplica NIP-70 al evento original pero acepta reposts que llevan el mismo contenido, la etiqueta `-` no tiene efecto práctico. Este PR añade la regla de que los relays también deben rechazar reposts kind 6 y kind 16 de eventos protegidos. [strfry PR #176](https://github.com/hoytech/strfry/pull/176) ya lo implementa.

- **[NIP-71](/es/topics/nip-71/) (Eventos de vídeo): múltiples pistas de audio** ([PR #2255](https://github.com/nostr-protocol/nips/pull/2255)): Añade etiquetas `imeta` de audio para pistas alternativas, variantes por idioma y streams solo de audio. Un cliente podría mantener un archivo de vídeo estable mientras cambia idiomas de audio, o servir audio como una pista separada para contenido tipo podcast.

- **[NIP-11](/es/topics/nip-11/) (Documento de información del relay) y atributos de relay [NIP-66](/es/topics/nip-66/)** ([PR #2257](https://github.com/nostr-protocol/nips/pull/2257)): Añade un campo estructurado `attributes` a los documentos de información de relay, dando a clientes y herramientas de descubrimiento metadatos legibles por máquinas más allá de la descripción actual en texto libre.

## Profundización NIP: NIP-49 (Cifrado de clave privada)

[NIP-49](/es/topics/nip-49/) define cómo un cliente cifra una clave privada con una contraseña y codifica el resultado como una cadena bech32 `ncryptsec`. [Formstr](#formstr) usa NIP-49 en su nuevo flujo de registro.

El formato no está ligado a un kind de evento dedicado. Un cliente empieza con la clave privada secp256k1 en bruto de 32 bytes, deriva una clave simétrica de la contraseña del usuario con scrypt, cifra la clave usando XChaCha20-Poly1305 y luego envuelve el resultado en una cadena bech32 `ncryptsec`. Un indicador de un byte registra si alguna vez se supo que la clave fue manejada de forma insegura antes del cifrado.

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

El evento JSON anterior es un ejemplo a nivel de aplicación, no un requisito de NIP-49. El NIP estandariza el formato de la clave cifrada. Un cliente puede almacenar el `ncryptsec` localmente, sincronizarlo mediante almacenamiento específico de la app o exportarlo como cadena de respaldo. Las contraseñas se normalizan a Unicode NFKC antes de la derivación de claves para que la misma contraseña descifre de forma consistente entre clientes y plataformas.

La bandera de seguridad de clave de un byte tiene tres valores definidos: `0x00` significa que el historial de manejo de la clave es desconocido, `0x01` significa que se sabe que la clave fue manejada de forma insegura (por ejemplo, pegada como texto plano en un formulario web antes del cifrado), y `0x02` significa que la clave se generó y cifró en un contexto seguro y nunca fue expuesta. Los clientes pueden usar esto para mostrar advertencias al importar claves con historial inseguro conocido.

NIP-49 protege mejor las claves que una exportación `nsec` en texto claro, pero el cifrado solo es tan fuerte como la contraseña y el costo scrypt configurado. Valores `LOG_N` más altos dificultan la adivinación offline, pero ralentizan operaciones de descifrado legítimas. La especificación advierte contra publicar claves cifradas en relays públicos, ya que los atacantes se benefician de recopilar ciphertext para cracking offline. En comparación, la firma remota [NIP-46](/es/topics/nip-46/) evita exponer claves por completo, y la firma Android [NIP-55](/es/topics/nip-55/) mantiene las claves dentro de una app firmante dedicada. NIP-49 cubre un hueco distinto: backup cifrado portable para usuarios que gestionan sus propias claves.

Las implementaciones incluyen [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) para registro, [Amber](https://github.com/greenart7c3/Amber) para backup y restore de ncryptsec, [diVine v1.0.6](#divine-lanza-v106-con-infraestructura-de-pruebas-e2e-e-importacion-nip-49) para importación de cuentas, [Keep v0.6.0](#keep-v060) para exportación de shares FROST y herramientas de gestión de claves como [nsec.app](https://nsec.app) y [Alby](https://github.com/getAlby/hub).

## Profundización NIP: NIP-70 (Eventos protegidos)

[NIP-70](/es/topics/nip-70/) define eventos protegidos. Cuando un evento lleva la etiqueta `["-"]`, un relay debe rechazarlo a menos que el relay requiera autenticación [NIP-42](/es/topics/nip-42/) y la pubkey autenticada coincida con el autor del evento.

El flujo de auth NIP-42 funciona así: el relay envía un desafío `AUTH` que contiene una cadena aleatoria, y el cliente responde con un evento kind `22242` firmado cuyas etiquetas incluyen la URL del relay y el desafío. El relay verifica la firma y comprueba que la pubkey en el evento de auth coincide con la pubkey del evento protegido que se está publicando. Si las pubkeys no coinciden, el relay rechaza el evento con un prefijo de mensaje `restricted`.

El contenido del evento todavía puede ser público. La etiqueta `-` solo controla quién puede publicar el evento en un relay que respeta la etiqueta. Esto cubre feeds semicerrados de [NIP-29](/es/topics/nip-29/) (Grupos simples), espacios de relay solo para miembros y otros contextos en los que el autor quiere limitar la redistribución a través del grafo de relays. NIP-70 es una convención de una sola etiqueta, no un kind de evento nuevo, así que cualquier kind de evento existente puede llevar la etiqueta `-`.

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

Aunque un relay bloquee la publicación por terceros del evento original, alguien puede volver a publicar el contenido dentro de un repost. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) aborda esto exigiendo que los relays también rechacen reposts kind 6 y kind 16 de eventos protegidos. [strfry PR #156](https://github.com/hoytech/strfry/pull/156) añade manejo de auth NIP-42 para eventos protegidos, y [strfry PR #176](https://github.com/hoytech/strfry/pull/176) bloquea reposts que incrustan contenido protegido.

NIP-70 controla el comportamiento del relay. Un destinatario todavía puede copiar el contenido a otro sitio, y la especificación lo dice explícitamente. La etiqueta `-` da a los relays una señal legible por máquinas para rechazar la republicación. En comparación, [NIP-62](/es/topics/nip-62/) (Request to Vanish) pide a los relays que eliminen datos después del hecho, mientras que NIP-70 previene publicación no autorizada en el momento de ingestión. Ambos son complementarios: un autor puede marcar eventos como protegidos para limitar su propagación y más tarde solicitar eliminación si quiere que el contenido se retire de relays que sí lo aceptaron.

---

Eso es todo por esta semana. ¿Estás construyendo algo o tienes noticias para compartir? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Escríbenos por DM de [NIP-17](/es/topics/nip-17/)</a> o encuéntranos en Nostr.
