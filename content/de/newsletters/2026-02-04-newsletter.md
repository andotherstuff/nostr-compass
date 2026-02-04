---
title: 'Nostr Compass #8'
date: 2026-02-04
translationOf: /en/newsletters/2026-02-04-newsletter.md
translationDate: 2026-02-04
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, deinem wöchentlichen Wegweiser durch Nostr.

**Diese Woche:** rust-nostr liefert ein großes API-Redesign mit 21 PRs, die die SDK-Architektur überarbeiten. Nostria 3.0 startet mit Dual-Pane-Navigation, Listenverwaltung und einer kompletten UI-Überarbeitung. Vector fügt SIMD-Beschleunigung hinzu und erreicht 65x-184x Geschwindigkeitssteigerungen sowie liefert [Marmot](/de/topics/marmot/)-Protokollunterstützung für verschlüsselte Gruppennachrichten. Frostr bringt Threshold-Signierung zu iOS via TestFlight. Damus implementiert [NIP-19 (Bech32 Kodierte Entitäten)](/de/topics/nip-19/) Relay-Hinweise für Cross-Relay-Inhaltsentdeckung. Primal Android fügt NWC-Verschlüsselung und Wallet-Transaktionsexporte hinzu. nostr-tools und NDK erhalten Zuverlässigkeitsverbesserungen. NIP-82 (Software-Anwendungen) erweitert sich auf 98% der Geräteplattformen. Das NIPs-Repository merged Hold-Invoice-Unterstützung für [NIP-47 (Nostr Wallet Connect)](/de/topics/nip-47/). Neue Protokollvorschläge umfassen NIP-74 für Podcasting, NIP-DB für Browser-Event-Datenbanken und eine TRUSTed-Filters-Suite für dezentralisierte Inhaltskuration. Neue Projekte umfassen Instagram to Nostr v2 für Content-Migration, Pod21 startet einen dezentralisierten 3D-Druck-Marktplatz, Clawstr führt KI-Agenten-verwaltete Communities ein, und Shosho und NosCall erweitern Live-Streaming- und Videoanruf-Fähigkeiten.

## Neuigkeiten

### rust-nostr liefert großes API-Redesign

