---
title: "Negentropy: Set-Reconciliation-Protokoll"
date: 2026-01-28
translationOf: /en/topics/negentropy.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Sync
---

Negentropy ist ein Set-Reconciliation-Protokoll, mit dem sich feststellen lässt, welche Events auf der einen Seite vorhanden sind und auf der anderen fehlen, ohne den vollständigen Datensatz erneut zu senden.

## Wie es funktioniert

Anstatt jedes Event anzufordern, das zu einem Filter passt, vergleicht negentropy zwei sortierte Mengen und arbeitet sich nur zu den Bereichen vor, die sich unterscheiden. Das Protokoll tauscht kompakte Bereichszusammenfassungen aus und fällt nur dort auf explizite Listen von IDs zurück, wo es nötig ist.

1. **Ordnung**: Beide Seiten sortieren Einträge nach Zeitstempel und dann nach ID
2. **Bereichsvergleich**: Sie tauschen Fingerprints für Bereiche von Einträgen aus
3. **Verfeinerung**: Bereiche mit Abweichungen werden weiter aufgeteilt, bis die tatsächlich fehlenden IDs feststehen

## Warum es wichtig ist

Die klassische Nostr-Synchronisierung verwendet zeitstempelbasierte `since`-Filter. Dabei können Events verloren gehen durch:
- Uhrendrift zwischen Client und Relay
- Mehrere Events mit identischen Zeitstempeln
- Events, die in anderer Reihenfolge eintreffen

Negentropy löst diese Probleme, indem es die tatsächlichen Event-Mengen vergleicht, statt sich auf Zeitstempel zu verlassen.

## Praktischer Einsatz

- **DM-Wiederherstellung**: Clients können fehlende Direktnachrichten erkennen und nachladen, auch bei alten Zeitstempeln
- **Feed-Sync**: Sorgt für vollständige Timeline-Synchronisierung über mehrere Relays hinweg
- **Offline-Sync**: Holt nach Unterbrechungen effizient auf

Das wichtige Implementierungsdetail ist, dass viele Clients normale Subscriptions nicht durch negentropy ersetzen. Sie verwenden es als Reparaturpfad. Damus etwa behielt das normale Laden von DMs bei und fügte negentropy für manuelle Aktualisierungen hinzu, um Nachrichten wiederherzustellen, die der normale Ablauf verpasst.

## Abwägungen

Negentropy erfordert Unterstützung auf beiden Seiten und erhöht die Protokollkomplexität gegenüber normalem `REQ`-Einsatz. Es ist besonders dort hilfreich, wo Korrektheit wichtiger ist als ein minimaler Implementierungsaufwand.

In gemischten Umgebungen brauchen Clients weiterhin ein sauberes Fallback-Verhalten, weil nicht jedes Relay das Protokoll unterstutzt.

---

**Primärquellen:**
- [Negentropy Protocol Repository](https://github.com/hoytech/negentropy)
- [Damus PR #3536](https://github.com/damus-io/damus/pull/3536)
- [Damus PR #3547](https://github.com/damus-io/damus/pull/3547)

**Erwähnt in:**
- [Newsletter #6: Damus ships negentropy for reliable DM syncing](/en/newsletters/2026-01-28-newsletter/#damus-ships-negentropy-for-reliable-dm-syncing)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**Siehe auch:**
- [NIP-01: Basisprotokoll](/de/topics/nip-01/)
