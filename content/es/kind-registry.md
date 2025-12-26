---
title: Registro de Kinds
date: 2025-12-17
draft: false
translationOf: /en/kind-registry.md
translationDate: 2025-12-26
---

Los kinds de eventos son enteros que categorizan eventos Nostr. Este registro lista todos los kinds estandarizados con sus descripciones y NIPs que los definen.

**Rangos de kind** (de [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)):
- **0-999**: Eventos regulares (todas las versiones se mantienen)
- **1000-9999**: Eventos regulares (continuación)
- **10000-19999**: Eventos reemplazables (solo se mantiene el más reciente por pubkey)
- **20000-29999**: Eventos efímeros (no almacenados, solo reenviados)
- **30000-39999**: Eventos direccionables (más reciente por pubkey + kind + d-tag)

## Eventos Principales (0-99)

| Kind | Descripción | NIP |
|------|-------------|-----|
| 0 | Metadatos de Usuario | [01](https://github.com/nostr-protocol/nips/blob/master/01.md) |
| 1 | Nota de Texto Corta | [10](https://github.com/nostr-protocol/nips/blob/master/10.md) |
| 2 | Recomendar Relay (obsoleto) | [01](https://github.com/nostr-protocol/nips/blob/master/01.md) |
| 3 | Seguidos | [02](https://github.com/nostr-protocol/nips/blob/master/02.md) |
| 4 | Mensajes Directos Encriptados | [04](https://github.com/nostr-protocol/nips/blob/master/04.md) |
| 5 | Solicitud de Eliminación de Evento | [09](https://github.com/nostr-protocol/nips/blob/master/09.md) |
| 6 | Repost | [18](https://github.com/nostr-protocol/nips/blob/master/18.md) |
| 7 | Reacción | [25](https://github.com/nostr-protocol/nips/blob/master/25.md) |
| 8 | Otorgamiento de Insignia | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 9 | Mensaje de Chat | [C7](https://github.com/nostr-protocol/nips/blob/master/C7.md) |
| 10 | Respuesta en Hilo de Chat Grupal (obsoleto) | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 11 | Hilo | [7D](https://github.com/nostr-protocol/nips/blob/master/7D.md) |
| 12 | Respuesta de Hilo Grupal (obsoleto) | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 13 | Seal | [59](https://github.com/nostr-protocol/nips/blob/master/59.md) |
| 14 | Mensaje Directo | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 15 | Mensaje de Archivo | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 16 | Repost Genérico | [18](https://github.com/nostr-protocol/nips/blob/master/18.md) |
| 17 | Reacción a un sitio web | [25](https://github.com/nostr-protocol/nips/blob/master/25.md) |
| 20 | Imagen | [68](https://github.com/nostr-protocol/nips/blob/master/68.md) |
| 21 | Evento de Video | [71](https://github.com/nostr-protocol/nips/blob/master/71.md) |
| 22 | Video Vertical Corto | [71](https://github.com/nostr-protocol/nips/blob/master/71.md) |
| 40 | Creación de Canal | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 41 | Metadatos de Canal | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 42 | Mensaje de Canal | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 43 | Ocultar Mensaje de Canal | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 44 | Silenciar Usuario de Canal | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 62 | Solicitud de Desaparición | [62](https://github.com/nostr-protocol/nips/blob/master/62.md) |
| 64 | Ajedrez (PGN) | [64](https://github.com/nostr-protocol/nips/blob/master/64.md) |

## Encriptación MLS (443-445)

| Kind | Descripción | NIP |
|------|-------------|-----|
| 443 | KeyPackage | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 444 | Mensaje de Bienvenida | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 445 | Evento de Grupo | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |

## Eventos Regulares (1000-9999)

| Kind | Descripción | NIP |
|------|-------------|-----|
| 1018 | Respuesta a Encuesta | [88](https://github.com/nostr-protocol/nips/blob/master/88.md) |
| 1021 | Oferta | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 1022 | Confirmación de Oferta | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 1040 | OpenTimestamps | [03](https://github.com/nostr-protocol/nips/blob/master/03.md) |
| 1059 | Gift Wrap | [59](https://github.com/nostr-protocol/nips/blob/master/59.md) |
| 1063 | Metadatos de Archivo | [94](https://github.com/nostr-protocol/nips/blob/master/94.md) |
| 1068 | Encuesta | [88](https://github.com/nostr-protocol/nips/blob/master/88.md) |
| 1111 | Comentario | [22](https://github.com/nostr-protocol/nips/blob/master/22.md) |
| 1222 | Mensaje de Voz | [A0](https://github.com/nostr-protocol/nips/blob/master/A0.md) |
| 1244 | Comentario de Mensaje de Voz | [A0](https://github.com/nostr-protocol/nips/blob/master/A0.md) |
| 1311 | Mensaje de Chat en Vivo | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 1337 | Fragmento de Código | [C0](https://github.com/nostr-protocol/nips/blob/master/C0.md) |
| 1617 | Parches | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1618 | Pull Requests | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1619 | Actualizaciones de Pull Request | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1621 | Issues | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1984 | Reporte | [56](https://github.com/nostr-protocol/nips/blob/master/56.md) |
| 1985 | Etiqueta | [32](https://github.com/nostr-protocol/nips/blob/master/32.md) |
| 2003 | Torrent | [35](https://github.com/nostr-protocol/nips/blob/master/35.md) |
| 2004 | Comentario de Torrent | [35](https://github.com/nostr-protocol/nips/blob/master/35.md) |
| 4550 | Aprobación de Publicación Comunitaria | [72](https://github.com/nostr-protocol/nips/blob/master/72.md) |
| 5000-5999 | Solicitud de Trabajo | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 6000-6999 | Resultado de Trabajo | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 7000 | Retroalimentación de Trabajo | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 7374 | Tokens Reservados de Cartera Cashu | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 7375 | Tokens de Cartera Cashu | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 7376 | Historial de Cartera Cashu | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 8000 | Agregar Usuario | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 8001 | Eliminar Usuario | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 9000-9030 | Eventos de Control de Grupo | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 9041 | Meta de Zap | [75](https://github.com/nostr-protocol/nips/blob/master/75.md) |
| 9321 | Nutzap | [61](https://github.com/nostr-protocol/nips/blob/master/61.md) |
| 9734 | Solicitud de Zap | [57](https://github.com/nostr-protocol/nips/blob/master/57.md) |
| 9735 | Zap | [57](https://github.com/nostr-protocol/nips/blob/master/57.md) |
| 9802 | Destacados | [84](https://github.com/nostr-protocol/nips/blob/master/84.md) |

## Eventos Reemplazables (10000-19999)

| Kind | Descripción | NIP |
|------|-------------|-----|
| 10000 | Lista de silenciados | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10001 | Lista de fijados | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10002 | Metadatos de Lista de Relays | [65](https://github.com/nostr-protocol/nips/blob/master/65.md) |
| 10003 | Lista de marcadores | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10004 | Lista de comunidades | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10005 | Lista de chats públicos | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10006 | Lista de relays bloqueados | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10007 | Lista de relays de búsqueda | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10009 | Grupos de usuario | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10012 | Lista de relays favoritos | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10013 | Lista de relays de eventos privados | [37](https://github.com/nostr-protocol/nips/blob/master/37.md) |
| 10015 | Lista de intereses | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10019 | Recomendación de Mint Nutzap | [61](https://github.com/nostr-protocol/nips/blob/master/61.md) |
| 10020 | Seguidos de medios | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10030 | Lista de emojis de usuario | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10050 | Lista de relays para recibir DMs | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 10051 | Lista de Relays KeyPackage | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 10063 | Lista de servidores de usuario | Blossom |
| 10166 | Anuncio de Monitor de Relay | [66](https://github.com/nostr-protocol/nips/blob/master/66.md) |
| 10312 | Presencia en Sala | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 13194 | Info de Cartera | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 13534 | Listas de Membresía | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 17375 | Evento de Cartera Cashu | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |

## Autenticación y Cartera (22000-27999)

| Kind | Descripción | NIP |
|------|-------------|-----|
| 22242 | Autenticación de Cliente | [42](https://github.com/nostr-protocol/nips/blob/master/42.md) |
| 23194 | Solicitud de Cartera | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 23195 | Respuesta de Cartera | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 24133 | Nostr Connect | [46](https://github.com/nostr-protocol/nips/blob/master/46.md) |
| 24242 | Blobs almacenados en mediaservers | Blossom |
| 27235 | HTTP Auth | [98](https://github.com/nostr-protocol/nips/blob/master/98.md) |

## Control de Acceso (28000-29999)

| Kind | Descripción | NIP |
|------|-------------|-----|
| 28934 | Solicitud de Unión | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 28935 | Solicitud de Invitación | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 28936 | Solicitud de Salida | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |

## Eventos Direccionables (30000-39999)

| Kind | Descripción | NIP |
|------|-------------|-----|
| 30000 | Conjuntos de seguidos | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30002 | Conjuntos de relays | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30003 | Conjuntos de marcadores | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30004 | Conjuntos de curación | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30005 | Conjuntos de video | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30007 | Conjuntos de silenciado por kind | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30008 | Insignias de Perfil | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 30009 | Definición de Insignia | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 30015 | Conjuntos de intereses | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30017 | Crear o actualizar un puesto | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30018 | Crear o actualizar un producto | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30019 | UI/UX de Marketplace | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30020 | Producto vendido como subasta | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30023 | Contenido de Formato Largo | [23](https://github.com/nostr-protocol/nips/blob/master/23.md) |
| 30024 | Borrador de Contenido de Formato Largo | [23](https://github.com/nostr-protocol/nips/blob/master/23.md) |
| 30030 | Conjuntos de emoji | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30063 | Conjuntos de artefactos de release | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30078 | Datos Específicos de Aplicación | [78](https://github.com/nostr-protocol/nips/blob/master/78.md) |
| 30166 | Descubrimiento de Relay | [66](https://github.com/nostr-protocol/nips/blob/master/66.md) |
| 30267 | Conjuntos de curación de apps | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30311 | Evento en Vivo | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30312 | Sala Interactiva | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30313 | Evento de Conferencia | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30315 | Estados de Usuario | [38](https://github.com/nostr-protocol/nips/blob/master/38.md) |
| 30402 | Listado Clasificado | [99](https://github.com/nostr-protocol/nips/blob/master/99.md) |
| 30403 | Borrador de Listado Clasificado | [99](https://github.com/nostr-protocol/nips/blob/master/99.md) |
| 30617 | Anuncios de repositorio | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 30618 | Anuncios de estado de repositorio | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 30818 | Artículo Wiki | [54](https://github.com/nostr-protocol/nips/blob/master/54.md) |
| 30819 | Redirecciones | [54](https://github.com/nostr-protocol/nips/blob/master/54.md) |
| 31234 | Evento Borrador | [37](https://github.com/nostr-protocol/nips/blob/master/37.md) |
| 31922 | Evento de Calendario Basado en Fecha | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31923 | Evento de Calendario Basado en Hora | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31924 | Calendario | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31925 | RSVP de Evento de Calendario | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31989 | Recomendación de handler | [89](https://github.com/nostr-protocol/nips/blob/master/89.md) |
| 31990 | Información de handler | [89](https://github.com/nostr-protocol/nips/blob/master/89.md) |
| 34550 | Definición de Comunidad | [72](https://github.com/nostr-protocol/nips/blob/master/72.md) |
| 38172 | Anuncio de Mint Cashu | [87](https://github.com/nostr-protocol/nips/blob/master/87.md) |
| 38173 | Anuncio Fedimint | [87](https://github.com/nostr-protocol/nips/blob/master/87.md) |
| 38383 | Eventos de orden peer-to-peer | [69](https://github.com/nostr-protocol/nips/blob/master/69.md) |
| 39000-39009 | Eventos de metadatos de grupo | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 39089 | Starter packs | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 39092 | Starter packs de medios | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 39701 | Marcadores web | [B0](https://github.com/nostr-protocol/nips/blob/master/B0.md) |

*Última actualización: Diciembre 2025*

Consulta el [repositorio de NIPs](https://github.com/nostr-protocol/nips) para la fuente autorizada.
