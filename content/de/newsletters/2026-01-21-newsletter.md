---
title: 'Nostr Compass #6'
date: 2026-01-21
publishDate: 2026-01-21
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, deinem wöchentlichen Ratgeber zu Nostr.

**Diese Woche:** Bitchat ersetzt C Tor durch die Rust Arti-Implementierung für bessere Zuverlässigkeit und Leistung. nostrdb-rs erhält Streaming-Fold-Abfragen, die Null-Allokations-Datenbankoperationen ermöglichen. Listr wird mit NDK 3 Beta-Migration und KI-gestützter Wartung nach einem Jahr Stillstand grundlegend überarbeitet. Zeus integriert 17 zusammengeführte PRs mit Fokus auf [NIP-47](/de/topics/nip-47/) (Nostr Wallet Connect für Remote Lightning Control) Verbesserungen und Cashu-Updates, während Primal Android Wallet-Backup-Flows und [NIP-92](/de/topics/nip-92/) (Media-Dimensionen für korrekte Seitenverhältnisse) Unterstützung hinzufügt. Ein neuer Entwurf-NIP schlägt [Trusted Relay Assertions](/de/topics/trusted-relay-assertions/) für standardisierte Relay-Vertrauensbewertung vor.

## Nachrichten

### Bitchat wechselt zu Rust Arti für Tor-Unterstützung