Das [rust-nostr](https://github.com/rust-nostr/nostr) SDK durchlief diese Woche eine signifikante Architekturüberarbeitung mit 21 gemergten PRs, die Breaking Changes in der gesamten Bibliothek einführen. Das Redesign betrifft Kern-APIs, auf die sich die meisten Rust-Entwickler verlassen.

[PR #1245](https://github.com/rust-nostr/nostr/pull/1245) redesignt Notification-APIs, während [PR #1244](https://github.com/rust-nostr/nostr/pull/1244) `RelayNotification::Shutdown` durch `RelayStatus::Shutdown` für sauberere Zustandshandhabung ersetzt. Die Signer-APIs sind jetzt via [PR #1243](https://github.com/rust-nostr/nostr/pull/1243) an andere SDK-Muster angeglichen. Client- und Relay-Methoden erhielten Cleanup in [PR #1242](https://github.com/rust-nostr/nostr/pull/1242), und Client-Optionen verwenden jetzt ein Builder-Pattern ([PR #1241](https://github.com/rust-nostr/nostr/pull/1241)).

Message-Sending-APIs wurden in [PR #1240](https://github.com/rust-nostr/nostr/pull/1240) redesignt, REQ-Unsubscription in [PR #1239](https://github.com/rust-nostr/nostr/pull/1239) und Relay-Entfernung in [PR #1229](https://github.com/rust-nostr/nostr/pull/1229). Ein [offener PR #1246](https://github.com/rust-nostr/nostr/pull/1246) fügt Unterstützung für blockierende APIs hinzu, um das Redesign abzurunden.

Die Änderungen bringen Konsistenz in das SDK, werden aber Migrationsaufwand von bestehenden Projekten erfordern. Entwickler, die auf rust-nostr aufbauen, sollten den Changelog sorgfältig prüfen, bevor sie upgraden.

### Instagram to Nostr v2 ermöglicht Content-Migration

Ein neues Tool ermöglicht es Kreativen, ihre bestehenden Inhalte von zentralisierten Plattformen zu Nostr zu migrieren. [Instagram to Nostr v2](https://github.com/primalpaul1/instagram-to-nostr-v2) unterstützt den Import von Instagram, TikTok, Twitter und Substack, ohne Zugang zu den privaten Schlüsseln des Benutzers zu benötigen.

Das Tool adressiert eine häufige Onboarding-Barriere: Benutzer, die zögern, auf einer neuen Plattform von vorne anzufangen, können jetzt ihre Inhaltshistorie bewahren. Es unterstützt auch das Verschenken von Nostr-Konten an neue Benutzer oder das Vorschlagen von Inhalten an bestehende Konten, was es nützlich macht, anderen beim Übergang zum Protokoll zu helfen.

### Pod21: Dezentralisiertes 3D-Druck-Netzwerk

[Pod21](https://pod21.com) verbindet 3D-Drucker-Betreiber mit Käufern unter Verwendung von Nostr für Marktplatz-Koordination. Die Plattform enthält einen [NIP-17 (Private Direktnachrichten)](/de/topics/nip-17/)-kompatiblen DM-Bot, der Marktplatz-Interaktionen handhabt und es Käufern ermöglicht, Drucke anzufordern und mit Herstellern durch verschlüsselte Direktnachrichten zu verhandeln.

Hersteller listen ihre Druckkapazität und Fähigkeiten; Käufer durchsuchen Listings und initiieren Bestellungen über den Bot. Die Architektur folgt einem ähnlichen Muster wie andere Nostr-Commerce-Anwendungen: Relay-basierte Entdeckung, verschlüsselte Nachrichten für Bestellkoordination und Lightning für Abwicklung. Pod21 reiht sich neben Ridestr und Shopstr als Nostr-Anwendung ein, die reale Transaktionen durch das Protokoll koordiniert.

### Clawstr: KI-Agenten-Sozialnetzwerk

[Clawstr](https://github.com/clawstr/clawstr) startet als Reddit-inspirierte Plattform, auf der KI-Agenten Communities auf Nostr erstellen und verwalten. Die Plattform ermöglicht es autonomen Agenten, thematische Communities zu etablieren, Inhalte zu kuratieren und mit Benutzern zu interagieren. Communities funktionieren wie Subreddits, aber mit KI-Moderatoren und Kuratoren, die Diskussionen leiten. Die Architektur nutzt Nostrs offenes Protokoll für Agent-zu-Agent- und Agent-zu-Mensch-Interaktionen und etabliert ein neues Modell für Community-Bildung in dezentralisierten sozialen Medien.

## Releases

### Ridestr v0.2.0: RoadFlare Release

[Ridestr](https://github.com/variablefate/ridestr) lieferte [v0.2.0](https://github.com/variablefate/ridestr/releases/tag/v0.2.0), genannt der "RoadFlare Release", der persönliche Rideshare-Netzwerke einführt. Die Funktion lässt Fahrgäste Lieblingsfahrer zu einem vertrauenswürdigen Netzwerk hinzufügen. Fahrer genehmigen Follower und teilen verschlüsselte Standorte, sodass Fahrgäste sehen können, wann vertrauenswürdige Fahrer online und in der Nähe sind. Fahrtanfragen gehen direkt an bekannte Fahrer.

Die Zahlungszuverlässigkeit verbesserte sich mit automatischer Escrow-Wiederherstellung, besserer Wallet-Synchronisierung über Geräte hinweg und schnellerer Zahlungsverarbeitung durch progressives Polling. [PR #37](https://github.com/variablefate/ridestr/pull/37) fügt die Phase 5-6 Infrastruktur hinzu, die diese Features unterstützt. [v0.2.1](https://github.com/variablefate/ridestr/releases/tag/v0.2.1) folgte mit Hotfixes für Zahlungsdialog-Bugs und den "Zu Favoriten hinzufügen"-Flow nach der Fahrt.

### Nostria 3.0

[Nostria](https://github.com/nostria-app/nostria), sondrebs plattformübergreifender Client für globale Skalierung, lieferte Version 3.0 mit einer kompletten UI-Überarbeitung, neuem Logo und Hunderten von Fixes. Das Release repräsentiert einen intensiven sechswöchigen Entwicklungszyklus.

Dual-Pane-Navigation ist die größte UX-Änderung, die es Desktop-Benutzern ermöglicht, Kontextwechsel beim Navigieren zwischen Listen, Details und Threads zu reduzieren. Ein neuer Home-Bereich bietet einen Überblick über alle verfügbaren Funktionen, und alle Bildschirme teilen eine vereinheitlichte Toolbar, Layout und Funktionalität.

Listenverwaltung ist das bedeutendste Feature-Update, das durch die gesamte Anwendung integriert ist. Benutzer können Profillisten verwalten und Inhalte in jeder Funktion filtern: Streams, Musik oder Feeds. Genervt von Spam in Threads? Filtern nach Favoriten, um nur deren Antworten zu sehen. Quick Zaps fügt Ein-Tap-Zapping mit konfigurierbaren Werten hinzu. Copy/Screenshot generiert Zwischenablage-Screenshots zum Teilen von Events überall. Stummgeschaltete Wörter filtert jetzt nach Profilfeldern (name, display_name, NIP-05), was es Benutzern ermöglicht, alle gebridgten Profile mit einem einzelnen gebannten Wort zu blockieren. Einstellungen wurden durchsuchbar für schnellere Konfigurationsänderungen.

Das Release fügt BOLT11- und BOLT12-Zahlungsanforderungs-Rendering, Textgröße- und Schriftauswahl sowie "Notiz-an-sich-selbst"-Nachrichten im Nachrichten-Bereich mit Rendering von referenzierten Inhalten wie Artikeln und Events hinzu. Der neue Teilen-Dialog ermöglicht schnelles Teilen per E-Mail, Websites oder Direktnachrichten an mehrere Empfänger. Zusätzliche Features umfassen benutzerdefinierte Emoji-Sets, Interessen (Hashtag-Listen als dynamische Feeds), Lesezeichen, öffentliche Relay-Feeds und vollständige Menüanpassung einschließlich welche Option das Nostria-Icon öffnet.

Verfügbar auf Android, iOS, Windows und im Web unter [nostria.app](https://www.nostria.app/).

### Applesauce v5.1.0

hzrd149s [Applesauce](https://github.com/hzrd149/applesauce)-Bibliothekssuite veröffentlichte v5.1.0 für alle Pakete. [applesauce-signers](https://github.com/hzrd149/applesauce/releases/tag/applesauce-signers%405.1.0) fügt Unterstützung für `switch_relays`- und `ping`-Methoden auf Nostr Connect Remote-Signern hinzu, nützlich für die programmatische Verwaltung von Signer-Verbindungen. [applesauce-loaders](https://github.com/hzrd149/applesauce/releases/tag/applesauce-loaders%405.1.0) führt `loadAsyncMap` für paralleles asynchrones Laden ein. [applesauce-react](https://github.com/hzrd149/applesauce/releases/tag/applesauce-react%405.1.0) fügt Padding-Argumente zu `useAction().run()` hinzu. [applesauce-core](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.1.0) aktualisiert Event-zu-Store-Mapping, um Strings direkt ohne `onlyEvents` zu handhaben.

### nak v0.18.3

fiatjafs [nak](https://github.com/fiatjaf/nak) (Nostr Army Knife) erreichte [v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3) mit Stabilitätsfixes von mattn. Das Release verhindert Panics, wenn Mint-URLs den `://`-Separator nicht haben, validiert Dateparser-Fehler vor Verwendung von Datumswerten und handhabt Grenzfälle beim AUTH-Challenge-Tag-Parsing. Diese defensiven Fixes machen die CLI robuster beim Verarbeiten fehlerhafter Eingaben.

### Aegis v0.3.7

[Aegis](https://github.com/ZharlieW/Aegis), der plattformübergreifende Desktop-Signer, lieferte [v0.3.7](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.7) mit Nostr App Browser-Unterstützung mit [NIP-07 (Browser-Erweiterungs-Interface)](/de/topics/nip-07/)-Signierung. Das Release zeichnet [NIP-04 (Verschlüsselte Direktnachrichten)](/de/topics/nip-04/)- und [NIP-44 (Versionierte Verschlüsselung)](/de/topics/nip-44/)-Verschlüsselungs-Events auf, was es Benutzern ermöglicht zu verfolgen, welche Anwendungen Verschlüsselungsoperationen anfordern. Das Browser-Segment filtert jetzt nach Plattform, um nur Web-Apps anzuzeigen.

### Bitchat v1.5.1 (iOS)

[Bitchat](https://github.com/permissionlesstech/bitchat), die offline-fähige Messaging-App mit Nostr und Bluetooth-Mesh, veröffentlichte [v1.5.1](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.1) mit iOS-Sicherheitshärtung. [PR #1012](https://github.com/permissionlesstech/bitchat/pull/1012) validiert Nostr-Event-Signaturen vor der Verarbeitung, lehnt ungültige Giftwraps und eingebettete Pakete ab, begrenzt übergroße Payloads und blockiert gefälschte BLE-Announce-Sender-IDs. [PR #998](https://github.com/permissionlesstech/bitchat/pull/998) behebt iOS BLE-Mesh-Authentifizierung durch Bindung von Sender-IDs an Verbindungs-UUIDs, was Identitätsfälschung im Mesh-Netzwerk verhindert. [PR #972](https://github.com/permissionlesstech/bitchat/pull/972) fügt Benachrichtigungs-Ratenbegrenzung hinzu, um Peer-Discovery-Fluten zu verhindern, wenn mehrere Mesh-Geräte in der Nähe sind.

### KeyChat v1.39.2

[KeyChat](https://github.com/keychat-io/keychat-app) veröffentlichte [v1.39.2](https://github.com/keychat-io/keychat-app/releases/tag/v1.39.2%2B6495) mit [NIP-47](/de/topics/nip-47/) Nostr Wallet Connect-Unterstützung via [PR #148](https://github.com/keychat-io/keychat-app/pull/148). Benutzer können jetzt externe Lightning-Wallets für Zahlungen innerhalb der Messaging-App verbinden. Das Release fügt auch macOS-Desktop-Benachrichtigungen hinzu.

### Nostrmo v3.5.0

[Nostrmo](https://github.com/haorendashu/nostrmo), der plattformübergreifende Flutter-Client, lieferte [v3.5.0](https://github.com/haorendashu/nostrmo/releases/tag/3.5.0) mit Überarbeitung seines Feed-Systems. Das Update ersetzt feste Feeds durch anpassbare Alternativen: General Feed, Mentioned Feed und Relay Feed, jeweils konfigurierbar durch neue Bearbeitungsseiten. Das Release implementiert Outbox-Modell-Unterstützung für besseres Event-Routing und erweitert lokale Relay-Funktionalität mit konfigurierbaren Größenlimits und Subscription-Unterstützung.

### Shosho v0.11.1

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), die Live-Streaming-App für Nostr, veröffentlichte [v0.11.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.11.1) mit Aufnahme- und VOD-Fähigkeiten. Das Update fügt Raum-Präsenzindikatoren hinzu, die zeigen, wer Streams schaut, Thread-Chat-Konversationen für bessere Diskussionsorganisation und Nostr Connect-Unterstützung auf iOS via [NIP-46](/de/topics/nip-46/). Streamer können jetzt ihre Übertragungen für späteres Ansehen speichern, während sie Echtzeit-Chat-Interaktionen mit ihrem Publikum aufrechterhalten.

### NosCall v0.5.0

[NosCall](https://github.com/sanah9/noscall), die Audio- und Videoanruf-App für Nostr, lieferte [v0.5.0](https://github.com/sanah9/noscall/releases/tag/v0.5.0-release) mit Kontaktgruppen zur Organisation von Anrufen nach Kategorie, Relay-Management für Verbindungsoptimierung und konfigurierbaren ICE-Server-Einstellungen für verbesserte NAT-Traversierung. Das Release fügt auch Dark-Mode-Unterstützung hinzu. NosCall verwendet Nostr für Anrufsignalisierung und -koordination und ermöglicht Peer-to-Peer-Anrufe ohne zentralisierte Server.

### diVine 1.0.4

[diVine](https://github.com/divinevideo/divine-mobile), rabbles Kurzform-Loop-Video-Client, veröffentlichte [1.0.4](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.4) als Android-Pre-Release-Alpha vor seiner Zapstore-Einreichung. Das Release konzentriert sich auf das Testen von Nostr-Schlüsselverwaltung, einschließlich nsec-Import, [NIP-46 (Nostr Connect)](/de/topics/nip-46/) Remote-Signierung mit nsecBunker und Amber sowie nostrconnect://-URL-Handling. Das Team bittet um Feedback zu Relay-Kompatibilität und Video-Interoperabilität mit anderen Clients. [PR #1265](https://github.com/divinevideo/divine-mobile/pull/1265) behebt iOS-Dateipfad-Handling, das dazu führte, dass Videoclips nach App-Updates unbrauchbar wurden, indem relative Pfade statt absoluter Container-Pfade gespeichert werden. [PR #1251](https://github.com/divinevideo/divine-mobile/pull/1251) behebt Navigationsprobleme beim Anzeigen von Profilen aus Kommentaren.

### Zeus v0.12.2

[Zeus](https://github.com/ZeusLN/zeus) lieferte [v0.12.2](https://github.com/ZeusLN/zeus/releases/tag/v0.12.2) als stabiles Release und konsolidiert die [NWC-Fixes aus vorherigen Ausgaben](/de/newsletters/2026-01-28-newsletter/#zeus-v0122-beta---nwc-korrekturen).

### Frostr Igloo iOS TestFlight

[Frostr](https://frostr.org/) startete [Igloo für iOS](https://github.com/FROSTR-ORG/igloo-ios-prototype) auf [TestFlight](https://testflight.apple.com/join/72hjQe3J) und erweitert Threshold-Signierung auf Apple-Geräte. Frostr verwendet FROST (Flexible Round-Optimized Schnorr Threshold)-Signaturen, um nsec-Schlüssel in Shares aufzuteilen, die über Geräte verteilt werden, was k-von-n-Signierung mit Fehlertoleranz ermöglicht. Benutzer, die im "Demo-Modus" beitreten, nehmen an einem Live-2-von-2-Threshold-Signatur-Experiment teil, das die Echtzeit-Koordinationsfähigkeiten des Protokolls demonstriert. Das iOS-Release schließt sich [Igloo für Android](https://github.com/FROSTR-ORG/igloo-android) (v0.1.2) an, das im Dezember mit [NIP-55 (Android Signer)](/de/topics/nip-55/)-Unterstützung für App-übergreifende Signierungsanfragen geliefert wurde. Beide mobilen Clients ergänzen [Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop) und die [Frost2x](https://github.com/FROSTR-ORG/frost2x)-Browser-Erweiterung.

## Projekt-Updates

### Damus implementiert NIP-19 Relay-Hinweise

[Damus](https://github.com/damus-io/damus) mergte [PR #3477](https://github.com/damus-io/damus/pull/3477) und implementiert [NIP-19](/de/topics/nip-19/) Relay-Hinweis-Verarbeitung für Event-Abruf. Die Funktion ermöglicht das Anzeigen von Notizen auf Relays, die nicht im konfigurierten Pool des Benutzers sind, indem Hinweise aus [NIP-10 (Antwort-Threads)](/de/topics/nip-10/), [NIP-18 (Reposts)](/de/topics/nip-18/) und NIP-19-Referenzen extrahiert werden. Die Implementierung verwendet ephemere Relay-Verbindungen mit referenzgezähltem Cleanup, was permanente Relay-Pool-Erweiterung vermeidet.

Zusätzliche Fixes umfassen Lightning-Invoice-Parsing ([PR #3566](https://github.com/damus-io/damus/pull/3566)), Wallet-View-Loading ([PR #3554](https://github.com/damus-io/damus/pull/3554)), Relay-List-Timing ([PR #3553](https://github.com/damus-io/damus/pull/3553)) und Profil-Preloading zur Reduzierung von visuellem "Popping" ([PR #3550](https://github.com/damus-io/damus/pull/3550)). Ein [Entwurfs-PR #3590](https://github.com/damus-io/damus/pull/3590) zeigt [NIP-17](/de/topics/nip-17/)-Private-DM-Unterstützung in Arbeit.

### Primal Android liefert NWC-Verschlüsselung

[Primal Android](https://github.com/PrimalHQ/primal-android-app) hatte eine sehr aktive Woche mit 18 gemergten PRs, fokussiert auf Wallet-Infrastruktur. Die App integriert jetzt mit Spark, Lightspars selbstverwahrendes Lightning-Protokoll. [PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874) fügt NWC-Verschlüsselungsunterstützung hinzu, während [PR #872](https://github.com/PrimalHQ/primal-android-app/pull/872) NWC-Info-Events sendet, wenn Verbindungen hergestellt werden.

[PR #870](https://github.com/PrimalHQ/primal-android-app/pull/870) ermöglicht CSV-Export für Wallet-Transaktionen, nützlich für Buchhaltung und Steuerzwecke. [PR #716](https://github.com/PrimalHQ/primal-android-app/pull/716) fügt einen lokalen Account-Switcher im Note-Editor hinzu. Mehrere Wallet-Restore-Fixes ([PR #876](https://github.com/PrimalHQ/primal-android-app/pull/876), [PR #875](https://github.com/PrimalHQ/primal-android-app/pull/875), [PR #873](https://github.com/PrimalHQ/primal-android-app/pull/873)) adressieren Grenzfälle für Benutzer mit Nicht-Spark-Wallet-Konfigurationen.

### Marmot TypeScript SDK fügt Nachrichtenverlauf hinzu

Die TypeScript-Implementierung des [Marmot](https://github.com/marmot-protocol/marmot)-Protokolls entwickelt sich weiter. [PR #38](https://github.com/marmot-protocol/marmot-ts/pull/38) von hzrd149 implementiert Nachrichtenverlaufs-Persistenz mit Paginierung für die Referenz-Chat-Anwendung, während [PR #39](https://github.com/marmot-protocol/marmot-ts/pull/39) die Bibliotheks-Ergonomie verbessert.

Auf der Rust-Seite implementiert [PR #161](https://github.com/marmot-protocol/mdk/pull/161) wiederholbares Zustandshandling zur Bewahrung des Nachrichtenkontexts bei Fehlern, und [PR #164](https://github.com/marmot-protocol/mdk/pull/164) wechselt zu std::sync::Mutex, um tokio-Panics mit SQLite zu vermeiden. Das whitenoise-rs-Backend fügt [Amber-Integration](https://github.com/marmot-protocol/whitenoise-rs/pull/418) ([PR #418](https://github.com/marmot-protocol/whitenoise-rs/pull/418)) hinzu, [Upgrades auf MDK und nostr-sdk 0.44](https://github.com/marmot-protocol/whitenoise-rs/pull/467) ([PR #467](https://github.com/marmot-protocol/whitenoise-rs/pull/467)) und führt Echtzeit-Benachrichtigungs-Streaming via [PR #460](https://github.com/marmot-protocol/whitenoise-rs/pull/460) mit NewMessage- und GroupInvite-Event-Typen ein.

### HAVEN fügt periodische WoT-Aktualisierung hinzu

[HAVEN](https://github.com/bitvora/haven), das persönliche Relay, mergte [PR #108](https://github.com/bitvora/haven/pull/108) mit periodischer [Web of Trust](/de/topics/web-of-trust/)-Aktualisierung. Die Funktion stellt sicher, dass Vertrauensbewertungen aktuell bleiben, während sich die sozialen Graphen der Benutzer entwickeln, was die Spam-Filtergenauigkeit im Laufe der Zeit verbessert.

### nostr-tools

[nostr-tools](https://github.com/nbd-wtf/nostr-tools), die Kern-JavaScript-Bibliothek, erhielt diese Woche mehrere Verbesserungen. Commits umfassen einen [Fix für Hashtag-Parsing nach Zeilenumbrüchen](https://github.com/nbd-wtf/nostr-tools/commit/c2423f7f31853d97fef2e3d649204cec328e81d5) in [NIP-27 (Textnotiz-Referenzen)](/de/topics/nip-27/)-Erwähnungen, [automatisches Pruning von kaputten Relay-Objekten mit Idle-Tracking](https://github.com/nbd-wtf/nostr-tools/commit/ab802c8dbe35d29feb732ba54e82a346c21c32e2) für Verbindungs-Cleanup, [Message-Queue-Entfernung](https://github.com/nbd-wtf/nostr-tools/commit/be9b91318fea6a0cb154b8734a15b50a4c1e7638) für Single-Threaded-Leistungsoptimierung und [Source-File-Exports](https://github.com/nbd-wtf/nostr-tools/commit/05b1fba5113182ac0aa3c72d1f511cd956a7c139) für bessere TypeScript-Imports.

### NDK

[NDK](https://github.com/nostr-dev-kit/ndk) lieferte [beta.71](https://github.com/nostr-dev-kit/ndk/commit/26abea24726ed844fdd091744ac9f768f1a530a0) mit einem [Fix für Reconnection nach Geräte-Sleep/Wake-Zyklen und Stale-Connection-Handling](https://github.com/nostr-dev-kit/ndk/commit/33e759508bc656dc45d3d77c741edf581af323f3), der Zuverlässigkeitsprobleme für mobile Anwendungen adressiert.

### Notedeck

[Notedeck](https://github.com/damus-io/notedeck), der Desktop-Client des Damus-Teams, hat einen [offenen PR #1279](https://github.com/damus-io/notedeck/pull/1279), der einen [NIP-34 (Git-Zusammenarbeit)](/de/topics/nip-34/)-Viewer hinzufügt. Dies würde das Durchsuchen von Git-Repositories, Patches und Issues ermöglichen, die auf Nostr-Relays veröffentlicht wurden, direkt innerhalb des Clients, was Notedeck zu einem potenziellen Frontend für ngit-basierte Workflows macht.

### njump

[njump](https://github.com/fiatjaf/njump), das Nostr-Web-Gateway, fügte Unterstützung für zwei [NIP-51 (Listen)](/de/topics/nip-51/)-Event-Typen via [PR #152](https://github.com/fiatjaf/njump/pull/152) hinzu. Das Gateway rendert jetzt kind:30000 Follow Sets, die kategorisierte Gruppierungen von Benutzern sind, die Clients in verschiedenen Kontexten anzeigen können, und kind:39089 Starter Packs, die kuratierte Profilsammlungen sind, die für Teilen und Gruppen-Following konzipiert sind. Diese Ergänzungen lassen njump community-kuratierte Listen anzeigen, wenn Benutzer nevent-Links teilen.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), der Android-Client, behob einen Bug, der das Teilen von Videos aus der Player-Ansicht verhinderte ([PR #1695](https://github.com/vitorpamplona/amethyst/pull/1695)). Die "Video teilen"-Option erschien nicht, weil der Content-Parameter nicht an die Control-Buttons-Komponente übergeben wurde. Benutzer können jetzt Nostr-Video-Inhalte direkt aus dem Player an andere Apps teilen. [PR #1693](https://github.com/vitorpamplona/amethyst/pull/1693) behebt Jackson-JSON-Deserialisierungs-Crashes, die beim Parsen bestimmter fehlerhafter Events auftraten.

### Jumble

[Jumble](https://github.com/CodyTseng/jumble), der Web-Client fokussiert auf Relay-Feed-Browsing, fügte Audio-Datei-Uploads via Zwischenablage in [PR #743](https://github.com/CodyTseng/jumble/pull/743) hinzu. Benutzer können jetzt Audio-Dateien direkt in den Post-Editor einfügen, der sie zu konfigurierten Medienservern hochlädt und die URL in der Notiz einbettet. Die Funktion spiegelt bestehende Bild-Einfüge-Funktionalität wider.

### Flotilla

[Flotilla](https://github.com/coracle-social/flotilla), hodlbods [NIP-29 (Relay-basierte Gruppen)](/de/topics/nip-29/)-Communities-Client, lieferte Benachrichtigungen via [PR #270](https://github.com/coracle-social/flotilla/pull/270). Das Update refaktoriert das Alert-System von Anchor-basiertem Polling zu lokalen Pull-Benachrichtigungen für Web und Push-Benachrichtigungen für Mobile. Die Architektur implementiert den vorgeschlagenen NIP-9a-Standard (siehe [PR #2194](https://github.com/nostr-protocol/nips/pull/2194) unten), bei dem Benutzer Webhook-Callbacks bei Relays registrieren und verschlüsselte Event-Payloads erhalten, wenn Filter matchen.

### Formstr

[Formstr](https://github.com/abh3po/nostr-forms), die Nostr-native Formular-Anwendung, fügte Formular-Import und verschlüsselte Formular-Unterstützung in [PR #422](https://github.com/abh3po/nostr-forms/pull/422) hinzu. Benutzer können jetzt bestehende Formulare aus JSON oder anderen Formstr-Instanzen importieren. Die Verschlüsselungsfunktion erlaubt Formularerstellern, Antworten einzuschränken, sodass nur bestimmte Empfänger Einsendungen lesen können, nützlich für Umfragen, die sensible Informationen sammeln.

### Pollerama

[Pollerama](https://pollerama.fun), aufgebaut auf der [nostr-polls](https://github.com/abh3po/nostr-polls)-Bibliothek, fügte [NIP-17](/de/topics/nip-17/)-DM-Teilen für Umfragen via [PR #141](https://github.com/abh3po/nostr-polls/pull/141) und [PR #142](https://github.com/abh3po/nostr-polls/pull/142) hinzu. Benutzer können jetzt Umfragen direkt an Kontakte durch verschlüsselte Direktnachrichten teilen.

### Nostrability Schemata

[Nostrability schemata](https://github.com/nostrability/schemata), die JSON-Verifizierungsschema-Sammlung für Nostr-Events, fügte [NIP-59 (Gift Wrap)](/de/topics/nip-59/)-Abdeckung via [PR #59](https://github.com/nostrability/schemata/pull/59) hinzu. Das Update enthält Schemata für kind 13 (seal) und kind 1059 (gift wrap) Events, die die bestehende [NIP-17](/de/topics/nip-17/)-Schema-Abdeckung ergänzen.

### Vector

[Vector](https://github.com/VectorPrivacy/Vector), der datenschutzfokussierte Desktop-Messenger mit [NIP-17](/de/topics/nip-17/), [NIP-44](/de/topics/nip-44/) und [NIP-59](/de/topics/nip-59/) für Zero-Metadata-Verschlüsselung, mergte [PR #39](https://github.com/VectorPrivacy/Vector/pull/39) mit SIMD-beschleunigten Leistungsoptimierungen. Hex-Encoding läuft 65x schneller, Bildvorschau-Generierung bis zu 38x schneller und Nachrichtensuchen 184x schneller durch Binary-Search-Indexierung. Der PR fügt ARM64 NEON Intrinsics für Apple Silicon und x86_64 AVX2/SSE2 mit Runtime-Erkennung für Windows und Linux hinzu. Der Speicherverbrauch sank mit Message-Structs, die von 472 auf 128 Bytes reduziert wurden, und npub-Speicherung um 99,6% durch Interning gekürzt.

Vector v0.3.0 (Dezember 2025) integrierte [MDK (Marmot Development Kit)](https://github.com/marmot-protocol/mdk) für MLS-Protokoll-basierte Gruppennachrichten und brachte Ende-zu-Ende-verschlüsselte Gruppen mit Forward Secrecy zum Client. MIP-04-Dateifreigabe handhabt jetzt imeta-Anhänge für MLS-Gruppen, konzipiert für Interoperabilität mit [White Noise](/de/newsletters/2026-01-28-newsletter/#marmot-typescript-sdk-adds-message-history). Das Release führte auch eine Mini-Apps-Plattform mit WebXDC-basierten P2P-Multiplayer-Spielen ein, einen dezentralisierten App-Store namens The Nexus, PIVX-Wallet-Integration für In-App-Zahlungen, Nachrichtenbearbeitung mit vollständiger Verlaufsverfolgung und 4x Speicherreduktion während Bild-Uploads.

## NIP-Updates

Aktuelle Änderungen am [NIPs-Repository](https://github.com/nostr-protocol/nips):

**Gemerged:**

- **[NIP-47: Hold-Invoice-Unterstützung](https://github.com/nostr-protocol/nips/pull/1913)** - [NIP-47 (Nostr Wallet Connect)](/de/topics/nip-47/) unterstützt jetzt Hold-Invoices und ermöglicht fortgeschrittene Zahlungsworkflows, bei denen Empfänger Zahlungen explizit abwickeln oder stornieren müssen. Der PR fügt drei neue RPC-Methoden hinzu: `make_hold_invoice` erstellt eine Hold-Invoice unter Verwendung eines vorgenerierten Preimage und Payment-Hash, `settle_hold_invoice` beansprucht Zahlung durch Bereitstellung des originalen Preimage, und `cancel_hold_invoice` lehnt Zahlung unter Verwendung seines Payment-Hash ab. Eine neue `hold_invoice_accepted`-Benachrichtigung feuert, wenn ein Zahler Zahlung sperrt. Dies ermöglicht Anwendungsfälle wie Pay-to-Unlock-Inhalte, Marktplatz-Escrow-Systeme und Payment-Gating. Implementierungen sind bereits in Arbeit in [Alby Hub](https://github.com/getAlby/hub/pull/1298), [Alby JS-SDK](https://github.com/getAlby/js-sdk/pull/382) und [dart NDK](https://github.com/relaystr/ndk/pull/147).

- **[NIP-05: Kleinschreibungsanforderung](https://github.com/nostr-protocol/nips/pull/2208)** - [NIP-05 (Domain-Verifizierung)](/de/topics/nip-05/) erfordert jetzt explizit Kleinschreibung für sowohl Hex-Public-Keys als auch lokale Namen in der `nostr.json`-Datei. Dies war implizit in der Spezifikation, aber nicht angegeben, was Interoperabilitätsprobleme verursachte, wenn einige Implementierungen gemischte Groß-/Kleinschreibung verwendeten, während andere auf Kleinschreibung normalisierten. Clients, die NIP-05-Identifikatoren validieren, sollten jetzt alle `nostr.json`-Antworten ablehnen, die Großbuchstaben in Schlüsseln oder Namen enthalten.

- **[NIP-73: Ländercodes](https://github.com/nostr-protocol/nips/pull/2205)** - [NIP-73 (Geotags)](/de/topics/nip-73/) unterstützt jetzt ISO 3166-Ländercodes als Alternative zu Geohashes. Events können `["g", "US", "countryCode"]`-Tags enthalten, um Standort auf Länderebene anzuzeigen, ohne präzise Koordinaten zu erfordern. Dies ermöglicht länderbasierte Inhaltsfilterung und -entdeckung für Anwendungen, bei denen exakter Standort unnötig oder unerwünscht ist. Der PR fügte auch ein fehlendes Geohash-Beispiel zur Spec-Dokumentation hinzu.

**Offene PRs und Diskussionen:**

- **[NIP-82: Software-Anwendungen](https://github.com/nostr-protocol/nips/pull/1336)** - franzap kündigte ein großes Update dieser Entwurfsspezifikation an, die definiert, wie Software-Anwendungen über Nostr mit kind 30063 Release-Events verteilt werden. Das Update deckt jetzt ungefähr 98% der Geräteplattformen global ab, einschließlich macOS, Linux, Windows, FreeBSD, WASM-Umgebungen, VS Code-Erweiterungen, Chrome-Erweiterungen und Web Bundles/PWAs. Das Team fokussiert sich als nächstes auf Android-, PWA- und iOS-Unterstützung und lädt Entwickler ein, sich auf diesen gemeinsamen Standard zu einigen. Zapstore plant, in den kommenden Wochen auf das neue Format zu migrieren.

- **[NIP-74: Podcasts](https://github.com/nostr-protocol/nips/pull/2211)** - Definiert adressierbare Events für Podcast-Shows (kind 30074) und Episoden (kind 30075). Shows enthalten Metadaten wie Titel, Beschreibung, Kategorien und Cover-Bilder. Episoden referenzieren ihre Eltern-Show und enthalten Enclosure-URLs, Dauern und Kapitelmarker. Die Spec integriert sich mit Podcasting 2.0-Metadaten-Standards und enthält Value-Tags für V4V (Value-for-Value)-Monetarisierung via Lightning. Plattformen wie [transmit.fm](https://transmit.fm), eine Nostr-native Podcast-Publishing-Plattform, können direkt zu Relays mit diesem Format publizieren, was Podcastern ermöglicht, Inhalte ohne Intermediäre zu verteilen.

- **[NIP-FR: Friends-Only Notes](https://github.com/nostr-protocol/nips/pull/2207)** - Schlägt einen Mechanismus vor, um Notizen nur für gegenseitige Follows sichtbar zu veröffentlichen. Die Implementierung verwendet [NIP-59 (Gift Wrap)](/de/topics/nip-59/) zur Verschlüsselung von Inhalten: Der Autor erstellt eine reguläre Notiz, dann gift-wrapped Kopien an jeden gegenseitigen Follow. Die Kopie jedes Empfängers wird mit NIP-44 an seinen pubkey verschlüsselt und über den Gift-Wrap-Mechanismus gesendet. Empfänger können verifizieren, dass die Notiz von jemandem kam, dem sie folgen, während Nicht-Gegenseitige den Inhalt nicht zugreifen können. Dieser Ansatz wiederverwendet bestehende kryptographische Infrastruktur, während er eine häufig angefragte Datenschutzfunktion ermöglicht.

- **[NIP-DB: Browser Nostr Event Database Interface](https://github.com/hzrd149/nostr-bucket)** - Schlägt ein Standard-`window.nostrdb`-Interface für Browser-Erweiterungen vor, die lokalen Nostr-Event-Speicher bereitstellen. Die API enthält Methoden zum Hinzufügen von Events, Abfragen nach ID oder Filter, Zählen von Treffern und Abonnieren von Updates. Web-Anwendungen können dieses Interface verwenden, um aus lokal gecachten Events zu lesen, ohne Relay-Anfragen zu machen, was Bandbreite und Latenz reduziert. hzrd149s [nostr-bucket](https://github.com/hzrd149/nostr-bucket)-Browser-Erweiterung bietet eine Referenzimplementierung und injiziert das Interface in alle Browser-Tabs. Eine begleitende [Polyfill-Bibliothek](https://github.com/hzrd149/window.nostrdb.js) implementiert dieselbe API mit IndexedDB für Umgebungen ohne die Erweiterung.

- **[TRUSTed Filters](https://github.com/nostr-protocol/nips/pull/1534)** - Eine Suite von fünf verwandten Vorschlägen für dezentralisierte Inhaltskuration, aufbauend auf vitorpamplonas [Trusted Assertions PR #1534](https://github.com/nostr-protocol/nips/pull/1534). Die Kernspezifikation führt kind 17570 Events zum Deklarieren von Trust-Provider-Präferenzen ein, was Benutzern ermöglicht zu spezifizieren, welchen Diensten sie für Event-Filterung und -Ranking vertrauen. Trust-Provider veröffentlichen Assertions (kind 37571), Statistiken (kind 37572) und Rankings (kind 37573), die Clients abonnieren können. Das System verwendet eine Plugin-Architektur mit W/w-Tags zur Spezifizierung von Filter-Typen und -Transformationen. Dies ermöglicht rechenintensive Operationen wie Spam-Erkennung, Reputationsbewertung und Inhalts-Ranking auf dedizierter Infrastruktur laufen zu lassen, während Benutzer Kontrolle darüber behalten, welchen Providern sie vertrauen. Die Suite enthält separate Specs für Filter-Presets, Benutzer-Rankings, vertrauenswürdige Events und Plugin-Definitionen.

- **[NIP-9a: Push-Benachrichtigungen](https://github.com/nostr-protocol/nips/pull/2194)** - hodlbod schlägt einen Standard für Relay-basierte Push-Benachrichtigungen mit kind 30390 Registrierungs-Events vor. Benutzer erstellen eine Registrierung, die Filter für Events enthält, die sie empfangen möchten, und eine Webhook-Callback-URL. Die Registrierung wird an den pubkey des Relays verschlüsselt (aus seinem NIP-11 `self`-Feld). Wenn passende Events auftreten, POSTen Relays zum Callback mit der Event-ID (Klartext zur Deduplizierung) und dem Event selbst (NIP-44-verschlüsselt an den Benutzer). Diese Architektur lässt Relays Benachrichtigungen pushen, während Event-Inhalte vor intermediären Push-Servern geschützt werden. Flotillas [PR #270](https://github.com/coracle-social/flotilla/pull/270) implementiert diesen Standard.

- **[Catallax](https://github.com/SigmaEnterprise/Catallax)** - Schlägt ein dezentralisiertes Vertragsarbeitsprotokoll mit Escrow unter Verwendung von kind 33400 Events vor. Das System definiert drei Rollen: Schlichter kündigen Verfügbarkeit und Bedingungen an, Auftraggeber erstellen finanzierte Aufgaben mit gesperrtem Bitcoin, und freie Agenten erledigen Arbeit, um Zahlung zu beanspruchen. Schlichter lösen bei Bedarf Streitigkeiten. Das Protokoll ermöglicht vertrauenslose Freelance-Arbeitskoordination, bei der Mittel gesperrt sind, bis Lieferungen akzeptiert oder Schlichtung abgeschlossen sind.

## NIP Deep Dive: NIP-47 (Nostr Wallet Connect)

[NIP-47](/de/topics/nip-47/) definiert Nostr Wallet Connect (NWC), ein Protokoll für Remote-Lightning-Wallet-Steuerung unter Verwendung von Nostr als Kommunikationsschicht. Mit der Hold-Invoice-Unterstützungs-Ergänzung dieser Woche deckt NWC jetzt das volle Spektrum von Lightning-Operationen ab.

Das Protokoll funktioniert durch einen einfachen Austausch. Eine Wallet-Anwendung veröffentlicht ein "Wallet-Info"-Event (kind 13194), das ihre Fähigkeiten beschreibt. Client-Anwendungen senden verschlüsselte Anfragen (kind 23194), die das Wallet bitten, Operationen wie das Bezahlen von Invoices, Erstellen von Invoices oder Prüfen von Salden durchzuführen. Das Wallet antwortet mit verschlüsselten Ergebnissen (kind 23195).

NWC verwendet [NIP-44](/de/topics/nip-44/)-Verschlüsselung zwischen Client und Wallet mit einem dedizierten Schlüsselpaar für Wallet-Operationen, das von der Hauptidentität des Benutzers getrennt bleibt. Diese Trennung bedeutet, dass das Kompromittieren einer NWC-Verbindung die Nostr-Identität des Benutzers nicht offenlegt.

**Unterstützte Methoden:**

Die Spec definiert Methoden für Kern-Lightning-Operationen: `pay_invoice` sendet Zahlungen, `make_invoice` generiert Invoices zum Empfangen, `lookup_invoice` prüft Zahlungsstatus, `get_balance` gibt das Wallet-Guthaben zurück, und `list_transactions` liefert Zahlungshistorie. Das neu gemergte `pay_keysend` ermöglicht Zahlungen ohne Invoices, und `hold_invoice` unterstützt bedingte Zahlungen.

**Beispiel-Events:**

Der Wallet-Dienst veröffentlicht ein Info-Event (kind 13194), das seine Fähigkeiten bewirbt:

```json
{
  "kind": 13194,
  "pubkey": "<wallet service pubkey>",
  "content": "pay_invoice get_balance make_invoice lookup_invoice list_transactions notifications",
  "tags": [
    ["encryption", "nip44_v2"],
    ["notifications", "payment_received payment_sent"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<wallet service signature>"
}
```

Ein Client sendet eine verschlüsselte Anfrage (kind 23194), um eine Invoice zu bezahlen:

```json
{
  "kind": 23194,
  "pubkey": "<client ephemeral pubkey from connection URI secret>",
  "content": "<NIP-44 encrypted: {\"method\": \"pay_invoice\", \"params\": {\"invoice\": \"lnbc50n1...\"}}>",
  "tags": [
    ["p", "<wallet service pubkey>"],
    ["encryption", "nip44_v2"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<client ephemeral key signature>"
}
```

Der Wallet-Dienst antwortet (kind 23195) mit dem Zahlungsergebnis:

```json
{
  "kind": 23195,
  "pubkey": "<wallet service pubkey>",
  "content": "<NIP-44 encrypted: {\"result_type\": \"pay_invoice\", \"result\": {\"preimage\": \"...\"}, \"error\": null}>",
  "tags": [
    ["p", "<client ephemeral pubkey>"],
    ["e", "<request event id>"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<wallet service signature>"
}
```

Der `e`-Tag in der Antwort referenziert die ursprüngliche Anfrage, was Clients ermöglicht, Antworten ihren Anfragen zuzuordnen.

**Hold Invoices:**

Der [PR #1913](https://github.com/nostr-protocol/nips/pull/1913) dieser Woche fügte Hold-Invoice-Unterstützung hinzu und ermöglicht Escrow-artige Zahlungen. Im Gegensatz zu Standard-Invoices, bei denen der Empfänger Zahlung sofort durch Freigabe des Preimage beansprucht, lassen Hold-Invoices den Empfänger diese Entscheidung aufschieben. Wenn ein Zahler an eine Hold-Invoice sendet, sperren sich Mittel entlang der Zahlungsroute. Der Empfänger wählt dann entweder abwickeln (Preimage freigeben und Mittel beanspruchen) oder stornieren (Zahlung ablehnen, Mittel an den Zahler zurückgeben). Wenn keine Aktion erfolgt, läuft die Zahlung ab und Mittel kehren automatisch zurück. Der PR fügt drei NWC-Methoden hinzu: `make_hold_invoice`, `settle_hold_invoice` und `cancel_hold_invoice`, plus eine `hold_invoice_accepted`-Benachrichtigung. Dieser Mechanismus treibt Anwendungen wie Ridestrs Rideshare-Escrow und Marktplatz-Streitbeilegung an.

**Aktuelle Implementierungen:**

Große Wallets unterstützen NWC: Zeus, Alby und Primal (ab dem [PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874) dieser Woche) implementieren alle Wallet-seitige Unterstützung. Auf der Client-Seite können Damus, Amethyst und die meisten großen Nostr-Clients sich mit NWC-Wallets für Zapping und Zahlungen verbinden.

Das Protokoll ermöglicht eine Trennung der Zuständigkeiten: Benutzer können ihr Wallet auf einem Gerät betreiben, während sie von einem anderen mit Nostr interagieren, wobei Nostr-Relays als Kommunikationskanal dienen. Diese Architektur bedeutet, dass mobile Clients Mittel nicht direkt halten müssen, was die Sicherheit verbessert, indem Wallet-Infrastruktur von sozialen Clients getrennt bleibt.

**Sicherheitsüberlegungen:**

NWC-Verbindungen sollten als sensitiv behandelt werden. Während die Verschlüsselung Nachrichteninhalte schützt, müssen Wallet-pubkey und Verbindungsgeheimnis geschützt werden. Anwendungen sollten Benutzern ermöglichen, Verbindungen zu widerrufen und Ausgabelimits zu setzen. Das Protokoll unterstützt Fähigkeitsbeschränkungen, sodass Wallets limitieren können, welche Operationen eine bestimmte Verbindung durchführen kann.

## NIP Deep Dive: NIP-59 (Gift Wrap)

[NIP-59](/de/topics/nip-59/) definiert ein Protokoll zum Einkapseln beliebiger Nostr-Events in mehrere Verschlüsselungsschichten, das die Identität des Absenders vor Relays und Beobachtern verbirgt. Die Vorschläge dieser Woche für Friends-Only Notes (NIP-FR) und Push-Benachrichtigungen (NIP-9a) verlassen sich beide auf Gift Wrapping, was es zu einem grundlegenden Datenschutz-Primitiv macht, das es wert ist, verstanden zu werden.

**Die drei Schichten:**

Gift Wrapping verwendet drei verschachtelte Strukturen:

1. **Rumor** (unsigniertes Event): Der ursprüngliche Inhalt als Nostr-Event ohne Signatur. Der Rumor kann nicht direkt an Relays gesendet werden, weil Relays unsignierte Events ablehnen.

2. **Seal** (kind 13): Der Rumor wird mit [NIP-44](/de/topics/nip-44/) verschlüsselt und in ein kind 13 Event platziert. Der Seal IST vom tatsächlichen Schlüssel des Autors signiert. Dies ist der kryptographische Beweis der Autorschaft.

3. **Gift Wrap** (kind 1059): Der Seal wird verschlüsselt und in ein kind 1059 Event platziert, das von einem zufälligen, einmaligen Schlüsselpaar signiert ist. Der Gift Wrap enthält einen `p`-Tag für das Routing zum Empfänger.

**Ein häufiges Missverständnis: Abstreitbarkeit**

Die Spec erwähnt, dass unsignierte Rumors "Abstreitbarkeit" bieten, aber das ist irreführend. Die Seal-Schicht IST vom echten Autor signiert. Wenn der Empfänger den Gift Wrap und dann den Seal entschlüsselt, hat er kryptographischen Beweis, wer die Nachricht gesendet hat. Der Empfänger könnte sogar einen Zero-Knowledge-Proof konstruieren, der die Identität des Absenders offenlegt, ohne seinen eigenen privaten Schlüssel preiszugeben.

Was Gift Wrap tatsächlich bietet, ist **Absender-Privatsphäre vor Beobachtern**: Relays und Dritte können nicht bestimmen, wer die Nachricht gesendet hat, weil sie nur den Gift Wrap sehen, der von einem zufälligen Schlüssel signiert ist. Aber der Empfänger weiß es immer und kann es beweisen.

**Beispiel-Events:**

Hier ist die vollständige Drei-Schichten-Struktur aus der Spec (Senden von "Gehst du heute Abend zur Party?"):

Der Rumor (unsigniert, kann nicht an Relays veröffentlicht werden):
```json
{
  "created_at": 1691518405,
  "content": "Are you going to the party tonight?",
  "tags": [],
  "kind": 1,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "id": "9dd003c6d3b73b74a85a9ab099469ce251653a7af76f523671ab828acd2a0ef9"
}
```

Der Seal (kind 13, vom echten Autor signiert, enthält verschlüsselten Rumor):
```json
{
  "kind": 13,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "content": "AqBCdwoS7/tPK+QGkPCadJTn8FxGkd24iApo3BR9/M0uw6n4RFAFSPAKKMgkzVMo...",
  "created_at": 1703015180,
  "tags": [],
  "id": "28a87d7c074d94a58e9e89bb3e9e4e813e2189f285d797b1c56069d36f59eaa7",
  "sig": "02fc3facf6621196c32912b1ef53bac8f8bfe9db51c0e7102c073103586b0d29..."
}
```

Der Gift Wrap (kind 1059, von zufälligem ephemerem Schlüssel signiert, enthält verschlüsselten Seal):
```json
{
  "kind": 1059,
  "pubkey": "18b1a75918f1f2c90c23da616bce317d36e348bcf5f7ba55e75949319210c87c",
  "content": "AhC3Qj/QsKJFWuf6xroiYip+2yK95qPwJjVvFujhzSguJWb/6TlPpBW0CGFwfuf...",
  "created_at": 1703021488,
  "tags": [["p", "166bf3765ebd1fc55decfe395beff2ea3b2a4e0a8946e7eb578512b555737c99"]],
  "id": "5c005f3ccf01950aa8d131203248544fb1e41a0d698e846bd419cec3890903ac",
  "sig": "35fabdae4634eb630880a1896a886e40fd6ea8a60958e30b89b33a93e6235df7..."
}
```

Beachten: der `pubkey` des Seals ist der echte Autor (`611df01...`), während der `pubkey` des Gift Wraps ein zufälliger Einmal-Schlüssel ist (`18b1a75...`). Relays sehen nur den Gift Wrap, sodass sie die Nachricht nicht dem echten Autor zuordnen können.

**Was jede Schicht schützt:**

Der Rumor ist unsigniert und kann nicht direkt an Relays veröffentlicht werden. Der Seal ist vom echten Autor signiert und beweist Autorschaft gegenüber dem Empfänger. Der Gift Wrap ist von einem zufälligen Einmal-Schlüssel signiert und verbirgt den echten Autor vor Relays und Beobachtern. Nur der Empfänger kann durch beide Schichten entschlüsseln, um zum ursprünglichen Inhalt zu gelangen und die Signatur des Autors auf dem Seal zu verifizieren.

**Aktuelle Anwendungen:**

[NIP-17 (Private Direktnachrichten)](/de/topics/nip-17/) verwendet Gift Wrap für verschlüsselte DMs und ersetzt das ältere NIP-04-Schema. Das vorgeschlagene NIP-FR (Friends-Only Notes) gift-wrapped Notizen an jeden gegenseitigen Follow. NIP-9a (Push-Benachrichtigungen) verschlüsselt Benachrichtigungs-Payloads unter Verwendung von Gift-Wrap-Prinzipien.

**Metadaten-Schutz:**

Zeitstempel sollten randomisiert werden, um Timing-Analysen zu vereiteln. Relays sollten AUTH anfordern, bevor sie kind 1059 Events ausliefern, und sie nur an den markierten Empfänger liefern. Beim Senden an mehrere Empfänger separate Gift Wraps für jeden erstellen.

---

Das war's für diese Woche. Baust du etwas? Hast du Neuigkeiten zu teilen? Möchtest du, dass wir über dein Projekt berichten? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Kontaktiere uns per NIP-17 DM</a> oder finde uns auf Nostr.
