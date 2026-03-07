---
title: "Trusted Relay Assertions"
date: 2026-01-21
translationOf: /en/topics/trusted-relay-assertions.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Relays
---

Trusted Relay Assertions beschreibt die Idee, signierte Bewertungen von Relays durch Dritte auf Nostr zu veröffentlichen, damit Clients Relays mit mehr Kontext auswählen können als nur mit selbst gemeldeten Metadaten. Der aktuell standardisierte Baustein dafür ist [NIP-85: Trusted Assertions](/de/topics/nip-85/), das festlegt, wie Nutzer Providern vertrauen und wie Provider signierte berechnete Ergebnisse veröffentlichen.

## Funktionsweise

Relay-Auswahl hat drei Ebenen. [NIP-11: Relay Information Document](/de/topics/nip-11/) beschreibt, was ein Relay über sich selbst sagt. [NIP-66: Relay Discovery and Liveness Monitoring](/de/topics/nip-66/) beschreibt, was Beobachter messen können, etwa Verfügbarkeit und Latenz. Trusted relay assertions versuchen die verbleibende Lücke zu füllen: was ein Dritter aus diesen Daten schließt und ob ein Client dieser Schlussfolgerung vertraut.

Im allgemeineren Modell von NIP-85 benennen Nutzer vertrauenswürdige Provider mit kind-`10040`-Events, und Provider veröffentlichen signierte addressable Assertion-Events. Eine Anwendung, die Relays bewertet, braucht dann noch zwei weitere Dinge, auf die sich Clients einigen: wie ein Relay als bewertetes Objekt identifiziert wird und welche Result-Tags den Score und die zugehörige Evidenz darstellen.

Diese Unterscheidung ist wichtig, weil Transport und Trust-Delegation standardisiert sind, das relay-spezifische Bewertungsmodell aber weiterhin ein Anwendungsmuster bleibt. Verschiedene Provider können sich berechtigterweise darin unterscheiden, was ein Relay vertrauenswürdig macht.

## Trust-Modell

Relay-Vertrauenswertungen sind keine objektiven Fakten. Ein Provider kann Uptime und Schreibdurchsatz priorisieren, ein anderer rechtliche Zuständigkeit, Moderationspolitik oder Betreiberidentität, und ein dritter vor allem Widerstand gegen Überwachung. Ein nützlicher Client sollte zeigen, wer den Score erzeugt hat, nicht nur den Score selbst.

Hier kommt auch [Web of Trust](/de/topics/web-of-trust/) ins Spiel. Wenn ein Client bereits bestimmten Menschen oder Diensten vertraut, kann er Relay-Bewertungen aus genau dieser sozialen Nachbarschaft bevorzugen, statt so zu tun, als gäbe es ein einziges globales Ranking.

## Warum das wichtig ist

Für [NIP-46](/de/topics/nip-46/) Remote Signer, Wallet-Verbindungen oder jede App, die unbekannte Relays vorschlägt, können Bewertungen durch Dritte blinden Trust in Standardwerte reduzieren. In Kombination mit [NIP-65](/de/topics/nip-65/) Relay-Listen können Clients trennen zwischen "welche Relays nutze ich" und "welchen Relays vertraue ich für diese Aufgabe".

Die wichtigste Korrektheitsgrenze ist der Geltungsbereich. Die Newsletter-Berichterstattung aus Januar 2026 beschrieb Relay-Trust-Scoring als eigenen Vorschlag, aber der gemergte Standard im NIPs-Repository ist das allgemeinere Format [NIP-85: Trusted Assertions](/de/topics/nip-85/). Relay-Scoring bleibt ein Anwendungsfall auf diesem Modell, kein eigenes finalisiertes Relay-Trust-Format auf Wire-Ebene.

---

**Primärquellen:**
- [NIP-85 Specification](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [PR #1534: Trusted Assertions](https://github.com/nostr-protocol/nips/pull/1534)

**Erwähnt in:**
- [Newsletter #6: News](/de/newsletters/2026-01-21-newsletter/#trusted-relay-assertions-a-new-approach-to-relay-trust)
- [Newsletter #6: NIP Updates](/de/newsletters/2026-01-21-newsletter/#nip-updates)
- [Newsletter #7: NIP Updates](/de/newsletters/2026-01-28-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-11: Relay Information Document](/de/topics/nip-11/)
- [NIP-66: Relay Discovery and Liveness Monitoring](/de/topics/nip-66/)
- [NIP-85: Trusted Assertions](/de/topics/nip-85/)
- [Web of Trust](/de/topics/web-of-trust/)