Bitchat ist von C Tor zu [Arti](https://gitlab.torproject.org/tpo/core/arti), der Rust-Implementierung des Tor-Protokolls, migriert. [PR #958](https://github.com/permissionlesstech/bitchat/pull/958) entfernt die C Tor-Abhängigkeit und integriert Arti, was Memory-Safety-Garantien und verbesserte Zuverlässigkeit mit sich bringt. Die Änderung behebt das Problem, dass ruhende Wake-Versuche Vordergrund-Service-Neustarts verursachten – ein langjähriges Problem der C-Implementierung.

**Was das für Nutzer bedeutet:** Stabilere verschlüsselte Messaging mit weniger Abbrüchen, besonders auf mobilen Geräten. Die Rust-Implementierung reduziert Absturzrisiken und Batterieverbrauch durch ständige Wiederverbindungsversuche.

Arti ist eine komplette Neuentwicklung von Tor in Rust durch das Tor Project, um bessere Sicherheit durch Memory Safety und einfachere Integration in Anwendungen zu bieten. Für Bitchat reduzieren die Memory-Safety-Eigenschaften die Angriffsfläche beim Umgang mit verschlüsselten Nachrichten und Relay-Verbindungen. Die Migration folgt der kürzlichen [Cure53-Sicherheitsaudit](/de/newsletters/2026-01-13-newsletter/#bitchat-completes-cure53-security-audit) des Teams (behandelt in Newsletter #5) und setzt ihre Sicherheitsverbesserungen fort.

Der PR führt auch umfassende Testabdeckung für ChatViewModel und BLEService ein, entfernt ungenutzten Code und stabilisiert die Test-Suite. Bluetooth Low Energy Mesh-Zuverlässigkeitsverbesserungen begleiten die Tor-Änderungen und beheben Probleme mit großen Datenübertragungen. Zusammen verbessern diese Änderungen Bitchats Widerstandsfähigkeit für Offline-Mesh-Netzwerk-Szenarien, in denen Tor Internetverbindung zusammen mit lokaler BLE-Kommunikation bereitstellt.


### Listr mit KI-gestützter Wartung erneuert

JeffG kündigte eine große Überarbeitung von [Listr](https://github.com/erskingardner/listr), der Nostr-Listenverwaltungsanwendung unter [listr.lol](https://listr.lol) verfügbar, nach mehr als einem Jahr Stillstand des Projekts an. Mit KI-Unterstützung führte er ein umfassendes Upgrade durch, einschließlich Migration zu [NDK](https://github.com/nostr-dev-kit/ndk) 3 Beta, Updates auf die neuesten Versionen von Svelte und Vite und alle Abhängigkeiten aktualisiert. Die Überarbeitung bietet erstklassige Unterstützung für Folge-Pakete, implementiert Pagination für Listen mit über 50 Elementen und behebt zahlreiche Fehler, die sich während der Stillstandszeit angesammelt hatten.

**Was das für Nutzer bedeutet:** Listr ist wieder online mit verbesserter Leistung und neuen Funktionen zur Verwaltung von Folgelisten, Inhaltssammlungen und Topic-Kurationen. Die Pagination-Verbesserung macht große Listen tatsächlich nutzbar.

JeffG bemerkte, dass diese Wartungsarbeit ohne KI-Unterstützung wahrscheinlich nie hätte stattfinden können und das Projekt vor dem Verlassensein bewahrt. Listr ermöglicht Inhalts-Kurationen auf Nostr und erlaubt Nutzern, Listen von Profilen, Topics und Ressourcen zu erstellen, zu verwalten und zu teilen. Das Upgrade hält die Anwendung kompatibel mit aktuellen Nostr-Standards und Client-Erwartungen, da Listenverwaltung zentraler für Content-Discovery im Protokoll wird.


## NIP-Updates

Aktuelle Änderungen im [NIPs Repository](https://github.com/nostr-protocol/nips):

**Zusammengeführt:**

- **[NIP-29](/de/topics/nip-29/)** (Relay-basierte Gruppen) - Relay-Schlüssel-Klarstellung ([#2190](https://github.com/nostr-protocol/nips/pull/2190) - zusammengeführt) stellt klar, dass der Relay-Schlüssel die Relay-URL selbst ist, nicht ein pubkey. Die Spec erklärt nun explizit "Der Relay-Schlüssel ist die WebSocket-URL des Relays (z.B. wss://groups.example.com)", um Verwechslungen zu vermeiden. Dies beeinflusst, wie Clients identifizieren, welcher Relay eine bestimmte Gruppe hostet und stellt sicher, dass Gruppen ordnungsgemäß ihren Hosting-Relays zugeordnet werden.

**Offene PRs und Diskussionen:**

- **Trusted Relay Assertions** - Ein Entwurf-NIP schlägt die Standardisierung der Relay-Vertrauensbewertung durch kind 30385 Events mit Vertrauenswerten (0-100) vor, berechnet aus [NIP-66](/de/topics/nip-66/) (Relay-Entdeckung und Überwachung) Metriken, Betreiber-Reputation und Nutzerberichten. Die Spezifikation unterteilt Vertrauen in Zuverlässigkeit (Verfügbarkeit, Latenz), Qualität (TLS, Dokumentation, Betreiber-Verifizierung) und Zugänglichkeit (Gerichtsbarkeit, Barrieren, Überwachungsrisiko) Komponenten. Die Betreiber-Verifizierung umfasst kryptografische Signaturen über [NIP-11](/de/topics/nip-11/) (Relay-Informationsdokumente), DNS TXT-Einträge und .well-known Dateien. Nutzer deklarieren vertraute Assertion-Provider über kind 10385 Events, was Clients ermöglicht, mehrere Provider für unterschiedliche Perspektiven abzufragen. Der Vorschlag ergänzt [NIP-66](/de/topics/nip-66/) Entdeckung mit Bewertung und hilft [NIP-46](/de/topics/nip-46/) (Remote-Signierung/Nostr Connect) bei der Beurteilung der Relay-Vertrauenswürdigkeit in Verbindungs-URIs.

- **Post-Quanten-Kryptografie** - [PR #2185](https://github.com/nostr-protocol/nips/pull/2185) (offen) entwickelt sich weiter, seit [Newsletter #5](/de/newsletters/2026-01-13-newsletter/#nip-updates) den Vorschlag für quantenresistente Algorithmen einführte. Die Diskussion dieser Woche konzentrierte sich auf Implementierungsdetails für Krypto-Agilität: wie Clients duale Signaturen während der Migration handhaben, Rückwärtskompatibilität für ältere Clients und Leistungsauswirkungen größerer quantenresistenter Signaturen. Beitragende debattierten, ob nur ML-DSA-44 vorgeschrieben werden soll oder mehrere Algorithmen (ML-DSA-44, Falcon-512, Dilithium) für Flexibilität unterstützt werden sollen. Der Konsens neigt zu einem schrittweisen Ansatz: optionale Quantensignaturen zunächst, die erst nach breiter Client-Unterstützung und dem Auftreten echter Quantenbedrohungen obligatorisch werden.


## NIP Deep Dive: NIP-11 und NIP-66

Diese Woche untersuchen wir zwei NIPs, die zusammenarbeiten, um Relay-Entdeckung und -Bewertung zu ermöglichen: NIP-11 definiert, wie Relays sich selbst beschreiben, und NIP-66 standardisiert, wie wir Relay-Verhalten messen. Zusammen bilden sie die Grundlage für Relay-Vertrauensbewertungssysteme.

### [NIP-11](/de/topics/nip-11/): Relay-Informationsdokument

[NIP-11](https://github.com/nostr-protocol/nips/blob/master/11.md) definiert ein JSON-Dokument, das Relays über HTTP bereitstellen, um ihre Fähigkeiten, Richtlinien und Betreiberinformationen zu beschreiben. Wenn ein Client sich mit `wss://relay.example.com` verbindet, kann er `https://relay.example.com` abrufen (ersetze `wss://` durch `https://`), um das Informationsdokument des Relays zu erhalten.

Das Dokument verwendet Standard-HTTP-Content-Negotiation mit dem `Accept: application/nostr+json` Header. Dies ermöglicht es Relays, ihre normale Website an Browser zu liefern und gleichzeitig maschinenlesbare Metadaten an Nostr-Clients bereitzustellen. Die Antwort enthält den Namen und die Version der Relay-Software, Kontaktinformationen des Betreibers (pubkey, E-Mail, alternativer Kontakt), unterstützte NIPs und operative Parameter wie Zahlungsanforderungen oder Inhaltsbeschränkungen.

Wichtig ist, dass grundlegende NIP-11-Dokumente unsigniertes JSON sind, das über HTTPS bereitgestellt wird und sich ausschließlich auf TLS-Zertifikate für die Authentizität verlässt. Das bedeutet, dass jeder, der den Webserver des Relays kontrolliert, das Dokument modifizieren kann, wodurch Betreiberbehauptungen nicht verifizierbar sind. Der Trusted Relay Assertions-Vorschlag schließt diese Lücke, indem er signierte Attestierungen durch das `self` pubkey-Feld eines Relays einführt und kryptografische Beweise für die Betreiberidentität ermöglicht, ähnlich wie Relays signierte Events für Authentifizierungsmechanismen verwenden.

```json
{
  "name": "relay.example.com",
  "description": "Ein allgemeines öffentliches Relay",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "contact": "admin@example.com",
  "supported_nips": [1, 2, 4, 9, 11, 12, 16, 20, 22],
  "software": "git+https://github.com/relay/relay.git",
  "version": "1.2.3",
  "limitation": {
    "max_message_length": 16384,
    "max_subscriptions": 20,
    "max_filters": 100,
    "max_limit": 5000,
    "max_subid_length": 100,
    "min_prefix": 4,
    "max_event_tags": 2000,
    "max_content_length": 8196,
    "min_pow_difficulty": 0,
    "auth_required": false,
    "payment_required": false
  },
  "payments_url": "https://relay.example.com/payments",
  "fees": {
    "admission": [{"amount": 5000, "unit": "msats"}],
    "subscription": [{"amount": 1000, "unit": "msats", "period": 2592000}],
    "publication": []
  }
}
```

Das `limitation`-Objekt teilt Clients mit, welche Einschränkungen das Relay durchsetzt. `max_message_length` begrenzt die WebSocket-Frame-Größe, `max_subscriptions` begrenzt gleichzeitige REQ-Abonnements pro Verbindung, `max_filters` begrenzt Filter pro REQ, und `max_limit` beschränkt, wie viele Events ein einzelner Filter anfordern kann. Diese Parameter helfen Clients, ihr Verhalten an die Relay-Fähigkeiten anzupassen und Verbindungsabbrüche durch Überschreitung von Limits zu vermeiden.

Zahlungsinformationen erscheinen in `fees` und `payments_url`. Relays können für Zutritt (einmaliger Zugriff), Abonnement (wiederkehrender Zugriff) oder Publikation (pro Event-Gebühren) Gebühren erheben. Die `payments_url` verweist auf Details zu Zahlungsmethoden, typischerweise Lightning-Rechnungen oder Ecash-Mints. Kostenpflichtige Relays verwenden diese Felder, um Preise zu kommunizieren, bevor Clients eine Authentifizierung versuchen.

Das `supported_nips`-Array ermöglicht es Clients, Relay-Fähigkeiten zu entdecken. Wenn ein Relay [NIP-50](/de/topics/nip-50/) auflistet, wissen Clients, dass sie Volltextsuche-Anfragen senden können. Wenn [NIP-42](/de/topics/nip-42/) erscheint, sollten Clients Authentifizierungs-Herausforderungen erwarten. Diese deklarative Fähigkeits-Werbung ermöglicht progressive Verbesserung: Clients können erweiterte Funktionen nutzen, wo sie verfügbar sind, während sie auf Relays mit begrenzter Unterstützung elegant degradieren.

Betreiberinformationen schaffen Verantwortlichkeit. Das `pubkey`-Feld identifiziert den Relay-Betreiber auf Nostr und ermöglicht direkte Kommunikation über [NIP-17](/de/topics/nip-17/) DMs oder öffentliche Erwähnungen. Die `contact`-E-Mail bietet eine Off-Protocol-Fallback-Option. Zusammen helfen diese Felder Nutzern, Betreiber für Missbrauchsmeldungen, Zugriffsanfragen oder technische Probleme zu erreichen.

[NIP-11](/de/topics/nip-11/)-Dokumente sind selbstberichtet: Relays beschreiben, was sie behaupten zu unterstützen, nicht unbedingt, was sie tatsächlich tun. Hier wird NIP-66 wichtig.

### [NIP-66](/de/topics/nip-66/): Relay-Entdeckung und Lebendüberwachung

[NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) standardisiert die Veröffentlichung von Relay-Überwachungsdaten auf Nostr. Überwachungsdienste testen kontinuierlich Relays auf Verfügbarkeit, Latenz, Protokollkonformität und unterstützte NIPs. Sie veröffentlichen Ergebnisse als kind 30166 Events und bieten Echtzeit-Relay-Status unabhängig von Relay-Selbstberichten.

Monitore prüfen die Relay-Verfügbarkeit, indem sie sich verbinden und Test-Abonnements senden. Latenzmessungen verfolgen Verbindungszeit, Abonnement-Antwortzeit und Event-Verbreitungsverzögerung. Protokollkonformitätstests verifizieren, dass das Relay-Verhalten den Spezifikationen entspricht, und erfassen Implementierungsfehler oder absichtliche Abweichungen. Die NIP-Unterstützungsverifizierung geht über [NIP-11](/de/topics/nip-11/)-Behauptungen hinaus, indem tatsächlich getestet wird, ob beworbene Funktionen korrekt funktionieren.

```json
{
  "id": "a34b5c7d89e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7",
  "pubkey": "4e2d0bc6f8e7c3a5b9f1d2e3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4",
  "created_at": 1736784000,
  "kind": 30166,
  "tags": [
    ["d", "wss://relay.example.com"],
    ["rtt", "open", "143", "1736784000"],
    ["rtt", "read", "89", "1736784000"],
    ["rtt", "write", "92", "1736784000"],
    ["nips", "1", "2", "4", "9", "11", "12"],
    ["geo", "US", "United States", "New York"],
    ["other", "network", "clearnet"],
    ["other", "payment_required", "false"],
    ["other", "auth_required", "false"]
  ],
  "content": "{\"last_check\": 1736784000, \"checks\": 8760}",
  "sig": "8b9c4d5e6a7f8b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b"
}
```

Das `d`-Tag enthält die Relay-URL, was dies zu einem parametrisierten ersetzbaren Event macht. Jeder Monitor veröffentlicht ein Event pro Relay, das aktualisiert wird, wenn sich Messungen ändern. Mehrere Monitore können dasselbe Relay verfolgen und bieten Redundanz und Kreuzvalidierung. Clients fragen mehrere Monitor-Pubkeys ab, um verschiedene Perspektiven zur Relay-Gesundheit zu erhalten.

Round-Trip-Time (rtt) Tags messen die Latenz für verschiedene Operationen. `rtt open` verfolgt die WebSocket-Verbindungserstellung, `rtt read` misst die Abonnement-Antwortzeit und `rtt write` testet die Event-Veröffentlichungsgeschwindigkeit. Alle Werte sind in Millisekunden. Clients verwenden diese Metriken, um Relays mit niedriger Latenz für zeitkritische Operationen zu bevorzugen oder langsame Relays zu deprioritisieren.

Das `nips`-Tag listet tatsächlich verifizierte NIP-Unterstützung auf, nicht nur behauptete Unterstützung. Monitore testen jeden NIP, indem sie seine Funktionalität ausüben. Wenn ein Relay [NIP-50](/de/topics/nip-50/) Suche in seinem [NIP-11](/de/topics/nip-11/) Dokument behauptet, aber Suchabfragen fehlschlagen, werden Monitore NIP-50 aus der verifizierten Liste weglassen. Dies liefert Grundwahrheit über Relay-Fähigkeiten.

Geografische Informationen helfen Clients, nahegelegene Relays für bessere Latenz und Zensurresistenz auszuwählen. Das `geo`-Tag enthält Ländercode, Ländername und Region. Das `network`-Tag unterscheidet Clearnet-Relays von Tor Hidden Services oder I2P-Endpunkten. Zusammen ermöglichen diese Tags geografische Vielfalt: Clients können sich mit Relays in mehreren Gerichtsbarkeiten verbinden, um regionaler Zensur zu widerstehen.

Monitordaten treiben Relay-Selektoren in Clients, Explorer-Websites und den Trusted Relay Assertions-Vorschlag an. Durch die Kombination von selbstberichteten [NIP-11](/de/topics/nip-11/) Dokumenten mit gemessenen [NIP-66](/de/topics/nip-66/) Daten und berechneten Vertrauensbehauptungen bewegt sich das Ökosystem in Richtung informierter Relay-Auswahl, anstatt sich auf hartcodierte Standards oder Mundpropaganda-Empfehlungen zu verlassen.

## Releases

### 0xchat v1.5.3 - Erweiterte Messaging-Funktionen

[0xchat v1.5.3](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.3-release) bringt bedeutende Verbesserungen für den Telegram-ähnlichen Nostr-Messaging-Client. Die Version behebt [NIP-55](/de/topics/nip-55/) (Android-Signer-Anwendung) Compliance-Probleme, die eine ordnungsgemäße Event-Signierung über externe Signer wie Amber verhinderten. Vollständige Compliance bedeutet, dass 0xchat jetzt korrekt Signieroperationen delegiert und die Sicherheit verbessert, indem private Schlüssel isoliert bleiben.

Das Update integriert sowohl FileDropServer als auch BlossomServer als Standard-Medienspeicheroptionen und gibt Nutzern Redundanz für Datei-Uploads. [Blossom](https://github.com/hzrd149/blossom) bietet inhaltsadressierte Speicherung, bei der Dateien durch ihre SHA-256-Hashes referenziert werden, was Integrität sicherstellt und Deduplizierung im Netzwerk ermöglicht. Automatisches Entwurf-Speichern für Moments verhindert Datenverlust beim Verfassen von Langform-Inhalten und behebt Nutzerbeschwerden über verlorene Posts während App-Wechseln oder Verbindungsunterbrechungen.

Die Cashu-Wallet-Integration erhält Politur mit automatischer Proof-Filterung, die ausgegebene Token aus der Wallet-Ansicht entfernt. Dies löst die verwirrende UX, bei der Nutzer ungültige Proofs neben gültigem Ecash sahen, was Bilanzberechnungen unzuverlässig machte. Die Filterung erfolgt clientseitig und bewahrt die Privatsphäre, während sie die Zahlungserfahrung für Peer-to-Peer-Transaktionen innerhalb von Chats verbessert.

### Amber v4.1.0 Pre-releases - UI-Überholung

[Amber v4.1.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.0-pre1) bis [v4.1.0-pre3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.0-pre3) führen eine neu gestaltete Oberfläche für den beliebten Android-Event-Signer ein. Der Login-Bildschirm zeigt jetzt deutlich an, welche Anwendung Signaturberechtigungen anfordert, und behebt Nutzerverwirrung über Autorisierungs-Flows. Der neue Events-Bildschirm bietet detaillierte Inspektion der Daten, die Anwendungen signieren möchten, sodass Nutzer informierte Sicherheitsentscheidungen treffen können, bevor sie Operationen genehmigen.

Das Berechtigungsmanagement erhält erhebliche Aufmerksamkeit mit einer überarbeiteten Oberfläche, die genau zeigt, welche Fähigkeiten jeder verbundenen Anwendung gewährt wurden. Nutzer können spezifische Berechtigungen widerrufen, ohne die Verbindung vollständig zu trennen, was eine feinkörnige Kontrolle über die Signierdelegation ermöglicht. Die überarbeiteten Relay-Zähler mit der aktualisierten Quartz-Bibliothek bieten Echtzeit-Statistiken über Event-Durchsatz und Relay-Leistung. [NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md) (Nostr Connect) Bunker-Verbindungen zeigen jetzt detaillierte Fehlermeldungen an, wenn Verbindungen fehlschlagen, und ersetzen kryptische Timeout-Fehler durch verwertbare Diagnosen.

## Bemerkenswerte Code- und Dokumentationsänderungen

*Dies sind zusammengeführte Pull Requests und frühphasige Entwicklungen, die es wert sind, verfolgt zu werden. Einige sind experimentelle Funktionen, die sich vor der Veröffentlichung noch entwickeln könnten.*

### Zeus (Lightning Wallet mit Nostr Wallet Connect)

Zeus führte diese Woche 17 Pull Requests zusammen und stärkt seine Position als führende [NIP-47](/de/topics/nip-47/) Nostr Wallet Connect-Implementierung. Die bedeutendsten Fixes beheben Datenkonsistenz- und Protokollkonformitätsprobleme, die Interoperabilitätsprobleme mit Nostr-Clients verursachten.

**Transaktionsverlauf-Fix** - [PR #3542](https://github.com/ZeusLN/zeus/pull/3542) behebt einen kritischen Fehler, bei dem NWC-Transaktionslisten falsche oder doppelte Einträge anzeigten. Das Problem trat auf, wenn Zeus Transaktionsdaten zwischenspeicherte, ohne Event-Updates ordnungsgemäß zu handhaben, was dazu führte, dass Nutzer Phantom-Transaktionen oder fehlende Zahlungen sahen. Der Fix implementiert ordnungsgemäße Event-Deduplizierung und Cache-Invalidierung, um sicherzustellen, dass der Transaktionsverlauf den Lightning-Node-Status genau widerspiegelt.

**Protokollkonformität** - [PR #3548](https://github.com/ZeusLN/zeus/pull/3548) behebt unvollständige `getInfo`-Antworten, die die Kompatibilität mit Clients brachen, die vollständige NIP-47-Konformität erwarteten. Einige Nostr-Clients stürzten ab, wenn sie partielle Antworten erhielten, denen Felder wie `block_height` oder `network` fehlten. Der PR stellt sicher, dass alle erforderlichen Felder mit sinnvollen Standardwerten zurückgegeben werden, auch wenn die zugrundeliegende Lightning-Implementierung sie nicht bereitstellt, was Zeus' Kompatibilität im gesamten Ökosystem verbessert.

**Verbindungsresilienz** - [PR #3543](https://github.com/ZeusLN/zeus/pull/3543) implementiert Timeout-Benachrichtigungen für ins Stocken geratene Nostr-Verbindungen. Zuvor warteten Nutzer unbegrenzt, wenn Relay-Verbindungen stillschweigend abbrachen. Jetzt zeigt Zeus klare Timeout-Nachrichten nach 30 Sekunden Inaktivität an, sodass Nutzer erneut versuchen oder Relays wechseln können. [PR #3541](https://github.com/ZeusLN/zeus/pull/3541) fügt Backend-Validierung hinzu, um NWC-Aktivierung auf inkompatiblen Lightning-Implementierungen zu verhindern und Konfigurationsfehler zu erfassen, bevor sie Laufzeitabstürze verursachen.

**Cashu Race Condition** - [PR #3531](https://github.com/ZeusLN/zeus/pull/3531) behebt einen Concurrency-Fehler in der Cashu-Token-Verwaltung, bei dem gleichzeitige Mint-Operationen die Token-Datenbank beschädigen konnten. Die Race Condition trat auf, wenn mehrere Threads Token-Zählungen ohne ordnungsgemäße Sperrung aktualisierten, was gelegentlich zu falschen Salden führte. Der Fix fügt Mutex-Schutz um kritische Abschnitte hinzu und stellt atomare Updates des Token-Status sicher.

### Primal Android (Client)

Primal Android lieferte 12 zusammengeführte PRs mit bedeutenden Verbesserungen bei Wallet-Sicherheit und Medienbehandlung. Die Wallet-Backup-Implementierung adressiert eine der meist angeforderten Funktionen, während NIP-92-Unterstützung die visuelle Erfahrung in der gesamten Anwendung verbessert.

**Wallet-Backup-System** - Eine vier-PR-Serie ([#844](https://github.com/PrimalHQ/primal-android-app/pull/844), [#845](https://github.com/PrimalHQ/primal-android-app/pull/845), [#846](https://github.com/PrimalHQ/primal-android-app/pull/846), [#848](https://github.com/PrimalHQ/primal-android-app/pull/848)) implementiert umfassende Seed-Phrase-Backup-Funktionalität. Nutzer können jetzt ihr 12-Wort-Mnemonic über einen sicheren Flow exportieren, der Screenshots verhindert, den Backup-Status im Wallet-Dashboard anzeigt und bestehende Nutzer durch die Migration führt. Die Implementierung folgt BIP-39-Standards und beinhaltet Validierung, um zu verhindern, dass Nutzer Gelder durch falsche Phrasenaufzeichnung verlieren.

**Mediendimensionen (NIP-92)** - [PR #718](https://github.com/PrimalHQ/primal-android-app/pull/718) implementiert [NIP-92](/de/topics/nip-92/) Unterstützung für korrekte Bild- und Video-Seitenverhältnisse. Ohne Dimensionsmetadaten müssen Clients Bilder herunterladen, um ihre Größe zu bestimmen, was zu Layout-Sprüngen führt, wenn Inhalte geladen werden. NIP-92 fügt `dim`-Tags (wie `["dim", "1920x1080"]`) zu Datei-Metadaten-Events hinzu, sodass Primal korrekten Platz vor dem Herunterladen von Medien reservieren kann. Dies eliminiert störende Reflows in Bildgalerien und verbessert die wahrgenommene Leistung.

**Remote-Signer-Zuverlässigkeit** - [PR #841](https://github.com/PrimalHQ/primal-android-app/pull/841) behebt [NIP-46](/de/topics/nip-46/) Verbindungsprobleme, bei denen fehlende `wss://`-Präfixe stille Fehler verursachten. Der PR validiert Relay-URIs während des Bunker-Verbindungsaufbaus und fügt das Protokoll-Präfix automatisch hinzu, wenn Nutzer bloße Domains einfügen. [PR #843](https://github.com/PrimalHQ/primal-android-app/pull/843) behebt einen Threading-Fehler, bei dem schlechte Netzwerkbedingungen dazu führten, dass Antworten als Root-Notes gepostet wurden und den Gesprächsfluss unterbrachen. Der Fix stellt sicher, dass Parent-Event-IDs durch Netzwerkunterbrechungen bestehen bleiben.

### Marmot Protocol: White Noise (Verschlüsselte Gruppenchat-Bibliothek)

White Noise, die Rust-Bibliothek, die [Marmot](/de/topics/marmot/) Protocols verschlüsselte Gruppenchats antreibt, führte sechs PRs zusammen, die Nutzererfahrung und Sicherheit verbessern. Die Änderungen bringen Marmot näher an Feature-Parität mit Mainstream-Messaging-Anwendungen, während sie ihre Privacy-First-Architektur beibehalten.

**Lesebestätigungen** - [PR #433](https://github.com/marmot-protocol/whitenoise-rs/pull/433) und [#436](https://github.com/marmot-protocol/whitenoise-rs/pull/436) implementieren Nachrichten-Leseverfolgung für Gruppenkonversationen. Das System speichert Lesepositionen pro Nutzer pro Gruppe innerhalb eines einzelnen Geräts und ermöglicht Ungelesen-Zähler-Badges. Die Implementierung verwendet monotone Zeitstempel, um die Position der zuletzt gelesenen Nachricht für jede Konversation zu verfolgen. Diese grundlegende Funktion ermöglicht UI-Indikatoren, die ungelesene Nachrichtenzahlen pro Konversation anzeigen.

**Konversations-Pinning** - [PR #442](https://github.com/marmot-protocol/whitenoise-rs/pull/442) fügt persistentes Konversations-Pinning durch ein `pin_order`-Feld in der `accounts_groups`-Junction-Tabelle hinzu, die Konten mit Gruppen verknüpft. Gepinnte Konversationen behalten ihre Position oben in Chat-Listen bei, unabhängig von Nachrichtenaktivität, was den Nutzererwartungen von Signal und WhatsApp entspricht. Die Implementierung verwendet Integer-Sortierung, um unbegrenzte Pins mit deterministischer Sortierung zu ermöglichen.

**Deterministische Commit-Auflösung (MIP-03)** - [PR #152](https://github.com/marmot-protocol/mdk/pull/152) (offen) implementiert Marmot Improvement Proposal 03 und löst das kritische Problem von Commit-Race-Conditions in verteilten Gruppenchats. Wenn mehrere Mitglieder gleichzeitig Gruppenstatusänderungen (Hinzufügen/Entfernen von Mitgliedern, Ändern von Berechtigungen) einreichen, könnten Clients bei der Commit-Reihenfolge divergieren und die Gruppe in inkompatible Zustände fragmentieren. MIP-03 führt Epochen-Snapshots und eine deterministische Gewinner-Auswahl ein: Der Commit mit dem frühesten `created_at`-Zeitstempel gewinnt, mit lexikografischer Event-ID als Tie-Breaker. Dies ermöglicht es allen Clients, durch Rollback und Replay auf denselben Zustand zu konvergieren und die Gruppenkohärenz auch während Netzwerkpartitionen aufrechtzuerhalten.

**Sicherheitshärtung** - [PR #443](https://github.com/marmot-protocol/whitenoise-rs/pull/443) verhindert unnötiges Kopieren kryptografischer Geheimnisse durch die Verwendung von Referenzen in `resolve_group_image_path`. Dies reduziert das Zeitfenster für Speicherangriffe, bei denen Geheimnisse aus freigegebenen Heap-Allokationen wiederhergestellt werden könnten. [PR #438](https://github.com/marmot-protocol/whitenoise-rs/pull/438) aktiviert SQLCipher-Datenbankverschlüsselung durch Keyring-Parameter und schützt die Nachrichtenhistorie im Ruhezustand. Die Keyring-Integration ermöglicht sichere Schlüsselspeicherung in Plattform-Keychains anstatt in Konfigurationsdateien.

### nostrdb-rs (Datenbankbibliothek) - Offener PR

**Streaming-Abfragen-Implementierung** - [PR #58](https://github.com/damus-io/nostrdb-rs/pull/58) (offen) schlägt Streaming-Fold-Abfragen vor, um Null-Allokations-Datenbankoperationen zu ermöglichen. Die Implementierung fügt `fold`, `try_fold`, `count`, `any`, `all` und `find_map` Methoden hinzu, die Datenbankergebnisse einzeln verarbeiten würden, ohne ganze Ergebnismengen in Vektoren zu materialisieren. Dieser Ansatz würde den Speicherverbrauch reduzieren und frühzeitige Beendigung für gängige Abfragemuster ermöglichen.

Die technische Implementierung exponiert Low-Level-Abfrageergebnis-Callbacks (`ndb_query_visit`) als zustandsbehaftete Rust-Visitors, die `ControlFlow`-Varianten auf C-Visitor-Aktionen abbilden. Nach der Zusammenführung wird Anwendungscode wie Iterator-Logik lesen, während er nahe an der Datenbankschicht läuft. Zum Beispiel würde das Zählen passender Notizen durch Ergebnisse streamen, anstatt sie zu sammeln, und `find_map` würde das erste nützliche Ergebnis zurückgeben, ohne verbleibende Zeilen zu verarbeiten.

nostrdb betreibt Damus und Notedeck, beide iOS/macOS bzw. Desktop-Clients. Die Streaming-Abfragen würden effiziente Muster wie Paginierung, bedingte Filterung und Existenzprüfungen ermöglichen. Der PR ändert 3 Dateien mit +756 Hinzufügungen und -32 Löschungen, eine substantielle Umgestaltung der Abfrageschicht. Nutzer von nostrdb-rs-basierten Anwendungen würden reduzierten Speicherverbrauch beim Durchsuchen großer Timelines oder beim Durchsuchen umfangreicher Event-Datenbanken sehen.

### nak (CLI-Tool)

nak, fiatjafs Kommandozeilen-Nostr-Tool, führte sechs PRs zusammen, die sich auf Build-System-Verbesserungen und neue Funktionalität konzentrieren. [PR #91](https://github.com/fiatjaf/nak/pull/91) implementiert eine Blossom-Mirror-Funktion, die es nak ermöglicht, als Mirror für Blossom-Medienserver zu dienen. [Blossom](/de/topics/blossom/) ist ein inhaltsadressiertes Medienspeicherprotokoll, das neben Nostr-Events funktioniert.

Die verbleibenden PRs behandeln Build-System-Kompatibilität über Windows-, macOS- und Linux-Plattformen und ermöglichen FUSE-Dateisystem-Unterstützung für das Mounten von Nostr-Events als lokale Verzeichnisse.

### Damus (iOS-Client) - Offene PRs

Damus hat 11 offene PRs, die bedeutende architektonische Verbesserungen erforschen. Obwohl diese noch nicht zusammengeführt wurden, signalisieren sie wichtige Richtungen für die iOS-Nostr-Client-Entwicklung, insbesondere in Bezug auf Privatsphäre, Synchronisationseffizienz und mobile Datenoptimierung.

**Tor-Integration** - [PR #3535](https://github.com/damus-io/damus/pull/3535) bettet den Arti Tor-Client direkt in Damus ein und ermöglicht anonyme Relay-Verbindungen ohne externe Abhängigkeiten. Im Gegensatz zu Orbot- oder Tor-Browser-Ansätzen bietet das Einbetten von Arti nahtlose Integration mit iOS-Sandboxing und Hintergrundausführungslimits. Die Rust-Implementierung bringt Memory Safety zur Netzwerkanonymisierung und reduziert die Angriffsfläche im Vergleich zu C Tor. Nutzer könnten den Tor-Modus pro-Relay oder global umschalten, wobei der Client das Circuit-Management transparent handhabt.

**Negentropy-Sync-Protokoll** - [PR #3536](https://github.com/damus-io/damus/pull/3536) implementiert Negentropy, ein Set-Reconciliation-Protokoll, das die Synchronisationseffizienz radikal verbessert. Anstatt alle Events seit der letzten Verbindung herunterzuladen, tauscht Negentropy kompakte Fingerabdrücke (Merkle-Bäume) aus, um genau zu identifizieren, welche Events zwischen Client und Relay unterschiedlich sind. Für Nutzer, die Hunderten von Pubkeys folgen, reduziert dies die Sync-Bandbreite von Megabytes auf Kilobytes. Die Implementierung integriert sich mit RelayPool und SubscriptionManager und ermöglicht automatische effiziente Synchronisation über alle verbundenen Relays.

**Low-Data-Modus** - [PR #3549](https://github.com/damus-io/damus/pull/3549) fügt Funktionen zur Mobilfunk-Dateneinsparung hinzu, die auf Nutzerfeedback über Bandbreitenverbrauch reagieren. Der Modus deaktiviert automatisches Bildladen, Video-Prefetching und reduziert Abonnement-Limits. Nutzer mit getakteten Verbindungen können Textinhalte durchsuchen, ohne Angst vor Überschreitung von Datenobergrenzen zu haben. Die Implementierung respektiert iOS-Low-Data-Modus-Einstellungen und bietet granulare Kontrollen für verschiedene Medientypen.

**Datenbankoptimierungen** - [PR #3548](https://github.com/damus-io/damus/pull/3548) überarbeitet nostrdb-Snapshot-Speicherung für schnellere Abfragen und reduzierten Speicherplatzbedarf. Die Optimierung ändert, wie Datenbank-Snapshots auf Disk persistiert werden, und verbessert sowohl die Leseleistung als auch die Schreibverstärkung. Dies behebt Beschwerden über Batterieentleerung von Nutzern mit großen Event-Datenbanken.

---

Das war's für diese Woche. Baust du etwas? Hast du Neuigkeiten zu teilen? Möchtest du, dass wir über dein Projekt berichten? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Kontaktiere uns über NIP-17 DM</a> oder finde uns auf Nostr.