---
title: 'Nostr Compass #3'
date: 2025-12-31
translationOf: /en/newsletters/2025-12-31-newsletter.md
translationDate: 2026-04-23
draft: false
type: newsletters
---

Nostr Compassへようこそ。Nostrプロトコルエコシステムの週刊ガイドです。

**今週の内容:** 2025年の締めくくりとして、Nostrの進化における12月の節目を5年分振り返ります。2020年12月のfiatjafによる最初のクライアント公開から、2022年12月のJack Dorseyによる14 BTCの寄付、そして今月の[NIP-55](/ja/topics/nip-55/)署名アプリの広がりとNDKの162倍キャッシュ高速化まで、12月は一貫してプロトコルの転換点になってきました。今回は、実験的な2つのrelayから50か国2,500超のノードへと成長した技術史を、各年の12月を通してたどります。あわせて、AmethystのデスクトップモジュールがQuartzで形になり、Notedeckはメッセージ機能を獲得し、CitrineはWebアプリをホスト可能になり、[NIP-54](/ja/topics/nip-54/)は非ラテン文字向けの国際化問題を修正しました。

## 12月の回顧: Nostrの5回の12月

Nostrは今年で5年になります。fiatjafがプロトコルを始めたのは2020年11月7日で、それ以降の毎年12月は、その進化のはっきり異なる段階を刻んできました。概念実証から世界的なムーブメントへ、さらに本番運用されるエコシステムへ。本稿は、Nostrの土台を形作り、ブレイクアウトの契機となった2020年12月から2025年12月までを技術的に振り返るものです。

### 2020年12月: 創世記

