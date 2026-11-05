---
title: 'Nostr Compass #47'
date: 2026-11-04
publishDate: 2026-11-04
draft: false
type: newsletters
translationOf: /en/newsletters/2026-11-04-newsletter.md
translationDate: 2026-11-05
---

今週は、[Amethyst](/ja/newsletters/2026-11-04-newsletter/#amethyst)が[埋め込みのセキュリティレビュー](https://github.com/vitorpamplona/amethyst/pull/4710)を受けた修正を含むインラインnappletを出荷し、[Napplets](/ja/newsletters/2026-11-04-newsletter/#napplets---web-packages)がアプレットのアイデンティティをドキュメントごとのポートに結び付け、[Marmotのmdk](/ja/newsletters/2026-11-04-newsletter/#marmot-protocol-mdk)のナイトリー版がグループメッセージングを強化しました。ほかにもリレー、ウォレット、署名ライブラリ、新しいアプリに変更がありましたが、その多くはマージ済みでまだ出荷されていないソースです。

## トップニュース {#top-stories}

### Amethyst {#amethyst}

AndroidクライアントのAmethystが[v1.21.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.21.0)をリリースし、Android 11以降とデスクトップでnappletをノート内にインラインで実行できるようになりました。[埋め込みのセキュリティレビュー](https://github.com/vitorpamplona/amethyst/pull/4710)を受けた修正により、リレーへのアクセス権を持つnappletなら何でも復号済みのDMを読めてしまう経路が塞がれました。復号には別途ユーザーの許可が、`nostr.signEvent`には署名者の権限が必要になりました。ただし、デスクトップのChromiumレンダラーは引き続きサンドボックス化されていません。[ファイルごとの添付暗号化の変更](https://github.com/vitorpamplona/amethyst/pull/4701)により、[NIP-17](/ja/topics/nip-17/)のプライベートダイレクトメッセージでは添付ファイルごとに新しいAES-GCM鍵とnonceが使われるようになりました。これまでは複数ファイルをまとめて送ると、鍵とnonceの両方が使い回されていました。上流のリスク説明はコード解析に基づくもので、エクスプロイトは再現されていません。また、送信済みのファイルは修復されません。

### Marmot Protocol (mdk) {#marmot-protocol-mdk}

mdkは、MarmotによるMLSベースのNostr向け暗号化メッセージングキットです。今回はテスト専用のナイトリープレリリースのみが公開され、この系列に安定版はありません。11月2日のナイトリーでは、グループ内で[新しい送信がキューにある古い送信の完了を待つ](https://github.com/marmot-protocol/mdk/pull/2849)ようになりました。これにより、履歴に追いつこうとしているメンバーにとって暗号化の世代の順序が保たれます。ただし、メッセージが失われないことまでは保証されません。マージ済みでデフォルト無効の[失われたWelcomeの修復](https://github.com/marmot-protocol/mdk/pull/2936)は、[Marmotのハートビート規則](https://github.com/marmot-protocol/marmot/pull/497)に従って動作します。最新のキャリア公開から10分以上経った後の活動が相手のハートビートに現れた時点で、保持していたWelcomeをそのまま再送します。ハートビートの間隔や時計の遅れによって修復が1時間以上遅れることがあり、完了までの時間に上限はありません。[デバイスリンクのコマンド](https://github.com/marmot-protocol/mdk/pull/2922)は引き続きデフォルト無効のdev-device-groups機能の下にあり、本番環境では無効です。

### Napplets - Webパッケージ {#napplets---web-packages}

サンドボックス化されたNostrアプレット向けのWebパッケージであるNappletsは、[core 0.37.0](https://github.com/napplet/web/releases/tag/%40napplet/core%400.37.0)、[nap 0.36.0](https://github.com/napplet/web/releases/tag/%40napplet/nap%400.36.0)、[shim 0.35.0](https://github.com/napplet/web/releases/tag/%40napplet/shim%400.35.0)をリリースし、[アプレットのアイデンティティをドキュメントごとのMessagePortに結び付けました](https://github.com/napplet/web/pull/302)。検証済みの(dTag, artifactHash)アイデンティティは、作成されたiframeからのhelloで渡されたポートに結び付けられ、NAPの通信はすべてそのポートを通ります。ナビゲーションで読み込まれたドキュメントには権限が一切付与されません。互換性を保つ手段がないため、Windowメッセージングを使い続けているシェルはアップグレードが必要です。その後のソースでは、frame-src 'none'によって[プレビューフレームを検証済みのドキュメントに固定しています](https://github.com/napplet/web/pull/305)。

## タグ付きリリース {#tagged-releases}

### Marble {#marble}

Cosignのしきい値署名を基盤とするベータ版クライアントMarbleは、[0.12.23](https://github.com/sybenx/marble/releases/tag/v0.12.23)でリレーをフィードとして閲覧できるようになりました。アドレスを指定してリレーを開くと、まずそのリレー自身の説明が、続いて投稿が新しい順に表示されます。お気に入りのリレーはkind 10012のリストに、リレーグループはkind 30002のセットに保存されます。これらはJumbleと同じリストです。このリリースではリアクションも作り直され、最近使ったリアクションのトレイや自分のカスタム絵文字を使えるようになりました。

### Sidecar {#sidecar}

ノートやWebハイライトを公開するためのブラウザ拡張機能Sidecarは、[1.16.6](https://github.com/dmnyc/sidecar/releases/tag/v1.16.6)でリレー上のウォレットのバックアップを削除できるようになりました。確認を経ると、暗号化されたコピーを空のコピーで置き換え、リレーに破棄を依頼します。接続済みのウォレットはそのまま残ります。ただし、リレーがバックアップを確実に消去する保証はありません。[v1.16.5](https://github.com/dmnyc/sidecar/releases/tag/v1.16.5)以降、SidecarはアップロードするJPEGからEXIF、XMP、IPTCのメタデータを事前に除去しています。さらに[アップロード準備の変更](https://github.com/dmnyc/sidecar/pull/572)により、メタデータを除去できないJPEGはアップロードが阻止されます。

### Haps {#haps}

Hapsは、Nostr鍵のもとでネイティブパッケージを公開・インストールするためのツールです。[Haps 0.1.25](https://github.com/mmalmi/haps/releases/tag/v0.1.25)では、macOS、Linux、Windows向けのバンドルが提供されます。バンドルには、チェックサムで固定されたhtreeヘルパーと、全アーカイブを対象とするSHA256SUMSファイルが含まれます。0.1.24のソースは、Hashtree仕様のドラフトに従って[バージョン付きのHashtree参照を書き込みます](https://github.com/mmalmi/haps/commit/3dd051cefe9e506886a7f036267950282a179ee8)。Haps 0.1.23以前では、レガシー移行用のカタログがないか、インストーラーやCargoビルドを更新しない限り、新しいカタログを読み取れません。

### Cosign {#cosign}

Marbleベータを支えるしきい値署名ライブラリCosignは、[0.12.9](https://github.com/sybenx/cosign/releases/tag/v0.12.9)で参加処理の修正を部分的に入れました。スキャンした招待者を通じて参加する場合、その招待者の寄与と、2人以上の異なる送信者からのピースが必要になりました。スマートフォン同士の参加は依然として拘束されていないため、攻撃者は鍵を2つ持っていれば足ります。また、空の復号パーツについては引き続き証明の検証が省略されます。[0.12.8](https://github.com/sybenx/cosign/releases/tag/v0.12.8)では、メンバーリストを書き込むサーバーが、秘密を把握済みのシェアポイントを依然として選べます。スマートフォンにはMarbleのリリースを通じてのみ修正が届きます。

### nostream {#nostream}

PostgreSQLを基盤とするTypeScript製リレーのnostreamでは、[アウトバウンドのピア同期](https://github.com/cameri/nostream/pull/1043)が[3.12.0](https://github.com/cameri/nostream/releases/tag/nostream%403.12.0)で追加されました。ワーカーは各ピアの[NIP-11](/ja/topics/nip-11/)リレー情報からスコープを読み取り、[NIP-42](/ja/topics/nip-42/)のクライアント認証で認証したうえで、[NIP-77](/ja/topics/nip-77/)のnegentropy同期で差分を突き合わせます。取得したイベントはID、署名、スコープに照らして検証されます。[ピア固有の制限](https://github.com/cameri/nostream/pull/1034)は、設定済みのピアがAUTHを完了した後でのみ適用されます。ソースがリリースされたからといって、実際にどこかのリレーで稼働しているとは限りません。

### diVine {#divine}

短尺ループ動画クライアントのdiVineは、インタラクティブな公開動画ステッカーを搭載した[Android安定版1.0.27](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.27)を公開しました。iOSとmacOSで利用できるかどうかは確認されていません。マージ済みの[ウィンドウより古い範囲の再クエリ](https://github.com/divinevideo/divine-mobile/pull/10711)は、初回の履歴復元が終わった後でのみ実行されます。ギフトラップ、非推奨となった[NIP-04](/ja/topics/nip-04/)の暗号化DM、削除イベントを、リレーごとに100件単位のページで読み込みます。この処理はリレーごとに個別に進みます。一方、既存の履歴取得は1つのカーソルを共有するため、上限に達したリレーでは古い履歴を取りこぼすことがあります。取得範囲には限りがあり、履歴を完全に復元できるわけではありません。

### Whistle {#whistle}

モバイル向けのグループ位置情報共有・チャットアプリWhistleは、[2.0.1](https://github.com/sjmcnamara/whistle/releases/tag/v2.0.1)をリリースしました。Marmot protocol v2上で動作する初の公開リリースです。既存のグループは引き継げないため、グループを作り直し、メンバー全員がアップデートする必要があります。npubアイデンティティは保持されます。招待コードやリンクは廃止され、スキャンによる参加に置き換わりました。既知の問題として、オフライン中に送信したチャットメッセージが遅れて届いたり、届かなかったりすることがあります。リリースではMarmotKitが原因とされています。位置情報の共有には影響ありません。

## 開発中 {#in-development}

### Quartz {#quartz}

Kotlin Multiplatform向けNostrライブラリのQuartzは、リリース2.14.0で[再接続後のライブサブスクリプション再開](https://github.com/vitorpamplona/quartz/pull/82)を提供しました。各リレーは配信済みの最新のcreated_atから再開し、その値はデバイスの時計を上限とします。また、gift-wrapフィルターはバックデートに対応するため、さらに2日分さかのぼります。リレーが障害中に保存した、より古いタイムスタンプのイベントは依然として取りこぼされる可能性があります。マージ済みで未リリースの[件数を考慮したnegentropyウィンドウ](https://github.com/vitorpamplona/quartz/pull/85)は、任意の[NIP-45](/ja/topics/nip-45/)イベント件数をローカルの件数と比較し、リレーの件数を信頼できないものとして扱います。

### Buzz {#buzz}

Buzzは、[kind 5および9005の削除を対象のソフトデリートと同一トランザクションでコミットする](https://github.com/block/buzz/pull/8944)変更をマージしました。これにより、障害が発生しても、対象が有効なまま削除だけが受理されることはなくなりました。過去に生じた不整合な行は修復されません。デバイス間の既読状態を扱うBuzzのドラフトである[NIP-RS](/ja/topics/nip-rs/)のモバイルプロファイルがマージされ、[既読フロンティアをデバイス間で同期](https://github.com/block/buzz/pull/8998)するようになりました。read_state_snapshotを持たない古いリレーでは、ローカルの既読処理は引き続き機能しますが、デバイス間同期はフォールバックなしで停止します。

### Alby Hub {#alby-hub}

[NIP-47](/ja/topics/nip-47/) Nostr Wallet Connectアプリにサービスを提供するセルフカストディ型LightningノードのAlby Hubは、db_migrateまたはPostgres移行の際に各テーブルのIDカウンターを維持する[データベース移行の修正](https://github.com/getAlby/hub/pull/2657)をマージしました。この修正以前は、新しいアプリが削除済みアプリのIDを再利用し、そのトランザクションと分離された残高を引き継ぐ可能性がありました。この修正を含むタグ付きリリースやデプロイは確認されていません。別の[通知に関する変更](https://github.com/getAlby/hub/pull/2677)はアプリごとの失敗を分離しますが、失敗した通知は依然として再試行されずに破棄されます。

### swift-nostr-client {#swift-nostr-client}

Swift 6向けNostrライブラリのswift-nostr-clientは、[RemoteSignerが最初のコマンドの前にconnectハンドシェイクを実行する](https://github.com/yysskk/swift-nostr/pull/287)ようにする破壊的変更をマージしました。新しいconnectsAutomatically設定のデフォルトはtrueで、ハンドシェイクが失敗した場合、コマンドは送信されません。[NIP-46](/ja/topics/nip-46/)のリモート署名シークレットは1回限りしか使えないため、保存済みのクライアント鍵ペアでbunkerセッションを再開するアプリはこれをfalseに設定する必要があります。そうしないと、最初のコマンドで使用済みのシークレットが提示されます。リリースはまだタグ付けされていません。

## 新規プロジェクト {#new-projects}

### Trikey {#trikey}

Trikeyは、スマートフォンアプリとガーディアンが暗号化されたNostrリレーメッセージでやり取りする、プレアルファ版で未監査のウォレットです。[リリース0.1.10-alpha](https://njump.me/nevent1qvzqqqr4dupzqpepqn8d9d5jc8r4qf6h7kd7ldpgrpqgdaw8wjwyrxztkjltnfy4qyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpk2jxzja4q4z8avcsc7jqenpuykke49p3z3halm0xtgmn3h6r6judumrxf)では、起動時にアプリがフリーズする問題に対処しました。双方が既読のwrap IDの記録を再起動後も保持するようになり、署名検証や復号の前にそれらをスキップします。リクエストやアラートに付く有効期限のヒントはリレーでの削除を保証するものではなく、公開者によるパフォーマンス測定はノートPC上で行われたものです。

### Pacto {#pacto}

従来のMarmotグループとNIP-17 DMを併用するデスクトップ向けコミュニティ組織化アプリのPactoは、送信済みメッセージを1分間編集できる未署名の[v0.7.5](https://github.com/covenant-gov/pacto-app/releases/tag/v0.7.5)をリリースしました。[DM配信の修正](https://github.com/covenant-gov/pacto-app/pull/425)により、プールに信頼済みリレーがない場合は送信が即座に失敗し、入力中インジケーターは信頼済みリレー経由で送られます。未マージのオープンなプルリクエストは、[スクワッドイベント](https://github.com/covenant-gov/pacto-app/pull/488)と[暗号化されたスクワッドドキュメント](https://github.com/covenant-gov/pacto-app/pull/490)を追加するものです。

### Mialuna {#mialuna}

メディア重視のFlutter製NostrクライアントであるMialunaは、[バージョン0.19.0のリリース告知](https://njump.me/nevent1qvzqqqr4dupzqeyvpafs936l8quz5nfvskjg9wf8e3sm9q52q72wxmrvc7tdap4xqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqk6ltj5kr6mtq8mkyz9rzqxkkrhq9hsjz675e05rwgltwgreddw3npkkez)を公開し、ユーザー自身のストーリーが期限切れになった際の削除リクエストを追加しました。[変更履歴のコミット](https://github.com/Lwb89dev/mialuna/commit/d0a38cb92dac724e6e7bac6ec8f94a31a378e886)には、リレーへの削除リクエストとBlossomメディアの削除が記録されており、ローカル鍵のアカウントではこれが自動的に実行され、AmberまたはbunkerのアカウントではユーザーがDelete nowを選択するまで待機します。APKとそのデバイス上での動作は独自に検証されていません。削除リクエストは、リレーやサーバーがデータを消去することを保証できません。

### whereAreYou {#whereareyou}

whereAreYouは、QRコードまたは招待リンクで参加するサークル内で位置情報を共有するAndroidアプリで、座標をAES-256-GCMで暗号化し、公開リレー経由で送信します。[メンバー署名のコミット](https://github.com/Dzekdrix/whereAreYou/commit/82121d0f13b4d5256b2392383e74640afde3019e)により、サークル鍵の保持者が別のメンバーになりすまして投稿することを防げるようになり、すべてのデバイスでアップデートが必要です。[Base45形式のアイデンティティバックアップ](https://github.com/Dzekdrix/whereAreYou/commit/82e185967dd0115b93472b3d92a4d0393c8751bc)について、作者は、QRコードを撮影した人なら誰でもその8桁のコードをオフラインで推測でき、作者の見積もりではGPU時間で数十分以内に可能だと警告しています。ベンチマークは公開されていません。この情報源はセキュリティ面での保証を示すものではありません。

## プロトコルと仕様の取り組み {#protocol-and-spec-work}

### Buzz、オーナー承認済みエージェントの認証情報ルートを定義 {#buzz-defines-owner-authorized-agent-credential-routes}

Buzzは[NIP-FA](/ja/topics/nip-fa/)の[オーナー承認済みエージェント認証情報のドラフト](https://github.com/block/buzz/pull/9015)をマージし、[NIP-OA](/ja/topics/nip-oa/)のオーナー証明を通じて承認されたエージェント向けに、付与、アサーション、失効のルートを定義しました。付与は、オーナーのセッションとエージェントの[NIP-98](/ja/topics/nip-98/) HTTP認証の証明を組み合わせたRFC 8693トークン交換によって得られます。失効によりエージェントは切断され、その鍵による再登録も防止されます。NIP-FAはソースにのみマージされたBuzzの仕様であり、本番環境での有効化や相互運用性は主張されていません。

### ポスト量子イベント署名に厳密な検証ルールが追加 {#post-quantum-event-signatures-gain-exact-validation-rules}

長期にわたってオープンになっているポスト量子署名の提案に、[NostrイベントのためのML-DSA-44の厳密な検証ルール](https://github.com/nostr-protocol/nips/commit/43104cbff30ae006e907d8ee0ec15c4949d0eef6)が追加されました。鍵と署名は固定長で、検証者は空のコンテキストを用いて、イベントIDの32バイトの生のダイジェストに対する署名を検証します。フォールバックアルゴリズムは認められません。提案されたアイデンティティには[NIP-19](/ja/topics/nip-19/)のbech32エンコーディングがなく、新しい署名によって[NIP-44](/ja/topics/nip-44/)の暗号化ペイロードや[NIP-59](/ja/topics/nip-59/)のgift wrapがポスト量子安全になるわけではありません。

### 署名付き前提条件の提案でイベント置換の消失を防止 {#a-proposed-signed-precondition-prevents-lost-event-replacements}

Buzzのオープンなプルリクエストは、置換可能イベントおよびアドレス指定可能イベント向けに[プロジェクト独自のNIP-CS署名付き前提条件を提案](https://github.com/block/buzz/pull/8835)しており、これは公式のNIPではありません。署名付きタグは現在のヘッドIDまたは`none`を指定し、リレーはそれを座標ロックの下でアトミックにチェックします。古い書き込みはfalseのOKまたはHTTP 409で拒否され、何も保存されません。タグのない書き込みは従来どおり動作し、このタグはリレー間でのcompare-and-swapを保証しません。

## NIPディープダイブ: NIP-31とNIP-73 {#nip-deep-dive-nip-31-and-nip-73}

クライアントは、ネイティブには理解できないコンテンツによく出会います。[NIP-31: Dealing with Unknown Event Kinds](/ja/topics/nip-31/)は見慣れないイベントkindに読みやすいラベルを付けます。[NIP-73: External Content IDs](/ja/topics/nip-73/)は、書籍やウェブページなどNostrの外にある対象に名前を付けます。この2つの規約は、互いに独立した既存の仕様です([NIP-31本文](https://github.com/nostr-protocol/nips/blob/master/31.md)、[NIP-73本文](https://github.com/nostr-protocol/nips/blob/master/73.md))。

### NIP-31は非推奨とされている {#nip-31-is-marked-unrecommended}

現在の[NIP-31本文](https://github.com/nostr-protocol/nips/blob/master/31.md)は冒頭に警告を掲げ、「不必要に肥大化している」("unnecessarily bloated")として`unrecommended`と位置付けています。ステータス行はdraft、unrecommended、optionalです。この規約を使ったイベントはすでにリレー上に存在します。そのため以下の仕組みは、クライアントがそれらをどう読むかを説明するものであり、新しいプロトコルに推奨するものではありません。

### altタグが運ぶもの {#what-an-alt-tag-carries}

[仕様](https://github.com/nostr-protocol/nips/blob/master/31.md)では、テキストとして読まれることを意図しないカスタムkindの作成者は、短いプレーンテキストの要約を入れた`alt`タグを追加します。kind 1中心のクライアントが他のkindを要求することは想定されていません。それでもユーザーはノートからそうしたイベントを参照でき、その際に要約が文脈を補います。ラベルで投票したり、ウォレットのリクエストに応じたりすることはできません。より豊かなやり取りについては、仕様は[NIP-89: Recommended Application Handlers](/ja/topics/nip-89/)を参照するよう示しています。

`alt`はタグなので、[NIP-01](/ja/topics/nip-01/): [Basic protocol flow description](https://github.com/nostr-protocol/nips/blob/master/01.md)のイベントIDと署名の対象に含まれます。有効な署名が認証するのは、作成者が管理する要約です。作成者がそのラベルを公開したことは示しますが、内容の正確さは示さないため、誤解を招く要約もありえます。タグは公開されるため、暗号化されたコンテンツを持つイベントに`alt`を付けると要約が露出し、コンテンツが隠している内容が明らかになるおそれがあります。これらの性質はNIP-31の規範的な本文ではなく、[NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)のエンベロープに由来します。また、トップレベルの`alt`タグは`imeta`内にある画像説明用の`alt`フィールドとは別物であり、レンダラーはこれらを個別に解析します。

### 2つのクライアントによるaltの読み方 {#how-two-clients-read-alt}

noStrudelの[コミット7c68acf時点の不明イベントカード](https://github.com/hzrd149/nostrudel/blob/7c68acf4f148260d8e59879975f71c4f1bd004df/src/components/embed-event/card/embedded-unknown.tsx)では、最初の`alt`タグがトリムされてメインのラベルになり、任意で`Using <client>`の行が付きます。値がない場合や空白の場合は`Unknown event (kind ...)`となり、最大3行のコンテンツがそれとは独立して表示されます。同じコンポーネントはNIP-89のハンドラーテンプレートを通じて`client`タグを解決します。共有可能なアドレスがあればOpenを、有効なハンドラーリンクが解決されれば`Open in <client>`を表示します。説明とアプリへの振り分けは別々のコントロールです。

Amethystの[コミット553f761時点のUnknownEventDigest.kt](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commons/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/rendering/unknown/UnknownEventDigest.kt#L168-L170)は、散文と分類したコンテンツを優先し、それがなければ`alt`にフォールバックします。パーサーは値をトリムし、最初の空白でない`alt`を採用します。そのため最初の`alt`が空白のイベントには、noStrudelとは異なるラベルが付く可能性があります。どちらの説明もそれぞれのコミット時点のソースに基づくもので、リリースでの動作を確認したものではありません。

### 例: altラベル付きの投票 {#example-a-poll-with-an-alt-label}

以下のkind 1068の投票はwss://relay.damus.ioから取得したもので、IDとBIP340署名は[NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)の規則に従って正しく検証されます。汎用レンダラーは2言語で書かれた`alt`テキストを表示でき、投票に対応したクライアントは`option`タグと`polltype`タグを読み取ります。

```json
{
  "kind": 1068,
  "id": "7d1df3922833b47645922de43c2edd83e928a0ad083cee592beeee2b262bb743",
  "pubkey": "5f6dc275f3f9f8752d010a110c226148a9ba3399c5b63a0f469ee93b1394a53e",
  "created_at": 1793626294,
  "tags": [
    [
      "option",
      "z25mgp",
      "Windows"
    ],
    [
      "option",
      "ncddq0",
      "macOS"
    ],
    [
      "option",
      "4wta6q",
      "Linux"
    ],
    [
      "option",
      "p9ykti",
      "UNIX or FreeBSD/NetBSD/OpenBSD"
    ],
    [
      "polltype",
      "singlechoice"
    ],
    [
      "alt",
      "Poll: Which one do you usually use?\n普段どれを使っていますか？"
    ],
    [
      "client",
      "Ditto",
      "31990:781a1527055f74c1f70230f10384609b34548f8ab6a0a6caa74025827f9fdae5:ditto"
    ]
  ],
  "content": "Which one do you usually use?\n普段どれを使っていますか？",
  "sig": "f1378a723c65e83bd3105b593f10767903bde993788cfaf625583466fca21f1ef2be945bb2ca526aa9e898c93d5f1677a2f5ceaf70cb3a59c99f97eb179658fa"
}
```

### NIP-73の対象とファミリー {#nip-73-subjects-and-families}

[NIP-73仕様](https://github.com/nostr-protocol/nips/blob/master/73.md)(draft、optional、unrecommendedフラグなし)は、外部の対象を`i`タグに、その識別子ファミリーを`k`タグに入れます。これによりクライアントは、特定の1つの対象もファミリー全体もクエリできます。書籍なら`["i", "isbn:9780765382030"]`と`["k", "isbn"]`を使い、ウェブページならそのURLを使って`k`を`web`にします。NIP-73はイベントkindを定義しておらず、これらのタグは他のイベントに含められます。

### 正規化とURLヒント {#normalization-and-url-hints}

照合は文字列が完全に一致するかどうかで決まるため、[仕様](https://github.com/nostr-protocol/nips/blob/master/73.md)はファミリーごとに形式を定めています。URLはフラグメントを除いて正規化し、ISBNはハイフンなし、geohashは小文字、ISO 3166コードは大文字です。任意の3番目の配列要素には、その識別子を独自に扱わないクライアント向けのURLヒントを入れます。このヒントは作成者が選ぶもので、アイデンティティの一部ではありません。所有権を証明するものでも、正規のサイトを示すものでもありません。

### 共有された識別子が証明しないこと {#what-a-shared-identifier-does-not-prove}

[NIP-73](https://github.com/nostr-protocol/nips/blob/master/73.md)では、同一の識別子は会話を結び付けるだけで、それ以外は何も確立しません。署名付きコメントからわかるのはコメント投稿者です。書籍、サイト、ポッドキャストの発行者を認証するものでも、誰がそれらを管理しているかを示すものでもありません。別名、版ごとに異なるISBN、正規化の結果が異なるURLによって、1つの対象が複数のスレッドに分かれることがあります。文脈にも注意が必要です。[NIP-22](/ja/topics/nip-22/): [Comment](https://github.com/nostr-protocol/nips/blob/master/22.md)はルートのスコープに大文字の`I`/`K`を、親に小文字の`i`/`k`を使います。[NIP-39: External Identities in Profiles](/ja/topics/nip-39/)はプロフィールのアイデンティティに`i`を使います。そのため、すべての`i`タグがNIP-73の対象とは限りません。

### パーサーとレンダラーのコードにおけるNIP-73 {#nip-73-in-parser-and-renderer-code}

rust-nostrの[コミット4c8099a時点のnip73.rs](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs)は、既知のプレフィックスを型付きの`ExternalContentId`に解析し、任意のヒントを型付きURLに変換します。3番目のタグ要素を出力するのはヒントがある場合だけです。テストではハイフン付きのISBNがそのまま残ります。パーサーはプレフィックスを取り除いた残りを格納するだけで、仕様の正規化を適用しません。つまり型付きの解析は、正規の文字列を保証しません。チェーンIDはファミリーから分離され、`ethereum:100:tx:<hash>`は`ethereum:tx`に対応付けられます。このリビジョンには、国を表す`iso3166`のバリアントがありません。

Amethystの[コミット553f761時点のDisplayExternalId.kt](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt)は、geohashとハッシュタグの識別子をそれぞれ専用の表示に振り分けます。URL識別子にも専用の表示があり、それ以外のサポート対象の型は汎用のスコープチップで表示されます。URLを開くと、そのページに対するアプリ独自のスレッド画面に移動します。プレビューが無効なら、通常の描画ではプレーンなリンクチップが表示され、プレビューは要求されません。プレビューが有効なら、未取得のプレビューを取得する際に対象サイトへアクセスする可能性があります。プレビューをオフにすれば、通常の描画ではそのリクエストを避けられます。どちらのファイルも、リリースでの動作を裏付けるものではありません。

### 例: ウェブページへのコメント {#example-a-comment-on-a-webpage}

wss://nos.lolから取得したこのkind 1111のコメントは、同じ公開RedditスレッドのURLを`I`/`K`と`i`/`k`の両方のペアに入れています。ファミリーは、[NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md)とNIP-73に従って`web`です。IDと署名は正しく検証されます。これでコメントの作成者は特定できますが、リンク先のページについては何もわかりません。

```json
{
  "kind": 1111,
  "id": "e4229e38d93fad5d612ae21c401573bf8e87f0462dc2bd653804a252f98a238a",
  "pubkey": "ce5b8496c144a9dcd4990df6e265d9b60a21cde2515f3b206dc67b1c343790a9",
  "created_at": 1793590574,
  "tags": [
    [
      "I",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "K",
      "web"
    ],
    [
      "i",
      "https://www.reddit.com/r/writinghelp/comments/1thd194/what_tools_and_systems_do_you_use_for_tracking"
    ],
    [
      "k",
      "web"
    ],
    [
      "client",
      "LayerTake"
    ],
    [
      "L",
      "layertake"
    ],
    [
      "l",
      "pin",
      "layertake"
    ],
    [
      "anchor",
      "{\"type\":\"text\",\"exact\":\"tools and systems\",\"prefix\":\"help • 6mo ago u/TheFarSea What \",\"suffix\":\" do you use for tracking and org\"}"
    ]
  ],
  "content": "Like this. I'm making this Public but could be just for me or friends/groups.",
  "sig": "a979389480d6ca919e4ab7b1ba92e532bf281be45c5df222e17d7d4ca62ef07d52c1004c0ce88620663dfac012b306154cfd73b858225764c701c40e3d9b7dfe"
}
```
