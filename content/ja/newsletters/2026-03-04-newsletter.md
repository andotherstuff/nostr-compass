---
title: 'Nostr Compass #12'
date: 2026-03-04
translationOf: /en/newsletters/2026-03-04-newsletter.md
translationDate: 2026-03-04
draft: false
type: newsletters
---

Nostr Compassへようこそ。Nostrの週刊ガイドです。

**今週の内容:** [Marmot Development Kit](https://github.com/marmot-protocol/mdk)が暗号化メディアと多言語バインディングを含む[初の公開リリース](#marmot-development-kitが初の公開リリースを出荷)を出荷。[Nostrability](https://github.com/nostrability/outbox)が14種のrelay選択アルゴリズムにわたる[アウトボックスモデルベンチマーク](#アウトボックスモデルの検証)を公開。[Wisp](https://github.com/barrydeen/wisp)がTorと[NIP-55](/ja/topics/nip-55/)（Android署名アプリケーション）署名を備え、8日間で[アルファからベータ](#wispがアルファからベータへ)に到達。[NIP-91](#nipアップデート)（ANDフィルター）がマージ。[Vector v0.3.1](#vector-v031)がnegentropy同期を15倍のパフォーマンス向上とともに提供。本号にはNostr2月の5年間回顧録も収録し、3つのrelayにサービスするスペック書き換えから、Damus App Store爆発、メッシュネットワーキングとAIエージェント提案までのプロトコルの歩みを辿ります。

## ニュース

### アウトボックスモデルの検証

[Nostrability](https://github.com/nostrability/outbox)が、異なるrelay選択アルゴリズムが分散relayネットワークからイベントをどの程度適切に取得するかをテストする一連のアウトボックスモデルベンチマークを公開しました。プロジェクトは10日間で16件のPRと76件のコミットをマージし、[NIP-65](/ja/topics/nip-65/)（Relayリストメタデータ）実装戦略に関する最も徹底的な実証分析となった可能性があります。

ベンチマークは5言語15種のクライアントとライブラリにわたる実世界のフォローリストに対して14種のrelay選択アルゴリズムをテストしています。人気relayのみをクエリするベースラインアプローチではイベントの約26%を取得します。Thompson Samplingを用いた貪欲集合被覆は80-90%の再現率に達します。双曲線割引とEWMA relayレイテンシ追跡を使用するレイテンシ対応バリアントを追加すると、6つのテストプロファイルにわたって2秒時点での完全性が62-80%から72-96%に向上しました。

[NIP-66](/ja/topics/nip-66/)（Relayモニタリング）のデッドrelayフィルタリングは大きな影響をもたらしました。[nostr.watch](https://nostr.watch)の稼働状況データに基づくrelay候補の事前フィルタリングにより、デッドrelayの40-64%が除外され、relay成功率が30%から75-85%に倍増しました。フィード読み込み時間は39%短縮されました（10プロファイルで40秒から24秒に）。EOSE-raceシミュレーションでは、EOSEプラス200msの猶予期間を待つことで、最初のrelayの完了時に停止するよりも完全性が向上することが判明しました。

relay経路設定を完全に書き換えられないクライアント向けに、「ハイブリッドアウトボックスエンリッチメント」アプローチがあります。既存のハードコードされたアプリrelayの上に著者ごとのアウトボックスクエリを追加します。このハイブリッドは26%のベースラインに対して80%の1年間イベント再現率を達成し、レガシーrelayアーキテクチャを持つクライアントへの移行パスを提供します。

### ContextVMがMCP NIPを提出しエフェメラルGift Wrapを出荷

[ContextVM](https://contextvm.org)はNostrと[Model Context Protocol](https://modelcontextprotocol.io/)を橋渡しするプロトコルで、今週[NIPsリポジトリ](https://github.com/nostr-protocol/nips)に2件の提案を提出しました。[PR #2246](https://github.com/nostr-protocol/nips/pull/2246)はCVMをエフェメラルkind 25910イベントを使用してNostr上でMCP JSON-RPCメッセージを転送するための慣例として形式化します。[PR #2245](https://github.com/nostr-protocol/nips/pull/2245)は[NIP-59](/ja/topics/nip-59/)（Gift Wrap）をエフェメラルkind（21059）で拡張し、[NIP-01](/ja/topics/nip-01/)（基本プロトコルフロー）のエフェメラルセマンティクスに従って、relayが配信後にラップされたメッセージを破棄できるようにします。

エフェメラルgift wrap慣例はContextVM SDK v0.6.xリリースファミリーの[CEP-19](https://docs.contextvm.org/spec/ceps/cep-19/)として出荷されました。[SDK実装](https://github.com/ContextVM/sdk)はOPTIONAL（両方のkindを受け入れてピア機能を自動検出）、EPHEMERAL（kind 21059のみ）、PERSISTENT（kind 1059のみ）の3つの設定を持つ`GiftWrapMode`列挙型を追加します。AIツール呼び出しでは、エフェメラルモードはrelayに中間リクエスト-レスポンストラフィックを保存することを回避し、ストレージコストとプライバシー露出の両方を削減します。

独立した運営者から新しいパブリックMCPサーバーがネットワーク上に出現し、Wolfram Alphaクエリサーバーも含まれます。ContextVMチームはv0.6.xリリースサイクルとともにCEP-15（共通ツールスキーマ）とCEP-17（サーバーrelayリスト公開）を公開しました。

### Marmot Development Kitが初の公開リリースを出荷

[MDK](https://github.com/marmot-protocol/mdk)（Marmot Development Kit）は[Pika](https://github.com/sledtools/pika)と[White Noise](https://github.com/marmot-protocol/whitenoise)にわたる[Marmot](/ja/topics/mls/)暗号化メッセージングを支えるRustライブラリで、初の公開リリースとして[v0.6.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.6.0)を出荷しました。200件以上のPRがこのバージョンにマージされ、6人の新しいコントリビューターが参加しました。

このリリースには暗号化メディアサポート（MIP-04）とHKDFシード導出（MIP-01 v2）、決定論的コミットレース解決（MIP-03）、暗号化ローカルストレージ、Marmotコミットとプロポーザルのための管理者認可バリデーション、プロトコル拡張性のためのGREASEサポートが含まれます。Kotlin、Python、Ruby、Windows向けのバインディングがAndroidクロスコンパイルとともに出荷されます。ライブラリはセキュリティアドバイザリ修正とメモリ内の機密値をゼロ化する`Secret<T>`型を含むOpenMLS 0.8.0にアップグレードされています。

コンパニオンプロトコル変更（[MIP-03](https://github.com/marmot-protocol/marmot/pull/48)）はkind 445メッセージの[NIP-44](/ja/topics/nip-44/)（暗号化ペイロード）暗号化をChaCha20-Poly1305に置き換えました。NIP-44は仕様上UTF-8文字列入力を要求するため、標準的なTypeScript Nostrライブラリを通じて生のMarmotメッセージバイトを渡すことが不可能でした。代替方式はMarmotエクスポーターシークレットから直接キーを導出します。この破壊的変更は[コアスペック](https://github.com/marmot-protocol/marmot/pull/48)、[MDK](https://github.com/marmot-protocol/mdk/pull/208)、[TypeScript SDK](https://github.com/marmot-protocol/marmot-ts/pull/54)にわたる協調的なアップデートを必要としました。

[marmot-ts](https://github.com/marmot-protocol/marmot-ts)はhzrd149がメンテナンスするTypeScript実装で、4件のPRをマージし独自の破壊的API変更を含みます。[包括的アップデート](https://github.com/marmot-protocol/marmot-ts/pull/52)はcreate/publish/rotateライフサイクル用のキーパッケージマネージャー、`sendChatMessage`コンビニエンスメソッド、参加なしの招待プレビュー（`readInviteGroupInfo`）、前方秘密性ローテーションの自己アップデート、構造化デバッグログを追加しました。グループ復号APIは`readGroupMessage`から`decryptGroupMessage`に変更され、より豊富な結果バリアント（processed/skipped/rejected/unreadable）を持ちます。gzuuusはNIP-65 relayサポートとMIP-00に準拠したラストリゾートキーパッケージ処理を含むサンプルクリーンアップに貢献しました。

[White Noise CLI](https://github.com/marmot-protocol/whitenoise-rs)（`wn`）はモバイルアプリと新しいTUIの両方を支えるRustバックエンドで、10日間で16件のPRをマージしました。署名者ライフサイクル処理がRAAIスコープガードによるキャンセルセーフティ（[PR #538](https://github.com/marmot-protocol/whitenoise-rs/pull/538)）を獲得し、中断された操作が署名者の状態をリークする可能性のあるバグのクラスを修正しました。ログインは必要なrelayリスト（kind 10002/10050/10051）が欠落している場合にブロックするようになり（[PR #515](https://github.com/marmot-protocol/whitenoise-rs/pull/515)）、giftwrapサブスクリプションはinboxリストが不在の場合に[NIP-65](/ja/topics/nip-65/) relayにフォールバックします（[PR #518](https://github.com/marmot-protocol/whitenoise-rs/pull/518)）。デバッグモード（[PR #528](https://github.com/marmot-protocol/whitenoise-rs/pull/528)）はデータベースクエリとMLSラチェットツリーの検査をJSON出力として公開します。その他の修正は、署名者の再登録後のサブスクリプション回復、ウェルカムメッセージのキャッチアップタイミング、relayフィルターバリデーション、ユーザー検索半径制限に対応しました。

Marmotは今週、コアのRustスタック以外でも大きな拡大を見せました。[White Noise TUI](https://github.com/marmot-protocol/wn-tui)はWhite Noiseメッセージングスタックへのターミナルベースのインターフェースで、3月3日にローンチしました。`wn` CLIをサブプロセスとしてラップし、そのJSON出力をElmにインスパイアされた単方向アーキテクチャでレンダリングし、未読インジケーター付きのマルチ会話ナビゲーション、グループ作成とメンバー検索、リアルタイムメッセージストリーミング、ターミナルからの絵文字リアクションを提供します。

[DavidGershony](https://github.com/DavidGershony)はRustツールチェーンの階層化アーキテクチャを反映した完全なC# Marmotスタックを公開しました。[dotnet-mls](https://github.com/DavidGershony/dotnet-mls)はC#でMLS RFC 9420暗号プリミティブを実装します。[marmot-cs](https://github.com/DavidGershony/marmot-cs)はその上にNostr relayトランスポートを追加し、MDKのC#相当として機能します。[OpenChat](https://github.com/DavidGershony/openChat)は.NET 9とAvalonia UIで構築されたクロスプラットフォームデスクトップアプリで、NIP-44 DM、Marmotグループ暗号化、[NIP-46](/ja/topics/nip-46/)（Nostr Connect）リモート署名、マルチrelayステータスインジケーターを備えた動作するチャットクライアントに両者を統合します。

[MDK PWA Reference](https://github.com/zerosats/mdk-pwa-reference)はMarmot暗号化アプリケーションを構築するためのProgressive Web Appテンプレートを提供し、グループチャットへのAIエージェント参加とArkadeウォレットインフラを通じたBitcoin支払いの実験的サポートを含みます。

### Wispがアルファからベータへ

[Wisp](https://github.com/barrydeen/wisp)は新しいAndroid Nostrクライアントで、2月24日の[初のアルファ](https://github.com/barrydeen/wisp/releases/tag/v0.1.0-alpha)から3月3日の[v0.3.4-beta](https://github.com/barrydeen/wisp/releases/tag/v0.3.4-beta)まで、8日間で19リリース、115件のマージ済みPR、276件のコミットを生み出しました。

機能の軌跡は、ほとんどのクライアントが到達するのに数か月かかる領域をカバーしています。v0.1.0はoutbox/inbox relayモデルサポートとオンボーディングフローを搭載して出荷されました。v0.1.3までにクライアントはAmber向けの[NIP-55](/ja/topics/nip-55/)インテントベース署名、`.onion` relay接続用の組み込みTor SOCKS5プロキシ、[NIP-47](/ja/topics/nip-47/)（Nostr Wallet Connect）を備えました。v0.2.0はミュートリストフィルタリングとカスタム絵文字サポートでベータに昇格し、v0.2.4はコンテンツ警告オーバーレイを追加しました。v0.3.xシリーズはノート向けの[NIP-13](/ja/topics/nip-13/)プルーフオブワーク、永続設定によるバックグラウンドPoWマイニング、`.onion` relayストレージ、ミュートスレッド通知を導入しました。

Google ML Kitによるオンデバイス翻訳は、最初のモデルダウンロード後はネットワークアクセスなしでローカルに実行されます。インタラクティブなソーシャルグラフ可視化は、ピンチズームナビゲーションとプロフィール検査を備えた約30fpsのvelocity Verlet物理シミュレーションを使用します。

## リリース

### Vector v0.3.1

Marmot暗号化メッセージングアプリの[Vector](https://github.com/VectorPrivacy/Vector)が、グループ管理の改善とパフォーマンス作業を含む[v0.3.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.3.1)を出荷しました。マルチ管理者グループ、一括招待、npubによる招待、グループアバターがコラボレーション機能を拡張します。Androidバックグラウンド通知がインラインの返信と既読マークアクションをサポートするようになりました。

[Negentropy](/ja/topics/negentropy/)ベースの決定論的同期がオフライン中に見逃されたメッセージを含む完全な会話履歴を取得します。音声テキスト変換がAndroidでGPUアクセラレーションにより再構築されました。ファイル添付処理がダウンロード進捗、再試行ステート、ディレクトリのzip送信、全体にわたるライブ進捗インジケーターで刷新されました。起動時間、画像処理、オーディオ再生、一般的なUIレスポンシブネスにわたってパフォーマンスが15倍以上向上しました。アプリインストールサイズは3分の1以上削減され、フロントエンドは約半分に縮小されました。32ビットARM Androidサポートが追加されました。

### Alby Hub v1.21.5

[Alby Hub](https://github.com/getAlby/hub)はNostr Wallet Connect（[NIP-47](/ja/topics/nip-47/)）をサポートするセルフカストディアルLightningノードで、[v1.21.5](https://github.com/getAlby/hub/releases/tag/v1.21.5)を出荷しました。デフォルトのNWC設定に2つ目のrelayが追加され、relay再起動時の信頼性が向上しました。トランザクションリスト内の無効なzapデータの修正により、不正な形式の[NIP-57](/ja/topics/nip-57/)（Lightning Zaps）イベントの表示問題が解消されました。新しいアプリストアエントリにはAlby CLIとLNVPSが含まれます。

### nospeak v0.12.x

[nospeak](https://github.com/psic4t/nospeak)はテキストベースのNostrメッセージングクライアントで、この期間に3つのリリースを出荷しました。[v0.12.0](https://github.com/psic4t/nospeak/releases/tag/v0.12.0)は4桁キーパッドによるPINアプリロックと、ベンガル語、タイ語、ベトナム語、ヒンディー語、アラビア語、ヘブライ語、ウルドゥー語、トルコ語、日本語、中国語、韓国語、オランダ語、ポーランド語、ロシア語、ペルシア語のRTLサポートを含む15以上の新しい言語翻訳を追加しました。[v0.12.1](https://github.com/psic4t/nospeak/releases/tag/v0.12.1)は純粋な黒背景とシアンアクセントのCypherテーマに加え、Android動画ポスター生成を導入しました。[v0.12.2](https://github.com/psic4t/nospeak/releases/tag/v0.12.2)は連絡先メニューにチャットエクスポートとプロフィール表示を追加しました。

### Citrine v2.0.0-pre2

greenart7c3によるAndroidパーソナルrelayの[Citrine](https://github.com/greenart7c3/Citrine)が、新しいデータベースインデックスと再構成されたKotlinコルーチンによるrelayパフォーマンス改善を含む[v2.0.0-pre2](https://github.com/greenart7c3/Citrine/releases/tag/v2.0.0-pre2)を出荷しました。各ホステッドウェブアプリが独自のポートで起動するようになりました。全文検索とイベント展開機能を備えた再設計されたイベント画面が変更を締めくくります。

### NoorNote v0.5.x

[NoorNote](https://github.com/77elements/noornote)はNostrベースのノートテイキングアプリケーションで、[v0.5.0](https://github.com/77elements/noornote/releases/tag/v0.5.0)から[v0.5.7](https://github.com/77elements/noornote/releases/tag/v0.5.7)まで8つのリリースを出荷しました。v0.5.0のAndroidローンチでは[NIP-55](/ja/topics/nip-55/) Amber署名者サポートと[NIP-71](/ja/topics/nip-71/)（動画イベント）ノート公開が追加されました。v0.5.1の再設計されたウェルカムページにはパブリックタイムラインプレビューが含まれ、APKが15 MBに縮小されました。v0.5.2のRelay Browserではユーザーが共有可能なURLを通じてパブリックrelayタイムラインを閲覧でき、メディアダウンロードと[NIP-30](/ja/topics/nip-30/)カスタム絵文字リアクションも搭載されました。v0.5.7までの後続リリースでは、協調的な「tribes」ノート共有システムにおける同期競合状態に対処しました。

### NosCall v0.5.1

[NosCall](https://github.com/sanah9/noscall)はNostr音声・動画通話アプリで、音声メッセージサポート、グループエントリーを含む最適化されたデスクトップエクスペリエンス、デスクトップでの連絡先お気に入り、連絡先ノートとフィルタリング、データエクスポートとクリーンアップオプション、システムフォントサイズのアクセシビリティサポートを含む[v0.5.1](https://github.com/sanah9/noscall/releases/tag/v0.5.1-release)を出荷しました。

### Shosho v0.13.0

[Shosho](https://github.com/r0d8lsh0p/shosho-releases)はNostrライブストリーミングアプリで、ストリームカードメニューからのMP4リプレイダウンロードとプロフィール向け[NIP-05](/ja/topics/nip-05/)（DNSベース検証）を含む[v0.13.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.13.0)を出荷しました。RTMPパブリッシャーはExpo Modules APIに移行されました。低帯域幅接続でのストリーミングパフォーマンスが改善され、旧型デバイスでのクラッシュと[Zap.Stream](https://zap.stream)へのiOSストリーミングが修正されました。

### nostr-java v2.0.0

[nostr-java](https://github.com/tcheeric/nostr-java)は設定可能なWebSocketバッファサイズを含む[v2.0.0](https://github.com/tcheeric/nostr-java/releases/tag/v2.0.0)を出荷し、アプリケーションがより大きなNostrイベントを切り捨てなしに処理できるようになりました。メジャーバージョンのバンプは接続APIへの破壊的変更を反映しています。

### Prism 1.1.0

[Prism](https://github.com/hardran3/Prism)はlong-formコンテンツサポート（kind 30023記事）とアプリ内で直接作成するためのMarkdownエディターを含む[1.1.0](https://github.com/hardran3/Prism/releases/tag/1.1.0)を出荷し、続いて[1.1.1](https://github.com/hardran3/Prism/releases/tag/1.1.1)のバグ修正リリースが行われました。

### Angor v0.2.6

[Angor](https://github.com/block-core/angor)はBitcoinクラウドファンディングプラットフォームで、Boltz統合とワンクリック投資フローを含む[v0.2.6](https://github.com/block-core/angor/releases/tag/v0.2.6)を出荷しました。投資と資金調達の両プロジェクトタイプがtestnet上でエンドツーエンドで動作します。チームはUIが約70%完成していると述べています。

## NIPアップデート

[NIPsリポジトリ](https://github.com/nostr-protocol/nips)への最近の変更：

**マージ済み：**

- **[NIP-91: フィルターのAND演算子](https://github.com/nostr-protocol/nips/pull/1365)**：relayサブスクリプションのタグ配列にANDフィルターセマンティクスを追加します。現在、タグフィルターに複数の値を指定すると（例：複数の`p`タグ）、そのいずれかを含むイベントにマッチします。NIP-91では指定されたすべてのタグ値に同時にマッチするイベントをクライアントが要求でき、帯域幅を削減しより高速なインデックス操作を可能にします。nostr-rs-relay、satellite-node、worker-relay、applesauceを含む複数のrelay実装が既に存在します。以前はNIP-119として番号付けされていました。

- **[NIP-30: タグ内の絵文字セットアドレス](https://github.com/nostr-protocol/nips/pull/2247)**：[NIP-30](/ja/topics/nip-30/)のカスタム絵文字タグにオプションの絵文字セットアドレスを含められるようになりました。クライアント内で絵文字をクリックすると、ブックマークやブラウジングのためにその絵文字が属するセットを開けます。[Chachi](https://github.com/purrgrammer/chachi)クライアントに由来します。

- **[NIP-29: unallowpubkeyとunbanpubkeyの追加](https://github.com/nostr-protocol/nips/pull/2111)**：[NIP-29](/ja/topics/nip-29/)グループチャット用の2つの新しい管理者コマンド。`unallowpubkey`はBANせずに許可リストからpubkeyを削除します。`unbanpubkey`はメンバーリストにpubkeyを再追加せずにBANを解除します。以前は許可リストからの削除にはBANが伴い、BANの解除にはメンバーとしての再追加が必要でした。

**オープンPRとディスカッション：**

- **[NIP-A7: Spells](https://github.com/nostr-protocol/nips/pull/2244)**（2月27日オープン）：purrgrammerによる提案で、spellsはkind 777イベントとして公開されるポータブルな保存済みNostrクエリです。spellはREQまたはCOUNTフィルターを構造化タグ（kindの`k`、pubkeyの`authors`、任意のタグフィルターの`tag`）にエンコードし、ランタイム変数を持ちます。`$me`はログインユーザーのpubkeyに解決され、`$contacts`はユーザーのkind 3フォローリストに展開されます。相対タイムスタンプ（`7d`、`2w`、`1mo`）によりハードコードされた日付なしにローリングタイムウィンドウを定義できます。[nak](https://github.com/fiatjaf/nak)と[Grimoire](https://github.com/purrgrammer/grimoire)で既に実装されており、spellsによりユーザーはクライアントをまたいで移動するキュレートされたフィードを作成、共有、購読できます。

- **[NIP-59: エフェメラルGift Wrap（kind 21059）](https://github.com/nostr-protocol/nips/pull/2245)**（2月27日オープン）：[NIP-59](/ja/topics/nip-59/) gift wrapのエフェメラルバリアントを追加します。kind 21059はNIP-01エフェメラルセマンティクスに従い、relayは配信後にイベントを破棄します。メッセージの永続化が不要なMCPトランスポート向けにContextVMが提案しました。

- **[ContextVM: Nostr上のMCP JSON-RPC](https://github.com/nostr-protocol/nips/pull/2246)**（2月27日オープン）：エフェメラルkind 25910イベントとアドレッシングおよび相関のための`p`と`e`タグを使用して、Model Context ProtocolメッセージをNostr上で転送する方法を規定します。意図的に薄い仕様で、プロトコルの詳細は[ContextVMスペック](https://docs.contextvm.org)に委ねています。

- **[NIP-29: オーディオ/ビデオライブスペース](https://github.com/nostr-protocol/nips/pull/2238)**（2月25日オープン、ドラフト）：fiatjafによるドラフトで、[NIP-29](/ja/topics/nip-29/)グループにライブオーディオとビデオを拡張します。グループメタデータイベントにオプションの`livekit`と`no-text`タグを追加します。ユーザーが音声スペースに参加する際、クライアントは`/.well-known/nip29/livekit/{groupId}`でrelayにJWTをリクエストします。relayはグループメンバーシップを確認し、ユーザーの16進pubkeyを`sub`クレームとするトークンを発行し、[LiveKit](https://livekit.io/)にメディアトランスポートのために渡されます。音声ルームのアクセスはグループの既存の権限モデルを継承するため、relayサイドのメンバーシップルールが発言者を管理します。PyramidとChachiでテスト中です。

- **[協調的イベント所有権](https://github.com/nostr-protocol/nips/pull/2235)**（2月24日オープン）：pablof7zはポインターイベント（kind 39382）を提案し、`p`タグに共同所有者のpubkeyを、`k`タグに対象イベントkindを記載して協調的空間を宣言します。リストされた所有者は誰でも同じ`d`タグでそのkindのイベントを公開でき、クライアントはすべての所有者をクエリして最新のイベントを採用することで現在の状態を解決します。共同著者属性は、検証可能な`a`タグがポインターを逆参照し著者がその`p`タグに含まれる場合にのみ表示され、なりすましを防ぎます。これにより共有Wikiページや共同著作リソースを単一のキーペアに制御を割り当てることなく実現できます。

- **[NIP-09: リポストの連鎖削除](https://github.com/nostr-protocol/nips/pull/2234)**（2月24日オープン）：元の著者がノートを削除した場合、relayはそれを参照するkind 6またはkind 16のリポストも削除すべきです。著者がソースを削除した後にリポストが誤って漏洩した情報を保持しうるプライバシー上の懸念から動機づけられています。変更はrelayサイドのみで、クライアントの修正は不要です。

- **[NIP-07: peekPublicKey](https://github.com/nostr-protocol/nips/pull/2233)**（2月23日オープン）：[NIP-07](/ja/topics/nip-07/)ブラウザ拡張機能に`peekPublicKey()`メソッドを追加します。`getPublicKey()`とは異なり、ユーザー確認のプロンプトなしに現在のpubkeyを返し、ユーザーが自動ログインを有効にしている場合のサイレント自動ログインを可能にします。

- **[NIP-BB: Book](https://github.com/nostr-protocol/nips/pull/2248)**（2月28日オープン、ドラフト）：Nostr上の構造化された書籍出版のために4つのアドレス可能イベントkind（30300-30303）を定義します。Coverイベントはタイトル、カバー画像、[NIP-32](/ja/topics/nip-32/)（ラベリング）ラベルによるライセンス、言語コードを含むルートメタデータを保持します。Indexイベントはbase62分数インデックスを使用して各章をその位置にマッピングし、著者が既存の章の間に番号の振り直しなしに新しい章を挿入できます。Chapterイベントはオプションの画像を含む構造的ヘッダーとして機能し、Episodeイベントは30,000文字上限の実際の散文を配置画像タグとともに運びます。レビューはCoverイベントへのZapで行われ、Zap説明がレビューテキストとなります。

- **[NIP-54: AsciidocからDjotへの切り替え](https://github.com/nostr-protocol/nips/pull/2242)**（2月26日オープン）：12月の[d-tag国際化修正](/en/newsletters/2025-12-31-newsletter/)に続き、このPRは[NIP-54](/ja/topics/nip-54/) WikiのAsciidocマークアップ形式を[Djot](https://djot.net/)に置き換えることを提案し、非ラテン文字スクリプトの理由説明セクションとwikilinkの例を追加します。

- **[NIP-66: 防御的措置](https://github.com/nostr-protocol/nips/pull/2240)**（2月26日オープン）：[nostrability/outbox](#アウトボックスモデルの検証)ベンチマークからの学びに基づき、[NIP-66](/ja/topics/nip-66/)のエッジケースに対する明示的な注意事項を追加します。コンパニオン[PR #2241](https://github.com/nostr-protocol/nips/pull/2241)はSSL、位置情報、ネットワーク、接続性チェックの出力タグを定義します。

- **NIP-C1: 暗号学的アイデンティティ証明**（wikiエントリ、kind 30817）：APK署名証明書をNostrプロフィールに暗号学的に紐づけるkind 30509イベントを提案します。証明は証明書の秘密鍵でNostr pubkeyを含む正規メッセージに署名し（ECDSA、RSA PKCS1v15、Ed25519などの標準アルゴリズムをサポート）、その署名をNostr鍵で署名されたkind 30509イベントとして公開することで機能します。検証者はアプリのAndroid署名証明書を制御する人物が、それを公開すると主張するNostr pubkeyも制御していることを確認できます。証明はデフォルトで1年後に失効し、明示的に取り消すこともできます。[Zapstore](https://github.com/zapstore/zapstore)ツールチェーンで実装されています。

- **NIP-31402: SARA収益シェアオファリングレジストリ**（wikiエントリ、kind 30817）：Nostr relay上でSimple Autonomous Revenue Agreement（SARA）オファリングを公開するためのkind 31402アドレス可能イベントを定義します。発行者はプール共有パーセンテージ、支払いトリガー、satsでの閾値、期間長、段階的料金設定を含むLightning決済型収益シェア条件を広告します。エージェントと人間は中央プラットフォームなしにrelay全体でオファリングを発見し自律的にサブスクライブできます。kind番号はkind 30402（L402サービスレジストリ、コンパニオンwikiエントリとして同じ著者が公開）を反映しており、SARAがL402支払い関係のリターンレグを表すためです。

## オープンPRとプロジェクトアップデート

### Damus: [NIP-89](/ja/topics/nip-89/)（推奨アプリケーションハンドラー）

[PR #3337](https://github.com/damus-io/damus/pull/3337)が[Damus](https://github.com/damus-io/damus)にNIP-89クライアントタグサポートを実装します。アプリはすべての投稿パス（メインアプリ、共有拡張機能、ハイライター、ドラフト）でクライアントタグを送出し、他のアプリがタグを含む場合にタイムスタンプの横に「via ClientName」を表示します。外観設定のプライバシートグルでユーザーがタグ送出を無効にできます。[PR #3652](https://github.com/damus-io/damus/pull/3652)はNostrDBとKingfisherキャッシュのディスク使用量をエクスポートサポート付きのインタラクティブ円グラフで分解する設定内ストレージセクションを追加します。

オープン：[PR #3657](https://github.com/damus-io/damus/pull/3657)は引用ノート向けの[NIP-65](/ja/topics/nip-65/) relayフォールバックを追加します。インラインの`nevent`に著者pubkeyが含まれるがrelayヒントがなくノートがユーザーのプールに見つからない場合、Damusは著者のkind 10002 relayリストを取得し、そのwrite relayから再試行します。

### Amethyst: [NIP-39](/ja/topics/nip-39/)（外部アイデンティティ）、NIP-C0、[NIP-66](/ja/topics/nip-66/)

[Amethyst](https://github.com/vitorpamplona/amethyst)は28件のPRにわたるNIP実装の大規模な波をマージしました。外部アイデンティティクレームは[NIP-39](/ja/topics/nip-39/)の下で専用kind 10011イベントとして公開されるようになり（[PR #1747](https://github.com/vitorpamplona/amethyst/pull/1747)）、後方互換フォールバック付きでソーシャルアイデンティティをkind 0メタデータから分離します。NIP-C0によるコードスニペットサポート（[PR #1744](https://github.com/vitorpamplona/amethyst/pull/1744)）は言語、拡張子、ランタイム、ライセンス、依存関係のアクセサーを持つkind 1337イベントを追加します。[NIP-66](/ja/topics/nip-66/) relayモニタリング実装（[PR #1742](https://github.com/vitorpamplona/amethyst/pull/1742)）はRTTメトリクス、ネットワークタイプ、サポートされるNIP、geohashの完全なタグパースを含む両イベントkindをカバーします。

暗号化DMがAmethyst Desktop（[PR #1710](https://github.com/vitorpamplona/amethyst/pull/1710)）に到着し、[NIP-04](/ja/topics/nip-04/)（暗号化ダイレクトメッセージ）と[NIP-17](/ja/topics/nip-17/)（プライベートダイレクトメッセージ）の両方をサポートするスプリットペインチャットレイアウトを備えます。新しいrelayフィード画面（[PR #1733](https://github.com/vitorpamplona/amethyst/pull/1733)）はフォロー/アンフォロー機能付きで特定のrelayからの投稿を閲覧できます。オープン：検閲耐性NIP-05検証（[PR #1734](https://github.com/vitorpamplona/amethyst/pull/1734)）はHTTP DNSの代わりにNamecoinブロックチェーンに対して解決する`.bit`識別子の並列検証パスを追加します。AmethystがNIP-05フィールドで`.bit`サフィックスを検出すると、ElectrumX-NMCサーバーに名前のトランザクション履歴をクエリし、最新の出力から`NAME_UPDATE`スクリプトを解析してNostr pubkeyを抽出し、36,000ブロック（Namecoinの有効期限ウィンドウ）より古い名前を拒否します。ElectrumX接続はTor有効時にSOCKS5を経由し、クリアネットと`.onion`エンドポイント間の動的サーバー選択を行います。1時間TTLのLRUキャッシュが繰り返しのブロックチェーンクエリを防ぎます。

### Notedeck: アウトボックスアーキテクチャ

[PR #1303](https://github.com/damus-io/notedeck/pull/1303)は[Notedeck](https://github.com/damus-io/notedeck)をアドホックなrelayプール管理からアカウントスコープのサブスクリプションを持つ集中型アウトボックスモデルに移行します。Messagesモジュールはデフォルトのリストが存在しない場合にデフォルトのDM relayリストを公開し、kind 10050ごとに受信者の優先relayにDMをルーティングするようになりました。

### Pika: グループごとのプロフィールとチュートリアルフィード

[Pika](https://github.com/sledtools/pika)はiOS、Android、デスクトップビルドで利用可能なMarmot暗号化メッセージングアプリで、グループごとのプロフィール（[PR #368](https://github.com/sledtools/pika/pull/368)）を獲得しました。ユーザーは各グループチャットに個別の表示名と画像、カスタムプロフィールを設定できるようになりました。これらのプロフィールはMarmotグループ内の暗号化kind 0イベントとして公開され、外部からは見えません。グループ固有のプロフィールが設定されていない場合はユーザーのグローバルNostrプロフィールにフォールバックします。新メンバーが参加すると、管理者は保存されたすべてのグループプロフィールを再ブロードキャストし、各メンバーはコミット時に自分のプロフィールを再公開します。プロフィール画像はBlossomアップロード前にMarmotメディア暗号化されます。PRには16の新しいユニットテストが含まれ、CLIコマンド（`update-group-profile`）とUIの両方で機能を公開します。

新しい`pika-news`ウェブアプリ（[PR #401](https://github.com/sledtools/pika/pull/401)）はPika自身のGitHub PRを監視し、PR diffからステップバイステップのチュートリアルウォークスルーを自動生成し、[NIP-07](/ja/topics/nip-07/)認証付きのサーバーレンダリングページとして公開します。ユーザーはNostr認証チャットを通じて特定のチュートリアルについてリアルタイムで議論できます。

### diVine: 埋め込みウィジェットとビデオリプライ

[diVine](https://github.com/divinevideo/divine-mobile)はNostrネイティブの動画共有プラットフォームで、10日間で132件のPRをマージしました。埋め込みiframeウィジェット（[PR #1843](https://github.com/divinevideo/divine-mobile/pull/1843)）はユーザーのプロフィールと最新動画をレンダリングする自己完結型の`/embed?npub=...`ページを提供します。ビデオリプライ機能（[PR #1915](https://github.com/divinevideo/divine-mobile/pull/1915)）はフィーチャーフラグの背後でゲートされ、[NIP-92](/ja/topics/nip-92/)（メディア添付）imetaメタデータを持つKind 1111コメント（[NIP-22](/ja/topics/nip-22/)）を使用します。Blueskyにインスパイアされた3段階コンテンツフィルター（[PR #1797](https://github.com/divinevideo/divine-mobile/pull/1797)）は17の[NIP-32](/ja/topics/nip-32/)コンテンツ警告カテゴリにわたって表示/警告/非表示コントロールを提供します。

### strfry: REQフィルターバリデーション

[PR #163](https://github.com/hoytech/strfry/pull/163)はC++ Nostr relayの[strfry](https://github.com/hoytech/strfry)に設定可能なREQフィルターバリデーションを追加します。オペレーターはREQあたりの最大フィルター数、必要な著者またはタグの存在、許可されるkindのホワイトリスト、フィルターごとのkind制限を設定できます。この機能は厳格なフィルター適用が必要なNWC relayデプロイメントをターゲットにしています。オープン：[PR #173](https://github.com/hoytech/strfry/pull/173)はインジェスト時のイベントペイロードのオプションzstd圧縮を追加します。

### rust-nostr: [NIP-62](/ja/topics/nip-62/) Request to Vanish

[rust-nostr](https://github.com/rust-nostr/nostr)はRust Nostrプロトコルライブラリで、3つすべてのデータベースバックエンドにわたる[NIP-62](/ja/topics/nip-62/)（Request to Vanish）サポートを追加しました。[LMDB](https://github.com/rust-nostr/nostr/pull/1268)、[SQLite](https://github.com/rust-nostr/nostr/pull/1270)、[インメモリ](https://github.com/rust-nostr/nostr/pull/1272)です。LMDB実装にはデプロイメントごとに[NIP-09](/ja/topics/nip-09/)とNIP-62の適用を有効または無効にする設定可能なオプションが含まれます。

### NDK: 協調イベントとNIP-46タイムアウト

JavaScript/TypeScript向けNostr Development Kitの[NDK](https://github.com/nostr-dev-kit/ndk)は、認可された著者を定義するアドレス可能ポインターイベント（kind 39382）を使用するマルチ著者協調ドキュメント用の`NDKCollaborativeEvent`を導入する[PR #380](https://github.com/nostr-dev-kit/ndk/pull/380)をマージしました。`NDKNip46Signer`の設定可能なタイムアウト（[PR #381](https://github.com/nostr-dev-kit/ndk/pull/381)）はバンカーが応答しない場合に[NIP-46](/ja/topics/nip-46/)リモート署名操作が無期限にハングすることを防ぎます。

### TENEX: エージェント分類とPubkeyゲーティング

[TENEX](https://github.com/tenex-chat/tenex)はNostrネイティブのAIエージェントオーケストレーションプラットフォームで、セキュリティ関連の2件のPRをマージしました。TIP-01ロールベースのエージェント分類（[PR #91](https://github.com/tenex-chat/tenex/pull/91)）はエージェントカテゴリ（principal、orchestrator、worker、advisor、auditor）をdenied-toolsマップを通じた自動ツール制限にマッピングします。フロントドアpubkeyゲーティング（[PR #87](https://github.com/tenex-chat/tenex/pull/87)）はホワイトリストまたはバックエンド署名済みpubkeyからのイベントのみが既知のエージェントとともにルーティングされることを保証し、未知のpubkeyは監査用OpenTelemetryスパンとともにサイレントにドロップされます。

### Zap Cooking: メンバーシップダッシュボード

[Zap Cooking](https://github.com/zapcooking/frontend)はNostrベースのレシピ共有プラットフォームで、10日間で25件のPRと85件のコミットをマージしました。メンバーシップダッシュボード（[PR #228](https://github.com/zapcooking/frontend/pull/228)）は有効期限と管理/アップグレードオプション付きのサブスクリプションステータスを表示し、クライアントサイドとサーバーサイドの両方のチェックでSous ChefとZappyティアのフィーチャーゲートを再有効化し、26ファイルにわたるティア命名を標準化します。2フェーズグループメッセージ読み込み（[PR #227](https://github.com/zapcooking/frontend/pull/227)）は即座の表示のための3日間の高速初期フェッチに続いてバックグラウンドの40日間バックフィルを提供します。

ウォレットニーモニックストレージがpubkey導出暗号化から[NIP-44](/ja/topics/nip-44/)自己暗号化に移行しました（[PR #224](https://github.com/zapcooking/frontend/pull/224)）。旧方式は`SHA-256(pubkey)`からキーを導出しており、pubkeyは公開情報のため事実上暗号化されていない脆弱性を修正します。既存のウォレットは最初の読み込み時にサイレントに移行されます。[NIP-29](/ja/topics/nip-29/)グループチャットは赤ドットバッジの未読インジケーターとkind 9009招待コードによる招待制アクセスを獲得しました（[PR #213](https://github.com/zapcooking/frontend/pull/213)）。リンクプレビューとNostrイベント埋め込みがDMとグループメッセージでレンダリングされるようになりました（[PR #218](https://github.com/zapcooking/frontend/pull/218)）。設定内のNostrバックアップセクション（[PR #210](https://github.com/zapcooking/frontend/pull/210)）はローテーティング3スロットバージョニングを持つ[NIP-78](/ja/topics/nip-78/)（アプリケーション固有データ）暗号化ストレージを通じてフォローとミュートリストを保存します。起動パフォーマンスは通知サービスの遅延化、IntersectionObserverによるレイジーDOMレンダリング（200イベントフィードでDOMノードを約15,000から約3,000に削減）、延長されたアウトボックスキャッシュTTLを通じて改善されました（[PR #208](https://github.com/zapcooking/frontend/pull/208)）。カスタマイズ可能な印刷レシピモーダル（[PR #205](https://github.com/zapcooking/frontend/pull/205)）はライブプレビュー付きでどのセクションを含めるかをトグルできます。[Branta SDK](https://github.com/BrantaOps/branta-core)統合（[PR #222](https://github.com/zapcooking/frontend/pull/222)）はPOSTとGETリクエストの検証ガードレールを追加します。

### Keep: Rust駆動の状態移行

[Keep](https://github.com/privkeyio/keep-android)はAndroid向けNostrベースの秘密鍵マネージャーで、4つのKotlin設定ストアを削除しkeep-mobileレイヤーからのRust駆動共有状態に置き換える[PR #178](https://github.com/privkeyio/keep-android/pull/178)をマージしました。10秒ポーリングループがRustからのプッシュベースの`KeepStateCallback`に置き換えられました。[PR #179](https://github.com/privkeyio/keep-android/pull/179)はパスフレーズ保護付きの暗号化バックアップとリストアを追加します。

### Mostro Mobile: 紛争チャット暗号化

[Mostro Mobile](https://github.com/MostroP2P/mobile)はMostro P2P Bitcoin取引プラットフォームのモバイルクライアントで、紛争チャット暗号化の2段階移行を出荷しました。最初のステップ（[PR #495](https://github.com/MostroP2P/mobile/pull/495)）はmostro固有のラッピングから管理者のpubkeyから導出された共有キー暗号化に切り替えます。その上に構築される[PR #501](https://github.com/MostroP2P/mobile/pull/501)はメッセージモデルを`NostrEvent`に統一し、gift wrapイベントをディスク上に暗号化して保存します。これはP2Pチャットパターンと一貫しています。BIP-340署名修正（[PR #496](https://github.com/MostroP2P/mobile/pull/496)）はbip340依存関係を0.2.0にオーバーライドし、Schnorr署名の1-2%を無効にし、公開鍵が`0x00`で始まるキーでは100%失敗を引き起こす`bigToBytes()`パディングバグを解決します。Order Detailsは生のプロトコル値の代わりに人間が読めるステータスラベルを表示するようになり、英語、スペイン語、イタリア語、フランス語にわたってローカライズされています（[PR #502](https://github.com/MostroP2P/mobile/pull/502)）。HalCashが追加されSEPAが支払い方法から削除されました（[PR #493](https://github.com/MostroP2P/mobile/pull/493)）。SEPA送金は24時間を超える可能性があるためです（SEPA Instantは維持）。

サーバーサイドでは、[Mostro](https://github.com/MostroP2P/mostro)が紛争セッションの復元にinitiatorフィールドを含めるよう修正し（[PR #599](https://github.com/MostroP2P/mostro/pull/599)）、売り手が資金をリリースした際にアクティブな紛争を自動的にクローズし、管理クライアントが解決を確認できるよう決済済みNostrイベントを公開するようになりました（[PR #606](https://github.com/MostroP2P/mostro/pull/606)）。

## Nostr 2月の5年間

[先月のニュースレター](/ja/newsletters/2026-01-28-newsletter/#nostr-1月の5年間)ではNostrの1月のマイルストーンを初期開発からDamusのブレイクアウト、2026年のセキュリティインフラまで辿りました。今回の回顧録は2021年から2026年までの各年2月に起きたことをカバーします。

### 2021年2月：リライト

誕生から3か月後、Nostrの2月はプロトコルの最も重大な初期変更を生み出しました。2月14-15日、fiatjafが[NIP-01を書き換え](https://github.com/nostr-protocol/nostr/commit/33a1a70)、オリジナルのメッセージ形式をプロトコルが現在も使用するEVENT/REQ/CLOSEモデルに置き換えました。この書き換え以前は、クライアントとrelayはよりシンプルな構造で通信していました。イベント公開（EVENT）とサブスクリプション管理（REQ/CLOSE）を分離することで、スケーリングに不可欠となるrelayサイドのフィルタリングが可能になりました。

同月に[NIP-04](/ja/topics/nip-04/)が到着し、secp256k1上のDiffie-Hellman鍵交換から導出された共有シークレットを使用する暗号化ダイレクトメッセージを追加しました。暗号化は基本的なもの（AES-256-CBC）で、後に[NIP-44](/ja/topics/nip-44/)の監査済み暗号方式に置き換えられましたが、少数の初期ユーザーにプロトコル上での最初のプライベート通信チャネルを提供しました。

ツールは[noscl](https://github.com/fiatjaf/noscl)（ターミナルベースのrelay操作用Goコマンドラインクライアント）で拡張され、futurepaullは初期のRust実装である[nostr-rs](https://github.com/futurepaul/nostr-rs)を開始しました。ネットワーク全体は2つか3つのrelayで運用され、[Telegramグループ](https://t.me/nostr_protocol)を通じて調整され、約7人のアクティブなコントリビューターがいました。

### 2022年2月：勢いの構築

2021年12月31日の[Hacker Newsの投稿](https://news.ycombinator.com/item?id=29749061)が引き続き2月まで開発者を引き付けました。[nostr-protocol/nostr](https://github.com/nostr-protocol/nostr)リポジトリ（正式な[NIPsリポジトリ](https://github.com/nostr-protocol/nips)は2022年5月まで存在しませんでした）は2月に6件のプルリクエストを受け取りました。vinliaoのNIP-13（Proof of Work）、fiatjafのNIP-14（Reputation）、CameriのNIP-15（Resource Relations）、melvincarvalhoの[NIP-17](https://github.com/nostr-protocol/nostr/pull/75)（Git Updates Over Nostr）が含まれます。NIP番号は後にPrivate Direct Messagesに再割り当てされ、Nostr上のgitコラボレーションは後に[gitworkshop.dev](https://gitworkshop.dev)となるものを通じて別途続きました。

Greg Heartsfield の[nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay)はこの月の主力で、34件のコミットと3つのリリースを記録しました。2月12日のバージョン0.5.0は[NIP-05](/ja/topics/nip-05/)認証済みユーザー公開制限を追加しました。バージョン0.5.1と0.5.2がその後2週間で続き、relayはネットワークのトラフィックの大部分を単独で処理していました。

Robert C. Martin（Uncle Bob）は[more-speech](https://github.com/unclebob/more-speech)（Clojureデスクトップクライアント）を構築しており、1月18日から2月末までに69件のコミットを記録しました。彼の関与はより広いソフトウェアエンジニアリングコミュニティからの注目を集めました。fiatjafの[nos2x](https://github.com/fiatjaf/nos2x)ブラウザ拡張機能は2月に[NIP-04](/ja/topics/nip-04/)復号サポートとrelay優先ポリシーを出荷し、ウェブクライアントが鍵委任に現在も使用する`window.nostr`インターフェース（[NIP-07](/ja/topics/nip-07/)）を実装しました。

[Branle](https://github.com/fiatjaf/branle)は依然として主要なウェブクライアントで、2月13日に`web+nostr`プロトコルハンドラー登録を獲得しました。これはNostrアプリケーション間のディープリンクの初期の試みでした。[nostr-tools](https://github.com/nbd-wtf/nostr-tools)はNIP-05検証を厳格化しました。[go-nostr](https://github.com/nbd-wtf/go-nostr)は11件のコミットでNIP-04暗号化DMサポートとNIP-12（Generic Tag Queries）パースを追加しました。ネットワークは約7-15のrelayで運用され、アクティブなユーザーベースはおそらく数百人規模でした。DamusとNostreamはまだ存在せず、2022年4月まで登場しませんでした。

### 2023年2月：国際的注目

2023年2月はNostrに最大の公的注目の波をもたらしました。William CasarinによるiOSクライアントの[Damus](https://github.com/damus-io/damus)は、度重なるリジェクトの後に[1月31日にApple App Storeで承認されました](https://www.coindesk.com/tech/2023/02/01/decentralized-social-media-project-nostrs-damus-gets-listed-on-apple-app-store)。2月1日までに米国ソーシャルネットワーキングでトップ10に到達しました。2日後の2月2日、報道によるとサイバースペース管理局の要請により[AppleがDamusを中国のApp Storeから削除しました](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/)。

TechCrunchやCoinDeskを含む主要メディアが削除を報じ、アプリとプロトコルの両方の認知度を高めました。nostr.directory上のメタデータ付きユニーク公開鍵は2月3日までに30万を超えました。すべてのrelayは自費で運営する愛好家によって運営されており、インフラは負荷に対処するために奔走しました。2月初旬までに約289のrelayが追跡され、その数は増加し続けました。

[NIPsリポジトリ](https://github.com/nostr-protocol/nips)はその月に29件のマージ済みプルリクエストを記録し、それまでのプロトコル史上最多の月間件数でした。[NIP-57](https://github.com/nostr-protocol/nips/pull/224)（Lightning Zaps）と[NIP-23](https://github.com/nostr-protocol/nips/pull/220)（Long-form Content）が2月13日に同時にマージされ、Bitcoinマイクロペイメントの追加とNostrの短文投稿以外への拡張が1日で実現しました。[NIP-65](/ja/topics/nip-65/)（Relayリストメタデータ）はその1週間前の2月7日にマージされ、後に続くアウトボックスモデルを可能にしました。[NIP-46](/ja/topics/nip-46/)（Nostr Connect）と[NIP-58](/ja/topics/nip-58/)（Badges）も月末までにランドしました。

Human Rights Foundationは2月21日に[William CasarinにNostrとDamus開発のため5万ドルの助成金を授与しました](https://hrf.org/devfund2023q1)。これはNostrプロジェクトへの最初期の機関助成金の1つでした。OpenSatsのNostrファンドはまだ開始されていませんでした（[2023年7月](https://opensats.org/blog/nostr-grants-july-2023)に開始）。

### 2024年2月：プロトコルの耐久性

2024年2月は成長からプロトコルの耐久性へと焦点を移しました。前年7月からオープンしていた[NIP-17](/ja/topics/nip-17/)（プライベートダイレクトメッセージ）は、[NIP-44](/ja/topics/nip-44/)の監査済み暗号方式と[NIP-59](/ja/topics/nip-59/) gift wrappingを使用する老朽化した[NIP-04](/ja/topics/nip-04/)暗号化の置き換えに向けて取り組んでいました。NIP-04はrelayオペレーターにメタデータを漏洩し、送信者と受信者のペアを確認できました。NIP-17は使い捨てキーペアの背後に送信者のアイデンティティを隠し、3月の最終レビューラウンドを経てその春にマージされました。

[NIP-29](/ja/topics/nip-29/)（Simple Groups）は数か月の議論を経て[2月28日にマージされ](https://github.com/nostr-protocol/nips/pull/566)、管理者ロールとアクセス制御を持つモデレートされたグループチャットをrelayがホストする方法を定義しました。[NIP-92](/ja/topics/nip-92/)（imetaタグ）は2月1日にマージされ、クライアントがメディアイベントに画像寸法とblurhashプレビューを添付する方法を標準化しました。

2月16日、NIPsリポジトリに[BREAKING.md](https://github.com/nostr-protocol/nips/commit/62c48eff)が追加されました。これはプロトコル仕様への後方互換性のない変更を追跡するファイルです。その作成は、Nostrが破壊的変更に正式な文書化が必要な成熟レベルに達したことを認めるものでした。

その月に22件のプルリクエストがマージされました。[npub.cash](https://github.com/cashubtc/npubcash-server)がサーバーを運用せずにどのnpubでも支払いを受け取れるLightningアドレスサービスとしてローンチされました。2月8日に公開された[学術論文](https://arxiv.org/abs/2402.05709)は、無料relayの95%が寄付だけでは運用コストを賄えず、有料relayの35%が1,000 sats（当時約0.45ドル）未満の入場料を請求していることを発見しました。

### 2025年2月：インフラの成長

2025年2月はNIPsリポジトリに28件のマージ済みプルリクエストを生み出しました。[Right to Vanish](/ja/topics/nip-62/) NIPが2月19日にマージされ、データポータビリティとユーザーコントロールに関する規制上の質問に応じてユーザーがrelayからのデータ削除を要求する方法を定義しました。

[NIP-60](/ja/topics/nip-60/)（Cashuウォレット）とNIP-61（Nutzaps）が簡素化アップデートを受け、ecashトークンストレージ形式が合理化されました。qタグ（引用タグ）のロールアウトが複数のNIPにわたって続き、イベントが引用とスレッディングのために他のイベントを参照する方法を標準化しました。

クライアントリリースは着実な進歩を示しました。[Notedeck](https://github.com/damus-io/notedeck) v0.3.0アルファが1月最終日に出荷され、2月もアドプションが続きました。Primal v2.1が2月7日に続き、Go relay実装の[GRAIN](https://github.com/0ceanSlim/grain) v0.3.0が2月21日にリリースされました。

NOSTRLDN v5がロンドンNostrコミュニティの第5回ミートアップを開催しました。DVMCPブリッジがNostrのData Vending Machines（[NIP-90](/ja/topics/nip-90/)）とModel Context Protocolを接続し、翌月に到来するAIエージェント統合作業を予告しました。

### 2026年2月：ソーシャルメディアを超えて

*2026年2月のアクティビティはNostr Compass第[8号](/ja/newsletters/2026-02-04-newsletter/)から第[11号](/ja/newsletters/2026-02-25-newsletter/)から引用しています。*

2026年2月はどのNostr単月でも最も広範なアプリケーションレイヤー開発を生み出しました。[Mostro](https://github.com/MostroP2P/mostro)が分散型P2P Bitcoin取引の[初のパブリックベータ](/ja/newsletters/2026-02-11-newsletter/#mostroが初のパブリックベータを出荷)を出荷し、[Zapstore](https://github.com/zapstore/zapstore)がリリース候補テストの数か月を経て[1.0安定版](/ja/newsletters/2026-02-11-newsletter/#zapstore-v100)に到達しました。[White Noise v0.3.0](/ja/newsletters/2026-02-25-newsletter/#white-noise-v030)が160件以上のマージ改善とAmber署名者サポートを含むリアルタイム[Marmot](/ja/topics/mls/)暗号化メッセージングを提供しました。

pablof7z（エージェントワークフロー用NIP-AE、MCPサーバーアナウンス用NIP-AD）とjoelklabo（AIエージェントメッセージ）からの競合するAIエージェント提案が、[NIP-90](/ja/topics/nip-90/)を拡張する[DVMエージェント調整提案](/ja/newsletters/2026-02-25-newsletter/#nipアップデート)とともに到着しました。[ContextVM](/ja/newsletters/2026-02-25-newsletter/#contextvmnostr上のmcp)がModel Context ProtocolをNostrトランスポートに接続するSDK改善を出荷しました。[Burrow](/ja/newsletters/2026-02-25-newsletter/#burrowaiエージェント向けmlsメッセージング)がAIエージェントと人間の両方に[Marmot](/ja/topics/mls/)暗号化メッセージングを追加し、Nostrのアイデンティティとrelayインフラをマシン間通信に拡張しました。

[FIPS](/ja/newsletters/2026-02-25-newsletter/#fipsnostrネイティブメッシュネットワーキング)がsecp256k1キーペアをノードアイデンティティとして使用し、UDP、イーサネット、Bluetooth、LoRadioにわたるトランスポート非依存ルーティングを持つNostrネイティブメッシュネットワーキングの動作するRust実装を出荷しました。その設計はNostrのキーモデルがソーシャルメディアを超えて物理ネットワークインフラに拡張できることを示しました。

[OpenSatsが第15波のNostr助成金を発表し](https://opensats.org/blog/fifteenth-wave-of-nostr-grants)、ContextVMとNostubeを含むプロジェクトに資金提供しました。プロトコル変更にはNostr Wallet Connectの[NIP-47](/ja/topics/nip-47/)ホールドインボイスサポートとrelayサイドのカウント推定のための[NIP-45](/ja/topics/nip-45/)（カウント結果）HyperLogLogが含まれました。[Web of Trust](/ja/topics/web-of-trust/)スコアリング用の[NIP-85](/ja/topics/nip-85/)（Trusted Assertions）サービスプロバイダー発見機能もマージされました。[rust-nostr](https://github.com/rust-nostr/nostr)が完全なAPI再設計を開始し、Nostria 3.0と[Frostr](https://github.com/FROSTR-ORG)（iOS TestFlight）が出荷されました。[Blossom](/ja/topics/blossom/)のローカルキャッシュレイヤーがrelay間のメディア可用性に対応しました。

### 今後の展望

5つの2月のプロトコル史は、基盤的作業からアプリケーションレイヤーの多様化への一貫した進展を示し、2023年のユーザー流入がターニングポイントとなりました。2021年には7人のコントリビューターが3つのrelayで作業していました。2026年までに、同じプロトコルがプロダクションインフラ上で実行されるメッシュネットワーキングと自律エージェント提案をサポートしています。

---

今週は以上です。構築中のプロジェクトや共有したいニュースがあれば、<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">[NIP-17](/ja/topics/nip-17/) DMでお問い合わせください</a>。Nostrでもお待ちしています。
