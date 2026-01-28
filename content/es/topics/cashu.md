---
title: "Cashu: Protocolo Ecash"
date: 2026-01-28
translationOf: /en/topics/cashu.md
translationDate: 2026-01-28
draft: false
categories:
  - Payments
  - Privacy
  - Bitcoin
---

Cashu es un protocolo ecash Chaumiano construido sobre Bitcoin y Lightning Network, permitiendo pagos privados, instantáneos y de bajas comisiones a través de tokens criptográficos.

## Cómo Funciona

Cashu usa firmas ciegas para crear tokens ecash no rastreables:

1. **Acuñación**: Los usuarios depositan Bitcoin/Lightning en un mint y reciben tokens cegados
2. **Gasto**: Los tokens pueden transferirse peer-to-peer sin involucrar al mint
3. **Canje**: Los destinatarios canjean tokens en el mint por Bitcoin/Lightning

El mint no puede vincular depósitos con canjes debido al proceso de cegado, proporcionando fuertes garantías de privacidad.

## Propiedades Clave

- **Privacidad**: El mint no puede rastrear transferencias de tokens entre usuarios
- **Instantáneo**: Las transferencias ocurren offline, sin necesidad de confirmación en blockchain
- **Bajas comisiones**: Sin comisiones on-chain para transferencias de tokens
- **Custodial**: Los usuarios confían en el mint para honrar los canjes

## Integración con Nostr

Cashu se integra con Nostr de varias formas:

- **Nutzaps**: Tokens ecash enviados como zaps con privacidad mejorada
- **Depósito en garantía**: Depósito de pagos basado en HTLC para servicios como viajes compartidos
- **Billeteras**: Billeteras nativas de Nostr almacenan tokens Cashu cifrados en relays
- **[NIP-87](/es/topics/nip-87/)**: Descubrimiento y reseñas de mints vía Nostr

## Modelo de Confianza

A diferencia del Bitcoin auto-custodiado, Cashu requiere confiar en los operadores de mints. Los usuarios deben:
- Usar mints reputables y bien reseñados
- Mantener saldos pequeños apropiados al nivel de confianza
- Entender que los mints pueden hacer exit-scam o desconectarse, llevándose los fondos

## Relacionado

- [NIP-87](/es/topics/nip-87/) - Recomendaciones de Mints Cashu
- [NIP-60](/es/topics/nip-60/) - Billetera Nostr
