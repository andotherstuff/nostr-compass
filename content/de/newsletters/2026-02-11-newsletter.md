---
title: 'Nostr Compass #9'
date: 2026-02-11
translationOf: /en/newsletters/2026-02-11-newsletter.md
translationDate: 2026-02-12
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, deinem wöchentlichen Wegweiser durch Nostr.

**Diese Woche:** Mostro liefert seine erste öffentliche Beta nach drei Jahren Entwicklung und bringt P2P-Bitcoin-Handel auf Mobilgeräte via Nostr. OpenSats vergibt seine sechzehnte Welle von Bitcoin-Grants, wobei Minibits Wallet eine Erneuerung für sein Nostr-integriertes Cashu-Wallet erhält. **Zapstore erreicht den stabilen 1.0-Release**, was die Reifung des dezentralisierten Android-App-Stores markiert. Coracle 0.6.29 fügt Themen und Highlight-Kommentare hinzu. Igloo Desktop v1.0.3 liefert umfangreiche Sicherheitshärtung für Frostr Threshold-Signierung. Amber v4.1.2-pre1 migriert zur Flow-Architektur. Angor erreicht v0.2.5 mit überarbeiteter Funding-UI und NIP-96-Bildserver-Konfiguration. NostrPress startet als Tool, das Nostr-Profile in statische Blogs umwandelt. Antiprimal liefert ein standardkonformes Gateway, das Primals proprietären Cache-Server mit Standard-Nostr-NIPs verbindet. Primal Android mergt 18 PRs, die die NWC-Infrastruktur mit Dual-Wallet-Unterstützung, Audit-Logging und der `lookup_invoice`-Methode erweitern. diVine liefert API-First Video-Feeds. Marmots TypeScript SDK lagert seine Referenz-Chat-App in ein eigenständiges Repo aus und beginnt die Migration zu ts-mls v2. Im NIPs-Repository wird HyperLogLog Approximate Counting für NIP-45 gemergt und Identitäts-Tags werden aus kind 0 extrahiert. Vorschläge von vitorpamplona beginnen systematisch kind 0 Metadaten-Events zu verschlanken. Neue Protokollvorschläge umfassen Nostr Relay Connect für NAT-Traversierung und Nostr Web Tokens für signierte Web-Claims. In den Deep Dives dieser Woche geht es um NIP-45s neues HyperLogLog Approximate Counting für relay-übergreifende Event-Metriken und NIP-96s HTTP-Dateispeicherungsprotokoll, das nun zugunsten von Blossom als veraltet markiert ist, während Projekte den Übergang zwischen den beiden Medienstandards vollziehen.

## Neuigkeiten

### Mostro liefert erste öffentliche Beta

