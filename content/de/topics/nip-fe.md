---
title: "NIP-FE-Vorschlag: HTTP-Befehle für relay"
date: 2026-09-30
draft: false
categories:
  - Project Proposals
  - Relays
translationOf: /en/topics/nip-fe.md
translationDate: 2026-10-01
---

Amethyst verwendet die vorläufige Bezeichnung NIP-FE für relay-Befehle über HTTP bei der Arbeit am Geode-relay und am Quartz-Client. Die Bezeichnung ist weder eine zugewiesene NIP noch ein Beleg für die Übernahme durch Nostr-relays.

## Transport

Statt eine WebSocket-Verbindung zu öffnen, sendet ein Client einen einzelnen `REQ`-, `COUNT`- oder `EVENT`-Frame per POST an einen HTTP-Endpunkt eines relay. Die Antwort überträgt relay-Frames als durch Zeilenumbrüche getrenntes JSON. Ein Client muss eine abgeschlossene Antwort von einem abgebrochenen Stream unterscheiden, und eine authentifizierte Anfrage verwendet weiterhin eine signierte Nostr-HTTP-Autorisierung. Der Transport ändert, wie Befehle ein relay erreichen; er ändert weder die zugrunde liegende event-Signatur noch den event-Inhalt.

Die [gemergte Implementierung](https://github.com/vitorpamplona/amethyst/pull/4231) von Amethyst ergänzt die Geode-Route, die Unterstützung im Quartz-Client, Begrenzungen für den Anfragekörper und die Nebenläufigkeit sowie Tests für Framing und Autorisierung. Sie ist ein Implementierungsbeleg auf Quellcode-Ebene, kein Nachweis dafür, dass unabhängige relays denselben Vorschlag implementiert haben.

## Namenskollision

Ein davon unabhängiger [Entwurfs-Pull-Request im NIPs-Repository](https://github.com/nostr-protocol/nips/pull/2488) verwendet ebenfalls **NIP-FE**, diesmal für private Feeds, die auf einer vorgeschlagenen Hülle für mehrere Empfänger aufbauen. Diese Arbeit ist noch offen und beschreibt ein anderes Problem als der HTTP-Transport von Amethyst. Keine der beiden vorläufigen Verwendungen belegt, dass die Bezeichnung einer akzeptierten Spezifikation zugewiesen wurde; Leser sollten den Vorschlag anhand seiner Quelle und seines Gegenstands identifizieren.

---

**Primärquellen:**
- [Implementierungs-PR für Amethyst Geode und Quartz](https://github.com/vitorpamplona/amethyst/pull/4231)
- [Amethyst-Repository](https://github.com/vitorpamplona/amethyst)
- [Offener Entwurf für private Feeds, der ebenfalls NIP-FE verwendet](https://github.com/nostr-protocol/nips/pull/2488)

**Erwähnt in:**
- [Newsletter #42: relay-Befehle von Amethyst](/de/newsletters/2026-09-30-newsletter/#amethyst-repairs-encrypted-group-interoperability)
