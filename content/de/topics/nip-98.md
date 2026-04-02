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

NIP-98 definiert HTTP-Authentifizierung mittels Nostr-Events. Es ermöglicht Servern, die Nostr-Identität eines Clients bei Standard-HTTP-Anfragen zu verifizieren, ohne Passwörter, API-Schlüssel oder OAuth-Flows.

## Funktionsweise

Wenn ein Client eine HTTP-Anfrage authentifizieren muss, erstellt er ein kind-27235-Event. Dieses Event enthält die Ziel-URL und die HTTP-Methode in seinen Tags und bindet die Authentifizierung an eine bestimmte Anfrage.

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

Der Client signiert dieses Event, Base64-kodiert es und sendet es im HTTP-`Authorization`-Header mit dem `Nostr`-Schema:

```
Authorization: Nostr <base64-encoded-signed-event>
```

Der Server dekodiert das Event, verifiziert die Signatur, prüft, ob URL und Methode mit der tatsächlichen Anfrage übereinstimmen, und bestätigt, dass der Zeitstempel aktuell ist. Wenn alle Prüfungen bestehen, weiß der Server, welcher Nostr-Pubkey die Anfrage gestellt hat.

Der optionale `payload`-Tag enthält einen SHA-256-Hash des Anfragekörpers, was verhindert, dass das Auth-Event mit anderem Inhalt wiederverwendet wird. Die Zeitstempelprüfung (Server lehnen typischerweise Events ab, die älter als einige Minuten sind) verhindert Replay-Angriffe.

## Anwendungsfälle

Blossom-Server verwenden NIP-98, um Datei-Uploads und -Löschungen zu authentifizieren und gespeicherte Medien an eine bestimmte Nostr-Identität zu binden. Datei-Hosting-Dienste verwenden es, um Upload-Kontingente pro Pubkey durchzusetzen. Jede HTTP-API, die einen Nostr-Nutzer identifizieren muss, ohne ein eigenes Kontosystem zu pflegen, kann NIP-98-Header als Identitätsnachweis akzeptieren.

---

**Primärquellen:**
- [NIP-98-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/98.md) - HTTP Auth

**Erwähnt in:**
- [Newsletter #15](/de/newsletters/2026-03-25-newsletter/)
