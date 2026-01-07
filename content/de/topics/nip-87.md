---
title: "NIP-87: Ecash Mint Auffindbarkeit"
date: 2026-01-07
draft: false
categories:
  - Ecash
  - Discovery
  - Protocol
---

NIP-87 definiert, wie Ecash-Mints (Cashu und Fedimint) sich auf Nostr ankündigen können und wie Nutzer anderen Mints empfehlen können.

## Event Kinds

- **kind 38172** - Cashu Mint Ankündigung (veröffentlicht von Mint-Betreibern)
- **kind 38173** - Fedimint Ankündigung (veröffentlicht von Mint-Betreibern)
- **kind 38000** - Mint-Empfehlung (veröffentlicht von Nutzern)

## Wie es funktioniert

1. **Mint-Betreiber** veröffentlichen die URL ihres Mints, unterstützte Features und Netzwerk (Mainnet/Testnet)
2. **Nutzer**, die einem Mint vertrauen, veröffentlichen Empfehlungen mit optionalen Bewertungen
3. **Andere Nutzer** fragen Empfehlungen von Personen ab, denen sie folgen, um vertrauenswürdige Mints zu entdecken

## Cashu Mint Ankündigung

```json
{
  "id": "<event-id>",
  "pubkey": "<mint-operator-pubkey>",
  "created_at": 1736200000,
  "kind": 38172,
  "tags": [
    ["d", "<mint-pubkey>"],
    ["u", "https://mint.example.com"],
    ["nuts", "1,2,3,4,5,6,7"],
    ["n", "mainnet"]
  ],
  "content": "",
  "sig": "<signature>"
}
```

Der `nuts`-Tag listet unterstützte NUTs (Notation, Usage, and Terminology Spezifikationen für Cashu) auf.

## Nutzer-Empfehlungen

```json
{
  "id": "<event-id>",
  "pubkey": "<recommender-pubkey>",
  "created_at": 1736200000,
  "kind": 38000,
  "tags": [
    ["k", "38172"],
    ["d", "<mint-identifier>"],
    ["a", "38172:mint-pubkey:<d-tag>", "wss://relay"]
  ],
  "content": "Ich nutze diesen Mint seit Monaten, sehr zuverlässig",
  "sig": "<signature>"
}
```

Nutzer können Bewertungen im `content`-Feld einschließen und auf bestimmte Mint-Ankündigungs-Events verweisen.

---

**Primäre Quellen:**
- [NIP-87 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Erwähnt in:**
- [Newsletter #4: Releases](/de/newsletters/2026-01-07-newsletter/#releases)

**Siehe auch:**
- [NIP-60: Cashu Wallet](/de/topics/nip-60/)
