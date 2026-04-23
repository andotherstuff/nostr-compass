---
title: "NIP-42: Autenticación de clientes a relays"
date: 2026-01-21
translationOf: /en/topics/nip-42.md
translationDate: 2026-04-22
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-42 define cómo los clientes se autentican ante relays. Los relays pueden requerir autenticación para proporcionar control de acceso, prevenir abusos o implementar servicios de relay de pago.

## Cómo funciona

El flujo de autenticación comienza cuando un relay envía un mensaje `AUTH` al cliente. Este mensaje contiene una cadena de desafío que el cliente debe firmar. El cliente crea un evento de autenticación kind 22242 que contiene el desafío y lo firma con su clave privada. El relay verifica la firma y el desafío, luego otorga acceso.

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

El desafío previene ataques de replay. La URL del relay en los tags impide que el mismo evento firmado se reutilice en diferentes relays.

## Notas del protocolo

La autenticación tiene alcance de conexión. Un desafío permanece válido durante la duración de la conexión, o hasta que el relay envíe uno nuevo. El evento firmado es efímero y no debe ser difundido como un evento normal.

La especificación también define prefijos de error legibles por máquina. `auth-required:` significa que el cliente aún no se ha autenticado. `restricted:` significa que se autenticó, pero esa pubkey carece de permisos para la acción solicitada.

## Casos de uso

Los relays de pago usan NIP-42 para verificar suscriptores antes de otorgar acceso. Los relays privados lo usan para limitar lecturas o escrituras a pubkeys aprobadas. También mejora la limitación de tasa porque los relays pueden rastrear el comportamiento por clave autenticada en lugar de por dirección IP.

Combinado con metadatos [NIP-11](/es/topics/nip-11/), los clientes pueden descubrir si un relay soporta NIP-42 antes de intentar consultas protegidas. En la práctica, el soporte sigue siendo desigual, por lo que los clientes necesitan un camino alternativo cuando un relay anuncia NIP-42 pero maneja eventos protegidos incorrectamente.

---

**Fuentes primarias:**
- [Especificación NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) - Autenticación de clientes a relays

**Mencionado en:**
- [Newsletter #6: Documentos de Información de Relay](/es/newsletters/2026-01-21-newsletter/)
- [Newsletter #9: Pruebas de Estado de Relay Marmot](/es/newsletters/2026-02-11-newsletter/)
- [Newsletter #10: Nostr MCP Server](/es/newsletters/2026-02-18-newsletter/)
- [Newsletter #13: AUTH de relay en apps reales](/en/newsletters/2026-03-11-newsletter/)

**Ver también:**
- [NIP-11: Documento de Información de Relay](/es/topics/nip-11/)
- [NIP-50: Búsqueda](/es/topics/nip-50/)
