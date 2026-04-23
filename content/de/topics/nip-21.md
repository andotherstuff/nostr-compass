---
title: "NIP-21: nostr:-URI-Schema"
date: 2026-04-22
translationOf: /en/topics/nip-21.md
translationDate: 2026-04-23
draft: false
categories:
  - Protocol
  - Interoperability
---

NIP-21 definiert das `nostr:`-URI-Schema, also eine standardisierte Methode, mit der Anwendungen, Websites und Betriebssysteme Nostr-Identifikatoren wie `npub`, `nprofile`, `nevent` und `naddr` an den Nostr-Client weiterreichen können, den der Nutzer als Handler registriert hat.

## Wie es funktioniert

Eine `nostr:`-URI besteht aus dem Schema-Präfix und einem der [NIP-19](/de/topics/nip-19/) bech32-Identifikatoren, mit Ausnahme von `nsec`. Clients und Betriebssysteme behandeln das Schema ähnlich wie `mailto:` oder `tel:`: Wer sich als Handler registriert, kann dafür sorgen, dass ein `nostr:`-Link überall im System direkt im bevorzugten Nostr-Client geöffnet wird.

Beispiele aus der Spezifikation:

- `nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9` verweist auf ein Nutzerprofil
- `nostr:nprofile1...` verweist auf ein Nutzerprofil mit eingebetteten Relay-Hinweisen
- `nostr:nevent1...` verweist auf ein bestimmtes Event mit Relay-Hinweisen
- `nostr:naddr1...` verweist auf ein parameterisiertes ersetzbares Event, zum Beispiel einen Longform-Artikel

## Verknüpfung von HTML-Seiten mit Nostr-Entitäten

NIP-21 spezifiziert außerdem zwei nützliche `<link>`-Konventionen für Webseiten, die Nostr-Entitäten entsprechen. Eine Seite, die denselben Inhalt wie ein Nostr-Event ausliefert, etwa ein aus einem [NIP-23](/de/topics/nip-23/) `kind:30023`-Artikel gerendertes Blogpost, kann ein `<link rel="alternate">` mit der Nostr-URI einbinden. Eine Profilseite kann ein `<link rel="me">` oder `<link rel="author">` auf ein `nprofile` setzen, um Nostr-basierte Autorenschaft zu signalisieren.

## Warum es wichtig ist

Das Schema ist die Interoperabilitätsschicht, die jeden Nostr-Identifikator außerhalb der UI eines einzelnen Clients zu einem funktionierenden Link macht. Browser-Erweiterungen, mobile Betriebssystem-Handler und Desktop-Shells können `nostr:`-URIs an den jeweils installierten Client weiterreichen. Dadurch lässt sich ein Profil oder Event als URI teilen, ohne die Möglichkeit zu verlieren, es Nostr-nativ zu öffnen.

## Implementierungen

Die Unterstützung für `nostr:`-URIs ist im gesamten Client-Ökosystem breit vorhanden, darunter große Web-, Mobile- und Desktop-Clients. Browser-Erweiterungen wie [nos2x](https://github.com/fiatjaf/nos2x) und [Alby](https://github.com/getAlby/lightning-browser-extension) übernehmen die URI-Registrierung in Desktop-Browsern.

---

**Primärquellen:**

- [NIP-21-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/21.md)

**Erwähnt in:**

- [Newsletter #19: Nostrability migriert zu NIP-34](/de/newsletters/2026-04-22-newsletter/#nostrability-migriert-zu-nip-34-und-offnet-19-pro-nip-interoperabilitats-tracker)

**Siehe auch:**

- [NIP-19: bech32-kodierte Entitäten](/de/topics/nip-19/)
- [NIP-23: Long-form content](/de/topics/nip-23/)
