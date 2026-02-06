---
title: 'Nostr Compass #7'
date: 2026-01-28
translationOf: /en/newsletters/2026-01-28-newsletter.md
translationDate: 2026-01-28
draft: false
type: newsletters
---

Nostr Compassへようこそ。Nostrの週刊ガイドです。

**今週の内容:** Ridestrが[Cashu](/ja/topics/cashu/)決済と暗号化された位置情報共有を使って、分散型ライドシェアリングをNostrにもたらします。Pomadeがマルチシグ署名者向けのメールベースリカバリーを導入。Damusが信頼性の高いDM同期のために[negentropy](/ja/topics/negentropy/)を実装。Amethystのデスクトップアプリに検索、ブックマーク、zapを追加。Amber v4.1.1がリレー信頼スコアを表示。MarmotがMIP-03をマージし、TypeScriptリファレンスチャットアプリを構築。diVineが[NIP-46](/ja/topics/nip-46/) QR認証とメンション対応を追加。新しいNIP提案がコミュニティ管理、シーケンスベースの同期、暗号化ファイルストレージに対応。また、2021年の少数の初期採用者から2023年のDamusのApp Store爆発的ローンチ、2025年の成熟したクライアントエコシステムまで、プロトコルの進化をたどる5年間のNostr1月の歴史を振り返ります。

## ニュース

### RidestrがNostrに分散型ライドシェアリングをもたらす

