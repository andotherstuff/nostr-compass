---
title: "NIP-98: HTTP Auth"
date: 2026-03-25
translationOf: /en/topics/nip-98.md
translationDate: 2026-04-01
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-98 define autenticación HTTP usando eventos Nostr. Permite a los servidores verificar la identidad Nostr de un cliente en solicitudes HTTP estándar sin contraseñas, claves API ni flujos OAuth.

## Cómo Funciona

Cuando un cliente necesita autenticar una solicitud HTTP, crea un evento kind 27235. Este evento contiene la URL de destino y el método HTTP en sus etiquetas, vinculando la autenticación a una solicitud específica.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1742860800,
  "kind": 27235,
  "tags": [
    ["u", "https://files.example.com/upload"],
    ["method", "POST"],
    ["payload", "<sha256-hash-of-request-body>"]
  ],
  "content": "",
  "sig": "<128-char hex>"
}
```

El cliente firma este evento, lo codifica en base64, y lo envía en el encabezado HTTP `Authorization` con el esquema `Nostr`:

```
Authorization: Nostr <base64-encoded-signed-event>
```

El servidor decodifica el evento, verifica la firma, comprueba que la URL y el método coincidan con la solicitud real, y confirma que la marca de tiempo es reciente. Si todas las verificaciones pasan, el servidor sabe qué pubkey Nostr realizó la solicitud.

La etiqueta opcional `payload` contiene un hash SHA-256 del cuerpo de la solicitud, lo que impide que el evento de autenticación sea reutilizado con contenido diferente. La verificación de marca de tiempo (los servidores típicamente rechazan eventos de más de unos minutos de antigüedad) previene ataques de repetición.

## Casos de Uso

Los servidores Blossom usan NIP-98 para autenticar subidas y eliminaciones de archivos, vinculando los medios almacenados a una identidad Nostr específica. Los servicios de alojamiento de archivos lo usan para imponer cuotas de subida por pubkey. Cualquier API HTTP que necesite identificar a un usuario Nostr sin mantener su propio sistema de cuentas puede aceptar encabezados NIP-98 como prueba de identidad.

---

**Fuentes primarias:**
- [Especificación NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) - HTTP Auth

**Mencionado en:**
- [Newsletter #15](/es/newsletters/2026-03-25-newsletter/)
