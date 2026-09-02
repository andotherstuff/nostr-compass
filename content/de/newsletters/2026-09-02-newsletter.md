---
title: "Nostr Compass #38"
date: 2026-09-02
translationOf: /en/newsletters/2026-09-02-newsletter.md
translationDate: 2026-09-02
draft: false
type: newsletters
---

Willkommen zurück bei [Nostr Compass](https://nostrcompass.org), eurem wöchentlichen Wegweiser für Nostr.

**Diese Woche:** [Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) 1.0 bringt verifizierte Nostr-Notizen und Longform-Abonnements in einen offlinefähigen Android-Reader, der Artikel vorliest. [nostream](https://github.com/cameri/nostream) erweitert relay-seitiges Job-Routing und den authentifizierten Betrieb, [NDK for Dart](https://github.com/relaystr/ndk) behebt Fehler bei negentropy und den Laufzeiten von Anfragen über mehrere relays, [Divine Mobile](https://github.com/divinevideo/divine-mobile) macht das Löschen und Signieren verpackter Nachrichten deterministisch, [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay) schützt Gift-Wrap-Postfächer standardmäßig, [Amethyst](https://github.com/vitorpamplona/amethyst) liefert portable Hervorhebungen aus, und [Mostro](https://github.com/MostroP2P/mostro) verifiziert signierte Aufträge vor seinem Spam-Filter. [Napstr](https://github.com/lnbits/napstr) veröffentlicht Audiokataloge und Seeder-Heartbeats über Nostr, während Dateien über Tor übertragen werden. Releases betreffen [MDK](https://github.com/marmot-protocol/mdk) und [pakstr](https://git.nostrdev.com/stuff/pakstr); bei der Protokollarbeit werden im [NIPs-Repository](https://github.com/nostr-protocol/nips) ein Paginierungshinweis für [NIP-67](/de/topics/nip-67/) und ein Tag-Schema für Hervorhebungen in [NIP-84](/de/topics/nip-84/) gemergt, während [Nostr Wallet Connect](https://github.com/nostr-wallet-connect/nwc) Transaktionssummen ergänzt; und der NIP Deep Dive verfolgt Reposts und Reaktionen durch ihre Event-Formen und aktuellen Implementierungen. ... [gekürzt]
## Top-Storys

### Voca 1.0 liest verifizierte Nostr-Notizen und Abonnements auf Android vor

[Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) ist ein offlinefähiger Android-Reader, der Artikel, PDFs, Markdown-Dateien und Nostr-Notizen mit der Text-to-Speech-Stimme des Telefons vorliest, während der gesprochene Satz auf der Seite hervorgehoben bleibt. Das [1.0-Release](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en), das [am 2026-08-27](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) unter einem eigenen [Projektschlüssel](https://njump.me/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu) veröffentlicht wurde, macht Nostr zu einer Quelle erster Klasse: Fügt man eine Notizadresse, eine Event-Kennung, einen npub, ein Profil oder einen gewöhnlichen Weblink mit einer darin enthaltenen Nostr-Entität ein, dekodiert die App die Referenz, ruft das signierte event von relays ab und liest den Text des Autors statt der darum gebauten Webseite vor.

Zwei verifizierte Verhaltensweisen bestimmen die Nostr-Integration; beide werden in [Vocas signierter 1.0-Ankündigung](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) beschrieben. Erstens wird jedes abgerufene event vor dem Speichern anhand seiner neu berechneten id und seiner BIP-340-Schnorr-Signatur geprüft. Dazu dienen die Bootstrap-relays, die [NIP-65](/de/topics/nip-65/)-relay-Liste des Autors (ein signiertes, ersetzbares event des kind `10002`, in dem ein Autor die relays aufführt, von denen er liest und auf die er schreibt) sowie Hinweise in der Referenz selbst. Ein relay kann eine Antwort also verweigern, aber einem Autor keine Worte in den Mund legen. Zweitens werden durch das Hinzufügen des npub eines Autors dessen Longform-Artikel nach [NIP-23](/de/topics/nip-23/) (adressierbare Beiträge des kind `30023` mit Titeln, Zusammenfassungen und Bildern) in einem einzigen Postfach auf dem Gerät neben RSS- und Atom-Feeds gesammelt. Das Update 1.1.0, [angekündigt am 2026-08-28](https://gitworkshop.dev/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu/voca) und am 2026-08-29 auf [Zapstore](https://zapstore.dev) veröffentlicht, stimmt das Scrollen auf Satzebene zeitlich ab, macht lange Dokumente flüssiger und stellt das Startbildschirm-Widget nach manuellem Scrollen, Größenänderungen, Prozessneustarts und Upgrades wieder her. ... [gekürzt]


### nostream erweitert relay-seitiges DVM-Routing und den authentifizierten Betrieb

Nach den [Arbeiten zur Job-Aufnahme vom 19. August](/de/newsletters/2026-08-19-newsletter/#nostream-adds-a-relay-monitor-and-mints-invite-codes) [speichert und liefert](https://github.com/cameri/nostream/pull/737) [nostream](https://github.com/cameri/nostream), eine TypeScript-relay-Implementierung, events für NIP-89 Application Handler. [NIP-89](/de/topics/nip-89/) (Erkennung von Application Handlern) verwendet Empfehlungen des kind `31989` und Handler-Informationen des kind `31990`; beide liegen bereits im parametrisiert ersetzbaren Bereich. Ein Client kann daher diese kinds abfragen und erhält bei einer Kollision des `d` tag einen Ersatz. Das relay veröffentlicht keine Handler-Informationen für seine eigenen Worker.

Ausstehende Jobs nach [NIP-90](/de/topics/nip-90/) (Data Vending Machine) [erreichen nun einen Worker-Prozess und kehren als Ergebnis-events zurück](https://github.com/cameri/nostream/pull/734). Bei Erfolg signiert das relay mit seinem eigenen Schlüssel ein Ergebnis des kind 6000–6999. Ein Timeout oder Worker-Absturz markiert den Job als fehlgeschlagen, statt ihn im Status „eingereicht“ zu belassen.

Authentifizierte Sitzungen und Admin-HTTP-Aufrufe liegen an unterschiedlichen Grenzen. [NIP-42](/de/topics/nip-42/) (Client-Authentifizierung gegenüber relays) [verfolgt den authentifizierten pubkey pro Socket](https://github.com/cameri/nostream/pull/716), kann AUTH verlangen, bevor Clients events veröffentlichen, und weist im [NIP-11](/de/topics/nip-11/)-Dokument (relay-Informationen) auf diese Anforderung hin; beide Steuerungen sind standardmäßig deaktiviert. Unabhängig davon [können Admin-API-Routen eine durch NIP-98 signierte HTTP-Autorisierung akzeptieren](https://github.com/cameri/nostream/pull/730). [NIP-98](/de/topics/nip-98/) (HTTP-Authentifizierung mit signierten events) bleibt deaktiviert, bis ein Betreiber sie einschaltet und die zulässigen pubkeys festlegt.

### NDK for Dart behebt negentropy, Laufzeiten von Multi-relay-Anfragen und Signaturprüfung

Ein Lauf nach [NIP-77](/de/topics/nip-77/) (negentropy-Mengenabgleich) in [NDK](https://github.com/relaystr/ndk), einem Dart-Development-Kit für Nostr, lieferte ohne Fehlermeldung die falschen Have- und Need-Mengen zurück, weil der Codec nicht das [negentropy](/de/topics/negentropy/)-Protokoll v1 sprach. Die [Korrektur der v1-Kodierung](https://github.com/relaystr/ndk/pull/722) liefert nun die ids zurück, die das relay besitzt, und jene, die ihm noch fehlen.

Identische Filter, die an verschiedene relays gesendet wurden, [fielen zu einer einzigen Anfrage zusammen](https://github.com/relaystr/ndk/pull/705). Anfragen mit demselben Filter bleiben nun getrennt, wenn sie auf unterschiedliche relays zielen oder verschiedene Laufzeiten haben. Eine kurze Abfrage kann somit weder events eines anderen relay in das Ergebnis mischen noch ein aktives Abonnement blockiert zurücklassen.

Dasselbe Kit [verifiziert eine Signatur einmal und behält das Ergebnis](https://github.com/relaystr/ndk/pull/726). Eine spätere doppelte Zustellung führt nicht mehr zu einer weiteren Prüfung und überschreibt das gespeicherte verifizierte event nicht.

### Divine Mobile macht das Löschen und Signieren verpackter Direktnachrichten deterministisch

Verpackte events des kind `5` nach [NIP-09](/de/topics/nip-09/) (Anfrage zum Löschen eines event), die auf eine Nachricht zielten, wurden in [Divine Mobile](https://github.com/divinevideo/divine-mobile), einem mobilen Kurzvideo-Client, der über Nostr veröffentlicht, nie angewandt. Der Client [löst nun jede Löschung gegen die benannte Nachricht auf](https://github.com/divinevideo/divine-mobile/pull/8174), statt alles, was keine Reaktion ist, als bereits verarbeitet zu behandeln. Eine zweite [„Für alle löschen“-Anfrage, während die erste noch lief](https://github.com/divinevideo/divine-mobile/pull/8164), verschwand zuvor ohne Fehler und ohne kind `5` im Netz; nun wird jede gleichzeitige Löschung veröffentlicht.

Nach dem bereits behandelten Release 1.0.22 [erzeugte](https://github.com/divinevideo/divine-mobile/pull/8163) das zweimalige Senden desselben 1:1-Texts nach [NIP-17](/de/topics/nip-17/) (Gift-Wrapped private DMs) innerhalb einer Sekunde dieselbe Rumor-id, sodass die zweite Sendung verschwand. Nun enthält jede Sendung im Rumor nach [NIP-59](/de/topics/nip-59/) (Gift Wrap) ein Token, damit sich die ids unterscheiden.

Ein Aufrufer, der ein event des kind `4` oder kind `5` bereits signiert hatte, [behielt diese Signatur](https://github.com/divinevideo/divine-mobile/pull/8173), statt dass anschließend ein Client-tag angehängt wurde, der die id änderte und relays das event als ungültig ablehnen ließ.

### Conduit Relay härtet sein durch NIP-42 geschütztes Postfach ab

Gift Wraps des kind `1059` werden für genau einen Empfänger gespeichert. [Conduit Relay](https://github.com/Conduit-BTC/conduit-relay), ein Go-relay, das diese Wraps in einem empfänger­geschützten Postfach verwahrt, [verwendet standardmäßig den Erzwingungsmodus](https://github.com/Conduit-BTC/conduit-relay/pull/8): Eine Abfrage nach kind `1059` muss eine [NIP-42](/de/topics/nip-42/)-Authentifizierung als dieser Empfänger vorlegen, sonst lehnt das relay die Anfrage ab. Filter mit gemischten kinds, Wildcards, Zählungen und [negentropy](/de/topics/negentropy/) über diese Wraps sind `restricted`, sodass ein anderer AUTH-Vorgang daraus keinen Dump des fremden Postfachs machen kann.

Derselbe [Merge für das geschützte Postfach](https://github.com/Conduit-BTC/conduit-relay/pull/8) verlangt eine kanonische event-id im übertragenen AUTH-event und akzeptiert ein ansonsten gültiges NIP-42-event unabhängig davon, ob `content` leer ist. Challenge-only bietet AUTH weiterhin an, ohne den Lesezugriff zu blockieren; disabled gewährt freien Zugriff. Der Standardwert der Bibliothek ist enforce.

### Amethyst liefert NIP-84-Hervorhebungen aus und behebt zwei relay-bezogene Fehlerpfade

Im Anschluss an die [Blossom-Autorisierungsarbeiten der vergangenen Woche](/de/newsletters/2026-08-26-newsletter/#amethyst-moves-blossom-authorization-off-image-loading-threads) liefert [Amethyst](https://github.com/vitorpamplona/amethyst), ein Android-Nostr-Client, [v1.14.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.14.0) mit [NIP-84](/de/topics/nip-84/) (portable Hervorhebungen) aus. Eine ausgewählte Passage wird über den Composer, einen Hervorhebungs-Feed oder das Teilen in die App zu einem event des kind `9802`.

Das Release ergänzt Lösch- und Archivierungssteuerungen für [NIP-29](/de/topics/nip-29/)-Kanäle ([PR #3812](https://github.com/vitorpamplona/amethyst/pull/3812)) und misst das Verhalten von relays anhand des Datenverkehrs, den der Client ohnehin erzeugt. Anschließend erweitert es diese [NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md)-Probes um Streaming-, Lese-, Schreib- und URL-Prüfungen ([PR #3836](https://github.com/vitorpamplona/amethyst/pull/3836), [PR #3857](https://github.com/vitorpamplona/amethyst/pull/3857)). Amethyst beseitigt außerdem eine Hash-Kollisionslücke im SharedKeyCache und vergleicht Nachrichtenauthentifizierungscodes in konstanter Zeit ([PR #3833](https://github.com/vitorpamplona/amethyst/pull/3833)), behebt ein Race, durch das die AUTH-Zustellung beim Verbindungsaufbau verloren gehen konnte ([PR #3838](https://github.com/vitorpamplona/amethyst/pull/3838)), verteilt die Sperren des Abonnementstatus, um einen ANR-Konvoi zu beenden ([PR #3851](https://github.com/vitorpamplona/amethyst/pull/3851)), und vergleicht alle Abonnementfilter statt nur des ersten ([PR #3856](https://github.com/vitorpamplona/amethyst/pull/3856)). ... [gekürzt]

[Newsletter #36 behandelte diese Änderungen an relay-Authentifizierung, Backups und öffentlichen Chats bereits](/de/newsletters/2026-08-19-newsletter/#amethyst-rebuilds-its-relay-authentication-decision-flow); v1.14.0 hat sie nun gemeinsam ausgeliefert. Concord Soft Bans schließen durch ein Audit gefundene Autoritätslücken ([PR #3885](https://github.com/vitorpamplona/amethyst/pull/3885)). Die relay-Authentifizierung hat einen neu gestalteten Berechtigungsablauf ([PR #3899](https://github.com/vitorpamplona/amethyst/pull/3899)), wartet auf die Auflösung einer Challenge, statt ein Timeout auszulösen ([PR #3905](https://github.com/vitorpamplona/amethyst/pull/3905)), authentifiziert neue Konten standardmäßig ([PR #3931](https://github.com/vitorpamplona/amethyst/pull/3931)), berücksichtigt diese Einstellung bei relays außerhalb der üblichen Auswahl des Kontos ([PR #3937](https://github.com/vitorpamplona/amethyst/pull/3937)) und behält Sitzungsfreigaben bei erneuten Verbindungen bei ([PR #3955](https://github.com/vitorpamplona/amethyst/pull/3955)). Ein geführter Ersteinrichtungs- und Einstellungsablauf macht Schlüssel-Backups auffindbar ([PR #3909](https://github.com/vitorpamplona/amethyst/pull/3909)), das Nachfüllen von Cashu-Proofs und die Paginierung des Verlaufs verhindern abgeschnittene Wallet-Guthaben ([PR #3941](https://github.com/vitorpamplona/amethyst/pull/3941)), und öffentliche Chats können nun stummgeschaltet werden ([PR #3939](https://github.com/vitorpamplona/amethyst/pull/3939)). ... [gekürzt]

Nach diesem tag werden [vertrauenswürdige Listen](https://github.com/vitorpamplona/amethyst/pull/3983) der kinds `30392` bis `30395` durch [NIP-50](/de/topics/nip-50/) (Volltextsuche) nur nach Titel indexiert. So lässt sich eine im Fließtext genannte Liste finden, ohne die Hex-ids ihrer Mitglieder zu indexieren. Wallet-Ablehnungen, die über [NIP-47](/de/topics/nip-47/) (Nostr Wallet Connect) eintrafen, [zeigen nun ihren Fehler an, statt wie ein wirkungsloses Tippen auszusehen](https://github.com/vitorpamplona/amethyst/pull/3987), darunter `QUOTA_EXCEEDED` und `RESTRICTED`, sowie einen Timeout, wenn die Wallet nie antwortet.

### Mostro validiert signierte Aufträge vor aufwendiger Arbeit und bewahrt Audit-events zu Aufträgen auf

Nach der [Cashu-Escrow-Grundlage von v0.18.1](/de/newsletters/2026-08-12-newsletter/#mostro-0181-starts-a-cashu-escrow-path-and-hardens-the-daemon) hat [Mostro](https://github.com/MostroP2P/mostro), ein Peer-to-Peer-Exchange-Daemon, das Aufträge über Nostr koordiniert, [v0.18.5](https://github.com/MostroP2P/mostro/releases/tag/v0.18.5) getaggt. Die Version verwendet standardmäßig [NIP-44](/de/topics/nip-44/) (Payload-Verschlüsselung) für den Transport und behält Gift Wrap als ausdrücklich zu aktivierende Option bei.

Das Release verankert Timeouts im Wartezustand am aufgezeichneten Übernahmezeitpunkt, damit eine Maker-Bond nicht nach der falschen Uhr gekürzt wird ([PR #879](https://github.com/MostroP2P/mostro/pull/879)), stößt jede Käuferauszahlung für einen abgewickelten Auftrag höchstens einmal an ([PR #881](https://github.com/MostroP2P/mostro/pull/881)) und führt diese Auszahlungen über begrenzte, nicht blockierende `send_payment`-Wartevorgänge aus ([PR #883](https://github.com/MostroP2P/mostro/pull/883)). Eine versuchte Änderung zur Auszahlung an den Gewinner einer Timeout-Kürzung ([PR #875](https://github.com/MostroP2P/mostro/pull/875)) wurde zurückgenommen, bevor derselbe tag ausgeliefert wurde ([PR #885](https://github.com/MostroP2P/mostro/pull/885)). Mostro veröffentlicht außerdem weder stündlich noch beim Start ein unverändertes ausstehendes Auftragsbuch erneut ([PR #888](https://github.com/MostroP2P/mostro/pull/888)), und seine Streitfall-events des kind `38386` tragen nun einen `created_at` tag für die nachgelagerte Sortierung ([PR #878](https://github.com/MostroP2P/mostro/pull/878)).

Nach diesem tag wird [die Signatur nun vor dem Spam-Filter geprüft](https://github.com/MostroP2P/mostro/pull/892). Eine event-id legt `sig` nicht fest, sodass eine Kopie des kind `14` eines Opfers mit beschädigter Signatur den Replay-Slot belegen und die gültige Nachricht unbemerkt verwerfen konnte. Der Daemon verifiziert jetzt zuerst und verwirft einen ungültigen Wrap, statt nur zu warnen und fortzufahren.

Gebühren-Audit-events des kind `8383` trugen einen Ablaufzeitpunkt nach [NIP-40](/de/topics/nip-40/) von 15 Tagen. Nun [behalten sie eine Ablaufzeit von einem Jahr](https://github.com/MostroP2P/mostro/pull/924), passend zu ihrer Rolle als öffentlicher Zahlungsnachweis. Auf einem Cashu-fähigen Node [fordert die Annahme eines Auftrags den Verkäufer über Nostr auf, ein 2-von-3-Escrow zu sperren](https://github.com/MostroP2P/mostro/pull/830), veröffentlicht das wartende Auftrags-event und überspringt die Erstellung einer Lightning-Hold-Invoice. Damit ist der Anfragepfad vollständig; nicht jeder Escrow- oder Marktplatzmissbrauchsfall ist dadurch automatisch gelöst.

### Napstr veröffentlicht Audiokataloge auf Nostr und überträgt Dateien über Tor

[Napstr](https://github.com/lnbits/napstr) ist ein Desktop-Client zum Teilen von Audio, der durchsuchbare Kataloge und aktive Seeder auf Nostr veröffentlicht und die Dateien anschließend über einen mitgelieferten Tor-Prozess ohne Fallback auf direkte IP-Verbindungen überträgt. [Version 0.2.0](https://github.com/lnbits/napstr/releases/tag/v0.2.0) lässt Profile und Katalogmetadaten öffentlich, hält jedoch Anfragen, Übertragungszugangsdaten, Dateiinhalte und Peer-IP-Adressen von den relays fern.

Die Discovery verwendet zwei adressierbare event-kinds aus dem [Napstr-Repository](https://github.com/lnbits/napstr). Katalogeinträge des kind `30421` bezeichnen eine Datei anhand ihres SHA-256-Digests, öffentlichen Basisnamens, ihrer Größe und ihres Audioformats; ein Autor zieht eine Datei zurück, indem er diese Koordinate durch einen Löschmarker ersetzt. Verfügbarkeits-Heartbeats des kind `30422` laufen nach zehn Minuten ab und führen die Datei-IDs auf, die der Autor seeden kann. Eine Katalogzeile ist daher nur aktiv, solange ein noch nicht abgelaufener Heartbeat diesen Digest enthält.

Öffentliche Unterhaltungen verwenden [NIP-C7](/de/topics/nip-c7/) (Chatnachrichten des kind 9) statt einer relay-eigenen Gruppe. Das [Napstr-Repository](https://github.com/lnbits/napstr) definiert einen gemeinsamen öffentlichen Raum sowie eine anhand des Datei-Digests benannte Diskussion pro Titel. Diese Nachrichten sind signiert und öffentlich. Sie enthalten weder Onion-Adressen noch Übertragungszugangsdaten oder Dateibytes.

Ein Download beginnt als Aushandlung über [NIP-17](/de/topics/nip-17/) (Gift-Wrapped private DMs). Das [Napstr-Repository](https://github.com/lnbits/napstr) verpackt eine Anfrage, ein Angebot oder eine Ablehnung in einen Rumor des kind `14`. relays sehen dadurch weder den temporären v3-Onion-Hostnamen noch die einmal verwendbare Berechtigung, die ein angenommenes Angebot zurückliefert. Das mitgelieferte Tor überträgt die Bytes anschließend über dieses Onion, prüft den vollständigen SHA-256-Digest und validiert die Audiodatei erneut, bevor sie abgespielt werden kann.

Der [Vergleich von v0.1.7 mit v0.2.0](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0) ergänzt Hörbuchsammlungen und Napstrfy, einen optionalen Android-Begleiter. Manifeste des kind `30423` führen geordnete Kapitel auf, die gewöhnliche Katalogdateien bleiben. Ein Client, der die Sammlung ignoriert, kann daher weiterhin jedes Kapitel abrufen. Napstr legt dafür einen nicht destruktiven lokalen Audiobooks-Ordner an. Napstrfy koppelt sich über einen einmal verwendbaren QR-Code an einen laufenden Desktop und sucht und beantragt Downloads dann über dessen bestehende Nostr- und Tor-Dienste, ohne den geheimen Schlüssel des Desktops zu erhalten.

Derselbe [Vergleich](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0) lässt einen unvollständigen Companion-Handshake per Timeout enden. Ein Seeder kopiert und hasht die freigegebene Datei, bevor er Bytes ausliefert, schreibt eingehende Daten in eine private temporäre Datei, beschränkt Hörbuchziele auf echte Unterverzeichnisse des Napstr-Ordners und bricht ab, falls sich dieses Ziel während der Übertragung ändert.

## Releases

### MDK v0.9.17: neueste KeyPackages, Mitgliedschaftsaktivität und dauerhafte Sendungen

[Newsletter #37 behandelte MDK 0.9.14 und 0.9.15](/de/newsletters/2026-08-26-newsletter/#mdk-v0914-and-v0915-keypackage-selection-epoch-gap-recovery-and-split-relay-roles), darunter die Änderung im [MDK-Repository](https://github.com/marmot-protocol/mdk) von der Auswahl des ältesten KeyPackage zuerst zum neuesten gültigen Paket des aktuellen Profils, die Gates zur Wiederherstellung von Epoch-Lücken, die Kontobereinigung und die Trennung zwischen Discovery- und Betriebs-relays. Diese Korrekturen bleiben die Grundlage für die beiden folgenden Releases. Ein veraltetes Paket blockiert daher kein Mitglied mehr, das bereits ein nutzbares veröffentlicht hat.

[Mitgliedschafts- und Admin-events rücken die Chatliste nun vor](https://github.com/marmot-protocol/mdk/pull/1551), wie es eine neue Nachricht tut: Vorschautext, Sortierung, Anzahl ungelesener Nachrichten und Lesemarker werden aktualisiert, wenn Personen beitreten, austreten oder ihre Rollen ändern; der lokale Systemakteur wird nicht als Nostr-Profil behandelt. Bei erneuten Verbindungen und Neustarts [wird für einen erneut versuchten dauerhaften ausgehenden Text dieselbe Sendeidentität verwendet](https://github.com/marmot-protocol/mdk/pull/1516), sodass dieselbe Gruppennachricht nicht zweimal veröffentlicht wird.

Die beiden seither erschienenen Releases konzentrieren sich auf die Kosten, große Gruppen funktionsfähig zu halten. [Version 0.9.16](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.16) [misst die Epoch-Abweichung relativ zur aktuellen Epoch statt zu einem Höchststand](https://github.com/marmot-protocol/mdk/pull/1559), hält abgelehnte eingehende events abrufbar ([PR #1565](https://github.com/marmot-protocol/mdk/pull/1565)), begrenzt ein Replay-Rollback auf den kanonischen Gruppenzustand ([PR #1563](https://github.com/marmot-protocol/mdk/pull/1563)) und führt [marmot-c](https://github.com/marmot-protocol/mdk/pull/1545) ein, eine per Makro erzeugte C-ABI über den UniFFI-Bindings, mit der Hosts die Engine direkt einbetten können. [Version 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.17) fasst die Pass-Admission-Scans anschließend in [einem Durchlauf über die Mitglieder statt einem Durchlauf pro Mitglied](https://github.com/marmot-protocol/mdk/pull/1617) zusammen, [prüft, ob ein Gruppenzustand umstritten ist, ohne den vollständigen Verlaufsgraphen zu initialisieren](https://github.com/marmot-protocol/mdk/pull/1620), [senkt die Kosten des Deferred-Peel-Sweeps bei Leerlaufabfragen](https://github.com/marmot-protocol/mdk/pull/1621) und [wendet das gebündelte Lesen von Komponenten auf die drei Projektionsstellen an, die beim ersten Durchgang übersehen wurden](https://github.com/marmot-protocol/mdk/pull/1622). Die passenden Artefakte [marmot-c 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/marmotc-v0.9.17) und [WN Agent 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/wn-agent-v0.9.17) werden aus demselben Commit gebaut, sodass Einbetter die günstigeren Wartungspfade gemeinsam erhalten. ... [gekürzt]


### pakstr v0.16.0: kind-32267-Kennungen bei der Veröffentlichung

Nach der [Zapstore-Veröffentlichungspipeline von 0.13.0 bis 0.15.0 aus der vergangenen Woche](/de/newsletters/2026-08-26-newsletter/#pakstr-0130-through-0150-makes-zapstore-publication-explicit) [protokolliert](https://git.nostrdev.com/stuff/pakstr/pulls/67) [pakstr](https://git.nostrdev.com/stuff/pakstr), ein CLI, das eine Web-App in eine signierte Android-APK verpackt und sie mit einem Nostr-Schlüssel veröffentlicht, die IDs der Anwendungs-events des kind `32267`, die es nachschlägt, veröffentlicht oder ersetzt. [Version 0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0) gibt sowohl die vorherige als auch die neue ID aus, wenn veraltete Listing-Metadaten eine erneute Veröffentlichung auslösen. So kann ein Publisher bestätigen, welches Listing-event auf dem relay aktiv ist.

Dasselbe [Kennungsprotokoll](https://git.nostrdev.com/stuff/pakstr/pulls/67) zeichnet vor einem Ersetzen die bei der Suche gefundene ID und anschließend die ID des veröffentlichten event auf. Eine wirkungslose Wiederverwendung erscheint somit als wiederholte ID. Dies ist die getaggte Änderung in [0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0); Content-Digest, Veröffentlichung vor dem Upload und Publisher-Validierung wurden bereits mit den früheren tags ausgeliefert.

## Unveröffentlichte Änderungen

### Zap Cooking begrenzt Bunker-relays und signiert kostenpflichtige Endpunkte

Beim erneuten Laden einer Bunker-Sitzung auf [Zap Cooking](https://github.com/zapcooking/frontend), einer auf Nostr-Longform-events aufgebauten Rezeptseite, wurde die verschlüsselte Unterhaltung nach [NIP-46](/de/topics/nip-46/) (Remote Signing über relays) bisher auf jedem relay veröffentlicht, das die Seite bereits verwendete. Die [Begrenzung des Signer-Datenverkehrs auf die eigenen relays des Bunkers](https://github.com/zapcooking/frontend/pull/633) wendet diese Einschränkung nun bei der Sitzungswiederherstellung und bei nostrconnect-Pairing, dem vom Signer initiierten Verbindungsablauf, an und gleicht ihn damit dem Anmeldepfad über eine Bunker-URL an. Eine leere relay-Menge aus einem fehlerhaften gespeicherten Datensatz wird nicht übernommen. relays, die nur Rezepte hosten, erfahren dadurch nicht mehr, dass derselbe pubkey eine aktive Bunker-Sitzung unterhält.

[Signierte HTTP-Authentifizierung](https://github.com/zapcooking/frontend/pull/630) schützt nun den kostenpflichtigen Chat mit dem Kochassistenten, die Kochbucheinführung und Aktualisierungen zugangsbeschränkter Rezepte gemäß [NIP-98](/de/topics/nip-98/) (HTTP-Authentifizierung mit einem signierten Nostr-event). Der Server liest den Request-Body einmal, verifiziert die Signatur gegen genau diese Payload und übernimmt die Identität aus dem verifizierten Auth-event statt aus einem im Body übermittelten öffentlichen Schlüssel. Die Chatvorschau funktioniert weiterhin ohne Header; eine vorhandene, aber ungültige Signatur wird dagegen abgelehnt, und die Kochbucheinführung verlangt immer eine Signatur. Die Aktualisierung eines zugangsbeschränkten Rezepts setzt nun außerdem voraus, dass der verifizierte Schlüssel dem gespeicherten Autor entspricht. Allen anderen wird mitgeteilt, das Rezept existiere nicht, sodass der Endpunkt nicht bestätigt, welche kostenpflichtigen Datensätze vorhanden sind.

### nostrord repariert verpackte DMs und geteilte event-Links

Nach [v2.9.0 aus der vergangenen Woche](/de/newsletters/2026-08-26-newsletter/#nostrord-v290-relay-scoped-group-state-and-media) hat [nostrord](https://github.com/nostrord/nostrord), ein plattformübergreifender Client für von relays gehostete Communitys, Korrekturen an der Zustellung gemergt, damit eine von einem Gerät gesendete [NIP-17](/de/topics/nip-17/)-Nachricht (Gift-Wrapped private DM) dasselbe Konto auf einem anderen Gerät erreicht. [Die unabhängige Veröffentlichung der Selbstkopie des Absenders](https://github.com/nostrord/nostrord/pull/295) verhindert, dass die erste Annahme des Empfänger-Wraps durch ein relay die von anderen Geräten abgerufene Kopie verwirft. Dieselbe Änderung sendet einen Wrap nach Abschluss der [NIP-42](/de/topics/nip-42/)-Authentifizierung (Client-Authentifizierung gegenüber relays) erneut und markiert die Sendung bei der ersten Annahme durch ein relay als erfolgreich, damit ein ausfallender Host die übrigen nicht blockieren kann. [Geparkte Gift Wraps, deren Entschlüsselung nach NIP-59 fehlschlug, werden erneut versucht](https://github.com/nostrord/nostrord/pull/297). Das geschieht nun zeitgesteuert, sodass ein dauerhaft verbundener Bunker diese Nachrichten nicht mehr mi... [gekürzt]

Eine Antwort nach [NIP-C7](/de/topics/nip-c7/) (Chatnachrichten des kind `9`) wiederholt den übergeordneten Beitrag als führenden [NIP-19](/de/topics/nip-19/)-Zeiger (Bech32-kodierte Entitäten) vom Typ `nevent` neben dem `q` tag. Wird [dieser führende Elternzeiger verworfen](https://github.com/nostrord/nostrord/pull/292), wenn er den Body eröffnet und den Antwort-Elternbeitrag benennt, kann die Zeile als einzelnes Antwortzitat gerendert werden. Ein Zeiger in der Mitte des Bodys oder ein Zeiger, der den gesamten Body ausmacht, wird weiterhin als Zitatkarte gerendert. [Links zu zitierten events kodieren nun `nevent`](https://github.com/nostrord/nostrord/pull/293) mit Autor, kind und dem relay, von dem das Zitat gelesen wurde. Ein in eine DM geteiltes event nach [NIP-29](/de/topics/nip-29/) (relay-verwaltete Gruppen) kann so von einem anderen Client abgerufen werden, statt nur eine blanke Notizkennung ohne Suchhinweise zu tragen.

## NIP-Aktualisierungen und Arbeit an Protokollspezifikationen

### Nostr Implementation Possibilities

Diese Woche wurden zwei Spezifikationsänderungen in das zentrale [NIPs-Repository](https://github.com/nostr-protocol/nips) gemergt.

[NIP-67](/de/topics/nip-67/) definiert Hinweise, die ein relay an eine `EOSE`-Nachricht (Ende der gespeicherten events) anhängen kann, damit ein Client weiß, ob er weiter paginieren soll. Der [gemergte `"auth"`-Hinweis](https://github.com/nostr-protocol/nips/pull/2371) ergänzt neben `finish` und `more` einen dritten Wert: Ein relay kann nun signalisieren, dass nach der Authentifizierung des Benutzers weitere gespeicherte events sichtbar werden könnten, und muss vor der `EOSE`, die diesen Hinweis trägt, die `AUTH`-Challenge nach [NIP-42](/de/topics/nip-42/) (relay-Authentifizierung) senden. Die [begleitende Ergänzung zu NIP-42](https://github.com/nostr-protocol/nips/pull/2371) definiert denselben Ablauf aus Sicht des Clients. Ein Client, der eine `EOSE` mit `auth` empfängt, besitzt daher bereits die Challenge, auf die er antworten muss.

[NIP-84](/de/topics/nip-84/) (portable Hervorhebungen, die oben von Amethyst als events des kind `9802` unterstützt wurden) [hat eine Aktualisierung des Tag-Schemas gemergt](https://github.com/nostr-protocol/nips/pull/2454): Hervorhebungen können ihre Quelle nun zusätzlich zu `a`/`e` tags für Nostr-events und `r` tags für alles andere mit strukturierten `i` tags gemäß [NIP-73](/de/topics/nip-73/) (Kennungen externer Inhalte) versehen. Beim Rendern von Zitathervorhebungen wurde außerdem wie bei einem Zitat-Repost aus MUST ein SHOULD.

### Nostr Wallet Connect

Eine `list_transactions`-Antwort kann angeben, wie viele Transaktionen auf die Anfrage passen, statt nur die Zahl der von der aktuellen Seite zurückgegebenen Zeilen. Das [gemergte optionale Feld `total_count`](https://github.com/nostr-wallet-connect/nwc/pull/4) in NWC-05 (der Wallet-Verlaufserweiterung) im [NWC-Erweiterungsrepository](https://github.com/nostr-wallet-connect/nwc) ergänzt dieses Feld in der Antwort, die mit [NIP-47](/de/topics/nip-47/) (verschlüsselte Fernsteuerung einer Wallet über Nostr) verwendet wird.

Der [Commit, der `total_count` ergänzt](https://github.com/nostr-wallet-connect/nwc/commit/ff3e49a47d040075edc46ee42fc0e33f10f1ef67), dokumentiert es als optionale Ganzzahl: die Gesamtzahl der Transaktionen, die den Anfragefiltern entsprechen.

Der [Commit, der die Paginierung aus der Zählung ausschließt](https://github.com/nostr-wallet-connect/nwc/commit/06315e735f744b1afd3df0b57436fdce8a7bfc2e), hält fest, dass diese Gesamtzahl die Paginierung nicht berücksichtigt und somit alle passenden Transaktionen über sämtliche Seiten zählt.

## NIP Deep Dive: Reposts und Reaktionen

Ein Kontakt kann eine bestehende Notiz wieder vor seinen Followern platzieren und ein kompaktes Like, Dislike oder Emoji anhängen, ohne eine Antwort zu schreiben. [NIP-18](/de/topics/nip-18/) (Reposts) veröffentlicht diese Weiterverteilung als eigenes signiertes event. [NIP-25](/de/topics/nip-25/) (Reaktionen) veröffentlicht die kompakte Reaktion als separates signiertes event. Beide sind in der [kanonischen Repost-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/18.md) beziehungsweise der [kanonischen Reaktionsspezifikation](https://github.com/nostr-protocol/nips/blob/master/25.md) weiterhin als `draft` und `optional` gekennzeichnet: Sie sind im NIPs-Repository vorhanden und werden von Clients implementiert, gelten aber noch nicht als final.

### Reposts (NIP-18)

Follower erhalten einen signierten Zeiger auf eine bereits veröffentlichte Textnotiz des kind 1, wenn ein Client ein event des kind 6 schreibt. Die [Repost-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/18.md) setzt `kind` auf 6, legt das stringifizierte JSON dieser Notiz in `content` ab (leerer `content` ist zulässig, aber nicht empfohlen), verlangt ein `e` tag, dessen Wert die `id` der Notiz ist und dessen dritter Eintrag eine relay-URL bezeichnet, von der die Notiz abgerufen werden kann, und besagt, dass das event außerdem ein `p` tag mit dem `pubkey` des ursprünglichen Autors enthalten SOLLTE. Bei einem Repost eines geschützten event nach [NIP-70](/de/topics/nip-70/) SOLLTE `content` leer bleiben, damit die geschützte Payload nicht in das neue event kopiert wird.

Ein Zitat ist ein Verweis innerhalb eines anderen event und kein Wrapper des kind 6. Wenn ein Client ein `nevent`, `note` oder `naddr` gemäß [NIP-21](/de/topics/nip-21/) (`nostr:`-URI) erwähnt, muss er diese Erwähnung in ein `q` tag der Form `["q", "<event-id> or <event-address>", "<relay-url>", "<pubkey-if-a-regular-event>"]` umwandeln. [Zitat-Repost-tags](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts) halten diese Verweise aus Antwort-Threads heraus und ermöglichen Clients, die Zitate eines Beitrags abzurufen und zu zählen.

Kind 6 ist für Notizen des kind 1 reserviert. Ein generischer Repost des kind 16 kann jedes event-kind außer kind 1 verpacken. Er SOLLTE ein `k` tag enthalten, dessen Wert der stringifizierte kind des inneren event ist. Ist dieses innere event ersetzbar, SOLLTE der generische Repost ein `a` tag mit der Koordinate `kind:pubkey:d-tag` ergänzen. Fehlt dieses `a` tag, zielt der Repost auf eine bestimmte Version, und `content` muss den vollständigen JSON-String dieser Version enthalten. Die [Regeln für generische Reposts](https://github.com/nostr-protocol/nips/blob/master/18.md#generic-reposts) verhindern, dass Longform-, adressierbare und andere Nicht-Notiz-events so veröffentlicht werden, als wären sie kind 1.

Das folgende event des kind 6 ist ein bei der Zusammenstellung von `wss://relay.damus.io` abgerufener Live-Repost ([event öffnen](https://njump.me/nevent1qqs88k8xgv2d3d3yymawaa24f22a0kqqvknpur0p05vq9e5r4y74xjspz3mhxue69uhhyetvv9ujuerpd46hxtnfdu7elvca)):

```json
{
  "kind": 6,
  "id": "73d8e64314d8b62426faeef5554a95d7d80065a61e0de17d1802e683a93d534a",
  "pubkey": "a60e79e0edad5100d7543b669e513dbc1c2170e8e9b74fdb8e971afd1e0e6813",
  "created_at": 1787768621,
  "tags": [
    [
      "e",
      "38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976"
    ],
    [
      "p",
      "34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095"
    ],
    [
      "client",
      "Primal iOS"
    ]
  ],
  "content": "{\"pubkey\":\"34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095\",\"sig\":\"8c0271f7b438083ce491c391335598e0cbceee0758177cf98f7894531033cb5153704b01009590f3d4e9cdfadd5bbf73fc5eea54186fcbac6d30744e0e6c1cd6\",\"id\":\"38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976\",\"tags\":[[\"r\",\"https:\/\/stacker.news\/items\/1555439\"],[\"client\",\"Damus\"]],\"created_at\":1787766056,\"content\":\"🚨 Attention CLN (Core Lightning) node runners 🚨\n\nhttps:\/\/stacker.news\/items\/1555439\",\"kind\":1}",
  "sig": "b6b97fa377cfdb651e2850f65f2ccb12ca0724c0de0fc0e39e9721f850abdfd31f5d5567517a51d988145c2a2de9ae9540b02eecf7352e554022870d5e8c64a5"
}
```

Sein `kind` ist 6, das `e` tag zeigt auf die repostete Notiz, das `p` tag identifiziert deren Autor, und `content` enthält das ursprüngliche event des kind 1 als stringifiziertes JSON. Diesem von einem relay abgerufenen event fehlt der relay-Hinweis, den die [NIP-18-Spezifikation](https://github.com/nostr-protocol/nips/blob/master/18.md) als erforderlich kennzeichnet. Das veranschaulicht, warum Leser und Clients reale events validieren und mit Produzenten umgehen müssen, die Felder auslassen.

### Reaktionen (NIP-25)

Ein Beitrag kann signierte Likes, Dislikes und Emojis sammeln, ohne dass diese Markierungen im Antwort-Thread erscheinen. Die [Reaktionsspezifikation](https://github.com/nostr-protocol/nips/blob/master/25.md) definiert eine solche Markierung als event des kind 7, dessen `content` den Reaktionswert enthalten MUSS. `+` oder ein leerer String MÜSSEN als Like oder Upvote gelesen werden. `-` MUSS als Dislike oder Downvote gelesen werden. Ein Emoji oder ein Shortcode für benutzerdefinierte Emojis nach [NIP-30](/de/topics/nip-30/) SOLLTE NICHT als Like oder Dislike gelesen werden, und ein Client DARF dieses Emoji am Beitrag anzeigen.

Das Ziel steht in den tags und wird nicht aus `content` abgeleitet. Es MUSS ein `e` tag geben, das auf die `id` des Ziel-event gesetzt ist, und dieses tag SOLLTE einen relay-Hinweis enthalten. Zusätzliche `e` tags werden nicht empfohlen; falls sie vorkommen, muss die Ziel-`id` zuletzt stehen. Für den Zielautor SOLLTE ein `p` tag vorhanden sein, das bei mehreren `p` tags zuletzt steht. Ein adressierbares Ziel SOLLTE außerdem ein `a` tag mit der Koordinate `kind:pubkey:d-tag` erhalten. Die `e` und `a` tags SOLLTEN relay- und pubkey-Hinweise enthalten, die `p` tags SOLLTEN relay-Hinweise enthalten, und ein `k` tag DARF den stringifizierten kind des event tragen, auf das reagiert wurde. [Diese Tag-Regeln](https://github.com/nostr-protocol/nips/blob/master/25.md#tags) ermöglichen einem Client, allein anhand des Reaktions-event das Ziel abzurufen und dessen Autor zu benachrichtigen.

Ein Client DARF in `content` einen einzelnen `:shortcode:` sowie ein `emoji` tag ablegen, das diesen Shortcode gemäß den [Regeln für Reaktionen mit benutzerdefinierten Emojis](https://github.com/nostr-protocol/nips/blob/master/25.md#custom-emoji-reaction) einer Bild-URL zuordnet. Ist das Ziel kein natives Nostr-event, MUSS die Reaktion kind 17 haben und gemäß den [Regeln für Reaktionen auf externe Inhalte](https://github.com/nostr-protocol/nips/blob/master/25.md#external-content-reactions) `k` und `i` tags nach [NIP-73](/de/topics/nip-73/) (Kennungen externer Inhalte) tragen. Kind 17 ist eine Reaktion auf eine Webseite, Podcastfolge oder ein anderes externes Objekt. Es ist weder eine Event-zu-Event-Reaktion des kind 7 noch ein Repost.

Das folgende event des kind 7 ist eine bei der Zusammenstellung von `wss://relay.damus.io` abgerufene Live-Reaktion ([event öffnen](https://njump.me/nevent1qqsytac63l00k7kyaphkfwqqn94wglmx78v6zhqtytg65w5k957luccpz3mhxue69uhhyetvv9ujuerpd46hxtnfdus63jym)):

```json
{
  "kind": 7,
  "id": "45f71a8fdefb7ac4e86f64b800996ae47f66f1d9a15c0b22d1aa3a962d3dfe63",
  "pubkey": "0755cc2b972c3cbcae36913109c50b36b3fe110fa38a76dc37d1f01c5305496a",
  "created_at": 1787768605,
  "tags": [
    [
      "e",
      "519de32071d71bb2ab8b71a07e03eb9a256b6a59f9b08877b156c80966d5c320"
    ],
    [
      "a",
      "34236:5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb:2ddda68516f4729d3ef55a1eb01fe028253393212493a34816ad8eb79f97a3b7"
    ],
    [
      "p",
      "5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb"
    ],
    [
      "k",
      "34236"
    ],
    [
      "client",
      "Divine",
      "31990:d95aa8fc0eff8e488952495b8064991d27fb96ed8652f12cdedc5a4e8b5ae540:divine-mobile",
      "wss://relay.divine.video"
    ]
  ],
  "content": "+",
  "sig": "3c081756c7a73e2ee8aa10fadf3b5009390d5ac9a72078ba03701c42af91022ef275df7cb17724689a23dca4e29ff1a7cd5e3a24135d021983e2726a28b00b1e"
}
```

Sein `content` ist `+`, das konventionelle Like aus [NIP-25](https://github.com/nostr-protocol/nips/blob/master/25.md). Das `e` tag benennt das event, auf das reagiert wurde; das `a` tag ergänzt dessen adressierbare Koordinate; das `p` tag identifiziert seinen Autor; und das optionale `k` tag zeichnet den kind des Ziels als String auf.

### Aktuelle Client-Implementierungen

[Amethyst](https://github.com/vitorpamplona/amethyst), ein Android-Nostr-Client, definiert in seiner aktuellen Protokollschicht den [Repost-event-Typ](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip18Reposts/RepostEvent.kt) und den [Reaktions-event-Typ](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip25Reactions/ReactionEvent.kt).

[Snort](https://github.com/v0l/snort), ein Web-Nostr-Client, implementiert [NIP-18-Helfer einschließlich der Verarbeitung von Tags für Zitatlinks](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip18.ts) und [erstellt NIP-25-tags für Event-Reaktionen](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip25.ts).

[Ditto](https://github.com/soapbox-pub/ditto), ein kombinierter Mastodon-Server und Nostr-relay, [veröffentlicht generische Reposts des kind 16 mit einem `k` tag und einer `a`-Koordinate für adressierbare Ziele](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/components/RepostMenu.tsx) und [wendet die Reaktionssemantik von kind 7 an, indem es das letzte `e` tag als Ziel-event behandelt](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/lib/nostrEvents.ts).

### Wie sie zusammenwirken

Ein event des kind 6 oder kind 16 verteilt ein bestehendes event erneut in den Feeds der Follower des Reposters, entweder durch Einbetten des JSON dieses event oder durch Verweisen auf eine ersetzbare Koordinate. Ein `q` tag kennzeichnet ein Zitat innerhalb eines anderen event. Die Thread-Rekonstruktion kann so Verweise zählen, ohne das zitierende event als Antwort zu behandeln; diese Trennung beschreibt der [Abschnitt zu Zitat-Reposts](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts). Ein event des kind 7 lässt das ursprüngliche event an Ort und Stelle und hängt nur den Reaktionswert samt Ziel-tags an, wie es die [Reaktionsspezifikation](https://github.com/nostr-protocol/nips/blob/master/25.md) festlegt. Clients, die einen pubkey abrufen, sehen deshalb die Reposts dieses pubkey als neue events des kind 6 oder 16 und seine Meinungen als events des kind 7 zu Beiträgen anderer Personen.

---

Sendet eine NIP-17-DM, um ein Projekt oder eine Nachricht über das [Nostr-Compass-Projekt](https://github.com/andotherstuff/nostr-compass) zu teilen.
