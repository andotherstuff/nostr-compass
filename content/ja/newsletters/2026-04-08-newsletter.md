---
title: 'Nostr Compass #17'
date: 2026-04-08
translationOf: /en/newsletters/2026-04-08-newsletter.md
translationDate: 2026-04-09
draft: false
type: newsletters
---

Nostr Compassへようこそ。Nostrの週刊ガイドです。

**今週の内容:** [Amethyst](https://github.com/vitorpamplona/amethyst)が、Arti Tor統合と再設計されたShorts UIを備えた[v1.08.0](#amethystがarti-torを出荷しpure-kotlinのmlsとmarmotを統合)を出荷し、[MLS](/ja/topics/mls/)と[Marmot](/ja/topics/marmot/)のpure Kotlin実装を[Quartz](/ja/topics/quartz/)ライブラリへ統合しました。[Nostur](https://github.com/nostur-com/nostur-ios-public)は、動画録画、アニメーションGIFプロフィール、プライベート返信を備えた[v1.27.0](#nostur-v1270が動画録画とプライベート返信を追加)を出荷しました。[Shosho](https://github.com/r0d8lsh0p/shosho-releases)は、Shows（OBSに接続できるカスタム配信情報）とTikTok風の縦型動画カルーセルを備えた[v0.15.0](#shosho-v0150がshowsと縦型動画カルーセルをローンチ)を開始しました。[Nymchat](https://github.com/Spl0itable/NYM)は、ローテーションするephemeral keysを使う[強化版NIP-17グループチャットへ戻すためMarmotを巻き戻し](#nymchatがmarmotを巻き戻し強化版nip-17グループチャットを出荷)、[Nostr VPN](https://github.com/mmalmi/nostr-vpn)は6リリースにわたり[exit node対応とUmbrelパッケージング](#nostr-vpnがexit-node対応とumbrelパッケージングを出荷)を進めました。[Amber](https://github.com/greenart7c3/Amber)は接続ごとの[NIP-46](/ja/topics/nip-46/)署名鍵とZapstoreアプリ内更新を備えた[v6.0.0-pre1](#amber-v600-pre1が接続ごとのnip-46署名鍵を追加)へ進みました。[Notedeck](https://github.com/damus-io/notedeck)はZapstore経由のAPK self-updateを備えた[v0.10.0-beta](#notedeck-v0100-betaがzapstore-self-updateを出荷)に到達し、[NIP-58](/ja/topics/nip-58/)（Badges）では[kind migration](#nipアップデート)が入りました。今週のNIPディープダイブは[NIP-17](/ja/topics/nip-17/)（Private Direct Messages）と[NIP-46](/ja/topics/nip-46/)（Nostr Remote Signing）です。

## トップストーリー

### AmethystがArti Torを出荷し、pure KotlinのMLSとMarmotを統合

[Amethyst](https://github.com/vitorpamplona/amethyst)はvitorpamplonaがメンテナンスするAndroidクライアントで、[v1.07.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.3)から[v1.08.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.08.0)まで4リリースを出荷し、未リリース作業の大きなまとまりを[Quartz](/ja/topics/quartz/)ライブラリ（共有Kotlin Multiplatform Nostrモジュール）へ統合しました。見出しとなるリリースはv1.08.0「Arti Tor」で、アプリのTor接続をCベースのTorライブラリから、Tor ProjectによるRust実装の[Arti](https://gitlab.torproject.org/tpo/core/arti)へ移行します。この移行は、従来のC Torバインディング下で起きていたランダムクラッシュに対処するものです。Artiはメモリ安全性とasync I/Oを目的にRustでゼロから書かれた、Tor ProjectによるCコードベースの長期的な置き換えです。

v1.07.3ではShorts UIも再設計され、ページ送り型のデザインが、画像、shorts、長尺動画向けのedge-to-edgeフィードへ置き換えられました。同じリリースでbadgesはkind `10008`へ、bookmarksはkind `10003`へ移行され、今週[マージされた](#nipアップデート)[NIP-58](/ja/topics/nip-58/)のkind migrationと足並みをそろえています。v1.07.4ではNostr Wallet Connectのsecret処理問題が修正され、v1.07.5では画像アップロード時のクラッシュが修正されました。

mainには入っているものの、まだタグ付きリリースには含まれていない作業として、チームは[MLS](/ja/topics/mls/)と[Marmot](/ja/topics/marmot/)プロトコルの完全なKotlin実装を書き上げ、ネイティブC/Rustライブラリバインディングを不要にしました。[PR #2147](https://github.com/vitorpamplona/amethyst/pull/2147)はMarmot MLSグループメッセージングの中核層を追加し、[PR #2149](https://github.com/vitorpamplona/amethyst/pull/2149)はグループチャットUIを追加し、[PR #2146](https://github.com/vitorpamplona/amethyst/pull/2146)はsubscription manager付きの送受信メッセージプロセッサを追加します。[PR #2141](https://github.com/vitorpamplona/amethyst/pull/2141)はMLS group stateの永続化とKeyPackage rotation管理を追加し、[PR #2150](https://github.com/vitorpamplona/amethyst/pull/2150)は改良されたGroupInfo署名を備えた完全なMLS test suiteを追加し、[PR #2158](https://github.com/vitorpamplona/amethyst/pull/2158)はKeyPackage公開状態の追跡を追加します。[PR #2166](https://github.com/vitorpamplona/amethyst/pull/2166)はNostrの暗号処理向けにpure Kotlinのsecp256k1実装を追加し、ネイティブCライブラリ依存を置き換えます。Kotlin版MLS実装と組み合わせることで、[Quartz](/ja/topics/quartz/)はネイティブバインディングなしでNostr署名とMarmotグループメッセージングを実行できるようになり、iOSを含むKotlin Multiplatformターゲットへの道が開かれます。

チームは[NIP-AC](/en/topics/nip-ac/)（P2P Voice and Video Calls）サポートも進めています。[PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143)はNIP-AC call state machine向けの完全なtest suiteを追加し、[PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164)はアプリ再起動後に古いcall offerが再発火しないようにしています。

### Nostur v1.27.0が動画録画とプライベート返信を追加

[Nostur](https://github.com/nostur-com/nostur-ios-public)はiOS Nostrクライアントで、4月2日に[v1.27.0](https://github.com/nostur-com/nostur-ios-public/releases/tag/v1.27.0)を出荷しました。このリリースは、アップロード前トリミング付きのアプリ内動画録画を追加しており、ユーザーは短いクリップを撮影し、長さを整え、クライアントを離れずに公開できます。アニメーションGIF対応はプロフィール写真とバナー写真にも広がり、アニメーションWebPレンダリングも追加されました。新しいShortcuts統合により、Apple Shortcutsの自動化からNostr投稿を送れるようにもなっています。さらに、private repliesが追加され、Nosturと他クライアントの間でメッセージ配信に影響していたDM互換性問題も修正されました。

### Shosho v0.15.0がShowsと縦型動画カルーセルをローンチ

[Shosho](https://github.com/r0d8lsh0p/shosho-releases)はNostrライブ配信アプリで、4月7日に[v0.15.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.0)と[v0.15.1](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.15.1)を出荷しました。目玉機能はShowsです。配信者はライブ開始前にカスタムの番組情報を設定し、その番組をOBSや任意の外部エンコーダへ接続できます。これにより、「今何を配信しているのか」というメタデータが、実際に配信を開始する操作から切り離され、配信者はタイトル、説明、商品を事前に準備できるようになります。同じリリースでは、ライブ、クリップ、リプレイをフルスクリーンフィードでスワイプして見ていけるTikTok風の縦型動画カルーセルと、プロフィールページから直接動画クリップを公開したり商品を追加したりできるQuick Addも入りました。v0.15.1では、キーボードがライブ配信チャット入力欄を隠していたバグが修正されています。

## 今週のリリース

### Notedeck v0.10.0-betaがZapstore self-updateを出荷

[Notedeck](https://github.com/damus-io/notedeck)はDamusチームによるデスクトップおよびモバイルクライアントで、APK self-update向けのテスト用プレリリースとして[v0.10.0-beta.1](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.1)と[v0.10.0-beta.2](https://github.com/damus-io/notedeck/releases/tag/v0.10.0-beta.2)を出荷しました。[PR #1417](https://github.com/damus-io/notedeck/pull/1417)はAndroidでNostr/Zapstore updater経由のAPK self-updateを追加し、[Newsletter #14](/en/newsletters/2026-03-18-newsletter/#notedeck-moves-release-discovery-onto-nostr)で扱ったNostrネイティブな更新発見の作業を土台にしています。更新フローは、relayへ公開されたNostrイベントを通じて新しいリリースを発見し、その後、開発者がホストしている場所（GitHub releases、Blossom CDN、そのほかの配布元）からAPKをダウンロードし、署名済みNostrイベントに対してSHA-256 hashを検証してからインストールします。[PR #1438](https://github.com/damus-io/notedeck/pull/1438)はLoginボタンとCreateAccountボタンが即座に前画面へ戻ってしまうwelcome screenのバグを修正し、[PR #1424](https://github.com/damus-io/notedeck/pull/1424)はAgentium AI session viewでのテキストあふれを修正します。

### Amber v6.0.0-pre1が接続ごとのNIP-46署名鍵を追加

[Amber](https://github.com/greenart7c3/Amber)は[NIP-55](/ja/topics/nip-55/)（Android Signer Application）署名者アプリで、4月4日に[v6.0.0-pre1](https://github.com/greenart7c3/Amber/releases/tag/v6.0.0-pre1)を出荷しました。最も重要な変更は、[NIP-46](/ja/topics/nip-46/)（Nostr Remote Signing）bunkerプロトコル向けの接続ごとの署名鍵です。Amberは、すべてのbunker接続に単一のkeypairを使う代わりに、接続された各クライアントごとに別の鍵を生成するようになりました。1つのクライアント接続が侵害されても、攻撃者は他のクライアントに対して署名者になりすますことができません。

[PR #377](https://github.com/greenart7c3/Amber/pull/377)はZapstore経由のアプリ内更新確認とインストールを追加し、[Notedeck](#notedeck-v0100-betaがzapstore-self-updateを出荷)と並んでNostrネイティブなアプリ配布を採用しました。[PR #375](https://github.com/greenart7c3/Amber/pull/375)はAndroidKeyStore障害時にクラッシュさせず警告を表示するようにし、[PR #371](https://github.com/greenart7c3/Amber/pull/371)は無制限なストレージ増大を防ぐため、サイズ制限とcontent切り詰めを伴うデータベースクリーンアップを追加しています。このプレリリースには、[先週扱ったv5.0.xサイクル](/en/newsletters/2026-04-01-newsletter/#amber-v502-through-v504)から[NIP-42](/ja/topics/nip-42/) relay auth whitelistとmnemonic recovery phrase loginも引き継がれています。

### Nostriaがネイティブモバイルアプリを出荷

[Nostria](https://github.com/nostria-app/nostria)はSondreBがメンテナンスするクロスプラットフォームNostrクライアントで、Android向けのネイティブモバイルアプリを、[v3.1.11](https://github.com/nostria-app/nostria/releases/tag/v3.1.11)から[v3.1.18](https://github.com/nostria-app/nostria/releases/tag/v3.1.18)まで8リリースにわたり公開しました。最も重要な新機能は、[Amber](https://github.com/greenart7c3/Amber)やAegisのような署名者向けのネイティブlocal signer対応です。Linux、macOS、Windows向けの[デスクトップインストーラー](https://www.nostria.app/download)も利用できます。[PR #610](https://github.com/nostria-app/nostria/pull/610)は適応的runtime制限とpreview URL cleanupによりフィードのメモリ負荷を下げ、v3.1.14では[Web of Trust](/ja/topics/web-of-trust/)プロバイダーであるBrainstormとの統合が修正されました。v3.1.15は音楽機能の改善に集中しています。新しいAndroidアプリは[Zapstore](https://zapstore.dev/apps/app.nostria)で入手できます。

### diVine 1.0.8がresumable uploadsとDMsを出荷

[diVine](https://github.com/divinevideo/divine-mobile)は短尺動画クライアントで、87件のマージ済みPRを含む[1.0.8](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.8)を出荷しました。resumable uploadsにより、接続が不安定な環境でアップロードが中断されても、クリエイターは最初からやり直すのではなく、チャンク単位で続きから再開できます。このリリースでは動画品質とビットレート設定、ダブルタップでのlike、DM改善も追加されました。[PR #2722](https://github.com/divinevideo/divine-mobile/pull/2722)はデスクトップ動画撮影向けのmacOS camera pluginを追加し、[PR #2820](https://github.com/divinevideo/divine-mobile/pull/2820)は通知システムをenrichmentとgroupingを備えたBLoCアーキテクチャへ移行します。チームはAI生成のステッカーとカテゴリ画像もOpenMoji SVGへ置き換えました（[PR #2844](https://github.com/divinevideo/divine-mobile/pull/2844)、[PR #2842](https://github.com/divinevideo/divine-mobile/pull/2842)）。

### Manent v1.3.0が機密ノートのぼかし表示とNIP-42 authを追加

[Manent](https://github.com/dtonon/manent)はプライベートな暗号化ノートおよびファイルストレージアプリで、4月2日に[v1.3.0](https://github.com/dtonon/manent/releases/tag/v1.3.0)を出荷しました。ユーザーはノートをsensitiveとしてマークできるようになり、一覧表示ではぼかして、何気ないスクロール中に私的な内容が露出しないようにできます。このリリースでは[NIP-42](/ja/topics/nip-42/)（Authentication of Clients to Relays）対応も追加され、Manentはイベントを受け入れる前に認証を要求するrelayへも接続できるようになりました。Manentはすべてのデータをユーザーのkeypairを使ってNostr relays上に暗号化して保存するため、NIP-42対応はストレージに使えるrelayの集合を広げます。

### Wisp v0.17.0からv0.17.3がライブ配信zapsとwallet backupを追加

[Wisp](https://github.com/barrydeen/wisp)はAndroid Nostrクライアントで、[v0.16.2-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.2-beta)から[v0.17.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.17.3-beta)まで6リリース、44件のマージ済みPRを出荷しました。v0.17.0ではwallet backup向けの安全プロンプトとzap UX改善が追加されています。[v0.17.1](https://github.com/barrydeen/wisp/releases/tag/v0.17.1-beta)はプラットフォーム横断のライブ配信チャット可視化とライブ配信zap機能を追加しました。[PR #423](https://github.com/barrydeen/wisp/pull/423)はprofileのauto-search、zap success animation、ユーザーステータス改善を追加し、[PR #426](https://github.com/barrydeen/wisp/pull/426)は大きなtag listを持つイベントで`computeId`がout-of-memoryクラッシュする問題を修正します。v0.16.x系列ではemoji shortcode autocomplete、グループチャットUI改善、すべての通知経路にわたるブロック済みユーザーフィルタリングも入りました。

### Mostroがdeep links、Nostr為替レート、重複支払い修正を出荷

[Mostro](https://github.com/MostroP2P/mostro)はNostr上に構築されたP2P Bitcoin取引所で、今週はサーバーデーモンとモバイルクライアントの両方で更新がありました。サーバー側では、[PR #692](https://github.com/MostroP2P/mostro/pull/692)が古い注文書き込みによって重複支払いが起きるのを防ぎます。このバグは、同じ取引に対して売り手へ二重に支払いが行われる可能性がありました。[PR #693](https://github.com/MostroP2P/mostro/pull/693)はorder全体の上書きではなく、dev_fee書き込みに対して対象を絞った更新を使います。

[Mostro Mobile](https://github.com/MostroP2P/mobile)はFlutterクライアントで、4月3日に[v1.2.3](https://github.com/MostroP2P/mobile/releases/tag/v1.2.3)を出荷しました。このリリースは異なるMostroインスタンスからのdeep linksを扱えるため、ユーザーは正しい取引所サーバーへルーティングされるリンクをそのままタップできます。[PR #498](https://github.com/MostroP2P/mobile/pull/498)はバックグラウンド通知パイプラインでadminおよびdispute DMを検出し、アプリはHTTP/cache fallback付きでNostrから為替レートを取得するようになりました。[PR #560](https://github.com/MostroP2P/mobile/pull/560)は、特定のネットワーク条件でアプリがrelayへ到達できなくなるrelay connection blockingバグを修正します。

### Unfiltered v1.0.12がhashtagsとcommentsを追加

[Unfiltered](https://github.com/dmcarrington/unfiltered)は画像中心のcontentに焦点を当てたNostrクライアントで、[v1.0.12](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.12)を出荷しました。[PR #69](https://github.com/dmcarrington/unfiltered/pull/69)はhashtag対応を追加し、[PR #72](https://github.com/dmcarrington/unfiltered/pull/72)は投稿へcommentsを書いて表示する機能を追加します。[PR #71](https://github.com/dmcarrington/unfiltered/pull/71)は、1投稿に複数画像がある場合のナビゲーション問題を修正しました。

### Primal Androidがwallet multi-account sharingとremote signer auto-reconnectを出荷

[Primal](https://github.com/PrimalHQ/primal-android-app)はAndroid Nostrクライアントで、4月7日にリリースを出荷しました。この更新ではwallet multi-account sharingが追加され、Dev Toolsにはwallet削除付きのoverflow menuが入りました。remote signerは接続断時に自動再接続するようになり、wallet serviceにも独自のauto-reconnectロジックが追加されています。修正には、poll zap votesがTop Zapsに表示されなくなる変更、空のpoll optionでのクラッシュ防止、wallet未設定時の残高非表示、NWCレスポンス内でWalletException型をerror codeへマッピングする対応が含まれます。

### Titan v0.1.0がBitcoin名登録付きネイティブ`nsite://`ブラウザをローンチ

[Titan](https://github.com/btcjt/titan)はNostr web向けのネイティブデスクトップブラウザで、4月7日に[v0.1.0](https://github.com/btcjt/titan/releases/tag/v0.1.0)を出荷しました。Titanは、Bitcoin上に登録された人間可読名を参照して`nsite://` URLを解決し、Nostr relaysへサイトのcontent eventsを問い合わせ、[Blossom](/ja/topics/blossom/)サーバーから取得したページをレンダリングします。その結果、DNSもTLS証明書もホスティング事業者も要らないweb閲覧体験が生まれます。名前はBitcoinトランザクションに結び付いた[web interface](https://npub1hmq6xuqnplk5lw0h3700cujmx5gymqn5wrn42u6432r6ntzumezqc3marw.nsite.lol/register)を通じて登録されます。初期リリースはmacOS `.dmg`（ARM、Intel向けRosetta 2対応）として提供され、Nix開発環境サポートも含みます。

### Bikel v1.5.0がde-Googled phones向けネイティブforeground serviceを出荷

[Bikel](https://github.com/Mnpezz/bikel)は、Nostrを使ってライド記録を公共インフラデータへ変える分散型サイクリングトラッカーで、4月4日に[v1.5.0](https://github.com/Mnpezz/bikel/releases/tag/v1.5.0)を出荷しました。このリリースでは、GMS依存のExpo TaskManagerからカスタムのネイティブforeground serviceへ移行し、LineageOS、GrapheneOS、そのほかのde-Googled Android環境で信頼性の高いバックグラウンド走行追跡を確保します。Bikel BotはCashu nutzapsによる自律的なeCash回収を行うdual-pocket architectureも獲得しました。v1.4.3とv1.4.2では非標準Android環境向けのバックグラウンド追跡同期が修正され、アプリにはOSM bike rack map pointの切り替えも追加されています。

### SproutがNIP-01、NIP-23、NIP-33対応を追加

[Sprout](https://github.com/block/sprout)はBlockによる、Nostr relayを内蔵したコミュニケーションプラットフォームで、4月6日に[desktop/v0.1.0-rc7](https://github.com/block/sprout/releases/tag/desktop/v0.1.0-rc7)を出荷しました。今週、チームは[NIP-23](/en/topics/nip-23/)（Long-form Content）のkind `30023`記事、`d`タグをキーに置き換える[NIP-33](/en/topics/nip-33/) parameterized replaceable events、そして[NIP-01](/ja/topics/nip-01/)/[NIP-02](/en/topics/nip-02/)のkind `1` text notesとkind `3` follow listsへの対応を追加しました。リリースには、54テーマを持つ適応型IDEテーマシステム、workflowおよびagent実行履歴のUX改善、members sidebarの整理も含まれています。

### mesh-llm v0.56.0が分散config protocolを出荷

[mesh-llm](https://github.com/michaelneale/mesh-llm)は、ノードアイデンティティにNostr keypairsを使う分散LLM推論システムで、4月7日に[v0.56.0](https://github.com/michaelneale/mesh-llm/releases/tag/v0.56.0)を出荷しました。このリリースは、ownership semanticsを備えた分散config protocol、メモリ使用量を減らすための非対称KV cache quantization（Q8_0 keysとQ4 values）、アイデンティティkeystore向けのOS keychain保存、メッセージキューイングを伴う滑らかなchat streaming、fullscreen layoutとflash attention付きKV cache splittingの修正を追加します。

### Nostr VPNがexit node対応とUmbrelパッケージングを出荷

[Nostr VPN](https://github.com/mmalmi/nostr-vpn)は、シグナリングにNostr relays、暗号化トンネルにWireGuardを使うP2P VPNで、今週は[v0.3.0](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.0)から[v0.3.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.6)まで6リリースを出荷しました。v0.3.xサイクルではWindowsとmacOSでexit node対応が追加され、ピアはネットワーク内の他ノードを経由してインターネットトラフィックをルーティングできるようになりました。inviteとaliasの伝播もNostr上で同期されるようになったため、ユーザーは帯域外の調整なしにネットワークアクセスを共有できます。これらのリリースには、self-hosted deployment向けUmbrelパッケージング、記憶した公開endpointを使うNAT punch-through、自動のstale exit node cleanup、公開されたprotocol specificationも含まれます。プロジェクトはself-healing default routesとunderlay repairによりmacOSのroute処理も安定化させ、Tauri経由のAndroid buildも追加しました。ビルドはmacOS（Apple SiliconとIntel）、Linux（AppImageと.deb）、Windows、Android向けに利用できます。

### NymchatがMarmotを巻き戻し、強化版NIP-17グループチャットを出荷

[Nymchat](https://github.com/Spl0itable/NYM)はMLS対応チャットクライアントで、[v3.56.261](https://github.com/Spl0itable/NYM/releases/tag/3.56.261)から[v3.58.274](https://github.com/Spl0itable/NYM/releases/tag/v3.58.274)まで14リリースを出荷しました。最も大きな変化はプロトコル方針の転換です。[v3.57.261](https://github.com/Spl0itable/NYM/releases/tag/v3.57.261)ではMarmot MLS group chatsが追加されましたが、[v3.58.268](https://github.com/Spl0itable/NYM/releases/tag/v3.58.268)では[Marmot](/ja/topics/marmot/)のmulti-device対応がまだ未完成で、デバイス間のgroup chat state同期に問題が出たため、[NIP-17](/ja/topics/nip-17/)へ戻しました。v3.58.271では、すべてのメッセージに対してローテーションするephemeral keysを使う強化版NIP-17グループチャットが導入され、タイミング攻撃や相関攻撃を防ぐ設計になっています。同週には、設定を細かく制御できるfriend system（[v3.58.262](https://github.com/Spl0itable/NYM/releases/tag/v3.58.262)）、暗号化されたアプリ設定内でのMLS group chat message同期、複数のrelay接続修正も入りました。

### nak v0.19.5がBlossom multi-serverとoutbox publishingを追加

[nak](https://github.com/fiatjaf/nak)はfiatjafによるコマンドラインNostrツールキットで、[v0.19.5](https://github.com/fiatjaf/nak/releases/tag/v0.19.5)を出荷しました。`blossom`コマンドは複数の`--server`フラグを受け取れるようになり、複数の[Blossom](/ja/topics/blossom/)サーバーへ1回でアップロードできます。新しい`key`コマンドは、部分的な鍵を左側ゼロ埋めで展開します。`event`コマンドにはoutbox model経由でイベントを公開する`--outbox`フラグが追加され、`fetch`はイベントが返らなかった場合にerror codeで終了するようになりました。

## 開発中

### White Noiseがthumbhashプレビューとpush registration bridgeを追加

[White Noise](https://github.com/marmot-protocol/whitenoise)は[Marmot](/ja/topics/marmot/)プロトコル上に構築されたプライベートメッセンジャーで、今週5件のPRをマージしました。[PR #549](https://github.com/marmot-protocol/whitenoise/pull/549)は画像プレビューのblurhashをthumbhashへ置き換えます。thumbhashは、元画像のアスペクト比と色分布を保ちながら、より小さいペイロードサイズで（典型的には30バイト未満、blurhashの約50から100バイトに対して）より鮮明なプレースホルダー画像を生成する新しいアルゴリズムです。古いcontent向けにはblurhashがfallbackとして残されています。[PR #548](https://github.com/marmot-protocol/whitenoise/pull/548)はwhitenoise-rsを更新し、[MIP-05](/ja/topics/mip-05/) push registration bridgeを追加して、[先週のpush notification仕様作業](/en/newsletters/2026-04-01-newsletter/#marmot-moves-keypackages-to-addressable-events-and-tightens-push-notifications)をクライアントへ接続します。[PR #493](https://github.com/marmot-protocol/whitenoise/pull/493)はチャットメッセージにcursor-based paginationを追加し、従来の読み込み戦略をスクロール駆動の方式へ置き換えました。

### Route96が動的label設定とzero-egress cleanupを追加

[Route96](https://github.com/v0l/route96)はv0lによる[Blossom](/ja/topics/blossom/)メディアサーバーで、今週3件のPRをマージしました。[PR #80](https://github.com/v0l/route96/pull/80)はadmin API経由の動的label model設定を追加し、オペレーターがサーバー再起動なしにcontent分類モデルを差し替えられるようにします。[PR #82](https://github.com/v0l/route96/pull/82)はadmin UIへlabel設定フィールドを追加し、[PR #79](https://github.com/v0l/route96/pull/79)は一度もダウンロードされていないファイルを自動削除するzero-egress file cleanup policyを追加して、オペレーターのストレージコストを抑えます。

### Snortがセキュリティ強化とDVM payment invoicesを出荷

[Snort](https://github.com/v0l/snort)はwebクライアントで、今週は包括的なセキュリティ監査を伴う2リリースを出荷しました。修正にはSchnorr署名検証、[NIP-46](/ja/topics/nip-46/) relay message forgery保護（侵害されたrelay経由で攻撃者が署名要求を注入するのを防ぐ）、PIN暗号化改善、NIP-26 delegation trustの削除が含まれます。性能面の改善は、WASM内でのバッチSchnorr検証、lazy-loaded routes、事前コンパイル済み翻訳、イベントごとの二重検証の排除から来ています。[PR #618](https://github.com/v0l/snort/pull/618)は[NIP-90](/en/topics/nip-90/)（Data Vending Machine）のkind `7000`支払い要求invoice表示を追加し、DVMが支払い要件を返したときにSnortがLightning invoiceをフィード内へ直接描画できるようにします。

### DamusがLMDB compactionを改善

[Damus](https://github.com/damus-io/damus)はiOSクライアントで、[PR #3719](https://github.com/damus-io/damus/pull/3719)をマージし、スケジュールに基づく自動LMDB compactionを追加しました。これによりローカルデータベースが時間とともに無制限に肥大化するのを防ぎます。[PR #3663](https://github.com/damus-io/damus/pull/3663)はBlurOverlayViewを、壊れて見えるのではなく保護的に見えるよう改善しています。

### Captain's Logがtag indexingとnote syncを追加

[Captain's Log](https://github.com/nodetec/captains-log)（Comet）はNodetecによるNostrネイティブな長文執筆ツールで、今週4件のPRをマージしました。[PR #156](https://github.com/nodetec/captains-log/pull/156)はノート横断のtag indexingとsync対応を追加し、[PR #157](https://github.com/nodetec/captains-log/pull/157)はnote syncとtag処理をリファクタリングし、[PR #159](https://github.com/nodetec/captains-log/pull/159)はゴミ箱に入れたノートの同期を修正して、削除済みノートがデバイス間でも削除されたまま保たれるようにします。

### Relatr v0.2.xがNostrネイティブvalidator marketplaceとともにplugin systemを再設計

[Relatr](https://github.com/ContextVM/relatr)は、social graph distanceと設定可能なvalidatorsからtrust rankingを計算する[Web of Trust](/ja/topics/web-of-trust/) scoring engineで、完全なplugin system再設計を伴うv0.2.x系列を出荷しました。validatorsは現在、マルチステップのhostオーケストレーション能力（Nostrクエリ、social graph lookup、NIP-05解決）を支えるためにforkされた、移植性の高い関数型式言語Eloで書かれています。pluginsはkind `765`のNostr eventsとして公開されるため、配布自体がrelayネットワークにネイティブです。新しい[plugin marketplace](https://relatr.net)により、オペレーターはブラウザからvalidatorsを発見、インストール、重み付けでき、ローカルでのauthoringとpublishingにはCLIの`relo`が使えます。アーキテクチャはsandbox化されており、pluginsはhostが明示的に提供した能力しか呼び出せないため、悪意あるvalidatorが定義されたスコープを抜け出すことはできません。Relatrインスタンスは今やwebsiteから管理でき、どのpluginsがscoring algorithmを構成しているか、各重みがいくつかまで完全に見通せます。

### Shopstrがモバイルナビゲーションとアクセス制御を改善

[Shopstr](https://github.com/shopstr-eng/shopstr)はBitcoinでの売買向けNostrネイティブなマーケットプレイスで、今週はメインアプリとコンパニオンプロジェクトの[Milk Market](https://github.com/shopstr-eng/milk-market)にまたがって158コミットを積みました。修正には、モバイルcommunityレイアウト改善、ナビゲーション時のmenu自動クローズ、dropdownのauto-closeが含まれます。保護されたルートはサインインなしで直接URLからアクセスできなくなり、slug matchingロジックも複数の完全一致を正しく扱うようになりました。

### Polleramaがnotifications、movie search、rating UIを追加

[Pollerama](https://github.com/formstr-hq/nostr-polls)はNostr上に構築されたpolling、survey、social ratingアプリで、thread notifications、movie search機能、rating UIの刷新を追加しました。このリリースではfeed読み込み問題の修正と依存関係バージョン更新も行われています。

### PurserがMarmot暗号化を使うNostrネイティブpayment daemonを構築

[Purser](https://github.com/EthnTuttle/purser)はZaprite代替として設計されたNostrネイティブpayment daemonで、今週はコアアーキテクチャ構築のために9件のPRをマージしました。このプロジェクトは、加盟店と顧客の暗号化メッセージングに、MDK経由の[Marmot](/ja/topics/marmot/) MLSを使い、payment providerとしてStrikeとSquareを採用しています。今週はconfigとcatalog読み込み、message schema validation、MDK communication layer、StrikeおよびSquare provider実装、polling engine、anti-spam rate limiting、pending payment永続化、order processing pipelineが入りました。チームがlocal modeでmock MLSを取り除き実際の暗号化へ切り替えたため、99件すべてのtestsは現在、実際のmdk-core MLS操作を通しています。

### VectorがDM attachmentsをリファクタリングし、profile editingを追加

[Vector](https://github.com/VectorPrivacy/Vector)はTauriで構築されたプライバシー重視のNostrメッセンジャーで、[PR #55](https://github.com/VectorPrivacy/Vector/pull/55)をマージしてfrontendをリファクタリングしました。DM attachmentの復号と保存はvector-coreライブラリへ移され、アプリはprofile editingにも対応しました。upload cancelフラグはTauriSendCallbackまで正しく配線され、未使用だったattachment preview callbacksも整理されています。

## プロトコルと仕様の動き

### NIPアップデート

[NIPsリポジトリ](https://github.com/nostr-protocol/nips)への最近の変更です。

**マージ済み：**

- **[NIP-58](/ja/topics/nip-58/)（Badges）: Profile Badgesはkind 10008へ、Badge Setsはkind 30008へ移行**（[PR #2276](https://github.com/nostr-protocol/nips/pull/2276)）：Profile Badgesをkind `30008`からkind `10008`へ移行し（replaceable event、pubkeyごとに1つ）、Badge Sets向けにkind `30008`を導入します。従来、Profile BadgesはBadge定義と同じkind（`30008`）を使っていたため、`d`タグで識別されるparameterized replaceable eventsになっていました。新しいkind `10008`は単純なreplaceable eventで、pubkeyごとに1つ、`d`タグは不要です。クライアントはparameterized replaceable eventsを走査する代わりに、ユーザーごとに単一のreplaceable eventを問い合わせればよくなります。Amethyst v1.07.3はすでにこの移行を出荷済みです。

- **[NIP-34](/ja/topics/nip-34/)（Git Stuff）: git関連follow listsを追加**（[PR #2130](https://github.com/nostr-protocol/nips/pull/2130)）：NIP-34のrepositoryおよびissue追跡向けfollow list慣例を追加します。ユーザーは、追跡したいrepositories（kind `30617`）への`a`タグ参照を含む、`git-repos`や`git-issues`のような`d`タグ付きのkind `30000` follow setsを公開します。クライアントはこれらのfollow setsを購読して、kind `3`のcontact listsがpubkeys向けに機能するのと同様に、ユーザーのフィードへrepository activityを表示できます。

**オープンPRとディスカッション：**

- **NIP-AC: WebRTC上のP2P Voice and Video Calls**（[PR #2301](https://github.com/nostr-protocol/nips/pull/2301)）：元のNIP-100（0xChatが実装）を3点で拡張します。すなわち、メタデータ漏えいをなくすために[NIP-59](/ja/topics/nip-59/) gift wrapsで包んだ[NIP-44](/ja/topics/nip-44/)暗号化へ移行すること、voiceとvideo callのセットアップ（offer、answer、ICE candidates）向けに明示されたWebRTCワークフローを定義すること、そして各ピアが他の全ピアへ直接WebRTC接続を張るmesh group callモデルを採ることです。この仕様はNIP-100との後方互換性はありません。Amethystはすでにこれに沿った実装を進めており、call state machine test suite（[PR #2143](https://github.com/vitorpamplona/amethyst/pull/2143)）とstale call offer処理（[PR #2164](https://github.com/vitorpamplona/amethyst/pull/2164)）が今週入りました。

- **[NIP-340](/en/topics/nip-340/)（FROST Quorum）**（[PR #2299](https://github.com/nostr-protocol/nips/pull/2299)）：Nostr上での[FROST](/ja/topics/frost/)（Flexible Round-Optimized Schnorr Threshold）threshold signing向け慣例を提案します。FROSTでは署名者グループが共同で1つのNostr identityを制御し、完全な秘密鍵を再構成せずに、t-of-nメンバーのいずれかでイベント署名できます。このNIPは、[FROSTR project](/en/newsletters/2026-04-01-newsletter/#igloo-signer-11)のIgloo signer作業を土台に、署名ラウンドの調整、key sharesの配布、threshold-signed eventsの公開方法を定義します。

- **[NIP-5D](/en/topics/nip-5d/)（Nostr Web Applets）**（[PR #2303](https://github.com/nostr-protocol/nips/pull/2303)）：iframe内で動作するsandboxed web applications（「napplets」）が、ホストアプリケーション（「shell」）と通信するための`postMessage`プロトコルを定義します。shellは、構造化メッセージAPIを通じてnappletへNostr署名、relay access、ユーザー文脈を提供し、iframe sandboxは鍵への直接アクセスを防ぎます。これは[NIP-5A](/en/topics/nip-5a/)の静的webサイトホスティングモデルを、Nostr eventsを読んだり書いたりできる対話的アプリケーションへ拡張するものです。このNIPは、動作するruntime実装を伴って活発に開発中です。

- **[NIP-5C](/en/topics/nip-5c/)（Scrolls）**（[PR #2281](https://github.com/nostr-protocol/nips/pull/2281)）：以前のNIP-A5提案から改名されたものです。Nostr上でWebAssemblyプログラムを公開し、発見するための慣例を定義します。WASM binariesはNostr eventsとして保存され、クライアントはそれらをダウンロードしてsandboxed runtimeで実行できます。[demo app](https://nprogram.netlify.app/)ではscrollsがブラウザ内で実行される様子が示されており、任意のクライアントが取得して実行できるexample programsがNostr eventsとして公開されています。

- **[NIP-85](/ja/topics/nip-85/)（Trusted Assertions）: Clarifications**（[PR #2304](https://github.com/nostr-protocol/nips/pull/2304)）：サービスプロバイダーごとに複数鍵や複数relayが存在する場合の仕様文言を引き締め、複数のpubkeysやrelay endpointsにまたがって運用するプロバイダーからのassertionsをクライアントがどう扱うべきかを明確にします。

- **[NIP-24](/ja/topics/nip-24/)（Extra Metadata Fields）: replaceable events向け`published_at`**（[PR #2300](https://github.com/nostr-protocol/nips/pull/2300)）：[NIP-23](/en/topics/nip-23/)（Long-form Content）由来の`published_at`タグを、すべてのreplaceable eventsとaddressable eventsへ一般化します。このタグは表示専用です。`published_at`が`created_at`と等しければ、その時刻に「created」と表示し、異なる場合（イベントが更新された場合）は代わりに「updated」と表示できます。これにより、kind `0`プロフィールに「joined at」日付を表示したり、他のreplaceable eventsでも更新をまたいで元の公開時刻を保てるようになります。補完的な[NIP-51](/ja/topics/nip-51/)提案（[PR #2302](https://github.com/nostr-protocol/nips/pull/2302)）は、同じタグをlist eventsにも追加します。

- **[NIP-59](/ja/topics/nip-59/)（Gift Wrap）: Ephemeral gift wrap kind**（[PR #2245](https://github.com/nostr-protocol/nips/pull/2245)）：既存のkind `1059` gift wrapに対応するephemeral版としてkind `21059`を追加します。ephemeral events（kinds `20000`から`29999`）は[NIP-01](/ja/topics/nip-01/)の意味論に従い、relayは保存を期待されず、配信後に破棄してかまいません。これによりアプリケーションは、通常の[NIP-17](/ja/topics/nip-17/) DMsと同じ3層暗号化モデルを保ったまま、relay上から配信後に消えるgift-wrapped messagesを送れるようになり、高頻度メッセージングのストレージ要件を下げられます。

### OpenSatsが第16回Nostr grantsを発表

[OpenSats](https://opensats.org)は4月8日に[第16回Nostr grants](https://opensats.org/blog/sixteenth-wave-of-nostr-grants)を発表し、初回助成4件と更新1件を採択しました。[Amethyst Desktop](https://github.com/vitorpamplona/amethyst/tree/main/desktopApp)には、contributorのRobert Nagyが[Quartz](/ja/topics/quartz/)とCommonsモジュール上にスタンドアロンのデスクトップアプリを構築するための資金が提供されます。これにより、Androidクライアントの機能群が、永続的なrelay接続を持つマウス中心のインターフェースへ持ち込まれます。[Nostr Mail](https://github.com/nogringo/nostr-mail)には、kind `1301` eventsを[NIP-59](/ja/topics/nip-59/) gift wrapsで包んで使う、Nostr上の完全なメールシステム構築向け資金が提供されます。FlutterクライアントとGmail/Outlook互換のSMTP bridge serversも含まれます。[Nostrord](https://github.com/Nostrord/nostrord)には、Discord風のグループメッセージング、モデレーション、スレッドを備えたKotlin Multiplatformの[NIP-29](/en/topics/nip-29/) relay-based group client向け資金が提供されます。[Nurunuru](https://github.com/tami1A84/null--nostr)には、LINEの馴染みあるインターフェースを手本にし、オンボーディング向けにpasskeyベースの生体認証ログインを備えた、日本語圏向けNostrクライアントのネイティブiOS版構築資金が提供されます。HAMSTRには助成更新が行われました（初回採択は[第11回](https://opensats.org/blog/eleventh-wave-of-nostr-grants#hamstr)）。

## NIPディープダイブ: NIP-17（Private Direct Messages）

[NIP-17](https://github.com/nostr-protocol/nips/blob/master/17.md)は、Nostrにおける現在のプライベートダイレクトメッセージ標準を定義します。これは、relay上で送信者、受信者、タイムスタンプがすべて見えてしまい、暗号構成も弱かった旧来の[NIP-04](/ja/topics/nip-04/)（Encrypted Direct Messages）方式を置き換えるものです。NIP-17は、暗号化に[NIP-44](/ja/topics/nip-44/)（Encrypted Payloads）を、メタデータ保護に[NIP-59](/ja/topics/nip-59/)（Gift Wrap）を組み合わせ、relayからは誰と誰が会話しているかが見えない3層システムを作ります。

このプロトコルは、3つのevent kindsを入れ子にして使います。最も内側の層は実際のメッセージで、署名されていないkind `14`イベントです。

```json
{
  "id": "a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744108800,
  "kind": 14,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef", "wss://inbox.example.com"],
    ["subject", "Project update"]
  ],
  "content": "The new relay config is deployed. Let me know if you see any issues.",
  "sig": ""
}
```

kind `14`イベントは意図的に署名されていません（`sig`は空です）。仕様はこれを否認可能性を与えるものとして説明しますが、実際の保護は限定的です。rumorを包むkind `13`のsealは、送信者の実鍵で署名されています。受信者はメッセージ内容を明かさなくても、その署名済みsealを第三者に見せることで、送信者が自分と通信した事実を証明できます。ゼロ知識証明を使えば、受信者は自分の秘密鍵を明かさずに、メッセージ内容そのものまで証明できます。署名のないrumorは、署名入り封筒に入った無署名の手紙のようなものです。封筒の署名が送信者と内容を結び付けます。真の否認可能性には、SignalのHMACのような対称認証が必要ですが、それはメッセージ自体が自己認証可能でなければならないNostrの分散relayモデルとは両立しません。NIP-17の本当の強みは、否認可能性ではなく、メタデータのプライバシーと内容の秘匿性です。

この無署名メッセージは次にkind `13`のsealで包まれ、実際の送信者によって署名され、受信者向けに[NIP-44](/ja/topics/nip-44/)で暗号化されます。

```json
{
  "id": "b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1",
  "pubkey": "d7e3a4b9c1f2e8d6a5b4c3d2e1f09876d7e3a4b9c1f2e8d6a5b4c3d2e1f09876",
  "created_at": 1744022400,
  "kind": 13,
  "tags": [],
  "content": "<nip44-encrypted kind 14 payload>",
  "sig": "e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4"
}
```

sealにはtagsがないため、復号できても受信者は分かりません。sealは送信者の実鍵で署名されており、受信者はsealの`pubkey`が内側のkind `14`の`pubkey`と一致することを確認することでメッセージを認証できます。

そのsealはさらにkind `1059`のgift wrapで包まれ、ランダムな使い捨て鍵で署名され、受信者宛てに送られます。

```json
{
  "id": "c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2c3d4e5f67890a1b2",
  "pubkey": "9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba",
  "created_at": 1744065600,
  "kind": 1059,
  "tags": [
    ["p", "f1a2b3c4d5e6f7890123456789abcdef01234567890abcdef1234567890abcdef"]
  ],
  "content": "<nip44-encrypted kind 13 payload>",
  "sig": "fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210fedcba9876543210"
}
```

gift wrapの`pubkey`は、このメッセージ専用に生成されたランダム鍵で、`created_at`は最大2日前までランダム化されています。relayが実際に見る最外層はこれです。未知のpubkeyから受信者宛てに送られたメッセージで、タイムスタンプも実際の送信時刻を反映しません。このランダム化タイムスタンプは、保存済みイベントを後から分析する攻撃への対策になりますが、relayへ能動的に接続している攻撃者はgift wrapが最初に現れた時点を観測できるため、この防御は後からrelayデータを問い合わせる受動的観測者に対してのみ有効です。pubkeyがランダムでタイムスタンプも偽装されているため、relayは実際の送信者を特定できません。受信者がメッセージを読むには、自分の鍵とランダムpubkeyを使ってgift wrapを復号し、中のsealを取り出し、次に自分の鍵とsealに入っている送信者pubkeyでsealを復号し、その内側にあるkind `14`メッセージを見つけます。

NIP-17はforward secrecyを提供しません。すべてのメッセージは静的なNostr keypairを使って暗号化されます（NIP-44で送信者鍵と受信者鍵から導出した鍵を使用）。秘密鍵が侵害されると、その鍵宛てに暗号化された過去と未来のすべてのメッセージが復号可能になります。これは意図的なトレードオフです。暗号化はnsecだけに依存するため、ユーザーがnsecをバックアップしていれば、gift wrapsをまだ保持している任意のrelayからメッセージ履歴全体を復元できます。[Marmot](/ja/topics/marmot/)で使われるMLSのようなプロトコルは、鍵素材をローテーションすることでforward secrecyを提供しますが、その代償としてstate同期が必要になり、鍵ローテーション後の過去メッセージ履歴復元は不可能になります。

NIP-17は暗号化ファイルメッセージ向けのkind `15`も定義しており、受信者がBlossomサーバーへアップロード前にAES-GCMで暗号化された添付ファイルを復号できるよう、`file-type`、`encryption-algorithm`、`decryption-key`、`decryption-nonce`タグを追加します。Kind `10050`は、送信者がgift wrapsをどこへ届けるべきか分かるよう、ユーザーが希望するDM relay listを公開するのに使われます。メッセージ内の`pubkey`と`p` tagsの集合が1つのチャットルームを定義し、参加者の追加や削除はクリーンな履歴を持つ新しいルームを作ります。

実装は主要クライアントの多くをカバーしています。[nospeak](https://github.com/psic4t/nospeak)はすべての1対1メッセージングにNIP-17を使っています。[Flotilla](https://gitea.coracle.social/coracle/flotilla)はproof-of-work DMsにNIP-17を使っています。[Amethyst](https://github.com/vitorpamplona/amethyst)、[Primal](https://github.com/PrimalHQ/primal-android-app)、[Nostur](https://github.com/nostur-com/nostur-ios-public)、[Damus](https://github.com/damus-io/damus)、[noStrudel](https://github.com/hzrd149/nostrudel)、[Coracle](https://github.com/coracle-social/coracle)は、いずれも主要DMプロトコルとしてNIP-17を実装しています。gift wrapへ`expiration`タグを設定することで、仕様はdisappearing messagesにも対応します。

## NIPディープダイブ: NIP-46（Nostr Remote Signing）

[NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md)は、ユーザーの秘密鍵をクライアントアプリケーションから分離するためのプロトコルを定義します。webアプリへnsecを貼り付ける代わりに、ユーザーは秘密鍵を保持し、Nostr relays経由の署名要求へ応答するremote signer（「bunker」とも呼ばれます）を動かします。クライアントが秘密鍵を見ることはありません。これにより攻撃面は小さくなります。侵害されたクライアントでも署名要求は送れますが、鍵そのものを引き抜くことはできません。

このプロトコルは、要求と応答の両方にkind `24133`を使い、[NIP-44](/ja/topics/nip-44/)（Encrypted Payloads）で暗号化します。クライアントはセッション用の使い捨て`client-keypair`を生成し、互いのpubkeysをタグ付けしたNIP-44暗号化メッセージを通じてremote signerと通信します。以下は、クライアントからremote signerへ送る署名要求の例です。

```json
{
  "id": "aa11bb22cc33dd44ee55ff6677889900aabbccdd11223344556677889900aabb",
  "pubkey": "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86",
  "created_at": 1744108800,
  "kind": 24133,
  "tags": [
    ["p", "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52"]
  ],
  "content": "<nip44-encrypted JSON-RPC request>",
  "sig": "1122334455667788990011223344556677889900aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff0011223344556677"
}
```

暗号化された`content`には、JSON-RPC風の構造が入っています。

```json
{
  "id": "random-request-id-1",
  "method": "sign_event",
  "params": ["{\"kind\":1,\"content\":\"Hello from remote signing\",\"tags\":[],\"created_at\":1744108800}"]
}
```

remote signerはこの要求を復号し、ユーザーへ承認を提示し（または設定済み権限に基づいて自動承認し）、ユーザーの秘密鍵でイベントへ署名し、その署名済みイベントを応答として返します。

```json
{
  "id": "bb22cc33dd44ee55ff6677889900aabb11223344556677889900aabbccddeeff",
  "pubkey": "fa984bd7dbb282f07e16e7ae87b26a2a7b9b90b7246a44771f0cf5ae58018f52",
  "created_at": 1744108801,
  "kind": 24133,
  "tags": [
    ["p", "eff37350d839ce3707332348af4549a96051bd695d3223af4aabce4993531d86"]
  ],
  "content": "<nip44-encrypted JSON-RPC response>",
  "sig": "aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899"
}
```

接続はどちら側からでも開始できます。remote signerは、自分のpubkeyとrelay情報を含む`bunker://` URLを提供します。クライアントは、自分のclient pubkey、relays、接続検証用secretを含む`nostrconnect://` URLを提供します。`secret`パラメータは接続なりすましを防ぎます。帯域外でURLを受け取った当事者だけがhandshakeを完了できます。

定義されているメソッドは8つです。セッション確立用の`connect`、イベント署名用の`sign_event`、ユーザーのpubkey取得用の`get_public_key`、keepalive用の`ping`、旧来暗号化用の`nip04_encrypt`と`nip04_decrypt`、現行暗号化用の`nip44_encrypt`と`nip44_decrypt`、そしてrelay管理用の`switch_relays`です。relay migrationはremote signerが処理するため、セッションを壊さずに接続先relayを時間とともに移せます。

クライアントは接続時にpermission systemを通じて具体的な能力を要求します。`nip44_encrypt,sign_event:1,sign_event:14`のようなpermission文字列は、NIP-44暗号化アクセスと、kind `1`およびkind `14`イベントに限定した署名アクセスを要求します。remote signerはこれらの権限を受け入れることも、拒否することも、変更することもできます。つまり、ノートの閲覧と投稿だけを行うwebクライアントには`sign_event:1`だけが与えられ、DMクライアントには`sign_event:14`と`nip44_encrypt`も与えられる、といった運用が可能です。

[Amber](https://github.com/greenart7c3/Amber)はAndroidでNIP-46を実装しており、今週の[v6.0.0-pre1](#amber-v600-pre1が接続ごとのnip-46署名鍵を追加)ではクライアント間の分離のため、接続ごとの署名鍵が追加されました。[nsec.app](https://github.com/nicktee/nsecapp)（旧Nostr Connect）はwebベースのbunkerを提供します。[nostr-tools](https://github.com/nbd-wtf/nostr-tools)にはJavaScriptクライアント向けの`BunkerSigner`が含まれており、[先週のPR #530](/en/newsletters/2026-04-01-newsletter/#nostr-tools-adds-bunker-relay-control-and-fixes-nip-47-multi-relay-parsing)では手動relay管理向けに`skipSwitchRelays`が追加されました。このプロトコルはauth challengeもサポートします。remote signerが追加認証（パスワード、生体認証、ハードウェアトークン）を必要とする場合、クライアントがブラウザで開いて完了させる`auth_url`を返します。

---

今週は以上です。何か作っているものがある、あるいは共有したいニュースがありますか。NostrでDMを送るか、[nostrcompass.org](https://nostrcompass.org)を見てください。
