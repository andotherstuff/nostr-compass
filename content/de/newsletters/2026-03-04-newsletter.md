---
title: 'Nostr Compass #12'
date: 2026-03-04
translationOf: /en/newsletters/2026-03-04-newsletter.md
translationDate: 2026-03-04
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, deinem wöchentlichen Wegweiser durch Nostr.

**Diese Woche:** Das [Marmot Development Kit](https://github.com/marmot-protocol/mdk) liefert seinen [ersten öffentlichen Release](#marmot-development-kit-liefert-ersten-öffentlichen-release) mit verschlüsselten Medien und Multi-Language-Bindings. [Nostrability](https://github.com/nostrability/outbox) veröffentlicht [Outbox-Modell-Benchmarks](#outbox-modell-unter-der-lupe) über 14 Relay-Auswahl-Algorithmen. [Wisp](https://github.com/barrydeen/wisp) geht in acht Tagen [von der ersten Alpha zur Beta](#wisp-von-alpha-zu-beta) mit Tor und [NIP-55](/de/topics/nip-55/) (Android Signer Application) Signing. [NIP-91](#nip-updates) (AND-Filter) wird gemergt. [Vector v0.3.1](#vector-v031) liefert negentropy-Sync mit 15-facher Leistungssteigerung. Diese Ausgabe enthält außerdem den Rückblick Fünf Jahre Nostr im Februar, der das Protokoll von einer Spec-Neufassung für drei Relays über die Damus-App-Store-Explosion bis zu Mesh-Networking und KI-Agenten-Vorschlägen nachzeichnet.

## Neuigkeiten

### Outbox-Modell unter der Lupe

[Nostrability](https://github.com/nostrability/outbox) veröffentlichte eine Reihe von Outbox-Modell-Benchmarks, die testen, wie gut verschiedene Relay-Auswahl-Algorithmen Events aus dem dezentralen Relay-Netzwerk abrufen. Das Projekt mergte 16 PRs und 76 Commits in zehn Tagen und produzierte die möglicherweise gründlichste empirische Analyse von [NIP-65](/de/topics/nip-65/) (Relay List Metadata) Implementierungsstrategien bisher.

Die Benchmarks testen 14 Relay-Auswahl-Algorithmen gegen reale Follow-Listen über 15 Clients und Bibliotheken in fünf Sprachen. Ein Baseline-Ansatz, der nur populäre Relays abfragt, ruft etwa 26 % der Events ab. Greedy Set-Cover mit Thompson Sampling erreicht 80-90 % Recall. Das Hinzufügen einer latenzbewussten Variante mit hyperbolischer Diskontierung und EWMA-Relay-Latenz-Tracking steigerte die Vollständigkeit von 62-80 % auf 72-96 % bei der 2-Sekunden-Marke über sechs Testprofile.

[NIP-66](/de/topics/nip-66/) (Relay Monitoring) Dead-Relay-Filterung erwies sich als folgenreich. Die Vorfilterung von Relay-Kandidaten gegen [nostr.watch](https://nostr.watch)-Liveness-Daten entfernte 40-64 % der toten Relays und verdoppelte die Relay-Erfolgsraten von 30 % auf 75-85 %. Feed-Ladezeiten sanken um 39 % (von 40 auf 24 Sekunden über 10 Profile). Eine EOSE-Race-Simulation ergab, dass das Warten auf EOSE plus eine 200-ms-Toleranzperiode die Vollständigkeit gegenüber dem Stoppen beim ersten fertigen Relay verbesserte.

Für Clients, die ihr Relay-Routing nicht vollständig umschreiben können, fügt ein „Hybrid-Outbox-Enrichment"-Ansatz pro Autor Outbox-Abfragen auf bestehende fest codierte App-Relays hinzu. Dieser Hybrid erreichte 80 % Ein-Jahres-Event-Recall gegenüber der 26 %-Baseline und bietet einen Migrationspfad für Clients mit Legacy-Relay-Architekturen.

### ContextVM öffnet MCP-NIP und liefert ephemere Gift Wraps

[ContextVM](https://contextvm.org), das Protokoll, das Nostr mit dem [Model Context Protocol](https://modelcontextprotocol.io/) verbindet, eröffnete diese Woche zwei Vorschläge im [NIPs-Repository](https://github.com/nostr-protocol/nips). [PR #2246](https://github.com/nostr-protocol/nips/pull/2246) formalisiert CVM als Konvention für den Transport von MCP-JSON-RPC-Nachrichten über Nostr mittels ephemerer kind-25910-Events. [PR #2245](https://github.com/nostr-protocol/nips/pull/2245) erweitert [NIP-59](/de/topics/nip-59/) (Gift Wrap) um eine ephemere Variante (kind 21059), die [NIP-01](/de/topics/nip-01/) (Basic Protocol Flow) ephemere Semantik folgt und Relays erlaubt, gewrappte Nachrichten nach der Zustellung zu verwerfen.

Die ephemere Gift-Wrap-Konvention wurde als [CEP-19](https://docs.contextvm.org/spec/ceps/cep-19/) in der ContextVM SDK v0.6.x Release-Familie veröffentlicht. Die [SDK-Implementierung](https://github.com/ContextVM/sdk) fügt ein `GiftWrapMode`-Enum mit drei Einstellungen hinzu: OPTIONAL (beide Kinds akzeptieren und Peer-Fähigkeit automatisch erkennen), EPHEMERAL (nur kind 21059) und PERSISTENT (nur kind 1059). Für KI-Tool-Aufrufe vermeidet der ephemere Modus die Speicherung von Zwischen-Request-Response-Traffic auf Relays und reduziert sowohl Speicherkosten als auch Datenschutz-Exposition.

Neue öffentliche MCP-Server erschienen im Netzwerk von unabhängigen Betreibern, darunter ein Wolfram-Alpha-Abfrageserver. Das ContextVM-Team veröffentlichte CEP-15 (Common-Tools-Schema) und CEP-17 (Server-Relay-Liste-Publikation) neben dem v0.6.x Release-Zyklus.

### Marmot Development Kit liefert ersten öffentlichen Release

[MDK](https://github.com/marmot-protocol/mdk) (Marmot Development Kit), die Rust-Bibliothek hinter [Marmot](/de/topics/mls/)-verschlüsseltem Messaging in [Pika](https://github.com/sledtools/pika) und [White Noise](https://github.com/marmot-protocol/whitenoise), lieferte [v0.6.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.6.0) als ersten öffentlichen Release. Über 200 PRs wurden in diese Version gemergt, mit sechs neuen Mitwirkenden.

Der Release umfasst verschlüsselte Medienunterstützung (MIP-04) mit HKDF-Seed-Ableitung (MIP-01 v2), deterministische Commit-Race-Resolution (MIP-03), verschlüsselten lokalen Speicher, Admin-Autorisierungsvalidierung für Marmot-Commits und -Proposals sowie GREASE-Unterstützung für Protokollerweiterbarkeit. Bindings werden für Kotlin, Python, Ruby und Windows bereitgestellt, zusammen mit Android-Cross-Compilation. Die Bibliothek aktualisiert auf OpenMLS 0.8.0 mit Security-Advisory-Fixes und einem `Secret<T>`-Typ, der sensible Werte im Speicher nullt.

Eine begleitende Protokolländerung ([MIP-03](https://github.com/marmot-protocol/marmot/pull/48)) ersetzte [NIP-44](/de/topics/nip-44/) (Encrypted Payloads) Verschlüsselung durch ChaCha20-Poly1305 für kind-445-Nachrichten. NIP-44 erforderte laut Spezifikation UTF-8-String-Eingabe, was es unmöglich machte, rohe Marmot-Nachrichtenbytes durch Standard-TypeScript-Nostr-Bibliotheken zu leiten. Der Ersatz leitet Schlüssel direkt vom Marmot-Exporter-Secret ab. Diese Breaking Change erforderte koordinierte Updates über die [Core-Spezifikation](https://github.com/marmot-protocol/marmot/pull/48), [MDK](https://github.com/marmot-protocol/mdk/pull/208) und das [TypeScript SDK](https://github.com/marmot-protocol/marmot-ts/pull/54).

[marmot-ts](https://github.com/marmot-protocol/marmot-ts), die TypeScript-Implementierung gepflegt von hzrd149, mergte vier PRs mit eigenen Breaking-API-Änderungen. Ein [Omnibus-Update](https://github.com/marmot-protocol/marmot-ts/pull/52) fügte einen Key-Package-Manager für den Create/Publish/Rotate-Lebenszyklus hinzu, eine `sendChatMessage`-Convenience-Methode, Einladungsvorschau ohne Beitritt (`readInviteGroupInfo`), Self-Update für Forward-Secrecy-Rotationen und strukturiertes Debug-Logging. Gruppen-Entschlüsselungs-APIs wurden von `readGroupMessage` zu `decryptGroupMessage` umbenannt, mit reichhaltigeren Ergebnisvarianten (processed/skipped/rejected/unreadable). gzuuus steuerte Beispiel-Bereinigung mit NIP-65-Relay-Unterstützung und Last-Resort-Key-Package-Handling gemäß MIP-00 bei.

Die [White Noise CLI](https://github.com/marmot-protocol/whitenoise-rs) (`wn`), das Rust-Backend hinter der mobilen App und der neuen TUI, mergte 16 PRs in zehn Tagen. Die Signer-Lifecycle-Behandlung erhielt Abbruchsicherheit durch einen RAII-Scope-Guard ([PR #538](https://github.com/marmot-protocol/whitenoise-rs/pull/538)), der eine Klasse von Bugs behebt, bei der abgebrochene Operationen Signer-Zustand leaken konnten. Login blockiert nun, wenn erforderliche Relay-Listen (kind 10002/10050/10051) fehlen ([PR #515](https://github.com/marmot-protocol/whitenoise-rs/pull/515)), und Giftwrap-Subscriptions fallen auf [NIP-65](/de/topics/nip-65/)-Relays zurück, wenn Inbox-Listen fehlen ([PR #518](https://github.com/marmot-protocol/whitenoise-rs/pull/518)). Ein Debug-Modus ([PR #528](https://github.com/marmot-protocol/whitenoise-rs/pull/528)) zeigt Datenbankabfragen und MLS-Ratchet-Tree-Inspektion als JSON-Ausgabe. Weitere Fixes betrafen Subscription-Recovery nach Signer-Neuregistrierung, Welcome-Message-Catch-up-Timing, Relay-Filter-Validierung und Nutzersuch-Radius-Limits.

Marmot verzeichnete diese Woche eine bedeutende Expansion über den Rust-Kernstack hinaus. [White Noise TUI](https://github.com/marmot-protocol/wn-tui), eine terminalbasierte Oberfläche für den White-Noise-Messaging-Stack, startete am 3. März. Sie umhüllt die `wn`-CLI als Subprozess und rendert deren JSON-Ausgabe durch eine Elm-inspirierte unidirektionale Architektur, die Multi-Konversations-Navigation mit Ungelesen-Indikatoren, Gruppenerstellung und Mitgliedersuche, Echtzeit-Nachrichten-Streaming und Emoji-Reaktionen vom Terminal aus bietet.

[DavidGershony](https://github.com/DavidGershony) veröffentlichte einen vollständigen C#-Marmot-Stack, der die geschichtete Architektur des Rust-Toolchains spiegelt. [dotnet-mls](https://github.com/DavidGershony/dotnet-mls) implementiert kryptografische MLS-RFC-9420-Primitive in C#. [marmot-cs](https://github.com/DavidGershony/marmot-cs) baut darauf auf und fügt Nostr-Relay-Transport hinzu, als C#-Äquivalent von MDK. [OpenChat](https://github.com/DavidGershony/openChat), eine plattformübergreifende Desktop-App mit .NET 9 und Avalonia UI, verbindet beides zu einem funktionierenden Chat-Client mit NIP-44-DMs, Marmot-Gruppenverschlüsselung, [NIP-46](/de/topics/nip-46/) (Nostr Connect) Remote-Signing und Multi-Relay-Statusindikatoren.

[MDK PWA Reference](https://github.com/zerosats/mdk-pwa-reference) stellt eine Progressive-Web-App-Vorlage für den Bau von Marmot-verschlüsselten Anwendungen bereit, mit experimenteller Unterstützung für KI-Agenten-Teilnahme in Gruppenchats und Bitcoin-Zahlungen über Arkade-Wallet-Infrastruktur.

### Wisp: Von Alpha zu Beta

[Wisp](https://github.com/barrydeen/wisp) ist ein neuer Android-Nostr-Client, der vom [ersten Alpha](https://github.com/barrydeen/wisp/releases/tag/v0.1.0-alpha) am 24. Februar zu [v0.3.4-beta](https://github.com/barrydeen/wisp/releases/tag/v0.3.4-beta) am 3. März gelangte und dabei 19 Releases, 115 gemergte PRs und 276 Commits in acht Tagen produzierte.

Die Feature-Entwicklung deckt Terrain ab, für das die meisten Clients Monate brauchen. v0.1.0 startete mit Outbox/Inbox-Relay-Modell-Unterstützung und Onboarding-Flows. Ab v0.1.3 verfügte der Client über [NIP-55](/de/topics/nip-55/) Intent-basiertes Signing für Amber, einen eingebetteten Tor-SOCKS5-Proxy für `.onion`-Relay-Konnektivität und [NIP-47](/de/topics/nip-47/) (Nostr Wallet Connect). v0.2.0 stieg zur Beta auf mit Mute-List-Filterung und Custom-Emoji-Unterstützung, während v0.2.4 Content-Warning-Overlays hinzufügte. Die v0.3.x-Serie führte [NIP-13](/de/topics/nip-13/) Proof-of-Work für Notes ein, Background-PoW-Mining mit persistenten Einstellungen, `.onion`-Relay-Speicher und Mute-Thread-Benachrichtigungen.

Gerätebasierte Übersetzung über Google ML Kit läuft lokal ohne Netzwerkzugang nach dem ersten Modell-Download. Eine interaktive soziale Graphvisualisierung nutzt eine Velocity-Verlet-Physiksimulation bei ungefähr 30fps mit Pinch-to-Zoom-Navigation und Profilinspektion.

## Releases

### Vector v0.3.1

[Vector](https://github.com/VectorPrivacy/Vector), die Marmot-verschlüsselte Messaging-App, lieferte [v0.3.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.1) mit Gruppenmanagement-Verbesserungen und Performance-Arbeit. Multi-Admin-Gruppen, Masseneinladungen, Einladung per npub und Gruppenavare erweitern die Kollaborationsfunktionen. Android-Hintergrundbenachrichtigungen unterstützen nun Inline-Antwort- und Gelesen-Markieren-Aktionen.

[Negentropy](/de/topics/negentropy/)-basierter deterministischer Sync ruft den vollständigen Gesprächsverlauf ab, einschließlich Nachrichten, die während Offline-Perioden verpasst wurden. Voice-to-Text wurde mit GPU-Beschleunigung auf Android neu aufgebaut. Die Dateianhang-Behandlung wurde überarbeitet mit Download-Fortschritt, Retry-Zuständen, Verzeichnis-Zip-und-Senden und Live-Fortschrittsanzeigen durchgängig. Die Leistung verbesserte sich über 15-fach bei Boot-Zeit, Bildverarbeitung, Audio-Wiedergabe und allgemeiner UI-Reaktionsfähigkeit. Die App-Installationsgröße sank um mehr als ein Drittel, wobei das Frontend um ungefähr die Hälfte reduziert wurde. 32-bit-ARM-Android-Unterstützung wurde hinzugefügt.

### Alby Hub v1.21.5

[Alby Hub](https://github.com/getAlby/hub), der selbst-verwahrende Lightning-Node mit Nostr Wallet Connect ([NIP-47](/de/topics/nip-47/)) Unterstützung, lieferte [v1.21.5](https://github.com/getAlby/hub/releases/tag/v1.21.5). Ein zweites Relay wurde zur Standard-NWC-Konfiguration hinzugefügt, was die Zuverlässigkeit bei Relay-Neustarts verbessert. Ein Fix für ungültige Zap-Daten in der Transaktionsliste behebt ein Anzeigeproblem mit fehlerhaften [NIP-57](/de/topics/nip-57/) (Lightning Zaps) Events. Neue App-Store-Einträge umfassen Alby CLI und LNVPS.

### nospeak v0.12.x

[nospeak](https://github.com/psic4t/nospeak), der textbasierte Nostr-Messaging-Client, lieferte drei Releases im Berichtszeitraum. [v0.12.0](https://github.com/psic4t/nospeak/releases/tag/v0.12.0) fügte einen PIN-App-Lock mit 4-stelligem Tastenfeld und über 15 neue Sprachübersetzungen hinzu, darunter Bengali, Thai, Vietnamesisch, Hindi, Arabisch, Hebräisch, Urdu, Türkisch, Japanisch, Chinesisch, Koreanisch, Niederländisch, Polnisch, Russisch und Persisch mit RTL-Unterstützung. [v0.12.1](https://github.com/psic4t/nospeak/releases/tag/v0.12.1) führte ein Cypher-Theme mit reinem Schwarz und Cyan-Akzenten ein, dazu Android-Video-Poster-Generierung. [v0.12.2](https://github.com/psic4t/nospeak/releases/tag/v0.12.2) fügte Chat-Export und „Profil anzeigen" in Kontaktmenüs hinzu.

### Citrine v2.0.0-pre2

[Citrine](https://github.com/greenart7c3/Citrine), das Android-Personal-Relay von greenart7c3, lieferte [v2.0.0-pre2](https://github.com/greenart7c3/Citrine/releases/tag/v2.0.0-pre2) mit Relay-Performance-Verbesserungen durch neue Datenbankindizes und umstrukturierte Kotlin-Coroutinen. Jede gehostete Web-App startet nun auf einem eigenen Port. Volltextsuche und ein neu gestalteter Events-Bildschirm mit Event-Erweiterung runden die Änderungen ab.

### NoorNote v0.5.x

[NoorNote](https://github.com/77elements/noornote), eine Nostr-basierte Notiz-Anwendung, lieferte 8 Releases von [v0.5.0](https://github.com/77elements/noornote/releases/tag/v0.5.0) bis [v0.5.7](https://github.com/77elements/noornote/releases/tag/v0.5.7). Der v0.5.0-Launch auf Android fügte [NIP-55](/de/topics/nip-55/) Amber-Signer-Unterstützung und [NIP-71](/de/topics/nip-71/) (Video Events) Note-Publishing hinzu. Eine neu gestaltete Willkommensseite in v0.5.1 enthielt öffentliche Timeline-Vorschauen und reduzierte das APK auf 15 MB. Der Relay Browser in v0.5.2 ermöglicht das Durchsuchen öffentlicher Relay-Timelines über teilbare URLs, zusammen mit Medien-Download und [NIP-30](/de/topics/nip-30/) Custom-Emoji-Reaktionen. Nachfolgende Releases bis v0.5.7 beheben Sync-Race-Conditions im kollaborativen „Tribes"-Notiz-Sharing-System.

### NosCall v0.5.1

[NosCall](https://github.com/sanah9/noscall), die Nostr-Voice- und Video-Calling-App, lieferte [v0.5.1](https://github.com/sanah9/noscall/releases/tag/v0.5.1-release) mit Sprachnachrichten-Unterstützung, einem optimierten Desktop-Erlebnis mit Gruppeneintritt, Kontakt-Favoriten auf dem Desktop, Kontaktnotizen und Filterung, Datenexport- und Bereinigungsoptionen sowie Unterstützung für Systemschriftgrößen-Barrierefreiheit.

### Shosho v0.13.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), die Nostr-Livestreaming-App, lieferte [v0.13.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.13.0) mit MP4-Replay-Downloads aus Stream-Card-Menüs und [NIP-05](/de/topics/nip-05/) (DNS-Based Verification) für Profile. Der RTMP-Publisher migrierte zur Expo Modules API. Die Streaming-Leistung bei niedrigerer Bandbreite verbesserte sich, und Abstürze auf älteren Geräten sowie iOS-Streaming zu [Zap.Stream](https://zap.stream) wurden behoben.

### nostr-java v2.0.0

[nostr-java](https://github.com/tcheeric/nostr-java) lieferte [v2.0.0](https://github.com/tcheeric/nostr-java/releases/tag/v2.0.0) mit konfigurierbaren WebSocket-Puffergrößen, die Anwendungen die Verarbeitung größerer Nostr-Events ohne Abschneidung ermöglichen. Der Major-Version-Bump spiegelt Breaking Changes an der Verbindungs-API wider.

### Prism 1.1.0

[Prism](https://github.com/hardran3/Prism) lieferte [1.1.0](https://github.com/hardran3/Prism/releases/tag/1.1.0) mit Langform-Inhaltsunterstützung (kind-30023-Artikel) und einem Markdown-Editor zum direkten Verfassen in der App, gefolgt von einem [1.1.1](https://github.com/hardran3/Prism/releases/tag/1.1.1) Bugfix-Release.

### Angor v0.2.6

[Angor](https://github.com/block-core/angor), die Bitcoin-Crowdfunding-Plattform, lieferte [v0.2.6](https://github.com/block-core/angor/releases/tag/v0.2.6) mit Boltz-Integration und einem 1-Klick-Invest-Flow. Sowohl Invest- als auch Fund-Projekttypen funktionieren End-to-End im Testnet. Das Team gibt an, dass die UI zu etwa 70 % fertiggestellt ist.

## NIP-Updates

Aktuelle Änderungen am [NIPs-Repository](https://github.com/nostr-protocol/nips):

**Gemergt:**

- **[NIP-91: AND-Operator für Filter](https://github.com/nostr-protocol/nips/pull/1365)**: Fügt AND-Filter-Semantik für Tag-Arrays in Relay-Subscriptions hinzu. Derzeit gleicht die Angabe mehrerer Werte in einem Tag-Filter (z.B. mehrere `p`-Tags) Events ab, die einen davon enthalten. NIP-91 ermöglicht Clients, Events zu verlangen, die alle angegebenen Tag-Werte gleichzeitig erfüllen, was Bandbreite reduziert und schnellere Index-Operationen ermöglicht. Mehrere Relay-Implementierungen existieren bereits, darunter nostr-rs-relay, satellite-node, worker-relay und applesauce. Früher als NIP-119 nummeriert.

- **[NIP-30: Emoji-Set-Adresse in Tags](https://github.com/nostr-protocol/nips/pull/2247)**: Custom-Emoji-Tags in [NIP-30](/de/topics/nip-30/) können nun eine optionale Emoji-Set-Adresse enthalten. Das Klicken auf ein Emoji in einem Client kann das zugehörige Set zum Speichern oder Durchsuchen öffnen. Entstanden aus dem [Chachi](https://github.com/purrgrammer/chachi)-Client.

- **[NIP-29: unallowpubkey und unbanpubkey hinzufügen](https://github.com/nostr-protocol/nips/pull/2111)**: Zwei neue Admin-Befehle für [NIP-29](/de/topics/nip-29/) Group Chat. `unallowpubkey` entfernt einen pubkey von der Erlaubnisliste, ohne ihn zu bannen. `unbanpubkey` hebt einen Bann auf, ohne den pubkey wieder zur Mitgliederliste hinzuzufügen. Zuvor bannte die einzige Möglichkeit, jemanden von der Erlaubnisliste zu entfernen, die Person gleichzeitig, und das Aufheben eines Banns erforderte das erneute Hinzufügen als Mitglied.

**Offene PRs und Diskussionen:**

- **[NIP-A7: Spells](https://github.com/nostr-protocol/nips/pull/2244)** (eröffnet 27. Feb): Vorgeschlagen von purrgrammer, sind Spells portable gespeicherte Nostr-Abfragen, die als kind-777-Events veröffentlicht werden. Ein Spell kodiert einen REQ- oder COUNT-Filter in strukturierten Tags (`k` für Kinds, `authors` für Pubkeys, `tag` für beliebige Tag-Filter) mit Laufzeitvariablen: `$me` löst sich zum pubkey des eingeloggten Nutzers auf, `$contacts` expandiert zur kind-3-Follow-Liste des Nutzers. Relative Zeitstempel (`7d`, `2w`, `1mo`) ermöglichen Spells, rollende Zeitfenster ohne fest codierte Daten zu definieren. Bereits in [nak](https://github.com/fiatjaf/nak) und [Grimoire](https://github.com/purrgrammer/grimoire) implementiert, erlauben Spells Nutzern, kuratierte Feeds zu erstellen, zu teilen und zu abonnieren, die clientübergreifend transportiert werden.

- **[NIP-59: Ephemeral Gift Wrap (kind 21059)](https://github.com/nostr-protocol/nips/pull/2245)** (eröffnet 27. Feb): Fügt eine ephemere Variante von [NIP-59](/de/topics/nip-59/) Gift Wraps hinzu. Kind 21059 folgt NIP-01-ephemerer Semantik, sodass Relays Events nach der Zustellung verwerfen. Vorgeschlagen von ContextVM für MCP-Transport, wo Nachrichtenpersistenz unnötig ist.

- **[ContextVM: MCP JSON-RPC über Nostr](https://github.com/nostr-protocol/nips/pull/2246)** (eröffnet 27. Feb): Spezifiziert den Transport von Model-Context-Protocol-Nachrichten über Nostr mittels ephemerer kind-25910-Events mit `p`- und `e`-Tags für Adressierung und Korrelation. Absichtlich schlank gehalten, delegiert Protokolldetails an die [ContextVM-Spezifikation](https://docs.contextvm.org).

- **[NIP-29: Audio/Video Live Spaces](https://github.com/nostr-protocol/nips/pull/2238)** (eröffnet 25. Feb, Entwurf): fiatjafs Entwurf erweitert [NIP-29](/de/topics/nip-29/)-Gruppen um Live-Audio und -Video. Der Vorschlag fügt optionale `livekit`- und `no-text`-Tags zu Gruppenmetadaten-Events hinzu. Wenn ein Nutzer einem Voice-Space beitreten möchte, fordert der Client ein JWT vom Relay unter `/.well-known/nip29/livekit/{groupId}` an. Das Relay prüft die Gruppenmitgliedschaft und stellt ein Token mit dem Hex-Pubkey des Nutzers als `sub`-Claim aus, das an [LiveKit](https://livekit.io/) für den Medientransport übergeben wird. Voice-Room-Zugang erbt das bestehende Berechtigungsmodell der Gruppe, sodass relay-seitige Mitgliedschaftsregeln bestimmen, wer sprechen kann. Wird in Pyramid und Chachi getestet.

- **[Collaborative Event Ownership](https://github.com/nostr-protocol/nips/pull/2235)** (eröffnet 24. Feb): pablof7z schlägt ein Pointer-Event (kind 39382) vor, das einen kollaborativen Raum deklariert, indem Miteigentümer-Pubkeys in `p`-Tags und ein Ziel-Event-Kind in einem `k`-Tag aufgelistet werden. Jeder aufgeführte Eigentümer kann Events dieses Kinds mit demselben `d`-Tag veröffentlichen, und Clients lösen den aktuellen Zustand auf, indem sie alle Eigentümer abfragen und das neueste Event nehmen. Koautoren-Attribution wird nur angezeigt, wenn ein verifizierbares `a`-Tag auf den Pointer zurückverweist und der Autor in dessen `p`-Tags erscheint, was gefälschte Ansprüche verhindert. Dies ermöglicht geteilte Wiki-Seiten und gemeinsam verfasste Ressourcen, ohne die Kontrolle einem einzelnen Schlüsselpaar zuzuweisen.

- **[NIP-09: Kaskadenlöschung von Reposts](https://github.com/nostr-protocol/nips/pull/2234)** (eröffnet 24. Feb): Wenn ein Originalautor eine Notiz löscht, sollten Relays auch alle kind-6- oder kind-16-Reposts löschen, die darauf verweisen. Motiviert durch Datenschutzbedenken: Reposts können versehentlich preisgegebene Informationen erhalten, nachdem der Autor die Quelle gelöscht hat. Die Änderung betrifft nur die Relay-Seite und erfordert keine Client-Modifikationen.

- **[NIP-07: peekPublicKey](https://github.com/nostr-protocol/nips/pull/2233)** (eröffnet 23. Feb): Fügt eine `peekPublicKey()`-Methode zu [NIP-07](/de/topics/nip-07/) Browser-Erweiterungen hinzu. Anders als `getPublicKey()` gibt sie den aktuellen pubkey zurück, ohne eine Nutzerbestätigung anzufordern, und ermöglicht stummes Auto-Login, wenn der Nutzer Auto-Login aktiviert hat.

- **[NIP-BB: Book](https://github.com/nostr-protocol/nips/pull/2248)** (eröffnet 28. Feb, Entwurf): Definiert vier adressierbare Event-Kinds (30300-30303) für strukturiertes Buchpublishing auf Nostr. Ein Cover-Event enthält Wurzel-Metadaten einschließlich Titel, Coverbild, Lizenz via [NIP-32](/de/topics/nip-32/) (Labeling) Labels und Sprachcode. Ein Index-Event ordnet jedes Kapitel seiner Position zu mittels Base62-Fractional-Indexing, das Autoren erlaubt, neue Kapitel zwischen bestehende einzufügen, ohne umzunummerieren. Chapter-Events fungieren als strukturelle Überschriften mit optionalen Bildern, während Episode-Events den eigentlichen Prosatext tragen, begrenzt auf 30.000 Zeichen mit positionierten Bild-Tags. Rezensionen verwenden Zaps auf Cover-Events mit der Zap-Beschreibung als Rezensionstext.

- **[NIP-54: Wechsel von Asciidoc zu Djot](https://github.com/nostr-protocol/nips/pull/2242)** (eröffnet 26. Feb): Nach dem [d-Tag-Internationalisierungsfix](/de/newsletters/2025-12-31-newsletter/) im Dezember schlägt dieser PR vor, das [NIP-54](/de/topics/nip-54/) Wiki-Asciidoc-Markup-Format durch [Djot](https://djot.net/) zu ersetzen, und fügt einen Begründungsabschnitt und Wikilink-Beispiele für nicht-lateinische Schriften hinzu.

- **[NIP-66: Defensive Measures](https://github.com/nostr-protocol/nips/pull/2240)** (eröffnet 26. Feb): Basierend auf Erkenntnissen aus den [nostrability/outbox](#outbox-modell-unter-der-lupe)-Benchmarks, fügt explizite Hinweise für [NIP-66](/de/topics/nip-66/) Grenzfälle hinzu. Ein begleitender [PR #2241](https://github.com/nostr-protocol/nips/pull/2241) definiert Output-Tags für SSL, Geolokation, Netzwerk- und Konnektivitätsprüfungen.

- **NIP-C1: Cryptographic Identity Proofs** (Wiki-Eintrag, kind 30817): Schlägt kind-30509-Events vor, die APK-Signaturzertifikate kryptografisch mit Nostr-Profilen verknüpfen. Der Nachweis funktioniert durch Signierung einer kanonischen Nachricht, die den Nostr-Pubkey enthält, mit dem privaten Schlüssel des Zertifikats (unterstützt ECDSA, RSA PKCS1v15, Ed25519 und andere Standardalgorithmen), und anschließende Veröffentlichung der Signatur in einem kind-30509-Event, das mit dem Nostr-Schlüssel signiert ist. Verifizierer können bestätigen, dass die Person, die ein Android-Signaturzertifikat einer App kontrolliert, auch den Nostr-Pubkey kontrolliert, der die Veröffentlichung beansprucht. Nachweise verfallen standardmäßig nach einem Jahr und können explizit widerrufen werden. Implementiert in der [Zapstore](https://github.com/zapstore/zapstore)-Toolchain.

- **NIP-31402: SARA Revenue Share Offering Registry** (Wiki-Eintrag, kind 30817): Definiert kind-31402 adressierbare Events für die Veröffentlichung von Simple Autonomous Revenue Agreement (SARA) Angeboten auf Nostr-Relays. Emittenten bewerben Lightning-abgerechnete Revenue-Share-Konditionen einschließlich Pool-Anteil-Prozentsatz, Auszahlungsauslöser, Schwellenwert in sats, Laufzeit und gestaffelter Preisgestaltung. Agenten und Menschen können Angebote über Relays entdecken und autonom ohne zentrale Plattform abonnieren. Die Kind-Nummer spiegelt kind 30402 (L402 Service Registry, vom selben Autor als begleitender Wiki-Eintrag veröffentlicht), da SARA die Rückseite der L402-Zahlungsbeziehung darstellt.

## Offene PRs und Projekt-Updates

### Damus: [NIP-89](/de/topics/nip-89/) (Recommended Application Handlers)

[PR #3337](https://github.com/damus-io/damus/pull/3337) implementiert NIP-89-Client-Tag-Unterstützung für [Damus](https://github.com/damus-io/damus). Die App sendet nun einen Client-Tag auf allen Posting-Pfaden (Haupt-App, Share-Extension, Highlighter, Entwürfe) und zeigt „via ClientName" neben Zeitstempeln an, wenn andere Apps ihre Tags mitliefern. Ein Datenschutz-Toggle in den Darstellungseinstellungen ermöglicht das Deaktivieren der Tag-Emission. [PR #3652](https://github.com/damus-io/damus/pull/3652) fügt einen Speicherbereich in den Einstellungen mit einem interaktiven Kreisdiagramm hinzu, das NostrDB- und Kingfisher-Cache-Speichernutzung mit Exportunterstützung aufschlüsselt.

Offen: [PR #3657](https://github.com/damus-io/damus/pull/3657) fügt [NIP-65](/de/topics/nip-65/) Relay-Fallback für zitierte Notizen hinzu. Wenn ein Inline-`nevent` einen Autor-Pubkey aber keine Relay-Hints enthält und die Notiz im Pool des Nutzers fehlt, ruft Damus die kind-10002-Relay-Liste des Autors ab und versucht es erneut von dessen Write-Relays.

### Amethyst: [NIP-39](/de/topics/nip-39/) (External Identities), NIP-C0, [NIP-66](/de/topics/nip-66/)

[Amethyst](https://github.com/vitorpamplona/amethyst) mergte eine Welle von NIP-Implementierungen über 28 PRs. Externe Identitätsansprüche werden nun als dedizierte kind-10011-Events unter [NIP-39](/de/topics/nip-39/) ([PR #1747](https://github.com/vitorpamplona/amethyst/pull/1747)) veröffentlicht, was soziale Identität von kind-0-Metadaten mit abwärtskompatibler Rückfalloption trennt. Code-Snippet-Unterstützung via NIP-C0 ([PR #1744](https://github.com/vitorpamplona/amethyst/pull/1744)) fügt kind-1337-Events mit Accessoren für Sprache, Erweiterung, Runtime, Lizenz und Abhängigkeiten hinzu. Die [NIP-66](/de/topics/nip-66/) Relay-Monitoring-Implementierung ([PR #1742](https://github.com/vitorpamplona/amethyst/pull/1742)) deckt beide Event-Kinds mit vollständigem Tag-Parsing für RTT-Metriken, Netzwerktyp, unterstützte NIPs und Geohash ab.

Verschlüsselte DMs kamen auf Amethyst Desktop ([PR #1710](https://github.com/vitorpamplona/amethyst/pull/1710)) mit einem Split-Pane-Chat-Layout, das sowohl [NIP-04](/de/topics/nip-04/) (Encrypted Direct Messages) als auch [NIP-17](/de/topics/nip-17/) (Private Direct Messages) unterstützt. Ein neuer Relay-Feed-Bildschirm ([PR #1733](https://github.com/vitorpamplona/amethyst/pull/1733)) ermöglicht das Durchsuchen von Beiträgen eines bestimmten Relays mit Follow/Unfollow-Funktionalität. Offen: Zensurresistente NIP-05-Verifizierung ([PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734)) fügt einen parallelen Verifizierungspfad für `.bit`-Identifikatoren hinzu, der gegen die Namecoin-Blockchain statt HTTP-DNS auflöst. Wenn Amethyst ein `.bit`-Suffix in einem NIP-05-Feld erkennt, fragt es einen ElectrumX-NMC-Server nach der Transaktionshistorie des Namens ab, parst das `NAME_UPDATE`-Skript aus dem neuesten Output, um den Nostr-Pubkey zu extrahieren, und lehnt Namen ab, die älter als 36.000 Blöcke sind (Namecoins Ablaufzeitraum). ElectrumX-Verbindungen werden über SOCKS5 geroutet, wenn Tor aktiviert ist, mit dynamischer Serverauswahl zwischen Clearnet- und `.onion`-Endpunkten. Ein LRU-Cache mit einer Stunde TTL verhindert wiederholte Blockchain-Abfragen.

### Notedeck: Outbox-Architektur

[PR #1303](https://github.com/damus-io/notedeck/pull/1303) migriert [Notedeck](https://github.com/damus-io/notedeck) von Ad-hoc-Relay-Pool-Management zu einem zentralisierten Outbox-Modell mit Account-bezogenen Subscriptions. Das Messages-Modul veröffentlicht nun eine Standard-DM-Relay-Liste, falls keine existiert, und routet DMs zu den bevorzugten Relays der Empfänger gemäß kind 10050.

### Pika: Gruppenspezifische Profile und Tutorial-Feed

[Pika](https://github.com/sledtools/pika), die Marmot-verschlüsselte Messaging-App für iOS und Android mit Desktop-Build, erhielt gruppenspezifische Profile ([PR #368](https://github.com/sledtools/pika/pull/368)). Nutzer können nun für jeden Gruppenchat einen separaten Anzeigenamen und ein Bild festlegen, zusammen mit einer benutzerdefinierten Bio. Diese Profile werden als verschlüsselte kind-0-Events innerhalb der Marmot-Gruppe veröffentlicht, unsichtbar für jeden außerhalb, mit Rückfall auf das globale Nostr-Profil des Nutzers, wenn kein gruppenspezifisches Profil gesetzt ist. Wenn neue Mitglieder beitreten, sendet der Admin alle gespeicherten Gruppenprofile erneut und jedes Mitglied veröffentlicht seines bei Commit neu. Profilbilder werden vor dem Blossom-Upload Marmot-Media-verschlüsselt. Der PR enthält 16 neue Unit-Tests und macht die Funktion sowohl über einen CLI-Befehl (`update-group-profile`) als auch die UI zugänglich.

Eine neue `pika-news`-Web-App ([PR #401](https://github.com/sledtools/pika/pull/401)) überwacht Pikas eigene GitHub-PRs und generiert automatisch Schritt-für-Schritt-Tutorial-Walkthroughs aus PR-Diffs, die als server-gerenderte Seiten mit [NIP-07](/de/topics/nip-07/) Authentifizierung veröffentlicht werden. Nutzer können bestimmte Tutorials in Echtzeit über Nostr-authentifizierten Chat diskutieren.

### diVine: Einbettbare Widgets und Video-Antworten

[diVine](https://github.com/divinevideo/divine-mobile), die Nostr-native Video-Sharing-Plattform, mergte 132 PRs in zehn Tagen. Einbettbare Iframe-Widgets ([PR #1843](https://github.com/divinevideo/divine-mobile/pull/1843)) bieten eine eigenständige `/embed?npub=...`-Seite, die Nutzerprofil und neueste Videos rendert. Video-Antwort-Funktionalität ([PR #1915](https://github.com/divinevideo/divine-mobile/pull/1915)), hinter einem Feature-Flag geschützt, verwendet Kind-1111-Comments ([NIP-22](/de/topics/nip-22/)) mit [NIP-92](/de/topics/nip-92/) (Media Attachments) imeta-Metadaten. Bluesky-inspirierte dreistufige Inhaltsfilter ([PR #1797](https://github.com/divinevideo/divine-mobile/pull/1797)) bieten Show/Warn/Hide-Steuerungen über 17 [NIP-32](/de/topics/nip-32/) Content-Warning-Kategorien.

### strfry: REQ-Filter-Validierung

[PR #163](https://github.com/hoytech/strfry/pull/163) fügt konfigurierbare REQ-Filter-Validierung zu [strfry](https://github.com/hoytech/strfry) hinzu, dem C++-Nostr-Relay. Betreiber können maximale Filter pro REQ, erforderliche Autoren- oder Tag-Präsenz, erlaubte Kind-Whitelists und pro Filter Kind-Limits festlegen. Die Funktion zielt auf NWC-Relay-Deployments, die strenge Filter-Durchsetzung benötigen. Offen: [PR #173](https://github.com/hoytech/strfry/pull/173) fügt optionale zstd-Kompression für Event-Payloads bei der Aufnahme hinzu.

### rust-nostr: [NIP-62](/de/topics/nip-62/) Request to Vanish

[rust-nostr](https://github.com/rust-nostr/nostr), die Rust-Nostr-Protokollbibliothek, fügte [NIP-62](/de/topics/nip-62/) (Request to Vanish) Unterstützung über alle drei Datenbank-Backends hinzu: [LMDB](https://github.com/rust-nostr/nostr/pull/1268), [SQLite](https://github.com/rust-nostr/nostr/pull/1270) und [In-Memory](https://github.com/rust-nostr/nostr/pull/1272). Die LMDB-Implementierung enthält konfigurierbare Optionen zum Aktivieren oder Deaktivieren von [NIP-09](/de/topics/nip-09/) und NIP-62-Durchsetzung pro Deployment.

### NDK: Collaborative Events und NIP-46-Timeout

[NDK](https://github.com/nostr-dev-kit/ndk), das Nostr Development Kit für JavaScript/TypeScript, mergte [PR #380](https://github.com/nostr-dev-kit/ndk/pull/380) mit `NDKCollaborativeEvent` für Mehrautorendokumente mittels eines adressierbaren Pointer-Events (kind 39382), das autorisierte Autoren definiert. Ein konfigurierbarer Timeout für `NDKNip46Signer` ([PR #381](https://github.com/nostr-dev-kit/ndk/pull/381)) verhindert, dass [NIP-46](/de/topics/nip-46/) Remote-Signing-Operationen endlos hängen, wenn ein Bunker nicht antwortet.

### TENEX: Agenten-Kategorisierung und Pubkey-Gating

[TENEX](https://github.com/tenex-chat/tenex), die Nostr-native KI-Agenten-Orchestrierungsplattform, mergte zwei sicherheitsbezogene PRs. TIP-01 rollenbasierte Agenten-Kategorisierung ([PR #91](https://github.com/tenex-chat/tenex/pull/91)) ordnet Agentenkategorien (Principal, Orchestrator, Worker, Advisor, Auditor) automatisierten Tool-Beschränkungen über eine Denied-Tools-Map zu. Front-Door-Pubkey-Gating ([PR #87](https://github.com/tenex-chat/tenex/pull/87)) stellt sicher, dass nur Events von Whitelisted- oder Backend-signierten Pubkeys zusammen mit bekannten Agenten geroutet werden; unbekannte Pubkeys werden stillschweigend mit OpenTelemetry-Spans für Audit verworfen.

### Zap Cooking: Mitgliedschafts-Dashboard

[Zap Cooking](https://github.com/zapcooking/frontend), die Nostr-basierte Rezeptteilungsplattform, mergte 25 PRs und 85 Commits in zehn Tagen. Ein Mitgliedschafts-Dashboard ([PR #228](https://github.com/zapcooking/frontend/pull/228)) zeigt den Abonnementstatus mit Ablaufdaten und Verwalten/Upgrade-Optionen, reaktiviert Feature-Gates für Sous-Chef- und Zappy-Stufen mit client- und serverseitigen Prüfungen und standardisiert Stufennamen über 26 Dateien. Zweiphasiges Gruppen-Nachrichten-Laden ([PR #227](https://github.com/zapcooking/frontend/pull/227)) bietet einen schnellen 3-Tage-Initial-Fetch für sofortige Anzeige, gefolgt von einem 40-Tage-Backfill im Hintergrund.

Wallet-Mnemonic-Speicher wechselte von pubkey-abgeleiteter Verschlüsselung zu [NIP-44](/de/topics/nip-44/) Encrypt-to-Self ([PR #224](https://github.com/zapcooking/frontend/pull/224)), was eine Schwachstelle behebt, bei der das alte Schema seinen Schlüssel aus `SHA-256(pubkey)` ableitete, was praktisch unverschlüsselt ist, da Pubkeys öffentlich sind. Bestehende Wallets werden beim ersten Laden stillschweigend migriert. [NIP-29](/de/topics/nip-29/) Group Chat erhielt Ungelesen-Indikatoren mit roten Punkt-Badges und Einladungszugang mit kind-9009-Einladungscodes ([PR #213](https://github.com/zapcooking/frontend/pull/213)). Link-Vorschauen und Nostr-Event-Einbettungen werden nun in DMs und Gruppennachrichten gerendert ([PR #218](https://github.com/zapcooking/frontend/pull/218)). Ein Nostr-Backup-Bereich in den Einstellungen ([PR #210](https://github.com/zapcooking/frontend/pull/210)) speichert Follows und Mute-Listen via [NIP-78](/de/topics/nip-78/) (Application-specific Data) verschlüsseltem Speicher mit rotierender 3-Slot-Versionierung. Startperformance verbesserte sich durch verzögerte Benachrichtigungsdienste, Lazy-DOM-Rendering via IntersectionObserver (Reduktion der DOM-Knoten von ~15.000 auf ~3.000 bei einem 200-Event-Feed) und erweiterte Outbox-Cache-TTLs ([PR #208](https://github.com/zapcooking/frontend/pull/208)). Ein anpassbares Rezeptdruck-Modal ([PR #205](https://github.com/zapcooking/frontend/pull/205)) ermöglicht das Umschalten der einzuschließenden Abschnitte mit Live-Vorschau. [Branta SDK](https://github.com/BrantaOps/branta-core) Integration ([PR #222](https://github.com/zapcooking/frontend/pull/222)) fügt Verifizierungs-Guardrails für POST- und GET-Anfragen hinzu.

### Keep: Rust-gesteuerte Zustandsmigration

[Keep](https://github.com/privkeyio/keep-android), der Nostr-basierte Private-Key-Manager für Android, mergte [PR #178](https://github.com/privkeyio/keep-android/pull/178), der vier Kotlin-Konfigurationsspeicher zugunsten von Rust-gesteuertem Shared State aus der keep-mobile-Schicht löscht. Eine 10-Sekunden-Polling-Schleife wurde durch Push-basiertes `KeepStateCallback` aus Rust ersetzt. [PR #179](https://github.com/privkeyio/keep-android/pull/179) fügt verschlüsseltes Backup und Restore mit Passphrase-Schutz hinzu.

### Mostro Mobile: Dispute-Chat-Verschlüsselung

[Mostro Mobile](https://github.com/MostroP2P/mobile), der mobile Client für die Mostro P2P-Bitcoin-Handelsplattform, lieferte eine zweiphasige Migration der Dispute-Chat-Verschlüsselung. Der erste Schritt ([PR #495](https://github.com/MostroP2P/mobile/pull/495)) wechselt von mostro-spezifischem Wrapping zu Shared-Key-Verschlüsselung, die vom pubkey des Admins abgeleitet wird. Darauf aufbauend vereinheitlicht [PR #501](https://github.com/MostroP2P/mobile/pull/501) das Nachrichtenmodell mit `NostrEvent` und speichert Gift-Wrap-Events verschlüsselt auf der Festplatte, konsistent mit dem Peer-to-Peer-Chat-Muster. Ein BIP-340-Signaturfix ([PR #496](https://github.com/MostroP2P/mobile/pull/496)) überschreibt die bip340-Abhängigkeit auf 0.2.0 und behebt einen `bigToBytes()`-Padding-Bug, der 1-2 % der Schnorr-Signaturen ungültig machte und 100 % Fehlerrate für Schlüssel verursachte, deren öffentlicher Schlüssel mit `0x00` beginnt. Bestelldetails zeigen nun menschenlesbare Status-Labels statt roher Protokollwerte, lokalisiert in Englisch, Spanisch, Italienisch und Französisch ([PR #502](https://github.com/MostroP2P/mobile/pull/502)). HalCash wurde hinzugefügt und SEPA als Zahlungsmethode entfernt ([PR #493](https://github.com/MostroP2P/mobile/pull/493)), da SEPA-Überweisungen 24 Stunden überschreiten können (SEPA Instant bleibt).

Auf der Serverseite behebt [Mostro](https://github.com/MostroP2P/mostro) die Wiederherstellung von Dispute-Sitzungen, um das Initiator-Feld einzuschließen ([PR #599](https://github.com/MostroP2P/mostro/pull/599)), und schließt nun automatisch aktive Disputes, wenn ein Verkäufer Gelder freigibt, wobei ein Settled-Nostr-Event veröffentlicht wird, damit Admin-Clients die Auflösung sehen ([PR #606](https://github.com/MostroP2P/mostro/pull/606)).

## Fünf Jahre Nostr im Februar

[Der Newsletter des letzten Monats](/de/newsletters/2026-01-28-newsletter/#fünf-jahre-nostr-im-januar) zeichnete Nostrs Januar-Meilensteine von der frühen Entwicklung über den Damus-Durchbruch bis zur Sicherheitsinfrastruktur im Jahr 2026 nach. Dieser Rückblick behandelt, was in jedem Februar von 2021 bis 2026 geschah.

### Februar 2021: Die Neufassung

Drei Monate nach seiner Entstehung brachte Nostrs Februar die folgenreichste frühe Änderung des Protokolls hervor. Am 14.-15. Februar [schrieb fiatjaf NIP-01 um](https://github.com/nostr-protocol/nostr/commit/33a1a70) und ersetzte das ursprüngliche Nachrichtenformat durch das EVENT/REQ/CLOSE-Modell, das das Protokoll bis heute verwendet. Vor dieser Neufassung kommunizierten Clients und Relays über eine einfachere Struktur. Die Trennung von Event-Veröffentlichung (EVENT) und Subscription-Management (REQ/CLOSE) ermöglichte relay-seitige Filterung, die sich als wesentlich für die Skalierung erweisen sollte.

[NIP-04](/de/topics/nip-04/) kam im selben Monat hinzu und fügte verschlüsselte Direktnachrichten über Shared Secrets aus Diffie-Hellman-Schlüsselaustausch über secp256k1 hinzu. Die Verschlüsselung war grundlegend (AES-256-CBC) und wurde später durch die geprüfte Kryptografie von [NIP-44](/de/topics/nip-44/) ersetzt, gab aber der Handvoll früher Nutzer ihren ersten privaten Kommunikationskanal auf dem Protokoll.

Das Tooling expandierte mit [noscl](https://github.com/fiatjaf/noscl), einem Go-Kommandozeilen-Client für terminalbasierte Relay-Interaktion, und futurepaul startete [nostr-rs](https://github.com/futurepaul/nostr-rs), eine frühe Rust-Implementierung. Das gesamte Netzwerk lief auf zwei oder drei Relays, koordiniert über eine [Telegram-Gruppe](https://t.me/nostr_protocol), mit ungefähr sieben aktiven Mitwirkenden.

### Februar 2022: Aufbau von Momentum

Der [Hacker-News-Beitrag](https://news.ycombinator.com/item?id=29749061) vom 31. Dezember 2021 zog weiterhin Entwickler bis in den Februar hinein an. Das [nostr-protocol/nostr](https://github.com/nostr-protocol/nostr)-Repository (das formale [NIPs-Repository](https://github.com/nostr-protocol/nips) existierte erst ab Mai 2022) erhielt im Februar sechs Pull Requests, darunter NIP-13 (Proof of Work) von vinliao, NIP-14 (Reputation) von fiatjaf, NIP-15 (Resource Relations) von Cameri und [NIP-17](https://github.com/nostr-protocol/nostr/pull/75) (Git Updates Over Nostr) von melvincarvalho. Die NIP-Nummer wurde später Private Direct Messages zugewiesen; Git-Zusammenarbeit auf Nostr wurde separat fortgesetzt durch das, was [gitworkshop.dev](https://gitworkshop.dev) wurde.

Greg Heartsfields [nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay) war das Arbeitspferd des Monats mit 34 Commits und drei Releases. Version 0.5.0 am 12. Februar fügte [NIP-05](/de/topics/nip-05/) verifizierte Nutzer-Publishing-Limits hinzu. Die Versionen 0.5.1 und 0.5.2 folgten in den nächsten zwei Wochen, und das Relay bewältigte den Großteil des Netzwerk-Traffics allein.

Robert C. Martin (Uncle Bob) baute [more-speech](https://github.com/unclebob/more-speech), einen Clojure-Desktop-Client, und verzeichnete 69 Commits zwischen dem 18. Januar und Ende Februar. Sein Engagement brachte Aufmerksamkeit aus der breiteren Software-Engineering-Community. fiatjafs [nos2x](https://github.com/fiatjaf/nos2x) Browser-Erweiterung lieferte [NIP-04](/de/topics/nip-04/) Decrypt-Unterstützung und Relay-Preference-Policies im Februar und implementierte das `window.nostr`-Interface ([NIP-07](/de/topics/nip-07/)), das Web-Clients noch heute für Key-Delegation nutzen.

[Branle](https://github.com/fiatjaf/branle), weiterhin der primäre Web-Client, erhielt am 13. Februar `web+nostr`-Protokoll-Handler-Registrierung, ein früher Versuch des Deep-Linking zwischen Nostr-Anwendungen. [nostr-tools](https://github.com/nbd-wtf/nostr-tools) verschärfte die NIP-05-Validierung. [go-nostr](https://github.com/nbd-wtf/go-nostr) fügte NIP-04-Encrypted-DM-Unterstützung und NIP-12 (Generic Tag Queries) Parsing über 11 Commits hinzu. Das Netzwerk lief auf ungefähr 7-15 Relays mit einer aktiven Nutzerbasis wahrscheinlich in den niedrigen Hunderten. Damus und Nostream existierten noch nicht und würden erst im April 2022 erscheinen.

### Februar 2023: Internationale Aufmerksamkeit

Februar 2023 brachte Nostr seine größte Welle öffentlicher Aufmerksamkeit. [Damus](https://github.com/damus-io/damus), der iOS-Client von William Casarin, war am [31. Januar im Apple App Store zugelassen worden](https://www.coindesk.com/tech/2023/02/01/decentralized-social-media-project-nostrs-damus-gets-listed-on-apple-app-store) nach wiederholten Ablehnungen. Am 1. Februar erreichte er die Top 10 im Bereich US Social Networking. Zwei Tage später, am 2. Februar, [entfernte Apple Damus aus Chinas App Store](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/), Berichten zufolge auf Antrag der Cyberspace Administration of China.

Große Medien wie TechCrunch und CoinDesk berichteten über die Entfernung und verstärkten das Bewusstsein sowohl für die App als auch für das Protokoll. Einzigartige öffentliche Schlüssel mit Metadaten auf nostr.directory überschritten am 3. Februar 300.000. Alle Relays wurden von Enthusiasten betrieben, die aus eigener Tasche zahlten, und die Infrastruktur kämpfte, die Last zu bewältigen. Etwa 289 Relays wurden Anfang Februar erfasst, eine Zahl, die weiter anstieg.

Das [NIPs-Repository](https://github.com/nostr-protocol/nips) verzeichnete in diesem Monat 29 gemergte Pull Requests, die höchste Einzelmonatszahl in der Geschichte des Protokolls bis dahin. [NIP-57](https://github.com/nostr-protocol/nips/pull/224) (Lightning Zaps) und [NIP-23](https://github.com/nostr-protocol/nips/pull/220) (Long-form Content) wurden beide am 13. Februar gemergt und fügten Bitcoin-Mikrozahlungen hinzu und erweiterten Nostr an einem einzigen Tag über kurze Beiträge hinaus. [NIP-65](/de/topics/nip-65/) (Relay List Metadata) wurde eine Woche zuvor am 7. Februar gemergt und ermöglichte das darauffolgende Outbox-Modell. [NIP-46](/de/topics/nip-46/) (Nostr Connect) und [NIP-58](/de/topics/nip-58/) (Badges) landeten ebenfalls vor Monatsende.

Die Human Rights Foundation [vergab 50.000 US-Dollar an William Casarin für Nostr- und Damus-Entwicklung](https://hrf.org/devfund2023q1) am 21. Februar, einer der ersten institutionellen Grants für ein Nostr-Projekt. OpenSats hatte seinen Nostr-Fonds noch nicht gestartet (das kam im [Juli 2023](https://opensats.org/blog/nostr-grants-july-2023)).

### Februar 2024: Protokollbeständigkeit

Februar 2024 verlagerte den Fokus von Wachstum auf Protokollbeständigkeit. [NIP-17](/de/topics/nip-17/) (Private Direct Messages), seit dem vergangenen Juli offen, arbeitete auf einen Ersatz für die alternde [NIP-04](/de/topics/nip-04/) Verschlüsselung mit [NIP-44](/de/topics/nip-44/)s geprüfter Kryptografie und [NIP-59](/de/topics/nip-59/) Gift-Wrapping hin. NIP-04 leckte Metadaten an Relay-Betreiber, die Sender-Empfänger-Paare sehen konnten. NIP-17 verbirgt die Absenderidentität hinter Einmal-Schlüsselpaaren und wurde im Frühjahr nach einer letzten Überprüfungsrunde im März gemergt.

[NIP-29](/de/topics/nip-29/) (Simple Groups) [wurde am 28. Februar gemergt](https://github.com/nostr-protocol/nips/pull/566) nach monatelanger Diskussion und definiert, wie Relays moderierte Gruppenchats mit Admin-Rollen und Zugangskontrolle hosten können. [NIP-92](/de/topics/nip-92/) (imeta-Tags) wurde am 1. Februar gemergt und standardisiert, wie Clients Bilddimensionen und Blurhash-Vorschauen an Medien-Events anhängen.

Am 16. Februar fügte das NIPs-Repository [BREAKING.md](https://github.com/nostr-protocol/nips/commit/62c48eff) hinzu, eine Datei zur Verfolgung rückwärtskompatibler Änderungen an der Protokollspezifikation. Ihre Erstellung bestätigte, dass Nostr einen Reifegrad erreicht hatte, bei dem Breaking Changes formale Dokumentation erforderten.

Zweiundzwanzig Pull Requests wurden in diesem Monat gemergt. [npub.cash](https://github.com/cashubtc/npubcash-server) startete als Lightning-Adressdienst, der jedem npub den Empfang von Zahlungen ermöglicht, ohne einen Server zu betreiben. Ein [akademisches Paper](https://arxiv.org/abs/2402.05709), veröffentlicht am 8. Februar, stellte fest, dass 95 % der kostenlosen Relays die Betriebskosten nicht durch Spenden decken konnten, wobei 35 % der kostenpflichtigen Relays Zugangsgebühren unter 1.000 sats (damals ungefähr 0,45 US-Dollar) erhoben.

### Februar 2025: Infrastrukturwachstum

Februar 2025 brachte 28 gemergte Pull Requests für das NIPs-Repository. Ein [Right to Vanish](/de/topics/nip-62/)-NIP wurde am 19. Februar gemergt und definiert, wie Nutzer die Löschung ihrer Daten von Relays anfordern können, als Reaktion auf regulatorische Fragen zu Datenportabilität und Nutzerkontrolle.

[NIP-60](/de/topics/nip-60/) (Cashu Wallet) und NIP-61 (Nutzaps) erhielten Vereinfachungs-Updates, die das Ecash-Token-Speicherformat strafften. Ein q-Tag (Quote-Tag) Rollout setzte sich über mehrere NIPs fort und standardisierte, wie Events andere Events für Zitierung und Threading referenzieren.

Client-Releases markierten stetigen Fortschritt. [Notedeck](https://github.com/damus-io/notedeck) v0.3.0 Alpha erschien am letzten Januartag, mit fortgesetzter Adoption im Februar. Primal v2.1 folgte am 7. Februar, und [GRAIN](https://github.com/0ceanSlim/grain) v0.3.0, eine Go-Relay-Implementierung, am 21. Februar.

NOSTRLDN v5 brachte die Londoner Nostr-Community zu ihrem fünften Meetup zusammen. Eine DVMCP-Bridge verband Nostrs Data Vending Machines ([NIP-90](/de/topics/nip-90/)) mit dem Model Context Protocol und deutete die KI-Agenten-Integrationsarbeit an, die im folgenden Monat kam.

### Februar 2026: Jenseits von Social Media

*Die Aktivität vom Februar 2026 stammt aus Nostr-Compass-Ausgaben [#8](/de/newsletters/2026-02-04-newsletter/) bis [#11](/de/newsletters/2026-02-25-newsletter/).*

Februar 2026 brachte das breiteste Spektrum an Application-Layer-Entwicklung in einem einzelnen Nostr-Monat. [Mostro](https://github.com/MostroP2P/mostro) lieferte seine [erste öffentliche Beta](/de/newsletters/2026-02-11-newsletter/#mostro-liefert-erste-öffentliche-beta) für dezentralen Peer-to-Peer-Bitcoin-Handel, und [Zapstore](https://github.com/zapstore/zapstore) erreichte [1.0 Stable](/de/newsletters/2026-02-11-newsletter/#zapstore-v100) nach Monaten in der Release-Candidate-Testphase. [White Noise v0.3.0](/de/newsletters/2026-02-25-newsletter/#white-noise-v030) lieferte Echtzeit-[Marmot](/de/topics/mls/)-verschlüsseltes Messaging mit Amber-Signer-Unterstützung und über 160 gemergten Verbesserungen.

Konkurrierende KI-Agenten-Vorschläge von pablof7z (NIP-AE für Agenten-Workflows, NIP-AD für MCP-Server-Ankündigungen) und joelklabo (AI Agent Messages) kamen zusammen mit einem [DVM Agent Coordination-Vorschlag](/de/newsletters/2026-02-25-newsletter/#nip-updates), der [NIP-90](/de/topics/nip-90/) erweitert. [ContextVM](/de/newsletters/2026-02-25-newsletter/#contextvm-mcp-über-nostr) lieferte SDK-Verbesserungen, die das Model Context Protocol mit dem Nostr-Transport verbinden. [Burrow](/de/newsletters/2026-02-25-newsletter/#burrow-mls-messaging-für-ki-agenten) fügte [Marmot](/de/topics/mls/)-verschlüsseltes Messaging sowohl für KI-Agenten als auch für Menschen hinzu und erweiterte Nostrs Identitäts- und Relay-Infrastruktur in die Machine-to-Machine-Kommunikation.

[FIPS](/de/newsletters/2026-02-25-newsletter/#fips-nostr-natives-mesh-networking) lieferte eine funktionierende Rust-Implementierung von Nostr-nativem Mesh-Networking, die secp256k1-Schlüsselpaare als Knotenidentitäten mit transport-agnostischem Routing über UDP, Ethernet, Bluetooth oder LoRa-Radio verwendet. Sein Design zeigte, dass Nostrs Schlüsselmodell über Social Media hinaus in physische Netzwerkinfrastruktur reicht.

[OpenSats kündigte seine fünfzehnte Welle von Nostr-Grants an](https://opensats.org/blog/fifteenth-wave-of-nostr-grants) und finanzierte Projekte wie ContextVM und Nostube. Protokolländerungen umfassten [NIP-47](/de/topics/nip-47/) Hold-Invoice-Unterstützung für Nostr Wallet Connect und [NIP-45](/de/topics/nip-45/) (Counting Results) HyperLogLog für relay-seitige Zählschätzung. [NIP-85](/de/topics/nip-85/) (Trusted Assertions) Service-Provider-Auffindbarkeit für [Web-of-Trust](/de/topics/web-of-trust/)-Bewertung wurde ebenfalls gemergt. [rust-nostr](https://github.com/rust-nostr/nostr) begann ein vollständiges API-Redesign, während Nostria 3.0 und [Frostr](https://github.com/FROSTR-ORG) (iOS TestFlight) beide erschienen. [Blossom](/de/topics/blossom/)s lokale Cache-Schicht adressierte die Medienverfügbarkeit über Relays.

### Ausblick

Fünf Februare Protokollgeschichte zeigen eine konsistente Progression von grundlegender Arbeit zu Application-Layer-Diversifizierung, mit dem Nutzerzustrom 2023 als Wendepunkt. 2021 arbeiteten sieben Mitwirkende über drei Relays. Bis 2026 unterstützte dasselbe Protokoll Mesh-Networking und autonome Agenten-Vorschläge auf Produktionsinfrastruktur.

---

Das war's für diese Woche. Wer etwas baut oder Neuigkeiten zu teilen hat: <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Per [NIP-17](/de/topics/nip-17/) DM erreichbar</a> oder auf Nostr findbar.
