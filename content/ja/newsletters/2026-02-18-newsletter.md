---
title: 'Nostr Compass #10'
date: 2026-02-18
translationOf: /en/newsletters/2026-02-18-newsletter.md
translationDate: 2026-02-18
draft: false
type: newsletters
---

Nostr Compassへようこそ。Nostrの週刊ガイドです。

**今週の内容:** BlossomのローカルキャッシュレイヤーがAndroid向けオフラインメディアアクセスを目指す独立プロジェクトの収束として形になっています。AlbyがNostr Wallet Connect統合のビルドとテストを実際の資金なしで行える[NWC開発者サンドボックス](https://sandbox.albylabs.com)を立ち上げました。AIエージェント通信に関する競合提案が同じ週に2人の著者から届きました。fiatjafがリレー運営者がほとんど採用しなかった保持ポリシー、国コード、プライバシーポリシー、コミュニティ設定タグを削除し、[NIP-11](https://github.com/nostr-protocol/nips/pull/1946)から未使用フィールドを除去しました。[NIP-85](https://github.com/nostr-protocol/nips/pull/2223)がTrusted AssertionsのサービスプロバイダーのDiscoverability指針としてマージされました。[NIP-52](https://github.com/nostr-protocol/nips/pull/1752)の新しい`D`タグがカレンダーイベントの日単位タイムスタンプインデックスを可能にします。新プロジェクトとして、分散型マップタイル配布の[Mapnolia](https://github.com/zeSchlausKwab/mapnolia)、MLS暗号化メッセージングの[Pika](https://github.com/sledtools/pika)、Android向けFROST閾値署名の[Keep](https://github.com/privkeyio/keep-android)、Nostr統合コンテンツアドレス型ストレージの[Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree)、AndroidアプリからNostrへコンテンツを共有する[Prism](https://github.com/hardran3/Prism)が登場しています。[Primal Android](https://github.com/PrimalHQ/primal-android-app)がデュアルウォレットサポートと自動サービスライフサイクル管理を追加する11件のNWC PRをマージ。[Mostro Mobile](https://github.com/MostroP2P/mobile)がNWC統合による[内蔵Lightningウォレット](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2)を出荷。[Notedeck](https://github.com/damus-io/notedeck)がAndroidアプリストアリリースに向けて準備し、HAVENがマルチnpubサポートとクラウドバックアップを備えた[v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3)に到達。今週のディープダイブでは、Web of Trust計算をサービスプロバイダーに委任するNIP-85のTrusted Assertionsシステムと、日単位インデックス更新後のNIP-52カレンダーイベントプロトコルを取り上げます。

## ニュース

### Blossomローカルキャッシュレイヤーが登場

複数の独立プロジェクトが同じ問題に収束しています。モバイルデバイスでの[Blossom](/ja/topics/blossom/)メディアへのオフラインアクセスです。

[Morganite](https://github.com/greenart7c3/Morganite)は、[Amber](https://github.com/greenart7c3/amber)と[Citrine](https://github.com/greenart7c3/Citrine)の開発者greenart7c3による新しいAndroidアプリで、Blossomメディアのクライアントサイドキャッシングを実装しています。ユーザーはネットワーク接続なしに以前に閲覧した画像やファイルにアクセスできます。

[Aerith](https://github.com/hardran3/Aerith)が画像ラベリング、一括ミラー・タグ・削除操作、ラベルとファイルタイプによるフィルタリング、初期ローカルBlossomキャッシュサポートを備えた[v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2)を出荷しました。Aerithは複数のBlossomサーバーにメディアを保存するユーザーがblobを整理・ミラーリングするための管理インターフェースです。

Blossom仕様に新しい[ローカルキャッシュ実装ガイド](https://github.com/hzrd149/blossom/blob/master/implementations/local-blossom-cache.md)が追加され、クライアントサイドのblobストレージが文書化されました。一方、[Prism](https://github.com/hardran3/Prism)（Aerithと同じ開発者による）がAndroidのNostrへ共有フローにBlossomアップロード統合を追加。今週4つの独立プロジェクトが同じ問題に収束しました。専用キャッシュアプリ、メディアマネージャー、リファレンス仕様、Blossom統合を持つ共有ツールが、すべて単純なアップロード・取得を超えた永続的なローカルストレージを実装しています。

### Alby NWC開発者サンドボックス

[Alby](https://sandbox.albylabs.com)が[Nostr Wallet Connect（NIP-47）](/ja/topics/nip-47/)でビルドする開発者向けサンドボックス環境を立ち上げました。このサンドボックスはホスト型NWCウォレットサービスを提供し、開発者は実際のLightningウォレットに接続することなくテスト接続を作成してシミュレート決済を送信し、NWCイベントのリクエスト・レスポンスサイクル全体をリアルタイムで観察できます。開発者はサンドボックスから`nostr+walletconnect://`接続文字列を生成してクライアントに渡します。するとサンドボックスがクライアントとウォレットサービス間を流れるkind 23194リクエストとkind 23195レスポンスイベントを表示します。

これにより新しいNWC統合の参入障壁が下がります。以前はテストに個人のLightningウォレットまたはセルフホスト型NWCサービスが必要でした。サンドボックスはそれを抽象化し、`pay_invoice`、`get_balance`、`make_invoice`、`lookup_invoice`、`list_transactions`メソッドをライブNWCエンドポイントに対して実装するための即時フィードバックループを開発者に提供します。

### AIエージェントNIPが登場

Nostr上のAIエージェント通信に関する提案が数日以内に登場し、異なる角度から問題にアプローチしています。

joelklaboによる[NIP-XX: AI Agent Messages](https://github.com/nostr-protocol/nips/pull/2226)はAIエージェントインタラクションの完全なプロトコルを定義しています。プロンプト、レスポンス、ストリーミングデルタ、ステータス更新、ツールテレメトリ、エラー、キャンセル、機能ディスカバリー用のevent kindです。`ai.info`ディスカバリーイベント（kind 31340、置換可能）でエージェントがサポートするモデル、スキーマ付きツール、ストリーミングサポート、レート制限をアナウンスできます。joelklaboの提案にはプロンプトIDによるラン相関、セッション管理、シーケンス順序によるストリーム照合、メタデータプライバシー用の[NIP-59](/ja/topics/nip-59/)ガイダンスが含まれています。

pablof7zによる[NIP-AE: Agents](https://github.com/nostr-protocol/nips/pull/2220)は異なるアプローチを取り、エージェントのインスタンス化のためのkindを定義しています。定義とレッスンです。これらはpablof7zがNostr上に構築された自律学習システム[TENEX](https://github.com/tenex-chat/tenex)で使用するeventタイプです。同じくpablof7zによるコンパニオン提案[NIP-AD: MCP Server and Skill Announcements](https://github.com/nostr-protocol/nips/pull/2221)はNostr上で[Model Context Protocol](https://modelcontextprotocol.io/)サーバーとスキルをアナウンスするためのeventを定義しています。[NIP-22](/ja/topics/nip-22/)コメントがサポートされているため、コミュニティはNostr上で直接MCPサーバーについて議論・評価できます。

NIP-XXがエージェント通信全体をカバーし、NIP-AEとNIP-ADがアイデンティティとツールディスカバリーに対応します。これらの提案は統一された標準に収束するか、補完的なレイヤーとして共存するかもしれません。

## リリース

### HAVEN v1.2.0-rc3

[Blossom](/ja/topics/blossom/)メディアサーバーと4つのリレー機能をバンドルしたオールインワンパーソナルリレーの[HAVEN](https://github.com/bitvora/haven)が[v1.2.0-rc3](https://github.com/bitvora/haven/releases/tag/v1.2.0-rc3)に到達しました。このリリース候補では複数のnpubサポートが追加され、単一のHAVENインスタンスで複数のNostrアイデンティティを提供できます。以前のRCではクラウドバックアップ用の`--from-cloud`と`--to-cloud`フラグ（RC2）が追加され、Web of Trustの二重カウントバグが修正されました（RC1）。

### Mostro Mobile v1.2.0：内蔵Lightningウォレット

[Mostro](https://github.com/MostroP2P/mostro) P2P Bitcoin取引所のモバイルクライアント[Mostro Mobile](https://github.com/MostroP2P/mobile)（[先週取り上げたv1.1.0](/ja/newsletters/2026-02-11-newsletter/#mostroが初のパブリックベータを公開)）が、完全な[NWC（NIP-47）](/ja/topics/nip-47/)統合による内蔵Lightningウォレットを備えた[v1.2.0](https://github.com/MostroP2P/mobile/releases/tag/v1.2.0%2B2)を出荷しました。買い手と売り手はインボイスの処理にアプリを切り替える必要がなくなりました。アプリが売り手向けにホールドインボイスを検出して接続ウォレット経由で自動的に支払い、買い手は自動的なインボイス生成を受けられます。このリリースは同週前半の[v1.1.1](https://github.com/MostroP2P/mobile/releases/tag/v1.1.1%2B1)に続くもので、信頼できるインスタンスの厳選レジストリを持つマルチMostroノードサポート、ノード表示用のkind 0メタデータ取得、pubkeyによるカスタムノード管理、選択したノードがオフラインになった際の自動フォールバックが追加されました。

サーバー側では[Mostro v0.16.2](https://github.com/MostroP2P/mostro/releases/tag/v0.16.2)がリリースされ、重複開発手数料支払いの修正、パスワード検証RPCエンドポイントのレート制限、協調キャンセル時の適切な紛争クリーンアップが含まれています。

新しいコンパニオンプロジェクト[mostro-skill](https://github.com/MostroP2P/mostro-skill)により、エージェントがNostrを通じてMostroで取引できます。

### Aerith v0.2

[Blossom](/ja/topics/blossom/)画像マネージャーの[Aerith](https://github.com/hardran3/Aerith)が、メディア整理用の画像ラベル、サーバー間の一括ミラー・タグ・削除操作、ラベルとファイルタイプによるフィルタリング、初期ローカルキャッシュサポートを備えた[v0.2](https://github.com/hardran3/Aerith/releases/tag/v0.2)を出荷しました。ローカルキャッシュトレンドの全体的な文脈については[ニュースセクション](#blossomローカルキャッシュレイヤーが登場)を参照してください。

### Mapnolia：Nostr経由の分散型マップタイル

[Mapnolia](https://github.com/zeSchlausKwab/mapnolia)は、[PMTiles](https://github.com/protomaps/PMTiles)マップアーカイブを地理的地域にチャンク化し、分散型ディスカバリーのためにNostr上でアナウンスする新しい地理空間データサーバーです。kind 34444のパラメータ化された置換可能イベントをNostrリレーに公開し、マップタイルチャンクの完全なインデックス、レイヤーメタデータ、ジオハッシュ地域、ファイル参照、[Blossom](/ja/topics/blossom/)サーバー詳細を含みます。

クライアントは中央集権的なタイルサーバーの代わりにNostrネットワークを通じてマップデータを発見・取得します。アナウンスイベントにはリストされたBlossomサーバーから必要な地理的地域のみをリクエストするのに十分なメタデータが含まれています。Mapnoliaは地理空間データ配布をNostrにもたらす最初のプロジェクトで、オフライン対応マッピングアプリケーションの可能性を開きます。

### Pika：MarmotベースのE2E暗号化メッセージング

[Pika](https://github.com/sledtools/pika)は、Nostrリレー上に[Messaging Layer Security（MLS）](/ja/topics/mls/)をレイヤー化する[Marmot](/ja/topics/marmot/)プロトコルを使用したiOSとAndroid向けの新しいE2E暗号化メッセージングアプリです。アーキテクチャは関心事を分離しており、Nostrリレー経由のMLSステート管理とメッセージ暗号化・復号化を処理するRustコア（`pika_core`）と、SwiftUI（iOS）とKotlin（Android）のシンネイティブUIシェルで構成されています。ステートはUniFIとJNIバインディングを通じてUIからRustアクターへのアクション、そして状態とリビジョン番号のスナップショットをUIに返す一方向フローで流れます。

PikaはNostrリレーをMLSで暗号化された暗号文のトランスポートレイヤーとして使用する[White Noise](https://github.com/marmot-protocol/whitenoise)、[Vector](https://github.com/VectorPrivacy)、[0xchat](https://0xchat.com)と並ぶ成長中のMLS-on-Nostrメッセンジャー分野に加わります。すべてがNostrリレーをMLSで暗号化された暗号文のトランスポートレイヤーとして使用し、リレー運営者はメッセージ内容を読めません。PikaはMLS実装にMarmot Development Kit（MDK）を、リレー接続にnostr-sdkを使用しています。

### Keep：Android向け[FROST](/ja/topics/frost/)閾値署名

[Keep](https://github.com/privkeyio/keep-android)は、単一デバイスが完全な秘密鍵を保持しない[FROST](/ja/topics/frost/)閾値署名のための新しいAndroidアプリケーションです。[NIP-55](/ja/topics/nip-55/)（Android Signer）と[NIP-46](/ja/topics/nip-46/)（リモート署名）を実装しており、互換Nostrクライアントが鍵素材をデバイス間で分散したまま署名をリクエストできます。デフォルト設定は2-of-3と3-of-5ですが、任意のt-of-n閾値がサポートされています。

KeepのDKG（分散鍵生成）セレモニーはカスタムevent kindを使用してNostrリレー上で実行されます。kind 21101はグループアナウンス、kind 21102はラウンド1コミットメント多項式（公開ブロードキャスト）、kind 21103はラウンド2シークレットシェア（参加者間の[NIP-44](/ja/topics/nip-44/)暗号化ポイントツーポイント）です。グループ秘密鍵スカラーはDKG中にどこでも計算・組み立てられません。各デバイスは多項式評価シェアのみを保持し、任意のtシェアが2ラウンドのコミット・次に署名プロトコルを通じて有効なSchnorr署名を生成できます。結果の64バイト署名は単一署名者のSchnorr署名と区別できません。内部的にKeepはZcash Foundationの`frost-secp256k1-tr`クレートをTaproot調整で使用しており、グループ公開鍵がNostr npubとして直接機能します。

Keepは[Igloo Desktop](https://github.com/FROSTR-ORG/igloo-desktop)、[Igloo for Android](https://github.com/FROSTR-ORG/igloo-android)、[Frost2x](https://github.com/FROSTR-ORG/frost2x)、[Igloo for iOS](https://github.com/FROSTR-ORG/igloo-ios)と並ぶ[Frostr](https://frostr.org)ファミリーに加わり、Nostrにおける閾値鍵管理の選択肢を拡げます。

### Prism：AndroidアプリからNostrへ何でも共有

[Prism](https://github.com/hardran3/Prism)は、ユーザーが電話上の任意のアプリからテキスト、URL、画像、動画をNostrに公開できるよう、システム共有ターゲットとして登録する新しいAndroidアプリ（Kotlin/Jetpack Compose、API 26+）です。共有URLはノートに組み込まれる前にトラッキングパラメータ除去ツールを通過します。PrismはOpenGraphメタデータを取得してリッチリンクプレビューを生成し、ネイティブNostr参照（`note1`、`nevent1`）をインラインでレンダリングします。

スケジューリングエンジンはAndroidバッテリー最適化をバイパスするハイブリッドな`AlarmManager`/`WorkManager`アプローチを使用しています。AlarmManagerが正確なウェイクアップタイミングを処理し、エクスペディットWorkManagerタスクがデリバリーを保証し、オフラインシナリオには指数バックオフリトライがあります。メディアアップロードは画像と動画フレームのサムネイル生成を備えた設定可能な[Blossom](/ja/topics/blossom/)サーバーを通過します。すべてのevent署名は[Amber](https://github.com/greenart7c3/amber)のような[NIP-55](/ja/topics/nip-55/)外部署名者に委任され、アイデンティティ切り替えのマルチアカウントサポートがあります。Prismは[NIP-84（ハイライト）](/ja/topics/nip-84/)投稿もサポートしています。[Aerith](#aerith-v02)と同じ開発者によるものです。

### Hashtree：Nostr統合コンテンツアドレス型ストレージ

[Hashtree](https://files.iris.to/#/npub1xndmdgymsf4a34rzr7346vp8qcptxf75pjqweh8naa8rklgxpfqqmfjtce/hashtree)は、MerkleルートをNostr上に公開することでミュータブルなnpub/パスアドレスを作成するファイルシステムベースのコンテンツアドレス型blobストレージシステムです。このシステムは任意のキー・バリューストアで動作する「ダムストレージ」を使用し、コンテンツを[Blossom](/ja/topics/blossom/)アップロードに最適化された2MBブロックにチャンク化します。BitTorrentとは異なり、アクティブなMerkle証明計算は不要で、ハッシュでblobを保存・取得するだけです。

Nostr統合により、`htree://npub.../repo-name`のようなgitリモートURLでリポジトリをクローンでき、`htree publish mydata <hash>`のようなコマンドで`npub.../mydata`アドレスにコンテンツハッシュを公開できます。包括的なCLIは暗号化（デフォルト）とパブリックストレージモード、コンテンツピン止め、Blossomサーバーへのプッシュ、Nostrアイデンティティ管理をサポートしています。各保存アイテムは生バイトまたはツリーノードで、Nostrのリレーネットワークを通じた分散型コンテンツ配布の基盤を提供します。

### Espy：Shakespeare上のカラーパレットキャプチャ

[Shakespeare](https://soapbox.pub/tools/shakespeare/)プラットフォーム上に構築された[Espy](https://espy.you)は、ユーザーが写真からカラーパレットをキャプチャしてNostrイベントとして共有できるアプリです。ShakespeareはNIP-07ブラウザ拡張機能でユーザーを認証し、組み込みのNostrリレー接続を提供するAIパワードアプリビルダーで、開発者は独自の鍵管理やリレープールを実装せずにアプリを出荷できます。Espyはカメラ入力から支配的な色を抽出し、標準的なNostrフィードで発見可能な共有可能なパレットカードにします。

### Flotilla 1.6.4

hodlbodのDiscordライクなNostrクライアント[Flotilla](https://gitea.coracle.social/coracle/flotilla)がリレーをグループとして整理する[1.6.4](https://gitea.coracle.social/coracle/flotilla/releases/tag/1.6.4)を出荷しました。Coracleファミリーのプロジェクトがセルフホスト型[Gitea インスタンス](https://gitea.coracle.social/coracle)に移行しました。このリリースはNIP-9a経由のプッシュ通知とウォレット受信フロー、分類リストとスペースURLサポートを追加。インターフェースの改善にはモーダルと通知処理のクリーンアップが含まれています。モバイルでのルームミュートとセーフエリアインセットも変更点で、SafariでのSOURCE画像アップロードとカレンダーイベント詳細の修正もあります。

### Shosho v0.12.0

Nostr統合モバイルライブストリーミングアプリ[Shosho](https://github.com/r0d8lsh0p/shosho-releases)が[v0.12.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.12.0)を出荷しました。このリリースはインプレーヤーリプライとカスタム絵文字統合を備えた動画クリップを追加。スレッド保護が間接的なメンションスパムをブロックし、新しいQR共有機能でユーザーがオフラインでプロフィールを交換できます。新しいホリゾンタル再生モードでストリームにTwitchスタイルの視聴体験が生まれ、ブラウズ画面にライブストリームと並んでクリエイタークリップが表示されます。

### Granary v10.0

Nostr、Bluesky、ActivityPub、その他のプラットフォーム間でデータを共通フォーマットに変換するソーシャルウェブ変換ライブラリ[Granary](https://github.com/snarfed/granary)が、重大な変更を含む[v10.0](https://github.com/snarfed/granary/releases/tag/v10.0)を出荷しました。このリリースはNostrのデフォルトActivityStreams 1 IDをbech32からhexに切り替え、[NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md)メンション解析とarticleタグを含む拡張Nostrサポートを追加します。コンバーター全体の新しい複数出力オプションにより、開発者がプロトコル間でバッチ変換できます。

### Nostr MCP Server v3.0.0

AIエージェントがNostrネットワークとインタラクションできる[Model Context Protocol](https://modelcontextprotocol.io/)サーバーの[Nostr MCP Server](https://github.com/AustinKelsay/nostr-mcp-server)が[v3.0.0](https://github.com/AustinKelsay/nostr-mcp-server/releases/tag/v3.0.0)を出荷しました。このメジャーリリースはソーシャルアクション（フォロー、リアクション、リポスト、リプライ）と[NIP-65](https://github.com/nostr-protocol/nips/blob/master/65.md)サポートに加えてオプションの[NIP-42](/ja/topics/nip-42/)認証を含むリレーリスト管理を追加します。[NIP-17](/ja/topics/nip-17/)と[NIP-44](/ja/topics/nip-44/)経由のダイレクトメッセージも新しく追加されました。このリリースは今週の[AIエージェントNIP提案](#aiエージェントnipが登場)とペアになり、Nostr上で活動するエージェントの実用的なツールとなります。

### Aegis v0.3.8

クロスプラットフォームNostr署名者[Aegis](https://github.com/ZharlieW/Aegis)が、多言語UIサポートと内蔵Nostrアプリブラウザーのインクリメンタルアップデートマネージャーを備えた[v0.3.8](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.8)を出荷しました。新しいアップデートメカニズムはローカル状態に対してインクリメンタルにdiffし、Nostrウェブアプリのアプリ内ディレクトリを低帯域幅使用量で最新に保ちます。このリリースでは連続して複数のeventに署名する際のデータベースラウンドトリップを削減するため、5分間の鍵素材キャッシングも導入されます。

### SNSTR v0.3.1

NostrプロトコルのTypeScriptライブラリ[SNSTR](https://github.com/AustinKelsay/snstr)（Secure Nostr Software Toolkit for Renegades）が[v0.3.1](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.1)を出荷しました。このリリースはすべてのエントリーポイントがnpmタービューに含まれることを確認するパッケージ検証ガードを追加し、NodeとBunのCIエンフォースメントがあります。[v0.3.0](https://github.com/AustinKelsay/snstr/releases/tag/v0.3.0)も同じ週に出荷されました。

### Citrine v2.0.0-pre1

greenart7c3によるAndroid Nostrリレー[Citrine](https://github.com/greenart7c3/Citrine)が、最適化されたデータベースインデックスとKotlinコルーチン処理の改善によるパフォーマンス向上を含む[v2.0.0-pre1](https://github.com/greenart7c3/Citrine/releases/tag/v2.0.0-pre1)をリリースしました。このリリースはウェブアプリのホスティングサポートも強化し、各アプリが独自ポートで動作するようになりました。

## プロジェクトアップデート

### Primal Android：NWCインフラ拡張

[Primal Android](https://github.com/PrimalHQ/primal-android-app)が今週11件のNWC関連PRをマージし、[2週間前に開始した](/ja/newsletters/2026-02-04-newsletter/#primal-android-ships-nwc-encryption)構築を継続しました。このバッチはデュアルウォレットNWCサポート、バックエンド通知に連動した自動サービスの開始・停止、ウォレットタイプによる接続ルーティング、ウォレット削除時の適切なデータクリーンアップを追加します。NWCサービスがウォレット接続状態に基づいて独自のライフサイクルを管理するようになり、ユーザーの手動操作が減ります。

### Notedeck：Androidアプリストアの準備

[Damus](https://github.com/damus-io/damus)チームによるマルチプラットフォームNostrクライアント[Notedeck](https://github.com/damus-io/notedeck)が今週[Androidアプリストアリリース準備](https://github.com/damus-io/notedeck/pull/1287)をマージしました。このPRはGoogle Playが要求するUGC（ユーザー生成コンテンツ）コンプライアンスプランを追加しており、利用規約同意画面、コンテキストメニューと設定からのユーザーブロック、レポートイベントをリレーに公開する[NIP-56（報告）](/ja/topics/nip-56/)機能、コンテンツ・安全設定セクションが含まれます。署名済みリリースAPKとAAB（Android App Bundle）を新しいMakefileターゲット経由で生成するビルドインフラも追加されました。EULAドキュメントが17歳以上の要件とNostr固有の分散型コンテンツに関する免責事項を定めています。コンプライアンス機能自体はフォローアップPRで出荷されます。このマージはドキュメントと署名の基盤を整えるものです。

Damus iOS側では、コンテンツがロード済みにもかかわらずスピナーが永続する[無限ローディングスピナーのリグレッション](https://github.com/damus-io/damus/pull/3593)の修正が入りました。

### Nostria：ディスカバリーリレーとDM修正

クロスプラットフォームNostrクライアント[Nostria](https://github.com/nostria-app/nostria)が今週9件のPRをマージしました。最も注目すべきものはプロフィールルックアップ用の[ディスカバリーリレーの自動初期化](https://github.com/nostria-app/nostria/pull/460)を追加し、新規ユーザーが手動設定なしにリレー接続を得られます。その他の修正は[DMテキストエリアの折り返し](https://github.com/nostria-app/nostria/pull/466)、[フルスクリーン動画ビューポートフィル](https://github.com/nostria-app/nostria/pull/479)、[リポストプレビューでのarticleメタデータ抽出](https://github.com/nostria-app/nostria/pull/481)、[通知でのnostr: URI解決](https://github.com/nostria-app/nostria/pull/458)に対応しています。

### Camelus：Riverpod v3移行

FlutterベースのNostrクライアント[Camelus](https://github.com/camelus-hq/camelus)が今週5件のPRをマージし、[Riverpod v3 API移行](https://github.com/camelus-hq/camelus/pull/158)と[汎用フィードリファクタリング](https://github.com/camelus-hq/camelus/pull/159)を中心とした作業を行いました。[組み込みノートキャッシュ](https://github.com/camelus-hq/camelus/pull/161)が引用ノートの冗長なリレー取得を回避します。

## NIPアップデート

[NIPsリポジトリ](https://github.com/nostr-protocol/nips)への最近の変更：

**マージ済み：**

- **[NIP-85：サービスプロバイダーDiscoverability](https://github.com/nostr-protocol/nips/pull/2223)**：vitorpamplonaがリレーヒントとアルゴリズム固有のサービスキーを含む[NIP-85 Trusted Assertions](/ja/topics/trusted-relay-assertions/)サービスプロバイダーのクライアントディスカバリープロセスに関するガイダンスを追加しました。詳細は[下記のディープダイブ](#nipディープダイブnip-85-trusted-assertions)を参照してください。

- **[NIP-11：リレー情報のクリーンアップ](https://github.com/nostr-protocol/nips/pull/1946)**：fiatjafが[NIP-11](/ja/topics/nip-11/)から`privacy_policy`、`retention`配列、`relay_countries`、コミュニティ設定ブロックを削除しました。リレー運営者はこれらのフィールドをほとんど使用せず、クライアントもそれらに基づいた動作をしていませんでした。

- **[NIP-52：日単位タイムスタンプタグ](https://github.com/nostr-protocol/nips/pull/1752)**：staabが[NIP-52](/ja/topics/nip-52/)の時間ベースカレンダーイベント（kind 31923）に必須の`D`タグを追加しました。`floor(unix_seconds / 86400)`として計算される日単位Unixタイムスタンプを表し、複数の`D`タグが複数日イベントをカバーし、完全なタイムスタンプを解析せずに効率的な時間インデックスを可能にします。

- **[NIP-47：簡素化](https://github.com/nostr-protocol/nips/pull/2210)**：[ニュースレター#9で取り上げた](/ja/newsletters/2026-02-11-newsletter/)簡素化PRが今週マージされ、[NIP-47（Nostr Wallet Connect）](/ja/topics/nip-47/)から`multi_pay_invoice`と`multi_pay_keysend`が削除されました。完全なNWCプロトコルディープダイブは[ニュースレター#8](/ja/newsletters/2026-02-04-newsletter/#nipディープダイブnip-47-nostr-wallet-connect)を参照してください。

**オープンPRとディスカッション：**

- **[NIP-74：ポッドキャスト](https://github.com/nostr-protocol/nips/pull/2211)**：[ニュースレター#8](/ja/newsletters/2026-02-04-newsletter/)で取り上げたこのポッドキャスト仕様提案が今週活発な議論を展開しました。staabはすでに少なくとも3つの競合するポッドキャスト標準が実際に存在すると指摘し、derekrossは6ヶ月前からアクティブなアプリとポッドキャストを持つ既存の実装を示しました。実装間の収束がNIP番号を割り当てられる前に必要です。

- **[NIP-XX：AIエージェントメッセージ](https://github.com/nostr-protocol/nips/pull/2226)**：joelklaboがプロンプト、レスポンス、ストリーミング、ツールテレメトリ、エラー、機能ディスカバリー用のevent kindを持つ完全なAIエージェント通信プロトコルを提案しています。今週のすべてのAI提案のカバレッジは[ニュースセクション](#aiエージェントnipが登場)を参照してください。

- **[NIP-PNS：プライベートノートストレージ](https://github.com/nostr-protocol/nips/pull/1893)**：jb55のプライベートノートシステムは、誰が書いたかを明らかにすることなく暗号化された個人ノートをリレーに保存するためのkind 1080イベントを定義しています。このスキームはHKDFを通じてユーザーのnsecから決定論的な仮名キーペアを導出します。`pns_key = hkdf_extract(ikm=device_key, salt="nip-pns")`、そしてその導出キーからsecp256k1キーペアを生成します。2番目の導出が対称暗号化キーを生成します。`pns_nip44_key = hkdf_extract(ikm=pns_key, salt="nip44-v2")`。内部ノートはこのキーで[NIP-44](/ja/topics/nip-44/) v2で暗号化され、仮名pubkeyで公開されるため、リレーはユーザーのメインキーにリンクされていないアイデンティティからのkind 1080イベントを見ます。[NIP-59](/ja/topics/nip-59/)のギフトラップとは異なり、PNSはスパム不可能（仮名キーは決定論的でランダムではない）でゼロのパブリックメタデータを持ちます（受信者がいないので`p`タグが不要）。今週、jb55がNotedeck のRustバックエンド（`enostr::pns`モジュール）でPNSを実装した際の所見を投稿しました。仕様の`hkdf_extract`呼び出しがRFC 5869 HKDFに2つのフェーズ（抽出と展開）があり異なる出力を生成し、ほとんどのライブラリが両方を期待するため曖昧であることを特定しました。`pns_nip44_key`がNIP-44の通常のECDH鍵合意をバイパスして会話キーとして直接使用されることを明確化しました。これはほとんどのNIP-44ライブラリがデフォルトでECDHを使用するため実装者が知る必要がある詳細です。参照実装のTypeScriptで未定義変数も指摘しました。元々2025年4月からのこのPRが今積極的に実装されています。

- **[NIP-AE：エージェント](https://github.com/nostr-protocol/nips/pull/2220)**：pablof7zが[TENEX](https://github.com/tenex-chat/tenex)での作業から得たNostr上のエージェントアイデンティティのための4つのevent kindを定義しています。基本テンプレートはkind 4199（エージェント定義）で、タイトル、役割説明、システム指示、ツール宣言、バージョンを持ちます。動作モディファイアーはkind 4201（エージェントナッジ）に存在し、実行時の機能制御のために`only-tool`、`allow-tool`、`deny-tool`タグを使用します。エージェントは学習内容をkind 4129（エージェントレッスン）イベントとして公開し、`e`タグで親定義にリンクし、[NIP-22](/ja/topics/nip-22/)コメントスレッドで洗練されます。所有権検証はkind 14199を使用し、エージェントpubkeyをリストする置換可能イベントで、エージェントのkind 0プロフィールの`p`タグと照合した際に双方向チェーンを確立します。

- **[NIP-AD：MCPサーバーとスキルアナウンス](https://github.com/nostr-protocol/nips/pull/2221)**：pablof7zがNostr上で[Model Context Protocol](https://modelcontextprotocol.io/)サーバーと個々のスキルをアナウンスするためのeventを定義しています。MCPサーバーアナウンスはサーバーのエンドポイントURLとサポートされるプロトコルバージョン、入力スキーマ付きの利用可能ツールリストを持ちます。サーバーアナウンスに[NIP-22](/ja/topics/nip-22/)コメントがサポートされているため、コミュニティはNostr上で直接MCPサーバーを議論・評価できます。

- **[NIP-73：OSMタグkind](https://github.com/nostr-protocol/nips/pull/2224)**：DestBroがISBN（書籍）、ISAN（映画）、ポッドキャストフィード（GUID）、ジオハッシュ、URLなどの外部コンテンツへのNostrイベント参照を`i`と`k`タグで標準化する[NIP-73（外部コンテンツID）](/ja/topics/nip-73/)にOpenStreetMap識別子の追加を提案しています。提案されたOSM kindにより、イベントがOpenStreetMapのノードまたはウェイIDで特定の地図フィーチャー（建物、道路、公園）を参照でき、Nostrコンテンツをオープンな地理データベースに接続します。

- **[NIP-XX：レスポンシブ画像バリアント](https://github.com/nostr-protocol/nips/pull/2219)**：woikosが[NIP-94](/ja/topics/nip-94/)ファイルメタデータイベントを異なる解像度のレスポンシブ画像バリアント用のタグで拡張することを提案しています。クライアントが表示サイズとネットワーク条件に基づいて適切なバリアントを選択でき、[Blossom](/ja/topics/blossom/)サーバーにホストされた高解像度画像を閲覧するモバイルユーザーの帯域幅を削減します。

## NIPディープダイブ：NIP-85（Trusted Assertions）

[NIP-85](https://github.com/nostr-protocol/nips/blob/master/85.md)は高コストな計算を信頼できるサービスプロバイダーに委任し、そのプロバイダーが署名済みの結果をNostrイベントとして公開するシステムを定義しています。Web of Trustスコアとエンゲージメントメトリクスには多くのリレーをクロールして大量のeventボリュームを処理する必要があり、モバイルデバイスでは実行不可能な作業です。今週の[マージ](https://github.com/nostr-protocol/nips/pull/2223)によりこれらのプロバイダーのクライアントディスカバリープロセスに関するガイダンスが追加されました。

**委任：**

ユーザーのWeb of Trustスコアを計算するには多くのリレーにまたがって複数ホップのフォローグラフをクロールする必要があり、正確なフォロワー数を計算するにはリレーネットワーク全体での重複排除が必要です。モバイルデバイスとブラウザクライアントはこれらの操作を実行できませんが、その結果はスパムフィルタリングとコンテンツランキングに不可欠です。NIP-85は、ユーザーが信頼できるプロバイダーを指定して計算を実行し、結果を標準Nostrイベントとして公開することを可能にすることでこのギャップを埋めます。

**プロトコル設計：**

NIP-85は異なるサブジェクトタイプに関するアサーションのための4つのevent kindを使用します。ユーザーアサーション（kind 30382）はフォロワー数、投稿・リプライ・リアクション数、zap量、正規化ランク（0-100）、共通トピック、アクティブ時間を持ちます：

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30382,
  "tags": [
    ["d", "e88a691e98d9987c964521dff60025f60700378a4879180dcbbb4a5027850411"],
    ["rank", "89"],
    ["followers", "4521"],
    ["first_created_at", "1609459200"],
    ["post_cnt", "1283"],
    ["reply_cnt", "647"],
    ["reactions_cnt", "8920"],
    ["zap_amt_recd", "850000"],
    ["zap_amt_sent", "320000"],
    ["zap_cnt_recd", "412"],
    ["zap_cnt_sent", "198"],
    ["zap_avg_amt_day_recd", "1150"],
    ["zap_avg_amt_day_sent", "430"],
    ["reports_cnt_recd", "2"],
    ["reports_cnt_sent", "0"],
    ["t", "nostr"],
    ["t", "bitcoin"],
    ["active_hours_start", "14"],
    ["active_hours_end", "22"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

イベントアサーション（kind 30383）はコメント数、引用数、リポスト数、リアクション数、zapデータで個々のノートを評価します：

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30383,
  "tags": [
    ["d", "<target event id>"],
    ["rank", "72"],
    ["comment_cnt", "45"],
    ["quote_cnt", "12"],
    ["repost_cnt", "89"],
    ["reaction_cnt", "310"],
    ["zap_cnt", "23"],
    ["zap_amount", "125000"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

アドレス指定可能なイベント（長文記事、wikiページ）については、kind 30384がすべてのバージョンにわたって同じエンゲージメントメトリクスを適用します。Kind 30385は`i`と`k`タグでNostrイベントが外部コンテンツを参照する方法を標準化する[NIP-73（外部コンテンツID）](/ja/topics/nip-73/)を通じて参照される外部識別子（書籍、映画、ウェブサイト、場所、ハッシュタグ）を評価します：

```json
{
  "id": "<event hash>",
  "pubkey": "<service pubkey>",
  "created_at": 1739836800,
  "kind": 30385,
  "tags": [
    ["d", "isbn:9780765382030"],
    ["k", "isbn"],
    ["rank", "94"],
    ["comment_cnt", "67"],
    ["reaction_cnt", "203"]
  ],
  "content": "",
  "sig": "<service key signature>"
}
```

各アサーションは`d`タグにサブジェクト（pubkey、event ID、eventアドレス、またはNIP-73識別子）を含む置換可能なアドレス指定可能イベントです。サービスプロバイダーはこれらのイベントに独自のキーで署名し、クライアントは信頼関係に基づいて評価します。

**プロバイダーディスカバリー：**

ユーザーはkind 10040イベントを公開することで信頼するアサーションプロバイダーを宣言します。各エントリーはプロバイダーpubkeyとリレーヒント、オプションのアルゴリズムバリアントとともにアサーションタイプを指定します：

```json
{
  "id": "<event hash>",
  "pubkey": "<user pubkey>",
  "created_at": 1739836800,
  "kind": 10040,
  "tags": [
    ["30382:rank", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30382:rank", "3d842afe...", "wss://nostr.wine"],
    ["30382:zap_amt_sent", "4fd5e210...", "wss://nip85.nostr.band"],
    ["30383:rank", "4fd5e210...", "wss://nip85.nostr.band"]
  ],
  "content": "",
  "sig": "<user signature>"
}
```

ユーザーはプロバイダー設定を非公開にするため、[NIP-44](/ja/topics/nip-44/)を使用して`.content`のタグリストを暗号化できます。クライアントはフォローしたアカウントが信頼するプロバイダーを確認することでプロバイダーリストを構築し、アサーションプロバイダー自体の分散型レピュテーションレイヤーを作ります。

**セキュリティモデル：**

プロバイダーは異なるアルゴリズムには異なるサービスキーを使用しなければならず、アルゴリズムがユーザーごとにパーソナライズされる場合はユーザーごとにユニークなキーが必要で、ユーザー間のクエリのクロス相関を防ぎます。各サービスキーにはアルゴリズムの動作を説明するkind 0メタデータイベントがあり、ユーザーが何を信頼しているかを透明にします。アサーションイベントは基礎となるデータが実際に変化した場合にのみ更新されるべきで、不必要なリレートラフィックを防ぎ、クライアントが結果を自信を持ってキャッシュできるようにします。

**現在の採用状況：**

NIP-85は非公式にすでに生まれつつあったパターンを正式化しています。PrimalのキャッシュサーバーがエンゲージメントメトリクスとWeb of Trustスコアを計算しています。[ニュースレター#9](/ja/newsletters/2026-02-11-newsletter/#antiprimalprimalキャッシュへの規格準拠ゲートウェイ)で取り上げた[Antiprimal](https://gitlab.com/soapbox-pub/antiprimal)がNIP-85のevent kindを使用してこれらの計算を標準Nostrクライアントに橋渡ししています。[Nostr.band](https://nostr.band)は仕様の例で参照されている`wss://nip85.nostr.band`リレーを運営し、検索インデックスデータのアサーションイベントを提供しています。クライアント側では、[Amethyst](https://github.com/vitorpamplona/amethyst)（このNIPを書いたvitorpamplonaが開発）がアサーションイベントとサービスプロバイダー宣言を解析する`quartz`ライブラリで実験的なTrusted Assertionsサポートを持っています。[Vertex](https://vertexlab.io)は同様のWeb of Trustメトリクスを計算していますが、ディスカバリー問題とアサーションベースのアーキテクチャの計算オーバーヘッドを理由に、NIP-85イベントの代わりに直接APIを使用する[異なるアプローチを選択しました](https://vertexlab.io/blog/dvms_vs_nip_85/)。NIP-85があれば、クライアントは標準のeventフォーマットを通じて任意のプロバイダーからアサーションを消費でき、プロバイダーは精度で競争し、ユーザーが誰を信頼するかを選択します。

## NIPディープダイブ：NIP-52（カレンダーイベント）

[NIP-52](https://github.com/nostr-protocol/nips/blob/master/52.md)はNostr上のカレンダーイベントを定義し、クライアントが特定の瞬間または瞬間の間の出来事を標準的な方法で表現・発見できます。今週の[Dタグマージ](https://github.com/nostr-protocol/nips/pull/1752)により日単位インデックスが追加され、仕様のクエリインフラの欠落していたピースが完成しました。

**2つのeventタイプ：**

NIP-52は時間精度に基づいてカレンダーイベントを2つのkindに分けます。日付ベースイベント（kind 31922）は祝日や複数日フェスティバルのような終日の出来事を表します。`start`とオプションの`end`タグにISO 8601日付文字列を使用し、タイムゾーンは考慮しません：

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1735689600,
  "kind": 31922,
  "content": "Annual celebration of Bitcoin's genesis block",
  "tags": [
    ["d", "bitcoin-independence-day-2026"],
    ["title", "Bitcoin Independence Day"],
    ["start", "2026-01-03"],
    ["end", "2026-01-04"],
    ["location", "Worldwide"],
    ["g", "u4pruydqqv"],
    ["t", "bitcoin"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["r", "https://bitcoinindependenceday.com"]
  ],
  "sig": "<event creator signature>"
}
```

時間ベースイベント（kind 31923）は`start`とオプションの`end`タグにUnixタイムスタンプを持つ特定の瞬間を表し、表示用のIANAタイムゾーン識別子（`start_tzid`、`end_tzid`）も持ちます。両kindはパラメータ化された置換可能イベントで、主催者は同じ`d`タグで新しいイベントを公開することで詳細を更新できます。

**カレンダーとRSVP：**

Kind 31924イベントはコレクションとしてカレンダーを定義し、kind 31922またはkind 31923イベントをそのアドレス座標で指す`a`タグでイベントを参照します：

```json
{
  "id": "<event hash>",
  "pubkey": "<calendar owner pubkey>",
  "created_at": 1739836800,
  "kind": 31924,
  "content": "Nostr community events worldwide",
  "tags": [
    ["d", "nostr-community-calendar"],
    ["title", "Nostr Community Events"],
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["a", "31922:<organizer-pubkey>:bitcoin-independence-day-2026"]
  ],
  "sig": "<calendar owner signature>"
}
```

ユーザーは複数のカレンダー（個人、仕事、コミュニティ）を維持でき、クライアントは特定のpubkeyからカレンダーを購読できます。カレンダーイベントはカレンダーを参照する`a`タグを含めることで参加リクエストを送れ、複数のユーザーが所有していないカレンダーにイベントを追加する協力的なカレンダー管理を可能にします。

RSVPはkind 31925を使用し、ユーザーがオプションの空き・ビジーインジケーターとともに出席ステータスを公開します：

```json
{
  "id": "<event hash>",
  "pubkey": "<attendee pubkey>",
  "created_at": 1739836800,
  "kind": 31925,
  "content": "Looking forward to it",
  "tags": [
    ["a", "31923:<organizer-pubkey>:nostr-meetup-2026", "wss://relay.example.com"],
    ["e", "<kind 31923 event id>", "wss://relay.example.com"],
    ["d", "<unique-rsvp-id>"],
    ["status", "accepted"],
    ["fb", "busy"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com"]
  ],
  "sig": "<attendee signature>"
}
```

有効な`status`値は「accepted」「declined」「tentative」で、オプションの`fb`タグでその期間のユーザーの空き・ビジー状態を示します。RSVPイベントはカレンダーイベントの`a`タグを参照し、主催者の`p`タグを持つため、主催者のクライアントがリレーをまたいでレスポンスを集約できます。

**Dタグの追加：**

今週のマージ以前は、日付範囲でイベントをクエリするクライアントがpubkeyまたはカレンダーからすべてのイベントを取得してクライアントサイドでフィルタリングする必要がありました。時間ベースイベント（kind 31923）の新しい必須`D`タグには`floor(unix_seconds / 86400)`として計算された日単位Unixタイムスタンプが含まれます。複数日イベントには1日1つの複数の`D`タグが付きます。リレーがこれで日単位でイベントをインデックス化し、フィルタリングされたクエリに効率的に応答できるようになり、クライアントサイドのフィルタリング問題がリレーサイドのインデックスルックアップに変わります。

```json
{
  "id": "<event hash>",
  "pubkey": "<event creator pubkey>",
  "created_at": 1739836800,
  "kind": 31923,
  "content": "Monthly meetup for Nostr developers in Austin",
  "tags": [
    ["d", "nostr-meetup-2026"],
    ["title", "Nostr Developer Meetup"],
    ["summary", "Talks and demos from local Nostr builders"],
    ["image", "https://example.com/meetup-banner.jpg"],
    ["start", "1740067200"],
    ["end", "1740078000"],
    ["start_tzid", "America/New_York"],
    ["end_tzid", "America/New_York"],
    ["D", "20139"],
    ["location", "Bitcoin Commons, Austin TX"],
    ["g", "9v6knb2pg"],
    ["p", "<organizer-pubkey>", "wss://relay.example.com", "host"],
    ["p", "<speaker-pubkey>", "wss://relay.example.com", "speaker"],
    ["t", "nostr"],
    ["t", "meetup"],
    ["r", "https://bitcoincommons.com"]
  ],
  "sig": "<event creator signature>"
}
```

`D`値の`20139`は`floor(1740067200 / 86400)`に等しく、このイベントを2025年2月20日に配置します。「今週のすべてのイベント」をクエリするクライアントは対応する`D`範囲でフィルターを送信し、リレーは一致するイベントのみを返します。

**設計上の決定：**

NIP-52は繰り返しイベントを意図的に省略しています。仕様は繰り返しルール（iCalendarからのRRULE）を完全に除外し、その複雑さをクライアントに委ねています。主催者は各出来事ごとに個別のイベントを公開し、リレーサイドのデータモデルをシンプルに保ちます。参加者タグはオプションのロール（「host」「speaker」「attendee」）を持ち、locationタグは人間が読めるアドレスと並んで空間クエリ用のジオハッシュ`g`タグを含めることができます。

**実装：**

[Flockstr](https://github.com/zmeyer44/flockstr)はNIP-52上に構築された主要なカレンダークライアントです。[Coracle](https://gitea.coracle.social/coracle/coracle)がソーシャルフィードでカレンダーイベントを表示します。今週の`D`タグ追加により、両クライアントが特定の日付範囲でイベントをクエリする際の帯域幅削減に活用できるリレーサイドの時間インデックスが可能になります。

---

今週は以上です。構築中のプロジェクトや共有したいニュースがあれば、<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">NIP-17 DMでお問い合わせください</a>。Nostrでもお待ちしています。
