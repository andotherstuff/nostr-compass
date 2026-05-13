---
title: 'Nostr Compass #22'
date: 2026-05-13
publishDate: 2026-05-13
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-13-newsletter.md
translationDate: 2026-05-13
description: 'Nostr VPN lanza ocho versiones en una semana culminando en v4.0.10, avanzando desde un flujo de emparejamiento de dispositivos rediseñado hasta un intercambio de AEAD BoringSSL que duplica el rendimiento TCP y lotes sendmmsg; Marmot Protocol (White Noise) lanza una versión frontend que completa la función de bloqueo de usuarios y 31 PRs fusionados en MDK y backend; Grain v0.6.0 añade NIP-40, NIP-50, NIP-70 y NIP-45 en un hito; Citrine v3.0.0-pre1 trae Tor integrado y agregación de relay; Amber v6.1.0-pre2 mejora el flujo de conexión de nueva app; Alby Hub v1.22.2 añade página de IA y Agentes y soporte de Core Lightning; Mostro lanza bonos de tomador concurrentes y v0.11.0 de mostro-core; Jumble lanza cinco versiones de v26.5.2 a v26.5.6; Nostrord lanza v1.0.0 a v1.0.2 con modales de compartir grupo y paquetes de Arch Linux; Flotilla 1.8.0 añade videollamadas, renderizado de email y menciones de sala; Calendar by Formstr v1.5.1 lanza programación de citas y sincronización de calendario Android; Tamagostrich lanza un Tamagotchi NIP-78 descentralizado con recompensas en sats. Dos inmersiones profundas en NIP cubren NIP-78 (datos específicos de la app) y NIP-98 (HTTP Auth).'
---

Bienvenido de nuevo a Nostr Compass, tu guía semanal al desarrollo del protocolo Nostr.

