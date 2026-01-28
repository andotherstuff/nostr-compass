---
title: "NIP-42: Autenticación de clientes a relays"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-42 define cómo los clientes se autentican ante relays. Los relays pueden requerir autenticación para proporcionar control de acceso, prevenir abusos o implementar servicios de relay de pago.

## Cómo Funciona

El flujo de autenticación comienza cuando un relay envía un mensaje AUTH al cliente. Este mensaje contiene una cadena de desafío que el cliente debe firmar. El cliente crea un evento de autenticación kind 22242 conteniendo el desafío y lo firma con su clave privada. El relay verifica la firma y el desafío, luego otorga acceso.

```json
{
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com"],
    ["challenge", "random-challenge-string"]
  ],
  "content": "",
  "pubkey": "<client_pubkey>",
  "created_at": 1736784000,
  "sig": "<signature>"
}
```

El desafío previene ataques de replay: los clientes deben firmar desafíos frescos para cada intento de autenticación. La URL del relay en los tags asegura que los tokens de autenticación no puedan reutilizarse a través de diferentes relays.

## Casos de Uso

Los relays de pago usan NIP-42 para verificar suscriptores antes de otorgar acceso. Después de autenticarse, los relays pueden verificar el estado de pago o la expiración de suscripción. Los relays privados restringen el acceso a pubkeys aprobadas, creando comunidades cerradas o infraestructura de relay personal.

La limitación de tasa se vuelve más efectiva con autenticación. Los relays pueden rastrear tasas de solicitud por pubkey autenticada en lugar de por dirección IP, previniendo abusos mientras soportan usuarios legítimos detrás de IPs compartidas. La prevención de spam mejora cuando los relays requieren autenticación para publicar eventos.

Algunos relays usan NIP-42 para analíticas, rastreando qué usuarios acceden a qué contenido sin requerir cuentas centralizadas. Combinado con metadatos [NIP-11](/es/topics/nip-11/), los clientes descubren si los relays requieren autenticación antes de intentar conexiones.

---

**Fuentes primarias:**
- [Especificación NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) - Autenticación de clientes a relays

**Ver también:**
- [NIP-11: Documento de Información de Relay](/es/topics/nip-11/)
- [NIP-50: Capacidad de Búsqueda](/es/topics/nip-50/)
