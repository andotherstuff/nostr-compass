---
title: 'Nostr Compass #27'
date: 2026-06-17
publishDate: 2026-06-17
translationOf: /en/newsletters/2026-06-17-newsletter.md
translationDate: 2026-08-26
draft: false
type: newsletters
---

今週はsigner関連、P2P取引protocol、主要クライアントのリリースが目立ちました。[Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0)は170件超のPRをまとめ、[NIP-60](/ja/topics/nip-60/) Cashu wallet、[NIP-61](/ja/topics/nip-61/) nutzap、[NIP-82](https://github.com/nostr-protocol/nips/blob/master/82.md) software-appフィード、[NIP-F4](/ja/topics/nip-f4/) podcast対応、CLINKによるon-chain zap検証、KMPフェーズ1・2のiOS移行、Tor自己修復ドライバーを追加しました。[Clave v1.0.0（build 102）](https://github.com/DocNR/clave/releases/tag/v1.0.0)はApp Storeへ提出され、pushで起動するバックグラウンド署名と受信署名の検証をiOSにもたらします。[Mostro Core v0.13.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.0)はProtocol v2を出荷し、relay経由の注文通信を[NIP-44](/ja/topics/nip-44/) gift-wrapped DMへ置き換えました。[Mostro v0.17.5](https://github.com/MostroP2P/mostro/releases/tag/v0.17.5)ではオペレーター側の不正防止bondが任意かつ設定可能になりました。[Signet v1.11.0](https://github.com/Letdown2491/signet/releases/tag/v1.11.0)は、公開情報だけでkill-switchコマンドを偽造できた[NIP-17](/ja/topics/nip-17/)（gift-wrapped private DM）の管理コマンド署名バイパスを修正しました。[Chama](https://github.com/jesuspirate/chama)は6日間で7件のescrowリリースを出し、取引ルームを操作の壁から各参加者向けの対話型画面へ変えました。signer側では[Amber v6.2.1](https://github.com/greenart7c3/Amber/releases/tag/v6.2.1)、Claveのbuild [100](https://github.com/DocNR/clave/releases/tag/v0.2.0-build100)、[101](https://github.com/DocNR/clave/releases/tag/v0.2.0-build101)、[102](https://github.com/DocNR/clave/releases/tag/v1.0.0)、[Nostur 1.29.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.29.0-desktop)が、今週マージされた[NIP-46](/ja/topics/nip-46/)の新しい`logout`メソッド（[PR #2373](https://github.com/nostr-protocol/nips/pull/2373)）を実装しました。[Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1)とAmethystはいずれも、Nostr鍵向け共通Lightningインターフェース案であるCLINK nofferに対応します。[NIP-29](/ja/topics/nip-29/) relayグループには、banner tag、招待コード、メッセージのpin留め、[NIP-17](/ja/topics/nip-17/) DMによるグループ報告、role-based access controlを扱う5件の提案が出ました。

## トップストーリー

### Amethyst v1.12.0はCashu wallet、nutzap、CLINKドライバー、Tor自己修復を出荷

[Amethyst](https://github.com/vitorpamplona/amethyst)はVitor Pamplonaによる主要なAndroid Nostrクライアントです。[v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0)は、Newsletter #25で未リリース作業として扱った93件のPR（[NIP-32](/ja/topics/nip-32/) hashtagラベル、NIP-F4 podcast画面、音楽トラック、一時的signer、NIP-05フィルター付きon-chain zap）とNewsletter #26の続き（[NIP-F4](/ja/topics/nip-f4/)、Tor watchdogの基盤）に、今週の大規模な追加作業をまとめています。新作業の中心はCashu・nutzap画面、CLINK on-chain zapドライバー、Tor自己修復群、KMPのiOS移行です。

[NIP-60](/ja/topics/nip-60/) Cashu wallet対応と[NIP-61](/ja/topics/nip-61/) nutzap描画は[PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075)で入り、mint別残高画面（[PR #3115](https://github.com/vitorpamplona/amethyst/pull/3115)）と統合支払いカードUI（[PR #3191](https://github.com/vitorpamplona/amethyst/pull/3191)）がLightning address、on-chain zap、Cashu mint、NWCを1つのプロフィール支払い画面へまとめます（[PR #3185](https://github.com/vitorpamplona/amethyst/pull/3185)）。on-chain zap検証用CLINKドライバーは[PR #3039](https://github.com/vitorpamplona/amethyst/pull/3039)、[PR #3177](https://github.com/vitorpamplona/amethyst/pull/3177)、[PR #3182](https://github.com/vitorpamplona/amethyst/pull/3182)で出荷されました。CLINKはCommon Lightning Interface for Nostr Keysで、今週[Zeus v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1)も同じnofferインターフェースを搭載し、Amethystは検証state machine、再検証ドライバー、on-chain zapの最低額を追加します（[PR #3030](https://github.com/vitorpamplona/amethyst/pull/3030)）。[PR #3201](https://github.com/vitorpamplona/amethyst/pull/3201)は[NIP-17](/ja/topics/nip-17/)に従い、p-tag付きユーザーへのkind 1返信をgift wrapする非公開ノートを導入しました。宛先に応じてcomposerが公開ノートまたは封印されたグループ返信を生成します。

Torの信頼性改善は完全な自己修復stackとして入ります。[PR #3053](https://github.com/vitorpamplona/amethyst/pull/3053)はArtiをv2.3.0へ更新しwatchdogと統合テストを追加、[PR #3223](https://github.com/vitorpamplona/amethyst/pull/3223)はTorの準備完了までTor経由relayへのdialを抑止、[PR #3224](https://github.com/vitorpamplona/amethyst/pull/3224)は敵対的ネットワークがloopを停止させないようArti bootstrapを60秒でtimeout、[PR #3231](https://github.com/vitorpamplona/amethyst/pull/3231)はTorがActiveでも全circuitが停止している場合に自己修復します。その結果、ネットワーク変更やsleep・resume後にも手動操作なしで復旧します。KMP iOS移行のフェーズ1と2は[PR #3047](https://github.com/vitorpamplona/amethyst/pull/3047)と[PR #3050](https://github.com/vitorpamplona/amethyst/pull/3050)で出荷され、`quartz`と`commons` moduleのiOS CIを動かし、iOS版Amethystの基盤を整えます。

### Mostro Core v0.13.0はProtocol v2でrelayの仲介を削減

[Mostro](https://github.com/MostroP2P/mostro)は、Nostrをorder bookおよび取引通信層に使いLightningで決済するP2P Bitcoin取引所です。wire protocolを定義するRustライブラリ[mostro-core v0.13.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.0)は、relay経由のmessagingモデルをchangelogがProtocol v2と呼ぶ仕組みに置き換えます。これはkind 14 event上で動くNIP-44 direct transportです。取引固有のactionは[NIP-44](/ja/topics/nip-44/)でwrapされ、注文作成時に参加者が生成した取引別keyへ結び付けられたkind 14 messageとして流れ、公開addressable eventを介して会話を往復させません。

旧モデルでは、取引会話の全体がeventを運ぶすべてのrelayに露出していました。direct kind 14 transportでは注文設定、紛争処理、決済metadataが両当事者とMostro daemonの間に留まり、relayが見るのは暗号化envelopeだけです。v0.13.0はtransport変更に加え、v2 identity proofを取引keyへ結び付け（[commit log](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.0)）、新protocolに対するreplay riskの一種を閉じます。daemon側では[Mostro v0.17.5](https://github.com/MostroP2P/mostro/releases/tag/v0.17.5)が不正防止bondを任意かつオペレーター設定可能にしました。特定の取引を始める前に双方が少額のbondをlockし、正常完了時には返還、停滞、欠席、妨害時には没収される場合があります。bondはネットワーク全体ではなくnodeオペレーター単位で有効になるため、Mostroはnon-custodialを保ち、各オペレーターが取引摩擦と不正耐性の均衡を選べます。クライアント側の[Mostro Mobile v1.2.8](https://github.com/MostroP2P/mobile/releases/tag/v1.2.8)は新経路を支える17機能を追加しました。固定既定relayに代わるbootstrap relay discovery（[PR #610](https://github.com/MostroP2P/mobile/pull/610)）、bond展開フェーズ5として注文作成時のmaker不正防止bond（[PR #608](https://github.com/MostroP2P/mobile/pull/608)）、文脈付き注文キャンセルの通知履歴への永続化（[PR #602](https://github.com/MostroP2P/mobile/pull/602)）などです。2日後の[v1.2.9](https://github.com/MostroP2P/mobile/releases/tag/v1.2.9)はnode info eventの不正防止bond方針を表示し、注文前にそのMostro instanceのbond規則を確認できるようにしました（[PR #617](https://github.com/MostroP2P/mobile/pull/617)）。

### Signet v1.11.0はNIP-17管理コマンドの署名バイパスを修正

[Signet](https://github.com/Letdown2491/signet)はremote bunker signerで、管理者がhost machineへ触れずNostr経由でsignerをpanic、復旧、状態確認できるkill-switchを備えます。[v1.11.0](https://github.com/Letdown2491/signet/releases/tag/v1.11.0)は、その[NIP-17](/ja/topics/nip-17/) gift-wrap管理コマンド経路が署名済みsealを検証せず、未署名の内側のrumorが主張する作者だけを確認していた脆弱性を修正します。[NIP-44](/ja/topics/nip-44/) conversation keyは対称なので、signer pubkey、管理者npub、管理用relayという公開情報だけを持つ攻撃者が外部からgift wrapを偽造し、`panic`、`resumeall`、`alive`を含む任意のkill-switchコマンドを実行できました。修正はsealに`verifyEvent`を適用し、rumor作者をseal署名へ結び付けるため、未署名の偽造は入口で拒否されます。仕様と修正前コードから再現手順を明確に組み立てられるため、Signetオペレーターは速やかに更新すべきです。

### Chama v3.2.0からv3.5.0は取引ルームを刷新し資金経路を強化

[Chama](https://github.com/jesuspirate/chama)はFedimint ecashと2-of-3 Shamir秘密分散を組み合わせ、serverlessな取引決済を実現するNostr-native P2P escrowクライアントです。Newsletter #26ではstandalone app化とseller別storefrontを追加したv2.0.0からv3.1.0を扱いました。今週の6件の後続リリースは[v3.2.0](https://github.com/jesuspirate/chama/releases/tag/v3.2.0)から始まり、6月15日の[v3.5.0](https://github.com/jesuspirate/chama/releases/tag/v3.5.0)まで続きます。取引ルームUIを「今、自分は何をすべきか」という各参加者向けの問いを中心に再構成し、部分障害から資金経路を守ります。[v3.2.0](https://github.com/jesuspirate/chama/releases/tag/v3.2.0)はbuyer、seller、arbiterごとに色分けしたaction promptを追加し、全取引状態で各役割の次の行動を示します。[v3.3.0](https://github.com/jesuspirate/chama/releases/tag/v3.3.0)は取引engineの2つのconsensus ruleを厳格化し、効果を得るにはクライアントの協調更新を必須にしました。[v3.3.1](https://github.com/jesuspirate/chama/releases/tag/v3.3.1)は価格と支払い方法をtraderのcommunity currencyへlocalizeします。[v3.4.0](https://github.com/jesuspirate/chama/releases/tag/v3.4.0)は一時障害、race、tab終了でsatsを失わないよう資金経路へ5件のhardeningを追加しました。[v3.5.0](https://github.com/jesuspirate/chama/releases/tag/v3.5.0)は、取引を密かに偏らせ得るarbiter役に2つのクライアント側guardrailを加えます。

### Clave 1.0はpush起動バックグラウンド署名とともにApp Storeへ

[Clave](https://github.com/DocNR/clave)はユーザーのNostr秘密鍵をiPhone Keychainに保持するiOS向け[NIP-46](/ja/topics/nip-46/) remote signerです。アプリはend-to-end暗号化channelで署名を要求し、鍵自体は受け取りません。[v1.0.0 build 102](https://github.com/DocNR/clave/releases/tag/v1.0.0)は今週App Storeへ提出され、8か月のTestFlight betaを経て1.0 milestoneへ到達しました。このリリースはpush起動バックグラウンド署名を搭載します。Claveはアプリ終了中でもrequestを復号し、権限を確認し、署名して応答できるため、従来signerの応答性を制限していたiOS foreground要件がなくなります。受信署名はBIP-340 Schnorrと標準[NIP-01](/ja/topics/nip-01/) event serialization形式（署名済みNostr eventのhash方法を定義する基本仕様）で検証され、replay freshness guardも適用されるため、悪意あるアプリが再署名eventをresponse channelへ紛れ込ませることはできません。

このリリースはkind単位の権限モデルと3段階の機密度を持つ更新版[NIP-44](/ja/topics/nip-44/)暗号化層も導入します。「毎回確認」のrequestがユーザーの承認前にerrorを返していた低信頼署名のedge caseを修正し、1つのアプリpairingから複数identityを使えるmulti-account pairingを追加しました。bunker pairingは[NIP-46](/ja/topics/nip-46/) connect metadata拡張を通じて実際のアプリidentityを表示します。この拡張はClaveが[PR #2381](https://github.com/nostr-protocol/nips/pull/2381)で提案しました。正常な切断には新しい[NIP-46](/ja/topics/nip-46/) `logout`メソッドを使います。このメソッドは[PR #2373](https://github.com/nostr-protocol/nips/pull/2373)でマージされ、paired appは手動unpairなしでsessionを終えられます。アプリ別の信頼level（Full、Medium、Low）とevent kind別override、全署名のactivity log、任意のpush proxyにも対応します。proxy stackはMIT licenseで、クライアント別interop matrixは[`docs/nip46-compatibility.md`](https://github.com/DocNR/clave/blob/main/docs/nip46-compatibility.md)にあります。

## リリース

### Amber v6.2.1はNIP-46 logoutを追加しsignerのbattery消費を削減

[Amber](https://github.com/greenart7c3/Amber)は主要なAndroid Nostr signerです。[v6.2.1](https://github.com/greenart7c3/Amber/releases/tag/v6.2.1)はrelay再接続とWebSocket pingによるbattery消費を減らし、停止relayをsubscription poolから除き、relay通知更新時に端末を起こさなくしました。今週仕様にマージされたものと同じ[NIP-46](/ja/topics/nip-46/) `logout`にも対応し（[PR #2373](https://github.com/nostr-protocol/nips/pull/2373)）、クライアントがremote signer sessionを正常終了できます。event kind 39701（公開web bookmark）のparseも追加され、Amberからbookmark eventへ直接署名できます。SettingsはMaterial 3 cardと個別iconで再構築され、アプリ権限画面のnavigation crashを修正し、databaseをatomicに構築してaccount別connection leakを閉じました。

### Nostur 1.29.0は匿名返信とremote signer logoutを出荷

[Nostur](https://github.com/nostur-com/nostur-ios-public)はFabianによるiOS Nostrクライアントです。[1.29.0-desktop](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.29.0-desktop)はzap receiptへの返信と匿名返信を追加します。signer側ではremote bunker接続を改善し、account logout時にremote signerへ[NIP-46](/ja/topics/nip-46/) `logout`を送り、remote signer接続失敗時にspinnerが止まらない問題を修正しました。DM relayとアプリrelayの競合によるDM読み込み問題、返信へ移動して戻った際の重複投稿も修正し、通知行にmedia thumbnailを表示します。

### Citrine v3.0.0はNegentropy、NIP-42 AUTH、onion relay filterを出荷

[Citrine](https://github.com/greenart7c3/Citrine)はAndroidのlocal relay aggregatorです。[v3.0.0](https://github.com/greenart7c3/Citrine/releases/tag/v3.0.0)はmajor version更新で、set reconciliation同期用[NIP-77](/ja/topics/nip-77/) Negentropy、aggregatorでのexternal signerと[NIP-42](https://github.com/nostr-protocol/nips/blob/master/42.md) AUTH、aggregator取得での[NIP-51](https://github.com/nostr-protocol/nips/blob/master/51.md) mute list尊重を追加します。作者ごとの取得を3 relayに制限しsource relayとindexer relayを設定可能にし、follow、mute、metadataのcacheを再起動やnetwork変更後も再利用します。制限networkではpauseし、outbound proxy無効時にはonion relay URLを除外します。保護eventを埋め込むrepostを拒否し、mute listは既定で経年削除から保護されます。

### FIPS v0.4.0-rc1はNym mixnet transportとmDNS LAN discoveryを追加

[FIPS](https://github.com/jmcorgan/fips)はFIPS mesh sync protocolの実装です。[v0.4.0-rc1](https://github.com/jmcorgan/fips/releases/tag/v0.4.0-rc1)はv0.3.0とwire互換で、混在meshも相互運用でき一斉更新は不要です。node間の発見と接続方法として、single-container demoとmixnet relay例を備えたNym mixnet outbound transport、および任意のlocal-link mDNS / DNS-SD discoveryを追加します。counterのみの新しい`show_metrics` queryによりhot pathへ負荷を加えずPrometheus scraperを使え、FMPとFSPのrekeyは双方向packet loss時にも途切れないよう強化されました。

### Calendar by Formstr v1.6.1とv1.6.2はevent別通知を追加

[Calendar by Formstr](https://github.com/formstr-hq/nostr-calendar)は[NIP-52](/ja/topics/nip-52/) calendarクライアントです。[v1.6.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.6.1)はevent別の通知設定（[PR #109](https://github.com/formstr-hq/nostr-calendar/pull/109)）を追加し、個々のcalendar eventごとにreminderを有効・無効にできます。[v1.6.2](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.6.2)はAmberでのlogin（[PR #185](https://github.com/formstr-hq/nostr-calendar/pull/185)）を修正し、Amber 6.2.xの新しい[NIP-46](/ja/topics/nip-46/) handshakeがend-to-endで動作します。

### Bitchat v1.5.2とv1.5.3はNostr・BLE transportを強化

[Bitchat](https://github.com/permissionlesstech/bitchat)はBluetoothとNostrを使うmesh chatクライアントです。[v1.5.2](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.2)はflood防止のためiOS peer通知をrate limitし（[PR #972](https://github.com/permissionlesstech/bitchat/pull/972)）、Nostr検証とBLE announce確認を強化して（[PR #1012](https://github.com/permissionlesstech/bitchat/pull/1012)）、relay側のNostr ingest経路が不正messageをlocal mesh handlerへ届く前に拒否します。[v1.5.3](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.3)は`NostrRelayManager`と`NetworkActivationService`間の再帰的`dispatch_once`による起動crashのhotfixです（[PR #1343](https://github.com/permissionlesstech/bitchat/pull/1343)）。

### Keep v1.0.5はsigner方針を監査済みRust coreへ移行

[Keep](https://github.com/privkeyio/keep-android)は[keep](https://github.com/privkeyio/keep) Rust coreを包むAndroid signerです。[v1.0.5](https://github.com/privkeyio/keep-android/releases/tag/v1.0.5)は[keep v0.4.8](https://github.com/privkeyio/keep/releases/tag/v0.4.8)へ固定し、高負荷時にhandshakeの最初のeventを落とさないbunker初期化race修正（[PR #296](https://github.com/privkeyio/keep-android/pull/296)）、bunkerの`onConnect` callbackからAuthorized Clients画面を埋める変更（[PR #291](https://github.com/privkeyio/keep-android/pull/291)）、keep-mobileのkill switchを単一の正へ統合する変更（[PR #284](https://github.com/privkeyio/keep-android/pull/284)）を出荷します。上流Rust coreは6月13日に[v0.4.9](https://github.com/privkeyio/keep/releases/tag/v0.4.9)を公開しました。[NIP-55](/ja/topics/nip-55/)と[NIP-46](/ja/topics/nip-46/)のsigner方針（権限判断、機密kindの期間上限、期限、keyed-HMAC改ざん検知audit chain、callerのtrust-on-first-use、永続署名rate limiter）をKotlinとの重複実装から監査済みRust coreへ移し、[NIP-44](/ja/topics/nip-44/) v3 cipherも追加します。このcoreは次のkeep-mobile更新に入ります。

### ants v0.4.5は記事portal linkを追加しportal群にHablaを復帰

[ants](https://github.com/dergigi/ants)はdergigiによるNostr検索・reader toolです。[v0.4.5](https://github.com/dergigi/ants/releases/tag/v0.4.5)はlong-form postの記事cardに、article portal link、記事固有`naddr`共有、`nevent` copy、raw JSON表示を追加します。Hablaを復帰させ、停止destinationを交換し、imwald portalを削除してarticle portal群を更新しました。記事footnoteの描画と記事内anchor navigationも復元し、login復元時にはrelay接続後にprofileを取得することでheader avatarを正しく解決します。

### Morganite v0.0.3はTorを必要時に使うAndroid向けlocal Blossom cacheを出荷

[Morganite](https://github.com/greenart7c3/Morganite)はAmberとCitrineの作者greenart7c3による新しいAndroid local Blossom cacheです。[BUD-08](https://github.com/hzrd149/blossom/blob/master/buds/08.md) local mirrorとして動き、1GBを超えると利用頻度の低いblobから削除します。[v0.0.3](https://github.com/greenart7c3/Morganite/releases/tag/v0.0.3)は必要時にTorを起動し、idle時に停止してbatteryを節約します。作者検索後にNostr relayを切断してbackground消費を止め、filterなしlogcat streamとleakしたHTTP clientによるbattery消費を修正し、交換済み`OkHttp` clientをmain thread外で解放します。Blossom server list検索前にユーザーのinbox relayを取得してblob discoveryをoutbox modelに従わせ、local cacheにないblobへの`HEAD` requestでは実体をdownloadするため、cache warmupが実際の需要に結び付きます。

### Coracle 0.6.34と0.6.35はNIP-46 login、古いfeed、返信toggleを修正

[Coracle](https://github.com/coracle-social/coracle)はhodlbodによるNostr webクライアントです。[0.6.34](https://github.com/coracle-social/coracle/releases/tag/0.6.34)は[NIP-46](/ja/topics/nip-46/) login、view切替後にhome timelineが更新されない古いfeed状態、有効にすると全件を除外する返信toggleを修正します。feedとlist viewも再構築し、toast safe-area insetを修正、画像読み込みを改善しました。[0.6.35](https://github.com/coracle-social/coracle/releases/tag/0.6.35)は返信無効時にrepostまで隠れる問題を修正し、reply filterの過剰適用を止めます。

### Zeus v13.1.0-rc1はCLINK nofferとqueueなしNWCを出荷

[Zeus](https://github.com/ZeusLN/zeus)はwallet connectとnoffer支払いにNostrを使うself-custody Bitcoin・Lightning walletです。[v13.1.0-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.1.0-rc1)はPrimalとの協力でiOSにqueueなし[NIP-47](https://github.com/nostr-protocol/nips/blob/master/47.md) Nostr Wallet Connect支払いを追加し、支払い済みNWC invoiceがbackground queueで待たなくなります。Zeus Payが全account向けCLINK nofferを生成するため、senderはNostr鍵だけで任意のZeusユーザーへ支払えます。Zeus PayのNostr Zapを無効化するoptionも追加し、受取人はNWCを無効にせずkind 9735 receipt経路だけを止められます。

### Alby Extension v3.14.3はNIP-07 signerが使うnoble・scure crypto stackを移行

[Alby Extension](https://github.com/getAlby/lightning-browser-extension)はLightning機能とともに[NIP-07](https://github.com/nostr-protocol/nips/blob/master/07.md)署名とNostr Wallet Connectを提供するbrowser extensionです。[v3.14.3](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.14.3)は`@noble/curves`、`@noble/hashes`、`@noble/ciphers`、`@noble/secp256k1`、`@scure/bip32`、`@scure/base` stackをv2・v3 majorへ移行します。これらは[NIP-07](https://github.com/nostr-protocol/nips/blob/master/07.md) signer経路がevent署名と[NIP-44](/ja/topics/nip-44/)暗号化に使うcrypto libraryであり、major更新はNostr webクライアントからの全署名requestについてextensionが生成するwire formatに関わります。

### Mostro Mobile v1.2.8とv1.2.9はProtocol v2を支援しbond方針を表示

[Mostro Mobile](https://github.com/MostroP2P/mobile)はMostroのmobileクライアントです。[v1.2.8](https://github.com/MostroP2P/mobile/releases/tag/v1.2.8)は上のトップストーリーで扱った[mostro-core v0.13.0 Protocol v2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.13.0)のクライアント側対応を導入し、計17機能を追加します。[PR #608](https://github.com/MostroP2P/mobile/pull/608)のmaker不正防止bond、[PR #610](https://github.com/MostroP2P/mobile/pull/610)のbootstrap relay discovery、[PR #602](https://github.com/MostroP2P/mobile/pull/602)の通知履歴に残る注文キャンセル、[PR #605](https://github.com/MostroP2P/mobile/pull/605)の注文作成画面におけるfiat金額上限などです。[v1.2.9](https://github.com/MostroP2P/mobile/releases/tag/v1.2.9)はnode info eventの不正防止bond方針を表示し（[PR #617](https://github.com/MostroP2P/mobile/pull/617)）、注文前にMostro instanceのbond規則を確認できます。

### ZapBook build 4から27はmulti-account、Marmot key公開、circle再招待を出荷

[ZapBook](https://github.com/codeswot/ZapBook)はcodeswotによるiOS・Android向けNostr-native social readingアプリで、1人から100人のreading circle内でmilestoneを共有し、励ましとして互いにsatsをzapします。6月11日の[build 4](https://github.com/codeswot/ZapBook/releases/tag/v1.0.0-build.4)から6月15日の[build 27](https://github.com/codeswot/ZapBook/releases/tag/v1.0.0-build.27)までに17件のtag付きbuildと7件のmerged PRを出荷しました。滑らかなaccount切替を持つmulti-account対応は[PR #25](https://github.com/codeswot/ZapBook/pull/25)で入り、複数Nostr identityの保持とsession移行が可能です。初期[Marmot](/ja/topics/marmot/) key package（kind 443）の公開はonboarding完了時に自動実行され（[PR #20](https://github.com/codeswot/ZapBook/pull/20)）、reading circleでinvite-only group messagingを使う前提を満たします。circleから削除されたmemberの処理は新しい再招待を正しく扱い（[PR #24](https://github.com/codeswot/ZapBook/pull/24)）、再追加したmemberにinviteが届かない問題を解消しました。ONNX embedding inferenceをbackground isolateへ移してreader内semantic検索を支え（[PR #19](https://github.com/codeswot/ZapBook/pull/19)）、環境別設定用`APP_ID_SUFFIX`とともにNWC serviceを統合し、1つのhubで複数ZapBook buildを扱えます。

### Alby Hub v1.23.0は削除済みアプリのNIP-47公開を修正しBitrefillをNWCへ移行

[Alby Hub](https://github.com/getAlby/hub)はself-hosted Lightning・Nostr hubです。[v1.23.0](https://github.com/getAlby/hub/releases/tag/v1.23.0)のNostr以外の変更（Just-in-Time channel、debit card top-up用Cards page、実験的Ark payment backend、stories home page）はCompassの範囲外です。[NIP-47](https://github.com/nostr-protocol/nips/blob/master/47.md)側では、削除済みアプリのNIP-47 info公開を再試行しないため、削除したconnectionがkind 13194 info eventを再公開し続けなくなり（[PR #2391](https://github.com/getAlby/hub/pull/2391)）、Bitrefill独自app entryを標準NWC connectionへ置き換えます（[PR #2420](https://github.com/getAlby/hub/pull/2420)）。app storeアプリ向けreadonly option（[PR #2415](https://github.com/getAlby/hub/pull/2415)）はhub内store経由で公開されるNWCアプリの権限scopeを絞ります。

### その他のリリース

今週の小規模なリリースのうち、Nostrに関連するものの各リリース単体の内容が限られるものです。[Nostria v3.1.48からv3.1.50](https://github.com/nostria-app/nostria/releases)はWeb Bookmark展開を継続し、v3.1.50で通知の信頼性とevent thread databaseを最適化。[Deepmarks v0.7.0からv0.7.5](https://github.com/ostermayer/deepmarks-public/releases)は[NIP-B0](https://github.com/nostr-protocol/nips/pull/2280) social bookmarkクライアントを反復し、今週[PR #96](https://github.com/andotherstuff/nostr-compass/pull/96)でwebsite linkも追加。[Keep v1.1.1からv1.1.4](https://github.com/privkeyio/keep-android/releases)は上で扱ったv1.0.5 signerリリースに4件のF-Droid reproducible build修正を追加。[NoorNote v0.11.1、v0.12.0、v0.13.0、v0.13.1](https://github.com/77elements/noornote/releases)はdesktop noteクライアント、[Boris v0.12.2](https://github.com/dergigi/boris/releases/tag/v0.12.2)はBoris reader、[Nostr Mail Client v0.13.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.13.0)、[Feeder 2.21.1](https://github.com/spacecowboy/Feeder/releases/tag/2.21.1)、[nak v0.19.13](https://github.com/fiatjaf/nak/releases/tag/v0.19.13)はNostr CLIの内容なしmaintenance更新、[Hashtree v0.2.68からv0.2.71](https://github.com/mmalmi/hashtree/releases)はhash tree address型release publisherのgateway mutable-root cacheを更新、[NYM v3.72.501とv3.72.502](https://github.com/Spl0itable/NYM/releases)はNostrifyベースrelay実装を更新、[swift-nostr-client 0.3.0、0.4.0、0.5.0](https://github.com/yysskk/swift-nostr-client/releases)は85件のmerged PRを背景にiOS Nostrクライアントで3件のminor release、[lawallet-nwc v0.11.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v0.11.0)はLaWallet Nostr Wallet Connect bridgeで18件のmerged PR、[Astraea v5.35.59からv5.35.62](https://github.com/mouse484/astraea/releases)はAstraea Nostrクライアントを更新しました。また、[BTC RechargeとgiftcardshopのNIP-05検証済みNostr DM bot](https://github.com/andotherstuff/nostr-compass/pull/101)が新しいShops categoryでproject directoryへ追加されました。

## 未リリースの変更

### diVineは次のshort-form videoリリースへ向け119件のPRをマージ

[diVine](https://github.com/divinevideo/divine-mobile)はVine archiveをNostr基盤上で復元するNostr-native short-form looping videoクライアントです。今週、tag付きreleaseなしで119件のPRをマージしました。Nostrに関わる主要作業は、relayのOKが欠けても失敗として表示しないREST優先video公開経路（[PR #5221](https://github.com/divinevideo/divine-mobile/pull/5221)と[PR #5220](https://github.com/divinevideo/divine-mobile/pull/5220)）、広域blocklist変更時にcurated・liked gridを再filter（[PR #5208](https://github.com/divinevideo/divine-mobile/pull/5208)）、再install regression後のDM会話list復旧（[PR #5202](https://github.com/divinevideo/divine-mobile/pull/5202)）、profile上のNostr badge表示復元（[PR #5218](https://github.com/divinevideo/divine-mobile/pull/5218)）、comment引用内`nostr:`参照のlink化（[PR #5225](https://github.com/divinevideo/divine-mobile/pull/5225)）です。video editor stackはclipのmulti-select結合・削除、zoom追従letterbox scrim付きpinch-to-zoom canvas、clipのcrop・rotate・flipも追加しました。

### Polleramaはsigner再構築と機能群を含む15件のPRをマージ

[Pollerama](https://github.com/formstr-hq/nostr-polls)（repo `formstr-hq/nostr-polls`）はForm*系のNostr-native poll・feedクライアントで、今週v1.6.2を出した[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar)の姉妹projectです。`nostr-polls`の最新tagは3月の[v1.6.4](https://github.com/formstr-hq/nostr-polls/releases/tag/v1.6.4)なので期間内作業は次のtag待ちで未出荷ですが、6月9日から16日にabh3po、geralt-debugs、SIDDHANTCOOKIEの貢献を含む15件のPRがマージされました。signer側では[PR #198](https://github.com/formstr-hq/nostr-polls/pull/198)で既存署名面を置換し、[PR #201](https://github.com/formstr-hq/nostr-polls/pull/201)で更新しました。[PR #200](https://github.com/formstr-hq/nostr-polls/pull/200)はlogin時のkind 0 metadata更新を止め、新規sign-inが要求していないprofile eventを公開しないようにします。機能群にはprofile viewから投稿できるprofile editor（[PR #205](https://github.com/formstr-hq/nostr-polls/pull/205)）、改善したrepost flow（[PR #209](https://github.com/formstr-hq/nostr-polls/pull/209)）、topic discoveryを容易にする経路（[PR #202](https://github.com/formstr-hq/nostr-polls/pull/202)）があります。次のtag付きreleaseにこれらが入ります。

### Libraryとtooling

[NDK PR #375](https://github.com/nostr-dev-kit/ndk/pull/375)と[rust-nostr](https://github.com/rust-nostr/nostr)、[nostr-tools](https://github.com/nbd-wtf/nostr-tools) repoのmerged workは今週静かで、各1、2件のmerged PR、tag付きreleaseなしでした。[ContextVM SDK](https://github.com/contextvm/contextvm-sdk)（merged PR 1件）、[mesh-llm](https://github.com/agentvm/mesh-llm)（merged 37件、open 8件）、[Zap Cooking](https://github.com/seth-for-real/zap-cooking)（merged 26件）、[Routstrd](https://github.com/routstrd/routstrd)（merged 2件）の活動は期間内にrelease tagなしで続きました。

## NIP更新とprotocol仕様作業

今週のprotocol作業はsigner hardeningと[NIP-29](/ja/topics/nip-29/) group governanceの2領域に集中しました。

**今週マージ:**
- **[NIP-46](/ja/topics/nip-46/)（Nostr Connect）。** [PR #2373](https://github.com/nostr-protocol/nips/pull/2373)はクライアントがremote signer sessionを正常終了できる`logout`メソッドを追加しました。Amber、Clave、Nosturが同じ週に対応を出荷しました。
- **NIP-CC（Community Chat）。** [PR #2365](https://github.com/nostr-protocol/nips/pull/2365)はclient側の仕組みについて現行の[NIP-GC（Group Chat）](https://github.com/nostr-protocol/nips/pull/2331)仕様を参照するようNIP-CCを更新し、community room仕様を標準group chat primitiveへ合わせます。

**Open NIP-29群（relay-based group governance）:**
- **Banner tag。** [PR #2383](https://github.com/nostr-protocol/nips/pull/2383)はgroup metadata kind 39000 eventへ`banner` tagを追加します。
- **招待コードsuffix。** [PR #2380](https://github.com/nostr-protocol/nips/pull/2380)はgroup identifierへinvite code suffixを導入し、one-shot inviteをgroup ID自体へencodeできるようにします。
- **Message pin留め。** [PR #2379](https://github.com/nostr-protocol/nips/pull/2379)はupdate-pin-list moderation actionと、pin済み集合をbroadcastするkind 39005 eventを追加します。
- **NIP-17 DMによるgroup報告。** [PR #2377](https://github.com/nostr-protocol/nips/pull/2377)はmemberがgroup abuseをrelayの管理連絡先へ[NIP-17](/ja/topics/nip-17/) gift-wrapped DMで報告するflowを定義し、moderation trafficを公開group event streamから外します。
- **Role-based access control。** [PR #2376](https://github.com/nostr-protocol/nips/pull/2376)は既存のadmin・member分離の上にRBAC roleを追加します。

**Open NIP-46 follow-up:**
- **Connect requestのclient metadata。** [PR #2381](https://github.com/nostr-protocol/nips/pull/2381)は接続クライアントが任意の`name`、`url`、`icon` fieldをconnect requestで送り、signerがpairing画面にアプリidentityを表示できるようにします。Clave build 101が提案を実装しています。
- **Silent timeoutの回避。** [PR #2375](https://github.com/nostr-protocol/nips/pull/2375)はユーザー入力が必要なsignerが判断までrequestをopenに保つよう仕様を厳格化し、Clave build 100が実装側で修正したfailure modeを解消します。

**その他のopen work:**
- **NIP-100 Sovereign Agent Identity Network（SNIN）。** [PR #2378](https://github.com/nostr-protocol/nips/pull/2378)はautonomous agentのidentityとcapability discoveryを担うagent-to-agent protocolを提案します。範囲が広く、reviewで小さな単位へ分割される可能性があります。

**Blossom仕様。** [BUD-00 PR #108](https://github.com/hzrd149/blossom/pull/108)は6月15日にマージされ、serverが実装しないBlossom blob上のクライアント側慣習とdata formatもBUD定義へ含めました。これまで帯域外extensionとして扱われていたBUD-10（`blossom:` URI scheme）やBUD-08（今週Morganiteが実装したlocal cache慣習）も標準番号体系へ入ります。

## NIPディープダイブ: NIP-77（Negentropy）

[NIP-77](/ja/topics/nip-77/)はNostr relay向けset reconciliation protocolを定義します。clientとrelay、またはbridge内の2つのrelayがfilterに一致するevent集合をそれぞれ持ち、全件を再送せず和集合へ収束させます。単純な方法は全event IDをwireへ流して差分を取りますが、busyなfilterでは差分量にかかわらず大きい側の集合sizeに比例したcostがかかります。NIP-77はcostを対称差に比例するまで削減します。

仕様は`NEG-OPEN`と`NEG-MSG`という2つのrelay message上で動きます。clientは`["NEG-OPEN", <subscription_id>, <filter>, <initial_message>]`でreconciliation sessionを開きます。`<initial_message>`はclient側集合を記述するhex encode済みNegentropy payloadです。replyは`NEG-MSG` frameで届き、双方が固定点へ達するまでmessageを交換します。各`NEG-MSG`はrangeを固有fingerprint付きsub-rangeへ分割して不一致を絞るか、小rangeのIDを列挙してreceiverが直接diffを計算できるようleafを終端します。相手に自分が持たないeventがあると判断した側は通常の`REQ`でIDを要求し、自分だけが持つeventのuploadは相手側への通常の`EVENT` publishに任せます。

下層data structureは順序付きMerkle treeの変種です。local集合の各eventは`(created_at, id)`をkeyとしてrangeへbucket化され、各rangeには含まれるIDから計算した小さなfingerprintが付きます。clientとrelayでfingerprintが一致すれば、そのrangeは収束済みとしてskipされます。異なればreply側がrangeを半分またはsub-rangeへ分割し、各fingerprintを送って不一致を再帰的に絞ります。小さなthreshold未満のleaf rangeはそのまま送られます。収束済みrangeは内部event数にかかわらず、ほぼcostなしで確認できる点が重要です。

`created_at`順のframeには2つの意味があります。第一に、既存のNostr paginationは同じtimestampに`until`と`since`を使うため、reconcilerは全archiveを再同期せずsessionをまたいで再開できます。上限をcacheし、次の同期をそこから始めます。第二に、sort済みkeyからのrange分割は決定論的なので、clientとrelayは追加negotiation messageなしで次のboundaryに合意できます。sync costはおよそO(d log n)です。dは対称差のsize、nは大きい側の集合sizeで、単純なID dumpのO(n)やN件のREQを発行するO(n) round tripを大幅に下回ります。

実装には3つのtradeoffがあります。fingerprint sizeはcollision確率とbandwidthの均衡で、仕様はrangeごとに32 byteを使います。小さくすればbyteを節約できますが、誤一致でeventを欠落させる可能性が上がります。leaf threshold、すなわち分割を止めてIDを直接送る境界はround tripとmessage帯域の均衡で、小さいthresholdはroundを増やし、大きいthresholdはleaf messageを大きくします。またprotocolは双方が同じrangeから同じfingerprintを計算できることを前提とし、両実装が合意する安定した`(created_at, id)` pair serializationが必要です。そのため仕様はfingerprint構築時のbyte orderを厳密に定めています。

NIP-11の`supported_nips`でNIP-77を広告するrelayに対し、clientは通常の`REQ`同期の代わり、または併用でreconciliationできます。clientは用途でprotocolを選びます。過去stateのない新規subscriptionでtail trafficを求めるなら`REQ`、長時間停止後に追い付くmirrorならarchiveに対して対称差が小さいため`NEG-OPEN`を使います。両経路は異なるdeployment contextで補完関係にあります。

`NEG-OPEN`交換例:

```
→ ["NEG-OPEN", "sync-1", {"kinds":[1],"authors":["abc..."]}, "<hex initial Negentropy message>"]
← ["NEG-MSG", "sync-1", "<hex relay response>"]
→ ["NEG-MSG", "sync-1", "<hex client refinement>"]
← ["NEG-MSG", "sync-1", "<hex leaf with IDs the relay has and client lacks>"]
→ ["REQ", "fetch-1", {"ids":[...]}]
← [...EVENT messages...]
← ["EOSE", "fetch-1"]
→ ["CLOSE", "sync-1"]
```

[Citrine v3.0.0](https://github.com/greenart7c3/Citrine/releases/tag/v3.0.0)は今週relay aggregatorへ[NIP-77](/ja/topics/nip-77/)対応を出荷し、Android local relayからbulk `REQ`取得の代わりにexternal relayとreconciliationできるようにしました。

## NIPディープダイブ: NIP-61（Nutzap）

[NIP-61](/ja/topics/nip-61/)はNostr eventとして配送されるpeer-to-peer Cashu ecash支払いを定義します。senderはrecipientのNostr由来公開鍵へlockしたCashu tokenを公開し、recipientは都合のよい時にmintからredeemします。支払い時点でreceiverがLightning経由でreachableである必要があるNIP-57 zapと異なり、nutzapはrecipientが自分の予定でredeemできる自己完結型ecash tokenです。

仕様はCashuのP2PK lock primitiveと3つのevent kindを組み合わせます。kind 10019はrecipientのmint推奨で、recipientがnutzapを受け入れる1つ以上のmintと、proofをlockするCashu公開鍵を載せるreplaceable eventです。この鍵はrecipientのNostr identity keyとは別で、identity keyがecash secretへ触れないようnutzap受取用にderiveしたwallet scoped keyです。senderは送金前にkind 10019を読み、recipientが既に信頼するmintでredeemできるtokenを作ります。

kind 9321が支払いeventです。1つ以上のCashu `proof` tag（それぞれkind 10019のrecipient nutzap pubkeyへ結び付いたP2PK lock済みproof）、mint URLを持つ`u` tag、zap対象noteを示す任意の`e`・`a` tag、recipientの`p` tagを載せます。recipientは通常のNostr subscriptionでkind 9321を受け取り、proofが自分のkind 10019にあるmintで自分のnutzap pubkeyへlockされていることを検証し、対応する秘密鍵でunlockして[NIP-60](/ja/topics/nip-60/) walletへ保持するかLightningへmeltします。kind 7375はredeem済みproofをrecipientのwallet event chainへ記録し、relayから再同期したwalletが同じ送信元のnutzap proofを重複計上しないようにします。

trust modelは設計が明示的に負う代償です。Cashu mintが裏付け価値を保持するため、悪意ある、または差し押さえられたmintはredeemを拒否できます。NIP-61はNIP-60からcustody riskを継承し、それを除去しません。代わりにoffline対応で即時finalityを持つmicropaymentを得ます。token自体が支払いなのでrecipientはLightning nodeを動かしたり、real timeにincoming HTLCを受けたりする必要がなく、同じmintのproofを持つsenderはcustodianへのnetwork hopなしで支払えます。kind 10019の広告がsocial layerのgateです。recipientのtrusted set外のmintを選ぶsenderはredeem不能tokenを送るriskを負い、recipientのredeem面を予測可能に保ちます。

NIP-57と比べ検証経路も単純です。NIP-57 zap receiptはrecipientのLNURL serviceが公開するkind 9735で、verifierはLNURL endpointを取得し、receipt署名鍵がendpointの宣言と一致することを確認する必要があります。nutzapは支払いのcryptographic proof、すなわちP2PK lock済みproof自体をinlineで運ぶため、mintの公開鍵を持つverifierなら第三者へのround tripなしでproofの妥当性を確認できます。代わりにnutzap検証はmint keysetの理解が必要ですが、NIP-57検証には標準LNURL infrastructureだけが必要です。

2つのzap形式は補完関係で共存します。Lightning routingを持つreceiverと、Lightning settlement semanticsでsats建て支払いを望むsenderにはNIP-57 zapが適します。offline receiver、Lightning feeが送金額を上回るmicropayment中心のflow、Lightning infrastructureを持たないユーザー向けクライアントにはNIP-61 zapが適します。

nutzap event例:

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1750162800,
  "kind": 9321,
  "tags": [
    ["proof", "{\"amount\":21,\"secret\":\"...\",\"C\":\"...\",\"id\":\"...\"}"],
    ["u", "https://mint.example.com"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3"],
    ["p", "c5d8a4e3b2a1f0e9d8c7b6a5949382716050403020100ffeeddccbbaa99887766"]
  ],
  "content": "Great post!",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

[Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0)は今週、NIP-60 wallet面とともにNIP-61 nutzapの描画を正式対応として出荷しました（[PR #3075](https://github.com/vitorpamplona/amethyst/pull/3075)）。受信nutzapをtimelineへ描画し、walletでmint別残高を表示します。
