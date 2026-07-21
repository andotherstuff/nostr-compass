---
title: "Nostr Compass #31"
date: 2026-07-15
publishDate: 2026-07-15
translationOf: /en/newsletters/2026-07-15-newsletter.md
translationDate: 2026-07-15
draft: false
type: newsletters
description: "Vector v0.4.0 ersetzt Marmot für Gruppen-Chats durch das offene Concord-Protokoll und liefert Concord v2 Tage später, Amethyst mergt eine eigene Clean-Room-Concord-Implementierung, Sonar spaltet sich von Bitchat ab mit einer plattformübergreifenden Alpha und einer Sticker-Pack-Spezifikation, Divine Mobile 1.0.16 bringt At-Rest-Verschlüsselung und ProofMode-Provenienz, Bitchat 1.7.0 fügt Live-Push-to-Talk-Sprachübertragung hinzu, und MDK v0.9.4 begrenzt External-Signer-Login."
---

Willkommen zurück bei Nostr Compass, eurem wöchentlichen Wegweiser für Nostr.

**Diese Woche:** [Vector v0.4.0](#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later) ersetzt [Marmot](/de/topics/marmot/) als Standard-Transport für Group Chats zugunsten von [Concord](/de/topics/concord-protocol/), einem offenen, MIT-lizenzierten Community-Protokoll, das auch von Soapbox' Armada verwendet wird, und liefert vier Tage später Concord v2 mit einem Slash-Command-Picker für Bots, einem Selbstzerstörungs-Timer und NIP-58-Badges. [Amethyst mergt seine eigene Clean-Room-, drahtkompatible Concord-Implementierung](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities) in derselben Woche. [Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec) spaltet sich von Bitchat ab mit einer plattformübergreifenden Alpha und ist die zitierte Spezifikationsquelle für den Sticker-Pack-Kinds-Vorschlag dieser Woche. [Divine Mobile 1.0.16](#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance) liefert einen tieferen Video-Editor, At-Rest-Verschlüsselung und ProofMode-Provenienz, die wasserzeichenmarkierte Clip-Downloads überlebt. [Bitchat v1.7.0](#bitchat-v170-adds-live-push-to-talk-voice-for-dms-and-the-public-mesh) fügt Live-Push-to-Talk-Sprachübertragung für DMs und signiertes Push-to-Talk auf dem öffentlichen Mesh hinzu. [MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence) begrenzt External-Signer-Login und fügt Draft-Persistenz hinzu, während Vector in derselben Woche die Spezifikation für Gruppen-Chat verlässt.

Getaggte Releases bringen [n_cord v1.1](#n_cord-v11-adds-nsec-bunker-support) mit NSEC-Bunker-Unterstützung, [cdk v0.17.3](#cdk-v0173-adds-nip-47-wallet-service-support-across-cdk-cdk-nwc-and-cdk-ffi) mit NIP-47-Wallet-Service-Unterstützung über cdk, cdk-nwc und cdk-ffi, [Coop Mobile v0.2.4](#coop-mobile-v024-improves-nostr-connect-and-adds-ncryptsec1-import) mit verbessertem Nostr Connect und ncryptsec1-Import, [Nmail v0.14.0](#nmail-v0140-ships-on-macos-with-scheduled-send-and-push-notifications) auf macOS mit geplantem Senden, [Nostrord v2.2.0](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages) mit einem DM-Master-Toggle, [Nostr WoT 0.3.86](#nostr-wot-0386-hardens-key-backups-and-signing-prompts) mit gehärteten Schlüssel-Backups im NIP-49-Format, [Keep Android v1.1.8](#keep-android-v118-adds-first-run-frost-onboarding) mit First-Run-FROST-Onboarding, [Noscall v0.6.0](#noscall-v060-adds-a-cashu-wallet-and-relay-based-push-notifications) mit einem Cashu-Wallet und relay-basierten Push-Benachrichtigungen, [Kubo](#kubo-ships-tablet-mode-and-group-chat-photos) mit Tablet-Modus und Gruppen-Chat-Fotos und [Nostr Codex Phone v0.2.9](#nostr-codex-phone-v029-adds-gitdiffread-file-helper-requests) mit git-, diff- und read-file-Helper-Requests.

Auf der unveröffentlichten Seite lässt [Amethyst](#amethyst-lets-accounts-nickname-contacts-with-encrypted-nip-85-cards) Accounts Kontakte mit verschlüsselten NIP-85-Karten benennen, über 54 gemergte PRs. [Zap Cooking](#zap-cooking-ships-my-kitchen-phase-3-and-fixes-an-ndk-pool-quorum-bug) liefert My Kitchen Phase 3 und behebt einen NDK-Pool-Quorum-Bug. [Kehto](#kehto-streams-outbox-reads-before-relay-discovery) streamt Outbox-Reads vor Abschluss der Relay Discovery. [Wired und TAO](#wired-and-tao-add-nip-57-creator-revenue-sharing) fügen NIP-57-Creator-Revenue-Sharing hinzu. [Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout) baut seinen Händler-Bestelleingang um ephemeres Guest Checkout um. [Buzz](#buzz-hardens-channel-creator-provisioning-around-kind-39002) härtet Channel-Creator-Provisioning über 240 gemergte PRs. Und [Nostr Docs](#nostr-docs-adopts-a-nip-49-signer-with-multi-account-and-qr-pairing) übernimmt einen NIP-49-Signer mit Multi-Account und QR-Pairing. Neu getrackt diese Woche: [OpenDiscord v1.0.1](#opendiscord-v101-launches-as-a-discord-style-client-on-nostr), [Auditable Voting v0.1.140](#auditable-voting-v01140-aligns-organiser-voter-and-audit-proxy-roles) und Discovery-Pick [Cambium v0.3.2](#cambium-v032-pairs-with-heartwood-as-a-keyless-nip-55-signer), ein schlüsselloser NIP-55-Signer, der an einen Heartwood-Hardware-Companion weiterleitet.

Das NIPs-Repository mergt in der letzten Woche nichts und öffnet sechs Vorschläge: [kind:10011 Favorite Follow Sets](#open-kind10011-favorite-follow-sets), ein [privates verschlüsseltes Laufwerk als Erweiterung von NIP-4E](#open-private-encrypted-drive-extends-nip-4e), [NIP-DA permissioned private data sharing](#open-nip-da-permissioned-private-data-sharing), [Sticker-Pack-Kinds 10031 und 30031](#open-sticker-pack-kinds-10031-and-30031), [NIP-29 Message Pinning](#open-nip-29-message-pinning-with-kind9010-and-kind39005) und eine [NIP-66-Relay-Discovery-Umstrukturierung](#open-nip-66-relay-discovery-restructure). Der Deep Dive behandelt [NIP-99 und die Gamma-Markets-Commerce-Erweiterung](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension).

---

## Leitgeschichten

### Vector v0.4.0 moves Group Chats from Marmot to Concord, and Amethyst ships its own Concord client days later

[Vector](https://github.com/VectorPrivacy/Vector) ist ein Nostr-Messenger, der auf einem Single-Binary-, datenschutzorientierten Client für DMs und Gruppen-Chats aufbaut. [Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) schreibt die Messaging-Engine der App in eine gemeinsame `vector-core`-Bibliothek um und ersetzt im selben Release [Marmot](/de/topics/marmot/) (MLS-over-Nostr) als Standard-Transport für Group Chats durch [Concord](/de/topics/concord-protocol/), ein Ende-zu-Ende-verschlüsseltes Community-Protokoll; bestehende Marmot-Gruppenverläufe werden nicht übernommen, und die Release Notes empfehlen, alle Marmot-Gruppendaten vor dem Upgrade zu sichern. Vectors eigene Release Notes beschreiben Concord als „our custom messaging protocol", aber die zugrunde liegenden [CORD-01- bis CORD-07-Spezifikationen](https://github.com/concord-protocol/concord) werden separat veröffentlicht, sind MIT-lizenziert und bereits außerhalb von Vector implementiert: Soapbox' Discord-artiger Client [Armada](https://gitlab.com/soapbox-pub/armada) baut sein Communities-Feature auf derselben Concord-Spezifikation auf, und einen Tag später [mergte Amethyst seine eigene Clean-Room-, drahtkompatible Concord-Implementierung](https://github.com/vitorpamplona/amethyst/pull/3566), die weiter unten vollständig behandelt wird. Dasselbe Vector-Release fügt optionales Tor-Routing für allen Datenverkehr, [NIP-46](/de/topics/nip-46/) Remote-Signer-Login per QR oder eingefügter Bunker-URI, mehrere Accounts mit einem In-App-Switcher und benutzerdefinierte Emoji-Packs hinzu, die clientübergreifend geteilt werden. Das Löschen von Nachrichten entfernt eine Nachricht für beide Seiten in DMs und Gruppen-Chats, und Vector behält bewusst den ephemeren Signaturschlüssel, anstatt dem Standard-[NIP-17](/de/topics/nip-17/)-Löschablauf zu folgen, eine datenschutzmotivierte Abweichung, die das Projekt explizit in den Release Notes hervorhebt. Vier Tage später liefert [v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1) **Concord v2**, das wichtige Datenschutz- und Stabilitätsverbesserungen für Communities bringt, bei gleichzeitiger Kompatibilität bestehender Communities, zusammen mit einem Discord-artigen Slash-Command-Picker für Bots mit typisierten Parametern, einem Pro-Chat-Selbstzerstörungs-Timer und einem NIP-58-Badge-System für Bug Hunter. Der Wechsel weg von Marmot für Gruppen-Chat erfolgt in derselben Woche, in der [MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence) unten weiterhin in die Spezifikation investiert.

### Amethyst ships a clean-room Concord implementation for end-to-end encrypted communities

[Amethyst](https://github.com/vitorpamplona/amethyst) ist ein funktionsreicher Android- und Multiplattform-Nostr-Client. [PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566) fügt eine vollständige Implementierung von [Concord](/de/topics/concord-protocol/) (CORD-01 bis CORD-07) hinzu, die serverlose, Ende-zu-Ende-verschlüsselte Communities abdeckt: Gift-Wrapped Control-, Chat- und Guestbook-Ebenen über gewöhnliche Relays, vom Eigentümer verwurzelte Rollen- und Ban-Durchsetzung, die jeder Client lokal verifiziert, anstatt einem Server zu vertrauen, und Rekeying zum Ausschluss entfernter Mitglieder. Protokoll- und Krypto-Code liegt in `quartz/`, State und View Models in `commons/`, und Screens und Navigation in `amethyst/` für Android, mit schlanken CLI-Verben unter `cli/`; es gibt noch keine Desktop-UI, da die gemeinsame Logik in `quartz`/`commons` liegt, damit Desktop sie später übernehmen kann. Die Implementierung ist Clean-Room: aus den öffentlichen CORD-Spezifikationen und beobachteten Wire-Konstanten gebaut, unter Amethysts eigener MIT-Lizenz, getrennt von Armadas AGPL-3.0-Codebasis. Armadas eigene Test-Vector-Werte wurden in Quartz' Unit-Tests portiert, um zu bestätigen, dass die beiden Clients tatsächlich auf der Leitung interoperieren, was Concord innerhalb von Tagen drei unabhängige Implementierungen gibt: Vector liefert zuerst, Armada als Soapbox' Referenz-Client, und nun Amethysts Aus-der-Spezifikation-Build.

### Sonar splits off from Bitchat with a cross-platform alpha and a sticker-pack spec

[Sonar](https://sonarprivacy.xyz/) ist ein Bluetooth-Mesh-plus-Nostr-Messenger und Wallet, gewachsen aus Bitchat, mit Marmot-Gruppen-DMs, die mit White Noise interoperieren. Code liegt unter [hedwig-corp/bitchat-to-sonar](https://github.com/hedwig-corp/bitchat-to-sonar). [v0.1-alpha.7](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.7) fügt Signal-artiges begrenztes Transcript-Windowing hinzu, damit Open- und Scroll-Performance local-first bleibt, synchronisiert Nearby-Discovery-State über Peers und behebt Blossom-Medien-Uploads, die bei Content-Type und HTTP-Status-Handling fehlschlugen; das vorangehende [alpha.6](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.6) leerte Live-Marmot-Events für schnellere Chat-Aktualisierung und schloss Android-zu-iOS-Feature-Parity-Lücken über Anrufe, Messaging, Wallet und Push. Sonar ist auch die zitierte Spezifikationsquelle für [PR #2410](#open-sticker-pack-kinds-10031-and-30031), die Sticker-Pack-Event-Kinds unter der eigenen „Sonar Stickers"-Spezifikation des Projekts registriert, was diesem Launch eine direkte Hub-Verbindung zur Protokollarbeit dieser Woche gibt.

### Divine Mobile 1.0.16 ships a deeper video editor, at-rest encryption, and ProofMode provenance

[Divine](https://github.com/divinevideo/divine-mobile) ist ein Kurzvideo-Client, der auf Nostr mit Web-of-Trust-Feed-Kuratierung aufbaut. [v1.0.16](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.16), das erste getaggte Release seit #30, fügt dem Video-Editor Clip-Übergänge, Rückwärtswiedergabe, einen Voice-Over-Recorder und Timeline-Beat-Marker hinzu, zusammen mit einem Feed-Tuning-Control, das einem Nutzer ermöglicht, durch Wischen die Empfehlungen direkt anzupassen, anstatt sie opaken Engagement-Signalen zu überlassen. Das Release aktiviert auch At-Rest-Verschlüsselung für lokale Daten, fügt Hintergrund-Uploads hinzu, die das Suspendieren der App überleben, und führt [ProofMode](/de/topics/proofmode/)-Provenienzdaten weiter, wenn ein wasserzeichenmarkierter Clip heruntergeladen wird, damit die Attestierung menschlicher Herkunft beim Transit nicht entfernt wird. Divine liefert auch neue Schutzmaßnahmen für Accounts unter 16 Jahren und erweitert die Lokalisierung auf 17 Sprachen und 284 übersetzte Strings.

### Bitchat v1.7.0 adds live push-to-talk voice for DMs and the public mesh

[Bitchat](https://github.com/permissionlesstech/bitchat) ist eine Bluetooth-Mesh-Chat-App mit einem optionalen Gateway auf Nostr-Relays. [v1.7.0](https://github.com/permissionlesstech/bitchat/releases/tag/v1.7.0), veröffentlicht am Abend der Veröffentlichung von #30, fügt Live-Push-to-Talk-Sprachübertragung in [PR #1403](https://github.com/permissionlesstech/bitchat/pull/1403) hinzu, die Audio streamt, während der Sender die Taste hält, und bei Abbruch des Streams auf eine Sprachnotiz zurückfällt, plus signiertes öffentliches Mesh-Push-to-Talk in [PR #1406](https://github.com/permissionlesstech/bitchat/pull/1406), sodass Live-Sprach-Bursts auf dem gemeinsamen Mesh-Kanal Sender-Authentifizierung tragen. Das Release heilt auch Peer-ID-Rotation durch erneutes Binden des Links bei einem verifizierten Re-Announce, wobei derselbe Peer unter seiner neuen ID erkannt wird ([PR #1401](https://github.com/permissionlesstech/bitchat/pull/1401)), und Direktnachrichten an einen derzeit nicht erreichbaren Peer werden jetzt mit Store-and-Forward-Zustellung in die Warteschlange gestellt, anstatt direkt fehlzuschlagen ([PR #1415](https://github.com/permissionlesstech/bitchat/pull/1415)). Dies setzt direkt die Berichterstattung von #30 über v1.6.0's [NIP-13](/de/topics/nip-13/) Proof-of-Work und Mesh-to-Nostr-Gateway-Arbeit fort.

### MDK v0.9.4 bounds external-signer login and adds draft persistence

[MDK](https://github.com/marmot-protocol/mdk) ist das Referenz-SDK für das [Marmot](/de/topics/marmot/)-Protokoll, die MLS-over-Nostr-Messaging-Schicht, deren Spezifikation #30 als übernommen behandelte. [v0.9.4](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.4) begrenzt die Advisory-Directory-Schritte, die ein Client beim External-Signer-Login durchläuft, in [PR #793](https://github.com/marmot-protocol/mdk/pull/793), und verhindert eine unbegrenzte Retry-Schleife, wenn ein Remote Signer langsam oder nicht erreichbar ist. Dasselbe Release fügt Draft-Message-Persistenz und Profil-Website-Bindings in [PR #812](https://github.com/marmot-protocol/mdk/pull/812) hinzu und setzt den inkrementellen Härtungsdurchgang fort, den MDK seit dem Schneiden von v0.9.0 durchführt.

---

## Getaggte Releases

### n_cord v1.1 adds NSEC Bunker support

[n_cord](https://github.com/0n4t3/n_cord) ist ein Nostr-basierter Chat-Client, inspiriert von Discord und IRC. [v1.1](https://github.com/0n4t3/n_cord/releases/tag/v1.1) fügt [NIP-46](/de/topics/nip-46/) NSEC-Bunker-Unterstützung hinzu, zusammen mit einem Reply-Handling-Bug-Fix.

### cdk v0.17.3 adds NIP-47 wallet-service support across cdk, cdk-nwc, and cdk-ffi

[cdk](https://github.com/cashubtc/cdk) ist ein Cashu Development Kit; dieses Release ist in den meisten Aspekten rein Bitcoin/Lightning, aber [v0.17.3](https://github.com/cashubtc/cdk/releases/tag/v0.17.3) fügt [NIP-47](/de/topics/nip-47/) (Nostr Wallet Connect) Service-Unterstützung mit einem dedizierten NWC-Service-Crate, Wallet-Integration, FFI-Bindings für `cdk-ffi` und End-to-End-Testabdeckung hinzu, was auf cdk aufbauenden Cashu-Wallets eine standardmäßige Nostr-Wallet-Connect-Oberfläche gibt.

### Coop Mobile v0.2.4 improves Nostr Connect and adds ncryptsec1 import

[Coop Mobile](https://git.reya.su/reya/coop-mobile) ist ein [NIP-17](/de/topics/nip-17/) Private-Messaging-Client für mobile Plattformen. [v0.2.4](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.4) verbessert den [NIP-46](/de/topics/nip-46/) Nostr-Connect-Ablauf, behebt einen Ladeindikator, der bei manchen Verbindungen permanent hängen blieb, und fügt Import-Unterstützung für das [NIP-49](/de/topics/nip-49/) `ncryptsec1`-verschlüsselte-Schlüssel-Format hinzu, zusammen mit einem umgestalteten Identitätsimport-Bildschirm.

### Nmail v0.14.0 ships on macOS with scheduled send and push notifications

[Nmail](https://github.com/nogringo/nostr-mail-client) ist ein auf Nostr aufbauender Mail-Client; [v0.14.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.14.0) bringt die App auf macOS, fügt geplantes Senden mit einem dedizierten Scheduled-Postfach für wartende Nachrichten und Push-Benachrichtigungen hinzu. Das Release stellt auch die Adressbuch-Nostr-Identifier-Auflösung auf NDKs [NIP-05](/de/topics/nip-05/)-Resolver um, anstelle einer maßgeschneiderten Implementierung.

### Nostrord v2.2.0 adds a DM master toggle and richer direct messages

[Nostrord](https://github.com/nostrord/nostrord) ist ein [NIP-29](/de/topics/nip-29/) relay-basierter Gruppen-Chat-Client für Android, iOS, Web und Desktop. [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) fügt einen Master-Toggle zum gleichzeitigen Deaktivieren aller Direktnachrichten-Funktionen hinzu ([PR #175](https://github.com/nostrord/nostrord/pull/175)) und liefert „reichere Direktnachrichten" ([PR #186](https://github.com/nostrord/nostrord/pull/186)), fortgesetzt nach der Berichterstattung in #30 über das Release, das den Relay-Pool faltete und Zombie-WebSockets erkannte.

### Nostr WoT 0.3.86 hardens key backups and signing prompts

[Nostr WoT](https://github.com/nostr-wot/nostr-wot-extension) ist eine Browser-Erweiterung, die eine Nostr-Identität mit einem Lightning-Wallet koppelt. [v0.3.86](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.3.86) verschiebt verschlüsselte Schlüssel-Backups in das standardmäßige [NIP-49](/de/topics/nip-49/)-Format, lässt Signatur-Prompts das vollständige Event und alle Tags anzeigen anstatt einer Zusammenfassung, verifiziert Relay-Daten gegen deren Signatur und stoppt das Offenlegen der aktiven Identität beim Kontowechsel. Die Erweiterung entfernt auch die ungenutzte `scripting`-Browser-Berechtigung.

### Keep Android v1.1.8 adds first-run FROST onboarding

[Keep](https://github.com/privkeyio/keep-android) ist ein Android-Signer, der auf FROST-Threshold-Key-Shares aufbaut. [v1.1.8](https://github.com/privkeyio/keep-android/releases/tag/v1.1.8) fügt einen First-Run-Ablauf hinzu, der FROST-Key-Shares erklärt und einem neuen Nutzer ermöglicht, eine Signatur-Richtlinie (Manual, Basic oder Auto) zu wählen, bevor die erste Signaturanfrage eintrifft, das erste Android-seitige Onboarding für das Threshold-Signing-Modell des zugrunde liegenden keep-mobile-Crate.

### Noscall v0.6.0 adds a Cashu wallet and relay-based push notifications

[Noscall](https://github.com/sanah9/noscall) ist eine sichere Audio- und Videoanruf-App, die auf Nostr aufbaut. [v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release) fügt ein kontobezogenes Cashu-Wallet mit Multi-Mint-Salden, ecash-Senden und -Empfangen und Lightning-Zahlen und -Empfangen mit Quote-Persistenz hinzu. Das Release migriert Android-Push-Benachrichtigungen auch weg von Firebase Cloud Messaging auf einen Nostr-relay-basierten Zustellpfad über UnifiedPush und verbessert die iOS-VoIP- und APNs-Push-Zuverlässigkeit bei Login-Wiederholungsversuchen.

### Kubo ships tablet mode and group-chat photos

[Kubo](https://github.com/JeroenOnNostr/kubo) ist eine kindersichere Nostr-Videoplattform mit Web-of-Trust-Feed-Kuratierung. [kubo-v2026.07.05](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v2026.07.05) fügt ein optionales Tablet-Grid-Layout für den Kinder-Feed und Unterstützung für das Anhängen von Fotos an Gruppen-Chat-Nachrichten hinzu, plus Fixes für den Anmeldeknopf, der sich auf Android hinter der Bildschirmtastatur versteckt.

### Nostr Codex Phone v0.2.9 adds git/diff/read-file helper requests

[Nostr Codex Phone](https://github.com/tidley/nostr-codex-phone) ist eine mobile Steuerungsoberfläche für einen lokalen Coding-Assistant-Worker, der über verschlüsselte Nostr-DMs kommuniziert. [v0.2.9](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.9) fügt mobile OpenCode-Tool-Aktionen hinzu, darunter git-, diff-, read-file-, status- und history-Helper-Requests, Session-Pin- und Suchverbesserungen sowie eine Task-Stop-Steuerung, neben einem verschlüsselten [Blossom](/de/topics/blossom/)-Upload-Wrapper, der im vorangegangenen v0.2.8 geliefert wurde.

### GitWorkshop v3.0.3 fixes newly announced refs in the repo explorer, and ships its first Android build

[GitWorkshop](https://github.com/DanConwayDev/gitworkshop) ist eine git-over-Nostr-Web-UI zum Durchsuchen und Reviewen von NIP-34-Repositories. [v3.0.3](https://github.com/DanConwayDev/gitworkshop/releases/tag/v3.0.3) behebt das Fehlschlagen der Branches-, Tags-, Commits- und Code-Browsing-Ansichten beim Auflösen eines Refs, den ein Repository ankündigt, nachdem der Explorer es bereits geladen hat, zusammen mit CI-Workflow-Timing-Bereinigung, direkt gegen den Tag und die Commit-Historie bestätigt. In derselben Woche veröffentlichte GitWorkshop seinen ersten nativen Android-Build im [Zapstore](https://zapstore.dev), startend bei v3.0.0 und innerhalb von Stunden v3.0.3 erreichend; die Web-UI bleibt das primäre Interface, und das Android-Paket bringt dasselbe NIP-34-Repository-Browsing zum ersten Mal auf ein Telefon.

### Bitcoin-Safe reaches Flathub, spotlighting its Nostr Sync & Chat plugin

[Bitcoin-Safe](https://bitcoin-safe.org) ist ein Self-Custody-Bitcoin-Wallet, das auf Hardware-Signer-Workflows aufbaut. Das Projekt [hat ein Flathub-Paket veröffentlicht](https://flathub.org/apps/org.bitcoin_safe.BitcoinSafe) in dieser Woche, sein erster Eintrag in einem Mainstream-Linux-App-Store. Das Flathub-Release bringt Bitcoin-Safes Sync-&-Chat-Plugin vor ein breiteres Publikum: Das Plugin verwendet [NIP-17](/de/topics/nip-17/) Direktnachrichten über die projekteigene [bitcoin-nostr-chat](https://github.com/andreasgriffin/bitcoin-nostr-chat)-Bibliothek, um Wallet-Labels zwischen den Geräten eines Nutzers zu synchronisieren und PSBTs für Remote-Multisig-Co-Signing zwischen vertrauenswürdigen Teilnehmern zu senden und zu empfangen. Die Nostr-Schicht selbst wurde früher ausgeliefert, in [2.0.0](https://github.com/andreasgriffin/bitcoin-safe/releases/tag/2.0.0) (2026-06-29), das das Transaktionssignieren um einen „Share via Chat & Sync"-Verbindungstyp neben QR, USB und Bluetooth umgestaltete. Die Nachricht dieser Woche ist das Flathub-Packaging, das dieses bestehende Feature zum ersten Mal einem Mainstream-Linux-Publikum zugänglich macht.

---

## Unveröffentlichte Änderungen

### Amethyst lets accounts nickname contacts with encrypted NIP-85 cards

Neben der oben behandelten [Concord-Implementierung](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities) mergte Amethyst in der letzten Woche 54 weitere PRs. Das Highlight darunter ist [PR #3548](https://github.com/vitorpamplona/amethyst/pull/3548), das einem Account ermöglicht, jeden anderen Nutzer mit einem Spitznamen zu versehen, indem es seine eigene kind-30382-[NIP-85](/de/topics/nip-85/)-Kontaktkarte über ihn veröffentlicht. Der Petname, eine private Notiz und beliebige benutzerdefinierte [NIP-30](/de/topics/nip-30/) Emoji-Shortcode-Zuordnungen befinden sich im [NIP-44](/de/topics/nip-44/)-verschlüsselten Inhalt der Karte, sodass nur der signierende Account sie lesen kann, und Karten synchronisieren über das erweiterte Outbox-Relay-Set des Accounts bei Login und danach inkrementell. Feeds, Chats und Erwähnungen rendern den Petname anstelle des öffentlichen Anzeigenamens, mit einer antippbaren Spitznamenkarte auf der Profilseite oberhalb des echten Namens des Nutzers.

### Zap Cooking ships My Kitchen Phase 3 and fixes an NDK pool quorum bug

[Zap Cooking](https://github.com/zapcooking/frontend) ist eine Rezept-Sharing- und Koch-Community-App, die auf Nostr aufbaut. Sie mergte 43 PRs, die ihr „My Kitchen"-Mahlzeitenplanungs-Feature fortsetzen, mit Einkaufslisten-Generierung, einem Rezept-Picker und einem Planer-Wochenraster in dieser Phase. Dieselbe Reihe von Änderungen behebt einen [NDK](https://github.com/nostr-dev-kit/ndk) (Nostr Development Kit) Connection-Pool-Quorum-Readiness-Bug, der Relay-Reads warten lassen konnte, nachdem ein Quorum von Relays bereits geantwortet hatte.

### Kehto streams outbox reads before relay discovery

[Kehto](https://github.com/kehto/web) ist eine frühe webbasierte Laufzeitumgebung für [NIP-5D](/de/topics/nip-5d/) Nostr Applets, oder „Napplets". Sie mergte 26 PRs. [PR #193](https://github.com/kehto/web/pull/193) behebt Outbox-Reads, die zuvor auf das Laden der [NIP-65](/de/topics/nip-65/) Relay-Liste warteten, bevor überhaupt ein Relay geöffnet wurde, sodass ein Relay-Liste-Load, der nie abschloss, sowohl Event-Zustellung als auch Query-Timeouts blockieren konnte; der Fix öffnet validierte Relay-Hints sofort und streamt Ergebnisse, während Write-Relays entdeckt werden. Eine zweite Änderung ([PR #196](https://github.com/kehto/web/pull/196)) richtet die Identitäts-Audit-Seite des Projekts an NAP-SHELL aus, dem Lifecycle-Contract der Napplet-Plattform, Teil derselben Protokoll-Alignment-Arbeit, die anderswo im `napplet/web`-Release dieser Woche sichtbar ist.

### Wired and TAO add NIP-57 creator revenue sharing

[Wired](https://github.com/smolgrrr/Wired) und [TAO](https://github.com/smolgrrr/TAO) sind Zwillings-Free-Speech-fokussierte Social-Clients, die auf Nostr aufbauen und dieselbe PR-Liste teilen; beide mergten [PR #121](https://github.com/smolgrrr/Wired/pull/121), das [NIP-57](/de/topics/nip-57/) Creator Revenue Sharing implementiert, sodass an einen Post gesendete Zaps automatisch an Beitragende über den ursprünglichen Poster hinaus aufgeteilt werden können. Dies setzt die Berichterstattung von #30 über das Paar fort, das sein Proof-of-Work-Signal auf 21 Bit als unveröffentlichte Arbeit erhöht hat.

### Conduit Mono rebuilds the merchant orders inbox around ephemeral guest checkout

[Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) ist ein Marktplatz-Protokoll neben [NIP-99](/de/topics/nip-99/) Classified Listings. [PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174) fügt Guest Checkout mit einem browserseitig generierten ephemeren Schlüssel hinzu: Der Gast sendet eine verschlüsselte Bestellung und einen Zahlungsbericht an den Händler unter Verwendung dieses Einmalschlüssels, und der Händler folgt außerhalb des Bands per Telefon oder E-Mail auf, sodass der Käufer nie eine dauerhafte Inbox-Identität benötigt. [PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175) baut den Händler-Bestelleingang um ein einzelnes gemeinsames Bestellstatus-Modell um, trennt Käufer- und Händlerrollen und verlangt einen Tracking-Code und Carrier, bevor eine physische oder gemischte Bestellung auf „versandt" wechseln kann. Der Checkout-Ablauf des Projekts baut auf [NIP-17](/de/topics/nip-17/) Private Messages, [NIP-44](/de/topics/nip-44/) Verschlüsselung und [NIP-59](/de/topics/nip-59/) Gift Wrap auf. Der [NIP Deep Dive](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension) dieser Woche behandelt die [Gamma Markets](/de/topics/gamma-markets/)-Konventionen, auf die dasselbe Bestellstatus-Problem hinarbeitet.

### Buzz hardens channel-creator provisioning around kind 39002

[Buzz](https://github.com/block/buzz) ist eine Hive-Mind-Kommunikationsplattform, die KI-Agenten und Menschen über Nostr verbindet. Sie mergte 240 PRs in der letzten Woche und setzte ihren Relay-Schicht-Härtungsbogen fort, nach der Berichterstattung von #30 über kind-44200-Agent-Turn-Metriken. Der Fix dieser Woche ([PR #1830](https://github.com/block/buzz/pull/1830)) behandelt den Creator eines Channels als Mitglied, bevor die kind-39002-Channel-Provisioning-Logik ausgeführt wird, und schließt eine Race Condition, bei der der eigene Channel des Creators ihn während des Setups ablehnen konnte.

### Nostr Docs adopts a NIP-49 signer with multi-account and QR pairing

[Nostr Docs](https://github.com/formstr-hq/nostr-docs) ist eine Nostr-native kollaborative Dokumentenanwendung. Sie mergte 5 PRs, der bemerkenswerte ([PR #50](https://github.com/formstr-hq/nostr-docs/pull/50)) übernimmt das `@formstr/signer`-Paket für vollständige [NIP-49](/de/topics/nip-49/)-Authentifizierung mit Multi-Account-Switching und QR-Pairing und ersetzt einen früheren maßgeschneiderten Signaturpfad.

### Ebenfalls ausgeliefert

Kleinere Signer-Interop- und Zuverlässigkeits-Fixes landeten in der letzten Woche über mehrere getrackte Projekte hinweg, ohne genug neue Oberfläche für eigene Absätze: [ngit-cli](https://github.com/DanConwayDev/ngit-cli), ein Kommandozeilen-Client für eine Nostr-basierte GitHub-Alternative, liefert [v2.6.3](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.6.3), das `ngit init` umsetzbare Setup-Anleitung statt wiederholter nsec-Abfragen gibt; [Manent](https://github.com/dtonon/manent), eine private verschlüsselte Notizen-und-Dateien-App auf Nostr, liefert [v1.4.1](https://github.com/dtonon/manent/releases/tag/v1.4.1) mit einem Fix für defektes Android-Signer-Login, wenn Amber einen Hex-pubkey zurückgibt, und verbessertem Bunker-Login-Scrolling; [NoorNote](https://github.com/77elements/noornote), ein schlanker, Google-Service-freier Nostr-Client, liefert [v1.2.8](https://github.com/77elements/noornote/releases/tag/v1.2.8) mit einem Fix für verpasste Nostrord-Gruppen-Benachrichtigungen und einem Self-Post-Alert-Toggle; [Bray](https://github.com/forgesworn/bray), ein vertrauensbewusster Nostr-MCP-Server für KI-Agenten und Menschen, liefert [v1.34.0](https://github.com/forgesworn/bray/releases/tag/v1.34.0), das Client-Name-Metadaten bei [NIP-46](/de/topics/nip-46/) Bunker Connect sendet; [Lumilumi](https://github.com/TsukemonoGit/lumilumi), ein Nostr-Web-Client, cachet [NIP-65](/de/topics/nip-65/) Relay-Listen im lokalen Speicher für Offline-Fallback; [Earthly](https://github.com/moogmodular/earthly), eine Nostr-basierte lokale Stadt- und Community-App, fügt [NIP-50](/de/topics/nip-50/) Geo-Suche hinzu; und [lnbits](https://github.com/lnbits/lnbits), ein freies und Open-Source-Lightning-Wallet- und Kontensystem, liefert [PR #3925](https://github.com/lnbits/lnbits/pull/3925), das `send_nostr_dm` nicht-blockierend innerhalb eines ansonsten Lightning-fokussierten Releases veröffentlicht.

---

## Neu getrackt und entdeckt

### OpenDiscord v1.0.1 launches as a Discord-style client on Nostr

[OpenDiscord](https://github.com/sofia-gros/open-discord) ist ein Discord-artiger Server-und-Channel-Client, der auf Nostr mit rollenbasierten Berechtigungen und WebRTC/SFU-Sprach-Lobbies aufbaut. [v1.0.1](https://github.com/sofia-gros/open-discord/releases/tag/v1.0.1) ist das erste getaggte Installer-Release des Projekts.

### Auditable Voting v0.1.140 aligns organiser, voter, and audit-proxy roles

[Auditable Voting](https://github.com/tidley/auditable-voting) ist eine Client-only-Nostr-Abstimmungs-Shell. [v0.1.140](https://github.com/tidley/auditable-voting/releases/tag/v0.1.140) richtet die Organiser-, Voter- und Audit-Proxy-Rollen am exakten vom Organiser signierten öffentlichen Questionnaire-Definition-Event aus und schließt eine Lücke, bei der ein Audit-Proxy auf veralteten generierten Accounts oder State operieren konnte, der von einem anderen Worker oder Organiser stammte.

### Cambium v0.3.2 pairs with Heartwood as a keyless NIP-55 signer

[Cambium](https://github.com/forgesworn/cambium) ist der Discovery-Pick dieser Ausgabe: ein Android-[NIP-55](/de/topics/nip-55/)-Signer, der selbst kein privates Schlüsselmaterial hält und jede Signaturanfrage über [NIP-46](/de/topics/nip-46/) an einen Heartwood-Hardware-Signer-Companion weiterleitet. Das Projekt teilt die `forgesworn`-GitHub-Org mit dem getrackten Projekt Bray, und Heartwood selbst wurde in #30 behandelt, als es die Relay-to-Serial-Signing-Bridge auslieferte, mit der Cambiums Android-Seite nun kommuniziert. [v0.3.2](https://github.com/forgesworn/cambium) poliert das Genehmigungsblatt, um live zu warnen, wenn die gewählte Identität von der bestehenden Bindung der App abweicht, und verschiebt Activity-Log-Schreibvorgänge in eine einzelne nicht-blockierende Warteschlange.

### Ebenfalls diese Woche gestartet: echoes, Dispatch und Linky

Drei weitere Launches verdienen eine Erwähnung diese Woche. [echoes](https://github.com/Lwb89dev/echoes) ist eine Offline-First-, Ende-zu-Ende-verschlüsselte Notizen-App, die privat über Nostr synchronisiert. [Dispatch](https://github.com/freecritter/dispatch) ist ein Local-First-Reiseorganizer, bei dem jede Speicherung [NIP-44](/de/topics/nip-44/)-verschlüsselt und über Nostr unter einem dedizierten, nicht verlinkbaren Schlüssel gesichert wird, und sein [v0.3.0](https://github.com/freecritter/dispatch)-Release fügt Amber-[NIP-55](/de/topics/nip-55/)-Login hinzu, damit die App den privaten Schlüssel des Nutzers nie direkt berührt. [Linky](https://github.com/hynek-jina/linky) kombiniert Nostr-Kontakte und DMs mit Lightning- und Cashu-Zahlungen in einer einzigen Progressive Web App.

---

## Protokollarbeit und NIP-Updates

Keine PRs wurden in der letzten Woche in das [NIPs-Repository](https://github.com/nostr-protocol/nips) gemergt. Sechs Vorschläge wurden geöffnet.

### Open: kind:10011 favorite follow sets

[PR #2413](https://github.com/nostr-protocol/nips/pull/2413), von fiatjaf, fügt kind:10011 Favorite Follow Sets hinzu. Es spiegelt das bestehende Muster, bei dem kind:10012 (Favorite Relay Sets) `a`-Tags enthält, die auf kind:30002 Relay Sets zeigen, und erweitert denselben Favorisierungsmechanismus auf kind:30000 Follow Sets, damit ein Client eine kuratierte Follow-Liste als Lesezeichen speichern kann, ohne seine eigene Kontaktliste zu ersetzen.

### Open: private encrypted drive extends NIP-4E

[PR #2412](https://github.com/nostr-protocol/nips/pull/2412), vom Form*-Team, schlägt ein generisches Metadata-Event vor, kind 34578, unterschieden durch einen `d`-Identifier-Tag und einen `t`-Sub-Type-Tag, zusammen mit einem privaten verschlüsselten Dateisystem, das darauf aufbaut und bereits in Form*'s eigenem, noch experimentellem Form* Drive Client implementiert ist. Ein Datei-Datensatz ist ein Metadata-Event mit `t=files`: Datei-Blobs liegen auf [Blossom](/de/topics/blossom/)-Servern, während nur ein verschlüsselter Index auf Relays sitzt, und jeder Datei-Chunk erhält sein eigenes ephemeres Schlüsselpaar mit [NIP-44](/de/topics/nip-44/) v2 HKDF-abgeleiteter Verschlüsselung. Ein begleitendes Decoupled Encryption Key Event hält einen laufwerkweiten symmetrischen Schlüssel, gegen den jede Datei ihre Metadaten entschlüsselt, und baut explizit auf [NIP-4E](/de/topics/nip-4e/) auf, fiatjafs noch offenem Storage-Abstraction-Entwurf ([PR #1647](https://github.com/nostr-protocol/nips/pull/1647), offen seit Dezember 2024).

Dieser einzelne laufwerkweite Schlüssel bedeutet, dass ein durchgesickerter Schlüssel die Metadaten jeder Datei im Laufwerk offenlegt, nicht nur einer Datei, da die pro-Datei ephemeren Schlüsselpaare nur den Chunk-Verschlüsselungsschlüssel variieren, nicht den Metadaten-Entschlüsselungsschlüssel; es gibt noch keinen Rotations- oder Widerrufspfad außer dem Veröffentlichen eines neuen Metadata-Events mit der Warnung, dass ältere Events verloren gehen können. Ein zweiter, engerer Vorschlag greift dieselbe zugrunde liegende NIP-4E-Idee aus einem anderen Blickwinkel auf: [PR #2361](https://github.com/nostr-protocol/nips/pull/2361), von fiatjaf, entkoppelt Identitäts- und Verschlüsselungsschlüssel speziell innerhalb von [NIP-17](/de/topics/nip-17/) Messaging, offen seit 1. Juni. Beide PRs sind nicht gemergt, was dies zu einer aktiven, umstrittenen Ecke des Designraums macht. Form* sagt, der Drive Client sei experimentell und ein Update komme bald.

### Open: NIP-DA permissioned private data sharing

[PR #2411](https://github.com/nostr-protocol/nips/pull/2411), von JAFairweather, ist ein neuer NIP-DA-Entwurf für genehmigungsbasiertes privates Datenteilen über scoped Data Grants. Jeder Nutzer hält einen verschlüsselten, autoritativen Datensatz pro Scope auf Relays, und Zugang wird gewährt, indem der symmetrische Schlüssel dieses Scopes privat innerhalb eines [NIP-59](/de/topics/nip-59/) Gift Wraps zugestellt wird, sodass Relays nur Ciphertext speichern und nie erfahren, wer wem Zugang gewährt hat; ein Widerruf ist einfach eine Schlüsselrotation, ohne jeden Consumer-Kopie neu schreiben zu müssen. Der Autor positioniert es als distinkt von [NIP-17](/de/topics/nip-17/) DMs (die einen Daten-Snapshot transportieren können, aber keine Live-Updates oder Widerrufe) und von NIP-51 Private Lists (die kein Schlüsselmaterial transportieren), und zitiert zwei unabhängige Implementierungen, eine JavaScript-Referenzbibliothek und eine Go-CLI auf go-nostr, kreuzgetestet gegen relay.damus.io, nos.lol und relay.primal.net.

### Open: sticker pack kinds 10031 and 30031

[PR #2410](https://github.com/nostr-protocol/nips/pull/2410), von vincenzopalazzo, registriert kind 30031 (adressierbare Sticker Packs) und kind 10031 (die Sticker-Pack-Liste eines Nutzers) in der Event-Kinds-Tabelle, spezifiziert durch das „Sonar Stickers"-Format, das [Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec) diese Woche ausliefert. Die Kinds liegen bewusst einen Slot über den [NIP-30](/de/topics/nip-30/) Custom-Emoji-Kinds 30030 und 10030, damit ein Client ein Sticker Pack nicht mit einem Emoji-Set verwechseln kann; Sticker-Bild-Bytes liegen auf HTTPS-[Blossom](/de/topics/blossom/)-kompatiblen Servern, und gesendete Sticker-Referenzen tragen einen Klartext-Hash, damit ein bearbeitetes adressierbares Pack nicht stillschweigend das Aussehen von Stickern ändern kann, die bereits in alten Nachrichten gesendet wurden. Ein begleitender PR registriert dieselben Kinds im separaten `registry-of-kinds`-Projekt.

### Open: NIP-29 message pinning with kind:9010 and kind:39005

[PR #2379](https://github.com/nostr-protocol/nips/pull/2379), von Anderson-Juhasc, fügt Message Pinning zu [NIP-29](/de/topics/nip-29/) relay-basierten Gruppen hinzu: kind:9010 `update-pin-list` ist ein Moderations-Event, das die vollständige Liste der angepinnten Events als `e`-Tags in Anzeigereihenfolge trägt, sodass ein einzelnes Event pinnen, entpinnen, umsortieren oder die angepinnte Menge leeren kann, und kind:39005 ist ein relay-generierter Spiegel, der die zuletzt akzeptierte Liste offenlegt. Das Design ersetzt einen früheren Add/Remove-Paar-Ansatz aus [PR #1163](https://github.com/nostr-protocol/nips/pull/1163) nach Review-Feedback und wählt Kind-Nummern 9010/39005, weil 9009 und 39003 inzwischen von `create-invite` und Gruppenrollen beansprucht wurden. Anderson-Juhasc pflegt auch [Nostrord](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages), dessen [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) in derselben Woche ausgeliefert wird.

### Open: NIP-66 relay discovery restructure

[PR #2241](https://github.com/nostr-protocol/nips/pull/2241), von VincenzoImp, ist eine umfassende Umstrukturierung von [NIP-66](/de/topics/nip-66/) Relay Discovery. Es ersetzt die lose „Other tags include"-Prosa durch einen strukturierten Indexed-Tags-Abschnitt, fügt einen `W`-Tag hinzu, der NIP-11s `attributes`-Feld für Relay-Discovery-Filterung spiegelt, fügt einen `l`-Label-Tag mit standardisierten Namespaces (`ISO-639-1`, `ISO-3166-1`, `IANA-asn`, `IANA-tz`, `nip66.label.city`) hinzu und organisiert RTT-, SSL/TLS-, Netzwerk-, Geo-, DNS- und HTTP-Tags in dedizierte Abschnitte neben einer neuen Check-Types-Tabelle. Es behebt auch fehlerhafte Beispiel-Events mit falschen Feldnamen, einem fehlenden `kind` und ungültigen Check-Type-Namen und schließt [Issue #2171](https://github.com/nostr-protocol/nips/issues/2171) ab. Alle Änderungen bleiben abwärtskompatibel, da jeder hinzugefügte Tag optional ist.

---

## NIP Deep Dive: NIP-99 und die Gamma-Markets-Commerce-Erweiterung

[NIP-15](/de/topics/nip-15/), die ursprüngliche Nostr Marketplace-Spezifikation, ist inzwischen Legacy: Sie modellierte einen Merchant Stall (kind 30017) mit Produkten (kind 30018) darunter, und die Clients, die einst darauf liefen, Shopstr unter ihnen, sind seitdem zu [NIP-99](/de/topics/nip-99/) Classified Listings als aktiver Spezifikation gewechselt. NIP-99 selbst ist ein einzelnes adressierbares Event, kind 30402 für ein aktives Listing oder kind 30403 für einen Entwurf, ohne zuerst einen Stall erstellen zu müssen. Es lässt alles nach dem Listing undefiniert: Versandkosten, Bestellstatus, Quittungen, Bewertungen und eine Möglichkeit, mehrere Listings unter einem Schaufenster zu gruppieren, genau die Teile von NIP-15, die nie übernommen wurden. [Gamma Markets](/de/topics/gamma-markets/) füllt diese Lücke und ist die moderne Commerce-Schicht, die es heute zu verstehen lohnt.

### Die Lücke, die NIP-99 offen lässt

Das `content`-Feld eines NIP-99-Listings trägt eine Markdown-Beschreibung, `price` und `location` sitzen direkt auf dem Event, und `t`-Tags machen es als gewöhnlichen Hashtag-Content durchsuchbar. Da es auf dem pubkey-, kind- und `d`-Tag-Tupel adressierbar ist, bearbeitet ein Verkäufer ein Listing direkt, indem er eine neue Version mit demselben `d`-Tag veröffentlicht:

```json
{
  "kind": 30402,
  "content": "Vintage mechanical keyboard, Cherry MX Blue switches, barely used.",
  "tags": [
    ["d", "keyboard-mx-blue-01"],
    ["title", "Vintage Mechanical Keyboard"],
    ["summary", "Cherry MX Blue, barely used"],
    ["published_at", "1752537600"],
    ["location", "NYC"],
    ["price", "100", "USD"],
    ["t", "electronics"]
  ]
}
```

Das ist die gesamte Spezifikation: eine signierte, aktualisierbare Kleinanzeige. Jeder Client, der NIP-99 für echten E-Commerce implementiert, über eine einmalige Kleinanzeige hinaus, musste seine eigenen privaten Konventionen für Versand, Bestellnachrichten und Bewertungen erfinden. Zwei NIP-99-Clients konnten jeweils ein Listing korrekt darstellen und hatten trotzdem keinen gemeinsamen Weg, einen Checkout zwischen ihnen abzuschließen.

### Gamma Markets: Standardisierung dessen, was NIP-99 ausließ

Gamma Markets ist der Name, den eine Arbeitsgruppe von Nostr-Marktplatz-Entwicklern, die Teams hinter Shopstr, Cypher, Plebeian Market und Conduit Market, einem gemeinsamen Satz von E-Commerce-Konventionen gab, die auf NIP-99s bestehendem kind-30402-Event aufbauen. Die Spezifikation ist vom kanonischen NIP-99-Dokument über [PR #1784](https://github.com/nostr-protocol/nips/pull/1784) verlinkt und wird in ihrem eigenen Repository gepflegt, [GammaMarkets/market-spec](https://github.com/GammaMarkets/market-spec).

Gamma Markets fügt zwei eigenständige listing-angrenzende Kinds hinzu. Kind 30405 gruppiert mehrere Listings in eine Produktsammlung und referenziert jedes über ein explizites `a`-Tag:

```json
{
  "kind": 30405,
  "content": "Summer sale picks",
  "tags": [
    ["d", "summer-picks"],
    ["title", "Summer Sale"],
    ["a", "30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["shipping_option", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

Kind 30406 definiert eine Versandoption mit länderspezifischer Preisgestaltung und optionalen gewichts- oder entfernungsbasierten Kostenregeln:

```json
{
  "kind": 30406,
  "content": "Standard Regional Shipping",
  "tags": [
    ["d", "standard-regional"],
    ["title", "Standard Shipping"],
    ["price", "5.99", "USD"],
    ["country", "US"],
    ["service", "standard"],
    ["duration", "24", "72", "H"],
    ["weight-max", "30", "kg"]
  ]
}
```

Bestellerstellung, Zahlungsanforderungen, Status- und Versand-Updates und Zahlungsbelege laufen alle als gewöhnliche [NIP-17](/de/topics/nip-17/) Gift-Wrapped Private Messages, aufgeteilt auf drei Kinds nach Rolle, nicht durch erneutes Wrapping des Transports: kind 14 transportiert freie Käufer/Händler-Kommunikation, kind 16 transportiert jeden Bestellstatus-Übergang (ein `type`-Tag von 1 bis 4 markiert Bestellerstellung, Zahlungsanforderung, Statusupdate oder Versandupdate), und kind 17 transportiert den Zahlungsbeleg des Käufers. Eine Bestellerstellungsnachricht sieht vor dem Gift-Wrapping so aus:

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

Die Bewertung eines abgeschlossenen Kaufs ist ein separater adressierbarer Kind, 31555, der auf das bewertete Listing zurückverweist:

```json
{
  "kind": 31555,
  "content": "Arrived fast, exactly as described.",
  "tags": [
    ["d", "a:30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["rating", "1", "thumb"],
    ["rating", "1.0", "quality"],
    ["rating", "0.9", "delivery"]
  ]
}
```

Bestellnachrichten auf NIP-17 aufzusetzen bedeutet, dass ein Gamma-Markets-Checkout denselben Private-Message-Transport nutzt, den Clients bereits für DMs ausliefern, anstatt einen eigenen Bestellnachrichten-Kind zu erfinden.

Die zentrale Designentscheidung der Spezifikation ist, dass nichts kaskadiert. Ein Listing, das zu einer Sammlung gehört, referenziert diese explizit mit einem `a`-Tag, anstatt die Versandoptionen oder Beschreibung der Sammlung automatisch zu erben, und eine Versandoption, die ein Listing verwendet, wird auf dieselbe explizite Weise referenziert. Das ist eine bewusste Umkehrung von NIP-15s Stall-Modell, bei dem ein Produkt stillschweigend die Währung und Versandtabelle seines übergeordneten Stalls erbte. Der Kompromiss ist mehr explizites Tagging auf jedem Listing, im Austausch dafür, dass die vollständige Konfiguration eines Listings immer aus dem Event selbst lesbar ist, ohne ein übergeordnetes Objekt zuerst auflösen zu müssen.

### Wo das in der Praxis auftaucht

Die [Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout)-Arbeit dieser Woche liegt im selben Bestellnachrichten-Territorium, das Gamma Markets standardisiert: [PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174)'s ephemerer Schlüssel-Guest-Checkout und [PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175)'s Händler-Bestelleingang-Umbau lösen beide das Käufer/Händler-Bestellstatus-Problem, das Gamma Markets' kind-14-, 16- und 17-Nachrichten formalisieren; Conduit Mono betreibt sein eigenes Bestellstatus-Modell neben diesen Kinds, ohne sie direkt zu übernehmen. Shopstr, eines der vier Projekte, die die Spezifikation verfasst haben, hat seine eigene Commerce-Infrastruktur in der letzten Woche ebenfalls vorangetrieben: [PR #568](https://github.com/shopstr-eng/shopstr/pull/568) extrahiert duplizierte NIP-17-Gift-Wrap-Logik in ein gemeinsames Modul, und [PR #567](https://github.com/shopstr-eng/shopstr/pull/567) bringt seinen [NIP-98](/de/topics/nip-98/) HTTP-Auth-Parser auf vollständige Testabdeckung, Wartung an genau den Messaging- und Auth-Schichten, von denen ein Gamma-Markets-Bestellablauf abhängt, um einen Käufer und Händler sicher zu erreichen.

NIP-15 verlor die Storefront-Rolle, indem es einen Stall und ein Produkt standardisierte und dann Zahlungen, Versand, Bewertungen und Bestellstatus als Anwendungsproblem beließ. Gamma Markets füllt den größten Teil dieser fehlenden Oberfläche, ohne NIP-99s Single-Listing-Form zu verändern, und baut auf Nostrs bestehendem DM-Stack, NIP-17, auf, anstatt eine neue Messaging-Schicht zu erfinden.

---

Das war's für diese Woche. Baut ihr etwas oder habt Neuigkeiten zu teilen? Meldet euch per NIP-17-DM oder findet uns auf Nostr.
