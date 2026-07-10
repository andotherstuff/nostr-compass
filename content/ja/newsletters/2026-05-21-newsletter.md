---
title: 'Nostr Compass #23'
date: 2026-05-21
publishDate: 2026-05-21
draft: false
type: newsletters
translationOf: /en/newsletters/2026-05-21-newsletter.md
translationDate: 2026-07-01
---

Primal 3.5は再構築されたAndroidシェルを出荷し、Amethystはオンチェーンbitcoin zapを追加、White Noiseはmarkdownレンダリングとディープリンクを獲得、Keycastはセキュリティ監査に合格し、AgentNoiseはMarmot暗号化チャットでローカルAIコーディングエージェントを制御できるようにします。HostrはNostr上のP2P賃貸宿泊プラットフォームをローンチし、リスティング、予約、EVMベースのエスクローをカバーする4つの草案NIPを備えます。AngorはNIP-04からNIP-44への暗号化メッセージング移行を行い、Dart NDKはNIP-77とwebサイナーを追加し、Alby js-sdk v8はネイティブNWCマルチリレー再接続を出荷し、KeyChatはSignal one-time prekey削除における前方秘匿性のギャップにパッチを当てます。プロトコル面では、Mostroのanti-abuseボンドがフェーズ2に到達し、Wispはプライベート返信とgift-wrappedリアクションを出荷、Namecoin NIP-05実装ウェーブが1週間で半ダースのクライアントに触れます。

## トップストーリー

### Android版Primal 3.5

独自のキャッシュリレーインフラに支えられたソーシャルクライアントであるPrimalは、今週再構築されたアプリケーションシェルを備えた[3.5.9](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.9)を出荷しました。再設計は、以前のナビゲーション構造を更新されたレイアウトと新しいExplore画面に置き換え、メインの発見面に専用のホームを与えます。このリリースはリンクプレビューのオーディオ再生を追加し、ノートに埋め込まれたオーディオファイルはフィードを離れることなくインラインで再生されます。NIP-05検証バッジがプロフィール上でインライン表示され、一目でアイデンティティ確認を表面化します。通知フィルタリングは刷新され、ユーザーは通知リストに届くイベントタイプを絞り込むことができます。エディタはより良いイベントリンク処理を獲得し、基盤のデータベースレイヤーは安定性の修正を受けました。

### White Noise: markdown、ディープリンク、オーディオメタデータ

