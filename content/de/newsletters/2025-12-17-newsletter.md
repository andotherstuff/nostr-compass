---
title: 'Nostr Compass #1'
date: 2025-12-17
publishDate: 2025-12-15
draft: false
type: newsletters
translationOf: /en/newsletters/2025-12-17-newsletter.md
translationDate: 2025-12-26
---

Willkommen bei Nostr Compass, einem wöchentlichen Newsletter, der dem Nostr-Protokoll-Ökosystem gewidmet ist. Unsere Mission ist es, Entwickler, Relay-Betreiber und Builder über wichtige Entwicklungen im gesamten Netzwerk auf dem Laufenden zu halten. Wir dokumentieren die Protokollevolution mit technischer Genauigkeit, Neutralität und Tiefe und decken alles ab, von NIP-Vorschlägen über Client-Releases bis hin zu Best Practices für die Implementierung.

Nostr Compass ist inspiriert von [Bitcoin Optech](https://bitcoinops.org/), dessen jahrelange engagierte Arbeit zur Förderung des technischen Bitcoin-Wissens den Standard für protokollfokussierte Newsletter gesetzt hat. Wir sind dankbar für ihr Beispiel und hoffen, dieselbe Strenge in das Nostr-Ökosystem zu bringen.

Diese Erstausgabe etabliert unser wöchentliches Format. Jeden Mittwoch bringen wir dir NIP-Updates, Release-Notes, Entwicklungs-Highlights und technische Anleitungen. Ob du einen Client baust, einen Relay betreibst oder zum Protokoll beiträgst – Nostr Compass möchte deine zuverlässige Quelle für das Geschehen im Ökosystem sein.

## Was ist Nostr?

*Da dies unsere erste Ausgabe ist, beginnen wir mit einer Einführung in die Funktionsweise von Nostr. Regelmäßige Leser können [vorspringen](#news).*

Nostr (Notes and Other Stuff Transmitted by Relays) ist ein dezentrales Protokoll für soziale Netzwerke und Messaging. Anders als traditionelle Plattformen hat Nostr keinen zentralen Server, kein Unternehmen kontrolliert es und es gibt keinen Single Point of Failure. Benutzer besitzen ihre Identität durch kryptografische Schlüsselpaare, und Inhalte fließen durch unabhängige Relay-Server, die jeder betreiben kann.

**Wie es funktioniert:** Benutzer generieren ein Schlüsselpaar (einen privaten Schlüssel namens nsec und einen öffentlichen Schlüssel namens npub). Der private Schlüssel signiert Nachrichten, die "Events" genannt werden, und der öffentliche Schlüssel dient als deine Identität. Events werden an Relays gesendet, die sie speichern und an andere Benutzer weiterleiten. Da du deine Schlüssel kontrollierst, kannst du zwischen Clients oder Relays wechseln, ohne deine Identität oder Follower zu verlieren.

**Warum es wichtig ist:** Nostr bietet Zensurresistenz durch Relay-Vielfalt (wenn ein Relay dich sperrt, können andere immer noch deine Inhalte bereitstellen), Portabilität (deine Identität funktioniert in jeder Nostr-App) und Interoperabilität (alle Nostr-Clients sprechen dasselbe Protokoll). Es gibt keinen Algorithmus, der entscheidet, was du siehst, keine Werbung und keine Datensammlung.

**Das Ökosystem heute:** Nostr unterstützt Microblogging (wie Twitter/X), Langform-Inhalte (wie Medium), Direktnachrichten, Marktplätze, Livestreaming und mehr. Clients umfassen Damus (iOS), Amethyst (Android), Primal, Coracle und Dutzende weitere. Die Lightning-Network-Integration ermöglicht sofortige Zahlungen durch "Zaps". Das Protokoll entwickelt sich weiter durch NIPs (Nostr Implementation Possibilities), community-getriebene Spezifikationen, die die Funktionalität erweitern.

## News {#news}

**NIP-BE Merged: Bluetooth Low Energy Support** - Eine bedeutende neue Fähigkeit [ist im Protokoll gelandet](https://github.com/nostr-protocol/nips/pull/1979). [NIP-BE](/de/topics/nip-be/) spezifiziert, wie Nostr-Anwendungen über Bluetooth Low Energy kommunizieren und synchronisieren können. Dies ermöglicht offline-fähigen Apps, Daten zwischen nahen Geräten ohne Internetverbindung zu synchronisieren. Die Spezifikation passt WebSocket-Relay-Muster an die BLE-Einschränkungen an, verwendet DEFLATE-Kompression und fragmentierte Nachrichten, um mit den kleinen MTU-Größen von BLE (20-256 Bytes) umzugehen. Geräte verhandeln Rollen basierend auf UUID-Vergleich, wobei die höhere UUID zum GATT-Server wird.

**MIP-05: Datenschutzerhaltende Push-Benachrichtigungen** - Das [Marmot Protocol](/de/topics/marmot/) veröffentlichte [MIP-05](/de/topics/mip-05/) ([Spec](https://github.com/marmot-protocol/mips/blob/main/mip-05.md)), eine Spezifikation für Push-Benachrichtigungen, die die Privatsphäre wahren. Traditionelle Push-Systeme erfordern, dass Server Geräte-Token und Benutzeridentitäten kennen; MIP-05 löst dies, indem Geräte-Token mit ECDH+HKDF und ChaCha20-Poly1305 verschlüsselt werden und ephemere Schlüssel verwendet werden, um Korrelation zu verhindern. Ein Drei-Event-Gossip-Protokoll (Kinds 447-449) synchronisiert verschlüsselte Token zwischen Gruppenmitgliedern, und Benachrichtigungen verwenden [NIP-59](/de/topics/nip-59/) Gift Wrapping mit Köder-Token, um Gruppengrößen zu verbergen.

**Blossom BUD-10: Neues URI-Schema** - Das [Blossom](/de/topics/blossom/)-Medienprotokoll bekommt ein benutzerdefiniertes URI-Schema via [BUD-10](/de/topics/bud-10/) ([Spec](https://github.com/hzrd149/blossom/blob/master/buds/10.md)). Das neue `blossom:<sha256>.ext`-Format bettet Datei-Hash, Erweiterung, Größe, mehrere Server-Hinweise und Autor-Pubkeys für [BUD-03](/de/topics/bud-03/) Server-Entdeckung ein. Dies macht Blob-Links widerstandsfähiger als statische HTTP-URLs, indem automatisches Fallback zwischen Servern ermöglicht wird.

**Shopstr Marketplace Updates** - Der Nostr-native Marktplatz [implementierte Nostr Wallet Connect](https://github.com/shopstr-eng/shopstr/pull/202) ([NIP-47](/de/topics/nip-47/)) für Zahlungen, [fügte Listing-Ablauf hinzu](https://github.com/shopstr-eng/shopstr/pull/203) mit [NIP-40](/de/topics/nip-40/) und führte [Rabattcodes](https://github.com/shopstr-eng/shopstr/pull/210) für Verkäufer ein.

## NIP Updates {#nip-updates}

Aktuelle Änderungen am [NIPs Repository](https://github.com/nostr-protocol/nips):

**Neue NIPs:**
- **[NIP-BE](/de/topics/nip-be/)** - Bluetooth Low Energy Messaging und Gerätesynchronisation ([#1979](https://github.com/nostr-protocol/nips/pull/1979))
- **[NIP-63](/de/topics/nip-63/)** - Paywall/Premium Content Standard für die Handhabung von geschütztem Content im Protokoll ([#2156](https://github.com/nostr-protocol/nips/pull/2156))

**Bedeutende Änderungen:**
- **[NIP-24](/de/topics/nip-24/)** - Optionales `languages`-Array zu Kind 0 Benutzer-Metadaten hinzugefügt, das Benutzern erlaubt, mehrere bevorzugte Sprachen mit IETF BCP 47 Tags anzugeben ([#2159](https://github.com/nostr-protocol/nips/pull/2159))
- **[NIP-69](/de/topics/nip-69/)** - Order-Ablauf-Support für P2P-Trading mit `expires_at` und `expiration` Tags hinzugefügt ([#2118](https://github.com/nostr-protocol/nips/pull/2118))
- **[NIP-59](/de/topics/nip-59/)** - Gift Wrap Events können jetzt via NIP-09/NIP-62 Anfragen gelöscht werden ([#2131](https://github.com/nostr-protocol/nips/pull/2131))
- **[NIP-51](/de/topics/nip-51/)** - Hashtag- und URL-Tags aus generischen Lesezeichen entfernt; Hashtags verwenden jetzt Kind 30015 ([#2133](https://github.com/nostr-protocol/nips/pull/2133))
- **[NIP-18](/de/topics/nip-18/)** - Generische Reposts für ersetzbare Events mit `a` Tag Support verbessert ([#2132](https://github.com/nostr-protocol/nips/pull/2132))
- **[NIP-17](/de/topics/nip-17/)** - Formulierung verfeinert und Kind 7 Reaktions-Support zu DMs hinzugefügt ([#2098](https://github.com/nostr-protocol/nips/pull/2098))
- **[NIP-11](/de/topics/nip-11/)** - `self` Feld für Relay-Public-Key-Identifikation hinzugefügt ([#1764](https://github.com/nostr-protocol/nips/pull/1764))

## NIP Deep Dive: NIP-01 und NIP-19 {#nip-deep-dive-nip-01-and-nip-19}

Für diese Erstausgabe behandeln wir zwei fundamentale NIPs, die jeder Nostr-Entwickler verstehen sollte. Siehe unsere Themenseiten für [NIP-01](/de/topics/nip-01/) und [NIP-19](/de/topics/nip-19/).

### NIP-01: Basis-Protokoll {#nip-01-basic-protocol}

[NIP-01](/de/topics/nip-01/) definiert das Kernprotokoll. Alles in Nostr baut auf dieser Spezifikation auf.

**Events** sind der einzige Objekttyp. Jedes Event enthält:
- `id`: SHA256-Hash des serialisierten Events (der eindeutige Bezeichner des Events)
- `pubkey`: Der öffentliche Schlüssel des Erstellers (32-Byte Hex, secp256k1)
- `created_at`: Unix-Zeitstempel
- `kind`: Integer, der den Event-Typ kategorisiert
- `tags`: Array von Arrays für Metadaten
- `content`: Die Nutzlast (Interpretation hängt vom Kind ab)
- `sig`: Schnorr-Signatur, die beweist, dass die Pubkey dieses Event erstellt hat

**Kinds** bestimmen, wie Relays Events speichern:
- Reguläre Events (1, 2, 4-44, 1000-9999): Normal gespeichert, alle Versionen behalten
- Ersetzbare Events (0, 3, 10000-19999): Nur das neueste pro Pubkey wird behalten
- Ephemere Events (20000-29999): Nicht gespeichert, nur an Abonnenten weitergeleitet
- Adressierbare Events (30000-39999): Neuestes pro Pubkey + Kind + `d` Tag Kombination

Kind 0 sind Benutzer-Metadaten (Profil), Kind 1 ist eine Textnotiz (der Basis-Post), Kind 3 ist die Follow-Liste.

**Kind 1: Textnotizen** sind das Herz des sozialen Nostr. Ein Kind 1 Event ist ein Kurzform-Post, ähnlich einem Tweet. Das `content`-Feld enthält den Nachrichtentext (Plaintext, obwohl Clients oft Markdown rendern). Tags ermöglichen Antworten, Erwähnungen und Referenzen.

**Adressierbare Events** (30000-39999) funktionieren wie ersetzbare Events, verwenden aber ein `d` Tag als zusätzlichen Bezeichner. Das Relay behält nur die neueste Version jeder Pubkey + Kind + d-Tag Kombination. Dies ermöglicht editierbare Artikel, Produktlistings oder jeden Fall, in dem du mehrere ersetzbare Items pro Benutzer benötigst.

**Tags** sind Arrays, bei denen das erste Element der Tag-Name ist. Standard-Einzelbuchstaben-Tags (`e`, `p`, `a`, `d`, `t`) werden von Relays für effiziente Abfragen indexiert.

**Client-Relay-Kommunikation** verwendet WebSocket-Verbindungen mit JSON-Arrays als Nachrichten. Das erste Element identifiziert den Nachrichtentyp.

Von Client zu Relay:
- `["EVENT", <event>]` - Veröffentlicht ein Event am Relay
- `["REQ", <sub-id>, <filter>, ...]` - Abonniert Events, die dem/den Filter(n) entsprechen
- `["CLOSE", <sub-id>]` - Beendet ein Abonnement

Von Relay zu Client:
- `["EVENT", <sub-id>, <event>]` - Liefert ein Event, das deinem Abonnement entspricht
- `["EOSE", <sub-id>]` - "Ende gespeicherter Events" - das Relay hat alle historischen Treffer gesendet
- `["OK", <event-id>, <true|false>, <message>]` - Bestätigt, ob ein Event akzeptiert oder abgelehnt wurde
- `["NOTICE", <message>]` - Menschenlesbare Nachricht vom Relay

### NIP-19: Bech32-kodierte Bezeichner {#nip-19-bech32-encoded-identifiers}

[NIP-19](/de/topics/nip-19/) definiert die menschenfreundlichen Formate, die du überall in Nostr siehst: npub, nsec, note und mehr. Diese werden nicht im Protokoll selbst verwendet (das Hex verwendet), aber sie sind essentiell für Teilen und Anzeige.

**Warum bech32?** Rohe Hex-Schlüssel sind fehleranfällig beim Kopieren und visuell schwer zu unterscheiden. Bech32-Kodierung fügt ein menschenlesbares Präfix und Prüfsumme hinzu.

**Basis-Formate** kodieren rohe 32-Byte-Werte:
- `npub` - Öffentlicher Schlüssel (deine Identität, sicher zu teilen)
- `nsec` - Privater Schlüssel (geheim halten, zum Signieren verwendet)
- `note` - Event-ID (referenziert ein bestimmtes Event)

**Teilbare Bezeichner** enthalten Metadaten mit TLV-Kodierung (Type-Length-Value):
- `nprofile` - Profil mit Relay-Hinweisen
- `nevent` - Event mit Relay-Hinweisen, Autor-Pubkey und Kind
- `naddr` - Adressierbare Event-Referenz (Pubkey + Kind + d-Tag + Relays)

**Wichtig:** Verwende niemals bech32-Formate im Protokoll selbst. Events, Relay-Nachrichten und NIP-05-Antworten müssen Hex verwenden. Bech32 ist rein für menschliche Schnittstellen.

## Releases {#releases}

**Amber v4.0.4** - Die Android-Signer-App behebt einen NullPointerException, verbessert die Performance auf dem Aktivitätsbildschirm und fügt Übersetzungen für einige Event-Kinds hinzu. [Release](https://github.com/greenart7c3/Amber/releases/tag/v4.0.4)

**Coracle 0.6.28** - Bugfix-Release für den Web-Client. [Release](https://github.com/coracle-social/coracle/releases/tag/0.6.28)

**Flotilla v1.6.2** - Der Discord-ähnliche Communities-Client behebt Modal-Scrolling und Stil-Probleme. [Release](https://github.com/coracle-social/flotilla/releases/tag/1.6.2)

**nak v0.17.2** - Das Kommandozeilen-Nostr-Tool fügte einen neuen `nip` Befehl für schnelle NIP-Referenzsuche hinzu. [Release](https://github.com/fiatjaf/nak/releases/tag/v0.17.2)

**White Noise v0.2.1** - Major Release für die MLS-basierte verschlüsselte Messaging-App mit Bild-Sharing via Blossom, Hintergrund-Sync, Push-Benachrichtigungen und Lokalisierung in 8 Sprachen. [Release](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**Amethyst v1.04.2** - Feature-Release mit Follow-Listen/Packs, neuen Timeline-Filtern, Bildergalerie und H.265-Videokompression. [Release](https://github.com/vitorpamplona/amethyst/releases/tag/v1.04.2)

**Mostro v0.15.5** - P2P-Trading-Bot-Update mit NIP-69 Order-Ablauf-Support. [Release](https://github.com/MostroP2P/mostro/releases/tag/v0.15.5)

## Entwickler Best Practices {#developer-best-practices}

**Validiere Auth Events Defensiv** - go-nostr behob einen [Panic in NIP-42 Validierung](https://github.com/nbd-wtf/go-nostr/pull/182) wenn das Relay-Tag fehlte. Prüfe immer erforderliche Tags vor dem Zugriff.

**Rate Limiting nach Authentifizierungsstatus** - khatru fügte [NIP-42-basiertes Rate Limiting](https://github.com/fiatjaf/khatru/pull/57) hinzu, das Relays erlaubt, unterschiedliche Limits für authentifizierte vs. anonyme Verbindungen anzuwenden.

**Verwende Cursor-Paginierung für Listen** - Blossom [ersetzte datumsbasierte Paginierung](https://github.com/hzrd149/blossom/pull/65) durch cursorbasierte Paginierung. Datumsbasierte Paginierung bricht, wenn Items Zeitstempel teilen.

**Schema-Validierung für Event-Typen** - Das [nostrability/schemata](https://github.com/nostrability/schemata) Projekt bietet JSON-Schemas zur Validierung NIP-konformer Events.

---

Das war's für diese Woche. Baust du etwas? Hast du Neuigkeiten zu teilen? Möchtest du, dass wir dein Projekt behandeln? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Kontaktiere uns via NIP-17 DM</a> oder finde uns auf Nostr.
