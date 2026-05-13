---
title: 'Nostr Compass #21'
date: 2026-05-06
publishDate: 2026-05-06
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-06-newsletter.md
translationDate: 2026-05-13
description: 'Marmot Protocol liefert MDK 0.8.0 mit MIP-05-Benachrichtigungs-Primitiven und adressierbaren Schlüsselpaketen; LaWallet NWC liefert v0.10.0 mit dem vollständigen Monorepo, Admin-Dashboard, End-User-Wallet und einem neuen LightningAddress-zu-NWCConnection-Schema; Amethyst Nests stabilisiert sich mit Relay-Keep-Alive, lebenszyklusbewussten Abonnements, JWT-Refresh-Audio-Kontinuität und sichtbaren Sprecher-Indikatoren; ngit liefert v2.4.2 und v2.4.3 zur Behebung von GRASP-Server-Erkennung und Multi-Remote-State-Event-Filterung; GRAIN v0.5.4 bringt Produktionshärtung; Mostro Core v0.10.1 folgt dem v0.10.0 P2P-Chat-Protokollmodul der letzten Woche mit PGP-signierten Release-Artefakten; Clave v0.2.0 führt Multi-Account-Unterstützung unter iOS ein; nostream fügt Marmot Protocol Relay-Unterstützung und NIP-25-Reaktionen hinzu; Sprout liefert Desktop v0.0.4 und v0.0.5 neben NIP-OA-Agent-Authentifizierung für NIP-43-Mitgliedschaft und einem ephemeren Pairing-Sidecar; Angor 0.2.21 liefert kompakte App-Flows; Routstrd integriert Hermes für Daemon-Clients; micro-vpn-ansible tritt dem verfolgten NIP-34-Repo-Set bei; NIP-Diskussionen zeigen einen brokerfreien Hashrate-Markt-Entwurf, einen Curated-Feeds-Vorschlag als einfachere Alternative zu DVM-Feeds, ein Profile-Colors-NIP und einen Namecoin-verankerten Identitätstrack. Zwei NIP-Tieftauchgänge behandeln NIP-34 (git stuff) und NIP-53 (Live Activities).'
---

Willkommen zurück bei Nostr Compass, Ihrem wöchentlichen Leitfaden zu Nostr.

