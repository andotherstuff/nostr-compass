---
title: 'Nostr Compass #1'
date: 2025-12-17
publishDate: 2025-12-15
draft: false
type: newsletters
---

Nostr Compassへようこそ。Nostrプロトコルエコシステムに特化した週刊ニュースレターです。私たちの使命は、開発者、リレー運営者、ビルダーの皆さんにネットワーク全体の重要な動向をお伝えすることです。NIP提案からクライアントリリース、実装のベストプラクティスまで、技術的な正確さ、中立性、深さをもってプロトコルの進化を記録していきます。

Nostr Compassは[Bitcoin Optech](https://bitcoinops.org/)に触発されています。彼らの長年にわたるBitcoin技術知識の発展への献身的な取り組みは、プロトコルに焦点を当てたニュースレターの基準を確立しました。その模範に感謝し、同じ厳密さをNostrエコシステムにもたらすことを目指しています。

この創刊号では、週刊フォーマットを確立します。毎週水曜日にNIPの更新、リリースノート、開発ハイライト、技術ガイダンスをお届けします。クライアントを構築している方、リレーを運営している方、プロトコルに貢献している方、どなたにとってもNostr Compassはエコシステム全体で何が起きているかを知るための信頼できる情報源となることを目指しています。

## Nostrとは？

*これが創刊号のため、Nostrの仕組みについての入門から始めます。常連の読者は[ニュースと更新情報](#news--updates)に進んでください。*

Nostr（Notes and Other Stuff Transmitted by Relays）は、ソーシャルネットワーキングとメッセージングのための分散型プロトコルです。従来のプラットフォームとは異なり、Nostrには中央サーバーがなく、それを管理する会社もなく、単一障害点もありません。ユーザーは暗号鍵ペアを通じて自分のアイデンティティを所有し、コンテンツは誰でも運営できる独立したリレーサーバーを通じて流れます。

**仕組み:** ユーザーは鍵ペア（nsecと呼ばれる秘密鍵とnpubと呼ばれる公開鍵）を生成します。秘密鍵は「イベント」と呼ばれるメッセージに署名し、公開鍵はあなたのアイデンティティとして機能します。イベントはリレーに送信され、リレーはそれを保存して他のユーザーに転送します。鍵を自分で管理するため、アイデンティティやフォロワーを失うことなくクライアントやリレーを切り替えることができます。

**なぜ重要か:** Nostrはリレーの多様性による検閲耐性（1つのリレーがあなたを禁止しても、他のリレーがコンテンツを提供できる）、ポータビリティ（あなたのアイデンティティはどのNostrアプリでも機能する）、相互運用性（すべてのNostrクライアントは同じプロトコルを話す）を提供します。何を見るかを決めるアルゴリズムも、広告も、データ収集もありません。

**今日のエコシステム:** Nostrはマイクロブログ（Twitter/Xのような）、長文コンテンツ（Mediumのような）、ダイレクトメッセージ、マーケットプレイス、ライブストリーミングなどをサポートしています。クライアントにはDamus（iOS）、Amethyst（Android）、Primal、Coracleなど数十のものがあります。Lightning Networkの統合により「zaps」を通じた即時決済が可能です。プロトコルは機能を拡張するコミュニティ主導の仕様であるNIPs（Nostr Implementation Possibilities）を通じて進化し続けています。

## ニュース {#news}

**NIP-BEがマージ: Bluetooth Low Energyサポート** - 重要な新機能が[プロトコルに追加されました](https://github.com/nostr-protocol/nips/pull/1979)。[NIP-BE](/ja/topics/nip-be/)はNostrアプリケーションがBluetooth Low Energyを介してどのように通信・同期できるかを規定しています。これにより、オフライン対応アプリがインターネット接続なしで近くのデバイス間でデータを同期できるようになります。仕様はWebSocketリレーパターンをBLEの制約に適応させ、DEFLATEの圧縮とチャンクメッセージングを使用してBLEの小さなMTUサイズ（20-256バイト）を処理します。デバイスはUUID比較に基づいて役割を交渉し、より高いUUIDを持つ方がGATTサーバーになります。

**MIP-05: プライバシー保護プッシュ通知** - [Marmot Protocol](/ja/topics/marmot/)は[MIP-05](/ja/topics/mip-05/)（[仕様](https://github.com/marmot-protocol/mips/blob/main/mip-05.md)）を公開しました。これはプライバシーを維持するプッシュ通知の仕様です。従来のプッシュシステムはサーバーがデバイストークンとユーザーアイデンティティを知る必要がありましたが、MIP-05はECDH+HKDFとChaCha20-Poly1305でデバイストークンを暗号化し、一時的な鍵を使用して相関を防ぐことでこれを解決します。3イベントのゴシッププロトコル（kind 447-449）が暗号化されたトークンをグループメンバー間で同期し、通知は[NIP-59](/ja/topics/nip-59/)のgift wrappingとデコイトークンを使用してグループサイズを隠します。これにより、WhiteNoiseや他のMarmotクライアントがユーザープライバシーを損なうことなくタイムリーな通知を配信できます。

**Blossom BUD-10: 新しいURIスキーム** - [Blossom](/ja/topics/blossom/)メディアプロトコルは[BUD-10](/ja/topics/bud-10/)（[仕様](https://github.com/hzrd149/blossom/blob/master/buds/10.md)）を通じてカスタムURIスキームを取得します。新しい`blossom:<sha256>.ext`フォーマットは、ファイルハッシュ、拡張子、サイズ、複数のサーバーヒント、[BUD-03](/ja/topics/bud-03/)サーバー発見のための作成者pubkeyを埋め込みます。これにより、blobリンクがサーバー間の自動フォールバックを可能にすることで、静的HTTP URLよりも耐障害性が高くなります。

**Shopstrマーケットプレイスの更新** - Nostrネイティブマーケットプレイスは決済用に[Nostr Wallet Connectを実装し](https://github.com/shopstr-eng/shopstr/pull/202)（[NIP-47](/ja/topics/nip-47/)）、[NIP-40](/ja/topics/nip-40/)を使用した[リスティングの有効期限を追加し](https://github.com/shopstr-eng/shopstr/pull/203)、売り手向けの[割引コード](https://github.com/shopstr-eng/shopstr/pull/210)を導入しました。

## NIP更新 {#nip-updates}

[NIPsリポジトリ](https://github.com/nostr-protocol/nips)への最近の変更:

**新しいNIP:**
- **[NIP-BE](/ja/topics/nip-be/)** - Bluetooth Low Energyメッセージングとデバイス同期 ([#1979](https://github.com/nostr-protocol/nips/pull/1979))
- **[NIP-63](/ja/topics/nip-63/)** - プロトコル内でゲートコンテンツを処理するためのペイウォール/プレミアムコンテンツ標準 ([#2156](https://github.com/nostr-protocol/nips/pull/2156))

**重要な変更:**
- **[NIP-24](/ja/topics/nip-24/)** - Kind 0ユーザーメタデータにオプションの`languages`配列を追加。IETF BCP 47タグを使用して複数の優先言語を指定でき、コンテンツ発見とリレーマッチングが改善されます ([#2159](https://github.com/nostr-protocol/nips/pull/2159))
- **[NIP-69](/ja/topics/nip-69/)** - `expires_at`と`expiration`タグによるP2P取引の注文有効期限サポートを追加 ([#2118](https://github.com/nostr-protocol/nips/pull/2118))
- **[NIP-59](/ja/topics/nip-59/)** - Gift wrapイベントがNIP-09/NIP-62リクエストで削除可能に ([#2131](https://github.com/nostr-protocol/nips/pull/2131))
- **[NIP-51](/ja/topics/nip-51/)** - 汎用ブックマークからハッシュタグとURLタグを削除。ハッシュタグはkind 30015を使用 ([#2133](https://github.com/nostr-protocol/nips/pull/2133))
- **[NIP-18](/ja/topics/nip-18/)** - `a`タグサポートによる置換可能イベントの汎用リポストを改善 ([#2132](https://github.com/nostr-protocol/nips/pull/2132))
- **[NIP-17](/ja/topics/nip-17/)** - 文言を洗練し、DMへのkind 7リアクションサポートを追加 ([#2098](https://github.com/nostr-protocol/nips/pull/2098))
- **[NIP-11](/ja/topics/nip-11/)** - リレー公開鍵識別のための`self`フィールドを追加 ([#1764](https://github.com/nostr-protocol/nips/pull/1764))

## NIP詳細解説: NIP-01とNIP-19 {#nip-deep-dive-nip-01-and-nip-19}

この創刊号では、すべてのNostr開発者が理解すべき2つの基礎的なNIPを取り上げます。トピックページで[NIP-01](/ja/topics/nip-01/)と[NIP-19](/ja/topics/nip-19/)をご覧ください。

### NIP-01: 基本プロトコル

[NIP-01](/ja/topics/nip-01/)はコアプロトコルを定義します。Nostrのすべてはこの仕様の上に構築されています。

**イベント**は唯一のオブジェクト型です。各イベントには以下が含まれます:
- `id`: シリアライズされたイベントのSHA256ハッシュ（イベントの一意識別子）
- `pubkey`: 作成者の公開鍵（32バイトhex、secp256k1）
- `created_at`: Unixタイムスタンプ
- `kind`: イベントタイプを分類する整数
- `tags`: メタデータ用の配列の配列
- `content`: ペイロード（解釈はkindに依存）
- `sig`: pubkeyがこのイベントを作成したことを証明するSchnorr署名

**Kind**はリレーがイベントを保存する方法を決定します:
- 通常イベント (1, 2, 4-44, 1000-9999): 通常どおり保存され、すべてのバージョンが保持
- 置換可能イベント (0, 3, 10000-19999): pubkeyごとに最新のもののみ保持
- 一時的イベント (20000-29999): 保存されず、購読者に転送のみ
- アドレス指定可能イベント (30000-39999): pubkey + kind + `d`タグの組み合わせごとに最新のものを保持

Kind 0はユーザーメタデータ（プロフィール）、kind 1はテキストノート（基本的な投稿）、kind 3はフォローリストです。

**Kind 1: テキストノート**はソーシャルNostrの心臓部です。kind 1イベントはツイートに似た短文投稿です。`content`フィールドにはメッセージテキスト（プレーンテキスト、ただしクライアントはしばしばmarkdownをレンダリング）が含まれます。タグにより返信、メンション、参照が可能になります:

```json
{
  "id": "<32-byte-hex>",
  "pubkey": "<32-byte-hex>",
  "created_at": 1734480000,
  "kind": 1,
  "content": "Hello Nostr! Check out @jb55's work on Damus.",
  "tags": [
    ["e", "<replied-to-event-id>", "wss://relay.example.com", "reply"],
    ["p", "<jb55-pubkey>"]
  ],
  "sig": "<64-byte-hex>"
}
```

「reply」マーカー付きの`e`タグは、これが返信であることを示します（スレッディング規約については[NIP-10](/ja/topics/nip-10/)を参照）。`p`タグはユーザーをメンションし、クライアントがそのユーザーに通知し、生のpubkeyの代わりに名前をレンダリングできるようにします。クライアントはメンションされたユーザーのkind 0イベントを取得して、表示名と画像を取得します。

タイムラインを構築するために、クライアントはフォローしているpubkeyからのkind 1イベントを購読します: `["REQ", "feed", {"kinds": [1], "authors": ["<pubkey1>", "<pubkey2>", ...], "limit": 50}]`。リレーはマッチするノートを返し、クライアントはそれらを時系列でレンダリングします。

**アドレス指定可能イベント** (30000-39999)は置換可能イベントのように機能しますが、追加の識別子として`d`タグを使用します。リレーはpubkey + kind + dタグの組み合わせごとに最新バージョンのみを保持します。これにより、編集可能な記事、商品リスト、またはユーザーごとに複数の置換可能なアイテムが必要な場合に対応できます。

**タグ**は最初の要素がタグ名である配列です。標準的な1文字タグ（`e`、`p`、`a`、`d`、`t`）はリレーによってインデックス化され、効率的なクエリが可能です。例えば、`["e", "<event-id>"]`は別のイベントを参照し、`["p", "<pubkey>"]`はユーザーを参照します。

**クライアント-リレー通信**はWebSocket接続を使用し、JSONの配列をメッセージとして使用します。最初の要素がメッセージタイプを識別します。

クライアントからリレーへ:
- `["EVENT", <event>]` - リレーにイベントを公開
- `["REQ", <sub-id>, <filter>, ...]` - フィルターにマッチするイベントを購読
- `["CLOSE", <sub-id>]` - 購読を終了

リレーからクライアントへ:
- `["EVENT", <sub-id>, <event>]` - 購読にマッチするイベントを配信
- `["EOSE", <sub-id>]` - 「保存されたイベントの終わり」 - リレーはすべての履歴マッチを送信し、今後は新しいイベントが到着したときのみ送信
- `["OK", <event-id>, <true|false>, <message>]` - イベントが受け入れられたか拒否されたか（および理由）を確認
- `["NOTICE", <message>]` - リレーからの人間が読めるメッセージ

購読フロー: クライアントは購読IDとフィルターを含む`REQ`を送信し、リレーはマッチする`EVENT`メッセージで応答し、履歴に追いついたことを示す`EOSE`を送信します。`EOSE`の後、新しい`EVENT`メッセージはリアルタイムです。クライアントは完了したら`CLOSE`を送信します。

**フィルター**は取得するイベントを指定します。フィルターオブジェクトには以下を含めることができます: `ids`（イベントID）、`authors`（pubkey）、`kinds`（イベントタイプ）、`#e`/`#p`/`#t`（タグ値）、`since`/`until`（タイムスタンプ）、`limit`（最大結果数）。1つのフィルター内のすべての条件はANDロジックを使用します。`REQ`に複数のフィルターを含めることができ、それらはORロジックで結合されます - 1つの購読で異なるイベントタイプを取得するのに便利です。

### NIP-19: Bech32エンコード識別子

[NIP-19](/ja/topics/nip-19/)は、Nostrのどこでも見かける人間に優しいフォーマットを定義します: npub、nsec、noteなど。これらはプロトコル自体では使用されません（プロトコルはhexを使用）が、共有と表示には不可欠です。

**なぜbech32か？** 生のhex鍵はコピー時にエラーが発生しやすく、視覚的に区別しにくいです。Bech32エンコーディングは人間が読めるプレフィックスとチェックサムを追加します。`npub`（公開鍵）を`nsec`（秘密鍵）や`note`（イベントID）とすぐに区別できます。

**基本フォーマット**は生の32バイト値をエンコードします:
- `npub` - 公開鍵（あなたのアイデンティティ、共有しても安全）
- `nsec` - 秘密鍵（秘密に保つ、署名に使用）
- `note` - イベントID（特定のイベントを参照）

例: hexのpubkey `3bf0c63fcb93463407af97a5e5ee64fa883d107ef9e558472c4eb9aaaefa459d`は`npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6`になります。

**共有可能識別子**はTLV（Type-Length-Value）エンコーディングを使用してメタデータを含みます:
- `nprofile` - リレーヒント付きプロフィール（クライアントがユーザーを見つけるのに役立つ）
- `nevent` - リレーヒント、作成者pubkey、kindを含むイベント
- `naddr` - アドレス指定可能イベント参照（pubkey + kind + dタグ + リレー）

これらは重要な問題を解決します: 誰かがノートIDを共有したとき、どのリレーがそれを持っているかをどうやって知るのでしょうか？`nevent`はイベントIDと推奨リレーをバンドルし、共有をより信頼性の高いものにします。

**重要:** プロトコル自体ではbech32フォーマットを使用しないでください。イベント、リレーメッセージ、NIP-05レスポンスはhexを使用する必要があります。Bech32は純粋に人間用インターフェースのためのものです: 表示、コピー/ペースト、QRコード、URL。

## リリース {#releases}

**Amber v4.0.4** - Android署名アプリはNullPointerExceptionを修正し、アクティビティ画面のパフォーマンスを改善し、一部のイベントkindの翻訳を追加しました。以前のv4.0.3リリースでは、刷新された暗号化/復号化UI、アカウントのエクスポート/インポート、アカウントごとのリレー処理、bunkerのpingサポート、クラッシュレポートが追加されました。[リリース](https://github.com/greenart7c3/Amber/releases/tag/v4.0.4)

**Coracle 0.6.28** - WebクライアントのバグFixリリース。トピックフィード、imgproxyが無効な場合の画像処理、非リンクハイライトソースのリンク化を修正しました。[リリース](https://github.com/coracle-social/coracle/releases/tag/0.6.28)

**Flotilla v1.6.2** - Discordライクなコミュニティクライアントはモーダルのスクロールとスタイルの問題を修正。このサイクルの以前のリリースでは、通知用のオプションのバッジとサウンド、改善されたリンクレンダリング、招待リンク用のQRコードスキャン、合理化されたウォレットセットアップが追加されました。[リリース](https://github.com/coracle-social/flotilla/releases/tag/1.6.2)

**nak v0.17.2** - コマンドラインNostrツールはNIPリファレンスをすばやく検索するための新しい`nip`コマンドを追加し、gitリポジトリ処理とstdinイベント処理の修正も行いました。[リリース](https://github.com/fiatjaf/nak/releases/tag/v0.17.2)

**White Noise v0.2.1** - MLSベースの暗号化メッセージングアプリのメジャーリリース。Blossomを介した画像共有、バックグラウンド同期、プッシュ通知、8言語のローカライズ、グループメンバー管理を追加。[リリース](https://github.com/marmot-protocol/whitenoise/releases/tag/v0.2.1%2B14)

**Amethyst v1.04.2** - フォローリスト/パック、新しいタイムラインフィルター、画像ギャラリー、H.265動画圧縮（50%小さいファイル）を導入した機能リリース。Kotlin Multiplatformマイグレーションを完了。[リリース](https://github.com/vitorpamplona/amethyst/releases/tag/v1.04.2)

**Mostro v0.15.5** - NIP-69注文有効期限サポートと改善された取引履歴レスポンスを含むP2P取引プラットフォームの更新。[リリース](https://github.com/MostroP2P/mostro/releases/tag/v0.15.5)

**Nosflare v8.9.26** - Cloudflareインフラストラクチャ上に構築されたサーバーレスNostrリレー。このリリースはwebsocketの障害を引き起こす可能性のあるバグに対処する重要なホットフィックスを提供し、リレーに依存するユーザーとアプリケーションにより安定した接続を保証します。[リリース](https://github.com/Spl0itable/nosflare/releases/tag/v8.9.26)

**Noscall v0.4.1** - Nostrベースの安全な音声およびビデオ通話アプリ。このリリースはMeページのポップアップUIを改善し、いくつかの既知の問題を修正して、安定性と通話の信頼性が向上しました。[リリース](https://github.com/sanah9/noscall/releases/tag/v0.4.1-release)

**Gitplaza v0.25.0** - Git関連のアクティビティに焦点を当てたデスクトップNostrクライアント。このリリースは受信箱フィードに高度なkindフィルターを導入し、フィルターに通常のzapsを含め、タブテキストのフォーマットを簡素化しました。パフォーマンスの改善により、コメントツリーの読み込みが最適化され、不要なデータベースクエリが削減され、より高速な表示のためにキャッシュされたコメントブランチを使用します。[リリース](https://codeberg.org/dluvian/gitplaza/releases/tag/v0.25.0)

## 注目のコードとドキュメントの変更 {#notable-code-and-documentation-changes}

### Damus (iOS) {#damus-ios}

クラッシュとUIの修正に焦点を当てた安定性の改善: 作成ビューの[カーソルジャンプ修正](https://github.com/damus-io/damus/pull/3377)、トランザクションの安全性のためにSwiftの`~Copyable`型を使用した[NostrDBインターフェースの再設計](https://github.com/damus-io/damus/pull/3366)、アクションバーの再インスタンス化を修正する[スレッドUIの安定性](https://github.com/damus-io/damus/pull/3341)、AttributeGraphサイクルによる[ミュートリストのフリーズ](https://github.com/damus-io/damus/pull/3346)、クロススレッドトランザクションクリーンアップによる[プロフィールクラッシュ](https://github.com/damus-io/damus/pull/3334)。またAIコーディングエージェント用の[AGENTS.md](https://github.com/damus-io/damus/pull/3293)ガイドラインも追加。

### Notedeck (デスクトップ/モバイル) {#notedeck}

[セキュアキーストレージ](https://github.com/damus-io/notedeck/pull/1191)はnsecを自動マイグレーションでOSセキュアストアに移動。[将来のノートフィルタリング](https://github.com/damus-io/notedeck/pull/1201)は24時間以上先の日付のイベントを非表示にします（アンチスパム）。[neventコピー](https://github.com/damus-io/notedeck/pull/1183)にリレーヒントを含めるようになりました。また: [プロフィールカラムのクイック追加](https://github.com/damus-io/notedeck/pull/1212)、[キーボードナビゲーション](https://github.com/damus-io/notedeck/pull/1208)、[メディア読み込みの最適化](https://github.com/damus-io/notedeck/pull/1210)。

### Amethyst (Android) {#amethyst-android}

[[NIP-46](/ja/topics/nip-46/)リモート署名](https://github.com/vitorpamplona/amethyst/pull/1555)のNostr Connectサポート。[ブックマーク整理](https://github.com/vitorpamplona/amethyst/pull/1586)で公開/非公開リスト管理。リレー情報解析のエッジケースに対する[strfry互換性](https://github.com/vitorpamplona/amethyst/pull/1596)修正。

### Primal (Android) {#primal-android}

`nostrconnect://` URL用の[Nostr Connectディープリンク](https://github.com/PrimalHQ/primal-android-app/pull/788)。bunker接続用のQRスキャンによる[リモートログイン](https://github.com/PrimalHQ/primal-android-app/pull/787)。[接続競合状態の修正](https://github.com/PrimalHQ/primal-android-app/pull/783)。

### White Noise (暗号化メッセージング) {#white-noise-encrypted-messaging}

[アプリデータ保持の修正](https://github.com/marmot-protocol/whitenoise/pull/890)はプライバシーのためにAndroid自動バックアップを無効化。[チャットスクロール動作](https://github.com/marmot-protocol/whitenoise/pull/861)は履歴を読むときに位置を保持。

### Zeus (Lightningウォレット) {#zeus-lightning-wallet}

バッチzapスループット改善のための[[NIP-47](/ja/topics/nip-47/)並列支払い](https://github.com/ZeusLN/zeus/pull/3407)。

## 開発者ベストプラクティス

**認証イベントを防御的に検証する** - go-nostrはリレータグが欠落している場合のNIP-42検証での[パニックを修正](https://github.com/nbd-wtf/go-nostr/pull/182)しました。整形式のイベントを期待する認証フローでも、アクセスする前に必須タグをチェックしてください。

**認証状態によるレート制限** - khatruは[NIP-42ベースのレート制限](https://github.com/fiatjaf/khatru/pull/57)を追加し、認証済みと匿名の接続に異なる制限を適用できるようにしました。一律の制限ではなく、認証状態に基づく階層的な制限を検討してください。

**リストにはカーソルページネーションを使用** - Blossomは`/list`エンドポイントで[日付ベースのページネーションをカーソルベースのページネーションに置き換え](https://github.com/hzrd149/blossom/pull/65)ました。日付ベースのページネーションはアイテムがタイムスタンプを共有すると壊れます。カーソルは信頼性の高い反復を提供します。

**イベントタイプのスキーマ検証** - [nostrability/schemata](https://github.com/nostrability/schemata)プロジェクトはNIP準拠のイベントを検証するためのJSONスキーマを提供します。開発中にスキーマ検証を統合して、不正なイベントがリレーに到達する前に検出することを検討してください。

---

今週は以上です。何かを構築していますか？共有したいニュースがありますか？プロジェクトを取り上げてほしいですか？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">NIP-17 DMでお問い合わせください</a>。またはNostrで見つけてください。

