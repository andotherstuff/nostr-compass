---
title: "NIP-31: Umgang mit unbekannten Event-Kinds"
date: 2026-11-04
draft: false
categories:
  - NIPs
  - Protocol
translationOf: /en/topics/nip-31.md
translationDate: 2026-11-05
---

> **Statushinweis:** Die aktuelle [NIP-31-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/31.md) stuft sich selbst als `unrecommended` ein, da sie „unnötig aufgebläht“ sei, und ihre Statuszeile lautet draft, unrecommended und optional. Relays speichern bereits Events, die diese Konvention nutzen. Deshalb erklärt diese Seite, wie Clients sie lesen. Sie empfiehlt NIP-31 nicht für neue Protokolle.

NIP-31 definiert einen `alt`-Tag auf oberster Ebene. Der Tag enthält eine kurze Klartext-Zusammenfassung für benutzerdefinierte Event-Kinds, die nicht als gewöhnliche Textnotizen gelesen werden sollen.

## Funktionsweise {#how-it-works}

Die Autorin oder der Autor eines Events mit benutzerdefiniertem Kind fügt einen `alt`-Tag mit einer für Menschen lesbaren Beschriftung hinzu. Clients, die auf Kind 1 ausgerichtet sind, müssen nicht jedes Kind abonnieren, das sie nicht kennen. Ihre Nutzer können trotzdem auf ein solches Event stoßen, wenn eine Notiz darauf verweist. Die Beschriftung liefert dann etwas Kontext, obwohl der Client dieses Kind nicht implementiert.

Tag-Fragment, kein vollständiges Event:

```
["alt", "<short plaintext summary>"]
```

Eine lesbare Beschriftung betrifft nur die Anzeige. Sie kann keine Stimme abgeben, keine Wallet-Anfrage ausführen und keine andere native Aktion des Kinds durchführen. Für eine umfassendere Interaktion verweist die Spezifikation auf [NIP-89: Recommended Application Handlers](/de/topics/nip-89/).

## Implementierungen {#implementations}

In der [Karte für unbekannte Events von noStrudel bei Commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx) wird der erste `alt`-Tag getrimmt und dient als Hauptbeschriftung, optional ergänzt um eine Zeile `Using <client>`. Ein fehlender oder leerer Wert ergibt `Unknown event (kind ...)`, und bis zu drei Zeilen des Inhalts erscheinen separat. Dieselbe Komponente löst den `client`-Tag über NIP-89-Handler-Vorlagen auf. Sie zeigt eine Schaltfläche zum Öffnen, wenn eine teilbare Adresse existiert, und `Open in <client>`, wenn sich ein gültiger Handler-Link auflösen lässt. Die Erklärung und die Weiterleitung an die App sind getrennte Bedienelemente.

Amethysts [UnknownEventDigest.kt bei Commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170) bevorzugt Inhalt, den es als Fließtext einstuft, und greift ersatzweise auf `alt` zurück. Sein Parser trimmt die Werte und nimmt das erste nicht leere `alt`. Daher kann ein Event, dessen erstes `alt` leer ist, hier eine andere Beschriftung erhalten als in noStrudel. Beide Beschreibungen geben den Quellcode bei diesen Commits wieder. Keine bestätigt, wie sich eine veröffentlichte Version verhält.

## Grenzen {#limits}

- `alt` ist ein Tag, daher decken die in [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) definierte Event-ID und Signatur ihn ab. Eine gültige Signatur zeigt, dass der Autor die Beschriftung veröffentlicht hat. Sie zeigt nicht, dass die Beschriftung zutrifft, sodass eine Zusammenfassung irreführend sein kann.
- Tags sind öffentlich. Ein `alt` an einem Event mit verschlüsseltem Inhalt legt seine Zusammenfassung offen und kann verraten, was der Inhalt verbirgt.
- Beide oben genannten Eigenschaften ergeben sich aus dem Event-Umschlag von NIP-01. Der Text von NIP-31 selbst formuliert sie nicht als Anforderungen.
- Ein `alt`-Tag auf oberster Ebene unterscheidet sich vom Bildbeschreibungsfeld `alt` innerhalb von `imeta`, und Renderer parsen beide getrennt.

---

**Primärquellen:**
- [NIP-31-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/31.md)
- [noStrudel embedded-unknown.tsx bei Commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx)
- [Amethyst UnknownEventDigest.kt bei Commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt)

**Erwähnt in:**
- [Nostr Compass #47: NIP im Detail](/de/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)

**Siehe auch:**
- [NIP-89: Empfohlene Anwendungs-Handler](/de/topics/nip-89/)
- [NIP-73: Externe Inhalts-IDs](/de/topics/nip-73/)
- [NIP-01: Beschreibung des grundlegenden Protokollablaufs](/de/topics/nip-01/)
