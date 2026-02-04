---
title: "NIP-34 (Git-Zusammenarbeit)"
date: 2026-02-04
description: "NIP-34 ermöglicht dezentrales Git-Repository-Hosting und Zusammenarbeit durch Nostr-Events."
---

NIP-34 definiert Event-Arten für das Hosting von Git-Repositories, Patches und Issues auf Nostr-Relays. Dies ermöglicht vollständig dezentralisierte Code-Zusammenarbeit ohne Abhängigkeit von zentralisierten Hosting-Plattformen wie GitHub oder GitLab.

## Funktionsweise

Repositories werden als adressierbare Events (kind 30617) dargestellt, die Metadaten wie Name, Beschreibung und Clone-URLs enthalten. Der Repository-Eigentümer veröffentlicht dieses Event, um das Projekt auf Nostr zu etablieren.

Patches (kind 1617) enthalten Git-Patch-Inhalte, die auf ein Repository angewendet werden können. Beitragende reichen Patches als Events ein, die auf das Ziel-Repository verweisen. Dies spiegelt den E-Mail-basierten Patch-Workflow wider, der von Projekten wie dem Linux-Kernel verwendet wird.

Issues (kind 1621) funktionieren wie traditionelle Issue-Tracker. Sie verweisen auf ein Repository und enthalten Titel und Beschreibung. Kommentare zu Issues und Patches verwenden Standard-Antwort-Events.

## Event-Arten

- **30617** - Repository-Ankündigung (adressierbar)
- **1617** - Patch-Einreichung
- **1621** - Issue
- **1622** - Issue-Status (offen/geschlossen)

## Implementierungen

- **ngit** - Kommandozeilen-Tool zum Veröffentlichen von Repos und Patches auf Nostr
- **gitworkshop.dev** - Web-Oberfläche zum Durchsuchen von Nostr-gehosteten Repositories
- **Notedeck** - Desktop-Client mit [Entwurfsunterstützung für NIP-34-Anzeige](https://github.com/damus-io/notedeck/pull/1279)

## Primäre Quellen

- [NIP-34 Spezifikation](https://github.com/nostr-protocol/nips/blob/master/34.md)

## Erwähnt in

- [Newsletter #8 (2026-02-04)](/de/newsletters/2026-02-04-newsletter/) - Notedeck fügt NIP-34-Viewer hinzu
