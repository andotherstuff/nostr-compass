---
title: "Nostr Compass #31"
date: 2026-07-15
publishDate: 2026-07-15
draft: false
type: newsletters
translationOf: /en/newsletters/2026-07-15-newsletter.md
translationDate: 2026-07-15
description: "Vector v0.4.0 がグループチャットの Marmot を廃止し、オープンな MIT ライセンスの Concord プロトコルに切り替え、数日後に Concord v2 を出荷。Amethyst が独自のクリーンルーム版 Concord 実装をマージ。Sonar が Bitchat から分離してクロスプラットフォームのアルファ版とステッカーパック仕様を公開。Divine Mobile 1.0.16 が保存時暗号化と ProofMode の来歴情報を搭載。Bitchat 1.7.0 がライブのプッシュトゥトーク音声を追加。MDK v0.9.4 が外部署名者ログインに上限を設ける。"
---

Nostr Compass へようこそ。毎週お届けする Nostr のガイドです。

**今週:** [Vector v0.4.0](#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later) はグループチャットのデフォルトトランスポートである [Marmot](/ja/topics/marmot/) を廃止し、Soapbox の Armada でも使われているオープンな MIT ライセンスのコミュニティプロトコル [Concord](/ja/topics/concord-protocol/) に切り替えました。そして 4 日後には Concord v2 を出荷し、ボット向けのスラッシュコマンドピッカー、自己破壊タイマー、NIP-58 バッジを追加しました。同じ週に [Amethyst が独自のクリーンルーム版でワイヤー互換の Concord 実装をマージしました](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities)。[Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec) は Bitchat から分離してクロスプラットフォームのアルファ版を公開し、今週のステッカーパック kind 提案で引用された仕様のソースにもなっています。[Divine Mobile 1.0.16](#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance) はより高度なビデオエディター、保存時暗号化、そしてウォーターマーク付きクリップのダウンロードを経ても残る ProofMode の来歴情報を搭載しました。[Bitchat v1.7.0](#bitchat-v170-adds-live-push-to-talk-voice-for-dms-and-the-public-mesh) は DM 向けのライブのプッシュトゥトーク音声と、公開メッシュ上での署名付きプッシュトゥトークを追加しました。[MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence) は外部署名者ログインに上限を設け、下書きの永続化を追加し、Vector がグループチャットの仕様から離れたのと同じ週に堅牢化作業を継続しています。

タグ付きリリースには、[n_cord v1.1](#n_cord-v11-adds-nsec-bunker-support) の NSEC Bunker サポート追加、[cdk v0.17.3](#cdk-v0173-adds-nip-47-wallet-service-support-across-cdk-cdk-nwc-and-cdk-ffi) の cdk・cdk-nwc・cdk-ffi 全体にわたる NIP-47 ウォレットサービスサポート追加、[Coop Mobile v0.2.4](#coop-mobile-v024-improves-nostr-connect-and-adds-ncryptsec1-import) の Nostr Connect 改善と ncryptsec1 インポート追加、[Nmail v0.14.0](#nmail-v0140-ships-on-macos-with-scheduled-send-and-push-notifications) の macOS 対応と予約送信、[Nostrord v2.2.0](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages) の DM マスタートグル追加、[Nostr WoT 0.3.86](#nostr-wot-0386-hardens-key-backups-and-signing-prompts) の鍵バックアップの NIP-49 形式への堅牢化、[Keep Android v1.1.8](#keep-android-v118-adds-first-run-frost-onboarding) の初回起動時 FROST オンボーディング追加、[Noscall v0.6.0](#noscall-v060-adds-a-cashu-wallet-and-relay-based-push-notifications) の Cashu ウォレットと relay ベースのプッシュ通知追加、[Kubo](#kubo-ships-tablet-mode-and-group-chat-photos) のタブレットモードとグループチャット写真追加、そして [Nostr Codex Phone v0.2.9](#nostr-codex-phone-v029-adds-gitdiffread-file-helper-requests) の git・diff・ファイル読み取りの補助リクエスト追加が含まれます。

未リリースの側では、[Amethyst](#amethyst-lets-accounts-nickname-contacts-with-encrypted-nip-85-cards) が 54 件のマージ済み PR にわたり、暗号化された NIP-85 カードでアカウントが連絡先にニックネームを付けられるようにしました。[Zap Cooking](#zap-cooking-ships-my-kitchen-phase-3-and-fixes-an-ndk-pool-quorum-bug) は My Kitchen フェーズ 3 を出荷し、NDK プールのクォーラムバグを修正しました。[Kehto](#kehto-streams-outbox-reads-before-relay-discovery) は relay 検出が完了する前に outbox 読み取りをストリーミングします。[Wired と TAO](#wired-and-tao-add-nip-57-creator-revenue-sharing) は NIP-57 のクリエイター収益分配を追加しました。[Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout) は加盟店の注文受信トレイを一時的なゲストチェックアウトを中心に再構築しました。[Buzz](#buzz-hardens-channel-creator-provisioning-around-kind-39002) は 240 件のマージ済み PR にわたりチャンネル作成者のプロビジョニングを堅牢化しました。そして [Nostr Docs](#nostr-docs-adopts-a-nip-49-signer-with-multi-account-and-qr-pairing) は複数アカウントと QR ペアリングに対応した NIP-49 署名者を採用しました。今週新たに追跡対象になったもの: [OpenDiscord v1.0.1](#opendiscord-v101-launches-as-a-discord-style-client-on-nostr)、[Auditable Voting v0.1.140](#auditable-voting-v01140-aligns-organiser-voter-and-audit-proxy-roles)、そして Discovery の選出 [Cambium v0.3.2](#cambium-v032-pairs-with-heartwood-as-a-keyless-nip-55-signer) は、Heartwood ハードウェアコンパニオンにプロキシする鍵を持たない NIP-55 署名者です。

NIPs リポジトリはこの 1 週間で何もマージせず、6 件の提案をオープンしました: [kind:10011 お気に入りフォローセット](#open-kind10011-favorite-follow-sets)、[NIP-4E を拡張するプライベート暗号化ドライブ](#open-private-encrypted-drive-extends-nip-4e)、[NIP-DA 権限付きプライベートデータ共有](#open-nip-da-permissioned-private-data-sharing)、[ステッカーパック kind 10031 と 30031](#open-sticker-pack-kinds-10031-and-30031)、[NIP-29 のメッセージ固定](#open-nip-29-message-pinning-with-kind9010-and-kind39005)、そして [NIP-66 relay 検出の再構成](#open-nip-66-relay-discovery-restructure)。Deep Dive では [NIP-99 と Gamma Markets のコマース拡張](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension) を取り上げます。

---

## 主要ストーリー

### Vector v0.4.0 がグループチャットを Marmot から Concord に移行、数日後に Amethyst が独自の Concord クライアントを出荷

[Vector](https://github.com/VectorPrivacy/Vector) は、DM とグループチャット向けにプライバシー優先のシングルバイナリクライアントを中心に構築された Nostr メッセンジャーです。[Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) はアプリのメッセージングエンジンを共有ライブラリ `vector-core` に書き換え、同じリリースでグループチャットのデフォルトトランスポートである [Marmot](/ja/topics/marmot/)（MLS-over-Nostr）を廃止し、エンドツーエンド暗号化されたコミュニティプロトコル [Concord](/ja/topics/concord-protocol/) に切り替えました。既存の Marmot グループの履歴は引き継がれず、リリースノートはアップグレード前に Marmot グループのデータをバックアップするようユーザーに指示しています。Vector 自身のリリースノートは Concord を「当社独自のメッセージングプロトコル」と説明していますが、基盤となる [CORD-01 から CORD-07 の仕様](https://github.com/concord-protocol/concord) は別途 MIT ライセンスで公開されており、すでに Vector 以外でも実装されています。Soapbox の Discord スタイルクライアント [Armada](https://gitlab.com/soapbox-pub/armada) は同じ Concord 仕様の上に Communities 機能を構築しており、1 日後には [Amethyst が独自のクリーンルーム版でワイヤー互換の Concord 実装をマージしました](https://github.com/vitorpamplona/amethyst/pull/3566)（詳細は後述）。同じ Vector リリースは、すべてのトラフィックに対するオプションの Tor ルーティング、QR または貼り付けた bunker URI による [NIP-46](/ja/topics/nip-46/) リモート署名者ログイン、アプリ内スイッチャー付きの複数アカウント、そしてクライアント間で共有されるカスタム絵文字パックを追加しました。メッセージの削除は DM とグループチャットの双方向でメッセージを削除し、Vector は標準的な [NIP-17](/ja/topics/nip-17/) の削除フローに従わずに一時的な署名鍵を意図的に保持します。これはプライバシーを動機とした逸脱で、プロジェクトはリリースノートで明示的に言及しています。4 日後、[v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1) は **Concord v2** を出荷しました。これは既存の Communities を機能させたままプライバシーと安定性の大幅な改善をもたらすと説明されており、ボット向けの型付きパラメータを備えた Discord スタイルのスラッシュコマンドピッカー、チャットごとの自己破壊タイマー、バグハンター向けの NIP-58 バッジシステムを併せて追加しています。グループチャットの Marmot からの移行は、下記の [MDK v0.9.4](#mdk-v094-bounds-external-signer-login-and-adds-draft-persistence) が同じ週にその仕様へ投資を続けている中で行われました。

### Amethyst がエンドツーエンド暗号化コミュニティ向けにクリーンルーム版 Concord 実装を出荷

[Amethyst](https://github.com/vitorpamplona/amethyst) は機能豊富な Android およびマルチプラットフォームの Nostr クライアントです。[PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566) は [Concord](/ja/topics/concord-protocol/)（CORD-01 から CORD-07）の完全な実装を追加し、サーバーレスでエンドツーエンド暗号化されたコミュニティを対象としています。通常の relay 上での gift-wrap された制御・チャット・ゲストブックの各プレーン、すべてのクライアントがサーバーを信頼するのではなくローカルで検証する所有者を起点としたロールとバンの強制、そして削除されたメンバーを遮断するための再鍵化を含みます。プロトコルと暗号のコードは `quartz/` に、状態とビューモデルは `commons/` に、画面とナビゲーションは Android 向けに `amethyst/` に置かれ、`cli/` の下には薄い CLI 動詞があります。共有ロジックは後で Desktop が採用できるよう `quartz`/`commons` に置かれているため、デスクトップ UI はまだありません。実装はクリーンルーム方式で、公開された CORD 仕様と観測されたワイヤー定数から構築され、Amethyst 独自の MIT ライセンスの下にあり、Armada の AGPL-3.0 コードベースとは別個です。Armada 自身のテストベクトル値が Quartz のユニットテストに移植され、2 つのクライアントが実際にワイヤー上で相互運用できることを確認しました。これにより Concord は数日のうちに 3 つの独立した実装を得ました。最初に出荷した Vector、Soapbox のリファレンスクライアントである Armada、そして今回の仕様からの Amethyst のビルドです。

### Sonar が Bitchat から分離、クロスプラットフォームのアルファ版とステッカーパック仕様を公開

[Sonar](https://sonarprivacy.xyz/) は Bitchat から派生した Bluetooth メッシュと Nostr を組み合わせたメッセンジャー兼ウォレットで、White Noise と相互運用可能な Marmot グループ DM を備えています。コードは [hedwig-corp/bitchat-to-sonar](https://github.com/hedwig-corp/bitchat-to-sonar) にあります。[v0.1-alpha.7](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.7) は Signal スタイルの上限付きトランスクリプトウィンドウ処理を追加し、開閉とスクロールのパフォーマンスをローカルファーストに保ち、近接検出の状態をピア間で同期し、content-type と HTTP ステータスの処理で失敗していた Blossom メディアアップロードを修正しました。先行する [alpha.6](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.6) はより高速なチャット更新のためにライブの Marmot イベントを排出し、通話・メッセージング・ウォレット・プッシュにわたる Android から iOS への機能パリティのギャップを埋めました。Sonar は [PR #2410](#open-sticker-pack-kinds-10031-and-30031) で引用された仕様のソースでもあり、この PR はプロジェクト独自の「Sonar Stickers」仕様の下にステッカーパックのイベント kind を登録し、このローンチに今週のプロトコル作業への直接的なハブリンクを与えています。

### Divine Mobile 1.0.16 がより高度なビデオエディター、保存時暗号化、ProofMode の来歴情報を搭載

[Divine](https://github.com/divinevideo/divine-mobile) は Web-of-Trust によるフィードキュレーションを備えた、Nostr 上に構築されたショート動画クライアントです。[v1.0.16](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.16) は #30 以来初のタグ付きリリースで、ビデオエディターにクリップトランジション、逆再生、ボイスオーバーレコーダー、タイムラインのビートマーカーを追加し、あわせてユーザーがスワイプで直接おすすめを調整でき、不透明なエンゲージメントシグナルに任せずに済むフィード調整コントロールを追加しました。このリリースはローカルデータの保存時暗号化を有効にし、アプリが一時停止されても継続するバックグラウンドアップロードを追加し、ウォーターマーク付きクリップがダウンロードされる際に [ProofMode](/ja/topics/proofmode/) の来歴データを引き継ぎ、人間が作成したことの証明が転送中に取り除かれないようにします。Divine はまた 16 歳未満のアカウント向けの新しい保護を出荷し、ローカライゼーションを 17 言語 284 の翻訳文字列に拡大しました。

### Bitchat v1.7.0 が DM と公開メッシュ向けにライブのプッシュトゥトーク音声を追加

[Bitchat](https://github.com/permissionlesstech/bitchat) は Nostr relay へのオプトインゲートウェイを備えた Bluetooth メッシュチャットアプリです。[v1.7.0](https://github.com/permissionlesstech/bitchat/releases/tag/v1.7.0) は #30 が公開された夜にリリースされ、[PR #1403](https://github.com/permissionlesstech/bitchat/pull/1403) でライブのプッシュトゥトーク音声を追加しました。これは送信者がボタンを押している間に音声をストリーミングし、ストリームが切れた場合はボイスノートにフォールバックします。さらに [PR #1406](https://github.com/permissionlesstech/bitchat/pull/1406) で署名付きの公開メッシュプッシュトゥトークを追加し、共有メッシュチャンネル上のライブ音声バーストが送信者認証を伴うようにしました。このリリースは検証済みの再アナウンスでリンクを再バインドしてピア ID のローテーションを修復し、同じピアを新しい ID の下で認識します（[PR #1401](https://github.com/permissionlesstech/bitchat/pull/1401)）。また現在到達不能なピアへのダイレクトメッセージは、そのまま失敗するのではなく store-and-forward 配信でキューに入るようになりました（[PR #1415](https://github.com/permissionlesstech/bitchat/pull/1415)）。これは #30 で取り上げた v1.6.0 の [NIP-13](/ja/topics/nip-13/) proof-of-work とメッシュ・to・Nostr ゲートウェイ作業から直接続くものです。

### MDK v0.9.4 が外部署名者ログインに上限を設け、下書きの永続化を追加

[MDK](https://github.com/marmot-protocol/mdk) は [Marmot](/ja/topics/marmot/) プロトコル、すなわち #30 が仕様の採択を報じた MLS-over-Nostr メッセージング層のリファレンス SDK です。[v0.9.4](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.4) は [PR #793](https://github.com/marmot-protocol/mdk/pull/793) で、外部署名者ログイン中にクライアントが辿る勧告ディレクトリのステップに上限を設け、リモート署名者が遅いか応答しない場合の無制限のリトライループを防ぎます。同じリリースは [PR #812](https://github.com/marmot-protocol/mdk/pull/812) で下書きメッセージの永続化とプロフィールのウェブサイトバインディングを追加し、MDK が v0.9.0 をカットして以来続けてきた漸進的な堅牢化作業を継続しています。

---

## タグ付きリリース

### n_cord v1.1 が NSEC Bunker サポートを追加

[n_cord](https://github.com/0n4t3/n_cord) は Discord と IRC に触発された Nostr 駆動のチャットクライアントです。[v1.1](https://github.com/0n4t3/n_cord/releases/tag/v1.1) は返信処理のバグ修正とともに [NIP-46](/ja/topics/nip-46/) NSEC Bunker サポートを追加しました。

### cdk v0.17.3 が cdk、cdk-nwc、cdk-ffi 全体にわたる NIP-47 ウォレットサービスサポートを追加

[cdk](https://github.com/cashubtc/cdk) は Cashu 開発キットです。このリリースはほとんどの面で Bitcoin/Lightning のみですが、[v0.17.3](https://github.com/cashubtc/cdk/releases/tag/v0.17.3) は専用の NWC サービス crate、ウォレット統合、`cdk-ffi` 向けの FFI バインディング、そしてエンドツーエンドのテストカバレッジを備えた [NIP-47](/ja/topics/nip-47/)（Nostr Wallet Connect）サービスサポートを追加し、cdk 上に構築された Cashu ウォレットに標準的な Nostr Wallet Connect のサーフェスを提供します。

### Coop Mobile v0.2.4 が Nostr Connect を改善し ncryptsec1 インポートを追加

[Coop Mobile](https://git.reya.su/reya/coop-mobile) はモバイルプラットフォーム向けの [NIP-17](/ja/topics/nip-17/) プライベートメッセージングクライアントです。[v0.2.4](https://git.reya.su/reya/coop-mobile/releases/tag/v0.2.4) は [NIP-46](/ja/topics/nip-46/) Nostr Connect フローを改善し、一部の接続で永続的に止まっていたローディングインジケーターを修正し、再設計されたアイデンティティインポート画面とともに [NIP-49](/ja/topics/nip-49/) `ncryptsec1` 暗号化鍵形式のインポートサポートを追加しました。

### Nmail v0.14.0 が予約送信とプッシュ通知を備えて macOS に対応

[Nmail](https://github.com/nogringo/nostr-mail-client) は Nostr 上に構築されたメールクライアントです。[v0.14.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.14.0) はアプリを macOS に対応させ、キューに入ったメッセージ用の専用「予約済み」メールボックスを備えた予約送信を追加し、プッシュ通知を追加しました。このリリースはまた、アドレス帳の Nostr 識別子解決を独自実装に代えて NDK の [NIP-05](/ja/topics/nip-05/) リゾルバーに切り替えました。

### Nostrord v2.2.0 が DM マスタートグルとより充実したダイレクトメッセージを追加

[Nostrord](https://github.com/nostrord/nostrord) は Android、iOS、ウェブ、デスクトップ向けの [NIP-29](/ja/topics/nip-29/) relay ベースのグループチャットクライアントです。[v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) はすべてのダイレクトメッセージ機能を一度に無効化するマスタートグルを追加し（[PR #175](https://github.com/nostrord/nostrord/pull/175)）、「より充実したダイレクトメッセージ」を出荷しました（[PR #186](https://github.com/nostrord/nostrord/pull/186)）。これは relay プールを統合しゾンビ WebSocket を検出したリリースを取り上げた #30 の内容から続くものです。

### Nostr WoT 0.3.86 が鍵バックアップと署名プロンプトを堅牢化

[Nostr WoT](https://github.com/nostr-wot/nostr-wot-extension) は Nostr アイデンティティと Lightning ウォレットをペアリングするブラウザ拡張機能です。[v0.3.86](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.3.86) は暗号化された鍵バックアップを標準の [NIP-49](/ja/topics/nip-49/) 形式に移し、署名プロンプトが要約ではなくイベント全体とすべてのタグを表示するようにし、relay データを署名に対して検証し、アカウント切り替え時にアクティブなアイデンティティを露出しないようにします。この拡張機能はまた、使用されていない `scripting` ブラウザ権限を削除しました。

### Keep Android v1.1.8 が初回起動時 FROST オンボーディングを追加

[Keep](https://github.com/privkeyio/keep-android) は閾値 FROST 鍵シェアの上に構築された Android 署名者です。[v1.1.8](https://github.com/privkeyio/keep-android/releases/tag/v1.1.8) は FROST 鍵シェアを説明し、最初の署名リクエストが届く前に新規ユーザーが Manual、Basic、Auto の署名ポリシーを選べる初回起動フローを追加しました。これは基盤となる keep-mobile crate の閾値署名モデルに対する Android 側で初のオンボーディングです。

### Noscall v0.6.0 が Cashu ウォレットと relay ベースのプッシュ通知を追加

[Noscall](https://github.com/sanah9/noscall) は Nostr 上に構築された安全な音声・ビデオ通話アプリです。[v0.6.0](https://github.com/sanah9/noscall/releases/tag/v0.6.0-release) は複数 mint 残高、ecash の送受信、そして見積もりの永続化を伴う Lightning の支払いと受け取りを備えたアカウントスコープの Cashu ウォレットを追加しました。このリリースはまた、Android のプッシュ通知を Firebase Cloud Messaging から UnifiedPush 経由の Nostr relay ベースの配信経路に移行し、ログインリトライ中の iOS VoIP と APNs プッシュの信頼性を改善しました。

### Kubo がタブレットモードとグループチャット写真を出荷

[Kubo](https://github.com/JeroenOnNostr/kubo) は Web-of-Trust によるフィードキュレーションを備えた、子どもに安全な Nostr 動画プラットフォームです。[kubo-v2026.07.05](https://github.com/JeroenOnNostr/kubo/releases/tag/kubo-v2026.07.05) は子ども向けフィードのオプトインのタブレットグリッドレイアウトと、グループチャットメッセージへの写真添付のサポートを追加し、さらに Android で画面上のキーボードの後ろにサインアップボタンが隠れる問題を修正しました。

### Nostr Codex Phone v0.2.9 が git/diff/ファイル読み取りの補助リクエストを追加

[Nostr Codex Phone](https://github.com/tidley/nostr-codex-phone) は、暗号化された Nostr DM 経由で通信するローカルのコーディングアシスタントワーカー向けのモバイル制御サーフェスです。[v0.2.9](https://github.com/tidley/nostr-codex-phone/releases/tag/v0.2.9) は git、diff、ファイル読み取り、status、history の補助リクエストを含むモバイル OpenCode ツールアクション、セッションのピン留めと検索の改善、タスク停止コントロールを追加し、あわせて先行する v0.2.8 で出荷された暗号化された [Blossom](/ja/topics/blossom/) アップロードラッパーを備えます。

### GitWorkshop v3.0.3 がリポジトリエクスプローラーで新たにアナウンスされた ref を修正し、初の Android ビルドを出荷

[GitWorkshop](https://github.com/DanConwayDev/gitworkshop) は NIP-34 リポジトリの閲覧とレビューのための git-over-Nostr のウェブ UI です。[v3.0.3](https://github.com/DanConwayDev/gitworkshop/releases/tag/v3.0.3) は、エクスプローラーがすでにロードした後にリポジトリがアナウンスする ref を、ブランチ・タグ・コミット・コード閲覧の各ビューが解決できずに失敗する問題を、CI ワークフローのタイミングの整理とともに修正しました。これはタグとコミット履歴に対して直接確認されています。同じ週に GitWorkshop は [Zapstore](https://zapstore.dev) に初のネイティブ Android ビルドを公開し、v3.0.0 から始まって数時間のうちに v3.0.3 に到達しました。ウェブ UI が主要なインターフェースのままで、Android パッケージは同じ NIP-34 リポジトリ閲覧を初めて携帯電話にもたらします。

### Bitcoin-Safe が Flathub に登場、Nostr Sync & Chat プラグインに注目

[Bitcoin-Safe](https://bitcoin-safe.org) はハードウェア署名者のワークフローを中心に構築されたセルフカストディの Bitcoin ウォレットです。プロジェクトは今週 [Flathub パッケージを出荷](https://flathub.org/apps/org.bitcoin_safe.BitcoinSafe) し、主流の Linux アプリストアへの初の掲載となりました。この Flathub リリースは Bitcoin-Safe の Sync & Chat プラグインをより広い層に届けます。このプラグインはプロジェクト独自の [bitcoin-nostr-chat](https://github.com/andreasgriffin/bitcoin-nostr-chat) ライブラリを介して [NIP-17](/ja/topics/nip-17/) ダイレクトメッセージを使い、ユーザーのデバイス間でウォレットのラベルを同期し、信頼できる参加者間でのリモートマルチシグ共同署名のために PSBT を送受信します。Nostr 層そのものは以前の [2.0.0](https://github.com/andreasgriffin/bitcoin-safe/releases/tag/2.0.0)（2026-06-29）で出荷されており、これは QR、USB、Bluetooth と並ぶ「Share via Chat & Sync」接続タイプを中心にトランザクション署名を再設計しました。今週のニュースは、その既存機能を初めて主流の Linux 層に届ける Flathub パッケージングです。

---

## 未リリースの変更

### Amethyst がアカウントに暗号化された NIP-85 カードで連絡先へのニックネーム付けを可能に

上記で取り上げた [Concord 実装](#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities) に加えて、Amethyst はこの 1 週間で他に 54 件の PR をマージしました。その中心は [PR #3548](https://github.com/vitorpamplona/amethyst/pull/3548) で、アカウントが他のユーザーについて自身の kind 30382 [NIP-85](/ja/topics/nip-85/) 連絡先カードを発行することで、そのユーザーにニックネームを付けられるようにします。ペットネーム、プライベートノート、そして任意のカスタム [NIP-30](/ja/topics/nip-30/) 絵文字ショートコードのマッピングは、カードの [NIP-44](/ja/topics/nip-44/) で暗号化されたコンテンツの中に置かれ、署名アカウントだけがそれらを読めます。カードはログイン時にアカウントの拡張された outbox relay セットを通じて同期され、その後は漸進的に同期されます。フィード、チャット、メンションは公開表示名の代わりにペットネームを表示し、プロフィールページのユーザーの本名の上にタップ可能なニックネームカードを表示します。

### Zap Cooking が My Kitchen フェーズ 3 を出荷し NDK プールのクォーラムバグを修正

[Zap Cooking](https://github.com/zapcooking/frontend) は Nostr 上に構築されたレシピ共有と料理コミュニティのアプリです。「My Kitchen」の献立計画機能を継続する 43 件の PR をマージし、このフェーズで買い物リスト生成、レシピピッカー、プランナーの週グリッドを追加しました。同じ変更セットは、relay のクォーラムがすでに応答した時点を過ぎても relay 読み取りが待機し続ける可能性のある [NDK](https://github.com/nostr-dev-kit/ndk)（Nostr Development Kit）接続プールのクォーラム準備状態のバグを修正しました。

### Kehto が relay 検出の前に outbox 読み取りをストリーミング

[Kehto](https://github.com/kehto/web) は [NIP-5D](/ja/topics/nip-5d/) の Nostr アプレット、すなわち「napplet」のための初期段階のウェブベースランタイムです。26 件の PR をマージしました。[PR #193](https://github.com/kehto/web/pull/193) は、以前は [NIP-65](/ja/topics/nip-65/) の relay リストのロード完了を待ってからでないと relay を一切開かなかった outbox 読み取りを修正します。これにより、決着しない relay リストのロードがイベント配信とクエリのタイムアウトの両方をブロックしうる状態を解消します。修正は検証済みの relay ヒントを即座に開き、書き込み relay が検出されるにつれて結果をストリーミングします。2 つ目の変更（[PR #196](https://github.com/kehto/web/pull/196)）は、プロジェクトのアイデンティティ監査ページを Napplet プラットフォームのライフサイクルコントラクトである NAP-SHELL に整合させます。これは今週の `napplet/web` リリースの他の箇所にも見られる同じプロトコル整合作業の一環です。

### Wired と TAO が NIP-57 のクリエイター収益分配を追加

[Wired](https://github.com/smolgrrr/Wired) と [TAO](https://github.com/smolgrrr/TAO) は Nostr 上に構築された言論の自由に焦点を当てた双子のソーシャルクライアントで、同じ PR リストを共有しています。両者は [PR #121](https://github.com/smolgrrr/Wired/pull/121) をマージし、[NIP-57](/ja/topics/nip-57/) のクリエイター収益分配を実装しました。これにより投稿に送られた zap が元の投稿者以外の貢献者にも自動的に分割されます。これはこのペアが未リリースの作業として proof-of-work シグナルを 21 ビットに引き上げたことを取り上げた #30 の内容から続くものです。

### Conduit Mono が加盟店の注文受信トレイを一時的なゲストチェックアウトを中心に再構築

[Conduit Mono](https://github.com/Conduit-BTC/conduit-mono) は [NIP-99](/ja/topics/nip-99/) の分類広告に隣接するマーケットプレイスプロトコルです。[PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174) はブラウザ生成の一時鍵を使ったゲストチェックアウトを追加します。ゲストはその使い捨て鍵を使って暗号化された注文と支払いレポートを加盟店に送り、加盟店は電話やメールで帯域外にフォローアップするため、購入者は永続的な受信トレイのアイデンティティを一切必要としません。[PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175) は加盟店の注文受信トレイを単一の共有された注文状態モデルを中心に再構築し、購入者と加盟店のロールを分離し、物理的または混合の注文が発送済みに移行する前に追跡コードと配送業者を必須にします。プロジェクトのチェックアウトフローは [NIP-17](/ja/topics/nip-17/) プライベートメッセージ、[NIP-44](/ja/topics/nip-44/) 暗号化、[NIP-59](/ja/topics/nip-59/) gift wrap の上に構築されています。今週の [NIP Deep Dive](#nip-deep-dive-nip-99-and-the-gamma-markets-commerce-extension) は、この同じ注文状態の問題が向かう先である [Gamma Markets](/ja/topics/gamma-markets/) の規約を取り上げます。

### Buzz が kind 39002 まわりのチャンネル作成者プロビジョニングを堅牢化

[Buzz](https://github.com/block/buzz) は AI エージェントと人間を Nostr 上でつなぐ集合知型コミュニケーションプラットフォームです。この 1 週間で 240 件の PR をマージし、kind 44200 のエージェントターンメトリクスを取り上げた #30 からの relay 層の堅牢化の流れを継続しました。今週の修正（[PR #1830](https://github.com/block/buzz/pull/1830)）は、kind 39002 のチャンネルプロビジョニングロジックが実行される前にチャンネルの作成者をメンバーとして扱い、作成者自身のチャンネルがセットアップ中に作成者を拒否しうる競合状態を解消します。

### Nostr Docs が複数アカウントと QR ペアリングに対応した NIP-49 署名者を採用

[Nostr Docs](https://github.com/formstr-hq/nostr-docs) は Nostr ネイティブの共同ドキュメントアプリケーションです。5 件の PR をマージし、注目すべきもの（[PR #50](https://github.com/formstr-hq/nostr-docs/pull/50)）は、複数アカウント切り替えと QR ペアリングを備えた完全な [NIP-49](/ja/topics/nip-49/) 認証のために `@formstr/signer` パッケージを採用し、以前の独自署名経路を置き換えました。

### その他の出荷

いくつかの追跡対象プロジェクトで、個別の段落を割くほどの新しいサーフェスはないものの、署名者の相互運用と信頼性の小さな修正がこの 1 週間で行われました。Nostr ベースの GitHub 代替のコマンドラインクライアント [ngit-cli](https://github.com/DanConwayDev/ngit-cli) は [v2.6.3](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.6.3) を出荷し、`ngit init` が nsec を繰り返し要求する代わりに実行可能なセットアップガイダンスを示すようにしました。Nostr 上に構築されたプライベートな暗号化ノート・ファイルアプリ [Manent](https://github.com/dtonon/manent) は [v1.4.1](https://github.com/dtonon/manent/releases/tag/v1.4.1) を出荷し、Amber が 16 進 pubkey を返すときに壊れていた Android 署名者ログインを修正し、bunker ログインのスクロールを改善しました。スリムで Google サービスを使わない Nostr クライアント [NoorNote](https://github.com/77elements/noornote) は [v1.2.8](https://github.com/77elements/noornote/releases/tag/v1.2.8) を出荷し、見逃していた Nostrord グループの通知を修正し、自己投稿アラートのトグルを追加しました。AI エージェントと人間向けの信頼を意識した Nostr MCP サーバー [Bray](https://github.com/forgesworn/bray) は [v1.34.0](https://github.com/forgesworn/bray/releases/tag/v1.34.0) を出荷し、[NIP-46](/ja/topics/nip-46/) bunker 接続時にクライアント名のメタデータを送るようにしました。Nostr ウェブクライアント [Lumilumi](https://github.com/TsukemonoGit/lumilumi) は [NIP-65](/ja/topics/nip-65/) relay リストをオフラインフォールバックのためにローカルストレージにキャッシュします。Nostr ベースのローカルな都市・コミュニティアプリ [Earthly](https://github.com/moogmodular/earthly) は [NIP-50](/ja/topics/nip-50/) 地理検索を追加します。そして無料でオープンソースの Lightning ウォレット兼アカウントシステム [lnbits](https://github.com/lnbits/lnbits) は [PR #3925](https://github.com/lnbits/lnbits/pull/3925) を出荷し、その他は Lightning に焦点を当てたリリースの中で `send_nostr_dm` を非ブロッキングで発行するようにしました。

---

## 新たに追跡・発見されたもの

### OpenDiscord v1.0.1 が Nostr 上の Discord スタイルクライアントとしてローンチ

[OpenDiscord](https://github.com/sofia-gros/open-discord) は、ロールベースの権限と WebRTC/SFU 音声ロビーを備えた、Nostr 上に構築された Discord スタイルのサーバーとチャンネルのクライアントです。[v1.0.1](https://github.com/sofia-gros/open-discord/releases/tag/v1.0.1) はプロジェクト初のタグ付きインストーラーリリースです。

### Auditable Voting v0.1.140 が主催者・投票者・監査プロキシのロールを整合

[Auditable Voting](https://github.com/tidley/auditable-voting) はクライアントのみの Nostr 投票シェルです。[v0.1.140](https://github.com/tidley/auditable-voting/releases/tag/v0.1.140) は主催者・投票者・監査プロキシのロールを、主催者が署名した正確な公開アンケート定義イベントに整合させ、監査プロキシが古い生成済みアカウントや別のワーカーや主催者から永続化された状態に基づいて動作しうるギャップを解消します。

### Cambium v0.3.2 が Heartwood とペアリングする鍵を持たない NIP-55 署名者に

[Cambium](https://github.com/forgesworn/cambium) は今号の Discovery の選出です。自身のプライベート鍵素材を一切保持せず、すべての署名リクエストを [NIP-46](/ja/topics/nip-46/) 経由でコンパニオンの Heartwood ハードウェア署名者にプロキシする Android [NIP-55](/ja/topics/nip-55/) 署名者です。プロジェクトは追跡対象プロジェクト Bray と GitHub org `forgesworn` を共有しており、Heartwood 自体は Cambium の Android 側が今つないでいる relay-to-serial 署名ブリッジを出荷したものとして #30 で取り上げられました。[v0.3.2](https://github.com/forgesworn/cambium) は承認シートを磨き、選択されたアイデンティティがアプリの既存のバインディングと異なる場合にライブで警告し、アクティビティログの書き込みを単一の非ブロッキングキューに移します。

### 今週さらにローンチ: echoes、Dispatch、Linky

今週はさらに 3 つのローンチが言及に値します。[echoes](https://github.com/Lwb89dev/echoes) はオフラインファーストでエンドツーエンド暗号化されたノートアプリで、Nostr 上でプライベートに同期します。[Dispatch](https://github.com/freecritter/dispatch) はローカルファーストの旅行オーガナイザーで、すべての保存が [NIP-44](/ja/topics/nip-44/) で暗号化され、専用のリンク不可能な鍵の下で Nostr 上にバックアップされます。その [v0.3.0](https://github.com/freecritter/dispatch) リリースは Amber [NIP-55](/ja/topics/nip-55/) ログインを追加し、アプリがユーザーのプライベート鍵に直接触れないようにします。[Linky](https://github.com/hynek-jina/linky) は Nostr の連絡先と DM を Lightning および Cashu の支払いと単一のプログレッシブウェブアプリで組み合わせます。

---

## プロトコル作業と NIP の更新

この 1 週間で [NIPs リポジトリ](https://github.com/nostr-protocol/nips) にマージされた PR はありません。6 件の提案がオープンしました。

### オープン: kind:10011 お気に入りフォローセット

fiatjaf による [PR #2413](https://github.com/nostr-protocol/nips/pull/2413) は kind:10011 お気に入りフォローセットを追加します。これは kind:10012（お気に入り relay セット）が kind:30002 relay セットを指す `a` タグを保持する既存のパターンを反映し、同じお気に入り機構を kind:30000 フォローセットに拡張し、クライアントが自身の連絡先リストを置き換えることなくキュレーションされたフォローリストをブックマークできるようにします。

### オープン: NIP-4E を拡張するプライベート暗号化ドライブ

Form* チームによる [PR #2412](https://github.com/nostr-protocol/nips/pull/2412) は、`d` 識別子タグと `t` サブタイプタグで区別される汎用の Metadata イベント kind 34578 と、その上に構築されたプライベート暗号化ファイルシステムを提案しています。これはすでに Form* 自身のまだ実験的な Form* Drive クライアントで実装されています。ファイルレコードは `t=files` の Metadata イベントです。ファイルの blob は [Blossom](/ja/topics/blossom/) サーバー上に置かれ、暗号化されたインデックスだけが relay に置かれ、各ファイルチャンクは [NIP-44](/ja/topics/nip-44/) v2 の HKDF 由来の暗号化を伴う独自の一時鍵ペアを得ます。コンパニオンの Decoupled Encryption Key イベントは、すべてのファイルのメタデータがそれに対して復号されるドライブ全体で 1 つの対称鍵を保持し、fiatjaf のまだオープンなストレージ抽象化ドラフトである [NIP-4E](/ja/topics/nip-4e/)（[PR #1647](https://github.com/nostr-protocol/nips/pull/1647)、2024 年 12 月からオープン）の上に明示的に構築されています。

そのドライブ全体で 1 つの鍵という設計は、鍵が漏洩するとドライブ内の 1 つのファイルだけでなくすべてのファイルのメタデータが露出することを意味します。ファイルごとの一時鍵ペアはチャンク暗号化鍵だけを変え、メタデータ復号鍵は変えないためです。より古いイベントが失われる可能性があると警告する新しい Metadata イベントを発行する以外に、ローテーションや失効の経路はまだ存在しません。より狭い 2 つ目の提案は、同じ基盤となる NIP-4E のアイデアに別の角度から届きます。fiatjaf による [PR #2361](https://github.com/nostr-protocol/nips/pull/2361) は、特に [NIP-17](/ja/topics/nip-17/) メッセージングの中でアイデンティティ鍵と暗号化鍵を分離し、6 月 1 日からオープンです。両 PR ともマージされておらず、これは設計空間の活発で争点のある領域のままです。Form* は Drive クライアントは実験的で、まもなくアップデートが来ると述べています。

### オープン: NIP-DA 権限付きプライベートデータ共有

JAFairweather による [PR #2411](https://github.com/nostr-protocol/nips/pull/2411) は、スコープ付きデータ許可を通じた権限付きプライベートデータ共有のための新しい NIP-DA ドラフトです。各ユーザーはスコープごとに 1 つの暗号化された権威あるレコードを relay 上に保持し、そのスコープの対称鍵を [NIP-59](/ja/topics/nip-59/) gift wrap の中でプライベートに配信することでアクセスが付与されます。これにより relay は暗号文だけを保存し、誰が誰にアクセスを付与したかを知ることはありません。失効は単なる鍵のローテーションであり、各消費者のコピーを書き換える必要はありません。作者はこれを [NIP-17](/ja/topics/nip-17/) DM（データのスナップショットは運べるがライブ更新や失効は運べない）や NIP-51 プライベートリスト（鍵素材を運ばない）とは別個のものと位置づけ、JavaScript のリファレンスライブラリと go-nostr 上の Go CLI の 2 つの独立した実装を挙げ、relay.damus.io、nos.lol、relay.primal.net に対して相互テストしたとしています。

### オープン: ステッカーパック kind 10031 と 30031

vincenzopalazzo による [PR #2410](https://github.com/nostr-protocol/nips/pull/2410) は、[Sonar](#sonar-splits-off-from-bitchat-with-a-cross-platform-alpha-and-a-sticker-pack-spec) が今週出荷した「Sonar Stickers」形式で規定された kind 30031（アドレス指定可能なステッカーパック）と kind 10031（ユーザーのステッカーパックリスト）を Event Kinds テーブルに登録します。これらの kind は、クライアントがステッカーパックを絵文字セットと取り違えないよう、[NIP-30](/ja/topics/nip-30/) のカスタム絵文字 kind 30030 と 10030 の 1 つ上の枠に意図的に置かれています。ステッカー画像のバイトは HTTPS の [Blossom](/ja/topics/blossom/) 互換サーバー上に置かれ、送信されたステッカーの参照は平文のハッシュを伴い、編集されたアドレス指定可能なパックが古いメッセージですでに送信されたステッカーの見た目を密かに変えられないようにします。コンパニオンの PR が別プロジェクトの `registry-of-kinds` に同じ kind を登録します。

### オープン: kind:9010 と kind:39005 による NIP-29 のメッセージ固定

Anderson-Juhasc による [PR #2379](https://github.com/nostr-protocol/nips/pull/2379) は [NIP-29](/ja/topics/nip-29/) relay ベースのグループにメッセージ固定を追加します。kind:9010 `update-pin-list` は、固定されたイベントの完全なリストを表示順に `e` タグとして運ぶモデレーションイベントで、単一のイベントで固定・固定解除・並べ替え・固定セットのクリアができます。kind:39005 は relay が生成するミラーで、最新の受理済みリストを公開します。この設計は、レビューフィードバックを経て [PR #1163](https://github.com/nostr-protocol/nips/pull/1163) の以前の追加/削除ペア方式に取って代わり、9009 と 39003 がその後 `create-invite` とグループロールに取られたため、kind 番号 9010/39005 を選んでいます。Anderson-Juhasc は [Nostrord](#nostrord-v220-adds-a-dm-master-toggle-and-richer-direct-messages) も保守しており、その [v2.2.0](https://github.com/nostrord/nostrord/releases/tag/v2.2.0) は同じ週に出荷されています。

### オープン: NIP-66 relay 検出の再構成

VincenzoImp による [PR #2241](https://github.com/nostr-protocol/nips/pull/2241) は [NIP-66](/ja/topics/nip-66/) relay 検出の実質的な再構成です。緩い「その他のタグには」という散文を構造化された Indexed Tags セクションに置き換え、relay 検出のフィルタリング向けに NIP-11 の `attributes` フィールドを反映する `W` タグを追加し、標準化された名前空間（`ISO-639-1`、`ISO-3166-1`、`IANA-asn`、`IANA-tz`、`nip66.label.city`）を使う `l` ラベルタグを追加し、RTT、SSL/TLS、ネットワーク、地理、DNS、HTTP のタグを専用セクションに整理し、あわせて新しい Check Types テーブルを設けます。また、誤ったフィールド名、欠けた `kind`、不正なチェックタイプ名を含んでいた壊れた例示イベントを修正し、[issue #2171](https://github.com/nostr-protocol/nips/issues/2171) をクローズします。追加されるタグはすべて任意であるため、すべての変更は後方互換性を保ちます。

---

## NIP Deep Dive: NIP-99 と Gamma Markets のコマース拡張

[NIP-15](/ja/topics/nip-15/)、すなわち元祖の Nostr Marketplace 仕様は、現時点ではレガシーです。これは商店の出店（kind 30017）とその下に整理された商品（kind 30018）をモデル化しており、かつてその上で動いていたクライアント（Shopstr を含む）はその後、アクティブな仕様として [NIP-99](/ja/topics/nip-99/) の分類広告に移行しました。NIP-99 自体は単一のアドレス指定可能なイベントで、アクティブな広告なら kind 30402、下書きなら kind 30403 であり、先に出店を作成する必要はありません。これは広告より先のすべて、すなわち配送費、注文状態、レシート、レビュー、複数の広告を 1 つのストアフロントにまとめる方法を未定義のまま残しています。これらはまさに NIP-15 のうち引き継がれなかった部分です。[Gamma Markets](/ja/topics/gamma-markets/) がその隙間を埋め、今日理解しておく価値のある現代的なコマース層です。

### NIP-99 が残す隙間

NIP-99 広告の `content` フィールドは Markdown の説明を運び、`price` と `location` はイベントに直接乗り、`t` タグは通常のハッシュタグコンテンツとして検索可能にします。pubkey、kind、`d` タグの組でアドレス指定可能なため、売り手は同じ `d` タグで新しいバージョンを発行することで広告をその場で編集します:

```json
{
  "kind": 30402,
  "content": "Vintage mechanical keyboard, Cherry MX Blue switches, barely used.",
  "tags": [
    ["d", "keyboard-mx-blue-01"],
    ["title", "Vintage Mechanical Keyboard"],
    ["summary", "Cherry MX Blue, barely used"],
    ["published_at", "1752537600"],
    ["location", "NYC"],
    ["price", "100", "USD"],
    ["t", "electronics"]
  ]
}
```

それが仕様の全体です。署名された更新可能な分類広告です。一度きりの分類広告を超えて実際の EC のために NIP-99 を実装したすべてのクライアントは、配送、注文メッセージ、レビューのための独自のプライベートな規約を発明することになりました。2 つの NIP-99 クライアントはそれぞれ広告を正しく描画できても、両者間でチェックアウトを完了する共有された方法を持たないことがありえます。

### Gamma Markets: NIP-99 が残したものを標準化する

Gamma Markets は、Nostr マーケットプレイス開発者のワーキンググループ、すなわち Shopstr、Cypher、Plebeian Market、Conduit Market の背後にいるチームが、NIP-99 の既存の kind 30402 イベントの上に構築した共有の EC 規約群に付けた名前です。仕様は [PR #1784](https://github.com/nostr-protocol/nips/pull/1784) を通じて正典の NIP-99 ドキュメントからリンクされ、独自のリポジトリ [GammaMarkets/market-spec](https://github.com/GammaMarkets/market-spec) で保守されています。

Gamma Markets は広告に隣接する 2 つの独立した kind を追加します。kind 30405 は複数の広告を製品コレクションにまとめ、それぞれを明示的な `a` タグで参照します:

```json
{
  "kind": 30405,
  "content": "Summer sale picks",
  "tags": [
    ["d", "summer-picks"],
    ["title", "Summer Sale"],
    ["a", "30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["shipping_option", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

kind 30406 は、国ごとの価格設定と任意の重量ベースまたは距離ベースのコストルールを備えた配送オプションを定義します:

```json
{
  "kind": 30406,
  "content": "Standard Regional Shipping",
  "tags": [
    ["d", "standard-regional"],
    ["title", "Standard Shipping"],
    ["price", "5.99", "USD"],
    ["country", "US"],
    ["service", "standard"],
    ["duration", "24", "72", "H"],
    ["weight-max", "30", "kg"]
  ]
}
```

注文の作成、支払いリクエスト、状態と配送の更新、支払いレシートはすべて、通常の [NIP-17](/ja/topics/nip-17/) gift-wrap されたプライベートメッセージとして流れ、トランスポートを再ラップするのではなくロールごとに 3 つの kind に分割されます。kind 14 は自由形式の購入者/加盟店のコミュニケーションを運び、kind 16 はすべての注文状態遷移を運び（`type` タグの 1 から 4 が注文作成、支払いリクエスト、状態更新、配送更新を表します）、kind 17 は購入者の支払いレシートを運びます。注文作成メッセージは gift-wrapping 前にはこのようになります:

```json
{
  "kind": 16,
  "content": "Please leave the package with the doorman.",
  "tags": [
    ["p", "<merchant-pubkey>"],
    ["subject", "New order"],
    ["type", "1"],
    ["order", "order-8f21"],
    ["amount", "115000"],
    ["item", "30402:<merchant-pubkey>:keyboard-mx-blue-01", "1"],
    ["shipping", "30406:<merchant-pubkey>:standard-regional"]
  ]
}
```

完了した購入の評価は別のアドレス指定可能な kind 31555 で、レビュー対象の広告を指し返します:

```json
{
  "kind": 31555,
  "content": "Arrived fast, exactly as described.",
  "tags": [
    ["d", "a:30402:<merchant-pubkey>:keyboard-mx-blue-01"],
    ["rating", "1", "thumb"],
    ["rating", "1.0", "quality"],
    ["rating", "0.9", "delivery"]
  ]
}
```

注文メッセージを NIP-17 に乗せるということは、Gamma Markets のチェックアウトが、独自の注文メッセージ kind ではなく、クライアントが DM 向けにすでに出荷しているのと同じプライベートメッセージのトランスポートを使うことを意味します。

この仕様の中核的な設計上の選択は、何もカスケードで継承されないことです。コレクションに属する広告は、コレクションの配送オプションや説明を自動的に継承するのではなく、`a` タグで明示的にそれを参照し、広告が使う配送オプションも同じ明示的な方法で参照されます。これは、商品が親の出店が定義した通貨と配送テーブルを密かに継承していた NIP-15 の出店モデルの意図的な逆転です。トレードオフは各広告でより多くの明示的なタグ付けをすることであり、その代わりに広告の完全な設定が常にイベントそのものから読み取れ、先に解決すべき親オブジェクトがないことです。

### これが実践で現れる場所

今週の [Conduit Mono](#conduit-mono-rebuilds-the-merchant-orders-inbox-around-ephemeral-guest-checkout) の作業は、Gamma Markets が標準化するのと同じ注文メッセージの領域にあります。[PR #174](https://github.com/Conduit-BTC/conduit-mono/pull/174) の一時鍵ゲストチェックアウトと [PR #175](https://github.com/Conduit-BTC/conduit-mono/pull/175) の加盟店注文受信トレイの再構築は、いずれも Gamma Markets の kind 14、16、17 のメッセージが形式化する購入者/加盟店の注文状態の問題を解決します。Conduit Mono はそれらの kind を直接採用せず、それらと並行して独自の注文状態モデルを動かしています。仕様を書いた 4 つのプロジェクトのうちの 1 つである Shopstr も、この 1 週間で独自のコマース配管を動かし続けました。[PR #568](https://github.com/shopstr-eng/shopstr/pull/568) は重複した NIP-17 gift-wrap ロジックを共有モジュールに抽出し、[PR #567](https://github.com/shopstr-eng/shopstr/pull/567) は [NIP-98](/ja/topics/nip-98/) HTTP 認証パーサーを完全なテストカバレッジにします。これはまさに、Gamma Markets の注文フローが購入者と加盟店に安全に届くために依存するメッセージングと認証の層に対する保守作業です。

NIP-15 は出店と商品を標準化しながら、支払い、配送、レビュー、注文状態をアプリケーションの問題として残したことで、ストアフロントの役割を失いました。Gamma Markets は NIP-99 の単一広告の形に手を触れることなく、その欠けたサーフェスの大部分を埋め、新しいメッセージング層を発明するのではなく、Nostr の既存の DM スタックである NIP-17 の上に構築します。

---

今週はここまでです。何かを作っていたり、共有したいニュースがあれば、NIP-17 DM で連絡するか、Nostr で私たちを見つけてください。
