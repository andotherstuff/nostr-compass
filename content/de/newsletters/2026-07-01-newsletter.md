---
title: 'Nostr Compass #29'
date: 2026-07-01
publishDate: 2026-07-01
translationOf: /en/newsletters/2026-07-01-newsletter.md
translationDate: 2026-08-27
draft: false
type: newsletters
---

Willkommen zurück bei Nostr Compass, eurem wöchentlichen Wegweiser für Nostr.

**Diese Woche:** [FIPS v0.4.0](#fips-v040-ships-nym-mixnet-transport-mdns-discovery-and-a-data-plane-overhaul) liefert einen Nym-Mixnet-Transport, optionale mDNS-LAN-Discovery, unterbrechungsfreies Rekeying bei Paketverlust und eine Überarbeitung der Datenebene, wire-kompatibel mit v0.3.0. [Whitenoise Linux](#whitenoise-linux-surfaces-as-a-desktop-marmot-client) erscheint als Desktop-Marmot-Client in Rust und Slint; ein Protokollvorschlag verlagert Nachrichteneffekte in ein eigenes Kind-9-Event. [CustID v0.1.10-beta](#custid-launches-as-a-mobile-identity-vault-with-nip-46-and-nfc-challenge-flow) startet als hardwaregestützter mobiler Identitäts-Tresor, der als NIP-46-Remote-Signer arbeitet und physische Zugangs-Challenges über NFC beantwortet. [myco](#myco-launches-peer-to-peer-nsite-sharing-over-the-fips-mesh) startet Peer-to-Peer-nsite-Sharing über das FIPS-Mesh mit einem neuen BLE-L2CAP-Transport in v0.1.0. [Nostr Codex Phone](#nostr-codex-phone-launches-as-a-mobile-control-surface-for-a-local-codex-worker-over-nostr) startet als Android-Steueroberfläche für einen lokalen Codex-Coding-Assistenten über verschlüsselte Nostr-DMs. [Amethysts unveröffentlichter Stand](#amethyst-builds-nip-89-aware-ui-a-git-repositories-feed-and-a-napplet-browser-discover-section) ergänzt NIP-89-App-Handler-Parsing, einen Git-Repositories-Feed für NIP-34 und einen Discover-Bereich für nSites und napplets. [Notedeck](#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments) implementiert NIP-37, NIP-52 und NIP-22 in einer Woche. [Applesauce](#applesauce-ships-12-sub-packages-in-a-coordinated-62x-cut) veröffentlicht 12 Subpackage-Releases mit nbunksec-NIP-46-Helfern und einem Cashu-ts-v4-Wallet-Upgrade. [Meiso v1.4.0](#meiso-v140-ships-shared-key-collaborative-lists-that-replace-mls-for-task-sharing) liefert Shared-Key Collaborative Lists auf dem adressierbaren Kind 35000. Das NIPs-Repository mergte fünf PRs, darunter ein Relay-Roles-Event, die Aufhebung des NIP-44-Limits von 65.535 Byte, NIP-34-Fork-Semantik, NIP-46-Client-Metadaten und eine NIP-86-`signevent`-Methode. Die Deep Dives behandeln [NIP-86 (Relay-Verwaltungs-API)](#nip-deep-dive-nip-86-relay-management-api) und [NIP-89 (empfohlene Application Handler)](#nip-deep-dive-nip-89-recommended-application-handlers).

---

## Top-Storys

### FIPS v0.4.0 liefert Nym-Mixnet-Transport, mDNS-Discovery und eine überarbeitete Datenebene {#fips-v040-ships-nym-mixnet-transport-mdns-discovery-and-a-data-plane-overhaul}

[FIPS](https://github.com/jmcorgan/fips) ist ein privates, selbstorganisierendes Peer-to-Peer-Mesh-Netzwerk für Nostr, in dem Nodes einander finden und Traffic ohne zentrale Infrastruktur routen. [FIPS v0.4.0](https://github.com/jmcorgan/fips/releases/tag/v0.4.0) bringt einen Nym-Mixnet-Transport, optionale mDNS-LAN-Discovery, eine überarbeitete Datenebene, unterbrechungsfreies Rekeying bei Paketverlust, eine auf einem Render-Snapshot-Harness neu geschriebene `fipstop`-TUI, eine Observability-Ebene außerhalb des Hot Paths sowie neue Packaging-Ziele für OpenWrt apk und Nix flake. Alles bleibt wire-kompatibel mit v0.3.0, sodass gemischte Meshes während eines Rolling Upgrades interoperabel bleiben. Zwei neue Transporte für Peer-Discovery prägen das Release. Ein neuer [ausgehender Nym-Mixnet-Transport](https://github.com/jmcorgan/fips/releases/tag/v0.4.0) routet FIPS-Traffic über einen `nym-socks5-client`-SOCKS5-Proxy und mischt ihn in das Cover-Traffic-Netzwerk von [Nym](https://nymtech.net/), sodass Beobachter auf Link-Ebene nicht korrelieren können, welche Mesh-Peers miteinander sprechen. Ein Verzeichnis `examples/sidecar-nostr-mixnet-relay/` demonstriert ein Nostr-relay, das über einen FIPS-Link erreichbar ist, der Ende zu Ende über das Mixnet peert. Optionale mDNS-/DNS-SD-LAN-Discovery lässt Nodes im selben lokalen Netz ohne Adresskonfiguration und ohne STUN zueinanderfinden; Peers werden über einen Standard-Service-Record bei `node.discovery.lan.enabled: true` angekündigt und übernommen.

Die Datenebene wurde für höheren Durchsatz eines einzelnen Nodes überarbeitet. Ver- und Entschlüsselung pro Peer laufen nun auf eigenen Worker-Tasks außerhalb des Receive-Loops, sodass ein ausgelasteter Peer nicht mehr die Kryptografie des gesamten Nodes serialisiert. Der Linux-Sendepfad nutzt Generic Segmentation Offload und, wo verfügbar, einen verbundenen UDP-Socket; der Receive-Hot-Path vermeidet zuvor pro Paket angelegte Buffer-Kopien; macOS erhält einen gebündelten `recvmsg_x`-Receive als Gegenstück zum Linux-Batching mit `recvmmsg` aus v0.3.0. Die gesamte `show_*`-Leseoberfläche für `fipsctl` und `fipstop` bedient sich nun aus einem Snapshot pro Tick, den der Control-Accept-Task in ein lockfreies `ArcSwap` veröffentlicht. Operator-Abfragen antworten dadurch auch dann schnell, wenn der Receive-Loop eines Nodes ausgelastet ist. Eine neue reine Counter-Abfrage `show_metrics` (als `fipsctl stats metrics` verfügbar) ermöglicht Prometheus-Scraping ohne Kosten im Hot Path.

FMP- und FSP-Session-Rekeying erfolgt nun bei Paketverlust und Neuordnung in beiden Richtungen ohne Unterbrechung: Eingehende Frames authentifizieren sich vor dem K-Bit-Cutover gegen die ausstehende Session, bevor diese hochgestuft wird, sodass ein veralteter oder gefälschter Frame das Rekeying nicht entgleisen lassen kann. Die erneute Übertragung von Rekey-Nachricht 1 ist begrenzt, der Link-Dead-Heartbeat berücksichtigt Rekeying, und Rennen durch beidseitige Initiierung auf Links mit hoher Latenz werden durch symmetrischen Jitter entzerrt. Die `fipstop`-TUI wurde auf einem Render-Snapshot-Harness neu aufgebaut, das das exakte Textraster und den Stil jeder Zelle jeder Ansicht gegen vorbereitete Control-Socket-Ausgaben prüft. Hinzu kommen neue Packaging-Ziele: ein OpenWrt-`.apk` für OpenWrt 25+ (SDK-frei gebaut, unter Wiederverwendung des bestehenden `.ipk`-Cross-Compiles und des installierten Dateisystem-Payloads) sowie eine `flake.nix` im Projektstamm, die alle vier Binaries (`fips`, `fipsctl`, `fips-gateway`, `fipstop`) mit der gepinnten Toolchain aus dem Quellcode für Nix/NixOS baut.

### Whitenoise Linux erscheint als Desktop-Marmot-Client {#whitenoise-linux-surfaces-as-a-desktop-marmot-client}

[Whitenoise Linux](https://relay.ngit.dev/npub1ven4zk8xxw873876gx8y9g9l9fazkye9qnwnglcptgvfwxmygscqsxddfh/darkmatter-linux.git) ist ein Desktop-[Marmot](/de/topics/marmot/)-Client: MLS-Gruppennachrichten über Nostr-relays, verpackt als einzelnes Rust-Binary mit einer Slint-UI, die jedes Geheimnis in einem passwortverschlüsselten Tresor hält.

Der folgenreichste Thread dieser Woche schlägt vor, Whitenoise-Nachrichteneffekte als eigenes Kind-9-Event zu transportieren, das auf die übergeordnete Nachricht verweist. Das heutige Wire-Format hängt einen Marker wie `dmfx:sparkle` an das Ende des Nachrichtentextes an und verschmutzt damit den Text für jeden Renderer, der diese Konvention nicht kennt. Werden Effekte in ein eigenes Event verschoben, bleibt der Nachrichtentext sauber. Zugleich stellt sich eine Designfrage für den breiteren Marmot-Stack: Inline-Konventionen im Body oder Sidecar-Events für optionale Rich Features.

### CustID startet als mobiler Identitäts-Tresor mit NIP-46 und NFC-Challenge-Flow {#custid-launches-as-a-mobile-identity-vault-with-nip-46-and-nfc-challenge-flow}

[CustID v0.1.10-beta](https://zapstore.dev/apps/naddr1qq9rzqtdwfshxwf0wccsygqv94d2qg37755z67q9yjz6q60lcejldsc3ttak83333gjqgyvf3aqpsgqqqyf6w24n0c) ist die erste öffentliche Beta von CustID, einem auf Nostr und dem SISTR-Protokoll aufgebauten mobilen Identitäts-Tresor. CustID speichert mehrere Nostr-Identitäten in hardwaregestütztem sicherem Speicher, arbeitet für andere Clients als [NIP-46](/de/topics/nip-46/)-Remote-Signer und beantwortet physische und Online-Zugangs-Challenges über NFC und QR-Codes.

Die Beta ist für den NIP-46-Signer und den NFC-Challenge-Response-Flow funktionsvollständig; Zugangsabläufe mit Zero-Knowledge-Proofs bleiben ein künftiger Meilenstein. Das Release entfernt außerdem die im Hintergrund laufende [NIP-65](/de/topics/nip-65/)-Keep-alive-Schicht der App. Sie hatte pro Profil und Read-relay einen WebSocket geöffnet und Kinds eingelesen, die der Client sofort verwarf. Im Hintergrund bleiben nun nur die NIP-46-Sockets aktiv, die Benachrichtigungen über Signieranforderungen transportieren. Erst diese Korrektur macht den Betrieb von CustID als Bunker für andere Clients auf einem Smartphone praktikabel.

### myco startet Peer-to-Peer-nsite-Sharing über das FIPS-Mesh {#myco-launches-peer-to-peer-nsite-sharing-over-the-fips-mesh}

[myco v0.1.0](https://github.com/Origami74/myco/releases/tag/v0.1.0) wurde diese Woche am 27. Juni geöffnet und erreichte am 1. Juli v0.1.0. myco ist eine Rust-Android-App, die Apps von Menschen in der Nähe installiert: Peer-to-Peer-[nsite](/de/topics/nip-5a/)-Sharing über ein FIPS-Mesh mit jedem Transport, den das Mesh tragen kann (UDP, TCP, Tor, Bluetooth), vollständig offline. Das Design verbindet FIPS direkt als Transportsubstrat mit dem Static-Website-Event-Format von NIP-5A als Payload. Eine als nsite verteilte App kann dadurch zwischen Mesh-Peers wandern, ohne von relays oder HTTP abhängig zu sein.

v0.1.0 ergänzt einen L2CAP-Bluetooth-Funkpfad, über den zwei Smartphones mit installiertem FIPS ohne Netzwerk über BLE peeren können, dazu einen Speedtest pro Peer und NFC-ausgelöstes Sharing aus dem Circle-Bottom-Sheet der App. myco ist außerdem zur direkten Installation auf Zapstore veröffentlicht.

### Nostr Codex Phone startet als mobile Steueroberfläche für einen lokalen Codex-Worker über Nostr {#nostr-codex-phone-launches-as-a-mobile-control-surface-for-a-local-codex-worker-over-nostr}

[Nostr Codex Phone v0.1.122](https://github.com/tidley/nostr-codex-phone) startet diese Woche als Android-Client, der einen lokalen Codex-Coding-Assistant-Worker über verschlüsselte Nostr-Direktnachrichten steuert. Die App unterstützt mehrere Repository-Sessions, Sprachtranskription, geroutete Worker-Sessions, Blossom-Medien-Uploads und optionale gesprochene Antworten. Entwickler, die zu Hause einen Codex-Worker betreiben, können so von ihrem Smartphone überall dort Aufträge senden, wo das Telefon Relay-Zugriff hat.

Das Projekt ist ein direktes Geschwister von [CodeDeck](/en/newsletters/2026-06-24-newsletter/#codedeck-remote-agentic-coding-over-nostr), das in #28 startete. Beide bringen agentische Coding-Workflows mit verschlüsselten DMs auf den Nostr-Transport und nutzen Nostr als Pairing- und Messaging-Schicht, über die ein Smartphone einen heimischen Worker erreicht, ohne Löcher ins Netzwerk zu öffnen. Nostr als Control Plane für lokale Agenten entwickelt sich zu einem etablierten Muster.

### Coop Mobile veröffentlicht seine ersten versionierten Builds

[Coop Mobile v0.2.1](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.1) und [v0.2.2](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.2) erschienen diese Woche als erste versionierte Builds von Coop Mobile, einem Android-Client für verschlüsselte [NIP-17](/de/topics/nip-17/)-Direktnachrichten. Die beiden Releases erhöhen die Absturzsicherheit beim Parsen von Nachrichten und beim QR-Handling und löschen beim Abmelden alle gespeicherten Daten.

### Amethyst baut NIP-89-fähige UI, einen Git-Repositories-Feed und einen napplet-Discover-Bereich {#amethyst-builds-nip-89-aware-ui-a-git-repositories-feed-and-a-napplet-browser-discover-section}

[Amethysts](https://github.com/vitorpamplona/amethyst) Main-Branch baute diese Woche mehrere neue Oberflächen aus. Ein [Git-Repositories-Feed](https://github.com/vitorpamplona/amethyst/pull/3406) macht [NIP-34](/de/topics/nip-34/)-Repos zu einer durchsuchbaren Android-Timeline-Kategorie, filterbar nach Community und Autor, zusammen mit einem [Smart-HTTP-Git-Browser](https://github.com/vitorpamplona/amethyst/pull/3415), der Repository-Inhalte und Commits liest, ohne die App zu verlassen. Der napplet-Host erhielt einen [Discover-Bereich](https://github.com/vitorpamplona/amethyst/pull/3409), der kuratierte Web-Apps sowie gefolgte nSites und napplets aus [NIP-89](/de/topics/nip-89/)-Handler-Events und [NIP-5A](/de/topics/nip-5a/)-Site-Events auflistet. Die Notizanzeige [zeigt nun, welche Nostr-App ein Event verfasst hat](https://github.com/vitorpamplona/amethyst/pull/3422), und nutzt dafür NIP-89-Tags. Auf der Sync-Seite landet [NIP-77-Negentropy-Unterstützung](https://github.com/vitorpamplona/amethyst/pull/3434) mit Streaming-Reconciliation und automatischer `created_at`-Fensterung, um Relay-seitige Ergebnislimits zu umgehen. Das reduziert die Bandbreite, die nötig ist, um große lokale Event-Sets mit einem relay synchron zu halten.

### Buzz v0.3.38 härtet die Relay-Angriffsfläche und ergänzt providerunabhängige Modellauswahl

[Buzz v0.3.38](https://github.com/block/buzz/releases/tag/v0.3.38) härtet die [Relay-Angriffsfläche](https://github.com/block/buzz/pull/1369), die Buzz beim Veröffentlichen von Personas, Teams, verwalteten Agenten und NIP-OA-Owner-Attestierungen als signierte Nostr-Events exponiert. Ein Buzz-relay ist ein öffentliches Verzeichnis der Nostr-Identitäten eines Teams und ihres Zustands; dieses Release verschärft Eingabevalidierung und Replay-Schutz für die bekannten Event-Kinds, die Buzz definiert. Das Release verallgemeinert außerdem die Modellauswahl, sodass ein Buzz-Team jeden Provider ansprechen kann, für den Buzz Adapter besitzt, darunter ein neues Databricks-AI-Gateway-v2-Backend.

### Notedeck implementiert NIP-37-Private-Sync-relays, NIP-52-Kalender und NIP-22-Kommentare {#notedeck-implements-nip-37-private-sync-relays-nip-52-calendar-and-nip-22-comments}

[Notedeck](https://github.com/damus-io/notedeck), der native Rust-Desktop-Client des Damus-Teams, implementierte in einer Woche drei Protokolle. Private-Sync-relays werden nun als Kind-`10013`-[NIP-37](/de/topics/nip-37/)-Liste gespeichert, getrennt vom öffentlichen NIP-65-Outbox-Set des Nutzers. Der Kalenderbereich `horizon` liest [NIP-52](/de/topics/nip-52/)-Events aus nostrdb und erhielt ein neu gestaltetes Dreispalten-Layout. Der Bereich `headway` ergänzte ein [NIP-22](/de/topics/nip-22/)-Kommentar-Event-Modell auf Kind `1111`, dem von NIP-22 definierten Kind für die einheitliche Kommentaroberfläche, die NIP-10-Reply-Threading ersetzt.



### Applesauce bringt nbunksec-NIP-46-Sessions und ein Cashu-v4-Wallet-Upgrade {#applesauce-ships-12-sub-packages-in-a-coordinated-62x-cut}

[Applesauce](https://github.com/hzrd149/applesauce), das modulare Nostr-Toolkit für Signer, relays, Wallets und Inhalte, veröffentlichte ein koordiniertes [6.2.x-Release](https://github.com/hzrd149/applesauce/releases) über seine Subpackages. Das Signers-Package erhielt Helfer zum Import und Export von `nbunksec`, die eine [NIP-46](/de/topics/nip-46/)-Bunker-Session als portables Artefakt behandeln, das zwischen Clients verschoben werden kann. Das Wallet-Package aktualisierte seine [Cashu](/de/topics/nip-60/)-Bindings auf `@cashu/cashu-ts` v4, wo Proof-Beträge zu `Amount`-Value-Objects werden und sich die Token-Decoding-API ändert.

---

## Getaggte Releases

### mostro-core v0.14.0

[mostro-core v0.14.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.0) bringt die nächste Protokolliteration für das [Mostro](/de/topics/nip-69/)-P2P-Fiat-Handelsnetzwerk. Das Release folgt auf [v0.13.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.2) und erscheint zusammen mit [mostro-cli v0.16.0](https://github.com/MostroP2P/mostro-cli/releases/tag/v0.16.0), das den neuen Core übernimmt. Drei gemergte PRs landeten diese Woche im Core-Repository; der übrige Stack (mostro daemon und Mostro mobile) zielt auf v0.14.0 des gemeinsamen Types-Crates.

### ngit v2.6.1

[ngit v2.6.1](https://github.com/DanConwayDev/ngit-cli), das maßgebliche Git-over-Nostr-CLI für [NIP-34](/de/topics/nip-34/)-Repositories, implementiert die diese Woche gemergte [NIP-34-GRASP-06-Fork-Semantik](https://github.com/nostr-protocol/nips/pull/2395), die auf Repo-State-Events den `personal-fork`-Tag durch einen `u`-Tag ersetzt.

### mesh-llm v0.72.0 und v0.72.1

[mesh-llm](https://github.com/Mesh-LLM/mesh-llm), die Inferenzkomponente des ContextVM-Stacks, die Open-Source-LLMs hinter einer über Nostr adressierbaren JSON-RPC-Oberfläche betreibt, veröffentlichte [v0.72.0](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.0) und [v0.72.1](https://github.com/Mesh-LLM/mesh-llm/releases/tag/v0.72.1) mit einer Korrektur für einen Batching-Absturz bei großen Einzel-Prompts und einer Migration der MCP-Bridge weg von veralteten Helfern.

### Meiso v1.4.0 liefert Shared-Key Collaborative Lists, die MLS beim Teilen von Aufgaben ersetzen {#meiso-v140-ships-shared-key-collaborative-lists-that-replace-mls-for-task-sharing}

[Meiso v1.4.0](https://github.com/higedamc/meiso/releases/tag/v1.4.0) führt ein Modell für Shared-Key Collaborative Lists ein, das das bisherige MLS-basierte Teilen von Aufgaben durch ein einfacheres Design mit adressierbaren Events ersetzt. Jede geteilte Liste erzeugt einen eigenen, an Mitglieder verteilten Nostr-Schlüssel. Aufgaben sind adressierbare Events auf Kind `35000`, mit `d=task-id` gekennzeichnet und mit per [NIP-44](/de/topics/nip-44/) selbstverschlüsseltem Content; relays erzwingen Last-Write-Wins pro Aufgabe. Das Design gibt die Forward Secrecy und Post-Compromise Security von MLS zugunsten einer einfacheren Client-Implementierung und Relay-seitiger Konfliktauflösung auf.

### Cordn 0.3.2

[Cordn 0.3.2](https://github.com/Cordn-msg/cordn) liefert einen „more-private-coordinator“-Track, der kurzlebige Sender-Pubkeys aus dem Veröffentlichen von Gruppennachrichten entfernt und den Join-Request-Flow gegen veraltete Neuanfragen härtet. Cordn ist der MLS-basierte Messaging-Stack aus dem [Cordn-Ad-hoc-CVM-Launch in #28](/en/newsletters/2026-06-24-newsletter/#cordn-ad-hoc-cvm-a-browser-based-mls-coordinator); dieses Release ist das passende Update auf Coordinator-Seite.

---

## Unveröffentlichte Änderungen

### diVine bringt mit 108 gemergten PRs Feinschliff nach dem Launch

[diVine](https://github.com/divinevideo/divine-mobile), der Kurzvideo-Looping-Client, der Vine zurückbringt, durchläuft eine intensive Feinschliffphase nach dem Launch. Die Nostr-sichtbare Arbeit dieser Woche ist eine Stabilitätsrunde für den [NIP-46](/de/topics/nip-46/)-Connect-Flow, die Fehler von `nostrconnect://` auf strukturierte Reason Codes migriert.

### Zap Cooking setzt die projektübergreifende NIP-46-Korrektur und die Composer-Überarbeitung fort

[Zap Cooking](https://github.com/zapcooking/frontend) ist ein Nostr-Client zum Teilen von Rezepten, in dem Rezepte als Nostr-Langform-Events veröffentlicht werden. Die Arbeit dieser Woche setzt die projektübergreifende [NIP-46](/de/topics/nip-46/)-Korrektur und Composer-Überarbeitung fort, die in [#28](/en/newsletters/2026-06-24-newsletter/#unreleased-changes) als unveröffentlicht behandelt wurde.

### Conduit härtet Listing-Ablauf und Marketplace-Korrektheit

[Conduit](https://github.com/Conduit-BTC/conduit-mono) ist ein Marketplace-Monorepo mit drei Apps auf Nostr: Käufermarkt, Händlerportal und Store-Builder. Die Arbeit dieser Woche setzt den Push für Marketplace-Korrektheit fort, der im [Launch-Bericht von #28](/en/newsletters/2026-06-24-newsletter/#conduit-hardens-the-marketplace-mvp-and-switches-to-its-public-relay-by-default) behandelt wurde, und baut auf der [NIP-99](/de/topics/nip-99/)-Commerce-Welle auf, die in der vorigen Ausgabe die Protokoll-Story bildete.

### Pollerama v1.12 bis v1.13.1 ergänzen Client-Tag-Auswahl, Profil-Tabs und Thread-Limits

[Pollerama](https://github.com/formstr-hq/nostr-polls), ein Android-Nostr-Client mit Schwerpunkt auf Umfragen und Notizen und einer starken Web-of-Trust-Discovery-Schicht, veröffentlichte diese Woche v1.12.0, v1.13.0 und v1.13.1 auf Zapstore. Nutzer können nun wählen, welcher Client-Tag ihren verfassten Notizen und Umfragen angehängt wird, entweder aus einer vorgegebenen Liste oder als eigene Eingabe. Tief verschachtelte Kommentar- und Reply-Ketten enden nun nach wenigen Ebenen und verlinken zum vollständigen Thread auf der Notizseite. Profilseiten öffnen standardmäßig mit Notizen, aufgeteilt in die Tabs Posts und Conversations. Ein Persistenzfehler, durch den neu gefolgte Konten nach einem App-Neustart verschwanden, ist behoben; Follow-Buttons zeigen nun den Fortschritt.

### getwired.app und get-tao.app reparieren den NIP-13-Confess-Submission-Flow

[getwired.app](https://github.com/smolgrrr/Wired) und [get-tao.app](https://github.com/smolgrrr/TAO), die einen gemeinsamen Ablauf für anonyme Posts verwenden und beim Absenden NIP-13-Proof-of-Work gegen Spam einsetzen, reparierten den [Confess-Submission-Flow](https://github.com/smolgrrr/Wired/pull/57), sodass die UX während des PoW-Minings schlüssig ist.

### nostui ergänzt einen Mention-Timeline-Tab

[nostui](https://github.com/akiomik/nostui), ein terminalbasierter Nostr-Client in Rust, ergänzte einen [Mention-Timeline-Tab](https://github.com/akiomik/nostui/pull/463), der Kind-1-Events, die den aktiven Pubkey taggen, als eigene Ansicht in der TUI zeigt.

### Heartwood implementiert NIP-46-Bunker-URIs pro Identität und eine Signing-Bridge im HSM-Modus

[Heartwood](https://github.com/forgesworn/heartwood) ist ein [NIP-46](/de/topics/nip-46/)-Signer, bei dem der Signierschlüssel den Client niemals erreicht: Der Client spricht NIP-46 mit einem kleinen relay, das relay über ein serielles Frame-Protokoll mit einem angeschlossenen Hardwaregerät, das die Signatur ausführt. Diese Woche implementierte das Projekt eine [Relay-zu-Serial-Signing-Bridge](https://github.com/forgesworn/heartwood/pull/11) und [Bunker-Verbindungen pro Identität](https://github.com/forgesworn/heartwood/pull/16), sodass ein einzelnes Hardwaregerät mit mehreren Identitäten für jede davon einen eigenen Bunker-URI exponiert.

### Nostter überarbeitet Auth und Signer

[Nostter](https://github.com/SnowCait/nostter) überarbeitete diese Woche seine [Auth- und Signer-Schicht](https://github.com/SnowCait/nostter/pulls?q=is%3Amerged+auth), verlegte den Login-Zustand auf ein einzelnes Signal und extrahierte den Signer-Dispatch in Strategie-Module. Ziel ist eine klare Signer-Abstraktion, in der NIP-07-Web-Extension, NIP-46-Remote-Bunker und roher nsec denselben Codepfad nutzen.

### Dart NDK extrahiert den NIP-07-Signer und randomisiert NIP-59-Zeitstempel

[Dart NDK](https://github.com/relaystr/dart_ndk) verlagerte seinen [NIP-07](/de/topics/nip-07/)-Signer aus dem Core-Package nach `ndk_flutter`, wo die Flutter-WebView liegt, und [randomisierte seine NIP-59-Gift-Wrap-Zeitstempel](https://github.com/relaystr/dart_ndk/pull/667), um verschlüsselte Nachrichten gegen Timing-Korrelation zu härten.

### Milk Market ergänzt NIP-23-Storefront-Seiten und Square-Zahlungsabwicklung

[Milk Market](https://github.com/shopstr-eng/milk-market), das Marketplace-Storefront des Shopstr-Teams, gab jedem Storefront eine Blog-Seite auf Basis der [NIP-23](/de/topics/nip-23/)-Langform-Events des Verkäufers, mit editierbaren Bereichen und einer direkten Route zu den Blog-Einstellungen. In derselben Woche kamen [Square](https://github.com/shopstr-eng/milk-market/pull/30) als alternative Zahlungsabwicklung für Verkäufer und automatische Versandetiketten-Käufe für bezahlte Bestellungen hinzu.

### Calendar by Formstr veröffentlicht eine iOS-App

[Calendar by Formstr](https://github.com/formstr-hq/nostr-calendar) mergte diese Woche [PR #159 IOS App](https://github.com/formstr-hq/nostr-calendar/pull/159) und brachte damit den [NIP-52](/de/topics/nip-52/)-Kalender-Client auf iOS. [PR #197](https://github.com/formstr-hq/nostr-calendar/pull/197) korrigiert das Parsen von Kalenderdaten in lokaler Zeit, und [PR #201](https://github.com/formstr-hq/nostr-calendar/pull/201) ergänzt einen durch ein `run-tests`-Label ausgelösten Playwright-E2E-Workflow.

### cagliostr erzwingt NIP-22, NIP-09 nach Koordinate und NIP-13-Proof-of-Work

[cagliostr](https://github.com/mattn/cagliostr), eine Go-Relay-Implementierung, verschärfte diese Woche drei Enforcement-Pfade: [konfigurierbarer NIP-13-Proof-of-Work](https://github.com/mattn/cagliostr/pull/7) für eingehende Events, [NIP-09-Löschung nach adressierbarer Koordinate](https://github.com/mattn/cagliostr/pull/8), sodass replaceable Events über ihren `a`-Tag gelöscht werden können, was eine Löschung nur nach Event-ID nicht erreicht, sowie [konfigurierbare NIP-22-Zeitstempellimits](https://github.com/mattn/cagliostr/pull/9), die Events ablehnen, deren Zeitstempel zu weit in Vergangenheit oder Zukunft liegt.

---

## Neu erfasst und entdeckt

Die [Vanderwarker-Wellbeing-Suite](https://git.vanderwarker.family/wellbeing) veröffentlicht Telemetrie aus der physischen Welt als Nostr-Events unter einem gemeinsamen Publisher-Signierschlüssel. Sie besteht aus fünf Geschwister-Apps: [Holy Fit](https://git.vanderwarker.family/wellbeing/holyfit-android) ist ein Schrittzähler, der Fitnessdaten als `kind:30078` in Nostr verankert; [Nunlock](https://git.vanderwarker.family/wellbeing/nunlock-android) veröffentlicht täglich die Zahl der Smartphone-Entsperrungen; [Saint Stream](https://git.vanderwarker.family/wellbeing/saintstream-android) veröffentlicht die aktuelle Medienwiedergabe als User Status; [Sister Charge](https://git.vanderwarker.family/wellbeing/sistercharge-android) veröffentlicht alle 15 Minuten Akkustand, Spannung und Temperatur; [Cellibacy](https://git.vanderwarker.family/wellbeing/cellibacy-android) veröffentlicht den täglichen Datenverbrauch. Alle fünf erschienen zwischen dem 24. und 30. Juni auf Zapstore.

[ntrack v0.1.9](https://github.com/f321x/ntrack/releases/tag/v0.1.9) ist eine verschlüsselte serverlose Android-App für Live-Standortfreigabe, in Rust und Slint gebaut und am 29. Juni veröffentlicht. Sie ist ein Geschwister des [Haven](https://github.com/mehmetefeumit/Haven-App)-Standortteilers auf [Marmot](/de/topics/marmot/)-Basis, der in [#28](/en/newsletters/2026-06-24-newsletter/#haven-launches-private-location-sharing-on-marmot) behandelt wurde, besitzt aber eine andere Transportarchitektur: Verschlüsselte Nostr-DMs tragen die Standort-Updates, während Haven Marmot-Gruppennachrichten nutzt.

[NostrAppShell](https://git.nostrdev.com/stuff/NostrAppShell) ist ein frühes Application-Shell-Scaffold zum Bau von Nostr-Apps. Das Projekt veröffentlichte diese Woche seine erste nutzerorientierte Dokumentation.

[NIPs by Pollerama](https://nips.pollerama.fun) (Repository [abh3po/better-nips](https://github.com/abh3po/better-nips), erstellt am 2026-06-29) ist ein neuer Client für die von der Community verfassten `kind:30817`-NIPs von [NostrHub](https://nostrhub.io), positioniert als vertrauensgewichtete Alternative zu nostrhub.io. Jedes `kind:30817`-NIP besitzt eine eigene teilbare URL (`#/nip/<naddr>`) mit vollständigem Markdown-Rendering und den von ihm definierten Event-Kinds. Der Client bietet drei Feeds: Following, Web of Trust (Follows-of-Follows) und Global, jeweils sortierbar nach vertrauensgewichteten Freigaben oder Neuheit. Freigaben werden als [NIP-32](/de/topics/nip-32/)-Labels auf Kind `1985` mit den Tags `["L","nostrhub"]` und `["l","approve","nostrhub"]` veröffentlicht, dazu ein `a`-Tag auf die NIP-Zieladresse und ein `client`-Tag für `better-nips`. Das ist exakt die Event-Form, die NostrHub selbst signiert, sodass Freigaben zwischen beiden Clients kompatibel sind. Die Freigabe eines direkt gefolgten Kontos wiegt im Ranking stärker als die eines Follows-of-Follows zweiten Grades.

Der Signing-Stack ist [`@formstr/signer`](https://www.npmjs.com/package/@formstr/signer) mit einem vollständigen Login-Modal für [NIP-07](/de/topics/nip-07/), [NIP-46](/de/topics/nip-46/)-Bunker und nostrconnect, [NIP-49](/de/topics/nip-49/)-ncryptsec sowie [NIP-55](/de/topics/nip-55/)-Android-Signer; Sessions verbinden sich beim Neuladen still erneut. Die Netzwerkschicht läuft über [`@formstr/local-relay`](https://www.npmjs.com/package/@formstr/local-relay), einen Web Worker, der die [NIP-65](/de/topics/nip-65/)-Outbox des Nutzers über relays verteilt, damit ein großes Web-of-Trust-Set nicht auf ein einziges relay auffächert. Die Designposition: Community-NIPs sind auf Protokollebene alle gleich, unabhängig davon, ob sie bei NostrHub, in `better-nips` oder bei künftigen Clients gehostet werden. Das Ranking stammt aus dem Social Graph, nicht aus Moderatorenkuration, passend zum NIP-32-Labeling-Flow, den der Deep Dive in [#25](/en/newsletters/2026-06-03-newsletter/#nip-deep-dive-nip-32-labeling) behandelte.

Zwei neue [NIP-34](/de/topics/nip-34/)-Repo-Cluster erschienen diese Woche. [Vidstr](https://git.shakespeare.diy/npub14rg4vrt2v374q95ezeeydu3hkdhmzglcj950mggacap4x0lv0gyq04wun7/vidstr.git) ist ein videofokussierter Nostr-Client, und ein [nostrapps.com-Cluster](wss://gitnostr.com) veröffentlicht drei Geschwisterprojekte: [verdana](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/verdana.git), eine napp-VM für den Desktop; [hallway](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/hallway.git), ein anpassbarer Community-Client; und [napps](https://gitnostr.com/npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6/napps.git), eine Spezifikation und Runtime für HTML-Microapps. Der Cluster liegt parallel zur [napplet](/de/topics/nip-5d/)-Arbeit aus der Top-Story der vorigen Ausgabe.

---

## Protokollarbeit und NIP-Updates

### Gemergt: NIP-44 hebt das Payload-Limit von 65.535 Byte auf

[PR #1907](https://github.com/nostr-protocol/nips/pull/1907) wurde am 28. Juni gemergt, nachdem er seit 2024-09 offen war. Die Änderung entfernt die Obergrenze von 65.535 Byte für den Plaintext-Payload eines versionierten [NIP-44](/de/topics/nip-44/)-Verschlüsselungs-Envelopes und erhöht sie auf 4 GiB (`uint32_max`). NIP-44 kodiert die Payload-Länge im Wire-Format als `uint16`, was die ursprüngliche Spezifikation strikt für Interoperabilität verlangte; die gemergte Änderung übernimmt ein längeres, im Versionsbyte gekennzeichnetes Längenfeld, sodass v2-Implementierungen wire-kompatibel bleiben und v3+-Implementierungen die größere Länge tragen. Clients, die NIP-44 für [NIP-17](/de/topics/nip-17/)-Direktnachrichten, [NIP-59](/de/topics/nip-59/)-Gift-Wraps, [NIP-46](/de/topics/nip-46/)-Remote-Signer-Payloads oder andere NIP-44-verschlüsselte Nostr-Nachrichten einsetzen, können nun einzelne Events über 64 KiB austauschen, ohne sie auf Anwendungsebene aufzuteilen.

### Gemergt: NIP-86 erhält eine `signevent`-Methode und ein Relay-Roles-Event

[PR #2389](https://github.com/nostr-protocol/nips/pull/2389) ergänzt die [NIP-86](/de/topics/nip-86/)-JSON-RPC-API zur Relay-Verwaltung um eine `signevent`-Methode. Ein Administrator kann damit das relay bitten, ein Event mit dem eigenen Pubkey des relays zu signieren. Der begleitende [PR #2390](https://github.com/nostr-protocol/nips/pull/2390) definiert ein Relay-Roles-Event: ein replaceable Event, das ein relay veröffentlicht, um seine Administratoren und Moderatoren zu deklarieren. Zusammen erlauben sie NIP-86-Clients, die Admin-Liste eines relays zu ermitteln und ohne Out-of-band-Vertrauen zu prüfen, ob eine authentifizierte Anfrage von einem aktuellen Admin stammt. Der Deep Dive weiter unten behandelt beide Änderungen.

### Gemergt: NIP-34 ersetzt `personal-fork` durch `u` für GRASP-06

[PR #2395](https://github.com/nostr-protocol/nips/pull/2395) wurde am 24. Juni gemergt und ersetzt auf Repo-State-Events (`kind:30618`) den `personal-fork`-Tag von [NIP-34](/de/topics/nip-34/) durch einen `u`-Tag für „upstream“. Damit entspricht das Wire-Format der GRASP-06-Fork-Semantik, die die GitWorkshop-Suite implementiert. Die Änderung schließt [PR #2384](https://github.com/nostr-protocol/nips/pull/2384) (`NIP-34: remove maintainers to solve expiry issues`), der eine andere Korrektur der Fork-Semantik vorgeschlagen hatte. Die gemergte Richtung wird von ngit v2.6.x implementiert; gemergte Spezifikation und Referenz-CLI stimmen nun überein. Bestehende Repos mit `personal-fork` bleiben interoperabel, neue Repos und die ngit-v2.6-Linie veröffentlichen den `u`-Tag.

### Gemergt: NIP-46-Client-Metadaten, nun upstream, nachdem Amber sie ausgeliefert hat

[PR #2381](https://github.com/nostr-protocol/nips/pull/2381) wurde am 23. Juni gemergt und ergänzt die [NIP-46](/de/topics/nip-46/)-`connect`-Anfrage um optionale Client-Metadaten. Ein Client kann beim Verbinden mit dem Signer seinen Namen, eine Icon-URL und eine Homepage-URL veröffentlichen. [Amber v6.2.2](https://github.com/greenart7c3/Amber/releases/tag/v6.2.2) lieferte die Metadaten-Erweiterung bereits vorige Woche aus, behandelt in [#28](/en/newsletters/2026-06-24-newsletter/#amber-v622-implements-nip-46-client-metadata); diese Woche zieht das Upstream-NIP mit der ausgelieferten Implementierung gleich.

### Offen: epoch-basierte deterministische NIP-17-Wrapper-Schlüssel

[PR #2397](https://github.com/nostr-protocol/nips/pull/2397) und [PR #2396](https://github.com/nostr-protocol/nips/pull/2396) behandeln zwei konvergierende Vorschläge für NIP-17-Wrap-Schlüssel. PR #2397 schlägt vor, den kurzlebigen Signierschlüssel, der einen [NIP-59](/de/topics/nip-59/)-Gift-Wrap verfasst, deterministisch aus einem an eine grobe Zeitepoche gebundenen Seed pro Conversation abzuleiten. Ein Empfänger, der den Conversation Key kennt, kann dann vorhersagen, welche Pubkeys er abonnieren muss. Die aktuelle Spezifikation verlangt einen neuen zufälligen Schlüssel pro Wrap und macht diese Vorhersage unmöglich. PR #2396 ist die begleitende Änderung: Wraps für eine bestimmte Conversation sollen direkt mit dem Conversation Key signiert werden, sodass der Wrap-Pubkey zugleich als Conversation-Identifier dient. Zusammen definieren sie einen Weg zu filterbaren NIP-17-Conversations ohne Metadatenleckage. Beide sind offen und werden diskutiert.

### Offen: NIP-59 soll Kind-13-Seal-Events am relay ablehnen

[PR #2399](https://github.com/nostr-protocol/nips/pull/2399) schlägt vor, dass relays Kind-13-Events, das innere Seal eines [NIP-59](/de/topics/nip-59/)-Gift-Wraps, ablehnen sollen, wenn sie auf oberster Ebene einer Publish-Anfrage erscheinen. Ein Seal-Event ist nur innerhalb eines Wraps sinnvoll, und ein geleaktes Seal legt den Pubkey des Empfängers offen. Das begleitende [Issue #2398](https://github.com/nostr-protocol/nips/issues/2398) geht weiter und argumentiert, das Seal solle als kurzlebiges Kind neu definiert werden. Kurzlebige Kinds nach NIP-01 werden von relays nicht gespeichert; damit würde die Regel auf Protokollebene gehärtet und nicht mehr von der Policy einzelner relays abhängen.

### Offen: NIP-29-Gruppenzustände

[PR #2372](https://github.com/nostr-protocol/nips/pull/2372) ergänzt [NIP-29](/de/topics/nip-29/) (relay-basierte Gruppen) um explizite Gruppenzustandssemantik. Er definiert, was offene, geschlossene, öffentliche, private oder archivierte Gruppen bedeuten und wie Zustandsübergänge mit Member-Events interagieren. Der Vorschlag überführt bisher Client-spezifische Semantik in die Relay-Spezifikation.

### Offen: optionale Multi-Maintainer-Unterstützung in NIP-34

[PR #2324](https://github.com/nostr-protocol/nips/pull/2324) ist der begleitende Vorschlag zum gemergten [PR #2395](https://github.com/nostr-protocol/nips/pull/2395), dessen GRASP-06-Fork-Semantik oben behandelt wurde. PR #2324 ergänzt die Repo-Announcement-Events (`kind:30617`) von [NIP-34](/de/topics/nip-34/) um optionale Multi-Maintainer-Unterstützung. Ein Repository kann über wiederholte `maintainer`-Tags mehrere maßgebliche Maintainer-Pubkeys deklarieren. Von jedem deklarierten Maintainer signierte Patches und Issues gelten Clients dann als offiziell. Das schließt die langjährige Lücke, durch die NIP-34-Repos mit Co-Maintainern entweder alles über einen Pubkey leiten oder auf Koordination außerhalb des Protokolls ausweichen müssen.

### Offen: NIP-91-AND-Operator für Filter, der Vorschlag ist offen, nicht gemergt

[PR #2252](https://github.com/nostr-protocol/nips/pull/2252) ist der Vorschlag für einen AND-Operator in Nostr-[Filtern](/de/topics/nip-01/) und greift ein Design wieder auf, das erstmals im älteren geschlossenen [PR #1365](https://github.com/nostr-protocol/nips/pull/1365) diskutiert wurde. Implementierungen existieren bereits in [nostr-rs-relay](https://github.com/v0l/nostr-rs-relay), applesauce, [Amethyst](https://github.com/vitorpamplona/amethyst) und worker-relay; der Spezifikations-PR selbst bleibt jedoch offen.

### Geschlossen: vier pats2sats-Commerce-NIPs

Vier Commerce-on-Nostr-Vorschläge wurden diese Woche geschlossen: Escrow ([#2334](https://github.com/nostr-protocol/nips/pull/2334)), Reservations ([#2335](https://github.com/nostr-protocol/nips/pull/2335)), eine [NIP-99](/de/topics/nip-99/)-Marketplace-Listing-Erweiterung ([#2346](https://github.com/nostr-protocol/nips/pull/2346)) und ein Accommodation-Listing-Profil ([#2333](https://github.com/nostr-protocol/nips/pull/2333)). Dieselbe Commerce-Oberfläche wird nun in der [Gamma Market Spec](https://github.com/GammaMarkets/market-spec) konsolidiert, einem projekteigenen Extension-Repository, das auf NIP-99-Marketplace-Listings mit Bestellungen, Checkout, Escrow und Streitbeilegungssemantik aufbaut. Compass verfolgt dieses Repository nun neben Marmot und Blossom als Protokoll-Spec-Repo außerhalb des NIPs-Repository. Offene PRs dort umfassen diese Woche eine Klarstellung zur Client-Attribution ([#11](https://github.com/GammaMarkets/market-spec/pull/11)), einen Supersedes-Tag für Änderungen der Produktidentität ([#8](https://github.com/GammaMarkets/market-spec/pull/8)) und Semantik für Händlerbewertungen ([#7](https://github.com/GammaMarkets/market-spec/pull/7)).

### Offen: Verknüpfung von Bitcoin-Identitäten

Zwei Vorschläge zum Verknüpfen von Bitcoin- mit Nostr-Identitäten wurden diese Woche eröffnet: eine [NIP-352-Bitcoin-Silent-Payment-Adresse](https://github.com/nostr-protocol/nips/pull/2392) und ein [Bitcoin-OTC-Identity-Linkage-Proof](https://github.com/nostr-protocol/nips/pull/2401).

---

## NIP Deep Dive: NIP-86 (Relay-Verwaltungs-API) {#nip-deep-dive-nip-86-relay-management-api}

[NIP-86](/de/topics/nip-86/) definiert eine JSON-RPC-Schnittstelle zur Relay-Verwaltung, über die autorisierte Clients administrative Befehle über eine standardisierte API an relays senden können. Ein einzelner Client kann jedes NIP-86-kompatible relay ohne Relay-spezifische Werkzeuge verwalten. Zwei Spezifikations-Merges dieser Woche ([PR #2389](https://github.com/nostr-protocol/nips/pull/2389) und [PR #2390](https://github.com/nostr-protocol/nips/pull/2390)) schließen den Kreis zwischen Relay-signierten Events und den von einem relay deklarierten Administratoren.

### Der Transport

Eine NIP-86-Verwaltungsanfrage ist ein HTTP POST an denselben URI, über den das relay WebSocket-Verbindungen bereitstellt, mit `Content-Type: application/nostr+json+rpc`. Der Request-Body ist ein JSON-Dokument der folgenden Form:

```json
{
  "method": "<method-name>",
  "params": [<arg1>, <arg2>, ...]
}
```

Die Authentifizierung verwendet ein signiertes [NIP-98](/de/topics/nip-98/)-HTTP-Auth-Event im `Authorization`-Header. Das relay prüft vor dem Ausführen der Methode, ob der signierende Pubkey auf seiner Administratorliste steht. Die Antwort des relays ist ein JSON-Dokument der folgenden Form:

```json
{
  "result": <return-value>,
  "error": "<error-string-if-any>"
}
```

### Die bereits vor dieser Woche vorhandenen Methoden

Die bestehende Methodenmenge umfasst Pubkey-Bans (`banpubkey`, `allowpubkey`, `listbannedpubkeys`), Event-Bans (`banevent`, `allowevent`, `listbannedevents`), Relay-Metadaten (`changerelayname`, `changerelaydescription`, `changerelayicon`), die Verwaltung der Allowed-Pubkey-Liste (`allowkind`, `disallowkind`, `listallowedkinds`) und eine `stats`-Methode, die Relay-Statistiken zurückgibt. Die Form ist bewusst nah an einem standardmäßigen JSON-RPC-Service, sodass ein Client typisierte Bindings darüberlegen kann.

### Was sich diese Woche geändert hat

[PR #2389](https://github.com/nostr-protocol/nips/pull/2389) ergänzt die Spezifikation um eine `signevent`-Methode. Sie übernimmt ein partielles Event-Template (Kind, Tags, Content) als Argument und bittet das relay, ein vollständiges Event mit dem eigenen Pubkey des relays im Feld `pubkey` zu signieren und zurückzugeben. Das ist die Voraussetzung dafür, dass ein relay Protokoll-Events über sich selbst veröffentlichen kann: Ankündigungen gesperrter Pubkeys, Relay-Metadaten und das neue Relay-Roles-Event weiter unten müssen alle mit dem vom Operator kontrollierten Schlüssel des relays signiert werden. Die meisten Relay-Operatoren wollen einen privaten Schlüssel jedoch nicht in ihrem administrativen Client halten.

[PR #2390](https://github.com/nostr-protocol/nips/pull/2390) definiert ein Relay-Roles-Event: ein parameterized replaceable Event-Kind, das ein relay veröffentlicht, mit dem eigenen Pubkey über `signevent` signiert, um die Pubkeys seiner Administratoren und Moderatoren mit expliziter Rollensemantik zu deklarieren. Ein NIP-86-fähiger Client kann das Relay-Roles-Event von jedem erfassten relay abrufen, die Admin-Liste aus den Event-Tags erstellen und ohne Out-of-band-Vertrauen oder Relay-spezifische Konfiguration prüfen, ob eine authentifizierte NIP-86-Anfrage von einem aktuellen Admin stammt. Zusammen schließen die beiden PRs den Kreis: `signevent` ist der Mechanismus, Relay Roles das erste darauf aufbauende Event-Kind.

### Beispiel einer NIP-86-Anfrage

Eine vollständige NIP-86-`banpubkey`-Anfrage sieht so aus:

```json
{
  "method": "banpubkey",
  "params": [
    "<64-char-hex-pubkey-to-ban>",
    "spam"
  ]
}
```

mit einem `Authorization`-Header, der ein signiertes NIP-98-Event trägt:

```json
{
  "id": "5e1c2f9e1d3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c",
  "pubkey": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
  "created_at": 1782824400,
  "kind": 27235,
  "tags": [
    ["u", "https://relay.example.com/"],
    ["method", "POST"],
    ["payload", "<sha256-of-request-body>"]
  ],
  "content": "",
  "sig": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100"
}
```

Der signierende Pubkey muss in der Admin-Menge des relays enthalten sein, die nun im Relay-Roles-Event deklariert wird. Der `u`-Tag muss mit der HTTPS-URL des relays übereinstimmen; der `payload`-Tag muss dem SHA-256 des JSON-Request-Bodys entsprechen. Das relay gibt zurück:

```json
{
  "result": true,
  "error": null
}
```

### Implementierungen

- [Amethyst](https://github.com/vitorpamplona/amethyst) liefert eine NIP-86-Oberfläche zur Relay-Verwaltung auf Android (v1.07.0+).
- Zu den Referenz-relays, die die Spezifikation implementieren, gehören [strfry](https://github.com/hoytech/strfry), [khatru](https://github.com/fiatjaf/khatru) und mehrere kleinere Implementierungen, auf die die Spezifikation im Abschnitt `Implementation Status` verweist.

NIP-86-fähige Clients werden das Relay-Roles-Event als maßgebliche Quelle für die Admin-Liste eines relays behandeln, sobald Implementierer die Änderungen an `signevent` und Relay Roles übernehmen.

---

## NIP Deep Dive: NIP-89 (Empfohlene Application Handler) {#nip-deep-dive-nip-89-recommended-application-handlers}

[NIP-89](/de/topics/nip-89/) definiert zwei parameterized replaceable Event-Kinds: `kind:31990`, den von einem App-Entwickler veröffentlichten Application Handler, und `kind:31989`, die Empfehlung eines Nutzers für eine verwendete App. Zusammen ermöglichen sie Clients, Anwendungen für ein unbekanntes Event-Kind ohne Out-of-band-Koordination zu finden. Ein Langform-Reader, der auf ein `kind:30030`-Event trifft, das er nicht nativ behandelt, kann den NIP-89-Graph nach Handlern abfragen und dem Nutzer einen „Öffnen in ...“-Ablauf zu einer veröffentlichten App anbieten. NIP-89 ist die ursprüngliche Infrastruktur für dasselbe Cross-App-Routing-Problem, das die in dieser Ausgabe auftauchende napplet-/napps-Arbeit nun auf zusammensetzbare Nostr-native Applets erweitert.

### Das Application-Handler-Event (`kind:31990`)

Ein App-Entwickler veröffentlicht ein oder mehrere Handler-Events, die beschreiben, welche Event-Kinds die App unterstützt und wie eine Nostr-Entität in der App geöffnet wird:

```json
{
  "id": "8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b",
  "pubkey": "c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2",
  "created_at": 1782824400,
  "kind": 31990,
  "tags": [
    ["d", "longform-reader-v1"],
    ["k", "30023"],
    ["k", "30024"],
    ["web", "https://reader.example.com/a/<bech32>", "naddr"],
    ["ios", "longformreader://open/<bech32>"],
    ["android", "longformreader://open/<bech32>"]
  ],
  "content": "{\"name\": \"Longform Reader\", \"picture\": \"https://reader.example.com/icon.png\", \"about\": \"A native reader for NIP-23 longform.\"}",
  "sig": "1f2e3d4c5b6a798877665544332211000ffeeddccbbaa99887766554433221100ffeeddccbbaa99887766554433221100ffeeddccbbaa9988776655443322110a"
}
```

Der `d`-Tag identifiziert den Handler, sodass er ersetzt werden kann. Jeder `k`-Tag deklariert ein Event-Kind, das die App verarbeitet, und jeder Plattform-Tag (`web`, `ios`, `android`, ...) liefert ein URL-Template mit `<bech32>` als Platzhalter für eine [NIP-19](/de/topics/nip-19/)-kodierte Entität, die der aufrufende Client beim Öffnen einsetzt. Ein Handler-Event kann mehrere unterstützte Kinds bewerben, wenn sie dasselbe Routing-Muster teilen. Das hält App-Discovery kompakt und vermeidet ein Handler-Event pro Kind.

### Das Empfehlungsevent des Nutzers (`kind:31989`)

Ein Nutzer veröffentlicht eine Empfehlung, die angibt, welche Apps er für ein bestimmtes Event-Kind verwendet:

```json
{
  "id": "9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d",
  "pubkey": "d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3",
  "created_at": 1782824500,
  "kind": 31989,
  "tags": [
    ["d", "30023"],
    ["a", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com", "web"],
    ["a", "31990:e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6:reader-pro", "wss://relay.example.com", "ios"]
  ],
  "content": "",
  "sig": "2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6"
}
```

Der `d`-Tag trägt das empfohlene Event-Kind. Jeder `a`-Tag ist ein NIP-01-Adresszeiger auf ein `kind:31990`-Handler-Event, zusammen mit dem vorgeschlagenen relay und der Plattform, für die die Empfehlung gilt. Dieselbe Empfehlung kann mehrere Apps für verschiedene Plattformen auflisten.

### Der Client-Tag und der Datenschutz-Tradeoff

NIP-89 definiert außerdem einen optionalen `client`-Tag, den jede veröffentlichende App an von ihr verfasste Events anhängen kann:

```
["client", "Longform Reader", "31990:c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2:longform-reader-v1", "wss://relay.example.com"]
```

Damit kann jeder Client, der das Event anzeigt, die Herkunfts-App nennen, reichhaltigere Handler-Metadaten abrufen und vom Handler deklarierte Rendering-Hinweise beachten. Die Spezifikation weist ausdrücklich auch auf die Datenschutzkosten hin: Ein Client, der jedem Event einen `client`-Tag mitgibt, veröffentlicht die Softwareidentität des Nutzers und legt mit der Zeit Nutzungsmuster offen. Die Spezifikation empfiehlt Clients, Nutzern einen Opt-out anzubieten.

Amethysts [PR #3422](https://github.com/vitorpamplona/amethyst/pull/3422) parst und zeigt NIP-89-`t`-, `i`-, `a`- und `client`-Tags in der Event-Anzeige und macht direkt in der Timeline sichtbar, welche App eine Notiz verfasst hat.

### So läuft der Discovery-Flow in der Praxis

Ein Client, der ein unbekanntes Event-Kind empfängt, geht wie folgt vor. (1) Er fragt im Follow-Graph des Nutzers nach `kind:31989`-Events mit einem `d`-Tag, der dem Event-Kind entspricht. (2) Er löst jeden empfohlenen `a`-Tag zum zugehörigen `kind:31990`-Handler-Event auf. (3) Er wählt den Handler, dessen `web`-, `ios`- oder `android`-URL-Template zur aktuellen Plattform passt. (4) Er setzt die `bech32`-Kodierung der Entität in das URL-Template ein. (5) Er bietet dem Nutzer die resultierende URL als „Öffnen in ...“-Option an. Der Ablauf ist sozial gefiltert: Fragt ein Client beliebige Handler-Events von nicht vertrauenswürdigen relays ab, könnte er Nutzer zu schädlichen Apps umleiten. Bei Personen zu beginnen, denen der Nutzer folgt, ist daher ein sichererer Standard, als jeden veröffentlichten Handler als gleich vertrauenswürdig zu behandeln.

### NIP-89 und die napplet-Schicht

Amethysts Discover-Bereich, die napplet-Host-Runtime und die Anzeige von `client`-Tags bilden zusammen eine vollständige NIP-89-Consumer-Oberfläche auf Android. Die in der vorigen Ausgabe gestartete napplet-Spezifikation erweitert die Ziele dieser NIP-89-Handler-Events: sandboxed Applets, die eine zusammensetzbare Nostr-native Runtime über Nostr und Blossom ausführen. NIP-89 ist der Discovery- und Routing-Graph; die napplet-Runtime ist ein Ausführungsziel, auf das er zeigen kann.

---

*Feedback, Korrekturen und übersehene Projekte: Eröffnet ein Issue auf [github.com/andotherstuff/nostr-compass](https://github.com/andotherstuff/nostr-compass) oder erreicht uns per NIP-17-DM unter npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923.*
