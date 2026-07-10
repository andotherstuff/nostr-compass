---
title: "NIP-61: Nutzaps"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-61.md
translationDate: 2026-07-01
categories:
  - Zaps
  - Ecash
---

NIP-61 define los "nutzaps", pagos de ecash Cashu peer-to-peer entregados como eventos de Nostr. Un emisor publica un token Cashu bloqueado con P2PK dirigido a la clave de Nostr del destinatario, y el destinatario lo canjea en el mint cuando le convenga. Las propias pruebas transportan el valor, por lo que un pago NIP-61 llega como un token autocontenido que el destinatario puede canjear según su propio horario, sin necesidad de un canal Lightning ni de un handshake interactivo.

## Cómo funciona

NIP-61 se construye sobre dos primitivas existentes: wallets Cashu [NIP-60](/es/topics/nip-60/) y los bloqueos P2PK de Cashu. El flujo utiliza tres kinds de evento.

**Recomendación de mint (kind 10019):** un evento reemplazable que el destinatario publica para anunciar de qué mints acepta nutzaps y la clave pública de Cashu usada para bloquear pruebas a él. Los emisores leen esto antes de enviar para que el token bloqueado sea uno que el destinatario pueda canjear.

**Evento nutzap (kind 9321):** el pago en sí. Transporta las pruebas Cashu (bloqueadas con P2PK a la pubkey nutzap del destinatario del kind 10019), la URL del mint, tags opcionales `e` y `a` que identifican la nota zapeada, y un tag `p` para el destinatario. El destinatario lo recibe mediante suscripciones normales de Nostr, desbloquea las pruebas con la clave privada correspondiente y las mantiene en su wallet NIP-60 o las funde a Lightning.

**Info de nutzap (kind 7375):** estado en caché con la misma forma que los eventos de token NIP-60, registrando las pruebas de nutzap canjeadas para que la wallet no las cuente dos veces en una resincronización.

## Compromisos y modelo de confianza

Un nutzap es un token de ecash autocontenido. Mientras el destinatario pueda contactar más tarde con el mint, puede canjear el pago. El propio mint es el custodio de confianza, el mismo modelo de confianza que NIP-60, y esa elección de custodia es el precio explícito de los micropagos con capacidad offline y finalidad instantánea. Los zaps NIP-57 requieren que el receptor ejecute (o esté alojado en) un nodo Lightning con un endpoint LNURL que acepte HTLCs entrantes en tiempo real. Los teléfonos sin canal Lightning, los usuarios detrás de cortafuegos y los destinatarios que casualmente están offline quedan fuera de ese modelo.

El anuncio de kind 10019 es la puerta de confianza a nivel social. El emisor elige uno de los mints aceptados por el destinatario, lo que mantiene predecible la ruta de canje del destinatario. Un emisor que elige un mint fuera del conjunto del destinatario arriesga un token no canjeable, por lo que las wallets leen kind 10019 primero.

## Flujo de trabajo

1. El destinatario publica un kind 10019 anunciando los mints aceptados y una pubkey de nutzap
2. El emisor lee el kind 10019, acuña pruebas en uno de los mints listados y las bloquea con P2PK a la pubkey de nutzap del destinatario
3. El emisor publica un kind 9321 con las pruebas bloqueadas, la URL del mint y los tags objetivo
4. El destinatario recibe el kind 9321 vía su suscripción normal de Nostr
5. El destinatario desbloquea las pruebas usando su clave privada de nutzap y las mantiene en su wallet NIP-60 o las funde a Lightning

## Ejemplo de evento nutzap

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1750162800,
  "kind": 9321,
  "tags": [
    ["proof", "{\"amount\":21,\"secret\":\"...\",\"C\":\"...\",\"id\":\"...\"}"],
    ["u", "https://mint.example.com"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3"],
    ["p", "c5d8a4e3b2a1f0e9d8c7b6a5949382716050403020100ffeeddccbbaa99887766"]
  ],
  "content": "Great post!",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

## Implementaciones

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) incorpora renderizado de nutzaps con vistas de saldo por mint como parte de su superficie de wallet NIP-60/NIP-61 ([PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075))

---

**Fuentes primarias:**
- [Especificación NIP-61](https://github.com/nostr-protocol/nips/blob/master/61.md)
- [Amethyst PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075) - Soporte de wallet Cashu NIP-60 y nutzap NIP-61

**Mencionado en:**
- [Boletín #27: Amethyst v1.12.0 incorpora wallets Cashu, nutzaps, un driver CLINK y auto-reparación de Tor](/es/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**Véase también:**
- [NIP-57: Zaps](/es/topics/nip-57/)
- [NIP-60: Wallet Cashu](/es/topics/nip-60/)
- [Cashu](/es/topics/cashu/)
