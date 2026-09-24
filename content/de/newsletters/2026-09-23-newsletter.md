---
title: "Nostr Compass #41"
date: 2026-09-23
publishDate: 2026-09-23
draft: false
type: newsletters
description: "Nostr Compass #41 berichtet über lesbare Namen im FIPS-Mesh, das Fernentsperren verschlüsselter Root-Partitionen über FIPS, MintRadar, Grains Relay-Release-Kandidaten, Marmot Protocol 0.10.4, White Noise Androids Version für verschlüsselte Chats, neue Web-of-Trust-Werkzeuge, napplet.soy, RelayKit, Threshold Sessions, aktuelle Protokollarbeit und ausführliche Einblicke in eigene Emojis und Videoereignisse."
translationOf: /en/newsletters/2026-09-23-newsletter.md
translationDate: 2026-09-24
---

Willkommen zurück bei [Nostr Compass](https://nostrcompass.org), Ihrem wöchentlichen Leitfaden für Nostr.

**Diese Woche:** [fips2go](#fips2go-070-keeps-the-mesh-connected-through-bootstrap-failures) ergänzt Ersatzverbindungen im Mesh und optionales Peer-Discovery über Nostr. [fips-initramfs](#fips-initramfs-opens-encrypted-roots-over-fips-before-boot) erklärt in einem Nachtrag zur Veröffentlichung vom 6. September, wie sich verschlüsselte Root-Partitionen aus der Ferne entsperren lassen. [MintRadar](#mintradar-makes-cashu-mints-easier-to-compare) erleichtert den Vergleich von Cashu-Mints. [Grain 0.8.0-rc4](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc4) zeigt den Zustand des Relays in einem Betreiber-Dashboard, während [Marmot Protocols MDK](#marmot-protocol-0104-makes-local-sends-durable) lokale Sendungen und den Abruf von Anhängen dauerhaft absichert. [White Noise Android](#white-noise-android-2026921-improves-encrypted-chat-reliability-and-sharing) verbessert die Zustellung privater Chats, Sprachfunktionen und das Teilen von Profilen. Zu den vorgestellten Projekten zählen [napplet.soy](#nappletsoy-publishes-small-sandboxed-nostr-programs), [RelayKit](#relaykit-installs-a-self-hosted-nostr-stack) und [Threshold Sessions](#threshold-sessions-turn-coding-transcripts-into-private-training-data). Zusammengeführte Änderungen schließen [Sicherheitslücken in 0xchat](#0xchat-merges-fixes-for-signing-message-authentication-and-redirect-flaws) und [eine PIN-Offenlegung in nos2x-fox](#nos2x-fox-closes-a-pin-exposure-path); hinzu kommen [Relay-Zustandsereignisse in nostream](#nostream-publishes-relay-health-events), [Bildbeschreibungen in Zap Cooking](#zap-cooking-publishes-image-descriptions-and-blocks-secret-key-searches) und [Blossom-Uploads in Conduit](#conduit-uploads-product-images-through-blossom). Bei den Protokollen geht es um Spitznamen, Relay-Verwaltung, Nachweise für Zahlungsadressen, Blossom-Verzeichnisse, Moderation verschlüsselter Gruppen und Budgets für Nostr Wallet Connect. Die ausführlichen Beiträge erläutern [eigene Emojis nach NIP-30](#nip-30-custom-emoji) und [Videoereignisse nach NIP-71](#nip-71-video-events).

## Die wichtigsten Meldungen

### fips2go 0.7.0 hält das Mesh auch bei Bootstrap-Ausfällen verbunden {#fips2go-070-keeps-the-mesh-connected-through-bootstrap-failures}

[fips2go](https://github.com/fr34aky/fips2go) ist ein Android-Client, mit dem ausgewählte Anwendungen Peers und Dienste über das FIPS-verschlüsselte Mesh erreichen können. [Version 0.6.0](https://github.com/fr34aky/fips2go/releases/tag/v0.6.0) fügte gerätelokale Mesh-Namen wie `home.fips` hinzu. Die nachfolgende [Version 0.6.1](https://github.com/fr34aky/fips2go/releases/tag/v0.6.1) behebt die Bootstrap-Adressauswahl auf IPv6-Carriern mit DNS64/NAT64; sein Maintainer hat diese Behebung nicht in einem echten DNS64-Netzwerk getestet.

Das neue [Version 0.7.0](https://github.com/fr34aky/fips2go/releases/tag/v0.7.0) verbindet sich standardmäßig mit drei regionalen Bootstrap-Peers, anstatt sich auf einen zu verlassen. Es kann auch einen konfigurierten Peer an Nostr-beworbenen Endpunkten wiederholen, wenn sich seine statische Adresse ändert. Optionale Open Discovery fügt höchstens drei kürzlich von Nostr angekündigte Peers hinzu, bleibt aber standardmäßig ausgeschaltet: Der Maintainer berichtet, dass viele öffentliche Test-Mesh-Ankündigungen nicht mehr antworten. Der ARM64 Build wurde über die vorherige Version installiert und auf einem physischen Pixel überprüft; die anderen Gerätearchitekturen haben eine engere Verifizierung.

### fips-initramfs öffnet verschlüsselte Root-Partitionen vor dem Booten über FIPS {#fips-initramfs-opens-encrypted-roots-over-fips-before-boot}

[fips-initramfs](https://github.com/jmcorgan/fips-initramfs) ist ein Linux-Initramfs-Paket, das einen FIPS-Mesh-Knoten vor dem normalen Booten startet, so dass ein Operator einen LUKS-verschlüsselten Root über seinen npub-adressierten Knoten aus der Ferne öffnen kann. Das vom Benutzer eingereichte [Version 0.1.0](https://github.com/jmcorgan/fips-initramfs/releases/tag/v0.1.0), das am 6. September veröffentlicht wurde, enthält den Mesh-Client, den SSH-Zugriff und Passphrase-Eingabeskripte für Systeme, die ein unbeaufsichtigtes oder fernverschlüsseltes Root-Startup benötigen.

Die [erste Version](https://github.com/jmcorgan/fips-initramfs/releases/tag/v0.1.0) dokumentiert die Sicherheitsabwägungen, anstatt sie zu verbergen: Die Initramfs enthalten den Knotenschlüssel, die Passphrase kreuzt SSH über FIPS und der lokale Konsolenpassphraseneintrag bleibt verfügbar. Dieser Aufholartikel stammt aus einer früheren Benutzereingabe; Die Version vom 6. September fällt außerhalb des aktuellen Sammlungsfensters.

### Grain 0.8.0-rc4 macht den Zustand des Relays im Dashboard sichtbar {#grain-080-rc4-turns-relay-health-into-an-operator-dashboard}

[Grain](https://github.com/0ceanSlim/grain) ist ein selbst gehostetes Nostr-Relay mit integriertem Referenzclient und Administrationsschnittstelle. [Version 0.8.0-rc4](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc4) fügt ein Live-Statusanzeige für Ereignisvolumen, Verbindungen, Betriebszeit, Arbeitsspeicher, Datenspeicher und Zustand des Schreibprozesses sowie pro-Kind-Speicherkarten und neu organisierte Zugriffs-, Richtlinien- und Aufbewahrungskontrollen hinzu.

Der [Release Candidate](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc4) erweitert darüber hinaus die Suche nach fehlenden Ereignissen vom lokalen Relais zu Autoren-Outbox-Relais, eingebetteten Relaishinweisen und der NIP-50-Suche. NIP-50 standardisiert relayseitige Suchfilter, während NIP-01 die Kernereignis- und Abonnementregeln definiert, die Identifier und Author Prefix Matching enthalten. Grain fügt diese Präfix-Übereinstimmungen und konfigurierbaren Volltexttypen in seine Datenbank ein, während das Release-Candidate-Label deutlich macht, dass Betreiber das neue Dashboard- und Datenbankverhalten testen sollten, bevor sie es als stabile Linie behandeln.

### Marmot Protocol 0.10.4 speichert ausgehende Nachrichten dauerhaft {#marmot-protocol-0104-makes-local-sends-durable}

[Marmot Protocol's MDK](https://github.com/marmot-protocol/mdk) ist ein SDK für MLS-verschlüsselte Gruppennachrichten, deren Transport und Discovery über Nostr laufen. [Version 0.10.4](https://github.com/marmot-protocol/mdk/releases/tag/v0.10.4) hält lokale Sendungen vor der Netzwerkvervollständigung aufrecht, senkt die Latenzzeit von Draft- und Pending-Message-Nachrichten, verhindert wiederholte automatische Anhänge-Downloads und stellt den Aufbewahrungszustand in Chatlisten-Vorschauen frei.

[Dieselbe Version](https://github.com/marmot-protocol/mdk/releases/tag/v0.10.4) fügt Gruppenerstellung zu Agent-Control-Integrationen und Opt-in-Reaktionszustimmung für Genehmigungsaufforderungen hinzu. Es repariert auch ein Halt-Wrapper-Edge und begrenzt das Wiederholen von Backoffs während des Epochen-Backfills und setzt die Zuverlässigkeitsarbeit nach 0,10,0 fort, ohne die Anforderung zu ändern, dass generierte Bindungen und native Bibliotheken zusammenrücken.

### MintRadar erleichtert den Vergleich von Cashu-Mints {#mintradar-makes-cashu-mints-easier-to-compare}

[MintRadar](https://mintradar.org) ist ein datenschutzorientiertes Cashu-Dashboard, das Nostr verwendet, um Minzen zu entdecken und Community-Bewertungen an signierte Identitäten zu binden. Seine [aktueller Quellcode](https://github.com/hroomnik007/MintRadar) Hinzufügen von persistenten NIP-87-Mint-Ankündigungen, Erkennung des gleichen Betreibers von NUT-06-Pubkeys, gemeinsam nutzbaren Vergleichs-URLs und Nostr `naddr` Deep Links.

NIP-87 standardisiert Erkennungs- und Überprüfungsereignisse für Cashu-Münzen, während NUT-06 das Münzinformationsdokument definiert, das die öffentlichen Schlüssel und unterstützten Funktionen einer Mint offenlegt. A [signiertes vom Benutzer eingereichtes Update](https://njump.to/nevent1qqs9hwth0rgsprqaml9xuuve2s47x08w2ltjujgwwr4zyqw0qjptecqpzamhxue69uhhyetvv9ujuurjd9kkzmpwdejhgtczyqt40x2js6hcc27delgn5vqwn3qtcjn8uas3rrzmxe2hxsrvdvmmcqcyqqqqqqgyqg6ap) MintRadar zurück in die Aufnahme gebracht, nachdem es in einem früheren Durchgang verpasst wurde; Das Projekt hat seitdem erhebliche Stromfensterarbeiten um diese Vergleichs- und Entdeckungspfade angesammelt.

### Nostr WoT Oracle 0.3.1 sichert Vertrauensabfragen auch nach Neustarts ab

[Nostr WoT Oracle](https://github.com/nostr-wot/nostr-wot-oracle) ist ein Server, der öffentliche Folge- und Stummschaltungsereignisse aufnimmt und Antworten auf begrenzte Web-of-Trust-Pfadabfragen beantwortet. [Versionen 0.3.0 und 0.3.1](https://github.com/nostr-wot/nostr-wot-oracle/releases/tag/v0.3.1) fügen unabhängig persistente öffentliche stumme Beweise, Bereitschafts- und Aufnahmestatus, revisionsgebundene Caches, deterministische Auswahl austauschbarer Ereignisse und Rollback-Verhalten hinzu, das verhindert, dass unpersistierte Graphenänderungen abfragbar werden.

Der [0.3.1 performance pass](https://github.com/nostr-wot/nostr-wot-oracle/releases/tag/v0.3.1) stellt Graphkanten direkt in numerische Adjacency-Listen wieder her, führt vor der Veröffentlichung eine Verschmelzung von überholten Folge- und Stumm-Ereignissen durch und bündelt Distanz-Cache-Misss. Diese Änderungen sind für Clients wichtig, die eine erklärbare Folgedistanz oder stumme Beweise benötigen, ohne ein Beziehungsdiagramm aus einer älteren Revision stillschweigend zu bedienen.

### Nostr WoT SDK 1.0.2 komprimiert die Graphspeicherung im Browser

[Nostr WoT SDK](https://github.com/nostr-wot/nostr-wot-sdk) ist ein JavaScript-Toolkit zum Crawlen, Speichern und Abfragen von Nostr-Folgegraphen in Anwendungen. [Version 1.0.2](https://github.com/nostr-wot/nostr-wot-sdk/releases/tag/nostr-wot-sdk%401.0.2) verwendet eine Graph-Engine, die bis zu 100 Autoren pro Relay-Request batchet, Edges mit kompakter Delta-Codierung speichert, kompatible Traversals wiederverwendet und Batch-Distanzabfragen aussetzt.

Die [Speichermigration in graph 0.3.0](https://github.com/nostr-wot/nostr-wot-sdk/releases/tag/%40nostr-wot/graph%400.3.0) aktualisiert IndexedDB-Namespaces auf Schema 2 und kann nicht von älteren SDK-Versionen wieder geöffnet werden. Anwendungen, die ein Rollback benötigen, sollten einen separaten Namespace verwenden oder den aktualisierten Graphen löschen, anstatt davon auszugehen, dass der frühere Client ihn lesen kann.

### napplet.soy veröffentlicht kleine Nostr-Programme in einer Sandbox {#nappletsoy-publishes-small-sandboxed-nostr-programs}

[napplet.soy](https://napplet.soy) ist ein Web-Spielplatz- und Creator-Toolkit zum Erstellen, Veröffentlichen, Abspielen, Inspizieren und Remixen kleiner Sandbox-Nostr-Programme namens Napplets. NIP-34 definiert signierte Nostr-Events für Git Repository Discovery und Collaboration. Die [soyLI 0.18.2 release](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.18.2) folgt auf den Projektstart im September mit signierten Listen, Blossom-gehosteten Assets, Git- und NIP-34-Quellenreferenzen und von Relais entdeckten Manifesten.

Die [Projektquelle](https://github.com/zeSchlausKwab/napplet-soy) hält Netzwerk- und Speicherzugriff hinter deklarierten Funktionen, anstatt jedem Napplet uneingeschränkte Browserberechtigung zu geben. Die Projektidentität bleibt ungelöst, da die kanonische Site und das Repository kein Projekt oder Maintainer npub binden, so dass hier kein Identitätsanspruch beigefügt ist.

Die [CLI-Version soyLI 0.20.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.20.0) fügt begrenzte NIP-78-Helfer hinzu, um wiederverwendbare öffentliche Tracks, Puzzles, Zeichnungen und Presets sowie strukturierte Daten zu hohen Punktzahlen zu teilen. Schreibe werden auf ein napplet und spieleridentität mit zustimmung und revisionsprüfungen beschränkt; verknüpfte große assets verwenden blossom. Website- und Backend-Funktionen erfordern eine separate Bereitstellung, so dass das CLI-Tag allein nicht beweist, dass diese öffentlichen Funktionen auf der Website live sind.

### RelayKit installiert einen selbst gehosteten Nostr-Stack {#relaykit-installs-a-self-hosted-nostr-stack}

[RelayKit](https://relayk.it) ist ein One-Command-Installationsprogramm für einen selbst gehosteten Nostr-Stack, der Relais, Blossom-Medien, Websites, Git-Dienste und Benachrichtigungen enthalten kann. RelayKit packt jetzt einen breiteren Stapel als der Browser-Relay-Discovery-Client, der im April abgedeckt wurde. [Current Source Repository](https://github.com/samthomson/relaykit) dokumentiert die neue betreiberorientierte Einsatzfläche.

Seine [Aufstellungsort](https://relayk.it) stellt die Dienste als einen koordinierten Stapel dar, anstatt von den Betreibern zu verlangen, jede Komponente unabhängig zusammenzustellen. Diese Abdeckung behandelt daher RelayKit als eine geänderte Projektrichtung, nicht als sein erstes Aussehen.

### Threshold Sessions macht aus Coding-Transkripten private Trainingsdaten {#threshold-sessions-turn-coding-transcripts-into-private-training-data}

[Threshold Sessions](https://gitworkshop.dev/npub17m2ual3pdjvhd8yc6a3m8snzjsgnmtl26hwen48ne937qgyjyshs2zgvse/relay.ngit.dev/threshold) ist ein Kommandozeilen-Tool, das KI-Codierungssitzungen in normalisierte, redigierte und verschlüsselte Trainingsdaten-Epochen konvertiert. Sein Repository unterstützt Codex, Claude Code, Cursor, OpenCode und Pi-Transkripte, speichert verschlüsselte Artefakte auf Blossom und veröffentlicht signierte Referenzen über Nostr.

Recent [Threshold Sessions source history](https://relay.ngit.dev/npub17m2ual3pdjvhd8yc6a3m8snzjsgnmtl26hwen48ne937qgyjyshs2zgvse/threshold.git) fügt Zeitstempel-Randomisierung, Provenienz, Extraktoren und ein Ledger für produzierte Epochen hinzu. Das Design ermöglicht es einem Mitwirkenden, die Auditierbarkeit und die spätere Datennutzung zu erhalten, ohne das lesbare Sitzungsprotokoll in Relais zu veröffentlichen.

## Versionen mit Release-Tag

### White Noise Android 2026.9.21 verbessert die Zuverlässigkeit verschlüsselter Chats und das Teilen {#white-noise-android-2026921-improves-encrypted-chat-reliability-and-sharing}

[White Noise Android](https://github.com/marmot-protocol/whitenoise-android/releases/tag/android-v2026.9.21) ist ein Nostr-basierter Messenger für private Marmot-verschlüsselte Gruppengespräche. Die Veröffentlichung vom 21. September verbessert die Übermittlung von Nachrichten, Sprachdiktat, Text-zu-Sprache, Konversationsnavigation, Kontowechsel und AMOLED-Erscheinungsbild. Es fügt auch teilbares Profil hinzu und lädt QR-Karten und Gruppenaktionen aus Profilen ein.

### Nostr Mail Client 0.16.0 bietet Zustelloptionen für einzelne Empfänger

[Nostr Mail Client](https://github.com/nogringo/nostr-mail-client) ist ein Web-, Desktop- und Android-Mail-Client, der Nachrichten über Nostr-Relays austauscht und gleichzeitig die herkömmliche E-Mail-Zustellung unterstützt. [Version 0.16.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.16.0) ermöglicht es einem Absender, SMTP- oder Nostr-Lieferung für jeden Empfänger auszuwählen und Standort, Erfassungszeit und Gerätemetadaten von Fotos und Videos vor dem Hochladen zu entfernen.

Die [Version](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.16.0) erfordert auch, dass jedes Konto eine Relay-Liste erstellt, mindestens ein Relay konfiguriert hält und eine sicherere dauerhafte Löschung aus dem Müll hinzufügt. Diese Änderungen machen Routing und Anhang Privatsphäre explizit an dem Punkt, an dem eine gemischte E-Mail / Nostr Nachricht das Gerät verlässt.

### Amber 6.6.5 trennt die Backup-Verschlüsselung von App-Berechtigungen

[Amber](https://github.com/greenart7c3/Amber) ist ein Android-Unterzeichner, der Nostr private Schlüssel außerhalb der Anwendungen hält, die Signaturen oder Verschlüsselung anfordern. NIP-44 standardisiert verschlüsselte Nutzlasten zwischen Nostr-Schlüsseln, während NIP-46 das Signieren und Verschlüsseln einer Anwendungsanforderung von einem Fernsignierer über Relais ermöglicht. [Version 6.6.5](https://github.com/greenart7c3/Amber/releases/tag/v6.6.5) verschlüsselt Anwendungs-Backups mit einem dedizierten Schlüssel, der aus dem Kontoschlüssel abgeleitet wird, und verhindert, dass eine Anwendung mit erinnerter NIP-44-Entschlüsselungsberechtigung Backup-Nutzlasten liest, die lokale Schlüssel oder NIP-46-Geheimnisse pro App enthalten.

Der [Migrationspfad](https://github.com/greenart7c3/Amber/releases/tag/v6.6.5) kann immer noch ältere identitätsverschlüsselte Backups wiederherstellen, bis die nächste Veröffentlichung sie ersetzt, und die Veröffentlichung behebt eine Wiederherstellungsaufforderung, die nach dem Ausloggen verschwand, als das Backup-Publishing deaktiviert wurde. Benutzer erhalten sowohl eine engere Berechtigungsgrenze als auch einen Wiederherstellungspfad für bestehende Backups.

### Amethyst 1.16.0 sichert die Blossom-Signierung ab und ergänzt BOLT12-Angebote

[Amethyst](https://github.com/vitorpamplona/amethyst) ist ein Android Nostr-Client mit Medien-, Wallet- und Signer-Integrationen. [Version 1.16.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.16.0) behebt die schnelle Blossom-Leseberechtigung, so dass gleichzeitige Medienanfragen einen Signaturvorgang während des Fluges gemeinsam nutzen und den Token-Cache erneut überprüfen, bevor eine weitere Signatur angefordert wird. Die verschlagwortete Version stellt auch die standardmäßig gepolsterte Base64 für Blossom-Auth-Token wieder her.

[Version 1.16.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.16.0) unterstützt auch BOLT12-Angebote in Profilzahlungen und dem Zap-Picker, wobei BOLT11-Fallback, wenn ein Angebot abgelehnt wird. Benutzer erhalten einen angebotsbasierten Zahlungsweg, während bestehende rechnungsbasierte Zahlungen verfügbar bleiben.

### Alby Extension 3.15.0 sichert Anfragen von Websites ab

[Alby Extension](https://github.com/getAlby/lightning-browser-extension) ist eine Browser-Wallet und ein Nostr-Signer, der Websites Lightning- und Signierfunktionen gewährt. [Version 3.15.0](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.15.0) blockiert von der Website bereitgestellte LNURLs von lokalen oder privaten Netzwerkadressen, erfordert eine LNURL-auth-Bestätigung über den Host und entfernt die erinnerte Genehmigung für rohe Schnorr-Signierungsmethoden.

Die [Sicherheitsversion](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.15.0) belastet auch Zulagenbudgets, bevor sie gleichzeitige Zahlungen sendet, und entfernt die generische WebLN-Anforderungsmethode. Integratoren müssen dedizierte WebLN-Methoden verwenden, während Benutzer klarere Grenzen für Netzwerkziele, Authentifizierungshosts und Ausgabenlimits für Websites erhalten.

### LaWallet NWC 2.7.1 vereinheitlicht Zap-Belege für verschiedene Wallets

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc) ist ein Open-Source Lightning Wallet Service, der Konten über Nostr Wallet Connect Anwendungen aussetzt. NIP-57 standardisiert signierte Lightning-Zap-Anfragen und Abrechnungsbelege für Nostr-Profile und -Ereignisse. [Version 2.7.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.7.0) entkoppelt diese Empfangsveröffentlichung von Wallet-spezifischen Abwicklungspfaden, so dass jede unterstützte NWC-Wallet Zap-Belege aussenden kann, dann [2.7.1.](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.7.1) Bringt Empfangs- und Aktivitätsbildschirme auf den gleichen Empfangsfluss wie Sends.

Das [Paket 2.7.1](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.7.1) StartOS-Speicher- und Backup-Layout auch zwischen Sideload- und Community-Paketen anpasst. Betreiber, die die erste 2.7.0 Sideload aktualisieren, benötigen das korrigierte Paket, bevor sie sich auf den Datenbankvolumenübergang verlassen.

### NoorNote 1.6.0–1.7.0 ergänzt Kalender und Terminbuchungen

[NoorNote](https://github.com/77elements/noornote) ist eine Nostr-Notizenanwendung mit optionalen Produktivitätsmodulen und lokalen Erinnerungen. [Version 1.6.0](https://github.com/77elements/noornote/releases/tag/v1.6.0) fügt öffentliche und verschlüsselte Kalenderereignisse, Monats-, Wochen- und Listenansichten, Android-Erinnerungen und interaktive Zeitleistenkarten für gemeinsame Ereignisse hinzu.

[Version 1.6.1](https://github.com/77elements/noornote/releases/tag/v1.6.1) organisiert Addons in ein Pro-Account-Dashboard und behebt URLs, die `naddr`- oder `npub`-Kennungen enthalten, die als Karten oder Erwähnungen falsch gelesen werden. Diese Korrekturen erleichtern das Auffinden von Addon-Steuerelementen und halten Nostr-Identifikatoren in normalen Links intakt.

[Version 1.7.0](https://github.com/77elements/noornote/releases/tag/v1.7.0) ermöglicht es einem konto, verfügbare termin-slots zu teilen und buchungen und stornierungen per direktnachricht zu erhalten. Es importiert und exportiert auch Kalenderdaten als `.ics`, bewahrt die Web-NWC-Wallet-Verbindung nach IndexedDB-Räumung und vermeidet falsche Erwähnungen in Links, die npubs enthalten.

### Citrine 3.2.0 begrenzt den Speicherbedarf des Relay-Aggregators

[Citrine](https://github.com/greenart7c3/Citrine) ist ein Android Nostr-Relay, das anderen Anwendungen einen lokalen Event-Store und eine Relaisschnittstelle bietet. [Version 3.2.0](https://github.com/greenart7c3/Citrine/releases/tag/v3.2.0) streamt Matching-Ereignisse in Batches, caps Aggregator Fan-out bei 200 Relais und bounds caches, um zu verhindern, dass große Abfragen den Speicher ausschöpfen.

Die [Version](https://github.com/greenart7c3/Citrine/releases/tag/v3.2.0) deckt auch Ausfälle aus dem Speicher im In-App-Log auf und lässt die Operatoren das Ereignisdiagramm ausblenden. Ein Telefon, das sowohl als Relais als auch als Aggregator fungiert, versagt jetzt sichtbarer und hält eine definierte Speichergrenze.

### Wisp 1.2.4 ruft Threads über Inbox-Relays ab

[Wisp.](https://github.com/barrydeen/wisp) ist ein datenschutzorientierter Nostr-Client mit eingebauter Cashu- und Lightning-Wallet-Unterstützung. NIP-22 definiert generische Art `1111` Kommentare, die auf viele Arten von Nostr-Inhalten antworten können. [Version 1.2.4](https://github.com/barrydeen/wisp/releases/tag/v1.2.4) sendet Threads und Benachrichtigungen nur an Posteingangsrelais, behandelt diese Kommentare als Antworten und ermöglicht es Benutzern, ihren vollen Geldbeutelsaldo in der Kette abzuheben.

[Version 1.2.4](https://github.com/barrydeen/wisp/releases/tag/v1.2.4) beschränkt Thread Reads auf Posteingangsrelais und reduziert unnötige Relais-Exposition. Sein NIP-22-Handling hält Kommentare in Threads, Zählungen und Benachrichtigungen sichtbar.

### nostr-wot-extension 0.8.3 ergänzt NWC-Verbindungen mit eigenen Berechtigungen

[nostr-wot-extension](https://github.com/nostr-wot/nostr-wot-extension) ist ein Browser-Signer und eine Identitätserweiterung mit Wallet-Zahlungen und lokaler Web-of-Trust-Analyse. [Version 0.8.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.0) stellt seine experimentelle Web-of-Trust-API als reines Menü-Opt-in mit lokalen, Remote- und Hybrid-Abfragemodi, skalierbarer Graphensynchronisation, stummgeschaltetem Scoring und Speichersteuerungen pro Konto wieder her.

Die [Version](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.0) erfordert auch eine Bestätigung, bevor eine bekannte Folgeliste durch null oder einen Kontakt ersetzt wird, selbst wenn eine gespeicherte Berechtigung oder ein Fernsignierer vorhanden ist. Dieser Wächter verwendet verifiziertes Relais, signiertes Ereignis und synchronisierte Graphenhistorie, um destruktive Folgelistenänderungen schwerer zu genehmigen.

[Version 0.8.3](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.3) Erstellt separate Nostr Wallet Connect-Verbindungen für Anwendungen mit seiner LNbits-Wallet. Jeder kann einen Namen, ein tägliches Ausgabenlimit und einen Ablauf mit lokaler geheimer Speicherung, Budget-Sichtbarkeit und Widerruf haben. Der Live-Test des Projekts umfasste die Verbindungserstellung, den Widerruf und eine unterzeichnete `get_info` Austausch, keine echte Zahlung; Browser-Store-Publikation ist getrennt von der Quellversion.

### pakstr 0.22.0–0.24.0 übergibt Android-Signaturanfragen an externe Signer

[pakstr](https://git.nostrdev.com/stuff/pakstr) bündelt Webanwendungen mit nativen Nostr-Funktionen. Die letzte Woche behandelte die Verpackungssequenz 0.21.x. Die neue [0.22.0 release](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.22.0) fügt die NIP-55-Signierung über den NIP-46-Bunker hinzu, wodurch eine Android-Anwendung Unterschriftsanfragen an einen externen Unterzeichner übergeben kann. [Version 0.23.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.23.0) setzt dann die Laufzeit-API-Adresse über Neustarts hinweg fort.

[Version 0.24.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.24.0) veröffentlicht das Zapstore-Symbol; diese kosmetische Änderung ist nicht der Meilenstein des Unterzeichners. NostrAppShell-Einträge zeigen auf die gleiche Paketserie, so dass sie hier einmal abgedeckt sind.

### Nail 0.2.2 stellt E-Mails auch ohne fehlgeschlagene Anhänge zu

[Nail](https://github.com/formstr-hq/nail) ist eine Bridge und Anwendung, die Nostr-Nachrichten in E-Mail-Workflows überträgt. [Version 0.2.2](https://github.com/formstr-hq/nail/releases/tag/v0.2.2) ruft eine Nachricht ohne Anhänge zurück, wenn ein Relais die Anhängenutzlast ablehnt, eine Größenobergrenze hinzufügt, um einen Brückenneustart zu verhindern, und das Standard-Bridge-Relais ändert.

Das [App-Update](https://github.com/formstr-hq/nail/releases/tag/v0.2.2) stellt auch die Linköffnung und die Opt-in-Bildanzeige wieder her. Die Lieferung kann sich nun auf den Nachrichtentext verschlechtern, anstatt die gesamte E-Mail zu verlieren, wenn der Anhängepfad fehlschlägt.

### Mostro CLI 0.16.2 entfernt den alten Chat-Transport

[Mostro CLI](https://github.com/MostroP2P/mostro-cli) ist ein Terminal-Client für die Koordination von Peer-to-Peer-Bitcoin-Trades über das Nostr-Protokoll von Mostro. [Version 0.16.2](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.2) entfernt den Version-One-Geschenk-Wrap-Dual-Lese- und Dual-Write-Pfad, migriert den Peer-Chat zum aktuellen Umschlag und lässt einen Trader den Solver durch den Streit-Chat erreichen.

Die [Version](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.2) fügt auch einen Operatorbefehl für die Stornierung ausstehender Bestellungen hinzu. Bereitstellungen sollten die Erwartungen von Client und Koordinator gemeinsam aktualisieren, da der alte Chat-Transport kein Rückfall mehr ist.

### Dart NDK dev.4–dev.5 ergänzt signierte App-Updates und sichert die Relay-Zustellung ab

[Dart NDK](https://github.com/relaystr/ndk) ist eine Dart-Clientbibliothek für Relaisverbindungen, Signieren, Caching, Wallet-Operationen und Nostr-Anwendungsstatus. NIP-82 standardisiert signierte Anwendungsfreigabe-Metadaten und herunterladbare Artefakte. [Version 0.10.0-dev.4](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.4) fügt NIP-82 application-update support hinzu; [dev.5](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.5) macht Cashu Quote Recovery wieder herstellbar und lässt eine Sendung die Identität deklarieren, der sie zugeordnet werden kann.

quer [Das Dev.5 Release](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.5)Die Bibliothek vermeidet anonyme Verbindungen, wenn eine Sendung eine Authentifizierung erfordert, und stoppt das Aufwachen von Relais für Lieferungen, die auf einer fehlenden Identität geparkt sind. Anwendungen, die diese Vorabversion annehmen, sollten Migrationsarbeit in ihren Broadcast- und Wallet-Integrationen ermöglichen.

### BitBlik 0.11.0 bringt Streitfälle in die App

[BitBlik](https://github.com/bit-blik/bitblik) ist ein mobiler Peer-to-Peer-Bitcoin-Handelsclient, der Bestellungen und Chat über Nostr koordiniert. [Version 0.11.0](https://github.com/bit-blik/bitblik/releases/tag/v0.11.0) fügt den Koordinator-Streitchat, BOLT12-Auszahlungen, wo unterstützt, Android-Selbstaktualisierungen aus NIP-82-Release-Events und Wallet-Backup und Recovery-Fixes hinzu.

Die [Version](https://github.com/bit-blik/bitblik/releases/tag/v0.11.0) übernimmt auch Rückerstattungen nach Streiturteilen und bewahrt den Wallet-Status während der Neko-Wiederherstellung. Händler können nun für das Streitgespräch innerhalb des Kunden bleiben, anstatt zu einem separaten Koordinatorkanal zu wechseln.

### Scramble 0.7.2 wechselt die MLS-Engine und bietet zwei Android-Oberflächen

[Scramble](https://github.com/DavidGershony/Scramble) ist eine Nostr-basierte verschlüsselte Gruppenchat-Anwendung. Seine [Version 0.7.0](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.0) ersetzt die ehemalige MLS-Engine durch Dark Matter, stellt die Verschlüsselung im Ruhezustand für den Gruppenzustand wieder her und verhindert ein Android-Cloud-Backup der Profildatenbank. Die Migration hat eine wichtige Grenze: Gruppen, die in 0.6.x erstellt wurden, erscheinen nach dem Upgrade **nicht**, obwohl der Kontoschlüssel, die Kontakte, die Relais und die Unterzeichnerpaarung erhalten bleiben.

[Version 0.7.2](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.2) liefert Avalonia und native Android-Ansichtsebenen mit der gleichen App-ID und dem gleichen Release-Zertifikat, so dass man sie übereinander installieren kann, ohne das New-Engine-Konto und die Chats zu löschen. Sie können nicht nebeneinander installiert werden. Der nativen Ansicht fehlen immer noch einige Geräteverwaltungseinstellungen; In den Release Notes des Projekts heißt es, dass Protokoll-Interop getestet wurde, aber es wird kein Real-Device-Gruppenkonversationstest für die Migration von 0.7.0 beansprucht.

### Morganite 0.0.5 ermöglicht das Spulen in Blossom-Medien über Tor

[Morganite](https://github.com/greenart7c3/Morganite) ist ein Android Blossom Media Cache für Nostr-Clients. [Version 0.0.5](https://github.com/greenart7c3/Morganite/releases/tag/v0.0.5) holt Blobs von Tor `.onion` Blossom Servern mit Tor-Aware Retries und honoriert HTTP Range Requests auf einem Cache Miss. Ein Spieler kann in ein nicht zwischengespeichertes Video suchen, während Morganite den vollständigen Cache im Hintergrund ausfüllt, anstatt nur disjunkte angeforderte Scheiben zu speichern.

### Bitcredit 0.5.16 verarbeitet festhängende Nostr-Wechselereignisse erneut

[Bitcredit E-Bills](https://github.com/BitcreditProtocol/Bitcredit-Core) trägt Rechnung, Unternehmen und Identitätsketten durch Nostr Ereignisse. [Version 0.5.16](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.16) repariert die Serialisierungskompatibilität von Ereignis-Signaturen nach dem Nostr 0.45-Abhängigkeitsupgrade, stellt fehlgeschlagene Einträge in der Warteschlange zur Inspektion und Warteschlange frei und synchronisiert fehlende Kettenmetadaten, bevor eine Blockpublikation erneut versucht wird. Diese Änderungen zielen sowohl auf die Kompatibilität mit aktualisierten Daten als auch auf Nachrichten ab, die sonst hängen bleiben würden.

### fips-ts 0.0.43 schützt parallele FIPS-Sitzungen

[fips-ts](https://github.com/mmalmi/fips-ts) liefert die gemeinsam genutzte TypeScript FIPS-Mesh-Laufzeit, die von kompatiblen Clients verwendet wird. Seine [runtime 0.0.43 release](https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.43) bewahrt eine authentifizierte Identität bei gleichzeitiger Einrichtung oder einem aliasierten WebRTC-Transport, der eine Sitzung übergibt, während er eine andere Identität ablehnt. Es verhindert auch, dass abgesagte Verhandlungen und verspätete Rückrufe eine Arbeitsverbindung ersetzen. Dies ist eine Verbindungszuverlässigkeit auf Bibliotheksebene, getrennt von den Änderungen an der Client-Seite von fips2go.

### Bookshelf 0.1.25 macht signierte Buchrezensionen bearbeitbar

[Bookshelf](https://github.com/decent-newsroom/bookshelf-app) ist ein Nostr-verbundener Android-Reader mit Community-Buchbewertungen und privaten Highlights. [Version 0.1.25](https://github.com/decent-newsroom/bookshelf-app/releases/tag/v0.1.25) ermöglicht es den Lesern, ihre signierte Bewertung und schriftliche Bewertung durch einen dauerhaften Posteingang zu überarbeiten. Die App zeigt zwischengespeicherte Bewertungen sofort an, aktualisiert sie online und ersetzt ältere Revisionen durch das neueste Ereignis für dasselbe Buch und denselben Autor.

[release diff](https://github.com/decent-newsroom/bookshelf-app/compare/v0.1.24...v0.1.25) enthält den Review-Editor, den Revisions-Cache, die Relaissynchronisation und Tests. Es normalisiert auch eingefügte `nostr:naddr`-Referenzen, bevor nach den Publikationskoordinaten eines Buches gesucht wird.

### Cordn 0.5.0 reiht verschlüsselte Nachrichten offline ein

[Cordn](https://github.com/Cordn-msg/cordn-web) ist ein verschlüsselter Nostr-Gruppenchat-Client. [Version 0.5.0](https://github.com/Cordn-msg/cordn-web/releases/tag/v0.5.0) stellt Textsendungen in einem dauerhaften Offline-Posteingang in Warteschlangen, erstellt ein Terminal für fehlgeschlagene Einträge bis zu einem erfolgreichen Bestätigungsdurchlauf und nimmt die Koordinator-Chats in der richtigen Reihenfolge wieder auf. Es überprüft auch die NIP-44-Fähigkeit eines Unterzeichners, bevor eine verschlüsselte Aktion angeboten wird, wobei nicht unterstützte Unterzeichner auftauchen, anstatt stillschweigend zu scheitern.

### 21Meetup 1.6.6 stellt Vertrauenspfade über mehrere Kontakte wieder her

[21Meetup](https://github.com/louisthecat86/Einundzwanzig-Meetup-App) stellt Nostr-unterstützte Teilnahmeabzeichen für persönliche Veranstaltungen aus. [Version 1.6.6](https://github.com/louisthecat86/Einundzwanzig-Meetup-App/releases/tag/v1.6.6) stellt Vertrauenspfade zweiten und dritten Grades wieder her, indem die Kontaktdatensätze in begrenzten Phasen abgerufen werden. Fehlgeschlagene Badge-Publikationen können wiederholt werden, und ein Senden gilt erst als erfolgreich, nachdem ein Relais es bestätigt hat. Mehrtägige Veranstaltungen zählen jetzt als ein Anwesenheitsabzeichen anstelle von einem pro Tag.

### TWENTY ONE Companion 1.13.0 erklärt öffentliche Nostr-Anmeldungen

[TWENTY ONE Companion](https://github.com/HolgerHatGarKeineNode/twenty-one-companion) kombiniert Nostr-Räume und Artikel mit Meetup-Auflistungen. [Version 1.13.0](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.13.0) speichert gepinnte Räume und Artikel in Relais und zeigt einen Pin als lokal an, bis ein Relais ihn bestätigt. Berechtigte meetup-rsvps sind öffentliche nostr-events; die app warnt davor, dass relais von drittanbietern sie behalten können, auch wenn ein benutzer ablehnt. Eine Kontaktlistenvorschau weigert sich nun zu veröffentlichen, wenn sich die Liste nach der Überprüfung geändert hat.

### Armada 0.61.0 ergänzt Medienschutz und Mitgliedsverwaltung

[Armada](https://github.com/soapbox-pub/armada) ist ein Nostr-basierter verschlüsselter Community-Client. [Version 0.61.0](https://primal.net/e/122a06dbab02d207b3aa793b0fedd06fd59d36178a7b9ae5971cfc3b7f3eb6ce) fügt eine Opt-in-Bild-Proxy-Liste hinzu, so dass der Medienhost eines Absenders die Adresse eines Lesers nicht lernen muss. Mitarbeiter können ein mitglied von einer profilkarte aus kicken, verbieten oder unbannen, und ein privater kanalschlüssel, der mit einer rolle gewährt wird, gilt jetzt ohne eine separate einladung. Der proxy ist standardmäßig deaktiviert; betreiber wählen und drehen ihre eigenen server.

### Ditto 2.40.0 bringt die Top-8-Liste auf Nostr-Profile

[Ditto](https://gitlab.com/soapbox-pub/ditto) ist ein sozialer Client auf Nostr. [Version 2.40.0](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.40.0) ermöglicht es einem Benutzer, acht Lieblingspersonen in seinem Profil einzustufen. Die Neubestellung bleibt lokal bis zum Speichern, dann erscheint die Rangliste im Profil und ihre Aktualisierung kann als Karte in den Feeds der Follower angezeigt werden. Das verwandelt eine Profilpräferenz in ein gemeinsames Social-Graph-Signal mit einem expliziten Veröffentlichungsschritt.

### XM Arcade 1.1.3 bindet die Freigabe einer Mini-App an einen einzigen Lauf

[XM Arcade](https://gitworkshop.dev/r/xm-arcade) führt kleine Spiele und Mini-Apps in einem Nostr-Gruppenkontext aus. [Version 1.1.3](https://primal.net/e/dec0edda9ff464b4b7598032318cb48e17cf496e29d05031d1f1629409039a4c) bindet eine Post-Genehmigung an ein opakes Run-Token, die Anforderung, die App, das Konto, die Gruppe und den Kanal. Abgelaufene oder wiederholte Genehmigungen autorisieren keinen weiteren Mini-App-Lauf mehr. Das Update besteht auch während des Neustarts auf dem Status der vertrauenswürdigen Gruppenschlüssel.

### Zzub 0.0.15–0.0.16 erweitert mobile Projektboards

[Zzub](https://primal.net/e/70c5efeea2e9314329b8951346d83ad0688b74607a108e8bc820caae545196c2) ist ein Nostr-basierter Projekt- und Code-Review-Client. Die Version 0.0.15 fügt Statusspalten hinzu, Sortieren und Filtern, Thread-Kommentare, benannte Beauftragte und Genehmigung oder Anforderung von Änderungen an den Telefonkarten. Ein integrierter Git-Client öffnet Quell- und dateiengeänderte Diffs von einer Pull-Request-Karte und bringt den vorhandenen Desktop-Review-Flow auf das Telefon.

[Version 0.0.16](https://primal.net/e/d9ad994bfadc1152b4c77a4fd3eb6be1746eca9d2626008d341bf31d06988872) stellt die vollständige angekündigte Projektliste wieder her, nachdem das vorherige gerätelokale Scoping sie versteckt hatte. Die Version fügt einen @mention-Selektor zu Kartenkommentaren hinzu, zeigt Erwähnungen als Chips an und gibt dem Projektbildschirm Aufgaben und Bewertungen Registerkarten, die alle Repositorys umfassen, während die einzelnen Repository-Boards verfügbar bleiben. Es fügt auch Repository- und Statusfilter hinzu und hebt das Kommentarfeld über der Android-Navigation auf.

### Table Mesh 0.1.0 entdeckt Brettspiele über Nostr und spielt sie offline

[Table Mesh 0.1.0](https://primal.net/e/c5c5ad0eba413e18c10e3cd2be607e550ac818a8abaf97ccbf8fa242fbaff15f) ist eine erste Android-Version für das Spielen von Brettspielen über nahe gelegene Telefone über Bluetooth und lokales WLAN. Dazu gehören *Mensch ärgere Dich nicht* und Solobots. Ein Nostr Typ-7529-Katalog verteilt zusätzliche Sandbox-Spielmodule über Blossom, wobei die heruntergeladenen Bytes mit den angekündigten Hashes verglichen werden.

Der [App-Eintrag](https://zapstore.dev/apps/org.tablemesh.app) beschreibt das Bluetooth-Mesh, wie es in Simulationen und Emulatoren getestet wurde, noch nicht an echten Multi-Phone-Tischen. Die Tischsitzung selbst läuft lokal ohne Internetverbindung oder Konto; Nostr trägt seine Züge nicht.

## In Entwicklung

### 0xchat behebt Signatur-, Nachrichtenauthentifizierungs- und Weiterleitungslücken {#0xchat-merges-fixes-for-signing-message-authentication-and-redirect-flaws}

[0xchat's fusioned security PR](https://github.com/0xchat-app/0xchat-app-main/pull/92) befasst sich mit vier Prüfungsergebnissen im Nostr- und Cashu-Anwendungscode. Es beschränkt Cashu P2PK-Zeugensignierung auf Schlüssel, die tatsächlich durch ein Schloss autorisiert sind, lehnt unversiegelte Geschenk-Wrap-Inhalte ab, außer MLS Welcome-Ereignisse, akzeptiert die Infrastruktur-Host-Map-Konfiguration nur über den vertrauenswürdigen Serverschlüssel und erfordert die Zustimmung, bevor eine eingebettete Webseite NIP-07-Signierung aufrufen oder Relaiseinstellungen lesen kann.

Das [PR-Prüfprotokoll](https://github.com/0xchat-app/0xchat-app-main/pull/92) Berichte über statische Analysen und Laufzeitüberprüfungen für den Gift-Wrap-Pfad. Dies ist ein Fortschritt auf Quellebene, nicht eine Behauptung, dass eine aktualisierte App auf einem Gerät veröffentlicht oder unabhängig getestet wurde.

### nos2x-fox schließt einen Weg zur Offenlegung der PIN {#nos2x-fox-closes-a-pin-exposure-path}

[nos2x-fox](https://github.com/diegogurpegui/nos2x-fox) ist eine Firefox-Erweiterung, die Nostr-Signierung für Websites bietet. A [Mergered Access-Control Fix](https://github.com/diegogurpegui/nos2x-fox/pull/69) verhindert, dass eine Website den Erweiterungshintergrund für die zwischengespeicherte PIN anfordert, die ihren privaten Schlüssel-Verschlüsselungsschlüssel ableitet. Die Seitenbrücke leitet nun nur noch zulässige Anforderungstypen weiter, und der Hintergrund lehnt privilegierte Anfragen ab, es sei denn, sie stammen von einer Erweiterungsseite.

A getrennt [fusionierte Einspritzänderung](https://github.com/diegogurpegui/nos2x-fox/pull/67) macht das NIP-07 `window.nostr` Die Benutzeroberfläche erscheint beim Dokumentenstart und entfernt eine webzugängliche Skript-URL, die eine stabile Erweiterungskennung enthält. Es erhöht das Firefox-Minimum auf Version 128. Beide Fixes sind Quellarbeit zusammengeführt; ein neues Extension-Store-Release wurde nicht verifiziert.

### nostream veröffentlicht Ereignisse zum Zustand von Relays {#nostream-publishes-relay-health-events}

[nostream](https://github.com/cameri/nostream) ist eine Nostr-Relay-Implementierung, die auch einen Relaismonitor ausführt. Seine [zusammengeführte NIP-66-Arbeit](https://github.com/cameri/nostream/pull/741) veröffentlicht signierte Relais-Entdeckungs- und Monitor-Ankündigungsereignisse nach einer Sonde und gibt anderen Clients die Möglichkeit, die Messungen des Monitors über Nostr zu finden. [NIP-66](/de/topics/nip-66/) definiert Relais-Entdeckung und Monitorereignisse, so dass der Relaisstatus in einem gemeinsamen Format geteilt werden kann.

Das Relais auch [Zusammenführung einer Opt-in-Trust-Distanz-Regel für adaptiven Proof of Work](https://github.com/cameri/nostream/pull/779): Ein Operator kann die Schwierigkeit beim Posten von Schlüsseln in der Nähe seines Web-of-Trust-Graphen verringern, während unbekannte Schlüssel die volle Anforderung beibehalten. Ein Schwellenwert ist standardmäßig nicht konfiguriert, so dass bestehende Relais ihr vorheriges Aufnahmeverhalten beibehalten.

### nostter bindet Remote-Signierung an die aktive Sitzung

[Nostter](https://github.com/SnowCait/nostter) ist ein Web-Nostr-Client zum Lesen und Veröffentlichen über Relais. Seine [NIP-46-Verbindung Lebenszyklus](https://github.com/SnowCait/nostter/pull/2518) gehört nun zum Unterzeichner der authentifizierten Sitzung, so dass ein fehlgeschlagenes Anmelden oder Zurücksetzen der Sitzung die Remoteverbindung entsorgen kann, anstatt einen globalen Modul-Signer zurückzulassen. [NIP-46](/de/topics/nip-46/) lässt einen Client einen separaten Unterzeichner bitten, kryptographische Operationen über Nostr zu genehmigen.

Der Kunde auch [akzeptiert Bilder aus dem Freigabemenü des Betriebssystems](https://github.com/SnowCait/nostter/pull/2510)und übergibt sie an ihren normalen Komponisten und Upload-Pfad. Das macht es möglich, ein Foto in einem Nostr-Post zu teilen, ohne es zuerst im Client zu speichern und auszuwählen.

### Zap Cooking veröffentlicht Bildbeschreibungen und blockiert Suchen nach geheimen Schlüsseln {#zap-cooking-publishes-image-descriptions-and-blocks-secret-key-searches}

[Zap Cooking](https://github.com/zapcooking/frontend) ist ein Nostr Rezept und Long-Form-Publishing-Website. Seine [NIP-92 Bildbeschreibungsarbeiten](https://github.com/zapcooking/frontend/pull/746) lässt Autoren alternativen Text für Bilder in Notizen, Antworten, Rezepten, Artikeln und Produkten schreiben und trägt diesen Text dann in `imeta` Tags, die andere Clients rendern können. [NIP-92](/de/topics/nip-92/) standardisiert Medienmetadaten, die an Nostr-Ereignisse angehängt sind, einschließlich Bildbeschreibungen.

Die Website [Suchkorrektur](https://github.com/zapcooking/frontend/pull/744) öffnet jetzt pasted `nostr:` Identifikatoren direkt und lehnt geheime Schlüsseleingaben ab, bevor sie zu einer Relaissuche werden. Das ist wichtig, weil NIP-50 Suchbegriffe an Relais sendet; versehentlich einfügen eines `nsec` in das alte Suchfeld könnte den privaten Schlüssel zu diesen Relais offenlegen. [NIP-50](/de/topics/nip-50/) definiert relayseitige Suchfilter für Nostr-Inhalte.

### Divine Mobile verbindet inaktive Relay-Abonnements erneut

[Divine Mobile](https://github.com/divinevideo/divine-mobile) ist ein Kurzvideo-Client, der Nostr-Events veröffentlicht und liest. Ein [zusammengeführter Relais-Fix](https://github.com/divinevideo/divine-mobile/pull/9246) verbindet sich nach einem Leerlauf-Timeout oder einer Fernschließung wieder, einschließlich Abonnements, die nur Daten empfangen und niemals eine weitere Anforderung zur Auslösung der Wiederherstellung senden. Dadurch wird ein Pfad wiederhergestellt, der von Direct-Message-Posteingängen und Moderationsetiketten verwendet wird, nachdem eine Verbindung abfällt.

Ein separater [profile-verification fix](https://github.com/divinevideo/divine-mobile/pull/9293) wartet auf alle abgefragten Relais, bevor er zu dem Schluss kommt, dass ein Profil keine verknüpften Konten hat. Die vorherige leere Antwort könnte ein gültiges Identitätsereignis vor einem langsameren Relais verbergen, so dass Benutzer gültige Identitätsereignisse aus langsameren Relais in einer ersten Profilansicht sehen.

### Conduit lädt Produktbilder über Blossom hoch {#conduit-uploads-product-images-through-blossom}

[Leitung](https://github.com/Conduit-BTC/conduit-mono) ist ein Nostr-basierter Marktplatz mit Merchant Publishing Tools. Seine [Zusammengeführte Bild-Upload-Arbeit](https://github.com/Conduit-BTC/conduit-mono/pull/503) Händler können Produktbilder vom Desktop oder Mobilgerät über einen konfigurierten Blossom-Server hinzufügen, während die Produktpublikation separat signiert bleibt. Blossom ist ein Media-Storage-Protokoll, das Nostr-Identitäten verwendet, um Uploads zu autorisieren und Anwendungen Dateien abrufen zu lassen.

Der [Upload-Pfad](https://github.com/Conduit-BTC/conduit-mono/pull/503) autorisiert nur den vorbereiteten Bild-Hash und den ausgewählten Server mit einem kurzlebigen signierten Ereignis und überprüft dann das zurückgegebene Ergebnis. Das gibt einem Händler einen In-App-Media-Workflow, ohne die signierte Servereinstellung stillschweigend zu ändern, die bestimmt, wohin Bilder gehen.

### Buzz ergänzt authentifizierte Moderationsfunktionen für Relays

[Buzz](https://github.com/block/buzz) enthält ein Nostr-Relay und Community-Administrations-Tools. Seine [Zusammengeführte Relais-Admin-Routen](https://github.com/block/buzz/pull/7302) Erlauben Sie autorisierten Betreibern, aktive Sperren und Timeouts aufzulisten und sie durch eine signierte HTTP-Anfrage zu heben. [NIP-98](/de/topics/nip-98/) Definiert Nostr-Ereignis-Autorisierung für HTTP-Aufrufe, so dass das Relay überprüfen kann, wer die administrative Anforderung gestellt hat.

Die [Operationen zum Aufheben von Sperren und Timeouts](https://github.com/block/buzz/pull/7302) Schreiben ihres audit-protokolls in die gleiche datenbanktransaktion wie die einschränkungsänderung. Betreiber können daher eine live-moderationsentscheidung überprüfen und rückgängig machen, ohne dass eine erfolgreiche umkehrung ihren audit-trail verliert.

### ContextVM SDK verkürzt Wartezeiten beim Veröffentlichen und repariert Streams

[ContextVM SDK](https://github.com/ContextVM/sdk) ist ein TypeScript-Toolkit für Anwendungen, die signierte Anfragen und Streams über Nostr-Relays austauschen. Sein [Relaypool-Wechsel](https://github.com/ContextVM/sdk/pull/100) sendet ein Ereignis an jedes angeschlossene Relais, beendet aber standardmäßig die Wartezeit des Anrufers nach der ersten positiven Bestätigung; Anwendungen, die alle Bestätigungen benötigen, können diesen Modus weiterhin anfordern. Ein langsames Relais bestimmt nicht mehr das normale Veröffentlichen warten.

Das SDK auch [Absenderstromsequenzierung](https://github.com/ContextVM/sdk/pull/95) Client-Start-Streams verwenden also keine Sequenznummer mehr für einen Accept- und einen Control-Frame. Die PR stellt fest, dass der werkzeugseitige Verbrauch dieser gestreamten Teile unverdrahtet bleibt, so dass dies ein Transport-Meilenstein ist und keine Behauptung, dass jeder Streaming-Anwendungspfad vollständig ist.

### Mostro bewahrt den ursprünglichen Erstellungszeitpunkt einer Order

[Mostro](https://github.com/MostroP2P/mostro) ist ein Peer-to-Peer-Bitcoin-Austauschkoordinator, der Bestellungen über Nostr veröffentlicht. Seine [zusammengeführte Art `38383`-Änderung](https://github.com/MostroP2P/mostro/pull/971) fügt ein stabiles `created at`-Tag aus dem Auftragsdatensatz hinzu, das es den Kunden ermöglicht, eine Bestellung nach dem Zeitpunkt ihrer Eröffnung zu sortieren oder zu altern, anstatt nach ihrer letzten Statusrevision. [NIP-69](/de/topics/nip-69/) definiert das Nostr-Order-Format, das von interoperablen Handelskunden verwendet wird.

Dies ist das Gegenstück zur Umsetzung des [Vorgeschlagene NIP-69 Klarstellung](https://github.com/nostr-protocol/nips/pull/2476) unten. Ältere Kunden können das additive Tag ignorieren, während Kunden, die es lesen, vermeiden können, dass eine zurückgegebene oder reparierte Bestellung neu erstellt wird.

### Amethyst implementiert DECK-0003-Objekte und die Suche nach verschlüsselten Bags

[Amethysts DECK-0003-Arbeit](https://github.com/vitorpamplona/amethyst/pull/4186) liest und rendert Simple Nostr Objects, ein JSON 3D-Mesh-Format, das in Nostr-Ereignissen übertragen wird. Unterstützt die Art `11333` Avatare, Art `3330` Shards und Opening verschlüsselte Art `33330` Region Beutel von einem Ort Hinweis. CLI-Befehle analysieren und verifizieren Objekte oder berechnen die begrenzte Suche, die zum Öffnen einer Tasche erforderlich ist. Die PR berichtet 15 übergebene Konformitätsabschnitte gegen Referenzimplementierungen.

Die [Implementierung der Bag-Suche](https://github.com/vitorpamplona/amethyst/pull/4186) ist immer noch ein Entwicklungsmeilenstein, keine geräteverifizierte Version. Seine Karte kompiliert und seine State Machine hat Unit-Tests, aber es wurde nicht auf einem Telefon ausgeübt; die erreichbaren echten Taschen, die vom Maintainer überprüft wurden, fehlen der Hinweis, der benötigt wird, um eine Suchtaste anzubieten. Eine synthetische Tasche wird benötigt, um diesen Benutzerpfad auszuüben.

### Amethyst erweitert die MLS-Interoperabilität und repariert die Desktop-Anzeige von Gruppen

[Amethyst's Quartz library](https://github.com/vitorpamplona/amethyst/pull/4187) ermöglicht es Anrufern nun, eine MLS-Gruppen-ID auszuwählen und Marmot-only-Funktionen bei der Interaktion mit anderen MLS-Stacks wegzulassen. Getrennte zusammengeführte Änderungen ermöglichen [Verlängerungen, die von jedem Gruppenmitglied unterstützt werden](https://github.com/vitorpamplona/amethyst/pull/4182), [authentifizierte Anwendungsnachrichtendaten](https://github.com/vitorpamplona/amethyst/pull/4184) und legen eine optionale [Schlüsselpaketlebensdauer](https://github.com/vitorpamplona/amethyst/pull/4188) fest. Die Marmot-Standards bleiben unverändert; Dies sind Shared-Library-Fähigkeiten, keine Behauptung, dass jede Client-Benutzeroberfläche sie aussetzt.

Ein späterer [Desktop-Render-Fix](https://github.com/vitorpamplona/amethyst/pull/4189) verwendet gemeinsame Dialoge und verhindert leere Gruppennachrichten nach der Aufteilung der Anzeigeebene. Diese zusammengeführten PRs sind Entwicklungsfortschritt, keine getaggte Amethyst-Veröffentlichung.

### nostter prüft tatsächliche Berechtigungen vor Signaturen und privaten Lesezugriffen

Bei Fortsetzung der sitzungseigenen NIP-46-Arbeit prüft [nostter's merged signer migration](https://github.com/SnowCait/nostter/pull/2570) nach einem tatsächlichen Unterzeichner, bevor Schreibaktionen angeboten werden, anstatt jede angemeldete Sitzung als beschreibbar zu behandeln. [Private Bookmarks](https://github.com/SnowCait/nostter/pull/2574) erfordern jetzt die Entschlüsselungsfunktion NIP-04 oder NIP-44, und [Remote-Signer-Einstellungen](https://github.com/SnowCait/nostter/pull/2576) erfordern NIP-44-Unterstützung. Ein schreibgeschütztes oder anonymes Konto kann immer noch nicht schriftliche Profilaktionen verwenden.

Die [Änderung der npub-Anzeige](https://github.com/SnowCait/nostter/pull/2577) und nachfolgende Authentifizierungsstatus-Refaktors setzen die gleiche Migration fort. Dies sind zusammengeführte Anwendungsänderungen, aber es wird hier kein neues Tagged-Release beansprucht.

### Pensieve gleicht Archive begrenzt und dauerhaft ab

[Pensieve's Archivquittungsarbeit](https://github.com/andotherstuff/pensieve/pull/48) wartet auf tatsächliche dauerhafte Ereignismarker, bevor er einen Abgleichversuch für abgeschlossen erklärt, wobei ungelöste IDs während der gesamten Wiederherstellung beibehalten werden. Die [Siegeländerung](https://github.com/andotherstuff/pensieve/pull/49) trennt die periodische Archivhaltbarkeit von der optionalen Veröffentlichung des Parketts, und das [gebundene Inventar](https://github.com/andotherstuff/pensieve/pull/50) scannt versiegelte Segmente mit expliziten Grenzen und einem persistenten Cursor.

Diese sind [Zusammengeführte Bibliothekszuschläge](https://github.com/andotherstuff/pensieve/pull/50), kein aktivierter Relaisreparaturarbeiter: Laufzeitplanung, Peer-Authentifizierung, Bereitstellung und Produktion Kanarienvogel bleiben getrennte Tore.

### MDK vermeidet wiederholte Verarbeitung geparkter verschlüsselter Nachrichten

[MDK's merged replay fix](https://github.com/marmot-protocol/mdk/pull/2007) befasst sich mit Arbeiten, die nach einer Veröffentlichungsbestätigung, einem Veröffentlichungsfehler oder einem Gruppenbeitritt wiederholt wurden, wenn Nachrichten geparkt bleiben, weil sie noch nicht entschlüsselt werden können. Der vorherige Pfad klassifizierte die Linie jeder Zeile erneut und rollte den Gruppenzustand für jede Zeile zurück und behielt den Anker. Der neue aufgeschobene Sweep-Ingest-Pfad überspringt die redundante Klassifizierung und teilt einen gruppenscoped Cache historischer Kontexte, was ihn ungültig macht, wenn sich der kanonische Zustand ändert.

Die [PR-Regressionstests](https://github.com/marmot-protocol/mdk/pull/2007) Vergleichen Sie die einreihigen und achtreihigen geparkten Nachrichtenfälle. Seine Engine-Suite meldet 681 bestandene Tests und fünf übersprungen. Dies ist die zusammengeführte Bibliotheksarbeit nach MDK 0.10.4, nicht Teil dieser markierten Version oder eines gemessenen Latenzanspruchs für Endbenutzer.

## Arbeit an Protokollen und Spezifikationen

### NIP-02 präzisiert Spitznamen in Follow-Listen

[NIP-02 (Follow List)](/de/topics/nip-02/) standardisiert die Art `3` Ereignis, das aufzeichnet, wem ein Konto folgt, und jedem gefolgten Schlüssel einen lokalen Petname anhängen kann. Die [Die zusammengeführte Präzisierung zum Entfernen von Spitznamen](https://github.com/nostr-protocol/nips/pull/2472) ermöglicht anzeigesichere Zeichen, während das Feld als lokales Label eines Benutzers und nicht als global verifizierter Name erhalten bleibt.

### NIP-86 ergänzt Methoden zum Leeren und Auflisten in der Relay-Verwaltung

[NIP-86 (Relay Management API)](/de/topics/nip-86/) standardisiert authentifizierte administrative Aufrufe zum Verbot, Erlauben, Prüfen und Konfigurieren eines Relais. [PR #2477](https://github.com/nostr-protocol/nips/pull/2477), zusammengeführt am 23. September, fügt Methoden hinzu, um Pubkeys oder Ereignisse sowohl aus den Erlaubnis- als auch aus den Verbotslisten zu löschen und Rollen, erlaubte Ereignisse und unzulässige Arten aufzulisten, einschließlich des Verhaltens, das bereits im Khatru-Relay-Framework und in der Go-Nostr-Bibliothek vorhanden ist.

### NIP-69 schlägt einen festen Erstellungszeitpunkt für Handelsorders vor

[NIP-69 (Peer-to-Peer Trading)](/de/topics/nip-69/) standardisiert adressierbare Orderereignisse, die es mehreren Handelsanwendungen ermöglichen, Liquidität zu kaufen und zu verkaufen. [PR #2476](https://github.com/nostr-protocol/nips/pull/2476) schlägt ein optionales Creation-Time-Tag vor, das über alle Statusaktualisierungen hinweg unverändert bleibt, so dass eine zurückgegebene oder wiederveröffentlichte Bestellung ihr ursprüngliches Alter behält, selbst wenn ein neueres Ereignis eine Statusänderung aufzeichnet.

### NIP-A3 schlägt einen Besitznachweis für Zahlungsadressen vor

[NIP-A3 (Zahlungsziele)](/de/topics/nip-a3/) ermöglicht es einem Konto, tragbare Zahlungsadressen für mehrere Netzwerke in einem austauschbaren Ereignis zu veröffentlichen. [PR #2475](https://github.com/nostr-protocol/nips/pull/2475) schlägt eine optionale Signatur durch den eigenen Schlüssel der Zahlungsadresse vor, die kompatiblen Adresstypen einen Beweis gibt, der das Ziel an den Nostr-Autor bindet, während fehlende Beweise als neutral behandelt werden.

### BUD-16 schlägt deterministische Verzeichnis-Manifeste vor

[BUD-16](https://github.com/hzrd149/blossom/pull/105) ist ein offener Blossom-Vorschlag zur Gruppierung von inhaltsadressierten Blobs in benannte Verzeichnisbäume mit reproduzierbaren manifesten Hashes. Der Entwurf definiert deterministische MessagePack-Codierung, benannte Links, Metadaten, optionale Verschlüsselungsschlüssel und `.bdir` Pfadauflösung, während Server gewöhnliche Blobs speichern.

### Marmot ergänzt verschlüsselte Gruppenumfragen

[Marmot Protocol](/de/topics/marmot/) definiert interoperable Anwendungsereignisse innerhalb von MLS-verschlüsselten Gruppen, die über Nostr übertragen werden. NIP-88 definiert Umfragefragen und signierte Antwortereignisse. [Die zusammengeführte MIP-Änderung](https://github.com/marmot-protocol/marmot/pull/425) erkennt diese Umfragen innerhalb einer Gruppe, während die Relaisauswahl an authentifiziertes Gruppen-Routing gebunden bleibt und ausdrücklich angibt, dass sie nicht anonym oder wahlfähig sind.

### Marmot übernimmt Gruppenmeldungen und Löschungen durch Administratoren

[Marmot group moderation](https://github.com/marmot-protocol/marmot/pull/423) definiert verschlüsselte Berichts-, Entlassungs- und Administrator-Löschungsereignisse, die unter dem authentifizierten Status der Gruppe zusammenlaufen. Der in der vergangenen Woche behandelte Vorschlag wurde nun zusammengeführt und legt einen Statusübergang fest, mit dem die Implementierungen die Überprüfung von Berichten und die Entfernung von Nachrichten mit der akzeptierten Spezifikation in Einklang bringen können.

### NWC-13 schlägt Abfragen zum Verbindungsbudget vor

[Nostr Wallet Connect](/de/topics/nip-47/) ermöglicht eine Anwendungsanforderung engmaschige Wallet-Operationen durch verschlüsselte Nostr-Ereignisse. [NWC-13](https://github.com/nostr-wallet-connect/nwc/pull/7) schlägt eine gesonderte `get_budget` Berechtigung und Antwort, damit eine Anwendung die verwendete, die Gesamt- und die Verlängerungszulage überprüfen kann, ohne die Erlaubnis zum Lesen des Guthabens der Brieftasche zu erhalten.

## NIP im Detail: eigene Emojis und Videoereignisse

### NIP-30: Eigene Emojis {#nip-30-custom-emoji}

[NIP-30 (eigene Emojis)](/de/topics/nip-30/) standardisiert, wie ein signiertes Ereignis lesbare `:shortcodes:` Bild-URLs zuordnet. Optional verweist eine Adresse auf ein wiederverwendbares Emoji-Set. Die [Spezifikation](https://github.com/nostr-protocol/nips/blob/master/30.md) erlaubt Buchstaben, Ziffern, Bindestriche und Unterstriche (`_`) im Shortcode. Die Zuordnung gilt für Profile, kurze Textnotizen, Kommentare, Reaktionen und Live-Aktivitäten. NIP-51 definiert öffentliche und private Listenformate, darunter parametrisierte, ersetzbare Ereignisse vom Kind `30030`, die benannte Emoji-Sets enthalten.

Clients sollten den wörtlichen Shortcode beibehalten, wenn das Bild nicht geladen werden kann, ungültige Zuordnungen ablehnen und jeden Bildhost als externen Netzwerkzugriff behandeln: Er kann Adresse und Zugriffszeitpunkt des Betrachters beobachten. [Die Android-Implementierung in Amethyst](https://github.com/vitorpamplona/amethyst/blob/96bec0cc7c1df4c05d4208fb1cfd6aac06fe97e7/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip30CustomEmoji/EmojiUrlTag.kt) verarbeitet die optionale Set-Adresse und erzwingt die zulässigen Shortcode-Zeichen. [Die Implementierung im mobilen Wisp-Client](https://github.com/barrydeen/wisp/blob/b48be58271131c6062be2cc5449777cdd4fe6d31/app/src/main/kotlin/com/wisp/app/nostr/Nip30.kt) erstellt Emoji-Sets und entfernt doppelte Shortcodes aus gerenderten Inhalten. [Die Implementierung im Web-Client Nostria](https://github.com/nostria-app/nostria/blob/e861946f4ef4e70f3ec49997a4be27615b9b6f5e/src/app/utils/emoji-shortcode.ts) normalisiert Trennzeichen vor der Prüfung von Shortcodes. Das zeigt, weshalb Herausgeber ihre Tags mit gängigen Clients testen sollten, bevor sie sich auf Satzzeichen verlassen, die laut Spezifikation zulässig sind.

[NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) definiert die kanonische Serialisierung, Ereignis-ID und Signaturregeln zur Authentifizierung von Nostr-Ereignissen. Das folgende Emoji-Set-Ereignis vom Kind `30030` wurde bei der Überprüfung von `wss://nos.lol` und `wss://relay.primal.net` abgerufen. Es bestand sowohl die Prüfung der Ereignis-ID als auch die BIP-340-Signaturprüfung. Sein `d`-Tag liefert die Kennung des ersetzbaren Sets; das `emoji`-Tag ordnet `:liberlandflag:` dem gehosteten Bild zu.

```json
{"kind":30030,"id":"438814476db249b50067d167e50c85530e317126179546a584365c8371bdd97f","pubkey":"6e1897660c62153be7355a82a62549b09993fb12b50de73a32610725d1a5de6b","created_at":1790025651,"tags":[["d","1962f3e8-5a74-4327-b88d-4697bdd2119d"],["client","Amethyst"],["emoji","liberlandflag","https://nogues.ca/emoji/liberlandflag.png"],["title","Liberland"],["description","#Liberland"],["image","https://npub1dcvfwesvvg2nhee4t2p2vf2fkzve87cjk5x7ww3jvyrjt5d9me4szmscg7.blossom.band/a8aa38949d3d7a17e369703391de0406f50b518a1a6ca9791ebf38c94b51a0e1.jpg"]],"content":"","sig":"5f7dd5b8879311689e95cbab26edd6f65611d517d22d12d568a9de219c8a8fc6999365c83205d02ec74844b4b9944ed5419ec17ea9d8cbf4e347504cc3685304"}
```

[Alex Gleason führte NIP-30 im April 2023 ein](https://github.com/nostr-protocol/nips/commit/e91ce3409e1ce8267fc07a21784d2538621267c3). Der ursprüngliche Vorschlag, über den wir bereits in der Ausgabe vom 29. April berichteten, ist mittlerweile in aktuellen Clients umgesetzt. Zu den späteren Änderungen gehört ein [Update vom August 2026](https://github.com/nostr-protocol/nips/commit/735a25e44b8e7a01539864f2a2dcf3e728977fd3), das Kommentare vom Kind `1111` zu den unterstützten Ereignisarten hinzufügte. Die Bedeutung eines Emojis bleibt auf das jeweilige signierte Ereignis oder referenzierte Set begrenzt; Clients brauchen deshalb kein globales Shortcode-Verzeichnis.

### NIP-71: Videoereignisse {#nip-71-video-events}

[NIP-71 (Videoereignisse)](/de/topics/nip-71/) standardisiert Nostr-Ereignisse für Videos im Querformat und Kurzvideos, samt Wiedergabemetadaten, alternativen Dateien, Untertiteln, Kapiteln, Mitwirkenden und Angaben zur importierten Quelle. Die [maßgebliche Spezifikation](https://github.com/nostr-protocol/nips/blob/master/71.md) weist den unveränderlichen Beiträgen im Quer- und Hochformat die Kinds `21` und `22` zu. Die Kinds `34235` und `34236` verwenden dagegen ein `d`-Tag für adressierbare Videos, deren Metadaten unter einer festen Kennung aktualisiert werden können. Jedes `imeta`-Tag beschreibt eine abspielbare Variante mit URL und Medientyp sowie optionalen Angaben zu Abmessungen, Hash, Vorschaubild, Ausweichdatei, Dienst, Bitrate und Dauer.

Clients müssen Medien-URLs und Hashes prüfen, Downloads begrenzen, fehlende Varianten abfangen und Zugriffe auf externe Hosts für Nutzer sichtbar machen: Ein Videoserver kann den Wiedergabeverkehr beobachten. [Die Android-Implementierung in Amethyst](https://github.com/vitorpamplona/amethyst/blob/96bec0cc7c1df4c05d4208fb1cfd6aac06fe97e7/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip71Video/VideoEvent.kt) trennt Video- und Audiospuren und wählt eine abspielbare Variante. [Der mobile Wisp-Client](https://github.com/barrydeen/wisp/blob/b48be58271131c6062be2cc5449777cdd4fe6d31/app/src/main/kotlin/com/wisp/app/nostr/Nip71.kt) liest und erstellt gewöhnliche Videoereignisse mit strukturierten `imeta`-Feldern. [Die Browser-Erweiterung Resonote](https://github.com/ikuradon/Resonote/blob/4ac14e1206608315d6507da405d4c5df3312d4d0/packages/core/src/nip71-video.ts) erstellt und liest alle vier Ereignisarten sowie Medienvarianten, Textspuren, Segmente, Mitwirkende und Herkunftsmetadaten.

Das folgende Kurzvideoereignis vom Kind `22` wurde bei der Überprüfung von `wss://relay.damus.io` und `wss://nos.lol` abgerufen. Es bestand die Prüfung der [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)-Ereignis-ID und der BIP-340-Signatur. Das `imeta`-Tag verknüpft die MP4-URL mit MIME-Typ, SHA-256-Hash, Abmessungen und Dauer. Die übrigen Tags liefern Titel, Veröffentlichungszeitpunkt, Alternativtext für Barrierefreiheit und durchsuchbare Themen.

```json
{"kind":22,"id":"dd1fcfe7ce6db5450e362879897138ca4e639ef39654dfe3b1f669310fd9545d","pubkey":"870ce6f7aa9ee05025667245343278eccfb8e3eafc08bcab68824ad0f4cfa675","created_at":1790094714,"tags":[["title","Why Pepe moves 3x Bitcoin"],["published_at","1790094714"],["alt","Why Pepe moves 3x Bitcoin"],["imeta","url https://the-bitcoin-strategy.com/nostr-relay/pKy3my2zzMhCVNL1.mp4","m video/mp4","x 3dafddd0b1730213212bcaf96136684f15e20ee5f20a1252052a58f3a8b36652","dim 1080x1920","duration 62"],["duration","62"],["t","bitcoin"],["t","pepe"],["t","memecoin"],["t","altcoin"]],"content":"Why Pepe moves 3x Bitcoin\n\nPepe jumped about twenty percent in a single day, roughly triple Bitcoin's move. Most of the trading is not the token itself: on Binance, the volume in bets on the price was about eight times the volume in the actual token. Those bets are made with borrowed money, so every dollar tends to move the price more, in both directions.\n\nAsk Gerhard AI For Free:\nhttps://mybtcguy.com\n\n#bitcoin #pepe #memecoin #altcoin","sig":"0da305b00f4b1631b14b8fd33fcc6a2a0e54e24233dba541db3d2bce3705ac0dcf61401764b47555015e2566dcf4a8886cd3f767ea26ed2da76b3ac9bb23d680"}
```

[Die Dateigeschichte von NIP-71 begann im Dezember 2023](https://github.com/nostr-protocol/nips/commit/7afd1049d98a82aa7754f80de80d97dd686cf40e): zmeyer44 verschob den Vorschlag für Videoereignisse zu seiner heutigen Nummer. Das [Update für adressierbare Videos](https://github.com/nostr-protocol/nips/pull/1669), über das wir bereits in der Ausgabe vom 13. Januar berichteten, ist inzwischen in mehreren aktuellen Implementierungen angekommen. Die Kinds `34235` und `34236` geben Herausgebern eine feste Kennung für korrigierte Metadaten und einen Wechsel des Hosting-Dienstes.

### Wie die beiden Spezifikationen zusammenhängen

Die [Spezifikation NIP-30](https://github.com/nostr-protocol/nips/blob/master/30.md) regelt Darstellungsmetadaten für eine begrenzte Anzahl sozialer Ereignisarten. [NIP-71](https://github.com/nostr-protocol/nips/blob/master/71.md) definiert dagegen medienbezogene Ereignisse und ihre Wiedergabedaten. NIP-30 führt die vier Video-Kinds von NIP-71 derzeit nicht auf. Clients sollten eigene Emojis im Umfeld von Videos daher über unterstützte Profile, Kommentare, Reaktionen oder Live-Aktivitäten anzeigen und nicht voraussetzen, dass Shortcodes innerhalb eines Videoereignisses ersetzt werden. Diese Grenze gibt Implementierern eine eindeutige Interoperabilitätsregel, während beide Spezifikationen die darstellbaren Medien einer Nostr-Oberfläche erweitern.

---

NIP-17 definiert private Direktnachrichten, bei denen Absender und Metadaten in Gift-Wrap-Ereignissen verborgen sind. Schicken Sie eine NIP-17-Direktnachricht, um ein Projekt oder eine Nachricht über das [Nostr-Compass-Projekt](https://github.com/andotherstuff/nostr-compass) einzureichen.
