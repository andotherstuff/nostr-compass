---
title: "NIP-34: Colaboración Git"
date: 2026-02-04
description: "NIP-34 habilita hospedaje descentralizado de repositorios git y colaboración a través de eventos de Nostr."
translationOf: /en/topics/nip-34.md
translationDate: 2026-03-07
draft: false
categories:
  - NIP
  - Development
---

NIP-34 define tipos de evento para hospedar repositorios git, parches e issues en relays de Nostr. Esto permite colaboración de código completamente descentralizada sin dependencia de plataformas de hospedaje centralizadas como GitHub o GitLab.

## Cómo Funciona

Los repositorios se representan como eventos direccionables (kind 30617) que contienen metadatos como nombre, descripción y URLs de clonación. El propietario del repositorio publica este evento para establecer el proyecto en Nostr.

Los parches (kind 1617) contienen contenido `git format-patch` que puede aplicarse a un repositorio. Los contribuidores envían parches como eventos que referencian el repositorio objetivo. Esto refleja el flujo de trabajo de parches por correo electrónico usado por proyectos como el kernel de Linux.

Los issues (kind 1621) funcionan como rastreadores de issues tradicionales. Los pull requests usan los kinds 1618 y 1619, y las actualizaciones de estado usan del 1630 al 1633. Las respuestas a issues, parches y pull requests usan comentarios [NIP-22](/es/topics/nip-22/).

## Tipos de Evento

- **30617** - Anuncio de repositorio (direccionable)
- **30618** - Anuncio de estado de repositorio para ramas y tags
- **1617** - Envío de parche
- **1618** - Pull request
- **1619** - Actualización de pull request
- **1621** - Issue
- **1630-1633** - Eventos de estado: abierto, fusionado/resuelto, cerrado y borrador

## Por Qué Importa

NIP-34 separa el descubrimiento del transporte. El repositorio real puede seguir viviendo en servidores Git ordinarios, pero los eventos de Nostr proporcionan una capa distribuida por relays para descubrimiento, discusión, intercambio de parches y seguimiento de estado. Eso significa que un proyecto puede seguir usando herramientas nativas de git sin depender de la base de datos o API de un solo forge.

El tag `r` con el commit único más antiguo es uno de los detalles más importantes. Da a los clientes una forma de agrupar mirrors y forks que representan el mismo linaje de repositorio subyacente, algo difícil de inferir solo por nombres.

## Estado de Implementación

- **ngit** - Herramienta de línea de comandos para publicar repos y parches a Nostr
- **gitworkshop.dev** - Interfaz web para navegar repositorios hospedados en Nostr
- **Notedeck** - Cliente de escritorio con [soporte borrador para visualización NIP-34](https://github.com/damus-io/notedeck/pull/1279)

---

**Fuentes primarias:**

- [Especificación NIP-34](https://github.com/nostr-protocol/nips/blob/master/34.md)

**Mencionado en:**

- [Newsletter #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - Notedeck añadiendo visor NIP-34
- [Newsletter #9: Notedeck](/en/newsletters/2026-02-11-newsletter/#notedeck)

**Ver también:**
- [NIP-22: Comentarios](/es/topics/nip-22/)
