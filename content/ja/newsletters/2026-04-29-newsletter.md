---
title: 'Nostr Compass #20'
date: 2026-04-29
publishDate: 2026-04-29
draft: false
type: newsletters
translationOf: /en/newsletters/2026-04-29-newsletter.md
translationDate: 2026-07-01
description: 'GitWorkshopがブラウザ内PRマージボタン、リポジトリフォロー、帯域効率の良いgitエクスプローラ、そしてgit-over-Nostr向けインラインコードレビューコメントを出荷。RoutstrdはNostrプロバイダアナウンスとCashu決済を使ったローカル推論ルータをローンチ。リリースにはngit v2.4.2、Wisp v1.0.0、grain v0.5.2およびv0.5.3、Mostro Core v0.10.0、Mostro Mobile v1.2.5、marmot-ts v0.5.0、CruxCoach v0.1.3、Meiso v1.3.0、NoorNote、Nostria、Nostr Calendar、nos2x-fox、applesauce、nostr-double-ratchetが含まれる。未リリース作業にはAmethyst Nests、nostreamのNIP-65/NWC、FIPSのNostrベースudp:natブートストラップ、strfryの可観測性、Sproutオーナ証明、Zap Cookingレシピパックが含まれる。新規追跡プロジェクトはNostrord、Clave、Treasures、smesh、Surveil、Fundstr、Nod City、deploy-nsite-to-pages、null--nostr。月末の振り返りは2021年から2026年までのNostrの4月を扱う。'
---

Nostr Compassへようこそ、Nostrに関する毎週のガイドです。

