---
title: "NIP-47: Nostr Wallet Connect"
date: 2025-12-17
translationOf: /en/topics/nip-47.md
translationDate: 2026-03-11
draft: false
categories:
  - Wallet
  - Lightning
---

NIP-47 define Nostr Wallet Connect, un protocolo para permitir que una aplicación Nostr se comunique con un servicio remoto de billetera Lightning sin exponer las credenciales principales de la billetera a cada cliente.

## Cómo Funciona

Un servicio de billetera publica un evento reemplazable kind `13194` de información que describe los métodos y modos de cifrado que soporta. Un cliente se conecta usando una URI `nostr+walletconnect://` que contiene la pubkey del servicio de billetera, uno o más relays y un secreto dedicado para esa conexión. Las solicitudes se envían como eventos kind `23194` y las respuestas vuelven como eventos kind `23195`.

## Comandos y Notificaciones

Los métodos comunes incluyen `pay_invoice`, `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance` y `get_info`. Los servicios de billetera también pueden enviar notificaciones push como `payment_received`, `payment_sent` y `hold_invoice_accepted`.

La especificación originalmente acumuló varios métodos opcionales con el tiempo, pero una limpieza reciente eliminó los métodos `multi_` de pago. En la práctica, la interoperabilidad es mejor cuando los clientes se limitan a los comandos anunciados por el evento de información de la billetera en lugar de asumir un conjunto amplio de métodos.

## Casos de Uso

- **Zapping** - Enviar sats a publicaciones, perfiles o creadores de contenido
- **Pagos** - Pagar facturas Lightning desde cualquier aplicación Nostr
- **Separación de UX de billetera** - Usar un servicio de billetera a través de muchos clientes Nostr

## Notas de Seguridad e Interoperabilidad

La URI de conexión contiene un secreto dedicado que el cliente usa para firma y cifrado. Eso da a cada aplicación su propia identidad de billetera, lo que ayuda tanto a la revocación como a la privacidad. Una billetera puede limitar el gasto, deshabilitar métodos o revocar una conexión sin afectar a otra.

NIP-44 es ahora el modo de cifrado preferido. La especificación aún documenta el fallback NIP-04 para implementaciones antiguas, por lo que los clientes necesitan inspeccionar el tag `encryption` anunciado por la billetera en lugar de asumir que todas las billeteras han migrado.

---

**Fuentes primarias:**
- [Especificación NIP-47](https://github.com/nostr-protocol/nips/blob/master/47.md)
- [PR #1913: Soporte de Hold Invoice](https://github.com/nostr-protocol/nips/pull/1913)
- [PR #2210: Simplificación](https://github.com/nostr-protocol/nips/pull/2210)

**Mencionado en:**
- [Newsletter #1: Noticias](/es/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: Lanzamientos](/es/newsletters/2025-12-24-newsletter/#releases)
- [Newsletter #3: Resumen de Diciembre](/es/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #8: Análisis Profundo de NIP](/es/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-47-nostr-wallet-connect)
- [Newsletter #10: Actualizaciones de NIPs](/es/newsletters/2026-02-18-newsletter/#nip-updates)

**Ver también:**
- [NIP-57: Zaps](/es/topics/nip-57/)
