---
title: 'Nostr Compass #4'
date: 2026-01-07
publishDate: 2026-01-07
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, deinem wöchentlichen Wegweiser durch das Nostr-Protokoll-Ökosystem.

**Diese Woche:** Primal Android liefert [NIP-46](/de/topics/nip-46/) Remote Signing und [NIP-55](/de/topics/nip-55/) lokale Signer-Unterstützung aus und wird damit zu einem vollwertigen Signing-Hub für andere Android-Apps. Das [Marmot Protocol](/de/topics/marmot/)-Team hat Ergebnisse eines Sicherheitsaudits mit 18 zusammengeführten PRs zur Härtung von [MLS](/de/topics/mls/)-basierter verschlüsselter Kommunikation bearbeitet. Citrine erreicht v1.0 und Applesauce veröffentlicht v5.0 für seine gesamte Bibliothekssuite. TENEX baut KI-Agenten-Überwachung auf Nostr aus, und Jumble fügt intelligentes Relay-Pooling hinzu. Eine NIP-55-Spezifikationskorrektur klärt die `nip44_encrypt`-Rückgabefelder, und ein [NIP-50](/de/topics/nip-50/)-PR schlägt Query-Expression-Erweiterungen für erweiterte Suche vor. In unserem Deep Dive erklären wir [NIP-04](/de/topics/nip-04/) und [NIP-44](/de/topics/nip-44/): warum die Legacy-Verschlüsselung Sicherheitsmängel hat und wie der moderne Ersatz diese behebt.

## Neuigkeiten

