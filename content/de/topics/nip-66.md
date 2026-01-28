---
title: "NIP-66: Relay-Entdeckung und Liveness-Monitoring"
date: 2026-01-21
translationOf: /en/topics/nip-66.md
translationDate: 2026-01-28
draft: false
categories:
  - NIPs
  - Relays
---

NIP-66 standardisiert die Veröffentlichung von Relay-Monitoring-Daten auf Nostr. Monitor-Dienste testen Relays kontinuierlich auf Verfügbarkeit, Latenz, Protokollkonformität und unterstützte NIPs und veröffentlichen Ergebnisse als kind 30166 Events.

## Funktionsweise

Monitore überprüfen die Relay-Verfügbarkeit durch Verbindungsaufbau und Senden von Test-Subscriptions. Latenzmessungen erfassen Verbindungszeit, Subscription-Antwortzeit und Event-Propagierungsverzögerung. Protokollkonformitätstests verifizieren, dass das Relay-Verhalten den Spezifikationen entspricht, und fangen Implementierungsfehler oder absichtliche Abweichungen auf.

Die NIP-Unterstützungsverifizierung geht über [NIP-11](/de/topics/nip-11/)-Behauptungen hinaus, indem tatsächlich getestet wird, ob beworbene Funktionen korrekt funktionieren. Wenn ein Relay [NIP-50](/de/topics/nip-50/)-Suchunterstützung behauptet, aber Suchanfragen fehlschlagen, werden Monitore NIP-50 aus der verifizierten Liste weglassen. Dies liefert die Wahrheit über Relay-Fähigkeiten.

Kind 30166 Events verwenden die Relay-URL als `d`-Tag, was sie zu parametrisierten ersetzbaren Events macht. Jeder Monitor veröffentlicht ein Event pro Relay, das aktualisiert wird, wenn sich Messungen ändern. Mehrere Monitore können dasselbe Relay verfolgen und bieten Redundanz und Kreuzvalidierung.

Round-Trip-Time (rtt) Tags messen die Latenz für verschiedene Operationen:
- `rtt open`: WebSocket-Verbindungsaufbau
- `rtt read`: Subscription-Antwortzeit
- `rtt write`: Event-Veröffentlichungsgeschwindigkeit

Alle Werte sind in Millisekunden. Clients verwenden diese Metriken, um Relays mit niedriger Latenz für zeitkritische Operationen zu bevorzugen.

Geografische Informationen helfen Clients, nahegelegene Relays für bessere Latenz und Zensurresistenz auszuwählen. Das `geo`-Tag enthält Ländercode, Ländername und Region. Das `network`-Tag unterscheidet Clearnet-Relays von Tor Hidden Services oder I2P-Endpoints.

## Anwendungsfälle

Monitor-Daten treiben Relay-Auswähler in Clients, Explorer-Websites und Vertrauensbewertungssysteme an. Durch Bereitstellung von Echtzeit-Relay-Status unabhängig von Relay-Selbstberichten ermöglicht NIP-66 eine informierte Relay-Auswahl.

Kombiniert mit [NIP-11](/de/topics/nip-11/) (selbstberichtete Fähigkeiten) und Trusted Relay Assertions (Vertrauensbewertung) bewegt sich das Ökosystem in Richtung datengesteuerter Relay-Auswahl anstatt sich auf fest codierte Standardwerte zu verlassen.

---

**Primärquellen:**
- [NIP-66 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/66.md) - Relay-Entdeckung und Liveness-Monitoring-Standard

**Erwähnt in:**
- [Newsletter #6: NIP Deep Dive](/de/newsletters/2026-01-21-newsletter/#nip-deep-dive-nip-11-and-nip-66)

**Siehe auch:**
- [NIP-11: Relay-Informationsdokument](/de/topics/nip-11/)
- [Trusted Relay Assertions](/de/topics/trusted-relay-assertions/)