NostrとMLS ([RFC 9420](https://www.rfc-editor.org/rfc/rfc9420))上に構築されたMarmot暗号化グループメッセージングアプリであるWhite Noiseは、フロントエンドとバックエンドのリポジトリでこれまでで最も忙しい週の1つを迎えました。

フロントエンドでは、[PR #665](https://github.com/marmot-protocol/whitenoise/pull/665)がチャットメッセージ用の完全なmarkdownレンダリングを追加し、太字、斜体、コードブロック、リンクがメッセージビューでネイティブにレンダリングされるようになりました。[PR #675](https://github.com/marmot-protocol/whitenoise/pull/675)は、これまで最後の管理者以外にブロックされていたグループ退出フローを有効化し、[PR #661](https://github.com/marmot-protocol/whitenoise/pull/661)はHTTPリダイレクトインフラを必要とせずに、ユーザー、チャット、および設定をカバーする`whitenoise://`および`whitenoise-staging://` URIのネイティブディープリンクサポートを追加します。

バックエンドのwhitenoise-rsでは、[PR #835](https://github.com/marmot-protocol/whitenoise-rs/pull/835)がkind:30443発行のために`d_tag`スロットを再利用することでキーパッケージのローテーションが適切に機能するようにし、NIP-33置換可能イベントセマンティクスを有効にして、連続するキーパッケージのローテーションがリレー上の以前のイベントを置き換え、現在のキーパッケージだけを保持するようにします。[PR #833](https://github.com/marmot-protocol/whitenoise-rs/pull/833)は、オーディオ添付ファイル用のオプションの`duration_ms`および`waveform`フィールドで`FileMetadata`を拡張し、MDKの[PR #300](https://github.com/marmot-protocol/mdk/pull/300)と協調して同じフィールドをMIP-04メディアタグに追加します。新しい`whitenoise-markdown` crate ([PR #836](https://github.com/marmot-protocol/whitenoise-rs/pull/836))は、以前のnostr-sdkトークンパーサを専用のmarkdownレンダリングライブラリに置き換えます。

Marmotプロトコル仕様自体は、[PR #68](https://github.com/marmot-protocol/marmot/pull/68)でセキュリティ修正を受け、MIP-01の画像キー派生のためにHKDF-SHA256を明示的に指定することでセキュリティ問題を閉じ、実装の分岐につながる可能性のあった曖昧さを取り除きました。MDKでは、[PR #307](https://github.com/marmot-protocol/mdk/pull/307)がwelcome失敗理由をサニタイズし、保存長を制限して、別のセキュリティ発見を閉じました。

### Amethyst v1.10.0: オンチェーンbitcoin zap

Amethystは今週4つのリリースを出荷し、[v1.10.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.10.0)を目玉としました。このリリースはNIP-BCオンチェーンbitcoin zapのサポートを追加し、ユーザーがbitcoinトランザクションを介してオンチェーンで直接決済されるzapを送信、受信、表示できるようにします。実行中の以前のリリースは、非準拠のファイル名を拒否するようにBlossom blob検出を修正し ([v1.09.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.09.2))、デスクトップビルド用のProGuardルールにパッチを当て、拡張されたリアクションギャラリーで専用の₿行としてオンチェーンbitcoin zapper表示するプルリクエスト[#2977](https://github.com/vitorpamplona/amethyst/pull/2977)をマージしました。ページング付きの進行中のオンチェーントランザクション履歴画面が[PR #2974](https://github.com/vitorpamplona/amethyst/pull/2974)でランディングしました。

### AgentNoise: White Noise経由でコーディングエージェントを制御

nvkによる[AgentNoise](https://github.com/nvk/agentnoise)は、White Noiseを実行するスマートフォンをローカルのCodexおよびClaudeコーディングエージェントセッションのコントロールサーフェスとして使用できるようにするRustネイティブのデスクトップヘルパーです。このツールは1つ以上のWhite Noiseチャットを聞き、初回ペアリングPINフローで送信者を認証し、設定されたランチャーを介してローカルコーディングエージェントを起動します。スマートフォンから`/claude <prompt>`を送信すると、マシンホスト名と短いプロンプト要約にちなんで名付けられた新しいWhite Noise作業セッションが開かれ、進捗更新と最終出力がそのチャットにストリーミングされます。意図的にRustファーストで、Nodeを信頼できるブリッジパスから遠ざけています。プロジェクトは今週[v0.1.24](https://github.com/nvk/agentnoise/releases/tag/v0.1.24)に到達し、より短いスマートフォン読み取り可能な応答、短い一意のプレフィックスによるジョブ参照、およびオプトインのローカルセッションウォッチャを追加しました。AgentNoiseは`marmot-protocol/whitenoise-rs`から`wn`および`wnd` CLIをサブプロセスとして駆動するため、White Noiseクライアント自体とNostrトランスポートを共有します。

### Keycastセキュリティ監査完了

SQLite内で保存時に暗号化されたNostr秘密鍵を保存するチーム指向のNIP-46リモート署名サーバである[Keycast](https://github.com/marmot-protocol/keycast)は、2026年5月にセキュリティ監査を完了しました。強化パスは認証、権限、データ整合性、および依存関係の問題に取り組み、結果は[AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md)に文書化されています。変更内容: NIP-98 HTTP認証は今、正確に1つの`u`タグと1つの`method`タグを必要とし、古いタイムスタンプを拒否し、`payload`ハッシュを検証します。`ALLOWED_PUBKEYS`許可リストは正確に解析され、サーバ側で強制されます。空のポリシーはsign/encrypt/decryptリクエストをデフォルトで拒否します。SQLite接続で外部キー強制が有効化されます。`/teams/:id`などのネストされたアプリルートはサーバ側で保護されます。SQLマイグレーションは、起動時に古い許可kinds権限JSONを正規化します。プロジェクトはまだ初期段階であり、監査は実際のチーム鍵を委ねる前の残存項目を記録しています。

### Scramble: デスクトップとAndroid向けMarmotクライアント

[Scramble](https://github.com/DavidGershony/Scramble) (旧OpenChat)は、[Marmotプロトコル](/ja/topics/marmot/)用の.NET/Avaloniaデスクトップおよびandroidクライアントで、MIP 00-04を実装します: KeyPackage発行 (kind:30443)、NostrGroupData MLS拡張を伴うグループメタデータ、NIP-59 gift-wrapped welcomeイベント (kind:444)、ChaCha20-Poly1305暗号化メッセージ (kind:445)、およびBlossom暗号化メディア添付。White Noiseおよびその他のMarmot互換クライアントと完全に相互運用可能です。

プロジェクトは今週13のリリースを出荷し、マルチデバイスサポートを主な機能としました。各デバイスは一意のKeyPackageスロット (kind:30443の`d`タグ)を生成します。起動時、Scrambleはリレーからユーザー自身のKeyPackageを取得し、ピアデバイスのスロットIDを検出し、staged commitフローを使用して既存のMLSグループに自動的に追加します。自動追加は、現在のユーザーが管理者であるグループに制限されており、管理者でないグループはグループ管理者に依頼するようにガイダンスが表示されてスキップされます。前方秘匿性の開示バナーは、新しくリンクされたデバイスに古いメッセージが利用できないことを通知します。スロットID調整パス (`TryReconcileSlotId`)は、リレーKeyPackageバイトをローカルキーマテリアルと照合して正しい`d`タグを採用することで、マルチデバイス以前のバージョンから移行したデバイスを処理します。AmberおよびNIP-46ユーザー向けの外部signer再接続も修正されました: `ExternalSignerService`の組み込み自動再接続をブロックしていた`IsConnected`ガードが、`NostrService`内の9つのすべての呼び出しサイトで削除されました。

### Hostr: Nostr上のP2P賃貸宿泊

[Hostr](https://hostr.network) ([ソース](https://github.com/sudonym-btc/hostr))は、完全にNostr上に構築されたピアツーピアの賃貸宿泊プラットフォームです。物件の検索とリスティング、予約の交渉、支払いの決済といった、完全なAirbnbスタイルのフローをカバーし、プロジェクトがアプリケーションと並行して開発している4つの草案NIPを使用します。

宿泊NIPは、[NIP-99](https://github.com/nostr-protocol/nips/blob/master/99.md)クラス分けリスティング (kind:30402アクティブ、kind:30403草案)を、タイプ (`room`、`house`、`apartment`、`villa`、`hotel`、`hostel`、`resort`)、チェックイン/チェックアウト時間、最小滞在、および設定可能な精度で位置ベース検索を行うためのH3地理空間セルインデックスなどの宿泊固有のタグで拡張します。予約NIPは完全な交渉およびライフサイクルプロトコルを定義します: kind:32122置換可能予約イベントは`d`トレードID、リスティングアンカー`a`タグ、および役割 (`buyer`、`seller`、`escrow`)を持つ参加者`p`タグを運びます。kind:1327構造化メッセージrumorは、NIP-59 gift wrapを介してプライベート交渉段階のカウンターオファーを配信し、交渉が公開リレーから離れて留まるようにします。kind:1326追記専用遷移イベントは、予約がコミットされたら公開監査証跡を作成します。買い手のプライバシーは、暗号化された`participant_proof`タグを介して買い手の実際のアイデンティティにバインドされたトレードごとの一時的なNostr鍵を通じて保持されます。エスクローNIPはkind:30303エスクローサービス広告およびkind:17388ユーザー信頼宣言を定義します。リファレンス実装はRootstock上のEVMスマートコントラクトを使用し、`contractBytecodeHash`によってクライアントはデプロイされた契約が既知の監査済み実装と一致することを検証できます。マーケットプレイスリスティングNIPは、`instantBook`、`negotiable`、`quantity`、`securityDeposit`、`cancellationPolicy`、`maxDisputePeriod`を含む、すべてのNIP-99マーケットプレイスプロフィールで共有されるジェネリックタグを定義します。今週、プロジェクトはアプリストア提出を準備し、エージェント向け自動化のためのMCPクライアントアイデンティティサポートをマージしました。

今週、Shakespeare MiniAppsプラットフォーム上に2つの新しいエントリが登場しました: 構造化された雑誌スタイルのコンテンツをNostrイベントとして発行するAI雑誌ジェネレータ[InkPress](https://inkpress.shakespeare.wtf)と、Soapboxスタック用の執筆・発行プラットフォーム[PressStr](https://pressstr.shakespeare.wtf)です。

## 今週の出荷

### ngit v2.4.4

**ngit**は[v2.4.4](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.4)を出荷し、gitサーバがNostr状態よりもfast-forward先行しているケース向けに`ngit sync --trust-server` (`-t`)を追加しました。この状況が検出されると、syncは影響を受けるrefを報告し、更新された状態イベントに署名して発行するためにこのフラグを要求します。`nostr.trust-server-domains` git設定は、フラグなしで自動的に信頼されるべきサーバのセミコロン区切り許可リストを提供します。

### Amber v6.1.0-pre3がPSBT署名を追加

**Amber**は[v6.1.0-pre3](https://github.com/greenart7c3/Amber/releases/tag/v6.1.0-pre3)をリリースし、新しいアプリ接続用の改善されたレイアウト、クラッシュ修正、および権限画面での全選択/全選択解除オプションを備えました。[PR #438](https://github.com/greenart7c3/Amber/pull/438)は、Intentベースの経路とNIP-46リレーベースの経路の両方を通じてPSBT署名サポートを追加し、Amberが要求元のアプリにnsecを公開することなく、Partially Signed Bitcoin Transactionに署名できるようにします。

### Wisp v1.1.0がプライベート返信を出荷し、Amberサポートを削除

**Wisp**は[v1.1.0](https://github.com/barrydeen/wisp/releases/tag/v1.1.0)をリリースし、NIP-17 gift wrap経由のプライベート返信 ([PR #540](https://github.com/barrydeen/wisp/pull/540))、プライベート返信でのgift-wrappedリアクションとDIP-03 zap ([PR #543](https://github.com/barrydeen/wisp/pull/543))、ノートの自動翻訳 ([PR #523](https://github.com/barrydeen/wisp/pull/523))、およびzapダイアログのレジスタスタイルの法定通貨入力を備えました。[PR #541](https://github.com/barrydeen/wisp/pull/541)は、プライベートzapを自家製のDMリレー平文スキームから適切なDMリレールーティングを備えたDIP-03に移行します。同じリリースサイクルでNIP-55リモートsignerサポートが削除され ([PR #531](https://github.com/barrydeen/wisp/pull/531))、Amberおよびその他の外部signer統合が削除され、同梱のローカルリレーも削除されました ([PR #533](https://github.com/barrydeen/wisp/pull/533))。WispはAndroid向けNostrソーシャルクライアントです。

### Calendar by Formstr v1.5.4が新規参加者向けgift wrapを修正

**Calendar by Formstr**は[v1.5.4](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.5.4)を出荷しました (v1.5.2 → v1.5.4シーケンスの最新)。[PR #160](https://github.com/formstr-hq/nostr-calendar/pull/160)は、新規参加者を伴うプライベートカレンダーイベントを編集すると、更新されたイベントが`p`タグに新しいpubkeyで発行されるが、それらの参加者にgift wrap招待が作成または配信されないというバグを修正し、直前追加向けの招待フローを壊していた問題を解決します。[PR #156](https://github.com/formstr-hq/nostr-calendar/pull/156)はプライベートイベント復号周りのエラー処理を追加し、クライアントが復号不可能なイベントで例外をスローしなくなります。[PR #138](https://github.com/formstr-hq/nostr-calendar/pull/138)はタイムゾーンをまたいでドリフトしていた定期イベント時刻を修正します。

### Applesauce v6.1.0がNIP-34 gitキャストとNIP-51ルックアップリレーを追加

**Applesauce**はパッケージ全体で[v6.1.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%406.1.0)をリリースし、重要なNIP-34 (git-over-Nostr)サポートを備えました: applesauce-commonは新しい`GitRepository`、`GitGraspList`、`FavoriteGitRepos`キャストと対応するファクトリを追加し、`User.favoriteGitRepos$`、`User.gitAuthors$`、`User.graspServers$`リアクティブプロパティを公開し、アプリケーションが同じUserオブジェクトから直接、ユーザーがフォローするgitリポジトリ、リポジトリメンテナ、および設定されたGRASPサーバをリストできるようにします。同じリリースは、特定のデータを見つける場所を発見するために使用されるリレーリストファミリへの最近の追加である、NIP-51 kind 10086ルックアップリレーリストのサポートを追加します。applesauce-coreは、NIP-01置換可能アドレスルックアップのために`EventCast`上に`replaceableAddress`を得て、`pointer`、`kind`、および`getReplaceableAddressForEvent`ヘルパーを備え、ベースの`User`キャスト上に`timeline$()`メソッドを追加します。[PR #73](https://github.com/hzrd149/applesauce/pull/73)は、poolのマニュアルメソッドがオフラインリレーを黙って削除する問題を修正します。

### Sprout v0.0.16がSprigバイナリとhuddleプロトコルv2を出荷

BlockによるNostrリレーベースのセルフホストチームワークスペースで、人間とAIエージェントが同じ部屋とイベントログを共有する**Sprout**は、デスクトップアプリの[v0.0.16](https://github.com/block/sprout/releases/tag/v0.0.16)を、新しいSprigオールインワンバイナリ ([PR #605](https://github.com/block/sprout/pull/605))のローリングビルドと並行して出荷しました。SprigはACPハーネス、エージェント、および開発者MCPを単一のbusyboxスタイルバイナリにバンドルし、デプロイを容易にします。[PR #611](https://github.com/block/sprout/pull/611)で追加された`--no-memory`フラグは、オペレータがACPハーネス用のNIP-AEコアメモリ注入を無効化できるようにします。リアルタイム面では、[PR #609](https://github.com/block/sprout/pull/609)がhuddle音声プロトコルを、最大10の同時ピアをサポートするv2フレームヘッダに拡張します。

### Nostrord v1.0.3がOSキーチェーンとマルチアカウントを追加

**Nostrord**は[v1.0.3](https://github.com/nostrord/nostrord/releases/tag/v1.0.3)をリリースし、OSキーチェーンとパスフレーズフォールバックで強化されたローカルキーストレージ、マルチアカウントサポート、およびAndroid上でsignerアプリを開くタップ可能なbunker QRコードを備えました。

### AngorがNIP-44に移行し、セキュリティ強化を出荷

Nostrとタップルート上に構築されたbitcoinクラウドファンディングアプリである**Angor**は、今週セキュリティ強化とNostr統合の変更のセットを備えた3つの不安定版リリース ([v0.2.24](https://github.com/block-core/angor/releases/tag/v0.2.24)、[v0.2.25](https://github.com/block-core/angor/releases/tag/v0.2.25)、[v0.2.26](https://github.com/block-core/angor/releases/tag/v0.2.26))を出荷しました。[PR #860](https://github.com/block-core/angor/pull/860)は、Nostr暗号化メッセージングをNIP-04からNIP-44に移行し、非推奨のXORベースのスキームをChaCha20-Poly1305暗号化に置き換えます。[PR #861](https://github.com/block-core/angor/pull/861)は、エフェメラルなNostr認証キーを使用して、選択されたウォレットなしでBlossomメディアのアップロードを許可し、まだウォレットを接続していないユーザーのアップロードを解除します。セキュリティシリーズはいくつかの強化カテゴリに対処しました: [PR #854](https://github.com/block-core/angor/pull/854)はAngorKeyの型安全性とニーモニックメモリ保護を追加し、[PR #856](https://github.com/block-core/angor/pull/856)はタイムロック、手数料率、ダスト閾値、およびペナルティルールのためのプロトコルレベル検証を強制し、[PR #851](https://github.com/block-core/angor/pull/851)は8つの中および低重大度カテゴリにわたって非破壊的強化を適用します。[PR #859](https://github.com/block-core/angor/pull/859)は、AOTコンパイルを有効化しランタイムコード生成を削除することでGrapheneOS互換性を修正し、[PR #855](https://github.com/block-core/angor/pull/855)は、OSがプロセスを終了する前にウォレット状態を永続化することでAndroidスワイプキルでのウォレット損失を防ぎます。

### Alby js-sdk v8.0がNWCマルチリレー再接続を出荷

**Alby js-sdk**は、NWCマルチリレーサブスクリプションサポートを備えたv8.0ライン ([v8.0.1](https://github.com/getAlby/js-sdk/releases/tag/v8.0.1)から[v8.0.3](https://github.com/getAlby/js-sdk/releases/tag/v8.0.3))をリリースしました。[PR #516](https://github.com/getAlby/js-sdk/pull/516)は、nostr-tools依存関係を更新し、複数のリレーにわたるネイティブ自動再接続を有効化し、以前のポーリングアプローチをリレーネイティブの再接続ロジックに置き換えます。[PR #542](https://github.com/getAlby/js-sdk/pull/542)は、すべての`console.debug`呼び出しを注入可能なロガーインターフェースに置き換え、アプリケーション開発者がSDK診断を独自のロギングインフラを介してルーティングできるようにします。このリリースはWebSocketポリフィルを削除し、サーバサイドのコンシューマにはNode.js 22以上を必要とします。v8.0.2は、一部のバンドラを壊していたutils crypto importバグの修正を追加しました。

### KeyChat v1.41.1が前方秘匿性を修正

Signalプロトコルと Nostrリレートランスポートを組み合わせたメッセージングアプリである**KeyChat**は、[v1.41.1+6513](https://github.com/keychat-io/keychat-app/releases/tag/v1.41.1+6513)をリリースしました。目玉の修正は、成功した復号後にSignal one-time prekeyを直ちに削除することで前方秘匿性を強制し、デバイスが後に危殆化された場合に保持されたprekeyが過去のメッセージを復号するために使用される可能性があるギャップを閉じます。このリリースはまた、単一のリンクで構成されるメッセージのURLプレビューを追加し、20 MBの自動閾値を持つ新しい`FileDownloadManager`の下でメディア自動ダウンロードを集中化し、NIP-11リレー情報のフェッチをリファクタリングしてコールドスタートで強制リフレッシュし、有料リレー料金設定が常に正しく読み込まれるようにします。

## 開発中

**Citrine**は、NIP-70強制を実装する[PR #151](https://github.com/greenart7c3/Citrine/pull/151)をマージしました: Androidリレーは今、仕様が要求するように、保護されたイベントコンテンツを埋め込むリポストをブロックします。[PR #149](https://github.com/greenart7c3/Citrine/pull/149)は、リレー設定画面から複数の接続アドレス、localhost、ローカルWi-Fi、およびTorのための表示およびコピーアクションを追加します。[PR #141](https://github.com/greenart7c3/Citrine/pull/141)は、Amberとの外部signer統合を通じてNIP-42 AUTHチャレンジ処理を追加します。

**Mostro**は、anti-abuseボンドロールアウトのフェーズ2に到達しました。[PR #737](https://github.com/MostroP2P/mostro/pull/737)は、solver指向の紛争スラッシュロジックをランディングします: 管理者ハンドラは今、mostro-coreからの`BondResolution`ペイロードを消費し、管理者が紛争を解決する際にいずれかの当事者のボンドをスラッシュできるようにします。[PR #736](https://github.com/MostroP2P/mostro/pull/736)でマージされたフェーズ1.5は、専用の`PayBondInvoice`アクションと`WaitingTakerBond`ステータスを導入し、テイカーのanti-abuseボンド支払いを買い手のトレードペイアウトから分離しました。モバイルクライアントは、[PR #592](https://github.com/MostroP2P/mobile/pull/592)で完全なフェーズ1.5 UXを追加しました。MostroはNostr上に構築されたピアツーピアbitcoin取引プロトコルです。

**Damus**は、リレーシグナルインジケータを復元する[PR #3773](https://github.com/damus-io/damus/pull/3773)をマージし、[PR #3775](https://github.com/damus-io/damus/pull/3775)は初回接続失敗後に再接続を拒否したリレーを修正します。

**rust-nostr**は、イベント最終化トレイトとNIP固有のイベントビルダを追加する[PR #1358](https://github.com/rust-nostr/nostr/pull/1358)をマージし、特定のプロトコル機能向けに正しく型付けされたイベントを構築しやすくします。[PR #1363](https://github.com/rust-nostr/nostr/pull/1363)は、NIP-46 signerがconnectレスポンスを送信する前に通知にサブスクライブすることを保証する修正をバックポートし、connect直後に到着するクライアントメッセージが失われる可能性のある競合条件を閉じます。

**dart-nostr**は、Namecoin `.bit`リレーリゾルバとTLSAピンレコードを追加する[PR #44](https://github.com/ethicnology/dart-nostr/pull/44)をマージし、Flutterアプリケーションが`wss://example.bit/`リレーURLをNamecoin DNS経由で実際のWebSocketアドレスに解決できるようにします。

**Dart NDK** (Dart/Flutter Nostr開発キット、現在は`relaystr/ndk`)は、オフラインイベント署名プロトコルであるNIP-77を実装する[PR #464](https://github.com/relaystr/ndk/pull/464)をマージしました。signer側では、[PR #602](https://github.com/relaystr/ndk/pull/602)および[PR #601](https://github.com/relaystr/ndk/pull/601)がwebフィックスのイベントsignerと`PlatformEventVerifier`抽象を追加し、Flutter webアプリが別のコードパスなしでプラットフォームsignerを使用できるようにします。[PR #604](https://github.com/relaystr/ndk/pull/604)は、ランタイムsigner選択のためのイベントsignerファクトリを導入します。[PR #608](https://github.com/relaystr/ndk/pull/608)はユーザーのNIP-17 DMリレーリスト (kind:10050)を取得する`getDmRelays()`を追加し、[PR #600](https://github.com/relaystr/ndk/pull/600)はNIP-46署名済みフィールド保持を修正して、リモートsignerがラウンドトリップでフィールドを失わないようにします。

**Pages by Form\*** ([リポジトリ](https://github.com/formstr-hq/nostr-docs))はFormstrのNostrネイティブ共同ドキュメントアプリで、[pages.formstr.app](https://pages.formstr.app)でホストされ、今週暗号化添付およびドキュメント管理フローを引き締める4つのPRをマージしました。[PR #37](https://github.com/formstr-hq/nostr-docs/pull/37)は、暗号化添付をインライン化することでDOCX、HTML、およびPDFエクスポートの欠落画像を修正します: Blossomサーバから`<encrypted-file>` blobを取得し、保存された鍵とnonceを使用してAES-GCM 256ビットで復号し、画像MIMEタイプを検証し、base64データURLに変換して、暗号化された形式でBlossom上にのみ存在する画像がエクスポートで保持されるようにします。[PR #39](https://github.com/formstr-hq/nostr-docs/pull/39)はローカルドキュメント検索メカニズムを追加し、[PR #38](https://github.com/formstr-hq/nostr-docs/pull/38)はリネームフローを整理し、[PR #40](https://github.com/formstr-hq/nostr-docs/pull/40)は共有バックアップ処理を修正します。

**Zap Cooking**は、まだユーザーに見える変化なしにフィードレンダリングプリミティブを敷設するフィード刷新の第一フェーズである[PR #396](https://github.com/zapcooking/frontend/pull/396)をマージしました。このPRは、`url`、`m` (MIME)、`dim` (寸法)、`blurhash`、`alt`、`x` (ファイルハッシュ)、および`fallback`スロットを読み取るNIP-92 `imeta`タグパーサ、および手動でポートされた正規のblurhashデコーダ (~200 LOC)を導入し、SSRセーフなnullフォールバックを持つcanvas経由でPNGデータURLを生成します。`imeta`タグがない場合、パーサは現在のフィードがすでに使用しているのと同じヒューリスティックを使用してイベントコンテンツから生の画像およびビデオURLを抽出するフォールバックを行います。

**Nurunuru** (ぬるぬる、`tami1A84/null--nostr`)は、Rust FFIエンジンを共有するネイティブAndroid、iOS、およびWebバリアントを持つNostrクライアントで、[PR #176](https://github.com/tami1A84/null--nostr/pull/176)でv1.5.0 Native → Web同期をマージしました。この同期は、Android v1.4.9およびiOS 1.0.4ですでに出荷されたいくつかの機能追加をWebビルドにもたらします: [NotificationModal](https://github.com/tami1A84/null--nostr/pull/176)は今、誕生日通知、相互フォローzap検出、およびカスタム絵文字リアクション通知を表面化します。リアクションピッカーはUnicodeデフォルトリアクションクイック行を削除し、UXをカスタム絵文字に集中させます。`lib/recommendation.js`の推奨エンジンはアイコンや表示名のないユーザーをフィルタリングし、Followingエントリを優先し、Recommendedはバックグラウンドで読み込みます。音声入力は反対方向に進む唯一の機能です: WebビルドはすでにElevenLabs Scribeストリーミングを使用しており、v1.5.0はNative側をOS標準の`SpeechRecognizer` (Android)および`SFSpeechRecognizer` + `AVAudioEngine` (iOS)に部分同期しますが、完全なNative Scribe統合はv1.6に延期されます。

## プロトコルおよび仕様作業

**PR [#2251](https://github.com/nostr-protocol/nips/pull/2251)**はNIP-70保護イベント仕様を引き締めます: 今、保護されたイベントの完全なコンテンツを埋め込むリポストはリレーによって拒否されなければならないと明示的に述べます。NIP-70は、ノート作成者が自分のノートの再発行に同意しないことを示す`-`タグを定義します。元の仕様はリレーフィルタリングの動作をカバーしていましたが、リポストの場合は曖昧なままでした。このPRはそのギャップを閉じます。Citrineの[PR #151](https://github.com/greenart7c3/Citrine/pull/151)は、この同じ週にリレー側で強制を実装します。

**PR [#1653](https://github.com/nostr-protocol/nips/pull/1653)**は、プライベート草案イベントを保存および同期するためのDrafts NIPを提案します。この提案は、置換可能イベントと`draft`ステータス、および作成者自身の鍵に対するNIP-44暗号化を使用し、クライアントが進行中の作業をリレーに保存できるようにし、それらのイベントが他の誰にも見えないようにします。草案イベントは、最終的なkindおよびタグを含む、完全な意図された発行イベントを暗号化されたコンテンツとして運びます。

**Snapshots ([PR #2279](https://github.com/nostr-protocol/nips/pull/2279))**は、置換可能なNostrイベントの1つの正確なバージョンを保持するための不変のスナップショットイベントを定義するオープン提案です。スナップショットイベントは、置換可能イベントのアドレスに戻る`a`タグを持つ、特定の時点における置換可能イベントの完全なコンテンツを運び、すべての履歴バージョンが一緒にクエリ可能になります。これにより、リレーが古いバージョンの保持を停止した後でも、観察者が履歴状態を検査することが可能になります。

**Namecoin NIP-05波:** 今週、`.bit` NIP-05解決をNostrクライアントに追加する協調的な取り組みが見られました。NIP討論フィードは、Aegis ([#14](https://github.com/ZharlieW/Aegis/pull/14)、signerで署名時検証を追加)、nostter ([#2128](https://github.com/SnowCait/nostter/pull/2128))、およびdart-nostr ([#44](https://github.com/ethicnology/dart-nostr/pull/44))に対するオープンソースPRを、上流のNIP草案 ([PR #2349](https://github.com/nostr-protocol/nips/pull/2349))と並んで捉えました。Aegis PRは、検証をプロデューサ側に置く点で注目に値します: signerは、`.bit`アイデンティティを主張するkind:0イベントに署名する前にNamecoinチェーンをチェックし、不一致の場合はユーザーに警告し、イベントがリレーに到達する前に問題を捕捉します。

## NIPディープダイブ: NIP-07 (webブラウザ用window.nostr)

[NIP-07](https://github.com/nostr-protocol/nips/blob/master/07.md)は、ブラウザ拡張機能がwebアプリケーションに公開する`window.nostr`インターフェースを定義します。これはweb上で最も広く展開されているsignerインターフェースで、Alby、nos2x、Flamingo、およびhorseなどの拡張機能によって実装されています。

インターフェースには2つの必須メソッドといくつかのオプションメソッドがあります。`window.nostr.getPublicKey()`は、呼び出し元ページに秘密鍵を公開することなく、ユーザーの公開鍵を16進文字列として返します。`window.nostr.signEvent(event)`は、`created_at`、`kind`、`tags`、および`content`を持つ部分的なイベントを受け取り、`id`、`pubkey`、および`sig`が追加された完全な署名済みイベントを返します。重要なポイントは、秘密鍵が拡張機能の隔離されたコンテキストから決して離れないことです。webアプリケーションは未署名イベントを提出し、署名済みのものを受け取ります。

オプションメソッドは暗号化をカバーします: 古い (現在は非推奨の)NIP-04スキーム用の`window.nostr.nip04.encrypt`および`window.nostr.nip04.decrypt`、および現在のNIP-44スキーム用の`window.nostr.nip44.encrypt`および`window.nostr.nip44.decrypt`。NIP-44をサポートする拡張機能は、呼び出し元ページがnsecを見ることなく、ダイレクトメッセージ暗号化と、pubkey鍵付き暗号化を必要とする他のアプリケーションの両方を扱えます。

仕様には拡張機能の作者への推奨も含まれています: 拡張機能マニフェストで`"run_at": "document_end"`を使用してスクリプトをロードし、ページの読み込み時に`window.nostr`が同期的に利用可能になるようにし、クライアントが拡張機能が注入する前に`window.nostr`をチェックする競合条件を避けます。

動作中のNIP-07の重要な例は、上記で扱ったKeycastプロジェクトです。Keycast webフロントエンドは、NIP-98 HTTP認証イベントに署名するためにNIP-07を使用します: SvelteKitアプリはユーザーのnsecを直接扱いません。`window.nostr.signEvent`を呼び出して認証ヘッダを生成し、次にそのヘッダをKeycast APIに送信します。このアーキテクチャは、キーマテリアルがチーム鍵管理フロー全体を通じてブラウザ拡張機能内に留まることを意味します。

```json
{
  "id": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2",
  "pubkey": "7f8e9d0c1b2a3e4f5d6c7b8a9f0e1d2c3b4a5f6e7d8c9b0a1f2e3d4c5b6a7f8a",
  "created_at": 1747785600,
  "kind": 1,
  "tags": [],
  "content": "Hello from a NIP-07 signed event",
  "sig": "0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2cdd"
}
```

## NIPディープダイブ: NIP-39 (プロフィール内の外部アイデンティティ)

[NIP-39](https://github.com/nostr-protocol/nips/blob/master/39.md)は、Nostrユーザーがプロフィール内で外部プラットフォームアイデンティティに対する制御を宣言する方法を定義します。各宣言はkind:10011イベント内で`i`タグを使用し、他のプラットフォーム上の特定のアカウントの所有権と、独立に検証可能な証明を主張します。

各タグは`["i", "platform:identity", "proof"]`の形式に従い、`platform:identity`はコロンセパレータでプラットフォーム名とユーザー名を結合します (`github:semisol`、`twitter:semisol_public`)。`proof`はプラットフォーム自体上の検証可能なアーティファクトを指します。

GitHubの場合、証明はGist IDです。ユーザーは自分のGitHubアカウントから`Verifying that I control the following Nostr public key: npub1...`というテキストを含む公開Gistを作成します。主張を検証するクライアントは`https://gist.github.com/<identity>/<proof>`を取得し、Gistが主張されたGitHubユーザー名によって作成され、期待されるpubkeyを含むことを確認します。Twitterの場合、証明はツイートID、Mastodonの場合は投稿ID、Telegramの場合は公開グループ内のメッセージ参照です。

アイデンティティプロバイダ名は`a-z`、`0-9`、および`._-/`文字のみを含む必要があり、`:`を含んではなりません。アイデンティティ名は小文字に正規化されるべきで、複数存在する場合はプライマリエイリアスが使用されます。

今週起こっているNamecoin `.bit` NIP-05の議論は、より広範なアイデンティティスタックにおけるNIP-39の役割を示しています: それはNostrキーを他の場所の確立されたアイデンティティと相互参照するための、標準化された、リレー非依存の方法を提供し、中央検証機関を必要としません。クライアントは、指定されたプラットフォーム上の公開アーティファクトを取得することで独立に証明を検証でき、証明はGistまたはツイートテキスト内の特定のNostr pubkeyにバインドされ、一般的なプラットフォーム認証情報ではありません。

```json
{
  "id": "b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3",
  "pubkey": "7f8e9d0c1b2a3e4f5d6c7b8a9f0e1d2c3b4a5f6e7d8c9b0a1f2e3d4c5b6a7f8a",
  "created_at": 1747785600,
  "kind": 10011,
  "tags": [
    ["i", "github:semisol", "9721ce4ee4fceb91c9711ca2a6c9a5ab"],
    ["i", "twitter:semisol_public", "1619358434134196225"],
    ["i", "mastodon:bitcoinhackers.org/@semisol", "109775066355589974"]
  ],
  "content": "",
  "sig": "1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3eff"
}
```

---

今週はこれで終わりです。何か構築しているか、共有するニュースがあれば、NostrでDMを送るか、[nostrcompass.org](https://nostrcompass.org)で見つけてください。
