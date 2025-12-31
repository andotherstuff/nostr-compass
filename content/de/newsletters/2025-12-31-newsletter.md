---
title: 'Nostr Compass #3'
date: 2025-12-31
publishDate: 2025-12-31
translationOf: /en/newsletters/2025-12-31-newsletter.md
translationDate: 2025-12-31
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, Ihrem wöchentlichen Leitfaden zum Nostr-Protokoll-Ökosystem.

**Diese Woche:** Zum Abschluss des Jahres 2025 blicken wir auf fünf Jahre Dezember-Meilensteine in der Evolution von Nostr zurück. Von fiatjafs erster Client-Veröffentlichung im Dezember 2020, über Jack Dorseys wegweisende 14-BTC-Spende im Dezember 2022, bis zur NIP-55-Signer-Verbreitung und NDKs 162-facher Cache-Beschleunigung in diesem Monat - der Dezember hat konsequent Wendepunkte für das Protokoll markiert. Diese Sonderausgabe zeichnet die technische Geschichte durch jeden Dezember nach und dokumentiert das Wachstum des Protokolls von zwei experimentellen Relays zu über 2.500 Knoten in 50 Ländern. Außerdem: Amethysts Desktop-Modul nimmt durch Quartz Gestalt an, Notedeck erhält Messaging, Citrine hostet Web-Apps und NIP-54 behebt die Internationalisierung für nicht-lateinische Schriften.

## Dezember-Rückblick: Fünf Jahre Nostr-Dezember

Nostr wird dieses Jahr fünf. fiatjaf startete das Protokoll am 7. November 2020, und jeder Dezember seither markierte eine eigenständige Phase seiner Entwicklung: vom Proof-of-Concept zur globalen Bewegung zum Produktions-Ökosystem. Dies ist ein technischer Rückblick von Dezember 2020 bis Dezember 2025, die prägenden Jahre, die Nostrs Grundlage etablierten und seinen Durchbruch katalysierten.

### Dezember 2020: Genesis

