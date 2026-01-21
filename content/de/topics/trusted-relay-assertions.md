---
title: "Trusted Relay Assertions"
date: 2026-01-21
draft: false
categories:
  - Protokoll
  - Relays
---

Trusted Relay Assertions ist ein Entwurf-NIP-Vorschlag zur Standardisierung von Relay-Vertrauensbewertungen und Reputationsmanagement. Die Spezifikation führt kind 30385 Events ein, bei denen Assertion-Provider Vertrauenswerte veröffentlichen, die aus beobachteten Metriken, Betreiber-Reputation und Nutzerberichten berechnet werden.

## Funktionsweise

Der Vorschlag schließt eine Lücke im Relay-Ökosystem. Während [NIP-11](/de/topics/nip-11/) definiert, was Relays über sich selbst behaupten, und [NIP-66](/de/topics/nip-66/) misst, was wir beobachten, standardisiert Trusted Relay Assertions, was wir über die Vertrauenswürdigkeit von Relays schlussfolgern.

Assertion-Provider berechnen Punkte über drei Dimensionen. Zuverlässigkeit misst Verfügbarkeit, Wiederherstellungsgeschwindigkeit, Konsistenz und Latenz. Qualität bewertet Policy-Dokumentation, TLS-Sicherheit und Betreiber-Verantwortlichkeit. Zugänglichkeit beurteilt Zugangsbarrieren, Gerichtsbarkeitsfreiheit und Überwachungsrisiko. Ein Gesamt-Vertrauenswert (0-100) kombiniert diese Komponenten mit Gewichtungen: 40% Zuverlässigkeit, 35% Qualität, 25% Zugänglichkeit.

Jede Assertion enthält Konfidenzniveaus (niedrig, mittel, hoch) basierend auf Beobachtungszahlen. Die Betreiber-Verifizierung verwendet mehrere Methoden: kryptografischer Beweis über signierte NIP-11-Dokumente, DNS TXT-Einträge oder .well-known-Dateien. Die Spec integriert Web of Trust durch Betreiber-Vertrauenswerte. Die Policy-Klassifizierung hilft Nutzern, passende Relays zu finden: offen, moderiert, kuratiert oder spezialisiert.

Nutzer deklarieren vertrauenswürdige Assertion-Provider über kind 10385 Events. Clients fragen mehrere Provider ab und vergleichen Werte. Der Vorschlag beinhaltet einen Einspruchsprozess, bei dem Relay-Betreiber Werte unter Verwendung von [NIP-32](/de/topics/nip-32/) Labeling-Events anfechten können.

## Anwendungsfälle

Für [NIP-46](/de/topics/nip-46/) Remote-Signer helfen Vertrauens-Assertions Nutzern, unbekannte Relays zu bewerten, die in Verbindungs-URIs eingebettet sind, bevor sie Verbindungen akzeptieren. Kombiniert mit [NIP-65](/de/topics/nip-65/) Relay-Listen können Clients informierte Relay-Auswahlentscheidungen treffen, basierend sowohl auf Nutzerpräferenzen als auch auf Drittanbieter-Vertrauensbewertungen.

Die Spezifikation ergänzt bestehende Relay-Entdeckungsmechanismen. [NIP-66](/de/topics/nip-66/) bietet Entdeckung (was existiert), dieser Vorschlag fügt Bewertung hinzu (was gut ist). Zusammen ermöglichen sie informierte Relay-Auswahl anstatt sich auf hartcodierte Standards oder Mundpropaganda-Empfehlungen zu verlassen.

---

**Primärquellen:**
- [Entwurf NIP-Dokument](https://nostr.com/nevent1qqsqjymvcp6ch3ps3fqsxljf6j8u3adz64ucw8npnzuj3cn6dekn0gspz9mhxue69uhkummnw3ezumrpdejz7qg3waehxw309ahx7um5wgh8w6twv5hsyga3qg) - Kind 30817 Event, das die Spezifikation vorschlägt

**Erwähnt in:**
- [Newsletter #6: Nachrichten](/de/newsletters/2026-01-21-newsletter/#trusted-relay-assertions-a-new-approach-to-relay-trust)
- [Newsletter #6: NIP-Updates](/de/newsletters/2026-01-21-newsletter/#nip-updates)

**Siehe auch:**
- [NIP-11: Relay-Informationsdokument](/de/topics/nip-11/)
- [NIP-66: Relay-Entdeckung und Lebendüberwachung](/de/topics/nip-66/)
- [NIP-32: Labeling](/de/topics/nip-32/)