---
title: "NIP-CD: comandos de barra"
date: 2026-10-28
translationOf: /en/topics/nip-cd.md
translationDate: 2026-10-28
draft: false
categories:
  - Protocol
---

NIP-CD define los comandos de barra. Un servicio publica un comando y cualquiera puede invocarlo como texto plano en el contenido de cualquier event de Nostr. NIP-CD es una especificación opcional en borrador. Se fusionó el 21 de octubre de 2026 con el título Commands, tras una propuesta anterior, y pasó a titularse Slash Commands cuando se fusionaron las listas opcionales de comandos instalados, el 27 de octubre de 2026.

## Cómo funciona

Un event de kind 31992 define un comando. Los tags obligatorios indican la palabra disparadora sin barra, un título y una descripción de uso. Mediante tags `arg` ordenados se declaran argumentos posicionales, con tipos como pubkey, event, relay, number, enum o text. Los tags `s` limitan qué events activan el comando según kind, relay, autor o tag. Estos ámbitos funcionan como un filtro: los valores del mismo tipo son alternativas, y cada tipo presente debe coincidir.

Una invocación es un texto que empieza en el índice 0 del contenido de un event, como `/ban` seguido de argumentos, y no lleva tags. Si se añade un calificador con la forma `@nostr:npub1...`, la invocación se dirige a un único ejecutor. Sin calificador, puede actuar cualquier comando cuyo disparador coincida y cuyo ámbito incluya el event, de modo que un mismo mensaje puede activar varios servicios.

El soporte en los clientes es opcional. Estos pueden ofrecer autocompletado, selectores de argumentos y chips renderizados. No deben exigir su propio soporte antes de enviar una invocación, y deben enviar como contenido ordinario el texto que no se pueda analizar.

En los grupos basados en relays, las definiciones y las invocaciones van al relay del grupo. Para uso por difusión, las definiciones van a los outboxes de los ejecutores y las invocaciones, a sus inboxes.

## Listas de comandos instalados

Un usuario puede mantener una lista opcional de kind 10992, conforme a NIP-51, con tags `a` que apuntan a definiciones de comandos de kind 31992 mediante la pubkey del ejecutor y el valor `d`, con una pista de relay opcional. Los clientes deberían usar la lista para el autocompletado y los chips renderizados. La lista recoge una preferencia de visualización y descubrimiento del usuario. No autoriza a ningún ejecutor, y la invocación en texto plano funciona sin ella. Esta parte de la especificación se fusionó el 27 de octubre de 2026 mediante la PR #2525. La fusión no indica qué clientes han implementado la lista.

## Fuentes primarias

- [Especificación NIP-CD](https://github.com/nostr-protocol/nips/blob/master/CD.md)
- [Fusión de NIP-CD del 21 de octubre de 2026](https://github.com/nostr-protocol/nips/commit/7b5ea85479c0b4efce3c246abefa1dae8f8f91e4)
- [PR #2525 de listas de comandos instalados, fusionada el 27 de octubre de 2026](https://github.com/nostr-protocol/nips/pull/2525)
- [Commit del 26 de octubre de 2026 de la PR #2525, hecho en su rama antes de la fusión](https://github.com/nostr-protocol/nips/commit/0142de0384210d69074c089448ef5bc303faef37)
- [Fusión de las listas de comandos instalados en NIP-CD del 27 de octubre de 2026](https://github.com/nostr-protocol/nips/commit/400d157c53264b8e58c7b3cdbd21ef546fb7a157)

## Mencionado en
- [Boletín n.º 46: NIP-CD define comandos invocados como texto plano](/es/newsletters/2026-10-28-newsletter/#nip-cd-defines-commands-invoked-as-plain-text) Boletines

- [Boletín n.º 46: NIP-CD añade listas opcionales de comandos instalados](/es/newsletters/2026-10-28-newsletter/#nip-cd-adds-optional-installed-command-lists) Boletines

- [Boletín n.º 46 (2026-10-28): octubre de 2026, significados de consulta compartidos y servicios activados por texto](/es/newsletters/2026-10-28-newsletter/#october-2026-shared-query-meanings-and-text-triggered-services)

## Véase también

- [NIP-01: protocolo básico](/es/topics/nip-01/)
