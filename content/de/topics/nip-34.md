---
title: "NIP-34: Git-Zusammenarbeit"
date: 2026-02-04
translationDate: 2026-03-07
description: "NIP-34 ermöglicht dezentrales Hosting und dezentrale Zusammenarbeit für Git-Repositories über Nostr-Events."
categories:
  - NIP
  - Development
---

NIP-34 definiert Event-Kinds für das Hosting von Git-Repositories, Patches und Issues auf Nostr-Relays. Das ermöglicht vollständig dezentrale Code-Zusammenarbeit ohne Abhängigkeit von zentralen Hosting-Plattformen wie GitHub oder GitLab.

## Wie es funktioniert

Repositories werden als adressierbare Events dargestellt, also als kind 30617, die Metadaten wie Name, Beschreibung und Clone-URLs enthalten. Der Owner des Repositories veröffentlicht dieses Event, um das Projekt auf Nostr zu etablieren.

Patches, also kind 1617, enthalten `git format-patch`-Inhalte, die auf ein Repository angewendet werden können. Beitragende reichen Patches als Events ein, die auf das Ziel-Repository verweisen. Das spiegelt den E-Mail-basierten Patch-Workflow wider, den Projekte wie der Linux-Kernel verwenden.

Issues, also kind 1621, funktionieren wie klassische Issue-Tracker. Pull Requests verwenden kinds 1618 und 1619, und Status-Updates verwenden 1630 bis 1633. Antworten auf Issues, Patches und Pull Requests verwenden Kommentare nach [NIP-22](/de/topics/nip-22/).

## Event-Kinds

- **30617** - Repository-Ankündigung (adressierbar)
- **30618** - Repository-Statusankündigung für Branches und Tags
- **1617** - Patch-Einreichung
- **1618** - Pull Request
- **1619** - Pull-Request-Update
- **1621** - Issue
- **1630-1633** - Status-Events für offen, gemerged/gelöst, geschlossen und Entwurf

## Warum es wichtig ist

NIP-34 trennt Discovery von Transport. Das eigentliche Repository kann weiter auf gewöhnlichen Git-Servern liegen, während Nostr-Events eine über Relays verteilte Ebene für Discovery, Diskussion, Patch-Austausch und Statusverfolgung bereitstellen. Ein Projekt kann also weiter git-native Werkzeuge nutzen, ohne von der Datenbank oder API einer einzelnen Forge abzuhängen.

Das `r`-Tag mit dem frühesten eindeutigen Commit ist eines der wichtigsten Details. Es gibt Clients eine Möglichkeit, Mirrors und Forks zu gruppieren, die dieselbe zugrunde liegende Repository-Historie repräsentieren, was sich allein aus Namen nur schwer ableiten lässt.

## Implementierungsstatus

- **ngit** - Kommandozeilen-Tool zum Veröffentlichen von Repositories und Patches auf Nostr
- **gitworkshop.dev** - Web-Oberfläche zum Durchsuchen von auf Nostr gehosteten Repositories
- **Notedeck** - Desktop-Client mit [Entwurfsunterstützung für NIP-34-Ansichten](https://github.com/damus-io/notedeck/pull/1279)

---

**Primärquellen:**
- [NIP-34 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/34.md)

**Erwähnt in:**
- [Newsletter #8 (2026-02-04)](/en/newsletters/2026-02-04-newsletter/) - Notedeck bekommt einen NIP-34-Viewer
- [Newsletter #9: Notedeck](/en/newsletters/2026-02-11-newsletter/#notedeck)

**Siehe auch:**
- [NIP-22: Kommentare](/de/topics/nip-22/)
