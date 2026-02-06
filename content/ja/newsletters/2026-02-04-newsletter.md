---
title: 'Nostr Compass #8'
date: 2026-02-04
translationOf: /en/newsletters/2026-02-04-newsletter.md
translationDate: 2026-02-04
draft: false
type: newsletters
---

Nostr Compassへようこそ。Nostrの週刊ガイドです。

**今週の内容:** rust-nostrがSDKのアーキテクチャを刷新する21のPRで大規模なAPI再設計を出荷。Nostria 3.0がデュアルペインナビゲーション、リスト管理、完全なUI刷新でローンチ。VectorがSIMDアクセラレーションを追加し65x-184xの高速化を達成、暗号化グループメッセージング向け[Marmot](/ja/topics/marmot/)プロトコルサポートを出荷。FrostrがTestFlight経由でiOSに閾値署名をもたらす。Damusがクロスリレーコンテンツ発見のために[NIP-19 (Bech32エンコードエンティティ)](/ja/topics/nip-19/)リレーヒントを実装。Primal AndroidがNWC暗号化とウォレットトランザクションエクスポートを追加。nostr-toolsとNDKが信頼性の改善を受ける。NIP-82（ソフトウェアアプリケーション）がデバイスプラットフォームの98%をカバーするよう拡張。NIPsリポジトリが[NIP-47 (Nostr Wallet Connect)](/ja/topics/nip-47/)のホールドインボイスサポートをマージ。新しいプロトコル提案にはポッドキャスティング向けNIP-74、ブラウザイベントデータベース向けNIP-DB、分散型コンテンツキュレーション向けTRUSTed Filtersスイートが含まれる。新プロジェクトとしてコンテンツ移行用Instagram to Nostr v2、分散型3Dプリントマーケットプレイスを立ち上げるPod21、AIエージェント管理コミュニティを導入するClawstr、ライブストリーミングとビデオ通話機能を拡張するShoshoとNosCallが登場。

## ニュース

### rust-nostrが大規模なAPI再設計を出荷

