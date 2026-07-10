---
title: "CLINK: Interfaz común de Lightning para claves de Nostr"
date: 2026-06-17
draft: false
translationOf: /en/topics/clink.md
translationDate: 2026-07-01
categories:
  - Payments
  - Lightning
---

CLINK (Common Lightning Interface for Nostr Keys) es un formato propuesto de solicitud de pago que permite a un emisor pagar a cualquier identidad basada en clave de Nostr usando una única interfaz noffer. Un noffer CLINK codifica la clave pública de Nostr del destinatario junto con suficientes metadatos de enrutamiento para que la wallet del emisor construya un pago Lightning, un pago on-chain o una futura primitiva de liquidación que resuelva al destinatario. El destinatario publica un noffer por identidad, y los emisores lo pagan sin saber si la wallet receptora liquida por Lightning, on-chain o por otro rail.

## Cómo funciona

Un noffer CLINK es una solicitud de pago estructurada que la wallet del emisor decodifica en una instrucción de pago concreta. El noffer contiene:

- La clave pública de Nostr del destinatario como raíz canónica de identidad
- Uno o más endpoints de pago (URI de nodo Lightning, pista de derivación de dirección on-chain, futuros rails)
- Metadatos opcionales para el pago (memo, monto, expiración)
- Una firma del destinatario que vincula el noffer a su identidad de Nostr

Una wallet emisora que soporta CLINK lee el noffer, elige el rail que puede servir (una wallet solo-Lightning paga el endpoint Lightning, una wallet multi-rail elige la ruta más barata) y envía el pago. La wallet del destinatario confirma la recepción publicando o consultando el evento de finalización correspondiente, con la clave pública de Nostr actuando como identidad duradera entre rails.

## Por qué una interfaz basada en clave de Nostr

LNURL y BOLT-12 ya existen como formatos de solicitud de pago Lightning, y Bitcoin cuenta con un formato de dirección bien conocido para liquidación on-chain. CLINK no reemplaza ninguno. Añade una capa enraizada en la clave de Nostr para que un emisor pueda dirigirse a un destinatario por su identidad de Nostr y dejar que la wallet resuelva qué rail subyacente usar. Un usuario que cambia de proveedor Lightning, abre un nuevo mint o migra su wallet on-chain vuelve a publicar su noffer con la misma clave de Nostr, y los emisores no necesitan actualizar sus libretas de direcciones.

Para Zeus Pay (que genera un noffer CLINK para cada cuenta), esto significa que un emisor puede pagar a cualquier usuario de Zeus solo por clave de Nostr. Para el driver de zap on-chain de Amethyst, la máquina de estados de verificación de CLINK confirma que el noffer firmado on-chain coincide con la pubkey de Nostr declarada en la solicitud de zap, cerrando una ruta de falsificación contra zaps on-chain sin firmar.

## Implementaciones

- [Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) incorpora soporte de pagos con noffer CLINK, con Zeus Pay generando un noffer CLINK para cada cuenta para que un emisor pueda pagar a cualquier usuario de Zeus solo por clave de Nostr
- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) incorpora un driver CLINK para verificación de zaps on-chain con una máquina de estados de verificación y un driver de reverificación ([PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039), [PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177), [PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182))

---

**Fuentes primarias:**
- [Notas de lanzamiento de Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1) - Lanzamiento de noffer CLINK
- [Amethyst PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039) - Máquina de estados de verificación de zaps on-chain NIP-BC y driver de reverificación
- [Amethyst PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177) - Implementar CLINK (Common Lightning Interface for Nostr Keys)
- [Amethyst PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182) - Añadir soporte de kotlinx-serialization para los DTOs del protocolo CLINK

**Mencionado en:**
- [Boletín #27: Amethyst v1.12.0 incorpora wallets Cashu, nutzaps, un driver CLINK y auto-reparación de Tor](/es/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Boletín #27: Zeus v13.1.0-rc1 incorpora noffers CLINK y NWC sin cola](/es/newsletters/2026-06-17-newsletter/#zeus-v1310-rc1-ships-clink-noffers-and-queue-less-nwc)

**Véase también:**
- [NIP-57: Zaps](/es/topics/nip-57/)
- [NIP-47: Nostr Wallet Connect](/es/topics/nip-47/)
