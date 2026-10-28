---
title: "Vorgeschlagener NIP-82 (nicht vergeben): Katalog für Softwareanwendungen"
date: 2026-06-17
lastmod: 2026-10-28
translationOf: /en/topics/nip-82.md
translationDate: 2026-10-28
draft: false
categories:
  - Proposals
  - Apps
---

Der auf dieser Seite beschriebene Katalog für Softwareanwendungen ist ein Vorschlag, der derzeit geprüft wird. Er ist kein akzeptierter NIP. Er befindet sich in [nostr-protocol/nips Pull Request #2526](https://github.com/nostr-protocol/nips/pull/2526) mit dem Titel „Zapstore spec“. Zum Zeitpunkt der letzten Aktualisierung dieser Seite ist dieser Pull Request offen und nicht gemergt, und der offizielle master-Branch der NIPs enthält keine Datei `82.md`. „NIP-82“ ist die Bezeichnung, die der Vorschlag für sich selbst verwendet. Es ist keine offizielle NIP-Nummer. Event-kinds, Tags und Verhalten können sich vor einem etwaigen Merge ändern. Laut dem Pull Request löst er den früheren [Pull Request #1336](https://github.com/nostr-protocol/nips/pull/1336) ab.

## Vorgeschlagene Event-kinds

Der Entwurf unterteilt einen Softwarekatalog in mehrere Arten von Events:

- **Kind 32267, Anwendung:** ein adressierbares Event, das eine App beschreibt.
- **Kind 30063, Release:** ein adressierbares Event für eine Version dieser App. Es verweist auf die Assets dieser Version.
- **Kind 3063, Asset:** ein reguläres Event, das eine herunterladbare Datei beschreibt.
- **Kind 30267, Kuratierung:** eine adressierbare Liste, die ein Kurator veröffentlicht, um Apps zu gruppieren oder zu empfehlen.
- **Kind 30509, Verknüpfung mit Signaturzertifikat:** ein adressierbares Event, das ein X.509-Zertifikat, etwa ein APK-Signaturzertifikat, mit dem Nostr-Schlüssel verknüpft, der Software veröffentlicht, damit Clients wissen, welche Zertifikate dieser Herausgeber kontrolliert. Sein `d`-Tag ist der SHA-256-Hash des DER-kodierten Zertifikats. Es trägt eine mit dem privaten Schlüssel des Zertifikats erstellte Signatur sowie ein Ablaufdatum als Unix-Zeitstempel und kann die Verknüpfung optional als widerrufen kennzeichnen.
- **Kind 10067, Relay-Liste:** eine ersetzbare Liste von Relays, auf denen Katalog-Events zu finden sind.

## Plattform, Integrität und Gültigkeit

Asset-Events tragen Plattform- und Laufzeitkennungen, sodass ein Client nur die Dateien anzeigen kann, die zu einem Gerät passen. Jedes Asset trägt außerdem einen Datei-Hash. Ein Client kann damit prüfen, ob die heruntergeladenen Bytes dem entsprechen, was der Herausgeber signiert hat. Für Android-Pakete enthält der Entwurf den Fingerabdruck des Signaturzertifikats. Ein Installer kann ihn mit dem Zertifikat einer bereits installierten App vergleichen, bevor er ein Update anbietet. Vor der Installation eines Android-Pakets SOLLTEN Clients das Event der kind 30509 anhand des Zertifikat-Hashes abrufen. Sie sollten dessen Zertifikatssignatur gegen das im APK eingebettete Zertifikat und gegen den Herausgeber des Assets verifizieren und prüfen, dass der Nachweis weder abgelaufen ist noch widerrufen wurde.

## Grenzen des Vertrauens

Eine gültige Signatur zeigt nur, dass ein bestimmter Schlüssel ein Event veröffentlicht hat. Sie beweist weder, dass der Schlüssel dem echten Entwickler gehört, noch dass die Software sicher ist oder dass der Liste eines Kurators vertraut werden kann. Der Vorschlag gibt keine Garantie hinsichtlich beliebiger Herausgeber. Clients und Nutzer müssen entscheiden, auf welche Schlüssel von Herausgebern und Kuratoren sie sich verlassen. Diese Seite behauptet weder ein Sicherheitsaudit noch Interoperabilität im Produktivbetrieb.

## Verhältnis zu NIP-89

Handler-Events nach [NIP-89](/de/topics/nip-89/) geben bekannt, welche Anwendungen welche Event-kinds verarbeiten können. Dieser Vorschlag beschreibt die Software-Artefakte und wo man sie bezieht, sodass beide getrennte Belange abdecken.

---

**Primärquellen:**
- [nostr-protocol/nips PR #2526: Zapstore spec](https://github.com/nostr-protocol/nips/pull/2526) (offen, nicht gemergt; löst [PR #1336](https://github.com/nostr-protocol/nips/pull/1336) ab)

**Erwähnt in:**
- [Newsletter #27: Berichterstattung zum Release von Amethyst v1.12.0 (historische Referenz)](/de/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
- [Newsletter #46: Katalog für Softwareanwendungen als NIP-82 vorgeschlagen](/de/newsletters/2026-10-28-newsletter/#software-application-catalog-proposed-as-nip-82)

**Siehe auch:**
- [NIP-89: Anwendungs-Handler](/de/topics/nip-89/)
