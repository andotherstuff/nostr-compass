---
title: 'Nostr Compass #5'
date: 2026-01-13
publishDate: 2026-01-13
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, deinem wöchentlichen Leitfaden für Nostr.

**Diese Woche:** Bitchat durchläuft ein professionelles Sicherheitsaudit von Cure53, derselben Firma, die Signal und [NIP-44](/de/topics/nip-44/) geprüft hat, wobei bereits über 17 PRs mit Fixes für kritische Befunde gemergt wurden. [NIP-71](/de/topics/nip-71/) wurde gemergt und bringt adressierbare Video-Events ins Protokoll. Ein Post-Quantum-Kryptographie-NIP eröffnet die Diskussion über die Absicherung von Nostr gegen zukünftige Quantenangriffe. Amethyst v1.05.0 liefert Lesezeichenlisten, Sprachnachrichten und eine frühe Desktop-Version, während Nostur v1.25.3 [NIP-17](/de/topics/nip-17/)-DMs mit Reaktionen und Antworten verbessert. Bei den Libraries erweitert rust-nostr die [NIP-62](/de/topics/nip-62/)-Unterstützung auf SQLite- und LMDB-Backends, und NDK behebt einen Bug im Subscription-Tracking.

## Neuigkeiten

### Bitchat schließt Cure53-Sicherheitsaudit ab

Bitchat, der iOS-verschlüsselte Messenger, der Nostr mit Cashu kombiniert, hat ein professionelles Sicherheitsaudit von Cure53 durchlaufen, einer der angesehensten Sicherheitsfirmen der Branche. Cure53 hat zuvor Signal, Mullvad VPN und insbesondere die [NIP-44](/de/topics/nip-44/)-Verschlüsselungsspezifikation geprüft, die das Fundament moderner privater Nostr-Nachrichten bildet.

Das Audit fand mehr als 12 Sicherheitsprobleme (BCH-01-002 bis BCH-01-013). Das Bitchat-Team reagierte mit über 17 Pull Requests. Zu den wichtigsten Fixes gehören:

