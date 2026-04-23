---
title: 'Nostr Compass #18'
date: 2026-04-15
translationOf: /en/newsletters/2026-04-15-newsletter.md
translationDate: 2026-04-22
draft: false
type: newsletters
---

Nostr Compassへようこそ。Nostrの週刊ガイドです。

**今週の内容:** [Amethyst](https://github.com/vitorpamplona/amethyst)は、[NIP-AC](/ja/topics/nip-ac/)の音声通話とビデオ通話、[Marmot](/ja/topics/marmot/)向けのRFC 9420準拠、desktop Tor対応、custom C secp256k1、multi-wallet [NIP-47](/ja/topics/nip-47/)を含む大規模な更新を進めました。[nstrfy](https://github.com/vcavallo/nstrfy-android)は、kind `7741`イベントを使ってFirebaseをNostr relayで置き換えるAndroid向けpush通知appとして登場しました。[HAMSTR](https://github.com/LibertyFarmer/hamstr)はReticulumを追加し、LoRa mesh上でインターネットなしにNostrイベントを流せるようにしました。[Bloom](https://github.com/nostrnative/bloom)は、self-hostedな[Blossom](/ja/topics/blossom/) media serverとNostr relayを束ねたdesktop appとしてv0.1.0を出荷しました。[WaveFunc](https://github.com/zeSchlausKwab/wavefunc)は、Nostrベースのinternet radio directory兼playerとしてv0.1.0を開始しました。[Botburrow](https://github.com/marmot-protocol/botburrow)は、[Marmot](/ja/topics/marmot/)暗号化group chat向けself-hosted bot platformとして開発を始めました。[Snort](https://github.com/v0l/snort)は、security audit、batched WASM verification、message systemの再設計を含むv0.5.0からv0.5.3を出荷しました。

## Top Stories

### Amethyst merges desktop Tor, C secp256k1, WebRTC calls, and multi-wallet NWC

[Amethyst](https://github.com/vitorpamplona/amethyst)は、今週だけで29本のPRをマージし、cryptography、networking、calling、wallet infrastructureにまたがる大きな前進を見せました。[PR #2381](https://github.com/vitorpamplona/amethyst/pull/2381)は、kmp-tor daemonを埋め込んだfail-closed設計でdesktop Tor supportを追加し、Torが起動できない場合はrelay接続自体を拒否します。これによりAndroid版とdesktop版のprivacy routingがそろい、Tor統合には130件超のunit testが付きました。

[PR #2374](https://github.com/vitorpamplona/amethyst/pull/2374)は、JNI binding付きのcustom C secp256k1実装を追加し、Schnorr signature verificationを従来のpure Kotlin経路より2倍から3倍高速化しました。GLV decomposition、wNAF point encoding、x86_64とARM64向けのhardware-accelerated SHA-256が使われています。関連PRである[PR #2188](https://github.com/vitorpamplona/amethyst/pull/2188)、[PR #2195](https://github.com/vitorpamplona/amethyst/pull/2195)、[PR #2204](https://github.com/vitorpamplona/amethyst/pull/2204)では、fused multiply-reduce、field element保存用のFe4 struct、platform-specific intrinsicsも入り、Androidでさらに約28%の改善が見込まれています。

[PR #2202](https://github.com/vitorpamplona/amethyst/pull/2202)は、pure KotlinのMLS実装をRFC 9420へ合わせ、reuse guard、AAD、ciphertext sample derivation、commit処理修正、thread safetyを追加しました。これは[Marmot](/ja/topics/marmot/)統合に向けたもので、先週のKotlin MLS作業の続きを受けて[Quartz](/ja/topics/quartz/)を完全なMLS準拠へ近づけます。加えて、[PR #2203](https://github.com/vitorpamplona/amethyst/pull/2203)から[PR #2211](https://github.com/vitorpamplona/amethyst/pull/2211)にかけては、[NIP-AC](/ja/topics/nip-ac/)向けの完全なWebRTC音声通話・ビデオ通話stackが入りました。ICE restart、runtime camera switching、自動再接続、resolutionとbitrate設定、TURN server選択、Android 14以降のforeground service制約対応、call state machineのthread safetyまで含まれます。

wallet側では、[PR #1988](https://github.com/vitorpamplona/amethyst/pull/1988)がmulti-wallet [NIP-47](/ja/topics/nip-47/) supportを追加し、1つのaccountに複数NWC walletを接続し、個別のbalance cardを見て、default walletを選び、旧single-wallet設定から移行できるようにしました。[PR #2189](https://github.com/vitorpamplona/amethyst/pull/2189)はGIF-to-MP4変換も追加し、3MBのGIFを約159KBのMP4へ圧縮できます。同じ週には、post composer向けAI tone suggestionと自動言語検出も入りました。

### nstrfy launches Nostr-native push notifications for Android

[nstrfy](https://github.com/vcavallo/nstrfy-android)は4月13日に公開され、[v1.0.0](https://github.com/vcavallo/nstrfy-android/releases/tag/v1.0.0)から[v1.2.0](https://github.com/vcavallo/nstrfy-android/releases/tag/v1.2.0)まで3リリースを出しました。このappはntfy-androidのforkで、HTTP transportをNostrへ置き換えています。serverをpollしてpush通知を待つ代わりに、configurable relay上のkind `7741`イベントへsubscribeし、それをnative Android notificationとして表示します。

通知モデルは平文payloadと[NIP-44](/ja/topics/nip-44/)暗号化payloadの両方をサポートします。暗号化時には、[Amber](https://github.com/greenart7c3/Amber)を使って[NIP-55](/ja/topics/nip-55/)経由で署名するか、local nsecを使います。topic単位のsubscriptionでは送信者allowlistを設定でき、npub whitelistに入った相手だけがそのtopicの通知を発火できます。relay listは[NIP-65](/ja/topics/nip-65/)を通じてprofileから取り込み、[NIP-40](/ja/topics/nip-40/)のevent expirationにも従います。tap-to-open URL、priority level、custom icon、action buttonなど、ntfyの通知語彙もそのまま多くが使えます。user searchはbrainstorm.worldの[Web of Trust](/ja/topics/web-of-trust/) dataを使うNIP-50で動いています。

[nstrfy.sh](https://github.com/vcavallo/nstrfy.sh)のcompanion projectは、bash CLIと、browserから送受信できる[nstrfy.sh](https://nstrfy.sh)のhosted web clientの両方を提供し、NIP-07 signer supportも持ちます。native appは[Zapstore](https://zapstore.dev/apps/io.nstrfy.android)で配布されています。

### HAMSTR adds Reticulum for Nostr over LoRa mesh

[HAMSTR](https://github.com/LibertyFarmer/hamstr)は、ham radio経由でNostrイベントとLightning zapsを送るプロジェクトで、4月12日に[PR #10](https://github.com/LibertyFarmer/hamstr/pull/10)をマージし、transport backendとして[Reticulum](https://reticulum.network/) mesh networkingを追加しました。Reticulumは、LoRa、HF、VHF/UHF radio、serial link、TCP/IP上で動くcryptographic mesh protocolです。これによりHAMSTRは、インターネット基盤をまったく使わず、RNode hardware deviceのmesh上でNostrイベントをrelayできるようになります。

既存のAX.25 Packet RadioとVARA HF transportも引き続き利用でき、operatorは自分の構成に合うradio linkを選べます。HAMSTRのzero-knowledge server architectureではrelayが秘密鍵を見ず、[NIP-57](/ja/topics/nip-57/) zap準拠によりoffline Lightning zapsもAmethystやPrimalのようなclientに正しく現れます。Reticulum transportのsetup guideは[RETICULUM.MD](https://github.com/LibertyFarmer/hamstr/blob/master/RETICULUM.MD)にあり、同週の[PR #11](https://github.com/LibertyFarmer/hamstr/pull/11)ではfrontendがSvelte 5とTailwindCSS v4へ移行しました。

## Shipping This Week

### Bloom v0.1.0 ships self-hosted Blossom server and relay

[Bloom](https://github.com/nostrnative/bloom)は4月9日に初リリース[v0.1.0](https://github.com/nostrnative/bloom/releases/tag/v0.1.0)を出しました。Tauri v2（Rust backend）とReact 19で構築されており、完全な[Blossom](/ja/topics/blossom/) protocol media serverとNostr relayを1つのdesktop applicationへ束ねています。ユーザーは、server infrastructureを自分で管理しなくても、SHA-256 content addressing、[NIP-94](/ja/topics/nip-94/) file metadata対応、`blossom://` URI解決を備えたsovereign file storageを得られます。リリースには16本のplatform-specific binary assetが含まれています。

### WaveFunc v0.1.0 and v0.1.1 launch Nostr internet radio

[WaveFunc](https://github.com/zeSchlausKwab/wavefunc)は4月13日に[v0.1.0](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.0)と[v0.1.1](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.1)を出し、Nostrベースのinternet radio directory兼playerとして始動しました。独自event kindがdata modelを定義し、radio station listingにkind `31237`、favorites listにkind `30078`、live chatにkind `1311`、station commentにkind `1111`を使います。relay backendにはKhatruが使われ、SQLite storageとBluge full-text searchで[NIP-50](/ja/topics/nip-50/)を支えます。

WaveFuncは[NIP-60](/ja/topics/nip-60/) Cashu walletとnutzap supportも備え、NDKからapplesauce-coreへ移行しました。[v0.1.1](https://github.com/zeSchlausKwab/wavefunc/releases/tag/v0.1.1)ではgenre carousel、Lightning donation popover、認証済みユーザー向けstation management、Zapstore listingが追加されました。Tauri v2のdesktop buildにはsystem tray integration、media key support、autostart、deep linkingも入り、buildはmacOS、Windows、Linux、Android向けに[wavefunc.live](https://wavefunc.live)から入手できます。

### Snort ships v0.5.0 through v0.5.3 with security hardening and performance overhaul

[Snort](https://github.com/v0l/snort)は、ReactベースのNostr web clientで、[v0.5.0](https://github.com/v0l/snort/releases/tag/v0.5.0)から[v0.5.3](https://github.com/v0l/snort/releases/tag/v0.5.3)まで3リリースを出しました。中心となるv0.5.0は、実Schnorr signature verification、偽造relay messageに対する[NIP-46](/ja/topics/nip-46/)保護、PIN encryption改善、未検証[NIP-26](https://github.com/nostr-protocol/nips/blob/master/26.md) delegation trustの削除を含む包括的なsecurity audit対応です。性能面では、batched WASM signature verification、lazy-loaded route、priority profile loaderの再設計、worker-relay最適化が入りました。加えて、[NIP-90](/ja/topics/nip-90/) DVM向けkind `7000` payment-required invoice表示も追加されています。[PR #620](https://github.com/v0l/snort/pull/620)はmessage systemも再設計し、gift wrapをworker relayへ永続化しつつ、O(n²)だったchat list計算をsingle-passのMapベースへ置き換えました。

### Primal Android ships 3.0.21 and redesigns feed layout

[Primal Android](https://github.com/PrimalHQ/primal-android-app)は[v3.0.21](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.21)を出し、poll zap vote、wallet multi-account sharing、remote signerとwallet serviceのauto-reconnectまわりのbug fixを行いました。その後も7本のPRが入り、[PR #1008](https://github.com/PrimalHQ/primal-android-app/pull/1008)がmain screen layoutを統一し、[PR #1010](https://github.com/PrimalHQ/primal-android-app/pull/1010)が大きいavatarとindent付きcontentを備えた新feed card designを導入し、[PR #1009](https://github.com/PrimalHQ/primal-android-app/pull/1009)がmedia feed cardにvideo supportとportrait layoutを加え、[PR #1012](https://github.com/PrimalHQ/primal-android-app/pull/1012)がquick reply用compact text fieldを追加し、[PR #1013](https://github.com/PrimalHQ/primal-android-app/pull/1013)がapp barを再設計しました。

### Nostria v3.1.19 through v3.1.21 add local AI image generation

[Nostria](https://github.com/nostria-app/nostria)は[v3.1.19](https://github.com/nostria-app/nostria/releases/tag/v3.1.19)から[v3.1.21](https://github.com/nostria-app/nostria/releases/tag/v3.1.21)まで3リリースを出し、80件超のcommitを積みました。中心となる新機能は、WebGPU acceleration付きJanus Proを使うlocal image generationで、ユーザーは外部APIなしに端末上で画像を生成できます。加えてcloud image generation、multimodal chat、ONNX runtime support、AI prompt library、AI cache managementも入りました。client面では、新しいdialog system、note editorの見直し、music embed改善、signer login flow変更も含まれています。[Newsletter #17](/ja/newsletters/2026-04-08-newsletter/)では、v3.1.18までのnative mobile releaseを扱いました。

### TubeStr v1.0.3 ships feed and studio updates

[TubeStr](https://github.com/Tubestr/tubestr-v2)は、Nostr上に構築されたprivate family video sharing appで、4月13日に[v1.0.3](https://github.com/Tubestr/tubestr-v2/releases/tag/v1.0.3)を出しました。このリリースはfeedとstudioの改善が中心です。[PR #3](https://github.com/Tubestr/tubestr-v2/pull/3)はonboarding screenを刷新し、[PR #2](https://github.com/Tubestr/tubestr-v2/pull/2)はvideo export errorを修正しました。アプリはfamily member間の暗号化media sharingにNDKとMDK（[Marmot](/ja/topics/marmot/) Development Kit）を使っており、media storageには[Blossom](/ja/topics/blossom/)統合が予定されています。TubeStrは[Zapstore](https://zapstore.dev)で利用できます。

## In Development

### Botburrow begins development as Marmot bot platform

[Botburrow](https://github.com/marmot-protocol/botburrow)はMarmot teamの新プロジェクトで、4月3日に始まりました。これはself-hostedなbot management platformで、各botが独自のNostr identityを持ち、Welcome message経由で[Marmot](/ja/topics/marmot/)のMLS-encrypted group chatへ参加し、end-to-end encrypted messageを送受信します。dashboardはRails 8.1で構築され、単一のwhitenoise-rs daemon（`wnd`）とUnix socketで通信します。

Botburrowは、command、trigger、scheduled actionがcustom Ruby codeを実行できるscripting layerを備え、scriptは`wnd`経由でprofile、group membership、pending inviteを参照でき、dashboardには実group内のbotへ送受信できるlive chat viewもあり、各botはconfig、cache、生成output向けの個別file storageを持ちます。[Docker image](https://github.com/marmot-protocol/botburrow/commit/2ed012078eaab3c5b92dff16b87865c2e353bd80)はmulti-arch buildでUmbrelとStart9向けzero-config self-hostingを目指しており、READMEには[trust model section](https://github.com/marmot-protocol/botburrow/commit/c8ef8c306af247560b1952878206d854cde3fe20)も追加されました。

### Nostr Archives adds trending feeds relay and entity resolution

[Nostr Archives](https://github.com/barrydeen/nostrarchives-api)は、[nostrarchives.com](https://nostrarchives.com)で動くNostr archival and analytics platformで、Rust製[API](https://github.com/barrydeen/nostrarchives-api)とNext.js 16製[frontend](https://github.com/barrydeen/nostrarchives-frontend)の両方で開発が続いています。API側では[PR #118](https://github.com/barrydeen/nostrarchives-api/pull/118)がclient leaderboardへtime-range filteringを追加し、[PR #117](https://github.com/barrydeen/nostrarchives-api/pull/117)がreply eventへengagement counterを追加しました。frontend側では[PR #85](https://github.com/barrydeen/nostrarchives-frontend/pull/85)がURL pathからNostr entityを直接解決し、[PR #86](https://github.com/barrydeen/nostrarchives-frontend/pull/86)がAPI documentation pageを追加しました。platformはNIP-50 search relay、trending feeds relay、future-dated event用scheduler relay、kinds 0、3、10002向けindexer relayの4つを運用しています。

### Damus fixes favorites timeline

[Damus](https://github.com/damus-io/damus)は、iOS clientで、[PR #3708](https://github.com/damus-io/damus/pull/3708)をマージし、`subscribe_to_favorites()`関数をin-place filtering、deduplication rebuilding、persisted tab selection付きで書き直しました。

### Nostur adds private zaps and custom emoji viewing

[Nostur](https://github.com/nostur-com/nostur-ios-public)は今週10 commitを積み、private zap support、custom emoji viewing、animated `.webp` rendering修正、voice messageのaudio format detectionを追加しました。

### Amber ships v6.0.1 through v6.0.3 with WebDAV backup and relay reconnection fixes

[Amber](https://github.com/greenart7c3/Amber)は、Android向け[NIP-55](/ja/topics/nip-55/) signer appで、今週3リリースを出しました。[v6.0.1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.1)ではWebDAVとGoogle Drive共有の2つのbackup optionを追加し、relay reconnectionにexponential backoffを実装し、Quartz libraryを1.08.0へ更新し、app update eventとprofile eventのvalidationを修正しました。[v6.0.2](https://github.com/greenart7c3/Amber/releases/tag/v6.0.2)はseed word使用時のaccount index optionを追加し、起動時にrelayがofflineでもreconnectionできるようにし、[v6.0.3](https://github.com/greenart7c3/Amber/releases/tag/v6.0.3)はintent受信時の空request IDをさらに修正しました。

### Plektos v0.6.0 redesigns with Ditto themes

[Plektos](https://github.com/derekross/plektos)は、interactive mapを備えた[NIP-52](/ja/topics/nip-52/)ベースのdecentralized meetup and events platformで、4月14日に[v0.6.0](https://github.com/derekross/plektos/commit/7a691cdf089ceb7a8582dd5c0ee026830f2cdc77)と[v0.6.1](https://github.com/derekross/plektos/commit/3a6474ae380522d8ee1b3526423fcfc3328fd879)を出しました。この更新では、Ditto風community theme、custom background image upload、avatar shape設定、UI overhaulが入りました。[PR #6](https://github.com/derekross/plektos/pull/6)はsecurity、architecture、UXを含むfull code reviewを反映しています。Plektosはprotocol統合にNostrify、remote loginに[NIP-46](/ja/topics/nip-46/)、ticket paymentにzapsを使い、Android buildはZapstoreで利用できます。

### Shadow adds Nostr OS API and Cashu wallet app

[Shadow](https://github.com/justinmoon/shadow)はJustin Moonのapp runtime platformで、2日で30超のcommitを積みました。[Commit 88cbda5](https://github.com/justinmoon/shadow/commit/88cbda5131814d2730a2d892029932136db005df)はruntime内で動くCashu wallet appを追加し、[Commit 865c415](https://github.com/justinmoon/shadow/commit/865c415)はpodcast player demoを追加しました。runtimeは`Shadow.os.nostr`と`Shadow.os.audio`をOS-level APIとして公開し、Pixel runtime laneではroot化Android device上でWayland compositorとGPU compositingが動きます。[PR #1](https://github.com/justinmoon/shadow/pull/1)と[PR #2](https://github.com/justinmoon/shadow/pull/2)はdesktop Linuxのfont loadingとXDG state directory handlingを修正しました。正式releaseはまだありません。

### Lief fixes Amber login and adds Zapstore

[Lief](https://gitlab.com/chad.curtis/lief)は、他のNostrユーザーへlong-form letterを作成・送信するNostr appで、4月12日にbuild `v2026.04.12`を出しました。この更新ではAndroid上の[Amber](https://github.com/greenart7c3/Amber) signer login issueを修正し、signer nudge flowを単純化し、nostrify依存を更新し、Zapstore integrationを追加しました。

### Espy overhauls color picker and fixes Amber login

[Espy](https://gitlab.com/chad.curtis/espy)は、現実世界の場面から3から6色のpaletteを共有するNostr social appで、4月12日にbuild `v2026.04.12`を出しました。更新では、grayscale toggleに代えてcurved saturation arcを持つcolor picker overhaulが入り、hue ring flicker bugが修正され、AlchemistとAstrologerというEaster egg characterも追加されました。PNG assetは703KB削減され、[Amber](https://github.com/greenart7c3/Amber) login fix、signer nudge flow簡略化、nostrify依存更新、Zapstore integrationも含まれています。

### Jumble adds per-feed kind filters and articles tab

[Jumble](https://github.com/CodyTseng/jumble)は今週13 commitを積み、feedごとのkind filtering、Articles tab、privacy-preserving option付きnotification read status sync、avatar hide mode、account switchingのrace condition fixを追加しました。

### Primal Web ships 8 version bumps

[Primal Web](https://github.com/PrimalHQ/primal-web-app)は1週間で3.0.93から3.0.101までのversion bumpを行い、21 commitを積みました。作業は主に、live stream chat改善、mention境界修正、bookmark pagination、duplicate like防止、relay proxy修正に集中しています。

## Protocol and Spec Work

### NIP Updates

[NIPs repository](https://github.com/nostr-protocol/nips)への最近の変更です。

**Merged:**

- **[NIP-34](/ja/topics/nip-34/)（Git Stuff）: Add `nostr://` clone URLs**（[PR #2312](https://github.com/nostr-protocol/nips/pull/2312)）：[NIP-34](/ja/topics/nip-34/)は、kind `30617`のrepository announcementを使ってgit repositoryをNostr上でホストする方法を定義します。今回のPRは、`git-remote-nostr` helperで使える`nostr://` clone URL formatを追加し、`nostr://<naddr>`、`nostr://<npub|nip05>/<identifier>`、`nostr://<npub|nip05>/<relay-hint>/<identifier>`の3形式を定義します。relay hintとidentifierはRFC 3986に従ってpercent-encodeされ、Shakespeare、ngit、GitWorkshop.dev、NostrHub.ioですでに使われています。

**Open PRs and Discussions:**

- **NIP-63a: Minimal Payment Gateway Descriptor**（[PR #2315](https://github.com/nostr-protocol/nips/pull/2315)）：creatorが有料content access向けのpayment gateway、pricing model、subscription ruleを宣言するkind `10164` replaceable eventを提案します。clientごとの独自payment flowではなく、1つのイベントから受け入れpayment methodやpricing tierをdiscoverできるようにするものです。
- **NIP-XX: Relay Self-Declaration Manifest and Retention Horizon**（[PR #2314](https://github.com/nostr-protocol/nips/pull/2314)）：relay operatorがendpoint、retention window、write policy、supported NIPsを宣言するkind `10100`イベントと、relayが`EOSE`前に最古保持timestampを返す`HORIZON` messageを提案します。HTTP-onlyだったNIP-11の配布失敗を補い、relayの時間的境界を明示する狙いです。
- **NIP-TPLD: Transient Private Location Data**（[PR #2309](https://github.com/nostr-protocol/nips/pull/2309)）：kind `20411`のephemeral rangeを使い、特定受信者だけが復号できる位置情報共有を提案します。contentには受信者pubkeyごとの[NIP-44](/ja/topics/nip-44/)暗号payloadが入り、`ttl`タグで推奨保持期間を示します。
- **[NIP-5C](/ja/topics/nip-5c/)（Scrolls）: WASM programs update**（[PR #2281](https://github.com/nostr-protocol/nips/pull/2281)）：WebAssembly program publishingとexecution specの作業が続いています。clientがrelayからWASM binaryを取得してsandbox内で実行できる「scrolls」のevent formatとruntime interfaceを更新するもので、[demo app](https://nprogram.netlify.app/)もあります。
- **[NIP-44](/ja/topics/nip-44/) large payload support**（[PR #1907](https://github.com/nostr-protocol/nips/pull/1907)）：現在65,535バイトの上限を超えるpayloadをNIP-44で扱うための後方互換な拡張を提案します。大きなkind `3` contact listをremote signingする[NIP-46](/ja/topics/nip-46/)用途が主な動機です。
- **[NIP-C7](/ja/topics/nip-c7/): Restrict kind 9 to chat views**（[PR #2310](https://github.com/nostr-protocol/nips/pull/2310)）：kind `9`をchat-oriented viewに限定し、general feedで文脈を失ったchat messageが混ざらないようにする提案です。kind `1`やkind `30023`のような他contentはkind `9` message内で参照すべきだと整理します。

## NIP Deep Dive: NIP-29 (Relay-based Groups)

[NIP-29](https://github.com/nostr-protocol/nips/blob/master/29.md)は、relay自体がgroup membershipとmoderationを管理するgroup messaging modelを定義します。groupは特定relay上に存在し、relayが誰に書き込み権があるかを決めます。これは、client-side MLS encryptionを使う[Marmot](/ja/topics/marmot/)や、gift-wrapped DMベースの[NIP-17](/ja/topics/nip-17/) group chatとは異なる設計で、relay operatorがmessageを読め、moderationもrelayレベルで行われます。

groupは`<host>'<group-id>`形式で識別されます。例えば`groups.nostr.com'abcdef`のような形です。特別なgroup ID `_`はrelay-wide discussion向けtop-level groupとして予約されています。groupへ送るユーザーイベントは、group IDを持つ`h`タグを必ず含みます。`previous`タグはtamper detection用で、clientは直近50 message内で見た同じrelayのイベントhash先頭8文字を含め、relayは存在しない`previous`を参照するイベントを拒否します。これによりforkされたrelayへ文脈外でmessageを再送することが難しくなります。

membershipはkind `9000-9020`範囲のmoderation eventで管理されます。ユーザーはkind `9021`のjoin requestを送り、relayのpolicyに応じて受理または拒否されます。adminはkind `9000`でuser追加、kind `9001`で削除、kind `9002`でmetadata編集、kind `9005`でevent削除、kind `9009`でinvite code作成ができます。relayはkind `39000`でmetadata、kind `39001`でadmin list、kind `39002`でmember list、kind `39003`でroleとcapabilityを公開します。groupはpublic、closed、fully openなどさまざまに設定でき、visibilityとwrite-accessは独立しています。

重要なのは、NIP-29がchat message以外もgroup文脈へ入れられることです。long-form article（[NIP-23](/ja/topics/nip-23/)）、calendar event（[NIP-52](/ja/topics/nip-52/)）、live stream（[NIP-53](/ja/topics/nip-53/)）、market listingなども`h`タグを持ってgroup内へ入れられます。実装面では[Flotilla](https://gitea.coracle.social/coracle/flotilla)が最も活発で、[Coracle](https://github.com/coracle-social/coracle)も対応しており、reference implementationとして[groups.fiatjaf.com](https://github.com/fiatjaf/relay29)があります。relay operatorがcontentを読めるという明確なトレードオフがある一方、公開communityや開発者channelのような用途では、この単純さが利点になります。relayがcontentを読めないprivate messagingが必要なら、NIP-17かMarmotのほうが適しています。

## NIP Deep Dive: NIP-90 (Data Vending Machines)

[NIP-90](https://github.com/nostr-protocol/nips/blob/master/90.md)は、Nostr上でon-demand computationを行うためのプロトコルです。customerがjob requestを公開し、service providerがそれを処理して結果をNostr eventとして返します。仕様自身が言うように、これは「money in, data out」の市場であり、customerは誰が処理したかより出力そのものを重視します。

プロトコルは、job requestに`5000-5999`、job resultに`6000-6999`、feedbackにkind `7000`を割り当てます。result kindはrequest kindより常に1000大きくなります。requestには入力を示す`i`タグ、期待する形式を示す`output`タグ、最大支払いを示す`bid`、job固有設定を入れる`param`タグが含まれます。providerはresultで元requestを参照し、必要ならLightning invoiceを`amount`タグで返せます。kind `7000`のfeedback eventにより、`payment-required`、`processing`、`error`、`success`のような進捗通知も送れます。

NIP-90はjob chainingもサポートし、あるjobの出力を次のjobの入力へ渡せます。これにより、音声のtranscription、要約、翻訳を別providerで順につなぐようなpipelineが可能になります。privacyが必要な場合、customerは`i`や`param`を[NIP-04](/ja/topics/nip-04/)で暗号化し、`encrypted`タグ付きで`content`へ入れられます。その代わり、この場合は特定providerを事前に選ぶ必要があります。provider discoveryには[NIP-89](/ja/topics/nip-89/)が使われ、Snortのkind `7000` invoice表示やnoStrudelのDVM explorerなど、周辺実装も増えています。

---

今週は以上です。何か作っているものがある、または共有したい更新がある場合は、NostrでDMを送るか、[nostrcompass.org](https://nostrcompass.org)で見つけてください。
