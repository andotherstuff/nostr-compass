---
title: "NIP-A4: Öffentliche Nachrichten"
date: 2025-12-24
translationOf: /en/topics/nip-a4.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Social
---

NIP-A4 definiert öffentliche Nachrichten vom kind 24, die für Benachrichtigungsoberflächen gedacht sind und breite Client-Unterstützung anstreben.

## Funktionsweise

Kind `24` ist eine signierte Klartextnachricht an einen oder mehrere Empfänger. Der Nachrichtentext steht in `content`, und `p`-Tags identifizieren die vorgesehenen Empfänger. Die Spezifikation sagt, dass Clients diese Events an die Inbox-Relays der Empfänger aus [NIP-65](/de/topics/nip-65/) und an das Outbox-Relay des Senders senden sollten.

Im Unterschied zu Thread-Konversationen haben diese Nachrichten kein Konzept von Chat-Verlauf, Room-State oder Thread-Wurzeln. Sie sollen auf einer Benachrichtigungsfläche erscheinen und für sich allein verständlich sein.

## Protokollregeln

- Verwendet `p`-Tags zur Identifikation der Empfänger
- Darf keine `e`-Tags für Threading verwenden
- Kann `q`-Tags verwenden, um ein anderes Event zu zitieren
- Funktioniert am besten mit Expiration-Tags aus [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md), damit alte Benachrichtigungsnachrichten mit der Zeit verschwinden

## Warum es existiert

NIP-A4 gibt Clients ein einfacheres Primitive für öffentliche Nachrichten als eine vollständige Thread-Note. Das ist nützlich für nachrichtenartige Erwähnungen, leichte Shoutouts oder einmalige Benachrichtigungen, bei denen ein dauerhaftes Gesprächsbaum-Modell mehr Komplexität als Nutzen bringen würde.

Die Kehrseite ist, dass diese Nachrichten öffentlich sind. Gerade weil sie keinen privaten Session-State erzeugen, lassen sie sich leicht in einer Benachrichtigungs-UI anzeigen. Jeder kann sie lesen und beantworten, wenn er sie sieht.

## Interop-Hinweise

NIP-A4 lässt sich leicht mit Direct-Message-Protokollen verwechseln, weil es benannte Empfänger anspricht, bleibt aber ein öffentlicher Event-Kind. Clients sollten kind `24` weder als private Nachricht darstellen noch irgendeine Vertraulichkeit annehmen, die über die Platzierung auf Relays hinausgeht.

---

**Primärquellen:**
- [NIP-A4 Specification](https://github.com/nostr-protocol/nips/blob/master/A4.md)
- [NIP-A4 PR](https://github.com/nostr-protocol/nips/pull/1988)

**Erwähnt in:**
- [Newsletter #2: NIP Updates](/de/newsletters/2025-12-24-newsletter/#nip-updates)
- [Newsletter #3: December Recap](/de/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Siehe auch:**
- [NIP-01: Basic Protocol](/de/topics/nip-01/)
- [NIP-10: Text Note Threading](/de/topics/nip-10/)
