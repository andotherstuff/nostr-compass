---
title: Kind-Verzeichnis
url: /de/kind-registry/
translationOf: /en/kind-registry.md
translationDate: 2025-12-26
---

Event-Kinds sind Ganzzahlen, die Nostr-Events kategorisieren. Dieses Verzeichnis listet alle standardisierten Kinds mit ihren Beschreibungen und definierenden NIPs auf.

**Kind-Bereiche** (aus [NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)):
- **0-999**: Regulare Events (alle Versionen werden behalten)
- **1000-9999**: Regulare Events (Fortsetzung)
- **10000-19999**: Ersetzbare Events (nur der neueste pro Pubkey wird behalten)
- **20000-29999**: Ephemere Events (nicht gespeichert, nur weitergeleitet)
- **30000-39999**: Adressierbare Events (neuester pro Pubkey + Kind + d-Tag)

## Kern-Events (0-99)

| Kind | Beschreibung | NIP |
|------|-------------|-----|
| 0 | Benutzer-Metadaten | [01](https://github.com/nostr-protocol/nips/blob/master/01.md) |
| 1 | Kurze Textnotiz | [10](https://github.com/nostr-protocol/nips/blob/master/10.md) |
| 2 | Relay empfehlen (veraltet) | [01](https://github.com/nostr-protocol/nips/blob/master/01.md) |
| 3 | Follows | [02](https://github.com/nostr-protocol/nips/blob/master/02.md) |
| 4 | Verschlüsselte Direktnachrichten | [04](https://github.com/nostr-protocol/nips/blob/master/04.md) |
| 5 | Event-Löschungsanfrage | [09](https://github.com/nostr-protocol/nips/blob/master/09.md) |
| 6 | Repost | [18](https://github.com/nostr-protocol/nips/blob/master/18.md) |
| 7 | Reaktion | [25](https://github.com/nostr-protocol/nips/blob/master/25.md) |
| 8 | Abzeichen-Verleihung | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 9 | Chat-Nachricht | [C7](https://github.com/nostr-protocol/nips/blob/master/C7.md) |
| 10 | Gruppen-Chat-Threaded-Antwort (veraltet) | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 11 | Thread | [7D](https://github.com/nostr-protocol/nips/blob/master/7D.md) |
| 12 | Gruppen-Thread-Antwort (veraltet) | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 13 | Seal | [59](https://github.com/nostr-protocol/nips/blob/master/59.md) |
| 14 | Direktnachricht | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 15 | Datei-Nachricht | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 16 | Generischer Repost | [18](https://github.com/nostr-protocol/nips/blob/master/18.md) |
| 17 | Reaktion auf eine Website | [25](https://github.com/nostr-protocol/nips/blob/master/25.md) |
| 20 | Bild | [68](https://github.com/nostr-protocol/nips/blob/master/68.md) |
| 21 | Video-Event | [71](https://github.com/nostr-protocol/nips/blob/master/71.md) |
| 22 | Kurzform-Hochkant-Video | [71](https://github.com/nostr-protocol/nips/blob/master/71.md) |
| 40 | Kanal-Erstellung | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 41 | Kanal-Metadaten | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 42 | Kanal-Nachricht | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 43 | Kanal-Nachricht ausblenden | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 44 | Kanal-Benutzer stummschalten | [28](https://github.com/nostr-protocol/nips/blob/master/28.md) |
| 62 | Anfrage zum Verschwinden | [62](https://github.com/nostr-protocol/nips/blob/master/62.md) |
| 64 | Schach (PGN) | [64](https://github.com/nostr-protocol/nips/blob/master/64.md) |

## MLS-Verschlüsselung (443-445)

| Kind | Beschreibung | NIP |
|------|-------------|-----|
| 443 | KeyPackage | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 444 | Willkommensnachricht | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 445 | Gruppen-Event | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |

## Regulare Events (1000-9999)

| Kind | Beschreibung | NIP |
|------|-------------|-----|
| 1018 | Umfrage-Antwort | [88](https://github.com/nostr-protocol/nips/blob/master/88.md) |
| 1021 | Gebot | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 1022 | Gebot-Bestätigung | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 1040 | OpenTimestamps | [03](https://github.com/nostr-protocol/nips/blob/master/03.md) |
| 1059 | Gift Wrap | [59](https://github.com/nostr-protocol/nips/blob/master/59.md) |
| 1063 | Datei-Metadaten | [94](https://github.com/nostr-protocol/nips/blob/master/94.md) |
| 1068 | Umfrage | [88](https://github.com/nostr-protocol/nips/blob/master/88.md) |
| 1111 | Kommentar | [22](https://github.com/nostr-protocol/nips/blob/master/22.md) |
| 1222 | Sprachnachricht | [A0](https://github.com/nostr-protocol/nips/blob/master/A0.md) |
| 1244 | Sprachnachricht-Kommentar | [A0](https://github.com/nostr-protocol/nips/blob/master/A0.md) |
| 1311 | Live-Chat-Nachricht | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 1337 | Code-Schnipsel | [C0](https://github.com/nostr-protocol/nips/blob/master/C0.md) |
| 1617 | Patches | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1618 | Pull Requests | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1619 | Pull-Request-Updates | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1621 | Issues | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 1984 | Meldung | [56](https://github.com/nostr-protocol/nips/blob/master/56.md) |
| 1985 | Label | [32](https://github.com/nostr-protocol/nips/blob/master/32.md) |
| 2003 | Torrent | [35](https://github.com/nostr-protocol/nips/blob/master/35.md) |
| 2004 | Torrent-Kommentar | [35](https://github.com/nostr-protocol/nips/blob/master/35.md) |
| 4550 | Community-Beitragsgenehmigung | [72](https://github.com/nostr-protocol/nips/blob/master/72.md) |
| 5000-5999 | Job-Anfrage | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 6000-6999 | Job-Ergebnis | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 7000 | Job-Feedback | [90](https://github.com/nostr-protocol/nips/blob/master/90.md) |
| 7374 | Reservierte Cashu-Wallet-Tokens | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 7375 | Cashu-Wallet-Tokens | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 7376 | Cashu-Wallet-Verlauf | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |
| 8000 | Benutzer hinzufügen | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 8001 | Benutzer entfernen | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 9000-9030 | Gruppen-Steuerungs-Events | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 9041 | Zap-Ziel | [75](https://github.com/nostr-protocol/nips/blob/master/75.md) |
| 9321 | Nutzap | [61](https://github.com/nostr-protocol/nips/blob/master/61.md) |
| 9734 | Zap-Anfrage | [57](https://github.com/nostr-protocol/nips/blob/master/57.md) |
| 9735 | Zap | [57](https://github.com/nostr-protocol/nips/blob/master/57.md) |
| 9802 | Highlights | [84](https://github.com/nostr-protocol/nips/blob/master/84.md) |

## Ersetzbare Events (10000-19999)

| Kind | Beschreibung | NIP |
|------|-------------|-----|
| 10000 | Stummschaltungsliste | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10001 | Anpinnungsliste | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10002 | Relay-Listen-Metadaten | [65](https://github.com/nostr-protocol/nips/blob/master/65.md) |
| 10003 | Lesezeichenliste | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10004 | Communities-Liste | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10005 | Öffentliche-Chats-Liste | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10006 | Blockierte-Relays-Liste | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10007 | Such-Relays-Liste | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10009 | Benutzergruppen | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10012 | Favoriten-Relays-Liste | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10013 | Private-Event-Relay-Liste | [37](https://github.com/nostr-protocol/nips/blob/master/37.md) |
| 10015 | Interessenliste | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10019 | Nutzap-Mint-Empfehlung | [61](https://github.com/nostr-protocol/nips/blob/master/61.md) |
| 10020 | Medien-Follows | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10030 | Benutzer-Emoji-Liste | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 10050 | Relay-Liste für DM-Empfang | [17](https://github.com/nostr-protocol/nips/blob/master/17.md) |
| 10051 | KeyPackage-Relays-Liste | [EE](https://github.com/nostr-protocol/nips/blob/master/EE.md) |
| 10063 | Benutzer-Server-Liste | Blossom |
| 10166 | Relay-Monitor-Ankündigung | [66](https://github.com/nostr-protocol/nips/blob/master/66.md) |
| 10312 | Raum-Präsenz | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 13194 | Wallet-Info | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 13534 | Mitgliedschaftslisten | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 17375 | Cashu-Wallet-Event | [60](https://github.com/nostr-protocol/nips/blob/master/60.md) |

## Authentifizierung und Wallet (22000-27999)

| Kind | Beschreibung | NIP |
|------|-------------|-----|
| 22242 | Client-Authentifizierung | [42](https://github.com/nostr-protocol/nips/blob/master/42.md) |
| 23194 | Wallet-Anfrage | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 23195 | Wallet-Antwort | [47](https://github.com/nostr-protocol/nips/blob/master/47.md) |
| 24133 | Nostr Connect | [46](https://github.com/nostr-protocol/nips/blob/master/46.md) |
| 24242 | Auf Medienservern gespeicherte Blobs | Blossom |
| 27235 | HTTP Auth | [98](https://github.com/nostr-protocol/nips/blob/master/98.md) |

## Zugriffskontrolle (28000-29999)

| Kind | Beschreibung | NIP |
|------|-------------|-----|
| 28934 | Beitrittsanfrage | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 28935 | Einladungsanfrage | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |
| 28936 | Austrittsanfrage | [43](https://github.com/nostr-protocol/nips/blob/master/43.md) |

## Adressierbare Events (30000-39999)

| Kind | Beschreibung | NIP |
|------|-------------|-----|
| 30000 | Follow-Sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30002 | Relay-Sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30003 | Lesezeichen-Sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30004 | Kurations-Sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30005 | Video-Sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30007 | Kind-Stummschaltungs-Sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30008 | Profil-Abzeichen | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 30009 | Abzeichen-Definition | [58](https://github.com/nostr-protocol/nips/blob/master/58.md) |
| 30015 | Interessen-Sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30017 | Stand erstellen oder aktualisieren | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30018 | Produkt erstellen oder aktualisieren | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30019 | Marktplatz-UI/UX | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30020 | Produkt als Auktion verkauft | [15](https://github.com/nostr-protocol/nips/blob/master/15.md) |
| 30023 | Langform-Inhalt | [23](https://github.com/nostr-protocol/nips/blob/master/23.md) |
| 30024 | Entwurf Langform-Inhalt | [23](https://github.com/nostr-protocol/nips/blob/master/23.md) |
| 30030 | Emoji-Sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30063 | Release-Artefakt-Sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30078 | Anwendungsspezifische Daten | [78](https://github.com/nostr-protocol/nips/blob/master/78.md) |
| 30166 | Relay-Erkennung | [66](https://github.com/nostr-protocol/nips/blob/master/66.md) |
| 30267 | App-Kurations-Sets | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 30311 | Live-Event | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30312 | Interaktiver Raum | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30313 | Konferenz-Event | [53](https://github.com/nostr-protocol/nips/blob/master/53.md) |
| 30315 | Benutzerstatus | [38](https://github.com/nostr-protocol/nips/blob/master/38.md) |
| 30402 | Kleinanzeige | [99](https://github.com/nostr-protocol/nips/blob/master/99.md) |
| 30403 | Entwurf Kleinanzeige | [99](https://github.com/nostr-protocol/nips/blob/master/99.md) |
| 30617 | Repository-Ankündigungen | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 30618 | Repository-Status-Ankündigungen | [34](https://github.com/nostr-protocol/nips/blob/master/34.md) |
| 30818 | Wiki-Artikel | [54](https://github.com/nostr-protocol/nips/blob/master/54.md) |
| 30819 | Weiterleitungen | [54](https://github.com/nostr-protocol/nips/blob/master/54.md) |
| 31234 | Entwurf-Event | [37](https://github.com/nostr-protocol/nips/blob/master/37.md) |
| 31922 | Datumsbasiertes Kalender-Event | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31923 | Zeitbasiertes Kalender-Event | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31924 | Kalender | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31925 | Kalender-Event-RSVP | [52](https://github.com/nostr-protocol/nips/blob/master/52.md) |
| 31989 | Handler-Empfehlung | [89](https://github.com/nostr-protocol/nips/blob/master/89.md) |
| 31990 | Handler-Information | [89](https://github.com/nostr-protocol/nips/blob/master/89.md) |
| 34550 | Community-Definition | [72](https://github.com/nostr-protocol/nips/blob/master/72.md) |
| 38172 | Cashu-Mint-Ankündigung | [87](https://github.com/nostr-protocol/nips/blob/master/87.md) |
| 38173 | Fedimint-Ankündigung | [87](https://github.com/nostr-protocol/nips/blob/master/87.md) |
| 38383 | Peer-to-Peer-Order-Events | [69](https://github.com/nostr-protocol/nips/blob/master/69.md) |
| 39000-39009 | Gruppen-Metadaten-Events | [29](https://github.com/nostr-protocol/nips/blob/master/29.md) |
| 39089 | Starterpakete | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 39092 | Medien-Starterpakete | [51](https://github.com/nostr-protocol/nips/blob/master/51.md) |
| 39701 | Web-Lesezeichen | [B0](https://github.com/nostr-protocol/nips/blob/master/B0.md) |

*Zuletzt aktualisiert: Dezember 2025*

Siehe das [NIPs-Repository](https://github.com/nostr-protocol/nips) für die autoritative Quelle.
