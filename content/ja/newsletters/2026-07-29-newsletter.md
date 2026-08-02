---
title: "Nostr Compass #33"
date: 2026-07-29
publishDate: 2026-07-29
translationOf: /en/newsletters/2026-07-29-newsletter.md
translationDate: 2026-08-02
draft: false
type: newsletters
description: "Amethyst 1.13.1 は、1.13.0 で Nostr アプリを導入した後、認証付きのグループおよび Blossom アクセスを追加。Mosaico はコーディングエージェントの状態を Nostr 上で共有し、Nostrology は NIP-65 relay リストの集中度を可視化。"
---

毎週お届けする Nostr のガイド、[Nostr Compass](https://github.com/andotherstuff/nostr-compass) へようこそ。

**今週：** [Amethyst 1.13.1](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.1) は、バージョン 1.13.0 で Nostr アプリを導入した後、NIP-29 のホスト relay 認証と、認証付き Blossom ダウンロードの再試行を追加しました。[Code Call](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.68) は携帯電話からリモートのコーディングセッションを進められるようにし、[GitWorkshop](https://github.com/DanConwayDev/gitworkshop) はメンテナーとリポジトリ同期を調整し、[Mosaico](https://github.com/pablof7z/mosaico/releases/tag/v0.1.2) はコーディングエージェントに Nostr 上の共有認識レイヤーを提供します。[Nostrology](https://dev.nostrolo.gy/relays) は、プロフィールが公開済みの relay リスト内で読み取りと書き込みの役割をどう分けているかを可視化します。タグ付きリリースでは、[Mafrend](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.0)、[Hanami](https://github.com/Letdown2491/hanami-android/releases/tag/v0.1.0)、[Cordn](https://github.com/Cordn-msg/cordn-web/releases/tag/v0.2.1) の Android リリースが主な項目となり、[FIPS は OpenWrt アクセスレイヤーを追加](https://github.com/jmcorgan/fips/pull/126)し、[オープンな PR では FreeBSD への移植を提案](https://github.com/jmcorgan/fips/pull/129)しています。プロトコル関連では NIPs、BUDs、NAPs、Marmot、Gamma Markets、Concord、NWC を取り上げ、[Nostr の 6 年間の 7 月](https://github.com/nostr-protocol/nips/commits/master/)では、初期のドメイン検索から relay グループの状態に至るまで、7 月の変更をたどります。
## 主要ストーリー

### Amethyst 1.13.1 が Nostr アプリ導入に続き、認証付きのグループおよび Blossom アクセスを追加

Android およびマルチプラットフォーム向け Nostr クライアントとして 7 月 28 日に公開された [Amethyst 1.13.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.0) は、napplet と NIP-5A nsite を、鍵を持たない分離されたブラウザプロセス内で開きます。同意を条件とする `window.nostr` ブリッジは、アクティブなアカウントを通じて署名し、選択した機能を使用できます。サイト別およびアカウント別の権限画面では、ユーザーがそれらの許可を確認または取り消せます。お気に入りのアプリは、アカウント間で Cookie、ログイン状態、許可を共有することなく、下部バーに固定したままにできます。

同じ [1.13.0 リリース](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.0) は、Concord コミュニティ、NIP-29 relay グループ、Buzz グループチャット、Wiki ページ、RSS フィードに加え、Git リポジトリのツリー、issue、pull request を追加します。ユーザーは同じ Nostr アイデンティティのもとで、コード、コミュニティ、公開、ソーシャルの各ビューを行き来できます。

[バージョン 1.13.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.0) では、支払いとアイデンティティの機能も拡張されました。Amethyst は BOLT12 offer の作成と支払い、リモート署名者アカウントの自動起動、Blossom フォールバックサーバーの追加、バッジ、コミュニティ、relay グループ向け Web of Trust 制御の拡張に対応します。7 月 29 日の [1.13.1 フォローアップ](https://github.com/vitorpamplona/amethyst/releases/tag/v1.13.1) は、[CORD-02 解散シール](https://github.com/vitorpamplona/amethyst/pull/3767)、kind `9008` の[グループおよびチャンネル削除](https://github.com/vitorpamplona/amethyst/pull/3779)、[NIP-29 ホスト relay 認証](https://github.com/vitorpamplona/amethyst/pull/3788)、アクセス制限付き Blossom ダウンロード向けの認証付き [BUD-01 再試行](https://github.com/vitorpamplona/amethyst/pull/3789)を追加します。

### Code Call 0.2.68 が、0.2.66 のキャッチアップ導入に続き、ワーカーフォルダーブラウザを追加

コンピューター上のコーディングセッションを操作する Android リモートアプリ [Code Call 0.2.68](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.68) は、専用のワークスペース一覧を、ワーカーディレクトリを起点とするフォルダーブラウザに置き換えます。ユーザーは許可された入れ子のフォルダーに入り、OpenCode セッション用に 1 つを選び、親フォルダーへ戻れます。[バージョン 0.2.67](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.67) は、セッションの生成時にこのブラウザを開きます。

先行する [0.2.66 リリース](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.66) は、携帯電話から届いた最新メッセージ以降の状況を簡潔にまとめるよう、経路指定されたワーカーへ依頼できます。同じ週のほかのリリースは、[複数のセッションを独立した状態に保ち](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.51)、[想定した送信者](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.56)からの返信だけを受け入れ、バックグラウンド配信のために受信箱を[設定済みのすべてのワーカー relay](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.59)へ接続し続けます。要求と返信は [NIP-17（プライベートダイレクトメッセージ）](/ja/topics/nip-17/)を通じて送受信され、ローカルで暗号化された [Blossom](/ja/topics/blossom/) 添付ファイルは[復号後も元のファイル形式を維持します](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.55)。

### GitWorkshop がメンテナーを調整し、リポジトリ同期を独立させる

[GitWorkshop の 7 月 27 日付署名済みリリース](https://primal.net/e/869e01f9a74d98f468a66f3b83865d198a82cc718c1db36324398b1b88a17c60)は、[NIP-55（Android 署名者アプリケーション）](/ja/topics/nip-55/)を利用する Android ログインを、ブラウザベースの [NIP-34（`git` 関連）](/ja/topics/nip-34/) forge に追加します。[ソースリポジトリ](https://github.com/DanConwayDev/gitworkshop)では、主担当メンテナーを再帰的に調整し、各メンテナーの relay ヒントを保持し、招待の承認からリポジトリ同期を独立させるようになりました。リポジトリをまたぐ作業項目の参照は、関連する作業をリポジトリ間で結びます。GRASP は、転送を招待配信と結合せずに、選択した Git エンドポイントへリポジトリデータをコピーします。開発者が署名した [3.1.1 アップデート](https://primal.net/e/01d0939e9960cb82f1f7aba6f1900af2c61ce384e38352221bf9d5878116ae2d)は、Android 署名者の intent 配信、再帰的なメンテナー解決、パスを保持するリポジトリリンクを修復します。

### Mosaico 0.1.2 がコーディングエージェント間の Nostr 経由の状態共有を可能に

[Mosaico 0.1.2](https://github.com/pablof7z/mosaico/releases/tag/v0.1.2) は、Claude Code、Codex、Goose、Hermes、OpenCode、Grok のコーディングエージェントセッションが、[NIP-29（Relay ベースのグループ）](/ja/topics/nip-29/)を介して短い状態更新を公開できるようにします。セッションは、トランスクリプトやコンテキストを共有せずに、ホストをまたいで関連する進行中の作業を見つけられます。

名前付き Codex プロフィールの検出と Goose の Top Of Mind ビューにより、両方の実行環境内で共有状態を確認できます（[PR #618](https://github.com/pablof7z/mosaico/pull/618)、[PR #619](https://github.com/pablof7z/mosaico/pull/619)）。このリリースは、ホスト型エージェントが公開の認識レイヤーへ参加する機能を復元し、セットアップでは明示的な relay 選択が必須になりました（[PR #626](https://github.com/pablof7z/mosaico/pull/626)、[PR #629](https://github.com/pablof7z/mosaico/pull/629)）。Mosaico は認識レイヤーであり、エージェントのホスト、オーケストレーター、トランスクリプト統合機能ではありません。

### Nostrology が公開済み NIP-65 event から relay リストの集中度を可視化

[Nostrology の relay 観測ページ](https://dev.nostrolo.gy/relays)は、各プロフィールの最新の [NIP-65（Relay リストメタデータ）](/ja/topics/nip-65/) kind `10002` event から、[公開済み仕様](https://github.com/nostr-protocol/nips/blob/master/65.md)に従ってデータセットを構築します。読み取り、書き込み、兼用の relay 役割を分け、各プロフィールが掲載する relay 数をグラフ化し、基礎となる件数を並べ替え可能な表で公開します。7 月 29 日の公開レビュー時点で、このページには 34,430 個の異なる relay URL 値があり、relay を 1 個だけ掲載したプロフィールは 520,468 件、3 個は 150,657 件、4 個は 60,710 件でした。

同じ [Nostrology のスナップショット](https://dev.nostrolo.gy/relays)では、`relay.momostr.pink` が 298,859 プロフィール、`relay.damus.io` が 287,181、`nos.lol` が 279,468、`relay.primal.net` が 225,336 と、重複を含む集中が見られます。これらの件数は公開済みの relay リスト項目を測定するもので、可用性を示すものではありません。生の表には不正な URL やローカルアドレスが含まれる場合があり、[NIP-65 仕様](https://github.com/nostr-protocol/nips/blob/master/65.md)は経路指定メタデータを定義しますが、relay の稼働状態は検査しません。この観測ページは、掲載された relay を稼働中と見なさずに、採用状況とデータ品質の問題を可視化します。

## タグ付きリリース

### Kairos 0.1.1 がリマインダーとローカルの Astraea 指示を追加

[Kairos 0.1.1](https://primal.net/e/ffb054280008dc3ba488d5d3a2cbfec6c4123489a874683545a29a466682fd90) は期限リマインダー、Astraea への明示的なローカル指示、より厳格な relay および URL 処理を追加します。[0.1.0 署名済みリリース](https://primal.net/e/6e02430844abdabf5421bbf5745a09ef2870e4ade93f56627ee14ba8db58a00a)では、[オフライン優先のタスク管理ツール](https://github.com/Lwb89dev/kairos)が導入されました。その任意の同期レイヤーは、[NIP-44（暗号化ペイロード）](/ja/topics/nip-44/)で暗号化したレコードを、ユーザーが選択した relay に書き込みます。Kairos は決定論的なタスク座標と暗号化された tombstone を、[NIP-09（Event 削除要求）](/ja/topics/nip-09/)の削除要求とともに使用します。ローカル専用タスクは端末の外へ出ません。

### Bray 2.3.0 が CLI に汎用 gift wrap とローカル Blossom テスト環境を追加

Nostr SDK およびコマンドラインツールキットの [Bray 2.3.0](https://github.com/forgesworn/bray/releases/tag/v2.3.0) は、[NIP-59（Gift Wrap）](/ja/topics/nip-59/)を介して任意の event を gift wrap および unwrap できます。bunker が鍵を保持する場合、署名は [NIP-46（Nostr Connect）](/ja/topics/nip-46/)を介して処理されます。[PR #75](https://github.com/forgesworn/bray/pull/75) は、同梱のテスト relay に [NIP-42（Relay に対するクライアント認証）](/ja/topics/nip-42/)の challenge を追加し、残りの Blossom クライアントコマンドを公開します。[PR #77](https://github.com/forgesworn/bray/pull/77) は、署名済み認可によって各アップロードまたは削除を 1 つの blob に結び付ける、メモリ内の BUD-01/02 サーバーを追加します。[PR #76](https://github.com/forgesworn/bray/pull/76) は、名前付き event kind、短縮 tag、呼び出し元がすでに保持する event のダウンロードを避ける [NIP-77](/ja/topics/nip-77/) ID 照合フラグを追加します。

### Buzz Desktop 0.5.0 が招待、検索、relay アイデンティティ更新を強化

先週の Armada と Buzz ワークスペースに関する記事に続き、[Buzz Desktop 0.5.0](https://github.com/block/buzz/releases/tag/v0.5.0) は利用回数に上限がある招待リンク（[PR #3141](https://github.com/block/buzz/pull/3141)）と、作成者、チャンネル、期間の検索フィルター（[PR #2871](https://github.com/block/buzz/pull/2871)）を追加します。[PR #2862](https://github.com/block/buzz/pull/2862) はデスクトップアプリのネイティブネットワークレイヤーを通じて参加ポリシーを取得し、[PR #2607](https://github.com/block/buzz/pull/2607) は persona 名の変更が relay に届いた後、エージェントのアイデンティティレコードを再公開します。このリリースは、[NIP-44 リモートサービス拒否アドバイザリー](https://github.com/block/buzz/pull/3135)に対応して Nostr の依存関係も更新し、ローカルストレージの復旧、スレッド位置、relay 再接続、Linux および Windows の実行時パスを修復します。

### Shosho 1.0.0 がライブ配信マーケットプレイスを拡張

[Shosho 1.0.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.0.0) は、設定可能な relay 検索を通じてユーザーが見つけられるクリエイター、ライブセッション、クリップ、商品を中心に、ライブ配信マーケットプレイスを再設計します。統合通知フィードは、メンション、リアクション、リポスト、zap をまとめ、フィードから離れずに返信できるようになりました。視聴者はライブ配信またはリプレイからクリップを公開できます。このリリースは、スレッド形式のチャット、クリップへの返信、プロフィール読み込み、ネットワーク使用量も改善します。

### Mafrend v1.0 が場所を基盤とする Android 向け Nostr チャットを初公開

[Mafrend v1.0](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.0) は、場所を基盤とする Nostr チャットアプリとして計画されている製品の、初の公開 Android アルファ版です。[プロジェクトページ](https://mafrend.com)は、機能群が現在も開発中であると明記し、地図上の各場所を、その場所に関する会話専用のチャットルームとして説明しています。公開リリース用リポジトリではインストール可能な Zapstore パッケージを配布し、メインアプリは非公開のままです。

### Hanami 0.1.0 が Blossom サーバーに署名者仲介型の Android 経路を提供

[Hanami 0.1.0](https://github.com/Letdown2491/hanami-android/releases/tag/v0.1.0) は、[Blossom](/ja/topics/blossom/) サーバー用の Android コンパニオンで、携帯電話からのサインイン、アップロード、ダウンロードを可能にします。このアプリは、承認を介した署名に [NIP-55（Android 署名者アプリケーション）](/ja/topics/nip-55/)を使用し、サーバーセッションにネイティブの [NIP-98（HTTP 認証）](/ja/topics/nip-98/)ハンドシェイクを使用します。Hanami はウェブシェルと署名ブリッジを選択したサーバーの origin に限定し、認証情報を署名者側に保持する一方で、サーバーの既存ウェブインターフェースがアプリケーション体験を提供します。最初の公開リリースには Android 8 以降、到達可能な Hanami サーバー、互換性のある署名者アプリが必要です。

### Cordn が Nostr アイデンティティによるグループチャットを Android で公開

プライベートグループメッセージングクライアントの Cordn は、Android ユーザー向けに Nostr アイデンティティのオンボーディング、[NIP-05（Nostr 鍵と DNS ベースのインターネット識別子の対応付け）](/ja/topics/nip-05/)を介したプロフィールリンク、Cordn 内の宛先をアプリで開く検証済みリンクを提供するようになりました。[7 月 24 日公開の 0.2.1 リリース](https://github.com/Cordn-msg/cordn-web/releases/tag/v0.2.1)は、既存のウェブクライアントに加えてこのネイティブ版を導入します。メッセージはグループ暗号化プロトコルの [MLS](/ja/topics/mls/)を使用し、コーディネーターが配信を支援します。そのため、メールアドレスや電話番号を必要とせずに、グループは順序付けられた暗号化会話を維持できます。

### Nostur 1.30.1 がスレッドと重複投稿を修正、1.30.0 では共有機能を拡張

iPhone、iPad、Mac 向け Nostr クライアントの [Nostur 1.30.1](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.30.1) は、新しいレイアウトを妨げていた展開と折りたたみの不具合を解消し、入れ子になった返信スレッドをたどれるようにします。メディアアップロードのコールバックが繰り返された場合を含め、同じ下書きが 2 回公開されることも防ぎます。このリリースは、消えるダイレクトメッセージと、メディアを Nostr へ送るための共有シート経路を追加した [1.30.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/1.30.0) に続くものです。これにより、新しいメッセージングおよび公開経路に、日常的なスレッド閲覧と投稿フローの修正が加わりました。

### Formstr Drive 0.0.2 が Nostr ファイルメタデータと Blossom blob を組み合わせる

Nostr ネイティブのファイル管理ツール [Formstr Drive 0.0.2](https://github.com/formstr-hq/formstr-drive/releases/tag/v0.0.2) は、アプリ内プレビューと、オフィス文書を Nostr Docs で開く選択肢をユーザーに提供します。内部では、大きなファイルを分割した [Blossom](/ja/topics/blossom/) blob として保存し、ユーザーがファイルを削除するとリモートの blob も削除します。ローカル relay はアプリの Nostr メタデータを手元に保持し、Blossom はファイルデータを保持します。これにより、ファイルの整理と大容量のバイト列を分離します。

### NoorNote 1.3.1

ウェブ、デスクトップ、Android 向け Nostr クライアントの [NoorNote 1.3.1](https://github.com/77elements/noornote/releases/tag/v1.3.1) は、消えるメッセージのタイマーを追加し、新規作成アカウント向けに動作する既定の DM relay を設定します。カバー画像のないグローバル記事を除外し、リポスト通知を記事リーダーへ送ります。先行する [1.3.0 リリース](https://github.com/77elements/noornote/releases/tag/v1.3.0) は、[NIP-53（ライブアクティビティ）](/ja/topics/nip-53/)カード、[NIP-68（画像を中心にしたフィード）](/ja/topics/nip-68/)の人物 tag、[NIP-78（アプリケーションデータ）](/ja/topics/nip-78/)のソフトミュート、ノートが relay で確認された状態の表示を追加しました。

### algia 0.0.133

Nostr 向け Go コマンドラインクライアントの [algia 0.0.133](https://github.com/mattn/algia/releases/tag/v0.0.133) は、[0.0.132](https://github.com/mattn/algia/releases/tag/v0.0.132) に続くリリースです。0.0.132 は、[NIP-29（Relay ベースのグループ）](/ja/topics/nip-29/)の一覧表示、タイムライン、投稿、リアクション、削除、参加、退出の各フローを追加しました。同じリリースは、認証を必須に設定した relay 向けに [NIP-42（Relay に対するクライアント認証）](/ja/topics/nip-42/)の事前認証も追加しました。続くバージョン 0.0.133 は、通常、チャンネル、グループの各投稿コマンドにローカル画像のアップロードを追加し、生成された URL と [NIP-92（メディア添付）](/ja/topics/nip-92/) tag を各 event に添付します。画像だけの投稿にも対応し、グループ投稿は既定でグループの relay メディアストアを使用し、それ以外の投稿は設定済みのファイルサーバーを使用します。

### swift-nostr 0.7.0

Apple プラットフォーム向けの Nostr ライブラリ [swift-nostr 0.7.0](https://github.com/yysskk/swift-nostr/releases/tag/0.7.0) は、Swift アプリケーションで 1 つの [NIP-46 リモート署名者](/ja/topics/nip-46/)から署名抽象化を通じてすべてのクライアント機能を動かせるようにします。このリリースは、グループへの参加、投稿、モデレーションの各フローを含む [NIP-98（HTTP 認証）](/ja/topics/nip-98/)および [NIP-29（Relay ベースのグループ）](/ja/topics/nip-29/)のサポートを追加します。[NIP-44（暗号化ペイロード、バージョン付き）](/ja/topics/nip-44/)のパディングも公式ベクトルに照らして検証し、非標準のパディングに対して有効な MAC を持つペイロードを拒否します。

### lawallet-nwc 2.0.0

[LaWallet NWC 2.0.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.0.0) は、Nostr 接続型ウォレットおよび [NIP-47（Nostr Wallet Connect）](/ja/topics/nip-47/)サービスで、WebAuthn PRF 拡張を使ってブラウザ内で Nostr 署名鍵を導出するパスキーログインを追加します。サーバーはその秘密を受け取らず、同じパスキーを使えば別の同期済み端末で同じ鍵を復元できます。アカウントは複数の Nostr pubkey をリンクして統合できるようになりました。任意のリスナーサービスはウォレット接続 event を中継し、エンドポイントへ到達できない場合に webhook 配信を再試行します。

### MDK 0.9.10

[MDK 0.9.10](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.10) は、[Marmot プロトコル](/ja/topics/marmot/)の Rust 実装で、トランスポートが停止中でも保留中の送信を保持し、[relay 通知の転送を監督](https://github.com/marmot-protocol/mdk/pull/1157)して、遅延、panic、終了後に受信配信を復旧させます。[PR #1159](https://github.com/marmot-protocol/mdk/pull/1159) は、永続的でページ分割された会話履歴と、ローカルエージェント向けの完全な返信コンテキストを追加します。[PR #1167](https://github.com/marmot-protocol/mdk/pull/1167) は、代替を生成せず、現在の署名済み KeyPackage event を再公開します。このリリースは、手動のチャット順序を保持し、終端的なグループ解散に対応し、Web of Trust 順位付き検索、relay ポリシー API、言語バインディングも拡張します。

### pakstr 0.3.1

[pakstr 0.3.1](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.3.1) は、Nostr クライアントを Android 向けにパッケージ化するウェブ開発チームが、アプリシェルを再ビルドせずに実行時設定と API プロキシを提供できるようにします。[同日公開のリリース群](https://git.nostrdev.com/stuff/pakstr/releases)は、0.3.x の実行時設定対応に先立って、Amber 署名者ブリッジ、[NIP-44（暗号化ペイロード）](/ja/topics/nip-44/)の暗号化と復号、Android 権限挿入の修正を追加しました。この雛形はバンドル済みウェブアセットをローカルに保持し、配備固有の設定を実行時に受け取ります。プロキシは、通常の relay 接続に加え、ラップされたアプリに API 要求用の制御された経路を提供します。

### Ditto 2.34.2

カスタマイズ可能な Nostr ソーシャルクライアント [Ditto 2.34.2](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.34.2) は、カスタム絵文字、有効期限、任意のリンクプレビューを含むユーザーステータスを、フィード、詳細ページ、引用埋め込み内のカードとして表示します。コメント付き zap は、参照先の投稿の下に返信として表示されるようになりました。このリリースは、[2.34.1 の任意のプロフィール地球儀ボタン](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.34.1)も維持します。このボタンは [NIP-5A（ウェブサイトマニフェスト）](/ja/topics/nip-5a/)のルートサイトを公開する所有者向けです。さらに、ホームページのナビゲーション、ライブ配信検索、外部リンク処理、壊れたカスタム絵文字を修正します。

### Earthly 0.0.9

Nostr 上に構築された共同地図編集ツール [Earthly 0.0.9](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.0.9) は、地図エンティティのドロワーを閉じた後、再び開いた後、または更新した後も、「いいね」を表示したままにします。[NIP-57（Lightning zap）](/ja/topics/nip-57/)のフローは、有効な zap 要求 JSON を送信します。これにより、Lightning プロバイダーは、ローカル開発中も含め、公開到達可能な relay に検証済みの受領 event を公開できます。生成した invoice はエンティティ画面の切り替え後も表示され、検証済みの受領 event が届くとアプリが確認を表示します。

## 開発中

### Keep が event kind 単位の NIP-44 v3 署名を追加し、承認ポリシーを厳格化

Keep は、[NIP-44（暗号化ペイロード）](/ja/topics/nip-44/)v3 の暗号化および復号要求を、2 種類の [NIP-55（Android 署名者アプリケーション）](/ja/topics/nip-55/)トランスポートと [NIP-46（Nostr Connect）](/ja/topics/nip-46/)bunker の両方で扱う、5 件の Android 署名者変更をマージしました。[PR #451](https://github.com/privkeyio/keep-android/pull/451)、[#452](https://github.com/privkeyio/keep-android/pull/452)、[#453](https://github.com/privkeyio/keep-android/pull/453) は、v3 の許可を v2 から分離し、event kind ごとに範囲を限定し、kind がない場合や無効な場合は拒否し、通知から開いた承認要求を保持します。[PR #454](https://github.com/privkeyio/keep-android/pull/454) と [#455](https://github.com/privkeyio/keep-android/pull/455) は、Basic 署名ポリシーを Auto として扱うことをやめ、全体設定をコア所有の暗号化ストアへ移します。Keep のメンテナーは、最新のタグ付き Android リリース後に 5 件すべてをマージしました。

### Routstrd が未認証アクセスの露出を受け、既定のネットワーク bind を変更

Routstrd の [PR #56](https://github.com/Routstr/routstrd/pull/56) は、ローカル Nostr 推論ルーターの既定 bind アドレスを、すべてのネットワークインターフェースから `127.0.0.1` へ変更します。以前の既定値では、そのポートへ到達できる任意のホストに対して、未認証のウォレット残高、履歴、アクセス、送信、返金、API キー、プロバイダー、クライアント、使用量、デーモン停止の各エンドポイントを公開していました。運用者はローカル以外の bind を明示的に設定できますが、マージ済みの変更により、新規配備は既定でローカル限定になります。この変更はまだタグ付きリリースに含まれていません。

### Imwald Android がオフライン公開の状態を明確化

Android 向け Nostr クライアントの Imwald Android は、設定済みの対象がすべてローカルの場合に限り、ローカル relay からの確認応答を公開完了として扱うようになりました。[オフライン公開および outbox の修正](https://git.imwald.eu/silberengel/imwald-android/commit/f4de9f61df35110c77d2e5f99d764c0df176962b)では、ローカル relay が event を受け入れても、設定済みのリモート relay が受け入れていない場合は、リモート配信を保留中のままにします。そのため、公開レポートは端末内のローカル保存と relay への配信を区別します。

### FIPS が OpenWrt アクセスレイヤーを追加、FreeBSD への移植は引き続きレビュー中

Nostr ネイティブの Free Internetworking Peering System は、[マージ済み PR #126](https://github.com/jmcorgan/fips/pull/126)により、OpenWrt ルーターからオープンな `!FIPS` アクセスネットワークを公開できるようになりました。並行して進む、まだオープンな [FreeBSD PR #129](https://github.com/jmcorgan/fips/pull/129) は、デーモン、TUN データパス、`.fips` 名前解決、サービス管理、ネイティブパッケージのビルドを移植する提案です。OpenWrt のマージにより現在のアクセス範囲が広がり、FreeBSD の作業が完了すれば、別の汎用オペレーティングシステムにも拡張されます。

7 月 26 日の [FIPS プロジェクト更新](https://primal.net/e/d0afe733f75e909341ab7f39834883968df097472238a474df3a3346c5d38f51)は、公開 UDP オーバーレイに 300 を超えるノード、より広いメッシュに 2,000 近いノードがあると報告しました。[FIPS リポジトリ](https://github.com/jmcorgan/fips)は同じ週に、並行ネットワークテスト、鍵更新の継続性、hop limit の挙動、ファイアウォール検査、NAT ラボの分離を強化しました。リポジトリ内の作業により、ネットワークの成長に合わせて、運用者がこれらの挙動を再現可能な方法で検査できます。

### Zap Cooking が投稿を予約し、スキャナー要求を署名へ結び付ける

Nostr のレシピ共有および献立計画アプリ Zap Cooking は、予約投稿を暗号化ストレージに保持し、定期的な relay 巡回を通じて予定時刻に公開できるようになりました（[PR #566](https://github.com/zapcooking/frontend/pull/566)、[PR #569](https://github.com/zapcooking/frontend/pull/569)）。これにより、署名されていない投稿内容をスケジューラーのデータベースに露出させずに、予約公開を利用できます。

冷蔵庫スキャナーは [NIP-98](/ja/topics/nip-98/) HTTP 認証で要求本文そのものを認証するようになりました。そのため、会員資格の検査では、本文で指定された pubkey ではなく、スキャン要求に署名した鍵を使用します（[PR #599](https://github.com/zapcooking/frontend/pull/599)）。

### Citrine が Android 端末を管理可能な relay に変える

Android 上で動作する Nostr relay の Citrine は、保存済みの event を外部 relay へ送信できるようになり、運用者がローカル履歴を再配信する手段を提供します（[PR #179](https://github.com/greenart7c3/Citrine/pull/179)）。互換性のあるクライアントが relay を管理できるように、[NIP-86（Relay 管理 API）](/ja/topics/nip-86/)コマンドも追加します（[PR #150](https://github.com/greenart7c3/Citrine/pull/150)）。

グループ運用者は、[NIP-29](/ja/topics/nip-29/) relay ベースのグループを、[PR #178](https://github.com/greenart7c3/Citrine/pull/178) で Amber 署名を通じて管理できます。[PR #174](https://github.com/greenart7c3/Citrine/pull/174) は、再起動をまたいで Tor 経由の relay 設定とライフサイクル状態を一致させます。

### Wired がブラウザ内で完全な会話を復元

ブラウザベースの Nostr クライアント Wired は、固定された探索幅や結果件数の上限で止まらず、フィードのルート、返信、参照 event を最後までたどるようになりました（[PR #148](https://github.com/smolgrrr/Wired/pull/148)、[PR #147](https://github.com/smolgrrr/Wired/pull/147)、[PR #146](https://github.com/smolgrrr/Wired/pull/146)）。関連 event を relay から取得できる場合、ユーザーはより深いスレッドとフィードのコンテキストを復元できます。

ブラウザは参照 event の relay ヒントも保持し、まだ不足しているコンテキストだけに使用します。これにより、設定済み relay が保持していない会話も復元できます（[PR #145](https://github.com/smolgrrr/Wired/pull/145)、[PR #144](https://github.com/smolgrrr/Wired/pull/144)）。不完全な取得は完了済みのスナップショットと区別されるため、部分的な応答が以前のキャッシュ済みビューを上書きすることはありません。

## プロトコルと仕様の動向

### NIPs：NIP-34 のホスティング境界、グループ移行、3 件の進行中ドラフト

今週は 2 件の仕様変更がマージされました。[NIP-34 commit 6d2979b](https://github.com/nostr-protocol/nips/commit/6d2979b3f503a8539c983efbcdcf901bbcf9ed23) は `kind:1618` pull request の説明から GRASP のホスティング手順を削除し、ホスティングとフォールバックの挙動を event の契約外に置きます。[NIP-29 commit db5fe3d](https://github.com/nostr-protocol/nips/commit/db5fe3de8c5d1443b634c9bbf66ecb004f337057) は、relay グループのメタデータを別の relay へ移行する方法と、有効な移動と独立して存続する fork をクライアントが区別する方法を定義します。

[PR #2424](https://github.com/nostr-protocol/nips/pull/2424) は、相互の `kind:10045` 鍵セット宣言を提案します。この相互要件により、あるアイデンティティが別の鍵を一方的に関連付けることを防げます。[PR #2421](https://github.com/nostr-protocol/nips/pull/2421) は BOLT12 zap intent と支払者証明を提案します。クライアントは、受取人が運用する受領サーバーに依存せず、対象、金額、offer、決済済み支払いに照らしてそれらを検証できます。

[PR #2425](https://github.com/nostr-protocol/nips/pull/2425) は、NIP-B0 のブックマークが、ウェブ URL とともに `nostr:` のような HTTP 以外のスキームを保持できるようにする提案です。これにより、既存のウェブアドレスを含む同じ非公開または公開ブックマークリスト内で、Nostr ネイティブ識別子、支払い要求、その他のアプリケーションスキームをそのまま維持できます。

### Mill がクラウドアカウントによる鍵バックアップのドラフトを実装

Mill は[発表](https://primal.net/e/6362d9b00662fa64200530f8a29ae547521bac0a1e3c9379ef9086eac7d2030b)で、Google OIDC アカウント識別子と高エントロピーのパスフレーズを組み合わせて使い捨てのバックアップ鍵を導出する、実装済みの[クラウドアカウント鍵バックアップのドラフト](https://github.com/0ceanSlim/nostr-mill/blob/main/docs/nip-cloud-key-backup.md)を公開しました。その[参照実装](https://github.com/0ceanSlim/nostr-mill/blob/main/src/nipbackup.js)は、ユーザーの実際の鍵を [NIP-49（秘密鍵暗号化）](/ja/topics/nip-49/)の `ncryptsec` として暗号化し、設定済み relay 上の暫定的なパラメーター付き置換可能 kind `30049` event に保存します。プロジェクトは[バックアップフローを main にマージしました](https://github.com/0ceanSlim/nostr-mill/commit/eeb4b9114d02114b703a6823ad36ca8063b224da)が、v1.0.0 より後のリリースにはまだ含まれておらず、運用者が専用の `backupRelays` を指定しない限り、バックアップフローは無効のままです。バージョン付きの relay セットは暫定的なままで、ドラフトは、公開された暗号文に対してオフラインでパスフレーズを推測できる状態が続くと警告しています。この設計は、高エントロピーのパスフレーズに依存する実装済みの実験として扱う必要があります。

### BUDs：Blossom サーバーが未知のアップロードをバイト列から識別する可能性

[BUD-02 PR #110](https://github.com/hzrd149/blossom/pull/110) は、アップロード元が `Content-Type` を省略するか `application/octet-stream` を送る場合に、サーバー側で MIME を検出することを推奨する提案です。Blossom サーバーは、保守されているファイル形式ライブラリで先頭バイトを検査し、クライアントが指定した具体的な形式は保持し、検出に失敗した場合は汎用バイナリ形式へフォールバックします。これにより、すべてのアップロードでバイト判定を必須にせず、画像、音声、動画、エージェントが生成したファイルを表示可能な状態に保てます。

### NAPs：取得およびファイルシステムの契約が進展する中、番号付き系列を規約へ置き換え

[PR #87](https://github.com/napplet/naps/pull/87) は番号付きの napplet 間プロトコル系列を削除し、実行時機能を名前付き契約のもとに置きます。一方、アプリケーションメッセージは `napplet:<archetype>/<intent>` 形式の規約 URI に集約されます。マージ済みの[トピックアイデンティティ変更](https://github.com/napplet/naps/pull/89)は、問い合わせ文字列を含まない安定した規約パスを、メッセージごとのペイロードデータから分離します。[PR #90](https://github.com/napplet/naps/pull/90) は、その転置規則を検出およびハンドラーメタデータに適用します。

2 件の NAP ドラフトは、信頼されたシェルの境界を拡張します。[NAP-CAPTURE PR #94](https://github.com/napplet/naps/pull/94) は、マイクの同意、プラットフォーム権限、制限、保持、終了処理を実行環境内に置き、上限のあるメディア成果物をサンドボックス化された napplet へ返します。[NAP-FS PR #88](https://github.com/napplet/naps/pull/88) は、制限のないホストパスではなくポリシーに拘束されたハンドルを使う、これと対になる仮想ファイルシステムの提案です。

### Marmot：仕様がグループの終端状態を定義

[Marmot PR #409](https://github.com/marmot-protocol/marmot/pull/409) は、MLS 自体にグループ削除操作がないため、認証済みで不可逆な `Disbanded` 状態を追加します。権限を持つ管理者の commit により、グループは `Active` から移行し、古い branch、メッセージ、Welcome がグループを復活させることを防ぎ、既存グループが解散する前に明示的な互換経路を提供します。先行する[仕様 issue の一斉整理](https://github.com/marmot-protocol/marmot/pull/408)では、グループ状態の権限、収束、key package、確認応答、メディアルール、レジストリの文言、追跡中の 200 件の仕様 issue も整合させました。

### Gamma Markets：公開仕様に変更なし

[Gamma Markets 仕様リポジトリ](https://github.com/GammaMarkets/market-spec)では、7 月 21 日から 7 月 28 日まで、公開 commit や pull request の活動は記録されませんでした。公開済みの注文、決済、市場データの文書が引き続き現在の基準です。変更なしという項目も設けることで、毎週の仕様確認で Gamma を継続して扱います。

### Concord：1 つの plane 内で読み取り機能と書き込み機能を分割する可能性

[Concord PR #12](https://github.com/concord-protocol/concord/pull/12) は、すべての読者が書き込み権限を持つべきではない plane に関するオープンなドラフトです。Control Plane を読み取り stream と書き込み stream の個別機能へ移行させ、書き込み制限付きチャンネル、招待、鍵更新の範囲を概説します。ドラフトでは書き込み鍵が spam 防止ゲートとなり、署名済みの内部 actor と roster の検査が引き続き権限を担います。

### NWC：1 つのウォレットメソッドが BOLT11 と BOLT12 のいずれかを選択可能に

[NWC PR #2](https://github.com/nostr-wallet-connect/nwc/pull/2) は、BIP-321 支払い URI 向けの任意の `pay` および `receive` メソッドを提案します。ウォレットサービスは対応を告知し、URI から互換性のある BOLT11 invoice または BOLT12 offer を 1 つ選択し、支払い前に一致しない Bitcoin ネットワークを拒否し、使用した指示形式を報告できます。この提案は NWC コアの外に置かれるため、BIP-321 または BOLT12 に対応しないウォレットは実装する必要がありません。

## Nostr の 6 年間の 7 月

この 7 月の歴史では、読みやすい識別子、relay の絞り込み、移植可能なアプリケーションデータ、プライバシー、相互運用性という、Nostr が繰り返し向き合ってきた問題をたどります。6 年を通じて、各レイヤーは限定的な修正を共有インフラへと発展させてきました。名前はプロフィールに、フィルターはアプリケーションの契約に変わり、relay が運ぶ状態はノートからライブルームやグループへと広がっています。[最初の NIP-05 実装](https://github.com/nbd-wtf/nostr-tools/commit/1ce00bd3b6909f78f212a7a172cf845b55280599)から始まり、[今月のアドレス指定可能な検出機能のマージ](https://github.com/nostr-protocol/nips/commit/2f4b09335c54a993d483bc220195e3f4a33df1ec)で終えた後、それらのテーマを発展させた各年 7 月の変更を検討します。

### 2021 年 7 月

2021 年 7 月 19 日、[nostr-tools commit 1ce00bd](https://github.com/nbd-wtf/nostr-tools/commit/1ce00bd3b6909f78f212a7a172cf845b55280599) は `nip05.js` モジュールを追加し、パッケージをバージョン 0.5.0 に引き上げました。その `keyFromDomain` 関数は `_nostrkey.<domain>` に対する DNS TXT 要求を構築し、交代で使用する 8 つの DNS-over-HTTPS プロバイダーの 1 つへバイナリクエリを送信し、応答内の最初の鍵を返しました。これにより、ブラウザクライアントは DNS リゾルバーを運用せず、単一の固定プロバイダーにも依存せずに、人が管理するドメインを公開鍵へ変換できました。

この最初の方式は検索を実現しましたが、ドメイン内の名前には対応せず、信頼境界は DNS と選択したリゾルバーにありました。現在の [NIP-05 仕様](https://github.com/nostr-protocol/nips/blob/master/05.md)は検出先を `/.well-known/nostr.json` へ移し、ドメインがローカル名を pubkey に対応付け、relay ヒントを添付できるようにしました。2021 年のコードは、当時の設計上の要請を記録しています。公開鍵は移植可能でしたが、人々には読み取り、検証し、クライアント間で移動できる識別子が依然として必要でした。

### 2022 年 7 月

7 月 10 日、[NIP-12 commit 3771186](https://github.com/nostr-protocol/nips/commit/3771186c0351656a675576051b75d253f26c0f0b) は、汎用の relay クエリを 1 文字の tag に限定しました。この決定により、relay に任意のメタデータキーをすべて索引化させずに、`#r`、`#g`、`#t` などのフィルターを URL 参照、geohash、hashtag に利用できるようになりました。10 日後、最初の [NIP-20 ウェブコメントのドラフト](https://github.com/nostr-protocol/nips/commit/9f9a864ce1e1ebfdcfdd4835cd60807440f038e8)はこのクエリモデルを直接使用しました。kind `34` のコメントは正規化したウェブページ URL を `r` tag に持ち、サイトと独立したクライアントが relay から同じ議論を取得できるようにしました。

relay ポリシーとソーシャルな反応も続きました。元の [NIP-22 commit](https://github.com/nostr-protocol/nips/commit/f51ce9dc0efaf61f39a76e112c310a9f58af1c87)は、`created_at` timestamp が不自然に古い event を relay が拒否できるようにし、[commit 8bef0e9](https://github.com/nostr-protocol/nips/commit/8bef0e9d79ebb4b11f8fd2bea11dc8f1668bc9d0) は将来の timestamp を同じポリシーへ追加しました。7 月 30 日、[NIP-25 commit dcbd504](https://github.com/nostr-protocol/nips/commit/dcbd504639d20d1b0ae6bb837609710645781b88)は kind `7` のリアクションを定義し、対象を示す `e` および `p` tag を持たせました。次の commit は `-` を否定的なリアクションに割り当て、[commit 6903ff5](https://github.com/nostr-protocol/nips/commit/6903ff5b2c395a550a26069f6e2b5460ae1fdca6) は `+` を明示的な汎用「いいね」としました。これらの commit は、ドラフトを採用するクライアント向けに、relay による timestamp 拒否、tag による取得、ウェブコメント、リアクション tag を規定しました。

### 2023 年 7 月

2023 年 7 月には、短いノートを越える調整が進みました。[NIP-37 鍵紛失ドラフト](https://github.com/nostr-protocol/nips/commit/e057fa01ca3928a32bdc0e9a44c27f946f267041)は、結果を普遍的な鍵ローテーションとは明示的に呼ばず、不可逆な鍵の廃止、ソーシャルリカバリーの閾値、事前に確定した代替鍵を検討しました。5 日後、[NIP-53](https://github.com/nostr-protocol/nips/commit/141197c564d97073f0293e3b2f367f0b6b3619c2) は、アドレス指定可能な kind `30311` のライブアクティビティと kind `1311` のチャットメッセージを導入しました。これにより、配信、ステージ、ライブ配信ルームが、ホスト、参加者、状態、会話に関する共通 event モデルを得ました。

アプリケーションも仕事と商取引を告知し始めました。最初の [Data Vending Machine ドラフト](https://github.com/nostr-protocol/nips/commit/67e950a2009e81df1b8c91b0a2ade0596e83f168)は、文字起こし、要約、翻訳などのタスクについて、kind `68001` のジョブ要求、kind `68002` の結果、入札、期限、連鎖、競合プロバイダーを説明しました。7 月 13 日、[広告掲載ドラフト](https://github.com/nostr-protocol/nips/commit/451c06a3c572a13afe45c1d80616f8e6dd9bb1de)は、タイトル、要約、価格、場所、状態のメタデータを持つ、アドレス指定可能な kind `30402` の offer を追加しました。これらのドラフトは後に NIP-90 と NIP-99 になりましたが、7 月時点の形式ですでに、要求または掲載情報と、それを表示するサーバーを分離していました。

支払い経路も構成可能になりました。7 月 31 日の [NIP-57 zap 分割のマージ](https://github.com/nostr-protocol/nips/commit/5d63b1570c490007252b10e757f7f68ef1f4b717)は、単一の `zap` 宛先を、受取人の pubkey と relay ヒントからなる重み付きリストへ変更しました。クライアントは 1 回の zap を共同作業者間で分配し、一部に重みがある場合は重みのない受取人を除外し、支払い前に分割を表示できました。この変更は、重み付き zap 受取人と relay ヒントを表す署名済み event の形式を標準化し、互換性のあるクライアントが支払い前に分割を提示できるようにしました。

### 2024 年 7 月

7 月 4 日、[NIP-29 commit c60ca88](https://github.com/nostr-protocol/nips/commit/c60ca888efbdc9b8fa4bbfbace372409d0b2161a) は、グループを作成するための `kind:9007` relay モデレーション操作を追加しました。6 日後、[NIP-70](https://github.com/nostr-protocol/nips/commit/ae1906ec7943a6bd756f05d2cd2fb2a041398921) は保護された event を定義しました。`-` tag は、event の認証済み作成者からの公開だけを受け入れるよう relay に指示します。一方の変更は relay に明示的なグループ状態遷移を与え、もう一方は、それ自体は有効な署名済み event を第三者が relay へ再送することを作成者が防げるようにしました。

7 月 16 日、1 件の [Cashu 仕様 commit](https://github.com/nostr-protocol/nips/commit/506b38916ab67a37b2d98b46b62cf0c0c5fde5a4) が NIP-60 ウォレットと NIP-61 nutzap の両方を導入しました。NIP-60 はウォレットメタデータを kind `37375`、未使用 proof を暗号化された kind `7375` event、任意の取引履歴を kind `7376` に置きました。NIP-61 は、受取人の kind `10019` にある mint と relay の設定を、P2PK ロック付き kind `7337` nutzap と組み合わせました。ウォレット状態と bearer token は relay を通じて移動できるようになりましたが、引き換えは引き続き Cashu mint の proof と、二重請求を慎重に防ぐ処理に依存しました。

7 月後半の 2 件の編集は、決定論的な状態を厳密にしました。[NIP-01 commit 9c54549](https://github.com/nostr-protocol/nips/commit/9c54549f1842245b842d8a66f3bade744da24189) は、`created_at` timestamp が同じ場合、event ID を次の比較基準とするよう求めました。これにより、クライアントは同一の結果集合を同じ順序で並べられます。[NIP-09 削除のマージ](https://github.com/nostr-protocol/nips/commit/722ac7a58695a365be0dbb6eccb33ccd7890a8c7)は、kind `5` の要求が event ID またはアドレス指定可能な座標を対象にできることと、relay が削除すべき kind を示す `k` tag を含めるべきことを明確にしました。どちらの変更も、いずれも正しい 2 つの実装の間に相違が生じ得る範囲を狭めました。

### 2025 年 7 月

7 月 16 日、Ecash の検出に専用のソーシャルディレクトリが加わりました。[NIP-87 commit 1afb6da](https://github.com/nostr-protocol/nips/commit/1afb6da049e57dd628ef46a3b0f90300653a66ee)は、kind `38172` の Cashu mint レコード、kind `38173` の Fedimint レコード、それらのレコードを relay ヒント付きで参照できる kind `38000` の推薦を定義しました。ウォレットは mint へ接続する前に、信頼する作成者の推薦を問い合わせられるようになりました。一方、仕様は、絞り込まないグローバル検出がユーザーを悪意ある運用者へ誘導する可能性を警告しました。

1 週間後、あるドラフトが音声メッセージ向けの移植可能な Nostr event レコードを規定しました。最初の [NIP-A0 commit](https://github.com/nostr-protocol/nips/commit/e50f37a527ace39cc3057827d52295c6b6de1112)は、音声メッセージのルートに kind `1222`、返信に kind `1244` を割り当て、音声 URL とメディアメタデータを持たせました。7 月 27 日の[形式に関するフォローアップ](https://github.com/nostr-protocol/nips/commit/4984b057c20397eae919ee5e463bc8a5d3fb2dc0)は、Ogg コンテナ内の Opus を推奨し、圧縮波形を標準化しました。クライアントは、単一の録音機能、ホスト、波形表現について合意せずに、短い音声を交換できるようになりました。

続いて、プライベートメッセージングとウォレット接続は、既読追跡、暗号化方式の選択、支払い進捗のためのプロトコル状態を追加しました。[NIP-17 commit 3d76da3](https://github.com/nostr-protocol/nips/commit/3d76da368e157934e056d95b3b3d8d6eaa105b09)は、置換可能な kind `30016` レコードを定義しました。順序付けられた `seen` tag により、クライアントは既読メッセージと見落とした可能性のある欠落を区別できます。7 月 31 日、[NIP-47 暗号化ネゴシエーション](https://github.com/nostr-protocol/nips/commit/f30a43bd37e08516923b96dd0d860122c9ffe04e)により、ウォレットサービスは NIP-44 v2 または従来の NIP-04 を告知できるようになりました。一方、[取引状態の commit](https://github.com/nostr-protocol/nips/commit/0595d438aaa163dd33ed00748026698a411a0861)は `pending`、`settled`、`accepted`、`expired`、`failed` の各状態を追加しました。配信、暗号化、支払い進捗は、ローカルな推測ではなく明示的なプロトコルデータになりました。

### 2026 年 7 月

この 7 月は、通常のウェブアドレスを relay クエリへ結び付ける変更から始まりました。[アドレス指定可能な検出機能の commit 2f4b093](https://github.com/nostr-protocol/nips/commit/2f4b09335c54a993d483bc220195e3f4a33df1ec)は、Nostr フィルターと relay リストを応答に含む `/.well-known/nostr.json?ad=<path>` 検索を定義します。通常のブラウザは元の URL を HTML として開けます。一方、Nostr クライアントは、対応する `/.well-known/nostr.json?ad=<path>` エンドポイントへ問い合わせ、アドレスをグループ、nsite、フィード、event、その他のネイティブオブジェクトへ解決するフィルターと relay リストを取得できます。このパターンは、2021 年のドメインから鍵を得る問題を、より広いレイヤーで再検討します。1 つの人間が読める URL が、アイデンティティとクエリの両方を指せるようになりました。

続いて NIP-29 は、平面的な relay グループから構造化された空間へ発展しました。7 月 16 日の[サブグループ commit](https://github.com/nostr-protocol/nips/commit/223ddb3b0c282f2a133adb9f4a9c098a31b36937)は、親子関係と順序付きの子関係を追加しました。隣接する commit は、招待コードの suffix、banner、順序付き pin snapshot、アドレス指定可能な event の pin を追加しました。7 月 22 日、[移行と fork の明確化](https://github.com/nostr-protocol/nips/commit/db5fe3de8c5d1443b634c9bbf66ecb004f337057)は、メタデータによってグループを別の relay へ正当に移動できる条件と、稼働し続ける branch が独立した fork となる条件を定義しました。グループ識別子は単純なまま、階層、表示、relay の変更が明示的な状態になりました。

2 件の小規模な編集は、実装境界を明確にしました。[NIP-46 commit f0af204](https://github.com/nostr-protocol/nips/commit/f0af20484c5e0d12e2d1936f87c5a6681a08daff)は、未知または未対応のメソッドに対して、クライアントを無言でタイムアウトさせず、リモート署名者がエラーを返すよう求めます。[NIP-34 commit 6d2979b](https://github.com/nostr-protocol/nips/commit/6d2979b3f503a8539c983efbcdcf901bbcf9ed23) は、pull request event の説明から GRASP 固有のホスティング手順を削除します。一方は呼び出し元へ終端応答を返し、もう一方は移植可能な git event が 1 つのサーバープロトコルを暗黙に引き継ぐことを防ぎます。

---

プロジェクトやニュース項目を共有するには、[Nostr Compass プロジェクト](https://github.com/andotherstuff/nostr-compass)を通じて NIP-17 DM を送ってください。