Nostrが存在して初めて迎えた丸1か月のあいだに、fiatjafはプロトコル初のクライアントである[Branle](https://github.com/fiatjaf/branle)を公開しました。これはQuasar（Vue.js）とabsurd-sqlをローカルストレージに使った実装でした。fiatjafはすでに中核アーキテクチャを定めていました。ユーザーはsecp256k1公開鍵で識別され、すべての投稿は暗号学的に署名され、relayは相互に通信しない単純なストレージとして機能します。11月16日に始まったTelegramグループ[@nostr_protocol](https://t.me/nostr_protocol)で調整していた初期採用者のごく少人数を、1つか2つの実験的relayが支えていました。[当初のドキュメント](https://fiatjaf.com/nostr.html)はNostrを「検閲耐性のあるグローバルなソーシャルネットワークを作れる、最もシンプルなオープンプロトコル」と説明していましたが、その前提が実証されるまでにはさらに2年を要しました。

### 2021年12月: 初期開発期

2021年12月31日、NostrはCameriによる投稿で[Hacker Newsのフロントページ](https://news.ycombinator.com/item?id=29749061)に載り、110ポイントと138件のコメントを集めました。これはプロトコルがより広い開発者コミュニティに初めて大きく露出した瞬間でした。ネットワークは約7つのrelayと1,000人未満のユーザーで動いていました。Branleには12月31日の秘密鍵インポートや複数relayサポートなどの更新が入り、コマンドラインクライアントのnosclはターミナルからの操作を提供していました。プロトコル仕様はまだfiatjaf個人のドキュメントにあり、正式な[NIPsリポジトリ](https://github.com/nostr-protocol/nips)が作られるのは2022年5月になってからです。当時のプロトコルは、fiatjaf自身の言葉どおり「進行中の作業」でした。

### 2022年12月: 転換点

2022年12月は、Nostrをニッチな実験から主流のムーブメントへ押し上げました。きっかけは12月15日、Jack Dorseyがプロトコルを知り、「Blueskyに私たちが求めていたものを100パーセント満たしているが、企業から開発されたものではない」と述べたうえで、fiatjafに[14.17171699 BTC](https://www.coindesk.com/tech/2022/12/15/jack-dorsey-gives-decentralized-social-network-nostr-14-btc-in-funding)（約24.5万ドルから25万ドル）を寄付したことでした。12月16日、fiatjafはその資金をDamus開発者William Casarin（jb55）と分けると発表し、Dorsey自身もNostrアカウント（npub: `npub1sg6plzptd64u62a878hep2kev88swjh3tw00gjsfl8f237lmu63q0uf63m`）を認証しました。この資金提供によって、プロジェクトは一夜にして正当性を得ました。

同じ週、Twitterの混乱が採用を後押ししました。12月14日から15日にかけてはNew York Times、CNN、Washington Postの著名ジャーナリストたちが停止されました。12月18日にはTwitterが[NostrやMastodonなどを宣伝するアカウントの禁止](https://techcrunch.com/2022/12/18/twitter-wont-let-you-post-your-facebook-instagram-and-mastodon-handles/)を発表し、翌日には反発を受けて撤回しました。この流出が、ユーザーに代替手段を探させる原動力になりました。

プロトコル開発も急加速しました。12月16日には[NIP-19](/ja/topics/nip-19/)がマージされ（[#57](https://github.com/nostr-protocol/nips/pull/57)）、bech32でエンコードされた識別子（npub、nsec、note、nprofile、nevent）が導入され、鍵が人間に読みやすく区別しやすくなりました。その月のNIPsリポジトリには36件超のコミットが入り、NIP-40やNIP-07の更新も含まれていました。クライアントも増殖し、Damusは数時間でTestFlightベータが満員になり、Astralはプロフィール作成のためにBranleをフォークし、Snortは「高速で検閲耐性のある」Webクライアントとして立ち上がり、Vitor PamplonaはAmethystの開発を始めました。Alby v1.22.1「Kemble's Cascade of Stars」は12月22日に[NIP-19](/ja/topics/nip-19/)対応で出荷されました。12月7日時点でNostrにはプロフィールを持つユーザーがおよそ800人いましたが、Damusが2023年1月31日にApp Storeへ登場すると、成長は一気に加速し、2023年6月までに31.5万人超へ達しました。

### 2023年12月: エコシステムの成熟

2023年12月は、Nostrプロトコルのセキュリティにとって重要な変曲点でした。12月20日、独立したCure53セキュリティ監査（NOS-01）でTypeScript、Go、Rust実装にタイミング攻撃やforward secrecyの懸念を含む10件の問題が見つかったあと、[NIP-44 revision 3がマージ](https://github.com/nostr-protocol/nips/pull/746)されました。更新後の仕様は、不完全だった[NIP-04](/ja/topics/nip-04/)暗号化をChaCha20とHMAC-SHA256で置き換え、現在の[NIP-17](/ja/topics/nip-17/)プライベートDMと[NIP-59](/ja/topics/nip-59/) Gift Wrapを支える暗号基盤を確立しました。同じ週の12月21日には、[OpenSatsが第4回Nostr grantsを発表](https://opensats.org/blog/nostr-grants-december-2023)し、Lume、noStrudel、ZapThreads、独立したNIP-44監査を含む7プロジェクトを支援しました。これは2023年7月の[第1回助成](https://opensats.org/blog/nostr-grants-july-2023)に続くもので、Damus、Coracle、Irisなどを含め、Nostr Fund全体の配分は39件で約340万ドルに達しました。

この月は、エコシステムの持続可能性をめぐる緊張も露呈させました。12月28日、William Casarin（jb55）は[Stacker Newsへの投稿](https://stacker.news/items/368863)で、Appleのアプリ内zap制限によって収益化が大きく妨げられたことを理由に、「2024年はおそらくDamusにとって最後の年になる」と述べました。Damusチームはそれ以前にVC資金も断っています。一方で、[Nostr Wallet Connect v0.4.1](https://github.com/getAlby/nostr-wallet-connect/releases/tag/0.4.1)は12月26日に出荷され、[NIP-47](/ja/topics/nip-47/)を`pay_keysend`、`make_invoice`、`lookup_invoice`、`list_transactions`、`get_balance`、`get_info`メソッドで拡張しました。これは後に複数クライアントで標準になっていくウォレット統合の土台を築きました。

### 2024年12月: プロトコルの前進

2024年12月は、11月30日の[Notedeck Alpha公開](https://damus.io/notedeck/)から始まりました。これはDamusチームによるRust製デスクトップクライアントで、マルチカラムUIと複数アカウント対応を備えています。Linux、macOS、Windows向けに構築され、Androidは2025年予定でした。当初はDamus Purple購読者向けに提供され、iOSを超える戦略的拡張を示していました。2週間後の12月16日には、[OpenSatsが第9回Nostr grantsを発表](https://opensats.org/blog/9th-wave-of-nostr-grants)し、パーソナライズされたフィード向け初のアルゴリズムrelayであるAlgoRelay、通信制限下のインターネット向けBluetooth mesh対応AndroidアプリPokey、[NIP-60](/ja/topics/nip-60/)の[Cashu](/ja/topics/cashu/)トークン保存を行うNostr Safebox、軽量でアクセシブルなWebクライアントLumiLumiを支援しました。これによりNostr Fundの総配分は約900万ドルへ伸び、前年同期比67%増となりました。

この月はクライアント成熟の大きな進展も見せました。[Gossip 0.13.0](https://github.com/mikedilger/gossip/releases/tag/v0.13.0)は12月23日に、File Metadataの[NIP-92](/ja/topics/nip-92/)/[NIP-94](/ja/topics/nip-94/)サポート、Blossom統合、[NIP-50](/ja/topics/nip-50/) relay検索を携えて公開されました。[Coracle 0.5.0](https://github.com/coracle-social/coracle/releases/tag/0.5.0)は12月12日に、再設計されたオンボーディングとnostr-editor統合付きで出荷されました。プロトコル開発も活発で、12月9日から22日の間に30件のPRが提出され、そのうち10件がマージされています。内容には、[NIP-46](/ja/topics/nip-46/)のNIP-44暗号化専用への書き換えや、Signalレベルのdouble ratchet暗号化を目指す[NIP-104](/ja/topics/nip-104/)の継続作業が含まれていました。ネットワーク統計では、信頼済みpubkeyイベントが日次22.4万件超に達し、コンタクトリスト付き新規プロフィールは前年比4倍、公開ライティングイベントは50%増となりました。

### 2025年12月: エコシステムの拡大

2025年12月も、プロトコルの成熟とエコシステムの拡大が続きました。12月21日、[OpenSatsは第14回Nostr grantsを発表](https://opensats.org/blog/fourteenth-wave-of-nostr-grants)し、3つのプロジェクトを支援しました。長文コンテンツのクリエーターポータルと[Cashu](/ja/topics/cashu/)/Nutzaps決済統合を持つマルチプラットフォームクライアントYakiHonne、Amethystを支え将来のiOS版を可能にするVitor PamplonaのKotlin MultiplatformライブラリQuartz、そしてPlebOneによるRSSとNostrの双方向統合であるNostr Feedzです。加えて、Dart NDKとMattnのnostr-relayには更新助成が行われました。

プロトコル面では、11月にマージされた[NIP-BE](/ja/topics/nip-be/)（Bluetooth Low Energyメッセージング、[#1979](https://github.com/nostr-protocol/nips/pull/1979)）が、オフラインデバイス同期を可能にしました。その月の後半には[NIP-A4](/ja/topics/nip-a4/)（Public Messages、kind 24、[#1988](https://github.com/nostr-protocol/nips/pull/1988)）が入り、スレッドの複雑さを避けるため`q`タグを使う通知画面向けメッセージを定義しました。[NIP-29](/ja/topics/nip-29/)には大規模な明確化が入り（[#2106](https://github.com/nostr-protocol/nips/pull/2106)）、真にプライベートで発見不能なグループのための`hidden`タグが導入されました。[NIP-55](/ja/topics/nip-55/)仕様にも改訂があり（[#2166](https://github.com/nostr-protocol/nips/pull/2166)）、開発者がバックグラウンドプロセスから`get_public_key`を呼んでしまう一般的な実装ミスに対処しました。

クライアント側では、[Primal Androidが完全なNIP-55署名アプリになり](/ja/newsletters/2025-12-24-newsletter/#news)、8件のマージ済みPRで`LocalSignerContentProvider`を実装し、AmberとAegisに並ぶAndroid署名オプションとなりました。[NDKライブラリは162倍高速なキャッシュクエリを達成し](/ja/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)、重複書き込みと不要なLRUキャッシュ参照を排除することで、約3,690msから約22msまで短縮しました（[PR #371](https://github.com/nostr-dev-kit/ndk/pull/371)、[PR #372](https://github.com/nostr-dev-kit/ndk/pull/372)）。Shopstrはzapによるフラッシュセール機能[Zapsnags](/ja/newsletters/2025-12-24-newsletter/#news)を導入しました。White Noiseは[MIP-05](/ja/topics/mip-05/)のプライバシー保護プッシュ通知を出荷しています。詳細は[ニュースレター #1](/ja/newsletters/2025-12-17-newsletter/)と[ニュースレター #2](/ja/newsletters/2025-12-24-newsletter/)をご覧ください。

---

5年前、fiatjafはBranleを2つの実験的relay上のごく少数のユーザー向けに公開しました。現在、このプロトコルは140超のクライアント、50か国にまたがる2,500超のrelay、そして数十万の鍵ペアを結ぶ成長中のweb of trustを支えています。今月も12月らしい大型リリースの流れは続き、Bluetoothメッセージング、Android署名アプリの広がり、インフラ助成は、クロスプラットフォームのツール群に対する継続的な投資を示していました。

## ニュース

**Amethystデスクトップが形になり始める** - OpenSats第14回助成のQuartz支援は、すでに成果を出し始めています。[PR #1625](https://github.com/vitorpamplona/amethyst/pull/1625)は、Compose Multiplatformを使ったAmethyst向けの完全な`:desktopApp`モジュールを作成し、Desktop JVM上でログイン画面とグローバルフィード画面を動作可能にしました。アーキテクチャは`:commons`モジュールを、`commonMain`、`jvmAndroid`、`androidMain`、`jvmMain`という明確なソースセット構造を持つKotlin Multiplatformへ変換しています。これによりAndroidとデスクトップでUIコンポーネントを共有しつつ、プラットフォーム固有の判断は各ターゲットに委ねられます。同じKotlin Multiplatformの流れで、将来のiOS版の土台にもなります。

**Amethystに音声返信** - davotoulaからのクリスマスプレゼントとして、[PR #1622](https://github.com/vitorpamplona/amethyst/pull/1622)は専用の音声返信画面を追加しました。波形表示、録り直し対応、メディアサーバー選択、アップロード進捗表示を備えています。ユーザーはこれで、ルート音声メッセージにも既存の音声返信にも、音声で返答できます。

**Notedeckがメッセージ機能を追加** - DamusのデスクトップクライアントであるNotedeckは、[PR #1223](https://github.com/damus-io/notedeck/pull/1223)でメッセージ機能を獲得し、タイムライン閲覧だけでなくダイレクトなコミュニケーション領域へ踏み出しました。

**CitrineがWebアプリをホスト** - Citrineは今や[Webアプリケーションをホスト](https://github.com/greenart7c3/Citrine/pull/81)でき、スマートフォンをローカルファーストなNostr Webサーバーに変えます。別の[PR #85](https://github.com/greenart7c3/Citrine/pull/85)では、ネットワーク接続が戻ったときの自動再接続とイベント配信が追加され、Android APIレベルをまたぐ包括的なテストも整備されました。

**Nostrabilityの開発者ツールキットレジストリ** - [Developer Kits & Tooling](https://github.com/nostrability/nostrability/issues/264)トラッカーは、TypeScript、Rust、Python、Go、Dart、Swiftなど多言語にわたるSDK、ライブラリ、開発者ツールのキュレーション済みレジストリを維持しています。Nostr開発を始めたばかりなら、自分のスタックに合うツールキットを探す出発点として有用です。

## NIP更新

[NIPsリポジトリ](https://github.com/nostr-protocol/nips)への最近の変更:

- **[NIP-54](/ja/topics/nip-54/)** - Wikiのd-tag正規化に関する重要な国際化修正（[#2177](https://github.com/nostr-protocol/nips/pull/2177)）。従来のルールでは、すべての非ASCII文字が`-`へ変換され、日本語、中国語、アラビア語、キリル文字などのサポートが壊れていました。更新後の仕様ではUTF-8の文字を保持し、大文字小文字の区別がある文字にのみ小文字化を適用します。例も充実しており、`"ウィキペディア"`は`"ウィキペディア"`のまま、`"Москва"`は`"москва"`となり、`"日本語 Article"`のような混在スクリプトは`"日本語-article"`に正規化されます。

## リリース

**Zapstore 1.0-rc1** - Nostrベースのパーミッションレスなアプリストアが、新アーキテクチャの[最初のリリース候補](https://github.com/zapstore/zapstore/releases/tag/1.0-rc1)を公開しました。完全なUI刷新、改善されたエラーハンドリングを備えた書き直し済みパッケージマネージャー、キュレート発見用のApp Stacks、再設計されたプロフィール画面、バックグラウンド更新チェック、リリース一覧の無限スクロールを含みます。

**KeyChat v1.38.1** - MLSベースの暗号化メッセージングアプリが、AndroidとLinux向けのプッシュ通知に[UnifiedPushサポートを追加](https://github.com/keychat-io/keychat-app/releases/tag/v1.38.1%2B6489)しました。加えて、プライバシー関連操作向けの生体認証も入っています。Android、Windows、macOS、Linuxで利用できます。

**Alby Go v2.0.0** - モバイルLightningウォレットのコンパニオンアプリが、[ビジュアル刷新を出荷](https://github.com/getAlby/go/releases/tag/v2.0.0)しました。新ロゴ、更新されたカラーパレット、再設計されたアドレス帳、改善された金額入力キーボードを含みます。BTC Mapはホーム画面から利用でき、通知にはトランザクション説明も表示されます。

**nak v0.17.4** - fiatjafのコマンドラインNostrツールが[リリース](https://github.com/fiatjaf/nak/releases/tag/v0.17.4)されました。先週のv0.17.3で入ったLMDBのLinux制限修正に続くものです。

## 注目すべきコードとドキュメントの変更

*オープンPRや初期段階の作業で、今後追う価値があるもの。*

### Damus (iOS)

[NIP-19 relay hint](https://github.com/damus-io/damus/pull/3477)は、イベント取得時のrelay hint消費を実装します。ユーザーがnevent、nprofile、naddrリンクを開くと、Damusはbech32のTLVデータからrelay hintを抽出し、ユーザーのrelayプールにないコンテンツを取得するために一時的なrelayへ接続します。実装には、並行ルックアップ時のレース条件を防ぐためのref-countedクリーンアップも含まれます。[画像URL検出](https://github.com/damus-io/damus/pull/3474)は、作成画面に貼り付けた画像URLを自動的にプレビューサムネイルへ変換し、複数画像時にはカルーセル位置バッジも表示します。[npub貼り付け変換](https://github.com/damus-io/damus/pull/3473)は、貼り付けたnpub/nprofile文字列を、非同期プロフィール解決付きのメンションリンクへ変換します。

### Amethyst (Android)

[Payment targets](https://github.com/vitorpamplona/amethyst/pull/1627)は、[NIP-57](/ja/topics/nip-57/)のzap分配向けイベントインターフェースを追加し、投稿が複数の受取人を指定して入ってきたzapを分け合えるようにします。コラボレーション、収益分配、あるいはコンテンツ作成者とその利用ツールの両方へのチップに使えます。[Quartz feature parity documentation](https://github.com/vitorpamplona/amethyst/pull/1624)は、Android、Desktop JVM、iOSの各ターゲットでどの機能が実装済みかを追跡する詳細な表を追加し、iOS側では中核暗号（`Secp256k1Instance`）、JSONシリアライズ、データ構造が未実装であると記しています。

### Notedeck (Desktop)

[Timeline filter rebuild](https://github.com/damus-io/notedeck/pull/1226)は、アンフォロー済みアカウントがフィードに出続けるバグを修正します。タイムラインフィルターはコンタクトリストから一度だけ構築され、その後更新されていませんでした。この修正では`contact_list_timestamp`の追跡と、フォロー状態が変わったときに再構築を発火する`invalidate()`メソッドが追加されています。

### Citrine (Android Relay)

[ContentProvider API](https://github.com/greenart7c3/Citrine/pull/86)は、ローカルrelayのイベントデータベースを`ContentResolver`経由で他のAndroidアプリへ公開します。WebSocketインターフェースとは異なり、こちらはアプリが永続接続を維持したりNostr relayプロトコルを話したりする必要がありません。ContentProviderはAndroidネイティブのIPC機構を通じて、同期的なデータベースアクセスを提供します。外部アプリはID、pubkey、kind、日付範囲でイベントをクエリし、バリデーション付きで新規イベントを挿入し、ソケット接続を管理せずにイベントを削除できます。

### rust-nostr (Library)

[NIP-40 relay-level support](https://github.com/rust-nostr/nostr/pull/1183)は、期限切れ処理をrelay builderレベルに追加します。期限切れイベントは保存前に拒否され、クライアント送信前にも除外されるため、各データベース実装が独自に期限確認を持つ必要がなくなります。

### nak (CLI)

[Blossom mirror](https://github.com/fiatjaf/nak/pull/91)は、コマンドラインツール向けのblobミラーリング機能を実装します。

### Mostro (P2P Trading)

[Dev fee audit events](https://github.com/MostroP2P/mostro/pull/559)は、kind 8383のNostrイベントを通じて開発基金支払いの透明な監査証跡を追加します。実装では、成功した手数料支払いのあとに非ブロッキングな監査イベントを公開し、注文詳細と支払いハッシュを含めつつ、プライバシー保護のため買い手と売り手のpubkeyは除外します。

### MDK (Marmot Development Kit)

3件のセキュリティ監査修正が入りました。[Author verification](https://github.com/marmot-protocol/mdk/pull/40)は、rumorのpubkeyがMLS送信者資格情報と一致することを強制し、なりすまし攻撃を防ぎます。[KeyPackage identity binding](https://github.com/marmot-protocol/mdk/pull/41)は、credential identityがイベント署名者と一致することを検証します。[Admin update validation](https://github.com/marmot-protocol/mdk/pull/42)は、空の管理者集合や非メンバーへの管理者割り当てを防ぎます。

### Shopstr (Marketplace)

[HODL invoice escrow](https://github.com/shopstr-eng/shopstr/pull/217)は、実物商品のためのtrust-minimizedな支払いシステムを実装します。この構成ではAlbyの`makeHoldInvoice`を使って買い手の資金を自分のウォレット内にロックし、マーチャントの在庫確認後にのみ決済が実行されます。やり取りのプロトコルは[NIP-17](/ja/topics/nip-17/)暗号化DM上で進みます。買い手が注文要求を送り、販売者がHODL invoiceで返し、買い手が支払い、販売者が在庫と発送を確認したあとに、決済が資金を解放します。複数マーチャントのカートにも対応し、支払いはベンダーごとに分割されます。

### Jumble (Web Client)

[Per-relay discovery mode](https://github.com/CodyTseng/jumble/pull/713)は、特定のrelayでフォロー中ユーザーの投稿を非表示にするトグルを追加し、言語ベースの発見フィード（例: nostr.band/lang/*）を可能にします。この機能は、著者pubkeyがユーザーのフォローリストにある投稿を除外し、トグル状態をrelay URLごとにlocalStorageへ保存します。

### White Noise (Encrypted Messaging)

[Media upload retry](https://github.com/marmot-protocol/whitenoise/pull/937)は、失敗したアップロードの再試行オプションを追加します。[Profile edit warnings](https://github.com/marmot-protocol/whitenoise/pull/927)は、プロフィール変更時に警告を出します。バックエンド側では、[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs/pull/422)がAccountGroup作成時のレースコンディションを修正しています。

### npub.cash (Lightning Address Service)

[v3 rewrite](https://github.com/cashubtc/npubcash-server/pull/40)は、モノレポとサーバーをBunへ移行し、SQLiteサポートを追加し、v1互換を削除し、LUD-21を実装し、mint quoteのリアルタイム更新を加えます。

### nostr-java (Library)

[v1.1.1](https://github.com/tcheeric/nostr-java/releases/tag/v1.1.1)は、[2件のPR](https://github.com/tcheeric/nostr-java/pull/499)にまたがるWebSocket処理のリファクタリングと、より堅牢なテストを出荷しました。

### NIPs Repository

[NIP-54 Djot migration](https://github.com/nostr-protocol/nips/pull/2180)は、wiki仕様に対する別の変更提案です。コンテンツ形式をAsciidocからDjotへ切り替え、より簡潔な構文を持つ軽量マークアップへ移行します。このPRはwikilink向けに参照スタイルリンクを導入し、wiki記事間の相互参照をソース上で読みやすくします。[NIP-XX Quorum](https://github.com/nostr-protocol/nips/pull/2179)は、FROST（Flexible Round-Optimized Schnorr Threshold signatures）を用いたNostrグループ向けの閾値マルチシグガバナンスを提案します。QuorumはT-of-N方式でメンバー間に共有されるnsecであり、メンバー自身が参加することも、代表者の評議会へ委任することもできます。評議会が変わると古いnsecは無効になり、新しいnsecが配布されます。つまり、あらゆる評議会の最後の行為は、そのガバナンス移行イベントへ署名することです。仕様は、メンバーシップ（公開または非公開）、選挙や投票（一般投票、不信任投票）、任意の自然言語「laws」、さらにquorumが別のquorumのメンバーにもなれるquorum ontologyを定義します。これにより、地域団体が上位地域団体へ参加するような階層構造が可能になります。用途は、ソースコード開発、企業の取締役会、HOA、モデレーション付きコミュニティまで広がります。

---

今週は以上です。そして今年もここまでです。何か作っているものがありますか。共有したいニュースはありますか。取り上げてほしいプロジェクトはありますか。<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">NIP-17 DMでご連絡</a>いただくか、Nostr上で見つけてください。
