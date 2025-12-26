---
title: 'Nostr Compass #2'
date: 2025-12-24
publishDate: 2025-12-24
draft: false
type: newsletters
translationOf: /en/newsletters/2025-12-24-newsletter.md
translationDate: 2025-12-26
---

Willkommen zurück bei Nostr Compass, deinem wöchentlichen Guide zum Nostr-Protokoll-Ökosystem.

**Diese Woche:** Drei [NIP-55](/de/topics/nip-55/) Signer-Implementierungen erhalten Updates: Amber fügt Performance-Caching hinzu, Aegis erhält `nostrsigner:` URI-Unterstützung, und Primal Android gesellt sich als vollständiger lokaler Signer hinzu. Shopstr führt "Zapsnags" für Flash-Sales via Zaps ein. Mostro fügt einen Entwicklungsfonds hinzu. Vier NIP-Updates landen, darunter Public Messages (Kind 24) und Gruppen-Datenschutzverbesserungen. NDK-Cache-Abfragen werden 162x schneller, Applesauce fügt Reaktionen und NIP-60 Wallet-Unterstützung hinzu, und Tenex führt RAL-Architektur für KI-Agent-Delegation ein. In unserem Deep Dive erklären wir [NIP-02](/de/topics/nip-02/) (Follow-Listen) und [NIP-10](/de/topics/nip-10/) (Antwort-Threading), grundlegende Spezifikationen für den Aufbau sozialer Timelines und Konversationen.

## News {#news}

