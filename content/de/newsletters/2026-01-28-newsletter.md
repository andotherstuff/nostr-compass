---
title: 'Nostr Compass #7'
date: 2026-01-28
translationOf: /en/newsletters/2026-01-28-newsletter.md
translationDate: 2026-01-28
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, deinem wöchentlichen Wegweiser durch Nostr.

**Diese Woche:** Ridestr bringt dezentralisierte Mitfahrgelegenheiten zu Nostr mit [Cashu](/de/topics/cashu/)-Zahlungen und verschlüsselter Standortfreigabe. Pomade führt E-Mail-basierte Wiederherstellung für Multisig-Unterzeichner ein. Damus liefert [negentropy](/de/topics/negentropy/) für zuverlässige DM-Synchronisierung. Amethysts Desktop-App fügt Suche, Lesezeichen und Zaps hinzu. Amber v4.1.1 zeigt Relay-Vertrauensbewertungen an. Marmot merged MIP-03 und entwickelt eine TypeScript-Referenz-Chat-App. diVine fügt [NIP-46](/de/topics/nip-46/) QR-Authentifizierung und Erwähnungs-Unterstützung hinzu. Neue NIP-Vorschläge befassen sich mit Community-Management, sequenzbasierter Synchronisierung und verschlüsselter Dateispeicherung. Wir werfen auch einen Blick zurück auf fünf Jahre Nostr-Januare und verfolgen die Entwicklung des Protokolls von einer Handvoll früher Anwender im Jahr 2021 über den explosiven App Store-Start von Damus im Jahr 2023 bis zum ausgereiften Client-Ökosystem von 2025.

## Neuigkeiten

### Ridestr bringt dezentralisiertes Ridesharing zu Nostr

