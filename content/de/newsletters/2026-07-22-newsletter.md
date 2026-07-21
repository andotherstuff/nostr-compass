---
title: 'Nostr Compass #32'
date: 2026-07-22
translationOf: /en/newsletters/2026-07-22-newsletter.md
translationDate: 2026-07-22
draft: false
type: newsletters
description: "IndieSats legt seine Publisher-Rolle ab und startet als offene Nostr-Musikinfrastruktur neu, Nostrord v2.3.0 liefert die Client-Seite einer NIP-29-Spec-Woche mit fünf PRs, Zapstore 1.1.0 macht den Geräteschlüssel portierbar und bringt Hintergrund-Auto-Updates, Favorite-Follow-Sets mergen und nummerieren sofort um, und das Iris-Ökosystem liefert eine Pubsub-Bibliothek, eine Browser-FIPS-Runtime und nostr-social-graph 2.0."
---

Willkommen zurück beim Nostr Compass, eurem wöchentlichen Wegweiser für Nostr.

**Diese Woche:** [IndieSats](#indiesats-drops-its-publisher-role-and-relaunches-as-open-nostr-music-infrastructure) gibt die Schlüsselverwahrung, seine Whitelist und seinen obligatorischen Umsatzanteil auf und startet als offenes Relay, Player und Discovery-Schicht neu, auf der Künstler unter ihren eigenen Schlüsseln veröffentlichen. [Nostrord v2.3.0](#nostrord-v230-ships-group-moderation-mute-lists-and-onion-relays) bringt Gruppenmoderation, Mute-Listen und Onion-Relays in derselben Woche, in der fünf [NIP-29-Spec-PRs gemergt wurden](#protocol-work-and-nip-updates). [Zapstore 1.1.0](#zapstore-110-makes-the-device-key-portable-and-adds-background-auto-updates) führt einen portierbaren verschlüsselten Geräteschlüssel mit Amber-Backup und optionale Hintergrund-Auto-Updates ein. Der [Favorite-Follow-Sets-Listen-Kind](#the-favorite-follow-sets-list-kind-merges-and-immediately-moves-house) wurde gemergt und öffnete innerhalb weniger Tage einen Umnummerierungs-PR. Und das [Iris-Ökosystem](#the-iris-ecosystem-ships-a-pubsub-library-a-browser-fips-runtime-and-a-social-graph-20-in-one-week) liefert nostr-pubsub, die fips-ts-Browser-Runtime und nostr-social-graph 2.0.0 in einer einzigen Woche.

Getaggte Releases bringen [Amber v6.3.0](#amber-v630-groups-bunker-signing-approvals-and-adds-expert-list-support) mit gruppierten Bunker-Signierungs-Freigaben, [Wisp v1.2.0](#wisp-v120-adds-a-multi-account-switcher-and-collapsible-reply-threads) mit einem Multi-Account-Wechsler, [Sonar v0.1-alpha.11](#sonar-v01-alpha11-continues-the-alpha-line) als Fortsetzung der Alpha-Linie und das neue Projekt [ClipRelay v0.1.2](#cliprelay-v012-new-project-syncs-clipboards-across-devices-over-nostr-relays), das Zwischenablagen über Nostr-Relays synchronisiert.

Auf der unveröffentlichten Seite mergt [nostream](#nostream-merges-seven-prs-without-cutting-a-release) den Access-Control-Stack, den der Deep Dive dieser Woche behandelt, und [Amethyst](#amethyst-lands-v1130-pre-release-qa-on-napplet-isolation-and-concord-authority) liefert v1.13.0-Pre-Release-QA über 81 gemergte PRs.

Das NIPs-Repository mergt diese Woche fünf PRs, darunter das [NIP-29-Cluster](#protocol-work-and-nip-updates) und [kind:10011 Favorite Follow Sets](#the-favorite-follow-sets-list-kind-merges-and-immediately-moves-house), und eröffnet Debatten über [NIP-47-Vereinfachung](#protocol-work-and-nip-updates) und [Trusted Relay Assertions](#protocol-work-and-nip-updates). Der Deep Dive behandelt [NIP-42 und NIP-43, das Relay-Access-Control-Paar](#nip-deep-dive-nip-42-and-nip-43).

---

## Lead-Storys

### IndieSats legt seine Publisher-Rolle ab und startet als offene Nostr-Musikinfrastruktur neu

[IndieSats](https://zapstore.dev) ist eine Nostr-basierte Musikplattform, die bis diese Woche als Publisher agierte: Sie hielt Schlüssel für Künstler, betrieb eine Whitelist und nahm einen obligatorischen Anteil von 2 % der Einnahmen. In einer [Pivot-Ankündigung vom 20. Juli](https://njump.me/nevent1qqsr4awwnfndnnz77zanjxarw6nd0uld0ckayxp2navz0u9tzzwfweqpzamhxue69uhhyetvv9ujuurjd9kkzmpwdejhgtczyquwq70hxz22lzytw65rnnjewg0lj8a74khxa8h9j47q38pdnqy3kqcyqqqqqqgz8083u) gab das Projekt alle drei Rollen auf einmal auf. Die neu gestartete Plattform besteht stattdessen aus drei Teilen offener Infrastruktur: einem offenen Relay, einem Player und einer Discovery-Schicht, wobei Künstler Musik unter ihren eigenen Nostr-Profilen veröffentlichen statt unter einer von der Plattform verwahrten Identität. Umsatzbeteiligungen werden optional statt verpflichtend, und die Plattform berücksichtigt nun [NIP-09](/de/topics/nip-09/) kind:5-Löschanfragen, damit Künstler ihre Werke entfernen können. Für einen Bereich, der sonst darüber spricht, dass Protokolle Plattformen ersetzen, ist dies ein gelebter Fall einer Plattform, die sich freiwillig in Protokollteile zerlegt.

### Nostrord v2.3.0 liefert Gruppenmoderation, Mute-Listen und Onion-Relays

[Nostrord](https://github.com/nostrord/nostrord), der Gruppenchat-Client für Android, iOS, Web und Desktop, lieferte [v2.3.0](https://github.com/nostrord/nostrord/releases/tag/v2.3.0) mit verdrahteten Gruppenmoderations-Aktionen auf allen UIs ([PR #192](https://github.com/nostrord/nostrord/pull/192)), einwilligungsbasierten Gruppeneinladungen mit Cross-Relay-Erkennung ([PR #195](https://github.com/nostrord/nostrord/pull/195)), plattformübergreifenden [NIP-51](/de/topics/nip-51/)-Mute-Listen ([PR #188](https://github.com/nostrord/nostrord/pull/188)) und Tor-.onion-Relay-Unterstützung. Das Release erscheint in derselben Woche, in der die zugrunde liegende [NIP-29](/de/topics/nip-29/)-Spec fünf PRs zu Untergruppen, Nachrichten-Pinning, Bannern und Einladungscodes mergte (Details im [Protokoll-Abschnitt](#protocol-work-and-nip-updates) dieser Woche) — Gruppenchat auf Nostr hat nun also sowohl eine tiefere Spec als auch einen Client, der den Großteil davon ausübt, was die Feedbackschleife für alle anderen verkürzt, die auf Relay-Gruppen aufbauen.

### Zapstore 1.1.0 macht den Geräteschlüssel portierbar und fügt Hintergrund-Auto-Updates hinzu

[Zapstore](https://github.com/zapstore/zapstore) ist ein Nostr-nativer App-Store, in dem Releases von Entwicklerschlüsseln signiert werden und kein zentraler Betreiber für sie bürgt. [Version 1.1.0](https://github.com/zapstore/zapstore/releases/tag/1.1.0), das erste hier behandelte Release seit Anfang März, schließt die beiden größten Lücken zu konventionellen App-Stores. Die erste sind Updates: Optionale Hintergrund-Auto-Updates laden nun über WLAN herunter und installieren still oder gestuft, sodass Apps ohne manuelle Gänge durch den Store aktuell bleiben. Die zweite ist Identitätskontinuität: Der Geräteschlüssel wird portierbar, verschlüsselt und über [Amber](https://github.com/greenart7c3/Amber) via [NIP-55](/de/topics/nip-55/), der Android-Signer-Schnittstelle, sicherbar, sodass ein Nutzer beim Handywechsel nicht mehr als unbekanntes Gerät von vorn beginnt. Das Release verschiebt außerdem den App-Katalog als gerätesignierte kind:10067-Events auf Relays, fügt [NIP-56](/de/topics/nip-56/)-verifiziertes Melden aus dem Overflow-Menü hinzu, damit Nutzer problematische Apps auf eine für andere Clients konsumierbare Weise markieren können, und verifiziert den an ein Release angehängten C1-Proof, bevor eine Installation beginnt — was die Verbindung zwischen dem, was ein Entwickler signiert hat, und dem, was ein Gerät ausführt, enger zieht.

### Der Favorite-Follow-Sets-Listen-Kind mergt und zieht sofort um

Eine Spec-Koordinationsgeschichte spielte sich innerhalb einer einzigen Woche ab. [PR #2413](https://github.com/nostr-protocol/nips/pull/2413) wurde am 15. Juli gemergt und standardisiert einen ersetzbaren Listen-Kind für Favorite Follow Sets unter [NIP-51](/de/topics/nip-51/) (Listen): ein dedizierter Kind, auf dem Clients die kuratierten Sets gefolgter Accounts eines Nutzers veröffentlichen können, statt generische Listen-Kinds zu überladen. Innerhalb weniger Tage stellte sich heraus, dass der zugewiesene kind:10011 bereits anderweitig in Gebrauch war, sodass nun ein Folge-[PR #2417](https://github.com/nostr-protocol/nips/pull/2417) offen ist, um die Liste auf kind:10021 umzunummerieren. Gegen den gemergten Kind ist noch nichts ausgeliefert, was diesen Moment zum billigen Zeitpunkt für die Umnummerierung macht; sobald Clients anfangen, kind:10011-Events zu veröffentlichen, würde die Kollision teuer aufzulösen. Entwickler, die listenkonsumierende Features bauen, sollten den Umnummerierungs-PR verfolgen, nicht den gemergten Text, bis die Sache geklärt ist.

### Das Iris-Ökosystem liefert eine Pubsub-Bibliothek, eine Browser-FIPS-Runtime und einen Social Graph 2.0 in einer Woche

Drei Releases aus der Iris-Umlaufbahn landeten gemeinsam, und sie greifen ineinander. [nostr-pubsub](https://github.com/mmalmi/nostr-pubsub) ist eine transportneutrale Publish/Subscribe-Bibliothek für Nostr-Events; ihre [ersten getrackten Releases, v0.1.3 bis v0.5.2](https://github.com/mmalmi/nostr-pubsub/releases), liefern einen Browser-Relay-Carrier auf Basis von nostr-tools' SimplePool, Event-Verifizierung an der Transportgrenze, sodass ungültige Signaturen niemals Subscriber erreichen, und begrenzte historische Abfragen. [fips-ts](https://github.com/mmalmi/fips-ts) bringt [FIPS](/de/topics/fips/), den Noise-over-secp256k1-Peer-Transport, der bislang als Rust-Stack verfügbar war, als TypeScript-Runtime in den Browser: Die Releases [0.0.24 bis 0.0.30](https://github.com/mmalmi/fips-ts/releases) fügten einen WebRTC-Datachannel-Carrier, Nostr-basiertes Signaling für Peer-Discovery, einen Recent-Peer-Cache und einen IndexedDB-Adapter für Browser-Speicher hinzu, und die Runtime ist wire-kompatibel mit der Rust-Referenzimplementierung. Das dritte Stück, [nostr-social-graph v2.0.0](https://github.com/mmalmi/nostr-social-graph/releases/tag/v2.0.0), ist eine Major-Version der Social-Graph-Bibliothek: signierte Roster-Operationen für Nostr-Identitätsgraphen, Device-Approval-Flows, gebootstrapt aus einer kanonischen Drei-Felder-URI, und FIPS-Transport-Identitätsfacetten mit gemeinsamen Rust- und TypeScript-Testvektoren. Der verbindende Rahmen ist der [Iris Stack](https://stack.iris.to/), das Integrationslabor des Projekts, das diese Bibliotheken mit Blossom, Hashtree und verschlüsseltem Messaging zusammenbindet. Zusammengenommen kann eine Web-App nun Peers über Nostr entdecken, einen verschlüsselten FIPS-Kanal zu ihnen öffnen und einen signierten Social Graph pflegen — alles in TypeScript.

---

## Getaggte Releases

### Amber v6.3.0 gruppiert Bunker-Signierungs-Freigaben und fügt Expert-List-Unterstützung hinzu

[Amber](https://github.com/greenart7c3/Amber) ist ein Android-[NIP-46](/de/topics/nip-46/)-Remote-Signer. [v6.3.0](https://github.com/greenart7c3/Amber/releases/tag/v6.3.0) fügt gruppierte Multi-Request-Freigabe für Bunker-Signierungen hinzu, sodass ein Stapel ausstehender Signaturanfragen gemeinsam geprüft und freigegeben werden kann statt eine Eingabeaufforderung nach der anderen. Das Release fügt außerdem Unterstützung für Expert-List- (kind 12022) und Expert-Pack-Events (kind 32022) hinzu, einen Privacy-Modus, der sensible Inhalte auf dem Bildschirm verbirgt, und eine Änderung, die zuerst die [NIP-65](/de/topics/nip-65/)-Relay-Liste eines Accounts abruft und erst danach dessen Profil-Metadaten, sodass Signer-Flows vom tatsächlichen Relay-Set des Nutzers ausgehen. Dies folgt der v6.2.x-Linie aus der Ausgabe vom 08.07.2026.

### Nostrord v2.2.0-Nachtrag

Da [v2.3.0](#nostrord-v230-ships-group-moderation-mute-lists-and-onion-relays) den News-Abschnitt dieser Woche anführt, vermerkt der Tagged-Release-Slot nur, was der Lead nicht abdeckt: v2.3.0 folgt auf die DM-Steuerungen aus v2.2.0, behandelt in #31 — damit ist dies das zweite wöchentliche Release des Clients in Folge.

### Wisp v1.2.0 fügt einen Multi-Account-Wechsler und einklappbare Antwort-Threads hinzu

[Wisp](https://github.com/barrydeen/wisp) ist ein datenschutzorientierter Nostr-Client mit integrierter Wallet-Unterstützung. [v1.2.0](https://github.com/barrydeen/wisp/releases/tag/v1.2.0) fügt einen Multi-Account-Wechsler zum Wechseln zwischen Profilen ohne erneutes Login hinzu, einklappbare Antwort-Threads für lange Unterhaltungen, das Entfernen von Tracking-Parametern aus Note-Links, bevor sie geöffnet werden, und eine Wallet-Transaktionshistorie. Das Release folgt dem Wisp-Update aus der Ausgabe vom 08.07.2026.

### ClipRelay v0.1.2 (neues Projekt) synchronisiert Zwischenablagen über Nostr-Relays zwischen Geräten

[ClipRelay](https://github.com/tajava2006/cliprelay) ist eine neu gestartete plattformübergreifende App (Android, macOS, Windows, Linux), die deine Zwischenablage zwischen deinen eigenen Geräten synchronisiert: auf einem Rechner kopieren, auf einem anderen einfügen. Der gesamte Verkehr läuft über Nostr-Relays als [NIP-44](/de/topics/nip-44/)-verschlüsselte Events, die an dich selbst adressiert sind — es gibt also keinen Server zu betreiben und keinen Account zu erstellen; der private Schlüssel bleibt außerhalb der App. [v0.1.2](https://github.com/tajava2006/cliprelay/releases) behebt einen subtilen Sync-Fehler, bei dem ein aus dem Ruhezustand erwachender Rechner weiter veröffentlichte, aber still den Empfang einstellte, und verschärft die Relay-Status-Anzeigen, die zuvor tote Subscriptions als gesund meldeten. Dies ist ClipRelays erster Auftritt im Newsletter.

### Sonar v0.1-alpha.11 setzt die Alpha-Linie fort

[Sonar](https://github.com/hedwig-corp/bitchat-to-sonar), die Lead-Story der letzten Woche, schnitt [v0.1-alpha.11](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.11) mit Arbeit an der Rust-Mesh-Link-Engine, BLE- und Mesh-Fixes sowie Relay-Diagnostik; ein inkrementeller Nachtrag zur in #31 behandelten Alpha-Linie.

### Die kleineren Launches der Woche

Drei kleinere Releases verdienen je eine Zeile: [noscall v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release), die Nostr-Anruf-App, migrierte ihre Push-Benachrichtigungen auf UnifiedPush und hält das Call-Signaling damit von Googles Push-Infrastruktur fern; [nostr-vpn v4.1.1](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.1.1), ein Mesh-VPN, das Nostr für Signaling nutzt, lieferte ein Update auf Zapstore; und zwei neue Apps debütierten dort ebenfalls: StableKraft, ein Nostr-plus-Lightning-Musik- und Podcast-Aggregator, und Hakari, ein verschlüsseltes Nostr-Backup für einen Gewichts-Logger.

### Amethyst liefert v1.13.0-Pre-Release-QA zu Napplet-Isolation und Concord-Authority

[Amethyst](https://github.com/vitorpamplona/amethyst) mergte diese Woche 81 PRs im Vorfeld des v1.13.0-Releases. [PR #3650](https://github.com/vitorpamplona/amethyst/pull/3650) ist ein Pre-Release-QA-Durchlauf, der Napplet-Account-Isolation, Concord-Authority-Fixes und rund 30 weitere Fixes abdeckt, mit weiteren v1.13.0-Vorbereitungs-PRs bis zum 21.07. Dies setzt die Berichterstattung aus #31 über Amethysts Clean-Room-Implementierung des Concord-Clients fort und zieht das Authority- und Isolationsverhalten dieser Arbeit enger, bevor sie getaggt ausgeliefert wird.

---

## Unveröffentlichte Änderungen

### nostream mergt sieben PRs, ohne ein Release zu schneiden

[nostream](https://github.com/Cameri/nostream), die TypeScript-Relay-Implementierung, mergte diese Woche sieben PRs, ohne ein Release zu schneiden. Das Headline-Paar sind [PR #702](https://github.com/Cameri/nostream/pull/702) und [PR #676](https://github.com/Cameri/nostream/pull/676), die Relay-Betreibern zusammen einen funktionierenden Authentifizierungs-plus-Mitgliedschafts-Access-Control-Stack geben; der NIP Deep Dive dieser Woche geht genau diesen Handshake durch.

### FIPS v0.4.1 zieht den Transport enger, auf dem das Iris-Ökosystem aufbaut

[jmcorgan/fips](https://github.com/jmcorgan/fips) lieferte [v0.4.1](https://github.com/jmcorgan/fips/releases/tag/v0.4.1), ein Wartungsrelease, das den Antipoison-State deckelt, Convergence- und MTU-Handling fixt und die CPU-Last senkt. Für sich genommen ist das Klempnerarbeit, aber diese Woche ist es Bindegewebe: Die Browser-TypeScript-Runtime [fips-ts](https://github.com/mmalmi/fips-ts) aus dem Iris-Ökosystem-Cluster im News-Abschnitt dieser Ausgabe ist wire-kompatibel mit diesem Rust-Transport, sodass Fixes hier direkt zu dem propagieren, womit die Browser-Runtime interagiert.

---

## Protokollarbeit und NIP-Updates

Jüngste Änderungen am [NIPs-Repository](https://github.com/nostr-protocol/nips):

**Gemergt:**

- **[NIP-29](/de/topics/nip-29/) (Relay-based Groups): Untergruppen** ([PR #2319](https://github.com/nostr-protocol/nips/pull/2319), gemergt 2026-07-16): NIP-29 definiert relay-gehostete Gruppen, in denen Mitgliedschaft, Rollen und Chat-Verlauf auf einem einzelnen Relay als adressierbare `kind:39000`-Serien-Events leben, mit Moderationsaktionen in `kind:9000`-Serien-Admin-Events. Dieser PR erlaubt einer Gruppe, sich selbst als Untergruppe zu deklarieren, indem sie ihren Metadaten ein `parent`-Tag hinzufügt, das auf den `d`-Identifier einer anderen Gruppe auf demselben Relay zeigt. Untergruppen sind in jeder anderen Hinsicht gewöhnliche Gruppen: Mitgliedschaft kaskadiert nicht (der Beitritt zu einer Elterngruppe gewährt keine Mitgliedschaft in Kindgruppen), Admin-Rollen werden nicht vererbt (die `kind:39001`-Admins-Liste jeder Untergruppe ist für ihren eigenen Geltungsbereich maßgeblich), und jede Untergruppe behält ihre eigenen unabhängigen `kind:9000`/`kind:9001`-Mitglieder-Events. Relays, die die Hierarchie unterstützen, bewerben dies in ihrem NIP-11-Relay-Information-Dokument unter einem `nip29`-Objekt mit `"subgroups": true`, sodass Clients die Fähigkeit entdecken können, bevor sie verschachtelte Communities anlegen.

- **[NIP-29](/de/topics/nip-29/): Nachrichten-Pinning** ([PR #2379](https://github.com/nostr-protocol/nips/pull/2379), gemergt 2026-07-15; [PR #2416](https://github.com/nostr-protocol/nips/pull/2416), gemergt 2026-07-17): Gruppenadmins können nun Nachrichten innerhalb einer relay-basierten Gruppe anpinnen. Der Mechanismus fügt ein neues Moderations-Event hinzu, `kind:9010` `update-pin-list`, das die vollständige geordnete Pin-Liste als `e`-Tags trägt, die auf reguläre Event-IDs verweisen, sowie ein neues optionales gruppenweites Event, `kind:39005` *group pinned events*, das das Relay neu erzeugt, um die zuletzt akzeptierte Pin-Liste zu spiegeln. Da jedes `kind:9010` die gesamte Liste ersetzt statt einzelne Einträge umzuschalten, werden Pinnen, Entpinnen, Umordnen und Leeren der Pins alle durch das Einreichen einer neuen Liste ausgedrückt. Der Folge-PR #2416 erweitert das Format so, dass auch `a`-Tags in der Pin-Liste akzeptiert werden, wodurch Admins adressierbare Events (Longform-Posts, Wiki-Seiten und andere parametrisierte ersetzbare Inhalte) neben gewöhnlichen Chat-Nachrichten anpinnen können. Relays dürfen die Anzahl der Pins deckeln, und der gemergte Spec-Text empfiehlt, Pins in der Reihenfolge der Tags anzuzeigen.

- **[NIP-29](/de/topics/nip-29/): Banner-Tag und Invite-Code-Suffix** ([PR #2383](https://github.com/nostr-protocol/nips/pull/2383), gemergt 2026-07-16; [PR #2380](https://github.com/nostr-protocol/nips/pull/2380), gemergt 2026-07-16): Zwei Ergänzungen zu Gruppenmetadaten für Anzeige und Onboarding. PR #2383 fügt dem `kind:39000`-Gruppenmetadaten-Event ein optionales `banner`-Tag hinzu, das sich zu den bestehenden Feldern `name`, `picture` und `about` gesellt, damit Clients ein Header-Bild für eine Gruppenseite rendern können. PR #2380 definiert ein Invite-Code-Suffix für Gruppen-Share-Links: Ein Einladungscode darf an den `naddr`-Identifier der Gruppe als `naddr1...?invite=<code>` angehängt werden. Da der bech32-Zeichensatz kein `?` enthält, bleibt der Teil vor dem Suffix eigenständig ein gültiger naddr, sodass Clients, die die Erweiterung nicht verstehen, die Gruppe trotzdem auflösen können. Clients, die sie verstehen, füllen das `code`-Tag auf der `kind:9021`-Beitrittsanfrage vorab aus, was zusammen mit dem bestehenden `kind:9009` `create-invite`-Moderations-Event die Aufnahme in geschlossene Gruppen vereinfacht.

- **[NIP-51](/de/topics/nip-51/) (Listen): Favorite Follow Sets, kind:10011** ([PR #2413](https://github.com/nostr-protocol/nips/pull/2413), gemergt 2026-07-15): NIP-51 definiert die Standard-Listen-Kinds, aufgeteilt in ersetzbare `kind:10000`-Serien-Listen (eine pro Nutzer) und adressierbare `kind:30000`-Serien-Sets (viele pro Nutzer, per `d`-Tag adressiert). Dieser PR fügt `kind:10011` hinzu, *favorite follow sets*, eine standardisierte ersetzbare Liste, deren `a`-Tags auf `kind:30000`-Follow-Sets zeigen. Als Spiegel von `kind:10012` (Relay-Feeds), das `a`-Tags auf `kind:30002`-Relay-Sets hält, erlaubt der neue Kind einem Nutzer, benannte Follow-Sets zu bookmarken — etwa kuratierte Listen von Pubkey-Sammlungen, die von ihm selbst oder anderen veröffentlicht wurden — und Clients können sie für Folgen-per-Einmal-Tippen oder Feed-Wechsel anbieten. Beachte, dass diese Kind-Nummer bereits umstritten ist: siehe den offenen Umnummerierungs-PR unten.

- **[NIP-46](/de/topics/nip-46/) (Nostr Connect): Leitlinie zu Silent-Timeouts** ([PR #2375](https://github.com/nostr-protocol/nips/pull/2375), gemergt 2026-07-15): NIP-46 ist das Remote-Signing-Protokoll, bei dem ein Client verschlüsselte JSON-RPC-artige Anfragen über Relays an einen Signer (bunker) sendet und auf eine verschlüsselte Antwort wartet. Die gemergte Änderung ist ein Satz Wire-Verhalten: Anfragen mit unbekannten oder nicht unterstützten Methoden MÜSSEN mit einem Fehler beantwortet werden. Bisher konnte ein Signer, der eine Methode empfing, die er nicht implementiert hatte, einfach nie antworten — der Client hing dann, bis sein eigener Timeout zuschlug, ohne Möglichkeit, „nicht unterstützte Methode" von „Signer offline" zu unterscheiden. Die vorgeschriebene Fehlerantwort lässt Clients schnell scheitern und dem Nutzer eine aussagekräftige Meldung zeigen, statt endlos zu drehen.

**Offene PRs und Diskussionen:**

- **Umnummerierung von kind:10011 zu kind:10021** ([PR #2417](https://github.com/nostr-protocol/nips/pull/2417)): Verschiebt die frisch gemergte Favorite-Follow-Sets-Liste von `kind:10011` nach `kind:10021`, weil `10011` bereits anderweitig in Gebrauch ist. Der Umnummerierungs-PR war innerhalb weniger Tage nach dem ursprünglichen Merge offen, sodass Clients, die Favorite Follow Sets implementieren, diesem PR folgen und die finale Nummer anvisieren sollten, nicht `10011`.

- **[NIP-47](/de/topics/nip-47/) (Nostr Wallet Connect): Kernvereinfachung** ([PR #2419](https://github.com/nostr-protocol/nips/pull/2419)): Schlägt vor, NIP-47, das Wallet-Connect-Protokoll, mit dem Apps Lightning-Zahlungen von einer entfernten Wallet über Nostr anfordern, zu einer kleineren Kern-Spec zu verengen. Optionale und spezialisiertere Funktionalität würde aus `47.md` in ein dediziertes Extensions-Repository ausgelagert, [nostr-wallet-connect/nwc](https://github.com/nostr-wallet-connect/nwc), wo sich Extension-Specs unabhängig vom Kern weiterentwickeln können. Das erklärte Ziel ist, den Kern klein, stabil und leicht implementierbar zu halten — in der Linie früherer NWC-Calls, eine minimale Wallet-Connect-Schicht von reichhaltigerem optionalem Verhalten zu trennen. Angesichts der breiten Verbreitung von NIP-47 in Wallets und Apps sollte jeder, der NWC spricht, die Restrukturierungsdiskussion verfolgen.

- **Trusted Relay Assertions (Entwurf, noch keine Nummer vergeben)** ([PR #2418](https://github.com/nostr-protocol/nips/pull/2418)): Schlägt einen Standard zur Veröffentlichung von Vertrauensbewertungen über Nostr-Relays vor — positioniert als die „was wir daraus schließen"-Schicht neben [NIP-11](/de/topics/nip-11/) (was ein Relay über sich selbst behauptet) und [NIP-66](/de/topics/nip-66/) (was Monitore gemessen haben). Assertion-Anbieter würden Trust-Scores aus beobachteten Metriken, Betreiber-Reputation und Nutzerberichten berechnen; Clients würden diese Assertions abfragen, wenn sie wählen, mit welchen Relays sie sich verbinden. Der Entwurf führt `kind:30385` ein (adressierbare Trusted Relay Assertion mit Tags für Score, Zuverlässigkeit, Qualität, Erreichbarkeit, Betreiber, Richtlinie und Jurisdiktion), `kind:10385` (ersetzbare Trusted Provider List, die vom Nutzer gewählten Assertion-Anbieter), und nutzt [NIP-32](/de/topics/nip-32/)-Labels für Relay- und Betreiber-Reports wieder. Noch ist keine NIP-Nummer vergeben; dies ist ein früher Entwurf.

- **AND-Operator für Filter („NIP-91", vorgeschlagen, Nummer noch nicht im Repo)** ([PR #2252](https://github.com/nostr-protocol/nips/pull/2252)): Nach NIP-01 sind Tag-Filter reine ODER-Filter: Ein Filter `"#t": ["meme", "cat"]` matcht Events mit einem der beiden Tags. Dieser Vorschlag fügt einen `&`-Modifikator für indexierbare Tags hinzu, sodass `"&t": ["meme", "cat"]` nur Events zurückgibt, die beide Tags tragen — Relays können dann die Schnittmenge serverseitig bilden, statt dass Clients übermäßig fetchen und lokal filtern. Die Regeln legen fest, dass UND Vorrang vor ODER hat, dass Tag-Werte in UND von unterstützenden Relays im ODER ignoriert werden sollten und dass Clients zur Kompatibilität mit Relays ohne die Erweiterung ebenfalls die Standard-`#`-ODER-Tags mitschicken MÜSSEN (diese Relays liefern das breitere ODER-Ergebnis, das der Client lokal schneidet). Der PR ist eine wiedereröffnete Fortsetzung eines früheren Vorschlags und listet Relay-Implementierungen auf, darunter ein nostr-rs-relay-Docker-Image, netstr und einen Snort-Worker-Relay. Die NIP-91-Nummer erscheint nur im PR-Branch; sie steht noch nicht im NIP-Index der Repository-README, die Nummer ist also als vorläufig zu behandeln.

- **Nostr Web Applets („NIP-5D", vorgeschlagen, Nummer noch nicht im Repo)** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): Definiert ein `postMessage`-Protokoll, über das sandboxed Web-Anwendungen („Napplets") in iframes oder Webviews mit einer Host-Anwendung („Shell") kommunizieren. Die Spec ist bewusst ein dünner Kern: Sie spezifiziert den Nachrichten-Envelope, Sandbox-Regeln (Napplet-iframes MÜSSEN `sandbox="allow-scripts"` ohne `allow-same-origin` verwenden, und Shells DÜRFEN NICHT `window.nostr` NIP-07 im iframe exponieren), Sender-Identifikation über die unverfälschbare `MessageEvent.source`-Window-Referenz statt `event.origin` und manifest-basierte Capability-Aushandlung. Die eigentlichen Protokollnachrichten für Signieren, Relay-Zugriff, Speicher und Napplet-zu-Napplet-Kommunikation werden an NAP-Extension-Specs (Nostr Applet Protocol) delegiert, von denen jede eine Capability-Domäne besitzt; Signieren und Verschlüsselung werden stets von der Shell vermittelt, sodass Schlüssel niemals die Sandbox betreten. Der Vorschlag hängt von der NIP-5A-Napplet-Manifest-Spec ab und ist diese Woche aktuell: Amethysts v1.13.0-Pre-Release-Arbeit umfasst Napplet-Account-Isolation, was clientseitiges Napplet-Hosting zu einem aktiven Implementierungsfeld macht. Wie bei „NIP-91" oben ist die 5D-Nummer vorläufig.

---

## NIP Deep Dive: NIP-42 und NIP-43

Ein Relay zu betreiben, das nicht für alle offen ist, bedeutete früher, alles selbst zu erfinden. Der Betreiber eines bezahlten oder einladungsbasierten Relays musste eine Whitelist out-of-band pflegen — meist eine Textdatei mit über DMs gesammelten Pubkeys — ohne standardisierten Weg, einem verbundenen Client zu sagen „beweise, wer du bist", und ohne standardisierten Weg für einen Nutzer, um Aufnahme zu bitten oder zu wissen, ob er Mitglied war. Jedes Relay, das Lese- oder Schreib-Gates wollte, baute seinen eigenen privaten Mechanismus, und Clients konnten mit keinem davon interagieren. [NIP-42](/de/topics/nip-42/) standardisiert die Identitätsnachweis-Hälfte dieses Problems, und [NIP-43](/de/topics/nip-43/) standardisiert die Mitgliedschafts-Hälfte. Diese Woche mergte nostream, das TypeScript-Relay, das Paar von Ende zu Ende: [PR #702](https://github.com/Cameri/nostream/pull/702) beschränkt Lesevorgänge verschlüsselter Kinds auf authentifizierte Empfänger, und [PR #676](https://github.com/Cameri/nostream/pull/676) fügt Join- und Leave-Request-Event-Strategien hinzu, beide gemergt am 20. Juli.

### NIP-42: Authentifizierung von Clients gegenüber Relays

[NIP-42](/de/topics/nip-42/) beantwortet eine Frage: Wer ist auf dieser Verbindung? Ein Relay, das Lesen oder Schreiben gaten will, sendet eine `AUTH`-Nachricht mit einem Challenge-String, beim Verbindungsaufbau oder bei Bedarf, wenn eine Anfrage Authentifizierung benötigt. Der Client antwortet mit seiner eigenen `AUTH`-Nachricht, die ein signiertes ephemeres Event enthält, kind 22242, und das Relay antwortet mit einer `OK`-Nachricht, genau als wäre das Auth-Event ein gewöhnlicher Schreibvorgang. Die authentifizierte Sitzung gilt dann für die Dauer der Verbindung, und ein Client darf mehrere Pubkeys auf einer Verbindung mit einer Folge von `AUTH`-Nachrichten authentifizieren, von denen das Relay jede als authentifiziert behandelt.

Das signierte Auth-Event sieht so aus:

```json
{
  "id": "4ef6f2c0b1a84c9a3d0f9c58e2a1b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0",
  "pubkey": "c308e1f882c1f1dff2a43d4294239ddeec04e575f2d1aad1fa21ea7684e61fb5",
  "created_at": 1753195800,
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com/"],
    ["challenge", "challengestringhere"]
  ],
  "content": "",
  "sig": "8b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1"
}
```

Der `pubkey` ist die zu beweisende Identität, da das Relay die `sig` über der Event-`id` gegen ihn verifiziert. Der `kind` 22242 liegt im ephemeren Bereich: Das Event ist ein verbindungsebener Berechtigungsnachweis, und Relays dürfen es niemals speichern oder an andere Clients broadcasten. Das `relay`-Tag bindet die Signatur an eine Relay-URL, sodass ein erbeutetes Auth-Event nicht gegen ein anderes Relay wiedergegeben werden kann, und das `challenge`-Tag bindet es an den konkreten Challenge-String, den das Relay auf dieser Verbindung ausgegeben hat — was die Wiedergabe eines erbeuteten Auths auf einer späteren Verbindung blockiert. Der `created_at` muss nahe der aktuellen Zeit liegen, innerhalb von grob zehn Minuten, sodass ein abgestandenes Auth-Event von selbst abläuft. Das `content`-Feld ist leer; es wird nichts veröffentlicht.

Die Spec definiert außerdem zwei maschinenlesbare Präfixe, die Gating für Clients sichtbar machen. Ein Relay, das eine Subscription ablehnt, weil sich der Client noch nicht authentifiziert hat, antwortet mit einer `CLOSED`-Nachricht, die mit `auth-required:` beginnt, und ein abgelehnter Schreibvorgang erhält ein `OK` mit demselben Präfix. Ein Client, der authentifiziert ist, aber für die Aktion dennoch keine Berechtigung hat, erhält stattdessen `restricted:`. Genau auf dieser Unterscheidung baut [nostreams PR #702](https://github.com/Cameri/nostream/pull/702) auf: Lesevorgänge verschlüsselter Kinds können nun mit `auth-required:` geschlossen werden, bis der anfragende Pubkey beweist, dass er der Empfänger ist.

### NIP-43: Relay Access Metadata and Requests

[NIP-43](/de/topics/nip-43/) beantwortet die Folgefrage: Jetzt, wo das Relay weiß, wer du bist — was darfst du tun? Wo NIP-42 ein Handshake auf einer bestehenden Verbindung ist, ist NIP-43 ein Satz veröffentlichter Events, die den Mitgliedschaftsstatus beschreiben und Nutzern erlauben, dessen Änderung zu beantragen. Auf der Relay-Seite listet ein kind-13534-Event, signiert vom Pubkey im `self`-Feld des [NIP-11](/de/topics/nip-11/)-Dokuments des Relays, ein `member`-Tag pro Pubkey, mit optionalen Rollenargumenten, die auf als kind 33534 veröffentlichte Rollendefinitionen zeigen. Kind 8000 kündigt das Hinzufügen eines Mitglieds an und kind 8001 das Entfernen, beide signiert vom selben Relay-Schlüssel mit einem `p`-Tag für das betroffene Mitglied. Auf der Nutzerseite ist kind 28934 eine Beitrittsanfrage, die einen Einladungscode in einem `claim`-Tag trägt, kind 28935 ist ein ephemeres Invite-Code-Event, das das Relay on-the-fly erzeugt, wenn ein Nutzer einen Claim anfordert, und kind 28936 ist eine Austrittsanfrage.

Eine Beitrittsanfrage sieht so aus:

```json
{
  "id": "9f0e1d2c3b4a59687a6b5c4d3e2f1098a7b6c5d4e3f2019a8b7c6d5e4f3021a9b8",
  "pubkey": "ee1d336e13779e4d4c527b988429d96de16088f958cbf6c074676ac9cfd9c958",
  "created_at": 1753195900,
  "kind": 28934,
  "tags": [
    ["-"],
    ["claim", "invite-code-from-operator"]
  ],
  "content": "",
  "sig": "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2"
}
```

Der `pubkey` ist der Nutzer, der um Aufnahme bittet, und kind 28934 markiert das Event als Beitrittsanfrage. Das `-`-Tag ist der [NIP-70](/de/topics/nip-70/)-Protected-Event-Marker, der Relays anweist, dieses Event von niemandem außer seinem Autor anzunehmen. Das `claim`-Tag trägt den Einladungscode, den der Nutzer out-of-band erhalten hat, und `created_at` muss jetzt sein, plus/minus ein paar Minuten, sodass eine alte Anfrage nicht wiedergegeben werden kann. Das Relay beantwortet den Claim mit einer `OK`-Nachricht, wobei es das NIP-42-`restricted:`-Präfix für Fehler wie einen abgelaufenen oder ungültigen Code wiederverwendet, und sollte dann seine kind-13534-Liste aktualisieren und kann ein kind-8000-Add-Member-Event veröffentlichen. Mitgliedschaft wird bewusst nicht aus einem einzelnen Event abgeleitet: Die Spec sagt, die relay-signierte Liste sollte nicht als vollständig oder maßgeblich betrachtet werden, und ein Client, der entscheidet, ob jemand aktuell Mitglied ist, sollte sowohl das kind 13534 des Relays als auch die eigenen Events des Mitglieds konsultieren. Clients dürfen Join-, Invite- oder Leave-Requests nur an Relays senden, die diesen NIP im `supported_nips`-Abschnitt ihres NIP-11-Dokuments bewerben, und [nostreams PR #676](https://github.com/Cameri/nostream/pull/676) ist die relayseitige Maschinerie, die diese Request-Kinds in tatsächliche Mitgliedschaftsänderungen verwandelt.

### Geschichte

NIP-42 ist der ältere der beiden — mit deutlichem Abstand. Er ging am 2. Januar 2023 in [Commit c80be21c](https://github.com/nostr-protocol/nips/commit/c80be21c) in das NIPs-Repository ein, wo fiatjaf einen früheren von semisol entworfenen Relay-Auth-NIP drastisch vereinfachte und ein komplexeres Challenge-Schema auf das einzelne signierte ephemere Event reduzierte, das die Spec bis heute verwendet. NIP-43 kam viel später, am 30. Oktober 2025, als hodlbods [PR #1079](https://github.com/nostr-protocol/nips/pull/1079) gemergt wurde und Relay-Access-Metadaten und Requests direkt auf NIP-42s `restricted:`-Präfix aufsetzte. Die zweieinhalbjährige Lücke spiegelt, wie lange das Ökosystem bezahlte und private Relays auf Ad-hoc-Whitelists betrieb, bevor die Mitgliedschaftsschicht einen Standard bekam.

### Implementierungen

Auf der Relay-Seite liefert [nostream](https://github.com/Cameri/nostream) nach den Merges dieser Woche nun beide Hälften. [strfry](https://github.com/hoytech/strfry) implementiert NIP-42, validiert kind-22242-Auth-Events in seinem Ingester und gibt Challenges aus seiner Config heraus. [nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay) handhabt den AUTH-Handshake in seiner Connection-Schicht mit Tests für Challenge und Zeitstempelfenster. [khatru](https://github.com/fiatjaf/khatru), das Go-Relay-Framework, trackt den authentifizierten Pubkey pro Verbindung, sodass Policies Lesen und Schreiben darauf gaten können. Auf der Client-Seite signiert [Amethyst](https://github.com/vitorpamplona/amethyst) kind-22242-Antworten auf Relay-Challenges, einschließlich Per-Stream-Auth für seine verschlüsselten Concord-Communities. Die beiden NIPs teilen Access Control entlang einer sauberen Linie: NIP-42 ist Identitätsnachweis, begrenzt auf eine Verbindung, eine Challenge und ein paar Minuten Gültigkeit, und sagt nichts über Policy. NIP-43 ist Policy, ausgedrückt als gewöhnliche Relay-Events: wer Mitglied ist, wer hinzugefügt oder entfernt wurde, und wie ein Nutzer diese Übergänge beantragt. Die Lücke, die Implementierer im Blick behalten sollten, ist, dass bislang nichts feiner granulare Berechtigungen über NIP-43s optionale Rollen-Metadaten hinaus standardisiert — jedes Relay, das mehr tut als eine binäre Mitglied/Nicht-Mitglied-Teilung, entwirft diese Schicht also selbst.

---

Das war's für diese Woche. Baust du etwas oder hast News zu teilen? Melde dich per NIP-17-DM oder finde uns auf Nostr.
