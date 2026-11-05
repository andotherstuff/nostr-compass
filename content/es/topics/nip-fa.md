---
title: "Buzz NIP-FA: Adaptador de identidad federada"
date: 2026-10-21
draft: false
categories: ["NIPs"]
translationOf: /en/topics/nip-fa.md
translationDate: 2026-11-05
---

Buzz NIP-FA es una especificación en borrador y opcional del proyecto Buzz. Queda fuera de los NIPs aceptados del repositorio oficial nostr-protocol/nips.

Define un contrato HTTP neutral respecto al proveedor entre un cliente de Nostr y un adaptador de identidad empresarial. Tras un inicio de sesión en el navegador, el adaptador mantiene una sesión para el usuario. Emite aserciones Buzz NIP-FI, locales al proyecto, que vinculan al usuario con una clave de Nostr cuyo control el cliente demuestra con [NIP-98](/es/topics/nip-98/). El [operador elige la vigencia de cada aserción](https://github.com/block/buzz/pull/8934), que debe respetar el maximum_assertion_age del emisor aceptado por el relay, y exp no puede superar la expiración de la sesión del adaptador. La vigencia elegida limita durante cuánto tiempo una clave revocada podría todavía reconectarse tras un reinicio del relay, y los clientes no deben rechazar una aserción únicamente por su vigencia. NIP-FI y los NIPs oficiales no cambian. El inicio de sesión usa un desafío de traspaso S256 y un callback de loopback en `127.0.0.1` o `[::1]` que recibe un código de un solo uso. Los sistemas upstream como OIDC o SAML quedan detrás del adaptador. Determinar qué relays exigen identidad empresarial se deja a otras especificaciones.

Fuente primaria: la [especificación NIP-FA](https://github.com/block/buzz/blob/main/docs/nips/NIP-FA.md) en el repositorio de Buzz.

## Credenciales de agentes {#agent-credentials}

Buzz fusionó un [borrador de NIP-FA para credenciales de agentes autorizados por su propietario](https://github.com/block/buzz/pull/9015), que define rutas de concesión, aserción y revocación para agentes que un propietario ha autorizado mediante NIP-OA. Una concesión surge de un intercambio de tokens RFC 8693 que empareja la sesión del propietario con una prueba [NIP-98](/es/topics/nip-98/) del agente. Para obtener una aserción, el agente presenta la concesión como token Bearer junto con su propia prueba, y los clientes comprueban el `iss` de la aserción frente al emisor de la concesión. Las pruebas del agente son de un solo uso y pertenecen únicamente a las rutas de concesión y aserción. La revocación se ejecuta sobre la sesión del propietario sin prueba del agente; revoca la clave del agente y sus concesiones y desconecta al agente. La política del adaptador decide la vigencia de la concesión. Las condiciones de autorización no admitidas se rechazan, y una clave revocada no puede volver a inscribirse. NIP-FA es una especificación de Buzz, no un NIP aceptado. La fusión existe solo en el código fuente, sin ninguna afirmación de activación en producción, de una compilación publicada ni de interoperabilidad.

## Fuentes primarias {#primary-sources}

- [Buzz NIP-FA: Federated Identity Adapter](https://github.com/block/buzz/blob/main/docs/nips/NIP-FA.md)

- [Rutas de credenciales para agentes autorizados por su propietario](https://github.com/block/buzz/pull/9015)

## Mencionado en {#mentioned-in}

- [Boletín #47: credenciales de agentes de Buzz](/es/newsletters/2026-11-04-newsletter/#buzz-defines-owner-authorized-agent-credential-routes)


- [Boletín 45](/en/newsletters/2026-10-21-newsletter/#buzz)
