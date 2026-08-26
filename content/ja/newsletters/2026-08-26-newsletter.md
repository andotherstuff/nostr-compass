---
title: "Nostr Compass #37"
date: 2026-08-26
publishDate: 2026-08-26
translationOf: /en/newsletters/2026-08-26-newsletter.md
translationDate: 2026-08-26
draft: false
type: newsletters
description: "ShopstrとRoutstrが保存された秘密情報とrelay由来のディスカバリを強化し、PostrとInfansが登場、pakstrがZapstore公開を明示化し、「Nostr の 6 年間の 8 月」が静かな protocol の中核から実装クライアントまでコメントスレッドの流れをたどります。"
---

[Nostr Compass](https://nostrcompass.org)へようこそ。Nostrの週刊ガイドです。

**今週:** [Shopstr](https://github.com/shopstr-eng/shopstr)がリモートsignerとwalletの秘密情報をブラウザストレージの外に保ち、[Routstr SDK](https://github.com/Routstr/routstr-sdk)がrelay由来のプロバイダディスカバリを検証、[Postr](https://gitworkshop.dev/npub1qwkd5wzftcxquuhtkcg0xn9ed7evksluuppf7qdmdh34ywe9uncs5uqfvl/relay.ngit.dev/postr)が小さなAndroid投稿アプリとして登場、[Infans](https://github.com/TurkeyNostr/infans)が育児記録と共同養育者間の同期を暗号化、[walls.rip](https://walls.rip/comms)がPGP暗号化チャットを公開Nostr relay経由で運び、[pakstr](https://git.nostrdev.com/stuff/pakstr)がZapstore公開を明示化します。[nostr-tools](https://github.com/nbd-wtf/nostr-tools)はgift wrapのrumorをそのsealに結び付けます。リリースはsubscriptionの分離、プロフィールステータス、relay単位の退出マーカーを扱います。protocol関連の動きはコメントスレッドの実装展開、wallet connectの手数料上限と支払い照会のドラフト、napplet向けディスプレイ要求、同一アカウントからの実験的な参加登録に及びます。今号は[Nostr の 6 年間の 8 月](#nostr-の-6-年間の-8-月)で締めくくります。

## トップストーリー

### Postrが小さなAndroid投稿アプリとして登場

[Postr](https://gitworkshop.dev/npub1qwkd5wzftcxquuhtkcg0xn9ed7evksluuppf7qdmdh34ywe9uncs5uqfvl/relay.ngit.dev/postr)は、kind 1ノート向けに意図的に小さく作られたAndroid投稿アプリです。秘密鍵の保管は[Amber](https://github.com/greenart7c3/Amber)、すなわちAndroidの[NIP-55](/ja/topics/nip-55/)（ローカルsigner）およびNIP-46 signerに残ります。バージョン1.0.0は、接続断やプロセス終了に耐える永続的なoutbox、アカウントごとの非公開下書き、検証済みハッシュとスコープ付きアップロード認可を備えた[Blossom](/ja/topics/blossom/)添付を搭載します。

投稿が成功と見なされるのは、Postrが同一の署名済みイベントを読み戻し、その署名を確認した後です。再試行は同じevent idを保ちます。公開には著者の[NIP-65](/ja/topics/nip-65/)（relayリスト）書き込みrelayと暗号化されたブートストラップrelay、またはアカウントごとの独自リストを使います。署名済みの[NIP-34](/ja/topics/nip-34/)（git over Nostr）[リポジトリ告知](https://njump.me/nevent1qqsqxdwxa8k5e0ftf6j6q5ucs3u94ezgjqmyzwznqt99pyxxw23c74spz3mhxue69uhhyetvv9ujumn8d96zuer9wcx4nr0m)と対応する[kind 0プロジェクトプロフィール](https://njump.me/nevent1qqs24gy97frkjkma8ys3rwc3jj8f0qrrmsxjwe39jxrhuemztrygr8qpz3mhxue69uhhyetvv9ujumn8d96zuer9wcspcsat)は`relay.ngit.dev`で公開されます。フィード、アナリティクス、広告、鍵の保管はアプリの外に置かれます。

### InfansがNostr上で育児記録と共同養育者間の同期を暗号化

共同養育者は授乳、睡眠、成長の記録を自分の端末に保ちながら、育児データ事業者を介さずに共有できます。[Infans](https://github.com/TurkeyNostr/infans)はAndroidの育児記録アプリで、ローカルのRoomデータベースを唯一の正とみなし、バックアップとパートナー同期のために暗号化されたkind 30078の[NIP-78](/ja/topics/nip-78/)（アプリケーション固有データ）イベントを公開します。リポジトリはローカルの暗号方式を[NIP-44](/ja/topics/nip-44/)（ペイロード暗号化）と表記していますが、実装はAES-256-GCMを使っており、NIP-44 v2はChaCha20とHMAC-SHA256を要求します。したがってローカルモードのペイロードをNIP-44互換として示すべきではありません。

[パートナー同期](https://github.com/TurkeyNostr/infans/blob/main/README.md)はd-tag `baby-tracker-sync`を使い、自己バックアップは`baby-tracker-backup`を使います。非同期のメモはパートナー向けペイロードの内側を通ります。文書化されたAmber [NIP-55](/ja/topics/nip-55/)（ローカルsigner）経路は署名と暗号化をsignerに委譲しますが、リポジトリはすべてのバックアップおよびパートナー同期経路がNIP-44 v2の暗号文を生成することを示す相互運用テストを提供していません。リポジトリは医療機器としての主張も第三者によるセキュリティレビューも提示していません。

### walls.ripのGhost Chatが公開Nostr relayにPGP暗号化チャットを持ち込む

[walls.rip](https://walls.rip/comms)は匿名コミュニケーションのツール群で、そのGhost Chatモードはブラウザ内でOpenPGP identityを作成または取り込みます。[オープンソースのクライアント](https://github.com/KYC-rip/walls-rip/tree/cf40bda32df5f106007631b21afc3cd193ac0cda/src/components/ghostChat)は各メッセージを受信者のPGP公開鍵で暗号化します。読める会話は端末上のローカルセッションストレージに留まり、アプリにはチャットアカウントも中央のメッセージデータベースもありません。

トランスポートは本物のNostrですが、意図的にアプリ固有です。Ghost Chatは[armored暗号文をkind 1イベントとして公開](https://github.com/KYC-rip/walls-rip/blob/cf40bda32df5f106007631b21afc3cd193ac0cda/src/utils/nostrService.ts)し、5つの既定relayへ送り、各イベントに受信者のPGPフィンガープリントから導かれた安定したルームtagを付けます。これは開発者にとって、relayを検閲耐性のあるメッセージトランスポートとして使う具体例になると同時に、分散配信だけではメタデータが守られず、NIP-17ダイレクトメッセージとの相互運用性も得られない理由を示しています。

### pakstr 0.13.0から0.15.0がZapstore公開を明示化

7月の[0.3.1におけるパッケージングとAmber対応](/ja/newsletters/2026-07-29-newsletter/#pakstr-031)を経て、[pakstr](https://git.nostrdev.com/stuff/pakstr)はwebアセットのフォルダを署名済みAndroid APKに変換し、Nostr鍵でZapstoreへ公開するCLIです。[0.13.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.0)はリリースの自動バージョニングを追加します。0.13.1から0.13.3の後続版はBlossom公開を修復します。[認可がbase64urlを使うようになり](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.1)、[アップロードがContent-Digestを持ち](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.2)、[Zapstoreのapplicationイベントがアップロードより前に公開されます](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.13.3)。

[0.14.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.14.0)は公開処理を進める前にZapstoreの発行者を検証します。[0.15.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.15.0)は掲載メタデータをkind 32267のapplicationイベントに書き込み、リリースノートをkind 30063のreleaseイベントの`content`に入れます。これによりパッケージ化したアプリのZapstore掲載は、別途の手作業なしに名称、概要、ノートを持てます。

### Heterodyneが可搬なpersonaと暗号化されたソーシャル通信を仕様化

[Heterodyne](https://radicle.network/nodes/iris.radicle.network/rad%3Az2zX5XvPiggGJvCn8DPkp1hRNGA5)は、可搬なpersona、認証付き通信、自己端末の制御、ソーシャル交流のための仕様先行のprotocolファミリーです。[現在のREADME](https://radicle.network/nodes/iris.radicle.network/rad%3Az2zX5XvPiggGJvCn8DPkp1hRNGA5)は既存の4層を組み合わせます。署名済みNostrイベント、永続保存としての[Radicle](https://radicle.xyz)（ピアツーピアgit）、暗号化された個別・グループ会話のための[Marmot](/ja/topics/marmot/)（Nostr上のMLSグループメッセージング）、そしてidentityのローテーションのための[KERI](https://arxiv.org/abs/1907.02143)（Key Event Receipt Infrastructure）key-event logです。personaはコールドルートのNostr npubと承認済みKERI logの組み合わせとして記述され、日常の署名はローテーションするエポック鍵を使い、Radicleノードのidentityは二重証明で委任されます。

ファミリーはこの作業を[独立にバージョン管理される4つの0.xドラフト](https://radicle.network/nodes/iris.radicle.network/rad%3Az2zX5XvPiggGJvCn8DPkp1hRNGA5)に分けています。Coreはidentity、key-event logの検証、正規化されたNostrバイト列、Radicleリポジトリ基盤を担い、CommsはNostrネイティブなエンベロープ、プライバシー階層、公開、Marmot会話を担い、Socialは公開フォロー、インタラクション、リストを担います。自己端末の登録と権限付与を担うControlは未完成で、実現済みとは主張できません。これらの文書は1.0前に壊れる可能性のあるドラフトであり、今号はHeterodyneクライアントのリリースが出る前の段階でこのファミリーを紹介しています。

## リリース

### Nostr Java v2.0.8: subscriptionの分離と可搬なNIP-44

5件のイベントを持つrelayに対するgift wrapのクエリが0件、2件、6件をばらばらに返していました。原因は[Nostr Java](https://github.com/tcheeric/nostr-java)、relayとの通信とNostrペイロードの暗号化を行うJavaライブラリが、受信したすべてのフレームを接続上のすべてのlistenerに配っていたことです。[バージョン2.0.8](https://github.com/tcheeric/nostr-java/releases/tag/v2.0.8)は`EVENT`、`EOSE`、`CLOSED`をそれらのフレームが指すsubscriptionへルーティングするので、あるクエリの保存済みイベント終了シグナルが別のクエリを閉じることはなくなりました。`NOTICE`、`OK`、`AUTH`のような接続スコープのフレームは引き続きすべてのlistenerに届きます。

同じ[リリース](https://github.com/tcheeric/nostr-java/releases/tag/v2.0.8)の[NIP-44](/ja/topics/nip-44/)（ペイロード暗号化）は、プロセスに登録されたJCE providerを必要としなくなりました。以前は当該JVMで鍵を生成した後でしか暗号化が動かず、その副作用としてBouncyCastleが登録されていました。また"BC"という名前のproviderを追加しても無効なAndroidでは失敗していました。両方のcipher経路はBouncyCastleの軽量ChaCha20エンジンを使うようになり、鍵生成がプロセス全体のJCE状態を変えることもなくなりました。providerの登録をライブラリに任せていた呼び出し側は自分で登録する必要があります。これが閉じるissueは[NIP-44のJCE provider依存](https://github.com/tcheeric/nostr-java/issues/537)です。

### NoorNote v1.3.6: プロフィールステータスとclassified listing

[NoorNote](https://github.com/77elements/noornote)はデスクトップ、web、Android向けのNostrクライアントです。[1.3.4が暗号化されたコミュニティ参加を追加](/ja/newsletters/2026-08-19-newsletter/#noornote-134-joining-encrypted-communities-from-an-invite-link)した1週間後、[バージョン1.3.6](https://github.com/77elements/noornote/releases/tag/v1.3.6)はプロフィールの[NIP-05](/ja/topics/nip-05/)（ドメイン検証済み）名の下に[NIP-38](/ja/topics/nip-38/)（ユーザーステータス）を表示します。これは1行の一般ステータスまたは音楽ステータスを持つ、任意で期限切れになるkind `30315`のaddressableイベントです。その行をクリックすると閲覧者自身のステータスが設定されます。

[NIP-99](/ja/topics/nip-99/)（kind `30402`のマーケットプレイス出品）の[classified listing](https://github.com/77elements/noornote/releases/tag/v1.3.6)がアプリ全体で描画されるようになったため、マーケットプレイスのアドオンは売買のときだけ必要になりました。プロフィール上の非公開のpetnameメモも警告色のオレンジで表示され、塗りつぶしのメモアイコンとオレンジのアバターリングが付きます。

### nostrord v2.9.0: relay単位のグループ状態とメディア

あるホストで[NIP-29](/ja/topics/nip-29/)（relay管理グループ）のグループを退出すると、以前は他のすべてのrelayで同じグループidが抑止されていました。[nostrord](https://github.com/nostrord/nostrord)、relayホスト型コミュニティ向けのクロスプラットフォームクライアントが、退出と削除のマーカーを素のidでキー付けしていたためです。[relay単位にスコープされた退出・削除マーカー](https://github.com/nostrord/nostrord/pull/253)は、その抑止を生成したホストに留めるので、2つのrelayでidを共有するグループが対で退出・破棄されることはなくなりました。すでにメンバーであるためにrelayが拒否する参加は成功として扱われ、ローカルのマーカーを消去します。これは以前は吸収状態でした。自己修復が一方のスロットを消す一方で、コールドスタートがもう一方を復元していたのです。

[バージョン2.9.0](https://github.com/nostrord/nostrord/releases/tag/v2.9.0)は、他のクライアントが`![alt](url)`と書く[markdownの画像埋め込み](https://github.com/nostrord/nostrord/pull/254)も描画するようになり、すでに検出済みのURLの周りにmarkdownの記号を表示しなくなりました。ダイレクトメッセージは[NIP-17](/ja/topics/nip-17/)（gift wrapされた非公開DM）の[kind `15`ファイルrumor](https://github.com/nostrord/nostrord/pull/275)に対応したので、Jumbleから送られた暗号化添付がダウンロード、復号、表示され、送信する添付はアップロード前に暗号化されます。このタグは[先週取り上げたNIP-4e暗号鍵の作業](/ja/newsletters/2026-08-19-newsletter/#nostrord-implements-an-unmerged-encryption-key-proposal)を実際に出荷します。提案は未マージのままで、nostrordはドラフトと異なる部分では実運用のJumbleの挙動に従うと述べています。

## 未リリースの変更

### Shopstrがリモートsignerとwalletの秘密情報をブラウザストレージの外に保つ

[Shopstr](https://github.com/shopstr-eng/shopstr)は[NIP-99](/ja/topics/nip-99/) classified listing向けのwebマーケットプレイスです。[先月の支払い整合性の作業](/ja/newsletters/2026-07-22-newsletter/#shopstr-binds-payment-validation-to-signed-receipts-and-server-side-prices)に続き、[シリアライズしたbunker signerの秘密情報を`localStorage`に書き込むのをやめました](https://github.com/shopstr-eng/shopstr/pull/437)。[NIP-46](/ja/topics/nip-46/)（リモート署名）のbunkerペイロードには稼働中の`bunker://` URLと生成されたアプリ秘密鍵が含まれていたため、Shopstrのoriginで動く任意のスクリプトがリモート署名セッションを再開できました。bunkerデータは現在のセッションのあいだメモリ上に留まり、残っていたbunkerペイロードは見つかった時点で削除され、bunker以外のsignerタイプは以前の保存挙動を保ちます。

対応する[NWCの変更](https://github.com/shopstr-eng/shopstr/pull/436)は[NIP-47](/ja/topics/nip-47/)（wallet connect）の資格情報に同じ処理を行います。Shopstrはwallet操作に使う秘密を含む`nostr+walletconnect://`文字列全体を通常のブラウザデータとして保存し、決済時に再利用していました。接続文字列とwalletメタデータは現在メモリ上に留まり、古い保存済みコピーはローカルデータの読み取り時に削除されます。アクティブなセッション中にすでにShopstrのoriginで動いているスクリプトは、メモリ上のそれらの値を依然として見ることができます。

### Routstrがrelay由来のプロバイダディスカバリを検証

以前は単一の悪意あるrelayが、Routstrクライアントが信頼する推論プロバイダを決められました。[Routstr SDK](https://github.com/Routstr/routstr-sdk)は、Nostr上でAIプロバイダを見つけてCashuで支払うマーケットプレイスRoutstrの背後にあるTypeScriptライブラリです。[今週のディスカバリ修正](https://github.com/Routstr/routstr-sdk/pull/47)は、relayが届けたすべてのプロバイダ告知、モデル一覧、レビュー（kind 38421、38423、38425）を利用側が見る前に検証するので、信頼済みのpubkeyを名乗りながら不正な署名を持つレビューがランキングに入ることはなくなりました。

[遠い未来のタイムスタンプ](https://github.com/Routstr/routstr-sdk/pull/47)は「最新レビュー」の選択前に破棄されます。ローカル時計より15分以上先のイベントはライブ経路と永続ストアの読み取り時に除去されるので、偽造された`created_at`が再起動をまたいで正しく署名されたレビューを上回ることはできません。信頼できるレビューが得られない場合、レビューのゲートはfail-closedとなり、レビューが届くまで未レビューのプロバイダを支払いランキングから除外します。運用者は手動でプロバイダを有効化することもできます。

### nostr-toolsがgift wrapのrumorをそのsealに結び付ける

[NIP-59](/ja/topics/nip-59/)（gift wrap）イベントのunwrapは、以前はwrapを復号し、sealを復号して、sealが誰から来たかを確認せずに内側のrumorを返していました。[nostr-tools](https://github.com/nbd-wtf/nostr-tools)はNostr protocolのヘルパーを集めたJavaScriptライブラリです。[今週のunwrap修正](https://github.com/nbd-wtf/nostr-tools/pull/545)は、wrapがkind 1059であること、sealが有効な署名を持つkind 13であること、そしてrumorの`pubkey`がsealの`pubkey`と一致することを要求します。sealの復号自体が`seal.pubkey`の管理を証明しています。最後の確認がなければ、誰でも他人を著者と名乗るrumorをsealでき、クライアントにそのメッセージをその被害者に帰属させられてしまいます。

[NIP-17](/ja/topics/nip-17/)（gift wrapされた非公開DM）は同じunwrap経路を使うため、この結び付けは非公開DMにも適用されます。[バッチunwrap](https://github.com/nbd-wtf/nostr-tools/pull/545)は、これらの確認に失敗したwrapで例外を投げるのではなくスキップするようになりました。gift wrapは未承諾で届くものであり、1件の敵対的なイベントがrelayクエリの残りを捨ててしまうからです。

### Havenが署名付きrelay管理とローカルのノートブラウザを追加

[Haven](https://github.com/barrydeen/haven)はセルフホストのNostr relayかつBlossomメディアサーバーです。新たにマージされた[管理コンソール](https://github.com/barrydeen/haven/pull/135)は各relayエンドポイントでNIP-86の管理呼び出しを公開し、すべてのリクエストは設定されたオーナーのNIP-98イベントで認証されます。運用者はrelayに署名鍵を渡すことなく、BAN、許可リスト、kindのルール、relay名、保存メディアを管理できます。読み取り専用のノートブラウザは暗号化されたkindを不透明なまま保ち、リモートメディアはクリック後にのみ読み込むので、運用者のIPアドレスを外部ホストに漏らす自動リクエストを避けられます。

同じ[Havenの変更](https://github.com/barrydeen/haven/pull/135)は永続的なトラフィックグラフを追加し、既定のLMDBで保存イベントの数え上げが無限ループしてCPUコアを占有し、その後の統計呼び出しを止めてしまう不具合を修正します。Havenは終了が保証される場合はバックエンドのカウンタを使い、それ以外では上限付きのイベント走査を使います。プロジェクトはイベントのページング、削除、メトリクスの永続化、オーナー確認、URLに束縛されたリクエスト署名について最初の23件のテストを追加しました。

### AmethystがBlossom認可を画像読み込みスレッドから外す

[Amethyst](https://github.com/vitorpamplona/amethyst)、AndroidのNostrクライアントは、[OkHttpのdispatcherスレッド上でBlossom読み取り認可を待つのをやめました](https://github.com/vitorpamplona/amethyst/pull/3991)。interceptorはネットワークスレッドから離れて署名を開始し、画像fetcherはホストごとに共有される1つの署名を待って保護されたblobリクエストを再試行します。これにより、signerが応答している間に認可付き画像の集中が各ホストの接続スロットを埋め尽くすことはなくなりました。

同じ[Amethystのパッチ](https://github.com/vitorpamplona/amethyst/pull/3991)はトークンのエンコードをBUD-11に合わせます。パディングなしのBase64url、`server`スコープ、blob固有の`x` tagなしとし、1つのトークンが同一ホスト上の複数のblobを対象にできます。新しい並行性テストはキャッシュ、期限切れ、署名付き再試行、1つの署名を共有する16の同時呼び出しを検証します。

## プロトコルと仕様作業

### NIP

SnortとDittoは通常のテキスト返信に[NIP-22](/ja/topics/nip-22/)（コメントスレッド）を使うようになり、互換経路を保ちながらkind 1111に収束しています。これはprotocol全体で単一の返信kindを定めるものではありません。[6月の修正](/ja/newsletters/2026-06-24-newsletter/#kind-1111-as-reply-to-kind-1-notes)がkind 1ノートに対してNIP-22を使う禁止を取り除いた後、[NIP-30](/ja/topics/nip-30/)（カスタム絵文字）への[マージ済みの追記](https://github.com/nostr-protocol/nips/pull/2448)がkind `1111`を`emoji` tagを持てるイベントの一覧に加え、`content`内のショートコードがそのtagで解決されるようになりました。[Snort](https://github.com/v0l/snort)、webのNostrクライアントは、[すべての返信をkind 1111として書き](https://github.com/v0l/snort/commit/420ed60e2ff43bd373f2583e171a77002ec9f3a0)、大文字の`E`/`A` root scope tagを通じてそのコメントを読み込み、古いノートに対しては任意で[NIP-10](/ja/topics/nip-10/)（kind 1返信tag）経路も受け入れます。[Ditto](https://github.com/soapbox-pub/ditto)、MastodonサーバーとNostr relayを兼ねる実装は、[すべての返信をNIP-22コメントとして公開](https://github.com/soapbox-pub/ditto/commit/8a0ffc6e3a5d9202ffc452fa0de8ae33b5883384)し、テキストはkind `1111`、音声はkind `1244`とし、既存のkind 1返信も引き続き描画します。NIP-10しか理解しないクライアントは新しい形式を見られません。トップレベルの投稿はkind 1のままです。

[NIP-47](/ja/topics/nip-47/)（Nostr Wallet Connect）の`pay_invoice`リクエストには、クライアントがルーティング手数料の上限を指定する標準的な手段が今のところありません。[手数料上限のオープンな提案](https://github.com/nostr-protocol/nips/pull/2444)は、`pay_invoice`にミリサトシ単位の任意パラメータ`max_fee`を追加します。この予算を尊重するwalletは、ルーティング費用が`amount + max_fee`を超える支払いを送ってはならず（MUST NOT）、引き落としも支払い試行もない状態として定義される`FEE_LIMIT_EXCEEDED`を返さなければなりません（MUST）。対応する実装はクライアントが照合できるよう応答に`fees_paid`を含めなければなりません（MUST）。手数料上限に未対応の実装は未知のパラメータを無視し、クライアントは`fees_paid`フィールドの欠落を上限が適用されていない可能性のしるしとして扱うべきです。この変更はイベントkindを追加せず、マージされるまで提案のままです。

[NIP-32の言語ラベルに関するオープンな提案](https://github.com/nostr-protocol/nips/pull/2451)は、著者が宣言するテキスト言語のために`["l", "<BCP-47>", "lang"]`を標準化します。1文字の`l` tagはすでにrelayでインデックス可能なので、クライアントはrelayの更新やダウンロード後の当てにならない言語判定なしに`{"#l":["ja"]}`で日本語フィードを要求できます。ドラフトはNIP-66のrelayレポート、NIP-68の画像メタデータ、NIP-71の音声トラックにある言語の例も同じ名前空間へ移します。ラベルは検証されていない著者の主張のままで、この変更はマージされていません。

### Nostr Wallet Connect

タイムアウト、再接続、通知の取りこぼしの後、wallet connectクライアントは、どのBitcoin支払いprotocolがそれを作ったか知らないまま1件の支払い記録を問い合わせる手段を必要とします。[NWC拡張リポジトリ](https://github.com/nostr-wallet-connect/nwc)の[支払い照会のオープンなドラフト](https://github.com/nostr-wallet-connect/nwc/pull/5)は、NIP-47コアと並ぶ任意のNWC-09 `lookup_payment`を定義します。リクエストはちょうど1つのセレクタを使います。walletスコープで安定した`transaction_id`、`lookup_invoice`がすでに使うBOLT11互換の`payment_hash`および/または`invoice`フィールド、あるいは`payment_type`と別の拡張が定義する型付き`lookup`オブジェクトです。成功した結果は共通のエンベロープ（`transaction_id`、`type`、`state`、`payment_type`、msat単位の`amount`、タイムスタンプ、任意の`fees_paid`と`metadata`、および判別付き`details`オブジェクト）を返し、その接続から見える記録ちょうど1件に解決しなければなりません（MUST）。walletはアクセスできない記録が存在するかどうかを明かしてはならず（MUST NOT）、複数の可視記録に一致するセレクタは`MULTIPLE_MATCHES`を返します。状態は`pending`、`accepted`、`settled`、`failed`、`expired`、`canceled`です。同じ提案はそのエンベロープを再利用するNWC-12のBOLT12 offerと支払い詳細も追加します。どちらの文書もまだドラフトです。

### NAP

[オープンなNAP-DISPLAYのドラフト](https://github.com/napplet/naps/pull/97)は、nappletがホストに対して使用を許されたピクセルディスプレイを問い合わせられるようにします。これは別途進む[未マージのNIP-5D web appletsの提案](/ja/topics/nip-5d/)の上に築かれており、その提案はNewsletter #17で紹介され、マージ済みNIPの集合の外にとどまっています。ドラフトは`display.list`を定義し、論理的な幅と高さ、実行時に選ばれる種別（`lcd`、`eink`、`led-matrix`、`other`）を伴う不透明で安定した識別子を返します。また`display.push`は、座標指定された3バイトのsRGBピクセルの空でないバッチを送ります。実行時ディスカバリは論理RGBをネイティブの色深度、向き、リフレッシュへ対応付け、更新の回転、並べ替え、量子化、ディザリング、統合を行ってもよい（MAY）とされます。shellのポリシーはnappletが列挙または書き込みできるディスプレイを制御し、バッチを拒否、レート制限、上限設定してもよい（MAY）。ピクセルを適用する前にランタイムはバッチ全体を検証するので、失敗したpushは端末上で何も変えません。成功はバッチが受理されたことを意味し、ハードウェアのリフレッシュが完了したことは意味しません。

### Marmot

[Marmotのオープンな実験](https://github.com/marmot-protocol/marmot/pull/417)は、同一アカウントからの参加登録について、取り下げられたExternal Commitのドラフトを上限付きのCommit形式に置き換えます。[Marmot](/ja/topics/marmot/)、Nostr上のMLSグループメッセージングprotocolは、そのドラフトでデータなしコンポーネント`0x800d`（`marmot.same-account-membership.v1`）をネゴシエート済みの挙動マーカーとして割り当てます。それが必須である間、現在のleafはインラインの同一アカウントAddをちょうど1つ、またはインラインの兄弟Removeを1つから4つ作成でき、いずれも通常のUpdatePathと通常の収束優先度を持ち、すべてのCommitは1アカウントあたり最大5つの現在leafを残さなければなりません（MUST）。ペアリングはスポンサーが表示する短命のQR（`marmot-pairing-v1:`）を使い、その秘密がキャリア非依存のチャネル上でHKDF-SHA256とChaCha20-Poly1305に供給されます。ローカル限定のkind `453`証明はセッションを共有アカウント鍵に束縛し、relayへ送られることはありません。一致するWelcomeの後、参加者の最初のアプリケーションペイロードは、WelcomeとGroupInfoのダイジェストに束縛された非描画のkind `452`確認応答であり、バイト単位で同一のWelcomeをKeyPackageを再消費せずに復元できます。ペアになったスポンサーはその枝における参加者の信頼の起点であり、グローバルな確定性を証明しません。付随するアカウント同期の文書は探索的で相互運用性がありません。この実験は採用済みのベースプロファイルには含まれません。

## Nostr の 6 年間の 8 月

8月は1つの相互運用性の問題をたどります。クライアントがどのように対象を名指し、それにフィードバックを付けるかという問題です。[元のprotocolリポジトリ](https://github.com/nostr-protocol/nostr)は2021年8月のコミットを記録しておらず、署名済みイベントの中核は動きませんでした。[NIP-25](/ja/topics/nip-25/)（リアクション）は2022年にkind 1限定の枠を離れます。通常のreplaceableレコードは2023年に空の識別子を持つ`naddr`と`a`の座標を得ました。2024年には、別枠の[parameterized-replaceableという分類がaddressable eventへ改称](https://github.com/nostr-protocol/nips/commit/ca3c52e3e74f0a4679f1c6c0d9ac6461ea748d2d)され、wire formatは変わりませんでした。リアクションは2025年に外部メディアへ移りました。[NIP-22](/ja/topics/nip-22/)（コメントスレッド）のkind 1111は2026年に実際に書き込むクライアントへ届きました。この流れは、止まったprotocol文書から、ノート、replaceableレコード、ネットワーク外の対象をまたいで機能する共通の返信・リアクション語彙へと向かっています。

### 2021年8月

元のprotocolリポジトリの[2021年8月のコミット窓](https://api.github.com/repos/nostr-protocol/nostr/commits?since=2021-08-01T00:00:00Z&until=2021-08-31T23:59:59Z)は空です。その不活発な月の直前の変更は6月18日のNIP-05ドラフトで、公開鍵への人間可読なポインタとしてDNSドメイン識別子を追加しました。[NIP-05](/ja/topics/nip-05/)（ドメイン識別子）は後にwell-known JSONファイルへ移りますが、2021年半ばではまだDNS TXTの参照でした。8月はその識別子の作業を広げることも、新しいイベントkindやrelayメッセージを追加することもありませんでした。

同じ空の窓は、仕様の隣にすでに存在していたツールにも現れます。2021年1月に作られたコマンドラインクライアントの[noscl](https://github.com/fiatjaf/noscl/commits?since=2021-08-01&until=2021-09-01)は8月のコミットを記録せず、[go-nostr](https://github.com/nbd-wtf/go-nostr/commits?since=2021-08-01&until=2021-09-01)も[nostr-tools](https://github.com/nbd-wtf/nostr-tools/commits?since=2021-08-01&until=2021-09-01)も同様でした。protocolの動きは年末になって再開し、リポジトリが[NIP-09](/ja/topics/nip-09/)（イベント削除要求）を割り当て、DNS方式をwell-known JSONの識別子ファイルに置き換えました。2021年8月は、6月の識別子ドラフトと12月の削除およびwell-known JSONの作業のあいだにある不活発な段階であり、その間[署名済みイベントとrelayのモデル](https://fiatjaf.com/nostr.html)は書かれたとおりに保たれていました。

### 2022年8月

8月19日、[NIP-25の編集](https://github.com/nostr-protocol/nips/commit/7af2540c6e392d5cb789c743b1dd237294388649)がkind 7リアクションの対象をkind 1テキストノートから他のノートへ広げました。kind 7イベントと`+`/`-`の慣習はすでにドラフトにありました。この相互運用性の変更により、いいね、よくない、絵文字がプロフィール、フォローリスト、あるいは同じ`e`と`p` tagを再利用する後年のどのイベントkindにも付けられるようになりました。

現在の[NIP-25仕様](https://github.com/nostr-protocol/nips/blob/master/25.md)はこの一般化を保っています。リアクションは他のイベントに対するユーザーの反応を示し、addressableな対象には`kind:pubkey:d-tag`座標を持つ`a` tagも付きます。Androidクライアントの[Amethyst](https://github.com/vitorpamplona/amethyst/blob/main/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip25Reactions/ReactionEvent.kt)はリアクションのbuilderでこの契約を実装しています。builderは任意のイベントを受け取り、`e`、`p`、`k` tagを書き、対象がaddressable eventのときは`a` tagを加えます。これによりリアクションの対象はkind 1を超えて一般化されました。後の8月の変更は安定した座標とコメントの文脈tagを加えていきます。

relayソフトウェアもtagの規則をストレージの挙動に落とし込んでいました。8月17日、nostr-rs-relayは[16進数に見えるすべてのtag値をバイナリのインデックスキーとして扱うのをやめました](https://github.com/scsibug/nostr-rs-relay/commit/035cf34673ae23407bda6656eef505b3178482ab)。その最適化を1文字のtagと小文字の16進値に限定し、フィルタが一致させられない形式へデコードするのではなく通常のテキストtagを保ちました。同じ月は相互運用性の両面を結び付けたことになります。仕様はインタラクションが指し得る対象を広げ、relayはその対象tagのインデックス付けと取得の仕方を正しました。

### 2023年8月

8月24日、[NIP-19](/ja/topics/nip-19/)（bech32識別子）は[非parameterizedなreplaceable eventをnaddrとしてエンコードする方法を定めました](https://github.com/nostr-protocol/nips/commit/208dee210249f84496ddfa823542d023e23b3edb)。識別子フィールドである`d` tagは、メタデータや連絡先リストのようにpubkeyとkindだけで置き換わるkindでは空文字列になりました。5日後、[NIP-01](/ja/topics/nip-01/)（基本のイベントとrelay protocol）が[対応するa-tag形式を追加](https://github.com/nostr-protocol/nips/commit/e50bf508d9014cfb19bfa8a5c4ec88dc4788d490)しました。末尾のコロンを持ち識別子のない`kind:pubkey:`です。これによりクライアントは、次の置き換えで無効になる特定のevent idを待たずにreplaceableレコードを指せるようになりました。

[現在のNIP-19の本文](https://github.com/nostr-protocol/nips/blob/master/19.md)は、それらのreplaceable eventには空文字列を使うよう実装者に伝えています。JavaScriptの識別子ライブラリ[nostr-tools](https://github.com/nbd-wtf/nostr-tools/blob/master/nip19.ts)は`naddrEncode`でそのフィールドをエンコードするので、呼び出し側は空の識別子を渡して共有可能な座標を作れます。2023年8月の作業は、replaceableな状態を、基となるイベントが置き換えられた後でもコメントやリアクション、共有リンクが名指せるものに変えました。翌年の8月は関連するparameterized-replaceableという分類の用語を標準化し、後のコメントtagはその座標文法を`A`と`a`として再利用します。

同じ時期に非公開のペイロードも可搬になりつつありました。8月24日、rust-nostrは[JavaScriptバインディングにNIP-44の暗号化・復号関数を追加](https://github.com/nostrdevkit/nostr/commit/39e581d398d926ff37a6b57a1c6d5fceae270d77)し、バージョン付きのconversation key方式をネイティブRustの呼び出し側と並んでwebアプリケーションにも公開しました。8月22日、Amethystは[NIP-44の暗号化をメッセージングイベント形式から分離](https://github.com/vitorpamplona/amethyst/commit/fa4257ad7d7afa76ccb368b4cf6cadefa39461ba)し、内容をどう暗号化するかとアプリケーションがそれをどう運ぶかというprotocolの分離を反映しました。安定した座標は公開の対象を参照しやすくし、再利用可能な暗号化APIは非公開の内容を1つのメッセージkindに縛らずに実装間で移しやすくしました。

同じ月は、隣接する鍵の分離、インターフェース、教育の作業にも資金をもたらしました。[8月17日のOpenSats助成ラウンド](https://github.com/OpenSats/website/commit/acd33f11b7529c34a846e8c4b4a6c63e7187f970)は、Nostr Fundの助成をAmber、共有のNostrインターフェース設計、Nostrの利用例の教育に配分しました。Amberの助成はNIP-46を通じて署名鍵を専用のAndroidアプリケーションに保つことに集中し、設計と教育の助成はオンボーディングと再利用可能なアプリケーションのパターンに取り組みました。より広いNostrのシステムは、仕様のコミット、鍵の分離、インターフェースの作業、そして共有インフラとして資金提供された開発者教育を通じて前進していました。

### 2024年8月

8月20日、仕様は[「parameterized replaceable event」を「addressable event」へ改称](https://github.com/nostr-protocol/nips/commit/ca3c52e3e74f0a4679f1c6c0d9ac6461ea748d2d)しました。NIP-01と他の16の文書にまたがり、長文記事、ライブアクティビティ、リスト、カレンダー、classified listingを含みます。wire formatは変わりませんでした。`kind:pubkey:d-tag`が座標であり続けました。変わったのは、その座標をすでに使っていたすべての仕様が同じ語でそれを呼ぶようになったことです。

その語彙は現在の実装が出荷しているものです。[NIP-01](https://github.com/nostr-protocol/nips/blob/master/01.md)はaddressable eventをkind、pubkey、`d` tagごとの最新レコードとして保存します。[NIP-19](https://github.com/nostr-protocol/nips/blob/master/19.md)はnaddrを"a nostr addressable event coordinate"と呼びます。上で引いたAmethystのリアクション経路は、`a` tagを書く前に対象を`AddressableEvent`として型付けします。2023年の座標拡張と2024年の用語変更はどちらも`kind:pubkey:d-tag`という座標文法を使い、NIP-01は通常のreplaceable eventとaddressable eventの区別を続けています。したがって後のコメントは、その番地を今どのevent idが占めているかを気にせず、大文字の`A`でaddressableな議論を取得できます。

ストレージのprotocolも明示的な識別子への同じ好みを適用していました。8月27日、BlossomのBUD-04は[1つの認可イベントが複数のblobハッシュ`x` tagを持てるようにしました](https://github.com/hzrd149/blossom/commit/4325aa79891cb4d68448ce16e5fa5519058eae4b)。これによりクライアントは、ハッシュが1つの対象を表しているかのように装わずに、上限付きのアップロード、ミラー、削除のバッチを認可できました。4日後、プロジェクトは[blob descriptorを明確化し例を追加](https://github.com/hzrd149/blossom/commit/95eb92e70768b0a2d5bab3dc42a5e3418f9055ec)しました。Nostrイベントは内容アドレス指定されたメディアの操作を調整し、バイト列はメディアサーバーに留まって、署名された認可とストレージのトランスポートが分離されました。

8月29日、リモート署名は不完全なrelay集合に対して寛容になりました。go-nostrはNIP-46クライアントを変更し、[1つの不調なrelayが他の設定済みrelay経由で送られるリクエストを妨げられない](https://github.com/nbd-wtf/go-nostr/commit/5edb54efee52f469fe62180c20d2876fe9c72910)ようにしました。relay接続と公開試行は独立に動き、いずれかの接続が成功すれば呼び出しは進みます。8月19日、OpenSatsは[Amethystの作者Vitor Pamplonaへの長期支援も発表](https://github.com/OpenSats/website/commit/b0ac18552a80c662b6ca33381abeed5c3d833a4c)し、NIP-17の非公開メッセージ、クロスプラットフォームのライブラリ、outboxモデルの作業を含めました。protocolの語彙、粘り強いトランスポート、プライバシーの作業、そして継続的な保守資金は同じ目標へ収束していました。端末をまたぎ、まちまちなrelayの状況でも動き続けられるクライアントです。

### 2025年8月

8月22日、[NIP-25は外部コンテンツへのリアクションを得ました](https://github.com/nostr-protocol/nips/pull/2020)。ネイティブなNostrイベントではないものへのリアクションはkind 17でなければならず、[NIP-73](/ja/topics/nip-73/)（外部コンテンツ識別子）の`k`と`i` tagを持たなければならず、以前のwebサイト用`r` tagを置き換えます。マージされた本文の例はweb URL（`k=web`）と、番組GUIDと項目GUIDで識別されるポッドキャストのエピソードで、FountainのURLがヒントとして添えられます。リアクションは2022年にkind 1を離れました。今度はNostrのイベント集合そのものを離れたのです。

2025年8月15日に公開された[Fountain 1.3](https://blog.fountain.fm/p/1-3)は、仕様のマージより先にそれらのいいねを出荷し、他のポッドキャストアプリが読めるようNostrで動くと述べました。今日の[NIP-25の文書](https://github.com/nostr-protocol/nips/blob/master/25.md)はいまもFountainのポッドキャストGUIDの例を使っています。2025年8月までに、リアクションの座標は、コメントが後に外部rootに対して使うのと同じ識別子文法で、ポッドキャストのエピソードやwebページを名指せるようになっていました。

### 2026年8月

この8月は、通常の返信を書くクライアントにコメントスレッドを持ち込みました。後にマージされた[6月の修正](/ja/newsletters/2026-06-24-newsletter/#kind-1111-as-reply-to-kind-1-notes)は、短いノートにNIP-22コメントを使わないようクライアントに伝えていた行を削除しました。続いて[NIP-30](/ja/topics/nip-30/)（カスタム絵文字）が[kind 1111を追加](https://github.com/nostr-protocol/nips/pull/2448)し、ノート、リアクション、ユーザーステータスと並べたので、コメントもそれらのkindが既に使っていた同じ絵文字tagを持てます。仕様の作業は許可です。クライアントの作業は展開です。

webクライアントの[Snort](https://github.com/v0l/snort/commit/420ed60e2ff43bd373f2583e171a77002ec9f3a0)は、kind 1の対象に対して既定でNIP-22コメントを公開し、大文字の`E`/`A` root tagでスレッドを購読し、通知でkind 1111を受け入れます。コミュニティ向けwebクライアントの[Ditto](https://github.com/soapbox-pub/ditto/commit/8a0ffc6e3a5d9202ffc452fa0de8ae33b5883384)は、kind 1ノートへの返信も含めてすべての返信をNIP-22コメントとして公開し、テキストはkind 1111、音声は1244としつつ、[NIP-10](/ja/topics/nip-10/)（ノートのスレッド化）の返信も読み続けます。6年間の移り変わりはこれらの既定に現れています。2022年はリアクションを一般化し、2023年と2024年は座標を名付け、2025年はリアクションをネットワーク外へ向け、2026年はコメントをそれら同じ対象に対する共通の返信イベントにしました。

非公開グループの基盤は、復旧を相互運用性の要件として定義していました。Marmotの[8月13日の永続性と再起動の契約](https://github.com/marmot-protocol/marmot/commit/4a2bc65f8db5866cec3b2a127dedb37818eaf207)は、どのローカルMLSおよび公開の状態が再起動を生き延びなければならないかを定め、クライアントがグループ操作を続ける前に永続化された状態を突き合わせることを求めます。これは8月の流れを対象の名指しの先へ広げます。成熟したクライアントは、中断の後で安全に再開できるだけの暗号と配信の状態も保たなければなりません。共通のイベント形式が役に立つのは、実装がそれを使うために必要な状態を復元できるときだけです。

---

[Nostr Compassプロジェクト](https://github.com/andotherstuff/nostr-compass)を通じてプロジェクトやニュースを共有するには、[NIP-17](/ja/topics/nip-17/) DMを送ってください。
