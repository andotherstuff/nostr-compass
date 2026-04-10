---
title: 'Nostr Compass #17'
date: 2026-04-08
translationOf: /en/newsletters/2026-04-08-newsletter.md
translationDate: 2026-04-09
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, deinem wöchentlichen Wegweiser durch Nostr.

**Diese Woche:** [Amethyst](https://github.com/vitorpamplona/amethyst) liefert [v1.08.0](#amethyst-liefert-arti-tor-und-integriert-reines-kotlin-mls-und-marmot) mit Arti-Tor-Integration und einer neu gestalteten Shorts-UI aus und integriert zugleich reine Kotlin-Implementierungen von [MLS](/de/topics/mls/) und [Marmot](/de/topics/marmot/) in seine [Quartz](/de/topics/quartz/)-Bibliothek. [Nostur](https://github.com/nostur-com/nostur-ios-public) liefert [v1.27.0](#nostur-v1270-fügt-videoaufnahme-und-private-antworten-hinzu) mit Videoaufnahme, animierten GIF-Profilen und privaten Antworten. [Shosho](https://github.com/r0d8lsh0p/shosho-releases) startet [v0.15.0](#shosho-v0150-startet-shows-und-ein-vertikales-video-karussell) mit Shows, also benutzerdefinierten Livestream-Infos mit OBS-Anbindung, und einem TikTok-artigen vertikalen Video-Karussell. [Nymchat](https://github.com/Spl0itable/NYM) [nimmt Marmot zurück und liefert erweiterte NIP-17-Gruppenchats aus](#nymchat-nimmt-marmot-zurück-und-liefert-erweiterte-nip-17-gruppenchats-aus), die rotierende ephemeral keys nutzen. [Nostr VPN](https://github.com/mmalmi/nostr-vpn) liefert [exit node-Support und Umbrel-Paketierung](#nostr-vpn-liefert-exit-node-support-und-umbrel-paketierung-aus) über sechs Releases hinweg. [Amber](https://github.com/greenart7c3/Amber) springt auf [v6.0.0-pre1](#amber-v600-pre1-fügt-signing-keys-pro-verbindung-für-nip-46-hinzu) mit [NIP-46](/de/topics/nip-46/)-signing keys pro Verbindung und In-App-Updates über Zapstore. [Notedeck](https://github.com/damus-io/notedeck) erreicht [v0.10.0-beta](#notedeck-v0100-beta-liefert-zapstore-self-update-aus) mit APK-Self-Update via Zapstore, und [NIP-58](/de/topics/nip-58/) (Badges) erhält eine [kind-Migration](#nip-updates). Zwei NIP-Deep Dives behandeln [NIP-17](/de/topics/nip-17/) (Private Direct Messages) und [NIP-46](/de/topics/nip-46/) (Nostr Remote Signing).

## Neuigkeiten

### Amethyst liefert Arti Tor und integriert reines Kotlin MLS und Marmot

[Amethyst](https://github.com/vitorpamplona/amethyst), der von vitorpamplona gepflegte Android-Client, lieferte vier Releases von [v1.07.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.3) bis [v1.08.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.08.0) aus und mergte ein großes Paket noch unveröffentlichter Arbeit in seine [Quartz](/de/topics/quartz/)-Bibliothek, also das gemeinsame Kotlin-Multiplatform-Nostr-Modul. Das Hauptrelease ist v1.08.0 "Arti Tor", das die Tor-Anbindung der App von der C-basierten Tor-Bibliothek auf [Arti](https://gitlab.torproject.org/tpo/core/arti), die Rust-Implementierung des Tor Project, umstellt. Die Migration behebt zufällige Abstürze, die unter den bisherigen C-Tor-Bindings auftraten. Arti ist der langfristige Ersatz des Tor Project für die C-Codebasis, von Grund auf in Rust geschrieben für Memory Safety und async I/O.

Der Release v1.07.3 gestaltet die Shorts-UI neu und ersetzt das seitenbasierte Design durch randlose Feeds für Bilder, Shorts und lange Videos. Derselbe Release migriert Badges auf kind `10008` und Bookmarks auf kind `10003` und richtet sich damit an der [NIP-58](/de/topics/nip-58/)-kind-Migration aus, die [diese Woche gemergt wurde](#nip-updates). v1.07.4 behebt ein Problem bei der Secret-Verarbeitung in Nostr Wallet Connect, und v1.07.5 behebt einen Absturz beim Bild-Upload.

Auf `main`, aber noch nicht in einem getaggten Release, hat das Team eine vollständige Kotlin-Implementierung sowohl von [MLS](/de/topics/mls/) als auch des [Marmot](/de/topics/marmot/)-Protokolls geschrieben und damit den Bedarf an nativen C/Rust-Bibliotheks-Bindings ersetzt. [PR #2147](https://github.com/vitorpamplona/amethyst/pull/2147) fügt die zentrale Marmot-MLS-Schicht für Gruppennachrichten hinzu, [PR #2149](https://github.com/vitorpamplona/amethyst/pull/2149) fügt die Gruppenchat-UI hinzu, [PR #2146](https://github.com/vitorpamplona/amethyst/pull/2146) fügt eingehende und ausgehende Message-Processor mit Subscription-Manager hinzu, [PR #2141](https://github.com/vitorpamplona/amethyst/pull/2141) fügt Persistenz für MLS-Gruppenstatus und KeyPackage-Rotationsverwaltung hinzu, [PR #2150](https://github.com/vitorpamplona/amethyst/pull/2150) fügt eine vollständige MLS-Testsuite mit verbessertem GroupInfo-Signing hinzu, und [PR #2158](https://github.com/vitorpamplona/amethyst/pull/2158) fügt Tracking für den Veröffentlichungsstatus von KeyPackages hinzu. [PR #2166](https://github.com/vitorpamplona/amethyst/pull/2166) fügt eine reine Kotlin-secp256k1-Implementierung für Nostr-Kryptographieoperationen hinzu und ersetzt damit die Abhängigkeit von der nativen C-Bibliothek. Zusammen mit der Kotlin-MLS-Implementierung kann [Quartz](/de/topics/quartz/) Nostr-Signing und Marmot-Gruppennachrichten ohne jegliche native Bindings ausführen, was den Weg für Kotlin-Multiplatform-Ziele einschließlich iOS öffnet.

Das Team baut außerdem Unterstützung für [NIP-AC](/en/topics/nip-ac/) (P2P Voice and Video Calls): [PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143) fügt eine vollständige Testsuite für die NIP-AC-Call-State-Machine hinzu, und [PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164) verhindert, dass veraltete Call Offers nach einem App-Neustart erneut ausgelöst werden.

### Nostur v1.27.0 fügt Videoaufnahme und private Antworten hinzu

[Nostur](https://github.com/nostur-com/nostur-ios-public), der iOS-Nostr-Client, lieferte [v1.27.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/v1.27.0) am 2. April aus. Der Release fügt Videoaufnahme direkt in der App mit Zuschneiden vor dem Upload hinzu, sodass Nutzer kurze Clips aufnehmen, auf Länge schneiden und veröffentlichen können, ohne den Client zu verlassen. Die Unterstützung für animierte GIFs erstreckt sich nun auch auf Profil- und Bannerbilder, zusätzlich kam Rendering für animierte WebP-Dateien hinzu. Eine neue Shortcuts-Integration erlaubt es Nutzern, Nostr-Posts aus Apple-Shortcuts-Automationen zu senden. Der Release fügt außerdem private Antworten hinzu und behebt DM-Kompatibilitätsprobleme, die die Zustellung zwischen Nostur und anderen Clients beeinträchtigten.

### Shosho v0.15.0 startet Shows und ein vertikales Video-Karussell

[Shosho](https://github.com/r0d8lsh0p/shosho-releases), die Nostr-Livestreaming-App, lieferte [v0.15.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.0) und [v0.15.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.1) am 7. April aus. Das Hauptfeature ist Shows: Streamer können vor dem Start eines Livestreams eigene Show-Informationen anlegen und ihre Show mit OBS oder einem anderen externen Encoder verbinden. Dadurch wird die Metadatenfrage "Was streame ich?" vom eigentlichen Go-Live getrennt, sodass Streamer Titel, Beschreibungen und Produkte vorbereiten können, bevor sie senden. Derselbe Release fügt außerdem ein TikTok-artiges vertikales Video-Karussell zum Durchwischen von Lives, Clips und Replays in einem Vollbild-Feed hinzu sowie Quick Add zum Veröffentlichen von Videoclips und Hinzufügen von Produkten direkt von einer Profilseite. v0.15.1 behebt einen Fehler, bei dem die Tastatur das Chat-Eingabefeld des Livestreams verdeckte.

## Releases

### Notedeck v0.10.0-beta liefert Zapstore-Self-Update aus

[Notedeck](https://github.com/damus-io/notedeck), der Desktop- und Mobile-Client des Damus-Teams, lieferte [v0.10.0-beta.1](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.1) und [v0.10.0-beta.2](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.2) als Test-Prereleases für APK-Self-Update aus. [PR #1417](https://github.com/damus-io/notedeck/pull/1417) fügt APK-Self-Update über den Nostr/Zapstore-Updater auf Android hinzu und baut auf der [Nostr-nativen Release-Erkennung aus Newsletter #14](/en/newsletters/2026-03-18-newsletter/#notedeck-moves-release-discovery-onto-nostr) auf. Der Update-Flow entdeckt neue Releases über Nostr-Events, die an Relays veröffentlicht werden, lädt dann das APK dort herunter, wo der Entwickler es hostet, also etwa bei GitHub Releases, einem Blossom-CDN oder anderen Quellen, verifiziert den SHA-256-Hash gegen das signierte Nostr-Event und installiert es. [PR #1438](https://github.com/damus-io/notedeck/pull/1438) behebt einen Fehler im Welcome Screen, bei dem Login- und CreateAccount-Buttons sofort wieder zurücknavigierten, und [PR #1424](https://github.com/damus-io/notedeck/pull/1424) behebt Textüberlauf in der Agentium-AI-Session-Ansicht.

### Amber v6.0.0-pre1 fügt signing keys pro Verbindung für NIP-46 hinzu

[Amber](https://github.com/greenart7c3/Amber), die [NIP-55](/de/topics/nip-55/) (Android Signer Application) Signer-App, lieferte [v6.0.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.0-pre1) am 4. April aus. Die wichtigste Änderung sind signing keys pro Verbindung für das [NIP-46](/de/topics/nip-46/) (Nostr Remote Signing) Bunker-Protokoll. Statt ein einziges Schlüsselpaar für alle Bunker-Verbindungen zu verwenden, erzeugt Amber nun für jeden verbundenen Client einen eigenen Schlüssel. Wird die Verbindung eines Clients kompromittiert, kann ein Angreifer den Signer nicht gegenüber anderen Clients imitieren.

[PR #377](https://github.com/greenart7c3/Amber/pull/377) fügt In-App-Prüfung und Installation von Updates via Zapstore hinzu und folgt damit [Notedeck](#notedeck-v0100-beta-liefert-zapstore-self-update-aus) bei der Einführung Nostr-nativer App-Distribution. [PR #375](https://github.com/greenart7c3/Amber/pull/375) behandelt AndroidKeyStore-Fehler robust, indem eine Warnung angezeigt wird statt die App abstürzen zu lassen, und [PR #371](https://github.com/greenart7c3/Amber/pull/371) fügt Datenbankbereinigung mit Größenlimits und Inhaltskürzung hinzu, um unbegrenztes Speicherwachstum zu verhindern. Das Prerelease trägt außerdem die [NIP-42](/de/topics/nip-42/)-Relay-Auth-Whitelist und Mnemonic-Recovery-Phrase-Login aus dem [v5.0.x-Zyklus, den wir letzte Woche behandelt haben](/en/newsletters/2026-04-01-newsletter/#amber-v502-through-v504).

### Nostria liefert native Mobile-App aus

[Nostria](https://github.com/nostria-app/nostria), der von SondreB gepflegte plattformübergreifende Nostr-Client, veröffentlichte eine native Mobile-App für Android mit acht Releases von [v3.1.11](https://github.com/nostria-app/nostria/releases/tag/v3.1.11) bis [v3.1.18](https://github.com/nostria-app/nostria/releases/tag/v3.1.18). Die wichtigste neue Fähigkeit ist native Unterstützung für lokale Signer wie [Amber](https://github.com/greenart7c3/Amber) und Aegis. [Desktop-Installer](https://www.nostria.app/download) für Linux, macOS und Windows sind ebenfalls verfügbar. [PR #610](https://github.com/nostria-app/nostria/pull/610) senkt den Speicherdruck im Feed mit adaptiven Runtime-Limits und Bereinigung von Preview-URLs. v3.1.14 behebt die Integration mit Brainstorm, einem Anbieter für [Web of Trust](/de/topics/web-of-trust/). v3.1.15 konzentriert sich auf Musik-Verbesserungen. Die neue Android-App ist auf [Zapstore](https://zapstore.dev/apps/app.nostria) verfügbar.

### diVine 1.0.8 liefert fortsetzbare Uploads und DMs aus

[diVine](https://github.com/divinevideo/divine-mobile), der Kurzform-Video-Client, lieferte [1.0.8](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.8) mit 87 gemergten PRs aus. Fortsetzbare Uploads erlauben es Creatorn, unterbrochene Uploads Chunk für Chunk wiederaufzunehmen, statt bei instabiler Verbindung von vorn zu beginnen. Der Release fügt Einstellungen für Videoqualität und Bitrate, Double-Tap zum Liken und DM-Verbesserungen hinzu. [PR #2722](https://github.com/divinevideo/divine-mobile/pull/2722) fügt ein macOS-Kamera-Plugin für Desktop-Videoaufnahme hinzu, und [PR #2820](https://github.com/divinevideo/divine-mobile/pull/2820) migriert das Benachrichtigungssystem auf eine BLoC-Architektur mit Anreicherung und Gruppierung. Das Team ersetzte außerdem AI-generierte Sticker und Kategorie-Grafiken durch OpenMoji-SVGs ([PR #2844](https://github.com/divinevideo/divine-mobile/pull/2844), [PR #2842](https://github.com/divinevideo/divine-mobile/pull/2842)).

### Manent v1.3.0 fügt Unschärfe für sensible Notizen und NIP-42-Auth hinzu

[Manent](https://github.com/dtonon/manent), die private App für verschlüsselte Notizen und Dateispeicherung, lieferte [v1.3.0](https://github.com/dtonon/manent/releases/tag/v1.3.0) am 2. April aus. Nutzer können Notizen nun als sensibel markieren, damit sie in der Listenansicht unscharf dargestellt werden und private Inhalte beim beiläufigen Scrollen verborgen bleiben. Der Release fügt außerdem Unterstützung für [NIP-42](/de/topics/nip-42/) (Authentication of Clients to Relays) hinzu, sodass Manent sich bei Relays authentifizieren kann, die dies verlangen, bevor sie Events annehmen. Manent speichert alle Daten verschlüsselt auf Nostr-Relays unter Verwendung des Schlüsselpaares des Nutzers, daher erweitert NIP-42 die Menge an Relays, die es für die Speicherung nutzen kann.

### Wisp v0.17.0 bis v0.17.3 fügen Livestream-Zaps und Wallet-Backup hinzu

[Wisp](https://github.com/barrydeen/wisp), der Android-Nostr-Client, lieferte sechs Releases von [v0.16.2-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.2-beta) bis [v0.17.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.17.3-beta) mit 44 gemergten PRs aus. Der Release v0.17.0 fügt Sicherheitsabfragen für Wallet-Backups und Verbesserungen an der Zap-UX hinzu. [v0.17.1](https://github.com/barrydeen/wisp/releases/tag/v0.17.1-beta) fügt plattformübergreifende Sichtbarkeit des Livestream-Chats und Livestream-Zap-Funktionalität hinzu. [PR #423](https://github.com/barrydeen/wisp/pull/423) fügt automatisches Suchen von Profilen, eine Zap-Erfolgsanimation und Verbesserungen bei Nutzerstatus hinzu. [PR #426](https://github.com/barrydeen/wisp/pull/426) behebt einen Out-of-Memory-Absturz in `computeId` bei Events mit großen Tag-Listen. Die v0.16.x-Releases fügten Emoji-Shortcode-Autocomplete, Verbesserungen an der Gruppenchat-UI und Filterung blockierter Nutzer über alle Benachrichtigungspfade hinweg hinzu.

### Mostro liefert Deep Links, Nostr-Wechselkurse und einen Fix für doppelte Zahlungen aus

[Mostro](https://github.com/MostroP2P/mostro), die auf Nostr basierende Peer-to-Peer-Bitcoin-Börse, sah diese Woche Updates sowohl am Server-Daemon als auch am Mobile-Client. Auf der Serverseite verhindert [PR #692](https://github.com/MostroP2P/mostro/pull/692), dass veraltete Order-Schreibvorgänge doppelte Zahlungen verursachen, also ein Fehlerbild, bei dem ein Verkäufer für denselben Trade zweimal bezahlt werden könnte. [PR #693](https://github.com/MostroP2P/mostro/pull/693) nutzt gezielte Updates für dev_fee-Schreibvorgänge statt vollständiger Order-Überschreibungen.

[Mostro Mobile](https://github.com/MostroP2P/mobile), der Flutter-Client, lieferte [v1.2.3](https://github.com/MostroP2P/mobile/releases/tag/v1.2.3) am 3. April aus. Der Release behandelt Deep Links von unterschiedlichen Mostro-Instanzen, sodass Nutzer Links antippen können, die zum richtigen Exchange-Server führen. [PR #498](https://github.com/MostroP2P/mobile/pull/498) erkennt Admin- und Dispute-DMs in der Hintergrund-Benachrichtigungspipeline, und die App holt Wechselkurse nun von Nostr mit HTTP/Cache-Fallback. [PR #560](https://github.com/MostroP2P/mobile/pull/560) behebt einen blockierenden Relay-Verbindungsfehler, der die App unter bestimmten Netzwerkbedingungen daran hinderte, Relays zu erreichen.

### Unfiltered v1.0.12 fügt Hashtags und Kommentare hinzu

[Unfiltered](https://github.com/dmcarrington/unfiltered), ein Nostr-Client mit Fokus auf bildzentrierte Inhalte, lieferte [v1.0.12](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.12) aus. [PR #69](https://github.com/dmcarrington/unfiltered/pull/69) fügt Unterstützung für Hashtags hinzu, und [PR #72](https://github.com/dmcarrington/unfiltered/pull/72) fügt die Möglichkeit hinzu, Kommentare zu Beiträgen zu schreiben und anzuzeigen. [PR #71](https://github.com/dmcarrington/unfiltered/pull/71) behebt Navigationsprobleme bei Beiträgen mit mehreren Bildern.

### Primal Android liefert Wallet-Multi-Account-Sharing und Auto-Reconnect für Remote Signer aus

[Primal](https://github.com/PrimalHQ/primal-android-app), der Android-Nostr-Client, lieferte am 7. April einen Release aus. Das Update fügt Wallet-Multi-Account-Sharing sowie ein Overflow-Menü mit Wallet-Löschung in den Dev Tools hinzu. Der Remote Signer verbindet sich nun bei Verbindungsabbrüchen automatisch neu, und auch der Wallet-Service erhielt eine eigene Auto-Reconnect-Logik. Zu den Fixes gehören, dass Poll-Zap-Stimmen nicht länger als Top Zaps erscheinen, leere Poll-Optionen keinen Absturz mehr auslösen, Wallet-Guthaben verborgen wird, wenn keine Wallet existiert, und WalletException-Typen in NWC-Antworten auf Fehlercodes abgebildet werden.

### Titan v0.1.0 startet nativen nsite://-Browser mit Bitcoin-Namensregistrierung

[Titan](https://github.com/btcjt/titan), ein nativer Desktop-Browser für das Nostr-Web, lieferte [v0.1.0](https://github.com/btcjt/titan/releases/tag/v0.1.0) am 7. April aus. Titan löst `nsite://`-URLs auf, indem es menschenlesbare, auf Bitcoin registrierte Namen nachschlägt, Nostr-Relays nach den Content-Events der Website abfragt und Seiten rendert, die von [Blossom](/de/topics/blossom/)-Servern geladen werden. Das Ergebnis ist ein Browser-Erlebnis ohne DNS, ohne TLS-Zertifikate und ohne Hosting-Anbieter. Namen werden über eine [Weboberfläche](https://npub1hmq6xuqnplk5lw0h3700cujmx5gymqn5wrn42u6432r6ntzumezqc3marw.nsite.lol/register) registriert, die mit Bitcoin-Transaktionen verknüpft ist. Der erste Release kommt als macOS-`.dmg` für ARM, mit Rosetta-2-Unterstützung für Intel, und enthält Unterstützung für Nix-Entwicklungsumgebungen.

### Bikel v1.5.0 liefert nativen Foreground Service für de-Googled Phones aus

[Bikel](https://github.com/Mnpezz/bikel), ein dezentraler Fahrrad-Tracker, der Fahrten über Nostr in öffentliche Infrastrukturdaten verwandelt, lieferte [v1.5.0](https://github.com/Mnpezz/bikel/releases/tag/v1.5.0) am 4. April aus. Der Release migriert von dem von GMS abhängigen Expo TaskManager zu einem benutzerdefinierten nativen Foreground Service und sorgt damit für zuverlässiges Ride-Tracking im Hintergrund auf LineageOS, GrapheneOS und anderen de-Googled-Android-Varianten. Der Bikel Bot erhielt eine Dual-Pocket-Architektur mit autonomer eCash-Einsammlung via Cashu nutzaps. v1.4.3 und v1.4.2 beheben die Synchronisierung des Hintergrund-Trackings für nicht standardisierte Android-Umgebungen, und die App fügt Schalter für OSM-Fahrradständer-Kartenpunkte hinzu.

### Sprout fügt NIP-01-, NIP-23- und NIP-33-Unterstützung hinzu

[Sprout](https://github.com/block/sprout), eine Kommunikationsplattform von Block mit eingebautem Nostr-relay, lieferte [desktop/v0.1.0-rc7](https://github.com/block/sprout/releases/tag/desktop/v0.1.0-rc7) am 6. April aus. Diese Woche fügte das Team Unterstützung für [NIP-23](/en/topics/nip-23/) (Long-form Content) Artikel mit kind `30023`, [NIP-33](/en/topics/nip-33/) parametrisierbare ersetzbare Events mit `d`-Tag-basierter Ersetzung sowie [NIP-01](/de/topics/nip-01/)/[NIP-02](/en/topics/nip-02/) Textnotizen mit kind `1` und Follow-Listen mit kind `3` hinzu. Der Release fügt außerdem ein adaptives IDE-Theme-System mit 54 Themes, UX-Politur für Workflow- und Agent-Run-Historie sowie eine Bereinigung der Mitglieder-Sidebar hinzu.

### mesh-llm v0.56.0 liefert verteiltes Config-Protokoll aus

[mesh-llm](https://github.com/michaelneale/mesh-llm), ein verteiltes LLM-Inferenzsystem, das Nostr-Schlüsselpaare für Node-Identität nutzt, lieferte [v0.56.0](https://github.com/michaelneale/mesh-llm/releases/tag/v0.56.0) am 7. April aus. Der Release fügt ein verteiltes Config-Protokoll mit Ownership-Semantik, asymmetrische KV-Cache-Quantisierung mit Q8_0-Keys und Q4-Werten zur Reduzierung des Speicherverbrauchs, OS-Keychain-Speicherung für Identity-Keystores, flüssiges Chat-Streaming mit Message-Queueing sowie Fixes für Fullscreen-Layout und KV-Cache-Splitting mit Flash Attention hinzu.

### Nostr VPN liefert exit node-Support und Umbrel-Paketierung aus

[Nostr VPN](https://github.com/mmalmi/nostr-vpn), ein Peer-to-Peer-VPN, das Nostr-Relays für Signalisierung und WireGuard für verschlüsselte Tunnel nutzt, lieferte diese Woche sechs Releases von [v0.3.0](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.0) bis [v0.3.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.6) aus. Der v0.3.x-Zyklus fügt exit node-Support auf Windows und macOS hinzu, sodass Peers Internetverkehr durch andere Nodes im Netzwerk leiten können. Invite- und Alias-Propagation synchronisieren nun über Nostr, sodass Nutzer Netzwerkzugang teilen können, ohne sich außerhalb des Protokolls abzustimmen. Die Releases fügen Umbrel-Paketierung für Self-Hosting-Deployments, NAT-Punch-Through mit gemerkten öffentlichen Endpunkten, automatische Bereinigung veralteter exit nodes und eine veröffentlichte Protokollspezifikation hinzu. Das Projekt stabilisierte außerdem die Routenbehandlung auf macOS mit selbstheilenden Default Routes und Underlay-Reparatur und fügte einen Android-Build via Tauri hinzu. Builds sind für macOS, Apple Silicon und Intel, Linux, AppImage und .deb, Windows und Android verfügbar.

### Nymchat nimmt Marmot zurück und liefert erweiterte NIP-17-Gruppenchats aus

[Nymchat](https://github.com/Spl0itable/NYM), der MLS-fähige Chat-Client, lieferte 14 Releases von [v3.56.261](https://github.com/Spl0itable/NYM/releases/tag/3.56.261) bis [v3.58.274](https://github.com/Spl0itable/NYM/releases/tag/v3.58.274) aus. Die bedeutendste Änderung ist ein Protokollwechsel: [v3.57.261](https://github.com/Spl0itable/NYM/releases/tag/v3.57.261) fügte Marmot-MLS-Gruppenchats hinzu, aber [v3.58.268](https://github.com/Spl0itable/NYM/releases/tag/v3.58.268) kehrte zu [NIP-17](/de/topics/nip-17/) zurück, weil die Multi-Device-Unterstützung von Marmot noch nicht fertig ist, was Probleme bei der Synchronisierung des Gruppenchatzustands über Geräte hinweg verursachte. v3.58.271 führt erweiterte NIP-17-Gruppenchats mit rotierenden ephemeral keys für alle Nachrichten ein, die Timing- und Korrelationsangriffe verhindern sollen. Die Woche brachte außerdem ein Friends-System mit granularer Kontrolle über Einstellungen ([v3.58.262](https://github.com/Spl0itable/NYM/releases/tag/v3.58.262)), MLS-Gruppenchat-Nachrichtensynchronisierung in verschlüsselten App-Einstellungen und mehrere Fixes für Relay-Konnektivität.

### nak v0.19.5 fügt Blossom-Multi-Server und Outbox-Publishing hinzu

[nak](https://github.com/fiatjaf/nak), fiatjafs Kommandozeilen-Nostr-Toolkit, lieferte [v0.19.5](https://github.com/fiatjaf/nak/releases/tag/v0.19.5) aus. Der `blossom`-Befehl akzeptiert nun mehrere `--server`-Flags, um in einem Aufruf auf mehrere [Blossom](/de/topics/blossom/)-Server hochzuladen. Ein neuer `key`-Befehl erweitert partielle Schlüssel durch Linkspadding mit Nullen. Der `event`-Befehl erhält ein `--outbox`-Flag zum Veröffentlichen von Events über das Outbox-Modell, und `fetch` beendet sich nun mit einem Fehlercode, wenn kein Event zurückgegeben wird.

## In Entwicklung

### White Noise fügt thumbhash-Vorschauen und Push-Registration-Bridge hinzu

[White Noise](https://github.com/marmot-protocol/whitenoise), der private Messenger auf Basis des [Marmot](/de/topics/marmot/)-Protokolls, mergte fünf PRs. [PR #549](https://github.com/marmot-protocol/whitenoise/pull/549) ersetzt blurhash-Bildvorschauen durch thumbhash, einen neueren Algorithmus, der schärfere Platzhalterbilder mit kleinerer Payload-Größe erzeugt, typischerweise unter 30 Byte statt blurhashs etwa 50 bis 100 Byte, und dabei Seitenverhältnis und Farbverteilung des Originalbilds bewahrt. Blurhash bleibt als Fallback für ältere Inhalte erhalten. [PR #548](https://github.com/marmot-protocol/whitenoise/pull/548) aktualisiert whitenoise-rs und fügt die [MIP-05](/de/topics/mip-05/) Push-Registration-Bridge hinzu, die die [Push-Benachrichtigungsspezifikation der letzten Woche](/en/newsletters/2026-04-01-newsletter/#marmot-moves-keypackages-to-addressable-events-and-tightens-push-notifications) mit dem Client verbindet. [PR #493](https://github.com/marmot-protocol/whitenoise/pull/493) fügt cursor-basierte Pagination für Chat-Nachrichten hinzu und ersetzt die bisherige Ladestrategie durch einen scrollgesteuerten Ansatz.

### Route96 fügt dynamische Label-Konfiguration und Zero-Egress-Bereinigung hinzu

[Route96](https://github.com/v0l/route96), der [Blossom](/de/topics/blossom/)-Medienserver von v0l, mergte drei PRs. [PR #80](https://github.com/v0l/route96/pull/80) fügt dynamische Konfiguration des Label-Modells über die Admin-API hinzu, sodass Betreiber Content-Klassifizierungsmodelle ohne Neustart des Servers austauschen können. [PR #82](https://github.com/v0l/route96/pull/82) fügt Felder zur Label-Konfiguration der Admin-UI hinzu. [PR #79](https://github.com/v0l/route96/pull/79) fügt eine Zero-Egress-Dateibereinigungsrichtlinie hinzu, die Dateien, die nie heruntergeladen wurden, automatisch entfernt und so die Speicherkosten für Betreiber senkt.

### Snort liefert Sicherheitshärtung und DVM-Zahlungsrechnungen aus

[Snort](https://github.com/v0l/snort), der Web-Client, lieferte diese Woche zwei Releases zusammen mit einem umfassenden Sicherheitsaudit aus. Zu den Fixes gehören Schnorr-Signaturprüfung, Schutz vor Relay-Message-Forgery in [NIP-46](/de/topics/nip-46/), also vor Angriffen, bei denen kompromittierte Relays Signing-Anfragen einschleusen könnten, Verbesserungen bei der PIN-Verschlüsselung und die Entfernung des Vertrauens in NIP-26-Delegation. Performance-Gewinne kommen durch gebündelte Schnorr-Verifikation in WASM, lazy-geladene Routen, vorkompilierte Übersetzungen und den Wegfall doppelter Verifikation pro Event. [PR #618](https://github.com/v0l/snort/pull/618) fügt die Anzeige von zahlungspflichtigen Rechnungen für [NIP-90](/en/topics/nip-90/) (Data Vending Machine) kind `7000` hinzu, sodass Snort die Lightning-Rechnung direkt im Feed rendert, wenn eine DVM eine Zahlungsanforderung zurückgibt.

### Damus verbessert LMDB-Kompaktierung

[Damus](https://github.com/damus-io/damus), der iOS-Client, mergte [PR #3719](https://github.com/damus-io/damus/pull/3719), das automatische LMDB-Kompaktierung nach Zeitplan hinzufügt und damit verhindert, dass die lokale Datenbank unbegrenzt wächst. [PR #3663](https://github.com/damus-io/damus/pull/3663) verbessert die BlurOverlayView, sodass sie schützend statt kaputt wirkt.

### Captain's Log fügt Tag-Indizierung und Notiz-Sync hinzu

[Captain's Log](https://github.com/nodetec/captains-log) (Comet), das Nostr-native Langform-Schreibwerkzeug von Nodetec, mergte diese Woche vier PRs. [PR #156](https://github.com/nodetec/captains-log/pull/156) fügt Tag-Indizierung und Sync-Unterstützung über Notizen hinweg hinzu, [PR #157](https://github.com/nodetec/captains-log/pull/157) refaktoriert Notiz-Sync und Tag-Verarbeitung, und [PR #159](https://github.com/nodetec/captains-log/pull/159) behebt den Sync gelöschter Notizen, damit entfernte Notizen auf allen Geräten gelöscht bleiben.

### Relatr v0.2.x gestaltet das Plugin-System mit Nostr-nativem Validator-Marktplatz neu

[Relatr](https://github.com/ContextVM/relatr), eine [Web of Trust](/de/topics/web-of-trust/)-Scoring-Engine, die Vertrauensrankings aus Distanz im sozialen Graphen und konfigurierbaren Validatoren berechnet, lieferte die v0.2.x-Familie mit einer vollständigen Neugestaltung des Plugin-Systems aus. Validatoren werden nun in Elo geschrieben, einer portablen funktionalen Ausdruckssprache, die geforkt wurde, um mehrstufige, host-orchestrierte Fähigkeiten zu unterstützen, darunter Nostr-Abfragen, Social-Graph-Lookups und NIP-05-Auflösung. Plugins werden als Nostr-Events mit kind `765` veröffentlicht und machen die Distribution damit nativ für das Relay-Netzwerk. Ein neuer [Plugin-Marktplatz](https://relatr.net) erlaubt es Betreibern, Validatoren im Browser zu entdecken, zu installieren und zu gewichten, ergänzt durch eine CLI namens `relo` für lokales Authoring und Publishing. Die Architektur ist sandboxed: Plugins können nur Fähigkeiten aufrufen, die der Host ausdrücklich bereitstellt, sodass ein bösartiger Validator seinen definierten Scope nicht verlassen kann. Relatr-Instanzen lassen sich nun von der Website aus verwalten, mit voller Transparenz darüber, welche Plugins den Scoring-Algorithmus zusammensetzen und welches einzelne Gewicht sie haben.

### Shopstr verbessert Mobile-Navigation und Zugriffskontrolle

[Shopstr](https://github.com/shopstr-eng/shopstr), der Nostr-native Marktplatz für Kauf und Verkauf mit Bitcoin, pushte diese Woche 158 Commits über seine Haupt-App und das Begleitprojekt [Milk Market](https://github.com/shopstr-eng/milk-market). Zu den Fixes gehören Verbesserungen am Community-Layout auf Mobilgeräten, das Schließen von Menüs bei Navigation und automatisches Schließen von Dropdowns. Geschützte Routen lassen sich nicht mehr per direkter URL ohne Anmeldung aufrufen, und die Slug-Matching-Logik behandelt mehrere exakte Treffer nun korrekt.

### Pollerama fügt Benachrichtigungen, Filmsuche und Rating-UI hinzu

[Pollerama](https://github.com/formstr-hq/nostr-polls), eine auf Nostr basierende Umfrage-, Survey- und Social-Rating-App, fügte Thread-Benachrichtigungen, eine Filmsuche und eine überarbeitete Rating-UI hinzu. Der Release behebt außerdem Ladeprobleme im Feed und hebt Abhängigkeitsversionen an.

### Purser baut Nostr-nativen Zahlungs-Daemon mit Marmot-Verschlüsselung

[Purser](https://github.com/EthnTuttle/purser), ein Nostr-nativer Zahlungs-Daemon als Ersatz für Zaprite, mergte diese Woche neun PRs zum Ausbau seiner Kernarchitektur. Das Projekt nutzt [Marmot](/de/topics/marmot/) MLS über MDK für verschlüsselte Händler-Kunden-Kommunikation, mit Strike und Square als Zahlungsanbietern. Diese Woche landeten Konfigurations- und Katalogladen, Message-Schema-Validierung, die MDK-Kommunikationsschicht, Implementierungen für Strike und Square, eine Polling-Engine, Anti-Spam-Rate-Limiting, Persistenz ausstehender Zahlungen und die Order-Processing-Pipeline. Alle 99 Tests verwenden nun echte mdk-core-MLS-Operationen, nachdem das Team Mock-MLS zugunsten realer Verschlüsselung im lokalen Modus entfernt hat.

### Vector refaktoriert DM-Anhänge und fügt Profilbearbeitung hinzu

[Vector](https://github.com/VectorPrivacy/Vector), der mit Tauri gebaute datenschutzorientierte Nostr-Messenger, mergte [PR #55](https://github.com/VectorPrivacy/Vector/pull/55), das das Frontend refaktoriert. Entschlüsselung und Speichern von DM-Anhängen wurden in die vector-core-Bibliothek verschoben, und die App unterstützt nun Profilbearbeitung. Das Upload-Cancel-Flag ist jetzt korrekt durch TauriSendCallback verdrahtet, und ungenutzte Callbacks für Attachment-Vorschauen wurden entfernt.

## Protokoll- und Spezifikationsarbeit

### NIP-Updates

Aktuelle Änderungen am [NIPs-Repository](https://github.com/nostr-protocol/nips):

**Gemergt:**

- **[NIP-58](/de/topics/nip-58/) (Badges): Profile Badges wechseln zu kind 10008, Badge Sets zu kind 30008** ([PR #2276](https://github.com/nostr-protocol/nips/pull/2276)): Migriert Profile Badges von kind `30008` zu kind `10008`, also einem ersetzbaren Event, eines pro pubkey, und führt kind `30008` für Badge Sets ein. Zuvor nutzten Profile Badges denselben kind `30008` wie Badge-Definitionen und waren damit parametrisierbare ersetzbare Events mit einem `d`-Tag als Schlüssel. Der neue kind `10008` ist ein einfaches ersetzbares Event, eines pro pubkey, ohne benötigten `d`-Tag. Clients fragen damit ein einzelnes ersetzbares Event pro Nutzer ab, statt parametrisierbare ersetzbare Events zu scannen. Amethyst v1.07.3 liefert diese Migration bereits aus.

- **[NIP-34](/de/topics/nip-34/) (Git Stuff): Git-bezogene Follow-Listen hinzufügen** ([PR #2130](https://github.com/nostr-protocol/nips/pull/2130)): Fügt Konventionen für Follow-Listen zur Repository- und Issue-Verfolgung in NIP-34 hinzu. Nutzer veröffentlichen kind-`30000`-Follow-Sets mit `d`-Tags wie `git-repos` oder `git-issues`, die `a`-Tag-Referenzen auf Repositories enthalten, kind `30617`, die sie verfolgen möchten. Clients können diese Follow-Sets abonnieren, um Repository-Aktivität im Feed eines Nutzers anzuzeigen, ähnlich wie kind-`3`-Kontaktlisten für pubkeys funktionieren.

**Offene PRs und Diskussionen:**

- **NIP-AC: P2P Voice and Video Calls over WebRTC** ([PR #2301](https://github.com/nostr-protocol/nips/pull/2301)): Erweitert das ursprüngliche NIP-100, umgesetzt von 0xChat, um drei Änderungen: Migration auf [NIP-44](/de/topics/nip-44/)-Verschlüsselung, verpackt in [NIP-59](/de/topics/nip-59/) gift wraps, um Metadatenlecks zu eliminieren, einen spezifizierten WebRTC-Workflow für Sprach- und Videoanrufe, also Offer, Answer und ICE Candidates, und ein Mesh-Modell für Gruppenanrufe, bei dem jeder Peer eine direkte WebRTC-Verbindung zu jedem anderen Peer aufbaut. Die Spezifikation ist nicht abwärtskompatibel zu NIP-100. Amethyst baut bereits dagegen, mit einer Testsuite für die Call-State-Machine ([PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143)) und dem Handling veralteter Call Offers ([PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164)), die diese Woche landeten.

- **[NIP-340](/en/topics/nip-340/) (FROST Quorum)** ([PR #2299](https://github.com/nostr-protocol/nips/pull/2299)): Schlägt Konventionen für Threshold-Signing mit [FROST](/de/topics/frost/) (Flexible Round-Optimized Schnorr Threshold) auf Nostr vor. FROST erlaubt es einer Gruppe von Signern, gemeinsam eine Nostr-Identität zu kontrollieren, bei der beliebige t-von-n-Mitglieder Events signieren können, ohne den vollständigen privaten Schlüssel zu rekonstruieren. Das NIP definiert, wie Signing-Runden koordiniert, Key Shares verteilt und threshold-signierte Events veröffentlicht werden, aufbauend auf der Igloo-Signer-Arbeit aus dem [FROSTR-Projekt](/en/newsletters/2026-04-01-newsletter/#igloo-signer-11).

- **[NIP-5D](/en/topics/nip-5d/) (Nostr Web Applets)** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): Definiert ein `postMessage`-Protokoll für sandboxed Webanwendungen, sogenannte "napplets", die in iframes laufen und mit einer hostenden Anwendung, der "shell", kommunizieren. Die shell stellt dem napplet Nostr-Signing, Relay-Zugang und Nutzerkontext über eine strukturierte Message-API bereit, während die iframe-Sandbox direkten Zugriff auf Schlüssel verhindert. Das erweitert das Hosting-Modell für statische Websites aus [NIP-5A](/en/topics/nip-5a/) in Richtung interaktiver Anwendungen, die Nostr-Events lesen und schreiben können. Das NIP ist in aktiver Entwicklung und hat bereits eine funktionierende Runtime-Implementierung.

- **[NIP-5C](/en/topics/nip-5c/) (Scrolls)** ([PR #2281](https://github.com/nostr-protocol/nips/pull/2281)): Wurde gegenüber dem früheren Vorschlag NIP-A5 umbenannt. Definiert Konventionen für das Veröffentlichen und Entdecken von WebAssembly-Programmen auf Nostr. WASM-Binaries werden als Nostr-Events gespeichert, und Clients können sie in einer sandboxed Runtime herunterladen und ausführen. Eine [Demo-App](https://nprogram.netlify.app/) zeigt Scrolls, die im Browser laufen, mit Beispielprogrammen, die als Nostr-Events veröffentlicht sind und von jedem Client geladen und ausgeführt werden können.

- **[NIP-85](/de/topics/nip-85/) (Trusted Assertions): Klarstellungen** ([PR #2304](https://github.com/nostr-protocol/nips/pull/2304)): Präzisiert die Spezifikationssprache rund um mehrere Schlüssel und Relays pro Service-Provider und klärt, wie Clients mit Assertions von Anbietern umgehen sollten, die über mehrere pubkeys oder Relay-Endpunkte arbeiten.

- **[NIP-24](/de/topics/nip-24/) (Extra Metadata Fields): `published_at` für ersetzbare Events** ([PR #2300](https://github.com/nostr-protocol/nips/pull/2300)): Verallgemeinert den `published_at`-Tag aus [NIP-23](/en/topics/nip-23/) (Long-form Content) auf alle ersetzbaren und adressierbaren Events. Der Tag dient nur der Darstellung: Wenn `published_at` gleich `created_at` ist, zeigen Clients das Event als "created" zu diesem Zeitpunkt an, und wenn sie sich unterscheiden, weil das Event aktualisiert wurde, können Clients stattdessen "updated" anzeigen. Dadurch können Profile mit kind `0` ein "joined at"-Datum anzeigen, und andere ersetzbare Events behalten ihren ursprünglichen Veröffentlichungszeitpunkt über Updates hinweg. Ein komplementärer Vorschlag für [NIP-51](/de/topics/nip-51/) ([PR #2302](https://github.com/nostr-protocol/nips/pull/2302)) fügt denselben Tag zu Listen-Events hinzu.

- **[NIP-59](/de/topics/nip-59/) (Gift Wrap): Ephemeral gift wrap kind** ([PR #2245](https://github.com/nostr-protocol/nips/pull/2245)): Fügt kind `21059` als ephemeres Gegenstück zum bestehenden gift wrap mit kind `1059` hinzu. Ephemere Events, kinds `20000` bis `29999`, folgen der Semantik von [NIP-01](/de/topics/nip-01/): Relays müssen sie nicht speichern und können sie nach der Zustellung verwerfen. Dadurch können Anwendungen gift-wrapped Messages senden, die nach der Zustellung von Relays verschwinden, was die Speicheranforderungen für volumenstarke Nachrichten reduziert und dabei dasselbe Drei-Schichten-Verschlüsselungsmodell wie normale [NIP-17](/de/topics/nip-17/) DMs beibehält.

### OpenSats kündigt sechzehnte Welle von Nostr-Grants an

[OpenSats](https://opensats.org) kündigte am 8. April seine [sechzehnte Welle von Nostr-Grants](https://opensats.org/blog/sixteenth-wave-of-nostr-grants) an und finanziert damit vier Erstförderungen und eine Verlängerung. [Amethyst Desktop](https://github.com/vitorpamplona/amethyst/tree/main/desktopApp) erhält Förderung für den Contributor Robert Nagy, um auf Basis der [Quartz](/de/topics/quartz/)- und Commons-Module eine eigenständige Desktop-App zu bauen, die das Feature-Set des Android-Clients auf mausgesteuerte Oberflächen mit persistenten Relay-Verbindungen bringt. [Nostr Mail](https://github.com/nogringo/nostr-mail) erhält Förderung für den Bau eines vollständigen E-Mail-Systems auf Nostr unter Verwendung von kind-`1301`-Events, verpackt in [NIP-59](/de/topics/nip-59/) gift wraps, mit einem Flutter-Client und SMTP-Bridge-Servern für Gmail- und Outlook-Kompatibilität. [Nostrord](https://github.com/Nostrord/nostrord) erhält Förderung für einen Kotlin-Multiplatform-Gruppenclient auf Basis von [NIP-29](/en/topics/nip-29/) und Relay-basierten Gruppen, mit Discord-artigen Gruppenchats, Moderation und Threads. [Nurunuru](https://github.com/tami1A84/null--nostr) erhält Förderung für eine native iOS-Version des auf Japan fokussierten Nostr-Clients, modelliert an der vertrauten LINE-Oberfläche, mit passkey-basierter biometrischer Anmeldung für das Onboarding. HAMSTR erhielt eine Förderverlängerung, erstmals gefördert in der [elften Welle](https://opensats.org/blog/eleventh-wave-of-nostr-grants#hamstr).

## NIP Deep Dive: NIP-17 (Private Direct Messages)

[NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md) definiert den aktuellen Standard für private Direktnachrichten auf Nostr. Es ersetzt das ältere Schema [NIP-04](/de/topics/nip-04/) (Encrypted Direct Messages), das Metadaten leckte, also Absender, Empfänger und Zeitstempel waren auf Relays sichtbar, und eine schwächere Verschlüsselungskonstruktion nutzte. NIP-17 kombiniert [NIP-44](/de/topics/nip-44/) (Encrypted Payloads) für die Verschlüsselung mit [NIP-59](/de/topics/nip-59/) (Gift Wrap) für den Schutz von Metadaten und schafft damit ein Dreischichtensystem, in dem Relays nicht sehen können, wer mit wem spricht.

Das Protokoll verwendet drei ineinander verschachtelte Event-Kinds. Die innerste Schicht ist die eigentliche Nachricht, ein unsigniertes Event mit kind `14`:

```json
{
  "id": "a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744108800,
  "kind": 14,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef", "wss://inbox.example.com"],
    ["subject", "Project update"]
  ],
  "content": "The new relay config is deployed. Let me know if you see any issues.",
  "sig": ""
}
```

Das Event mit kind `14` ist absichtlich unsigniert, also mit leerem `sig`. Die Spezifikation beschreibt das als Deniability, aber in der Praxis ist dieser Schutz begrenzt. Das Siegel mit kind `13`, das das rumor umhüllt, ist mit dem echten Schlüssel des Absenders signiert. Ein Empfänger kann das signierte Siegel einem Dritten zeigen und damit beweisen, dass der Absender mit ihm kommuniziert hat, auch ohne den Nachrichteninhalt offenzulegen. Mit Zero-Knowledge-Proofs kann ein Empfänger sogar den exakten Nachrichteninhalt beweisen, ohne seinen eigenen privaten Schlüssel offenzulegen. Das unsignierte rumor ist wie ein unsignierter Brief in einem signierten Umschlag: Die Signatur auf dem Umschlag verbindet den Absender mit dem Inhalt. Echte Deniability würde symmetrische Authentifizierung erfordern, wie HMACs bei Signal, was mit Nostrs dezentralem Relay-Modell unvereinbar ist, weil Nachrichten selbstauthentifizierend sein müssen. Die eigentlichen Stärken von NIP-17 sind Privatsphäre bei Metadaten und Geheimhaltung des Inhalts, nicht Deniability.

Diese unsignierte Nachricht wird dann in ein Siegel mit kind `13` verpackt, das vom tatsächlichen Absender signiert und mit [NIP-44](/de/topics/nip-44/) für den Empfänger verschlüsselt wird:

```json
{
  "id": "b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744022400,
  "kind": 13,
  "tags": [],
  "content": "<nip44-encrypted kind 14 payload>",
  "sig": "e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4"
}
```

Das Siegel hat keine Tags, daher würde es selbst nach einer Entschlüsselung den Empfänger nicht offenlegen. Das Siegel ist mit dem echten Schlüssel des Absenders signiert, was dem Empfänger erlaubt, die Nachricht zu authentifizieren, indem er prüft, dass der `pubkey` des Siegels mit dem `pubkey` des inneren kind-`14`-Events übereinstimmt.

Das Siegel wird anschließend in ein gift wrap mit kind `1059` verpackt, signiert von einem zufälligen Wegwerf-Schlüssel und an den Empfänger adressiert:

```json
{
  "id": "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2",
  "pubkey": "9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba",
  "created_at": 1744065600,
  "kind": 1059,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef"]
  ],
  "content": "<nip44-encrypted kind 13 payload>",
  "sig": "fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210"
}
```

Der `pubkey` des gift wrap ist ein zufälliger Schlüssel, der nur für diese Nachricht erzeugt wurde, und `created_at` wird um bis zu zwei Tage in die Vergangenheit randomisiert. Das ist die äußerste Schicht, die Relays tatsächlich sehen: eine Nachricht von einem unbekannten pubkey an den Empfänger, mit einem Zeitstempel, der nicht widerspiegelt, wann die Nachricht tatsächlich gesendet wurde. Der randomisierte Zeitstempel schützt vor nachträglicher Analyse gespeicherter Events, aber ein Angreifer, der aktiv mit Relays verbunden ist, kann weiterhin beobachten, wann das gift wrap erstmals auftaucht, daher ist diese Verteidigung auf passive Beobachter beschränkt, die Relay-Daten später abfragen. Weil der pubkey zufällig und der Zeitstempel gefälscht ist, können Relays den echten Absender nicht bestimmen. Um die Nachricht zu lesen, entschlüsselt der Empfänger das gift wrap mit seinem eigenen Schlüssel und dem zufälligen pubkey, findet darin das Siegel, entschlüsselt das Siegel mit seinem eigenen Schlüssel und dem pubkey des Absenders aus dem Siegel und findet darin die Nachricht mit kind `14`.

NIP-17 bietet keine forward secrecy. Alle Nachrichten werden mit dem statischen Nostr-Schlüsselpaar verschlüsselt, über die Schlüsselableitung von NIP-44 aus den Schlüsseln von Absender und Empfänger. Wird ein privater Schlüssel kompromittiert, kann jede vergangene und zukünftige Nachricht entschlüsselt werden, die an diesen Schlüssel verschlüsselt wurde. Das ist ein bewusster Tradeoff: Weil die Verschlüsselung nur vom nsec abhängt, kann ein Nutzer, der seinen nsec sichert, seine gesamte Nachrichtenhistorie von jedem Relay wiederherstellen, das die gift wraps noch speichert. Protokolle wie MLS, wie es von [Marmot](/de/topics/marmot/) genutzt wird, bieten forward secrecy durch rotierendes Schlüsselmaterial, aber um den Preis von notwendiger State-Synchronisierung und der Unmöglichkeit, historische Nachrichten nach einer Schlüsselrotation wiederherzustellen.

NIP-17 definiert außerdem kind `15` für verschlüsselte Dateinachrichten. Dieser fügt die Tags `file-type`, `encryption-algorithm`, `decryption-key` und `decryption-nonce` hinzu, damit der Empfänger eine angehängte Datei entschlüsseln kann, die vor dem Upload auf einen Blossom-Server mit AES-GCM verschlüsselt wurde. kind `10050` wird genutzt, um die bevorzugte DM-Relay-Liste des Nutzers zu veröffentlichen, damit Absender wissen, wohin sie gift wraps zustellen sollen. Die Menge aus `pubkey`- und `p`-Tags in einer Nachricht definiert einen Chatraum, und das Hinzufügen oder Entfernen eines Teilnehmers erzeugt einen neuen Raum mit sauberer Historie.

Implementierungen decken die meisten großen Clients ab. [nospeak](https://github.com/psic4t/nospeak) nutzt NIP-17 für sämtliche Eins-zu-eins-Nachrichten. [Flotilla](https://gitea.coracle.social/coracle/flotilla) nutzt NIP-17 für seine Proof-of-Work-DMs. [Amethyst](https://github.com/vitorpamplona/amethyst), [Primal](https://github.com/PrimalHQ/primal-android-app), [Nostur](https://github.com/nostur-com/nostur-ios-public), [Damus](https://github.com/damus-io/damus), [noStrudel](https://github.com/hzrd149/nostrudel) und [Coracle](https://github.com/coracle-social/coracle) implementieren NIP-17 alle als ihr primäres DM-Protokoll. Die Spezifikation unterstützt auch verschwindende Nachrichten durch Setzen eines `expiration`-Tags im gift wrap.

## NIP Deep Dive: NIP-46 (Nostr Remote Signing)

[NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md) definiert ein Protokoll, das den privaten Schlüssel des Nutzers von der Client-Anwendung trennt. Statt einen nsec in eine Web-App einzufügen, betreibt der Nutzer einen Remote Signer, auch "bunker" genannt, der den privaten Schlüssel hält und über Nostr-Relays auf Signing-Anfragen antwortet. Der Client sieht den privaten Schlüssel nie. Das reduziert die Angriffsfläche: Ein kompromittierter Client kann Signaturen anfordern, den Schlüssel selbst aber nicht extrahieren.

Das Protokoll nutzt kind `24133` sowohl für Requests als auch für Responses, verschlüsselt mit [NIP-44](/de/topics/nip-44/) (Encrypted Payloads). Ein Client erzeugt für die Session ein Wegwerf-`client-keypair` und kommuniziert mit dem Remote Signer über NIP-44-verschlüsselte Nachrichten, die mit den pubkeys des jeweils anderen getaggt sind. Hier ist eine Signing-Anfrage von einem Client an einen Remote Signer:

```json
{
  "id": "aa11bb22cc33dd44ee55ff6677889900aabbccdd11223344556677889900aabb",
  "pubkey": "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86",
  "created_at": 1744108800,
  "kind": 24133,
  "tags": [
    ["p", "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52"]
  ],
  "content": "<nip44-encrypted JSON-RPC request>",
  "sig": "1122334455667788990011223344556677889900aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff0011223344556677"
}
```

Das verschlüsselte `content` enthält eine JSON-RPC-ähnliche Struktur:

```json
{
  "id": "random-request-id-1",
  "method": "sign_event",
  "params": ["{\"kind\":1,\"content\":\"Hello from remote signing\",\"tags\":[],\"created_at\":1744108800}"]
}
```

Der Remote Signer entschlüsselt die Anfrage, legt sie dem Nutzer zur Freigabe vor, oder genehmigt sie automatisch auf Basis konfigurierter Berechtigungen, signiert das Event mit dem privaten Schlüssel des Nutzers und gibt das signierte Event in einer Response zurück:

```json
{
  "id": "bb22cc33dd44ee55ff6677889900aabb11223344556677889900aabbccddeeff",
  "pubkey": "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52",
  "created_at": 1744108801,
  "kind": 24133,
  "tags": [
    ["p", "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86"]
  ],
  "content": "<nip44-encrypted JSON-RPC response>",
  "sig": "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
}
```

Verbindungen können von beiden Seiten initiiert werden. Ein Remote Signer stellt eine `bunker://`-URL bereit, die seinen pubkey und Relay-Informationen enthält. Ein Client stellt eine `nostrconnect://`-URL mit seinem Client-pubkey, Relays und einem Secret zur Verbindungsüberprüfung bereit. Der Parameter `secret` verhindert Connection-Spoofing: Nur die Partei, die die URL außerhalb des Protokolls erhalten hat, kann den Handshake abschließen.

Acht Methoden sind definiert: `connect` zum Aufbau der Session, `sign_event` zum Signieren von Events, `get_public_key` zum Abrufen des pubkeys des Nutzers, `ping` für Keepalive, `nip04_encrypt` und `nip04_decrypt` für Legacy-Verschlüsselung, `nip44_encrypt` und `nip44_decrypt` für aktuelle Verschlüsselung sowie `switch_relays` für Relay-Management. Relay-Migration wird vom Remote Signer behandelt, der die Verbindung im Lauf der Zeit auf neue Relays verschieben kann, ohne die Session zu unterbrechen.

Clients fordern beim Verbindungsaufbau spezifische Fähigkeiten über ein Berechtigungssystem an. Ein Berechtigungsstring wie `nip44_encrypt,sign_event:1,sign_event:14` fordert Zugriff auf NIP-44-Verschlüsselung und Signing-Rechte nur für Events mit kind `1` und kind `14` an. Der Remote Signer kann diese Berechtigungen akzeptieren, ablehnen oder verändern. Das bedeutet, dass ein Web-Client zum Lesen und Posten von Notizen vielleicht nur `sign_event:1` erhält, während ein DM-Client zusätzlich `sign_event:14` und `nip44_encrypt` bekommen kann.

[Amber](https://github.com/greenart7c3/Amber) implementiert NIP-46 auf Android, und [v6.0.0-pre1](#amber-v600-pre1-fügt-signing-keys-pro-verbindung-für-nip-46-hinzu) dieser Woche fügt signing keys pro Verbindung hinzu, um Clients voneinander zu isolieren. [nsec.app](https://github.com/nicktee/nsecapp), früher Nostr Connect, bietet einen webbasierten bunker. [nostr-tools](https://github.com/nbd-wtf/nostr-tools) enthält `BunkerSigner` für JavaScript-Clients, und [PR #530 der letzten Woche](/en/newsletters/2026-04-01-newsletter/#nostr-tools-adds-bunker-relay-control-and-fixes-nip-47-multi-relay-parsing) fügte `skipSwitchRelays` für manuelles Relay-Management hinzu. Das Protokoll unterstützt außerdem Auth-Challenges: Wenn ein Remote Signer zusätzliche Authentifizierung benötigt, also Passwort, Biometrie oder Hardware-Token, antwortet er mit einer `auth_url`, die der Client in einem Browser öffnet, damit der Nutzer den Vorgang abschließen kann.

---

Das war's für diese Woche. Baust du etwas oder hast Neuigkeiten zu teilen? Schreib uns eine DM auf Nostr oder finde uns auf [nostrcompass.org](https://nostrcompass.org).
