---
title: "NIP-B0: Marcadores web"
date: 2026-05-28
draft: false
translationOf: /en/topics/nip-b0.md
translationDate: 2026-07-01
categories:
  - Protocol
  - Social
---

NIP-B0 define un evento parametrizado reemplazable (kind 39701) que publica marcadores web como eventos de Nostr de primera clase. La propuesta permite a los usuarios construir colecciones de marcadores curadas que pueden descubrirse, recibir zaps y republicarse entre clientes sin depender de un servicio de marcadores centralizado.

## Cómo funciona

Un marcador es un evento kind 39701 cuyo tag `d` es la URL canónica de la página marcada. La semántica reemplazable permite al autor actualizar su propio marcador para esa URL (reetiquetado, actualización del título, marcado como obsoleto) sin producir eventos duplicados. El campo content transporta la nota del autor sobre el marcador; los tags transportan título, descripción, imagen y tags de tópico `t` para descubrimiento.

```json
{
  "kind": 39701,
  "tags": [
    ["d", "https://example.com/an-article-worth-saving"],
    ["title", "Article Title"],
    ["t", "nostr"],
    ["t", "protocol"],
    ["published_at", "1717000000"]
  ],
  "content": "Useful primer on the topic.",
  "pubkey": "...",
  "sig": "..."
}
```

El tag `d` identifica el marcador de forma única por autor, por lo que dos usuarios pueden marcar la misma URL con sus propias anotaciones y conjuntos de tags.

## Descubrimiento y curación

Debido a que cada marcador es un evento de primera clase, cualquier cliente de Nostr puede mostrar un feed de marcadores suscribiéndose a eventos kind 39701 filtrados por tags o autores. Los flujos de trabajo dirigidos por curadores se vuelven naturales: un curador publica una lista de marcadores, los lectores siguen la pubkey del curador, y los marcadores fluyen a través de cualquier relay que los transporte. No hay directorio centralizado.

## Implementaciones

- [deepmarks-public](https://github.com/ostermayer/deepmarks-public) — Cliente web de referencia con una arquitectura de tres cajas (curador, indexador, visor) y un sistema de niveles financiado por zaps NIP-57 directos al curador. Implementa NIP-B0 junto con NIP-07, NIP-46, NIP-57, NIP-44, NIP-98, NIP-65 y Blossom BUD-01/BUD-04 para almacenamiento de archivos.

## Notas de confianza y seguridad

- Los marcadores son públicos por defecto; no publiques listas de lectura privadas por esta vía
- La republicación depende de que los relays sigan transportando los eventos; los relays efímeros descartarán los marcadores
- El tag `published_at` es afirmado por el publicador, no verificable

---

**Fuentes primarias:**
- [Especificación propuesta de NIP-B0](https://github.com/nostr-protocol/nips/pull/2089) — Sigue el evento de marcador web kind 39701 propuesto
- [deepmarks-public](https://github.com/ostermayer/deepmarks-public) — Implementación de referencia con sistema de niveles de curador

**Mencionado en:**
- [Boletín #24: Marcadores NIP-B0 de deepmarks con publicación monetizada por el curador](/es/newsletters/2026-05-28-newsletter/#deepmarks-nip-b0-bookmarks-with-curator-monetized-publishing)
- [Boletín #27: También lanzado](/es/newsletters/2026-06-17-newsletter/#also-shipped)

**Véase también:**
- [NIP-57: Zaps Lightning](/es/topics/nip-57/)
- [NIP-65: Metadatos de lista de relays](/es/topics/nip-65/)
