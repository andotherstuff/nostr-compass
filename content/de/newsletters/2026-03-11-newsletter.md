---
title: 'Nostr Compass #13'
date: 2026-03-11
translationOf: /en/newsletters/2026-03-11-newsletter.md
translationDate: 2026-04-23
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, deinem wöchentlichen Wegweiser durch Nostr.

**Diese Woche:** [Shopstr](https://github.com/shopstr-eng/shopstr) und [Milk Market](https://github.com/shopstr-eng/milk-market) bauen MCP-Oberflächen für agentengesteuerten Handel, während [OAuth Bunker](https://github.com/flox1an/oauth-bunker), [Amber](https://github.com/greenart7c3/Amber) und [strfry](https://github.com/hoytech/strfry) [NIP-42](/de/topics/nip-42/) (Authentication of Clients to Relays) Relay-Auth und Protected-Event-Unterstützung quer durch App-, Signer- und Relay-Software ergänzen. [Route96](https://github.com/v0l/route96) veröffentlicht zwei Releases rund um KI-Kennzeichnung, Moderationswarteschlangen, Perceptual Hashing und maschinenlesbare Server-Dokumentation. [Samizdat](https://github.com/satsdisco/samizdat), bereits im Web live, veröffentlicht sein erstes Android-Alpha und ergänzt später [NIP-55](/de/topics/nip-55/) (Android Signer Application) Signer-Unterstützung. [Formstr](https://github.com/formstr-hq/nostr-forms) fügt Registrierung per [NIP-49](/de/topics/nip-49/) (Private Key Encryption) hinzu, [Amethyst](https://github.com/vitorpamplona/amethyst) liefert Namecoin-basierte [NIP-05](/de/topics/nip-05/) (Domain Verification) Auflösung, [Mostro](https://github.com/MostroP2P/mostro) veröffentlicht [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4), und das NIPs-Repository merged [NIP-91](/de/topics/nip-91/) (AND Operator for Filters) sowie defensive Hinweise für [NIP-66](/de/topics/nip-66/) (Relay Discovery and Liveness Monitoring).

## Neuigkeiten

### Shopstr und Milk Market öffnen MCP-Handelsoberflächen

[Shopstr](https://github.com/shopstr-eng/shopstr), der Peer-to-Peer-Marktplatz mit Lightning- und Cashu-Zahlungen, mergte [PR #234](https://github.com/shopstr-eng/shopstr/pull/234) ([Commit 94ef7d1](https://github.com/shopstr-eng/shopstr/commit/94ef7d1a4519e8e0158668d13c8cb8684b1d46e2)) und fügte damit einen MCP-Server mit API-Key-Authentifizierung für agentenbasiertes Account-Management hinzu. Die Änderung ergänzt `.well-known/agent.json` für Agent-Erkennung, MCP-Onboarding- und Status-Endpunkte, Routen für Bestellerstellung und Zahlungsprüfung, dedizierte Kauf- und Lesetools sowie einen Einstellungsbildschirm für API-Keys. [PR #236](https://github.com/shopstr-eng/shopstr/pull/236) erweitert das um Seller-seitige Aktionen für Nachrichten, Adressen, Bestell-Updates und Produktspezifikationsauswahl. Ein Sicherheitsfix in [PR #235](https://github.com/shopstr-eng/shopstr/pull/235) ersetzt Single-Iteration-SHA-256 beim Hashing der API-Keys durch gesalzenes PBKDF2 mit 100.000 Iterationen.

Agenten können [NIP-99](/de/topics/nip-99/) (Classified Listings) Listings lesen und sich mit den bestehenden Zahlungsflüssen aus [NIP-47](/de/topics/nip-47/) (Nostr Wallet Connect) und [NIP-60](/de/topics/nip-60/) (Cashu Wallet) bis zum Checkout bewegen, ohne Seiten zu scrapen oder Client-Verhalten rückwärts zu analysieren.

[Milk Market](https://github.com/shopstr-eng/milk-market), ein Lebensmittel-Marktplatz auf Nostr unter [milk.market](https://milk.market), übernahm dieselbe MCP- und API-Key-Basis in [Commit da6c0b4](https://github.com/shopstr-eng/milk-market/commit/da6c0b499494b4e4861c4ff8a220e066c46285b3). [PR #10](https://github.com/shopstr-eng/milk-market/pull/10) fügt Abo-Bestellungen, Änderungen der Lieferadresse nach dem Kauf sowie Multi-Merchant- und Multi-Währungs-Checkout für Stripe und andere Fiat-Zahlungswege hinzu. Ein nachfolgender [PR #11](https://github.com/shopstr-eng/milk-market/pull/11) behebt einen Initialisierungsfehler der Datenbank beim Start, bei dem auf frischen Installationen die Tabelle für fehlgeschlagene Relay-Publishes nicht angelegt wurde und dadurch beim ersten Laden 500-Fehler entstanden. Die agentenseitige Schnittstelle funktioniert mit Bitcoin-nativem Checkout bei Shopstr oder gemischtem Fiat- und Bitcoin-Checkout bei Milk Market.

### NIP-42-Relay-Auth in Bunker, Signer und Relay

[OAuth Bunker](https://github.com/flox1an/oauth-bunker), ein [NIP-46](/de/topics/nip-46/) (Nostr Connect) Bunker, der OAuth-Provider mit Nostr-Signing verbindet, ergänzte Login per [NIP-07](/de/topics/nip-07/) (Browser Extension Signer), automatische Auswahl einer einzelnen Identität und Aufräumlogik für gelöschte Identitäten ([Commit f0c7683](https://github.com/flox1an/oauth-bunker/commit/f0c7683cb2374fd9a3ebd1b186055da8abd2c2ff)). Wenn nur eine Identität existiert, wählt der Bunker sie jetzt automatisch aus, statt nachzufragen. Wird eine Identität gelöscht, entfernt der Bunker auch ihre verwaisten Zuordnungen und Verbindungen. [Commit 6b8796c](https://github.com/flox1an/oauth-bunker/commit/6b8796c6c59c7d48dc1ede92d6de6bf54feb56cc) ergänzt außerdem einen Konfigurationspfad `ALWAYS_ALLOWED_KINDS` für zugewiesene Nutzer, standardmäßig für kind `30078` app-spezifische Daten, damit delegierte Identitäten in app-spezifischen Speicher schreiben können, ohne pro Event eine Freigabe zu brauchen.

[Amber](https://github.com/greenart7c3/Amber), der wichtigste [NIP-55](/de/topics/nip-55/) Signer für Android, veröffentlichte [v4.1.3-pre4](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3-pre4) mit vier Pre-Releases innerhalb einer Woche. [PR #317](https://github.com/greenart7c3/Amber/pull/317) ergänzt [NIP-42](/de/topics/nip-42/) Relay-Authentifizierung für kind-`22242`-Anfragen. Die Implementierung fügt eine neue Datenbankspalte für relay-spezifische Berechtigungen mit einem eindeutigen Index auf `(pkKey, type, kind, relay)` hinzu. Nutzer sehen einen dedizierten Auth-Bildschirm, auf dem sie Berechtigungen pro Relay oder für alle Relays per Wildcard-`*` gewähren oder verweigern und diese Entscheidung dauerhaft speichern können. Wildcard-Berechtigungen löschen alle relay-spezifischen Einträge für einen Kind. [PR #318](https://github.com/greenart7c3/Amber/pull/318) räumt danach Multi-Event-Anfragebildschirme auf und zeigt Details inline mit Composable Cards statt per Navigation auf einen separaten Screen. Das Release aktualisiert außerdem die Standard-Profil-Relays, ergänzt eine Bottom-Sheet-Darstellung für Anfragen und behebt einen Absturz auf MediaTek-Geräten, indem StrongBox-Keystore deaktiviert wird.

Auf Relay-Seite implementiert [strfry PR #156](https://github.com/hoytech/strfry/pull/156) NIP-42-Auth für [NIP-70](/de/topics/nip-70/) (Protected Events), und [PR #176](https://github.com/hoytech/strfry/pull/176) lehnt Reposts ab, die geschützte Events einbetten.

### Notedeck ergänzt NIP-11-Relay-Limits und Agentium-Funktionen

[Notedeck](https://github.com/damus-io/notedeck), der native Desktop-Client des Damus-Teams, mergte diese Woche 14 PRs. [PR #1316](https://github.com/damus-io/notedeck/pull/1316) ergänzt das Abrufen von [NIP-11](/de/topics/nip-11/) (Relay Information Document) Relay-Limits, sodass alle Outbox-Relays nun `max_message_length` und `max_subscriptions` aus dem Relay-Info-Dokument berücksichtigen. Die Implementierung umfasst Hintergrundjob-Verarbeitung, exponentielles Backoff mit Jitter für Verbindungswiederholungen und benutzerdefinierte HTTP-Accept-Header. [PR #1312](https://github.com/damus-io/notedeck/pull/1312) behebt einen Fehler, bei dem DMs nach dem Account-Wechsel gelegentlich nicht geladen wurden, und [PR #1333](https://github.com/damus-io/notedeck/pull/1333) ergänzt einen Backoff-Mechanismus für die Multicast-Relay-Kommunikation, um Broadcast-Spam bei Fehlern zu vermeiden.

Das Agentium-Subsystem, Notedecks eingebaute UI für Coding-Agenten, intern "Dave" genannt, erhielt Einfügen von Bildern aus der Zwischenablage, benannte Run-Konfigurationen, die über kind-`31991`-Events geräteübergreifend synchronisieren ([NIP-33](/de/topics/nip-33/) (Parameterized Replaceable Events)), einen Git-Worktree-Ersteller und einen Model-Picker zur Auswahl von Backends pro Sitzung ([PR #1336](https://github.com/damus-io/notedeck/pull/1336)). [PR #1338](https://github.com/damus-io/notedeck/pull/1338) integriert `egui_kittest` für headless UI-Tests, und [PR #1339](https://github.com/damus-io/notedeck/pull/1339) ergänzt eine Dashboard-Karte, die neue Kontaktlistenerstellungen nach Client verfolgt. Ein offener [PR #1314](https://github.com/damus-io/notedeck/pull/1314) portiert Amethysts Namecoin-NIP-05-Auflösung nach Notedeck, inklusive ElectrumX-Lookups, SOCKS5-Tor-Routing und Suchleisten-Integration.

### diVine veröffentlicht v1.0.6 mit E2E-Testinfrastruktur und NIP-49-Import

[diVine](https://github.com/divinevideo/divine-mobile), der Shortform-Looping-Video-Client zur Wiederherstellung von Vine-Archiven unter [divine.video](https://divine.video), veröffentlichte [v1.0.6](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.6) mit 127 gemergten PRs. Das Release ergänzt [NIP-49](/de/topics/nip-49/) Account-Import, externe [NIP-05](/de/topics/nip-05/) Unterstützung, Multi-Account-Handhabung, macOS- und experimentelle Linux-Builds sowie eine neu gestaltete Entwurfs- und Clip-Bibliothek auf Basis lokaler Speicherung.

Auf Engineering-Seite ergänzt [PR #1928](https://github.com/divinevideo/divine-mobile/pull/1928) eine vollständige E2E-Integrationstest-Infrastruktur mit Patrol für native UI-Automatisierung gegen einen Docker-Backend-Stack aus Relay, API, Blossom, Postgres, Redis und ClickHouse. Fünf Tests für Auth-Journeys decken Registrierung, Verifizierung, Passwort-Reset, Session-Ablauf und Token-Refresh ab. [PR #2105](https://github.com/divinevideo/divine-mobile/pull/2105) stellt das Laden von Videos von HLS-first auf direktes MP4 mit automatischem HLS-Fallback um und verkürzt die Ladezeit damit von 30-60 Sekunden auf nahezu sofort. [PR #2076](https://github.com/divinevideo/divine-mobile/pull/2076) cached die Home-Feed-API-Antwort in SharedPreferences, damit sie bei Cold Starts sofort angezeigt werden kann. [PR #2104](https://github.com/divinevideo/divine-mobile/pull/2104) erzwingt, dass `ai-generated`-Inhaltskennzeichnungen in Feeds ausgeblendet werden, und [PR #2100](https://github.com/divinevideo/divine-mobile/pull/2100) ergänzt eine Sicherheitseinstellung, die nur von diVine gehostete Videos anzeigt. Die Migration des Profil-Caches von Hive zu Drift läuft weiter über [PR #1881](https://github.com/divinevideo/divine-mobile/pull/1881), [PR #1883](https://github.com/divinevideo/divine-mobile/pull/1883) und [PR #1903](https://github.com/divinevideo/divine-mobile/pull/1903) und ersetzt rund 1.074 Zeilen Hive-Code durch Drift-DAOs.

### Vector v0.3.2 bringt NIP-77-Negentropy-Sync und MLS-Verbesserungen

[Vector](https://github.com/VectorPrivacy/Vector), ein datenschutzorientierter Desktop-Messenger mit MLS-Gruppenverschlüsselung sowie [NIP-17](/de/topics/nip-17/) (Private Direct Messages) und [NIP-44](/de/topics/nip-44/) (Encrypted Payloads), veröffentlichte [v0.3.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.2). Die wichtigste Änderung ist NIP-77-Negentropy für die MLS-Gruppensynchronisierung ([Commit b06adf4](https://github.com/VectorPrivacy/Vector/commit/b06adf4af2673fb5ac5add01356999ea70628eac)), das verpasste Nachrichten per Parallel Boot deutlich schneller nachholt. Das Release ergänzt außerdem eine neu aufgebaute Audio-Engine mit voller Linux-Unterstützung, Bild-Spoiler mit weichgezeichneten Vorschauen, anklickbare Hyperlinks mit Rich-Link-Previews, `@mention`-Pings mit `@everyone` für Gruppenadmins, Emoji-Shortcode-Autocomplete, Gruppenstummschaltung, Tap-to-React auf bestehende Reaktionen und abbrechbare Datei-Uploads. Vector filtert explizit NIP-17-Gruppenchat-Events heraus ([Commit 2179a51](https://github.com/VectorPrivacy/Vector/commit/2179a51c0449b3a70663a1573195b7945adf58ba)) und verwendet MLS ausschließlich für Gruppenverschlüsselung.

## Releases

### Route96 v0.5.0 und v0.5.1

[Route96](https://github.com/v0l/route96), ein Medienserver mit Unterstützung für Blossom und [NIP-96](/de/topics/nip-96/) (HTTP File Storage), veröffentlichte [v0.5.0](https://github.com/v0l/route96/releases/tag/v0.5.0) und [v0.5.1](https://github.com/v0l/route96/releases/tag/v0.5.1). v0.5.0 ergänzt automatisierte KI-Kennzeichnung, rückwirkendes Backfill für unmarkierte Uploads, Moderationswarteschlangen für markierte Dateien, EXIF-basierte Datenschutzablehnung und den Umgang mit gebannten Hashes.

v0.5.1 ergänzt Perceptual Image Hashes, Locality-Sensitive Hashing zur Suche nach ähnlichen Bildern, Batch-Admin-Endpunkte und ein veröffentlichtes [`SKILL.md`](https://github.com/v0l/route96/releases/tag/v0.5.1), das die Blossom- und NIP-96-API-Oberfläche des Servers für Agent-Tooling beschreibt. [PR #58](https://github.com/v0l/route96/pull/58) verschiebt Hintergrund-Worker auf vollständig asynchrone Tokio-Tasks, und [Commit 97b00a3](https://github.com/v0l/route96/commit/97b00a39e27b07053c2ad335dbf475bacba57bf8) ergänzt Backoff, um Hot Loops zu vermeiden.

### Samizdat v1.0.0-alpha

[Samizdat](https://github.com/satsdisco/samizdat), ein Longform-Reader und Publisher unter [samizdat.press](https://samizdat.press), veröffentlichte mit [v1.0.0-alpha](https://github.com/satsdisco/samizdat/releases/tag/v1.0.0-alpha) seinen ersten Android-Build. Die App startet mit einer kuratierten Press-Seite für lange Nostr-Artikel und einer unteren Tab-Navigation für Press, Feed, Gespeichert und Schreiben. Der Android-Build ergänzt native Schlüsselspeicherung per Android-Keystore-Verschlüsselung mit biometrischer Entsperrung, verarbeitet `nostr:`-URIs und `samizdat.press`-Deep-Links und unterstützt die Übergabe an Signer per Android-App-Chooser, Amber, Primal und andere, statt einen direkten Schlüsselimport zu verlangen. Pull-to-Refresh, Safe-Area-Handhabung über verschiedene Bildschirmgrößen hinweg sowie native Share-, Clipboard-, Haptik- und Splash-Screen-Integrationen sind nun Teil der Android-Hülle statt des Web-Wrappers.

[Commit d17308f](https://github.com/satsdisco/samizdat/commit/d17308f3c2e6020e14074fbb1c03a8f60f29a3e6) ergänzt intentbasiertes [NIP-55](/de/topics/nip-55/) Signing für Amber- und Primal-Flows, und [Commit e29dab8](https://github.com/satsdisco/samizdat/commit/e29dab84f7b58edd621f7b86ed7ca6458f965614) ersetzt einen JavaScript-Bridge-Workaround durch ein natives Capacitor-Plugin mit `startActivityForResult`. Die App setzt Android 7.0+ (API 24) voraus, wird in diesem Alpha als Debug-APK ausgeliefert und hat noch keine Push-Benachrichtigungen. Das Veröffentlichen hängt derzeit von einer Signer-App ab, während `nsec`-Login lokales Lesen und Account-Zugriff abdeckt.

### Calendar by Form* v0.2.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar), eine dezentrale Kalender-App mit [NIP-59](/de/topics/nip-59/) (Gift Wrap) für private Event-Freigabe unter [calendar.formstr.app](https://calendar.formstr.app), veröffentlichte [v0.2.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.0) mit [PR #38](https://github.com/formstr-hq/nostr-calendar/pull/38). Das Release erweitert die Behandlung wiederkehrender Events für [NIP-52](/de/topics/nip-52/) (Calendar Events) und geht damit über das Einzelevent-Fundament von v0.1.0 hinaus. Die zugrunde liegenden Änderungen betreffen außerdem lokale Eventspeicherung, Signer-Handhabung und Android-Benachrichtigungslogik. Es ist die zweite aktive Anwendung der Formstr-Organisation nach der Repository-Migration im vergangenen Monat.

### Mostro v0.16.4

[Mostro](https://github.com/MostroP2P/mostro), die Peer-to-Peer-Bitcoin-Börse auf Nostr, veröffentlichte [v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4). Die Wiederherstellung von Dispute-Sessions ([PR #599](https://github.com/MostroP2P/mostro/pull/599)) und die Auto-Close-Fixes ([PR #606](https://github.com/MostroP2P/mostro/pull/606)), die [wir vergangene Woche behandelt haben](/en/newsletters/2026-03-04-newsletter/), sind enthalten. Neu in diesem Release: [PR #625](https://github.com/MostroP2P/mostro/pull/625) ergänzt ein `days`-Feld für User-Rating-Events vom Kind `38384`, [PR #612](https://github.com/MostroP2P/mostro/pull/612) fügt ein Ablaufdatum für diese Rating-Events hinzu, und [PR #614](https://github.com/MostroP2P/mostro/pull/614) stellt Order-Events auf konfigurierte Ablaufwerte statt auf ein hart kodiertes 24-Stunden-Fenster um. [PR #622](https://github.com/MostroP2P/mostro/pull/622) ergänzt eine Idempotenzprüfung, um doppelte Auszahlungen von Development Fees zu verhindern.

### Mostro Mobile v1.2.1

[Mostro Mobile](https://github.com/MostroP2P/mobile), der Flutter-Client für die Mostro-P2P-Börse, veröffentlichte [v1.2.1](https://github.com/MostroP2P/mobile/releases/tag/v1.2.1) mit 11 neuen Features und 11 Bugfixes. Das Release ergänzt die Darstellung verschlüsselter Multimedia-Inhalte im Dispute-Chat ([PR #514](https://github.com/MostroP2P/mobile/pull/514)), automatisches Schließen der Dispute-UI, sobald Orders einen Endzustand erreichen ([PR #503](https://github.com/MostroP2P/mobile/pull/503)), QR-Scanning für NWC-Wallet-Import ([Commit 12eaee4](https://github.com/MostroP2P/mobile/commit/12eaee4d154fa31b07f82b96819de520e825aee6)), französische Übersetzungen und FCM-Push-Benachrichtigungen. [PR #496](https://github.com/MostroP2P/mobile/pull/496) behebt einen Padding-Bug bei Schnorr-Signaturen, indem die bip340-Abhängigkeit auf v0.2.0 festgelegt wird.

### 0xchat v1.5.4

[0xchat](https://github.com/0xchat-app/0xchat-app-main), der Telegram-artige Messaging-Client mit Cashu-Unterstützung, veröffentlichte [v1.5.4](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.4-release), fokussiert auf Linux-Desktop-Fixes: AppImage-Dock-Icons, Emoji-Rendering, Freezes im Kontextmenü und Hänger bei Reply- und Copy-UI. Das Release behebt außerdem Probleme beim Bild-Upload und der npub.cash-Integration. [PR #49](https://github.com/0xchat-app/0xchat-app-main/pull/49) eliminiert unnötige UI-Rebuilds, indem ein 3-Sekunden-Polling-Timer entfernt wird, der glasartige Repaints auslöste, ohne etwas zu tun, und entblockt die Login-Initialisierung, indem der Event-Cache parallel geladen wird, statt Relay-, Kontakt- und Channel-Start zu blockieren.

### Keep v0.6.0

[Keep](https://github.com/privkeyio/keep-android), ein FROST-Threshold-Signer für Android mit Unterstützung für [NIP-55](/de/topics/nip-55/) und [NIP-46](/de/topics/nip-46/), veröffentlichte [v0.6.0](https://github.com/privkeyio/keep-android/releases/tag/v0.6.0) und [v0.6.1](https://github.com/privkeyio/keep-android/releases/tag/v0.6.1). v0.6.0 ergänzt Koordination und UI für Wallet-Deskriptoren, einen Backup-/Restore-Flow mit biometrischer Authentifizierung ([PR #184](https://github.com/privkeyio/keep-android/pull/184)), `nsec`-Recovery aus Threshold-Shares ([PR #187](https://github.com/privkeyio/keep-android/pull/187)), plattformübergreifende Erzeugung animierter QR-Rahmen via Rust UniFFI ([PR #188](https://github.com/privkeyio/keep-android/pull/188)) sowie einen Signing-Audit-Trail mit Chain-Verifikation ([PR #189](https://github.com/privkeyio/keep-android/pull/189)). v0.6.1 stellt die Lizenz von AGPL-3.0 auf MIT um ([PR #191](https://github.com/privkeyio/keep-android/pull/191)).

### njump v0.3.0

[njump](https://github.com/fiatjaf/njump), das statische Gateway zum Anzeigen von Nostr-Inhalten unter [njump.me](https://njump.me), veröffentlichte [v0.3.0](https://github.com/fiatjaf/njump/releases/tag/v0.3.0) mit einer Breaking Change beim Parsen von `note1`-Codes und einem Update der zugrunde liegenden nostr-Bibliothek.

### Roadstr v0.1.1

[Roadstr](https://github.com/jooray/roadstr), eine dezentrale App zur Meldung von Straßenereignissen auf Nostr, veröffentlichte ihre erste Demo-Version [v0.1.1](https://github.com/jooray/roadstr/releases/tag/v0.1.1). Die App zeigt Straßenereignisse auf einer Karte an und verwendet dazu Vector Tiles von openfreemap.org.

### Bitcredit v0.5.3

[Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core), eine E-Bill-Anwendung mit Nostr-Transportebene und eigenem Relay unter [bit.cr](https://www.bit.cr/), veröffentlichte [v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3). [PR #846](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846) ergänzt `payment_actions`- und `bill_state`-Felder in der API für Zahlungs- und Annahmestatus, und [PR #849](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849) behebt die Behandlung von Signing-Adressen für anonyme Signer.

### OpenChat v0.1.0-alpha.3

[OpenChat](https://github.com/DavidGershony/openChat), eine Chat-Anwendung auf den .NET-MLS- und C#-Bibliotheken des Marmot-Protokolls, veröffentlichte [v0.1.0-alpha.3](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.3). Das Release ergänzt externe Signer-Unterstützung für Amber- und [NIP-46](/de/topics/nip-46/)-Flows ([Commit e568d97](https://github.com/DavidGershony/openChat/commit/e568d979fe15eead19172f2eb6f8cf26ca845247)), verlagert die Persistenz des MLS-Zustands in den MLS-Service, um Datenverlustfenster bei Abstürzen zu beseitigen ([Commit 4720bc8](https://github.com/DavidGershony/openChat/commit/4720bc8625136a0d5b0e23322bc0c50cd80577e8)), und veröffentlicht Windows-, Linux- und Android-Builds über eine neue CI-Pipeline.

### OpenSignal v1.0.0

[OpenSignal](https://github.com/turizspace/opensignal), ein Kotlin-Multiplatform-Trading-Copilot für Nostr, veröffentlichte [v1.0.0](https://github.com/turizspace/OpenSignal/releases/tag/v1.0.0). Das Release bündelt geteilte KMP-Module für Domain-Logik, Chart-Rendering, Nostr-Authentifizierung und -Publishing, Blossom-[NIP-96](/de/topics/nip-96/) Upload-Unterstützung sowie ONNX-basierte KI-Inferenz-Hooks über Desktop- und Android-Shells hinweg. Die veröffentlichte Architektur umfasst außerdem einen FastAPI-KI-Service zur Analyse von Chart-Screenshots, Model-Training-Pipelines und eine Risk-Engine, die strukturierte Trade-Pläne mit Sizing und Warnungen erzeugt. Der Login unterstützt entweder rohe `nsec`-Keys oder externe Signer, und der Output-Fluss endet beim Publizieren von Nostr-Events statt bei rein lokaler Analyse.

## Projekt-Updates

### Formstr

[Formstr](https://github.com/formstr-hq/nostr-forms), die Google-Forms-Alternative auf Nostr, mergte [PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) ([Commit e9c4fd5](https://github.com/formstr-hq/nostr-forms/commit/e9c4fd5dadfa0b83f1e87d7596eaf35f9fdb7da8)) und ergänzt damit einen Registrierungsflow mit [NIP-49](/de/topics/nip-49/) verschlüsselten privaten Schlüsseln. Vor dieser Änderung brauchten Nutzer entweder eine [NIP-07](/de/topics/nip-07/) Browser-Erweiterung oder ein eingefügtes rohes `nsec`, um Formstr zu nutzen. Der neue Flow erzeugt das Schlüsselpaar clientseitig, verschlüsselt den privaten Schlüssel mit einem vom Nutzer gewählten Passwort nach NIP-49 mit scrypt + XChaCha20-Poly1305 und speichert die daraus entstehende `ncryptsec`-Zeichenkette. Nutzer können sich dann später mit ihrem Passwort wieder anmelden, ohne eine Signer-Erweiterung zu installieren. Das Schlüsselmanagement bleibt während des gesamten Prozesses clientseitig.

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst), der funktionsreiche Android-Client, mergte vier PRs, die die Namecoin-gestützte [NIP-05](/de/topics/nip-05/) Auflösung ausliefern, die [letzte Woche noch offen war](/en/newsletters/2026-03-04-newsletter/). [PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734) ergänzt zensurresistente NIP-05-Verifizierung über ElectrumX für `.bit`-, `d/`- und `id/`-Identifikatoren. Wenn Amethyst eines dieser Suffixe in einem NIP-05-Feld erkennt, fragt es einen ElectrumX-NMC-Server nach der Transaktionshistorie des Namens ab, parst das `NAME_UPDATE`-Script aus dem neuesten Output, um den Nostr-Pubkey zu extrahieren, und lehnt Namen ab, die älter als 36.000 Blöcke sind, das Ablauf-Fenster von Namecoin. ElectrumX-Verbindungen laufen über SOCKS5, wenn Tor aktiviert ist, und die Serverauswahl wechselt dynamisch zwischen Clearnet- und `.onion`-Endpunkten. Ein LRU-Cache mit einer Stunde TTL verhindert wiederholte Blockchain-Abfragen.

[PR #1771](https://github.com/vitorpamplona/amethyst/pull/1771) behebt Race Conditions und verbessert die Korrektheit des Resolvers in diesem Flow. [PR #1785](https://github.com/vitorpamplona/amethyst/pull/1785) erlaubt neuen Nutzern, beim Signup eine Follow-Liste entweder aus gewöhnlichen NIP-05-Identifikatoren oder aus Namecoin-basierten zu importieren. [PR #1786](https://github.com/vitorpamplona/amethyst/pull/1786) ergänzt benutzerdefinierte ElectrumX-Servereinstellungen, sodass Nutzer auswählen können, welcher Server ihre Lookups bearbeitet.

### nostr-idb

[nostr-idb](https://github.com/hzrd149/nostr-idb), eine Bibliothek mit Hilfsmethoden zum Speichern von Nostr-Events in IndexedDB, mergte [PR #6](https://github.com/hzrd149/nostr-idb/pull/6) und ergänzt damit Unterstützung für [NIP-91](/de/topics/nip-91/) AND-Tag-Filter. Die Änderung fügt der clientseitigen Filterlogik Schnittmengen-Semantik hinzu, sodass IndexedDB-Abfragen alle aufgelisteten Tag-Werte statt nur einen davon verlangen können. [PR #8](https://github.com/hzrd149/nostr-idb/pull/8) aktualisiert die Bibliothek auf die neueste NIP-DB-Schnittstelle, und ein nachfolgender [Commit b49b3d3](https://github.com/hzrd149/nostr-idb/commit/b49b3d32c575ff8214dc3fb07675109c2a971972) behebt einen Subscribe-Deadlock und entfernt nostr-tools als Produktionsabhängigkeit.

### Pensieve

[Pensieve](https://github.com/andotherstuff/pensieve), ein archive-first Nostr-Indexer mit ClickHouse-Analytics, mergte [PR #8](https://github.com/andotherstuff/pensieve/pull/8) und ergänzt damit Durchsetzung von Cache-TTL pro Eintrag sowie Miss-Coalescing pro Schlüssel, um CPU-Spitzen in der API zu reduzieren. Die teuersten Time-Series-Endpunkte, Engagement-Statistiken, stündliche Aktivität und Aktivität pro Kind, verwenden nun serverseitige TTLs von zehn Minuten, statt synchronisierte Neuberechnungsstürme auszulösen.

### Blossom

[Blossom](https://github.com/hzrd149/blossom), das dezentrale Medienhosting-Protokoll und der zugehörige Server-Stack, mergte zwei BUD-11-Autorisierungsupdates. [PR #91](https://github.com/hzrd149/blossom/pull/91) verschiebt optionale Autorisierung in einen eigenen BUD und präzisiert die Rolle der Tags `x` und `server`. [PR #93](https://github.com/hzrd149/blossom/pull/93) räumt endpoint-spezifisches Auth-Verhalten auf und formalisiert den Header `X-SHA-256` zur Upload-Verifikation. Die beiden PRs konsolidieren die Auth-Logik in BUD-11 und entfernen Unklarheiten beim Hashing von Requests für Upload-, Delete- und Medienverwaltungsflüsse.

## NIP-Updates

Aktuelle Änderungen im [NIPs-Repository](https://github.com/nostr-protocol/nips):

**Gemergt:**

- **[NIP-91](/de/topics/nip-91/) (AND Operator for Filters)** ([PR #1365](https://github.com/nostr-protocol/nips/pull/1365)): Fügt Schnittmengen-Semantik für Tag-Filter hinzu, sodass Relays Abfragen beantworten können, die alle aufgelisteten Tag-Werte statt nur eines davon verlangen. Das reduziert clientseitiges Post-Filtering und Bandbreite bei taglastigen Abfragen.

- **[NIP-66](/de/topics/nip-66/) (Relay Discovery and Liveness Monitoring): Defensive Measures** ([PR #2240](https://github.com/nostr-protocol/nips/pull/2240)): Nach der [Outbox-Benchmark-Arbeit aus der vergangenen Woche](/en/newsletters/2026-03-04-newsletter/) ergänzt die Spezifikation nun Warnhinweise für schwierige Pfade bei Relay-Monitoring-Daten. Clients dürfen kind-`30166`-Monitoring-Events nicht voraussetzen, um zu funktionieren. Ein Monitor kann falsch, veraltet oder böswillig sein. Clients sollen Quellen gegeneinander prüfen und nicht auf Grundlage eines einzelnen Feeds große Teile des Relay-Graphs eines Nutzers abschneiden.

- **[NIP-39](/de/topics/nip-39/) (External Identities in Profiles): kind 10011 Registry Cleanup** ([PR #2256](https://github.com/nostr-protocol/nips/pull/2256)): Ergänzt die Referenz auf kind `10011` direkt in der Spezifikation und richtet sie damit an Amethysts Implementierung aus, die [wir vergangene Woche behandelt haben](/en/newsletters/2026-03-04-newsletter/).

**Offene PRs und Diskussionen:**

- **[NIP-70](/de/topics/nip-70/) (Protected Events): Reject reposts that embed protected events** ([PR #2251](https://github.com/nostr-protocol/nips/pull/2251)): Wenn ein Relay NIP-70 für das Original-Event durchsetzt, aber Reposts mit demselben Inhalt akzeptiert, hat das `-`-Tag praktisch keine Wirkung. Dieser PR ergänzt daher die Regel, dass Relays auch Reposts der Kinds 6 und 16 von geschützten Events ablehnen müssen. [strfry PR #176](https://github.com/hoytech/strfry/pull/176) implementiert das bereits.

- **[NIP-71](/de/topics/nip-71/) (Video Events): Multiple Audio Tracks** ([PR #2255](https://github.com/nostr-protocol/nips/pull/2255)): Ergänzt Audio-`imeta`-Tags für alternative Tonspuren, Sprachvarianten und reine Audio-Streams. Ein Client könnte damit dieselbe Videodatei behalten und nur die Audiosprache wechseln oder Audio als separate Spur für podcastartige Inhalte ausliefern.

- **[NIP-11](/de/topics/nip-11/) (Relay Information Document) und [NIP-66](/de/topics/nip-66/) Relay Attributes** ([PR #2257](https://github.com/nostr-protocol/nips/pull/2257)): Ergänzt ein strukturiertes `attributes`-Feld in Relay-Informationsdokumenten und gibt Clients sowie Discovery-Tools damit maschinenlesbare Metadaten zusätzlich zur bisherigen Freitextbeschreibung.

## NIP Deep Dive: NIP-49 (Private Key Encryption)

[NIP-49](/de/topics/nip-49/) definiert, wie ein Client einen privaten Schlüssel mit einem Passwort verschlüsselt und das Ergebnis als `ncryptsec`-bech32-Zeichenkette kodiert. [Formstr](#formstr) verwendet NIP-49 in seinem neuen Registrierungsflow.

Das Format ist nicht an einen speziellen Event-Kind gebunden. Ein Client startet mit dem rohen 32-Byte-secp256k1-Privatschlüssel, leitet per scrypt aus dem Passwort einen symmetrischen Schlüssel ab, verschlüsselt den Schlüssel mit XChaCha20-Poly1305 und verpackt das Ergebnis anschließend in eine bech32-`ncryptsec`-Zeichenkette. Ein Ein-Byte-Flag speichert, ob der Schlüssel vor der Verschlüsselung irgendwann bekanntermaßen unsicher behandelt wurde.

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

Das obige JSON-Event ist ein Anwendungsbeispiel, keine Anforderung von NIP-49. Der NIP standardisiert das Format des verschlüsselten Schlüssels. Ein Client kann das `ncryptsec` lokal speichern, über app-spezifischen Speicher synchronisieren oder als Backup-String exportieren. Passwörter werden vor der Schlüsselableitung nach Unicode NFKC normalisiert, damit dasselbe Passwort über Clients und Plattformen hinweg konsistent entschlüsselt wird.

Für das Ein-Byte-Flag zur Schlüsselsicherheit sind drei Werte definiert: `0x00` bedeutet, dass die Behandlungshistorie des Schlüssels unbekannt ist, `0x01` bedeutet, dass der Schlüssel bekanntermaßen unsicher behandelt wurde, zum Beispiel als Klartext in ein Webformular eingefügt, bevor er verschlüsselt wurde, und `0x02` bedeutet, dass der Schlüssel in einem sicheren Kontext erzeugt und verschlüsselt wurde und nie offengelegt war. Clients können diese Information nutzen, um beim Import von Schlüsseln mit bekannter unsicherer Historie Warnungen anzuzeigen.

NIP-49 schützt Schlüssel besser als ein Klartext-`nsec`-Export, aber die Verschlüsselung ist nur so stark wie das Passwort und der konfigurierte scrypt-Kostenfaktor. Höhere `LOG_N`-Werte erschweren Offline-Erraten, verlangsamen aber auch legitime Entschlüsselungsvorgänge. Die Spezifikation warnt davor, verschlüsselte Schlüssel auf öffentliche Relays zu veröffentlichen, weil Angreifer davon profitieren, Ciphertext für Offline-Cracking zu sammeln. Zum Vergleich vermeidet [NIP-46](/de/topics/nip-46/) Remote-Signing die Exposition von Schlüsseln vollständig, und [NIP-55](/de/topics/nip-55/) Android-Signing hält Schlüssel innerhalb einer dedizierten Signer-App. NIP-49 besetzt einen anderen Platz: portables verschlüsseltes Backup für Nutzer, die ihre Schlüssel selbst verwalten.

Implementierungen umfassen [Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434) für den Signup, [Amber](https://github.com/greenart7c3/Amber) für `ncryptsec`-Backup und -Restore, [diVine v1.0.6](#divine-veroffentlicht-v106-mit-e2e-testinfrastruktur-und-nip-49-import) für den Account-Import, [Keep v0.6.0](#keep-v060) für den Export von FROST-Shares sowie Key-Management-Tools wie [nsec.app](https://nsec.app) und [Alby](https://github.com/getAlby/hub).

## NIP Deep Dive: NIP-70 (Protected Events)

[NIP-70](/de/topics/nip-70/) definiert geschützte Events. Wenn ein Event das Tag `["-"]` trägt, muss ein Relay es ablehnen, sofern das Relay nicht [NIP-42](/de/topics/nip-42/) Authentifizierung verlangt und der authentifizierte Pubkey mit dem Autor des Events übereinstimmt.

Der NIP-42-Auth-Flow läuft so ab: Das Relay sendet eine `AUTH`-Challenge mit einem zufälligen String, und der Client antwortet mit einem signierten kind-`22242`-Event, dessen Tags die Relay-URL und die Challenge enthalten. Das Relay prüft die Signatur und verifiziert, dass der Pubkey im Auth-Event dem Pubkey im zu publizierenden geschützten Event entspricht. Stimmen die Pubkeys nicht überein, lehnt das Relay das Event mit einem `restricted`-Präfix in der Fehlermeldung ab.

Der Event-Inhalt kann weiterhin öffentlich sein. Das `-`-Tag steuert nur, wer das Event zu einem Relay veröffentlichen darf, das dieses Tag respektiert. Das deckt [NIP-29](/de/topics/nip-29/) (Simple Groups) halbgeschlossene Feeds, Relay-Räume nur für Mitglieder und andere Kontexte ab, in denen der Autor die Weiterverbreitung über den Relay-Graphen begrenzen will. NIP-70 ist eine Ein-Tag-Konvention, kein neuer Event-Kind, daher kann jeder bestehende Event-Kind das `-`-Tag tragen.

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

Selbst wenn ein Relay die Veröffentlichung des Original-Events durch Dritte blockiert, kann jemand den Inhalt in einem Repost erneut veröffentlichen. [PR #2251](https://github.com/nostr-protocol/nips/pull/2251) adressiert das, indem Relays auch Reposts der Kinds 6 und 16 von geschützten Events ablehnen müssen. [strfry PR #156](https://github.com/hoytech/strfry/pull/156) ergänzt NIP-42-Auth für geschützte Events, und [strfry PR #176](https://github.com/hoytech/strfry/pull/176) blockiert Reposts, die geschützte Inhalte einbetten.

NIP-70 steuert Relay-Verhalten. Ein Empfänger kann den Inhalt trotzdem anderswo kopieren, und die Spezifikation sagt das auch ausdrücklich. Das `-`-Tag gibt Relays ein maschinenlesbares Signal, die Wiederveröffentlichung zu verweigern. Zum Vergleich bittet [NIP-62](/de/topics/nip-62/) (Request to Vanish) Relays, Daten nachträglich zu löschen, während NIP-70 unautorisierte Veröffentlichung bereits bei der Annahme verhindert. Beide ergänzen sich: Ein Autor kann Events als geschützt markieren, um ihre Verbreitung zu begrenzen, und später zusätzlich Löschung verlangen, wenn Inhalte von Relays entfernt werden sollen, die sie bereits akzeptiert hatten.

---

Das war es für diese Woche. Baust du etwas oder hast du Neuigkeiten, die wir kennen sollten? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Melde dich per [NIP-17](/de/topics/nip-17/) DM</a> oder finde uns auf Nostr.
