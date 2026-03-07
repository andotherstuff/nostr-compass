---
title: "Web of Trust"
date: 2025-12-31
translationOf: /en/topics/web-of-trust.md
translationDate: 2026-03-07
draft: false
categories:
  - Vertrauen
  - Soziales Netzwerk
---

Web of Trust, kurz WoT, ist ein dezentrales Vertrauensmodell, bei dem Reputation und Vertrauenswürdigkeit aus Beziehungen im sozialen Graphen abgeleitet werden statt von zentralen Autoritäten.

## Funktionsweise

In Nostr beginnt Web of Trust meist beim Follow-Graphen aus [NIP-02: Follow List](/de/topics/nip-02/) und ergänzt manchmal Mutes, Reports oder verifizierte Identitätssignale. Ein Client oder Dienst wählt einen oder mehrere Seed-Pubkeys, denen er bereits vertraut, und propagiert Vertrauen von dort nach außen durch den Graphen.

1. **Graph-Aufbau**: Ein gerichteter Graph aus Follows und optionalen negativen Signalen wird aufgebaut
2. **Auswahl der Seeds**: Ausgangspunkt sind Pubkeys, denen der Beobachter bereits vertraut
3. **Score-Propagation**: Rang wird mit einem Algorithmus wie PageRank oder einer Variante durch den Graphen weitergegeben
4. **Grenzwerte und Normalisierung**: Graph-Tiefe wird begrenzt, Accounts mit schwachem Signal werden gedämpft und der Endwert für Anzeige oder Filterung normalisiert

Der genaue Algorithmus ist nicht standardisiert. Zwei WoT-Systeme können beide gültig sein und trotzdem unterschiedliche Rankings liefern, weil sie unterschiedliche Seeds, Graph-Tiefen, Zerfallsregeln oder Behandlungen von Mutes und Reports verwenden.

## Warum das wichtig ist

WoT gibt Nostr eine Möglichkeit zu ranken und zu filtern, ohne einen zentralen Moderationsdienst zu brauchen. Ein personalisierter Trust-Graph lässt sich schwerer manipulieren als eine rohe Follower-Zahl, weil gefälschte Accounts trotzdem Vertrauen aus dem bestehenden Netzwerk des Beobachters erhalten müssen.

Die Kehrseite ist der Cold Start. Wenn du niemandem folgst, hat ein personalisiertes WoT fast keine Grundlage, um irgendetwas zu bewerten. Viele Produkte lösen das mit Start-Follows, Standards für vertrauenswürdige Provider oder vorab berechneten Scores externer Dienste.

## Anwendungen in Nostr

- **Spam-Filterung**: Relays können WoT nutzen, um Inhalte mit geringem Vertrauen zu filtern
- **Content Discovery**: Inhalte von Accounts hervorheben, denen dein Netzwerk vertraut
- **Payment Directories**: Lightning-Adresssuche mit Schutz gegen Nachahmung
- **Relay Policies**: WoT-Relays akzeptieren nur Notes von vertrauenswürdigen Pubkeys
- **Dezentrale Moderation**: Communities können anhand von Trust-Scores kuratieren

## Implementierungshinweise

Weil WoT-Berechnungen große Teile des Netzwerks crawlen müssen, berechnen viele Clients sie nicht lokal. [NIP-85: Trusted Assertions](/de/topics/nip-85/) existiert teilweise genau deshalb: Es gibt Clients einen Weg, signierte WoT-Berechnungen von Dritten zu nutzen, wenn lokale Berechnung zu teuer ist.

Bestehende Implementierungen beantworten außerdem unterschiedliche Fragen. Ein globaler Trust-Rang ist nützlich für Discovery und Spam-Resistenz im gesamten Netzwerk. Ein personalisierter lokaler Score ist besser für Fragen wie "zeige mir Accounts, denen mein Graph vertrauen würde". Eine WoT-Zahl ohne Kenntnis des zugrunde liegenden Modells zu lesen, ist eine häufige Quelle von Verwirrung.

---

**Primärquellen:**
- [NIP-02: Follow List](https://github.com/nostr-protocol/nips/blob/master/02.md)
- [NIP-85: Trusted Assertions](https://github.com/nostr-protocol/nips/blob/master/85.md)
- [Nostr.Band Trust Rank](https://trust.nostr.band/)
- [DCoSL Protocol](https://github.com/wds4/DCoSL)
- [Noswot](https://codeberg.org/weex/noswot)

**Erwähnt in:**
- [Newsletter #3: December Recap](/de/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Siehe auch:**
- [NIP-02: Follow List](/de/topics/nip-02/)
