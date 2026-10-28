---
title: "NIP-82 propuesto (sin asignar): catálogo de aplicaciones de software"
date: 2026-06-17
lastmod: 2026-10-28
translationOf: /en/topics/nip-82.md
translationDate: 2026-10-28
draft: false
categories:
  - Proposals
  - Apps
---

El catálogo de aplicaciones de software que se describe en esta página es una propuesta en revisión. No es un NIP aceptado. Se encuentra en la [pull request #2526 de nostr-protocol/nips](https://github.com/nostr-protocol/nips/pull/2526), titulada «Zapstore spec». En la fecha de la última actualización de esta página, esa pull request sigue abierta y sin fusionar, y la rama master oficial de los NIPs no contiene ningún archivo `82.md`. «NIP-82» es la etiqueta que la propuesta se da a sí misma. No es un número de NIP oficial. Los kinds de event, los tags y el comportamiento pueden cambiar antes de cualquier fusión. Según la pull request, esta sustituye a la anterior [pull request #1336](https://github.com/nostr-protocol/nips/pull/1336).

## Kinds de event propuestos

El borrador divide un catálogo de software en varios tipos de event:

- **Kind 32267, aplicación:** un event direccionable que describe una app.
- **Kind 30063, lanzamiento:** un event direccionable para una versión concreta de esa app. Hace referencia a los recursos de esa versión.
- **Kind 3063, recurso:** un event regular que describe un archivo descargable.
- **Kind 30267, curación:** una lista direccionable que publica un curador para agrupar o recomendar apps.
- **Kind 30509, vínculo de certificado de firma:** un event direccionable que vincula un certificado X.509, como un certificado de firma de APK, a la clave de Nostr que publica el software, de modo que los clientes sepan qué certificados controla ese publicador. Su tag `d` es el hash SHA-256 del certificado codificado en DER. Lleva una firma hecha con la clave privada del certificado y una caducidad expresada como marca de tiempo Unix, y opcionalmente puede marcar el vínculo como revocado.
- **Kind 10067, lista de relays:** una lista reemplazable de relays en los que se pueden encontrar events del catálogo.

## Plataforma, integridad y validez

Los events de recurso llevan identificadores de plataforma y de entorno de ejecución, para que un cliente pueda mostrar solo los archivos que corresponden a un dispositivo. Cada recurso lleva además un hash del archivo. Con él, un cliente puede comprobar que los bytes descargados coinciden con lo que firmó el publicador. Para los paquetes de Android, el borrador incluye la huella del certificado de firma. Antes de ofrecer una actualización, un instalador puede compararla con el certificado de una app que ya esté instalada. Antes de instalar un paquete de Android, los clientes DEBERÍAN obtener el event de kind 30509 por el hash del certificado. Deberían verificar su firma de certificado frente al certificado incrustado en el APK y frente al publicador del recurso, y comprobar que la prueba no ha caducado ni ha sido revocada.

## Límites de confianza

Una firma válida solo demuestra que una clave concreta publicó un event. No prueba que la clave pertenezca al desarrollador real, que el software sea seguro ni que la lista de un curador sea fiable. La propuesta no ofrece ninguna garantía sobre publicadores arbitrarios. Son los clientes y los usuarios quienes deben decidir en qué claves de publicadores y curadores confiar. Esta página no afirma que exista ninguna auditoría de seguridad ni interoperabilidad en producción.

## Relación con NIP-89

Los events de handler de [NIP-89](/es/topics/nip-89/) anuncian qué aplicaciones pueden gestionar qué kinds de event. Esta propuesta, en cambio, describe los artefactos de software y dónde obtenerlos, por lo que ambas abarcan cuestiones distintas.

---

**Fuentes primarias:**
- [PR #2526 de nostr-protocol/nips: Zapstore spec](https://github.com/nostr-protocol/nips/pull/2526) (abierta, sin fusionar; sustituye a la [PR #1336](https://github.com/nostr-protocol/nips/pull/1336))

**Mencionado en:**
- [Boletín n.º 27: cobertura del lanzamiento de Amethyst v1.12.0 (referencia histórica)](/en/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Boletín n.º 46: catálogo de aplicaciones de software propuesto como NIP-82](/es/newsletters/2026-10-28-newsletter/#software-application-catalog-proposed-as-nip-82)

**Véase también:**
- [NIP-89: manejadores de aplicaciones](/es/topics/nip-89/)