**Primal Android wird zum vollständigen Signing-Hub** - [Version 2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) fügt sowohl [NIP-46](/de/topics/nip-46/) Remote Signing als auch [NIP-55](/de/topics/nip-55/) lokales Signing hinzu und macht Primal damit zu einem vollständigen Signer für andere Nostr-Apps. Remote Signing über NIP-46 ermöglicht Nutzern die Verbindung zu Bunker-Diensten über Nostr-Relays, wobei die Schlüssel komplett vom Gerät ferngehalten werden. Lokales Signing über NIP-55 macht Primal als Android Content Provider verfügbar, sodass Apps wie Amethyst oder Citrine Signaturen anfordern können, ohne jemals den privaten Schlüssel zu berühren. [Mehrere Folge-PRs](https://github.com/PrimalHQ/primal-android-app/pull/839) beheben Kompatibilitätsprobleme mit der NIP-55-Spezifikationsanforderung für Hex-Pubkeys und verbessern das Parsen fehlerhafter `nostrconnect://`-URIs. Das Release beinhaltet außerdem Media-Pre-Caching für flüssigeres Scrollen, verbesserte Thread-Ladezeiten und Avatar-Pre-Caching.

**Marmot Protocol härtet Sicherheit nach Audit** - Das [Marmot Development Kit](https://github.com/marmot-protocol/mdk) (mdk), das [NIP-104](/de/topics/nip-104/) MLS-basierte Ende-zu-Ende-verschlüsselte Kommunikation implementiert, erhielt diese Woche umfangreiche Sicherheitskorrekturen. Achtzehn zusammengeführte Pull Requests behoben Audit-Ergebnisse, darunter: [Hash-Verifizierung für verschlüsselte Gruppenbilder](https://github.com/marmot-protocol/mdk/pull/97) zur Verhinderung von Blob-Substitutionsangriffen auf Speicherebene, [Paginierung für ausstehende Willkommensnachrichten](https://github.com/marmot-protocol/mdk/pull/110) zur Verhinderung von Speichererschöpfung, [MLS Group ID-Lecks in Fehlermeldungen](https://github.com/marmot-protocol/mdk/pull/112), und [Base64-Encoding-Durchsetzung](https://github.com/marmot-protocol/mdk/pull/98) für Key Packages. Die [Marmot-Spezifikation selbst wurde aktualisiert](https://github.com/marmot-protocol/marmot/pull/20) mit MIP-04 v2-Versionierung und Sicherheitsverbesserungen. Aktive PRs bearbeiten weiterhin Nonce-Wiederverwendung, Secret-Zeroization und Cache-Pollution-Vektoren.

**Nostrability verfolgt Relay-Hint-Unterstützung** - Ein neuer [Relay-Hints-Kompatibilitätstracker](https://github.com/nostrability/nostrability/issues/270) dokumentiert, wie Clients Relay-Hints im gesamten Ökosystem konstruieren und konsumieren. Der Tracker zeigt, dass die meisten Clients mittlerweile Hints gemäß [NIP-10](/de/topics/nip-10/) und [NIP-19](/de/topics/nip-19/) konstruieren, der Konsum jedoch stark variiert: einige Clients fügen Hints in ausgehende Events ein, nutzen aber eingehende Hints nicht zum Abrufen. Sechs Clients erhielten den "Full"-Tier-Status für vollständige Implementierung. Der Tracker ist nützlich für Entwickler, die Interoperabilität prüfen, und für Nutzer, die sich fragen, warum manche Clients Inhalte finden, die andere nicht finden können.

**Nostria 2.0 liefert plattformübergreifende Feature-Überarbeitung** - Der [Nostria](https://nostria.app)-Client [veröffentlichte Version 2.0](nostr:naddr1qvzqqqr4gupzp5daxvenwv7ucsglpm5f8vuts530cr0zylllgkwejpzvak0x2kqmqqykummnw3exjcfdxgedqf5p) am 30. Dezember mit signifikanten Erweiterungen für iOS (TestFlight), Android (Play Store), Web und Windows. Das Release fügt native Musikunterstützung mit Playlist-Erstellung, Track-Upload, Zap-basierten Künstlerzahlungen und einem WinAmp-ähnlichen Player mit funktionalem Equalizer hinzu. Live-Streaming erhält Game-API-Integration, die während Gameplay-Streams reichhaltige Metadaten anzeigt. Eine neue Zusammenfassungsfunktion generiert stündliche, tägliche oder wöchentliche Aktivitätsdigests als komprimierte Timeline-Ansichten. Der Discover-Bereich bietet kuratierte Listen zum Finden von Inhalten und Profilen. Medienveröffentlichung wird mit automatischer Kurzform-Post-Generierung für Cross-Client-Auffindbarkeit vereinfacht. Remote-Signer-Verbindungen funktionieren jetzt per QR-Code-Scan ohne manuelle Konfiguration. Die Profilerkennung adressiert ein häufiges Nostr-Problem: Wenn Nutzer zwischen Relays wechseln, ohne ihre Metadaten mitzunehmen, findet Nostria ihr Profil und veröffentlicht es erneut auf ihren aktuellen Relays. Premium-Abonnenten erhalten YouTube-Kanal-Integration, private Memos, Analyse-Dashboards und automatische Following-Listen-Backups mit Merge/Restore-Optionen.

## NIP-Updates

Aktuelle Änderungen im [NIPs-Repository](https://github.com/nostr-protocol/nips):

**Zusammengeführt:**
- **[NIP-55](/de/topics/nip-55/)** - Das Rückgabefeld für die `nip44_encrypt`-Methode wurde korrigiert ([#2184](https://github.com/nostr-protocol/nips/pull/2184)). Android-Signer müssen den verschlüsselten Payload jetzt im `signature`-Feld zurückgeben (passend zu `nip44_decrypt`) statt in einem separaten Feld. Dies bringt die Spezifikation mit bestehenden Implementierungen in Amber und Primal in Einklang.

**Offene PRs:**
- **[NIP-50](/de/topics/nip-50/)** - Query Expression Extensions ([#2182](https://github.com/nostr-protocol/nips/pull/2182)) schlägt vor, NIP-50-Suche mit strukturierten Query-Ausdrücken zu erweitern. Der PR fügt Operatoren wie `kind:1`, `author:npub1...` und boolesche Kombinationen (`AND`, `OR`, `NOT`) hinzu, die präzisere Suchabfragen jenseits einfacher Textsuche ermöglichen. Dies würde Clients erlauben, erweiterte Suchoberflächen zu erstellen und dabei Rückwärtskompatibilität mit einfachen Suchstrings zu wahren.

## NIP Deep Dive: NIP-04 und NIP-44

Diese Woche behandeln wir Nostrs Verschlüsselungsstandards: das Legacy-NIP-04, dem du noch begegnen wirst, und seinen modernen Ersatz NIP-44, der kritische Sicherheitsmängel behebt.

### [NIP-04](/de/topics/nip-04/): Verschlüsselte Direktnachrichten (Legacy)

[NIP-04](https://github.com/nostr-protocol/nips/blob/master/04.md) war Nostrs erster Versuch für verschlüsselte Kommunikation unter Verwendung von kind 4 Events. Obwohl einfach zu implementieren, hat es bekannte Sicherheitsschwächen und wurde zugunsten von NIP-44 als veraltet erklärt.

**Wie es funktioniert:** NIP-04 verwendet ECDH (Elliptic Curve Diffie-Hellman), um ein gemeinsames Geheimnis zwischen Sender und Empfänger abzuleiten, und verschlüsselt dann mit AES-256-CBC.

```json
{
  "id": "<event-id>",
  "pubkey": "<sender-pubkey>",
  "created_at": 1736200000,
  "kind": 4,
  "tags": [["p", "<recipient-pubkey>"]],
  "content": "base64-ciphertext?iv=base64-iv",
  "sig": "<signature>"
}
```

Der Verschlüsselungsablauf:
1. Gemeinsamen Punkt berechnen: `shared = ECDH(sender_privkey, recipient_pubkey)`
2. Schlüssel ableiten: `key = SHA256(shared_x_coordinate)`
3. Zufälligen 16-Byte IV generieren
4. Verschlüsseln: `ciphertext = AES-256-CBC(key, iv, plaintext)`
5. Inhalt formatieren: `base64(ciphertext)?iv=base64(iv)`

**Sicherheitsprobleme:**

- **Keine Authentifizierung:** AES-CBC bietet Vertraulichkeit, aber keine Integrität. Ein Angreifer, der ein Relay kontrolliert, könnte Ciphertext-Bits modifizieren und vorhersagbare Änderungen am Klartext verursachen (Bit-Flipping-Angriffe).
- **IV im Klartext:** Der Initialisierungsvektor wird zusammen mit dem Ciphertext übertragen, und CBC-Modus mit vorhersagbaren IVs ermöglicht Chosen-Plaintext-Angriffe.
- **Keine Padding-Validierung:** Implementierungen unterscheiden sich darin, wie sie PKCS#7-Padding handhaben, was Padding-Oracle-Angriffe ermöglichen kann.
- **Metadaten-Exposition:** Der Sender-Pubkey, Empfänger-Pubkey und Zeitstempel sind alle für Relays sichtbar.
- **Schlüsselwiederverwendung:** Das gleiche gemeinsame Geheimnis wird für alle Nachrichten zwischen zwei Parteien verwendet, für immer.

**Warum es noch existiert:** Viele ältere Clients und Relays unterstützen nur NIP-04. Du wirst ihm begegnen, wenn du mit Legacy-Systemen interagierst. Signer wie Amber und Apps wie Primal implementieren weiterhin `nip04_encrypt`/`nip04_decrypt` für Rückwärtskompatibilität.

### [NIP-44](/de/topics/nip-44/): Versionierte Verschlüsselung

[NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md) ist der moderne Verschlüsselungsstandard, der entwickelt wurde, um NIP-04s bekannte Mängel zu beheben. Ein Cure53-Sicherheitsaudit von NIP-44-Implementierungen identifizierte 10 Probleme (einschließlich Timing-Angriffe und Forward-Secrecy-Bedenken), die vor Finalisierung der Spezifikation behoben wurden. Es verwendet ChaCha20-Poly1305 mit korrekter Schlüsselableitung und authentifizierter Verschlüsselung.

**Wesentliche Verbesserungen gegenüber NIP-04:**

| Aspekt            | NIP-04                     | NIP-44                  |
|:------------------|:---------------------------|:------------------------|
| Cipher            | AES-256-CBC                | XChaCha20-Poly1305      |
| Authentifizierung | Keine                      | Poly1305 MAC            |
| Schlüsselableitung | SHA256(shared_x)         | HKDF mit Salt           |
| Nonce             | 16-Byte IV, Muster-Wiederverwendung | 24-Byte zufällige Nonce |
| Padding           | PKCS#7 (Länge sichtbar)   | Auf Zweierpotenz gepaddet |
| Versionierung     | Keine                      | Versions-Byte-Prefix    |

**Verschlüsselungsablauf:**

1. **Conversation Key:** Einen stabilen Schlüssel für jedes Sender-Empfänger-Paar ableiten:
   ```
   shared_x = ECDH(sender_privkey, recipient_pubkey).x
   conversation_key = HKDF-SHA256(
     ikm = shared_x,
     salt = "nip44-v2",
     info = ""
   )
   ```

2. **Message Keys:** Für jede Nachricht eine zufällige 32-Byte-Nonce generieren und Verschlüsselungs-/Authentifizierungsschlüssel ableiten:
   ```
   keys = HKDF-SHA256(
     ikm = conversation_key,
     salt = nonce,
     info = "nip44-v2"
   )
   chacha_key = keys[0:32]
   chacha_nonce = keys[32:44]
   hmac_key = keys[44:76]
   ```

3. **Klartext padden:** Auf die nächste Zweierpotenz auffüllen (Minimum 32 Bytes), um die Nachrichtenlänge zu verbergen:
   ```
   padded = [length_u16_be] + [plaintext] + [zeros to next power of 2]
   ```

4. **Verschlüsseln und authentifizieren:**
   ```
   ciphertext = XChaCha20(chacha_key, chacha_nonce, padded)
   mac = HMAC-SHA256(hmac_key, nonce + ciphertext)
   ```

5. **Payload formatieren:**
   ```
   payload = [version=0x02] + [nonce] + [ciphertext] + [mac]
   content = base64(payload)
   ```

**Versions-Byte:** Das erste Byte (`0x02`) zeigt die Verschlüsselungsversion an. Dies ermöglicht zukünftige Upgrades ohne Beschädigung bestehender Nachrichten. Version `0x01` war ein früherer Entwurf, der nie breit eingesetzt wurde.

**Entschlüsselung:**

1. Base64 dekodieren, Versions-Byte auf `0x02` prüfen
2. Nonce (Bytes 1-32), Ciphertext und MAC (letzte 32 Bytes) extrahieren
3. Conversation Key mit dem privaten Schlüssel des Empfängers und dem öffentlichen Schlüssel des Senders ableiten
4. Message Keys aus Conversation Key und Nonce ableiten
5. MAC vor der Entschlüsselung verifizieren (bei Ungültigkeiten ablehnen)
6. Ciphertext entschlüsseln, Längen-Prefix extrahieren, ungepaddet Klartext zurückgeben

**Sicherheitseigenschaften:**

- **Authentifizierte Verschlüsselung:** Poly1305 MAC stellt sicher, dass jede Manipulation vor der Entschlüsselung erkannt wird
- **Forward Secrecy (partiell):** Jede Nachricht verwendet eine einzigartige Nonce, sodass die Kompromittierung einer Nachricht keine anderen preisgibt. Allerdings offenbart die Kompromittierung eines privaten Schlüssels weiterhin alle vergangenen Nachrichten (kein Ratcheting).
- **Längenverbergung:** Zweierpotenz-Padding verschleiert die exakte Nachrichtenlänge
- **Timing-Angriff-Resistenz:** Konstantzeit-Vergleich für MAC-Verifizierung

**Verwendung in der Praxis:** NIP-44 ist die Verschlüsselungsschicht für:
- [NIP-17](/de/topics/nip-17/) private Direktnachrichten (innerhalb von Gift Wrap)
- [NIP-46](/de/topics/nip-46/) Remote-Signer-Kommunikation
- [NIP-59](/de/topics/nip-59/) Seal-Verschlüsselung
- [Marmot Protocol](/de/topics/nip-104/) Gruppennachrichten, wobei NIP-44 MLS-verschlüsselte Inhalte mit einem vom MLS-Exporter-Secret abgeleiteten Schlüssel umhüllt
- Jede Anwendung, die sichere Punkt-zu-Punkt-Verschlüsselung benötigt

**Migrationsempfehlung:** Neue Anwendungen sollten ausschließlich NIP-44 verwenden. Für Rückwärtskompatibilität prüfe, ob der Client eines Kontakts NIP-44 unterstützt (über [NIP-89](/de/topics/nip-89/) App-Metadaten oder Relay-Unterstützung), bevor auf NIP-04 zurückgefallen wird. Beim Empfangen von Nachrichten versuche zuerst NIP-44-Entschlüsselung, dann falle auf NIP-04 für Legacy-Inhalte zurück.

## Releases

**Primal Android v2.6.18** - Das [vollständige Release](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18) fügt [NIP-46](/de/topics/nip-46/) Remote Signing und [NIP-55](/de/topics/nip-55/) lokales Signing hinzu und macht Primal damit zu einem Signing-Hub für andere Android-Apps. Leistungsverbesserungen umfassen Media-Pre-Caching, Avatar-Pre-Caching und schnelleres Thread-Laden. Bugfixes beheben Selbst-Erwähnungen in Bios, Media-Galerie-Abstürze und Stream-Titel-Fallbacks. Unter iOS verwendet Primal Hintergrund-Audiowiedergabe, um die App für den Empfang von NIP-46-Signaturanfragen aktiv zu halten; Nutzer können den Sound in den Einstellungen ändern oder komplett stummschalten.

**Mostro v0.15.6** - Das [neueste Release](https://github.com/MostroP2P/mostro/releases/tag/v0.15.6) der [NIP-69](/de/topics/nip-69/) P2P-Bitcoin-Trading-Plattform vervollständigt die Entwicklungsfonds-Implementierung mit Phase 4 Audit-Events. Dev-Fee-Zahlungen werden jetzt über kind 38383 Nostr-Events verfolgt, die nach jeder erfolgreichen Zahlung veröffentlicht werden, was Drittpartei-Verifizierung und Analysen ermöglicht. Betragsberechnungen wurden für Käufer/Verkäufer-Nachrichten korrigiert, und die Premium-Logik wurde mit der lnp2pbot-Referenzimplementierung abgeglichen.

**Aegis v0.3.5** - Der plattformübergreifende Signer [fügt Dark Mode hinzu](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.5), verbesserte App-Icon-Anzeige und sauberere UI-Layouts. Bugfixes beheben iOS iCloud Private Relay-Konflikte und Event-Parsing-Probleme. Das Release verbessert auch, wie Event-JSON an die Rust-Signing-Funktion übergeben wird.

**Citrine v1.0.0** - Die Android-Relay-App [erreicht 1.0](https://github.com/greenart7c3/Citrine/releases/tag/v1.0.0). Citrine ermöglicht den Betrieb eines persönlichen Nostr-Relays direkt auf deinem Android-Gerät, nützlich für lokales Caching, Backup oder als NIP-55-Begleiter. Dieses Release fügt einen Crash-Report-Handler hinzu, verbessert die Effizienz von Datenbankabfragen und aktualisiert Übersetzungen via Crowdin.

**Applesauce v5.0.0** - hzrd149s TypeScript-Bibliothekssuite [liefert eine Major-Version](https://github.com/hzrd149/applesauce/releases) mit Breaking Changes, die auf Korrektheit und Einfachheit fokussiert sind. Das Core-Paket [verifiziert jetzt Event-Signaturen standardmäßig](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.0.0) und benennt Koordinaten-Methoden um, um klarere "Address"-Terminologie zu verwenden (`parseCoordinate` -> `parseReplaceableAddress`). Das Relay-Paket [senkt Standard-Retries von 10 auf 3](https://github.com/hzrd149/applesauce/releases/tag/applesauce-relay%405.0.0) und ignoriert standardmäßig nicht erreichbare Relays, plus fügt `createUnifiedEventLoader` für einfacheres Event-Fetching hinzu. Das Wallet-Paket erhält [NIP-87](/de/topics/nip-87/) [Cashu Mint Discovery](https://github.com/hzrd149/applesauce/releases/tag/applesauce-wallet%405.0.0). Direkte `nostr-tools`-Abhängigkeiten wurden paketübergreifend entfernt, was Bundle-Größe und Versionskonflikte reduziert.

## Bemerkenswerte Code- und Dokumentationsänderungen

*Dies sind offene Pull Requests und Arbeiten im Frühstadium, perfekt um Feedback zu erhalten, bevor sie zusammengeführt werden. Wenn dir etwas ins Auge fällt, erwäge einen Review oder Kommentar!*

### Damus (iOS)

Eine Serie von PRs verbessert das Langform-Artikel-Erlebnis. [Lese-UX-Verbesserungen](https://github.com/damus-io/damus/pull/3496) fügen einen Fortschrittsbalken, geschätzte Lesezeit, Sepia-Modus, einstellbare Zeilenhöhe und Fokus-Modus hinzu, der die Navigation beim Scrollen versteckt. [Bild-Korrekturen](https://github.com/damus-io/damus/pull/3489) stellen sicher, dass Bilder in Markdown-Inhalten mit korrekten Seitenverhältnissen angezeigt werden, indem einzelne Bilder als Block-Level-Elemente vorverarbeitet werden. [Langform-Vorschaukarten](https://github.com/damus-io/damus/pull/3497) ersetzen Inline-`@naddr1...`-Text durch reichhaltige Vorschaukarten, die Artikeltitel und Metadaten zeigen. Eine neue [Relay-Integrationstestsuite](https://github.com/damus-io/damus/pull/3508) fügt 137 netzwerkbezogene Tests hinzu, einschließlich [NIP-01](/de/topics/nip-01/)-Protokollverifizierung und Verhalten unter verschlechterten Netzwerkbedingungen (3G-Simulation).

### Bitchat (Verschlüsselte Kommunikation)

Sicherheitshärtung im iOS Nostr+Cashu-Messenger. [Noise Protocol DH Secret Clearing](https://github.com/permissionlesstech/bitchat/pull/928) behebt sechs Stellen, an denen gemeinsame Geheimnisse nach Diffie-Hellman Key Agreement nicht gelöscht wurden, und stellt Forward-Secrecy-Garantien wieder her. [Thread-Sicherheit für Lesebestätigungs-Queues](https://github.com/permissionlesstech/bitchat/pull/929) fügt Barrier-Synchronisation hinzu, um Race Conditions in NostrTransport zu verhindern. [Nachrichten-Deduplikator-Optimierung](https://github.com/permissionlesstech/bitchat/pull/920) verbessert die Leistung bei hohem Nachrichtenvolumen, und [Hex-String-Parsing-Härtung](https://github.com/permissionlesstech/bitchat/pull/919) verhindert Abstürze durch fehlerhafte Eingaben.

### Frostr (Threshold Signing)

Das [FROST](/de/topics/frost/)-basierte Threshold-Signing-Protokoll [fügt QR-Code-Anzeige hinzu](https://github.com/FROSTR-ORG/igloo-desktop/pull/62) für Gruppen-Anmeldedaten und Share-Anmeldedaten während des Onboardings und in der Signer-Oberfläche. Dies ermöglicht eine einfachere Einrichtung beim Verteilen von Schlüsselanteilen über mehrere Geräte, da Nutzer Anmeldedaten scannen können, anstatt lange Zeichenketten manuell zu kopieren.

### Marmot mdk (Bibliothek)

Über die oben erwähnten Sicherheitskorrekturen hinaus adressieren aktive PRs verbleibende Audit-Ergebnisse: [Secret<T>-Typ für Zeroization](https://github.com/marmot-protocol/mdk/pull/109) führt einen Wrapper-Typ ein, der sensible Daten beim Drop automatisch löscht, [Nachrichten-Abfrage-Paginierung](https://github.com/marmot-protocol/mdk/pull/111) verhindert Speichererschöpfung beim Laden des Chat-Verlaufs, und [verschlüsselter Speicher](https://github.com/marmot-protocol/mdk/pull/102) fügt Ruheverschlüsselung für die SQLite-Datenbank hinzu, die Gruppenstatus und Nachrichten speichert.

### Amethyst (Android)

Eine arbeitsreiche Woche mit Stabilitätskorrekturen im Android-Client. [Nachsichtiges JSON-Parsing](https://github.com/vitorpamplona/amethyst/commit/2c42796) verhindert Abstürze durch fehlerhafte Events, indem Kotlin Serialization nachgiebiger gemacht wird. Event-Validierung [prüft jetzt die Kind-Feldgröße](https://github.com/vitorpamplona/amethyst/commit/40f9622) vor der Verarbeitung, um Exceptions durch übergroße Werte zu vermeiden. Die Trust-Score-UI bekam ein kleineres Icon, um visuelle Störungen zu reduzieren, und [verbessertes Fehler-Logging](https://github.com/vitorpamplona/amethyst/commit/69c53ac) hilft bei der Diagnose von Relay-Verbindungsproblemen. Übersetzungsaktualisierungen kamen via Crowdin, und mehrere SonarQube-Warnungen wurden behoben.

### TENEX (KI-Agenten)

Das Nostr-native KI-Agenten-Framework sah 81 Commits diese Woche, die autonome Fähigkeiten ausbauen. Ein neues [Agenten-Überwachungssystem](https://github.com/tenex-chat/tenex/pull/48) implementiert Verhaltensheuristiken zur Überwachung von Agentenaktionen und zum Eingreifen bei Bedarf. [Delegationstransparenz](https://github.com/tenex-chat/tenex/commit/b244c10) fügt Benutzerinterventions-Logging zu Delegationstranskripten hinzu, damit Nutzer überprüfen können, was Agenten in ihrem Namen getan haben. Die [LLM-Provider-Registry](https://github.com/tenex-chat/tenex/pull/47) wurde modularisiert für einfachere Integration verschiedener KI-Backends. Projektübergreifende Konversationsunterstützung ermöglicht es Agenten, Kontext über mehrere Nostr-basierte Projekte hinweg zu bewahren.

### Jumble (Web-Client)

Der Relay-fokussierte Web-Client fügt mehrere User-Experience-Verbesserungen hinzu. [Intelligenter Relay-Pool](https://github.com/CodyTseng/jumble/commit/695f2fe) verwaltet Verbindungen intelligent basierend auf Nutzungsmustern. [Live-Feed-Toggle](https://github.com/CodyTseng/jumble/commit/917fcd9) lässt Nutzer zwischen Echtzeit-Streaming und manueller Aktualisierung wechseln. [Automatische Anzeige neuer Notizen](https://github.com/CodyTseng/jumble/commit/d1b3a8c) oben bringt frische Inhalte an die Oberfläche, ohne Seitenneuladen zu erfordern. [Persistenter Cache](https://github.com/CodyTseng/jumble/commit/fd9f41c) für Following-Feed und Benachrichtigungen verbessert Ladezeiten bei Rückkehrbesuchen. Nutzer können jetzt [Standard-Relays ändern](https://github.com/CodyTseng/jumble/commit/53a67d8) über die Einstellungen.

---

Das wars für diese Woche. Baust du etwas? Hast du Neuigkeiten zu teilen? Möchtest du, dass wir über dein Projekt berichten? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Kontaktiere uns per NIP-17 DM</a> oder finde uns auf Nostr.
