---
title: "ProofMode"
date: 2026-07-15
draft: false
translationOf: /en/topics/proofmode.md
translationDate: 2026-07-15
categories:
  - Media
  - Provenance
---

[ProofMode](https://proofmode.org/) es un conjunto de herramientas de procedencia de medios de código abierto, construido por Guardian Project, WITNESS y Okthanks, que adjunta datos verificables de autenticidad y cadena de custodia a fotos y video en el momento de la captura. No es específico de Nostr; los clientes Nostr que llevan datos ProofMode están integrando un estándar externo existente en lugar de una nueva capa de protocolo.

## Cómo funciona

El componente Capture de ProofMode incrusta metadatos de procedencia directamente en archivos de medios durante la captura, soportando los mismos estándares interoperables utilizados por la Content Authenticity Initiative (CAI), Content Credentials (CR) y C2PA. Un componente Verify separado inspecciona archivos de audio, imagen y video para verificar esos metadatos en busca de señales de generación por IA o edición posterior, y un componente Preserve maneja almacenamiento redundante en la web descentralizada de los datos de prueba subyacentes para archivado a largo plazo. Un SDK Develop permite a las aplicaciones integrar captura y verificación sin construir el formato de procedencia por su cuenta.

## Por qué importa

Para un cliente Nostr de video o imagen, llevar datos ProofMode significa que un espectador tiene una forma externa y multiplataforma de verificar si un contenido multimedia fue capturado como se afirma y si ha sido alterado silenciosamente desde entonces, sin depender del cliente publicador o del relay como fuente de confianza. Esa distinción importa más para una copia descargada o recodificada de un clip: los datos de procedencia que sobreviven a la descarga y a cualquier marca de agua que aplique un cliente son lo que hace que la atestación siga siendo verificable después de que el archivo sale de la aplicación que lo produjo.

## Implementaciones

- [Divine](https://github.com/divinevideo/divine-mobile) - cliente de video corto Nostr; lleva datos de procedencia ProofMode a través de descargas de clips con marca de agua

---

**Fuentes primarias:**
- [ProofMode](https://proofmode.org/)

**Mencionado en:**
- [Newsletter #17](/es/newsletters/2026-04-29-newsletter/)
- [Newsletter #31: Divine Mobile 1.0.16 incorpora un editor de video más profundo, cifrado en reposo y procedencia ProofMode](/es/newsletters/2026-07-15-newsletter/#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance)

**Ver también:**
- [Blossom](/es/topics/blossom/)