**Primal Android wird ein NIP-55 Signer** - Aufbauend auf der [Nostr Connect Unterstützung der letzten Woche](/de/newsletters/2025-12-17-newsletter/#primal-android) hat Primal vollständige lokale Signing-Fähigkeiten durch acht zusammengeführte Pull Requests implementiert. Die Implementierung umfasst einen vollständigen `LocalSignerContentProvider`, der Signing-Operationen für andere Android-Apps über die Content Provider-Schnittstelle von Android freilegt, gemäß der [NIP-55](/de/topics/nip-55/)-Spezifikation. Die Architektur trennt Verantwortlichkeiten sauber: `SignerActivity` behandelt benutzerorientierte Genehmigungsabläufe, `LocalSignerService` verwaltet Hintergrundoperationen, und ein neues Berechtigungssystem lässt Benutzer kontrollieren, welche Apps Signaturen anfordern können. Dies macht Primal zu einer praktikablen Alternative zu Amber für Android-Benutzer, die ihre Schlüssel in einer App behalten möchten, während sie andere für verschiedene Nostr-Erlebnisse nutzen.

**Shopstr Zapsnags: Flash Sales via Lightning** - Der Nostr-native Marktplatz führte ["Zapsnags"](https://github.com/shopstr-eng/shopstr/pull/211) ein, eine Flash-Sale-Funktion, mit der Käufer Artikel direkt aus ihrem sozialen Feed mit einem einzigen Zap kaufen können. Die Implementierung filtert Kind 1 Notizen, die mit `#shopstr-zapsnag` getaggt sind, und rendert sie als Produktkarten mit einem "Zap to Buy"-Button anstelle des Standard-Warenkorb-Flows.

**Mostro führt Entwicklungsfonds ein** - Der [NIP-69](/de/topics/nip-69/) P2P Bitcoin Trading Bot [implementierte konfigurierbare Entwicklungsgebühren](https://github.com/MostroP2P/mostro/pull/555) zur Unterstützung nachhaltiger Wartung. Betreiber können `dev_fee_percentage` zwischen 10-100% der Mostro-Handelsgebühr festlegen (Standard 30%), die bei jedem erfolgreichen Trade automatisch an einen Entwicklungsfonds weitergeleitet wird.

## NIP Updates {#nip-updates}

Aktuelle Änderungen am [NIPs Repository](https://github.com/nostr-protocol/nips):

**Neue NIPs:**
- **[NIP-A4](/de/topics/nip-a4/) (Public Messages, Kind 24)** - Ein neuer Kind für Benachrichtigungsbildschirm-Nachrichten, konzipiert für breite Client-Unterstützung ([#1988](https://github.com/nostr-protocol/nips/pull/1988)).

**Bedeutende Änderungen:**
- **[NIP-29](/de/topics/nip-29/)** - Wichtige Klärung der Gruppen-Semantik ([#2106](https://github.com/nostr-protocol/nips/pull/2106)). Das `closed` Tag bedeutet jetzt "schreibunfähig" (nur-Lesen für Nicht-Mitglieder), entkoppelt von Beitrittsmechanik. Ein neues `hidden` Tag verhindert, dass Relays Metadaten oder Mitglieder-Events an Nicht-Mitglieder senden.
- **[NIP-51](/de/topics/nip-51/)** - Kind 30006 für kuratierte Bildersets hinzugefügt ([#2170](https://github.com/nostr-protocol/nips/pull/2170)).
- **[NIP-55](/de/topics/nip-55/)** - Verbindungsinitiierung für Android-Signer geklärt ([#2166](https://github.com/nostr-protocol/nips/pull/2166)).

## NIP Deep Dive: NIP-02 und NIP-10 {#nip-deep-dive-nip-02-and-nip-10}

Diese Woche behandeln wir zwei NIPs, die für soziale Funktionalität essentiell sind: wie Clients wissen, wem du folgst, und wie Konversationen strukturiert werden.

### [NIP-02](/de/topics/nip-02/): Follow-Liste {#nip-02-follow-list}

[NIP-02](https://github.com/nostr-protocol/nips/blob/master/02.md) definiert Kind 3 Events, die deine Follow-Liste speichern. Dieser einfache Mechanismus betreibt den sozialen Graphen, der Timelines möglich macht.

**Struktur:** Ein Kind 3 Event enthält `p` Tags, die gefolgten Pubkeys auflisten:

```json
{
  "id": "d7a8f...",
  "pubkey": "a3b9c...",
  "created_at": 1734912000,
  "kind": 3,
  "tags": [
    ["p", "91cf9..af5f", "wss://alicerelay.example.com", "alice"],
    ["p", "14aeb..8dad", "wss://bobrelay.example.com", "bob"],
    ["p", "612ae..982b", "", ""]
  ],
  "content": "",
  "sig": "e4f8a..."
}
```

Jedes `p` Tag hat vier Positionen: der Tag-Name, die gefolgte Pubkey (Hex), ein optionaler Relay-URL-Hinweis und ein optionaler "Petname" (ein lokaler Spitzname).

**Ersetzbares Verhalten:** Kind 3 fällt in den ersetzbaren Bereich (0, 3, 10000-19999), sodass Relays nur die neueste Version pro Pubkey behalten. Wenn du jemandem Neuen folgst, veröffentlicht dein Client ein vollständiges neues Kind 3, das alle deine Follows plus den neuen enthält.

**Timelines bauen:** Um einen Home-Feed zu erstellen, ruft der Client das Kind 3 des Benutzers ab, extrahiert alle Pubkeys der `p` Tags und abonniert dann Kind 1 Events dieser Autoren.

### [NIP-10](/de/topics/nip-10/): Textnotiz-Threading {#nip-10-text-note-threading}

[NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md) spezifiziert, wie Kind 1 Notizen sich gegenseitig referenzieren, um Antwort-Threads zu bilden.

**Das Problem:** Wenn jemand auf eine Notiz antwortet, müssen Clients wissen: Worauf ist dies eine Antwort? Was ist die Wurzel der Konversation? Wer sollte benachrichtigt werden?

**Markierte Tags (bevorzugt):** Moderne Clients verwenden explizite Marker in `e` Tags:

```json
{
  "kind": 1,
  "tags": [
    ["e", "abc123...", "wss://relay.example.com", "root"],
    ["e", "def456...", "wss://relay.example.com", "reply"],
    ["p", "91cf9..."],
    ["p", "14aeb..."]
  ],
  "content": "Toller Punkt! Ich stimme zu."
}
```

Der `root` Marker zeigt auf die ursprüngliche Notiz, die den Thread gestartet hat. Der `reply` Marker zeigt auf die spezifische Notiz, die beantwortet wird.

**Threading-Regeln:**
- Direkte Antwort auf Root: Ein `e` Tag mit `root` Marker
- Antwort auf eine Antwort: Zwei `e` Tags, eines `root` und eines `reply`
- Der `root` bleibt durch den Thread konstant; `reply` ändert sich je nachdem, worauf du antwortest

## Releases {#releases}

**Zeus v0.12.0** - Aufbauend auf der [NWC parallelen Zahlungsunterstützung der letzten Woche](/de/newsletters/2025-12-17-newsletter/#zeus) liefert das [Major Release](https://github.com/ZeusLN/zeus/releases/tag/v0.12.0) der Lightning-Wallet einen vollständigen [NIP-47](/de/topics/nip-47/) Nostr Wallet Connect Service mit benutzerdefinierter Relay-Unterstützung und Budget-Tracking.

**Amber v4.0.6** - Der Android [NIP-55](/de/topics/nip-55/) Signer [fügt Performance-Caching](https://github.com/greenart7c3/Amber/releases/tag/v4.0.6) zu Signing-Operationen hinzu.

**nak v0.17.3** - Das [neueste Release](https://github.com/fiatjaf/nak/releases/tag/v0.17.3) beschränkt LMDB-Builds auf Linux.

**Aegis v0.3.4** - Der plattformübergreifende Nostr-Signer [fügt Unterstützung](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.4) für das `nostrsigner:` URI-Schema hinzu.

## Bemerkenswerte Code- und Dokumentationsänderungen {#notable-code-and-documentation-changes}

### Damus (iOS) {#damus-ios}

[Mute-Listen-Persistenz](https://github.com/damus-io/damus/pull/3469) behebt ein Problem, bei dem Mute-Listen bei Kaltstart gelöscht wurden. [Profil-Stream-Timing](https://github.com/damus-io/damus/pull/3457) eliminiert eine ~1-Sekunden-Verzögerung bevor gecachte Profile erschienen.

### NDK (Bibliothek) {#ndk-library}

Zwei Pull Requests lieferten dramatische Cache-Performance-Verbesserungen. [PR #371](https://github.com/nostr-dev-kit/ndk/pull/371) behob einen Bug, bei dem Events aus dem SQLite-Cache sofort zurückgeschrieben wurden. [PR #372](https://github.com/nostr-dev-kit/ndk/pull/372) entfernte unnötige `seenEvent` Aufrufe. Ergebnis: Cache-Abfragen fielen von ~3.690ms auf ~22ms (162x schneller).

### rust-nostr (Bibliothek) {#rust-nostr-library}

[Multi-Filter REQ Unterstützung](https://github.com/rust-nostr/nostr/pull/1176) wurde nach Entfernung in einem früheren Refactor wiederhergestellt. [Relay-Herkunft](https://github.com/rust-nostr/nostr/pull/1156) wurde zu `stream_events*` Methoden hinzugefügt. Ein [Sicherheitsfix](https://github.com/rust-nostr/nostr/pull/1179) entfernte die `url-fork` Abhängigkeit.

### Tenex (KI-Agenten) {#tenex-ai-agents}

Das [Multi-Agent-Koordinationssystem](https://github.com/tenex-chat/tenex) führte RAL (Request-Action-Lifecycle) Architektur in [fünf zusammengeführten PRs](https://github.com/pablof7z/tenex/pull/38) ein. RAL ermöglicht Agenten, beim Delegieren von Aufgaben zu pausieren und fortzufahren, wenn Ergebnisse eintreffen.

---

Das war's für diese Woche. Baust du etwas? Hast du Neuigkeiten zu teilen? Möchtest du, dass wir dein Projekt behandeln? <a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">Kontaktiere uns via NIP-17 DM</a> oder finde uns auf Nostr.