[Ridestr](https://github.com/variablefate/ridestr)は、Nostr上に完全に構築されたピアツーピアのライドシェアアプリケーションを開発しており、BitcoinおよびCashu決済による直接的なドライバー・ライダー間取引を可能にします。このプロトコルはカスタムイベントkind（30173、3173-3175、30180/30181）を使用してライドを調整しながら、段階的な位置情報開示と[NIP-44](/ja/topics/nip-44/)暗号化によってプライバシーを維持します。

システムは慎重に設計されたフローで動作します：ドライバーはkind 30173イベントを介してgeohashエンコードされた位置情報（約5km精度）で空き状況をブロードキャストし、ライダーはkind 3173を通じて運賃見積もりとともにライドをリクエストし、ライドが始まる前にHTLCエスクロートークンを使用して支払いが確保されます。位置情報のプライバシーは段階的開示によって保護され、ピックアップの詳細はドライバーが到着したときにのみ公開され、目的地はPIN確認後に共有されます。当事者間のすべての通信は[NIP-44](/ja/topics/nip-44/)暗号化を使用してプライバシーを確保します。

RidestrはP2PK署名を使用したHTLCエスクローによって支払いセキュリティを実装しています。ライダーがドライバーのオファーを受け入れると、ライド完了後にドライバーのみが請求できる支払いハッシュで[Cashu](/ja/topics/cashu/)トークンをロックします。このプロトコルは現在シングルミントアーキテクチャで動作しており、ライダーとドライバーが同じ[Cashu](/ja/topics/cashu/)ミントを使用する必要があります。プロジェクトのKotlinベースのAndroid実装は、NUT-07状態チェックを通じてプルーフ検証と古いプルーフの回復を処理します。

Ridestrは、ほとんどのNostrアプリケーションが避けている課題に取り組んでいます：リアルタイムの位置情報調整、紛争解決を伴う支払いエスクロー、および物理世界でのやり取りのための評価システム。このプロジェクトはベータ版であり、Nostrのイベントモデルがコンテンツ共有だけでなく、ピアツーピアのサービスマーケットプレイスもサポートできることを実証しています。

### Pomadeがマルチシグ署名者向けアルファリカバリーシステムを開始

hodlbodが開発した[Pomade](https://github.com/coracle-social/pomade)は、既存の[FROSTR](https://github.com/FROSTR-ORG)エコシステムを基盤として、リカバリーに焦点を当てた閾値署名サービスを提供します。@frostr/bifrostライブラリを介して[FROST](/ja/topics/frost/)（Flexible Round-Optimized Schnorr Threshold）署名を使用し、Pomadeは閾値暗号の上にメールベースのリカバリーフローを追加します。システムはShamir Secret Sharingを使用してユーザーの秘密鍵をシャーディングし、設定可能な閾値（2-of-3、3-of-5など）で複数の独立した署名者にシェアを分散します。

プロトコルは[NIP-44](/ja/topics/nip-44/)暗号化ペイロードを持つ単一のイベントkind（28350）を使用して、完全にNostr上で動作します。署名時、クライアントは少なくとも`threshold`数の署名者から部分署名を要求し、それらを有効なSchnorr署名に集約します。暗号化では、署名者はECDHを介して共有シークレットを導出するために協力し、どの単一当事者も完全な鍵を知ることはありません。

リカバリーは2つの認証方法で動作します：パスワードベース（署名者のpubkeyをソルトとして使用したargon2id）またはメールOTP。OTPリカバリー中のMITM攻撃を防ぐために、各署名者はクライアント提供のプレフィックスを持つ独自の検証コードを生成し、ユーザーは各署名者と独立して認証する必要があります。プロトコルはスパム防止のために登録イベントにプルーフオブワーク（[NIP-13](/ja/topics/nip-13/)ごとに20ビット以上）を要求します。

信頼モデルは明示的です：`threshold`数の署名者が共謀すれば、鍵を盗むことができます。メールプロバイダーはOTPを傍受できるため、完全に信頼されています。ユーザーは完全な秘密鍵を独立して回復することはできません。そのためには`threshold`数の署名者の協力が必要です。プロトコルは鍵管理に不慣れな新規ユーザーのオンボーディング用に設計されており、慣れたらセルフカストディに移行することが明示的に推奨されています。Pomadeは未監査のアルファ状態であることから、「鍵の紛失、盗難、サービス拒否、またはメタデータ漏洩」の可能性について警告しています。

## リリース

### Damusが信頼性の高いDM同期のためにNegentropyを実装

[Damus v1.13](https://github.com/damus-io/damus/tree/v1.13)は、[先週オープンPRとしてプレビューした](/ja/newsletters/2026-01-21-newsletter/#damus-ios-client---open-prs)negentropy実装を出荷しました。[PR #3536](https://github.com/damus-io/damus/pull/3536)はネットワーキングレイヤーに基本的な[negentropy](/ja/topics/negentropy/)サポートを追加し、プロトコルをサポートするリレーとの集合調整を可能にします。コンパニオン[PR #3547](https://github.com/damus-io/damus/pull/3547)は、標準的なREQサブスクリプションが失敗したときにnegentropyを使用して欠落メッセージを回復するプルトゥリフレッシュDM同期を追加します。

実装は保守的なアプローチに従います：通常のDM読み込みは変更されず、ユーザーが手動でリフレッシュしたときにリカバリーメカニズムとして[negentropy](/ja/topics/negentropy/)が利用可能になります。自動テストは、標準クエリでは見逃される古いタイムスタンプを持つDMを生成し、[negentropy](/ja/topics/negentropy/)同期を使用して正常に取得することで修正を実証します。[negentropy](/ja/topics/negentropy/)サポートには互換性のあるリレーが必要ですが、実装は利用可能な場所でプロトコルを使用することで、混合リレー環境を適切に処理します。

### Amber v4.1.1 - リレー信頼スコア

[Amber v4.1.1](https://github.com/greenart7c3/Amber/releases/tag/v4.1.1)はリレー信頼スコア表示を出荷し（[PR #289](https://github.com/greenart7c3/Amber/pull/289)）、[先週のTrusted Relay Assertions NIPカバレッジ](/ja/newsletters/2026-01-21-newsletter/#nip-updates)で議論されたリレー評価コンセプトを実装しています。信頼スコアはRelaysページとNostrConnect接続リクエストに表示され、接続を承認する前にユーザーがリレーの信頼性を評価するのに役立ちます。このリリースには、再設計されたログイン/イベント/権限UIと`switch_relays`メソッドのサポートも含まれています。パフォーマンス改善により、古いデバイスで報告された20秒以上の読み込み時間に対処するキーストア操作のキャッシュが行われました。

### nak v0.18.2 - MCP統合

fiatjafの[nak](https://github.com/fiatjaf/nak)（Nostr Army Knife）[v0.18.2](https://github.com/fiatjaf/nak/releases/tag/v0.18.2)は`nak mcp`を介して[Model Context Protocol](https://nostrify.dev/mcp)サポートを追加し、AIエージェントがNostr上で人を検索し、ノートを公開し、ユーザーにメンションし、outboxモデルを使用してコンテンツを読むことを可能にします。このリリースでは、事前にビルドされたバイナリをダウンロードする[ワンラインインストーラー](https://github.com/fiatjaf/nak/blob/master/install.sh)（`curl -sSL https://raw.githubusercontent.com/fiatjaf/nak/master/install.sh | sh`）も導入され、エンドユーザーにとってGoツールチェーンの要件がなくなりました。BunkerモードはUnixソケットと`switch_relays`をサポートするようになりました。

### Zeus v0.12.2 Beta - NWC修正

[Zeus v0.12.2-beta1](https://github.com/ZeusLN/zeus/releases)は、[先週のZeusカバレッジ](/ja/newsletters/2026-01-21-newsletter/#zeus-lightning-wallet-with-nostr-wallet-connect)で取り上げた問題に対処する複数のNWC修正を出荷しました。

## プロジェクトアップデート

### Amethystデスクトップ - フェーズ2A出荷

[Amethyst](https://github.com/vitorpamplona/amethyst)は[デスクトップアプリのフェーズ2A](https://github.com/vitorpamplona/amethyst/pull/1676)を展開し、デスクトップ体験に検索、ブックマーク、Zap、スレッドビュー、長文コンテンツ（Reads）を追加しました。コンパニオン[PR #1683](https://github.com/vitorpamplona/amethyst/pull/1683)は透過的なイベントブロードキャストフィードバックを追加し、ユーザーはイベントがネットワーク全体に伝播する際にリアルタイムでリレーごとのステータスを確認でき、接続性の問題を診断しやすくなりました。

### Notedeckの進捗：カレンダーアプリとUXポリッシュ

Damusチームの[Notedeck](https://github.com/damus-io/notedeck)デスクトップクライアントは、モバイルビューでより多くの画面スペースを確保するためにスクロール速度に応答する自動非表示ツールバー動作をマージしました（[PR #1268](https://github.com/damus-io/notedeck/pull/1268)）。[ドラフトPR #1271](https://github.com/damus-io/notedeck/pull/1271)は、月/週/日/アジェンダビュー、RSVPサポート、カレンダーイベントへの[NIP-22](/ja/topics/nip-22/)コメントを備えた完全な[NIP-52](/ja/topics/nip-52/)カレンダーアプリを追加し、現在テスト用にフィーチャーフラグが設定されています。

### Jumbleがコミュニティモードを追加

リレーに焦点を当てたWebクライアント[Jumble](https://github.com/CodyTseng/jumble)は、[コミュニティモード](https://github.com/CodyTseng/jumble/pull/738)と[環境変数によるリレーセットプリセット](https://github.com/CodyTseng/jumble/pull/736)のサポートを追加し、[nostr.moe](https://nostr.moe/)のようなテーマ付きインスタンスのデプロイを容易にしました。

### Shopstr注文ダッシュボード

[Shopstr](https://github.com/shopstr-eng/shopstr)は、チャットベースの注文管理を専用の[注文ダッシュボード](https://github.com/shopstr-eng/shopstr/pull/219)に置き換えました。新しいインターフェースは、マーチャントがチャットスレッドをスクロールすることなく、注文ステータスの追跡、メッセージの既読マーク、フルフィルメントの管理を行うための集中ビューを提供します。このアップデートでは、サーバーサイドの注文ステータスAPIを優先してIndexedDBキャッシュを廃止し、より良いフィルタリングのために注文DMのタグ付け方法を改訂しました。

### FormstrがグリッドQuestionを追加

Nostrネイティブのフォームアプリ[Formstr](https://github.com/abh3po/nostr-forms)は、[グリッドQuestion](https://github.com/abh3po/nostr-forms/pull/419)を追加し、埋め込みサポート付きで[SDKを書き直しました](https://github.com/abh3po/nostr-forms/pull/410)。[非NIP-07署名者向けの修正](https://github.com/abh3po/nostr-forms/pull/418)により、bunkerまたはローカル署名者を持つユーザーが自分のIDでフォームを送信しようとする際の問題が解決されました。

### nostr-toolsが暗号依存関係をアップグレード

コアJavaScriptライブラリの[nostr-tools](https://github.com/nbd-wtf/nostr-tools)は[@noble/curves v2.0.1にアップグレード](https://github.com/nbd-wtf/nostr-tools/pull/520)し、27ファイルにわたる破壊的なAPI変更に対処し、最新の監査済みnobleライブラリを採用しました。fiatjafはまた[NIP-46](/ja/topics/nip-46/)に`switch_relays`サポートを追加し、bunkerクライアントがリレー接続を動的に変更できるようにしました。

### ZeusがNIP-87ミントレビューに取り組み中

[Zeus](https://github.com/ZeusLN/zeus)には[[NIP-87](/ja/topics/nip-87/)ミントレビュー用のオープンPR](https://github.com/ZeusLN/zeus/pull/3576)があり、ユーザーはNostrフォローでフィルタリングされた[Cashu](/ja/topics/cashu/)ミントを発見してレビューできます。レビューには星評価が含まれ、匿名またはユーザーのnsecで送信できます。

### Camelusが完全なDMサポートを出荷

バッテリー効率の良いモバイルパフォーマンスのためにDart NDKで構築されたFlutterベースのAndroidクライアント[Camelus](https://github.com/camelus-hq/camelus)は、今週20以上のコミットで包括的なダイレクトメッセージングを追加しました。このアップデートには、チャットカテゴリ、メッセージ日付、楽観的送信UI、自分へのメモ機能、適切なDMリレー処理が含まれます。

### Marmot Protocolアップデート

[先週オープンPRとしてカバーした](/ja/newsletters/2026-01-21-newsletter/#marmot-protocol-white-noise-encrypted-group-chat-library)MIP-03決定論的コミット解決がマージされました。[MDK PR #152](https://github.com/marmot-protocol/mdk/pull/152)は、同じエポックに対して複数の有効なコミットが到着したときに、すべての[MLS](/ja/topics/mls/)ベースのグループチャットが同じ状態に収束することを保証します。

コンパニオン[仕様PR #28](https://github.com/marmot-protocol/marmot/pull/28)は、実装監査からのギャップに対処するinit_keyライフサイクル要件を追加します：Welcomeメッセージからの秘密鍵マテリアルは処理後に安全に削除する必要があり（ゼロ化、ストレージクリーンアップ）、新しいメンバーはforward secrecyのために24時間以内にセルフアップデートを実行する必要があります。

TypeScript SDK（[marmot-ts](https://github.com/marmot-protocol/marmot-ts)）はリファレンスチャットアプリケーションを構築しています。[PR #37](https://github.com/marmot-protocol/marmot-ts/pull/37)は、グループ作成/リスト、公開/ブロードキャスト/削除フローを備えたキーパッケージ管理、QRコード招待を追加します。hzrd149による[オープンPR #38](https://github.com/marmot-protocol/marmot-ts/pull/38)は、ページネーション付きのメッセージ履歴永続化を実装します。whitenoise-rsバックエンドは今週15のPRをマージし、多言語サポート（[PR #455](https://github.com/marmot-protocol/whitenoise-rs/pull/455)）とMIP-04 v2メディアリファレンス（[PR #450](https://github.com/marmot-protocol/whitenoise-rs/pull/450)）を含みます。

### diVineがNostr統合機能を追加

ショートフォームビデオアプリ[diVine](https://github.com/divinevideo/divine-mobile)は、急速なNostr統合を継続しています。

オープンPRには[NIP-46](/ja/topics/nip-46/) QRコード認証（[PR #1019](https://github.com/divinevideo/divine-mobile/pull/1019)）と[NIP-17](/ja/topics/nip-17/)暗号化ダイレクトメッセージング（[PR #834](https://github.com/divinevideo/divine-mobile/pull/834)）が含まれます。今週の活動は、`nostr:` URIと@メンションをクリック可能なプロファイルリンクに変換する[メンションサポート](https://github.com/divinevideo/divine-mobile/pull/1098)、Nostrプロファイルを使用した[Classic Vinersアバターフォールバック](https://github.com/divinevideo/divine-mobile/pull/1097)、[描画](https://github.com/divinevideo/divine-mobile/pull/1056)、[フィルター](https://github.com/divinevideo/divine-mobile/pull/1053)、[ステッカー](https://github.com/divinevideo/divine-mobile/pull/1050)を含むビデオ編集ツールに焦点を当てました。

## NIPアップデート

[NIPsリポジトリ](https://github.com/nostr-protocol/nips)への最近の変更：

**マージ済み：**

- **[Trusted Relay Assertions](https://github.com/nostr-protocol/nips/pull/1534)** - [先週カバーした](/ja/newsletters/2026-01-21-newsletter/#nip-updates)リレー信頼スコアリングを標準化する提案がマージされました。仕様は、信頼性、品質、アクセシビリティにわたるスコアリングを持つリレー信頼アサーション用のkind 30385イベントを定義します。マージに至る議論は、信頼スコアが「グローバル」（すべてのユーザーに対して一度計算される）であるべきか「パーソナライズ」（各観察者のソーシャルグラフに相対的）であるべきかに集中しました。[nostr.bandのTrust Rank](https://trust.nostr.band/)や[GrapeRank](https://github.com/Pretty-Good-Freedom-Tech/graperank-nodejs)のようなPageRankスタイルのアルゴリズムは、偽アカウントを通じて渡されるランクをボットファームのサイズで割ることでシビル攻撃に抵抗します。

**オープンPRとディスカッション：**

- **Communikeys** - リレーベースのアプローチの代わりに、既存のnpubをコミュニティ識別子として使用するコミュニティ管理のための[包括的な提案](https://nostrhub.io)。任意のnpubがkind 10222イベントを公開することでコミュニティになることができ、出版物はkind 30222イベントを介してコミュニティをターゲットにします。アクセス制御は[NIP-58](/ja/topics/nip-58/)バッジを使用し、コミュニティキーのコールドストレージによる委任されたメンバーシップ管理を可能にします。

- **[NIP-CF: Changes Feed](https://github.com/nostr-protocol/nips/pull/2196)** - タイムスタンプベースの`since`フィルターの代替として、シーケンスベースのイベント同期を提案するドラフト。問題：`since`タイムスタンプを使用した標準的なNostr同期は、複数のイベントが同じ秒精度のタイムスタンプを共有する場合、クライアントとリレーのクロックがずれる場合、またはチェックポイントが不正確な場合にイベントを見逃す可能性があります。NIP-CFは、リレーが保存されたイベントに単調増加するシーケンス番号を割り当てることでこれを解決し、厳密な全順序を提供します。クライアントは特定のシーケンス番号以降の変更をリクエストし、保証された順序でイベントを受信し、イベントを見逃さない正確なチェックポイントを提供します。この提案は、初期同期後にサブスクリプションがリアルタイム更新のためにオープンのままになるライブ/継続モードもサポートします。

- **[NIP-XX: Encrypted File Sync](https://github.com/nostr-protocol/nips/pull/1947)** - Nostrリレーを使用してデバイス間で暗号化コンテンツを同期するためのkind 30800（暗号化ファイル）、30801（ボールトインデックス）、30802（共有ドキュメント）を定義するプロトコル。このプロトコルにより、ローカルファーストのノートテイキングアプリは、集中サーバーなしでエンドツーエンド暗号化同期を提供できます。ファイルの内容、パス、名前、フォルダ構造はすべて[NIP-44](/ja/topics/nip-44/)セルフ暗号化を使用して暗号化されるため、リレーは読み取れないブロブを保存します。画像のようなバイナリ添付ファイルは、クライアントサイド暗号化を使用して[Blossom](/ja/topics/blossom/)サーバーを使用します。Kind 30802は、受信者の公開鍵に暗号化することで、ユーザー間のドキュメント共有を可能にします。

## Nostrの5年間の1月の歴史

[先月のニュースレター](/ja/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)では、fiatjafの最初のクライアントリリースからJack Dorseyの触媒的な寄付まで、Nostrの12月のマイルストーンをたどりました。この回顧録では、検証された技術開発に焦点を当て、2021年から2025年までの各1月に何が起こったかを記録します。

### 2021年1月：初期開発

Nostrの3か月目は、2020年12月にローンチしたfiatjafのVue.jsクライアントBranleの継続的な開発を見ました。おそらく15人未満の少数の初期採用者グループが、Telegramグループ[@nostr_protocol](https://t.me/nostr_protocol)（2020年11月16日作成）を通じて調整し、1つまたは2つの実験的なリレーでプロトコルをテストしていました。コマンドラインクライアントnosclはターミナルベースのインタラクションを提供しました。

技術的な基盤はすでにロックされていました：ユーザーはsecp256k1公開鍵で識別され、投稿はSchnorr署名で暗号的に署名され、リレーは互いに通信しないダムストレージとして機能します。これは意図的にBitcoinネイティブな暗号であり、後年の採用パターンを形成する設計選択でした。

### 2022年1月：開発者の発見

2022年1月は、Nostrが[最初のHacker News登場](https://news.ycombinator.com/item?id=29749061)（2021年12月31日）の余韻の中で始まり、110ポイントと138コメントを獲得しました。その投稿の時点で、ネットワーク全体を動かしていたリレーはわずか約7つで、コメント者は「nostrはとても新しく、誰も使っていないので、スパムはまだ問題ではない」と指摘していました。Robert C. Martin（「Uncle Bob」）はNostrを「ソーシャルコミュニケーションのエンドゲームソリューション」になる可能性があると支持しました。議論は1月も続き、開発者たちはリレーアーキテクチャ対真のP2P、検閲耐性対モデレーション、シンプルさがスケールするかどうかについて議論しました。

HNの投稿は新しい実装の波を引き起こしました。Uncle Bob自身は1月18日に[more-speech](https://github.com/unclebob/more-speech)というClojureデスクトップクライアントを開始しました。fiatjafの[go-nostr](https://github.com/nbd-wtf/go-nostr)ライブラリ（2021年1月作成）と[noscl](https://github.com/fiatjaf/noscl)コマンドラインクライアントがGoツールを提供し、[nostr-tools](https://github.com/nbd-wtf/nostr-tools)がJavaScriptサポートを提供しました。2022年12月までに、約800のプロファイルがバイオを持っていました。Branleは主要なWebクライアントとして残り、秘密鍵のインポートとマルチリレーサポートを含む更新を受けました。技術的な課題は明らかでした：64文字の16進数キーは直感的ではなく、メッセージの遅延がユーザーを苛立たせ、コミュニティはアーキテクチャがTwitter規模のトラフィックを処理できるかどうかを疑問視しました。

### 2023年1月：ブレイクアウト

2023年1月はNostrを実験から運動へと変貌させました。William Casarin（jb55）によるiOSクライアントDamusは、AppleのApp Store承認プロセスと戦いました。1月1日に拒否され、1月26日に再度拒否され、[1月31日についに承認されました](https://www.coindesk.com/tech/2023/02/01/decentralized-social-media-project-nostrs-damus-gets-listed-on-apple-app-store)。その承認は連鎖反応を引き起こしました：Damusはすぐに米国のソーシャルネットワーキングで#10に達しました。Jack Dorseyはそれを「オープンプロトコルのマイルストーン」と[呼びました](https://web.archive.org/web/20240304043638/https://www.theblock.co/post/207448/nostr-based-decentralized-twitter-alternative-damus-goes-live-on-apple-app-store)。

その8日前の1月23日、[Edward SnowdenがNostr上での存在を発表しました](https://x.com/Snowden/status/1617623779626352640)：「Nostrのクールなことの一つは...検閲耐性を超えて、280文字に制限されないことです。」NSA内部告発者からの彼の支持はプライバシー意識の高いサークルで重みを持ち、ユーザーはすぐにLightningを通じて彼にsatsをzapし始めました。

Webクライアントは流入をオンボードするために競争しました。2022年12月にkieranが作成した[Snort](https://github.com/v0l/snort)は、機能豊富なReactクライアントとして登場しました。1月13日、SnortはNostr Plebs APIを介したNIP-05登録を統合し、新規ユーザーがオンボーディング中に人間が読めるIDを主張できるようにしました。Martti Malmi（Satoshiから2番目のBitcoinトランザクションを受け取った初期のBitcoin貢献者）がフルタイムで開発した[Iris](https://iris.to)は、iris.toで無料のNIP-05 IDを持つWebとモバイルの両方のインターフェースを提供しました。monlovesmangoがBranleフォークとしてQuasar（Vue.js）で構築した[Astral](https://github.com/monlovesmango/astral)は、ユーザーが投稿とフィルタリングのためにリレーをセットに整理できるリレーグルーピング機能を備えたリレー管理に焦点を当てました。iOSクライアントのTestFlightベータは数時間以内に満杯になり、AmethystがAndroidを席巻しました。

インフラストラクチャはペースについていくのに苦労しました。すべてのリレーは自腹で支払う愛好家によって運営されていました。Lightningマイクロペイメントを使用した有料リレーは自然なスパムフィルタリングを作成しましたが、アクセスの摩擦を導入しました。[Damusは承認からわずか2日後に中国のApp Storeから削除されました](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/)。報道によると、中国のトップインターネット監視機関の要請によるものでした。

### 2024年1月：プロトコルの強化

2024年1月はプロトコルの標準化とコミュニティ構築に焦点を当てました。[Nostr PHX](https://www.nostrphx.com/events)は1月5日にフェニックスでミートアップを開催し、地元のサイファーパンクを集めました。これはその年の多くのコミュニティイベントの最初であり、BTC Prague（6月）、リガでのNostriga（8月）、Nostrasiaが含まれます。

最も重要なプロトコル開発は、1月29日にマージされた[NIP-59（Gift Wrap）](https://github.com/nostr-protocol/nips/pull/716)で、暗号化通信のためのメタデータ保護を提供しました。Gift Wrapは[NIP-44の暗号化標準](https://github.com/paulmillr/nip44)（2023年12月に[Cure53によって監査](https://cure53.de/audit-report_nip44-implementations.pdf)）を基に、リレーから送信者のIDを隠します。プロトコルは暗号化されたメッセージをランダムな使い捨てキーペアで署名された外部イベント内にラップします。リレーは使い捨てのpubkeyのみを見て、実際の送信者のIDは受信者のみが復号化できる暗号化ペイロードに埋め込まれています。これにより、リレーオペレーターやネットワーク観察者が誰が誰にメッセージを送っているかを知ることを防ぎます。タイミング分析を無効にするためにタイムスタンプもランダム化できます。

エコシステムはソーシャルメディアを超えて拡大しました。[Plebeian Market](https://plebeian.market)は[NIP-15](/ja/topics/nip-15/)準拠で完全にNostrネイティブになり、クロススタールショッピングカートとマーチャントを発見するためのスタールブラウザを可能にしました。[Shopstr](https://github.com/shopstr-eng/shopstr)はBitcoinコマースを促進するパーミッションレスマーケットプレイスとして登場しました。kieranが構築した[Zap.stream](https://zap.stream/)は、21 sats/分のLightning支払いでNostrにライブストリーミングをもたらしました。開発者ツールは[NDK](https://github.com/nostr-dev-kit/ndk)がTypeScript抽象化を提供し、[rust-nostr](https://github.com/rust-nostr/nostr)がRustバインディングを提供することで成熟しました。[Zeus v0.8.1](https://blog.zeusln.com/new-release-zeus-v0-8-1/)はNostrコンタクトインポートと永続的なLNDを出荷し、後のリリースでのNostr Wallet Connect統合の基礎を築きました。

しかし、インフラストラクチャの持続可能性は[依然として課題でした](https://arxiv.org/abs/2402.05709)。この時期の学術研究では、リレーの95%が運営コストをカバーするのに苦労しており、20%が大幅なダウンタイムを経験していることがわかりました。有料リレーの入場料は平均1,000 sats（約$0.45）未満で、運営を維持するには不十分でした。

*詐欺に関する注意：この時期にローンチされた「Nostr Assets Protocol」および関連する「$NOSTR」トークンは、[fiatjafによって公に非難され](https://www.aicoin.com/en/article/377704)、「100%詐欺」であり「実際のNostrプロトコルとは何の関係もないアフィニティ詐欺」とされました。*

### 2025年1月：クライアントの成熟

2025年1月は、エコシステム全体で継続的なクライアント開発を見ました。[Nostur 1.17.0](https://www.nobsbitcoin.com/nostur-v1-17-0/)は1月13日に既読状態のクロスデバイス同期、[FROST](/ja/topics/frost/)マルチシグログインサポート、最適化されたローカルデータベースパフォーマンスを出荷しました。Amethystは手動設定を必要とせずにフォローリストに基づいてリレーセットを自動的にコンパイルするoutboxモデルへの移行を続けました。

主要なクライアントはダイレクトメッセージで[NIP-04](/ja/topics/nip-04/)から離れ始め、[NIP-17](/ja/topics/nip-17/)と提案された[NIP-104](/ja/topics/nip-104/)に向けて移行し、暗号化とメタデータ保護を強化しました。エコシステムがより効率的なリレー使用パターンに収束するにつれて、Gossipモデル（outbox/inbox通信）が採用されました。業界の観察者は、これがNostrがニッチなプロトコルから主流の認知へと移行する年になると予測し、毎日のアクティビティを倍増させる可能性のある注目を集めるプラットフォーム移行があるかもしれないと予測しました。

### 2026年1月：セキュリティと署名インフラストラクチャ

2026年1月はセキュリティと署名インフラストラクチャの大幅な進歩をもたらしました。[Primal Android 2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18)は[NIP-46](/ja/topics/nip-46/)リモート署名と[NIP-55](/ja/topics/nip-55/)ローカル署名者サポートを出荷し、AmberとAegisに加わって他のAndroidアプリの完全な署名ハブになりました。[BitchatはSignalとNIP-44を監査した同じ会社であるCure53のセキュリティ監査を完了しました](https://github.com/permissionlesstech/bitchat/pulls)。DHシークレットのクリアリングとスレッドセーフの問題を含む重要な発見を修正する17以上のPRがありました。BitchatとDamusの両方がC TorからRust Artiに移行し、信頼性とメモリセーフティを向上させました。

プロトコル作業は[NIP-71](https://github.com/nostr-protocol/nips/pull/1669)（アドレス可能なビデオイベント）のマージと、量子攻撃に対するNostrの将来の保護についてのディスカッションを開くポスト量子暗号NIPで継続しました。Trusted Relay Assertionsドラフトは、署名されたアテステーションを通じてリレー信頼スコアリングを標準化することを提案しました。[Marmot Protocol](https://github.com/marmot-protocol/mdk)は、監査の発見に対処する18のマージされたPRで[MLS](/ja/topics/mls/)ベースの暗号化メッセージングを強化しました。

実世界のアプリケーションは、[Cashu](/ja/topics/cashu/)エスクローと[NIP-44](/ja/topics/nip-44/)暗号化を使用した分散型ライドシェアリングを開発する[Ridestr](https://github.com/variablefate/ridestr)と、[FROST](/ja/topics/frost/)閾値署名にメールベースのリカバリーフローを追加する[Pomade](https://github.com/coracle-social/pomade)で拡大しました。Damusは信頼性の高いDM同期のために[negentropy](/ja/topics/negentropy/)を出荷し、Amethystのデスクトップアプリは検索、ブックマーク、zapでフェーズ2Aに達しました。

### 今後の展望

6年間の1月は、Nostrの初期開発（2021年）から公開発見（2022年）、爆発的成長（2023年）、プロトコル強化（2024年）、クライアント成熟（2025年）、セキュリティインフラストラクチャ（2026年）への進化を明らかにしています。このパターンはオープンプロトコルの成長を見てきた人には馴染み深いものです：静かな構築の年月、条件が揃ったときの突然の爆発、そしてすべてを信頼できるものにするための長い作業。7つのリレーとHacker Newsのスレッドから始まったものは、今や実際のアプリケーションを持つ監査済みインフラストラクチャになっています。2027年の問題：誰かがNostrを使ってライドを呼び、暗号化メッセージを送り、紛失した鍵を回復するとき、彼らはそれを使っていることに気づくでしょうか？

---

今週は以上です。何か構築していますか？共有したいニュースはありますか？プロジェクトの報道を希望しますか？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">NIP-17 DMでお問い合わせください</a>、またはNostrで見つけてください。
