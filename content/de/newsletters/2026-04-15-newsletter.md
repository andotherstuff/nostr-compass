---
title: 'Nostr Compass #18'
date: 2026-04-15
translationOf: /en/newsletters/2026-04-15-newsletter.md
translationDate: 2026-04-22
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, deinem wöchentlichen Wegweiser durch Nostr.

**Diese Woche:** [Amethyst](https://github.com/vitorpamplona/amethyst) mergt 29 PRs, darunter Desktop-Tor-Support, eine eigene C-secp256k1-Implementierung, ein vollständiges WebRTC-Calls-System für [NIP-AC](/de/topics/nip-ac/), RFC-9420-MLS-Compliance für [Marmot](/de/topics/marmot/) und Multi-Wallet-[NIP-47](/de/topics/nip-47/). [nstrfy](https://github.com/vcavallo/nstrfy-android) startet als Android-Push-App, die Firebase durch Nostr-Relays und kind `7741` ersetzt. [HAMSTR](https://github.com/LibertyFarmer/hamstr) fügt Reticulum hinzu und bringt Nostr über LoRa-Mesh ohne Internetanbindung. [Bloom](https://github.com/nostrnative/bloom) startet mit v0.1.0 als Desktop-App mit integriertem [Blossom](/de/topics/blossom/)-Server und Relay. [WaveFunc](https://github.com/zeSchlausKwab/wavefunc) debütiert als Nostr-Internetradio auf Basis von [NIP-53](/de/topics/nip-53/). [Botburrow](https://github.com/marmot-protocol/botburrow) startet als self-hosted Bot-Plattform für [Marmot](/de/topics/marmot/)-Gruppenchats. [Snort](https://github.com/v0l/snort) liefert v0.5.0 bis v0.5.3 mit Security-Audit und Performance-Überarbeitung, und [Primal Android](https://github.com/PrimalHQ/primal-android-app) gestaltet seinen Feed neu.

## Top Stories

### Amethyst mergt Desktop Tor, C secp256k1, WebRTC-Calls und Multi-Wallet NWC

[Amethyst](https://github.com/vitorpamplona/amethyst), der von vitorpamplona gepflegte Android-Client, mergte diese Woche 29 PRs zu Kryptographie, Networking, Calling und Wallet-Infrastruktur. [PR #2381](https://github.com/vitorpamplona/amethyst/pull/2381) ist die größte Änderung: Desktop-Tor-Support mit eingebettetem kmp-tor-Daemon und Fail-Closed-Design. Wenn Tor aktiviert ist, laufen alle Relay-Verbindungen über den eingebetteten Tor-Prozess. Startet Tor nicht, verbindet sich die App nicht. Damit erreicht das Privacy-Routing Parität zwischen Android- und Desktop-Builds.

[PR #2374](https://github.com/vitorpamplona/amethyst/pull/2374) fügt eine eigene C-secp256k1-Implementierung mit JNI-Bindings für die Signaturverifikation hinzu. Die Implementierung nutzt GLV-Decomposition, wNAF-Punktkodierung und hardwarebeschleunigtes SHA-256 auf x86_64 und ARM64. Das bringt laut Projekt eine zwei- bis dreifache Beschleunigung der Schnorr-Signaturprüfung gegenüber dem bisherigen reinen Kotlin-Pfad. Zusätzliche PRs in derselben Serie verbessern fused multiply-reduce, ersetzen `LongArray` durch eine dedizierte Fe4-Struktur und fügen plattformspezifische Intrinsics hinzu.

[PR #2202](https://github.com/vitorpamplona/amethyst/pull/2202) bringt die reine Kotlin-MLS-Implementierung auf RFC-9420-Compliance und ergänzt Reuse-Guard-Prüfungen, Additional Authenticated Data, Korrekturen beim Commit-Processing und Thread-Safety für die [Marmot](/de/topics/marmot/)-Integration. Eine Serie von WebRTC-PRs, [PR #2203](https://github.com/vitorpamplona/amethyst/pull/2203) bis [PR #2211](https://github.com/vitorpamplona/amethyst/pull/2211), fügt ein vollständiges Sprach- und Video-Calls-System für [NIP-AC](/de/topics/nip-ac/) hinzu, einschließlich ICE-Restart, Kamerawechsel zur Laufzeit, Netzwerküberwachung, Reconnect-Logik und Android-14+-Foreground-Service-Fixes. [PR #1988](https://github.com/vitorpamplona/amethyst/pull/1988) ergänzt außerdem Multi-Wallet-[NIP-47](/de/topics/nip-47/)-Support.

### nstrfy startet Nostr-native Push-Benachrichtigungen für Android

[nstrfy](https://github.com/vcavallo/nstrfy-android) startete am 13. April mit drei Releases von [v1.0.0](https://github.com/vcavallo/nstrfy-android/releases/tag/v1.0.0) bis [v1.2.0](https://github.com/vcavallo/nstrfy-android/releases/tag/v1.2.0). Die App ist ein Fork von ntfy-android, bei dem der HTTP-Transport durch Nostr ersetzt wurde. Statt einen Server auf Push-Nachrichten abzufragen, abonniert nstrfy kind-`7741`-Events auf konfigurierbaren Relays und zeigt sie als native Android-Benachrichtigungen an.

Das Benachrichtigungsmodell unterstützt sowohl plaintext als auch mit [NIP-44](/de/topics/nip-44/) verschlüsselte Payloads. Wenn Verschlüsselung aktiv ist, nutzt nstrfy [Amber](https://github.com/greenart7c3/Amber) für Signing via [NIP-55](/de/topics/nip-55/) oder einen lokalen nsec. Topic-basierte Subscriptions erlauben pro Topic Sender-Allowlists mit npub-Whitelisting. Die App importiert Relay-Listen aus dem Profil des Nutzers über [NIP-65](/de/topics/nip-65/) und respektiert [NIP-40](/de/topics/nip-40/) Event Expiration. Das Begleitprojekt [nstrfy.sh](https://github.com/vcavallo/nstrfy.sh) liefert eine bash-CLI und einen gehosteten Web-Client.

### HAMSTR fügt Reticulum für Nostr über LoRa-Mesh hinzu

[HAMSTR](https://github.com/LibertyFarmer/hamstr), das Nostr-Events und Lightning-zaps über Amateurfunk überträgt, mergte am 12. April [PR #10](https://github.com/LibertyFarmer/hamstr/pull/10) und fügte [Reticulum](https://reticulum.network/) als Transport-Backend hinzu. Reticulum ist ein kryptographisches Mesh-Protokoll für LoRa, HF, VHF/UHF, serielle Verbindungen und TCP/IP. Mit dieser Ergänzung kann HAMSTR Nostr-Events über ein Mesh aus RNode-Hardware vollständig ohne Internet-Infrastruktur weiterleiten.

Die bestehenden AX.25-Packet-Radio- und VARA-HF-Transports bleiben verfügbar. HAMSTRs Zero-Knowledge-Server-Architektur bedeutet, dass das Relay keine private keys sieht, und die [NIP-57](/de/topics/nip-57/)-Zap-Compliance sorgt dafür, dass Offline-Lightning-zaps in Clients wie Amethyst und Primal korrekt erscheinen. Eine Setup-Anleitung für den Reticulum-Transport ist in [RETICULUM.MD](https://github.com/LibertyFarmer/hamstr/blob/master/RETICULUM.MD) enthalten.

## Shipping This Week

### Bloom v0.1.0 liefert self-hosted Blossom-Server und Relay aus

[Bloom](https://github.com/nostrnative/bloom) veröffentlichte seinen ersten Release, [v0.1.0](https://github.com/nostrnative/bloom/releases/tag/v0.1.0), am 9. April. Bloom wird mit Tauri v2 und React 19 gebaut und bündelt einen vollständigen [Blossom](/de/topics/blossom/)-Medienserver, BUD-00 bis BUD-10, und ein Nostr-Relay in einer einzigen Desktop-Anwendung für macOS, Windows und Linux. Nutzer erhalten souveräne Dateispeicherung mit SHA-256-Content-Addressing, [NIP-94](/de/topics/nip-94/)-Dateimetadaten und `blossom://`-Auflösung, ohne eigene Server-Infrastruktur betreiben zu müssen.

### WaveFunc v0.1.0 und v0.1.1 starten Nostr-Internetradio

[WaveFunc](https://github.com/zeSchlausKwab/wavefunc) veröffentlichte [v0.1.0](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.0) und [v0.1.1](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.1) am 13. April. Der Dienst startet als auf Nostr basierendes Internetradio-Verzeichnis und Player. Die Datenstruktur nutzt eigene Event-Kinds: kind `31237` für Senderlisten, kind `30078` für Favoritenlisten, kind `1311` für Live-Chat und kind `1111` für Senderkommentare. Ein Khatru-Relay-Backend liefert SQLite-Speicherung und Bluge-Volltextsuche mit [NIP-50](/de/topics/nip-50/).

WaveFunc bringt außerdem eine [NIP-60](/de/topics/nip-60/)-Cashu-Wallet und nutzap-Support mit, migrierte von NDK zu applesauce-core und ergänzte in v0.1.1 Genre-Karussells, Lightning-Donations, Senderverwaltung für eingeloggte Nutzer und einen Zapstore-Eintrag.

### Snort liefert v0.5.0 bis v0.5.3 mit Security-Härtung und Performance-Überarbeitung

[Snort](https://github.com/v0l/snort) veröffentlichte drei Releases von [v0.5.0](https://github.com/v0l/snort/releases/tag/v0.5.0) bis [v0.5.3](https://github.com/v0l/snort/releases/tag/v0.5.3). v0.5.0 ist der größte Schritt und bringt ein umfassendes Security-Audit, echte Schnorr-Signaturprüfung, gehärteten Schutz für [NIP-46](/de/topics/nip-46/) gegen gefälschte Relay-Nachrichten, verbesserte PIN-Verschlüsselung und das Ende des Vertrauens in unbestätigte NIP-26-Delegation. Performance-Gewinne kommen durch gebündelte WASM-Verifikation, lazy-geladene Routen und einen neu geschriebenen Priority-Profile-Loader.

Die Release-Linie ergänzt außerdem die Anzeige von kind-`7000`-Payment-Required-Invoices für [NIP-90](/de/topics/nip-90/) DVMs. [PR #620](https://github.com/v0l/snort/pull/620) überarbeitet zusätzlich das Messaging-System und ersetzt eine O(n²)-Berechnung der Chat-Liste durch einen einzelnen Map-basierten Durchlauf.

### Primal Android liefert 3.0.21 und gestaltet das Feed-Layout neu

[Primal Android](https://github.com/PrimalHQ/primal-android-app) veröffentlichte [v3.0.21](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.21) mit Fixes für Poll-Zap-Stimmen, Wallet-Multi-Account-Sharing und Auto-Reconnect für Remote Signer und Wallet-Service. Danach folgten sieben gemergte PRs. [PR #1008](https://github.com/PrimalHQ/primal-android-app/pull/1008) vereinheitlicht das Main-Screen-Layout, [PR #1010](https://github.com/PrimalHQ/primal-android-app/pull/1010) führt ein neues Feed-Card-Design mit größeren Avataren ein, und [PR #1009](https://github.com/PrimalHQ/primal-android-app/pull/1009) ergänzt Video-Support und Portrait-Layout für Media-Cards.

### Nostria v3.1.19 bis v3.1.21 fügen lokale AI-Bildgenerierung hinzu

[Nostria](https://github.com/nostria-app/nostria) veröffentlichte drei Releases von [v3.1.19](https://github.com/nostria-app/nostria/releases/tag/v3.1.19) bis [v3.1.21](https://github.com/nostria-app/nostria/releases/tag/v3.1.21) mit mehr als 80 Commits. Die wichtigste Neuerung ist lokale Bildgenerierung mit Janus Pro und WebGPU-Beschleunigung, sodass Nutzer Bilder direkt auf dem Gerät ohne externe API erzeugen können. Dazu kommen Cloud-Bildgenerierung, multimodaler Chat, ONNX-Runtime-Support, eine AI-Prompt-Bibliothek und AI-Cache-Management.

### TubeStr v1.0.3 liefert Feed- und Studio-Updates aus

[TubeStr](https://github.com/Tubestr/tubestr-v2) veröffentlichte [v1.0.3](https://github.com/Tubestr/tubestr-v2/releases/tag/v1.0.3) am 13. April. Der Release verbessert Feed und Studio. [PR #3](https://github.com/Tubestr/tubestr-v2/pull/3) überarbeitet das Onboarding, [PR #2](https://github.com/Tubestr/tubestr-v2/pull/2) behebt einen Fehler beim Videoexport. Die App nutzt NDK und MDK für verschlüsselte Medienfreigabe im Familienkontext und plant [Blossom](/de/topics/blossom/) für die Medienspeicherung.

## In Development

### Botburrow beginnt die Entwicklung als Marmot-Bot-Plattform

[Botburrow](https://github.com/marmot-protocol/botburrow) ist ein neues Projekt des Marmot-Teams, gestartet am 3. April. Es ist eine self-hosted Bot-Management-Plattform, auf der jeder Bot eine eigene Nostr-Identität erhält, [Marmot](/de/topics/marmot/)-verschlüsselten Gruppen per Welcome-Nachrichten beitritt und Ende-zu-Ende-verschlüsselte Nachrichten sendet und empfängt. Das Dashboard ist mit Rails 8.1 gebaut und spricht über einen Unix-Socket mit einem einzelnen whitenoise-rs-Daemon.

### Nostr Archives fügt Trending-Feeds-Relay und Entity Resolution hinzu

[Nostr Archives](https://github.com/barrydeen/nostrarchives-api) entwickelte seine Rust-API und das Next.js-Frontend weiter. [PR #118](https://github.com/barrydeen/nostrarchives-api/pull/118) ergänzt Time-Range-Filterung für das Client-Leaderboard, [PR #117](https://github.com/barrydeen/nostrarchives-api/pull/117) fügt Engagement-Zähler für Reply-Events hinzu. Auf der Frontend-Seite löst [PR #85](https://github.com/barrydeen/nostrarchives-frontend/pull/85) Nostr-Entities direkt aus URL-Pfaden auf, und [PR #86](https://github.com/barrydeen/nostrarchives-frontend/pull/86) fügt eine API-Dokumentationsseite hinzu.

### Damus behebt die Favorites-Timeline

[Damus](https://github.com/damus-io/damus) mergte [PR #3708](https://github.com/damus-io/damus/pull/3708), das `subscribe_to_favorites()` mit In-Place-Filtering, neuer Deduplizierung und persistierter Tab-Auswahl neu schreibt.

### Nostur fügt private zaps und benutzerdefinierte Emoji-Anzeige hinzu

[Nostur](https://github.com/nostur-com/nostur-ios-public) pushte zehn Commits und ergänzte private zaps, Anzeige benutzerdefinierter Emoji, einen Fix für animiertes `.webp`-Rendering und Erkennung des Audioformats für Sprachmemos.

### Amber liefert v6.0.1 bis v6.0.3 mit WebDAV-Backups und Relay-Reconnect-Fixes

[Amber](https://github.com/greenart7c3/Amber), die Android-[NIP-55](/de/topics/nip-55/)-Signer-App, veröffentlichte drei Releases. [v6.0.1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.1) fügt WebDAV- und Google-Drive-Backups hinzu, implementiert Exponential Backoff für Relay-Reconnects und aktualisiert Quartz. [v6.0.2](https://github.com/greenart7c3/Amber/releases/tag/v6.0.2) ergänzt eine Account-Index-Option bei Seed-Wörtern, und [v6.0.3](https://github.com/greenart7c3/Amber/releases/tag/v6.0.3) behebt leere Request-IDs beim Empfangen von Intents.

### Plektos v0.6.0 gestaltet mit Ditto-Themes neu

[Plektos](https://github.com/derekross/plektos), die auf [NIP-52](/de/topics/nip-52/) basierende Meetup- und Event-Plattform, veröffentlichte [v0.6.0](https://github.com/derekross/plektos/commit/7a691cdf089ceb7a8582dd5c0ee026830f2cdc77) und [v0.6.1](https://github.com/derekross/plektos/commit/3a6474ae380522d8ee1b3526423fcfc3328fd879). Das Update bringt Ditto-artige Community-Themes, konfigurierbare Avatar-Formen und eine UI-Überarbeitung.

### Shadow fügt Nostr OS API und Cashu-Wallet-App hinzu

[Shadow](https://github.com/justinmoon/shadow) pushte in zwei Tagen über 30 Commits. [Commit 88cbda5](https://github.com/justinmoon/shadow/commit/88cbda5131814d2730a2d892029932136db005df) fügt eine Cashu-Wallet-App innerhalb der Shadow-Runtime hinzu, [Commit 865c415](https://github.com/justinmoon/shadow/commit/865c415) ergänzt einen Podcast-Player-Demo. Die Runtime exponiert `Shadow.os.nostr` und `Shadow.os.audio` als erstklassige OS-APIs.

### Lief behebt Amber-Login und fügt Zapstore hinzu

[Lief](https://gitlab.com/chad.curtis/lief) veröffentlichte Build `v2026.04.12` und behebt ein [Amber](https://github.com/greenart7c3/Amber)-Signer-Login-Problem auf Android, vereinfacht den Signer-Nudge-Flow, aktualisiert nostrify und ergänzt Zapstore-Integration.

### Espy überarbeitet den Color Picker und behebt Amber-Login

[Espy](https://gitlab.com/chad.curtis/espy) veröffentlichte ebenfalls Build `v2026.04.12`. Das Update überarbeitet den Color Picker, ersetzt den Grayscale-Toggle durch einen gekrümmten Sättigungsbogen, behebt Flicker-Bugs im Hue-Ring und fügt Easter-Egg-Charaktere hinzu. Außerdem kommt derselbe Amber-Login-Fix wie in Lief.

### Jumble fügt Kind-Filter pro Feed und einen Artikel-Tab hinzu

[Jumble](https://github.com/CodyTseng/jumble) pushte 13 Commits und ergänzte Kind-Filter pro Feed, einen Articles-Tab, Sync des Notification-Read-Status mit einer privacy-preserving Option, einen Avatar-Hide-Modus und einen Fix für einen Race-Condition beim Account-Wechsel.

### Primal Web liefert acht Versionssprünge

[Primal Web](https://github.com/PrimalHQ/primal-web-app) veröffentlichte in einer Woche die Versionen 3.0.93 bis 3.0.101 mit 21 Commits. Die Arbeit konzentrierte sich auf Verbesserungen im Livestream-Chat, Mention-Boundary-Fixes, Bookmark-Pagination, Verhinderung doppelter Likes und Relay-Proxy-Fixes.

## Protocol and Spec Work

### NIP Updates

Aktuelle Änderungen im [NIPs repository](https://github.com/nostr-protocol/nips):

**Merged:**

- **[NIP-34](/de/topics/nip-34/) (Git Stuff): Add `nostr://` clone URLs** ([PR #2312](https://github.com/nostr-protocol/nips/pull/2312)): Der PR fügt ein `nostr://`-Clone-URL-Format für Git-over-Nostr-Repositories hinzu. Definiert werden direkte `naddr`-Referenzen sowie menschenlesbare Formen über `npub` oder [NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md). Die Änderung ist bereits in Shakespeare, ngit, GitWorkshop.dev und NostrHub.io sichtbar und verschärft zugleich das `d`-Tag-Format für Repository-Identifiers.

**Open PRs and Discussions:**

- **NIP-63a: Minimal Payment Gateway Descriptor** ([PR #2315](https://github.com/nostr-protocol/nips/pull/2315)): Schlägt ein neues replaceable kind-`10164`-Event vor, mit dem Content-Creator Payment Gateways, Preisstufen und Subscription-Regeln für bezahlte Inhalte deklarieren können.
- **NIP-XX: Relay Self-Declaration Manifest and Retention Horizon** ([PR #2314](https://github.com/nostr-protocol/nips/pull/2314)): Schlägt kind `10100` für gossippbare Relay-Selbsterklärungen sowie eine neue Relay-zu-Client-Nachricht `HORIZON` vor, die dem Client vor `EOSE` mitteilt, ab welchem Timestamp das Relay überhaupt Daten hält.
- **NIP-TPLD: Transient Private Location Data** ([PR #2309](https://github.com/nostr-protocol/nips/pull/2309)): Schlägt kind `20411` für verschlüsselte Geolokationsdaten an ausgewählte Empfänger vor, mit `ttl`-Tag und per Empfänger verschlüsselten [NIP-44](/de/topics/nip-44/)-Payloads.
- **[NIP-5C](/de/topics/nip-5c/) (Scrolls): WASM programs update** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): Führt die Spezifikation für WebAssembly-Programme auf Nostr weiter aus und verfeinert Event-Format und Runtime-Interface für Scrolls.
- **[NIP-44](/de/topics/nip-44/) large payload support** ([PR #1907](https://github.com/nostr-protocol/nips/pull/1907)): Schlägt abwärtskompatible Unterstützung für Payloads vor, die größer als 65.535 Byte sind, vor allem relevant für große [NIP-46](/de/topics/nip-46/)-Antworten wie umfangreiche Contact Lists.
- **[NIP-C7](/de/topics/nip-c7/): Restrict kind 9 to chat views** ([PR #2310](https://github.com/nostr-protocol/nips/pull/2310)): Präzisiert, dass Clients in Chat-Ansichten nur kind-`9`-Events abrufen sollen, damit Chat-Nachrichten nicht ohne Kontext in allgemeine Feeds geraten.

## NIP Deep Dive: NIP-29 (Relay-based Groups)

[NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md) definiert ein Modell für Gruppenkommunikation, bei dem das Relay selbst Mitgliedschaft und Moderation verwaltet. Gruppen leben auf einem bestimmten Relay und das Relay setzt durch, wer schreiben darf. Das ist eine andere Architektur als [Marmot](/de/topics/marmot/) oder [NIP-17](/de/topics/nip-17/) Gruppenchats: Bei NIP-29 ist das Relay die Autorität, kann die Nachrichten lesen und moderiert auf Relay-Ebene.

Eine Gruppe wird durch `<host>'<group-id>` identifiziert, etwa `groups.nostr.com'abcdef`. Nutzer-Events tragen ein `h`-Tag mit der Gruppen-ID, und das optionale `previous`-Tag wirkt als Mechanismus zur Tamper-Erkennung. Clients fügen die ersten acht Hex-Zeichen kürzlich gesehener Events bei, und Relays lehnen Events ab, deren `previous`-Referenzen sie nicht in ihrer Datenbank finden. Das ist keine vollständige Chain of Custody, macht aber Kontextverluste und Replay in Relay-Forks erkennbar.

Mitgliedschaft wird über eine Reihe von Moderations-Events im Bereich `9000-9020` verwaltet. Ein Nutzer tritt über kind `9021` bei, das Relay akzeptiert oder verweigert die Anfrage nach eigener Policy. Admins können Nutzer mit Rollen hinzufügen, entfernen, Gruppenmetadaten ändern und Events löschen. Die Gruppe veröffentlicht ihren Zustand als addressable Events, etwa kind `39000` für Metadaten und kind `39003` für Rollen und Fähigkeiten. Der entscheidende Tradeoff bleibt: NIP-29 ist einfach und praktisch für öffentliche Communities, aber das Relay ist ein Vertrauensanker und kein neutraler Transport.

## NIP Deep Dive: NIP-90 (Data Vending Machines)

[NIP-90](https://github.com/nostr-protocol/nips/blob/master/90.md) definiert ein Protokoll für On-Demand-Compute über Nostr. Ein Kunde veröffentlicht einen Job-Request, Service-Provider konkurrieren um die Ausführung, und Resultate kommen als Nostr-Events zurück. Die Spezifikation reserviert kinds `5000-5999` für Requests, `6000-6999` für Resultate und kind `7000` für Feedback. Ein Result- kind ist immer genau `1000` höher als der passende Request-kind.

Requests nutzen `i`-Tags für Input, `output` für das erwartete Format, `bid` für eine Preisobergrenze und `param` für job-spezifische Parameter. Resultate referenzieren den Original-Request, nennen den pubkey des Kunden und können über das `amount`-Tag eine Lightning-Rechnung mitliefern. Feedback-Events mit kind `7000` erlauben Statusmeldungen wie `payment-required`, `processing`, `error` oder `success`, bevor das Endergebnis vorliegt.

Wichtig ist, dass NIP-90 auch Job Chaining erlaubt. Ein nachgelagerter Job kann den Output eines früheren Jobs über einen `i`-Tag vom Typ `job` referenzieren. Damit entstehen Pipeline-artige Abläufe, etwa Audio transkribieren, den Text zusammenfassen und das Ergebnis übersetzen. Für Privacy können `i`- und `param`-Daten verschlüsselt in `content` verschoben werden, was Relay-Beobachtern die Eingaben verbirgt, aber die Auswahl eines bestimmten Providers voraussetzt.

---

Das war's für diese Woche. Wenn du etwas baust oder Neuigkeiten teilen willst, schreib uns auf Nostr oder schau bei [nostrcompass.org](https://nostrcompass.org) vorbei.
