---
title: 'Nostr Compass #14'
date: 2026-03-18
translationOf: /en/newsletters/2026-03-18-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Nostr Compassへようこそ。Nostrの週刊ガイドです。

**今週の内容:** [Amethyst](https://github.com/vitorpamplona/amethyst)が完全な[NIP-47](/ja/topics/nip-47/)（Nostr Wallet Connect）メソッドサポートを実装、[Alby Hub](https://github.com/getAlby/hub)が[v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6)で複数relayサポートを追加、[Amber](https://github.com/greenart7c3/Amber)が組み込みTorとより細かい署名者権限を備えた[v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3)を出荷、[Zeus](https://github.com/ZeusLN/zeus)が[PR #3835](https://github.com/ZeusLN/zeus/pull/3835)でリスクのあるNWC keysendパスを削除。[Notedeck](https://github.com/damus-io/notedeck)が[v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2)で[NIP-94](/ja/topics/nip-94/)（ファイルメタデータ）イベントを通じてリリースを発見する署名付きアップデーターを出荷、[Damus](https://github.com/damus-io/damus)が古い[NIP-65](/ja/topics/nip-65/)（Relayリストメタデータ）状態を修正、[Nostrability Outbox](https://github.com/nostrability/outbox)が修正データでベンチマーク結果を改訂、[Primal iOS](https://github.com/PrimalHQ/primal-ios-app)がDM用の直接relayサブスクリプションをテスト。[Primal Android](https://github.com/PrimalHQ/primal-android-app)が[3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7)を出荷、[Route96](https://github.com/v0l/route96)が[v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0)を出荷、[OpenChat](https://github.com/DavidGershony/openChat)が[v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11)でMarmot相互運用性を強化、[Pika](https://github.com/sledtools/pika)が[pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1)でランタイムを統合、[Nostria](https://github.com/nostria-app/nostria)が[NIP-85](/ja/topics/nip-85/)（Trusted Assertions）Web of Trustフィルタリングを追加。NIPsリポジトリが[NIP-54](/ja/topics/nip-54/)（Wiki）Djotマークアップと[NIP-19](/ja/topics/nip-19/)（Bech32エンコードエンティティ）の5000文字入力上限をマージ。

## ニュース

### Wallet Connectサポートが拡大し、ウォレットクライアントが障害パスを強化

vitorpaplonaがメンテナンスするAndroidクライアントの[Amethyst](https://github.com/vitorpamplona/amethyst)が[PR #1828](https://github.com/vitorpamplona/amethyst/pull/1828)をマージし、[NIP-47](/ja/topics/nip-47/)実装をほぼ完全なプロトコルカバレッジに近づけました。このパッチは`make_invoice`、`lookup_invoice`、`list_transactions`、`get_balance`、`get_info`、ホールドインボイスメソッド、TLVレコード付きkeysendサポート、kind `13194`による機能ディスカバリー、[NIP-44](/ja/topics/nip-44/)（暗号化ペイロード）を使用したkind `23197`の通知イベントを追加します。これにより、アプリ固有の拡張に頼ることなく、クライアントのNWCサーフェスが大幅に拡大されました。

周辺のウォレットスタックも同じ方向に動きました。多くのNWCデプロイメントを支えるセルフカストディアルLightningノードおよびウォレットサービスの[Alby Hub](https://github.com/getAlby/hub)が、複数relayサポートとよりシンプルな接続・スワップフローを備えた[v1.21.6](https://github.com/getAlby/hub/releases/tag/v1.21.6)を出荷しました。モバイルLightningウォレットの[Zeus](https://github.com/ZeusLN/zeus)が、そのフローにおけるサイレントな資金流出パスを特定した後、NWC keysendサポートを削除する[PR #3835](https://github.com/ZeusLN/zeus/pull/3835)をマージし、同時にペンディングイベントとCashuアクティビティの処理も修正しました。Nostr上のウォレット接続は広がっており、実装者はセキュアにしにくいフローを削除しています。

### Notedeckがリリース発見をNostr上に移行

[先週のNotedeck記事に続き](/en/newsletters/2026-03-11-newsletter/)、Damusチームのネイティブデスクトップクライアント[Notedeck](https://github.com/damus-io/notedeck)が[PR #1326](https://github.com/damus-io/notedeck/pull/1326)をマージした後、[v0.8.0-rc2](https://github.com/damus-io/notedeck/releases/tag/v0.8.0-rc2)を出荷しました。新しいアップデーターは署名されたkind `1063`リリースイベントを購読し、ローカルプラットフォームと照合し、参照されたバイナリをダウンロードして、インストール前にSHA256ハッシュを検証します。リリースメタデータはもはやGitHub APIやプロジェクトウェブサイトから取得する必要はありません。信頼されたリリースpubkeyとrelay接続で十分です。

同じパッチは、GitHubリリースアーティファクトからこれらのイベントを公開する`notedeck-release` CLIも追加しており、リリースパイプラインにNostrネイティブの公開パスと発見パスの両方が備わったことになります。また、DamusとNotedeckのアップデーターモデルをZapstoreのrelay公開署名リリースフローにかなり近づけました。Zapstoreの`zsp`ツールは既にソフトウェアアセットをkind `1063`または`3063`イベントとして処理しているため、このパスは1つのクライアントや1つのパブリッシャーに固定されていません。リリース候補の残りはフォローカラム、プロフィール「View As User」、[NIP-59](/ja/topics/nip-59/)（Gift Wrap）サポート、リアルタイムノート統計、[NIP-11](/ja/topics/nip-11/)（Relay情報ドキュメント）制限処理など、実用的なデスクトップ作業ですが、アップデーターがこの1つのリリースサイクルを超えて存続する可能性が最も高い部分です。

### Relay状態がランタイム動作に近づく

[Damus](https://github.com/damus-io/damus)が[PR #3665](https://github.com/damus-io/damus/pull/3665)をマージし、古い保存済みrelayリストイベントIDを最新のkind `10002`イベントの直接データベースクエリに置き換えました。古い値が古くなると、relay追加・削除操作がブートストラップや1年前のリストにフォールバックし、一部のrelay変更が成功したように見えても実際のアクティブ状態は変わらないままになる可能性がありました。[PR #3690](https://github.com/damus-io/damus/pull/3690)はLMDBコンパクション中に古い`lock.mdb`状態を削除することで2番目の障害パスを修正し、次回起動時にアプリが`SIGBUS`でクラッシュしなくなります。

[Primal iOS](https://github.com/PrimalHQ/primal-ios-app)が[PR #194](https://github.com/PrimalHQ/primal-ios-app/pull/194)をオープンし、会話中にチャット相手の[NIP-04](/ja/topics/nip-04/)（暗号化ダイレクトメッセージ）書き込みrelayに直接サブスクライブし、キャッシュサーバーをフォールバックとして維持します。[Nostur](https://github.com/nostur-com/nostur-ios-public)が[PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53)をオープンし、ランダム化されたrelayスコアリング、nostr.watchの[NIP-66](/ja/topics/nip-66/)稼働状況フィルタリング、Thompson Samplingを組み合わせて、relay選択を固定ヒューリスティックから学習ポリシーに変更します。クライアントは長い間relay選択をセットアップデータとして扱ってきましたが、より多くのアプリがそれを測定と修復ロジックが必要なライブ状態として扱うようになっています。

## リリース

### Primal Android 3.0.7

Primalの Androidクライアント[Primal Android](https://github.com/PrimalHQ/primal-android-app)が、新しいポールとウォレットサイクルを含む[3.0.7](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.7)を出荷しました。[PR #945](https://github.com/PrimalHQ/primal-android-app/pull/945)がzapベースのポール投票を追加、[PR #948](https://github.com/PrimalHQ/primal-android-app/pull/948)が投票読み込みをページネーションし大規模なポールの使いやすさを維持、[PR #965](https://github.com/PrimalHQ/primal-android-app/pull/965)がすべてのトランザクションのzapレシートを取得します。同リリースでは[PR #968](https://github.com/PrimalHQ/primal-android-app/pull/968)でサポートされるイベントに[NIP-89](/ja/topics/nip-89/)（推奨アプリケーションハンドラー）クライアントメタデータをタグ付けし、ダウンストリームクライアントがイベントの出所をよりクリーンに属性付けできるようになります。

### Amber v4.1.3

[先週のAmber記事に続き](/en/newsletters/2026-03-11-newsletter/)、[NIP-55](/ja/topics/nip-55/)フロー用のAndroid署名者アプリ[Amber](https://github.com/greenart7c3/Amber)が[v4.1.3](https://github.com/greenart7c3/Amber/releases/tag/v4.1.3)を出荷しました。このリリースは最近の[NIP-42](/ja/topics/nip-42/)relay認証作業の上に、より多くの運用強化を施しています。[PR #327](https://github.com/greenart7c3/Amber/pull/327)がOrbotサポートに加えて組み込みTorを追加、[PR #324](https://github.com/greenart7c3/Amber/pull/324)が粗いNIPベースの暗号化権限をコンテンツタイプ固有のルールに置き換え、[PR #336](https://github.com/greenart7c3/Amber/pull/336)がオフラインフレーバーからネットワーク権限を削除し、[PR #335](https://github.com/greenart7c3/Amber/pull/335)がそれを維持するためのCIチェックを追加します。[PR #322](https://github.com/greenart7c3/Amber/pull/322)もPINストレージを暗号化DataStoreに移行しました。

このリリースは署名者の境界自体を強化します。実際の鍵やrelay認証の判断をAmberに渡すAndroidフローにとって、難しい部分は署名者に何ができるかだけではなく、どれだけ狭くスコープを制限できるかでもあります。

### Route96 v0.6.0

[先週のRoute96記事に続き](/en/newsletters/2026-03-11-newsletter/)、Blossomと[NIP-96](/ja/topics/nip-96/)（HTTPファイルストレージ）をサポートするメディアサーバーの[Route96](https://github.com/v0l/route96)が[v0.6.0](https://github.com/v0l/route96/releases/tag/v0.6.0)をリリースしました。このリリースは設定とホワイトリスト状態をホットリロード付きでデータベースに移動し、コールドまたは古くなったファイル向けの保持ポリシーを追加します。また、より豊富な`GET /user/files`エンドポイントに加え、ダウンロードとエグレスのファイル統計追跡も追加し、オペレーターにストレージサーバーの使用状況に関するより多くの可視性を提供します。

### OpenChat v0.1.0-alpha.11

[先週のOpenChat記事に続き](/en/newsletters/2026-03-11-newsletter/)、Marmotスタック上に構築されたAvaloniaベースのチャットクライアント[OpenChat](https://github.com/DavidGershony/openChat)が、1週間の高速プロトコル作業の後に[v0.1.0-alpha.11](https://github.com/DavidGershony/openChat/releases/tag/v0.1.0-alpha.11)を出荷しました。[コミット c33895d](https://github.com/DavidGershony/openChat/commit/c33895d6b1a198f01b9b01a7be974bdce033fb9c)がWelcomeイベントを[NIP-59](/ja/topics/nip-59/) gift wrapでラップし古いMIP-00タグ正規化シムを削除、[コミット 2738ff4](https://github.com/DavidGershony/openChat/commit/2738ff428154f60f50debb8f2a53662d427b28f1)がMIP-02準拠監査を完了、[コミット 8e470cf](https://github.com/DavidGershony/openChat/commit/8e470cf7945bced010168c8229d73d67db638b9f)がMIP-03グループメッセージ暗号化について同様に完了しました。[コミット 129ca37](https://github.com/DavidGershony/openChat/commit/129ca37e264efaa2d1a8b04fe95cd72e5e212547)もNIP-44処理を共有marmot-cs実装に統合し、クライアントサイドの暗号ドリフトのリスクを低減しました。

### nak v0.19.0 および v0.19.1

fiatjafのコマンドラインNostrツールキット[nak](https://github.com/fiatjaf/nak)が[v0.19.0](https://github.com/fiatjaf/nak/releases/tag/v0.19.0)と[v0.19.1](https://github.com/fiatjaf/nak/releases/tag/v0.19.1)を出荷しました。0.19シリーズは[コミット 5f4efdb](https://github.com/fiatjaf/nak/commit/5f4efdbc69a36fc80ea3f97b2cdee1db6a7c5b47)でグループフォーラムUIを追加、[コミット da0b753](https://github.com/fiatjaf/nak/commit/da0b75337198010687aceb6a07bbae67407faee3)でグループメタデータ編集を完全置換フローに切り替え、[コミット bef67d3](https://github.com/fiatjaf/nak/commit/bef67d35d259e0450debf0fd870e1a937a2406bf)で古い`no-text`処理を`supported_kinds`に置き換えました。グループ実装者にとって、これによりCLIがグループ仕様とクライアントが向かう方向と整合します。

## プロジェクトアップデート

### Amethyst

[先週のAmethyst記事に続き](/en/newsletters/2026-03-11-newsletter/)、Nostrで最も広いプロトコルサーフェスの1つを持つAndroidクライアント[Amethyst](https://github.com/vitorpamplona/amethyst)は、NIP-47パッチ後もウォレットとrelay作業の構築を続けました。[PR #1853](https://github.com/vitorpamplona/amethyst/pull/1853)がrelay管理画面全体に[NIP-45](/ja/topics/nip-45/)（イベントカウント）COUNTクエリを追加し、各relayがホームフィード、通知、DM、インデックスデータについて実際にどれだけのイベントを保持しているかをユーザーが確認できるようになりました。[PR #1849](https://github.com/vitorpamplona/amethyst/pull/1849)が[NIP-17](/ja/topics/nip-17/)（プライベートダイレクトメッセージ）チャット用の暗号化ファイルアップロードを追加し、ストレージホストが暗号化バージョンを拒否した場合の非暗号化アップロードへのリトライパスも備えています。

[PR #1791](https://github.com/vitorpamplona/amethyst/pull/1791)も完全な[NIP-46](/ja/topics/nip-46/)（Nostr Connect）デスクトップバンカーログインをハートビートインジケーター付きで実装しました。これが重要なのは、リモート署名の失敗がユーザー側からはランダムなUI破損のように感じられることが多いためです。クライアントは署名者が生きているかどうかと最近いつ応答したかを表示し、現在のセッションがバンカーを使用している場合もそれを明確にします。

### Nostria

ローカルファーストスタックを中心に構築されたマルチプラットフォームクライアントの[Nostria](https://github.com/nostria-app/nostria)が、フィードとスレッドリプライのWeb of Trustフィルタリングを追加する[PR #561](https://github.com/nostria-app/nostria/pull/561)をマージしました。この機能は既存のtrust-serviceランクデータを使用し、フィードフィルターとリプライフィルターの両方として公開し、閾値をクリアしないランクの著者を非表示にしつつ、信頼された子孫が存在する場合はスレッド構造を保持します。これにより、「全員を表示」とハードコードされたリストベースのキュレーションの中間レイヤーがユーザーに提供されます。

同じ週に[PR #563](https://github.com/nostria-app/nostria/pull/563)も実装され、サマリーページにコンテンツフィルタリングとリポストサポートが追加されました。追跡されたPRリスト外では、Nostriaはパワーユーザーサーフェスの充実も進めています。最新のBrainstorm Web of Trustサービスへのアプリ内サインアップ、NWCとBOLT-11インボイスを使用したDMでの送金・受金フロー、絵文字NIPを通じたNostrネイティブのGIF処理、ポッドキャストフィードから既存のLightningスプリットを取り込める強化されたRSSインポートパスも追加されました。Nostriaはランキング、メディア、ペイメント、パブリッシングを1つの接続されたアプリサーフェスとして扱っています。

### Nostur

nostur-comがメンテナンスするiOSクライアントの[Nostur](https://github.com/nostur-com/nostur-ios-public)が、アウトボックスルーティングを固定プランからスコア付きポリシーに変更する[PR #53](https://github.com/nostur-com/nostur-ios-public/pull/53)をオープンしました。このパッチはランダム化されたrelayスコアリング、キャッシュされたnostr.watchフィードによる[NIP-66](/ja/topics/nip-66/) relay稼働状況フィルタリング、Thompson Samplingを追加し、relayの成功・失敗データが将来の選択を変更するようにします。設計はフィルタリングされるrelayが多すぎる場合のセーフティバルブを保持し、`.onion` relayも保持します。これは、relay選択を適応型システムとして扱うクライアントの最も明確な現在の例の1つです。

### Nostrability Outbox

[以前のOutboxベンチマークレポートに続き](/ja/newsletters/2026-03-04-newsletter/)、[NIP-65](/ja/topics/nip-65/)と[NIP-66](/ja/topics/nip-66/)クライアントルーティングに焦点を当てたベンチマーク・分析プロジェクトの[Nostrability Outbox](https://github.com/nostrability/outbox)は、今週自身の主張を精緻化しました。[PR #35](https://github.com/nostrability/outbox/pull/35)がインフレートされたThompson Samplingの結果を1,511回のランにわたる完全な再ベンチマークに置き換え、NDKスタイルルーティング向けに`CG3`バリアントを推奨しました。[PR #43](https://github.com/nostrability/outbox/pull/43)が減衰とユースケース比較を追加し、`0 follows`キャッシュポイズニングバグを修正し、キャッシュTTLを固定した後にTellurideデータセットを再実行しました。

これは通常の意味でのプロダクト作業ではありませんが、プロジェクトの数値がよりシャープになり、以前過大に主張していた部分ではより控えめになったため、クライアント作者にとって重要です。修正された結果は依然として有用です。ランダム化された選択はOutboxが関心を持つケースにおいて純粋に決定論的なルーティングに勝ち続けており、Thompson型の学習はクライアントが有用なrelay履歴を永続化する場合にカバレッジを実質的に改善でき、[NIP-66](/ja/topics/nip-66/)稼働状況フィルタリングはデッドrelayへの無駄な時間を削減します。この作業は[NDK #387](https://github.com/nostr-dev-kit/ndk/pull/387)、[Nostur #53](https://github.com/nostur-com/nostur-ios-public/pull/53)、[Amethyst #1833](https://github.com/vitorpamplona/amethyst/pull/1833)、[rust-nostr #1282](https://github.com/rust-nostr/nostr/pull/1282)、[welshman #53](https://github.com/coracle-social/welshman/pull/53)、[applesauce #54](https://github.com/hzrd149/applesauce/pull/54)と[applesauce #55](https://github.com/hzrd149/applesauce/pull/55)を含む具体的な実装提案にも発展しています。

### White Noiseバックエンド

White Noiseやその他のMarmotツーリングが使用するRustバックエンドの[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)が、Blossomメディア処理周辺の境界強化パッチ2件をマージしました。[PR #637](https://github.com/marmot-protocol/whitenoise-rs/pull/637)がBlossom URLにHTTPSを強制しアップロードタイムアウトを追加、[PR #642](https://github.com/marmot-protocol/whitenoise-rs/pull/642)がBlobダウンロードを`100 MiB`に上限設定し、過大なメディアプルがサービス拒否パスに変わることをブロックします。プライベートメッセージングソフトウェアにとって、メディアURLは暗号化されたアプリケーションロジックと信頼できないネットワークインフラストラクチャの間の最も鋭いインターフェースの1つです。今週チームはそのエッジを強化しました。

### rust-nostr

Rustプロトコルライブラリの[rust-nostr](https://github.com/rust-nostr/nostr)が、`LocalRelayBuilderNip42`のコンビニエンスコンストラクターを追加する[PR #1280](https://github.com/rust-nostr/nostr/pull/1280)をマージしました。新しいreadとwriteヘルパーは、埋め込みrelayやテストセットアップに[NIP-42](/ja/topics/nip-42/)認証ポリシーをコードに変換するためのより明確な方法を提供します。これは小さなライブラリパッチですが、毎回ボイラープレートを繰り返さずに認証を有効にする必要があるローカルまたはアプリバンドルrelayを構築するチームにとって重要です。

### Pika

[以前のPika記事に続き](/ja/newsletters/2026-03-04-newsletter/)、Marmotベースのメッセージングアプリ[Pika](https://github.com/sledtools/pika)が、ランタイム統合に焦点を当てたリリースサイクルで[pika/v1.1.1](https://github.com/sledtools/pika/releases/tag/pika/v1.1.1)と[pikachat-v1.1.1](https://github.com/sledtools/pika/releases/tag/pikachat-v1.1.1)を出荷しました。[PR #542](https://github.com/sledtools/pika/pull/542)がCLIとサイドカー用の共有Marmotランタイムファサードを導入し、アプリホストも同じサーフェスに移行します。[PR #556](https://github.com/sledtools/pika/pull/556)がOpenClawエージェントのライフサイクルとプロビジョニング状態を強化、[PR #600](https://github.com/sledtools/pika/pull/600)がバックアップからの復元と管理環境向けのより厳格な回復安全性を追加しました。

直接的なユーザー向けサーフェスは前回のPika記事よりも小さいですが、アーキテクチャの変更は意味があります。グループ、メディア、通話、セッションロジックを1つの共有ランタイムの背後にまとめることで、Marmotスタックの成長に伴ってアプリとデーモンが乖離する可能性が減少します。

## NIPアップデート

[NIPsリポジトリ](https://github.com/nostr-protocol/nips)への最近の変更：

**マージ済み：**

- **[NIP-54](/ja/topics/nip-54/)（Wiki）: AsciidocからDjotへの切り替え**（[PR #2242](https://github.com/nostr-protocol/nips/pull/2242)）：kind `30818`のWikiコンテンツがDjotを正規マークアップ形式として使用するようになりました。マージされたテキストは明示的なwikilink動作、kind `818`のマージリクエスト例、kind `30819`のリダイレクト例、`d`タグの非ラテンスクリプト正規化例を追加します。これにより、実装者はAsciidocよりもクリーンなパースターゲットを得られ、Ruby中心のツールチェーンに依存するスペックパスが1つ削除されます。

- **[NIP-19](/ja/topics/nip-19/)（Bech32エンコードエンティティ）: 入力制限の追加**（[PR #2264](https://github.com/nostr-protocol/nips/pull/2264)）：仕様がBech32エンコードエンティティ文字列を5000文字で上限設定することを推奨するようになりました。NIP-19文字列はQRフロー、ディープリンク、共有シート、多くのクライアントにわたるユーザー貼り付け入力に表示されるようになったため、これは実際のパーサー価値を持つ小さな変更です。

**オープンPRとディスカッション：**

- **[NIP-49](/ja/topics/nip-49/)（秘密鍵暗号化）向けNostrキーファイル**（[PR #2269](https://github.com/nostr-protocol/nips/pull/2269)）：パスワード暗号化された鍵のエクスポートとインポート用の`.nostrkey`ファイル形式を提案しています。マージされれば、生の`ncryptsec`文字列をコピーするよりも通常のファイルベースのバックアップパスをクライアントに提供します。

- **[NIP-43](/ja/topics/nip-43/)（Relayアクセスメタデータとリクエスト）のメンバーシップ状態の一貫性**（[PR #2267](https://github.com/nostr-protocol/nips/pull/2267)）：relayがpubkeyごとに1つの権威あるメンバーシップ状態を維持すべきであることを明確にするセクションを追加します。メンバーシップの変更やリプレイされた履歴に関するグループクライアントロジックを簡素化します。

- **[NIP-17](/ja/topics/nip-17/)（プライベートダイレクトメッセージ）の削除ガイダンス**（[PR #2260](https://github.com/nostr-protocol/nips/pull/2260)）：gift wrapされた削除イベントを通じたプライベートメッセージの編集と削除のための具体的なパスを提案しています。作業はまだオープンですが、NIP-17が古いDMフローを完全に置き換えるには、クライアント作者にここでの答えが必要です。

- **[NIP-222](/ja/topics/nip-222/)向け共有インテントURI**（[PR #2266](https://github.com/nostr-protocol/nips/pull/2266)）：モバイルおよびデスクトップアプリが共有コンテンツをNostrクライアントに渡す方法を標準化するドラフトです。現在のアプリ間フローで最も粗い相互運用エッジの1つです。

## NIPディープダイブ: NIP-94（ファイルメタデータ）

[NIP-94](/ja/topics/nip-94/)はkind `1063`をファイルのファーストクラスメタデータイベントとして定義します。[仕様](https://github.com/nostr-protocol/nips/blob/master/94.md)はイベントに人間が読める`content`と、ダウンロードURL、MIMEタイプ、ハッシュ、寸法、プレビュー、フォールバック、ストレージサービスヒントの機械可読タグを提供します。これが重要なのは、ファイルがrelayで独自のオブジェクトとしてクエリ可能になるためです。クライアントはファイルが何であるかを理解するために周囲のコンテンツからメタデータをスクレイプする必要がありません。

```json
{
  "id": "6a92ef8d7c3a1b5d4e8f9a0b1c2d3e4f567890abcdef1234567890abcdef1234",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1742342400,
  "kind": 1063,
  "tags": [
    ["url", "https://downloads.example.org/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["m", "application/gzip"],
    ["x", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["ox", "4a5b6c7d8e9f00112233445566778899aabbccddeeff00112233445566778899"],
    ["size", "48392011"],
    ["dim", "0x0"],
    ["magnet", "magnet:?xt=urn:btih:00112233445566778899aabbccddeeff00112233"],
    ["i", "00112233445566778899aabbccddeeff00112233"],
    ["blurhash", "LEHV6nWB2yk8pyo0adR*.7kCMdnj"],
    ["thumb", "https://downloads.example.org/notedeck/v0.8.0-rc2/thumb.png", "bbccddeeff00112233445566778899aabbccddeeff0011223344556677889900"],
    ["image", "https://downloads.example.org/notedeck/v0.8.0-rc2/screenshot.png", "ccddeeff00112233445566778899aabbccddeeff001122334455667788990011"],
    ["summary", "Signed macOS release artifact for Notedeck v0.8.0-rc2"],
    ["alt", "Notedeck desktop release archive"],
    ["fallback", "https://mirror.example.net/notedeck/v0.8.0-rc2/notedeck-macos-universal.tar.gz"],
    ["service", "nip96"]
  ],
  "content": "Notedeck macOS universal build",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

タグは見た目以上の仕事をしています。`x`は配信されるファイルを識別し、`ox`はサーバーサイドの変換前のオリジナルファイルを識別します。プレビュータグによりクライアントは完全なアセットをダウンロードせずにブラウズ可能なファイルインデックスを構築でき、`summary`はそれらの横に短い抜粋を付けられます。`fallback`はメインURLが失敗した場合の第2のソースを提供し、`service`は[NIP-96](/ja/topics/nip-96/)や別のホストなど、ファイル背後のストレージプロトコルをヒントとして示します。したがってNIP-94はソーシャル投稿の下で、生のストレージの上に位置します。ファイル自体を記述し、ファイルに関する会話を記述するものではありません。

今週のNotedeckアップデーターが興味深い理由がここにあります。[PR #1326](https://github.com/damus-io/notedeck/pull/1326)はソフトウェアリリース発見に署名されたkind `1063`イベントを使用し、ダウンロードしたバイナリを公開されたSHA256と照合して検証します。同じイベント形状でソフトウェアアーティファクトもメディアアップロードも記述できます。NIP-94は安定するほど古くなっていますが、より多くのプロジェクトがメタデータイベントを人のための装飾としてだけでなく、機械のためのトランスポートとして扱っているため、成長の余地があります。

## NIPディープダイブ: NIP-54（Wiki）

[NIP-54](/ja/topics/nip-54/)はkind `30818`をWiki記事イベントとして定義します。[仕様](https://github.com/nostr-protocol/nips/blob/master/54.md)は`d`タグを正規化された記事トピックとして扱い、多くの著者が同じ主題のエントリを公開できるようにします。記事本文は`content`に格納され、タグは正規化されたアイデンティティ、表示タイトル、要約、以前のバージョンへの参照を処理します。つまりNIP-54は単なるコンテンツ形式ではなく、取得とランキングの問題でもあります。各クライアントはどの記事バージョンを表示するかを決定する必要があるためです。

```json
{
  "id": "8c94e5d1f2a300112233445566778899aabbccddeeff00112233445566778899",
  "pubkey": "00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff",
  "created_at": 1742342400,
  "kind": 30818,
  "tags": [
    ["d", "nostr-wiki"],
    ["title", "Nostr Wiki"],
    ["summary", "Djot-formatted reference article about Nostr wiki events"],
    ["a", "30818:11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff:nostr-wiki", "wss://relay.example.org", "fork"],
    ["e", "11223344556677889900aabbccddeeff00112233445566778899aabbccddeeff", "wss://relay.example.org", "fork"]
  ],
  "content": "Nostr is a [protocol][] for carrying events across relays.\n\n[protocol]: nostr:nevent1example",
  "sig": "33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889900112233cc44dd55ee66ff77889900aabbccddeeff00112233445566778899001122"
}
```

今週のマージは[PR #2242](https://github.com/nostr-protocol/nips/pull/2242)で正規マークアップをAsciidocからDjotに変更しました。これが実装者にとって重要なのは、Djotがより厳密な独立した仕様と言語間でよりシンプルなパーサーストーリーを持つためです。マージされたテキストはリファレンススタイルwikilinkの解決方法、kind `818`のマージリクエストの使用方法、kind `30819`のリダイレクトの使用方法、非ラテンスクリプトの`d`タグ正規化の動作方法も明確にしています。これらは2つの独立したクライアントがリンクの指す先の記事について合意する部分です。

NIP-54はプロトコル内で特殊な位置にもあります。Wikiクライアントはコンテンツレンダリングを必要としますが、ランキングポリシーも必要です。リアクション、relayリスト、コンタクトリスト、明示的な委譲シグナルはすべて、特定のトピックでどの記事が勝つかに影響します。Djotへの切り替えはこのランキング問題を解決しませんが、その下にあったパーサーの曖昧さの1つを取り除きます。今このマージが重要な理由がここにあります。変更はより見栄えの良い散文フォーマットについてではなく、マルチクライアントWiki動作を一貫して実装しやすくすることについてです。

何か作っていますか、それとも取り上げてほしいことがありますか？Nostrで[NIP-17](/ja/topics/nip-17/) DMを`npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923`宛にお送りください。