Der erste vollständige Monat von Nostrs Existenz sah fiatjaf [Branle](https://github.com/fiatjaf/branle) veröffentlichen, den ersten Client des Protokolls, gebaut mit Quasar (Vue.js) und absurd-sql für lokale Speicherung. fiatjaf hatte bereits die Kernarchitektur etabliert: Benutzer identifiziert durch secp256k1-Public-Keys, alle Posts kryptografisch signiert, Relays dienen als einfache Speicher, die nicht miteinander kommunizieren. Ein oder zwei experimentelle Relays bedienten eine Handvoll frühe Anwender, die sich in der Telegram-Gruppe [@nostr_protocol](https://t.me/nostr_protocol) koordinierten, die am 16. November gestartet war. Die [ursprüngliche Dokumentation](https://fiatjaf.com/nostr.html) beschrieb "das einfachste offene Protokoll, das in der Lage ist, ein zensurresistentes globales soziales Netzwerk zu schaffen" - eine Prämisse, deren Beweis noch zwei weitere Jahre dauern sollte.

### Dezember 2021: Frühe Entwicklung

Am 31. Dezember 2021 erreichte Nostr die [Hacker-News-Titelseite](https://news.ycombinator.com/item?id=29749061) mit 110 Punkten und 138 Kommentaren, eingereicht von Cameri. Dies markierte die erste bedeutende Exposition des Protokolls gegenüber der breiteren Entwickler-Community. Das Netzwerk lief auf etwa sieben Relays mit weniger als 1.000 Benutzern. Branle erhielt Updates einschließlich Private-Key-Import (31. Dezember) und Multi-Relay-Unterstützung. Ein Kommandozeilen-Client, noscl, bot Terminal-basierte Interaktion. Die Protokollspezifikationen existierten in fiatjafs Dokumentation, obwohl das formelle [NIPs-Repository](https://github.com/nostr-protocol/nips) erst im Mai 2022 erstellt werden würde. Das Protokoll war, wie fiatjaf es beschrieb, "ein Work in Progress".

### Dezember 2022: Der Wendepunkt

Dezember 2022 transformierte Nostr von einem Nischenexperiment in eine Mainstream-Bewegung. Der Katalysator kam am 15. Dezember, als Jack Dorsey [14,17171699 BTC](https://www.coindesk.com/tech/2022/12/15/jack-dorsey-gives-decentralized-social-network-nostr-14-btc-in-funding) (~245.000-250.000 $) an fiatjaf spendete, nachdem er das Protokoll entdeckt und erklärt hatte, es sei "100 Prozent das, was wir von Bluesky wollten, aber es wurde nicht von einer Firma entwickelt". Am 16. Dezember kündigte fiatjaf an, die Mittel mit Damus-Entwickler William Casarin (jb55) zu teilen, und Dorsey verifizierte sein Nostr-Konto (npub: `npub1sg6plzptd64u62a878hep2kev88swjh3tw00gjsfl8f237lmu63q0uf63m`). Die Finanzierung legitimierte das Projekt über Nacht.

In derselben Woche beschleunigte Twitters Chaos die Adoption. Am 14.-15. Dezember gab es Suspendierungen prominenter Journalisten von der New York Times, CNN und Washington Post. Am 18. Dezember [kündigte Twitter Verbote](https://techcrunch.com/2022/12/18/twitter-wont-let-you-post-your-facebook-instagram-and-mastodon-handles/) für Konten an, die Nostr, Mastodon und andere Plattformen bewarben. Die Richtlinie wurde am folgenden Tag nach Gegenwehr zurückgenommen. Der Exodus trieb Benutzer dazu, Alternativen zu erkunden.

Die Protokollentwicklung beschleunigte sich. Am 16. Dezember wurde [NIP-19](/de/topics/nip-19/) gemerged ([#57](https://github.com/nostr-protocol/nips/pull/57)), das bech32-kodierte Identifikatoren (npub, nsec, note, nprofile, nevent) einführte, die Schlüssel menschenlesbar und unterscheidbar machten. Das NIPs-Repository verzeichnete in diesem Monat 36+ Commits, einschließlich Updates für NIP-40 und NIP-07. Clients vermehrten sich: Damus füllte seine TestFlight-Beta innerhalb von Stunden, Astral forkte Branle für die Profilerstellung, Snort startete als "schneller, zensurresistenter" Web-Client, und Vitor Pamplona begann die Amethyst-Entwicklung. Alby v1.22.1 "Kemble's Cascade of Stars" wurde am 22. Dezember mit NIP-19-Unterstützung ausgeliefert. Bis zum 7. Dezember hatte Nostr etwa 800 Benutzer mit Profilen; als Damus am 31. Januar 2023 den App Store erreichte, öffneten sich die Schleusen und trieben das Wachstum bis Juni 2023 auf über 315.000 Benutzer.

### Dezember 2023: Ökosystem-Reifung

Dezember 2023 markierte einen kritischen Wendepunkt für die Sicherheit des Nostr-Protokolls. Am 20. Dezember wurde [NIP-44 Revision 3 gemerged](https://github.com/nostr-protocol/nips/pull/746) nach einem unabhängigen Cure53-Sicherheitsaudit (NOS-01), das 10 Probleme in den TypeScript-, Go- und Rust-Implementierungen identifizierte, einschließlich Timing-Attacken und Forward-Secrecy-Bedenken. Die aktualisierte Spezifikation ersetzte die fehlerhafte [NIP-04](/de/topics/nip-04/)-Verschlüsselung durch ChaCha20 und HMAC-SHA256 und etablierte die kryptografische Grundlage, die jetzt [NIP-17](/de/topics/nip-17/) private DMs und [NIP-59](/de/topics/nip-59/) Gift Wrapping untermauert. In derselben Woche kündigte [OpenSats ihre vierte Grant-Welle](https://opensats.org/blog/nostr-grants-december-2023) am 21. Dezember an und finanzierte sieben Projekte einschließlich Lume, noStrudel, ZapThreads und ein unabhängiges NIP-44-Audit. Dies folgte der [ersten Welle im Juli 2023](https://opensats.org/blog/nostr-grants-july-2023), die Damus, Coracle, Iris und andere finanziert hatte, und brachte die Gesamtzuweisung des Nostr-Fonds auf etwa 3,4 Millionen Dollar über 39 Grants.

Der Monat offenbarte auch Nachhaltigkeitsspannungen im Ökosystem. Am 28. Dezember [postete William Casarin (jb55) auf Stacker News](https://stacker.news/items/368863), dass 2024 "wahrscheinlich das letzte Jahr von Damus" sein werde, und führte an, dass "Nostr-Clients kein Geld verdienen", nachdem Apples Einschränkungen bei In-App-Zaps das Umsatzpotenzial stark limitiert hatten. Das Damus-Team hatte zuvor VC-Finanzierung abgelehnt. Unterdessen wurde [Nostr Wallet Connect v0.4.1](https://github.com/getAlby/nostr-wallet-connect/releases/tag/0.4.1) am 26. Dezember ausgeliefert und erweiterte [NIP-47](/de/topics/nip-47/) mit `pay_keysend`, `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance` und `get_info`-Methoden, was den Grundstein für die Wallet-Integrationen legte, die zum Standard über alle Clients werden sollten.

### Dezember 2024: Protokoll-Fortschritt

Dezember 2024 begann mit dem [Notedeck Alpha-Launch](https://damus.io/notedeck/) am 30. November, dem Rust-basierten Desktop-Client des Damus-Teams mit einer mehrspaligen Oberfläche und Unterstützung mehrerer Konten. Gebaut für Linux, macOS und Windows (Android für 2025 geplant), wurde Notedeck zunächst an Damus-Purple-Abonnenten ausgeliefert und stellte eine strategische Expansion über iOS hinaus dar. Zwei Wochen später kündigte [OpenSats ihre neunte Grant-Welle](https://opensats.org/blog/9th-wave-of-nostr-grants) am 16. Dezember an und finanzierte AlgoRelay (das erste algorithmische Relay für personalisierte Feeds), Pokey (Android-App mit Bluetooth-Mesh für eingeschränktes Internet), Nostr Safebox ([NIP-60](/de/topics/nip-60/) Cashu-Token-Speicherung) und LumiLumi (leichtgewichtiger barrierefreier Web-Client), was die Gesamtzuweisung des Nostr-Fonds auf etwa 9 Millionen Dollar brachte - ein Anstieg von 67% im Jahresvergleich.

Der Monat sah signifikante Client-Reifung im gesamten Ökosystem. [Gossip 0.13.0](https://github.com/mikedilger/gossip/releases/tag/v0.13.0) landete am 23. Dezember mit File-Metadata-Unterstützung ([NIP-92](/de/topics/nip-92/)/[NIP-94](/de/topics/nip-94/)), Blossom-Integration und [NIP-50](/de/topics/nip-50/) Relay-Suche. [Coracle 0.5.0](https://github.com/coracle-social/coracle/releases/tag/0.5.0) wurde am 12. Dezember mit überarbeitetem Onboarding und nostr-editor-Integration ausgeliefert. Die Protokollentwicklung blieb aktiv mit 30 Pull Requests zwischen dem 9. und 22. Dezember (10 gemerged), einschließlich [NIP-46](/de/topics/nip-46/)-Umschreibungen zur ausschließlichen Verwendung von NIP-44-Verschlüsselung und fortgesetzter Arbeit an [NIP-104](/de/topics/nip-104/) für Double-Ratchet-Verschlüsselung auf Signal-Niveau. Netzwerkstatistiken zeigten über 224.000 tägliche Trusted-Pubkey-Events, 4-faches Jahreswachstum bei neuen Profilen mit Kontaktlisten und einen 50%igen Anstieg bei öffentlichen Schreib-Events.

### Dezember 2025: Ökosystem-Expansion

Dezember 2025 brachte fortgesetzte Protokollreifung und Ökosystem-Expansion. Am 21. Dezember kündigte [OpenSats ihre vierzehnte Nostr-Grant-Welle](https://opensats.org/blog/fourteenth-wave-of-nostr-grants) an und finanzierte drei Projekte: YakiHonne (ein Multi-Plattform-Client mit Creator-Portal für Long-Form-Content und Cashu/Nutzaps-Zahlungsintegration), Quartz (Vitor Pamplonas Kotlin-Multiplatform-Bibliothek, die Amethyst antreibt und eine iOS-Version ermöglichen wird) und Nostr Feedz (bidirektionale RSS-zu-Nostr-Integration von PlebOne). Grant-Verlängerungen gingen an Dart NDK und Mattns nostr-relay.

Die Protokollevolution setzte sich fort mit [NIP-BE](/de/topics/nip-be/) (Bluetooth Low Energy Messaging, [#1979](https://github.com/nostr-protocol/nips/pull/1979)), das im November gemerged wurde und Offline-Gerätesynchronisation ermöglicht. [NIP-A4](/de/topics/nip-a4/) (Public Messages, kind 24, [#1988](https://github.com/nostr-protocol/nips/pull/1988)) landete später im Monat und definierte Benachrichtigungsbildschirm-Nachrichten, die `q`-Tags verwenden, um Threading-Komplikationen zu vermeiden. [NIP-29](/de/topics/nip-29/) erhielt größere Klärung ([#2106](https://github.com/nostr-protocol/nips/pull/2106)) und führte das `hidden`-Tag für wirklich private, nicht auffindbare Gruppen ein. Die [NIP-55](/de/topics/nip-55/)-Spezifikation sah ebenfalls Verfeinerung ([#2166](https://github.com/nostr-protocol/nips/pull/2166)) und adressierte einen häufigen Implementierungsfehler, bei dem Entwickler `get_public_key` aus Hintergrundprozessen aufriefen.

Auf der Client-Seite wurde [Primal Android zu einem vollständigen NIP-55-Signer](/de/newsletters/2025-12-24-newsletter/#news) durch acht gemergte PRs, die `LocalSignerContentProvider` implementierten, und schloss sich Amber und Aegis als Android-Signing-Optionen an. Die [NDK-Bibliothek erreichte 162-mal schnellere Cache-Abfragen](/de/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes) (von ~3.690ms auf ~22ms) durch Eliminierung doppelter Schreibvorgänge und unnötige LRU-Cache-Lookups ([PR #371](https://github.com/nostr-dev-kit/ndk/pull/371), [PR #372](https://github.com/nostr-dev-kit/ndk/pull/372)). Shopstr führte [Zapsnags](/de/newsletters/2025-12-24-newsletter/#news) für Flash-Sales via zaps ein. White Noise lieferte datenschutzfreundliche Push-Benachrichtigungen mit [MIP-05](/de/topics/mip-05/). Siehe [Newsletter #1](/de/newsletters/2025-12-17-newsletter/) und [Newsletter #2](/de/newsletters/2025-12-24-newsletter/) für vollständige Berichterstattung.

---

Vor fünf Jahren veröffentlichte fiatjaf Branle für eine Handvoll Benutzer über zwei experimentelle Relays. Heute unterstützt das Protokoll 140+ Clients, 2.500+ Relays in 50 Ländern und ein wachsendes Web of Trust, das Hunderttausende von Keypairs verbindet. Dezembersmuster grosser Veröffentlichungen setzte sich diesen Monat fort mit Bluetooth-Messaging, Android-Signer-Verbreitung und Infrastruktur-Grants, die nachhaltige Investitionen in plattformübergreifende Tools signalisieren.

## Neuigkeiten

**Amethyst Desktop nimmt Gestalt an** - Der Quartz-Grant aus OpenSats' vierzehnter Welle produziert bereits Ergebnisse. [PR #1625](https://github.com/vitorpamplona/amethyst/pull/1625) erstellt ein vollständiges `:desktopApp`-Modul für Amethyst mit Compose Multiplatform, mit funktionierenden Login- und Global-Feed-Bildschirmen auf Desktop JVM. Die Architektur konvertiert das `:commons`-Modul zu Kotlin Multiplatform mit einer sauberen Source-Set-Struktur (`commonMain`, `jvmAndroid`, `androidMain`, `jvmMain`), die gemeinsame UI-Komponenten zwischen Android und Desktop ermöglicht, während plattformspezifische Entscheidungen jedem Target überlassen werden. Dies legt den Grundstein für die eventuelle iOS-Version über denselben Kotlin-Multiplatform-Ansatz.

**Amethyst Sprachantworten** - Eine Weihnachtslieferung von davotoula: [PR #1622](https://github.com/vitorpamplona/amethyst/pull/1622) fügt dedizierte Sprachantwort-Bildschirme mit Wellenform-Visualisierung, Neuaufnahme-Unterstützung, Medienserver-Auswahl und Upload-Fortschrittsanzeigen hinzu. Benutzer können jetzt sowohl auf Root-Sprachnachrichten als auch auf Sprachantworten mit Audio antworten.

**Notedeck fügt Messaging hinzu** - Notedeck, der Damus-Desktop-Client, erhielt eine Nachrichtenfunktion in [PR #1223](https://github.com/damus-io/notedeck/pull/1223), die über Timeline-Browsing hinaus in direkte Kommunikation expandiert.

**Citrine hostet Web-Apps** - Citrine kann jetzt [Web-Anwendungen hosten](https://github.com/greenart7c3/Citrine/pull/81) und verwandelt Ihr Telefon in einen Local-First-Nostr-Webserver. Ein separater [PR #85](https://github.com/greenart7c3/Citrine/pull/85) fügt automatische Neuverbindung und Event-Broadcasting hinzu, wenn die Netzwerkkonnektivität zurückkehrt, mit umfassender Testabdeckung über Android-API-Levels.

**Nostrability Developer Toolkit Registry** - Der [Developer Kits & Tooling](https://github.com/nostrability/nostrability/issues/264)-Tracker pflegt ein kuratiertes Register von SDKs, Bibliotheken und Entwicklertools über Sprachen hinweg (TypeScript, Rust, Python, Go, Dart, Swift und mehr). Wenn Sie neu in der Nostr-Entwicklung sind, ist dies ein nützlicher Ausgangspunkt, um das richtige Toolkit für Ihren Stack zu finden.

## NIP-Updates

Aktuelle Änderungen am [NIPs-Repository](https://github.com/nostr-protocol/nips):

- **[NIP-54](/de/topics/nip-54/)** - Kritische Internationalisierungskorrektur für Wiki-d-Tag-Normalisierung ([#2177](https://github.com/nostr-protocol/nips/pull/2177)). Frühere Regeln konvertierten alle Nicht-ASCII-Zeichen zu `-`, was die Unterstützung für Japanisch, Chinesisch, Arabisch, Kyrillisch und andere Schriften brach. Die aktualisierte Spezifikation bewahrt UTF-8-Buchstaben, wendet Kleinschreibung nur auf Zeichen mit Grossbuchstaben-Varianten an und enthält umfassende Beispiele: `"ウィキペディア"` bleibt `"ウィキペディア"`, `"Москва"` wird zu `"москва"`, und gemischte Schriften wie `"日本語 Article"` normalisieren zu `"日本語-article"`.

## Veröffentlichungen

**Zapstore 1.0-rc1** - Der Nostr-basierte permissionless App Store liefert den [ersten Release Candidate](https://github.com/zapstore/zapstore/releases/tag/1.0-rc1) seiner neuen Architektur mit einer vollständigen UI-Überarbeitung, umgeschriebenem Paketmanager mit verbesserter Fehlerbehandlung, App Stacks für kuratierte Entdeckung, neugestalteten Profilbildschirmen, Hintergrund-Update-Prüfung und unendlichem Scrollen in Release-Listen.

**KeyChat v1.38.1** - Die MLS-basierte verschlüsselte Messaging-App [fügt UnifiedPush-Unterstützung](https://github.com/keychat-io/keychat-app/releases/tag/v1.38.1%2B6489) für Android- und Linux-Push-Benachrichtigungen hinzu, plus biometrische Authentifizierung für Datenschutzoperationen. Verfügbar für Android, Windows, macOS und Linux.

**Alby Go v2.0.0** - Der mobile Lightning-Wallet-Begleiter [liefert ein visuelles Redesign](https://github.com/getAlby/go/releases/tag/v2.0.0) mit neuem Logo, aktualisierter Farbpalette, neugestaltetem Adressbuch und verbesserter Betragseingabe-Tastatur. BTC Map ist jetzt vom Startbildschirm aus zugänglich, und Transaktionsbeschreibungen erscheinen in Benachrichtigungen.

**nak v0.17.4** - fiatjafs Kommandozeilen-Nostr-Tool [veröffentlicht](https://github.com/fiatjaf/nak/releases/tag/v0.17.4), nach v0.17.3s LMDB-Linux-Restriktionskorrektur von letzter Woche.

## Bemerkenswerte Code- und Dokumentationsänderungen

*Offene Pull Requests und Arbeiten im Frühstadium, die es wert sind, beobachtet zu werden.*

### Damus (iOS)

[NIP-19 relay hints](https://github.com/damus-io/damus/pull/3477) implementiert den Verbrauch von Relay-Hints für Event-Abruf. Wenn Benutzer nevent-, nprofile- oder naddr-Links öffnen, extrahiert Damus jetzt Relay-Hints aus den bech32-TLV-Daten und verbindet sich mit ephemeren Relays, um Inhalte abzurufen, die nicht im Relay-Pool des Benutzers sind. Die Implementierung enthält referenzgezählte Bereinigung, um Race Conditions während gleichzeitiger Lookups zu verhindern. [Bild-URL-Erkennung](https://github.com/damus-io/damus/pull/3474) konvertiert automatisch eingefügte Bild-URLs in Vorschau-Thumbnails im Composer, mit Karussell-Positionsabzeichen für mehrere Bilder. [npub-Einfüge-Konvertierung](https://github.com/damus-io/damus/pull/3473) transformiert eingefügte npub/nprofile-Strings in Erwähnungs-Links mit asynchroner Profilauflösung.

### Amethyst (Android)

[Payment targets](https://github.com/vitorpamplona/amethyst/pull/1627) fügt eine Event-Schnittstelle für NIP-57-Zap-Splits hinzu, die es Posts ermöglicht, mehrere Empfänger anzugeben, die eingehende zaps teilen (nützlich für Kollaborationen, Umsatzbeteiligung oder Trinkgeld an sowohl Content-Ersteller als auch die Tools, die sie verwenden). [Quartz-Feature-Paritätsdokumentation](https://github.com/vitorpamplona/amethyst/pull/1624) fügt eine detaillierte Tabelle hinzu, die verfolgt, welche Features über Android-, Desktop-JVM- und iOS-Targets implementiert sind, und vermerkt, dass iOS Core-Kryptografie (`Secp256k1Instance`), JSON-Serialisierung und Datenstrukturen fehlen.

### Notedeck (Desktop)

[Timeline-Filter-Neubau](https://github.com/damus-io/notedeck/pull/1226) behebt einen Bug, bei dem entfolgte Konten weiterhin in Feeds erschienen. Timeline-Filter wurden einmal aus der Kontaktliste erstellt und nie aktualisiert; die Korrektur fügt `contact_list_timestamp`-Tracking und eine `invalidate()`-Methode hinzu, um Neubauten auszulösen, wenn sich der Folge-Status ändert.

### Citrine (Android Relay)

[ContentProvider API](https://github.com/greenart7c3/Citrine/pull/86) exponiert die Event-Datenbank des lokalen Relays an andere Android-Apps über `ContentResolver`. Im Gegensatz zur WebSocket-Schnittstelle (die erfordert, dass Apps eine persistente Verbindung aufrechterhalten und das Nostr-Relay-Protokoll sprechen) bietet ContentProvider direkten synchronen Datenbankzugriff über Androids nativen IPC-Mechanismus. Externe Apps können Events nach ID, pubkey, kind oder Datumsbereich abfragen, neue Events mit Validierung einfügen und Events löschen, ohne Socket-Verbindungen zu verwalten.

### rust-nostr (Library)

[NIP-40 Relay-Level-Unterstützung](https://github.com/rust-nostr/nostr/pull/1183) fügt Ablaufbehandlung auf Relay-Builder-Ebene hinzu. Abgelaufene Events werden jetzt vor der Speicherung abgelehnt und vor dem Senden an Clients herausgefiltert, wodurch die Notwendigkeit entfällt, dass jede Datenbankimplementierung Ablaufprüfungen unabhängig behandelt.

### nak (CLI)

[Blossom mirror](https://github.com/fiatjaf/nak/pull/91) implementiert Blob-Mirroring-Funktionalität für das Kommandozeilen-Tool.

### Mostro (P2P Trading)

[Dev fee audit events](https://github.com/MostroP2P/mostro/pull/559) fügt transparente Audit-Trails für Entwicklungsfonds-Zahlungen durch kind-8383-Nostr-Events hinzu. Die Implementierung veröffentlicht nicht-blockierende Audit-Events nach erfolgreichen Gebührenzahlungen, einschließlich Bestelldetails und Zahlungs-Hashes, während Käufer/Verkäufer-Pubkeys aus Datenschutzgründen ausgeschlossen werden.

### MDK (Marmot Development Kit)

Drei Sicherheitsaudit-Korrekturen landeten: [Autorenverifizierung](https://github.com/marmot-protocol/mdk/pull/40) erzwingt, dass Rumor-Pubkeys mit MLS-Absender-Credentials übereinstimmen, um Impersonationsangriffe zu verhindern. [KeyPackage-Identitätsbindung](https://github.com/marmot-protocol/mdk/pull/41) verifiziert, dass Credential-Identität mit Event-Signierern übereinstimmt. [Admin-Update-Validierung](https://github.com/marmot-protocol/mdk/pull/42) verhindert leere Admin-Sets und Nicht-Mitglieder-Admin-Zuweisungen.

### Shopstr (Marketplace)

[HODL invoice escrow](https://github.com/shopstr-eng/shopstr/pull/217) implementiert ein vertrauensminimiertes Zahlungssystem für physische Güter. Die Architektur verwendet Albys `makeHoldInvoice`, um Käufergelder in ihrer eigenen Wallet zu sperren, wobei die Abwicklung erst nach der Bestandsverifizierung durch den Händler ausgelöst wird. Das Handshake-Protokoll läuft über [NIP-17](/de/topics/nip-17/) verschlüsselte DMs: Käufer sendet Bestellanfrage, Händler antwortet mit HODL Invoice, Käufer zahlt (Gelder gesperrt), Händler bestätigt Bestand und Versand, dann gibt die Abwicklung die Gelder frei. Multi-Händler-Warenkorb-Unterstützung teilt Zahlungen auf Verkäufer auf.

### Jumble (Web Client)

[Pro-Relay-Entdeckungsmodus](https://github.com/CodyTseng/jumble/pull/713) fügt einen Schalter hinzu, um Posts von gefolgten Benutzern auf bestimmten Relays zu verbergen, was sprachbasierte Entdeckungs-Feeds ermöglicht (z.B. nostr.band/lang/*). Die Funktion filtert Posts heraus, bei denen der Autoren-Pubkey in der Folgeliste des Benutzers erscheint, und persistiert den Schalter-Status pro Relay-URL in localStorage.

### White Noise (Encrypted Messaging)

[Medien-Upload-Wiederholung](https://github.com/marmot-protocol/whitenoise/pull/937) fügt Wiederholungsoptionen für fehlgeschlagene Uploads hinzu. [Profilbearbeitungswarnungen](https://github.com/marmot-protocol/whitenoise/pull/927) warnen Benutzer vor Profiländerungen. Im Backend behebt [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs/pull/422) eine Race Condition bei der AccountGroup-Erstellung.

### npub.cash (Lightning Address Service)

[v3-Umschreibung](https://github.com/cashubtc/npubcash-server/pull/40) migriert zu Bun für das Monorepo und den Server, fügt SQLite-Unterstützung hinzu, entfernt v1-Kompatibilität, implementiert LUD-21 und fügt Echtzeit-Mint-Quote-Updates hinzu.

### nostr-java (Library)

[v1.1.1](https://github.com/tcheeric/nostr-java/releases/tag/v1.1.1) liefert WebSocket-Handling-Refaktoren und verbesserte Test-Robustheit über [zwei PRs](https://github.com/tcheeric/nostr-java/pull/499).

### NIPs Repository

[NIP-54-Djot-Migration](https://github.com/nostr-protocol/nips/pull/2180) schlägt eine separate Änderung der Wiki-Spezifikation vor: Wechsel des Inhaltsformats von Asciidoc zu Djot, einer leichtgewichtigen Auszeichnungssprache mit sauberer Syntax. Der PR führt referenzbasierte Links für Wikilinks ein, was Querverweise zwischen Wiki-Artikeln in Quellform lesbarer macht. [NIP-XX Quorum](https://github.com/nostr-protocol/nips/pull/2179) führt Schwellenwert-Multisignatur-Governance für Nostr-Gruppen mit FROST (Flexible Round-Optimized Schnorr Threshold signatures) ein. Ein Quorum ist ein nsec, das unter Mitgliedern durch ein T-von-N-Schema geteilt wird, bei dem Mitglieder sich selbst vertreten oder an einen Repräsentantenrat delegieren können. Wenn der Rat wechselt, wird der alte nsec obsolet und ein neuer wird verteilt - der letzte Akt jedes Rats ist die Signierung des Governance-Übergangs-Events. Die Spezifikation definiert Mitgliedschaft (öffentlich oder privat), Wahlen und Abstimmungen (Volksabstimmungen, Misstrauensvoten), optionale "Gesetze" in natürlicher Sprache und, entscheidend, Quorum-Ontologien, bei denen Quoren Mitglieder anderer Quoren sein können, was hierarchische Strukturen wie Lokalitäten ermöglicht, die regionalen Körperschaften beitreten. Anwendungsfälle umfassen Quellcode-Entwicklung, Unternehmensvorstande, HOAs und moderierte Gemeinschaften.

---

Das war's für diese Woche und dieses Jahr. Bauen Sie etwas? Haben Sie Neuigkeiten zu teilen? Möchten Sie, dass wir über Ihr Projekt berichten? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Kontaktieren Sie uns via NIP-17 DM</a> oder finden Sie uns auf Nostr.
