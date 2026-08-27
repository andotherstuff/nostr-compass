---
title: "Nostr Compass #30"
date: 2026-07-08
publishDate: 2026-07-08
translationOf: /en/newsletters/2026-07-08-newsletter.md
translationDate: 2026-08-27
draft: false
type: newsletters
description: "Marmot は採用された仕様をマークし、MDK は MarmotKit bindingと暗号化されたグループ avatarを使用して v0.9.0 から v0.9.3 をカットし、Mostro は NIP-44 に Transport v2 を出荷し、Bitchat は NIP-13 の作業証明とメッシュから Nostr へのゲートウェイを追加します。 rust-nostr は、ギフト ラップおよびプライベート DM builderに NIP-40 の有効期限を追加します。"
---

Nostr の週刊ガイド、Nostr Compass へようこそ。

**今週:** [Marmot 仕様は採用マーク](#marmot-marks-the-spec-adopted-and-mdk-cuts-v09x) 42 ファイルにわたり、暗号化されたグループ avatar、外部signerのサポート、MarmotKit MarmotKit を使用して、MDK が v0.9.0 から v0.9.3 をカットします。 Androidのビンディング。 [Mostro は Transport v2 を出荷](#mostro-v0180-and-mobile-v130-ship-transport-v2-on-nip-44) mostrod、v0.18.0、モバイル v1.3.0 の両方でスパム対策ゲートと共存ウィンドウを備えた NIP-44 ダイレクト メッセージ。 [Bitchat 1.6.0 は、NIP-13 プルーフ オブ ワークを追加](#bitchat-160-adds-nip-13-proof-of-work-and-an-opt-in-mesh-to-nostr-gateway) を geohash チャネル メッセージに追加し、1 台のオンライン電話で群衆全体をアップリンクできるオプトイン メッシュ to Nostr ゲートウェイ、プレキー バンドル、推移的検証、および作成者が管理する暗号化されたプライベート グループ。 [Amber](#amber-v623-scopes-profile-subscriptions-and-adds-a-tor-status-notification) は、アカウントごとにプロファイル subscriptionをスコープし、プロファイル metadataの前に NIP-65 relay リストを取得し、再起動アクションを伴うライブ Tor ステータス通知を追加します。 [rust-nostr](#rust-nostr-adds-nip-40-expiration-to-gift-wrap-and-private-dm-builders) は、ラップのランダム化されたtimestampにアンカーされた NIP-40 有効期限をギフト ラップおよび NIP-17 DM builderに追加します。 [Amethyst](#amethyst-spends-the-week-hardening-negentropy-sync-and-adding-nip-50-search) は、ネゲントロピー同期強化の 43 の PR、NIP-50 全文検索インフラストラクチャ、およびニッチ分野向けのeventの種類をマージします。 [Nostrord には v2.0.0 および v2.1.0 が同梱されています](#nostrord-v200-and-v210-fold-the-relay-pool-and-heal-zombie-websockets) は、折り畳まれたrelay プール、ゾンビ WebSocket 検出、およびフル ディスク ファースト キャッシュ シームを備えています。 [Ngit v2.6.2](#ngit-v262-stops-duplicate-pr-status-events-on-default-branch-push)、[Jumble v26.7.1](#jumble-v2671-makes-blossom-the-default-upload-service-in-a-dm-focused-cut)、 [Applesauce signer 6.2.2](#applesauce-signers-622-drops-an-nbunksec-dependency)、[Bray v1.33.0](#bray-v1330-cli-picks-up-a-bunker-profile-persona-and-tor-outbound)、[Deepmarks] 1.0.0](#deepmarks-100-hardens-the-nostr-bookmarking-surface)、[Bitcredit Core v0.5.13](#bitcredit-core-v0513-unencrypts-block-metadata-on-the-nostr-wire)、[Coop Mobile] v0.2.4](#coop-mobile-v023-and-v024)、[Granary v11.0](#granary-v110-adds-nip-71-video-event-support)、[Nostr-relay] v0.0.244](#nostr-relay-v00244-adds-a-firestore-backend)、[Manent v1.4.0](#manent-v140-fixes-nip-42-auth-and-adds-media-clipboard-flows)、[Routstrd] v0.3.7](#routstrd-v037-makes-the-nostr-event-store-the-persistent-source-of-truth)、[Nymchat 1.0.1](#nymchat-101-launches-as-a-progressive-web-app-on-nip-17)、および [21Meetup] 1.1.0](#21meetup-110-launches-nostr-signed-attendance-badges) も出荷され、[SafeBox はフェーズ 3 が実質的に完了したことをマーク](#safebox-publishes-a-phase-3-progress-report-and-a-freebsd-jail-runbook) とともに、FreeBSD ジェイル展開ランブックと電子譲渡可能な記録のための OpenETR のスピンオフ。 NIP リポジトリは [NIP-51 と NIP-37 の名前の配置](#merged-nip-51-and-nip-37-align-the-kind-10013-name) をマージし、次の 5 つの提案をオープンします: [NIP-AD Nostr Web アドレス](#open-nip-ad-nostr-web-addresses-via-well-known-lookup)、 [NIP-86 招待コードのクレーム管理](#open-nip-86-claim-management-for-invite-codes)、[HSL ロール カラー形式](#open-role-color-as-h-s-l-tuple)、[NIP-80 ハードウェア証明されたメディアの出所](#open-nip-80-ハードウェア証明されたメディアの出所)、および[NIP-01 でのページネーションの修正](#open-nip-01-pagination-hardening)。詳細には、[NIP-13 (proof-of-work)](#nip-deep-dive-nip-13-proof-of-work) および [NIP-40 (有効期限timestamp)](#nip-deep-dive-nip-40-expiration-timestamp) が含まれます。

---

## リードストーリー

### Marmot は採用された仕様をマークし、MDK は v0.9.x をカットします。

[Marmot protocol リポジトリ](https://github.com/marmot-protocol/marmot) は 7 月 3 日に [PR #170](https://github.com/marmot-protocol/marmot/pull/170) を統合し、42 個のファイルを `Status: draft for internal review` (および `experimental draft`) から `Status: adopted` に変更しました。 README タイトルは進行中の作業としてのリポジトリの枠組みから、採用されたテキストとしての「Marmot protocol」に移動し、MIP 時代のドキュメントはprotocolの非推奨バージョンとして再構築され、「レビュー ステータス」セクション (「これはまだ採用されていない仕様テキストです」) が現在の仕様を編集するための「レビュー ガイダンス」になりました。 `v2` ラベルは全体にわたって消えます。MIP コントラストの表現 (「v2 の新機能」、「v2 仕様は維持」) が「この仕様」および「この仕様の下」に置き換えられます。 2 つのドキュメントは仕様によりドラフト ステータスを維持します。`implementation-model.md` は非規範的なままであり、マルチデバイス機能自体のドキュメントはドラフトのままです。

同じリポジトリに、管理ポリシー、メンバーシップ、およびロール変更の不変条件を調整する [PR #171](https://github.com/marmot-protocol/marmot/pull/171) が追加されました。 Remove によって管理者が孤立できないかどうかのコンポーネント間チェックが、結果として生じるすべてのエポックのプロパティとして記述されるようになり、commitに管理ポリシーの更新が含まれていない場合、前のエポックの管理者セットに対して評価されます。 Convergence の候補branch ルールは厳格化されており、「検証」とはコンポーネント間の結果エポック チェックを含む完全なcommitの有効性を意味し、不変条件に違反するcommitがbranch上で候補エッジを作成することを防ぎます。置き換えられたcommit MUST から派生した状態通知は、branch選択によって置き換えられると取り消されます。これにより、仕様レベルでの「名前変更の喪失が成功したシステム メッセージとしてレンダリングされる」バグが解決されます。 `member-departure.md` の新しい「削除の実現」セクションでは、プライマリ実現入力 (最後のリーフを削除する受け入れられた正規commit) と、削除commitを適用しなかったclientのフォールバックが定義されます。認証されたエビクション後の証拠は、削除されたグループ コピーの非アクティブな保持セマンティクスを備えた `SelfEvicted` 結果として表示されるようになりました。 [PR #236](https://github.com/marmot-protocol/marmot/pull/236) その後、wire境界の検証を強化し、KeyPackage の有効期間の受け入れを 84 日間 + 1 時間のスキュー マージンに固定し、グループ `h`、gift wrap `p`、ウェルカム `e` および `relays`、KeyPackage tagの Nostr tag カーディナリティ テーブルを追加し、未検証の Nostr event ID とmetadataは信頼できないと述べました。ルーティング、リプレイ、またはテレメトリーの証拠。

ダウンストリームでは、[MDK workspace](https://github.com/marmot-protocol/mdk) が 7 月 6 日にworkspaceの完全バージョンアップで [v0.9.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.0) を削減し、その後 2 日間にわたって [v0.9.1](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.1)、[v0.9.2](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.2)、[v0.9.3](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.3) が続きました。 v0.9.0 は、新しい SQLite データベースが作成されるときに古いキーリング エントリをローテーションし、ストレージ レイヤー全体で変更前検証の規則を適用します。 v0.9.1 は、[PR #732](https://github.com/marmot-protocol/mdk/pull/732) を介して 1 つのホスト セーフティ ダイヤル チョークポイントを介してすべての発信接続をルーティングし、異なる呼び出しサイトが異なる検証でネットワークに到達するという一連のバグを解決します。 v0.9.3 は、[PR #771](https://github.com/marmot-protocol/mdk/pull/771) を介して `download_group_image` および `image_hash_hex` を介して暗号化されたグループ avatarを uniffi bindingに公開し、外部signerのサポートを追加し、[PR #781](https://github.com/marmot-protocol/mdk/pull/781) を介して `wn-opencode` を本番対応としてマークします。 MDK カットに加えて、MarmotKit は各バージョンで iOS および Android binding (MarmotKit.xcframework、iOS および Kotlin bindingの Swift binding、および Android の JNI ライブラリ、どちらも固定された MDK commitから生成) を同梱しています。hash）、新しい wn-agent リリース チャネルは、WN エージェントのバージョンを不変のリリース tagに固定するシェル インストーラーを提供するため、ダウンストリーム アプリは 1 つの `curl` コマンドで現在のエージェントをプルできます。

### Mostro v0.18.0 およびモバイル v1.3.0 は NIP-44 に Transport v2 を出荷します

Mostro は、暗号化された DMs を介してclientが通信するdaemon (`mostrod`) によって調整され、注文帳、エスクロー、Nostr event上の紛争解決を実行するピアツーピアのビットコイン取引protocolです。今週まで、clientと mostrod 間のワイヤ protocolは Transport v1 でした。 [Mostro v0.18.0](https://github.com/MostroP2P/mostro/releases/tag/v0.18.0) は Transport v2 を着陸させ、サーバー側で実行されるスパム対策ゲートとデュアル受信サポートを備えた [NIP-44](/ja/topics/nip-44/) ダイレクト メッセージにprotocolを接続します。 [PR #776](https://github.com/MostroP2P/mostro/pull/776) はフェーズ 1 のワイヤ変更であり、[PR #780](https://github.com/MostroP2P/mostro/pull/780) はprotocol v2 のフェーズ 2 スパム対策ゲートを追加し、[PR #785](https://github.com/MostroP2P/mostro/pull/785) は内部protocol バージョンをアクティブなトランスポートに従わせ、移行期間中に v2 clientと v1 clientが共存できるようにします。関連する [PR #782](https://github.com/MostroP2P/mostro/pull/782) は、`protocol_versions` の名前を単数形の `protocol_version` に変更することで、NIP-33 情報tagを修正します。このリリースでは、トランスポート作業と並行して、キャッシュと古さの強制を伴うフェーズ 4 の統合ライブクォート パス ([PR #783](https://github.com/MostroP2P/mostro/pull/783)) と、キューバの CUP と MLC ペアをカバーする El Toque 法定通貨クロス プロバイダー ([PR #778](https://github.com/MostroP2P/mostro/pull/778)) が導入されます。 [PR #779](https://github.com/MostroP2P/mostro/pull/779) 紛争スラッシュにスラッシュ パーティ通知を追加し、ボンドを失ったユーザーがdaemonから直接連絡を受けるようにします。以前の動作はウォレット残高の不足としてのみ表面化しました。

[Mostro Mobile v1.3.0](https://github.com/MostroP2P/mobile/releases/tag/v1.3.0) は、移行のclient側の半分です。 [PR #613](https://github.com/MostroP2P/mobile/pull/613) はアプリを Riverpod 3.x に移行します。フェーズ A ([PR #620](https://github.com/MostroP2P/mobile/pull/620)) は、メイン分離とバックグラウンド分離で NIP-44 ダイレクト メッセージのデュアル受信サポートを追加します。これにより、v2 mostrod と v1 clientが移行中に通信できるようになります。[PR のフェーズ B] #624](https://github.com/MostroP2P/mobile/pull/624) はデュアル送信を追加し、[PR #632](https://github.com/MostroP2P/mobile/pull/632) は Riverpod 3.x カット後にデュアル送信を再適用し、[PR #637](https://github.com/MostroP2P/mobile/pull/637) のフェーズ C で移行が完了します。このリリースでは、アフリカの支払い方法の対象範囲も追加されています。[PR #625](https://github.com/MostroP2P/mobile/pull/625) ではマラウイ クワチャの支払い方法が追加され、[PR #627](https://github.com/MostroP2P/mobile/pull/627)では KES (ケニア シリング)、MZN (モザンビーク メティカル)、TZS (タンザニア シリング)、UGX (ウガンダ シリング)、ZAR (南アフリカ ランド)、ZMW (ザンビア クワチャ) が追加されています。 NGN (ナイジェリア ナイラ) を拡大しながらの手法。復元フローは、復元リクエストを発行する前にノードの接続を待機するようになり、原因を認識した処理により、紛争によるボンド スラッシュとタイムアウトによるボンド スラッシュが区別されます。

### Bitchat 1.6.0 は、NIP-13 の作業証明とオプトインのメッシュから Nostr ゲートウェイを追加します

[Bitchat 1.6.0](https://github.com/permissionlesstech/bitchat/releases/tag/v1.6.0) は、geohash チャネルと DM ハンドオフに Nostr を使用する Bluetooth メッシュ チャット アプリです。このリリースには、読む価値のある 2 つの Nostr 形式の内容が記載されています。 [PR #1382](https://github.com/permissionlesstech/bitchat/pull/1382) [NIP-13 (proof-of-work)](/ja/topics/nip-13/) を送信ジオhash チャネル メッセージ (kind 20000 一時event) に追加します。各送信は公開前に `["nonce", "<value>", "<target>"]` tagをマイニングし、先頭の 8 ビットを対象とし、平均 256 回のhash試行が行われ、M-series Mac では 1 ミリ秒未満で完了します。検証済みの PoW を使用したインバウンド eventでは、送信者ごとの取り込みレート制限が緩和されるため、スパマーはメッセージごとにコンピューティング料金を支払いますが、通常の送信者はコストを感じません。スコープは意図的に狭くされています。kind 20000 チャネル メッセージのみが PoW をマイニングし、プレゼンス ハートビート (kind 20001)、kind-1 ロケーション ノート、および DMs は変更されません。

[PR #1384](https://github.com/permissionlesstech/bitchat/pull/1384) ゲートウェイ モード、ジオhash チャネル用のオプトイン メッシュから Nostr へのアップリンクを追加します。メッシュ専用ユーザー (インターネットなし、到達可能なrelayなし) が geohash チャネルで送信し、メッシュ上の別のピアが `.gateway` 機能をアドバタイズすると、署名された kind 20000 eventは新しい `MessageType.nostrCarrier = 0x28` TLV エンベロープでラップされ、1 つのゲートウェイに送信されます。ゲートウェイ ピアは、送信者に代わってeventを Nostr にパブリッシュし、デフォルトの TTL を使用して受信チャネル トラフィックをメッシュに再ブロードキャストします。アップリンク デポジットは、クーリエ エンベロープ パス (直接、中継されたマルチホップ) に乗ります。ダウンリンクライドブロードキャスト。署名はeventが送信者から送信される前に行われるため、ゲートウェイは公開するかどうかを決定できますが、帰属を偽造することはできません。述べられている動機は、群衆の中で 1 台の電話が接続されているだけで、Geohash チャネル全体に動作する Nostr アップリンクを提供できる災害や抗議活動のシナリオです。

同じリリースで、Nostr に隣接する作品の 2 番目のバッチが出荷されます。 [PR #1381](https://github.com/permissionlesstech/bitchat/pull/1381) は、宅配便メール パス上での前方秘密の非同期ファースト コンタクト用のプレキー バンドルを追加します。これにより、送信者は、最初にライブ Noise handshakeを実行しなくても、オフラインのピアへのメッセージを作成してメッシュに渡すことができます。 [PR #1380](https://github.com/permissionlesstech/bitchat/pull/1380) は推移的な検証を追加します。すでに検証した相手との Noise handshakeを完了したピアは、Noise セッション上で保証されるようになりました。そのため、新しい連絡先ごとに新たな対面検証を必要とするのではなく、信頼グラフは一度に 1 ホップずつ伝播します。 [PR #1383](https://github.com/permissionlesstech/bitchat/pull/1383) はメッシュ上に作成者管理の暗号化プライベート グループを追加し、[PR #1376](https://github.com/permissionlesstech/bitchat/pull/1376) は `/pay` コマンドで Cashu ecash トークンを検出、レンダリング、引き換え、そして [PR #1379](https://github.com/permissionlesstech/bitchat/pull/1379) はメッシュ同期上にレイヤー化された永続的な署名付き geohash 掲示板を追加します。 [PR #1372](https://github.com/permissionlesstech/bitchat/pull/1372) は、オープン クーリエ、スプレー アンド ウェイト ルーティング、永続的な送信トレイ、6 時間の公開履歴ウィンドウによりストア アンド フォワードを拡張します。 Bitchat 1.5.4 は、ピア リストの重複、Nostr 同期、および `/fav` キーの破損をクリーンアップする [PR #1367] (https://github.com/permissionlesstech/bitchat/pull/1367) のエンドツーエンドのお気に入りの修正とともに [週の初めに](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.4) 出荷されました。

---

## tag付きリリース

### Amber v6.2.3 はプロファイルのsubscriptionをスコープし、Tor ステータス通知を追加します

[Amber v6.2.3](https://github.com/greenart7c3/Amber/releases/tag/v6.2.3) は、Android [NIP-46](/ja/topics/nip-46/) signerに対するパフォーマンスと正確性のパスであり、その周囲の週にマージされた PR は一貫したテーマを示しています。このリリース自体は、[なし] および [常に] オプション ([PR #492](https://github.com/greenart7c3/Amber/pull/492)) を使用して構成可能なプロファイル取得間隔設定を追加し、アカウント切り替えの下部シートにプロファイル画像を表示し、現在のアカウントごとにプロファイル subscriptionの範囲を設定するため、複数のアカウントを持つsignerが、ユーザーが現在署名していないアカウントのsubscriptionをファンアウトするのを停止します。バンカー権限の解析では、解析失敗時の明示的なエラー処理が可能になります。いくつかの StrictMode 違反が修正されました。Coil の `onSuccess` ロギングによる DiskReadViolation、メイン スレッドでのアカウントのロードによるキーストア違反、アカウント スイッチ シートのアカウント名と画像のメイン スレッド読み取り、ログイン画面とサインアップ画面での熱心な `KeyPair()` 構築がメイン スレッドから移動されました。 v6.2.3 が出荷されてから数日で、[PR #493](https://github.com/greenart7c3/Amber/pull/493) は、プロファイル metadataの前にユーザーの [NIP-65](/ja/topics/nip-65/) relay リストをフェッチするようにブート パスを並べ替え (そのため、プロファイル フェッチはユーザーが公開するrelayをクエリします)、[PR #494](https://github.com/greenart7c3/Amber/pull/494) は組み込みの Tor 通知をライブ ステータスに変更しました。これにより、署名セッション中に Tor daemonが停止したユーザーは失敗を認識し、signerを離れることなくそれをバウンスできます。 [PR #495](https://github.com/greenart7c3/Amber/pull/495) コードベース全体で Android lint を厳密なエラーとして警告するモードが有効になりました。

### Jumble v26.7.1 は、Blossom を DM に焦点を当てたカットのデフォルトのアップロード サービスにします

[Jumble v26.7.1](https://github.com/CodyTseng/jumble/releases/tag/v26.7.1) は、ダイレクト メッセージとメディアに焦点を当てた Nostr Web client カットです。このリリースではメディア アップロード設定が再設計され、[Blossom](/ja/topics/blossom/) がデフォルトのアップロード サービスとなり、以前の NIP-96 のデフォルトが置き換えられました。 DM 処理では、モバイル メッセージ メニュー、改善されたデスクトップ メッセージ アクション、「最新にスクロール」ボタン、DM メディアの長押し反応、およびメッセージ リストからの失敗した送信 DMs の再試行パスを取得します。カスタム絵文字の編集は詳細ビューを獲得し、請求書と埋め込みコンテンツのメッセージ バブルのサイズが改善され、いくつかの DM スクロールとメッセージの順序付けの問題が修正され、絵文字の挿入、テキスト コピー、ファイルのドラッグに関するポストエディターの問題がクリーンアップされています。アップロード時にmetadataが削除されると画像の向きが修正され、Linux ARM64 ダウンロードがリリース マトリックスに追加されます。

### Applesauce signer 6.2.2 は nbunksec 依存関係を削除します

[applesauce-signers@6.2.2](https://github.com/hzrd149/applesauce/releases/tag/applesauce-signers%406.2.2) は、[commit d654349](https://github.com/hzrd149/applesauce/commit/d654349) を介して組み込みの [nbunksec](/ja/topics/nip-46/) ヘルパーを優先して、サブパッケージの `@sandwichfarm/encoded-entities` 依存関係を削除します。先週追加された Applesauce の [NIP-46](/ja/topics/nip-46/) バンカー セッション エンコーディングは、外部エンコーディング ライブラリを必要としなくなり、signerパッケージを消費する下流clientのサプライ チェーン サーフェイスが 1 つ削減されます。

### Ngit v2.6.2 は、デフォルト branch プッシュ時に重複する PR ステータス eventを停止します

[Ngit v2.6.2](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.6.2) は、git-over-Nostr CLI のバグ修正リリースです。デフォルト branchへの `git push` は、すでに適用済みとしてマークされている PR の重複 PR マージ/適用ステータス eventの発行を停止します。これは、マージ検出がプッシュ前の Nostr リポジトリ状態 (PR がワークフローの [NIP-34](/ja/topics/nip-34/) 側ですでに解決されているかどうかの信頼できる情報源) を読み取るためです。以前のヒューリスティックは git 内部に依存し、ステータス eventを複製しました。 git-over-Nostr プッシュ フローに ngit を使用するアクティブ リポジトリは、重複した kind-1621 ステータス eventをオーディエンスに送信しなくなります。

### Bray v1.33.0 CLI はバンカーのプロファイル、ペルソナ、および Tor アウトバウンドを取得します

[Bray v1.33.0](https://github.com/forgesworn/bray/releases/tag/v1.33.0) は、Nostr SDK プラス CLI リリースです。 `bunker --profile <name>` は自動安定接続キーとrelay フォールバックを取得するため、保存されたプロファイルはrelayの停止後も存続できます。 `bunker --persona <name>` は、派生 nsec ツリー ID として署名し、1 人のsignerが 1 つの派生ツリーからの複数の公開鍵として機能します。すべての HTTP フェッチは、構成時に Tor SOCKS プロキシ経由でルーティングできます。このリリースでは、[NIP-47](/ja/topics/nip-47/) NWC、[NIP-29](/ja/topics/nip-29/) グループ管理書き込み操作 (作成、更新、ユーザー追加、ユーザー削除、ロール設定)、NIP-86 管理動詞、および [NIP-65](/ja/topics/nip-65/) 送信ボックス ヘルパーのウォレット サブコマンドが追加されます。パブリッシュ動詞は、`--jsonl`、`--csv`、および `--tsv` 出力フラグ、汎用 NIP-01 filter クエリ用の `req` 動詞、任意のevent構築用の `event` 動詞、事前に構築されたeventに署名してブロードキャストする `publish-raw` コマンド、`bunker sign` ワンショットを取得します。 NIP-46 署名コマンド、およびすべての発行コマンドのコマンドごとの `--relay` フラグ。セキュリティ作業には、秘密のゼロ化規律、HTTP トランスポート ベアラー認証とレート制限の強化、relay URL の SSRF 検証という 3 つの監査延期のバッチが含まれます。 npm tarball は 533,844 バイトで出荷され、2 つの独立した CI ランナー間で検証されたバイト同一の再現可能なビルドが含まれます。

### Deepmarks 1.0.0 は Nostr ブックマークの表面を強化します

[Deepmarks 1.0.0](https://github.com/ostermayer/deepmarks-public/releases/tag/v1.0.0) は、パブリック Nostr ブックマーク サービスのセキュリティ強化 1.0 マイルストーンです。すべてのブックマークは署名された Nostr eventであり、どのclientでも読み取ることができます。 API とアーカイブ ワーカーは特権ネットワークの位置にあるため (内部 Redis、バンカーのrelay パス、クラウド metadataにアクセスできる)、SSRF ガードは負荷に耐え、リリースでは `isPrivateIp` の重要な IPv6 リテラル バイパスが修正されています。括弧で囲まれた IPv6 リテラルはパブリックとして分類されていました。 `[::1]`、`[fd00::1]`、および IPv4 にマップされた `[::ffff:10.0.0.4]` はすべて、デュアル スタック接続経由で内部ターゲットに到達しました。ガードは、両方のボックスのプライベート範囲チェックの前に、ブラケットを取り除き、IPv4 マップされた IPv4 互換の IPv6 を埋め込み v4 に折りたたむようになりました。外部relayから取り込まれた `kind:0` プロファイルは、シンクで署名検証されるようになりました。そのため、敵対的なrelayは、任意の被害者の公開鍵に対して `nip05` または `lud16` を偽造できません。また、ブックマーク URL はすべてのレンダー シンクでスキーム チェックされるため、`kind:39701` ブックマークは、`javascript:` または `data:` を使用してrelayに直接パブリッシュされます。 `d` tagが `<a href>` に到達しなくなります。 Zap の受信は一時的なバンカーの停止後も存続するようになりました。決済ハンドラーは保留中の ZAP をアトミックに要求し、署名が成功した場合にのみ終了し、失敗した場合は要求を解放して、再配信された `invoice_updated` が再試行できるようにします。 `/publish` ファンアウト ドレインは、ハートビート ゲート リカバリを備えたワーカーごとの処理リストに `BLMOVE` を使用するため、クラッシュしたワーカーはclientがすでに 202 されていた署名済みeventを保存します。

### Bitcredit Core v0.5.13 は Nostr wire上のブロック metadataを暗号化解除します

[Bitcredit Core v0.5.13](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.13) は、クレジット請求protocolで使用される Nostr パブリック eventから暗号化レイヤーを削除します。ブロックのmetadata (ブロック ID、hash、署名) は、Nostr wire上で暗号化されなくなりました。ブロック データ自体のみが、対応する請求書キーで暗号化されたままになります。新しいアプリは古いチェーンを処理しますが、古いアプリは新しいチェーンを処理しません。このリリースでは、請求書チェーンを取得するための請求書サービス機能も追加され、公開を楽観的しきい値モデルに切り替えます。設定されたrelayしきい値 (デフォルトのしきい値) が公開を受け入れると、残りのrelayがeventを非同期で受信するため、最も遅いrelayによって公開がブロックされなくなります。

### Coop Mobile v0.2.3 および v0.2.4

[Coop Mobile](https://git.reya.su/reya/coop-mobile) は 7 月 4 日に [v0.2.3](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.3) を出荷し、7 月 7 日に [v0.2.4](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.4) を出荷し、Android [NIP-17](/ja/topics/nip-17/) ダイレクト メッセージング clientの安定したリリース リズムを継続しました。 v0.2.3 は、チャット メッセージにインライン画像とリンクのレンダリング、画像の添付ファイル、音声テキスト入力、連絡先削除の確認ダイアログを追加します。 v0.2.4 は、永遠にスタックしていたインジケーターを修正し、Nostr Connect handshakeを改善し、再設計されたインポート ID 画面とともに `ncryptsec1` インポート ([NIP-49](/ja/topics/nip-49/) 暗号化秘密キー形式) を追加します。

### Granary v11.0 は、NIP-71 ビデオ eventのサポートを追加します

[Granary v11.0](https://github.com/snarfed/granary/releases/tag/v11.0) は、Bridgy Fed のクロスネットワーク ブリッジングを強化するマルチprotocol変換ライブラリです。 Nostr モジュールには 3 つの目に見える変更が加えられています。 [NIP-71](/ja/topics/nip-71/) ビデオ event (種類 21、22、34235、および 34236) は、ビデオ添付ファイルを含む ActivityStreams 1 ノートに変換されるようになり、コンバーターは `imeta` 画像 (サムネイル)、ビデオの長さ、トップレベルの `published_at` tag、およびフォールバックとして `alt` tagを抽出します。最初のビデオまたはオーディオ添付ファイルの `displayName`。 API 側では、`sign` の名前が `hash_and_sign` に変更され、`verify` は失敗時に `ValueError` を生成するようになりました。 `Nostr` コンストラクターは無効なrelay URL で `ValueError` を生成し、呼び出し元が `privkey` を設定していない場合、`Nostr.query` は [NIP-42](/ja/topics/nip-42/) AUTH チャレンジを正常にスキップします。フォローアップの変換修正により、`id` なしで Nostr `article` オブジェクトが到着した場合にクラッシュすることがなくなりました。 Granary を通じて NIP-71 ビデオ eventを消費するブリッジまたはリーダーは、ターゲット リーダーが予期する形式でeventを表示できるようになりました。

### Nostr-relay v0.0.244 は Firestore バックエンドを追加します

[mattn/nostr-relay v0.0.244](https://github.com/mattn/nostr-relay/releases/tag/v0.0.244) は、[PR #12](https://github.com/mattn/nostr-relay/pull/12) 経由で Firestore バックエンドを追加し、既存のバックエンドに加えて Google Cloud Firestore オプションを使用して Go relayのストレージ レイヤを拡張します。変更は小さいですが、中継オペレーターの管理対象サーバーレス データベース オプションとして Firestore が開かれます。

### Manent v1.4.0 は NIP-42 AUTH を修正し、メディア クリップボード フローを追加します

[Manent v1.4.0](https://github.com/dtonon/manent/releases/tag/v1.4.0) は、[NIP-44](/ja/topics/nip-44/) 暗号化、[NIP-46](/ja/topics/nip-46/) および [NIP-55](/ja/topics/nip-55/) signerのサポート、[NIP-65](/ja/topics/nip-65/) 送信トレイ ルーティングを備えた、Nostr 上に構築された暗号化メモおよびファイル ストレージ アプリです。 Blossomストレージ。このリリースでは、[NIP-42](/ja/topics/nip-42/) relay認証 (以前は壊れていました) が修正され、`http://` ホストへの Blossom アップロード (以前は誤って処理されていました) が修正され、圧縮フローが書き直されました。メディア側では、ユーザーはクリップボードへの画像のコピー、クリップボードからの画像の貼り付け、ファイルのドラッグ アンド ドロップ、画像のトリミングと回転、ビデオや GIF の再生、カメラ アイコンの長押しによるビデオの撮影ができるようになりました。 Linux では、マウスの中クリックでプライマリ クリップボードにアクセスできます。ノートの読み込みとスクロールにはいくつかの最適化が行われます。

### Routstrd v0.3.7 は、Nostr eventを永続的な信頼できる情報源として保存します。

[Routstrd v0.3.7](https://github.com/routstr/routstrd/releases/tag/v0.3.7) は、Routstr 分散型 AI 推論ネットワークのローカル daemonであり、Nostr kind 38421 プロバイダー検出および kind 38425 LGTM レビューを介して LLM リクエストをルーティングします。このリリースでは、routstrd と cocod の両方の新しいバイナリをダウンロードし、実行中のdaemonを正常に再起動する `routstrd update` サブコマンドが追加されています。daemonは起動時と 21 分ごとに `refreshNostrEvents()` を呼び出すようになり、プロバイダーの検出とレビューが手動介入なしで最新の状態に保たれます。バンドルされている `@routstr/sdk` は、0.3.12 から 0.3.15 にアップグレードし、直接 `DiscoveryAdapter` を使用するために ProviderRegistry レイヤーを削除し、ランキングに漏れないよう消滅した Nostr プロバイダーからモデルをクリーンアップし、Nostr event ストアを永続的な真実の情報源として扱います (キャッシュされたeventの誤った 210 分の TTL はなくなりました)。 Xcashu 返金処理が強化されます。返金トークンはエラー パス内のオリジナルよりも前に試行され、404 は 2 分間隔で 3 回再試行され、425 Too Early はスローせずに処理されます。

### Nymchat 1.0.1 は NIP-17 上で Progressive Web App として起動します

[Nymchat 1.0.1](https://github.com/Spl0itable/NYM) (NYM、Nostr Ynstant メッセンジャーとしても知られています) は、Bitchat とブリッジされた、Nostr 経由の一時チャット用の Progressive Web App およびネイティブ iOS/Android メッセンジャーです。チャネルは、geohash チャネルには kind 20000 一時eventを使用し、名前付きチャネルには kind 23333 を使用します。プライベート メッセージとグループ チャットは、ローテーションの一時的な受信者キーと侵害後の自動回復を備えた [NIP-17](/ja/topics/nip-17/) gift wrapされたevent (kind 1059) に乗ります。ユーザーは、登録なしでセッションごとの一時キーペアを生成したり、[NIP-07](/ja/topics/nip-07/) ブラウザー拡張機能、[NIP-46](/ja/topics/nip-46/) リモートsigner、または nsec を介して永続的な ID でログインしたりできます。オプションのデバイス ローカル ID 暗号化では、パスワード、PIN、パスキー、または WebAuthn PRF (パスキーと生体認証) または PBKDF2 (パスワードと PIN) による生体認証ロック解除を使用します。暗号化がオンになっている間、平文キーがディスクに書き込まれることはありません。音声通話とビデオ通話では、シグナリングに NIP-17 ギフト ラップを使用し、メディア パスに WebRTC を使用します。メッセージの反応は [NIP-25](https://github.com/nostr-protocol/nips/blob/master/25.md) を使用し、カスタム絵文字は [NIP-30](/ja/topics/nip-30/) を使用し、Web アプリは静的ファイルとして提供されるほか、relayやメディアのプライバシー プロキシとして機能する Cloudflare Pages 関数も提供されます。

### 21Meetup 1.1.0 が Nostr のサイン入り出席バッジを発売

[21Meetup 1.1.0](https://github.com/louisthecat86/Einundzwanzig-Meetup-App) は、NFC tagとローリング QR コードを介してミートアップの出席を記録する、ドイツの Einundzwanzig Bitcoin コミュニティ用の Flutter アプリです。各出席バッジは、BIP-340 Schnorr を使用してミートアップ主催者によって署名された Nostr event (kind 21000) であるため、参加者は、特定のブロックの高さでの特定のミートアップを証明する署名付きeventのセットを蓄積します。ローリング QR コードは 10 秒ごとに回転するため、バッジをリモートから鋳造することはできず、NFC tagは物理的に近接した場所でのみ読み取ることができます。信頼スコアは、収集されたバッジからローカルで計算されます。スコアは、ピアツーピア取引中の検証用に QR コードとして提示できます。このアプリは、汎用の Nostr ソーシャルではなく、ビットコイン コミュニティの評判をターゲットにしていますが、バッジ event自体は読者であれば誰でも確認できる通常の Nostr eventです。

### Nostrord v2.0.0 および v2.1.0 はrelay プールをフォールドし、ゾンビ WebSocket を修復します

[Nostrord v2.0.0](https://github.com/nostrord/nostrord/releases/tag/v2.0.0) は、NIP-29、NIP-42、NIP-44、NIP-46、NIP-57、NIP-65、および NIP-98 を話す KMP/WASM Nostr clientのメジャー カットです。 [v2.0.1](https://github.com/nostrord/nostrord/releases/tag/v2.0.1) は、リリースをブロックするデスクトップ修正を含む [PR #166](https://github.com/nostrord/nostrord/pull/166) 経由で 1 日後に出荷されました。パッケージ化された 2.0.0 (deb、rpm、msi、dmg) は、jpackage jlink イメージに SQLDelight sqlite ドライバーが依存する `java.sql` モジュールが欠けていたため、起動時に `NoClassDefFoundError: java/sql/DriverManager` でクラッシュしました。この修正により、ランタイム イメージに `java.sql` が追加され、同じ PR がネットワーク層を介してオプティミスティック送信をルーティングするため、メッセージはrelay (以前のコード パスはサイレントにキャッシュされ、配信されませんでした) に到達し、さらにモバイル Web でのキーボードとスクロールの動作が行われます。

[v2.1.0](https://github.com/nostrord/nostrord/releases/tag/v2.1.0) は、7 月 7 日に「relay プールのフォールド」([PR #176](https://github.com/nostrord/nostrord/pull/176)) を実行し、これまで分離されていた NIP-29 に焦点を当てたrelay ソケットを共有プールに統合しました。 1 つの再接続スケジューラがすべてのrelayをカバーするようになり、[NIP-42](/ja/topics/nip-42/) AUTH 署名は再試行に制限され、フェイル クローズと認証が必要な場合の再試行をパブリッシュし、`requestPrivateGroupData` と `fetchGroupPreviews` のリクエスト ストーム レースはクローズされ、kind-10009 ユーザー グループ リストはrelayごとにバッチを取得し、`mux_chat` ライブ subscriptionは参加しているすべてのグループをカバーするようになりました。 (開かれたものだけでなく)、relayがsubscriptionをサイレントにドロップすると自己修復します。 UI 側の変更により、レイアウトを変更する「送信中...」行がインラインの時計確認アイコンに置き換えられ、停止したスクロールバックが明示的な再試行行に変わります。 [PR #179](https://github.com/nostrord/nostrord/pull/179) は、Android 上のゾンビ WebSocket を検出するために同日に着陸しました。モバイル ネットワークと Doze モードは、クローズ フレームなしで TCP を強制終了するため、デッド ソケット バッファにスローせずにローカルで書き込み、何も受信されない場合でも `isConnected()` は true のままになります。 `NostrGroupClient` は、すべてのフレームで `lastInboundAtMs` をスタンプし、`markDead()` (フレーム ループをキャンセルして通常の再接続および再サブスクライブ パスが実行される)、および `probeLiveness()` (REQ のrelayは 5 秒以内に応答する必要がある) を獲得し、受信フレームがゼロの OK タイムアウト、またはマルチプレクサが失われ、ソケット フレームの沈黙が発生したときにトリガーされます。同じ PR の 2 番目のバグ修正により、挿入時にオプティミスティック メッセージが永続キャッシュに書き込まれるのが停止されます。今では配達確認後にのみ書き込みを行うようになりました。 [v2.1.1](https://github.com/nostrord/nostrord/releases/tag/v2.1.1) は 1 日後に [PR #178](https://github.com/nostrord/nostrord/pull/178) 経由で出荷され、v2.1.0 ゾンビ WebSocket の動作に加えて、iOS プラットフォーム実績、ネイティブ テスト サポート、アプリ アイコンが追加されました。

---

## 未リリースの変更

### rust-nostr は、ギフト ラップおよびプライベート DM builderに NIP-40 の有効期限を追加します

[rust-nostr は PR #1384 を統合](https://github.com/rust-nostr/nostr/pull/1384) `expiration` オプションを `GiftWrapBuilder` と `PrivateDirectMessageBuilder` に追加します。ライブラリは呼び出し元から `Duration` を受け取ります。[NIP-40](/ja/topics/nip-40/) 有効期限tagはgift wrapのランダム化された `created_at` (created_at +duration) に固定されており、実際の送信時間から切り離されています。呼び出し元に絶対timestampを渡すと、送信時刻がrelay オブザーバーに漏洩するため (期間を減算すると、元の送信時刻が復元されます)、ライブラリはランダム化されたラップ timestampから内部でtagを構築します。有効期限tagは、kind:13 seal ([NIP-59](/ja/topics/nip-59/) では空のtagが必要です) ではなく、ギフト ラップ eventに付けられます。 NIP-17 は、同じ値を `PrivateDirectMessageBuilder` からギフト ラップ builderに渡します。この変更は [問題 #1381](https://github.com/rust-nostr/nostr/issues/1381) を終了し、rust-nostr が `extra_tags` に使用するものと同じbuilder パターンを介して適用されます。 rust-nostr も [PR #1387](https://github.com/rust-nostr/nostr/pull/1387) を統合し、`nostr-relay-builder` を `nostr-sdk` に統合し、workspaceをフラット化しました。

### Amethyst は 1 週間かけてネゲントロピー同期を強化し、NIP-50 検索を追加しました

Amethyst の [メイン branch](https://github.com/vitorpamplona/amethyst) は、3 つの一貫したテーマにわたる 43 の PR を統合しました。最大のスレッドは、Geode と strfry の境界での negentropy 同期です。clientをウィンドウ分割ループに突入させるために使用されていた拒否されたウィンドウ障害モードは、現在はきれいにバックオフし ([PR #3480](https://github.com/vitorpamplona/amethyst/pull/3480))、基礎となる `negentropyKmp` 依存関係は v1.1.1 ([PR #3475](https://github.com/vitorpamplona/amethyst/pull/3475))、100 万eventに移行します。 geode-to-strfry ベンチマークは strfry パリティ ミラー ([PR #3478](https://github.com/vitorpamplona/amethyst/pull/3478)) を使用して実現され、実稼働ベンチマークは広範な同期最適化 ([PR #3458](https://github.com/vitorpamplona/amethyst/pull/3458)、[PR #3466](https://github.com/vitorpamplona/amethyst/pull/3466)) とともに CI マトリックスに加わります。ロックフリーの同時コレクションは、以前のrelayごとのミューテックス パターンを置き換え、UDP ソケット スレッドの修正も適用されます ([PR #3459](https://github.com/vitorpamplona/amethyst/pull/3459))。

2 番目のスレッドは [NIP-50](/ja/topics/nip-50/) 全文検索インフラストラクチャです。 `SearchableEvent` インターフェイスが導入されたため、eventはインデックス metadataを直接伝送できるようになり ([PR #3452](https://github.com/vitorpamplona/amethyst/pull/3452))、NIP-50 検索拡張機能は SQLite FTS をクエリする前に削除されるようになり、ローカル検索エンジンがサーバー側拡張構文で停止することがなくなりました ([PR #3464](https://github.com/vitorpamplona/amethyst/pull/3464))。デフォルトの検索relayが集中化されます ([PR #3446](https://github.com/vitorpamplona/amethyst/pull/3446))。

3 番目のスレッドは、ニッチな業界向けのprotocol統合です。 Birdstar 鳥検出event (kind 2473) のサポートが Android client ([PR #3473](https://github.com/vitorpamplona/amethyst/pull/3473)) に到達し、PS1 メモリーカードの保存状態を kind 38192 で署名付きeventとして公開できます ([PR #3482](https://github.com/vitorpamplona/amethyst/pull/3482))。今週の締めくくり: 署名作成設定により投稿にカスタム テキストが自動追加され ([PR #3450](https://github.com/vitorpamplona/amethyst/pull/3450))、デスクトップ通知ビューがネイティブ OS トーストと共有filterを使用して再設計され ([PR #3457](https://github.com/vitorpamplona/amethyst/pull/3457))、メッセージ列がプライバシー ロックを選択します ([PR #3432](https://github.com/vitorpamplona/amethyst/pull/3432))、`NostrServer.ingest` が追加しました送信ごとの検証スキップを備えたローカル書き込みパス ([PR #3469](https://github.com/vitorpamplona/amethyst/pull/3469))、`equals`/`hashCode` コントラクトは OpenTimestamps 検証パス ([PR #3477](https://github.com/vitorpamplona/amethyst/pull/3477)) で修復されます。

### Buzz はrelayを強化し続け、エージェント ターン メトリクスの kind 44200 を定義します

[Buzz](https://github.com/block/buzz) (以前は Sprout と呼ばれていたプロジェクト) は、7 月 1 日から 7 月 7 日までの期間にマージされた 123 個の PR を獲得しました。 2 つのスレッドがほとんどの重量を支えます。 1 つ目は、エージェント テレメトリの新しいeventの種類です。[PR #1441](https://github.com/block/buzz/pull/1441) は、NIP-AM の永続的な暗号化されたエージェント ターン メトリクスを kind 44200 として定義します。これにより、テレメトリが署名付きeventとして取得され、ユーザー自身のrelay アーカイブに保存され、ユーザー所有のインフラストラクチャにメトリクスが保持されます。その種類のローカル アーカイブが続き ([PR #1555](https://github.com/block/buzz/pull/1555))、種類の削除パスがアトミックになり ([PR #1562](https://github.com/block/buzz/pull/1562))、モデル名が出力パスを介してスレッド化されるため、下流のリーダーはどのモデルがどのターンを生成したかを区別できます ([PR #1564](https://github.com/block/buzz/pull/1564))。

2 番目のスレッドはrelayのパフォーマンスです。commit後のディスパッチは延期され、クローンの検証は回避されます ([PR #1453](https://github.com/block/buzz/pull/1453))。取り込みとファンアウト DB のラウンドトリップは、前のチップと比較して 7 ～ 16 パーセントの p99 ACK ドロップと 29 ～ 53 パーセントの p999 テール ドロップでバッチ処理されます ([PR #1454](https://github.com/block/buzz/pull/1454))。マルチfilter クエリの実行は制限付き同時実行で実行されます。 ([PR #1457](https://github.com/block/buzz/pull/1457))、送信 WebSocket データ フレームは送信時にバッチ処理されます ([PR #1464](https://github.com/block/buzz/pull/1464))。パフォーマンス作業に加えて、管理者が設定し、relayが [NIP-11](/ja/topics/nip-11/) 経由で提供するコミュニティごとのworkspace アイコン セットは、コミュニティごとのカスタマイズ面 ([PR #1463](https://github.com/block/buzz/pull/1463)) で NIP-11 の情報ドキュメントを拡張し、エージェントの所有者はrelay kind:5 eventと一致するデスクトップおよびモバイル UX ([PR) を介してエージェントのメッセージを削除できます。 #1519](https://github.com/block/buzz/pull/1519))、OpenTelemetry トレースはrelay上の Prometheus メトリクスに結合し ([PR #1398](https://github.com/block/buzz/pull/1398))、git repo-name レジストリは Postgres に移動します ([PR #1432](https://github.com/block/buzz/pull/1432))。

### Divine Video はrelay署名検証と NostrConnect 抽出を接続します

Divine Video の [モバイル アプリ](https://github.com/divinevideo/divine-mobile) はウィンドウ内の 97 個の PR をマージし、Nostr 側のスレッドは信頼境界の強化と認証のクリーンアップを行いました。 [PR #5774](https://github.com/divinevideo/divine-mobile/pull/5774) 受信relay event署名を検証し、relayの信頼性に関する一連のバグを解決します。 [PR #5828](https://github.com/divinevideo/divine-mobile/pull/5828) kind-3080 登録解除eventの FCM プッシュ トークンを暗号化することで、ユーザーのデバイス トークンが登録解除時にrelay上に平文で表示されなくなります。 [PR #5831](https://github.com/divinevideo/divine-mobile/pull/5831) は、kind:5 の削除 REQ をチャンク化して、大量の削除履歴を持つユーザーがrelay フレームをオーバーフローさせなくなりました。認証側では、[PR #5826](https://github.com/divinevideo/divine-mobile/pull/5826) は `nostrconnect://` フローの `NostrConnectCoordinator` を抽出し、[問題 #4741](https://github.com/divinevideo/divine-mobile/issues/4741) で追跡されている広範な認証リファクタリングの前に、[NIP-46](/ja/topics/nip-46/) clientによって開始されたバンカー コード パスをクリーンアップします。 [PR #5709](https://github.com/divinevideo/divine-mobile/pull/5709) は、`notification_type` が存在しない場合に kind-16 の再ポストをマップするため、送信clientがヒントを省略した場合でも再ポスト通知が正しくレンダリングされます。

### Zap Cooking は NIP-46 バンカー ログインを修正し、NIP-50 レシピ検索を追加します

[Zap Cooking のフロントエンド](https://github.com/zapcooking/frontend) は、Nostr 認証サーフェスを障害から回復するという 1 つのテーマに沿ってウィンドウ内の 18 個の PR をマージしました。 [PR #503](https://github.com/zapcooking/frontend/pull/503) は、明示的な接続handshake、authUrl 処理、およびエラー表示によるバンカー ログインを修正し、外部signerをアタッチしているユーザーには、前のカットでログイン画面がハングした失敗時に実際のエラー メッセージが表示されるようにします。 [PR #495](https://github.com/zapcooking/frontend/pull/495) NIP-98 認証を抽出レシピ エンドポイントの画像およびテキストのアップロード パスに追加して、アップロードが公開鍵に関連付けられるようにします。別の機能スレッドは、nostrarchives 検索relay バックエンド ([PR #483](https://github.com/zapcooking/frontend/pull/483)) を介して NIP-50 全文レシピ検索を実行し、ユーザーがclient側のインデックスなしでrelay コーパス全体でレシピをクエリできるようにします。コンテンツ レンダリングの洗練も同時に行われます。引用ノートのコンテンツとメディアは、以前の埋め込みリンク フォールバック ([PR #491](https://github.com/zapcooking/frontend/pull/491)) に代わって親ノートに直接表示されるようになり、リンク プレビューとhashtagのサイジング ランド ([PR #492](https://github.com/zapcooking/frontend/pull/492))、複数の単語の検索クエリが機能し ([PR #482](https://github.com/zapcooking/frontend/pull/482))、サーバー側のソーシャル プレビュー カードがノート用に生成されます。読書、プロフィールのリンク ([PR #494](https://github.com/zapcooking/frontend/pull/494))。

### swift-nostr-client v0.6.0 は最初の安定カットに向けて前進

[yysskk/swift-nostr-client](https://github.com/yysskk/swift-nostr-client) は、30 個のマージされた PR とともに [v0.6.0](https://github.com/yysskk/swift-nostr-client/releases/tag/0.6.0) を出荷しました。 Swift Nostr ライブラリは、MDK または MarmotKit ツールチェーンのリンクを回避する Swift Nostr client向けに、最初の安定した API サーフェスに近づきます。

### Nostr Applet Protocol (NAPS) は NAP-OUTBOX のルーティングとファンアウトを強化します

NAPS は、主に [NAP-OUTBOX](https://github.com/napplet/naps/pull/32) で有意義なクリーンアップ週間を過ごしました。見出しは、より厳しい境界です。呼び出し元制御のルーティングが減少し、relayの詳細の漏洩が減少し、relay ヒントとリソース サイドカーを運ぶことができる共有event結果の形状が [NAP-RESOURCE](https://github.com/napplet/naps/pull/80) に結び付けられます。パブリッシュも明確になり、送信ボックス、受信ボックス、およびrelayのファンアウト ルールが明確になります。最終的な効果: 曖昧さが減り、相互運用性が向上します。

### ナプレット ツールチェーンがprotocolの調整を強化し、CLI を出荷

今週、Napplet のパッケージは「便利な SDK」からより緊密なprotocol ツールチェーンに移行しました。大きな特徴は、ライブ NAP 仕様との調整です。[NAP-COUNT クエリ サポート](https://github.com/napplet/web/pull/104)、[OUTBOX のランタイム所有のライフサイクル](https://github.com/napplet/web/pull/112)、および [RelayEventResult サイドカー](https://github.com/napplet/web/pull/108) がすべて実装され、シェルを介した読み取りとsubscriptionがより正確になりました。 CVM レジストリ サポート、DM エラー エンベロープ、MEDIA セッション コンテキスト、LISTS カウント フィールド、COMMON プロファイル結果、htree: RESOURCE スキームなど、いくつかのドメインも強化されました。ツールに関しては、新しい [@napplet/cli](https://github.com/napplet/web/pull/103) が主要なマイルストーンであり、構成の検出、デプロイ計画、署名、Blossom アップロード、マニフェスト生成が追加されています。最後に、[ホスト注入可能なシム プレリュード](https://github.com/napplet/web/pull/127) と [JSR 準備作業](https://github.com/napplet/web/pull/145) により、スタックの注入、公開、検証が容易になりました。

### primal-android はリモートsignerサーフェスを拡張します

[Primal Android](https://github.com/PrimalHQ/primal-android-app) はウィンドウ内の 18 個の PR をマージしました。 Nostr 側では、[PR #1075](https://github.com/PrimalHQ/primal-android-app/pull/1075) はアプリのリモートsignerの役割に `switch_relays` メソッドと `logout` メソッドを実装し、Primal の NIP-46 signerサーフェスを拡張します。 [PR #1083](https://github.com/PrimalHQ/primal-android-app/pull/1083) はスプラッシュ ゲートのローカル アプリ移行フレームワークを追加し、[PR #1080](https://github.com/PrimalHQ/primal-android-app/pull/1080) はスプラッシュ ビュー モデルでノートフィードのプリフェッチを実装します。残りは、ホームの上部と下部のバー、探索ヒント、プロフィール画面全体の UI の洗練です。

### Wisp はマルチアカウント スイッチャーと Blossom パーサー テストを追加します

[Wisp](https://github.com/barrydeen/wisp) 9 つの PR をマージしました。 [PR #604](https://github.com/barrydeen/wisp/pull/604) アカウント追加フローに明示的なキャンセル パスを持つマルチアカウント スイッチャーを追加します。 [PR #613](https://github.com/barrydeen/wisp/pull/613) `Blossom.parseServerList` の単体テストを追加し、[Blossom](/ja/topics/blossom/) サーバーリスト パーサーを強化します。 [PR #574](https://github.com/barrydeen/wisp/pull/574) はインスタントザップ設定画面で iOS レイアウトのザップシートを書き換え、[PR #605](https://github.com/barrydeen/wisp/pull/605) はトランザクション履歴をスワイプアップのボトムシートに変換し、[PR #611](https://github.com/barrydeen/wisp/pull/611) は非 ASCII Unicode 文字を含むhashtagを解析し、[PR #609](https://github.com/barrydeen/wisp/pull/609)プロフィール メモ フィードのページ分割を維持し、インライン ギャラリー メディアをレンダリングし、[PR #603](https://github.com/barrydeen/wisp/pull/603) はインライン プロフィールとhashtag セグメントの前の空白行を保持します。

### TAO および Wired は、PoW 信号を 21 ビットに引き上げ、新しい PoW ルートを表面化します。

[smolgrrr/TAO](https://github.com/smolgrrr/TAO) と [smolgrrr/Wired](https://github.com/smolgrrr/Wired) (同じcommit セットが両方のリポジトリに配置されました) は 13 の PR をマージしました。 [PR #84](https://github.com/smolgrrr/TAO/pull/84) は、デフォルトの信号後のproof-of-work ターゲットを先頭のゼロ 21 ビットに引き上げます。また、[PR #80](https://github.com/smolgrrr/TAO/pull/80) は、clientが最近の NIP-13 作業によってタイムラインをランク付けできるように、新しい PoW アクティビティからフィード ルートを表面化します。前回のランキングは生のevent年齢でした。 [PR #75](https://github.com/smolgrrr/TAO/pull/75) はカスタム絵文字ピッカーを復元し、[PR #65](https://github.com/smolgrrr/TAO/pull/65) は最初のフレームのビデオ プレビューを追加します。これは、ユーザー生成コンテンツのファーストクラス filterとして NIP-13 を利用する今週 2 番目の Nostr clientであり、Bitchat のチャネル スコープの PoW を補完します。

### keep-android は NIP-46 UX を磨き、TOCTOU 修正をリリースします

[privkeyio/keep-android](https://github.com/privkeyio/keep-android) は 13 個のマージされた PR とともに [v1.1.5](https://github.com/privkeyio/keep-android/releases/tag/v1.1.5) を出荷し、その後 7 月 8 日に [v1.1.6](https://github.com/privkeyio/keep-android/releases/tag/v1.1.6) で基礎となるキープ コアを v0.5.0 に固定しました。 Keep はモバイル ID ボールトです ([問題 #29](/en/newsletters/2026-07-01-newsletter/#custid-launches-as-a-mobile-identity-vault-with-nip-46-and-nfc-challenge-flow) で CustID として取り上げられます)。 v1.1.5 は、[NIP-46](/ja/topics/nip-46/) チャレンジ フローの UX を磨きました。 v1.1.6 は、基盤となる keep-mobile クレートから `set_active_share` のチェックしてから設定 (TOCTOU) レースを終了し、[NIP-98](/ja/topics/nip-98/) HTTP 認証承認プロンプトで承認されている URL とメソッドを表示して、ユーザーが署名している内容を確認できるようにし、RNG ヘルス チェックをパニックではなくフェール クローズ (エラーを返す) に切り替えます。インストルメント化されたテストでは、NIP-55 承認フロー キル スイッチがカバーされます。基礎となるリリースに付属していた v0.5.0 CLI の機能 (しきい値 OPRF ロック解除、ソフトウェア DKG、HD FROST ウォレット) は、Android アプリにはまだ表示されていません。 v1.1.6 はセキュリティ修正のみを提供します。

### Heartwood にはrelayからシリアルへの署名ブリッジが同梱されています

[forgesworn/heartwood v0.7.0](https://github.com/forgesworn/heartwood/releases/tag/v0.7.0) は、先週飛行していたrelayからシリアルへの署名ブリッジを着陸させ、Bray のシリアルsignerパスの HSM モード データ プレーンを配線します。 [PR #11](https://github.com/forgesworn/heartwood/pull/11) はブリッジ自体であり、[PR #13](https://github.com/forgesworn/heartwood/pull/13) はシリアル フレーム カバレッジを追加してデバイス `read_frame` payload オフセットを修正し、[PR #14](https://github.com/forgesworn/heartwood/pull/14) はシリアル フレーム コーデックを共有 `heartwood-frame` クレートに抽出します。

### SafeBox がフェーズ 3 の進捗レポートと FreeBSD ジェイル ランブックを公開

[SafeBox](https://github.com/trbouma/safebox) は、[NIP-47](/ja/topics/nip-47/) Nostr Wallet Connect、nAuth、nembed、および QR および NFC を介したrelay仲介レコード転送を 1 つのオペレーターが導入可能なサービスに組み合わせた Nostr 上のプライベート ポータブル データ ボールトです。 7 月 6 日に公開された [2026 年 7 月の進捗レポート](https://github.com/trbouma/safebox/blob/main/docs/PROGRESS-REPORT-2026-07.md) は、フェーズ 3 が実質的に完了したことを示しています。4 月のレポート以来 49 件のcommitが到着し、リポジトリのcommit数は 1,136 になり、フェーズ 3 の 4 つのエンジニアリング commitメント (フェーズ 2 の実験の強化、相互運用可能なインスタンスのサポート、規模の準備、商用製品の規律の追加) はほぼ達成されています。この報告書は、次のステップを限定的なパイロットとして枠組み化しており、NDAに基づく電気通信プロバイダーがSafeBoxでの健康記録のパイロットを検討していることを明らかにしている。

Nostr に向けた具体的な作業はフェーズ 3 の早い段階で行われ、レポートにまとめられています。変異する NWC アクションはプルーフ レースを避けるためにキューに入れられるようになり、失敗した Lightning Melt は戻る前にプルーフを保護し、長寿命の NWC リスナーは積極的に更新されるようになり、セッションがアイドルしきい値を超えても存続できるようになりました。以前の動作はサイレント ストールであり、LNURL コールバックは明示的な JSON および CORS 応答を持つ正規のオリジンを使用します。 QR および NFC レコード交換は、受信者提示モード、送信者提示モード、およびクロスデバイス プレゼンテーション モードをカバーする統一フロー仕様を獲得し、Open Quantum Safe ライブラリを介したより明確な KEM (キー カプセル化メカニズム) の処理とリプレイ保護を備えています。ウィンドウ内commitは [`6866dae`](https://github.com/trbouma/safebox/commit/6866dae) です。これにより、[FreeBSD アプライアンス仕様](https://github.com/trbouma/safebox/blob/main/docs/devops/SAFEBOX-FREEBSD-APPLIANCE-SPEC.md) とともに [FreeBSD ジェイル デプロイメントおよび liboqs ビルド Runbook](https://github.com/trbouma/safebox/blob/main/docs/devops/freebsd-jail-from-scratch.md) が追加され、ZFS スナップショット、ジェイル分離、`rc.d` サービス管理、ホストレベルのリバース プロキシ構成、およびロールバック手順が文書化されます。 FreeBSD/ARM ハードウェア上での SafeBox の展開。

このレポートはまた、SafeBox の暗号制御プラスポータブル記録アーキテクチャを電子譲渡可能な記録 (船荷証券、倉庫受領書、約束手形、証明書) に適用する別個のスピンオフとして [OpenETR](https://github.com/trbouma/openetr) を発表しています。 OpenETR のリポジトリでは、7 月 7 日に 7 件のcommitが確認されました。これには、コア レコードから構成証明を分離する [`ea612a9`](https://github.com/trbouma/openetr/commit/ea612a9)、義務と効果の処理に関する [`ca153a3`](https://github.com/trbouma/openetr/commit/ca153a3)、検証可能な資格情報形式との比較を追加する [`ba84b61`](https://github.com/trbouma/openetr/commit/ba84b61) が含まれます。

---

## protocolの動作と NIP の更新

### マージ: NIP-51 と NIP-37 が kind 10013 名を揃えます

[PR #2404](https://github.com/nostr-protocol/nips/pull/2404) は散文のみの一貫性修正です。 [NIP-37](/ja/topics/nip-37/) では、kind 10013 は `Relay List for Private Content` という名前になります。 `Draft relays` の [NIP-51](/ja/topics/nip-51/) で、同じ種類が異なる文言で説明されていました。 NIP-51 は、同じeventの種類に対して NIP-37 名を使用するようになりました。ワイヤの動作の変更や新しいtagのセマンティクスはありません。重要なのは、NIP-51 がリスト形式のeventの包括的な仕様であり、NIP-37 がプライベート コンテンツのフォローアップであることです。この 2 つの名前の位置が一致していないため、これらが同じ種類のものであることを見逃しやすくなります。

### 開く: .well-known ルックアップによる NIP-AD Nostr Web アドレス

[PR #2406](https://github.com/nostr-protocol/nips/pull/2406) は、クローズされた PR #2393 の後継として、[`AD.md`](https://github.com/nostr-protocol/nips/blob/2f4b09335c54a993d483bc220195e3f4a33df1ec/AD.md) でフルスペックのドラフトとともにオープンします。 NIP-AD は、オプションの Nostr 対応物を含む Web URL を定義します。 `https://golf.com/players` のような URL を見たclientは `https://golf.com/.well-known/nostr.json?ad=/players` をリクエストし、`{filter, relays}` ペアへのパスをマッピングする JSON オブジェクトを返します。返されるfilterは、標準の NIP-01 filter (種類、作成者、`#d`、`limit` など) と、clientがクエリする必要があるrelayの配列名です。 `"limit": 1` では、URL は単一のeventに解決されます。それなしでリストに。通常の Web ブラウザでは、URL は他の URL と同様に HTML をレンダリングするため、同じドメインが 1 つの正規パスから Web ユーザーと Nostr clientにサービスを提供できます。記載されているユースケースには、特定のrelay上の kind 39000 eventに解決される [NIP-29](/ja/topics/nip-29/) グループ名 (グループ ID ファーミングの必要性がなくなる)、[NIP-5A](/ja/topics/nip-5a/) nsite ルックアップ、`{"ids": [...]}` filterを公開するホストされたフィード、貼り付けられた `njump.me/nevent1...` とclient固有のevent URL のネイティブ レンダリングが含まれます。 Nostr を燃料とするブログは、Nostr 内と外部の訪問者の両方にネイティブに存在します。 `.well-known/nostr.json` 再利用とオブジェクト キーとしてのパスのレイアウトが選択されているため、リゾルバーは静的ファイルにすることができます。

### 開く: 招待コードの NIP-86 クレーム管理

[PR #2408](https://github.com/nostr-protocol/nips/pull/2408) は、[NIP-86](/ja/topics/nip-86/) に 3 つのメソッドを追加することを提案しています: `listclaims` (パラメータ `[]`、[NIP-43](/ja/topics/nip-43/) 招待コードの配列を返します)、`createclaim` (パラメータ `[claim]`、`true` を返します)、 `deleteclaim` (パラメータは `[claim]`、戻り値は `true`)。現在、NIP-86 を使用すると、relay管理者はユーザーとロールの割り当てを管理できますが、招待コード サーフェスはありません。 PR 著者のユースケースは、コミュニティrelayオンボーディングです。管理者は、ロールに関連付けられた招待コードを作成し、ユーザーの ID が作成される前に支払いを徴収し、招待コードをユーザーに渡します。ボットは、relay上で結果として生じる kind 28935 要求eventをリッスンして、ロールを自動割り当てします。 3 つの方法では、フロー全体がrelay管理 RPC を通じて実行されます。

### オープン: (h, s, l) タプルとしての役割の色

[PR #2402](https://github.com/nostr-protocol/nips/pull/2402) は、[NIP-43](/ja/topics/nip-43/) のロール カラー形式を単一の `hue` 値 (0 ～ 360) から `hue` (0 ～ 360)、`saturation` (0 ～ 1)、および `lightness` (0 ～ 1) のタプルに変更します。どのコンポーネントでも空の文字列が許可されているため、clientは一貫したパレットに独自のデフォルトを指定できます。仕様テキストでは、銀などの特定の色が必要でない限り、`hue` のみを指定することを推奨しています。同じ PR 内の NIP-86 を介した変更スレッド: `createrole` と `editrole` は `[id, label, description, [h, s, l], order]` を取得するようになりました。以前のシグネチャでは、同じスロットに単色のパラメータが含まれていました。その動機は、オペレータが色相だけでclientに彩度と明度を選択させるため、異なるclientが同じ役割を目に見えて異なる強度で表現できるようにするためです。

### オープン: NIP-80 ハードウェアで証明されたメディアの出所

[PR #2409](https://github.com/nostr-protocol/nips/pull/2409) は、キャプチャ ハードウェアに固定されたメディア来歴のevent フォーマットである NIP-80 を開きます。カメラは、撮影の瞬間に各写真に署名し、コンテンツ自体をキーとする証拠をrelayに公開するため、metadataの削除、再ホスティング、プラットフォームの削除後も検証が可能になります。この提案では、6 つの新しいeventの種類を定義しています。キャプチャ証明書用の kind 1080、サイズ変更、トリミング、再圧縮、または秘匿化操作 (公開モードまたはゼロ知識オプション付き) を対象とする派生証明書用の kind 1081、取り消し用の kind 1082 (通常のevent、永続的、作成者スコープの、単調)、デバイスのアナウンス用の kind 11080、デバイスの承認用の kind 31080、匿名証明書用に設定されたデバイスの kind 31081 (実験的としてマークされており、コンパニオン NIP に分割される可能性があります)。再利用されるプリミティブには、NIP-94 `x` tag セマンティクス、失効検出用の [NIP-92](/ja/topics/nip-92/) `imeta`、[NIP-65](/ja/topics/nip-65/)、メディア ストレージ用の [Blossom](/ja/topics/blossom/)、およびオプションが含まれます。 [NIP-03](https://github.com/nostr-protocol/nips/blob/master/03.md) timestamp アンカリング。署名モデルは、主流のセキュア エレメントがまだ BIP-340 署名を生成していないため、BIP-340 デバイス キーとハードウェア ECDSA キーを組み合わせます (Microchip ATECC608 は P-256 をサポートし、NXP SE050 は secp256k1 をサポートしますが、ECDSA、TPM 2.0 モジュールおよび Infineon OPTIGA Trust M は P-256/RSA、Apple Secure Enclave をカバーするのみです)および Android StrongBox は P-256 を使用します)。記載されているスコープは、シーンが本物であることを明示的に証明しようとするものではありません。証明書は、この正確な画像がほぼこの時点でこのデバイスから送信され、宣言された証明可能な方法でのみ変更されたことを証明し、仕様はclientが結果を裸の「本物の」バッジに折りたたむことを禁止しています。 ATECC608 セキュア エレメントを使用する Raspberry Pi 用の Rust カメラ ランタイムである実用的なプロトタイプ [OpenVeilCam](https://github.com/PrarthanaPurohit/OpenVeilCam) は、スタンドアロンの検証ツールとともに提案されたeventの種類を公開するために更新されています。

### オープン: NIP-01 ページネーションの強化

[PR #2407](https://github.com/nostr-protocol/nips/pull/2407) NIP-01 に「ページネーションと制限」サブセクションを追加しました。具体的なルール: 最大 `limit` MUST を課すrelayは、データベース内の単一の `created_at` を共有するeventの最大数よりも大きく設定するため、ページが 1 秒も埋まってページネーションが停止することはありません。逆方向にページングするclientは、MUST で `until = oldest` (両端を含む) でリクエストを繰り返し、MUST は `id` で重複排除します (ラウンドごとに最も古い 2 番目が再フェッチされるため)。重複排除後にラウンドで新しいeventが生成されない場合、ページングは​​完了します。ページ全体に 1 つの `created_at` を共有する最も古いeventと最新のeventがある場合、client MUST はその秒をより大きな `limit` で再試行し、relayがより大きな `limit` をクランプしても 1 秒に制限されたページを返す場合、client MUST は `until = oldest - 1` (未取得のeventをドロップされたものとして扱う) に進むか中止します。通常のページング MUST NOT セット `limit`;relayの最大値が有効であり、値が小さいと再びストールが発生します。 `limit` を上げてスタック秒を排出する場合は 1 つの例外です。この修正が重要なのは、単純な `since`/`until` カーソルは重複したtimestampを持つeventを見逃すか再処理するためであり、現在の NIP-01 テキストはトラップを回避する方法をどちらの側にも伝えていないためです。

---

## NIP の詳細: NIP-13 (作業証明)

[NIP-13](/ja/topics/nip-13/) は、Nostr eventのプルーフ・オブ・ワーク・メカニズムを定義します。これが存在するのは、電子メール形式のスパムが公共中継ネットワーク上で生成されるのが簡単であるためです。誰でもキーペアを生成してトピックを大量に送信でき、eventごとに経済的コストが発生しません。 NIP-13 を使用すると、event作成者はeventごとに計算コストを課すことができ、スパム送信者はその計算コストを総額で支払う必要がありますが、通常の送信者はメッセージごとに 1 回しか支払いません。その後、relayとclientは、難易度のしきい値を満たすeventを要求または優先することができます。

### 仕組み

event作成者は、ビットで表現される難易度ターゲットを選択し、少なくともその数の先行ゼロ ビットが含まれるまでeventの ID (シリアル化されたeventの sha256 hash) をマイニングします。event ID には `created_at` timestamp、tag、コンテンツが含まれるため、マイニングではhash空間を検索するためにevent本文の何かを変更する必要があります。 NIP-13 は、まさにこの目的のために `nonce` tagを定義します。

```
["nonce", "<nonce_value>", "<target_bits>"]
```

`nonce_value` はマイナーが選択する任意の文字列です。 `target_bits` はマイナーが取り組んだ難易度です。ベリファイアはevent ID の先頭の 0 ビットをカウントし、`target_bits` と比較します。tag内の `target_bits` はクレームであり、検証者は ID の実際の先頭ゼロの数を測定してそれを確認します。

ランダムな sha256 出力内の先行ゼロ ビットの数は幾何学的分布に従います。ビットが追加されるたびに、予想される作業量が 2 倍になります。 8 ビットでは平均 256 回のhash試行、20 ビットでは平均約 100 万回、28 ビットでは平均約 2 億 6,800 万回のhash試行になります。 Bitchat の geohash チャネル メッセージの 8 ビット ターゲットは、最新のハードウェアでは CPU のコストが 1 ミリ秒未満で、知覚可能な遅延未満で完了します。 TAO と Wired の 21 ビットのデフォルトは、ポストあたり約 200 万回のhash試行で、ラップトップでは高速ですが、ボット ファームの大規模な場合には高価です。 NIP-13 は難易度を要求しません。各relayとclientは独自のものを選択します。

### event例

NIP-13 でマイニングされた最小限の kind-1 ノートは次のようになります。

```json
{
  "id": "000000000e9d97a1ab09fc381030b346cdd7a1a8a6f27c9c88f68c8b9d0f6c8a",
  "pubkey": "82341f882b6eabcd2ba7f1ef90aad961cf074af15b9ef44a09f9d2a8fbfbe6a2",
  "created_at": 1720368000,
  "kind": 1,
  "tags": [
    ["nonce", "72847", "28"]
  ],
  "content": "hello, this cost me 28 bits of PoW",
  "sig": "b1a5c9c74cff59f8a48e5c3b3d8e1c8e7e2c1d4a8e2b9f7d1c3e8b4f6a2c8d1e9f4b3c7a1d8e5b2f9c6a3d7e1b8f4c9a2d6e3b7f1c8a4d9e2b5f8c1a7d4e6b9f3c2"
}
```

`id` は 7 つの 16 進ゼロ (先頭の 28 ビット、ノンス tagの `target_bits` と一致) で始まります。マイナーは、ID がターゲットを満たすまで、`nonce_value` `72847` を変更しました。検証者はシリアル化されたeventをhashし、ID の先頭に少なくとも 28 ビットのゼロがあることを確認してから、署名を検証します。 NIP-13 は新しいフィールドを追加しません。 `nonce` tagを追加し、ID のゼロビット数を制限します。

### 使用される場所

Bitchat の 1.5.4 リリースでは、kind 20000 ジオhash チャネル メッセージで 8 ビット PoW を使用します。アウトバウンド送信では、公開前にtagがマイニングされ、検証された PoW によるインバウンド eventでは、送信者ごとの取り込みレート制限が緩和されます。 TAO および Wired は、デフォルトのポスト信号しきい値として 21 ビット PoW を使用し、新しい PoW アクティビティからのサーフェス フィード ルートを使用し、PoW をタイムライン ランキング信号として扱います。 [cagliostr](https://github.com/mattn/algia) はrelay層で NIP-13 を強制し、しきい値を下回るeventを拒否します。 NoStrudel は、フィルタリング clientに信号を送りたい作成者向けに、client側の PoW マイニング設定を公開します。 Damus と Amethyst はeventを表示するときに先頭の 0 ビットを計算し、ユーザーがノート上の PoW commitメントを確認できるようにします。 Coracle は、マイニングとフィルタリングの両方のために PoW を公開します。 NDK と nostr-tools は、PoW マイニング ヘルパーをライブラリ コンシューマに公開します。

NIP-13 の展開を形成する設計特性は、PoW が偽造できないことです。`target_bits` の主張は、ID の先頭にその数のゼロがある場合にのみ証拠としてカウントされ、偽造の場合は作業をやり直す必要があります。このプロパティにより、スパム発信者が高い難易度を主張する場合でも、Bitchat は受信 PoW をレート制限緩和手段として使用できます。チェックはhash数であり、信頼性の決定ではありません。補完的な特性は、PoW がマイナーを特定の公開キーやコンテンツにcommitしないことです。スパマーは依然として 8 ビットでマイニングしてコンピューティングを焼き付けることを選択できますが、コンピューティングには実際のコストがかかります。 NIP-13 は、スパム問題を「不可能」から「定量化可能」に変え、clientが独自の価格を設定できるようにします。

---

## NIP 詳細: NIP-40 (有効期限timestamp)

[NIP-40](/ja/topics/nip-40/) は、特定の Unix timestampの後にeventが期限切れになったと見なす必要があることをrelayとclientに指示する `expiration` tagを定義します。これが存在するのは、Nostr eventが永続的であるためです。署名されたeventがrelayに到達すると、それを削除する唯一の方法は NIP-09 削除eventであり、その後でもrelayはオリジナルを保持する可能性があります。 NIP-40 を使用すると、作成者は公開時にeventの存続期間が短いことを宣言し、relayにeventの提供を停止し、clientにtimestampの後にeventの表示を停止するよう要求できます。

### 仕組み

作成者は `expiration` tagをeventに追加します。

```
["expiration", "<unix_timestamp>"]
```

timestampは Unix 秒です。relay MAY は取り込み時に有効期限がすでに過ぎているeventを拒否し、MAY は有効期限が過ぎたeventの処理を停止し、SHOULD は作成者が指定した有効期限を尊重します。client SHOULD は、期限切れのeventをユーザーから隠します。 NIP-40 はrelayがeventを削除する必要はなく、NIP-70 の保護されたeventのセマンティクスを無効にすることはありません。それはヒントとソフトコントラクトです。

tagはevent自体 (またはラップされたメッセージングの場合は外側のラップ) 上に存在します。 NIP-40 は削除セマンティクスを定義しません。eventは署名されたeventのままであり、それを持っている人なら誰でも読むことができます。 NIP-40 が与えるのは、relayとclientが期限後にeventの表示を停止するという調整された期待です。これにより、NIP-40 は、一時的な投稿、時間指定されたアナウンス、event後に提供を停止する必要があるライブ event メモ、および指定された期間を超えて残すべきでない NIP-17 ダイレクト メッセージに役立ちます。

### gift wrapとのやり取り

今週掲載された rust-nostr PR ([PR #1384](https://github.com/rust-nostr/nostr/pull/1384)) は、NIP-40 が [NIP-59](/ja/topics/nip-59/) gift wrapとどのようにやり取りするかを示すケーススタディです。 NIP-59 は、送信者の実際のキーで署名された kind:13 "seal" eventと、一時的なキーで署名された kind:1059 "ギフト ラップ" eventの 2 層エンベロープを定義します。両方の層には、実際の送信時刻の最大 48 時間前までにランダム化された `created_at` 値があるため、relay オブザーバーは真の送信timestampを回復できません。 NIP-59 では、sealに空のtagを付けることが義務付けられています。

この義務は、有効期限tagがgift wrap紙に付けられ、封印されないようにしなければならない理由と、実際の送信時刻にtagを固定することがgift wrapのタイミングプライバシーを損なう理由です。呼び出し側が絶対有効期限timestampを渡すと、オブザーバーは呼び出し側の意図した TTL を減算して、実際の送信時刻を回復します。 rust-nostr の設計上の決定は、呼び出し元から API を `Duration` として公開し、ライブラリ内で `expiration = wrap.created_at + duration` を計算することです。ラップの `created_at` はライブラリ内ですでにランダム化されているため、有効期限timestampは同じランダム化を継承し、実際の送信時刻を漏らすことはありません。

### event例

kind-1 メモの最小限の NIP-40 の例:

```json
{
  "id": "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b",
  "pubkey": "82341f882b6eabcd2ba7f1ef90aad961cf074af15b9ef44a09f9d2a8fbfbe6a2",
  "created_at": 1720368000,
  "kind": 1,
  "tags": [
    ["expiration", "1720454400"]
  ],
  "content": "this note expires in 24 hours",
  "sig": "d2e5b8a1c4f7b0d3e6a9c2f5b8d1e4a7c0f3b6d9e2a5c8f1b4d7e0a3c6f9b2d5e8a1c4f7b0d3e6a9c2f5b8d1e4a7c0f3b6d9e2a5c8f1b4d7e0a3c6f9b2d5e8a1"
}
```

`created_at` は発行時の Unix timestampです。有効期限tagには、86,400 秒 (24 時間) 後にeventの提供を停止する必要があることが示されています。 NIP-40 を尊重するrelayは、`1720454400` 以降、このeventを REQ に返すことを停止し、NIP-40 を尊重するclientは、それ以降、このeventをユーザーに対して非表示にします。

### 使用される場所

rust-nostr のbuilder (`GiftWrapBuilder`、`PrivateDirectMessageBuilder`) は、有効期限をファーストクラスの `Duration` パラメーターとして公開するようになりました。 NDK は、kind-1 および DM builderの有効期限ヘルパーを公開します。 nostr-tools には、tagの読み取りと強制を行うための `getExpiration` と `isExpired` のペアがあります。 strfry、nostr-rs-relay、khatru、およびその他のrelay実装は、REQ 処理で NIP-40 を尊重します (オペレーターのポリシーに応じて、期限切れのeventを拒否または省略します)。 Damus、Amethyst、noStrudel、Coracle、および Primal はすべて、タイムライン レンダリングから期限切れのeventをfilterします。 zap.stream などのライブ アクティビティ clientは、関連する kind-1311 チャット eventで NIP-40 を使用するため、ストリーム終了後にライブ チャットは継続しなくなります。

ほとんどの実装で NIP-40 を適切に実現する設計特性は、eventごとにオプトインされ、調整された展開を必要としないことです。著者は今すぐtagを追加できます。それを尊重するrelayはよりクリーンなワーキングセットを取得します。それを無視したrelayは以前よりも悪いことはしません。そして、期限切れのeventを非表示にするclientは、作成者に要求したものを提供します。今週の rust-nostr の変更は、tagの存在と同じくらいtagの配置が重要であることを強化しています。NIP-59 gift wrapのようなプライバシー保護封筒では、tagはtimestampがすでにランダム化されているレイヤー上に配置され、API サーフェスは呼び出し元が誤って実際のtimestampをラップに漏洩するのを防ぎます。

---

今週はここまでです。何かを構築していますか、それとも共有するニュースがありますか? NIP-17 DM 経由でお問い合わせいただくか、Nostr で当社を見つけてください。
