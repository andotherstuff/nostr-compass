---
title: "Nostr Compass #38"
date: 2026-09-02
publishDate: 2026-09-02
translationOf: /en/newsletters/2026-09-02-newsletter.md
translationDate: 2026-09-02
draft: false
type: newsletters
description: "Voca 1.0がオフラインのテキスト読み上げアプリに検証済みNostr閲覧をもたらし、nostreamがrelay側のジョブルーティングと認証を拡張、NapstrがTorベースの音声カタログを公開、MDK 0.9.17がグループ保守コストを削減し、NIPs本体がページネーションのヒントとハイライトtagをNWCの取引総数とともにマージし、NIP詳細解説がリポストとリアクションを説明します。"
---

[Nostr Compass](https://nostrcompass.org)へようこそ。Nostrの週刊ガイドです。

**今週:** [Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en) 1.0が、記事を読み上げるオフラインAndroidリーダーに検証済みNostrノートと長文subscriptionをもたらします。[nostream](https://github.com/cameri/nostream)はrelay側のジョブルーティングと認証付き運用を拡張し、[NDK for Dart](https://github.com/relaystr/ndk)はnegentropyと複数relayリクエストの生存期間を修正し、[Divine Mobile](https://github.com/divinevideo/divine-mobile)はラップされたメッセージの削除と署名を決定論的にし、[Conduit Relay](https://github.com/Conduit-BTC/conduit-relay)は既定でgift wrapのinboxを保護し、[Amethyst](https://github.com/vitorpamplona/amethyst)は可搬なハイライトを出荷し、[Mostro](https://github.com/MostroP2P/mostro)はスパムゲートの前に署名済み注文を検証します。[Napstr](https://github.com/lnbits/napstr)はファイルをTor経由で転送しながら、音声カタログとseederのheartbeatをNostr上で公開します。リリースは[MDK](https://github.com/marmot-protocol/mdk)と[pakstr](https://git.nostrdev.com/stuff/pakstr)を扱います。protocol関連では、[NIPsリポジトリ](https://github.com/nostr-protocol/nips)が[NIP-67](/ja/topics/nip-67/)のページネーションヒントと[NIP-84](/ja/topics/nip-84/)のハイライトtag方式をマージし、[Nostr Wallet Connect](https://github.com/nostr-wallet-connect/nwc)が取引総数を追加します。NIP詳細解説では、リポストとリアクションをevent形式と現在の実装にわたってたどります。

## トップストーリー

### Voca 1.0が検証済みNostrノートとsubscriptionをAndroidで読み上げ

[Voca](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en)は、読み上げ中の文をページ上で強調表示しながら、記事、PDF、Markdownファイル、Nostrノートを端末自身のテキスト読み上げ音声で再生するオフラインAndroidリーダーです。独自の[プロジェクト鍵](https://njump.me/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu)で[2026-08-27に公開された](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en)[1.0リリース](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en)は、Nostrを第一級の情報源にします。ノートアドレス、event識別子、npub、プロフィール、またはNostrエンティティを含む通常のwebリンクを貼り付けると、アプリは参照をデコードし、署名済みeventをrelayから取得し、その周囲に作られたwebページではなく著者のテキストを読み上げます。

Nostr統合は、[Vocaの署名済み1.0告知](https://njump.me/naddr1qq98vmmrvyknzt3s9ccqyg84e2v65erlexz84kmpkmkjqrvmzkgf8fdewfkyun3tnxlel5er3upsgqqqw4rsw0l3en)に記載された2つの検証済み挙動で定義されます。第一に、取得したすべてのeventは保存前に、再計算したidとBIP-340 Schnorr署名に対して検証されます。その際、ブートストラップrelay、著者の[NIP-65](/ja/topics/nip-65/) relayリスト（著者が読み書きするrelayを列挙する、署名済みでreplaceableなkind `10002` event）、参照自体に含まれるヒントを使います。そのためrelayは応答を拒めても、著者が言っていない内容を捏造できません。第二に、著者のnpubを追加すると、その著者の[NIP-23](/ja/topics/nip-23/)長文記事（タイトル、概要、画像を持つaddressableなkind `30023`投稿）が、RSSおよびAtomフィードと並ぶ端末上の単一inboxに入ります。2026-08-28に[告知され](https://gitworkshop.dev/npub17h9fn2ny0lycg7kmvxmw6gqdnv2epya9h9excnjw9wvml87nyw8sqy3hpu/voca)、2026-08-29に[Zapstore](https://zapstore.dev)へ公開された1.1.0更新は、文単位のスクロールをタイミングに合わせ、長い文書の動作を滑らかにし、手動スクロール、サイズ変更、プロセス再起動、アップグレード後にホーム画面widgetを復旧します。


### nostreamがrelay側のDVMルーティングと認証付き運用を拡張

[8月19日のジョブ取り込み作業](/en/newsletters/2026-08-19-newsletter/#nostream-adds-a-relay-monitor-and-mints-invite-codes)に続き、TypeScript製relay実装の[nostream](https://github.com/cameri/nostream)は、[NIP-89 application handler eventを保存して配信します](https://github.com/cameri/nostream/pull/737)。[NIP-89](/ja/topics/nip-89/)（application handler discovery）はkind `31989`の推薦とkind `31990`のhandler情報を使います。どちらもすでにparameterized-replaceable範囲にあるため、クライアントはそれらのkindを問い合わせ、`d` tagが衝突したときに置き換えを受け取れます。relayは自身のworkerについてhandler情報を公開しません。

保留中の[NIP-90](/ja/topics/nip-90/)（data vending machine）ジョブは、いまや[workerプロセスへ届き、結果eventとして戻ります](https://github.com/cameri/nostream/pull/734)。成功時にはrelayが自身の鍵でkind 6000〜6999の結果に署名します。タイムアウトまたはworkerのクラッシュ時には、送信済みのまま放置せずジョブを失敗として記録します。

認証済みセッションと管理用HTTP呼び出しは、異なる境界に置かれます。[NIP-42](/ja/topics/nip-42/)（クライアントからrelayへの認証）は[socketごとに認証済みpubkeyを追跡し](https://github.com/cameri/nostream/pull/716)、クライアントがeventを公開する前にAUTHを要求でき、その要件を[NIP-11](/ja/topics/nip-11/)（relay情報）文書で告知します。両方の制御は既定で無効です。これとは別に、[管理API routeはNIP-98署名済みHTTP認可を受け入れられます](https://github.com/cameri/nostream/pull/730)。[NIP-98](/ja/topics/nip-98/)（署名済みeventによるHTTP認証）は、運用者が有効にして許可するpubkeyを指定するまで無効のままです。

### NDK for Dartがnegentropy、複数relayリクエストの生存期間、署名検証を修正

Nostr向けDart開発キットの[NDK](https://github.com/relaystr/ndk)で[NIP-77](/ja/topics/nip-77/)（negentropyによる集合照合）を実行すると、codecが[negentropy](/ja/topics/negentropy/) protocol v1に対応していなかったため、エラーを出さず誤った保有集合と必要集合を返していました。[v1エンコード修正](https://github.com/relaystr/ndk/pull/722)により、relayが保有するidと、まだ必要とするidが正しく返るようになりました。

異なるrelayへ送られた同一filterが[1つのリクエストに畳み込まれていました](https://github.com/relaystr/ndk/pull/705)。同じfilterを持つリクエストでも、対象relayまたは生存期間が異なれば別々に保たれるため、短いqueryに別のrelayのeventが混ざったり、継続中のsubscriptionが停止したままになったりしません。

同じキットは[署名を一度検証し、その結果を保持します](https://github.com/relaystr/ndk/pull/726)。後から重複して配信されても再度の検証コストはかからず、保存済みの検証済みeventも上書きされません。

### Divine Mobileがラップされたダイレクトメッセージの削除と署名を決定論的に

Nostr経由で公開するモバイル短編動画クライアント[Divine Mobile](https://github.com/divinevideo/divine-mobile)では、メッセージを対象にする、ラップされた[NIP-09](/ja/topics/nip-09/)（event削除要求）のkind `5` eventが適用されていませんでした。クライアントは、リアクションでないものを処理済みと扱う代わりに、[各削除を指定されたメッセージに対して解決するようになりました](https://github.com/divinevideo/divine-mobile/pull/8174)。最初の処理中に2件目の[全員から削除する要求](https://github.com/divinevideo/divine-mobile/pull/8164)を出すと、以前はエラーもwire上のkind `5`もないまま消えていましたが、並行する削除はいまやそれぞれ公開されます。

以前扱った1.0.22リリース後、同じ1対1の[NIP-17](/ja/topics/nip-17/)（gift wrapされた非公開DM）テキストを1秒以内に2回送ると[同じrumor idが作られ](https://github.com/divinevideo/divine-mobile/pull/8163)、2回目が消えていました。各送信はいまや[NIP-59](/ja/topics/nip-59/)（gift wrap）のrumor内にtokenを持ち、idが異なります。

kind `4`またはkind `5` eventに呼び出し側がすでに署名していた場合、その[署名が保持されるようになりました](https://github.com/divinevideo/divine-mobile/pull/8173)。以前は後からclient tagが追加されてidが変わり、relayがeventを無効として拒否していました。

### Conduit RelayがNIP-42保護inboxを強化

Kind `1059` gift wrapは1人の受信者向けに保存されます。それらのwrapを受信者保護inboxに保つGo製relayの[Conduit Relay](https://github.com/Conduit-BTC/conduit-relay)は、[既定で強制モードになります](https://github.com/Conduit-BTC/conduit-relay/pull/8)。kind `1059`のqueryは、その受信者としての[NIP-42](/ja/topics/nip-42/)認証を提示しなければrelayに拒否されます。それらのwrapに対する複数kindのfilter、wildcard、count、[negentropy](/ja/topics/negentropy/)は`restricted`であるため、別人のAUTHで他人のinboxを丸ごと取得することはできません。

同じ[保護inboxのマージ](https://github.com/Conduit-BTC/conduit-relay/pull/8)は、送信されたAUTH eventに正規のevent idを要求し、それ以外が有効なNIP-42 eventなら`content`が空かどうかにかかわらず受け入れます。challenge-onlyは読み取りを妨げずAUTHを提示し、disabledは自由に許可します。ライブラリの既定値はenforceです。

### AmethystがNIP-84ハイライトを出荷し、relay関連の2つの障害経路を修正

先週の[Blossom認可作業](/en/newsletters/2026-08-26-newsletter/#amethyst-moves-blossom-authorization-off-image-loading-threads)に続き、Android Nostrクライアントの[Amethyst](https://github.com/vitorpamplona/amethyst)は、[NIP-84](/ja/topics/nip-84/)（可搬なハイライト）を備えた[v1.14.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.14.0)を出荷しました。選択した一節は、composer、ハイライトフィード、またはアプリへの共有からkind `9802` eventになります。

このリリースは[NIP-29](/ja/topics/nip-29/)のchannel削除・アーカイブ制御（[PR #3812](https://github.com/vitorpamplona/amethyst/pull/3812)）を追加し、クライアントがすでに行う通信からrelayの挙動を測定したうえで、それらの[NIP-66](https://github.com/nostr-protocol/nips/blob/master/66.md) probeをstreaming、read、write、URLの検査へ拡張します（[PR #3836](https://github.com/vitorpamplona/amethyst/pull/3836)、[PR #3857](https://github.com/vitorpamplona/amethyst/pull/3857)）。AmethystはさらにSharedKeyCacheのハッシュ衝突脆弱性を除去し、メッセージ認証コードを定数時間で比較し（[PR #3833](https://github.com/vitorpamplona/amethyst/pull/3833)）、接続時のAUTH配信を失い得る競合を修復し（[PR #3838](https://github.com/vitorpamplona/amethyst/pull/3838)）、subscription状態のlockをstripingしてANRの連鎖を解消し（[PR #3851](https://github.com/vitorpamplona/amethyst/pull/3851)）、最初のものだけでなくすべてのsubscription filterを比較します（[PR #3856](https://github.com/vitorpamplona/amethyst/pull/3856)）。

[Newsletter #36では、これらのrelay認証、バックアップ、公開チャットの変更を以前に扱いました](/en/newsletters/2026-08-19-newsletter/#amethyst-rebuilds-its-relay-authentication-decision-flow)。v1.14.0はいま、それらをまとめて出荷しています。Concordのsoft banは監査で見つかった権限の穴を塞ぎます（[PR #3885](https://github.com/vitorpamplona/amethyst/pull/3885)）。relay認証はpermission flowを再設計し（[PR #3899](https://github.com/vitorpamplona/amethyst/pull/3899)）、タイムアウトせずchallengeの解決を待ち（[PR #3905](https://github.com/vitorpamplona/amethyst/pull/3905)）、新規アカウントは既定で認証し（[PR #3931](https://github.com/vitorpamplona/amethyst/pull/3931)）、アカウントの通常の集合外にあるrelayでもその設定を尊重し（[PR #3937](https://github.com/vitorpamplona/amethyst/pull/3937)）、再接続をまたいでセッション許可を保ちます（[PR #3955](https://github.com/vitorpamplona/amethyst/pull/3955)）。案内付きの初回起動と設定flowは鍵のバックアップを見つけやすくし（[PR #3909](https://github.com/vitorpamplona/amethyst/pull/3909)）、Cashu proofのbackfillと履歴のページ送りはwallet残高が途中で切れるのを防ぎ（[PR #3941](https://github.com/vitorpamplona/amethyst/pull/3941)）、公開チャットをミュートできるようにします（[PR #3939](https://github.com/vitorpamplona/amethyst/pull/3939)）。

そのtagの後、kind `30392`〜`30395`の[trusted list](https://github.com/vitorpamplona/amethyst/pull/3983)は、タイトルだけが[NIP-50](/ja/topics/nip-50/)（全文検索）でindexされます。そのため本文で名前が挙がったlistを、メンバーの16進idをindexせずに見つけられます。[NIP-47](/ja/topics/nip-47/)（Nostr Wallet Connect）経由で届いたwalletの拒否は、[タップしても何も起きなかったように見える代わりにエラーを表示するようになりました](https://github.com/vitorpamplona/amethyst/pull/3987)。`QUOTA_EXCEEDED`と`RESTRICTED`に加え、walletが応答しない場合のタイムアウトも含まれます。

### Mostroが高コストな処理の前に署名済み注文を検証し、注文監査eventを保持

[v0.18.1のCashu escrow基盤](/en/newsletters/2026-08-12-newsletter/#mostro-0181-starts-a-cashu-escrow-path-and-hardens-the-daemon)に続き、Nostr上で注文を調整するピアツーピア交換daemonの[Mostro](https://github.com/MostroP2P/mostro)は、transportの既定値を[NIP-44](/ja/topics/nip-44/)（ペイロード暗号化）とし、gift wrapを明示的なopt-inとして保つ[v0.18.5](https://github.com/MostroP2P/mostro/releases/tag/v0.18.5)をtag付けしました。

このリリースは、maker bondが誤った時計で没収されないよう待機状態のタイムアウトを記録済みのtake時刻に固定し（[PR #879](https://github.com/MostroP2P/mostro/pull/879)）、成立済み注文の買い手への支払いを多くても1回だけ実行し（[PR #881](https://github.com/MostroP2P/mostro/pull/881)）、それらの支払いを上限付きでnon-blockingな`send_payment`待機へ移します（[PR #883](https://github.com/MostroP2P/mostro/pull/883)）。タイムアウト没収の勝者へ支払う変更の試み（[PR #875](https://github.com/MostroP2P/mostro/pull/875)）は、同じtagの出荷前に取り消されました（[PR #885](https://github.com/MostroP2P/mostro/pull/885)）。Mostroはさらに、変更のない保留中の注文一覧を毎時および起動時に再公開するのをやめ（[PR #888](https://github.com/MostroP2P/mostro/pull/888)）、kind `38386`の紛争eventは下流の並べ替え用に`created_at` tagを持つようになりました（[PR #878](https://github.com/MostroP2P/mostro/pull/878)）。

そのtagの後、[署名検証がスパムゲートより前に実行されるようになりました](https://github.com/MostroP2P/mostro/pull/892)。event idは`sig`をcommitしないため、被害者のkind `14`を壊れた署名とともに複製するとreplay slotを占有し、正しいメッセージを黙って捨てられました。daemonは先に検証し、無効なwrapについて警告して処理を続けるのではなく破棄します。

kind `8383`の手数料監査eventは、15日間の[NIP-40](/ja/topics/nip-40/)（有効期限timestamp）を持っていました。いまは公開の支払い記録という役割に合わせ、[1年間の有効期限を保ちます](https://github.com/MostroP2P/mostro/pull/924)。Cashu対応nodeでは、注文の引き受け時に[2-of-3 escrowをlockするようNostr経由で売り手に要求し](https://github.com/MostroP2P/mostro/pull/830)、待機中の注文eventを公開し、Lightning hold invoiceの作成を省きます。これはrequest経路を完成させますが、それだけですべてのescrowや市場悪用の問題を解決するものではありません。

### Napstrが音声カタログをNostr上で公開し、ファイルをTor経由で転送

[Napstr](https://github.com/lnbits/napstr)は、検索可能なカタログと稼働中のseederをNostr上で公開し、直接IPへのfallbackなしに同梱のTorプロセスでファイルを転送するデスクトップ音声共有クライアントです。[バージョン0.2.0](https://github.com/lnbits/napstr/releases/tag/v0.2.0)はプロフィールとカタログmetadataを公開のまま保ち、request、転送credential、ファイル内容、peer IPアドレスはrelayへ送りません。

ディスカバリは[Napstrリポジトリ](https://github.com/lnbits/napstr)の2種類のaddressable event kindを使います。kind `30421`のカタログ項目はSHA-256 digest、公開basename、サイズ、音声formatでファイルを示し、著者はその座標を削除markerで置き換えてファイルを取り下げます。kind `30422`のavailability heartbeatは10分後に期限切れとなり、著者がseedする用意のあるファイルidを列挙します。そのためカタログの行が有効なのは、期限内のheartbeatがそのdigestをまだ含む間だけです。

公開の会話には、relay所有のグループではなく[NIP-C7](/ja/topics/nip-c7/)（kind 9のチャットメッセージ）を使います。[Napstrリポジトリ](https://github.com/lnbits/napstr)は、共有の公開roomと、ファイルdigestを鍵にしたtrackごとの議論を定義します。それらのメッセージは署名済みで公開されます。onionアドレス、転送credential、ファイルbyte列は含みません。

ダウンロードは[NIP-17](/ja/topics/nip-17/)（gift wrapされた非公開DM）による交渉として始まります。[Napstrリポジトリ](https://github.com/lnbits/napstr)はrequest、offer、refusalをkind `14` rumor内にwrapするため、relayには一時的なv3 onion hostnameも、承諾したofferが返す1回限りのcapabilityも見えません。その後、同梱のTorがそのonion経由でbyte列を転送し、完全なSHA-256 digestを検証し、ファイルを再生可能にする前に音声を再検証します。

[v0.1.7からv0.2.0の比較](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0)では、audiobook collectionと任意のAndroid companionであるNapstrfyが追加されています。kind `30423`のmanifestは、通常のカタログファイルのままである章を順番に列挙するため、collectionを無視するクライアントも各章を取得できます。Napstrはそのために、既存内容を壊さないローカルAudiobooksフォルダを作ります。Napstrfyは1回限りのQR codeで稼働中のデスクトップとpairingし、デスクトップの秘密鍵を受け取ることなく、既存のNostrおよびTorサービスを通じて検索とダウンロードrequestを行います。

同じ[比較](https://github.com/lnbits/napstr/compare/v0.1.7...v0.2.0)では、完了しないcompanion handshakeがタイムアウトします。seederは配信前に共有ファイルを複製してhash化し、受信データを非公開の一時ファイルへ書き込み、audiobookの保存先をNapstrフォルダの実在する子要素に限定し、転送中に保存先が変わった場合は中止します。

## リリース

### MDK v0.9.17: 最新のKeyPackage、メンバーシップ活動、永続的な送信

[Newsletter #37ではMDK 0.9.14と0.9.15を扱いました](/en/newsletters/2026-08-26-newsletter/#mdk-v0914-and-v0915-keypackage-selection-epoch-gap-recovery-and-split-relay-roles)。これには[MDKリポジトリ](https://github.com/marmot-protocol/mdk)で、KeyPackage選択を古い順から最新の有効な現行プロフィール用packageへ変更したこと、epoch gapの復旧gate、アカウントcleanup、discovery relayとoperational relayの分離が含まれます。これらの修正は続く2リリースの基盤であり続けるため、すでに利用可能なpackageを公開したメンバーを古いpackageが妨げることはなくなりました。

[メンバーシップと管理eventも、新しいメッセージと同様にチャット一覧を進めるようになりました](https://github.com/marmot-protocol/mdk/pull/1551)。参加、退出、role変更時にpreview text、並び順、未読数、既読markerが更新され、ローカルsystem actorはNostrプロフィールとして扱われません。再接続と再起動は、[再試行される永続的な送信テキストに1つの送信identityを再利用する](https://github.com/marmot-protocol/mdk/pull/1516)ため、同じグループメッセージが2回公開されることはありません。

その後の2リリースは、大規模グループを健全に保つコストに集中しています。[バージョン0.9.16](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.16)は[high-water markではなく現在のepochからepoch divergenceを測定し](https://github.com/marmot-protocol/mdk/pull/1559)、拒否した受信eventを取得可能なまま保ち（[PR #1565](https://github.com/marmot-protocol/mdk/pull/1565)）、replay rollbackを正規のグループ状態に限定し（[PR #1563](https://github.com/marmot-protocol/mdk/pull/1563)）、hostがengineを直接埋め込める、UniFFI binding上のmacro生成C ABIである[marmot-c](https://github.com/marmot-protocol/mdk/pull/1545)を導入します。[バージョン0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.17)は次に、pass-admission scanを[メンバーごとのpassではなく1回のmember walkにまとめ](https://github.com/marmot-protocol/mdk/pull/1617)、[完全な履歴graphをseedせずグループ状態が競合しているか調べ](https://github.com/marmot-protocol/mdk/pull/1620)、[deferred-peel sweepのidle pollコストを削減し](https://github.com/marmot-protocol/mdk/pull/1621)、[最初のpassで漏れた3つのprojection箇所にbatched component readを適用します](https://github.com/marmot-protocol/mdk/pull/1622)。対応する[marmot-c 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/marmotc-v0.9.17)と[WN Agent 0.9.17](https://github.com/marmot-protocol/mdk/releases/tag/wn-agent-v0.9.17)のartifactは同じcommitからbuildされるため、埋め込み側は低コストな保守経路をまとめて得られます。


### pakstr v0.16.0: 公開時にkind-32267識別子を表示

[先週の0.13.0から0.15.0までのZapstore公開pipeline](/en/newsletters/2026-08-26-newsletter/#pakstr-0130-through-0150-makes-zapstore-publication-explicit)に続き、webアプリを署名済みAndroid APKへpackage化し、Nostr鍵で公開するCLIの[pakstr](https://git.nostrdev.com/stuff/pakstr)は、検索、公開、置き換えの対象となる[kind `32267` application-eventのIDをlogへ記録します](https://git.nostrdev.com/stuff/pakstr/pulls/67)。[バージョン0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0)は、古いlisting metadataによって再公開するとき、以前のIDと新しいIDの両方を出力するため、発行者はrelay上でどのlisting eventが有効か確認できます。

同じ[識別子log](https://git.nostrdev.com/stuff/pakstr/pulls/67)は、置き換え前に検索で見つかったIDを記録し、次に公開されたeventのIDを記録します。そのため何も変更せず再利用した場合は同じIDが繰り返し表示されます。これが[0.16.0](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.16.0)でtag付けされた変更です。Content-Digest、upload前の公開、発行者検証の挙動は以前のtagですでに出荷されています。

## 未リリースの変更

### Zap Cookingがbunker relayを限定し、有料endpointへ署名を要求

Nostr長文event上に構築されたrecipeサイト[Zap Cooking](https://github.com/zapcooking/frontend)でbunker sessionを再読み込みすると、暗号化された[NIP-46](/ja/topics/nip-46/)（relay経由のremote signing）の会話が、以前はページですでに使っているすべてのrelayへ公開されていました。[signer通信をbunker自身のrelayへ限定する](https://github.com/zapcooking/frontend/pull/633)ことで、session復元時と、signer主導の接続flowであるnostrconnect pairing時にも、bunker URLによるlogin経路と同じ制限が適用されます。不正な保存recordから空のrelay集合を設定することは拒否されるため、recipeだけをhostするrelayが、同じpubkeyで稼働中のbunker sessionを保っていると知ることはなくなりました。

[署名済みHTTP認証](https://github.com/zapcooking/frontend/pull/630)が、[NIP-98](/ja/topics/nip-98/)（署名済みNostr eventによるHTTP認証）の下で、有料の料理assistant chat、cookbookの導入、gate付きrecipe更新を保護するようになりました。serverはrequest bodyを一度だけ読み、その正確なpayloadに対して署名を検証し、bodyで渡された公開鍵ではなく検証済みauth eventからidentityを得ます。chat previewはheaderなしでも動きますが、提示された署名が無効なら拒否され、cookbookの導入には常に署名が必要です。gate付きrecipeの更新では、検証済み鍵が保存済み著者と一致することも求めるようになりました。それ以外の人にはrecipeが存在しないと伝えるため、どの有料recordが存在するかをendpointが明かしません。

### nostrordがラップされたDMと共有eventリンクを修復

先週の[v2.9.0](/en/newsletters/2026-08-26-newsletter/#nostrord-v290-relay-scoped-group-state-and-media)に続き、relay host型コミュニティ向けのクロスプラットフォームクライアント[nostrord](https://github.com/nostrord/nostrord)は、ある端末から送った[NIP-17](/ja/topics/nip-17/)（gift wrapされた非公開DM）が同じアカウントの別端末へ届くよう配信修正をマージしました。[送信者自身へのcopyを独立に公開する](https://github.com/nostrord/nostrord/pull/295)ことで、受信者向けwrapが最初のrelayに受理されたとき、他端末が取得するcopyまで落ちることを防ぎます。同じ変更は[NIP-42](/ja/topics/nip-42/)（クライアントからrelayへの認証）の完了後にwrapを再送し、最初のrelayが受理した時点で送信を成功と記録するため、1つのhostの障害が残りを止めることはありません。[NIP-59](/ja/topics/nip-59/)（gift wrap）の復号に失敗して保留されたgift wrapの[再試行](https://github.com/nostrord/nostrord/pull/297)はいまやtimerで行われるため、接続を保つbunkerでそれらのメッセージが未…［省略］

[NIP-C7](/ja/topics/nip-c7/)（kind `9`チャットメッセージ）の返信は、`q` tagと並べて、親を先頭の[NIP-19](/ja/topics/nip-19/)（bech32エンコードされたエンティティ）`nevent` pointerとして繰り返します。本文の先頭にあり返信先を示す場合に[その親pointerを取り除く](https://github.com/nostrord/nostrord/pull/292)ことで、行は単一の返信quoteとして描画されます。一方、本文途中のpointerや本文全体を占めるpointerは、引き続きquote cardとして描画されます。[引用eventリンクは`nevent`をエンコードするようになり](https://github.com/nostrord/nostrord/pull/293)、著者、kind、quoteを読んだrelayを含むため、DMへ共有された[NIP-29](/ja/topics/nip-29/)（relay管理グループ）eventを、検索ヒントのない裸のnote識別子ではなく別のクライアントから取得できます。

## NIP更新とprotocol仕様作業

### Nostr実装の可能性

今週、中心となる[NIPsリポジトリ](https://github.com/nostr-protocol/nips)に2件の仕様変更がマージされました。

[NIP-67](/ja/topics/nip-67/)は、relayが`EOSE`（保存済みeventの終端）メッセージへ付加できるヒントを定義し、クライアントがページ送りを続けるべきか判断できるようにします。マージされた[`"auth"`ヒント](https://github.com/nostr-protocol/nips/pull/2371)は、`finish`と`more`に続く3つ目の値を追加します。relayは、ユーザーが認証すれば追加の保存済みeventが見える可能性を通知でき、そのヒントを持つ`EOSE`より前に[NIP-42](/ja/topics/nip-42/)（relay認証）の`AUTH` challengeを送らなければなりません。[付随するNIP-42の追加](https://github.com/nostr-protocol/nips/pull/2371)はクライアント側からも同じflowを定義します。そのため`auth`付きの`EOSE`を受け取ったクライアントは、応答に必要なchallengeをすでに持っています。

[NIP-84](/ja/topics/nip-84/)（可搬なハイライト、上でAmethystが対応を出荷したkind `9802` event）は[tag方式の更新をマージしました](https://github.com/nostr-protocol/nips/pull/2454)。ハイライトはNostr event向けの`a`/`e` tag、その他向けの`r` tagに加え、[NIP-73](/ja/topics/nip-73/)（外部コンテンツ識別子）に従う構造化された`i` tagで出典を示せるようになりました。またquoteハイライトは、quote repostのように描画することがMUSTからSHOULDへ変わりました。

### Nostr Wallet Connect

`list_transactions`の応答は、現在のページが返した行数ではなく、requestに一致する取引数を報告できます。[NWC拡張リポジトリ](https://github.com/nostr-wallet-connect/nwc)のNWC-05（wallet履歴拡張）で[任意の`total_count`がマージされ](https://github.com/nostr-wallet-connect/nwc/pull/4)、[NIP-47](/ja/topics/nip-47/)（Nostr経由の暗号化remote wallet制御）とともに使う応答へこのフィールドが追加されます。

[`total_count`を追加したcommit](https://github.com/nostr-wallet-connect/nwc/commit/ff3e49a47d040075edc46ee42fc0e33f10f1ef67)は、これをrequest filterに一致する取引の総数を表す任意の整数として記述しています。

[countからページネーションを除外するcommit](https://github.com/nostr-wallet-connect/nwc/commit/06315e735f744b1afd3df0b57436fdce8a7bfc2e)は、この総数がページネーションを除外すると明記しています。したがってすべてのページにわたる一致取引を数えます。

## NIP詳細解説: リポストとリアクション

ある連絡先は、既存のノートを自分のフォロワーの前へ再び出せます。また返信を書かずに、簡潔ないいね、よくない、絵文字を付けられます。[NIP-18](/ja/topics/nip-18/)（リポスト）は、その再配布を独自の署名済みeventとして公開します。[NIP-25](/ja/topics/nip-25/)（リアクション）は、簡潔な応答を別の署名済みeventとして公開します。どちらも、[正規のリポスト仕様](https://github.com/nostr-protocol/nips/blob/master/18.md)と[正規のリアクション仕様](https://github.com/nostr-protocol/nips/blob/master/25.md)における`draft` `optional`ファイルのままです。NIPsリポジトリに存在し、クライアントに実装されていますが、なお未確定と表示されています。

### リポスト（NIP-18）

クライアントがkind 6 eventを書くと、すでに誰かが公開したkind 1テキストノートへの署名済みpointerをフォロワーが受け取ります。[リポスト仕様](https://github.com/nostr-protocol/nips/blob/master/18.md)は`kind`を6とし、そのノートを文字列化したJSONを`content`に入れ（空の`content`も許可されますが非推奨です）、値がノートの`id`で3番目の要素がノートを取得できるrelay URLである`e` tagを要求し、eventに元の著者の`pubkey`を持つ`p` tagも含めるべき（SHOULD）としています。[NIP-70](/ja/topics/nip-70/)（保護されたevent）のeventをリポストするときは、保護されたpayloadが新しいeventへ複製されないよう`content`を空に保つべき（SHOULD）です。

quoteはkind 6のwrapperではなく、別のevent内の引用です。クライアントが[NIP-21](/ja/topics/nip-21/)（`nostr:` URI）の`nevent`、`note`、`naddr`へ言及すると、その言及を`["q", "<event-id> or <event-address>", "<relay-url>", "<pubkey-if-a-regular-event>"]`形式の`q` tagに変換しなければなりません。[quote repost tag](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts)は、それらの引用を返信threadの外に保ち、クライアントが投稿上のquoteを取得して数えられるようにします。

Kind 6はkind 1ノート専用です。kind 16の汎用リポストは、kind 1以外の任意のevent kindをwrapできます。内側のeventのkindを文字列化した値を持つ`k` tagを含めるべき（SHOULD）です。その内側のeventがreplaceableなら、汎用リポストは`kind:pubkey:d-tag`座標を持つ`a` tagを追加すべき（SHOULD）です。その`a` tagがない場合、リポストは特定の1バージョンを対象とし、`content`はそのバージョンの完全なJSON文字列を持たなければなりません。[汎用リポストの規則](https://github.com/nostr-protocol/nips/blob/master/18.md#generic-reposts)は、長文、addressable、その他の非ノートeventがkind 1であるかのように公開されるのを防ぎます。

次のkind 6 eventは、編集時に`wss://relay.damus.io`から取得した実在するリポストです（[eventを開く](https://njump.me/nevent1qqs88k8xgv2d3d3yymawaa24f22a0kqqvknpur0p05vq9e5r4y74xjspz3mhxue69uhhyetvv9ujuerpd46hxtnfdu7elvca)）。

```json
{
  "kind": 6,
  "id": "73d8e64314d8b62426faeef5554a95d7d80065a61e0de17d1802e683a93d534a",
  "pubkey": "a60e79e0edad5100d7543b669e513dbc1c2170e8e9b74fdb8e971afd1e0e6813",
  "created_at": 1787768621,
  "tags": [
    [
      "e",
      "38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976"
    ],
    [
      "p",
      "34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095"
    ],
    [
      "client",
      "Primal iOS"
    ]
  ],
  "content": "{\"pubkey\":\"34d2f5274f1958fcd2cb2463dabeaddf8a21f84ace4241da888023bf05cc8095\",\"sig\":\"8c0271f7b438083ce491c391335598e0cbceee0758177cf98f7894531033cb5153704b01009590f3d4e9cdfadd5bbf73fc5eea54186fcbac6d30744e0e6c1cd6\",\"id\":\"38980cd673ee16609dc87081d9f645c331d5a5a8b5b0d6c8147600ed29447976\",\"tags\":[[\"r\",\"https:\/\/stacker.news\/items\/1555439\"],[\"client\",\"Damus\"]],\"created_at\":1787766056,\"content\":\"🚨 Attention CLN (Core Lightning) node runners 🚨\n\nhttps:\/\/stacker.news\/items\/1555439\",\"kind\":1}",
  "sig": "b6b97fa377cfdb651e2850f65f2ccb12ca0724c0de0fc0e39e9721f850abdfd31f5d5567517a51d988145c2a2de9ae9540b02eecf7352e554022870d5e8c64a5"
}
```

その`kind`は6で、`e` tagはリポストされたノートを指し、`p` tagはそのノートの著者を示し、`content`は元のkind 1 eventを文字列化したJSONとして保持します。このrelayから取得したeventは、[NIP-18仕様](https://github.com/nostr-protocol/nips/blob/master/18.md)が必須とするrelayヒントを省いています。これはreaderとクライアントが実在するeventを検証し、フィールドを省略するproducerを許容しなければならない理由を示しています。

### リアクション（NIP-25）

投稿は、署名済みのいいね、よくない、絵文字を、それらの印が返信threadへ入ることなく集められます。[リアクション仕様](https://github.com/nostr-protocol/nips/blob/master/25.md)は、その印をリアクション値を`content`に必ず持つ（MUST）kind 7 eventとして定義します。`+`または空文字列は、いいねまたはupvoteとして読まなければなりません（MUST）。`-`は、よくないまたはdownvoteとして読まなければなりません（MUST）。絵文字または[NIP-30](/ja/topics/nip-30/)（カスタム絵文字）のshortcodeは、いいねやよくないとして読むべきではなく（SHOULD NOT）、クライアントはその絵文字を投稿上に表示してもかまいません（MAY）。

対象はtag内にあり、`content`から推測されるものではありません。対象eventの`id`を設定した`e` tagが必須（MUST）で、そのtagにはrelayヒントを含めるべき（SHOULD）です。余分な`e` tagは非推奨で、存在する場合は対象の`id`が最後でなければなりません。対象著者の`p` tagを含めるべき（SHOULD）で、複数の`p` tagがある場合は最後に置きます。addressableな対象には`kind:pubkey:d-tag`座標を持つ`a` tagも付けるべき（SHOULD）です。`e`と`a` tagにはrelayとpubkeyのヒント、`p` tagにはrelayのヒントを含めるべき（SHOULD）で、`k` tagはリアクション対象eventのkindを文字列化して持ってもかまいません（MAY）。[これらのtag規則](https://github.com/nostr-protocol/nips/blob/master/25.md#tags)により、クライアントはリアクションeventだけから対象を取得し、その著者へ通知できます。

クライアントは[カスタム絵文字リアクションの規則](https://github.com/nostr-protocol/nips/blob/master/25.md#custom-emoji-reaction)に従い、`content`に1つの`:shortcode:`を入れ、そのshortcodeを画像URLに対応付ける`emoji` tagを1つ付けてもかまいません（MAY）。対象がNostrネイティブのeventでない場合、リアクションはkind 17でなければならず（MUST）、[外部コンテンツへのリアクション規則](https://github.com/nostr-protocol/nips/blob/master/25.md#external-content-reactions)のように[NIP-73](/ja/topics/nip-73/)（外部コンテンツID）の`k`と`i` tagを持たなければなりません（MUST）。Kind 17はwebサイト、podcast episode、その他の外部objectへのリアクションです。kind 7のevent間リアクションでもリポストでもありません。

次のkind 7 eventは、編集時に`wss://relay.damus.io`から取得した実在するリアクションです（[eventを開く](https://njump.me/nevent1qqsytac63l00k7kyaphkfwqqn94wglmx78v6zhqtytg65w5k957luccpz3mhxue69uhhyetvv9ujuerpd46hxtnfdus63jym)）。

```json
{
  "kind": 7,
  "id": "45f71a8fdefb7ac4e86f64b800996ae47f66f1d9a15c0b22d1aa3a962d3dfe63",
  "pubkey": "0755cc2b972c3cbcae36913109c50b36b3fe110fa38a76dc37d1f01c5305496a",
  "created_at": 1787768605,
  "tags": [
    [
      "e",
      "519de32071d71bb2ab8b71a07e03eb9a256b6a59f9b08877b156c80966d5c320"
    ],
    [
      "a",
      "34236:5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb:2ddda68516f4729d3ef55a1eb01fe028253393212493a34816ad8eb79f97a3b7"
    ],
    [
      "p",
      "5ab67f7d7fed4f781008c0ec0d26c8113f9fb46094a8346246c70c75e75db9fb"
    ],
    [
      "k",
      "34236"
    ],
    [
      "client",
      "Divine",
      "31990:d95aa8fc0eff8e488952495b8064991d27fb96ed8652f12cdedc5a4e8b5ae540:divine-mobile",
      "wss://relay.divine.video"
    ]
  ],
  "content": "+",
  "sig": "3c081756c7a73e2ee8aa10fadf3b5009390d5ac9a72078ba03701c42af91022ef275df7cb17724689a23dca4e29ff1a7cd5e3a24135d021983e2726a28b00b1e"
}
```

その`content`は`+`で、[NIP-25](https://github.com/nostr-protocol/nips/blob/master/25.md)における慣例的ないいねです。`e` tagはリアクション対象のeventを示し、`a` tagはそのaddressableな座標を追加し、`p` tagは著者を示し、任意の`k` tagは対象のkindを文字列として記録します。

### 現在のクライアント実装

Android Nostrクライアントの[Amethyst](https://github.com/vitorpamplona/amethyst)は、現在のprotocol layerで[リポストevent型](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip18Reposts/RepostEvent.kt)と[リアクションevent型](https://github.com/vitorpamplona/amethyst/blob/d06b83bd53c510e589d5ce13d46f6bd1a8206394/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip25Reactions/ReactionEvent.kt)を定義しています。

web Nostrクライアントの[Snort](https://github.com/v0l/snort)は、[quoteリンクのtag処理を含むNIP-18 helper](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip18.ts)を実装し、[NIP-25 eventリアクションtagを作成します](https://github.com/v0l/snort/blob/8b2e6cb6dc5a5e0b7e052b4ed89a9c5630444e95/packages/system/src/impl/nip25.ts)。

Mastodon serverとNostr relayを組み合わせた[Ditto](https://github.com/soapbox-pub/ditto)は、[addressableな対象に`k` tagと`a`座標を持つkind 16汎用リポストを公開し](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/components/RepostMenu.tsx)、[最後の`e` tagを対象eventとして扱うことでkind 7のリアクション規則を適用します](https://github.com/soapbox-pub/ditto/blob/570fc4b26e5900ccb4085cfdb2cc86d08cdd9ade/src/lib/nostrEvents.ts)。

### 連携の仕組み

kind 6またはkind 16 eventは、既存eventのJSONを埋め込むかreplaceableな座標を指すことで、そのeventをリポストした人のフォロワーのフィードへ再配布します。`q` tagは別のevent内のquoteを示し、thread再構築がquoteしたeventを返信として扱わず引用を数えられるようにします。これは[quote repostの節](https://github.com/nostr-protocol/nips/blob/master/18.md#quote-reposts)が示す区別です。kind 7 eventは元のeventをそのままにし、リアクション値と対象tagだけを付けます。これが[リアクション仕様](https://github.com/nostr-protocol/nips/blob/master/25.md)の契約です。したがって1つのpubkeyを取得するクライアントには、そのpubkeyのリポストが新しいkind 6または16 eventとして、そのpubkeyの意見が他人の投稿上のkind 7 eventとして見えます。

---

[Nostr Compassプロジェクト](https://github.com/andotherstuff/nostr-compass)を通じてプロジェクトやニュース項目を共有するには、NIP-17 DMを送ってください。
