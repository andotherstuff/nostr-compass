---
title: 'Nostr Compass #16'
date: 2026-04-01
translationOf: /en/newsletters/2026-04-01-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, deinem wöchentlichen Wegweiser durch Nostr.

**Diese Woche:** [Amethyst](https://github.com/vitorpamplona/amethyst) liefert [v1.07.0](#amethyst-liefert-angepinnte-notizen-relay-management-und-request-to-vanish) mit angepinnten Notizen, Relay-Management über [NIP-86](/de/topics/nip-86/) und [NIP-62](/de/topics/nip-62/) Request-to-Vanish-Unterstützung. [NIP-5A](#nip-5a-wird-gemergt-und-bringt-statische-websites-auf-nostr) (Static Websites) wird ins NIPs-Repository gemergt und definiert, wie Websites unter Nostr-Schlüsselpaaren mit [Blossom](/de/topics/blossom/)-Speicher gehostet werden. [Flotilla](https://gitea.coracle.social/coracle/flotilla) liefert [v1.7.0](#flotilla-v170-fügt-voice-rooms-und-email-login-hinzu) mit Voice Rooms, Email/Password-Login und Proof-of-Work-DMs. [White Noise](https://github.com/marmot-protocol/whitenoise) behebt Relay-Churn in [v2026.3.23](#white-noise-behebt-relay-churn-und-erweitert-client-kontrollen), [nospeak](https://github.com/psic4t/nospeak) startet sein [1.0.0](#nospeak-startet-als-10-private-messenger) als Messenger ohne Anmeldung. [Nymchat](https://github.com/Spl0itable/NYM) [übernimmt Marmot](#nymchat-liefert-marmot-basierte-gruppenchats) für MLS-verschlüsselte Gruppenchats mit NIP-17-Fallback. [Calendar by Form*](https://github.com/formstr-hq/nostr-calendar) erreicht [v1.0.0](#calendar-by-form-v100) mit privaten Kalenderlisten und ICS-Import, [Amber](https://github.com/greenart7c3/Amber) fügt [Mnemonic-Recovery und NIP-42-Relay-Auth-Whitelisting](#amber-v502-bis-v504) hinzu, und die [Marmot-Spezifikation](#marmot-verschiebt-keypackages-zu-adressierbaren-events-und-verschärft-push-benachrichtigungen) verschiebt KeyPackages zu adressierbaren Events und verschärft das MIP-05-Push-Benachrichtigungsformat.

## Neuigkeiten

### Amethyst liefert angepinnte Notizen, Relay-Management und Request to Vanish

[Amethyst](https://github.com/vitorpamplona/amethyst), der Android-Client gepflegt von vitorpamplona, lieferte sechs Releases in drei Tagen, von [v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0) bis [v1.07.5](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.5). Das Hauptfeature-Set umfasst sechs Protokolloberflächen: angepinnte Notizen, einen dedizierten Polls-Feed-Bildschirm, [NIP-62](/de/topics/nip-62/) (Request to Vanish) Unterstützung für das Anfordern vollständiger Event-Löschung von Relays, [NIP-86](/de/topics/nip-86/) (Relay Management API) innerhalb des Clients, [NIP-66](/de/topics/nip-66/) (Relay Discovery and Liveness Monitoring) Assessments im Relay-Info-Bildschirm und [NIP-43](/de/topics/nip-43/) (Relay Access Metadata and Requests) Anzeige von Mitgliedsinformationen.

[NIP-86](/de/topics/nip-86/) definiert eine JSON-RPC-Schnittstelle für Relay-Betreiber, die Clients ermöglicht, administrative Befehle wie das Sperren von Pubkeys, das Erlauben von Pubkeys und das Auflisten gesperrter Nutzer über eine standardisierte API zu senden. Amethyst stellt dies nun direkt in seiner Relay-Management-UI bereit, sodass Nutzer, die ihre eigenen Relays betreiben, sie aus demselben Client verwalten können, den sie zum Posten verwenden. [PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039) ersetzt den alten Hex-Input-Dialog für gesperrte und erlaubte Pubkeys durch einen interaktiven Nutzersuchdialog.

v1.07.2 fügte GIF-Keyboard-Uploads hinzu und behob eine Signing-Regression, bei der Amber-Ablehnungsantworten falsch gelesen wurden, weil ältere Amber-Versionen einen leeren String für das `rejected`-Feld zurückgaben ([PR #2042](https://github.com/vitorpamplona/amethyst/pull/2042)). v1.07.5 behebt einen Absturz beim Bild-Upload. Die Releases [v1.06.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.2) und [v1.06.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.3) früher in der Woche fügten einen Poll-Typ-Selektor für Einzel- versus Mehrfachauswahl-Polls, Drag-to-Seek auf Video-Fortschrittsleisten und Verbesserungen beim anonymen Posten hinzu.

### NIP-5A wird gemergt und bringt statische Websites auf Nostr

[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md) (Static Websites) wurde über [PR #1538](https://github.com/nostr-protocol/nips/pull/1538) gemergt und definiert, wie statische Websites unter Nostr-Schlüsselpaaren gehostet werden. Die Spezifikation verwendet zwei Event-Kinds: Kind `15128` für eine Root-Site, eine pro Pubkey, und Kind `35128` für benannte Sites, die durch einen `d`-Tag identifiziert werden. Jedes Manifest ordnet URL-Pfade SHA256-Hashes zu, mit optionalen `server`-Tags, die auf [Blossom](/de/topics/blossom/)-Speicher-Hosts zeigen, auf denen die eigentlichen Dateien liegen.

Das Hosting-Modell funktioniert so: Ein Seitenautor baut eine statische Site, lädt die Dateien zu einem oder mehreren Blossom-Servern hoch und veröffentlicht dann ein signiertes Manifest-Event, das Pfade auf Content-Hashes abbildet. Ein Host-Server empfängt Web-Anfragen, löst den Pubkey des Autors aus der Subdomain auf, ruft das Manifest aus der [NIP-65](/de/topics/nip-65/) Relay-Liste des Autors ab und liefert Dateien aus, indem er die passenden Blobs von Blossom herunterlädt. Die Site bleibt unter Kontrolle des Autors, weil nur dieser Schlüssel ein aktualisiertes Manifest signieren kann. Der Host-Server ist austauschbar, weil jeder Server, der NIP-5A versteht, dieselbe Site aus demselben Manifest ausliefern kann.

Die Spezifikation baut auf Infrastruktur auf, die bereits existiert. [nsite](https://github.com/lez/nsite), die NIP-5A-Referenz-Host-Implementierung von lez, und [nsite-manager](https://github.com/hzrd149/nsite-manager), hzrd149s Management-UI, liefen bereits, bevor das NIP gemergt wurde. Der Merge macht die Event-Kinds und URL-Auflösungsregeln offiziell und gibt zweiten und dritten Implementierungen ein stabiles Ziel.

### White Noise behebt Relay-Churn und erweitert Client-Kontrollen

[White Noise](https://github.com/marmot-protocol/whitenoise), der private Messenger auf Basis des [Marmot](/de/topics/marmot/)-Protokolls, lieferte [v2026.3.23](https://github.com/marmot-protocol/whitenoise/releases/tag/v2026.3.23) am 25. März. Die Hauptarbeit betrifft Relay-Stabilität. Login wartet nicht mehr darauf, dass jede Relay-List-Publikation abgeschlossen ist, weil Relay-List-Publishing nun Quorum-Logik verwendet und den Rest im Hintergrund wiederholt. Einmalige Fetches und Publishes verwenden abgegrenzte ephemere Relay-Sessions, statt im langlebigen Pool zu verbleiben, wiederhergestellte Sessions holen nach dem Start ihren Group-Refresh-Pfad wieder ein, und die App stellt nun Relay-Diagnostik und Relay-State-Inspektion über [PR #495](https://github.com/marmot-protocol/whitenoise/pull/495) und [PR #502](https://github.com/marmot-protocol/whitenoise/pull/502) bereit.

Dasselbe Release ändert auch das Verhalten von Konversationen. [PR #468](https://github.com/marmot-protocol/whitenoise/pull/468) fügt NIP-C7-Reply-Threading mit `q`-Tags und `nostr:nevent`-Referenzen hinzu, [PR #471](https://github.com/marmot-protocol/whitenoise/pull/471) und [PR #512](https://github.com/marmot-protocol/whitenoise/pull/512) lassen gelöschte Nachrichten als gelöschte Platzhalter sichtbar statt sie still zu entfernen, [PR #478](https://github.com/marmot-protocol/whitenoise/pull/478) fügt einen In-App-Bugreport-Flow mit [NIP-44](/de/topics/nip-44/) (Encrypted Payloads) anonymen Berichten hinzu, und [PR #486](https://github.com/marmot-protocol/whitenoise/pull/486) fügt Support-Chat direkt im Client hinzu. Nutzerseitige Nachrichtenkontrollen landeten im selben Zeitfenster: [PR #532](https://github.com/marmot-protocol/whitenoise/pull/532) archiviert Chats, [PR #541](https://github.com/marmot-protocol/whitenoise/pull/541) fügt Mute und Unmute mit konfigurierbaren Dauern hinzu, und [PR #535](https://github.com/marmot-protocol/whitenoise/pull/535) fügt Benachrichtigungseinstellungen hinzu. [PR #539](https://github.com/marmot-protocol/whitenoise/pull/539) ist vorbereitende Push-Registrierungsarbeit und verdrahtet APNs-Registrierung auf iOS und Play-Services-Erkennung auf Android, damit Registrierung darauf aufbauen kann. Auf der Backend-Seite fügte das [MDK](https://github.com/marmot-protocol/mdk) (Marmot Development Kit) MIP-05-Push-Benachrichtigungsprimitiven und einen Notification-Request-Builder hinzu ([PR #235](https://github.com/marmot-protocol/mdk/pull/235), [PR #238](https://github.com/marmot-protocol/mdk/pull/238)), während [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs) Persistenz für Push-Benachrichtigungsregistrierung ([PR #688](https://github.com/marmot-protocol/whitenoise-rs/pull/688)), Fixes für Hintergrund-Task-Abbrüche ([PR #696](https://github.com/marmot-protocol/whitenoise-rs/pull/696)) und Key-Package-Recovery beim Start ([PR #693](https://github.com/marmot-protocol/whitenoise-rs/pull/693)) hinzufügte.

### Nostr VPN erreicht v0.3.0 mit Roster-Sync und Invite v2

[Anschließend an die Launch-Berichterstattung der letzten Woche](/de/newsletters/2026-03-25-newsletter/#nostr-vpn-startet-als-tailscale-alternative), [nostr-vpn](https://github.com/mmalmi/nostr-vpn), das Peer-to-Peer-VPN, das Nostr-Relays zur Signalisierung und WireGuard für verschlüsselte Tunnel nutzt, setzte sein schnelles Release-Tempo fort und lieferte Releases bis [v0.3.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.3). Der Versionssprung bringt zwei Breaking Changes: Das Invite-Format wechselt auf v2 (0.3.0 kann weiterhin v1-Invites importieren, ältere Builds können aber keine v2-Invites importieren), und admin-signierter Roster-Sync wurde dem Signalisierungsprotokoll hinzugefügt. Peers mit gemischten Versionen können sich auf der Mesh-Ebene weiterhin verbinden, aber ältere Peers nehmen nicht an der Roster-Synchronisierung teil.

Die Ergänzung des Roster-Syncs beginnt die Bewegung in Richtung eines verwalteten Netzwerks. Ein Admin-Node kann nun Mitgliedschaftsänderungen an alle Peers pushen, sodass das Hinzufügen oder Entfernen eines Geräts aus dem Mesh nicht verlangt, dass jeder Peer seine Konfiguration manuell aktualisiert. Die v0.2.x-Releases derselben Woche adressierten spezifische Deployment-Probleme: [v0.2.22](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.22) bis [v0.2.28](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.28) beheben Windows-Service-Management, fügen Android-Build-Skripte hinzu und verfeinern den LAN-Pairing-Flow.

### nospeak startet als 1.0-Private-Messenger

[nospeak](https://github.com/psic4t/nospeak), ein privater Messenger auf Nostr-Basis, lieferte seinen [1.0.0](https://github.com/psic4t/nospeak/releases/tag/v1.0.0)-Release am 27. März. Das Projekt umfasst Eins-zu-eins- und Gruppenkonversationen, Kontaktmanagement und eine selbst hostbare Architektur. Eins-zu-eins-Chats nutzen [NIP-17](/de/topics/nip-17/) (Private Direct Messages), das [NIP-59](/de/topics/nip-59/) (Gift Wrap) mit [NIP-44](/de/topics/nip-44/) (Encrypted Payloads) kombiniert, um den Absender vor Relays zu verbergen. Für Medien werden Dateien client-seitig mit AES-256-GCM verschlüsselt, bevor sie zu Blossom-Servern hochgeladen werden. Der Release kommt auch als Container-Image für Self-Hosting.

### Flotilla v1.7.0 fügt Voice Rooms und Email-Login hinzu

[Flotilla](https://gitea.coracle.social/coracle/flotilla), hodlbods Discord-artiger [NIP-29](/de/topics/nip-29/) (Relay-based Groups) Client rund um das Modell „Relays as groups“, lieferte [v1.7.0](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.0) und [v1.7.1](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.1) am 30. und 31. März. Das Hauptfeature sind Voice Rooms, beigesteuert von mplorentz. Nutzer können nun Voice Calls innerhalb von Gruppenchannels beitreten, mit einem Join-Dialog ([PR #109](https://gitea.coracle.social/coracle/flotilla/pulls/109)), der ihnen erlaubt, ein Audio-Eingabegerät auszuwählen und zu entscheiden, ob sie dem Voice Call beitreten oder nur den Text-Chat sehen wollen. Der Dialog löst ein UX-Problem der vorherigen Iteration: Das Betreten eines Voice-fähigen Raums aktivierte zuvor das Mikrofon zwangsweise, selbst wenn der Nutzer nur Nachrichten lesen oder Raumeinstellungen prüfen wollte.

Dasselbe Release fügt Email-und-Passwort-Login als Alternative zu Nostr-Schlüssel-basierter Auth hinzu, Proof-of-Work auf DMs, DM-Editing, neu gestaltetes Relay-Onboarding und Einstellungen, Blossom-Support-Erkennung über `supported_nips`, verbesserte Benachrichtigungs-Badges, Android-Push-Benachrichtigungs-Fallback und File-Upload-Fixes auf Android. v1.7.1 folgt mit einem Fix für Pomade-Registrierungs-Fallback bei Verwendung eines Offline-Signers.

Hodlbod baut auch [Caravel](https://gitea.coracle.social/coracle/caravel), einen Hosting-Manager und ein Dashboard für zooid-Relays, das diese Woche 40 Commits in der frühen Entwicklung verzeichnete.

### Nymchat liefert Marmot-basierte Gruppenchats

[Nymchat](https://github.com/Spl0itable/NYM) (auch bekannt als NYM, Nostr Ynstant Messenger), der ephemere Chat-Client mit Bitchat-Bridge, kündigte an, dass alle neuen Gruppenchats nun das [Marmot](/de/topics/marmot/)-Protokoll für MLS-verschlüsselte Nachrichten verwenden. Die Integration nutzt die Kinds `443`, `444` und `445` für Key Packages, Welcome Messages und Gruppennachrichten und liefert Forward Secrecy, Post-Compromise Security und null Metadaten-Leckage. Wenn ein Empfänger MLS nicht nutzen kann, fällt Nymchat auf seinen früheren [NIP-17](/de/topics/nip-17/) (Private Direct Messages) Gruppenchats-Pfad zurück, der weiterhin Ende-zu-Ende verschlüsselt ist, aber nicht die Ratchet-Tree-Eigenschaften von MLS besitzt.

Die Serien v3.55 und v3.56 konzentrierten sich diese Woche auf Randfälle bei Gruppenchats: Laden auf neuen Geräten, Leave-Verhalten, Notification-Routing und Unread-Badge-Zähler. Derselbe Zyklus patchte auch eine XSS-Schwachstelle durch unescaped HTML und fügte Keyword- und Phrase-Blocking hinzu, das auch auf Nutzernamen ausgeweitet wurde. Das macht Nymchat zu einem weiteren Marmot-Client neben [White Noise](#white-noise-behebt-relay-churn-und-erweitert-client-kontrollen) und [OpenChat](#openchat-v024-bis-v030) und erweitert die Menge an Apps, die MLS-verschlüsselte Gruppennachrichten über dasselbe Protokoll austauschen können.

## Releases

### Calendar by Form* v1.0.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), die dezentrale Kalender-App auf Basis von [NIP-52](/de/topics/nip-52/) (Calendar Events), erreichte [v1.0.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.0.0) am 29. März. Der Release fügt private Kalenderlisten mit verschlüsselten Nostr-Events (Kind `32123`) und [NIP-44](/de/topics/nip-44/) (Encrypted Payloads) Self-Encryption hinzu, sodass Nutzer Events in privaten Sammlungen organisieren können, ohne die Gruppierung Relays preiszugeben. Derselbe Release fügt ICS-Intent-Behandlung zum Import von Kalenderdaten aus anderen Anwendungen und Invitation Requests zum Teilen von Events zwischen Nutzern hinzu.

### Amber v5.0.2 bis v5.0.4

[Amber](https://github.com/greenart7c3/Amber), die [NIP-55](/de/topics/nip-55/) (Android Signer Application) Signer-App, lieferte drei Punkt-Releases: [v5.0.2](https://github.com/greenart7c3/Amber/releases/tag/v5.0.2), [v5.0.3](https://github.com/greenart7c3/Amber/releases/tag/v5.0.3) und [v5.0.4](https://github.com/greenart7c3/Amber/releases/tag/v5.0.4). Die sichtbarste Ergänzung ist Mnemonic-Recovery-Phrase-Login ([PR #358](https://github.com/greenart7c3/Amber/pull/358)), das Nutzern erlaubt, ihren Signer aus einer BIP39-Seed-Phrase wiederherzustellen, statt den rohen nsec- oder ncryptsec-String zu benötigen. [PR #357](https://github.com/greenart7c3/Amber/pull/357) fügt eine [NIP-42](/de/topics/nip-42/) Relay-Auth-Whitelist hinzu, sodass Nutzer einschränken können, welche Relays Client-Authentifizierung anfordern dürfen. [PR #353](https://github.com/greenart7c3/Amber/pull/353) fügt Encryption-Scope-Auswahl für Decrypt-Berechtigungen hinzu, sodass Nutzer NIP-04-only- oder NIP-44-only-Decrypt-Zugriff statt einer pauschalen Berechtigung gewähren können. v5.0.4 behebt einen Bug, bei dem Ablehnung Scoped-Encrypt- und -Decrypt-Berechtigungen nicht respektierte, und verbessert die Performance beim Empfang mehrerer Bunker-Requests.

### Aegis v0.4.0

[Aegis](https://github.com/ZharlieW/Aegis), der plattformübergreifende Signer, lieferte [v0.4.0](https://github.com/ZharlieW/Aegis/releases/tag/v0.4.0) am 26. März. Der Release fügt Full- und Selective-Authorization-Modi in den Einstellungen hinzu und behebt mehrere QR-Scanning-Probleme. Folge-Commits [d4f799f](https://github.com/ZharlieW/Aegis/commit/d4f799fe51dd82968d54f72ac77f2de29d0cfe6b), [3313af9](https://github.com/ZharlieW/Aegis/commit/3313af92e55e449ebc98fbd91a085bd444d716e7), [3b214e4](https://github.com/ZharlieW/Aegis/commit/3b214e4176f5dbe7f18690d0996e69dd151fe00f) und [e4f40b6](https://github.com/ZharlieW/Aegis/commit/e4f40b6f1f48c2dae1bb5e4246df26c26dba419e) setzen dieselbe Arbeit fort mit Batch-Select-Kontrollen, wiederverwendbaren Batch-Selection-Statistiken, Set-All-Groups-Selection-APIs und Pro-Berechtigung-Nutzungsstatistiken auf der App-Permissions-Seite.

### Schemata v0.2.7 bis v0.3.0

[Schemata](https://github.com/nostrability/schemata), die JSON-Schema-Definitionen zur Validierung von Nostr-Event-Kinds, lieferte vier Releases von [v0.2.7](https://github.com/nostrability/schemata/releases/tag/v0.2.7) bis [v0.3.0](https://github.com/nostrability/schemata/releases/tag/v0.3.0) mit 21 gemergten PRs. Der Release v0.3.0 bringt Pattern-Consistency-Fixes über Relay-URLs, Hex-IDs, MIME-Typen und BOLT-11-Strings hinweg ([PR #126](https://github.com/nostrability/schemata/pull/126)), zentralisierte Relay-URL-Patterns ([PR #117](https://github.com/nostrability/schemata/pull/117)), [NIP-19](/de/topics/nip-19/) Bech32-Basistyp-Schemas ([PR #118](https://github.com/nostrability/schemata/pull/118)) und Validierung für Kind-777-Spell-Events ([PR #125](https://github.com/nostrability/schemata/pull/125)). Die Release-Pipeline veröffentlicht nun bei jedem Release eine Kind-`1`-Notiz auf Nostr ([PR #120](https://github.com/nostrability/schemata/pull/120)), sodass das Projekt sich selbst über das Protokoll ankündigt, das es validiert. Schemata unterstützt nun ein Dutzend Sprachen jenseits des kanonischen JS/TS-Pakets: Rust, Go, Python, Kotlin, Java, Swift, Dart, PHP, C#/.NET, C++, Ruby und C.

Neben Schemata veröffentlichte das Team [schemata-codegen](https://github.com/nostrability/schemata-codegen), einen experimentellen Codegenerator, der ein anderes Vorgehen für dasselbe Validierungsproblem verfolgt. Während Schematas Validator-Pakete eine JSON-Schema-Runtime-Abhängigkeit benötigen, portiert schemata-codegen Schemas direkt in typisierte native Sprachkonstrukte (typisierte Tag-Tupel, Kind-Interfaces und Runtime-Validatoren) und entfernt die Notwendigkeit einer Validator-Bibliothek zur Laufzeit. Der [Vergleich codegen-vs-validators](https://github.com/nostrability/schemata-codegen/blob/main/CODEGEN-VS-VALIDATORS.md) dokumentiert, wann welcher Ansatz passt.

### BigBrotr v6.5.0 bis v6.5.4

[BigBrotr](https://github.com/BigBrotr/bigbrotr), die Relay-Analyseplattform, lieferte fünf Releases von [v6.5.0](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.5.0) bis [v6.5.4](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.5.4). Der Release v6.5.0 zentralisiert Relay-URL-Validierung mit einer `parse_relay_url()`-Factory-Funktion und fügt URL-Längenprüfung und Pfad-Sanitization hinzu. Die Monitoring-Infrastruktur erhielt ebenfalls Fixes: Announcement-Events enthalten nun Geohash-Location-Tags (in Anlehnung an [NIP-52](/de/topics/nip-52/)), und Timeout-Schutz wurde zu den Geo/Net-[NIP-66](/de/topics/nip-66/) Metadaten-Tests hinzugefügt, die zuvor keine Deadline hatten und unbegrenzt hängen konnten. [PR #410](https://github.com/BigBrotr/bigbrotr/pull/410) aktualisiert PostgreSQL von 16 auf 18, was das Async-I/O-Subsystem und verbesserten WAL-Durchsatz zur Relay-Analyse-Pipeline bringt.

### Vertex-Lab-Relay fügt NIP-50-Profilsuche hinzu

[Vertex Lab](https://vertexlab.io), das Team hinter [npub.world](https://github.com/vertex-lab/npub.world) und der [Vertex](https://vertexlab.io/docs) Web-of-Trust-Engine, kündigte an, dass `wss://relay.vertexlab.io` nun [NIP-50](/de/topics/nip-50/) (Search) für Profilabfragen unterstützt. NIP-50 erweitert den Standard-Nostr-`REQ`-Filter um ein `search`-Feld und erlaubt Clients, Volltextsuchanfragen an Relays zu senden, die Indizierung unterstützen. Das Hinzufügen von Profilsuche zu einem Relay, das bereits Web-of-Trust-Daten ausliefert, bedeutet, dass Clients, die mit `relay.vertexlab.io` verbunden sind, Nutzer per Name oder Beschreibung finden können, ohne einen separaten Suchdienst zu benötigen.

### Hashtree v0.2.17 und v0.2.18 liefern WebRTC-Mesh und Iris Desktop

[Hashtree](https://github.com/mmalmi/hashtree), mmalmis content-addressiertes Blob-Speichersystem, das Merkle-Wurzeln auf Nostr veröffentlicht, lieferte [v0.2.17](https://github.com/mmalmi/hashtree/releases/tag/v0.2.17) und [v0.2.18](https://github.com/mmalmi/hashtree/releases/tag/v0.2.18) am 31. März. Die beiden Releases krönen einen 30-Commit-Sprint, der drei unterschiedliche Fähigkeiten hinzufügt. Erstens fügt das `hashtree-webrtc`-Crate (in v0.2.18 in `hashtree-network` umbenannt) WebRTC-basierten Peer-to-Peer-Blob-Transport mit einheitlicher Mesh-Signalisierung über Rust-CLI, Simulation-Harness und TypeScript-Client hinweg hinzu. Zweitens baut die Release-Pipeline nun Windows-Artefakte (CLI-Zip und Iris-Installer) und bringt plattformübergreifende Abdeckung für macOS, Linux und Windows. Drittens bündeln beide Releases Iris Desktop 0.1.0, mmalmis Nostr-Social-Client, als AppImage-, .deb- und Windows-Installer-Assets neben der Hashtree-CLI. [Hashtree wurde erstmals in Newsletter #10 behandelt](/de/newsletters/2026-02-18-newsletter/), als es als filesystem-basierter [Blossom](/de/topics/blossom/)-kompatibler Store startete. Die WebRTC-Schicht ist der erste Schritt zu Peer-to-Peer-Content-Distribution ohne Abhängigkeit von zentralisierten Blossom-Servern.

### Nostr Mail Client v0.7.0 bis v0.7.2

[Nostr Mail Client](https://github.com/nogringo/nostr-mail-client), der Flutter-Mail-Client auf Basis von Nostr-Identitäten, lieferte [v0.7.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.0), [v0.7.1](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.1) und [v0.7.2](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.2) in drei Tagen. Die sichtbare Produktarbeit konzentrierte sich auf Onboarding ([PR #9](https://github.com/nogringo/nostr-mail-client/pull/9)) und Profilbearbeitung ([PR #10](https://github.com/nogringo/nostr-mail-client/pull/10)), beides grundlegende Teile für jeden Client, der Nostr als Postfach präsentieren will. Die späteren Punkt-Releases paketierten diese Arbeit in neue Android- und Linux-Builds.

### Wisp v0.14.0 bis v0.16.1

[Wisp](https://github.com/barrydeen/wisp), der Android-Nostr-Client, lieferte 13 weitere Releases von [v0.14.0-beta](https://github.com/barrydeen/wisp/releases/tag/v0.14.0-beta) bis [v0.16.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.3-beta). Die Arbeit diese Woche umfasst NIP-17-Rumor-JSON-Fixes ([PR #385](https://github.com/barrydeen/wisp/pull/385)), Repost-Badges auf Galerie-Karten ([PR #383](https://github.com/barrydeen/wisp/pull/383)), ausklappbare Reaktionsdetails ([PR #382](https://github.com/barrydeen/wisp/pull/382)), persistente Emoji-Sets ([PR #381](https://github.com/barrydeen/wisp/pull/381)) und Video-Autoplay-Kontrollen ([PR #380](https://github.com/barrydeen/wisp/pull/380)). Das neueste [v0.16.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.3-beta) behebt außerdem benutzerdefinierte Emoji-Shortcodes mit Bindestrichen und fehlende Emoji-Tags.

### Primal Android 3.0.17

[Primal Android](https://github.com/PrimalHQ/primal-android-app) lieferte [3.0.17](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.17) am 24. März. [PR #1000](https://github.com/PrimalHQ/primal-android-app/pull/1000) ordnet WalletException-Typen Fehlercodes in NWC-Antworten zu und gibt [NIP-47](/de/topics/nip-47/) Clients strukturierte Fehlerinformationen statt generischer Fehler. [PR #995](https://github.com/PrimalHQ/primal-android-app/pull/995) behebt, dass Poll-Zap-Stimmen als Top Zaps erscheinen, und [PR #998](https://github.com/PrimalHQ/primal-android-app/pull/998) blendet Wallet-Guthaben und Aktionsbuttons aus, wenn keine Wallet konfiguriert ist.

### OpenChat v0.2.4 bis v0.3.0

[OpenChat](https://github.com/DavidGershony/openChat), der Avalonia-basierte Chat-Client auf dem [Marmot](/de/topics/marmot/)-Stack, lieferte sechs Releases von [v0.2.4](https://github.com/DavidGershony/openChat/releases/tag/v0.2.4) bis [v0.3.0](https://github.com/DavidGershony/openChat/releases/tag/v0.3.0) in vier Tagen. Das Commit-Log erzählt die Geschichte eines Clients, der die Lücken zwischen „Marmot funktioniert“ und „jemand kann das tatsächlich täglich nutzen“ schließt. [NIP-42](/de/topics/nip-42/) Relay-Authentifizierung landete, gefolgt von einer Relay-Picker-UI mit Duplicate-Event-Filtering. Voice Messages erhielten Pause, Resume, Seek und Zeitanzeige. Der Signer-Pfad wurde gehärtet: Amber-Verbindungen wurden mit einem aktualisierten [NIP-46](/de/topics/nip-46/) URI-Format behoben, der WebSocket reconnectet nun automatisch vor dem Senden von Requests, und doppelte Amber-Requests werden jetzt durch Prüfung auf replizierte Antworten abgefangen. Auf der Speicherseite erhielten Linux und macOS AES-256-GCM Secure Storage mit file-backed keys, und das Abrufen von User-Metadaten nutzt nun [NIP-65](/de/topics/nip-65/) Relay-Discovery und cached Ergebnisse in einer lokalen Datenbank.

### Igloo Signer 1.1

[Igloo](https://github.com/FROSTR-ORG/igloo-ios-prototype), der iOS-[FROST](/de/topics/frost/) Threshold-Signer des FROSTR-Projekts, lieferte [v1.1](https://github.com/FROSTR-ORG/igloo-ios-prototype/releases/tag/v1.1) am 28. März. FROST (Flexible Round-Optimized Schnorr Threshold) Signaturen erlauben einer Gruppe von Signern, gemeinsam ein Nostr-Schlüsselpaar zu kontrollieren, wobei beliebige t-von-n-Teilnehmer ein Event signieren können, ohne dass eine einzelne Partei den vollständigen privaten Schlüssel hält. Igloo ist eine der ersten mobilen Implementierungen dieses Ansatzes für Nostr.

### nak v0.19.3 und v0.19.4

[nak](https://github.com/fiatjaf/nak), fiatjafs Kommandozeilen-Nostr-Toolkit, lieferte [v0.19.3](https://github.com/fiatjaf/nak/releases/tag/v0.19.3) und [v0.19.4](https://github.com/fiatjaf/nak/releases/tag/v0.19.4) am 26. und 30. März. Beide Releases beheben Panic-Zustände: [PR #118](https://github.com/fiatjaf/nak/pull/118) ersetzt `strings.Split` durch `strings.Cut`, um einen potenziellen Out-of-Bounds-Zugriff zu verhindern, und [PR #119](https://github.com/fiatjaf/nak/pull/119) verhindert dieselbe Klasse von Panic bei der Curl-Flag-Parsing-Logik.

### Flora v0.3.0

[Flora](https://github.com/shawnyeager/flora-extension), eine Chrome-Erweiterung für dezentrale Bildschirmaufnahme und -teilung auf Nostr, lieferte [v0.3.0](https://github.com/shawnyeager/flora-extension/releases/tag/v0.3.0). Der Release fügt private verschlüsselte Video-Freigabe mit öffentlichen, ungelisteten und privaten Modi hinzu. Private Aufnahmen werden mit AES-256-GCM verschlüsselt und via [NIP-17](/de/topics/nip-17/) (Private Direct Messages) an Empfänger ausgeliefert, sodass die Aufnahme niemals im Klartext einen Server berührt.

### YakiHonne Mobile 2.0.3

[YakiHonne](https://github.com/YakiHonne/mobile-app), der mobile Nostr-Client, lieferte [2.0.3](https://github.com/YakiHonne/mobile-app/releases/tag/YakiHonne-2.0.3) mit Relay-Reviews und Join-Requests, erweiterten verschachtelten Antworten, Auto-Übersetzung für Notizen und NWC-Multi-Relay-Unterstützung.

## Projekt-Updates

### Zap Cooking fügt Zap-Polls und Branta-Zahlungsverifizierung hinzu

[Zap Cooking](https://github.com/zapcooking/frontend), die Rezept- und Content-Plattform, mergte diese Woche 11 PRs mit Fokus auf interaktive Inhalte und Zahlungsflüsse. [PR #277](https://github.com/zapcooking/frontend/pull/277) fügt Zap-Polls (Kind 6969) hinzu, bei denen Nutzer durch das Senden von sats abstimmen und Wählerlisten mit Profilbildern sehen können. [PR #274](https://github.com/zapcooking/frontend/pull/274) gestaltet die Poll-UX neu, sodass die Abstimmungsoberfläche natürlicher im Feed sitzt.

[PR #276](https://github.com/zapcooking/frontend/pull/276) fügt kamera-basiertes QR-Scanning zum Send-Payment-Flow hinzu und integriert [Branta](https://branta.pro/), einen Verifizierungsdienst, der prüft, ob ein Zahlungsziel legitim ist, bevor gesendet wird. Branta prüft Zahlungsziele vor dem Senden auf Phishing, Address Swaps und Man-in-the-Middle-Abfangen. In Zap Cookings Implementierung erscheinen ein Branta-verifizierter Plattformname und ein Logo direkt im Zahlungsfluss, und Branta-fähige QR-Codes können `branta_id`- und `branta_secret`-Parameter tragen, sodass die Wallet das Ziel direkt aus dem gescannten Code verifizieren kann.

### diVine legt die Grundlage für einheitliche Suche und härtet Video-Auslieferung

[diVine](https://github.com/divinevideo/divine-mobile), der Kurzform-Video-Client, verbrachte die Woche damit, Suche, Feed-Navigation, Playback-Recovery und Upload-Verhalten zu verschärfen. [PR #2540](https://github.com/divinevideo/divine-mobile/pull/2540) legt die Grundlage für einen einheitlichen Suchbildschirm mit gruppierten Abschnitten für Videos, People und Tags. [PR #2623](https://github.com/divinevideo/divine-mobile/pull/2623) härtet Pagination über Profil-Feeds, Inbox, Benachrichtigungen, Discover-Listen, klassische Vines, Suche und die composable Grid-Feeds, indem sie auf einen gemeinsamen Pagination-Controller verschoben werden.

Auch die Video-Auslieferung erhielt mehrere konkrete Fixes. [PR #2643](https://github.com/divinevideo/divine-mobile/pull/2643) wiederholt Divine-gehostete Derivatquellen der Reihe nach und fällt auf den rohen Blob zurück, bevor ein Playback-Fehler angezeigt wird, sodass transiente Fehler an einer Quelle die Wiedergabe nicht sofort beenden. [PR #2634](https://github.com/divinevideo/divine-mobile/pull/2634) hält resumable Uploads auf dem Divine-eigenen Pfad, wenn Capability-Probing transient fehlschlägt, und reduziert dadurch defekte Uploads durch kurze Netzwerkfehler. [PR #2637](https://github.com/divinevideo/divine-mobile/pull/2637) ändert außerdem das Sensitive-Content-Gate, sodass Videos nur bei tatsächlichen Warning-Labels hart blockiert werden, nicht bloß bei vom Creator gelieferten Content-Warning-Labels.

### Shopstr fügt benutzerdefinierte Storefronts hinzu und Milk Market liefert weiter Marktplatz-Arbeit aus

[Shopstr](https://github.com/shopstr-eng/shopstr), der Nostr-basierte Marktplatz, mergte [PR #245](https://github.com/shopstr-eng/shopstr/pull/245) und fügt benutzerdefinierte Storefronts hinzu. Das gibt Verkäufern eine deutlichere Home-Oberfläche, statt jedes Listing in dieselbe generische Darstellung zu zwingen.

[Milk Market](https://github.com/shopstr-eng/milk-market), ein dedizierter Marktplatz für Milch, setzte die Arbeit mit Storefront-Optimierungen ([PR #18](https://github.com/shopstr-eng/milk-market/pull/18)), Account-Recovery ([PR #17](https://github.com/shopstr-eng/milk-market/pull/17)), Beef-Splits ([PR #15](https://github.com/shopstr-eng/milk-market/pull/15)) und MCP-Tool-Typing-Fixes ([PR #16](https://github.com/shopstr-eng/milk-market/pull/16)) fort.

### Notedeck fügt Soundeffekte hinzu und erweitert seinen Updater-Pfad in Richtung Android

[Notedeck](https://github.com/damus-io/notedeck), der Desktop-Client des Damus-Teams, mergte [PR #1412](https://github.com/damus-io/notedeck/pull/1412), die ein Soundeffekt-Subsystem mit UI-Interaktionsgeräuschen via rodio hinzufügt, und [PR #1399](https://github.com/damus-io/notedeck/pull/1399) mit Agentium-Updates einschließlich eines CLI-Title-Flags und einklappbarer Session-Ordner. Ein offener [PR #1417](https://github.com/damus-io/notedeck/pull/1417) schlägt APK-Self-Update via Nostr/Zapstore auf Android vor und baut auf [Notedecks Nostr-nativer Updater-Arbeit aus Newsletter #14](/de/newsletters/2026-03-18-newsletter/#notedeck-verlagert-release-erkennung-auf-nostr) auf.

### Nostria fügt Repost-Relay-Hints und NIP-98-Ausrichtung hinzu

[Nostria](https://github.com/nostria-app/nostria) mergte [PR #583](https://github.com/nostria-app/nostria/pull/583) und fügt [NIP-18](/de/topics/nip-18/) (Reposts) Relay-Hints zu Repost-`e`-Tags für Kind-6- und Kind-16-Events hinzu, [PR #582](https://github.com/nostria-app/nostria/pull/582) richtet Brainstorm-HTTP-Auth (Kind 27235) an den von [NIP-98](/de/topics/nip-98/) (HTTP Auth) geforderten Tags aus, und [PR #576](https://github.com/nostria-app/nostria/pull/576) fügt Schemata-Schema-Validation-Tests hinzu. Die NIP-98-Änderung bedeutet, dass Nostria sich gegenüber externen Diensten mit demselben HTTP-Auth-Format authentifizieren kann, das andere Clients verwenden.

### Nostr-Doc fügt Desktop-Paketierung und Offline-First-Arbeit hinzu

[Nostr-Doc](https://github.com/formstr-hq/nostr-docs), der kollaborative Editor von Form*, hatte eine arbeitsreiche Woche mit Paketierung und Editor-Arbeit. [Commit fcdc00a](https://github.com/formstr-hq/nostr-docs/commit/fcdc00a564c8d76f094c586b06efce07592a60e4) fügt eine Desktop-App hinzu, [Commit 3977a8e](https://github.com/formstr-hq/nostr-docs/commit/3977a8eb2e62b84a67de756c2776e14de8470927) startet Native-App-Arbeit, und [Commit 413a030](https://github.com/formstr-hq/nostr-docs/commit/413a030f5b47fb8e32a5dff81bcef557ad9b5869) drängt die App in Richtung Offline-First-Verhalten. Auf der Editor-Seite fügt [Commit 1855ce8](https://github.com/formstr-hq/nostr-docs/commit/1855ce86ee83ad504e14e47d9c339baffb114786) Ctrl+S-Speichern, Save-Warnungen, Link-Preview-Fixes und korrigiertes Strikethrough-Rendering hinzu.

### rust-nostr optimiert NIP-21-Parsing und fügt Relay-seitige NIP-62-Unterstützung hinzu

[rust-nostr](https://github.com/rust-nostr/nostr) mergte acht PRs. Der bemerkenswerteste ist [PR #1308](https://github.com/rust-nostr/nostr/pull/1308), der [NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) URI-Parsing in `PublicKey::parse` optimiert, indem es an die Performance des Standard-Bech32-Parsings angeglichen wird. Zuvor brauchten NIP-21-URIs ungefähr doppelt so lange zum Parsen wie rohe Bech32-Schlüssel. Das Projekt hat außerdem vier offene PRs, die Relay-spezifische [NIP-62](/de/topics/nip-62/) (Request to Vanish) Unterstützung über die Memory-, LMDB-, SQLite- und Datenbank-Test-Backends hinzufügen ([PR #1315](https://github.com/rust-nostr/nostr/pull/1315), [PR #1316](https://github.com/rust-nostr/nostr/pull/1316), [PR #1317](https://github.com/rust-nostr/nostr/pull/1317), [PR #1318](https://github.com/rust-nostr/nostr/pull/1318)).

### nostr-tools fügt Bunker-Relay-Kontrolle hinzu und behebt NIP-47-Multi-Relay-Parsing

[nostr-tools](https://github.com/nbd-wtf/nostr-tools) mergte [PR #530](https://github.com/nbd-wtf/nostr-tools/pull/530) und fügt `skipSwitchRelays` zu BunkerSignerParams für manuelles Relay-Management hinzu, und [PR #529](https://github.com/nbd-wtf/nostr-tools/pull/529) behebt [NIP-47](/de/topics/nip-47/) (Nostr Wallet Connect) Connection-String-Parsing, um mehrere Relays zu unterstützen, wie es die Spezifikation erlaubt.

### Nostrability integriert Sherlock-Audit-Daten und veröffentlicht Schemata-Überblick

[Nostrability](https://github.com/nostrability/nostrability), der Interoperability-Tracker für Nostr-Clients, mergte 14 PRs. [PR #306](https://github.com/nostrability/nostrability/pull/306) integriert Sherlock-Scan-Statistiken in das Dashboard. Sherlock ist Nostrabilitys automatisiertes Audit-Tool, das sich mit Nostr-Clients verbindet, die von ihnen veröffentlichten Events erfasst und jedes Event gegen die Schemata-JSON-Schema-Definitionen validiert, um Spec-Verstöße zu erkennen. Das Dashboard zeigt nun schema fail rates pro Client ([PR #315](https://github.com/nostrability/nostrability/pull/315)), sodass Entwickler sehen können, bei welchen Event-Kinds ihr Client Fehler macht. [PR #323](https://github.com/nostrability/nostrability/pull/323) überarbeitet den Nostr-Publish-Workflow, sodass Release-Ankündigungen als separater Job laufen, der nicht durch frühere CI-Schritte abgebrochen werden kann.

elsat veröffentlichte außerdem am 30. März [Schemata for nostr devs](https://njump.me/naddr1qvzqqqr4gupzq96n3hp2vfmf6z2y8uvvxl97xk86kkalnqghx4p25lzl79c76a7yqy2hwumn8ghj7un9d3shjtnyv9kh2uewd9hj7qgwwaehxw309ahx7uewd3hkctcqz4fnx4rkw3x57nrcwdn8zt22xd982jehfptsgqtrww), das beschreibt, wie schemata, schemata-codegen und Sherlock zusammenpassen, und aktuelle Abdeckungszahlen nennt: 179 Event-Kind-Schemas über 65 NIPs, 154 Tag-Schemas, 13 Protokollnachrichten und 310 Beispiel-Events.

### Nalgorithm fügt Digest-Generierung und lokales Score-Caching hinzu

[Nalgorithm](https://github.com/jooray/nalgorithm), ein neues relevance-geranktes Nostr-Feed-Projekt, startete diese Woche die öffentliche Entwicklung. [Commit cf6c501](https://github.com/jooray/nalgorithm/commit/cf6c501e754ef95a1b4fecc1a76288471a101f43) legt die initiale Web-App an, die Posts von Follows lädt und sie gegen einen nutzerdefinierten Präferenz-Prompt bewertet. [Commit 8e931b6](https://github.com/jooray/nalgorithm/commit/8e931b6ae85d470e73603752134ff49b7ba4bb86) fügt ein CLI-Digest-Tool hinzu, das Top-gerankte Posts in eine gesprochene Zusammenfassung verwandelt, während [Commit 4cb9c63](https://github.com/jooray/nalgorithm/commit/4cb9c635489a9a3429e8d71f3861dc2a11624153) file-basiertes Score-Caching und inkrementelle Learned-Prompt-Evolution aus jüngsten Likes hinzufügt. [Commit c2edfb8](https://github.com/jooray/nalgorithm/commit/c2edfb8b89fadbe0028c3f5729bda7e23b2e3c03) stoppt außerdem das Caching von Fallback-Scores aus fehlgeschlagenen Batches, sodass ein transienter Scoring-Fehler nicht dauerhaft das Ranking eines Posts abflacht.

### TENEX fügt RAG-Vector-Store und gezielten MCP-Start hinzu

[TENEX](https://github.com/tenex-chat/tenex), das Nostr-native Agent-Framework, das AI-Agenten über Telegram mit Nostr-Channels verbindet, mergte diese Woche sieben PRs. [PR #101](https://github.com/tenex-chat/tenex/pull/101) fügt eine austauschbare Vector-Store-Abstraktion mit SQLite-vec-, LanceDB- und Qdrant-Backends hinzu und gibt Agenten Retrieval-Augmented Generation, ohne auf eine einzelne Vector-Datenbank festgelegt zu sein. [PR #102](https://github.com/tenex-chat/tenex/pull/102) macht den MCP-Start gezielt: Es werden nur die MCP-Server gestartet, deren Tools ein Agent tatsächlich nutzt, statt alle Server beim ersten Lauf eager zu starten. [PR #100](https://github.com/tenex-chat/tenex/pull/100) fügt ein `send_message`-Tool hinzu, sodass Agenten mit Telegram-Channel-Bindings Nachrichten proaktiv pushen können, statt nur auf eingehende zu antworten. [PR #106](https://github.com/tenex-chat/tenex/pull/106) vermeidet einen Subprozess-Spawn, der eine 9GB-Bun/JSC-Pre-Allocation von Speicher auslöste, indem `.git/HEAD` direkt gelesen wird, statt `git branch` auszuführen.

### Dart NDK verschiebt Amber-Signer und fügt Alby Go 1-Click hinzu

[Dart NDK](https://github.com/relaystr/ndk), das Flutter Nostr Development Kit, lieferte 11 gemergte PRs. [PR #525](https://github.com/relaystr/ndk/pull/525) verschiebt Amber-Signer-Unterstützung in das ndk_flutter-Paket, und [PR #552](https://github.com/relaystr/ndk/pull/552) fügt Alby-Go-One-Click-Wallet-Verbindung zur Sample-App hinzu. [PR #502](https://github.com/relaystr/ndk/pull/502) fügt ein install.sh-Skript für die CLI hinzu, und [PR #523](https://github.com/relaystr/ndk/pull/523) entfernt die Rust-Verifier-Abhängigkeit zugunsten nativer Asset-Behandlung.

## Protokoll- und Spezifikationsarbeit

### Marmot verschiebt KeyPackages zu adressierbaren Events und verschärft Push-Benachrichtigungen

Die [Marmot-Spezifikation](https://github.com/marmot-protocol/marmot) mergte vier PRs, die ändern, wie das Protokoll Schlüsselmaterial und Gruppenmitgliedschaft handhabt. [PR #54](https://github.com/marmot-protocol/marmot/pull/54) migriert KeyPackage-Events von regulärem `kind:443` zu adressierbarem `kind:30443` mit einem `d`-Tag und eliminiert damit die Notwendigkeit von [NIP-09](/de/topics/nip-09/) Event-Löschung während der Schlüsselrotation. Addressable Events überschreiben sich an Ort und Stelle, wodurch Rotation in sich geschlossen wird. [PR #57](https://github.com/marmot-protocol/marmot/pull/57) erlaubt Nicht-Admin-Nutzern, SelfRemove-Proposals (freiwilliger Gruppenaustritt) zu committen, und [PR #62](https://github.com/marmot-protocol/marmot/pull/62) verlangt von Admins, vor der Nutzung von SelfRemove ihren Admin-Status aufzugeben, um zu verhindern, dass ein Admin verschwindet, während er noch erhöhte Rechte hält.

[PR #61](https://github.com/marmot-protocol/marmot/pull/61) verschärft das [MIP-05](/de/topics/mip-05/) Push-Benachrichtigungsformat, indem Single-Blob-Base64-Kodierung, Versionierung, Token-Wire-Format und X-only-Key-Verwendung explizit gemacht werden. Der Effekt ist eine definierte Wire-Repräsentation für Token-Blobs und X-only-Keys über Spezifikation, Client-Bibliotheken und App-Backends hinweg. Die Implementierung dieser Spec-Änderungen landete diese Woche im White-Noise-Stack und wird im [White Noise v2026.3.23-Abschnitt oben](#white-noise-behebt-relay-churn-und-erweitert-client-kontrollen) behandelt.

### NIP-Updates

Aktuelle Änderungen am [NIPs-Repository](https://github.com/nostr-protocol/nips):

**Gemergt:**

- **[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md): Static Websites** ([PR #1538](https://github.com/nostr-protocol/nips/pull/1538)): Definiert Kind `15128` (Root Site) und Kind `35128` (Named Site) Manifest-Events zum Hosting statischer Websites unter Nostr-Schlüsselpaaren mit Blossom-Speicher. Siehe den [Deep Dive unten](#nip-deep-dive-nip-5a-static-websites).

- **[NIP-30](/de/topics/nip-30/) (Custom Emoji): Bindestriche in Shortcodes erlauben** ([PR #2297](https://github.com/nostr-protocol/nips/pull/2297)): Aktualisiert die Shortcode-Beschreibung, um Bindestriche einzuschließen. Bindestrichhaltige Shortcodes werden in der Praxis seit Einführung des NIPs verwendet, daher dokumentiert die Spezifikation nun die aktuelle Nutzung.

**Offene PRs und Diskussionen:**

- **NIP-C1: Agent-TUI-Messages** ([PR #2295](https://github.com/nostr-protocol/nips/pull/2295)): Schlägt ein strukturiertes Nachrichtenformat vor, mit dem Agenten interaktive UI-Elemente über verschlüsselte DMs senden können, einschließlich typisierter `text`-, `buttons`-, `card`- und `table`-Payloads. Der Entwurf hält alles innerhalb bestehender [NIP-17](/de/topics/nip-17/) und [NIP-04](/de/topics/nip-04/) Direktnachrichten-Inhalte als JSON. Er definiert keinen neuen Event-Kind und verwendet ein einfaches Callback-String-Format für Button-Antworten.

- **NIP-95: Hybrid Peer-to-Peer Relay Protocol** ([PR #2293](https://github.com/nostr-protocol/nips/pull/2293)): Schlägt ein hybrides Relay-Modell vor, bei dem Relays autoritativ bleiben, aber auch Peer-to-Peer-Verteilung jüngerer Events über WebRTC koordinieren können. Der Entwurf führt Relay-Messages wie `PEER_REGISTER`, `PEER_REQUEST` und `PEER_OFFER` ein, mit stabilen Clients als Super Peers und dem Relay als Seed Node und Fallback.

- **NIP-B9: Zap-Poll-Events** ([PR #2284](https://github.com/nostr-protocol/nips/pull/2284)): Öffnet die alte NIP-69-Zap-Poll-Idee erneut, jetzt da [NIP-88](https://github.com/nostr-protocol/nips/blob/master/88.md) (Polls) freie Umfragen abdeckt. Der Entwurf nutzt Kind `6969` Poll-Definitionen und Kind `9734` Zaps als Stimmen und macht daraus ein bezahltes Poll-System mit ökonomischer Sybil-Resistenz. Es ergänzt freie One-Key-One-Vote-Polls.

- **NIP-AD: Super Zap** ([PR #2289](https://github.com/nostr-protocol/nips/pull/2289)): Schlägt eine Konvention vor, bei der Zaps, die an den Pubkey eines Relays oder Clients gesendet werden, als spezialisierte Werbenotizen angezeigt werden, wodurch Zap-Quittungen faktisch zu einer Anzeigenfläche werden. Relay-Betreiber und Clients würden Profile mit `lud16` veröffentlichen, diese Quittungen abrufen, eingebettete Inhalte aus Zap-Beschreibungen extrahieren und optional Minimum-sats-Schwellen setzen, um Spam zu unterdrücken.

- **NIP-XX: Agent Reputation Attestations** ([PR #2285](https://github.com/nostr-protocol/nips/pull/2285)): Schlägt Kind `30085` als parametrisierbares ersetzbares Event für strukturierte Reputations-Assertions über Nostr-Agenten vor. Der Entwurf vermeidet einen einzelnen globalen Score, indem Reputation beobachterabhängig gemacht wird, fügt zeitlichen Decay hinzu, damit alte Assertions verblassen, unterstützt negative Bewertungen mit Evidenzanforderungen und skizziert sowohl einfaches gewichtetes Scoring als auch Graph-Diversity-Scoring für bessere Sybil-Resistenz.

- **NIP-XX: Paid API Service Announcements** ([PR #2291](https://github.com/nostr-protocol/nips/pull/2291)): Schlägt Kind-`31402`-Addressable-Events zum Bewerben bezahlter HTTP-APIs vor, wobei Nostr Discovery und HTTP-402-Handhabung die Zahlung übernimmt. Der Entwurf ist tags-first, sodass Relays nach Zahlungsmethoden, Preisen und Fähigkeiten filtern können, ohne JSON-Inhalt zu parsen, und erlaubt optionale Request- und Response-Schemas, sodass Clients oder Agenten Aufrufe automatisch generieren können.

- **NIP-XX: Key Derivation from LNURL-auth via SplitSig** ([PR #2294](https://github.com/nostr-protocol/nips/pull/2294)): Schlägt vor, ein Nostr-Schlüsselpaar aus einer LNURL-auth-ECDSA-Signatur kombiniert mit einer client-seitigen zufälligen Nonce abzuleiten. Die Ableitungsformel ist `nsec = SHA256(ecdsa_signature || nonce)`. Der Server sieht die ECDSA-Signatur (inhärent im LNURL-auth-Handshake), aber niemals die Nonce, und der Browser generiert die Nonce, kontrolliert aber nicht die Signatur. Keine der beiden Komponenten allein kann den nsec ableiten. Das beabsichtigte Ergebnis ist, dass dieselbe Lightning-Wallet über Geräte hinweg denselben Nostr-Schlüssel produziert, mit der Wallet als Recovery-Anker und ohne dass ein Server den privaten Schlüssel rekonstruieren kann.

- **[NIP-55](/de/topics/nip-55/): `rejected`-Feld dokumentieren** ([PR #2290](https://github.com/nostr-protocol/nips/pull/2290)): Dokumentiert das `rejected`-Feld für intent-basierte Signer-Antworten und formalisiert damit das Verhalten, das [Amethysts v1.07.x-Fix](#amethyst-liefert-angepinnte-notizen-relay-management-und-request-to-vanish) umgehen musste.

## NIP Deep Dive: NIP-5A (Static Websites)

[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md) definiert, wie statische Websites unter Nostr-Schlüsselpaaren gehostet werden, wobei zwei Event-Kinds und bestehende Blob-Speicher-Infrastruktur genutzt werden, um signierte Events in ausgelieferte Webseiten zu verwandeln. Die [Spezifikation](https://github.com/nostr-protocol/nips/blob/master/5A.md) wurde am 25. März über [PR #1538](https://github.com/nostr-protocol/nips/pull/1538) gemergt.

Das Modell nutzt Kind `15128` für eine Root Site, eine pro Pubkey, und Kind `35128` für benannte Sites, die durch einen `d`-Tag identifiziert werden. Jedes Manifest ordnet absolute URL-Pfade SHA256-Hashes zu. Hier ist ein Root-Site-Manifest:

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["path", "/favicon.ico", "fedcba0987654321fedcba0987654321fedcba0987654321fedcba0987654321"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["description", "A static website hosted on Nostr"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

Der Serving-Flow arbeitet in drei Schritten. Ein Host-Server empfängt eine HTTP-Anfrage, extrahiert den Pubkey des Autors aus der Subdomain (entweder ein npub für Root Sites oder ein base36-kodierter Pubkey für benannte Sites), ruft die Relay-Liste des Autors über [NIP-65](/de/topics/nip-65/) ab und fragt nach dem Site-Manifest. Sobald das Manifest gefunden ist, löst der Server den angeforderten Pfad in einen Content-Hash auf, lädt den passenden Blob vom Blossom-Server oder den Blossom-Servern herunter, die in den `server`-Tags aufgelistet sind, und gibt ihn zurück.

Das DNS-Subdomain-Format ist eng spezifiziert. Root Sites verwenden den Standard-npub als Subdomain. Benannte Sites verwenden eine 50-Zeichen-Base36-Kodierung des rohen Pubkeys gefolgt vom `d`-Tag-Wert, alles in einem einzigen DNS-Label. Weil DNS-Labels auf 63 Zeichen begrenzt sind und die Base36-Kodierung immer 50 Zeichen benötigt, ist der `d`-Tag auf 13 Zeichen begrenzt. Die Spezifikation verlangt außerdem, dass `d`-Tags zu `^[a-z0-9-]{1,13}$` passen und nicht mit einem Bindestrich enden, um Mehrdeutigkeiten bei der DNS-Auflösung zu verhindern.

Die Verwendung von Content-Hashes bedeutet, dass dieselbe Site von verschiedenen Host-Servern ausgeliefert werden kann und die Datei-Integrität überprüfbar ist, ohne dem Server zu vertrauen. Ein Host-Server muss keine Dateien selbst speichern. Er lädt sie bei Bedarf von Blossom anhand der Hashes im Manifest. Das bedeutet, der Autor kontrolliert, was ausgeliefert wird, der Blossom-Server speichert die rohen Dateien, und der Host-Server verbindet nur beides. Jede dieser drei Komponenten kann unabhängig ersetzt werden.

Bestehende Implementierungen umfassen [nsite](https://github.com/lez/nsite), den Host-Server, der Manifeste auflöst und Dateien ausliefert, und [nsite-manager](https://github.com/hzrd149/nsite-manager), eine UI zum Erstellen und Veröffentlichen von Manifesten. Die Spezifikation fügte auch einen `source`-Tag zum Verlinken des Source-Code-Repositories einer Site hinzu, und das separat gemergte README-Update in [PR #2286](https://github.com/nostr-protocol/nips/pull/2286) registrierte sowohl Kind `15128` als auch `35128` im NIP-Kind-Index.

## NIP Deep Dive: NIP-62 (Request to Vanish)

[NIP-62](https://github.com/nostr-protocol/nips/blob/master/62.md) definiert Kind `62` als Anfrage an Relays, alle Events des anfragenden Pubkeys zu löschen. Die [Spezifikation](https://github.com/nostr-protocol/nips/blob/master/62.md) ist rechtlich motiviert: In Jurisdiktionen mit Right-to-be-Forgotten-Gesetzen gibt eine standardisierte, signierte Löschanfrage Relay-Betreibern ein klares Signal zum Handeln.

```json
{
  "id": "a7b8c9d0e1f23456789012345678901234567890abcdef1234567890abcdef12",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1743465600,
  "kind": 62,
  "tags": [
    ["relay", "wss://relay.example.com"]
  ],
  "content": "Requesting deletion of all events from this relay.",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

Die Spezifikation trennt gezielte und globale Vanish-Anfragen. Eine gezielte Anfrage enthält spezifische `relay`-Tags, die identifizieren, welche Relays handeln sollen. Eine globale Anfrage verwendet den Literal-String `ALL_RELAYS` als `relay`-Tag-Wert und fordert jedes Relay, das das Event sieht, auf, alle Events dieses Pubkeys zu löschen. Relays, die dem folgen, müssen außerdem sicherstellen, dass gelöschte Events nicht wieder in das Relay zurückgesendet werden können, sodass die Löschung sticky wird.

NIP-62 geht in Umfang und Absicht über [NIP-09](/de/topics/nip-09/) (Event Deletion) hinaus. NIP-09 erlaubt das Löschen einzelner Events, und Relays MAY folgen. NIP-62 fordert die Löschung von allem, und die Spezifikation sagt, dass Relays MUST folgen, wenn ihre URL getaggt ist. Sie bittet Relays außerdem, [NIP-59](/de/topics/nip-59/) (Gift Wrap) Events zu löschen, die den anfragenden Pubkey mit `p` getaggt haben, was bedeutet, dass eingehende DMs zusammen mit den eigenen Events des Nutzers aufgeräumt werden. Das Veröffentlichen einer NIP-09-Löschung gegen eine NIP-62-Vanish-Anfrage hat keinen Effekt: Sobald du vanished bist, kannst du das Verschwinden nicht rückgängig machen, indem du die Vanish-Anfrage löschst.

Diese Woche lieferte [Amethyst v1.07.0](#amethyst-liefert-angepinnte-notizen-relay-management-und-request-to-vanish) client-seitige NIP-62-Unterstützung und ermöglicht Nutzern, Vanish-Anfragen aus der App heraus zu initiieren. Auf der Relay-Seite hat [rust-nostr](https://github.com/rust-nostr/nostr) vier offene PRs, die NIP-62-Unterstützung über die Memory-, LMDB-, SQLite- und Datenbank-Test-Backends hinzufügen ([PR #1315](https://github.com/rust-nostr/nostr/pull/1315), [PR #1316](https://github.com/rust-nostr/nostr/pull/1316), [PR #1317](https://github.com/rust-nostr/nostr/pull/1317), [PR #1318](https://github.com/rust-nostr/nostr/pull/1318)). Das bringt Client- und Relay-Unterstützungsarbeit in dieselbe Woche.

Das Protokolldesign wirft eine praktische Spannung auf. Nostrs Wertversprechen umfasst Zensurresistenz, was bedeutet, dass Relays die Veröffentlichung nicht verhindern sollten. NIP-62 führt einen Fall ein, in dem ein Relay MUST die Wiederveröffentlichung eines bestimmten Pubkeys verhindern. Die beiden Eigenschaften koexistieren, weil die Anfrage selbstgerichtet ist: Du bittest um Löschung deiner eigenen Events, nicht der von jemand anderem. Die Zensurresistenz-Eigenschaft bleibt für alle intakt außer für die Person, die sich explizit dagegen entschieden hat.

---

Das war's für diese Woche. Wer etwas baut oder Neuigkeiten zu teilen hat: <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Per [NIP-17](/de/topics/nip-17/) (Private Direct Messages) DM erreichbar</a> oder auf Nostr findbar.
