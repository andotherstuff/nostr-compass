---
title: 'Nostr Compass #22'
date: 2026-05-13
publishDate: 2026-05-13
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-13-newsletter.md
translationDate: 2026-05-13
description: 'Nostr VPN liefert acht Releases in einer Woche, gipfelnd in v4.0.10, von einem neu gestalteten Geräte-Pairing-Flow über einen BoringSSL-AEAD-Tausch, der den TCP-Durchsatz verdoppelt, bis hin zu sendmmsg-Batching und einem vollständigen Geräte-Pairing-UX-Überarbeitung; Marmot Protocol (White Noise) liefert ein Frontend-Release, das das Benutzer-Blockierungsfeature abschließt, und 31 fusionierte PRs über MDK und Backend; Grain v0.6.0 fügt NIP-40, NIP-50, NIP-70 und NIP-45 in einem Meilenstein hinzu; Citrine v3.0.0-pre1 bringt eingebauten Tor und Relay-Aggregation; Amber v6.1.0-pre2 verbessert den neuen App-Verbindungsflow; Alby Hub v1.22.2 fügt eine KI- und Agents-Seite sowie Core-Lightning-Unterstützung hinzu; Mostro liefert gleichzeitige Taker-Bonds und v0.11.0 von mostro-core; Jumble liefert fünf Releases von v26.5.2 bis v26.5.6 mit Benachrichtigungs-Gruppierung, Suche-zuletzt und Account-Daten-Persistenz; Nostrord liefert v1.0.0 bis v1.0.2 mit Gruppen-Share-Modals und Arch-Linux-Paketen; Flotilla 1.8.0 fügt Videoanrufe, E-Mail-Rendering und Raum-Erwähnungen hinzu; Calendar by Formstr v1.5.1 liefert Terminplanung und Android-Kalendersync; Tamagostrich startet ein dezentralisiertes NIP-78-Tamagotchi mit Sats-Belohnungen über NIP-47; NIP-Diskussionen zeigen Reservierungen, Treuhandservices, Unterkunftslisten, Onchain-Zaps und verifizierbare Community-Regeln. Zwei NIP-Tieftauchgänge behandeln NIP-78 (App-spezifische Daten) und NIP-98 (HTTP-Auth).'
---

Willkommen zurück bei Nostr Compass, Ihrem wöchentlichen Leitfaden zur Nostr-Protokollentwicklung.

