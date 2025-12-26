---
title: "NIP-17: Private Direktnachrichten"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-17 definiert private Direktnachrichten unter Verwendung von NIP-59 Gift Wrapping für Absender-Privatsphäre. Im Gegensatz zu NIP-04-DMs, die den Absender offenlegen, verbergen NIP-17-Nachrichten, wer die Nachricht gesendet hat. Der Empfänger bleibt in der äußeren Gift-Wrap-Hülle sichtbar.

## Funktionsweise

Nachrichten werden in mehrere Verschlüsselungsschichten eingewickelt:
1. Der eigentliche Nachrichteninhalt (Kind 14)
2. Ein Siegel, das den Inhalt für den Empfänger verschlüsselt
3. Eine Gift-Wrap-Hülle, die die Identität des Absenders verbirgt

Die äußere Gift-Wrap-Hülle verwendet ein zufälliges Einweg-Schlüsselpaar, sodass Relays und Beobachter nicht bestimmen können, wer die Nachricht gesendet hat.

## Nachrichtenstruktur

- **Kind 14** - Der eigentliche DM-Inhalt (innerhalb des Siegels)
- Verwendet NIP-44-Verschlüsselung für den Inhalt
- Unterstützt Reaktionen (Kind 7) innerhalb von DM-Konversationen

## Privatsphäre-Garantien

- Relays können den Absender nicht sehen (verborgen durch das Einweg-Schlüsselpaar der Gift-Wrap-Hülle)
- Der Empfänger ist sichtbar (im `p`-Tag der Gift-Wrap-Hülle)
- Nachrichtenzeitstempel werden innerhalb eines Fensters randomisiert
- Kein sichtbares Threading oder Konversationsgruppierung auf dem Relay

## Vergleich zu NIP-04

NIP-04-DMs verschlüsseln den Inhalt, lassen aber Metadaten sichtbar:
- Der Absender-Pubkey ist öffentlich
- Der Empfänger-Pubkey ist im `p`-Tag
- Zeitstempel sind exakt

NIP-17 verbirgt den Absender auf Kosten einer komplexeren Implementierung.

---

**Primärquellen:**
- [NIP-17 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/17.md)

**Erwähnt in:**
- [Newsletter #1: NIP-Updates](/de/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #2: Neuigkeiten](/de/newsletters/2025-12-24-newsletter/#news)

**Siehe auch:**
- [NIP-59: Gift Wrap](/de/topics/nip-59/)