**Esta semana:** [Nostr VPN](https://github.com/mmalmi/nostr-vpn) lanza [ocho versiones en siete días](#nostr-vpn-lanza-ocho-versiones-culminando-en-v4010) desde un flujo de emparejamiento de dispositivos rediseñado hasta un intercambio de AEAD FIPS que aproximadamente duplica el rendimiento TCP. [Marmot Protocol](https://github.com/marmot-protocol) (la base de [White Noise](https://github.com/marmot-protocol/whitenoise)) lanza una [versión frontend que completa la función de bloqueo de usuarios](#marmot-white-noise-lanza-frontend-con-bloqueo-completo-y-31-prs-fusionados-en-mdk-y-backend) y 31 PRs fusionados en MDK y backend. [Grain](https://github.com/0ceanSlim/grain) lanza [v0.6.0](#grain-v060-añade-nip-40-nip-50-nip-70-y-nip-45) con cuatro nuevas implementaciones de NIP en un hito. [Citrine](https://github.com/greenart7c3/Citrine) lanza [v3.0.0-pre1](#citrine-v300-pre1-trae-tor-integrado-y-agregación-de-relay) con Tor integrado y agregación de relay.

## Historias principales

### Nostr VPN lanza ocho versiones culminando en v4.0.10

[Nostr VPN](https://github.com/mmalmi/nostr-vpn), la VPN de malla descentralizada basada en Rust que usa Nostr para el descubrimiento de pares y un protocolo noise respaldado por FIPS para el plano de datos, lanzó ocho versiones desde [v4.0.1](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.1) hasta [v4.0.10](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.10) en macOS, Linux, Windows y Android esta semana.

El cambio principal está en [v4.0.8](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.8): el AEAD se intercambió del backend suave `chacha20poly1305` de RustCrypto al ChaCha20-Poly1305 de BoringSSL en `ring` 0.17, que usa NEON ajustado a mano en aarch64 y AVX2/AVX-512 en x86_64. Los benchmarks de Docker en hardware idéntico mostraron que el rendimiento TCP directo de 2 nodos saltó de 437 a 1097 Mbps.

[v4.0.9](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.9) añadió lotes `sendmmsg(2)` en la ruta de envío UDP, amortizando las llamadas al sistema `sendto` por paquete en lotes de 8 paquetes y empujando TCP de flujo único de 1066 a 1548 Mbps (1,45×). [v4.0.10](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.10) lanzó una revisión completa de UX para el emparejamiento de dispositivos.

### Marmot / White Noise lanza frontend con bloqueo completo y 31 PRs fusionados en MDK y backend

[White Noise](https://github.com/marmot-protocol/whitenoise), la app de mensajería grupal privada construida sobre el protocolo [Marmot](/es/topics/marmot/) basado en MLS, lanzó [v2026.5.7+24](https://github.com/marmot-protocol/whitenoise/releases/tag/v2026.5.7+24) el 7 de mayo como la versión frontend que completa el conjunto de funciones de bloqueo. Un usuario bloqueado ahora está oculto de invitaciones, vistas previas de chat, líneas de tiempo de mensajes, resultados de búsqueda y notificaciones, y sus mensajes ya no cuentan para las insignias de no leídos.

El trabajo de soporte abarca 31 PRs fusionados en MDK y el backend. MDK aportó [PR #258](https://github.com/marmot-protocol/mdk/pull/258) con el formato de cable de extensión v3 y el esquema `disappearing_message_secs`, sentando las bases para los mensajes que desaparecen.

### Grain v0.6.0 añade NIP-40, NIP-50, NIP-70 y NIP-45

[Grain](https://github.com/0ceanSlim/grain), la biblioteca relay y cliente Nostr basada en Go, lanzó [v0.6.0](https://github.com/0ceanSlim/grain/releases/tag/v0.6.0) el 6 de mayo con cuatro nuevas implementaciones de NIP y un pase de endurecimiento de producción. El hito v0.6 añade expiración de eventos [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md), búsqueda de texto completo [NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md), eventos protegidos [NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md) y conteos de eventos [NIP-45](https://github.com/nostr-protocol/nips/blob/master/45.md).

## Lanzamientos de esta semana

### Citrine v3.0.0-pre1 trae Tor integrado y agregación de relay

[Citrine](https://github.com/greenart7c3/Citrine), la app Android que convierte un teléfono en un nodo relay Nostr, lanzó [v3.0.0-pre1](https://github.com/greenart7c3/Citrine/releases/tag/v3.0.0-pre1) como pre-lanzamiento esta semana. Las adiciones principales son soporte Tor integrado para acceso a relay que preserva la privacidad y agregación de relay, donde Citrine puede obtener eventos de múltiples relays upstream y servirlos a clientes locales. [PR #139](https://github.com/greenart7c3/Citrine/pull/139) añade soporte [NIP-77 (Reconciliación Negentropy)](/es/topics/nip-77/) para sincronización eficiente de eventos basada en reconciliación de conjuntos.

### Amber v6.1.0-pre2 mejora el flujo de conexión de nueva app

[Amber](https://github.com/greenart7c3/Amber), la app firmadora Android para [NIP-55 (Aplicación firmadora Android)](/es/topics/nip-55/) y [NIP-46](/es/topics/nip-46/), lanzó [v6.1.0-pre2](https://github.com/greenart7c3/Amber/releases/tag/v6.1.0-pre2). Las correcciones principales: el diálogo del firmador ahora se cierra correctamente después de aceptar una solicitud de bunker, las solicitudes de bunker malformadas muestran una pantalla de solicitud inválida y se añade limitación de tasa para solicitudes de firma basadas en intención.

### Alby Hub v1.22.2 añade página de IA y Agentes y soporte de Core Lightning

[Alby Hub](https://github.com/getAlby/hub), el nodo Lightning autocustodio y servidor Nostr Wallet Connect, lanzó [v1.22.2](https://github.com/getAlby/hub/releases/tag/v1.22.2) con varias adiciones importantes. La nueva página de IA y Agentes expone las capacidades Lightning y NWC de Alby Hub a agentes de IA y herramientas compatibles con MCP. La función más solicitada desde el lanzamiento: Core Lightning (CLN) ahora es un backend compatible junto con LND y LDK.

### Mostro lanza bonos de tomador concurrentes y mostro-core v0.11.0

[Mostro](https://github.com/MostroP2P/mostro), el protocolo de intercambio Bitcoin peer-to-peer en Nostr, fusionó 11 PRs esta semana avanzando la función de bono de tomador que previene el griefing al requerir que ambas partes bloqueen fondos antes de que proceda un intercambio. [PR #733](https://github.com/MostroP2P/mostro/pull/733) implementa bonos de tomador concurrentes donde múltiples tomadores pueden enviar facturas de bono simultáneamente y el primero en bloquear gana.

[mostro-core](https://github.com/MostroP2P/mostro-core) lanzó [v0.11.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.11.0) con las adiciones de biblioteca correspondientes, y [mostro-cli](https://github.com/MostroP2P/mostro-cli) lanzó [v0.15.0](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.15.0).

### Jumble lanza cinco versiones con búsqueda reciente y persistencia de cuenta

[Jumble](https://github.com/CodyTseng/jumble), el cliente Nostr centrado en relay disponible como app web y app de escritorio Electron, lanzó cinco versiones esta semana: [v26.5.2](https://github.com/CodyTseng/jumble/releases/tag/v26.5.2) a [v26.5.6](https://github.com/CodyTseng/jumble/releases/tag/v26.5.6). [v26.5.5](https://github.com/CodyTseng/jumble/releases/tag/v26.5.5) añade historial de búsquedas recientes. Se corrigió un bug crítico de persistencia en [v26.5.6](https://github.com/CodyTseng/jumble/releases/tag/v26.5.6): las cuentas y los datos en caché ahora sobreviven a un reinicio completo de la app.

### Nostrord lanza modales de compartir grupo, carga de medios y paquetes de Arch Linux

[Nostrord](https://github.com/nostrord/nostrord), un cliente Nostr dirigido a grupos basados en relay NIP-29, lanzó [v1.0.0](https://github.com/nostrord/nostrord/releases/tag/v1.0.0), [v1.0.1](https://github.com/nostrord/nostrord/releases/tag/v1.0.1) y [v1.0.2](https://github.com/nostrord/nostrord/releases/tag/v1.0.2) esta semana. [v1.0.1](https://github.com/nostrord/nostrord/releases/tag/v1.0.1) lanza paquetes de Arch Linux via AUR como `nostrord-bin`, y [v1.0.2](https://github.com/nostrord/nostrord/releases/tag/v1.0.2) añade compartir grupos via [PR #49](https://github.com/nostrord/nostrord/pull/49) con un modal de compartir que genera tanto un URI `nostr:naddr` como un enlace `nostrord.com/open/` amigable para la web.

### FIPS v0.3.0 lanza alcance multiplataforma, descubrimiento de pares Nostr y un gateway para LANs sin modificar

[FIPS](https://github.com/jmcorgan/fips) (Free Internetworking Peering System), el proyecto de red de malla nativo de Nostr, lanzó [v0.3.0](https://github.com/jmcorgan/fips/releases/tag/v0.3.0) esta semana, un hito importante que amplía el proyecto de solo Linux a Linux, macOS, Windows y OpenWrt. La adición principal es el descubrimiento de pares mediado por Nostr con traversal NAT UDP asistido por STUN.

### Flotilla 1.8.0 lanza videollamadas, renderizado de email y menciones de sala

[Flotilla](https://flotilla.social), la app de chat grupal [NIP-29](/es/topics/nip-29/) basada en relay de hodlbod, lanzó [1.8.0](https://gitea.coracle.social/coracle/flotilla/src/tag/1.8.0) esta semana con varias adiciones notables. Las salas de voz ahora soportan video: los participantes pueden encender cámaras o compartir su pantalla durante una llamada. El renderizado de email llega a través de una actualización a la biblioteca welshman: Flotilla ahora puede recibir mensajes que incrustan contenido de email HTML y lo renderiza en línea.

### Calendar by Formstr lanza v1.5.1 con programación de citas y sincronización de calendario Android

[Calendar by Formstr](https://calendar.formstr.app), una app de calendario nativa de Nostr, lanzó [v1.5.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.5.0) el 10 de mayo y [v1.5.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.5.1) el 11 de mayo. La programación de citas llega en [PR #89](https://github.com/formstr-hq/nostr-calendar/pull/89), permitiendo a los usuarios crear franjas horarias reservables en su calendario. La integración de calendario Android de solo lectura en [PR #123](https://github.com/formstr-hq/nostr-calendar/pull/123) sincroniza eventos Nostr al calendario del dispositivo.

## Nuevos proyectos

### Tamagostrich lanza un Tamagotchi NIP-78 descentralizado con recompensas en sats

[Tamagostrich](https://github.com/Negr087/tamagostrich) es un juego de mascota virtual basado en navegador lanzado en el Hackathon IDENTITY 2026 donde un avestruz bebé, Nori, evoluciona a través de tu actividad social en Nostr. El estado de la mascota vive en un evento [NIP-78](/es/topics/nip-78/) kind:30078 para que se sincronice en cada dispositivo que comparte el mismo par de claves. Las recompensas de hito pagan automáticamente en sats via [NIP-47 (Nostr Wallet Connect)](/es/topics/nip-47/): 50 sats en el nivel 5, 210 sats en el nivel 10 y 420 sats en el nivel máximo 21.

## Trabajo de protocolo y especificaciones

El repositorio de NIPs fusionó [PR #2338](https://github.com/nostr-protocol/nips/pull/2338) corrigiendo los enlaces de referencia del README para los kinds de eventos Marmot y el kind de geocaching 37516. Se abrieron cinco nuevas propuestas esta semana:

[PR #2331](https://github.com/nostr-protocol/nips/pull/2331) propone **NIP-9A: Reglas de Comunidad Verificables**, introduciendo kind:34551, un evento reemplazable parametrizado que permite al propietario de una comunidad publicar un documento de reglas legible por máquina y firmado criptográficamente.

[PR #2335](https://github.com/nostr-protocol/nips/pull/2335) propone **Eventos de Reserva para Mercados Nostr**, definiendo kind:32122 (eventos de reserva reemplazables parametrizados), kind:1326 (registros de auditoría de transición de solo adición) y kind:32124 (reseñas post-intercambio).

[PR #2334](https://github.com/nostr-protocol/nips/pull/2334) propone **Servicios de Custodia para Mercados Nostr**, usando kind:30303 para que los operadores de custodia declaren su dirección de contrato EVM y programa de tarifas.

[PR #2333](https://github.com/nostr-protocol/nips/pull/2333) propone **Perfiles de Listado de Alojamiento para Listados del Mercado NIP-99**, extendiendo los listados clasificados NIP-99 con tags de índice geoespacial H3 `g`.

[PR #2332](https://github.com/nostr-protocol/nips/pull/2332) propone **NIP-BC: Zaps Onchain (kind 8333)**, explotando una identidad directa entre las claves Nostr y las direcciones Bitcoin Taproot.

## Inmersión profunda en NIP: NIP-78 (datos específicos de la app)

[NIP-78](/es/topics/nip-78/) define una forma estándar para que las aplicaciones almacenen datos privados o públicos arbitrarios en nombre de un usuario usando eventos Nostr. El kind de evento central es 30078, un evento reemplazable parametrizado donde el tag `d` es una cadena de identificador definida por la aplicación.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1747180800,
  "kind": 30078,
  "tags": [
    ["d", "tamagostrich-pet-state"]
  ],
  "content": "{\"level\":7,\"xp\":1420,\"happiness\":82,\"energy\":61}",
  "sig": "<128-char hex>"
}
```

La motivación principal es la sincronización entre dispositivos sin un servidor centralizado. Para datos de aplicación privados, los eventos NIP-78 pueden cifrar el campo de contenido usando [NIP-44 (Cifrado con Versión)](/es/topics/nip-44/) o el más antiguo [NIP-04](/es/topics/nip-04/) antes de publicar.

---

**Fuentes primarias:**
- [Especificación NIP-78](https://github.com/nostr-protocol/nips/blob/master/78.md)
- [Tamagostrich](https://github.com/Negr087/tamagostrich): implementación en producción esta semana

**Ver también:**
- [NIP-51: Listas](/es/topics/nip-51/)
- [NIP-65: Metadatos de Lista de Relays](/es/topics/nip-65/)

## Inmersión profunda en NIP: NIP-98 (HTTP Auth)

[NIP-98](/es/topics/nip-98/) define un esquema de autenticación HTTP que permite que los pares de claves Nostr autoricen solicitudes a servidores HTTP, eliminando la necesidad de nombres de usuario, contraseñas o tokens OAuth para el acceso a API del lado del servidor. Un cliente construye un evento Nostr de corta duración de kind 27235, lo firma con su clave privada, codifica el JSON en base64 y lo envía en un encabezado HTTP `Authorization: Nostr <base64>`.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1747180800,
  "kind": 27235,
  "tags": [
    ["u", "https://files.example.com/upload"],
    ["method", "POST"],
    ["payload", "<sha256-hash-of-request-body>"]
  ],
  "content": "",
  "sig": "<128-char hex>"
}
```

El evento kind 27235 incluye el método HTTP en un tag `method`, la URL completa de la solicitud en un tag `u` y una marca de tiempo `created_at`. El servidor valida la firma, verifica que el método y la URL coincidan con la solicitud real y confirma que la marca de tiempo es reciente para prevenir ataques de repetición.

NIP-98 se usa en Blossom ([BUD-01](https://github.com/hzrd149/blossom/blob/master/buds/01.md)) para autenticar cargas y descargas de blobs. Routstr lo usa para control de acceso a la API HTTP por solicitud. Sprout lo usa para autenticación de transporte git y acceso a relay REST.

---

**Fuentes primarias:**
- [Especificación NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md)
- [BUD-01: Auth de carga Blossom](https://github.com/hzrd149/blossom/blob/master/buds/01.md)

**Ver también:**
- [NIP-96: Integración de Almacenamiento de Archivos HTTP](/es/topics/nip-96/)

---

Eso es todo por esta semana. Si estás construyendo algo o tienes noticias que compartir, envíanos un DM en Nostr o encuéntranos en [nostrcompass.org](https://nostrcompass.org).