[Mostro](https://github.com/MostroP2P/mostro), die Peer-to-Peer-Bitcoin-Börse auf Nostr, hat ihre [Mobile App v1.1.0](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0) veröffentlicht, die erste öffentliche Beta des Projekts nach drei Jahren Entwicklung. Nutzer können Bitcoin direkt handeln, wobei Nostr für Auftragskoordination und Lightning für Abwicklung sorgt, ganz ohne treuhänderischen Vermittler.

Enthalten sind Push-Benachrichtigungen mit verbesserter Hintergrundzuverlässigkeit auf Android, ein optionales Logging-System zur Erfassung und Weitergabe von Diagnosedaten bei auftretenden Problemen, sanftere Relay-Updates durch additive Initialisierung und Phase-2-UI-Verfeinerungen mit Internationalisierungsunterstützung. Verfügbar auf [Zapstore](https://zapstore.dev) und als direkter [GitHub-Download](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0).

Mostro reiht sich neben Shopstr und Plebeian Market als Nostr-native Commerce-Anwendung ein, mit dem Unterschied, dass es sich auf Fiat-zu-Bitcoin-Börsenkoordination konzentriert. Order-Matching und Streitbeilegung laufen über Nostr-Relays via den zugrunde liegenden [Mostro-Daemon](https://github.com/MostroP2P/mostro).

### OpenSats sechzehnte Welle von Bitcoin-Grants

[OpenSats](https://opensats.org/blog/sixteenth-wave-of-bitcoin-grants) kündigte Grants für 17 Open-Source-Projekte an. Nostr-relevantes Highlight: [Minibits Wallet](https://github.com/minibits-cash/minibits_wallet), das Android-[Cashu](/de/topics/cashu/)-Wallet mit [NIP-60](/de/topics/nip-60/) Wallet-Event-Unterstützung und Nutzap-Integration, erhielt einen Erneuerungsgrant. Minibits verwendet Nostr-Events zur Speicherung des ecash-Token-Zustands, was Wallet-Backups per Relay-Sync geräteübergreifend portabel macht.

### NostrPress: Nostr-Profil zum statischen Blog

[NostrPress](https://github.com/besoeasy/NostrPress) ([blog.besoeasy.com](https://blog.besoeasy.com)) wandelt ein Nostr-Profil in einen vollständig statischen Blog um, der überall bereitgestellt werden kann. Artikel werden auf Nostr veröffentlicht, und NostrPress generiert daraus eine eigenständige Website, inklusive lokaler Medienspeicherung und RSS-Feeds.

Auf Nunjucks-Templating und JavaScript aufbauend, produziert NostrPress Seiten ohne Plattform-Lock-in. Die generierte Ausgabe ist reines HTML/CSS, das auf jedem statischen Dateiserver, GitHub Pages, Netlify oder einem persönlichen VPS laufen kann. Neben [Npub.pro](https://github.com/nostrband/nostrsite) und [Servus](https://github.com/servus-social/servus) bietet sich das Tool als weitere Option an, Nostr-Inhalte in traditionelle Websites zu verwandeln.

### Antiprimal: Standardkonformes Gateway zu Primals Cache

[antiprimal](https://gitlab.com/soapbox-pub/antiprimal) ([antiprimal.net](https://antiprimal.net)), von Alex Gleason und dem Soapbox-Team entwickelt, ist ein WebSocket-Gateway, das Primals proprietären Cache-Server mit Standard-Nostr-Protokollnachrichten verbindet. Primal bietet Funktionen wie Event-Statistiken, Inhaltssuche und Web-of-Trust-Berechnungen per `wss://cache.primal.net/v1`, setzt aber ein proprietäres Nachrichtenformat mit einem nicht-standardmäßigen `cache`-Feld voraus, das Standard-Nostr-Clients nicht verwenden können. Antiprimal übersetzt Standard-NIP-Anfragen in Primals Format und konvertiert Antworten zurück.

Unterstützt werden [NIP-45](/de/topics/nip-45/) COUNT-Abfragen (Reaktionen, Antworten, Reposts, Zap-Zähler, Follower-Zahlen), [NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md) Suche, [NIP-11](/de/topics/nip-11/) Relay-Informationen und [NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md) Trusted Assertions. Zusätzlich veröffentlicht ein Begleit-Bot NIP-85 kind 30382 (Benutzerstatistiken) und kind 30383 (Event-Engagement) Events. In TypeScript auf Bun mit der Nostrify-Bibliothek gebaut, hat das Projekt seit seiner Erstellung am 6. Februar bereits 53 Commits und ist live unter antiprimal.net.

### Ikaros: KI-Agent-Messaging-Gateway für Signal und Nostr

[Ikaros](https://gitlab.com/soapbox-pub/ikaros), vom Soapbox-Team entwickelt, ist ein Messaging-Gateway, das KI-Agenten die Kommunikation per Signal und Nostr-verschlüsselten DMs ermöglicht. Via [Agent Client Protocol](https://agentclientprotocol.org) (ACP) verbindet die Bridge jeden ACP-kompatiblen KI-Codierassistenten mit echten Messaging-Netzwerken. Drei Pull Requests bilden den initialen Build des Projekts diese Woche.

[PR #1](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/1) implementiert einen vollständigen [NIP-04](/de/topics/nip-04/) Encrypted-DM-Adapter mit Sende-/Empfangsunterstützung, Antwort-Pufferung mit explizitem Flush bei Abschluss, `nsec`- und Hex-Private-Key-Formaten, Multi-Relay-Publishing mit automatischer Wiederverbindung und einem interaktiven Setup-Wizard. Verwendet werden nostr-tools v2.23.0 und das ACP SDK v0.14.1.

In [PR #2](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/2) wird ein stiller Nachrichtenverlust durch Session-Update-Race-Condition behoben: eingehende Benachrichtigungen, die vor Registrierung der Session in der Map eintrafen, gingen still verloren, und der Fix puffert sie nun zum Replay nach Abschluss der Registrierung. [PR #3](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/3) fügt Signal-Nutzer- und Gruppennamen-/UUID-Metadaten zu Agenten-Interaktionen hinzu, sodass der KI-Agent weiß, mit wem er spricht und in welcher Gruppe. Damit eröffnet sich ein neuer Designraum: KI-Agenten, die per Nostr-DMs erreichbar sind und auch von Signal aus kontaktiert werden können, und umgekehrt.

### Kind-0-Schlankheitskampagne

vitorpamplona eröffnete diese Woche PRs, die systematische Extraktion von Daten aus kind 0 (Benutzer-Metadaten) Events in dedizierte Event-Kinds vorschlagen. Adressiert wird ein wachsendes Problem: kind 0 Events haben im Laufe der Zeit Felder angesammelt, die meisten Clients nicht verwenden, was die Größe jedes Profil-Abrufs aufbläht.

[PR #2216](https://github.com/nostr-protocol/nips/pull/2216) (gemergt) verschiebt Identitäts-Tags (`i`-Tags) von kind 0 zu einem neuen kind 10011, da die Adoption minimal war. [PR #2213](https://github.com/nostr-protocol/nips/pull/2213) schlägt vor, [NIP-05](/de/topics/nip-05/)-Verifizierung nach kind 10008 zu verschieben, was mehrere NIP-05-Identifikatoren pro Nutzer und Filterung nach NIP-05-Adresse ermöglichen würde. [PR #2217](https://github.com/nostr-protocol/nips/pull/2217) zielt darauf ab, Lightning-Adressen (lud06/lud16) in einen neuen kind zu extrahieren, sodass nicht mehr alle kind 0 Nutzer Zap-bezogene Felder mitführen, die nur bei Lightning-Integration relevant sind.

Wiederbelebt wurde damit auch die Diskussion um die breitere Frage der kind 0 Struktur, einschließlich [PR #1770](https://github.com/nostr-protocol/nips/pull/1770), dem langjährigen Vorschlag, stringifiziertes JSON in kind 0 Inhalten durch strukturierte Tags zu ersetzen.

### NIP-70-Relay-Unterstützung entscheidend für verschlüsselte Nachrichten

White Noise, die Implementierung des [Marmot](/de/topics/marmot/)-Protokolls, hat eine [kritische Lücke identifiziert](https://blog.jgmontoya.com/2026/02/10/nip70-relay-status.html) in der Relay-Unterstützung von [NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md) (Protected Events) und [NIP-42](/de/topics/nip-42/) (Authentifizierung). Tests ergaben, dass große öffentliche Relays wie Damus, Primal und nos.lol geschützte Events mit `blocked: event marked as protected`-Fehlern direkt ablehnen, statt die erforderliche Authentifizierungs-Challenge einzuleiten.

Gebrochen wird dadurch ein zentrales Sicherheitsfeature: NIP-70 ermöglicht das sichere Löschen verbrauchter MLS KeyPackages und verhindert „harvest now, decrypt later"-Angriffe. Verschlüsselte Messaging-Protokolle können Nutzer nicht vor zukünftiger Schlüsselkompromittierung schützen, solange Relays dies nicht unterstützen. White Noise hat NIP-70 als Reaktion standardmäßig deaktiviert und behält ein optionales Flag bei.

**Aufruf an Relay-Betreiber:** Implementiert den vollständigen NIP-42-Authentifizierungsablauf. Fordert bei geschützten Events zur Eigentümerschaftsbestätigung auf und akzeptiert dann validierte Schreibvorgänge. Geschützte Events ohne Authentifizierung abzulehnen bricht Protokoll-Sicherheitsgarantien, auf die verschlüsselte Messaging-Anwendungen angewiesen sind.

## Releases

### Coracle 0.6.29

[Coracle](https://github.com/coracle-social/coracle) ([coracle.social](https://coracle.social)), hodlbods Web-Client, hat [0.6.29](https://github.com/coracle-social/coracle/releases/tag/0.6.29) veröffentlicht. Neu sind Anzeige von Themen und Kommentaren zu kind 9802 Highlights sowie ein Listen-Navigationselement, das schnellen Zugriff auf benutzerkuratierte Listen aus der Haupt-UI bietet. Unter der Haube wurde Coracle auf eine neue Version von Welshman aktualisiert, der gemeinsamen Nostr-Bibliothek für Relay-Management und Event-Handling. Aktualisiert wurde auch die Standard-Relay-Liste, und Glitchtip-Error-Tracking wurde entfernt.

### Igloo Desktop v1.0.3

[Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop), die [FROST](/de/topics/frost/)-basierte Threshold-Signer- und Schlüsselverwaltungsanwendung, hat [v1.0.3](https://github.com/FROSTR-ORG/igloo-desktop/releases/tag/v1.0.3) mit umfangreicher Sicherheitshärtung veröffentlicht. IPC-Validierung, Electron-Isolation und SSRF-bewusste Relay-Prüfungen wehren Server-Side-Request-Forgery ab. Hinzu kommen ein neuer Onboarding- und Share-Import-Flow zur Vereinfachung der Schlüsselverteilung, Relay-Planung mit Normalisierung und Prioritäts-Merging, und eine Preload-basierte Electron-API-Architektur zur Verbesserung der Sicherheitsgrenze zwischen Renderer und Hauptprozess. Stabilität bei Threshold-Signing-Sessions gewährleistet ein Signer-Keep-Alive-System, und Recovery-UX-Verbesserungen reduzieren die Reibung bei der Schlüsselwiederherstellung.

### Amber v4.1.2-pre1

[Amber](https://github.com/greenart7c3/Amber), der Android Event-Signer, hat [v4.1.2-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.2-pre1) veröffentlicht. Behoben werden die fehlende Relay-Trust-Score-Anzeige aus v4.1.1 und JSON-Parsing-Probleme bei Nicht-Nostr-Verschlüsselungs-/Entschlüsselungsanfragen. Migriert wurde das Account-Modell von LiveData zu Flow, Bunker-Secrets wechseln zu vollständigen UUIDs, und Gradle Plugin 9 kommt als Upgrade hinzu.

### Mostro Mobile v1.1.0 und Daemon v0.16.1

Im [Neuigkeiten-Abschnitt oben](#mostro-liefert-erste-öffentliche-beta) findet sich die vollständige Berichterstattung zum Mobile-Release. Serverseitig hat der [Mostro-Daemon](https://github.com/MostroP2P/mostro) [v0.16.1](https://github.com/MostroP2P/mostro/releases/tag/v0.16.1) veröffentlicht, mit automatischem Publishing von NIP-01 kind 0 Metadaten beim Start ([PR #575](https://github.com/MostroP2P/mostro/pull/575)), sodass der Daemon seine Identität im Netzwerk ankündigt. Ebenfalls aktualisiert wurde die Dokumentation zur Dev-Fee-Berechnung ([PR #571](https://github.com/MostroP2P/mostro/pull/571)).

### Angor v0.2.5

[Angor](https://github.com/block-core/angor) ([angor.io](https://angor.io)), das dezentralisierte P2P-Funding-Protokoll auf Bitcoin und Nostr, hat [v0.2.5](https://github.com/block-core/angor/releases/tag/v0.2.5) mit drei gemergten PRs veröffentlicht. [PR #649](https://github.com/block-core/angor/pull/649) redesignt den Funds-Management-Bereich (V2) und ersetzt das bisherige Layout durch ein neues Interface zur Verfolgung einzelner UTXOs und Investitionspositionen. [PR #651](https://github.com/block-core/angor/pull/651) überarbeitet die InvoiceView: aktualisierte Button-Styles, schließbare Dialoge, „Copy Address"-Befehl, Abbruchunterstützung und verbessertes Investment-Flow-Handling. Konfigurierbare [NIP-96](/de/topics/nip-96/) ([Spec](https://github.com/nostr-protocol/nips/blob/master/96.md)) Bildserver in den Einstellungen kommen via [PR #652](https://github.com/block-core/angor/pull/652), sodass Nutzer ihren Media-Upload-Endpunkt wählen können. In der Vorwoche wurde [v0.2.4](https://github.com/block-core/angor/releases/tag/v0.2.4) veröffentlicht.

### Ridestr v0.2.2 und v0.2.3

[Ridestr](https://github.com/variablefate/ridestr), die dezentralisierte Rideshare-Plattform, [letzte Woche vorgestellt](/de/newsletters/2026-02-04-newsletter/#ridestr-v020-roadflare-release), setzte die schnelle Iteration mit [v0.2.2](https://github.com/variablefate/ridestr/releases/tag/v0.2.2) (Bridge Payment Hotfix) und [v0.2.3](https://github.com/variablefate/ridestr/releases/tag/v0.2.3) nach dem v0.2.0 „RoadFlare Release" fort. Im v0.2.2-Hotfix wird ein Bug behoben, bei dem Cross-Mint-[Cashu](/de/topics/cashu/)-Bridge-Zahlungen Fahrten automatisch stornierten, während die Zahlung noch verarbeitet wurde oder letztendlich erfolgreich gewesen wäre, was vorzeitige Fahrtenstornierung bei langsameren Abwicklungen verhindert. Ebenfalls behoben wurden UI-Flackern und defekte Touch-Hitboxen beim „Mein Standort"-Button. v0.2.3 liefert weitere Bugfixes. Beide Releases enthalten separate APKs, jeweils eine Ridestr-Fahrgast-App und eine Drivestr-Fahrer-App.

### Nostr PHP 1.9.4

[Nostr PHP](https://github.com/nostrver-se/nostr-php) ([nostr-php.dev](https://nostr-php.dev)), die PHP-Hilfsbibliothek, hat [1.9.4](https://github.com/nostrver-se/nostr-php/releases/tag/1.9.4) veröffentlicht und fügt eine konfigurierbare `timeout`-Eigenschaft zur Request-Klasse hinzu ([PR #106](https://github.com/nostrver-se/nostr-php/pull/106)). Entwickler können damit benutzerdefinierte Timeout-Dauern für Relay-Verbindungen und Nachrichtenanfragen setzen, um endloses Hängen zu verhindern.

### Zapstore v1.0.0

[Zapstore](https://github.com/zapstore/zapstore/releases/tag/1.0.0) ([zapstore.dev](https://zapstore.dev)), der erlaubnisfreie Android-App-Store auf Nostr, **hat diese Woche seinen stabilen 1.0-Release-Meilenstein erreicht** nach Monaten von Release-Kandidaten.

Wichtige Stabilitätsverbesserungen sind enthalten: Install-Button-Zustandshandling, das sicherstellt, dass „Löschen" sofort nach Abschluss der Installation erscheint, nutzerfreundliche Fehlermeldungen mit aufklappbaren technischen Details und ein „Problem melden"-Button, der verschlüsselte DMs via Nostr mit ephemeren Schlüsseln sendet. Hinzu kommen neuer Update-Bildschirm mit Polling und Batch-Tracking, besserer Download-Watchdog, dynamische parallele Download-Limits basierend auf Geräteleistung, häufigere Synchronisierung installierter Pakete und verbesserte Versionsvergleichslogik. Gelöst wurde ein kritisches flutter_secure_storage-Problem, und die Package-Manager-Behandlung von Grenzfällen wurde verbessert.

Dieser Meilenstein repräsentiert die Reifung von Nostrs erster dedizierter App-Distributionsplattform, die Entwicklern ermöglicht, Android-Anwendungen direkt an Nutzer zu veröffentlichen, frei von zentralisiertem App-Store-Gatekeeping.

### ZSP v0.3.1

[ZSP](https://github.com/zapstore/zsp), das Go CLI-Tool vom [Zapstore](https://github.com/zapstore/zapstore)-Team, ersetzt Zapstores bisheriges Publishing-Tooling zum Signieren und Hochladen von Android-Apps und hat [v0.3.1](https://github.com/zapstore/zsp/releases/tag/v0.3.1) veröffentlicht. ZSP übernimmt APK-Beschaffung von GitHub, GitLab, Codeberg, F-Droid oder lokalen Dateien, parst dann Metadaten, signiert Nostr-Events (via privatem Schlüssel, [NIP-46](/de/topics/nip-46/) Bunker oder [NIP-07](/de/topics/nip-07/) Browser-Erweiterung) und lädt Artefakte auf [Blossom](/de/topics/blossom/)-Server hoch. Neu sind vollständiger Offline-Modus zum Keystore-Linking, `Content-Digest`-Header bei Blossom-Uploads, verbesserte arm64-v8a APK-Erkennung aus F-Droid-Repositories, GitLab Trailing-Query-Parameter-Fixes und vollständige `.env`-Dateiunterstützung.

### Damus iOS 1.17

[Damus](https://github.com/damus-io/damus), der iOS Nostr-Client, wurde auf Version 1.17 aktualisiert ([PR #3606](https://github.com/damus-io/damus/pull/3606)). Behoben wird ein RelayPool-Problem, bei dem Verbindungen nach ephemerer Lease-Freigabe geschlossen wurden ([PR #3605](https://github.com/damus-io/damus/pull/3605)), was dazu führen konnte, dass Subscriptions unerwartet abbrachen. Gelöst wird außerdem ein Bug bei der Favoriten-Timeline, die keine Events anzeigte, sobald zwischen Tabs gewechselt wurde ([PR #3603](https://github.com/damus-io/damus/pull/3603)).

### nak v0.18.3

[nak](https://github.com/fiatjaf/nak), das Nostr Army Knife CLI, hat [v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3) mit drei Stabilitätsfixes veröffentlicht: Verhinderung eines Panics bei nil oder zu kurzen AUTH-Challenge-Tags, Prüfung von Dateparser-Fehlern vor Verwendung des geparsten Werts und Behandlung von Cashu-Mint-URLs, denen der `://`-Separator fehlt.

### Mi: Browserbasiertes lokales Relay

[Mi](https://git.shakespeare.diy/npub1scvyzz02ayma34hesz62pdrd5nhsmxp74hjq8msmfs9khh3r3drsnw68d8/mi.git) ([mi.shakespeare.wtf](https://mi.shakespeare.wtf)), eine [Shakespeare](https://shakespeare.wtf) MiniApp, ist ein browserbasiertes lokales Relay, das Nostr-Events in IndexedDB archiviert. Mi ruft Profile (kind 0), Kontaktlisten (kind 3), Relay-Listen (kind 10002) und Wallet-Events von verbundenen Relays ab und speichert sie lokal, was Offline-Zugriff auf eigene Daten ermöglicht. Aufgebaut mit React und nostr-tools 2.15.0.

### Agora v1.0.2

[Agora](https://gitlab.com/soapbox-pub/agora) ([agora.spot](https://agora.spot)), die dezentralisierte Aktivismus- und Fundraising-Plattform des Soapbox-Teams, hat [v1.0.2](https://gitlab.com/soapbox-pub/agora/-/releases/v1.0.2) mit Android-APK zum direkten Installieren veröffentlicht. Dies ist die erste Compass-Erwähnung von Agora, das am 17. Januar mit einem Leitbild startete: „Join the global movement for freedom. Send support to activists on the ground internationally and take part in local actions."

Im Zentrum steht eine Weltkarte, auf der Nutzer nach Land durchsuchen, standortgetaggte „Aktionen" erstellen (Proteste, Kampagnen, Community-Organisation) und diese durch verschachtelte Kommentare diskutieren können. Alle Inhalte werden via Nostr-Relays verbreitet, sodass kein zentraler Server abgeschaltet werden kann, um Koordination zum Schweigen zu bringen. Agora unterstützt mehrere Sprachen mit CI-erzwungener Übersetzungsparität, integriert [Blossom](/de/topics/blossom/)-Medienserver und bietet Suche, Hashtag-Browsing mit globalem/regionalem Toggle, Profile und Reaktionssysteme. Als aktueller Android-Build ist v1.0.2 als direkter APK-Download verfügbar.

### xonos v0.1.6

[xonos](https://codeberg.org/xonos/xonos), der experimentelle 3D-Nostr-Client auf Basis der Bevy Game Engine, hat [v0.1.6](https://codeberg.org/xonos/xonos/releases/tag/v0.1.6) veröffentlicht. xonos rendert Nostr-Events in einer räumlichen 3D-Umgebung mit Text-to-Speech-Fähigkeiten und erforscht, wie soziale Protokolldaten außerhalb konventioneller 2D-Interfaces funktionieren könnten.

## Projekt-Updates

### Primal Android erweitert NWC-Infrastruktur

[Primal Android](https://github.com/PrimalHQ/primal-android-app) mergte 18 PRs diese Woche und setzt den NWC-Ausbau fort, der [letzte Woche begonnen wurde](/de/newsletters/2026-02-04-newsletter/#primal-android-liefert-nwc-verschlüsselung). [PR #883](https://github.com/PrimalHQ/primal-android-app/pull/883) fügt NWC-Verbindungen für beide Wallets (Spark und extern) hinzu, und [PR #879](https://github.com/PrimalHQ/primal-android-app/pull/879) implementiert die `lookup_invoice`-NWC-Methode zur Überprüfung des Zahlungsstatus.

NWC-Request-Response-Audit-Logging zur Fehlersuche bei Wallet-Interaktionen bringt [PR #880](https://github.com/PrimalHQ/primal-android-app/pull/880). Multi-Account-Unterstützung in `PrimalNwcService` kommt via [PR #877](https://github.com/PrimalHQ/primal-android-app/pull/877), sodass Nutzer mit mehreren Profilen separate Wallet-Verbindungen pflegen können. [PR #882](https://github.com/PrimalHQ/primal-android-app/pull/882) implementiert periodische Bereinigung abgelaufener Budget-Holds und verhindert, dass veraltete Zahlungsreservierungen Wallet-Operationen blockieren.

UI-Arbeit umfasst Wallet-Upgrade-Bildschirm-Redesigns ([PR #889](https://github.com/PrimalHQ/primal-android-app/pull/889)), Wallet-Upgrade-FAQ ([PR #885](https://github.com/PrimalHQ/primal-android-app/pull/885)), Lightning-Adress-Einstellung beim Onboarding ([PR #888](https://github.com/PrimalHQ/primal-android-app/pull/888)) und einen Fix, der Zap-Transaktionen korrekt von regulären Zahlungen bei Nicht-Lightning-Typen unterscheidet ([PR #887](https://github.com/PrimalHQ/primal-android-app/pull/887)).

### diVine liefert API-First Video-Feeds

[diVine](https://github.com/divinevideo/divine-mobile), der Kurzform-Video-Client, mergte 19 PRs diese Woche und verlagert sich zu einer API-First-Architektur. [PR #1468](https://github.com/divinevideo/divine-mobile/pull/1468) führt API-First Video-Feeds ein, und [PR #1466](https://github.com/divinevideo/divine-mobile/pull/1466) ergänzt Trending-, Recent- und Home-API-Endpunkte. Spezifische Video-Controller zum effizienten Feed-Rendering werden in [PR #1433](https://github.com/divinevideo/divine-mobile/pull/1433) indiziert.

Profilhandling verbesserte sich mit [PR #1440](https://github.com/divinevideo/divine-mobile/pull/1440), der ein Cache-plus-Fresh-Pattern implementiert, was Ladezeiten reduziert und gleichzeitig Datenaktualität sicherstellt. Geliefert wurden auch Benachrichtigungs-Fixes ([PR #1437](https://github.com/divinevideo/divine-mobile/pull/1437)), Kommentar-Flow-Refactoring ([PR #1431](https://github.com/divinevideo/divine-mobile/pull/1431)) und Tab-Swiping auf dem Benachrichtigungsbildschirm ([PR #1388](https://github.com/divinevideo/divine-mobile/pull/1388)).

### White Noise: Keyring-Vereinheitlichung und Suche

Das [White Noise](https://github.com/marmot-protocol/whitenoise-rs) Backend des [Marmot](/de/topics/marmot/)-Protokolls mergte 4 PRs diese Woche. Zwei PRs verbesserten das Keyring-Handling: [PR #468](https://github.com/marmot-protocol/whitenoise-rs/pull/468) macht den Keyring-Service-Identifier per `WhitenoiseConfig` konfigurierbar, und [PR #475](https://github.com/marmot-protocol/whitenoise-rs/pull/475) vereinheitlicht die Implementierung auf ein einzelnes `keyring-core`-Crate mit plattformnativen Stores. Suchfunktionalität kommt separat in [PR #470](https://github.com/marmot-protocol/whitenoise-rs/pull/470) hinzu.

### Marmot TS extrahiert Referenz-Chat-App

Das [Marmot](/de/topics/marmot/) TypeScript SDK ([marmot-ts](https://github.com/marmot-protocol/marmot-ts)) mergte [PR #40](https://github.com/marmot-protocol/marmot-ts/pull/40), der die eingebaute Referenz-Chat-Anwendung entfernt und in ein eigenständiges Repo auslagert: [marmots-web-chat](https://github.com/marmot-protocol/marmots-web-chat). Am 6. Februar erstellt, ist das neue Repo eine Referenzimplementierung mit eigener CI-Pipeline, Tabbed-Chat-View und unabhängigem Build-System. So kann sich das SDK auf Bibliotheksbelange konzentrieren, während die Chat-App die UX unabhängig weiterentwickelt.

Offen ist [PR #41](https://github.com/marmot-protocol/marmot-ts/pull/41), der marmot-ts zu ts-mls v2.0.0 migriert und eine überarbeitete API mit vereinheitlichten Kontextobjekten, neuen Nachrichtenbehandlungs-Utilities (Event-Erstellung, Lesen, Deserialisierung), KeyPackage-Metadaten-Helfern und Löschungs-Event-Unterstützung bringt.

### Alby Hub Updates

[Alby Hub](https://github.com/getAlby/hub) mergte 5 PRs diese Woche. [PR #2049](https://github.com/getAlby/hub/pull/2049) fügt ein Alby CLI zum App-Store-Interface hinzu. Ungültige Zap-Daten in der Transaktionsliste behandelt [PR #2033](https://github.com/getAlby/hub/pull/2033), und [PR #2046](https://github.com/getAlby/hub/pull/2046) entfernt die ungenutzte `ListTransactions`-Methode aus dem LNClient-Interface.

### Notedeck liefert Dashboard und Agentium

[Notedeck](https://github.com/damus-io/notedeck), der plattformübergreifende Nostr-Client von Damus, mergte 6 PRs diese Woche. [PR #1247](https://github.com/damus-io/notedeck/pull/1247) fügt eine initiale Dashboard-App hinzu. Agentium, die Multi-Agent-Entwicklungsumgebung, die den Dave-KI-Assistenten in ein System mit dualen KI-Modi und szenenbasiertem Agenten-Management verwandelt, kommt in [PR #1293](https://github.com/damus-io/notedeck/pull/1293). Mehrzeiliger Nachrichtenkomposer mit Signal-artigen Tastenkombinationen folgt in [PR #1276](https://github.com/damus-io/notedeck/pull/1276), und [PR #1278](https://github.com/damus-io/notedeck/pull/1278) bringt Medienperformance-Verbesserungen. Bemerkenswerte offene PRs umfassen [Outbox-Infrastruktur](https://github.com/damus-io/notedeck/pull/1288) und [NIP-34](/de/topics/nip-34/) [Git-App-Planung](https://github.com/damus-io/notedeck/pull/1289).

### Agora liefert großes UI-Overhaul

[Agora](https://gitlab.com/soapbox-pub/agora) mergte 7 PRs diese Woche neben dem v1.0.2-Release. Am umfangreichsten ist [PR #106](https://gitlab.com/soapbox-pub/agora/-/merge_requests/106), der 11 UI-Aufgaben in den Bereichen Einstellungen, Profilbearbeitung, Karteninteraktionen, Suchergebnisse, Kommentarfilterung und Blossom-Server-Management abschließt. Reaktionsbuttons wurden deaktiviert, damit nicht-authentifizierte Nutzer keine stillen Fehler mehr erhalten. Zudem wurden Date-Line-Kartenschwenken und fette Übereinstimmungstexte in Suchergebnissen ergänzt.

Kommentarzähler unter Feed-Beiträgen und Thread-Seiten kommen in [PR #108](https://gitlab.com/soapbox-pub/agora/-/merge_requests/108). Automatische Wiederholung bei Event-Ladefehlern mit explizitem Neulade-Button fügt [PR #107](https://gitlab.com/soapbox-pub/agora/-/merge_requests/107) hinzu. [PR #104](https://gitlab.com/soapbox-pub/agora/-/merge_requests/104) ändert Hashtag-Browsing auf standardmäßig globalen Scope, da länderspezifischer Standard oft null Ergebnisse lieferte.

[PR #109](https://gitlab.com/soapbox-pub/agora/-/merge_requests/109) prüft per CI-Schritt die Übersetzungsparität und lässt den Build fehlschlagen, falls Werte fehlen. [PR #110](https://gitlab.com/soapbox-pub/agora/-/merge_requests/110) kürzt große Notizen in Feeds zum Erhalt des Scroll-Rhythmus, und [PR #111](https://gitlab.com/soapbox-pub/agora/-/merge_requests/111) behebt iOS-Mobile-Zoom beim Kommentieren von Aktionen, verursacht durch kleine Schriftgrößen.

### Clawstr liefert CLI und Lightning-Zap-Buttons

[Clawstr](https://gitlab.com/soapbox-pub/clawstr), die Reddit-inspirierte Plattform, auf der KI-Agenten Communities auf Nostr erstellen und verwalten, mergte 3 PRs diese Woche. In [PR #11](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/11) werden alle manuellen nak-Befehle in den KI-Agenten-Skill-Definitionen durch das neue `@clawstr/cli`-Paket (`npx -y @clawstr/cli@latest`) ersetzt, manuelle JSON-Event-Konstruktion zugunsten von CLI-Befehlen eliminiert und Wallet-Operationen (init, balance, zap, npc) sowie [NIP-50](/de/topics/nip-50/) Volltextsuche hinzugefügt.

[PR #13](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/13) bringt eine „For Humans"-Dokumentationsseite und eine `ProfileZapDialog`-Komponente. Auf Profilseiten erscheint der Zap-Button, sobald eine Lightning-Adresse konfiguriert ist, und funktioniert ohne Login per LNURL-pay mit voreingestellten sats-Beträgen und QR-Code-Anzeige. In [PR #12](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/12) wird der `wallet sync`-Befehl dokumentiert und erklärt, wie Zahlungen an Lightning-Adressen von NPC gehalten werden, bis Agenten ihre Wallets explizit synchronisieren.

## NIP-Updates

Aktuelle Änderungen am [NIPs-Repository](https://github.com/nostr-protocol/nips):

**Gemergt:**

- **[NIP-45: HyperLogLog Relay Response](https://github.com/nostr-protocol/nips/pull/1561)** - [NIP-45 (Event-Zählung)](/de/topics/nip-45/) unterstützt jetzt HyperLogLog (HLL) Approximate Counting. Relays können 256-Byte HLL-Registerwerte zusammen mit COUNT-Antworten zurückgeben. Durch Zusammenführen dieser Register von mehreren Relays berechnen Clients approximative Kardinalitäten, ohne vollständige Event-Sets herunterladen zu müssen. Primärer Anwendungsfall sind Follower- und Reaktionszähler, ohne auf ein einzelnes Relay als autoritative Quelle angewiesen zu sein. Schon zwei Reaktions-Events verbrauchen mehr Bandbreite als die 256-Byte-HLL-Payload. HyperLogLog++-Korrekturen verbessern die Genauigkeit bei kleinen Kardinalitäten.

- **[NIP-39: Identitäts-Tags aus Kind 0 verschoben](https://github.com/nostr-protocol/nips/pull/2216)** - [NIP-39](/de/topics/nip-39/) Identitätsanspruchs-Tags (`i`-Tags) wurden aus kind 0 Metadaten-Events in ein neues dediziertes kind 10011 extrahiert. Begründung: fast keine Clients unterstützen diese Tags, sodass sie jedem kind 0 Abruf Größe hinzufügen, ohne Mehrwert zu bieten. Dies ist der erste in einer Reihe von Kind-0-Extraktions-PRs von vitorpamplona (siehe [Neuigkeiten-Abschnitt](#kind-0-schlankheitskampagne)).

**Offene PRs und Diskussionen:**

- **[NIP-XX: Nostr Relay Connect (NRC)](https://github.com/nostr-protocol/nips/pull/2214)** - woikos schlägt ein Protokoll zum Zugriff auf Nostr-Relays durch verschlüsseltes Tunneling via öffentliches Rendezvous-Relay vor. Ermöglicht wird damit der Zugang zu Relays hinter NAT oder Firewalls, einschließlich persönlicher Relays auf Heimservern oder Mobilgeräten. Verwendet werden kind 24891/24892 Events mit [NIP-44](/de/topics/nip-44/)-Verschlüsselung. Praktische Anwendung: jeder Nostr-Client kann lokalen Speicher (IndexedDB, SQLite) als Relay-Endpunkt für geräteübergreifende Synchronisation bereitstellen. Standard NIP-01 Semantiken (REQ, EVENT, CLOSE, COUNT) passieren den Tunnel transparent. Referenzimplementierungen existieren in Go (ORLY Relay) und TypeScript (Smesh).

- **[Nostr Web Tokens (NWT)](https://github.com/nostr-protocol/nips/pull/2187)** - pippellia-btc schlägt Nostr Web Tokens vor, ein Nostr-Event-Format zur Übermittlung signierter Claims zwischen Web-Parteien, inspiriert von JSON Web Tokens (JWTs). NWT kann sowohl [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) (HTTP Auth) als auch [Blossom-Autorisierungs-Events](/de/topics/blossom/) repräsentieren und gibt Clients Flexibilität in Bezug darauf, wie und wie lange Tokens gültig bleiben. Verfügbar ist eine Go-Referenzbibliothek. Verlinkt im PR sind eine [Video-Erklärung](https://github.com/pippellia-btc/nostr-web-tokens) und ein [detaillierter Vergleich](https://github.com/pippellia-btc/nostr-web-tokens#comparisons) mit NIP-98 und Blossom Auth.

- **[NIP-47-Vereinfachung](https://github.com/nostr-protocol/nips/pull/2210)** - rolznz schlägt vor, die `multi_`-Methoden aus [NIP-47 (Nostr Wallet Connect)](/de/topics/nip-47/) zu entfernen, da sie komplex zu implementieren waren und keine Adoption fanden. Reduziert wird auch Duplizierung in Verschlüsselungs- und Abwärtskompatibilitäts-Handling, was die Spec nach der [Hold-Invoice-Ergänzung letzte Woche](/de/newsletters/2026-02-04-newsletter/#nip-updates) bereinigt.

- **[NIP-05: Verschiebung in eigenen Event-Kind](https://github.com/nostr-protocol/nips/pull/2213)** - vitorpamplona schlägt vor, NIP-05-Verifizierung von kind 0 in ein neues kind 10008 zu verschieben, was mehrere NIP-05-Identifikatoren pro Nutzer und Filterung nach NIP-05-Adresse ermöglicht. Teil der Kind-0-Schlankheitskampagne.

- **[NIP-57: Lightning-Adressen aus Kind 0](https://github.com/nostr-protocol/nips/pull/2217)** - vitorpamplona schlägt vor, lud06/lud16 (Lightning-Adressen) aus kind 0 in einen dedizierten Event-Kind gemäß [NIP-57](/de/topics/nip-57/) zu extrahieren, und setzt die Kind-0-Schlankheitsbemühung fort.

- **[Profil-Hypercustomization](https://github.com/nostr-protocol/nips/pull/2165)** - fiatjaf schlägt erweiterte Profilanpassungsfähigkeiten vor, die weit hinaus gehen, was kind 0 derzeit unterstützt.

## NIP Deep Dive: NIP-45 (Event-Zählung) und HyperLogLog

[NIP-45](/de/topics/nip-45/) ([Spec](https://github.com/nostr-protocol/nips/blob/master/45.md)) definiert, wie Clients Relays bitten können, Events zu zählen, die einem Filter entsprechen, ohne die Events selbst zu übertragen. Mit dem Merge von [HyperLogLog-Unterstützung](https://github.com/nostr-protocol/nips/pull/1561) diese Woche kommt eine probabilistische Datenstruktur hinzu, die ein grundlegendes Problem löst: wie zählt man Dinge sicher, die auf mehreren unabhängigen Relays verteilt liegen.

**Das Problem:**

Events auf einem einzelnen Relay zu zählen ist einfach: COUNT-Anfrage senden, Zahl zurückbekommen. Netzwerkübergreifend ist es schwieriger. Meldet Relay A 50 Reaktionen und Relay B 40, ergibt das nicht 90, da viele Events auf beiden Relays existieren. Die wahre Zählung lässt sich nicht ermitteln, ohne alle Events herunterzuladen und zu deduplizieren.

**HyperLogLog:**

HyperLogLog (HLL) ist ein probabilistischer Algorithmus, der die Anzahl eindeutiger Elemente in einer Menge mit festem Speicherbedarf schätzt. In NIP-45 kommen 256 Register mit je einem Byte zum Einsatz, was genau 256 Bytes verbraucht, unabhängig von der Anzahl gezählter Events. Funktionieren tut der Algorithmus, indem er die Binärdarstellung jeder Event-ID untersucht und die Position der führenden Nullen verfolgt. Events, deren IDs mit vielen Nullen beginnen, sind statistisch selten, sodass ihr Auftreten auf eine große Menge hinweist.

**Wie es in NIP-45 funktioniert:**

Antwortet ein Relay auf eine COUNT-Anfrage, kann es ein `hll`-Feld mit base64-kodierten Registerwerten einschließen:

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

HLL-Werte von mehreren Relays sammelt der Client und führt sie zusammen, indem er den Maximalwert an jeder Registerposition übernimmt. Dieses zusammengeführte HLL repräsentiert die Vereinigungsmenge aller Event-Sets und behandelt Deduplizierung automatisch. Aus den zusammengeführten Registern wird dann die endgültige Kardinalitätsschätzung berechnet.

**Genauigkeit:**

Bei 256 Registern beträgt der Standardfehler ungefähr 5,2%. Liegt die tatsächliche Zählung bei 1.000, fällt die Schätzung typischerweise zwischen 948 und 1.052. Konstant bleibt der relative Fehler auch bei größeren Zählungen: 100.000 wird auf ungefähr 94.800-105.200 geschätzt. HyperLogLog++-Korrekturen verbessern die Genauigkeit bei kleinen Kardinalitäten (unter ca. 200), wo der Basisalgorithmus zur Überschätzung neigt.

**Warum es wichtig ist:**

Soziale Metriken (Follower-Zahlen, Reaktionszahlen, Repost-Zahlen) sind Kernfunktion von Social-Media-Clients. Relays einzeln abzufragen zentralisiert die Zählung, alle Events von allen Relays herunterzuladen verschwendet Bandbreite. HLL ermöglicht gute ungefähre Zählungen von mehreren Relays mit nur 256 Bytes Overhead pro Relay, unabhängig von der tatsächlichen Zählung. Schon zwei Reaktions-Events verbrauchen mehr Bandbreite als eine vollständige HLL-Payload.

Fixiert ist die Registeranzahl auf 256 zur Interoperabilität. Alle Relays produzieren zusammenführbare HLL-Werte, unabhängig von der verwendeten Implementierung. Einmal implementiert, profitieren Clients von jedem Relay, das HLL unterstützt.

**Aktueller Status:**

Von fiatjaf eröffnet, war der PR mehrere Monate in Diskussion, bevor er diese Woche gemergt wurde. Relay-Implementierungen müssen HLL-Berechnung zu ihren COUNT-Handlern hinzufügen, Client-Implementierungen brauchen HLL-Zusammenführung in ihrer Zählaggregationslogik.

## NIP Deep Dive: NIP-96 (HTTP-Dateispeicherung) und der Übergang zu Blossom

[NIP-96](/de/topics/nip-96/) ([Spec](https://github.com/nostr-protocol/nips/blob/master/96.md)) definierte, wie Nostr-Clients Dateien auf HTTP-Medienservern hochladen, herunterladen und verwalten. Inzwischen als „nicht empfohlen" zugunsten von [Blossom](/de/topics/blossom/) (BUD-basiertes Medien-Hosting) markiert, bleibt NIP-96 diese Woche relevant, weil Angor v0.2.5 [NIP-96-Serverkonfiguration hinzugefügt hat](#angor-v025) und ZSP v0.3.1 [auf Blossom-Server hochlädt](#zsp-v031), was einen Protokollübergang in Aktion zeigt.

**Wie NIP-96 funktioniert:**

Fähigkeiten eines Dateiservers erkennt der Client durch Abruf von `/.well-known/nostr/nip96.json`, das API-URL, unterstützte Inhaltstypen, Größenlimits und verfügbare Medientransformationen zurückgibt:

```json
{
  "api_url": "https://file-server.example/api",
  "download_url": "https://cdn.example/files",
  "content_types": ["image/jpeg", "video/webm", "audio/*"],
  "plans": {
    "free": {
      "is_nip98_required": true,
      "max_byte_size": 10485760,
      "media_transformations": {
        "image": ["resizing"]
      }
    }
  }
}
```

Zum Hochladen sendet der Client einen `multipart/form-data` POST an die API-URL mit einem [NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md)-Autorisierungs-Header (ein signiertes Nostr-Event, das die Identität des Uploaders beweist). Zurück kommt eine [NIP-94](/de/topics/nip-94/) Dateimetadaten-Struktur mit Datei-URL, Original- und transformierten SHA-256-Hashes, MIME-Typ und Abmessungen:

```json
{
  "status": "success",
  "nip94_event": {
    "tags": [
      ["url", "https://cdn.example/files/<hash>.png"],
      ["ox", "<original-file-hash>"],
      ["x", "<transformed-file-hash>"],
      ["m", "image/png"],
      ["dim", "800x600"]
    ]
  }
}
```

Downloads verwenden GET-Anfragen an `<api_url>/<sha256-hash>`, mit optionalen Abfrageparametern wie Bildgrößenänderung (z.B. Breite 320). Löschung erfolgt per DELETE mit NIP-98-Auth, und nur der ursprüngliche Uploader kann seine Dateien löschen. Paginierte Ergebnisse der Uploads lassen sich per Dateilistungs-Endpunkt abrufen.

Zur Deklaration bevorzugter Upload-Server veröffentlichen Nutzer kind 10096 Events, sodass Clients den richtigen Server automatisch auswählen.

**Warum es als veraltet markiert wurde:**

NIP-96 band Datei-URLs an bestimmte Server. Fiel `files.example.com` aus, verlor jede Nostr-Notiz, die darauf verwies, ihre Medien. Fragil war die Adresse, weil der Server selbst die Adresse war.

[Blossom](/de/topics/blossom/) (Blobs Stored Simply on Mediaservers) kehrt dies um, indem der SHA-256-Hash des Dateiinhalts zur kanonischen Kennung wird. Jede Blossom-URL enthält den Hash (`https://blossom.example/<sha256>.png`), aber jeder Blossom-Server, der dieselbe Datei hostet, liefert sie unter demselben Hash-Pfad. Verschwindet ein Server, fragen Clients einen anderen nach demselben Hash ab. Content-Adressierung macht Daten standardmäßig serverübergreifend portabel.

Blossom vereinfacht auch die API. NIP-96 verwendete Multipart-Form-Uploads mit JSON-Antworten, Transformationsrichtlinien und einem Discovery-Endpunkt. Blossom setzt auf einfachen PUT, GET und signierte Nostr-Events (statt HTTP-Header) zur Autorisierung. Aufgeteilt ist die Blossom-Spezifikation in modulare Dokumente: BUD-01 (Server-Protokoll, Autorisierung, Abruf), BUD-02 (Blob-Upload), BUD-03 (Nutzerserver) und BUD-04 (Spiegelung zwischen Servern).

Im September 2025 erfolgte die Markierung als veraltet via [PR #2047](https://github.com/nostr-protocol/nips/pull/2047), der NIP-96 im NIPs-Index als „nicht empfohlen" kennzeichnete.

**Der Übergang in der Praxis:**

Server wie nostr.build und void.cat unterstützten NIP-96 und haben Blossom-Endpunkte hinzugefügt oder dorthin migriert. In unterschiedlichen Stadien befinden sich die Clients: Angors v0.2.5-Release diese Woche fügte NIP-96-Serverkonfiguration hinzu, während ZSPs v0.3.1-Release Artefakte ausschließlich auf Blossom-Server mit `Content-Digest`-Headern hochlädt. Amethyst und Primal unterstützen Blossom-Uploads. Fortbestehen wird die Koexistenz wahrscheinlich, bis die verbleibenden NIP-96-Implementierungen ihre Migration abschließen.

**Was übernommen wird:**

Kind 10096 Server-Präferenz-Events bleiben nützlich. NIP-94-Dateimetadaten (kind 1063 Events) beschreiben Dateieigenschaften weiterhin unabhängig vom verwendeten Upload-Protokoll. Zur Grundlage von Blossoms Content-Adressierung wurde das SHA-256-Hashing, das NIP-96 nutzte. NIP-96s Design informierte, was Blossom vereinfacht hat: Medien-Hosting in einem dezentralisierten Netzwerk erfordert inhaltsadressierten Speicher, um der Zensurresistenz der Relay-Schicht zu entsprechen.

---

Das war's für diese Woche. Wer etwas baut, Neuigkeiten hat oder sein Projekt vorgestellt sehen möchte, kann sich <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">per NIP-17 DM an uns wenden</a> oder uns auf Nostr finden.
