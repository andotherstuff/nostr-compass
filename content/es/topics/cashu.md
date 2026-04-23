---
title: "Cashu: Protocolo Ecash"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-04-22
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu es un protocolo ecash Chaumiano construido sobre Bitcoin y Lightning. Los usuarios poseen tokens al portador emitidos por un mint, y luego transfieren esos tokens sin exponer el grafo completo de pagos al mint.

## Cómo funciona

Cashu usa firmas ciegas para emitir tokens ecash:

1. **Acuñación**: Los usuarios depositan Bitcoin/Lightning en un mint y reciben tokens cegados
2. **Gasto**: Los tokens pueden transferirse peer-to-peer sin involucrar al mint
3. **Canje**: Los destinatarios canjean tokens en el mint por Bitcoin/Lightning

El mint firma secretos cegados, por lo que puede verificar los tokens después sin haber visto los secretos originales en el momento de emisión. Eso rompe el vínculo directo entre depósito y canje dentro del mint.

## Seguridad y Modelo de Confianza

Cashu mejora la privacidad de pagos, pero sigue siendo custodial. Un mint puede rechazar canjes, desconectarse o perder los fondos de respaldo.

Las pruebas Cashu son instrumentos al portador. Quien controle la prueba puede gastarla. Eso hace que el manejo de pruebas se parezca más al efectivo que a un saldo de cuenta: las copias de seguridad, el compromiso de dispositivos o la filtración de tokens en texto plano importan de inmediato.

## Integración con Nostr

Cashu se integra con Nostr de varias formas:

- **Nutzaps**: Tokens ecash enviados como zaps con privacidad mejorada
- **Depósito en garantía**: Depósito de pagos basado en HTLC para servicios como viajes compartidos
- **Billeteras**: Billeteras nativas de Nostr almacenan tokens Cashu cifrados en relays
- **[NIP-87](/es/topics/nip-87/)**: Descubrimiento y reseñas de mints vía Nostr
- **[TollGate](/es/topics/tollgate/)**: Protocolo de acceso de red de pago por uso que acepta tokens ecash de Cashu para conectividad, definido en [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) a partir del [release v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0)

## Compensaciones

Cashu es rápido porque las transferencias ocurren off-chain y a menudo off-mint hasta el canje. La compensación es interoperabilidad y confianza.

En la práctica, los usuarios frecuentemente necesitan el mismo mint, o necesitan un swap o puente entre mints. Por eso las aplicaciones Nostr frecuentemente combinan Cashu con descubrimiento de mints, sincronización de billeteras y sistemas de reseñas.

---

**Fuentes primarias:**
- [Repositorio Cashu NUTs](https://github.com/cashubtc/nuts)
- [NUT-00: Criptografía y modelos](https://github.com/cashubtc/nuts/blob/main/00.md)
- [NIP-60: Billetera Cashu](/es/topics/nip-60/)
- [NIP-87: Recomendaciones de Mints Cashu](/es/topics/nip-87/)

**Mencionado en:**
- [Boletín #7](/es/newsletters/2026-01-28-newsletter/)
- [Boletín #11](/es/newsletters/2026-02-25-newsletter/)
- [Boletín #19: TollGate v0.1.0](/en/newsletters/2026-04-22-newsletter/)

**Ver también:**
- [NIP-60: Billetera Cashu](/es/topics/nip-60/)
- [NIP-87: Recomendaciones de Mints Cashu](/es/topics/nip-87/)
- [TollGate](/es/topics/tollgate/)
