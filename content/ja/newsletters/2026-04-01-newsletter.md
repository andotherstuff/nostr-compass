---
title: 'Nostr Compass #16'
date: 2026-04-01
translationOf: /en/newsletters/2026-04-01-newsletter.md
translationDate: 2026-04-01
draft: false
type: newsletters
---

Nostr Compassへようこそ。Nostrの週刊ガイドです。

**今週の内容:** [Amethyst](https://github.com/vitorpamplona/amethyst)が、ピン留めノート、[NIP-86](/ja/topics/nip-86/)経由のrelay管理、[NIP-62](/ja/topics/nip-62/) Request to Vanishサポートを備えた[v1.07.0](#amethystがピン留めノートrelay管理request-to-vanishを出荷)を出荷しました。[NIP-5A](#nip-5aがマージ-nostrに静的ウェブサイトをもたらす)（静的ウェブサイト）がNIPsリポジトリへマージされ、[Blossom](/ja/topics/blossom/)ストレージを使ってNostrキーペア配下でサイトをホストする方法を定義しました。[Flotilla](https://gitea.coracle.social/coracle/flotilla)は、voice rooms、email/password login、proof-of-work DMを含む[v1.7.0](#flotilla-v170がvoice-roomsemail-loginを追加)を出荷しました。[White Noise](https://github.com/marmot-protocol/whitenoise)は[v2026.3.23](#white-noiseがrelay-churnを修正しクライアント制御を拡張)でrelay churnを修正し、[nospeak](https://github.com/psic4t/nospeak)はサインアップ不要の暗号化メッセンジャーとして[1.0.0](#nospeakが10プライベートメッセンジャーとしてローンチ)を開始しました。[Nymchat](https://github.com/Spl0itable/NYM)は[group chats向けにMarmotを採用](#nymchatがmarmotベースのグループチャットを出荷)し、[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar)はプライベートカレンダーリストとICS importを備えた[v1.0.0](#calendar-by-form-v100)へ到達し、[Amber](https://github.com/greenart7c3/Amber)は[mnemonic recoveryとNIP-42 relay auth whitelist](#amber-v502-から-v504)を追加し、[Marmot spec](#marmotがkeypackageをアドレス可能イベントへ移しpush-notificationを厳格化)はKeyPackagesをアドレス可能イベントへ移してMIP-05 push notification形式を厳格化しました。

## ニュース

### Amethystがピン留めノート、relay管理、Request to Vanishを出荷

[Amethyst](https://github.com/vitorpamplona/amethyst)はvitorpamplonaがメンテナンスするAndroidクライアントで、3日間に6リリース、[v1.07.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.0)から[v1.07.5](https://github.com/vitorpamplona/amethyst/releases/tag/v1.07.5)までを出荷しました。目玉機能群は6つのプロトコルサーフェスにまたがっています。ピン留めノート、専用ポールフィード画面、relayへ完全なイベント削除を求める[NIP-62](/ja/topics/nip-62/)（Request to Vanish）サポート、クライアント内からの[NIP-86](/ja/topics/nip-86/)（Relay Management API）、relay情報画面内の[NIP-66](/ja/topics/nip-66/)（Relay Discovery and Liveness Monitoring）評価、そして[NIP-43](/ja/topics/nip-43/)（Relay Access Metadata and Requests）のメンバー情報表示です。

[NIP-86](/ja/topics/nip-86/)はrelayオペレーター向けのJSON-RPCインターフェースを定義し、pubkeyのBAN、pubkeyの許可、BANユーザー一覧の取得といった管理コマンドを標準化API経由でクライアントから送れるようにします。Amethystはこれをrelay管理UIに直接公開したため、自分のrelayを運用するユーザーは、投稿に使うのと同じクライアントから運用管理もできるようになりました。[PR #2039](https://github.com/vitorpamplona/amethyst/pull/2039)は、BANおよび許可pubkeyの旧来のhex入力ダイアログを、対話型のユーザー検索ダイアログへ置き換えています。

v1.07.2ではGIF keyboard uploadsが追加され、旧Amberバージョンが`rejected`フィールドに空文字列を返していたために起きていた署名リグレッションも修正されました（[PR #2042](https://github.com/vitorpamplona/amethyst/pull/2042)）。v1.07.5では画像アップロード時クラッシュが修正されています。同週前半の[v1.06.2](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.2)と[v1.06.3](https://github.com/vitorpamplona/amethyst/releases/tag/v1.06.3)では、単一選択と複数選択ポールの切り替え、動画プログレスバーのdrag-to-seek、匿名投稿の改善が入っていました。

### NIP-5Aがマージ、Nostrに静的ウェブサイトをもたらす

[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md)（静的ウェブサイト）が[PR #1538](https://github.com/nostr-protocol/nips/pull/1538)経由でマージされ、Nostrキーペア配下で静的ウェブサイトをホストする方法を定義しました。仕様は2つのイベントkindを使います。kind `15128`はpubkeyごとに1つのroot site用、kind `35128`は`d`タグで識別されるnamed site用です。各manifestはURL pathをSHA256 hashへ対応づけ、実ファイルが置かれている[Blossom](/ja/topics/blossom/)ストレージホストを指す`server`タグをオプションで持てます。

ホスティングモデルは次のように動きます。サイト作者が静的サイトをビルドし、ファイルを1つまたは複数のBlossomサーバーへアップロードし、その後にpathとcontent hashの対応表を持つ署名済みmanifestイベントを公開します。ホストサーバーはWebリクエストを受けると、subdomainから作者のpubkeyを解決し、作者の[NIP-65](/ja/topics/nip-65/) relay listからmanifestを取得し、対応するblobをBlossomからダウンロードして配信します。更新manifestに署名できるのはその鍵だけなので、サイトの制御権は作者の側に残ります。NIP-5Aを理解するサーバーならどれでも同じmanifestから同じサイトを配信できるため、ホストサーバー自体は置き換え可能です。

この仕様はすでに存在していたインフラの上に乗っています。lezによるNIP-5Aのreference host実装[nsite](https://github.com/lez/nsite)と、hzrd149による管理UI[nsite-manager](https://github.com/hzrd149/nsite-manager)は、NIPがマージされる前から稼働していました。今回のマージにより、イベントkindとURL解決ルールが公式化され、2つ目3つ目の実装にとって安定したターゲットが生まれました。

### White Noiseがrelay churnを修正し、クライアント制御を拡張

[White Noise](https://github.com/marmot-protocol/whitenoise)は[Marmot](/ja/topics/marmot/)プロトコル上のプライベートメッセンジャーで、3月25日に[v2026.3.23](https://github.com/marmot-protocol/whitenoise/releases/tag/v2026.3.23)を出荷しました。主な作業はrelay安定性です。relay list publishはquorum logicを使い、残りをバックグラウンドで再試行するようになったため、ログインはすべてのrelay-list publish完了を待たずに先へ進めるようになりました。単発のfetchとpublishは長寿命poolに残留せず、スコープ付きの一時relay sessionを使います。復元されたsessionは起動後にgroup refresh pathを回復し、アプリは[PR #495](https://github.com/marmot-protocol/whitenoise/pull/495)と[PR #502](https://github.com/marmot-protocol/whitenoise/pull/502)を通じてrelay diagnosticsとrelay state inspectionを公開しました。

同じリリースでは会話の振る舞いも変わりました。[PR #468](https://github.com/marmot-protocol/whitenoise/pull/468)が`q`タグと`nostr:nevent`参照を使うNIP-C7 reply threadingを追加し、[PR #471](https://github.com/marmot-protocol/whitenoise/pull/471)と[PR #512](https://github.com/marmot-protocol/whitenoise/pull/512)が削除メッセージを静かに消すのではなく削除済みプレースホルダーとして見せるようにし、[PR #478](https://github.com/marmot-protocol/whitenoise/pull/478)が[NIP-44](/ja/topics/nip-44/)（暗号化ペイロード）を使った匿名バグレポートフローを入れ、[PR #486](https://github.com/marmot-protocol/whitenoise/pull/486)がクライアント内サポートチャットを追加しました。ユーザー向けメッセージ制御も同期間に入り、[PR #532](https://github.com/marmot-protocol/whitenoise/pull/532)はchat archive、[PR #541](https://github.com/marmot-protocol/whitenoise/pull/541)は期間指定可能なmute/unmute、[PR #535](https://github.com/marmot-protocol/whitenoise/pull/535)はnotification settingsを追加しています。[PR #539](https://github.com/marmot-protocol/whitenoise/pull/539)はpush登録の準備作業で、iOSではAPNs登録、AndroidではPlay Services検出を配線し、その上に登録処理を積める状態にしました。バックエンド側では[MDK](https://github.com/marmot-protocol/mdk)がMIP-05 push notification primitivesとnotification request builderを追加し（[PR #235](https://github.com/marmot-protocol/mdk/pull/235)、[PR #238](https://github.com/marmot-protocol/mdk/pull/238)）、[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)はpush notification登録の永続化（[PR #688](https://github.com/marmot-protocol/whitenoise-rs/pull/688)）、バックグラウンドタスクキャンセル修正（[PR #696](https://github.com/marmot-protocol/whitenoise-rs/pull/696)）、起動時のkey package回復（[PR #693](https://github.com/marmot-protocol/whitenoise-rs/pull/693)）を追加しました。

### Nostr VPNがv0.3.0に到達し、roster syncとinvite v2を追加

[先週のローンチ記事](/ja/newsletters/2026-03-25-newsletter/#nostr-vpnがtailscale代替としてローンチ)に続き、Nostr relayをシグナリングに、WireGuardを暗号化トンネルに使うP2P VPNの[nostr-vpn](https://github.com/mmalmi/nostr-vpn)は高速なリリースペースを維持し、[v0.3.3](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.3.3)まで進みました。このバージョン更新では2つの破壊的変更が入っています。invite formatがv2へ移行し（0.3.0はv1 inviteをまだimportできますが、旧ビルドはv2 inviteをimportできません）、シグナリングプロトコルにadmin署名付きroster syncが追加されました。バージョンが混在するpeer同士でもmesh層では接続できますが、古いpeerはroster同期には参加しません。

roster syncの追加は、managed networkへの移行の始まりです。admin nodeが全peerにmembership変更をpushできるようになり、meshへのデバイス追加や削除のたびに各peerが手動で設定を更新する必要がなくなります。同週のv0.2.xリリース群は具体的なデプロイ問題を修正しており、[v0.2.22](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.22)から[v0.2.28](https://github.com/mmalmi/nostr-vpn/releases/tag/v0.2.28)ではWindows service管理、Android build scripts、LAN pairing flowの改善が入っています。

### nospeakが1.0プライベートメッセンジャーとしてローンチ

[nospeak](https://github.com/psic4t/nospeak)はNostr上のプライベートメッセンジャーで、3月27日に[1.0.0](https://github.com/psic4t/nospeak/releases/tag/v1.0.0)を出荷しました。プロジェクトは1対1会話、グループ会話、連絡先管理、self-hostableアーキテクチャを含みます。1対1チャットは[NIP-17](/ja/topics/nip-17/)（プライベートダイレクトメッセージ）を使い、これは[NIP-59](/ja/topics/nip-59/)（Gift Wrap）と[NIP-44](/ja/topics/nip-44/)（暗号化ペイロード）を組み合わせることで、relayから送信者を隠します。メディアについては、ファイルはBlossomサーバーへアップロードされる前にクライアント側でAES-256-GCM暗号化されます。このリリースはself-hosting向けcontainer imageとしても配布されています。

### Flotilla v1.7.0がvoice roomsとemail loginを追加

[Flotilla](https://gitea.coracle.social/coracle/flotilla)は、hodlbodによるDiscord風[NIP-29](/ja/topics/nip-29/)（Relay-based Groups）クライアントで、「relays as groups」モデルを中心に構築されています。3月30日と31日に[v1.7.0](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.0)および[v1.7.1](https://gitea.coracle.social/coracle/flotilla/src/tag/1.7.1)を出荷しました。目玉機能はmplorentzによるvoice roomsです。ユーザーはグループchannel内でvoice callへ参加できるようになり、join dialog（[PR #109](https://gitea.coracle.social/coracle/flotilla/pulls/109)）ではaudio input deviceの選択と、音声通話に参加するかテキストチャットだけを見るかを選べます。このダイアログは前段のUX問題を解決します。以前はvoice対応roomへ入ると、メッセージ閲覧や設定確認だけが目的でもマイクが強制的に有効化されていました。

同じリリースには、Nostr鍵ベース認証の代替となるemail/password login、DMへのproof-of-work、DM編集、再設計されたrelay onboardingとsettings、`supported_nips`経由のBlossomサポート検出、改善されたnotification badges、Android push notification fallback、Androidでのfile upload修正も入っています。v1.7.1ではoffline signer使用時のpomade registration fallbackも修正されました。

hodlbodは同時に[zooid relay](https://gitea.coracle.social/coracle/caravel)向けのhosting managerおよびdashboardであるCaravelも構築しており、初期開発だけで今週40コミットを記録しています。

### NymchatがMarmotベースのgroup chatsを出荷

[Nymchat](https://github.com/Spl0itable/NYM)（NYM、Nostr Ynstant Messengerとしても知られます）はBitchatとbridgeされたエフェメラルチャットクライアントで、すべての新しいグループチャットが[Marmot](/ja/topics/marmot/)プロトコルを使うMLS暗号化メッセージングへ移行したと発表しました。この統合では、key packages、welcome messages、group messagesにそれぞれkinds `443`、`444`、`445`を使い、forward secrecy、post-compromise security、metadata leakageゼロを提供します。受信者がMLSを使えない場合、Nymchatは従来の[NIP-17](/ja/topics/nip-17/)（プライベートダイレクトメッセージ）ベースのgroup chat pathにフォールバックします。こちらもエンドツーエンド暗号化ですが、MLSのratchet-tree特性は持ちません。

今週のv3.55およびv3.56系列は、新規デバイスでの読み込み、leave動作、notification routing、未読badge countといったgroup chatの境界ケースに集中していました。同じサイクルでは、エスケープされていないHTMLに起因するXSS脆弱性の修正と、user nicknameにも拡張されたkeyword/phrase blockingも入りました。これによりNymchatは、[White Noise](#white-noiseがrelay-churnを修正しクライアント制御を拡張)と[OpenChat](#openchat-v024-から-v030)に続くもう1つのMarmotクライアントとなり、同じプロトコル上でMLS暗号化group messagesを交換できるアプリ群を広げています。

## リリース

### Calendar by Form* v1.0.0

[Calendar by Form*](https://github.com/formstr-hq/nostr-calendar)は[NIP-52](/ja/topics/nip-52/)（カレンダーイベント）上に構築された分散カレンダーアプリで、3月29日に[v1.0.0](https://github.com/formstr-hq/nostr-calendar/releases/tag/v1.0.0)へ到達しました。このリリースは、暗号化Nostrイベント（kind `32123`）と[NIP-44](/ja/topics/nip-44/)（暗号化ペイロード）の自己暗号化を使うprivate calendar listsを追加し、relayへそのグルーピングを明かさずにイベントを私的コレクションへ整理できるようにします。同じリリースでは、他アプリからカレンダーデータを取り込むICS intent handlingと、ユーザー間でイベントを共有するinvitation requestsも追加されました。

### Amber v5.0.2 から v5.0.4

[Amber](https://github.com/greenart7c3/Amber)は[NIP-55](/ja/topics/nip-55/)（Android署名アプリケーション）署名者アプリで、3つのポイントリリース、[v5.0.2](https://github.com/greenart7c3/Amber/releases/tag/v5.0.2)、[v5.0.3](https://github.com/greenart7c3/Amber/releases/tag/v5.0.3)、[v5.0.4](https://github.com/greenart7c3/Amber/releases/tag/v5.0.4)を出荷しました。最も目に見える追加は、raw nsecやncryptsec文字列を要求せず、BIP39 seed phraseからsignerを復元できるmnemonic recovery phrase login（[PR #358](https://github.com/greenart7c3/Amber/pull/358)）です。[PR #357](https://github.com/greenart7c3/Amber/pull/357)は[NIP-42](/ja/topics/nip-42/) relay auth whitelistを追加し、どのrelayがclient authenticationを要求できるかをユーザーが制限できるようにしました。[PR #353](https://github.com/greenart7c3/Amber/pull/353)はdecrypt permission向けのencryption scope選択を追加し、包括的権限ではなくNIP-04専用あるいはNIP-44専用のdecrypt accessを付与できるようにしています。v5.0.4では、scoped encrypt/decrypt permissionsが拒否処理に正しく反映されないバグが修正され、複数のbunker request受信時の性能も改善されました。

### Aegis v0.4.0

[Aegis](https://github.com/ZharlieW/Aegis)はクロスプラットフォーム署名者で、3月26日に[v0.4.0](https://github.com/ZharlieW/Aegis/releases/tag/v0.4.0)を出荷しました。このリリースではSettingsにFullおよびSelective authorization modesが追加され、複数のQRスキャン問題も修正されています。追随するコミット[d4f799f](https://github.com/ZharlieW/Aegis/commit/d4f799fe51dd82968d54f72ac77f2de29d0cfe6b)、[3313af9](https://github.com/ZharlieW/Aegis/commit/3313af92e55e449ebc98fbd91a085bd444d716e7)、[3b214e4](https://github.com/ZharlieW/Aegis/commit/3b214e4176f5dbe7f18690d0996e69dd151fe00f)、[e4f40b6](https://github.com/ZharlieW/Aegis/commit/e4f40b6f1f48c2dae1bb5e4246df26c26dba419e)では、この方向をさらに進め、batch select controls、再利用可能なbatch selection stats、set-all-groups selection APIs、app permissionsページ上のpermission別使用統計を追加しています。

### Schemata v0.2.7 から v0.3.0

[Schemata](https://github.com/nostrability/schemata)はNostrイベントkind検証用のJSON Schema定義群で、[v0.2.7](https://github.com/nostrability/schemata/releases/tag/v0.2.7)から[v0.3.0](https://github.com/nostrability/schemata/releases/tag/v0.3.0)まで4リリース、21件のマージ済みPRを出しました。v0.3.0では、relay URL、hex ID、MIME type、BOLT-11文字列にわたるpattern consistency修正（[PR #126](https://github.com/nostrability/schemata/pull/126)）、relay URL patternの集中管理（[PR #117](https://github.com/nostrability/schemata/pull/117)）、[NIP-19](/ja/topics/nip-19/) bech32 base type schema（[PR #118](https://github.com/nostrability/schemata/pull/118)）、kind 777 spellイベントの検証（[PR #125](https://github.com/nostrability/schemata/pull/125)）が入りました。release pipelineは各リリース時にNostrへkind `1` noteも公開するようになり（[PR #120](https://github.com/nostrability/schemata/pull/120)）、プロジェクト自身が検証対象のプロトコルを通じて自らを告知します。Schemataは、canonicalなJS/TSパッケージ以外に、Rust、Go、Python、Kotlin、Java、Swift、Dart、PHP、C#/.NET、C++、Ruby、Cの計12超の言語をサポートするようになりました。

Schemataと並行して、チームは[schemata-codegen](https://github.com/nostrability/schemata-codegen)も公開しました。これは同じ検証問題に対して別アプローチを取る実験的コードジェネレーターです。Schemataのvalidator packagesがJSON Schema runtime dependencyを必要とするのに対し、schemata-codegenはschemaをtyped tag tuples、kind interfaces、runtime validatorsといったネイティブ言語構造へ直接移植することで、実行時にvalidator libraryを不要にします。[codegen-vs-validators比較](https://github.com/nostrability/schemata-codegen/blob/main/CODEGEN-VS-VALIDATORS.md)は、どちらのアプローチがどの場面に適するかを文書化しています。

### BigBrotr v6.5.0 から v6.5.4

[BigBrotr](https://github.com/BigBrotr/bigbrotr)はrelay分析プラットフォームで、[v6.5.0](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.5.0)から[v6.5.4](https://github.com/BigBrotr/bigbrotr/releases/tag/v6.5.4)まで5リリースを出荷しました。v6.5.0では、`parse_relay_url()` factory functionによるrelay URL validationの集中化、URL length checking、path sanitizationが入りました。monitoring基盤にも修正があり、announcementイベントは[NIP-52](/ja/topics/nip-52/)にならったgeohash location tagsを含むようになり、期限のなかったGeo/Net [NIP-66](/ja/topics/nip-66/) metadata testsにはtimeout protectionが追加され、無期限ハングを防いでいます。[PR #410](https://github.com/BigBrotr/bigbrotr/pull/410)はPostgreSQLを16から18へ上げており、async I/O subsystemとWAL throughput改善がrelay analytics pipelineに入っています。

### Vertex Lab relayがNIP-50プロフィール検索を追加

[Vertex Lab](https://vertexlab.io)は[npub.world](https://github.com/vertex-lab/npub.world)と[Vertex](https://vertexlab.io/docs) Web of Trust engineを手がけるチームで、`wss://relay.vertexlab.io`がプロフィールクエリ向けに[NIP-50](/ja/topics/nip-50/)（検索）をサポートしたと発表しました。NIP-50は標準Nostr `REQ` filterに`search`フィールドを拡張し、relayがindexを持つ場合にクライアントが全文検索クエリを送れるようにします。Web of Trustデータも提供するrelayにプロフィール検索が入ることで、`relay.vertexlab.io`へ接続するクライアントは別検索サービスなしに名前や説明からユーザーを発見できます。

### Hashtree v0.2.17 と v0.2.18がWebRTCメッシュとIris Desktopを出荷

[Hashtree](https://github.com/mmalmi/hashtree)はmmalmiによる、Merkle rootをNostrへ公開するcontent-addressed blob storage systemで、3月31日に[v0.2.17](https://github.com/mmalmi/hashtree/releases/tag/v0.2.17)と[v0.2.18](https://github.com/mmalmi/hashtree/releases/tag/v0.2.18)を出荷しました。この2リリースは30コミットのスプリントを締めくくるもので、3つの機能が加わっています。1つ目は`hashtree-webrtc` crate（v0.2.18で`hashtree-network`へ改名）によるWebRTCベースのP2P blob配布で、Rust CLI、simulation harness、TypeScript clientにまたがる統一mesh signalingを追加します。2つ目はrelease pipelineがWindows artifacts（CLI zipとIris installer）をビルドするようになったことで、macOS、Linux、Windowsのクロスプラットフォーム対応が整いました。3つ目は、両リリースがIris Desktop 0.1.0、すなわちmmalmiのNostr social clientを、AppImage、.deb、Windows installer assetとしてhashtree CLIと一緒に同梱していることです。Hashtreeは[Newsletter #10](/ja/newsletters/2026-02-18-newsletter/)で、filesystemベースの[Blossom](/ja/topics/blossom/)互換ストアとして初めて取り上げました。今回のWebRTC層は、中央集権的Blossomサーバーに依存しないP2P content distributionへの第一歩です。

### Nostr Mail Client v0.7.0 から v0.7.2

[Nostr Mail Client](https://github.com/nogringo/nostr-mail-client)はNostrアイデンティティ上に構築されたFlutter製メール風クライアントで、3日間で[v0.7.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.0)、[v0.7.1](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.1)、[v0.7.2](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.7.2)を出荷しました。見えるプロダクト作業はオンボーディング（[PR #9](https://github.com/nogringo/nostr-mail-client/pull/9)）とプロフィール編集（[PR #10](https://github.com/nogringo/nostr-mail-client/pull/10)）に集中しており、Nostrをメールボックスとして提示しようとするクライアントにとって基本的な部品です。後続のポイントリリースはこの作業を新しいAndroidおよびLinuxビルドへパッケージしました。

### Wisp v0.14.0 から v0.16.1

[Wisp](https://github.com/barrydeen/wisp)はAndroid Nostrクライアントで、今週さらに[v0.14.0-beta](https://github.com/barrydeen/wisp/releases/tag/v0.14.0-beta)から[v0.16.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.3-beta)まで13リリースを出しました。作業内容には、NIP-17 rumor JSON修正（[PR #385](https://github.com/barrydeen/wisp/pull/385)）、gallery cards上のrepost badges（[PR #383](https://github.com/barrydeen/wisp/pull/383)）、展開可能なreaction details（[PR #382](https://github.com/barrydeen/wisp/pull/382)）、永続emoji sets（[PR #381](https://github.com/barrydeen/wisp/pull/381)）、video autoplay controls（[PR #380](https://github.com/barrydeen/wisp/pull/380)）が含まれます。最新の[v0.16.3-beta](https://github.com/barrydeen/wisp/releases/tag/v0.16.3-beta)では、ハイフンを含むcustom emoji shortcodeと欠落emoji tagsも修正されています。

### Primal Android 3.0.17

[Primal Android](https://github.com/PrimalHQ/primal-android-app)は3月24日に[3.0.17](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.0.17)を出荷しました。[PR #1000](https://github.com/PrimalHQ/primal-android-app/pull/1000)はWalletExceptionの型をNWC response内のerror codeへ対応付け、[NIP-47](/ja/topics/nip-47/)クライアントに汎用エラーではなく構造化された障害情報を返します。[PR #995](https://github.com/PrimalHQ/primal-android-app/pull/995)はpoll zap votesがTop Zapsとして見えてしまう問題を修正し、[PR #998](https://github.com/PrimalHQ/primal-android-app/pull/998)はwallet未設定時に残高とaction buttonsを非表示にします。

### OpenChat v0.2.4 から v0.3.0

[OpenChat](https://github.com/DavidGershony/openChat)は[Marmot](/ja/topics/marmot/)スタック上に構築されたAvaloniaベースのチャットクライアントで、4日間で[v0.2.4](https://github.com/DavidGershony/openChat/releases/tag/v0.2.4)から[v0.3.0](https://github.com/DavidGershony/openChat/releases/tag/v0.3.0)まで6リリースを出荷しました。commit logは、「Marmotが動く」から「誰かが日常的に使える」までの隙間を埋めていくクライアントの過程を示しています。[NIP-42](/ja/topics/nip-42/) relay authenticationが入り、それに続いてduplicate event filteringを持つrelay picker UIも入りました。voice messagesはpause、resume、seek、時間表示を獲得しました。signer pathも強化され、更新された[NIP-46](/ja/topics/nip-46/) URI formatによってAmber接続が修正され、WebSocketはrequest送信前に自動再接続するようになり、replayed responseを検査することでduplicate Amber requestsも捕捉されます。ストレージ面では、LinuxとmacOSにAES-256-GCM secure storageとfile-backed keysが入り、user metadata fetchは[NIP-65](/ja/topics/nip-65/) relay discoveryを使ってローカルデータベースにキャッシュされるようになりました。

### Igloo Signer 1.1

[Igloo](https://github.com/FROSTR-ORG/igloo-ios-prototype)はFROSTRプロジェクトによるiOS向け[FROST](/ja/topics/frost/) threshold signerで、3月28日に[v1.1](https://github.com/FROSTR-ORG/igloo-ios-prototype/releases/tag/v1.1)を出荷しました。FROST（Flexible Round-Optimized Schnorr Threshold）署名は、署名者のグループが共同で1つのNostrキーペアを制御し、単一の当事者が完全な秘密鍵を保持しないまま、t-of-n参加者でイベント署名できるようにします。Iglooは、Nostr向けにこのアプローチを実装した最初期のモバイル実装の1つです。

### nak v0.19.3 と v0.19.4

fiatjafのコマンドラインNostrツールキット[nak](https://github.com/fiatjaf/nak)が、3月26日と30日に[v0.19.3](https://github.com/fiatjaf/nak/releases/tag/v0.19.3)と[v0.19.4](https://github.com/fiatjaf/nak/releases/tag/v0.19.4)を出荷しました。どちらのリリースもpanic条件を修正しています。[PR #118](https://github.com/fiatjaf/nak/pull/118)は`strings.Split`を`strings.Cut`へ置き換え、潜在的なout-of-bounds accessを防ぎます。[PR #119](https://github.com/fiatjaf/nak/pull/119)はcurl flag parsingでも同種のpanicを防ぎます。

### Flora v0.3.0

[Flora](https://github.com/shawnyeager/flora-extension)は、Nostr上で分散スクリーン録画と共有を行うChrome拡張で、[v0.3.0](https://github.com/shawnyeager/flora-extension/releases/tag/v0.3.0)を出荷しました。このリリースは、public、unlisted、private modeを備えたprivate encrypted video sharingを追加します。private録画はAES-256-GCMで暗号化され、[NIP-17](/ja/topics/nip-17/)（プライベートダイレクトメッセージ）経由で受信者に渡されるため、録画は平文のままサーバーに触れません。

### YakiHonne Mobile 2.0.3

[YakiHonne](https://github.com/YakiHonne/mobile-app)はモバイルNostrクライアントで、relay reviewsとjoin requests、拡張されたnested replies、ノートのauto-translation、NWC multi-relay supportを含む[2.0.3](https://github.com/YakiHonne/mobile-app/releases/tag/YakiHonne-2.0.3)を出荷しました。

## プロジェクトアップデート

### Zap Cookingがzap pollsとBranta支払い検証を追加

[Zap Cooking](https://github.com/zapcooking/frontend)はレシピおよびcontentプラットフォームで、今週11件のPRをマージしました。焦点はinteractive contentとpayment flowsです。[PR #277](https://github.com/zapcooking/frontend/pull/277)はkind 6969のzap pollsを追加し、ユーザーはsatsを送って投票し、プロフィール画像付きで投票者一覧を見られるようになりました。[PR #274](https://github.com/zapcooking/frontend/pull/274)は投票インターフェースがフィード内で自然に見えるようpoll UXを再設計しています。

[PR #276](https://github.com/zapcooking/frontend/pull/276)はSend Payment flowにcamera-based QR scanningを追加し、送信先が正当かどうかを送信前に確認する検証サービス[Branta](https://branta.pro/)を統合しました。Brantaは送信前に支払い先をphishing、address swaps、man-in-the-middle interceptionに対して検査します。Zap Cookingでの実装では、Brantaにより検証されたplatform nameとlogoが支払いフロー内に直接表示され、Branta対応QRコードは`branta_id`と`branta_secret`パラメータを持てるため、walletはスキャンされたコード自体から送信先を検証できます。

### diVineが統一検索の基盤を敷き、動画配信を強化

[diVine](https://github.com/divinevideo/divine-mobile)は短尺動画クライアントで、今週は検索、feed navigation、playback recovery、upload behaviorの強化に取り組みました。[PR #2540](https://github.com/divinevideo/divine-mobile/pull/2540)は、Videos、People、Tagsのグループ化セクションを持つ統一検索画面の基礎を敷きます。[PR #2623](https://github.com/divinevideo/divine-mobile/pull/2623)は、profile feeds、inbox、notifications、discover lists、classic vines、search、composable grid feedsにわたるpaginationを共通pagination controllerへ移すことで全体を強化しました。

動画配信にも具体的な修正がいくつか入りました。[PR #2643](https://github.com/divinevideo/divine-mobile/pull/2643)はDivineホスト由来の派生ソースを順番に再試行し、それでもだめならraw blobへフォールバックしてからplayback errorを出すようにし、1つのソースの一時障害で即座に再生失敗にならないようにします。[PR #2634](https://github.com/divinevideo/divine-mobile/pull/2634)はcapability probingが一時的に失敗してもresumable uploadをDivine所有パスに維持し、短時間のネットワーク障害でuploadが壊れることを減らします。[PR #2637](https://github.com/divinevideo/divine-mobile/pull/2637)はsensitive-content gateも変更し、実際のwarning labelsがある動画のみをハードゲートし、単に作者が付けたcontent warning labelだけではゲートしないようにしました。

### Shopstrがカスタムstorefrontを追加し、Milk Marketが引き続きマーケットプレイス作業を進める

[Shopstr](https://github.com/shopstr-eng/shopstr)はNostrベースのマーケットプレイスで、[PR #245](https://github.com/shopstr-eng/shopstr/pull/245)をマージしてcustom storefrontsを追加しました。これにより、売り手はすべてのlistingが同じ汎用表示に押し込まれるのではなく、より独自性のあるhome surfaceを持てます。

[Milk Market](https://github.com/shopstr-eng/milk-market)は牛乳に特化した専用マーケットプレイスで、storefront最適化（[PR #18](https://github.com/shopstr-eng/milk-market/pull/18)）、account recovery（[PR #17](https://github.com/shopstr-eng/milk-market/pull/17)）、beef splits（[PR #15](https://github.com/shopstr-eng/milk-market/pull/15)）、MCP tool typing fixes（[PR #16](https://github.com/shopstr-eng/milk-market/pull/16)）を継続しています。

### Notedeckが効果音を追加し、Android向けupdater pathを拡張

[Notedeck](https://github.com/damus-io/notedeck)はDamusチームによるデスクトップクライアントで、rodioを使ったUI interaction soundsを含むsound effects subsystemを追加する[PR #1412](https://github.com/damus-io/notedeck/pull/1412)と、CLI title flagや折りたたみ可能なsession foldersを含むAgentium更新を入れる[PR #1399](https://github.com/damus-io/notedeck/pull/1399)をマージしました。オープンな[PR #1417](https://github.com/damus-io/notedeck/pull/1417)は、Android上でNostr/Zapstore経由のAPK self-updateを提案しており、[Newsletter #14](/ja/newsletters/2026-03-18-newsletter/#notedeckがリリース発見をnostr上に移行)で扱ったNotedeckのNostrネイティブupdater作業をさらに先へ進めています。

### Nostriaがrepost relay hintsとNIP-98整合を追加

[Nostria](https://github.com/nostria-app/nostria)は、kind 6およびkind 16イベントのrepost `e` tagsへ[NIP-18](/ja/topics/nip-18/)（Reposts）relay hintsを追加する[PR #583](https://github.com/nostria-app/nostria/pull/583)、Brainstorm HTTP auth（kind 27235）を[NIP-98](/ja/topics/nip-98/)（HTTP認証）の必須タグへ合わせる[PR #582](https://github.com/nostria-app/nostria/pull/582)、Schemata schema validation testsを追加する[PR #576](https://github.com/nostria-app/nostria/pull/576)をマージしました。NIP-98の変更により、Nostriaは他クライアントと同じHTTP auth形式で外部サービスへ認証できるようになります。

### Nostr-Docがデスクトップパッケージングとoffline-first作業を追加

[Nostr-Doc](https://github.com/formstr-hq/nostr-docs)はForm*による共同編集ツールで、今週はパッケージングとエディター作業が活発でした。[commit fcdc00a](https://github.com/formstr-hq/nostr-docs/commit/fcdc00a564c8d76f094c586b06efce07592a60e4)がデスクトップアプリを追加し、[commit 3977a8e](https://github.com/formstr-hq/nostr-docs/commit/3977a8eb2e62b84a67de756c2776e14de8470927)がネイティブアプリ作業を始め、[commit 413a030](https://github.com/formstr-hq/nostr-docs/commit/413a030f5b47fb8e32a5dff81bcef557ad9b5869)がアプリをoffline-first挙動へ近づけています。エディター側では[commit 1855ce8](https://github.com/formstr-hq/nostr-docs/commit/1855ce86ee83ad504e14e47d9c339baffb114786)がCtrl+S保存、保存警告、link preview修正、strikethrough描画修正を追加しました。

### rust-nostrがNIP-21解析を最適化し、relay側NIP-62サポートを追加

[rust-nostr](https://github.com/rust-nostr/nostr)は8件のPRをマージしました。最も注目すべきは、[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md) URI解析を標準bech32解析性能に合わせる形で`PublicKey::parse`内で最適化する[PR #1308](https://github.com/rust-nostr/nostr/pull/1308)です。以前はNIP-21 URIの解析にraw bech32 keysの約2倍の時間がかかっていました。加えて、このプロジェクトにはmemory、LMDB、SQLite、database test backendsそれぞれへrelay固有の[NIP-62](/ja/topics/nip-62/)（Request to Vanish）サポートを追加する4つのオープンPRもあります（[PR #1315](https://github.com/rust-nostr/nostr/pull/1315)、[PR #1316](https://github.com/rust-nostr/nostr/pull/1316)、[PR #1317](https://github.com/rust-nostr/nostr/pull/1317)、[PR #1318](https://github.com/rust-nostr/nostr/pull/1318)）。

### nostr-toolsがbunker relay制御を追加し、NIP-47 multi-relay parsingを修正

[nostr-tools](https://github.com/nbd-wtf/nostr-tools)は、manual relay management向けにBunkerSignerParamsへ`skipSwitchRelays`を追加する[PR #530](https://github.com/nbd-wtf/nostr-tools/pull/530)と、仕様が許す複数relayに対応するため[NIP-47](/ja/topics/nip-47/)（Nostr Wallet Connect）接続文字列解析を修正する[PR #529](https://github.com/nbd-wtf/nostr-tools/pull/529)をマージしました。

### NostrabilityがSherlock audit dataを統合し、Schemata overviewを公開

[Nostrability](https://github.com/nostrability/nostrability)はNostrクライアント向け相互運用性trackerで、14件のPRをマージしました。[PR #306](https://github.com/nostrability/nostrability/pull/306)はdashboardへSherlock scan statisticsを統合しています。SherlockはNostrabilityの自動監査ツールで、Nostrクライアントへ接続し、公開されたイベントを取得し、各イベントをSchemata JSON Schema定義に照らして検証し、仕様違反を検出します。dashboardは現在、クライアントごとのschema fail rateを表示し（[PR #315](https://github.com/nostrability/nostrability/pull/315)）、開発者が自分のクライアントがどのイベントkindを誤っているかを確認できるようにしています。[PR #323](https://github.com/nostrability/nostrability/pull/323)はNostr publish workflowも刷新し、release announcementを、先行CIステップにキャンセルされない別jobとして実行するようにしました。

elsatは3月30日に、[Schemata for nostr devs](https://njump.me/naddr1qvzqqqr4gupzq96n3hp2vfmf6z2y8uvvxl97xk86kkalnqghx4p25lzl79c76a7yqy2hwumn8ghj7un9d3shjtnyv9kh2uewd9hj7qgwwaehxw309ahx7uewd3hkctcqz4fnx4rkw3x57nrcwdn8zt22xd982jehfptsgqtrww)も公開しました。ここではschemata、schemata-codegen、Sherlockがどう組み合わさるかが説明され、現時点のカバレッジ数、65 NIPsにまたがる179のevent kind schema、154のtag schema、13のprotocol messages、310のsample eventsが示されています。

### Nalgorithmがdigest生成とローカルscore cachingを追加

[Nalgorithm](https://github.com/jooray/nalgorithm)は新しいrelevance-ranked Nostr feedプロジェクトで、今週public developmentを開始しました。[commit cf6c501](https://github.com/jooray/nalgorithm/commit/cf6c501e754ef95a1b4fecc1a76288471a101f43)は、followからpostを取得し、ユーザー定義のpreference promptに照らしてscore付けする初期Webアプリを構築します。[commit 8e931b6](https://github.com/jooray/nalgorithm/commit/8e931b6ae85d470e73603752134ff49b7ba4bb86)はトップランク投稿をspoken-word summaryへ変換するCLI digest toolを追加し、[commit 4cb9c63](https://github.com/jooray/nalgorithm/commit/4cb9c635489a9a3429e8d71f3861dc2a11624153)はfile-based score cachingとrecent likesからのincremental learned-prompt evolutionを追加しました。[commit c2edfb8](https://github.com/jooray/nalgorithm/commit/c2edfb8b89fadbe0028c3f5729bda7e23b2e3c03)は失敗したbatchのfallback scoresをキャッシュしないようにもしており、一時的なscoring failureでpost rankが恒久的に平坦化されることを防いでいます。

### TENEXがRAG vector storeとtargeted MCP startupを追加

[TENEX](https://github.com/tenex-chat/tenex)は、AIエージェントをTelegram経由でNostr channelへ接続するNostrネイティブのagent frameworkで、今週7件のPRをマージしました。[PR #101](https://github.com/tenex-chat/tenex/pull/101)はSQLite-vec、LanceDB、Qdrant backendsを持つpluggable vector store abstractionを追加し、特定のvector databaseに縛られないretrieval-augmented generationをエージェントへ提供します。[PR #102](https://github.com/tenex-chat/tenex/pull/102)はMCP startupをtargeted化し、最初の実行時に全MCPサーバーを起動する代わりに、エージェントが実際に使うtoolsを持つサーバーだけを起動するようにしました。[PR #100](https://github.com/tenex-chat/tenex/pull/100)は`send_message` toolを追加し、Telegram channel bindingを持つagentが、受信メッセージに応答するだけでなく自発的にメッセージをpushできるようにします。[PR #106](https://github.com/tenex-chat/tenex/pull/106)は`.git/HEAD`を直接読むことで、subprocess起動に伴って発生していた9GBのBun/JSCメモリ事前確保を回避しました。

### Dart NDKがAmber signerを移し、Alby Go 1-clickを追加

[Dart NDK](https://github.com/relaystr/ndk)はFlutter向けNostr development kitで、11件のPRをマージしました。[PR #525](https://github.com/relaystr/ndk/pull/525)はAmber signer supportをndk_flutter packageへ移し、[PR #552](https://github.com/relaystr/ndk/pull/552)はsample appにAlby Goのone-click wallet connectionを追加します。[PR #502](https://github.com/relaystr/ndk/pull/502)はCLI向けinstall.sh scriptを追加し、[PR #523](https://github.com/relaystr/ndk/pull/523)はnative asset handlingを優先してRust verifier dependencyを削除しました。

## Protocol and Spec Work

### MarmotがKeyPackagesをアドレス可能イベントへ移し、push notificationsを厳格化

[Marmot specification](https://github.com/marmot-protocol/marmot)は、プロトコルが鍵素材とgroup membershipを扱う方法を変える4件のPRをマージしました。[PR #54](https://github.com/marmot-protocol/marmot/pull/54)はKeyPackageイベントを通常の`kind:443`から`d`タグ付きのアドレス可能`kind:30443`へ移行し、鍵ローテーション時に[NIP-09](/ja/topics/nip-09/)イベント削除を使う必要をなくします。アドレス可能イベントは上書き更新されるため、rotationが自己完結します。[PR #57](https://github.com/marmot-protocol/marmot/pull/57)は非adminユーザーによるSelfRemove proposals（自発的なgroup離脱）コミットを許可し、[PR #62](https://github.com/marmot-protocol/marmot/pull/62)はadminがSelfRemoveを使う前にadmin statusを relinquish することを要求し、高権限を保持したまま消えることを防ぎます。

[PR #61](https://github.com/marmot-protocol/marmot/pull/61)は[MIP-05](/ja/topics/mip-05/) push notification formatも厳格化し、single-blob base64 encoding、versioning、token wire format、x-only key使用法を明示しました。その結果、spec、client libraries、app backendsの間でtoken blobsとx-only keysに対して1つの定義済みwire representationが得られます。これらのspec変更の実装は今週White Noiseスタックへ入り、上の[White Noise v2026.3.23セクション](#white-noiseがrelay-churnを修正しクライアント制御を拡張)で取り上げました。

### NIPアップデート

[NIPsリポジトリ](https://github.com/nostr-protocol/nips)への最近の変更：

**マージ済み：**

- **[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md): 静的ウェブサイト**（[PR #1538](https://github.com/nostr-protocol/nips/pull/1538)）：Blossomストレージを使い、Nostrキーペア配下で静的ウェブサイトをホストするためのkind `15128`（root site）およびkind `35128`（named site）manifestイベントを定義します。詳しくは[下のディープダイブ](#nipディープダイブ-nip-5a静的ウェブサイト)を参照してください。

- **[NIP-30](/ja/topics/nip-30/)（カスタム絵文字）: shortcodeでハイフンを許可**（[PR #2297](https://github.com/nostr-protocol/nips/pull/2297)）：shortcode記述がハイフンを含められるよう更新されました。ハイフン入りshortcodeは実際にはNIP導入当初から使われており、今回の仕様変更は現在の利用実態を文書化するものです。

**オープンPRとディスカッション：**

- **NIP-C1: Agent TUI Messages**（[PR #2295](https://github.com/nostr-protocol/nips/pull/2295)）：暗号化DM経由でagentが対話的UI要素を送るための構造化メッセージ形式を提案しています。typed `text`、`buttons`、`card`、`table` payloadsを含みます。ドラフトは既存の[NIP-17](/ja/topics/nip-17/)および[NIP-04](/ja/topics/nip-04/)ダイレクトメッセージcontent内にJSONとして収め、新しいイベントkindは定義せず、button responsesには単純なcallback文字列形式を使います。

- **NIP-95: Hybrid Peer-to-Peer Relay Protocol**（[PR #2293](https://github.com/nostr-protocol/nips/pull/2293)）：relayが権威を保ちつつ、最近のイベントをWebRTC経由でP2P配布する調整役にもなるハイブリッドrelayモデルを提案します。ドラフトでは`PEER_REGISTER`、`PEER_REQUEST`、`PEER_OFFER`などのrelay messageを導入し、安定したクライアントがSuper Peersとして振る舞い、relayがseed node兼fallbackとなります。

- **NIP-B9: Zap Poll Events**（[PR #2284](https://github.com/nostr-protocol/nips/pull/2284)）：[NIP-88](https://github.com/nostr-protocol/nips/blob/master/88.md)（Polls）が無料ポールをカバーした後、古いNIP-69 zap-poll案を再始動する提案です。ドラフトはkind `6969`のpoll定義とkind `9734`のzapsを投票として使い、経済的Sybil耐性を持つ有料ポーリングシステムにします。無料の1鍵1票ポールを補完します。

- **NIP-AD: Super Zap**（[PR #2289](https://github.com/nostr-protocol/nips/pull/2289)）：relayのpubkeyやクライアントのpubkeyへ送られたzapsを、特化したプロモーションノートとして表示する慣例を提案しています。relayオペレーターやクライアントは`lud16`付きプロフィールを公開し、そのreceiptを取得し、zap description内の埋め込みcontentを抽出し、必要に応じて最小sats閾値でspamを抑制します。

- **NIP-XX: Agent Reputation Attestations**（[PR #2285](https://github.com/nostr-protocol/nips/pull/2285)）：Nostrエージェントに対する構造化reputation attestations向けのparameterized replaceable eventとしてkind `30085`を提案しています。ドラフトは単一のグローバルスコアを避け、reputationを観測者依存とし、古いattestationが薄れていくtemporal decayを追加し、証拠要件付きnegative ratingsをサポートし、より良いSybil耐性に向けた単純weighted scoringとgraph-diversity scoringの両方を概説します。

- **NIP-XX: Paid API Service Announcements**（[PR #2291](https://github.com/nostr-protocol/nips/pull/2291)）：有料HTTP APIsを広告するためのkind `31402`アドレス可能イベントを提案し、発見はNostr、支払いはHTTP 402処理を使います。ドラフトはtags-first設計なので、relayはJSON contentを解析せずに支払い方法、価格、能力でfilterできます。また任意でrequest/response schemaも許可し、クライアントやagentが呼び出しを自動生成できるようにします。

- **NIP-XX: SplitSigを使うLNURL-authからの鍵導出**（[PR #2294](https://github.com/nostr-protocol/nips/pull/2294)）：LNURL-authのECDSA署名とクライアント側ランダムnonceを組み合わせてNostrキーペアを導出する提案です。導出式は`nsec = SHA256(ecdsa_signature || nonce)`です。サーバーはECDSA署名（LNURL-auth handshakeに内在）を見ますがnonceは見ず、ブラウザはnonceを生成しますが署名は制御しません。どちらの断片だけでもnsecは導出できません。狙いは、同じLightning walletがデバイス間で同じNostr鍵を生み、walletがrecovery anchorとなり、どのサーバーも秘密鍵を再構築できないことです。

- **[NIP-55](/ja/topics/nip-55/): rejected fieldの文書化**（[PR #2290](https://github.com/nostr-protocol/nips/pull/2290)）：intentベース署名者レスポンスの`rejected`フィールドを文書化し、[Amethyst v1.07.xの修正](#amethystがピン留めノートrelay管理request-to-vanishを出荷)が回避しなければならなかった挙動を正式化します。

## NIPディープダイブ: NIP-5A（静的ウェブサイト）

[NIP-5A](https://github.com/nostr-protocol/nips/blob/master/5A.md)は、署名済みイベントを配信されるWebページへ変えるために、2つのイベントkindと既存blob storageインフラを使って、Nostrキーペア配下で静的ウェブサイトをホストする方法を定義します。[仕様](https://github.com/nostr-protocol/nips/blob/master/5A.md)は3月25日に[PR #1538](https://github.com/nostr-protocol/nips/pull/1538)経由でマージされました。

このモデルでは、pubkeyごとに1つのroot site用にkind `15128`、`d`タグで識別されるnamed sites用にkind `35128`を使います。各manifestは絶対URL pathをSHA256 hashへマッピングします。以下はroot site manifestの例です。

```json
{
  "id": "5324d695ed7abf7cdd2a48deb881c93b7f4e43de702989bbfb55a1b97b35a3de",
  "pubkey": "266815e0c9210dfa324c6cba3573b14bee49da4209a9456f9484e5106cd408a5",
  "created_at": 1743465600,
  "kind": 15128,
  "tags": [
    ["path", "/index.html", "186ea5fd14e88fd1ac49351759e7ab906fa94892002b60bf7f5a428f28ca1c99"],
    ["path", "/about.html", "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456"],
    ["path", "/favicon.ico", "fedcba0987654321fedcba0987654321fedcba0987654321fedcba0987654321"],
    ["server", "https://blossom.primal.net"],
    ["title", "My Nostr Site"],
    ["description", "A static website hosted on Nostr"],
    ["source", "https://github.com/lez/nsite"]
  ],
  "content": "",
  "sig": "f4e4a9e785f70e9fcaa855d769438fea10781e84cd889e3fcb823774f83d094cf2c05d5a3ac4aebc1227a4ebc3d56867286c15a6df92d55045658bb428fd5fb5"
}
```

配信フローは3段階です。ホストサーバーがHTTP requestを受け取り、subdomainから著者のpubkeyを抽出します（root sitesならnpub、named sitesならbase36エンコードpubkey）。次に、著者のrelay listを[NIP-65](/ja/topics/nip-65/)経由で取得し、site manifestを問い合わせます。manifestが見つかると、サーバーは要求されたpathをcontent hashへ解決し、`server` tagsに列挙されたBlossomサーバーから対応blobをダウンロードして返します。

DNS subdomain formatは厳密に指定されています。root sitesは標準npubをsubdomainに使います。named sitesは、生のpubkeyの50文字base36 encodingに続けて`d`タグ値を1つのDNS labelに収めます。DNS labelは63文字制限があり、base36 encodingは常に50文字を使うため、`d`タグは13文字に制限されます。仕様はさらに、`d`タグが`^[a-z0-9-]{1,13}$`に一致し、ハイフンで終わらないことを要求しており、DNS解決の曖昧さを防ぎます。

content hashを使うことで、同じサイトを異なるhost serversから配信でき、file integrityもサーバーを信用せずに検証できます。host serverはファイルを自前で保存する必要がありません。manifest内hashを使って必要時にBlossomから取得するだけです。つまり、作者が何を配信するかを制御し、Blossom serverが生ファイルを保持し、host serverは両者を接続するだけです。この3要素はそれぞれ独立に交換可能です。

既存実装には、manifestを解決してファイルを配信するhost server[nsite](https://github.com/lez/nsite)と、manifestの構築と公開を行うUI[nsite-manager](https://github.com/hzrd149/nsite-manager)があります。仕様にはサイトのsource code repositoryへのリンク用`source`タグも追加され、別途[PR #2286](https://github.com/nostr-protocol/nips/pull/2286)でマージされたREADME更新では、kind `15128`と`35128`の両方がNIP kind indexへ登録されました。

## NIPディープダイブ: NIP-62（Request to Vanish）

[NIP-62](https://github.com/nostr-protocol/nips/blob/master/62.md)は、要求したpubkeyからのすべてのイベントをrelayが削除するよう求めるkind `62`イベントを定義します。[仕様](https://github.com/nostr-protocol/nips/blob/master/62.md)の動機は法的なものです。忘れられる権利のある法域では、標準化され署名された削除要求があれば、relayオペレーターは行動すべき明確なシグナルを得られます。

```json
{
  "id": "a7b8c9d0e1f23456789012345678901234567890abcdef1234567890abcdef12",
  "pubkey": "f1e2d3c4b5a697887766554433221100ffeeddccbbaa99887766554433221100",
  "created_at": 1743465600,
  "kind": 62,
  "tags": [
    ["relay", "wss://relay.example.com"]
  ],
  "content": "Requesting deletion of all events from this relay.",
  "sig": "11aa22bb33cc44dd55ee66ff77889900aabbccddeeff0011223344556677889911aa22bb33cc44dd55ee66ff77889900aabbccddeeff00112233445566778899"
}
```

この仕様は、targeted vanish requestとglobal vanish requestを分けています。targeted requestは、どのrelayが対応すべきかを示す具体的な`relay`タグを含みます。global requestは、relayタグ値として文字列`ALL_RELAYS`を使い、そのイベントを見るすべてのrelayに対して、そのpubkey由来のすべてのイベント削除を求めます。準拠するrelayは、削除済みイベントが再びrelayへ再放送されないことも保証しなければならず、削除はstickyである必要があります。

NIP-62は、範囲と意図の両面で[NIP-09](/ja/topics/nip-09/)（イベント削除）を超えます。NIP-09は個別イベントを削除でき、relayは準拠してもしなくてもよい仕様です。NIP-62はすべての削除を要求し、仕様はURLがタグ付けされたrelayに対してMUST準拠を求めています。さらに、要求pubkeyをp-tagした[NIP-59](/ja/topics/nip-59/)（Gift Wrap）イベントも削除するようrelayに求めているため、受信DMもユーザー自身のイベントと一緒に消されます。NIP-62 vanish requestに対してNIP-09削除イベントを公開しても効果はありません。いったんvanishした後で、vanish request自体を削除してun-vanishすることはできません。

今週、[Amethyst v1.07.0](#amethystがピン留めノートrelay管理request-to-vanishを出荷)はクライアント側のNIP-62サポートを出荷し、ユーザーがアプリからvanish requestを開始できるようにしました。relay側では、[rust-nostr](https://github.com/rust-nostr/nostr)が、memory、LMDB、SQLite、database test backendsそれぞれにNIP-62を追加する4つのオープンPRを抱えています（[PR #1315](https://github.com/rust-nostr/nostr/pull/1315)、[PR #1316](https://github.com/rust-nostr/nostr/pull/1316)、[PR #1317](https://github.com/rust-nostr/nostr/pull/1317)、[PR #1318](https://github.com/rust-nostr/nostr/pull/1318)）。クライアントサポートとrelayサポートが同じ週に進んでいるわけです。

この設計は実務的な緊張も生みます。Nostrの価値提案には検閲耐性が含まれ、relayは公開を妨げるべきではありません。一方でNIP-62は、特定pubkeyからの再公開をrelayがMUST防ぐケースを導入します。両者が両立するのは、この要求が自己指向だからです。あなたが求めているのは他人のイベント削除ではなく、自分自身のイベント削除です。検閲耐性は、明示的にオプトアウトした本人以外についてはそのまま保たれます。

---

今週は以上です。何か作っているものや共有したいニュースがあれば、<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">[NIP-17](/ja/topics/nip-17/)（プライベートダイレクトメッセージ）DMでご連絡ください</a>。Nostr上でもお待ちしています。
