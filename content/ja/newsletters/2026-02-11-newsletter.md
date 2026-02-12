---
title: 'Nostr Compass #9'
date: 2026-02-11
translationOf: /en/newsletters/2026-02-11-newsletter.md
translationDate: 2026-02-12
draft: false
type: newsletters
---

Nostr Compassへようこそ。Nostrの週刊ガイドです。

**今週の内容:** Mostroが3年間の開発を経て初のパブリックベータを公開し、Nostr経由でP2P Bitcoin取引をモバイルに提供します。OpenSatsが第16波のBitcoin助成金を発表し、Nostr統合Cashuウォレットの開発を続けるMinibits Walletが更新助成金を受領しました。**Zapstoreが安定版1.0リリースに到達**し、分散型Androidアプリストアの成熟を示しています。Coracle 0.6.29がトピックとハイライトコメントを追加。Igloo Desktop v1.0.3がFrostr閾値署名のセキュリティ強化を出荷。Amber v4.1.2-pre1がFlowアーキテクチャに移行。Angorがv0.2.5に到達し、資金調達UIの刷新とNIP-96画像サーバー設定を追加。NostrPressがNostrプロフィールを静的ブログに変換するツールとして登場。AntiprimalがPrimalの独自キャッシュサーバーを標準Nostr NIPsに橋渡しする規格準拠ゲートウェイを出荷。Primal Androidが18件のPRをマージし、デュアルウォレットサポート、監査ログ、`lookup_invoice`メソッドでNWCインフラを拡張。diVineがAPI優先のビデオフィードを出荷。Marmot TypeScript SDKがリファレンスチャットアプリを独立リポジトリに分離し、ts-mls v2への移行を開始。NIPsリポジトリがNIP-45のHyperLogLog近似カウントをマージし、kind 0からidentityタグを抽出。vitorpamplonaによる一連の提案がkind 0メタデータイベントの体系的なスリム化を開始。新しいプロトコル提案として、NAT越え用のNostr Relay Connectと署名付きWeb主張用のNostr Web Tokensが登場。今週のディープダイブでは、NIP-45の新しいHyperLogLog近似カウント（クロスrelay event計測向け）と、NIP-96のHTTPファイルストレージプロトコル（Blossom移行が進む中で非推奨化）を取り上げます。

## ニュース

### Mostroが初のパブリックベータを公開

