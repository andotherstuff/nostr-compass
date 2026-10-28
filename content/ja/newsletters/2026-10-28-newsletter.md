---
title: "Nostr Compass #46"
date: 2026-10-28
publishDate: 2026-10-28
translationOf: /en/newsletters/2026-10-28-newsletter.md
translationDate: 2026-10-28
draft: false
type: newsletters
description: "Mostroが署名付きのアイデンティティ再バインドを追加し、Amethyst 1.20.0がMarmotグループのプライベート投票と暗号化された設定同期を導入、swift-nostr 0.9.0がリリースされ、6回分のNostrの10月を振り返ります。"
---

今週は、**Mostro**が[署名付きのアイデンティティ再バインド](https://github.com/MostroP2P/mostro/pull/1035)を追加しました。**Amethyst**は、Marmotグループに[プライベート投票](https://github.com/vitorpamplona/amethyst/pull/4630)を、デバイス間に[暗号化された設定同期](https://github.com/vitorpamplona/amethyst/pull/4613)をもたらします。**swift-nostr**は、[公開鍵が署名者のものと一致しないeventへの署名を拒否するチェック](https://github.com/yysskk/swift-nostr/pull/239)を搭載してリリースされました。締めくくりは「Nostrの10月、6年間の歩み 2021–2026」です。

## トップストーリー {#top-stories}

[commands-review]: https://github.com/nostr-protocol/nips/pull/2462 "Proposed previously, now merged"
[marmot-devices-review]: https://github.com/marmot-protocol/marmot/pull/442 "Proposed previously, now merged"
[cd-installed-merge]: https://github.com/nostr-protocol/nips/commit/400d157c53264b8e58c7b3cdbd21ef546fb7a157

### Mostro {#mostro}

Nostrで調整されるピアツーピア取引所デーモンの[Mostro](https://github.com/MostroP2P/mostro)が、[0.20.1をリリースしました](https://github.com/MostroP2P/mostro/releases/tag/v0.20.1)。このリリースでは[署名付きのアイデンティティ再バインド](https://github.com/MostroP2P/mostro/pull/1035)が追加されました。これは[前号](/en/newsletters/2026-10-21-newsletter/#mostro)で未実装と説明していた機能です。また、これまでソースコードでのみ提供されていたレピュテーションのエクスポート機能も同梱されています。バインド済みのアイデンティティが、ノードと新しいアイデンティティを指定した使い捨ての認可に署名し、その有効期間は最長1時間です。デーモンはevent IDを記録したうえでcompare-and-swapで切り替えるため、署名が失敗したり競合に負けたりしても何も変わりません。運営者向けには、認証トークンと理由の指定を必要とする、監査付きのループバック専用RPCも用意されています。なお、再バインドを行っても、発行済みのアテステーションは失効しません。

その後にマージされた変更は、リリースへの収録が確認されていません。[オプトイン方式の固定USDペッグプロバイダー](https://github.com/MostroP2P/mostro/pull/1083)は、運営者が有効にした場合に限り、Nostrの`mostro-rates`フィードにUSDT、USDC、DOCを追加します。ネットワークプロバイダーや、relay経由で中継されたコイン相場によって暗黙的に有効化されることはありません。[後続の変更](https://github.com/MostroP2P/mostro/pull/1091)では、プロバイダーとその設定キーの名前を`pegged`に変更し、未リリースだった`stablecoins`キーを置き換えています。さらに、BTC、LBTC、RBTCをsats建てで1:1に固定して提示し、そのレートをkind 30078のeventとして公開します。これらは設定されたペッグの前提にすぎず、ペッグや決済が保証されるわけではありません。リアルタイムのペッグ確認は、この仕組みの対象外です。このプロバイダーはデフォルトで無効になっています。注文は引き続き受け入れ通貨によって制限されており、クライアント、プロトコルブック、ペッグガードに関する作業は別に扱われています。[ボンドのタイムロックは、エスクローとは別に動作するようになりました](https://github.com/MostroP2P/mostro/pull/1085)。公開される注文の有効期限には上限が設けられ、オーダーブック上で注文を受けられる期間は、ボンドが失効しうる時点より前に締め切られます。既存の144ブロックのメイカーボンドはアップグレード時に失効するため、該当する注文は作り直す必要があります。進行中の取引とCashuモードには影響しません。ただし、運営者の設定によっては、ボンドのタイムロックを調整するまで起動を拒否する場合があります。

### Nostr WoT拡張機能 {#nostr-wot-extension}

web-of-trust機能を備えたブラウザ署名ツールである[Nostr WoT拡張機能](https://github.com/nostr-wot/nostr-wot-extension)が、[0.8.15](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.15)をリリースしました。このバージョンでは、ユーザー自身がサイコロやコインで得た256ビットのエントロピーからリカバリーキーを作成するオプションが加わっています。サイコロの出目はSHA-256でハッシュ化され、コイン投げの結果はそのままビットとして使われます。この処理は、リカバリーフレーズを表示しない隔離されたタブの中で行われます。relayに到達できない場合、オンボーディングはタイムアウトするようになりました。[バージョン0.8.16](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.16)では[relay認証（NIP-42）](/ja/topics/nip-42/)向けの常設許可が追加され、ユーザーはサイト上のすべてのrelay、または接続済みのすべてのサイトに対して、AUTHを一度で承認できるようになりました（[relay認証の実装](https://github.com/nostr-wot/nostr-wot-extension/pull/47)）。relayやサイト単位の拒否はこれらの許可より優先され、キューに入ったリクエストが解決される前に、取り消しの有無が改めて確認されます。広い範囲の許可は常にユーザーが明示的に選ぶものであり、[HTTP Auth（NIP-98）](/ja/topics/nip-98/)に適用されることはありません。キューの上限は5件のままなので、超過したリクエストは引き続き失敗し、再試行されます。[バージョン0.8.18](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.18)では、インポートとリカバリーが一つのフローに統合されました。このフローは鍵の形式を検出し、アイデンティティをプレビューします。互換性のあるNosskeyリカバリーでは、同じアイデンティティ、既存のアカウント、元のパスキーがそのまま維持されます。

これとは別の開発者向けSDKである[nostr-wot-sdk](https://github.com/nostr-wot/nostr-wot-sdk)は、安定版のidentity 1.1をサポートする[3.0.1](https://github.com/nostr-wot/nostr-wot-sdk/releases/tag/nostr-wot-sdk%403.0.1)をリリースしました。Nosskey経由を含むパスキーによるリカバリーでは元のpubkeyが維持され、プロバイダー、リカバリー、署名の各コードは単一の実装を共有するようになりました（[SDKのリカバリーとプロバイダーのソース](https://github.com/nostr-wot/nostr-wot-sdk/pull/22)）。非推奨となったフォワーダーパッケージは引き続き動作しますが、組み込む開発者はメンテナンスされているエントリポイントへ移行すべきです。

### Amethyst {#amethyst}

AndroidおよびデスクトップのNostrクライアントである[Amethyst](https://github.com/vitorpamplona/amethyst)が、[バージョン1.20.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.20.0)をリリースし、[プライベート投票やその他のMarmot暗号化グループ機能](https://github.com/vitorpamplona/amethyst/pull/4630)を追加しました。具体的には、差し替え可能なプライベート投票、暗号化されたカスタム絵文字、管理者によるメッセージ削除と通報、グループの現在のepochに固定されたメディアなどです。作者はレビュー後にクライアント間の相互運用性チェックを再実行しておらず、Android上での手動テストも行っていません。同じepoch番号を共有する競合ブランチのキャッシュキーは残ったままであり、暗号化されたメディアの鍵が消えるメッセージよりも長く残る可能性があります。[設定同期](https://github.com/vitorpamplona/amethyst/pull/4613)は、アプリ設定の6つのグループを暗号化された[NIP-78](/ja/topics/nip-78/)データとして保存します。鍵、署名者、ウォレット、通知、デッキ、既読マーカーは、それぞれのデバイスに留まります。最初に設定を編集した時点で、6つのグループすべてが公開されます。読み取り専用アカウントでは設定がローカルに保持されます。2台の署名デバイスをまたいだ動作は検証されていません。

デスクトップのシステム通知は[通知フィルターに従う](https://github.com/vitorpamplona/amethyst/pull/4650)ようになり、使い捨ての外側のgift wrapやミュートされたDMは通知の対象外となりました。[255バイトを超える信頼できない`d` tag](https://github.com/vitorpamplona/amethyst/pull/4616)によってエラーが発生することもなくなりました。[kindの検索](https://github.com/vitorpamplona/amethyst/pull/4600)は、接続済みのrelayとアカウントの検索用relayにのみ問い合わせ、それぞれ最大200件のeventを取得します。アプリは[QuartzのKite JSON処理を使用する](https://github.com/vitorpamplona/amethyst/pull/4595)ようになり、その対象はフレーム、event、フィルター、そして[NIP-46](/ja/topics/nip-46/)と[NIP-55](/ja/topics/nip-55/)のメッセージです。ただし、これら2つのプロトコルを介した署名は、デバイス上で検証されていません。その後の[ライブラリ分割](https://github.com/vitorpamplona/amethyst/pull/4654)では、他のクライアントが必要とするMarmotとcordnのプロトコルルールが共有ライブラリへ移されています。

1.20.0以降にマージされ、まだリリースに含まれていないソースでは、[アプリのMarmot受信経路が共有ライブラリ上で動作します](https://github.com/vitorpamplona/amethyst/pull/4672)。復号されたメッセージはすべて冪等に永続化されます。参加時にはベースラインが記録されるため、最初のメンバーシップ変更にも対応する行が表示されます。対応するコミットより先に届いたkind 445メッセージは保留され、後で再生されます。また、管理者のキャッチアップ処理では、ステージングされた退出がコミットされます。`amy cordn migrate export`は、インポートまたは新しいresumeコマンドが実行されるまで、旧インストールのセッションコマンドを無効にします。作者はローカルのチェックアウトに対して、ループバックでのamyテストとライブラリテストを実行しました。一方で、実際のアプリの受信経路を手動で動かすことも、Marmotの相互運用テストスイートを実行することもしていません。提案中の[NIP-5D napplet形式](/ja/topics/nip-5d/)に対する[破壊的な更新](https://github.com/vitorpamplona/amethyst/pull/4659)により、napplet manifestのハッシュは単一の`/index.html`アーティファクトとして読み取られるようになり、従来のパス集約は置き換えられました。そのため、旧形式のバンドルは再公開が必要です。必須のNAPドメインが利用できない場合はフェイルクローズとなり、オプションのドメインは存在しないままになります。アイコンにはハッシュとデコーダーのチェックが行われます。ストレージはmanifestのkind、アーティファクト、スナップショットごとに分割され、リソースのblobには正規のbase64が使われます。デバイスでの手動テスト、クライアント間のテスト、実際のrelayへの公開は行われていません。

[外部署名アプリでの拒否](https://github.com/vitorpamplona/amethyst/pull/4669)が、これまでガードのなかったコルーチン全体で処理されるようになり、アプリがクラッシュしなくなりました。[PressStrの電子書籍、雑誌、号](https://github.com/vitorpamplona/amethyst/pull/4662)（kind 33953、34609、39731）も表示されるようになりました。PDFはアプリ内リーダーで開き、EPUBはシステムのハンドラーに渡されます。カードにはファイルの種類とサイズが表示されます。プレビューのためだけに大きなPDFをダウンロードすることはなく、号は雑誌の作者からのみ取得されます。この変更について、作者はAndroidデバイスでのテストを報告していません。リッチプレビューがオフの場合、[インボイスとLNURLはコピー可能なコンパクトなラベルとして表示され](https://github.com/vitorpamplona/amethyst/pull/4663)、支払いボタンは表示されません。インボイスカードには有効期限も表示されるようになりました。`amy gift wrap`は[sealとwrapにそれぞれ別々のランダムな日時を付けるようになり](https://github.com/vitorpamplona/amethyst/pull/4661)、いずれも最大2日前まで遡ります。`--no-backdate`でこの動作を無効にできます。通常のDM経路については、Quartz側で別途修正されます。デスクトップでは[各動画カードが自身の再生を管理する](https://github.com/vitorpamplona/amethyst/pull/4660)ようになったため、同じURLを持つカード同士が互いの動画を奪い合うことはなくなりました。作者はmacOSでこれをテストしましたが、コールドキャッシュの状態ではテストしていません。[提案中のWindows向けリンク修正](https://github.com/vitorpamplona/amethyst/pull/4666)は、rundll32をフルパスで指定してリンクを開き、AWTへのフォールバックも備えています。根本原因は再現されていないため、これは確認済みの修正ではなく、有力な修正候補にとどまります。

### Mycoが暗号化されたnappletストレージと署名付きの更新通知を追加 {#myco-adds-encrypted-napplet-storage-and-signed-update-notices}

Nostr napplet向けのAndroidホストであるMycoが、0.12.0と[0.12.1](https://github.com/Origami74/myco/releases/tag/v0.12.1)をリリースしました。nappletは、ランタイムを通じて[NIP-44](/ja/topics/nip-44/)で[自己暗号化したデータ](https://github.com/Origami74/myco/pull/152)を保存できるようになりました。ただし、relay、outbox、meshの読み取り許可を持つアプリは平文を参照できるため、データはアプリごとに分離されていません。以前にAmberでログインしたユーザーは、新しい暗号化と復号の権限を付与するために、再度ログインする必要があります。更新通知はピン留めされた発行者によって署名され、すでに0.12を実行しているデバイスにのみ届きます。オンライン時、MycoはZapstoreを毎日確認できるほか、Circleも確認できます。一方、メッシュ専用モードではCircleにのみ問い合わせます。これは[当初の一時停止](https://github.com/Origami74/myco/pull/151)に代わる仕組みです。明示的に選択したローカルBlossomレールでは、サーバーを使わずにファイルをデバイス上に保持し、上限はアプリごとに1日あたり64 MiBです。承認済みのデフォルトサーバーへのアップロードに失敗した場合も、ローカルにコピーが残ります。どちらの経路でも、EXIFメタデータは除去されません。これらのリリースでは、Android TVのサポートと、ユーザー自身がファイルを選ぶNAPFSファイルピッカーも追加されています。

## タグ付きリリース {#tagged-releases}

### Monostr {#monostr}

AndroidのNostrソーシャルクライアントである[Monostr](https://github.com/schmidt1024/monostr)が、最新バージョンの[0.26.0](https://github.com/schmidt1024/monostr/releases/tag/v0.26.0)をリリースしました。最長2分までの動画はデバイス上で圧縮されるようになり、位置情報のメタデータは削除されます。Discover、検索、オンボーディングでは、厳選されたフォローリストが提示されます。スレッドと通知には、[NIP-22](/ja/topics/nip-22/)コメントとして送られたFediverseからの返信が表示されるようになりました。

[0.25.0](https://github.com/schmidt1024/monostr/releases/tag/v0.25.0)で導入された機能も引き続き利用できます。返信の親投稿が見つからない場合、アプリは返信のrelayヒントと、親投稿の作者のrelayを検索します。つまり、ユーザー自身のリストにないrelayへ一時的に接続することになります。また、デバイスのネットワークが切り替わるたびに、relayとライブメッセージの購読が再接続されます。

### Sidecar {#sidecar}

Nostrのブラウザ拡張機能兼署名ツールである[Sidecar](https://github.com/dmnyc/sidecar)が、[1.16.3をリリースしました](https://github.com/dmnyc/sidecar/releases/tag/v1.16.3)。コンポーザーとハイライトツールは、[アカウント自身のrelayに公開し、eventを確認応答したrelayのみをカウントする](https://github.com/dmnyc/sidecar/pull/545)ようになり、そのうえでそれらのrelayへのリンクを示します。確認応答は、relayがeventを受け付けたことを示すものであり、それを保持し続けることを示すものではありません。拡張コンポーザーは、設定にあるデフォルトのrelayへフォールバックしなくなりました。relayごとに、それぞれ12秒の期限が設けられています。すべてのrelayで失敗した公開に限り、新しいソケットで1回だけ再試行されます。[投票結果](https://github.com/dmnyc/sidecar/pull/544)では、4つの公開relayにも投票を問い合わせます。タグ付け後にマージされた変更では、通常のrelay以外に投じられた投票を拾うため、[relayがもう1つ追加されています](https://github.com/dmnyc/sidecar/pull/550)。ある実際の投票では、これにより票数が21票から23票に増えました。これは1件の投票での結果にすぎず、ネットワーク全体での網羅性については何も示していません。集計では引き続き1人1票のみが認められ、締め切り後に投じられた票は無視されます。それ以前の[1.16.1](https://github.com/dmnyc/sidecar/releases/tag/v1.16.1)では、常設の署名許可が、それを承認したアカウントとサイトに限定され、eventにd tagがある場合は単一のaddressableレコードに限定されています。許可が暗号化や復号に及ぶことはありません。プロフィール、フォロー、ミュート、relayの各リストは、どの許可の対象にもなりません。削除、zapリクエスト、relay AUTH、ウォレット操作も除外されます。ロックされた拡張機能では、引き続きPINの入力が求められます。許可を取り消すか、サイトの情報を消去すると、そのサイトの許可と承認期間がクリアされます。

これとは別に、[オープン中のプルリクエスト](https://github.com/dmnyc/sidecar/pull/552)では、CLINKオファーへの支払いをzapとして扱えるようにすることが提案されています。この変更は変更履歴のUnreleasedに入っており、Debitsは実装していません。オファーパネルはpayer_dataを含む署名済みのkind 9734 zapリクエストを渡し、サービスがkind 9735のレシートを公開できるようにする想定です。レシートはまずオファーのrelayに、次に受取人のrelayに送られ、重複を除いたうえで最大6つに制限されます。支払者のrelayは使用されません。オファーがコード3と、デコード可能な後継オファーを返した場合、Sidecarは新しいリクエストと新しい署名でそれに一度だけ従います。受取人のプロフィールに書き込むことは決してありません。この変更は、締め切り時点でまだマージされていませんでした。

### Roadbeacon {#roadbeacon}

位置情報を報告するクライアントRoadbeacon（旧称Roadstr。独立したRoadstrアプリとは別物）が、[新名称で0.4.0をリリース](https://github.com/jooray/roadbeacon/releases/tag/v0.4.0)した。新しいパッケージとして提供され、新しいevent形式を採用している。レポートと投票には共有の相互運用可能なkind 1315と1316が使われるようになり、座標は正確に復元できる整数フレームで表され、Web版は署名を検証する。このパッケージは旧パッケージと並行してインストールされ、データは移行されない。古いeventはrelay上で引き続き有効だが、新しいクライアントでは読み込めない。

### Jumble {#jumble}

Nostr Webクライアントの[Jumble](https://github.com/CodyTseng/jumble)が[v26.10.1をリリース](https://github.com/CodyTseng/jumble/releases/tag/v26.10.1)した。新機能には、長文記事エディター、デバイス間で同期されるミュートワード、システム通知、グループおよびGitコンテンツ用のリーダーが含まれる。最近の号で取り上げた保留中投稿とレイアウトの変更も、このリリースの一部として提供される。

リリース後にマージされたコミットでは、[NIP-22による返信のオプション設定](https://github.com/CodyTseng/jumble/commit/ea798677d366ff750ac556d31c5628fe47ebd275)が追加された。デフォルトではオフで、ローカルの設定として保存される。有効にすると、kind 1テキストノートへの返信はkind 1111コメントとして送信される。既存のkind 1111スレッドはルートを維持し、他のkindや外部コンテンツへのコメントもkind 1111のままとなる。設定がオフなら、返信は従来のkind 1の挙動を保つ。一部のクライアントではこれらのコメントが表示されない可能性があると、アプリは警告している。

### nostr-idb {#nostr-idb}

ブラウザのIndexedDBにNostr eventをキャッシュするライブラリ[nostr-idb](https://github.com/hzrd149/nostr-idb)が、[クエリ修正を含む5.1.1をリリース](https://github.com/hzrd149/nostr-idb/releases/tag/v5.1.1)した。replaceable eventとaddressable eventでもIDの完全一致検索が機能するようになり、すべてのフィルター条件とフィルターごとのlimitが、書き込み待ちのデータや購読履歴も含めて適用されるようになった。キャッシュの刈り込みと、タイムスタンプがゼロのeventの問題も修正されている。インメモリキャッシュのサイズ`maxMemoryEvents`はデフォルトで`maxEvents`となり、ゼロにすると無効になる。

### Manent {#manent}

Nostr経由で同期する暗号化ノートブック[Manent](https://github.com/dtonon/manent)が、[ボイスノート機能を備えた3.0.0をリリース](https://github.com/dtonon/manent/releases/tag/v3.0.0)した。録音は他のノートと同様に暗号化されて同期され、文字起こしはアプリがモデルをダウンロードした後、Whisperによってオフラインで生成される。以前ソースコード上の作業として取り上げたrelay認証の復旧機能もこのリリースに含まれており、現在はNostr開発キットライブラリであるNDKのバージョン0.10.1を通じて提供されている。

### NoorNote {#noornote}

デスクトップおよびWeb向けのNostrクライアント[NoorNote](https://github.com/77elements/noornote)は、ノートとダイレクトメッセージを対象とする[デバイスローカルの全文検索を備えた1.9.2をリリース](https://github.com/77elements/noornote/releases/tag/v1.9.2)し、キャッシュのみのモードも追加した。[バージョン1.9.3](https://github.com/77elements/noornote/releases/tag/v1.9.3)では、1.9.2で生じた透明ガラス表示のリグレッションを受けて、ドロップダウン、メニュー、トーストが再び読みやすくなった。これらのリリースには、以前はソースにのみ存在した未来のタイムスタンプを除外するフィルターも含まれている。読み込みに失敗したプロフィールは、取得失敗が確定するまで読み込み中の状態にとどまるようになった。

### Earthly {#earthly}

Nostrの地図作成クライアントEarthlyが、[relayと支払いに関する修正を含む0.1.22をリリース](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.22)した。relay認証は、アクティブなアカウントに紐付けられるようになった。復旧された購読とカウントでは、取得できないカウントと実際のゼロが区別され、地図のリビジョンをまたいでカウントが保持される。zapの合計は実際のzapレシートから算出され、アプリは支払いの前にウォレットの同期完了を待つ。実環境でのNostr Wallet Connectとmintによる支払いは、まだテストされていない（[リリースへの統合](https://github.com/zeSchlausKwab/earthly/pull/36)）。

### Chama {#chama}

Nostr eventの上に構築されたエスクロー取引クライアント[Chama](https://github.com/jesuspirate/chama)が[6.4.31をリリース](https://github.com/jesuspirate/chama/releases/tag/v6.4.31)し、資金投入の前にシードのバックアップを確認するようになった。このデバイスのオンチェーン取引鍵が署名済みのCREATE、JOIN、またはデポジットの条件に組み込まれる前に、デバイスが開いた署名済みシードバックアップをrelayが返さなければならない。バックアップが存在しない、廃止済み、または競合している場合、取引は停止する。再試行の際は新しいシードを生成せず、保存済みのバックアップをそのまま再送信する。この読み戻しが示すのはその時点での利用可能性であって、永続性ではない。複数単位の出品では、数量指定の注文が使われるようになった。[バージョン6.4.30](https://github.com/jesuspirate/chama/releases/tag/v6.4.30)は、購入者が署名した条件が署名済みの出品と一致する場合にのみストアフロントの注文をカウントし、署名済みCREATEの日付が2026年12月1日以降の取引では遅れて届く部外者のeventを防ぐ。それより前の取引では、従来の有効期限の挙動が維持される（[取引の有効期限とストアフロントの検証](https://github.com/jesuspirate/chama/pull/77)）。

ソースのカットオフ時点で未マージのオープンなプルリクエストは、[アイデンティティごとにウォレットシードのバックアップを1つだけ許可する](https://github.com/jesuspirate/chama/pull/92)ものだ。起動時には、ページ内キューとWeb Locksによって最初の作成処理を直列化し、その後relayの状態を読み直す。別々のブラウザ間では、この読み直しだけが頼りとなる。分散ロックや、既存の競合するバックアップの修復は、この変更の範囲外である。我々は資金に関わる経路を一切テストしていない。

### Linky {#linky}

Nostr経由で同期するCashuウォレット[Linky](https://github.com/linky-fit/linky)は、[バージョン26.10.7](https://github.com/linky-fit/linky/releases/tag/linky-v26.10.7)と[Android版26.10.8ビルド](https://github.com/linky-fit/linky/releases/tag/linky-v26.10.8)で、フラグで有効化する実験的なオンチェーン送金を追加した。設定された人間のオペレーターが手数料と引き換えに送金と受取のリクエストを24時間以内に処理するため、送金はアトミックでもトラストレスでもない。[この連携の変更](https://github.com/linky-fit/linky/pull/637)では、カスタムのNostrアプリメッセージ、[NIP-78](/ja/topics/nip-78/)によるオペレーター設定、新しいリンク同期スコープが使われる。このスコープはオペレーターの保留中のecash送金を同期し、オペレーターの他のデバイスが同じ送金を二重に支払ったり、返金したり、決済したりできないようにする。受取が完了するのは、ユーザーのウォレットが対応する額のCashuを受け取ったときだけである。オペレーターとユーザーが互いを見つけられるのは推奨relay上に限られ、[NIP-65](/ja/topics/nip-65/)のrelayリストやDM受信箱リストは使われない。そのため、共有relayをすべて失うと連携が途絶える可能性がある。

### LaWallet {#lawallet}

Nostr Wallet Connect上に構築されたウォレット兼アカウントサービス[LaWallet](https://github.com/lawalletio/lawallet-nwc)は、[バージョン2.9.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.9.0)と[Android 1.2.0ベータ](https://github.com/lawalletio/android-wallet/releases/tag/v1.2.0)をリリースした。どちらも、新しいNostrログインへのNFCカード支援による復旧機能を追加している（[ネイティブ復旧フロー](https://github.com/lawalletio/android-wallet/pull/1)）。復旧には、暗号学的に検証された新たなカードタップと、15分間有効な使い捨ての復旧用QRコードが必要となる。資産は1回のトランザクションで移され、ロールは移行されず、古いOAuth許可は取り消され、古いログインは空の状態で残される。カードによる復旧はデフォルトで有効で、アカウント保有者はセキュリティ設定でこれを無効化したり、未使用のコードを取り消したりできる。到達できないウォレットは残高ゼロと表示されるようになったが、これは空であることを意味しない。Androidベータ版では、レポート送信先のエンドポイントを持つビルドの場合、以前にオプトアウトしていてもSentryによるエラーレポートが強制的に有効になる。ローカルビルドとF-Droidビルドにはエンドポイントがない。

タグ付け後にマージされたソースでは、残高で支払いを賄える場合に[カードのコールバックがNWCの決済前にOKを返すことがある](https://github.com/lawalletio/lawallet-nwc/pull/385)ため、POSシステムは自身の請求書を確認する必要がある。残高に基づく上限は、[固定の支払い上限](https://github.com/lawalletio/lawallet-nwc/pull/388)に置き換えられた。ソースのカットオフ時点で未マージのオープンなプルリクエストは、設定されたプロバイダーまたはNosskey復旧を通じて、他のアプリの互換パスキーによるサインインを可能にするもので、有効期限付きの一時セッションを発行する前にアカウントを確認する（[#386](https://github.com/lawalletio/lawallet-nwc/pull/386)）。プロバイダーは秘密鍵をインポートせずに署名でき、インポートは確認を経て行う別個の選択となる。そのスクリーンショットに示されているのはシミュレートされたデモ応答であり、実環境でのクロスオリジンサインインの証拠ではない。

同じくリリースへの収録が確認されていない別のマージにより、NWCおよびLightningアドレスのコールバックは、[make_invoiceのエラーだけを理由にユーザーのリモートウォレットを置き換えることがなくなった](https://github.com/lawalletio/lawallet-nwc/pull/389)。代わりに、生存確認と残高確認によってウォレットを維持し、503を返すことができる。サービスは残高と保護資金の状態も記憶し、Restore（復元）オプションも追加する。そのしきい値と、それ以前の不明な履歴によって保護できる範囲は限られるため、すべての資金の安全を保証するものではない。デプロイや、ユーザーアカウントの復元が行われたとは主張されていない。

### KithMoot {#kithmoot}

ルームチャットと通話のためのNostrベースのアプリ[KithMoot](https://github.com/forgesworn/kithmoot)は、発行元の公開サービスなしで動作するようになった。10月21日から23日にかけて、発行元は[公開ミーティングコード、共有TURNサービス、ファイルアップロード、保存済みファイルの読み出しを廃止した](https://github.com/forgesworn/kithmoot/pull/535)。ミーティングコードは招待リンクに置き換えられ、公開ファイルはデフォルトでYakihonneに送られて初回送信時に通知が表示されるが、ユーザーは独自のサーバーを選ぶこともできる。通話は引き続きまず直接接続を試みる一方、Hide IPには動作するTURNサーバーが必要で、直接接続にフォールバックすることはない。デスクトップ0.1.102とAndroid 0.6.106では、[発行元のSTUNがCloudflareの公開STUNに置き換えられ](https://github.com/forgesworn/kithmoot/pull/548)、ユーザーは独自のものを設定できる。[配信されていたバックアップのコピーは削除された](https://github.com/forgesworn/kithmoot/pull/543)が、[オフラインの暗号化コピーは残っている](https://github.com/forgesworn/kithmoot/pull/545)。[デスクトップ0.1.109とAndroid 0.6.121](https://github.com/forgesworn/kithmoot/pull/596)は、デバイスの認証情報が期限切れになると下書きを保持したままチャットをブロックし、任意のディレクトリ検索とは[別にユーザー自身のプロフィール名を読み込む](https://github.com/forgesworn/kithmoot/pull/594)。通常の通話エンジンは実験的な[リアルタイムSDKプレビュー](https://github.com/forgesworn/kithmoot/pull/561)には切り替わっておらず、[MLSグループの候補](https://github.com/forgesworn/kithmoot/pull/583)もデフォルトでは無効のままである。

[デスクトップ0.1.110](https://github.com/forgesworn/kithmoot/releases/tag/v0.1.110)では、デスクトップとWebで画像、音声、動画、PDFを表示する[サンドボックス化された添付ファイルビューアー](https://github.com/forgesworn/kithmoot/pull/597)が追加された。デスクトップでは、Nodeへのアクセス、アプリケーションストレージ、外部ネットワークへのアクセスをいずれも持たない、専用かつ非永続のElectronレンダラー内で動作する。ストリーミングには上限があり、ビューアーは閉じられたとき、またはメッセージが取り消されたときにクリーンアップされる。プルリクエストのWebKitでの実行と、パッケージ版で悪意あるSVGを使った追加の実行は途中で停止しており、検証済みとはされていない。また、これらはいずれもセキュリティ認証ではない。macOSビルドは公証済みだが、Windows版は未署名のプレビューのままだ。

0.1.110に含まれていることが示されていない後続のマージは、スリープ後と送信前に[期限切れのデバイス認証情報を実時間（ウォールクロック時間）に基づいて更新し](https://github.com/forgesworn/kithmoot/pull/605)、署名者の応答を待つ間も下書きを保持する。これは、テスターのスリープ中のノートPCで認証情報が一晩のうちに期限切れになった事例を受けたものだ。応答が返ってこない署名者リクエストは依然として更新を保留させ、Androidには更新に関する別の未解決の問題がある。ソースのカットオフ時点で未マージのオープンなプルリクエストは、[Help other people connectを一時停止する](https://github.com/forgesworn/kithmoot/pull/606)ものだ。作成者によると、アプリはピア支援のペアをそのメディアを中継しないまま受け入れてしまい、それによってフォワーダーやTURNへのフォールバックが止まり、無音の通話になることがあるという。ライブラリのデフォルトは変更されない。

### Marmot TS {#marmot-ts}

Marmot暗号化グループメッセージングプロトコル向けのTypeScriptライブラリ[marmot-ts](https://github.com/marmot-protocol/marmot-ts)が、破壊的変更を含む[v0.8.0](https://github.com/marmot-protocol/marmot-ts/releases/tag/v0.8.0)と[v0.9.0](https://github.com/marmot-protocol/marmot-ts/releases/tag/v0.9.0)をリリースした。暗号化メディアV2ではソースのバインディングが加わり、遅れて届いたメディアを再起動後に復号できるようになった。Blossomのアップロード記述子、送信先、暗号文は、署名の前に検証される。永続化されたグループはページ単位でバックフィルされ、不確定なコミットはリトライされる。アプリは今後、耐久性のある取り込み用ストアとリワインド用ストアを提供する必要があり、そのアダプターは失敗またはタイムアウトした読み取りを拒否しなければならない。V1ヘルパーは履歴用にのみ残されるため、レガシーのV1グループは作り直す必要がある。

その後マージされたソースでは、[キーパッケージ、招待、履歴の各ウォッチャーにオプションのAbortSignalが追加された](https://github.com/marmot-protocol/marmot-ts/commit/bce57044f91251040807b1c0fd7a739046ee2f4e)。これらのリスナーは、ストレージの読み取りがまだ保留中であっても、return、throw、または破棄の時点で速やかにクリーンアップされる。コンシューマーが一時停止している間に届いた変更はラッチされ、1つの更新にまとめられる。キャンセル後も、基盤となるバックエンドの読み取りは継続する。クエリの失敗は引き続きrejectされ、この変更は実行時の相互運用性を保証するものではない。

### Nostrメールクライアント {#nostr-mail-client}

Nostr上に構築されたメールクライアント[nostr-mail-client](https://github.com/nogringo/nostr-mail-client)は[v0.19.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.19.0)をリリースし、bunker、nsec、ncryptsecに対応する単一のログインフローを導入した。このフローには、リモート署名者のauth_urlの承認も含まれる。DM、受信箱、送信箱、プライベートの各relayリストの変更には再ログインなしで追従するようになり、同期中のメール通知は重複排除され、メール署名は暗号化された形でデバイス間で同期される。25 MBの上限を超えるメール添付ファイルは通知とともに破棄され、Nostr専用のアドレスはメールから送られた返信を受け取れない。

### Napplet適合性CLI {#napplet-conformance-cli}

napplet（署名済みNostr eventとして配布されるWebアプリ）向けのWebパッケージとツール群である[napplet/web](https://github.com/napplet/web)は、前号で取り上げた検証作業を、バージョン付きの[@napplet/conformance-cli 0.4.0](https://github.com/napplet/web/releases/tag/%40napplet/conformance-cli%400.4.0)として提供するようになった。ヘッドレス実行の前に、CLIはマニフェストのevent ID、署名、生のHTMLの正確なハッシュを確認し、ランタイムバインディング、名前空間、インストールの失敗をnappletのエラーとは区別して報告する。組み込みのフォールバックが対応するのはRESOURCEとGAMEPADだけであるため、カスタムホストはソースとスナップショットの入力を明示的に渡す必要がある。

[Nappletのdeployコマンドは、デフォルトでZapstoreの掲載情報を準備するようになった](https://github.com/napplet/web/pull/265)。選択された各ビルドのスクリーンショットを撮影し、kind 32267のSoftware Application eventを準備する。`--no-screenshot`と`--no-zapstore`でこれらの手順を無効にできる。メタデータの準備はリリースの公開ではなく、この変更によってパッケージのリリースやアセットのeventが追加されるわけでもない。

### napplet-soy {#napplet-soy}

[napplet-soy](https://github.com/soytec/napplet-soy) は napplet をビルドして公開するためのワークスペースで、コマンドラインツール soyli に [v0.31.2](https://github.com/soytec/napplet-soy/releases/tag/soyli-v0.31.2) と [v0.31.3](https://github.com/soytec/napplet-soy/releases/tag/soyli-v0.31.3) のタグを付けました。これらは Studio のデプロイではありません。Git での配信が確認されると、公開処理は正確な祖先関係とターゲット、さらに現在のリビジョンを確認したうえで、含まれる Git コラボレーション([NIP-34](/ja/topics/nip-34/))の提案をマージ済みとしてマークします。再開時には事前署名済みのステータスを再利用します。より新しい提案リビジョンはオープンのまま残ります。また、あるコミットを含むタグがあっても、ターゲットブランチがそのコミットをマージした証拠とは見なされません。これらのタグの元になったソースは、統合された Manage ワークスペースに初期の Cashu ウォレット([NIP-60](/ja/topics/nip-60/))ビューも追加し、タブを切り替えても実行中の napplet を維持します。それ以前の [v0.31.1](https://github.com/soytec/napplet-soy/releases/tag/soyli-v0.31.1) のアップデーターは安定した GitHub リポジトリ ID を追跡するので、Soytec への移行後もインストール環境はアカウントとプロジェクトを保持します。古いアップデーターを使っているインストール環境では、インストーラーを一度実行する必要があります。

[NIP-60 Cashu ウォレット](https://github.com/soytec/napplet-soy/pull/39)は [NIP-61](/ja/topics/nip-61/) の nutzap を償還し、準備済みの mint 出力と署名済みの relay 更新を実行前に保存します。そのため、結果が不確かなリクエストも、支払いを繰り返さずに復旧できます。ウォレットはアカウントごとに分離されたままで、複数のブラウザタブが同時に支払いを行うこともできません。ただし、テストには偽の mint が使われており、実際のお金での相互運用性は検証されていません。[コントリビューションページが作者宛ての zap に対応しました](https://github.com/soytec/napplet-soy/pull/42)。支払先は、選択したリリースまたは提案に署名した作者です。

[soyli v0.31.4](https://github.com/soytec/napplet-soy/releases/tag/soyli-v0.31.4) のタグには、作者のコントリビューション履歴と zap、さらに [NIP-5D の準備完了処理、オーディオ、テストに関する変更](https://github.com/soytec/napplet-soy/pull/43)が記載されています。ドメイン呼び出しは、shell が準備完了を報告するのを待たなくなりました。napplet が NAPMEDIA を通じて所有するオーディオは共有ホストが調整し、iframe の分離は緩められません。このタグも Studio のデプロイではありません。設定された 5 つのチェックが合格し、5 つはスキップされました。完全な準拠はまだ証明されておらず、修正されたアプリは再公開を待っています。

### Pakstr {#pakstr}

[Pakstr](https://git.nostrdev.com/stuff/pakstr) は Android アプリをビルドして Nostr に公開するコマンドラインツールで、[v0.29.1](https://git.nostrdev.com/stuff/pakstr/releases/tag/v0.29.1) のタグを付けました。公開前には、[APK が v2 または v3 の署名ブロックで主張する署名者証明書を読み取り](https://git.nostrdev.com/stuff/pakstr/commit/4dbdbec3bec10bef3f96c42a8324e0fc1a10d5c5)、その SHA-256 を期待されるサイドカーおよび ID 証明と照合します([公開のレビュー](https://git.nostrdev.com/stuff/pakstr/pulls/108))。未署名、不正な形式、または複数の証明書を持つ APK は拒否されます。再ビルド時には古いサイドカーが削除され、公開用の nsec が無効な場合はビルド前に失敗します。パーサーは APK の署名そのものは検証せず、それは Android と apksigner に任されています。したがって、古いビルド、未署名のビルド、誤った証明書のビルドは検出できますが、ビルドが偽造されていないことは証明できません。ZIP64、複数の署名者、鍵のローテーションはサポートされていません。

### MDK {#mdk}

Marmot 暗号化グループ向けの SDK およびランタイムである MDK が、[安定版 v0.14.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.14.0) をリリースしました。メディアファイルの受け渡しとストレージ、順序付きのオフライン追いつき、フォローリストの保持、SQLCipher の raw キーによる再鍵化を備えており、MLS とワイヤーフォーマットは変更されていません。[0.14.0 リリースガイド](https://github.com/marmot-protocol/mdk/blob/v0.14.0/docs/release/0.14.0.md)と [0.14.0 統合ガイド](https://github.com/marmot-protocol/mdk/blob/v0.14.0/docs/integration/0.14.0.md)は、バインディング、ネイティブライブラリ、ヘッダーを互いに一致したセットで同梱するようアプリに求めています。[MarmotKit 0.14.0](https://github.com/marmot-protocol/mdk/releases/tag/marmotkit-v0.14.0) は、このセットを Apple と Android 向けにパッケージ化しています。Apple プラットフォームではバイナリが raw の静的 XCFramework なので、アプリはそれを対応する Swift バインディングと組み合わせ、その PrivacyInfo.xcprivacy リソースを自ら割り当てたラッパープロダクトにコピーします。リリースのアーカイブチェックに合格しても、App Store へのエクスポートが成功することの証明にはなりません。データベースとストレージの移行は一方向で、すべてのページが一度ずつ再鍵化されます。ダウングレードは引き続きサポートされません。アカウントのメディアと受け渡しデータは、バックアップから除外すべきです。WN エージェントはまだプレリリースで、クレートは crates.io に公開されていません。既知の制限も残っています。5 エポックを超えて遅れて届いた履歴は、通知なしに復号不能になります。エポックの進行をまたいで転送中に失われたメディアの問題は修正されておらず、グループコンテキストの順序に関する互換性の問題も残っています。

タグの祖先関係を見ると、安定版タグには同期とメディアに関する 5 つの変更も含まれています。[グループサブスクリプションの更新では、変更された REQ バッチファミリーだけが再パックされます](https://github.com/marmot-protocol/mdk/pull/2583)。失敗したファミリーは次の同期に向けてライブルートを保持しますが、部分的なコミットは引き続き同期の失敗を報告します。[送信前の更新が失敗しても、送信とグループ変更は引き続き永続キューに入ります](https://github.com/marmot-protocol/mdk/pull/2567)。ただし、完了状態は CompletionUnknown のままになることがあります。[到達不能な relay の REQ は、再接続まで同じ ID のまま未処理として保持されます](https://github.com/marmot-protocol/mdk/pull/2572)。そのため、劣化したカバレッジは完全な履歴を意味しません。[オンボーディングの修復承認は、すべての検出ソースを待ちます](https://github.com/marmot-protocol/mdk/pull/2545)。宣言されたソースがタイムアウトした場合は RetryableFailure を返します。[オプトインのアカウント単位のメディア保持](https://github.com/marmot-protocol/mdk/pull/2541)は、Keep forever から 30 日までの範囲で設定でき、受信時刻または最後の明示的な再ダウンロードを基準にメディアを削除します。最後に閲覧した時刻は基準になりません。メッセージ履歴は削除されません。ホストは新しい CleanedBySetting FFI 値を処理する必要があります。

タグの後も、マージされたソースではマルチデバイスとプッシュの作業が続きましたが、それを含むと謳うリリースはまだありません。[参加後の履歴リクエストは](https://github.com/marmot-protocol/mdk/pull/2635)コミットや再起動をまたいで永続化され、Welcome とライブメッセージの間の空白を埋めます。[メンバーをアカウント単位で数えることで](https://github.com/marmot-protocol/mdk/pull/2634)、2 台目のデバイスが参加または離脱したときに、ある人物について誤った通知が出なくなります。また、[Welcome の処理は兄弟デバイス宛ての配信を無視し](https://github.com/marmot-protocol/mdk/pull/2633)、それによって参加が失敗したり鍵が消費されたりすることはありません。プッシュについては、MDK は[新しいプッシュ gossip ストレージ](https://github.com/marmot-protocol/mdk/pull/2617)上で[コミット後に所有者署名済みのレコードと tombstone を gossip し](https://github.com/marmot-protocol/mdk/pull/2620)、[メンバー追加後にトークンを再共有し](https://github.com/marmot-protocol/mdk/pull/2613)、[受信者のすべてのデバイスに通知します](https://github.com/marmot-protocol/mdk/pull/2609)。ただし、送信者自身のデバイスには依然として通知が届きません。[トリガーごとに新しいランダムパディングを付ける](https://github.com/marmot-protocol/mdk/pull/2608)ことで、重複排除によって起動通知が抑制されるのを防ぎます。[KeyPackage の公開ではアカウント自身の relay リストが採用されます](https://github.com/marmot-protocol/mdk/pull/2594)。リストが不完全な場合や使用可能な relay がない場合は、保存済みのリストを保持したまま失敗します。[型付きの古いエポック(stale-epoch)および未確定(unsettled)のメディアステータス](https://github.com/marmot-protocol/mdk/pull/2312)は、再アップロードすべきか、同期して再送すべきかをアプリに伝えます。さらに、[転送状態の変化は即座に通知され、バイト単位の進捗はまとめて送られます](https://github.com/marmot-protocol/mdk/pull/2311)。

より新しいアカウントデバイス関連のソースは、後のリリースに向けた進捗であり、安定版 0.15 ではありません。10 月 28 日付のナイトリー 3 つはテスト専用と表示されており、コミット b8d0a49 に固定されています。このコミットは後のマージより前のものなので、それらのアセットにはその内容がすべて含まれているわけではありません。MDK は、アカウントごとに最近の最大 20 台のデバイスについて、[デバイスごとに互換性のある KeyPackage を選択します](https://github.com/marmot-protocol/mdk/pull/2649)。[サインアウトすると、このデバイスの公開スロットだけが撤回されます](https://github.com/marmot-protocol/mdk/pull/2654)。[新しいパッケージの有効期間は 30 日と 1 時間で、公開から 6〜7 日後に更新されます](https://github.com/marmot-protocol/mdk/pull/2643)。検出処理はすべてのデバイスを探しますが、relay の障害によって一部が漏れることがあります。再招待で解決する場合もありますが、自動的に復旧する保証はありません。[認証済みのリーフ単位の機能チェック](https://github.com/marmot-protocol/mdk/pull/2645)が、アカウント単位のキャッシュに取って代わります。すべての創設者が対応している場合、[新しいグループはアカウントデバイスコンポーネント 0x800d を必須とし](https://github.com/marmot-protocol/mdk/pull/2656)、[アップグレードされたデバイスはこれを広告するようになりました](https://github.com/marmot-protocol/mdk/pull/2659)。そうしたグループは、これを持たない古いデバイスを拒否しますが、既存のグループは変わりません。この要件の下で MDK は、[コンポーネントデータ、未対応のリーフ、アカウントあたり 20 を超えるリーフ、そして要件を取り除こうとする試みを拒否します](https://github.com/marmot-protocol/mdk/pull/2637)。レガシーなグループと要件のないグループは、そのまま残されます。これとは別に、[スキーマにデータを持たないアプリコンポーネントについては、ホストが提供する初期データを拒否します](https://github.com/marmot-protocol/mdk/pull/2662)。この拒否は、グループ、Welcome、event のいずれかが作成される前に行われます。

0x800d グループでは、エンジンに[親の状態を考慮したコミット分類を伴う、自アカウントによる追加と削除の権限](https://github.com/marmot-protocol/mdk/pull/2650)が加わり、self-update、self-remove、同一アカウント、admin の各コミットが区別されます。同一アカウントの特権には、by-value の提案が必要です。[対応する Welcome の処理は、同一アカウントからの Welcome を受け入れます](https://github.com/marmot-protocol/mdk/pull/2646)が、それはこれらのグループに限られ、しかもコンポーネント状態と署名のチェックを経た後に限られます。その他のグループでは、引き続きアクティブな admin が必要です。[自アカウントの追加と削除の送信インテントは、スケジューラーで公平に順番を割り当てられます](https://github.com/marmot-protocol/mdk/pull/2655)。ただし、アプリの API はまだ同一アカウントの送信インテントを公開していません。[デバイス自身のリーフが削除されたかどうかで、そのデバイスのローカルなメンバーシップが決まるようになりました](https://github.com/marmot-protocol/mdk/pull/2640)。そのため、兄弟デバイスが存在していても、削除されたデバイスのメンバー操作が維持されることはなくなりました。

プッシュ gossip には、[レコードと tombstone の 8 バイトのダイジェストプレフィックスを運ぶ、永続的にキューイングされる kind 447 アナウンス](https://github.com/marmot-protocol/mdk/pull/2648)が追加されます。これは参加時、レコード変更時、そして 7 日ごとのメッセージ周期で送信されます。ピアは、順位付けされ時間差を付けた応答によって[欠落している所有者署名済みレコードを修復します](https://github.com/marmot-protocol/mdk/pull/2658)。その際、重複は抑制され、リーフごとに 24 時間の上限があります。リカバリーでは、[cut と cancel が新たな損失をでっち上げなくなりました](https://github.com/marmot-protocol/mdk/pull/2673)。進展のない試行が 24 回続くと、その義務は不完全な履歴の警告の背後で保留されます。[カバレッジ台帳](https://github.com/marmot-protocol/mdk/pull/2667)はシャドーレコーダーとしてのみ動作します。一方、[時間分割スイープ](https://github.com/marmot-protocol/mdk/pull/2665)は古いものから順にスライスを再開しますが、本番用のスケジューラーはまだありません。[オプトインの監査ファイル](https://github.com/marmot-protocol/mdk/pull/2664)は最後の書き込みから 30 日後に期限切れとなり、起動時と 1 時間ごとにクリーンアップされます。実際の削除は 1 日遅れることがあります。別個の鍵開示セキュリティログは、この期限切れの対象外です。

[ペアリング用クレート](https://github.com/marmot-protocol/mdk/pull/2670)は、一時的な X25519、コミットメント、ユーザーが両方の画面で確認する 7 つの絵文字の比較、そして ConfirmedLink で終わる HMAC 確認を使います。そのワイヤーアダプターはトランスポートのみを扱い、仕様が定まるまでデフォルトで無効になっています。UI、および Welcome とグループリンクに関するフォローアップは未完成で、この実装の相互運用性は未検証のままです。[デバイス名簿 0x800e のソース](https://github.com/marmot-protocol/mdk/pull/2666)は、非表示の単一アカウントグループに差分更新を適用します。ただし、0x800e を広告するにはテストポリシーのオーバーライドが必要なので、本番ビルドではまだデバイスグループを作成することも、それに参加することもできません。

MDK のその他の提案は、まだオープンのままです。そのひとつは、[NIP-67](/ja/topics/nip-67/) の[完了を完全なカバレッジの証明として扱うのをやめる](https://github.com/marmot-protocol/mdk/pull/2674)提案です。スケジュールされていないスイープでは、完全性が保証されないためです。ほかに、[チェックポイントのリプレイ](https://github.com/marmot-protocol/mdk/pull/2671)、[自動再参加](https://github.com/marmot-protocol/mdk/pull/2661)、[既存グループでの 0x800d の有効化](https://github.com/marmot-protocol/mdk/pull/2668)を追加する提案もあります。改めてステータスを確認したところ、以前のネイティブ API 提案 3 件もまだオープンでした。[過去の添付ファイルの復旧](https://github.com/marmot-protocol/mdk/pull/2614)は、ソーススロットを調べ、認証済みのダイジェストと有効期限を確認してから、検証済みのバイトを非公開のリース済みファイルに書き込むもので、タイムラインはネットワークを使わないままになります。配信されたコピーはスナップショットであり、取り消すことはできません。[フィルター全体のチャット選択ハンドル](https://github.com/marmot-protocol/mdk/pull/2592)は、読み込まれたページを超えてフィルターに一致するすべてのチャットを対象としつつ、後から届いたチャットは除外するものです。また、[wn-agent のグループ作成における創設 admin の選択](https://github.com/marmot-protocol/mdk/pull/2587)は、招待された創設 admin を選び、アップロード前にメンバー以外を拒否するものです。

### nosfry {#nosfry}

Rust で書かれた Nostr relay である nosfry が、ネイティブ版と Workers/SQL 版向けに [nosfry v0.2.0](https://github.com/qntx/nosfry/releases/tag/v0.2.0) をリリースしました。v0.1 の時点では未リリースだった機能が含まれています。具体的には、[NIP-09](/ja/topics/nip-09/) の削除、[NIP-40](/ja/topics/nip-40/) の有効期限、[NIP-70](/ja/topics/nip-70/) の保護された event を伴う NIP-42 AUTH、[NIP-45](/ja/topics/nip-45/) の COUNT、[NIP-77](/ja/topics/nip-77/) の Negentropy 同期、[NIP-62](/ja/topics/nip-62/) の消去リクエスト、そして [NIP-86](/ja/topics/nip-86/) の管理 API です。さらに、送信予算と書き込みポリシーを備えた上限付きサブスクリプションを追加しており、permessage-deflate はデフォルトで有効だと説明しています。性能と準拠に関する主張は独立して再現されておらず、すべての実装との相互運用を主張しているわけでもありません。

0.3 タグの後、10 月 25 日に 4 つの堅牢化の変更がマージされましたが、リリース済みのバイナリには含まれていません。Worker の接続とレートのバケットは IPv6 を /64 単位で集約しますが、NIP-86 の IP ブロックリストは引き続き正確なアドレスで照合します([#78](https://github.com/qntx/nosfry/pull/78))。また、NEG-OPEN のスキャンは、収集中にグローバルな同期メモリ予算を 1024 レコード単位で消費します([#73](https://github.com/qntx/nosfry/pull/73))。同じタイムスタンプを持つタイグループでは、クエリの上限によって制限されたヒープが保持されます([#72](https://github.com/qntx/nosfry/pull/72))。NIP-86 のモデレーションスナップショットは、リクエスト時点で取得された内容のまま、保存済みデータの読み取りとライブ配信に適用されます。そのため、開いているリクエストに新しい ban が即座に反映されることはありません([#68](https://github.com/qntx/nosfry/pull/68))。

同じく未リリースの別のマージは、[ライターを 64 MiB のバイト予算で制限し](https://github.com/qntx/nosfry/pull/79)、公開のバックログをより大きなトランザクションで処理します。各トランザクションの上限は実行した作業量で決まり、LMDB の永続的な同期は維持されます。プロジェクトのベンチマーク数値は独自のプローブバリアントによるもので、私たちが測定したものではありません。

### nostream {#nostream}

TypeScript製のNostr relayであるnostreamが、[nostream 3.7.0](https://github.com/cameri/nostream/releases/tag/nostream%403.7.0)と[nostream 3.8.0](https://github.com/cameri/nostream/releases/tag/nostream%403.8.0)をリリースした。以前はソース上のみの存在として報じた管理操作、監査ログ、署名付きwebhook、メトリクスが、バージョン3.7.0で正式に出荷された。有料書き込み向けにオプトイン方式のライフサイクルが追加され、LNbits 1以降に対するISO時刻の解析と有効期限の処理も修正された。静的ミラーリングは削除され、その設定は現在、NIP-77同期を優先するため警告付きで無視される。3.7.0のコンテナイメージは、Dockerタグに不正な `@` が含まれていたため公開に失敗しており、3.8.0ではタグが修正されたうえ、失敗したイメージビルドの再実行も追加された。さらに3.8.0では、pubkeyとkindのリスト、IPおよびレート制限のバイパス制御が管理APIとコンソールに加わり、上位の発行者、IP、レート制限の発動回数に関する統計も得られる。レート制限戦略の切り替え時やアップグレード時に起きていたRedisキーの衝突も修正された。ソースだけではイメージが現在正しく公開されていることは確認できず、課金機能が実運用に展開されたという主張もない。

これとは別に、`rewrite/main` ブランチで進むRustによる書き直しでは、実際のクライアントに応答する最初のワイヤーコアが[740ef69](https://github.com/Cameri/nostream/commit/740ef699fb04f3f54bd82a9d012e27c04dabb480)でマージされ、[2b2287f](https://github.com/Cameri/nostream/blob/2b2287f8acc43b1e0b3039c745c88a03268831aa/crates/nostream-relay/src/strategies/mod.rs)の時点ではストラテジーレジストリが残る14個のストラテジーアームを実装している。デフォルトではないこのプロトタイプは、TypeScript版の `main` や安定版の3.xリリースとは切り離されたままだ。そのレビューとCIの結果は作者自身によるものである。[NIP-43](/ja/topics/nip-43/)と[NIP-56](/ja/topics/nip-56/)の処理は、デフォルトで無効のままとなっている。vanishリクエストは同時に行われた公開との競合に負ける可能性が依然としてあるため、vanishはプライバシーを保証するものではない。アクセスおよびIDに関するコードについて作者が求めている手動レビューの要請は、現在も有効だ。

### swift-nostr {#swift-nostr}

Swift用のNostr SDKであるswift-nostrは、10月27日に[0.9.0](https://github.com/yysskk/swift-nostr/releases/tag/0.9.0)を公開した。このリリースでは、型付きのキー、event ID、URL、タイムスタンプ、座標、サブスクリプションIDが追加された。ローカルでもリモートでも任意の署名者が署名できるEventTemplate、型付きエラー、プールが所有するサブスクリプション、そしてプール経由、指定したrelay、またはNIP-65 outboxを通じたRelayRouteルーティングも加わっている。Event.verifyは不正な署名に対して例外をスローするようになったため、0.8からの移行にはソースの変更が必要だ。それ以前の[0.8.0](https://github.com/yysskk/swift-nostr/releases/tag/0.8.0)は堅牢化のためのリリースで、リリースノートによれば、置換可能なevent、gift wrapの送信者、NIP-46およびNWCの応答を検証し、複数relayからの応答の重複を排除し、署名者主導または共有鍵によるNIP-44暗号化を追加したという。破壊的変更として、zapのチェックも厳格化された。これらは作者の主張であり、監査によるものではない。

以前取り上げた0.8以降の修正は、0.9.0で出荷された。署名者は[自身のものと異なる公開鍵を持つeventを拒否する](https://github.com/yysskk/swift-nostr/pull/239)ようになり、[購読解除の際にCLOSEを送るためだけに切断済みのrelayへ接続を開くこともなくなった](https://github.com/yysskk/swift-nostr/pull/238)。コアの送信呼び出しはnotConnectedをスローし、購読は明示的に接続を行う。ただし、NWCとNIP-46のトランスポートは、新しいリクエストのために切断されたrelayへ引き続き再接続する。NWCとリモート署名者の呼び出しには[型付きエラーと即時キャンセルが導入された](https://github.com/yysskk/swift-nostr/pull/247)が、すでに送信済みのリクエストは処理されてしまう可能性が残る。NWCの通知ストリームと認証チャレンジのストリームは[relayが終了すると終わる](https://github.com/yysskk/swift-nostr/pull/242)ようになった。接続待機は[すべてのrelayストリームが終了した時点で失敗し](https://github.com/yysskk/swift-nostr/pull/244)、[フィルタのtagクエリは一度だけ格納される](https://github.com/yysskk/swift-nostr/pull/241)ことで、tagごとにJSONキーが1つになった。汎用の[WalletConnectRequest](https://github.com/yysskk/swift-nostr/pull/232)は、通常のresult_typeとエラーのチェックを伴うカスタムの単一応答型[NIP-47](/ja/topics/nip-47/)メソッドをサポートし、multi_payは別扱いのままとなる。拡張可能な[RemoteSignerMethod](https://github.com/yysskk/swift-nostr/pull/229)は、組み込みのセット以外のNIP-46メソッドを呼び出し、結果の文字列を返す。いずれの場合も、ウォレットまたは署名者がそのメソッドをサポートしている必要がある。[EventTemplateとsigner.sign](https://github.com/yysskk/swift-nostr/pull/214)により、以前はローカルのEventSignerを必要としたzapリクエストなどのヘルパーを、リモートのNIP-46署名者でも使えるようになった。これに伴い、[いくつかのデータモデル](https://github.com/yysskk/swift-nostr/pull/215)、[NIP-29](/ja/topics/nip-29/)および[NIP-98のビルダー](https://github.com/yysskk/swift-nostr/pull/216)にも関連する変更が加えられている。この変更が変えるのはAPIであり、ワイヤーフォーマットではない。

0.9.0のタグ以降にマージされたコードは、そのリリースには含まれない。呼び出し側が[送信をキャンセルしても、正常なrelayは維持されるようになった](https://github.com/yysskk/swift-nostr/pull/257)。また、[DMのオープンと結果の型が簡素化され、rumorの作者は署名者に結び付けられた](https://github.com/yysskk/swift-nostr/pull/260)。[FileAttachmentは暗号化ファイルのメタデータを統一する](https://github.com/yysskk/swift-nostr/pull/261)。[単一のsetSignerとremoveSignerのペア](https://github.com/yysskk/swift-nostr/pull/262)によって、古くなったリモートでの設定処理がサインアウトを取り消してしまう問題が防がれる。removeSignerはAUTHへの応答を止めるが、すでに送信済みのリモートリクエストを取り消すことはない。[再接続と重複排除の設定には、それぞれ専用の設定型が用意された](https://github.com/yysskk/swift-nostr/pull/263)。

### haps {#haps}

Nostr鍵で署名されたソフトウェアのインストーラーであるhapsが、[haps v0.1.22](https://github.com/mmalmi/haps/releases/tag/v0.1.22)をリリースした。これは[haps v0.1.18](https://github.com/mmalmi/haps/releases/tag/v0.1.18)を土台としている。v0.1.18では、LinuxとmacOSのソースビルドを、プライベートなホームディレクトリと書き込み可能なチェックアウトの中で、デフォルトでネットワークアクセスを無効にして実行していた。明示的なallow-build-networkおよびallow-host-buildオプションで、この挙動を上書きできる。Windowsのソースビルドにはhost-buildが必要だ。インストールされたアプリはサンドボックスの外に置かれたままである。[haps v0.1.19](https://github.com/mmalmi/haps/releases/tag/v0.1.19)では、監査とインストールを一度で行う確認が追加された。この確認は固定されたソースとビルドレシピを、ビルドされたペイロードのハッシュに結び付けるため、一致する発行者のバイナリを、そのレビュー済みビルドのポリシーの下でインストールできる。信頼済みのレビューを再利用しても、別の独立した監査とはみなされない。不変の署名付きカタログからのインストールには引き続き監査が必要で、公開された警告については、デフォルトが「いいえ」となる別途の同意が求められる。バージョン0.1.22では、[上限付きのルックアップと、完全なソースを対象とする発行者チェック](https://github.com/mmalmi/haps/commit/606a1cd25ef8ff9f454adb0d89acb5d4c9605a35)が追加された。ルックアップは短い期限を共有するようになり、クライアントは[最初のrelayが接続した後にクエリを開始する](https://github.com/mmalmi/haps/commit/f58d7fa30e149c8f0e500bd7cd59da7e834cc61c)。スナップショット検索は、1回あたり3秒の予算内で見つかった検証済みの結果を返す。公開処理は、ソースrefを変更する前に、条件を満たす同梱のgitヘルパー、固定されたコンパニオンバイナリと一致する別途インストール済みのヘルパー、またはcomplete-blob-dag-v1を提示するヘルパーのいずれかが見つからない限り、実行を拒否する。ベースラインの依存関係レビューの対象範囲、シンボリックリンクとサイズのガード、上限付きのリトライは維持されているが、これは新たな独立監査ではない。コールドインストールが1回成功しただけでは、断続的な転送タイムアウトが修正されたことの証明にはならない。固定されたヘルパーバンドルも、依然としてホストのツールチェーンに依存している。

### Swarm、管理APIをNIP-98認証で保護 {#swarm-protects-its-admin-api-with-nip-98-authentication}

Nostrと連携するパブリッシングおよび管理サーバーであるSwarmは、[v0.2.0をリリースし](https://github.com/HiveTalk/swarm/releases/tag/v0.2.0)、既存のダッシュボード用cookieに加えて[管理API向けのNIP-98 HTTP認証](https://github.com/HiveTalk/swarm/pull/59)を導入した。サーバーが検証するのは、kind 27235 eventの署名、過去5分から未来1分までのタイムスタンプの許容範囲、HTTPメソッド、パスとクエリ、運営者が固定したpubkey、そして任意のペイロードハッシュだ。転送されたホストを受け入れる場合は、前段に信頼できるプロキシがあることが前提となる。以前は公開されていた `/environment` エンドポイントは、管理者認証が必要になった。

その後のマージでは、リンクされたチームメンバーのkind 1ノートを対象に、[Xへのオプトイン方式のクロスポスト](https://github.com/HiveTalk/swarm/pull/67)が追加されたが、リリースに含まれたかは確認されていない。予約投稿されたノートも、WebSocket経由で届いたノートも、同じ経路をたどる。`e` tagを含む返信はスキップされ、過去分の遡及投稿は行われず、重複はevent IDによって除去される。CMS側ではNIP-98認証が使われる。投稿はローカルのOAuthか、信頼された委任サービスに依存するため、分散型でもトラストレスでもない。本番のXサービスへの投稿は、まだテストされていない。

### fips2go、検証済みメッシュドメインへの直接リンクを有効化 {#fips2go-turns-on-direct-links-to-verified-mesh-domains}

fips2goは、Nostr上の告知（advert）を通じてピアとドメインの主張を見つけるAndroid向けメッシュクライアントで、バージョン0.9.6から[0.10.0](https://github.com/fr34aky/fips2go/releases/tag/v0.10.0)までをリリースした。バージョン0.10では、直近に検証されたドメインのうち最大2つについて、そのサーバーへの[直接リンクがデフォルトで有効になった](https://github.com/fr34aky/fips2go/pull/91)。対象となるのは、DNSSECまたは複数のリゾルバーを通じて固定されたドメインのみだ。これらのリンクは、スマートフォンのパブリックIPアドレスとオンラインのタイミングをそれらのサーバーに公開し、どのサーバーを選んだかを公開relayに明かすが、ユーザーは無効にできる。特定のサーバーとポートに対してすでに固定されているTXTレコードは、新たなNostrの主張なしで解決されるようになった。一方、新しいサーバー、移動したポート、ポートを含まないレコードは、引き続き待機する。ネットワークの切り替えで新しいVPNルートが必要になっても設定が変わっていない場合、アプリはトンネルだけを置き換え、ノード、リンク、セッションは維持する。ホットスポットの変更、その他の設定変更、障害時のフォールバックでは、これまでどおりノードが再構築される。

### fips-pub-domains、主張の取得前に固定済みルックアップへ応答 {#fips-pub-domains-answers-pinned-lookups-before-fetching-claims}

パブリックドメインからメッシュアドレスへのNostr署名付きバインディングを解決するfips-pub-domainsは、[0.2.9](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.9)と[0.2.10](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.10)をリリースした。特定のサーバーとポートに対して固定されたTXTレコードは、同じピンポリシーの下で、バックグラウンドでの主張の取得が完了する前に応答できるようになった。ただし、新しいサーバーやポートは引き続き主張を待つ。デスクトップの起動時とネットワーク変更後には、リゾルバーが最大16の固定済みサーバーをウォームアップするため、それらのサーバーとルーティングノードにオンライン状態が明らかになる。最初の20秒のバックオフの間は3秒ごとに再試行し、いずれかのサーバーが応答した時点で早期に終了する。

これらのタグ以降にマージされた2つの変更は、未リリースだ。[1つ目は `fips-ca` ServiceClaimロールを追加する](https://github.com/fr34aky/fips-pub-domains/pull/29)もので、このロールはポートを持たず、独自のDNSSECチェーンとattestationを備え、`fips-dns` とは分離されている。新たなPKIを立ち上げることも、DNSバインディングのポリシーを変更することもない。[もう1つはCLIのverifyコマンドとzoneコマンドを追加する](https://github.com/fr34aky/fips-pub-domains/pull/30)もので、これらはピンファイルを読み込むが、書き込みはしない。このコードでは、attestationは自身の直前のwitnessのみを保持し、他のロールのエントリは再検証される。require-previousオプションはデータの欠落を拒否するが、障害と存在しないレコードとを区別することはできない。

### Codr {#codr}

White Noiseの暗号化チャットを通じてデスクトップのコーディングセッションを操作するブリッジ、[Codr v0.8.0](https://github.com/tidley/codr/releases/tag/v0.8.0)は、ワーカーの更新機能を追加した。この更新はチャット内で確認される必要があり、10分以内に実行されなければならない。更新では、固定されたメンテナーからngitレコードを取得し、Blossomからはチェックサム検証済みのバイトを取得する。GitHubへのフォールバックはない。コネクタやストレージのコホートの変更は拒否され、起動に失敗した場合は古い実行ファイルが復元される。今のところ、この更新はテスト用フィクスチャに対してしか実行されていない。ファイルとメディアは、処理中のセッションを中断することなく届くようになった。上限は25 MiB、添付ファイルは4件までだ。オプションのGemini文字起こしは、復号した音声メモをGoogleに送信するもので、デフォルトでは無効になっている。リリース0.4から0.7では、スマートフォンからのテキストを処理中のセッションに届けられるようになり、/cancelとプロジェクト、エージェント、モデルのメニューが追加され、MDK 0.14への移行も行われた。0.13からの移行は一方向のみで、バックアップと承認が必要となる。

[オプトイン方式のオーナー専用コントロールチャット](https://github.com/tidley/codr/pull/7)（`control_chat=true`、デフォルトでは無効）は、次回のワーカー起動時にそのグループを作成する。`/new` は、チャットがリンクされる前にプロジェクトセッションを開始する。作成されたかどうかが不確かな場合、自動での再試行は行われない。

本稿の情報源の締め切り時点で未マージだったオープンなプルリクエストは、[新しいコーディングセッションのグループ作成](https://github.com/tidley/codr/pull/18)の際に、まだ書き込まれていないトランスクリプトを空として扱えるようにするものだ。無効または曖昧なトランスクリプトは、引き続き拒否される。これにより、新規の `/new` セッションで最初のプロンプトより前にスマートフォンへの招待を送る機能が復活することになるが、セッションの認可方法は変わらない。

### nostr-media {#nostr-media}

Nostrメディアをホストするためのプラグインである[nostr-media 0.17](https://github.com/fabianfabian/nostr-media/releases/tag/0.17)は、Blossomミラーリングを強化した。ミラーURLを取得する前に[署名付きkind 24242のハッシュ認可を確認する](https://github.com/fabianfabian/nostr-media/commit/f29e15e387a41c0d43b97d5b8643e287ccae88d4)ようになり、認可されていないリクエストはダウンロードせずに拒否される。取得にはWordPressの安全なHTTP APIが使われる。このAPIは公開されたHTTP(S)ホストのみを許可し、リダイレクトを検証するもので、上限は20秒、リダイレクト3回、128 MiBだ。ダウンロードしたバイトも、引き続きハッシュ化されてチェックされる。Authorization、X-SHA-256、X-Content-Typeヘッダーは、大文字と小文字を区別せずに照合される。サーバーサイドリクエストフォージェリに対する保護は、WordPressの安全なAPIの強度を超えるものではない。

### NosTube {#nostube}

Nostr上に構築された動画サイトである[NosTube](https://github.com/flox1an/nostube)は、侵害された認証局への信頼を取り除くため、[server 0.1.25](https://github.com/flox1an/nostube/releases/tag/server-v0.1.25)と[desktop 0.2.51](https://github.com/flox1an/nostube/releases/tag/v0.2.51)をリリースした。サーバーのRust製relayはWebSocket接続とHTTPS接続でその認証局を信頼しなくなり、イメージのビルドには固定されたDebianのシステムCAバンドルが必須となった。デスクトップ版のリリースでは、同じ緩和策がTLS層とalmondサイドカーに適用されている。これらのセキュリティ上の主張は、リリースノートに基づくものだ。その後のserver 0.1.27のリリースノートは、古いlibbrotli1を同梱しているとしてそのイメージについて「DO NOT USE」（使用禁止）と記し、0.1.28を案内しているが、0.1.28がリリースされたことは本稿では確認できていない。

### bitchat {#bitchat}

Bluetoothメッシュと Nostr上で動作するメッセンジャーである[bitchat](https://github.com/permissionlesstech/bitchat)は、[1.8.0](https://github.com/permissionlesstech/bitchat/releases/tag/v1.8.0)をリリースした。Nostrの位置情報チャット（geochat）向けのパフォーマンス改善と、DMのrumorに対するタイムスタンプの範囲制限が含まれている。アプリは、ユーザー自身のメッセージをニックネームではなく送信者IDで識別するようになった（[送信者識別の修正](https://github.com/permissionlesstech/bitchat/pull/1793)）。プライベートグループは作成者を固定し、メッシュのピアIDはgeohash DMに含まれない。パフォーマンスの数値はプロジェクト自身によるもので、本稿では再現していない。

ソースのカットオフ時点で未マージのオープンなプルリクエストは、最も近い5つのrelayと共有の5つのバックアップを経由してルーティングし、ルートあたりの接続数を10に制限することで、relay障害時にも地理チャットの接続を維持できるようにするものです([#1822](https://github.com/permissionlesstech/bitchat/pull/1822))。relayディレクトリが読み込まれる前はメッセージがキューに入り、サブスクリプションと保留中の書き込みはアイデンティティを変えずに移行される予定です。検証は作成者自身によるもので、対応するAndroid側の変更は別のプルリクエストになっています。

同じく未マージの別のオープンなプルリクエストは、Nostrトランスポートではなく独自の`LIVE_VIDEO_V1`フォーマットを用いて、[iOSおよびmacOSのBluetoothメッシュ上でのライブ映像](https://github.com/permissionlesstech/bitchat/pull/1827)を追加するものです。公開フレームには署名と鮮度チェックが施される予定です。DMフレームはNoise暗号化の内部で送られ、録画はメッセージとして送信されます。作成者は、AndroidからiPhoneへのストリームを受信できたと報告しています。iPhoneからの送信、iOS同士のペア、DMでのライブ映像は未テストです。

### ngit {#ngit}

Nostr上でGitのコラボレーションを行うためのコマンドラインツール[ngit](https://github.com/DanConwayDev/ngit-cli)が、[v3.0.4](https://github.com/DanConwayDev/ngit-cli/releases/tag/v3.0.4)をリリースしました。relay接続とAndroidでのHTTPSは、侵害された認証局をもう信頼しなくなりました。対話型プロンプトは空入力を防ぐようになり、コマンドはオフラインフィルターに従います。リモート追跡の更新では、まだ公開されていないコミットが保持されます。さらに診断機能は、ソースが存在しない場合と、クエリの結果が0件だった場合を区別して示すようになりました。

### Hasheus {#hasheus}

以前はverifyという名前だったファイル検証ツールは[Hasheus](https://github.com/tinfoilhash/hasheus)に改名され、[2.0.0](https://github.com/tinfoilhash/hasheus/releases/tag/v2.0.0)をリリースしました。Nostr上で公開されたハッシュと照合してファイルを確認するツールで、今回から信頼できる検証者から説明とURLを取得し、大きなファイルはチャンク単位でハッシュ化します。検証済みバナーが表示されるのは、公開されたファイルと完全に一致するものだけです。不正な形式のプロフィールの処理や検証者の重複排除にも対応し、relayが指定されていない場合はエラーを出します。チェックサムが一致すればファイル自体は確認できますが、そのファイルに関する公開者の主張まで確認されるわけではありません。

### Alby JS SDK {#alby-js-sdk}

[AlbyのJavaScript SDK](https://github.com/getAlby/js-sdk)が[9.0.0](https://github.com/getAlby/js-sdk/releases/tag/v9.0.0)をリリースしました。NWCクライアントは、公開した各リクエストについてrelayのOKを固定で5秒間待ち、届かなければNip47PublishTimeoutErrorで失敗するようになりました。一方、メソッドごとの応答タイムアウトは変わっていません。復号に失敗した応答はrejectされるようになり、relayの失敗テキストも保持されます([リクエストエラーの処理](https://github.com/getAlby/js-sdk/pull/597))。破壊的変更として非推奨のmulti_*メソッドが削除されたため、Nip47SingleMethodを使うコードはNip47Methodへ移行する必要があります。relayのOKはrelayがリクエストを受け付けたことを意味するにすぎず、支払いが成功したことを示すものではありません。

### Alby Hub {#alby-hub}

Nostr Wallet Connect経由でウォレットを提供するセルフホスト型Lightningノード、[Alby Hub](https://github.com/getAlby/hub)が[1.24.4](https://github.com/getAlby/hub/releases/tag/v1.24.4)をリリースしました。このパッチでは、ハブのNWCウォレットサービスが依存しているネイティブのLDKおよびGoのTLS接続から、侵害された認証局への信頼が取り除かれました。CLNのhold-invoiceプラグインの起動も修正されています。

### Orchard {#orchard}

Flatpakのソフトウェアカタログである[Orchard](https://github.com/Letdown2491/orchard)が、[0.3.0](https://github.com/Letdown2491/orchard/releases/tag/v0.3.0)をリリースしました。このリリースは、[ソフトウェアリリースの相互運用性](https://github.com/Letdown2491/orchard/pull/4)を[NIP-82](/ja/topics/nip-82/)と結び付けるとともに、ngitやその他のNIP-82ツールで公開するための[Flatpakアセットの準備](https://github.com/Letdown2491/orchard/pull/5)にも対応しています。NIP-82は番号の割り当ても採択もされていない、提案段階のソフトウェアカタログ仕様です。そのためOrchardが実装しているのは、今後も変更される可能性のあるドラフトです。

### Bell {#bell}

[Bell](https://njump.me/nevent1qvzqqqr4dupzpynsnxlt28xupkyf02qln9da4wuv3cg00gf7l3cu39hv6qdr3k9kqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpdljffezmc9dgwal6akc90mk3dye9gektu8s2cfptj37xrrt476wf42080)はNostrの会話を集約するAndroidアプリで、複数アカウントへの返信と引用を1つの時系列リストにまとめます。[0.1.0のリリースノート](https://njump.me/nevent1qvzqqqr4dupzpynsnxlt28xupkyf02qln9da4wuv3cg00gf7l3cu39hv6qdr3k9kqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzq0s4r2rh63clk2e97sr8kfx7874dequvnhdcf562ag28pwjxg3fmvvs3al)によると、いいね、zap、単純なリポスト、一般的なメンションは対象外です。アカウントはAmberを通じて署名するか、閲覧専用のまま使います。[0.6.0](https://njump.me/nevent1qvzqqqr4dupzpynsnxlt28xupkyf02qln9da4wuv3cg00gf7l3cu39hv6qdr3k9kqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqh7w3wy9773f599y90vm5c32xkr8uea57gvp3ce08x85254z06xvfrc5f8)から0.9.0までのリリースでは、アカウントごとのミュートルールと、複数選択でまとめて既読にできる未読のみの表示が追加されました。それらのリリースノートによれば、復旧時には署名済みの返信とリアクションがそのままの形で保持され、自動的に重複が生じることはありません。[0.10.0](https://njump.me/nevent1qqsdu5x6ca9npnef9kfmcavpf6qelacc86rvcufa35mf67kdxm6f36qzyzf8pxd7k5wdcrvgj75plx2mm2acerss77snalr3eztwe5q68rvtvqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetk09q3d2)と[0.10.1](https://njump.me/nevent1qqsyv7r8a0e82ltdhawfctcwrk5n5a9lejaart2q3hxkquqfqqzxdgszyzf8pxd7k5wdcrvgj75plx2mm2acerss77snalr3eztwe5q68rvtvqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetk8kg3j4)では、個々の投稿を端末上で非表示にできるようになり、取り消しや復元も可能です。非表示にしてもrelayから何かが削除されるわけではなく、新しい返信は引き続き表示されます。スパム報告は投稿とその作成者の両方を対象とし、明示的に選んだアカウントから公開で送信されるもので、非公開のブロックとしては機能しません。[0.11.0](https://njump.me/nevent1qqsytpz6d4ctsfvpzrdgx23m7542y8wzjnn0qsctk4p5pp2hnwyugrszyzf8pxd7k5wdcrvgj75plx2mm2acerss77snalr3eztwe5q68rvtvqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkjh2y3n)では、元の投稿と送信アカウントを確認したうえでリポストできるようになりました。誰が返信、リアクション、リポストを行うかは、アカウントのアバターで選びます。リポストを公開できるようになったからといって、単純なリポストの通知が集約されるようになったわけではありません。キャッシュされたスレッドは不完全なままの場合があります。また、オプトインのバックグラウンド受信はAndroidの電力およびネットワークのルールに左右され、常時接続や即時配信は約束されていません。

### SkateSpots {#skatespots}

[SkateSpots](https://njump.me/nevent1qvzqqqr4dupzqg88e9f588nx7wyz4wt0ura23w3yd4hmztqrkr95utwyvgachjepqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpas2cx4mzh73kytt49479xdtrs2q37llm848e0zhvs0y72296sv8c7ad0x)は、スケートスポットとショップのコミュニティマップです。バージョン1.7.4ではエンドツーエンド暗号化されたコミュニティチャットが追加されました。新しい端末はコミュニティのbotが自動的に承認し、管理者も承認できます。[1.7.0](https://njump.me/nevent1qvzqqqr4dupzqg88e9f588nx7wyz4wt0ura23w3yd4hmztqrkr95utwyvgachjepqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzq50n30vvchf923kmne5vj0ptk7ful6qldk37xva9x2ap2879e4rmaep40k)では、コミュニティrelayがスポットとショップの正式な情報源になりました。[1.7.3](https://njump.me/nevent1qvzqqqr4dupzqg88e9f588nx7wyz4wt0ura23w3yd4hmztqrkr95utwyvgachjepqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzp8g4ah0nqaj796uuw0me3ck37azyjxp8gs9e3munfd7v5542snvp5wm656)では、以前のリリースで導入されたプライベートなクルーチャットについて、Androidの招待用QRコードが修正されました。[1.7.8](https://njump.me/nevent1qqsppdcrel94afrsluvt0gz4s2k079yvmne776w0juak38js857zsdszyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkuwx9gn)、[1.7.10](https://njump.me/nevent1qqspp0kr4x4c6m5fw5glqtdv7r08jseq70mp8n224qqp6rzmm2rt5yszyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetke6cpl5)、[1.7.15](https://njump.me/nevent1qqsq375v0ucwszn7s6wdatn2c9fgyxrcalmt7yazedav5zypt5d4pkqzyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkj0vmg9)、[1.7.19](https://njump.me/nevent1qqsr7xkz9evx70q47nzqr5wlsfs7cpzxaxy2ymzhxh4h9thy2s62n9qzyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkgrmthk)、[1.7.20](https://njump.me/nevent1qqsxn8f0az09eg75tnsc7kxlf3spwe4vfvh633te9k3mcsf3nhl3thszyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkqddtl9)、[1.7.21](https://njump.me/nevent1qqsr9wdhzwznntvkcjzphdy0249esazdgg7k0spz370lw9mzj8jwsggzyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetk7dgt33)、[1.7.22](https://njump.me/nevent1qqspx5m53qxctceqmva3dkynkswukl6zrwl4gr6mu3r0zucdwt96muqzyqsw0j2ngw0xduug92uklc864zazgmt0kykq8vxtfckugc3m309jzqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetk977zdf)の各リリースは、このクルーチャットを拡張しています。コミュニティチャットのbotによる承認とは異なり、新しい端末は既存のクルーメンバーがQRで承認します。メンバーや端末は削除でき、創設者を昇格させるとadmin tagが再公開されます。リアクション、削除tombstone、既読通知は、暗号化されたMLSコントロールとして送られます。tombstoneはrelay上での完全な削除ではなく、自動の既読通知はサイレント署名者からしか送られません。バックグラウンドのウォッチャーは、管理者の鍵ではなく必ずメンバー自身の鍵を使い、参加リクエストをおよそ1分ごとに[NIP-17](/ja/topics/nip-17/)のDMまたはベル通知に変換します。Amberユーザーの場合、参加通知はベルを開くまで待機しますが、サイレント署名者は事前に読み込めます。そのため、バックグラウンドでAmberにプロンプトが表示されることはありません。未読数は保留中のNIP-17エンベロープIDを復号せずに使って算出され、ユーザー自身が送信したコピーは除外されます。会話の主題を明かしたり確認したりすることもありません。即時または継続的なバックグラウンド配信は保証されていません。1.7.19から1.7.22までのリリースでは、コマンドパレットを開いている間だけ動作するデータセット全体の検索も追加され、地図とレイヤーの状態が記憶されるようになりました。これらの変更について、私たちは独自に実機でのテストやセキュリティ監査を行っていません。

### Emanator {#emanator}

マルチアカウント対応のNostrクライアントである[Emanator](https://njump.me/nevent1qvzqqqr4dupzpk4kccr9csumnwhmpv83ladqc6p88089cx2e5s2c4448ppgl2pakqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqannu7pfrkl3daywutspdhdfp3ct4wyk0njcs69nlhufh6gm36a724p5x6)は、1.5.0で[NIP-17](/ja/topics/nip-17/)のプライベートな会話を新たに開始できるようになりました。以前のリリースでは、既存のスレッドに返信することしかできませんでした。ユーザーはメッセージ機能が有効な送信アカウントを選び、名前や[NIP-05](/ja/topics/nip-05/)で連絡先を検索するか、npubまたはnprofileを貼り付けます。既存の会話は再利用されます。受信者がDMの受信箱を公開していない場合、アプリはベストエフォートでの配信に加えてレガシーなオプションを提示します。[1.4.1](https://njump.me/nevent1qvzqqqr4dupzpk4kccr9csumnwhmpv83ladqc6p88089cx2e5s2c4448ppgl2pakqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpx8h9aamsmuvu7fzkhc9n8v37m9rcnyhrc60sjuwrgftk8hhns02ahkkqn)のもとで。再試行では、すでに受理された署名済みのeventが保持されます。再署名して日付を更新できるのは、どのrelayにも受理されなかった古いeventだけです。

### Feather {#feather}

Androidで動くNostrクライアントのFeatherは、0.9系の時期に第45号で最後に取り上げましたが、その後[1.8.4](https://njump.me/nevent1qvzqqqr4dupzqmjxss3dld622uu8q25gywum9qtg4w4cv4064jmg20xsac2aam5nqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqqguewyhvswx5qkcn29ckc7mjsendh0wtc2u6n6l8wzvnvup0wt8y6q9ww)に到達しました。1.xのリリースノートでは、リポジトリが告知しているrelayを介した、ネイティブなNIP-34のissue閲覧と報告が追加されています。署名済みのアクションは端末上のアウトボックスで待機するようになり、WorkManagerがそれをバックグラウンドで配信します。その際、返信より先に親が送信されます。[1.8.0](https://njump.me/nevent1qvzqqqr4dupzqmjxss3dld622uu8q25gywum9qtg4w4cv4064jmg20xsac2aam5nqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqny0jdx2y7gaxdwcmexndm6rk2qgtkxz3zq3cucdlxvdyl92sp532mdl79)では、下書きの保存とオフライン配信に対応したkind 20の画像投稿が追加されました。1.8.4では、報告が成功した後に任意でミュートできるようになっています。[1.7.0](https://njump.me/nevent1qvzqqqr4dupzqmjxss3dld622uu8q25gywum9qtg4w4cv4064jmg20xsac2aam5nqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzp2qa3hycyvc8g7c7wt3a2zl06uneuu5xt8w38q87xqd4pq9uq89udwewmd)以降、翻訳は別アプリのOffline Translatorとその言語パックを通じて行われ、クラウドへのフォールバックはありません。

### OUTKAST {#outkast}

AndroidのNostrクライアントである[OUTKAST](https://njump.me/nevent1qvzqqqr4dupzqeyvpafs936l8quz5nfvskjg9wf8e3sm9q52q72wxmrvc7tdap4xqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzqg4n7egyu8slmmx6gtmus5stgf6fdsxr43rp9fz57ftv4ru5ettxrc4nc3)は、2.2.1で端末上で動作するNetwork discoveryを追加しました。フォローしている人が過去48時間にいいねまたはリポストした、未フォローのアカウントのノートを表示する機能です。リリースノートによると、ランキングではリアクション、返信、zapを(satの額ではなく)件数で数え、そのうえで友人の数と新しさを加味しており、ランキングサーバーは使いません。40以上のアカウントをフォローしている場合、ノートには少なくとも2人の友人の後押しが必要になります。結果は100件のノートで打ち切られ、それより古いページはありません。リリースノートではさらに、選んだ人やリストからのカスタムフィードと、写真エディターについても説明されています。このエディターは編集結果をメタデータのないJPEGとして保存し、変更していないオリジナルはそのままアップロードします。

### CustID {#custid}

Nostrの署名アプリである[CustID](https://njump.me/nevent1qvzqqqr4dupzpw5cfkeqauh4qfmq3grjpaqd8l3n97mpcs94a4s0x946ypqgzv0fqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzp6736dd3jl2ucdqs85ycw8yj9veluh4ug8jqwu3y0wfr06up4s7y8cfupa)は、0.2.2-betaで、生体認証で保護されたアイデンティティに対するNIP-46のASKリクエストに生体認証による承認を必須としました。ただし、直近に認証していれば、それでこのプロンプトを満たせる場合があります。記憶された承認ルールと拒否ルールは、以前の承認も含め、NIP-46とNIP-55の両方で表示なしに適用されるようになりました。自動承認を有効にしようとすると、まず確認の警告が表示され、キャンセルすれば何も変わりません。このベータ版では、公開するeventに[NIP-89](/ja/topics/nip-89/)のclient tagも付与されます。これはデフォルトで有効で、どのアプリがeventを公開したかを読み手に示します。Privacy設定でオフにすることもできます。

### Nostr Vault {#nostr-vault}

Nostrクライアントの[Nostr Vault](https://njump.me/nevent1qvzqqqr4dupzqcdl0y9jp990kq6ftj0px6k0v9d7plxv9ju4kkk0khmvemlp3vrzqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpdeavwf9zysh2zcmlx7hevu7h3nk6nvtzlk05zsajkvewvt84z3zj929ve)は、3.0.0でオプトインのFIPSデバイス接続を追加しました。アドレスまたはQRコードでペアリングすることで、自宅のMacや予備のスマートフォンをvaultとして機能させられます。vaultはノートと履歴を同期し、既存の写真をメッシュ経由で取得します。メッシュを有効にしていれば、再起動後にrelayとともに起動します。公開のメディア投稿には、引き続き公開メディアサーバーが必要です。このリリースではほかにも、フォローやサインアップに関わるアカウント間の競合状態が修正されました。投稿の成功を報告する前に、ユーザー自身の書き込みrelayからの確認応答を待つようになり、見知らぬ相手からのDMはRequestsに留め置かれます。

### Holoboard {#holoboard}

[Holoboard](https://njump.me/nevent1qvzqqqr4dupzpu0ekzvk6nl3ha6708jvepthez0tvvlxss2u07hhfnch5palsz7cqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzq0j3gw5m0602kdr606fgapm3c5f4sk230ahxxr8ryvdhusrlen4cwsqg0s) は、料金を支払って投稿を掲載するボードで、Android 1.1.0 をリリースした。あわせて、ウェブサイトとバックエンドには、支払いで完了するガイド付きの Add to board フローが加わった。ゲストはテキストやリンク、または既存の Nostr 投稿を送信できる。作成済みのインボイスは同じデバイスの同じブラウザプロファイルで再開でき、インボイスの QR はアカウントや接続済みウォレットがなくても引き続き表示される。APK 単体ではランチャーアイコンとスプラッシュ画面が更新されるだけなので、ボードの変更は対応するウェブサイトとバックエンドに依存する。メールアドレスやパスワードによるサインインはない。

### Hopp {#hopp}

[Hopp](https://njump.me/nevent1qvzqqqr4dupzpx7mjedrw4lzxd5ekk4tmr79t0qvrayw88zdtt9vd5mm9ay0y9s7qyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpk7ks3v4gvr2ffqsedrlgm44xy9dlcq3clvptw4rwglrm9dm8stu2jp6t6) は value-for-value の boost に対応したポッドキャストアプリで、第45号で取り上げた 0.2.x のアイデンティティと支払いに関する作業から先へ進んだ。バージョン 0.3.0 では、Hopp サーバーを介さずに Nostr 上で行う暗号化されたデバイス間の同期と復元が追加され、購読、再生位置、お気に入り、Up Next、聴取傾向、ダウンロード設定が対象となる。復元しても既存のライブラリは保持され、ステータス画面では relay と保留中の状態を確認できる。リリースノートによると、結果が不明な boost の分配分は重複した再試行から保護されており、予算は Release Boosting と Boost2Unlock も考慮するようになった。

### Nostrautica {#nostrautica}

[Nostrautica](https://njump.me/nevent1qvzqqqr4dupzpk4kccr9csumnwhmpv83ladqc6p88089cx2e5s2c4448ppgl2pakqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzp23s4qefknu9dzeefgkxuegzd0dsml4zs2gj0sppmqvcmeh7mp5q279sgs) はイベント向けのコンパニオンアプリで、[0.15.1](https://njump.me/nevent1qvzqqqr4dupzpk4kccr9csumnwhmpv83ladqc6p88089cx2e5s2c4448ppgl2pakqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpgrrf3n4vaeafhqhl7msnkvvscw6np9cup4e6pgm3f4x3yrz9mkxd24hwd) でオフラインのイベントパックを追加した。電波の弱い会場に備えて、人物、参加者同士のマッチング、講演、イベントページ、投稿、プロフィール画像を保存する。チャットにはメンション名の表示と、削除を含む編集機能が加わり、送信待ちのメッセージは再試行または破棄できる。バージョン 0.16.0 では、Marmot のグループメッセージングライブラリである MarmotKit 0.14 に移行し、より少ないグループ relay 接続でオフライン中の未取得分に追いつけるようにしたほか、保持期間に基づくクリーンアップの際にも未読メッセージを残す。ストレージの移行は一方向のため、移行後は古いバージョンのアプリはサポートされない。リリースノートでは、White Noise メッセンジャーやウェブとの相互運用性に変更はないとしている。

### Staircase {#staircase}

[Staircase](https://njump.me/nevent1qvzqqqr4dupzqlxr9zsgmke2lhuln0nhhml5eq6gnluhjuscyltz3f2z7v4zglqwqyv8wumn8ghj7un9d3shjtn6v9c8xar0wfjjuer9wcqzpw255ly0xpmr7vqxvn3t45z0clzu2nljrgjcrml9jpquvvyzd44ux0dqpc) は relay.tools による Nostr グループチャットアプリで、0.1.25 で Frequent 通知モードを追加した。このモードはおよそ5分または10分ごとに確認を行い、その後接続を切る。ディープスリープ中はタイミングを Android のスケジューリングが決めるため、バックグラウンドでの配信は即時でもなければ保証されたものでもない。Periodic モードと Frequent モードは、ネットワークが復帰した際に上限付きの確認を1回実行し、その頻度は最大で2分に1回である。Instant モードに変更はない。グループ参加のステータスは、リクエストが処理されたか期限切れになった時点で待機をやめるが、そのどちらなのかは示さない。カスタムのコーディネーター relay はユーザーの管理下にとどまり、公開されたリストで上書きされることはない。

## 開発中 {#in-development}

### Coracle {#coracle}

[Coracle](https://github.com/coracle-social/coracle) は Nostr のウェブクライアントで、master に[ルーティングの修正](https://github.com/coracle-social/coracle/pull/685)をマージした。Lists や Groups などのメニュー項目をクリックしても、同じモーダルがすでに最前面にある場合は何も起きなくなった。以前はクリックするたびに同一のパネルが積み重なっていた。Escape キーでは、それらを1枚ずつ閉じることになっていた。異なるモーダルや通常のページ遷移は従来どおり動作する。これはマージ済みのソースであり、特定のリリースとは結びついていない。

### nostter {#nostter}

[nostter](https://github.com/SnowCait/nostter) は Nostr のウェブクライアントで、zap フローに対する5件の修正をマージした。[Nostr Wallet Connect の pay_invoice 応答](https://github.com/SnowCait/nostter/pull/2746)は、正しい result type と有効な preimage があり、かつ error フィールドが null または省略されている場合にのみ、成功とみなされるようになった。不正な形式の応答は拒否される。[専用の rx-nostr クライアント](https://github.com/SnowCait/nostter/pull/2747)は、セットアップに失敗した場合でも必ず破棄される。ウォレットから10秒間応答がない場合は、失敗ではなく結果不明として扱われる。[インボイスと署名のエラー](https://github.com/SnowCait/nostter/pull/2748)はインラインで表示され、再試行に備えて金額とコメントが保持される。また、インボイスの失敗は NWC の失敗とは区別して報告される。繰り返し zap できるよう、[zap ボタンは有効なまま](https://github.com/SnowCait/nostter/pull/2750)になる。そのオレンジ色の表示は QR のインボイスが表示されたときにも現れるが、これは手動での支払いが完了したことを確認するものではない。[ダイアログを開き直した](https://github.com/SnowCait/nostter/pull/2752)ときにリセットされるのは、アイドル状態の場合だけである。インボイスや署名が届いた後にダイアログを閉じると新たな NWC 支払いは止まるが、すでに送信済みの支払いは続行される。

[オープンなプルリクエスト](https://github.com/SnowCait/nostter/pull/2753)では、結果不明となった後に QR のフォールバックで支払う前に、ウォレットの履歴を確認するよう促す警告を表示し、ウォレットの自動起動を抑制することが提案されている。タイムアウトは、ウォレットが課金しなかったことを意味するわけではない。

### Pollerama {#pollerama}

[Pollerama](https://github.com/formstr-hq/nostr-polls) は投票とフィードのクライアントで、[relay ごとのリクエストキュー](https://github.com/formstr-hq/nostr-polls/pull/258)をマージした。このキューは同時に実行するリクエスト数を調整し、relay がレート制限をかけた際にはバックオフし、大きすぎるフィルタを分割し、relay の URL を正規化する。Mine パックのビューは常設のサブスクリプションを維持するようになったため、relay の応答が遅くても結果が表示される。アプリ内の既知の再リクエストの問題は未解決のままで、ダイレクトメッセージはこの変更に合わせたテストが行われていない。

### Grimoire {#grimoire}

[Grimoire](https://github.com/purrgrammer/grimoire) は Nostr のソーシャルクライアントで、[ダイレクトメッセージ同期の修正](https://github.com/purrgrammer/grimoire/pull/352)をマージした。途中までしか遡れていないマージ済みの relay ページによって履歴カーソルが進むことはなくなった。また、ログアウトでメッセージと既読マーカーが消去された後に、復号処理がそれらを再び埋め戻すことを中断ガードが防ぐ。中断されたバックフィルは、カーソルを動かしたり履歴を取得し尽くしたとマークしたりする前に停止する。課題は残っている。応答した relay が1つだけでも、他の relay に欠落がある状態で履歴を取得し尽くしたとマークされることがあり、署名者が恒久的に拒否した場合にもカーソルは依然として進んでしまう。

### nostr-vpn {#nostr-vpn}

[nostr-vpn](https://github.com/mmalmi/nostr-vpn) は peer の発見に Nostr の鍵を使う VPN で、[モバイルでの再接続の修正](https://github.com/mmalmi/nostr-vpn/pull/77)をマージした。発見用のプローブを実行する時期がすでに来ている場合、クライアントは既知の peer への使い果たされた経路を再び有効にするようになった。これが行われるのは、最近何も受信しておらず、接続済みまたは保留中の経路が存在しない場合に限られ、頻度は最大で300秒に1回である。正常な経路や保留中の経路には手を加えず、ワイヤーフォーマットにも変更はない。作者は分離されたネイティブのフィクスチャに対してこの修正をテストしたが、セルラーネットワーク上ではテストしていない。マージされたもう1つの変更は、登録用の join secret と生のデーモン状態を診断出力から除外することで、[doctor バンドルからネットワークの join secret を取り除く](https://github.com/mmalmi/nostr-vpn/pull/97)ものだ。Nostr の秘密鍵は、すでにそこで伏せられていた。この変更以前に共有されたバンドルは露出したままなので、共有したことがある人は影響を受ける join secret をローテーションすべきである。

いくつかの関連する変更はまだオープンな提案で、マージもリリースもされていない。保存された秘密情報については、既存の移行パスを通じて[ネットワークの join secret をプラットフォームのシークレットストレージに保管する](https://github.com/mmalmi/nostr-vpn/pull/120)提案がある。別の提案は、Nostr ノードの鍵を保持する DPAPI ファイルを対象に、[Windows マシンのサイドカーの秘密情報へのアクセスを SYSTEM と Administrators に限定する](https://github.com/mmalmi/nostr-vpn/pull/101)ものだ。この制限が適用されるのは次にファイルが書き込まれたときだけで、ファイルの作成から ACL の適用までにはわずかな隙間がある。カスタムの設定パスは対象外であり、作者はマルチユーザーの Windows マシンではテストしていない。署名付きメンバーシップについては、[ロスターのスナップショットがディスク上の内容と一致しなくなった参加承認を拒否する](https://github.com/mmalmi/nostr-vpn/pull/117)提案があり、これにより管理者は再読み込みして再試行することになり、同時に承認されたデバイスは保持される。別の提案は、[管理者の時計のずれを5分まで許容し、設定済みの join 署名者を常に必須とする](https://github.com/mmalmi/nostr-vpn/pull/111)もので、ローカルの管理者リストが空の場合でも必須としつつ、リクエストの secret への紐付けは維持する。3つ目は、[タイムスタンプが同じロスター同士の優先順位をアーティファクトのハッシュで決める](https://github.com/mmalmi/nostr-vpn/pull/109)ものだ。両方のロスターを目にした peer は同じ1つのロスターを選ぶことになるが、各ロスターはそれぞれのメンバーシップ内容を保ったままとなる。最後の提案は、[ディープリンクによる参加リクエストと有料の出口プロバイダーに確認を必須とする](https://github.com/mmalmi/nostr-vpn/pull/110)ものだ。macOS と Linux では、参加リンクは明示的な Add-device ステップを待つことになる。macOS ではさらに、有料プロバイダーのリンクも確認のために保留される。いずれのプラットフォームでも、ネイティブ環境での動作は実証されていない。テスト結果はすべて作者による報告である。

### Buzz {#buzz}

[Buzz](https://github.com/block/buzz) はデスクトップとモバイルのクライアントを備えたコミュニティ relay で、グループとエージェントに関する作業をマージした。エージェントは、プロジェクト独自の [NIP-FI](/ja/topics/nip-fi/) [JWT 仕様](https://github.com/block/buzz/pull/8401)に基づいて認証できる。この仕様は発行者が主張する人間のオーナーを検証するもので、そのオーナーを拒否または切断すると、そのオーナーのエージェントのセッションは終了する。また、オーナーのコミュニティメンバーシップによってエージェントを参加させることもできる。Huddle も[検証済みの管理エージェントレコードを受け入れる](https://github.com/block/buzz/pull/8544)ようになった。対象は現在のユーザーまたは Huddle オーナーからのレコードで、[NIP-OA](/ja/topics/nip-oa/) のオーナー証明ボットロールに加えて受け入れられる。このフォールバックは互換性のためのポリシーであり、未知のサードパーティのレコードを信頼するものではない。身元の証明にもならない。いずれの仕様も承認済みの NIP ではない。

[オープンなアナウンスチャンネル](https://github.com/block/buzz/pull/8143)は `join_role=guest` を通じて読み取り専用のゲストを受け入れることができ、[一覧に載らないオープンチャンネル](https://github.com/block/buzz/pull/8579)はメンバー以外による発見からは隠されるが、チャンネル ID を知っていれば誰でも読める。受け入れ用の event では[最大100人のメンバーを追加でき](https://github.com/block/buzz/pull/8575)、一部のみ成功する場合もある。先週オープンな提案として報じた[チャンネル設定の修正](https://github.com/block/buzz/pull/8516)がマージされた。変更は、関連するリクエストや通知とともに1つのトランザクションでコミットされる。公開から非公開への切り替えに失敗した場合は完全にロールバックされ、そのロールバックによって削除済みのメンバーが再び現れることを防ぐ。モバイルでは、[プッシュ設定の失敗](https://github.com/block/buzz/pull/8610)によってアプリが壊れることはなくなった。アプリは限られた回数だけ再試行し、手動での復旧手段を提示する。ただし、テストはモックしたチャンネルによるもので、APNs でのデバイスの挙動は検証されていない。[同期されたミュートが原因で起動時に空白画面になることはなくなり](https://github.com/block/buzz/pull/8608)、実際の DM プッシュ購読と照合するようになった。この修正の根拠は iPhone のログ1件だけである。relay メッシュでは、ハートビートが5分間ないと[応答しなくなった peer のレコードが期限切れになる](https://github.com/block/buzz/pull/8503)一方、稼働中の接続は対象外となる。

より新しいマージについては、リリースに含まれているかどうか確認されていない。[kind 9000 のメンバー追加](https://github.com/block/buzz/pull/8606)は、ロスターへの書き込みと一緒にコミットされるようになった。変更が失敗した場合はどちらも保存されず、同じ署名済み event を再試行できる。kind 9001、9021、9022 には従来の隙間が残っている。[NIP-FI のシャドウモード診断](https://github.com/block/buzz/pull/8634)は、拒否されるはずだったケースについて、検証済みの Nostr 鍵と固定の非公開の理由をログに記録するようになった。トークンやクレームはログに記録しない。これによって受け入れや強制の挙動が変わることはない。Buzz 独自の [NIP-AP](/ja/topics/nip-ap/) [エージェント仕様](https://github.com/block/buzz/pull/8631)は承認済み NIP の枠外にあるプロジェクト文書で、設定内にクライアント定義の `agentType` を必須とするようになった。別のタイプの設定での起動は拒否される。フィールドがない場合は従来の意味が維持され、タイプを変更すると以前のタイプのネストされた設定が破棄されることがある。[単独エージェントの選択](https://github.com/block/buzz/pull/8616)は、最新の kind 30177 管理エージェントポリシーが不正な形式の場合、フェイルクローズする。古いデータは引き続き除外される。エージェントにはオーナーが管理する名前でラベルを付けるが、アートワークやメッセージの作成者には引き続きプロフィールが使われる。

モバイルでは、[ホスト型エージェントの作成、一覧表示、削除](https://github.com/block/buzz/pull/8626)に NIP-OA のオーナー証明と kind 30177 の登録を使い、同一アイデンティティでの永続的な再試行に対応するほか、非公開の指示はセキュアストレージに保管する。ビルド時のホスト型ゲートは App Store 版と社内ビルドでオフになっているため、一般公開されたことを意味するものではない。[ホスト型 iOS の招待からのコールドスタート](https://github.com/block/buzz/pull/8617)では、招待の intent を保持し、一致する鍵をインポートし、バックアップから復旧する。メインのパスをテストしたのは作者だけで、メンバーシップのフォールバック用エンドポイントと新規サインアップは未解決のままである。[プッシュ登録の復旧](https://github.com/block/buzz/pull/8629)では、指数バックオフで待機した後、401 で拒否された保存済みのリクエストを、回数に上限のある新しいチャレンジと App Attest 鍵で置き換える。400 や一時的なエラーの後も intent は保持され、通常の 404 は通常どおり扱われる。この復旧処理は実機では確認されていない。[メッセージリンク](https://github.com/block/buzz/pull/8518)がユーザーの参加していない公開チャンネルを指す場合は、kind 39000 のメタデータを取得して読み取り専用で開き、非公開チャンネルと DM の制限は変わらない。再接続中のリンクはキューに入り、1件の検索が遅いと後続のリンクが最大8秒遅れることがある。

本号のソース締め切り時点で、いくつかのオープンなプルリクエストが未マージのままでした。デフォルトで無効の `buzz_v1` ケイパビリティは、クライアント側の既読状態を[呼び出し元専用の NIP-98 サイドバー、既読状態、カバレッジ API](https://github.com/block/buzz/pull/8639)に置き換えます。さらに、人ごとのリビジョンと relay 限定の kind 24300 無効化 ping も加わります。このケイパビリティを持たない relay は引き続き[NIP-RS](/ja/topics/nip-rs/)を使います。大規模なデータベースでは、先にインデックスを並行構築しておく必要があります。[スレッド要約](https://github.com/block/buzz/pull/8635)は最新 1,000 件の返信のみを走査し、最新の 10 人の作成者を返します。ライブ更新の送信は pod ごとに最大で毎秒 1 回です。そのため、過去の参加者全員を列挙するわけではありません。リアクションに対するエージェントの応答は、最後の有効な [NIP-25](/ja/topics/nip-25/) の `e` tag を使って[リアクション対象のメッセージの下にスレッド化され](https://github.com/block/buzz/pull/8642)、それが使えない場合は従来のアンカーにフォールバックします。Hermes ベースのエージェントには、[チャンネルや DM に投稿するための、エージェント単位にスコープされた MCP シェル](https://github.com/block/buzz/pull/8643)が提供されます。このシェルはブリッジなしでは実行を拒否し、認証情報をマスクします。ただし、インストール、再起動、実際の投稿は検証されていません。[ACP アダプターの修正](https://github.com/block/buzz/pull/8625)は、v1 と v2 の両方の初期化名を送信し、安定版の v1 にフォールバックし、検証済みのメジャーバージョンを固定します。これはエージェントのトランスポートの修復であり、Nostr プロトコルの変更ではありません。モバイルの[読み上げ](https://github.com/block/buzz/pull/8637)機能は端末の音声合成エンジンを使い、コード、リンク、添付ファイルは読み飛ばします。音声がどこで処理されるかは、ユーザーが選んだエンジンによって決まります。単体の[relay 負荷生成ツール](https://github.com/block/buzz/pull/8636)は人間と NIP-OA エージェントをシミュレートし、設定されたエラーやレイテンシの上限を超えた実行を失敗扱いにします。relay のコードは一切変更せず、本番規模での動作を証明するものでもありません。

### Mosaico {#mosaico}

[Mosaico](https://github.com/pablof7z/mosaico)は、[relay ベースのグループ（NIP-29）](/ja/topics/nip-29/)内でエージェントを調整するデーモンです。今回、[ハートビートベースのプレゼンス](https://github.com/pablof7z/mosaico/pull/847)がマージされました。エージェントがチャンネルに在席しているとみなされるのは、ステータス event を公開している間だけになりました。この event には、90 秒先に設定され 30 秒ごとに更新される[有効期限タイムスタンプ（NIP-40）](/ja/topics/nip-40/)が付きます。ローカルでプロセスが動いているだけでは、もはやプレゼンスとはみなされません。エージェントがオフラインの間もメンバーシップは維持されるため、後で再開できます。[再構築されたグループ読み取りモデル](https://github.com/pablof7z/mosaico/pull/845)は、relay の変更ごとに 1 回、正規の到着カーソルとともに構築されます。これにより、広範なグループ購読が置き換えられてもチャットが失われることはなくなりました。

その後の 3 件のマージは、リリースに含まれたことが確認されていません。[置き換え用の購読](https://github.com/pablof7z/mosaico/pull/854)は新しい REQ ID を使い、古い購読が閉じられる前に開かれるようになりました。退役したプロファイルはレイテンシが重要な経路の外で公開されます。チャンネルを離れるエージェントは、NIP-29 のメンバーのままプレゼンスを取り下げます。裏付けとなるプローブは作成者によるもので、私たちの測定ではありません。[クレーム優先のリトライ管理](https://github.com/pablof7z/mosaico/pull/851)はスキーマ 27 に永続的に保存され、relay のリプレイ後も失われません。リトライは単一の直列タイマー上で 30 秒から 1 時間まで指数関数的にバックオフし、10 回失敗すると打ち切られます。欠落した event は削除として扱われません。また、保持ウィンドウに入るのは 4,096 件のエントリまでなので、すべての event の配信は保証されません。[グループ限定のスナップショット](https://github.com/pablof7z/mosaico/pull/852)がグループのコンシューマーを起動するようになりました。タイムスタンプが同じ置き換えでは、[NIP-01](/ja/topics/nip-01/) の規定どおり最小の event ID が残ります。コンテンツのみの変更では、引き続き汎用コンシューマーが起動されます。親が欠落している場合のスコープ付きフォールバックは、次のグループ変更か 15 秒のタイムアウトまで待つことがあります。

### Sonar {#sonar}

Nostr、MLS 暗号化、Bluetooth Low Energy メッシュを組み合わせたメッセンジャーである[Sonar](https://github.com/hedwig-corp/bitchat-to-sonar)は、[モバイルデータ通信接続時の起動に関する修正](https://github.com/hedwig-corp/bitchat-to-sonar/pull/665)をマージしました。この PR によれば、初回描画が遅い原因は、プッシュ relay へのアタッチがストアのロックを保持していることにあります。Android では、ローカルノードがすでに開いていれば、起動処理はそのロックをスキップします。たとえば、プッシュ登録がコールドスタート前にローカルノードを開いていた場合です。iOS では、アプリが描画できるよう、通知サービス拡張に接続とドレイン処理の停止を指示します。

### Shopstr {#shopstr}

Nostr マーケットプレイスの[Shopstr](https://github.com/shopstr-eng/shopstr)は、[先週提案された](/en/newsletters/2026-10-21-newsletter/#shopstr)[出品削除のサポート](https://github.com/shopstr-eng/shopstr/commit/2e11d0b6d7b8d5d3007c5393882a77dc2f0721e2)をマージしました。販売者が署名した[event 削除リクエスト（NIP-09）](/ja/topics/nip-09/)により、出品はキャッシュから削除されてトゥームストーン化されるようになりました。そのため、削除された商品がキャッシュから再表示されたり購入されたりすることはありません。一方、より新しい再出品は引き続き表示されます。それでも一部の削除は取りこぼされます。出品より先に届いた削除は無視されます。`k` tag のない古いリクエストは relay クエリに一致しません。過去の削除も遡って反映されません。relay が削除された event を保持し続ける可能性もあります。これとは別に、[不正な形式の gift wrap メッセージ](https://github.com/shopstr-eng/shopstr/pull/614)が原因で「注文」と「マイ出品」の画面が停止することはなくなりました。また、[販売者が自分の注文を閲覧できるようになりました](https://github.com/shopstr-eng/shopstr/pull/652)。他のユーザーには引き続き 403 が返されます。

ソース締め切り時点で未マージの 3 件のオープンなプルリクエストは、注文の整合性を対象としています。[#665](https://github.com/shopstr-eng/shopstr/pull/665)は、NIP-98 による登録を通じて各注文の参加者を一度だけ記録します。購入者は認証から、販売者は署名済みの出品から取得されます。一度記録された参加者は、その後の書き込みでは変更できません。登録に失敗してもチェックアウトは止まりません。新たな未解決の注文が tag から推測されることもありません。旧来の注文は限られた期限までしかカバーされず、注文 ID ごとのステータス保存方法にある欠陥も未修正のままです。#665 に依存する[#666](https://github.com/shopstr-eng/shopstr/pull/666)は、gift wrap（[NIP-59](/ja/topics/nip-59/)）された注文ステータスメッセージを、その注文に記録された購入者または販売者から届いた場合にのみ適用します。認証済みでも、それ以外の送信者からのメッセージは適用されません。未解決の注文は保留のままです。購入者による支払い後の確認は、販売者の確認とはみなされません。偽造されたメッセージは注文の状態を変えず、チャットとして残ります。[#664](https://github.com/shopstr-eng/shopstr/pull/664)は、エスクローの登録と裁定のために、ネットワーク経由で keyset を参照せずに Cashu v2 keyset トークンのメタデータを読み取り、proof の合計を修正します。注文作成時のトークンのデコードについては、引き続き別途修正が必要です。

### Conduit {#conduit}

[Conduit](https://github.com/Conduit-BTC/conduit-mono)は、購入者向けと販売者向けの対になったアプリを備える Nostr マーケットプレイスです。今回、[単一の暗号化アカウントレコード](https://github.com/Conduit-BTC/conduit-mono/pull/711)がマージされました。ウォレットのメタデータ、シード、ネイティブ ID、アドレス、設定、セットアップの進捗は、1 つの[任意のカスタムアプリデータ（NIP-78）](/ja/topics/nip-78/)レコードに格納されるようになりました。このレコードは[バージョン付き暗号化ペイロード（NIP-44）](/ja/topics/nip-44/)で暗号化され、署名、所有者、導出された ID が検証されます。署名者が承認すると、両方のアプリがこのレコードを見つけられます。この切り替えには後方互換性がありません。古いバックアップおよび復元経路は無視されます。旧来のバックアップは自動移行されず、そのまま残ります。その他のマージで、ブラウザのローカルストレージに保持される[既存の nsec でのサインイン](https://github.com/Conduit-BTC/conduit-mono/pull/646)が追加されました。商品ファミリーの編集時には[署名済みの正確な配送条件](https://github.com/Conduit-BTC/conduit-mono/pull/647)が必須となりました。さらに、[チェックアウトの復元データは IndexedDB に移され](https://github.com/Conduit-BTC/conduit-mono/pull/708)、保存済みとマークする前に読み戻しが行われます。

Conduit は[NWC SDK 8.1.1 にも移行し](https://github.com/Conduit-BTC/conduit-mono/pull/740)、同 SDK の金額検証、接続試行回数の制限、クローズ済みプールの処理、処理中レスポンスに関する修正を取り込みました。Conduit のウォレットの選択、暗号化、支払いポリシーは変わっていません。アプリのデプロイは未確認のままです。ソース締め切り時点で、2 件のドラフトのプルリクエストが未マージのままでした。[支払いの有効化](https://github.com/Conduit-BTC/conduit-mono/pull/743)は、固定の 2 分間の実行ウィンドウ内で支払い状態を永続化し、読み戻し、配信します。この実行ウィンドウはリトライでリセットされません。Nostr のレシート、非公開のアカウント復元、在庫やフルフィルメントの変更には、それぞれ個別の署名済みの証拠が必要になります。レシートはその後 24 時間保持されますが、それによって支払い権限が復活することはありません。資金を入れた状態での確認、実機での確認、メンテナーによる確認はまだ完了していません。[イベント専用商品](https://github.com/Conduit-BTC/conduit-mono/pull/741)は、[NIP-99](/ja/topics/nip-99/) の kind 30402 の出品を `conduit_event_only` 拡張で非表示としてマークします。これらの商品は通常のカタログやチェックアウトには現れず、承認済みの正確なイベント開催回への割り当てが必要になります。非表示にされた署名済みデータは公開されたままです。他のクライアントがサポートするのは標準の hidden フラグのみです。

### LNbits {#lnbits}

Lightning のウォレットおよびアカウントサーバーである[LNbits](https://github.com/lnbits/lnbits)は、[Nostr 通知を NIP-17 のプライベートメッセージとして送信するオプション](https://github.com/lnbits/lnbits/pull/4260)をマージしました。管理者は、旧来の [NIP-04](/ja/topics/nip-04/) 暗号化メッセージと [NIP-17](/ja/topics/nip-17/) プライベートダイレクトメッセージのどちらかを選べます。新規設定のデフォルトは NIP-17 です。NIP-17 の場合、サーバーは受信者の DM 受信箱 relay リストを検索します。NIP-05 の relay は、探索のヒントとして、またリストが存在しない場合の送信先として使われます。空のリストが公開されていると、送信は失敗します。各送信には 30 秒の制限があり、少なくとも 1 つの受信箱 relay に受け入れられる必要があります。NIP-04 へのフォールバックは一切行われません。

### Zeus {#zeus}

モバイル向けの Bitcoin および Lightning ウォレットである[Zeus](https://github.com/ZeusLN/zeus)は、プレリリース版[v13.2.4-rc1](https://github.com/ZeusLN/zeus/releases/tag/v13.2.4-rc1)に[支払い後の更新が失敗した際の Nostr Wallet Connect の予算計上に関する修正](https://github.com/ZeusLN/zeus/pull/5389)を含めました。同じリリースには、[Nostr Wallet Connect の make_invoice が自身の作成した invoice を返すようにする](https://github.com/ZeusLN/zeus/pull/5316)以前の修正も入っています。修正前は、[NIP-47](/ja/topics/nip-47/) による送金後に更新エラーが起きると、予算計上がスキップされていました。その結果、成功していた可能性のある支払いに対してエラーが返されていました。現在は、preimage が返されれば既存のフォールバックを通じて予算から差し引かれます。タイムアウトした場合は、支払いが一覧に見当たらなくても、その金額が保留中の支出として確保されます。処理中の LND 支払いを含め、その他の欠落は残っている可能性があります。続く[v13.2.4-rc2](https://github.com/ZeusLN/zeus/releases/tag/v13.2.4-rc2)は依存関係の更新のみでした。

その後、さらに新しい 2 件の修正がソースにマージされましたが、いずれのリリース候補にも含まれていることは確認されていません。[デフォルト有効期限の修正](https://github.com/ZeusLN/zeus/pull/5394)により、invoice に有効期限フィールドがない場合、ローカルの BOLT11 デコーダーは仕様のデフォルト有効期限である 3600 秒を適用するようになりました。こうした invoice はこれまで期限切れにならないものとして扱われていました。そのため、期限切れ invoice への支払いを阻止するチェックが適用されていませんでした。`NostrConnectUtils` における NWC の invoice 検証にも同じ欠陥がありました。[ウォレット単位のバックアップ修正](https://github.com/ZeusLN/zeus/pull/5191)は、ecash ウォレットごとに Nostr のミントバックアップのタイムスタンプをリセットします。この修正以前は、別の ecash ウォレットと同じセッション内でシードから復元されたウォレットが、そのウォレットのタイムスタンプを引き継ぐことがありました。すると、自身のより古い relay 上のバックアップを古いものとして破棄し、空のミントリストを保存してしまうことがありました。これにより自動復元が無効になっていました。ウォレットの切り替え後に完了したバックアップは、依然として誤ったウォレットにタイムスタンプを書き込む可能性があります。すでに影響を受けたウォレットには、保存された空のリストが残ったままです。Mint sync で手動復元を行うか、ミント URL を再追加する必要があります。それらのウォレットの ecash はミントに残っています。どちらのプルリクエストも、実機でのテストは行われていないと報告しています。

### npub.cash {#npubcash}

[npub.cash](https://github.com/cashubtc/npubcash-server)は、Nostr アイデンティティ宛ての Lightning 支払いを受け取り、Cashu ecash に変換します。今回、[支払者が要求した relay に zap レシートを公開するサーバー側の変更](https://github.com/cashubtc/npubcash-server/pull/67)がマージされました。サーバーはこれまでも zap リクエストで指定された relay を解析していました。しかし、支払い済みのレシートを公開する際にはそれらを無視していました。現在は、リクエストで少なくとも 1 つの relay が指定されていれば、レシートはそれらの relay に送られます。relay リストがない、または空のリクエストでは、引き続き設定済みのデフォルト relay が使われます。

### eHagaki {#ehagaki}

埋め込み可能な Web Component としても提供される Nostr Web クライアントの[eHagaki](https://github.com/Lokuyow/ehagaki)は、[1.31.0](https://github.com/Lokuyow/ehagaki/releases/tag/v1.31.0)と[1.31.1](https://github.com/Lokuyow/ehagaki/releases/tag/v1.31.1)をリリースしました。バージョン 1.31.0 では、リポスト（[NIP-18](/ja/topics/nip-18/)）、リアクション（[NIP-25](/ja/topics/nip-25/)）、アップロード済みメディアの管理が追加されました。event が外部署名者に渡される前に outbox ルーティング（NIP-65）が確定されるようにもなりました。さらに、投稿履歴とキャッシュをローカルの Citrine relay に保持できます。このバージョンの IndexedDB 移行では、ローカルに表示される投稿履歴がリセットされます。下書きと保存済みの削除リクエストは保持されます。relay 上にある履歴は再取得できますが、ローカルにしかない投稿はアップグレード前にバックアップまたはエクスポートしておく必要があります。バージョン 1.31.1 は、Blossom の kind 10063 に加えて kind 10096 を通じて [NIP-96](/ja/topics/nip-96/) のアップロードサーバーを同期します。使用可能な部分的 relay 設定も保持されます。アップロードサーバーリストとメディアサーバー同期の修正も含まれています。宣言された読み取り relay を介した[アップロードサーバーリストの取得](https://github.com/Lokuyow/ehagaki/pull/366)では、他の relay がタイムアウトしても、有効な署名を持つ最新のリストが保持されます。リストが 1 つも届かない場合、設定は変更されません。[メディアサーバー同期](https://github.com/Lokuyow/ehagaki/pull/364)は Blossom と [NIP-96](/ja/topics/nip-96/) の設定を別々に扱います。検索に失敗した後に、短縮されたリストを公開することはありません。

マージ済みのその他の信頼性修正も、まだリリースへの収録は確認されていません。401または403が返された後、ユーザーは[メディア画面からyabu.meまたはnostrcheck.meのNIP-96サーバーに登録](https://github.com/Lokuyow/ehagaki/pull/374)できます。NIP-98署名は実際のPOST URLとボディハッシュを対象とし、アカウントや送信先が変わるとリクエストは取り消されます。ガードが二重送信を防ぎ、結果が不明なリクエストは再送されません。eHagakiがパスワードを提供することは一切なく、招待コードや支払いの手順はプロバイダーの公式サイトに引き継がれます。[大量のBlossomファイル一覧](https://github.com/Lokuyow/ehagaki/pull/363)は、上限付きのローカルスナップショットから24件ずつページ送りされます。8 MiBまたは10,000件を超える応答は拒否され、アカウント、セッション、サーバーのいずれかが変わるとスナップショットは破棄されます。末尾に達したというのはスナップショットを使い切ったという意味であり、サーバーにそれ以上ファイルがないという意味ではありません。[NIP-46リモート署名者の復旧](https://github.com/Lokuyow/ehagaki/pull/355)では接続を再構築し、古い保留中のリクエストは30秒後に再送せず明示的に拒否します。[PrimalのBlossomサーバーへのアップロード](https://github.com/Lokuyow/ehagaki/pull/367)では、既存の署名済み認可をパディング付きの標準Base64でエンコードし、他のサーバーでは引き続きBase64URLを使います。

より新しい2件のマージも、リリースへの収録は確認されていません。[公開処理](https://github.com/Lokuyow/ehagaki/pull/393)は、上限付きで検証済みのrelayリクエスト待機を共有するようになり、配信と進捗をセッションに結び付けたまま、複数の個別タイマーを置き換えました。最初の有効なrelay確認応答をもって成功とみなし、残りのrelayへの配信はそのまま続きます。進捗表示がすべてのrelayへの配信を主張することはありません。アカウントを切り替えたりログアウトしたりすると、バックグラウンド配信は停止します。投稿履歴では、要求に応じて3秒の制限内で[関連する返信、リアクション、削除を更新](https://github.com/Lokuyow/ehagaki/pull/391)できます。部分的なタイムアウトが起きても、すでに受信した結果は保持されます。また、届かない削除があっても、削除が存在しない証拠とはみなされません。

### Formstr Drive {#formstr-drive}

NostrとBlossomの上に構築された暗号化ファイル共有アプリであるFormstr Driveは、以前オープンな提案として報じた[DriveKey復旧の作業をマージ](https://github.com/formstr-hq/formstr-drive/commit/e7f8c00583dc746e4a69b9ce4c97f8c3e1af851f)しました。アプリは統合キーリングを書き込む前に到達可能なすべてのrelayを読み取るため、古い鍵は見えるようになるにつれて収束していきます。新しい鍵を作成するのは、4つのアプリrelayのうち2つが何も返さず、履歴もバージョンもない場合に限られます。応答しない書き込みrelayが古い鍵をしばらく隠してしまう可能性は残り、古いビルドは新しいJSON形式を読めません。

プロジェクトはまた、[アカウントごとの復号済みファイル、共有、フォルダー、アウトボックスを分離しました](https://github.com/formstr-hq/formstr-drive/pull/85)。アカウントを切り替えると前のアカウントの保留中の署名とインポートはブロックされますが、ステージング済みのblobが参照されないまま残ることがあります。[新規アカウントではアップロードサーバーを明示的に選ぶ必要があり](https://github.com/formstr-hq/formstr-drive/pull/88)、暗黙のフェイルオーバーは行われません。一方、以前の自動デフォルトは維持されます。サーバーには引き続きpubkey、アップロードのタイミング、暗号化されたバイトが見えます。[重複警告は、同じサーバーとフォルダー上に同一のライブなバイトがある場合にのみ出るようになりました](https://github.com/formstr-hq/formstr-drive/pull/89)。アカウント分離と重複確認のAndroidでの経路は未テストであり、これらがリリースに含まれているかどうかも確認できていません。

### diVine {#divine}

Nostr向けのショート動画クライアントであるdiVineは、メッセージング、アカウント、チャレンジに関する変更をマージしました。初期のベータリリースには汎用的なノートしかないため、これらのいずれも出荷済みビルドに含まれているとは確認されていません。[フィールド単位で暗号化されたアカウントスナップショット](https://github.com/divinevideo/divine-mobile/pull/10413)は、設定、バッジの判断、非表示操作を同期し、保留中の変更をローカルで再試行し、読み取りが不完全な場合は安全でない公開をブロックします。DMの既読マーカーは既存のプロトコルを維持し、通知の既読はサーバーAPIを使います。すべて既読にするには接続が必要です。OSの権限、認証情報、年齢に関する同意は端末内にとどまります。

DMでは、[メッセージが安全にキューに入るとコンポーザーと共有シートが閉じます](https://github.com/divinevideo/divine-mobile/pull/10500)。アプリが終了している間はバックグラウンド配信は動作せず、配信はrelayの確認応答があって初めてカウントされます。[失敗した再試行は、試行回数の上限に一貫して算入されます](https://github.com/divinevideo/divine-mobile/pull/10346)。[形式が不正なレガシーNIP-04メッセージは破棄され、台帳に記録されます](https://github.com/divinevideo/divine-mobile/pull/10522)が、保存済みの空の吹き出しは残り、外部署名者や他の端末との互換性は確認されていません。[信頼済み送信者からの動画DMに対するオプションのぼかしプレビュー](https://github.com/divinevideo/divine-mobile/pull/10437)はデフォルトでオフで、常にぼかされたうえでコンテンツ警告が付きます。動画自体はダウンロードされるため、ぼかしによってネットワーク上のプライバシーが得られるわけではありません。グループでは、[メンバーをブロックしても隠れるのはそのメンバーのメッセージだけ](https://github.com/divinevideo/divine-mobile/pull/10156)で、相手には引き続き自分のメッセージが届くという警告が表示されます。ルームからの退出状態は保存され、維持されます。新しいグループの作成は、デフォルトでオフのフラグの背後にとどまっています。これらの変更は既存のグループに適用され、信頼と安全性のレビューは保留中です。

以前オープンだった2つの機能がマージされました。[受信したDM動画のキャッシュ](https://github.com/divinevideo/divine-mobile/commit/25f9b7b8783ce11d70fc965936d1939b50f5f198)は、復号済みファイルをアカウントごとに最大30日間または300 MBまで保持します。信頼済みチャットやフォロー中のユーザーからの動画を自動読み込みすると、視聴時刻がメディアホストに知られます。見知らぬ相手の動画はタップが必要です。サーバー側でテイクダウンされても、キャッシュ済みのバイトが即座に取り消されることはありません。ただし、それより早く追い出される場合はあります。[ユーザー名の所有者照会](https://github.com/divinevideo/divine-mobile/commit/489231071520bd066636384f4dd2a8e6d88f3f96)は、Divineハンドル検索の最初のページについてネームサーバーのNIP-05ディレクトリを確認し、アクティブな所有者のみを固定表示します。クエリ名はサーバーログに残り、これは一般的なNIP-05検証ではありません。

[人物リストが一般提供へ移行しました](https://github.com/divinevideo/divine-mobile/pull/10415)。これは[発見と管理を統合した作業](https://github.com/divinevideo/divine-mobile/pull/9742)を土台としています。プロフィールのサポートリンクはデフォルトでオンです。エディターはすべてのrelayから厳密な生のkind 0読み取りが揃うのを待ち、非表示のプロバイダーと未保存の編集を保持します。ストアのリリースチャネルでのビルドの昇格とバックエンドの展開はまだ行われていません。[クライアント帰属tagは、再試行やメタデータ編集の際に現在のNIP-89設定に従い](https://github.com/divinevideo/divine-mobile/pull/10387)、署名前に他クライアントのclient tagを取り除きます。一方、署名済みの予約投稿が変わることはありません。デフォルトでオフの[認証付き外部短縮リンク](https://github.com/divinevideo/divine-mobile/pull/10507)は、正確なNIP-98 POSTとボディに2秒以内に署名し、できなければ正規URLにフォールバックします。DMとNostr eventでは常に正規URLが保持されます。ゲートウェイでの作成機能はオフの状態でデプロイ済みで、この先に展開ゲートが控えています。

クリエイターは[明示的なtagによって公開動画の再利用を許可](https://github.com/divinevideo/divine-mobile/pull/10467)できます。この機能はデフォルトでオフで、改変禁止ライセンスの音声を使う場合は公開時にオフに固定されます。あくまでクライアントの慣習であり、DRMではありません。テスト専用のチャレンジ作業は、特別なテストビルドにおける[署名付きプロトコル基盤](https://github.com/divinevideo/divine-mobile/pull/10374)、[ルールと同意のチェックを伴うエントリー署名](https://github.com/divinevideo/divine-mobile/pull/10503)、[アカウントごとの永続ストレージ](https://github.com/divinevideo/divine-mobile/pull/10509)、[ネイティブのレビューおよび取り下げフロー](https://github.com/divinevideo/divine-mobile/pull/10515)を対象としています。relayの確認応答は主催者の承認を意味しません。本番環境での発見機能は無効になっています。バックエンドの提供、実アカウントでの受け入れテスト、クライアント横断のリリース手順はまだ残っています。

より新しいマージも、リリースへの収録は確認されていません。受信者のkind 10050 DMインボックスを読み取れない場合、[NIP-17の保留送信キュー](https://github.com/divinevideo/divine-mobile/pull/10531)は、relayがすでに受理した受信者宛てgift wrapのIDを再利用するようになり、再試行をまたいでそのwrapの同一性を保ちます。再試行でインボックスが見つかれば、クライアントは告知されたrelayに再公開できます。インボックスが見つからなければ、受理済みのコピーで確定し、その保持をrelayに委ねます。メッセージが「失敗」と表示される可能性は依然としてあります。受信者への配信や受信者による既読は証明されておらず、リアクションと削除の再試行はこの変更の対象外です。[公開通知のプリロードとタイムゾーンの更新](https://github.com/divinevideo/divine-mobile/pull/10460)は、上限付きのサムネイルキャッシュと共有のSQLiteインデックスを使い、DMとキャンペーンは除外します。通常のネイティブリリースに加えて連携したサービス側の変更が必要で、バックグラウンド実行は保証されません。動画エディターには[5種類のトランジション](https://github.com/divinevideo/divine-mobile/pull/10543)が加わって合計20種類となり、プレビューとエクスポートでネイティブにレンダリングされます。モーション低減の設定では、意図的にプレビュータイルが制限されます。フラッシュの間隔はディゾルブにフォールバックすることがあります。ネイティブ実装の実地テストは行っていません。

ソースのカットオフ時点で、4件のオープンなプルリクエストが未マージでした。以前のinfo-sticker作業の上に積まれた[ソーシャル動画ステッカー](https://github.com/divinevideo/divine-mobile/pull/10540)は、メンション（`p`）、ハッシュタグ（`t`）、リンク（`r`）のメタデータを持つ、小さくフラットなステッカーtagを書き込むものです。プレーヤーはタップ可能な領域を重ねて表示し、外部リンクを開く前に警告する予定です。他のクライアントでは、そのtagを実装しない限り、動画に焼き込まれたステッカーしか見えません。なお、このtagは承認済みのNIPではありません。[フラグで制限されたConcordチャット](https://github.com/divinevideo/divine-mobile/pull/10536)内のメンションは、認証済みの暗号化メッセージの中に身元情報を保持することになります。アプリ内アラートは、ユーザーが開いたことのあるルームで、フォロー中かつブロックしていない送信者からのものに限られ、上限は50行で既読状態が保存される見込みです。OSのプッシュ通知や公開チャットの展開を引き起こすことはなく、身元の衝突、リプレイ、ブロックのチェックは範囲を限定したテストでしか検証されていません。[NIP-17のrumor tag](https://github.com/divinevideo/divine-mobile/pull/10534)では、リアクションの作成者を実際のkindとともに一度だけ示し、ラップされた削除からは誤解を招く`p` tagを取り除く予定です。gift wrapはもともと正しい受信者宛てになっていたため、これは受信者情報の漏洩を修正するものではありません。すでにキューに入ったrumorは変更されず、他のクライアントでの動作は未テストで、ルームへの振り分けに関するトレードオフも残ります。[次のネイティブビルド](https://github.com/divinevideo/divine-mobile/pull/10532)では既存の短縮リンク共有がデフォルトでオンになり、Web版はオフのままとなる予定です。無効時、サインアウト時、エラー時の経路では完全な正規URLが保持されます。ストアでの配布、サービスの準備状況、端末での確認は証明されていません。

### rust-nostr {#rust-nostr}

RustによるNostrプロトコルライブラリ群であるrust-nostrは、[サブスクリプションの再発行方法に関する破壊的変更](https://github.com/nostrdevkit/nostr/pull/1495)をマージしました。`SubscriptionData`は、各relayの現在のEOSE状態を示すようになりました。再発行時には、切断中であっても、CLOSEと保存済みフィルターのREQを1つのアトミックな手順でキューに入れます。これで保証されるのはキューへの入れ方であり、両方のフレームがrelayに届くことまでは保証されません。通知の欠落から回復する際に、サブスクリプションが黙って失われたり、重複したリクエストが送られたりすることはなくなりました。それでも、前のREQから遅れて届くEOSEメッセージやeventが新しいREQと重なる可能性は残ります。ワイヤー上にはそれらを区別するものが何もないためです。これはマージ済みのソースであり、リリースに含まれているかどうかは確認できていません。

### nostr-sdk-ffi {#nostr-sdk-ffi}

他の言語からrust-nostrのSDKを使えるようにするバインディングであるnostr-sdk-ffiは、[NIP-44 v2の会話鍵への生のアクセス](https://github.com/nostrdevkit/nostr-sdk-ffi/pull/96)をマージしました。これにより、Concordのホストは独自のECDHおよびHKDFコードを同梱する必要がなくなります。既存の導出処理を薄くラップしているだけで、新たな暗号処理は追加していません。作成者はPythonでのビルドと、双方から同じ鍵が得られる往復確認を報告していますが、専用のユニットテストは追加していません。これはマージ済みのソースにすぎません。

### NDK {#ndk}

Dart向けのNostr開発キットであるNDKは、破壊的変更を含むプレリリース[0.11.0-dev.2](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.2)を公開しました。安定版の0.11.0ではなく、JavaScriptのNDKとも無関係です。このリリースでは、[NIP-49](/ja/topics/nip-49/)の[パスワード暗号化されたncryptsec鍵とサンプルUI](https://github.com/relaystr/ndk/pull/896)が追加されました。ノートによれば、復号時にはlogNに上限を設け、未知のセキュリティバイトを拒否し、導出したバッファをゼロ化します。これらの主張はノートとマージ済みソースに基づくもので、独立した監査やテストベクターの実行は確認していません。[リクエストは、接続または送信の失敗内容を伴うnotSentという結果を報告するようになりました](https://github.com/relaystr/ndk/pull/911)。到達不能なrelayへのリクエストは、応答できるrelayやフィルターが残っていない時点で、タイムアウトを待たずに終了します。[ブロードキャストはeventを送信中とマークする前に署名者の有無を確認し](https://github.com/relaystr/ndk/pull/908)、[zapリクエストのIDには保存されたcreated_atが使われます](https://github.com/relaystr/ndk/pull/907)。さらに、[NIP-11](/ja/topics/nip-11/)の[relayメタデータは共有キャッシュを通じて必要時に取得されるようになり](https://github.com/relaystr/ndk/pull/887)、同期のたびに処理を妨げることはなくなりました。

このプレリリースには、これまでソースのみだった変更も含まれます。[relay URLが重複するNIP-65リストが正しく統合されるようになり](https://github.com/relaystr/ndk/pull/914)、読み取りと書き込みのマーカーを組み合わせたうえで、outboxの書き込みrelayセットを保持します。作成者は、1回の観測で932件のプロフィールのうち5件のリストが誤読されているのを確認しました。[オプションのBUD-06アップロード事前確認](https://github.com/relaystr/ndk/pull/902)は、アップロード自体の認可を使って、サーバーがblobを受け入れるかどうかを問い合わせ、ステータスと理由を報告します。実際のアップロードが拒否された場合も、現在は同様に報告されます。404はサポート状況が不明であることを意味し、事前確認を通過してもアップロードの成功は保証されません。[NIP-77の照合タイムアウトに関する破壊的変更](https://github.com/relaystr/ndk/pull/888)では、単一のタイムアウトを、型付きエラーを伴うオープンタイムアウトとアイドルタイムアウトに分割し、認証待ちの時間は除外します。全体の期限は設けられていないため、進捗し続ける同期は無期限に実行される可能性があります。また、この変更がライブのrelayで検証されたことは確認していません。

未マージのプルリクエストでは、[識別子をキーとするNIP-05キャッシュ（ネガティブキャッシュ付き）](https://github.com/relaystr/ndk/pull/937)、[NIP-77向けにIDとタイムスタンプを返すキャッシュAPI](https://github.com/relaystr/ndk/pull/933)、[WebSocketの準備完了状態の処理](https://github.com/relaystr/ndk/pull/932)、[NIP-11の全フィールド対応](https://github.com/relaystr/ndk/pull/931)、[接続拒否時の完了処理](https://github.com/relaystr/ndk/pull/930)が提案されています。直近のステータス確認でもまだオープンのままである別の提案は、[ブラウザおよびFlutterプラットフォームのパスキー](https://github.com/relaystr/ndk/pull/909)を使ってアカウントの作成と復旧を行うものです。これは、派生鍵モードと保存鍵モード、さらに明示的なレガシーメタデータを備えたパスキーアイデンティティ設計のドラフトに沿っています。未知のハンドルは拒否され、新規アカウントとして扱われることはありません。また、保存された登録を保持する前に、復旧を独立して検証する必要があります。作成者は、すべてのパスキープロバイダー間での相互運用性はまだ検証されていないと述べています。

### Applesauce {#applesauce}

Nostr向けTypeScriptライブラリ群であるApplesauceには、changesetを伴う新たなソース変更がありますが、対応するリリースがあるとは主張しません。[スタンドアロンのメッセージングクライアントと明示的なrelay認証](https://github.com/hzrd149/applesauce/commit/a4f50406cdd625534a486b7d47369d59d004a24f)により、固定アカウント向けのNIP-04およびNIP-17クライアントが追加されました。これらは明示的にNIP-42認証リクエストを行い、準備済みの署名付き送信を再試行します。[スコープ付きのラップされた会話とrumorストア](https://github.com/hzrd149/applesauce/commit/056038ed7108c3f113035a06011a5f7acdf8365f)は、signerやネットワークの処理を開始することなく、kind 14のrumorとスレッドモデルを公開します。復号はデフォルトで無効です。ラップした送信には送信者を含む全参加者のkind 10050 relayが必要で、relayによる受理は相手側の受信を意味しません。[上限付きの復号済みコンテンツキャッシュ復元](https://github.com/hzrd149/applesauce/commit/d6ac42102747feb72372ac5970ce2743e4b685ca)は並行数がデフォルトで8であり、1に設定しない限りeventの順序が入れ替わる可能性があります。これらの平文キャッシュのスコープ設定と暗号化は、アプリ自身が行わなければなりません。続いて、[NDRトランスポートと、それとは別のCordnコーディネータークライアント](https://github.com/hzrd149/applesauce/commit/907a9591de867899aa7c84de1c4aa40628307a17)が登場しました。NDRは独自の別個のラチェット状態を永続化する必要があり、Submittedはローカルでの引き渡しを意味するもので、相手側の受信ではありません。Cordnはトランスポートのみを扱い、サンプルでは棚上げされており、MLSは実装していません。[ウィンドウ単位のKehto ContextVM統合](https://github.com/hzrd149/applesauce/commit/24ad6e9650e20cc92950c3fccbc0ac0263f6d443)は、各nappletウィンドウに一時的なContextVMアイデンティティを与えます。アカウント認証や支払いは伴いません。[アプリが所有する永続的な入金とnutzap復旧](https://github.com/hzrd149/applesauce/commit/cd483f5a610bf6fe8be7719ae5bb0dd0638c3296)の導入により、ウォレットへの新たな入金と償還には、利用側アプリが提供する復旧ストアと、mintによるNUT-09復元が必要になります。ジャーナルには使用可能なproof、シークレット、ブラインディングファクターが永続化されるため、暗号化したうえでアカウントごとにスコープを分けるべきです。再開は明示的に呼び出された場合にのみ実行され、署名済みIDを再利用し、relayによる受理が確認されるまでジャーナルを保持します。また、キャンセルしてもインボイスは無効になりません。[同期的なウォレット状態を伴うタイムラインスナップショットのバッチ化](https://github.com/hzrd149/applesauce/commit/1042bc595c35cb6199a76776daab482916beda57)では、タイムラインの更新を16 msの時間枠でまとめる一方、ウォレットトークンの状態は同期的なまま保たれます。[COUNTリクエストスケジューラ](https://github.com/hzrd149/applesauce/commit/564643fd648f5456387b54b3c8eddb79f165f46b)は[先週提案された](https://github.com/hzrd149/applesauce/pull/106)もので、このたびマージされました。並行数の上限は8から始まり、最初のレート制限エラーまたはトランスポートエラーが起きるまで倍増し、エラーのたびに上限が半減してクールダウンが加わります。タイムアウトはCountFailureとして表面化し、上限は下がりません。レイテンシはrelay選択の目安にすぎません。3つのrelayによるベンチマークでは、一般的な性能について主張するには依然として不十分です。

### eventstore {#eventstore}

fiatjafによるNostr event用ストレージバックエンドのライブラリである[eventstore](https://github.com/fiatjaf/eventstore)が、クエリに関する2件の修正をマージしました。これらを含むタグ付きリリースは確認されていません。すべてのバックエンドが、[NIP-01](/ja/topics/nip-01/)の[空のフィルターリスト](https://github.com/fiatjaf/eventstore/pull/79)に関するルールに従うようになりました。空のids、authors、kinds、またはtagリストは何にもマッチしませんが、存在しない（nil）tagリストは引き続き何の制限も課しません。[LMDBのeventカウントの修正](https://github.com/fiatjaf/eventstore/pull/78)により、マッチ後にHyperLogLogカーソルが前に進むようになり、カウントが永遠にハングすることはなくなりました。さらに、フィルターにauthor、kind、tagの指定がない場合、カウント時にそれらのチェックを適用しなくなりました。以前はこれが原因でゼロが返されていました。

### zsp {#zsp}

AndroidアプリをNostrに公開するためのZapstoreのコマンドラインツールであるzspが、[バージョン2.0.0をリリースしました](https://github.com/zapstore/zsp/releases/tag/v2.0.0)。[そのタグ時点のREADME](https://github.com/zapstore/zsp/blob/v2.0.0/README.md)では、人間がC1署名証明書の所有権を証明するウィザードと、エージェントに公開手順を伝える`zsp skill`コマンドが用意されています。キーストア、そのパスワード、いかなる秘密鍵もエージェントに渡すことは禁止されており、証明は人間が行うものとして保たれます。このリリースでは[JKSおよびPKCS12キーストアを内容から判別する](https://github.com/zapstore/zsp/commit/f767a1c4c98ba7130dd355f8da95afde6eeb8e08)ようにもなりました。そのため、.jksや.keystoreという名前のPKCS12ストアも、ウィザードと公開処理の両方で読み込まれます。私たちはこれを使った公開はテストしていません。

### nsite-gateway {#nsite-gateway}

Nostr上で公開された静的ウェブサイトを配信するnsite-gatewayが、[バージョン3.6.6をリリースしました](https://github.com/hzrd149/nsite-gateway/releases/tag/v3.6.6)。[ソース変更](https://github.com/hzrd149/nsite-gateway/commit/e7bbff215e23c0f3d9e23ee0ca14f5a2fb5e62dd)ではApplesauce 7にアップグレードし、eventの有効期限処理を復活させています。以前のバージョンでは、上流のタイマー値クランプのバグを回避するため、意図的に無効化した有効期限マネージャーに差し替えていました。そのため、期限切れのサイトeventがゲートウェイのストア内で無期限に有効なまま残る可能性がありました。上流で修正が入ったことで、ゲートウェイは再び通常のevent storeを使うようになりました。ここでの有効期限は、ゲートウェイが何を保持・配信するかを左右するものであり、relayやサードパーティのキャッシュからeventを削除するものではありません。デプロイ済みのゲートウェイはテストしていません。

### 44billion {#44billion}

Nostrアプリランチャーの44billionが、[権限の記憶方法を変更しました](https://github.com/44Billion/44billion/commit/4eb2cd9beecd8bb209dc7db47e99f338aacc5ac9)。保存された許可は、アプリ、権限名、eventのkind、スコープに紐づくようになり、ワイルドカードであるkind -1の許可が特定のkindを認可することはなくなりました。スコープが細分化されるのは、翻訳済みラベルを持つ登録済みのkindとスコープの組み合わせに限られます。未知のスコープは空のkind全体スコープにフォールバックし、レジストリは空の状態から始まります。IndexedDBのスキーマバージョン5は、起動時にバージョン4の許可を意図的にリセットし、サポートされないスコープ付き許可を削除しますが、その他のアプリデータは保持します。独自の個人用暗号化APIには、承認された標準ではないNIP-44 v3風のヘルパーが含まれています。これはソース変更であり、該当するリリースやデプロイは確認されていません。

さらに新しいソースでは、[アプリデータアクセス設定](https://github.com/44Billion/44billion/commit/9800ff204c3994c269b3dc7acdba8614a1819997)が追加されました。記憶された許可をアプリごとにまとめ、リロードせずに個別の許可またはアプリ全体の許可を取り消せます。取り消しが影響するのは、今後の保護されたリクエストのみです。すでに保存またはコピーされたデータは削除されず、すでに進行中の処理は停止されない場合があります。[Blossomのアセットキャッシュに関する変更](https://github.com/44Billion/44billion/commit/9bc2265a125a302ba61b09d13f52b2a8615218a9)では、本体全体のSHA-256が一致し、対応する検証済みマーカーが保存されて初めて、キャッシュされたアセットを完全なものとして扱います。古いキャッシュに由来する暫定チャンクは再検証され、ストリーミングが誤った最終チャンクを報告することもなくなりました。ただし、これは検証前にバイトが一切露出しないことを意味するものではなく、新しいバイナリリースもありません。

### Blossom Servers {#blossom-servers}

Blossom Serversディレクトリは、サーバーURLごとに[コミュニティによる機能レポートを追加しました](https://github.com/hzrd149/blossomservers/commit/b3546fb745c0859094157b0eb20e9b29fc2443a9)。各レポートには、その投稿者が明記されます。手動の申告とブラウザによる観測は区別して保持され、それぞれ90日後と24時間後にフィルターの対象から外れます。チェックでは、HTTPレスポンスと告知されたメソッドに加え、認証と支払いのチャレンジも調べます。匿名のブラウザチェックは、何もアップロードせずに68バイトのPNGのメタデータを提示するHEADリクエストを送ります。したがって、200の応答は実際のアップロードが機能することの証明にはなりません。ディスカッションの読み込みはスコープが限定されるようになり、以前の運営者の権威を暗に示す扱いは、投稿者の明記に置き換えられました。レポートは誰がサーバーを運営しているかの証明ではなく、全体的な稼働率やBUDへの完全準拠については何も示しません。また、投稿者同士の意見が食い違うことも、投稿者が誤っていることもあり得ます。デプロイやリリースは検証していません。

さらに新しいソースでは、[設定可能なアプリ用relayとルックアップ用relayが追加され](https://github.com/hzrd149/blossomservers/commit/9ff8112963d68dee9c92d698740e47a23df7caf1)、NIP-65を通じてアカウントとoutboxを読み込むようになりました。既存の公開kind 10086ルックアップリストがあれば、それが優先されます。保存時に公開リストが更新されるのはそれがすでに存在する場合のみで、それ以外の場合はローカルにとどまります。ローカルの公開記録は、少なくとも1つのrelayがeventを確認応答した後にのみ更新されますが、これはすべてのrelayが受信したことを意味しません。リリースやデプロイは確認されていません。

### Ditto {#ditto}

SoapboxによるNostrクライアントのDittoは、トランスコードされた動画がiOSで再生できるよう、[不正な形式のWebCodecsエンコーダーが生成したH.264メタデータを修正しました](https://gitlab.com/soapbox-pub/ditto/-/commit/1c30cbac)。avcCレコード内の重複したSPSおよびPPSのNALヘッダーバイトや不正な予約ビットを検出し、MediabunnyのmuxerがMP4メタデータを書き込む前に修復します。正しい形式のレコードや認識できないレコードには手を加えません。バージョン2.45.1が公開されていますが、この修正が含まれているかは確認しておらず、実機のiOSデバイスでの再生もテストしていません。この変更が対象とするのはこのH.264の不具合であり、あらゆるコーデックや動画ではありません。

### Amberのデスクトップsignerと Android版のNIP-46修正 {#amber-desktop-signer-and-android-nip-46-fix}

AndroidのNostr signerであるAmberは、10月27日に、Compose製のデスクトップ向けNIP-46 signer（Windows/macOS/Linux）のソースをマージしました。これはAndroid版のアプリ単位・kind単位の権限モデルを踏襲しています（[コミット](https://github.com/greenart7c3/Amber/commit/1c12bb17e72d5b4ad46753062c1681d4af64adeb)）。NIP-55は引き続きAndroid専用です。デスクトップ版のコードは、複数アカウントと、アプリごとのrelayと履歴を備えたnostrconnect/bunker接続に対応し、さらにTorとトレイ通知もサポートします。鍵は必須のArgon2idパスフレーズで保護された暗号化PKCS12ストレージに保管され、アカウントごとのデータベースも暗号化されます。デスクトップ版のパッケージングや実行時の動作は検証していません。

これとは別に、デスクトップsignerではなくAndroidアプリに対してマージされた変更では、[アカウントのログアウト後にNIP-46のrelayサブスクリプションと接続フィルターを更新する](https://github.com/greenart7c3/Amber/commit/2fbb1ee7bea7d5df574db5ca70b73841e8ba500d)ようになりました。その結果、Amberは削除されたアカウントの鍵に対する待ち受けをやめます。内容を伏せたロック画面通知には、リクエストの説明も表示されるようになりました。これにより通知はより有用になりますが、プライバシーが高まるわけではありません。いずれのAndroid向け変更についても、それを含む新しい安定版リリースは確認されていません。

### noStrudelのnappletインテントと同期されるアプリデータ {#nostrudel-napplet-intents-and-synced-app-data}

WebクライアントのnoStrudelは複数のソース変更をマージしましたが、タグやデプロイは確認されていません。napplet間のインテントはカタログとz/iマニフェストの宣言を通じて解決され、受理されたペイロードは、ターゲットフレームの読み込み後に、ランタイムが証明した送信者IDとともに配信されます。サポートされないインテントは拒否され、ターゲットを明示的に指定するハンドラーにはユーザーの確認が必要です（[コミット](https://github.com/hzrd149/nostrudel/commit/e0211136e71dac6de2bb8af2c0d9e291b02df9ba)）。インストール済みのnappletとデフォルトハンドラーは、NIP-44で暗号化されたkind 30078のアプリデータにより、3-wayマージを用いてアカウントごとに同期されます（[コミット](https://github.com/hzrd149/nostrudel/commit/887a6194c8cbab9ce6d780eb62961714777f72f5)）。また、選択した[NIP-66](/ja/topics/nip-66/)のrelayモニターは、暗号化されたNIP-78アプリデータを通じて同期されます（[コミット](https://github.com/hzrd149/nostrudel/commit/5a20096f4bcdfbd7ff86b4676cd5653d637ea4bf)）。NIP-17メッセージは、キャッシュ済みのgift wrapを読み込んで復元し、セッションごとに1回、DM relayから30日分を照合します。サポートされている場合はNIP-77を使い、それより古い履歴はオンデマンドで取得します（[コミット](https://github.com/hzrd149/nostrudel/commit/ce95080547485fb403c68f71ce6ad0404f42d230)）。

### Nostr Feedzがアーカイブ化 {#nostr-feedz-archived}

RSSとNostrの長文記事や動画を組み合わせていたNostr Feedzは、アーカイブ済みでありもうメンテナンスされていないとREADMEに明記しました（[コミット](https://github.com/PlebOne/Nostr-Feedz/commit/3b6f6967e532e1f0f4a3503354737cebc3350895)）。この告知では、開発を継続するフォークとして、PrivKeyによる[Readstr](https://github.com/privkeyio/readstr)が案内されています。これはメンテナンス状況の変更です。GitHub上でリポジトリがアーカイブとしてマークされているかどうか、またアカウントやデータが引き継がれるかどうかは確認していません。

### Zap Cookingの保護付きリスト、signer修正、パスキーによるサインアップ {#zap-cooking-guarded-lists-signer-fixes-and-passkey-signup}

Nostrのレシピ共有クライアントであるZap Cookingは、Web版ソースの大量の変更をマージしました。デプロイやリリースは確認されていません。保存済みのkind 30001リストへの書き込みは、まず読み込みを行い、アカウントごとに直列化されるようになりました。最新の完全なベースから外部由来のtagと暗号化コンテンツを保持し、relayリストが不明な場合やクォーラムが足りない場合は書き込みを拒否します（[#869](https://github.com/zapcooking/frontend/pull/869)）。クォーラムには、リストに対応したEOSE応答が少なくとも2件と、ユーザーの対応可能な書き込みrelayの半数が必要です。また、nostr.wineからの空の応答は、存在しないことの証明にはなりません（[#878](https://github.com/zapcooking/frontend/pull/878)）。カスタムコレクションも同じ保護付きの書き込み処理を共有し、キューに入っていた古い操作は新たなガードのもとで再実行されます（[#885](https://github.com/zapcooking/frontend/pull/885)）。さらに、集約された空のEOSEだけでリストが空として表示されることはなくなりました（[#872](https://github.com/zapcooking/frontend/pull/872)）。

明示的な認証方式の導入により、本番環境のminificationでsignerクラスが混同されるバグが修正されました。これにより、NIP-46と[NIP-07](/ja/topics/nip-07/)の暗号化には、古いローカル鍵ではなくアクティブなsignerが使われます。NIP-46では、relayへのウォレットバックアップは引き続きブロックされます（[#896](https://github.com/zapcooking/frontend/pull/896)）。保存やリアクションをきっかけに開始したログインは、完了後にその操作を再開します。保留中のzapは金額と対象を保持しますが、送信操作は引き続き必要です。signerが拒否した場合はエラーが表示され、無関係な鍵で黙って再署名することはありません（[#867](https://github.com/zapcooking/frontend/pull/867)）。

サインアップではアイデンティティがローカルで作成され、パスキーで暗号化された vault 同期がデフォルトで有効になります。同期がオフの場合やアップロードに失敗した場合はバックアップキーが必要で、Google Drive は復元専用です（[#893](https://github.com/zapcooking/frontend/pull/893)）。WebAuthn PRF のワンプロンプト設定では、vault は未確認のままとなり、平文の nsec もブラウザに残ります。その後 vault の復号に成功した時点で、vault が確認され、平文の鍵が削除されます（[#907](https://github.com/zapcooking/frontend/pull/907)）。このプロンプトをサインアップにも拡張する変更は、認証ではない署名なしの登録に依存しています。新しいサーバーチャレンジを入手した者なら誰でも検証を通過する登録を偽造でき、credential ID を知る攻撃者は未確認のエントリ（TTL 30日）を置き換えて、正規ユーザーの同期を妨げることができます（[#911](https://github.com/zapcooking/frontend/pull/911)）。これらは文書化されたトレードオフであり、セキュリティ上の保証ではありません。

ノートへのリンクは [NIP-19](/ja/topics/nip-19/) の nevent としてエンコードされ、観測された relay ヒントを最大3つ含みます。これにより、複製の少ない event をクライアントが見つけやすくなりますが、可用性は保証されません（[#873](https://github.com/zapcooking/frontend/pull/873)）。プロフィールの Replies には、event をルートとする [NIP-22](/ja/topics/nip-22/) の kind 1111 コメントが含まれるようになりました（[#877](https://github.com/zapcooking/frontend/pull/877)）。また、座標パーサーの修正によって、URL の d-tag を持つレシピがパックやプランに残るようになっています（[#888](https://github.com/zapcooking/frontend/pull/888)）。プレミアムレシピのペイウォール実験は、作者自身による監査でクエリ pubkey によるバイパスが見つかったことを受けて終了しました。従来の kind 35000 の投稿は、保存済みコンテンツとして読むことができます（[#862](https://github.com/zapcooking/frontend/pull/862)）。

ミュートリストを対象とする提案がオープンになっていますが、まだマージされていません（[#921](https://github.com/zapcooking/frontend/pull/921)）。この提案では、ミュートリストの取得が利用不能だった場合を、リストを返した成功した取得やリストなしを返した成功した取得とは区別して扱います。利用不能だった取得を空のリストとして5分間キャッシュすることもなくなります。パースの失敗は再試行され、非公開ミュートの復号に失敗した場合は警告が表示されます。通知ベルを開くと、リストが再読み込みされます。目的は、気づかれないまま古くなった空のミュートリストのせいで、ミュートした作者が通知に入り込むのを防ぐことです。すべての失敗でコンテンツをブロックするようになるわけではなく、デプロイもされていません。

### Lumilumi の NWC による zap 支払い {#lumilumi-nwc-zap-payments}

Nostr の Web クライアントである Lumilumi に、zap のインボイスを Nostr Wallet Connect（NIP-47）経由でワンタップで支払えるようにするドラフトのプルリクエストがあります（[#1120](https://github.com/TsukemonoGit/lumilumi/pull/1120)）。支払い権限を持つ接続 URI はローカルにのみ保存され、平文の kind 30078 設定バックアップからは除外されます。ウォレットが nip44_v2 を告知している場合、リクエストには NIP-44 が使われ、そうでない場合は NIP-04 にフォールバックします。作者は実際の支払いを伴わないモックウォレットで動作を確認しました。このドラフトは、本誌の情報源締め切り時点で未マージでした。

### Wisp の識別子検索 {#wisp-identifier-search}

Wisp Nostr クライアント向けのオープンなプルリクエスト（本誌の情報源締め切り時点で未マージ）は、貼り付けられた NIP-19 や NIP-05 の識別子、hex キー、Web のエンティティリンクを検索で認識させ、該当しない場合に [NIP-50](/ja/topics/nip-50/) のテキストクエリへフォールバックさせるものです（[#681](https://github.com/barrydeen/wisp/pull/681)）。参照には relay ヒントとローカルキャッシュが使われます。検索は、問い合わせ先の relay からの EOSE を最大15秒まで待つ間も結果をストリーミングするようになり、遅い relay が切り捨てられることはなくなります。作者が報告しているのはエミュレーターでのテストのみで、実機ではテストしていません。

### Zapstore の Android TV 対応 {#zapstore-android-tv-support}

Nostr ベースのアプリストアである Zapstore には、Android TV 向けのオープンな v2 プルリクエストがあり、本誌の情報源締め切り時点で未マージです（[#407](https://github.com/zapstore/zapstore/pull/407)）。この変更は 32 ビット ABI にマッチさせ、リモコンのみで操作する Leanback フォーカスをサポートするもので、インストール許可画面が利用できない場合のフォールバックも備えています。Arti を含まない 32 ビットビルドでは Direct のみの接続であることを明示し、Arti が欠けている 64 ビットビルドはフェイルクローズします。TV ビルドが使うローカルのデバッグ署名者はテスト用であり、配布用ではありません。また、作者が行った唯一の TV テストでは、公開バンドルが利用できなかったため、ローカルでビルドした relay を使用しました。

### strfry の堅牢化と NIP-11 の提案 {#strfry-hardening-and-nip-11-proposals}

C++ 製の Nostr relay である strfry には、本誌の情報源締め切り時点で未マージの提案が2つあります。[#281](https://github.com/hoytech/strfry/pull/281) は relay 監査の指摘事項 SF-01 から SF-13 に対応するもので、JSON の深さ、展開後のペイロード、キュー、メトリクスのラベルに上限を設け、空の negentropy フィルターによるクラッシュを修正し、長い tag のインデックスをハッシュ化します。DB フォーマット 4 に移行するため、採用者はエクスポートと再インポートを行うことになります。テストの合格は作者自身によるものです。ドラフトの [#278](https://github.com/hoytech/strfry/pull/278) は、実際に適用される [NIP-11](/ja/topics/nip-11/) の limitation のみを、任意の fees と payments_url とともに告知するものです。payment_required のデフォルトは false で、設定された価格自体は支払い機能を実装しません。

### nostrcheck-server の Bark 支払い {#nostrcheck-server-bark-payments}

Nostr のメディアホスティングサーバーである nostrcheck-server に、barkd（Bark）の支払いプロバイダーを追加するドラフトのプルリクエストがあります（[#62](https://github.com/quentintaranpino/nostrcheck-server/pull/62)）。barkd の REST API を通じて Lightning インボイスを作成し、オプションでファイルごとの X-Ark BIP-321 URI を 402 レスポンスに付与するもので、同じ Lightning インボイスがフォールバックになります。同じ Ark サーバー上のウォレットは Ark で支払い、それ以外のウォレットは Lightning を使います。決済済みの支払いによって、ファイルが1回アンロックされます。テストはモック化した barkd を使用しており、オープン中の BUD-07 プルリクエスト #61 に依存しています。本誌の情報源締め切り時点で未マージであり、share.yabu.me の機能ではありません。

### mattn の nostr-relay の有料書き込み {#mattn-nostr-relay-paid-writes}

mattn の nostr-relay 向けのドラフトのプルリクエスト（本誌の情報源締め切り時点で未マージ）は、Bark ウォレットを通じたオプションの有料書き込みを追加するもので、デフォルトではオフです（[#37](https://github.com/mattn/nostr-relay/pull/37)）。pubkey は barkd を通じて書き込み料金を前払いし、オプションで kind フィルターを指定できます。クレジットのない書き込み者には、支払い URL 付きの restricted: レスポンスが返されます。チャージには BIP-321 URI または NWC を介して Ark か Lightning を使い、料金は NIP-11 に掲載されます。テストはモックのデーモンを使っています。この機能をツリー内に含めるべきか、フックの背後に置くべきかは決まっていません。

### ContextVM の再接続時リプレイ防止 {#contextvm-reconnect-replay-guard}

MCP を Nostr 上で運ぶ ContextVM に、relay の再接続後の重複実行を防ぐ、TypeScript SDK 向けのオープンなプルリクエストがあります（[#113](https://github.com/ContextVM/sdk/pull/113)）。サーバートランスポートは、検証済みの event ID をクローズするまで保持します。さらに、別個の上限付きエンベロープキャッシュが、再ラップされた重複をブロックします。メモリはトランスポートの存続期間中、一意の検証済み event の数に応じて増加します。この修正は本誌の情報源締め切り時点で未マージで、リリース済みパッケージにも含まれていません。

### Kehto シェルのメディア再生と承認 {#kehto-shell-media-playback-and-approvals}

Nostr の napplet 向け Web シェルである Kehto は、[10月28日に NAP-MEDIA の再生機能をマージしました](https://github.com/kehto/web/pull/354)。Paja と playground の両ホストは、ポリシーを介した音声・動画プレーヤーを共有するようになりました。有限の URL および Blossom ソースにはブラウザのコーデックを使います。MediaSource がコーデックに対応している場合は、ライブの HTTPS MP3 または ADTS AAC ストリームも、レスポンスが終わる前から再生します。セッションの権限は、エンドポイント、ソースウィンドウ、ACL に結び付けられたままです。失効または破棄が起きると、Blob URL が廃棄され、再生が停止し、ストリームがキャンセルされます。ホスト専用の ResourceService.openStream メソッドは、既存のエンドポイントオリジンの許可とポリシーを使用し、リソース用のワイヤーメッセージは追加しません。終端時の配信は残っています。従来の sendCommand エイリアスも引き続き動作します。これとは別に、判別可能な2引数のコールバックは警告付きで引き続き動作します。単項の従来型コールバックは、コマンドオブジェクトに移行します。ブラウザのリゾルバーは、HTTPS 以外の URL、認証情報、プライベート IP リテラルを拒否します。リダイレクトとリファラーも無効にします。ただし DNS を検査できないため、名前解決時のプライベートアドレス保護は保証されません。本番のリゾルバーには DNS 解決時のチェックが必要であり、ブラウザのデフォルトは CORS とプライベートネットワーク保護に依存しています。HLS、DASH、ライブ Ogg、Nostr ソース、キュー、永続化、フォーカス時の自動再開は、引き続き未対応です。作者は 155 件の Chromium テストと、無改変の Funclet アーティファクトによる 112 秒間のラジオ再生を報告していますが、本誌では再実行していません。これはソースのみの作業です。公開されている Napplet 0.32 パッケージには、一部のドラフト型が含まれていません。NAP-MEDIA は依然としてドラフトであり、リリースとしての準拠は主張されていません。

もう1つのマージされた変更は、[署名と公開の承認をバージョン固有のものにします](https://github.com/kehto/web/pull/357)。各承認は、検証済みの公開者、アーティファクトのハッシュ、アクティブな署名者に結び付けられます。承認は取り消すことができ、署名のみの承認と公開のみの承認は別々に扱われます。従来の権限が黙って昇格されることはありません。変更可能な開発用 URL への同意はその読み込みの間だけ有効で、エンドポイントやアカウントが変わると保留中のリクエストは拒否されます。NAP-LINK は、ホストのモーダルで明示的にクリックされた後にのみ、noopener を使ってリンクを開きます。この変更は外部の CVM ラジオソースに対する網羅的なテストを主張するものではありません。また、ソースのマージは npm リリースを示すものでもありません。

### Pact {#pact}

[Pact](https://github.com/bobodread876/pact/pull/17) は、エージェント間の関係とオペレーターの同意のための Nostr プロトコルで、Nostr Wallet Connect の応答を認証するようになりました。各結果にはウォレットの署名が付き、対応するリクエストを参照していなければなりません。Pact は結果の種類と支払いハッシュを確認し、preimage が返された場合はそれも検証します。償還処理にはアトミックな台帳書き込みと、リクエストの消費および再試行に対するガードが加わり、同意を偽造できる経路もさらに塞がれました。[MCP の支払いに上限を設けるフォローアップ](https://github.com/bobodread876/pact/pull/18)では、`PACT_MCP_ALLOW_PAYMENTS=1` が設定されていない限り支払いを無効のままにし、デフォルトの 1,000 sat の上限を、記載された金額と BOLT11 の金額の両方に照らして確認します。非公開受信箱のウィンドウは 200 ラップで停止し、切り捨てが発生したことを示すようになりました。作者のテストはモックに依存しています。

### nostr.watch {#nostrwatch}

Nostr relay モニターである [nostr.watch](https://github.com/sandwichfarm/nostr-watch/pull/961) は、FIPS の検出とトランスポートを明示的にサポートするようになり、オーバーレイの参照が公開の DNS-over-HTTPS にフォールスルーすることはなくなりました。DNS と IPv6 のルーティングは、引き続きホスト側が提供します。モニターには FIPS デーモンやプロキシが同梱されておらず、匿名性も提供しないためです。[より厳格な npub チェック](https://github.com/sandwichfarm/nostr-watch/pull/964)により、npub はパースされた `.fips` ホスト名の中でのみ受け付けられます。[NIP-11 と NIP-05 の自動プローブはアプリ所有の ServiceWorker に移され](https://github.com/sandwichfarm/nostr-watch/pull/959)、観測された拡張機能駆動のナビゲーション経路から、所有タブのコンテキストが取り除かれました。この点は、標準の Firefox 155 で、制御された拡張機能のフィクスチャを使って確認されています。[準拠テストスイート](https://github.com/sandwichfarm/nostr-watch/pull/960)には、範囲を限定した NIP-01 チェックが15件含まれており、独立した接続をサポートする会話レイヤーを備えています。作者はテストの合格と隔離されたメッシュでの実行を報告していますが、これは公開 relay での監査やブラウザセキュリティの監査ではありません。

### Bitcredit Core {#bitcredit-core}

Nostr を利用するピアツーピアの信用・手形プロトコルである [Bitcredit Core](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1060) は、ブロック操作がローカルに何かを永続化したり、その効果を引き起こしたりする前に、少なくとも1つの書き込み relay が接続されていることを確認するようになりました。リカバリーもクリーンに再初期化されます。先週オープンとして報じた[候補チェーンの検証](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1059)はその後マージされ、チェーンは永続化される前に検証・準備されるようになりました。これらの手順により、ローカルの状態が不整合になる可能性は低くなります。relay が接続されていても、relay が event を受け入れることや決済が完了することは保証できません。また、そのチェックだけでローカルの永続化が耐久性を持つようになるわけでもありません。

リリースでの収録は確認されていない、より新しいマージにより、[アイデンティティサービスにトランザクションマネージャーが追加されました](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1063)。アイデンティティのブロック、状態、メール確認は、Nostr 経由で何かが伝播する前にアトミックにコミットされるようになりました。新しいテストでは、コミットが失敗した場合に何も送信されないことを確認しています。対象はアイデンティティサービスのみです。手形と会社の永続化にはこのアトミックなコミットがなく、relay による受け入れと決済も依然として保証されません。

### MLS-KMP と Marmot の互換性 {#mls-kmp-and-marmot-compatibility}

marmot-kmp の基盤となる Kotlin 製 MLS ライブラリ [MLS-KMP](https://github.com/vitorpamplona/mls-kmp/pull/9) は、以前、他の MLS 実装に合わせるためにいくつかのワイヤー上の挙動を修正しました。そのため、列挙されたケースでは 1.2.0 のメンバーとその新しいコードのメンバーとの間で食い違いが生じ、グループは一斉にアップグレードする必要があります。保存された状態はバージョン 10 に移行しており、古いリリースでは復元できません。下流の Marmot 互換性ジョブはノンブロッキングです。そのテストはこの変更の作成環境では実行されておらず、Marmot は引き続き `authorizeProposal` と GREASE に対応する必要があります。それ以前の [app-components の変更](https://github.com/vitorpamplona/mls-kmp/pull/7)は、Marmot が MDK v0.14 に従うために必要なコンポーネントを強制します。Amethyst での採用状況は、本誌では確認していません。

リリース済みの 1.3.0 に含まれるとはされていない、より新しいマージ済みソースは、[ナイトリーの相互運用ランナーのコンパイルを修復し](https://github.com/vitorpamplona/mls-kmp/pull/14)、スクリプトごとに pass、fail、skip を報告します。したがって、ライブランナーが一度も実行されていないという本誌の以前の記述は古くなっています。作者は実行が機能していると報告していますが、変更がオープンされた時点で最後の実行はまだ進行中であり、本誌は最終的な CI 結果を確認していません。OpenMLS ジョブはノンブロッキングのままで、未対応またはパニックする 22 のシナリオをスキップし、ciphersuite 0x0001 のみを対象としているため、相互運用性を保証するものではありません。この変更では、保持されたグループ ID による ReInit PSK の参照、エポック 0 の暫定トランスクリプト、最初のエポックのランダムシークレット、外部コミット時の再開 PSK の処理も修正されています。エポック 0 のトランスクリプトについては、コードが OpenMLS に合わせて RFC 9420 の 11 節に従うようになりました。そのため、エポック 0 への外部参加は 1.3.0 およびそれ以前のリリースとは異なり、保存済みの古いグループは最初のコミットまで古いハッシュを保持します。元のエンジンは、最初のエポックシークレットをゼロから導出していました。後続のコミットには新しい UpdatePath が含まれることから、作者はエクスプロイトを見つけていませんが、この修正はすべてのセキュリティ問題が解決されたことを示すものではありません。

### Obelisk Relay {#obelisk-relay}

[Obelisk Relay](https://github.com/obelisk-app/obelisk-relay/commit/d575c071729eb5230e73b95d2e2d9db219d5c00b) は、非公開の NIP-29 グループに関する修正をデフォルトブランチにマージしました。グローバルな relay 管理者は以前から非公開グループに対して REQ を送信できましたが、event の可視性フィルターが該当する event を拒否していました。現在は relay 管理者がこれらの event を読めるようになり、メンバーのアクセスチェックも維持されています。relay 内で非公開のグループはエンドツーエンド暗号化されておらず、この変更はサーバー管理者から見えることを明示的にするものです。この修正は、開発者と運用者向けのマージ済みソースの作業です。

### Plume {#plume}

Rust と Tauri で構築されたデスクトップクライアント [Plume](https://github.com/cpkb-bluezoo/plume/commit/2e962efb73bf7ef82d5394dc96240d3fb136a428) は、relay ごとに、永続的で自動再接続する WebSocket を 1 本だけ維持する変更をマージした。フィード、プロフィール、パブリッシュ、ダイレクトメッセージの各操作は、すべてこの接続を共有する。サブスクリプションと event ID は、この接続上で多重化される。再接続の試行には段階的なバックオフがかかり、アプリの終了時には接続が閉じられる。この変更の前は、操作のたびに新しいソケットが開かれ、そのまま解放されずに残っていた。レビューを経たこの変更は、マージ済みのソースコード上の作業である。パフォーマンスの測定結果は、ここでは確認されていない。損失のない復旧や配信の保証を約束するものでもない。

### Hashtree {#hashtree}

Hashtree の [TypeScript ランタイム 0.5.22](https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.22) では、ブラウザのプロバイダが、署名済みの現行の公開ピアアナウンスを最大 256 件まで IndexedDB に保持できるようになった。保持はアイデンティティとアプリごとにスコープが分けられる。プロバイダは、ネットワーク探索の前にそれらを再読み込みできる。通常のピア REQ は、既存の受け入れルールが許す範囲でこのキャッシュをリプレイできる。一方、プライベートな探索は別のオーナースコープに分離されたままとなる。これとは別に、マージ済みの [Rust アダプタの変更](https://github.com/mmalmi/hashtree/pull/4)は、放棄されたインデックス読み取りをキャンセルする。そのため、コマンドがトランスポートのタイムアウトが満了するまで待ち続けることはなくなった。このプルリクエストは hashtree-nostr-pubsub 0.2.87 を公開済みと報告している。なお、このパッケージは TypeScript ランタイムとは別にバージョン管理されている。ソースのみに存在する Rust クライアントのコミットでは、[読み取り時にレガシー、読み取り、書き込みの各 Blossom オリジンを統合して使う変更](https://github.com/mmalmi/hashtree/commit/cc1c73c1733bd14673bad6c87eae6829330b25cf)と、ソースごとに[型付きのリクエスト段階の接続リセットに対して 1 回だけ再試行する変更](https://github.com/mmalmi/hashtree/commit/57b30cfdfac3c745c1c3c7083459eb2512ad1ef1)が追加された。どちらも部分的なレスポンスはキャッシュしない。Mac での 1 回のコールドインストールだけでは、断続的な転送タイムアウトが修正されたことの証明にはならない。

### nostr-pubsub {#nostr-pubsub}

[nostr-pubsub TS 0.5.20](https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.20) は、署名済み event を上限付きのストアに保持する。さらに、通常の Nostr REQ に向けて、IndexedDB による永続化、タブ間のアトミックなトランザクション、有効期限の処理、ローカルリプレイを追加する。同じソースでは別途、アトミックなスナップショットと排他的なライターリースを備えた、オプションのネイティブ Rust ファイルストア API についても説明されている。これは TypeScript パッケージとは別物である。[永続 event ストアの実装](https://github.com/mmalmi/nostr-pubsub/commit/0ee66735e248d9b635caa3f44bdf8b23daf59b0d)では、再読み込みの際に、署名と、NIP-01 の置換可能 event でどれが勝者になるかを再確認する。エフェメラル event と、現在時刻より 5 分を超えて先のタイムスタンプは拒否される。ストアが暗黙的に開かれることはなく、公開アナウンスのスコープは呼び出し側が選択する。FIPS は、ネットワーク探索の前に署名済みの kind 37195 アナウンスを復元する。その場合も、鮮度、スキーマ、名前空間のチェックは引き続き行われる。匿名またはプライベートな探索のキャッシュは、公開リプレイと分離しておかなければならない。また、ネットワークから取得するルーターをリプレイ元として使うべきではない。保持量に上限があるため、無期限のオフラインブートストラップは提供されない。

### FIPS-TS {#fips-ts}

[FIPS-TS ランタイム 0.0.57](https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.57) は、アプリケーションが所有する永続的な探索プロバイダを受け付ける。このプロバイダは、既存のインターフェースを通じて、署名済みの kind 37195 アナウンスをパブリッシュおよびサブスクライブする。プロバイダが注入されている場合、トランスポートは Nostr の relay クライアントを一切開かず、空の relay リストも受け入れる。シャットダウン時には、保留中のサブスクリプションがドレインされる。プロバイダのライフタイムと復元されたストレージの管理は、呼び出し側の責任となる。名前空間、署名、有効期限のチェックは引き続き適用される。ピアの認可も依然として必要である。キャッシュされたアナウンスがあっても、オフラインブートストラップが保証されるわけではない。新たな認証済みルーティングと WebRTC シグナリングには、到達可能な FIPS キャリアが引き続き必要だからだ。

### Flotilla {#flotilla}

Flotilla は 3 件のソース変更をマージした。[チャットへの共有（Share to Chat）](https://gitea.coracle.social/coracle/flotilla/pulls/847)によって、ユーザーは単独のノートや NIP-22 コメントを、任意のルームや会話に共有できる。会話の中で引用しても、引用元の作者が p-tag に追加されたり、メンバー構成が分岐したりすることはなくなった。[中断されたアップロードの再開](https://gitea.coracle.social/coracle/flotilla/pulls/849)では、添付ファイルのアップロードが下書きから復元される。アップロードが失敗した場合はエラーが表示され、ユーザーはそこから復旧できる。圧縮に失敗すると元のファイルにフォールバックするため、そのファイルのメタデータが残る可能性がある。[保存済み既読マーカーの待機](https://gitea.coracle.social/coracle/flotilla/pulls/846)は、保存されている既読状態が読み込まれるまで、ページの既読マーカーの書き込みを保留する。これにより、起動時の早い段階で発生した既読の更新が失われなくなる。

### following.space {#followingspace}

[following.space](https://github.com/callebtc/following.space) に対するオープンなプルリクエストは、当方のソース締め切り時点では未マージだった。このプルリクエストは、[フォローパックの作成、編集、削除を復活させる](https://github.com/callebtc/following.space/pull/25)もので、パックのメンバーをフォローする機能も併せて復活させる。アカウントと outbox relay の探索には Applesauce を使い、パックは `naddr` アドレスとして共有する。対応する署名方式は、ブラウザ拡張機能の署名者、メモリ内にのみ保持されるシークレット、bunker 署名者である。コードと、作者が説明しているテストからは、サービスがデプロイされていることも、あらゆる署名者と互換性があることも示されない。

### Routstr {#routstr}

Routstr の 3 件のプルリクエストは、当方のソース締め切り時点でオープンのまま、未マージだった。コアサービスでは、[プロバイダのヘルス探索](https://github.com/Routstr/routstr-core/pull/885)が、グローバルでないアドレスに解決されるアナウンス済みの URL とリダイレクトを拒否するようになる。onion プロキシの扱いはそのまま維持される。作者らはサーバーサイドリクエストフォージェリ（SSRF）の危険性とテストについて説明しているが、これはデプロイ済みの修正でも、確認されたエクスプロイトでもない。SDK では、[URL に対するプロバイダのクレジット](https://github.com/Routstr/routstr-sdk/pull/123)が、kind 38421 event に署名した鍵に従って決まるようになる。コンテンツ内に書かれた pubkey は、未検証のまま扱われる。作者がデフォルトの relay 上で確認した 81 件の event のうち、コンテンツに基づくプロバイダリストを含むものは 1 件もなかった。したがって、既知の URL が悪用されたとも、すべてのプロバイダが安全になったとも主張されていない。[モデルパスの自動ピン留め](https://github.com/Routstr/routstr-sdk/pull/125)は、組み込みの定数から、信頼されたアドレス指定可能な kind 38427 event に含まれる署名済みスナップショットへと移行する。SDK は最後の正常なスナップショットとロールバックのウォーターマークを保持し、空のスナップショットはキルスイッチとして機能する。この変更は、カスタムアダプタの API に互換性のない変更をもたらす。ポリシー event はまだ一つも公開されておらず、ロールアウトは依然としてオペレーター側が行う作業である。

### SatSigner {#satsigner}

SatSigner に対するオープンなプルリクエストは、当方のソース締め切り時点では未マージで、[Nostr の relay、キャッシュ、同期のレイヤーを作り直す](https://github.com/satsigner/satsigner/pull/687)ものだ。event が見つからない状態（relay が保存済み event の終わりを示す応答を返した場合）は、タイムアウトとも、relay がまったく存在しない状態とも区別して扱われるようになる。古くなったキャッシュ済みコンテンツには、フラグが付けられる。処理によってカーソルが進む前に event が保存され、gift-wrap の rumor ID も検証される。アイデンティティを削除すると、そのアイデンティティの Nostr テーブルが消去される。ただし、kind 0 の同期によって、ローカルでのプロフィール編集が上書きされる可能性はある。これに[スタックされたフォローアップ](https://github.com/satsigner/satsigner/pull/688)では、機密情報を伏せた診断情報が追加される。Nostr フィードでは、タップすると読み込まれる動画ポスターが表示され、プレーヤーは最大 3 つに制限される。さらに、relay プールを破棄せずに、アプリ再開時に取りこぼした分を取得する機能も追加される。障害を注入する relay テストも加わる。新しいネイティブ動画モジュールを使うにはアプリの再ビルドが必要で、実機での検証はまだ終わっていない。どちらの変更もリリースされておらず、ランタイムでのチェックも通過していない。

### Bray {#bray}

[Bray 3.5.4](https://github.com/forgesworn/bray/releases/tag/v3.5.4) は、NIP-46 の bunker クライアントとデーモンに、NIP-42 による relay 認証を追加した。これにより、AUTH を必要とするプライベート relay を使って、bunker 宛てのメッセージを読み取れるようになった。それより後のソース変更がこのタグに含まれていることは、確認されていない。

その後にマージされたソースでは、署名者が設定されていない場合、または BRAY_READ_ONLY が強制されている場合に、Bray の MCP サーバーが[読み取り専用で起動する](https://github.com/forgesworn/bray/pull/139)。この判断は、シークレットを一つでも開くより前に行われる。このモードではウォレットは読み込まれず、署名、暗号化、復号はいずれも拒否される。利用できるのは、261 個あるツールのうち、参照系の 111 個だけである。CLI と SDK は引き続き署名者を必要とし、設定はされているが中身が空のシークレットファイルも、これまでどおりエラーとなる。新しいアテステーションは nip-va に代わり、[現在は](https://github.com/forgesworn/bray/pull/140) [NIP-32](/ja/topics/nip-32/) のアテステーションラベル名前空間を使用している。既存の #l タイプのクエリでは新旧どちらのラベルも検出できるが、signet-protocol は独自の 2.5.5 のコピーを保持したままである。これは NIP として正式に採用されたことを意味するものではない。ネストされたすべてのライブラリが移行したという意味でもない。どちらの変更についても、3.5.4 に含まれていることは示されていない。

### Alby browser extension {#alby-browser-extension}

[Alby Lightning ブラウザ拡張機能](https://github.com/getAlby/lightning-browser-extension)に対するオープンなプルリクエストは、当方のソース締め切り時点では未マージだった。このプルリクエストは、[パーミッションヘルパーが、記憶済みのブロックエントリを 1 回の読み取りで拒否する](https://github.com/getAlby/lightning-browser-extension/pull/3644)ようにするものだ。これによって、拒否エントリを削除した際に、Nostr ハンドラーがプロンプトを表示せずに動作できてしまう競合状態が解消される。BTC と Liquid にも同等のブロックエントリの経路はあるが、現時点では到達できない。これはデプロイ済みの修正ではなく、エクスプロイトも確認されていない。

### MintRadar relay write policy {#mintradar-relay-write-policy}

[MintRadar のソース](https://github.com/hroomnik007/MintRadar/commit/6fd6c8185c053e63610d9b4820e1656552885d85)は、プロジェクトの Nostr relay にオペレーター向けの書き込みポリシーを追加する。公開の kind 38172 アナウンスと kind 38000 レビューは、event あたりシリアライズ済み JSON で 16,384 文字までに制限される。投稿数は IPv6 の /64 ごとに 1 時間あたり 120 件までで、圧縮表記の IPv6 プレフィックスは正規形に変換したうえで扱われる。負荷の大きい送信元には 1 時間あたり 3,000 件のソフト上限が適用される。さらに 1 時間あたり 6,000 件の絶対上限があり、これは全送信元を通じて受理された event のみを数える。特権鍵には制限がない。新規接続は 1 分あたり 120 件、バースト 60 件に制限される。これはコードとオペレーターの設定であり、本番環境への展開や、サービス拒否攻撃に対する完全な防御を証明するものではない。

## 新しいプロジェクト {#new-projects}

### bosstro {#bosstro}

[Bosstro](https://github.com/MostroP2P/bosstro/blob/24bfd318f3e0d9d971e82a04daf12d0f035df2ab/README.md) は、Mostro の紛争解決者（solver）向けの新しい Android クライアントである。MVP のソースが公開されており、Mostro の Rust コアの上で Flutter のフロントエンドが動作する。solver は専用の solver 鍵で署名し、ノード鍵で署名することは決してない。ノードは各 solver に、読み取り権限または読み書き権限を付与する。認可された solver は紛争を引き受けることができる。買い手と売り手の間の暗号化されたチャット（画像や PDF を含む）に参加し、買い手への支払いや売り手への返金も行える。鍵は Android Keystore を基盤とするストレージに保存される。ただし、Linux 版と Web 版の開発ビルドにはそうした保護がない。公開されているチェックサムは、公開者が誰であるかを証明するものではない。

### cordn-kmp {#cordn-kmp}

[cordn-kmp](https://github.com/vitorpamplona/cordn-kmp/commit/dcc0508fd818c1b6bc373b2a7d85742a2ec3dc1b) は、Kotlin Multiplatform による新しい Cordn 実装である。Quartz と mls-kmp を基盤とし、JVM、Android、iOS、macOS、Linux に対応する。ヘッドレスの CordnGroupManager は、Nostr 上の MCP コーディネーターを介して、グループの作成、招待、参加、送信、キャッチアップを行う。これは Marmot の relay 配信とは異なるモデルである。永続化はフロントエンドがそれぞれ用意する。README にある ts-mls との相互運用性の主張は、作者によるものである。

このプロジェクトはその後 [1.1.0](https://github.com/vitorpamplona/cordn-kmp/releases/tag/v1.1.0) を公開した。このバージョンはリリース済みの Quartz 2.4.0 に対してビルドされる。そのため、未リリースの Quartz をビルドフラグで有効化したローカルチェックアウトが必要という以前の要件は、タグ付きリリースには当てはまらなくなった。[1.2.0](https://github.com/vitorpamplona/cordn-kmp/releases/tag/v1.2.0) は[公開メソッドの CordnExposure.differsFromMarmot() を削除し](https://github.com/vitorpamplona/cordn-kmp/pull/5)、別のバインディングとの比較はフロントエンドに任せるようにした。マイナーバージョンの番号が付いているものの、これは API の破壊的変更である。ある提案ではこのバージョンを 2.0.0 と呼んでいたが、実際のリリースでは 1.2.0 が使われた。

### emosphere {#emosphere}

[EmoSphere](https://github.com/Vojta01/emosphere/blob/dfabe1862c57493dbfa9b9881d26b30c1c272762/README.md) は Nostr のムードマップで、現在はソースが公開されている。README では、バージョン 0.5.1 について説明している。各デバイスは独自の鍵を生成し、署名済みの kind 1074 event を公開する。この event には、感情とその強度、任意の短いメモ、大まかな位置情報が含まれる。位置情報はユーザーがオフにできる。投稿は、時間を遡って再生できる世界地図と、フォローフィードに表示される。これらのシグナルは公開されており、仮名で発信される。そのため relay は気分と位置情報を読み取ることができ、時間をかけてそれらを鍵と結び付けることもできる。Android 版は鍵をセキュアストレージに保管し、Web 版は localStorage を使用する。

### matrix-appservice-nostr {#matrix-appservice-nostr}

[matrix-appservice-nostr](https://github.com/Haven-Organization/matrix-appservice-nostr/blob/2f46b9cfcd7265db38d6a7a2c13552ab2a2aa4cc/README.md) は、Nostr relay と組み合わせて動作する Matrix アプリケーションサービスのプロトタイプのソースである。Matrix ユーザーは Nostr のアイデンティティを作成またはインポートし、Matrix のルームから投稿、フォロー、返信、リアクション、DM を行える。ブリッジのドメイン上の NIP-05 ハンドルも使える。コンテンツとメディアは Matrix のバックエンドに保存されたままで、relay は保存されたオリジナルから event を再構築する。鍵は、設定されたシークレットを使って AES-GCM で暗号化されるか、NIP-46 を通じてリモートに保持される。ユーザーはオペレーターを信頼する必要がある。また、Matrix の redaction（コンテンツの削除操作）で削除されるのは、ブリッジ側のコピーだけである。

[より新しい 7 件のコミット](https://github.com/Haven-Organization/matrix-appservice-nostr/compare/a23289b2fcb42511066b47f1839e52a0184a98fa...b0cd64433ffa0ab6026635de2901a6e0a2146101)では、[シャドウ Nostr アイデンティティ](https://github.com/Haven-Organization/matrix-appservice-nostr/commit/081ac30dbc8ae56f31ff8cb06f2b70cefb6b2a09)が追加された。ブリッジは、許可された Matrix ユーザーが外部とやり取りすると、このアイデンティティを自動的に作成する。そのプロフィールは Matrix 側のプロフィールを反映したものになる。完全なプロフィールを作成すると、既存のアカウントがそのままアップグレードされ、同じ鍵が引き継がれる。ブリッジの管理者は、外部のユーザーやホームサーバーに対して、フルアクセスまたはシャドウアクセスを付与できる。ルーム単位の受動的な返信、リアクション、投票のアクセスを付与することもできる。特定ユーザーに対する付与や禁止はホームサーバーのルールより優先され、ホームサーバーのルールはルームのルールより優先される。フル権限があればプロフィールを作成できるが、プロフィールが自動的に公開されるわけではない。アクセスを取り消しても、鍵、履歴、ルームは保持される。ただし、許可されなくなった場所への外部投稿は停止される。インポートされたアイデンティティが、Matrix から反映したプロフィールで上書きされることはない。これらのチェックにはコードとテストがあるものの、ランタイムでの相互運用性やセキュリティは検証されていない。オペレーターによる鍵の扱いを信頼する必要があることにも変わりはない。ステッカーは画像として送信されるようになった。

### nostr-scrutiny {#nostr-scrutiny}

[Nostr Scrutiny](https://github.com/rzazo24/nostr-scrutiny/blob/2f2c38aa67eb7db72113bcf1ba00c55e99bc7e2e/README.md) は、Amethyst、Damus、Nostrich、Primal、Quill の5つの Nostr クライアントを比較した、10月24日付のソースとファクトシートを公開している。シートごとに、クライアントのアプリストアにおけるプライバシー表示と公開コードを取り上げ、ブラウザでの初回訪問時に観測されたネットワークリクエストもあわせて記載している。サイトは静的なプレーン HTML で構築されており、ファーストパーティのトラッキングはないとしている。これらのシートは日付付きの事実の一覧にすぎず、セキュリティ認証でも暗号監査でもない。なお、作者は Quill の開発も手がけており、この利益相反は開示されている。

### v2 {#v2}

[Solid Chat v2](https://github.com/solid-chat/v2/blob/da8b577a98167235f4452cbc97ca5fdb918b5cea/README.md) は新たに公開されたクライアントのソースだ。1つの did:nostr 鍵を使い、NIP-98 HTTP 認証で Solid pod のルームに書き込むほか、NIP-17 の gift wrap された DM を送信する。署名には NIP-07、NIP-46、ローカルの nsec のいずれかを使え、NIP-44 暗号化と kind 1059 のラップを用いる。ルームは平文で、各 pod の ACL だけが保護の手段となる。暗号化された DM のメディアは Blossom にアップロードされ、プロフィールの検索は nostr.social のディレクトリに送られる。ローカルの nsec は localStorage に保存されるので、外部署名者を使うほうが安全だ。

### witchat {#witchat}

[Witchat](https://github.com/BarefootJoey/witchat/blob/905f17d322752554e077a5a0e774555c38417e50/README.md) は、Windows と Linux 向けの非公式 bitchat クライアントのソースだ。近くの Bluetooth メッシュ上でチャットし、相互にお気に入り登録したユーザー同士では Nostr の gift wrap にフォールバックする。Nostr 上の公開 geohash チャンネルにも参加でき、メッセージには kind 20000 の event を、プレゼンスには kind 20001 を使う。bitchat のトランスポートとの相互運用性は作者が主張しているもので、Windows バイナリには署名がない。Nostr の relay からは IP アドレスとチャンネルのメタデータが見える。近隣へのブロードキャストは、現時点では Bluetooth 経由でしか送られない。

### wn-notify {#wn-notify}

[wn-notify](https://github.com/jooray/wn-notify/blob/ba21270edace90c0d6dde7fde7c3b1e3fb5c6201/README.md) は、標準ライブラリだけで書かれた非公式の Python CLI だ。marmot.agent-control.v2 Unix ソケット経由でローカルの wn-agent を通し、White Noise グループにメッセージやファイルを送信する。鍵、MLS 状態、relay はコネクタ側が保持する。CLI は final_sent とメッセージ ID を確認する。結果が不明なときは unknown として非ゼロで終了し、手動で再試行できるよう冪等性キーを残す。CLI が自分で再試行することは一切ないからだ。確認応答で確かめられるのは relay への公開であり、誰かがメッセージを読んだことまでは確かめられない。テストされているのは wn-agent 0.13.0 だけだ。

### xmradar {#xmradar}

[XMRadar](https://github.com/KYC-rip/xmradar/blob/537309555c511e2f5f257fe7e471b0ff2c91ac4f/README.md) は、Web の投稿や X の記事を Nostr にコピーするブラウザ拡張機能だ。公開はすべて、外部の NIP-07 署名者を通じて承認される。[リリース 0.2.0](https://github.com/KYC-rip/xmradar/releases/tag/v0.2.0) では、Nostr アイデンティティを持つ作者に X 上で Monero のチップを送れるようになった。

[実装](https://github.com/KYC-rip/xmradar/commit/213d4b1a6604fe07af4c1991a1c8159a7bcc4abc)では、チップを送ったとユーザーが申告し、さらに確認操作をした後でなければ kind 9042 のレシートは公開されない。このレシートによって、両当事者の npub、金額、アドレスが公開される。トランザクション ID、トランザクションキー、支払い証明は含まれない。金額にはランダムな少額の piconero が加えられており、これを手がかりに受取人のウォレットが支払いを照合し、kind 9044 の確認を公開できる。この確認は受取人が署名したもので、独立したオンチェーンの証明ではない。インターフェース上では、受取人が確認したチップと未確認の申告が区別される。ユーザー自身が送ったチップは30分間保留のままになる。未確認の申告は支払者ごとに1回だけ集計され、その額は現在のアドレスに対する最小のレシートの金額となる。こうした申告は偽造できる。合計は投稿単位ではなく作者単位で保持される。[NIP-A3](/ja/topics/nip-a3/) と [NIP-39](/ja/topics/nip-39/) の X 証明によるアドレス探索は、デフォルトでは無効だ。有効にすると、ユーザーがどのアイデンティティを閲覧しているかが relay と X に知られる。

### agent-inbox {#agent-inbox}

[agent-inbox](https://github.com/ec175/agent-inbox/commit/88fa9da299c3013a0c6a2c88abf0223945229bfa) は、AI エージェント同士が Nostr 上で短いハンドルを使って連絡を取り合えるようにする新しいツールだ。単一の Python ファイルで構成され、NIP-44 v2 で暗号化した標準的な NIP-17 gift wrap を送信できる。公開掲示板への投稿にも対応し、公式テストベクターから作ったフィクスチャも同梱している。ハンドルは公開鍵の末尾を切り出したものにすぎず、認証されたアイデンティティではない。README は、純粋な Python で実装された暗号処理が定数時間ではないと警告しており、私たちはこれを監査していない。エージェントの npub には、どの NIP-17 クライアントからでも引き続きメッセージを送れる。

### CarryChat {#carrychat}

[CarryChat](https://github.com/kemal-arslan/carrychat/commit/64437892165b41070d93acb9b6815dc97168b5a1) は新しいストア・アンド・フォワード型のメッセンジャーで、サイズに上限のあるメッセージバンドルを、そのとき使える経路で運ぶ。インターネット側のトランスポートには Nostr を使い、オフラインの場面は Bluetooth LE や単純なファイル交換といったローカルリンクで補う。ソースには Nostr トランスポートとそのテストが含まれている。README はこれを初期の 0.2 リリースと位置付けており、物理ハードウェアでの LoRa のフィールドテストはまだ終わっていないとしている。私たちは実機ではテストしていない。

[311f176](https://github.com/kemal-arslan/carrychat/commit/311f1765e72079c7b70cf8d1c55865dc781cc2ad) までの[13件の新しいコミット](https://github.com/kemal-arslan/carrychat/compare/64437892165b41070d93acb9b6815dc97168b5a1...311f1765e72079c7b70cf8d1c55865dc781cc2ad)によって、ロードマップ上のプレースホルダーが実際に動くソースに置き換えられた。対象は Wi-Fi Direct、MeshCore 無線アダプター、Reticulum リンク、NFC 連絡先カード、音声トランスポートで、Kotlin、Rust、UI のコードが含まれる。音声経由の通信では、受信側が連絡先カードの署名を検証し、通常のメッセージフレームは受け入れるが、ファイルチャンクは拒否する。NFC で交換するのは連絡先カードだけで、メッセージはやり取りしない。これらは以前の 0.2.0 リリースの後に進められたソース開発であり、新たに検証されたバイナリではない。README によると、MeshCore と LoRa、Reticulum、Wi-Fi Direct、NFC は、いずれもフィールドテストや2台のスマートフォンを使ったテストがまだ済んでいない。今回の変更は、ハードウェア互換性、匿名性、セキュリティのいずれについても何も主張していない。高周波の音声はハードウェアに左右されるため、どの環境でも聞こえないとは限らない。Nostr は今後も、ローカルリンクと並ぶインターネット relay トランスポートの1つという位置付けだ。

### Cosign and Marble {#cosign-and-marble}

[Cosign](https://github.com/sybenx/cosign/commit/c42da802f4d526c5c3c2b08593fcba267f3097c9) は、Nostr の署名鍵を FROST の閾値シェアに分割する新しいプロトコル兼ライブラリで、現在はベータ版だ。ユーザーのデバイスはサーバーと共同で署名できるが、サーバー単独では署名できない。紙のバックアップシェアは、README に記載されたリカバリーとシェア更新のフローを支える。ただし、これらのフローのセキュリティは検証されていない。Android とブラウザ向けのクライアント [Marble](https://github.com/sybenx/marble/commit/d5b50d760c6d4f093120d1d955918430d8360bf6) は、フィードと署名に Cosign を使っている。基盤の FROST ライブラリは監査を受けているが、Cosign 独自のプロトコルについては独立したレビューが一度も行われていない。

[新しいソース](https://github.com/sybenx/marble/commit/ebd110f907d3569a8a9b3e385394c5a55b5582ec)では、Marble のブラウザクライアントが未送信のノートをサインイン中のアカウントに紐付けるようになった。公開の前には、別のタブやリモートセッションによってサインインが終了していないかを確認する。サインアウト済みのクライアントからリクエストが来た場合は Signed out と表示される。[インスタント検索](https://github.com/sybenx/marble/commit/029d8b0f918a9783910aef15f6fe1f160d9c6707)が問い合わせる先は Ditto と relay であり、一般の Web は対象外だ。特定の作者の投稿を検索するときは、relay に問い合わせる前に、すでに読み込まれた投稿を調べる。スパムと思われるものは、展開できる通知の下に折りたたまれる。Not Spam による上書きが有効なのは、そのブラウザ内の、その作者に対してだけだ。これらの検索補助機能があるからといって、セキュリティレビューが行われた証拠にはならない。

[Cosign 0.12.7](https://github.com/sybenx/cosign/releases/tag/v0.12.7) では、メンバーリストのマージをサーバーからしか受け付けないようにした。これにより、紙のバックアップシェアが別のロールに昇格されることを防ぐ。エポック同期の後、古い状態のサーバーには遅れていることを示すマークが付く。無効な部分結果は拒否され、自動修復は引き続き無効のままだ。復号の部分結果には Chaum-Pedersen 証明が付くようになり、部分結果を結合する前にこの証明が検証される。古いクライアントはこの証明を無視する。Marble の Android 部分は次のビルドで対応する予定だ。セキュリティに関するこれらの説明はリリース作者によるもので、私たちは暗号処理を監査していない。

[0.12.7 タグの後にコミットされた Android NIP-55 のソース](https://github.com/sybenx/cosign/commit/e53941f699e9e77ed430015e416daa723c95204f)では、初回接続時の競合状態が修正された。これは、サーバーの許可がまだ relay 経由で届く途中に起きるものだ。公開鍵の照会にはすぐ応答するようになった。署名と復号は UI スレッドの外で待機する。再試行は1回だけで、新たに許可された接続が取り消し済みの応答を受けたときに限って行われる。さらに、到達できないサーバーと、応答したうえで拒否したサーバーをコードで区別するようになった。この後から入ったソース修正が、0.12.7 タグや現行の Marble バイナリに含まれていることは確認されていない。

### Dream Nests {#dream-nests}

[Dream Nests](https://github.com/2three1y/dreamnests/commit/0edc7af86c326452a020ba0b7124c55f5a0413b5) は、ライブ中の Nostr 音声ルームを一覧できる新しい読み取り専用のディレクトリだ。Nests のルームとライブアクティビティの event を、それぞれのチャットとあわせて集約する。この Web アプリはスクリーンリーダー向けに見出しと polite なライブリージョンでの通知を使い、短いイヤコンを音による合図として鳴らす。公開 HLS ストリームは聴取専用で再生する。Nests のルームは Nests で開き、Corny Chat と HiveTalk のルームはそれぞれのサイトで開く。そのため、発言はそれらのアプリの中で行うことになる。マイクのインジケーターはプレゼンスのメタデータに基づいて表示されるもので、実際に音声アクティビティを検出しているわけではない。実機でのアクセシビリティテストは、私たちは行っていない。リポジトリには、公開中のライブ URL が記載されている。

### fips-pub-pki {#fips-pub-pki}

[fips-pub-pki](https://github.com/fr34aky/fips-pub-pki/commit/bd0ea8a16a24eb14d92563cd8d470afad172c83a) は、署名付き Nostr 証明書のための新しいソースだ。ドメインがサブ発行者に権限を委任でき、パス検証はオフラインで行える。トラストアンカーは姉妹プロジェクトの fips-pub-domains から提供される。fips-pub-domains は、DNSSEC による主張にピンとウィットネスを組み合わせている。検証器が DNS に問い合わせることは一切ない。失効の仕組みは有効期限と明示的なマーカーによるもので、relay から event を削除する方式ではない。README によると、公開ドメインとスマートフォンを使ったライブのメッシュテストはまだ終わっていない。NIP の提出も kind の登録もされていないため、これは実験段階のものであり、TLS の代替ではない。

### Magnetar {#magnetar}

[Magnetar](https://github.com/awake-devel/magnetar/commit/b519486d6ed3a1e6f41c4e7faa5c587e9362caf1) は、[NIP-35](/ja/topics/nip-35/) の torrent event を対象とした新しい検索スタックだ。クローラーと検索バックエンドに、ローカルの SQLite キャッシュを持つ Android アプリを組み合わせている。フォロー関係から公開者の信頼度を算出し、スウォームが生きているかどうかも確認する。最初の 0.1 プレリリースには、クローラーのコードと、Android とサーバーそれぞれのテストが含まれている。作者による検証は自動テストとエミュレーターだけで、実際のスマートフォンでは試していない。フォローに基づく信頼で torrent が合法になったり安全になったりするわけではない。また、このバックエンドは権威あるインデックスでもない。

### Magnitude Relay {#magnitude-relay}

[Magnitude Relay](https://github.com/VectorPrivacy/magnitude-relay/commit/92f2440d96a3bf3a6c86691b146ebd6fef7b9f10) は VectorPrivacy による新しい Rust 製の Nostr relay だ。Vector の gift wrap された DM と Concord のトラフィックに合わせて調整されており、NIP-77 同期とタイピングインジケーターに対応する。運営者によると、既存の2つの Vector エンドポイントで strfry から置き換えたという。リポジトリには敵対的テストとベンチマーク用のハーネスが含まれている。ただし、公開されている速度の数値は作者自身が計測したもので、第三者による再現は行われていない。

その後、運営者向けの [Docker と Compose によるパッケージング](https://github.com/VectorPrivacy/magnitude-relay/pull/1)がマージされた。非特権ユーザーで動作し、データボリューム、ローカル限定のバインド、ヘルスチェックを備える。プルリクエストに記載された本番環境とインポートに関する所見は作者によるもので、arm64 ではテストされていない。パッケージングが整っただけでは、プロトコルに準拠していることの裏付けにはならない。

[新しいソース](https://github.com/VectorPrivacy/magnitude-relay/commit/af1b354c5f465d4bf7772ef8fa8f0eaf35a7aabe)では、IP ごとの新規接続にデフォルトで制限がかかる。最初にバースト300まで許可し、その後は毎分60に絞られる。制限値を0にすると制限は無効になり、ループバックは制限の対象外となる。プロキシが付与する実 IP ヘッダーは、localhost から来た場合にのみ信頼される。拒否された接続には、WebSocket が開く前に HTTP 429 が返る。公開 relay での拒否は集計値としてしか報告されず、IP ごとの詳細は管理用ソケットからしか確認できない。NIP-77 の一括同期では、エフェメラル event と、600秒以内に期限が切れる event が除外される。一方、ライブ配信では寿命の短い event も引き続き届けられる。信頼済みリンクが変わったとき、relay は冗長な gift wrap の可視性プローブを省くが、gift wrap 自体の同期は続ける。いずれもソース上の変更であり、本番環境で計測したベンチマークはない。

### nostr_doctor {#nostr_doctor}

[nostr_doctor](https://github.com/nogringo/nostr-doctor/commit/348efc1dd32c213badf34c6ba529707b952bd658) は、アカウントのデータをクライアントが発見できるかどうかを確認する新しい Dart ライブラリで、CLI と Flutter のフロントエンドも用意されている。最初にプロフィールのメタデータと NIP-65 の relay リストを調べる。続いてプライベート DM 用の relay と下書き、さらに Blossom サーバーと nutzap の設定も確認する。relay リストが発見できるかどうかは、replaceable なリストをプローブして確かめる。私たちはこの診断ツールをソースとしてレビューしたが、アプリのリリースは検証していない。結果に反映されるのは問い合わせた relay の状況だけで、ネットワーク全体での可用性を示すものではない。

### nostr-indexer-relay {#nostr-indexer-relay}

[nostr-indexer-relay](https://github.com/nogringo/nostr-indexer-relay/commit/f75e4415f24f629935f7e6b3567232e2c6dbf80a) は、NIP-65 の relay リストだけを保存する新しい Go 製の relay だ。クローラーがそれらのリストに記載された relay を見つけ出し、NIP-77 に対応しているかをプローブする。稼働中の他のインデクサーとは negentropy で同期する。公開の検索ページと管理インターフェースを備え、自身を初期段階のプロジェクトと説明している。relay リストに特化したインデックスであり、Nostr のアーカイブでも汎用のコンテンツ relay でもない。

### nostr2gh {#nostr2gh}

[nostr2gh](https://github.com/kravens/nostr2gh/commit/ec189b10d48d0f9f0c0e8a464c930263b2275c95) は、NIP-34 のパッチ event とプルリクエスト event を、それらの更新も含めて、ホワイトリストに登録されたリレイヤー経由で Nostr から GitHub へ届ける新しいブリッジだ。コントリビューターはフェッチ可能な場所にブランチをプッシュし、Nostr event に署名する。すると、問題なく使える GitHub アカウントを持つ友人が、本人に代わって PR を開く。GitHub にアクセスできないコントリビューターの助けにはなるが、BAN を自動で回避するものではない。信頼できないパッチを自動で実行してよいという許可を与えるものでもない。

### Relay Radio {#relay-radio}

[Relay Radio](https://github.com/2three1y/relayradio/commit/3993e7226de616ac9a2768a5d50a271535449806) は、ライブの Nostr フィードをイヤコンとブラウザのテキスト読み上げで音に変える新しい読み取り専用の Web アプリだ。スクリーンリーダー利用者向けに、polite なライブリージョンもオプションで用意されている。リスナーは、厳選されたグローバル局と、自分がフォローしている人々から構成される局のどちらかを選べる。対象はノート、リプライ、リポスト、リアクション、zap だ。リスナーに代わって投稿したり支払ったりすることは一切ない。コンテンツのフィルタリングはベストエフォートなので、読み上げられる内容がすべて安全だとは保証できない。

### Hibiki {#hibiki}

[Hibiki](https://github.com/ChiefmonkeyArt/torii-hibiki/commit/3820208896df7ba28a06a2cfa38fefc1a753f9d1)はTorii向けのスタンドアロンなフィードnappletで、ソースではバージョン0.2.1を最初に動作するフィードとしています。公開投稿とメディアの取得はノードが担い、ユーザーの好みに基づくランキングはブラウザ内で実行されます。フィードは直接のネットワークアクセスを持たないサンドボックス化されたiframe内で動作し、署名付きのスパム評価はあくまで助言として扱います。プライバシー境界について、私たちは独自に検証していません。

バージョン0.2.6までのマージ済みソースでは[インライン返信と抽出型のニュース要約](https://github.com/ChiefmonkeyArt/torii-hibiki/pull/8)が追加され、いいねによって投稿の順位が並べ替えられることはなくなりました。タグ付きリリースはまだ確認されていません。Watchプレーヤーのプレビュー対応によって[プレビューフレーム](https://github.com/ChiefmonkeyArt/torii-hibiki/pull/9)が加わりました。[Zap](https://github.com/ChiefmonkeyArt/torii-hibiki/pull/11)はプロフィールページとともに導入されます。ノードは各インボイスの金額とdescription hashを検査します。支払いのたびにオーナーの確認が必要で、支払者はWebLNまたはQRコードを使います。ノードは資金も鍵も保持しません。Primalアドレスのインボイスにはdescription hashがないため、[追加の修正](https://github.com/ChiefmonkeyArt/torii-hibiki/pull/12)では金額が完全に一致する場合に限りそれらを受け入れます。こうしたインボイスにはbound:falseのフラグが付き、ウォレットが確認しない可能性があるとオーナーに警告されます。この措置はインボイスとzapリクエストの結びつきを弱めるものであり、これらを有効な[NIP-57](/ja/topics/nip-57/)の確認にするものではありません。ウォレットの5xxエラーとタイムアウトは1回だけ再試行され、LNURLの理由が表示されます。実際のウォレットでエンドツーエンドのzapに成功したという報告は、作者からまだ出ていません。

### wax {#wax}

[wax](https://github.com/modus-lisp/wax/commit/0b48716cfce52be990e0ef43fcecb2c5fa899b44)は、BIP-39シードからロール鍵を導出する新しいCommon Lisp製の署名器です。すべてのリクエストをポリシーガードに通し、承認コールバックまたは許可リストが認めない限りデフォルトで拒否します。呼び出し元ごとのエンベロープシーケンスがリプレイを防ぎます。メソッド名はNIP-46に似ていますが、コアはネットワークトランスポートを提供しません。この署名器のセキュリティ監査は行っていません。

### WhatZaps {#whatzaps}

[WhatZaps](https://github.com/nostr-wot/whatsapp-zaps/commit/ab86552a5178c9c1b55dd917084f4e3cf223ea89)は、Nostr WoT拡張機能のWebLNサポートを通じて、WhatsAppの連絡先にLightningで支払いができる新しいブラウザ拡張機能です。連絡先をNostrプロフィールに対応付けてその支払いアドレスを確認し、支払い前には必ず明示的な確認を求めます。/zapコマンドがチャットメッセージとして送信されることはなく、リアクションやボタン経由で支払う場合も何も投稿されません。これらはIDの照会にNostrを使うLightning支払いであり、署名付きの[NIP-57](/ja/topics/nip-57/) zapレシートではありません。ブラウザでのメッセージ照合はテストしていません。

### Agoraの暗号化投票 {#agora-encrypted-polls}

[Agora](https://github.com/maxgfr/agora/commit/85d83f49dcb3ed138c4118bced60d1a2f48fb01b)は、暗号化されたグループ投票のためのブラウザプロトタイプです。メンバーによる保証（vouching）とブラインド投票チケットを組み合わせ、通信をNostrのrelayとWebRTCで運びます。[README](https://github.com/maxgfr/agora/blob/85d83f49dcb3ed138c4118bced60d1a2f48fb01b/README.md)ではこの設計を「実在する1人につき1票」と位置づけていますが、それはチケットを偽造できるチケット発行者を信頼することと、社会的信頼の一形態である保証に依存しています。この設計に強要耐性はありません。relayからはタイミングとIPアドレスが見え、結果はクライアントがどのeventを受信するかに左右されます。なお、このプロジェクトは以前からあるghobs91/Agoraチャットプロジェクトとは無関係です。

### Cinderous SDK {#cinderous-sdk}

[Cinderous SDK](https://github.com/VaalRL/cinderous-sdk/commit/59314a6c2dffb85224c6262348a707f6acc4eb83) v0.83.0は新しいソースプロトタイプです。デバイスごとに個別の鍵を割り当て、Gitのような履歴付きでドキュメントをNostrとWebRTC上で同期し、必要に応じてrelayにフォールバックします。relayの選択とデプロイは呼び出し側が行い、SDKにデフォルトの公開relayは同梱されていません。暗号化には実験的なCinderEK方式とDouble Ratchetを使っており、外部監査は受けていません。ハイブリッド鍵交換によってsecp256k1署名が耐量子になるわけではなく、[README](https://github.com/VaalRL/cinderous-sdk/blob/59314a6c2dffb85224c6262348a707f6acc4eb83/README.md)ではこのSDKを本番利用に対応していないものとしています。

### evil-napplets {#evil-napplets}

[evil-napplets](https://github.com/napplet/evil/commit/7311b6298e7b64e595d8b566f226a26cad1cfee5)に、攻撃ラダーのレベル02から08が追加されました。対象は、ドラフトのNIP-5D opaque-originモデルの下でnappletを実行するホストのテストです。悪意あるnappletが機能とブリッジの境界を探り、ホストが何を許可したかを報告します。デフォルトはデモンストレーションモードで、アクティブモードは明示的に有効化する必要があります。アクティブテストは、テスト実施者が調査を許可されているホストに対してのみ実行すべきです。このスイートはレッドチーム用のフィクスチャなので、合格したホストが安全であると示されたことにはなりません。別のアプリアーキテクチャを対象とするevil-nappsとは別のプロジェクトです。

### evil-napps {#evil-napps}

[evil-napps](https://github.com/sandwichfarm/evil-napps/commit/f0746e4cb958bbcb01806e2354809472b63a943a)は、NAPPランチャーの権限境界を探る新しいソーススイートです。ランチャーのブリッジと、アプリに公開されるNIP-07署名器を対象とします。SharedDBストレージも範囲に含まれます。NAPPバンドルはメタデータとindexファイルを組み合わせたもので、NIP-5D nappletで使われる単一HTMLアーティファクトとは形式が異なります。[README](https://github.com/sandwichfarm/evil-napps/blob/f0746e4cb958bbcb01806e2354809472b63a943a/README.md)によると、このスイートはデフォルトでデモンストレーションモードで動作し、アクティブな調査は明示的に要求された場合にのみ実行します。テストとハーネスは、ランチャーを認証するものではありません。

### Feedstr {#feedstr}

[Feedstr](https://github.com/0n4t3/Feedstr/commit/3fe44eca46106488585d0d1554509f5d3e498f39)は、フィード、既読状態、お気に入りをNostr上で暗号化して同期する新しいRust製RSSリーダーです。同期はフィードごとにオフにできます。OPMLのインポートとエクスポートに対応し、[NIP-23](/ja/topics/nip-23/)の長文記事も扱えます。リポジトリにはコア、Android、Web、Flatpakのソースツリーがあります。[README](https://github.com/0n4t3/Feedstr/blob/3fe44eca46106488585d0d1554509f5d3e498f39/README.md)によれば、このソフトウェアはほとんどテストされておらず使用は推奨されないとのことで、インストール方法と使い方の説明は近日公開予定とされています。

### NKIP入金レシートツールキット {#nkip-deposit-receipt-toolkit}

[KYC-rip/nkip-0001](https://github.com/KYC-rip/nkip-0001/commit/6d6a9489db72626794e7e2b88a18846ea19a10e2)は、XBToshiがメンテナンスする、NKIP-0001入金レシート向けの新しいTypeScriptツールキットです。NKIP-0001はアプリケーションのレシート形式であり、採用済みのNostr NIPではありません。このツールキットは、Ed25519で署名された入金レシート、ソルト付きコミットメント、Nostrのwitness event、そしてNIP-44暗号化によるソルト復元を扱います。保護が機能するかどうかは、witnessが観測されるまでアプリケーションが入金アドレスを提示しないことにかかっています。SDKは注文を制限せず、払い出しも保証しません。詳細は[README](https://github.com/KYC-rip/nkip-0001/blob/6d6a9489db72626794e7e2b88a18846ea19a10e2/README.md)にあります。

### nostr-parse {#nostr-parse}

[nostr-parse](https://github.com/VectorPrivacy/nostr-parse/commit/703f07cd7177b2b52977aa6deaa6f11a696d4914)は、VectorPrivacyによる署名付きNostr event向けの新しいRust製パーサーです。厳密な7フィールドのevent形状を強制し、非負整数を要求します。さらにkindをu16の範囲に制限し、hexフィールドを検査し、エスケープされた文字列を検証します。エラーはオフセット付きで報告されます。呼び出し側はコンパクトな所有型アロケーションか、入力への借用スパンを生成できます。また、`parse_unsigned`は署名なしのNIP-59 rumorを受け付けます。パースの際にevent IDの再計算もSchnorr署名の検証も行わないため、これらのチェックは引き続き呼び出し側が自分で実行する必要があります。

### cl-deposits {#cl-deposits}

[cl-deposits](https://github.com/modus-lisp/cl-deposits/commit/3d74564de6be0d25efec3ce6ad76a4fc691dc676)は、Bitcoin Depositsの新しいCommon Lisp実装です。この設計では、オペレーターがTaprootの準備金に裏付けられたハッシュチェーン台帳をNostr上で運用し、台帳は署名付きで、クォーラムによる共同署名も受けます。リポジトリにはソースと、検査テスト付きのdevnetが含まれています。READMEと[ROADMAP](https://github.com/modus-lisp/cl-deposits/blob/3d74564de6be0d25efec3ce6ad76a4fc691dc676/ROADMAP.md)によると、作者は参照フィクスチャを再生し、signetのdevnetを動かし、deposits-rustとの相互運用性を双方向でテストしました。作者はLightningの受け取り経路が動作することも報告しており、次の作業として支払いのInvoiceLockとFulfillを挙げています。ユーザーは、オペレーター、共同署名クォーラム、そして準備金に関する前提に依存することになります。

### Streets {#streets}

タイムライン、通知、検索を並べて表示するカラム型のNostr Webクライアント[Streets](https://streets.eyemono.moe)が、デフォルトのリアクション絵文字をアカウントのNIP-78デッキドキュメント（kind 30078）に保存する[変更](https://github.com/eyemono-moe/streets/commit/6b31a7c97cc6801cf392ab61c4de4af7d3286233)をマージしました。再ログインした後や別のデバイスで、もう一度選び直す必要はなくなります。以前は、この選択はデバイスのlocalStorageにしか保存されていませんでした。デッキドキュメントはNIP-44で暗号化されるため、デバイス間で同期するには暗号化に対応した拡張機能または署名器でログインする必要があります。それ以外のログイン方式では、設定はデバイス上に保持されます。アカウントに保存済みのリアクションがなければ既存のデバイスの値が使われるので、設定がハートにリセットされることはありません。保存された値が無効な場合は、デッキの残りを破棄せずにその値だけが捨てられます。この変更はソースに入っていますが、1.22.0のリリースノートはまだ下書きの段階です。

### Labradorite {#labradorite}

Labradoriteは、ペアリングしたLinuxコンピューター上のコーディングエージェントセッションを操作するAndroidアプリで、[0.1.0](https://njump.me/nevent1qqsdqkdh6z32nysms5exwtw76n0vp3h2zzxtchh4sfcrywe5tz5gd0czyp6hjpmdntls5n8aa7n7ypzlyjrv0ewch33ml3452wtjx0smhl93jqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkylssg9)と[0.2.0](https://njump.me/nevent1qqs9pra62cxllt9uggf38lqxsmv7np34f4jjfyr6zath3d4ffn0hlxszyp6hjpmdntls5n8aa7n7ypzlyjrv0ewch33ml3452wtjx0smhl93jqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkn9vmwk)を公開しました。スマートフォンは操作インターフェースにすぎません。エージェントを実行するのはコンピューター上のデーモンで、通常のNostr relayを介してMarmot MLSメッセージをやり取りし、セッションごとに1つのグループを使います。受け付けるのは許可リストに載ったnpubだけで、このリストはデフォルトでは空です（[ソース](https://gitworkshop.dev/npub1w4uswmv6lu9yel005l3qgheysmr7tk9uvwluddznju3nuxalevvs2d0jr5/relay.ngit.dev/nostr-agents)）。バージョン0.1.0は承認済みのセッションを開始または再開し、テキスト、ツール呼び出し、差分をストリーミングし、承認や質問を処理します。Gitの操作と読み取り専用のファイル閲覧も提供します。バージョン0.2.0では、フォローアップを個別のターンとしてキューに入れ、スマートフォンからキャンセルできるようになりました。キューに入った作業はデーモンの再起動後も保持され、再接続後には見逃した履歴が再生されます。これらは公開者の主張であり、そのセキュリティについて私たちは独自に監査していません。

### Nomisma {#nomisma}

Nomismaは[プロトタイプのベータ版](https://github.com/Lwb89dev/nomisma/tree/46ed9b3190ab93d1acea511677c6d4d18de931b5)段階にあるAndroid向けの共有経費台帳で、2人の参加者をNostrのプライベートメッセージでペアリングします。追跡するのは残高だけで、お金を移動したり精算したりはしません。[バージョン0.1.3](https://njump.me/nevent1qqszafzumepzzcw68g652k3m47v473y4jac9mhan5fpk344qd0w0m4szypjgcr6nqtr47wpc9fxjepdys2uj0nrpk2pg5pu5udkxe3ukm6r2vqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetknw8e4p)では、ペアリング済みデバイスが自動的に再接続し、永続化された変更が間隔を延ばしながら再試行されるようになり、NIP-42のrelay認証も追加されました。欠落した操作の再送も行います。2台のデバイスがエントリ、支払者、分担のSHA-256フィンガープリントを比較するのは、作者ごとのベクトルクロックが一致したときだけです。デフォルトのrelayが変わったため、両方のデバイスに0.1.3と一致するrelay設定が必要です。チェックポイントは15分のNIP-40有効期限付きでgift wrapされます。これはrelayに削除を求めるものですが、消去を保証するものではありません。リリースノートはネイティブライブラリの読み込み、Schnorrの引数順序、NIP-44の鍵導出に関する修正を報告していますが、私たちはそのセキュリティを独自に監査していません。ユーザーの署名はAmberを通じて行われる一方、デバイス上には一時鍵も存在します。APK署名証明書について配布ノートの記述が食い違っているため、ここではアップグレード互換性を確認済みとしていません。

### Onyx {#onyx}

[Onyx](https://gitworkshop.dev/npub1vx40p5mkcwyrg2gnthf343y39tf0zqxl56ajvql2m9q3rxremynsfp37lu/relay.ngit.dev/onyx)は、ソースとして入手できる非公開日記のプロトタイプであり、検証済みのリリースではありません。日付付きのMarkdownファイルを信頼できる情報源としてデバイス上に保持し、暗号化されたkind 30078 eventとしてrelayにバックアップします。ソルト付きのd-tagを使うことで、エントリの日付が直接露出しないようにしています。復元には別途ローカルの暗号鍵が必要なので、ユーザーはそれをバックアップしておかなければなりません。npubだけでは日記を復元できないためです。10月27日のパッチでは、公開前にリクエストフィールドの完全性をチェックするガードが追加されました。署名器が返したeventのkind、content、pubkey、tags、タイムスタンプがリクエストと一致している必要があります。このパッチは、誤った作者からのダウンロードを拒否し、より新しいローカルの編集を保持し、復元時にはデータをアトミックに置き換えます。eventの作者とタイムスタンプは公開されたままです。暗号化コマンドに渡された平文が、ローカルのプロセス検査で一時的に見えてしまう可能性があります。また、エントリを削除してもrelay上のコピーは消去されません。

### Zzub {#zzub}

[Zzub 0.0.41](https://njump.me/nevent1qqs2rzmlu7hwflagzswk3q6e20nrzp6gcq5rgk4uu2a9kcuuzlhmfyszyrts65qfz5ztnyk3swyz9teyt40kkwskhqkez7kt0yjvaas76jkwuqcyqqq82mcprpmhxue69uhhyetvv9uju7npwpehgmmjv5hxgetkfm8t9z)は、Buzzからフォークしたコミュニティクライアントです。公開者の短いノートによると、このバージョンではタイムゾーン対応のカレンダーRSVP、プロフィールzap、[NIP-58](/ja/topics/nip-58/)バッジの表示、ライブミーティングに参加するハドルボタンが追加されました。エージェント操作には、再起動オプション、予算対象外リストの編集、新しいタスクカードの種類が加わっています。起動時には、キャッシュされたチャンネルが使われるようになりました。

## プロトコルと仕様の動向 {#protocol-and-spec-work}

### NIP-CDはプレーンテキストで呼び出すコマンドを定義 {#nip-cd-defines-commands-invoked-as-plain-text}

当初はCommands、現在はSlash Commandsというタイトルの[NIP-CD仕様](/ja/topics/nip-cd/)が、[10月21日にNIPsリポジトリへマージされました](https://github.com/nostr-protocol/nips/commit/7b5ea85479c0b4efce3c246abefa1dae8f8f91e4)（[提案のレビュー][commands-review]）。エグゼキューターはkind 31992 eventでコマンドを告知し、そこにはトリガー、タイトル、説明、型付きの位置引数、スコープが列挙されます。ユーザーはevent contentの先頭にプレーンテキストとして書くことでコマンドを呼び出し、必要に応じてエグゼキューターのnpubで修飾することもできます。そのため、コマンド固有のtagもクライアント側の対応も必要ありません。修飾なしのトリガーは、複数のエグゼキューターに一致する可能性があります。クライアントはオートコンプリートを提供してもかまいませんが、それを必須にすることはできません。

### Marmotがアカウントごとの複数デバイスを採用 {#marmot-adopts-multiple-devices-per-account}

[Marmot](/ja/topics/marmot/)は、MLSをベースとしたNostr向けの暗号化グループメッセージングプロトコルであり、10月26日に[マルチデバイスのアカウントルールをマージした](https://github.com/marmot-protocol/marmot/commit/be923c9cad997176cc155d5d851d40d28e19cc6b)（[提案レビュー][marmot-devices-review]）。マージされたのは、以前のドラフトから改訂された形である。招待者が1つのCommitで1アカウントに追加できるKeyPackageは最大20個である。各デバイスは生涯変わらないランダムな公開スロットをちょうど1つ保持し、MLS状態や非公開のKeyPackageをコピーすることは決してない。パッケージの有効期間は30日とし、7日ごとに更新すべきとされる。招待者は対象となる各デバイスにそれぞれ個別のWelcomeを送り、アカウントを削除するとそのアカウントのすべてのリーフが削除される。

### Marmotでメンバーが自分のアカウントのリーフを管理可能に {#marmot-lets-members-manage-their-own-accounts-leaves}

Marmotは[同一アカウントのメンバーシップコンポーネントを採用した](https://github.com/marmot-protocol/marmot/pull/443)。`marmot.group.account-devices.v1`（ID 0x800d）というもので、データは一切持たない。グループのネゴシエーションでこのコンポーネントが必須とされている場合、メンバーは管理者権限なしに自分のアカウントに対するAddとRemoveをコミットできる。このコンポーネントの下では、メンバーはコミッター自身のリーフを削除することも、他のアカウントを削除することもできず、そのアカウントの管理者としての地位も変わらない。既存のグループは、このコンポーネントを有効化し、そのサポートに関する不変条件を満たす必要がある。

### Marmotのプッシュトリガーに新規パディングを導入 {#marmot-push-triggers-gain-fresh-padding}

Marmotは10月26日にマージされた変更で、[すべてのプッシュトリガーに新規のパディングを必須とした](https://github.com/marmot-protocol/marmot/pull/445)。各kind 446トリガーには、CSPRNGで新たに生成した1,084バイトのパディングチャンクが少なくとも1つ含まれる。これにより、32チャンクの上限のうち実際の暗号化トークンに使えるのは最大31個となる。新しいパディングがなければ、同一のトークンバイト列によってコンテンツハッシュの重複排除が働き、後続の正当な通知が抑制されてしまう。サーバーはすべてのチャンクをハッシュし、パディングを検出できないことを理由に構造的に有効なトリガーを拒否してはならない。パディングはrelayや観測者からトークン数を隠すが、復号を行う通知サーバーからは引き続き見える。

### Marmotが新メンバー向けのプッシュトークン修復を追加 {#marmot-adds-push-token-repair-for-new-members}

Marmotは10月26日に[新メンバー向けのプッシュトークン修復をマージし](https://github.com/marmot-protocol/marmot/pull/447)、[フォローアップでその最終的な文言が明確化された](https://github.com/marmot-protocol/marmot/blob/e8e09c822ca1a3874d2bd01c1f332d91e70bc97c/features/push-notifications.md)。参加者を追加するCommitの所有者は、有効なkind 448トークンスナップショットとkind 449削除トゥームストーンを送信すべきとされる。kind 447アナウンスにオプションのフィンガープリントセットを含めると、ピアは欠けているレコードだけを送ればよくなる。ランク上位3つのリーフが時間差をつけたタイマーで応答し、アナウンスするリーフごとに24時間のレート制限がかかる。relayで中継された署名付きレコードと保持された削除トゥームストーンにより、所有者がオフラインの間でも欠けたトークン状態が修復される。

### パスキーで保持するNostr鍵の提案 {#proposal-for-passkey-held-nostr-keys}

[パスキーで保持するNostr鍵の提案](https://github.com/nostr-protocol/nips/pull/2519)は、パスキーをNostr鍵とともに使うための既存の仕組みであるNosskeyを土台にしている。タグ付きハンドルによってPRF/HKDFから導出されたアイデンティティと保存された鍵が区別され、暗号化されたkind 31778のrelayレコードがrelying party、作成者、クレデンシャルを結び付ける。メタデータが欠けている場合や不明な場合に、新しいアイデンティティを暗黙のうちに作成してはならない。relying partyのオリジン認可は引き続き適用され、旧来のNosskeyデータには明示的な移行用リーダーが必要である。導出されたアイデンティティは、別途バックアップしない限りパスキーとともに失われる。

### NIP-05識別子のDNS委任の提案 {#proposal-for-dns-delegation-of-nip-05-identifiers}

[NIP-05 DNSベース識別子](/ja/topics/nip-05/)に対する未マージの[DNS委任の提案](https://github.com/nostr-protocol/nips/pull/2527)は、元のHTTPSルックアップが404または410を返した場合にのみ適用されるフォールバックを追加する。その場合、クライアントはHTTPSプロバイダーを指す`_nip05` TXTレコードを読み取る。タイムアウト、TLSやCORSの失敗、リダイレクト、鍵の不一致によってフォールバックが発動することはなく、DNSには鍵が一切保存されない。DNSSECは推奨されるが必須ではない。そのため署名されていないDNSでは、プロバイダーのTLSによって元のドメインの認可を独立して認証することはできない。古いクライアントは委任のみの識別子を解決できない。

### ソフトウェアアプリカタログをNIP-82として提案 {#software-application-catalog-proposed-as-nip-82}

[ソフトウェアアプリケーションカタログの提案](https://github.com/nostr-protocol/nips/pull/2526)は、オープンで未マージのそのプルリクエストにおいて、提案上の番号としてNIP-82を使っている。この番号は割り当ても採用もされていない。提案は、アプリ（32267）、リリース（30063）、アセット（3063）、キュレーション（30267）、証明書所有証明（30509）、カタログrelayリスト（10067）のkindをまとめたものである。アセットはファイルハッシュとともにプラットフォームとランタイムを識別する。Androidのアセットには、署名証明書のハッシュも加わる。証明の署名はパブリッシャーがその証明書を管理していることを示すが、それでも読み手は有効期限と失効を確認しなければならない。

### BIP 321 URIをNIP-A3の支払い先として提案 {#bip-321-uris-proposed-as-nip-a3-payment-targets}

[NIP-A3の支払い先](/ja/topics/nip-a3/)に[bip321支払いタイプを追加する提案](https://github.com/nostr-protocol/nips/pull/2522)は未マージであり、kind 10133 eventが完全な`bitcoin:` URIを静的で再利用可能な支払い指示として持てるようにする。支払い先が再利用されるため、提案では金額と、使い切りのBOLT11 `lightning`請求書パラメータを禁止している。金額は支払者が選び、ウォレットは自身がサポートする支払い方法を選択する。Lightningアドレスへのフォールバックは維持される。

### BIP 321の支払い先を通じて支払うzapの提案 {#proposal-for-zaps-paid-through-bip-321-targets}

[BIP 321の支払い先を通じて支払うzapの提案](https://github.com/nostr-protocol/nips/pull/2521)では、送信者が受信者の再利用可能なNIP-A3 bip321支払い先に対し、Ark（オフチェーンのBitcoinプロトコル）、Lightning、またはオンチェーンで支払い、その後kind 9740のzapを公開する。受領鍵の保持者は、kind 9741で決済を確認する。どちらのkind番号も、まだ仮のものである。支払い参照は[NIP-44バージョン付き暗号化](/ja/topics/nip-44/)を使って、受信者がオプトインした受領鍵宛てに暗号化され、その鍵だけが支払いを確認できる。第三者は支払いの詳細を検証できないため、確認は受信者の署名を信頼することに依存する。この提案は[NIP-57 Lightning zap](/ja/topics/nip-57/)を置き換えるものではない。

### Nostr Wallet ConnectにArk支払いを提案 {#ark-payments-proposed-for-nostr-wallet-connect}

[Nostr Wallet Connect](/ja/topics/nip-47/)（アプリがリモートのウォレットを操作できるようにするNIP-47プロトコル）に対する未マージの[Ark拡張の提案](https://github.com/nostr-wallet-connect/nwc/pull/11)は、既存のBIP 321による支払いと受け取りのサポートにArk指示を、`lookup_payment`にArk支払いレコードを追加するもので、新しいメソッドは追加しない。ウォレットがこの指示を使うのは、アドレスのバージョンとネットワークをサポートし、かつ同じArkサーバーを共有している場合に限られる。そうでなければ、URI内の別の指示を試す。金額はミリサトシの丸めなしの整数サトシでなければならない。また、レコードではサーバーが共同署名した支払いと、受信者が回収済みで使用可能な資金とが区別される。

### BlossomサーバーにArk支払いヘッダーを提案 {#ark-payment-header-proposed-for-blossom-servers}

[Blossom](/ja/topics/blossom/)（HTTPサーバーにメディアblobを保存するためのプロトコル）における[Ark支払いヘッダーの提案](https://github.com/hzrd149/blossom/pull/116)は、BUD-07のHTTP 402 Payment Required応答に`X-Ark`を追加する。ヘッダーには、リクエストごとに新しく生成されたArkアドレスと金額を含むBIP 321 URIが入る。オプションとして、URIには同じ支払いをLightning請求書としても含めることができる。証明として、クライアントは決済後に支払い済みのArkアドレスを付けて再試行する。フォールバックを使ったクライアントは、Lightningのプリイメージを付けて再試行する。HEADリクエストは証明付きで再試行されず、クライアントはGETまたはPUTに進む。

### ノート内の資産言及のためのキャッシュタグ提案 {#cashtag-proposal-for-asset-mentions-in-notes}

[キャッシュタグの提案](https://github.com/nostr-protocol/nips/pull/2528)は、`$`の後に2〜6文字のASCII英字が続くもののオプションのトークン化を定義しており、コード、URL、Nostr参照は対象外となる。ティッカーだけでは資産を一意に識別できないため、単一のcashtag tagで表示モードを設定し、作成者が選んだ資産IDを付けられるようになっている。読み手はシンボルがチェーンとアドレスに一致するかを確認し、不一致があればラベルを付け替えずにフラグを立てる。オプションの`t` tag（`$ticker`の形式）により、標準的なrelay検索が可能になる。

### Napplet gamepad仕様の撤回 {#napplet-gamepad-specification-withdrawn}

Napplet仕様が公開されているNAPsリポジトリは、10月27日に[gamepad仕様の削除をマージした](https://github.com/napplet/naps/pull/129)。この変更によりNAP-GAMEPAD.mdが削除され、以前の採用が取り消される。現在採用されているgamepad NAPは存在しない。

### Cyberspaceの高さtagがグループtagとの衝突を回避 {#cyberspace-height-tags-avoid-group-tag-collisions}

Nostr上に構築された空間プロトコルであるCyberspaceは、DECKと呼ばれる独自の仕様をいくつかマージした。これらはプロジェクトの仕様であり、公式のNIPではない。仕様では現在、[bagとchatの高さtagが`h`から`H`に改名されている](https://github.com/arkin0x/cyberspace/pull/73)。小文字のtagはNIP-29のグループtagと衝突し、eventが拒否されたり誤って分類されたりする原因となっていた。読み手が旧来の`h`にフォールバックするのは、`H`がない場合に限られる。これはプロジェクト仕様のみの変更である。NIP-29を修正するものでも、展開済みのクライアントが相互運用できることを証明するものでもない。

### Cyberspaceの隠しオーディオ {#cyberspace-hidden-audio}

[DECK-0007は隠しオーディオを定義している](https://github.com/arkin0x/cyberspace/pull/79)。これは暗号化されたBlossomファイルであり、署名済みのbagまたはchestの内部にある署名なしのrumorから参照される。つまり、隠した人物が、再生可能な、別途署名された公開投稿を通じて特定されることはない。配置ごとに新しい鍵と暗号文が使われるものの、鍵は依然として誰でも共有できる。仕様は、暗号化によって発見者のプライバシーが保証されるとも、そのURLルールがすべてのSSRFを防ぐとも主張しておらず、リーダー側のサポートはまだ進行中である。

### Cyberspaceの公開モデルとアニメーション {#cyberspace-public-models-and-animation}

[アイテムはbobおよびspinアニメーション付きの公開SNOモデルを参照できるようになり](https://github.com/arkin0x/cyberspace/pull/74)、モデルが無効または利用できない場合は従来のレンダリングにフォールバックする。ライブのモデルは変更されたり消えたりする可能性があり、広く採用されているとは主張されていない。

### Cyberspaceのアイテム、チャット、コメントの仕様 {#cyberspace-item-chat-and-comment-specifications}

[オプションのDECK 0004から0006](https://github.com/arkin0x/cyberspace/pull/67)は、アイテム、chest、出品、暗号化されたローカルチャット、封印されたコメントに関する既存のコードを、合成テストベクトルとともに文書化している。いくつかの問題は未解決のままである。bagとchestでは署名が異なり、封印されたコメントは公開tagを通じて親のIDとkindを露出する。保有者は出品を上書きできる。チャットにはリプレイとコンテキストバインディングに関する欠陥があり、chest参照は実装されていない。この文書化によって修正されるセキュリティ問題はなく、展開を意味するものでもない。

### マルチ作成者eventの提案 {#multi-author-events-proposal}

署名付きの長文記事[Multi-Author Nostr Events as a Soft Fork](https://njump.me/nevent1qqszlhx6hpwf0th2mk760n7cxqdknglwshgprpupsk4tj0nkr2n66wgzypzcxhpk7swe0x7gz2vrpuh4myjk9af584h7mht0xz48jjq8xrexuxjg87j)は、IDハッシュが複数の作成者pubkeyを対象とし、各作成者が同じIDに署名するeventを提案している。古いクライアントには、新形式のデータと、ルックアップのヒントとしてのQ tagを運ぶsecp256k1互換のラッパーが見えることになる。ピアは接続ごとに新形式をネゴシエートする想定である。この記事は、将来の鍵を共著者の1人として追加するという、著者が以前に出した耐量子の提案を一般化したものである。これは番号のない提案であり、採用されたNIPではない。共著のnaddrの置き換えとバイナリトランスポートは、未解決の問題として残っている。

### Buzz NIP-AR同期サブスクリプションはライブのヘッドの前に完全なスナップショットを送信 {#buzz-nip-ar-sync-subscriptions-send-a-complete-snapshot-before-live-heads}

Buzzのオープンなプルリクエストが、[NIP-AR](/ja/topics/nip-ar/)のWebSocket同期サブスクリプションを提案している（[#8522](https://github.com/block/buzz/pull/8522)）。relayはREPEATABLE READで読み取った一貫性のあるアーティファクトセットを送信し、そのセットが完全になった時点で初めてEOSEを発行し、その後ライブの現在のヘッドをストリーミングする。ライブのRedis登録は、初回の読み取りより前に行われる。Redisの切断や遅延が起きるとサブスクリプションはCLOSEDで終了し、再同期が必要になる。アクセスの変更、redaction、キューの満杯の場合も同様である。サブスクリプションの上限は4,096アーティファクトであり、この変更は当方のソース締め切り時点で未マージで、本番環境では利用できなかった。

### HTTP経由のBuzz NIP-ARアーティファクト増分読み取り {#buzz-nip-ar-incremental-artifact-reads-over-http}

別のオープンなBuzzプルリクエストは、NIP-ARアーティファクトのHTTP増分読み取りを追加する（[#8523](https://github.com/block/buzz/pull/8523)）。クライアントはデータベースの更新タイムスタンプと安定したIDによって、120秒の重なりを持たせてページングし、現在のリビジョンか削除のいずれかを受け取る。既知のIDを復元することもできる。結果には結果整合性モデルが用いられる。この提案は完全なスナップショットを約束するものではなく、あるアーティファクトが存在しないことは、削除やアクセスの喪失を意味しない。その最新リビジョンの取得には、メンバーシップ、または非掲載のオープンチャネルに対する明示的な#hスコープが必要であり、掲載状態が変わると増分の進捗はリセットされる。機能ゲートであるBUZZ_ARTIFACT_INCREMENTAL_ENABLEDはオフになっており、すべての書き込み側と移行（現在は0074から0076）が揃っていることが必要となる。この120秒の遅延は運用上の前提である。当方のソース締め切り時点で、この変更はオープンのままだった。

### 委任されたメトリクス閲覧者のためのNIP-AMドラフトテキスト {#draft-nip-am-text-for-delegated-metric-readers}

Buzzのドキュメントに関するドラフトのプルリクエストは、実行時の認可を変更することなく、[NIP-AM](/ja/topics/nip-am/)メトリクスの委任閲覧者を規定している（[#8582](https://github.com/block/buzz/pull/8582)）。所有者宛てに暗号化されたkind 44200 eventは変更されず、エージェントは有効な付与ごとに別個のNIP-44コピーを発行する。各コピーは、所有者が作成した付与eventの正確なIDに紐付けられる。提案されている付与kind 30180と閲覧者数の上限は未解決の問題として残っており、履歴、失効、公開上の紐付けも同様である。署名付きの失効であっても受信者がすでに保持しているコピーを消すことはできず、このドラフトは当方のソース締め切り時点で未マージだった。

### DECK-0003により親が配置するオブジェクトを自ら運べるように {#deck-0003-lets-a-parent-carry-the-objects-it-places}

Cyberspaceのオープンなプルリクエストが、インラインのSNOオブジェクトペイロードのルートテーブルであるDECK-0003 §1.10を提案している（[#81](https://github.com/arkin0x/cyberspace/pull/81)）。親のコピーにエントリが存在すれば、それが無効であっても、ネットワークからの取得なしにそのエントリが優先される。各エントリは作成者のpubkeyにスコープされ、サイズと深さに上限があるほか、循環の制限も設けられている。古いリーダーは欠けているオブジェクトを取得し、プレースホルダーを表示する。提案には、この変更を待って保留されている実装が記載されているが、この変更は当方のソース締め切り時点で未マージだった。

### DECK-0004で導出されたルーム鍵を持つ高さに紐付いたドアを定義 {#deck-0004-defines-height-bound-doors-with-derived-room-keys}

Cyberspace のオープンなプルリクエストは、DECK-0004 に見た目(looks)とドア(doors)に関する §3.6 と §3.7 を追加するものです([#82](https://github.com/arkin0x/cyberspace/pull/82))。ドアは高さに結び付けられています。部屋の鍵は SHA-256(ドメイン分離子 ‖ ロケーション鍵 ‖ ドアシークレット)であり、部屋のバッグはこの鍵で暗号化されます。部屋は複数のドアや入れ子になったドアを持つことができ、新しい錠を設定すると鍵がローテーションされます。最初の実装が存在するまでテストベクターはなく、この文書は当方のソース締め切り時点で未マージでした。

### nostream の NIP-11 ピアリング告知拡張 {#nostream-nip-11-peering-advertisement-extension}

nostream のオープンなプルリクエストは、relay の NIP-11 ドキュメントにピアリングセクションを追加しようとするものです([#999](https://github.com/cameri/nostream/pull/999))。このセクションは、時間的な範囲と決済条件を伴うフィード kind を告知し、あわせて連絡用エンドポイントとピアリング用のプルーフ・オブ・ワークも示します。セクションを無効にするのは `enabled: false` だけで、条件が空であれば決済なしのピアリングを意味します。告知されたオファーは、受け入れられたピアではありません。この変更は、ピア合意も有料フェデレーションも実装していません。当方のソース締め切り時点では未マージでした。

### NIP-CD に任意のインストール済みコマンドリストが加わる {#nip-cd-adds-optional-installed-command-lists}

NIP-CD のフォローアップが [10月27日に NIPs のデフォルトブランチへマージされ](https://github.com/nostr-protocol/nips/pull/2525)([マージ][cd-installed-merge])、仕様のタイトルは現在 Slash Commands となっています。この仕様は [NIP-51](/ja/topics/nip-51/) に倣った任意の kind 10992 リストを定義しており、ユーザーはそこに kind 31992 のコマンド定義を指すアドレス tag を保持します。各コマンド定義は実行者の pubkey と d 値で識別され、任意で relay ヒントを付けることができます。ユーザーはこのリストを管理してもよく、クライアントはオートコンプリートや表示されるチップのためにこれを利用すべきです。このリストは、表示と発見に関する設定です。実行者を認可するものではありません。リストがなくてもプレーンテキストでの呼び出しは引き続き機能し、コマンド固有の tag も、必須のクライアントサポートも必要ありません。NIP-CD は引き続き任意のドラフトであり、今回のマージはどのクライアントがこのリストを採用したかを示すものではありません。

### Marmot、アカウントデバイス向けの公平な準備ルールを絞り込む {#marmot-narrows-its-fair-preparation-rule-for-account-devices}

Marmot は、アカウントデバイスを必要とするグループ向けのスケジューリングルールについて、[10月28日に修正をマージしました](https://github.com/marmot-protocol/marmot/pull/450)。有界の収束パスが Stable に達した後は、キューに入った受信処理だけで次のパスが強制される前に、管理者によって認可されたキュー内のインテント1件、または同じアカウントからの許可されたインテント1件が、準備の試行を1回受けます。SelfUpdate と Leave はこの追加の公平性保証の対象外ですが、どのメンバーも引き続きそれらをコミットできます。この変更は、認可されたすべてのインテントを対象としていた以前の文言を修正するものです。アカウントデバイスを必要としないグループは、従来のスケジューリングを維持します。ワイヤ形式の変更はなく、準備の試行は、有効な、受理された、あるいは正規の Commit を保証するものではありません。

### Marmot、アカウントグループ向けの非表示デバイス名簿を提案 {#marmot-proposes-a-hidden-device-roster-for-account-groups}

マージされていないオープンな Marmot の提案は、[device-roster-v1 コンポーネントを追加するもので](https://github.com/marmot-protocol/marmot/pull/452)、ID は 0x800e、すべてのリーフが1つのアカウントに属する非表示グループを対象とします。グループは作成時から名簿を持つか、一度も持たないかのどちらかです。名簿はデバイス、拒否されたスロット、拒否された KeyPackage、リーフマップを記録します。また、候補となる親に適用される、明示的で順序に依存しない差分更新を使う最初のコンポーネントでもあります。削除されたスロットは、兄弟デバイスがそれらを削除できないグループについて、リーフマップを保持できます。デバイスがデバイスグループを信頼するのは、そのグループを自ら作成した場合か、確認済みのリンクによって認証された Welcome を通じて参加した場合に限られます。したがって、0x800e マーカーだけでは信頼は付与されません。設立時の Add は、確認済みリンクに由来する KeyPackage を正確に指定します。盗まれたリンク済みデバイスは、削除されるまで名簿を編集できます。デバイス数の上限は、デバイスに適用されます。リーフマップと拒否のレコードにはエントリごとのサイズ制限がありますが、レコード数の上限はありません。名簿データが他のアカウントにコピーされることはなく、このグループはチャット、件数、通知、送信先から非表示のままです。本文によれば、MDK は名簿のバイト列をテスト用スイッチの背後に置いており、新たな通常の UI はありません。

### Marmot、アカウントデバイスの有効化失敗時のフィードバック明確化を提案 {#marmot-proposes-clearer-feedback-when-account-device-activation-fails}

マージされていない別のオープンな Marmot 提案は、アカウントデバイスについて[クライアントが有効化の失敗を説明できるようにするものです](https://github.com/marmot-protocol/marmot/pull/453)。クライアントは、あるグループでアカウントデバイスを有効化できないことを報告できます。ただし、このグループ単位のフィードバックでは、それを妨げているメンバーやデバイスを特定することはできません。アクティブな管理者ではないメンバーが知ることができるのは、自身が管理者の地位を持たないということだけです。ブランチの選択が失われた場合や、再生成された有効化チェックが失敗した場合には、ユーザーが新たにリクエストを行う必要があります。クライアントが自動的に有効化を再試行することは決してありません。有効化には、認可されたクライアントからのユーザーによる新たなリクエストが必要だという既存のルールは変わりません。これは規範的なドラフト文であり、実装済みまたはデプロイ済みの動作を示すものではありません。

### Marmot、新しいデバイスのペアリングに絵文字による検証を提案 {#marmot-proposes-emoji-verification-for-pairing-new-devices}

マージされていないオープンな Marmot の提案は、Matrix の m.sas.v1 をモデルとし、X25519、HKDF、HMAC を用いるやり取りによって[新しいデバイスをペアリングする方法を記述しています](https://github.com/marmot-protocol/marmot/pull/454)。ユーザーは両方の画面に表示されるラベル付きの7つの絵文字を比較するだけで、コードを読んだり入力したりはしません。アカウント鍵を保持していることが、デバイスの認証になることは決してありません。署名なしの5つの rumor(Request、Answer、Reveal、Confirm、Cancel)はアカウントの pubkey 宛てにラップされ、アカウント、セッション、新しい KeyPackageRef、既存のデバイススロット、新規の鍵を結び付けます。先に確認を行うのは既存のデバイスで、確認された KeyPackageRef そのものだけを追加します。新しいデバイスは検証を終えてから確認を行い、確認済みのやり取りによって認証されたグループ ID に対する Welcome だけを受け入れます。kind 452 から 456 が提案されており、457 から 489 は予約されています。アカウント鍵の保有者は、確認後であっても Cancel を偽造してサービス拒否を引き起こすことができます。1時間あたりの Answer の上限は、再起動をまたいで保持されません。relay はラップの集中的な送信とアカウントのアドレスを見ることができ、マージや Welcome に関する一部のケースは先送りされたままです。実装ではこれらの形式はデフォルトで無効になっています。また、作成者が提供した2つの既知解ベクターは、独立したセキュリティ監査や相互運用性監査ではありません。

### NIP-5D napplet 提案、メディアとソースのフィールドを厳格化 {#nip-5d-napplet-proposal-tightens-media-and-source-fields}

[オープンな NIP-5D napplet 提案](https://github.com/nostr-protocol/nips/pull/2303)については以前に紹介しました。その10月28日の変更が、NIPs のデフォルトブランチではなく提案ブランチにマージされ、10月17日に導入された任意のメディアおよびソースのフィールドが改訂されました。スクリーンショットとプレビューの tag は [NIP-92](/ja/topics/nip-92/) のキーバリュー形式のフィールドを再利用するようになり、必須の小文字 SHA-256 の x 値1つと、任意の m、dim、size、alt、duration を持ちます。読み取り側は、レンダリングの前にハッシュを検証し、実際の形式をデコードしなければなりません。有効な m フィールドが存在する場合は、デコードされた形式がその MIME タイプとも一致していなければなりません。x が欠落している、重複している、または不正なエントリは無視されます。不正な任意フィールドは、他の利用可能なメディアを破棄することなく取り除かれ、複数のプレビューは無視されます。source-commit は完全な Git ID に正確に解決されなければならず、HTTPS のソースアーカイブにはバイト単位で正確な SHA-256 の一致が必要です。重複した、または形式が不正なソースフィールドは無視され、利用できないソースデータが HTML の再生を妨げてはなりません。コミットやアーカイブが一致しても、再現可能なビルドが証明されるわけではなく、クライアントの適合性も主張されていません。

## Nostr の10月、6年分 {#six-years-of-nostr-octobers}

6回の10月を通じて、Nostr の日付の付いた変更は、メッセージのフレーミングから、その上に構築されるアプリケーションへと外側に広がっていきました。2021年には、基本仕様が[クライアントメッセージをトップレベルの JSON 配列としてフレーミングすることを確定させました](https://github.com/nostr-protocol/nostr/commit/69509f40cd6a4d5c14a7c402b04495a1de5ab2c2)。その後の10月には、クライアントでの検索と Lightning インボイス、タイムスタンプによる証拠とジョブリクエスト、メディアのバリアントと ecash ウォレット、そしてコードコラボレーションとプライベートメッセージのメタデータが加わりました。同じ月の他の変更によって、relay の状態の可視化から、署名者用の独立した鍵、ウォレットのペアリングに至るまで、アイデンティティや接続をプログラム間で持ち運びやすくなりました。今年の10月には、同じドキュメントが[空のフィルターリストが何にマッチするかを定義し](https://github.com/nostr-protocol/nips/commit/37db639582d857e12468dcccd99b2c7f1d657da9)、同一の JSON を読む relay は、それがどの event を選択するかについて共通のルールを持つようになりました。

### 2021年10月:トランスポートの曖昧さをなくす {#october-2021-making-the-transport-unambiguous}

10月4日、基本プロトコル仕様である [NIP-01](/ja/topics/nip-01/) が[改訂され、クライアントメッセージはトップレベルの JSON 配列となりました](https://github.com/nostr-protocol/nostr/commit/69509f40cd6a4d5c14a7c402b04495a1de5ab2c2)。非公式だった EVENT、REQ、CLOSE の接頭辞は各配列の最初の要素となり、固定の `/ws` パスの要件が削除されたため、どの WebSocket エンドポイントでもよくなりました。これは、すでにコードが存在していた仕様を明確化するものでした。独立して書かれたクライアント同士が、より高度な機能で相互運用するには、まず正確なフレーミングが必要です。

10月23日には、[relay からクライアントへの方向に、明示的な EVENT と NOTICE メッセージが加わりました](https://github.com/nostr-protocol/nostr/commit/97786e31423b45239306323a9a297188d20dbf21)。relay の EVENT は既存の REQ サブスクリプションの識別子を含むため、1つの接続で複数のサブスクリプションを実行しているクライアントは、結果をリクエストと対応付けることができます。NOTICE は人間が読めるテキストを運びます。これほど小さな語彙であれば複数回実装するのも現実的で、個別に運営される relay に適しています。

[10月23日時点の NIP-01 のテキスト](https://github.com/nostr-protocol/nostr/blob/97786e31423b45239306323a9a297188d20dbf21/nips/01.md)は、署名が何をカバーするかも示しています。event の ID は、先頭のゼロ、作成者の公開鍵、タイムスタンプ、kind、tag、content を収めたコンパクトな UTF-8 JSON 配列のダイジェストです。作成者は、そのダイジェストに secp256k1 曲線上の Schnorr 署名で署名します。WebSocket のエンベロープとサブスクリプション識別子は、その署名対象データの外側にあります。このテキストからは、同じ署名済み event が、再署名されることなく異なるサブスクリプションや異なる接続を通じて届きうることが導かれます。REQ はまず一致する保存済み event を返し、その後、クライアントが CLOSE を送るか、ソケットを閉じるか、新しい REQ でサブスクリプション ID を再利用するまでライブ状態を保ちます。1つのフィルター内ではすべての条件が満たされなければならず、1つの REQ 内の複数のフィルターは、そのいずれかを満たす event にマッチします。そのバージョンのフィルター名は、現在のものとは異なります。NOTICE の挙動は規定されないままで、relay が event をどれだけの期間保持するかについても、クエリがそれらをすべて返すことについても、何も約束されていませんでした。5年後、同じ仕様は REQ 内のフィルターが何を意味するかという問題に立ち返ることになります。

### 2022年10月:フィードがスマートフォンで使えるものになる {#october-2022-a-feed-becomes-usable-on-a-phone}

10月8日、iOS 向け Nostr クライアントの Damus が[ハッシュタグ、プロフィール、event の検索を追加しました](https://github.com/damus-io/damus/commit/2c4c392b76d9ad92b28e71d6d578bdb42c2ac3de)。この変更は検索結果ビューとスレッドモデルに手を入れるもので、読者は流れてくるテキストをスクロールするだけでなく、署名済みのアイデンティティや特定の event に直接移動できるようになりました。この検索はクライアント自身のナビゲーション内で機能するもので、relay 側の全文検索ではありませんでした。

8日後、Damus は [relay 設定の単純な行を、各接続の状態を示すビューに置き換えました](https://github.com/damus-io/damus/commit/e5e0fb2db279a5a2763d39b15d5fff20bec26fdd)。色付きのドットは、クライアントの relay プールの状態を読み取ります。緑は接続済み、黄は接続中または再接続中を意味し、それ以外は赤、最初の読み取り前は灰色です。ビューは表示された時点で更新され、その後は2秒ごとに更新されます。既存のスワイプによる削除は、新しいビューに移されました。ドットが見えるようになったことで、フィードが止まっていても、それを作成者の沈黙と解釈する必要はなくなりました。複数の独立した接続のうち、どれがつながっていてどれが再試行中かを、読者が確認できるようになったからです。緑のドットが示すのは、ソケットが開いていることです。relay が event を受け入れた、あるいは保持したことを示すものではありません。クエリが relay の保持するすべてを返したことを示すものでもありません。このコミットは、マージ済みのソースにおける実装を記録しています。このソース変更から、App Store でのリリース日が確定するわけではありません。

10月19日、Damus は投稿、チャット、ダイレクトメッセージ向けに [BOLT11 Lightning インボイスのパーサーとインボイスウィジェットを追加しました](https://github.com/damus-io/damus/commit/c6ab1de63926ff7f6e29a260e3e7f2473855c9c7)。ウィジェットにはインボイスの説明と satoshi 単位の金額が表示され、その Pay ボタンは `lightning:` URI を iOS 経由でインストール済みのハンドラーに渡します。ソーシャルクライアントは署名済みの投稿を表示し、支払いは別のウォレットが行います。これらのウィジェットは後の zap レシートの慣例より前のものであり、標準化された zap ではなく、インボイスの表示です。

### 2023年10月:event が証拠と作業リクエストを運ぶ {#october-2023-events-carry-evidence-and-requests-for-work}

10月11日、event に関する証拠を Bitcoin に固定する [NIP-03](/ja/topics/nip-03/) の OpenTimestamps 証明が、[event 上の `ots` フィールドから、独立した kind 1040 event へと移されました](https://github.com/nostr-protocol/nips/commit/09ffb951c69343312486aaff2726dca04bc42f6e)。その event は `e` tag で元の event を指し、少なくとも1つの Bitcoin 証明を含む base64 形式の OpenTimestamps ファイル全体を content に収めます。参照される event id はそれ自体が証明の対象となるダイジェストなので、検証者はその event が証明された時刻までに存在していたことを知ることができます。その時刻の出どころは、作成者の `created_at` ではなく Bitcoin です。この証明は event の日付を示すものであり、その内容については何も主張しません。

10月12日には、タイムスタンプの変更とは別に、[NIP-06](/ja/topics/nip-06/) の鍵導出に[2つのテストベクターが追加されました](https://github.com/nostr-protocol/nips/commit/202e18f2b256646148805880ed58731c1c8b2b9b)。ニーモニックとは、リカバリーシードをエンコードする単語の並びです。これらのベクターは12語と24語のニーモニックを1つずつ扱い、それぞれについて期待される秘密鍵と公開鍵を、16進数、および nsec と npub のエンコーディングで示しています。NIP-06 はすでに BIP-39 を使ってニーモニックをバイナリシードに変換し、BIP-32 パス `m/44'/1237'/<account>'/0/0` を使って鍵を導出しており、アカウント0が基本的な単一鍵の選択肢でした。10月の追加が提供したのは既知の答えであり、ニーモニックによる復元や新しい導出アルゴリズムではありませんでした。これによりクライアントは、自らの導出とエンコーディングが文書化されたアイデンティティを再現するかどうかを確認できるようになりました。ベクターと一致すれば、実装同士を比較できるようになります。ただし、それは特定の実装を認証するものでも、すべてのウォレットやクライアントのインポートが一致することを証明するものでもありません。シードを盗難から守ることは別の問題であり、ベクターはそれに対処していません。

10月29日、データ・ベンディング・マシンの標準である[NIP-90](/ja/topics/nip-90/)が、[固定のジョブkindを定めたうえでNIPsリポジトリにマージされました](https://github.com/nostr-protocol/nips/commit/7a2de8ab25ceaa35376e6b7457f08b5bffde70b3)。kind 5000から5999がジョブリクエスト用に予約され、各結果のkindはリクエストのkindに1000を足した値と定められました。フィードバックにはkind 7000が使われました。リクエストはテキスト、URL、あるいは以前のジョブを参照できます。期待する出力を指定し、任意で入札額を提示することもできます。こうしてタスクは、特定のベンダーのAPIに依存せず、どのプロバイダーでも応答できる署名付きeventの中に置かれることになります。以前のドラフトではkind 68001と68002が使われていました。

### 2024年10月：メディアの代替バリアントとポータブルなecash {#october-2024-media-alternatives-and-portable-ecash}

10月15日、[NIP-71](/ja/topics/nip-71/)のビデオeventは[ビデオのバリアントに`imeta` tagを採用しました](https://github.com/nostr-protocol/nips/commit/1cda2dcc594538ea14b88aec7f1f784e06a31bbf)。当時のaddressableなkind 34235と34236では、各バリアントのURL、寸法、MIMEタイプ、プレビュー画像、フォールバックが1つのtagにまとめて収められていました。解像度を選ぶクライアントは、どのサムネイルとフォールバックがその解像度に対応するのかを知る必要があります。平坦化されたメタデータでは、それを示せませんでした。なお、これらのkind番号は過去のものです。現在のNIP-71ではkind 21と22が使われています。

その10日後、いずれも以前のドラフトで導入されていた[NIP-60](/ja/topics/nip-60/)のCashuウォレットと[NIP-61](/ja/topics/nip-61/)のnutzapが、[仕様としてまとめてマージされました](https://github.com/nostr-protocol/nips/commit/ba46b23d95b186c9a8fedabf8324af2ae40e8ce4)。どちらも、mintが発行するトークンを用いるecashプロトコルであるCashuを基盤としています。NIP-60は暗号化されたウォレットのプルーフをrelayに保存するので、互換性のあるアプリケーションは同じウォレット状態にアクセスできます。NIP-61では、受信者のkind 10019 eventに、信頼するmint、relay、ロック用の鍵が記載されます。送信者のkind 9321 eventはその鍵にロックされたプルーフを運び、受信者がそれを引き換えます。ユーザーは引き続き、トークンを発行するmintに依存します。また、アプリケーションは同じプルーフが二重に引き換えられないよう対策しなければなりません。

10月29日には、ユーザーに代わって署名する鍵を別のサービスが保持する[NIP-46](/ja/topics/nip-46/)のリモート署名が、[`bunker://`接続文字列にリモート署名者の公開鍵を含めるよう改訂されました](https://github.com/nostr-protocol/nips/commit/f1e8d2c4f764d66996c0c1fb2eeabfbc0c7b2528)。ユーザーのアイデンティティは別途取得します。[改訂後のテキスト](https://github.com/nostr-protocol/nips/blob/f1e8d2c4f764d66996c0c1fb2eeabfbc0c7b2528/46.md)は、クライアントに対して2つの鍵を区別すること、そして接続後に`get_public_key`を呼び出すことを求めています。クライアントはこのやり取りのために独自の鍵ペアを生成し、暗号化したリクエストを署名者の鍵宛てに送ります。一方、`sign_event`はユーザーの鍵で署名されたeventを返します。2つの鍵が同じである場合もありますが、同じである必要はありません。接続文字列内の鍵が識別するのは署名サービスだけです。ユーザーのアカウントを表すのは、`get_public_key`が返す公開鍵です。4日前のNIP-60は共有ウォレット状態に取り組みましたが、この改訂が扱うのは署名者のアイデンティティという別の問題です。このコミット時点の例は、当時NIP-46が規定していた暗号化トランスポートをまだ使っています。また、この変更によってリモート署名者がトラストレスになるわけではなく、誰がユーザーの鍵を保持しているかが証明されるわけでもありません。

### 2025年10月：コラボレーションの更新とプライベートメッセージのメタデータ {#october-2025-collaboration-updates-and-private-message-metadata}

10月8日、[NIP-47](/ja/topics/nip-47/)のNostr Wallet Connectに、[アプリとウォレットをペアリングするためのディープリンクが追加されました](https://github.com/nostr-protocol/nips/commit/2ace01cf1ad0a68dae6217111c9286e3de759923)。ウォレットは`nostrnwc://connect`またはアプリ固有の`nostrnwc+{app_name}://connect`を登録できます。リクエスト側のアプリは、URIエンコードしたアイコン、自身の名前、コールバックスキームを付けてそのリンクを開きます。ウォレットは接続を作成すると、`value`パラメーターを付けてコールバックを開きます。このパラメーターには、ペアリングコードである`nostr+walletconnect://` URIが入っています。DamusがiOSを通じてウォレットにインボイスを渡してから3年が経ち、1台のスマートフォン上でペアリングするために、同じ画面に表示されたQRコードを読み取ったり、アプリ間で長い文字列をコピーしたりする必要はなくなりました。この追加が対象とするのは、この受け渡しだけです。支払い方法は何も変わらず、この仕組み自体が支払いを行うこともありません。両方のアプリがハンドラーを実装する必要があり、仕様のテキストは、すべてのウォレットが実装していることの証拠にはなりません。支出予算、同意画面、どのアプリならコールバックスキームを安全に所有できるかといった問題も、これで解決するわけではありません。

10月16日には、[NIP-34](/ja/topics/nip-34/)のgitコラボレーションに、既存のパッチeventに加えて[kind 1618のプルリクエストeventとkind 1619の更新eventが追加されました](https://github.com/nostr-protocol/nips/commit/6e6b9877b32b44e84c0f3c3d412d688cf86761b0)。プルリクエストは先端のコミットとクローン元の場所を指定し、更新eventはその先端を移動させます。パッチは60 kB未満が推奨され、それより大きな提出にはプルリクエストを使います。これにより、大きな提出に推奨される経路は、event内に格納するパッチ本体から、コミットへの署名付き参照へと移りました。小さな変更は、引き続きパッチとして送ることができます。Nostrが運ぶのは調整と署名付き参照であり、それらの参照が指すコミットオブジェクトは引き続きGitサーバーが提供します。

10月27日、[NIP-59](/ja/topics/nip-59/)のgift wrapに、有効期限tagを追加する際は[sealとgift wrapのタイムスタンプをそれぞれ独立にランダム化するよう求めるガイダンスが加わりました](https://github.com/nostr-protocol/nips/commit/bcaad2957d0e9cec20e4265298d2788be87d3190)。gift wrapはメッセージをこの2つの層で包みます。各層に独自のランダムなタイムスタンプを与えると、層どうしのタイミングを相関づけにくくなります。ここで関心の対象は、内容の暗号化から、メタデータの相関によって明らかになりうる情報を抑えることへと移りました。暗号化はメッセージそのものを隠しますが、封筒の周りにあるタイミングなどのメタデータは観測可能なままです。それらをどれだけ容易に結びつけられるかは、実装上の選択によって決まります。このガイダンスは新たな暗号化を加えるものではなく、参加者を匿名にするものでもありません。

### 2026年10月：クエリの意味の共有とテキストで起動するサービス {#october-2026-shared-query-meanings-and-text-triggered-services}

10月5日、[NIP-92](/ja/topics/nip-92/)のメディア添付は[`imeta` tagの適用範囲をkind 0のプロフィールに広げました](https://github.com/nostr-protocol/nips/commit/a79e21d90fce5465b50ef385dd368bba99ec4a0b)。これによりプロフィールは、自身の`picture`と`banner`について、フォールバックURL、blurhash（ぼかしたプレビューをコンパクトにエンコードしたもの）、寸法、代替テキスト、その他の添付メタデータを記述できるようになりました。NIP-92自体はこの変更以前から存在していました。新しいのは、2024年にNIP-71がビデオのバリアントに適用したグループ化されたメタデータが、今度はプロフィール画像にまで及ぶようになった点です。対応付けには完全一致が求められます。tagが適用されるのは、そのURLがpictureまたはbannerのURLと等しい場合に限られます。クライアントはどちらにも一致しないtagを無視すべき（SHOULD）であり、プライマリURLが失敗した場合はフォールバックを試すべき（SHOULD）です。新しいkind 0 eventは以前のプロフィールを置き換えます。そのため発行者は、変更のない画像についてはメタデータを引き継ぎ、もう使われていない画像のtagは削除すべき（SHOULD）です。そうすれば、古い代替テキストや寸法が、いつの間にか別の画像を説明している事態を防げます。この更新ルールは、新しいフィールドと同じくらい重要です。`imeta` tagがあっても、画像が利用可能であり続けることや、より速く読み込まれることは保証されません。プライバシー保護も提供せず、クライアントがすべてのフィールドを表示する必要もありません。

10月17日、[NIP-01が明確化され、filter内の空リストはどのeventにも一致しないと定められました](https://github.com/nostr-protocol/nips/commit/37db639582d857e12468dcccd99b2c7f1d657da9)。これは属性を省略した場合とは異なる扱いです。[続く変更では、一貫性のない「1つ以上」という表現が削除され、一致しえないリストをクライアントが送らないよう推奨されました](https://github.com/nostr-protocol/nips/commit/0b5532c0355ab27f447e071a93c09cf3a2b4aad5)。2021年10月、この文書ではREQのJSONメッセージの構造について合意が得られました。REQメッセージは配列であり、各filterはその中に含まれるJSONオブジェクトです。今年の10月に定まったのはfilterのセマンティクスで、そうしたfilter内の空リストが何を意味するかが確定しました。同じフレームを同じように解析するrelayどうしでも、異なる結果を返す可能性があったからです。

10月21日には、[当時Commandsという名称だったNIP-CDが、提案からマージ済みのドラフト仕様へと移行しました](https://github.com/nostr-protocol/nips/commit/7b5ea85479c0b4efce3c246abefa1dae8f8f91e4)。NIP-CDはスラッシュコマンドについて記述しています。コマンドはkind 31992 eventで定義されます。呼び出しはeventのcontentの最初の文字から始まるプレーンテキストなので、クライアントがそれを送信するのに特別なサポートは要りません。[続く提案](https://github.com/nostr-protocol/nips/pull/2525)は、別ブランチ上の[以前のコミット](https://github.com/nostr-protocol/nips/commit/0142de0384210d69074c089448ef5bc303faef37)とともに、[10月27日にマージされました](https://github.com/nostr-protocol/nips/commit/400d157c53264b8e58c7b3cdbd21ef546fb7a157)。この提案により仕様の名称はSlash Commandsに改められ、任意で使えるkind 10992のインストール済みコマンドリストが追加されました。クライアントは、これを自動補完と表示に使うべきとされています。これらのリストはユーザーの好みを記録するものです。実行者を認可したり、プレーンテキストによる呼び出しを制限したりするものではありません。NIP-90のジョブが構造化されたリクエストeventと結果eventを使うのに対し、コマンドは普通のテキストとして読める形のままです。
