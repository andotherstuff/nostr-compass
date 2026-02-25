---
title: 'Nostr Compass #11'
date: 2026-02-25
translationOf: /en/newsletters/2026-02-25-newsletter.md
translationDate: 2026-02-25
draft: false
type: newsletters
---

Nostr Compassへようこそ。Nostrの週刊ガイドです。

**今週の内容:** [White Noise v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0)がリアルタイムメッセージングとAmber署名者サポートを160件以上のマージ改善とともに届けます。[diVine 1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5)が動画再生の問題を修正し、クリエイター分析用のkind 22236ビューイベントを追加。[Pika](https://github.com/sledtools/pika)、[Ridestr](https://github.com/variablefate/ridestr)、[Unfiltered](https://github.com/dmcarrington/unfiltered)がアップデートを出荷。[FIPS](https://github.com/jmcorgan/fips)がNostrネイティブメッシュネットワーキングの動作するRust実装を出荷。NotecrumbsがDamus.ioリンクプレビューの安定性修正を受け取る。[ContextVM](https://contextvm.org)がNostrとModel Context Protocolを橋渡し。新しいプロジェクトとして、AIエージェントと人間の間のMLS暗号化メッセージング用[Burrow](https://github.com/CentauriAgent/burrow)と、ブラウザベースのvaultとアイデンティティ管理用[Nostria Signer](https://github.com/nostria-app/nostria-signer-extension)が登場。ディープダイブではNIP-55のAndroid署名とNIP-60のCashuウォレット同期を取り上げます。

## ニュース

### Notecrumbsの安定性改善

[Notecrumbs](https://github.com/damus-io/notecrumbs)はDamus.ioのリンクプレビューを支えるNostr APIおよびウェブサーバーで、信頼性の問題に対処する一連の修正を受け取りました。

[並行処理の修正](https://github.com/damus-io/notecrumbs/commit/3f201f63ea49)により、インフライトの重複排除メカニズムがwatchチャンネルに置き換えられました。同じノートをリクエストする2人の呼び出し元が両方ともフェッチャーになり得て、一方が他方が通知をサブスクライブする前に完了した場合にデッドロックを引き起こしていました。アトミック操作を使用するwatchチャンネルにより、1つのフェッチャーのみが実行され、他の処理は結果を待ちます。

[レート制限](https://github.com/damus-io/notecrumbs/commit/b0d0bf5a2f17)はrelayへの過剰アクセスに対する二層の防御を実装します。ユーザーが同じノートに繰り返しアクセスすると、システムは5分間のクールダウンウィンドウでrelayリクエストをデバウンスするようになりました。この保護はすべての[NIP-19](/ja/topics/nip-19/)タイプとプロフィールフィードに拡張され、重いトラフィック時のrelayへの比例スパムを防ぎます。

[パフォーマンス改善](https://github.com/damus-io/notecrumbs/commit/38670b3972b6)により、二次データフェッチがバックグラウンドのtokioタスクに移動しました。ページはキャッシュされたデータで即座にレンダリングされるようになり、合計7.5秒に達する可能性のある連続したrelayタイムアウトでブロックされません。nostrdb 0.10.0へのアップグレードもこれらの修正に伴いました。

### ContextVM：Nostr上のMCP

[ContextVM](https://contextvm.org)はNostrと[Model Context Protocol](https://modelcontextprotocol.io/)（MCP）を橋渡しするツール群です。最近のコミットでは支払いを可能にする新しい[CEP-8](https://docs.contextvm.org/spec/ceps/cep-8/)仕様が導入され、2月を通じて[SDK](https://github.com/ContextVM/sdk)の改善が進んでいます。

SDKはMCP over Nostr用のTypeScriptクライアントとサーバートランスポートを提供します。開発者はNostrネットワーク全体にMCPサーバーを公開でき、クライアントはそれらに接続できます。relayはメッセージバスとして機能し、暗号化されたeventをただルーティングします。Nostrをネイティブにサポートしないクライアントはプロキシレイヤーを通じて接続します。ライブラリはevent認証のためのrelay管理と暗号署名を処理し、Node.jsとブラウザ環境の両方で動作します。

[CVMI](https://github.com/ContextVM/cvmi)はサーバーディスカバリーとメソッド呼び出し用のCLIを提供します。[Relatr](https://github.com/ContextVM/relatr)はソーシャルグラフの距離とプロフィール検証を組み合わせてパーソナライズされたトラストスコアを計算します。

ContextVMはブリッジレイヤーとして位置づけられています。既存のMCPサーバーは従来のトランスポートを維持しながらNostrの相互運用性を得ます。

### White Noiseが分散型ユーザー検索を解説

[jgmontoyaのブログ投稿](https://blog.jgmontoya.com/2026/02/22/user-search.html)では、[White Noise](https://github.com/marmot-protocol/whitenoise)が分散型relayネットワーク全体でどのようにユーザー検索を処理するかが詳しく説明されています。

プロフィール分散が課題を生み出します。統一されたデータベースを持つ中央集権的なメッセンジャーとは異なり、Nostrのプロフィールは中央インデックスなしに数十のrelay全体に散らばっています。White Noiseはプロデューサー・コンシューマーアーキテクチャをパラレルに実行することでこれを解決します。

プロデューサープロセスはユーザーのフォローからソーシャルグラフを外側に継続的に拡張し、増加する距離でフォローリストを取得してプロフィール解決のために発見したpubkeyをキューに入れます。コンシューマーは5つのコスト増加ティアでマッチを解決します。ローカルユーザーテーブル（最速）、前回の検索からのキャッシュされたプロフィール、接続されたrelay、[NIP-65](/ja/topics/nip-65/)によるユーザーrelayリスト、ユーザー宣言relayへの直接クエリ（最も低速）です。

コールド検索は約3秒かかりますが、キャッシュからのウォーム検索は約10ミリ秒に短縮されます。確立されたソーシャルグラフを持たない新規ユーザーに対しては、検索機能を確保するためによく接続されたブートストラップノードが挿入されます。グループメンバーシップは明示的なフォローと並んで暗黙のソーシャルシグナルを提供します。

計測が最適化に不可欠だったと著者は述べています。メトリクスなしでは改善は当て推量でした。

### FIPS：Nostrネイティブメッシュネットワーキング

[FIPS](https://github.com/jmcorgan/fips)（Free Internetworking Peering System）は、Nostrのキーペア（secp256k1）をノードのアイデンティティとして使用する自己組織化メッシュネットワークの動作するRust実装です。[設計ドキュメント](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md)が機能的なコードとともに公開されています。

このプロトコルはインフラの独立性に対応します。ノードは中央サーバーや認証局なしに自動的に相互発見します。スパニングツリーが座標ベースのルーティングを提供し、bloom filterが到達可能性情報を伝播させ、ノードはローカルの知識だけで転送判断を行えます。トランスポートの非依存性により、同じプロトコルがUDP、イーサネット、Bluetooth、LoRadio、あるいはデータグラム対応の任意のメディア上で動作します。

2つの暗号化レイヤーがトラフィックを保護します。リンクレイヤー暗号化（Noise IKパターン）が相互認証と前方秘密性を持つホップ間の隣接ノード通信を保護します。セッションレイヤー暗号化（Noise XKパターン）が中間ルーターに対するエンドツーエンドの保護を提供し、宛先のみがペイロードを復号できます。これはTLSがHTTPトラフィックを信頼できないネットワークを通過する場合でも保護する方法を反映しています。

アーキテクチャはルーティングに「貪欲埋め込み」スパニングツリーを使用します。各ノードはツリーのルートと親に対する位置に基づいて座標を受け取ります。パケットは目的地に近い座標に向かって貪欲にルーティングされ、bloom filterが到達可能なエンドポイントを通知します。貪欲なルーティングが失敗する場合（局所的最小値）、ノードはツリーベースのパスにフォールバックできます。

Rust実装にはすでにbloom filterディスカバリーを含むUDPトランスポートが含まれています。今後の作業はピアブートストラップのためのNostr relay統合を目標としています。

## リリース

今週はrelayインフラとクライアントアプリケーション全体でリリースがあり、この分野に新しいプロジェクトも参入しました。

### HAVEN v1.2.0

[Blossom](/ja/topics/blossom/)メディアサーバーと4つのrelay機能をバンドルしたオールインワンパーソナルrelay[HAVEN](https://github.com/bitvora/haven)が[v1.2.0](https://github.com/bitvora/haven/releases/tag/v1.2.0)を出荷しました。このリリースは[先週取り上げた](/ja/newsletters/2026-02-18-newsletter/#haven-v120-rc3)RCステージを超えて進んでいます。

マルチnpubサポートにより、単一のHAVENインスタンスがホワイトリストを通じて複数のNostrアイデンティティを提供でき、アクセス制御のための新しいブラックリスト機能も追加されました。書き換えられたバックアップシステムはポータブルなJSONL形式を使用し、JSONLファイルからノートをインポートするための`haven restore`コマンドが利用できます。クラウドストレージ統合がリモートバックアップ管理のための`--to-cloud`と`--from-cloud`フラグを追加します。

[Web of Trust](/ja/topics/web-of-trust/)の改善として、トラスト計算の設定可能な深度レベルとメモリオーバーヘッドを削減するロックレス最適化を伴う自動24時間更新間隔が含まれます。relayリクエスト用のユーザーエージェント設定と設定可能なBlastrタイムアウト設定がリリースを完成させ、圧縮JSONLへのデータエクスポートも追加されました。

### White Noise v0.3.0

[White Noise](https://github.com/marmot-protocol/whitenoise)は[MLS](/ja/topics/mls/)ベースの暗号化メッセージングアプリで[Marmot](/ja/topics/marmot/)プロトコルを実装しており、160件以上のマージ改善を含む[v0.3.0](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.3.0)を出荷しました。

このリリースではポーリングの代わりにストリーミング接続によるリアルタイムメッセージングが実現され、メッセージが即座に届きます。Amberサポート（[NIP-55](/ja/topics/nip-55/)）により秘密鍵がアプリに触れる必要がなくなります。画像共有がアップロード進捗追跡と読み込み中のblurhashプレースホルダーとともに機能するようになりました。フルスクリーン表示でピンチズームをサポートします。

グループメッセージングはチャットリストに送信者名を表示し、[MLS](/ja/topics/mls/)暗号化が前方秘密性を確保する信頼性改善を受けました。ユーザー検索はフォローから4次の隔たりまで外側に拡張され、見つかった結果がストリーミングで表示されます。

Marmotプロトコルの変更と暗号化ローカルストレージへの切り替えにより、アップグレード時にすべてのローカルデータがリセットされる破壊的変更があります。アップグレード前にnsecキーのバックアップを取ることをお勧めします。

### diVine 1.0.5

[diVine](https://github.com/divinevideo/divine-mobile)は復元されたVineアーカイブ上に構築された短編ループ動画クライアントで、広範な動画再生修正と新しい分散型分析システムを含む[1.0.5](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.5)を出荷しました。

動画再生の問題が修正の大部分を占めました。ファントムポーズ、動画間のデュアルオーディオ、サムネイルと最初のフレーム間のブラックフラッシュ、廃棄されたプレイヤーのクラッシュがすべて解消されました。プールされた動画プレイヤーがホームフィードの一貫した再生を処理するようになりました。

kind 22236のエフェメラルビューイベントがクリエイター分析と推薦を可能にします。システムはトラフィックソース（ホーム、ディスカバリーバリアント、プロフィール、共有、検索）とループ数を追跡しながら自己ビューを除外します。Nostr event imetaタグのローカルファイルパスリークが、BUD-01仕様に従いクライアント側で構築された正規のBlossom URLで修正されました。

[NIP-46](/ja/topics/nip-46/)リモート署名者の改善として、並列化されたrelay接続とコールバックURLサポートが追加されました。AndroidはSigner承認後のアプリ再開時にWebSocket接続を再接続します。

### Coracle 0.6.30

[Coracle](https://github.com/coracle-social/coracle)はrelayマネジメントと[Web of Trust](/ja/topics/web-of-trust/)モデレーションに特化したウェブベースのNostrクライアントで、フィードでのメディアブラウジングを向上させる動画サムネイルサポートを含む[0.6.30](https://github.com/coracle-social/coracle/releases/tag/0.6.30)を出荷しました。

### Nostur v1.26.0

[Nostur](https://github.com/nostur-com/nostur-ios-public)はiOS向けNostrクライアントで、新しいライブストリームフィードセクションと再設計された設定画面を含む[v1.26.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.26.0)を出荷しました。GIFがBlossomメディアサーバーでホストできるようになり、中央集権的なサービスへの依存が減ります。Klipy GIF統合がTenorが利用できない場合のバックアップを提供します。DM会話の年ヘッダーとメンション数表示もユーザー向け変更として含まれます。

今週は開発者向けツールとCLIアプリもアップデートを受け取りました。

### nak v0.18.5

[nak](https://github.com/fiatjaf/nak)はfiatjafによるNostrのコマンドラインツールで、ユーザープロフィールの取得と表示のための新しい`nak profile`サブコマンドを含む[v0.18.5](https://github.com/fiatjaf/nak/releases/tag/v0.18.5)を出荷しました。`git clone`コマンドが`nostr://`URIで[NIP-05](/ja/topics/nip-05/)名をサポートするようになり、人間が読める識別子でリポジトリをクローンできます。

### Pika v0.5.3

[Pika](https://github.com/sledtools/pika)は[Marmot](/ja/topics/marmot/)プロトコル上に構築されたiOS、Android、デスクトップ向けの[MLS](/ja/topics/mls/)暗号化メッセンジャーで、[v0.5.3](https://github.com/sledtools/pika/releases/tag/pikachat-v0.5.3)を出荷しました。最近のコミットではデスクトップアプリへのファイルアップロードとドラッグアンドドロップメディアサポートが追加され、Cloudflare Workersデプロイの修正も含まれます。

PikaはすべてのビジネスロジックをRustコアが担い、iOS（SwiftUI）とAndroid（Kotlin）は状態スナップショットをレンダリングするシンUIレイヤーとして機能します。MDK（Marmot Development Kit）がMLS実装を提供します。プロジェクトはアルファステータスであることを明記し、センシティブなワークロードへの使用に警告しています。

### Ridestr v0.2.6

[Ridestr](https://github.com/variablefate/ridestr)はCashu支払いを持つ分散型ライドシェアプラットフォームで、[v0.2.6](https://github.com/variablefate/ridestr/releases/tag/v0.2.6)を出荷しました。このリリースはTalkBackアクセシビリティの問題を修正し、支払い方法を切り替えた際にドライバーが近くのリストから消えたり、ドライバーがオフラインになった際に選択されたドライバー数が更新されなかったりするバグを解消します。

「全員に送信」機能は「RoadFlareをブロードキャスト」に変更され、新規ドライバーインストール時のサイレント失敗の修正も含まれます。RidestrはトラストレスなライドペイメントにHTLCエスクローを実装し、デバイス間のウォレット同期に[NIP-60](/ja/topics/nip-60/)を使用しています。

### Unfiltered v1.0.6

[Unfiltered](https://github.com/dmcarrington/unfiltered)はAndroid向けInstagramライクな写真共有アプリで、改善されたユーザー検索と60秒ごとの自動relay再接続を含む[v1.0.6](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.6)を出荷しました。

KotlinとJetpack Composeで構築され、UnfilteredはRust-nostrバインディングとBlossom互換サーバーを画像ホスティングに使用します。Amber統合（[NIP-55](/ja/topics/nip-55/)）がセキュアな鍵管理を処理します。アプリはアルゴリズムや広告なしにフォローしたアカウントの投稿を時系列順で表示します。

今週は2つの新しいメッセージングと署名プロジェクトも立ち上がりました。

### Burrow：AIエージェント向けMLSメッセージング

[Burrow](https://github.com/CentauriAgent/burrow)は電話番号や中央集権的なサーバーなしにMLS暗号化通信のための[Marmot](/ja/topics/marmot/)プロトコルを実装するメッセンジャーです。人間ユーザーとAIエージェントの両方が参加できます。

JSONLアウトプットモードを持つ純粋なRust CLIデーモンが自動化システムとの統合を処理します。FlutterクロスプラットフォームアプリがAndroid、iOS、Linux、macOS、Windowsをカバーします。メディア添付ファイルはメッセージとともに暗号化され、WebRTCが設定可能なTURNサーバーで音声とビデオ通話を処理します。

BurrowはNostrインフラ上にMLS暗号化をレイヤー化します。アイデンティティはNostrキーペア（secp256k1）を使用し、MLS KeyPackageはkind 443イベントとして公開されます。メッセージは[NIP-44](/ja/topics/nip-44/)でkind 445イベントとして暗号化され、ウェルカム招待は[NIP-59](/ja/topics/nip-59/)ギフトラッピングを使用します。

[OpenClaw](https://openclaw.ai)統合によりAIエージェントがフルツールアクセスで参加できます。監査ログ付きアクセス制御リストがコンタクトとグループの権限を管理します。この組み合わせにより、BurrowはSignal レベルの暗号化を分散インフラ上に求めるエージェント間およびエージェントと人間のメッセージングシナリオに適しています。

### Nostria Signer拡張機能

[Nostria Signer](https://github.com/nostria-app/nostria-signer-extension)はNostrユーザー向けのvaultとアイデンティティ管理を提供するChromiumベースのブラウザ拡張機能です。

複数のアカウントを含む複数のvaultにより、ユーザーは異なるコンテキストのアイデンティティを整理できます。国際化にはRTL言語サポートが含まれます。AngularとTypeScript（コードベースの79.2%）で構築され、ブラウザ拡張機能とProgressiveウェブアプリの両方として動作します。

Nostria Signerはブラウザ拡張機能による署名のための[NIP-07](/ja/topics/nip-07/)を実装し、ウェブベースのNostrクライアントが秘密鍵に直接アクセスすることなくevent署名をリクエストできます。自動ウォレットマイグレーションがChrome Web Storeを通じて配布されるアップデートを処理します。ユーザーは`dist/extension`フォルダからサイドロードすることもできます。

開発者は実験的なステータスを強調しています。開発者は失われた鍵へのアクセスを回復できないため、ユーザーは自身のシークレットリカバリーフレーズを管理する必要があります。

## プロジェクトアップデート

### FormstrがOrganizationを移行

Nostr上のGoogleフォーム代替[Formstr](https://github.com/formstr-hq/nostr-forms)がリポジトリを`abh3po/nostr-forms`から`formstr-hq`organizationに移行しました。このOpenSatsグラント受領者は新しい場所で開発を継続します。

### 注目のオープンPR

Nostrプロジェクト全体の進行中の作業：

- **Damusアウトボックスモデル** ([PR #3602](https://github.com/damus-io/damus/pull/3602))：iOSでのgossip/アウトボックスrelayモデルの実装計画。このアーキテクチャ変更は、受信者が実際に読むrelayに公開することでメッセージ配信を改善します。

- **Notedeckクロスプラットフォーム通知** ([PR #1296](https://github.com/damus-io/notedeck/pull/1296))：Android FCM、macOS、Linuxをカバーするダムスデスクトップクライアントのネイティブ通知システム。

- **NDK Cashu v3アップグレード** ([PR #370](https://github.com/nostr-dev-kit/ndk/pull/370))：Nostr Development Kitのウォレット統合をcashu-ts v3に更新。

- **ZeusのCashuオフライン** ([PR #3742](https://github.com/ZeusLN/zeus/pull/3742))：ZeusのLightningウォレットのオフラインecash送受信。

- **Shopstrの暗号化デジタル配信** ([PR #231](https://github.com/shopstr-eng/shopstr/pull/231))：デジタル商品の暗号化配信と物理アイテムのダイナミックウェイトサポートを追加。

## NIPアップデート

[NIPsリポジトリ](https://github.com/nostr-protocol/nips)への最近の変更：

**今週マージ済み：**

- **[NIP-85サービスプロバイダーDiscoverability](https://github.com/nostr-protocol/nips/pull/2223)**：[NIP-85](/ja/topics/nip-85/)仕様にクライアントが信頼されたアサーションプロバイダーを発見する方法についてのガイダンスが追加されました。クライアントが[Web of Trust](/ja/topics/web-of-trust/)スコアや他の計算済みメトリクスを必要とする場合、ユーザーがすでにフォローまたは信頼するプロバイダーからのkind 30085アナウンスをrelayにクエリできます。

- **[NIP-29の非管理グループ削除](https://github.com/nostr-protocol/nips/pull/2229)**：[NIP-29](/ja/topics/nip-29/)グループチャット仕様が非管理グループ（任意のメンバーが他のメンバーを追加できる）のサポートを廃止しました。すべてのNIP-29グループは明示的な管理者ロールを持つリレーサイドの管理が必要になり、実装を簡素化してスパムのベクターを削減します。

- **[NIP-11の非推奨フィールド削除](https://github.com/nostr-protocol/nips/pull/2231)**：[NIP-11](/ja/topics/nip-11/)のrelay情報ドキュメントには非推奨の`software`と`version`フィールドが含まれなくなりました。実装はこれらをレスポンスから削除する必要があります。

- **[NIP-39のアイデンティティタグ移動](https://github.com/nostr-protocol/nips/pull/2227)**：外部アイデンティティクレーム（GitHubやTwitterなどの[NIP-39](/ja/topics/nip-39/)`i`タグ）がkind 0プロフィールから専用のkind 30382イベントに移動しました。これによりアイデンティティ検証がプロフィールメタデータから分離されます。

**AIエージェントNIPの進捗：**

4つのAI特化NIPが活発な開発を継続しています。[先週の報道](/ja/newsletters/2026-02-18-newsletter/#aiエージェントnipが登場)以降：

- **[NIP-AE：エージェント](https://github.com/nostr-protocol/nips/pull/2220)**（2月19日更新）：エージェント定義のkind 4199とプロンプト（「ナッジ」）のkind 4201でエージェントアイデンティティを定義します。エージェントは拡張説明のために[NIP-94](/ja/topics/nip-94/)ファイルメタデータを参照できます。

- **[NIP-XX：AIエージェントメッセージ](https://github.com/nostr-protocol/nips/pull/2226)**（2月18日更新）：ステータス、ストリーミングデルタ、プロンプト、レスポンス、ツール呼び出し、エラー、キャンセル用の7つのエフェメラルevent kind（25800-25806）で会話メッセージングを標準化します。kind 31340「AI Info」イベントでエージェントがサポートするモデルと機能をアドバタイズできます。

- **[NIP-AC：DVMエージェント調整](https://github.com/nostr-protocol/nips/pull/2228)**（2月18日オープン）：自律エージェントワークフロー用に[NIP-90](/ja/topics/nip-90/)を拡張します。エージェントディスカバリーのためのハートビート、品質追跡のためのジョブレビュー、結果コミットメントのためのデータエスクロー、マルチステップパイプラインのためのワークフローチェーン、競争的プロバイダー選択のためのスワームビッディングを追加します。リファレンス実装は2020117.xyzで動作しています。

- **[NIP-AD：MCPサーバーアナウンス](https://github.com/nostr-protocol/nips/pull/2221)**（2月12日オープン）：Nostr上のModel Context ProtocolサーバーとスキルのアナウンスをTENEXプラットフォームで既に使用中の形式で標準化します。

**その他のオープンPR：**

- **[NIP-144：サービス認証プロトコル](https://github.com/nostr-protocol/nips/pull/2232)**：クライアントがNostr上のサービスプロバイダーにアイデンティティと権限を証明する方法を定義します。

- **[NIP-DC：Nostr Webxdc](https://github.com/nostr-protocol/nips/pull/2230)**：alexgleasonがWebxdc（分散型ウェブアプリケーション）とNostr eventの統合を提案しています。

## NIPディープダイブ：NIP-55（Android署名アプリケーション）

[NIP-55](https://github.com/nostr-protocol/nips/blob/master/55.md)はAndroid向けNostrクライアントが専用の署名アプリケーションに暗号操作をリクエストする方法を定義します。今週[White Noise v0.3.0](#white-noise-v030)と[Unfiltered v1.0.6](#unfiltered-v106)の両方がAmberサポートを追加したため、Android署名プロトコルを詳しく見ていきます。

**通信チャンネル：**

NIP-55は2つのメカニズムを通じてアプリ間署名を可能にします。インテントは一回限りの操作に視覚的フィードバック付きの手動ユーザー承認を提供します。コンテンツリゾルバーはユーザーが永続的な権限を付与した場合の自動署名を可能にし、繰り返しのプロンプトなしにバックグラウンドでアプリが署名できます。

通信はカスタムの`nostrsigner:`URIスキームを使用します。クライアントは次のように接触を開始します：

```
nostrsigner:<base64-encoded-event>?type=sign_event&callbackUrl=myapp://callback
```

**サポートされる操作：**

仕様は7つの暗号メソッドを定義します。イベント署名（`sign_event`）、公開鍵取得（`get_public_key`）、[NIP-04](/ja/topics/nip-04/)暗号化・復号化、[NIP-44](/ja/topics/nip-44/)暗号化・復号化、zapイベント復号化（`decrypt_zap_event`）です。

**パーミッションモデル：**

クライアントは信頼関係を確立するために`get_public_key`を一度呼び出し、署名者のパッケージ名とユーザーのpubkeyを受け取ります。仕様はクライアントがこれらの値を保存し、`get_public_key`を再度呼び出さないことを義務付けており、フィンガープリンティング攻撃を防ぎます。

署名リクエストに対して、ユーザーは一度承認するかバックグラウンド操作のために「選択を記憶」を付与できます。ユーザーが操作を繰り返し拒否する場合、署名者は「rejected」ステータスを返して繰り返しのプロンプトを防ぎます。

**実装：**

[Amber](https://github.com/greenart7c3/amber)はAndroid向けの主要なNIP-55署名者です。NIP-55をサポートするクライアントには[Amethyst](https://github.com/vitorpamplona/amethyst)、[White Noise](#white-noise-v030)、[Unfiltered](#unfiltered-v106)などがあります。ウェブアプリケーションは署名者のレスポンスを直接受信できず、コールバックURLまたはクリップボード操作を使用する必要があります。

**他の署名NIPとの関係：**

NIP-55は[NIP-07](/ja/topics/nip-07/)（ブラウザ拡張機能）と[NIP-46](/ja/topics/nip-46/)（relay経由のリモート署名）を補完します。NIP-07がデスクトップブラウザを処理し、NIP-46がクロスデバイス署名を処理するのに対し、NIP-55は最小限のレイテンシでネイティブAndroid統合を提供します。

## NIPディープダイブ：NIP-60（Cashuウォレット）

[NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md)は[Cashu](/ja/topics/cashu/) ecashウォレットがNostr relay上に状態を保存し、クロスアプリケーションのウォレット同期を可能にする方法を定義します。[Ridestr v0.2.6](#ridestr-v026)がデバイス間のウォレット同期にNIP-60を使用しているため、このプロトコルを詳しく見ていきます。

**イベントの種類：**

NIP-60は4つのイベントタイプを使用します。置換可能なkind 17375はミントURLとP2PK ecash支払いを受け取るための専用秘密鍵を含むウォレット設定を保存します。トークンイベント（kind 7375）は未使用の暗号証明を含み、支払い履歴（kind 7376）はユーザーの透明性のためにトランザクションを記録します。オプションのkind 7374はミント支払いクォートを追跡します。

**ウォレットアーキテクチャ：**

ウォレット状態はrelayに存在し、アプリケーション間でアクセスできます。ユーザーのウォレットイベントにはCashuミントへの暗号化された参照と、ユーザーのNostrアイデンティティとは別のウォレット専用秘密鍵が含まれます。この分離は重要です。ウォレット鍵はecash操作を処理し、Nostr鍵はソーシャル機能を処理します。

```json
{
  "kind": 17375,
  "content": "<nip44-encrypted-wallet-config>",
  "tags": [["d", "cashu-wallet"]]
}
```

**証明の管理：**

Cashuの証明は無記名証券です。一度使われると証明は無効になります。NIP-60はロールオーバーメカニズムでこれを管理します。支払い時にクライアントは残りの未使用証明を持つ新しいトークンイベントを作成し、[NIP-09](/ja/topics/nip-09/)を通じて元のものを削除します。破棄されたトークンIDは状態追跡のために`del`フィールドに入ります。

クライアントは以前に使われた証明を検出するためにミントに対して証明を定期的に検証する必要があります。ミントごとに複数のトークンイベントが許可されており、支払い履歴イベントはオプションであってもユーザーがトランザクションを追跡するのに役立ちます。

**セキュリティモデル：**

すべての機密データは[NIP-44](/ja/topics/nip-44/)暗号化を使用します。ウォレット秘密鍵は平文では現れません。relayは内容を理解せずに暗号化されたblobを保存するため、ウォレット状態は信頼できないrelayでもプライベートのままです。

**実装：**

NIP-60をサポートするウォレットには[Nutsack](https://github.com/gandlafbtc/nutsack)と[eNuts](https://github.com/cashubtc/eNuts)があります。[Ridestr](#ridestr-v026)のようなクライアントはクロスデバイス同期にNIP-60を使用し、デスクトップでチャージしてモバイルから手動転送なしに使えます。

---

今週は以上です。構築中のプロジェクトや共有したいニュースがあれば、<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">NIP-17 DMでお問い合わせください</a>。Nostrでもお待ちしています。
