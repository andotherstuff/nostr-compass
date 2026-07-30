---
title: 'Nostr Compass #32'
date: 2026-07-22
translationOf: /en/newsletters/2026-07-22-newsletter.md
translationDate: 2026-07-30
draft: false
type: newsletters
---

Nostr Compass へようこそ。毎週お届けする Nostr のガイドです。

**今週:** [IndieSats](#indiesats-drops-its-publisher-role-and-relaunches-as-open-nostr-music-infrastructure) は鍵の管理、ホワイトリスト、必須の収益分配を廃止し、アーティストが自分の鍵で公開できるオープンな relay、プレイヤー、ディスカバリーレイヤーとして再出発しました。[Nostrord v2.3.0](#nostrord-v230-ships-group-moderation-mute-lists-and-onion-relays) は、5 件の [NIP-29 仕様 PR がマージされた](#protocol-work-and-nip-updates)のと同じ週に、グループモデレーション、ミュートリスト、onion relay を実装しました。[Zapstore 1.1.0](#zapstore-110-makes-the-device-key-portable-and-adds-background-auto-updates) は、Amber でバックアップできるポータブルな暗号化デバイス鍵と、オプトインのバックグラウンド自動更新を導入しました。[お気に入りフォローセットのリスト kind](#the-favorite-follow-sets-list-kind-merges-and-immediately-moves-house) はマージされ、その数日後には番号変更の PR がオープンしました。また、[Iris プロジェクト群](#the-iris-projects-ship-a-pubsub-library-a-browser-fips-runtime-and-a-social-graph-20-in-one-week)は 1 週間で nostr-pubsub、ブラウザ向け fips-ts ランタイム、nostr-social-graph 2.0.0 をリリースしました。

タグ付きリリースでは、[Amber v6.3.0](#amber-v630-groups-bunker-signing-approvals-and-adds-expert-list-support) が bunker 署名承認をグループ化し、[Armada v0.37.0](#armada-v0370-opens-buzz-workspaces-from-a-second-client) が Buzz ワークスペースに対応する 2 つ目のクライアントとなり、[Divine Mobile 1.0.17](#divine-mobile-1017-hardens-relay-security-and-dm-delivery) が NIP-17 の確実な配信と厳格な TLS 検証を追加し、[nak v0.20.2](#nak-v0202-adds-nip-34-pull-request-workflows) が NIP-34 pull request 用コマンドを導入しました。

未リリースの変更では、[Snort](#snort-rewrites-query-synchronization-around-eose-proven-coverage) が EOSE で証明されたキャッシュ範囲を記録し、[Shopstr](#shopstr-binds-payment-validation-to-signed-receipts-and-server-side-prices) が決済の完全性に関する 2 つの欠陥を解消し、[Mostr](#mostr-bridges-activitypub-private-chats-and-nostr-dms) が ActivityPub のプライベートチャットと Nostr DM を橋渡ししました。[nostream](#nostream-merges-eight-prs-without-cutting-a-release) は今週の Deep Dive で取り上げるアクセス制御スタックをマージし、[Amethyst](#amethyst-lands-v1130-pre-release-qa-on-napplet-isolation-and-concord-authority) は Desktop での完全な NIP-88 投票対応を含む 88 件の PR をマージしました。

NIPs リポジトリは今週 5 件の PR をマージしました。[NIP-29 クラスター](#protocol-work-and-nip-updates)と [kind:10011 お気に入りフォローセット](#the-favorite-follow-sets-list-kind-merges-and-immediately-moves-house)を含み、[NIP-47 の簡素化](#protocol-work-and-nip-updates)と[信頼済み relay アサーション](#protocol-work-and-nip-updates)についての議論が始まっています。Deep Dive では [NIP-42 と NIP-43、relay アクセス制御のペア](#nip-deep-dive-nip-42-and-nip-43)を取り上げます。

---

## 主要ストーリー

### IndieSats がパブリッシャーの役割を手放し、オープンな Nostr 音楽インフラとして再ローンチ

[IndieSats](https://zapstore.dev) は Nostr ベースの音楽プラットフォームで、今週まではパブリッシャーとしてアーティストの鍵を預かり、ホワイトリストを運用し、収益の 2% を必須で受け取っていました。[7 月 20 日に公開された方針転換の発表](https://njump.me/nevent1qqsr4awwnfndnnz77zanjxarw6nd0uld0ckayxp2navz0u9tzzwfweqpzamhxue69uhhyetvv9ujuurjd9kkzmpwdejhgtczyquwq70hxz22lzytw65rnnjewg0lj8a74khxa8h9j47q38pdnqy3kqcyqqqqqqgz8083u)で、プロジェクトはこれら 3 つの役割を同時に廃止しました。再出発したプラットフォームは、オープンな relay、プレイヤー、ディスカバリーレイヤーという 3 つのオープンインフラで構成され、アーティストは自分の Nostr プロフィールで音楽を公開します。トラックごとの 2% のプラットフォーム分配は任意ですが、公開時にはデフォルトで選択されており、アーティストはこれを解除して支払いの全額を受け取れます。また、プラットフォームは [NIP-09](/ja/topics/nip-09/) の kind:5 削除リクエストに従うため、アーティストは作品を削除できます。[7 月 21 日公開の v1.1.5 更新](https://zapstore.dev/apps/com.indiesats.app)では、トラック公開を Amethyst などの Nostr 音楽クライアントが想定する event 形式に変更し、relay への配信を明示的にしました。プロトコルがプラットフォームに置き換わると語られがちな分野で、これはプラットフォームが自らをプロトコルの構成要素へと分解した実例です。

### Nostrord v2.3.0 がグループモデレーション、ミュートリスト、onion relay を出荷

Android、iOS、web、デスクトップ向けのグループチャットクライアント [Nostrord](https://github.com/nostrord/nostrord) は、[v2.3.0](https://github.com/nostrord/nostrord/releases/tag/v2.3.0) を出荷しました。すべての UI で配線されたグループモデレーションアクション([PR #192](https://github.com/nostrord/nostrord/pull/192))、クロス relay 検出付きの同意ベースのグループ招待([PR #195](https://github.com/nostrord/nostrord/pull/195))、クロスプラットフォームの [NIP-51](/ja/topics/nip-51/) ミュートリスト([PR #188](https://github.com/nostrord/nostrord/pull/188))、そして Tor .onion relay サポートが含まれます。このリリースは、サブグループ、メッセージ固定、バナー、招待コードをカバーする 5 件の PR が基盤となる [NIP-29](/ja/topics/nip-29/) 仕様にマージされたのと同じ週に着地しました(詳細は今週の[プロトコルセクション](#protocol-work-and-nip-updates))。これにより Nostr 上のグループチャットは、より深い仕様とその大部分を実際に動かすクライアントの両方を得て、relay グループ上に構築する他のすべての人にとってフィードバックループが短縮されます。

### Zapstore 1.1.0 がデバイス鍵をポータブル化し、バックグラウンド自動更新を追加

[Zapstore](https://github.com/zapstore/zapstore) は Nostr ネイティブなアプリストアで、リリースは開発者の鍵で署名され、中央の運営者がその正当性を保証することはありません。3 月上旬以来ここで取り上げる最初のリリースとなる [バージョン 1.1.0](https://github.com/zapstore/zapstore/releases/tag/1.1.0) は、従来型アプリストアとの最大の 2 つの隔たりを埋めます。更新については、オプトインのバックグラウンドダウンロードが Wi-Fi 経由で動作し、サイレントまたは段階的にインストールするため、ストアを手動で開かなくてもアプリを最新に保てます。アイデンティティの継続性は、[Amber](https://github.com/greenart7c3/Amber) に Android の署名者インターフェースである [NIP-55](/ja/topics/nip-55/) を介してバックアップできるポータブルな暗号化デバイス鍵によって実現し、端末を移行してもデバイスアイデンティティを維持できます。バージョン 1.1.0 はさらに、アプリカタログをデバイス署名の kind:10067 event として relay 上へ移し、オーバーフローメニューに [NIP-56](/ja/topics/nip-56/) の検証済み報告機能を追加して、問題のあるアプリを他のクライアントも利用できる形で報告できるようにしました。また、インストール前にリリースへ添付された C1 proof を検証し、開発者が署名した内容とデバイスが実行する内容の結び付きを強化しています。

### お気に入りフォローセットのリスト kind がマージされ、即座に引っ越し

1 週間の中で仕様調整の物語が展開されました。[PR #2413](https://github.com/nostr-protocol/nips/pull/2413) は 7 月 15 日にマージされ、[NIP-51](/ja/topics/nip-51/)(リスト)の下でお気に入りフォローセットのための置き換え可能なリスト kind を標準化しました。クライアントが汎用リスト kind を濫用する代わりに、ユーザーの厳選したフォローアカウントのセットを公開できる専用 kind です。数日のうちに、割り当てられた kind:10011 がすでに他で使用されていることが判明し、フォローアップの [PR #2417](https://github.com/nostr-protocol/nips/pull/2417) がオープンしてリストを kind:10021 にリナンバリングしようとしています。マージされた kind に対してまだ何も出荷されていないため、リナンバリングするには今が安価なタイミングです。クライアントが kind:10011 event を公開し始めたら、衝突を解消するコストは高くなります。リスト消費機能を構築する開発者は、解決するまではマージされたテキストではなくリナンバリング PR を追跡すべきです。

### Iris プロジェクト群が 1 週間で pubsub ライブラリ、ブラウザ FIPS ランタイム、ソーシャルグラフ 2.0 をリリース

Iris 圏からの 3 つのリリースが同時に着地し、それらは相互に噛み合っています。[nostr-pubsub](https://github.com/mmalmi/nostr-pubsub) は Nostr event 向けのトランスポート中立な publish/subscribe ライブラリです。[v0.1.3 から v0.5.2 までの最初の追跡リリース](https://github.com/mmalmi/nostr-pubsub/releases)は、nostr-tools の SimplePool 上に構築されたブラウザ relay キャリア、無効な署名がサブスクライバーに到達しないようトランスポート境界でのイベント検証、そして上限付きの履歴クエリを提供します。[fips-ts](https://github.com/mmalmi/fips-ts) は、以前は Rust スタックとして利用可能だった Noise-over-secp256k1 ピアトランスポートである [FIPS](/ja/topics/fips/) を TypeScript ランタイムとしてブラウザにもたらします。リリース [0.0.24 から 0.0.30](https://github.com/mmalmi/fips-ts/releases) は WebRTC データチャネルキャリア、ピア発見のための Nostr ベースのシグナリング、最近のピアのキャッシュ、ブラウザストレージ向けの IndexedDB アダプターを追加し、このランタイムはリファレンスの Rust 実装とワイヤー互換です。3 つ目の [nostr-social-graph v2.0.0](https://github.com/mmalmi/nostr-social-graph/releases/tag/v2.0.0) はソーシャルグラフライブラリのメジャーバージョンで、Nostr アイデンティティグラフ向けの署名済みロースター操作、正規の 3 フィールド URI からブートストラップされるデバイス承認フロー、共有の Rust と TypeScript テストベクトルを備えた FIPS トランスポートアイデンティティファセットを提供します。つなぎとなる枠組みは [Iris Stack](https://stack.iris.to/) で、Blossom、Hashtree、暗号化メッセージングとともにこれらのライブラリを結びつけるプロジェクトの統合ラボです。全体として、web アプリは今や Nostr 経由でピアを発見し、暗号化された FIPS チャネルを開き、署名済みソーシャルグラフを維持でき、すべて TypeScript で実現できます。

---

## タグ付きリリース

### Amber v6.3.0 が bunker 署名承認をグループ化し、Expert List サポートを追加

[Amber](https://github.com/greenart7c3/Amber) は Android の [NIP-46](/ja/topics/nip-46/) リモート署名者です。[v6.3.0](https://github.com/greenart7c3/Amber/releases/tag/v6.3.0) は bunker 署名向けのグループ化された複数リクエスト承認を追加し、保留中の署名リクエストのバッチを一度に 1 プロンプトずつではなく、まとめてレビュー・承認できるようにしました。このリリースはまた、Expert List(kind 12022)と Expert Pack(kind 32022)event のサポート、画面上の機密コンテンツを隠すプライバシーモード、そしてプロフィールメタデータより先にアカウントの [NIP-65](/ja/topics/nip-65/) relay リストを取得する変更を追加し、署名者フローがユーザーの実際の relay セットから開始されるようにしました。これは 2026-07-08 号で取り上げた v6.2.x ラインに続くものです。

### Nostrord v2.2.0 のフォローアップ

[v2.3.0](#nostrord-v230-ships-group-moderation-mute-lists-and-onion-relays) が今週のニュースセクションをリードしているため、タグ付きリリースの枠ではリード記事が扱わない部分だけを記します。v2.3.0 は #31 で取り上げた v2.2.0 の DM コントロールに続くもので、このクライアントにとって 2 週連続のリリースとなりました。

### Armada v0.37.0 が Buzz ワークスペースを 2 つ目のクライアントから利用可能に

[Armada](https://gitlab.com/soapbox-pub/armada) は Discord 風の Nostr クライアントです。[v0.37.0](https://gitlab.com/soapbox-pub/armada/-/commit/7a0d0ade51fb8a7bafa4513d2881d275bb2c7dde) では、拡張 [NIP-29](/ja/topics/nip-29/) ワークスペースモードとして Buzz relay に対応し、その機能を relay の [NIP-11](/ja/topics/nip-11/) メタデータから検出します。クライアントは Buzz のフォーラム投稿とコメントを kind 45001 と 45003 として表示し、編集と削除をストリームのタイムラインへ反映するほか、プレゼンス、ワークフロー、ジョブ、ハドル、共有キャンバスの各画面を追加します。Projects ワークスペースは、[NIP-34](/ja/topics/nip-34/) のリポジトリ告知、patch、pull request、issue、ステータス event を relay から直接読み取ります（[実装 commit](https://gitlab.com/soapbox-pub/armada/-/commit/7d5603a3e21d564301d667113d28de4407d6f642)）。これにより、Buzz ワークスペースは会話とリポジトリ作業の両方に対応する 2 つ目のクライアントを得ました。

### Wisp v1.2.0 がマルチアカウントスイッチャーと折りたたみ可能な返信スレッドを追加

[Wisp](https://github.com/barrydeen/wisp) はウォレット機能を内蔵したプライバシー指向の Nostr クライアントです。[v1.2.0](https://github.com/barrydeen/wisp/releases/tag/v1.2.0) は再ログインなしでプロフィール間を移動できるマルチアカウントスイッチャー、長い会話向けの折りたたみ可能な返信スレッド、ノートリンクが開かれる前のトラッキングパラメータの除去、そしてウォレットの取引履歴ビューを追加します。このリリースは 2026-07-08 号で取り上げた Wisp の更新に続くものです。

### Divine Mobile 1.0.17 が relay の安全性と DM 配信を強化

Nostr の短編動画クライアント [Divine Mobile](https://github.com/divinevideo/divine-mobile) は、永続的なストップモーションエディターと Nostr 経路の強化を含む [1.0.17](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.17) をリリースしました。ダイレクトメッセージは relay の `OK` 応答を待ち、永続キューから再試行し、受信者の kind 10050 inbox relay リストを経由するようになりました（[PR #6046](https://github.com/divinevideo/divine-mobile/pull/6046)）。NIP-46 のペアリングでは、`auth_url` challenge を復旧可能な署名手順として保持します（[PR #6151](https://github.com/divinevideo/divine-mobile/pull/6151)）。[PR #6278](https://github.com/divinevideo/divine-mobile/pull/6278) は、本番環境の relay WebSocket と、NIP-96 upload、LNURL、zap に使う HTTP request から寛容な証明書受け入れを削除し、debug 用 loopback 接続以外ではプラットフォームの TLS 検証を復元しました。中断した upload はサーバーが最後に確認した offset から再開できるため、公開処理がバックグラウンドへ移っても最初からやり直す必要がありません。

### ClipRelay v0.1.2(新プロジェクト)が Nostr relay 経由でデバイス間のクリップボードを同期

[ClipRelay](https://github.com/tajava2006/cliprelay) は新たにローンチされたクロスプラットフォームアプリ(Android、macOS、Windows、Linux)で、自分のデバイス間でクリップボードを同期します。1 台のマシンでコピーし、別のマシンで貼り付けられます。すべてのトラフィックは自分宛の [NIP-44](/ja/topics/nip-44/) 暗号化 event として Nostr relay を経由するため、運用するサーバーも作成するアカウントもありません。秘密鍵はアプリの外に保たれます。[v0.1.2](https://github.com/tajava2006/cliprelay/releases) は、スリープから復帰したマシンが公開は続けるが受信を静かに停止するという微妙な同期失敗を修正し、以前は死んだサブスクリプションを正常と報告していた relay ステータスインジケーターを強化しました。ClipRelay がニュースレターに登場するのはこれが初めてです。

### Sonar v0.1-alpha.11 がアルファラインを継続

先週のリードストーリー [Sonar](https://github.com/hedwig-corp/bitchat-to-sonar) は、[v0.1-alpha.11](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.11) をカットしました。Rust メッシュリンクエンジン、BLE とメッシュの修正、relay 診断への取り組みが含まれ、#31 で取り上げたアルファラインへの増分的なフォローアップです。

### nak v0.20.2 が NIP-34 pull request のワークフローを追加

Nostr のコマンドラインツール [nak](https://github.com/fiatjaf/nak) は、[v0.20.2](https://github.com/fiatjaf/nak/releases/tag/v0.20.2) をリリースしました。[NIP-34](/ja/topics/nip-34/) の pull request を作成、取得、マージするコマンドと、個別の patch を取得するコマンドを追加し、リポジトリ告知を書き換えずに push することも可能です。[11 commit のリリース差分](https://github.com/fiatjaf/nak/compare/v0.20.1...v0.20.2)には、[NIP-29](/ja/topics/nip-29/) の親グループ処理、より多くの outbox relay への問い合わせ、relay 接続 timeout の設定機能、デフォルトの `--sec` 値しかない場合の bunker 選択修正も含まれます。

### 今週の小規模ローンチ

4 つの小規模リリースもそれぞれ紹介します。Nostr 通話アプリ [noscall v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release) は push notification を UnifiedPush へ移行し、通話シグナリングを Google の push インフラから切り離しました。Nostr をシグナリングに使う mesh VPN [nostr-vpn v4.1.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v4.1.3) は、プラットフォーム間で exit DNS policy を統一し、WireGuard または private exit の session 終了後に元の route と DNS 状態を復元するようになりました。4 月に取り上げた Nostr と Lightning の音楽・podcast aggregator [StableKraft v1.3.0](https://github.com/ChadFarrow/stablekraft-app/releases/tag/v1.3.0) は、Android の lock screen と headset のネイティブ操作、および再生中だけ有効になる wake lock を追加し、Doze 中も音声再生を継続できるようにしました。Zapstore の新アプリ Hakari は、体重記録を暗号化された Nostr event でバックアップします。

### Amethyst が napplet 分離と Concord 権限の v1.13.0 プレリリース QA を着地

[Amethyst](https://github.com/vitorpamplona/amethyst) は v1.13.0 のリリースに先立ち、今週 88 件の PR をマージしました。[PR #3650](https://github.com/vitorpamplona/amethyst/pull/3650) は、napplet のアカウント分離、Concord の権限修正、その他約 30 件の修正を含むリリース前 QA です。期間末の作業では、Desktop に [NIP-88](https://github.com/nostr-protocol/nips/blob/master/88.md) の投票表示、作成、投票、宣言された relay に基づく集計、kind 1068 検索をすべて追加しました（[PR #3664](https://github.com/vitorpamplona/amethyst/pull/3664)）。NIP-50 検索は BM25 の関連度で結果を順位付けし、大規模な tag watcher は上限付き merge を使うようになりました（[PR #3663](https://github.com/vitorpamplona/amethyst/pull/3663)）。別の relay store 改修では、測定した cost に基づいて query index を選び、tag-author-kind index を追加し、fanout ごとに live event を 1 回だけ serialize します（[PR #3660](https://github.com/vitorpamplona/amethyst/pull/3660)）。報告された benchmark では、ある query が 149 ms から 4 ms に、一般的な DM room query が 14.2 ms から 0.66 ms に短縮されました。

---

## 未リリースの変更

### Snort が EOSE で証明された範囲を軸に query 同期を書き換え

Web Nostr クライアント [Snort](https://github.com/v0l/snort) は、[commit 8a62770](https://github.com/v0l/snort/commit/8a627700d8a5af9527cb68655d844dd14a3ac79d) で query と cache 同期の経路を書き換えました。クライアントは、どの query window が EOSE に達したかを記録し、その watermark を使って既に網羅した cache 範囲を読み飛ばし、event dispatch を 1 つの relay pool listener に集約し、NIP-11 document で [NIP-50](/ja/topics/nip-50/) 対応を示す relay にだけ search filter を送ります。その後の修正では、同時に行われる watermark 更新を直列化し、timeline の包含境界を修正しました。[commit 9d1721b](https://github.com/v0l/snort/commit/9d1721b8b5696a6f96f462170c469c232cabe672) は、分割された follow feed への live subscription を復元し、ページ読込後に届いた event が cache window の外で止まらないようにしています。

### Shopstr が決済検証を署名済み receipt とサーバー側の価格に結び付け

Nostr marketplace クライアント [Shopstr](https://github.com/shopstr-eng/shopstr) は、決済の完全性に関する 2 つの欠陥を解消しました。[PR #552](https://github.com/shopstr-eng/shopstr/pull/552) では、Zapsnag が kind 9735 receipt を購入として扱う前に、その署名、署名者、埋め込まれた zap request、受取人と商品 tag、BOLT11 の金額、任意の preimage を invoice の payment hash と照合します。[PR #449](https://github.com/shopstr-eng/shopstr/pull/449) は Cashu quote の作成を Shopstr API route の背後へ移し、listing を解決して価格をサーバー側で再計算するため、ブラウザで変更された金額から mint invoice が決まることはありません。

### Mostr が ActivityPub のプライベートチャットと Nostr DM を橋渡し

ActivityPub と Nostr の bridge である [Mostr](https://gitlab.com/soapbox-pub/mostr) は、1 対 1 の Pleroma ChatMessage object と暗号化された Nostr DM を双方向に転送するようになりました（[commit 36ee547](https://gitlab.com/soapbox-pub/mostr/-/commit/36ee547035f9287029f71656c472fe029a7ab31b)）。ActivityPub のプライベートチャットは Nostr の受信者宛ての kind 4 event になり、bridge された Fediverse user 宛ての kind 4 message は復号され、ChatMessage object として federation へ送られます。bridge はこれらの event を [NIP-42](/ja/topics/nip-42/) で制限された設定済み DM relay に限定し、別の relay key で認証します。この相互運用経路は従来の [NIP-04](/ja/topics/nip-04/) 暗号化を使い、NIP-17 の gift wrapping は今回の実装に含まれません。

### nostream がリリースを行わずに 8 件の PR をマージ

TypeScript relay 実装の [nostream](https://github.com/Cameri/nostream) は今週、リリースを行わずに 8 件の PR をマージしました。中心となる [PR #702](https://github.com/Cameri/nostream/pull/702) と [PR #676](https://github.com/Cameri/nostream/pull/676) は、relay 運営者が利用できる認証とメンバーシップのアクセス制御 stack を組み合わせて実装しました。今週の NIP Deep Dive では、その handshake を詳しく解説します。[PR #694](https://github.com/Cameri/nostream/pull/694) は、汎用の `#e`、`#p`、`#g` などの tag filter が一致した tag row ごとに同じ event を返す問題を修正し、1 つの subscription 内で重複して流れる protocol traffic を減らしました。

### FIPS v0.4.1 が Iris エコシステムの基盤となるトランスポートを強化

[jmcorgan/fips](https://github.com/jmcorgan/fips) は、antipoison state に上限を設け、収束と MTU 処理を修正し、CPU 使用量を削減するメンテナンスリリース [v0.4.1](https://github.com/jmcorgan/fips/releases/tag/v0.4.1) を公開しました。Iris プロジェクト群のブラウザ向け TypeScript runtime [fips-ts](https://github.com/mmalmi/fips-ts) はこの Rust transport と wire 互換であるため、ここでの修正はブラウザとの相互運用性へ直接反映されます。

---

## プロトコル作業と NIP 更新

[NIPs リポジトリ](https://github.com/nostr-protocol/nips)の最近の変更:

**マージ済み:**

- **[NIP-29](/ja/topics/nip-29/)(Relay ベースのグループ): サブグループ**([PR #2319](https://github.com/nostr-protocol/nips/pull/2319)、2026-07-16 マージ): NIP-29 は relay ホスト型グループを定義し、メンバーシップ、ロール、チャット履歴は単一の relay 上でアドレス可能な `kind:39000` 系 event として存在し、モデレーションアクションは `kind:9000` 系の管理者 event によって運ばれます。この PR は、グループがメタデータに `parent` tag を追加し、同じ relay 上の別のグループの `d` 識別子を指すことで、自身をサブグループと宣言できるようにします。サブグループはそれ以外の点では通常のグループです。メンバーシップはカスケードせず(親への参加は子のメンバーシップを与えない)、管理者ロールは継承されず(各サブグループの `kind:39001` 管理者リストが自身のスコープで権威を持つ)、各サブグループは独自の独立した `kind:9000`/`kind:9001` メンバー event を保持します。この階層をサポートする relay は NIP-11 の relay 情報ドキュメントの `nip29` オブジェクトに `"subgroups": true` を記載して広告するため、クライアントはネストされたコミュニティの作成を試みる前にその機能を発見できます。

- **[NIP-29](/ja/topics/nip-29/): メッセージ固定**([PR #2379](https://github.com/nostr-protocol/nips/pull/2379)、2026-07-15 マージ;[PR #2416](https://github.com/nostr-protocol/nips/pull/2416)、2026-07-17 マージ): グループ管理者が relay ベースのグループ内でメッセージを固定できるようになりました。この仕組みは新しいモデレーション event `kind:9010` `update-pin-list` を追加します。これは通常の event id を参照する `e` tag として完全な順序付き固定リストを運び、relay が最新の受理された固定リストをミラーするよう再生成する新しいオプションのグループレベル event `kind:39005` *group pinned events* も追加します。各 `kind:9010` は単一エントリのトグルではなくリスト全体を置き換えるため、固定、固定解除、並べ替え、固定のクリアはすべて 1 つの新しいリストを送信することで表現されます。フォローアップの PR #2416 は形式を拡張し、固定リストで `a` tag も受理されるようにし、管理者が通常のチャットメッセージに加えてアドレス可能な event(長文投稿、wiki ページ、その他のパラメータ化された置き換え可能なコンテンツ)を固定できるようにします。relay は固定数に上限を設けることができ、マージされた仕様テキストは tag が現れる順序で固定を表示することを推奨しています。

- **[NIP-29](/ja/topics/nip-29/): バナー tag と招待コードサフィックス**([PR #2383](https://github.com/nostr-protocol/nips/pull/2383)、2026-07-16 マージ;[PR #2380](https://github.com/nostr-protocol/nips/pull/2380)、2026-07-16 マージ): グループメタデータへの表示とオンボーディングの 2 つの追加。PR #2383 は `kind:39000` グループメタデータ event にオプションの `banner` tag を追加し、既存の `name`、`picture`、`about` フィールドに加わって、クライアントがグループページのヘッダー画像をレンダリングできるようにします。PR #2380 はグループ共有リンクの招待コードサフィックスを定義します。招待コードはグループの `naddr` 識別子に `naddr1...?invite=<code>` として付加できます。bech32 の文字セットには `?` が含まれないため、サフィックスより前の部分はそれ自体で有効な naddr のままであり、この拡張を理解しないクライアントでもグループを解決できます。理解するクライアントは `kind:9021` 参加リクエストの `code` tag を事前入力し、既存の `kind:9009` `create-invite` モデレーション event と組み合わせて、クローズドグループへの参加を簡素化します。

- **[NIP-51](/ja/topics/nip-51/)(リスト): お気に入りフォローセット、kind:10011**([PR #2413](https://github.com/nostr-protocol/nips/pull/2413)、2026-07-15 マージ): NIP-51 は標準のリスト kind を定義し、置き換え可能な `kind:10000` 系リスト(ユーザーごとに 1 つ)とアドレス可能な `kind:30000` 系セット(ユーザーごとに複数、`d` tag でキー付け)に分かれています。この PR は `kind:10011` *お気に入りフォローセット* を追加します。これは `a` tag が `kind:30000` フォローセットを指す標準の置き換え可能なリストです。`kind:30002` relay セットを参照する `a` tag を保持する `kind:10012`(relay フィード)のミラーであり、新しい kind はユーザーが自分自身や他者が公開した pubkey コレクションの厳選リストなど、名前付きフォローセットをブックマークし、クライアントがワンタップでのフォローやフィード切り替えのためにそれらを表示できるようにします。この kind 番号はすでに争われていることに注意してください。下記のオープン中のリナンバリング PR を参照してください。

- **[NIP-46](/ja/topics/nip-46/)(Nostr Connect): サイレントタイムアウトのガイダンス**([PR #2375](https://github.com/nostr-protocol/nips/pull/2375)、2026-07-15 マージ): NIP-46 はリモート署名プロトコルで、クライアントが暗号化された JSON-RPC スタイルのリクエストを relay 経由で署名者(bunker)に送信し、暗号化された応答を待ちます。マージされた変更はワイヤー動作に関する 1 文です。未知またはサポートされていないメソッドで行われたリクエストには、エラーで応答しなければなりません(MUST)。以前は、実装していないメソッドを受け取った署名者が応答しないことがあり、「サポートされていないメソッド」と「署名者オフライン」を区別する方法がないまま、クライアントは自身のタイムアウトが発火するまでハングしていました。義務付けられたエラー応答により、クライアントは素早く失敗し、無限にスピンする代わりに意味のあるメッセージをユーザーに表示できます。

**オープン中の PR とディスカッション:**

- **kind:10011 から kind:10021 へのリナンバリング**([PR #2417](https://github.com/nostr-protocol/nips/pull/2417)): 新しくマージされたお気に入りフォローセットリストを `kind:10011` から `kind:10021` に移動します。`10011` がすでに他で使用されているためです。リナンバリング PR は元のマージから数日以内にオープンされたため、お気に入りフォローセットを実装するクライアントはこの PR を追跡し、`10011` ではなく最終番号を対象にすべきです。

- **[NIP-47](/ja/topics/nip-47/)(Nostr Wallet Connect): コアの簡素化**([PR #2419](https://github.com/nostr-protocol/nips/pull/2419)): アプリが Nostr 経由でリモートウォレットに Lightning 支払いをリクエストできるウォレット接続プロトコル NIP-47 を、より小さなコア仕様に絞ることを提案します。オプションでより専門的な機能は `47.md` から専用の拡張リポジトリ [nostr-wallet-connect/nwc](https://github.com/nostr-wallet-connect/nwc) に移され、拡張仕様がコアとは独立に進化できるようになります。明示された目標は、以前の NWC コールで合意された、最小限のウォレット接続レイヤーとよりリッチなオプション動作を分離する方向に従い、コアを小さく、安定し、実装しやすく保つことです。NIP-47 がウォレットとアプリ全体に広くデプロイされていることを考えると、NWC を話すすべての人がこの再構成の議論を追跡すべきです。

- **Trusted Relay Assertions(ドラフト、番号未割当)**([PR #2418](https://github.com/nostr-protocol/nips/pull/2418)): Nostr relay に関する信頼評価を公開する標準を提案し、[NIP-11](/ja/topics/nip-11/)(relay が自身について主張すること)と [NIP-66](/ja/topics/nip-66/)(モニターが測定したこと)に並ぶ「私たちが結論づけること」レイヤーとして位置づけられています。アサーションプロバイダーは観測されたメトリクス、運営者の評判、ユーザーレポートから信頼スコアを計算し、クライアントは接続する relay を選ぶ際にこれらのアサーションをクエリします。ドラフトは `kind:30385`(アドレス可能な Trusted Relay Assertion。スコア、信頼性、品質、アクセシビリティ、運営者、ポリシー、管轄区域の tag を運ぶ)、`kind:10385`(置き換え可能な Trusted Provider List。ユーザーが選んだアサーションプロバイダー)を導入し、relay と運営者のレポートに [NIP-32](/ja/topics/nip-32/) ラベルを再利用します。まだ NIP 番号は割り当てられておらず、初期段階のドラフトです。

- **フィルターの AND 演算子(「NIP-91」、提案中、番号はまだリポジトリにない)**([PR #2252](https://github.com/nostr-protocol/nips/pull/2252)): NIP-01 の下では、tag フィルターは OR のみです。フィルター `"#t": ["meme", "cat"]` はどちらかの tag を持つ event にマッチします。この提案はインデックス可能な tag に `&` 修飾子を追加し、`"&t": ["meme", "cat"]` が両方の tag を持つ event のみを返すようにし、クライアントが過剰にフェッチしてローカルでフィルタリングする代わりに、relay がサーバーサイドで交差を行えるようにします。ルールは、AND が OR より優先されること、AND で使用される tag 値はサポートする relay によって OR では無視されるべきこと、そしてクライアントは拡張をサポートしない relay との互換性のために標準の `#` OR tag も含めなければならないこと(MUST)を規定しています(それらの relay はより広い OR 結果を返し、クライアントがローカルで交差します)。この PR は以前の提案の再オープン継続であり、nostr-rs-relay docker イメージ、netstr、Snort ワーカー relay を含む relay 実装を挙げています。NIP-91 番号は PR ブランチにのみ現れ、まだリポジトリの README の NIP インデックスにはないため、番号は暫定的なものとして扱ってください。

- **Nostr web アプレット(「NIP-5D」、提案中、番号はまだリポジトリにない)**([PR #2303](https://github.com/nostr-protocol/nips/pull/2303)): iframe や webview で実行されるサンドボックス化された web アプリケーション(「napplet」)がホスティングアプリケーション(「シェル」)と通信するための `postMessage` プロトコルを定義します。仕様は意図的に薄いコアです。メッセージエンベロープ、サンドボックスルール(napplet の iframe は `allow-same-origin` なしで `sandbox="allow-scripts"` を使用しなければならず(MUST)、シェルは iframe 内で `window.nostr` NIP-07 を公開してはならない(MUST NOT))、`event.origin` ではなく偽造不可能な `MessageEvent.source` window 参照による送信者識別、そしてマニフェストベースの機能ネゴシエーションを規定します。署名、relay アクセス、ストレージ、napplet 間通信のための実際のプロトコルメッセージは NAP(Nostr Applet Protocol)拡張仕様に委任され、それぞれが機能ドメインを所有し、署名と暗号化は常にシェルによって仲介されるため、鍵はサンドボックスに入りません。この提案は NIP-5A napplet マニフェスト仕様に依存しており、今週はタイムリーです。Amethyst の v1.13.0 プレリリース作業には napplet のアカウント分離が含まれており、クライアントサイドの napplet ホスティングが活発な実装領域となっています。上記の「NIP-91」と同様に、5D 番号は暫定的です。

---

## NIP Deep Dive: NIP-42 と NIP-43

誰にでも開かれていない relay を運営することは、かつてはすべてを自分で発明することを意味しました。有料または招待制の relay 運営者は帯域外でホワイトリストを維持しなければならず、通常は DM で集めた pubkey のテキストファイルで、接続されたクライアントに「あなたが誰か証明せよ」と伝える標準的な方法も、ユーザーが参加を求めたり自分がメンバーかどうかを知る標準的な方法もありませんでした。ゲート付きの読み取りや書き込みを望むすべての relay が独自のプライベートな仕組みを構築し、クライアントはそのどれとも相互運用できませんでした。[NIP-42](/ja/topics/nip-42/) はその問題の身元証明の半分を標準化し、[NIP-43](/ja/topics/nip-43/) はメンバーシップの半分を標準化します。今週、TypeScript relay の nostream はこのペアをエンドツーエンドでマージしました。[PR #702](https://github.com/Cameri/nostream/pull/702) は暗号化された kind の読み取りを認証された受信者に制限し、[PR #676](https://github.com/Cameri/nostream/pull/676) は参加および脱退リクエストの event 戦略を追加し、どちらも 7 月 20 日にマージされました。

### NIP-42: クライアントから relay への認証

[NIP-42](/ja/topics/nip-42/) は 1 つの問いに答えます。この接続にいるのは誰か? 読み取りや書き込みをゲートしたい relay は、接続時またはリクエストが認証を必要とする際にオンデマンドで、チャレンジ文字列を運ぶ `AUTH` メッセージを送信します。クライアントは署名済みの一時 event、kind 22242 を含む自身の `AUTH` メッセージで応答し、relay は認証 event が通常の書き込みであるかのように正確に `OK` メッセージで応えます。認証されたセッションは接続の間保持され、クライアントは一連の `AUTH` メッセージで 1 つの接続上で複数の pubkey を認証でき、それぞれを relay は認証済みとして扱います。

署名済みの認証 event は次のようになります:

```json
{
  "id": "4ef6f2c0b1a84c9a3d0f9c58e2a1b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0",
  "pubkey": "c308e1f882c1f1dff2a43d4294239ddeec04e575f2d1aad1fa21ea7684e61fb5",
  "created_at": 1753195800,
  "kind": 22242,
  "tags": [
    ["relay", "wss://relay.example.com/"],
    ["challenge", "challengestringhere"]
  ],
  "content": "",
  "sig": "8b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1"
}
```

`pubkey` は証明されるアイデンティティで、relay は event `id` に対する `sig` をそれに照らして検証します。kind 22242 は一時的な範囲にあり、この event は接続レベルのクレデンシャルであり、relay はそれを保存したり他のクライアントにブロードキャストしたりしてはいけません。`relay` tag は署名を 1 つの relay URL に束縛し、キャプチャされた認証 event が別の relay に対してリプレイされるのを防ぎ、`challenge` tag はそれをこの接続で relay が発行した特定のチャレンジ文字列に束縛し、後の接続でのキャプチャされた認証のリプレイをブロックします。`created_at` は現在時刻に近く、おおよそ 10 分のウィンドウ内でなければならず、古い認証 event は自然に失効します。`content` フィールドは空で、何も公開されていません。

仕様はまた、ゲートをクライアントに可視化する 2 つの機械可読なプレフィックスを定義しています。クライアントがまだ認証していないためにサブスクリプションを拒否する relay は `auth-required:` で始まる `CLOSED` メッセージで応答し、拒否された書き込みは同じプレフィックスの `OK` を受け取ります。認証したもののまだそのアクションの権限を欠くクライアントは代わりに `restricted:` を受け取ります。この区別が [nostream の PR #702](https://github.com/Cameri/nostream/pull/702) の基盤です。暗号化された kind の読み取りは、リクエスト元の pubkey が受信者であることを証明するまで `auth-required:` で閉じることができるようになりました。

### NIP-43: Relay アクセスメタデータとリクエスト

[NIP-43](/ja/topics/nip-43/) は続く問いに答えます。relay があなたが誰かを知った今、あなたは何を許されているか? NIP-42 がライブ接続上のハンドシェイクであるのに対し、NIP-43 はメンバーシップ状態を記述し、ユーザーがその変更を求めることを可能にする公開 event のセットです。relay 側では、relay の [NIP-11](/ja/topics/nip-11/) `self` フィールドの pubkey によって署名された kind 13534 event が、pubkey ごとに 1 つの `member` tag をリストし、オプションのロール引数は kind 33534 として公開されたロール定義を指します。kind 8000 はメンバーの追加を、kind 8001 は削除を告知し、どちらも影響を受けるメンバーの `p` tag とともに同じ relay 鍵で署名されます。ユーザー側では、kind 28934 は `claim` tag に招待コードを運ぶ参加リクエスト、kind 28935 はユーザーがクレームを要求したときに relay がその場で生成する一時的な招待コード event、kind 28936 は脱退リクエストです。

参加リクエストは次のようになります:

```json
{
  "id": "9f0e1d2c3b4a59687a6b5c4d3e2f1098a7b6c5d4e3f2019a8b7c6d5e4f3021a9b8",
  "pubkey": "ee1d336e13779e4d4c527b988429d96de16088f958cbf6c074676ac9cfd9c958",
  "created_at": 1753195900,
  "kind": 28934,
  "tags": [
    ["-"],
    ["claim", "invite-code-from-operator"]
  ],
  "content": "",
  "sig": "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2"
}
```

`pubkey` は参加を求めるユーザーで、kind 28934 がこの event を参加リクエストとして示します。`-` tag は [NIP-70](/ja/topics/nip-70/) の保護された event マーカーで、relay にこの event を作者以外から受け付けないよう伝えます。`claim` tag はユーザーが帯域外で入手した招待コードを運び、`created_at` は現在時刻から数分以内でなければならず、古いリクエストはリプレイできません。relay はクレームに `OK` メッセージで応答し、期限切れや無効なコードなどの失敗には NIP-42 の `restricted:` プレフィックスを再利用し、その後 kind 13534 リストを更新し、kind 8000 のメンバー追加 event を公開することができます。メンバーシップは意図的に単一の event から導出されません。仕様は relay 署名のリストを網羅的または権威的と見なすべきではないと述べ、誰かが現在メンバーかどうかを判断するクライアントは relay の kind 13534 とメンバー自身の event の両方を参照すべきです。クライアントは参加、招待、脱退リクエストを、NIP-11 ドキュメントの `supported_nips` セクションでこの NIP を広告する relay にのみ送信しなければならず、[nostream の PR #676](https://github.com/Cameri/nostream/pull/676) はこれらのリクエスト kind を実際のメンバーシップ変更に変える relay 側の仕組みです。

### 歴史

NIP-42 は 2 つのうちではるかに古い方です。2023 年 1 月 2 日に [commit c80be21c](https://github.com/nostr-protocol/nips/commit/c80be21c) で NIPs リポジトリに入り、fiatjaf が semisol によって起草された以前の relay 認証 NIP を大幅に簡素化し、より複雑なチャレンジスキームを、仕様が今日も使う単一の署名済み一時 event に集約しました。NIP-43 ははるかに遅く、2025 年 10 月 30 日に hodlbod の [PR #1079](https://github.com/nostr-protocol/nips/pull/1079) がマージされ、NIP-42 の `restricted:` プレフィックスの上に直接構築された relay アクセスメタデータとリクエストが追加されました。2 年半のギャップは、メンバーシップレイヤーに標準ができる前に、エコシステムが有料およびプライベート relay をアドホックなホワイトリストで運営していた期間の長さを反映しています。

### 実装

relay 側では、[nostream](https://github.com/Cameri/nostream) が今週のマージで両半分を出荷するようになりました。[strfry](https://github.com/hoytech/strfry) は NIP-42 を実装し、その ingester で kind 22242 認証 event を検証し、設定からチャレンジを発行します。[nostr-rs-relay](https://github.com/scsibug/nostr-rs-relay) は接続レイヤーで AUTH ハンドシェイクを処理し、チャレンジとタイムスタンプウィンドウをカバーするテストがあります。[khatru](https://github.com/fiatjaf/khatru)(Go relay フレームワーク)は接続ごとに認証された pubkey を追跡し、ポリシーがそれに基づいて読み取りと書き込みをゲートできるようにします。クライアント側では、[Amethyst](https://github.com/vitorpamplona/amethyst) が Concord 暗号化コミュニティ向けのストリームごとの認証を含め、relay チャレンジへの kind 22242 応答に署名します。2 つの NIP はアクセス制御をきれいな線で分割します。NIP-42 は身元証明で、1 つの接続、1 つのチャレンジ、数分の有効性にスコープされ、ポリシーについては何も述べません。NIP-43 はポリシーで、通常の relay event として表現されます。誰がメンバーか、誰が追加または削除されたか、そしてユーザーがそれらの遷移をどう要求するかです。実装者が念頭に置くべきギャップは、NIP-43 のオプションのロールメタデータを超えるより細かい権限を標準化するものはまだないため、バイナリのメンバー/非メンバー分割以上のことを行う relay はそのレイヤーを独自に設計しているということです。

---

今週は以上です。何かを構築していますか、共有するニュースはありますか? NIP-17 DM で連絡するか、Nostr で私たちを見つけてください。
