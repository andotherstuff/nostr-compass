---
title: 'Nostr Compass #15'
date: 2026-03-25
translationOf: /en/newsletters/2026-03-25-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Nostr Compassへようこそ。Nostrの週刊ガイドです。

**今週の内容:** [Primal Android](https://github.com/PrimalHQ/primal-android-app)が3.0系ウォレットリリースに続き、[Follow Packs、zap拡張、`primalconnect://`ディープリンク](#primalがfollow-packszap拡張ディープリンクを追加)を追加しました。[BigBrotr](https://github.com/BigBrotr/bigbrotr)は1,085個のrelayにまたがる4,100万イベントを走査し、16,599個の有効な秘密鍵を見つけた[nsec漏えい分析](#bigbrotrがrelayネットワーク全体の公開秘密鍵を可視化)を公開しました。同じ週に[npub.world](https://npub.world)もプロフィールページへ警告を統合しています。Martti MalmiはNostr relayでシグナリングしWireGuardトンネルを張るTailscale代替の[nostr-vpn](#nostr-vpnがtailscale代替としてローンチ)を立ち上げ、7日間で11リリースを出しました。[Vector](https://github.com/VectorPrivacy/Vector)チームは[Nostr上で動くP2P DOOM](#オープンソースdoomがnostr上でpeer-to-peer動作)をオープンソース化し、[FIPS](https://github.com/jmcorgan/fips)は[v0.2.0](#fips-v020がtorトランスポート再現可能ビルドsidecar例を出荷)を出荷、[Nostrability Schemata](https://github.com/nostrability/schemata)は1週間で[6言語対応](#nostrability-schemataが多言語化)へ拡大しました。

## ニュース

### PrimalがFollow Packs、zap拡張、ディープリンクを追加

[先週の3.0.7記事](/ja/newsletters/2026-03-18-newsletter/)に続き、[Primal Android](https://github.com/PrimalHQ/primal-android-app)は今週、オンボーディング、コンポーザーUX、ウォレット文脈に関するリリース後の作業を進めました。再設計されたオンボーディングはFollow Packs（[PR #949](https://github.com/PrimalHQ/primal-android-app/pull/949)）を導入し、ノートコンポーザーにはネイティブGIFボタンが追加され、zap拡張サービス（[PR #979](https://github.com/PrimalHQ/primal-android-app/pull/979)）がウォレットトランザクションにzap文脈を注釈し、`primalconnect://`ディープリンクプロトコル（[PR #969](https://github.com/PrimalHQ/primal-android-app/pull/969)）がアプリ間ナビゲーションを可能にします。

[Primal iOS](https://github.com/PrimalHQ/primal-ios-app)も同じ作業を並行してTestFlight経由で出荷しており、ウォレット切り替え（[PR #191](https://github.com/PrimalHQ/primal-ios-app/pull/191)）、ポール実装、オンボーディングのリファクタリングが同じ期間に入っています。

### BigBrotrがrelayネットワーク全体の公開秘密鍵を可視化

Nostr relay分析プラットフォームの[BigBrotr](https://github.com/BigBrotr/bigbrotr)が、relayネットワーク上で露出した秘密鍵に関する[詳細な分析](https://bigbrotr.com/blog/exposed-nsec-analysis/)を公開しました。この調査は1,085個のrelayから4,100万イベントを走査し、イベントcontentに埋め込まれた有効なnsec文字列を探索した結果、16,599個の有効な秘密鍵を見つけました。この数字は一見すると深刻ですが、一致の92%を占める「Mr.nsec」というbotを除外すると見え方が変わります。botトラフィックを除いた後に残ったのは、合計21,000人超のフォロワーを持つ実在アカウント38件だけで、そのどれにも自分の鍵が公開されている自覚は見られませんでした。

チームはnsec-leak-checkerを[NIP-90](/ja/topics/nip-90/)（Data Vending Machine）サービスとして構築し、秘密鍵そのものをチェッカーに明かさずに、走査済みデータセットに自分の鍵が含まれているかどうかを確認できるようにしました。[npub.world](https://npub.world)も同週にこの漏えいデータを統合し、公開鍵が検出されたプロフィールページに警告バナーを表示しています。この組み合わせにより、ネットワークはDVMやエージェント向けのプログラマブルなインターフェースと、一般ユーザー向けの人間可読な警告の両方を得ました。この基盤データセットは、置換可能イベントとアドレス可能イベントのマテリアライズドビュー、ならびに同期アイドルタイムアウト修正を追加した[BigBrotr v6.4.0](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.4.0)にも流れています。

### nostr-vpnがTailscale代替としてローンチ

Irisの作者であるMartti Malmi（mmalmi）が、Nostr relayをシグナリングに、boringtun経由のWireGuardを暗号化トンネルに使うP2P VPNの[nostr-vpn](https://github.com/mmalmi/nostr-vpn)を構築して出荷しました。動機は直接的で、「Tailscaleがサードパーティアカウントを要求するのにうんざりしたので、Nostr VPNを作った」というものです。このツールはNostrキーペアをアイデンティティとして用い、中央調整サーバーなしでデバイス間にメッシュネットワークを作ります。

プロジェクトは[v0.2.2](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.2)から[v0.2.13](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.13)まで、7日間で11リリースを出しました。このスプリントではWindows対応、ローカルネットワーク発見のためのLANペアリング、モバイル向けAndroid sidecarが追加されました。アーキテクチャは単純です。2台のデバイスがNostr relay上で接続メタデータを交換し、その後に直接WireGuardトンネルを確立します。発見とNAT越えのシグナリングはNostrが担い、実際の通信はWireGuardが担います。アイデンティティはNostrキーペアです。

MalmiはSignal風の安全なメッセージングチャネルライブラリである[nostr-double-ratchet](https://github.com/mmalmi/nostr-double-ratchet)の開発も継続しており、同じ週に[v0.0.86](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.86)から[v0.0.93](https://github.com/mmalmi/nostr-double-ratchet/releases/tag/v0.0.93)まで6リリースを出しました。

### オープンソースDOOMがNostr上でpeer-to-peer動作

[Vector](https://github.com/VectorPrivacy/Vector)チームは、Nostrをピア発見に、[Marmot](/ja/topics/marmot/)をエンドツーエンド暗号化に、n0のQUICネットワーキングライブラリ[Iroh](https://github.com/n0-computer/iroh)をgossipトランスポートに使うP2PマルチプレイヤーDOOM実装をオープンソース化しました。ゲームは4.2 MBのWebXDCファイルとして出荷され、チャットメッセージ内で送信でき、試合をホストしたり調整したりするサーバーを必要としません。

技術的アプローチは、1993年の元のlockstep netcodeをリアルタイムのハイブリッド同期モデルに置き換えます。プレイヤーはNostr relayクエリを通じて互いを発見し、Marmotで暗号化されたチャネルでセッションを交渉し、その後低遅延のゲーム通信のためにIrohのQUIC gossip層へ移行します。このスタックでは、発見をNostr、暗号化をMarmot、トランスポートをIrohが担当します。

Vectorは今週セキュリティ強化も出荷しました。リリースには、メモリ強化されたキーボールトとanti-debug保護、機密鍵素材のzeroize、完全なDMおよびグループメッセージフィルタリングを伴うユーザーブロック、Mini Apps向けのWebXDCリアルタイムチャネル修正が含まれます。

### FIPS v0.2.0がTorトランスポート、再現可能ビルド、sidecar例を出荷

Nostr隣接のメッシュネットワーキングプロジェクトである[FIPS](https://github.com/jmcorgan/fips)（Free Internetworking Peering System）が[v0.2.0](https://github.com/jmcorgan/fips/releases/tag/v0.2.0-rel)を出荷しました。このリリースは匿名化されたメッシュリンク用のTorトランスポート、再現可能ビルド、Nostr relay経由で接続するsidecar例、OpenWrtパッケージワークフローにおけるNostrリリース公開を追加します。また、rekey後にdrain-windowフレームが原因で発生していたjitterスパイクも修正しました。ワイヤーフォーマットはv0.1.0から変更されているため、既存のv0.1.0ノードはアップグレードなしではv0.2.0と相互運用できません。

### Nostrability Schemataが多言語化

Nostrイベントkindを検証するJSON Schema定義を維持する[Nostrability Schemata](https://github.com/nostrability/schemata)プロジェクトが、1週間でJavaScript専用から6言語対応へ拡大しました。Rust、Go、Dart、Swift、Python向けの新しいパッケージが出荷され、それぞれがデータパッケージとvalidatorを提供します。[v0.2.6](https://github.com/nostrability/schemata/releases/tag/v0.2.6)では17個の新しいイベントkind schemaも追加されました。

[Nostrability interop tracker](https://nostrability.github.io/nostrability/)も並行して刷新されました。新しいWhat's Newタブは更新をAtomフィードとNostrイベントの両方で公開し、アプリカテゴリフィルタリングにより特定のクライアント種別に絞り込めるようになり、trackerはGitHubリポジトリのメタデータからプログラミング言語を自動検出するようになりました。Nostrability自体も専用npubを持つようになり、文書化するプロトコルを通じてプロジェクト自身が発見可能になっています。複数言語をまたぐライブラリ作者にとって、多言語schemaパッケージは各プロジェクトが独自のschemaコピーを維持する代わりに、同じイベントkind定義をネイティブimportとして利用できることを意味します。

## リリース

### Amethyst v1.06.0 と v1.06.1

vitorpamplonaがメンテナンスするAndroidクライアント[Amethyst](https://github.com/vitorpamplona/amethyst)が、3月23日に[v1.06.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.0)と[v1.06.1](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.1)を出荷しました。目玉機能は[NIP-85](/ja/topics/nip-85/)（Trusted Assertions）データを使った重み付き投票によるポールサポートで、ポールカードとzap pollカードも再設計されています。新しいレンダリングは、標準ポールとzap重み付きポールの双方に、より整理された視覚レイアウトを与えます。v1.06.1では、ポール描画パスで導入された安定性退行に対処する同時変更クラッシュ修正が入っています。

### Amber v5.0.0 と v5.0.1

[Amber](https://github.com/greenart7c3/Amber)は[NIP-55](/ja/topics/nip-55/)（Android署名アプリケーション）署名者アプリで、3月18日に最近の4.1.xプレリリース作業を安定版[v5.0.0](https://github.com/greenart7c3/Amber/releases/tag/v5.0.0)へ昇格させました。この安定版には、先週取り上げた[NIP-42](/ja/topics/nip-42/) relay認証、組み込みTor、コンテンツタイプ固有の権限、暗号化PINストレージの変更が含まれています。その後の[v5.0.1](https://github.com/greenart7c3/Amber/releases/tag/v5.0.1)では、オフラインビルドフレーバーからinternet権限が削除され、そのビルドはAndroid権限レイヤーでネットワークリクエストを行えなくなりました。

### Mostro v0.17.0 と Mostro Mobile v1.2.2

Nostr上に構築されたP2P Bitcoin取引所[Mostro](https://github.com/MostroP2P/mostro)が、3月18日に[v0.17.0](https://github.com/MostroP2P/mostro/releases/tag/v0.17.0)を出荷しました。サーバー側リリースはv0.16.xサイクルからの紛争処理とレーティング作業を継続し、買い手と売り手のより完全な取引レピュテーションデータをNostrイベントとして追加します。Flutterクライアントの[Mostro Mobile](https://github.com/MostroP2P/mobile)も3月23日に[v1.2.2](https://github.com/MostroP2P/mobile/releases/tag/v1.2.2)を続けて出荷し、モバイルインターフェースを最新のプロトコル変更と同期させています。

### Shosho v0.14.0

Nostrライブストリーミングアプリ[Shosho](https://github.com/r0d8lsh0p/shosho-releases)が、3月19日にShosho Shopの開始を含む[v0.14.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v0.14.0)を出荷しました。リリースではプロフィールにShopタブ、Browse内のShop、ライブとクリップ上のIn-Live Shopボタンが追加されています。リリースノートによれば既存の「Nostr products」は自動的に表示され、購入者は売り手のPlebeian Marketページへ遷移して購入します。Shoshoのリリースノートはリスティングイベントkindを明示していないため、Shosho Shopが[Shopstr](https://github.com/shopstr-eng/shopstr)がREADMEで明示的にサポートしている[NIP-99](/ja/topics/nip-99/)分類リスティングを読んでいるかは、まだ確認できません。

### Applesauce v5.2.0

hzrd149によるNostrアプリ構築向けヘルパーパッケージ集[Applesauce](https://github.com/hzrd149/applesauce)が、3月22日に[v5.2.0](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core@5.2.0)を出荷しました。このリリースは6つのパッケージにまたがります。SQLiteパッケージはイベントタグに対するUNIQUE制約衝突を修正し、重複挿入を防ぎます。signersパッケージは`AndroidNativeSigner`を追加し、[NIP-55](/ja/topics/nip-55/)ネイティブAndroid signerインターフェースをラップすることで、web-viewベースアプリが独自のbridgeコードなしでハードウェア支援署名を使えるようにします。relayパッケージはrelayとpoolの状態オブジェクトに`challenge`フィールドを追加し、[NIP-42](/ja/topics/nip-42/)認証状態を追跡して、relayが認証を要求していることをアプリが検知してプログラム的に応答できるようにします。coreパッケージはイベント参照の重複排除用に`isEventPointerSame`と`isAddressPointerSame`を得て、commonパッケージはユーザーのBlossomメディアサーバー解決用に`user.blossomServers$`を追加します。ApplesauceはnoStrudel、Satellite、その他複数のWebクライアントを支えているため、これらの修正はWebクライアント層全体に伝播します。

### Wispが1週間で16リリース

Android Nostrクライアント[Wisp](https://github.com/barrydeen/wisp)が、今週[v0.9.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.9.3-beta)から[v0.13.1-beta](https://github.com/barrydeen/wisp/releases/tag/v0.13.1-beta)まで16リリースを出荷しました。追加された機能には、マルチアカウント対応、通知を減らすzen notificationsモード、ドラフトと予約投稿、安全性コンテンツフィルター、新しいflameアイコンが含まれます。

### Manent v1.2.0

プライベートな暗号化ノートおよびファイルストレージアプリ[Manent](https://github.com/dtonon/manent)が、3月20日に[v1.2.0](https://github.com/dtonon/manent/releases/tag/v1.2.0)を出荷しました。このリリースはアプリ内からのカメラ撮影、ストレージコスト削減のためのアップロード前画像リサイズ、保存済み画像確認時のピンチズームを追加します。Manentはユーザーのキーペアを用いてノートとファイルをNostr relay上に暗号化して保存し、電話やデスクトップアプリをrelayデータから完全な状態を再構築できるthin clientにします。

### diVine 1.0.7

短尺動画クライアント[diVine](https://github.com/divinevideo/divine-mobile)が、3月21日に動画再生watchdogを含む[1.0.7](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.7)を出荷しました。このwatchdogは停止した動画を自動で再開します。[v1.0.6](/en/newsletters/2026-03-11-newsletter/)でE2Eテスト基盤と直接MP4読み込みが入った後、このリリースはエラーを出さず中断する動画という残る障害パスを対象にしています。

### Alby Extension v3.14.2

[Alby Extension](https://github.com/getAlby/lightning-browser-extension)は[NIP-07](/ja/topics/nip-07/)（ブラウザ拡張署名者）ブラウザ拡張で、3月18日にLightningアドレスQRコード表示とSchnorr署名サポートを含む[v3.14.2](https://github.com/getAlby/lightning-browser-extension/releases/tag/v3.14.2)を出荷しました。Schnorr対応により、ブラウザ拡張はNostrがネイティブに使うsecp256k1署名方式と整合します。

### NoorNote v0.6.5 から v0.6.11

ノートテイキングアプリ[NoorNote](https://github.com/77elements/noornote)が、[v0.6.5](https://github.com/77elements/noornote/releases/tag/v0.6.5)から[v0.6.11](https://github.com/77elements/noornote/releases/tag/v0.6.11)まで7リリースを出荷しました。目玉はFollow Packsで、ユーザーがまとめて閲覧・購読できるアカウントのキュレート済み束です。Twitter Listsに似ていますが、オンボーディング向けに設計されています。ユーザーはカスタムタイトル、説明、カバー画像付きでFollow Packsを作成、編集、共有できます。このシリーズでは基盤NostrライブラリもNDK v2からv3へ更新され、relay接続処理とサブスクリプション管理が改善されました。picture notesと再設計されたrelay接続体験もこの流れを締めくくっています。

### nak v0.19.1 と v0.19.2

fiatjafのコマンドラインNostrツールキット[nak](https://github.com/fiatjaf/nak)が、3月17日と20日に[v0.19.1](https://github.com/fiatjaf/nak/releases/tag/v0.19.1)と[v0.19.2](https://github.com/fiatjaf/nak/releases/tag/v0.19.2)を出荷しました。このツールはrelayとの対話、[NIP-19](/ja/topics/nip-19/)（Bech32エンコードエンティティ）識別子のエンコードとデコード、イベント署名、relayデータの照会を行います。2つのポイントリリースは、先週の[v0.19.0](/ja/newsletters/2026-03-18-newsletter/)で入ったグループフォーラムUI追加に続くものです。

### Calendar by Form* v0.2.1

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar)は[NIP-52](/ja/topics/nip-52/)（カレンダーイベント）上に構築された分散カレンダーアプリで、3月20日に[v0.2.1](https://github.com/formstr-hq/nostr-calendar/releases/tag/v0.2.1)を出荷しました。このリリースはイベントリマインダーに影響していた通知テンプレート問題を修正します。CalendarはイベントをNostr kind 31922（日付ベース）とkind 31923（時刻ベース）イベントとして保存するため、これらのkindをサポートするNostrクライアントなら任意にカレンダーデータを表示できます。アプリはFormstrチームが開発しており、同チームはFormstr（分散フォーム）とPollerama（ポール）も維持しています。

### NYM v3.50 から v3.53

[NYM](https://github.com/Spl0itable/NYM)はBitchatとbridgeされた軽量エフェメラルチャットクライアントで、v3.50からv3.53まで28リリースを出荷しました。最も目立つ機能は、チャンネル内の`@nymbot`メンションに応答し、relay状態や管理機能を提供する組み込みチャットbotのNymbotです。「hardcore mode」は送信する各メッセージごとに新しいキーペアを生成し、会話スレッドをアイデンティティレベルでリンク不能にします。トレードオフは明快で、永続アイデンティティは失われる一方、メッセージごとの匿名性を得ます。relay proxy層にも作業が入り、接続性向上のためのsharded relay proxy workers、geohash channelサポート、不正確なシステムクロックを持つノード向けのclock skew耐性が追加されました。

## プロジェクトアップデート

### DittoがBlueskyブリッジとWikipedia統合を追加

[Ditto](https://github.com/soapbox-pub/ditto)はSoapboxチームのカスタマイズ可能なNostrソーシャルクライアントで、今週3つの機能トラックにわたり300超のコミットを記録しました。1つ目はBlueskyブリッジで、19コミットを使ってBluesky投稿を完全なフィード風スレッドとしてインライン表示し、公式Discover（whats-hot）フィードをバックエンドに持つBluesky discoveryページへのサイドバーナビゲーションを追加し、コメント、共有、リアクション、リンクコピーのアクションボタンを接続しています。ユーザーがDitto内からBluesky投稿に返信すると、compose modalにはこのやり取りがクロスプロトコルであることを示す免責calloutが表示されます。[NIP-73](/ja/topics/nip-73/)（外部コンテンツID）のkind 17リアクションがこのクロスプロトコルモデルを支えています。NostrユーザーがBluesky投稿に反応すると、そのリアクションは外部コンテンツ識別子を参照する標準Nostrイベントとして保存されます。これはBluesky投稿からYouTube動画、Webページまで、あらゆる外部コンテンツにリアクションをブリッジできる同じNIP-73パターンです。

2つ目のトラックはWikipedia統合で、9コミットが入りました。Dittoは汎用リンクプレビューの代わりに詳細ページでリッチなWikipedia記事contentをレンダリングし、記事サムネイル付き検索autocompleteを追加し、Wikipedia APIから特集contentを引く`/wikipedia`ページも提供します。WikipediaとArchive.orgの結果は一般検索autocompleteドロップダウンにも表示されます。3つ目のトラックはCapacitor経由のiOSプラットフォーム対応で、remote build scriptとplatform設定が、アプリ内の全ページでbackdrop-blurヘッダーを新しいarc-based navigationデザインに置き換えるUI刷新（55コミット）と並行して入りました。314コミットにより、DittoはNostr専用クライアントから、BlueskyとWikipediaをNostrフィードと並ぶ第一級のcontent sourceとして扱うマルチプロトコル集約クライアントへ近づいています。

### PikaがNIP-34 forge CIパイプラインを構築

[Pika](https://github.com/sledtools/pika)はMarmotベースの暗号化メッセージングアプリで、今週33件のPRをマージしました。焦点はプレマージCI付きのセルフホスト型[NIP-34](/ja/topics/nip-34/) forgeです。このforgeはNIP-34イベントとしてパッチを受け取り、マージ前にCIチェックを実行し、構造化された状態をNostrイベント経由で返すgitホスティング層です。[PR #701](https://github.com/sledtools/pika/pull/701)はlaneベースのプレマージおよびnightly CIを追加し、Rust、TypeScript、Apple buildsといった各コードパスを独立したlaneで実行し、個別のpass/fail状態を持たせます。[PR #715](https://github.com/sledtools/pika/pull/715)は分離のためにmanaged CI agentsをIncus OpenClaw containersへ切り替え、[PR #733](https://github.com/sledtools/pika/pull/733)はコマンドラインからhosted forgeと対話するための`ph forge` CLIを追加します。関連PRでは、マージ時のrepo書き込み権限（[PR #736](https://github.com/sledtools/pika/pull/736)）、live status badgesを伴う構造化CIメタデータ（[PR #722](https://github.com/sledtools/pika/pull/722)）、Apple nightly buildsの分割（[PR #738](https://github.com/sledtools/pika/pull/738)）、forge認証とbranch lookup修正（[PR #734](https://github.com/sledtools/pika/pull/734)）が処理されています。これはNIP-34 gitイベント上に構築された最初期の実用CI/CDシステムの1つであり、Nostrベースのソースコードホスティングを基本的なパッチ交換から、開発者がGitHubやGitLabに期待するマージとテストのワークフローへ押し進めています。

### Nostriaがcommunities、code snippets、voice event処理を追加

[Nostria](https://github.com/nostria-app/nostria)はsondrebがメンテナンスするクロスプラットフォームNostrクライアントで、#14で触れたWeb of Trustフィルタリングの先へ今週アプリサーフェスを広げました。主な追加は完全な[NIP-72](/ja/topics/nip-72/)（モデレートコミュニティ）実装で、コミュニティ作成、モデレーターおよびrelay設定、画像プレビュー付き投稿承認追跡、PostsタブとModeratorsタブを持つ専用コミュニティページを提供します。

同じ作業期間では、構文ハイライト付きエディターによるcode snippetの表示と編集、音声会話向けvoice event replyサポート、ダイレクトメッセージ用chat relay設定、Web Share APIによるchannel共有、メディアプレイヤー用toolbar docking system、最新Brainstorm Web of Trustサービスへのアプリ内サインアップ、NWCとBOLT-11インボイスを使うDMでの送金と受け取り、NostrネイティブGIF処理、既存のLightning splitをポッドキャストfeedから取り込めるより強いRSS import pathも追加されました。

### nostr-vpnの高速反復

[初回ローンチ記事](#nostr-vpnがtailscale代替としてローンチ)の先でも、[nostr-vpn](https://github.com/mmalmi/nostr-vpn)のcommit logは実運用時に直面した具体的な問題を示しています。[v0.2.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.3)から[v0.2.5](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.5)では初期installer scriptとクロスプラットフォームCLIが追加されました。[v0.2.6](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.6)と[v0.2.7](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.7)でWindows対応が入り、config書き込みのUAC path quotingとdaemon所有config更新が必要になりました。[v0.2.8](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.8)から[v0.2.10](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.10)ではWindows GUI service actions、CLI subprocess handling、machine-scoped service configurationが修正されました。[v0.2.12](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.12)ではLAN discoveryがtimed LAN pairingに置き換えられています。これは同じローカルネットワーク上の2デバイスがrelayシグナリングなしでペアリングする、ユーザー主導のフローです。このパターンは初期フィールドテストの典型で、各リリースが特定のデプロイ障害を狙い、ユーザーベースが小さいため日次で反復でき、開発者自身がリリース間でツールを使っていることがわかります。

### Cometの自動ビルド

[Comet](https://github.com/nodetec/comet)（旧Captain's Log）は、NodetecによるNostrネイティブ長文執筆ツールで、今週40超の自動alpha buildを生成しました。CometはNIP-23長文記事の執筆と公開のためのデスクトップアプリで、ローカルdraft保存、markdown編集、ユーザーのrelay setへのワンクリック公開を備えます。自動ビルドパイプラインはmain branchへの各commitごとにtagged releaseを生成するため、生のリリース数は機能開発速度の指標としては誤解を招きます。40ビルドが示しているのは、アプリが日次のアクティブ開発下にあり、各commitが数分以内にテスト・パッケージ化され・ダウンロード可能になっているということです。

## NIPアップデート

3月17日から24日の期間における[NIPsリポジトリ](https://github.com/nostr-protocol/nips)の最近の変更：

3月18日から3月24日の間にNIPのマージはありませんでした。

**期間中に更新されたオープンPRとディスカッション：**

- **NIP-AA: Autonomous Agents on Nostr**（[PR #2259](https://github.com/nostr-protocol/nips/pull/2259)）：Nostrネットワーク上で動作する自律エージェント向けの慣例を提案しています。このPRは、エージェントが自身を識別し、サービスを発見し、Nostrイベントを通じて他のエージェントや人間と協調する方法を定義します。

- **[NIP-50](/ja/topics/nip-50/)（検索）: ソート拡張**（[PR #2283](https://github.com/nostr-protocol/nips/pull/2283)）：NIP-50検索クエリにtop、hot、zaps、newを含むsortパラメータを追加します。これによりクライアントは、クライアント側でソートする代わりに、全文検索をサポートするrelayへランク済み結果を要求できます。

- **NIP-A5: WASM Programs**（[PR #2281](https://github.com/nostr-protocol/nips/pull/2281)）：WebAssemblyプログラムをNostr上で公開・発見するための慣例を提案しています。WASMバイナリはNostrイベントとして配布でき、relayはポータブル実行コードの発見層になります。

- **NIP-CF: Combine Forces interoperable napps**（[PR #2277](https://github.com/nostr-protocol/nips/pull/2277)）：異なるクライアントやサービス間で機能を合成できる相互運用可能なNostrアプリケーション「napps」の慣例を定義します。

- **Snapshots NIP**（[PR #2279](https://github.com/nostr-protocol/nips/pull/2279)）：relay同期とバックアップのためのrelay状態スナップショット機構を提案しています。

- **Checkpoints NIP**（[PR #2278](https://github.com/nostr-protocol/nips/pull/2278)）：既知の良好なrelay状態を示すcheckpointイベントを提案し、snapshots提案を補完します。

- **[NIP-58](/ja/topics/nip-58/)（バッジ）: Badge Setsリファクタ**（[PR #2276](https://github.com/nostr-protocol/nips/pull/2276)）：バッジコレクションの構成と参照方法を再編成します。

- **[NIP-11](/ja/topics/nip-11/)（Relay情報ドキュメント）: 拡張**（[PR #2280](https://github.com/nostr-protocol/nips/pull/2280)）：より豊かな機械可読relayメタデータのために追加フィールドを導入します。

## Nostrの5つの3月

[先月のニュースレター](/ja/newsletters/2026-03-04-newsletter/#nostr-2月の5年間)では、NIP-01の書き換えからDamus App Storeの波、メッシュネットワーキング、エージェント提案まで、Nostrの2月がどう進んだかを振り返りました。今回の回顧は2021年から2026年まで、それぞれの3月に何が起きたかを追います。

### 2021年3月: 2つのコミット

誕生から4か月後、Nostrの3月の成果は3月4日に入った2つのコミットだけでした。fiatjafは[nostwitterインスタンスへのリンクを追加し](https://github.com/nostr-protocol/nostr/commit/dcd8cc3)、初期訪問者を実際に動くデプロイ先へ導きました。また[基本filter定義にkindを追加しました](https://github.com/nostr-protocol/nostr/commit/54dfb46)。この2つ目のコミットは示唆的です。2021年3月時点では、Nostrイベントをkindでfilterすることすらまだできませんでした。プロトコルはその程度に原始的だったのです。ネットワークには2つか3つのrelayしかなく、調整チャネルはTelegramグループだけでした。NIPsリポジトリもまだ存在せず、プロトコル提案はメインnostrリポジトリ内のファイルとして管理されていました。その月のコミッターはfiatjafただ1人です。5年後にVPN、マルチプレイヤーゲーム、メッシュネットワーキングを支えるプロトコルになるものの2021年3月の全成果は、1つのgit diffに収まります。

### 2022年3月: Damus以前の構築期

メインのプロトコルリポジトリは2022年3月に0コミットでした。開発は完全にツール系リポジトリへ移っていました。fiatjafのVue.js Webクライアントで当時の主要Nostrインターフェースだった[Branle](https://github.com/fiatjaf/branle)には、Dockerデプロイ支援や[NIP-05](/ja/topics/nip-05/)（DNSベース検証）の表示名修正を含む5コミットが入り、検証バッジから`_@`プレフィックスが除去されました。Robert C. Martinの[more-speech](https://github.com/unclebob/more-speech)はClojureデスクトップクライアントで、threading、キーボードナビゲーション、編集ウィンドウを加える13以上のコミットを記録しました。その月にNostr上で最も有名なソフトウェア作者として積極的に開発していたのは暗号開発者ではなく、『Clean Code』を何百万部も売った人物でした。彼がClojureでNostrクライアントを書いていたという事実は、初期コミュニティの性格をよく示しています。そこには自分たちのために作る、意見の強いプログラマたちがいました。

relayネットワークはおよそ15relayへ拡大し、アクティブユーザーは数百人規模になっていました。Damusはまだ存在せず、作成されるのは2022年4月まで待つ必要がありました。Nostreamもまだ現れていません。その月の作業はインフラ整備であり、すでに日々使われていた小さなコミュニティのために既存ツールをより信頼できるものにすることに集中していました。

### 2023年3月: 爆発後のインフラ期

Damus App Storeの波と30万公開鍵超えから1か月後、2023年3月はその成長を吸収する時期でした。[NIPsリポジトリ](https://github.com/nostr-protocol/nips)は28件のPRをマージし、これはプロトコル史上2番目に多い月間件数です。[NIP-51](/ja/topics/nip-51/)（リスト）がマージされ、クライアントは構造化されたフォロー・ミュート・ブックマークコレクションを得ました。[NIP-39](/ja/topics/nip-39/)（プロフィール内の外部アイデンティティ）も入り、NIP-78（アプリ固有データ）はアプリがプライベート状態を必要とする際の汎用ストレージkindを提供し、[NIP-57](/ja/topics/nip-57/)（Lightning Zaps）の書き直し（[PR #392](https://github.com/nostr-protocol/nips/pull/392)）はzapフローを統合して用語を明確にしました。この月で最も議論されたPRは、50超のコメントを集めた別案のmention handling提案（[PR #381](https://github.com/nostr-protocol/nips/pull/381)）でした。

最も重要な新規プロジェクトは、relay接続、イベント署名、キャッシュ、サブスクリプション管理のためのTypeScriptライブラリ[NDK](https://github.com/nostr-dev-kit/ndk)でした。pablof7zは2023年3月16日に[初回コミット](https://github.com/nostr-dev-kit/ndk/commit/09e5e03)を行い、11日後の3月27日には「ほぼ別の初回コミット」としてゼロから書き直し、3月31日にはLNURLとzapサポートを動かしていました。NDKは15日でゼロからzap対応に到達したのです。NDK作成から5日後の3月21日には、Albyチームが[NWC](https://github.com/getAlby/nostr-wallet-connect)を作成しました。これは[NIP-47](/ja/topics/nip-47/)のリファレンス実装で、LightningウォレットをNostrアプリケーションへ接続します。その後3年間のWebベースNostr開発を支える2つのプロジェクトは、同じ30日間の中で生まれました。OpenSatsのNostr fundはまだ立ち上がっておらず、最初の波はNDK作成から4か月後の[2023年7月](https://opensats.org/blog/nostr-grants-july-2023)まで待つ必要がありました。

その月のその他の注目作としては、NostrGit、NostrChat、LNbitsによるnostr-signing-deviceプロジェクト、nostrmoがありました。インテリジェントrelay選択に焦点を当てたRustデスクトップクライアント[Gossip](https://github.com/mikedilger/gossip)は3つのリリースを出しました。プロトコルは構築モードにあり、2023年3月に作られたツール群は3年後の今も使われています。

### 2024年3月: プロトコル成熟期

2024年3月は、プロトコルを長期利用に耐えるものへ硬化させる時期でした。NIPsリポジトリは12件のPRをマージしました。最も重要だったのは、130超のコメントと44日のレビューを経て3月5日にマージされた[NIP-34](/ja/topics/nip-34/)（Git Stuff）、[PR #997](https://github.com/nostr-protocol/nips/pull/997)です。この議論スレッドは、分散型GitHubをどう作るかをコミュニティが議論していた時代の記録です。jb55は`git send-email`との類似性を指摘し、Giszmoはcross-fork discoveryのためにroot commit hashを使う案を出し、「GitHubがやっていないことを私たちはできる」と述べ、mikedilgerはSSH鍵の代わりに[NIP-98](/ja/topics/nip-98/)（HTTP認証）のイベント署名認証を提案し、fiatjafはバージョン管理の一般性は不要だと率直に切り捨てました。「各バージョン管理システム向けではなく、git向けでいい。他は誰も使っていない」と。PRを開いた数時間後には、fiatjafはnak、go-nostr、gitstrを既にNostr上のpatch受け取り対応へ切り替えていました。OpenSats granteeだったngitのDanConwayDevも、この議論の最も活発な参加者の1人でした。プロフィールメタデータ向けのbot fieldも同時にマージされ、クライアントが自動アカウントと人間のアカウントを機械可読に区別できるようになりました。

[Amethyst](https://github.com/vitorpamplona/amethyst)はgitイベント対応、wiki記事、医療データ描画、content編集を1つのリリースでまとめたv0.85.0を出荷しました。[Mostro](https://github.com/MostroP2P/mostro)はv0.10.0へ到達しました。[Nosflare](https://github.com/Spl0itable/nosflare)はCloudflare Workers上で動くserverless Nostr relayとして、relayロジックがedgeで動けることを示しました。OpenSatsはAmethystクライアントへの継続的貢献に対して、Bruno Garciaへ[Long-Term Support grant](https://opensats.org/blog/bruno-garcia-receives-lts-grant)を出しています。

### 2025年3月: インフラ拡張期

2025年3月には10本のNIPがマージされました。主役は[NIP-66](/ja/topics/nip-66/)（Relay Discovery and Liveness Monitoring）、[PR #230](https://github.com/nostr-protocol/nips/pull/230)で、25か月に及ぶ道のりを経て3月3日にマージされました。dskvrは2023年2月にrelay monitoringを初めて提案し、クライアント側でできると言われ、何千ものrelayへ同時接続することが個々のクライアントには非現実的である理由を説明し、完全な草案を7回作り直し、8地域（米国北東部、ブラジル、米国西部、米国東部、オーストラリア、インド、韓国、南アフリカ）にmonitoring nodesを構築し、relay toolingが追いつくのを待ちました。マージ時点ですでに実装はnostr.watch、relaypag.es、monitorlizard、Snort、noStrudel、Jumbleに存在していました。NIP-66データは後に[Newsletter #12](/ja/newsletters/2026-03-04-newsletter/#アウトボックスモデルの検証)で取り上げたNostrability outboxベンチマークの燃料になります。NIP-C0（Code Snippets）も[PR #1852](https://github.com/nostr-protocol/nips/pull/1852)でマージされ、kind 1337イベントによるソースコード共有を追加しました。

この月にはNostr向け最初のMCPサーバー群も登場しました。[nostr-mcp-server](https://github.com/AustinKelsay/nostr-mcp-server)は3月23日に、[nwc-mcp-server](https://github.com/getAlby/nwc-mcp-server)は3月14日に出現しており、これはAnthropicが2024年11月にModel Context Protocolを発表してから4か月後のことです。これら初期ブリッジは、後の2025年末から2026年初頭にかけて現れる完全な[ContextVM](/ja/topics/contextvm/) SDKやagent commerce作業に先行していました。

[Gossip](https://github.com/mikedilger/gossip)はv0.14.0を出荷し、relay認識型フィード管理を持つhodlbodのWebクライアント[Coracle](https://github.com/coracle-social/coracle)も3つのリリースを出しました。OpenSatsは[第10波のNostr grants](https://opensats.org/blog/10th-wave-of-nostr-grants)を発表し、2023年半ばから続く資金供給パイプラインを維持しました。

### 2026年3月: 収束

*2026年3月の活動は、Nostr Compassの[#12](/ja/newsletters/2026-03-04-newsletter/)から[#15](#)（本号）までの各号をもとにしています。*

2026年3月は、ばらばらだった流れが実用システムへ収束した月でした。[Marmot Development Kit](/ja/newsletters/2026-03-04-newsletter/#marmot-development-kitが初の公開リリースを出荷)が暗号化メディア、多言語バインディング、spec・Rust・TypeScript間の協調更新を必要としたChaCha20-Poly1305移行を伴う初の公開リリースを出荷しました。[ShopstrとMilk Market](/en/newsletters/2026-03-11-newsletter/)はagent-driven purchasing向けのMCP commerce surfaceを追加しました。[NIP-42](/ja/topics/nip-42/) relay認証は[Amber](/en/newsletters/2026-03-11-newsletter/)、strfry、OAuth Bunkerに同時に入っており、signer、relay、bunkerソフトウェア間のループを閉じています。[Notedeck](/ja/newsletters/2026-03-18-newsletter/#notedeckがリリース発見をnostr上に移行)は[NIP-94](/ja/topics/nip-94/)（ファイルメタデータ）リリースイベントを用いたNostrネイティブのソフトウェア更新を出荷しました。

今週は、[BigBrotr](#bigbrotrがrelayネットワーク全体の公開秘密鍵を可視化)が漏えい秘密鍵を探すためにrelayネットワーク全体を走査し、分析とDVM checkerの両方を公開しました。[Nostr VPN](#nostr-vpnがtailscale代替としてローンチ)は、Nostrの鍵モデルがソーシャルメディアだけでなくネットワークインフラにも機能することを示しました。[DOOM](#オープンソースdoomがnostr上でpeer-to-peer動作)は、Nostr discovery、Marmot暗号化、QUIC transportを組み合わせてリアルタイムマルチプレイヤーゲームを動かせることを示しました。[Amber](#amber-v500-と-v501)はv5.0.0へ到達し、[Wisp](#wispが1週間で16リリース)は7日で16リリースを出しました。主要プロジェクト群から1週間で25件以上のtagged releaseが出ています。

月の最初の24日だけで7つのNIPがマージされました。プロトコルには[NIP-54](/ja/topics/nip-54/)（Wiki）のDjotマークアップ、[NIP-19](/ja/topics/nip-19/)（Bech32エンコードエンティティ）の入力制限、[NIP-91](/ja/topics/nip-91/)（フィルター用AND演算子）のboolean query logic、[NIP-85](/ja/topics/nip-85/)（Trusted Assertions）のWeb of Trust assertionが加わりました。オープン提案は、自律エージェント（NIP-AA）からWASMプログラム（NIP-A5）、[NIP-50](/ja/topics/nip-50/)向け検索ソート拡張まで広がっています。

### 今後の展望

Nostrの5つの3月を辿ると、明確な弧が見えます。2021年には、まだkindでイベントをfilterできないプロトコルに対して、1人が2つのコミットを入れていました。2023年には、Damus後の爆発を吸収するためにNDKとNWCが5日違いで誕生しました。2024年には、141コメントのPRスレッドがソーシャルプロトコル上でgit協業をどう機能させるかを論じました。2025年には、25か月かけて7回書き直されたrelay monitoring specがついにマージされました。2026年には、Tailscaleがアカウントを要求することに苛立った誰かがNostrキーペアを使うVPNを作り、別の誰かがNostr relayでピアを発見しMarmotでゲームプレイを暗号化するマルチプレイヤーDOOMを出荷しました。BigBrotrが1,085relayにまたがる4,100万イベントを走査したことは、ネットワークの成長を測る具体的な尺度を与えます。2026年3月のプロトコル表面積は2021年3月の自分には見分けがつかないほど広がっていますが、土台のモデル、すなわちsecp256k1鍵で署名されrelay経由で配布されるイベントという構造自体は変わっていません。

---

今週は以上です。何か作っているものや共有したいニュースがあれば、<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">[NIP-17](/ja/topics/nip-17/)（プライベートダイレクトメッセージ）DMでご連絡ください</a>。Nostr上でもお待ちしています。
