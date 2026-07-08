---
title: 'Nostr Compass #25'
date: 2026-06-03
publishDate: 2026-06-03
draft: false
type: newsletters
translationOf: /en/newsletters/2026-06-03-newsletter.md
translationDate: 2026-07-08
---

Amber 6.2.0は仕様に先立ってNIP-44 v3暗号化を出荷しました。Mostroは8つのPRにわたってCashuで決済されるエスクローの基礎を実現し、既存のCashu Development KitをLightningと並ぶ2番目の決済バックエンドとしてラップしました。NIP-F4ポッドキャストは27か月の議論を経てマージされました。fiatjafはbunker対Marmotのアーキテクチャ論争を再開させる論争的なNIP-17キー分離提案を公開しました。Amethystは52の未リリースPRにわたってNIP-32ハッシュタグラベリング、専用ポッドキャスト画面、オンチェーンzapを実現しました。

## トップストーリー

### Amber 6.2.0: NIP-44 v3暗号化を出荷

6月1日にリリースされた[Amber v6.2.0](https://github.com/greenart7c3/Amber/releases/tag/v6.2.0)は、専用の承認画面、intentプレビュー、bunkerプレビュー、履歴ロギング、および無効なリクエストの自動拒否を備えた[NIP-44 v3暗号化サポート](https://github.com/greenart7c3/Amber/pull/448)を追加します。このリリースは、他のAndroidアプリが既存のv2パスと並んでv3暗号化を要求できるように[NIP-44 v3 ContentProviderオーソリティ](https://github.com/greenart7c3/Amber/commit/8b93340)も登録します。NIP-44自体は、[NIP-17](/ja/topics/nip-17/)プライベートDM、NIP-46 bunkerトラフィック、およびその他のNostrプリミティブによって使用されるバージョン付き暗号化ペイロード仕様です。Amberのv3はv2と並ぶオプトインで、別の署名者メソッドによって信号送信されるので、受信側クライアントはアルゴリズムを明示的に交渉できます。対応するNIPs PRはまだ着地していないので、Amberはプロトコルの合意に先立ってv3を展開しており、ワイヤーフォーマットとContentProviderオーソリティが下流のクライアント統合のために登録されています。

NIP-46セッションは接続時にpingリクエストを自動承認するようになり、ペアリング後の最初のラウンドトリップでのプロンプトが削除されました。`sign_message`署名者メソッドは非推奨で未使用になった後、完全に削除されました。

Amberが優勢なAndroid署名者なので、v3を求める下流のクライアントはNIPs PRが着地するまでAmberのワイヤーフォーマットをターゲットにしなければなりません。それはプロトコルが追いつくまで、最終的なv3仕様に対してAmberに暗黙の発言権を与えます。トレードオフは現実的です: 本番のv3は、他のクライアントが今マッチしなければならない一時的な単一実装のリファレンスポイントを犠牲にして、最終的なNIPのための実装フィードバックをAmberに集めさせます。

### Mostro: CDK経由のCashuエスクロー統合

grunchは今週MostroP2P全体で8つのPRを実現し、CashuのP2PKマルチシグプリミティブ (NUT-10とNUT-11) をNostr協調型のP2P Bitcoin取引所でLightningと並ぶ2番目の決済バックエンドとして統合しました。暗号プリミティブはCashuのものであり、作業は統合の足場と新しいエスクローバックエンドtraitです。5月30日にリリースされた[Mostro core v0.12.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.12.0)は、[2-of-3マルチシグエスクロー用のプロトコルタイプ](https://github.com/MostroP2P/mostro-core/pull/150)、プルーフごとのP_M署名、およびレスポンス検証を通じてエスクローイベントを許可します。アーキテクチャは[PR #756](https://github.com/MostroP2P/mostro/pull/756)で文書化されており、[PR #757](https://github.com/MostroP2P/mostro/pull/757)で明確化された注文ごとの取引キーを使用します。

実装は1日で6つのフォローアップPRにわたって展開されました。[F2 (PR #758)](https://github.com/MostroP2P/mostro/pull/758)は設定、エスクローモード、条件付きブートを追加しました。次のスライスである[F3 (PR #760)](https://github.com/MostroP2P/mostro/pull/760)は、Lightning実装とCashuスタブを持つ`EscrowBackend` traitを定義し、Mostroが注文状態マシンを変更せずに決済バックエンドを切り替えられるようにしました。[F4 (PR #759)](https://github.com/MostroP2P/mostro/pull/759)は、mintおよびウォレット操作のために[CDK](https://github.com/cashubtc/cdk) (Cashu Development Kit) をラップしました。[F5 (PR #761)](https://github.com/MostroP2P/mostro/pull/761)のデータベース作業は、compare-and-swapエスクローロックとアクティブロッククエリを追加しました。[F6 (PR #762)](https://github.com/MostroP2P/mostro/pull/762)は、エンドツーエンドのエスクローテストのために専用CIジョブでコンテナ化されたmintを構築しました。Mostroフローは既にNIP-59ギフトラップDMをリレー上での注文コーディネーションに使用しているので、Cashuエスクローはワイヤープロトコルに触れることなくLightningと並ぶ2番目の決済オプションとしてスロットインします。

## リリース

### ngit v2.5.0: GRASPフォールバックと遅延gitフェッチ

[ngit v2.5.0](https://github.com/DanConwayDev/ngit-cli/releases/tag/v2.5.0)は、リポジトリに少なくとも1つのGRASPサーバーが登録されているときに、新しい提案に対して`git push pr/<branch>`と`ngit send`のデフォルト動作をPR kindを生成するように変更します。以前は、これは60 KBを超える大きすぎるコミット、またはサブモジュールを含むコミットに対してのみトリガーされていました。PRがリポジトリのGRASPサーバーにプッシュできない場合、ngitは宣言されたサーバーを通じてGRASP-06ルーティングにフォールバックするようになりました。`ngit send --git-server`フラグまたは`git push -o git-server=<url>`により、コントリビューターはカスタムgit URLまたはGRASPサーバーを明示的にターゲットにできます。

`ngit init`の再公開は、既存のアナウンスから未知のタグを保持するようになったので、将来のngitバージョンやサードパーティツールによって追加されたタグは再公開を生き延びます。黄色の警告が引き継がれたタグをリストし、`--clean`は要求に応じてそれらを削除します。`ngit pr apply`、`ngit pr checkout`、`ngit pr list`はgitサーバーを遅延して参照し、単一のフェッチヘルパーを共有するので、コミットが既にローカルにあるときにcheckoutが無条件にフェッチしなくなりました。`ngit pr checkout`はまた、リポジトリの宣言されたgitサーバーがPRチップを持たないときに、PRイベントから提出者が提供したクローンURLをフォールバックとして試み、`ngit pr apply`の既存の動作と一致させます。ngitはNostr上のgitコラボレーションのための参照[NIP-34](/ja/topics/nip-34/)実装であり、v2.5.0はGRASPを新しいコントリビューターの第一級のパスにします。

### Jumble v26.5.7: EXIF除去と検証されたzapカウント

[Jumble v26.5.7](https://github.com/CodyTseng/jumble/releases/tag/v26.5.7)は、ユーザーのプライバシーとデータの整合性に直接影響する2つの変更を追加します。EXIFの位置と カメラ識別子は、クライアントを離れる前に画像アップロードから除去されるようになり、Jumbleから投稿されるすべての画像に影響を及ぼしていた長年のメタデータリークサーフェスが閉じられました。zapカウントは、暗号的に検証された領収書からのみ計算されるようになり、攻撃者がノートのzap合計を誇張することを許していた不正な形式のzapイベントによる膨張したカウントを修正しました。このリリースはまた、[NIP-17](/ja/topics/nip-17/) DMの送信者アイデンティティ検証を追加し、送信者がシール内で`pubkey`を偽造できる詐称サーフェスを閉じます。

### nostr-calendar v1.6.0: RSVPと重複参加者処理

[nostr-calendar v1.6.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.6.0)はFormstrのRSVPフロー ([PR #169](https://github.com/formstr-hq/nostr-calendar/pull/169)) を実現し、イベント招待の重複参加者を防ぎます ([PR #168](https://github.com/formstr-hq/nostr-calendar/pull/168))。publish関数の`waitForAll`オプションはfalseにデフォルトするようになったので、UIは遅いリレー上でブロックしなくなりました ([PR #170](https://github.com/formstr-hq/nostr-calendar/pull/170))。[PR #157](https://github.com/formstr-hq/nostr-calendar/pull/157)は、アポイントメントスケジューリングと予約のためのFormstrの2つのNIP提案ドラフトを出荷しました。

### Sprout 0.3.6: Sprout × mesh-llmとチャネルセクション

[Sprout v0.3.6](https://github.com/block/sprout/releases/tag/v0.3.6)は、今週のv0.3.1からv0.3.6までの6リリースランのハイライトです。プロセス内Sprout × mesh-llm統合は[PR #798](https://github.com/block/sprout/pull/798)に着地し、Sproutがリレー承認を通じてmesh-llmノードをサーブおよび消費できるようにします。ユーザー定義のチャネルセクションはNostr経由でデバイス間で同期し ([PR #792](https://github.com/block/sprout/pull/792))、チャネルセクションはリレー同期とともにモバイルに来ました ([PR #800](https://github.com/block/sprout/pull/800))。可変フォローとミュートコントロールを備えたスレッド認識通知は[PR #761](https://github.com/block/sprout/pull/761)に到着します。

ダウンロードカード付きの任意ファイルタイプ添付は[PR #810](https://github.com/block/sprout/pull/810)に到着し、Sproutを画像のみの添付を超えて拡張しました。モバイルはPulseソーシャルフィードタブ ([PR #772](https://github.com/block/sprout/pull/772)) と、フィード、作成、フィルタサーフェス全体のPulseポリッシュ ([PR #796](https://github.com/block/sprout/pull/796)) を獲得しました。

### NostrBotKit v0.5.0: RustボットフレームワークにおけるMarmotグループチャット

5月24日にCodebergで公開された[NostrBotKit v0.5.0](https://codeberg.org/Tuxor/NostrBotKit/src/branch/main/CHANGELOG.md)は、セルフホストされたRustボットフレームワークに[Marmot](/ja/topics/marmot/) (MLS-over-Nostr、[NIP-104](https://github.com/nostr-protocol/nips/pull/2014)) サポートを追加します。`marmot: true`が設定されると、ボットは MLSキーパッケージ (kind 443、30443、10051) を公開し、グループ招待を自動的に受け入れ、参加したグループでメッセージをリッスンします。2つの新しいコマンドタイプ`dm_marmot`と`dm_marmot_npub`により、ボットはcronジョブまたはwebhook経由で名前付きMarmotグループまたは1:1 Marmotチャットにメッセージを送信できます。他のボットとのフィードバックループを防ぐために、NostrBotKitボットは`/command`または`@botname/command`経由で明示的に彼らに宛てられたメッセージにのみ応答します。MIP-04を使用した暗号化された添付はBlossomまたはNIP-96経由で自動的に復号され再アップロードされ、MLS状態データベースはボットの秘密鍵から導出されたキーで暗号化されます。NostrBotKitはNIP-104ボットサポートを出荷する最初のRustフレームワークであり、Marmot暗号化ボット展開を既存のTypeScriptパスとは異なる運用プロフィールに開きます。

### noscrypt v0.1.14: 署名付き暗号ライブラリリリース

[noscrypt v0.1.14](https://github.com/vnuge/noscrypt/releases/tag/v0.1.14)は、secp256k1、NIP-04、NIP-44プリミティブのためにいくつかのNostrクライアントによって使用されるC暗号ライブラリのセキュリティリリースです。このリリースはメンテナーの公開鍵に対して検証可能な[PGP署名付きダウンロード](https://www.vaughnnugent.com/resources/software/modules/noscrypt)とともに出荷されます。noscryptをバンドルする下流のクライアントは、統合する前に署名を検証すべきです。

### Chama v1.3.0: Fedimintを使用した新しいNostrネイティブP2Pエスクロー

6月1日にリリースされた[Chama v1.3.0](https://github.com/jesuspirate/chama/releases/tag/v1.3.0)は、決済のためにFedimint ecashと2-of-3 Shamir秘密分散を使用する新しいNostrネイティブP2Pエスクロークライアントのための4リリースランのハイライトです。プロジェクトは[getchama.app](https://getchama.app)で出荷され、サーバーなしで動作します。v1.3.0は「くっつくヒーリング」(セッション再起動を生き延びる成功した再ブロードキャストと取引ヒーリング) と、米国寄りのChamaが米国決済レールを最初に表示する決済レールマッチングを導入します。マルチユニットストアフロントの基礎工事は[v1.2.11](https://github.com/jesuspirate/chama/releases/tag/v1.2.11) (マルチユニットスキーマ) と[v1.2.12](https://github.com/jesuspirate/chama/releases/tag/v1.2.12) (ストアフロント在庫会計士 + ネイティブFedimintブリッジ回復強化) にわたって着地しました。ChamaはNostrマーケットプレイスカテゴリでMostroとShopstrに加わり、そのサーバーレスアーキテクチャとFedimintベースのエスクロー決済によって区別されます。

## 未リリースの変更

### Amethyst: NIP-32ハッシュタグラベリング、ポッドキャスト画面、音楽トラック

Amethystはリリースタグを切ることなく今週52 PRと411コミットをマージしました。最大の機能追加は[PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111)であり、`L`名前空間と`l`ラベルタグを持つkind 1985イベントを使用した[NIP-32](/ja/topics/nip-32/)ハッシュタグラベリングとラベルベースのハッシュタグフィードを実装します。これは、脆弱なテキストマッチ`#tag`メカニズムを、ユーザーがコンテンツクリエイターをフォローするのと同じ方法で特定のラベラーnpubをフォローできるラベラーベースの発見モデルに置き換えます。[PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105)は、[NIP-F4](/ja/topics/nip-f4/)ポッドキャスト仕様マージから数日以内に、エピソードリストとインラインプレーヤーを備えた専用ポッドキャスト画面を追加します。[PR #3071](https://github.com/vitorpamplona/amethyst/pull/3071)はフォローリストフィルタリング付きのソフトウェアアプリフィードを追加し、[PR #3067](https://github.com/vitorpamplona/amethyst/pull/3067)は[NIP-51](/ja/topics/nip-51/)セット経由で音楽トラックとプレイリストサポートを追加します。

匿名投稿アップロード用のエフェメラル署名者は[PR #3123](https://github.com/vitorpamplona/amethyst/pull/3123)に着地し、ユーザーはアイデンティティキーをアップロードサービスに公開せずに匿名で投稿できるようになります。Arti v2.3.0に対する統合テストを備えたTor自己修復ウォッチドッグは[PR #3053](https://github.com/vitorpamplona/amethyst/pull/3053)に到着し、一時的なネットワーク停止時のAmethystのTorルーティングを強化します。オンチェーンzapとGemini からの復帰ユーザー用のNIP-05フィルタは[PR #3052](https://github.com/vitorpamplona/amethyst/pull/3052)に着地し、zapサーフェスをLightningを超えてオンチェーンBitcoin支払いに広げます。

### Shopstr: OpenGraphプレビューURL検証

[PR #504](https://github.com/shopstr-eng/shopstr/pull/504)は、マーケットプレイスリスティングでOpenGraphプレビューURLをレンダリングする前に検証し、悪意のあるセラーが細工されたOGメタデータを介してスクリプト付きコンテンツを埋め込むことができる潜在的なXSSサーフェスを閉じます。ShopstrがホストするショップはExternalリンクのOGプレビューを表示し、未検証のURLは攻撃者がショップUIに任意のコンテンツを注入することを許します。

## NIP更新とプロトコル仕様作業

### NIP-F4 (ポッドキャスト) が2年後にマージ

[PR #1093](https://github.com/nostr-protocol/nips/pull/1093)は、fiatjafが元のドラフトを公開してから2年3か月後の5月28日にマージされました。NIP-F4は、オーディオファイルメタデータ用の`imeta`タグ (URL、mimeタイプ、言語ISOコード、フォールバックURL、NIP-96サービスフラグ、ビットレート、時間)、`title`タグ、オプションの`image`と`description`タグ、およびトピックラベル用の`t`タグを持つkind 54イベントとしてポッドキャストエピソードを定義します。仕様はRSSを意図的に真実のソースとして保ちます: エピソードはRSSポッドキャストGUIDを参照する`i`タグを持つことができるので、Nostrクライアントはオーディオホスティングを重複させることなく既存のポッドキャストフィードにリンクできます。PRスレッドでの長い議論 (ポッドキャスト名前空間の共著者Dave Jones、Alex Gleason、Mike Terenzioと) は、NostrがRSSの上のソーシャルレイヤーを提供し、RSSが配信レイヤーを保つ共存モデルに落ち着きました。Amethystの[PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105)ポッドキャスト画面は仕様マージから数日以内に着地し、JumbleのGIFピッカーの作業には初期のポッドキャスト添付の足場も含まれます。

### NIP-17キー分離 (PR #2361)

fiatjafは6月1日に[PR #2361](https://github.com/nostr-protocol/nips/pull/2361)を公開し、NIP-17がアイデンティティキーを暗号化キーから分離することを提案しました。受信者は新しいkind 10044イベントで暗号化キーを広告し、送信者は (存在するときには) その広告されたキーをギフトラップの内側のシールに使用し、広告が不在のときにのみ受信者のアイデンティティキーにフォールバックします。PRはまた、送信者の暗号化pubkeyを運ぶ`n`タグをシールに追加するので、受信者はリタイアされたキーごとに試行復号することなく正しい会話キーを導出できます。表明された動機はbunker UXです: 現在の設計では、bunkerユーザーは暗号化キーが署名者が保持するアイデンティティキーであるため、受信したすべてのDMを復号するために署名者を通じてラウンドトリップさせなければなりません。分離により、クライアントは暗号化キーをローカルに保持しつつ、アイデンティティキーを署名のためにbunkerに保持できます。

この提案は今週最も論争的なレビューを引き付けました。Cody Tseng (Jumble) は、これをクロスクライアントDM相互運用性への最も簡単なパスとしてサポートしています。Vitor Pamplona (Amethyst) は2つの理由で反対します: これはbunkerの外に新しい長期の復号シークレットを追加し、そしてそれを出荷しないクライアントは、静かに出荷するクライアントからのメッセージを復号できなくなり、断絶がシールレイヤーで起こるので劣化パスがありません。Pamplonaは、この問題は既に[Marmot](/ja/topics/marmot/)のキーパッケージとエポック回転によって正しく解決されており、キー分離をベースNIP-17仕様に後付けすることは、Marmotが回避するのに2年かかった種類の相互運用性の失敗を作り出すと主張します。fiatjafの反論は3部構成です: 分離は受信者ごとにオプションであり、nタグ修正が試行復号の懸念に対処し、代替案はTelegramがメッセージングのユースケースを飲み込む間にbunker UXを壊れたままにしておくことです。スレッドはマージ決定なしでオープンのままであり、四半期で最も注目されているNIPの議論です。

### NIP-Silent Payments決済フロー (PR #2362)

[silentius-satoshiは6月1日にPR #2362を公開](https://github.com/nostr-protocol/nips/pull/2362)し、より広い[Nostr Silent Payments NIPドラフト (PR #2355)](https://github.com/nostr-protocol/nips/pull/2355)への同伴として位置付けました。決済フローNIPは、silent payment受領書通知用のkind 8352 (領収書リンクが公に観測可能にならないように[NIP-59](/ja/topics/nip-59/)ギフトラップ経由で配信) と、同じSilent Paymentsウォレット用にデバイス間で同期する暗号化UTXOキャッシュ用のkind 10353を定義します。ペアは一緒に、支払者がオープンなリレー層でオンチェーンリンクを公開することなく、Nostrネイティブプリミティブを使用してSilent PaymentsアドレスへのExpressで支払いを信号送信できるようにします。

### NIP-PIP Perfect IP Packets (PR #2364)

[RandyMcMillanは6月1日にPR #2364を公開](https://github.com/nostr-protocol/nips/pull/2364)し、ドラフトとしました。それは3つの新しいアドレス可能なkindを持つパケットツリートランスポートを導入します: 39078はマニフェストを運び、39079は個別のスライスを運び、39080は修復リクエストを運びます。仕様は、大きなファイルがアドレス可能なスライスに分解されるワイヤーフォーマットを定義し、マニフェストはスライスツリーを記述し、修復リクエストは受信者に不足しているスライスを要求させます。初期ドラフト状態が適用され、提案はまだメンテナーレビューを引き付けていません。

### NIP-29オーディオ/ビデオライブスペース (PR #2238)

[PR #2238](https://github.com/nostr-protocol/nips/pull/2238)は5月28日にマージされ、[NIP-29](/ja/topics/nip-29/)リレーベースのグループをオーディオとビデオのライブスペースサポートで拡張しました。グループはアクティブなライブスペースセッションを参照できるようになったので、[NIP-53](/ja/topics/nip-53/)スタイルのライブアクティビティイベントはNIP-29グループコンテキストにアンカーできます。

### NIP-71ビデオ複数オーディオトラック (PR #2255)

[PR #2255](https://github.com/nostr-protocol/nips/pull/2255)は5月28日にマージされ、NIP-71ビデオイベントにオーディオトラック`imeta`タグを追加しました。新しいフォーマットはURL、ハッシュ、mimeタイプ、言語タグ (ISO-639-1と オリジナルバージョンフラグ)、フォールバックURL、NIP-96サービス信号、ビットレート、時間を運びます。これはオーディオのみのストリーミング (ビデオポッドキャスト)、安定したオーディオでの解像度切り替え、複数の言語トラック、およびサーバーがオーディオをビデオファイルに直接埋め込まないときのストレージ削減を可能にします。クライアントは単一トラックの動作を仮定する前にオーディオトラックの可用性をチェックすべきです。

### NIP-59エフェメラルギフトラップ (PR #2245)

[PR #2245](https://github.com/nostr-protocol/nips/pull/2245)は5月28日にマージされ、既存のkind 1059ギフトラップのエフェメラルカウンターパートとしてkind 21059を追加しました。セマンティクスは標準のNIP-59ラップと一致しますが、NIP-01ごとのエフェメラルイベントルール (リレーはブロードキャスト後にそれらをドロップし、永続化しない) に従います。これは、アプリが要件に基づいて永続性を選択できるようにします: タイピングインジケーターと存在pingはエフェメラルから利益を得ますが、DM履歴には永続性が必要です。

### NIP-78アプリケーション固有のkind (PR #2292)

[PR #2292](https://github.com/nostr-protocol/nips/pull/2292)は5月28日にマージされ、NIP-78アプリケーション固有データを通常のアドレス可能kindとして再分類し、以前の別の範囲を削除しました。これはリプレイス可能性のセマンティクスを単純化し、NIP-78を他のアプリケーション状態NIPで使用されるアドレス可能イベントモデルに合わせます。

### NIP-85明確化 (PR #2304)

[PR #2304](https://github.com/nostr-protocol/nips/pull/2304)は5月28日にマージされ、[NIP-85](/ja/topics/nip-85/) Trusted Assertionsにおけるサービスプロバイダーごとの複数のキーとリレーに関する言語の小さな改善を行い、リレーアサーションサービスの運用者キー回転パスを明確にしました。

### NIP-01リレー接続管理ワンライナー (PR #2307)

[PR #2307](https://github.com/nostr-protocol/nips/pull/2307)は5月28日にマージされ、クライアントがリレー接続の寿命をどう処理すべきかについての単一の文章をNIP-01に追加しました。この修正は、クライアントがフェッチ後にWebSocket接続を開いたままにするかどうかで違いがあり、アイドル接続をドロップするリレーで静かなメッセージ損失につながっていた長引くギャップに対処します。

### NIP-C7 kind 9チャット制約 (PR #2310)

[PR #2310](https://github.com/nostr-protocol/nips/pull/2310)は5月28日にマージされ、NIP-C7チャットビューをkind 9メッセージのみに制限しました。これは、NIP-C7スタイルのチャットサーフェスを実装するクライアントにおいて、エフェメラルチャットをkind 1タイムラインポストから分離します。

### NIP-55簡素化 (PR #2363)

greenart7c3による、6月1日に公開された[PR #2363](https://github.com/nostr-protocol/nips/pull/2363)は、Android署名者アプリケーション仕様を簡素化します。Vitor Pamplonaは「良さそう」とサインオフし、fiatjafはマージの準備ができているかを尋ねました。この変更は、Amberが今週出荷したNIP-44 v3 ContentProviderオーソリティ登録への道を開きます。

### NIP-44 v3 (仕様に先立ってのAmber実装)

Amberは、暗号化アップグレードとContentProviderオーソリティ登録を実装する8つのコミットとともにv6.2.0でNIP-44 v3を出荷しましたが、NIPsリポの仕様PRはまだ着地していません。NIP-44自体は、署名されたイベント内で使用されるバージョン付き暗号化ペイロード形式を定義します。既存のv2 (2024年から本番) はsecp256k1 ECDH、HKDF、パディング、ChaCha20、HMAC-SHA256、およびbase64を使用します。v3ワイヤーフォーマットはnonceの前に新しいバージョンバイト (0x03) を追加し、受信側クライアントがアルゴリズムを明示的に交渉できるようにします。Amberの実装には、無効なv3リクエストの自動拒否、v2承認とは別の専用承認画面、および履歴用の方向ごとの平文ロギングが含まれます。NIPs PRがマージされるまで、v3はAmber固有の拡張機能として立ちます。それを安定したプロトコル全体の信号送信ではなく、前を見た信号として扱ってください。

## NIPディープダイブ: NIP-32 (ラベリング)

[NIP-32](/ja/topics/nip-32/)は、名前空間付きラベル語彙とともにアドレス可能なkind 1985イベントを使用して、任意のNostrアクターがイベント、pubkey、リレー、URL、またはトピックにラベルを付ける構造化された方法を定義します。仕様は2つの新しいタグを導入します: `L`はラベル名前空間を示し、`l`はその名前空間内のラベルを示します。ラベルターゲットタグ (`e`、`p`、`a`、`r`、または`t`) はラベル付けされているものを指定します。名前空間要件は、複数のラベルシステムが衝突するのを防ぎます: `nip28.moderation`の`spam`ラベルは、`relay-report`の`spam`ラベルとは異なるセマンティクスを運びます。

NIP-32をモデレーションを超えて有用にする設計選択は、ラベルがアサーションであり、プロトコルレベルの真実ではないことです。kind 1985イベントは、特定のpubkeyが特定の名前空間で特定のターゲットにラベルを付けたことだけを述べます。信頼モデルはクライアントに委任されます: 各クライアントはどのラベラーを尊重するか、どの名前空間を読むか、および各ラベルにどのUIアフォーダンスを与えるかを選択します。同じプリミティブが、コンテンツ警告、ライセンス割り当て、kind 1ノートのISO-639-1言語タグ、ISO-3166-2地理タグ、コンテンツ分類、分散モデレーション提案、および評判スコアを運びます。

今週のAmethystの[PR #3111](https://github.com/vitorpamplona/amethyst/pull/3111)は、これまでで最大の展開です。それはNIP-32を通じてハッシュタグラベリングとラベルベースのハッシュタグフィードを追加し、ユーザーが信頼されたラベラーによって割り当てられたラベルでブラウズできるようにします。Nostr上でハッシュタグ発見を最初に駆動した以前の`#tag`テキストマッチメカニズムは、ラベルのないノートのフォールバックとして残ります。ハッシュタグとしてのラベルモデルは、同じノートが異なるラベラーによって割り当てられた複数のラベルの下で発見可能であることを意味し、ユーザーは基礎となるノートに影響を与えることなく特定のラベラーをミュートまたはブーストできます。

セルフラベリングもサポートされています。作者は`L`と`l`タグを自分のkind 1ノートに直接添付して、言語、場所、およびトピックを宣言できます。`["L", "ISO-639-1"], ["l", "en", "ISO-639-1"]`とタグ付けされたノートは自身を英語として識別し、サードパーティラベリングインフラストラクチャなしに言語認識クライアントによってフィルタリングできます。

kind 1ノートを英語としてラベル付けし、モデレーションタグを割り当てるNIP-32ラベルイベントの例:

```json
{
  "id": "a5f87fe2d4c8b9a0e3f1c4d5e6a7b8c9d0e1f2a3b4c5d6e7f8091a2b3c4d5e6f",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748908800,
  "kind": 1985,
  "tags": [
    ["L", "ISO-639-1"],
    ["l", "en", "ISO-639-1"],
    ["L", "nip28.moderation"],
    ["l", "approve", "nip28.moderation"],
    ["e", "8b39f4e5d6c7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3", "wss://relay.example.com"]
  ],
  "content": "Labeled as English-language content approved for NIP-28 chat moderation",
  "sig": "f1e2d3c4b5a6978869504132c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5d6e7f80192a3b4c5"
}
```

Amethystの展開と最近のTrusted Relay Assertionsの作業を組み合わせると、NIP-32はNostr上の「ターゲットについてのユーザー駆動アサーション」パターンの標準基盤になりつつあることを示唆します。次のテストは、ラベラー自身が信頼階層を発展させるかどうかです: ユーザーはコンテンツクリエイターをフォローするのと同じように特定のラベラーnpubをフォローするかどうか。

## NIPディープダイブ: NIP-F4 (ポッドキャスト)

[NIP-F4](https://github.com/nostr-protocol/nips/blob/master/F4.md)は、fiatjafが元のドラフト (PR #1093) を公開してから2年3か月後の今週マージされました。プレフィックスFは単純な16進数番号付けです: NIP-F0からNIP-FFはNIP-0AからNIP-0Dと同じ1バイトの16進空間を使用し、上位の16進範囲は01-99の10進範囲が埋まる中でオーバーフローとして機能します。NIP-F4は、オーディオファイル自体のための補完層としてRSSを保ちながら、ポッドキャストがエピソードとメタデータをNostrイベントとして公開する方法を定義します。

コアアーキテクチャの選択は、各ポッドキャストがそれ自体のNostrキーペアであることです。仕様はこれで直接開きます: 「各ポッドキャストはそれ自体のNostrキーペアです」。これにより、ポッドキャストはそのポッドキャスティングプレゼンスを通常のkind 0 / kind 1マイクロブログプレゼンスと組み合わせることができ、キーハンドオーバーまたはMuSig2スタイルの共有署名を通じて時間とともにオーナーシップを変更できます。4つのイベントkindが公開層を運びます:

- **`kind:10154`**: リプレイス可能なポッドキャストメタデータ。`title`、`image`、`description`、オプションの`website`タグ、およびホスト、コホスト、またはエディターの`role`を持つ作者をマークするオプションの`p`タグを運びます。
- **`kind:10164`**: 作者の反対請求。仕様の例ではkind `10064` (訂正のためにオープンなタイポ) を使用していますが、見出しと周囲のテキストはそれを`kind:10164`として識別します。ユーザーは自分が著作するポッドキャストのpubkeyをリストするので、クライアントは`kind:10154`の`p`タグを推定された作者からの同等の主張に対して検証できます。これがなければ、ポッドキャストは誰でもホストとして誤ってタグ付けできます。
- **`kind:54`**: ポッドキャストpubkeyによって直接著作されたエピソードイベント。タグには`title`、オプションの`image`、`description`、および1つ以上の`audio`タグが含まれます。各`audio`タグは`["audio", "<audio-url>", "<optional_media_type>"]`です。仕様は「さらなる発見の後にここで指定される他の重要なフィールド」と述べており、マージされた形式は意図的に最小限です。
- **`kind:10054`**: [NIP-51](/ja/topics/nip-51/)スタイルのお気に入りポッドキャストリストで、ユーザーがフォローしているポッドキャストをマークできるようにします。

マージ周りのスレッド討論は、Podcasting 2.0共著者[Dave Jones](https://github.com/daveajones)、[Alex Gleason](https://github.com/alexgleason)、[Mike Terenzio](https://github.com/mterenzio)、[Pablo F7z](https://github.com/pablof7z)、および[staab](https://github.com/staab)を巻き込みました。JonesはRSSを置き換えるいかなる試みにも強く反対しました: 「それは何度も試みられ、常に失敗してきた」、JSONfeed、XMPP、AMP、TwitterのAPI、およびSpotifyの失敗した移行を引き合いに出しました。Terenzioは提案をRSSの上のソーシャルレイヤーとして再フレームし、RSS自体を配信レイヤーとして保ちました。fiatjafは一歩下がって提案を熟成させることに同意しました: 「あなたが言ったことすべてに同意しますが、それでも実現できると思います、しばらくここで止めましょう」。2年後、マージされた仕様は置換よりも共存に近く着地しました。

3つの設計上の疑問がマージされた仕様に明示的に残っています:

- `kind:10164`のタイポ (例が`10064`を示す) は、クライアントが安全に相互運用できる前に和解する必要があります。
- RSS GUIDリンクなしのエピソードレベルの発見はオープンなままです。マージされた仕様には`i`タグ、`podcast:item:guid`形式、またはRSSブリッジメカニズムがありません。既存のRSSカタログをkind 54イベントにブリッジしたいクライアントは、ブリッジ規約自体を定義しなければなりません。
- `kind:54`定義の「その他の重要なフィールド」スタブは、ビットレート、時間、言語、トランスクリプトポインター、チャプター、およびセグメントごとのメタデータをフォローアップ提案のためのオープンな領域として残します。

Amethystの[PR #3105](https://github.com/vitorpamplona/amethyst/pull/3105)はマージから数日以内にエピソードリストとインラインプレーヤーを備えた専用ポッドキャスト画面を実現し、最初の主要クライアント実装となりました。JumbleはGIFピッカーと並んで初期のポッドキャスト添付の足場を出荷しました。Wavlakeは最大のNostrネイティブポッドキャストプラットフォームのままで、既存のkind 31337音楽トラックイベントをNIP-F4のkind 54エピソードモデルに合わせるかどうかを決定する必要があります。

マージされた仕様の最小タグセットに一致するNIP-F4 kind 54エピソードイベントの例:

```json
{
  "id": "55807e7d5cd90d0303d7dce7397f996fdbaed8697903f326c7cf8ad999b9de3d",
  "pubkey": "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "created_at": 1748995200,
  "kind": 54,
  "tags": [
    ["title", "Episode 42: Why RSS Won"],
    ["image", "https://podcast.example.com/ep42-cover.jpg"],
    ["description", "Dave Jones and fiatjaf on protocol coexistence and the social layer."],
    ["audio", "https://podcast.example.com/audio/ep42.mp3", "audio/mpeg"]
  ],
  "content": "In this episode we discuss the two-year journey of NIP-F4 from draft to merge, and why coexistence with RSS turned out to be the right architectural choice.",
  "sig": "abc123def456789012345678901234567890abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef01234567"
}
```

PR #1093は27か月間オープンで、マージされたNIPs PRの中央オープン期間を大きく上回っています。NIP-F4の次のテストは、kind 10164のタイポが和解されるかどうか、実装者からエピソード発見およびRSSブリッジ規約が出現するかどうか、および主要なポッドキャストホストが仕様が推奨するようにポッドキャストごとのキーペアの下で公開するかどうかです。
