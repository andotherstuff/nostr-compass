---
title: 'Nostr Compass #26'
date: 2026-06-10
publishDate: 2026-06-10
draft: false
type: newsletters
translationOf: /en/newsletters/2026-06-10-newsletter.md
translationDate: 2026-07-08
---

Marmot Protocol組織は、v2プロトコルドラフトとネイティブクライアントの系統のために3つの新しいリポジトリを公開しました: `darkmatter`という名前のRustワークスペース、SwiftUI iOSアプリ`darkmatter-ios`、Kotlin/Compose Androidアプリ`darkmatter-android`。オリジナルのFlutter Whitenoiseはアーカイブされました。Chamaは17のリリースを1週間に圧縮し、v3.0.0でスタンドアロンアプリのラインを越えてから、v3.1.0で完全な取引ルームUIの再描画と、ホルダー専用Shamir共有、アービター置換、全世界コミュニティルーティング、およびエンドツーエンドの取引通知の上に構築された販売者ごとのストアフロントを実現しました。Coracleは、オープンソースのCaravelとzooidスタックに支えられた有料のホスト型リレーサービスをローンチし、深いFlotilla統合が計画されています。Angorはv0.2.30でデフォルトをmainnetに反転させ、v0.2.29で3ユーザーUAT資金調達テストを実現しました。Amethystは、先週のNIP-32 / NIP-F4 / Torの作業を継続する41の未リリースPRを実現しました。NIP-67 (EOSE完全性ヒント) とNIP-50オートコンプリートがマージされ、コアリレープロトコルの2つの長年の正確性ギャップを閉じました。NIP-GARTは緊急アラートのためのプライバシー保護ワイヤーフォーマットを提案し、NIP-46はlogoutメソッドを獲得します。

## トップストーリー

### Marmot v2 (Dark Matter): プロトコル再ドラフト、ネイティブクライアント、アーカイブされたFlutterアプリ

