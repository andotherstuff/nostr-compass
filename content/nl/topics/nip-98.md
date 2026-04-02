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

NIP-98 definieert HTTP-authenticatie met behulp van Nostr-events. Het stelt servers in staat de Nostr-identiteit van een client te verifiëren bij standaard HTTP-verzoeken zonder wachtwoorden, API-sleutels of OAuth-flows.

## Hoe Het Werkt

Wanneer een client een HTTP-verzoek moet authenticeren, maakt het een kind 27235 event aan. Dit event bevat de doel-URL en HTTP-methode in zijn tags, waardoor de authenticatie aan een specifiek verzoek wordt gebonden.

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

De client ondertekent dit event, base64-codeert het, en stuurt het mee in de HTTP `Authorization` header met het `Nostr` schema:

```
Authorization: Nostr <base64-encoded-signed-event>
```

De server decodeert het event, verifieert de handtekening, controleert dat de URL en methode overeenkomen met het werkelijke verzoek, en bevestigt dat de tijdstempel recent is. Als alle controles slagen, weet de server welke Nostr pubkey het verzoek heeft gedaan.

De optionele `payload` tag bevat een SHA-256 hash van de verzoekbody, wat voorkomt dat het auth-event hergebruikt wordt met andere inhoud. De tijdstempelcontrole (servers weigeren doorgaans events ouder dan enkele minuten) voorkomt replay-aanvallen.

## Toepassingen

Blossom-servers gebruiken NIP-98 om bestandsuploads en -verwijderingen te authenticeren, waarbij opgeslagen media wordt gekoppeld aan een specifieke Nostr-identiteit. Bestandshostingservices gebruiken het om uploadquota per pubkey af te dwingen. Elke HTTP API die een Nostr-gebruiker moet identificeren zonder een eigen accountsysteem te onderhouden, kan NIP-98 headers accepteren als identiteitsbewijs.

---

**Primaire bronnen:**
- [NIP-98 Specificatie](https://github.com/nostr-protocol/nips/blob/master/98.md) - HTTP Auth

**Vermeld in:**
- [Newsletter #15](/nl/newsletters/2026-03-25-newsletter/)
