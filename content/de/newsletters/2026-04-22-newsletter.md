---
title: 'Nostr Compass #19'
date: 2026-04-22
translationOf: /en/newsletters/2026-04-22-newsletter.md
translationDate: 2026-04-22
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, deinem wöchentlichen Wegweiser durch Nostr.

**Diese Woche:** [Amethyst](https://github.com/vitorpamplona/amethyst) liefert einen großen Schwung an Marmot-, Community- und MoQ-Audio-Rooms-Arbeit aus, [TollGate](https://github.com/OpenTollGate/tollgate) stabilisiert Pay-per-use-Internetzugang über Nostr und Cashu in v0.1.0, und [nostream](https://github.com/Cameri/nostream) schließt eine Woche Relay-Arbeit rund um [NIP-45](/de/topics/nip-45/), [NIP-62](/de/topics/nip-62/), Kompression, Query-Härtung und vollständige [NIP-11](/de/topics/nip-11/)-Parität ab. Forgesworn startet einen kompletten Signing-, Identity- und Paid-API-Stack für Nostr. ShockWallet treibt Nostr-native Lightning-Wallet-Flows weiter voran. Die Formstr-Suite bringt Security-Härtung in Pollerama, i18n in Forms und RRULE-Support in Nostr Calendar. StableKraft, Keep, topaz, WoT Relay, Flotilla und NipLock runden die Releases ab. Die Deep Dives behandeln [NIP-72](/de/topics/nip-72/) und [NIP-57](/de/topics/nip-57/).

## Top Stories

### Amethyst liefert Marmot-MIP-Compliance, NIP-72-Communities, Zap Goals und MoQ-Audio-Räume

[Amethyst](https://github.com/vitorpamplona/amethyst) mergte diese Woche 57 PRs. Die Hauptthemen sind [Marmot](/de/topics/marmot/)-Compliance, erstklassige [NIP-72](/de/topics/nip-72/)-Communities, Zap Goals auf Livestreams und ein neuer Audio-Rooms-Stack auf Basis von Media over QUIC. [PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) richtet die eingebettete [MDK](https://github.com/marmot-protocol/mdk)-Implementierung an den Wire-Formaten von MIP-01 und MIP-05 aus. [PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) ergänzt MIP-00 KeyPackage Relay Lists, und [PR #2436](https://github.com/vitorpamplona/amethyst/pull/2436) schließt Admin-Gate- und Media-Lücken aus Cross-Client-Tests mit [White Noise](https://github.com/marmot-protocol/whitenoise).

Am selben Tag landen Korrekturen für MLS-Commit-Framing und Outer-Layer-Decryption in [PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466) und [PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471). Weitere Compliance-Arbeit in [PR #2477](https://github.com/vitorpamplona/amethyst/pull/2477) und [PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493) schließt zusätzliche Commit- und Message-Encryption-Lücken und fügt einen Validator für MLS-Commit-Kryptographie hinzu. Parallel dazu liefert [PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) `amy`, eine CLI für Marmot- und MLS-Gruppenoperationen.

[PR #2468](https://github.com/vitorpamplona/amethyst/pull/2468) bringt erstklassige Erstellung und Verwaltung von [NIP-72](/de/topics/nip-72/)-Communities. Nutzer können die kind-`34550`-Community-Definition veröffentlichen, Moderatoren und Relay-Hints hinzufügen, Beiträge mit `a`-Tag einreichen und ausstehende Freigaben über kind `4549` verwalten. [PR #2469](https://github.com/vitorpamplona/amethyst/pull/2469) integriert [NIP-75](/de/topics/nip-75/) Zap Goals in den [NIP-53](/de/topics/nip-53/)-Live-Activities-Screen. Jeder Stream erhält jetzt einen Fundraising-Header mit Fortschrittsbalken, One-Tap-Zap-Button und Top-Zappers-Leaderboard.

Der ambitionierteste neue Bereich ist Echtzeit-Audio. [PR #2494](https://github.com/vitorpamplona/amethyst/pull/2494) fügt einen Media-over-QUIC-Transport-Client und Audio-Rooms-Support hinzu. Zusammen mit dem neuen Public-Chats-Screen aus [PR #2487](https://github.com/vitorpamplona/amethyst/pull/2487) hat Amethyst nun eine End-to-End-Oberfläche für öffentliche Audio-Räume neben seinem Marmot-Messaging.

### TollGate v0.1.0 stabilisiert Pay-per-use-Internet über Nostr und Cashu

[TollGate](https://github.com/OpenTollGate/tollgate) veröffentlichte am 21. April [v0.1.0](https://github.com/OpenTollGate/tollgate/releases/tag/v0.1.0), den ersten getaggten Snapshot seines Spezifikationsstapels für Pay-per-use-Netzwerkzugang. Das Protokoll erlaubt Geräten wie WiFi-Routern, Ethernet-Switches oder Bluetooth-Tethers, Preise zu bewerben, [Cashu](/de/topics/cashu/)-ecash-Tokens zu akzeptieren und Sessions über vorausbezahlte lokale Tokens zu verwalten. Ein Kunde mit einigen sats in einer lokalen Cashu-Wallet kann so die nächsten Minuten oder Megabytes Konnektivität kaufen.

Der Release fixiert drei Schichten der Architektur. [TIP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-01.md) definiert die Basis-Eventformen, [TIP-02](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/TIP-02.md) legt Cashu-Zahlungen darüber, [HTTP-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/HTTP-01.md) bis HTTP-03 definieren eine plain-HTTP-Oberfläche, [NOSTR-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/NOSTR-01.md) die Nostr-Relay-Variante, und [WIFI-01](https://github.com/OpenTollGate/tollgate/blob/v0.1.0/WIFI-01.md) die Captive-Portal-Routing-Schicht. Die neue [TollGate-Topic-Page](/de/topics/tollgate/) deckt den gesamten Stack ab.

### nostream mergt 53 PRs für NIP-45, NIP-62, Kompression und Query-Härtung

[nostream](https://github.com/Cameri/nostream), die TypeScript-Relay-Implementierung von Cameri, mergte 53 PRs in einer Woche. [PR #522](https://github.com/Cameri/nostream/pull/522) fügt [NIP-45](/de/topics/nip-45/) `COUNT`-Support hinzu, [PR #544](https://github.com/Cameri/nostream/pull/544) ergänzt [NIP-62](/de/topics/nip-62/) Right-to-Vanish in der beworbenen Feature-Liste, [PR #548](https://github.com/Cameri/nostream/pull/548) erweitert das Filter-Schema um Großbuchstaben-Tag-Filter, und [PR #514](https://github.com/Cameri/nostream/pull/514) bringt gzip- und xz-Kompression für Event-Import und -Export.

[PR #534](https://github.com/Cameri/nostream/pull/534) führt ein Benchmarking-Harness und Optimierungen in der Filter-zu-SQL-Übersetzung ein. [PR #524](https://github.com/Cameri/nostream/pull/524) behebt einen Fehler beim Matching von Pubkeys in White- und Blacklists, [PR #553](https://github.com/Cameri/nostream/pull/553) fügt einen deterministischen Tie-Breaker zu `upsertMany` hinzu, und [PR #493](https://github.com/Cameri/nostream/pull/493) beschränkt das Vertrauen in `X-Forwarded-For` auf konfigurierte Trusted Proxies. [PR #557](https://github.com/Cameri/nostream/pull/557) bringt vollständige [NIP-11](/de/topics/nip-11/)-Parität.

## Shipping This Week

### Primal Android liefert Explore-Tab, NIP-05-Verifikation und Audio-Player

[Primal Android](https://github.com/PrimalHQ/primal-android-app) pushte 11 gemergte PRs auf den Feed-Redesigns der Vorwoche aufbauend. [PR #1021](https://github.com/PrimalHQ/primal-android-app/pull/1021) bringt einen neuen Explore-Tab, [PR #1015](https://github.com/PrimalHQ/primal-android-app/pull/1015) einen Feed-Editor mit Primal-DSL, [PR #994](https://github.com/PrimalHQ/primal-android-app/pull/994) [NIP-05](https://github.com/nostr-protocol/nips/blob/master/05.md)-Verifikation für Profile und [PR #997](https://github.com/PrimalHQ/primal-android-app/pull/997) einen In-Feed-Audio-Player. [PR #1018](https://github.com/PrimalHQ/primal-android-app/pull/1018) ergänzt [NIP-46](/de/topics/nip-46/) nostr-connect-Pairing über den Wallet-QR-Scanner.

### strfry fügt Prometheus-Write-Path-Metriken hinzu und behebt NIP-42-AUTH-Envelope

[strfry](https://github.com/hoytech/strfry) veröffentlichte mehrere operator-orientierte Verbesserungen. [PR #194](https://github.com/hoytech/strfry/pull/194) fügt einen dedizierten Prometheus-Exporter für den Write Path hinzu, [PR #197](https://github.com/hoytech/strfry/pull/197) loggt Bytes up und down sowie Kompressionsraten, und [PR #192](https://github.com/hoytech/strfry/pull/192) macht das Filter-Tag-Limit zur Laufzeit konfigurierbar. [PR #201](https://github.com/hoytech/strfry/pull/201) korrigiert die [NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md)-AUTH-Failures vom `NOTICE`-Format auf das im NIP spezifizierte `OK`-Envelope.

### Shopstr härtet Storefront-Sicherheit über 13 PRs

[Shopstr](https://github.com/shopstr-eng/shopstr) mergte 13 PRs, dominiert von Security-Fixes. Dazu gehören die Schließung einer Stored-JavaScript-Lücke in Storefront-Links, Escaping für HTML-Rendering, Absicherung von API-Endpunkten hinter Auth und Fixes für SSRF-Funde. Funktional wurden ein Replay-sicherer Failed-Relay-Publish-Queue, ein Fix für Wallet-Events-Fetches und Revalidierung gespeicherter Cart-Discounts ergänzt.

### Nostria v3.1.22 bis v3.1.28 fügen Hintergrund-Musikwiedergabe auf Android hinzu

[Nostria](https://github.com/nostria-app/nostria) veröffentlichte sechs Releases von [v3.1.22](https://github.com/nostria-app/nostria/releases/tag/v3.1.22) bis [v3.1.28](https://github.com/nostria-app/nostria/releases/tag/v3.1.28). Die zentrale Änderung in [v3.1.26](https://github.com/nostria-app/nostria/releases/tag/v3.1.26) ist Hintergrund-Musikwiedergabe auf Android mit Steuerung in Benachrichtigungsleiste und Lockscreen. Die nachfolgenden Releases härten diesen neuen Media-Service-Pfad.

### Wisp v0.18.0-beta fügt Normie Mode, For You Feed und NIP-29-Gruppenkonfiguration hinzu

[Wisp](https://github.com/barrydeen/wisp) veröffentlichte [v0.18.0-beta](https://github.com/barrydeen/wisp/releases/tag/v0.18.0-beta) am 16. April. [PR #462](https://github.com/barrydeen/wisp/pull/462) ergänzt einen Normie Mode mit Fiat-Beträgen, [PR #464](https://github.com/barrydeen/wisp/pull/464) überarbeitet das Onboarding, und [PR #469](https://github.com/barrydeen/wisp/pull/469) fügt einen For You Feed hinzu. Auf der Protokollseite ergänzt [PR #471](https://github.com/barrydeen/wisp/pull/471) [NIP-29](/de/topics/nip-29/)-Gruppenkonfiguration für Flags, Invites, Rollen und AUTH-Prompts.

### NoorNote v0.8.4 fügt geplante Beiträge und Livestream-Zaps hinzu

[NoorNote](https://github.com/77elements/noornote) veröffentlichte [v0.8.4](https://github.com/77elements/noornote/releases/tag/v0.8.4) und [v0.8.5](https://github.com/77elements/noornote/releases/tag/v0.8.5). v0.8.4 bringt ein Scheduled-Posts-Add-on, bei dem die App ein vollständig signiertes Event an ein NoorNote-Relay übergibt, das es zum geplanten Zeitpunkt veröffentlicht. Derselbe Release ergänzt One-Tap-Zapping aus Livestream-Karten, wobei die sats im Chat-Overlay des Streams über [NIP-53](/de/topics/nip-53/) erscheinen.

### topaz v0.0.2 liefert ein Nostr-Relay für Android aus

[topaz](https://github.com/fiatjaf/topaz), ein neues Nostr-Relay für Android-Telefone von fiatjaf, veröffentlichte [v0.0.2](https://github.com/fiatjaf/topaz/releases/tag/v0.0.2) am 17. April. Das Projekt ist Kotlin-first und positioniert das Smartphone als stets verfügbares persönliches Relay.

### StableKraft v1.0.0 liefert den ersten stabilen PWA-Release für Musik und Podcasts aus

[StableKraft](https://github.com/ChadFarrow/stablekraft-app) ist eine Next.js-PWA zum Entdecken, Organisieren und Streamen von Musik aus Podcast-Feeds, mit Nostr für Auth und soziale Features und Lightning für V4V-Zahlungen. Das Projekt erreichte [v1.0.0](https://github.com/ChadFarrow/stablekraft-app/releases/tag/v1.0.0) am 18. April. Dieselbe Woche brachte Feed-Ingestion-Härtung und ein kleineres Reparse-Fenster, damit neu hinzugefügte Feeds schneller selbst heilen.

### NipLock liefert einen auf NIP-17 basierenden Passwortmanager aus

[NipLock](https://gitworkshop.dev/npub1z5jf78uhd68znuwwwu926th55rzd0wy8nd9clkr03cx22mwme0jqazk56h/relay.ngit.dev/passwd) ist ein Passwortmanager, der Zugangsdaten über [NIP-17](/de/topics/nip-17/) Gift-Wrapped Direct Messages zwischen Geräten speichert und synchronisiert. Jede Passwort-Zeile ist eine NIP-17-DM vom Schlüssel des Nutzers an sich selbst, sodass dieselben Events auf jedes Gerät replizieren, das sich mit demselben Schlüssel authentifiziert. Signing funktioniert mit nsec, Browser Extensions wie [nos2x](https://github.com/fiatjaf/nos2x) oder [Amber](https://github.com/greenart7c3/Amber) via [NIP-46](/de/topics/nip-46/).

### flotilla-budabit poliert seine NIP-34-Repo-Oberfläche

Die Budabit-Community-Fork von [Flotilla](https://gitea.coracle.social/coracle/flotilla), [flotilla-budabit](https://github.com/Pleb5/flotilla-budabit), lieferte mehrere Fixes für ihren NIP-34-Git-over-Nostr-Workflow aus, darunter wiederhergestellte Repo-Diskussionssteuerung, sichtbare Sticky-Tabs, Laden von Repo-Announcements aus gespeicherten GRASP-Relays und Synchronisierung des durch Maintainer gesetzten Patch-Status.

### rx-nostr 3.7.2 bis 3.7.4 fügen Default-Verifier und optionale Constructor-Argumente hinzu

[rx-nostr](https://github.com/penpenpng/rx-nostr) veröffentlichte [3.7.2](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.2), [3.7.3](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.3) und [3.7.4](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%403.7.4). [PR #192](https://github.com/penpenpng/rx-nostr/pull/192) ergänzt einen standardmäßigen Schnorr-Signaturverifier, und [PR #195](https://github.com/penpenpng/rx-nostr/pull/195) macht die Argumente von `createRxNostr()` optional.

### Keep Android v1.0.0 liefert mit reproducible builds und null Trackern aus

[Keep](https://github.com/privkeyio/keep-android) veröffentlichte [v1.0.0](https://github.com/privkeyio/keep-android/releases/tag/v1.0.0) am 21. April nach mehreren Hardening-PRs. Dazu gehören reproducible builds mit fixierter Toolchain, der Wechsel von Google ML Kit zu ZXing und ein [Exodus Privacy scan](https://reports.exodus-privacy.eu.org/en/), der null Tracker auf dem v1.0.0-Build zeigt.

### Flotilla 1.7.3 und 1.7.4 fügen kind-9-Wrapping für reichere NIP-29-Räume hinzu

[Flotilla](https://gitea.coracle.social/coracle/flotilla), hodlbods [NIP-29](/de/topics/nip-29/)-Client, veröffentlichte [1.7.3](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.3) und [1.7.4](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.4). Die wichtigste Protokolländerung ist kind-9-Wrapping für Nicht-Chat-Inhaltstypen, angekündigt in [hodlbods Release-Note](nostr:nevent1qvzqqqqqqypzp978pfzrv6n9xhq5tvenl9e74pklmskh4xw6vxxyp3j8qkke3cezqyvhwumn8ghj76rzwghxxmmjv93kcefwwdhkx6tpdshszrnhwden5te0dehhxtnvdakz7qgawaehxw309a5x7ervvfhkgtnrdaexzcmvv5h8xmmrd9skctcqyrrclae7mhmm5dnumwfzhg3fxu74a4hh24jd8pvn8v0hye9w3g6tuljtr85) und verknüpft mit [NIP PR #2310](https://github.com/nostr-protocol/nips/pull/2310).

### WoT Relay v0.2.1 migriert den Eventstore auf LMDB

[WoT Relay](https://github.com/bitvora/wot-relay) veröffentlichte [v0.2.1](https://github.com/bitvora/wot-relay/releases/tag/v0.2.1) am 22. April. [PR #97](https://github.com/bitvora/wot-relay/pull/97) migriert den Eventstore auf [LMDB](http://www.lmdb.tech/), [PR #99](https://github.com/bitvora/wot-relay/pull/99) aktualisiert `golang.org/x/crypto`, und [PR #100](https://github.com/bitvora/wot-relay/pull/100) aktualisiert die beworbene [NIP-11](/de/topics/nip-11/)-Software-URL und Versionszeichenkette.

### Formstr suite: Pollerama-Security-Pass, Forms-i18n, Calendar-RRULE-Support

Die Formstr-Suite mergte 26 PRs über Pollerama, Formstr Forms und Nostr Calendar hinweg. [Pollerama](https://pollerama.fun) härte sein Key-Handling, indem gecachte Direct Messages beim Logout verfallen, lokale Keys in sichere Browser-Storage wandern und `JSON.parse` von kind-0-Profilen auf allen Login-Pfaden abgesichert wird. [Formstr](https://formstr.app) ergänzte Audio- und Video-URLs, i18n und einen Google-Forms-Importer. [Nostr Calendar by Formstr](https://calendar.formstr.app) veröffentlichte [v1.3.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.3.0) und [v1.4.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.4.0) mit RRULE-Unterstützung, UTC-Korrektur für Floating-Dates und überarbeitetem Login- und Loading-Pfad.

### Also shipped: notedeck, nostr.blue, cliprelay, Captain's Log

Mehrere Clients veröffentlichten kleinere iterative Releases ohne große Headlines. notedeck brachte v0.10.0-beta.4 mit Column-Rendering- und Relay-Pool-Fixes, nostr.blue v0.8.6 zog Dioxus 0.7.5 nach und reparierte den Android-Build, cliprelay veröffentlichte Desktop v0.0.3 und Android v0.0.4, und Captain's Log lieferte Alpha-Builds mit Liveness Detection für Sync-Relays.

## In Development

### whitenoise-rs refaktoriert zu session-scoped Account-Views

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs), der Rust-Daemon unter dem [Marmot](/de/topics/marmot/)-Client, mergte 15 PRs, die einen mehrphasigen Refactor von globalen Singletons zu account-spezifischen `AccountSession`-Views voranbringen. [PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743) schuf das Grundgerüst, Folgephasen migrierten Relay-Handles, Drafts, Settings, Message-Ops, Gruppenfunktionen, Push Notifications und KeyPackage-Reads, und [PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770) verlegt nun auch den Event-Dispatch in die Session.

### White Noise fügt Block/Unblock-UI, Leave-Group und Offline-Hinweise hinzu

[White Noise](https://github.com/marmot-protocol/whitenoise) ergänzte fehlende Group-Lifecycle-Steuerung. [PR #578](https://github.com/marmot-protocol/whitenoise/pull/578) liefert die Block- und Unblock-UI, [PR #571](https://github.com/marmot-protocol/whitenoise/pull/571) und [PR #572](https://github.com/marmot-protocol/whitenoise/pull/572) verkabeln `clear_chat`, `delete_chat` und `leave_and_delete_group` aus der Rust-Seite in die App, und [PR #569](https://github.com/marmot-protocol/whitenoise/pull/569) plus [PR #576](https://github.com/marmot-protocol/whitenoise/pull/576) ergänzen Offline-Hinweise in Chat- und Settings-Screens.

### MDK fügt Mixed-Version-Invite-Support und SelfUpdate-Konvergenz hinzu

[MDK](https://github.com/marmot-protocol/mdk) mergte sieben PRs. Die wichtigste Korrektur ist [PR #261](https://github.com/marmot-protocol/mdk/pull/261), die `RequiredCapabilities` einer Gruppe als LCD der Invitee-Fähigkeiten berechnet und damit Mixed-Version-Invites zwischen Amethyst und White Noise freischaltet. [PR #264](https://github.com/marmot-protocol/mdk/pull/264) vereinheitlicht das SelfUpdate-Wire-Format, weitere PRs härten Invitee-KeyPackage-Parsing, Admin-Depletion-Validierung und In-Memory-Storage.

### nostter fügt NIP-44-Verschlüsselung für People Lists, Bookmarks und Mutes hinzu

[nostter](https://github.com/SnowCait/nostter) mergte 10 PRs. [PR #2088](https://github.com/SnowCait/nostter/pull/2088) ergänzt [NIP-44](/de/topics/nip-44/) für Mute-Listen, [PR #2089](https://github.com/SnowCait/nostter/pull/2089) für Bookmarks und [PR #2090](https://github.com/SnowCait/nostter/pull/2090) für People Lists. Damit wandert die App dort, wo es passt, von [NIP-04](/de/topics/nip-04/) ab.

### zap.cooking liefert Nourish-Scoring und wiederverwendbaren Comment Thread

[zap.cooking](https://github.com/zapcooking/frontend) mergte 20 PRs. Das zentrale Feature ist ein neues Nourish-Rezeptbewertungsmodul, dazu kommt ein vierstufiger Refactor, der das Comments-Modul zu einem wiederverwendbaren `CommentThread` macht.

### ridestr extrahiert gemeinsamen Rider Coordinator

[ridestr](https://github.com/variablefate/ridestr) mergte 10 PRs, refaktorierte Compose-Screens in fokussierte Komponenten und extrahierte Protokolllogik für Rider und Driver in ein gemeinsames `:common`-Coordinator-Modul. [PR #60](https://github.com/variablefate/ridestr/pull/60) ergänzt einen kind-`3189`-Driver-Ping-Receiver.

### Blossom entwirft einen BUD-01-Sunset-Header für Blob-Expiration

[Blossom](https://github.com/hzrd149/blossom) eröffnete [PR #99](https://github.com/hzrd149/blossom/pull/99), um einen `Sunset`-Header zu BUD-01 hinzuzufügen. Ein Server könnte damit einen zukünftigen Timestamp ankündigen, ab dem ein Blob nicht mehr ausgeliefert wird.

## New Projects

### Forgesworn veröffentlicht ein 29-Repos-umfassendes kryptographisches Toolkit für Nostr

[Forgesworn](https://github.com/forgesworn) veröffentlichte in fünf Tagen 29 Open-Source-Repositories für Signing, Identity, Attestations, Web of Trust und Paid-API-Discovery auf Nostr. Zum Signing-Stack gehören [nsec-tree](https://github.com/forgesworn/nsec-tree), [Heartwood](https://github.com/forgesworn/heartwood), [Sapwood](https://github.com/forgesworn/sapwood) und [nsec-tree-cli](https://github.com/forgesworn/nsec-tree-cli). Auf der Identity-Seite erreichte [Signet](https://github.com/forgesworn/signet) [v1.6.0](https://github.com/forgesworn/signet/releases/tag/v1.6.0), [nostr-attestations](https://github.com/forgesworn/nostr-attestations) definiert ein einheitliches kind-`31000`-Event, und [nostr-veil](https://github.com/forgesworn/nostr-veil) baut ein privacy-preserving Web of Trust auf LSAG-Ring-Signaturen.

Die Monetisierungsseite deckt bezahlte APIs über Lightning und Nostr ab. [toll-booth](https://github.com/forgesworn/toll-booth) ist ein L402-Middleware-Layer für mehrere Frameworks, [toll-booth-dvm](https://github.com/forgesworn/toll-booth-dvm) exponiert die API als [NIP-90](/de/topics/nip-90/) Data Vending Machine, und [402-announce](https://github.com/forgesworn/402-announce) publiziert kind-`31402`-Events für HTTP-402-Service-Discovery auf Nostr.

### ShockWallet liefert Nostr-nativen Lightning-Wallet-Sync und Multi-Node-Verbindungen aus

[ShockWallet](https://github.com/shocknet/wallet2) ist eine Lightning-Wallet, die Nostr als Transport für die Verbindung zu selbstverwahrten Lightning-Nodes nutzt. Die App koppelt sich über ein `nprofile` an einen oder mehrere [Lightning.Pub](https://github.com/shocknet/Lightning.Pub)-Nodes und signiert Payment-Autorisierungen Ende zu Ende zwischen Wallet und Node. Das Team lieferte [PR #608](https://github.com/shocknet/wallet2/pull/608) mit einer neuen Channels-Dashboard-UI aus, dazu kamen ein Admin-Invite-Link-QR-Flow und Verbesserungen für das Metrics-Dashboard.

ShockWallet nutzt [NIP-78](/de/topics/nip-01/) application-specific data events für Multi-Device-Wallet-State-Sync, sodass die Wallet-Sicht über Browser und Smartphone konsistent bleibt, ohne einen zentralen Sync-Server.

### Nostrability-Issues wechseln nach GitHub-Zensur zu Git over Nostr

[Nostrability](https://gitworkshop.dev/elsat@habla.news/nostrability/issues), elsats Interoperabilitäts-Tracker für Nostr-Clients und Relays, verlagert seinen Issue-Workflow auf Git over Nostr, nachdem die GitHub-Organisation Nostrability entfernt wurde und zwei Wochen lang keine Antwort vom GitHub-Support kam.

### nowhere codiert vollständige Websites in URL-Fragmente und routet Bestellungen über Nostr

[nowhere](https://github.com/5t34k/nowhere) serialisiert eine komplette Website in den URL-Fragmentteil nach `#`, komprimiert sie und kodiert sie base64url. Weil Browser Fragmente nicht an Server senden, sieht der Host, der die Seite ausliefert, den eigentlichen Inhalt nie. Fünf der acht Site-Typen sind statisch, für Store, Forum und Petition läuft die Live-Kommunikation über Nostr-Relays und [NIP-44](/de/topics/nip-44/)-verschlüsselte Events mit Wegwerf-Schlüsseln.

### Kleine neue Flächen: relayk.it und Brainstorm Search

Zwei kleine Projekte verdienen ohne großes Changelog eine Erwähnung. [relayk.it](https://relayk.it) ist ein mit [Shakespeare](https://shakespeare.diy) gebauter Relay-Discovery-Client komplett im Browser. [Brainstorm Search](https://brainstorm.world) ist eine Single-Page-Nostr-Suche mit Fokus auf Inhalte im gesamten Netzwerk.

## Protocol and Spec Work

### NIP Updates

Aktuelle Vorschläge und Diskussionen im [NIPs repository](https://github.com/nostr-protocol/nips):

**Open PRs and Discussions:**

- **[NIP-67](/de/topics/nip-67/): EOSE Completeness Hint** ([PR #2317](https://github.com/nostr-protocol/nips/pull/2317)): Schlägt ein optionales drittes Element für `EOSE` vor, damit ein Relay explizit signalisieren kann, ob alle passenden gespeicherten Events geliefert wurden.
- **NIP-5D: Nostr Applets** ([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): Schlägt einen neuen kind für interaktive Applets auf Nostr vor, zwischen [NIP-5A](/de/topics/nip-5a/) und [NIP-5C](/de/topics/nip-5c/).
- **NIP-29: Subgroups spec** ([PR #2319](https://github.com/nostr-protocol/nips/pull/2319)): Erweitert [NIP-29](/de/topics/nip-29/) um eine Subgroup-Hierarchie für mehrere Channels innerhalb einer Gruppe.
- **NIP-29: Explicit role permissions on kind 39003** ([PR #2316](https://github.com/nostr-protocol/nips/pull/2316)): Definiert ein explizites Berechtigungsschema für Rollen in NIP-29.
- **NIP-11: access_control field for gated-relay discovery** ([PR #2318](https://github.com/nostr-protocol/nips/pull/2318)): Schlägt ein neues optionales `access_control`-Objekt im [NIP-11](/de/topics/nip-11/) Relay Information Document vor.
- **NIP-63a: Minimal Payment Gateway Descriptor** ([PR #2315](https://github.com/nostr-protocol/nips/pull/2315)): Wird seit [Newsletter #18](/de/newsletters/2026-04-15-newsletter/) weiter ausgearbeitet.
- **NIP-XX: Agent Reputation Attestations (Kind 30085)** ([PR #2320](https://github.com/nostr-protocol/nips/pull/2320)): Schlägt ein addressable Event für signierte Attestierungen über autonome Agenten und Services auf Nostr vor.
- **NIP-TPLD: Transient Private Location Data** ([PR #2309](https://github.com/nostr-protocol/nips/pull/2309)): Iteriert weiter am kind-`20411`-Modell und der [NIP-44](/de/topics/nip-44/)-Verschlüsselungsform pro Empfänger.
- **marmot-ts 0.5.0 release PR** ([PR #70](https://github.com/marmot-protocol/marmot-ts/pull/70)): Bündelt die ersten geplanten Breaking Changes im TypeScript-Marmot-Client.

## NIP Deep Dive: NIP-72 (Moderated Communities)

[NIP-72](https://github.com/nostr-protocol/nips/blob/master/72.md) definiert ein Modell für themenbasierte Communities auf Nostr, in dem Moderatoren eine Leseansicht über sonst unbeschränkte Schreibrechte kuratieren. Anders als bei [NIP-29](/de/topics/nip-29/)-Gruppen liegt die Autorität nicht bei einem einzelnen Relay. Eine NIP-72-Community lebt in normalen Nostr-Events, und jedes Relay, das die relevanten Kinds trägt, kann sie ausliefern.

Eine Community wird durch ein addressable kind-`34550`-Event definiert. Das `d`-Tag ist ihr stabiler Slug, `name`, `description`, `image` und `rules` tragen Darstellungsmetadaten, und `p`-Tags mit Marker `moderator` listen die pubkeys auf, deren Freigaben zählen. Nutzer reichen Beiträge ein, indem sie ein beliebiges gewöhnliches Event veröffentlichen und ein `a`-Tag mit der Community-Koordinate hinzufügen. Die Freigabe erfolgt über ein separates kind-`4549`-Event eines Moderators, das die Einreichung referenziert und eine stringifizierte Kopie davon in `content` cached.

Das Modell hat drei wichtige Eigenschaften: Moderationsentscheidungen sind transparent, weil jede Freigabe ein signiertes Nostr-Event ist; Moderation ist nicht exklusiv, weil derselbe Beitrag von mehreren Communities freigegeben werden kann; und sie ist auf Leseschicht umkehrbar, weil ältere Freigaben eines entfernten Moderators in Clients nicht mehr zählen müssen. Der Tradeoff bleibt, dass Einreichungen von Anfang an öffentlich sind. NIP-72 verbirgt unfreigegebene Beiträge auf Rendering-Ebene, hält sie aber nicht vom Wire fern.

## NIP Deep Dive: NIP-57 (Zaps)

[NIP-57](https://github.com/nostr-protocol/nips/blob/master/57.md) definiert zaps, also die Verknüpfung von Lightning-Zahlungen mit Nostr-Identitäten und Inhalten. Ein Zap beweist, dass ein bestimmter Sender einen bestimmten Betrag an einen bestimmten Empfänger für ein bestimmtes Ziel bezahlt hat und dass dieser Nachweis von jedem Nostr-Client gelesen werden kann. Das NIP verbindet LNURL, Lightning und Nostr in einem gemeinsamen Ablauf.

Der Sender entdeckt zuerst den LNURL-Endpoint des Empfängers aus dessen Profil oder einem `zap`-Tag auf dem Ziel-Event. Danach signiert der Client ein kind-`9734`-Zap-Request-Event und sendet es an den LNURL-Callback, nicht an Relays. Nach Zahlung veröffentlicht der Wallet-Server des Empfängers ein kind-`9735`-Zap-Receipt auf den Relays, die im Request angegeben wurden. Das Receipt enthält den stringifizierten Zap-Request im `description`-Tag, die bezahlte Invoice im `bolt11`-Tag und einen `preimage`-Nachweis.

Die Sicherheitsgarantie entsteht erst durch Validierung. Ein Client sollte die Signatur des Receipts gegen den `nostrPubkey` aus der LNURL-Antwort prüfen, die `bolt11`-Amount gegen den `amount`-Tag vergleichen, den Description-Hash gegen den eingebetteten Request validieren und das `preimage` gegen den `payment_hash` der Invoice prüfen. Ohne diese Prüfungen ist ein Receipt nur eine Behauptung. NIP-57 trägt außerdem [NIP-75](/de/topics/nip-75/) Zap Goals, bei denen beliebige Zap Receipts auf das Fortschrittsziel eines kind-`9041`-Events angerechnet werden.

---

Das war's für diese Woche. Wenn du etwas baust oder Neuigkeiten teilen willst, schreib uns auf Nostr oder schau bei [nostrcompass.org](https://nostrcompass.org) vorbei.