今週、[marmot-protocol](https://github.com/marmot-protocol) GitHub組織の下に3つの新しいリポジトリが登場し、合わせてMarmot v2プロトコルドラフトの初期進捗の形と、Flutterアプリのラインを置き換えるネイティブクライアント系統を形成しています。[`darkmatter`](https://github.com/marmot-protocol/darkmatter) (Rust、5月13日作成、過去7日間で34コミット) は`spec/`にv2プロトコルドラフト、`crates/cgka-engine`にOpenMLSベースのCGKAエンジン、プロパティテスト付きの適合性シミュレーター、および収束証明のためのTamarin形式モデルを保持しています。[`darkmatter-ios`](https://github.com/marmot-protocol/darkmatter-ios) (Swift、5月25日作成) は、Rustワークスペースから生成されたベンダー化された`MarmotKit` UniFFI xcframeworkに支えられたSwiftUIクライアントです。[`darkmatter-android`](https://github.com/marmot-protocol/darkmatter-android) (Kotlin/Jetpack Compose、5月25日作成) は同じRustバインディング上に位置しています。オリジナルのFlutter Whitenoiseは[`whitenoise-archive`](https://github.com/marmot-protocol/whitenoise-archive)としてマークされています (「ARCHIVED: これはオリジナルのWhite Noise Flutterアプリでした」)。新しい[`whitenoise`](https://github.com/marmot-protocol/whitenoise) Dartリポジトリが並行してアクティブなFlutterラインを運びます。

これは完成したピボットではなく、より信頼性の高いMarmotへの初期の進捗として読んでください。darkmatterのREADMEは自身を「Marmot v2プロトコルドラフト候補、CGKAエンジン、および適合性ワークスペース」とラベル付けし、直接述べています: 「このドラフトとエンジンが採用されるまで、MDKは展開されたRustプロトコル実装のままです」。ワークスペース内で、cgka-engineクレートは`0.1.0`、「単一の内部消費者、semver安定ではない」とタグ付けされています。すべての仕様ページには「ステータス: 内部レビュー用ドラフト」と記載されています。ワークスペースリポジトリでの3つのスターとiOSおよびAndroidアプリでのゼロは、作業がアナウンス前であることを確認します。方向性、スコープ、規律がここでの信号です。本番の準備が完了していることは主張されていません。

プロトコルドラフトはv1からv2へのデルタを具体化します。Marmotの開始以来、グループ名、説明、管理者pubkey、Nostrグループルーティングid、リレーリスト、グループ画像データ、および消えるメッセージ設定を1つの傘の下に運んでいたMIP-01のモノリシックな`marmot_group_data` MLS拡張は、[バージョン付きアプリコンポーネントに分割](https://github.com/marmot-protocol/darkmatter/blob/master/spec/mip-coverage.md)されます: 名前と説明のための`marmot.group.profile.v1`、管理者pubkeyのための`marmot.group.admin-policy.v1`、ランダムな`nostr_group_id`と正規のリレーリストのための`marmot.transport.nostr.routing.v1`、画像ハッシュ、暗号化キー、nonce、およびアップロードキーのための`marmot.group.blossom.image.v1`、消えるメッセージの秒数のための`marmot.group.message-retention.v1`。各コンポーネントは正確なバイトと独自のバージョン管理パスを所有するので、将来の機能は、残りのグループ状態がMLS拡張のコンセンサスを再度踏襲することを強制することなく、1つのコンポーネントを改訂できます。MIP-00クレデンシャルも新しい基礎文書`account-identity-proof-v1.md`を獲得し、「v2の新規で破壊的」と呼び出されます。アイデンティティ証明は今や、KeyPackage構築とは別に独自のサーフェスに存在します。

ライブラリのデルタは仕様の再設計を支えます。`cgka-engine`は新しいローカルグループ状態マシンです: OpenMLSをラップし、`Stable`、`PendingPublish`、`Merging`、`Recovering`エポック状態を所有し、意図をMLSコミットに変換し、あらゆる受信トランスポートエンベロープに対して型付き`IngestOutcome`と`GroupEvent`値を返し、明示的にトランスポートも永続性も出荷しません。`TransportPeeler` traitはNostrをエンジンから分離し、`StorageProvider` traitはSQLite ( SQLCipherベースの`storage-sqlite`経由) をエンジンから分離します。今日のMDKはこのすべてを一緒にパックしています。層を分割することで、1つのエンジンが今Nostrリレートランスポートの下に位置し、後で収束モデルを書き直すことなく、また出荷される[QUICストリームとブローカートランスポート](https://github.com/marmot-protocol/darkmatter/blob/master/docs/quic-broker-deployment.md)の下にも位置できます。収束自体は`distributed-convergence.md`として文書化されており、決定論的ブランチ選択、ポリシーゲート適格性、保持アンカーリプレイ、古いブランチ拒否、配信の並べ替え、重複、アプリ出力の無効化、welcome/commitハンドオフ、提案消費、および同期中のアウトバウンドゲーティングをカバーするTamarinモデルで証明されています。次にRustプロパティテストが、エンジンが実際のOpenMLSオブジェクトとシミュレーターハーネスで同じルールに従うことを確認します。このスコープの形式手法の信頼性の作業は、現在のMarmotスタックにはありません。

両方のネイティブクライアントは、プラットフォームネイティブUIツールキットのためにFlutterをドロップします。[`darkmatter-ios`](https://github.com/marmot-protocol/darkmatter-ios)は、MIP-05プッシュウェイクをデバイス上で復号するNotification Service Extensionを備えた純粋なSwiftUIで、Rustワークスペースから構築された生成された`MarmotKit` Swiftパッケージをベンダーし、`dev.ipf.darkmatter`バンドルIDとアプリグループの下に登録します。[`darkmatter-android`](https://github.com/marmot-protocol/darkmatter-android)はKotlinとJetpack Composeで、`just`駆動のビルドが署名された`arm64-v8a` APKを生成し、`local.properties`からテレメトリエンドポイントを読み取ります。Android READMEはアーキテクチャの原則を直接述べています: 「Dark Matterはプロトコルデータを所有し、SQLiteに保存します。Androidアプリはそのデータをレンダリングし、Androidプラットフォームの動作を管理し、UIライフサイクル状態を保つべきです。AndroidアプリはDark Matterデータのための2番目のデータベースになるべきではありません」。それは、UIレイヤーに適用された、Rust層でcgka-engine READMEが強制する境界規律を反映します。

Marmotにとってネイティブクライアントが重要な理由は、プロトコルの最も引用される弱点が、不均一な配信条件下でのモバイルの信頼性だったからです: 締め切りを逃した通知ウェイク、ネットワークフラップ中のMLSコミットレース、エポックの進行を座礁させるバックグラウンドフェッチ制限。SwiftUIとComposeは、Flutterがプラグインブリッジを通じて到達するプラットフォームバックグラウンド処理プリミティブへの直接アクセスをクライアントに与え、UniFFIバインディングパスは、両方のプラットフォームで静的ライブラリとして出荷される1つのRustワークスペースにプロトコルロジックを保ちます。Flutter Whitenoiseラインは、アーカイブされていない[`whitenoise`](https://github.com/marmot-protocol/whitenoise)リポジトリで継続するので、アナウンスは加算的です: v2仕様が収束する間、新しいネイティブクライアントの系統がFlutterアプリと並行して動作します。MDKまたは現在のWhitenoiseアプリからの本番切り替えは、ドラフト、エンジン、およびクライアントが本番対応リリースに到達するのを待ちます。

### Chama v2.0.0からv3.1.0: 1週間でスタンドアロンP2Pエスクロー

ニュースレター #25でv1.3.0で紹介されたNostrネイティブP2Pエスクロークライアントは、過去7日間で17のタグ付きリリースを出荷し、6月9日の[v3.1.0](https://github.com/jesuspirate/chama/releases/tag/v3.1.0)で取引ルームUIの再描画と販売者ごとのストアフロントで終了しました。バージョントレイルはストーリーを語ります: [v2.0.0](https://github.com/jesuspirate/chama/releases/tag/v2.0.0)は破壊的なベースで、続いて[v2.0.1](https://github.com/jesuspirate/chama/releases/tag/v2.0.1)、[v2.0.2](https://github.com/jesuspirate/chama/releases/tag/v2.0.2)、[v2.0.3](https://github.com/jesuspirate/chama/releases/tag/v2.0.3)がFedi WebViewの資金調達レールギャップを閉じます。[v2.1.0](https://github.com/jesuspirate/chama/releases/tag/v2.1.0)、[v2.2.0](https://github.com/jesuspirate/chama/releases/tag/v2.2.0)、[v2.3.0](https://github.com/jesuspirate/chama/releases/tag/v2.3.0)、[v2.3.1](https://github.com/jesuspirate/chama/releases/tag/v2.3.1)はアービターレイヤーを強化します。[v2.4.0](https://github.com/jesuspirate/chama/releases/tag/v2.4.0)、[v2.5.0](https://github.com/jesuspirate/chama/releases/tag/v2.5.0)、[v2.6.0](https://github.com/jesuspirate/chama/releases/tag/v2.6.0)はセルフカストディサーフェスと全世界コミュニティルーティングを追加します。[v2.7.0](https://github.com/jesuspirate/chama/releases/tag/v2.7.0)、[v2.8.0](https://github.com/jesuspirate/chama/releases/tag/v2.8.0)、[v2.9.0](https://github.com/jesuspirate/chama/releases/tag/v2.9.0)、[v2.10.0](https://github.com/jesuspirate/chama/releases/tag/v2.10.0)は、平易な英語でのキーコピー、グループアプリケーション、紛争締切アービトレーション、および評判を重ねます。[v3.0.0](https://github.com/jesuspirate/chama/releases/tag/v3.0.0)はエンドツーエンドの取引通知でパッケージをまとめ、6月9日の[v3.1.0](https://github.com/jesuspirate/chama/releases/tag/v3.1.0)は、Reserved → Locked → Settled進行スパイン、ロール色付けされたアクションカード、および販売者ごとのストアフロントリスティングクラス (キュレートされたスワップ、ローンブック、および請求書) の周りに取引画面を再描画します。

アーキテクチャピボットはv2.0.0に存在します。エスクローLOCKフォーマットは、2-of-3 Shamir分割の各共有がそのホルダーのみに暗号化されるように変更されました (sharePolicy `holder-only-v1`)。フェデレーションのbearer ecashは、単一の参加者だけからは再構成されなくなり、自分の共有とフェデレーションが保持する共有の両方を持つ悪意のある当事者が同意なしに取引を完了できるパスが閉じられました。プレ2.0クライアントは「共有が見つかりません」で大声で失敗します。取引は古いクライアントでは完了できず、その過程で資金は失われません。v2.0ロックは、決済するためにv2.xのすべての当事者を必要とします。v2.0.0はまた、マルチユニットストアフロントとsatsのみのマーケットビューを追加しました。

v2.1.0はアービター置換を導入しました: Shamirインデックス2のアービター共有は、コミュニティアービタープール上の決定論的優先順位に暗号化されるようになったので、不在のアービターは取引を座礁させることなく置き換えられます。v2.2.0は、₿121の取引で野生での置換が機能することを証明し、ヒーリング置換バックアップを追加しました。v2.3.0はロック時にリスティングアービターのコミュニティメンバーシップをチェックすることで最後のアービターフロントランニングギャップを閉じ、v2.3.1は自動割り当てされたアービタースロットがロックが彼らを座らせるまでプレビューだった兄弟レースを閉じました。

セルフカストディサーフェスはv2.4.0で到着しました (Fedimint ecashウォレット用のBIP-39リカバリフレーズ、Nostrに暗号化されて保存される) およびv2.5.0 (Nostrアイデンティティとウォレットシードを所有するマスターnsecバックアップ)。v2.6.0は、ローカルChamaがない国のユーザーを最も近いフェデレーションにルーティングするグローバルコミュニティピッカーの周りにオンボーディングを再作業しました。以前のビルドはフォールバックなしでユーザーをバウンスさせていました。v2.7.0は、リカバリキー画面を平易な英語で書き直しました (「あなたのアカウントとその中のお金への唯一のキー。Chamaはそれを見ることはなくリセットもできません。失うと、誰もあなたのアカウントを取り戻せません」)。v2.8.0はグループアプリケーション、ダーク/ライトテーマ、および2つの新しいイベントkind (38120ロスター、38121アプリケーション) を追加しました。v2.9.0は締切時の紛争解決を変更しました: 期限に達した争われた取引は、アービターの裁定によって解決されるようになりました。以前の動作は自動返金でした。リリースは COORDINATED としてマークされているので、紛争のすべての当事者が更新しなければなりません。v2.10.0は、新しいイベントkind 38123として取引ごとのthumb-up/thumb-down評価を追加しました。

v3.0.0は、アプリが動作するために調整コミュニティを必要としなくなるマイルストーンです。エンドツーエンドの取引通知は、アクション可能な状態遷移でのみユーザーにpingを送信します: 相手方がsatsをロックした、支払いが請求可能、紛争がアービターとしてのユーザーの裁定を必要とする、または取引が決済または期限切れになった。Me画面の1つのトグルが通知をオンまたはオフにし、許可プロンプトはトグルが有効化されているときにのみ発火します。fire-once dedupは、状態の再ロードがアラート嵐をトリガーするのを防ぎます。間違ったchamaガードレールバグも[PR #103](https://github.com/jesuspirate/chama/pull/103)で閉じられました。以前のバージョンは、1つのchamaのラベルで別のchamaのフェデレーションを持つリスティングをスタンプできました。WindowsとLinuxデスクトップバンドルはリリースとともに出荷されます。macOS dmgは、署名と公証が着地するまで保留されます。

ChamaはMostroとShopstrにNostrネイティブマーケットプレイスとして加わり、そのサーバーレスアーキテクチャ、Fedimintに支えられた2-of-3 Shamirエスクロー、ホルダーのみの共有暗号化、および3つのうち調整コミュニティなしで自己完結型のデスクトップとモバイルクライアントを出荷する唯一のものとして区別されます。

### Coracle Hosting: 有料リレーサービスとオープンソースCaravelスタック

6月3日、Hodlbodは[hosting.coracle.social](https://hosting.coracle.social)で[Coracle Hostingを発表](https://nos.lol/e/f8586160cd12df479c261397353c99e6f3e4d870b616382e1b4338bad3ab498a)しました。これはNWCまたはカード経由の定期的なlightning支払いを受け付けるホスト型コミュニティリレーサービスです。サービスは、Coracleの請求とプロビジョニングフロントエンドである[Caravel](https://gitea.coracle.social/coracle/caravel)と、単一のマシン上で多くの仮想リレーをホストするリレーランタイムである[zooid](https://gitea.coracle.social/coracle/zooid)によって支えられています。両方ともCoracleのセルフホスト型giteaでオープンソースです。Caravelは、オプションの[livekit](https://livekit.io)と[Blossom](/ja/topics/blossom/)統合とともに出荷され、オペレーターはリレーごとに切り替えることができます。メンバー数の制限がある無料ティアにより、オペレーターは支払い詳細をコミットする前にサービスを評価できます。

Hodlbodはビジネスモデルについて率直です: 他の誰もが実行できるスタックのホスト版を販売することによってオープンソースを収益化する。競争的な堀は[Flotilla](https://flotilla.social)統合であり、これは次に計画されているステップです。Flotillaはユーザーサーフェスを所有しているので、Flotilla内部から提供されるホストオプションは、管理されたインフラストラクチャを好む任意のユーザーのデフォルトパスになります。Hodlbodは、連絡があれば他のCaravelオペレーターをFlotillaの代替ホスティングピッカーに追加することを申し出て、連合ホスティング市場への扉を開いたままにしています。

CaravelはPaid Memberティアを備えた公開Nostrリレープロビジョニングプラットフォームとして[relay.tools](https://relay.tools)に加わります。relay.toolsはCaravelよりも前からあり、今日主要なリレー作成サービスとして出荷され、コミュニティリレーの独自のディレクトリと、有料メンバーまたはモデレーター参加フローを備えています。Caravelの区別する特徴は、調整されたスタックです: リレーランタイム (zooid)、請求とプロビジョニングフロントエンド (Caravel自体)、およびクライアント側ピッカー (Flotilla統合、まだ進行中) が1つの設計として出荷されます。他の区別する特徴は、zooidのプロセスごとの多リレー密度であり、顧客リレーが単一のホストプロセスを共有するので、オペレーターは多くの小さなコミュニティ全体でホスティングコストを償却します。これは、2000年代初頭に共有Webホスティングを実現可能にしたのと同じ密度の議論であり、Nostrのリレーレイヤーに適用されています。

## リリース

### Angor v0.2.29とv0.2.30: mainnetデフォルトと3ユーザーUAT資金調達テスト

6月4日の[Angor v0.2.29](https://github.com/block-core/angor/releases/tag/v0.2.29)と6月8日の[v0.2.30](https://github.com/block-core/angor/releases/tag/v0.2.30)は、分散型Bitcoin-and-Nostr資金調達プロトコルの今週の2つのリリースです。v0.2.30の目玉変更は[PR #893](https://github.com/block-core/angor/pull/893)で、デフォルトネットワークをmainnetに反転させます。Angorは不安定なアルファリリースとして出荷され続けますが、default-mainnet切り替えは、プロトコルがデスクトップおよびモバイルクライアントのtestnet-onlyフェーズを過ぎたことを信号送信します。v0.2.30はまた、画像アップロードとスクロールリセットを備えたシングルタップモバイル作成プロジェクトフロー ([PR #889](https://github.com/block-core/angor/pull/889)) を実現し、lightningインボイススピナーがハングする可能性があった競合条件を解決します ([PR #890](https://github.com/block-core/angor/pull/890))。

v0.2.29は、未確認の使用を伴う10ラウンドにわたる3ユーザー送金をカバーするエンドツーエンドのUATテストを[PR #881](https://github.com/block-core/angor/pull/881)で追加しました。これはAngorテストスイートで最初のマルチユーザー資金調達フローテストです。このリリースはまた、Angor CLIとMCPサーバーの実装計画 ([PR #792](https://github.com/block-core/angor/pull/792)) を追加し、[PR #880](https://github.com/block-core/angor/pull/880)でMCPテストワークフローのためのCLI改善を行いました。DavidGershonyによる[PR #885](https://github.com/block-core/angor/pull/885)は、ランタイムネットワーク切り替え後に間違ったネットワークを使用したBoltz lightningインボイスを修正しました。これはv0.2.30のmainnetデフォルトの後に本番に浮上したはずのバグです。設定は、データワイプ中のオプションのリカバリウォレットファイルパージを提供するようになりました ([PR #883](https://github.com/block-core/angor/pull/883))。

### Sprout v0.3.15: エフェメラルチャネルTTL更新とACPスラッシュコマンド

6月10日にリリースされた[Sprout v0.3.15](https://github.com/block/sprout/releases/tag/v0.3.15)は、6月2日のv0.3.7で始まったランの8番目のリリースです。ニュースレター #25はmesh-llm統合とチャネルセクションの作業とともにv0.3.1からv0.3.6のランをカバーしました。v0.3.7からv0.3.15はその下流であり、ポリッシュといくつかのユーザー向け追加に焦点を当てています。最もユーザーに見える変更は、[PR #902](https://github.com/block/sprout/pull/902)でのエフェメラルチャネルのTTL更新です: ユーザーがエフェメラルチャネルをアーカイブ解除すると、Sproutはチャネルのtime-to-liveを延長するので、アーカイブ解除は元の期限タイマーの下で即座に再アーカイブしません。モバイルカスタム絵文字は、設定の再設計とともに[PR #906](https://github.com/block/sprout/pull/906)に到着し、リアクションカウントは変更時にアニメーションするようになりました ([PR #904](https://github.com/block/sprout/pull/904))。

[PR #905](https://github.com/block/sprout/pull/905)は、複数語の表示名が壊れ、[NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md) `nostr:npub`メンション抽出が静かにドロップされる長年のギャップを修正します。ディレクトリベースのデスクトップ用チームUIは、インストール、同期、および表示コマンドとともに[PR #912](https://github.com/block/sprout/pull/912)で出荷されます。スラッシュコマンドは、[ACP](https://agentclientprotocol.com)コネクタを通じて渡されるようになり ([PR #919](https://github.com/block/sprout/pull/919))、Sprout UIをパスから外したまま、Sproutが`/help`スタイルのコマンドを直接エージェントランタイムに転送できるようになります。

### Wisp v1.1.1: Sparkウォレット統合とnsecペーストガード

6月5日にリリースされた[Wisp v1.1.1](https://github.com/barrydeen/wisp/releases/tag/v1.1.1)は、[PR #548](https://github.com/barrydeen/wisp/pull/548)で[Spark](https://www.spark.money)サブスクリーンを備えた2ティアウォレット接続画面を実現し、[PR #549](https://github.com/barrydeen/wisp/pull/549)でiOSウォレットUIとのダッシュボードパリティを実現します。このリリースには、アプリのどこかで`nsec1`プレフィックス付きペーストを検出し、フィールドがそれを受け入れるのをブロックする、システム全体の[nsecペーストガード](https://github.com/barrydeen/wisp/pull/553)が含まれており、Nostr UXで最も引用されるフットガンの1つを閉じます。QRスキャンログインと`npub`および`nprofile`用のウォッチオンリーモードは[PR #552](https://github.com/barrydeen/wisp/pull/552)で出荷され、ユーザーはプロフィールを読み取り専用でブラウズできます。Zapメッセージは、エンゲージメントドロワーでミニ投稿としてレンダリングされるようになったので ([PR #559](https://github.com/barrydeen/wisp/pull/559))、zapノートはsat金額と並んでそのテキストを運びます。スレッド返信のweb-of-trustフィルターは[PR #583](https://github.com/barrydeen/wisp/pull/583)に着地し、ユーザーはフォローグラフの外のアカウントからの返信スパムを隠すことができます。

### Nostria v3.1.46とnospeak 1.1.3: 通知の再作業とICE再起動

6月7日の[Nostria v3.1.46](https://github.com/nostria-app/nostria/releases/tag/v3.1.46)は、最後のビューから新しい通知のみをカウントするように通知カウンターを再作業する3リリースランを終了し、スクロールによって古い通知をロードするとバッジカウントが膨らむ長年のインフレーションを排除します。[Nostria v3.1.45](https://github.com/nostria-app/nostria/releases/tag/v3.1.45)はlightningおよびQRコード支払いに影響する分割支払いバグを修正し、Androidのコンポジターでは実現不可能として以前に計画されていた半透明UIをドロップしました。

6月4日の[nospeak v1.1.3](https://github.com/psic4t/nospeak/releases/tag/v1.1.3)は、1対1音声通話用のFAILED状態でのICE再起動を追加します。標準のWebRTC動作は、ICE候補が代替パスなしにタイムアウトしたときに通話をドロップします。ICE再起動パスは候補を再交渉するので、通話は一時的なNATまたはネットワークの変更から回復します。Android通話は、ビデオ通話中に画面をオンに保つようになりました。

## 未リリースの変更

### Amethyst: NIP-32 / NIP-F4 / Torトラックを継続する41 PR

Amethystは、リリースタグを切ることなく今週41のPRをマージしました。これは先週の52 PRと、ニュースレター #25でカバーされた[NIP-32](/ja/topics/nip-32/)ハッシュタグラベリングおよび[NIP-F4](/ja/topics/nip-f4/)ポッドキャストの作業の上にあります。アクティブなブランチは、次のタグ付きリリースのために機能を蓄積し続け、先週の目玉追加の上にポリッシュを重ねます: ハッシュタグラベラーの発見、ポッドキャスト画面、音楽トラックとプレイリスト、Tor自己ヒーリングウォッチドッグ、匿名アップロード用のエフェメラル署名者、およびNIP-05フィルタリングを備えたオンチェーンzap。AmethystのPRスループットは、任意のNostrクライアントの中で最も高いままで、未リリースキューは、他のAndroid Nostrクライアントがマッチする必要があるものの事実上のロードマップです。

### Damus: OKメッセージからのリレー追跡とv1.17変更ログ

6月3日にマージされた[Damus PR #3786](https://github.com/damus-io/damus/pull/3786)は、リレーからの成功した`OK`メッセージをポストリレーリストに追加します。以前のDamusビルドは、リレーからの汎用メッセージを受信したときにのみseen-relaysリストを埋めていたので、ポストを確認したがイベントを何も返さなかったリレーはユーザーには見えませんでした。この変更は、投稿が好みのoutboxリレーに着地したことを確認したいユーザーにとって重要です。[PR #3796](https://github.com/damus-io/damus/pull/3796)はプロフィールビューでの`AttributeGraph`サイクルを修正し、[PR #3725](https://github.com/damus-io/damus/pull/3725)は次のタグ付きリリースに先立ってv1.17変更ログを実現します。

### Shopstr: NIP-34デュアル公開

Shopstrの[ngit上のshopstrリポ](https://relay.ngit.dev/npub1u350hpq840naxzkkle4gmdtvzanfxmjd9m9tytn5355aua7jh2cqgfuw39/shopstr.git)は、今週Nostr上で[NIP-34](/ja/topics/nip-34/) gitリポとして発表され、ngitのトラックされたリポに加わりました。ショップクライアントのGitHubリポは主要な開発サーフェスのままです。NIP-34アナウンスは、並行するgit-over-Nostrコラボレーションパスを利用可能にします。これは[Mostro](https://relay.ngit.dev/)の後にNIP-34にデュアル公開する2番目の主要Nostrマーケットプレイスプロジェクトであり、プロジェクトメタデータのNostrのgitトランスポートへの段階的な移行を継続します。

### Hermes-Marmot: MLSを介したAIエージェントゲートウェイ

[hermes-marmot](https://github.com/notmandatory/hermes-marmot)は、[Hermes Agent](https://github.com/NousResearch/hermes-agent)のプラグインで、Rust Marmot Development KitへのPythonバインディングである[mdk-python](https://github.com/marmot-protocol/mdk-python)を使用して、AIエージェントのメッセージングサーフェスを[Marmot](/ja/topics/marmot/) (MLS-over-Nostr) グループに接続します。プラグインにより、ユーザーは[Whitenoise](https://whitenoise.chat)を含む、kind 445 MLSメッセージを話す任意のNostrクライアントからAIエージェントにDMを送信できます。受信DMは[nostr-sdk](https://github.com/rust-nostr/nostr) Pythonバインディング経由で[NIP-59](/ja/topics/nip-59/)ギフトラップアンラッピングを使用し、受信welcomeは`UnwrappedGift.from_gift_wrap`を通じて`mdk.process_welcome`と`mdk.accept_welcome`に流れます。アクセス制御は`MARMOT_ALLOWED_USERS` (カンマ区切りのnpub許可リスト) または開発アクセス用の`MARMOT_ALLOW_ALL_USERS=true`を通じて動作します。

リポは新しく (最終更新は5月27日) 小さいものです。その意義はアーキテクチャ的です: それはLLMエージェントランタイムとMLS暗号化されたNostrメッセージングチャネルの間の最初の公的なブリッジであり、Whitenoise自体を超えたmdk-pythonの最初の本番使用です。このパターンは、両方のエンドポイントがMLSキーを保持し、リレーが暗号文のみを見るエージェント間通信を指し示します。

## NIP更新とプロトコル仕様作業

### NIP-67 EOSE完全性ヒント (PR #2317) マージ

mattnによる[PR #2317](https://github.com/nostr-protocol/nips/pull/2317)は6月6日にマージされ、[NIP-67](/ja/topics/nip-67/)をプロトコルに追加しました。NIPは`EOSE`リレーメッセージをオプションの3番目の要素で拡張します: `["EOSE", <subscription_id>, "finish"]`はフィルターに一致するすべての保存されたイベントが配信されたことを信号送信し、裸の`["EOSE", <subscription_id>]`は完全性の主張を運びません。ヒントを省略するリレーは、クライアントにさらにあるかもしれないと伝えています。NIP-11でNIP-67のアドバタイズを省略するリレーは、既存のレガシーヒューリスティックの下で今日の動作を保ちます。変更は両方向で下位互換性があります: レガシークライアントは末尾の配列要素を無視し、レガシーリレーはそれを省略します。

マージされた仕様の動機は二重です。まず、静かなデータ損失: クライアントは300イベントの内部キャップを持つリレーに対して最後の500ノートを要求し、リレーは300イベントを返し、クライアント (標準の`received < limit`ヒューリスティックを使用) は結果が完全であると結論付けます。201番目からN番目の最も古い一致するノートは、クライアントがその事実に盲目のまま、未読でリレーに残ります。第2に、必須の無駄なラウンドトリップ: リレーがレスポンスを300イベントでキャップするとき、キャップを使い果たすサブスクリプションは、フィルターが正確に300イベントに一致する場合でも、完了を確認するために純粋に`until=<oldest_created_at>`で2番目の`REQ`を必要とします。両方の失敗モードは、すべてのキャップを使い果たしたサブスクリプションで各クライアントによって支払われます。`"finish"`ヒントは、1つの既存のメッセージ上の1つのオプション文字列で、両方のコストを排除します。

### NIP-50オートコンプリート拡張 (PR #2357) マージ

Alex Gleasonによる[PR #2357](https://github.com/nostr-protocol/nips/pull/2357)は6月6日にマージされ、[NIP-50](/ja/topics/nip-50/)検索に`autocomplete:true/false`トークンを追加しました。拡張により、クライアントはクエリをtypeaheadルックアップとしてマークできるので、リレーはトークンなしのクエリのデフォルトとして全文検索を使用しながら、プレフィックスマッチングを使用します。Ditto's のリレーは、フォローパック、リスト、および`title`タグを持つ任意のイベントに対して実装し、タイトルプレフィックスに対するマッチを返します。デフォルトの検索パスは全文スコアリングを実行します。このトークンなしでは、オートコンプリートスタイルのUIはプレフィックス検索の意図を伝える方法がなく、リレーはクエリの形状から推測しなければなりませんでした。トークンは検索ごとのヒントであり、リレー全体の機能ではないので、リレーは一般的なオートコンプリートサポートを主張することなく、1つのイベントクラス (タイトル) に対して実装できます。

### NIP-GART緊急アラートと位置情報ブロードキャスト (PR #2374)

disinqaによる、6月9日に公開された[PR #2374](https://github.com/nostr-protocol/nips/pull/2374)は、信頼されたレシピエントのグループに宛てられた緊急アラートと位置情報ブロードキャストのためのNostr上のプライバシー保護ワイヤーフォーマットを定義します。表明された設計目標は、イベントをリプレイセーフで署名検証可能なエンドツーエンドに保ちながら、送信者アイデンティティ、グループメンバーシップ、およびペイロードをリレー運用者から隠すことです。NIP番号はまだTBDで、提案は初期ドラフトです。ユースケースは標準の緊急アラートパターンです: 脅威にさらされているユーザーは、事前共有された信頼された連絡先のグループだけが復号できる位置情報pingをブロードキャストし、リレーは送信者、受信者セット、およびペイロードに盲目です。ワイヤーフォーマットの詳細はPRに存在し、メンテナーがレビューするにつれて進化する可能性があります。

### NIP-46 logoutメソッド (PR #2373)

hzrd149による、6月8日に公開された[PR #2373](https://github.com/nostr-protocol/nips/pull/2373)は、クライアントがセッションが終了したことをbunkerに明示的に伝えることができるように、`logout`メソッドを[NIP-46](/ja/topics/nip-46/)に追加します。今まで、bunkerセッションを終了する唯一の方法は、セッションタイムアウトを待つか接続の使用を停止することでした。両方とも、なくなったクライアントのセッション状態をbunkerに保持させます。提案は短く (1つの新しいメソッド)、長寿命のbunker統合をよりクリーンにするタイプのハウスキーピング変更です。

### NIP-95ハイブリッドリレー-P2P提案はロングフォームとして回覧

npub `91bea5cd9361504c409aaf459516988f68a2fcd482762fd969a7cdc71df4451c`から6月4日に*Protocolo Híbrido Relay-P2P via WebRTC*というタイトルで、`kind:30023`投稿として[NIP-95仕様](https://github.com/nostr-protocol/nips)のロングフォームが回覧されました。ポルトガル語の文書は、Nostrクライアントが保存されたイベント取得とオフライン配信のためにリレーを引き続き使用しながら、ライブメッセージング用にWebRTC経由で相互に直接接続するハイブリッドピアツーピアリレープロトコルを定義します。作者は仕様を「LLM対応」として明示的にフレームし、AIモデルが動作するクライアントまたはサーバーコードを生成できるレベルの詳細でメッセージ定義、論理フロー、データスキーマ、および状態ルールを提供しました。提案はまだNIP PRとして着地していません。`kind:30023`経由の回覧は、正式なnostr-protocol/nipsプルリクエストの慣習的な前駆体です。

### NIP-44 v3が2番目の署名者を獲得: Claveが仕様を移植

[先週のAmberのv6.2.0 NIP-44 v3ロールアウト](/ja/newsletters/2026-06-03-newsletter/#nip-44-v3-amber-implementation-ahead-of-spec)は、マージされたNIPs PRの前に出荷され、v3を、相互運用するために他のクライアントがミラーしなければならないAmber固有の拡張として残しました。その単一実装のフレーミングは今週変わりました。プッシュベースのiOS NIP-46リモート署名者[Clave](https://github.com/DocNR/clave)は、6月3日と4日に8つのコミットにわたって独立したNIP-44 v3ポートを実現しました。暗号プリミティブは3つのコミットで出荷されます: [HKDF + ECDHキーレイヤー](https://github.com/DocNR/clave/commit/99ca5a5aacb501d1666c489fcdea30187c7853fa)、[v3パディングアルゴリズム](https://github.com/DocNR/clave/commit/8808cdca54d32b4ae57856bd4b07ed73a45e8e5c)、および[トップレベルパブリックAPIと暗号化コンテキスト](https://github.com/DocNR/clave/commit/ae1f506a53cb2c8aa16523540dbe790876c1839e)。それらの上に、NIP-46サーフェスが[LightSigner内のRPCディスパッチ配線](https://github.com/DocNR/clave/commit/f37aa1afc8368862fc3ebac533408442349bfc38)と、[v3コンテキスト (kindとscope) を運ぶPendingRequestスキーマ](https://github.com/DocNR/clave/commit/e51bcb49fc61cfa89b6030d61b203e046aeddb0a)で続くので、署名者はv3ペイロードがどのイベントkindとユースケースに対して承認されたかを記録できます。

Claveはユーザー向けサーフェスでAmberから分岐します。[感度階層を備えた許可付与スキーマ](https://github.com/DocNR/clave/commit/0a8b7de63c1f2994a80a66bf139ec519fab12877)により、ユーザーは選択された感度レベルで特定のイベントkindおよびスコープに対してv3暗号化を許可できます。最初の遭遇では、[一度きりの説明カードを備えたv3コンテキスト認識の承認プロンプト](https://github.com/DocNR/clave/commit/2cf563cb15b0406f5e8aaa0b4e34b887ff1896a1)がv3をユーザーに紹介します。作業はmainにあり[Xcodeプロジェクトに配線](https://github.com/DocNR/clave/commit/4bd0c26d7cf308386ef15e5d96ee5673d6db2d4a)されていますが、未リリースです。最新のタグ付きビルドは5月12日の[v0.2.0-build79](https://github.com/DocNR/clave/releases/tag/v0.2.0-build79)です。

2つの独立した実装がNIPs PRのマージ前に本番パスでNIP-44 v3を実現することで、プロトコルPRが正式化する基礎となるワイヤーフォーマットのケースが強化されます。クロス実装相互運用性テストは、AmberのAndroid承認サーフェスとClaveのiOS感度層モデルを2つの参照ポイントとして、仕様収束へのパスになります。v3を配線する他のリモート署名者 (nsec.appのnoauthは2025年5月以来休止しており、他のbunkerはv3の作業を発表していません) は、コンセンサスをさらに強化するでしょう。

### NIP-34アクティビティ: Irisが新しいhashtreeトランスポートでスタックを採用

Irisは6月8日に[`hashtree`](https://njump.me/nevent1qqs8kmy7a9dn5awurlp9q26lsaetl7dc4wauzdl8ww68dzmn09e074gpzfmhxue69uhhgetdwqhxjunfwvh8gmc850du0)のNIP-34リポアナウンスを、6月9日に[`iris-apps`](https://njump.me/nevent1qqsq4grx000f6p0r8hdv4lqhcgn7707vmktv2j528kn0ldps4y9g49qpzfmhxue69uhhgetdwqhxjunfwvh8gmcmq47as)、[`iris-drive`](https://njump.me/nevent1qqsyj5r0tyqvpp9v7qnras90u6kzqtpqx6ktntwym66m8qyngvf59vqpzfmhxue69uhhgetdwqhxjunfwvh8gmcpts6pf)、および[`iris-chat-rs`](https://njump.me/nevent1qqs0x98hpsv8vmrxvwm2rs9exxttrue5qv5p2n2sqjeylz2kgdmd7tgpzfmhxue69uhhgetdwqhxjunfwvh8gmca8783s)を公開し、`wss://temp.iris.to`から提供される新しい`htree://`スキームの下にクローンURLをアドバタイズしました。hashtreeトランスポートは、GRASPルーティングクローンへのコンテンツアドレスドな代替であり、これら4つのアナウンスはその最初の公的な使用です。リポは空の説明を運び、アーキテクチャの詳細はまだ出現していますが、(カスタムのIris内部マニフェストではなく) NIP-34アナウンスを介して公開するという選択は、IrisがNIP-34 git-over-Nostrスタック全体にコミットしていることを信号送信します。

## NIPディープダイブ: NIP-67 (EOSE完全性ヒント)

[NIP-67](/ja/topics/nip-67/)は、[NIP-01](/ja/topics/nip-01/)で最も長い間続いていた正確性ギャップの1つを閉じます。元の仕様は`EOSE`を`REQ`の保存されたイベントとライブサブスクリプションイベントの間の境界として定義していますが、リレーがすべての保存された一致を配信し終えたのか、内部キャップのために途中で停止したのかを指定したことはありませんでした。すべてのリレーは、クライアントの`limit`とは独立してサブスクリプションごとのキャップ (一般的に300から1000イベント) を強制し、クライアントはそのキャップを観察する方法を持ちませんでした。

標準の回避策は、受信数を要求された`limit`と比較することでした。`received < limit`なら、結果を完全として扱い、そうでなければ`until=<oldest_created_at>`でページネートします。両方のブランチが壊れています。`received < limit`ブランチは静かに切り詰めます: 300でキャップされたリレーに対して500ノートを要求するクライアントは300イベントを見て、`300 < 500`なので結果が完全であると結論付け、残りを決してフェッチしません。リレーで保持されたイベントは、既存のメッセージを通じて「さらに利用可能」を信号送信できません。2番目のブランチとしてのページネーションは無駄です: キャップに正確に一致するフィルターは、完全性を確認するために2番目の`REQ`を必要とし、リレーで完全なフィルタースキャンを消費しながらゼロイベントを返します。

NIP-67の修正は、`EOSE`メッセージの1つのオプション文字列です:

```
["EOSE", "<sub_id>", "finish"]   // 明示的: すべての保存されたイベントが配信された
["EOSE", "<sub_id>"]              // 完全性の主張なし
```

[NIP-11](/ja/topics/nip-11/) `supported_nips`でNIP-67をアドバタイズし、裸の`EOSE`を発するリレーは、クライアントにさらにあると伝えています。アドバタイズを省略するリレーは今日の動作を保ち、クライアントは既存のヒューリスティックにフォールバックします。レガシークライアントは末尾の配列要素を無視します。下位互換性は両方向で保持され、新しい動詞またはイベントkindはありません。

NIP-67を検討する価値があるのは、意図的に制限したスコープです。仕様はカーソルまたはページネーショントークンを定義しないので、`until`ベースのページネーションはメカニズムのままです。リレーキャップは現在の位置に留まり、NIPはそれらの露出を必要としません。NIP-67は、`EOSE`を保存からライブへの境界としての意味を保持し、境界でyes-or-no信号のみを追加します: 「あなたのためにさらにあります」対「それがすべてです」。この最小限のサーフェスが、PRがNIP-01拡張としては比較的短いレビュー期間の後にマージされた理由であり、mattnがPRで英語テキストにAI翻訳が使用されたことを明示的に述べる理由です。変更は、翻訳の不確実性が問題にならないほど十分に小さいです。

キャップを強制するリレーとクライアント間のNIP-67対応の交換の例。リレーからのNIP-11アドバタイズメント:

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1781136000,
  "kind": 11,
  "tags": [],
  "content": "{\"supported_nips\":[1,11,50,67]}",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

続くワイヤーレベルの交換:

```
→ ["REQ", "abc", {"kinds":[1],"limit":500}]
← [...300 EVENTメッセージ...]
← ["EOSE", "abc"]               // "finish"なし: キャップに達し、さらに利用可能
→ ["REQ", "def", {"kinds":[1],"limit":300,"until":1780900000}]
← [...178 EVENTメッセージ...]
← ["EOSE", "def", "finish"]     // 明示的に完了
```

178イベントのレスポンスは、以前は完了を確認するために3番目の`REQ`をトリガーしていました。NIP-67では、クライアントはそこで停止します。

NIP-67は、稀なコンセンサスとともに着地するNIP-01修正としても注目に値します。プロトコルの小さなサーフェスがすべての実装で荷重をかけるので、ほとんどのNIP-01の変更は長い議論スレッドを引き付けます。NIP-67は延長されたレビュー期間 (公開からマージまでおおよそ7週間) の後にマージされました。これは、NIP-01の変更が十分に小さく、失敗モードが十分に具体的なとき (静かなデータ損失、必須の無駄なラウンドトリップ)、プロトコルのメンテナーはコアメッセージ語彙を拡張する意思があることを示唆しています。

## NIPディープダイブ: NIP-50 (検索)

[NIP-50](/ja/topics/nip-50/)は`REQ`メッセージ内の`search`フィルターフィールドを定義し、クライアントがクエリ文字列に対する全文一致でイベントをフィルターするようリレーに要求できるようにします。マージされたベース仕様は意図的に最小限です: `search`フィールドは文字列で、各リレーは独自の検索セマンティクス (どのフィールドがインデックス化されるか、スコアリングがどう機能するか、ステミングが適用されるかどうか) を決定し、リレーはNIP-11文書でNIP-50サポートをアドバタイズします。クライアントは、クエリ文字列自体を通じてのみ検索アルゴリズムを制御します。

このミニマリズムはNIP-50の強みと制約の両方です。強みは、任意のリレーが任意の品質レベルで検索を実装できることです: 基本的な部分文字列スキャンは仕様を満たし、ElasticsearchまたはMeilisearchを実行するリレーは等しく満たします。制約は、クライアントが検索意図を表現する方法を欠いていることです。プロフィールメンションtypeahead UIは表示名に対するプレフィックスマッチングを望みます。全文コンテンツ検索はノート本体全体でトークン化された全文スコアリングを望みます。同じ`search`フィールドが両方を運び、リレーはクエリの形状から推測しなければなりません。

[PR #2357](https://github.com/nostr-protocol/nips/pull/2357)は、最初のNIP-50拡張トークンを追加します: 検索クエリに埋め込まれた`autocomplete:true`または`autocomplete:false`は、クライアントがどのモードを望むかを信号送信します。Ditto's リレーは、フォローパック、リスト、および`title`タグを持つ任意のイベントに対してトークンを実装し、`autocomplete:true`が存在するときにプレフィックスマッチングに切り替えます。トークンはクエリ内にインラインで存在するので (別のフィルターフィールドはそのままに)、検索文字列とともに移動し、ワイヤープロトコルのバンプは必要ありません:

```
search: "fiat autocomplete:true"
```

このようなトークン形状のヒントは、NIP-50がリレー固有の方言を常に扱ってきた方法です。リレーは既に`language:en`や`domain:example.com`のようなトークンをサポートしていました。それぞれはリレー固有のままで、各リレーは独自の方言を文書化します。NIP-50のPR #2357は、`autocomplete`をリレー限定のトークンから仕様に祝福されたものに昇格させ、リレー全体でtypeahead対応検索への道を開きます。

kind 0プロフィールタイトルをインデックス化するリレーをターゲットにする、autocompleteトークンを備えたNIP-50 `REQ`の例:

```json
{
  "id": "b7c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f7081a2b3c4d5e6f70819a2b3c4d5",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1781136000,
  "kind": 1,
  "tags": [
    ["client", "example-mention-picker"]
  ],
  "content": "Sent search: kinds=[0], search=\"fiat autocomplete:true\", limit=10",
  "sig": "12d3e4f5061728394a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f7081a2b3c4d5e6f70819a2b3c4d5e6f7081a2b3c4d5e6f708192"
}
```

実際のワイヤーレベルのREQ:

```
["REQ", "mention-picker", {"kinds":[0],"search":"fiat autocomplete:true","limit":10}]
```

トークンを認識しないリレーは、`autocomplete:true`をリテラル検索文字列の一部として扱い、全文マッチングにフォールバックし、正しい (異なるようにランク付けされた) 結果を返します。優雅な劣化により、利用可能なときにプレフィックスマッチングを好むクライアントは、無条件にトークンを含めることが安全です。

次に可能性の高いNIP-50拡張は、kindごとのランキング制御です: デフォルトの関連性スコアの代わりに「`created_at`降順でランク付け」を言うヒント。いくつかのリレーは既に`sort:newest`をリレー限定トークンとして受け入れ、`autocomplete`を仕様に持ち込んだのと同じ昇格パスが適用されます。検索は、リレーが結果の品質で競争する数少ないNostrプリミティブの1つのままです。配信の信頼性はすべての準拠するリレーで同じです。増分トークンにより、クライアントはリレーが重量級の新しい仕様を出荷することを強制することなく、その品質競争を活用できます。
