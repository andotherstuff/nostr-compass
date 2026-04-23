---
title: "NIP-57: Zaps"
date: 2025-12-17
translationOf: /en/topics/nip-57.md
translationDate: 2026-04-22
draft: false
categories:
  - Wallet
  - Lightning
  - Social
---

NIP-57 definiert zaps, also eine Möglichkeit, Lightning-Zahlungen an Nostr-Identitäten und Inhalte zu hängen. Standardisiert werden sowohl die Anfrage nach einer zap-fähigen Invoice als auch das Receipt-Event, das Wallets nach der Zahlung veröffentlichen.

## Funktionsweise

1. Der Client entdeckt den LNURL-Endpunkt des Empfängers in den Profil-Metadaten oder in einem `zap`-Tag auf dem Ziel-Event.
2. Der Client sendet einen signierten kind-`9734`-Zap-Request an den LNURL-Callback des Empfängers, nicht an Relays.
3. Der Nutzer bezahlt die Invoice.
4. Der Wallet-Server des Empfängers veröffentlicht ein kind-`9735`-Zap-Receipt an die im Zap-Request aufgeführten Relays.
5. Clients validieren und zeigen den zap an.

## Zap Request (kind 9734)

Der Zap-Request ist ein signiertes Event, das den Zahler und das beabsichtigte Ziel identifiziert. Er enthält normalerweise:

- `p`-Tag mit dem pubkey des Empfängers
- `e`-Tag mit dem gezappten Event, optional
- `amount`-Tag in millisatoshis
- `relays`-Tag mit der Liste der Relays, auf denen das Receipt veröffentlicht werden soll

Addressable Content kann statt eines `e`-Tags oder zusätzlich dazu ein `a`-Tag verwenden. Das optionale `k`-Tag zeichnet den Ziel-kind auf.

## Zap Receipt (kind 9735)

Es wird nach Bestätigung der Zahlung vom Wallet-Server des Empfängers veröffentlicht. Es enthält:

- den ursprünglichen Zap-Request in einem `description`-Tag
- ein `bolt11`-Tag mit der bezahlten Invoice
- ein `preimage`-Tag als Zahlungsnachweis

Clients sollten das Receipt gegen den LNURL-`nostrPubkey` des Empfängers, den Betrag der Invoice und den ursprünglichen Zap-Request validieren. Ein Receipt ohne diese Validierung ist nur eine Behauptung.

## Vertrauen und Tradeoffs

Zaps sind nützlich, weil sie Zahlungen im Social Graph sichtbar machen, aber das Receipt wird weiterhin von der Wallet-Infrastruktur des Empfängers erzeugt. Die Spezifikation selbst weist darauf hin, dass ein Zap-Receipt kein universeller Zahlungsnachweis ist. Am besten versteht man es als wallet-signierte Aussage, dass eine Invoice bezahlt wurde, die an einen Zap-Request gebunden war.

Ein validierender Client sollte vier Dinge prüfen, bevor er ein Receipt als zap anzeigt: Die Signatur des Receipts muss zum `nostrPubkey` aus der LNURL-Antwort des Empfängers passen, der `bolt11`-Betrag muss zum `amount`-Tag im eingebetteten Zap-Request passen, der Description-Hash der Invoice muss an den stringifizierten Zap-Request gebunden sein, und das `preimage` muss auf den `payment_hash` der Invoice hashen. Clients, die aufaddierte Zap-Zahlen ohne diese Prüfungen rendern, sind trivial durch gefälschte kind-`9735`-Events spoofbar.

## Private and Anonymous Zaps

Private zaps ergänzen eine Vertraulichkeitsschicht. Ein Sender kann `content` des Zap-Requests für den Empfänger verschlüsseln und ein `anon`-Tag im äußeren Request setzen, sodass das Relay-Netzwerk zwar das Zahlungsziel sieht, aber die beigefügte Notiz nicht lesen kann. Ein anonymer zap geht noch einen Schritt weiter: Der Client erzeugt für den Zap-Request selbst ein frisches ephemeres Keypair, sodass das Receipt zwar weiterhin beweist, dass eine Zahlung stattgefunden hat, der Empfänger sie aber nicht mehr mit dem langlebigen pubkey des Senders verknüpfen kann.

## Zap Goals and Splits

NIP-57 bildet die Grundlage des in [NIP-75](/de/topics/nip-75/) spezifizierten Zap-Goal-Systems. Ein Goal ist ein kind-`9041`-Event, das einen Zielbetrag und einen Relay-Satz deklariert, auf dem Receipts zählen. Clients berechnen den Fortschritt, indem sie validierte `bolt11`-Beträge passender kind-`9735`-Events aufsummieren.

Zap Splits, die in einem Anhang zum NIP definiert sind, erlauben es einem Empfänger, ein kind-`0`-Profil mit mehreren gewichteten `zap`-Tags zu veröffentlichen, sodass eine einzelne Zap-Zahlung atomar auf mehrere pubkeys verteilt wird. [Amethyst](https://github.com/vitorpamplona/amethyst), [Damus](https://github.com/damus-io/damus) und [noStrudel](https://github.com/hzrd149/nostrudel) implementieren Split-Paying End-to-End.

---

**Primärquellen:**
- [NIP-57 Specification](https://github.com/nostr-protocol/nips/blob/master/57.md)

**Erwähnt in:**
- [Newsletter #1: News](/de/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: News](/de/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: Notable Code Changes](/de/newsletters/2025-12-31-newsletter/)
- [Newsletter #9: NIP Updates](/de/newsletters/2026-02-11-newsletter/)
- [Newsletter #19: NIP Deep Dive](/en/newsletters/2026-04-22-newsletter/)

**Siehe auch:**
- [NIP-47: Nostr Wallet Connect](/de/topics/nip-47/)
- [NIP-75: Zap Goals](/de/topics/nip-75/)
- [NIP-53: Live Activities](/de/topics/nip-53/)
