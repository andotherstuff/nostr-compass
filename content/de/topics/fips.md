---
title: "FIPS"
date: 2026-02-25
translationOf: /en/topics/fips.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Networking
  - Infrastructure
---

FIPS (Free Internetworking Peering System) ist ein selbstorganisierendes Mesh-Networking-Protokoll, das Nostr-artige secp256k1-Schlüsselpaare als Knotenidentitäten verwendet.

## Wie es funktioniert

FIPS zielt darauf ab, Peer-Networking ohne zentrale Server oder Zertifizierungsstellen zu ermöglichen. Knoten entdecken Nachbarn, bauen Routing-Zustand auf und leiten Pakete nur anhand von lokalem Wissen weiter.

Das Design kombiniert einen Spanning Tree mit Bloom-Filter-Erreichbarkeitsdaten. Jeder Knoten erhält Koordinaten relativ zum Baum und routet dann gierig auf das Ziel zu. Falls Greedy-Routing scheitert, bietet der Baum weiterhin einen Fallback-Pfad.

Zwei Verschlüsselungsschichten schützen den Datenverkehr. Link-Layer-Verschlüsselung (Noise IK-Muster) sichert die Hop-by-Hop-Kommunikation zwischen Nachbarn. Session-Layer-Verschlüsselung (Noise XK-Muster) bietet Ende-zu-Ende-Schutz gegen zwischengeschaltete Router.

## Warum es wichtig ist

FIPS nutzt dasselbe Schlüsselmodell, das Nostr-Entwickler bereits kennen, wendet es aber auf Paket-Routing statt auf soziale Events an. Das ergibt eine einfache Identitätsgeschichte: Die Netzwerkidentität ist der kryptographische Schlüssel, keine IP-Zuweisung oder Zertifikatskette.

Das transport-agnostische Design ist ebenfalls wichtig. Dasselbe Routing- und Identitätsmodell kann im Prinzip über UDP, Ethernet, Bluetooth oder LoRa betrieben werden, was FIPS für feindliche oder unzuverlässige Netzwerkumgebungen interessant macht.

## Implementierungsstatus

Wie in Compass berichtet, enthält die aktuelle Rust-Implementierung bereits funktionierenden UDP-Transport und Bloom-Filter-basiertes Discovery. Relay-basiertes Bootstrapping ist noch zukünftige Arbeit, daher ist das Protokoll heute eher ein Networking-Substrat als ein fertiger Nostr-Relay-Ersatz.

---

**Primärquellen:**
- [FIPS Repository](https://github.com/jmcorgan/fips)
- [Design-Dokumentation](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md)

**Erwähnt in:**
- [Newsletter #11: FIPS News](/en/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**Siehe auch:**
- [Marmot Protocol](/de/topics/marmot/)
