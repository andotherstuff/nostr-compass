---
title: "NIP-61: Nutzaps"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-61.md
translationDate: 2026-07-01
categories:
  - Zaps
  - Ecash
---

NIP-61 definiert "nutzaps", Peer-to-Peer-Cashu-Ecash-Zahlungen, die als Nostr-events zugestellt werden. Ein Absender veröffentlicht ein P2PK-gesperrtes Cashu-Token, das an den Nostr-Schlüssel des Empfängers adressiert ist, und der Empfänger löst es zu einem für ihn passenden Zeitpunkt bei der Mint ein. Die proofs selbst tragen den Wert, sodass eine NIP-61-Zahlung als in sich geschlossenes Token ankommt, das der Empfänger nach eigenem Zeitplan einlösen kann, ohne dass ein Lightning-Kanal oder ein interaktiver Handshake erforderlich ist.

## Wie es funktioniert

NIP-61 baut auf zwei bestehenden Primitiven auf: [NIP-60](/de/topics/nip-60/) Cashu-Wallets und Cashus P2PK-Sperren. Der Ablauf verwendet drei event-kinds.

**Mint-Empfehlung (kind 10019):** ein ersetzbares event, das der Empfänger veröffentlicht, um bekannt zu geben, von welchen Mints er nutzaps akzeptiert und welcher öffentliche Cashu-Schlüssel zum Sperren der proofs für ihn verwendet wird. Absender lesen dies vor dem Senden, damit das gesperrte Token eines ist, das der Empfänger einlösen kann.

**Nutzap-event (kind 9321):** die Zahlung selbst. Sie enthält die Cashu-proofs (P2PK-gesperrt an den nutzap-pubkey des Empfängers aus kind 10019), die Mint-URL, optionale `e`- und `a`-tags, die die gezappte Notiz identifizieren, und ein `p`-tag für den Empfänger. Der Empfänger erhält sie über normale Nostr-Abonnements, entsperrt die proofs mit dem entsprechenden privaten Schlüssel und behält sie entweder in seiner NIP-60-Wallet oder wandelt sie in Lightning um.

**Nutzap-Info (kind 7375):** zwischengespeicherter Zustand mit derselben Form wie NIP-60-Token-events, der eingelöste nutzap-proofs aufzeichnet, damit die Wallet sie beim erneuten Synchronisieren nicht doppelt zählt.

## Kompromisse und Vertrauensmodell

Ein nutzap ist ein in sich geschlossenes Ecash-Token. Solange der Empfänger die Mint später kontaktieren kann, kann er die Zahlung einlösen. Die Mint selbst ist der vertrauenswürdige Verwahrer, das gleiche Vertrauensmodell wie bei NIP-60, und diese Verwahrungsentscheidung ist der ausdrückliche Preis für offline-fähige Mikrozahlungen mit sofortiger Endgültigkeit. NIP-57-zaps erfordern, dass der Empfänger einen Lightning-Node mit einem LNURL-Endpunkt betreibt (oder auf einem solchen gehostet wird), der eingehende HTLCs in Echtzeit akzeptiert. Telefone ohne Lightning-Kanal, Nutzer hinter Firewalls und Empfänger, die zufällig offline sind, liegen alle außerhalb dieses Modells.

Die kind 10019-Ankündigung ist das soziale Vertrauensgate. Der Absender wählt eine der vom Empfänger akzeptierten Mints, was den Einlösungsweg des Empfängers vorhersehbar hält. Ein Absender, der eine Mint außerhalb der Menge des Empfängers wählt, riskiert ein nicht einlösbares Token, weshalb Wallets zuerst kind 10019 lesen.

## Ablauf

1. Empfänger veröffentlicht ein kind 10019, das akzeptierte Mints und einen nutzap-pubkey ankündigt
2. Absender liest kind 10019, prägt proofs bei einer der aufgelisteten Mints und sperrt sie per P2PK an den nutzap-pubkey des Empfängers
3. Absender veröffentlicht ein kind 9321 mit den gesperrten proofs, der Mint-URL und den Ziel-tags
4. Empfänger erhält das kind 9321 über sein normales Nostr-Abonnement
5. Empfänger entsperrt die proofs mit seinem privaten nutzap-Schlüssel und behält sie entweder in seiner NIP-60-Wallet oder wandelt sie in Lightning um

## Beispiel für ein nutzap-event

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1750162800,
  "kind": 9321,
  "tags": [
    ["proof", "{\"amount\":21,\"secret\":\"...\",\"C\":\"...\",\"id\":\"...\"}"],
    ["u", "https://mint.example.com"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3"],
    ["p", "c5d8a4e3b2a1f0e9d8c7b6a5949382716050403020100ffeeddccbbaa99887766"]
  ],
  "content": "Great post!",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

## Implementierungen

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) liefert nutzap-Rendering mit Guthabenansichten pro Mint als Teil seiner NIP-60/NIP-61-Wallet-Oberfläche ([PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075))

---

**Primärquellen:**
- [NIP-61-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/61.md)
- [Amethyst PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075) - NIP-60-Cashu-Wallet- und NIP-61-nutzap-Unterstützung

**Erwähnt in:**
- [Newsletter #27: Amethyst v1.12.0 liefert Cashu-Wallets, nutzaps, einen CLINK-Treiber und Tor-Selbstheilung](/de/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**Siehe auch:**
- [NIP-57: Zaps](/de/topics/nip-57/)
- [NIP-60: Cashu Wallet](/de/topics/nip-60/)
- [Cashu](/de/topics/cashu/)
