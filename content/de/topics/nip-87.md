---
title: "NIP-87: Ecash Mint Discoverability"
date: 2026-01-07
translationOf: /en/topics/nip-87.md
translationDate: 2026-03-07
draft: false
categories:
  - Ecash
  - Discovery
  - Protocol
---

NIP-87 definiert, wie ecash-Mints wie Cashu und Fedimint sich auf Nostr ankündigen können und wie Nutzer Mints anderen empfehlen.

## Event-Kinds

- **kind 38172** - Cashu-Mint-Ankündigung, veröffentlicht von Mint-Betreibern
- **kind 38173** - Fedimint-Ankündigung, veröffentlicht von Mint-Betreibern
- **kind 38000** - Mint-Empfehlung, veröffentlicht von Nutzern

## Funktionsweise

1. **Mint-Betreiber** veröffentlichen die URL ihres Mints, unterstützte Features und das Netzwerk, etwa mainnet oder testnet
2. **Nutzer**, die einem Mint vertrauen, veröffentlichen Empfehlungen mit optionalen Reviews
3. **Andere Nutzer** fragen Empfehlungen von Accounts ab, denen sie folgen, um vertrauenswürdige Mints zu finden

## Cashu-Mint-Ankündigung

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

Das `nuts`-Tag listet unterstützte NUTs auf, also die Notation-, Usage- und Terminology-Spezifikationen von Cashu.

Das `d`-Tag sollte der Cashu-Pubkey des Mints sein. So erhalten Clients einen stabilen Bezeichner für die Auffindung, selbst wenn das Mint später Metadaten ändert oder seine Ankündigung neu veröffentlicht.

## Empfehlungen von Nutzern

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
  "content": "I've used this mint for months, very reliable",
  "sig": "<signature>"
}
```

Nutzer können Reviews im `content`-Feld hinterlegen und auf konkrete Mint-Ankündigungs-Events verweisen.

Empfehlungs-Events sind parameterized replaceable events. Das ist nützlich, weil ein Nutzer seine Empfehlung später überarbeiten, den Review-Text ändern oder die Unterstützung für ein Mint zurückziehen kann, ohne mehrere veraltete Empfehlungs-Events stehen zu lassen.

## Trust-Modell

NIP-87 sagt Clients nicht, welches Mint sicher ist. Es gibt ihnen nur eine Möglichkeit, von Betreibern veröffentlichte Metadaten mit sozialen Empfehlungen von Accounts zu kombinieren, denen der Nutzer bereits vertraut.

Diese Unterscheidung ist wichtig, weil direkte Abfragen nach Mint-Ankündigungen verrauscht oder bösartig sein können. Die Spezifikation warnt Clients ausdrücklich davor, ohne Spam-Schutz oder hochwertige Relays soziale Empfehlungen zu umgehen und Ankündigungen direkt abzufragen.

## Interop-Hinweise

Cashu und Fedimint nutzen unterschiedliche Ankündigungs-Kinds, weil sie verschiedene Verbindungsdetails veröffentlichen. Cashu-Ankündigungen enthalten Mint-URLs und unterstützte NUTs, während Fedimint-Ankündigungen Invite-Codes und unterstützte Federation-Module enthalten. Eine Wallet, die beides unterstützt, muss deshalb beide Formate verstehen.

---

**Primärquellen:**
- [NIP-87 Specification](https://github.com/nostr-protocol/nips/blob/master/87.md)

**Erwähnt in:**
- [Newsletter #4: Releases](/de/newsletters/2026-01-07-newsletter/#releases)
- [Newsletter #7: Zeus](/de/newsletters/2026-01-28-newsletter/)

**Siehe auch:**
- [Cashu](/de/topics/cashu/)
- [NIP-60: Cashu Wallet](/de/topics/nip-60/)
