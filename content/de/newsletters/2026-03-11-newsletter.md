---
title: 'Nostr Compass #13'
date: 2026-03-11
translationOf: /en/newsletters/2026-03-11-newsletter.md
translationDate: 2026-03-11
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, deinem wöchentlichen Wegweiser durch Nostr.

**Diese Woche:** [Shopstr](https://github.com/shopstr-eng/shopstr) und [Milk Market](https://github.com/shopstr-eng/milk-market) fügen MCP-Oberflächen für agentengesteuerten Handel hinzu, während [OAuth Bunker](https://github.com/flox1an/oauth-bunker), [Amber](https://github.com/greenart7c3/Amber) und [strfry](https://github.com/hoytech/strfry) Relay-Auth und Unterstützung für geschützte Events nach [NIP-42](/de/topics/nip-42/) (Authentifizierung von Clients bei Relays) über App-, Signer- und Relay-Software hinweg ergänzen. [Route96](https://github.com/v0l/route96) liefert zwei Releases rund um KI-Labeling, Moderationswarteschlangen, perzeptuelles Hashing und maschinenlesbare Serverdokumentation. [Samizdat](https://github.com/satsdisco/samizdat), bereits im Web live, veröffentlichte seine erste Android-Alpha und ergänzte später Signer-Unterstützung nach [NIP-55](/de/topics/nip-55/) (Android-Signer-Anwendung). [Formstr](https://github.com/formstr-hq/nostr-forms) ergänzt Signup über [NIP-49](/de/topics/nip-49/) (Verschlüsselung privater Schlüssel), [Amethyst](https://github.com/vitorpamplona/amethyst) liefert Namecoin-basierte Auflösung für [NIP-05](/de/topics/nip-05/) (Domain-Verifizierung), [Mostro](https://github.com/MostroP2P/mostro) veröffentlicht [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4), und das NIPs-Repository merged [NIP-91](/de/topics/nip-91/) (AND-Operator für Filter) sowie defensive Hinweise für [NIP-66](/de/topics/nip-66/) (Relay-Entdeckung und Liveness-Monitoring).

## Neuigkeiten

<a id="shopstr-and-milk-market-open-mcp-commerce-surfaces"></a>
### Shopstr und Milk Market öffnen MCP-Commerce-Oberflächen

[Shopstr](https://github.com/shopstr-eng/shopstr), der Peer-to-Peer-Marketplace mit Lightning- und Cashu-Zahlungen, mergte [PR #234](https://github.com/shopstr-eng/shopstr/pull/234) ([commit 94ef7d1](https://github.com/shopstr-eng/shopstr/commit/94ef7d1a4519e8e0158668d13c8cb8684b1d46e2)) und fügte einen MCP-Server mit API-Key-Authentifizierung für agentenseitige Kontoverwaltung hinzu. Die Änderung ergänzt `.well-known/agent.json` für Agent-Discovery, MCP-Onboarding- und Status-Endpunkte, Routen für Bestellerstellung und Zahlungsprüfung, dedizierte Kauf- und Lese-Tools sowie einen Einstellungsbildschirm für API-Keys. [PR #236](https://github.com/shopstr-eng/shopstr/pull/236) erweitert das um verkäuferseitige Aktionen für Nachrichten, Adressen, Bestellupdates und Produktspezifikations-Auswahl. Ein Sicherheitsfix in [PR #235](https://github.com/shopstr-eng/shopstr/pull/235) ersetzt Single-Iteration-SHA-256-Hashing für API-Keys durch gesalzenes PBKDF2 mit 100.000 Iterationen.

Agenten können Listings nach [NIP-99](/de/topics/nip-99/) (Kleinanzeigen) lesen und den Checkout über die bestehenden Zahlungsflüsse von [NIP-47](/de/topics/nip-47/) (Nostr Wallet Connect) und [NIP-60](/de/topics/nip-60/) (Cashu Wallet) durchlaufen, ohne Seiten zu scrapen oder Client-Verhalten zurückzuentwickeln.

[Milk Market](https://github.com/shopstr-eng/milk-market), ein Lebensmittel-Marketplace auf Nostr unter [milk.market](https://milk.market), landete dieselbe MCP- und API-Key-Grundlage in [commit da6c0b4](https://github.com/shopstr-eng/milk-market/commit/da6c0b499494b4e4861c4ff8a220e066c46285b3). [PR #10](https://github.com/shopstr-eng/milk-market/pull/10) ergänzt Abo-Bestellungen, Änderungen der Lieferadresse nach dem Kauf sowie Multi-Merchant- und Multi-Currency-Checkout für Stripe und andere Fiat-Zahlungswege. Ein nachfolgender [PR #11](https://github.com/shopstr-eng/milk-market/pull/11) behebt einen Start-Bug bei der Datenbankinitialisierung, bei dem die Tabelle für fehlgeschlagene Relay-Publishes auf frischen Installationen nicht erstellt wurde und beim ersten Laden 500-Fehler verursachte. Die agentenseitige Oberfläche funktioniert mit Bitcoin-nativem Checkout bei Shopstr oder gemischtem Fiat- und Bitcoin-Checkout bei Milk Market.

### NIP-42-Relay-Auth über Bunker, Signer und Relay hinweg

[OAuth Bunker](https://github.com/flox1an/oauth-bunker), ein [NIP-46](/de/topics/nip-46/) (Nostr Connect) Bunker, der OAuth-Provider mit Nostr-Signing verbindet, ergänzte Login über [NIP-07](/de/topics/nip-07/) (Browser-Erweiterungs-Signer), automatische Auswahl einer einzelnen Identität und Bereinigung gelöschter Identitäten ([commit f0c7683](https://github.com/flox1an/oauth-bunker/commit/f0c7683cb2374fd9a3ebd1b186055da8abd2c2ff)). Wenn nur eine Identität existiert, wählt der Bunker sie nun automatisch aus, statt nachzufragen. Das Löschen einer Identität entfernt außerdem ihre verwaisten Zuweisungen und Verbindungen. [Commit 6b8796c](https://github.com/flox1an/oauth-bunker/commit/6b8796c6c59c7d48dc1ede92d6de6bf54feb56cc) ergänzt einen Konfigurationspfad `ALWAYS_ALLOWED_KINDS` für zugewiesene Nutzer, standardmäßig für kind `30078` app-spezifische Daten, damit delegierte Identitäten in app-spezifischen Speicher schreiben können, ohne pro Event bestätigt werden zu müssen.

[Amber](https://github.com/greenart7c3/Amber), der wichtigste [NIP-55](/de/topics/nip-55/) Signer für Android, veröffentlichte [v4.1.3-pre4](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3-pre4) mit vier Pre-Releases innerhalb der Woche. [PR #317](https://github.com/greenart7c3/Amber/pull/317) ergänzt NIP-42-Relay-Authentifizierung für kind-`22242`-Anfragen. Die Implementierung fügt eine neue Datenbankspalte hinzu, die relay-spezifische Berechtigungen mit einem eindeutigen Index auf `(pkKey, type, kind, relay)` speichert. Nutzer sehen einen eigenen Auth-Bildschirm, in dem sie pro Relay oder relayübergreifend mit einem Wildcard-Scope `*` erlauben oder ablehnen und diese Wahl speichern können. Wildcard-Berechtigungen löschen alle relay-spezifischen Einträge für einen kind. [PR #318](https://github.com/greenart7c3/Amber/pull/318) folgt darauf mit einem Refactor der Multi-Event-Anfragebildschirme, die Details nun inline mit composable cards anzeigen, statt zu einem separaten Bildschirm zu navigieren. Das Release aktualisiert außerdem Standard-Profil-Relays, ergänzt eine Bottom-Sheet-Darstellung für Anfragen und behebt einen Absturz auf MediaTek-Geräten durch das Deaktivieren des StrongBox-Keystore.

Auf der Relay-Seite implementiert [strfry PR #156](https://github.com/hoytech/strfry/pull/156) NIP-42-Auth-Handling für [NIP-70](/de/topics/nip-70/) (Geschützte Events), und [PR #176](https://github.com/hoytech/strfry/pull/176) lehnt Reposts ab, die geschützte Events einbetten.

<a id="notedeck-adds-nip-11-relay-limits-and-agentium-features"></a>
### Notedeck ergänzt NIP-11-Relay-Limits und Agentium-Features

[Notedeck](https://github.com/damus-io/notedeck), der native Desktop-Client des Damus-Teams, mergte diese Woche 14 PRs. [PR #1316](https://github.com/damus-io/notedeck/pull/1316) ergänzt das Abrufen von Relay-Limits nach [NIP-11](/de/topics/nip-11/) (Relay-Informationen), sodass alle Outbox-Relays nun `max_message_length` und `max_subscriptions` aus dem Relay-Info-Dokument beachten. Die Implementierung umfasst Hintergrundjob-Verarbeitung, exponentielles Backoff mit Jitter für Verbindungs-Retries und benutzerdefinierte HTTP-Accept-Header. [PR #1312](https://github.com/damus-io/notedeck/pull/1312) behebt einen Bug, bei dem DMs nach einem Accountwechsel manchmal nicht geladen wurden, und [PR #1333](https://github.com/damus-io/notedeck/pull/1333) ergänzt einen Backoff-Mechanismus für multicast Relay-Kommunikation, um Broadcast-Spam bei Fehlern zu verhindern.

Das Agentium-Subsystem (Notedecks eingebaute Coding-Agent-UI, intern „Dave" genannt) erhielt Einfügen von Zwischenablagebildern, benannte Run-Konfigurationen, die sich über kind-`31991`-Events geräteübergreifend synchronisieren ([NIP-33](/de/topics/nip-33/) (Parametrisierte ersetzbare Events)), einen git-worktree-Ersteller und einen Model-Picker zur Auswahl von Backends pro Sitzung ([PR #1336](https://github.com/damus-io/notedeck/pull/1336)). [PR #1338](https://github.com/damus-io/notedeck/pull/1338) integriert `egui_kittest` für Headless-UI-Tests, und [PR #1339](https://github.com/damus-io/notedeck/pull/1339) ergänzt eine Dashboard-Karte, die neu erstellte Kontaktlisten pro Client nachverfolgt. Ein offener [PR #1314](https://github.com/damus-io/notedeck/pull/1314) portiert Amethysts Namecoin-NIP-05-Auflösung nach Notedeck mit ElectrumX-Lookups, SOCKS5-Tor-Routing und Suchleisten-Integration.

### diVine liefert v1.0.6 mit E2E-Test-Infrastruktur und NIP-49-Import

[diVine](https://github.com/divinevideo/divine-mobile), der Short-Form-Looping-Video-Client zur Wiederherstellung von Vine-Archiven unter [divine.video](https://divine.video), veröffentlichte [v1.0.6](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.6) mit 127 gemergten PRs. Das Release ergänzt Account-Import nach [NIP-49](/de/topics/nip-49/), externe [NIP-05](/de/topics/nip-05/)-Unterstützung, Multi-Account-Handling, macOS- und experimentelle Linux-Builds sowie eine neu gestaltete Bibliothek für Entwürfe und Clips auf Basis lokalen Speichers.

Auf der Engineering-Seite ergänzt [PR #1928](https://github.com/divinevideo/divine-mobile/pull/1928) eine vollständige E2E-Integrations-Test-Infrastruktur mit Patrol für native UI-Automatisierung gegen einen Docker-Backend-Stack (relay, API, Blossom, Postgres, Redis, ClickHouse). Fünf Auth-Journey-Tests decken Registrierung, Verifizierung, Passwort-Reset, Session-Ablauf und Token-Refresh ab. [PR #2105](https://github.com/divinevideo/divine-mobile/pull/2105) wechselt das Videoladen von HLS-first auf direktes MP4 mit automatischem HLS-Fallback und reduziert die Ladezeit damit von 30-60 Sekunden auf nahezu sofort. [PR #2076](https://github.com/divinevideo/divine-mobile/pull/2076) cached die Home-Feed-API-Antwort in SharedPreferences für sofortige Anzeige beim Cold Start. [PR #2104](https://github.com/divinevideo/divine-mobile/pull/2104) erzwingt, dass `ai-generated`-Inhaltslabel in Feeds verborgen werden, und [PR #2100](https://github.com/divinevideo/divine-mobile/pull/2100) ergänzt eine Sicherheitseinstellung, die nur von diVine gehostete Videos zeigt. Die Hive-zu-Drift-Migration des Profil-Caches läuft weiter über [PR #1881](https://github.com/divinevideo/divine-mobile/pull/1881), [PR #1883](https://github.com/divinevideo/divine-mobile/pull/1883) und [PR #1903](https://github.com/divinevideo/divine-mobile/pull/1903) und ersetzt ungefähr 1.074 Zeilen Hive-Code durch Drift-DAOs.

### Vector v0.3.2 liefert NIP-77-Negentropy-Sync und MLS-Verbesserungen

[Vector](https://github.com/VectorPrivacy/Vector), ein datenschutzorientierter Desktop-Messenger mit MLS-Gruppenverschlüsselung unter Verwendung von [NIP-17](/de/topics/nip-17/) (Private Direktnachrichten) und [NIP-44](/de/topics/nip-44/) (Verschlüsselte Payloads), veröffentlichte [v0.3.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.2). Die wichtigste Änderung ist NIP-77-Negentropy für MLS-Gruppensynchronisierung ([commit b06adf4](https://github.com/VectorPrivacy/Vector/commit/b06adf4af2673fb5ac5add01356999ea70628eac)), das verpasste Nachrichten mit parallelem Boot deutlich schneller aufholt. Das Release ergänzt außerdem eine neu aufgebaute Audio-Engine mit voller Linux-Unterstützung, Bild-Spoiler mit verschwommenen Vorschauen, anklickbare Hyperlinks mit Rich-Link-Previews, `@mention`-Pings mit `@everyone` für Gruppenadmins, Emoji-Shortcode-Autovervollständigung, Gruppen-Stummschaltung, Tap-to-React auf bestehende Reaktionen und abbrechbare Datei-Uploads. Vector filtert NIP-17-Gruppenchat-Events ausdrücklich heraus ([commit 2179a51](https://github.com/VectorPrivacy/Vector/commit/2179a51c0449b3a70663a1573195b7945adf58ba)) und nutzt MLS ausschließlich für Gruppenverschlüsselung.

## Releases

### Route96 v0.5.0 und v0.5.1

[Route96](https://github.com/v0l/route96), ein Medienserver mit Unterstützung für Blossom und [NIP-96](/de/topics/nip-96/) (HTTP-Dateispeicherung), veröffentlichte [v0.5.0](https://github.com/v0l/route96/releases/tag/v0.5.0) und [v0.5.1](https://github.com/v0l/route96/releases/tag/v0.5.1). v0.5.0 ergänzt automatisches KI-Labeling, rückwirkendes Backfill für ungelabelte Uploads, Moderationswarteschlangen für markierte Dateien, EXIF-basierte Datenschutz-Ablehnung und Handling gebannter Hashes.

v0.5.1 ergänzt perzeptuelle Bild-Hashes, locality-sensitive hashing für Similar-Image-Lookups, Batch-Admin-Endpunkte und ein veröffentlichtes [`SKILL.md`](https://github.com/v0l/route96/releases/tag/v0.5.1), das die Blossom- und NIP-96-API-Oberfläche des Servers für Agent-Tooling beschreibt. [PR #58](https://github.com/v0l/route96/pull/58) verschiebt Hintergrund-Worker auf vollständig asynchrone Tokio-Tasks, und [commit 97b00a3](https://github.com/v0l/route96/commit/97b00a39e27b07053c2ad335dbf475bacba57bf8) ergänzt Backoff, um Hot Loops zu vermeiden.

### Samizdat v1.0.0-alpha

[Samizdat](https://github.com/satsdisco/samizdat), ein Longform-Reader und Publisher unter [samizdat.press](https://samizdat.press), veröffentlichte seinen ersten Android-Build in [v1.0.0-alpha](https://github.com/satsdisco/samizdat/releases/tag/v1.0.0-alpha). Die App öffnet mit einer kuratierten Press-Seite für Nostr-Langformartikel und Bottom-Tab-Navigation über Press-, Feed-, Saved- und Write-Ansichten. Der Android-Build ergänzt native Schlüsselspeicherung per Android-Keystore-Verschlüsselung mit biometrischem Unlock, verarbeitet `nostr:`-URIs und `samizdat.press`-Deep-Links und unterstützt Signer-Handoff über den Android-App-Chooser (Amber, Primal usw.), statt direkten Key-Import zu verlangen. Pull-to-Refresh, Safe-Area-Handling über verschiedene Bildschirmgrößen hinweg sowie native Share-, Clipboard-, Haptics- und Splash-Screen-Integrationen sind nun Teil der Android-Shell statt des Web-Wrappers.

[Commit d17308f](https://github.com/satsdisco/samizdat/commit/d17308f3c2e6020e14074fbb1c03a8f60f29a3e6) ergänzt intent-basiertes [NIP-55](/de/topics/nip-55/) Signing für Amber- und Primal-Flows, und [commit e29dab8](https://github.com/satsdisco/samizdat/commit/e29dab84f7b58edd621f7b86ed7ca6458f965614) ersetzt einen JavaScript-Bridge-Workaround durch ein natives Capacitor-Plugin unter Verwendung von `startActivityForResult`. Die App benötigt Android 7.0+ (API 24), wird in dieser Alpha als Debug-APK ausgeliefert und hat weiterhin keine Push-Benachrichtigungen. Veröffentlichen hängt derzeit von einer Signer-App ab, während `nsec`-Login lokales Lesen und Account-Zugriff abdeckt.

### Calendar by Form* v0.2.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), eine dezentrale Kalender-App mit privatem Event-Sharing über [NIP-59](/de/topics/nip-59/) (Gift Wrap) unter [calendar.formstr.app](https://calendar.formstr.app), veröffentlichte [v0.2.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.0) mit [PR #38](https://github.com/formstr-hq/nostr-calendar/pull/38). Das Release erweitert das Handling wiederkehrender Events für [NIP-52](/de/topics/nip-52/) (Kalenderereignisse) und geht damit über die Single-Event-Grundlage von v0.1.0 hinaus. Die zugrunde liegenden Änderungen betreffen außerdem lokalen Event-Speicher, Signer-Handling und Android-Benachrichtigungsanbindung. Dies ist die zweite aktive Anwendung der Formstr-Organisation nach der Repository-Migration im letzten Monat.

### Mostro v0.16.4

[Mostro](https://github.com/MostroP2P/mostro), die auf Nostr basierende Peer-to-Peer-Bitcoin-Börse, veröffentlichte [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4). Die Fixes für die Wiederherstellung von Dispute-Sessions ([PR #599](https://github.com/MostroP2P/mostro/pull/599)) und Auto-Close ([PR #606](https://github.com/MostroP2P/mostro/pull/606)), die [letzte Woche behandelt wurden](/de/newsletters/2026-03-04-newsletter/), sind enthalten. Neu in diesem Release: [PR #625](https://github.com/MostroP2P/mostro/pull/625) ergänzt ein Feld `days` zu Nutzerbewertungs-Events des kinds `38384`, [PR #612](https://github.com/MostroP2P/mostro/pull/612) ergänzt Ablaufdaten für diese Bewertungs-Events, und [PR #614](https://github.com/MostroP2P/mostro/pull/614) stellt Bestell-Events auf konfigurierte Ablaufwerte statt auf ein hartkodiertes 24-Stunden-Fenster um. [PR #622](https://github.com/MostroP2P/mostro/pull/622) ergänzt eine Idempotenzprüfung, um doppelte Zahlungen der Development Fee zu verhindern.

### Mostro Mobile v1.2.1

[Mostro Mobile](https://github.com/MostroP2P/mobile), der Flutter-Client für die Mostro-P2P-Börse, veröffentlichte [v1.2.1](https://github.com/MostroP2P/mobile/releases/tag/v1.2.1) mit 11 neuen Features und 11 Bugfixes. Das Release ergänzt verschlüsseltes Multimedia-Rendering im Dispute-Chat ([PR #514](https://github.com/MostroP2P/mobile/pull/514)), automatisches Schließen der Dispute-UI, wenn Bestellungen einen Endzustand erreichen ([PR #503](https://github.com/MostroP2P/mobile/pull/503)), QR-Scanning für NWC-Wallet-Import ([commit 12eaee4](https://github.com/MostroP2P/mobile/commit/12eaee4d154fa31b07f82b96819de520e825aee6)), französische Übersetzungen und FCM-Push-Benachrichtigungen. [PR #496](https://github.com/MostroP2P/mobile/pull/496) behebt einen Padding-Bug bei Schnorr-Signaturen, indem die bip340-Abhängigkeit auf v0.2.0 festgesetzt wird.

### 0xchat v1.5.4

[0xchat](https://github.com/0xchat-app/0xchat-app-main), der Telegram-artige Messaging-Client mit Cashu-Unterstützung, veröffentlichte [v1.5.4](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.4-release) mit Fokus auf Linux-Desktop-Fixes: AppImage-Dock-Icons, Emoji-Rendering, eingefrorene Kontextmenüs und Hänger bei Antwort-/Kopier-UI. Das Release behebt außerdem Probleme beim Bild-Upload und der npub.cash-Integration. [PR #49](https://github.com/0xchat-app/0xchat-app-main/pull/49) beseitigt unnötige UI-Rebuilds, indem ein 3-Sekunden-Polling-Timer entfernt wird, der ohne Nutzen glassmorphe Repaints erzwang, und entblockiert die Login-Initialisierung, indem das Laden des Event-Caches parallel läuft, statt Relay-, Kontakt- und Channel-Start zu blockieren.

### Keep v0.6.0

[Keep](https://github.com/privkeyio/keep-android), ein FROST-Threshold-Signer für Android mit Unterstützung für [NIP-55](/de/topics/nip-55/) und [NIP-46](/de/topics/nip-46/), veröffentlichte [v0.6.0](https://github.com/privkeyio/keep-android/releases/tag/v0.6.0) und [v0.6.1](https://github.com/privkeyio/keep-android/releases/tag/v0.6.1). v0.6.0 ergänzt Koordination von Wallet-Deskriptoren und Management-UI, einen Backup-/Restore-Flow mit biometrischer Authentifizierung ([PR #184](https://github.com/privkeyio/keep-android/pull/184)), `nsec`-Wiederherstellung aus Threshold-Shares ([PR #187](https://github.com/privkeyio/keep-android/pull/187)), plattformübergreifende animierte QR-Frame-Generierung via Rust UniFFI ([PR #188](https://github.com/privkeyio/keep-android/pull/188)) und einen Signier-Audit-Trail mit Kettenverifikation ([PR #189](https://github.com/privkeyio/keep-android/pull/189)). v0.6.1 stellt die Lizenz von AGPL-3.0 auf MIT um ([PR #191](https://github.com/privkeyio/keep-android/pull/191)).

### njump v0.3.0

[njump](https://github.com/fiatjaf/njump), das statische Gateway zum Anzeigen von Nostr-Inhalten unter [njump.me](https://njump.me), veröffentlichte [v0.3.0](https://github.com/fiatjaf/njump/releases/tag/v0.3.0) mit einer Breaking Change beim Parsing von `note1`-Codes und einem Update der zugrunde liegenden nostr-Bibliothek.

### Roadstr v0.1.1

[Roadstr](https://github.com/jooray/roadstr), eine dezentrale App zur Meldung von Straßenereignissen auf Basis von Nostr, veröffentlichte ihren ersten Demo-Release [v0.1.1](https://github.com/jooray/roadstr/releases/tag/v0.1.1). Die App zeigt Straßenereignisse auf einer Karte mit Vektor-Tiles von openfreemap.org an.

### Bitcredit v0.5.3

[Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core), eine E-Bill-Anwendung mit Nostr-Transportschicht und dediziertem Relay unter [bit.cr](https://www.bit.cr/), veröffentlichte [v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3). [PR #846](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846) ergänzt die API um die Felder `payment_actions` und `bill_state` für Zahlungs- und Annahmestatus, und [PR #849](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849) behebt das Handling von Signieradressen für anonyme Signer.

### OpenChat v0.1.0-alpha.3

[OpenChat](https://github.com/DavidGershony/openChat), eine Chat-Anwendung auf Basis der .NET-MLS- und C#-Bibliotheken des Marmot-Protokolls, veröffentlichte [v0.1.0-alpha.3](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.3). Das Release ergänzt Unterstützung für externe Signer bei Amber- und [NIP-46](/de/topics/nip-46/)-Flows ([commit e568d97](https://github.com/DavidGershony/openChat/commit/e568d979fe15eead19172f2eb6f8cf26ca845247)), verschiebt die Persistierung des MLS-Zustands in den MLS-Service, um Datenverlust in Absturzfenstern zu verhindern ([commit 4720bc8](https://github.com/DavidGershony/openChat/commit/4720bc8625136a0d5b0e23322bc0c50cd80577e8)), und veröffentlicht Windows-, Linux- und Android-Builds über eine neue CI-Pipeline.

### OpenSignal v1.0.0

[OpenSignal](https://github.com/turizspace/opensignal), ein Kotlin-Multiplatform-Trading-Copilot für Nostr, veröffentlichte [v1.0.0](https://github.com/turizspace/OpenSignal/releases/tag/v1.0.0). Das Release bündelt gemeinsame KMP-Module für Domain-Logik, Chart-Rendering, Nostr-Authentifizierung und -Publishing, Blossom-[NIP-96](/de/topics/nip-96/)-Upload-Unterstützung und ONNX-basierte KI-Inferenz-Hooks über Desktop- und Android-Shells hinweg. Die veröffentlichte Architektur umfasst außerdem einen FastAPI-KI-Service für die Analyse von Chart-Screenshots, Pipelines zum Modelltraining und eine Risiko-Engine, die strukturierte Trade-Pläne mit Sizing und Warnungen erzeugt. Login unterstützt entweder rohe `nsec`-Schlüssel oder externe Signer, und der Ausgabe-Flow endet in der Veröffentlichung von Nostr-Events statt in rein lokaler Analyse.

## Projekt-Updates

### Formstr

[Formstr](https://github.com/formstr-hq/nostr-forms), die Google-Forms-Alternative auf Nostr, mergte [PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) ([commit e9c4fd5](https://github.com/formstr-hq/nostr-forms/commit/e9c4fd5dadfa0b83f1e87d7596eaf35f9fdb7da8)) und ergänzt einen Signup-Flow mit nach [NIP-49](/de/topics/nip-49/) (Verschlüsselung privater Schlüssel) verschlüsselten privaten Schlüsseln. Vor dieser Änderung brauchten Nutzer entweder eine [NIP-07](/de/topics/nip-07/) Browser-Erweiterung oder das direkte Einfügen eines rohen `nsec`, um Formstr zu verwenden. Der neue Flow erzeugt clientseitig ein Schlüsselpaar, verschlüsselt den privaten Schlüssel mit einem vom Nutzer gewählten Passwort nach NIP-49s scrypt- plus XChaCha20-Poly1305-Schema und speichert den resultierenden `ncryptsec`-String. Nutzer können sich dann mit ihrem Passwort wieder anmelden, ohne eine Signer-Erweiterung installieren zu müssen. Das Schlüsselmanagement bleibt durchgehend clientseitig.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), der funktionsreiche Android-Client, mergte vier PRs, die die Namecoin-gestützte [NIP-05](/de/topics/nip-05/)-Auflösung liefern, die [letzte Woche offen war](/de/newsletters/2026-03-04-newsletter/). [PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734) ergänzt zensurresistente NIP-05-Verifizierung via ElectrumX für `.bit`-, `d/`- und `id/`-Identifier. Wenn Amethyst einen dieser Suffixe in einem NIP-05-Feld erkennt, fragt es einen ElectrumX-NMC-Server nach der Transaktionshistorie des Namens, parst das `NAME_UPDATE`-Skript aus dem neuesten Output, um den Nostr-pubkey zu extrahieren, und lehnt Namen ab, die älter als 36.000 Blöcke sind (Namecoins Ablauf-Fenster). ElectrumX-Verbindungen laufen über SOCKS5, wenn Tor aktiviert ist, mit dynamischer Serverauswahl zwischen Clearnet- und `.onion`-Endpunkten. Ein LRU-Cache mit einer Stunde TTL verhindert wiederholte Blockchain-Abfragen.

[PR #1771](https://github.com/vitorpamplona/amethyst/pull/1771) behebt Race Conditions und die Korrektheit des Resolvers in diesem Flow. [PR #1785](https://github.com/vitorpamplona/amethyst/pull/1785) erlaubt neuen Nutzern beim Signup den Import einer Follow-Liste entweder aus gewöhnlichen NIP-05-Identifiern oder aus Namecoin-gestützten. [PR #1786](https://github.com/vitorpamplona/amethyst/pull/1786) ergänzt benutzerdefinierte ElectrumX-Servereinstellungen, damit Nutzer wählen können, welcher Server ihre Lookups verarbeitet.

### nostr-idb

[nostr-idb](https://github.com/hzrd149/nostr-idb), eine Bibliothek mit Hilfsmethoden zum Speichern von Nostr-Events in IndexedDB, mergte [PR #6](https://github.com/hzrd149/nostr-idb/pull/6), die Unterstützung für AND-Tag-Filter nach [NIP-91](/de/topics/nip-91/) ergänzt. Die Änderung fügt clientseitigem Filter-Matching Schnittmengen-Semantik hinzu, sodass IndexedDB-Abfragen verlangen können, dass alle aufgelisteten Tag-Werte erfüllt sind statt nur irgendeiner davon. [PR #8](https://github.com/hzrd149/nostr-idb/pull/8) aktualisiert die Bibliothek auf die neueste NIP-DB-Schnittstelle, und ein nachfolgender [commit b49b3d3](https://github.com/hzrd149/nostr-idb/commit/b49b3d32c575ff8214dc3fb07675109c2a971972) behebt einen Subscribe-Deadlock und entfernt nostr-tools als Produktionsabhängigkeit.

### Pensieve

[Pensieve](https://github.com/andotherstuff/pensieve), ein archive-first Nostr-Indexer mit ClickHouse-Analytik, mergte [PR #8](https://github.com/andotherstuff/pensieve/pull/8), der pro Eintrag erzwungene Cache-TTLs und Miss-Coalescing pro Schlüssel ergänzt, um CPU-Spitzen der API zu senken. Die teuersten Time-Series-Endpunkte (Engagement-Statistiken, stündliche Aktivität, Aktivität pro kind) verwenden nun serverseitige TTLs von zehn Minuten, statt synchronisierte Recompute-Stürme auszulösen.

### Blossom

[Blossom](https://github.com/hzrd149/blossom), das dezentrale Medien-Hosting-Protokoll und der zugehörige Server-Stack, mergte zwei Autorisierungs-Updates für BUD-11. [PR #91](https://github.com/hzrd149/blossom/pull/91) verschiebt optionale Autorisierung in ein eigenes BUD und präzisiert die Rolle der Tags `x` und `server`. [PR #93](https://github.com/hzrd149/blossom/pull/93) bereinigt endpunktspezifisches Auth-Verhalten und formalisiert den Header `X-SHA-256` zur Upload-Verifikation. Die beiden PRs konsolidieren die Auth-Logik in BUD-11 und beseitigen Unklarheiten rund um Request-Hashing für Upload-, Delete- und Medienverwaltungs-Flows.

<a id="nip-updates"></a>
## NIP-Updates

Aktuelle Änderungen am [NIPs-Repository](https://github.com/nostr-protocol/nips):

**Gemergt:**

- **[NIP-91](/de/topics/nip-91/) (AND-Operator für Filter)** ([PR #1365](https://github.com/nostr-protocol/nips/pull/1365)): Ergänzt Schnittmengen-Semantik für Tag-Filter, sodass Relays Abfragen beantworten können, die alle aufgeführten Tag-Werte statt nur eines davon verlangen. Das reduziert clientseitiges Nachfiltern und Bandbreitenverbrauch bei taglastigen Abfragen.

- **[NIP-66](/de/topics/nip-66/) (Relay-Entdeckung und Liveness-Monitoring): Defensive Measures** ([PR #2240](https://github.com/nostr-protocol/nips/pull/2240)): Nach der [Outbox-Benchmark-Arbeit von letzter Woche](/de/newsletters/2026-03-04-newsletter/) ergänzt die Spezifikation nun Warnungen zu problematischen Pfaden bei Relay-Monitoring-Daten. Clients dürfen Monitoring-Events des kinds `30166` nicht voraussetzen, um zu funktionieren. Ein Monitor kann falsch, veraltet oder bösartig sein. Von Clients wird erwartet, Quellen gegenzuprüfen und nicht auf Basis eines einzelnen Feeds große Teile des Relay-Graphen eines Nutzers abzuschneiden.

- **[NIP-39](/de/topics/nip-39/) (Externe Identitäten in Profilen): Bereinigung des kind-10011-Registers** ([PR #2256](https://github.com/nostr-protocol/nips/pull/2256)): Ergänzt die Referenz auf kind `10011` direkt in der Spezifikation und richtet sie damit an Amethysts Implementierung aus, die [letzte Woche behandelt wurde](/de/newsletters/2026-03-04-newsletter/).

**Offene PRs und Diskussionen:**

- **[NIP-70](/de/topics/nip-70/) (Geschützte Events): Reposts ablehnen, die geschützte Events einbetten** ([PR #2251](https://github.com/nostr-protocol/nips/pull/2251)): Wenn ein Relay NIP-70 auf das ursprüngliche Event durchsetzt, aber Reposts akzeptiert, die denselben Inhalt tragen, hat das Tag `-` praktisch keine Wirkung. Dieser PR ergänzt daher die Regel, dass Relays auch Reposts vom kind 6 und kind 16 geschützter Events ablehnen müssen. [strfry PR #176](https://github.com/hoytech/strfry/pull/176) implementiert das bereits.

- **[NIP-71](/de/topics/nip-71/) (Video-Events): Mehrere Audiospuren** ([PR #2255](https://github.com/nostr-protocol/nips/pull/2255)): Ergänzt Audio-`imeta`-Tags für alternative Tracks, Sprachvarianten und Audio-only-Streams. Ein Client könnte eine stabile Videodatei beibehalten und gleichzeitig die Audiosprache wechseln oder Audio als separaten Track für podcastähnliche Inhalte ausliefern.

- **[NIP-11](/de/topics/nip-11/) (Relay-Informationen) und [NIP-66](/de/topics/nip-66/) Relay-Attribute** ([PR #2257](https://github.com/nostr-protocol/nips/pull/2257)): Ergänzt ein strukturiertes Feld `attributes` zu Relay-Informationsdokumenten und gibt Clients und Discovery-Tools damit maschinenlesbare Metadaten jenseits der bisherigen Freitextbeschreibung.

<a id="nip-deep-dive-nip-49-private-key-encryption"></a>
## NIP-Vertiefung: NIP-49 (Verschlüsselung privater Schlüssel)

[NIP-49](/de/topics/nip-49/) definiert, wie ein Client einen privaten Schlüssel mit einem Passwort verschlüsselt und das Ergebnis als bech32-String `ncryptsec` kodiert. [Formstr](#formstr) verwendet NIP-49 in seinem neuen Signup-Flow.

Das Format ist nicht an einen eigenen Event-kind gebunden. Ein Client beginnt mit dem rohen 32-Byte-secp256k1-Private-Key, leitet mit scrypt aus dem Passwort des Nutzers einen symmetrischen Schlüssel ab, verschlüsselt den Schlüssel mit XChaCha20-Poly1305 und verpackt das Ergebnis dann in einen bech32-String `ncryptsec`. Ein Ein-Byte-Flag speichert, ob der Schlüssel vor der Verschlüsselung irgendwann bekanntermaßen unsicher behandelt wurde.

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

Das JSON-Event oben ist ein Beispiel auf Anwendungsebene, keine NIP-49-Anforderung. Das NIP standardisiert das Format des verschlüsselten Schlüssels. Ein Client kann das `ncryptsec` lokal speichern, über app-spezifischen Speicher synchronisieren oder als Backup-String exportieren. Passwörter werden vor der Schlüsselableitung auf Unicode NFKC normalisiert, damit dasselbe Passwort über Clients und Plattformen hinweg konsistent entschlüsselt.

Das Ein-Byte-Flag für Schlüsselsicherheit hat drei definierte Werte: `0x00` bedeutet, dass die Handhabungshistorie des Schlüssels unbekannt ist, `0x01` bedeutet, dass der Schlüssel bekanntermaßen unsicher behandelt wurde (zum Beispiel als Klartext in ein Webformular eingefügt, bevor er verschlüsselt wurde), und `0x02` bedeutet, dass der Schlüssel in einem sicheren Kontext erzeugt und verschlüsselt wurde und nie offengelegt war. Clients können dies nutzen, um beim Import von Schlüsseln mit bekannter unsicherer Historie Warnungen anzuzeigen.

NIP-49 schützt Schlüssel besser als ein einfacher `nsec`-Export, aber die Verschlüsselung ist nur so stark wie das Passwort und die konfigurierte scrypt-Kostenstufe. Höhere `LOG_N`-Werte erschweren Offline-Raten, verlangsamen aber legitime Entschlüsselungsvorgänge. Die Spezifikation warnt davor, verschlüsselte Schlüssel auf öffentliche Relays zu veröffentlichen, weil Angreifer vom Sammeln von Ciphertext für Offline-Cracking profitieren. Zum Vergleich vermeidet Remote-Signing nach [NIP-46](/de/topics/nip-46/) die Offenlegung von Schlüsseln vollständig, und Android-Signing nach [NIP-55](/de/topics/nip-55/) hält Schlüssel in einer dedizierten Signer-App. NIP-49 füllt einen anderen Slot: portables verschlüsseltes Backup für Nutzer, die ihre eigenen Schlüssel verwalten.

Implementierungen umfassen [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) für Signup, [Amber](https://github.com/greenart7c3/Amber) für ncryptsec-Backup und -Restore, [diVine v1.0.6](#divine-liefert-v106-mit-e2e-test-infrastruktur-und-nip-49-import) für Account-Import, [Keep v0.6.0](#keep-v060) für FROST-Share-Export und Key-Management-Tools wie [nsec.app](https://nsec.app) und [Alby](https://github.com/getAlby/hub).

<a id="nip-deep-dive-nip-70-protected-events"></a>
## NIP-Vertiefung: NIP-70 (Geschützte Events)

[NIP-70](/de/topics/nip-70/) definiert geschützte Events. Wenn ein Event das Tag `["-"]` trägt, muss ein Relay es ablehnen, es sei denn, das Relay verlangt Authentifizierung nach [NIP-42](/de/topics/nip-42/) und der authentifizierte pubkey entspricht dem Autor des Events.

Der NIP-42-Auth-Flow funktioniert wie folgt: Das Relay sendet eine `AUTH`-Challenge mit einem Zufallsstring, und der Client antwortet mit einem signierten kind-`22242`-Event, dessen Tags die Relay-URL und die Challenge enthalten. Das Relay verifiziert die Signatur und prüft, dass der pubkey im Auth-Event mit dem pubkey des geschützten Events übereinstimmt, das veröffentlicht werden soll. Wenn die pubkeys nicht übereinstimmen, lehnt das Relay das Event mit dem Nachrichtenpräfix `restricted` ab.

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

Selbst wenn ein Relay die Veröffentlichung des ursprünglichen Events durch Dritte blockiert, kann jemand den Inhalt in einem Repost erneut veröffentlichen. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) adressiert das, indem Relays verpflichtet werden, auch Reposts vom kind 6 und kind 16 geschützter Events abzulehnen. [strfry PR #156](https://github.com/hoytech/strfry/pull/156) ergänzt NIP-42-Auth-Handling für geschützte Events, und [strfry PR #176](https://github.com/hoytech/strfry/pull/176) blockiert Reposts, die geschützten Inhalt einbetten.

NIP-70 steuert Relay-Verhalten. Ein Empfänger kann den Inhalt weiterhin anderswo kopieren, und die Spezifikation sagt das ausdrücklich. Das Tag `-` gibt Relays ein maschinenlesbares Signal, die Wiederveröffentlichung abzulehnen. Zum Vergleich fordert [NIP-62](/de/topics/nip-62/) (Vanish Requests) Relays dazu auf, Daten nachträglich zu löschen, während NIP-70 unautorisierte Veröffentlichung bereits bei der Aufnahme verhindert. Beide ergänzen sich: Ein Autor kann Events als geschützt markieren, um Verbreitung zu begrenzen, und später Löschung anfordern, wenn Inhalte von Relays entfernt werden sollen, die sie doch angenommen haben.

---

Das war's für diese Woche. Baust du etwas oder hast Neuigkeiten zu teilen? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Melde dich per [NIP-17](/de/topics/nip-17/) DM</a> oder finde uns auf Nostr.