**今週:** [GitWorkshop](#gitworkshop-ships-in-browser-pr-merge-repository-following-and-a-bandwidth-efficient-git-explorer)はgit-over-Nostrを、ブラウザ内PRマージボタン、Starsとリポジトリフォロー、帯域効率の良いgitエクスプローラ、kind `1111`のインラインレビューコメント、暗号化されたマルチデバイス通知状態を備えた、より充実したコードレビューの場へと発展させました。[Routstrd](#routstrd-launches-a-local-router-for-inference-over-nostr)はNostrのkind `38421`アナウンスを介してモデルプロバイダを発見し、Cashuで支払いを行うローカルデーモンをローンチしました。タグ付けされたリリースには[ngit v2.4.2](#ngit-v242-fixes-grasp-relay-detection-for-pr-submissions)、[Wisp v1.0.0](#wisp-v100-graduates-from-beta)、[grain v0.5.2およびv0.5.3](#grain-v052-fixes-websocket-lockup-v053-continues-polish)、[Mostro Core v0.10.0とMostro Mobile v1.2.5](#mostro-core-v0100-and-mostro-mobile-v125-adopt-nip-59-dual-key-gift-wrap)、[marmot-ts v0.5.0](#marmot-ts-v050-ships-addressable-keypackages)、[CruxCoach v0.1.3](#cruxcoach-v013-ships-encrypted-climbing-data-backup-with-nostr-and-blossom)、[Meiso v1.3.0](#meiso-v130-adds-subtasks-blossom-attachments-and-nip-89-tagging)、NoorNote、Nostria、Nostr Calendar、nos2x-fox、applesauce、nostr-double-ratchetなどが含まれます。未リリースの変更は[Amethyst Nests](#amethyst-advances-nests-audio-rooms-with-moq-interop-testing)、[nostreamのNIP-65およびNWC](#nostream-adds-nip-65-relay-list-support-and-nwc-payments)、[FIPSのNostrベースudp:natブートストラップ](#fips-adds-nostr-based-udpnat-bootstrap)、[strfryの可観測性](#strfry-adds-per-connection-observability)、[Sproutオーナ証明](#sprout-adds-owner-attestation-and-multi-workspace-support)、[Zap Cookingレシピパック](#zap-cooking-adds-recipe-packs-delete-requests-and-bunker-login)を扱います。新規追跡プロジェクトには[Nostrord](#nostrord-a-nip-29-client-built-with-kotlin-multiplatform-and-wasm)、[Clave](#clave-brings-nip-46-remote-signing-to-ios-via-apns)、[Treasures](#treasures-decentralized-geocaching-on-nostr)、[smesh](#smesh-v051-self-hosted-nostr-relay-client-and-signer-in-one-stack)、[Surveil](#surveil-a-magic-the-gathering-deck-builder-on-nostr)、[Fundstr、Nod City、deploy-nsite-to-pages、null--nostr](#smaller-additions-fundstr-nod-city-deploy-nsite-to-pages-and-null-nostr)が含まれます。月末の振り返りは2021年から2026年までのNostrの4月を扱います。

## トップストーリー

### GitWorkshopがブラウザ内PRマージ、リポジトリフォロー、帯域効率の良いgitエクスプローラを出荷

Dan Conwayによる[NIP-34](/ja/topics/nip-34/) git-over-Nostr向けのウェブベース共同作業レイヤーである[GitWorkshop](https://gitworkshop.dev)は、今週メジャーリリースを出荷しました。これにより、コメント、リポジトリリスト、通知を署名済みNostrイベント内に保ちながら、開発者がGitHubやGitLabに期待するワークフローに大きく近づきました。

目玉の追加は、GRASPリレーを使用するリポジトリ向けの長らく待ち望まれていたブラウザ内PRマージボタンです。このリリースでは、リアクションと[NIP-51](/ja/topics/nip-51/)リストの上に構築されたStarsおよびリポジトリフォロー機能も追加され、ピン留めされたリポジトリセットは順序付き`a`タグを介してkind `30617`のリポジトリアナウンスを指すkind `10617`イベントとして発行されます。プロフィールページには、ポータブルなリポジトリリストを表示できるようになりました。

帯域効率の良いgitエクスプローラが、これまでのブラウザ内の浅いクローンに取って代わりました。新しいエクスプローラはGRASPが構築されている基盤のgitクライアント/サーバプロトコルに依存しているため、ブラウザに完全なパックの取得を強制することなく大規模なリポジトリを扱えます。検索はユーザー名とリポジトリメタデータを対象とし、[NIP-50](https://github.com/nostr-protocol/nips/blob/master/50.md)と、ネットワーク全体でリポジトリアナウンスを発見・同期する`ngit-indexer`リレー実装によって動作します。ブラウザ内のリポジトリ作成ワークフローが、発見とオンボーディングの経路を完成させます。

レビューツールは、Files Changedタブ、パッチごとの差分ビューア、および一連の実験的な新しいプリミティブを中心に再構築されています。インラインコードレビューコメントはkind `1111`を使用し、[NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md)の上に構築されています。各コメントはファイルパス(`f`タグ)、コミットSHA(`c`タグ)、選択された行範囲(`line`タグ)を指すため、クライアントは差分内の正しい位置にコメントを表示できます。実験的プリミティブの第二階層は、作成者およびリポジトリメンテナによる権限付けが行われ、[NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md)ラベルを使用します。IssueまたはPRの件名を提出後にリネーム、提出後にハッシュタグを追加、編集可能な要約のためにバージョン管理されたCoverNoteをPRまたはIssueの先頭にピン留め、インラインコード議論のサブスレッドを解決済みとしてマークすることができます。判定イベントと`suggestion`ブロックは草案のままで、まだ出荷されていません。

デバイス間の通知状態もNostrを介して同期されますが、プライバシー保護のひねりが加えられています。GitWorkshopは専用の通知キーペアを生成し、そのnsecを暗号化し、kind `30078`イベント内に格納します。通知nsecは実際の通知状態イベントに署名します。この間接化により、ユーザーのメイン署名者が読み取りやアーカイブ操作ごとの頻繁な暗号化・復号リクエストでスパムされることが防がれ、外部の観察者がユーザーが通知状態を触った時を容易に見ることができなくなります。ユーザーはデバイス間で読み取り状態とアーカイブ状態を同期でき、リレーは暗号化されたblobだけを見ます。

### RoutstrdがNostr経由推論のローカルルータをローンチ

[Routstrd](https://github.com/routstr/routstrd)は、ローカルツールにOpenAI互換のエンドポイントを提供し、各リクエストを競合する[Routstr](https://routstr.com)プロバイダにルーティングする新しいTypeScriptデーモンです。デーモンはRoutstrのRIP-02仕様で定義されたNostrのkind `38421`アナウンスを介してプロバイダを発見します。次に、RIP-06に基づいて価格、信頼、最近のパフォーマンスでプロバイダをスコアリングし、各リクエストを現在最良の選択肢に送信します。

支払いは、cocodによって管理されLightningで資金供給されるローカルCashuウォレットを介して行われます。これにより、Nostrリレーを通じてプロバイダ発見を公開かつパーミッションレスに保ちながら、クライアントにsats建ての決済経路を提供します。セッション中にプロバイダが失敗した場合、Routstrdは次にランク付けされたノードにフォールバックできます。インストール経路は`bun install -g routstrd`、続いてウォレットとリレー設定のための`routstrd onboard`です。

より広範な[Routstrオーガニゼーション](https://github.com/routstr)は、デーモン、Pythonノードソフトウェア(`routstr-core`)、チャットUI、およびプロトコル仕様を保守しています。ユーザーにとって、ローカルポートが安定したインターフェースとなります。既存のOpenAI互換ツールがRoutstrdを指す一方、デーモンがプロバイダ発見、ルーティング、支払いを処理します。

## タグ付きリリース

### ngit v2.4.2はPR提出向けのGRASPサーバ検出を修正

[ngit](https://codeberg.org/DanConwayDev/ngit-cli)は、リポジトリのGRASPサーバ検出の修正を伴う[v2.4.2](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.2)を出荷し、提案がPR kindを使用する際のPR提出をハッピーパスに保ちます。ngitは現在、大規模でない限りほとんどの変更に対してデフォルトで`Patch` kindを使用することに注意してください。メンテナはデフォルトの変更に向けて作業中です。週の前半に出荷された[v2.4.1](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.4.1)は、オープンPRのgitデータがリポジトリの指定されたgitサーバで利用できない場合のクローンおよびフェッチ中の`fatal`エラーを修正しました。

### Wisp v1.0.0がベータから卒業

リレールーティング、プライバシー、および小さなネイティブUIに焦点を当てたKotlinとJetpack ComposeのAndroidクライアントである[Wisp](https://github.com/barrydeen/wisp)は、[v1.0.0](https://github.com/barrydeen/wisp/releases/tag/v1.0.0)を出荷し、続いて[v1.0.2](https://github.com/barrydeen/wisp/releases/tag/v1.0.2)を出荷しました。1.0.0のマイルストーンは、[Newsletter #19](/ja/newsletters/2026-04-22-newsletter/#wisp-v0180-beta-adds-normie-mode-for-you-feed-and-nip-29-group-config)で扱ったNormie Modeの法定通貨表示切り替え、For Youフィード、[NIP-29](/ja/topics/nip-29/)リレーベースのグループ設定、および[NIP-65](/ja/topics/nip-65/)リレーリスト配信をまとめたものです。v1.0.2はAndroid 15の16 KBページサイズサポート、ドロワーシートのQRスキャンタブ、インラインビデオコントロール用のダウンロードボタン、通知リストのパフォーマンス修正を追加します。

### grain v0.5.2はWebSocketロックアップを修正、v0.5.3は仕上げを継続

0ceanSlim製のGoリレーである[grain](https://github.com/0ceanSlim/grain)は、v0.5.0で導入されたWebSocketロックアップに対する重要なホットフィックスとして[v0.5.2](https://github.com/0ceanSlim/grain/releases/tag/v0.5.2)をカットし、続いて[v0.5.3](https://github.com/0ceanSlim/grain/releases/tag/v0.5.3)を出荷しました。ロックアップは特定のフィルタおよびWebSocketパスの下で接続をハングさせていたため、v0.5.1またはv0.5.0のオペレータはアップグレードすべきです。grainはすべての主要なNostrイベントカテゴリを追跡し、NIP-11リレー情報を公開し、ホワイトリスト/ブラックリストのアクセス制御、kindごとのレート制限、ウェブダッシュボード、およびv0.5.xラインで追加されたGoクライアントライブラリをサポートします。

### Mostro Core v0.10.0とMostro Mobile v1.2.5がNIP-59デュアルキーgift wrapを採用

[Mostro Core v0.10.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.10.0)は、識別鍵とトレード鍵を分割した新しい[NIP-59](/ja/topics/nip-59/) gift-wrapモジュールを追加します。以前のトランスポートコードは、トレードidentityとgift wrappingの両方に単一のidentity鍵を使用していました。v0.10.0は安定したトレードidentityをエフェメラルなwrapping鍵から分離するため、トレードプロトコルに必要なidentityを保ちながら、各トレードで新鮮なトランスポート鍵を使用できます。デーモン統合は[Mostro PR #718](https://github.com/MostroP2P/mostro/pull/718)経由でランディングし、[mostro-cli PR #165](https://github.com/MostroP2P/mostro-cli/pull/165)は同じ移行をコマンドラインクライアントにもたらします。

[Mostro Mobile v1.2.5](https://github.com/MostroP2P/mobile/releases/tag/v1.2.5)はプロトコル作業と並行して出荷されました。[PR #581](https://github.com/MostroP2P/mobile/pull/581)は、テイカーがメイカーのアカウント年齢によってオファーをフィルタリングできるようにし、ユーザーがオーダーブック内の新しく作成されたメイカーアカウントを避ける方法を提供します。[PR #580](https://github.com/MostroP2P/mobile/pull/580)はキャンセルされたオーダー詳細の役割ラベルを修正し、[PR #576](https://github.com/MostroP2P/mobile/pull/576)は協調的キャンセルボタンを整理します。

### marmot-ts v0.5.0がアドレス可能KeyPackagesを出荷

[marmot-ts](https://github.com/marmot-protocol/marmot-ts)は、TypeScript版[Marmot](/ja/topics/marmot/)クライアントの最初の計画された破壊的変更リリースである[@internet-privacy/marmot-ts@0.5.0](https://github.com/marmot-protocol/marmot-ts/releases/tag/%40internet-privacy%2Fmarmot-ts%400.5.0)をカットしました。[PR #68](https://github.com/marmot-protocol/marmot-ts/pull/68)はアドレス可能KeyPackageサポートを追加します。`KeyPackageManager`は今、レガシーのkind `443`と新しいkind `30443`の両方のKeyPackageイベントを扱えます。このリリースは`KeyPackageStore`とグループ状態ストレージクラスを削除し、それらを`KeyPackageManager`と`MarmotGroup`に渡される汎用キーバリューストアに置き換えます。また、招待とグループ管理を`MarmotClient.invites`と`MarmotClient.groups`に移動するため、直接埋め込むユーザーはアップグレード前にコンストラクタとストレージの変更が必要です。

### CruxCoach v0.1.3がNostrとBlossomを使った暗号化クライミングデータバックアップを出荷

[CruxCoach](https://codeberg.org/CruxCoach/CruxCoach)は、Kilter Boardクライマー向けの新しいオープンソースAndroidアプリです。Kilter Boardは、Bluetooth経由でホールドが光ってルートを表示する対話型トレーニングウォールです。アプリは4月14日にローンチし、4月26日に[v0.1.3](https://codeberg.org/CruxCoach/CruxCoach/releases/tag/v0.1.3)に到達しました。

v0.1.3はオプトイン暗号化クラウドバックアップを追加します。ユーザーのCruxCoachアカウントはNostrキーペアであり、秘密鍵はローカルバックアップ暗号化鍵への入力を兼ねます。アプリはクライミングデータをオンデバイスで暗号化し、暗号文をBlossomストレージサーバ(`blossom.primal.net`および`nostr.download`)にミラーリングします。リモート削除アクションはBlossomクリーンアップパスを呼び出します。バックアップに加えて、CruxCoachはAmberサポート用の[NIP-46](/ja/topics/nip-46/)リモート署名、アプリ内開発者連絡用の[NIP-17](/ja/topics/nip-17/)プライベートDM、リレー発見用の[NIP-65](/ja/topics/nip-65/)リレーリスト、およびNostr配管用のVitor Pamplonaの[Quartz](https://github.com/vitorpamplona/quartz)ライブラリを使用します。ユーザーはZapstoreまたは直接Codeberg APKからインストールできます。

### Meiso v1.3.0がサブタスク、Blossom添付、NIP-89タグ付けを追加

[Meiso](https://github.com/higedamc/meiso)は、タスクを[NIP-44](/ja/topics/nip-44/)で暗号化されたkind `30078`アプリケーションデータとしてNostrリレーに格納する、Android向けのミニマリストなFlutterタスクマネージャです。4月6日にリリースされた[v1.3.0](https://github.com/higedamc/meiso/releases/tag/v1.3.0)は、親子関係を持つサブタスク、ブロック/被ブロック/関連/重複のタスクリンク、Blossomおよび[NIP-96](/ja/topics/nip-96/) HTTPファイルアップロードエンドポイントを介した画像添付、発行されたイベント上の[NIP-89](https://github.com/nostr-protocol/nips/blob/master/89.md)推奨アプリケーション`client`タグ、およびGoコマンドライン同期ツールを追加します。v1.3.0はまた、コールドスタートリレー動作とAmberクライアント再利用を修正します。

### NoorNote、Nostria、Nostr Calendar、nos2x-fox、およびライブラリリリース

[NoorNote](https://github.com/77elements/noornote)は[v0.8.7](https://github.com/77elements/noornote/releases/tag/v0.8.7)、[v0.8.8](https://github.com/77elements/noornote/releases/tag/v0.8.8)、[v0.8.9](https://github.com/77elements/noornote/releases/tag/v0.8.9)を発行しました。これらのリリースは引用リポストでの画像とビデオのクリック処理を修正し、長文記事画像のライトボックスサポートを追加し、空白のデスクトップ起動画面を修正します。[Nostria](https://github.com/nostria-app/nostria)は[v3.1.29](https://github.com/nostria-app/nostria/releases/tag/v3.1.29)、[v3.1.30](https://github.com/nostria-app/nostria/releases/tag/v3.1.30)、[v3.1.31](https://github.com/nostria-app/nostria/releases/tag/v3.1.31)をカットし、記事エディタの画像圧縮、ウォレットのUSDトグル、プロモーションカード制御、PDFサポート、およびモバイルレイアウトの磨き上げを追加しました。

[Nostr Calendar v1.4.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.4.1)は、カレンダーイベント発行をカレンダーリスト管理から切り離し、招待追跡を修正します。[nos2x-fox v1.19.0](https://github.com/diegogurpegui/nos2x-fox/releases/tag/v1.19.0)は、Firefox NIP-07ブラウザ署名の許可にカスタム認可時間枠を追加します。[nostr-double-ratchet v0.0.97](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.97)は新しいバイナリを出荷します。[nostr-wot-sdk 0.9.0](https://github.com/nostr-wot/nostr-wot-sdk/releases/tag/nostr-wot-sdk%400.9.0)はデフォルトで`NostrSessionProvider`をマウントし、[nostr-tools PR #535](https://github.com/nbd-wtf/nostr-tools/pull/535)はNIP-47ウォレットコネクト文字列のマルチリレー解析サポートを追加します。

週の後半に、[Amber v6.1.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v6.1.0-pre1)は、より良いconnect-new-appレイアウト、signer-dialog修正、通知許可処理の改善、およびリファクタリングされたアカウント選択を伴うプレリリースを出荷しました。[nostr-vpn v0.3.14](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.14)はmacOS Apple Silicon、Linux、Windowsの成果物を含む新しいビルドをカットしました。[Bitcredit Core v0.5.7-hotfix-1およびv0.5.8](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.8)は、orphaned-blockバリデーション問題への連続的な修正を出荷しました。[Surveil v0.1.6](https://gitlab.com/chad.curtis/surveil/-/tags/v0.1.6)はモバイルUIの磨き上げと刷新されたAboutページをもたらしました。プロジェクト自体は[以下](#surveil-a-magic-the-gathering-deck-builder-on-nostr)で紹介します。

### applesauce 6.0.0がレガシーイベントファクトリを削除し、Blossom URI解析を追加

hzrd149のTypeScript Nostrツールキットである[applesauce](https://github.com/hzrd149/applesauce)は、モノレポ全体で6.0.0リリーストレインを出荷しました。[applesauce-core@6.0.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%406.0.0)はレガシーの`EventFactory`クラスと古い`buildEvent`、`modifyEvent`、`createEvent`ヘルパーを削除し、呼び出し元を`applesauce-core/factories`と`applesauce-common`内の新しいファクトリクラスに移行させます。また、リンク解析へのIPアドレスとlocalhost処理、BUD-10 Blossom URI正規表現、および`timeoutWithIgnore`、`combineLatestBy`、`combineLatestByIndex`、`combineLatestByKey`などの新しいobservableヘルパーを追加します。

パッケージレベルのリリースがNostr固有の部分を埋めます。[applesauce-content@6.0.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-content%406.0.0)はテキストとMarkdown向けBUD-10 Blossom URIノードを追加し、レンダラにコンテンツ内のBlossom参照を解析するファーストクラスの方法を提供します。[applesauce-actions@6.0.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-actions%406.0.0)はリレー、ユーザー、アイテムをカバーするNIP-51リスト向けの基底ファクトリクラスを追加し、リスト構築をよりad hocでないものにします。[applesauce-wallet-connect@6.0.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-wallet-connect%406.0.0)は`WalletConnect.connectURI`を公開するため、アプリは既存のNIP-47ウォレットコネクトURIに直接アクセスできます。

## 未リリースの変更

### AmethystがMoQ相互運用テストでNestsオーディオルームを推進

[Amethyst](https://github.com/vitorpamplona/amethyst)は今週、先週の[Media over QUIC](https://datatracker.ietf.org/group/moq/about/)オーディオルームスタックの上に構築された、いくつかのNestsフォーカスなPRをマージしました。[PR #2622](https://github.com/vitorpamplona/amethyst/pull/2622)は、Amethyst MoQクライアントをリファレンスウェブ実装に対して動作させるクロスクライアント相互運用ハーネスを追加します。目標は、Android/ブラウザのワイヤレベルの分岐をユーザーが遭遇する前に捕捉することです。[PR #2625](https://github.com/vitorpamplona/amethyst/pull/2625)はピクチャインピクチャのスピーカーフォーカスと接続状態を改善し、[PR #2620](https://github.com/vitorpamplona/amethyst/pull/2620)は参加者グリッド内のアバター、ミュート状態、発話状態を明確化します。週の後半に、[PR #2634](https://github.com/vitorpamplona/amethyst/pull/2634)がフルスクリーンNestビューでのIMEパディングとウィンドウインセットを修正し、[PR #2635](https://github.com/vitorpamplona/amethyst/pull/2635)がNestsフィードにプレゼンスベースの新鮮さフィルタリングを追加しました。別途、[PR #2627](https://github.com/vitorpamplona/amethyst/pull/2627)がAmethystのカスタムC secp256k1実装を削除し、`libschnorr256k1`に移行しました。

### nostreamがNIP-65リレーリストサポートとNWC決済を追加

[nostream](https://github.com/Cameri/nostream)は、先週の53 PRリレースプリントの後、3つの注目すべきPRをマージしました。[NIP-65](/ja/topics/nip-65/)リレーリストメタデータサポートが[PR #585](https://github.com/Cameri/nostream/pull/585)でランディングし、リレーがkind `10002`リレーリストイベントをインデックスして提供できるようになります。Nostr Wallet Connect決済プロセッサが[PR #539](https://github.com/Cameri/nostream/pull/539)で続き、pay-to-relay経路を追加します。接続クリーンアップは[PR #438](https://github.com/Cameri/nostream/pull/438)で改善され、アクティブなサブスクリプションを持つソケットが刈り取られず、長期間稼働するインスタンスでサブスクリプション数がドリフトするデッドコネクションのバグを修正します。

### FIPSがNostrベースudp:natブートストラップを追加

[Newsletter #6](/ja/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking)および[Newsletter #10](/ja/newsletters/2026-03-25-newsletter/#fips-v020-ships-tor-transport-reproducible-builds-and-sidecar-examples)で以前扱ったFree Internetworking Peering Systemである[FIPS](https://github.com/jmcorgan/fips)は、Nostrベースの`udp:nat`ブートストラップを伴う[PR #53](https://github.com/jmcorgan/fips/pull/53)をマージしました。この変更により、ノードはNostrアドバートを発行し、暗号化されたofferおよびanswerシグナリングを交換し、STUNを介して公開アドレスを発見し、UDPホールパンチングを実行し、パンチされたソケットを通常のFIPSトランスポートスタックに引き渡すことができます。実装は、シグナルペイロードのアイデンティティを実際のNostr送信者にバインドし、設定されたDMおよびアドバートリレーに問い合わせてインボックスルックアップを行い、失敗した採用トラバーサルハンドオフをロールバックして、孤立したUDPトランスポートが生き続けないようにします。これは正規のリポジトリ`jmcorgan/fips`で追跡すべきNostrアナウンスおよびNATトラバーサル作業です。

### strfryが接続ごとの可観測性を追加

[strfry](https://github.com/hoytech/strfry)は[PR #214](https://github.com/hoytech/strfry/pull/214)をマージし、接続ごとの可観測性とPrometheus経由でエクスポート可能な接続レベルメトリクスを追加しました。[PR #204](https://github.com/hoytech/strfry/pull/204)はPrometheusラベルを正規化し、[PR #215](https://github.com/hoytech/strfry/pull/215)はstrfry上に構築されたNamecoin identityプロジェクトを扱うCommunity Integrationsセクションをドキュメントに追加します。

### SproutがOwner Attestationとマルチワークスペースサポートを追加

BlockのNostrクライアントである[Sprout](https://github.com/block/sprout)は、NIP-OA (Owner Attestation)を実装する[PR #406](https://github.com/block/sprout/pull/406)をマージしました。この機能は、自律エージェントに特定の人間のpubkeyがそのアクションを認可したという暗号学的証明を与えます。[PR #409](https://github.com/block/sprout/pull/409)はデスクトップアプリにマルチワークスペースサポートを追加し、[PR #411](https://github.com/block/sprout/pull/411)はモバイルcomposeに`#channel`オートコンプリートを追加し、[PR #410](https://github.com/block/sprout/pull/410)はアクティブチャネルメッセージをドロップする可能性のあった競合ウィンドウを閉じます。[PR #413](https://github.com/block/sprout/pull/413)はデバイス間の既読状態同期のためのNIP-RSを導入し、フォローアップの[PR #420](https://github.com/block/sprout/pull/420)と[PR #422](https://github.com/block/sprout/pull/422)がその既読状態をモバイルの未読バッジに配線します。

### Zap Cookingがレシピパック、削除リクエスト、bunkerログインを追加

[Zap Cooking](https://github.com/zapcooking/frontend)は生産的なレシピ発行作業の一週間をマージしました。ユーザー自身のRecipe Packsに対する[NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md)削除リクエストが[PR #367](https://github.com/zapcooking/frontend/pull/367)でランディングします。発行の信頼性は[PR #366](https://github.com/zapcooking/frontend/pull/366)を通じて改善され、新しいレシピをすべて強制的にgardenリレーに載せ、共有レシピセットのリトライキューを追加します。ワンクリックの著者パック発行が[PR #365](https://github.com/zapcooking/frontend/pull/365)でランディングし、[PR #331](https://github.com/zapcooking/frontend/pull/331)は[NIP-46](/ja/topics/nip-46/) bunkerログインサポートを追加します。

### Whitenoise-rsがローカルデータベースを暗号化

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)は[PR #758](https://github.com/marmot-protocol/whitenoise-rs/pull/758)をマージし、Whitenoiseのオンディスクデータベースに対するSQLCipher暗号化を追加しました。これによりMarmotデーモンスタックの長年のat-restセキュリティギャップが閉じられます。[PR #775](https://github.com/marmot-protocol/whitenoise-rs/pull/775)はグループ必須機能を公開し、[PR #772](https://github.com/marmot-protocol/whitenoise-rs/pull/772)はグループメディア操作をセッション所有の`MediaOps`に移行し、[PR #773](https://github.com/marmot-protocol/whitenoise-rs/pull/773)はsession-opsリファクタの一部として`SharedServices`ホルダーを抽出します。モバイル側では、[whitenoise PR #577](https://github.com/marmot-protocol/whitenoise/pull/577)がAndroidフォアグラウンドサービスのブート自動再起動を有効化し、デバイス再起動後にデーモンが戻らないケースを修正します。

## 新規追跡と発見

### Nostrord: Kotlin MultiplatformとWASMで構築されたNIP-29クライアント

[Nostrord](https://github.com/nostrord/nostrord)は、Discord代替のユースケースをターゲットとする新しい[NIP-29](/ja/topics/nip-29/)グループチャットクライアントです。グループはリレー強制のメンバーシップ、ロール、モデレーション、アクセス制御を持つNostrリレー上に存在するため、グループ状態は選択されたNIP-29リレーによってホストされます。クライアント開発者はそれらのグループのために別個のアプリケーションデータベースを制御しません。ウェブアプリは[web.nostrord.com](https://web.nostrord.com)で稼働し、WebAssemblyにコンパイルするKotlin Multiplatformで構築されており、ネイティブのAndroid、iOS、デスクトップビルドが開発中です。Nostrordは[OpenSats](https://opensats.org)助成金の受領者であり、Flotilla、Chachi、0xChatが使用するのと同じNIP-29リレーと相互運用します。

### ClaveがAPNs経由でNIP-46リモート署名をiOSにもたらす

[Clave](https://github.com/DocNR/clave)はベータ版のiOSリモート署名者で、アプリが開かれていないときにNostrイベントに署名します。秘密鍵はiPhone Keychainに残ります。クライアントが[NIP-46](/ja/topics/nip-46/)リモート署名リクエストを送信すると、サーバサイドのプロキシがApple Push Notificationを配信し、Notification Service Extensionを最大30秒間起こします。その拡張は[NIP-44](/ja/topics/nip-44/)暗号化でリクエストを復号し、Keychainの鍵で署名し、レスポンスを発行します。デバイストークン登録はトークンハイジャックを防ぐために[NIP-98](https://github.com/nostr-protocol/nips/blob/master/98.md) HTTP Authを使用します。Claveは`bunker://`と`nostrconnect://`ペアリング、クライアントごとの信頼レベル、kindごとのオーバーライドをサポートし、Nosturとnastrudelでテスト済みです。

### Treasures: Nostr上の分散型ジオキャッシング

[Treasures](https://gitlab.com/chad.curtis/treasures)は、キャッシュと発見が署名済みNostrイベントであるジオキャッシングプラットフォームです。キャッシュ作成者はGPS座標を持つkind `37516`アドレス可能イベントを発行します。発見者は物理キャッシュに添付されたQRコードをスキャンして発見を記録します。コードは作成者pubkey、キャッシュ`d`タグ、および物理訪問の証明として使用される検証秘密鍵をエンコードします。[NIP-57](/ja/topics/nip-57/) zapは発見者からキャッシュ作成者に流れることができ、ライブアプリは[treasures.to](https://treasures.to)にあります。

### smesh v0.5.1: セルフホストのNostrリレー、クライアント、および署名者を1つのスタックに

[smesh](https://git.smesh.lol/smesh/smesh)は、mlekuによってGoおよびTinyGoから派生したカスタム言語Moxieで書かれたセルフホストのNostrスタックです。このスタックは、HTTP、WebSocket、AUTH、検索、およびBlossomサポート付きのネイティブリレーバイナリ、ESモジュールにコンパイルされたウェブクライアント`sm3sh`、およびNIP-07ブラウザ署名とNIP-04およびNIP-44暗号化サポートを備えたブラウザ署名者拡張機能を出荷します。最近の作業には、v0.5.0でのMLS (RFC 9420) グループメッセージング、リレー同期のためのnegentropyセット調整、およびWeb of Trustグラフエンジンが含まれます。コードはmlekuのセルフホストforge `git.smesh.lol`にあり、彼自身の`git-web`ツールで構築されています。関連する[gitea-nostr-auth](https://git.smesh.lol/smesh/gitea-nostr-auth)リポジトリは、Gitea向けのOAuth2/OIDCブリッジです。ユーザーはNIP-07ブラウザ署名者で認証し、ブリッジはNIP-65を介してリレーを発見し、GiteaはOIDC identity claimsを標準的に受け取ります。

### Surveil: Nostr上のMagic: The Gatheringデッキビルダー

[Surveil](https://gitlab.com/chad.curtis/surveil)は、Magic: The Gatheringプレイヤー向けのNostrクライアントで、ユーザーはカードを検索し、デッキを構築し、オンデバイスML Kit OCRでAndroid上の紙のカードをスキャンし、ネットワーク全体でデッキを共有できます。デッキはkind `37381`アドレス可能イベントとして発行され、デッキイベント仕様はプロジェクトの`NIP.md`に文書化されています。ソーシャルレイヤーは標準的なNostrプリミティブから構築されています。各デッキにスコープされたNIP-22 (kind `1111`) スレッド化コメント、NIP-25 (kind `7`) リアクション、プレイヤーホーム向けの[NIP-78](https://github.com/nostr-protocol/nips/blob/master/78.md) (kind `30078`) プロフィールデータ、kind `3`フォローフィード、および元のデッキに戻る`a`タグを持つフォークです。[v0.1.6](https://gitlab.com/chad.curtis/surveil/-/tags/v0.1.6)は今週、モバイルUIの磨き上げ、ライフカウンター改善、刷新されたAboutページ、デッキヒーローバナーのリレーピルとともに出荷されました。ウェブアプリは静的HTMLが提供されるあらゆる場所で稼働し、Androidビルドは[Zapstore](https://zapstore.dev)を介して出荷され、kind `37381`イベントは[Ditto](https://about.ditto.pub/reference)によってもMagicデッキとしてネイティブにインデックスされます。リポジトリはGitLabの[chad.curtis/surveil](https://gitlab.com/chad.curtis/surveil)にあります。

### 小さな追加: Fundstr、Nod City、deploy-nsite-to-pages、null--nostr

[Fundstr](https://github.com/ritty65/Fundstr)は、一度限りおよび定期的な誓約のためのCashu ecashを使用したNostr上のクリエイター資金調達プラットフォームで、クリエイターティア定義とNostr DMを備えます。[Nod City](https://nod.city)は、レビューが署名済みNostrイベントであり、レビュアーがzapを受け取ることができるBitcoinサービスレビューサイトです。公開ソースリポジトリは見つかりませんでした。[deploy-nsite-to-pages](https://github.com/Origami74/deploy-nsite-to-pages)は、`nsyte download`を使用してnsiteをGitHub Pagesにミラーリングし、ルートkind `15128`および名前付きkind `35128` nsiteをサポートするGitHub Actionです。今週のNIP-34データでも発見された[null--nostr](https://github.com/tami1A84/null--nostr)は、最近のOpenSatsウェーブでNurunuruとして扱われたクライアントです。MLSグループメッセージング、Amber、NIP-50検索、NIP-70保護投稿、ProofModeバッジ、およびZapstore配布をサポートします。

FIPSはCompassにとって新しいプロジェクトではありません。[Newsletter #6](/ja/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking)および[Newsletter #10](/ja/newsletters/2026-03-25-newsletter/#fips-v020-ships-tor-transport-reproducible-builds-and-sidecar-examples)で扱いました。データベースは今、正規のリポジトリである[jmcorgan/fips](https://github.com/jmcorgan/fips)を指しており、今週のNIP-34発見でも`fips`や`awesome-fips`のような関連するgit-over-Nostrミラーが表面化しました。

## プロトコル作業

### NIPアップデート

[NIPsリポジトリ](https://github.com/nostr-protocol/nips)における最近の提案と議論:

**今週マージされたもの:**

- **NIP-34 git repositories: remove unused refs tag extension** ([PR #2325](https://github.com/nostr-protocol/nips/pull/2325)): 定義されていたが使用されていなかった[NIP-34](/ja/topics/nip-34/)の`refs`タグ拡張を削除します。このクリーンアップは、git-over-Nostrツールの実装曖昧性を減らします。

- **NIP-34 git repositories: remove incorrect NIP-09 claim** ([PR #2326](https://github.com/nostr-protocol/nips/pull/2326)): [NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md)削除イベントがリポジトリ状態をリセットできるという誤った主張を削除します。NIP-09削除はクライアント側のイベント削除リクエストであり、リポジトリ状態機械ではありません。この訂正により、NIP-34実装者が削除ヒントを権威あるリポジトリリセットとして扱うことを防ぎます。

**オープンおよび実装主導の作業:**

- **GitWorkshopのkind `1111`インラインレビューコメント**: インラインコードレビューコメントkindはGitWorkshopの`NIP.md`に文書化されており、現在活発に使用されていますが、正式なNIPとしてはまだ提案されていません。判定イベント(kind `7321`)と`suggestion`ブロックは草案のままで、まだ出荷されていません。GitWorkshopとngitからの実装フィードバックが、これらの形が独立したgit-review NIPになるか、NIP-34の上に層をなすアプリケーションコンベンションのままであるかを決定します。

- **Nostr mail coreとNostrmon**: 今週、2つの新しいカスタムNIP草案が回覧されました。[Nostr mail core](https://njump.me/57d11cdf2f9ed73f7f39d6a7a6012ee3d642584ab11887f96a031f7d00fd9697)はRFC 2822メールコンテンツ用のkind `1301`を提案し、プライベート配信のためにNIP-59でラップされ、NIP-05で解決されたブリッジpubkeyを介してレガシーメールにブリッジされます。[Nostrmon](https://njump.me/5e9a8cee19d464f5f0322518ac9ccaf2399c69da6572346b4fb12d36acb17a27)は、地域、マップ、クリーチャー、NPC、プレイヤーセーブ、およびアイテム用のアドレス可能イベントkindをスケッチします。両方ともカスタム草案のままで、マージされたNIPではありません。

- **NIP-67: EOSE Completeness Hint** ([PR #2317](https://github.com/nostr-protocol/nips/pull/2317)): 提案は`EOSE`に肯定的な完了マーカーを追加することの反復を続けており、リレーが「保存イベントが完全に配信された」を、リレーが完了主張をしないレガシーの`EOSE`ケースと区別できるようにします。

## 6つのNostrの4月

4月はNostrの開発経路のきれいな断面図を与えます。2021年のプロトコル文書、2022年の初期クライアント作業、2023年のDamus後のアプリケーション波、2024年のプライベートメッセージングとgit-over-Nostr作業、2025年のBlossomとリレーリストのクリーンアップ、2026年の採用フォーカスのクライアント助成金です。

### 2021年4月: NIPsリポジトリ以前のプロトコル文書

Fiatjafは2020年11月20日に元のNostr記事、["Notes and Other Stuff Transmitted by Relays"](https://fiatjaf.com/nostr.html)を発表しました。その最初のテキストには既に、プロトコルを今も定義する核となる形が含まれていました。ユーザーは鍵でイベントに署名し、それらをリレーに発行し、選択したリレーから読み取ります。[`nostr-protocol/nostr`コミットログ](https://github.com/nostr-protocol/nostr/commits?since=2021-04-01&until=2021-04-30)は、4月1日から4月30日の間にコミットがないことを示しています。活動はその両側にあります。2021年3月のコミットは初期の「nostwitter」リンクと`kind`フィルタを追加し、2021年5月にはNIP-02が再利用され、NIP著作権が追加されました。

2021年4月には、公開クライアント市場もなく、目に見えるリレーネットワークもなく、NIPsリポジトリもありませんでした。プロトコルは依然として小さな文書といくつかの実験として存在していました。Nostrはまだソーシャルネットワークにも開発プラットフォームにもなっていませんでした。それは依然として、最初の持続的な貢献者の波を待つリレー/鍵/イベントモデルでした。

### 2022年4月: NIPsはまだメインリポジトリに存在した

2022年4月は、NIPsがメインの`nostr-protocol/nostr`リポジトリから移動する前の最後の月でした。分割がまだ起こっていなかったため、専用の[`nostr-protocol/nips`](https://github.com/nostr-protocol/nips)リポジトリには4月のプルリクエスト履歴がありませんでした。メインリポジトリでは、3つの4月のコミットがランディングしました。4月8日のgoswami1999による["Update readme to add nip12"](https://github.com/nostr-protocol/nostr/commit/bae286312a233b971bee5429adda7aff41747eb8)、4月25日のjb55による["add kinds list"](https://github.com/nostr-protocol/nostr/commit/4b9e9d123273ba8a5c70d77df46922070c11c11d)、4月28日のsteliosrammosによる["add js formatting to sample code"](https://github.com/nostr-protocol/nostr/commit/759997657f07e0344064228ffe5e93febe85d367)です。

クライアント作業も形を成し始めていました。2022年4月のDamusコミットは初期のチャットルーム動作、プロフィール処理、およびアプリアイコンを追加し、nostr-toolsは初期のクライアントおよび実験のためのJavaScriptライブラリ経路になりつつありました。プロトコル面では、NIP-12ジェネリックタグクエリがタグ検索に文書化された場所を与え、kinds listはNostrをレジストリモデルに向けて動かし、より良いJavaScript例は仕様をクライアントおよびライブラリ作者にとって実装しやすくしました。5月1日、fiatjafはNIPsを専用リポジトリに移動しました。2022年4月は元のシングルリポジトリ時代の最後の月でした。

### 2023年4月: Damus後のアプリケーション拡大

2023年4月は、Damusが2023年1月31日にiOS App Storeでローンチしてから3か月後、Jack DorseyがNostrの公開鍵を投稿した後に到来しました。ネットワークはちょうど最初の大きな公開成長波を吸収したところでした。Damus、Snort、Iris、Coracle、Amethystなどのクライアントがアクティブで、リレーオペレータはより大きなソーシャルグラフが帯域幅、スパム、検索、モデレーションの前提に何をするかを学んでいました。

2023年4月には1つのマージされたNIPs PRがありました。4月17日にマージされた[PR #456](https://github.com/nostr-protocol/nips/pull/456)は、NIP-21のURI処理にNIP-19 bech32エンティティリンクを追加しました。周囲のコミットは、プロトコル作業の背後にあるアプリケーション圧力を示しています。2023年4月には、[NIP-45 COUNT](https://github.com/nostr-protocol/nips/commit/8b39976e78f90fe766ad7149e250777cddacbb5e)、イベント固有のzapマーカー、[NIP-15マーケットプレイス](https://github.com/nostr-protocol/nips/commit/bf0a0da6a48b96467172414d8e41dc72b0ca379c)、NIP-26削除委任セマンティクス、NIP-94ファイルメタデータ、NIP-47ウォレットコネクトエラー処理、[NIP-30カスタム絵文字](https://github.com/nostr-protocol/nips/commit/e91ce3409e1ce8267fc07a21784d2538621267c3)に関する作業がありました。貢献者リストはfiatjaf、staab、pablof7z、Semisol、CodyTseng、sethforprivacy、mikedilger、AsaiToshiya、alexgleason、martindsq、frbittencourt、arkin0xを含むように広がりました。

Damus、Snort、Iris、Coracle、Amethystはもはや仕様の周りのデモではありませんでした。それらはオンボーディング、フィード、スパム、zap、メディア、リレー選択に対処する本番クライアントでした。2023年4月のプロトコル作業は、それらのクライアントが作成したバックログのように読めます。zap、マーケットプレイス、ファイルメタデータ、カウント、絵文字、identityリンクはすべて、仕様を単純なノートおよびフォローを超えて押し進めました。

### 2024年4月: プライベートメッセージング、git-over-Nostr、およびメンテナサポート

2024年4月には2つのNIP PRマージがありました。4月10日にマージされた[PR #1167](https://github.com/nostr-protocol/nips/pull/1167)は、クライアントと署名者が要求および認可されたアクションに対して正確な言葉遣いを必要とする[NIP-46](/ja/topics/nip-46/)リモート署名の紛らわしい用語を修正しました。4月17日にマージされた[PR #1108](https://github.com/nostr-protocol/nips/pull/1108)は、ステータスイベント、明確化、オプションのメンテナ、リポジトリ識別子、および発見可能性タグを含む[NIP-34](/ja/topics/nip-34/) git repositoriesを拡張しました。そのステップは、git-over-Nostrをngitとその後のGitWorkshopにとってより実用的にしました。

以前はNIP-24だった[NIP-17](https://github.com/nostr-protocol/nips/commit/df30012430c88d49fb5b124992b04d5c61b6338b)は、プライベートDMおよび小グループチャット向けのsealed gift-wrappedメッセージとして4月24日にランディングしました。同じ期間にAmethyst、Primal、Gossip、nostr-tools、NDK、およびrust-nostrがすべてアクティブで、クライアントとライブラリの作業が並行して行われました。

OpenSatsも2024年4月にNostr開発者への長期サポートを発表しました。4月9日の[PabloF7z](https://opensats.org/blog/pablofz7-receives-lts-grant)、4月12日の[Stuart Bowman](https://opensats.org/blog/stuart-bowman-receives-lts-grant)、4月15日の[hzrd149](https://opensats.org/blog/hzrd149-receives-lts-grant)です。これらの助成金は、資金を孤立したプロジェクト助成金から、リレー、ライブラリ、クライアントインフラの持続的な維持へと移動させました。

### 2025年4月: 密なNIPクリーンアップとBlossom正式化

2025年4月は、この振り返りで最も密なプロトコル月間で、16のマージされたNIPs PRがありました。月はNIP-73にブロックチェーントランザクションとアドレスを追加した[PR #1846](https://github.com/nostr-protocol/nips/pull/1846)と、標準化タグ表にNIP-C0タグを追加した[PR #1865](https://github.com/nostr-protocol/nips/pull/1865)で始まりました。続いて[PR #1801](https://github.com/nostr-protocol/nips/pull/1801)と[PR #1889](https://github.com/nostr-protocol/nips/pull/1889)がkind `10002`リレーリスト再発行ガイダンスを改善し、[PR #1879](https://github.com/nostr-protocol/nips/pull/1879)が[NIP-65](/ja/topics/nip-65/)を縮小して明確化しました。

[PR #1822](https://github.com/nostr-protocol/nips/pull/1822)はBlossom相互作用のためにNIP-B7を追加し、1年以上の非公式な実践の後にNostrクライアントとBlossomサーバに正規の調整レイヤーを与えました。[PR #1051](https://github.com/nostr-protocol/nips/pull/1051)は、委任イベント署名仕様である[NIP-26](https://github.com/nostr-protocol/nips/blob/master/26.md)を非推奨としました。NIP-26は安全に実装することが難しく、NIP-46や他の署名者パターンが成熟するにつれて魅力が薄れていました。

月の残りはクリーンアップとアプリケーション拡大を組み合わせました。[PR #1882](https://github.com/nostr-protocol/nips/pull/1882)は[NIP-11](/ja/topics/nip-11/)にプライバシーポリシーおよび利用規約フィールドを追加し、[PR #1849](https://github.com/nostr-protocol/nips/pull/1849)はNIP-B0の下でkind `39701`ウェブブックマークを拡張し、[PR #1891](https://github.com/nostr-protocol/nips/pull/1891)はそのブックマークkindをREADMEに追加し、[PR #1895](https://github.com/nostr-protocol/nips/pull/1895)はNIP-B0標準化タグを追加しました。OpenSatsは4月16日に[Eleventh Wave of Nostr Grants](https://opensats.org/blog/eleventh-wave-of-nostr-grants)を発表し、Swae、HAMSTR、Vertex、Nostr Double Ratchet、Nostr Game Engineに資金を提供しました。Primal、Coracle、noStrudel、nostr-tools、NDK、rust-nostrもこの期間を通じて出荷していたため、プロトコルクリーンアップはアクティブなクライアントとライブラリ作業の隣に位置していました。

### 2026年4月: NIP-34の強化、バッジ、および採用フォーカスの助成金

この号が閉じる2026年4月は、4つのマージされたNIPs PRがありました。最初は4月1日にマージされた[PR #2276](https://github.com/nostr-protocol/nips/pull/2276)で、[NIP-58](https://github.com/nostr-protocol/nips/blob/master/58.md)プロフィールバッジをkind `10008`に変更し、kind `30008`バッジセットを追加して、バッジ割り当てとバッジコレクションをより組み合わせやすくしました。第二のgit-over-Nostrユーザビリティ変更は4月10日にマージされた[PR #2312](https://github.com/nostr-protocol/nips/pull/2312)で到来し、[NIP-34](/ja/topics/nip-34/)に`nostr://`クローンURLセマンティクスを追加しました。4月25日のクリーンアップ、[PR #2325](https://github.com/nostr-protocol/nips/pull/2325)と[PR #2326](https://github.com/nostr-protocol/nips/pull/2326)は、使われていないおよび誤ったNIP-34の言葉遣いを削除しました。

関連するコミットは同じ表面を鋭くします。4月22日、fiatjafはNIP-51にBlossomサーバリストを追加し、NIP-29メタデータ編集をFlotillaのPUT形式の動作に合わせるように調整しました。4月26日、彼は明確化のためにNIP-5Aをリネームしました。2026年4月は、すでに使われているプロトコル表面を実装しやすく、誤読しにくくすることに焦点を当てました。

OpenSatsは4月8日に[Sixteenth Wave of Nostr Grants](https://opensats.org/blog/sixteenth-wave-of-nostr-grants)を発表し、Amethyst Desktop、Nostr Mail、Nostrord、Nurunuru (null--nostr)、およびHAMSTRの更新を支援しました。デスクトップクライアント、メール様メッセージング、グループUX、日本語オンボーディング、およびオフグリッド接続です。

---

*Nostr Compass #20をお読みいただきありがとうございます。ヒント、修正、または扱うべき新しいプロジェクトがあれば[NostrでDMを送ってください](https://nostr.com)。*
