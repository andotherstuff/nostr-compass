---
title: "NIP-66: Relay-Entdeckung und Liveness-Monitoring"
date: 2026-01-21
translationOf: /en/topics/nip-66.md
translationDate: 2026-03-11
draft: false
categories:
  - NIPs
  - Relays
---

NIP-66 standardisiert die Veröffentlichung von Relay-Monitoring-Daten auf Nostr. Monitor-Dienste testen Relays fortlaufend auf Verfügbarkeit, Latenz, Protokollkonformität und unterstützte NIPs und veröffentlichen die Ergebnisse als kind-30166-Events.

## Funktionsweise

Monitore prüfen die Verfügbarkeit eines Relays, indem sie sich verbinden und Test-Subscriptions senden. Latenzmessungen erfassen Verbindungszeit, Antwortzeit auf Subscriptions und die Verzögerung bei der Event-Weitergabe. Protokollkonformitätstests prüfen, ob das Verhalten eines Relays den Spezifikationen entspricht, und erkennen Implementierungsfehler oder absichtliche Abweichungen.

Die Prüfung der NIP-Unterstützung geht über Behauptungen in [NIP-11](/de/topics/nip-11/) hinaus, weil tatsächlich getestet wird, ob beworbene Funktionen korrekt arbeiten. Wenn ein Relay etwa Unterstützung für [NIP-50](/de/topics/nip-50/) behauptet, Suchanfragen aber fehlschlagen, wird NIP-50 nicht in der verifizierten Liste erscheinen. Das liefert eine belastbare Aussage über die Fähigkeiten eines Relays.

Kind-30166-Events verwenden die Relay-URL als `d`-Tag und sind damit parameterized replaceable events. Jeder Monitor veröffentlicht pro Relay ein Event, das aktualisiert wird, wenn sich die Messwerte ändern. Mehrere Monitore können dasselbe Relay beobachten und so Redundanz und Quervergleich liefern.

Round-trip-time-Tags (`rtt`) messen die Latenz verschiedener Operationen:
- `rtt open`: Aufbau der WebSocket-Verbindung
- `rtt read`: Antwortzeit auf eine Subscription
- `rtt write`: Geschwindigkeit beim Veröffentlichen eines Events

Alle Werte sind in Millisekunden angegeben. Clients können diese Metriken nutzen, um für zeitkritische Vorgänge Relays mit niedriger Latenz zu bevorzugen.

Geografische Informationen helfen Clients, nahe Relays für bessere Latenz und Zensurresistenz auszuwählen. Das `geo`-Tag enthält Ländercode, Ländernamen und Region. Das `network`-Tag unterscheidet Clearnet-Relays von Tor Hidden Services oder I2P-Endpunkten.

## Warum das wichtig ist

NIP-66 macht Relay-Qualität von Anekdoten zu maschinenlesbaren Daten. Ein Client muss sich nicht nur auf das eigene [NIP-11](/de/topics/nip-11/)-Dokument eines Relays oder eine hartcodierte Allowlist verlassen. Er kann gemessene Uptime, gemessene Latenz und getestete Feature-Unterstützung von einem oder mehreren Monitoren vergleichen.

Das ist besonders wichtig für die Relay-Auswahl im Outbox Model. Wenn Clients sich dynamisch mit vielen Relays verbinden, führen tote oder falsch konfigurierte Relays direkt zu langsameren Feeds und mehr fehlgeschlagenen Abrufen.

## Anwendungsfälle

Monitoring-Daten speisen Relay-Selektoren in Clients, Explorer-Websites und Trust-Bewertungssystemen. Weil NIP-66 Relay-Status in Echtzeit unabhängig von Selbstaussagen eines Relays bereitstellt, wird fundierte Relay-Auswahl möglich.

Zusammen mit [NIP-11](/de/topics/nip-11/) für selbst gemeldete Fähigkeiten und [Trusted Relay Assertions](/de/topics/trusted-relay-assertions/) für Trust-Bewertungen bewegt sich das Ökosystem hin zu datengetriebener Relay-Auswahl statt zu hartcodierten Standards.

## Trust-Modell

NIP-66 schafft keinen einzelnen autoritativen Monitor. Mehrere Monitore können Ergebnisse für dasselbe Relay veröffentlichen, und Clients können sie vergleichen. Dieses Design reduziert die Abhängigkeit von der Einschätzung eines einzelnen Betreibers, bedeutet aber auch, dass Clients Regeln brauchen, welchem Monitor sie bei widersprüchlichen Ergebnissen vertrauen.

---

**Primärquellen:**
- [NIP-66 Specification](https://github.com/nostr-protocol/nips/blob/master/66.md) - Relay discovery and liveness monitoring standard

**Erwähnt in:**
- [Newsletter #6: NIP Deep Dive](/de/newsletters/2026-01-21-newsletter/#nip-deep-dive-nip-11-and-nip-66)

**Siehe auch:**
- [NIP-11: Relay Information Document](/de/topics/nip-11/)
- [NIP-65: Relay List Metadata](/de/topics/nip-65/)
- [Trusted Relay Assertions](/de/topics/trusted-relay-assertions/)
