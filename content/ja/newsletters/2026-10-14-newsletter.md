---
title: "Nostr Compass #44"
date: 2026-10-14
publishDate: 2026-10-14
draft: false
type: newsletters
description: "デスクトップ版Amethyst、Amberのセキュリティ修正、プライベートな添付ファイル、認証付きソフトウェアインストール、コンテンツ警告とステータス。"
translationOf: /en/newsletters/2026-10-14-newsletter.md
translationDate: 2026-10-15
---

**[Amethyst](#amethyst)** はAndroidのインターフェースをデスクトップに展開し、Waylandのネイティブサポートを追加しました。**[Amber](#amber)** は、権限の取り消し、コピーしたシークレットの消去、鍵の喪失につながり得る設定変更の問題を修正しました。**[Keep](#keep-android)** は自動署名の権限を厳格化し、**[MDK](#mdk)** はプライベートな添付ファイルのストリーミングと、古いメッセージから順に取得する追いつき処理を導入しました。**[Zap Cooking](#zap-cooking)** は、フォローリスト編集の保護策と、認証に基づくメンバーシップ処理をマージしました。以下では、プロトコルの変更や公開ステータスの仕組みとともに、[リリースの詳細](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0)を紹介します。

## 主なニュース

### Amethyst

[Amethyst v1.18.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.18.0) は、Android向けソーシャルクライアントの共通インターフェースをデスクトップに展開し、カスタムフィード、幅広ウィンドウ向けのデッキ表示、任意で有効にするロック、暗号化メディア、[Blossomへのアップロード](/ja/topics/blossom/)に対応しました。[NIP-85の信頼できるアサーション](/ja/topics/nip-85/)に基づくプロバイダーのスコアは、リクエスト、通知、バッジで利用するためにローカルでインデックス化され、プロバイダーとしきい値はユーザーが選択できます。

本日の[v1.19.0リリース](https://github.com/vitorpamplona/amethyst/releases/tag/v1.19.0)では、Waylandのネイティブサポートと、別途インストールしたFFmpegおよびffprobeを使用するデスクトップでの動画圧縮が追加されました。鍵ストレージの修正により、キーチェーンの確認が繰り返される問題とLinuxのキーリングの失敗に対処しています。カレンダーコレクションとRSVPの表示に対応し、Androidのログイン画面には[NIP-46によるリモート署名](/ja/topics/nip-46/)が追加されました。暗号化エンベロープを並列で開いてから逐次インデックス化するようになり、relayへの再接続とフィード投稿者のrelayリストの処理も修正されました。[relayクライアントはレート制限のバックオフを守り](https://github.com/vitorpamplona/amethyst/pull/4422)、その後に購読や送信を再開します。

[信頼プロバイダーのrelayに関する変更](https://github.com/vitorpamplona/amethyst/pull/4437)では、ユーザーのkind 10040リストにあるプロバイダーのrelayを、自身の信頼済みrelayとして扱います。これらの接続は既定で直接接続を使用し、Torを使用するには信頼済みrelayの設定を有効にする必要があります。メインクライアントの[NIP-42によるrelay認証](/ja/topics/nip-42/)は、これらのrelayにユーザーの公開鍵を開示する可能性があります。

### Amber

[Amber 6.6.9](https://github.com/greenart7c3/Amber/releases/tag/v6.6.9) は、Android向けNostr署名アプリの3件のセキュリティ上の欠陥を修正しました。[取り消された権限](https://github.com/greenart7c3/Amber/security/advisories/GHSA-8f7m-9g64-vrjw)がキャッシュの競合によって残存することはなくなり、明示的な拒否が完全に信頼された状態より優先されるようになりました。[コピーしたシークレット](https://github.com/greenart7c3/Amber/security/advisories/GHSA-g62f-m6pm-jv9p)には、プロセスが強制終了された場合も含め、60秒後にクリップボードを消去する処理がシステムによって予約されます。その間は内容を読み取ることができ、その後にコピーしたテキストも消去される場合があります。[「端末のロック解除を必須にする」](https://github.com/greenart7c3/Amber/security/advisories/GHSA-wv7c-hq2j-ppc5)設定を変更しても、シークレットの移行が完了するまで古いラッピング鍵が保持されますが、以前に失われた鍵は復元されません。このリリースでは、複数リクエストのnostrconnect承認を修正し、URIで指定されたrelayに応答するようにしました。6.6.8以前のユーザーは更新してください。

### Keep Android

[Keep Android v1.3.0](https://github.com/privkeyio/keep-android/releases/tag/v1.3.0)は、[FROSTしきい値署名アプリ](/ja/topics/frost/)であり、端末上での分散鍵生成と、中断されたシェア操作の認証付き復旧を追加しました。StrongBoxに対応していない端末にも対応しています。しきい値署名では、参加端末が署名用シークレットのシェアを保持し、協力して署名を生成します。どの端末が参加できるかは、セットアップと復旧の手順によって決まります。

[バージョン1.3.1](https://github.com/privkeyio/keep-android/releases/tag/v1.3.1)では、自動署名が、記憶された拒否、Ask権限、期限切れの承認、権限の読み取り失敗を上書きしないようにしました。期限切れになると、拒否は保持したまま、バックグラウンドでの承認が削除されます。[アプリごとのポリシー移行](https://github.com/privkeyio/keep-android/pull/532)では、より厳格な判断を保持しつつ、権限をコアが管理するストアへ移します。

### Chama

[Chama v6.4.21](https://github.com/jesuspirate/chama/releases/tag/v6.4.21) は、Nostrを介した取引アプリケーションが使用する[ネイティブウォレットブリッジを認証](https://github.com/jesuspirate/chama/pull/29)し、本番環境でのURLベースのブリッジリダイレクトを無効化し、支払額を検証します。また、内容を読み取れないウォレットの消去を拒否します。

[バージョン6.4.22](https://github.com/jesuspirate/chama/releases/tag/v6.4.22)では、外部者のeventに対するリプレイ処理を強化し、後継関係を確認し、空の仲裁者プールを拒否し、署名済みのLOCK時刻から返金時期を算出します。コンセンサスの変更は2026年11月1日以降に署名されたCREATE eventに適用され、クライアント側の保護は直ちに適用されます。リリースノートには、出品情報で選択されるフェデレーションとダスト額の支払いに関する注意事項が引き続き記載されています。その後の[署名アプリと復旧に関する変更](https://github.com/jesuspirate/chama/releases/tag/v6.4.23)では、保護されたシードの読み取り機能と、遅延したロックからの復旧が追加され、[v6.4.24](https://github.com/jesuspirate/chama/releases/tag/v6.4.24)では大規模な取引リストが改善されました。

### Zap Cooking

レシピとソーシャル機能を備えたクライアント[Zap Cookingは、フォローリスト編集の保護策をマージ](https://github.com/zapcooking/frontend/pull/795)し、不完全な読み取り、古い読み取り結果、予期せず縮小した読み取り結果に対処しました。フォロー操作は、既存のtagとコンテンツを保持する、保護された単一の更新経路を共有します。送信前には署名者の識別情報を確認します。[メンバーシップ認可の修正](https://github.com/zapcooking/frontend/pull/802)では、認証済みリクエストに署名した公開鍵を使用します。[管理用シークレットを露出させていたルートは削除されました](https://github.com/zapcooking/frontend/pull/801)が、デプロイ時には引き続きシークレットのローテーションが必要であり、変更がマージされたというだけでは、その実施を確認できません。その後の[スレッドとブックマークの修正](https://github.com/zapcooking/frontend/pull/833)では、実際の返信ルートを保持し、失敗したブックマークの書き込みを復旧します。[レシピのtagフィールド](https://github.com/zapcooking/frontend/pull/836)は、キー入力をプロフィールやNIP-50の検索サービスに送信したり、未保存の変更を残したままエディターから離れたりすることがなくなりました。

## tag付きリリース

### MDK

[MDK v0.13.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.13.0)は、[Marmotの暗号化グループ](/ja/topics/marmot/)向けランタイムであり、進捗表示とキャンセルに対応した、プライベートな添付ファイルのストリーミングおよび再開可能な転送を追加しました。また、メッセージ、グループ、relayの識別子を含めずに、非公開の[NIP-56による通報](/ja/topics/nip-56/)を[NIP-59のgift wrap](/ja/topics/nip-59/)を通じてデプロイ先の運用者へ送信します。追いつき処理では最大256件のeventを古い順にバッチ処理し、relayのCLOSEDによる拒否を保持します。SOCKS5によるルーティングはrelay、メディア、探索サービスを対象とし、直接接続へのフォールバックはありません。

[リリースガイド](https://github.com/marmot-protocol/mdk/blob/v0.13.0/docs/release/0.13.0.md)では、バインディング、ヘッダー、ネイティブ成果物をそろえて更新することが求められています。データベーススキーマは101から107へ進み、ダウングレード経路はありません。ホストのシークレットストレージには移行が必要です。MarmotKitとCの成果物は安定版ですが、WN Agentは引き続きプレリリースで、ワークスペースのcrateはcrates.ioで公開されていません。5 [MLS epoch](/ja/topics/mls/)を超えて遅れて到着した履歴は、履歴が不完全であるとの通知がないまま、依然として復号できない場合があります。また、認証済みのエージェントクライアントはAPI全体へのアクセス権を引き続き持ちます。

このリリースでは、[最初の受領確認後も保留状態に残ったプロフィール、フォローリスト、relayリストの保存を再試行](https://github.com/marmot-protocol/mdk/pull/2228)するようにもなりました。これらのバックグラウンド再試行は、再起動後には引き継がれません。[招待の検索では、探索用relay上でKeyPackageの削除と有効期限を確認](https://github.com/marmot-protocol/mdk/pull/2211)しますが、その応答では、受信者がKeyPackageの秘密情報を今も保持していることは証明できません。[アクティビティへのリアクションの対象](https://github.com/marmot-protocol/mdk/pull/2187)は、認証済みのアクターと個々のグループコミットから一貫して導出されるようになりました。アクター情報のない古い履歴は、引き続き不完全なままです。

その後の master での作業では、[閉じられずに残っていた relay の購読を終了し、アクティベーション時の再生処理を500件の event を上限とするページに分割します](https://github.com/marmot-protocol/mdk/pull/2274)。[エポック間の欠落からの復旧](https://github.com/marmot-protocol/mdk/pull/2298)では、比較に失敗した relay から最新の256件の event を取得しますが、履歴の完全性を保証するものではありません。[自己更新コミットは、送信できなかったすべてのグループ relay への送信を再試行します](https://github.com/marmot-protocol/mdk/pull/2275)。新しい警告チェックは、[古いことが判明しているエポック](https://github.com/marmot-protocol/mdk/pull/2273)と、[relay にまだ送信すべきコミット](https://github.com/marmot-protocol/mdk/pull/2288)を対象とします。ユーザーはリスクを承知したうえで続行できるため、これらのチェックはグループの分岐が起こらないことを保証するものではありません。

[ストレージ不足で停止した添付ファイルのダウンロード](https://github.com/marmot-protocol/mdk/pull/2249)は、空き容量が足りない場合も再開可能な進捗を保持します。明示的に開始した大容量ダウンロードではファイルへの書き出しを使用し、ステージングとチェックポイントのために、本体サイズのおよそ5〜6倍の空き容量が必要になります。[検証済みの公開 event のプレビュー](https://github.com/marmot-protocol/mdk/pull/2304)には、容量制限のある暗号化されたアカウントキャッシュが追加され、[廃止済みの KeyPackage しか含まれない結果](https://github.com/marmot-protocol/mdk/pull/2305)は、不完全な relay 検索と区別できるようになります。これらは後続のソース変更であり、ホスト側でも対応する変更を取り込む必要があります。取得完了済みの event ID によるプレビューでは、その後の削除を再確認しません。

エージェントブリッジでも、巨大な応答によるメモリの枯渇を防ぐために[バックエンド出力に上限を設け](https://github.com/marmot-protocol/mdk/pull/2103)、[コネクターが実際に返す削除応答を受け入れるようにしています](https://github.com/marmot-protocol/mdk/pull/2301)。出力上限によってターンが停止しても、すでに配信されたテキストは配信済みのままです。

### Myco

[Myco v0.11.0](https://github.com/Origami74/myco/releases/tag/v0.11.0)は、スマートフォンや fips デスクトップ間の USB 接続を追加し、署名された成果物とアイコンのハッシュを含む[現在提案中の NIP-5D マニフェスト形式](https://github.com/Origami74/myco/pull/135)を採用しています。古いスマートフォンでも引き続きペアリングできますが、これらの napplet を開くには更新が必要です。[ダウンロードポリシーの変更](https://github.com/Origami74/myco/pull/133)では、インターネット、メッシュ、ユーザー設定の HTTP 接続先を区別します。インターネットポリシーでは、作者が指定したヒントやリダイレクトを使ってローカルネットワークを探索することはできませんが、ユーザーが設定した接続先には制限がありません。ソフトウェアクライアントは、[作者の BUD-03 Blossom サーバー上でも blob を検出します](https://github.com/Origami74/myco/pull/134)。これにより成果物を見つけやすくなる一方、インストール時の通信がそれらのサーバーに見えるようになります。これらの HTTP に関する変更は、WebSocket 接続に同等の保護を確立するものではありません。[近隣メッシュの可用性チェック](https://github.com/Origami74/myco/pull/132)では、blob をダウンロードしたり公開 Blossom サーバーに接続したりせずに、ピアに blob の有無を問い合わせます。これらの上限付き HEAD リクエストにはメッシュの権限が必要です。保有者数は、成果物全体が引き続き利用可能であることの証明にはなりません。

このリリースでは、ローミング先キャリアのタイムアウトによって relay や成果物の検索が妨げられないように、[上流 DNS サーバーへ並行して問い合わせ、先に返った応答を使用します](https://github.com/Origami74/myco/pull/137)。Outbox からの公開は、一覧にあるすべての書き込み用 relay を対象とし、遅い接続先への配信はバックグラウンドで行われます。インターネットメッシュは引き続きデフォルトで無効であり、ウェブ上の画像は再起動をまたいで保持されません。

### Unfiltered

[Unfiltered 1.0.13](https://github.com/dmcarrington/unfiltered/releases/tag/v1.0.13)は、Android 写真クライアントに読み取り用・書き込み用 relay リストと outbox ルーティングを追加します。[リリースノート](https://njump.me/nevent1qqsy8287ykdstql8ec2udgr8slj3czzkkdkjjc36xwn4lnjrrhggfwgu8dmj2)では relay の役割を説明しており、リストのないアカウントはデフォルトの公開 relay 3つから利用を開始します。Nearby は粗い粒度の geohash と隣接セルを使用します。投稿への位置情報の追加はオプトインで、デフォルトでは無効です。それでも、それらの tag は地域を公開します。確認した公開処理の結果が意味するのは、ソケットへの送信キューに入ったということであり、relay による受理はまだ確認されていません。

### monostr

[monostr 0.17.0](https://github.com/schmidt1024/monostr/releases/tag/v0.17.0)では、ユーザーが個人用 watcher を通じて Monero のチップを受け取れるようになり、[0.18.0](https://github.com/schmidt1024/monostr/releases/tag/v0.18.0)では、新規設定時にチップの金額と通知の送信者名をデフォルトで非表示にします。画像はデフォルトでタップして読み込む方式となり、任意機能の Primal の件数表示とクライアント tag は無効になっています。ホスティングされた watcher は、登録ウォレットの秘密ビューキーを通じて、そのウォレットへのすべての入金を引き続き把握できます。金額が非表示でも、公開される受領記録には受取人、時刻、参照先の投稿が残ります。

### Grocery

[Grocery 1.0.2](https://github.com/Marc26z/nostr-grocery/releases/tag/v1.0.2)は、共有の暗号化された買い物リスト、パスキーに支えられた Nostr ID、リストごとの Marmot チャットを組み合わせています。ベアラーキーを貼り付けることでリストに参加でき、そのキーは閲覧と編集の権限を与えます。パスキーによるログインは、ブラウザーとプロバイダーが WebAuthn の擬似ランダム関数拡張に対応しているかどうかに依存します。メンバーの tag は引き続き relay から見えます。[バージョン 1.0.3](https://github.com/Marc26z/nostr-grocery/releases/tag/v1.0.3)は、復号済みの内容をローカルにキャッシュすることで、開き直した際もリストを保持します。これにより、relay がリストを再配信するまでキーしか残らない場合があった問題を修正しています。

### Roadstr

[Roadstr 1.1.0](https://github.com/roadstrapp/roadstr-app/releases/tag/v1.1.0)は、別の Roadstr クライアントの kind 1315/1316 を、意図された有効期間と確認ルールに従って読み取ります。コンパクトなコーデックは、実験的な MeshCore 無線と relay のブリッジ向けに、再構成可能な署名済みレポートを保持します。互換形式での公開と無線送信はデフォルトで無効であり、共有前に同意を求めます。無線レポートは、受信範囲内の誰に対しても位置、時刻、署名公開鍵を明らかにします。テストにはシミュレーションされた無線機を使用しており、実機、Android BLE、公開 relay への公開は未検証です。

### OUTKAST

[OUTKAST 1.1.3](https://github.com/Lwb89dev/outkast/releases/tag/v1.1.3)は、Android クライアントの記事コメントと引用投稿の処理を改善します。記事コメントは、記事をルート、コメントを親とする kind 1111 を使用し、通常のノートへの返信は引き続き kind 1 を使用します。引用の検出は q tag と、リンクを含む従来の e メンションの両方に対応し、新たに公開する引用には q tag を追加します。公開に失敗した場合、楽観的に反映したリアクションを元に戻します。

### Bookshelf

[Bookshelf 0.1.28](https://github.com/decent-newsroom/bookshelf-app/releases/tag/v0.1.28)では、章と子インデックスの両方を発行者の指定順に含む kind-30040 出版インデックスを、[入れ子構造のまま読み込む機能](https://njump.me/nevent1qqs8pukgjrnuzryv0z67lze2y0jsshepdckuss25qggvwn5skxqfa7gslzul0)について説明しています。オフラインコピーは、その階層構造と、各出現箇所にひもづくブックマークを保持します。更新時には座標で現在の改訂版を取得しますが、結果が不完全、古い、または取得に失敗した場合は、以前のダウンロードを保持します。再配信では、元の署名済み子孫要素を保持します。展開範囲に上限を設け、部分的な分岐も読めるようにすることで、構造が欠けたものを完成した本として表示しないようにしています。

### Ditto

[Ditto 2.45.0](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.45.0)は、コンテンツフィード全体で Global を Discover に置き換えます。Discover は、ユーザーがフォローしている人たちのフォロー先から投稿を集め、共通のつながりに基づいて順位を付け、ユーザー自身とすでにフォローしているアカウントを除外します。ログアウト中のユーザーと、誰もフォローしていないアカウントには、代わりに選定された初期ネットワークを表示します。これにより、デフォルトの発見範囲はソーシャルな近隣へと変わりますが、スパム耐性やそれらのアカウントの信頼性は、依然として別の問題です。

### Postr

[Postr 1.1.2](https://njump.me/nevent1qqsf4uu87v5r7awyfhktjqnuc9m6xzfngpvr7gj37zca05sx7lk03vqy4wq7x)は、下書きの保存から公開まで、選択したプロフィールの ID をメンションにひもづけたまま保持します。投稿作成画面は、署名と送信の間、アカウント、テキスト、メンション、添付ファイルを固定し、その操作が終わるまで受信した共有内容を保留します。再試行では、以前から保留中の投稿も含め、元の署名済み event を保持します。@ の後に名前を入力するだけでは不十分で、ユーザーはプロフィールを選択する必要があります。古い下書きですでに失われた ID は、再度選択する必要があります。

### Nostrautica

[Nostrautica Android 0.11.0](https://github.com/jooray/nostrautica/releases/tag/android-v0.11.0)は、コミュニティとそのミートアップを関連付けます。関連付けられたeventへの参加承認によって、再度の承認なしでコミュニティのメンバー資格を付与することもできます。参加申請フォームではこの点を明示し、申請者が辞退できるようにしています。既存の参加者には、ワンタップで応じられる招待が届きます。eventは独自の参加者、マッチング、チャットを維持し、コミュニティにはそのeventの一覧が表示されます。リリースノートでは、eventとコミュニティのコーディネーターが異なる場合への対応が説明されていますが、独立した相互運用性テストや暗号化テストが行われたことまでは示されていません。

### Minibits

[Minibits v0.4.4 beta 1](https://github.com/minibits-cash/minibits_wallet/releases/tag/v0.4.4-beta.1)は、Androidの[Nostr Wallet Connect](/ja/topics/nip-47/)による支払い処理が、ウォレットのバックグラウンド動作中に停止し、処理の蓄積によってアプリケーションが応答しなくなる不具合を修正します。このネイティブ版リリースには、過去5か月分の無線配信による変更がまとめて含まれています。[バージョン0.4.5 beta 1](https://github.com/minibits-cash/minibits_wallet/releases/tag/v0.4.5-beta.1)は、AndroidからiOSへのNFC転送を修正します。今後の無線配信アップデートには、このバージョンが必要です。これらはリリースで報告されている修正であり、バックグラウンド処理は引き続き端末のライフサイクル制限に左右されます。

### NoorNote

[NoorNote v1.9.0](https://github.com/77elements/noornote/releases/tag/v1.9.0)では、記事エディターからレシピを公開し、共有されたレシピパックを開き、フォローしている著者のレシピを閲覧できます。先週紹介されたウェブサイトカードとプロフィールグリッドが、relayのレート制限への対応やAndroidでの直接の`nostr:`リンクとともに、このリリースに搭載されました。ウェブサイトへのリンクは、そのサイトの内容を検証することとは別です。ゲートウェイ経由でアクセスすると、クリックによるリクエストがそのゲートウェイに伝わります。

### Gittr

[Gittr v1.0.2](https://github.com/arbadacarbaYK/gittr/releases/tag/v1.0.2)は、[NIP-46リモート署名](/ja/topics/nip-46/)を通じてAmberを利用し、NostrのGitフォージをAndroid向けにパッケージ化しています。このAPKは既存のホスト型`gittr.space`アプリケーションを開くため、ユーザーは引き続きそこで配信されるブラウザーコードとサービスの可用性に依存します。このラッパー内ではブラウザー拡張機能による署名は利用できません。セルフホスティングには、別途Gitをデプロイする必要があります。

### Dart NDK

[Dart NDK 0.11.0 開発版ゼロ](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.0)は、DartおよびFlutter向けツールキットの[認証同意ハンドラー](https://github.com/relaystr/ndk/pull/862)と、NIP-46署名器のrelay切り替えをプレリリースに取り込んでいます。これらの変更は先週、マージ済みの作業として紹介され、今回リリースされました。署名器は差し替えられたrelayリストに追従できますが、アプリケーション側でそのリストを永続化する必要があります。[開発版ワン](https://github.com/relaystr/ndk/releases/tag/v0.11.0-dev.1)では、relay情報内の文字を含むNIP識別子への対応が追加されています。どちらのリリースにも、組み込みに関する破壊的変更が含まれます。

### Cambium

[Cambium v0.9.0](https://github.com/forgesworn/cambium/releases/tag/v0.9.0)は、ネイティブAndroidアプリに[4種類の承認期間](https://github.com/forgesworn/cambium/pull/32)を提供します。1回限り、1時間、1日、または無期限です。権限の付与範囲は、操作とeventのkindごとに限定されます。Cambiumはリモート署名を通じてHeartwoodハードウェア署名器にリクエストを転送しますが、どのリクエストに署名するかは引き続きHeartwoodが決定します。ウェブサイトへの承認は引き続き1回限りです。ペアリング済みの署名器には、テストと再接続の操作、対応するトランスポートrelayの更新、機密情報を伏せた診断情報が追加されます。[NIP-55によるAndroid署名](/ja/topics/nip-55/)のバッチ処理では、リクエストの順序と個別の拒否が維持され、再利用されて解釈が曖昧になったインテントについては、明示的な1回限りの同意が求められます。

### Grain

[Grain v0.8.1](https://github.com/0ceanSlim/grain/releases/tag/v0.8.1)は、複数ユーザーにサービスを提供するアプリケーション向けに、Goクライアントライブラリの[NIP-42 relay認証](/ja/topics/nip-42/)を修正します。各`UserContext`は、専用の認証済み接続、relay設定、接続の保持を管理し、共有プールは認証を一切行いません。ライブラリは受信したIDと署名を検証し、サブスクリプションとの一致を確認し、tagおよび時刻のフィルターを正しくシリアライズします。認証を利用する呼び出し元は、`UserContext`に移行する必要があります。relayの保存処理と配信処理に変更はなく、認証には引き続き接続開始時のチャレンジが必要です。

### Nmail

暗号化メールクライアントの[Nmail v0.18.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.18.0)は、見知らぬ送信者を「リクエスト」に、ブロック済みの送信者を「スパム」に振り分けます。承認とブロックはデバイス間で同期されます。既存の受信トレイ内の送信者にも承認が必要で、「すべて承認」も利用できます。「スパム」は通知せず、承認待ちのリクエストでは同じ送信者について通知を繰り返しません。返信には受信時のアイデンティティを使用します。リセットまたはログイン後のメールボックス復元の修正に加え、プライベートrelayの管理、同期コードのコピー前のデバイスロック確認、共有テーマ、より充実した連絡先情報の保持、Windowsインストーラーが含まれます。

### Meiso

[Meiso v1.5.0](https://github.com/higedamc/meiso/releases/tag/v1.5.0)は、Nostrで同期するタスクマネージャーに、暗号化コメントと未読表示を搭載します。コメントには[NIP-44暗号化](/ja/topics/nip-44/)を施したアドレス指定可能なkind 35002のeventを使用し、タスクとの関連付けは暗号文の中に保持します。このリリースは、[オフラインでの送信](https://github.com/higedamc/meiso/pull/212)、再接続時の未取得分の取得、保存済みrelayを使用した起動、空のリストの伝播を修正します。また、部分的な同期によってタスクが削除されることも防ぎます。未読表示と未取得分の取得機能は、アプリケーションが閉じている間の通知サービスを追加するものではありません。

### Haps

実験的なソフトウェアインストーラーの[Haps v0.1.13](https://github.com/mmalmi/haps/releases/tag/v0.1.13)は、デフォルトで、ユーザーの[信頼の網](/ja/topics/web-of-trust/)に属する人による、その正確なリリースを対象とした監査を必須とします。監査では、固定されたソースと再ビルドした成果物を比較でき、非公開のままにすることも公開することもできます。[バージョン0.1.14](https://github.com/mmalmi/haps/releases/tag/v0.1.14)では、名前だけを指定してインストールする際に、ユーザーに発行者の確認を求めます。自動処理では発行者の指定が必須です。監査は根拠を提供しますが、ネイティブプログラムとビルドレシピは引き続きサンドボックスなしで実行されます。監査要件は1回の操作に限って回避できますが、署名、完全性、発行者確認のチェックは維持されます。

### Sidecar

[Sidecar v1.16.0](https://github.com/dmnyc/sidecar/releases/tag/v1.16.0)は、ブラウザー拡張機能型のソーシャルクライアントに、署名付きチャット、リアクション、zapを備えた[ライブ配信の発見と再生](https://github.com/dmnyc/sidecar/pull/479)を追加します。保存した配信ブックマークは、暗号化されたアカウントのバックアップと復元に対応し、非公開の通知ミュート設定でアラートを制御できます。検索にはフォローとミュートの操作が追加され、自動ロックとウォレット履歴の更新にも変更が加えられています。

### Ants

検索インターフェースの[Ants v0.7.0](https://github.com/dergigi/ants/releases/tag/v0.7.0)は、ログインなしで[構造化検索を振り分けます](https://github.com/dergigi/ants/pull/316)。[NIP-65 relayリスト](/ja/topics/nip-65/)を通じて、著者が公開している書き込み用relayと、言及されたユーザーの読み取り用relayへ送ります。探索では、参照するアイデンティティとrelayの数を制限し、キャンセルまたはタイムアウト時に停止します。リストがない場合は、フォールバックの経路を維持します。テキストクエリには、引き続き検証済みの[NIP-50検索relay](/ja/topics/nip-50/)を使用します。

### soyLI

[soyLI v0.27.0](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.27.0)は、提案段階の[NIP-5Dアプリケーション](/ja/topics/nip-5d/)向けのnapplet公開・再生ツールであり、キーバインドと、GitホスティングサービスGRASPを通じたフォーク不要の提案を追加し、再試行時にはリビジョンの厳密な一致を確認します。[v0.26.0リリース](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.26.0)では、最初の公開後に、署名済みリリースを検証済みのアウトボックスrelayへ配布します。削除時には配布を試みた宛先を追跡しますが、把握していないコピーを回収することはできません。[バージョン0.26.1](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.26.1)は、新規ビルドと公開に対する25 MiBの上限を維持しつつ、読み取り、再生、レビューの容量枠を100 MiBに引き上げます。その後の[直接埋め込む表示用メタデータ](https://github.com/zeSchlausKwab/napplet-soy/pull/14)では、著者のカバー画像とクリップを署名済みマニフェストに直接配置し、付随するeventを廃止します。凍結された旧ジョブは引き続きサポートされます。このバージョン管理されたSoy拡張には対応するリーダーが必要であり、固定されたNIP-5D仕様には含まれません。

### nostream

relayサーバーの[nostream v3.3.0](https://github.com/cameri/nostream/releases/tag/v3.3.0)は、WebSocketの読み書きの往復時間、任意の認証の検出、ミラー先の検出を行う[NIP-66 relay監視](/ja/topics/nip-66/)のプローブを追加しました。観測された動作が[NIP-11 relay情報](/ja/topics/nip-11/)と一致しない場合に警告します。レート制限されたOKレスポンスには、ミリ秒単位のバックオフ時間を含む任意の第5要素を付加できます。[バージョン3.4.0](https://github.com/cameri/nostream/releases/tag/v3.4.0)は、IPごとのメッセージ制限によって`REQ`または`COUNT`が拒否された場合、[CLOSEDレスポンス](https://github.com/cameri/nostream/pull/821)の第4要素としてミリ秒単位のバックオフ時間を追加します。[PostgreSQLによるnegentropy照合のコア](https://github.com/cameri/nostream/pull/809)と、順序付けされたeventインベントリも搭載しています。[NIP-77](/ja/topics/nip-77/)のrelay間でやり取りするメッセージと対応機能の告知は、引き続き別の作業です。

### Bark

[Bark v1.3.15](https://github.com/forgesworn/bark/releases/tag/v1.3.15)では、リモート署名の承認にキーボード操作、eventとアイデンティティの明示的な確認、[1分、5分、10分の判断時間](https://github.com/forgesworn/bark/pull/52)が用意されました。バックグラウンドで期限を管理し、期限切れの判断とキュー内のリクエストを拒否します。判断結果の送信に失敗した場合は、再試行できるようポップアップを開いたままにします。[バージョン1.3.17](https://github.com/forgesworn/bark/releases/tag/v1.3.17)では、署名者とのハンドシェイクが完了すると[NIP-07ブラウザー署名](/ja/topics/nip-07/)が利用可能になり、任意の診断処理はその後も継続します。更新後には既存のタブのブリッジを復元します。

### Mostro

[Mostro v0.19.3](https://github.com/MostroP2P/mostro/releases/tag/v0.19.3)は、未完了の注文がなくても、本人認証済みのユーザー自身の評判に関するリクエストに応答します。このピアツーピア取引所は、リクエスト元の取引キーに非公開で返信し、[マージ済みのCLIコマンド](https://github.com/MostroP2P/mostro-cli/pull/203)からその問い合わせを実行できます。評判のインポートは引き続きプレビュー段階で、インポート処理は未実装のため、運営者は無効のままにしておく必要があります。[その後マージされた変更](https://github.com/MostroP2P/mostro/pull/1057)では、Lightningエスクローのガーディアン・マージンを公開し、安全でない設定を拒否します。最小値の18ブロックは、LNDのデフォルトの保留期限設定を前提としています。

### Elisym

[Elisymのcommerce 0.11.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.11.0)は、販売者の売上から手数料を差し引く方式に対応しています。署名付きのストアプロフィールのtagで分割支払いへの対応を宣言し、手数料が適用される場合は非対応のストアを拒否します。[マージ済みの管理機能の変更](https://github.com/elisymlabs/elisym/pull/170)では、Nostr relayから注文と商品情報を読み取ります。ストアの秘密鍵の入力を求めるため、配信されるブラウザーコードと拡張機能を信頼する必要があります。ローカルの管理機能は引き続き利用可能です。ホスト型のデプロイとメインネットでの手数料の有効化は、引き続き未検証です。[Merchant-node 0.10.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/merchant-node%400.10.0)は台帳をアップグレードしますが、ダウングレードには対応していません。

### Routstrd

[Routstrd v0.4.16](https://github.com/Routstr/routstrd/releases/tag/v0.4.16)は、[Nostr Wallet Connect](/ja/topics/nip-47/)による残高補充がタイムアウトした直後に、支払い可能な別のインボイスが生成されることを防ぎます。支払いが成功または失敗するまで、[既存のミント操作を確認](https://github.com/Routstr/routstrd/pull/144)します。状態を取得できない場合は、補充を一時停止したままにします。推論ゲートウェイでは、Nostrのレビューラベルに基づいてプロバイダーを有効にし、実験的なラベルには明示的なオプトインを必要とします。[バージョン0.4.17](https://github.com/Routstr/routstrd/releases/tag/v0.4.17)には、これを支えるSDKが含まれています。未決済の操作に対する保護はメモリ内にのみ保持されるため、デーモンを再起動すると失われます。

### Buzz

[Buzz desktop 0.5.28](https://github.com/block/buzz/releases/tag/desktop-v0.5.28)では、認証済みのスタッフが接続を切り替えずに、relay上の[すべてのコミュニティを閲覧・モデレーション](https://github.com/block/buzz/pull/8027)できます。管理操作では、確認したコミュニティ、relay、署名者が保持されます。認証が無効でも、コンソールは閲覧用として利用できます。別途[マージされたrelay側の変更](https://github.com/block/buzz/pull/8197)では、非公開の投稿者レコードに対する適切なtag付きの削除eventを、クエリとリアルタイム配信の両方で非表示にします。このサーバー側の修正にはデプロイが必要であり、すでに開示されたコピーや、過去のtagのない削除レコードは修正の対象外です。

### Earthly

[Earthly v0.1.21](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.21)では、ユーザーが[公開Nostr地図データセットをウェブサイトに埋め込める](https://github.com/zeSchlausKwab/earthly/pull/35)ようになり、プレビューと、外観および初期カメラ位置の設定機能が用意されています。Maps MCP連携はチャットから地図を作成・公開し、その後に共有リンクや埋め込みを生成します。この連携は、引き続き個人向けの接続型プラグインの試験運用段階です。埋め込みは、地物数300、サイズ48 KiBまでのインラインデータセットに対応しています。非公開、未公開、blobを使用したデータセットは対象外です。

### Milk Market

[Milk Marketのmobile v0.3.0](https://github.com/shopstr-eng/self-sown/releases/tag/mobile-v0.3.0)では、ウェブ版エディターと同じセクションとフィールドを備えた、本格的なストアフロントのデザインエディターが販売者向けアプリに導入されました。商品ごとのページデザインで、メタデータやソーシャル共有用画像を含め、テーマとセクションの選択を上書きできます。このリリースには、モバイル版とウェブ版の設定の整合性を保つためのチェックが追加されています。[バージョン0.3.1](https://github.com/shopstr-eng/self-sown/releases/tag/mobile-v0.3.1)では、モバイル版のプレビューカードのコントラストを修正しています。Android向けのダウンロードは各リリースに添付されており、iOS版はTestFlightで利用できます。

### Zeus

[Zeus v13.2.3](https://github.com/ZeusLN/zeus/releases/tag/v13.2.3)には、先週取り上げた[LDKのルーティング手数料の修正](https://github.com/ZeusLN/zeus/pull/4353)が含まれ、リリース済みとなりました。LDKを基盤とするNostr Wallet Connectサービスでは、報告されたルーティング手数料をレスポンスと支出記録に含められます。予算チェックは引き続き決済前のインボイス金額を対象とし、丸め処理された手数料は後から差し引かれます。また、ルーティング手数料には別途1,000 satoshiの上限があります。このリリースでは組み込みのLNDも更新され、rust-lightningのセキュリティ修正も含まれていますが、実機のNWCデバイスでの検証は引き続き未確認です。その後[マージされたZaplockerの削除](https://github.com/ZeusLN/zeus/pull/4933)では、Nostrによる証明と引き換えのフローが廃止されます。そのサーバーに支払いが保留されている状態でアップグレードすると、引き換えができなくなります。送信者は保留インボイスの期限切れと返金を待つ必要があります。この廃止はv13.2.3には含まれておらず、展開にはサーバーの無効化と既存ユーザーへの警告が必要です。

## 開発中

### nosvelte

[nosvelteのevent検証機能の修正](https://github.com/akiomik/nosvelte/pull/162)では、署名を検証する前に、eventに付与されたIDを、そのフィールドから算出した正規のハッシュと照合します。このSvelteライブラリのデフォルトの検証機能は、以前はIDが差し替えられていても、フィールドに正しい署名があれば受け入れていました。そのため、コンテンツが別のeventの識別子を占有し、置換処理を妨げることが可能でした。マージされた変更は、デフォルトの検証機能を使うバージョン1のリクエスト経路と送信経路に適用されます。レガシーのエクスポートやカスタム検証機能が[NIP-01のevent形式](/ja/topics/nip-01/)に適合することを保証するものではありません。その後の[リクエストフィルターの修正](https://github.com/akiomik/nosvelte/pull/171)では、relayからのeventのフィールドを検査してコピーした後に照合します。不正な形式のデータによって、デフォルトのプロバイダーのサブスクリプションが終了したり、次の有効なeventが破棄されたりすることはなくなりました。呼び出し側が提供するエンジンクライアントでは、依存関係による従来の照合動作が残る場合があります。

### nostter

nostterは、[外部から提供されたrelayヒントを制限](https://github.com/SnowCait/nostter/pull/2684)し、安全なWebSocket URLのみを許可して、ローカルのホスト名とグローバルではないIPアドレスを拒否します。アカウントで選択したローカルのrelayとリモート署名者のURLは、従来の処理経路を維持します。DNSリバインディングはチェックの対象外です。このウェブクライアントは、閲覧者が「表示」を押した後にのみ、[実験的な、分離されたコンテンツ警告のペイロードを読み取り](https://github.com/SnowCait/nostter/pull/2680)、参照先のevent ID、投稿者の一致、および元のeventのkindと一致する`k` tagを確認します。リアクションと返信は元のeventを対象とします。これらのマージ済みの変更によって、現在の[NIP-36](/ja/topics/nip-36/)の公開形式が変わることはありません。

### Coracle

[Coracleのリストエディター](https://github.com/coracle-social/coracle/pull/679)は、非同期のデコードが完了するまで待ってからフォームを描画することで、編集と削除を復旧します。以前は、編集するとリストのフィールドが失われ、保存でも削除でもeventが公開されませんでした。

### Routstr Core

[Routstr Coreの現行バージョン0.5.0のソース](https://github.com/Routstr/routstr-core/releases/tag/v0.5.0)では、[自動生成されたNostr秘密鍵のログ記録を停止](https://github.com/Routstr/routstr-core/pull/812)し、[初回起動時の公開IDを維持](https://github.com/Routstr/routstr-core/pull/818)します。[プロバイダーの告知](https://github.com/Routstr/routstr-core/pull/823)では、localhostと、プライベートアドレスまたはリンクローカルアドレスを直接記述したHTTPアドレスが除外されます。このチェックではホスト名の名前解決は行われません。現行のtagには、記録上の公開日である10月7日より後にマージされた変更が含まれているため、過去のバイナリとデプロイの状況は未検証のままです。以前に露出したログについては、引き続き運用者による確認が必要です。

### Alby Hub

[Alby Hubのインボイス認可に関する変更](https://github.com/getAlby/hub/pull/2629)により、決済とキャンセルの対象は、要求元のアプリが作成したインボイスに限定されます。このセルフホスト型ウォレットは、[NIP-47、Nostr Wallet Connect](/ja/topics/nip-47/)を通じてアプリ接続を提供します。ある接続が自身のインボイスを管理できるからといって、別のアプリのインボイスを操作する権限まで与えてはなりません。別の[分離接続のプライバシー修正](https://github.com/getAlby/hub/pull/2621)では、分離接続のブラウザー上の成功時処理経路から、メインウォレットのLightningアドレスが削除されます。

### nak

[マージ済みのnakのrelayコマンド](https://github.com/fiatjaf/nak/pull/222)は、接続、読み取り、書き込みにかかる時間とrelay情報を調査し、署名されていないkind 30166の発見用eventを出力します。その結果を`nak event`にパイプで渡すことで署名と公開が行われ、同じターミナルツールで[NIP-66によるrelay監視](/ja/topics/nip-66/)を定期実行できます。実際に観測された認証や制限に関する応答は、relayが公表する情報より優先されます。書き込みの調査には、使い捨ての鍵で署名した一時的なeventを使用します。kind 10166のモニター告知は、引き続き別の操作です。

### Kehto

[Kehtoのマニフェスト検証](https://github.com/kehto/web/pull/277)は、実行前に、現行形式の単一アーティファクト用署名付きマニフェストとアーティファクトのバイト列を検査します。旧形式の解析は別に保たれています。nappletシェルは[推奨ハンドラーも検証](https://github.com/kehto/web/pull/294)し、保存済みの選択と競合する場合はユーザーに確認を求め、受け入れた呼び出しURLを消費済みにすることで繰り返し配信を防ぎます。マニフェスト検証で確認するのは発行者のIDとアーティファクトのバイト列であり、アプリケーションコードの安全性を保証するものではありません。[ゲームパッドのスナップショット](https://github.com/kehto/web/pull/297)は、フォーカスと表示状態に従うようになりました。Paja/playgroundのフレームは、アプリケーションコードの実行前に、ネイティブのゲームパッド、HID、USBへの直接アクセスをブロックし、ホストを介したアクセスだけを残します。利用側には対応するホストパッケージが必要であり、シェルの準備完了状態は別の機能です。その後の[Pajaの受け入れ判定の変更](https://github.com/kehto/web/pull/305)では、必須とされた実験的ドメインが利用できない場合に警告を出しつつ、読み込みを許可します。ただし、それらのドメインは引き続きAPIも権限付与も提供しません。

### napplet SDK

[napplet SDKは、URIベースの呼び出しと保持された配信を実装しています](https://github.com/napplet/web/pull/228)。[公開用メタデータは単独のHTMLでも保持され](https://github.com/napplet/web/pull/226)、[任意のアプリケーション参照](https://github.com/napplet/web/pull/239)によって、アーティファクトのハッシュを変更せずに、マニフェストを署名付きの掲載情報やスクリーンショットに結び付けられます。アプリケーション参照の形式は、引き続き提案段階です。参照シェルのテストでは、本番環境での発見、インストール、署名検証はホストに委ねられています。

### rust-nostr

RustのNostrライブラリである[rust-nostrは、relayの終端エラーとともに、途中までのダウンロード進捗を保持します](https://github.com/nostrdevkit/nostr/pull/1483)。失敗したrelayは失敗集合に残るため、呼び出し側は、同期が途中で停止した証拠を失うことなく、すでに受信したeventを利用できます。

### Pensieve

[Pensieveの照合の安全性に関する修正](https://github.com/andotherstuff/pensieve/pull/92)は、[欠落eventの除外に関する作業](https://github.com/andotherstuff/pensieve/pull/90)に続くものです。relayとアーカイブのツール群は、失敗を分類する前に、欠落しているIDを正確に指定して再要求し、クエリの件数上限によって末尾が切り詰められたことを誤った除外判定につなげないようにします。一時停止の集計はジョブごとに行われ、すでにアーカイブ済みのeventは別に扱われます。完了したジョブにも、欠落eventの明示的な記録が残る場合があります。完了したという事実だけでは、アーカイブが完全であることは確認できません。

[Premium Primalとの継続的な照合](https://github.com/andotherstuff/pensieve/pull/84)は10月12日に有効化されました。運用者の[デプロイ記録](https://github.com/andotherstuff/pensieve/pull/93)によると、修正済みの両バイナリのデプロイと、失敗に基づく一時停止の有効化は10月13日に行われました。その後の[除外情報の引き継ぎ](https://github.com/andotherstuff/pensieve/pull/95)では、同じrelayかつ期間が重なる場合に、元の検証済み除外情報だけを再利用し、連鎖的な引き継ぎと新たに混在したIDを除外します。その[デプロイは同日午後に記録されました](https://github.com/andotherstuff/pensieve/pull/97)。[アーカイブの事前チェックとキャッシュ停止の修正](https://github.com/andotherstuff/pensieve/pull/98)は、[10月14日にデプロイされました](https://github.com/andotherstuff/pensieve/pull/99)。その後の[引き継ぎの優先順位に関する修正](https://github.com/andotherstuff/pensieve/pull/103)はマージ済みですが、出典の記録上ではまだデプロイされていません。

### njump

Nostrのウェブビューアーである[njumpは、上書き用ファイルが指定されていない場合に、組み込みのrelayデフォルト設定を復元します](https://github.com/fiatjaf/njump/pull/173)。また、[同時実行されるMarkdownレンダラー](https://github.com/fiatjaf/njump/pull/171)と[タイムアウト時のレスポンスヘッダー](https://github.com/fiatjaf/njump/pull/169)をそれぞれ分離し、引用された長文eventの描画中や同時リクエストの処理中にプロセスをクラッシュさせる可能性のあった競合を修正します。これらはマージ済みのサーバー側の変更であり、稼働環境へのデプロイは未検証です。

### Nostr Components

[Nostr Componentsのzap署名の修正](https://github.com/saiy2k/nostr-components/pull/187)により、選択された署名者が拒否すると支払いフローが停止します。埋め込み可能なソーシャルウィジェットは、拒否後にランダムな匿名IDで代用しなくなりました。[受領証の集約](https://github.com/saiy2k/nostr-components/pull/197)では、[NIP-57のzap受領証](/ja/topics/nip-57/)を検証してから、relay上の複製、インボイス、リクエストIDの重複を排除します。

### rx-nostr

リアクティブなクライアントライブラリである[rx-nostrのバージョン4の検証に関する変更](https://github.com/penpenpng/rx-nostr/pull/207)では、JavaScriptとWebAssemblyの両方で、正規のevent構造、ID、署名を一貫して検査します。リクエスト条件のリストが空の場合は何にも一致せず完了します。従来の送信処理は、送信先がない場合に失敗を報告します。公開のオブザーバーは確定結果を変更できず、破棄されたリクエストの子孫は再開できません。[有限のクエリ区間](https://github.com/penpenpng/rx-nostr/pull/213)により、指定されたすべての区間が終了した後に、過去方向へのクエリを完了できます。これらの変更は、APIに破壊的変更を含むプレリリースの[4.0.0 beta 2](https://github.com/penpenpng/rx-nostr/releases/tag/rx-nostr%404.0.0-beta.2)に含まれています。

### eHagaki

ソーシャルクライアントの[eHagakiは、段階的なアウトボックス配信を追加](https://github.com/Lokuyow/ehagaki/pull/268)し、署名前に投稿者の送信先relayを確定します。センシティブな投稿のフローでは、各relay自身の受領確認を使い、参照構造より先にペイロードをそのrelayへ送信します。ペイロードだけが成功した場合は、投稿作成画面を保持します。[投稿履歴全体のスキャン](https://github.com/Lokuyow/ehagaki/pull/312)は、検証済みの結果を逐次保存します。スキャンが完了と表示されても、不確かな範囲は未確認のまま残り、その説明を表示する情報コントロールが用意されています。[Citrineのローカルrelay対応](https://github.com/Lokuyow/ehagaki/pull/315)では、検証済みの閲覧範囲を保持し、外部への公開に成功した後に、署名済みeventをそのままアーカイブします。ローカルでの受領確認によって外部への送信失敗が成功に変わることはなく、オフライン公開キューが追加されるわけでもありません。[アップロード済みメディアの管理](https://github.com/Lokuyow/ehagaki/pull/321)では、対応するNIP-96およびBlossomサーバー上のアップロード済み画像や動画を一覧表示し、削除できます。[その後のデータベース移行](https://github.com/Lokuyow/ehagaki/pull/325)では、下書きと削除リクエストを保持しつつ、キャッシュされた表示履歴と投稿履歴をリセットします。また、消去後に、以前からキューに入っていた同期結果によって履歴が再び埋められることも防ぎます。

### Formstr

[Formstrの送信結果の修正](https://github.com/formstr-hq/nostr-forms/pull/508)では、どのrelayにも受け入れられなかったフォーム回答を拒否します。このNostrフォームアプリケーションは、relayごとの結果を表示し、入力済みの回答を保持したまま再試行できるようにします。Webhookと確認ページは受け入れを待ち、SDKにも同じチェックが適用されます。relayからの確認応答は依然として長期保存の保証とは異なりますが、公開が完全に失敗した場合に成功メッセージが表示されることはなくなります。

### Auditable Voting

[Auditable Votingに、任意で利用できる非公開ワーカーによる投票の一括処理が追加されます](https://github.com/tidley/auditable-voting/pull/35)。主催者が署名した定義で、ワーカーのID、DM用relay、公開のしきい値または期限を指定します。投票者は[NIP-17でギフトラップされた投票](/ja/topics/nip-17/)を送信し、そのワーカーに照らして受領証を認証します。委任では、キューへの追加と公開の両方を許可する必要があります。公開される投票にはワーカーのIDが使われます。ワーカーは送信内容を読むことができ、期限によって公開されるバッチは少数になる場合があります。有効な非公開経路が見つからない場合、調査対象のクライアントは公開送信にフォールバックします。これはマージ済みの開発作業です。

### MintRadar

[MintRadarに、オプトイン方式のギフトラップされたアラートが追加されます](https://github.com/hroomnik007/MintRadar/pull/122)。対象は、mintまたはmeltの問題、古いソフトウェア、およびこれらの操作に対するサポートの喪失です。Cashu mintディレクトリでは、[ウォッチリストの操作をこれらの通知設定に接続し](https://github.com/hroomnik007/MintRadar/pull/123)、サーバーの応答後に設定を確定します。アトミックな送信権の確保によって、重複して実行される監視処理が同じアラートを送るのを防ぎ、relayへの公開に失敗した場合は、その権利を解放して再試行できるようにします。[NIP-17の非公開メッセージ](/ja/topics/nip-17/)が通知内容を保護しますが、relayが受け入れても、受信者が読んだかどうかは確認されません。

### Nostr Docs

[Nostr Docsのローカルrelayへの移行](https://github.com/formstr-hq/nostr-docs/pull/65)では、共同編集用Markdownエディターの読み書きを、IndexedDBのeventキャッシュと再試行用送信トレイを備えたWeb Worker経由にします。ドキュメントのタイトルとtagは再読み込み後も保持され、連続するメタデータ編集には増加するタイムスタンプが付くため、1秒以内に行われた2回の編集も区別されます。既存の暗号鍵ストレージはそのまま維持されます。ネットワークプールへのフォールバックにはワーカーの送信トレイの永続性がなく、キューに入れた公開処理を受け付けたことは、relayが受け入れたことを意味しません。

### Pakstr

[Pakstrのネイティブなローカル署名機能](https://git.nostrdev.com/stuff/pakstr/pulls/105)により、Androidアプリケーションシェルが端末上でNostrアカウントを作成できるようになります。鍵はネイティブ層に保持され、Android Keystoreで保護されたラッピング鍵によって暗号化されます。署名結果は、Webアプリケーションに返される前に検証されます。シェルは[NIP-07のブラウザー署名](/ja/topics/nip-07/)と暗号化されたリクエストに対応します。署名機能の選択画面は必要になった時点で開かれ、同時に発生するリクエストを調整します。

### Nostr WoT SDK

ウェブ・オブ・トラストのライブラリである[Nostr WoT SDKは、認証への同意の対象を拡張し](https://github.com/nostr-wot/nostr-wot-sdk/pull/15)、型付けされたネイティブおよびリモートのリクエスト元にも対応します。確認画面を表示する前に保存済みの拒否を確認し、再利用可能な同意は、リクエスト元のトランスポートと宛先に結び付けられます。Webリクエストは、引き続きデフォルトで1回限りです。[管理型のBlossomアップロード](https://github.com/nostr-wot/nostr-wot-sdk/pull/13)では、不変のバイト列を検証し、キャンセルに対応し、アクティブなセッションが変わると停止します。また、認証はサーバーに結び付けられ、リダイレクトには制限が設けられます。

### NosTube

[NosTube v0.2.49](https://github.com/flox1an/nostube/releases/tag/v0.2.49)は、デスクトップ向けインストーラーを提供します。これとは別に、マージ済みのサーバー側の作業で、[永続性のある予約公開が追加されます](https://github.com/flox1an/nostube/pull/126)。eventは予定時刻より前に署名され、SQLiteに保存されたうえで、停止期間後に未処理分を追いつかせるワーカーによって公開されます。[編集と削除のフロー](https://github.com/flox1an/nostube/pull/124)は、削除記録、ミラーへの配信、所有ファイルのクリーンアップを追跡します。[初回セットアップ](https://github.com/flox1an/nostube/pull/134)では、ユーザーのブラウザー署名機能とサーバー管理のチャンネル鍵を区別します。過去の所有者不明のblobは、引き続き自動クリーンアップの対象外です。

### diVine

[diVine 1.0.24](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.24)では、クレジット表記を伴う非公開のクリップ共同制作と、署名付きの撮影・編集来歴の確認が追加されます。視聴者が選択した翻訳字幕は、翻訳待ちまたは未検証の間、元の字幕にフォールバックします。これらの来歴確認は、録画が未編集であることを保証するものではありません。

この短編動画クライアントの[ルーティングの変更](https://github.com/divinevideo/divine-mobile/pull/9884)では、テキストおよびビデオチャットのメッセージについて受信者の受信箱用relayを参照し、配信結果が不確かな場合はその状態を保持します。[送信者用コピーの処理](https://github.com/divinevideo/divine-mobile/pull/10006)により、ユーザー自身のグループメッセージを、そのユーザーのほかの端末にも表示できるようになります。以前に破棄されたコピーを表示するには、アカウントを再インポートする必要があります。[一部への送信後にキャンセルされたグループ送信](https://github.com/divinevideo/divine-mobile/pull/10031)では、「全員には送信されていません」という記録が保持されます。キャンセルは終端状態であり、これらの記録から再試行することはできません。グループの作成と、相手が新たに開始したルームの認識は、引き続き[デフォルトで無効のフラグの背後にあります](https://github.com/divinevideo/divine-mobile/pull/10020)。

その後のメインブランチの変更では、[中断されたデータベース復元のコピーを一時キャッシュの外に保持し](https://github.com/divinevideo/divine-mobile/pull/10118)、[再構築中も予約投稿、キュー内の通報、プロフィール編集、削除済みチャットの記録を保持します](https://github.com/divinevideo/divine-mobile/pull/10115)。[送信期限にはrelayへの再接続も含まれ](https://github.com/divinevideo/divine-mobile/pull/10127)、中断された送信を再試行するまでのしきい値が160秒から137秒に短縮されます。[インデクサーの受信箱検索は、上限を設けた別のプールを使用し](https://github.com/divinevideo/divine-mobile/pull/10116)、フィードの読み取り待ちに巻き込まれるのを防ぎます。また、確認前に連絡先リストが変わっても、[フォロー操作は選択したアクションを保持します](https://github.com/divinevideo/divine-mobile/pull/10147)。これらの後続のマージでは、再接続が遅い場合にrelayからの確認応答を待てる時間が短くなります。データベースの修復で、以前に失われたデータを復元することはできません。その後に追加された[オプトイン方式の録画コピー](https://github.com/divinevideo/divine-mobile/pull/10110)により、AndroidとiOSのギャラリーバックアップで、新たに録画したクリップを保存できるようになります。署名付きの来歴がないコピーには警告が表示され、再インポートできません。この機能はデフォルトで無効で、追加のストレージが必要です。

### Conduit

[Conduitのコマースアプリケーションに、共通の永続的な受信箱が追加され](https://github.com/Conduit-BTC/conduit-mono/pull/616)、MarketとMerchantの間で暗号化されたメッセージの配信と復旧が維持されます。送信者自身へのコピーが失敗しても、受信者側relayによる受け入れは保持され、復旧時には同じバイト列を再利用することで、意味上の二重送信を避けます。[署名機能を利用した共通ウォレット](https://github.com/Conduit-BTC/conduit-mono/pull/635)が両アプリケーションを接続します。この復旧経路では、復旧用の平文を署名機能に委ねます。ソースへの統合だけでは、実稼働へのデプロイも、実資金を使った受け入れテストも確認できません。[独立したrelay許可](https://github.com/Conduit-BTC/conduit-mono/pull/645)は、複数のアカウント経路が同じURLを共有していても維持されます。ある経路を無効にしても、別の署名済みrelayリストや受信箱の許可が消去されることはなくなり、認証が必要な読み取りや不完全な読み取りは、利用不可という結果を保持します。[マージ済みの決済ルーター](https://github.com/Conduit-BTC/conduit-mono/pull/613)は、購入者が承認した1回の資金支払いを、販売者と供給者へのLightning支払い、続いてConduit手数料へと分割し、支払い意図との厳密な照合と、共通のNostr受信箱を通じた暗号化された復旧を行います。本番環境とステージング環境での実行は、引き続き無効です。プロバイダー側での完了は、受取人による受領請求や支払いの消し込みを証明するものではありません。

### Bitcredit

[Bitcreditの永続化データの暗号化](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1041)は、個人IDのニーモニックを使用して、電子手形アプリケーションのID、会社、手形の各鍵を、Nostr再送キューも含めて保護します。初期化には、一致するニーモニックが必要です。[インスタンス管理](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/1043)により、testnetとmainnetのインスタンスが、1台の端末上でバックグラウンドのNostrサブスクリプションをそれぞれ独立して実行し続けられるようになります。

## 新しいプロジェクト

### Submarine

[Submarine 0.1.0](https://github.com/nogringo/submarine/releases/tag/v0.1.0)では、暗号化された保管庫をNostr経由で同期するパスワードマネージャーがリリースされました。外部署名ツールに対応し、同時に作成された項目の複数バージョンを保持するほか、Bitwarden JSONのインポートとエクスポートにも対応しています。変更はrelayによる受理を待つ前にローカルに保存されます。このリリースにはAndroid、デスクトップ、CLI向けのダウンロードが用意されています。プロジェクトはまだ開発初期段階にあると説明し、重要なパスワードには実績のあるマネージャーを使うよう勧めています。リリースタグ時点のプロトコル仕様はまだ空のままです。[Webストレージ](https://github.com/nogringo/submarine/blob/v0.1.0/apps/app/README.md)では、保護対象のデータと同じ場所に暗号鍵が保存されます。

### cl-marmot

[cl-marmot](https://github.com/modus-lisp/cl-marmot/blob/5dd9dea97ece82b0e4cc08f0c893397fbb333a5b/README.md)は、Nostr上で動作するMLSグループチャットのCommon Lisp実装を追加しています。10月9日のコードでは、競合するCommitの収束と、暗号化されたBlossom添付ファイルが追加されました。作者は、MDKのwnコマンドラインクライアントとの相互運用性テストを実施したと報告しています。この実装は監査を受けておらず、アカウント鍵とメッセージログは保存時に暗号化されません。時間制限付きの収束ウィンドウ、ロールバック可能範囲を超えたリプレイ、グループの解散は未実装です。確認したテストハーネスでは、使い捨てのローカルrelayが使用されています。

### nalgorithm Android

[nalgorithmのAndroidリリース](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.0)は、好みに基づいて順位付けしたNostrフィードと、オフライン再生できるバックグラウンド音声ダイジェストを生成します。ユーザーは、Lightningで料金を支払うホスト型の推論か、自分の鍵を使ってスマートフォンからリクエストする推論を選択します。この2つは別々の経路です。ログインでは、リモート署名を通じてAmberに対応しています。その後のリリースでは、[自分の鍵を使った順位付けとフォローリストの検出を修正](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.1)し、続いて[別のrelayで障害が発生しても、正常に動作しているrelayから取得した「いいね」を保持](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.2)するとともに、ダイジェストの復旧を改善しています。[バージョン1.0.3](https://github.com/jooray/nalgorithm/releases/tag/android-v1.0.3)では、モデル設定の順序を変更し、接続テストに必要な入力が不足している場合に通知するようになりました。

## プロトコルと仕様の取り組み

### 認証されたnappletエンドポイント

nappletアプリケーション向けのNAP仕様では、10月9日にマージされた[NAP-INCエンドポイント識別子](https://github.com/napplet/naps/pull/104)によって、単なるハンドラー名が認証された識別子に置き換えられます。発行者が異なれば、同じ名前でも同じ通信相手を指すことはなくなります。通信は引き続きランタイムが仲介し、ルートマニフェストやスナップショットマニフェストに、名前付きの`d`座標は必要ありません。

### 呼び出しリンク内のハンドラー推奨

同じく10月9日にマージされた[呼び出しリンクの推奨仕様](https://github.com/napplet/naps/pull/99)では、任意の`#naddr`ハンドラー推奨を指定できます。シェルは検出とインストールを提示でき、フォールバックとして通常の解決処理を利用できます。保存済みの設定とシェルのポリシーが優先されます。したがって、推奨ハンドラーは検出の手がかりを提供するものであり、ユーザーの既存の選択を置き換えたり、リンクの送信者にインストールの権限を移したりするものではありません。

### 配信の受諾とアプリケーションの処理

[インテントの告知と配信に関する変更](https://github.com/napplet/naps/pull/91)では、発行者間で安全に使える識別子を用い、同じ検証済みマニフェストからロールとインテントを導出します。配信の受諾は、送信元アプリケーションが動作し続けていることに依存しなくなります。`ok: true`という応答は配信の責任を引き受けたことを示し、宛先でのアプリケーションの処理が完了したことを意味するわけではありません。マージ済みのこの仕様変更でも、再試行と再起動の動作は引き続きランタイムのポリシーに委ねられています。

### Cyberspaceのアクションチェーン

[Cyberspaceの改訂されたチェーン規則](https://github.com/arkin0x/cyberspace/pull/48)では、フォークが発生すると署名済みアクションチェーンがその生成地点から無効になり、クライアントは次のアクションに署名する前に、現在有効な先端を確認する必要があります。このNostrを基盤とするワールドには、実装が従うべき判定結果を伴う[140本の署名済み合成チェーン](https://github.com/arkin0x/cyberspace/pull/49)が追加されています。[コピー時のクレジット規則](https://github.com/arkin0x/cyberspace/pull/47)では、元のオブジェクトへの`q`参照を使用し、公開リミックスでは元の作者に通知します。封印されたコピーでは、その通知を省略します。これらはマージ済みのプロジェクト仕様ですが、稼働中の検証器がどこまで対応しているかは未確認です。

### relayの永続保存確認応答

[未マージの永続保存提案](https://github.com/nostr-protocol/nips/pull/2496)は、永続保存の確認応答、PROOFクエリ、任意の署名付きkind 1797 relay証明を導入します。署名によって、保存しているという主張を特定のrelayに帰属させることはできますが、継続的な保持を証明するものではありません。また、クエリはクライアントがどのeventに関心を持っているかを明らかにします。

### Marmotグループの共有ピン留め

[Marmotの未マージのピン留め提案](https://github.com/marmot-protocol/marmot/pull/434)は、最大64件のメッセージ参照について、メンバーと管理者の権限を備えた認証済み共有状態を定義しています。変更を有効にするにはMLS Commitとエポック遷移が必要であり、遷移後のすべてのメンバーリーフがこの機能に対応していなければなりません。ピン留めはメッセージ本文をコピーしたり保持期間を延長したりしないため、利用できない参照先は未解決のままになります。提供されているテストフィクスチャは認証済み状態を前提としており、暗号処理やクライアント間の収束を実証するものではありません。

## NIP詳解：NIP-36とNIP-38

### 表示前のコンテンツ警告

[NIP-36「センシティブなコンテンツ」](/ja/topics/nip-36/)では、作者はeventに`content-warning` tagを追加でき、任意で理由を含めることもできます。クライアントは、読者が表示を選択するまでコンテンツを非表示にできます。[仕様](https://github.com/nostr-protocol/nips/blob/master/36.md)はインターフェースをクライアントに委ねており、補足的なラベルtagも認めています。警告を追加しても、そのeventを読める人の範囲は変わりません。公開投稿では、relayやほかのクライアントは引き続きその内容を受信します。

[Amethystの警告tagパーサー](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip36SensitiveContent/ContentWarningTag.kt)はこのtagを認識し、理由が存在しない場合や空白の場合は未指定として扱います。[Coracleの投稿作成画面](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/views/NoteCreate.svelte)は理由をtagに書き込み、その[コンテンツ表示画面](https://github.com/coracle-social/coracle/blob/8f4d34cc16bfb4380208923d26307fab561a867d/src/app/shared/NoteContent.svelte)は読者のセンシティブコンテンツ設定を尊重し、内容を表示する操作を提供します。[noStrudelのノート表示画面](https://github.com/hzrd149/nostrudel/blob/0476cad1944dcc999da5eae21ea5224e27014042/src/components/timeline/note/note-content-with-warning.tsx)は、独自の警告設定と展開状態を適用したうえで、警告インターフェースを表示します。

[NIP-36](https://github.com/nostr-protocol/nips/blob/master/36.md)はeventを暗号化するものではなく、非表示を義務付けるものでもありません。警告がないことは、コンテンツについて何も示しません。警告をプレビューや表示操作にどう反映するかは、クライアントが決定します。

### プロフィールのステータスと有効期限

[NIP-38「ユーザーステータス」](/ja/topics/nip-38/)は、アドレス指定可能なkind 30315 eventを使用します。作者、kind、`d` tagによってステータスの座標が識別され、`general`と`music`には意味が定義されています。新しいeventは、その座標にある以前のステータスを置き換えますが、`d`の値が異なるものは別のステータスとして保持されます。内容を空にするとステータスがクリアされます。[仕様](https://github.com/nostr-protocol/nips/blob/master/38.md)は、URL、プロフィール、event、アドレスへの参照も認めています。

この署名済み[NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md) eventは、有効期限が切れた一般ステータスを示しています。作者の元の綴りはそのまま保持しています。

```json
{
  "kind": 30315,
  "id": "8848719ae347e705afbbdbfa3a9f5dcca5dd31c4f39182503bf84de5e362bcf4",
  "pubkey": "f13fdeecd852acebaa77dbc18806a051eaa7ea2214c157a3495982d7535a77f3",
  "created_at": 1791983702,
  "tags": [
    [
      "d",
      "general"
    ],
    [
      "expiration",
      "1791984600"
    ]
  ],
  "content": "I'm listening 📩 on 3 ralys",
  "sig": "b5c98a578773f0199cb833d4b916aac115f2b13474a61e81fdca7316b848d397d7d8ad86d299abee4721f404b7b8a1af26e8c53143457ad14d2fb933b21daf85"
}
```

[Damusのステータスモデル](https://github.com/damus-io/damus/blob/4a94f666d7e159e380e10b4dbbb2967d1688709e/damus/Features/Status/Models/UserStatus.swift)は、有効期限付きの一般ステータスと音楽ステータスを扱います。[Nostriaのステータスサービス](https://github.com/nostria-app/nostria/blob/e861946f4ef4e70f3ec49997a4be27615b9b6f5e/src/app/services/user-status.service.ts)は、空の値や有効期限切れの値を無視し、楽曲の再生時間を使って音楽ステータスを公開します。通常のサブスクリプションでは、一般タイプと音楽タイプのみを要求します。[Amethyst](https://github.com/vitorpamplona/amethyst/blob/a9c2f04becf163dbff5d1cada9028ca197240a16/quartz/src/commonMain/kotlin/com/vitorpamplona/quartz/nip38UserStatus/UserStatusEvent.kt)は、ステータスをクリアする際にも`d`識別子を保持します。そのため、カスタムタイプを使うには、共通の通信データ構造に加えて合意が必要です。

ステータスは、作成者による公開の表明です。オンラインであることや、誰かが楽曲を聴いたことを証明するものではありません。音楽や応対可能かどうかを公開すると、習慣が明らかになる可能性があります。また、任意で設定できる有効期限は、古くなった情報の表示を抑えるものであり、削除を保証するものではありません。[NIP-38](https://github.com/nostr-protocol/nips/blob/master/38.md)は、NIP-36と同様、引き続きドラフト段階の任意仕様です。クライアントはそれぞれを独立して実装でき、読者に何が表示されるかは、クライアントの表示設定によって決まります。
