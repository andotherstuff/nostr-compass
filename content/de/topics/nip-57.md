---
title: "NIP-57: Zaps"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57 definiert Zaps, also eine Moglichkeit, Lightning-Zahlungen an Nostr-Identitaten und Inhalte zu hangen. Standardisiert werden sowohl die Anfrage nach einer zap-fahigen Rechnung als auch das Quittungs-Event, das Wallets nach der Zahlung veroffentlichen.

## Wie es funktioniert

1. Der Client entdeckt den LNURL-Endpunkt des Empfangers in den Profil-Metadaten oder in einem `zap`-Tag auf dem Zielevent.
2. Der Client sendet eine signierte Zap-Anfrage vom Kind `9734` an den LNURL-Callback des Empfangers, nicht an Relays.
3. Der Nutzer bezahlt die Rechnung.
4. Der Wallet-Server des Empfangers veroffentlicht eine Zap-Quittung vom Kind `9735` an die in der Zap-Anfrage aufgefuhrten Relays.
5. Clients validieren und zeigen den Zap an.

## Zap-Anfrage (kind 9734)

Die Zap-Anfrage ist ein signiertes Event, das den Zahler und das beabsichtigte Ziel identifiziert. Sie enthalt meistens:

- `p`-Tag mit dem Pubkey des Empfangers
- `e`-Tag mit dem gezappten Event (optional)
- `amount`-Tag in Millisatoshis
- `relays`-Tag mit der Liste der Orte, an denen die Quittung veroffentlicht werden soll

Adressierbare Inhalte konnen ein `a`-Tag statt eines `e`-Tags oder zusatzlich dazu verwenden. Das optionale `k`-Tag zeichnet das Ziel-Kind auf.

## Zap-Quittung (kind 9735)

Sie wird nach Bestatigung der Zahlung vom Wallet-Server des Empfangers veroffentlicht. Sie enthalt:

- Die ursprungliche Zap-Anfrage in einem `description`-Tag
- `bolt11`-Tag mit der bezahlten Rechnung
- `preimage`-Tag als Nachweis der Zahlung

Clients sollten die Quittung gegen den `nostrPubkey` der LNURL des Empfangers, den Rechnungsbetrag und die ursprungliche Zap-Anfrage validieren. Ohne diese Validierung ist eine Quittung nur eine Behauptung.

## Vertrauen und Tradeoffs

Zaps sind nutzlich, weil sie Zahlungen im sozialen Graph sichtbar machen, aber die Quittung wird weiterhin von der Wallet-Infrastruktur des Empfangers erzeugt. Die Spezifikation selbst weist darauf hin, dass eine Zap-Quittung kein universeller Zahlungsnachweis ist. Am besten versteht man sie als von einer Wallet signierte Aussage, dass eine Rechnung, die an eine Zap-Anfrage gebunden war, bezahlt wurde.

---

**Primarquellen:**
- [NIP-57 Specification](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Erwahnt in:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #2: News](/en/newsletters/2025-12-24-newsletter/#news)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/#amethyst-android)
- [Newsletter #9: NIP Updates](/en/newsletters/2026-02-11-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-47: Nostr Wallet Connect](/de/topics/nip-47/)
