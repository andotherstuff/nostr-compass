---
title: 'Nostr Compass #13'
date: 2026-03-11
translationOf: /en/newsletters/2026-03-11-newsletter.md
translationDate: 2026-03-11
draft: false
type: newsletters
---

Nostr Compassへようこそ。Nostrの週刊ガイドです。

**今週の内容:** [Shopstr](https://github.com/shopstr-eng/shopstr)と[Milk Market](https://github.com/shopstr-eng/milk-market)が、agent駆動コマース向けにMCPサーフェスを追加しました。一方で[OAuth Bunker](https://github.com/flox1an/oauth-bunker)、[Amber](https://github.com/greenart7c3/Amber)、[strfry](https://github.com/hoytech/strfry)は、アプリ、signer、Relayソフトウェア全体で[NIP-42](/ja/topics/nip-42/)（クライアントからRelayへの認証）のrelay-authとprotected event対応を追加しました。[Route96](https://github.com/v0l/route96)は、AI labeling、moderation queue、perceptual hashing、machine-readableなserver文書を中心とする2件のreleaseを出しました。[Samizdat](https://github.com/satsdisco/samizdat)は、すでにwebで稼働していましたが、初のAndroid alphaを公開し、その後[NIP-55](/ja/topics/nip-55/)（Android署名アプリケーション）signerサポートも追加しました。[Formstr](https://github.com/formstr-hq/nostr-forms)は[NIP-49](/ja/topics/nip-49/)（秘密鍵暗号化）によるsignupを追加し、[Amethyst](https://github.com/vitorpamplona/amethyst)はNamecoinベースの[NIP-05](/ja/topics/nip-05/)（ドメイン検証）解決機能を出荷しました。[Mostro](https://github.com/MostroP2P/mostro)は[v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4)を公開し、NIPsリポジトリは[NIP-91](/ja/topics/nip-91/)（フィルターのAND演算子）と[NIP-66](/ja/topics/nip-66/)（Relay発見と稼働監視）向け防御的ガイダンスをマージしました。

## ニュース

### ShopstrとMilk MarketがMCPコマースサーフェスを公開

[Shopstr](https://github.com/shopstr-eng/shopstr)は、LightningとCashu支払いを備えたP2Pマーケットプレイスで、[PR #234](https://github.com/shopstr-eng/shopstr/pull/234)（[commit 94ef7d1](https://github.com/shopstr-eng/shopstr/commit/94ef7d1a4519e8e0158668d13c8cb8684b1d46e2)）をマージし、agentのアカウント管理向けにAPI key認証付きMCP serverを追加しました。この変更では、agent discovery用の`.well-known/agent.json`、MCPのonboardingとstatus endpoint、注文作成と支払い確認route、購入用・読み取り用の専用tool、API key用settings画面が加わります。[PR #236](https://github.com/shopstr-eng/shopstr/pull/236)はこれを拡張し、message、address、注文更新、product spec選択に対するseller側操作を追加しました。[PR #235](https://github.com/shopstr-eng/shopstr/pull/235)のセキュリティ修正では、1回だけのSHA-256 API key hashingを、salt付きPBKDF2 100,000回反復へ置き換えています。

agentは、既存の[NIP-47](/ja/topics/nip-47/)（Nostr Wallet Connect）と[NIP-60](/ja/topics/nip-60/)（Cashuウォレット）支払いフローを使って、ページをscrapeしたりクライアント挙動をreverse engineerしたりせずに、[NIP-99](/ja/topics/nip-99/)（分類型リスティング）のlistingを読み、checkoutまで進めます。

[Milk Market](https://github.com/shopstr-eng/milk-market)は、[milk.market](https://milk.market)で動くNostr上のfood marketplaceで、同じMCPとAPI key基盤を[commit da6c0b4](https://github.com/shopstr-eng/milk-market/commit/da6c0b499494b4e4861c4ff8a220e066c46285b3)で導入しました。[PR #10](https://github.com/shopstr-eng/milk-market/pull/10)は、subscription注文、購入後の配送先変更、Stripeなどの法定通貨支払い経路に対応するmulti-merchantかつmulti-currencyのcheckout処理を追加します。続く[PR #11](https://github.com/shopstr-eng/milk-market/pull/11)は、fresh install時にfailed relay publishes tableが作成されず初回ロードで500 errorが出る起動時database初期化バグを修正しました。このagent向けinterfaceは、ShopstrではBitcoinネイティブのcheckout、Milk Marketでは法定通貨とBitcoinを混ぜたcheckoutの両方に対応します。

### NIP-42リレー認証がBunker、Signer、Relayに広がる

[OAuth Bunker](https://github.com/flox1an/oauth-bunker)は、OAuth providerをNostr署名に橋渡しする[NIP-46](/ja/topics/nip-46/)（Nostr Connect）bunkerで、[NIP-07](/ja/topics/nip-07/)（ブラウザ拡張署名者）login、自動single-identity選択、削除されたidentityのcleanupを追加しました（[commit f0c7683](https://github.com/flox1an/oauth-bunker/commit/f0c7683cb2374fd9a3ebd1b186055da8abd2c2ff)）。identityが1つしかない場合、bunkerは今やpromptせず自動選択します。identityを削除すると、ぶら下がったassignmentとconnectionも同時に消えます。[Commit 6b8796c](https://github.com/flox1an/oauth-bunker/commit/6b8796c6c59c7d48dc1ede92d6de6bf54feb56cc)は、assignment済みユーザー向けの`ALWAYS_ALLOWED_KINDS`設定経路を追加し、既定ではkind `30078`のapp固有データを許可します。これにより、委任されたidentityはイベントごとの承認なしでapp固有storageへ書き込めます。

[Amber](https://github.com/greenart7c3/Amber)は、Android向け主要[NIP-55](/ja/topics/nip-55/) signerであり、1週間の間に4件のpre-releaseを含む[v4.1.3-pre4](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3-pre4)を公開しました。[PR #317](https://github.com/greenart7c3/Amber/pull/317)はkind `22242` request向けの[NIP-42](/ja/topics/nip-42/) Relay認証処理を追加します。実装では、Relay固有permissionを追跡する新しいdatabase columnと、`(pkKey, type, kind, relay)`上のunique indexが加わります。ユーザーには専用auth画面が表示され、Relayごと、またはwildcard `*` scopeで全Relay向けに許可・拒否し、その選択を永続化できます。wildcard permissionは、そのkindに対するRelay固有entryをすべて消去します。[PR #318](https://github.com/greenart7c3/Amber/pull/318)は続けて、multi-event request画面をrefactorし、別画面へ遷移せずcomposable cardで詳細をその場表示するようにしました。このreleaseでは、default profile Relayの更新、bottom-sheetでのrequest表示、StrongBox keystoreを無効にすることでMediaTek端末のcrash修正も含まれます。

Relay側では、[strfry PR #156](https://github.com/hoytech/strfry/pull/156)が[NIP-70](/ja/topics/nip-70/)（保護イベント）向けNIP-42 auth handlingを実装し、[PR #176](https://github.com/hoytech/strfry/pull/176)がprotected eventを埋め込むrepostを拒否します。

### NotedeckがNIP-11リレー制限とAgentium機能を追加

[Notedeck](https://github.com/damus-io/notedeck)は、Damus teamによるnative desktop clientで、今週14件のPRをマージしました。[PR #1316](https://github.com/damus-io/notedeck/pull/1316)は[NIP-11](/ja/topics/nip-11/)（Relay情報ドキュメント）のRelay制限取得を追加し、すべてのoutbox RelayがRelay情報文書内の`max_message_length`と`max_subscriptions`を尊重するようにしました。実装には、background job処理、接続再試行のためのjitter付き指数backoff、custom HTTP Accept headerが含まれます。[PR #1312](https://github.com/damus-io/notedeck/pull/1312)はaccount切り替え後にDMが読み込めなくなることがあるバグを直し、[PR #1333](https://github.com/damus-io/notedeck/pull/1333)はerror時のbroadcast spamを防ぐため、multicast Relay通信にbackoff機構を追加しました。

Agentium subsystem（Notedeck内蔵のcoding agent UI、内部名「Dave」）には、clipboard画像paste、kind `31991`イベント経由で端末間同期する名前付きrun configuration（[NIP-33](/ja/topics/nip-33/)（パラメータ化置換可能イベント））、git worktree creator、sessionごとにbackendを選べるmodel pickerが追加されました（[PR #1336](https://github.com/damus-io/notedeck/pull/1336)）。[PR #1338](https://github.com/damus-io/notedeck/pull/1338)はheadless UI test向けに`egui_kittest`を統合し、[PR #1339](https://github.com/damus-io/notedeck/pull/1339)はclientごとの新しいcontact list作成数を追跡するdashboard cardを追加します。open状態の[PR #1314](https://github.com/damus-io/notedeck/pull/1314)は、ElectrumX lookup、SOCKS5 Tor routing、search bar統合を伴って、AmethystのNamecoin NIP-05解決をNotedeckへ移植します。

### diVineがE2Eテスト基盤とNIP-49インポートを備えたv1.0.6を出荷

[diVine](https://github.com/divinevideo/divine-mobile)は、[divine.video](https://divine.video)でVine archiveを復元するshort-form looping video clientで、127件のPRを取り込んだ[v1.0.6](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.6)を公開しました。このreleaseには、[NIP-49](/ja/topics/nip-49/)アカウントimport、外部[NIP-05](/ja/topics/nip-05/)サポート、multi-account処理、macOSとexperimental Linux build、ローカルストレージに支えられた再設計済みdraftとclip libraryが含まれます。

engineering面では、[PR #1928](https://github.com/divinevideo/divine-mobile/pull/1928)が、Docker backend stack（Relay、API、Blossom、Postgres、Redis、ClickHouse）に対するnative UI automation用Patrolを使った完全なE2E integration test基盤を追加します。auth journey testは5本あり、登録、検証、パスワードリセット、session expiry、token refreshをカバーします。[PR #2105](https://github.com/divinevideo/divine-mobile/pull/2105)は、動画読み込みをHLS優先からdirect MP4と自動HLS fallbackへ切り替え、30-60秒かかっていたロード時間をほぼ即時へ短縮しました。[PR #2076](https://github.com/divinevideo/divine-mobile/pull/2076)はhome feed API応答をSharedPreferencesへcacheし、cold start時に即表示できるようにします。[PR #2104](https://github.com/divinevideo/divine-mobile/pull/2104)は`ai-generated` content labelをfeed上でhiddenに強制し、[PR #2100](https://github.com/divinevideo/divine-mobile/pull/2100)はdiVineホスト動画のみを表示するsafety settingを追加します。HiveからDriftへのprofile cache migrationは、[PR #1881](https://github.com/divinevideo/divine-mobile/pull/1881)、[PR #1883](https://github.com/divinevideo/divine-mobile/pull/1883)、[PR #1903](https://github.com/divinevideo/divine-mobile/pull/1903)にまたがって進み、約1,074行のHive codeをDrift DAOで置き換えています。

### Vector v0.3.2がNIP-77 negentropy同期とMLS改善を出荷

[Vector](https://github.com/VectorPrivacy/Vector)は、[NIP-17](/ja/topics/nip-17/)（プライベートダイレクトメッセージ）と[NIP-44](/ja/topics/nip-44/)（暗号化ペイロード）を使うMLS group encryptionベースのprivacy-focused desktop messengerで、[v0.3.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.2)を公開しました。最大の変更は、MLS group sync向けのNIP-77 negentropy（[commit b06adf4](https://github.com/VectorPrivacy/Vector/commit/b06adf4af2673fb5ac5add01356999ea70628eac)）で、parallel bootにより見逃したメッセージへの追い付きが大幅に速くなります。このreleaseではさらに、Linux完全対応の再構築audio engine、blur preview付きimage spoiler、rich link preview付きclickable hyperlink、group admin向け`@everyone`を含む`@mention` ping、emoji shortcode autocomplete、group mute、既存reactionへのtap-to-react、cancel可能なfile uploadも追加されました。Vectorは[NIP-17](/ja/topics/nip-17/) group chat eventを明示的に除外しており（[commit 2179a51](https://github.com/VectorPrivacy/Vector/commit/2179a51c0449b3a70663a1573195b7945adf58ba)）、group暗号化にはMLSのみを使っています。

## リリース

### Route96 v0.5.0とv0.5.1

[Route96](https://github.com/v0l/route96)は、Blossomと[NIP-96](/ja/topics/nip-96/)（HTTPファイルストレージ）をサポートするmedia serverで、[v0.5.0](https://github.com/v0l/route96/releases/tag/v0.5.0)と[v0.5.1](https://github.com/v0l/route96/releases/tag/v0.5.1)を公開しました。v0.5.0では、自動AI labeling、label未付与uploadへのretroactive backfill、flag付きfile向けmoderation queue、EXIFベースのprivacy拒否、ban済みhash処理が加わります。

v0.5.1では、perceptual image hash、類似画像探索向けlocality-sensitive hashing、batch admin endpoint、agent tooling向けserverのBlossomおよびNIP-96 API surfaceを説明する公開済み[`SKILL.md`](https://github.com/v0l/route96/releases/tag/v0.5.1)が追加されました。[PR #58](https://github.com/v0l/route96/pull/58)はbackground workerを完全非同期なTokio taskへ移し、[commit 97b00a3](https://github.com/v0l/route96/commit/97b00a39e27b07053c2ad335dbf475bacba57bf8)はhot loopを避けるためのbackoffを追加します。

### Samizdat v1.0.0-alpha

[Samizdat](https://github.com/satsdisco/samizdat)は、[samizdat.press](https://samizdat.press)で利用できるlong-form reader兼publisherで、初のAndroid buildを[v1.0.0-alpha](https://github.com/satsdisco/samizdat/releases/tag/v1.0.0-alpha)として公開しました。アプリは、long-form Nostr記事をキュレーションしたPress pageで始まり、Press、Feed、Saved、Writeの各viewをbottom tab navigationで行き来します。Android buildは、Android Keystore暗号化とbiometric unlockによるnative key storage、`nostr:` URIと`samizdat.press` deep linkの処理、そしてdirect key importを要求せずAndroid app chooser（Amber、Primalなど）経由でsigner handoffをサポートします。pull-to-refresh、各画面サイズでのsafe-area処理、native share、clipboard、haptics、splash-screen統合も、web wrapperではなくAndroid shell側に組み込まれました。

[Commit d17308f](https://github.com/satsdisco/samizdat/commit/d17308f3c2e6020e14074fbb1c03a8f60f29a3e6)は、AmberとPrimal flow向けのintentベース[NIP-55](/ja/topics/nip-55/)署名を追加し、[commit e29dab8](https://github.com/satsdisco/samizdat/commit/e29dab84f7b58edd621f7b86ed7ca6458f965614)はJavaScript bridge workaroundを、`startActivityForResult`を使うnative Capacitor pluginへ置き換えました。このアプリはAndroid 7.0以上（API 24）を要求し、このalphaではdebug APKとして配布され、push notificationはまだありません。公開機能は現在signer appに依存し、`nsec` loginはローカル閲覧とaccount accessのみを扱います。

### Calendar by Form* v0.2.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar)は、[calendar.formstr.app](https://calendar.formstr.app)で利用できる[NIP-59](/ja/topics/nip-59/)（Gift Wrap）によるprivate event共有を備えた分散型calendar appで、[PR #38](https://github.com/formstr-hq/nostr-calendar/pull/38)を含む[v0.2.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.0)を公開しました。このreleaseは[NIP-52](/ja/topics/nip-52/)（カレンダーイベント）のrecurring event handlingを拡張し、v0.1.0でのsingle-event基盤を超える内容になっています。内部変更は、local event storage、signer handling、Android notification plumbingにも及びます。これは、先月のrepository migration後、Formstr organizationで稼働する2つ目のアクティブアプリです。

### Mostro v0.16.4

[Mostro](https://github.com/MostroP2P/mostro)は、Nostr上に構築されたP2P Bitcoin exchangeで、[v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4)を公開しました。[先週取り上げた](/ja/newsletters/2026-03-04-newsletter/)dispute session restore（[PR #599](https://github.com/MostroP2P/mostro/pull/599)）とauto-close（[PR #606](https://github.com/MostroP2P/mostro/pull/606)）修正もこのreleaseに入っています。今回新たに、[PR #625](https://github.com/MostroP2P/mostro/pull/625)はkind `38384`のuser rating eventへ`days` fieldを追加し、[PR #612](https://github.com/MostroP2P/mostro/pull/612)はそれらのrating eventへexpirationを追加し、[PR #614](https://github.com/MostroP2P/mostro/pull/614)はorder eventのexpirationを固定24時間ではなく設定値へ切り替えます。[PR #622](https://github.com/MostroP2P/mostro/pull/622)は、development-fee支払いの重複を防ぐidempotency checkを追加しました。

### Mostro Mobile v1.2.1

[Mostro Mobile](https://github.com/MostroP2P/mobile)は、Mostro P2P exchange向けFlutter clientで、11件の新機能と11件のbug fixを含む[v1.2.1](https://github.com/MostroP2P/mobile/releases/tag/v1.2.1)を公開しました。このreleaseでは、dispute chatでの暗号化マルチメディア表示（[PR #514](https://github.com/MostroP2P/mobile/pull/514)）、注文がterminal stateに達した際のdispute UI自動close（[PR #503](https://github.com/MostroP2P/mobile/pull/503)）、NWC wallet import向けQR scan（[commit 12eaee4](https://github.com/MostroP2P/mobile/commit/12eaee4d154fa31b07f82b96819de520e825aee6)）、フランス語翻訳、FCM push notification handlingが追加されました。[PR #496](https://github.com/MostroP2P/mobile/pull/496)は、bip340 dependencyをv0.2.0に固定してSchnorr signature padding bugを修正します。

### 0xchat v1.5.4

[0xchat](https://github.com/0xchat-app/0xchat-app-main)は、Cashu対応のTelegram風messaging clientで、Linux desktop向け修正に集中した[v1.5.4](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.4-release)を公開しました。AppImage dock icon、emoji rendering、context menu freeze、reply/copy UI hangが修正されています。このreleaseではimage upload問題とnpub.cash統合も修正されました。[PR #49](https://github.com/0xchat-app/0xchat-app-main/pull/49)は、何もしない3秒polling timerを削除して不要なUI rebuildをなくし、glassmorphic repaintを抑えます。また、event cache loadを並行実行し、Relay、contact、channel起動をblockしないようにすることでlogin初期化も詰まりなく進むようにしました。

### Keep v0.6.0

[Keep](https://github.com/privkeyio/keep-android)は、Android向けFROST threshold signerで、[NIP-55](/ja/topics/nip-55/)と[NIP-46](/ja/topics/nip-46/)をサポートし、[v0.6.0](https://github.com/privkeyio/keep-android/releases/tag/v0.6.0)と[v0.6.1](https://github.com/privkeyio/keep-android/releases/tag/v0.6.1)を公開しました。v0.6.0では、wallet descriptor coordinationとmanagement UI、biometric authentication付きbackup/restore flow（[PR #184](https://github.com/privkeyio/keep-android/pull/184)）、threshold shareからのnsec recovery（[PR #187](https://github.com/privkeyio/keep-android/pull/187)）、Rust UniFFIによるcross-platform animated QR frame生成（[PR #188](https://github.com/privkeyio/keep-android/pull/188)）、chain verification付き署名audit trail（[PR #189](https://github.com/privkeyio/keep-android/pull/189)）が追加されました。v0.6.1はlicenseをAGPL-3.0からMITへ変更しています（[PR #191](https://github.com/privkeyio/keep-android/pull/191)）。

### njump v0.3.0

[njump](https://github.com/fiatjaf/njump)は、[njump.me](https://njump.me)でNostr contentを閲覧するためのstatic gatewayで、`note1` code parsingの破壊的変更と基盤nostr library更新を含む[v0.3.0](https://github.com/fiatjaf/njump/releases/tag/v0.3.0)を公開しました。

### Roadstr v0.1.1

[Roadstr](https://github.com/jooray/roadstr)は、Nostrを使う分散型road event reporting appで、初のdemo releaseとなる[v0.1.1](https://github.com/jooray/roadstr/releases/tag/v0.1.1)を公開しました。このアプリはopenfreemap.orgのvector tileを使ってroad eventをmap上に表示します。

### Bitcredit v0.5.3

[Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core)は、Nostr transport layerと専用Relayを備え、[bit.cr](https://www.bit.cr/)で動作するe-bill applicationで、[v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3)を公開しました。[PR #846](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846)は、paymentとacceptance state向けにAPIへ`payment_actions`と`bill_state` fieldを追加し、[PR #849](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849)はanonymous signer向けの署名address handlingを修正します。

### OpenChat v0.1.0-alpha.3

[OpenChat](https://github.com/DavidGershony/openChat)は、Marmot protocolの.NET MLSとC# libraryの上に構築されたchat applicationで、[v0.1.0-alpha.3](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.3)を公開しました。このreleaseは、Amberと[NIP-46](/ja/topics/nip-46/) flow向けの外部signer support（[commit e568d97](https://github.com/DavidGershony/openChat/commit/e568d979fe15eead19172f2eb6f8cf26ca845247)）、crash windowでのデータ損失をなくすためMLS state persistenceをMLS serviceへ移す変更（[commit 4720bc8](https://github.com/DavidGershony/openChat/commit/4720bc8625136a0d5b0e23322bc0c50cd80577e8)）、新しいCI pipelineを通じたWindows、Linux、Android build公開を含みます。

### OpenSignal v1.0.0

[OpenSignal](https://github.com/turizspace/opensignal)は、Nostr向けKotlin Multiplatform trading copilotで、[v1.0.0](https://github.com/turizspace/OpenSignal/releases/tag/v1.0.0)を公開しました。このreleaseには、domain logic、chart rendering、Nostr認証とpublishing、Blossom [NIP-96](/ja/topics/nip-96/) upload support、ONNXベースAI inference hookをDesktopとAndroid shellにまたがって共通化したKMP moduleが含まれます。公開されたarchitectureには、chart screenshot analysis向けFastAPI AI service、model training pipeline、sizeとwarningを備えた構造化trade planを生成するrisk engineも含まれます。loginは生の`nsec`鍵か外部signerのどちらかを使え、出力フローはローカル解析止まりではなくNostr event公開で終わります。

## プロジェクトアップデート

### Formstr

[Formstr](https://github.com/formstr-hq/nostr-forms)は、Nostr上のGoogle Forms代替で、[PR #434](https://github.com/formstr-hq/nostr-forms/pull/434)（[commit e9c4fd5](https://github.com/formstr-hq/nostr-forms/commit/e9c4fd5dadfa0b83f1e87d7596eaf35f9fdb7da8)）をマージし、[NIP-49](/ja/topics/nip-49/)（秘密鍵暗号化）で暗号化した秘密鍵を使うsignup flowを追加しました。この変更以前、ユーザーがFormstrを使うには[NIP-07](/ja/topics/nip-07/) browser extensionか、生の`nsec`貼り付けが必要でした。新しいflowでは、key pairをclient側で生成し、ユーザーが選んだpasswordでNIP-49のscrypt + XChaCha20-Poly1305方式により秘密鍵を暗号化し、結果の`ncryptsec`文字列を保存します。これでユーザーはsigner extensionを入れなくてもpasswordだけで再loginできます。鍵管理は終始client側にとどまります。

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst)は、多機能なAndroid clientで、先週openだったNamecoinベース[NIP-05](/ja/topics/nip-05/)解決機能を含む4件のPRをマージしました。[PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734)は、`.bit`、`d/`、`id/`識別子向けに、ElectrumX経由で検閲耐性のあるNIP-05検証を追加します。AmethystがNIP-05 fieldでこれらのsuffixを検出すると、ElectrumX-NMC serverに名前のtransaction historyを問い合わせ、最新outputの`NAME_UPDATE` scriptを解析してNostr pubkeyを抽出し、36,000 block（Namecoinのexpiry window）より古い名前は拒否します。ElectrumX接続はTor有効時にSOCKS5経由へ回り、clearnet endpointと`.onion` endpointの間で動的にserver選択します。1時間TTLのLRU cacheが繰り返しblockchain queryを防ぎます。

[PR #1771](https://github.com/vitorpamplona/amethyst/pull/1771)は、このflowのrace conditionとresolver correctnessを修正します。[PR #1785](https://github.com/vitorpamplona/amethyst/pull/1785)は、新規ユーザーがsignup中に通常のNIP-05識別子かNamecoinバックのものからfollow listをimportできるようにし、[PR #1786](https://github.com/vitorpamplona/amethyst/pull/1786)はlookup先のElectrumX serverをユーザーが選べるcustom設定を追加します。

### nostr-idb

[nostr-idb](https://github.com/hzrd149/nostr-idb)は、IndexedDBにNostrイベントを保存するhelper methodを提供するlibraryで、[PR #6](https://github.com/hzrd149/nostr-idb/pull/6)をマージし、[NIP-91](/ja/topics/nip-91/)のAND tag filterをサポートしました。この変更は、クライアント側filter matchingにintersection semanticsを追加し、IndexedDB queryがリスト内のいずれか1つではなく、列挙されたすべてのtag valueを要求できるようにします。[PR #8](https://github.com/hzrd149/nostr-idb/pull/8)はlibraryを最新のNIP-DB interfaceへ更新し、続く[commit b49b3d3](https://github.com/hzrd149/nostr-idb/commit/b49b3d32c575ff8214dc3fb07675109c2a971972)はsubscribe deadlockを修正し、nostr-toolsをproduction dependencyから外しました。

### Pensieve

[Pensieve](https://github.com/andotherstuff/pensieve)は、ClickHouse analyticsを備えたarchive-first Nostr indexerで、[PR #8](https://github.com/andotherstuff/pensieve/pull/8)をマージし、entryごとのcache TTL強制とkeyごとのmiss coalescingを追加してAPI CPU spikeを抑えました。最もコストの高いtime-series endpoint（engagement stats、hourly activity、per-kind activity）は、同期的な再計算stormを起こす代わりに、server側10分TTLを使うようになりました。

### Blossom

[Blossom](https://github.com/hzrd149/blossom)は、分散型media-hosting protocolおよびserver stackで、BUD-11のauthorization更新を2件マージしました。[PR #91](https://github.com/hzrd149/blossom/pull/91)は任意authorizationを独立したBUDへ分離し、`x`タグと`server`タグの役割を明確化します。[PR #93](https://github.com/hzrd149/blossom/pull/93)はendpoint固有のauth挙動を整理し、upload検証向け`X-SHA-256` headerを正式化します。この2件のPRにより、auth logicはBUD-11へ整理統合され、upload、delete、media-management flowにおけるrequest hashingの曖昧さが取り除かれました。

## NIPアップデート

[NIPsリポジトリ](https://github.com/nostr-protocol/nips)の最近の変更:

**マージ済み:**

- **[NIP-91](/ja/topics/nip-91/)（フィルターのAND演算子）** ([PR #1365](https://github.com/nostr-protocol/nips/pull/1365)): tag filterにintersection semanticsを追加し、Relayが列挙されたすべてのtag valueを必要とするqueryに応答できるようにします。1つでも一致すればよい、ではなく、全部に一致する必要があります。tagが多いqueryでclient側post-filteringと帯域幅を減らします。

- **[NIP-66](/ja/topics/nip-66/)（Relay発見と稼働監視）: 防御的措置** ([PR #2240](https://github.com/nostr-protocol/nips/pull/2240)): [先週取り上げたoutbox benchmark作業](/ja/newsletters/2026-03-04-newsletter/)を受けて、この仕様はRelay監視データのunhappy pathに関する警告を追加しました。クライアントは機能のためにkind `30166`監視イベントを必須にしてはいけません。monitorは誤っていることも、古くなっていることも、悪意を持つこともあります。クライアントは情報源を突き合わせ、単一feedだけを根拠にユーザーのRelay graphの大半を切り捨てないようにする必要があります。

- **[NIP-39](/ja/topics/nip-39/)（プロフィール内の外部アイデンティティ）: kind 10011レジストリ整理** ([PR #2256](https://github.com/nostr-protocol/nips/pull/2256)): kind `10011`参照を仕様へ直接追加し、[先週取り上げた](/ja/newsletters/2026-03-04-newsletter/)Amethyst実装と整合させます。

**オープンPRとディスカッション:**

- **[NIP-70](/ja/topics/nip-70/)（保護イベント）: protected eventを埋め込むrepostを拒否** ([PR #2251](https://github.com/nostr-protocol/nips/pull/2251)): Relayが元イベントにNIP-70を適用しても、同じcontentを持つrepostを受け入れるなら、`-`タグに実効性はありません。このPRは、Relayがkind 6とkind 16のprotected event repostも拒否しなければならないという規則を追加します。[strfry PR #176](https://github.com/hoytech/strfry/pull/176)はすでにこれを実装しています。

- **[NIP-71](/ja/topics/nip-71/)（動画イベント）: 複数音声トラック** ([PR #2255](https://github.com/nostr-protocol/nips/pull/2255)): alternate track、言語variant、audio-only stream向けのaudio `imeta`タグを追加します。クライアントは動画ファイル自体を安定させたまま音声言語だけ切り替えたり、podcast風content向けに音声を別trackとして提供したりできます。

- **[NIP-11](/ja/topics/nip-11/)（Relay情報ドキュメント）と[NIP-66](/ja/topics/nip-66/)のRelay属性** ([PR #2257](https://github.com/nostr-protocol/nips/pull/2257)): Relay情報ドキュメントに構造化`attributes` fieldを追加し、clientやdiscovery toolに対して、現在のfree-text descriptionを超えるmachine-readable metadataを与えます。

## NIP Deep Dive: NIP-49（秘密鍵暗号化）

[NIP-49](/ja/topics/nip-49/)は、クライアントが秘密鍵をパスワードで暗号化し、その結果をbech32の`ncryptsec`文字列としてエンコードする方法を定義します。[Formstr](#formstr)は新しいsignup flowでNIP-49を使っています。

この形式は専用イベントkindには結び付いていません。クライアントは生の32-byte secp256k1秘密鍵から始め、ユーザーのパスワードからscryptで対称鍵を導出し、XChaCha20-Poly1305で鍵を暗号化し、その結果をbech32 `ncryptsec`文字列へ包みます。暗号化前に鍵が安全でない扱いを受けたことがあるかどうかは、1-byte flagに記録されます。

```json
{
  "id": "4d47f4f0a6f6edbc1bbd7f4e2a45ec68f27cba91d6c6ab5cf28d8d87b0f3d57e",
  "pubkey": "1f8b4c3e7b0f9451d4f9b8a7c6e5d4c3b2a1908f7e6d5c4b3a29181716151413",
  "created_at": 1741699200,
  "kind": 30078,
  "tags": [
    ["d", "encrypted-key-backup"],
    ["format", "ncryptsec"],
    ["encryption", "nip49"]
  ],
  "content": "ncryptsec1qgg9947rlpvqu76pj5ecreduf9jxhselq2nae2kghhvd5g7dgjtcxfqtd67p9m0w57lspw8gsq6yphnm8623nsl8xn9j4jdzz84zm3frztj3z7s35vpzmqf6ksu8r89qk5z2zxfmu5gv8th8wclt0h4p",
  "sig": "6a8f6e4b2d1901735f0ad4b6e8c1f3a579d0e2b4c6f8a1d3e5f7091b2c3d4e5f11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff"
}
```

上のJSONイベントは、アプリケーション層での例であって、NIP-49の要件ではありません。NIPが標準化するのは暗号化済み鍵形式です。クライアントは`ncryptsec`をローカル保存したり、アプリ固有ストレージ経由で同期したり、backup stringとしてexportしたりできます。パスワードは鍵導出前にUnicode NFKCへ正規化されるため、クライアントやplatformが違っても同じpasswordで一貫して復号できます。

1-byteの鍵セキュリティflagには3つの定義済み値があります。`0x00`は鍵の扱い履歴が不明、`0x01`は暗号化前に平文web formへ貼り付けるなど安全でない扱いが確認されている、`0x02`は安全な文脈で生成・暗号化され一度も露出していない、を意味します。クライアントはこの値を使って、既知のunsafe historyを持つ鍵をimportするときに警告を表示できます。

NIP-49は平文`nsec` exportより鍵をよく保護しますが、暗号強度はpasswordと設定されたscrypt costに依存します。`LOG_N`が高いほどoffline推測は難しくなりますが、正規の復号処理も遅くなります。仕様は、暗号文を集めるほど攻撃者がoffline crackで有利になるため、暗号化済み鍵をpublic Relayへ公開しないよう警告しています。比較すると、[NIP-46](/ja/topics/nip-46/)のremote signingはそもそも鍵を露出させず、[NIP-55](/ja/topics/nip-55/)のAndroid signingは鍵を専用signer app内に留めます。NIP-49は別の役割を埋めます。つまり、自分で鍵を管理するユーザー向けの持ち運び可能な暗号化backupです。

実装としては、signup用の[Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434)、ncryptsec backupとrestoreを備える[Amber](https://github.com/greenart7c3/Amber)、account importに対応した[diVine v1.0.6](#divineがe2eテスト基盤とnip-49インポートを備えたv106を出荷)、FROST share export向けの[Keep v0.6.0](#keep-v060)、そして[nsec.app](https://nsec.app)や[Alby](https://github.com/getAlby/hub)のような鍵管理toolがあります。

## NIP Deep Dive: NIP-70（保護イベント）

[NIP-70](/ja/topics/nip-70/)はprotected eventを定義します。イベントが`["-"]`タグを持つ場合、そのタグを尊重するRelayは、[NIP-42](/ja/topics/nip-42/)認証を要求し、かつ認証済みpubkeyがイベント著者と一致しない限り、そのイベントを拒否しなければなりません。

NIP-42のauth flowは次の通りです。Relayがランダム文字列を含む`AUTH` challengeを送り、クライアントはRelay URLとchallengeをタグに含む署名済みkind `22242`イベントで応答します。Relayは署名を検証し、auth event内pubkeyが公開しようとしているprotected eventのpubkeyと一致するかを確認します。一致しなければ、Relayは`restricted` message prefix付きでそのイベントを拒否します。

イベントcontent自体は依然として公開であり得ます。`-`タグが制御するのは、そのタグを尊重するRelayへ誰がそのイベントを公開できるかだけです。これは、[NIP-29](/ja/topics/nip-29/)（Relayベースのグループ）の半閉鎖feed、member-only Relay空間、その他、著者がRelay graph経由の再配布を制限したい場面に適しています。NIP-70は単一タグの慣例であり、新しいイベントkindではないため、既存のどのイベントkindにも`-`タグを付けられます。

```json
{
  "id": "cb8feca582979d91fe90455867b34dbf4d65e4b86e86b3c68c368ca9f9eef6f2",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1707409439,
  "kind": 1,
  "tags": [
    ["-"]
  ],
  "content": "hello members of the secret group",
  "sig": "fa163f5cfb75d77d9b6269011872ee22b34fb48d23251e9879bb1e4ccbdd8aaaf4b6dc5f5084a65ef42c52fbcde8f3178bac3ba207de827ec513a6aa39fa684c"
}
```

Relayが元イベントの第三者公開を防いでも、誰かがそのcontentをrepost内に再掲することはできます。[PR #2251](https://github.com/nostr-protocol/nips/pull/2251)はこれに対処し、protected eventを埋め込むkind 6とkind 16のrepostもRelayが拒否するよう要求します。[strfry PR #156](https://github.com/hoytech/strfry/pull/156)はprotected event向けNIP-42 auth handlingを加え、[strfry PR #176](https://github.com/hoytech/strfry/pull/176)はprotected contentを埋め込むrepostをblockします。

NIP-70が制御するのはRelayの振る舞いです。受信者は依然としてcontentを別の場所へコピーできますし、仕様もそう明記しています。`-`タグは、Relayに再公開拒否を求める機械可読シグナルを著者に与えます。比較すると、[NIP-62](/ja/topics/nip-62/)（Vanishリクエスト）は事後にRelayへデータ削除を求めますが、NIP-70は受信時点で不正な公開を防ぎます。両者は補完関係にあります。著者は拡散を抑えるためにイベントをprotectedとしてマークし、後で受理済みRelayからcontentを消したければ削除要求を出せます。

---

今週はここまでです。何か作っているものがある、あるいは共有したいニュースがあるなら、<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">[NIP-17](/ja/topics/nip-17/) DMで連絡してください</a>。Nostrでも見つけられます。