[rust-nostr](https://github.com/rust-nostr/nostr) SDKは今週、ライブラリ全体に破壊的変更を導入する21のマージされたPRで大幅なアーキテクチャ刷新を受けました。この再設計はほとんどのRust開発者が依存するコアAPIに影響を与えます。

[PR #1245](https://github.com/rust-nostr/nostr/pull/1245)は通知APIを再設計し、[PR #1244](https://github.com/rust-nostr/nostr/pull/1244)は`RelayNotification::Shutdown`を`RelayStatus::Shutdown`に置き換えてよりクリーンな状態処理を実現。署名者APIは[PR #1243](https://github.com/rust-nostr/nostr/pull/1243)を通じて他のSDKパターンと整合。ClientとRelayメソッドは[PR #1242](https://github.com/rust-nostr/nostr/pull/1242)でクリーンアップされ、クライアントオプションはビルダーパターンを使用するようになりました（[PR #1241](https://github.com/rust-nostr/nostr/pull/1241)）。

メッセージ送信APIは[PR #1240](https://github.com/rust-nostr/nostr/pull/1240)で再設計され、REQアンサブスクリプションは[PR #1239](https://github.com/rust-nostr/nostr/pull/1239)で、リレー削除は[PR #1229](https://github.com/rust-nostr/nostr/pull/1229)で対応。[オープンPR #1246](https://github.com/rust-nostr/nostr/pull/1246)はブロッキングAPIのサポートを追加して再設計を締めくくります。

これらの変更はSDKに一貫性をもたらしますが、既存のプロジェクトからの移行作業が必要になります。rust-nostr上で構築している開発者は、アップグレード前に変更ログを注意深く確認すべきです。

### Instagram to Nostr v2がコンテンツ移行を可能に

新しいツールにより、クリエイターは既存のコンテンツを集中型プラットフォームからNostrに移行できます。[Instagram to Nostr v2](https://github.com/primalpaul1/instagram-to-nostr-v2)は、ユーザーの秘密鍵にアクセスすることなく、Instagram、TikTok、Twitter、Substackからのインポートをサポートします。

このツールは一般的なオンボーディング障壁に対処します：新しいプラットフォームでゼロから始めることに躊躇するユーザーがコンテンツ履歴を保存できるようになります。また、新規ユーザーへのNostrアカウントのギフティングや既存アカウントへのコンテンツ提案もサポートしており、他の人のプロトコルへの移行を支援するのに便利です。

### Pod21：分散型3Dプリントネットワーク

[Pod21](https://github.com/gobrrrme/Pod21) ([pod21.com](https://pod21.com))はNostrをマーケットプレイス調整に使用して、3Dプリンターオペレーターとバイヤーを接続します。プラットフォームには[NIP-17 (プライベートダイレクトメッセージ)](/ja/topics/nip-17/)互換のDMボットが含まれており、マーケットプレイスのやり取りを処理し、バイヤーがプリントをリクエストし、暗号化されたダイレクトメッセージを通じてメーカーと交渉できます。

メーカーはプリント容量と機能をリストし、バイヤーはリストを閲覧してボットを通じて注文を開始します。アーキテクチャは他のNostrコマースアプリケーションと同様のパターンに従います：リレーベースの発見、注文調整のための暗号化メッセージング、決済のためのLightning。Pod21はRidestrやShopstrと共に、プロトコルを通じて現実世界の取引を調整するNostrアプリケーションに加わります。

### Clawstr：AIエージェントソーシャルネットワーク

[Clawstr](https://github.com/clawstr/clawstr)は、AIエージェントがNostr上でコミュニティを作成・管理するRedditに触発されたプラットフォームとしてローンチ。プラットフォームにより、自律エージェントがトピックコミュニティを確立し、コンテンツをキュレートし、ユーザーと関わることができます。コミュニティはサブレディットのように機能しますが、AIモデレーターとキュレーターが議論を導きます。アーキテクチャはエージェント間およびエージェントと人間のインタラクションにNostrのオープンプロトコルを使用し、分散型ソーシャルメディアにおけるコミュニティ形成の新しいモデルを確立します。

## リリース

### Ridestr v0.2.0：RoadFlareリリース

[Ridestr](https://github.com/variablefate/ridestr)は「RoadFlareリリース」と名付けられた[v0.2.0](https://github.com/variablefate/ridestr/releases/tag/v0.2.0)を出荷し、パーソナルライドシェアネットワークを導入。この機能により、ライダーはお気に入りのドライバーを信頼ネットワークに追加できます。ドライバーはフォロワーを承認し、暗号化された位置情報を共有することで、ライダーは信頼するドライバーがオンラインで近くにいるときを確認できます。ライドリクエストは既知のドライバーに直接送られます。

支払いの信頼性が向上し、自動エスクローリカバリー、デバイス間のウォレット同期改善、プログレッシブポーリングによる高速支払い処理が実現。[PR #37](https://github.com/variablefate/ridestr/pull/37)はこれらの機能をサポートするフェーズ5-6インフラストラクチャを追加。[v0.2.1](https://github.com/variablefate/ridestr/releases/tag/v0.2.1)は支払いダイアログのバグとライド後の「お気に入りに追加」フローのホットフィックスが続きました。

### Nostria 3.0

sondrebが構築したグローバルスケール向けクロスプラットフォームクライアント[Nostria](https://github.com/nostria-app/nostria)がバージョン3.0を出荷し、完全なUI刷新、新ロゴ、数百の修正を含みます。このリリースは集中的な6週間の開発サイクルを表しています。

デュアルペインナビゲーションが最大のUX変更であり、デスクトップユーザーがリスト、詳細、スレッド間を移動する際のコンテキスト切り替えを削減できます。新しいホームセクションは利用可能なすべての機能の概要を提供し、すべての画面が統一されたツールバー、レイアウト、機能性を共有します。

リスト管理が最も重要な機能アップデートであり、アプリケーション全体に統合されています。ユーザーはプロファイルリストを管理し、Streams、Music、Feedsの任意の機能でコンテンツをフィルタリングできます。スレッドのスパムにうんざりしていますか？お気に入りでフィルタリングして彼らの返信のみを表示できます。Quick Zapsは設定可能な値でワンタップzappingを追加。Copy/Screenshotはどこでもイベントを共有するためのクリップボードスクリーンショットを生成。Muted Wordsはプロファイルフィールド（name、display_name、NIP-05）でフィルタリングするようになり、ユーザーは単一の禁止ワードですべてのブリッジプロファイルをブロックできます。設定は検索可能になり、より速い構成変更が可能に。

このリリースはBOLT11とBOLT12支払いリクエストレンダリング、テキストサイズとフォント選択、メッセージセクションでの参照コンテンツ（記事やイベントなど）のレンダリング付き「Note-to-Self」メッセージングを追加。新しい共有ダイアログにより、メール、ウェブサイト、または複数の受信者へのダイレクトメッセージを通じた迅速な共有が可能に。追加機能にはカスタム絵文字セット、Interests（動的フィードとしてのハッシュタグリスト）、ブックマーク、パブリックリレーフィード、Nostriaアイコンがどのオプションを開くかを含む完全なメニューカスタマイズがあります。

Android、iOS、Windows、および[nostria.app](https://www.nostria.app/)のWebで利用可能。

### Applesauce v5.1.0

hzrd149の[Applesauce](https://github.com/hzrd149/applesauce)ライブラリスイートがすべてのパッケージでv5.1.0をリリース。[applesauce-signers](https://github.com/hzrd149/applesauce/releases/tag/applesauce-signers%405.1.0)はNostr Connectリモート署名者での`switch_relays`と`ping`メソッドのサポートを追加し、署名者接続をプログラマティックに管理するのに便利。[applesauce-loaders](https://github.com/hzrd149/applesauce/releases/tag/applesauce-loaders%405.1.0)は並列非同期ローディング用の`loadAsyncMap`を導入。[applesauce-react](https://github.com/hzrd149/applesauce/releases/tag/applesauce-react%405.1.0)は`useAction().run()`にパディング引数を追加。[applesauce-core](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.1.0)はイベントからストアへのマッピングを更新し、`onlyEvents`を必要とせずに文字列を直接処理。

### nak v0.18.3

fiatjafの[nak](https://github.com/fiatjaf/nak)（Nostr Army Knife）はmattnからの安定性修正で[v0.18.3](https://github.com/fiatjaf/nak/releases/tag/v0.18.3)に到達。このリリースはミントURLが`://`セパレーターを欠く場合のパニックを防止し、日付値を使用する前にdateparserエラーを検証し、AUTH challengeタグ解析のエッジケースを処理。これらの防御的な修正により、不正な入力を処理する際のCLIの耐障害性が向上。

### Aegis v0.3.7

クロスプラットフォームデスクトップ署名者[Aegis](https://github.com/ZharlieW/Aegis)は、[NIP-07 (ブラウザ拡張インターフェース)](/ja/topics/nip-07/)署名付きのNostr App Browserサポートを追加する[v0.3.7](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.7)を出荷。このリリースは[NIP-04 (暗号化ダイレクトメッセージ)](/ja/topics/nip-04/)と[NIP-44 (バージョン付き暗号化)](/ja/topics/nip-44/)暗号化イベントを記録し、ユーザーはどのアプリケーションが暗号化操作を要求したかを追跡できます。ブラウザセグメントはプラットフォームでフィルタリングしてWebアプリのみを表示するようになりました。

### Bitchat v1.5.1 (iOS)

NostrとBluetoothメッシュを使用するオフライン対応メッセージングアプリ[Bitchat](https://github.com/permissionlesstech/bitchat)は、iOSセキュリティ強化付きの[v1.5.1](https://github.com/permissionlesstech/bitchat/releases/tag/v1.5.1)をリリース。[PR #1012](https://github.com/permissionlesstech/bitchat/pull/1012)は処理前にNostrイベント署名を検証し、無効なgiftwrapと埋め込みパケットを拒否し、サイズ超過ペイロードを制限し、偽装されたBLEアナウンス送信者IDをブロック。[PR #998](https://github.com/permissionlesstech/bitchat/pull/998)は送信者IDを接続UUIDにバインドすることでiOS BLEメッシュ認証を修正し、メッシュネットワークでのアイデンティティスプーフィングを防止。[PR #972](https://github.com/permissionlesstech/bitchat/pull/972)は複数のメッシュデバイスが近くにあるときのピア発見フラッドを防ぐ通知レート制限を追加。

### KeyChat v1.39.2

[KeyChat](https://github.com/keychat-io/keychat-app)は[PR #148](https://github.com/keychat-io/keychat-app/pull/148)を通じて[NIP-47](/ja/topics/nip-47/) Nostr Wallet Connectサポートを追加する[v1.39.2](https://github.com/keychat-io/keychat-app/releases/tag/v1.39.2%2B6495)をリリース。ユーザーはメッセージングアプリ内での支払いのために外部Lightningウォレットを接続できるようになりました。このリリースはmacOSデスクトップ通知も追加。

### Nostrmo v3.5.0

クロスプラットフォームFlutterクライアント[Nostrmo](https://github.com/haorendashu/nostrmo)はフィードシステムを刷新する[v3.5.0](https://github.com/haorendashu/nostrmo/releases/tag/3.5.0)を出荷。アップデートは固定フィードをカスタマイズ可能な代替物に置き換えます：General Feed、Mentioned Feed、Relay Feedはそれぞれ新しい編集ページで設定可能。このリリースはより良いイベントルーティングのためのoutboxモデルサポートを実装し、設定可能なサイズ制限とサブスクリプションサポートでローカルリレー機能を拡張。

### Shosho v0.11.1

Nostr向けライブストリーミングアプリ[Shosho](https://github.com/r0d8lsh0p/shosho-releases)は録画とVOD機能付きの[v0.11.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.11.1)をリリース。アップデートはストリームを視聴している人を表示するルームプレゼンスインジケーター、より良いディスカッション整理のためのスレッド化されたチャット会話、[NIP-46](/ja/topics/nip-46/)経由のiOSでのNostr Connectサポートを追加。ストリーマーは視聴者とのリアルタイムチャットインタラクションを維持しながら、放送を後で視聴するために保存できます。

### NosCall v0.5.0

Nostr向けオーディオおよびビデオ通話アプリ[NosCall](https://github.com/sanah9/noscall)は、カテゴリ別に通話を整理するコンタクトグループ、接続最適化のためのリレー管理、改善されたNATトラバーサルのための設定可能なICEサーバー設定付きの[v0.5.0](https://github.com/sanah9/noscall/releases/tag/v0.5.0-release)を出荷。このリリースはダークモードサポートも追加。NosCallは通話シグナリングと調整にNostrを使用し、集中型サーバーなしでピアツーピア通話を可能にします。

### diVine 1.0.4

rabbleのショートフォームループビデオクライアント[diVine](https://github.com/divinevideo/divine-mobile)は、Zapstore提出に先立つAndroidプレリリースアルファとして[1.0.4](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.4)をリリース。このリリースはnsecインポート、nsecBunkerとAmberによる[NIP-46 (Nostr Connect)](/ja/topics/nip-46/)リモート署名、nostrconnect:// URL処理を含むNostr鍵管理のテストに焦点を当てています。チームはリレー互換性と他のクライアントとのビデオ相互運用性についてフィードバックを募集中。[PR #1265](https://github.com/divinevideo/divine-mobile/pull/1265)は絶対コンテナパスの代わりに相対パスを保存することで、アプリ更新後にビデオクリップが使用不能になっていたiOSファイルパス処理を修正。[PR #1251](https://github.com/divinevideo/divine-mobile/pull/1251)はコメントからプロファイルを表示する際のナビゲーション問題を修正。

### Zeus v0.12.2

[Zeus](https://github.com/ZeusLN/zeus)は安定版リリースとして[v0.12.2](https://github.com/ZeusLN/zeus/releases/tag/v0.12.2)を出荷し、[以前のエディションでカバーしたNWC修正](/ja/newsletters/2026-01-28-newsletter/#zeus-v0122-beta---nwc-fixes)を統合。

### Frostr Igloo iOS TestFlight

[Frostr](https://github.com/FROSTR-ORG) ([frostr.org](https://frostr.org/))は[Igloo for iOS](https://github.com/FROSTR-ORG/igloo-ios)を[TestFlight](https://testflight.apple.com/join/72hjQe3J)でローンチし、閾値署名をAppleデバイスに拡張。FrostrはFROST（Flexible Round-Optimized Schnorr Threshold）署名を使用してnsec鍵をデバイス間に分散されたシェアに分割し、フォールトトレランスを持つk-of-n署名を可能にします。「デモモード」で参加するユーザーはライブ2-of-2閾値署名実験に参加し、プロトコルのリアルタイム調整機能を実演します。iOSリリースは12月に[NIP-55 (Android署名者)](/ja/topics/nip-55/)サポート付きでクロスアプリ署名リクエスト向けに出荷された[Igloo for Android](https://github.com/FROSTR-ORG/igloo-android)（v0.1.2）に加わります。両モバイルクライアントは[Iglooデスクトップ](https://github.com/FROSTR-ORG/igloo-desktop)と[Frost2x](https://github.com/FROSTR-ORG/frost2x)ブラウザ拡張を補完します。

## プロジェクトアップデート

### DamusがNIP-19リレーヒントを実装

[Damus](https://github.com/damus-io/damus)はイベント取得用の[NIP-19](/ja/topics/nip-19/)リレーヒント消費を実装する[PR #3477](https://github.com/damus-io/damus/pull/3477)をマージ。この機能により、[NIP-10 (返信スレッド)](/ja/topics/nip-10/)、[NIP-18 (リポスト)](/ja/topics/nip-18/)、NIP-19参照からヒントを抽出することで、ユーザーの設定プール外のリレー上のノートを表示できます。実装は参照カウント付きクリーンアップでエフェメラルリレー接続を使用し、永続的なリレープール拡張を回避。

追加の修正にはLightningインボイス解析（[PR #3566](https://github.com/damus-io/damus/pull/3566)）、ウォレットビュー読み込み（[PR #3554](https://github.com/damus-io/damus/pull/3554)）、リレーリストタイミング（[PR #3553](https://github.com/damus-io/damus/pull/3553)）、視覚的な「ポッピング」を軽減するプロファイルプリロード（[PR #3550](https://github.com/damus-io/damus/pull/3550)）が含まれます。[ドラフトPR #3590](https://github.com/damus-io/damus/pull/3590)は進行中の[NIP-17](/ja/topics/nip-17/)プライベートDMサポートを示しています。

### Primal AndroidがNWC暗号化を出荷

[Primal Android](https://github.com/PrimalHQ/primal-android-app)はウォレットインフラストラクチャに焦点を当てた18のマージされたPRで非常に活発な週を過ごしました。アプリはLightsparkのセルフカストディアルLightningプロトコルであるSparkと統合しています。[PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874)はNWC暗号化サポートを追加し、[PR #872](https://github.com/PrimalHQ/primal-android-app/pull/872)は接続確立時にNWC infoイベントを送信。

[PR #870](https://github.com/PrimalHQ/primal-android-app/pull/870)はウォレットトランザクションのCSVエクスポートを有効にし、会計と税務目的に便利。[PR #716](https://github.com/PrimalHQ/primal-android-app/pull/716)はNote Editorにローカルアカウントスイッチャーを追加。複数のウォレット復元修正（[PR #876](https://github.com/PrimalHQ/primal-android-app/pull/876)、[PR #875](https://github.com/PrimalHQ/primal-android-app/pull/875)、[PR #873](https://github.com/PrimalHQ/primal-android-app/pull/873)）は非Sparkウォレット構成のユーザー向けのエッジケースに対処。

### Marmot TypeScript SDKがメッセージ履歴を追加

[Marmot](https://github.com/marmot-protocol/marmot)プロトコルのTypeScript実装が開発を継続。hzrd149による[PR #38](https://github.com/marmot-protocol/marmot-ts/pull/38)はリファレンスチャットアプリケーション向けにページネーション付きのメッセージ履歴永続化を実装し、[PR #39](https://github.com/marmot-protocol/marmot-ts/pull/39)はライブラリのエルゴノミクスを改善。

Rust側では、[PR #161](https://github.com/marmot-protocol/mdk/pull/161)が失敗時のメッセージコンテキストを保持するリトライ可能な状態処理を実装し、[PR #164](https://github.com/marmot-protocol/mdk/pull/164)はSQLiteでのtokioパニックを回避するためにstd::sync::Mutexに切り替え。whitenoise-rsバックエンドは[Amber統合](https://github.com/marmot-protocol/whitenoise-rs/pull/418)（[PR #418](https://github.com/marmot-protocol/whitenoise-rs/pull/418)）を追加し、[MDKとnostr-sdk 0.44にアップグレード](https://github.com/marmot-protocol/whitenoise-rs/pull/467)（[PR #467](https://github.com/marmot-protocol/whitenoise-rs/pull/467)）、NewMessageとGroupInviteイベントタイプによるリアルタイム通知ストリーミングを[PR #460](https://github.com/marmot-protocol/whitenoise-rs/pull/460)で導入。

### HAVENが定期的なWoTリフレッシュを追加

パーソナルリレー[HAVEN](https://github.com/bitvora/haven)は、定期的な[Web of Trust](/ja/topics/web-of-trust/)リフレッシュを追加する[PR #108](https://github.com/bitvora/haven/pull/108)をマージ。この機能により、ユーザーのソーシャルグラフの進化に応じて信頼スコアが最新に保たれ、時間の経過とともにスパムフィルタリングの精度が向上。

### nostr-tools

コアJavaScriptライブラリ[nostr-tools](https://github.com/nbd-wtf/nostr-tools)は今週複数の改善を受けました。コミットには[NIP-27 (テキストノート参照)](/ja/topics/nip-27/)メンションでの[改行後のハッシュタグ解析修正](https://github.com/nbd-wtf/nostr-tools/commit/c2423f7f31853d97fef2e3d649204cec328e81d5)、接続クリーンアップのための[アイドル追跡付き壊れたリレーオブジェクトの自動プルーニング](https://github.com/nbd-wtf/nostr-tools/commit/ab802c8dbe35d29feb732ba54e82a346c21c32e2)、シングルスレッドパフォーマンス最適化のための[メッセージキュー削除](https://github.com/nbd-wtf/nostr-tools/commit/be9b91318fea6a0cb154b8734a15b50a4c1e7638)、より良いTypeScriptインポートのための[ソースファイルエクスポート](https://github.com/nbd-wtf/nostr-tools/commit/05b1fba5113182ac0aa3c72d1f511cd956a7c139)が含まれます。

### NDK

[NDK](https://github.com/nostr-dev-kit/ndk)は[デバイススリープ/ウェイクサイクル後の再接続と古い接続処理の修正](https://github.com/nostr-dev-kit/ndk/commit/33e759508bc656dc45d3d77c741edf581af323f3)付きの[beta.71](https://github.com/nostr-dev-kit/ndk/commit/26abea24726ed844fdd091744ac9f768f1a530a0)を出荷し、モバイルアプリケーションの信頼性の問題に対処。

### Notedeck

Damusチームのデスクトップクライアント[Notedeck](https://github.com/damus-io/notedeck)には、[NIP-34 (Git コラボレーション)](/ja/topics/nip-34/)ビューアを追加する[オープンPR #1279](https://github.com/damus-io/notedeck/pull/1279)があります。これにより、Nostrリレーに公開されたgitリポジトリ、パッチ、issueをクライアント内で直接閲覧できるようになり、Notedeckがngitベースのワークフロー向けの潜在的なフロントエンドになります。

### njump

Nostr Webゲートウェイ[njump](https://github.com/fiatjaf/njump)は[PR #152](https://github.com/fiatjaf/njump/pull/152)を通じて2つの[NIP-51 (リスト)](/ja/topics/nip-51/)イベントタイプのサポートを追加。ゲートウェイはkind:30000 Follow Sets（クライアントが異なるコンテキストで表示できるユーザーのカテゴリ別グループ）とkind:39089 Starter Packs（共有とグループフォロー用に設計されたキュレートされたプロファイルコレクション）をレンダリングするようになりました。これらの追加により、ユーザーがneventリンクを共有するときにnjumpがコミュニティキュレートリストを表示できます。

### Amethyst

Androidクライアント[Amethyst](https://github.com/vitorpamplona/amethyst)はプレイヤービューからのビデオ共有を妨げていたバグを修正（[PR #1695](https://github.com/vitorpamplona/amethyst/pull/1695)）。「ビデオを共有」オプションは、コンテンツパラメータがコントロールボタンコンポーネントに渡されていなかったため表示されませんでした。ユーザーはプレイヤーから直接Nostrビデオコンテンツを他のアプリに共有できるようになりました。[PR #1693](https://github.com/vitorpamplona/amethyst/pull/1693)は特定の不正なイベントを解析する際に発生していたJackson JSONデシリアライズクラッシュを修正。

### Jumble

リレーフィードブラウジングに焦点を当てたWebクライアント[Jumble](https://github.com/CodyTseng/jumble)は[PR #743](https://github.com/CodyTseng/jumble/pull/743)でクリップボード経由のオーディオファイルアップロードを追加。ユーザーは投稿エディタにオーディオファイルを直接ペーストでき、設定されたメディアサーバーにアップロードしてノートにURLを埋め込みます。この機能は既存の画像ペースト機能を反映。

### Flotilla

hodlbodの[NIP-29 (リレーベースグループ)](/ja/topics/nip-29/)コミュニティクライアント[Flotilla](https://github.com/coracle-social/flotilla)は[PR #270](https://github.com/coracle-social/flotilla/pull/270)を通じて通知を出荷。アップデートはアンカーベースのポーリングからWeb向けローカルプル通知とモバイル向けプッシュ通知にアラートシステムをリファクタリング。アーキテクチャは提案されたNIP-9a標準（下記の[PR #2194](https://github.com/nostr-protocol/nips/pull/2194)を参照）を実装し、ユーザーがリレーにwebhookコールバックを登録し、フィルターが一致したときに暗号化されたイベントペイロードを受信します。

### Formstr

Nostrネイティブフォームアプリケーション[Formstr](https://github.com/abh3po/nostr-forms)は[PR #422](https://github.com/abh3po/nostr-forms/pull/422)でフォームインポートと暗号化フォームサポートを追加。ユーザーはレスポンスリンクを通じてまたは他のFormstrインスタンスから既存のフォームをインポートできるようになりました。暗号化機能により、フォーム作成者は指定された受信者のみが提出を読めるように応答を制限でき、機密情報を収集するアンケートに便利。

### Pollerama

[nostr-tools](https://github.com/nbd-wtf/nostr-tools)上に構築された[Pollerama](https://github.com/abh3po/nostr-polls) ([pollerama.fun](https://pollerama.fun))は[PR #141](https://github.com/abh3po/nostr-polls/pull/141)と[PR #142](https://github.com/abh3po/nostr-polls/pull/142)を通じて投票用の[NIP-17](/ja/topics/nip-17/) DM共有を追加。ユーザーは暗号化ダイレクトメッセージを通じて連絡先に投票を直接共有できるようになりました。

### Nostrability Schemata

Nostrイベント用のJSON検証スキーマコレクション[Nostrability schemata](https://github.com/nostrability/schemata)は[PR #59](https://github.com/nostrability/schemata/pull/59)を通じて[NIP-59 (Gift Wrap)](/ja/topics/nip-59/)カバレッジを追加。アップデートにはkind 13（seal）とkind 1059（gift wrap）イベントのスキーマが含まれ、既存の[NIP-17](/ja/topics/nip-17/)スキーマカバレッジを補完。

### Vector

[NIP-17](/ja/topics/nip-17/)、[NIP-44](/ja/topics/nip-44/)、[NIP-59](/ja/topics/nip-59/)をゼロメタデータ暗号化に使用するプライバシー重視のデスクトップメッセンジャー[Vector](https://github.com/VectorPrivacy/Vector)は、SIMDアクセラレーションパフォーマンス最適化を導入する[PR #39](https://github.com/VectorPrivacy/Vector/pull/39)をマージ。16進数エンコードは65倍高速化、画像プレビュー生成は最大38倍高速化、バイナリサーチインデックスによるメッセージルックアップは184倍高速化。PRはApple Silicon向けARM64 NEONイントリンシクスとWindowsおよびLinux向けランタイム検出付きx86_64 AVX2/SSE2を追加。メッセージ構造体を472から128バイトに削減し、インターニングによりnpubストレージを99.6%削減してメモリ使用量が低下。

Vector v0.3.0（2025年12月）はMLSプロトコルベースのグループメッセージング用に[MDK (Marmot Development Kit)](https://github.com/marmot-protocol/mdk)を統合し、前方秘匿性を持つエンドツーエンド暗号化グループをクライアントにもたらしました。MIP-04ファイル共有はMLSグループ向けのimeta添付ファイルを処理し、[White Noise](/ja/newsletters/2026-01-28-newsletter/#marmot-protocol-updates)との相互運用性を考慮して設計。このリリースはWebXDCベースのP2Pマルチプレイヤーゲームを持つMini Appsプラットフォーム、The Nexusという分散型アプリストア、アプリ内支払い用PIVX ウォレット統合、完全な履歴追跡付きメッセージ編集、画像アップロード中の4倍メモリ削減も導入。

## NIPアップデート

[NIPsリポジトリ](https://github.com/nostr-protocol/nips)への最近の変更：

**マージ済み：**

- **[NIP-47：ホールドインボイスサポート](https://github.com/nostr-protocol/nips/pull/1913)** - [NIP-47 (Nostr Wallet Connect)](/ja/topics/nip-47/)がホールドインボイスをサポートするようになり、受取人が明示的に支払いを決済またはキャンセルする必要がある高度な支払いワークフローが可能に。PRは3つの新しいRPCメソッドを追加：`make_hold_invoice`は事前生成されたプリイメージと支払いハッシュを使用してホールドインボイスを作成、`settle_hold_invoice`は元のプリイメージを提供して支払いを請求、`cancel_hold_invoice`は支払いハッシュを使用して支払いを拒否。新しい`hold_invoice_accepted`通知は支払い者が支払いをロックしたときに発火。これにより、アンロック用支払い、マーケットプレイスエスクローシステム、支払いゲーティングなどのユースケースが可能に。実装は[Alby Hub](https://github.com/getAlby/hub/pull/1298)、[Alby JS-SDK](https://github.com/getAlby/js-sdk/pull/382)、[dart NDK](https://github.com/relaystr/ndk/pull/147)で進行中。

- **[NIP-05：小文字要件](https://github.com/nostr-protocol/nips/pull/2208)** - [NIP-05 (ドメイン検証)](/ja/topics/nip-05/)が`nostr.json`ファイル内の16進数公開鍵とローカル名の両方に小文字を明示的に要求するように。これは仕様で暗黙的でしたが明記されておらず、一部の実装が大文字小文字混合を使用し、他の実装が小文字に正規化していたため相互運用性の問題が発生。NIP-05識別子を検証するクライアントは、キーや名前に大文字を含む`nostr.json`応答を拒否すべきです。

- **[NIP-73：国コード](https://github.com/nostr-protocol/nips/pull/2205)** - [NIP-73 (ジオタグ)](/ja/topics/nip-73/)がgeohashの代替としてISO 3166国コードをサポートするように。イベントは正確な座標を必要とせずに国レベルの位置を示す`["g", "US", "countryCode"]`タグを含めることができます。これにより、正確な位置が不要または望ましくないアプリケーション向けに国ベースのコンテンツフィルタリングと発見が可能に。PRは仕様ドキュメントに欠落していたgeohash例も追加。

**オープンPRとディスカッション：**

- **[NIP-82：ソフトウェアアプリケーション](https://github.com/nostr-protocol/nips/pull/1336)** - franzapがこのドラフト仕様への大幅なアップデートを発表。kind 30063リリースイベントを使用してNostr経由でソフトウェアアプリケーションを配布する方法を定義。アップデートはmacOS、Linux、Windows、FreeBSD、WASM環境、VS Code拡張、Chrome拡張、Web Bundles/PWAを含む、グローバルで約98%のデバイスプラットフォームをカバーするように。チームは次にAndroid、PWA、iOSサポートに注力し、開発者にこの共有標準への収束を呼びかけ。Zapstoreは今後数週間で新フォーマットへの移行を予定。

- **[NIP-74：ポッドキャスト](https://github.com/nostr-protocol/nips/pull/2211)** - ポッドキャスト番組（kind 30074）とエピソード（kind 30075）用のアドレス可能イベントを定義。番組にはタイトル、説明、カテゴリ、カバー画像などのメタデータが含まれます。エピソードは親番組を参照し、エンクロージャURL、再生時間、チャプターマーカーを含みます。仕様はPodcasting 2.0メタデータ標準と統合し、Lightning経由のV4V（value-for-value）マネタイゼーション用のvalueタグを含みます。NostrネイティブポッドキャストパブリッシングプラットフォームのTRUSTed[transmit.fm](https://transmit.fm)のようなプラットフォームは、このフォーマットを使用してリレーに直接公開でき、ポッドキャスターが仲介者なしでコンテンツを配信可能に。

- **[NIP-FR：フレンズオンリーノート](https://github.com/nostr-protocol/nips/pull/2207)** - ViewKeyと呼ばれる共有対称鍵を使用して、ユーザー定義のフレンドリストにのみ表示されるノートを公開するメカニズムを提案。作成者はViewKeyを使用してNIP-44でノート（kind 2044）を暗号化します。ViewKey自体は[NIP-59 (Gift Wrap)](/ja/topics/nip-59/)を通じて各友人に一度だけ配布されます。ViewKeyを持つ友人はノートを復号して読むことができ、それ以外の全員は暗号文しか見えません。作成者が友人を削除すると、ViewKeyがローテーションされます：新しい鍵が生成され、gift wrapを通じて残りの全友人に再配布され、削除された友人が将来の投稿にアクセスできないことが保証されます。このアプローチはコンテンツ暗号化（対称、効率的）と鍵配布（非対称、友人ごと）を分離し、頻繁にリクエストされるプライバシー機能を実現しながらプロトコルを軽量に保ちます。

- **[NIP-DB：ブラウザNostrイベントデータベースインターフェース](https://nostrhub.io/e/1a451c1581888215ae5c311d36c8a7c7d9e5e81f1f4010de4afaf7fcbd553e90)** ([spec](https://github.com/hzrd149/nostr-bucket/blob/master/nip.md)) - ローカルNostrイベントストレージを提供するブラウザ拡張用の標準`window.nostrdb`インターフェースを提案。APIにはイベント追加、IDまたはフィルタによるクエリ、マッチカウント、更新サブスクリプション用のメソッドが含まれます。Webアプリケーションはこのインターフェースを使用して、リレーリクエストなしでローカルキャッシュされたイベントから読み取り、帯域幅とレイテンシーを削減できます。hzrd149の[nostr-bucket](https://github.com/hzrd149/nostr-bucket)ブラウザ拡張がリファレンス実装を提供し、すべてのブラウザタブにインターフェースを注入。コンパニオン[ポリフィルライブラリ](https://github.com/hzrd149/window.nostrdb.js)は拡張なしの環境向けにIndexedDBを使用して同じAPIを実装。

- **[TRUSTed Filters](https://nostrhub.io/e/237667820943d1c8bbe7ab7732623ae51b337f177776ece439d4a8be84708eb7)** - vitorpamonaの[マージされたTrusted Assertions PR #1534](https://github.com/nostr-protocol/nips/pull/1534)を基に構築された、分散型コンテンツキュレーション用の5つの関連提案のスイート。コア仕様はTrust Provider Preferencesを宣言するためのkind 17570イベントを導入し、ユーザーはイベントフィルタリングとランキングでどのサービスを信頼するかを指定できます。信頼プロバイダーはクライアントがサブスクライブできるアサーション（kind 37571）、統計（kind 37572）、ランキング（kind 37573）を公開。システムはフィルタータイプと変換を指定するW/wタグ付きのプラグインアーキテクチャを使用。これにより、スパム検出、レピュテーションスコアリング、コンテンツランキングのような計算コストの高い操作を専用インフラストラクチャで実行しながら、ユーザーはどのプロバイダーを信頼するかの制御を維持できます。スイートにはフィルタープリセット、ユーザーランキング、信頼されたイベント、プラグイン定義用の個別仕様が含まれます。

- **[NIP-9a：プッシュ通知](https://github.com/nostr-protocol/nips/pull/2194)** - hodlbodがkind 30390登録イベントを使用するリレーベースのプッシュ通知の標準を提案。ユーザーは受信したいイベントのフィルターとwebhookコールバックURLを含む登録を作成。登録はリレーのpubkey（NIP-11の`self`フィールドから）に暗号化。一致するイベントが発生すると、リレーはイベントID（重複排除用のプレーンテキスト）とイベント自体（ユーザーにNIP-44暗号化）を含むコールバックにPOST。このアーキテクチャにより、リレーは通知をプッシュしながら、仲介プッシュサーバーからイベントコンテンツを保護できます。Flotillaの[PR #270](https://github.com/coracle-social/flotilla/pull/270)がこの標準を実装。

- **[Catallax](https://github.com/SigmaEnterprise/Catallax)** - kind 33400イベントを使用したエスクロー付き分散型コントラクトワークプロトコルを提案。システムは3つの役割を定義：アービターは利用可能性と条件を発表、パトロンはエスクローされたBitcoinで資金提供されたタスクを作成、フリーエージェントは支払いを請求するために作業を完了。アービターは必要に応じて紛争を解決。プロトコルはトラストレスなフリーランス作業調整を可能にし、成果物が受け入れられるか仲裁が終了するまで資金がロック。

## NIP詳細解説：NIP-47 (Nostr Wallet Connect)

[NIP-47](/ja/topics/nip-47/)はNostr Wallet Connect（NWC）を定義し、通信レイヤーとしてNostrを使用したリモートLightningウォレット制御のプロトコルです。今週のホールドインボイスサポート追加により、NWCはLightning操作の全範囲をカバーするようになりました。

プロトコルはシンプルな交換を通じて動作します。ウォレットアプリケーションはその機能を説明する「wallet info」イベント（kind 13194）を公開。クライアントアプリケーションはインボイスの支払い、インボイスの作成、残高確認などの操作をウォレットに要求する暗号化リクエスト（kind 23194）を送信。ウォレットは暗号化された結果（kind 23195）で応答。

NWCはクライアントとウォレット間で[NIP-44](/ja/topics/nip-44/)暗号化を使用し、ウォレット操作用の専用キーペアを使用して、ユーザーのメインIDから分離します。この分離により、NWC接続が侵害されてもユーザーのNostr IDは露出しません。

**サポートされているメソッド：**

仕様はコアLightning操作用のメソッドを定義：`pay_invoice`は支払いを送信、`make_invoice`は受取用のインボイスを生成、`lookup_invoice`は支払いステータスをチェック、`get_balance`はウォレット残高を返し、`list_transactions`は支払い履歴を提供。新たにマージされた`pay_keysend`はインボイスなしの支払いを可能にし、`hold_invoice`は条件付き支払いをサポート。

**イベント例：**

ウォレットサービスはその機能を宣伝するinfoイベント（kind 13194）を公開：

```json
{
  "kind": 13194,
  "pubkey": "<wallet service pubkey>",
  "content": "pay_invoice get_balance make_invoice lookup_invoice list_transactions notifications",
  "tags": [
    ["encryption", "nip44_v2"],
    ["notifications", "payment_received payment_sent"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<wallet service signature>"
}
```

クライアントはインボイスを支払うための暗号化リクエスト（kind 23194）を送信：

```json
{
  "kind": 23194,
  "pubkey": "<client ephemeral pubkey from connection URI secret>",
  "content": "<NIP-44 encrypted: {\"method\": \"pay_invoice\", \"params\": {\"invoice\": \"lnbc50n1...\"}}>",
  "tags": [
    ["p", "<wallet service pubkey>"],
    ["encryption", "nip44_v2"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<client ephemeral key signature>"
}
```

ウォレットサービスは支払い結果で応答（kind 23195）：

```json
{
  "kind": 23195,
  "pubkey": "<wallet service pubkey>",
  "content": "<NIP-44 encrypted: {\"result_type\": \"pay_invoice\", \"result\": {\"preimage\": \"...\"}, \"error\": null}>",
  "tags": [
    ["p", "<client ephemeral pubkey>"],
    ["e", "<request event id>"]
  ],
  "created_at": "<unix timestamp>",
  "id": "<event hash>",
  "sig": "<wallet service signature>"
}
```

応答の`e`タグは元のリクエストを参照し、クライアントが応答をリクエストにマッチさせることを可能にします。

**ホールドインボイス：**

今週の[PR #1913](https://github.com/nostr-protocol/nips/pull/1913)はエスクロースタイルの支払いを可能にするホールドインボイスサポートを追加。受取人がプリイメージを解放して即座に支払いを請求する標準インボイスとは異なり、ホールドインボイスは受取人がこの決定を延期できます。支払い者がホールドインボイスに送信すると、資金は支払い経路に沿ってロック。受取人は決済（プリイメージを解放して資金を請求）またはキャンセル（支払いを拒否して支払い者に資金を返却）を選択。どちらのアクションも発生しない場合、支払いはタイムアウトして自動的に資金が返却。PRは3つのNWCメソッド（`make_hold_invoice`、`settle_hold_invoice`、`cancel_hold_invoice`）と`hold_invoice_accepted`通知を追加。このメカニズムはRidestrのライドシェアエスクローやマーケットプレイス紛争解決などのアプリケーションを支えます。

**現在の実装：**

主要ウォレットがNWCをサポート：Zeus、Alby、Primal（今週の[PR #874](https://github.com/PrimalHQ/primal-android-app/pull/874)時点）がすべてウォレット側サポートを実装。クライアント側では、Damus、Amethyst、およびほとんどの主要Nostrクライアントがzapと支払いのためにNWCウォレットに接続可能。

プロトコルは関心事の分離を可能に：ユーザーは1つのデバイスでウォレットを実行しながら、別のデバイスからNostrとやり取りでき、Nostrリレーが通信チャネルとして機能。このアーキテクチャにより、モバイルクライアントは直接資金を保持する必要がなくなり、ウォレットインフラストラクチャをソーシャルクライアントから分離することでセキュリティが向上。

**セキュリティ考慮事項：**

NWC接続は機密として扱うべきです。暗号化がメッセージ内容を保護する一方、ウォレットpubkeyと接続シークレットは保護が必要。アプリケーションはユーザーが接続を取り消し、支出制限を設定できるようにすべきです。プロトコルは機能制限をサポートしており、ウォレットは特定の接続が実行できる操作を制限できます。

## NIP詳細解説：NIP-59 (Gift Wrap)

[NIP-59](/ja/topics/nip-59/)は任意のNostrイベントを複数の暗号化レイヤーにカプセル化し、リレーやオブザーバーから送信者のIDを隠すプロトコルを定義。今週のフレンズオンリーノート（NIP-FR）とプッシュ通知（NIP-9a）の提案は両方ともgift wrappingに依存しており、理解する価値のある基礎的なプライバシープリミティブです。

**3つのレイヤー：**

Gift wrappingは3つのネストされた構造を使用：

1. **Rumor**（未署名イベント）：署名なしのNostrイベントとしての元のコンテンツ。リレーは未署名イベントを拒否するため、rumorを直接リレーに送信することはできません。

2. **Seal**（kind 13）：rumorは[NIP-44](/ja/topics/nip-44/)を使用して暗号化され、kind 13イベントに配置。sealは実際の作成者の鍵で署名されます。これが作成者の証明となる暗号的証拠です。

3. **Gift Wrap**（kind 1059）：sealは暗号化され、ランダムなワンタイムキーペアで署名されたkind 1059イベントに配置。gift wrapは受信者へのルーティング用の`p`タグを含みます。

**よくある誤解：否認可能性**

仕様は未署名rumorが「否認可能性」を提供すると言及していますが、これは誤解を招きます。sealレイヤーは実際の作成者によって署名されています。受信者がgift wrapを復号し、次にsealを復号すると、誰がメッセージを送ったかの暗号的証拠を持ちます。受信者は自分の秘密鍵を露出させずに送信者のIDを明らかにするゼロ知識証明を構築することさえできます。

gift wrapが実際に提供するのは**オブザーバーからの送信者プライバシー**です：リレーと第三者はランダムな鍵で署名されたgift wrapしか見ないため、誰がメッセージを送ったか判断できません。しかし受信者は常に知っており、それを証明できます。

**イベント例：**

仕様からの完全な3レイヤー構造（「Are you going to the party tonight?」を送信）：

rumor（未署名、リレーに公開不可）：
```json
{
  "created_at": 1691518405,
  "content": "Are you going to the party tonight?",
  "tags": [],
  "kind": 1,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "id": "9dd003c6d3b73b74a85a9ab099469ce251653a7af76f523671ab828acd2a0ef9"
}
```

seal（kind 13、実際の作成者が署名、暗号化rumorを含む）：
```json
{
  "kind": 13,
  "pubkey": "611df01bfcf85c26ae65453b772d8f1dfd25c264621c0277e1fc1518686faef9",
  "content": "AqBCdwoS7/tPK+QGkPCadJTn8FxGkd24iApo3BR9/M0uw6n4RFAFSPAKKMgkzVMo...",
  "created_at": 1703015180,
  "tags": [],
  "id": "28a87d7c074d94a58e9e89bb3e9e4e813e2189f285d797b1c56069d36f59eaa7",
  "sig": "02fc3facf6621196c32912b1ef53bac8f8bfe9db51c0e7102c073103586b0d29..."
}
```

gift wrap（kind 1059、ランダムなエフェメラル鍵が署名、暗号化sealを含む）：
```json
{
  "kind": 1059,
  "pubkey": "18b1a75918f1f2c90c23da616bce317d36e348bcf5f7ba55e75949319210c87c",
  "content": "AhC3Qj/QsKJFWuf6xroiYip+2yK95qPwJjVvFujhzSguJWb/6TlPpBW0CGFwfuf...",
  "created_at": 1703021488,
  "tags": [["p", "166bf3765ebd1fc55decfe395beff2ea3b2a4e0a8946e7eb578512b555737c99"]],
  "id": "5c005f3ccf01950aa8d131203248544fb1e41a0d698e846bd419cec3890903ac",
  "sig": "35fabdae4634eb630880a1896a886e40fd6ea8a60958e30b89b33a93e6235df7..."
}
```

注目：sealの`pubkey`は実際の作成者（`611df01...`）で、gift wrapの`pubkey`はランダムなワンタイム鍵（`18b1a75...`）。リレーはgift wrapしか見ないため、実際の作成者にメッセージを帰属させることができません。

**各レイヤーが保護するもの：**

rumorは未署名であり、リレーに直接公開できません。sealは実際の作成者によって署名され、受信者に対して作成者を証明します。gift wrapはランダムなワンタイム鍵で署名され、リレーやオブザーバーから実際の作成者を隠します。受信者のみが両方のレイヤーを通じて復号し、元のコンテンツに到達してseal上の作成者の署名を検証できます。

**現在のアプリケーション：**

[NIP-17 (プライベートダイレクトメッセージ)](/ja/topics/nip-17/)は暗号化DMにgift wrapを使用し、古いNIP-04スキームを置き換えます。提案されたNIP-FR（フレンド限定ノート）は、Gift Wrappingを使用してViewKeyを友人に配布し、友人はそれらの鍵で暗号化されたノートを復号します。NIP-9a（プッシュ通知）はgift wrap原則を使用して通知ペイロードを暗号化。

**メタデータ保護：**

タイミング分析を阻止するためにタイムスタンプをランダム化すべきです。リレーはkind 1059イベントを提供する前にAUTHを要求し、マークされた受信者にのみ提供すべきです。複数の受信者に送信する場合は、それぞれに個別のgift wrapを作成します。

---

今週は以上です。何か構築していますか？共有したいニュースはありますか？プロジェクトの報道を希望しますか？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">NIP-17 DMでお問い合わせください</a>、またはNostrで見つけてください。
