---
title: "Dominios públicos de FIPS"
date: 2026-09-30
draft: false
categories:
  - Protocol
  - Networking
  - Identity
translationOf: /en/topics/fips-pub-domains.md
translationDate: 2026-10-01
---

fips-pub-domains es una implementación inicial para resolver nombres de dominio habituales de Internet a servicios de la red de malla [FIPS](/es/topics/fips/). Publica declaraciones firmadas de Nostr, pero una firma solo demuestra quién hizo una declaración. Un cliente también debe comprobar pruebas de DNS o DNSSEC, un testigo de confianza o una vinculación fijada previamente antes de considerar al declarante como propietario del dominio.

## Verificación y uso sin conexión

La [primera versión](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.1.0) añadió la declaración, el demonio de resolución y la integración con Android. La [versión 0.2.0](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.0) puede adjuntar una prueba DNSSEC a una declaración, lo que permite que un cliente que solo ve un relay de la red de malla verifique un dominio firmado que no haya visto antes frente a las claves raíz de DNS. También admite más de un servidor verificado para un dominio. La [versión 0.2.1](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.1) corrigió la unidad de servidor incluida en el paquete y la modificó para que se ejecutara sin root; las instalaciones existentes necesitan la unidad de reemplazo.

Las [notas de pruebas](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md) del proyecto describen casos con dos nodos y con un relay accesible únicamente a través de la red de malla. Son pruebas comunicadas por el mantenedor, no pruebas de un despliegue más amplio. Su [propuesta NIP-DB](https://github.com/nostr-protocol/nips/pull/2487) sigue abierta, y los números de kind de event de su borrador son marcadores provisionales, no valores de kind asignados en Nostr.

---

**Fuentes primarias:**
- [Repositorio y README](https://github.com/fr34aky/fips-pub-domains)
- [Versiones 0.1.0–0.2.1](https://github.com/fr34aky/fips-pub-domains/releases)
- [Propuesta NIP-DB](https://github.com/nostr-protocol/nips/pull/2487)
- [Notas de pruebas](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)

**Mencionado en:**
- [Boletín #42: fips-pub-domains](/es/newsletters/2026-09-30-newsletter/#fips-pub-domains-tests-signed-public-names-for-a-mesh)

**Véase también:**
- [FIPS](/es/topics/fips/)
