---
title: 'Nostr Compass #15'
date: 2026-03-25
translationOf: /en/newsletters/2026-03-25-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, deinem wöchentlichen Wegweiser durch Nostr.

**Diese Woche:** [Primal Android](https://github.com/PrimalHQ/primal-android-app) folgt seinem 3.0-Wallet-Release mit [Follow Packs, Zap-Anreicherung und `primalconnect://`-Deep-Links](#primal-fügt-follow-packs-zap-anreicherung-und-deep-links-hinzu). [BigBrotr](https://github.com/BigBrotr/bigbrotr) veröffentlicht eine [nsec-Leak-Analyse](#bigbrotr-kartiert-exponierte-private-schlüssel-im-relay-netzwerk), die 41 Millionen Events über 1.085 Relays scannt und 16.599 gültige private Schlüssel findet, während [npub.world](https://npub.world) in derselben Woche Leak-Warnungen in Profilseiten integriert. Martti Malmi startet [nostr-vpn](#nostr-vpn-startet-als-tailscale-alternative), eine Tailscale-Alternative, die über Nostr-Relays signalisiert und WireGuard-Tunnel erstellt, und liefert 11 Releases in sieben Tagen. Das [Vector](https://github.com/VectorPrivacy/Vector)-Team [veröffentlicht P2P-DOOM als Open Source](#open-source-doom-läuft-peer-to-peer-über-nostr) über Nostr, [FIPS](https://github.com/jmcorgan/fips) liefert [v0.2.0](#fips-v020-liefert-tor-transport-reproduzierbare-builds-und-sidecar-beispiele), und [Nostrability Schemata](https://github.com/nostrability/schemata) expandiert in einer Woche auf [sechs Sprachen](#nostrability-schemata-wird-mehrsprachig).

## Neuigkeiten

### Primal fügt Follow Packs, Zap-Anreicherung und Deep Links hinzu

[Anschließend an die 3.0.7-Berichterstattung der letzten Woche](/de/newsletters/2026-03-18-newsletter/), [Primal Android](https://github.com/PrimalHQ/primal-android-app) arbeitete diese Woche an Post-Release-Arbeit rund um Onboarding, Composer-UX und Wallet-Kontext. Neu gestaltetes Onboarding führt Follow Packs ein ([PR #949](https://github.com/PrimalHQ/primal-android-app/pull/949)), ein nativer GIF-Button kommt in den Notiz-Composer, ein Zap-Anreicherungsdienst ([PR #979](https://github.com/PrimalHQ/primal-android-app/pull/979)) annotiert Wallet-Transaktionen mit Zap-Kontext, und ein `primalconnect://`-Deep-Linking-Protokoll ([PR #969](https://github.com/PrimalHQ/primal-android-app/pull/969)) ermöglicht app-übergreifende Navigation.

[Primal iOS](https://github.com/PrimalHQ/primal-ios-app) liefert dieselbe Arbeit parallel über TestFlight, wobei der Wallet-Wechsel ([PR #191](https://github.com/PrimalHQ/primal-ios-app/pull/191)), die Poll-Implementierung und der Onboarding-Umbau im selben Zeitfenster landen.

### BigBrotr kartiert exponierte private Schlüssel im Relay-Netzwerk

[BigBrotr](https://github.com/BigBrotr/bigbrotr), die Nostr-Relay-Analyseplattform, veröffentlichte eine [detaillierte Analyse exponierter privater Schlüssel](https://bigbrotr.com/blog/exposed-nsec-analysis/) im Relay-Netzwerk. Die Studie scannte 41 Millionen Events von 1.085 Relays und suchte nach gültigen nsec-Strings in Event-Inhalten, wobei 16.599 gültige private Schlüssel gefunden wurden. Diese Zahl sieht alarmierend aus, bis man einen Bot namens "Mr.nsec" herausfiltert, der 92 % der Treffer ausmacht. Nach Entfernung des Bot-Traffics hatten nur 38 echte Accounts mit mehr als 21.000 kombinierten Followern exponierte Schlüssel, und keiner zeigte Anzeichen dafür, dass er wusste, dass seine Schlüssel öffentlich waren.

Das Team baute einen nsec-Leak-Checker als [NIP-90](/de/topics/nip-90/) (Data Vending Machine) Dienst, der Nutzern ermöglicht zu prüfen, ob ihr privater Schlüssel irgendwo im gescannten Datensatz auftaucht, ohne den Schlüssel dem Prüfer preiszugeben. [npub.world](https://npub.world) integrierte die Leak-Daten in derselben Woche und zeigt Warnbanner auf Profilseiten, auf denen exponierte Schlüssel erkannt wurden. Die Kombination gibt dem Netzwerk sowohl eine programmatische Schnittstelle für DVMs und Agenten als auch eine menschenlesbare Warnung für reguläre Nutzer. Der zugrundeliegende Datensatz speist auch [BigBrotr v6.4.0](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.4.0), das ersetzbare und adressierbare Event-Materialized-Views und einen Synchronizer-Idle-Timeout-Fix hinzufügt.

### Nostr VPN startet als Tailscale-Alternative

Martti Malmi (mmalmi), Schöpfer von Iris, baute und lieferte [nostr-vpn](https://github.com/mmalmi/nostr-vpn), ein Peer-to-Peer-VPN, das Nostr-Relays für Signalisierung und WireGuard (via boringtun) für verschlüsselte Tunnel verwendet. Die Motivation war direkt: "Got annoyed by Tailscale requiring 3rd party accounts, so created Nostr VPN." Das Tool erstellt Mesh-Netzwerke zwischen Geräten unter Verwendung von Nostr-Schlüsselpaaren als Identität, ohne zentralen Koordinationsserver.

Das Projekt lieferte 11 Releases in sieben Tagen, von [v0.2.2](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.2) bis [v0.2.13](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.13). Dieser Sprint fügte Windows-Unterstützung, LAN-Pairing für lokale Netzwerkerkennung und einen Android-Sidecar für mobile Geräte hinzu. Die Architektur ist einfach: Zwei Geräte tauschen Verbindungsmetadaten über Nostr-Relays aus, dann bauen sie einen direkten WireGuard-Tunnel auf. Nostr übernimmt Discovery und NAT-Traversal-Signalisierung. WireGuard übernimmt den eigentlichen Traffic. Identität ist ein Nostr-Schlüsselpaar.

Malmi trieb auch [nostr-double-ratchet](https://github.com/mmalmi/nostr-double-ratchet) weiter voran, eine Signal-artige sichere Messaging-Channel-Bibliothek, und lieferte sechs Releases von [v0.0.86](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.86) bis [v0.0.93](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.93) in derselben Woche.

### Open-Source-DOOM läuft Peer-to-Peer über Nostr

Das [Vector](https://github.com/VectorPrivacy/Vector)-Team veröffentlichte eine Peer-to-Peer-Multiplayer-DOOM-Implementierung als Open Source, die Nostr für Peer-Discovery, [Marmot](/de/topics/marmot/) für Ende-zu-Ende-Verschlüsselung und [Iroh](https://github.com/n0-computer/iroh), die QUIC-Networking-Bibliothek von n0, für Gossip-Transport verwendet. Das Spiel kommt als 4,2 MB WebXDC-Datei, die innerhalb von Chat-Nachrichten gesendet werden kann, ohne dass Server zum Hosten oder Koordinieren eines Matches nötig sind.

Der technische Ansatz ersetzt den originalen 1993er Lockstep-Netcode durch ein Echtzeit-Hybrid-Sync-Modell. Spieler entdecken sich gegenseitig durch Nostr-Relay-Abfragen, verhandeln Sessions durch Marmot-verschlüsselte Kanäle und übergeben dann an Irohs QUIC-Gossip-Layer für den latenzarmen Spiel-Traffic. Der Stack verwendet Nostr für Discovery, Marmot für Verschlüsselung und Iroh für Transport.

Vector lieferte auch Sicherheitshärtung diese Woche. Der Release fügt einen speichergehärteten Key Vault mit Anti-Debug-Schutz und Zeroize für sensibles Schlüsselmaterial hinzu, User-Blocking mit vollständiger DM- und Gruppennachrichten-Filterung sowie WebXDC-Realtime-Channel-Fixes für Mini Apps.

### FIPS v0.2.0 liefert Tor-Transport, reproduzierbare Builds und Sidecar-Beispiele

[FIPS](https://github.com/jmcorgan/fips), das Free Internetworking Peering System und Nostr-angrenzendes Mesh-Networking-Projekt, lieferte [v0.2.0](https://github.com/jmcorgan/fips/releases/tag/v0.2.0-rel). Der Release fügt Tor-Transport-Unterstützung für anonymisierte Mesh-Links, reproduzierbare Builds, ein Sidecar-Beispiel das sich über ein Nostr-Relay verbindet und Nostr-Release-Publishing im OpenWrt-Paket-Workflow hinzu. Der Release behebt auch Post-Rekey-Jitter-Spikes, die durch Drain-Window-Frames verursacht wurden. Das Wire-Format hat sich gegenüber v0.1.0 geändert, sodass bestehende v0.1.0-Nodes nicht mit v0.2.0 interoperieren können, ohne zu aktualisieren.

### Nostrability Schemata wird mehrsprachig

Das [Nostrability Schemata](https://github.com/nostrability/schemata)-Projekt, das JSON-Schema-Definitionen zur Validierung von Nostr-Event-Kinds pflegt, expandierte in einer Woche von JavaScript-only auf sechs Sprachen. Neue Pakete für Rust, Go, Dart, Swift und Python wurden veröffentlicht, jeweils mit sowohl einem Datenpaket als auch einem Validator. [v0.2.6](https://github.com/nostrability/schemata/releases/tag/v0.2.6) fügte auch 17 neue Event-Kind-Schemas hinzu.

Der [Nostrability-Interop-Tracker](https://nostrability.github.io/nostrability/) erhielt eine parallele Überarbeitung. Ein neuer What's-New-Tab veröffentlicht Updates sowohl über einen Atom-Feed als auch über ein Nostr-Event, App-Kategorie-Filterung erlaubt Besuchern, in bestimmte Client-Typen einzutauchen, und der Tracker erkennt nun automatisch Programmiersprachen aus GitHub-Repository-Metadaten. Nostrability hat auch nun einen eigenen npub, was das Projekt selbst über das Protokoll auffindbar macht, das es dokumentiert. Für Bibliotheksautoren, die über Sprachen hinweg arbeiten, bedeuten die mehrsprachigen Schema-Pakete, dass dieselben Event-Kind-Definitionen als native Imports verfügbar sind, anstatt dass jedes Projekt seine eigene Schema-Kopie pflegen muss.

## Releases

### Amethyst v1.06.0 und v1.06.1

[Amethyst](https://github.com/vitorpamplona/amethyst), der Android-Client gepflegt von vitorpamplona, lieferte [v1.06.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.0) und [v1.06.1](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.1) am 23. März. Das Hauptfeature ist Poll-Unterstützung mit [NIP-85](/de/topics/nip-85/) (Trusted Assertions) Daten für gewichtetes Voting, mit neu gestalteten Poll- und Zap-Poll-Karten. Das neue Rendering gibt sowohl Standard-Polls als auch Zap-gewichteten Polls ein saubereres visuelles Layout. v1.06.1 folgt mit Concurrent-Modification-Crash-Fixes, die Stabilitätsregressionen im Poll-Rendering-Pfad adressieren.

### Amber v5.0.0 und v5.0.1

[Amber](https://github.com/greenart7c3/Amber), die [NIP-55](/de/topics/nip-55/) (Android Signer Application) Signer-App, beförderte ihre jüngste 4.1.x-Pre-Release-Arbeit mit [v5.0.0](https://github.com/greenart7c3/Amber/releases/tag/v5.0.0) am 18. März in Stable. Dieser Stable-Release trägt die [NIP-42](/de/topics/nip-42/) Relay-Auth-, eingebaute Tor-, inhaltstypspezifische Berechtigungs- und verschlüsselte PIN-Speicher-Änderungen, die letzte Woche behandelt wurden. [v5.0.1](https://github.com/greenart7c3/Amber/releases/tag/v5.0.1) entfernt dann die Internet-Berechtigung aus dem Offline-Build-Flavor, sodass dieser Build auf Android-Berechtigungsebene keine Netzwerkanfragen mehr stellen kann.

### Mostro v0.17.0 und Mostro Mobile v1.2.2

[Mostro](https://github.com/MostroP2P/mostro), die Peer-to-Peer-Bitcoin-Börse auf Nostr, lieferte [v0.17.0](https://github.com/MostroP2P/mostro/releases/tag/v0.17.0) am 18. März. Der Server-Release setzt die Dispute- und Rating-Arbeit aus dem v0.16.x-Zyklus fort und fügt vollständigere Handels-Reputationsdaten für Käufer und Verkäufer als Nostr-Events hinzu. [Mostro Mobile](https://github.com/MostroP2P/mobile), der Flutter-Client, folgte mit [v1.2.2](https://github.com/MostroP2P/mobile/releases/tag/v1.2.2) am 23. März und hält die mobile Oberfläche synchron mit den neuesten Protokolländerungen.

### Shosho v0.14.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), die Nostr-Livestreaming-App, lieferte [v0.14.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.14.0) am 19. März mit dem Launch von Shosho Shop. Der Release fügt einen Shop-Tab auf Profilen, Shop in Browse und einen In-Live-Shop-Button auf Lives und Clips hinzu. Die Release-Notes sagen, dass bestehende "Nostr-Produkte" automatisch erscheinen und Käufer zur Plebeian-Market-Seite des Verkäufers durchklicken. Shoshos Release-Notes identifizieren den Listing-Event-Kind nicht, daher lässt sich noch nicht bestätigen, ob Shosho Shop dieselben [NIP-99](/de/topics/nip-99/) Kleinanzeigen liest, die [Shopstr](https://github.com/shopstr-eng/shopstr) explizit in seinem README unterstützt.

### Applesauce v5.2.0

[Applesauce](https://github.com/hzrd149/applesauce), hzrd149s Sammlung von Helper-Paketen für den Bau von Nostr-Anwendungen, lieferte [v5.2.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core@5.2.0) am 22. März. Der Release umfasst sechs Pakete. Das SQLite-Paket behebt eine UNIQUE-Constraint-Kollision bei Event-Tags, die doppelte Inserts verursachte. Das Signers-Paket fügt `AndroidNativeSigner` hinzu, der die [NIP-55](/de/topics/nip-55/) native Android-Signer-Schnittstelle umhüllt, sodass WebView-basierte Apps hardwaregestütztes Signing ohne benutzerdefinierten Bridge-Code nutzen können. Das Relay-Paket fügt ein `challenge`-Feld zu Relay- und Pool-Status-Objekten hinzu, das den [NIP-42](/de/topics/nip-42/) Auth-Status verfolgt, sodass Apps erkennen können, wann ein Relay Authentifizierung anfordert und programmatisch reagieren können. Das Core-Paket erhält `isEventPointerSame`- und `isAddressPointerSame`-Methoden zum Deduplizieren von Event-Referenzen, und das Common-Paket fügt `user.blossomServers$` zum Auflösen der Blossom-Medienserver eines Nutzers hinzu. Applesauce betreibt noStrudel, Satellite und mehrere andere Web-Clients, sodass sich diese Fixes über die Web-Client-Schicht verbreiten.

### Wisp liefert 16 Releases in einer Woche

[Wisp](https://github.com/barrydeen/wisp), der Android-Nostr-Client, lieferte 16 Releases von [v0.9.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.9.3-beta) bis [v0.13.1-beta](https://github.com/barrydeen/wisp/releases/tag/v0.13.1-beta) diese Woche. Die Feature-Ergänzungen umfassen Multi-Account-Unterstützung, einen Zen-Benachrichtigungsmodus für reduzierte Unterbrechungen, Entwürfe und geplante Beiträge, Sicherheits-Content-Filter und ein neues Flammen-Icon.

### Manent v1.2.0

[Manent](https://github.com/dtonon/manent), die private verschlüsselte Notizen- und Dateispeicher-App, lieferte [v1.2.0](https://github.com/dtonon/manent/releases/tag/v1.2.0) am 20. März. Der Release fügt Kameraaufnahme direkt aus der App, Bildgrößenanpassung vor dem Upload zur Reduzierung der Speicherkosten und Pinch-to-Zoom zum Betrachten gespeicherter Bilder hinzu. Manent speichert Notizen und Dateien verschlüsselt auf Nostr-Relays unter Verwendung des Nutzer-Schlüsselpaars und macht das Telefon oder die Desktop-App zu einem Thin Client, der seinen vollständigen Zustand aus Relay-Daten rekonstruieren kann.

### diVine 1.0.7

[diVine](https://github.com/divinevideo/divine-mobile), der Kurzform-Video-Client, lieferte [1.0.7](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.7) am 21. März mit einem Video-Wiedergabe-Watchdog, der ins Stocken geratene Videos automatisch fortsetzt. Nach der E2E-Testinfrastruktur und dem direkten MP4-Laden in [v1.0.6](/en/newsletters/2026-03-11-newsletter/#divine-ships-v106-with-e2e-test-infrastructure-and-nip-49-import) zielt dieser Release auf den verbleibenden Wiedergabe-Fehlerpfad: Videos, die mitten im Stream stoppen, ohne einen Fehler zu werfen.

### Alby Extension v3.14.2

[Alby Extension](https://github.com/getAlby/lightning-browser-extension), die [NIP-07](/de/topics/nip-07/) (Browser Extension Signer) Browsererweiterung, lieferte [v3.14.2](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.14.2) am 18. März mit Lightning-Adress-QR-Code-Anzeige und Schnorr-Signatur-Unterstützung. Die Schnorr-Ergänzung bringt die Browsererweiterung in Einklang mit dem secp256k1-Signaturschema, das Nostr nativ verwendet.

### NoorNote v0.6.5 bis v0.6.11

[NoorNote](https://github.com/77elements/noornote), die Notiz-App, lieferte sieben Releases von [v0.6.5](https://github.com/77elements/noornote/releases/tag/v0.6.5) bis [v0.6.11](https://github.com/77elements/noornote/releases/tag/v0.6.11). Die Hauptergänzung sind Follow Packs: kuratierte Bündel von Accounts, die Nutzer durchsuchen und in großen Mengen abonnieren können, ähnlich wie Twitter-Listen, aber für Onboarding konzipiert. Nutzer können Follow Packs mit benutzerdefinierten Titeln, Beschreibungen und Coverbildern erstellen, bearbeiten und teilen. Die Serie aktualisiert auch die zugrundeliegende Nostr-Bibliothek von NDK v2 auf v3, was verbesserte Relay-Verbindungsbehandlung und Subscription-Management bringt. Bildnotizen und ein neu gestaltetes Relay-Verbindungserlebnis runden die Serie ab.

### nak v0.19.1 und v0.19.2

[nak](https://github.com/fiatjaf/nak), fiatjafs Kommandozeilen-Nostr-Toolkit für die Interaktion mit Relays, das Kodieren und Dekodieren von [NIP-19](/de/topics/nip-19/) (Bech32-Encoded Entities) Identifikatoren, das Signieren von Events und das Abfragen von Relay-Daten, lieferte [v0.19.1](https://github.com/fiatjaf/nak/releases/tag/v0.19.1) und [v0.19.2](https://github.com/fiatjaf/nak/releases/tag/v0.19.2) am 17. und 20. März. Die beiden Punkt-Releases folgen der [v0.19.0](/de/newsletters/2026-03-18-newsletter/) Gruppen-Forum-UI-Ergänzung der letzten Woche.

### Calendar by Form* v0.2.1

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), die dezentrale Kalender-App auf Basis von [NIP-52](/de/topics/nip-52/) (Calendar Events), lieferte [v0.2.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.1) am 20. März. Der Release behebt ein Benachrichtigungsvorlagen-Problem, das Event-Erinnerungen betraf. Calendar speichert Events als Nostr kind 31922 (datumsbasiert) und kind 31923 (zeitbasiert) Events, sodass jeder Nostr-Client Kalenderdaten rendern kann, wenn er die Kinds unterstützt. Die App wird vom Formstr-Team gebaut, das auch Formstr (dezentrale Formulare) und Pollerama (Umfragen) pflegt.

### NYM v3.50 bis v3.53

[NYM](https://github.com/Spl0itable/NYM), der leichtgewichtige ephemere Chat-Client mit Bitchat-Bridge, lieferte 28 Releases von v3.50 bis v3.53 (die Patch-Versionen inkrementieren schnell). Das bemerkenswerteste Feature ist Nymbot, ein eingebauter Chat-Bot, der auf `@nymbot`-Erwähnungen in Kanälen reagiert und Relay-Status- und Management-Funktionen bietet. Ein "Hardcore-Modus" generiert für jede gesendete Nachricht ein frisches Schlüsselpaar, was Konversationsthreads auf Identitätsebene unverknüpfbar macht. Der Kompromiss ist klar: Man verliert persistente Identität, gewinnt aber Pro-Nachricht-Anonymität. Die Relay-Proxy-Schicht erhielt ebenfalls Arbeit, mit Sharded-Relay-Proxy-Workern für bessere Konnektivität, Geohash-Channel-Unterstützung und Clock-Skew-Toleranz für Nodes mit ungenauen System-Uhren.

## Projekt-Updates

### Ditto fügt Bluesky-Bridge und Wikipedia-Integration hinzu

[Ditto](https://github.com/soapbox-pub/ditto), der anpassbare Nostr-Social-Client des Soapbox-Teams, verzeichnete diese Woche über 300 Commits über drei verschiedene Feature-Tracks. Der erste ist eine Bluesky-Bridge (19 Commits), die Bluesky-Posts inline als vollständige Feed-artige Threads rendert, Sidebar-Navigation zu einer Bluesky-Discovery-Seite mit dem offiziellen Discover-Feed (whats-hot) hinzufügt und Aktionsbuttons für Kommentieren, Teilen, Reagieren und Link-Kopieren verdrahtet. Wenn ein Nutzer von innerhalb Ditto auf einen Bluesky-Post antwortet, zeigt das Compose-Modal einen Disclaimer-Hinweis, der auf die protokollübergreifende Natur der Interaktion hinweist. [NIP-73](/de/topics/nip-73/) (External Content IDs) kind-17-Reaktionen treiben das protokollübergreifende Modell an: Ein Nostr-Nutzer reagiert auf einen Bluesky-Post, und die Reaktion wird als Standard-Nostr-Event gespeichert, das den externen Content-Identifier referenziert. Dies ist dasselbe NIP-73-Muster, das Reaktionen auf jeden externen Inhalt brücken könnte, von Bluesky-Posts über YouTube-Videos bis zu Webseiten.

Der zweite Track ist eine Wikipedia-Integration (9 Commits). Ditto rendert nun reichhaltige Wikipedia-Artikelinhalte auf Detailseiten statt generischer Link-Vorschauen, fügt Such-Autocomplete mit Artikel-Thumbnails hinzu und bietet eine `/wikipedia`-Seite, die Featured Content von der Wikipedia-API zieht. Wikipedia- und Archive.org-Ergebnisse erscheinen auch im allgemeinen Such-Autocomplete-Dropdown. Der dritte Track ist iOS-Plattformunterstützung via Capacitor, mit einem Remote-Build-Skript und Plattformkonfiguration, die neben einer UI-Überarbeitung (55 Commits) landet, die Backdrop-Blur-Header durch ein neues Arc-basiertes Navigationsdesign über jede Seite in der App ersetzt. Die 314 Commits bewegen Ditto von einem Nostr-Only-Client zu einem Multiprotokoll-Aggregator, der Bluesky und Wikipedia als erstklassige Inhaltsquellen neben dem Nostr-Feed behandelt.

### Pika baut eine NIP-34-Forge-CI-Pipeline

[Pika](https://github.com/sledtools/pika), die Marmot-basierte verschlüsselte Messaging-App, mergte 33 PRs diese Woche, fokussiert auf eine selbst-gehostete [NIP-34](/de/topics/nip-34/) Forge mit Pre-Merge-CI. Die Forge ist eine Git-Hosting-Schicht, die Patches als NIP-34-Events empfängt, CI-Prüfungen vor dem Merge durchführt und strukturierten Status über Nostr-Events zurückmeldet. [PR #701](https://github.com/sledtools/pika/pull/701) fügt Lane-basierte Pre-Merge- und Nightly-CI hinzu, wobei jeder Code-Pfad (Rust, TypeScript, Apple-Builds) in seiner eigenen Lane mit unabhängigem Pass/Fail-Status läuft. [PR #715](https://github.com/sledtools/pika/pull/715) schneidet verwaltete CI-Agenten auf Incus-OpenClaw-Container für Isolation, und [PR #733](https://github.com/sledtools/pika/pull/733) fügt eine `ph forge`-CLI für die Interaktion mit der gehosteten Forge von der Kommandozeile hinzu. Unterstützende PRs behandeln Repo-Schreibberechtigungen für Merges ([PR #736](https://github.com/sledtools/pika/pull/736)), strukturierte CI-Metadaten mit Live-Status-Badges ([PR #722](https://github.com/sledtools/pika/pull/722)), Apple-Nightly-Build-Splits ([PR #738](https://github.com/sledtools/pika/pull/738)) und Forge-Auth- und Branch-Lookup-Fixes ([PR #734](https://github.com/sledtools/pika/pull/734)). Dies ist eines der ersten funktionierenden CI/CD-Systeme, die auf NIP-34-Git-Events aufgebaut sind, und bewegt Nostr-basiertes Source-Code-Hosting über einfachen Patch-Austausch hinaus in Richtung des Merge-und-Test-Workflows, den Entwickler von GitHub oder GitLab erwarten.

### Nostria fügt Communities, Code-Snippets und Voice-Event-Behandlung hinzu

[Nostria](https://github.com/nostria-app/nostria), der plattformübergreifende Nostr-Client gepflegt von sondreb, erweiterte diese Woche die App-Oberfläche über die in #14 behandelte Web-of-Trust-Filterung hinaus. Die Hauptergänzung ist eine vollständige [NIP-72](/de/topics/nip-72/) (Moderated Communities) Implementierung mit Community-Erstellung, Moderator- und Relay-Konfiguration, Post-Approval-Tracking mit Bildvorschauen und einer dedizierten Community-Seite mit Posts- und Moderatoren-Tabs.

Derselbe Arbeitszeitraum fügt auch Code-Snippet-Rendering und -Bearbeitung mit einem syntaxhervorgehobenen Editor, Voice-Event-Reply-Unterstützung für Audio-Konversationen, Chat-Relay-Einstellungen für Direktnachrichten, Channel-Sharing über die Web Share API, ein Toolbar-Docking-System für den Media Player, In-App-Anmeldung für den neuesten Brainstorm Web-of-Trust-Dienst, Geld-Sende- und -Empfangsflows in DMs über NWC und BOLT-11-Invoices, Nostr-native GIF-Behandlung und einen stärkeren RSS-Import-Pfad für Musiker hinzu, der bestehende Lightning-Splits aus Podcast-Feeds übernehmen kann.

### nostr-vpn schnelle Iteration

Über den [initialen Launch](#nostr-vpn-startet-als-tailscale-alternative) hinaus zeigt das [nostr-vpn](https://github.com/mmalmi/nostr-vpn) Commit-Log die spezifischen Probleme, die beim echten Deployment auftraten. [v0.2.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.3) bis [v0.2.5](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.5) fügten das initiale Installer-Skript und die plattformübergreifende CLI hinzu. [v0.2.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.6) und [v0.2.7](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.7) brachten Windows-Unterstützung, was UAC-Pfad-Quoting für Config-Writes und Daemon-eigene Config-Updates erforderte. [v0.2.8](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.8) bis [v0.2.10](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.10) behob Windows-GUI-Service-Aktionen, CLI-Subprozess-Behandlung und maschinen-bezogene Service-Konfiguration. [v0.2.12](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.12) ersetzte LAN-Discovery durch zeitgesteuertes LAN-Pairing, einen nutzer-initiierten Flow, bei dem sich zwei Geräte im selben lokalen Netzwerk ohne Relay-Signalisierung pairen. Das Muster ist lehrbuchmäßiges Frühphasen-Feld-Testing: Jeder Release zielt auf einen bestimmten Deployment-Fehler, die Nutzerbasis ist klein genug für tägliche Iteration, und der Entwickler nutzt das Tool persönlich zwischen den Releases.

### Comet automatisierte Builds

[Comet](https://github.com/nodetec/comet) (ehemals Captain's Log), das Nostr-native Langform-Schreibtool von Nodetec, produzierte diese Woche über 40 automatisierte Alpha-Builds. Comet ist eine Desktop-App zum Schreiben und Veröffentlichen von NIP-23 (Long-form Content) Artikeln, mit lokaler Entwurfsspeicherung, Markdown-Bearbeitung und Ein-Klick-Publishing zum Relay-Set des Nutzers. Die automatisierte Build-Pipeline generiert einen getaggten Release für jeden Commit auf den Main-Branch, was die rohe Release-Anzahl als Maß für Feature-Velocity irreführend macht. Was die 40 Builds zeigen, ist, dass die App unter täglicher aktiver Entwicklung steht, wobei jeder Commit getestet, paketiert und innerhalb von Minuten zum Download bereitgestellt wird.

## NIP-Updates

Aktuelle Änderungen am [NIPs-Repository](https://github.com/nostr-protocol/nips) im Zeitfenster 17.-24. März:

Zwischen dem 18. und 24. März wurden keine NIPs gemergt.

**Offene PRs und Diskussionen, die im Zeitfenster aktualisiert wurden:**

- **NIP-AA: Autonome Agenten auf Nostr** ([PR #2259](https://github.com/nostr-protocol/nips/pull/2259)): Schlägt Konventionen für autonome Agenten vor, die im Nostr-Netzwerk operieren. Der PR definiert, wie Agenten sich identifizieren, Dienste entdecken und sich mit anderen Agenten und Menschen über Nostr-Events koordinieren.

- **[NIP-50](/de/topics/nip-50/) (Search): Sortierungserweiterungen** ([PR #2283](https://github.com/nostr-protocol/nips/pull/2283)): Fügt Sortierparameter zu NIP-50-Suchabfragen hinzu, einschließlich top, hot, zaps und new. Das würde Clients ermöglichen, gerankte Ergebnisse von Relays anzufordern, die Volltextsuche unterstützen, anstatt client-seitig zu sortieren.

- **NIP-A5: WASM-Programme** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): Schlägt eine Konvention für das Veröffentlichen und Entdecken von WebAssembly-Programmen auf Nostr vor. WASM-Binaries könnten als Nostr-Events verteilt werden, wobei Relays als Discovery-Schicht für portablen ausführbaren Code dienen.

- **NIP-CF: Combine Forces interoperable napps** ([PR #2277](https://github.com/nostr-protocol/nips/pull/2277)): Definiert eine Konvention für interoperable Nostr-Anwendungen ("napps"), die Funktionalität über verschiedene Clients und Dienste hinweg zusammensetzen können.

- **Snapshots-NIP** ([PR #2279](https://github.com/nostr-protocol/nips/pull/2279)): Schlägt einen Mechanismus für Relay-Status-Snapshots vor, für Relay-Synchronisation und Backup.

- **Checkpoints-NIP** ([PR #2278](https://github.com/nostr-protocol/nips/pull/2278)): Schlägt Checkpoint-Events zum Markieren bekannt-guter Relay-Zustände vor, komplementär zum Snapshots-Vorschlag.

- **[NIP-58](/de/topics/nip-58/) (Badges): Badge-Sets-Refactor** ([PR #2276](https://github.com/nostr-protocol/nips/pull/2276)): Restrukturiert, wie Badge-Sammlungen organisiert und referenziert werden.

- **[NIP-11](/de/topics/nip-11/) (Relay Information Document): Erweiterungen** ([PR #2280](https://github.com/nostr-protocol/nips/pull/2280)): Fügt zusätzliche Felder zum Relay-Informationsdokument für reichhaltigere maschinenlesbare Relay-Metadaten hinzu.

## Fünf Jahre Nostr im März

[Der Newsletter des letzten Monats](/de/newsletters/2026-03-04-newsletter/#fünf-jahre-nostr-im-februar) behandelte, wie Nostrs Februare vom NIP-01 (Basic Protocol Flow) Rewrite über die Damus-App-Store-Welle bis zu Mesh-Networking und Agenten-Vorschlägen fortschritten. Dieser Rückblick zeichnet nach, was in jedem März von 2021 bis 2026 geschah.

### März 2021: Zwei Commits

Vier Monate nach seiner Entstehung produzierte Nostrs März genau zwei Commits zum Protokoll-Repository, beide am 4. März. fiatjaf [fügte Links zu Nostwitter-Instanzen hinzu](https://github.com/nostr-protocol/nostr/commit/dcd8cc3), die frühe Besucher auf funktionierende Deployments verwiesen, und [fügte Kind zur grundlegenden Filterdefinition hinzu](https://github.com/nostr-protocol/nostr/commit/54dfb46). Dieser zweite Commit ist aufschlussreich: Im März 2021 konnte man Nostr-Events noch nicht nach Kind filtern. Das Protokoll war so primitiv. Zwei oder drei Relays bedienten das Netzwerk. Die Telegram-Gruppe war der einzige Koordinationskanal. Das NIPs-Repository existierte noch nicht; Protokollvorschläge lebten als Dateien im Haupt-Nostr-Repository. fiatjaf war der einzige Committer in diesem Monat. Der gesamte März-2021-Output dessen, was fünf Jahre später ein Protokoll werden würde, das VPNs, Multiplayer-Spiele und Mesh-Networking unterstützt, passt in einen einzigen Git-Diff.

### März 2022: Pre-Damus-Aufbau

Das Haupt-Protokoll-Repository erhielt im März 2022 null Commits. Die Entwicklung hatte sich vollständig auf Tool-Repositories verlagert. [Branle](https://github.com/fiatjaf/branle), fiatjafs Vue.js-Web-Client und zu dieser Zeit die primäre Nostr-Oberfläche, erhielt 5 Commits einschließlich Docker-Deployment-Unterstützung und [NIP-05](/de/topics/nip-05/) (DNS-Based Verification) Anzeigenamen-Fixes, die das `_@`-Präfix aus Verifizierungsbadges entfernten. Robert C. Martins [more-speech](https://github.com/unclebob/more-speech), der Clojure-Desktop-Client, verzeichnete 13 oder mehr Commits mit Threading, Tastaturnavigation und einem Bearbeitungsfenster. Der berühmteste Software-Autor, der in diesem Monat aktiv auf Nostr baute, war kein Krypto-Entwickler, sondern die Person, deren "Clean Code" Millionen Exemplare verkauft hat, die einen Nostr-Client in Clojure schrieb, einer Sprachwahl, die alles über die frühe Community verrät: Das waren eigenwillige Programmierer, die für sich selbst bauten.

Das Relay-Netzwerk hatte sich auf etwa 15 Relays mit einer aktiven Nutzerbasis im Hunderte-Bereich erweitert. Damus existierte noch nicht und würde erst im April 2022 erstellt werden. Nostream war ebenfalls noch nicht erschienen. Die Arbeit des Monats war Infrastruktur: Die bestehenden Tools zuverlässiger machen für die kleine Community, die sie bereits täglich nutzte.

### März 2023: Post-Explosions-Infrastruktur

Einen Monat nach der Damus-App-Store-Welle und dem Anstieg über 300.000 öffentliche Schlüssel ging es im März 2023 darum, das Wachstum aufzunehmen. Das [NIPs-Repository](https://github.com/nostr-protocol/nips) mergte 28 Pull Requests, die zweithöchste monatliche Anzahl in der Protokollgeschichte. [NIP-51](/de/topics/nip-51/) (Lists) wurde gemergt und gab Clients strukturierte Follow-, Mute- und Bookmark-Sammlungen. [NIP-39](/de/topics/nip-39/) (External Identities in Profiles) landete, NIP-78 (Application-Specific Data) lieferte einen allgemeinen Speicher-Kind für Apps, die privaten Zustand brauchten, und ein Rewrite von [NIP-57](/de/topics/nip-57/) (Lightning Zaps) ([PR #392](https://github.com/nostr-protocol/nips/pull/392)) konsolidierte den Zap-Flow und klärte die Terminologie. Der meistdiskutierte PR des Monats war ein alternativer Mention-Handling-Vorschlag ([PR #381](https://github.com/nostr-protocol/nips/pull/381)) mit über 50 Kommentaren.

Das folgenreichste neue Projekt war [NDK](https://github.com/nostr-dev-kit/ndk) (Nostr Development Kit), die TypeScript-Bibliothek für Relay-Verbindungen, Event-Signing, Caching und Subscription-Management. pablof7z machte den [ersten Commit](https://github.com/nostr-dev-kit/ndk/commit/09e5e03) am 16. März 2023, schrieb es 11 Tage später am 27. März von Grund auf neu ("basically another initial commit") und hatte am 31. März LNURL- und Zap-Unterstützung am Laufen. NDK ging in 15 Tagen von nichts zu Zap-fähig. Fünf Tage nach NDKs Erstellung, am 21. März, erstellte das Alby-Team [NWC](https://github.com/getAlby/nostr-wallet-connect) (Nostr Wallet Connect), die Referenzimplementierung von [NIP-47](/de/topics/nip-47/), die Lightning-Wallets mit Nostr-Anwendungen verband. Die beiden Projekte, die die nächsten drei Jahre webbasierter Nostr-Entwicklung untermauern würden, wurden im selben 30-Tage-Fenster geboren. OpenSats hatte seinen Nostr-Fonds noch nicht gestartet; die erste Welle kam erst im [Juli 2023](https://opensats.org/blog/nostr-grants-july-2023), vier Monate nach NDKs Erstellung.

Weitere bemerkenswerte Kreationen in diesem Monat waren NostrGit, NostrChat, ein nostr-signing-device-Projekt von LNbits und nostrmo. [Gossip](https://github.com/mikedilger/gossip), der Rust-Desktop-Client mit Fokus auf intelligente Relay-Auswahl, lieferte drei Releases. Das Protokoll war im Build-Modus, und die im März 2023 erstellten Tools sind drei Jahre später noch in Gebrauch.

### März 2024: Protokollreifung

Im März 2024 ging es um die Härtung des Protokolls für Langzeitnutzung. Das NIPs-Repository mergte 12 Pull Requests. Der bedeutendste war [NIP-34](/de/topics/nip-34/) (Git Stuff), [PR #997](https://github.com/nostr-protocol/nips/pull/997), der am 5. März nach über 130 Kommentaren und 44 Tagen Review gemergt wurde. Der Diskussionsthread ist eine Zeitkapsel der Community, die debattiert, wie man ein dezentrales GitHub baut. jb55 zog Parallelen zu `git send-email`, Giszmo schlug vor, Root-Commit-Hashes für Cross-Fork-Discovery zu verwenden ("something GitHub doesn't do and we could"), mikedilger schlug [NIP-98](/de/topics/nip-98/) (HTTP Auth) Event-signierte Authentifizierung anstelle von SSH-Schlüsseln vor, und fiatjaf wies die Notwendigkeit von Versionskontroll-Allgemeinheit brüsk zurück: "not for each version control system, just for git. No one uses the others." Innerhalb von Stunden nach Öffnung des PRs hatte fiatjaf bereits nak, go-nostr und gitstr umgestellt, um Patches über Nostr zu akzeptieren. DanConwayDev, dessen ngit bereits OpenSats-Grantee war, gehörte zu den aktivsten Beitragenden in der Diskussion. Ein Bot-Feld für Profil-Metadaten wurde ebenfalls gemergt, das Clients eine maschinenlesbare Möglichkeit gibt, automatisierte Accounts von menschlichen zu unterscheiden.

[Amethyst](https://github.com/vitorpamplona/amethyst) lieferte v0.85.0 mit Git-Event-Unterstützung, Wiki-Artikeln, medizinischem Daten-Rendering und Content-Editing in einem einzigen Release. [Mostro](https://github.com/MostroP2P/mostro) erreichte v0.10.0. [Nosflare](https://github.com/Spl0itable/nosflare), ein serverloses Nostr-Relay auf Cloudflare Workers, bewies, dass Relay-Logik am Edge laufen kann. OpenSats erteilte einen [Long-Term-Support-Grant an Bruno Garcia](https://opensats.org/blog/bruno-garcia-receives-lts-grant) für nachhaltige Beiträge zum Amethyst-Client.

### März 2025: Infrastruktur-Expansion

Der März 2025 produzierte 10 gemergte NIPs. Die Schlagzeile war [NIP-66](/de/topics/nip-66/) (Relay Discovery and Liveness Monitoring), [PR #230](https://github.com/nostr-protocol/nips/pull/230), der am 3. März nach einer 25-monatigen Reise gemergt wurde. dskvr schlug Relay-Monitoring erstmals im Februar 2023 vor, bekam zu hören, es könnte client-seitig gemacht werden, erklärte, warum das Verbinden zu Tausenden von Relays gleichzeitig für einzelne Clients unpraktisch war, durchlief sieben vollständige Entwürfe, baute Monitoring-Nodes über acht geografische Regionen (Northeast US, Brasilien, US-West, US-East, Australien, Indien, Korea, Südafrika) und wartete darauf, dass das Relay-Tooling aufholte. Als es gemergt wurde, existierten bereits Implementierungen in nostr.watch, relaypag.es, monitorlizard, Snort, noStrudel und Jumble. Die NIP-66-Daten würden später die Nostrability-Outbox-Benchmarks speisen, die in [Newsletter #12 behandelt wurden](/de/newsletters/2026-03-04-newsletter/#outbox-modell-unter-der-lupe). NIP-C0 (Code Snippets) wurde ebenfalls gemergt ([PR #1852](https://github.com/nostr-protocol/nips/pull/1852), 63 Kommentare) und fügte kind-1337-Events zum Teilen von Quellcode hinzu.

Die ersten MCP-Server für Nostr erschienen in diesem Monat. [nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server) erschien am 23. März und [nwc-mcp-server](https://github.com/getAlby/nwc-mcp-server) am 14. März, nur vier Monate nachdem Anthropic das Model Context Protocol im November 2024 angekündigt hatte. Diese frühen Bridges gingen dem vollständigen [ContextVM](/de/topics/contextvm/) SDK und der Agenten-Commerce-Arbeit voraus, die Ende 2025 und Anfang 2026 folgte.

[Gossip](https://github.com/mikedilger/gossip) lieferte v0.14.0. [Coracle](https://github.com/coracle-social/coracle), hodlbods Web-Client mit Relay-bewusstem Feed-Management, lieferte drei Releases. OpenSats kündigte seine [zehnte Welle von Nostr-Grants](https://opensats.org/blog/10th-wave-of-nostr-grants) an und setzte die Finanzierungspipeline fort, die seit Mitte 2023 lief.

### März 2026: Konvergenz

*Die Aktivität vom März 2026 stammt aus Nostr-Compass-Ausgaben [#12](/de/newsletters/2026-03-04-newsletter/) bis [#15](#) (diese Ausgabe).*

März 2026 ist der Monat, in dem verschiedene Stränge zu funktionierenden Systemen konvergierten. Das [Marmot Development Kit](/de/newsletters/2026-03-04-newsletter/#marmot-development-kit-liefert-ersten-öffentlichen-release) lieferte seinen ersten öffentlichen Release mit verschlüsselten Medien, Multi-Language-Bindings und einer ChaCha20-Poly1305-Migration, die koordinierte Updates über Spec, Rust und TypeScript erforderte. [Shopstr und Milk Market](/en/newsletters/2026-03-11-newsletter/#shopstr-and-milk-market-open-mcp-commerce-surfaces) fügten MCP-Commerce-Oberflächen für agentengesteuerten Einkauf hinzu. [NIP-42](/de/topics/nip-42/) Relay-Auth landete gleichzeitig in [Amber](/en/newsletters/2026-03-11-newsletter/#nip-42-relay-auth-across-bunker-signer-and-relay), strfry und OAuth Bunker und schloss die Schleife zwischen Signer-, Relay- und Bunker-Software. [Notedeck](/de/newsletters/2026-03-18-newsletter/#notedeck-verlagert-release-erkennung-auf-nostr) lieferte Nostr-native Software-Updates unter Verwendung von [NIP-94](/de/topics/nip-94/) (File Metadata) Release-Events.

Diese Woche scannte [BigBrotr](#bigbrotr-kartiert-exponierte-private-schlüssel-im-relay-netzwerk) das gesamte Relay-Netzwerk nach geleakten privaten Schlüsseln und veröffentlichte sowohl die Analyse als auch einen DVM-Checker. [Nostr VPN](#nostr-vpn-startet-als-tailscale-alternative) bewies, dass Nostrs Schlüsselmodell für Netzwerkinfrastruktur funktioniert, nicht nur für soziale Medien. [DOOM](#open-source-doom-läuft-peer-to-peer-über-nostr) demonstrierte, dass Nostr-Discovery, Marmot-Verschlüsselung und QUIC-Transport ein Echtzeit-Multiplayer-Spiel betreiben können. [Amber](#amber-v500-und-v501) sprang auf v5.0.0. [Wisp](#wisp-liefert-16-releases-in-einer-woche) lieferte 16 Releases in sieben Tagen. 25 oder mehr getaggte Releases kamen von großen Projekten in einer einzigen Woche.

Sieben NIPs wurden in den ersten 24 Tagen des Monats gemergt. Das Protokoll fügte [NIP-54](/de/topics/nip-54/) (Wiki) Djot-Markup, [NIP-19](/de/topics/nip-19/) (Bech32-Encoded Entities) Eingabegrenzen, [NIP-91](/de/topics/nip-91/) (AND Operator for Filters) boolesche Abfragelogik und [NIP-85](/de/topics/nip-85/) (Trusted Assertions) Web-of-Trust-Assertions hinzu. Offene Vorschläge reichten von autonomen Agenten (NIP-AA) über WASM-Programme (NIP-A5) bis zu Such-Sortierungserweiterungen für [NIP-50](/de/topics/nip-50/).

### Ausblick

Fünf Märze Nostr zeichnen einen klaren Bogen. 2021 machte eine Person zwei Commits an ein Protokoll, das Events noch nicht nach Kind filtern konnte. Bis 2023 wurden NDK und NWC fünf Tage auseinander geboren, um die Post-Damus-Explosion aufzufangen. Bis 2024 debattierte ein 141-Kommentar-PR-Thread, wie Git-Zusammenarbeit auf einem sozialen Protokoll funktionieren sollte. Bis 2025 wurde eine Relay-Monitoring-Spezifikation, die geduldig sieben Mal über 25 Monate umgeschrieben worden war, endlich gemergt. 2026 wurde jemand genervt davon, dass Tailscale einen Account verlangt, und baute ein VPN mit Nostr-Schlüsselpaaren, während jemand anderes Multiplayer-DOOM lieferte, das Peers über Nostr-Relays entdeckt und Gameplay über Marmot verschlüsselt. BigBrotrs Scan von 41 Millionen Events über 1.085 Relays gibt ein konkretes Maß dafür, wie weit das Netzwerk gewachsen ist. Die Protokolloberfläche im März 2026 wäre für den März 2021 unerkennbar gewesen, aber das zugrundeliegende Modell, Events signiert mit secp256k1-Schlüsseln und verteilt über Relays, hat sich nicht geändert.

---

Das war's für diese Woche. Wer etwas baut oder Neuigkeiten zu teilen hat: <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Per [NIP-17](/de/topics/nip-17/) (Private Direct Messages) DM erreichbar</a> oder auf Nostr findbar.
