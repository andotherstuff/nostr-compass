---
title: 'Nostr Compass #13'
date: 2026-03-11
translationOf: /en/newsletters/2026-03-11-newsletter.md
translationDate: 2026-04-23
draft: false
type: newsletters
---

Nostr Compassへようこそ。Nostrの週刊ガイドです。

**今週の内容:** [Shopstr](https://github.com/shopstr-eng/shopstr)と[Milk Market](https://github.com/shopstr-eng/milk-market)が、エージェント駆動コマース向けのMCPサーフェスを追加しました。一方で[OAuth Bunker](https://github.com/flox1an/oauth-bunker)、[Amber](https://github.com/greenart7c3/Amber)、[strfry](https://github.com/hoytech/strfry)は、[NIP-42](/ja/topics/nip-42/)（クライアントからrelayへの認証）に基づくrelay-authとprotected event対応を、アプリ、署名アプリ、relayソフトウェア全体に広げています。[Route96](https://github.com/v0l/route96)はAIラベリング、モデレーションキュー、perceptual hash、機械可読なサーバードキュメントを含む2つのリリースを出荷しました。すでにWebで動いている[Samizdat](https://github.com/satsdisco/samizdat)は最初のAndroid alphaを公開し、その後[NIP-55](/ja/topics/nip-55/)（Android署名アプリケーション）対応も追加しました。[Formstr](https://github.com/formstr-hq/nostr-forms)は[NIP-49](/ja/topics/nip-49/)（秘密鍵暗号化）によるサインアップを追加し、[Amethyst](https://github.com/vitorpamplona/amethyst)はNamecoinベースの[NIP-05](/ja/topics/nip-05/)（ドメイン認証）解決機能を出荷しました。[Mostro](https://github.com/MostroP2P/mostro)は[v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4)を公開し、NIPsリポジトリでは[NIP-91](/ja/topics/nip-91/)（フィルターのAND演算子）と[NIP-66](/ja/topics/nip-66/)（relay発見と稼働監視）向けの防御的ガイダンスがマージされました。

## ニュース

### ShopstrとMilk MarketがMCPコマースサーフェスを公開

[Shopstr](https://github.com/shopstr-eng/shopstr)はLightningとCashu決済を備えたP2Pマーケットプレイスで、[PR #234](https://github.com/shopstr-eng/shopstr/pull/234)（[commit 94ef7d1](https://github.com/shopstr-eng/shopstr/commit/94ef7d1a4519e8e0158668d13c8cb8684b1d46e2)）をマージし、APIキー認証付きのMCPサーバーを追加しました。変更には、エージェント発見用の`.well-known/agent.json`、MCPのオンボーディングとステータス用エンドポイント、注文作成と支払い確認ルート、専用の購入ツールと読み取りツール、APIキー向け設定画面が含まれます。[PR #236](https://github.com/shopstr-eng/shopstr/pull/236)では、メッセージ、住所、注文更新、商品仕様選択といった売り手側アクションも追加されました。[PR #235](https://github.com/shopstr-eng/shopstr/pull/235)のセキュリティ修正では、1回だけのSHA-256 APIキーハッシュを廃止し、ソルト付きPBKDF2を100,000回適用する方式へ置き換えています。

エージェントは[NIP-99](/ja/topics/nip-99/)（Classified Listings）の出品を読み取り、既存の[NIP-47](/ja/topics/nip-47/)（Nostr Wallet Connect）と[NIP-60](/ja/topics/nip-60/)（Cashu Wallet）の決済フローを使って、ページのスクレイピングやクライアント挙動の逆解析なしにチェックアウトまで進めます。

[Milk Market](https://github.com/shopstr-eng/milk-market)は、Nostr上の食品マーケットプレイスであり、[milk.market](https://milk.market)で公開されています。こちらも同じMCPとAPIキーの基盤を[commit da6c0b4](https://github.com/shopstr-eng/milk-market/commit/da6c0b499494b4e4861c4ff8a220e066c46285b3)で導入しました。[PR #10](https://github.com/shopstr-eng/milk-market/pull/10)は、定期注文、購入後の配送先変更、Stripeその他の法定通貨決済経路を含む複数マーチャント・複数通貨チェックアウト処理を追加します。続く[PR #11](https://github.com/shopstr-eng/milk-market/pull/11)では、新規インストール時にfailed relay publishesテーブルが作成されず、初回ロードで500エラーになる起動時データベース初期化バグを修正しました。エージェント向けインターフェースは、ShopstrではBitcoinネイティブ決済、Milk Marketでは法定通貨とBitcoinの混在決済の両方に対応します。

### Bunker、署名アプリ、relayへ広がるNIP-42 relay認証

[OAuth Bunker](https://github.com/flox1an/oauth-bunker)は、OAuthプロバイダーをNostr署名に橋渡しする[NIP-46](/ja/topics/nip-46/)（Nostr Connect）bunkerで、[NIP-07](/ja/topics/nip-07/)（ブラウザ拡張署名アプリ）ログイン、自動的な単一ID選択、削除されたIDのクリーンアップを追加しました（[commit f0c7683](https://github.com/flox1an/oauth-bunker/commit/f0c7683cb2374fd9a3ebd1b186055da8abd2c2ff)）。IDが1つしかない場合、bunkerはプロンプトを出さず自動でそれを選びます。IDを削除すると、ぶら下がったassignmentやconnectionも同時に除去されます。[Commit 6b8796c](https://github.com/flox1an/oauth-bunker/commit/6b8796c6c59c7d48dc1ede92d6de6bf54feb56cc)は、assignmentされたユーザー向けに`ALWAYS_ALLOWED_KINDS`設定を追加し、既定値としてアプリ固有データのkind `30078`を許可します。これにより、委任されたIDはイベントごとの承認なしにアプリ固有ストレージへ書き込めます。

[Amber](https://github.com/greenart7c3/Amber)は、Android向け主要な[NIP-55](/ja/topics/nip-55/)署名アプリであり、週内に4つのプレリリースを含む[v4.1.3-pre4](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3-pre4)を出荷しました。[PR #317](https://github.com/greenart7c3/Amber/pull/317)は、kind `22242`リクエスト向けの[NIP-42](/ja/topics/nip-42/) relay認証処理を追加します。実装では、relayごとの権限を追跡する新しいデータベースカラムが追加され、`(pkKey, type, kind, relay)`に一意インデックスが張られています。ユーザーには専用の認証画面が表示され、relay単位またはすべてのrelay対象のワイルドカード`*`スコープで許可・拒否を選んで保存できます。ワイルドカード権限を付与すると、あるkindに対するrelay固有エントリはすべて消去されます。[PR #318](https://github.com/greenart7c3/Amber/pull/318)はその後続として、複数イベントリクエスト画面を別画面遷移ではなく、composableカードでインライン表示するようリファクタリングしました。このリリースには、デフォルトプロフィールrelayの更新、bottom sheetでのリクエスト表示、MediaTekデバイスでのクラッシュを避けるためStrongBox keystoreを無効化する修正も含まれます。

relay側では、[strfry PR #156](https://github.com/hoytech/strfry/pull/156)が[NIP-70](/ja/topics/nip-70/)（Protected Events）向けのNIP-42認証処理を実装し、[PR #176](https://github.com/hoytech/strfry/pull/176)はprotected eventを埋め込んだリポストを拒否します。

### NotedeckがNIP-11 relay制限とAgentium機能を追加

[Notedeck](https://github.com/damus-io/notedeck)は、Damusチームによるネイティブデスクトップクライアントで、今週14件のPRをマージしました。[PR #1316](https://github.com/damus-io/notedeck/pull/1316)は[NIP-11](/ja/topics/nip-11/)（Relay Information Document）にあるrelay制限の取得を追加し、すべてのoutbox relayがrelay情報ドキュメントに記載された`max_message_length`と`max_subscriptions`を尊重するようにします。実装には、バックグラウンドジョブ処理、接続再試行用のjitter付き指数バックオフ、カスタムHTTP Acceptヘッダーが含まれます。[PR #1312](https://github.com/damus-io/notedeck/pull/1312)はアカウント切り替え後にDMが読み込めなくなることがあるバグを修正し、[PR #1333](https://github.com/damus-io/notedeck/pull/1333)はエラー時のbroadcast spamを防ぐため、multicast relay通信にバックオフ機構を追加します。

Agentiumサブシステム（Notedeckに内蔵されたコーディングエージェントUIで、内部名は「Dave」）には、クリップボード画像の貼り付け、kind `31991`イベントを介してデバイス間同期する名前付き実行設定（[NIP-33](/ja/topics/nip-33/) パラメータ化置換イベント）、git worktree作成機能、セッションごとにバックエンドを選べるモデルピッカーが追加されました（[PR #1336](https://github.com/damus-io/notedeck/pull/1336)）。[PR #1338](https://github.com/damus-io/notedeck/pull/1338)はヘッドレスUIテスト向けに`egui_kittest`を統合し、[PR #1339](https://github.com/damus-io/notedeck/pull/1339)はクライアント別の新規コンタクトリスト作成を追跡するダッシュボードカードを追加します。オープン中の[PR #1314](https://github.com/damus-io/notedeck/pull/1314)は、AmethystのNamecoin NIP-05解決機能を、ElectrumXルックアップ、SOCKS5経由のTorルーティング、検索バー統合付きでNotedeckへ移植します。

### diVine v1.0.6がE2Eテスト基盤とNIP-49インポートを出荷

[diVine](https://github.com/divinevideo/divine-mobile)は、[divine.video](https://divine.video)でVineアーカイブを復元する短尺ループ動画クライアントであり、127件のマージ済みPRを含む[v1.0.6](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.6)を出荷しました。このリリースでは[NIP-49](/ja/topics/nip-49/)アカウントインポート、外部[NIP-05](/ja/topics/nip-05/)サポート、複数アカウント管理、macOSおよび実験的Linuxビルド、ローカルストレージを基盤にした再設計済みのdraftsおよびclipsライブラリが追加されています。

エンジニアリング面では、[PR #1928](https://github.com/divinevideo/divine-mobile/pull/1928)が、Dockerバックエンドスタック（relay、API、Blossom、Postgres、Redis、ClickHouse）を相手にネイティブUI自動化を行うPatrolベースの完全なE2E統合テスト基盤を追加しました。5つの認証ジャーニーテストが、登録、認証、パスワードリセット、セッション期限切れ、トークン更新をカバーします。[PR #2105](https://github.com/divinevideo/divine-mobile/pull/2105)は動画読み込みをHLS優先から直接MP4優先へ切り替え、HLSには自動フォールバックします。これにより読み込み時間は30〜60秒からほぼ即時まで短縮されました。[PR #2076](https://github.com/divinevideo/divine-mobile/pull/2076)は、ホームフィードのAPIレスポンスをSharedPreferencesへキャッシュし、cold start時に即時表示できるようにします。[PR #2104](https://github.com/divinevideo/divine-mobile/pull/2104)は`ai-generated`コンテンツラベルをフィードで非表示扱いにし、[PR #2100](https://github.com/divinevideo/divine-mobile/pull/2100)はdiVineホスト動画だけを表示する安全設定を追加します。HiveからDriftへのプロフィールキャッシュ移行は、[PR #1881](https://github.com/divinevideo/divine-mobile/pull/1881)、[PR #1883](https://github.com/divinevideo/divine-mobile/pull/1883)、[PR #1903](https://github.com/divinevideo/divine-mobile/pull/1903)にまたがって継続しており、約1,074行のHiveコードをDrift DAOへ置き換えています。

### Vector v0.3.2がNIP-77 negentropy同期とMLS改善を出荷

[Vector](https://github.com/VectorPrivacy/Vector)は、[NIP-17](/ja/topics/nip-17/)（プライベートダイレクトメッセージ）と[NIP-44](/ja/topics/nip-44/)（暗号化ペイロード）を使ったMLSグループ暗号化ベースのプライバシー重視デスクトップメッセンジャーで、[v0.3.2](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.2)を出荷しました。目玉は、MLSグループ同期向けのNIP-77 negentropy（[commit b06adf4](https://github.com/VectorPrivacy/Vector/commit/b06adf4af2673fb5ac5add01356999ea70628eac)）で、parallel bootを用いて見逃したメッセージを大幅に速く取り込みます。リリースにはこのほか、Linux完全対応の再構築された音声エンジン、ぼかしプレビュー付き画像spoiler、リッチリンクプレビュー付きクリック可能ハイパーリンク、グループ管理者向け`@everyone`を含む`@mention` ping、絵文字shortcodeオートコンプリート、グループミュート、既存リアクションへのタップ反応、キャンセル可能なファイルアップロードも含まれます。Vectorは[NIP-17](/ja/topics/nip-17/)グループチャットイベントを明示的にフィルタし（[commit 2179a51](https://github.com/VectorPrivacy/Vector/commit/2179a51c0449b3a70663a1573195b7945adf58ba)）、グループ暗号化にはMLSのみを使います。

## リリース

### Route96 v0.5.0 と v0.5.1

[Route96](https://github.com/v0l/route96)は、Blossomと[NIP-96](/ja/topics/nip-96/)（HTTP File Storage）をサポートするメディアサーバーであり、[v0.5.0](https://github.com/v0l/route96/releases/tag/v0.5.0)と[v0.5.1](https://github.com/v0l/route96/releases/tag/v0.5.1)を出荷しました。v0.5.0は、自動AIラベリング、未ラベルアップロードへの遡及的バックフィル、フラグ付きファイル向けモデレーションキュー、EXIFベースのプライバシー拒否、禁止ハッシュ処理を追加します。

v0.5.1は、知覚画像ハッシュ、類似画像検索のためのlocality-sensitive hashing、バッチ管理者エンドポイント、そしてエージェントツール向けにサーバーのBlossomおよびNIP-96 API面を説明する公開[`SKILL.md`](https://github.com/v0l/route96/releases/tag/v0.5.1)を追加しました。[PR #58](https://github.com/v0l/route96/pull/58)はバックグラウンドワーカーを完全非同期のTokioタスクへ移し、[commit 97b00a3](https://github.com/v0l/route96/commit/97b00a39e27b07053c2ad335dbf475bacba57bf8)はhot loopを避けるためにバックオフを追加します。

### Samizdat v1.0.0-alpha

[Samizdat](https://github.com/satsdisco/samizdat)は、[samizdat.press](https://samizdat.press)で利用できる長文リーダー兼パブリッシャーであり、最初のAndroidビルドを[v1.0.0-alpha](https://github.com/satsdisco/samizdat/releases/tag/v1.0.0-alpha)で出荷しました。アプリは、キュレートされたNostr長文記事のPressページを起点に、Press、Feed、Saved、Writeの各ビューを下部タブで切り替えます。Androidビルドは、Android Keystore暗号化によるネイティブ鍵保存、`nostr:` URIと`samizdat.press` deep linkの処理、AmberやPrimalなどへのAndroidアプリチューザー経由の署名アプリ引き渡しを追加し、直接鍵インポートを不要にします。pull-to-refresh、画面サイズをまたぐsafe area処理、ネイティブ共有、クリップボード、ハプティクス、スプラッシュスクリーン統合も、単なるWebラッパーではなくAndroid shell側に移されています。

[Commit d17308f](https://github.com/satsdisco/samizdat/commit/d17308f3c2e6020e14074fbb1c03a8f60f29a3e6)は、AmberとPrimalフロー向けのインテントベース[NIP-55](/ja/topics/nip-55/)署名を追加し、[commit e29dab8](https://github.com/satsdisco/samizdat/commit/e29dab84f7b58edd621f7b86ed7ca6458f965614)はJavaScript bridge回避策を、`startActivityForResult`を使うネイティブCapacitorプラグインへ置き換えました。このalpha版のアプリはAndroid 7.0以上（API 24）が必要で、debug APKとして配布され、まだpush notificationはありません。公開は現在も署名アプリに依存しており、`nsec`ログインはローカル閲覧とアカウント利用向けです。

### Calendar by Form* v0.2.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar)は、[calendar.formstr.app](https://calendar.formstr.app)で利用できる、[NIP-59](/ja/topics/nip-59/)（Gift Wrap）によるプライベートイベント共有を持つ分散型カレンダーアプリです。[PR #38](https://github.com/formstr-hq/nostr-calendar/pull/38)を含む[v0.2.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.0)では、[NIP-52](/ja/topics/nip-52/)（Calendar Events）の定期イベント処理が拡張され、v0.1.0の単発イベント基盤を越えました。基礎となる変更は、ローカルイベント保存、署名アプリ処理、Android通知まわりにも及んでいます。これは、先月のリポジトリ移行に続くFormstr組織の2つ目のアクティブアプリケーションです。

### Mostro v0.16.4

[Mostro](https://github.com/MostroP2P/mostro)は、Nostr上に構築されたP2P Bitcoin取引所であり、[v0.16.4](https://github.com/MostroP2P/mostro/releases/tag/v0.16.4)を公開しました。[先週取り上げた](/ja/newsletters/2026-03-04-newsletter/)紛争セッション復元（[PR #599](https://github.com/MostroP2P/mostro/pull/599)）と自動クローズ（[PR #606](https://github.com/MostroP2P/mostro/pull/606)）の修正も含まれています。このリリースで新たに入ったのは、kind `38384`のユーザー評価イベントに`days`フィールドを追加する[PR #625](https://github.com/MostroP2P/mostro/pull/625)、同評価イベントに有効期限を追加する[PR #612](https://github.com/MostroP2P/mostro/pull/612)、注文イベントの有効期限を固定24時間ではなく設定値へ切り替える[PR #614](https://github.com/MostroP2P/mostro/pull/614)です。[PR #622](https://github.com/MostroP2P/mostro/pull/622)は、開発手数料の重複支払いを防ぐidempotencyチェックを追加しています。

### Mostro Mobile v1.2.1

[Mostro Mobile](https://github.com/MostroP2P/mobile)は、Mostro P2P取引所向けFlutterクライアントであり、11件の新機能と11件のバグ修正を含む[v1.2.1](https://github.com/MostroP2P/mobile/releases/tag/v1.2.1)を出荷しました。リリースには、紛争チャットでの暗号化マルチメディア表示（[PR #514](https://github.com/MostroP2P/mobile/pull/514)）、注文が終端状態へ達したときの紛争UI自動クローズ（[PR #503](https://github.com/MostroP2P/mobile/pull/503)）、NWCウォレットインポート用QRスキャン（[commit 12eaee4](https://github.com/MostroP2P/mobile/commit/12eaee4d154fa31b07f82b96819de520e825aee6)）、フランス語翻訳、FCM push notification処理が含まれます。[PR #496](https://github.com/MostroP2P/mobile/pull/496)は、bip340依存をv0.2.0へ固定してSchnorr署名パディングバグを修正しました。

### 0xchat v1.5.4

[0xchat](https://github.com/0xchat-app/0xchat-app-main)は、Cashu対応のTelegram風メッセージングクライアントであり、Linuxデスクトップ修正に集中した[v1.5.4](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.4-release)を出荷しました。AppImageのdock icon、絵文字描画、context menuフリーズ、返信・コピーUIのハングを修正しています。画像アップロード問題とnpub.cash統合も修正されました。[PR #49](https://github.com/0xchat-app/0xchat-app-main/pull/49)は、何もしていないのにglassmorphic再描画を強いていた3秒ポーリングタイマーを削除し、不要なUI再構築をなくしています。また、イベントキャッシュ読み込みを並行実行に変えることで、relay、contacts、channel起動を塞いでいたログイン初期化も解消しました。

### Keep v0.6.0

[Keep](https://github.com/privkeyio/keep-android)は、[NIP-55](/ja/topics/nip-55/)と[NIP-46](/ja/topics/nip-46/)に対応するAndroid向けFROST threshold signerで、[v0.6.0](https://github.com/privkeyio/keep-android/releases/tag/v0.6.0)と[v0.6.1](https://github.com/privkeyio/keep-android/releases/tag/v0.6.1)を出荷しました。v0.6.0には、wallet descriptorの調整と管理UI、生体認証付きバックアップ/復元フロー（[PR #184](https://github.com/privkeyio/keep-android/pull/184)）、threshold shareからのnsec復元（[PR #187](https://github.com/privkeyio/keep-android/pull/187)）、Rust UniFFI経由のクロスプラットフォームanimated QR frame生成（[PR #188](https://github.com/privkeyio/keep-android/pull/188)）、チェーン検証付き署名監査証跡（[PR #189](https://github.com/privkeyio/keep-android/pull/189)）が含まれます。v0.6.1はライセンスをAGPL-3.0からMITへ切り替えました（[PR #191](https://github.com/privkeyio/keep-android/pull/191)）。

### njump v0.3.0

[njump](https://github.com/fiatjaf/njump)は、[njump.me](https://njump.me)でNostrコンテンツを閲覧するための静的ゲートウェイであり、`note1`コード解析の破壊的変更と基盤nostrライブラリ更新を含む[v0.3.0](https://github.com/fiatjaf/njump/releases/tag/v0.3.0)を出荷しました。

### Roadstr v0.1.1

[Roadstr](https://github.com/jooray/roadstr)は、Nostrを使う分散型道路イベント報告アプリで、初のデモリリース[v0.1.1](https://github.com/jooray/roadstr/releases/tag/v0.1.1)を出荷しました。アプリはopenfreemap.orgのvector tileを使って道路イベントを地図上に表示します。

### Bitcredit v0.5.3

[Bitcredit](https://github.com/BitcreditProtocol/Bitcredit-Core)は、Nostrトランスポート層と専用relayを[bit.cr](https://www.bit.cr/)に持つ電子手形アプリケーションであり、[v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3)を出荷しました。[PR #846](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846)は支払いと承認状態のためにAPIへ`payment_actions`と`bill_state`フィールドを追加し、[PR #849](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849)は匿名署名者向けの署名アドレス処理を修正します。

### OpenChat v0.1.0-alpha.3

[OpenChat](https://github.com/DavidGershony/openChat)は、Marmotプロトコルの.NET MLSとC#ライブラリの上に構築されたチャットアプリケーションであり、[v0.1.0-alpha.3](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.3)を出荷しました。リリースには、Amberおよび[NIP-46](/ja/topics/nip-46/)フロー向け外部署名アプリ対応（[commit e568d97](https://github.com/DavidGershony/openChat/commit/e568d979fe15eead19172f2eb6f8cf26ca845247)）、クラッシュウィンドウ中のデータ損失をなくすためMLS状態永続化をMLSサービス内部へ移す変更（[commit 4720bc8](https://github.com/DavidGershony/openChat/commit/4720bc8625136a0d5b0e23322bc0c50cd80577e8)）、新しいCIパイプライン経由のWindows、Linux、Androidビルド公開が含まれます。

### OpenSignal v1.0.0

[OpenSignal](https://github.com/turizspace/opensignal)は、Nostr向けKotlin Multiplatform製トレーディングcopilotであり、[v1.0.0](https://github.com/turizspace/OpenSignal/releases/tag/v1.0.0)を出荷しました。このリリースは、ドメインロジック、チャート描画、Nostr認証と公開、Blossomの[NIP-96](/ja/topics/nip-96/)アップロードサポート、ONNXベースAI推論フックを、DesktopとAndroid shellをまたぐ共有KMPモジュールとしてまとめています。公開されたアーキテクチャには、チャートスクリーンショット解析用FastAPI AIサービス、モデル訓練パイプライン、サイズ計算と警告付きの構造化取引計画を生成するrisk engineも含まれます。ログインは生の`nsec`鍵か外部署名アプリのどちらにも対応し、出力フローはローカル分析で終わらずNostrイベント公開まで進みます。

## プロジェクト更新

### Formstr

[Formstr](https://github.com/formstr-hq/nostr-forms)は、Nostr上のGoogle Forms代替であり、[PR #434](https://github.com/formstr-hq/nostr-forms/pull/434)（[commit e9c4fd5](https://github.com/formstr-hq/nostr-forms/commit/e9c4fd5dadfa0b83f1e87d7596eaf35f9fdb7da8)）をマージして、[NIP-49](/ja/topics/nip-49/)（秘密鍵暗号化）による秘密鍵暗号化サインアップフローを追加しました。これ以前、Formstrを使うには[NIP-07](/ja/topics/nip-07/)ブラウザ拡張か、生の`nsec`貼り付けが必要でした。新しいフローではクライアント側で鍵ペアを生成し、ユーザーが選んだパスワードでNIP-49のscrypt + XChaCha20-Poly1305方式を使って秘密鍵を暗号化し、その結果の`ncryptsec`文字列を保存します。これでユーザーは署名拡張を入れなくても、パスワードだけで再ログインできます。鍵管理は終始クライアント側にとどまります。

### Amethyst

[Amethyst](https://github.com/vitorpamplona/amethyst)は、高機能Androidクライアントであり、[先週オープンだった](/ja/newsletters/2026-03-04-newsletter/)Namecoinベース[NIP-05](/ja/topics/nip-05/)解決機能を4件のPRで出荷しました。[PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734)は、`.bit`、`d/`、`id/`識別子向けにElectrumXを使った検閲耐性NIP-05検証を追加します。AmethystがNIP-05フィールド内でこれらのサフィックスを検出すると、ElectrumX-NMCサーバーへ名前のトランザクション履歴を問い合わせ、最新出力から`NAME_UPDATE`スクリプトを解析してNostr pubkeyを抽出し、36,000ブロックより古い名前は拒否します。これはNamecoinの有効期限ウィンドウに相当します。ElectrumX接続はTor有効時にSOCKS5経由で行われ、クリアネットと`.onion`エンドポイント間を動的に選択します。1時間TTLのLRUキャッシュが繰り返しのブロックチェーンクエリを防ぎます。

[PR #1771](https://github.com/vitorpamplona/amethyst/pull/1771)は、そのフローにおけるレースコンディションとresolverの正しさを修正しました。[PR #1785](https://github.com/vitorpamplona/amethyst/pull/1785)では、新規ユーザーが通常のNIP-05識別子またはNamecoinベースの識別子から、サインアップ時にフォローリストを取り込めるようになります。[PR #1786](https://github.com/vitorpamplona/amethyst/pull/1786)は、どのElectrumXサーバーで名前解決を行うかをユーザーが選べるカスタム設定を追加しました。

### nostr-idb

[nostr-idb](https://github.com/hzrd149/nostr-idb)は、IndexedDBへのNostrイベント保存を補助するライブラリであり、[PR #6](https://github.com/hzrd149/nostr-idb/pull/6)をマージして[NIP-91](/ja/topics/nip-91/)のANDタグフィルターをサポートしました。この変更はクライアント側フィルターマッチングへ積集合セマンティクスを追加し、IndexedDBクエリが列挙されたタグ値のうち1つではなく、すべてを要求できるようにします。[PR #8](https://github.com/hzrd149/nostr-idb/pull/8)はライブラリを最新のNIP-DBインターフェースへ更新し、続く[commit b49b3d3](https://github.com/hzrd149/nostr-idb/commit/b49b3d32c575ff8214dc3fb07675109c2a971972)は購読デッドロックを修正するとともに、nostr-toolsを本番依存から外しました。

### Pensieve

[Pensieve](https://github.com/andotherstuff/pensieve)は、ClickHouse分析を備えたarchive-first Nostr indexerであり、[PR #8](https://github.com/andotherstuff/pensieve/pull/8)をマージして、エントリ単位のキャッシュTTL強制とキー単位のmiss coalescingを追加しました。最もコストの高い時系列エンドポイント（engagement stats、hourly activity、per-kind activity）は、同期的な再計算ストームを起こす代わりに、10分間のサーバー側TTLを使うようになっています。

### Blossom

[Blossom](https://github.com/hzrd149/blossom)は、分散型メディアホスティングのプロトコル兼サーバースタックであり、BUD-11認可に関する2つの更新をマージしました。[PR #91](https://github.com/hzrd149/blossom/pull/91)は、オプション認可を独立したBUDへ切り出し、`x`タグと`server`タグの役割を明確化します。[PR #93](https://github.com/hzrd149/blossom/pull/93)は、エンドポイント固有の認可挙動を整理し、アップロード検証用`X-SHA-256`ヘッダーを正式化します。この2件のPRで、認可ロジックはBUD-11へ統合され、アップロード、削除、メディア管理フローにおけるリクエストハッシュ処理の曖昧さが解消されます。

## NIP更新

[NIPsリポジトリ](https://github.com/nostr-protocol/nips)への最近の変更:

**マージ済み:**

- **[NIP-91](/ja/topics/nip-91/)（フィルターのAND演算子）**（[PR #1365](https://github.com/nostr-protocol/nips/pull/1365)）: タグフィルターへ積集合セマンティクスを追加し、relayが列挙されたタグ値のどれか1つではなく、すべてを要求するクエリに応答できるようにします。タグの多いクエリで、クライアント側の後処理と帯域幅を減らします。

- **[NIP-66](/ja/topics/nip-66/)（relay発見と稼働監視）: 防御的措置**（[PR #2240](https://github.com/nostr-protocol/nips/pull/2240)）: [先週取り上げた](/ja/newsletters/2026-03-04-newsletter/)outbox benchmarkを受け、仕様はrelay監視データの不機嫌な経路に関する警告を追加しました。クライアントはkind `30166`監視イベントを前提に動作してはなりません。監視者は誤っていることも、古いことも、悪意あることもあります。クライアントは複数ソースを照合し、単一フィードだけでユーザーのrelay graphの大部分を切り落とさないことが求められます。

- **[NIP-39](/ja/topics/nip-39/)（プロフィール内の外部ID）: kind 10011レジストリ整理**（[PR #2256](https://github.com/nostr-protocol/nips/pull/2256)）: kind `10011`への参照を仕様へ直接追加し、[先週取り上げた](/ja/newsletters/2026-03-04-newsletter/)Amethyst実装と整合させます。

**オープンPRと議論:**

- **[NIP-70](/ja/topics/nip-70/)（Protected Events）: protected eventを埋め込んだリポストの拒否**（[PR #2251](https://github.com/nostr-protocol/nips/pull/2251)）: relayが元イベントにはNIP-70を強制しても、同じ内容を含むリポストを受け入れてしまえば、`-`タグは実質的な効果を持ちません。このPRは、relayがkind 6およびkind 16によるprotected eventのリポストも拒否しなければならないとするルールを追加します。[strfry PR #176](https://github.com/hoytech/strfry/pull/176)はすでにこれを実装しています。

- **[NIP-71](/ja/topics/nip-71/)（動画イベント）: 複数音声トラック**（[PR #2255](https://github.com/nostr-protocol/nips/pull/2255)）: 代替トラック、言語バリアント、音声のみストリーム向けのaudio `imeta`タグを追加します。クライアントは安定した動画ファイルを保ったまま音声言語だけを切り替えたり、ポッドキャストのようなコンテンツ向けに音声を別トラックとして配信したりできます。

- **[NIP-11](/ja/topics/nip-11/)（Relay Information Document）と[NIP-66](/ja/topics/nip-66/)のrelay属性**（[PR #2257](https://github.com/nostr-protocol/nips/pull/2257)）: relay情報ドキュメントに構造化された`attributes`フィールドを追加し、現在の自由文descriptionを超える機械可読メタデータをクライアントやdiscoveryツールへ提供します。

## NIP詳細解説: NIP-49（秘密鍵暗号化）

[NIP-49](/ja/topics/nip-49/)は、クライアントが秘密鍵をパスワードで暗号化し、その結果を`ncryptsec` bech32文字列としてエンコードする方法を定義します。[Formstr](#formstr)は新しいサインアップフローでNIP-49を使っています。

この形式は、専用のイベントkindに結びついているわけではありません。クライアントはまず生の32バイトsecp256k1秘密鍵を取り、scryptでユーザーのパスワードから対称鍵を導出し、XChaCha20-Poly1305で秘密鍵を暗号化してから、その結果をbech32の`ncryptsec`文字列へ包みます。1バイトのフラグは、その鍵が暗号化前に安全でない取り扱いを受けたことがあるかどうかを記録します。

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

上のJSONイベントはアプリケーションレベルの例であり、NIP-49そのものの必須要件ではありません。NIPが標準化するのは暗号化された鍵フォーマットです。クライアントは`ncryptsec`をローカルに保存してもよく、アプリ固有ストレージを通じて同期してもよく、バックアップ文字列としてエクスポートしてもかまいません。パスワードは鍵導出前にUnicode NFKCへ正規化されるため、同じパスワードならクライアントやプラットフォームをまたいでも一貫して復号できます。

1バイトの鍵セキュリティフラグには3つの定義済み値があります。`0x00`は鍵の取り扱い履歴が不明であること、`0x01`は暗号化前に平文Webフォームへ貼り付けたなど安全でない取り扱いがあったことが分かっていること、`0x02`は安全な文脈で生成・暗号化され、露出したことが一度もないことを意味します。クライアントはこれを使って、既知の不安全履歴を持つ鍵のインポート時に警告を表示できます。

NIP-49は平文`nsec`エクスポートより鍵を強く守りますが、その強さはパスワードと設定されたscryptコスト次第です。`LOG_N`値を高くすればオフライン総当たりは難しくなりますが、正当な復号も遅くなります。仕様は、攻撃者にオフライン解析用のciphertext収集機会を与えるため、暗号化済み鍵を公開relayへ載せないよう警告しています。比較対象として、[NIP-46](/ja/topics/nip-46/)リモート署名は鍵そのものを露出させず、[NIP-55](/ja/topics/nip-55/) Android署名は鍵を専用署名アプリ内に閉じ込めます。NIP-49は別の役割を担います。自分で鍵を管理するユーザー向けの、持ち運び可能な暗号化バックアップです。

実装例には、サインアップ向けの[Formstr PR #434](https://github.com/formstr-hq/nostr-forms/pull/434)、`ncryptsec`のバックアップと復元に対応する[Amber](https://github.com/greenart7c3/Amber)、アカウントインポートを追加した[diVine v1.0.6](#divine-v106がe2eテスト基盤とnip-49インポートを出荷)、FROST shareエクスポート向けの[Keep v0.6.0](#keep-v060)、そして[nsec.app](https://nsec.app)や[Alby](https://github.com/getAlby/hub)のような鍵管理ツールがあります。

## NIP詳細解説: NIP-70（Protected Events）

[NIP-70](/ja/topics/nip-70/)はprotected eventを定義します。イベントが`["-"]`タグを持つ場合、relayは[NIP-42](/ja/topics/nip-42/)認証を要求し、かつ認証済みpubkeyがイベント作成者と一致しない限り、それを拒否しなければなりません。

NIP-42認証フローは次のとおりです。relayはランダム文字列を含む`AUTH` challengeを送り、クライアントはrelay URLとchallengeをタグに含む署名済みkind `22242`イベントで応答します。relayは署名を検証し、認証イベント内のpubkeyが、公開しようとしているprotected event内のpubkeyと一致することを確認します。pubkeyが一致しない場合、relayは`restricted`メッセージ接頭辞とともにイベントを拒否します。

イベント内容自体は公開でも構いません。`-`タグが制御するのは、そのタグを尊重するrelayへ誰がそのイベントを公開できるかだけです。これは、[NIP-29](/ja/topics/nip-29/)（Simple Groups）の半閉鎖フィード、メンバー専用relay空間、その他relay graphを通じた再配布を制限したい文脈を対象にしています。NIP-70は新しいイベントkindではなく単一タグによる慣例なので、既存のどのイベントkindにも`-`タグを付けられます。

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

relayが元イベントの第三者公開を防いでも、誰かがその内容をリポストに包んで再公開することはできます。[PR #2251](https://github.com/nostr-protocol/nips/pull/2251)はこれに対処し、relayがkind 6とkind 16のprotected eventリポストも拒否しなければならないと定めます。[strfry PR #156](https://github.com/hoytech/strfry/pull/156)はprotected event向けNIP-42認証を追加し、[strfry PR #176](https://github.com/hoytech/strfry/pull/176)はprotected contentを埋め込んだリポストを遮断します。

NIP-70が制御するのはrelayの挙動です。受信者が別の場所に内容をコピーすることまでは防げませんし、仕様もそれを明記しています。`-`タグは、relayに再公開拒否の機械可読シグナルを与えます。比較すると、[NIP-62](/ja/topics/nip-62/)（Request to Vanish）はrelayに事後削除を求める一方、NIP-70は取り込み時点で未承認公開を防ぎます。両者は補完関係にあります。作成者は拡散を抑えるためにイベントをprotectedにでき、その後、受け入れてしまったrelayから削除したければ削除要求を送れます。

---

今週は以上です。何か作っているものがありますか。共有したいニュースはありますか。<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">[NIP-17](/ja/topics/nip-17/) DMでご連絡</a>いただくか、Nostr上で見つけてください。