**Diese Woche:** [Marmot Protocol](https://github.com/marmot-protocol) liefert [MDK 0.8.0](#mdk-080-fügt-mip-05-benachrichtigungs-primitive-und-adressierbare-schlüsselpakete-hinzu) mit den ersten MIP-05-Benachrichtigungs-Primitiven, adressierbaren [NIP-51 (Listen)](/de/topics/nip-51/)-Schlüsselpaketen und einem verschärften Sicherheitsreview. [LaWallet NWC](https://github.com/lawalletio/lawallet-nwc) liefert [v0.10.0](#lawallet-nwc-v0100-liefert-das-vollständige-monorepo-und-end-user-wallet) als größten Release seit der OpenSats-Finanzierung mit einem vollständigen Admin-Dashboard, End-User-Wallet, End-to-End-Aktivitätsprotokoll und einem neuen `LightningAddress 1→N`- und `NWCConnection`-Schema. [Amethyst](https://github.com/vitorpamplona/amethyst) bringt einen [Nests-Stabilitätssprint](#amethyst-stabilisiert-nests-mit-keep-alive-jwt-resilienz-und-lebenszyklus-abonnements) mit Audio-Gap-Beseitigung beim JWT-Refresh, lebenszyklusbewussten Schlüsseldatenabonnements, Relay-Keep-Alive-Wiederverbindung und einem animierten Sprecher-Teilnehmer-Indikator. [ngit](https://github.com/DanConwayDev/ngit-cli) liefert [v2.4.2](#ngit-v242-und-v243-beheben-grasp-server-erkennung-und-multi-remote-state-events) und [v2.4.3](#ngit-v242-und-v243-beheben-grasp-server-erkennung-und-multi-remote-state-events) zur Behebung der GRASP-Server-Erkennung bei PR-Einreichungen und der Multi-Remote-State-Event-Filterung. [GRAIN](https://github.com/0ceanSlim/grain) liefert [v0.5.4](#grain-v054-bringt-produktionshärtung-und-einen-stillen-datenverlust-fix) mit Produktionshärtung und einem stillen Datenverlust-Fix im Docker-Quickstart. [Mostro Core](https://github.com/MostroP2P/mostro-core) liefert [v0.10.1](#mostro-core-v0101-fügt-pgp-signierte-release-artefakte-hinzu) mit PGP-signierten Release-Artefakten als Nachfolger des v0.10.0 P2P-Chat-Protokollmoduls der letzten Woche. [Clave](https://github.com/clave-mobile) startet [v0.2.0](#clave-v020-startet-multi-account-unter-ios-mit-nip-46-nostr-connect-signierung) mit Multi-Account-Unterstützung unter iOS.

## Hauptgeschichten

### MDK 0.8.0 fügt MIP-05-Benachrichtigungs-Primitive und adressierbare Schlüsselpakete hinzu

[MDK](https://github.com/marmot-protocol/mdk), die Rust-Kernbibliothek für das [Marmot](/de/topics/marmot/)-Protokoll, lieferte [v0.8.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.8.0) am 4. Mai. Dieses Release bringt die ersten MIP-05-Benachrichtigungs-Bausteine, verschiebt MIP-00-Schlüsselpakete zu adressierbaren Events, damit das Schlüsselpaket eines Benutzers an Ort und Stelle ersetzt werden kann, verbessert die gemischte Versionskompatibilität der Gruppe, erweitert die UniFFI-Abdeckung für mobile Bindungen und verschärft Validierungspfade rund um Admin-Aktionen, Commits, Speicherung, Verschlüsselungsgrenzen und Replay-Behandlung. MIP-05-Primitive umfassen Blattindex-Helfer, die in [PR #235](https://github.com/marmot-protocol/mdk/pull/235) hinzugefügt wurden und nachgelagerten Clients genug Informationen geben, um pro-Empfänger-Push-Benachrichtigungen zu liefern, ohne die Gruppenstruktur preiszugeben. Operative Fixes landen ebenfalls: [PR #273](https://github.com/marmot-protocol/mdk/pull/273) stellt die mdk-core crates.io-Veröffentlichung wieder her, und [PR #269](https://github.com/marmot-protocol/mdk/pull/269) legt das test_util-Modul hinter einem `test-utils`-Cargo-Feature frei, damit externe Client-Suiten Marmots Test-Harness teilen können. Für Client-Teams ist die wichtigste praktische Änderung das adressierbare Schlüsselpaket: Die MIP-00-Ankündigung eines Benutzers ist jetzt ein Kind, das an Ort und Stelle ersetzt wird, sodass das Rotieren zu einem frischen Schlüsselpaket keine veralteten Events mehr über Relays verteilt.

### LaWallet NWC v0.10.0 liefert das vollständige Monorepo und End-User-Wallet

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc), die [NIP-47](/de/topics/nip-47/)-Nostr-Wallet-Connect-Implementierung des LaWallet-Teams, lieferte [v0.10.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v0.10.0) am 30. April. Dies ist der größte Release seit der OpenSats-Finanzierung des Projekts. Er liefert das vollständige Monorepo, das komplette Admin-Dashboard, ein End-User-Wallet, ein End-to-End-Aktivitätsprotokoll, dynamisches Branding und das neue `LightningAddress 1→N`- und `NWCConnection`-Schema, das pro-Adresse-NWC-Routing freischaltet, wo eine Lightning-Adresse an mehrere NWC-Verbindungen unter verschiedenen RBAC-Rollen weitergeleitet werden kann. Das benutzerorientierte Wallet, das in [PR #191](https://github.com/lawalletio/lawallet-nwc/pull/191) geliefert wurde, deckt Onboarding, Home, Senden/Empfangen, Scan, Währungen, einen Aktivitätsfeed und einen Offline-Cache ab. [PR #192](https://github.com/lawalletio/lawallet-nwc/pull/192) verbindet den First-Run-Flow mit confirm-root, Community-Auto-Import und Setup-now-CTAs. [PR #196](https://github.com/lawalletio/lawallet-nwc/pull/196) fügt eine Live-OpenAPI-3.1-Referenz hinzu, die durch Scalar mit rollenbasierter Zugriffskontrolldokumentation gerendert wird, und [PR #193](https://github.com/lawalletio/lawallet-nwc/pull/193) bringt vollständige JSDoc-Abdeckung für die öffentliche `lib/`-Oberfläche, damit Editor-Tooltips die Wallet-API korrekt bei Integrationsarbeiten anzeigen.

### Amethyst stabilisiert Nests mit Keep-Alive, JWT-Resilienz und Lebenszyklus-Abonnements

[Amethyst](https://github.com/vitorpamplona/amethyst), der funktionsreiche Android-Client, setzte die [NIP-53](/de/topics/nip-53/)-Nests-Audio-Raum-Arbeit aus Newsletter [#20](/de/newsletters/2026-04-29-newsletter/#amethyst-advances-nests-audio-rooms-with-moq-interop-testing) mit einem Stabilitätssprint fort, der sich auf die Fehlermodi konzentrierte, die Anrufe in der Produktion unterbrachen. Der Audio-Gap-Fix in [PR #2733](https://github.com/vitorpamplona/amethyst/pull/2733) überschneidet den neuen Anmeldeinformationserwerb mit dem aktiven Stream während des JWT-Refreshs, sodass der Hörer keinen Ausfall hört, wenn das Token rotiert. Ein neuer Keep-Alive-Mechanismus in [PR #2730](https://github.com/vitorpamplona/amethyst/pull/2730) verbindet getrennte Relays wieder, ohne eine manuelle Benutzeraktion zu erfordern, und [PR #2728](https://github.com/vitorpamplona/amethyst/pull/2728) ersetzt das Legacy-`KeyDataSourceSubscription` durch `LifecycleAwareKeyDataSourceSubscription`, das die Abonnementlebensdauer an den Android-Activity-Lebenszyklus bindet, damit Hintergrundtabs keine offenen Abonnements durchsickern lassen. Androids 12+ `ForegroundServiceStartNotAllowedException` wird jetzt über [PR #2727](https://github.com/vitorpamplona/amethyst/pull/2727) graceful behandelt, und [PR #2726](https://github.com/vitorpamplona/amethyst/pull/2726) fügt den lebenszyklusbewussten Abonnements eine Schonfrist hinzu, damit ein kurzes Ausschalten des Bildschirms den Anruf nicht abbricht. Hörer erhalten einen neuen visuellen Hinweis aus [PR #2724](https://github.com/vitorpamplona/amethyst/pull/2724), einen animierten Außenring-Indikator, der den sprechenden Teilnehmer in Multi-Sprecher-Sitzungen hervorhebt.

### ngit v2.4.2 und v2.4.3 beheben GRASP-Server-Erkennung und Multi-Remote-State-Events

[ngit](https://github.com/DanConwayDev/ngit-cli), das Kommandozeilen-Tool und `git`-Plugin für [NIP-34](/de/topics/nip-34/)-Kollaboration, lieferte [v2.4.2](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.2) am 28. April und [v2.4.3](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.3) am 1. Mai. v2.4.2 behebt einen URL-Normalisierungs-Mismatch, bei dem `repo_grasps` normalisierte Hostnamen hielt, aber der Vergleich gegen vollständige Clone-URLs gemacht wurde. Die leere Kandidatenserverliste bedeutete, dass jede PR-Einreichung stillschweigend auf den Fork-Erstellungspfad auf einem persönlichen GRASP-Server fiel, wenn der korrekte Pfad ein direkter Push zum eigenen GRASP-Server des Repositorys war. v2.4.3 behebt eine State-Event-Ambiguität, die auftrat, wenn ein Repository mehrere `nostr://`-Remotes mit demselben Bezeichner hat: Relays konnten State-Events zurückgeben, die von Maintainern des *anderen* Remotes erstellt wurden, und ohne Filterung gewann das neueste Event unabhängig vom Autor und zeigte Refs auf die falschen Commits. State-Event-Kandidaten in `run_list` werden jetzt auf Maintainer der Repo-Ankündigung des aktuellen Remotes gefiltert, damit der richtige State gewinnt.

### GRAIN v0.5.4 bringt Produktionshärtung und einen stillen Datenverlust-Fix

[GRAIN](https://github.com/0ceanSlim/grain), die Go-basierte Nostr-Relay- und Client-Bibliothek, lieferte [v0.5.4](https://github.com/0ceanSlim/grain/releases/tag/v0.5.4) am 30. April. Das Release fasst sechs akkumulierte Fixes seit v0.5.3 zusammen, darunter einen stillen Datenverlust-Bug im Docker-Quickstart, der zuvor Events bei Neustart des Containers verlor, einen Speicherschicht-Korrektheitsbug bei adressierbaren Event-Lesevorgängen, bei dem falsches Tag-Handling Event-Lesevorgänge nach dem Neustart unterbrach, und zwei Verbindungsverfolgungsbugs, die beim Debuggen der v0.5.0-zu-v0.5.3-Sperrkette aufgedeckt wurden. Das Produktionshärtungspaar, das v0.5.3 ursprünglich angestrebt hatte, ist jetzt vorhanden: ein Pro-IP-Ratenlimit und eine IP-Blacklist, beide konfigurierbar.

### Mostro Core v0.10.1 fügt PGP-signierte Release-Artefakte hinzu

[Mostro Core](https://github.com/MostroP2P/mostro-core), die Rust-Bibliothek für Peer-to-Peer-Funktionalität für den Mostro-Daemon und andere nachgelagerte Anwendungen, lieferte [v0.10.1](https://github.com/MostroP2P/mostro-core/releases/tag/v0.10.1) am 28. April als Nachfolger des [v0.10.0 P2P-Chat-Protokollmoduls der letzten Woche](/de/newsletters/2026-04-29-newsletter/#mostro-core-v0100-and-mostro-mobile-v125-adopt-nip-59-dual-key-gift-wrap). Das neue Release fügt PGP-signierte Release-Artefakte und einen `verify-release`-Flow hinzu, damit nachgelagerte Packager die Artefaktherkunft bestätigen können, bevor sie die Bibliothek vertreiben.

## Getaggte Releases

### Clave v0.2.0 startet Multi-Account unter iOS mit NIP-46 (Nostr Connect) Signierung

[Clave](https://github.com/clave-mobile), die iOS-[NIP-46](/de/topics/nip-46/)-Remote-Signierungsapp, die APNs für Push-Zustellung verwendet (behandelt in [#20](/de/newsletters/2026-04-29-newsletter/#clave-brings-nip-46-remote-signing-to-ios-via-apns)), lieferte [v0.2.0](https://github.com/clave-mobile/clave/releases) am 5. Mai. Das bisher größte Update führt Multi-Account-Unterstützung ein: Clave kann jetzt bis zu vier Accounts auf einem Gerät halten, mit einem Ein-Tipp-Wechsler und Pro-Account-Isolation. Die iOS-Klempner und das Entwicklermenü für Multi-Account landen in [PR #23](https://github.com/clave-mobile/clave/pull/23), und [PR #22](https://github.com/clave-mobile/clave/pull/22) fügt dem APNs-Payload ein `signer_pubkey`-Feld hinzu, damit das Gerät weiß, zu welchem Account eine Remote-Signierungsanfrage gehört. Aktivitätsdetails beschreiben jetzt, was signiert wurde, und verlinken auf `njump` ([PR #19](https://github.com/clave-mobile/clave/pull/19)). Der Cold-Start-Zustellungs-Bug, bei dem das APNs-Token registriert war, aber das iOS-Benachrichtigungscenter veraltete leere Slots hatte, die die Zustellung verhinderten, ist in [PR #16](https://github.com/clave-mobile/clave/pull/16) behoben.

### Wisp liefert v1.0.3 → v1.0.5 Stabilitätsarbeit

[Wisp](https://github.com/barrydeen/wisp), der Android-Client, der [in #20 aus der Beta graduierte](/de/newsletters/2026-04-29-newsletter/#wisp-v100-graduates-from-beta), lieferte [v1.0.3](https://github.com/barrydeen/wisp/releases/tag/v1.0.3), [v1.0.4](https://github.com/barrydeen/wisp/releases/tag/v1.0.4) und [v1.0.5](https://github.com/barrydeen/wisp/releases/tag/v1.0.5) am 4. Mai mit Stabilitätsarbeit. [PR #506](https://github.com/barrydeen/wisp/pull/506) fügt Thumbhash für verschwommene Bildvorschauen hinzu, während vollständige Medien laden, und [PR #514](https://github.com/barrydeen/wisp/pull/514) reduziert Ruckeln beim Wechsel der unteren Tabs. [PR #515](https://github.com/barrydeen/wisp/pull/515) reduziert Start- und Feed-Rendering-Arbeit, und [PR #516](https://github.com/barrydeen/wisp/pull/516) verhindert, dass die App beim Wechsel der unteren Navigation veraltete Tab-Back-Stacks wiederherstellt.

### Amber 6.1.0-pre1 liefert Layout- und Stabilitätsfixes

[Amber](https://github.com/greenart7c3/Amber), die Android-Signer-App für [NIP-55 (Android Signer Application)](/de/topics/nip-55/) und [NIP-46](/de/topics/nip-46/), lieferte [v6.1.0-pre1](https://github.com/greenart7c3/Amber/releases) mit einem Layout-Pass beim neuen App-Verbindungsflow und mehreren gemeldeten Crash-Fixes. [PR #416](https://github.com/greenart7c3/Amber/pull/416) behebt `ActivityStatsBar`-Layout- und Textüberlaufprobleme, [PR #412](https://github.com/greenart7c3/Amber/pull/412) verbessert die Benachrichtigungsberechtigungsbehandlung und Fehlerresilienz, und [PR #411](https://github.com/greenart7c3/Amber/pull/411) stellt sicher, dass `SignerActivity` nach der Behandlung einer Anfrage immer schließt.

### Routstr Core v0.4.3 verbessert Zahlung, Rückerstattung und Nutzungsberichte

[Routstr Core](https://github.com/Routstr/routstr-core), die dezentrale Inferenzschicht, lieferte [v0.4.3](https://github.com/Routstr/routstr-core/releases) als Pre-Release am 1. Mai. Das Release verbessert Zahlungs- und Rückerstattungshandling, schärft Kostenverfolgung und Nutzungsberichte und liefert mehrere Fixes rund um API-Key-Anzeige, Nachrichtenhandling und Modellvalidierung.

### Nostria v3.1.37 bis v3.1.41 fügen Web-Lesezeichen und ein Auto-Theme hinzu

[Nostria](https://github.com/nostria-app/nostria), der Multi-Plattform-Nostr-Client, lieferte [v3.1.37 bis v3.1.41](https://github.com/nostria-app/nostria/releases) am 30. April und 4. Mai. Die Releases fügen [NIP-B0 (Web Bookmarks)](/de/topics/nip-b0/)-Unterstützung, ein "Auto"-Theme, das den Geräteeinstellungen folgt, In-App-PDF-Ansicht, Layout-Fixes für den Mediaplayer im Vollbildmodus und einen verbesserten Artikel- und Notizeditor hinzu.

### NoorNote v0.8.9 behebt leeren Startbildschirm auf Desktop

[NoorNote](https://github.com/77elements/noornote), der plattformübergreifende Nostr-Client, lieferte [v0.8.9](https://github.com/77elements/noornote/releases/tag/v0.8.9) am 28. April und behebt einen Leerbildschirm-Bug beim ersten Start der Desktop-App, bei dem der Willkommens- und Anmeldebildschirm nicht gerendert wurde.

### Kubo v0.3.4 bis v0.4.1 liefert eine kindersichere Nostr-Videoplattform mit elterlicher Kontrolle und Web-of-Trust-Feed-Kuration

[Kubo](https://github.com/JeroenOnNostr/kubo), eine kindersichere Videoplattform auf Nostr, die Eltern ermöglicht, die Inhaltswelt ihres Kindes durch Web-of-Trust-Filter zu kuratieren, lieferte [v0.3.4](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v0.3.4), [v0.3.5](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v0.3.5), [v0.4.0](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v0.4.0) und [v0.4.1](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v0.4.1) am 4. und 5. Mai. Die Plattform ist ein Soft-Fork von [Ditto](https://github.com/soapbox-pub/ditto), der für den Familien-und-Kinder-Anwendungsfall umbenannt wurde. Jedes Kind erhält ein separates Nostr-Schlüsselpaar und einen videozentrierten Feed, wo Eltern Zeitlimits (15 bis 180 Minuten täglich), erlaubte Zeitfenster und andere Aspekte der Feed-Steuerung kontrollieren.

## Nicht veröffentlichte Änderungen

### Sprout liefert Desktop v0.0.4 und v0.0.5 neben NIP-OA-Agent-Authentifizierung und dem Pair-Relay-Sidecar

[Sprout](https://github.com/block/sprout), Blocks Nostr-Client mit eingebautem Relay, lieferte [Sprout Desktop v0.0.4](https://github.com/block/sprout/releases) am 5. Mai und [v0.0.5](https://github.com/block/sprout/releases) am 6. Mai, neben ungefähr 80 zusammengeführten PRs, die einen großen NIP-OA-, NIP-43- und NIP-AB-Pairing-Pass abdecken. Die Hauptänderung in [PR #471](https://github.com/block/sprout/pull/471) verbindet NIP-OA-Agent-Authentifizierung mit dem NIP-43-Mitgliedschaftsflow des Relays über WebSocket-, REST- und Git-Transporte, sodass ein autonomer Agent beweisen kann, dass ein bestimmter menschlicher Pubkey seine Aktionen autorisiert hat, bevor das Relay Zugang gewährt. Ein neues ephemeres Sidecar-Relay für NIP-AB-Gerätepairing kommt in [PR #467](https://github.com/block/sprout/pull/467) als `sprout-pair-relay`.

### nostream fügt Marmot-Relay-Unterstützung und NIP-25-Reaktionen hinzu

[nostream](https://github.com/Cameri/nostream), die Node.js-Relay-Implementierung, fusionierte eine produktive Woche von Protokollzusätzen. Marmot Protocol Relay-Unterstützung für MIPs 00 bis 03 landet in [PR #602](https://github.com/Cameri/nostream/pull/602). Die kleineren Protokollzusätze: [NIP-25](/de/topics/nip-25/)-Reaktionsunterstützung in [PR #589](https://github.com/Cameri/nostream/pull/589), Geohash-Präfix-Matching für `#g`-Filter in [PR #586](https://github.com/Cameri/nostream/pull/586) und eine verschärfte `maxlimit`-Prüfung für Abonnement-Event-Anfragen in [PR #600](https://github.com/Cameri/nostream/pull/600).

### strfry fügt Pro-Verbindungs-Observierbarkeit hinzu und reduziert nofiles-Decke

[strfry](https://github.com/hoytech/strfry), das C++-Nostr-Relay, fusionierte 14 PRs, die auf Observierbarkeit und operative Hygiene abzielen. Die Hauptänderung ist [PR #218](https://github.com/hoytech/strfry/pull/218), das Pro-Verbindungs-ausstehende Ausgangs-Observierbarkeit und eine konfigurierbare Backpressure-Kappe hinzufügt. Auf der Performance-Seite entfernt [PR #224](https://github.com/hoytech/strfry/pull/224) `std::function`-Heap-Allokationen aus dem Pro-Event-Monitor-Fanout.

### Damus ersetzt Tenor GIFs durch einen Purple-Proxy und liefert Kompaktierungs-UX

[Damus](https://github.com/damus-io/damus), der iOS-Nostr-Client, fusionierte [PR #3737](https://github.com/damus-io/damus/pull/3737), der die Tenor-GIF-Integration durch einen [Damus Purple](https://damus.io/purple/)-Proxy ersetzt, bei dem Damus' gehosteter Abonnementdienst GIF-Anfragen im Namen des Clients weiterleitet.

### Primal Android poliert Explore, Benachrichtigungen und das NIP-05-Verifizierungsabzeichen

[Primal Android](https://github.com/PrimalHQ/primal-android-app) fusionierte [PR #1043](https://github.com/PrimalHQ/primal-android-app/pull/1043), der ein flackerndes [NIP-05 (Domain-Verifizierung)](/de/topics/nip-05/)-Verifizierungsabzeichen für Benutzer mit `_@domain`-Bezeichnern behebt.

### Alby Hub fügt NWC-Zahlungen von App-Verbindungen hinzu

[Alby Hub](https://github.com/getAlby/hub) fusionierte [PR #2267](https://github.com/getAlby/hub/pull/2267), der Zahlungen von App-Verbindungen erlaubt, und [PR #2268](https://github.com/getAlby/hub/pull/2268), der die Onchain-Empfangsrouting-Logik vereinfacht, beide über Alby Hubs [NIP-47 (Nostr Wallet Connect)](/de/topics/nip-47/)-Oberfläche geliefert.

### routstrd-auth: ein dockerisierter Routstrd für Teams mit NIP-98-Auth und npub-RBAC

[routstrd-auth](https://github.com/Routstr/routstrd-auth), am 27. April vom Routstr-Team erstellt, ist eine dockerisierte Variante von Routstrd für Multi-User-Team-Deployments. Die Hauptänderung ist ein granulares npub-basiertes rollenbasiertes Zugriffskontrollsystem mit `admin`- und `user`-Rollen und Client-Endpunkten, die [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md)-HTTP-Authentifizierung mit Eigentumsnahverfolgung übernehmen.

### Routstrd integriert Hermes für Daemon-Clients und Remote-Modus

[Routstrd](https://github.com/routstr/routstrd), der lokale Daemon, der Routstr-Inferenz-Clients orchestriert, fusionierte [PR #22](https://github.com/routstr/routstrd/pull/22) und fügt Integration mit [Hermes Agent](https://github.com/NousResearch/hermes-agent) hinzu, sodass die Konfigurationsdatei des Agents mit den Modellanbietern und API-Keys gefüllt wird, die Routstrd über Nostr entdeckt.

### diVine liefert NIP-07-Web-Anmeldung und 16-Locale-Schlüsselparität

[diVine](https://github.com/divinevideo/divine-mobile), der Video-Client, lieferte diese Woche zwei iOS-Releases neben 139 fusionierten PRs. [PR #3994](https://github.com/divinevideo/divine-mobile/pull/3994) fügt [NIP-07 (Browser-Extension-Signer)](/de/topics/nip-07/)-Anmeldung für den Web-Build hinzu, [PR #3992](https://github.com/divinevideo/divine-mobile/pull/3992) übersetzt 16 nicht-englische Locales auf vollständige Schlüsselparität.

### whitenoise-rs liefert Pro-Account-Datenbankirsolierung und Vorschlagsupgrades

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs), die Rust-Kernbibliothek für den White-Noise-Messenger, fusionierte [PR #796](https://github.com/marmot-protocol/whitenoise-rs/pull/796), das Nachrichtenprojektionstabellen in Pro-Account-Datenbanken verschiebt, und [PR #791](https://github.com/marmot-protocol/whitenoise-rs/pull/791), das Vorschlagsupgrades hinzufügt, damit Gruppen ihre Funktionalität mit neuen Vorschlagstypen erweitern können.

### Angor 0.2.21 liefert kompakte App-Flows neben Key-Provider- und Netzwerkwechsel-Härtung

[Angor](https://github.com/block-core/angor), die Bitcoin-Crowdfunding-Plattform mit Nostr-veröffentlichten Gründerprofilen, lieferte [Angor 0.2.21](https://github.com/block-core/angor/releases) am 6. Mai und fasst eine Woche mobiler und Integrationsarbeit zusammen.

## Neu verfolgt und entdeckt

### BitMacro Signer: ein selbst-hostbarer NIP-46-Bunker mit clientseitiger Schlüsselverschlüsselung

[BitMacro Signer](https://github.com/bitmacro/bitmacro-signer) ist ein selbst-hostbares Nostr-Signing-Tool, das private Schlüssel mit dem [NIP-46](/de/topics/nip-46/)-Bunker-Modell verwaltet. Der Signer verschlüsselt Schlüssel auf dem Client vor der Speicherung, sodass die Serverseite niemals Klartext hält.

Die NIP-34-Repo-Entdeckung dieser Woche brachte 26 neue Repository-Ankündigungen hervor, von denen vier herausragen.

### gnostr: eine Git-Implementierung direkt auf Nostr aufgebaut

[gnostr](https://github.com/gnostr-org/gnostr) ist eine Git-Implementierung, die direkt auf Nostr aufgebaut ist und sich von `git-remote-nostr` dadurch unterscheidet, dass sie eigene Working-Tree-Befehle als von Grund auf native Nostr-Versionskontroll-Client liefert.

### nostr-archive: eine inhaltsadressierte Archivspezifikation auf Nostr und Blossom

[nostr-archive](https://gitworkshop.dev/nostr-archive/nostr-archive) ist eine Entwurfsspezifikation und Referenzimplementierung für inhaltsadressierte Archive auf Nostr und Blossom.

### flower-cache: ein lokaler Blossom-Cache-Server

[flower-cache](https://gitworkshop.dev/flower-cache/flower-cache) ist ein lokaler Blossom-Cache-Server, nützlich für Clients, die einen heißen lokalen Spiegel eines Remote-Blossom-Server-Blob-Sets ohne Round-Trip zum Upstream wünschen.

### micro-vpn-ansible: Ansible-Playbooks für VPN-Deployment über NIP-34

[micro-vpn-ansible](https://gitworkshop.dev/npub1mu9fsh42uh48trncevdpju8cyv3mxmj9qj3rdjqc46zc324c6hys9ctsnc/relay.ngit.dev/micro-vpn-ansible) ist eine kleine Ansible-Playbook-Sammlung für das Deployment eines Micro-VPN, gehostet als NIP-34-Repository.

## Protokollarbeit

### NIP-Updates

- **Ein brokerfreier Hashrate-Markt über Nostr** ([Entwurfsvorschlag](https://njump.me/nevent1qqsqd2478wqugjh9ur9lenw9la0wd987h6jcc0tma4kkuat4xceymvszypxxmj0zcqtwqm34f48gzulrg99daaczllhtqun7xsldkh8neua2jhr32rf)): Anonymer NIP-Entwurf aus einem Nostr-Langformbeitrag, der argumentiert, dass die aktuellen Hashrate-Marktakteure (Braiins, Nicehash, Mining Rig Rentals) alle verwahrende Broker sind, die Benutzer KYC unterziehen. Der Vorschlag skizziert einen Peer-to-Peer-Hashrate-Markt auf Nostr-Events.
- **Curated Feeds: eine einfachere Alternative zu DVM-Feeds** ([Entwurfsvorschlag](https://njump.me/nevent1qqsqj55kvu28uyq2jr6nfwx20mv7c0vkm0vxkgx0zzrnanfp4wwv8nczyzm7669svt0xkjsju50a22zurc0qa589z2xd4yatzx6p2z64a5e0cyxz3e3)): Ein Entwurf argumentiert, dass [NIP-90](/de/topics/nip-90/) Data Vending Machines als allgemeiner Rechenmarktplatz konzipiert wurden und das Anfrage/Antwort-Modell schwerer ist als notwendig, wenn ein Client nur eine adressierbare Liste von Event-IDs möchte.
- **Profile Colors: deterministische visuelle Identität** ([Entwurfsvorschlag](https://njump.me/nevent1qqsy3tj7mn3r7wczmc52aknf5ym43lj3rrhd3sfprzvc6qydsq62wrgzyzjk8j56zmt5fwv088l5y84hqq4gags3grvuznlu4zmyt54w34cccyxenp3)): Ein neues NIP-Entwurf zur Ableitung deterministischer, lesbarer Farben aus einem Nostr-Pubkey für konsistente visuelle Identität über Clients hinweg.
- **Namecoin-Track NIPs: Verankern von Identität, Relays, TLS und Reputation** ([Entwurfscluster](https://njump.me/nevent1qqsydpjnaj2netmv0h5mlm2j6zpk8u50yvc9pqth3ly8pzuwy22720szypp3shk7edn43y5zfvdr0ftl8eq8l00zaknjqx3c9xuv7ja8ck60q7uupzs)): Ein trennbarer Cluster von NIP-Entwürfen, der Teile des bestehenden Nostr-Stacks in Namecoin-verankerte Records verschiebt.

## NIP-Tieftauchgang: NIP-34 (git stuff)

[NIP-34](/de/topics/nip-34/) definiert Event-Kinds für das Hosting von Git-Repositories, Patches, Pull-Requests, Issues und Merge-Status auf Nostr-Relays. Es ist der Standard, der Nostr zu einer Koordinationsschicht für Code-Kollaboration macht: Die Repository-Daten leben weiterhin auf einem Git-Server (GitHub, eine selbst-gehostete Forge oder ein GRASP-Server), während Ankündigungs-Events, Patches, PRs, Issues und Status-Updates auf Relays laufen.

Ein Repository wird als kind-`30617`-adressierbares Event angekündigt, dessen `d`-Tag ein Kebab-Case-Bezeichner (typischerweise der Projektname) ist und dessen Body `name`, `description`, eine oder mehrere `clone`-URLs, optionale `web`-URLs, einen `relays`-Tag mit Relays, die der Maintainer überwacht, und einen `maintainers`-Tag mit zusätzlichen Pubkeys zur Verwaltung des Projekts enthält.

Patches verwenden kind `1617` und tragen `git format-patch`-Ausgabe im Content-Body. Pull-Requests verwenden kind `1618` und sind für Changesets größer als 60 KB gedacht. Issues verwenden kind `1621` mit Markdown-Inhalt. Status-Events verschieben einen Thread zwischen Open (`1630`), Applied/Merged oder Resolved (`1631`), Closed (`1632`) und Draft (`1633`).

Die NIP-34-Geschichte dieser Woche ist dieselbe wie die [GitWorkshop-v2-Einführung der letzten Woche](/de/newsletters/2026-04-29-newsletter/#gitworkshop-ships-in-browser-pr-merge-repository-following-and-a-bandwidth-efficient-git-explorer): Der In-Browser-PR-Merge-Button funktioniert, weil GRASP-Server, ngit und das `nostr://`-Clone-URL-Schema zusammen die Schleife einer vollständig dezentralisierten Forge schließen.

## NIP-Tieftauchgang: NIP-53 (Live Activities)

[NIP-53](/de/topics/nip-53/) definiert die Standardereignisoberfläche für Live-Aktivitäten auf Nostr: Live-Streams, persistente Meeting-Räume, geplante Konferenzereignisse, Hörer-Präsenz und den Live-Chat-Kanal, der Chat-Nachrichten an einen bestimmten Live-Aktivitätsdatensatz bindet.

Ein Live-Stream wird als kind-`30311`-adressierbares Event angekündigt. Sein `d`-Tag ist der stabile Bezeichner, der `streaming`-Tag zeigt auf die Wiedergabe-URL, und der `status`-Tag trägt einen von `planned`, `live` oder `ended`. NIP-53 trennt den persistenten Raum vom geplanten Event, das darin stattfindet. Eine kind-`30312`-Meeting-Space definiert einen Raum, und ein kind-`30313`-Konferenz-Event repräsentiert ein geplantes oder laufendes Meeting in diesem Raum.

Der Nostr-Live-Aktivitäts-Stack ist absichtlich dünn: NIP-53 kündigt die Aktivität an, während andere NIPs angrenzende Belange handhaben. Zaps für Live-Streams verwenden [NIP-57 (Zaps)](/de/topics/nip-57/)-Zap-Quittungen, Spendensammelziele verwenden [NIP-75 (Zap Goals)](/de/topics/nip-75/)-Zap-Ziele, und Videoaufzeichnungen können als [NIP-71 (Video Events)](/de/topics/nip-71/)-Video-Events erneut veröffentlicht werden.

---

Das war es für diese Woche. Wenn du etwas baust oder Neuigkeiten zu teilen hast, sende uns eine DM auf Nostr oder finde uns auf [nostrcompass.org](https://nostrcompass.org).
