---
title: "Propuesta NIP-DB: Vinculaciones de servicios de dominio"
date: 2026-09-30
draft: false
categories:
  - Proposals
  - Networking
  - Identity
translationOf: /en/topics/nip-db.md
translationDate: 2026-10-01
---

NIP-DB es una **propuesta abierta** para vincular un dominio de Internet convencional a un servicio direccionado por clave. Sus valores de kind para event y su redacción siguen sujetos a revisión; esta página no lo presenta como una especificación de Nostr aceptada.

## Modelo de verificación

Una clave que presta el servicio puede publicar una declaración firmada que indique el dominio y el servicio. La propuesta describe pruebas opcionales de DNS o DNSSEC, atestaciones de testigos y un registro de zona para los nombres bajo el dominio. Una firma demuestra qué clave publicó una declaración, pero no demuestra el control del dominio. Un cliente debe verificar la vinculación mediante pruebas de DNS, un testigo de confianza o una clave previamente fijada antes de utilizarla para resolver un nombre.

[fips-pub-domains](/es/topics/fips-pub-domains/) es la implementación de referencia del autor para la malla FIPS. Sus pruebas documentadas de dos nodos y exclusivamente en malla constituyen pruebas de la implementación comunicadas por el mantenedor. No resuelven la revisión abierta de la propuesta ni demuestran un despliegue más amplio.

---

**Fuentes primarias:**
- [Solicitud de incorporación de cambios abierta de NIP-DB](https://github.com/nostr-protocol/nips/pull/2487)
- [Borrador del autor y marcadores provisionales de kind de event](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/nip.md)
- [Implementación de referencia y pruebas](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**Mencionado en:**
- [Boletín #42: dominios públicos](/es/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)
- [Boletín #42: propuesta NIP-DB](/es/newsletters/2026-09-30-newsletter/#nip-db-proposes-verified-domain-names-for-key-addressed-services)
