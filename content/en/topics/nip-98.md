---
title: "NIP-98: HTTP Auth"
date: 2026-03-25
draft: false
categories:
  - NIPs
  - Authentication
---

NIP-98 defines HTTP authentication using Nostr events. It allows servers to verify a client's Nostr identity on standard HTTP requests without passwords, API keys, or OAuth flows.

## How It Works

When a client needs to authenticate an HTTP request, it creates a kind 27235 event. This event contains the target URL and HTTP method in its tags, binding the authentication to a specific request.

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

The client signs this event, base64-encodes it, and sends it in the HTTP `Authorization` header with the `Nostr` scheme:

```
Authorization: Nostr <base64-encoded-signed-event>
```

The server decodes the event, verifies the signature, checks that the URL and method match the actual request, and confirms the timestamp is recent. If all checks pass, the server knows which Nostr pubkey made the request.

The optional `payload` tag contains a SHA-256 hash of the request body, which prevents the auth event from being reused with different content. The timestamp check (servers typically reject events older than a few minutes) prevents replay attacks.

## Use Cases

Blossom servers use NIP-98 to authenticate file uploads and deletions, tying stored media to a specific Nostr identity. File hosting services use it to enforce upload quotas per pubkey. Any HTTP API that needs to identify a Nostr user without maintaining its own account system can accept NIP-98 headers as proof of identity.

---

**Primary sources:**
- [NIP-98 Specification](https://github.com/nostr-protocol/nips/blob/master/98.md) - HTTP Auth

**Mentioned in:**
- [Newsletter #15](/en/newsletters/2026-03-25-newsletter/)
