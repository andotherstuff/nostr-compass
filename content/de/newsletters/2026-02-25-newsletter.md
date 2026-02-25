---
title: 'Nostr Compass #11'
date: 2026-02-25
translationOf: /en/newsletters/2026-02-25-newsletter.md
translationDate: 2026-02-25
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, deinem wöchentlichen Wegweiser durch Nostr.

**Diese Woche:** [White Noise v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0) bringt Echtzeit-Messaging und Amber-Signer-Unterstützung mit über 160 gemergten Verbesserungen. [diVine 1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5) behebt Video-Wiedergabeprobleme und fügt Kind-22236-View-Events für Creator-Analytics hinzu. [Pika](https://github.com/sledtools/pika), [Ridestr](https://github.com/variablefate/ridestr) und [Unfiltered](https://github.com/dmcarrington/unfiltered) liefern Updates. [FIPS](https://github.com/jmcorgan/fips) veröffentlicht eine funktionierende Rust-Implementierung von Nostr-nativem Mesh-Networking. Notecrumbs erhält Stabilitäts-Fixes für damus.io-Link-Vorschauen. [ContextVM](https://contextvm.org) verbindet Nostr mit dem Model Context Protocol. Neue Projekte umfassen [Burrow](https://github.com/CentauriAgent/burrow) für MLS-verschlüsseltes Messaging zwischen KI-Agenten und Menschen sowie [Nostria Signer](https://github.com/nostria-app/nostria-signer-extension) für browserbasierte Vault- und Identitätsverwaltung. Die Deep Dives dieser Woche behandeln NIP-55 Android-Signing und NIP-60 Cashu-Wallet-Synchronisierung.

## Neuigkeiten

### Notecrumbs Stabilitätsverbesserungen

[Notecrumbs](https://github.com/damus-io/notecrumbs), der Nostr-API- und Webserver, der damus.io-Link-Vorschauen antreibt, erhielt eine Reihe von Fixes für Zuverlässigkeitsprobleme.

Ein [Nebenläufigkeits-Fix](https://github.com/damus-io/notecrumbs/commit/3f201f63ea49) ersetzte den Inflight-Deduplizierungsmechanismus durch Watch-Channels. Zwei Aufrufer, die dieselbe Notiz anforderten, konnten beide zu Fetchern werden, was zu einem Deadlock führte, wenn einer abschloss, bevor der andere die Benachrichtigung abonniert hatte. Watch-Channels mit atomaren Operationen stellen sicher, dass nur ein Fetcher läuft, während andere auf das Ergebnis warten.

[Rate-Limiting](https://github.com/damus-io/notecrumbs/commit/b0d0bf5a2f17) implementiert eine zweischichtige Verteidigung gegen Relay-Hammering. Wenn Nutzer wiederholt auf dieselbe Notiz zugreifen, entprellt das System nun Relay-Anfragen mit einem 5-Minuten-Cooldown-Fenster. Dieser Schutz erstreckt sich auf alle [NIP-19](/de/topics/nip-19/)-Typen und Profil-Feeds und verhindert proportionalen Spam an Relays bei starkem Traffic.

[Performance-Verbesserungen](https://github.com/damus-io/notecrumbs/commit/38670b3972b6) verlagerten sekundäre Datenabrufe in Hintergrund-tokio-Tasks. Seiten rendern nun sofort mit gecachten Daten, statt bei sequenziellen Relay-Timeouts zu blockieren, die bis zu 7,5 Sekunden aufaddieren konnten. Ein Upgrade auf nostrdb 0.10.0 begleitete diese Fixes.

### ContextVM: MCP über Nostr

[ContextVM](https://contextvm.org) ist eine Suite von Werkzeugen, die Nostr und das [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) verbindet. Aktuelle Commits führten die neue [CEP-8](https://docs.contextvm.org/spec/ceps/cep-8/)-Spezifikation ein, die Zahlungen ermöglicht, und trieben im Februar [SDK](https://github.com/ContextVM/sdk)-Verbesserungen voran.

Das SDK stellt TypeScript-Client- und Server-Transports für MCP über Nostr bereit. Entwickler können MCP-Server über das Nostr-Netzwerk exponieren, und Clients verbinden sich mit ihnen, während Relays als blinder Nachrichtenbus verschlüsselte Events weiterleiten. Clients ohne native Nostr-Unterstützung kommen über eine Proxy-Schicht hinein. Die Bibliothek übernimmt Relay-Management und kryptografisches Signing für Event-Authentifizierung und funktioniert sowohl in Node.js- als auch in Browser-Umgebungen.

[CVMI](https://github.com/ContextVM/cvmi) stellt ein CLI für Server-Discovery und Methoden-Aufruf bereit. [Relatr](https://github.com/ContextVM/relatr) berechnet personalisierte Vertrauenswerte aus sozialer Graphdistanz kombiniert mit Profilvalidierung.

ContextVM positioniert sich als Brückenschicht: Bestehende MCP-Server gewinnen Nostr-Interoperabilität und behalten dabei ihre konventionellen Transports.

### White Noise dokumentiert dezentrale Nutzersuche

Ein [Blogbeitrag von jgmontoya](https://blog.jgmontoya.com/2026/02/22/user-search.html) erläutert, wie [White Noise](https://github.com/marmot-protocol/whitenoise) die Nutzersuche über das dezentrale Relay-Netzwerk handhabt.

Die Verteilung von Profilen schafft die Herausforderung: Anders als zentralisierte Messenger mit einheitlichen Datenbanken verteilen sich Nostr-Profile über Dutzende von Relays ohne zentralen Index. White Noise löst dies durch eine Producer-Consumer-Architektur, die parallel läuft.

Ein Producer-Prozess erweitert kontinuierlich den sozialen Graphen ausgehend von den Follows des Nutzers, ruft Follow-Listen in zunehmenden Abständen ab und stellt entdeckte pubkeys zur Profilauflösung in die Warteschlange. Der Consumer löst Treffer durch fünf zunehmend aufwändigere Stufen auf: lokale Nutzertabelle (schnellste), gecachte Profile aus vorherigen Suchen, verbundene Relays, Nutzer-Relay-Listen gemäß [NIP-65](/de/topics/nip-65/) und direkte Abfragen an nutzerdeklarierten Relays (langsamste).

Kalte Suchen dauern etwa 3 Sekunden, während warme Suchen aus dem Cache auf rund 10 Millisekunden fallen. Für neue Nutzer ohne etablierte soziale Graphen injiziert das System gut vernetzte Bootstrap-Knoten, um die Suchfunktion sicherzustellen. Gruppenmitgliedschaft liefert ein implizites soziales Signal neben expliziten Follows.

Instrumentierung erwies sich laut Autor als entscheidend für die Optimierung. Ohne Metriken war Verbesserung reines Raten.

### FIPS: Nostr-natives Mesh-Networking

[FIPS](https://github.com/jmcorgan/fips) (Free Internetworking Peering System) ist eine funktionierende Rust-Implementierung eines selbstorganisierenden Mesh-Netzwerks, das Nostr-Schlüsselpaare (secp256k1) als Knotenidentitäten verwendet. Die [Design-Dokumentation](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md) begleitet funktionalen Code.

Das Protokoll adressiert Infrastruktur-Unabhängigkeit: Knoten entdecken sich automatisch ohne zentrale Server oder Zertifizierungsstellen. Ein Spanning-Tree bietet koordinatenbasiertes Routing, während bloom filter Erreichbarkeitsinformationen verbreiten und Knoten Weiterleitungsentscheidungen mit rein lokalem Wissen treffen lassen. Transport-Agnostizismus bedeutet, dass dasselbe Protokoll über UDP, Ethernet, Bluetooth, LoRa-Radio oder jedes datagrammfähige Medium funktioniert.

Zwei Verschlüsselungsschichten schützen den Traffic. Link-Layer-Verschlüsselung (Noise-IK-Muster) sichert Hop-für-Hop-Kommunikation zwischen Nachbarn mit gegenseitiger Authentifizierung und Forward Secrecy. Session-Layer-Verschlüsselung (Noise-XK-Muster) bietet Ende-zu-Ende-Schutz gegen Zwischenrouter, wobei nur das Ziel die Nutzlast entschlüsseln kann. Dies spiegelt wider, wie TLS HTTP-Traffic schützt, auch wenn er nicht vertrauenswürdige Netzwerke traversiert.

Die Architektur verwendet einen "Greedy Embedding"-Spanning-Tree für das Routing. Jeder Knoten erhält Koordinaten basierend auf seiner Position relativ zur Baumwurzel und dem Elternknoten. Pakete werden gierig zu Koordinaten weitergeleitet, die dem Ziel näher sind, wobei bloom filter erreichbare Endpunkte bekannt machen. Wenn gieriges Routing versagt (lokale Minima), können Knoten auf baumbasierte Pfade zurückfallen.

Die Rust-Implementierung umfasst bereits UDP-Transport mit bloom-filter-basierter Discovery. Zukünftige Arbeit zielt auf Nostr-Relay-Integration für Peer-Bootstrapping.

## Releases

Diese Woche brachte Releases bei Relay-Infrastruktur und Client-Anwendungen, wobei auch neue Projekte in den Bereich eintraten.

### HAVEN v1.2.0

[HAVEN](https://github.com/bitvora/haven), das All-in-One-Persönlichkeitsrelay, das vier Relay-Funktionen mit einem [Blossom](/de/topics/blossom/)-Medienserver bündelt, lieferte [v1.2.0](https://github.com/bitvora/haven/releases/tag/v1.2.0). Dieser Release verlässt die RC-Phase, die [letzte Woche behandelt wurde](/de/newsletters/2026-02-18-newsletter/#haven-v120-rc3).

Multi-npub-Unterstützung erlaubt es einer einzigen HAVEN-Instanz, mehrere Nostr-Identitäten durch Whitelisting zu bedienen, mit neuer Blacklisting-Funktionalität für Zugangskontrolle. Das Backup-System wurde neu geschrieben: Es verwendet das portable JSONL-Format, und ein `haven restore`-Befehl importiert Notizen aus diesen Dateien. Cloud-Storage-Integration fügt `--to-cloud`- und `--from-cloud`-Flags für Remote-Backup-Management hinzu.

[Web-of-Trust](/de/topics/web-of-trust/)-Verbesserungen umfassen konfigurierbare Tiefenebenen für Vertrauensberechnungen und automatische 24-Stunden-Aktualisierungsintervalle mit Lock-freier Optimierung zur Reduzierung des Speicher-Overheads. Nutzeragent-Konfiguration für Relay-Anfragen und konfigurierbare Blastr-Timeout-Einstellungen runden den Release ab, zusammen mit Datenexport in komprimiertes JSONL.

### White Noise v0.3.0

[White Noise](https://github.com/marmot-protocol/whitenoise), die [MLS](/de/topics/mls/)-basierte verschlüsselte Messaging-App, die das [Marmot](/de/topics/marmot/)-Protokoll implementiert, lieferte [v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0) mit über 160 gemergten Verbesserungen.

Dieser Release bringt Echtzeit-Messaging durch Streaming-Verbindungen statt Polling, sodass Nachrichten sofort ankommen. Amber-Unterstützung ([NIP-55](/de/topics/nip-55/)) bedeutet, dass private Schlüssel die App nie berühren müssen. Bild-Sharing funktioniert nun mit Upload-Fortschrittsanzeige und Blurhash-Platzhaltern während des Ladens. Vollbild-Anzeige unterstützt Pinch-to-Zoom.

Gruppen-Messaging erhielt Zuverlässigkeitsverbesserungen mit Chat-Listen, die Absendernamen anzeigen, und [MLS](/de/topics/mls/)-Verschlüsselung stellt Forward Secrecy sicher. Die Nutzersuche erweitert sich von Follows bis zu vier Trennungsgraden, mit Ergebnissen, die beim Auffinden eingestreamt werden.

Eine Breaking-Change setzt bei einem Upgrade alle lokalen Daten zurück aufgrund von Marmot-Protokolländerungen und dem Wechsel zu verschlüsseltem lokalen Speicher. Nutzer sollten nsec-Schlüssel vor dem Upgrade sichern.

### diVine 1.0.5

[diVine](https://github.com/divinevideo/divine-mobile), der Kurzform-Looping-Video-Client auf der Basis restaurierter Vine-Archive, lieferte [1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5) mit umfangreichen Video-Wiedergabe-Fixes und einem neuen dezentralen Analytics-System.

Video-Wiedergabeprobleme dominierten die Fixes: Phantom-Pause, doppelter Ton zwischen Videos, schwarzer Blitz zwischen Thumbnails und ersten Frames sowie Abstürze durch verworfene Player sind alle behoben. Ein gepoolter Video-Player übernimmt nun den Home-Feed für konsistente Wiedergabe.

Kind-22236-ephemere View-Events ermöglichen Creator-Analytics und Empfehlungen. Das System verfolgt Traffic-Quellen (Home, Discovery-Varianten, Profil, Share, Suche) und Loop-Zählungen und filtert dabei Eigenaufrufe heraus. Lokale Dateipfad-Leaks in Nostr-Event-imeta-Tags werden mit kanonischen Blossom-URLs behoben, die clientseitig gemäß BUD-01-Spezifikation konstruiert werden.

[NIP-46](/de/topics/nip-46/)-Remote-Signer-Verbesserungen umfassen parallelisierte Relay-Verbindungen und Callback-URL-Unterstützung. Android stellt WebSocket-Verbindungen beim App-Resume nach Signer-Genehmigung wieder her.

### Coracle 0.6.30

[Coracle](https://github.com/coracle-social/coracle), der webbasierte Nostr-Client mit Fokus auf Relay-Management und [Web-of-Trust](/de/topics/web-of-trust/)-Moderation, lieferte [0.6.30](https://github.com/coracle-social/coracle/releases/tag/0.6.30) mit Video-Thumbnail-Unterstützung, was das Medien-Browsing in Feeds verbessert. Ebenfalls aktualisiert:

### Nostur v1.26.0

[Nostur](https://github.com/nostur-com/nostur-ios-public), der iOS-Nostr-Client, lieferte [v1.26.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.26.0) mit einem neuen Live-Streams-Feed-Bereich und einem neu gestalteten Einstellungsbildschirm. GIFs können nun auf Blossom-Medienservern gehostet werden, was die Abhängigkeit von zentralisierten Diensten reduziert. Klipy-GIFs-Integration bietet einen Fallback, wenn Tenor nicht verfügbar ist. Jahresüberschriften in DM-Gesprächen und Anzeige der Erwähnungsanzahl runden die nutzerseitigen Änderungen ab.

Entwickler-Werkzeuge und CLI-Apps erhielten diese Woche ebenfalls Updates.

### nak v0.18.5

[nak](https://github.com/fiatjaf/nak), fiatjafs Kommandozeilen-Schweizer-Taschenmesser für Nostr, lieferte [v0.18.5](https://github.com/fiatjaf/nak/releases/tag/v0.18.5) mit einem neuen `nak profile`-Unterbefehl zum Abrufen und Anzeigen von Nutzerprofilen. Der `git clone`-Befehl unterstützt nun [NIP-05](/de/topics/nip-05/)-Namen in `nostr://`-URIs und ermöglicht das Klonen von Repositories über menschenlesbare Identifikatoren. Zwei weitere Projekte lieferten ebenfalls Releases:

### Pika v0.5.3

[Pika](https://github.com/sledtools/pika), der [MLS](/de/topics/mls/)-verschlüsselte Messenger für iOS, Android und Desktop, der auf dem [Marmot](/de/topics/marmot/)-Protokoll aufgebaut ist, lieferte [v0.5.3](https://github.com/sledtools/pika/releases/tag/pikachat-v0.5.3). Aktuelle Commits fügen Datei-Upload und Drag-and-Drop-Medienunterstützung für die Desktop-App hinzu, neben Cloudflare-Workers-Deployment-Fixes.

Pika verwendet einen Rust-Kern, der die gesamte Geschäftslogik besitzt, während iOS (SwiftUI) und Android (Kotlin) als schlanke UI-Schichten fungieren, die Zustands-Snapshots rendern. MDK (Marmot Development Kit) stellt die MLS-Implementierung bereit. Das Projekt weist auf Alpha-Status hin und warnt vor dem Einsatz für sensible Workloads.

### Ridestr v0.2.6

[Ridestr](https://github.com/variablefate/ridestr), die dezentrale Mitfahrplattform mit Cashu-Zahlungen, lieferte [v0.2.6](https://github.com/variablefate/ridestr/releases/tag/v0.2.6). Dieser Release behebt TalkBack-Barrierefreiheitsprobleme und löst Bugs, bei denen Fahrer von der Nearby-Liste verschwanden, wenn sie die Zahlungsmethode wechselten, oder bei denen ausgewählte Fahrerzählungen nicht aktualisierten, wenn Fahrer offline gingen.

Das "Send to All"-Feature heißt nun "Broadcast RoadFlare" mit Fixes für stille Fehler bei frischen Fahrer-Installationen. Ridestr implementiert HTLC-Escrow für vertrauenslose Fahrtbezahlungen und [NIP-60](/de/topics/nip-60/)-Wallet-Sync über Geräte hinweg.

### Unfiltered v1.0.6

[Unfiltered](https://github.com/dmcarrington/unfiltered), die Instagram-ähnliche Foto-Sharing-App für Android, lieferte [v1.0.6](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.6) mit verbesserter Nutzersuche und automatischer Relay-Wiederverbindung alle 60 Sekunden.

Mit Kotlin und Jetpack Compose gebaut, verwendet Unfiltered rust-nostr-Bindings und Blossom-kompatible Server für Bild-Hosting. Amber-Integration ([NIP-55](/de/topics/nip-55/)) übernimmt sicheres Schlüsselmanagement. Die App zeigt Beiträge von gefolgten Accounts in chronologischer Reihenfolge ohne Algorithmen oder Werbung.

Diese Woche starteten auch zwei neue Messaging- und Signing-Projekte.

### Burrow: MLS-Messaging für KI-Agenten

[Burrow](https://github.com/CentauriAgent/burrow) ist ein Messenger, der das [Marmot](/de/topics/marmot/)-Protokoll für MLS-verschlüsselte Kommunikation ohne Telefonnummern oder zentralisierte Server implementiert. Sowohl menschliche Nutzer als auch KI-Agenten können teilnehmen.

Ein reiner Rust-CLI-Daemon mit JSONL-Ausgabemodus übernimmt die Integration mit automatisierten Systemen. Eine Flutter-Cross-Platform-App deckt Android, iOS, Linux, macOS und Windows ab. Medienanhänge werden zusammen mit Nachrichten verschlüsselt, und WebRTC übernimmt Audio- und Videoanrufe mit konfigurierbaren TURN-Servern.

Burrow schichtet MLS-Verschlüsselung auf Nostr-Infrastruktur. Identität verwendet Nostr-Schlüsselpaare (secp256k1), während MLS-KeyPackages als kind-443-Events veröffentlicht werden. Nachrichten verschlüsseln mit [NIP-44](/de/topics/nip-44/) als kind-445-Events, und Willkommenseinladungen verwenden [NIP-59](/de/topics/nip-59/)-Gift-Wrapping.

[OpenClaw](https://openclaw.ai)-Integration ermöglicht KI-Agenten-Beteiligung mit vollem Werkzeugzugang. Zugangskontrolllisten mit Audit-Logging verwalten Kontakt- und Gruppenberechtigungen. Diese Kombination positioniert Burrow für Agent-zu-Agent- und Agent-zu-Mensch-Messaging-Szenarien, die Signal-Level-Verschlüsselung auf dezentraler Infrastruktur erfordern.

### Nostria Signer Extension

[Nostria Signer](https://github.com/nostria-app/nostria-signer-extension) ist eine Chromium-basierte Browser-Erweiterung, die Vault- und Identitätsverwaltung für Nostr-Nutzer bietet.

Mehrere Vaults mit mehreren Accounts erlauben Nutzern, Identitäten für verschiedene Kontexte zu organisieren. Internationalisierung umfasst RTL-Sprachunterstützung. Mit Angular und TypeScript gebaut (79,2 % des Codebases), funktioniert sie sowohl als Browser-Erweiterung als auch als Progressive Web App.

Nostria Signer implementiert [NIP-07](/de/topics/nip-07/) für Browser-Extension-Signing und ermöglicht webbasierten Nostr-Clients, Event-Signaturen anzufordern, ohne direkt auf private Schlüssel zugreifen zu müssen. Automatisierte Wallet-Migration übernimmt Updates, die über den Chrome Web Store verteilt werden. Nutzer können auch aus dem `dist/extension`-Ordner sideloaden.

Entwickler betonen den experimentellen Status: Nutzer müssen ihre eigenen geheimen Wiederherstellungsphrasen verwalten, da die Entwickler keinen Zugang zu verlorenen Schlüsseln wiederherstellen können.

## Projekt-Updates

### Formstr zieht in neue Organisation um

[Formstr](https://github.com/formstr-hq/nostr-forms), die Google-Forms-Alternative auf Nostr, migrierte sein Repository von `abh3po/nostr-forms` zur `formstr-hq`-Organisation. Dieser OpenSats-Stipendienempfänger setzt die Entwicklung am neuen Standort fort.

### Bemerkenswerte offene PRs

Laufende Arbeiten in Nostr-Projekten:

- **Damus Outbox-Modell** ([PR #3602](https://github.com/damus-io/damus/pull/3602)): Implementierungsplan für das Gossip-/Outbox-Relay-Modell auf iOS. Diese Architekturänderung verbessert die Nachrichtenübermittlung durch Veröffentlichung an die Relays, auf denen Empfänger tatsächlich lesen.

- **Notedeck plattformübergreifende Benachrichtigungen** ([PR #1296](https://github.com/damus-io/notedeck/pull/1296)): Natives Benachrichtigungssystem für den Damus-Desktop-Client, das Android FCM, macOS und Linux abdeckt.

- **NDK Cashu v3 Upgrade** ([PR #370](https://github.com/nostr-dev-kit/ndk/pull/370)): Aktualisiert die Wallet-Integration des Nostr Development Kit auf cashu-ts v3.

- **Zeus Cashu Offline** ([PR #3742](https://github.com/ZeusLN/zeus/pull/3742)): Offline-Ecash-Senden und -Empfangen für die Zeus-Lightning-Wallet.

- **Shopstr Encrypted Digital Delivery** ([PR #231](https://github.com/shopstr-eng/shopstr/pull/231)): Fügt verschlüsselte Lieferung für digitale Güter mit dynamischer Gewichtsunterstützung für physische Artikel hinzu.

## NIP-Updates

Aktuelle Änderungen am [NIPs-Repository](https://github.com/nostr-protocol/nips):

**Diese Woche gemergt:**

- **[NIP-85 Service-Provider-Auffindbarkeit](https://github.com/nostr-protocol/nips/pull/2223)**: Die [NIP-85](/de/topics/nip-85/)-Spezifikation enthält nun Hinweise dazu, wie Clients vertrauenswürdige Assertion-Provider entdecken. Wenn ein Client [Web-of-Trust](/de/topics/web-of-trust/)-Scores oder andere berechnete Metriken benötigt, kann er Relays nach kind-30085-Ankündigungen von Providern abfragen, denen der Nutzer bereits folgt oder vertraut.

- **[NIP-29 entfernt unverwaltete Gruppen](https://github.com/nostr-protocol/nips/pull/2229)**: Die [NIP-29](/de/topics/nip-29/)-Gruppen-Chat-Spezifikation strich die Unterstützung für unverwaltete Gruppen (bei denen jedes Mitglied andere hinzufügen konnte). Alle NIP-29-Gruppen erfordern nun relay-seitiges Management mit expliziten Admin-Rollen, was Implementierungen vereinfacht und Spam-Vektoren reduziert.

- **[NIP-11 entfernt veraltete Felder](https://github.com/nostr-protocol/nips/pull/2231)**: [NIP-11](/de/topics/nip-11/)-Relay-Informationsdokumente enthalten nicht mehr die veralteten `software`- und `version`-Felder. Implementierungen sollten diese aus ihren Antworten entfernen.

- **[NIP-39 verschiebt Identity-Tags](https://github.com/nostr-protocol/nips/pull/2227)**: Externe Identitätsansprüche ([NIP-39](/de/topics/nip-39/) `i`-Tags für GitHub, Twitter usw.) wurden von kind-0-Profilen in dedizierte kind-30382-Events verschoben. Dies trennt Identitätsverifizierung von Profil-Metadaten.

**KI-Agenten-NIPs: Fortschritt:**

Vier KI-fokussierte NIPs befinden sich weiterhin in aktiver Entwicklung. Seit der [Berichterstattung der letzten Woche](/de/newsletters/2026-02-18-newsletter/#ki-agenten-nips-erscheinen):

- **[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220)** (aktualisiert 19. Feb): Definiert Agenten-Identität mit kind 4199 für Agenten-Definitionen und kind 4201 für Prompting ("Nudges"). Agenten können [NIP-94](/de/topics/nip-94/)-Datei-Metadaten für erweiterte Beschreibungen referenzieren.

- **[NIP-XX: AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226)** (aktualisiert 18. Feb): Standardisiert konversationelles Messaging mit sieben ephemeren Event-Kinds (25800-25806) für Status, Streaming-Deltas, Prompts, Antworten, Tool-Aufrufe, Fehler und Abbrüche, wobei kind-31340-"AI-Info"-Events Agenten erlauben, unterstützte Modelle und Fähigkeiten anzukündigen.

- **[NIP-AC: DVM Agent Coordination](https://github.com/nostr-protocol/nips/pull/2228)** (geöffnet 18. Feb): Erweitert [NIP-90](/de/topics/nip-90/) für autonome Agenten-Workflows mit Heartbeats für Agenten-Discovery, Job-Reviews für Qualitätsverfolgung, Daten-Escrow für Ergebnisverpflichtung, Workflow-Ketten für mehrstufige Pipelines und Swarm-Bidding für wettbewerbliche Provider-Auswahl. Eine Referenzimplementierung läuft unter 2020117.xyz.

- **[NIP-AD: MCP Server Announcements](https://github.com/nostr-protocol/nips/pull/2221)** (geöffnet 12. Feb): Standardisiert die Ankündigung von Model-Context-Protocol-Servern und Skills auf Nostr. Bereits auf der TENEX-Plattform im Einsatz.

**Weitere offene PRs:**

- **[NIP-144: Service Authorization Protocol](https://github.com/nostr-protocol/nips/pull/2232)**: Definiert, wie Clients Identität und Berechtigungen gegenüber Dienstanbietern auf Nostr nachweisen.

- **[NIP-DC: Nostr Webxdc](https://github.com/nostr-protocol/nips/pull/2230)**: alexgleason schlägt die Integration von Webxdc (dezentralisierte Webanwendungen) mit Nostr-Events vor.

## NIP Deep Dive: NIP-55 (Android Signer Application)

[NIP-55](https://github.com/nostr-protocol/nips/blob/master/55.md) definiert, wie Android-Nostr-Clients kryptografische Operationen von dedizierten Signer-Anwendungen anfordern. Da [White Noise v0.3.0](#white-noise-v030) und [Unfiltered v1.0.6](#unfiltered-v106) diese Woche beide Amber-Unterstützung hinzufügten, ist das Android-Signing-Protokoll eine nähere Betrachtung wert.

**Kommunikationskanäle:**

NIP-55 ermöglicht App-übergreifendes Signing durch zwei Mechanismen. Intents bieten manuelle Nutzergenehmigung mit visuellem Feedback für einmalige Operationen. Content-Resolver ermöglichen automatisiertes Signing, wenn Nutzer dauerhafte Berechtigungen erteilen, und lassen Apps im Hintergrund signieren ohne wiederholte Aufforderungen.

Die Kommunikation verwendet das benutzerdefinierte `nostrsigner:`-URI-Schema. Ein Client initiiert Kontakt mit:

```
nostrsigner:<base64-encoded-event>?type=sign_event&callbackUrl=myapp://callback
```

**Unterstützte Operationen:**

Die Spezifikation definiert sieben kryptografische Methoden: Event-Signing (`sign_event`), Public-Key-Abruf (`get_public_key`), [NIP-04](/de/topics/nip-04/)-Verschlüsselung/-Entschlüsselung, [NIP-44](/de/topics/nip-44/)-Verschlüsselung/-Entschlüsselung und Zap-Event-Entschlüsselung (`decrypt_zap_event`).

**Berechtigungsmodell:**

Clients rufen `get_public_key` einmal auf, um eine Vertrauensbeziehung herzustellen, und erhalten den Paketnamen des Signers und den pubkey des Nutzers. Die Spezifikation schreibt vor, dass Clients diese Werte speichern und `get_public_key` nie wieder aufrufen, um Fingerprinting-Angriffe zu verhindern.

Für Signing-Anfragen können Nutzer einmalig genehmigen oder "Meine Wahl merken" für Hintergrundoperationen erteilen. Wenn Nutzer Operationen konsistent ablehnen, gibt der Signer einen "abgelehnt"-Status zurück und verhindert wiederholte Aufforderungen.

**Implementierungen:**

[Amber](https://github.com/greenart7c3/amber) ist der primäre NIP-55-Signer für Android. Clients mit NIP-55-Unterstützung umfassen [Amethyst](https://github.com/vitorpamplona/amethyst), [White Noise](#white-noise-v030), [Unfiltered](#unfiltered-v106) und andere. Webanwendungen können Signer-Antworten nicht direkt empfangen und müssen Callback-URLs oder Zwischenablagen-Operationen verwenden.

**Verhältnis zu anderen Signing-NIPs:**

NIP-55 ergänzt [NIP-07](/de/topics/nip-07/) (Browser-Erweiterungen) und [NIP-46](/de/topics/nip-46/) (Remote-Signing über Relays). Während NIP-07 Desktop-Browser und NIP-46 geräteübergreifendes Signing abdeckt, bietet NIP-55 native Android-Integration mit minimaler Latenz.

## NIP Deep Dive: NIP-60 (Cashu Wallet)

[NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md) definiert, wie [Cashu](/de/topics/cashu/)-Ecash-Wallets Zustände auf Nostr-Relays speichern und damit anwendungsübergreifende Wallet-Synchronisierung ermöglichen. Da [Ridestr v0.2.6](#ridestr-v026) NIP-60 für Wallet-Sync über Geräte nutzt, verdient das Protokoll eine Betrachtung.

**Event-Kinds:**

NIP-60 verwendet vier Event-Typen. Das ersetzbare kind 17375 speichert Wallet-Konfiguration einschließlich Mint-URLs und eines dedizierten privaten Schlüssels für den Empfang von P2PK-Ecash-Zahlungen. Token-Events (kind 7375) enthalten unverbrauchte kryptografische Beweise, während Ausgabenhistorie (kind 7376) Transaktionen für Nutzertransparenz aufzeichnet. Ein optionales kind 7374 verfolgt Mint-Zahlungsquotes.

**Wallet-Architektur:**

Der Wallet-Zustand lebt auf Relays und ist damit über Anwendungen hinweg zugänglich. Das Wallet-Event eines Nutzers enthält verschlüsselte Referenzen auf Cashu-Mints und einen wallet-spezifischen privaten Schlüssel, der vom Nostr-Identitätsschlüssel des Nutzers getrennt ist. Diese Trennung ist wichtig: Der Wallet-Schlüssel übernimmt Ecash-Operationen, während der Nostr-Schlüssel soziale Funktionen übernimmt.

```json
{
  "kind": 17375,
  "content": "<nip44-encrypted-wallet-config>",
  "tags": [["d", "cashu-wallet"]]
}
```

**Proof-Management:**

Cashu-Beweise sind Inhaberinstrumente. Einmal ausgegeben, wird ein Beweis ungültig. NIP-60 verwaltet dies durch einen Rollover-Mechanismus: Beim Ausgeben erstellen Clients ein neues Token-Event mit verbleibenden unverbrauchten Beweisen und löschen das Original via [NIP-09](/de/topics/nip-09/). Gelöschte Token-IDs kommen in ein `del`-Feld für Zustandsverfolgung.

Clients sollten Beweise regelmäßig gegen Mints validieren, um zuvor ausgegebene Anmeldeinformationen zu erkennen. Mehrere Token-Events pro Mint sind zulässig, und Ausgabenhistorie-Events helfen Nutzern, Transaktionen zu verfolgen, obwohl sie optional sind.

**Sicherheitsmodell:**

Alle sensiblen Daten verwenden [NIP-44](/de/topics/nip-44/)-Verschlüsselung. Der private Wallet-Schlüssel erscheint nie im Klartext. Da Relays verschlüsselte Blobs speichern, ohne deren Inhalt zu verstehen, bleibt der Wallet-Zustand auch auf nicht vertrauenswürdigen Relays privat.

**Implementierungen:**

Wallets mit NIP-60-Unterstützung umfassen [Nutsack](https://github.com/gandlafbtc/nutsack) und [eNuts](https://github.com/cashubtc/eNuts). Clients wie [Ridestr](#ridestr-v026) verwenden NIP-60 für geräteübergreifenden Sync und ermöglichen Nutzern, auf dem Desktop aufzuladen und vom Mobilgerät aus auszugeben, ohne manuelle Überweisungen.

---

Das war's für diese Woche. Wer etwas baut oder Neuigkeiten zu teilen hat: <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Per [NIP-17](/de/topics/nip-17/) DM erreichbar</a> oder auf Nostr findbar.
