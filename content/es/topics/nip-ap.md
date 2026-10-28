---
title: "NIP-AP de Buzz: personas de agentes"
date: 2026-10-21
translationOf: /en/topics/nip-ap.md
translationDate: 2026-10-28
draft: false
categories: ["NIPs"]
---

NIP-AP de Buzz es una especificación en borrador del proyecto Buzz, ajena a los NIPs aceptados en nostr-protocol/nips.

Define events de persona de kind 30175, que son definiciones direccionables para instanciar un agente de IA, identificadas por un slug `d` en texto plano. El kind 30178 contiene una proyección del catálogo de equipos. Los relays que lo implementan restringen el acceso a ambos kinds: los autores leen sus propios events, y los demás lectores solo ven un event en consultas, entrega en directo, búsquedas, recuentos o localizaciones por id si lleva `["shared", "true"]`. Compartir un equipo expone la proyección incrustada y las instrucciones de cada miembro, incluidos los miembros con personas no compartidas. La restricción controla el acceso sin cifrar el contenido; el operador del relay todavía puede leerlo.

Fuente primaria: la [especificación NIP-AP](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md) en el repositorio de Buzz.

## Fuentes primarias

- [NIP-AP de Buzz: personas de agentes](https://github.com/block/buzz/blob/main/docs/nips/NIP-AP.md)

## Mencionado en

- [Boletín n.º 46 (2026-10-28): buzz](/es/newsletters/2026-10-28-newsletter/#buzz)

- [Boletín 45](/en/newsletters/2026-10-21-newsletter/#buzz)
