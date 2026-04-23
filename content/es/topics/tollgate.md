---
title: "TollGate: Internet de pago por uso sobre Nostr y Cashu"
date: 2026-04-22
translationOf: /en/topics/tollgate.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocols
---

TollGate es un protocolo para vender acceso de red a cambio de pagos pequeños y frecuentes con activos bearer. Un dispositivo que puede controlar la conectividad, como un router WiFi, un switch Ethernet o un Bluetooth tether, actúa como un TollGate que anuncia precios, acepta tokens ecash de [Cashu](/es/topics/cashu/) y gestiona sesiones. Los clientes pagan exactamente por los minutos o megabytes que consumen. No hay cuentas, no hay suscripciones, no hay KYC.

## Cómo funciona

TollGate separa responsabilidades en tres capas. La capa de protocolo define las formas de evento y la semántica de pago. La capa de interfaz define cómo intercambian esos eventos el cliente y la puerta. La capa de medio describe el enlace físico que transporta el tráfico pagado. Un TollGate funcional combina una especificación de cada capa, y algunas interfaces corren sobre relays Nostr mientras que otras corren sobre HTTP plano.

En la capa de protocolo, [TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md) define tres eventos base: un kind Advertisement que lista precios y mints aceptados, un kind Session que rastrea cuánto ha pagado el cliente y cuánto ha consumido, y un kind Notice para mensajería fuera de banda. [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) añade pagos Cashu encima, para que un cliente pueda canjear tokens ecash de cualquier mint que el TollGate anuncie y recibir crédito de sesión a cambio.

En la capa de interfaz, [HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md) hasta HTTP-03 definen la superficie HTTP para dispositivos en sistemas operativos restrictivos que no pueden abrir fácilmente conexiones WebSocket a relays arbitrarios, y [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md) define el transporte por relay Nostr para clientes que sí pueden. En la capa de medio, [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md) describe cómo una configuración de captive portal WiFi identifica y enruta a los clientes que pagan.

Como el activo de pago es un bearer token y no una credencial, el cliente no necesita acceso previo a internet para producirlo. Un token Cashu guardado en una cartera local basta por sí solo para comprar el primer minuto de conectividad, punto a partir del cual el cliente puede recargar con más tokens según lo necesite. Los TollGates también pueden comprar uplink entre sí, de modo que el alcance va más allá de un único operador.

## Por qué importa

El WiFi de pago convencional depende de cuentas, captive portals y tarjetas de pago, cada uno de los cuales crea fricción y una estela de datos. El modelo de TollGate convierte la conectividad en una mercancía que cualquier router puede vender a cualquier cliente pagador sin saber quién es. La abstracción permite que operadores independientes fijen sus propios precios, acepten sus mints preferidos y compitan en cobertura y calidad en lugar de en lock-in.

El [release v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0) es la primera instantánea etiquetada de estas especificaciones. No estandariza cada detalle, pero fija suficiente superficie para que firmware de routers, carteras cliente y revendedores multi-hop puedan empezar a construir contra una referencia estable.

---

**Fuentes primarias:**
- [TollGate v0.1.0 release](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)
- [TIP-01: Eventos base](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md)
- [TIP-02: Pagos Cashu](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md)
- [HTTP-01 hasta HTTP-03](https://github.com/OpenTollGate/tollgate/tree/v0.1.0)
- [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md)
- [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md)
- [Repositorio TollGate](https://github.com/OpenTollGate/tollgate)

**Mencionado en:**
- [Boletín #19: TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/)

**Ver también:**
- [Cashu](/es/topics/cashu/)
- [NIP-60: Cashu Wallet](/es/topics/nip-60/)
