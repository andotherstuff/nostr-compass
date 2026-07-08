---
title: "Keycast: Team-Nostr-Remote-Signierung"
date: 2026-05-21
draft: false
translationOf: /en/topics/keycast.md
translationDate: 2026-07-01
categories:
  - Signing
  - Security
  - Teams
---

Keycast ist ein selbst gehosteter NIP-46-Remote-Signing-Server, der für Teams entwickelt wurde. Er speichert private Nostr-Schlüssel verschlüsselt in SQLite, generiert NIP-46-bunker-Verbindungszeichenketten und betreibt Signierer-Prozesse, die Remote-Signieranfragen gemäß konfigurierbarer Richtlinien pro Schlüssel genehmigen oder ablehnen. Das Projekt wird von der Marmot Protocol-Organisation gepflegt.

## Wie es funktioniert

Der Server besteht aus vier Hauptkomponenten: einer Axum-API, die die Team-Verwaltung und NIP-98-HTTP-Authentifizierung übernimmt, einem SvelteKit-Web-Frontend, das NIP-07 zur Authentifizierung verwendet, einem Signierer-Manager, der Autorisierungszeilen überwacht und einen `signer_daemon` pro Autorisierung startet, und einer SQLite-Datenbank mit Migrationen.

Teammitglieder melden sich über ihre NIP-07-Browser-Erweiterung an. Die Web-App fordert ein NIP-98-HTTP-Auth-event an, das lokal von der Erweiterung signiert wird, und sendet dann diesen Auth-Header an die API. Die API verifiziert das event, extrahiert den pubkey und prüft die Team-Mitgliedschaft. Gespeicherte Schlüssel werden mit einer Root-`master.key`-Datei verschlüsselt, die separat vom Image eingebunden und niemals committet werden darf.

Der Signierer-Daemon entschlüsselt beim Start den gespeicherten Schlüssel und den bunker-Schlüssel, verbindet sich mit konfigurierten relays und ruft `Authorization::validate_policy` auf, bevor er jede NIP-46-Signieranfrage genehmigt. Richtlinien legen fest, welche event-kinds eine bestimmte bunker-Verbindung signieren darf.

## Sicherheitsaudit (Mai 2026)

Ein im Mai 2026 abgeschlossenes Sicherheitsaudit befasste sich mit Problemen bei Authentifizierung, Berechtigungen, Datenintegrität und Abhängigkeiten. Wichtige Änderungen:

- Die NIP-98-Authentifizierung erfordert nun genau einen `u`-tag und einen `method`-tag, weist veraltete oder zukünftige Zeitstempel zurück und validiert `payload`-Hashes des Anfragekörpers
- `ALLOWED_PUBKEYS` wird exakt geparst und serverseitig durchgesetzt; das Frontend stellt `/api/config?pubkey=<hex>` bereit, damit der Browser den Allowlist-Status prüfen kann, ohne die vollständige Serverliste zu erhalten
- Leere Richtlinien lehnen sign/encrypt/decrypt-Anfragen standardmäßig ab; die Richtlinienerstellung weist unbekannte oder fehlerhafte Berechtigungskonfigurationen zurück
- SQLite-Verbindungen aktivieren die Durchsetzung von Fremdschlüsseln; die Team-Löschung verliert keine Berechtigungs-Join-Daten mehr vor der Bereinigung
- Der serverseitige Routenschutz deckt nun auch verschachtelte App-Routen wie `/teams/:id` ab
- Web-Antworten setzen CSP-, Frame-, Content-Type-, Referrer-, Permissions- und HSTS-Header
- Eine SQL-Migration normalisiert alte allowed-kinds-Berechtigungs-JSON beim Start von `{"sign":[...]}` zu `{"allowed_kinds":[...]}`

Das Audit vermerkt verbleibende Punkte in [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md), die vor dem Vertrauen der Bereitstellung mit echten Team-Schlüsseln bearbeitet werden sollten.

## Bereitstellung

Die Docker-Compose-Bereitstellung bindet `master.key` in API- und Signierer-Container ein, führt Container mit einer Nicht-Root-UID/GID und einem schreibgeschützten Root-Dateisystem aus und verwendet Caddy-Labels, um `/api/*` an die API und alles andere an die Web-App zu leiten. Das veröffentlichte Image unter `ghcr.io/marmot-protocol/keycast` ist mit `master`, `latest` und `sha-<commit>` getaggt.

---

**Primärquellen:**
- [Keycast-Repository](https://github.com/marmot-protocol/keycast)
- [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md) - Ergebnisse des Sicherheitsaudits vom Mai 2026

**Erwähnt in:**
- [Newsletter #23: Keycast-Sicherheitsaudit abgeschlossen](/de/newsletters/2026-05-21-newsletter/#keycast-security-audit-complete)

**Siehe auch:**
- [NIP-46: Nostr Remote Signing](/de/topics/nip-46/)
- [NIP-07: Browser Extension Signer](/de/topics/nip-07/)
- [Marmot Protocol](/de/topics/marmot/)
