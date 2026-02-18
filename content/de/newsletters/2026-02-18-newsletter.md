---
title: 'Nostr Compass #10'
date: 2026-02-18
translationOf: /en/newsletters/2026-02-18-newsletter.md
translationDate: 2026-02-18
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, deinem wöchentlichen Wegweiser durch Nostr.

**Diese Woche:** Eine Blossom-Local-Cache-Schicht nimmt Gestalt an, da unabhängige Projekte auf Offline-Medienzugriff für Android konvergieren. Alby startet eine [NWC-Entwickler-Sandbox](https://sandbox.albylabs.com) zum Erstellen und Testen von Nostr Wallet Connect-Integrationen ohne echte Mittel zu riskieren. Konkurrierende Vorschläge für KI-Agenten-Kommunikation auf Nostr erscheinen in derselben Woche von zwei Autoren. fiatjaf entfernt ungenutzte Felder aus [NIP-11](https://github.com/nostr-protocol/nips/pull/1946) und streicht Aufbewahrungsrichtlinien, Ländercodes, Datenschutzrichtlinien und Community-Präferenz-Tags, die Relay-Betreiber nie übernommen haben. [NIP-85](https://github.com/nostr-protocol/nips/pull/2223) mergt Hinweise zur Service-Provider-Auffindbarkeit für Trusted Assertions. Ein neuer `D`-Tag in [NIP-52](https://github.com/nostr-protocol/nips/pull/1752) ermöglicht tagesgranulares Timestamp-Indexing von Kalender-Events. Neue Projekte umfassen [Mapnolia](https://github.com/zeSchlausKwab/mapnolia) für dezentrale Kartenkachel-Verteilung, [Pika](https://github.com/sledtools/pika) für MLS-verschlüsseltes Messaging, [Keep](https://github.com/privkeyio/keep-android) für FROST-Threshold-Signing auf Android, [Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree) für inhaltsadressierten Speicher mit Nostr-Integration und [Prism](https://github.com/hardran3/Prism) zum Teilen von Inhalten auf Nostr aus jeder Android-App. [Primal Android](https://github.com/PrimalHQ/primal-android-app) mergt 11 NWC-PRs mit Dual-Wallet-Unterstützung und automatischem Service-Lebenszyklus. [Mostro Mobile](https://github.com/MostroP2P/mobile) liefert eine [eingebaute Lightning-Wallet](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2) durch NWC-Integration. [Notedeck](https://github.com/damus-io/notedeck) bereitet die Veröffentlichung im Android App Store vor, während HAVEN [v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3) mit Multi-npub-Unterstützung und Cloud-Backup erreicht. Die Deep Dives dieser Woche behandeln NIP-85s Trusted Assertions-System zur Delegation von Web-of-Trust-Berechnungen an Service Provider sowie NIP-52s Kalender-Events-Protokoll nach dem tagesgranularen Indexierungs-Update.

## Neuigkeiten

### Blossom Local Cache Layer entsteht

Mehrere unabhängige Projekte konvergieren auf dasselbe Problem: Offline-Zugriff auf [Blossom](/de/topics/blossom/)-Medien auf Mobilgeräten.

[Morganite](https://github.com/greenart7c3/Morganite), eine neue Android-App von greenart7c3 (dem Entwickler hinter [Amber](https://github.com/greenart7c3/amber) und [Citrine](https://github.com/greenart7c3/Citrine)), implementiert clientseitiges Caching für Blossom-Medien. Nutzer können zuvor angezeigte Bilder und Dateien ohne Netzwerkverbindung aufrufen.

[Aerith](https://github.com/hardran3/Aerith) lieferte [v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2) mit Bildmarkierung, Massen-Mirror-/Tag-/Löschoperationen, Filterung nach Bezeichnung und Dateityp sowie erster lokaler Blossom-Cache-Unterstützung. Aerith ist eine Verwaltungsoberfläche für Nutzer, die Medien über mehrere Blossom-Server verteilt speichern und ihre Blobs organisieren und spiegeln müssen.

Ein neuer [Leitfaden zur lokalen Cache-Implementierung](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md) in der Blossom-Spezifikation dokumentiert clientseitigen Blob-Speicher, während [Prism](https://github.com/hardran3/Prism) (vom selben Entwickler wie Aerith) Blossom-Upload-Integration in seinen Android-Share-to-Nostr-Ablauf integriert. Vier unabhängige Projekte konvergierten diese Woche auf dasselbe Problem: eine dedizierte Caching-App, ein Medienmanager, eine Referenzspezifikation und ein Share-Tool mit Blossom-Integration – alle implementieren persistenten lokalen Speicher über einfaches Upload-und-Abrufen hinaus.

### Alby NWC-Entwickler-Sandbox

[Alby](https://sandbox.albylabs.com) hat eine Sandbox-Umgebung für Entwickler gestartet, die mit [Nostr Wallet Connect (NIP-47)](/de/topics/nip-47/) arbeiten. Die Sandbox bietet einen gehosteten NWC-Wallet-Dienst, mit dem Entwickler Testverbindungen erstellen und simulierte Zahlungen senden können, ohne eine echte Lightning-Wallet anzubinden – und dabei den vollständigen Request-Response-Zyklus von NWC-Events in Echtzeit beobachten können. Entwickler erzeugen einen `nostr+walletconnect://`-Verbindungsstring aus der Sandbox und übergeben ihn an ihren Client. Die Sandbox zeigt dann die resultierenden kind-23194-Request- und kind-23195-Response-Events an, während sie zwischen Client und Wallet-Dienst fließen.

Dies senkt die Einstiegshürde für neue NWC-Integrationen. Bisher erforderte das Testen entweder eine persönliche Lightning-Wallet oder einen selbst gehosteten NWC-Dienst. Die Sandbox abstrahiert das weg und gibt Entwicklern eine sofortige Feedback-Schleife für die Implementierung von `pay_invoice`, `get_balance`, `make_invoice`, `lookup_invoice` und `list_transactions` gegen einen Live-NWC-Endpunkt.

### KI-Agenten-NIPs erscheinen

Vorschläge für KI-Agenten-Kommunikation auf Nostr erschienen innerhalb weniger Tage voneinander und nähern sich dem Problem aus verschiedenen Blickwinkeln.

[NIP-XX: AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226) von joelklabo definiert ein vollständiges Protokoll für KI-Agenten-Interaktion: Event-Kinds für Prompts, Antworten, Streaming-Deltas, Status-Updates, Tool-Telemetrie, Fehler, Abbrüche und Fähigkeits-Erkennung. Ein `ai.info`-Discovery-Event (kind 31340, ersetzbar) ermöglicht Agenten, ihre unterstützten Modelle, Tools mit Schemata, Streaming-Unterstützung und Rate-Limits anzukündigen. joelklabos Vorschlag umfasst Run-Korrelation via Prompt-ID, Session-Management, Stream-Abgleich mit Sequenzordnung und [NIP-59](/de/topics/nip-59/)-Hinweise für Metadaten-Privatsphäre.

[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220) von pablof7z verfolgt einen anderen Ansatz und definiert Kinds für Agenten-Instanziierung: Definitionen und Lektionen. Das sind die Event-Typen, die pablof7z in [TENEX](https://github.com/tenex-chat/tenex) verwendet, dem autonomen Lernsystem auf Nostr. Ein Begleitvorschlag, [NIP-AD: MCP Server and Skill Announcements](https://github.com/nostr-protocol/nips/pull/2221), ebenfalls von pablof7z, definiert Events zur Ankündigung von [Model Context Protocol](https://modelcontextprotocol.io/)-Servern und Skills auf Nostr. [NIP-22](/de/topics/nip-22/)-Kommentare werden unterstützt, sodass die Community MCP-Server direkt auf Nostr diskutieren und bewerten kann.

NIP-XX deckt vollständige Agenten-Kommunikation ab, während NIP-AE und NIP-AD Identität und Tool-Discovery adressieren. Diese Vorschläge könnten zu einem einheitlichen Standard konvergieren oder als komplementäre Schichten koexistieren.

## Releases

### HAVEN v1.2.0-rc3

[HAVEN](https://github.com/bitvora/haven), das All-in-One-Persönlichkeitsrelay, das vier Relay-Funktionen mit einem [Blossom](/de/topics/blossom/)-Medienserver bündelt, erreichte [v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3). Dieser Release-Kandidat fügt Unterstützung für mehrere npubs hinzu und ermöglicht es einer einzigen HAVEN-Instanz, mehrere Nostr-Identitäten zu bedienen. Frühere RCs fügten `--from-cloud`- und `--to-cloud`-Flags für Cloud-Backup hinzu (RC2) und behobenen einen Web-of-Trust-Doppelzählungsfehler (RC1).

### Mostro Mobile v1.2.0: Eingebaute Lightning-Wallet

[Mostro Mobile](https://github.com/MostroP2P/mobile), der Mobile-Client für die [Mostro](https://github.com/MostroP2P/mostro) P2P-Bitcoin-Börse ([v1.1.0 letzte Woche behandelt](/de/newsletters/2026-02-11-newsletter/#mostro-liefert-erste-öffentliche-beta)), lieferte [v1.2.0](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2) mit einer eingebauten Lightning-Wallet durch vollständige [NWC (NIP-47)](/de/topics/nip-47/)-Integration. Käufer und Verkäufer müssen nicht mehr zwischen Apps wechseln, um Rechnungen zu bearbeiten. Die App erkennt Hold-Invoices für Verkäufer und bezahlt sie automatisch über die verbundene Wallet, während Käufer automatische Rechnungserstellung erhalten. Dem Release folgte [v1.1.1](https://github.com/MostroP2P/mobile/releases/tag/v1.1.1%2B1) aus früherer Woche, das Multi-Mostro-Node-Unterstützung mit einem kuratierten Register vertrauenswürdiger Instanzen, kind-0-Metadaten-Abruf für Node-Anzeige, benutzerdefiniertes Node-Management per pubkey und automatischen Fallback bei Offline-Nodes hinzufügte.

Serverseitig landete [Mostro v0.16.2](https://github.com/MostroP2P/mostro/releases/tag/v0.16.2) mit Fixes für doppelte Dev-Fee-Zahlungen, Rate-Limiting am Passwortvalidierungs-RPC-Endpunkt und ordentliches Dispute-Cleanup bei kooperativem Abbruch.

Ein neues Begleitprojekt, [mostro-skill](https://github.com/MostroP2P/mostro-skill), ermöglicht Agenten den Handel auf Mostro über Nostr.

### Aerith v0.2

[Aerith](https://github.com/hardran3/Aerith), der [Blossom](/de/topics/blossom/)-Bildmanager, lieferte [v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2) mit Bildbezeichnungen zur Medienorganisation, Massen-Mirror-/Tag-/Löschoperationen über Server hinweg, Filterung nach Bezeichnung und Dateityp sowie erster lokaler Cache-Unterstützung. Siehe [Neuigkeiten-Abschnitt](#blossom-local-cache-layer-entsteht) für den Kontext zum übergreifenden Local-Cache-Trend.

### Mapnolia: Dezentrale Kartenkacheln über Nostr

[Mapnolia](https://github.com/zeSchlausKwab/mapnolia) ist ein neuer Geodaten-Server, der [PMTiles](https://github.com/protomaps/PMTiles)-Kartenarchive in geografische Regionen unterteilt und sie über Nostr zur dezentralen Auffindbarkeit ankündigt. Er veröffentlicht kind-34444-parametrisierte ersetzbare Events an Nostr-Relays, die einen vollständigen Index von Kartenkachel-Chunks mit Layer-Metadaten, Geohash-Regionen, Dateireferenzen und [Blossom](/de/topics/blossom/)-Server-Details enthalten.

Clients entdecken und rufen Kartendaten über das Nostr-Netzwerk ab statt über zentralisierte Kachel-Server, wobei Ankündigungs-Events genug Metadaten tragen, um nur die benötigten geografischen Regionen von aufgeführten Blossom-Servern anzufordern. Mapnolia ist das erste Projekt, das Geodaten-Verteilung zu Nostr bringt und Möglichkeiten für offline-fähige Kartenanwendungen eröffnet.

### Pika: Marmot-basiertes verschlüsseltes Messaging

[Pika](https://github.com/sledtools/pika) ist eine neue Ende-zu-Ende-verschlüsselte Messaging-App für iOS und Android, die das [Marmot](/de/topics/marmot/)-Protokoll nutzt, das [Messaging Layer Security (MLS)](/de/topics/mls/) über Nostr-Relays schichtet. Die Architektur trennt Zuständigkeiten in einen Rust-Kern (`pika_core`), der MLS-Zustandsverwaltung und Nachrichten-Verschlüsselung/-Entschlüsselung über Nostr-Relays übernimmt, mit schlanken nativen UI-Schalen in SwiftUI (iOS) und Kotlin (Android). Der Zustand fließt unidirektional: die UI versendet Aktionen an den Rust-Actor, der den Zustand mutiert und Snapshots mit Revisionsnummern per UniFFI- und JNI-Bindungen zurück an die UI emittiert.

Pika reiht sich in ein wachsendes Feld von MLS-on-Nostr-Messengern ein, neben [White Noise](https://github.com/marmot-protocol/whitenoise), [Vector](https://github.com/VectorPrivacy) und [0xchat](https://0xchat.com). Alle nutzen Nostr-Relays als Transportschicht für MLS-verschlüsselten Ciphertext und halten Relay-Betreiber davon fern, Nachrichteninhalte zu lesen. Pika verwendet das Marmot Development Kit (MDK) für seine MLS-Implementierung und nostr-sdk für Relay-Konnektivität.

### Keep: [FROST](/de/topics/frost/)-Threshold-Signing für Android

[Keep](https://github.com/privkeyio/keep-android) ist eine neue Android-Anwendung für [FROST](/de/topics/frost/)-Threshold-Signing, bei dem kein einzelnes Gerät den vollständigen privaten Schlüssel hält. Es implementiert [NIP-55](/de/topics/nip-55/) (Android Signer) und [NIP-46](/de/topics/nip-46/) (Remote-Signing), sodass kompatible Nostr-Clients Signaturen anfordern können, während das Schlüsselmaterial über Geräte verteilt bleibt. Die Standardkonfigurationen sind 2-von-3 und 3-von-5, wobei jeder t-von-n-Schwellenwert unterstützt wird.

Keeps verteilte Schlüsselgenerierung (DKG) läuft über Nostr-Relays mit benutzerdefinierten Event-Kinds: kind 21101 für Gruppenankündigungen, kind 21102 für Round-1-Commitment-Polynome (öffentlich übertragen) und kind 21103 für Round-2-Geheimschlüsselanteile ([NIP-44](/de/topics/nip-44/) verschlüsselt Punkt-zu-Punkt zwischen Teilnehmern). Der private Gruppenschlüssel-Skalar wird während des DKG nirgends berechnet oder zusammengesetzt. Jedes Gerät hält nur seinen Polynomauswertungs-Anteil, und jede t-Anteile können durch ein Zwei-Runden-Commit-then-Sign-Protokoll eine gültige Schnorr-Signatur erzeugen. Die resultierende 64-Byte-Signatur ist von einer Single-Signer-Schnorr-Signatur nicht zu unterscheiden. Intern verwendet Keep die `frost-secp256k1-tr`-Crate der Zcash Foundation mit Taproot-Tweaking, sodass der Gruppen-Public-Key direkt als Nostr-npub funktioniert.

Keep reiht sich in die [Frostr](https://frostr.org)-Projektfamilie ein, neben [Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop), [Igloo für Android](https://github.com/FROSTR-ORG/igloo-android), [Frost2x](https://github.com/FROSTR-ORG/frost2x) und [Igloo für iOS](https://github.com/FROSTR-ORG/igloo-ios), und erweitert die Optionen für Threshold-Key-Management auf Nostr.

### Prism: Alles von Android aus auf Nostr teilen

[Prism](https://github.com/hardran3/Prism) ist eine neue Android-App (Kotlin/Jetpack Compose, API 26+), die sich als System-Share-Ziel registriert und Nutzern ermöglicht, Text, URLs, Bilder und Videos aus jeder App auf ihrem Telefon auf Nostr zu veröffentlichen. Geteilte URLs durchlaufen einen Tracking-Parameter-Stripper, bevor sie zu Notizen komponiert werden. Prism ruft OpenGraph-Metadaten ab, um reichhaltige Link-Vorschauen zu generieren, und rendert native Nostr-Referenzen (`note1`, `nevent1`) inline.

Die Scheduling-Engine verwendet einen hybriden `AlarmManager`/`WorkManager`-Ansatz, um Android-Batterieoptimierungen zu umgehen: AlarmManager übernimmt präzises Aufweck-Timing, während expedited WorkManager-Tasks die Zustellung sicherstellen, mit exponentiellem Backoff-Retry für Offline-Szenarien. Medien-Uploads laufen über konfigurierbare [Blossom](/de/topics/blossom/)-Server mit Thumbnail-Generierung für Bilder und Video-Frames. Das gesamte Event-Signing wird an [NIP-55](/de/topics/nip-55/)-externe Signer wie [Amber](https://github.com/greenart7c3/amber) delegiert, mit Multi-Account-Unterstützung zum Wechseln zwischen Identitäten. Prism unterstützt auch [NIP-84 (Highlights)](/de/topics/nip-84/)-Posts. Vom selben Entwickler wie [Aerith](#aerith-v02).

### Hashtree: Inhaltsadressierter Speicher mit Nostr-Integration

[Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree) ist ein dateisystembasiertes inhaltsadressiertes Blob-Speichersystem, das Merkle-Wurzeln auf Nostr veröffentlicht, um veränderbare npub/Pfad-Adressen zu erzeugen. Das System verwendet „dumb storage", das mit jedem Key-Value-Store funktioniert und Inhalte in 2-MB-Blöcke unterteilt, die für [Blossom](/de/topics/blossom/)-Uploads optimiert sind. Anders als BitTorrent wird keine aktive Merkle-Proof-Berechnung benötigt – Blobs werden einfach per Hash gespeichert und abgerufen.

Die Nostr-Integration ermöglicht Git-Remote-URLs wie `htree://npub.../repo-name` zum Klonen von Repositories, mit Befehlen wie `htree publish mydata <hash>` zum Veröffentlichen von Inhalts-Hashes unter `npub.../mydata`-Adressen. Das umfassende CLI unterstützt verschlüsselte (Standard) und öffentliche Speichermodi, Content-Pinning, Push zu Blossom-Servern und Verwaltung von Nostr-Identitäten. Jedes gespeicherte Element ist entweder rohe Bytes oder ein Baumknoten und bietet eine Grundlage für dezentrale Inhaltsverteilung über Nostrs Relay-Netzwerk.

### Espy: Farbpaletten-Erfassung auf Shakespeare

[Espy](https://espy.you), aufgebaut auf der [Shakespeare](https://soapbox.pub/tools/shakespeare/)-Plattform, ermöglicht Nutzern die Erfassung von Farbpaletten aus Fotos und deren Teilen als Nostr-Events. Shakespeare ist ein KI-gestützter App-Builder, der Nutzer über NIP-07-Browser-Erweiterungen authentifiziert und eingebaute Nostr-Relay-Konnektivität bietet, sodass Entwickler Apps ohne eigene Schlüsselverwaltung oder Relay-Pool ausliefern können. Espy extrahiert dominante Farben aus Kamerainput in teilbare Palettenkarten, die über Standard-Nostr-Feeds auffindbar sind.

### Flotilla 1.6.4

[Flotilla](https://gitea.coracle.social/coracle/flotilla), hodlbods Discord-ähnlicher Nostr-Client, der Relays als Gruppen organisiert, lieferte [1.6.4](https://gitea.coracle.social/coracle/flotilla/releases/tag/1.6.4). Die Coracle-Projektfamilie ist von GitHub auf eine selbst gehostete [Gitea-Instanz](https://gitea.coracle.social/coracle) umgezogen. Dieses Release fügt Push-Benachrichtigungen via NIP-9a und einen Wallet-Empfangsablauf hinzu, sowie klassifizierte Einträge und Space-URL-Unterstützung. Verbesserungen der Oberfläche umfassen aufgeräumte Modals und Benachrichtigungs-Handling. Raum-Stummschaltung und sichere Bereichs-Einfügungen auf Mobilgeräten runden die Änderungen ab, begleitet von Fixes für Safari-Bild-Uploads und Kalender-Event-Details.

### Shosho v0.12.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), die mobile Live-Streaming-App mit Nostr-Integration, lieferte [v0.12.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.12.0). Dieses Release fügt Video-Clips mit In-Player-Antworten und benutzerdefinierter Emoji-Integration hinzu. Thread-Schutz blockiert indirekten Erwähnungs-Spam, und eine neue QR-Teilen-Funktion ermöglicht Nutzern den Offline-Profilaustausch. Ein neuer horizontaler Wiedergabemodus gibt Streams eine Twitch-ähnliche Betrachtungserfahrung, und der Stöbern-Bildschirm zeigt nun Creator-Clips neben Live-Streams.

### Granary v10.0

[Granary](https://github.com/snarfed/granary), eine Social-Web-Übersetzungsbibliothek, die Daten zwischen Nostr, Bluesky, ActivityPub und anderen Plattformen in ein gemeinsames Format konvertiert, lieferte [v10.0](https://github.com/snarfed/granary/releases/tag/v10.0) mit Breaking Changes. Das Release wechselt Nostrs Standard-ActivityStreams-1-IDs von bech32 zu Hex und fügt erweiterte Nostr-Unterstützung hinzu, einschließlich [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md)-Erwähnungs-Parsing und Artikel-Tags. Eine neue Mehrfach-Ausgabe-Option über Konverter hinweg ermöglicht Entwicklern die Massenübersetzung zwischen Protokollen.

### Nostr MCP Server v3.0.0

[Nostr MCP Server](https://github.com/AustinKelsay/nostr-mcp-server), ein [Model Context Protocol](https://modelcontextprotocol.io/)-Server, der KI-Agenten die Interaktion mit dem Nostr-Netzwerk ermöglicht, lieferte [v3.0.0](https://github.com/AustinKelsay/nostr-mcp-server/releases/tag/v3.0.0). Dieses Major-Release fügt soziale Aktionen (Follows, Reaktionen, Reposts, Antworten) und Relay-Listen-Management mit [NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md)-Unterstützung plus optionaler [NIP-42](/de/topics/nip-42/)-Authentifizierung hinzu. Direktnachrichten via [NIP-17](/de/topics/nip-17/) und [NIP-44](/de/topics/nip-44/) sind ebenfalls neu. Das Release ergänzt die dieswöchigen [KI-Agenten-NIP-Vorschläge](#ki-agenten-nips-erscheinen) als praktisches Tooling für Agenten auf Nostr.

### Aegis v0.3.8

[Aegis](https://github.com/ZharlieW/Aegis), der plattformübergreifende Nostr-Signer, lieferte [v0.3.8](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.8) mit mehrsprachiger UI-Unterstützung und einem inkrementellen Update-Manager für seinen eingebauten Nostr-App-Browser. Der neue Update-Mechanismus vergleicht inkrementell gegen den lokalen Zustand und hält das In-App-Verzeichnis der Nostr-Web-Apps mit geringerem Bandbreitenverbrauch aktuell. Das Release führt außerdem 5-Minuten-Schlüsselmaterial-Caching ein, um Datenbank-Round-Trips beim Signieren mehrerer Events in Folge zu reduzieren.

### SNSTR v0.3.1

[SNSTR](https://github.com/AustinKelsay/snstr) (Secure Nostr Software Toolkit for Renegades), eine TypeScript-Bibliothek für das Nostr-Protokoll, lieferte [v0.3.1](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.1). Das Release fügt Paketverifizierungs-Guards hinzu, die sicherstellen, dass alle Einstiegspunkte in npm-Tarballs enthalten sind, mit CI-Durchsetzung auf Node und Bun. [v0.3.0](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.0) erschien in derselben Woche.

### Citrine v2.0.0-pre1

[Citrine](https://github.com/greenart7c3/Citrine), das Android-Nostr-Relay von greenart7c3, veröffentlichte [v2.0.0-pre1](https://github.com/greenart7c3/Citrine/releases/tag/v2.0.0-pre1) mit Performance-Verbesserungen durch optimierte Datenbankindizes und besseres Kotlin-Coroutine-Handling. Das Release verbessert außerdem die Unterstützung für das Hosting von Web-Apps, wobei jede App nun auf einem eigenen Port läuft.

## Projekt-Updates

### Primal Android: NWC-Infrastrukturausbau

[Primal Android](https://github.com/PrimalHQ/primal-android-app) mergte diese Woche 11 NWC-bezogene PRs und setzt den Ausbau fort, der [vor zwei Wochen begonnen wurde](/de/newsletters/2026-02-04-newsletter/#primal-android-liefert-nwc-verschlüsselung). Dieser Batch fügt Dual-Wallet-NWC-Unterstützung hinzu, automatischen Service-Start/Stopp gekoppelt an Backend-Benachrichtigungen, Verbindungsrouting nach Wallet-Typ und ordentliche Datenbereinigung bei Wallet-Löschung. Der NWC-Dienst verwaltet nun seinen eigenen Lebenszyklus basierend auf dem Wallet-Verbindungsstatus und reduziert manuellen Benutzereingriff.

### Notedeck: Android-App-Store-Vorbereitung

[Notedeck](https://github.com/damus-io/notedeck), der plattformübergreifende Nostr-Client vom [Damus](https://github.com/damus-io/damus)-Team, mergte diese Woche die [Vorbereitung für die Android-App-Store-Veröffentlichung](https://github.com/damus-io/notedeck/pull/1287). Der PR fügt einen UGC (User Generated Content)-Compliance-Plan hinzu, der von Google Play gefordert wird, einschließlich eines Nutzungsbedingungs-Akzeptanzbildschirms, Nutzerblockierung über Kontextmenüs und Einstellungen, [NIP-56 (Meldungen)](/de/topics/nip-56/)-Funktionalität, die Report-Events an Relays veröffentlicht, und eines Abschnitts für Inhalts- und Sicherheitseinstellungen. Build-Infrastruktur wurde für die Generierung signierter Release-APKs und AABs (Android App Bundles) via neue Makefile-Ziele hinzugefügt. Ein EULA-Dokument legt eine Altersanforderung von 17+ und Nostr-spezifische Haftungsausschlüsse über dezentrale Inhalte fest. Die Compliance-Features selbst erscheinen in Follow-up-PRs; dieser Merge legt die Dokumentations- und Signierungsgrundlage.

Auf der Damus-iOS-Seite landete ein Fix für eine [endlos drehende Lade-Spinner-Regression](https://github.com/damus-io/damus/pull/3593), bei der der Spinner unbegrenzt weiter lief, nachdem Inhalte bereits geladen waren.

### Nostria: Discovery-Relays und DM-Fixes

[Nostria](https://github.com/nostria-app/nostria), der plattformübergreifende Nostr-Client mit Fokus auf globale Skalierung, mergte diese Woche 9 PRs. Der bemerkenswerteste fügt [Auto-Initialisierung von Discovery-Relays](https://github.com/nostria-app/nostria/pull/460) für Profil-Lookup hinzu und gibt neuen Nutzern funktionierende Relay-Konnektivität ohne manuelle Konfiguration. Weitere Fixes adressieren [DM-Textarea-Umbruch](https://github.com/nostria-app/nostria/pull/466), [Vollbild-Video-Viewport-Füllung](https://github.com/nostria-app/nostria/pull/479), [Artikel-Metadaten-Extraktion in Repost-Vorschauen](https://github.com/nostria-app/nostria/pull/481) und [nostr:-URI-Auflösung in Benachrichtigungen](https://github.com/nostria-app/nostria/pull/458).

### Camelus: Riverpod-v3-Migration

[Camelus](https://github.com/camelus-hq/camelus), der Flutter-basierte Nostr-Client, mergte diese Woche 5 PRs, die auf eine [Riverpod-v3-API-Migration](https://github.com/camelus-hq/camelus/pull/158) und ein [generisches Feed-Refactoring](https://github.com/camelus-hq/camelus/pull/159) zentriert sind. Ein [eingebetteter Notizen-Cache](https://github.com/camelus-hq/camelus/pull/161) vermeidet redundante Relay-Abrufe für zitierte Notizen.

## NIP-Updates

Aktuelle Änderungen am [NIPs-Repository](https://github.com/nostr-protocol/nips):

**Gemergt:**

- **[NIP-85: Service-Provider-Auffindbarkeit](https://github.com/nostr-protocol/nips/pull/2223)**: vitorpamplona fügte Hinweise zur Client-Discovery von [NIP-85 Trusted Assertions](/de/topics/trusted-relay-assertions/)-Service-Providern hinzu, einschließlich Relay-Hints und algorithmusspezifischer Service-Schlüssel. Siehe den [Deep Dive unten](#nip-deep-dive-nip-85-trusted-assertions) für vollständige Berichterstattung.

- **[NIP-11: Relay-Informations-Bereinigung](https://github.com/nostr-protocol/nips/pull/1946)**: fiatjaf entfernte `privacy_policy`, das `retention`-Array, `relay_countries` und den Community-Präferenz-Block aus [NIP-11](/de/topics/nip-11/). Relay-Betreiber befüllten diese Felder selten, und Clients handelten nicht danach.

- **[NIP-52: Tagesgranularer Timestamp-Tag](https://github.com/nostr-protocol/nips/pull/1752)**: staab fügte einen erforderlichen `D`-Tag zu [NIP-52](/de/topics/nip-52/) zeitbasierten Kalender-Events (kind 31923) hinzu, der den tagesgranularen Unix-Timestamp darstellt, berechnet als `floor(unix_sekunden / 86400)`. Mehrere `D`-Tags decken mehrtägige Events ab und ermöglichen effizientes temporales Indexing ohne Parsing vollständiger Timestamps.

- **[NIP-47: Vereinfachung](https://github.com/nostr-protocol/nips/pull/2210)**: Der Vereinfachungs-PR [in Newsletter #9 diskutiert](/de/newsletters/2026-02-11-newsletter/) mergte diese Woche und entfernte `multi_pay_invoice` und `multi_pay_keysend` aus [NIP-47 (Nostr Wallet Connect)](/de/topics/nip-47/). Siehe [Newsletter #8](/de/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-47-nostr-wallet-connect) für den vollständigen NWC-Protokoll-Deep-Dive.

**Offene PRs und Diskussionen:**

- **[NIP-74: Podcasts](https://github.com/nostr-protocol/nips/pull/2211)**: In [Newsletter #8](/de/newsletters/2026-02-04-newsletter/) behandelt, erlebte dieser Podcast-Spezifikationsvorschlag diese Woche hitzige Diskussionen. staab wies darauf hin, dass mindestens drei konkurrierende Podcast-Standards bereits in freier Wildbahn existieren, und derekross verwies auf eine bestehende sechsmonatige Implementierung mit aktiven Apps und Podcasts. Der Weg nach vorne erfordert Konvergenz zwischen Implementierungen, bevor eine NIP-Nummer zugewiesen werden kann.

- **[NIP-XX: KI-Agenten-Nachrichten](https://github.com/nostr-protocol/nips/pull/2226)**: joelklabo schlägt ein vollständiges KI-Agenten-Kommunikationsprotokoll mit Event-Kinds für Prompts, Antworten, Streaming, Tool-Telemetrie, Fehler und Fähigkeits-Discovery vor. Siehe [Neuigkeiten-Abschnitt](#ki-agenten-nips-erscheinen) für Berichterstattung zu allen KI-Vorschlägen dieser Woche.

- **[NIP-PNS: Privater Notizen-Speicher](https://github.com/nostr-protocol/nips/pull/1893)**: jb55s privates Notizen-System definiert kind-1080-Events zur Speicherung verschlüsselter persönlicher Notizen auf Relays, ohne preiszugeben, wer sie geschrieben hat. Das Schema leitet ein deterministisches pseudonymes Schlüsselpaar aus dem nsec des Nutzers via HKDF ab: `pns_key = hkdf_extract(ikm=device_key, salt="nip-pns")`, dann wird ein secp256k1-Schlüsselpaar aus diesem abgeleiteten Schlüssel generiert. Eine zweite Ableitung produziert einen symmetrischen Verschlüsselungsschlüssel: `pns_nip44_key = hkdf_extract(ikm=pns_key, salt="nip44-v2")`. Innere Notizen werden mit [NIP-44](/de/topics/nip-44/) v2 mit diesem Schlüssel verschlüsselt und unter dem pseudonymen pubkey veröffentlicht, sodass Relays kind-1080-Events von einer Identität sehen, die nicht mit dem Hauptschlüssel des Nutzers verknüpft ist. Anders als [NIP-59](/de/topics/nip-59/) Gift Wraps ist PNS nicht spam-anfällig (der pseudonyme Schlüssel ist deterministisch, nicht zufällig) und trägt keine öffentlichen Metadaten (keine `p`-Tags erforderlich, da es keinen Empfänger gibt). Diese Woche veröffentlichte jb55 Erkenntnisse aus der PNS-Implementierung in Notedecks Rust-Backend (`enostr::pns`-Modul). Er identifizierte, dass der `hkdf_extract`-Aufruf der Spezifikation mehrdeutig ist, weil RFC-5869-HKDF zwei Phasen (Extract und Expand) hat, die unterschiedliche Ausgaben produzieren, und die meisten Bibliotheken beide erwarten. Er stellte klar, dass `pns_nip44_key` NIP-44s normalen ECDH-Schlüsselaustausch umgeht und direkt als Konversationsschlüssel verwendet wird – ein Detail, das Implementierer kennen müssen, da die meisten NIP-44-Bibliotheken standardmäßig ECDH verwenden. Er flaggte auch eine undefinierte Variable in der Referenzimplementierung in TypeScript. Der PR, ursprünglich aus April 2025, wird nun aktiv implementiert.

- **[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220)**: pablof7z definiert vier Event-Kinds für Agenten-Identität auf Nostr, aus seiner Arbeit an [TENEX](https://github.com/tenex-chat/tenex) herleitet. Die Basisvorlage ist kind 4199 (Agent Definition), mit Titel, Rollenbeschreibung, Systemanweisungen, Tool-Deklarationen und Version. Verhaltensmodifikatoren leben in kind 4201 (Agent Nudge), das `only-tool`-, `allow-tool`- und `deny-tool`-Tags für Laufzeit-Fähigkeitskontrolle verwendet. Agenten veröffentlichen, was sie lernen, als kind-4129 (Agent Lesson)-Events, kategorisiert und zurückverknüpft zur übergeordneten Definition via `e`-Tags, verfeinerbar durch [NIP-22](/de/topics/nip-22/)-Kommentar-Threads. Eigentümerschaftsverifikation verwendet kind 14199, ein ersetzbares Event, bei dem menschliche Betreiber ihre Agenten-pubkeys auflisten und damit eine bidirektionale Kette etablieren, wenn sie mit dem `p`-Tag des kind-0-Profils des Agenten abgeglichen werden.

- **[NIP-AD: MCP-Server- und Skill-Ankündigungen](https://github.com/nostr-protocol/nips/pull/2221)**: pablof7z definiert Events zur Ankündigung von [Model Context Protocol](https://modelcontextprotocol.io/)-Servern und einzelnen Skills auf Nostr. MCP-Server-Ankündigungen tragen die Endpunkt-URL und die unterstützte Protokollversion zusammen mit einer Liste verfügbarer Tools mit ihren Eingabe-Schemata. [NIP-22](/de/topics/nip-22/)-Kommentare werden auf Server-Ankündigungen unterstützt, sodass die Community MCP-Server direkt auf Nostr diskutieren und bewerten kann.

- **[NIP-73: OSM-Tag-Kind](https://github.com/nostr-protocol/nips/pull/2224)**: DestBro schlägt vor, OpenStreetMap-Identifikatoren zu [NIP-73 (Externe Inhalts-IDs)](/de/topics/nip-73/) hinzuzufügen, das standardisiert, wie Nostr-Events externe Inhalte wie Bücher (ISBN), Filme (ISAN), Podcast-Feeds (GUID), Geohashes und URLs via `i`- und `k`-Tags referenzieren. Der vorgeschlagene OSM-Kind würde Events ermöglichen, spezifische Kartenfunktionen (Gebäude, Straßen, Parks) durch ihre OpenStreetMap-Knoten- oder Weg-ID zu referenzieren und Nostr-Inhalte mit der offenen geografischen Datenbank zu verbinden.

- **[NIP-XX: Responsive Image Variants](https://github.com/nostr-protocol/nips/pull/2219)**: woikos schlägt vor, [NIP-94](/de/topics/nip-94/)-Dateimetadaten-Events um Tags für responsive Bildvarianten in verschiedenen Auflösungen zu erweitern. Clients könnten die geeignete Variante basierend auf Displaygröße und Netzwerkbedingungen auswählen und so die Bandbreite für mobile Nutzer reduzieren, die hochauflösende Bilder auf [Blossom](/de/topics/blossom/)-Servern betrachten.

## NIP Deep Dive: NIP-85 (Trusted Assertions)

[NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md) definiert ein System zur Delegation aufwändiger Berechnungen an vertrauenswürdige Service Provider, die signierte Ergebnisse als Nostr-Events veröffentlichen. Web-of-Trust-Scores und Engagement-Metriken erfordern das Crawlen vieler Relays und die Verarbeitung großer Event-Mengen – Arbeit, die auf Mobilgeräten nicht praktikabel ist. Der dieswöchige [Merge](https://github.com/nostr-protocol/nips/pull/2223) fügte Hinweise zum Client-Discovery-Prozess für diese Provider hinzu.

**Delegation:**

Die Berechnung des Web-of-Trust-Scores eines Nutzers erfordert das Crawlen von Follow-Graphen mehrere Hops tief über viele Relays hinweg, und die Berechnung genauer Follower-Zahlen bedeutet Deduplizierung über das gesamte Relay-Netzwerk. Mobilgeräte und Browser-Clients können diese Operationen nicht durchführen, doch die Ergebnisse sind für Spam-Filterung und Inhalts-Ranking unerlässlich. NIP-85 überbrückt diese Lücke, indem Nutzern ermöglicht wird, vertrauenswürdigen Providern die Berechnungen zu übertragen, die die Ergebnisse als Standard-Nostr-Events veröffentlichen.

**Protokoll-Design:**

NIP-85 verwendet vier Event-Kinds für Aussagen über verschiedene Subjekttypen. Nutzer-Aussagen (kind 30382) tragen Follower-Anzahl, Post-/Antwort-/Reaktions-Zähler, Zap-Beträge, normalisierten Rang (0-100), häufige Themen und aktive Stunden:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30382,
  "tags": [
    ["d", "e88a691e98d9987c964521dff60025f60700378a4879180dcbbb4a5027850411"],
    ["rank", "89"],
    ["followers", "4521"],
    ["first_created_at", "1609459200"],
    ["post_cnt", "1283"],
    ["reply_cnt", "647"],
    ["reactions_cnt", "8920"],
    ["zap_amt_recd", "850000"],
    ["zap_amt_sent", "320000"],
    ["zap_cnt_recd", "412"],
    ["zap_cnt_sent", "198"],
    ["zap_avg_amt_day_recd", "1150"],
    ["zap_avg_amt_day_sent", "430"],
    ["reports_cnt_recd", "2"],
    ["reports_cnt_sent", "0"],
    ["t", "nostr"],
    ["t", "bitcoin"],
    ["active_hours_start", "14"],
    ["active_hours_end", "22"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Event-Aussagen (kind 30383) bewerten einzelne Notizen mit Kommentarzahl, Zitatanzahl, Reposts, Reaktionen und Zap-Daten:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30383,
  "tags": [
    ["d", "<target event id>"],
    ["rank", "72"],
    ["comment_cnt", "45"],
    ["quote_cnt", "12"],
    ["repost_cnt", "89"],
    ["reaction_cnt", "310"],
    ["zap_cnt", "23"],
    ["zap_amount", "125000"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Für adressierbare Events (Langform-Artikel, Wiki-Seiten) wendet kind 30384 dieselben Engagement-Metriken kollektiv auf alle Versionen an. Kind 30385 bewertet externe Identifikatoren (Bücher, Filme, Websites, Orte, Hashtags), die über [NIP-73 (Externe Inhalts-IDs)](/de/topics/nip-73/) referenziert werden und standardisiert, wie Nostr-Events externe Inhalte via `i`- und `k`-Tags referenzieren:

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30385,
  "tags": [
    ["d", "isbn:9780765382030"],
    ["k", "isbn"],
    ["rank", "94"],
    ["comment_cnt", "67"],
    ["reaction_cnt", "203"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

Jede Aussage ist ein ersetzbares adressierbares Event, bei dem der `d`-Tag das Subjekt enthält: einen pubkey, eine Event-ID, eine Event-Adresse oder einen NIP-73-Identifikator. Service Provider signieren diese Events mit ihren eigenen Schlüsseln, und Clients bewerten sie basierend auf Vertrauensbeziehungen.

**Provider-Discovery:**

Nutzer erklären, welchen Assertion-Providern sie vertrauen, indem sie kind-10040-Events veröffentlichen. Jeder Eintrag spezifiziert den Assertion-Typ mit dem Provider-pubkey und Relay-Hint sowie optionalen Algorithmusvarianten:

```json
{
  "id": "<event hash>",
  "pubkey": "<user pubkey>",
  "created_at": 1739836800,
  "kind": 10040,
  "tags": [
    ["30382:rank", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30382:rank", "3d842afe...", "wss://nostr.wine"],
    ["30382:zap_amt_sent", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30383:rank", "4fd5e210...", "wss://nip85.nostr.band"]
  ],
  "content": "",
  "sig": "<user signature>"
}
```

Nutzer können die Tag-Liste in `.content` mit [NIP-44](/de/topics/nip-44/) verschlüsseln, um ihre Provider-Präferenzen privat zu halten. Clients erstellen eine Provider-Liste, indem sie prüfen, welchen Providern ihre gefolgten Accounts vertrauen, und schaffen so eine dezentrale Reputationsschicht für die Assertion-Provider selbst.

**Sicherheitsmodell:**

Provider müssen für unterschiedliche Algorithmen verschiedene Service-Schlüssel verwenden und einen eindeutigen Schlüssel pro Nutzer, wenn Algorithmen personalisiert sind, um Kreuz-Korrelation von Anfragen über Nutzer hinweg zu verhindern. Jeder Service-Schlüssel erhält ein kind-0-Metadaten-Event, das das Verhalten des Algorithmus beschreibt und Nutzern Transparenz darüber gibt, wem sie vertrauen. Assertion-Events sollten nur aktualisiert werden, wenn sich die zugrunde liegenden Daten tatsächlich ändern, um unnötigen Relay-Traffic zu verhindern und Clients zu ermöglichen, Ergebnisse zuverlässig zu cachen.

**Aktuelle Adoption:**

NIP-85 formalisiert ein Muster, das informell bereits entsteht. Primals Cache-Server berechnet Engagement-Metriken und Web-of-Trust-Scores. [Antiprimal](https://gitlab.com/soapbox-pub/antiprimal), in [Newsletter #9](/de/newsletters/2026-02-11-newsletter/#antiprimal-standardkonformes-gateway-zu-primals-cache) behandelt, überbrückt diese Berechnungen zu Standard-Nostr-Clients mittels NIP-85 Event-Kinds. [Nostr.band](https://nostr.band) betreibt das `wss://nip85.nostr.band`-Relay, das in den Beispielen der Spezifikation selbst referenziert wird, und stellt Assertion-Events für seine Suchindex-Daten bereit. Auf der Client-Seite hat [Amethyst](https://github.com/vitorpamplona/amethyst) (verfasst von vitorpamplona, der auch dieses NIP schrieb) experimentelle Trusted-Assertions-Unterstützung in seiner `quartz`-Bibliothek, die Assertion-Events und Service-Provider-Deklarationen parst. [Vertex](https://vertexlab.io) berechnet ähnliche Web-of-Trust-Metriken, [wählte jedoch einen anderen Ansatz](https://vertexlab.io/blog/dvms_vs_nip_85/), eine direkte API statt NIP-85-Events, unter Berufung auf das Discovery-Problem und den Berechnungsaufwand assertion-basierter Architekturen. Mit NIP-85 kann jeder Client Aussagen von jedem Provider durch ein Standard-Event-Format konsumieren, und Provider konkurrieren auf Genauigkeit, während Nutzer wählen, wem sie vertrauen.

## NIP Deep Dive: NIP-52 (Kalender-Events)

[NIP-52](https://github.com/nostr-protocol/nips/blob/master/52.md) definiert Kalender-Events auf Nostr und gibt Clients eine standardisierte Möglichkeit, Ereignisse zu bestimmten Zeitpunkten oder zwischen Zeitpunkten darzustellen und zu entdecken. Der dieswöchige [D-Tag-Merge](https://github.com/nostr-protocol/nips/pull/1752) fügte tagesgranulares Indexing hinzu und schloss eine fehlende Lücke in der Abfrage-Infrastruktur der Spezifikation.

**Zwei Event-Typen:**

NIP-52 trennt Kalender-Events in zwei Kinds basierend auf zeitlicher Präzision. Datumsbasierte Events (kind 31922) repräsentieren ganztägige Ereignisse wie Feiertage oder mehrtägige Festivals. Sie verwenden ISO-8601-Datumsstrings in ihren `start`- und optionalen `end`-Tags ohne Zeitzonen-Berücksichtigung:

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1735689600,
  "kind": 31922,
  "content": "Annual celebration of Bitcoin's genesis block",
  "tags": [
    ["d", "bitcoin-independence-day-2026"],
    ["title", "Bitcoin Independence Day"],
    ["start", "2026-01-03"],
    ["end", "2026-01-04"],
    ["location", "Worldwide"],
    ["g", "u4pruydqqv"],
    ["t", "bitcoin"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["r", "https://bitcoinindependenceday.com"]
  ],
  "sig": "<event creator signature>"
}
```

Zeitbasierte Events (kind 31923) repräsentieren spezifische Momente mit Unix-Timestamps in ihren `start`- und optionalen `end`-Tags sowie IANA-Zeitzonen-Identifikatoren (`start_tzid`, `end_tzid`) für die Darstellung. Beide Kinds sind parametrisiert ersetzbare Events, sodass Veranstalter Details aktualisieren können, indem sie ein neues Event mit demselben `d`-Tag veröffentlichen.

**Kalender und RSVPs:**

Kind-31924-Events definieren Kalender als Sammlungen und referenzieren Events via `a`-Tags, die auf kind-31922- oder kind-31923-Events durch ihre Adresskoordinaten zeigen:

```json
{
  "id": "<event hash>",
  "pubkey": "<calendar owner pubkey>",
  "created_at": 1739836800,
  "kind": 31924,
  "content": "Nostr community events worldwide",
  "tags": [
    ["d", "nostr-community-calendar"],
    ["title", "Nostr Community Events"],
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["a", "31922:<organizer-pubkey>:bitcoin-independence-day-2026"]
  ],
  "sig": "<calendar owner signature>"
}
```

Nutzer können mehrere Kalender pflegen (persönlich, Arbeit, Community), und Clients können Kalender von spezifischen pubkeys abonnieren. Kalender-Events können einen `a`-Tag enthalten, der einen Kalender referenziert, um die Aufnahme anzufordern, und ermöglichen so kollaboratives Kalender-Management, bei dem mehrere Nutzer Events zu Kalendern beitragen, die ihnen nicht gehören.

RSVPs verwenden kind 31925, bei dem Nutzer ihren Teilnahme-Status zusammen mit einem optionalen Frei-/Belegt-Indikator veröffentlichen:

```json
{
  "id": "<event hash>",
  "pubkey": "<attendee pubkey>",
  "created_at": 1739836800,
  "kind": 31925,
  "content": "Looking forward to it",
  "tags": [
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["e", "<kind 31923 event id>", "wss://relay.example.com"],
    ["d", "<unique-rsvp-id>"],
    ["status", "accepted"],
    ["fb", "busy"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com"]
  ],
  "sig": "<attendee signature>"
}
```

Gültige `status`-Werte sind "accepted", "declined", "tentative", und der optionale `fb`-Tag markiert den Nutzer als frei oder belegt für diesen Zeitraum. RSVP-Events referenzieren den `a`-Tag des Kalender-Events und tragen den `p`-Tag des Veranstalters, sodass der Client des Veranstalters Antworten über Relays hinweg aggregieren kann.

**Die D-Tag-Ergänzung:**

Vor dem dieswöchigen Merge mussten Clients, die Events in einem Datumsbereich abfragen wollten, alle Events eines pubkeys oder Kalenders abrufen und clientseitig filtern. Der neue erforderliche `D`-Tag auf zeitbasierten Events (kind 31923) enthält einen tagesgranularen Unix-Timestamp, berechnet als `floor(unix_sekunden / 86400)`. Mehrtägige Events tragen mehrere `D`-Tags, einen pro Tag. Relays können Events nun nach Tag indexieren und auf gefilterte Anfragen effizient antworten und verwandeln damit ein clientseitiges Filterproblem in eine relay-seitige Index-Abfrage.

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1739836800,
  "kind": 31923,
  "content": "Monthly meetup for Nostr developers in Austin",
  "tags": [
    ["d", "nostr-meetup-2026"],
    ["title", "Nostr Developer Meetup"],
    ["summary", "Talks and demos from local Nostr builders"],
    ["image", "https://example.com/meetup-banner.jpg"],
    ["start", "1740067200"],
    ["end", "1740078000"],
    ["start_tzid", "America/New_York"],
    ["end_tzid", "America/New_York"],
    ["D", "20139"],
    ["location", "Bitcoin Commons, Austin TX"],
    ["g", "9v6knb2pg"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["p", "<speaker-pubkey>", "wss://relay.example.com", "speaker"],
    ["t", "nostr"],
    ["t", "meetup"],
    ["r", "https://bitcoincommons.com"]
  ],
  "sig": "<event creator signature>"
}
```

Der `D`-Wert `20139` entspricht `floor(1740067200 / 86400)` und platziert dieses Event auf den 20. Februar 2025. Clients, die „alle Events diese Woche" abfragen, senden einen Filter mit dem entsprechenden `D`-Bereich, und Relays geben nur passende Events zurück.

**Design-Entscheidungen:**

NIP-52 lässt wiederkehrende Events bewusst weg. Die Spezifikation lässt Wiederholungsregeln (RRULE aus iCalendar) vollständig aus und delegiert diese Komplexität an Clients. Ein Veranstalter veröffentlicht individuelle Events für jedes Vorkommen und hält das relay-seitige Datenmodell einfach. Teilnehmer-Tags tragen optionale Rollen ("host", "speaker", "attendee"), und Standort-Tags können Geohash-`g`-Tags für räumliche Abfragen neben menschenlesbaren Adressen enthalten.

**Implementierungen:**

[Flockstr](https://github.com/zmeyer44/flockstr) ist der primäre Kalender-Client, der auf NIP-52 aufgebaut ist. [Coracle](https://gitea.coracle.social/coracle/coracle) zeigt Kalender-Events in seinem sozialen Feed an. Die `D`-Tag-Ergänzung dieser Woche ermöglicht relay-seitiges temporales Indexing, das beide Clients nutzen können, um die Bandbreite beim Abfragen von Events in einem bestimmten Datumsbereich zu reduzieren.

---

Das war's für diese Woche. Wer etwas baut, Neuigkeiten hat oder sein Projekt vorgestellt sehen möchte, kann sich <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">per [NIP-17](/de/topics/nip-17/) DM an uns wenden</a> oder uns auf Nostr finden.
