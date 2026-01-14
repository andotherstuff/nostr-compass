---
title: "NIP-65: Metadatos de Lista de Relays"
date: 2026-01-13
draft: false
categories:
  - Protocol
  - Discovery
---

NIP-65 define eventos kind 10002 que anuncian qué relays prefiere un usuario para lectura y escritura. Estos metadatos ayudan a otros usuarios y clientes a localizar tu contenido a través de la red distribuida de relays, habilitando el "modelo outbox" que distribuye la carga y mejora la resistencia a la censura.

## Estructura

Una lista de relays es un evento reemplazable (kind 10002) que contiene etiquetas `r` para cada relay que el usuario quiere anunciar. El evento reemplaza cualquier lista de relays anterior de la misma pubkey.

```json
{
  "id": "a1b2c3d4e5f6...",
  "pubkey": "abcd1234...",
  "created_at": 1736726400,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "sig1234..."
}
```

Cada etiqueta `r` contiene una URL WebSocket de relay y un marcador opcional que indica cómo el usuario interactúa con ese relay. El marcador `read` significa que el usuario consume eventos de este relay, por lo que otros deben publicar allí para llegar al usuario. El marcador `write` significa que el usuario publica en este relay, por lo que otros deben suscribirse allí para ver el contenido del usuario. Omitir el marcador indica tanto lectura como escritura.

El campo `content` está vacío para eventos de lista de relays.

## El Modelo Outbox

NIP-65 habilita un patrón de distribución de contenido descentralizado llamado el "modelo outbox". En lugar de que todos publiquen y lean de los mismos relays centrales, los usuarios publican en sus propios relays preferidos y los clientes descubren dinámicamente dónde encontrar el contenido de cada usuario.

Cuando Alice quiere encontrar las publicaciones de Bob, su cliente primero obtiene el evento kind 10002 de Bob desde cualquier relay que lo tenga. Luego extrae los relays que Bob marcó para `write` ya que esos son donde él publica. Su cliente se suscribe a esos relays para los eventos de Bob. Cuando Alice quiere enviar a Bob un mensaje directo, su cliente busca sus relays `read` en su lugar y publica el mensaje allí.

Los clientes que siguen el modelo outbox mantienen conexiones con los relays listados en los eventos NIP-65 de sus usuarios seguidos. A medida que descubren nuevas cuentas, se conectan dinámicamente a nuevos relays. Los relays que aparecen en las listas de múltiples usuarios seguidos obtienen prioridad ya que conectarse a ellos sirve a más del grafo social del usuario.

Esta arquitectura mejora la resistencia a la censura porque ningún relay único necesita almacenar o servir el contenido de todos. Si un relay se cae o bloquea a un usuario, su contenido permanece disponible en sus otros relays listados.

## Relación con las Pistas de Relay

NIP-65 complementa las pistas de relay encontradas a lo largo de otros NIPs. Cuando etiquetas a alguien con `["p", "pubkey", "wss://hint.relay"]`, la pista le dice a los clientes dónde buscar esa referencia específica. NIP-65 proporciona la lista autoritativa de relays preferidos controlada por el usuario, mientras que las pistas ofrecen atajos incrustados en eventos individuales para un descubrimiento más rápido.

## Mejores Prácticas

Mantén tu lista de relays actualizada ya que las entradas obsoletas que apuntan a relays desaparecidos te hacen más difícil de encontrar. Incluye al menos dos o tres relays para redundancia de modo que si un relay se cae, tu contenido permanezca accesible a través de los otros.

Evita listar demasiados relays. Cuando listas diez o quince relays, cada cliente que quiere obtener tu contenido debe conectarse a todos ellos, ralentizando su experiencia y aumentando la carga a través de la red. Una lista enfocada de tres a cinco relays bien elegidos te sirve mejor que una lista exhaustiva que sobrecarga a todos los que te siguen.

Mezcla relays de propósito general con cualquier relay especializado que uses. Por ejemplo, podrías listar un relay general popular como `wss://relay.damus.io`, un relay enfocado en tu región geográfica, y un relay para una comunidad específica en la que participas.

---

**Fuentes primarias:**
- [Especificación NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md)

**Mencionado en:**
- [Newsletter #5: Análisis Profundo de NIPs](/es/newsletters/2026-01-13-newsletter/#nip-65-metadatos-de-lista-de-relays)

**Ver también:**
- [NIP-11: Información de Relay](/es/topics/nip-11/)