[Ridestr](https://github.com/variablefate/ridestr) entwickelt eine Peer-to-Peer-Mitfahranwendung, die vollständig auf Nostr aufgebaut ist und direkte Fahrer-Fahrgast-Transaktionen mit Bitcoin- und [Cashu](/de/topics/cashu/)-Zahlungen ermöglicht. Das Protokoll verwendet benutzerdefinierte Event-Arten (30173, 3173-3175, 30180/30181) zur Koordinierung von Fahrten und wahrt dabei die Privatsphäre durch progressive Standortfreigabe und [NIP-44](/de/topics/nip-44/)-Verschlüsselung.

Das System funktioniert durch einen sorgfältig choreografierten Ablauf: Fahrer übertragen ihre Verfügbarkeit mit geohash-codierten Standorten (~5km Präzision) über kind 30173 Events, Fahrgäste fordern Fahrten mit Preisschätzungen über kind 3173 an, und Zahlungen werden mittels HTLC-Treuhand-Tokens vor Fahrtbeginn gesichert. Die Standortprivatsphäre wird durch progressive Freigabe gewahrt, bei der Abholdetails erst bei Ankunft des Fahrers und Zielorte erst nach PIN-Verifizierung geteilt werden. Die gesamte Kommunikation zwischen den Parteien verwendet [NIP-44](/de/topics/nip-44/)-Verschlüsselung für Privatsphäre.

Ridestr implementiert Zahlungssicherheit durch HTLC-Treuhand mit P2PK-Signaturen. Wenn ein Fahrgast das Angebot eines Fahrers annimmt, sperrt er [Cashu](/de/topics/cashu/)-Tokens mit einem Zahlungs-Hash, den nur der Fahrer nach Abschluss der Fahrt einlösen kann. Das Protokoll arbeitet derzeit mit Single-Mint-Architektur, die erfordert, dass Fahrgäste und Fahrer denselben [Cashu](/de/topics/cashu/)-Mint verwenden. Die Kotlin-basierte Android-Implementierung des Projekts übernimmt die Proof-Verifizierung und Wiederherstellung veralteter Proofs durch NUT-07 Zustandsprüfungen.

Ridestr nimmt Herausforderungen an, die die meisten Nostr-Anwendungen vermeiden: Echtzeit-Standortkoordination, Zahlungs-Treuhand mit Streitbeilegung und Reputationssysteme für Interaktionen in der physischen Welt. Das Projekt befindet sich in der Beta-Phase und demonstriert, dass Nostrs Event-Modell Peer-to-Peer-Dienstleistungsmarktplätze unterstützen kann, nicht nur Content-Sharing.

### Pomade startet Alpha-Wiederherstellungssystem für Multisig-Unterzeichner

[Pomade](https://github.com/coracle-social/pomade), entwickelt von hodlbod, baut auf dem bestehenden [FROSTR](https://github.com/FROSTR-ORG)-Ökosystem auf, um einen wiederherstellungsorientierten Schwellenwert-Signierdienst bereitzustellen. Unter Verwendung von [FROST](/de/topics/frost/) (Flexible Round-Optimized Schnorr Threshold) Signaturen über die @frostr/bifrost-Bibliothek fügt Pomade E-Mail-basierte Wiederherstellungsabläufe zur Schwellenwert-Kryptographie hinzu. Das System teilt den geheimen Schlüssel eines Benutzers mit Shamir Secret Sharing auf und verteilt Anteile auf mehrere unabhängige Unterzeichner mit einem konfigurierbaren Schwellenwert (2-von-3, 3-von-5, usw.).

Das Protokoll arbeitet vollständig über Nostr unter Verwendung einer einzigen Event-Art (28350) mit [NIP-44](/de/topics/nip-44/)-verschlüsselten Payloads. Beim Signieren fordert der Client Teil-Signaturen von mindestens `threshold` Unterzeichnern an und aggregiert diese dann zu einer gültigen Schnorr-Signatur. Für die Verschlüsselung arbeiten die Unterzeichner zusammen, um gemeinsame Geheimnisse über ECDH abzuleiten, ohne dass eine einzelne Partei den vollständigen Schlüssel erfährt.

Die Wiederherstellung funktioniert über zwei Authentifizierungsmethoden: passwortbasiert (unter Verwendung von argon2id mit dem pubkey des Unterzeichners als Salt) oder E-Mail-OTP. Um MITM-Angriffe während der OTP-Wiederherstellung zu verhindern, generiert jeder Unterzeichner seinen eigenen Verifizierungscode mit einem vom Client bereitgestellten Präfix, was Benutzer dazu zwingt, sich unabhängig bei jedem Unterzeichner zu authentifizieren. Das Protokoll erfordert Proof-of-Work für Registrierungs-Events (20+ Bits gemäß [NIP-13](/de/topics/nip-13/)) um Spam zu verhindern.

Das Vertrauensmodell ist explizit: Wenn `threshold` Unterzeichner zusammenarbeiten, können sie den Schlüssel stehlen. E-Mail-Anbietern wird vollständig vertraut, da sie OTPs abfangen können. Benutzer können ihren vollständigen geheimen Schlüssel nicht unabhängig wiederherstellen; dies erfordert die Zusammenarbeit von `threshold` Unterzeichnern. Das Protokoll ist für das Onboarding neuer Benutzer konzipiert, die mit Schlüsselverwaltung nicht vertraut sind, mit der ausdrücklichen Empfehlung, dass Benutzer zur Selbstverwahrung wechseln sollten, sobald sie sich sicher fühlen. Pomade warnt vor potenziellem „Schlüsselverlust, Diebstahl, Denial of Service oder Metadaten-Lecks" angesichts seines ungeprüften Alpha-Status.

## Releases

### Damus liefert Negentropy für zuverlässige DM-Synchronisierung

[Damus v1.13](https://github.com/damus-io/damus/tree/v1.13) liefert die negentropy-Implementierung, [die wir letzte Woche als offenen PR vorgestellt haben](/de/newsletters/2026-01-21-newsletter/#damus-ios-client---open-prs). [PR #3536](https://github.com/damus-io/damus/pull/3536) fügt grundlegende [negentropy](/de/topics/negentropy/)-Unterstützung zur Netzwerkschicht hinzu und ermöglicht Set-Reconciliation mit Relays, die das Protokoll unterstützen. Ein begleitender [PR #3547](https://github.com/damus-io/damus/pull/3547) fügt Pull-to-Refresh DM-Synchronisierung hinzu, die negentropy verwendet, um fehlende Nachrichten wiederherzustellen, wenn Standard-REQ-Subscriptions fehlschlagen.

Die Implementierung folgt einem konservativen Ansatz: Das normale DM-Laden bleibt unverändert, wobei [negentropy](/de/topics/negentropy/) als Wiederherstellungsmechanismus verfügbar ist, wenn Benutzer manuell aktualisieren. Automatisierte Tests demonstrieren die Korrektur, indem sie eine DM mit einem alten Zeitstempel generieren, die Standard-Abfragen verfehlen würden, und dann die [negentropy](/de/topics/negentropy/)-Synchronisierung verwenden, um sie erfolgreich abzurufen. Während [negentropy](/de/topics/negentropy/)-Unterstützung kompatible Relays erfordert, handhabt die Implementierung gemischte Relay-Umgebungen elegant, indem sie das Protokoll dort verwendet, wo es verfügbar ist.

### Amber v4.1.1 - Relay-Vertrauensbewertungen

[Amber v4.1.1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.1) liefert die Anzeige von Relay-Vertrauensbewertungen ([PR #289](https://github.com/greenart7c3/Amber/pull/289)) und implementiert die in der [letztewöchigen Berichterstattung über Trusted Relay Assertions NIP diskutierten](/de/newsletters/2026-01-21-newsletter/#nip-updates) Relay-Bewertungskonzepte. Vertrauensbewertungen erscheinen jetzt auf der Relays-Seite und für NostrConnect-Verbindungsanfragen und helfen Benutzern, die Zuverlässigkeit von Relays einzuschätzen, bevor sie Verbindungen autorisieren. Das Release enthält auch eine neu gestaltete Login/Events/Berechtigungen-Benutzeroberfläche und Unterstützung für die `switch_relays`-Methode. Leistungsverbesserungen cachen Keystore-Operationen und beheben Berichte über 20+ Sekunden Ladezeiten auf älteren Geräten.

### nak v0.18.2 - MCP-Integration

fiatjafs [nak](https://github.com/fiatjaf/nak) (Nostr Army Knife) [v0.18.2](https://github.com/fiatjaf/nak/releases/tag/v0.18.2) fügt [Model Context Protocol](https://nostrify.dev/mcp)-Unterstützung über `nak mcp` hinzu und ermöglicht es KI-Agenten, auf Nostr nach Personen zu suchen, Notizen zu veröffentlichen, Benutzer zu erwähnen und Inhalte mit dem Outbox-Modell zu lesen. Das Release führt auch einen [Einzeilen-Installer](https://github.com/fiatjaf/nak/blob/master/install.sh) (`curl -sSL https://raw.githubusercontent.com/fiatjaf/nak/master/install.sh | sh`) ein, der vorgefertigte Binärdateien herunterlädt und die Go-Toolchain-Anforderung für Endbenutzer eliminiert. Der Bunker-Modus unterstützt jetzt Unix-Sockets und `switch_relays`.

### Zeus v0.12.2 Beta - NWC-Korrekturen

[Zeus v0.12.2-beta1](https://github.com/ZeusLN/zeus/releases) liefert mehrere NWC-Korrekturen, die Probleme aus der [letztewöchigen Zeus-Berichterstattung](/de/newsletters/2026-01-21-newsletter/#zeus-lightning-wallet-with-nostr-wallet-connect) beheben.

## Projekt-Updates

### Amethyst Desktop - Phase 2A ausgeliefert

[Amethyst](https://github.com/vitorpamplona/amethyst) rollte [Phase 2A seiner Desktop-App](https://github.com/vitorpamplona/amethyst/pull/1676) aus und fügte Suche, Lesezeichen, Zaps, Thread-Ansichten und Langform-Inhalte (Reads) zur Desktop-Erfahrung hinzu. Ein begleitender [PR #1683](https://github.com/vitorpamplona/amethyst/pull/1683) fügt transparentes Event-Broadcasting-Feedback hinzu, sodass Benutzer jetzt den Echtzeit-Status pro Relay sehen, während ihre Events über das Netzwerk verbreitet werden, was die Diagnose von Verbindungsproblemen erleichtert.

### Notedeck-Fortschritt: Kalender-App und UX-Politur

Die Desktop-Anwendung [Notedeck](https://github.com/damus-io/notedeck) des Damus-Teams merged das Auto-Hide-Toolbar-Verhalten ([PR #1268](https://github.com/damus-io/notedeck/pull/1268)), das auf die Scroll-Geschwindigkeit reagiert, um mehr Bildschirmfläche in mobilen Ansichten zu bieten. Ein [Entwurfs-PR #1271](https://github.com/damus-io/notedeck/pull/1271) fügt eine vollständige [NIP-52](/de/topics/nip-52/) Kalender-App mit Monats-/Wochen-/Tages-/Agenda-Ansichten, RSVP-Unterstützung und [NIP-22](/de/topics/nip-22/)-Kommentaren zu Kalenderereignissen hinzu, derzeit mit Feature-Flag für Tests.

### Jumble fügt Community-Modus hinzu

[Jumble](https://github.com/CodyTseng/jumble), der relay-fokussierte Web-Client, fügte [Community-Modus](https://github.com/CodyTseng/jumble/pull/738) und Unterstützung für [Relay-Set-Voreinstellungen über Umgebungsvariablen](https://github.com/CodyTseng/jumble/pull/736) hinzu, was die Bereitstellung thematischer Instanzen wie [nostr.moe](https://nostr.moe/) erleichtert.

### Shopstr Bestellungs-Dashboard

[Shopstr](https://github.com/shopstr-eng/shopstr) ersetzte sein chat-basiertes Bestellungsmanagement durch ein dediziertes [Bestellungs-Dashboard](https://github.com/shopstr-eng/shopstr/pull/219). Die neue Oberfläche bietet Händlern eine zentrale Ansicht zur Verfolgung des Bestellstatus, zum Markieren von Nachrichten als gelesen und zur Verwaltung der Erfüllung, ohne durch Chat-Threads scrollen zu müssen. Das Update deprecates IndexedDB-Caching zugunsten von serverseitigen Bestellstatus-APIs und überarbeitet die Art und Weise, wie Bestellungs-DMs für bessere Filterung getaggt werden.

### Formstr fügt Raster-Fragen hinzu

[Formstr](https://github.com/abh3po/nostr-forms), die Nostr-native Formular-App, fügte [Raster-Fragen](https://github.com/abh3po/nostr-forms/pull/419) hinzu und [schrieb sein SDK um](https://github.com/abh3po/nostr-forms/pull/410) mit Embed-Unterstützung. Ein [Fix für nicht-[NIP-07](/de/topics/nip-07/)-Unterzeichner](https://github.com/abh3po/nostr-forms/pull/418) behob Probleme für Benutzer mit Bunker- oder lokalen Unterzeichnern, die versuchten, Formulare mit ihrer Identität abzuschicken.

### nostr-tools aktualisiert Krypto-Abhängigkeiten

[nostr-tools](https://github.com/nbd-wtf/nostr-tools), die Kern-JavaScript-Bibliothek, [aktualisierte auf @noble/curves v2.0.1](https://github.com/nbd-wtf/nostr-tools/pull/520), behob Breaking-API-Änderungen in 27 Dateien und übernahm die neuesten auditierten noble-Bibliotheken. fiatjaf fügte auch `switch_relays`-Unterstützung zu [NIP-46](/de/topics/nip-46/) hinzu, was es Bunker-Clients ermöglicht, Relay-Verbindungen dynamisch zu ändern.

### Zeus arbeitet an NIP-87 Mint-Bewertungen

[Zeus](https://github.com/ZeusLN/zeus) hat einen [offenen PR für [NIP-87](/de/topics/nip-87/) Mint-Bewertungen](https://github.com/ZeusLN/zeus/pull/3576), der es Benutzern ermöglicht, [Cashu](/de/topics/cashu/)-Mints zu entdecken und zu bewerten, gefiltert nach Nostr-Follows. Bewertungen enthalten Sternebewertungen und können anonym oder mit dem nsec eines Benutzers abgegeben werden.

### Camelus liefert vollständige DM-Unterstützung

[Camelus](https://github.com/camelus-hq/camelus), ein Flutter-basierter Android-Client, der mit Dart NDK für batterieeffiziente mobile Leistung entwickelt wurde, fügte diese Woche umfassende Direktnachrichten mit 20+ Commits hinzu. Das Update umfasst Chat-Kategorien, Nachrichtendaten, optimistische Sende-UI, Notiz-an-sich-selbst-Funktionalität und ordnungsgemäße DM-Relay-Handhabung.

### Marmot-Protokoll-Updates

Die deterministische Commit-Auflösung MIP-03, [die wir letzte Woche als offenen PR vorgestellt haben](/de/newsletters/2026-01-21-newsletter/#marmot-protocol-white-noise-encrypted-group-chat-library), wurde jetzt gemerged. [MDK PR #152](https://github.com/marmot-protocol/mdk/pull/152) stellt sicher, dass alle [MLS](/de/topics/mls/)-basierten Gruppenchats auf denselben Zustand konvergieren, wenn mehrere gültige Commits für dieselbe Epoche ankommen.

Ein begleitender [Spec PR #28](https://github.com/marmot-protocol/marmot/pull/28) fügt Anforderungen für den init_key-Lebenszyklus hinzu, die Lücken aus Implementierungsaudits adressieren: Privates Schlüsselmaterial aus Welcome-Nachrichten muss nach der Verarbeitung sicher gelöscht werden (Nullierung, Speicherbereinigung), und neue Mitglieder müssen innerhalb von 24 Stunden Selbst-Updates für Forward Secrecy durchführen.

Das TypeScript SDK ([marmot-ts](https://github.com/marmot-protocol/marmot-ts)) entwickelt eine Referenz-Chat-Anwendung. [PR #37](https://github.com/marmot-protocol/marmot-ts/pull/37) fügt Gruppenerstellung/-auflistung, Key-Package-Management mit Publish/Broadcast/Delete-Flows und QR-Code-Einladungen hinzu. Ein [offener PR #38](https://github.com/marmot-protocol/marmot-ts/pull/38) von hzrd149 implementiert Nachrichtenverlaufs-Persistenz mit Paginierung. Das whitenoise-rs Backend merged diese Woche 15 PRs, darunter Mehrsprachenunterstützung ([PR #455](https://github.com/marmot-protocol/whitenoise-rs/pull/455)) und MIP-04 v2 Medienreferenzen ([PR #450](https://github.com/marmot-protocol/whitenoise-rs/pull/450)).

### diVine fügt Nostr-Integrationsfunktionen hinzu

[diVine](https://github.com/divinevideo/divine-mobile), die Kurzform-Video-App, setzt die schnelle Nostr-Integration fort.

Offene PRs umfassen [NIP-46](/de/topics/nip-46/) QR-Code-Authentifizierung ([PR #1019](https://github.com/divinevideo/divine-mobile/pull/1019)) und [NIP-17](/de/topics/nip-17/) verschlüsselte Direktnachrichten ([PR #834](https://github.com/divinevideo/divine-mobile/pull/834)). Die Aktivität dieser Woche konzentrierte sich auf [Erwähnungs-Unterstützung](https://github.com/divinevideo/divine-mobile/pull/1098), die `nostr:`-URIs und @Erwähnungen in klickbare Profillinks umwandelt, [Classic Viners Avatar-Fallbacks](https://github.com/divinevideo/divine-mobile/pull/1097) mit Nostr-Profilen und Video-Bearbeitungstools einschließlich [Zeichnen](https://github.com/divinevideo/divine-mobile/pull/1056), [Filter](https://github.com/divinevideo/divine-mobile/pull/1053) und [Sticker](https://github.com/divinevideo/divine-mobile/pull/1050).

## NIP-Updates

Aktuelle Änderungen am [NIPs-Repository](https://github.com/nostr-protocol/nips):

**Zusammengeführt:**

- **[Trusted Relay Assertions](https://github.com/nostr-protocol/nips/pull/1534)** - Der Vorschlag zur Standardisierung von Relay-Vertrauensbewertungen, [den wir letzte Woche vorgestellt haben](/de/newsletters/2026-01-21-newsletter/#nip-updates), wurde zusammengeführt. Die Spezifikation definiert kind 30385 Events für Relay-Vertrauensaussagen mit Bewertung über Zuverlässigkeit, Qualität und Erreichbarkeit. Die Diskussion vor dem Zusammenführen drehte sich darum, ob Vertrauensbewertungen „global" (einmal für alle Benutzer berechnet) oder „personalisiert" (relativ zum sozialen Graphen jedes Beobachters) sein sollten. PageRank-ähnliche Algorithmen wie [nostr.band's Trust Rank](https://trust.nostr.band/) und [GrapeRank](https://github.com/Pretty-Good-Freedom-Tech/graperank-nodejs) widerstehen Sybil-Angriffen, indem sie jeden durch gefälschte Konten weitergegebenen Rang durch die Größe der Bot-Farm teilen.

**Offene PRs und Diskussionen:**

- **Communikeys** - Ein [umfassender Vorschlag](https://nostrhub.io) für Community-Management, der bestehende npubs als Community-Identifikatoren verwendet, anstatt relay-basierter Ansätze. Jeder npub kann eine Community werden, indem er ein kind 10222 Event veröffentlicht; Veröffentlichungen zielen auf Communities über kind 30222 Events. Die Zugriffskontrolle verwendet [NIP-58](/de/topics/nip-58/)-Badges und ermöglicht delegiertes Mitgliedschaftsmanagement mit Cold Storage für Community-Schlüssel.

- **[NIP-CF: Changes Feed](https://github.com/nostr-protocol/nips/pull/2196)** - Ein Entwurf, der sequenzbasierte Event-Synchronisierung als Alternative zu zeitstempelbasierten `since`-Filtern vorschlägt. Das Problem: Standard-Nostr-Synchronisierung mit `since`-Zeitstempeln kann Events verpassen, wenn mehrere Events denselben sekundenpräzisen Zeitstempel teilen, Client- und Relay-Uhren auseinanderdriften oder Checkpointing ungenau ist. NIP-CF löst dies, indem Relays eingehenden Events monoton steigende Sequenznummern zuweisen, was eine strikte Gesamtordnung bietet. Clients fordern Änderungen seit einer bestimmten Sequenznummer an und erhalten Events in garantierter Reihenfolge mit präzisem Checkpointing, das niemals Events verpasst. Der Vorschlag unterstützt auch Live-/Continuous-Modus, bei dem Subscriptions nach der initialen Synchronisierung für Echtzeit-Updates offen bleiben.

- **[NIP-XX: Encrypted File Sync](https://github.com/nostr-protocol/nips/pull/1947)** - Ein Protokoll, das kinds 30800 (verschlüsselte Dateien), 30801 (Tresor-Indizes) und 30802 (geteilte Dokumente) für die Synchronisierung verschlüsselter Inhalte über Geräte hinweg mit Nostr-Relays definiert. Das Protokoll ermöglicht local-first Notiz-Apps, Ende-zu-Ende-verschlüsselte Synchronisierung ohne zentralisierte Server bereitzustellen. Dateiinhalte, Pfade, Namen und Ordnerstruktur werden alle mit [NIP-44](/de/topics/nip-44/) Selbstverschlüsselung verschlüsselt, sodass Relays Blobs speichern, die sie nicht lesen können. Binäre Anhänge wie Bilder verwenden [Blossom](/de/topics/blossom/)-Server mit clientseitiger Verschlüsselung. Kind 30802 ermöglicht die Dokumentenfreigabe zwischen Benutzern durch Verschlüsselung an den öffentlichen Schlüssel des Empfängers.

## Fünf Jahre Nostr-Januare

[Der Newsletter des letzten Monats](/de/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers) verfolgte Nostrs Dezember-Meilensteine von fiatjafs erstem Client-Release bis zu Jack Dorseys katalytischer Spende. Dieser Rückblick zeichnet nach, was jeden Januar von 2021 bis 2025 passierte, mit Fokus auf verifizierte technische Entwicklungen.

### Januar 2021: Frühe Entwicklung

Nostrs dritter Monat sah die fortgesetzte Entwicklung an Branle, fiatjafs Vue.js-Client, der im Dezember 2020 gestartet war. Eine kleine Gruppe früher Anwender, wahrscheinlich weniger als 15 Personen, koordinierte sich über die Telegram-Gruppe [@nostr_protocol](https://t.me/nostr_protocol) (erstellt am 16. November 2020) und testete das Protokoll auf ein oder zwei experimentellen Relays. Der Kommandozeilen-Client noscl ermöglichte terminalbasierte Interaktion.

Das technische Fundament war bereits festgelegt: Benutzer identifiziert durch secp256k1 öffentliche Schlüssel, Beiträge kryptographisch signiert mit Schnorr-Signaturen und Relays als dumme Speicher, die nicht miteinander kommunizieren. Dies war bewusst Bitcoin-native Kryptographie, eine Designentscheidung, die Jahre später die Adoptionsmuster prägen sollte.

### Januar 2022: Entwickler-Entdeckung

Der Januar 2022 begann, während Nostr noch vom [ersten Hacker-News-Auftritt](https://news.ycombinator.com/item?id=29749061) (31. Dezember 2021) summte, der 110 Punkte und 138 Kommentare generierte. Zum Zeitpunkt dieses Posts betrieben nur etwa sieben Relays das gesamte Netzwerk, wobei Kommentatoren anmerkten: „Spam ist noch kein Problem, weil Nostr super neu ist und niemand es benutzt." Robert C. Martin („Uncle Bob") hatte Nostr als potentiell „die Endspiel-Lösung für soziale Kommunikation" unterstützt. Die Diskussion setzte sich im Januar fort, wobei Entwickler über Relay-Architektur versus echtes P2P, Zensurresistenz versus Moderation und ob Einfachheit skalieren kann, debattierten.

Der HN-Post löste eine Welle neuer Implementierungen aus. Uncle Bob selbst startete [more-speech](https://github.com/unclebob/more-speech), einen Clojure-Desktop-Client, am 18. Januar. fiatjafs [go-nostr](https://github.com/nbd-wtf/go-nostr)-Bibliothek (erstellt Januar 2021) und [noscl](https://github.com/fiatjaf/noscl)-Kommandozeilen-Client stellten Go-Tooling bereit, während [nostr-tools](https://github.com/nbd-wtf/nostr-tools) JavaScript-Unterstützung bot. Bis Dezember 2022 hatten etwa 800 Profile Bios. Branle blieb der primäre Web-Client und erhielt Updates einschließlich Private-Key-Import und Multi-Relay-Unterstützung. Technische Herausforderungen waren offensichtlich: 64-Zeichen-Hex-Schlüssel erwiesen sich als unintuitiv, Nachrichtenverzögerungen frustrierten Benutzer, und die Community fragte sich, ob die Architektur Twitter-skaliertem Traffic standhalten könnte.

### Januar 2023: Der Durchbruch

Der Januar 2023 transformierte Nostr vom Experiment zur Bewegung. Damus, der iOS-Client von William Casarin (jb55), kämpfte mit Apples App Store-Genehmigungsprozess. Am 1. Januar abgelehnt, am 26. Januar erneut abgelehnt, wurde er schließlich [am 31. Januar genehmigt](https://www.coindesk.com/tech/2023/02/01/decentralized-social-media-project-nostrs-damus-gets-listed-on-apple-app-store). Diese Genehmigung löste eine Kaskade aus: Damus erreichte sofort Platz 10 in den US Social Networking Charts. Jack Dorsey [nannte es](https://web.archive.org/web/20240304043638/https://www.theblock.co/post/207448/nostr-based-decentralized-twitter-alternative-damus-goes-live-on-apple-app-store) „einen Meilenstein für offene Protokolle."

Acht Tage zuvor, am 23. Januar, [kündigte Edward Snowden](https://x.com/Snowden/status/1617623779626352640) seine Präsenz auf Nostr an: „Eines der coolen Dinge an Nostr... neben Zensurresistenz ist, dass man nicht auf 280 Zeichen beschränkt ist." Seine Unterstützung als NSA-Whistleblower hatte Gewicht in datenschutzbewussten Kreisen, und Benutzer begannen sofort, ihm Sats über Lightning zu zappen.

Web-Clients rannten um die Wette, um den Zustrom aufzunehmen. [Snort](https://github.com/v0l/snort), erstellt von kieran im Dezember 2022, entstand als funktionsreicher React-Client; am 13. Januar integrierte Snort NIP-05-Registrierung über die Nostr Plebs API, was neuen Benutzern ermöglichte, menschenlesbare Identitäten während des Onboardings zu beanspruchen. [Iris](https://iris.to), hauptberuflich entwickelt von Martti Malmi (einem frühen Bitcoin-Mitwirkenden, der die zweite Bitcoin-Transaktion überhaupt von Satoshi erhielt), bot sowohl Web- als auch Mobile-Interfaces mit kostenlosen NIP-05-Identitäten bei iris.to. [Astral](https://github.com/monlovesmango/astral), gebaut von monlovesmango mit Quasar (Vue.js) als Branle-Fork, konzentrierte sich auf Relay-Management mit seiner Relay-Gruppierungsfunktion, die es Benutzern ermöglichte, Relays in Sets zum Posten und Filtern zu organisieren. TestFlight-Betas für iOS-Clients füllten sich innerhalb von Stunden, und Amethyst dominierte Android.

Die Infrastruktur kämpfte, um Schritt zu halten. Alle Relays wurden von Enthusiasten betrieben, die aus eigener Tasche zahlten. Bezahlte Relays mit Lightning-Mikrozahlungen schufen natürliche Spam-Filterung, führten aber Zugangsreibung ein. [Damus wurde nur zwei Tage nach der Genehmigung aus Chinas App Store entfernt](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/), Berichten zufolge auf Anfrage von Chinas oberster Internet-Aufsichtsbehörde.

### Januar 2024: Protokoll-Härtung

Der Januar 2024 konzentrierte sich auf Protokollstandardisierung und Community-Aufbau. [Nostr PHX](https://www.nostrphx.com/events) startete das Jahr mit einem Meetup am 5. Januar in Phoenix und brachte lokale Cypherpunks zusammen. Dies war das erste von vielen Community-Events in diesem Jahr, darunter BTC Prague (Juni), Nostriga in Riga (August) und Nostrasia.

Die bedeutendste Protokollentwicklung war das Mergen von [NIP-59 (Gift Wrap)](https://github.com/nostr-protocol/nips/pull/716) am 29. Januar, das Metadatenschutz für verschlüsselte Kommunikation bietet. Gift Wrap baut auf [NIP-44s Verschlüsselungsstandard](https://github.com/paulmillr/nip44) (der im Dezember 2023 von [Cure53 auditiert](https://cure53.de/audit-report_nip44-implementations.pdf) worden war) auf, um die Absenderidentität vor Relays zu verbergen. Das Protokoll wickelt verschlüsselte Nachrichten in ein äußeres Event ein, das von einem zufälligen, einmalig verwendeten Schlüsselpaar signiert ist. Relays sehen nur den Wegwerf-Pubkey, während die echte Absenderidentität im verschlüsselten Payload verborgen ist, den nur der Empfänger entschlüsseln kann. Dies verhindert, dass Relay-Betreiber und Netzwerkbeobachter erfahren, wer mit wem kommuniziert. Zeitstempel können auch randomisiert werden, um Timing-Analysen zu vereiteln.

Das Ökosystem expandierte über Social Media hinaus. [Plebeian Market](https://plebeian.market) wurde vollständig Nostr-nativ mit [NIP-15](/de/topics/nip-15/)-Konformität und ermöglichte standübergreifende Warenkörbe und einen Standbrowser zum Entdecken von Händlern. [Shopstr](https://github.com/shopstr-eng/shopstr) entstand als erlaubnisfreier Marktplatz für Bitcoin-Handel. [Zap.stream](https://zap.stream/), gebaut von kieran, brachte Live-Streaming zu Nostr mit Lightning-Zahlungen zu 21 Sats/Minute. Entwicklerwerkzeuge reiften mit [NDK](https://github.com/nostr-dev-kit/ndk) für TypeScript-Abstraktionen und [rust-nostr](https://github.com/rust-nostr/nostr) für Rust-Bindings. [Zeus v0.8.1](https://blog.zeusln.com/new-release-zeus-v0-8-1/) lieferte Nostr-Kontaktimport und persistentes LND und legte den Grundstein für Nostr Wallet Connect Integration in späteren Releases.

Dennoch [blieb die Infrastruktur-Nachhaltigkeit herausfordernd](https://arxiv.org/abs/2402.05709). Akademische Forschung aus dieser Zeit fand, dass 95% der Relays Schwierigkeiten hatten, die Betriebskosten zu decken, wobei 20% erhebliche Ausfallzeiten erlebten. Die Eintrittsgebühr für bezahlte Relays betrug im Durchschnitt weniger als 1.000 Sats (~$0,45), unzureichend für einen nachhaltigen Betrieb.

*Eine Anmerkung zu Betrug: Das „Nostr Assets Protocol" und der zugehörige „$NOSTR"-Token, die ungefähr zu dieser Zeit gestartet wurden, [wurden öffentlich von fiatjaf angeprangert](https://www.aicoin.com/en/article/377704) als „100% betrügerisch" und „ein Affinitätsbetrug" ohne Verbindung zum eigentlichen Nostr-Protokoll.*

### Januar 2025: Client-Reifung

Der Januar 2025 sah die fortgesetzte Client-Entwicklung im gesamten Ökosystem. [Nostur 1.17.0](https://www.nobsbitcoin.com/nostur-v1-17-0/) lieferte am 13. Januar geräteübergreifende Synchronisierung für Lesestatus, [FROST](/de/topics/frost/) Multi-Sig-Login-Unterstützung und optimierte lokale Datenbankleistung. Amethyst setzte seinen Übergang zum Outbox-Modell fort und kompilierte automatisch Relay-Sets basierend auf Follow-Listen, anstatt manuelle Konfiguration zu erfordern.

Große Clients begannen, sich von [NIP-04](/de/topics/nip-04/) für Direktnachrichten zu entfernen und migrierten in Richtung [NIP-17](/de/topics/nip-17/) und dem vorgeschlagenen [NIP-104](/de/topics/nip-104/) für verbesserte Verschlüsselung und Metadatenschutz. Das Gossip-Modell (Outbox/Inbox-Kommunikation) gewann an Akzeptanz, während das Ökosystem auf effizientere Relay-Nutzungsmuster konvergierte. Branchenbeobachter sagten voraus, dass dies das Jahr sein würde, in dem Nostr vom Nischenprotokoll zur Mainstream-Anerkennung übergeht, mit einer möglichen hochkarätigen Plattformmigration, die die tägliche Aktivität verdoppeln könnte.

### Januar 2026: Sicherheits- und Signierinfrastruktur

Der Januar 2026 brachte bedeutende Fortschritte in der Sicherheits- und Signierinfrastruktur. [Primal Android 2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) lieferte [NIP-46](/de/topics/nip-46/) Remote-Signing und [NIP-55](/de/topics/nip-55/) lokale Signer-Unterstützung und gesellte sich zu Amber und Aegis als vollwertiger Signing-Hub für andere Android-Apps. [Bitchat absolvierte ein Cure53-Sicherheitsaudit](https://github.com/permissionlesstech/bitchat/pulls), dieselbe Firma, die Signal und NIP-44 auditierte, mit 17+ PRs, die kritische Befunde einschließlich DH-Geheimnis-Löschung und Thread-Sicherheitsprobleme beheben. Sowohl Bitchat als auch Damus migrierten von C Tor zu Rust Arti für verbesserte Zuverlässigkeit und Speichersicherheit.

Die Protokollarbeit setzte sich fort mit dem Mergen von [NIP-71](https://github.com/nostr-protocol/nips/pull/1669) (adressierbare Video-Events) und einer Post-Quanten-Kryptographie-NIP, die Diskussionen über die Zukunftssicherheit von Nostr gegen Quantenangriffe eröffnet. Der Trusted Relay Assertions-Entwurf schlug die Standardisierung von Relay-Vertrauensbewertungen durch signierte Attestierungen vor. Das [Marmot-Protokoll](https://github.com/marmot-protocol/mdk) härtete seine [MLS](/de/topics/mls/)-basierte verschlüsselte Nachrichtenübermittlung mit 18 gemergten PRs, die Audit-Befunde adressieren.

Realwelt-Anwendungen expandierten mit [Ridestr](https://github.com/variablefate/ridestr), das dezentralisiertes Ridesharing mit [Cashu](/de/topics/cashu/)-Treuhand und [NIP-44](/de/topics/nip-44/)-Verschlüsselung entwickelt, und [Pomade](https://github.com/coracle-social/pomade), das E-Mail-basierte Wiederherstellungsabläufe zu [FROST](/de/topics/frost/)-Schwellenwert-Signierung hinzufügt. Damus lieferte [negentropy](/de/topics/negentropy/) für zuverlässige DM-Synchronisierung, während Amethysts Desktop-App Phase 2A mit Suche, Lesezeichen und Zaps erreichte.

### Ausblick

Sechs Jahre von Januaren offenbaren Nostrs Evolution von früher Entwicklung (2021) zu öffentlicher Entdeckung (2022) zu explosivem Wachstum (2023) zu Protokoll-Härtung (2024) zu Client-Reifung (2025) zu Sicherheitsinfrastruktur (2026). Das Muster ist jedem vertraut, der das Wachstum offener Protokolle beobachtet hat: Jahre ruhiger Entwicklung, eine plötzliche Explosion, wenn die Bedingungen stimmen, dann die längere Arbeit, alles zuverlässig zu machen. Was mit sieben Relays und einem Hacker-News-Thread begann, ist jetzt auditierte Infrastruktur mit echten Anwendungen. Die Frage für 2027: Wenn jemand eine Fahrt ruft, eine verschlüsselte Nachricht sendet oder einen verlorenen Schlüssel mit Nostr wiederherstellt, werden sie dann überhaupt wissen, dass sie es benutzen?

---

Das war's für diese Woche. Baust du etwas? Hast du Neuigkeiten zu teilen? Möchtest du, dass wir über dein Projekt berichten? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Kontaktiere uns per NIP-17 DM</a> oder finde uns auf Nostr.