Nostr上に構築されたピアツーピアBitcoin取引所[Mostro](https://github.com/MostroP2P/mostro)が、[モバイルアプリv1.1.0](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0)をリリースしました。3年間の開発を経た初のパブリックベータです。このアプリは、Nostrを注文調整に、Lightningを決済に使用し、カストディアル仲介者なしでBitcoinの直接取引を可能にします。

今回のリリースでは、Androidでのバックグラウンド信頼性が改善されたプッシュ通知、問題発生時に診断データをキャプチャして共有できるオプションのログシステム、加算的初期化によるスムーズなrelay更新、国際化対応を含むフェーズ2のUIリファインメントが導入されています。アプリは[Zapstore](https://zapstore.dev)およびGitHubからの直接[ダウンロード](https://github.com/MostroP2P/mobile/releases/tag/v1.1.0)で入手可能です。

MostroはShopstrやPlebeian Marketに並ぶNostrネイティブコマースアプリケーションで、法定通貨とBitcoinの交換調整に特化している点が特徴です。基盤となる[Mostroデーモン](https://github.com/MostroP2P/mostro)がNostr relay経由で注文マッチングと紛争解決を処理します。

### OpenSats第16波Bitcoin助成金

[OpenSats](https://opensats.org/blog/sixteenth-wave-of-bitcoin-grants)が17のオープンソースプロジェクトへの助成金を発表しました。Nostr関連の注目点は、[NIP-60](/ja/topics/nip-60/)ウォレットイベントサポートとNutzap統合を備えたAndroid [Cashu](/ja/topics/cashu/)ウォレット[Minibits Wallet](https://github.com/minibits-cash/minibits_wallet)が更新助成金を受領したことです。MinibitsはNostrイベントを使用してecashトークンの状態を保存し、relay同期によりデバイス間でウォレットバックアップを移行可能にしています。

### NostrPress：Nostrプロフィールから静的ブログへ

[NostrPress](https://github.com/besoeasy/NostrPress)（[blog.besoeasy.com](https://blog.besoeasy.com)）は、Nostrプロフィールをどこにでもデプロイ可能な完全静的ブログに変換する新しいツールです。ユーザーは任意のクライアントからNostr上に記事を公開し、NostrPressがそれらのイベントからローカルメディアホスティングとRSSフィード付きのスタンドアロンWebサイトを生成します。

NunjucksテンプレートとJavaScriptで構築されたNostrPressは、プラットフォームロックインのないサイトを生成します。出力は任意の静的ファイルサーバー、GitHub Pages、Netlify、個人VPSでホスティング可能なプレーンHTML/CSSです。このツールは[Npub.pro](https://github.com/nostrband/nostrsite)や[Servus](https://github.com/servus-social/servus)に並ぶ、Nostrコンテンツを従来のWebサイトに変換するオプションとなります。

### Antiprimal：Primalキャッシュへの規格準拠ゲートウェイ

Alex GleasonとSoapboxチームによる新プロジェクト[antiprimal](https://gitlab.com/soapbox-pub/antiprimal)（[antiprimal.net](https://antiprimal.net)）は、Primalの独自キャッシュサーバーを標準Nostrプロトコルメッセージに橋渡しするWebSocketゲートウェイです。Primalはevent統計、コンテンツ検索、Web of Trust計算などの機能を`wss://cache.primal.net/v1`経由で提供していますが、アクセスには標準Nostrクライアントが使用できない非標準の`cache`フィールドを持つ独自メッセージフォーマットが必要です。Antiprimalは標準NIPリクエストをPrimalのフォーマットに変換し、レスポンスを元に戻します。

このゲートウェイは[NIP-45](/ja/topics/nip-45/) COUNTクエリ（リアクション数、リプライ数、リポスト数、zap数、フォロワー数）、[NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md)検索、[NIP-11](/ja/topics/nip-11/) relay情報、[NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md) Trusted Assertions（Primalの事前計算されたWeb of Trustデータ）をサポートします。コンパニオンボットがNIP-85 kind 30382（ユーザー統計）とkind 30383（eventエンゲージメント）のイベントを設定可能なrelayに公開します。プロジェクトはBun上のTypeScriptで構築され、Nostrifyライブラリを使用しています。2月6日に作成され、開発開始3日間で53コミットがあり、antiprimal.netで稼働中です。

### Ikaros：SignalとNostr向けAIエージェントメッセージングゲートウェイ

Soapboxチームによる新プロジェクト[Ikaros](https://gitlab.com/soapbox-pub/ikaros)は、AIエージェントがSignalとNostr暗号化DMの両方を通じて通信できるメッセージングゲートウェイです。このブリッジは[Agent Client Protocol](https://agentclientprotocol.org)（ACP）を使用して、ACP互換のAIコーディングアシスタントを実際のメッセージングネットワークに接続します。3つのpull requestが今週のプロジェクト初期ビルドを構成しています。

[PR #1](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/1)は、送受信サポート、明示的フラッシュ付きレスポンスバッファリング、`nsec`およびhex秘密鍵フォーマット、自動再接続付きマルチrelay公開、対話型セットアップウィザードを備えた完全な[NIP-04](/ja/topics/nip-04/)暗号化DMアダプターを実装しています。このアダプターはnostr-tools v2.23.0を使用し、ACP SDKをv0.14.1にアップデートしています。

[PR #2](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/2)は、セッション更新の競合状態によるサイレントメッセージドロップを修正しています。セッションがマップに登録される前に到着した受信通知がサイレントに失われていた問題を、登録完了後にリプレイするバッファリングで解決しました。[PR #3](https://gitlab.com/soapbox-pub/ikaros/-/merge_requests/3)は、Signalユーザーおよびグループの名前/UUIDメタデータをエージェントインタラクションに追加し、AIエージェントが誰とどのグループで会話しているかを認識できるようにします。このプロジェクトは新しい設計空間を開きます。Nostr DMでアドレス可能なAIエージェントがSignalからも到達可能であり、その逆も可能です。

### Kind 0スリム化キャンペーン

vitorpamplonaは今週一連のPRを公開し、kind 0（ユーザーメタデータ）イベントからデータを専用eventタイプに体系的に抽出することを提案しました。このキャンペーンは、時間の経過とともにkind 0イベントにほとんどのクライアントが使用しないフィールドが蓄積され、すべてのプロフィール取得のサイズが肥大化している問題に対処します。

[PR #2216](https://github.com/nostr-protocol/nips/pull/2216)（マージ済み）はidentityタグ（`i`タグ）をkind 0から新しいkind 10011に移動しました。これらのタグの採用が最小限であったためです。[PR #2213](https://github.com/nostr-protocol/nips/pull/2213)は[NIP-05](/ja/topics/nip-05/)検証をkind 10008に移動することを提案しており、これによりユーザーが複数のNIP-05識別子を持ち、NIP-05アドレスでイベントをフィルタリングできるようになります。[PR #2217](https://github.com/nostr-protocol/nips/pull/2217)はLightningアドレス（lud06/lud16）を新しいkindに抽出することを提案し、Lightning統合を持つクライアントのみが必要とするzap関連フィールドをすべてのkind 0ユーザーが運ぶことを止めます。

これらの提案は、[PR #1770](https://github.com/nostr-protocol/nips/pull/1770)を含むkind 0構造のより広い議論を再活性化しました。これはkind 0コンテンツの文字列化JSONを構造化タグに置き換える長年の提案です。

### NIP-70 Relayサポートが暗号化メッセージングセキュリティに不可欠

[Marmot](/ja/topics/marmot/)プロトコルのWhite Noise実装が、[NIP-70](https://github.com/nostr-protocol/nips/blob/master/70.md)（Protected Events）と[NIP-42](/ja/topics/nip-42/)（Authentication）のrelayサポートに[重大なギャップを特定しました](https://blog.jgmontoya.com/2026/02/10/nip70-relay-status.html)。テストの結果、Damus、Primal、nos.lolなどの主要パブリックrelayが、必要な認証チャレンジを開始する代わりに`blocked: event marked as protected`エラーでprotected eventsを拒否していることが判明しました。

これは重要なセキュリティ機能を破壊します。NIP-70は使用済みMLS KeyPackagesの安全な削除を可能にし、「今収集して後で復号化する」攻撃を防ぎます。relayサポートがなければ、暗号化メッセージングプロトコルは将来の鍵漏洩からユーザーを保護できません。White NoiseはNIP-70をデフォルトで無効化し、サポートするrelayを持つユーザー向けにオプションフラグを維持する対応を取りました。

**relayオペレーターへの呼びかけ：** 完全なNIP-42認証フローを実装してください。protected eventsを受信した際は、クライアントに所有権の証明を要求し、検証済みの書き込みを受け入れてください。認証なしでprotected eventsを拒否することは、暗号化メッセージングアプリケーションが依存するプロトコルセキュリティ保証を破壊します。

## リリース

### Coracle 0.6.29

hodlbodのWebクライアント[Coracle](https://github.com/coracle-social/coracle)（[coracle.social](https://coracle.social)）が[0.6.29](https://github.com/coracle-social/coracle/releases/tag/0.6.29)を出荷しました。このリリースではkind 9802ハイライトのトピックとコメントの表示が追加されました。新しいリストナビゲーション項目により、メインUIからユーザーキュレーションリストに素早くアクセスできます。内部的にはCoracleがWelshmanの新バージョンにアップグレードされ、Welshmanはcoracleのrelay管理とevent処理を支えるNostr共有ライブラリです。デフォルトrelayリストが更新され、Glitchtipエラートラッキングがコードベースから削除されました。

### Igloo Desktop v1.0.3

[FROST](/ja/topics/frost/)ベースの閾値署名者および鍵管理アプリケーション[Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop)が、大規模なセキュリティ強化を含む[v1.0.3](https://github.com/FROSTR-ORG/igloo-desktop/releases/tag/v1.0.3)を出荷しました。このリリースではIPC検証、Electron隔離、サーバーサイドリクエストフォージェリ防御のためのSSRF対応relayチェックが導入されています。新しいオンボーディングとシェアインポートフローで鍵配布が簡素化され、relay計画には正規化と優先度マージが含まれ、プリロードベースのElectron APIアーキテクチャがレンダラーとメインプロセス間のセキュリティ境界を改善しています。署名者キープアライブシステムが閾値署名セッションの安定性を維持し、リカバリーUXの改善で鍵復元の摩擦が軽減されました。

### Amber v4.1.2-pre1

Androidイベント署名者[Amber](https://github.com/greenart7c3/Amber)が[v4.1.2-pre1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.2-pre1)をリリースしました。v4.1.1で発生したrelay信頼スコア表示の欠落を修正し、Nostr以外の暗号化/復号化リクエストのJSON解析問題を解決し、アカウントモデルをLiveDataからFlowに移行してより予測可能な状態管理を実現しています。bunkerシークレットを完全UUIDに切り替え、Gradleプラグイン9にアップグレードしました。

### Mostro Mobile v1.1.0とDaemon v0.16.1

モバイルリリースの詳細は[上記ニュースセクション](#mostroが初のパブリックベータを公開)を参照してください。サーバー側では、[Mostroデーモン](https://github.com/MostroP2P/mostro)が[v0.16.1](https://github.com/MostroP2P/mostro/releases/tag/v0.16.1)を出荷し、起動時にNIP-01 kind 0メタデータの自動公開を追加しました（[PR #575](https://github.com/MostroP2P/mostro/pull/575)）。これによりデーモンはオンラインになった際にネットワークに自身のアイデンティティをアナウンスします。開発手数料の計算ドキュメントの修正（[PR #571](https://github.com/MostroP2P/mostro/pull/571)）も含まれています。

### Angor v0.2.5

BitcoinとNostr上に構築された分散型P2P資金調達プロトコル[Angor](https://github.com/block-core/angor)（[angor.io](https://angor.io)）が3つのマージ済みPRを含む[v0.2.5](https://github.com/block-core/angor/releases/tag/v0.2.5)を出荷しました。[PR #649](https://github.com/block-core/angor/pull/649)はFunds管理セクション（V2）を再設計し、個別のUTXOと投資ポジションを追跡する新しいインターフェースに置き換えました。[PR #651](https://github.com/block-core/angor/pull/651)はInvoiceViewを刷新し、ボタンスタイルの更新、閉じられるダイアログ、新しい「アドレスコピー」コマンド、アドレス監視のキャンセルサポート、投資フローの処理改善を含みます。[PR #652](https://github.com/block-core/angor/pull/652)は設定画面に[NIP-96](/ja/topics/nip-96/)（[仕様](https://github.com/nostr-protocol/nips/blob/master/96.md)）画像サーバーの設定機能を追加し、プロジェクト画像やドキュメントを処理するメディアアップロードエンドポイントをユーザーが選択できるようにしました。[v0.2.4](https://github.com/block-core/angor/releases/tag/v0.2.4)は前週に出荷されています。

### Ridestr v0.2.2とv0.2.3

分散型ライドシェアプラットフォーム[Ridestr](https://github.com/variablefate/ridestr)は、[先週取り上げた](/ja/newsletters/2026-02-04-newsletter/#ridestr-v020-roadflare-release)v0.2.0「RoadFlare Release」に続き、[v0.2.2](https://github.com/variablefate/ridestr/releases/tag/v0.2.2)（Bridge Payment Hotfix）と[v0.2.3](https://github.com/variablefate/ridestr/releases/tag/v0.2.3)で急速なイテレーションを続けました。v0.2.2ホットフィックスは、クロスミント[Cashu](/ja/topics/cashu/)ブリッジ決済が処理中または最終的に成功するにもかかわらず自動キャンセルされるバグに対処し、低速決済での早期ライドキャンセルを防止します。UIのちらつきと「現在地」ボタンのタッチヒットボックス破損も修正されています。v0.2.3では追加のバグ修正を出荷。両リリースともRidestr（ライダーアプリ）とDrivestr（ドライバーアプリ）の個別APKが含まれています。

### Nostr PHP 1.9.4

Nostrプロトコル用PHPヘルパーライブラリ[Nostr PHP](https://github.com/nostrver-se/nostr-php)（[nostr-php.dev](https://nostr-php.dev)）が[1.9.4](https://github.com/nostrver-se/nostr-php/releases/tag/1.9.4)を出荷し、リクエストクラスに設定可能な`timeout`プロパティを追加しました（[PR #106](https://github.com/nostrver-se/nostr-php/pull/106)）。開発者がrelay接続とメッセージリクエストにカスタムタイムアウト期間を設定でき、relayが無応答または応答が遅い場合の無期限ハングを防止します。

### Zapstore v1.0.0

Nostr上に構築されたパーミッションレスAndroidアプリストア[Zapstore](https://github.com/zapstore/zapstore/releases/tag/1.0.0)（[zapstore.dev](https://zapstore.dev)）が、数ヶ月のリリース候補を経て**安定版1.0リリースのマイルストーンに到達**しました。

1.0リリースには重要な安定性改善が含まれています。インストール完了後にDeleteが即座に表示されるインストールボタン状態の処理、展開可能な技術詳細付きのユーザーフレンドリーなエラーメッセージ、エフェメラルキーを使用してNostr経由で暗号化DMを送信する「問題を報告」ボタン。ポーリングとバッチ追跡付きの新しい更新画面、停滞した転送用のダウンロードウォッチドッグの改善、デバイスパフォーマンスに基づく動的同時ダウンロード制限、より頻繁なインストール済みパッケージ同期、改善されたバージョン比較ロジックも出荷されています。flutter_secure_storageの重大な問題が修正され、パッケージマネージャーのエッジケース処理も強化されました。

このマイルストーンは、Nostr初の専用アプリ配布プラットフォームの成熟を示しています。中央集権的なアプリストアのゲートキーピングなしに、開発者がAndroidアプリケーションを直接ユーザーに公開できるようにします。

### ZSP v0.3.1

[Zapstore](https://github.com/zapstore/zapstore)チームのGo CLIツール[ZSP](https://github.com/zapstore/zsp)が[v0.3.1](https://github.com/zapstore/zsp/releases/tag/v0.3.1)をリリースしました。ZSPはZapstoreの以前の公開ツールを置き換え、AndroidアプリのNostr relayへの署名とアップロードを担当します。GitHub、GitLab、Codeberg、F-Droid、またはローカルファイルからAPKを取得し、メタデータを解析し、Nostr event署名（秘密鍵、[NIP-46](/ja/topics/nip-46/) bunker、[NIP-07](/ja/topics/nip-07/)ブラウザ拡張機能経由）を行い、[Blossom](/ja/topics/blossom/)サーバーにアーティファクトをアップロードします。今回のリリースでは、ネットワーク接続なしでkeystoreリンクが可能な完全オフラインモード、プロトコル準拠のための`Content-Digest`ヘッダーのBlossomアップロード対応、F-Droidリポジトリからのarm64-v8a APK検出の修正、GitLabの末尾クエリパラメータ修正、設定用の完全な`.env`ファイルサポートが追加されました。

### Damus iOS 1.17

iOS Nostrクライアント[Damus](https://github.com/damus-io/damus)がバージョン1.17にアップデートされました（[PR #3606](https://github.com/damus-io/damus/pull/3606)）。エフェメラルリースリリース後に接続が閉じるRelayPoolの問題を修正し（[PR #3605](https://github.com/damus-io/damus/pull/3605)）、サブスクリプションが予期せずドロップする可能性がありました。タブ切り替え時にお気に入りタイムラインがイベントを表示しないバグも解決されています（[PR #3603](https://github.com/damus-io/damus/pull/3603)）。

### nak v0.18.3

Nostr army knife CLI [nak](https://github.com/fiatjaf/nak)が[v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3)を出荷し、3つの安定性修正を含みます。AUTHチャレンジタグがnilまたは短すぎる場合のパニック防止、解析値を使用する前のdateparserエラーチェック、`://`セパレータのないCashu mint URLの処理です。

### Mi：ブラウザベースのローカルRelay

[Mi](https://git.shakespeare.diy/npub1scvyzz02ayma34hesz62pdrd5nhsmxp74hjq8msmfs9khh3r3drsnw68d8/mi.git)（[mi.shakespeare.wtf](https://mi.shakespeare.wtf)）は、新しい[Shakespeare](https://shakespeare.wtf) MiniAppで、ユーザーのNostrイベントをIndexedDBにアーカイブするブラウザベースのローカルrelayです。Miは接続されたrelayからプロフィール（kind 0）、コンタクトリスト（kind 3）、relayリスト（kind 10002）、ウォレットイベントを取得してローカルに保存し、自分のデータへのオフラインアクセスを提供します。ReactとNostr-tools 2.15.0で構築されています。

### Agora v1.0.2

Soapboxチームによる分散型アクティビズムおよび資金調達プラットフォーム[Agora](https://gitlab.com/soapbox-pub/agora)（[agora.spot](https://agora.spot)）が、直接インストール可能なAndroid APK付き[v1.0.2](https://gitlab.com/soapbox-pub/agora/-/releases/v1.0.2)を出荷しました。これはCompassでのAgoraの初の言及で、1月17日にミッションステートメントとともにローンチされました。「自由のためのグローバル運動に参加しよう。国際的に現地の活動家に支援を送り、地域の行動に参加しよう。」

このプラットフォームは世界地図を中心に構成され、ユーザーは国別に閲覧し、位置タグ付き「アクション」（抗議、キャンペーン、コミュニティ組織化）を作成し、スレッドコメントで議論できます。すべてのコンテンツがNostr relay経由で伝播するため、中央サーバーを停止して調整を沈黙させることはできません。Agoraは多言語サポートとCI強制の翻訳パリティ、アップロード用の[Blossom](/ja/topics/blossom/)メディアサーバー統合、検索、グローバル/地域切り替え付きハッシュタグブラウジング、ユーザープロフィール、リアクションシステムをサポートしています。v1.0.2は現在のAndroidビルドで、APK直接ダウンロードで利用可能です。

### xonos v0.1.6

Bevyゲームエンジンで構築された実験的3D Nostrクライアント[xonos](https://codeberg.org/xonos/xonos)が[v0.1.6](https://codeberg.org/xonos/xonos/releases/tag/v0.1.6)を出荷しました。xonosはNostrイベントをテキスト読み上げ機能付き3D空間環境でレンダリングし、ソーシャルプロトコルデータが従来の2Dインターフェース外でどのように機能しうるかを探求しています。

## プロジェクトアップデート

### Primal AndroidがNWCインフラを拡張

[Primal Android](https://github.com/PrimalHQ/primal-android-app)は今週18件のPRをマージし、[先週開始した](/ja/newsletters/2026-02-04-newsletter/#primal-android-ships-nwc-encryption)NWCの構築を継続しました。[PR #883](https://github.com/PrimalHQ/primal-android-app/pull/883)は両ウォレット（Sparkおよび外部）にまたがるNWC接続サポートを追加し、[PR #879](https://github.com/PrimalHQ/primal-android-app/pull/879)は支払い状況を確認するための`lookup_invoice` NWCメソッドを実装しています。

[PR #880](https://github.com/PrimalHQ/primal-android-app/pull/880)はウォレットインタラクションのデバッグ用にNWCリクエスト-レスポンスの監査ログを追加。[PR #877](https://github.com/PrimalHQ/primal-android-app/pull/877)は`PrimalNwcService`にマルチアカウントサポートを追加し、複数プロフィールを持つユーザーが個別のウォレット接続を維持できるようにしています。[PR #882](https://github.com/PrimalHQ/primal-android-app/pull/882)は期限切れの予算ホールドの定期的クリーンアップを実装し、古い支払い予約がウォレット操作をブロックすることを防止します。

UI関連では、ウォレットアップグレード画面の再設計（[PR #889](https://github.com/PrimalHQ/primal-android-app/pull/889)）、ウォレットアップグレードFAQ（[PR #885](https://github.com/PrimalHQ/primal-android-app/pull/885)）、オンボーディング時のLightningアドレス設定（[PR #888](https://github.com/PrimalHQ/primal-android-app/pull/888)）、非Lightningタイプでzapトランザクションが通常の支払いとして表示される問題の修正（[PR #887](https://github.com/PrimalHQ/primal-android-app/pull/887)）が含まれます。

### diVineがAPI優先のビデオフィードを出荷

ショートフォームビデオクライアント[diVine](https://github.com/divinevideo/divine-mobile)は今週19件のPRをマージし、API優先アーキテクチャへの移行を進めました。[PR #1468](https://github.com/divinevideo/divine-mobile/pull/1468)がAPI優先のビデオフィードを導入し、[PR #1466](https://github.com/divinevideo/divine-mobile/pull/1466)がトレンド、最新、ホームAPIエンドポイントを追加。[PR #1433](https://github.com/divinevideo/divine-mobile/pull/1433)が効率的なフィードレンダリングのために特定のビデオコントローラーをインデックス化しています。

プロフィール処理では、[PR #1440](https://github.com/divinevideo/divine-mobile/pull/1440)が他のプロフィール表示にキャッシュ＋フレッシュパターンを実装し、データの鮮度を確保しながら読み込み時間を短縮しました。通知修正（[PR #1437](https://github.com/divinevideo/divine-mobile/pull/1437)）、コメントフローのリファクタリング（[PR #1431](https://github.com/divinevideo/divine-mobile/pull/1431)）、通知画面でのタブスワイプ（[PR #1388](https://github.com/divinevideo/divine-mobile/pull/1388)）も出荷されています。

### White Noise：キーリング統一とユーザー検索

[Marmot](/ja/topics/marmot/)プロトコルの[White Noise](https://github.com/marmot-protocol/whitenoise-rs)バックエンドは今週4件のPRをマージしました。2件のPRがキーリング処理を改善しています。[PR #468](https://github.com/marmot-protocol/whitenoise-rs/pull/468)が`WhitenoiseConfig`経由でキーリングサービス識別子を設定可能にし、[PR #475](https://github.com/marmot-protocol/whitenoise-rs/pull/475)がプラットフォームネイティブストアを持つ単一の`keyring-core`クレートで実装を統一し、断片化されたプラットフォーム固有コードを置き換えました。別途、[PR #470](https://github.com/marmot-protocol/whitenoise-rs/pull/470)がユーザー検索機能を追加しています。

### Marmot TSがリファレンスチャットアプリを分離

[Marmot](/ja/topics/marmot/) TypeScript SDK（[marmot-ts](https://github.com/marmot-protocol/marmot-ts)）が[PR #40](https://github.com/marmot-protocol/marmot-ts/pull/40)をマージし、組み込みリファレンスチャットアプリケーションを削除して独立リポジトリ[marmots-web-chat](https://github.com/marmot-protocol/marmots-web-chat)に分離しました。2月6日に作成された新リポジトリは、独自のCIパイプライン、タブ付きチャットビュー、独立ビルドシステムを持つMarmot TypeScript SDKのリファレンス実装です。この分離により、SDKはライブラリの関心事に集中でき、チャットアプリは独立してUXのイテレーションが可能になります。

オープンPR（[#41](https://github.com/marmot-protocol/marmot-ts/pull/41)）はmarmot-tsをts-mls v2.0.0に移行し、統一コンテキストオブジェクト、新しいメッセージ処理ユーティリティ（event作成、読み取り、デシリアライゼーション）、キーパッケージメタデータヘルパー、削除eventサポートを含む再設計されたAPIを提供します。

### Alby Hubアップデート

[Alby Hub](https://github.com/getAlby/hub)は今週5件のPRをマージしました。[PR #2049](https://github.com/getAlby/hub/pull/2049)がアプリストアインターフェースにAlby CLIを追加。[PR #2033](https://github.com/getAlby/hub/pull/2033)がトランザクションリストでの無効なzapデータの処理を修正し、[PR #2046](https://github.com/getAlby/hub/pull/2046)がLNClientインターフェースから未使用の`ListTransactions`メソッドを削除しました。

### NotedeckがダッシュボードとAgentiumを出荷

DamusのクロスプラットフォームNostrクライアント[Notedeck](https://github.com/damus-io/notedeck)は今週6件のPRをマージしました。[PR #1247](https://github.com/damus-io/notedeck/pull/1247)が初期ダッシュボードアプリを追加。[PR #1293](https://github.com/damus-io/notedeck/pull/1293)はAgentiumを導入し、Dave AIアシスタントをデュアルAIモードとシーンベースのエージェント管理を備えたシステムに変換するマルチエージェント開発環境です。[PR #1276](https://github.com/damus-io/notedeck/pull/1276)がSignalスタイルのキーバインド付きマルチラインメッセージコンポーザーを追加し、[PR #1278](https://github.com/damus-io/notedeck/pull/1278)がメディアパフォーマンスの改善を提供。注目のオープンPRには[outboxインフラ](https://github.com/damus-io/notedeck/pull/1288)と[NIP-34](/ja/topics/nip-34/) [Gitアプリ計画](https://github.com/damus-io/notedeck/pull/1289)が含まれます。

### Agoraが大規模UIオーバーホールを出荷

[Agora](https://gitlab.com/soapbox-pub/agora)はv1.0.2リリースと併せて今週7件のPRをマージしました。[PR #106](https://gitlab.com/soapbox-pub/agora/-/merge_requests/106)が最大規模で、設定、プロフィール編集、マップインタラクション、検索結果、コメントフィルタリング、Blossomサーバー管理にまたがる11のUIタスクを完了。未認証ユーザーのリアクションボタンを無効化し（以前はマップ上の投稿にリアクションしようとするとサイレント失敗していた）、日付線のマップパンニングを修正し、検索結果に太字マッチテキストを追加しました。

[PR #108](https://gitlab.com/soapbox-pub/agora/-/merge_requests/108)がフィード投稿下とスレッドページにコメント数を追加。[PR #107](https://gitlab.com/soapbox-pub/agora/-/merge_requests/107)がeventロード失敗時の自動リトライと、リトライ回数超過時の明示的リロードボタンを追加。[PR #104](https://gitlab.com/soapbox-pub/agora/-/merge_requests/104)がハッシュタグブラウジングのデフォルトをグローバルスコープに変更しました。以前の国別スコープデフォルトではゼロ結果になることが多かったためです。

[PR #109](https://gitlab.com/soapbox-pub/agora/-/merge_requests/109)がすべての言語の翻訳パリティをチェックするCIステップを追加し、キーに値が欠けている場合にビルドを失敗させます。[PR #110](https://gitlab.com/soapbox-pub/agora/-/merge_requests/110)がフィードの長いノートをクリップしてスクロールのリズムを保持し、[PR #111](https://gitlab.com/soapbox-pub/agora/-/merge_requests/111)がアクションへのコメント時に小フォントサイズが原因で発生するiOSモバイルズームの問題を修正しました。

### ClawstrがCLIとLightning Zapボタンを出荷

AIエージェントがNostr上でコミュニティを作成・管理するRedditインスパイアのプラットフォーム[Clawstr](https://gitlab.com/soapbox-pub/clawstr)は今週3件のPRをマージしました。[PR #11](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/11)がAIエージェントスキル定義のすべての手動nakコマンドを新しい`@clawstr/cli`パッケージ（`npx -y @clawstr/cli@latest`）に置き換え、手動JSONイベント構築をCLIコマンドに移行し、ウォレット操作（init、balance、zap、npc）と[NIP-50](/ja/topics/nip-50/)全文検索を追加しました。

[PR #13](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/13)が「For Humans」ドキュメントページと`ProfileZapDialog`コンポーネントを追加。zapボタンはユーザーにLightningアドレスが設定されている場合にプロフィールページに表示され、ログイン不要でLNURL-payを直接使用し、プリセットsats金額とQRコード表示を備えています。[PR #12](https://gitlab.com/soapbox-pub/clawstr/-/merge_requests/12)が`wallet sync`コマンドを文書化し、Lightningアドレスへの支払いがエージェントが明示的にウォレットを同期するまでNPCに保持される仕組みを説明しています。

## NIPアップデート

[NIPsリポジトリ](https://github.com/nostr-protocol/nips)への最近の変更：

**マージ済み：**

- **[NIP-45：HyperLogLog Relayレスポンス](https://github.com/nostr-protocol/nips/pull/1561)** - [NIP-45（Event Counting）](/ja/topics/nip-45/)がHyperLogLog（HLL）近似カウントをサポートするようになりました。relayはCOUNTレスポンスとともに256バイトのHLLレジスター値を返すことができます。クライアントは複数のrelayからこれらのレジスターをマージし、完全なeventセットをダウンロードすることなく近似カーディナリティを計算します。主なユースケースは、単一relayを信頼できるソースとして依存せずにフォロワー数やリアクション数を取得することです。リアクションeventが2つでも、256バイトのHLLペイロードより多くの帯域幅を消費します。クライアントは小さなカーディナリティの精度向上にHyperLogLog++補正を適用できます。

- **[NIP-39：Identity TagsのKind 0からの移動](https://github.com/nostr-protocol/nips/pull/2216)** - [NIP-39](/ja/topics/nip-39/)のidentity claimタグ（`i`タグ）がkind 0メタデータイベントから新しい専用kind 10011に抽出されました。根拠は、ほぼどのクライアントもこれらのタグをサポートしていないため、すべてのkind 0取得にサイズを追加するだけで価値を提供していなかったことです。これはvitorpamplonaによるkind 0抽出PRシリーズの最初です（[ニュースセクション](#kind-0スリム化キャンペーン)を参照）。

**オープンPRとディスカッション：**

- **[NIP-XX：Nostr Relay Connect（NRC）](https://github.com/nostr-protocol/nips/pull/2214)** - woikosが、パブリックランデブーrelay経由の暗号化トンネリングによるNostr relayへのアクセスプロトコルを提案しています。NATやファイアウォールの背後にあるrelay（ホームサーバーやモバイルデバイス上のパーソナルrelayを含む）へのアクセスを可能にします。トンネリングはkind 24891/24892イベントと[NIP-44](/ja/topics/nip-44/)暗号化を使用し、ランデブーrelayはトラフィックを復号化できません。実用的なアプリケーションとして、任意のNostrクライアントがローカルストレージ（IndexedDB、SQLite）をrelayエンドポイントとして公開し、クロスデバイス同期を実現できます。標準NIP-01セマンティクス（REQ、EVENT、CLOSE、COUNT）がトンネルを透過的に通過します。Go（ORLY Relay）とTypeScript（Smesh）にリファレンス実装が存在します。

- **[Nostr Web Tokens（NWT）](https://github.com/nostr-protocol/nips/pull/2187)** - pippellia-btcが、JSON Web Tokens（JWT）に触発された、Web当事者間で署名付き主張を伝達するためのNostrイベントフォーマットであるNostr Web Tokensを提案しています。NWTは[NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md)（HTTP Auth）と[Blossom認可イベント](/ja/topics/blossom/)の両方を表現でき、トークンの有効期間と方法にクライアントの柔軟性を提供します。リファレンスGoライブラリが利用可能です。[動画による説明](https://github.com/pippellia-btc/nostr-web-tokens)とNIP-98およびBlossom Authとの[詳細比較](https://github.com/pippellia-btc/nostr-web-tokens?tab=readme-ov-file#comparisons)がPRにリンクされています。

- **[NIP-47簡素化](https://github.com/nostr-protocol/nips/pull/2210)** - rolznzが[NIP-47（Nostr Wallet Connect）](/ja/topics/nip-47/)から`multi_`メソッドの削除を提案しています。実装が複雑で採用も進まなかったためです。このPRは暗号化と後方互換性の処理における重複も削減し、[先週のhold invoice追加](/ja/newsletters/2026-02-04-newsletter/#nip-updates)後の仕様をクリーンアップしています。

- **[NIP-05：独自Event Kindへの移動](https://github.com/nostr-protocol/nips/pull/2213)** - vitorpamplonaがNIP-05検証をkind 0から新しいkind 10008に移動することを提案し、ユーザーごとの複数NIP-05識別子とNIP-05アドレスによるフィルタリングを可能にします。kind 0スリム化キャンペーンの一環です。

- **[NIP-57：Kind 0からのLightningアドレス](https://github.com/nostr-protocol/nips/pull/2217)** - vitorpamplonaが[NIP-57](/ja/topics/nip-57/)に従いlud06/lud16（Lightningアドレス）をkind 0から専用event kindに抽出することを提案し、kind 0スリム化を継続しています。

- **[プロフィールハイパーカスタマイゼーション](https://github.com/nostr-protocol/nips/pull/2165)** - fiatjafが、現在のkind 0がサポートする範囲を超えた拡張プロフィールカスタマイゼーション機能を提案しています。

## NIPディープダイブ：NIP-45（Event Counting）とHyperLogLog

[NIP-45](/ja/topics/nip-45/)（[仕様](https://github.com/nostr-protocol/nips/blob/master/45.md)）は、クライアントがevent自体を転送せずにフィルターに一致するeventの数をrelayに問い合わせる方法を定義しています。今週マージされた[HyperLogLogサポート](https://github.com/nostr-protocol/nips/pull/1561)は、根本的な問題を解決する確率的データ構造を追加しました。複数の独立したrelayにまたがって物事を数える方法という問題です。

**問題点：**

単一relayでのeventカウントは単純です。COUNTリクエストを送信し、数値を受け取ります。ネットワーク全体でのカウントはより困難です。relay Aが50リアクション、relay Bが40リアクションを報告した場合、合計は90ではありません。多くのeventが両方のrelayに存在するためです。すべてのeventをダウンロードして重複排除しなければ、クライアントは正確な数を計算できません。

**HyperLogLog：**

HyperLogLog（HLL）は、固定量のメモリを使用してセット内のユニーク要素数を推定する確率的アルゴリズムです。NIP-45の実装は各1バイトの256レジスターを使用し、カウントされるevent数に関わらず正確に256バイトを消費します。このアルゴリズムは各event IDのバイナリ表現を調べ、先頭ゼロの位置を追跡することで動作します。IDが多くのゼロで始まるeventは統計的にまれであるため、その出現は大きなセットを示します。

**NIP-45での動作：**

COUNTリクエストに応答するrelayは、base64エンコードされたレジスター値を含む`hll`フィールドを含めることができます：

```json
["COUNT", "<subscription_id>", {"count": 4527, "hll": "<base64 encoded 256 bytes>"}]
```

クライアントは複数のrelayからHLL値を収集し、各レジスター位置で最大値を取ることでマージします。このマージされたHLLはrelay間のすべてのeventセットの和集合を表し、重複排除を自動的に処理します。最終的なカーディナリティ推定は、マージされたレジスターから計算されます。

**精度：**

256レジスターでの標準誤差は約5.2%です。真の数が1,000の場合、推定は通常948から1,052の間に収まります。より大きな数でも相対誤差は一定で、真の数が100,000の場合は約94,800から105,200と推定されます。HyperLogLog++補正は小さなカーディナリティ（約200未満）での精度を向上させ、基本アルゴリズムが過大評価する傾向を改善します。

**意義：**

ソーシャルメトリクス（フォロワー数、リアクション数、リポスト数）はソーシャルメディアクライアントの中核機能です。HLLなしでは、クライアントはカウントを中央集権化する形で単一の「信頼できる」relayに問い合わせるか、帯域幅を浪費してすべてのrelayからすべてのeventをダウンロードするしかありません。HLLにより、クライアントは実際のカウントに関わらず、relay当たり256バイトのオーバーヘッドで複数relayから適切な近似カウントを取得できます。リアクションeventが2つでも、完全なHLLペイロードより多くの帯域幅を消費します。

仕様は相互運用性のためにレジスター数を256に固定しています。すべてのrelayが、どのrelay実装を実行していても、クライアントがマージ可能なHLL値を生成します。この標準化により、クライアントはHLLサポートを一度実装すれば、それをサポートするすべてのrelayから恩恵を受けることができます。

**現在のステータス：**

このPRはfiatjafが公開し、今週のマージ前に数ヶ月にわたって議論されていました。relay実装はCOUNTハンドラーにHLL計算を追加する必要があります。クライアント実装はカウント集約ロジックにHLLマージを追加する必要があります。

## NIPディープダイブ：NIP-96（HTTPファイルストレージ）とBlossomへの移行

[NIP-96](/ja/topics/nip-96/)（[仕様](https://github.com/nostr-protocol/nips/blob/master/96.md)）は、NostrクライアントがHTTPメディアサーバー上でファイルをアップロード、ダウンロード、管理する方法を定義していました。現在は[Blossom](/ja/topics/blossom/)（BUDベースのメディアホスティング）に移行が推奨されていますが、Angor v0.2.5が[NIP-96サーバー設定を追加](#angor-v025)し、ZSP v0.3.1が[Blossomサーバーにアップロード](#zsp-v031)していることから、プロトコル移行の進行中が分かり、NIP-96は今週も関連性を持っています。

**NIP-96の動作原理：**

クライアントは`/.well-known/nostr/nip96.json`を取得してファイルサーバーの機能を発見します。API URL、サポートされるコンテンツタイプ、サイズ制限、利用可能なメディア変換が返されます：

```json
{
  "api_url": "https://file-server.example/api",
  "download_url": "https://cdn.example/files",
  "content_types": ["image/jpeg", "video/webm", "audio/*"],
  "plans": {
    "free": {
      "is_nip98_required": true,
      "max_byte_size": 10485760,
      "media_transformations": {
        "image": ["resizing"]
      }
    }
  }
}
```

アップロードするには、クライアントは[NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md)認可ヘッダー付きの`multipart/form-data` POSTをAPI URLに送信します。認可ヘッダーにはアップローダーのアイデンティティを証明する署名済みNostr eventが含まれます。サーバーはファイルURL、オリジナルおよび変換済みSHA-256ハッシュ、MIMEタイプ、寸法を含む[NIP-94](/ja/topics/nip-94/)ファイルメタデータ構造を返します：

```json
{
  "status": "success",
  "nip94_event": {
    "tags": [
      ["url", "https://cdn.example/files/<hash>.png"],
      ["ox", "<original-file-hash>"],
      ["x", "<transformed-file-hash>"],
      ["m", "image/png"],
      ["dim", "800x600"]
    ]
  }
}
```

ダウンロードは`<api_url>/<sha256-hash>`へのGETリクエストを使用し、画像リサイズ（`?w=320`）などのサーバーサイド変換のオプションクエリパラメータが利用可能です。削除はNIP-98認証付きDELETEを使用し、元のアップローダーのみが自分のファイルを削除できます。ファイルリストエンドポイントはユーザーのアップロードのページ分けされた結果を返します。

ユーザーは優先アップロードサーバーを宣言するkind 10096イベントを公開し、手動設定なしにクライアントが適切なサーバーを自動選択できるようにします。

**非推奨化の理由：**

NIP-96はファイルURLを特定のサーバーに紐付けていました。`files.example.com`がダウンした場合、そのサーバーのURLを参照するすべてのNostrノートがメディアを失います。サーバーがアドレスであり、そのアドレスは脆弱でした。

[Blossom](/ja/topics/blossom/)（Blobs Stored Simply on Mediaservers）はこれを反転させ、ファイルコンテンツのSHA-256ハッシュを正規の識別子とします。BlossomのURLは`https://blossom.example/<sha256>.png`のようになりますが、同じファイルをホストする任意のBlossomサーバーが同じハッシュパスで提供します。あるサーバーが消えた場合、クライアントは同じハッシュで別のサーバーに問い合わせることができます。コンテンツアドレッシングにより、デフォルトでデータがサーバー間で移行可能になります。

BlossomはAPIも簡素化しています。NIP-96はJSONレスポンス付きのマルチパートフォームアップロード、変換ポリシー、ディスカバリーエンドポイントを使用していました。BlossomはアップロードにプレーンなPUT、ダウンロードにGET、認可には署名付きNostr eventを使用し、HTTPヘッダーに依存しません。Blossom仕様はモジュール式ドキュメントに分割されています。BUD-01がサーバープロトコル、認可、取得をカバーし、BUD-02がブロブアップロード、BUD-03がユーザーサーバー、BUD-04がサーバー間のミラーリングをカバーしています。

非推奨化は2025年9月に[PR #2047](https://github.com/nostr-protocol/nips/pull/2047)で行われ、NIPsインデックスでNIP-96に「非推奨」のマークが付けられました。

**実践における移行：**

nostr.buildやvoid.catのようなサーバーはNIP-96をサポートし、Blossomエンドポイントを追加または移行しました。クライアントは様々な段階にあります。今週のAngor v0.2.5リリースはプロジェクト画像用にNIP-96サーバー設定を追加し、ZSP v0.3.1はプロトコル準拠の`Content-Digest`ヘッダー付きでBlossomサーバーのみにアーティファクトをアップロードしています。AmethystとPrimalはBlossomアップロードをサポートしています。残りのNIP-96実装が移行を完了するまで、両者の共存は続くでしょう。

**引き継がれるもの：**

Kind 10096サーバー設定イベントはBlossomサーバー選択に引き続き有用です。NIP-94ファイルメタデータ（kind 1063イベント）は、どのアップロードプロトコルで作成されたかに関わらず、ファイルプロパティを記述します。NIP-96がダウンロードURLに使用していたSHA-256ハッシングは、Blossomのコンテンツアドレッシングの基盤となりました。NIP-96の設計は、Blossomが何を簡素化したかを示しました。分散型ネットワーク上のメディアホスティングには、relayレイヤーの検閲耐性に匹敵するコンテンツアドレスストレージが必要だという教訓です。

---

今週は以上です。構築中のプロジェクトや共有したいニュースがあれば、<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">NIP-17 DMでお問い合わせください</a>。Nostrでもお待ちしています。
