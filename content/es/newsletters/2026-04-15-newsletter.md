---
title: 'Nostr Compass #18'
date: 2026-04-15
translationOf: /en/newsletters/2026-04-15-newsletter.md
translationDate: 2026-04-22
draft: false
type: newsletters
---

Bienvenido de nuevo a Nostr Compass, tu guía semanal de Nostr.

**Esta semana:** [Amethyst](https://github.com/vitorpamplona/amethyst) fusionó una tanda grande de trabajo en Tor, secp256k1, llamadas WebRTC y [Marmot](/es/topics/marmot/), incluyendo soporte de llamadas para [NIP-AC](/es/topics/nip-ac/) y múltiples carteras [NIP-47](/es/topics/nip-47/). [nstrfy](https://github.com/vcavallo/nstrfy-android) lanzó notificaciones push nativas de Nostr para Android con soporte para [NIP-44](/es/topics/nip-44/), [NIP-55](/es/topics/nip-55/), [NIP-65](/es/topics/nip-65/) y [NIP-40](/es/topics/nip-40/). [HAMSTR](https://github.com/LibertyFarmer/hamstr) añadió transporte Reticulum para eventos Nostr sobre LoRa. [Bloom](https://github.com/nostrnative/bloom), [WaveFunc](https://github.com/zeSchlausKwab/wavefunc), [Snort](https://github.com/v0l/snort) y [Primal Android](https://github.com/PrimalHQ/primal-android-app) encabezaron los lanzamientos de la semana, mientras los análisis de NIP cubren [NIP-29](/es/topics/nip-29/) y [NIP-90](/es/topics/nip-90/).

## Noticias principales

### Amethyst fusiona desktop Tor, secp256k1 en C, llamadas WebRTC y multi-wallet NWC

[Amethyst](https://github.com/vitorpamplona/amethyst) fusionó 29 PRs entre criptografía, networking, llamadas y carteras. Lo más importante fue [PR #2381](https://github.com/vitorpamplona/amethyst/pull/2381), que añade soporte Tor de escritorio con diseño fail-closed, [PR #2374](https://github.com/vitorpamplona/amethyst/pull/2374), que introduce una implementación secp256k1 en C con bindings JNI para acelerar verificación Schnorr, y [PR #2202](https://github.com/vitorpamplona/amethyst/pull/2202), que alinea su implementación MLS pura en Kotlin con RFC 9420 para mejorar la interoperabilidad de [Marmot](/es/topics/marmot/). Una serie de PRs de WebRTC añadió llamadas de voz y vídeo para [NIP-AC](/es/topics/nip-ac/), y [PR #1988](https://github.com/vitorpamplona/amethyst/pull/1988) incorpora soporte multi-wallet para [NIP-47](/es/topics/nip-47/).

### nstrfy lanza notificaciones push nativas de Nostr para Android

[nstrfy](https://github.com/vcavallo/nstrfy-android) debutó como una app Android de notificaciones push basada en eventos kind `7741` en relays Nostr. Soporta payloads en texto plano y cifrados con [NIP-44](/es/topics/nip-44/), puede firmar vía [Amber](https://github.com/greenart7c3/Amber) usando [NIP-55](/es/topics/nip-55/), importa listas de relays desde [NIP-65](/es/topics/nip-65/) y respeta expiración de eventos de [NIP-40](/es/topics/nip-40/). El proyecto complementario [nstrfy.sh](https://github.com/vcavallo/nstrfy.sh) ofrece un cliente bash y una versión web alojada.

### HAMSTR añade Reticulum para Nostr sobre malla LoRa

[HAMSTR](https://github.com/LibertyFarmer/hamstr) añadió [Reticulum](https://reticulum.network/) como backend de transporte para enviar eventos Nostr a través de hardware LoRa sin infraestructura de internet. El proyecto mantiene también sus transportes AX.25 Packet Radio y VARA HF, y sigue soportando zaps de [NIP-57](/es/topics/nip-57/) para que los pagos Lightning offline aparezcan correctamente en clientes como Amethyst y Primal.

## Lanzamientos de esta semana

### Bloom v0.1.0 lanza servidor Blossom y relay autoalojados

[Bloom](https://github.com/nostrnative/bloom) lanzó [v0.1.0](https://github.com/nostrnative/bloom/releases/tag/v0.1.0) como aplicación de escritorio que empaqueta un servidor de medios [Blossom](/es/topics/blossom/) y un relay Nostr en una sola app Tauri. El release ofrece almacenamiento soberano de archivos con content addressing SHA-256, soporte de metadatos de archivo [NIP-94](/es/topics/nip-94/) y resolución de URIs `blossom://`.

### WaveFunc v0.1.0 y v0.1.1 lanzan radio por internet sobre Nostr

[WaveFunc](https://github.com/zeSchlausKwab/wavefunc) salió como directorio y reproductor de radio por internet basado en Nostr. Usa kinds personalizados para emisoras, favoritos, chat en vivo y comentarios, y añade una cartera [NIP-60](/es/topics/nip-60/) con nutzaps, junto con mejoras de escritorio como system tray, media keys y deep linking.

### Snort lanza v0.5.0 a v0.5.3 con endurecimiento de seguridad y mejora de rendimiento

[Snort](https://github.com/v0l/snort) publicó tres releases centrados en una auditoría de seguridad, verificación real de firmas Schnorr, protección reforzada de [NIP-46](/es/topics/nip-46/), mejoras en cifrado de PIN y optimizaciones de rendimiento. También añadió visualización de invoices de pago requerido kind `7000` para [NIP-90](/es/topics/nip-90/) y rehízo el sistema de mensajería para evitar cuellos de botella.

### Primal Android lanza 3.0.21 y rediseña el layout del feed

[Primal Android](https://github.com/PrimalHQ/primal-android-app) publicó [v3.0.21](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.21) con correcciones de votos zap de encuestas, servicio de cartera y reconexión del signer remoto. Después llegaron siete PRs que unifican el layout principal, rediseñan las tarjetas del feed, mejoran tarjetas multimedia, añaden respuestas rápidas compactas y actualizan las app bars.

### Nostria v3.1.19 a v3.1.21 añaden generación local de imágenes

[Nostria](https://github.com/nostria-app/nostria) añadió generación local de imágenes con Janus Pro y WebGPU, además de generación en la nube, chat multimodal y mejoras del editor y del sistema de diálogos. El proyecto sigue ampliando una superficie que en el release anterior ya había sumado signer local y aplicaciones móviles nativas.

### TubeStr v1.0.3 lanza mejoras en feed y estudio

[TubeStr](https://github.com/Tubestr/tubestr-v2) añadió mejoras de feed y studio, renovó la experiencia de onboarding y corrigió una exportación de vídeo defectuosa. La app usa NDK y MDK para compartir medios cifrados entre familiares y planea integración futura con [Blossom](/es/topics/blossom/).

## En desarrollo

### Botburrow inicia desarrollo como plataforma de bots de Marmot

[Botburrow](https://github.com/marmot-protocol/botburrow) es una nueva plataforma autoalojada para gestionar bots con identidad Nostr propia dentro de chats grupales [Marmot](/es/topics/marmot/). Cada bot se conecta a un daemon `wnd`, puede entrar a grupos mediante mensajes Welcome y ejecutar scripts, triggers y tareas programadas.

### Nostr Archives añade relay de trending feeds y resolución de entidades

[Nostr Archives](https://github.com/barrydeen/nostrarchives-api) siguió expandiendo su plataforma de archivado y analítica con filtros de leaderboard, contadores de engagement, resolución directa de entidades Nostr desde rutas URL y una página de documentación de API. El servicio mantiene varios relays especializados, incluyendo búsqueda [NIP-50](/es/topics/nip-50/) y feeds de tendencias.

### Damus corrige la timeline de favoritos

[Damus](https://github.com/damus-io/damus) reescribió `subscribe_to_favorites()` para filtrar in place, reconstruir la deduplicación y persistir la selección de pestaña, corrigiendo fallos en la timeline de favoritos.

### Nostur añade zaps privados y visualización de emoji personalizados

[Nostur](https://github.com/nostur-com/nostur-ios-public) añadió soporte de zaps privados, visualización de emoji personalizados, renderizado corregido de `.webp` animado y detección del formato de audio de mensajes de voz.

### Amber lanza v6.0.1 a v6.0.3 con backups WebDAV y correcciones de reconexión a relays

[Amber](https://github.com/greenart7c3/Amber) publicó tres releases con nuevas opciones de backup, retroceso exponencial para reconexión a relays, actualización de Quartz y correcciones para eventos y flujos de intents. Como firmante [NIP-55](/es/topics/nip-55/), Amber sigue ganando robustez para clientes Android.

### Plektos v0.6.0 se rediseña con temas Ditto

[Plektos](https://github.com/derekross/plektos), construido sobre [NIP-52](/es/topics/nip-52/), añadió temas estilo Ditto, configuración de forma de avatar y una revisión visual amplia, además de atender hallazgos de una revisión completa de código.

### Shadow añade API Nostr OS y app de cartera Cashu

[Shadow](https://github.com/justinmoon/shadow) siguió ampliando su runtime con una app de cartera Cashu, un reproductor de podcasts demo y APIs del sistema para Nostr y audio. También mejoró soporte Linux de escritorio con correcciones de fuentes y rutas XDG.

### Lief corrige login con Amber y añade Zapstore

[Lief](https://gitlab.com/chad.curtis/lief) solucionó un problema de login con [Amber](https://github.com/greenart7c3/Amber), simplificó el flujo de signer nudge, actualizó nostrify y añadió integración con Zapstore.

### Espy rehace el selector de color y corrige login con Amber

[Espy](https://gitlab.com/chad.curtis/espy) renovó su color picker con un arco curvo de saturación, corrigió fallos visuales del anillo de tono y añadió personajes ocultos, mientras compartía con Lief las correcciones de login con Amber y la integración con Zapstore.

### Jumble añade filtros por kind por feed y pestaña de artículos

[Jumble](https://github.com/CodyTseng/jumble) añadió filtrado por kind para cada feed, una pestaña Articles, sincronización del estado leído de notificaciones, modo para ocultar avatares y una corrección de race condition al cambiar de cuenta.

### Primal Web lanza 8 subidas de versión

[Primal Web](https://github.com/PrimalHQ/primal-web-app) publicó versiones 3.0.93 a 3.0.101 con foco en mejoras del chat de live streams, mención de límites, paginación de bookmarks, prevención de likes duplicados y correcciones del relay proxy.

## Trabajo de protocolo y especificación

### Actualizaciones de NIP

En el repositorio de NIPs se fusionó soporte para URLs de clonación `nostr://` en [NIP-34](/es/topics/nip-34/), y siguieron abiertas varias propuestas alrededor de descriptores mínimos de gateways de pago, manifiestos de autodeclaración de relays, datos privados de localización transitoria, programas WASM de [NIP-5C](/es/topics/nip-5c/), payloads grandes para [NIP-44](/es/topics/nip-44/) y la restricción de [NIP-C7](/es/topics/nip-c7/) a vistas de chat.

## NIP Deep Dive: NIP-29 (grupos basados en relay)

[NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md) define mensajería grupal en la que el relay actúa como autoridad para membresía y moderación. Los eventos de usuario llevan una etiqueta `h` con el ID del grupo, las referencias `previous` sirven como defensa frente a rebroadcasts fuera de contexto y los eventos de moderación de la serie `9000` gestionan alta, baja, roles y metadatos. El modelo es adecuado para comunidades públicas o moderadas en las que el operador del relay puede leer el contenido, a diferencia de alternativas cifradas como [Marmot](/es/topics/marmot/) o [NIP-17](/es/topics/nip-17/).

## NIP Deep Dive: NIP-90 (Data Vending Machines)

[NIP-90](https://github.com/nostr-protocol/nips/blob/master/90.md) describe un mercado de cómputo bajo demanda sobre Nostr. Los clientes publican trabajos en el rango `5000-5999`, los proveedores devuelven resultados en `6000-6999` y pueden emitir feedback kind `7000` como `payment-required`, `processing`, `error` o `success`. El diseño permite entradas por URL, texto, eventos o trabajos previos y deja flexible la lógica comercial para acomodar desde transformaciones baratas hasta tareas costosas de GPU.
