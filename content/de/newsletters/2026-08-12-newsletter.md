---
title: "Nostr Compass #35"
date: 2026-08-12
publishDate: 2026-08-12
translationOf: /en/newsletters/2026-08-12-newsletter.md
translationDate: 2026-08-12
draft: false
type: newsletters
description: "Post-Quanten-Identitätstools, stärkere verschlüsselte Nachrichten und Signierung, portable Community-Einstellungen und Protokollarbeit über NIPs und Concord hinweg."
---

Willkommen zurück bei [Nostr Compass](https://nostrcompass.org), eurem wöchentlichen Wegweiser für Nostr.

**Diese Woche:** [nostr-wot-extension](https://github.com/nostr-wot/nostr-wot-extension) fügt Post-Quanten-Schlüssel und optional geschützte Nachrichten neben bestehenden Nostr-Identitäten hinzu. [Divine](https://github.com/divinevideo/divine-mobile) verschärft Kontoisolation, Validierung privater Nachrichten und Veröffentlichungsbestätigung; [MDK](https://github.com/marmot-protocol/mdk) stärkt Konvergenz und Wiederherstellung verschlüsselter Gruppen; und [Amber](https://github.com/greenart7c3/Amber) macht gruppierte Signierentscheidungen explizit. Releases verbessern Wallet-Verbindungen, verschlüsselten Chat, soziale Discovery, Gerätesynchronisation und Remote-Signing, während die Protokollarbeit Identität und verschlüsselte Communities abdeckt. Die Deep Dives erklären authentifizierte Löschanfragen und dezentrale Meldungen.

## Top-Storys

### nostr-wot-extension 0.4.0 fügt Post-Quanten-Schlüssel neben einer Nostr-Identität hinzu

[nostr-wot-extension 0.4.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.4.0) ist eine Browser-Erweiterung zum Verwalten von Nostr-Identitäten und zum Signieren. Konten, die aus einem 24-Wort-Seed erstellt wurden, können nun ML-KEM-1024-Verschlüsselungs- und ML-DSA-87-Signierschlüssel neben ihrem bestehenden Nostr-Schlüssel ableiten. Ein Ein-Klick-Ablauf veröffentlicht eine Attestierung des Kinds `10203`, die den Nostr-Public-Key an beide Post-Quanten-Public-Keys bindet und einen ML-DSA-Besitznachweis enthält. Konten, die aus einer 12-Wort-Mnemonik, einem bloßen `nsec`, einem Remote-Signer oder einem schreibgeschützten Schlüssel importiert wurden, können den Ableitungsablauf nicht nutzen, und die Erweiterung erklärt diese Einschränkung in der Kontenansicht.

Das Release fügt außerdem optionale Post-Quanten-Direktnachrichten hinzu. Es kombiniert das ML-KEM-gemeinsame Geheimnis mit dem bestehenden [NIP-44-Verschlüsselungs-Gesprächsschlüssel](https://github.com/nostr-protocol/nips/blob/master/44.md) über HKDF und behält die normalen NIP-59-Metadaten-verbergenden Gift-Wrap-Schichten für die Relay-Zustellung bei. Die Verschlüsselung fällt nach der Opt-in-Entscheidung eines Empfängers nie stillschweigend zurück, während die Entschlüsselung automatisch den passenden Pfad wählt. Das schützt den neuen Nachrichtenpfad vor späterer Wiederherstellung eines heutigen Nostr-Private-Keys, ersetzt aber keine secp256k1-Event-Signaturen; das Release überlässt diese größere Migration ausdrücklich künftiger Abstimmung mit Relays und Clients.

### Divine Mobile 1.0.19 verschärft Konten, private Nachrichten und Veröffentlichung

[Divine Mobile 1.0.19](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.19) ist ein mobiler Kurzvideo-Client, der Videos über Nostr veröffentlicht und abruft. Sein Kontowechsler baut jede angemeldete Identität nun um einen kontobezogenen Container herum auf, und eine Veröffentlichungskorrektur verhindert, dass ein Video unter dem falschen Konto gesendet wird. Relay-Veröffentlichungspfade warten nun auf eine `OK`-Antwort mit expliziter Erfolgssemantik, während ein Relay-`CLOSED`-Frame seine eigene ausstehende Abfrage beenden kann, statt die Anfrage hängen zu lassen.

Die [Behandlung privater Nachrichten](https://github.com/divinevideo/divine-mobile/pull/6368) lehnt nicht authentifizierte Rumor-Felder und unsignierte Seals ab, stellt vier Fälle fehlender Nachrichten wieder her und leitet Gruppenunterhaltungen vollständig gefolgter Teilnehmer in den Posteingang. Das Release bewahrt außerdem die Tags adressierbarer Video-Events, wenn Listen aktualisiert werden, und verarbeitet beobachtete Löschanfragen, sodass entfernte Videos aus dem lokalen Zustand verschwinden. Diese Änderungen folgen der Arbeit an pro-Relay-Abfrage-Timeouts aus der letzten Woche, verlagern den Fokus aber von Abrufisolation zu Identitätsgrenzen, Nachrichtenvalidierung und Veröffentlichungsbestätigung.

### MDK 0.9.11 härtet Marmot-Gruppenkonvergenz und -wiederherstellung ab

[MDK 0.9.11](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.11) ist ein Rust-Entwicklungskit für Marmot, ein verschlüsseltes Gruppennachrichtenprotokoll über Nostr. Das Release baut ein größeres Konvergenz- und Wiederherstellungssystem um die Gruppenzustandsmaschine: veraltete Konvergenzdurchläufe öffnen wieder am aktuellen Gruppentip, eingehende Capability-Projektionen committen atomar, zurückgestellte Nachrichten erhalten begrenzte Lebensdauern über Neustarts hinweg, und commit-adressierte Checkpoints helfen, eigene Commit-Forks einer Identität wiederherzustellen. Nicht stabile Sends können in die Warteschlange gelegt und wiederhergestellt werden, während ein Epochen-Stall-Pfad zu Backfill eskaliert und gesendete Nachrichten Konvergenzarbeit überleben.

[Speicher- und Host-Integrationen](https://github.com/marmot-protocol/mdk/pull/1201) erhalten eine parallele Härtung. MDK löscht beschnittene SQLite-Projektionen sicher, nullt importierte Private Keys, NIP-49-verschlüsselte Schlüssel-Export-Zwischenstände und OpenMLS-Serialisierungspuffer und redigiert Gruppenbildschlüssel aus Debug-Ausgaben. Kontenimport kann nach Unterbrechung fortgesetzt werden, iOS- und Android-Privatspeicherpfade sind repariert, und Hosts können Speicher vor dem Suspendieren explizit schließen. Neue leichtgewichtige Roster- und lokale Mitgliedschaftsprojektionen reduzieren, was Anwendungen lesen müssen, während der Hermes-Connector mehrere agentengenerierte Bilder als ein Marmot-Album zustellen kann.

### Nostria 4.1.67 erweitert die Verwaltung verschlüsselter Communities

[Nostria 4.1.67](https://github.com/nostria-app/nostria/releases/tag/v4.1.67) ist ein Web- und Desktop-Social-Client für Nostr. Er baut auf den experimentellen NIP-29-relay-verwalteten Gruppen und Concord-verschlüsselten Communities auf, die in 4.1.53 eingeführt wurden, und fügt Community-Auflösung, Icon- und Banner-Verwaltung, verschlüsselte Foto-Uploads mit komprimierten Vorschauen, einen vollständigen Reaktions-Picker und ein Dual-Pane-Layout hinzu, das eine Community geöffnet hält, während der Nutzer Notizen oder Artikel liest. Das Release fügt außerdem Thread-Nachrichten und einen kombinierten Hub für öffentliche, Gruppen- und private Chats hinzu.

### Amber 6.4.0 macht jede gruppierte Signierentscheidung explizit

[Amber 6.4.0](https://github.com/greenart7c3/Amber/releases/tag/v6.4.0) ist ein Android-Signer, der Nostr-Private-Keys von den Signaturen anfordernden Anwendungen trennt. Sein neu gestalteter Multi-Request-Bildschirm bietet Approve- und Deny-Steuerungen für jede Anfrage und jede Gruppe und ersetzt den bisherigen Auswahl-und-Bestätigen-Ablauf. Abgelehnte Anfragen, die über Ambers relay-vermittelte Bunker-Schnittstelle gesendet werden, erhalten nun ordentliche Fehlerantworten, sodass der anfragende Client Ablehnung von einem hängenden Signer unterscheiden kann.

[Ambers getaggte Quelle](https://github.com/greenart7c3/Amber/tree/v6.4.0) fügt außerdem lokalisierte, menschenlesbare Labels für 113 weitere Event-Kinds in jeder ausgelieferten Locale hinzu. Die Ergänzungen umfassen Concord-Gruppen-Events, NIP-51-Git-Repository-Lesezeichen und NIP-53-Raum-Präsenz-Events und geben Nutzern mehr Kontext über unbekannte Daten, bevor sie eine Signatur genehmigen. Eine Concurrent-Map-Absicherung behebt außerdem einen Relay-Abonnement-Absturz, der eine `NegativeArraySizeException` auslösen konnte.

### Safebox Acorn trennt eine portable Wiederherstellungskomponente von der Web-App

[Safebox Acorn](https://github.com/trbouma/safebox-acorn) ist eine eigenständige Python-Komponente und Command-Line-Schnittstelle zum Schutz nutzerkontrollierter Schlüssel, Mittel und Datensätze mit Nostr-gestütztem Zustand. Das Auslagern von Acorn aus der breiteren Safebox-Webanwendung lässt ein anderes Python-Projekt die Runtime installieren und deren Schlüssel-, Nostr-Profil-, Relay-, Record-, Cashu-, Lightning- und kryptografische Helfer nutzen, ohne die Web-Oberfläche mitzunehmen. Ihre aktuellen Record-Schutz-Primitive können einen frischen 256-Bit-Schlüssel erzeugen, einen aus separat gelieferter Entropie ableiten und den exakten Schlüssel als checksummte 24-Wort-Wiederherstellungsphrase kodieren.

Der [Wiederherstellungs- und Kontinuitätsleitfaden](https://trbouma.github.io/safebox-acorn/recovery-and-continuity/) des Projekts rahmt Acorn als austauschbare Protokollkomponente innerhalb einer Haushalts- oder Community-Safebox. Das Design hält verschlüsselten Zustand über ein lokales Relay und unabhängige Replikas verfügbar, sodass Wiederherstellung nicht von einem Gerät, einer Anwendung, einem Relay, einer Mint oder einem Dienstanbieter abhängt. Die Dokumentation ist vorsichtig mit der gegenwärtigen Grenze: Verschlüsselung geschützter Records ist noch in Planung, daher sollten Anwendungen Records nicht vom neuen Record-Schutz-Schlüssel abhängig machen, bis dieses Profil implementiert und geprüft wurde.


## Releases

### Mostro Core 0.14.2 ändert den verschlüsselten Chat-Umschlag

[Mostro Core](https://github.com/MostroP2P/mostro-core) ist die Rust-Bibliothek gemeinsamer Typen und Peer-to-Peer-Funktionen, die vom Mostro-Exchange-Daemon und seinen Clients genutzt wird. [Version 0.14.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.2) ersetzt gift-wrapped Chat-Nachrichten durch Kind-14-Umschläge, die separate Gesprächsverschlüsselungs- und Signierschlüssel aus dem gemeinsamen Geheimnis der Peers ableiten. Der neue Reader validiert Autor, Signatur, Empfänger, Zeitstempel und Inhaltsgröße, während Legacy-Gift-Wrap-Helfer verfügbar bleiben, damit Clients während der Migration beide Formate lesen können.

### Mostro 0.18.1 startet einen Cashu-Escrow-Pfad und härtet den Daemon ab

[Mostro](https://github.com/MostroP2P/mostro) ist ein Peer-to-Peer-Lightning-Exchange-Daemon, der Orders über Nostr koordiniert. [Version 0.18.1](https://github.com/MostroP2P/mostro/releases/tag/v0.18.1) legt die Grundlage für ein Cashu-Escrow-Backend, einschließlich Konfiguration, Datenbankhelfern, Mint-Integration, Startup-Verdrahtung und der ersten Lock-Aktion. Er kann außerdem Preise nutzen, die ein vertrauenswürdiger Node über Nostr ankündigt, und wirbt Proof-of-Work-Anforderungen für den Erstkontakt in seinem ersetzbaren Info-Event aus. Das Release aktualisiert seine Nostr-Abhängigkeit für einen NIP-44-Denial-of-Service-Fix, entfernt Private Keys aus Restore-Session-Logs, lehnt nicht autorisierte kooperative Stornierungsnachrichten ab, härtet LNURL-Abrufe gegen serverseitige Request-Forgery und Hänger ab, validiert Auszahlungs-Invoices und stellt Hold-Invoice-Abonnements nach einem Neustart wieder her.

### LaWallet NWC 2.3.0 fügt Nostr-Benachrichtigungen und Zap-Receipts hinzu

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc) ist eine Open-Source-Lightning-Address-Plattform, die Wallets über [Nostr Wallet Connect](/de/topics/nip-47/) verbindet. [Version 2.3.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.3.0) lässt jede Wallet empfangene und weitergeleitete Benachrichtigungen als konfigurierbare Nostr-Events senden, einschließlich eines Empfänger-`p`-Tags, ausgewählter Relays, templatisierter Inhalte und optionaler [NIP-44](/de/topics/nip-44/)-Verschlüsselung; Wiederholungen nutzen dieselbe signierte Event-ID. Er akzeptiert außerdem Zap-Anfragen und veröffentlicht nach der Abwicklung signierte [NIP-57](/de/topics/nip-57/)-Kind-9735-Receipts, während eine neue Address-Capability-Ansicht zeigt, ob die aufgelöste Adresse NIP-05, NIP-57 und verwandte Lightning-Address-Protokolle unterstützt.

### nostr-double-ratchet TypeScript 0.0.166 bindet öffentliche Einladungen an Session-Keys

[nostr-double-ratchet](https://github.com/irislib/nostr-double-ratchet) stellt TypeScript- und Rust-Primitive für Ende-zu-Ende-verschlüsselte Direkt- und Gruppennachrichten über Nostr-Relays bereit. [TypeScript 0.0.166](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.166) verlangt, dass eine Einladungsantwort den Besitz ihres Session-Keys nachweist, und verhindert so, dass eine wiederverwendbare öffentliche Einladung eine Nostr-Identität an die Session einer anderen Partei bindet. Das Release lehnt außerdem fehlerhafte Rumor-Felder ab und verschärft die Payload-Validierung; bestehende Sessions funktionieren weiter, aber ein aktualisierter Einladender lehnt beweislose Antworten älterer Eingeladener ab.

### cln-nip47 0.2.0 erweitert und isoliert NWC-Anfragen

[cln-nip47](https://github.com/daywalker90/cln-nip47) ist ein Core-Lightning-Plugin, das einen Node Wallets über [Nostr Wallet Connect](/de/topics/nip-47/) bereitstellt. [Version 0.2.0](https://github.com/daywalker90/cln-nip47/releases/tag/v0.2.0) fügt NWC-Methoden zum Erstellen, Stornieren und Abwickeln von Hold-Invoices plus eine `hold_invoice_accepted`-Benachrichtigung hinzu und wirbt die Methodenmenge aus, die der verbundene Node tatsächlich unterstützt. Transaktionslisten-Antworten enden nun bei 500 Einträgen und etwa 128 kB, Anfrage-Events werden nach Event-ID dedupliziert, und die fehlgeschlagene Benachrichtigung eines Clients verhindert nicht mehr die Zustellung an andere Clients. Das Release entfernt außerdem die beiden Multi-Payment-Methoden, die nicht mehr Teil der NWC-Spezifikation sind.

### ClipRelay 0.1.3 stellt Relay- und Signer-Verbindungen nach Leerlaufphasen wieder her

[ClipRelay](https://github.com/tajava2006/cliprelay) synchronisiert die Zwischenablage eines Nutzers zwischen Geräten über Nostr-Relays und verschlüsselt den Inhalt für dieselbe Identität mit [NIP-44](/de/topics/nip-44/). Die passenden [Desktop-](https://github.com/tajava2006/cliprelay/releases/tag/desktop/v0.1.3)- und [Android-](https://github.com/tajava2006/cliprelay/releases/tag/android/v0.1.3)-Releases in Version 0.1.3 fügen ein Textfeld hinzu, um getippten Text direkt in die Zwischenablage eines anderen Geräts zu senden. Sie testen außerdem die Lebendigkeit mit echten Relay-Roundtrips nach Leerlaufphasen, eskalieren von erneuter Abonnement bis zu Socket-Ersatz und einem neu aufgebauten Verbindungspool, während hängende [NIP-46](/de/topics/nip-46/)-Signer-Aufrufe nun time-outen und automatisch neu aufgebaut werden.

### NoorNote 1.3.2 verlagert Artikel-Discovery in den Social Graph

[NoorNote](https://github.com/77elements/noornote) ist ein Nostr-Client für Social Posts, verschlüsselte Nachrichten, Longform-Artikel und andere Event-Typen für Web, Desktop und Android. [Version 1.3.2](https://github.com/77elements/noornote/releases/tag/v1.3.2) ersetzt seinen flachen globalen Artikel-Feed durch Discovery aus Kontakten ersten, zweiten und dritten Grades und gibt Lesern eine am Follow-Graph verwurzelte Artikel-Timeline. Er fasst außerdem Stöße wiedergegebener Direktnachrichten unbekannter Absender zu einer rollierenden Benachrichtigung zusammen, statt einen Stapel Toasts zu erzeugen, wenn Relay-Historie eintrifft.

### Bray 2.4.0 fügt einen kompakten Remote-Signing-Dialekt hinzu

[Bray](https://github.com/forgesworn/bray) ist ein Nostr-MCP-Server, der Software-Agenten und Menschen Werkzeuge für Relay-Zugriff, Identität, Veröffentlichung und Remote-Signing gibt. [Version 2.4.0](https://github.com/forgesworn/bray/releases/tag/v2.4.0) akzeptiert eine Signieranfrage, deren Event ein Objekt ist, sowie die von [NIP-46](/de/topics/nip-46/) genutzte stringifizierte Form, und fügt `sign_event_compact` hinzu, das nur Event-ID, Signatur, Public Key und Zeitstempel zurückgibt. Dieses kleinere Anfrage- und Antwortformat reduziert den Speicherverbrauch für ressourcenarme Hardware-Signer, während der Standard-`sign_event`-Ablauf unverändert bleibt und beide Dialekte eine Signatur über die ID des empfangenen Events erzeugen.


## Neu entdeckt

### Pact bringt gegenseitig zugestimmte Agent-Bindungen nach Nostr

[Pact](https://github.com/bobodread876/pact), diese Woche neu entdeckt, ist eine frühe Beziehungsebene für Software-Agenten, aufgebaut auf MATE.md und einem NIP-BD-Transport-Entwurf. Seine signierten, gegenseitig zugestimmten Bindungen werden von den eigenen Schlüsseln der Agenten gehalten und können über Nostr veröffentlicht werden, während private Bindungen [NIP-59](/de/topics/nip-59/)-Gift-Wrapping nutzen. Das Monorepo umfasst einen MCP-Server, ein TypeScript-SDK, einen Command-Line-Client, einen selbst hostbaren Daemon und eine Web-Oberfläche. Seine jüngste Repository-Aktivität liegt vor dem wöchentlichen Fenster dieser Ausgabe, daher ist dies ein Discovery-Hinweis und kein Anspruch auf ein neues Release.


## Unveröffentlichte Änderungen

### nostrord hält Gruppen-Stummschaltung zwischen Geräten synchron

[nostrord](https://github.com/nostrord/nostrord) ist ein plattformübergreifender Client für relay-verwaltete Communities. [PR #250](https://github.com/nostrord/nostrord/pull/250) speichert die Stummschaltungsentscheidungen eines Kontos pro Gruppe in einem selbst verschlüsselten [NIP-78](/de/topics/nip-78/)-Kind-`30078`-Event (anwendungsspezifische Daten), sodass eine auf einem Gerät getroffene Einstellung dem Nutzer auf ein anderes folgen kann, ohne die Gruppenliste dem Relay preiszugeben. Der ersetzbare Datensatz nutzt Neueste-Event-Reihenfolge, lauscht auf Live-Änderungen und rollt die Oberfläche zurück, wenn Signieren oder Veröffentlichen fehlschlägt, statt den lokalen Zustand desynchron zu lassen. Stummgeschaltete Gruppen tragen nicht mehr zu sichtbaren Ungelesen-Summen bei, behalten aber ihre Ungelesen-Position für den nächsten Besuch.

### Amethyst schließt Concords Einladungs-Lebenszyklus ab

[Amethyst](https://github.com/vitorpamplona/amethyst) ist ein Android-Nostr-Client, dessen Unterstützung verschlüsselter Communities das Concord-Protokoll implementiert. [PR #3888](https://github.com/vitorpamplona/amethyst/pull/3888) lässt Einladungslinks eine Community-Neugründung überleben, indem ihre Bundles an denselben adressierbaren Koordinaten neu ausgestellt werden, während eine Ban-Prüfung verhindert, dass ein entferntes Mitglied diesen Wiederherstellungspfad nutzt. Er implementiert außerdem die verschlüsselte CORD-05-Einladungsliste sowohl in der App als auch im `amy`-Command-Line-Client, fügt pro Link Widerrufs-Tombstones hinzu und verlangt Relay-Bestätigung, bevor der einzige gespeicherte Signierschlüssel gelöscht wird, der einen Link stilllegen kann. Dieselbe Arbeit gibt `amy` die Control-Key-Zustellung, Neugründung, Rekeying und Wiederherstellungspfad für gestrandete Mitglieder, die spätere Community-Epochen folgen müssen.

### Buzz trägt das Erscheinungsbild jeder Community über Desktop und Mobile

[Buzz](https://github.com/block/buzz) ist ein Nostr-basierter Community-Workspace mit Desktop- und Mobile-Clients. Gemergte Desktop-[PR #3653](https://github.com/block/buzz/pull/3653) und Mobile-[PR #3767](https://github.com/block/buzz/pull/3767) speichern Theme, Akzent und Systemmodus-Wahl jeder Community als verschlüsselten NIP-78-Datensatz auf dem Relay dieser Community. Beide Clients teilen dieselbe versionierte Payload und halten identitätsbezogene lokale Caches, sodass Community- oder Kontowechsel nicht das falsche Erscheinungsbild anwenden können, während das Relay nicht verfügbar ist. Ersatz-Reihenfolge, abgesicherte Schreibvorgänge und erneute Abonnement nach geschlossener Verbindung lassen die beiden Clients nach dem Wiederverbinden wieder konvergieren.

[Buzz Desktop 0.5.10](https://github.com/block/buzz/releases/tag/desktop-v0.5.10) folgte vor dem Issue-Cutoff mit einem Performance- und Zuverlässigkeitsdurchlauf. Er entfernt Regressionen nach 0.5.9, beschleunigt das Laden von Kanälen, begrenzt die anfängliche Timeline-Aufbewahrung, bündelt Read-State-Persistenz, bewahrt frische Kanal-Timelines und verhindert, dass der Relay-Ingest-Worker bei Reaktionen auf Projekt-Events abstürzt. Er fügt außerdem das Senden einer Thread-Nachricht an einen Kanal hinzu und grenzt die Desktop-Suche auf den beabsichtigten Umfang ein.


## NIP-Updates und Protokoll-Spezifikationsarbeit

### NIPs

[NIPs PR #2435](https://github.com/nostr-protocol/nips/pull/2435) ist eine offene Änderung an NIP-34, das Git-Repository-Zusammenarbeit über Nostr-Events standardisiert. Sie fügt einem Pull-Request-Event einen optionalen `b`-Tag hinzu, damit der Autor einen Zielbranch außerhalb des Repository-Defaults benennen kann. Der Vorschlag entspricht Unterstützung, die bereits in ngit und GitWorkshop implementiert ist, ist aber noch nicht in die Spezifikation aufgenommen.

[NIPs PR #2434](https://github.com/nostr-protocol/nips/pull/2434) ist ein offener Vorschlag für Post-Quanten-Identitätsschlüssel. Er leitet Post-Quanten-Verschlüsselungs- und Signierschlüssel neben dem bestehenden secp256k1-Schlüssel aus einem NIP-06-Mnemonik-Schlüsselableitungs-Seed ab und bindet die Public Keys dann mit einer Attestierung des Kinds `10203` an die Nostr-Identität. Der Entwurf beschränkt seinen Anspruch darauf, die Vertraulichkeit früherer Nachrichten zu schützen, falls secp256k1 später bricht; er ersetzt nicht die heutigen Event-Signaturen.

[NIPs PR #2431](https://github.com/nostr-protocol/nips/pull/2431) ist eine offene NIP-07-Änderung für Browser-Signer. Ein Client könnte den Public Key, den er erwartet, Signier- oder Verschlüsselungsanfragen anhängen und den Signer verpflichten, dieses Konto zu nutzen oder den Aufruf abzulehnen. Das würde verhindern, dass eine Seite stillschweigend unter einer anderen Identität weitermacht, nachdem der Nutzer im Signer das Konto gewechselt hat.

[NIPs PR #1813](https://github.com/nostr-protocol/nips/pull/1813) bleibt nach substantieller Arbeit im Fenster ein offener Double-Ratchet-Vorschlag. Er spezifiziert forward-secret verschlüsselte Unterhaltungen, deren Schlüssel sich mit Nachrichten weiterentwickeln, mit einer Implementierung, die bereits in der nostr-double-ratchet-Bibliothek und Iris verfügbar ist. Er ist weiterhin ein Entwurf, kein gemergtes NIP.

[NIPs PR #2433](https://github.com/nostr-protocol/nips/pull/2433) wurde im Fenster geöffnet und ohne Merge geschlossen. Er schlug vor, NIP-42-Relay-Fehler zu klären, sodass `auth-required` bedeuten würde, dass eine weitere Authentifizierung das Ergebnis ändern könnte, während `restricted` bedeuten würde, dass dies nicht möglich ist. Die Unterscheidung adressierte Verbindungen, die für einen Schlüssel authentifiziert waren, aber für einen anderen noch keine Autorisierung hatten; der geschlossene Status bedeutet, dass die Formulierung nicht in die Spezifikation aufgenommen wurde.

[NIPs PR #2378](https://github.com/nostr-protocol/nips/pull/2378), zuvor noch als Vorschlag behandelt, ist nun ohne Merge geschlossen. Seine vorgeschlagenen Agent-Passports, Discovery-, Task-, Marketplace-, Invoice- und Connection-Events bleiben daher außerhalb des NIP-Sets.

[NIPs Commit 656cecc](https://github.com/nostr-protocol/nips/commit/656cecc7c0a815b6a2b218d3b5d6f078b3f4dbab) hat eine rein dokumentarische Korrektur an NIP-29 gemergt. Er fügt dem Gruppenmetadaten-Beispiel einen `previous`-Tag hinzu und zeigt, wie ein Ersatz-Event das Event identifizieren kann, das es ersetzt. Das klärt ein Beispiel und führt kein neues Protokollfeature ein.

### Concord und CORDs

[CORD PR #18](https://github.com/concord-protocol/concord/pull/18) würde verschlüsselte Community Lists über Kind-`33302`-Events sharden, das 50-Mitgliedschafts-Limit entfernen und ausgeschiedene Einträge beschneiden, um Relay-Limits einzuhalten. Zwei weitere offene Vorschläge fügen [private Mention-Locators](https://github.com/concord-protocol/concord/pull/16) und ein [Pause-Signal](https://github.com/concord-protocol/concord/pull/17) hinzu, das Chat aussetzt, ohne Nachrichten zu verwerfen.

[CORD-02 PR #15](https://github.com/concord-protocol/concord/pull/15) wurde am 6. August gemergt und beschränkt Schreibvorgänge auf die Kontrollebene einer Community. Owner und Staff halten ein neues `control_root`-Signiergeheimnis, während alle Mitglieder den abgeleiteten Public Key und Read Key behalten, die Moderationszustand verifizieren und entschlüsseln. Der Write Key ist eine Spam-Barriere, kein Ersatz für die inneren Actor-Signaturen und Roster-Prüfungen, die Autorität etablieren.

[CORD PR #12](https://github.com/concord-protocol/concord/pull/12), zuvor als offener Entwurf behandelt, ist nun ohne Merge geschlossen. Sein Kontrollebenen-Anteil wurde durch die engere gemergte CORD-02-Änderung oben ersetzt, während restricted-write-Kanäle und das übrige Entwurfsmaterial nicht in die Spezifikation aufgenommen wurden.

## NIP Deep Dive

### Event-Löschanfragen (NIP-09)

[NIP-09](/de/topics/nip-09/), definiert in der [primären Spezifikation](https://github.com/nostr-protocol/nips/blob/master/09.md), gibt einem Event-Autor einen signierten Weg, Relays und Clients zu bitten, eines oder mehrere Events dieses Autors nicht mehr auszuliefern. Es löscht nicht jede Kopie. Es trägt die Absicht des Autors durch dasselbe Relay-Netzwerk, das das ursprüngliche Event verteilt hat.

Die Anfrage ist ein gewöhnliches signiertes Kind-`5`-Event. Seine Tags enthalten eine oder mehrere `e`-Referenzen auf konkrete Event-IDs oder `a`-Referenzen auf adressierbare Event-Koordinaten, und die [NIP-09-Tag-Regeln](https://github.com/nostr-protocol/nips/blob/master/09.md#event-deletion-request) sagen, dass für jedes referenzierte Event-Kind ein `k`-Tag enthalten sein sollte. Der optionale `content` kann den Grund erklären. Für eine `a`-Referenz sollte ein Relay jede Version an dieser Koordinate entfernen, deren Zeitstempel nicht später als `created_at` der Anfrage ist, was verhindert, dass eine alte Löschanfrage eine spätere Ersetzung unterdrückt.

[Autorschaft ist die Sicherheitsgrenze](https://github.com/nostr-protocol/nips/blob/master/09.md#relay-behavior). Ein Relay sollte ein referenziertes Event nur dann nicht mehr veröffentlichen, wenn sein `pubkey` dem `pubkey` der Löschanfrage entspricht, und ein Client muss diese Prüfung durchführen, bevor er ein Event ausblendet. Ein Relay besitzt das referenzierte Event möglicherweise nicht und kann die Beziehung daher bei Annahme der Anfrage nicht validieren, sodass Clients Relay-Annahme nicht als Beweis behandeln können, dass die Löschung autorisiert war. Die Spezifikation bittet Relays außerdem, die Kind-`5`-Anfrage aufzubewahren, weil ein anderer Client das ursprüngliche Event bereits halten und die Anfrage später sehen kann.

Hier ist ein [signiertes Kind-`5`-Event](https://primal.net/e/6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943):

```json
{
  "id": "6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943",
  "pubkey": "5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743",
  "created_at": 1786465675,
  "kind": 5,
  "tags": [
    ["e", "f3d47f8b813928c5baf7ac993846be0220dc37a2e7c7b128fb49a4b92711f131"],
    ["k", "30091"],
    ["a", "30091:5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743:survey:0ad5cebc-608b-47d7-97fd-9e6c47787199"],
    ["t", "nostr-survey"]
  ],
  "content": "Public survey summary deleted during privacy refresh",
  "sig": "846be83b038dc5f91af0c9d03a4ac81aff9bc4cfde7d85c849fa2fdae890f75cc444a4072f45aa18883b0b3871e15381b220182d6e366892f0c9c6f9c0557244"
}
```

Löschung bleibt eine kooperative Policy, keine Widerrufung eines signierten Objekts. Ein Relay, Cache, Screenshot oder Offline-Client kann die ursprünglichen Bytes bewahren, und das Löschen der Kind-`5`-Anfrage selbst macht sie nicht rückgängig. Clients können das Ziel ausblenden, als disowned markieren oder den Anfragegrund anzeigen, sollten Nutzern aber sagen, dass universelle Löschung nicht garantiert werden kann. Das unterscheidet sich von [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md), wo ein `expiration`-Tag Relays bittet, ein Event nach einer beim Veröffentlichen gewählten Zeit nicht mehr zu speichern. NIP-09 behandelt eine spätere Autorenentscheidung und kann auf bereits verteilte Events zeigen.

Aktuelle Implementierungen wenden diese Policy auf unterschiedlichen Ebenen an. [Divine PR #6623](https://github.com/divinevideo/divine-mobile/pull/6623) entfernt gelöschte Videos aus dem Event-Store des Clients, [strfry PR #251](https://github.com/hoytech/strfry/pull/251) erweitert gültige Löschanfragen auf Gift-Wrap-Empfänger, und [Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md) deklariert NIP-09-Unterstützung in seinem Client. [nostrords Gruppenclient](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/network/NostrGroupClient.kt) liefert einen weiteren aktuellen Implementierungspfad.

### Meldungen (NIP-56)

[NIP-56](/de/topics/nip-56/), definiert in der [primären Spezifikation](https://github.com/nostr-protocol/nips/blob/master/56.md), standardisiert eine signierte Meldung über ein Konto, ein Event oder einen referenzierten Blob. Sie trennt das Meldungssignal von der Moderationsentscheidung und erlaubt jedem Client oder Relay zu wählen, welchen Meldenden es vertraut und welche Reaktion zu seiner Policy passt.

Eine Meldung nutzt Kind `1984` und muss das gemeldete Konto in einem `p`-Tag identifizieren. Die Meldung einer Notiz erfordert außerdem ein `e`-Tag für die Event-ID. Der dritte Wert des Tags trägt eine der spezifizierten Kategorien: `nudity`, `malware`, `profanity`, `illegal`, `spam`, `impersonation` oder `other`. Eine Meldung über einen Blob kann seinen Hash in einem `x`-Tag, ein `e`-Tag für das Event, das den Blob referenzierte, und optional ein `server`-Tag für einen Ort nutzen. Optionale `L`- und `l`-Tags aus [NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) können ein namespaced Label hinzufügen, wenn die feste Kategorieliste nicht präzise genug ist.

[Das Event beweist nur, dass ein Schlüssel eine Behauptung aufgestellt hat](https://github.com/nostr-protocol/nips/blob/master/56.md#reporting). Der gemeldete Inhalt wird nicht falsch, illegal oder entfernbar allein deshalb, weil ein gültiges Kind `1984` existiert, und ein offenes Relay kann anonyme Meldungen nicht sicher als Stimmen zählen. Die Spezifikation rät von automatischer Relay-Moderation ab, weil Meldungen leicht zu manipulieren sind, erlaubt Relay-Administratoren aber, auf Meldungen von Moderatoren zu reagieren, denen sie bereits vertrauen. Ein Client kann Meldungen stattdessen über den Social Graph eines Nutzers gewichten, etwa indem er Inhalte verwischt, nachdem mehrere vertrauenswürdige Kontakte dasselbe Konto markiert haben.

Hier ist ein [signiertes Kind-`1984`-Event](https://primal.net/e/17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2):

```json
{
  "id": "17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2",
  "pubkey": "1ff02fb5cdc633c1be55368ab655490ec25d2f5dc2e364d4703bc3196d99eab1",
  "created_at": 1786465319,
  "kind": 1984,
  "tags": [
    ["p", "3a72b02cc05ee07310dc580874b6a9ca8271c6518b90655bd2e98003c9601e68", "impersonation"]
  ],
  "content": "",
  "sig": "6362e415410feb19e0505654a4660e8456b6b2aec5ae39173a0429a6a8e5fa1381c9488198ca2982db43ee8198af056f2a25537705c763784062056d0ab2eb1a"
}
```

[NIP-56 und NIP-09 lösen unterschiedliche Probleme](https://github.com/nostr-protocol/nips/tree/master). Eine Kind-`1984`-Meldung kann das Konto oder Event einer anderen Person anvisieren, verleiht aber keine Löschbefugnis. Eine Kind-`5`-Anfrage drückt die Absicht des ursprünglichen Autors aus und ist nur gegen die eigenen Events dieses Autors gültig. Keines garantiert Entfernung: NIP-56 delegiert die Aktion bewusst an lokale Moderationspolicy, während NIP-09 davon abhängt, dass Relays und Clients eine authentifizierte Anfrage respektieren.

Implementierungen legen diese Entscheidungen in unterschiedlichen Produkten offen. [Divine PR #6591](https://github.com/divinevideo/divine-mobile/pull/6591) korrigiert die Meldungszustellung in einem Kurzvideo-Client, [Conduit PR #250](https://github.com/Conduit-BTC/conduit-mono/pull/250) liest Meldungen als begrenzten Kontext für Marketplace-Teilnehmer, und [nostrords NIP-56-Modul](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/nostr/Nip56.kt) veröffentlicht und verarbeitet Meldungs-Events. [Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md#nip-support) listet außerdem aktuelle NIP-56-Unterstützung.


---

Sende eine NIP-17-DM, um ein Projekt oder eine Nachricht über das [Nostr-Compass-Projekt](https://github.com/andotherstuff/nostr-compass) zu teilen.
