---
title: "Nostr Compass #34"
date: 2026-08-05
publishDate: 2026-08-05
translationOf: /en/newsletters/2026-08-05-newsletter.md
translationDate: 2026-08-06
draft: false
type: newsletters
description: "Sandstr bietet Rundgänge mit Mock-Daten durch Nostr-Clients, nostr-mill führt eine Signierzustimmung pro Event ein, und nostrord erweitert relay-gehostete Gruppen. Die Deep Dives behandeln relay-gestützte Suche und portable Highlights."
---

Willkommen zurück bei [Nostr Compass](https://github.com/andotherstuff/nostr-compass), eurem wöchentlichen Wegweiser für Nostr.

**Diese Woche:** [Sandstr](https://sandstr.app/) lässt Neulinge simulierte Nostr-Clients erkunden, ohne Schlüssel zu erstellen oder eine App zu installieren. [nostr-mill](https://github.com/0ceanSlim/nostr-mill) führt eine Signierzustimmung pro Event und eine clientübergreifende Schlüsselwiederherstellung ein, während [nostrord](https://github.com/nostrord/nostrord) relay-gehostete Gruppen, Signer, Moderation, Uploads und Highlights erweitert. Die Protokollarbeit umfasst Nostr-Eventformate, Wallet-Verbindungen, Relay-Discovery, Napplets, Marmot und Concord; die Deep Dives erklären relay-gestützte Suche und portable Highlights.

## Top-Storys

### nostr-mill 1.6.0 bringt Signierzustimmung und Kontowiederherstellung in den Browser

[nostr-mill 1.6.0](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0) ist ein einbettbarer Browser-Kontowähler und -Signer. Er fragt nun pro Event-Kind um Zustimmung und zeigt decodierte Inhalte und Tags vor dem Signieren an, mit zeitlich begrenzten Freigaben und einem Berechtigungsmanager. Das Release behebt außerdem einen Fehler in der ersten Sitzung, der Kategorien, die für eine Abfrage bei jedem Mal konfiguriert waren, ohne Nachfrage signieren ließ. Das optionale Google-Onboarding kann einen bestehenden `nsec` importieren, speichert den Schlüssel verschlüsselt im App-Daten-Ordner des Nutzers auf Drive, unterstützt mehrere Identitäten und kann einen `ncryptsec` im [NIP-49](/de/topics/nip-49/)-Format (verschlüsseltes Private-Key-Format) exportieren.

Das [experimentelle Relay-Backup](https://github.com/0ceanSlim/nostr-mill/releases/tag/v1.6.0) leitet eine starke Wiederherstellungsphrase mit scrypt und HKDF ab, verpackt den Schlüssel als `ncryptsec`, verifiziert abgerufene Events und verlangt vor der Wiederherstellung ein Relay-Quorum. Der [NIP-55](/de/topics/nip-55/)-Login (Android-Signer-Intents) nutzt jetzt Ambers Zwischenablage-Rückweg, und [NIP-46](/de/topics/nip-46/)-Verbindungen (relay-vermitteltes Remote-Signing) sind standardmäßig leise. Branding-Steuerungen und responsive Berechtigungsbildschirme runden das Release ab, ohne bestehende Integrationen zu ändern, sofern ein Betreiber nicht aktiv zustimmt.

### nostrord 2.5.0 verleiht Relay-Gruppen stabile, relay-spezifische Identitäten

[nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) ist ein plattformübergreifender Client für relay-gehostete Communities. Er leitet nun eine [NIP-29](/de/topics/nip-29/)-Identität (relay-verwaltete Gruppen) aus Gruppen-ID und Host-Relay ab, begrenzt Mitgliedschaft und Admin-Abzeichen auf dieselbe Weise, akzeptiert Gruppen-`naddr`-Deep-Links und synchronisiert private Gruppen-Threads zwischen Geräten.

Das [Release](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) fügt außerdem einen [NIP-56](/de/topics/nip-56/)-Moderations-Posteingang (Report-Events) hinzu, Amber-Login über NIP-55, Rate-Limit-Backoff für NIP-46-Signer-Verkehr, [NIP-84](/de/topics/nip-84/)-Rendering (portable Highlights) mit Wiederholungsversuchen für unaufgelöste Referenzen sowie Medien-Uploads über Blossom oder [NIP-96](/de/topics/nip-96/) (HTTP-Dateispeicherung). Der Google-Login sichert den Schlüssel jetzt vor der Kontoerstellung und bestätigt Trennungen. Thread-Antworten erhalten reichhaltigere Inhalte und Admin-Löschungen, während Korrekturen am Desktop-Schlüsselbund und an der mobilen Tastatur diese Protokollfunktionen nutzbar halten.

### Primal Android 3.5.25 aktualisiert Remote-Signing und Follow-Listen-Filterung

[Primal Android 3.5.25](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.25) ist ein mobiler Nostr-Client mit Feeds, Suche und Remote-Signing. Er aktualisiert seinen Remote-Signer auf das aktuelle Protokollverhalten, fügt eine Stummschaltungsliste für Gefolgte hinzu, öffnet die Suche aus Explore, repariert blockierte Relay-Verbindungen automatisch, legt Anfrage-Timeouts in der Oberfläche offen, weist ungültige Follow-Listen-Einträge zurück und aktualisiert die Fallback-Relay-URLs. Feed-Prefetching, geringerer Speicherverbrauch und eine 100-MB-Cache-Obergrenze senken die Kosten für die Aktualität dieser Feeds. Notizen mit einem einzelnen Bild nutzen nun die volle Inhaltsbreite, und Profilsteuerungen sowie Medien-Vorladen erhalten kleinere Interaktions- und Sortierkorrekturen.

### Nostur 1.30.2 erweitert private Antworten und Medien in Direktnachrichten

[Nostur 1.30.2](https://github.com/nostur-com/nostur-ios-public/releases/tag/527) ist ein Nostr-Client für Apple-Plattformen. Er blendet die Aktion für private Antworten jetzt immer ein, fügt DM-Medien-Caches pro Unterhaltung mit Limits und Löschsteuerungen hinzu, verbessert die Namen- und Tag-Vervollständigung in Beiträgen und Chats, zeigt referenzierte Nachrichten im Live-Chat an und nimmt den Raumtitel in Chat-Benachrichtigungen auf. Korrekturen an der Feed-Paginierung und an verschachtelten Antworten beheben Rückschritte beim Abruf und beim Rendern von Unterhaltungen.

### Chama 5.7.0 führt Schlichter-Einträge und gecachte Handelswiederherstellung ein

[Chama 5.7.0](https://github.com/jesuspirate/chama/releases/tag/v5.7.0) koordiniert Peer-Handel und Schlichtung über signierte Nostr-Event-Ketten. Es zeigt den gesperrten Betrag eines Schlichters, die Laufzeit seiner Kaution und seinen Finanzierungs-Outpoint an; verzeichnet, wann ein Ersatz einen abwesenden Schlichter ersetzt hat; und definiert ruhende Fehler-Attestierungen des Kinds `38136`, die die Signaturen beider Parteien erfordern. Eine explizite Reparatur wiederholt unvollständige Relay-Historien gegen den dauerhaften Geräte-Cache und veröffentlicht wiederhergestellte Events erneut, während fehlgeschlagene Veröffentlichungen für die nächste Verbindung in die Warteschlange gehen. Das Release verhindert außerdem geräteübergreifend doppelte Schlichter-Prämienzahlungen, indem es das Kind-`38113`-Event des Autors als Zahlungsnachweis behandelt.

### Auditable Voting 0.1.165 stellt die Zustellung delegierter Stimmzettel wieder her

[Auditable Voting 0.1.165](https://github.com/tidley/auditable-voting/releases/tag/v0.1.165) führt verifizierbare Abstimmungen durch und trennt dabei Wähler-Credentials vom Stimmzettelinhalt. Es stellt die delegierte Ausstellung blinder Stimmzettel über authentifizierte Delegationszustellung und Kontroll-DM-Nachträge wieder her, belässt Direktnachrichten mit blinden Credentials auf den konfigurierten privaten Relays und aktualisiert den Audit-Proxy auf 0.1.52.

### Sandstr lässt Neulinge Nostr-Clients mit Mock-Daten ausprobieren

[Sandstr](https://sandstr.app/) bietet interaktive Browser-Simulationen von Nostr-Clients, damit Neulinge deren Oberflächen vergleichen können, bevor sie einen installieren oder ein Schlüsselpaar erstellen. Der Launch vom 3. August umfasst referenzverifizierte Nachbildungen von Damus, Amethyst, Primal, Snort, YakiHonne, Coracle und Wisp sowie klar gekennzeichnete frühe Vorschauen von Gossip, Keychat und Olas. Alles läuft lokal gegen Mock-Daten, sodass die Simulationen weder Schlüssel erzeugen noch sich mit Relays verbinden. Jede Simulation verlinkt auf die Website und das Quell-Repository des echten Clients und macht Sandstr damit zu einem Onboarding- und Interface-Vergleichswerkzeug statt zu einem weiteren Nostr-Client. Es zeigt, wie sich Feeds, Profile, Threads, Direktnachrichten, Suche, Zaps und Relay-Steuerungen anfühlen, ohne von einem Erstnutzer vorab eine Identitäts- oder Sicherheitsentscheidung zu verlangen.


### mineracks signer kombiniert eine Browser-Erweiterung mit einem Desktop-Bunker

[mineracks signer](https://github.com/mineracks/mineracks-signer) bietet zwei Signier-Oberflächen aus demselben Projekt. Seine Browser-Erweiterung implementiert [NIP-07](/de/topics/nip-07/), damit Webanwendungen Signaturen anfordern können, ohne den privaten Schlüssel zu erhalten, während die Desktop-Anwendung einen [NIP-46](/de/topics/nip-46/)-Remote-Signer für Clients bereitstellt, die über Relays kommunizieren.

Das [Desktop-Release 0.1.0](https://github.com/mineracks/mineracks-signer/releases/tag/desktop-v0.1.0) des Projekts speichert Schlüsselmaterial mit der NIP-49-Verschlüsselungscodierung und hält den entschlüsselten Schlüssel im Rust-Prozess, statt ihn an die Oberfläche weiterzugeben. Jede Anfrage zeigt die aufrufende Anwendung und die angeforderte Aktion, während die automatische Genehmigung pro Anwendung optional und widerrufbar ist. Der erste Desktop-Build unterstützt Apple Silicon, aber keine Intel-Macs.

## Releases

### Jumble 26.8.1 führt Proof-of-Work-Steuerungen und Kommentar-Vorschauen ein

[Jumble 26.8.1](https://github.com/CodyTseng/jumble/releases/tag/v26.8.1) ist ein Web- und Desktop-Nostr-Client. Er merkt sich die Proof-of-Work-Schwierigkeit für das Veröffentlichen, zeigt Abzeichen für verifizierte Arbeit an, zeigt Vorschauen verlinkter Kommentare über externen Inhalten, speichert Bilder aus dem Vollbild-Viewer und klappt lange Profil-Biografien bei Bedarf aus. Reaktions-Benachrichtigungen verwerfen jetzt nicht unterstützte Event-Kinds, Hinweise auf Relay-Trennungen sind weniger aufdringlich, die Standard-Relays wurden aktualisiert und ein Konflikt bei der Medien-Autowiedergabe wurde behoben.

### nostr-calendar 2.1.0 stellt die Signer-Bindung bei privaten Formularen wieder her

[nostr-calendar 2.1.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v2.1.0) veröffentlicht Kalender, Events und Formularantworten als Nostr-Daten. Es bindet Einreichungen privater Formulare an den aktiven Signer, speichert beabsichtigte doppelte Events auf Relays, behebt den Relay-Abruf, parst Kalenderdaten in lokaler Zeit und fügt App-Benachrichtigungen sowie einen iOS-Client hinzu. Die Signer-Korrektur verhindert, dass eine veraltete Identität eine unbrauchbare verschlüsselte Antwort erzeugt.

### Manent 2.0.0 führt Tagging und Suche für gespeicherte Notizen ein

[Manent 2.0.0](https://github.com/dtonon/manent/releases/tag/v2.0.0) ist ein persönliches Archiv für signierte Nostr-Notizen. Es fügt lokale Tags und Suche hinzu, sodass Leser gespeicherte Events organisieren und abrufen können, ohne deren signierte Inhalte zu verändern.

### nosvelte 0.6.1 schließt leere Abonnements nach EOSE

[nosvelte 0.6.1](https://github.com/akiomik/nosvelte/releases/tag/v0.6.1) stellt reaktive Svelte-Komponenten und -Hooks für Relay-Daten bereit. Leere Suchen kommen jetzt mit dem End of Stored Events zum Abschluss, ein Abbruch schließt das zugrunde liegende `REQ`, Wiederholungen räumen veraltete Fehler ab, und Listen-Hooks geben ihren dokumentierten Leerwert zurück. Es erkennt außerdem adressierbare Events unabhängig davon, wo ihr `d`-Tag steht, ersetzt überholte Metadaten und Artikel, dedupliziert Reaktionen nach Event-ID und behält jedes Event aus dem ersten Batch eines Relays.

## Unveröffentlichte Änderungen

### NMP bindet die Relay-Zulassung an Deklarationen und erweitert Gruppenabfragen

[NMP](https://github.com/pablof7z/nmp) ist ein TypeScript-Toolkit zum Bauen von Nostr-Anwendungen und relay-gestützten Gruppen-Oberflächen. [PR #1254](https://github.com/pablof7z/nmp/pull/1254) lässt die Relay-Zulassung dem Eigentümer der autorisierenden Deklaration folgen und hält die Berechtigungsentscheidung so an den signierten Nostr-Zustand gebunden. [PR #1255](https://github.com/pablof7z/nmp/pull/1255) verallgemeinert [NIP-29](/de/topics/nip-29/)-Abfragen relay-verwalteter Gruppen, statt eine einzige enge Abfrageform anzunehmen. Beide Änderungen sind gemergt, aber noch nicht in einem getaggten Release erschienen.

### Mosaico leitet die Identität verwalteter Gruppen aus Relay-Einträgen ab

[Mosaico](https://github.com/pablof7z/mosaico) ist ein Nostr-Client zum Durchsuchen und Verwalten relay-verwalteter Communities. [PR #758](https://github.com/pablof7z/mosaico/pull/758) leitet die Identität einer verwalteten Gruppe vom Relay ab, das ihre maßgeblichen Einträge hostet. [PR #757](https://github.com/pablof7z/mosaico/pull/757) beobachtet den veröffentlichten Eintrag der Gruppe bei der Auflösung des Administrationsstatus. So bleiben zwei gleichnamige Gruppen auf unterschiedlichen Relays unterscheidbar, und Clients erhalten eine relay-gestützte Quelle für ihre Verwaltungsmetadaten.

### Divine isoliert langsame Relays bei Multi-Relay-Abfragen

[Divine](https://github.com/divinevideo/divine-mobile) ist ein mobiler Kurzvideo-Client, der Videos über Nostr veröffentlicht und abruft. [PR #6673](https://github.com/divinevideo/divine-mobile/pull/6673) gibt jeder Relay-Abfrage ihr eigenes Timeout, statt eine blockierte Verbindung das Zeitbudget einer gesamten Anfrage aufbrauchen zu lassen. Ergebnisse antwortender Relays können so eintreffen, während der langsame Endpunkt unabhängig aufgegeben wird. Die Änderung verbessert den Abruf, ohne ein Relay als maßgeblich für das kombinierte Ergebnis zu behandeln.

### rust-nostr härtet Verschlüsselung, Hashes und Reconciliation

[rust-nostr](https://github.com/rust-nostr/nostr) ist eine Rust-Bibliothek und ein Toolkit für Nostr-Clients, -Relays und Protokollimplementierungen. [PR #1421](https://github.com/rust-nostr/nostr/pull/1421) reduziert Allokationen im versionierten [NIP-44](/de/topics/nip-44/)-Verschlüsselungspfad, während [PR #1423](https://github.com/rust-nostr/nostr/pull/1423) typisierte Hashes einführt, die das versehentliche Vermischen inkompatibler Digest-Werte erschweren. [Commit 21e31c2](https://github.com/rust-nostr/nostr/commit/21e31c28da3dfadedb5fa6e58c712647f16e5f69) verhindert, dass eine fehlerhafte [NIP-77](/de/topics/nip-77/)-Negentropy-Nachricht zur Mengenabgleichung das lokale Relay trennt. Die gemergte Arbeit verschärft sowohl den Umgang mit verschlüsselten Nutzdaten als auch das Fehlerverhalten bei der Reconciliation vor dem nächsten Release.

### Zeus serialisiert NWC-Zahlungen vor der Belastung von Ausgabenbudgets

[Zeus](https://github.com/ZeusLN/zeus) ist eine mobile Bitcoin- und Lightning-Wallet, die Wallet-Operationen über Nostr Wallet Connect bereitstellen kann. [PR #4305](https://github.com/ZeusLN/zeus/pull/4305) rechnet ausstehende Zahlungen auf ein [NIP-47](/de/topics/nip-47/)-Budget (Nostr Wallet Connect) an, statt auf die Abwicklung zu warten. [PR #4303](https://github.com/ZeusLN/zeus/pull/4303) serialisiert die Zahlungsabwicklung, damit gleichzeitige Anfragen nicht dasselbe Autorisierungslimit überrennen können. Das gemergte Paar schließt eine Lücke bei der Budgetdurchsetzung auf der Nostr-Kontrolloberfläche der Wallet.

### Nostr Components teilt einen einzigen Relay-Verbindungsversuch

[Nostr Components](https://github.com/saiy2k/nostr-components) ist eine wiederverwendbare Web-Component-Bibliothek, um Nostr-Daten und -Interaktionen in Anwendungen einzubinden. [PR #105](https://github.com/saiy2k/nostr-components/pull/105) lässt gleichzeitig gemountete Komponenten einen laufenden Relay-Verbindungsversuch teilen. Jeder Nutzer erhält weiterhin die resultierende Verbindung, aber gleichzeitige Mounts öffnen keine doppelten Sockets mehr, während der erste Handshake noch aussteht. Die Änderung reduziert vermeidbare Relay-Last in Anwendungen, die aus mehreren unabhängigen Komponenten zusammengesetzt sind.

## NIP-Updates und Protokoll-Spezifikationsarbeit

### Nostr-Eventformate und Discovery

[NIP-PR #2430](https://github.com/nostr-protocol/nips/pull/2430) schlägt Sticker-Packs als adressierbare Kind-`30031`-Definitionen und die installierten Packs eines Nutzers als ersetzbares Kind `10031` vor. Jeder Sticker-Tag trägt einen Shortcode, einen SHA-256-Hash und einen MIME-Typ; das Bild verbleibt auf einem [NIP-B7](https://github.com/nostr-protocol/nips/blob/master/B7.md)-Server (Blossom-Blob-Speicher). Der offene Entwurf standardisiert damit Pack-Identität und -Installation, ohne Bildbytes in Events abzulegen.

[NIP-PR #2429](https://github.com/nostr-protocol/nips/pull/2429) schlägt adressierbare Gopher-Dokumente des Kinds `31436` vor. Jedes Event enthält einen UTF-8-Text- oder Menüknoten, und signierte Knoten unter einer Pubkey bilden ein Gopherhole, das jede relay-gestützte RFC-1436-Bridge ausliefern kann. Der offene Vorschlag nutzt den gewöhnlichen Speicher adressierbarer Events, statt die Veröffentlichung an einen einzelnen Gopher-Hostnamen zu binden.

[NIP-PR #2428](https://github.com/nostr-protocol/nips/pull/2428) schlägt private Gruppen mit Epochen-Tickets vor. Eine Gruppe rotiert Mitgliedschafts-Credentials zwischen Epochen, und Clients legen das Ticket der aktuellen Epoche vor, um teilzunehmen. Der Entwurf zielt auf privaten Chat ab, ohne von einem Relay zu verlangen, ein permanentes Bearer-Token als lebenslange Mitgliedschaft zu behandeln.

[NIP-PR #2425](https://github.com/nostr-protocol/nips/pull/2425), letzte Woche als Vorschlag behandelt, hat nun eine URI-Klarstellung in [NIP-B0](/de/topics/nip-b0/) (adressierbare Web-Lesezeichen) gemergt. Er unterscheidet weggelassene HTTPS-Präfixe von expliziten URI-Schemata, wenn ein Lesezeichen sein Ziel im `d`-Tag speichert, und verhindert so, dass Clients ein mehrdeutiges Ziel rekonstruieren.

### Zahlungen und Wallet-Verbindungen

[NIP-PR #2419](https://github.com/nostr-protocol/nips/pull/2419), in der Ausgabe vom 22. Juli als Vorschlag behandelt, hat nun einen kleineren [NIP-47](/de/topics/nip-47/)-Kern (Nostr Wallet Connect) gemergt. Verbindungs-URIs, verschlüsselter Relay-Transport, Capability-Discovery, Verschlüsselungsaushandlung und gängige Methoden bleiben im NIP; Benachrichtigungen, Hold-Invoices, Keysend, Transaktionshistorie, Metadaten und Deep-Link-Pairing wandern in ein eigenes Erweiterungs-Repository. Bestehende Verbindungen bleiben kompatibel, während Wallets die optionalen Verträge unabhängig implementieren können.

[NWC-PR #2](https://github.com/nostr-wallet-connect/nwc/pull/2), letzte Woche als Vorschlag behandelt, hat nun BIP-321-Zahlungsmethoden in jenes Erweiterungs-Repository gemergt. BIP-321 stellt einen gemeinsamen Bitcoin-Zahlungs-URI bereit, der verschiedene Rails tragen kann, sodass NWC-Aufrufer eine Zahlung anfordern oder senden können, ohne für jeden zugrunde liegenden Anweisungstyp einen neuen Kern-RPC hinzuzufügen.

### Napplet-Host-Fähigkeiten

[NAP-PR #95](https://github.com/napplet/naps/pull/95) schlägt Katalog-Discovery für über Nostr verteilte Sandbox-Anwendungen vor. Ein Napplet fragt seinen Host, welche Anwendungen und Fähigkeiten verfügbar sind, und der Host liefert policy-gefilterte Metadaten, statt seine gesamte lokale Umgebung offenzulegen. Der Vertrag unterstützt Startentscheidungen, ohne während der Discovery Ausführungsrechte zu gewähren.

[NAP-PR #33](https://github.com/napplet/naps/pull/33) schlägt shell-vermittelte Datei- und Blob-Uploads vor. Ein Napplet liefert Bytes und Absicht; der Host wählt einen NIP-96- oder Blossom-Rail, signiert die Autorisierung, meldet den Fortschritt und gibt URLs, Hashes, MIME-Daten und anhängfertige [NIP-94](/de/topics/nip-94/)-Tags (Datei-Metadaten) zurück. Speicher-Credentials und HTTP-Autorität gelangen niemals in das Napplet.

### Marmot-verschlüsselte Gruppen

[Marmot-PR #410](https://github.com/marmot-protocol/marmot/pull/410) hat Konvergenz- und Deferred-Input-Regeln gemergt. Clients unterscheiden ein Objekt, dem eine aktuelle Epochen-Abhängigkeit fehlt, von veralteter oder ungültiger Eingabe, halten es nach einer Ressourcenverweigerung für einen erneuten Abruf berechtigt und versuchen es erneut, wenn ein anderer Commit den Entschlüsselungskontext ändert. Ein domänensepariertes State-Commitment gibt Konformitätstests ein gemeinsames Konvergenz-Orakel, ohne ein Produktions-Wire-Feld hinzuzufügen.

### Concord-Community-Ebenen

[Concord-PR #14](https://github.com/concord-protocol/concord/pull/14) hat CORD-08-Disappearing-Messages gemergt. Ein Community-Metadatenwert legt die Lebensdauer fest; Chat-Rumors und verschlüsselte Wraps tragen einen [NIP-40](/de/topics/nip-40/)-Tag (Event-Ablauf), während Lösch-Events und der Timer-Hinweis des Kinds `1740` ausgenommen sind. Der signierte Timer reist mit dem Community-Zustand, wobei das Relay-Löschen weiterhin eine Aufbewahrungsanfrage und keine kryptografische Löschgarantie bleibt.

[Concord-PR #13](https://github.com/concord-protocol/concord/pull/13) hat rotierungsfestes Pinnen in CORD-04 gemergt. Jeder Kanal hat eine vollständig ersetzende Pin-Liste auf der Kontrollebene; Einträge tragen das ursprüngliche signierte Siegel plus NIP-44-Expansionsschlüssel pro Nachricht, sodass ein neues Mitglied Autor und Klartext verifizieren kann, ohne einen alten Epochenschlüssel zu erhalten. Private Listen können an eine Kanal-Epoche versiegelt bleiben, Obergrenzen begrenzen die Listengröße, und Autoren-Löschungen entfernen Pins, ohne die Kontrolebenen-Kette zu forken.

## NIP Deep Dive

### Suchfähigkeit (NIP-50)

[NIP-50](/de/topics/nip-50/), definiert in der [primären Spezifikation](https://github.com/nostr-protocol/nips/blob/master/50.md), fügt einen optionalen Suchfilter für Relays hinzu. Gewöhnliche Nostr-Filter funktionieren, wenn ein Client bereits einen Autor, ein Event-Kind, eine Kennung oder einen Tag kennt; NIP-50 adressiert die Discovery, wenn die Eingabe eine menschliche Anfrage wie `best nostr apps` ist.

Das [NIP-50-Wire-Format](https://github.com/nostr-protocol/nips/blob/master/50.md#search-filter-field) fügt einem normalen Filter innerhalb einer `REQ`-Nachricht einen `search`-String hinzu. Eine Anfrage kann dieses Feld mit `kinds`, `authors`, `ids`, Tag-Filtern und `limit` kombinieren, und ein REQ kann mehrere unabhängige Filter tragen. Ein unterstützendes Relay sollte primär gegen den Event-`content` matchen, darf andere Felder nutzen, wenn das Event-Kind dies sinnvoll macht, und sollte nach seinem eigenen Relevanz-Score sortieren, bevor es das `limit` anwendet. Diese Reihenfolge unterscheidet sich vom üblichen Neueste-zuerst-Eventstream.

Der Query-String kann die [`key:value`-Erweiterungen](https://github.com/nostr-protocol/nips/blob/master/50.md#extensions) der Spezifikation enthalten. Sie nennt `include:spam`, `domain:`, `language:`, `sentiment:` und `nsfw:`; ein Relay sollte Erweiterungen ignorieren, die es nicht implementiert. Clients erkennen die deklarierte Unterstützung über das `supported_nips`-Feld des Relays in [NIP-11](/de/topics/nip-11/), können den Filter aber trotzdem an andere Relays senden, wenn sie bereit sind, nicht passende Antworten zu verwerfen.

Die [NIP-50-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/50.md) standardisiert bewusst weder Tokenisierung, Stemming, Ranking, Spracherkennung, Sentiment-Analyse noch Spam-Klassifizierung. Zwei konforme Relays können für dieselbe Anfrage unterschiedliche Events und unterschiedliche Reihenfolgen liefern. Das macht das Relay zu einem Index- und Ranking-Anbieter, nicht zu einer Wahrheitsquelle. Die Spezifikation empfiehlt, mehrere unterstützende Relays abzufragen, zu prüfen, ob die zurückgegebenen Events dem Anwendungsfall des Clients genügen, und Relays mit schlechter Präzision fallen zu lassen.

Das unterscheidet sich vom exakten [NIP-01-Filtern](https://github.com/nostr-protocol/nips/blob/master/01.md). Ein `authors`- oder `#t`-Filter hat deterministische Match-Semantik, die ein Client direkt verifizieren kann, während ein Suchtreffer von einem Index und einem opaken Score abhängen kann. NIP-50 behält den signierten Event-Umschlag und den Relay-Transport von NIP-01 bei, akzeptiert aber Variationen bei Recall und Reihenfolge, um offene Abfragen zu ermöglichen.

Das folgende Event ist ein illustratives Suchergebnis mit den [sieben NIP-01-Event-Feldern](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures). Die wiederholten Hexadezimalwerte sind Platzhalter und keine gültige Signatur.

```json
{
  "id": "0000000000000000000000000000000000000000000000000000000000000000",
  "pubkey": "1111111111111111111111111111111111111111111111111111111111111111",
  "created_at": 1785888000,
  "kind": 1,
  "tags": [["t", "nostr"]],
  "content": "A comparison of Nostr search relays and their indexes.",
  "sig": "22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
}
```

Aktuelle Clients nutzen denselben Filter in unterschiedlichen Discovery-Oberflächen. [Nostria](https://github.com/nostria-app/nostria/blob/d291c2ab091c60c36f99c90241e2fd9da1b0c4bc/src/app/services/relays/search-relay.ts) sendet NIP-50-Suchen an dedizierte Such-Relays, [Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useSearchEvents.ts) sucht Events über seinen Relay-Pool, und [NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/services/orchestration/SearchOrchestrator.ts) koordiniert relay-gestützte Suchen für das Longform-Lesen. Ihre unterschiedliche Ergebnisbehandlung spiegelt den Spielraum wider, den NIP-50 Relays und Clients lässt.

### Highlights (NIP-84)

[NIP-84](/de/topics/nip-84/), definiert durch seine [primäre Spezifikation](https://github.com/nostr-protocol/nips/blob/master/84.md), weist einem Highlight das Kind `9802` zu. Es verwandelt eine ausgewählte Passage oder eine Referenz auf nicht-textuelle Medien in ein signiertes Event, das zwischen Lese-, Social- und Annotations-Clients wandern kann.

Der [`content` des Events](https://github.com/nostr-protocol/nips/blob/master/84.md#format) enthält den ausgewählten Text und kann leer sein, wenn die Quelle Audio, Video oder ein anderes nicht-textuelles Medium ist. Ein Highlight verweist mit einem `a`-Tag auf ein adressierbares Event oder mit einem `e`-Tag auf ein gewöhnliches Event als Nostr-Quelle; ein `r`-Tag identifiziert eine Web-URL. URL-erzeugende Clients sollten Tracking- und andere nutzlose Query-Parameter vor dem Veröffentlichen entfernen, damit kosmetische URL-Varianten Referenzen auf dieselbe Quelle nicht fragmentieren.

Optionale [`p`-Tags](https://github.com/nostr-protocol/nips/blob/master/84.md#attribution) attribuieren die Quelle einer oder mehreren Nostr-Pubkeys. Ihr vierter Wert kann eine Rolle wie `author` oder `editor` angeben, und ein `context`-Tag kann umgebenden Text bewahren, wenn die Auswahl allein unklar wäre. Ein Quote-Highlight fügt stattdessen einen `comment`-Tag hinzu, statt eine zweite Kind-`1`-Notiz zu veröffentlichen: Der `r`-Tag der Quelle erhält die Markierung `source`, während im Kommentar erwähnte Pubkeys oder URLs `mention` tragen, sodass Renderer Attribution von der Antwort des Nutzers unterscheiden können.

Die [Kind-`9802`-Definition](https://github.com/nostr-protocol/nips/blob/master/84.md) macht ein Highlight zu einem regulären statt einem ersetzbaren Event. Das Wiederholen oder Korrigieren einer Auswahl erzeugt ein weiteres signiertes Event, und das Entfernen hängt vom normalen Löschanfrage-Fluss und der Aufbewahrungspolitik des Relays ab. Die Spezifikation definiert keine Byte-Offsets, Selektoren oder einen kanonischen Dokumenten-Snapshot, sodass ein Client eine Passage nach einer Änderung ihrer Web-Quelle möglicherweise nicht wiederfindet. Öffentliche Highlights offenbaren außerdem Leseinteressen; private Annotation erfordert ein separates Verschlüsselungs- und Sharing-Design.

NIP-84 unterscheidet sich von einem [NIP-23-Longform-Event](https://github.com/nostr-protocol/nips/blob/master/23.md), das einen ganzen Artikel als Kind `30023` veröffentlicht; ein Highlight zitiert oder zeigt in Material, das anderswo verbleiben kann. Es unterscheidet sich auch von einem [NIP-51-Lesezeichen-Set](https://github.com/nostr-protocol/nips/blob/master/51.md), das eine ersetzbare Sammlung von Referenzen speichert. NIP-84 macht jede Auswahl unabhängig signiert, attribuierbar, auffindbar und diskutierbar.

Dieses illustrative Highlight enthält die [sieben NIP-01-Event-Felder](https://github.com/nostr-protocol/nips/blob/master/01.md#events-and-signatures). Seine Kennung und Signatur sind Platzhalter.

```json
{
  "id": "3333333333333333333333333333333333333333333333333333333333333333",
  "pubkey": "4444444444444444444444444444444444444444444444444444444444444444",
  "created_at": 1785888000,
  "kind": 9802,
  "tags": [
    ["a", "30023:6666666666666666666666666666666666666666666666666666666666666666:relay-search", "wss://relay.example"],
    ["p", "6666666666666666666666666666666666666666666666666666666666666666", "wss://relay.example", "author"],
    ["context", "Search relays are indexes whose ranking policies can differ."]
  ],
  "content": "ranking policies can differ",
  "sig": "55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555"
}
```

Das Format überschreitet bereits Client-Grenzen. [nostrord 2.5.0](https://github.com/nostrord/nostrord/releases/tag/v2.5.0) hat diese Woche NIP-84-Rendering hinzugefügt, [NoorNote](https://github.com/77elements/noornote/blob/bf1f9b431552497dc1779ea0d8fed2c3c28e6070/src/components/ui/note-rendering/HighlightRenderer.ts) rendert Highlight-Events in seinem Longform-Client, und [Ditto](https://github.com/soapbox-pub/ditto/blob/04adb2d242ab6f5807fd27ae3e0cb9beab091641/src/hooks/useCreateHighlight.ts) veröffentlicht sie aus ausgewählten Inhalten. Diese Implementierungen decken Lesen, Erstellen und Social-Rendering ab, ohne dass ein einzelner Dienst die Annotation besitzen muss.

---

Sende eine NIP-17-DM, um ein Projekt oder eine Nachricht über das [Nostr-Compass-Projekt](https://github.com/andotherstuff/nostr-compass) zu teilen.
