---
title: 'Nostr Compass #47'
date: 2026-11-04
publishDate: 2026-11-04
draft: false
type: newsletters
translationOf: /en/newsletters/2026-11-04-newsletter.md
translationDate: 2026-11-05
---

Diese Woche hat [Amethyst](/de/newsletters/2026-11-04-newsletter/#amethyst) Inline-Napplets mit Korrekturen aus einer [Sicherheitsprüfung der Einbettung](https://github.com/vitorpamplona/amethyst/pull/4710) ausgeliefert. [Napplets](/de/newsletters/2026-11-04-newsletter/#napplets---web-packages) hat die Applet-Identität an Ports pro Dokument gebunden, und die Nightlies von [Marmots mdk](/de/newsletters/2026-11-04-newsletter/#marmot-protocol-mdk) haben das Gruppen-Messaging verschärft. Darüber hinaus gab es Änderungen bei Relays, Wallets, Signaturbibliotheken und neuen Apps, vieles davon in gemergtem Quellcode, der noch nicht ausgeliefert wurde.

## Top-Meldungen {#top-stories}

### Amethyst {#amethyst}

Amethyst, der Android-Client, hat [v1.21.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.21.0) veröffentlicht. Die Version führt Napplets unter Android 11+ und auf dem Desktop direkt in Notizen aus. Korrekturen aus einer [Sicherheitsprüfung der Einbettung](https://github.com/vitorpamplona/amethyst/pull/4710) schließen einen Weg, über den jedes Napplet mit Relay-Zugriff entschlüsselte DMs lesen konnte. Die Entschlüsselung erfordert jetzt eine separate Freigabe durch den Nutzer, und `nostr.signEvent` benötigt die Berechtigung des Signers. Der Chromium-Renderer auf dem Desktop läuft dagegen weiterhin ohne Sandbox. Eine [Änderung an der Verschlüsselung pro Datei](https://github.com/vitorpamplona/amethyst/pull/4701) gibt jedem Anhang einer privaten Direktnachricht nach [NIP-17](/de/topics/nip-17/) einen frischen AES-GCM-Schlüssel und eine frische Nonce. Bisher wurden in Stapeln mit mehreren Dateien beide wiederverwendet. Die Risikobeschreibung des Upstream-Projekts beruht auf einer Codeanalyse ohne reproduzierten Exploit, und bereits gesendete Dateien werden nicht nachträglich repariert.

### Marmot Protocol (mdk) {#marmot-protocol-mdk}

mdk, Marmots MLS-basiertes Kit für verschlüsselte Nachrichten auf Nostr, hat Nightly-Vorabversionen ausschließlich zu Testzwecken veröffentlicht. In dieser Linie gibt es kein stabiles Release. Im Nightly vom 2. November [warten neue Sendungen innerhalb einer Gruppe hinter älteren, bereits eingereihten](https://github.com/marmot-protocol/mdk/pull/2849). So bleiben die Verschlüsselungsgenerationen für Mitglieder, die den Verlauf nachholen, in der richtigen Reihenfolge. Das garantiert allerdings nicht, dass keine Nachrichten verloren gehen. Eine gemergte, standardmäßig deaktivierte [Reparatur verlorener Welcomes](https://github.com/marmot-protocol/mdk/pull/2936) folgt der [Heartbeat-Regel von Marmot](https://github.com/marmot-protocol/marmot/pull/497). Sie sendet genau das aufbewahrte Welcome erneut, sobald der Heartbeat des Ziels Aktivität zeigt, die mindestens zehn Minuten nach der letzten Carrier-Veröffentlichung liegt. Der Heartbeat-Takt oder eine nachgehende Uhr können die Reparatur um eine Stunde oder mehr verzögern, und für den Abschluss gibt es keine Obergrenze. [Befehle zur Geräteverknüpfung](https://github.com/marmot-protocol/mdk/pull/2922) bleiben hinter dem standardmäßig deaktivierten Feature dev-device-groups und sind in der Produktion abgeschaltet.

### Napplets - Webpakete {#napplets---web-packages}

Napplets, die Webpakete für Nostr-Applets in Sandboxen, hat [core 0.37.0](https://github.com/napplet/web/releases/tag/%40napplet/core%400.37.0), [nap 0.36.0](https://github.com/napplet/web/releases/tag/%40napplet/nap%400.36.0) und [shim 0.35.0](https://github.com/napplet/web/releases/tag/%40napplet/shim%400.35.0) veröffentlicht, die [die Applet-Identität an einen MessagePort pro Dokument binden](https://github.com/napplet/web/pull/302). Die verifizierte Identität (dTag, artifactHash) ist an den Port gebunden, der im Hello aus dem erzeugten iframe übergeben wird, und der gesamte NAP-Verkehr läuft über diesen Port. Ein Dokument, das per Navigation geladen wird, erhält keine Freigaben. Shells, die noch Window-Messaging verwenden, müssen aktualisieren, da es keinen Kompatibilitätspfad gibt. Späterer Quellcode [bindet den Vorschau-Frame fest an sein verifiziertes Dokument](https://github.com/napplet/web/pull/305), und zwar mit frame-src 'none'.

## Getaggte Releases {#tagged-releases}

### Marble {#marble}

Marble, ein Beta-Client auf Basis der Schwellenwertsignaturen von Cosign, kann in [0.12.23](https://github.com/sybenx/marble/releases/tag/v0.12.23) Relays als Feeds lesen. Ein über seine Adresse geöffnetes Relay zeigt zuerst seine eigene Beschreibung und dann seine Beiträge, die neuesten zuerst. Favorisierte Relays werden in einer Liste vom kind 10012 gespeichert, Relay-Gruppen in Sets vom kind 30002. Das sind dieselben Listen, die Jumble verwendet. Das Release überarbeitet außerdem die Reaktionen und bringt eine Leiste mit kürzlich verwendeten Reaktionen sowie die eigenen benutzerdefinierten Emojis des Nutzers.

### Sidecar {#sidecar}

Sidecar, eine Browsererweiterung zum Veröffentlichen von Notizen und Web-Highlights, kann in [1.16.6](https://github.com/dmnyc/sidecar/releases/tag/v1.16.6) sein Wallet-Backup von Relays löschen. Nach einer Bestätigung ersetzt es die verschlüsselte Kopie durch eine leere und bittet die Relays, sie zu vergessen. Die verbundene Wallet bleibt dabei bestehen. Es ist nicht garantiert, dass Relays das Backup tatsächlich löschen. Seit [v1.16.5](https://github.com/dmnyc/sidecar/releases/tag/v1.16.5) entfernt Sidecar vor dem Hochladen EXIF-, XMP- und IPTC-Metadaten aus JPEGs, und seine [Änderung an der Upload-Vorbereitung](https://github.com/dmnyc/sidecar/pull/572) blockiert jedes JPEG, das sich nicht bereinigen lässt.

### Haps {#haps}

Haps veröffentlicht und installiert native Pakete unter Nostr-Schlüsseln. [Haps 0.1.25](https://github.com/mmalmi/haps/releases/tag/v0.1.25) liefert Bundles für macOS, Linux und Windows mit per Prüfsumme fixierten htree-Hilfsprogrammen sowie eine SHA256SUMS-Datei, die alle Archive abdeckt. Der Quellcode für 0.1.24 [schreibt versionierte Hashtree-Referenzen](https://github.com/mmalmi/haps/commit/3dd051cefe9e506886a7f036267950282a179ee8) gemäß dem Entwurf der Hashtree-Spezifikation. Haps 0.1.23 und ältere Versionen können die neuen Kataloge nur mit einem Legacy-Übergangskatalog oder einem aktualisierten Installer bzw. Cargo-Build lesen.

### Cosign {#cosign}

Cosign, die Bibliothek für Schwellenwertsignaturen hinter der Marble-Beta, liefert in [0.12.9](https://github.com/sybenx/cosign/releases/tag/v0.12.9) eine teilweise Korrektur für den Beitritt: Ein Beitritt über eine gescannte einladende Person erfordert jetzt deren Beitrag sowie Teile von mindestens zwei verschiedenen Absendern. Beitritte von Telefon zu Telefon bleiben ungebunden, sodass einem Angreifer weiterhin zwei Schlüssel genügen. Leere Entschlüsselungsteile überspringen weiterhin die Beweisprüfung. In [0.12.8](https://github.com/sybenx/cosign/releases/tag/v0.12.8) kann ein Server, der die Mitgliederliste schreibt, weiterhin Share-Punkte mit bekannten Geheimnissen wählen. Telefone erhalten Korrekturen nur über ein Marble-Release.

### nostream {#nostream}

nostream, ein in TypeScript geschriebenes Relay mit PostgreSQL-Backend, ergänzt eine [ausgehende Peer-Synchronisierung](https://github.com/cameri/nostream/pull/1043) in [3.12.0](https://github.com/cameri/nostream/releases/tag/nostream%403.12.0). Der Worker liest für jeden Peer die Scopes aus dessen Relay-Informationen nach [NIP-11](/de/topics/nip-11/), authentifiziert sich per Client-Authentifizierung nach [NIP-42](/de/topics/nip-42/) und gleicht per Negentropy-Synchronisierung nach [NIP-77](/de/topics/nip-77/) ab. Abgerufene Events prüft er dabei anhand von ID, Signatur und Scope. [Peer-spezifische Limits](https://github.com/cameri/nostream/pull/1034) gelten erst, nachdem ein konfigurierter Peer AUTH abgeschlossen hat. Ein Release des Quellcodes beweist nicht, dass irgendein Relay es bereits einsetzt.

### diVine {#divine}

diVine, ein Client für kurze Loop-Videos, hat [stabiles Android 1.0.27](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.27) mit interaktiven öffentlichen Video-Stickern veröffentlicht. Ob die Version auch für iOS und macOS verfügbar ist, ist unbestätigt. Eine gemergte [Nachabfrage unterhalb des Fensters](https://github.com/divinevideo/divine-mobile/pull/10711) läuft erst, nachdem die anfängliche Wiederherstellung des Verlaufs abgeschlossen ist. Sie liest Gift Wraps, veraltete verschlüsselte DMs nach [NIP-04](/de/topics/nip-04/) und Löschungen in Seiten zu je 100 Nachrichten pro Relay. Dabei durchläuft sie jedes Relay unabhängig, während der bestehende Verlaufsabruf einen gemeinsamen Cursor verwendet und den älteren Verlauf eines Relays mit Ergebnisobergrenze überspringen kann. Die Abdeckung ist begrenzt, und ein vollständiger Verlauf wird nicht wiederhergestellt.

### Whistle {#whistle}

Whistle, eine mobile App zum Teilen von Standorten in Gruppen und zum Chatten, hat [2.0.1](https://github.com/sjmcnamara/whistle/releases/tag/v2.0.1) veröffentlicht, das erste öffentliche Release auf Basis von Marmot-Protokoll v2. Bestehende Gruppen lassen sich nicht übernehmen. Gruppen müssen deshalb neu erstellt werden, und alle Mitglieder müssen aktualisieren. npub-Identitäten bleiben erhalten. Beitreten per Scan ersetzt Einladungscodes und -links. Ein bekanntes Problem: Offline gesendete Chatnachrichten können verspätet oder gar nicht ankommen. Laut Release liegt das an MarmotKit. Die Standortfreigabe ist davon nicht betroffen.

## In Entwicklung {#in-development}

### Quartz {#quartz}

Quartz, eine Kotlin-Multiplatform-Bibliothek für Nostr, hat mit Release 2.14.0 die [Wiederaufnahme von Live-Abonnements nach einem Reconnect](https://github.com/vitorpamplona/quartz/pull/82) ausgeliefert. Jedes Relay setzt beim neuesten zugestellten created_at fort, das auf die Geräteuhr begrenzt ist. Gift-Wrap-Filter reichen zwei zusätzliche Tage zurück, um Rückdatierungen abzudecken. Events mit älterem Zeitstempel, die ein Relay während eines Ausfalls gespeichert hat, können weiterhin verpasst werden. Bereits gemergte, aber noch unveröffentlichte [zählungsbewusste Negentropy-Fenster](https://github.com/vitorpamplona/quartz/pull/85) vergleichen eine optionale Event-Anzahl nach [NIP-45](/de/topics/nip-45/) mit der lokalen Anzahl und behandeln die Zählungen von Relays als nicht vertrauenswürdig.

### Buzz {#buzz}

Buzz hat eine Änderung gemergt, die [Löschungen der Kinds 5 und 9005 in einer einzigen Transaktion zusammen mit dem Soft Delete des Ziels festschreibt](https://github.com/block/buzz/pull/8944). Ein Fehler kann daher keine Löschung mehr akzeptieren, während das Ziel aktiv bleibt. Bereits bestehende inkonsistente Zeilen werden nicht repariert. Das Mobilprofil von [NIP-RS](/de/topics/nip-rs/), einem Buzz-Entwurf für einen geräteübergreifenden Lesestatus, ist gemergt und [synchronisiert Lesegrenzen über Geräte hinweg](https://github.com/block/buzz/pull/8998). Auf älteren Relays ohne read_state_snapshot funktioniert der lokale Lesestatus weiterhin, die geräteübergreifende Synchronisierung bricht dort jedoch ohne Fallback ab.

### Alby Hub {#alby-hub}

Alby Hub ist ein selbstverwahrter Lightning-Node, der Nostr-Wallet-Connect-Apps nach [NIP-47](/de/topics/nip-47/) bedient. Das Projekt hat einen [Fix für Datenbankmigrationen](https://github.com/getAlby/hub/pull/2657) gemergt, durch den der ID-Zähler jeder Tabelle bei db_migrate oder einer Postgres-Migration erhalten bleibt. Zuvor konnte eine neue App die ID einer gelöschten App wiederverwenden und deren Transaktionen sowie deren isoliertes Guthaben erben. Ein getaggtes Release oder ein Deployment, das den Fix enthält, wurde nicht gefunden. Eine separate [Änderung an den Benachrichtigungen](https://github.com/getAlby/hub/pull/2677) isoliert Fehler pro App, fehlgeschlagene Benachrichtigungen werden aber weiterhin ohne erneuten Versuch verworfen.

### swift-nostr-client {#swift-nostr-client}

swift-nostr-client, eine Nostr-Bibliothek für Swift 6, hat eine Breaking Change gemergt, durch die [RemoteSigner den Connect-Handshake vor seinem ersten Befehl ausführt](https://github.com/yysskk/swift-nostr/pull/287). Die neue Einstellung connectsAutomatically steht standardmäßig auf true. Schlägt der Handshake fehl, wird der Befehl nicht gesendet. Da Secrets für Remote Signing nach [NIP-46](/de/topics/nip-46/) nur einmal verwendbar sind, müssen Apps, die eine Bunker-Sitzung mit einem gespeicherten Client-Schlüsselpaar fortsetzen, die Einstellung auf false setzen. Andernfalls legt der erste Befehl das bereits verbrauchte Secret vor. Ein Release wurde noch nicht getaggt.

## Neue Projekte {#new-projects}

### Trikey {#trikey}

Trikey ist eine Wallet im Pre-Alpha-Stadium ohne Audit, deren Smartphone-App und Guardian über verschlüsselte Nachrichten über Nostr-Relays kommunizieren. Mit [Release 0.1.10-alpha](https://njump.me/nevent1qvzqqqr4dupzqpepqn8d9d5jc8r4qf6h7kd7ldpgrpqgdaw8wjwyrxztkjltnfy4qyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpk2jxzja4q4z8avcsc7jqenpuykke49p3z3halm0xtgmn3h6r6judumrxf) geht das Projekt das Einfrieren der App beim Öffnen an. Beide Seiten speichern nun dauerhaft, auch über Neustarts hinweg, welche Wrap-IDs bereits gelesen wurden, und überspringen diese vor jeder Signaturprüfung oder Entschlüsselung. Ablaufhinweise in Anfragen und Warnmeldungen garantieren nicht, dass Relays die Daten löschen. Die Leistungsmessungen des Herausgebers wurden auf einem Laptop durchgeführt.

### Pacto {#pacto}

Pacto, eine Desktop-App für Community-Organizing, die Legacy-Marmot-Gruppen neben NIP-17-DMs betreibt, hat die unsignierte Version [v0.7.5](https://github.com/covenant-gov/pacto-app/releases/tag/v0.7.5) veröffentlicht. Damit lassen sich gesendete Nachrichten eine Minute lang bearbeiten. Die [Fixes für die DM-Zustellung](https://github.com/covenant-gov/pacto-app/pull/425) lassen Sendevorgänge sofort fehlschlagen, wenn der Pool kein vertrauenswürdiges Relay enthält, und leiten Tippindikatoren über vertrauenswürdige Relays. Offene, noch nicht gemergte Pull Requests würden [Squad-Events](https://github.com/covenant-gov/pacto-app/pull/488) und [verschlüsselte Squad-Dokumente](https://github.com/covenant-gov/pacto-app/pull/490) hinzufügen.

### Mialuna {#mialuna}

Mialuna, ein medienorientierter Nostr-Client auf Flutter-Basis, hat eine [Release-Ankündigung für Version 0.19.0](https://njump.me/nevent1qvzqqqr4dupzqeyvpafs936l8quz5nfvskjg9wf8e3sm9q52q72wxmrvc7tdap4xqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqk6ltj5kr6mtq8mkyz9rzqxkkrhq9hsjz675e05rwgltwgreddw3npkkez) veröffentlicht. Die Version sendet Löschanfragen für die eigenen Stories des Nutzers, sobald diese ablaufen. Laut dem [Changelog-Commit](https://github.com/Lwb89dev/mialuna/commit/d0a38cb92dac724e6e7bac6ec8f94a31a378e886) umfasst das Löschanfragen an Relays und das Löschen von Medien auf Blossom. Konten mit lokalem Schlüssel erledigen dies automatisch, Amber- und Bunker-Konten warten dagegen, bis der Nutzer „Delete now“ wählt. Die APK und ihr Verhalten auf Geräten wurden nicht unabhängig geprüft. Löschanfragen können nicht garantieren, dass Relays oder Server die Daten tatsächlich löschen.

### whereAreYou {#whereareyou}

whereAreYou ist eine Android-App, die den Standort innerhalb von Kreisen teilt. Kreisen tritt man per QR-Code oder Einladungslink bei. Die App verschlüsselt Koordinaten mit AES-256-GCM und sendet sie über öffentliche Relays. Ein [Commit zur Signatur durch Mitglieder](https://github.com/Dzekdrix/whereAreYou/commit/82121d0f13b4d5256b2392383e74640afde3019e) verhindert, dass Inhaber des Kreisschlüssels als ein anderes Mitglied posten. Dafür muss jedes Gerät aktualisiert werden. Zum [Base45-Identitätsbackup](https://github.com/Dzekdrix/whereAreYou/commit/82e185967dd0115b93472b3d92a4d0393c8751bc) warnt der Autor, dass jeder, der den QR-Code fotografiert, den zugehörigen achtstelligen Code offline erraten könnte, nach seiner Schätzung innerhalb weniger Dutzend Minuten GPU-Zeit. Einen Benchmark hat er nicht veröffentlicht. Die Quelle bescheinigt keine Sicherheit.

## Protokoll- und Spezifikationsarbeit {#protocol-and-spec-work}

### Buzz definiert vom Eigentümer autorisierte Routen für Agenten-Credentials {#buzz-defines-owner-authorized-agent-credential-routes}

Buzz hat einen [NIP-FA](/de/topics/nip-fa/)-[Entwurf für vom Eigentümer autorisierte Agenten-Credentials](https://github.com/block/buzz/pull/9015) gemergt. Er definiert Routen für Grant, Assertion und Widerruf für Agenten, die per Eigentümerattestierung nach [NIP-OA](/de/topics/nip-oa/) autorisiert sind. Ein Grant entsteht aus einem Token-Exchange nach RFC 8693, der die Sitzung des Eigentümers mit einem HTTP-Auth-Nachweis des Agenten nach [NIP-98](/de/topics/nip-98/) verknüpft. Ein Widerruf trennt die Verbindung des Agenten und verhindert, dass sich sein Schlüssel erneut registriert. NIP-FA ist eine Buzz-Spezifikation, die bisher nur im Quellcode gemergt wurde. Eine Aktivierung im Produktivbetrieb oder Interoperabilität wird nicht behauptet.

### Post-Quanten-Signaturen für Events erhalten exakte Validierungsregeln {#post-quantum-event-signatures-gain-exact-validation-rules}

Der seit Langem offene Vorschlag für Post-Quanten-Signaturen hat [exakte ML-DSA-44-Validierungsregeln für Nostr-Events](https://github.com/nostr-protocol/nips/commit/43104cbff30ae006e907d8ee0ec15c4949d0eef6) erhalten. Schlüssel und Signaturen haben feste Längen. Verifizierer prüfen die Signatur über die 32 rohen Bytes des Event-ID-Digests mit leerem Kontext, und ein Fallback-Algorithmus ist nicht zulässig. Für die vorgeschlagene Identität gibt es keine bech32-Kodierung nach [NIP-19](/de/topics/nip-19/). Neue Signaturen machen weder verschlüsselte Payloads nach [NIP-44](/de/topics/nip-44/) noch Gift Wraps nach [NIP-59](/de/topics/nip-59/) sicher gegen Quantenangriffe.

### Eine vorgeschlagene signierte Vorbedingung verhindert verlorene Event-Ersetzungen {#a-proposed-signed-precondition-prevents-lost-event-replacements}

Ein offener Pull Request bei Buzz [schlägt die projektlokale signierte Vorbedingung NIP-CS für ersetzbare und adressierbare Events vor](https://github.com/block/buzz/pull/8835). Es handelt sich nicht um einen offiziellen NIP. Das signierte Tag nennt die ID des aktuellen Heads oder `none`. Das Relay prüft es atomar unter einer Sperre auf die Koordinate, lehnt einen veralteten Schreibvorgang mit einem OK false oder HTTP 409 ab und speichert nichts. Schreibvorgänge ohne das Tag funktionieren wie bisher, und das Tag bietet keine Compare-and-Swap-Garantie über mehrere Relays hinweg.

## NIP-Vertiefung: NIP-31 und NIP-73 {#nip-deep-dive-nip-31-and-nip-73}

Clients stoßen oft auf Inhalte, die sie nicht nativ verstehen. [NIP-31: Dealing with Unknown Event Kinds](/de/topics/nip-31/) gibt einem unbekannten Event-Kind eine lesbare Beschriftung, und [NIP-73: External Content IDs](/de/topics/nip-73/) benennt Gegenstände außerhalb von Nostr, etwa Bücher oder Webseiten. Die beiden Konventionen sind voneinander unabhängige, bereits bestehende Spezifikationen ([NIP-31-Text](https://github.com/nostr-protocol/nips/blob/master/31.md), [NIP-73-Text](https://github.com/nostr-protocol/nips/blob/master/73.md)).

### NIP-31 ist als nicht empfohlen markiert {#nip-31-is-marked-unrecommended}

Der aktuelle [NIP-31-Text](https://github.com/nostr-protocol/nips/blob/master/31.md) beginnt mit einer Warnung, die ihn als „unnecessarily bloated“ bezeichnet und als `unrecommended` kennzeichnet, und seine Statuszeile lautet draft, unrecommended und optional. Events, die diese Konvention nutzen, existieren bereits auf Relays. Die folgende Mechanik beschreibt daher, wie Clients sie lesen, und ist keine Empfehlung für neue Protokolle.

### Was ein alt-Tag enthält {#what-an-alt-tag-carries}

Gemäß der [Spezifikation](https://github.com/nostr-protocol/nips/blob/master/31.md) fügt der Autor eines eigenen Kinds, das nicht als Text gelesen werden soll, ein `alt`-Tag mit einer kurzen Klartext-Zusammenfassung hinzu. Von Clients, die auf Kind 1 ausgerichtet sind, wird nicht erwartet, dass sie andere Kinds abfragen, doch Nutzer können solche Events trotzdem aus Notizen heraus referenzieren, wo eine Zusammenfassung Kontext liefert. Eine Beschriftung kann keine Stimme abgeben und keine Wallet-Anfrage ausführen. Für eine reichhaltigere Interaktion verweist die Spezifikation auf [NIP-89: Recommended Application Handlers](/de/topics/nip-89/).

Weil `alt` ein Tag ist, decken die Event-ID und die Signatur aus [NIP-01](/de/topics/nip-01/): [Basic protocol flow description](https://github.com/nostr-protocol/nips/blob/master/01.md) es ab. Eine gültige Signatur authentifiziert eine vom Autor kontrollierte Zusammenfassung: Sie zeigt, dass der Autor die Beschriftung veröffentlicht hat, nicht aber, dass sie zutrifft, irreführende Zusammenfassungen sind also möglich. Tags sind öffentlich, daher legt ein `alt` an einem Event mit verschlüsseltem Inhalt dessen Zusammenfassung offen und kann verraten, was der Inhalt verbirgt. Diese Eigenschaften ergeben sich aus der Hülle von [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md), nicht aus dem normativen Text von NIP-31. Ein `alt`-Tag auf oberster Ebene unterscheidet sich zudem vom `alt`-Feld für Bildbeschreibungen innerhalb von `imeta`, und Renderer parsen beide getrennt.

### Wie zwei Clients alt lesen {#how-two-clients-read-alt}

In der [Karte für unbekannte Events bei Commit 7c68acf](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx) von noStrudel wird das erste `alt`-Tag getrimmt und zur Hauptbeschriftung, optional ergänzt um eine Zeile `Using <client>`. Ein fehlender oder leerer Wert ergibt `Unknown event (kind ...)`, und unabhängig davon erscheinen bis zu drei Zeilen Inhalt. Dieselbe Komponente löst das `client`-Tag über NIP-89-Handler-Vorlagen auf und zeigt Open an, wenn eine teilbare Adresse existiert, sowie `Open in <client>`, wenn ein gültiger Handler-Link aufgelöst wird. Erklärung und App-Weiterleitung sind getrennte Bedienelemente.

[UnknownEventDigest.kt bei Commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170) von Amethyst bevorzugt Inhalt, den es als Fließtext einstuft, und greift ersatzweise auf `alt` zurück. Sein Parser trimmt Werte und nimmt das erste nicht leere `alt`, sodass ein Event, dessen erstes `alt` leer ist, hier anders beschriftet werden kann als in noStrudel. Beide Beschreibungen geben den Quellcode bei diesen Commits wieder, nicht bestätigtes Verhalten in Releases.

### Beispiel: eine Umfrage mit alt-Beschriftung {#example-a-poll-with-an-alt-label}

Die folgende Umfrage mit Kind 1068 wurde von wss://relay.damus.io abgerufen, und ihre ID und BIP340-Signatur sind nach den Regeln von [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md) gültig. Ein generischer Renderer kann den zweisprachigen `alt`-Text anzeigen, während ein umfragefähiger Client die Tags `option` und `polltype` ausliest.

```json
{
  "kind": 1068,
  "id": "7d1df3922833b47645922de43c2edd83e928a0ad083cee592beeee2b262bb743",
  "pubkey": "5f6dc275f3f9f8752d010a110c226148a9ba3399c5b63a0f469ee93b1394a53e",
  "created_at": 1793626294,
  "tags": [
    [
      "option",
      "z25mgp",
      "Windows"
    ],
    [
      "option",
      "ncddq0",
      "macOS"
    ],
    [
      "option",
      "4wta6q",
      "Linux"
    ],
    [
      "option",
      "p9ykti",
      "UNIX or FreeBSD/NetBSD/OpenBSD"
    ],
    [
      "polltype",
      "singlechoice"
    ],
    [
      "alt",
      "Poll: Which one do you usually use?\n普段どれを使っていますか？"
    ],
    [
      "client",
      "Ditto",
      "31990:781a1527055f74c1f70230f10384609b34548f8ab6a0a6caa74025827f9fdae5:ditto"
    ]
  ],
  "content": "Which one do you usually use?\n普段どれを使っていますか？",
  "sig": "f1378a723c65e83bd3105b593f10767903bde993788cfaf625583466fca21f1ef2be945bb2ca526aa9e898c93d5f1677a2f5ceaf70cb3a59c99f97eb179658fa"
}
```

### NIP-73: Gegenstände und Familien {#nip-73-subjects-and-families}

Die [NIP-73-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/73.md) (draft, optional, ohne unrecommended-Kennzeichnung) legt einen externen Gegenstand in einem `i`-Tag und dessen Identifikatorfamilie in einem `k`-Tag ab, sodass Clients einen exakten Gegenstand oder eine ganze Familie abfragen können. Ein Buch verwendet `["i", "isbn:9780765382030"]` mit `["k", "isbn"]`, eine Webseite ihre URL mit `k` auf `web`. NIP-73 definiert kein Event-Kind; andere Events tragen die Tags.

### Normalisierung und URL-Hinweise {#normalization-and-url-hints}

Der Abgleich beruht auf identischen Zeichenketten, deshalb legt die [Spezifikation](https://github.com/nostr-protocol/nips/blob/master/73.md) je Familie eine Form fest: URLs normalisiert und ohne Fragment, ISBNs ohne Bindestriche, Geohashes in Kleinbuchstaben, ISO-3166-Codes in Großbuchstaben. Ein optionales drittes Array-Element enthält einen URL-Hinweis für Clients, die zum Identifikator keine eigene Auffassung haben. Diesen Hinweis wählt der Autor, und er ist nicht Teil der Identität. Er beweist zudem keine Eigentümerschaft und benennt keine kanonische Website.

### Was ein gemeinsamer Identifikator nicht beweist {#what-a-shared-identifier-does-not-prove}

Gemäß [NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md) verbinden gleiche Identifikatoren Unterhaltungen und belegen sonst nichts. Ein signierter Kommentar identifiziert seinen Verfasser; er authentifiziert weder den Herausgeber des Buchs, der Website oder des Podcasts, noch zeigt er, wer diese kontrolliert. Aliasse, ausgabenspezifische ISBNs und unterschiedlich normalisierte URLs können einen Gegenstand auf mehrere Threads aufteilen. Der Kontext zählt: [NIP-22](/de/topics/nip-22/): [Comment](https://github.com/nostr-protocol/nips/blob/master/22.md) verwendet großgeschriebenes `I`/`K` für den Wurzelbereich und kleingeschriebenes `i`/`k` für das Elternelement, und [NIP-39: External Identities in Profiles](/de/topics/nip-39/) nutzt `i` für Profilidentitäten, daher ist nicht jedes `i`-Tag ein NIP-73-Gegenstand.

### NIP-73 in Parser- und Renderer-Code {#nip-73-in-parser-and-renderer-code}

[nip73.rs bei Commit 4c8099a](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs) von rust-nostr parst bekannte Präfixe in eine typisierte `ExternalContentId` und macht aus einem optionalen Hinweis eine typisierte URL; das dritte Tag-Element wird nur ausgegeben, wenn ein Hinweis vorhanden ist. Die Tests behalten ISBNs mit Bindestrichen bei: Der Parser entfernt das Präfix und speichert den Rest, ohne die Normalisierung der Spezifikation anzuwenden, typisiertes Parsen garantiert also keine kanonischen Zeichenketten. Chain-IDs trennt er von der Familie und bildet `ethereum:100:tx:<hash>` auf `ethereum:tx` ab. Diese Revision kennt keine Ländervariante `iso3166`.

[DisplayExternalId.kt bei Commit 553f761](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt) von Amethyst leitet Geohash- und Hashtag-Identifikatoren an eigene Anzeigen weiter. Auch URL-Identifikatoren erhalten eine eigene Anzeige, während andere unterstützte Typen an einen generischen Bereichs-Chip gehen. Eine URL öffnet die appeigene Thread-Route für diese Seite. Bei deaktivierten Vorschauen zeigt die normale Darstellung einen einfachen Link-Chip und fordert keine Vorschau an. Bei aktivierten Vorschauen kann das Abrufen einer fehlenden Vorschau die Zielseite kontaktieren. Das Abschalten der Vorschauen vermeidet diese Anfrage bei normaler Darstellung. Keine der beiden Dateien belegt das Verhalten in Releases.

### Beispiel: ein Kommentar zu einer Webseite {#example-a-comment-on-a-webpage}

Dieser Kommentar mit Kind 1111, abgerufen von wss://nos.lol, setzt dieselbe öffentliche Reddit-Thread-URL sowohl in sein `I`/`K`- als auch in sein `i`/`k`-Paar, mit `web` als Familie gemäß [NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md) und NIP-73. ID und Signatur sind gültig; das identifiziert, wer den Kommentar geschrieben hat, und sagt nichts über die verlinkte Seite aus.

```json
{
  "kind": 1111,
  "id": "e4229e38d93fad5d612ae21c401573bf8e87f0462dc2bd653804a252f98a238a",
  "pubkey": "ce5b8496c144a9dcd4990df6e265d9b60a21cde2515f3b206dc67b1c343790a9",
  "created_at": 1793590574,
  "tags": [
    [
      "I",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "K",
      "web"
    ],
    [
      "i",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "k",
      "web"
    ],
    [
      "client",
      "LayerTake"
    ],
    [
      "L",
      "layertake"
    ],
    [
      "l",
      "pin",
      "layertake"
    ],
    [
      "anchor",
      "{\"type\":\"text\",\"exact\":\"tools and systems\",\"prefix\":\"help • 6mo ago u/TheFarSea What \",\"suffix\":\" do you use for tracking and org\"}"
    ]
  ],
  "content": "Like this. I'm making this Public but could be just for me or friends/groups.",
  "sig": "a979389480d6ca919e4ab7b1ba92e532bf281be45c5df222e17d7d4ca62ef07d52c1004c0ce88620663dfac012b306154cfd73b858225764c701c40e3d9b7dfe"
}
```
