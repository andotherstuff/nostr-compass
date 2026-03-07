---
title: "NIP-55: Aplicación firmante para Android"
date: 2025-12-17
translationOf: /en/topics/nip-55.md
translationDate: 2026-03-07
draft: false
categories:
  - Signing
  - Mobile
---

NIP-55 define cómo las aplicaciones Android solicitan operaciones de firma y cifrado desde una aplicación firmante separada. Ofrece a los clientes Android una alternativa nativa a las extensiones de navegador y los bunkers remotos.

## Cómo funciona

NIP-55 usa dos mecanismos de Android:

- **Intents** para flujos en primer plano con aprobación explícita del usuario
- **Content resolvers** para flujos en segundo plano después de que el usuario concede permiso persistente

El flujo de conexión habitual comienza con `get_public_key`. El firmante devuelve tanto la pubkey del usuario como el nombre del paquete del firmante, y se espera que el cliente cachee ambos. Repetir `get_public_key` en bucles en segundo plano es un error de implementación común contra el que la especificación advierte explícitamente.

## Operaciones principales

- **get_public_key** - Obtener la pubkey del usuario y el nombre del paquete del firmante
- **sign_event** - Firmar un evento Nostr
- **nip04_encrypt/decrypt** - Cifrar o descifrar mensajes NIP-04
- **nip44_encrypt/decrypt** - Cifrar o descifrar mensajes NIP-44
- **decrypt_zap_event** - Descifrar payloads de eventos relacionados con zaps

## Notas de seguridad y UX

NIP-55 mantiene las claves en el dispositivo, pero depende de los límites de las aplicaciones Android y del manejo de permisos del firmante. El soporte de content resolver ofrece una UX más fluida que las solicitudes repetidas de intents, pero solo después de que el usuario haya concedido aprobación duradera a ese cliente.

Para aplicaciones web en Android, NIP-55 es menos ergonómico que NIP-46. Los flujos basados en navegador no pueden recibir respuestas directas en segundo plano de la manera en que las aplicaciones nativas de Android pueden, así que muchas implementaciones recurren a URLs de callback, transferencia por portapapeles o pegado manual.

---

**Fuentes primarias:**
- [Especificación NIP-55](https://github.com/nostr-protocol/nips/blob/master/55.md)

**Mencionado en:**
- [Boletín #1: Lanzamientos](/en/newsletters/2025-12-17-newsletter/#releases)
- [Boletín #2: Noticias](/en/newsletters/2025-12-24-newsletter/#news)
- [Boletín #2: Actualizaciones de NIP](/en/newsletters/2025-12-24-newsletter/#nip-updates)
- [Boletín #3: Resumen de diciembre](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Boletín #7: Actualizaciones de NIP](/en/newsletters/2026-01-07-newsletter/#nip-updates)
- [Boletín #11: NIP Deep Dive](/en/newsletters/2026-02-25-newsletter/#nip-deep-dive-nip-55-android-signer-application)

**Ver también:**
- [NIP-46: Nostr Connect](/es/topics/nip-46/)
