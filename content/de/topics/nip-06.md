---
title: "NIP-06: Schlüsselableitung aus einer Mnemonic"
date: 2026-10-28
translationOf: /en/topics/nip-06.md
translationDate: 2026-10-28
draft: false
categories: ["Identity", "Keys"]
---

NIP-06 beschreibt, wie man ein Nostr-Schlüsselpaar aus einer mnemonischen Seed-Phrase ableitet. Der [aktuelle offizielle NIP-06-Text](https://github.com/nostr-protocol/nips/blob/master/06.md) ist als Entwurf und optional gekennzeichnet und enthält diese Warnung:

> __Warnung__ `unrecommended`: einen einzelnen nsec bevorzugen

Diese Seite behandelt NIP-06 aus Gründen der historischen Kompatibilität. Sie empfiehlt nicht, die Seed-Ableitung einzuführen.

## Funktionsweise

Laut der [aktuellen Spezifikation](https://github.com/nostr-protocol/nips/blob/master/06.md) wird BIP39 verwendet, um die mnemonischen Wörter zu erzeugen und daraus einen binären Seed abzuleiten. Anschließend leitet BIP32 Schlüssel entlang des Pfads `m/44'/1237'/<account>'/0/0` ab, wobei 1237 der Nostr-Eintrag in SLIP44 ist. Ein einfacher Client kann Account 0 verwenden. Durch Erhöhen des Account-Werts ergeben sich weitere Schlüssel aus demselben Seed. Zwei Implementierungen reproduzieren nur dann dieselbe Identität, wenn sie bei den Ableitungsschritten übereinstimmen und für das Ergebnis die korrekten Kodierungen verwenden.

## Testvektoren

Ein [Commit vom 12. Oktober 2023](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b) fügte zwei Testvektoren hinzu, einen auf Basis einer Mnemonic mit 12 Wörtern und einen auf Basis einer Mnemonic mit 24 Wörtern. Jeder führt den erwarteten privaten und öffentlichen Schlüssel in Hex auf, zusammen mit den passenden nsec- und npub-Kodierungen. Entwickler können die Vektoren nutzen, um Implementierungen gegeneinander zu prüfen. Die Vektoren sagen nichts über die Schlüsselverwahrung aus, bescheinigen keine Sicherheit und garantieren keine universelle Interoperabilität.

## Siehe auch

- [NIP-01](/de/topics/nip-01/)

**Primärquellen:**

- [NIP-06 (aktuell)](https://github.com/nostr-protocol/nips/blob/master/06.md)
- [Commit, der NIP-06-Testvektoren hinzufügt (12. Oktober 2023)](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b)

**Erwähnt in:**

- [Newsletter #46](/de/newsletters/2026-10-28-newsletter/#october-2023-events-carry-evidence-and-requests-for-work)
