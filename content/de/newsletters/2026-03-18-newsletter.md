---
title: 'Nostr Compass #14'
date: 2026-03-18
translationOf: /en/newsletters/2026-03-18-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, deinem wöchentlichen Wegweiser durch Nostr.

**Diese Woche:** [Amethyst](https://github.com/vitorpamplona/amethyst) landet volle [NIP-47](/de/topics/nip-47/) (Nostr Wallet Connect) Methodenunterstützung, [Alby Hub](https://github.com/getAlby/hub) fügt Multi-Relay-Unterstützung in [v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6) hinzu, [Amber](https://github.com/greenart7c3/Amber) liefert [v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3) mit eingebautem Tor und feineren Signer-Berechtigungen, und [Zeus](https://github.com/ZeusLN/zeus) entfernt einen riskanten NWC-Keysend-Pfad in [PR #3835](https://github.com/ZeusLN/zeus/pull/3835). [Notedeck](https://github.com/damus-io/notedeck) liefert einen signierten Updater in [v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2), der Releases über [NIP-94](/de/topics/nip-94/) (File Metadata) Events entdeckt, während [Damus](https://github.com/damus-io/damus) veralteten [NIP-65](/de/topics/nip-65/) (Relay List Metadata) Zustand behebt, [Nostrability Outbox](https://github.com/nostrability/outbox) seine Benchmark-Ergebnisse mit korrigierten Daten überarbeitet, und [Primal iOS](https://github.com/PrimalHQ/primal-ios-app) direkte Relay-Subscriptions für DMs testet. [Primal Android](https://github.com/PrimalHQ/primal-android-app) liefert [3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7), [Route96](https://github.com/v0l/route96) liefert [v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0), [OpenChat](https://github.com/DavidGershony/openChat) verbessert weiter die Marmot-Interoperabilität in [v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11), [Pika](https://github.com/sledtools/pika) konsolidiert seine Runtime in [pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1), und [Nostria](https://github.com/nostria-app/nostria) fügt [NIP-85](/de/topics/nip-85/) (Trusted Assertions) Web-of-Trust-Filterung hinzu. Das NIPs-Repository mergt [NIP-54](/de/topics/nip-54/) (Wiki) Djot-Markup und eine 5000-Zeichen-Eingabebegrenzung für [NIP-19](/de/topics/nip-19/) (Bech32-Encoded Entities), während offene Vorschläge von `.nostrkey`-Datei-Backups für [NIP-49](/de/topics/nip-49/) (Private Key Encryption) bis zu einem [NIP-222](/de/topics/nip-222/) Share-Intent-URI reichen. Die NIP Deep Dives dieser Woche behandeln [NIP-94](#nip-deep-dive-nip-94-file-metadata) (File Metadata) und [NIP-54](#nip-deep-dive-nip-54-wiki).

## Neuigkeiten

### Wallet-Connect-Unterstützung wird breiter, und Wallet-Clients verschärfen Fehlerpfade

[Amethyst](https://github.com/vitorpamplona/amethyst), der Android-Client gepflegt von vitorpamplona, mergte [PR #1828](https://github.com/vitorpamplona/amethyst/pull/1828), der seine [NIP-47](/de/topics/nip-47/)-Implementierung nahe an die vollständige Protokollabdeckung bringt. Der Patch fügt `make_invoice`, `lookup_invoice`, `list_transactions`, `get_balance`, `get_info`, Hold-Invoice-Methoden, Keysend-Unterstützung mit TLV-Records, Capability-Discovery über Kind `13194` und Benachrichtigungs-Events auf Kind `23197` mit [NIP-44](/de/topics/nip-44/) (Encrypted Payloads) hinzu. Das gibt dem Client eine viel breitere NWC-Oberfläche, ohne auf App-spezifische Erweiterungen angewiesen zu sein.

Der umgebende Wallet-Stack bewegte sich in dieselbe Richtung. [Alby Hub](https://github.com/getAlby/hub), der selbstverwahrende Lightning-Node und Wallet-Dienst hinter vielen NWC-Deployments, lieferte [v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6) mit Multi-Relay-Unterstützung und einfacheren Verbindungs- und Swap-Flows. [Zeus](https://github.com/ZeusLN/zeus), die mobile Lightning-Wallet, mergte [PR #3835](https://github.com/ZeusLN/zeus/pull/3835), der NWC-Keysend-Unterstützung entfernt, nachdem ein stiller Fund-Drain-Pfad in diesem Flow identifiziert wurde, und behob gleichzeitig Pending-Event- und Cashu-Activity-Behandlung. Wallet-Konnektivität auf Nostr wird breiter, und Implementierer entfernen Flows, die schwer abzusichern sind.

### Notedeck verlagert Release-Erkennung auf Nostr

[Anschließend an die Notedeck-Berichterstattung der letzten Woche](/en/newsletters/2026-03-11-newsletter/), [Notedeck](https://github.com/damus-io/notedeck), der native Desktop-Client des Damus-Teams, lieferte [v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2) nach dem Mergen von [PR #1326](https://github.com/damus-io/notedeck/pull/1326). Der neue Updater abonniert signierte kind-`1063`-Release-Events, gleicht die lokale Plattform ab, lädt die referenzierte Binärdatei herunter und verifiziert deren SHA256-Hash vor der Installation. Release-Metadaten müssen nicht mehr von der GitHub-API oder einer Projektwebsite kommen. Ein vertrauenswürdiger Release-Pubkey und eine Relay-Verbindung reichen aus.

Derselbe Patch fügt eine `notedeck-release`-CLI hinzu, die diese Events aus GitHub-Release-Artefakten veröffentlicht, was bedeutet, dass die Release-Pipeline nun sowohl einen Nostr-nativen Veröffentlichungspfad als auch einen Nostr-nativen Erkennungspfad hat. Es bringt auch das Damus- und Notedeck-Updater-Modell viel näher an Zapstores Relay-veröffentlichten signierten Release-Flow: Zapstores `zsp`-Tooling behandelt bereits Software-Assets als kind-`1063`- oder `3063`-Events, sodass dieser Pfad nicht an einen Client oder einen Publisher gebunden ist. Der Rest des Release-Kandidaten ist praktische Desktop-Arbeit: Follow-Spalten, Profil-"View As User", [NIP-59](/de/topics/nip-59/) (Gift Wrap) Unterstützung, Echtzeit-Note-Statistiken und [NIP-11](/de/topics/nip-11/) (Relay Information Document) Limitation-Handling, aber der Updater ist der Teil, der diesen einen Release-Zyklus wahrscheinlich überdauert.

### Relay-Zustand rückt näher an Laufzeitverhalten

[Damus](https://github.com/damus-io/damus) mergte [PR #3665](https://github.com/damus-io/damus/pull/3665), der eine veraltete gespeicherte Relay-Listen-Event-ID durch eine direkte Datenbankabfrage für das neueste kind-`10002`-Event ersetzt. Wenn der alte Wert veraltet war, konnten Relay-Hinzufügen- und -Entfernen-Operationen auf Bootstrap- oder jahresalte Listen zurückfallen, was einige Relay-Änderungen als erfolgreich erscheinen ließ, während der aktive Zustand unverändert blieb. [PR #3690](https://github.com/damus-io/damus/pull/3690) behebt einen zweiten Fehlerpfad, indem veralteter `lock.mdb`-Zustand während der LMDB-Kompaktierung gelöscht wird, damit die App beim nächsten Start nicht mit `SIGBUS` abstürzt.

[Primal iOS](https://github.com/PrimalHQ/primal-ios-app) eröffnete [PR #194](https://github.com/PrimalHQ/primal-ios-app/pull/194), der direkt die [NIP-04](/de/topics/nip-04/) (Encrypted Direct Messages) Write-Relays eines Chatpartners abonniert, während eine Konversation geöffnet ist, wobei der Cache-Server als Fallback dient. [Nostur](https://github.com/nostur-com/nostur-ios-public) eröffnete [PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53), der randomisiertes Relay-Scoring, [NIP-66](/de/topics/nip-66/) Liveness-Filterung von nostr.watch und Thompson-Sampling kombiniert, um die Relay-Auswahl von einer festen Heuristik in eine gelernte Policy umzuwandeln. Clients haben Relay-Auswahl lange als Setup-Daten behandelt. Mehr Apps behandeln sie nun als Live-Zustand, der Mess- und Reparaturlogik benötigt.

## Releases

### Primal Android 3.0.7

[Primal Android](https://github.com/PrimalHQ/primal-android-app), der Android-Client von Primal, lieferte [3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7) mit einem neuen Poll- und Wallet-Zyklus. [PR #945](https://github.com/PrimalHQ/primal-android-app/pull/945) fügt Zap-basiertes Poll-Voting hinzu, [PR #948](https://github.com/PrimalHQ/primal-android-app/pull/948) paginiert das Laden von Stimmen, damit größere Umfragen nutzbar bleiben, und [PR #965](https://github.com/PrimalHQ/primal-android-app/pull/965) ruft Zap-Quittungen für alle Transaktionen ab. Dasselbe Release taggt unterstützte Events auch mit [NIP-89](/de/topics/nip-89/) (Recommended Application Handlers) Client-Metadaten in [PR #968](https://github.com/PrimalHQ/primal-android-app/pull/968), was nachgelagerten Clients hilft, Event-Ursprünge sauberer zuzuordnen.

### Amber v4.1.3

[Anschließend an die Amber-Berichterstattung der letzten Woche](/en/newsletters/2026-03-11-newsletter/), [Amber](https://github.com/greenart7c3/Amber), die Android-Signer-App für [NIP-55](/de/topics/nip-55/) Flows, lieferte [v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3). Der Release baut auf der jüngsten [NIP-42](/de/topics/nip-42/) Relay-Auth-Arbeit auf mit weiterer operationeller Härtung: [PR #327](https://github.com/greenart7c3/Amber/pull/327) fügt eingebautes Tor neben Orbot-Unterstützung hinzu, [PR #324](https://github.com/greenart7c3/Amber/pull/324) ersetzt grobe NIP-basierte Verschlüsselungsberechtigungen durch inhaltstypspezifische Regeln, und [PR #336](https://github.com/greenart7c3/Amber/pull/336) entfernt Netzwerkberechtigungen aus dem Offline-Flavor, während [PR #335](https://github.com/greenart7c3/Amber/pull/335) CI-Prüfungen hinzufügt, um das so beizubehalten. [PR #322](https://github.com/greenart7c3/Amber/pull/322) verschiebt auch die PIN-Speicherung in verschlüsselten DataStore.

Dieser Release verschärft die Signer-Grenze selbst. Das ist nützlich für jeden Android-Flow, der echte Schlüssel oder Relay-Auth-Entscheidungen an Amber übergibt, denn der schwierige Teil ist nicht nur, was der Signer kann. Es ist auch, wie eng er eingegrenzt werden kann.

### Route96 v0.6.0

[Anschließend an die Route96-Berichterstattung der letzten Woche](/en/newsletters/2026-03-11-newsletter/), [Route96](https://github.com/v0l/route96), der Medienserver, der Blossom und [NIP-96](/de/topics/nip-96/) (HTTP File Storage) unterstützt, veröffentlichte [v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0). Der Release verschiebt Konfiguration und Whitelist-Zustand in die Datenbank mit Hot Reload und fügt Aufbewahrungsrichtlinien für kalte oder alternde Dateien hinzu. Er fügt auch einen reichhaltigeren `GET /user/files`-Endpunkt plus Datei-Statistik-Tracking für Downloads und Egress hinzu, was Betreibern mehr Einblick gibt, wie ihr Speicherserver genutzt wird.

### OpenChat v0.1.0-alpha.11

[Anschließend an die OpenChat-Berichterstattung der letzten Woche](/en/newsletters/2026-03-11-newsletter/), [OpenChat](https://github.com/DavidGershony/openChat), der Avalonia-basierte Chat-Client auf dem Marmot-Stack, lieferte [v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11) nach einer Woche schneller Protokollarbeit. [Commit c33895d](https://github.com/DavidGershony/openChat/commit/c33895d6b1a198f01b9b01a7be974bdce033fb9c) verpackt Welcome-Events in [NIP-59](/de/topics/nip-59/) Gift Wrap und entfernt alte MIP-00-Tag-Normalisierungs-Shims, [Commit 2738ff4](https://github.com/DavidGershony/openChat/commit/2738ff428154f60f50debb8f2a53662d427b28f1) vervollständigt das MIP-02-Compliance-Audit, und [Commit 8e470cf](https://github.com/DavidGershony/openChat/commit/8e470cf7945bced010168c8229d73d67db638b9f) tut dasselbe für MIP-03-Gruppennachrichtenverschlüsselung. [Commit 129ca37](https://github.com/DavidGershony/openChat/commit/129ca37e264efaa2d1a8b04fe95cd72e5e212547) konsolidiert auch die NIP-44-Behandlung auf die gemeinsame marmot-cs-Implementierung, was das Risiko client-seitiger Krypto-Drift reduziert.

### nak v0.19.0 und v0.19.1

[nak](https://github.com/fiatjaf/nak), fiatjafs Kommandozeilen-Nostr-Toolkit, lieferte [v0.19.0](https://github.com/fiatjaf/nak/releases/tag/v0.19.0) und [v0.19.1](https://github.com/fiatjaf/nak/releases/tag/v0.19.1). Die 0.19-Serie fügt eine Gruppen-Forum-UI in [Commit 5f4efdb](https://github.com/fiatjaf/nak/commit/5f4efdbc69a36fc80ea3f97b2cdee1db6a7c5b47) hinzu, wechselt Gruppen-Metadaten-Edits auf einen vollständigen Replace-Flow in [Commit da0b753](https://github.com/fiatjaf/nak/commit/da0b75337198010687aceb6a07bbae67407faee3), und ersetzt die ältere `no-text`-Behandlung durch `supported_kinds` in [Commit bef67d3](https://github.com/fiatjaf/nak/commit/bef67d35d259e0450debf0fd870e1a937a2406bf). Für Gruppen-Implementierer hält das die CLI im Einklang mit der Richtung, in die sich Gruppen-Specs und -Clients bewegen.

## Projekt-Updates

### Amethyst

[Anschließend an die Amethyst-Berichterstattung der letzten Woche](/en/newsletters/2026-03-11-newsletter/), [Amethyst](https://github.com/vitorpamplona/amethyst), der Android-Client mit einer der breitesten Protokolloberflächen in Nostr, baute nach dem NIP-47-Patch weiter an seiner Wallet- und Relay-Arbeit. [PR #1853](https://github.com/vitorpamplona/amethyst/pull/1853) fügt [NIP-45](/de/topics/nip-45/) (Event Counting) COUNT-Abfragen über Relay-Management-Bildschirme hinzu, sodass Nutzer sehen können, wie viele Events jedes Relay tatsächlich für Home-Feed, Benachrichtigungen, DMs und Index-Daten vorhält. [PR #1849](https://github.com/vitorpamplona/amethyst/pull/1849) fügt verschlüsselte Datei-Uploads für [NIP-17](/de/topics/nip-17/) (Private Direct Messages) Chats hinzu, mit einem Retry-Pfad für unverschlüsselte Uploads, wenn ein Speicher-Host die verschlüsselte Version ablehnt.

[PR #1791](https://github.com/vitorpamplona/amethyst/pull/1791) bringt auch vollständigen [NIP-46](/de/topics/nip-46/) (Nostr Connect) Desktop-Bunker-Login mit einem Heartbeat-Indikator, was wichtig ist, weil Remote-Signing-Fehler von der Nutzerseite oft wie zufällige UI-Ausfälle wirken. Der Client zeigt, ob der Signer aktiv ist und wie kürzlich er geantwortet hat, und macht gleichzeitig deutlich, wenn die aktuelle Sitzung einen Bunker verwendet.

### Nostria

[Nostria](https://github.com/nostria-app/nostria), der Multiplattform-Client mit einem Local-First-Stack, mergte [PR #561](https://github.com/nostria-app/nostria/pull/561) und fügt Web-of-Trust-Filterung für Feeds und Thread-Antworten hinzu. Das Feature nutzt die bestehenden Trust-Service-Rang-Daten und stellt sie sowohl als Feed-Filter als auch als Antwort-Filter zur Verfügung, wobei Autoren ausgeblendet werden, deren Rang den Schwellenwert nicht erreicht, während die Thread-Struktur erhalten bleibt, wenn vertrauenswürdige Nachfolger vorhanden sind. Das gibt Nutzern eine Zwischenschicht zwischen "alle anzeigen" und fest codierter listenbasierter Kuration.

Dieselbe Woche brachte auch [PR #563](https://github.com/nostria-app/nostria/pull/563), der Content-Filterung und Repost-Unterstützung zur Zusammenfassungsseite hinzufügt. Außerhalb der getrackten PR-Liste hat Nostria auch mehr seiner Power-User-Oberfläche gefüllt. Es unterstützt nun den neuesten Brainstorm Web-of-Trust-Dienst mit In-App-Anmeldung, zusammen mit Geld-Sende- und -Empfangsflows in DMs über NWC und BOLT-11-Invoices. Es fügt auch Nostr-native GIF-Behandlung über das Emoji-NIP und einen stärkeren RSS-Import-Pfad für Musiker hinzu, der bestehende Lightning-Splits aus Podcast-Feeds übernehmen kann. Nostria behandelt Ranking, Medien, Zahlungen und Publishing als eine verbundene App-Oberfläche.

### Nostur

[Nostur](https://github.com/nostur-com/nostur-ios-public), der iOS-Client gepflegt von nostur-com, eröffnete [PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53), um Outbox-Routing von einem festen Plan in eine bewertete Policy umzuwandeln. Der Patch fügt randomisiertes Relay-Scoring, [NIP-66](/de/topics/nip-66/) Relay-Liveness-Filterung mit einem gecachten nostr.watch-Feed und Thompson-Sampling hinzu, sodass Relay-Erfolgs- und -Fehlerdaten zukünftige Auswahlen ändern. Das Design behält ein Sicherheitsventil bei, wenn zu viele Relays herausgefiltert würden, und bewahrt `.onion`-Relays. Dies ist eines der klarsten aktuellen Beispiele dafür, wie ein Client Relay-Auswahl als adaptives System behandelt.

### Nostrability Outbox

[Anschließend an den früheren Outbox-Benchmark-Bericht](/de/newsletters/2026-03-04-newsletter/), [Nostrability Outbox](https://github.com/nostrability/outbox), das Benchmark- und Analyseprojekt für [NIP-65](/de/topics/nip-65/) und [NIP-66](/de/topics/nip-66/) Client-Routing, verbrachte die Woche damit, seine eigenen Behauptungen zu verschärfen. [PR #35](https://github.com/nostrability/outbox/pull/35) ersetzt aufgeblähte Thompson-Sampling-Ergebnisse durch einen vollständigen Re-Benchmark über 1.511 Durchläufe und empfiehlt die `CG3`-Variante für NDK-artiges Routing. [PR #43](https://github.com/nostrability/outbox/pull/43) fügt Decay- und Anwendungsfall-Vergleiche hinzu, behebt einen `0 follows`-Cache-Poisoning-Bug und führt dann das Telluride-Dataset nach dem Pinnen von Cache-TTLs erneut aus.

Das ist keine Produktarbeit im üblichen Sinne, aber es ist wichtig für Client-Autoren, weil die Zahlen des Projekts nun schärfer und weniger schmeichelhaft an den Stellen sind, an denen sie zuvor zu viel beansprucht hatten. Das korrigierte Ergebnis ist trotzdem nützlich. Randomisierte Auswahl schlägt weiterhin rein deterministische Routing-Verfahren in den Fällen, die Outbox interessieren, Thompson-artiges Lernen kann die Abdeckung materiell verbessern, wenn Clients nützliche Relay-Historie persistieren, und [NIP-66](/de/topics/nip-66/) Liveness-Filterung spart verschwendete Zeit bei toten Relays. Die Arbeit mündet auch in konkrete Implementierungsvorschläge, darunter [NDK #387](https://github.com/nostr-dev-kit/ndk/pull/387), [Nostur #53](https://github.com/nostur-com/nostur-ios-public/pull/53), [Amethyst #1833](https://github.com/vitorpamplona/amethyst/pull/1833), [rust-nostr #1282](https://github.com/rust-nostr/nostr/pull/1282), [welshman #53](https://github.com/coracle-social/welshman/pull/53) und [applesauce #54](https://github.com/hzrd149/applesauce/pull/54) plus [applesauce #55](https://github.com/hzrd149/applesauce/pull/55).

### White Noise Backend

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs), das Rust-Backend, das von White Noise und anderem Marmot-Tooling verwendet wird, mergte zwei Boundary-Härtungs-Patches rund um Blossom-Medienbehandlung. [PR #637](https://github.com/marmot-protocol/whitenoise-rs/pull/637) erzwingt HTTPS auf Blossom-URLs und fügt ein Upload-Timeout hinzu, während [PR #642](https://github.com/marmot-protocol/whitenoise-rs/pull/642) Blob-Downloads auf `100 MiB` begrenzt, um übergroße Medienabrufe daran zu hindern, sich in einen Denial-of-Service-Pfad zu verwandeln. Für Private-Messaging-Software sind Medien-URLs eine der schärfsten Schnittstellen zwischen verschlüsselter Anwendungslogik und nicht vertrauenswürdiger Netzwerkinfrastruktur. Diese Woche hat das Team diese Kante verschärft.

### rust-nostr

[rust-nostr](https://github.com/rust-nostr/nostr), die Rust-Protokollbibliothek, mergte [PR #1280](https://github.com/rust-nostr/nostr/pull/1280), der Convenience-Konstruktoren für `LocalRelayBuilderNip42` hinzufügt. Die neuen Read- und Write-Helper geben eingebetteten Relay- und Test-Setups einen klareren Weg, [NIP-42](/de/topics/nip-42/) Auth-Policy in Code umzusetzen. Dies ist ein kleiner Bibliotheks-Patch, aber er ist wichtig für Teams, die lokale oder App-gebündelte Relays bauen, die Auth eingeschaltet brauchen, ohne jedes Mal Boilerplate zu wiederholen.

### Pika

[Anschließend an die frühere Pika-Berichterstattung](/de/newsletters/2026-03-04-newsletter/), [Pika](https://github.com/sledtools/pika), die Marmot-basierte Messaging-App, lieferte [pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1) und [pikachat-v1.1.1](https://github.com/sledtools/pika/releases/tag/pikachat-v1.1.1) mit einem Release-Zyklus, der auf Runtime-Konvergenz fokussiert ist. [PR #542](https://github.com/sledtools/pika/pull/542) führt eine gemeinsame Marmot-Runtime-Fassade für CLI und Sidecar ein, wobei der App-Host auf dieselbe Oberfläche migriert. [PR #556](https://github.com/sledtools/pika/pull/556) verschärft den OpenClaw-Agenten-Lebenszyklus und Provisioning-Zustand, während [PR #600](https://github.com/sledtools/pika/pull/600) Restore-from-Backup und strengere Recovery-Sicherheit für verwaltete Umgebungen hinzufügt.

Die direkte nutzerfreundliche Oberfläche ist hier kleiner als im letzten Pika-Bericht, aber die architektonische Änderung ist bedeutsam. Gruppen-, Medien-, Call- und Session-Logik hinter eine gemeinsame Runtime zu ziehen, reduziert die Chance, dass App und Daemon auseinanderdriften, während der Marmot-Stack wächst.

## NIP-Updates

Aktuelle Änderungen am [NIPs-Repository](https://github.com/nostr-protocol/nips):

**Gemergt:**

- **[NIP-54](/de/topics/nip-54/) (Wiki): Wechsel von Asciidoc zu Djot** ([PR #2242](https://github.com/nostr-protocol/nips/pull/2242)): Wiki-Inhalte auf Kind `30818` verwenden nun Djot als kanonisches Markup-Format. Der gemergte Text fügt explizites Wikilink-Verhalten, Merge-Request-Beispiele für Kind `818`, Redirect-Beispiele für Kind `30819` und Normalisierungsbeispiele für nicht-lateinische Schriften bei `d`-Tags hinzu. Das gibt Implementierern ein saubereres Parse-Ziel als Asciidoc und entfernt einen weiteren Spec-Pfad, der auf einer Ruby-zentrierten Toolchain basierte.

- **[NIP-19](/de/topics/nip-19/) (Bech32-Encoded Entities): Eingabegrenze hinzufügen** ([PR #2264](https://github.com/nostr-protocol/nips/pull/2264)): Die Spezifikation empfiehlt nun eine Begrenzung von Bech32-kodierten Entity-Strings auf 5000 Zeichen. Dies ist eine kleine Änderung mit echtem Parser-Wert, weil NIP-19-Strings mittlerweile in QR-Flows, Deep-Links, Share-Sheets und nutzereingefügter Eingabe über viele Clients erscheinen.

**Offene PRs und Diskussionen:**

- **Nostr-Key-Datei für [NIP-49](/de/topics/nip-49/) (Private Key Encryption)** ([PR #2269](https://github.com/nostr-protocol/nips/pull/2269)): Schlägt ein `.nostrkey`-Dateiformat für passwort-verschlüsselten Schlüsselexport und -import vor. Bei einem Merge würde es Clients einen normaleren dateibasierten Backup-Pfad geben, als rohe `ncryptsec`-Strings herumzukopieren.

- **Mitgliedschaftsstatus-Konsistenz für [NIP-43](/de/topics/nip-43/) (Relay Access Metadata and Requests)** ([PR #2267](https://github.com/nostr-protocol/nips/pull/2267)): Fügt einen Abschnitt hinzu, der klarstellt, dass Relays einen autoritativen Mitgliedschaftsstatus pro Pubkey führen sollten. Das würde die Gruppen-Client-Logik rund um Mitgliedschaftsänderungen und replizierte Historie vereinfachen.

- **Löschungsanleitung für [NIP-17](/de/topics/nip-17/) (Private Direct Messages)** ([PR #2260](https://github.com/nostr-protocol/nips/pull/2260)): Schlägt einen konkreten Pfad für das Bearbeiten und Löschen privater Nachrichten durch Gift-Wrapped-Delete-Events vor. Die Arbeit ist noch offen, aber Client-Autoren brauchen hier eine Antwort, wenn NIP-17 ältere DM-Flows vollständig ersetzen soll.

- **Share-Intent-URI für [NIP-222](/de/topics/nip-222/)** ([PR #2266](https://github.com/nostr-protocol/nips/pull/2266)): Der Entwurf würde standardisieren, wie mobile und Desktop-Apps geteilte Inhalte an einen Nostr-Client übergeben. Das ist eine der rauesten Interop-Kanten in aktuellen App-zu-App-Flows.

## NIP Deep Dive: NIP-94 (File Metadata)

[NIP-94](/de/topics/nip-94/) definiert Kind `1063` als erstklassiges Metadaten-Event für eine Datei. Die [Spezifikation](https://github.com/nostr-protocol/nips/blob/master/94.md) gibt dem Event einen eigenen menschenlesbaren `content` plus maschinenlesbare Tags für Download-URL, MIME-Typ, Hashes, Dimensionen, Vorschauen, Fallbacks und Speicherdienst-Hinweise. Das ist wichtig, weil die Datei auf Relays als eigenes Objekt abfragbar wird. Ein Client muss keine Metadaten aus umgebendem Inhalt herausparsen, um zu verstehen, was die Datei ist.

```json
{
  "id": "6a92ef8d7c3a1b5d4e8f9a0b1c2d3e4f567890abcdef1234567890abcdef1234",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1742342400,
  "kind": 1063,
  "tags": [
    ["url", "https://downloads.example.org/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["m", "application/gzip"],
    ["x", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["ox", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["size", "48392011"],
    ["dim", "0x0"],
    ["magnet", "magnet:?xt=urn:btih:00112233445566778899aabbccddeeff00112233"],
    ["i", "00112233445566778899aabbccddeeff00112233"],
    ["blurhash", "LEHV6nWB2yk8pyo0adR*.7kCMdnj"],
    ["thumb", "https://downloads.example.org/notedeck/v0.8.0-rc2/thumb.png", "bbccddeeff00112233445566778899aabbccddeeff0011223344556677889900"],
    ["image", "https://downloads.example.org/notedeck/v0.8.0-rc2/screenshot.png", "ccddeeff00112233445566778899aabbccddeeff001122334455667788990011"],
    ["summary", "Signed macOS release artifact for Notedeck v0.8.0-rc2"],
    ["alt", "Notedeck desktop release archive"],
    ["fallback", "https://mirror.example.net/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["service", "nip96"]
  ],
  "content": "Notedeck macOS universal build",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

Die Tags leisten mehr, als sie zunächst erscheinen. `x` identifiziert die ausgelieferte Datei, während `ox` die Originaldatei vor jeder serverseitigen Transformation identifiziert. Die Vorschau-Tags erlauben Clients, durchsuchbare Datei-Indizes zu erstellen, ohne das vollständige Asset herunterladen zu müssen, und `summary` kann daneben einen kurzen Auszug tragen. `fallback` gibt eine zweite Quelle, wenn die Haupt-URL ausfällt, und `service` weist auf das Speicherprotokoll hinter der Datei hin, wie [NIP-96](/de/topics/nip-96/) oder einen anderen Host. NIP-94 sitzt daher unterhalb von Social Posting und oberhalb von Roh-Speicher. Es beschreibt die Datei, nicht die Konversation um die Datei.

Deshalb ist der Notedeck-Updater dieser Woche interessant. [PR #1326](https://github.com/damus-io/notedeck/pull/1326) verwendet signierte kind-`1063`-Events für Software-Release-Erkennung und verifiziert dann die heruntergeladene Binärdatei gegen den veröffentlichten SHA256. Dieselbe Event-Form kann ein Software-Artefakt oder einen Medien-Upload beschreiben. NIP-94 ist alt genug, um stabil zu sein, hat aber noch Raum zum Wachsen, weil mehr Projekte Metadaten-Events als Transport für Maschinen behandeln, nicht nur als Dekoration für Menschen.

## NIP Deep Dive: NIP-54 (Wiki)

[NIP-54](/de/topics/nip-54/) definiert Kind `30818` als Wiki-Artikel-Event. Die [Spezifikation](https://github.com/nostr-protocol/nips/blob/master/54.md) behandelt den `d`-Tag als das normalisierte Artikelthema und erlaubt vielen Autoren, Einträge für dasselbe Thema zu veröffentlichen. Der Artikelkörper lebt in `content`, während Tags normalisierte Identität, Anzeigetitel, Zusammenfassungen und Referenzen zu früheren Versionen handhaben. Das bedeutet, NIP-54 ist nicht nur ein Inhaltsformat. Es ist auch ein Abruf- und Ranking-Problem, weil jeder Client immer noch entscheiden muss, welche Artikelversion er anzeigt.

```json
{
  "id": "8c94e5d1f2a300112233445566778899aabbccddeeff00112233445566778899",
  "pubkey": "00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff",
  "created_at": 1742342400,
  "kind": 30818,
  "tags": [
    ["d", "nostr-wiki"],
    ["title", "Nostr Wiki"],
    ["summary", "Djot-formatted reference article about Nostr wiki events"],
    ["a", "30818:11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff:nostr-wiki", "wss://relay.example.org", "fork"],
    ["e", "11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff", "wss://relay.example.org", "fork"]
  ],
  "content": "Nostr is a [protocol][] for carrying events across relays.\n\n[protocol]: nostr:nevent1example",
  "sig": "33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889900112233cc44dd55ee66ff77889900aabbccddeeff00112233445566778899001122"
}
```

Der Merge dieser Woche ändert das kanonische Markup von Asciidoc zu Djot in [PR #2242](https://github.com/nostr-protocol/nips/pull/2242). Das ist wichtig für Implementierer, weil Djot eine straffere eigenständige Spezifikation und einfachere Parser-Geschichte über Sprachen hinweg hat. Der gemergte Text klärt auch, wie referenzbasierte Wikilinks aufgelöst werden, wie Merge-Requests Kind `818` verwenden, wie Weiterleitungen Kind `30819` verwenden und wie sich die `d`-Tag-Normalisierung für nicht-lateinische Schriften verhalten sollte. Das sind die Teile, die zwei unabhängige Clients dazu bringen, sich einig zu sein, auf welchen Artikel ein Link zeigt.

NIP-54 sitzt auch an einem ungewöhnlichen Ort im Protokoll. Ein Wiki-Client braucht Content-Rendering, aber er braucht auch Ranking-Policy. Reaktionen, Relay-Listen, Kontaktlisten und explizite Deference-Signale fließen alle in die Frage ein, welcher Artikel für ein bestimmtes Thema gewinnt. Der Djot-Wechsel löst dieses Ranking-Problem nicht, aber er entfernt eine der Parser-Mehrdeutigkeiten, die darunter lagen. Deshalb ist der Merge jetzt wichtig: Die Änderung handelt weniger von hübscherer Prosa-Formatierung und mehr davon, Multi-Client-Wiki-Verhalten konsistenter implementierbar zu machen.

Wer etwas baut oder möchte, dass wir darüber berichten: Per [NIP-17](/de/topics/nip-17/) DM erreichbar auf Nostr unter `npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923`.
