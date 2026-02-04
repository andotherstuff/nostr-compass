---
title: "NIP-34 (Colaboración Git)"
date: 2026-02-04
description: "NIP-34 habilita hospedaje descentralizado de repositorios git y colaboración a través de eventos de Nostr."
---

NIP-34 define tipos de evento (kinds) para hospedar repositorios git, parches e issues en relays de Nostr. Esto permite colaboración de código completamente descentralizada sin dependencia de plataformas de hospedaje centralizadas como GitHub o GitLab.

## Cómo Funciona

Los repositorios se representan como eventos direccionables (kind 30617) que contienen metadatos como nombre, descripción y URLs de clonación. El propietario del repositorio publica este evento para establecer el proyecto en Nostr.

Los parches (kind 1617) contienen contenido de parche git que puede aplicarse a un repositorio. Los contribuidores envían parches como eventos referenciando el repositorio objetivo. Esto refleja el flujo de trabajo de parches basado en correo electrónico usado por proyectos como el kernel de Linux.

Los issues (kind 1621) funcionan como rastreadores de issues tradicionales. Referencian un repositorio y contienen un título y descripción. Los comentarios en issues y parches usan eventos de respuesta estándar.

## Tipos de Evento

- **30617** - Anuncio de repositorio (direccionable)
- **1617** - Envío de parche
- **1621** - Issue
- **1622** - Estado de issue (abierto/cerrado)

## Implementaciones

- **ngit** - Herramienta de línea de comandos para publicar repos y parches a Nostr
- **gitworkshop.dev** - Interfaz web para navegar repositorios hospedados en Nostr
- **Notedeck** - Cliente de escritorio con [soporte borrador para visualización NIP-34](https://github.com/damus-io/notedeck/pull/1279)

## Fuentes Primarias

- [Especificación NIP-34](https://github.com/nostr-protocol/nips/blob/master/34.md)

## Mencionado En

- [Boletín #8 (2026-02-04)](/es/newsletters/2026-02-04-newsletter/) - Notedeck añadiendo visor NIP-34
