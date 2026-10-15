---
title: "Nostr Compass #44"
date: 2026-10-14
publishDate: 2026-10-14
draft: false
type: newsletters
description: "Amethyst auf dem Desktop, Sicherheitskorrekturen für Amber, private Anhänge, authentifizierte Softwareinstallationen sowie Inhaltswarnungen und Status."
translationOf: /en/newsletters/2026-10-14-newsletter.md
translationDate: 2026-10-15
---

**[Amethyst](#amethyst)** bringt seine Android-Oberfläche auf den Desktop und ergänzt native Wayland-Unterstützung. **[Amber](#amber)** behebt Fehler beim Widerruf von Berechtigungen, beim Löschen kopierter Geheimnisse und bei einer Einstellungsänderung, die zum Verlust von Schlüsseln führen konnte. **[Keep](#keep-android)** verschärft die Berechtigungen für automatisches Signieren, während **[MDK](#mdk)** Streaming für private Anhänge und das Nachladen von Nachrichten in der Reihenfolge von alt nach neu bereitstellt. **[Zap Cooking](#zap-cooking)** integriert Schutzmaßnahmen für Änderungen an Follow-Listen und für authentifizierte Mitgliedschaften. Es folgen [Details zur Veröffentlichung](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0) sowie Protokolländerungen und Mechanismen für den öffentlichen Status.

## Topmeldungen

### Amethyst

[Amethyst v1.18.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.18.0) bringt die gemeinsame Oberfläche des Android-Social-Clients auf den Desktop – mit benutzerdefinierten Feeds, Deck-Ansichten für breite Fenster, optional aktivierbaren Sperren, verschlüsselten Medien und [Blossom-Uploads](/de/topics/blossom/). Anbieterbewertungen aus [NIP-85, vertrauenswürdigen Aussagen](/de/topics/nip-85/), werden für Anfragen, Benachrichtigungen und Abzeichen lokal indexiert; Anbieter und Schwellenwerte wählen die Nutzer selbst.

Die heutige [Veröffentlichung von v1.19.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0) ergänzt native Wayland-Unterstützung und Videokomprimierung auf dem Desktop mithilfe von separat installiertem FFmpeg und ffprobe. Korrekturen an der Schlüsselspeicherung beheben wiederholte Schlüsselbundabfragen und Fehler mit Linux-Schlüsselbunden. Kalendersammlungen und Teilnahmeantworten werden nun dargestellt, und die Android-Anmeldeoberfläche ergänzt [Remote-Signieren nach NIP-46](/de/topics/nip-46/). Verschlüsselte Umschläge werden parallel geöffnet, bevor die serielle Indexierung erfolgt; außerdem werden die Wiederverbindung zu relay und die Verarbeitung der relay-Listen von Feed-Autoren korrigiert. Der [relay-Client berücksichtigt die Wartezeit bei Ratenbegrenzungen](https://github.com/vitorpamplona/amethyst/pull/4422), bevor er Abonnements oder Veröffentlichungen fortsetzt.

Die [Änderung für relay von Vertrauensanbietern](https://github.com/vitorpamplona/amethyst/pull/4437) behandelt Anbieter-relay aus der kind-10040-Liste des Nutzers als eigene, vertrauenswürdige relay. Diese Verbindungen nutzen standardmäßig einen direkten Weg; für Tor muss die Einstellung für vertrauenswürdige relay aktiviert werden. Die [relay-Authentifizierung nach NIP-42](/de/topics/nip-42/) des Hauptclients kann diesen relay den öffentlichen Schlüssel des Nutzers offenlegen.

### Amber

[Amber 6.6.9](https://github.com/greenart7c3/Amber/releases/tag/v6.6.9) behebt drei Sicherheitslücken im Nostr-Signer für Android. [Widerrufene Berechtigungen](https://github.com/greenart7c3/Amber/security/advisories/GHSA-8f7m-9g64-vrjw) bleiben nicht mehr durch eine Race Condition im Cache bestehen, und ausdrückliche Ablehnungen haben Vorrang vor dem Status „vollständig vertrauenswürdig“. Für [kopierte Geheimnisse](https://github.com/greenart7c3/Amber/security/advisories/GHSA-g62f-m6pm-jv9p) wird ein vom System geplantes Löschen der Zwischenablage nach 60 Sekunden eingerichtet, auch wenn der Prozess beendet wird; während dieses Zeitraums bleiben die Inhalte lesbar, und auch später kopierter Text kann gelöscht werden. Beim Ändern von [„Entsperrtes Gerät erforderlich“](https://github.com/greenart7c3/Amber/security/advisories/GHSA-wv7c-hq2j-ppc5) bleibt der alte Wrapping-Schlüssel erhalten, bis die Migration der Geheimnisse abgeschlossen ist; bereits verlorene Schlüssel bleiben jedoch verloren. Die Veröffentlichung repariert nostrconnect-Genehmigungen für mehrere Anfragen und antwortet über die in der URI angegebenen relay. Nutzer von 6.6.8 und älteren Versionen sollten aktualisieren.

### Keep Android

[Keep Android v1.3.0](https://github.com/privkeyio/keep-android/releases/tag/v1.3.0), ein [FROST-Schwellenwert-Signer](/de/topics/frost/), ergänzt verteilte Schlüsselerzeugung auf den Geräten und die authentifizierte Wiederaufnahme unterbrochener Operationen mit Schlüsselanteilen. Die Version unterstützt auch Geräte ohne StrongBox. Beim Schwellenwert-Signieren halten die beteiligten Geräte Anteile des geheimen Signierschlüssels und arbeiten zusammen, um eine Signatur zu erzeugen; die Einrichtungs- und Wiederherstellungsschritte bestimmen, welche Geräte teilnehmen können.

[Version 1.3.1](https://github.com/privkeyio/keep-android/releases/tag/v1.3.1) verhindert, dass automatisches Signieren gespeicherte Ablehnungen, Berechtigungen mit der Einstellung „Nachfragen“, abgelaufene Genehmigungen oder fehlgeschlagene Berechtigungsabfragen übergeht. Nach Ablauf entfällt die Genehmigung im Hintergrund, während Ablehnungen erhalten bleiben. Die [Migration der anwendungsspezifischen Richtlinien](https://github.com/privkeyio/keep-android/pull/532) verschiebt Berechtigungen in den vom Kern verwalteten Speicher und bewahrt dabei strengere Entscheidungen.

### Chama

[Chama v6.4.21](https://github.com/jesuspirate/chama/releases/tag/v6.4.21) [authentifiziert die native Wallet-Bridge](https://github.com/jesuspirate/chama/pull/29), die von seiner über Nostr vermittelten Handelsanwendung genutzt wird, deaktiviert die URL-basierte Umleitung der Bridge im Produktivbetrieb und validiert Auszahlungsbeträge. Außerdem verweigert die Version das Löschen einer Wallet, deren Inhalt nicht gelesen werden kann.

[Version 6.4.22](https://github.com/jesuspirate/chama/releases/tag/v6.4.22) härtet das erneute Abspielen gegen fremde event ab, prüft Nachfolgerbeziehungen, lehnt leere Schlichter-Pools ab und leitet den Rückerstattungszeitpunkt aus der signierten LOCK-Zeit ab. Ihre Konsensänderungen gelten für CREATE-event, die ab dem 1. November 2026 signiert werden; die Schutzmaßnahmen im Client gelten sofort. Die Versionshinweise behalten Vorbehalte zu den vom Angebot ausgewählten Föderationen und zu Dust-Auszahlungen bei. Nachfolgende [Änderungen an Signer und Wiederherstellung](https://github.com/jesuspirate/chama/releases/tag/v6.4.23) ergänzen Leser für geschützte Seeds und wiederherstellbare verspätete Sperren, während [v6.4.24](https://github.com/jesuspirate/chama/releases/tag/v6.4.24) große Handelslisten verbessert.

### Zap Cooking

Der Rezept- und Social-Client [Zap Cooking integriert Schutzmaßnahmen für Änderungen an Follow-Listen](https://github.com/zapcooking/frontend/pull/795) gegen unvollständige, veraltete oder unerwartet verkleinerte Leseergebnisse. Follow-Aktionen verwenden einen gemeinsamen, abgesicherten Aktualisierungspfad, der vorhandene tag und Inhalte bewahrt. Vor der Veröffentlichung wird die Identität des Signers geprüft. Die [Korrektur der Mitgliedschaftsautorisierung](https://github.com/zapcooking/frontend/pull/802) verwendet den öffentlichen Schlüssel, mit dem die authentifizierte Anfrage signiert wurde. Eine [Route, die ein administratives Geheimnis offenlegte, wurde entfernt](https://github.com/zapcooking/frontend/pull/801); beim Deployment ist weiterhin eine Rotation des Geheimnisses erforderlich, die durch eine integrierte Änderung allein nicht sichergestellt werden kann. Spätere [Korrekturen an Threads und Lesezeichen](https://github.com/zapcooking/frontend/pull/833) bewahren den tatsächlichen Ursprung einer Antwort und holen fehlgeschlagene Lesezeichen-Schreibvorgänge nach. [Rezept-tag-Felder](https://github.com/zapcooking/frontend/pull/836) senden keine Tastatureingaben mehr an Profil- oder NIP-50-Suchdienste und verlassen den Editor nicht mehr mit ungespeicherten Änderungen.

## Veröffentlichungen mit Versions-tag

### MDK

[MDK v0.13.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.13.0), die Laufzeitumgebung für [verschlüsselte Marmot-Gruppen](/de/topics/marmot/), ergänzt Streaming und wiederaufnehmbare Übertragungen privater Anhänge mit Fortschrittsanzeige und Abbruchmöglichkeit. Außerdem sendet die Version private [NIP-56-Meldungen](/de/topics/nip-56/) über [NIP-59-Geschenkverpackungen](/de/topics/nip-59/) an den Betreiber der Instanz, wobei Nachrichten-, Gruppen- und relay-Kennungen weggelassen werden. Beim Nachladen werden Stapel von bis zu 256 event in der Reihenfolge von alt nach neu verarbeitet; CLOSED-Ablehnungen der relay bleiben erhalten. SOCKS5-Routing umfasst relay, Medien und Discovery-Dienste ohne direkten Ausweichpfad.

Der [Veröffentlichungsleitfaden](https://github.com/marmot-protocol/mdk/blob/v0.13.0/docs/release/0.13.0.md) verlangt, dass Bindings, Header und native Artefakte gemeinsam aktualisiert werden. Die Datenbankschemas wechseln von 101 auf 107, ohne Möglichkeit zur Rückstufung. Der Geheimnisspeicher des Hosts muss migriert werden. MarmotKit und C-Artefakte sind stabil; WN Agent bleibt eine Vorabversion, und die Workspace-Crates sind nicht auf crates.io veröffentlicht. Ein Verlauf, der mehr als fünf [MLS-Epochen](/de/topics/mls/) verspätet eintrifft, kann weiterhin unentschlüsselbar sein, ohne dass ein Hinweis auf einen unvollständigen Verlauf erscheint; authentifizierte Agent-Clients behalten Zugriff auf die gesamte API.

Die Veröffentlichung [wiederholt außerdem Speichervorgänge für Profile, Follow-Listen und relay-Listen, die nach der ersten Bestätigung ausstehend blieben](https://github.com/marmot-protocol/mdk/pull/2228); diese Wiederholungsversuche im Hintergrund überstehen keinen Neustart. Die [Einladungssuche prüft auf Discovery-relay, ob KeyPackages gelöscht oder abgelaufen sind](https://github.com/marmot-protocol/mdk/pull/2211); deren Antworten können nicht belegen, dass der Empfänger sein privates KeyPackage-Material noch besitzt. [Ziele von Aktivitätsreaktionen](https://github.com/marmot-protocol/mdk/pull/2187) werden nun konsistent aus authentifizierten Akteuren und einzelnen Gruppen-Commits abgeleitet; älterer Verlauf ohne Akteursangaben bleibt unvollständig.

Spätere Arbeiten am master-Branch [schließen nicht freigegebene relay-Abonnements und teilen Aktivierungswiederholungen in Seiten mit höchstens 500 events auf](https://github.com/marmot-protocol/mdk/pull/2274). Die [Wiederherstellung bei Epoch-Lücken](https://github.com/marmot-protocol/mdk/pull/2298) ruft die neuesten 256 events eines relays ab, bei dem der Vergleich fehlgeschlagen ist, ohne damit einen vollständigen Verlauf zu bestätigen. [Self-Update-Commits versuchen die Zustellung an jedes verpasste Gruppen-relay erneut](https://github.com/marmot-protocol/mdk/pull/2275). Neue Warnprüfungen erfassen [bekannte veraltete Epochs](https://github.com/marmot-protocol/mdk/pull/2273) und [Commits, die relays noch zugestellt werden müssen](https://github.com/marmot-protocol/mdk/pull/2288); Nutzer können das Risiko akzeptieren, sodass diese Prüfungen nicht garantieren, dass sich eine Gruppe nicht aufspalten kann.

[Durch Speichermangel blockierte Anhang-Downloads](https://github.com/marmot-protocol/mdk/pull/2249) behalten ihren fortsetzbaren Fortschritt bei, wenn der freie Speicherplatz nicht ausreicht. Große, ausdrücklich angeforderte Downloads werden direkt in eine Datei geschrieben, wobei Zwischenspeicherung und Prüfpunkte freien Speicherplatz in Höhe des etwa Fünf- bis Sechsfachen der Nutzdatengröße benötigen. [Verifizierte Vorschauen öffentlicher events](https://github.com/marmot-protocol/mdk/pull/2304) erhalten einen größenbegrenzten, verschlüsselten Konto-Cache, während [KeyPackage-Ergebnisse, die ausschließlich veraltete Einträge enthalten](https://github.com/marmot-protocol/mdk/pull/2305), von unvollständigen relay-Abfragen unterscheidbar werden. Dies sind spätere Änderungen am Quellcode, die eine entsprechende Übernahme durch die Host-Anwendung erfordern; event-ID-Vorschauen aus abgeschlossenen Abrufen prüfen nicht erneut auf spätere Löschungen.

Die Agent-Bridges [begrenzen außerdem die Backend-Ausgabe](https://github.com/marmot-protocol/mdk/pull/2103), damit übergroße Antworten nicht den Speicher erschöpfen, und [akzeptieren die tatsächliche Löschantwort des Konnektors](https://github.com/marmot-protocol/mdk/pull/2301). Bereits zugestellter Text bleibt zugestellt, wenn ein Ausgabelimit einen Durchlauf beendet.

### Myco

[Myco v0.11.0](https://github.com/Origami74/myco/releases/tag/v0.11.0) ergänzt USB-Verbindungen zwischen Telefonen oder fips-Desktops und übernimmt [das derzeit vorgeschlagene NIP-5D-Manifestformat](https://github.com/Origami74/myco/pull/135) mit signierten Artefakt- und Symbol-Hashes. Ältere Telefone lassen sich weiterhin koppeln, benötigen aber ein Update, um diese Napplets zu öffnen. Die [Änderungen an den Download-Richtlinien](https://github.com/Origami74/myco/pull/133) unterscheiden zwischen Internet-, Mesh- und vom Nutzer konfigurierten HTTP-Zielen. Vom Autor bereitgestellte Hinweise und Weiterleitungen können unter der Internet-Richtlinie keine lokalen Netzwerke sondieren, während vom Nutzer konfigurierte Ziele uneingeschränkt bleiben. Der Software-Client [findet außerdem Blobs auf den BUD-03-Blossom-Servern des Autors](https://github.com/Origami74/myco/pull/134). Das verbessert das Auffinden von Artefakten, macht den Installationsverkehr aber für diese Server sichtbar. Diese HTTP-Änderungen schaffen keinen gleichwertigen Schutz für WebSocket-Verbindungen. [Verfügbarkeitsprüfungen im nahegelegenen Mesh](https://github.com/Origami74/myco/pull/132) fragen Peers nach Blobs ab, ohne diese herunterzuladen oder öffentliche Blossom-Server zu kontaktieren. Diese begrenzten HEAD-Anfragen erfordern eine Mesh-Berechtigung; die Anzahl der Besitzer beweist nicht, dass das gesamte Artefakt weiterhin verfügbar ist.

Die Veröffentlichung [fragt außerdem mehrere vorgelagerte DNS-Server parallel ab](https://github.com/Origami74/myco/pull/137), damit Zeitüberschreitungen beim Roaming-Anbieter die Auflösung von relays und Artefakten nicht blockieren. Outbox-Veröffentlichungen richten sich an jedes aufgeführte Schreib-relay; langsamere Ziele werden im Hintergrund beliefert. Internet-Mesh bleibt standardmäßig ausgeschaltet, und Bilder aus dem Web werden über Neustarts hinweg nicht aufbewahrt.

### Unfiltered

[Unfiltered 1.0.13](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.13) ergänzt seinen Android-Fotoclient um Lese-/Schreib-relay-Listen und Outbox-Routing. Die [Versionshinweise](https://njump.me/nevent1qqsy8287ykdstql8ec2udgr8slj3czzkkdkjjc36xwn4lnjrrhggfwgu8dmj2) beschreiben die Rollen der relays; Konten ohne Liste beginnen mit drei öffentlichen Standard-relays. Die Umgebungsfunktion nutzt grobe Geohashes und benachbarte Zellen; das Hinzufügen eines Standorts zu einem Beitrag erfordert eine ausdrückliche Aktivierung und ist standardmäßig ausgeschaltet. Diese tags legen dennoch öffentlich ein Gebiet offen. Das untersuchte Veröffentlichungsergebnis bedeutet lediglich, dass die Daten für einen Socket in die Warteschlange gestellt wurden; die Annahme durch das relay ist weiterhin unbestätigt.

### monostr

[monostr 0.17.0](https://github.com/schmidt1024/monostr/releases/tag/v0.17.0) ermöglicht Nutzern, über einen persönlichen Watcher Monero-Trinkgelder zu empfangen, während [0.18.0](https://github.com/schmidt1024/monostr/releases/tag/v0.18.0) bei Neueinrichtungen standardmäßig die Trinkgeldbeträge und die Absendernamen in Benachrichtigungen verbirgt. Bilder werden standardmäßig erst nach Antippen geladen; optionale Primal-Zähler und Client-tags sind deaktiviert. Ein gehosteter Watcher erfährt über den privaten Ansichtsschlüssel der registrierten Wallet weiterhin von jeder dort eingehenden Zahlung. Öffentliche Belege enthalten auch bei verborgenen Beträgen weiterhin den Empfänger, den Zeitpunkt und den referenzierten Beitrag.

### Grocery

[Grocery 1.0.2](https://github.com/Marc26z/nostr-grocery/releases/tag/v1.0.2) kombiniert gemeinsame verschlüsselte Einkaufslisten mit Passkey-gestützten Nostr-Identitäten und einem Marmot-Chat für jede Liste. Einer Liste kann durch Einfügen eines Bearer-Schlüssels beigetreten werden, der Lese- und Bearbeitungszugriff gewährt. Die Passkey-Anmeldung hängt davon ab, ob Browser und Anbieter die Pseudozufallsfunktions-Erweiterung von WebAuthn unterstützen; Mitglieder-tags bleiben für relays sichtbar. [Version 1.0.3](https://github.com/Marc26z/nostr-grocery/releases/tag/v1.0.3) erhält Listen beim erneuten Öffnen durch lokales Zwischenspeichern der entschlüsselten Inhalte. Damit werden Fälle behoben, in denen nur der Schlüssel erhalten blieb, bis ein relay die Liste erneut zustellte.

### Roadstr

[Roadstr 1.1.0](https://github.com/roadstrapp/roadstr-app/releases/tag/v1.1.0) liest die kinds 1315/1316 eines anderen Roadstr-Clients unter Beachtung ihrer vorgesehenen Gültigkeitsdauern und Bestätigungsregeln. Ein kompakter Codec bewahrt rekonstruierbare signierte Meldungen für eine experimentelle MeshCore-Funk- und relay-Bridge. Die kompatible Veröffentlichung und die Funkübertragung sind standardmäßig ausgeschaltet; vor dem Teilen ist eine Zustimmung erforderlich. Funkmeldungen legen Position, Zeitpunkt und den zur Signatur gehörenden öffentlichen Schlüssel für alle Personen in Reichweite offen. Die Tests verwendeten simulierte Funkgeräte; echte Hardware, Android BLE und die Veröffentlichung auf öffentlichen relays sind weiterhin ungeprüft.

### OUTKAST

[OUTKAST 1.1.3](https://github.com/Lwb89dev/outkast/releases/tag/v1.1.3) verbessert Artikelkommentare und den Umgang mit zitierten Beiträgen in seinem Android-Client. Artikelkommentare verwenden kind 1111 mit dem Artikel als Wurzel und dem Kommentar als übergeordnetem Element, während gewöhnliche Antworten auf Notizen bei kind 1 bleiben. Die Zitatsuche akzeptiert sowohl q tags als auch ältere e-Erwähnungen mit Links; neu veröffentlichte Zitate fügen q tags hinzu. Fehlgeschlagene Veröffentlichungen machen vorab angezeigte Reaktionen rückgängig.

### Bookshelf

[Bookshelf 0.1.28](https://github.com/decent-newsroom/bookshelf-app/releases/tag/v0.1.28) beschreibt [das Lesen verschachtelter](https://njump.me/nevent1qqs8pukgjrnuzryv0z67lze2y0jsshepdckuss25qggvwn5skxqfa7gslzul0) Publikationsverzeichnisse vom kind 30040, die sowohl Kapitel als auch untergeordnete Verzeichnisse in der vom Herausgeber festgelegten Reihenfolge enthalten. Offline-Kopien behalten diese Hierarchie sowie Lesezeichen bei, die an das jeweilige Vorkommen gebunden sind. Beim Aktualisieren werden aktuelle Fassungen anhand der Koordinate abgerufen; der vorherige Download bleibt jedoch erhalten, wenn Ergebnisse unvollständig, älter oder erfolglos sind. Bei der erneuten Verbreitung bleiben die ursprünglich signierten untergeordneten Elemente erhalten. Eine begrenzte Auflösung der Verschachtelung und lesbare Teilzweige verhindern, dass eine lückenhafte Struktur als vollständiges Buch dargestellt wird.

### Ditto

[Ditto 2.45.0](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.45.0) ersetzt Global in seinen Inhaltsfeeds durch Entdecken. Entdecken bezieht Inhalte von Personen, denen die vom Nutzer abonnierten Konten folgen, und ordnet Beiträge nach gemeinsamen Verbindungen; der Nutzer selbst und bereits abonnierte Konten werden ausgeschlossen. Nicht angemeldete Nutzer und Konten ohne Abonnements sehen stattdessen ein ausgewähltes Einstiegsnetzwerk. Dadurch wird die standardmäßige Entdeckung auf ein soziales Umfeld eingegrenzt; Spamresistenz und die Vertrauenswürdigkeit dieser Konten bleiben davon getrennte Fragen.

### Postr

[Postr 1.1.2](https://njump.me/nevent1qqsf4uu87v5r7awyfhktjqnuc9m6xzfngpvr7gj37zca05sx7lk03vqy4wq7x) behält die Zuordnung ausgewählter Profilidentitäten zu Erwähnungen über gespeicherte Entwürfe und die Veröffentlichung hinweg bei. Der Beitragseditor friert Konto, Text, Erwähnungen und Anhänge während des Signierens und Sendens ein und hält eingehende geteilte Inhalte zurück, bis dieser Vorgang abgeschlossen ist. Wiederholungsversuche behalten das ursprünglich signierte event bei, auch bei älteren ausstehenden Beiträgen. Einen Namen nach @ einzugeben reicht nicht aus: Nutzer müssen ein Profil auswählen, und Identitäten, die in alten Entwürfen bereits verloren gegangen sind, müssen erneut ausgewählt werden.

### Nostrautica

[Nostrautica Android 0.11.0](https://github.com/jooray/nostrautica/releases/tag/android-v0.11.0) verknüpft Communitys mit ihren Treffen. Die Zulassung zu einem verknüpften event kann zugleich die Community-Mitgliedschaft gewähren, ohne dass eine zweite Genehmigung nötig ist; das Beitrittsformular weist darauf hin und ermöglicht es Antragstellern, dies abzulehnen. Bereits angemeldete Teilnehmer erhalten eine Einladung, die sie mit einem Tippen annehmen können. Events behalten ihre eigenen Teilnehmer, ihr Matching und ihren Chat, während die Community ihre events auflistet. Die Versionshinweise beschreiben die Unterstützung unterschiedlicher Koordinatoren für events und Communitys, ohne damit unabhängige Interoperabilitäts- oder Verschlüsselungstests zu belegen.

### Minibits

[Minibits v0.4.4 beta 1](https://github.com/minibits-cash/minibits_wallet/releases/tag/v0.4.4-beta.1) behebt einen Fehler bei der Zahlungsabwicklung über [Nostr Wallet Connect](/de/topics/nip-47/) unter Android: Diese konnte zum Stillstand kommen, während die Wallet im Hintergrund lief, und durch sich aufstauende Vorgänge dazu führen, dass die Anwendung nicht mehr reagierte. Die native Veröffentlichung bündelt die Over-the-Air-Änderungen der vorangegangenen fünf Monate. [Version 0.4.5 beta 1](https://github.com/minibits-cash/minibits_wallet/releases/tag/v0.4.5-beta.1) behebt die NFC-Übertragung von Android zu iOS; künftige Over-the-Air-Updates setzen diese Version voraus. Diese Fehlerbehebungen werden in den Versionshinweisen angegeben; die Hintergrundverarbeitung bleibt weiterhin von den Lebenszyklusbeschränkungen des Telefons abhängig.

### NoorNote

[NoorNote v1.9.0](https://github.com/77elements/noornote/releases/tag/v1.9.0) ermöglicht es Nutzern, Rezepte aus dem Artikeleditor zu veröffentlichen, geteilte Rezeptpakete zu öffnen und Rezepte von Autoren zu durchsuchen, denen sie folgen. Die letzte Woche behandelten Website-Karten und Profilraster sind nun Bestandteil der Veröffentlichung, ebenso wie die Behandlung von relay-Ratenbegrenzungen und direkte `nostr:`-Links unter Android. Website-Links sind weiterhin von einer Überprüfung der Inhalte einer Website zu unterscheiden; beim Zugriff über ein Gateway wird die angeklickte Anfrage für dieses Gateway sichtbar.

### Gittr

[Gittr v1.0.2](https://github.com/arbadacarbaYK/gittr/releases/tag/v1.0.2) stellt seine Nostr-Git-Schmiede für Android bereit und nutzt dabei Amber über [NIP-46-Remote-Signierung](/de/topics/nip-46/). Die APK öffnet die bestehende gehostete Anwendung `gittr.space`; Nutzer sind daher weiterhin von deren ausgeliefertem Browsercode und ihrer Verfügbarkeit abhängig. Das Signieren über Browser-Erweiterungen ist innerhalb dieser Hülle nicht verfügbar; Selbsthosting bleibt eine separate Git-Bereitstellung.

### Dart NDK

[Dart NDK 0.11.0 Entwicklungsversion null](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.0) bringt den [Handler für die Zustimmung zur Authentifizierung](https://github.com/relaystr/ndk/pull/862) des Dart- und Flutter-Toolkits sowie den relay-Wechsel für NIP-46-Signer in eine Vorabversion. Diese Änderungen wurden letzte Woche als zusammengeführte Arbeiten behandelt und sind nun veröffentlicht. Der Signer kann einer Ersatzliste von relays folgen, die Anwendungen dauerhaft speichern müssen. [Entwicklungsversion eins](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.1) ergänzt die Unterstützung für NIP-Kennungen mit Buchstaben in relay-Informationen. Beide Veröffentlichungen enthalten Änderungen, die bestehende Integrationen inkompatibel machen.

### Cambium

[Cambium v0.9.0](https://github.com/forgesworn/cambium/releases/tag/v0.9.0) bietet nativen Android-Apps [vier Genehmigungsoptionen](https://github.com/forgesworn/cambium/pull/32): einmalig, eine Stunde, einen Tag oder unbegrenzt. Erteilte Berechtigungen sind auf den jeweiligen Vorgang und den event kind beschränkt. Cambium leitet Anfragen per Remote-Signierung an einen Heartwood-Hardware-Signer weiter; Heartwood entscheidet weiterhin, welche Anfragen es signiert. Website-Genehmigungen gelten weiterhin nur einmalig. Gekoppelte Signer erhalten Bedienelemente zum Testen und Wiederverbinden, Aktualisierungen unterstützter Transport-relays und Diagnosedaten mit geschwärzten Angaben. Bei [NIP-55, Android-Signierung](/de/topics/nip-55/), bewahren Stapelanfragen die Reihenfolge der Anfragen und einzelne Ablehnungen; bei mehrdeutigen wiederverwendeten Intents wird eine sichtbare einmalige Zustimmung eingeholt.

### Grain

[Grain v0.8.1](https://github.com/0ceanSlim/grain/releases/tag/v0.8.1) behebt die [NIP-42-relay-Authentifizierung](/de/topics/nip-42/) seiner Go-Clientbibliothek für Anwendungen, die mehrere Nutzer bedienen. Jeder `UserContext` verfügt über eigene private authentifizierte Verbindungen, relay-Präferenzen und Haltemechanismen für Verbindungen; der gemeinsam genutzte Pool authentifiziert sich nie. Die Bibliothek validiert eingehende IDs und Signaturen, prüft die Übereinstimmung mit Abonnements und serialisiert tag- und Zeitfilter korrekt. Authentifizierte Aufrufer müssen zu `UserContext` migrieren. Die Speicherung und Bereitstellung durch relays bleiben unverändert, und die Authentifizierung erfordert beim Öffnen der Verbindung weiterhin eine Challenge.

### Nmail

[Nmail v0.18.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.18.0), ein verschlüsselter Mailclient, ordnet unbekannte Absender unter „Anfragen“ und blockierte Absender unter „Spam“ ein. Annahmen und Blockierungen werden geräteübergreifend synchronisiert. Bereits im Posteingang vorhandene Absender müssen angenommen werden; dafür steht „Alle annehmen“ zur Verfügung. Spam bleibt stumm, und bei wartenden Anfragen werden wiederholte Benachrichtigungen über denselben Absender vermieden. Antworten verwenden die Identität, an die die Nachricht gerichtet war. Die Verwaltung privater relays, Prüfungen der Gerätesperre vor dem Kopieren von Synchronisierungscodes, gemeinsame Designs, eine umfassendere Bewahrung von Kontaktdaten und ein Windows-Installationsprogramm ergänzen Fehlerbehebungen bei der Wiederherstellung des Postfachs nach dem Zurücksetzen oder Anmelden.

### Meiso

[Meiso v1.5.0](https://github.com/higedamc/meiso/releases/tag/v1.5.0) liefert verschlüsselte Kommentare und Ungelesen-Anzeigen für seinen über Nostr synchronisierten Aufgabenmanager. Kommentare verwenden adressierbare events vom kind 35002 mit [NIP-44-Verschlüsselung](/de/topics/nip-44/), wobei ihre Zuordnung zu einer Aufgabe innerhalb des Chiffretexts bleibt. Die Veröffentlichung [behebt das Offline-Senden](https://github.com/higedamc/meiso/pull/212), das Nachholen nach einer Wiederverbindung, den Start mit gespeicherten relays und die Weitergabe leerer Listen. Sie verhindert außerdem, dass eine unvollständige Synchronisierung Aufgaben löscht. Die Funktionen für ungelesene Einträge und das Nachholen ergänzen keinen Benachrichtigungsdienst für eine geschlossene Anwendung.

### Haps

[Haps v0.1.13](https://github.com/mmalmi/haps/releases/tag/v0.1.13), ein experimentelles Software-Installationsprogramm, verlangt standardmäßig eine Prüfung der exakten Veröffentlichung aus dem [Vertrauensnetz](/de/topics/web-of-trust/) des Nutzers. Prüfungen können auf eine bestimmte Revision festgelegten Quellcode und neu erstellte Artefakte vergleichen und privat bleiben oder veröffentlicht werden. [Version 0.1.14](https://github.com/mmalmi/haps/releases/tag/v0.1.14) fordert Nutzer bei einer Installation allein anhand des Namens auf, den Herausgeber zu bestätigen; automatisierte Abläufe müssen einen Herausgeber angeben. Prüfungen liefern Belege, während native Programme und Build-Rezepte weiterhin ohne Sandbox ausgeführt werden. Die Prüfpflicht lässt sich für einen einzelnen Vorgang umgehen; Prüfungen von Signatur und Integrität sowie die Bestätigung des Herausgebers bleiben bestehen.

### Sidecar

[Sidecar v1.16.0](https://github.com/dmnyc/sidecar/releases/tag/v1.16.0) ergänzt seinen Social-Client als Browser-Erweiterung um das [Entdecken und Abspielen von Livestreams](https://github.com/dmnyc/sidecar/pull/479), mit signiertem Chat, Reaktionen und zaps. Gespeicherte Stream-Lesezeichen unterstützen die verschlüsselte Sicherung und Wiederherstellung des Kontos, und private Stummschaltungen von Benachrichtigungen geben Nutzern Kontrolle über Hinweise. Die Suche erhält Bedienelemente zum Folgen und Stummschalten; hinzu kommen Änderungen an der automatischen Sperre und der Aktualisierung des Wallet-Verlaufs.

### Ants

Die Suchoberfläche [Ants v0.7.0](https://github.com/dergigi/ants/releases/tag/v0.7.0) [leitet strukturierte Suchanfragen](https://github.com/dergigi/ants/pull/316) über [NIP-65-relay-Listen](/de/topics/nip-65/) an die von Autoren angegebenen Schreib-relays und die Lese-relays erwähnter Nutzer weiter, ohne Anmeldung. Die Ermittlung begrenzt die Anzahl der berücksichtigten Identitäten und relays und endet bei Abbruch oder Zeitüberschreitung. Bei fehlenden Listen bleibt die Ausweichweiterleitung bestehen. Textanfragen verwenden weiterhin verifizierte [NIP-50-Such-relays](/de/topics/nip-50/).

### soyLI

[soyLI v0.27.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.27.0), eine Anwendung zum Veröffentlichen und Abspielen von napplets für vorgeschlagene [NIP-5D-Anwendungen](/de/topics/nip-5d/), ergänzt Tastenzuordnungen und Vorschläge ohne Fork über den Git-Hostingdienst GRASP, mit Prüfungen der exakten Revision bei erneuten Versuchen. Die [Veröffentlichung v0.26.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.26.0) verteilt signierte Veröffentlichungen nach der primären Veröffentlichung an verifizierte Outbox-relays; beim Löschen werden die Ziele erfasst, an die eine Übermittlung versucht wurde, unbekannte Kopien lassen sich jedoch nicht zurückrufen. [Version 0.26.1](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.26.1) erhöht die Größenbudgets für Lesen, Abspielen und Prüfen auf 100 MiB, behält jedoch für neue Builds und Veröffentlichungen eine Grenze von 25 MiB bei. Später hinzugefügte [direkte Präsentationsmetadaten](https://github.com/zeSchlausKwab/napplet-soy/pull/14) platzieren Titelbilder und Clips der Autoren direkt in signierten Manifesten und lösen damit das begleitende event ab. Eingefrorene ältere Aufträge werden weiterhin unterstützt; diese versionierte Soy-Erweiterung erfordert kompatible Leseanwendungen und ist nicht Teil der auf einen festen Stand festgelegten NIP-5D-Spezifikation.

### nostream

Der relay-Server [nostream v3.3.0](https://github.com/cameri/nostream/releases/tag/v3.3.0) ergänzt [NIP-66-relay-Monitoring](/de/topics/nip-66/) um Prüfungen der WebSocket-Lese- und -Schreib-Roundtrip-Zeiten, die Erkennung optionaler Authentifizierung und die Ermittlung von Spiegelzielen. Er warnt, wenn das beobachtete Verhalten von den [NIP-11-relay-Informationen](/de/topics/nip-11/) abweicht. Ratenbegrenzte OK-Antworten können ein optionales fünftes Element mit einer Wartezeit in Millisekunden enthalten. [Version 3.4.0](https://github.com/cameri/nostream/releases/tag/v3.4.0) ergänzt [CLOSED-Antworten](https://github.com/cameri/nostream/pull/821) um ein viertes Element mit einer Wartezeit in Millisekunden, wenn IP-Nachrichtenlimits `REQ` oder `COUNT` zurückweisen. Sie enthält den [PostgreSQL-Kern für den negentropy-Abgleich](https://github.com/cameri/nostream/pull/809) und ein geordnetes event-Inventar; relay-Protokollnachrichten und die Bekanntgabe unterstützter Funktionen nach [NIP-77](/de/topics/nip-77/) bleiben separate Arbeiten.

### Bark

[Bark v1.3.15](https://github.com/forgesworn/bark/releases/tag/v1.3.15) bietet für Freigaben beim Remote-Signieren Tastatursteuerung, eine ausdrückliche Prüfung von event und Identität sowie [eine, fünf oder zehn Minuten Entscheidungszeit](https://github.com/forgesworn/bark/pull/52). Die Durchsetzung im Hintergrund weist abgelaufene Entscheidungen und Anfragen in der Warteschlange zurück; schlägt die Übermittlung einer Entscheidung fehl, bleibt das Popup für einen erneuten Versuch geöffnet. [Version 1.3.17](https://github.com/forgesworn/bark/releases/tag/v1.3.17) stellt [NIP-07-Signierung im Browser](/de/topics/nip-07/) bereit, sobald der Handshake mit dem Signer abgeschlossen ist, während optionale Diagnosen weiterlaufen. Nach Updates stellt sie die Bridges in bereits geöffneten Tabs wieder her.

### Mostro

[Mostro v0.19.3](https://github.com/MostroP2P/mostro/releases/tag/v0.19.3) beantwortet identitätsauthentifizierte Anfragen zur eigenen Reputation des Nutzers, auch ohne offenen Auftrag. Die Peer-to-Peer-Börse sendet Antworten privat an den anfragenden Handelsschlüssel; ein [integrierter CLI-Befehl](https://github.com/MostroP2P/mostro-cli/pull/203) macht diese Abfrage zugänglich. Der Reputationsimport bleibt eine Vorschau, deren Importfunktionen nicht implementiert sind; Betreiber sollten ihn deaktiviert lassen. [Später integrierte Arbeiten](https://github.com/MostroP2P/mostro/pull/1057) veröffentlichen den Sicherheitspuffer des Lightning-Escrow-Wächters und weisen unsichere Konfigurationen zurück; das Minimum von 18 Blöcken setzt LNDs Standardeinstellung für den Hold-Ablauf voraus.

### Elisym

[Elisyms commerce 0.11.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.11.0) unterstützt Gebühren, die von den Händlereinnahmen abgezogen werden. Ein signierter tag im Shop-Profil erklärt die Unterstützung aufgeteilter Zahlungen; inkompatible Shops werden abgewiesen, wenn eine Gebühr anfällt. [Integrierte Admin-Arbeiten](https://github.com/elisymlabs/elisym/pull/170) lesen Bestellungen und Angebote von Nostr-relays. Dabei wird der geheime Schlüssel des Shops angefordert, was Vertrauen in den ausgelieferten Browsercode und in Erweiterungen erfordert; die lokale Administration bleibt verfügbar. Die gehostete Bereitstellung und die Aktivierung von Gebühren im Mainnet bleiben unbestätigt. [Merchant-node 0.10.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/merchant-node%400.10.0) aktualisiert sein Ledger ohne Unterstützung für ein Downgrade.

### Routstrd

[Routstrd v0.4.16](https://github.com/Routstr/routstrd/releases/tag/v0.4.16) verhindert, dass eine Aufladung über [Nostr Wallet Connect](/de/topics/nip-47/) nach einer Zeitüberschreitung sofort eine weitere bezahlbare Rechnung erzeugt. Es [prüft den bestehenden Mint-Vorgang](https://github.com/Routstr/routstrd/pull/144), bis die Zahlung erfolgreich ist oder fehlschlägt; ist der Status nicht verfügbar, bleibt die Aufladung pausiert. Das Inferenz-Gateway aktiviert Anbieter anhand von Nostr-Bewertungslabels, wobei experimentelle Labels eine ausdrückliche Zustimmung erfordern. [Version 0.4.17](https://github.com/Routstr/routstrd/releases/tag/v0.4.17) enthält das zugehörige SDK. Der Schutz bei noch nicht abgeschlossenen Vorgängen bleibt im Arbeitsspeicher, sodass er bei einem Neustart des Daemons verloren geht.

### Buzz

[Buzz desktop 0.5.28](https://github.com/block/buzz/releases/tag/desktop-v0.5.28) ermöglicht authentifizierten Mitarbeitenden, [alle Communitys auf einem relay zu durchsuchen und zu moderieren](https://github.com/block/buzz/pull/8027), ohne die Verbindung zu wechseln. Administrative Aktionen behalten die geprüfte Community, den relay und den Signer bei; bei deaktivierter Authentifizierung bleibt die Konsole zum Lesen verfügbar. Separat [integrierte relay-Arbeiten](https://github.com/block/buzz/pull/8197) verbergen korrekt mit tags versehene Lösch-events für private Autorendatensätze sowohl bei Abfragen als auch bei der Live-Auslieferung. Diese Serverkorrektur muss bereitgestellt werden und erfasst weder zuvor offengelegte Kopien noch historische Löschdatensätze ohne tags.

### Earthly

[Earthly v0.1.21](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.21) ermöglicht Nutzern, [öffentliche Nostr-Kartendatensätze in Websites einzubetten](https://github.com/zeSchlausKwab/earthly/pull/35), mit einer Vorschau sowie Steuerelementen für das Erscheinungsbild und die anfängliche Kameraposition. Die Maps-MCP-Integration erstellt und veröffentlicht Karten aus dem Chat heraus und erzeugt anschließend Freigabelinks oder Einbettungen. Die Integration bleibt ein persönlicher Pilotversuch mit einem verbundenen Plugin. Einbettungen unterstützen Inline-Datensätze mit bis zu 300 Features und 48 KiB; private, unveröffentlichte und Blob-basierte Datensätze sind ausgeschlossen.

### Milk Market

[Milk Markets mobile v0.3.0](https://github.com/shopstr-eng/self-sown/releases/tag/mobile-v0.3.0) bringt vollständige Editoren für das Shop-Design in die Verkäufer-App, mit denselben Abschnitten und Feldern wie im Web-Editor. Das Seitendesign einzelner Produkte kann die Auswahl von Theme und Abschnitten überschreiben, einschließlich Metadaten und Bildern für soziale Medien. Die Veröffentlichung ergänzt Prüfungen, damit Mobil- und Webkonfigurationen übereinstimmen. [Version 0.3.1](https://github.com/shopstr-eng/self-sown/releases/tag/mobile-v0.3.1) korrigiert den Kontrast in der mobilen Vorschaukarte; Android-Downloads sind den Veröffentlichungen beigefügt, iOS ist über TestFlight verfügbar.

### Zeus

[Zeus v13.2.3](https://github.com/ZeusLN/zeus/releases/tag/v13.2.3) enthält die letzte Woche behandelte [Korrektur der LDK-Routinggebühren](https://github.com/ZeusLN/zeus/pull/4353), die nun ausgeliefert wurde. Sein LDK-basierter Nostr-Wallet-Connect-Dienst kann gemeldete Routinggebühren in Antworten und Ausgabenaufzeichnungen aufnehmen. Budgetprüfungen berücksichtigen weiterhin den Rechnungsbetrag vor der Abwicklung; gerundete Gebühren werden anschließend abgebucht, und für Routinggebühren gilt eine separate Obergrenze von 1.000 Satoshi. Die Veröffentlichung aktualisiert außerdem das eingebettete LND und enthält Sicherheitskorrekturen für rust-lightning; die Validierung mit realen NWC-Geräten bleibt unbestätigt. Die später [integrierte Entfernung von Zaplocker](https://github.com/ZeusLN/zeus/pull/4933) stellt dessen Nostr-Attestierungs- und Einlösungsablauf ein. Ein Upgrade, während Zahlungen noch von diesem Server gehalten werden, entfernt die Einlösemöglichkeit; Absender müssen den Ablauf der Hold-Rechnung und die Rückerstattung abwarten. Diese Stilllegung ist nicht Teil von v13.2.3; die Einführung hängt davon ab, dass der Server deaktiviert und bestehende Nutzer gewarnt werden.

## In Entwicklung

### nosvelte

[Die Korrektur des event-Verifizierers von nosvelte](https://github.com/akiomik/nosvelte/pull/162) gleicht die mitgelieferte ID eines event mit dem kanonischen Hash seiner Felder ab, bevor die Signatur geprüft wird. Der Standardverifizierer der Svelte-Bibliothek akzeptierte zuvor korrekt signierte Felder mit einer ausgetauschten ID, sodass Inhalte die Identität eines anderen event annehmen und die Ersetzungslogik beeinträchtigen konnten. Die integrierte Änderung gilt für Anfrage- und Sendepfade der Version eins, die den Standardverifizierer verwenden; sie bestätigt nicht die Konformität des Legacy-Exports oder benutzerdefinierter Verifizierer mit dem [event-Format von NIP-01](/de/topics/nip-01/). Eine spätere [Korrektur des Anfragefilters](https://github.com/akiomik/nosvelte/pull/171) prüft und kopiert event-Felder von relays vor dem Abgleich. Fehlerhafte Daten können nicht mehr das Abonnement des Standard-Providers beenden oder dessen nächstes gültiges event verwerfen. Vom Aufrufer bereitgestellte Engine-Clients können das frühere Abgleichverhalten der Abhängigkeiten beibehalten.

### nostter

nostter [beschränkt extern bereitgestellte relay-Hinweise](https://github.com/SnowCait/nostter/pull/2684) auf sichere WebSocket-URLs und weist lokale Hostnamen sowie nicht globale IP-Adressen zurück. Für vom Konto ausgewählte lokale relays und Remote-Signer-URLs bleiben die bestehenden Pfade erhalten; DNS-Rebinding wird von der Prüfung nicht erfasst. Der Webclient [liest experimentelle, getrennte Inhaltswarnungs-Nutzdaten](https://github.com/SnowCait/nostter/pull/2680) außerdem erst, nachdem der Leser auf „Anzeigen“ gedrückt hat. Dabei prüft er die referenzierte event-ID, die Übereinstimmung des Autors und einen `k`-tag, der dem ursprünglichen event-kind entspricht. Reaktionen und Antworten beziehen sich auf das ursprüngliche event. Diese integrierten Änderungen lassen das aktuelle Veröffentlichungsformat nach [NIP-36](/de/topics/nip-36/) unverändert.

### Coracle

[Coracles Listeneditor](https://github.com/coracle-social/coracle/pull/679) stellt Bearbeitung und Löschung wieder her, indem er vor dem Rendern des Formulars die asynchrone Dekodierung abwartet. Zuvor gingen beim Bearbeiten die Felder der Liste verloren, und weder beim Speichern noch beim Löschen wurde ein event veröffentlicht.

### Routstr Core

[Der Quellcode der aktuellen Version 0.5.0 von Routstr Core](https://github.com/Routstr/routstr-core/releases/tag/v0.5.0) [protokolliert automatisch erzeugte private Nostr-Schlüssel nicht mehr](https://github.com/Routstr/routstr-core/pull/812) und [behält die beim ersten Start erzeugte öffentliche Identität bei](https://github.com/Routstr/routstr-core/pull/818). [Anbieterankündigungen](https://github.com/Routstr/routstr-core/pull/823) schließen localhost sowie direkt angegebene private oder linklokale HTTP-Adressen aus; Hostnamen werden für diese Prüfung nicht aufgelöst. Der aktuelle tag enthält Änderungen, die erst nach seinem verzeichneten Veröffentlichungsdatum am 7. Oktober zusammengeführt wurden; historische Binärdateien und Bereitstellungen bleiben daher ungeprüft. Bereits offengelegte Protokolle müssen weiterhin von den Betreibern überprüft werden.

### Alby Hub

[Die Änderung an der Rechnungsautorisierung von Alby Hub](https://github.com/getAlby/hub/pull/2629) beschränkt die Abwicklung und Stornierung auf Rechnungen, die von der anfragenden App erstellt wurden. Die selbst gehostete Wallet stellt App-Verbindungen über [NIP-47, Nostr Wallet Connect](/de/topics/nip-47/) bereit; die Berechtigung einer Verbindung, ihre eigenen Rechnungen zu verwalten, darf keine Befugnis über die Rechnungen einer anderen App verleihen. Eine separate [Datenschutzkorrektur für isolierte Verbindungen](https://github.com/getAlby/hub/pull/2621) entfernt die Lightning-Adresse der Haupt-Wallet aus den Erfolgsabläufen im Browser für isolierte Verbindungen.

### nak

[Der zusammengeführte relay-Befehl von nak](https://github.com/fiatjaf/nak/pull/222) prüft Verbindungs-, Lese- und Schreibzeiten sowie relay-Informationen und gibt anschließend unsignierte Discovery-events des kind 30166 aus. Werden diese Ergebnisse über eine Pipe an `nak event` übergeben, übernimmt dieser Befehl das Signieren und Veröffentlichen. Damit wird zeitgesteuertes [relay-Monitoring nach NIP-66](/de/topics/nip-66/) mit demselben Terminalwerkzeug möglich. Beobachtete Antworten zu Authentifizierung oder Beschränkungen haben Vorrang vor den angekündigten relay-Informationen. Schreibtests verwenden ein kurzlebiges event, das mit einem Wegwerfschlüssel signiert wird; Monitorankündigungen des kind 10166 bleiben ein separater Vorgang.

### Kehto

[Die Manifestprüfung von Kehto](https://github.com/kehto/web/pull/277) prüft vor der Ausführung aktuelle signierte Manifeste für ein einzelnes Artefakt sowie die Bytes des Artefakts; das Parsen älterer Formate bleibt davon getrennt. Die napplet-Shell [prüft außerdem empfohlene Handler](https://github.com/kehto/web/pull/294), fragt Benutzer bei Konflikten mit gespeicherten Auswahlen und verbraucht eine akzeptierte Aufruf-URL, um eine wiederholte Zustellung zu verhindern. Die Manifestprüfung kontrolliert die Identität des Herausgebers und die Bytes des Artefakts; sie stellt nicht sicher, dass der Anwendungscode sicher ist. [Gamepad-Momentaufnahmen](https://github.com/kehto/web/pull/297) richten sich jetzt nach Fokus und Sichtbarkeit. Paja/playground-Frames blockieren den direkten nativen Zugriff auf Gamepads, HID und USB, bevor Anwendungscode ausgeführt wird, und überlassen den vermittelten Zugriff dem Host. Nutzer dieser Funktionen benötigen die entsprechenden Host-Pakete; die Bereitschaft der Shell ist eine separate Fähigkeit. Eine spätere [Änderung an der Zulassung in Paja](https://github.com/kehto/web/pull/305) warnt vor nicht verfügbaren experimentellen Pflicht-Domänen, erlaubt aber das Laden; diese Domänen stellen weiterhin weder APIs noch Berechtigungen bereit.

### napplet SDK

[Das napplet SDK implementiert URI-basierte Aufrufe und eine bis zur Zustellung vorgehaltene Übergabe](https://github.com/napplet/web/pull/228). [Veröffentlichungsmetadaten bleiben in eigenständigem HTML erhalten](https://github.com/napplet/web/pull/226), und [optionale Anwendungsreferenzen](https://github.com/napplet/web/pull/239) verknüpfen Manifeste mit signierten Verzeichniseinträgen und Screenshots, ohne die Hashes der Artefakte zu ändern. Das Format für Anwendungsreferenzen bleibt ein Vorschlag. Die Tests der Referenz-Shell überlassen die produktive Erkennung, Installation und Signaturprüfung den Hosts.

### rust-nostr

Die Rust-Nostr-Bibliothek [rust-nostr bewahrt teilweise erzielten Downloadfortschritt neben abschließenden relay-Fehlern](https://github.com/nostrdevkit/nostr/pull/1483). Das fehlgeschlagene relay bleibt in der Menge der fehlgeschlagenen relays, sodass aufrufender Code bereits empfangene events nutzen kann, ohne den Nachweis zu verlieren, dass die Synchronisierung vorzeitig beendet wurde.

### Pensieve

[Die Sicherheitskorrektur für den Abgleich in Pensieve](https://github.com/andotherstuff/pensieve/pull/92) folgt auf die [Arbeiten zum Ausschluss fehlender events](https://github.com/andotherstuff/pensieve/pull/90). Die relay- und Archivwerkzeuge fordern die exakt fehlenden IDs erneut an, bevor sie Fehler klassifizieren. Dadurch wird verhindert, dass wegen Abfragelimits abgeschnittene Enden von Ergebnismengen zu fälschlichen Ausschlüssen führen. Pausen werden pro Auftrag erfasst, und bereits archivierte events werden gesondert behandelt. Ein abgeschlossener Auftrag kann weiterhin ausdrückliche Einträge zu fehlenden events enthalten; der Abschluss allein belegt kein vollständiges Archiv.

[Der kontinuierliche Abgleich mit Premium Primal](https://github.com/andotherstuff/pensieve/pull/84) wurde am 12. Oktober aktiviert. Laut dem [Bereitstellungsprotokoll](https://github.com/andotherstuff/pensieve/pull/93) des Betreibers wurden am 13. Oktober beide korrigierten Binärdateien bereitgestellt und das fehlerabhängige Pausieren aktiviert. Die spätere [Übernahme von Ausschlüssen](https://github.com/andotherstuff/pensieve/pull/95) verwendet ausschließlich ursprüngliche, nachgewiesene Ausschlüsse für dasselbe relay und ein überlappendes Zeitfenster erneut; verkettete Übernahmen und neu hinzugemischte IDs sind ausgeschlossen. Die [Bereitstellung wurde an jenem Nachmittag dokumentiert](https://github.com/andotherstuff/pensieve/pull/97). Die [Archiv-Vorabprüfung und die Korrektur für Cache-Stillstände](https://github.com/andotherstuff/pensieve/pull/98) wurden [am 14. Oktober bereitgestellt](https://github.com/andotherstuff/pensieve/pull/99). Eine spätere [Korrektur der Übernahmepriorität](https://github.com/andotherstuff/pensieve/pull/103) ist zusammengeführt, laut zugehörigem Quelleintrag jedoch noch nicht bereitgestellt.

### njump

Der Nostr-Webviewer [njump stellt die eingebetteten relay-Standardwerte wieder her](https://github.com/fiatjaf/njump/pull/173), wenn keine Datei zum Überschreiben angegeben wird. Außerdem [isoliert er parallel arbeitende Markdown-Renderer](https://github.com/fiatjaf/njump/pull/171) und [Antwort-Header bei Zeitüberschreitungen](https://github.com/fiatjaf/njump/pull/169). Damit werden Race Conditions behoben, die den Prozess beim Rendern zitierter Langform-events oder beim Bearbeiten gleichzeitiger Anfragen zum Absturz bringen konnten. Diese Serveränderungen sind zusammengeführt; ihre Bereitstellung im laufenden Betrieb bleibt ungeprüft.

### Nostr Components

[Die Korrektur der zap-Signierung in Nostr Components](https://github.com/saiy2k/nostr-components/pull/187) stoppt den Zahlungsablauf, wenn der ausgewählte Signierer ablehnt. Die einbettbaren sozialen Widgets ersetzen die Identität nach einer Ablehnung nicht mehr durch eine zufällige anonyme Identität. Ihre [Belegaggregation](https://github.com/saiy2k/nostr-components/pull/197) validiert [zap-Belege nach NIP-57](/de/topics/nip-57/), bevor sie Duplikate von relay-Kopien, Rechnungen und Anfrage-IDs entfernt.

### rx-nostr

Die [Änderungen an der Verifizierung in Version vier von rx-nostr](https://github.com/penpenpng/rx-nostr/pull/207), einer reaktiven Clientbibliothek, prüfen die kanonische event-Struktur, IDs und Signaturen in JavaScript und WebAssembly einheitlich. Eine leere Liste von Anfragebedingungen liefert keine Treffer und wird abgeschlossen; der Versand über den älteren Mechanismus meldet einen Fehler, wenn kein Ziel vorhanden ist. Beobachter der Veröffentlichung können den Abschlussstatus nicht verändern, und freigegebene untergeordnete Anfragen können nicht erneut starten. [Endliche Abfragesegmente](https://github.com/penpenpng/rx-nostr/pull/213) ermöglichen es Rückwärtsabfragen, nach Abschluss aller übergebenen Segmente abzuschließen. Diese Änderungen sind in [4.0.0 beta 2](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%404.0.0-beta.2) enthalten, einer Vorabversion mit inkompatiblen API-Änderungen.

### eHagaki

Der soziale Client [eHagaki ergänzt eine gestaffelte Outbox-Zustellung](https://github.com/Lokuyow/ehagaki/pull/268), bei der die relay-Ziele des Autors vor dem Signieren festgeschrieben werden. Sein Ablauf für sensible Beiträge sendet jedem relay die Nutzdaten vor der darauf verweisenden Struktur und verwendet dabei die jeweilige Bestätigung dieses relays; wenn nur die Nutzdaten erfolgreich zugestellt wurden, bleibt der Beitragseditor erhalten. Ein [vollständiger Scan des Beitragsverlaufs](https://github.com/Lokuyow/ehagaki/pull/312) speichert verifizierte Ergebnisse schrittweise. Uneindeutige Bereiche bleiben unbestätigt, selbst wenn der Scan als abgeschlossen angezeigt wird; ein Informationselement erläutert dies. Die [Unterstützung für das lokale relay Citrine](https://github.com/Lokuyow/ehagaki/pull/315) bewahrt verifizierte Durchsichtsbereiche und archiviert nach erfolgreicher externer Veröffentlichung die exakten signierten events. Lokale Bestätigungen machen aus einem fehlgeschlagenen externen Versand keinen Erfolg, und es wird keine Warteschlange für Offline-Veröffentlichungen hinzugefügt. Die [Verwaltung hochgeladener Medien](https://github.com/Lokuyow/ehagaki/pull/321) listet und löscht hochgeladene Bilder und Videos auf unterstützten NIP-96- und Blossom-Servern. Eine [spätere Datenbankmigration](https://github.com/Lokuyow/ehagaki/pull/325) setzt den zwischengespeicherten Anzeige- und Beitragsverlauf zurück, behält jedoch Entwürfe und Löschanfragen bei. Sie verhindert außerdem, dass ältere Synchronisierungsergebnisse aus der Warteschlange den Verlauf nach dem Leeren erneut füllen.

### Formstr

[Formstrs Korrektur für Übermittlungsergebnisse](https://github.com/formstr-hq/nostr-forms/pull/508) weist eine Formularantwort zurück, wenn kein relay sie annimmt. Die Nostr-Formularanwendung zeigt die Ergebnisse der relays an und bietet einen erneuten Versuch an, wobei ausgefüllte Antworten erhalten bleiben. Webhooks und Bestätigungsseiten warten auf die Annahme, und das SDK erhält dieselbe Prüfung. Eine Bestätigung durch ein relay ist weiterhin nicht mit garantierter langfristiger Speicherung gleichzusetzen, aber ein vollständiges Scheitern der Veröffentlichung führt nicht mehr zu einer Erfolgsmeldung.

### Auditable Voting

[Auditable Voting ergänzt die optionale gebündelte Freigabe von Stimmzetteln über einen privaten Worker](https://github.com/tidley/auditable-voting/pull/35). Vom Organisator signierte Definitionen legen eine Worker-Identität, DM-relays und einen Schwellenwert oder eine Frist für die Freigabe fest. Abstimmende senden [per NIP-17 gift-wrapped verpackte Stimmzettel](/de/topics/nip-17/) und authentifizieren Empfangsbestätigungen anhand dieses Workers; Delegationen müssen sowohl das Einreihen in die Warteschlange als auch die Freigabe autorisieren. Freigegebene Stimmzettel verwenden die Identität des Workers. Der Worker kann die eingereichten Stimmzettel lesen, und bei fristgesteuerter Freigabe können die Pakete klein sein. Wenn sich kein gültiger privater Übermittlungsweg ermitteln lässt, greift der untersuchte Client auf eine öffentliche Übermittlung zurück. Diese Entwicklungsarbeit wurde bereits zusammengeführt.

### MintRadar

[MintRadar ergänzt optionale gift-wrapped Benachrichtigungen](https://github.com/hroomnik007/MintRadar/pull/122) für Probleme bei Mint- oder Melt-Vorgängen, veraltete Software und den Wegfall der Unterstützung für diese Vorgänge. Sein Cashu-Mint-Verzeichnis [verknüpft die Bedienelemente der Beobachtungsliste](https://github.com/hroomnik007/MintRadar/pull/123) mit diesen Benachrichtigungseinstellungen und bestätigt sie nach der Serverantwort. Atomare Reservierungen verhindern, dass überlappende Prüfungen dieselbe Benachrichtigung senden, und eine fehlgeschlagene Veröffentlichung über relays gibt die Reservierung für einen erneuten Versuch frei. [Private Nachrichten nach NIP-17](/de/topics/nip-17/) schützen den Inhalt der Benachrichtigungen; die Annahme durch ein relay bestätigt nicht, dass der Empfänger sie gelesen hat.

### Nostr Docs

[Die Migration von Nostr Docs auf ein lokales relay](https://github.com/formstr-hq/nostr-docs/pull/65) leitet die Lese- und Schreibzugriffe des kollaborativen Markdown-Editors durch einen Web Worker mit einem IndexedDB-Cache für event-Daten und einem Postausgang für erneute Zustellversuche. Dokumenttitel und tags bleiben beim Neuladen erhalten, und aufeinanderfolgende Metadatenänderungen erhalten aufsteigende Zeitstempel, sodass zwei Änderungen innerhalb einer Sekunde unterscheidbar bleiben. Die bestehende Speicherung von Verschlüsselungsschlüsseln bleibt unverändert. Dem Rückfall auf den Netzwerkpool fehlt die dauerhafte Speicherung des Worker-Postausgangs, und die Annahme einer Veröffentlichung in die Warteschlange belegt keine Annahme durch ein relay.

### Pakstr

[Pakstrs nativer lokaler Signer](https://git.nostrdev.com/stuff/pakstr/pulls/105) ermöglicht es der Android-Anwendungshülle, auf dem Gerät ein Nostr-Konto anzulegen. Der Schlüssel bleibt in der nativen Schicht und wird mit einem durch den Android Keystore geschützten Wrapping-Schlüssel verschlüsselt. Signierergebnisse werden vor der Rückgabe an die Webanwendung überprüft. Die Anwendungshülle unterstützt [Browsersignierung nach NIP-07](/de/topics/nip-07/) und verschlüsselte Anfragen. Die Signer-Auswahl öffnet sich erst bei Bedarf und koordiniert gleichzeitige Anfragen.

### Nostr WoT SDK

Die Web-of-Trust-Bibliothek [Nostr WoT SDK erweitert die Zustimmung zur Authentifizierung](https://github.com/nostr-wot/nostr-wot-sdk/pull/15) auf typisierte native und entfernte Anfragesteller. Gespeicherte Ablehnungen werden vor Rückfragen geprüft, und wiederverwendbare Zustimmungen sind an den anfragenden Transportweg und das Ziel gebunden. Webanfragen bleiben standardmäßig einmalig. Die [verwalteten Blossom-Uploads](https://github.com/nostr-wot/nostr-wot-sdk/pull/13) validieren unveränderliche Bytes, unterstützen den Abbruch und stoppen, wenn sich die aktive Sitzung ändert; dabei gelten eine servergebundene Authentifizierung und Einschränkungen für Weiterleitungen.

### NosTube

[NosTube v0.2.49](https://github.com/flox1an/nostube/releases/tag/v0.2.49) stellt Desktop-Installationsprogramme bereit. Unabhängig davon [ergänzen zusammengeführte Serveränderungen eine dauerhaft gespeicherte zeitgesteuerte Veröffentlichung](https://github.com/flox1an/nostube/pull/126). events werden vor ihrem vorgesehenen Zeitpunkt signiert, in SQLite gespeichert und von einem Worker veröffentlicht, der nach Ausfallzeiten ausstehende Veröffentlichungen nachholt. Der [Ablauf für Bearbeitung und Löschung](https://github.com/flox1an/nostube/pull/124) verfolgt Löschmarkierungen, die Zustellung an Spiegelserver und die Bereinigung eigener Dateien. Die [Einrichtung beim ersten Start](https://github.com/flox1an/nostube/pull/134) unterscheidet den Browser-Signer eines Nutzers von einem serververwalteten Kanalschlüssel. Ältere Blobs ohne zugeordneten Eigentümer bleiben von der automatischen Bereinigung ausgenommen.

### diVine

[diVine 1.0.24](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.24) ergänzt die private Zusammenarbeit an Clips mit Nennung der Mitwirkenden und Prüfungen signierter Aufnahme- oder Bearbeitungsnachweise. Von Zuschauern ausgewählte übersetzte Untertitel fallen auf die Originale zurück, solange die Übersetzung aussteht oder nicht verifiziert ist. Diese Herkunftsprüfungen garantieren keine unbearbeitete Aufnahme.

Die [Routing-Änderungen](https://github.com/divinevideo/divine-mobile/pull/9884) des Kurzvideo-Clients ziehen für Text- und Videochatnachrichten die Inbox-relays der Empfänger heran und bewahren ungewisse Zustellergebnisse als solche. Die [Verarbeitung von Absenderkopien](https://github.com/divinevideo/divine-mobile/pull/10006) lässt eigene Gruppennachrichten der Nutzer auf deren anderen Geräten erscheinen; für zuvor verworfene Kopien muss das Konto erneut importiert werden. [Abgebrochene, nur teilweise erfolgte Gruppensendungen](https://github.com/divinevideo/divine-mobile/pull/10031) behalten Einträge mit dem Status „Nicht an alle gesendet“ bei; der Abbruch ist endgültig, und diese Einträge lassen sich nicht erneut senden. Die Gruppenerstellung und die Erkennung neuer, von anderen Teilnehmern eröffneter Räume bleiben [hinter einem standardmäßig deaktivierten Schalter](https://github.com/divinevideo/divine-mobile/pull/10020).

Nachfolgende Änderungen im Hauptzweig [halten Kopien unterbrochener Datenbankwiederherstellungen außerhalb des temporären Caches](https://github.com/divinevideo/divine-mobile/pull/10118) und [bewahren geplante Beiträge, eingereihte Meldungen, Profiländerungen und Einträge zu entfernten Chats während des Neuaufbaus](https://github.com/divinevideo/divine-mobile/pull/10115). [Sendefristen schließen den erneuten Verbindungsaufbau zu relays ein](https://github.com/divinevideo/divine-mobile/pull/10127), wodurch der Schwellenwert für einen erneuten Versuch nach einem aufgegebenen Sendevorgang von 160 auf 137 Sekunden sinkt. [Inbox-Abfragen über den Indexer verwenden einen separaten begrenzten Pool](https://github.com/divinevideo/divine-mobile/pull/10116), damit sie nicht hinter Feed-Lesezugriffen warten müssen, und [die Bedienelemente zum Folgen bewahren die gewählte Aktion](https://github.com/divinevideo/divine-mobile/pull/10147), falls sich die Kontaktliste vor der Bestätigung ändert. Diese später zusammengeführten Änderungen lassen bei langsamen Wiederverbindungen weniger Zeit für eine Bestätigung durch relays; Datenbankreparaturen können zuvor verlorene Daten nicht wiederherstellen. Später ergänzte [optionale Aufnahmekopien](https://github.com/divinevideo/divine-mobile/pull/10110) ermöglichen es der Galeriesicherung unter Android und iOS, neu aufgenommene Clips zu bewahren. Kopien ohne signierten Herkunftsnachweis werden mit einer Warnung versehen und können nicht erneut importiert werden; die Funktion ist standardmäßig deaktiviert und benötigt zusätzlichen Speicherplatz.

### Conduit

Die Handelsanwendungen in [Conduit erhalten einen gemeinsamen, dauerhaft gespeicherten Posteingang](https://github.com/Conduit-BTC/conduit-mono/pull/616), der die verschlüsselte Nachrichtenzustellung und Wiederherstellung über Market und Merchant hinweg bewahrt. Die Annahme durch das relay des Empfängers bleibt auch bei einer fehlgeschlagenen Selbstkopie des Absenders bestehen; die Wiederherstellung verwendet dieselben Bytes erneut, um einen zweiten Sendevorgang mit gleicher Bedeutung zu vermeiden. [Gemeinsame signer-gestützte Wallets](https://github.com/Conduit-BTC/conduit-mono/pull/635) verbinden beide Anwendungen. Dieser Wiederherstellungsweg vertraut dem Signer den Klartext für die Wiederherstellung an; die Integration in den Quellcode allein belegt weder einen laufenden Einsatz noch Abnahmetests mit tatsächlichem Guthaben. [Unabhängige relay-Berechtigungen](https://github.com/Conduit-BTC/conduit-mono/pull/645) bleiben erhalten, wenn mehrere Kontorouten dieselbe URL verwenden. Das Deaktivieren einer Route löscht nicht mehr die signierte relay-Listen- oder Inbox-Berechtigung einer anderen, und Lesezugriffe, die eine Authentifizierung erfordern oder unvollständig sind, behalten den Ergebnisstatus „nicht verfügbar“. Der [zusammengeführte Zahlungsrouter](https://github.com/Conduit-BTC/conduit-mono/pull/613) teilt eine vom Käufer genehmigte Finanzierungszahlung in Lightning-Auszahlungen an Händler und Lieferanten und anschließend die Conduit-Gebühr auf, mit einem exakten Abgleich der beabsichtigten Zahlung und verschlüsselter Wiederherstellung über den gemeinsamen Nostr-Posteingang. Die Ausführung in Produktions- und Staging-Umgebungen bleibt deaktiviert; ein Abschluss beim Anbieter beweist weder die Inanspruchnahme durch den Empfänger noch den endgültigen Abschluss der Zahlung.

### Bitcredit

[Bitcredits Verschlüsselung gespeicherter Daten](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1041) schützt die Identitäts-, Unternehmens- und Wechselschlüssel seiner Anwendung für elektronische Wechsel, einschließlich der Nostr-Warteschlange für erneute Sendungen, mithilfe der mnemonischen Phrase der persönlichen Identität. Die Initialisierung erfordert eine passende mnemonische Phrase. Die [Instanzverwaltung](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1043) ermöglicht es Testnet- und Mainnet-Instanzen, ihre Nostr-Abonnements im Hintergrund unabhängig voneinander auf einem Gerät weiterlaufen zu lassen.

## Neue Projekte

### Submarine

[Submarine 0.1.0](https://github.com/nogringo/submarine/releases/tag/v0.1.0) veröffentlicht einen Passwortmanager, dessen verschlüsselte Tresore über Nostr synchronisiert werden. Er unterstützt externe Signer und bewahrt gleichzeitig entstandene Versionen von Einträgen auf; Import und Export im JSON-Format von Bitwarden sind ebenfalls möglich. Änderungen werden lokal gespeichert, bevor auf die Annahme durch einen relay gewartet wird. Zur Veröffentlichung stehen Downloads für Android, Desktop und CLI bereit. Das Projekt bezeichnet sich als jung und empfiehlt für kritische Passwörter einen bewährten Passwortmanager; die mit diesem Versions-tag versehene Protokollspezifikation ist noch leer. Sein [Webspeicher](https://github.com/nogringo/submarine/blob/v0.1.0/apps/app/README.md) bewahrt den Verschlüsselungsschlüssel zusammen mit den geschützten Daten auf.

### cl-marmot

[cl-marmot](https://github.com/modus-lisp/cl-marmot/blob/5dd9dea97ece82b0e4cc08f0c893397fbb333a5b/README.md) ergänzt eine Common-Lisp-Implementierung von MLS-Gruppenchats über Nostr. Der Code vom 9. Oktober ergänzt Konvergenz bei konkurrierenden Commits und verschlüsselte Blossom-Anhänge; der Autor berichtet von Interoperabilitätstests mit MDKs Kommandozeilenclient wn. Die Implementierung wurde keinem Audit unterzogen, und Kontoschlüssel sowie Nachrichtenprotokolle sind im Ruhezustand nicht verschlüsselt. Zeitlich begrenzte Konvergenzfenster, Replay über den Rollback-Horizont hinaus und das Auflösen von Gruppen sind noch nicht implementiert; die untersuchte Testumgebung verwendet lokale Einweg-relays.

### nalgorithm Android

[Die Android-Veröffentlichung von nalgorithm](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.0) erstellt einen nach Präferenzen sortierten Nostr-Feed und im Hintergrund eine Audio-Zusammenfassung, die offline abgespielt werden kann. Nutzer wählen zwischen gehosteter, über Lightning abgerechneter Inferenz und vom Telefon angeforderter Inferenz mit eigenem Schlüssel; dies sind getrennte Wege. Die Anmeldung unterstützt Amber über Remote-Signing. Nachfolgende Veröffentlichungen [beheben die Rangfolgenberechnung mit eigenem Schlüssel und das Auffinden von Follow-Listen](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.1), [bewahren anschließend Likes von funktionierenden relays, wenn ein anderer relay ausfällt](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.2), und verbessern die Wiederherstellung der Audio-Zusammenfassung. [Version 1.0.3](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.3) ändert die Reihenfolge der Modelleinrichtung und meldet fehlende Eingaben für den Verbindungstest.

## Arbeit an Protokollen und Spezifikationen

### Authentifizierte napplet-Endpunkte

In den NAP-Spezifikationen für napplet-Anwendungen ersetzen die am 9. Oktober übernommenen [NAP-INC-Endpunktkennungen](https://github.com/napplet/naps/pull/104) bloße Handler-Namen durch authentifizierte Kennungen. Gleiche Namen von unterschiedlichen Herausgebern bezeichnen nicht länger denselben Peer. Die Laufzeitumgebung vermittelt weiterhin die Kommunikation, und Root- oder Snapshot-Manifeste benötigen keine benannte `d`-Koordinate.

### Handler-Empfehlungen in Aufruflinks

[Die Empfehlung für Aufruflinks](https://github.com/napplet/naps/pull/99), ebenfalls am 9. Oktober übernommen, erlaubt eine optionale Handler-Empfehlung per `#naddr`. Eine Shell kann das Auffinden und Installieren anbieten und andernfalls auf die gewöhnliche Auflösung zurückgreifen. Gespeicherte Präferenzen und die Shell-Richtlinie haben Vorrang. Ein empfohlener Handler liefert somit einen Hinweis zum Auffinden, ohne die bestehende Auswahl des Nutzers zu ersetzen oder die Befugnis zur Installation an den Absender des Links zu übertragen.

### Annahme der Zustellungsverantwortung und Anwendungsverarbeitung

[Die Änderungen an Intent-Ankündigung und Zustellung](https://github.com/napplet/naps/pull/91) leiten Rollen und Intents aus demselben verifizierten Manifest ab und verwenden dabei Kennungen, die Verwechslungen zwischen Herausgebern vermeiden. Die Annahme der Zustellungsverantwortung hängt nicht mehr davon ab, dass die Quellanwendung weiterläuft. Eine Antwort mit `ok: true` übernimmt die Verantwortung für die Zustellung; sie bedeutet nicht, dass die Verarbeitung in der Zielanwendung abgeschlossen ist. Das Verhalten bei Wiederholungsversuchen und Neustarts bleibt unter dieser übernommenen Spezifikationsänderung eine Richtlinienentscheidung der Laufzeitumgebung.

### Cyberspace-Aktionsketten

[Die überarbeiteten Kettenregeln von Cyberspace](https://github.com/arkin0x/cyberspace/pull/48) machen eine signierte Aktionskette bei einer Verzweigung ab ihrem Spawn ungültig und verlangen von Clients, vor dem Signieren einer weiteren Aktion die aktuelle Kettenspitze zu bestätigen. Die auf Nostr basierende Welt ergänzt [140 signierte synthetische Ketten](https://github.com/arkin0x/cyberspace/pull/49) mit normativen Bewertungen für Implementierungen. [Regeln zur Quellenangabe bei Kopien](https://github.com/arkin0x/cyberspace/pull/47) verwenden `q`-Verweise auf das ursprüngliche Objekt und benachrichtigen dessen Autor bei öffentlichen Remixen; bei versiegelten Kopien entfällt diese Benachrichtigung. Dies sind übernommene Projektspezifikationen; inwieweit eingesetzte Verifizierer sie abdecken, ist nicht verifiziert.

### Persistenzbestätigungen von relays

[Der offene Persistenzvorschlag](https://github.com/nostr-protocol/nips/pull/2496) führt Bestätigungen der dauerhaften Speicherung, PROOF-Abfragen und optionale signierte relay-Bescheinigungen mit kind 1797 ein. Eine Signatur macht eine Speicherzusage einem relay zurechenbar; sie beweist keine fortdauernde Aufbewahrung. Abfragen legen außerdem offen, welche events den Client interessieren.

### Gemeinsame Anheftungen für Marmot-Gruppen

[Marmots offener Vorschlag zum Anheften](https://github.com/marmot-protocol/marmot/pull/434) definiert einen authentifizierten gemeinsamen Zustand für bis zu 64 Nachrichtenverweise mit Berechtigungen für Mitglieder und Administratoren. Wirksame Änderungen erfordern einen MLS Commit und einen Epochenwechsel, und jedes daraus resultierende Mitgliedsblatt muss die Funktion unterstützen. Anheftungen kopieren keine Nachrichteninhalte und verlängern die Aufbewahrung nicht, sodass nicht verfügbare Ziele unaufgelöst bleiben. Die bereitgestellten Testdaten setzen einen authentifizierten Zustand voraus; sie demonstrieren weder kryptografische Verarbeitung noch Konvergenz zwischen Clients.

## NIP im Detail: NIP-36 und NIP-38

### Inhaltswarnungen vor der Anzeige

[NIP-36, sensible Inhalte](/de/topics/nip-36/), ermöglicht es Autoren, einem event einen `content-warning`-tag hinzuzufügen, optional mit einer Begründung. Ein Client kann den Inhalt ausblenden, bis der Leser sich entscheidet, ihn anzuzeigen. Die [Spezifikation](https://github.com/nostr-protocol/nips/blob/master/36.md) überlässt die Benutzeroberfläche den Clients und erlaubt ergänzende Label-tags. Das Hinzufügen einer Warnung ändert nicht, wer das event lesen kann. Bei einem öffentlichen Beitrag erhalten relays und andere Clients weiterhin dessen Inhalt.

[Amethysts Parser für Warnungs-tags](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt) erkennt den tag und behandelt eine fehlende oder leere Begründung als nicht angegeben. [Coracles Beitragseditor](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/views/NoteCreate.svelte) schreibt die Begründung in den tag; seine [Inhaltsansicht](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte) berücksichtigt die Einstellung des Lesers zu sensiblen Inhalten und bietet eine Aktion zum Einblenden an. [noStrudels Beitragsansicht](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx) wendet ihre eigene Warnungspräferenz und ihren Aufklappzustand an, bevor sie die Warnungsoberfläche anzeigt.

[NIP-36](https://github.com/nostr-protocol/nips/blob/master/36.md) verschlüsselt events nicht und schreibt kein Ausblenden vor. Eine fehlende Warnung sagt nichts über den Inhalt aus; Clients entscheiden, wie sich Warnungen auf Vorschauen und Bedienelemente zum Einblenden auswirken.

### Profilstatus und Ablauf

[NIP-38, Nutzerstatus](/de/topics/nip-38/), verwendet adressierbare events mit kind 30315. Autor, kind und `d`-tag identifizieren eine Statuskoordinate; `general` und `music` haben festgelegte Bedeutungen. Ein neueres event ersetzt den vorherigen Status an dieser Koordinate, während ein anderer `d`-Wert getrennt bleibt. Leerer Inhalt löscht einen Status. Die [Spezifikation](https://github.com/nostr-protocol/nips/blob/master/38.md) erlaubt außerdem Verweise auf URLs, Profile, events und Adressen.

Dieses signierte [NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md)-event zeigt einen abgelaufenen allgemeinen Status. Die ursprüngliche Schreibweise des Autors bleibt erhalten.

```json
{
  "kind": 30315,
  "id": "8848719ae347e705afbbdbfa3a9f5dcca5dd31c4f39182503bf84de5e362bcf4",
  "pubkey": "f13fdeecd852acebaa77dbc18806a051eaa7ea2214c157a3495982d7535a77f3",
  "created_at": 1791983702,
  "tags": [
    [
      "d",
      "general"
    ],
    [
      "expiration",
      "1791984600"
    ]
  ],
  "content": "I'm listening 📩 on 3 ralys",
  "sig": "b5c98a578773f0199cb833d4b916aac115f2b13474a61e81fdca7316b848d397d7d8ad86d299abee4721f404b7b8a1af26e8c53143457ad14d2fb933b21daf85"
}
```

[Das Statusmodell von Damus](https://github.com/damus-io/damus/blob/4a94f666d7e159e380e10b4dbbb2967d1688709e/damus/Features/Status/Models/UserStatus.swift) verarbeitet allgemeine Statusangaben und Musikstatusangaben mit Ablaufzeit. [Der Statusdienst von Nostria](https://github.com/nostria-app/nostria/blob/e861946f4ef4e70f3ec49997a4be27615b9b6f5e/src/app/services/user-status.service.ts) ignoriert leere oder abgelaufene Werte und veröffentlicht Musikstatusangaben anhand der Titeldauer; seine regulären Abonnements fragen nur allgemeine und musikbezogene Typen ab. [Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip38UserStatus/UserStatusEvent.kt) behält beim Löschen eines Status die Kennung `d` bei. Benutzerdefinierte Typen erfordern daher eine über die gemeinsame Übertragungsstruktur hinausgehende Abstimmung.

Statusangaben sind öffentliche Aussagen ihrer Verfasser. Sie belegen weder eine Onlinepräsenz noch, dass jemand einen Titel angehört hat. Die Veröffentlichung von Musik oder Verfügbarkeit kann Gewohnheiten offenlegen, und eine optionale Ablaufzeit begrenzt die Anzeige veralteter Angaben, ohne eine Löschung zu versprechen. [NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) bleibt ebenso wie NIP-36 eine optionale Spezifikation im Entwurfsstadium. Clients können beide unabhängig voneinander implementieren, wobei ihre Anzeigeeinstellungen bestimmen, was Leser sehen.
