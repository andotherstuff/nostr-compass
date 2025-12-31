---
title: "Web of Trust"
date: 2025-12-31
translationOf: /en/topics/web-of-trust.md
translationDate: 2025-12-31
draft: false
categories:
  - Vertrauen
  - Soziales Netzwerk
---

Web of Trust (WoT) ist ein dezentralisiertes Vertrauensmodell, bei dem Reputation und Vertrauenswürdigkeit aus Beziehungen im sozialen Graphen abgeleitet werden, anstatt von zentralen Autoritäten.

## So Funktioniert Es

In Nostr nutzt Web of Trust den Follow-Graphen (NIP-02-Kontaktlisten) und Melde-Events, um Vertrauenswerte zu berechnen:

1. **Graph-Konstruktion**: Ein gerichteter Graph wird aus pubkeys, Events und deren Beziehungen (Follows, Stummschaltungen, Meldungen) erstellt
2. **Gewichtszuweisung**: Anfangsgewichte werden bekannten vertrauenswürdigen pubkeys zugewiesen (z.B. solche mit verifizierten NIP-05-Identifikatoren)
3. **Iterative Propagation**: Vertrauenswerte fließen durch das Netzwerk mit Algorithmen ähnlich PageRank
4. **Sybil-Resistenz**: Wenn ein Angreifer viele gefälschte Konten erstellt, wird das an sie weitergegebene Vertrauen durch die Anzahl der Fälschungen geteilt

## Wichtige Eigenschaften

- **Dezentralisiert**: Keine zentrale Autorität bestimmt die Reputation
- **Personalisiert**: Vertrauen kann aus der Perspektive jedes Benutzers basierend darauf berechnet werden, wem er folgt
- **Sybil-Resistent**: Bot-Farmen können das System aufgrund der Vertrauensverdünnung nicht leicht manipulieren
- **Komponierbar**: Kann für Spam-Filterung, Content-Moderation, Relay-Zugang und Zahlungsverzeichnisse angewendet werden

## Anwendungen in Nostr

- **Spam-Filterung**: Relays können WoT verwenden, um Inhalte mit niedrigem Vertrauen zu filtern
- **Content-Entdeckung**: Inhalte von Konten anzeigen, denen Ihr Netzwerk vertraut
- **Zahlungsverzeichnisse**: Lightning-Adresssuche mit Schutz vor Identitätsdiebstahl
- **Relay-Richtlinien**: WoT-Relays akzeptieren nur Notizen von vertrauenswürdigen pubkeys
- **Dezentrale Moderation**: Communities können basierend auf Vertrauenswerten kuratieren

## Implementierungen

Mehrere Projekte implementieren Web of Trust für Nostr:
- **Nostr.Band Trust Rank**: PageRank-ähnliche Bewertung für das Netzwerk
- **WoT Relays**: Relays, die nach sozialer Distanz filtern
- **DCoSL**: Protokoll für dezentralisierte Reputationssysteme
- **Noswot**: Vertrauensbewertung basierend auf Follows und Meldungen

---

**Primäre Quellen:**
- [Nostr.Band Trust Rank](https://trust.nostr.band/)
- [DCoSL-Protokoll](https://github.com/wds4/DCoSL)
- [Noswot](https://codeberg.org/weex/noswot)

**Erwähnt in:**
- [Newsletter #3: Dezember-Rückblick](/de/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Siehe auch:**
- [NIP-02: Folgeliste](/de/topics/nip-02/)
