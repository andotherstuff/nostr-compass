---
title: 'Nostr Compass #25'
date: 2026-06-03
publishDate: 2026-06-03
draft: false
type: newsletters
translationOf: /en/newsletters/2026-06-03-newsletter.md
translationDate: 2026-07-01
---

Amber 6.2.0 liefert NIP-44 v3 Verschlüsselung vor der Spezifikation aus. Mostro landet über acht PRs das Fundament für Cashu-abgewickelten Escrow und wrappt das bestehende Cashu Development Kit als zweites Settlement-Backend neben Lightning. NIP-F4 Podcasts wird nach 27 Monaten Debatte gemerged. fiatjaf öffnet einen umstrittenen NIP-17-Key-Decoupling-Vorschlag, der das Bunker-gegen-Marmot-Architekturargument wieder öffnet. Amethyst landet NIP-32 Hashtag-Labeling, einen dedizierten Podcast-Screen und Onchain-Zaps über 52 unveröffentlichte PRs.

## Top-Stories

### Amber 6.2.0: NIP-44 v3 Verschlüsselung ausgeliefert

[Amber v6.2.0](https://github.com/greenart7c3/Amber/releases/tag/v6.2.0), veröffentlicht am 1. Juni, fügt [NIP-44 v3 Verschlüsselungsunterstützung](https://github.com/greenart7c3/Amber/pull/448) mit einem dedizierten Zustimmungs-Screen, Intent-Vorschau, Bunker-Vorschau, History-Logging und Auto-Reject für ungültige Anfragen hinzu. Das Release registriert außerdem [NIP-44 v3 ContentProvider-Authorities](https://github.com/greenart7c3/Amber/commit/8b93340), sodass andere Android-Apps v3-Verschlüsselung neben dem bestehenden v2-Pfad anfordern können. NIP-44 selbst ist die versionierte Encrypted-Payload-Spezifikation, die von [NIP-17](/de/topics/nip-17/) privaten DMs, NIP-46 Bunker-Verkehr und anderen Nostr-Primitiven verwendet wird; v3 in Amber ist ein Opt-in neben v2, signalisiert durch eine separate Signer-Methode, sodass empfängerseitige Clients den Algorithmus explizit aushandeln können. Der entsprechende NIPs-PR ist noch nicht gelandet, sodass Amber v3 vor dem Protokoll-Konsens ausrollt, wobei das Wire-Format und die ContentProvider-Authority für die Downstream-Client-Integration registriert sind.

NIP-46-Sitzungen akzeptieren jetzt automatisch Ping-Anfragen beim Verbinden und entfernen den Prompt beim ersten Round-Trip nach dem Pairing. Die `sign_message`-Signer-Methode wurde vollständig entfernt, nachdem sie deprecated und ungenutzt war.

Da Amber der dominante Android-Signer ist, muss jeder Downstream-Client, der v3 möchte, Ambers Wire-Format anvisieren, bis der NIPs-PR landet. Das gibt Amber implizites Mitspracherecht bei der endgültigen v3-Spezifikation, bis das Protokoll aufholt. Der Trade ist real: v3 in Produktion lässt Amber Implementierungs-Feedback für das schließliche NIP sammeln, zum Preis eines temporären Single-Implementation-Referenzpunkts, an den sich andere Clients jetzt anpassen müssen.

### Mostro: Cashu-Escrow-Integration per CDK

grunch landete diese Woche acht PRs über MostroP2P, die Cashus bestehende P2PK-Multisig-Primitive (NUT-10 und NUT-11) als zweites Settlement-Backend neben Lightning auf dem Nostr-koordinierten P2P-Bitcoin-Exchange integrieren. Die kryptografischen Primitive sind Cashus; die Arbeit ist Integrations-Scaffolding und ein neuer Escrow-Backend-Trait. [Mostro core v0.12.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.12.0), veröffentlicht am 30. Mai, fügt die [Protokoll-Typen für 2-von-3-Multisig-Escrow](https://github.com/MostroP2P/mostro-core/pull/150), Per-Proof P_M-Signaturen hinzu und erlaubt Escrow-Events durch die Response-Validierung. Die Architektur ist in [PR #756](https://github.com/MostroP2P/mostro/pull/756) dokumentiert und verwendet Per-Order-Trade-Keys, geklärt in [PR #757](https://github.com/MostroP2P/mostro/pull/757).

Die Implementierung wurde über sechs Follow-up-PRs an einem einzigen Tag ausgerollt. [F2 (PR #758)](https://github.com/MostroP2P/mostro/pull/758) fügte die Konfiguration, den Escrow-Modus und den bedingten Boot hinzu. Die nächste Scheibe, [F3 (PR #760)](https://github.com/MostroP2P/mostro/pull/760), definierte einen `EscrowBackend`-Trait mit einer Lightning-Implementierung und einem Cashu-Stub, sodass Mostro Settlement-Backends wechseln kann, ohne die Order-State-Machine zu ändern. [F4 (PR #759)](https://github.com/MostroP2P/mostro/pull/759) wrappte [CDK](https://github.com/cashubtc/cdk) (das Cashu Development Kit) für Mint- und Wallet-Operationen. Datenbankarbeit in [F5 (PR #761)](https://github.com/MostroP2P/mostro/pull/761) fügte Compare-and-Swap-Escrow-Locks und Active-Locked-Queries hinzu. [F6 (PR #762)](https://github.com/MostroP2P/mostro/pull/762) baute ein containerisiertes Mint in einem dedizierten CI-Job für End-to-End-Escrow-Tests. Der Mostro-Flow verwendet bereits NIP-59 gift-wrapped DMs zur Order-Koordination über das Relay, sodass Cashu-Escrow als zweite Settlement-Option neben Lightning einrastet, ohne das Wire-Protokoll zu berühren.

## Releases

### ngit v2.5.0: GRASP-Fallback und lazy Git-Fetches

[ngit v2.5.0](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.5.0) ändert das Standardverhalten von `git push pr/<branch>` und `ngit send`, um bei neuen Vorschlägen ein PR-kind zu erzeugen, wenn im Repository mindestens ein GRASP-Server registriert ist. Zuvor wurde dies nur bei übergroßen Commits über 60 KB oder Commits mit Submodulen ausgelöst. Wenn ein PR nicht an die GRASP-Server des Repositorys gepusht werden kann, fällt ngit jetzt auf GRASP-06-Routing über die deklarierten Server zurück. Das `ngit send --git-server`-Flag oder `git push -o git-server=<url>` erlaubt es Beitragenden, eine benutzerdefinierte Git-URL oder einen GRASP-Server explizit anzuvisieren.

`ngit init` Republishes bewahren jetzt unbekannte Tags aus bestehenden Ankündigungen, sodass Tags, die von einer zukünftigen ngit-Version oder einem Drittanbieter-Tool hinzugefügt wurden, den Republish überleben. Eine gelbe Warnung listet die übertragenen Tags, und `--clean` entfernt sie auf Anfrage. `ngit pr apply`, `ngit pr checkout` und `ngit pr list` konsultieren Git-Server lazy und teilen sich einen einzigen Fetch-Helper, sodass Checkout nicht mehr bedingungslos fetcht, wenn der Commit bereits lokal ist. `ngit pr checkout` probiert auch vom Einreicher gelieferte Clone-URLs aus dem PR-Event als Fallback, wenn die deklarierten Git-Server des Repos die PR-Spitze nicht tragen, und passt so das bestehende Verhalten in `ngit pr apply` an. ngit ist die Referenz-[NIP-34](/de/topics/nip-34/)-Implementierung für Git-Zusammenarbeit über Nostr, und v2.5.0 macht GRASP zum First-Class-Pfad für neue Beitragende.

### Jumble v26.5.7: EXIF-Stripping und validierte Zap-Zählungen

[Jumble v26.5.7](https://github.com/CodyTseng/jumble/releases/tag/v26.5.7) fügt zwei Änderungen hinzu, die die Privatsphäre und Datenintegrität der Nutzer direkt betreffen. EXIF-Standort- und Kamera-Identifikatoren werden jetzt vor dem Verlassen des Clients aus Bild-Uploads entfernt, was eine langbestehende Metadata-Leak-Oberfläche schließt, die jedes von Jumble gepostete Bild betraf. Zap-Zählungen werden jetzt nur aus kryptografisch validierten Quittungen berechnet, was aufgeblähte Zählungen aus fehlgeformten Zap-Events behebt, die Angreifern erlaubten, Zap-Gesamtwerte an Notes zu übertreiben. Das Release fügt außerdem Sender-Identity-Verifikation für [NIP-17](/de/topics/nip-17/)-DMs hinzu, was eine Spoofing-Oberfläche schließt, in der ein Absender seinen `pubkey` im Seal fälschen konnte.

### nostr-calendar v1.6.0: RSVP und Duplikat-Teilnehmer-Handling

[nostr-calendar v1.6.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.6.0) landet Formstrs RSVP-Flow ([PR #169](https://github.com/formstr-hq/nostr-calendar/pull/169)) und verhindert Duplikat-Teilnehmer in Event-Einladungen ([PR #168](https://github.com/formstr-hq/nostr-calendar/pull/168)). Die `waitForAll`-Option in der Publish-Funktion ist jetzt standardmäßig false, sodass die UI nicht bei langsamen Relays blockiert ([PR #170](https://github.com/formstr-hq/nostr-calendar/pull/170)). [PR #157](https://github.com/formstr-hq/nostr-calendar/pull/157) lieferte Formstrs zwei NIP-Vorschlagsentwürfe für Terminplanung und Reservierungen.

### Sprout 0.3.6: Sprout × mesh-llm und Kanalabschnitte

[Sprout v0.3.6](https://github.com/block/sprout/releases/tag/v0.3.6) ist die Schlagzeile eines Sechs-Release-Laufs von v0.3.1 bis v0.3.6 diese Woche. In-Process Sprout × mesh-llm Integration landet in [PR #798](https://github.com/block/sprout/pull/798) und lässt Sprout mesh-llm-Nodes über Relay-Zulassung bereitstellen und konsumieren. Benutzerdefinierte Kanalabschnitte synchronisieren über Geräte hinweg über Nostr in [PR #792](https://github.com/block/sprout/pull/792), und Kanalabschnitte kommen mit Relay-Sync auf Mobile in [PR #800](https://github.com/block/sprout/pull/800). Thread-bewusste Benachrichtigungen mit veränderlichen Follow- und Mute-Kontrollen kommen in [PR #761](https://github.com/block/sprout/pull/761) an.

Anhänge beliebiger Dateitypen mit Download-Karten kamen in [PR #810](https://github.com/block/sprout/pull/810) an und erweiterten Sprout über reine Bild-Anhänge hinaus. Mobile gewann einen Pulse-Social-Feed-Tab ([PR #772](https://github.com/block/sprout/pull/772)) und Pulse-Politur über Feed-, Compose- und Filter-Oberflächen hinweg ([PR #796](https://github.com/block/sprout/pull/796)).

### NostrBotKit v0.5.0: Marmot-Gruppenchat in einem Rust-Bot-Framework

[NostrBotKit v0.5.0](https://codeberg.org/Tuxor/NostrBotKit/src/branch/main/CHANGELOG.md), veröffentlicht am 24. Mai auf Codeberg, fügt [Marmot](/de/topics/marmot/)-Unterstützung (MLS-über-Nostr, [NIP-104](https://github.com/nostr-protocol/nips/pull/2014)) zum selbstgehosteten Rust-Bot-Framework hinzu. Wenn `marmot: true` gesetzt ist, veröffentlicht der Bot seine MLS-Key-Packages (kind 443, 30443, 10051), akzeptiert Gruppeneinladungen automatisch und lauscht auf Nachrichten in beigetretenen Gruppen. Zwei neue Command-Typen, `dm_marmot` und `dm_marmot_npub`, lassen Bots Nachrichten in benannte Marmot-Gruppen oder 1:1 Marmot-Chats per Cron-Jobs oder Webhooks senden. Um Feedback-Loops mit anderen Bots zu verhindern, antworten NostrBotKit-Bots nur auf Nachrichten, die explizit an sie adressiert sind, per `/command` oder `@botname/command`. Verschlüsselte Anhänge, die MIP-04 verwenden, werden automatisch entschlüsselt und per Blossom oder NIP-96 neu hochgeladen, und die MLS-Zustandsdatenbank wird mit einem aus dem privaten Schlüssel des Bots abgeleiteten Schlüssel verschlüsselt. NostrBotKit ist das erste Rust-Framework, das NIP-104-Bot-Unterstützung ausliefert und Marmot-verschlüsseltes Bot-Deployment einem anderen Operator-Profil öffnet als dem bestehenden TypeScript-Pfad.

### noscrypt v0.1.14: signiertes Kryptografie-Bibliotheks-Release

[noscrypt v0.1.14](https://github.com/vnuge/noscrypt/releases/tag/v0.1.14) ist ein Security-Release der C-Kryptografie-Bibliothek, die von mehreren Nostr-Clients für secp256k1-, NIP-04- und NIP-44-Primitive verwendet wird. Das Release wird mit [PGP-signierten Downloads](https://www.vaughnnugent.com/resources/software/modules/noscrypt) ausgeliefert, die gegen den Public Key des Maintainers verifizierbar sind. Downstream-Clients, die noscrypt bundeln, sollten die Signatur vor der Integration validieren.

### Chama v1.3.0: neuer Nostr-nativer P2P-Escrow mit Fedimint

[Chama v1.3.0](https://github.com/jesuspirate/chama/releases/tag/v1.3.0), veröffentlicht am 1. Juni, ist die Schlagzeile eines Vier-Release-Laufs für einen neuen Nostr-nativen P2P-Escrow-Client, der Fedimint-Ecash und 2-von-3 Shamir-Secret-Sharing für Settlement verwendet. Das Projekt läuft unter [getchama.app](https://getchama.app) und funktioniert ohne Server. v1.3.0 führt "Heal that Sticks" ein (erfolgreiches Re-Broadcasten und Trade-Healing, das Session-Neustarts überlebt) und Pay-Rail-Matching, bei dem US-orientierte Chamas US-Zahlungsschienen zuerst anzeigen. Multi-Unit-Storefront-Grundlagen landeten über [v1.2.11](https://github.com/jesuspirate/chama/releases/tag/v1.2.11) (Multi-Unit-Schema) und [v1.2.12](https://github.com/jesuspirate/chama/releases/tag/v1.2.12) (Storefront-Stock-Accountant + native Fedimint-Bridge-Recovery-Härtung). Chama gesellt sich zu Mostro und Shopstr in der Nostr-Marketplace-Kategorie, unterschieden durch seine serverlose Architektur und Fedimint-basierte Escrow-Abwicklung.

## Unveröffentlichte Änderungen

### Amethyst: NIP-32 Hashtag-Labeling, Podcast-Screen, Musiktracks

Amethyst mergte diese Woche 52 PRs und 411 Commits, ohne einen Release-Tag zu schneiden. Die größte funktionale Ergänzung ist [PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111), der [NIP-32](/de/topics/nip-32/) Hashtag-Labeling und einen Label-basierten Hashtag-Feed mit kind 1985 Events mit `L`-Namespace- und `l`-Label-Tags implementiert. Dies ersetzt den brüchigen Text-Match-`#tag`-Mechanismus durch ein labeler-basiertes Discovery-Modell, in dem Nutzer bestimmten Labeler-npubs so folgen können, wie sie Content-Erstellern folgen. [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) fügt einen dedizierten Podcast-Screen mit Episodenliste und Inline-Player hinzu, und landet innerhalb von Tagen nach dem Merge der [NIP-F4](/de/topics/nip-f4/) Podcast-Spec. [PR #3071](https://github.com/vitorpamplona/amethyst/pull/3071) fügt einen Software-Apps-Feed mit Follow-List-Filterung hinzu, und [PR #3067](https://github.com/vitorpamplona/amethyst/pull/3067) fügt Unterstützung für Musiktracks und Playlists über [NIP-51](/de/topics/nip-51/) Sets hinzu.

Ephemere Signer für anonyme Post-Uploads landen in [PR #3123](https://github.com/vitorpamplona/amethyst/pull/3123) und lassen Nutzer anonym posten, ohne ihren Identity-Key an Upload-Services preiszugeben. Ein Tor-Self-Heal-Watchdog mit Integrationstests gegen Arti v2.3.0 kommt in [PR #3053](https://github.com/vitorpamplona/amethyst/pull/3053) an und stärkt Amethysts Tor-Routing bei vorübergehenden Netzwerkausfällen. Onchain-Zaps und ein NIP-05-Filter für zurückkehrende Nutzer aus Gemini landen in [PR #3052](https://github.com/vitorpamplona/amethyst/pull/3052) und erweitern die Zap-Oberfläche über Lightning hinaus auf Onchain-Bitcoin-Zahlungen.

### Shopstr: OpenGraph-Preview-URL-Validierung

[PR #504](https://github.com/shopstr-eng/shopstr/pull/504) validiert OpenGraph-Preview-URLs vor dem Rendern in Marketplace-Listings und schließt eine potenzielle XSS-Oberfläche, in der böswillige Verkäufer skriptbaren Content über gefertigte OG-Metadaten einbetten konnten. Shopstr-gehostete Shops zeigen OG-Vorschauen für externe Links, und unvalidierte URLs erlaubten einem Angreifer, beliebigen Inhalt in die Shop-UI zu injizieren.

## NIP-Updates und Protokoll-Spec-Arbeit

### NIP-F4 (Podcasts) nach zwei Jahren gemerged

[PR #1093](https://github.com/nostr-protocol/nips/pull/1093) wurde am 28. Mai gemerged, zwei Jahre und drei Monate nachdem fiatjaf den ursprünglichen Entwurf geöffnet hatte. NIP-F4 definiert Podcast-Episoden als kind 54 Events mit `imeta` Tags für Audio-Datei-Metadaten (URL, MIME-Typ, ISO-Sprachcode, Fallback-URLs, NIP-96 Service-Flag, Bitrate, Dauer), einem `title` Tag, optionalen `image` und `description` Tags sowie `t` Tags für Topic-Labels. Die Spec behält bewusst RSS als Source of Truth: Episoden können ein `i` Tag tragen, das auf die RSS-Podcast-GUID verweist, wodurch Nostr-Clients zu bestehenden Podcast-Feeds verlinken können, ohne Audio-Hosting zu duplizieren. Die lange Debatte im PR-Thread (mit dem Podcast-Namespace-Co-Autor Dave Jones, Alex Gleason und Mike Terenzio) einigte sich auf ein Koexistenz-Modell, in dem Nostr die soziale Schicht auf RSS bereitstellt, während RSS die Verteilungsschicht behält. Amethysts [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) Podcast-Screen landet innerhalb von Tagen nach dem Spec-Merge, und Jumbles GIF-Picker-Arbeit enthält auch frühes Podcast-Attachment-Scaffolding.

### NIP-17-Key-Decoupling (PR #2361)

fiatjaf öffnete [PR #2361](https://github.com/nostr-protocol/nips/pull/2361) am 1. Juni und schlug vor, dass NIP-17 den Identity-Key vom Encryption-Key trennt. Empfänger kündigen ihren Encryption-Key in einem neuen kind 10044 Event an, und Sender verwenden diesen angekündigten Key (falls vorhanden) für das Gift-Wrap-Inner-Seal und fallen nur dann auf den Identity-Key des Empfängers zurück, wenn die Ankündigung fehlt. Der PR fügt außerdem ein `n` Tag zum Seal hinzu, das den Encryption-pubkey des Senders trägt, sodass Empfänger den korrekten Konversationsschlüssel ableiten können, ohne Trial-Decryption gegen jeden ausrangierten Key durchführen zu müssen. Die erklärte Motivation ist Bunker-UX: unter dem aktuellen Design muss ein Bunker-Nutzer jede empfangene DM zum Entschlüsseln über den Signer roundtrippen, da der Encryption-Key der Signer-gehaltene Identity-Key ist. Die Entkopplung lässt den Client den Encryption-Key lokal halten, während der Identity-Key im Bunker für Signaturen bleibt.

Der Vorschlag zog das umstrittenste Review der Woche an. Cody Tseng (Jumble) unterstützt ihn als den einfachsten Weg zu Cross-Client-DM-Interop. Vitor Pamplona (Amethyst) hat zwei Einwände: Er fügt ein neues langlebiges Entschlüsselungs-Geheimnis außerhalb des Bunkers hinzu, und Clients, die es nicht ausliefern, werden Nachrichten von Clients, die es tun, stillschweigend nicht mehr entschlüsseln, ohne Degradations-Pfad, weil der Bruch auf der Seal-Ebene liegt. Pamplona argumentiert, dass das Problem bereits korrekt durch [Marmots](/de/topics/marmot/) Key-Packages und Epoch-Rotation gelöst ist, und dass das nachträgliche Einbauen der Key-Trennung in die Basis-NIP-17-Spec die Art von Interop-Fehler erzeugt, um die Marmot zwei Jahre lang engineeren musste. fiatjafs Gegenrede hat drei Teile: Entkopplung ist optional pro Empfänger, der n-Tag-Fix adressiert die Trial-Decryption-Sorge, und die Alternative ist, Bunker-UX kaputt zu halten, während Telegram den Messaging-Use-Case frisst. Der Thread bleibt ohne Merge-Entscheidung offen und ist die meistbeobachtete NIP-Diskussion des Quartals.

### NIP-Silent-Payments Payment-Flow (PR #2362)

[silentius-satoshi öffnete PR #2362](https://github.com/nostr-protocol/nips/pull/2362) am 1. Juni als Begleiter zum breiteren [Nostr Silent Payments NIP-Entwurf (PR #2355)](https://github.com/nostr-protocol/nips/pull/2355). Das Payment-Flow-NIP definiert kind 8352 für Silent-Payment-Empfangsbenachrichtigungen (ausgeliefert per [NIP-59](/de/topics/nip-59/) Gift Wrap, damit der Empfangslink nicht öffentlich beobachtbar ist) und kind 10353 für einen verschlüsselten UTXO-Cache, der über Geräte für dieselbe Silent-Payments-Wallet synchronisiert. Das Paar zusammen lässt einen Zahler eine Zahlung an eine Silent-Payments-Adresse mit Nostr-nativen Primitiven signalisieren, ohne den On-Chain-Link auf der offenen Relay-Ebene preiszugeben.

### NIP-PIP Perfect IP Packets (PR #2364)

[RandyMcMillan öffnete PR #2364](https://github.com/nostr-protocol/nips/pull/2364) am 1. Juni als Entwurf. Er führt einen Paket-Baum-Transport mit drei neuen adressierbaren kinds ein: 39078 trägt das Manifest, 39079 trägt einzelne Slices, und 39080 trägt Reparatur-Anfragen. Die Spec definiert ein Wire-Format, in dem große Dateien in adressierbare Slices zerlegt werden, mit Manifesten, die den Slice-Baum beschreiben, und Reparatur-Anfragen, die Empfängern erlauben, fehlende Slices anzufordern. Frühentwurfsstatus gilt, und der Vorschlag hat noch keine Maintainer-Review angezogen.

### NIP-29 Audio/Video Live Spaces (PR #2238)

[PR #2238](https://github.com/nostr-protocol/nips/pull/2238) wurde am 28. Mai gemerged und erweitert [NIP-29](/de/topics/nip-29/) relay-basierte Gruppen um Audio- und Video-Live-Space-Unterstützung. Gruppen können jetzt auf eine aktive Live-Space-Session verweisen, wodurch [NIP-53](/de/topics/nip-53/)-artige Live-Activity-Events in einem NIP-29-Gruppenkontext verankert werden können.

### NIP-71 Video Multiple Audio Tracks (PR #2255)

[PR #2255](https://github.com/nostr-protocol/nips/pull/2255) wurde am 28. Mai gemerged und fügt Audio-Track-`imeta` Tags zu NIP-71 Video-Events hinzu. Das neue Format trägt URL, Hash, MIME-Typ, Sprach-Tag (mit ISO-639-1 plus Original-Version-Flag), Fallback-URLs, NIP-96 Service-Signal, Bitrate und Dauer. Das ermöglicht Audio-only Streaming (Video-Podcasts), Auflösungswechsel mit stabilem Audio, mehrere Sprachtracks und reduzierten Speicher, wenn Server Audio nicht direkt in Video-Dateien einbetten. Clients sollten die Audio-Track-Verfügbarkeit prüfen, bevor sie Single-Track-Verhalten annehmen.

### NIP-59 Ephemeral Gift Wrap (PR #2245)

[PR #2245](https://github.com/nostr-protocol/nips/pull/2245) wurde am 28. Mai gemerged und fügt kind 21059 als ephemeres Gegenstück zum bestehenden kind 1059 Gift Wrap hinzu. Die Semantik entspricht dem Standard-NIP-59-Wrap, folgt aber ephemeren Event-Regeln gemäß NIP-01 (Relays lassen sie nach dem Broadcast fallen und persistieren sie nicht). Damit können Apps Persistenz basierend auf Anforderungen wählen: Tipp-Indikatoren und Presence-Pings profitieren von Ephemeral, während DM-Historie Persistenz braucht.

### NIP-78 Application-Specific Kind (PR #2292)

[PR #2292](https://github.com/nostr-protocol/nips/pull/2292) wurde am 28. Mai gemerged und klassifiziert NIP-78 anwendungsspezifische Daten neu als normales adressierbares kind, wobei der vorherige separate Bereich aufgegeben wird. Dies vereinfacht die Replaceability-Semantik und richtet NIP-78 mit dem adressierbaren Event-Modell aus, das von anderen Anwendungszustand-NIPs verwendet wird.

### NIP-85-Klärungen (PR #2304)

[PR #2304](https://github.com/nostr-protocol/nips/pull/2304) wurde am 28. Mai gemerged, mit kleinen Verbesserungen der Sprache rund um mehrere Keys und Relays pro Service-Provider in [NIP-85](/de/topics/nip-85/) Trusted Assertions, und klärt den Operator-Key-Rotation-Pfad für Relay-Assertion-Services.

### NIP-01 Relay-Connection-Management-Einzeiler (PR #2307)

[PR #2307](https://github.com/nostr-protocol/nips/pull/2307) wurde am 28. Mai gemerged und fügt einen einzigen Satz zu NIP-01 darüber hinzu, wie Clients Relay-Verbindungs-Lebensdauern handhaben sollen. Der Fix adressiert eine langlaufende Lücke, in der Clients uneinig waren, ob WebSocket-Verbindungen nach dem Fetchen offen bleiben sollten, was zu stillem Nachrichtenverlust auf Relays führte, die Idle-Verbindungen fallen lassen.

### NIP-C7 Kind 9 Chat-Beschränkung (PR #2310)

[PR #2310](https://github.com/nostr-protocol/nips/pull/2310) wurde am 28. Mai gemerged und beschränkt NIP-C7-Chat-Ansichten auf ausschließlich kind 9 Nachrichten. Das trennt ephemeren Chat von kind 1 Timeline-Posts in Clients, die NIP-C7-artige Chat-Oberflächen implementieren.

### NIP-55-Vereinfachung (PR #2363)

[PR #2363](https://github.com/nostr-protocol/nips/pull/2363) von greenart7c3, geöffnet am 1. Juni, vereinfacht die Android-Signer-Anwendungsspec. Vitor Pamplona gab "Looks good" als Zustimmung, und fiatjaf fragte, ob er bereit zum Mergen ist. Die Änderung ebnet den Weg für die NIP-44 v3 ContentProvider-Authority-Registrierung, die Amber diese Woche ausgeliefert hat.

### NIP-44 v3 (Amber-Implementierung vor der Spec)

Amber lieferte NIP-44 v3 in v6.2.0 mit acht Commits aus, die das Verschlüsselungs-Upgrade und die ContentProvider-Authority-Registrierung implementieren, aber der NIPs-Repo-Spec-PR ist noch nicht gelandet. NIP-44 selbst definiert ein versioniertes Encrypted-Payload-Format, das innerhalb signierter Events verwendet wird; das bestehende v2 (seit 2024 in Produktion) verwendet secp256k1 ECDH, HKDF, Padding, ChaCha20, HMAC-SHA256 und base64. Das v3-Wire-Format fügt ein neues Versions-Byte (0x03) vor der Nonce hinzu, wodurch Empfänger-Clients den Algorithmus explizit aushandeln können. Ambers Implementierung enthält Auto-Reject für ungültige v3-Anfragen, einen dedizierten Zustimmungs-Screen, der sich von v2-Zustimmungen unterscheidet, und Per-Direction-Klartext-Logging für die History. Bis der NIPs-PR merged, steht v3 als Amber-spezifische Erweiterung. Behandle es als vorwärtsblickendes Signal, nicht als stabile protokollweite Signalisierung.

## NIP Deep Dive: NIP-32 (Labeling)

[NIP-32](/de/topics/nip-32/) definiert eine strukturierte Möglichkeit für jeden Nostr-Akteur, Events, pubkeys, Relays, URLs oder Topics mit adressierbaren kind 1985 Events unter Verwendung eines namespaced Label-Vokabulars zu labeln. Die Spec führt zwei neue Tags ein: `L` bezeichnet einen Label-Namespace, und `l` bezeichnet ein Label innerhalb dieses Namespaces. Label-Ziel-Tags (`e`, `p`, `a`, `r` oder `t`) spezifizieren, was gelabelt wird. Die Namespace-Anforderung verhindert, dass mehrere Label-Systeme kollidieren: ein `spam`-Label in `nip28.moderation` trägt eine andere Semantik als ein `spam`-Label in `relay-report`.

Die Designentscheidung, die NIP-32 über Moderation hinaus nützlich macht, ist, dass Labels Behauptungen sind, keine Protokoll-Level-Wahrheit. Ein kind 1985 Event sagt nur, dass ein bestimmter pubkey ein bestimmtes Ziel in einem bestimmten Namespace gelabelt hat. Das Vertrauensmodell wird an den Client delegiert: jeder Client wählt, welchen Labelern er glaubt, welche Namespaces er liest und welche UI-Affordance er jedem Label gibt. Dasselbe Primitiv trägt Content-Warnungen, Lizenzzuweisung, ISO-639-1-Sprach-Tags auf kind 1 Notes, ISO-3166-2-geografische Tags, Content-Klassifizierung, verteilte Moderations-Vorschläge und Reputations-Scores.

Amethysts [PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111) diese Woche ist das bislang größte Deployment. Er fügt Hashtag-Labeling über NIP-32 und einen Label-basierten Hashtag-Feed hinzu, wodurch Nutzer nach Labels, die von vertrauenswürdigen Labelern zugewiesen wurden, browsen können. Der frühere `#tag` Text-Match-Mechanismus, der Hashtag-Discovery auf Nostr ursprünglich antrieb, bleibt als Fallback für ungelabelte Notes. Das Hashtag-als-Label-Modell bedeutet, dass dieselbe Note unter mehreren Labels, die von verschiedenen Labelern zugewiesen wurden, entdeckbar sein kann, und Nutzer können bestimmte Labeler muten oder boosten, ohne die zugrunde liegenden Notes zu beeinflussen.

Self-Labeling wird ebenfalls unterstützt. Ein Autor kann `L` und `l` Tags direkt an seine eigenen kind 1 Notes anhängen, um Sprache, Standort und Thema zu deklarieren. Eine Note, die mit `["L", "ISO-639-1"], ["l", "en", "ISO-639-1"]` getaggt ist, identifiziert sich selbst als Englisch und kann von sprach-bewussten Clients ohne Drittanbieter-Labeling-Infrastruktur gefiltert werden.

Beispiel eines NIP-32 Label-Events, das eine kind 1 Note als Englisch taggt und ihr einen Moderations-Tag zuweist:

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748908800,
  "kind": 1985,
  "tags": [
    ["L", "ISO-639-1"],
    ["l", "en", "ISO-639-1"],
    ["L", "nip28.moderation"],
    ["l", "approve", "nip28.moderation"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3", "wss://relay.example.com"]
  ],
  "content": "Labeled as English-language content approved for NIP-28 chat moderation",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

Der Amethyst-Rollout kombiniert mit der jüngsten Trusted-Relay-Assertions-Arbeit legt nahe, dass NIP-32 zum Standard-Substrat für jedes "user-driven assertion about a target"-Muster auf Nostr wird. Der nächste Test ist, ob die Labeler selbst Vertrauens-Hierarchien entwickeln: ob Nutzer bestimmten Labeler-npubs so folgen werden, wie sie Content-Erstellern folgen.

## NIP Deep Dive: NIP-F4 (Podcasts)

[NIP-F4](https://github.com/nostr-protocol/nips/blob/master/F4.md) wurde diese Woche gemerged, zwei Jahre und drei Monate nachdem fiatjaf den ursprünglichen Entwurf geöffnet hatte (PR #1093). Das F-Präfix ist einfache Hex-Nummerierung: NIP-F0 bis NIP-FF nutzen denselben 1-Byte-Hex-Raum wie NIP-0A bis NIP-0D, wobei der obere Hex-Bereich als Überlauf dient, jetzt wo sich der Dezimalbereich 01–99 füllt. NIP-F4 definiert, wie Podcasts Episoden und Metadaten als Nostr-Events veröffentlichen, während RSS als ergänzende Schicht für die Audio-Datei selbst erhalten bleibt.

Die zentrale architektonische Entscheidung ist, dass jeder Podcast sein eigenes Nostr-Keypair ist. Die Spec eröffnet mit dieser Aussage direkt: "each podcast is its own Nostr keypair". Das lässt Podcasts ihre Podcasting-Präsenz mit einer normalen kind 0 / kind 1 Microblogging-Präsenz kombinieren und lässt einen Podcast den Besitz über die Zeit hinweg über Key-Übergabe oder MuSig2-artiges geteiltes Signieren wechseln. Vier Event-kinds tragen die Publishing-Schicht:

- **`kind:10154`**: replaceable Podcast-Metadaten. Trägt `title`, `image`, `description`, optionale `website` Tags und optionale `p` Tags, die Autoren mit einer `role` von `host`, `cohost` oder `editor` markieren.
- **`kind:10164`**: Autoren-Gegenbehauptung. Das Beispiel in der Spec verwendet kind `10064` (ein Typo, der zur Korrektur offen ist), aber die Überschrift und der umliegende Text identifizieren es als `kind:10164`. Nutzer listen die Podcast-pubkeys, die sie authoren, sodass Clients die `p` Tags in `kind:10154` gegen eine äquivalente Behauptung des vermeintlichen Autors verifizieren können. Ohne dies könnte ein Podcast fälschlicherweise jeden als Host taggen.
- **`kind:54`**: Episoden-Events, die direkt vom Podcast-pubkey authored werden. Tags umfassen `title`, optionales `image`, `description` und eine oder mehrere `audio` Tags. Jedes `audio` Tag ist `["audio", "<audio-url>", "<optional_media_type>"]`. Die Spec notiert "other important fields to be specified here later after further discovery", und die gemergte Form ist bewusst minimal.
- **`kind:10054`**: eine [NIP-51](/de/topics/nip-51/)-artige Favorite-Podcasts-Liste, mit der Nutzer markieren können, welchen Podcasts sie folgen.

Die Thread-Debatte rund um den Merge beinhaltete den Podcasting-2.0-Co-Autor [Dave Jones](https://github.com/daveajones), [Alex Gleason](https://github.com/alexgleason), [Mike Terenzio](https://github.com/mterenzio), [Pablo F7z](https://github.com/pablof7z) und [staab](https://github.com/staab). Jones argumentierte stark gegen jeden Versuch, RSS zu ersetzen: "It's been tried many times and always fails", und zitierte JSONfeed, XMPP, AMP, Twitters API und Spotifys gescheiterte Migration. Terenzio formulierte den Vorschlag als soziale Schicht auf RSS um, wobei RSS selbst die Verteilungsschicht bleibt. fiatjaf stimmte zu, zurückzutreten und den Vorschlag reifen zu lassen: "I agree with everything you said but I still think we can pull it off, let's stop here for a while". Zwei Jahre später landet die gemergte Spec näher an Koexistenz als an Ersatz.

Drei Designfragen bleiben in der gemergten Spec explizit:

- Der `kind:10164`-Typo (Beispiel zeigt `10064`) muss abgeglichen werden, bevor Clients sicher interoperieren können.
- Episoden-Level-Discovery ohne RSS-GUID-Linking bleibt offen. Die gemergte Spec hat kein `i` Tag, kein `podcast:item:guid`-Format und keinen RSS-Bridging-Mechanismus. Clients, die einen bestehenden RSS-Katalog in kind 54 Events überbrücken wollen, müssen die Bridge-Konvention selbst definieren.
- Der "other important fields"-Stub auf der `kind:54`-Definition lässt Bitrate, Dauer, Sprache, Transkript-Pointer, Kapitel und Per-Segment-Metadaten als offenes Territorium für Follow-up-Vorschläge.

Amethysts [PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105) landet einen dedizierten Podcast-Screen mit Episodenliste und Inline-Player innerhalb von Tagen nach dem Merge, die erste große Client-Implementierung. Jumble lieferte frühes Podcast-Attachment-Scaffolding neben seinem GIF-Picker aus. Wavlake bleibt die größte Nostr-native Podcast-Plattform und muss entscheiden, ob es seine bestehenden kind 31337 Musiktrack-Events mit NIP-F4s kind 54 Episoden-Modell in Einklang bringt.

Beispiel eines NIP-F4 kind 54 Episoden-Events, passend zum minimalen Tag-Set der gemergten Spec:

```json
{
  "id": "55807e7d5cd90d0303d7dce7397f996fdbaed8697903f326c7cf8ad999b9de3d",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748995200,
  "kind": 54,
  "tags": [
    ["title", "Episode 42: Why RSS Won"],
    ["image", "https://podcast.example.com/ep42-cover.jpg"],
    ["description", "Dave Jones and fiatjaf on protocol coexistence and the social layer."],
    ["audio", "https://podcast.example.com/audio/ep42.mp3", "audio/mpeg"]
  ],
  "content": "In this episode we discuss the two-year journey of NIP-F4 from draft to merge, and why coexistence with RSS turned out to be the right architectural choice.",
  "sig": "abc123def456789012345678901234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef01234567"
}
```

PR #1093 war 27 Monate offen, weit über der Median-Offenzeit für gemergte NIPs-PRs. Der nächste Test für NIP-F4 ist, ob der kind 10164-Typo abgeglichen wird, ob Episoden-Discovery- und RSS-Bridge-Konventionen von den Implementierern entstehen und ob die großen Podcast-Hosts unter Per-Podcast-Keypairs veröffentlichen, wie die Spec empfiehlt.
