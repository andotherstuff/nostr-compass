---
title: "Nostr Compass #39"
date: 2026-09-09
publishDate: 2026-09-09
translationOf: /en/newsletters/2026-09-09-newsletter.md
translationDate: 2026-09-11
draft: false
type: newsletters
description: "Nostr Compass #39 begleitet signierte Git-Workflows, Veröffentlichung im Browser, selbst gehostete Livestreams, Relay-Einwilligung in Communities, private Veranstaltungen, fokussierte Releases und den NIP-21/NIP-27-Linkvertrag."
---

Willkommen zurück bei [Nostr Compass](https://nostrcompass.org), deinem wöchentlichen Wegweiser durch Nostr.

**Diese Woche:** [ngit und GitWorkshop](https://ngit.dev/v3) bringen signierte Git-Workflows auf Nostr und [Blossom](/de/topics/blossom/), [nsite-clay](https://github.com/jooray/nsite-clay) macht das Veröffentlichen im Browser wiederherstellbar, und die [Wingman App](https://github.com/OtherStuffAI/wm-app) verbindet Browsing, lokale Signierung, Authentifizierung und Dateien. [Shosho und Livelier](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0) verbinden selbst gehostete Streams mit Nostr, [Communitator](https://github.com/dyne/communitator) macht Relay-Vorlagen vor der Signierung prüfbar, [cal.emre.xyz](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743) veröffentlicht Terminslots, und [Plektos](https://github.com/derekross/plektos/pull/16) verschlüsselt private Veranstaltungen. Getaggte Releases bringen Arbeit an Wiederherstellung und Privatsphäre in [Vector](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4), [Primal Android](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27), [LibreNostr](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) und [SkateSpots](https://zapstore.dev/apps/org.skatespots.app). Die Entwicklungsarbeit umfasst [NIP-27](/de/topics/nip-27/)-Rendering, signierte Relay-Einstellungen in [Conduit](https://github.com/Conduit-BTC/conduit-mono/pull/397), [NIP-A3](/de/topics/nip-a3/)-Zahlungsziele und Blossom-Mirrors. Gemergte Änderungen im [NIPs-Repository](https://github.com/nostr-protocol/nips) präzisieren reine Live-Abonnements und authentifizierte Anwendungsdaten. Unser Deep Dive erklärt, wie [NIP-21](/de/topics/nip-21/)-Links und NIP-27-Referenzen Nostr-Profile und -Events über Anwendungen hinweg transportieren.

## Top-Storys

### Signierte Git-Workflows bringen CI, private Repositories und Releases auf Nostr

Der [v3-Launch vom 8. September](https://ngit.dev/v3) vereint ngit, GitWorkshop, ngit-grasp und ngit-ci in einem signierten Workflow. [ngit](https://ngit.dev/ngit.git) überträgt Branches, Patches und Pull Requests als [NIP-34](/de/topics/nip-34/)-Events, während [GitWorkshop](https://ngit.dev/gitworkshop.git) die Review-Oberfläche bereitstellt. Der Launch ergänzt ngit-ci 0.1, einen selbst gehosteten Continuous-Integration-Dienst, dessen Anweisungen und Ergebnisse als signierte Nostr-Events übertragen werden, sodass Checks auf von Maintainern kontrollierter Hardware parallel zur Code-Review laufen können.

Derselbe Release bringt [ngit-grasp v3](https://ngit.dev/ngit-grasp.git) private Repositories über die GRASP-08-Erweiterung für private Repositories und macht die Autorität der Maintainer explizit. Signierte Release-Einträge können auf Assets in [Blossom](/de/topics/blossom/) verweisen, wodurch sowohl Release-Metadaten als auch inhaltsadressierte Dateien außerhalb einer gehosteten Forge bleiben. Die [neue Dokumentationsseite](https://ngit.dev/v3) bündelt die Client-, Private-Repository-, CI- und Web-Komponenten.

### nsite-clay macht das Veröffentlichen im Browser wiederherstellbar

Eine [Signer-Prompt-Korrektur vom 31. August](https://github.com/jooray/nsite-clay/commit/064a0c5350f1e2b107f7d8f1de00ad75ef2e69d8), die [Wiederherstellung von Veröffentlichungen](https://github.com/jooray/nsite-clay/commit/d1ad514f8068eec2e007059dc62a5b6f1d240ae0) und die [Bearbeitungssteuerung vom 2. September](https://github.com/jooray/nsite-clay/commit/8f9d7d140dd3cd3e1db8726781fcd852041713f7) machen [nsite-clay](https://github.com/jooray/nsite-clay) zu einem Veröffentlichungswerkzeug im Browser für eine Single-Page-Site. Ein Nutzer bearbeitet das Document Object Model direkt, serialisiert das Ergebnis, lädt es als inhaltsadressiertes [Blossom](/de/topics/blossom/)-Blob hoch und veröffentlicht das [NIP-5A](/de/topics/nip-5a/)-Manifest der Site neu. Kein lokaler Build oder Server ist erforderlich.

Der [Browser-Publisher](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/deploy.html) macht fehlgeschlagene Veröffentlichungen nun wiederherstellbar und reduziert wiederholte Signer-Abfragen, während der [Bearbeitungsleitfaden](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/guide.html) den Ablauf dokumentiert. Das Ergebnis bleibt für bestehende Gateways eine gewöhnliche NIP-5A-Site.

### Wingman App verbindet Browsing, Signierung und Dateien

Die Arbeiten im September ergänzen die [Wingman App](https://github.com/OtherStuffAI/wm-app) um [Datei-Dialoge](https://github.com/OtherStuffAI/wm-app/commit/b0c9c03d317573adeafa92b1a56d696ad399e3ec), [Profilveröffentlichung](https://github.com/OtherStuffAI/wm-app/commit/f2343add8493625d62a1eb7fb76002ceab73f704), [sicheren Signer und Sitzungswiederherstellung](https://github.com/OtherStuffAI/wm-app/commit/4e278d96eb9258b89dc8b9639eac7bde3ac475c6) sowie [getestete mobile Builds](https://github.com/OtherStuffAI/wm-app/commit/60456ec0a8b4ed26ecde53812a61f95dc0bd22ac). Ihre Flutter-Shell injiziert einen [NIP-07](/de/topics/nip-07/)-Provider in Seiten, die innerhalb der App geöffnet werden, während Flight Deck und das Tower-gestützte Drive eine Arbeitsfläche und einen Datei-Arbeitsbereich neben dem Browser bereitstellen.

Wingman signiert authentifizierte HTTP-Anfragen mittels [NIP-98](/de/topics/nip-98/). Die [Anfrage-Implementierung](https://github.com/OtherStuffAI/wm-app/blob/67ed27d216e528da5bb431322bd10ac15553796f/crates/wmapp-core/src/auth/nip98.rs) erstellt das Event, das ein Server vor der Antwort verifiziert, und gibt einer installierten Identität damit einen konsistenten Genehmigungsweg für Relay-Aktionen, Web-App-Signierung und Dateien.

### Shosho liefert Liveliers selbst gehostete Streams

[Shosho 1.1.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0) erschien am 1. September mit Unterstützung für [Livelier](https://github.com/r0d8lsh0p/livelier), dessen [Attributions-Update vom 31. August](https://github.com/r0d8lsh0p/livelier/commit/7d8abb875770289502b55c3d947987db08e206dc) die Bridge und die Owncast-Quelle in überbrückten Profilen kennzeichnet. Livelier beobachtet das öffentliche Verzeichnis von Owncast, prüft, ob ein Videostream live ist, und veröffentlicht dann ein adressierbares `kind:30311`-Ereignis nach [NIP-53](/de/topics/nip-53/). Die Entdeckung läuft über Nostr, während das Video auf dem Server des Streamers bleibt.

Der Chat durchquert die Bridge als `kind:1311`-Ereignisse. Das [Bridge-Design](https://github.com/r0d8lsh0p/livelier) öffnet eine quellseitige Verbindung nur, solange ein Nostr-Reader abonniert ist, kennzeichnet abgeleitete Identitäten und sendet flüchtige Chats an ein Relay, das sie nach drei Stunden löscht. Das Discovery-Relay akzeptiert Schreibzugriffe für Live-Ereignisse nur vom Bridge-Schlüssel; das Chat-Relay verwendet [NIP-42-Authentifizierung](/de/topics/nip-42/) und [NIP-70-Flags für geschützte Ereignisse](/de/topics/nip-70/).

### Communitator macht Relay-Vorlagen vor der Signierung überprüfbar

Die [Veröffentlichungsserie vom 31. August](https://github.com/dyne/communitator/commit/520edd33a253ca3249993172fd1003c80bfd9b7c) stattet [Communitator](https://github.com/dyne/communitator) mit kanonischen Vorlagen für Relay-Listen der Art `10002`, Blossom-Server der Art `10063` und Posteingänge für private Nachrichten der Art `10050` aus. Bevor ein Signer verbunden wird, zeigt die Anwendung normalisierte Endpunkte, Lese- und Schreibberechtigungen, Ereignisarten, feste Veröffentlichungs-Relays und Ziele an.

Der [begrenzte Signier- und Veröffentlichungsablauf](https://github.com/dyne/communitator/commit/2bd04c8fab292e73fe9a4ada250c64358aee8501) trennt das Verbinden vom Anwenden. Jedes Ereignis wird einzeln signiert, ein Durchlauf nutzt höchstens vier WebSocket-Verbindungen, und ein Ziel zählt erst nach einem positiven [NIP-01](/de/topics/nip-01/)-`OK`. Die Ergebnisse unterscheiden zwischen vollständiger, teilweiser, fehlgeschlagener und abgebrochener Zustellung. Geteilte Vorlagen bleiben unvertrauenswürdige Empfehlungen; die [Zustimmungsoberfläche](https://github.com/dyne/communitator#security-and-consent) erläutert die Beobachtbarkeit von Relays und Netzwerk.

### cal.emre.xyz veröffentlicht Terminverfügbarkeit nach NIP-52

Das öffentliche Repository wurde mit einem [ersten Commit vom 2. September](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743) eröffnet, gefolgt von einer signierten [Handler-Ankündigung vom 3. September](https://njump.me/6fead386f0f401c2d8641ef842ccc2ade5abb4e45d61bfd7f3872b43db04cdac) für [cal.emre.xyz](https://cal.emre.xyz). Ein Gastgeber veröffentlicht Verfügbarkeit als `kind:31923`-Ereignis nach [NIP-52](/de/topics/nip-52/); ein Gast veröffentlicht eine `kind:31925`-RSVP.

Es liest Gastgeber-Ereignisse und akzeptierte Besetzt-RSVPs von Relays, schließt sich überschneidende Zeitspannen aus und behält Nostr-Ereignisse als Terminplanungsaufzeichnung bei, ohne sie in eine separate Datenbank zu kopieren. Gastgeber können mit [NIP-07](/de/topics/nip-07/), [NIP-46](/de/topics/nip-46/) oder einem lokalen Schlüssel signieren; Gäste können einen separaten Schlüssel erzeugen. Das [Repository](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743) stellt außerdem die resultierenden `naddr`- und Kalender-Links bereit, wobei E-Mail standardmäßig deaktiviert ist.

### Plektos macht private Veranstaltungen zu einem verschlüsselten Kanal

Die [Implementierung privater Veranstaltungen vom 2. September](https://github.com/derekross/plektos/pull/12) macht jede [Plektos](https://github.com/derekross/plektos)-Zusammenkunft zu einem privaten Kanal innerhalb einer mit [Concord](/de/topics/concord-protocol/) verschlüsselten Community. Gästeliste, RSVP-Liste, Anmeldeboard, Thread, Beiträge, Titelbilder, Bearbeitungen und Löschungen werden gemeinsam verschlüsselt; eine Einladung enthält nur den Schlüssel des jeweiligen Ereignisses, und es wird kein Klartext-Kalenderereignis veröffentlicht.

Das [Lebenszyklus-Audit vom 6. September](https://github.com/derekross/plektos/pull/14) verankert die ID der Ereignisdefinition für den direkten Abruf, wenn mehr als 500 Wraps existieren, und behält zugleich einen paginierten Fallback bei. Einladungspakete laufen 30 Tage nach dem Ende eines Ereignisses ab und können deaktiviert werden, doch wer einen Kanalschlüssel bereits erhalten hat, kann ihn behalten. Eine separate [Parser-Sicherheitsreparatur](https://github.com/derekross/plektos/pull/16) sorgt dafür, dass fehlerhafte Type-Length-Value (TLV)-[NIP-19](/de/topics/nip-19/)-Bezeichner fehlschlagen, statt den Parser festzuhängen.

## Releases

### Vector 0.4.4 macht die Wiederherstellung verschlüsselter Communities sicherer

[Vector 0.4.4](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4) erschien am 31. August mit Korrekturen für Community-Wiederherstellung, Schlüsselrotation, Moderation und Antwort-Routing. Die Neugründung schließt eine angegriffene Community für den Einladungspfad, den Angreifer genutzt haben; der Ersatz der Mitgliedschaft ersetzt veralteten lokalen Zustand; und ein einzelnes unerreichbares Mitglied friert die Liste nicht mehr ein. Leere Rotationen werden abgelehnt, Beförderungen erhalten online befindliche Mitglieder, und Operationen verweigern die Ausführung, wenn erforderliche Mitglieder nicht erreichbar sind.

Die [Veröffentlichung](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4) persistiert außerdem Löschungen und Sperren durch Moderatoren, verschlüsselt das Gästebuch nach einer Passwortänderung neu, bindet Benachrichtigungsantworten nach einem Neustart an ihre Konversation und verwendet ausschließlich verifizierte Mehrspieler-Pfade. Es handelt sich um Wiederherstellungskontrollen, nicht um den Widerruf bereits erlangter Schlüssel.

### Primal Android 3.5.27 prüft Signer- und Wallet-Identität

[Primal Android 3.5.27](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27) erschien am 3. September, nachdem [die Signer-Identitätsprüfung](https://github.com/PrimalHQ/primal-android-app/pull/1108) und [die Wallet-Anfrage-Authentifizierung](https://github.com/PrimalHQ/primal-android-app/pull/1105) am 31. August gemergt wurden. Die lokale Signierung lehnt eine Anfrage ab, deren Identität nicht zum gehaltenen Konto passt, und eingehende [NIP-47](/de/topics/nip-47/)-Anfragen werden vor der Verarbeitung authentifiziert. Das Zap-Poll-Routing sendet Stimmen außerdem an den Autor der Umfrage, wenn die Umfrage in einer Antwort erscheint.

### GRAIN 0.8.0-rc2 schließt einen Pfad, der bestätigt, aber nicht gespeichert wird

[GRAIN 0.8.0-rc2](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2) erschien am 7. September, nachdem ein Speicherfehler ein `OK` erlaubt hatte, bevor deren asynchroner LMDB-Datenbank-Writer die volle Speicherkapazität bemerkte. Der Relay warnt jetzt bei 80 und 95 Prozent, verweigert neue Events bei 97 Prozent, lässt aber Raum für Löschungen, und meldet Writer-Fehler nach der Annahme. Die Retention läuft vom ältesten zum neuesten Eintrag, das Teardown behandelt späte Nachrichten, und ungültige Filter verwerfen keine gültigen Geschwister mehr.

Das [Release](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2) bestätigt außerdem Monitor-Ankündigungen von Kind `10166` und Relay-Reports von Kind `30166`, entfernt veraltete Reports, behält konfigurierte Relays als Fallback und meldet Live-Limits und Authentifizierung in [NIP-11](/de/topics/nip-11/) statt statischer Nullen.

### LibreNostr 0.5.0–0.5.2 macht Tor-Routing fail-closed

[LibreNostr 0.5.0](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) erschien am 7. September mit einem Orbot-Modus, der Relays, Zaps, Uploads, Medien, Wiedergabe und Vorschauen über einen SOCKS-Port leitet, plus einer Reparatur für einen Zap-Sheet-Absturz. Wenn Orbot oder der Proxy nicht verfügbar ist, stoppen Verbindungen, anstatt auf eine direkte Route zu leaken. [Version 0.5.1](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.1) verhindert, dass langsame [NIP-50](/de/topics/nip-50/)-Suchen lokale Ergebnisse verzögern; [0.5.2](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.2) ersetzt das rekursive Thread-Layout und repariert die Thread-Reihenfolge.

Das [Fail-Closed-Verhalten](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0) gilt für jede im Release aufgeführte Netzwerkfläche, und ein Neustart ist erforderlich, weil diese Clients langlebig sind. Die Patch-Releases bewahren diese Wahl, begrenzen zugleich aber unzusammenhängende Such-, Stack-Tiefen- und Layout-Fehler.

### SkateSpots fügt einen On-Device-Relay-Pfad hinzu

Der signierte [Zapstore-Release vom 8. September](https://zapstore.dev/apps/org.skatespots.app) fügt SkateSpots einen optionalen Citrine-Relay hinzu. Spots, Crews, Nachrichten und Kartendaten können lokal geladen werden; Beiträge werden offline in die Warteschlange gestellt; und das Telefon behält eine lokale Kopie. Bestehende Stash- und Nachrichteninhalte bleiben Ende-zu-Ende-verschlüsselt. Zahlungsprüfungen verlangen Rechnungsbeträge und vom Anbieter ausgestellte Zap-Receipts, bevor Zugriff gewährt oder Beiträge gezählt werden.

Der [lokale Relay](https://zapstore.dev/apps/org.skatespots.app) ist eine Speicher- und Kontinuitätsoption, kein Ersatz für jeden Remote-Relay. Er lässt einen Skater durch eine unverbundene Phase weiterarbeiten und später signierte Aktivität abgleichen, während die Zahlungsänderungen verhindern, dass ein selbsterstellter Receipt zum Nachweis der Abrechnung wird.

### Whistle 1.8.15 repariert die Recovery des Lebenszyklus verschlüsselter Gruppen

[Whistle 1.8.15](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15) erschien am 3. September, nachdem eine Android-Lebenszyklus-Reparatur verhinderte, dass route-ebene State-Holder anwendungsweite Relay-Subscriptions und Standortupdates zerstören. Die Release-Notes beschreiben außerdem aktualisierten Verbindungsstatus nach Sperre oder Doze sowie einen im beobachteten Fall zurückgewonnenen 501-Event-Backlog.

Der [Bug](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15) band den Besitz eines langlebigen Dienstes an einen kurzlebigen Bildschirm. Die aktivitätsbezogene Instanz am Leben zu halten und den Socket vor einem Einmal-Lesezugriff zu prüfen, macht es weniger wahrscheinlich, dass gewöhnliche Android-Navigation und Hintergrund-Suspendierung wie eine leere Gruppe aussehen.

### TWENTY ONE Companion 1.12.0 trennt verschlüsselte DMs von Legacy-Chat

[TWENTY ONE Companion 1.12.0](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0) erschien am 5. September mit gift-wrapped DMs nach [NIP-17](/de/topics/nip-17/). Der verschlüsselte Posteingang ist von älterem Space-Chat getrennt, der eigen bleibt, weil diese Nachrichten nie verschlüsselt waren und nicht migriert werden können. PDFs und Videos werden unter Vorbehalt der Relay-Richtlinie unterstützt, und persönliche Verbergungen synchronisieren, ohne zu Moderator-Bans zu werden.

Die [sichtbare Trennung](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0) ist Teil des Sicherheitsmodells. Die alte Historie als sicheren Posteingang zu bezeichnen, würde deren Herkunft falsch darstellen, während eine stille Migration eine Verschlüsselung suggerieren würde, die bei deren Erstellung nicht existierte.

### ZapStore 1.1.2 validiert Event-Ids und Zertifikatsrotation

[ZapStore 1.1.2](https://github.com/zapstore/zapstore/releases/tag/1.1.2) erschien am 4. September mit NIP-01-Event-Id-Validierung: Der Client berechnet die Id eines eingehenden Events neu und lehnt Abweichungen vor der Verwendung ab. Das Release identifiziert außerdem Pakete, die außerhalb von ZapStore installiert wurden. Auf dem Server bewahrt die [Zertifikat-Hash-Retention](https://github.com/zapstore/relay/pull/8) wiederholte `apk_certificate_hash`-Tags, sodass die Rotation des Android-Signierschlüssels eine genehmigte Herkunft bewahren kann.

Die [Event-Id-Prüfung](https://github.com/zapstore/zapstore/releases/tag/1.1.2) verhindert, dass ein Relay oder Cache Tags oder Inhalt ändert, während die alte Id behalten wird. Der Installationsquellen-Indikator liefert separate Herkunft, wenn ein Android-Paket mit gleicher Anwendungs-Id aus einem anderen Kanal stammt.

### Amber 6.6.1 hält Signer-Antworten zuordenbar

[Amber 6.6.1](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1) erschien am 4. September, nachdem das Berechtigungs-Parsing so repariert wurde, dass ein fehlendes optionales `kind` toleriert wird, und abgelehnte Signieranfragen begannen, ihren ursprünglichen Anfrage-Id zurückzugeben. Aufrufende Anwendungen können eine Ablehnung der eingereichten Operation zuordnen. Das Release aktualisiert außerdem Remote-Signer-Standardeinstellungen und fügt einen Indexer-Relay hinzu.

Gemeinsam bewahren diese [Fixes](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1) die Zuordnung in beide Richtungen: Ein Berechtigungseintrag bleibt nutzbar, wenn ein optionales Feld fehlt, und eine Ablehnung bleibt an die auslösende Anfrage gebunden. Die Änderungen der Relay-Standardeinstellungen betreffen die Discovery, ersetzen aber nicht die lokale Autorisierungsentscheidung des Signers.

## Unveröffentlichte Änderungen

### Zap Cooking rendert NIP-27-Referenzen mit Relay-Hinweisen

[Der Merge vom 4. September](https://github.com/zapcooking/frontend/pull/665) sorgt dafür, dass [Zap Cooking](https://github.com/zapcooking/frontend) `nostr:npub`- und `nostr:nprofile`-Referenzen in Artikeln, Rezepten, Editor-Vorschauen und Druckansichten rendert. Ungültige Bezeichner bleiben Text, die Auflösung erfolgt nicht-blockierend, und der Editor zeigt eine Vorschau des Markdowns, das signiert wird. Wenn Relay-Informationen vorhanden sind, wird aus einem nackten `npub` ein `nprofile` mit Outbox-Relays und einem passenden `p`-Tag.

In derselben Woche wurden [autorenbezogene Kind-`30023`-Abfragen](https://github.com/zapcooking/frontend/commit/6a379c680727bb49074a4ff85f070b404dba97a7) korrigiert, [verifizierte NIP-50-Suchrelays](https://github.com/zapcooking/frontend/commit/1802e8d7e95ed482209d09e03c834c2d9adfc1ea) mit Deduplizierung und Schutz vor veralteten Abfragen hinzugefügt und [NIP-47-Wallet-Aufrufe](https://github.com/zapcooking/frontend/pull/705) repariert, nachdem Änderungen an Abhängigkeiten Guthaben und Verlauf beschädigt hatten.

### Conduit gleicht signierte Relay- und Blossom-Einstellungen ab

[Conduit](https://github.com/Conduit-BTC/conduit-mono) hat am 2. September die [Bearbeitung von Blossom-Einstellungen](https://github.com/Conduit-BTC/conduit-mono/pull/374) und am 7. September den [Abgleich signierter Einstellungen](https://github.com/Conduit-BTC/conduit-mono/pull/397) gemergt. Market und Merchant behalten die neueste gültige Kind-`10002`-Relay-Liste und die Kind-`10050`-Inbox-Deklaration, bewahren eine nutzbare signierte Liste, wenn ein neueres Event fehlerhaft ist, unterscheiden eine explizit leere Liste von einer nicht verfügbaren Abfrage und ersetzen fehlgeschlagene deklarierte Relays nicht durch Code-Standardwerte.

Der [Kind-`10063`-Editor](https://github.com/Conduit-BTC/conduit-mono/pull/374) ermöglicht es einem Nutzer, eine geordnete HTTPS-Medienserver-Liste zu laden, neu zu ordnen, zu prüfen, extern zu signieren, zu veröffentlichen und zurückzulesen, ohne diese Server zu kontaktieren oder einen nicht deklarierten Standardwert einzufügen.

### NIP-A3-Zahlungsziele erreichen drei Clients

Vom 1. bis 3. September haben [Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041), [Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851) und [Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98) NIP-A3-Zahlungsziele vom Kind `10133` implementiert. Amethyst bietet eine optionale Übergabe nur an, wenn ein kompatibles Ziel existiert, und verwandelt sie nicht in einen Zap; Grimoire nutzt eine feste Registry, bevor Wallet-URIs erstellt werden; Pollerama validiert Monero-Adressen und ruft die Relay-Liste des Autors ab, bevor Ziele abgefragt werden. Jeder Client benötigt weiterhin eine erlaubte Zahlungsmethode, eine Relay-Route und eine korrekte Anzeige.

### Ditto erweitert Blossom-Fallback und Live-Einbettungen

[Ditto](https://github.com/soapbox-pub/ditto) hat am 6. September [breiten Blossom-Fallback und Mirroring](https://github.com/soapbox-pub/ditto/commit/1e35a0705c28f706eb40d1f99aedef3105cf6f07) gemergt. Avatare, Badges, Banner, Community-Bilder, benutzerdefinierte Emojis und Anwendungssymbole versuchen nun deklarierte Server mit demselben Blob-Hash; Mirror-Uploads verwenden ein standardmäßiges BUD-11-Autorisierungstoken. Eine [Änderung vom 4. September](https://github.com/soapbox-pub/ditto/commit/e2a29004a65122470179c83d6ded8336a5c10dfa) fügte kompakte `kind:30311`-Livestream-Einbettungen hinzu.

## NIP-Aktualisierungen und Arbeit an Protokollspezifikationen

### Nostr Implementation Possibilities

[NIP-01](/de/topics/nip-01/) präzisiert nun [den `limit: 0`-Filter](https://github.com/nostr-protocol/nips/pull/2460), gemergt am 4. September. Ein Relay MUSS keine gespeicherten Events zurückliefern, MUSS `EOSE` senden, sobald die initialen Abfragen abgeschlossen sind, und MUSS das Abonnement für neue passende Events aktiv halten. Clients können mit einem einzigen Filterfeld ein reines Live-Abonnement öffnen und dabei den lokalen Verlauf behalten. Die Klarstellung dokumentiert kompatibles Verhalten über mehrere Relay-Implementierungen und öffentliche Relays hinweg.

[NIP-78](/de/topics/nip-78/) erhielt eine [Anforderung für authentifizierte App-Daten](https://github.com/nostr-protocol/nips/pull/2458), gemergt am 3. September. Relays SOLLTEN [NIP-42](/de/topics/nip-42/)-Authentifizierung für die Kinds `78` und `30078` verlangen und SOLLTEN diese nur an den authentifizierten Event-Autor ausliefern. Das ist ein SOLLTE, keine Vertraulichkeitsgarantie: Clients können beliebige Relays nicht als privaten Speicher behandeln. Der Merge rät außerdem davon ab, benutzerdefinierte App-Daten-Kinds als generischen öffentlichen Austausch zu verwenden.

[NIP-AC](/de/topics/nip-ac/) wurde am 4. September als ausdrücklich offener [WebRTC-Signalisierungsvorschlag](https://github.com/nostr-protocol/nips/pull/2461) eröffnet. Er verwendet vorläufige ephemere Kinds für Ping, Verbindungsanfragen, Angebote, Antworten und ICE-Kandidaten, adressiert mit `p` und gruppiert über ein Sitzungs-`e`-Tag; Kind `30600` unterstützt die Auffindbarkeit. Relays SOLLTEN diese Signalisierungs-Events weiterverbreiten und DÜRFEN sie NICHT speichern, während Peers sich direkt verbinden. Die Nummern bleiben vorläufig, Clients SOLLTEN [NIP-65-Relay-Listen](/de/topics/nip-65/) verwenden, und Anwendungen, die Vertraulichkeit benötigen, SOLLTEN Angebots-, Antwort- und Kandidateninhalte mit [NIP-44](/de/topics/nip-44/) verschlüsseln.

## NIP Deep Dive: URI-Links und Referenzen im Event-Text

Ein Nostr-Bezeichner braucht eine transportierbare Bedeutung, bevor eine andere Anwendung ihn öffnen kann. [NIP-21](/de/topics/nip-21/) setzt einen [NIP-19](/de/topics/nip-19/)-Bezeichner hinter das `nostr:`-URI-Schema und gibt Browsern, Betriebssystemen und Anwendungen damit eine einzige weiterleitbare Form. [NIP-27](/de/topics/nip-27/) definiert, was dasselbe URI innerhalb eines lesbaren Event-`content` bedeutet. NIP-21 überschreitet eine Anwendungsgrenze; NIP-27 hält eine Profil- oder Event-Referenz in signiertem Fließtext. Keines der beiden erzeugt ein Event-Kind oder ändert Relay-Nachrichten; die [beiden Spezifikationen](https://github.com/nostr-protocol/nips/tree/master) definieren ausschließlich Verlinkungs- und Darstellungsverhalten.

### URI-Dispatch und NIP-19-Semantik

[Die Grammatik von NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) besteht aus `nostr:` gefolgt von einer NIP-19-bech32-Entität. `nsec` ist ausgeschlossen, da es einen privaten Schlüssel kodiert. Es gibt keine Authority-, Pfad- oder Query-Komponente, daher ist ein konformer Link `nostr:npub1...` und nicht `nostr://npub1...`. Eine Plattform oder ein Client kann sich als Handler registrieren; die Spezifikation wählt weder die installierte Anwendung aus noch definiert sie einen Web-Fallback.

Das Präfix teilt einem Client mit, was zu dekodieren ist. `npub` enthält einen öffentlichen Schlüssel und `note` eine Event-ID. `nprofile` fügt einem Profil optionale Relay-Hinweise hinzu; `nevent` ergänzt eine Event-ID um Relays, Autor und Kind; und `naddr` enthält Autor, Kind und die `d`-Kennung eines adressierbaren Events, mit optionalen Relays. Diese Formen verwenden [NIP-19-Type-Length-Value-Felder](https://github.com/nostr-protocol/nips/blob/master/19.md). Hinweise grenzen die Auffindbarkeit ein, beweisen aber weder den Besitz des Relays noch die Kontrolle des Autors. Jedes abgerufene Event erfordert weiterhin eine Neuberechnung der ID und eine Signaturprüfung.

Die Profilform in der [NIP-21-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/21.md) lautet:

```
nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9
```

[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) definiert außerdem HTML-Brücken: Eine Seite, die ein Nostr-Event ausliefert, kann dessen `naddr` in `<link rel="alternate">` einbetten, und ein Profil kann ein `nprofile` in `<link rel="me">` oder `<link rel="author">` einbetten.

### NIP-27-Rendering und optionale Tags

[NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) gilt für lesbaren Event-Inhalt wie Notizen des Kinds `1` und Artikel des Kinds `30023`. Ein Composer kann `@name` anzeigen, veröffentlicht aber `nostr:nprofile1...` im signierten String. Ein Reader scannt die URI, dekodiert ihre NIP-19-Entität, ruft das Ziel ab und kann einen Namen, eine Karte, eine Vorschau oder einen lokalen Link rendern. Schlägt die Dekodierung fehl, bleibt die URI gewöhnlicher Text. Der Rohinhalt darf nicht umgeschrieben werden: Eine Änderung verändert die NIP-01-Serialisierung, die ID und die Signatur.

Inhaltsreferenzen und Tags haben verwandte, aber unterschiedliche Aufgaben. [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) beschreibt optionale `p`- und `e`-Tags sowie den `q`-Tag aus [NIP-18](/de/topics/nip-18/). Ein Client kann eine Referenz anzeigen, ohne eine Benachrichtigung oder eine Thread-Beziehung zu erzeugen; die Ermittlung von Zitaten sollte sowohl die URI als auch ein `q`-Tag schreiben. [Die Implementierung von Zap Cooking vom 4. September](https://github.com/zapcooking/frontend/pull/665) folgt dieser Trennung, indem die URI beibehalten und gleichzeitig Relay-Hinweise sowie ein passendes `p`-Tag hinzugefügt werden. Das Hinzufügen von `p` oder `q` macht die URI nicht privat, und NIP-27 kennt keinen Modus für versteckte Erwähnungen.

Das folgende [Event des Kinds `1`](https://njump.me/note1e0my422kylehy2g4ax4d98vsthdvnvy702yq3f6eguedjr0256as200k6a) wurde von `wss://nos.lol` wiederhergestellt und vor der Aufnahme als konkrete NIP-27-Referenz verifiziert. Sein `content` enthält ein `naddr` für ein versionsunabhängiges adressierbares Event. Die Dekodierung ergibt Kind `30402`, den Autor `91036d...310a`, die `d`-Kennung des Workbooks und einen Hinweis auf `wss://nos.lol/`. Die Tags `q`, `p`, `t`, `zap` und `client` sind Entscheidungen der Anwendung, keine Anforderungen von NIP-27.

```json
{
  "id": "cbf64aa95627f3722915e9aad29d905ddac9b09e7a8808a7594732d90deaa6bb",
  "pubkey": "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
  "created_at": 1788953511,
  "kind": 1,
  "tags": [
    [
      "p",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/"
    ],
    [
      "t",
      "archetype"
    ],
    [
      "q",
      "30402:91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a:Archetype-Workbook-Companion-Meet-your-King-Warrioir-Magician-Lover-today-oejbwe",
      "wss://nos.lol/"
    ],
    [
      "zap",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/",
      "0.9"
    ],
    [
      "zap",
      "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
      "wss://relay.nostr.band/",
      "0.1"
    ],
    [
      "client",
      "Amethyst"
    ]
  ],
  "content": "You can check, read and use this Workbook already! You can also support and get it for few sats and support us in this project.\n\nI hope it'll help you in your Archetype Journey :)\n\n#archetype\n\nnostr:naddr1qpgyzunrdpjhg7tsv5k4wmmjdd3x7mmt94pk7mtsv9hxjmmw94xk2et594uk7atj949kjmn894tkzunjd9hkju3df4skw6trd9skut2vdamx2u3dw3hkgcte94hk26nzwajszrnhwden5te0dehhxtnvdakz7q3qjypkmmqcaetrcpld4m27la946cch2hrk7qr8xjehsu5j5h3uxy9qxpqqqpmvyqnrm7n",
  "sig": "aa9592e7c773271b9e9f980c8a7e17fda2ffd5a4483a1789e5dd4c4a83018ac576c5202b21b33b08770dcabe023f93998a41f1a0be4bf00e36cdde611d07915e"
}
```

### Vertrauen, Fehlerverhalten und Client-Implementierungen

Ein sicherer Parser findet ein vollständiges `nostr:`-Token, validiert bech32, dekodiert NIP-19, weist `nsec` zurück, ignoriert unbekannte TLV-Typen und lässt fehlerhaften oder übergroßen Text unverändert. `npub` und `nprofile` führen zu Profilabfragen; `note` und `nevent` identifizieren unveränderliche Events; `naddr` wählt das neueste gültige adressierbare Event für seinen Kind, Autor und `d`-Tag aus. Relay-Hinweise verringern den Suchaufwand, erweitern aber nicht das Vertrauen. Gemäß den [NIP-01-Event-Regeln](https://github.com/nostr-protocol/nips/blob/master/01.md) verifiziert der Client die ID eines abgerufenen `nevent` und prüft jede Signatur eines `naddr`-Kandidaten, bevor er die Ersetzungsregeln für adressierbare Events anwendet.

Inline-Vorschauen sind eine Entscheidung des Clients mit Kosten für Privatsphäre und Ressourcen. Das Abrufen jeder Referenz offenbart die Interessen des Lesers und kann einen Anfragesturm auslösen, daher können Clients einen Cache verwenden, Abrufe bis zur Sichtbarkeit aufschieben, die Parallelität begrenzen und für unbekannte Medien einen Klick verlangen. Gemäß [NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) muss eine Vorschau vom signierten Text des aktuellen Autors unterscheidbar bleiben. Ein Fehlschlag sollte als unaufgelöster Text oder nicht verfügbare Karte sichtbar sein, nicht stillschweigend als verifizierter Inhalt behandelt werden.

Das Vertrauen ändert sich auch je nach Identifikatortyp. Ein `nevent` bezeichnet unveränderliche Bytes, daher kann ein Client ein abgerufenes Event zurückweisen, dessen serialisierte ID von der angeforderten ID abweicht. Ein `naddr` bezeichnet eine ersetzbare Koordinate, daher muss ein Client jeden Kandidaten verifizieren und die Regeln für adressierbare Events anwenden, bevor er entscheidet, welche Version angezeigt wird. Ein Relay-Hinweis ist in beiden Fällen für die erste Abfrage nützlich, aber keine Empfehlung für das Relay oder den zurückgegebenen Inhalt. Die [TLV-Definition von NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md) liefert die Daten, die nötig sind, um diese Prüfungen explizit zu machen.

[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) definiert einen portablen Link, der von außerhalb von Nostr geöffnet werden kann, während NIP-27 denselben Link innerhalb signierten Texts dauerhaft macht. Ein Client, der nur NIP-21 implementiert, kann einen eingefügten URI öffnen, aber keine eingebetteten Referenzen darstellen. Vollständige NIP-27-Unterstützung fügt Scanning, sicheres Dekodieren, Abrufstrategien, lokale Darstellung und eine explizite Entscheidung über Benachrichtigungs- und Zitat-Tags hinzu. Der gemeinsame URI hält diese Ebenen interoperabel, ohne Clients zu zwingen, sie identisch darzustellen. [Damus](https://github.com/damus-io/damus) modelliert Inline-Referenzen als typisierte Erwähnungen. Sein [Mention-Code](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/Mentions.swift) bildet `npub` und `nprofile` auf Profilreferenzen, `note` und `nevent` auf Event-Referenzen und `naddr` auf Adressreferenzen ab; [NostrLink](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/NostrLink.swift) leitet sie an das passende Ziel weiter. [Primal Android](https://github.com/PrimalHQ/primal-android-app) [parst das Schema und eingefügte Formen](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/domain/nostr/src/commonMain/kotlin/net/primal/domain/nostr/utils/NostrUriUtils.kt), validiert bech32 und extrahiert Relay-Hinweise, und [bildet Referenzen anschließend auf Notizinhaltsmodelle ab](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/app/src/main/kotlin/net/primal/android/notes/feed/model/NoteNostrUriUi.kt). [Zap Cooking](https://github.com/zapcooking/frontend/pull/665) stellt dieselben Referenzen in Artikeln, Rezepten, Editor-Vorschauen und Druckansichten dar.

---

Sende eine NIP-17-DM, um ein Projekt oder eine Nachricht über das [Nostr-Compass-Projekt](https://github.com/andotherstuff/nostr-compass) zu teilen.