**Diese Woche:** [Nostr VPN](https://github.com/mmalmi/nostr-vpn) liefert [acht Releases in sieben Tagen](#nostr-vpn-liefert-acht-releases-gipfelnd-in-v4010) von einem neu gestalteten Geräte-Pairing-Flow über einen FIPS-AEAD-Tausch, der den TCP-Durchsatz ungefähr verdoppelt. [Marmot Protocol](https://github.com/marmot-protocol) (die Grundlage für [White Noise](https://github.com/marmot-protocol/whitenoise)) liefert ein [Frontend-Release, das das Benutzer-Blockierungsfeature abschließt](#marmot-white-noise-liefert-blockierungskomplettes-frontend-und-31-fusionierte-prs-über-mdk-und-backend), und 31 fusionierte PRs über MDK und Backend. [Grain](https://github.com/0ceanSlim/grain) liefert [v0.6.0](#grain-v060-fügt-nip-40-nip-50-nip-70-und-nip-45-hinzu) mit vier neuen NIP-Implementierungen in einem Meilenstein. [Citrine](https://github.com/greenart7c3/Citrine) liefert [v3.0.0-pre1](#citrine-v300-pre1-bringt-eingebauten-tor-und-relay-aggregation) mit eingebautem Tor und Relay-Aggregation. [Amber](https://github.com/greenart7c3/Amber) liefert [v6.1.0-pre2](#amber-v610-pre2-verbessert-neuen-app-verbindungsflow) mit Verbindungsflow- und Signierungsverbesserungen. [Alby Hub](https://github.com/getAlby/hub) liefert [v1.22.2](#alby-hub-v1222-fügt-ki-und-agents-seite-und-core-lightning-unterstützung-hinzu) mit einer KI- und Agents-Seite und Core-Lightning-Integration. [Mostro](https://github.com/MostroP2P/mostro) liefert gleichzeitige Taker-Bonds und [mostro-core v0.11.0](#mostro-liefert-gleichzeitige-taker-bonds-und-mostro-core-v0110). [Jumble](https://github.com/CodyTseng/jumble) liefert [fünf Releases](#jumble-liefert-fünf-releases-mit-zuletzt-gesucht-und-account-persistenz) mit Suchverlauf und Account-Daten-Persistenz-Fixes. [Nostrord](https://github.com/nostrord/nostrord) liefert [drei Releases](#nostrord-liefert-gruppen-share-modals-medien-upload-und-arch-linux-pakete) mit Gruppen-Share-Modals und Arch-Linux-Paketen. [Flotilla](https://flotilla.social) liefert [1.8.0](#flotilla-180-liefert-videoanrufe-e-mail-rendering-und-raum-erwähnungen) mit Videoanrufen, E-Mail-Rendering und Raum-Erwähnungen. [Calendar by Formstr](https://calendar.formstr.app) liefert [v1.5.1](#calendar-by-formstr-liefert-v151-mit-terminplanung-und-android-kalendersync) mit Terminplanung und Android-Kalendersync. [Tamagostrich](https://github.com/Negr087/tamagostrich) [startet ein dezentralisiertes NIP-78-Tamagotchi mit Sats-Belohnungen](#tamagostrich-startet-ein-dezentralisiertes-nip-78-tamagotchi-mit-sats-belohnungen).

## Top-Geschichten

### Nostr VPN liefert acht Releases, gipfelnd in v4.0.10

[Nostr VPN](https://github.com/mmalmi/nostr-vpn), das Rust-basierte dezentralisierte Mesh-VPN, das Nostr für Peer-Discovery und ein FIPS-gestütztes Noise-Protokoll für die Datenebene verwendet, lieferte acht Releases von [v4.0.1](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.1) bis [v4.0.10](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.10) über macOS, Linux, Windows und Android diese Woche.

Die Hauptänderung ist in [v4.0.8](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.8): Das AEAD wurde vom RustCrypto-`chacha20poly1305`-Soft-Backend auf BoringSSLs ChaCha20-Poly1305 in `ring` 0.17 getauscht, das hand-abgestimmtes NEON auf aarch64 und AVX2/AVX-512 auf x86_64 verwendet. Docker-Benchmarks auf identischer Hardware zeigten, dass der 2-Node-Direkt-TCP-Durchsatz von 437 auf 1097 Mbps sprang. Das Drahtformat ist unverändert.

Früher in der Woche baute [v4.0.1](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.1) den Geräte-Pairing-Flow mit Exit-Node-Leckschutz, einem einheitlichen WireGuard-Konfigurationsblock unter Exit-Nodes und signierten/notarisierten macOS-Artefakten neu. [v4.0.9](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.0.9) fügte `sendmmsg(2)`-Batching auf dem UDP-Sendepfad hinzu, amortisierte Pro-Paket-`sendto`-Syscalls über 8-Paket-Batches und schob TCP Single-Stream von 1066 auf 1548 Mbps (1,45×).

### Marmot / White Noise liefert blockierungskomplettes Frontend und 31 fusionierte PRs über MDK und Backend

[White Noise](https://github.com/marmot-protocol/whitenoise), die private Gruppen-Messaging-App, die auf dem [Marmot](/de/topics/marmot/)-MLS-basierten Protokoll aufgebaut ist, lieferte [v2026.5.7+24](https://github.com/marmot-protocol/whitenoise/releases/tag/v2026.5.7+24) am 7. Mai als das Frontend-Release, das das Blockierungsfeature-Set abschließt. Das vorherige Release lieferte Stummschalten, Suche und Archivierung; dieses vollendet die Blockierung. Ein blockierter Benutzer ist jetzt aus Einladungen, Chat-Vorschauen, Nachrichtenzeitlinien, Suchergebnissen und Benachrichtigungen ausgeblendet, und seine Nachrichten zählen nicht mehr zu ungelesenen Abzeichen. Video-Anhänge funktionieren Ende-zu-Ende über Geräte hinweg.

Die unterstützende Arbeit umfasst 31 fusionierte PRs über MDK und das Backend. MDK landete [PR #258](https://github.com/marmot-protocol/mdk/pull/258) mit dem Extension-v3-Drahtformat und `disappearing_message_secs`-Schema, was die Grundlage für verschwindende Nachrichten legt.

### Grain v0.6.0 fügt NIP-40, NIP-50, NIP-70 und NIP-45 hinzu

[Grain](https://github.com/0ceanSlim/grain), die Go-basierte Nostr-Relay- und Client-Bibliothek, lieferte [v0.6.0](https://github.com/0ceanSlim/grain/releases/tag/v0.6.0) am 6. Mai mit vier neuen NIP-Implementierungen und einem Produktionshärtungs-Pass. Der v0.6-Meilenstein fügt [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md)-Event-Ablauf, [NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md)-Volltextsuche, [NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md)-geschützte Events und [NIP-45](https://github.com/nostr-protocol/nips/blob/master/45.md)-Event-Zählungen hinzu.

Event-Ablauf über NIP-40 lässt Publisher einen Ablaufzeitstempel setzen, damit der Relay Events nach ihrem Ablauf verwirft, in der Praxis für ephemere Präsenz-Events und zeitlich begrenzte Ankündigungen verwendet. NIP-50-Volltextsuche lässt Clients `search`-Filter in REQ-Nachrichten ausgeben und den Relay die Abgleicharbeit machen. Geschützte Events über NIP-70 verhindern, dass Relays Events ohne die ausdrückliche Erlaubnis des Autors weitergeben. NIP-45-Zählabfragen lassen Clients einen Relay fragen, eine Anzahl übereinstimmender Events zurückzugeben.

## Lieferungen dieser Woche

### Citrine v3.0.0-pre1 bringt eingebauten Tor und Relay-Aggregation

[Citrine](https://github.com/greenart7c3/Citrine), die Android-App, die ein Telefon in einen Nostr-Relay-Knoten verwandelt, lieferte [v3.0.0-pre1](https://github.com/greenart7c3/Citrine/releases/tag/v3.0.0-pre1) als Pre-Release diese Woche. Die Hauptzusätze sind eingebaute Tor-Unterstützung für datenschutzerhaltenden Relay-Zugang und Relay-Aggregation, bei der Citrine Events von mehreren Upstream-Relays abrufen und lokalen Clients bereitstellen kann. [PR #139](https://github.com/greenart7c3/Citrine/pull/139) fügt [NIP-77 (Negentropy-Abgleich)](/de/topics/nip-77/)-Unterstützung für effizienten set-reconciliation-basierten Event-Sync hinzu.

### Amber v6.1.0-pre2 verbessert neuen App-Verbindungsflow

[Amber](https://github.com/greenart7c3/Amber), die Android-Signer-App für [NIP-55 (Android Signer Application)](/de/topics/nip-55/) und [NIP-46](/de/topics/nip-46/), lieferte [v6.1.0-pre2](https://github.com/greenart7c3/Amber/releases/tag/v6.1.0-pre2). Die Hauptfixes: Der Signer-Dialog schließt sich jetzt korrekt nach dem Akzeptieren einer Bunker-Anfrage, fehlerhafte Bunker-Anfragen zeigen einen Invalid-Request-Bildschirm, und Rate-Limiting wird für intentbasierte Signieranfragen hinzugefügt.

### Alby Hub v1.22.2 fügt KI- und Agents-Seite und Core-Lightning-Unterstützung hinzu

[Alby Hub](https://github.com/getAlby/hub), der selbstverwahrende Lightning-Knoten und Nostr-Wallet-Connect-Server, lieferte [v1.22.2](https://github.com/getAlby/hub/releases/tag/v1.22.2) mit mehreren wichtigen Zusätzen. Die neue KI- und Agents-Seite legt Alby Hubs Lightning- und NWC-Fähigkeiten für KI-Agents und MCP-kompatible Tools frei. Das meistgewünschte Feature seit dem Launch wurde geliefert: Core Lightning (CLN) ist jetzt ein unterstütztes Backend neben LND und LDK.

### Mostro liefert gleichzeitige Taker-Bonds und mostro-core v0.11.0

[Mostro](https://github.com/MostroP2P/mostro), das Peer-to-Peer-Bitcoin-Handelsprotokoll auf Nostr, fusionierte 11 PRs diese Woche und advance das Taker-Bond-Feature, das Griefing verhindert, indem beide Parteien Mittel sperren müssen, bevor ein Handel fortschreitet. [PR #733](https://github.com/MostroP2P/mostro/pull/733) implementiert gleichzeitige Taker-Bonds, bei denen mehrere Taker gleichzeitig Bond-Rechnungen einreichen können und der erste, der sperrt, gewinnt.

[mostro-core](https://github.com/MostroP2P/mostro-core) lieferte [v0.11.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.11.0) mit den passenden Bibliothekszusätzen, und [mostro-cli](https://github.com/MostroP2P/mostro-cli) lieferte [v0.15.0](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.15.0).

### Jumble liefert fünf Releases mit Zuletzt-Gesucht und Account-Persistenz

[Jumble](https://github.com/CodyTseng/jumble), der relay-zentrische Nostr-Client als Web-App und Electron-Desktop-App, lieferte fünf Releases diese Woche: [v26.5.2](https://github.com/CodyTseng/jumble/releases/tag/v26.5.2) bis [v26.5.6](https://github.com/CodyTseng/jumble/releases/tag/v26.5.6). [v26.5.5](https://github.com/CodyTseng/jumble/releases/tag/v26.5.5) fügt Suche-zuletzt-Verlauf hinzu. Ein kritischer Persistenz-Bug ist in [v26.5.6](https://github.com/CodyTseng/jumble/releases/tag/v26.5.6) behoben: Accounts und gecachte Daten überleben jetzt einen vollständigen App-Neustart.

### Nostrord liefert Gruppen-Share-Modals, Medien-Upload und Arch-Linux-Pakete

[Nostrord](https://github.com/nostrord/nostrord), ein Nostr-Client für NIP-29-relay-basierte Gruppen, lieferte [v1.0.0](https://github.com/nostrord/nostrord/releases/tag/v1.0.0), [v1.0.1](https://github.com/nostrord/nostrord/releases/tag/v1.0.1) und [v1.0.2](https://github.com/nostrord/nostrord/releases/tag/v1.0.2) diese Woche. [v1.0.1](https://github.com/nostrord/nostrord/releases/tag/v1.0.1) liefert Arch-Linux-Pakete über AUR als `nostrord-bin` mit PGP-signierten `.pkg.tar.zst`-Artefakten, und [v1.0.2](https://github.com/nostrord/nostrord/releases/tag/v1.0.2) fügt Gruppen-Sharing über [PR #49](https://github.com/nostrord/nostrord/pull/49) mit einem Share-Modal hinzu, das sowohl einen `nostr:naddr`-URI als auch einen webfreundlichen `nostrord.com/open/`-Link generiert.

### FIPS v0.3.0 liefert plattformübergreifende Reichweite, Nostr-Peer-Discovery und ein Gateway für unmodifizierte LANs

[FIPS](https://github.com/jmcorgan/fips) (Free Internetworking Peering System), das Nostr-native Mesh-Netzwerk-Projekt, lieferte [v0.3.0](https://github.com/jmcorgan/fips/releases/tag/v0.3.0) diese Woche als wichtigen Meilenstein, der das Projekt von Linux-only auf Linux, macOS, Windows und OpenWrt erweitert. Der Hauptzusatz ist Nostr-vermittelte Peer-Discovery mit STUN-unterstützter UDP-NAT-Traversal. Knoten veröffentlichen jetzt signierte Overlay-Adverts als kind:37195-parametrisierte ersetzbare Events auf öffentlichen Nostr-Relays.

### Flotilla 1.8.0 liefert Videoanrufe, E-Mail-Rendering und Raum-Erwähnungen

[Flotilla](https://flotilla.social), die [NIP-29](/de/topics/nip-29/)-relay-basierte Gruppen-Chat-App von hodlbod, lieferte [1.8.0](https://gitea.coracle.social/coracle/flotilla/src/tag/1.8.0) diese Woche mit mehreren bemerkenswerten Zusätzen. Sprach-Räume unterstützen jetzt Video: Teilnehmer können Kameras einschalten oder ihren Bildschirm während eines Anrufs teilen. E-Mail-Rendering kommt über ein Update der welshman-Bibliothek: Flotilla kann jetzt Nachrichten empfangen, die eingebettete HTML-E-Mail-Inhalte enthalten, und rendert das HTML inline.

### Calendar by Formstr liefert v1.5.1 mit Terminplanung und Android-Kalendersync

[Calendar by Formstr](https://calendar.formstr.app), eine Nostr-native Kalender-App, lieferte [v1.5.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.5.0) am 10. Mai und [v1.5.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.5.1) am 11. Mai. Terminplanung kommt in [PR #89](https://github.com/formstr-hq/nostr-calendar/pull/89), das Benutzern erlaubt, buchbare Zeitfenster in ihrem Kalender zu erstellen. Schreibgeschützte Android-Kalender-Integration in [PR #123](https://github.com/formstr-hq/nostr-calendar/pull/123) synchronisiert Nostr-Events mit dem Gerätekalender.

## In Entwicklung

### Amethyst fügt geplante Beiträge, NIP-9A-Community-Regeln und ein Desktop-Local-Relay hinzu

[Amethyst](https://github.com/vitorpamplona/amethyst), der funktionsreiche Android-Client, fusionierte 78 PRs diese Woche über mehrere wichtige Feature-Bereiche. Geplante Beiträge landen auf Android in [PR #2765](https://github.com/vitorpamplona/amethyst/pull/2765): Benutzer können eine Notiz verfassen und eine zukünftige Veröffentlichungszeit setzen. Ein Desktop-Build erhält ein eingebettetes lokales Relay mit SQLite-Event-Persistenz in [PR #2841](https://github.com/vitorpamplona/amethyst/pull/2841).

### Shopstr fügt MCP-Audit-Protokollierung und Sitzungssicherheit hinzu

[Shopstr](https://github.com/shopstr-eng/shopstr), der dezentralisierte Marktplatz auf Nostr, fusionierte fünf PRs diese Woche. Audit-Protokollierung für die MCP-Tool-Schicht landet in [PR #456](https://github.com/shopstr-eng/shopstr/pull/456), und Sitzungssicherheit wird in [PR #477](https://github.com/shopstr-eng/shopstr/pull/477) verschärft.

### Dart NDK fügt Web-Unterstützung und Seal-Signatur-Verifizierung hinzu

[Dart NDK](https://github.com/relaystr/dart_ndk), die Dart-Bibliothek für Nostr-Protokollentwicklung, fusionierte sechs PRs diese Woche. Web-Unterstützung kommt in `SembastCacheManager` über [PR #571](https://github.com/relaystr/dart_ndk/pull/571), und Seal-Signatur-Verifizierung landet in [PR #595](https://github.com/relaystr/dart_ndk/pull/595) für den [NIP-59 (Gift Wrap)](/de/topics/nip-59/)-Flow.

## Neue Projekte

### Tamagostrich startet ein dezentralisiertes NIP-78-Tamagotchi mit Sats-Belohnungen

[Tamagostrich](https://github.com/Negr087/tamagostrich) ist ein browser-basiertes virtuelles Haustierspiel, das beim IDENTITY Hackathon 2026 gestartet wurde, bei dem ein Baby-Strauß, Nori, sich durch deine Nostr-Social-Aktivität entwickelt. Der Haustierstatus lebt in einem [NIP-78](/de/topics/nip-78/)-kind:30078-Event, damit er über jedes Gerät synchronisiert wird, das dasselbe Schlüsselpaar teilt. Meilenstein-Belohnungen zahlen automatisch in Sats über [NIP-47 (Nostr Wallet Connect)](/de/topics/nip-47/) aus: 50 Sats auf Level 5, 210 Sats auf Level 10 und 420 Sats auf dem maximalen Level 21.

## Protokoll- und Spezifikationsarbeit

Das NIPs-Repository fusionierte [PR #2338](https://github.com/nostr-protocol/nips/pull/2338), das README-Referenzlinks für Marmot-Event-Kinds und den Geocaching-Kind 37516 behebt. Fünf neue Vorschläge wurden diese Woche eröffnet:

[PR #2331](https://github.com/nostr-protocol/nips/pull/2331) schlägt **NIP-9A: Verifizierbare Community-Regeln** vor, das kind:34551 einführt, ein parametrisiertes ersetzbares Event, das einem Community-Eigentümer erlaubt, ein maschinenlesbares, kryptografisch signiertes Regelwerk zu veröffentlichen.

[PR #2335](https://github.com/nostr-protocol/nips/pull/2335) schlägt **Reservierungs-Events für Nostr-Marktplätze** vor, das kind:32122 (parametrisierte ersetzbare Reservierungs-Events), kind:1326 (Append-only-Übergangs-Audit-Records) und kind:32124 (Post-Trade-Bewertungen) definiert.

[PR #2334](https://github.com/nostr-protocol/nips/pull/2334) schlägt **Treuhandservices für Nostr-Marktplätze** vor, das kind:30303 für Treuhandoperatoren verwendet, um ihre EVM-Vertragsadresse und Gebührenplan zu deklarieren.

[PR #2333](https://github.com/nostr-protocol/nips/pull/2333) schlägt **Unterkunftslisten-Profile für NIP-99-Marktplatz-Listings** vor, das NIP-99-klassifizierte Listings mit H3-Geospatial-Index-`g`-Tags erweitert.

[PR #2332](https://github.com/nostr-protocol/nips/pull/2332) schlägt **NIP-BC: Onchain-Zaps (kind 8333)** vor, das eine direkte Identität zwischen Nostr-Schlüsseln und Bitcoin-Taproot-Adressen ausnutzt: Ein Nostr-Pubkey ist ein 32-Byte-x-only-secp256k1-Schlüssel, und so ist auch ein BIP-341-P2TR-interner Schlüssel.

## NIP-Tieftauchgang: NIP-78 (App-spezifische Daten)

[NIP-78](/de/topics/nip-78/) definiert eine Standardmethode für Anwendungen, beliebige private oder öffentliche Daten im Namen eines Benutzers über Nostr-Events zu speichern. Der zentrale Event-Kind ist 30078, ein parametrisiertes ersetzbares Event, bei dem der `d`-Tag eine anwendungsdefinierte Bezeichner-Zeichenfolge ist.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1747180800,
  "kind": 30078,
  "tags": [
    ["d", "tamagostrich-pet-state"]
  ],
  "content": "{\"level\":7,\"xp\":1420,\"happiness\":82,\"energy\":61}",
  "sig": "<128-char hex>"
}
```

Die primäre Motivation ist die geräteübergreifende Synchronisation ohne zentralen Server. Jeder Client, der den öffentlichen Schlüssel eines Benutzers und den `d`-Tag der Anwendung kennt, kann den aktuellen Zustand aus dem Relay-Set des Benutzers abrufen. Für private Anwendungsdaten können NIP-78-Events den Inhaltsbereich mit [NIP-44 (Versionierte Verschlüsselung)](/de/topics/nip-44/) oder dem älteren [NIP-04](/de/topics/nip-04/) verschlüsseln.

---

**Primäre Quellen:**
- [NIP-78-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/78.md)
- [Tamagostrich](https://github.com/Negr087/tamagostrich): Produktionsimplementierung diese Woche

**Siehe auch:**
- [NIP-51: Listen](/de/topics/nip-51/)
- [NIP-65: Relay-Listen-Metadaten](/de/topics/nip-65/)

## NIP-Tieftauchgang: NIP-98 (HTTP-Auth)

[NIP-98](/de/topics/nip-98/) definiert ein HTTP-Authentifizierungsschema, das Nostr-Schlüsselpaaren erlaubt, Anfragen an HTTP-Server zu autorisieren, ohne Benutzernamen, Passwörter oder OAuth-Token zu benötigen. Ein Client erstellt ein kurzlebiges Nostr-Event von kind 27235, signiert es mit seinem privaten Schlüssel, base64-kodiert das JSON und sendet es in einem `Authorization: Nostr <base64>`-HTTP-Header.

```json
{
  "id": "<64-char hex>",
  "pubkey": "<64-char hex>",
  "created_at": 1747180800,
  "kind": 27235,
  "tags": [
    ["u", "https://files.example.com/upload"],
    ["method", "POST"],
    ["payload", "<sha256-hash-of-request-body>"]
  ],
  "content": "",
  "sig": "<128-char hex>"
}
```

Das Kind-27235-Event enthält die HTTP-Methode in einem `method`-Tag, die vollständige Anfrage-URL in einem `u`-Tag und einen `created_at`-Zeitstempel. Der Server validiert die Signatur, prüft, dass die Methode und URL mit der tatsächlichen Anfrage übereinstimmen, und verifiziert, dass der Zeitstempel aktuell ist (innerhalb weniger Minuten), um Replay-Angriffe zu verhindern.

NIP-98 wird in Blossom ([BUD-01](https://github.com/hzrd149/blossom/blob/master/buds/01.md)) zur Authentifizierung von Blob-Uploads und -Downloads verwendet. Routstr verwendet es für HTTP-API-Zugriffskontrolle auf Pro-Anfrage-Basis. Sprout verwendet es für Git-Transport-Auth und REST-Relay-Zugang.

---

**Primäre Quellen:**
- [NIP-98-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/98.md)
- [BUD-01: Blossom-Upload-Auth](https://github.com/hzrd149/blossom/blob/master/buds/01.md)

**Siehe auch:**
- [NIP-96: HTTP-Dateispeicher-Integration](/de/topics/nip-96/)

---

Das war es für diese Woche. Wenn du etwas baust oder Neuigkeiten zu teilen hast, sende uns eine DM auf Nostr oder finde uns auf [nostrcompass.org](https://nostrcompass.org).
