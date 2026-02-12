---
title: "NIP-39: Identidades Externas en Perfiles"
date: 2026-02-11
translationOf: /en/topics/nip-39.md
translationDate: 2026-02-12
draft: false
categories:
  - NIPs
  - Identity
---

NIP-39 define cómo adjuntar claims de identidad externa a perfiles Nostr usando etiquetas `i`. Estas etiquetas vinculan una pubkey Nostr a cuentas en plataformas externas como GitHub, Twitter o dominios DNS.

## Cómo Funciona

Se publican claims de identidad como etiquetas `i`. Cada etiqueta contiene un identificador de plataforma y una URL de prueba donde la cuenta externa enlaza de vuelta a la pubkey Nostr, estableciendo verificación bidireccional:

```json
{
  "tags": [
    ["i", "github:username", "https://gist.github.com/username/proof"],
    ["i", "twitter:handle", "https://twitter.com/handle/status/proof_tweet_id"]
  ]
}
```

Al obtener la URL de prueba, el cliente verifica que contiene la pubkey Nostr del usuario. Esto crea una red de conexiones de identidad sin requerir servicios de verificación centralizados.

## Cambios Recientes

A febrero de 2026, [PR #2216](https://github.com/nostr-protocol/nips/pull/2216) extrajo las etiquetas de identidad de eventos kind 0 (metadatos de usuario) a un kind dedicado 10011. El cambio fue parte de la campaña de reducción del kind 0 de vitorpamplona, motivada por la baja adopción. Casi ningún cliente implementó la verificación de etiquetas `i`, pero cada consulta de kind 0 cargaba con ese overhead. El nuevo kind 10011 permite a clientes interesados obtener claims de identidad por separado.

---

**Fuentes principales:**
- [NIP-39: External Identities in Profiles](https://github.com/nostr-protocol/nips/blob/master/39.md)

**Mencionado en:**
- [Newsletter #9: Actualizaciones de NIPs](/es/newsletters/2026-02-11-newsletter/#actualizaciones-de-nips)

**Ver también:**
- [NIP-05: Verificación Basada en DNS](/es/topics/nip-05/)