**Noise Protocol DH Secret Clearing** - [PR #928](https://github.com/permissionlesstech/bitchat/pull/928) behebt sechs Stellen, an denen Diffie-Hellman-Shared-Secrets nach dem Key Agreement nicht gelöscht wurden, und stellt damit die Forward-Secrecy-Garantien wieder her. Wenn Secrets länger als nötig im Speicher verbleiben, könnte ein Memory-Dump oder Cold-Boot-Angriff vergangene Kommunikation kompromittieren.

**Signaturverifizierung** - Mehrere PRs härten die kryptographischen Verifizierungspfade und stellen sicher, dass Nachrichtenauthentizitätsprüfungen nicht durch fehlerhafte Eingaben umgangen werden können.

**Thread-Sicherheit** - [PR #929](https://github.com/permissionlesstech/bitchat/pull/929) fügt Barrier-Synchronisation zu den Lesebestätigungs-Queues in NostrTransport hinzu und verhindert Race Conditions, die bei hohem Nachrichtenaufkommen zu Datenbeschädigung oder Abstürzen führen könnten.

**Speichersicherheit** - [PR #920](https://github.com/permissionlesstech/bitchat/pull/920) optimiert den Nachrichtendeduplikator für bessere Leistung bei hohem Nachrichtendurchsatz und vermeidet gleichzeitig Speichererschöpfung.

**Eingabevalidierung** - [PR #919](https://github.com/permissionlesstech/bitchat/pull/919) härtet das Parsing von Hex-Strings, um Abstürze durch fehlerhafte Eingaben zu verhindern, ein häufiger Angriffsvektor für Denial-of-Service.

Bitchat verarbeitet Cashu-Ecash, weshalb eine professionelle Sicherheitsüberprüfung unerlässlich ist. Das Audit folgt auf das [Marmot](/de/topics/marmot/)-Protokoll-Audit vom letzten Jahr und das NIP-44-Audit, das die Verschlüsselungsschicht verifizierte.

## NIP-Updates

Aktuelle Änderungen am [NIPs-Repository](https://github.com/nostr-protocol/nips):

**Gemergt:**

- **[NIP-71](/de/topics/nip-71/)** - Adressierbare Video-Events ([#1669](https://github.com/nostr-protocol/nips/pull/1669)) führt kinds 34235 (horizontales Video) und 34236 (vertikales Video) als adressierbare Events ein. Ein erforderlicher `d`-Tag liefert eindeutige Identifikatoren, sodass Video-Metadaten aktualisiert werden können, ohne das gesamte Event neu zu veröffentlichen. Ein optionaler `origin`-Tag verfolgt Importquellen. Bereits in Amethyst und nostrvine implementiert.

**Offene PRs:**

- **Post-Quantum-Kryptographie** - [PR #2185](https://github.com/nostr-protocol/nips/pull/2185) schlägt vor, quantenresistente kryptographische Algorithmen zu Nostr hinzuzufügen. Die Spezifikation führt ML-DSA-44 und Falcon-512 für digitale Signaturen ein und zielt auf „hochwertige Events" wie Anwendungen und Autoritäten ab, nicht auf einzelne Benutzer. Während die symmetrische Verschlüsselung von [NIP-44](/de/topics/nip-44/) (ChaCha20) quantenresistent ist, verwendet der Schlüsselaustausch secp256k1 ECDH, das anfällig für Shors Algorithmus ist. Der Vorschlag enthält ML-KEM für Key Agreement, um diese Lücke zu schließen. Dies ist ein Vorschlag im Frühstadium, der die Diskussion über Krypto-Agilität für Nostrs langfristige Sicherheit eröffnet.
- **BOLT12 für NIP-47** - Nach 137 Kommentaren und ausführlicher Diskussion entschied die Community, dass BOLT12-Offers eine eigene Spezifikation verdienen, anstatt [NIP-47](/de/topics/nip-47/) zu erweitern. BOLT12-Offers bieten erhebliche Verbesserungen gegenüber BOLT11-Invoices, darunter Wiederverwendbarkeit, bessere Privatsphäre durch Blinded Paths und optionale Zahlungsinformationen. Das neue NIP wird Methoden wie `make_offer`, `pay_offer` und `list_offers` für Nostr Wallet Connect-Implementierungen definieren.
- **Audio-Track-NIP** - [PR #1043](https://github.com/nostr-protocol/nips/pull/1043) schlägt kinds 32100 für Musiktracks und 32101 für Podcast-Episoden vor und gibt Audioinhalten die gleiche erstklassige Behandlung, die NIP-71 für Video bietet. Derzeit verwenden Audioplattformen wie Wavlake, Zapstr und Stemstr jeweils proprietäre Event-Formate, was das Ökosystem fragmentiert. Ein gemeinsamer Standard würde Interoperabilität ermöglichen, sodass Benutzer Audio von jedem kompatiblen Client entdecken und abspielen können.
- **NIP-A3 Universal Payment Targets** - [PR #2119](https://github.com/nostr-protocol/nips/pull/2119) schlägt kind 10133 Events vor, die RFC-8905 `payto:`-URIs verwenden, um Zahlungsoptionen über mehrere Netzwerke hinweg bereitzustellen. Anstatt separate Event-Kinds für Bitcoin, Lightning, Cashu oder traditionelle Zahlungswege zu erstellen, ermöglicht diese Abstraktion Clients, standardisierte Tags zu parsen und native Zahlungs-Handler aufzurufen. Der Ansatz ist zukunftssicher, da neue Zahlungsmethoden nur ein `payto:`-URI-Schema benötigen.

## NIP-Vertiefung: NIP-51 und NIP-65

Diese Woche behandeln wir zwei NIPs, die Benutzereinstellungen speichern: NIP-51 zum Organisieren von Inhalten und NIP-65 zum Organisieren von Relay-Verbindungen. Beide verwenden ersetzbare Events, was bedeutet, dass jede neue Veröffentlichung die vorherige Version überschreibt.

### [NIP-51](/de/topics/nip-51/): Listen

[NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md) definiert mehrere Listentypen zum Organisieren von Referenzen auf Events, Benutzer, Hashtags und andere Inhalte. Amethyst v1.05.0 fügt Lesezeichen-Unterstützung hinzu, was dies zu einem guten Zeitpunkt macht, um zu verstehen, wie Listen funktionieren.

Die Spezifikation definiert mehrere List-Kinds, die jeweils einem anderen Zweck dienen. Kind 10000 ist deine Stummschaltungsliste zum Ausblenden von Benutzern, Threads oder Wörtern. Kind 10001 pinnt Events, um sie auf deinem Profil hervorzuheben. Kind 30003 speichert Lesezeichen, was Amethyst jetzt unterstützt. Andere Kinds verwalten Follow-Sets (30000), kuratierte Artikelsammlungen (30004), Hashtag-Interessen (30015) und benutzerdefinierte Emoji-Sets (30030).

Listen referenzieren Inhalte über Tags. Eine Lesezeichenliste verwendet `e`-Tags für spezifische Events und `a`-Tags für adressierbaren Inhalt wie Artikel:

```json
{
  "id": "ae3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1736784000,
  "kind": 30003,
  "tags": [
    ["d", "saved-articles"],
    ["e", "abc123def456...", "wss://relay.example"],
    ["a", "30023:author-pubkey:article-id", "wss://relay.example"]
  ],
  "content": "<encrypted-private-bookmarks>",
  "sig": "908a15e46fb4d8675bab026fc230a0e3542bfade63da02d542fb78b2a8513fcd0092619a2c8c1221e581946e0191f2af505dfdf8657a414dbca329186f009262"
}
```

Der `d`-Tag liefert einen eindeutigen Identifikator, sodass du mehrere Lesezeichen-Sets wie „saved-articles", „read-later" oder „favorites" unter demselben Kind pflegen kannst.

Listen unterstützen sowohl öffentliche als auch private Einträge. Öffentliche Einträge erscheinen im Tags-Array und sind für jeden sichtbar, der das Event abruft. Private Einträge kommen in das `content`-Feld und werden mit [NIP-44](/de/topics/nip-44/) an dich selbst verschlüsselt. Diese duale Struktur ermöglicht es dir, öffentliche Lesezeichen zu führen und gleichzeitig private Notizen anzuhängen, oder eine Stummschaltungsliste zu pflegen, ohne preiszugeben, wen du stummgeschaltet hast. Um an dich selbst zu verschlüsseln, verwende NIP-44 mit deinem eigenen pubkey als Empfänger.

Die 10000er-Serie-Kinds sind ersetzbar, was bedeutet, dass Relays nur ein Event pro pubkey behalten. Die 30000er-Serie sind parametrisiert ersetzbar und erlauben ein Event pro pubkey- und `d`-Tag-Kombination. In beiden Fällen bedeutet das Aktualisieren einer Liste das Veröffentlichen eines vollständigen Ersatzes; du kannst keine inkrementellen Änderungen senden. Clients sollten unbekannte Tags beim Ändern von Listen beibehalten, um das Überschreiben von Daten zu vermeiden, die von anderen Anwendungen hinzugefügt wurden.

### [NIP-65](/de/topics/nip-65/): Relay-Listen-Metadaten

[NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md) definiert kind 10002 Events, die bekannt geben, welche Relays ein Benutzer zum Lesen und Schreiben bevorzugt. Dies hilft anderen Benutzern und Clients, deine Inhalte zu finden.

```json
{
  "id": "bd2217a96b5835b59f9a6a42d8d8a36f8c9b7d4e5f0a1b2c3d4e5f6a7b8c9d0e1",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1736784000,
  "kind": 10002,
  "tags": [
    ["r", "wss://relay.damus.io", "read"],
    ["r", "wss://nos.lol"],
    ["r", "wss://relay.nostr.band", "write"]
  ],
  "content": "",
  "sig": "f1c2d3e4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2"
}
```

Jeder `r`-Tag enthält eine Relay-URL und einen optionalen Marker. Ein `write`-Marker bezeichnet deine Outbox: Relays, auf denen du deine Inhalte veröffentlichst. Ein `read`-Marker bezeichnet deine Inbox: Relays, auf denen du nach Erwähnungen, Antworten und Tags schaust. Das Weglassen des Markers zeigt beides an.

Wenn Alice Bobs Beiträge finden will, ruft ihr Client Bobs kind 10002 ab, extrahiert seine Write-Relays (seine Outbox) und abonniert dort. Wenn Alice auf Bob antwortet, veröffentlicht ihr Client auf seinen Read-Relays (seiner Inbox), damit er die Erwähnung sieht. Dieses relay-bewusste Routing ist das „Outbox-Modell", und es verteilt Benutzer auf viele Relays, anstatt alle auf wenigen zentralen Servern zu konzentrieren.

NIP-65 behandelt das Routing öffentlicher Inhalte, aber private Nachrichten verwenden eine separate Liste. [NIP-17](/de/topics/nip-17/) definiert kind 10050 für DM-Inbox-Relays und verwendet `relay`-Tags anstelle von `r`-Tags. Beim Senden einer privaten Nachricht suchen Clients nach dem kind 10050 Event des Empfängers und veröffentlichen dort die verschlüsselte Gift-Wrapped-Nachricht. Diese Trennung hält das DM-Routing vom Routing öffentlicher Inhalte getrennt und ermöglicht es Benutzern, verschiedene Relays für private und öffentliche Kommunikation anzugeben.

Das Outbox-Modell verbessert die Zensurresistenz, da kein einzelnes Relay die Inhalte aller speichern oder bereitstellen muss. Clients halten Verbindungen zu Relays aufrecht, die in den NIP-65-Events ihrer gefolgten Benutzer aufgelistet sind, und verbinden sich dynamisch mit neuen Relays, wenn sie neue Konten entdecken. NIP-65 ergänzt die Relay-Hints, die in anderen NIPs zu finden sind. Wenn du jemanden mit `["p", "pubkey", "wss://hint.relay"]` taggst, teilt der Hint Clients mit, wo sie nach dieser spezifischen Referenz suchen sollen. NIP-65 liefert die autoritative, vom Benutzer kontrollierte Liste, während Hints Abkürzungen bieten, die in einzelne Events eingebettet sind.

Für beste Ergebnisse halte deine Relay-Liste aktuell, da veraltete Einträge dich schwerer auffindbar machen. Die Spezifikation empfiehlt zwei bis vier Relays pro Kategorie. Das Auflisten zu vieler Relays belastet jeden Client, der deine Inhalte abrufen möchte, verlangsamt deren Erfahrung und erhöht die Netzwerklast. Clients cachen NIP-65-Events und aktualisieren sie regelmäßig, um auf dem neuesten Stand zu bleiben, wenn Benutzer ihre Einstellungen ändern.

## Releases

**Amethyst v1.05.0** - Der beliebte Android-Client [liefert ein großes Update](https://github.com/vitorpamplona/amethyst/releases) mit mehreren Hauptfunktionen. [NIP-51](/de/topics/nip-51/) kind 30003 Lesezeichenlisten ermöglichen es Benutzern, Beiträge zur späteren Referenz zu speichern und über kompatible Clients hinweg zu synchronisieren. Sprachnachrichten funktionieren jetzt in DMs und normalen Beiträgen mit Wellenformvisualisierung, Medienserver-Auswahl und Upload-Fortschrittsanzeigen. [Web of Trust](/de/topics/web-of-trust/)-Scores sind jetzt in der Oberfläche sichtbar und helfen Benutzern zu verstehen, wie der Algorithmus Konten relativ zu ihrem sozialen Graphen bewertet. Die [Quartz](/de/topics/quartz/)-Datenbankmigration verbessert die Abfrageleistung als Teil der von OpenSats finanzierten Kotlin-Multiplatform-Arbeit. Ein frühes Desktop-Release bringt Amethyst über Compose Multiplatform auf Windows, macOS und Linux und teilt dieselbe Codebasis wie die Android-App. Neue Benutzer-Onboarding-Flows erleichtern die Erfahrung für erstmalige Nostr-Benutzer.

**Nostur v1.25.3** - Der iOS- und macOS-Client [konzentriert sich auf private Nachrichten](https://github.com/nostur-com/nostur-ios-public/releases) mit [NIP-17](/de/topics/nip-17/)-Verbesserungen. DM-Konversationen unterstützen jetzt Reaktionen und Antworten und bringen die Interaktivität öffentlicher Beiträge in verschlüsselte Nachrichten. Die Konversationsansicht wurde mit besserem Threading überarbeitet, sodass Mehrfachnachrichtenaustausche leichter zu verfolgen sind, und Zeitstempel zeigen „Zeit her" in der DM-Liste für schnelles Scannen. Desktop-Benutzer erhalten Multi-Spalten-Layouts zum gleichzeitigen Anzeigen mehrerer Feeds oder Konversationen. [NIP-46](/de/topics/nip-46/) Remote-Signer-Unterstützung ermöglicht es Benutzern, ihre privaten Schlüssel in dedizierten Signer-Apps wie Amber oder nsec.app aufzubewahren. Zusätzliche Fixes stellen die DM-Funktionalität auf iOS 15 und iOS 16 wieder her, beheben Benachrichtigungsverzögerungen und fügen die Möglichkeit hinzu, zu konfigurieren, welche Relays veröffentlichte DMs erhalten.

## Bemerkenswerte Code- und Dokumentationsänderungen

*Dies sind offene Pull Requests und Arbeiten im Frühstadium, perfekt um Feedback zu erhalten, bevor sie gemergt werden. Wenn dich etwas interessiert, erwäge einen Review oder Kommentar!*

### Citrine (Android Relay)

[PR #89](https://github.com/greenart7c3/Citrine/pull/89) behebt eine SQL-Injection-Schwachstelle in der persönlichen Android-Relay-App. Das Problem ermöglichte es fehlerhaften Event-Daten, beliebige Datenbankabfragen auszuführen, ein ernstes Problem für jede App, die nicht vertrauenswürdige Eingaben speichert und verarbeitet. Der Fix bereinigt alle Datenbankoperationen ordnungsgemäß mit parametrisierten Abfragen. Es wurde noch kein Release getaggt, sodass Benutzer auf die nächste Version warten oder aus dem Quellcode bauen müssen. [PR #90](https://github.com/greenart7c3/Citrine/pull/90) optimiert die ContentProvider-Abfrageleistung mit Filterung und Paginierung auf Datenbankebene und reduziert die Latenz, wenn externe Apps wie Amethyst über Androids Inter-Process-Communication-Layer auf Citrines Event-Datenbank zugreifen.

### rust-nostr (Library)

Die [NIP-62](/de/topics/nip-62/) (Vanish Requests) Unterstützung wird über die Datenbank-Backends von rust-nostr hinweg erweitert. [PR #1180](https://github.com/rust-nostr/nostr/pull/1180), vor zwei Wochen gemergt, fügte NIP-62-Unterstützung zu SQLite hinzu und behandelt `ALL_RELAYS` Vanish Requests, da die Datenbankschicht keine spezifischen Relay-URLs kennt. [PR #1210](https://github.com/rust-nostr/nostr/pull/1210) erweitert dies auf das LMDB-Backend und stellt sicher, dass Vanish Requests auf der Festplatte persistiert werden und Relay-Neustarts überleben. Eine IndexedDB-Implementierung für Browser-Umgebungen ist ebenfalls in Arbeit. Zusammen geben diese Änderungen Entwicklern konsistente NIP-62-Unterstützung über SQLite, LMDB und bald Browser-Storage hinweg.

### NDK (Nostr Development Kit)

[PR #375](https://github.com/nostr-dev-kit/ndk/pull/375) behebt einen Bug im seenEvents-Tracking-System. Das Problem führte dazu, dass bestimmte Subscription-Muster Events fälschlicherweise als bereits gesehen markierten, was zu verpassten Inhalten führte, wenn Benutzer neue Subscriptions öffneten oder sich wieder mit Relays verbanden. Der Fix stellt sicher, dass Events über Subscription-Lebenszyklen hinweg korrekt verfolgt werden, was besonders wichtig für Anwendungen ist, die basierend auf Benutzernavigation dynamisch subscriben und unsubscriben. NDK wurde auf beta.70 aktualisiert mit diesem Fix.

### Damus (iOS)

[PR #3515](https://github.com/damus-io/damus/pull/3515) behebt einen Startabsturz, der iOS 17-Benutzer betraf. Das Problem stammte von einem arithmetischen Überlauf in `NdbUseLock`, einer Fallback-Klasse, die verwendet wird, weil Swift Mutexes auf iOS 17 nicht verfügbar sind. Der Fix ersetzt den vorherigen Synchronisationsansatz durch `NSLock`, das auf iOS 17 verfügbar ist und die verbleibenden Race Conditions ordnungsgemäß behandelt. iOS 18+-Benutzer waren nicht betroffen, da sie Zugang zur nativen Swift Mutex-Implementierung haben.

Separat landete eine Reihe von Longform-Artikel-Verbesserungen über [PR #3509](https://github.com/damus-io/damus/pull/3509). Lesefortschrittsbalken verfolgen deine Position durch Artikel, geschätzte Lesezeiten erscheinen auf Vorschauen, und Sepia-Modus mit einstellbaren Zeilenhöheneinstellungen bieten komfortableres Lesen. Der Fokusmodus blendet die Navigations-Chrome beim Scrollen automatisch aus und stellt sie bei Tippen wieder her, was visuelle Ablenkungen für ablenkungsfreies Lesen reduziert. Mehrere Fixes beheben die Bildanzeige in Markdown-Inhalten und stellen sicher, dass Artikel oben statt mittendrin geöffnet werden.

### Zap.stream (Live-Streaming)

YouTube- und Kick-Chat-Integration verbindet Nachrichten von externen Streaming-Plattformen mit Nostr. Streamer, die zu YouTube, Kick und Zap.stream multicasten, können jetzt alle Chat-Nachrichten in einer einheitlichen Ansicht sehen, wobei Nachrichten von jeder Plattform neben nativen Nostr-Kommentaren erscheinen. Dies beseitigt einen großen Reibungspunkt für Creator, die Nostr zum Streamen nutzen möchten, aber Audiences auf etablierten Plattformen nicht aufgeben können. Die Integration zeigt an, von welcher Plattform jede Nachricht stammt, und übernimmt den Authentifizierungsflow zum Verbinden externer Konten.

### Chachi (NIP-29 Groups)

Der [NIP-29](/de/topics/nip-29/) Gruppen-Chat-Client lieferte diese Woche sechs gemergte PRs. Ein Sicherheitsupdate adressiert [CVE-2026-22029](https://github.com/purrgrammer/chachi/pull/89), eine XSS-Schwachstelle in react-router, die Open-Redirect-Angriffe ermöglichen könnte; der Fix aktualisiert auf react-router-dom 6.30.0. [PR #92](https://github.com/purrgrammer/chachi/pull/92) fügt paginiertes Nachrichten-Laden für Gruppenchats hinzu, sodass lange Konversationen inkrementell statt auf einmal geladen werden. [PR #91](https://github.com/purrgrammer/chachi/pull/91) behebt mehrere NIP-29-Bugs, darunter eine Race Condition, die beim ersten Laden zu leeren Gruppennamen führte, und undefinierte Teilnehmerlisten, die Mitgliederansichten zum Absturz brachten. Die Übersetzungsabdeckung umfasst jetzt alle 31 unterstützten Sprachen mit je 1060 Schlüsseln.

### 0xchat (Messaging)

Der Messaging-Client im Telegram-Stil verbesserte die [NIP-55](/de/topics/nip-55/)-Compliance, indem Signer-Paketnamen bei Verwendung externer Signatur-Apps ordnungsgemäß gespeichert werden, was Probleme behebt, bei denen die App nach Neustarts den Überblick verlor, welcher Signer verwendet werden sollte. Die NIP-17-Antwortbehandlung enthält jetzt korrekt den `e`-Tag für Threading und stellt sicher, dass Antworten über Clients hinweg im richtigen Konversationskontext erscheinen. Leistungsoptimierungen beheben Scroll-Lag in Nachrichtenlisten, ein häufiger Schmerzpunkt beim Laden langer Chat-Verläufe. Entwürfe werden automatisch gespeichert, um Nachrichtenverlust zu verhindern, wenn du mitten in der Komposition wegnavigierst, und Dateispeicheroptionen enthalten jetzt Standard-FileDropServer- und BlossomServer-Endpoints.

### Primal (iOS)

[NIP-46](/de/topics/nip-46/) Remote-Signer-Unterstützung landet auf iOS über [PR #184](https://github.com/PrimalHQ/primal-ios-app/pull/184) und vervollständigt den plattformübergreifenden Rollout, der vor einigen Wochen mit Android begann. Benutzer können jetzt ihre privaten Schlüssel in dedizierten Bunker-Diensten wie nsec.app oder selbst gehosteten nsecBunker-Instanzen aufbewahren und sich über Nostr-Relays verbinden, um Events zu signieren, ohne Schlüssel der Client-App auszusetzen. Diese Trennung verbessert die Sicherheitslage für Benutzer, die Primals Funktionen nutzen möchten, während sie strengere Schlüsselverwaltungspraktiken beibehalten. Die Implementierung enthält QR-Code-Scanning für Bunker-Verbindungs-URIs und übernimmt den NIP-46-Request/Response-Flow über verschlüsselte Relay-Nachrichten.

---

Das war's für diese Woche. Baust du etwas? Hast du Neuigkeiten zu teilen? Möchtest du, dass wir über dein Projekt berichten? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Melde dich per NIP-17 DM</a> oder finde uns auf Nostr.
