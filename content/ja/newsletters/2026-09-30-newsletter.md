---
title: "Nostr Compass #42"
date: 2026-09-30
publishDate: 2026-09-30
translationOf: /en/newsletters/2026-09-30-newsletter.md
translationDate: 2026-10-02
draft: false
type: newsletters
description: "Nostr Compass #42では、Compass Androidアプリを紹介し、White Noiseの投票、安定版Dart NDK、HoloboardとFIPS、新しいNostrアプリ、relayと署名アプリの変更、そして6年間の9月の節目を取り上げます。"
---

Nostrの週刊ガイド、[Nostr Compass](https://nostrcompass.org)へおかえりなさい。

専用の[Nostr Compass Androidアプリ](https://gitworkshop.dev/npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923/relay.ngit.dev/nostr-compass-android)は、ニュースレター、ポッドキャストのエピソード、トピックガイド、寄稿者の音声メモを1か所にまとめます。[最新の署名付きリリースノート](https://zapstore.dev/apps/naddr1qq2x7un89ehx7um5wf3k7mtsv9ehxtnpwpcqzxrhwden5te0wfjkccte9eaxzurnw3hhyefwv3jhvq3qwav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qqxpqqqplqk563kdn)には、署名検証済みのニュースレター全文、オフラインで利用できる保存済みの号と110件のトピックガイド、記事と利用可能な文字起こしを横断するローカル検索が記載されています。寄稿者は音声メモを録音して返信でき、送信前に保存した録音を確認でき、秘密鍵をアプリに保存せずにAmber経由で署名できます。公開された録音はNostrとBlossomで公開されます。

[最新のアプリ更新](https://zapstore.dev/apps/naddr1qq2x7un89ehx7um5wf3k7mtsv9ehxtnpwpcqzxrhwden5te0wfjkccte9eaxzurnw3hhyefwv3jhvq3qwav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qqxpqqqplqk563kdn)では、Androidがバックグラウンド処理を停止した場合でも、キューに入った録音とアップロードのチェックポイントが保持され、Amberによる承認が必要なときに表示され、通知から該当する録音を開けます。エピソードと音声メモのビューはそれぞれ独立してスクロール位置を保持し、再生は同じ位置から再開します。新しい録音の通知は、Androidのスケジューリングと権限に依存します。

**今週の内容：** [White Noise](#white-noise-android-adds-group-polls-and-account-specific-disappearing-message-defaults)は暗号化されたグループ投票と、チャット履歴が不完全な場合の通知を追加しました。[Holoboard](#holoboard-adds-nostr-promotion-commands-and-an-android-app)は[プライベートメッセージによるプロモーションコマンド](https://github.com/ptrio42/holoboard.space/blob/main/CHANGELOG.md#2026-09-23)とAndroidアプリを追加し、[fips-pub-domains](#fips-pub-domains-tests-signed-public-names-for-a-mesh)はメッシュ上で署名付きの公開名を試験しています。[Marmot MDK](#marmot-mdk-0110-makes-account-history-gaps-visible)は暗号化グループの履歴の欠落を可視化し、[Myco](#myco-080081-gives-nearby-apps-their-own-nostr-store)は近くの端末とのアプリ共有にNostrのidentityとストアを与えます。[nostream](#nostream-310-adjusts-relay-proof-of-work-to-load)は負荷に応じてrelayの受け入れ条件を調整し、[Nostr double ratchet](#nostr-double-ratchet-0017100172-closes-a-removed-member-gap)は削除されたメンバーに関する隙間を塞ぎます。開発中の作業では、[Amethystの暗号化グループの相互運用性](#amethyst-repairs-encrypted-group-interoperability)が修復され、[Divineの暗号化ビデオメッセージ](#divine-adds-encrypted-video-to-direct-messages)が追加され、[Nostr Atlas](#nostr-atlas-opens-a-directory-for-checkable-identities)が公開されました。プロトコルの更新では、identityの証明、relayの招待、フォローセット、提案中のドメインクレームが改良されています。月末の[9月の回顧](#six-years-of-nostr-septembers)では、同じ問いを6年間のNostrの歩みを通してたどります。

## トップストーリー {#top-stories}

### HoloboardがNostrのプロモーションコマンドとAndroidアプリを追加 {#holoboard-adds-nostr-promotion-commands-and-an-android-app}

[Holoboard](/ja/topics/holoboard/)は、Lightning支払いで順位を引き上げられるランキングを通じて[Nostrのノートを見つけるためのボード](https://holoboard.space)です。元の投稿はNostrのeventのままであり、Holoboardはランキングと表示用のデータを独自のHTTP APIから提供しています。ボードの並び順をrelayネイティブなフィードだと考える読者にとって、この区別は重要です。

[9月23日の変更履歴](https://github.com/ptrio42/holoboard.space/blob/main/CHANGELOG.md#2026-09-23)には、暗号化された[NIP-17](/ja/topics/nip-17/)と従来の[NIP-04](/ja/topics/nip-04/)の両方の経路でのダイレクトメッセージによるプロモーションコマンドが記録されています。NIP-17はプライベートメッセージを包んでその内容と送信者をrelayから隠し、NIP-04はそれより古いダイレクトメッセージの暗号化形式です。ユーザーは同じ会話の中でプロモーションの請求書を要求し、最初の有料プロモーションについてラベル付きの見積もりを1件受け取り、`YES`と返信することで期限切れのリマインダーに登録できます。プロモーションの送信処理は失敗したrelayに再試行し、[9月24日の更新](https://github.com/ptrio42/holoboard.space/blob/main/CHANGELOG.md)ではAndroidアプリが追加され、請求書の流れが簡素化されました。

プロジェクトの[relay連携ノート](https://github.com/ptrio42/holoboard.space/blob/main/relay/README.md)では、Nostr上の通常のノートとコメント、暗号化された受信箱のルーティング、引用と削除の処理が説明されています。署名付きの[ZapstoreのAndroid掲載情報](https://zapstore.dev/apps/space.holoboard.app)はアプリのリリースが存在することを裏付けていますが、掲載に使われた鍵がHoloboardの公開ボードのidentityであることは確認されていません。Compassがこのプロジェクトを取り上げるのは今回が初めてです。

### fips-pub-domainsがメッシュ向けの署名付き公開名を試験 {#fips-pub-domains-tests-signed-public-names-for-a-mesh}

[fips-pub-domains](/ja/topics/fips-pub-domains/)は、公開ドメイン名をFIPS上のノードに結び付ける新しい[リゾルバーと命名の実験](https://github.com/fr34aky/fips-pub-domains)です。FIPSは、ピアの発見にNostrのメッセージを使う暗号化メッシュです。[最初のリリース](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.1.0)では、これらのクレームを、DNS TXTレコード、任意のDNSSEC検証、ローカルにピン留めされたバインディング、Linux用のリゾルバーデーモン、そしてスマートフォン向けFIPSクライアントであるfips2goとのAndroid連携と組み合わせています。署名付きクレームだけでは公開ドメインの所有権は確立されません。クライアントには、DNSまたはDNSSECの証拠、設定済みの証人、または以前に信頼したピンが必要です。

[0.2.0リリース](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.0)では、クレームにDNSSEC証明が追加され、メッシュ上のrelayしか持たないクライアントでもピン留めされていない名前を検証できるようになりました。また、検証済みの複数のサーバーが1つのドメインを提供できるようになりました。古くなったピンとDNSのフェイルオーバーも修復されています。[バージョン0.2.1](https://github.com/fr34aky/fips-pub-domains/releases/tag/v0.2.1)では、そのままでは起動に失敗していたsystemdユニットが修正され、サーバーがroot権限なしで動作するようになりました。既存のインストールでこの修正を受けるには、ユニットを差し替える必要があります。

Androidでは、[マージされたfips2goの変更](https://github.com/fr34aky/fips2go/pull/55)により、DNSプロキシが検証済みの公開名のバインディングに従うようになりました。[2つ目のマージ済みの変更](https://github.com/fr34aky/fips2go/pull/59)は、設定済みのNostr relayへの接続をメッシュ経由で運ぶため、スマートフォンがインターネットに接続していない間でも、リゾルバーは初めて見るドメインクレームを取得して検証できます。デバイスでの結果はそれらのプルリクエストでメンテナーが報告したものであり、より広い展開を示すものではありません。

プロジェクトの[2ノード構成とメッシュ内relayのみの構成のテスト](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/testing.md)は、本番環境での展開ではなく、初期段階の実装についてメンテナーが報告した証拠です。その[NIP-DB](/ja/topics/nip-db/)の[提案](https://github.com/nostr-protocol/nips/pull/2487)はまだオープンであり、[ドラフト](https://github.com/fr34aky/fips-pub-domains/blob/main/docs/nip.md)中のevent kindは登録待ちのプレースホルダーのままです。先週のfips2goの記事ではメッシュのブートストラップとピアの発見を扱いましたが、今週の作業は公開名と検証に取り組んでいます。

### Marmot MDK 0.11.0がアカウント履歴の欠落を可視化 {#marmot-mdk-0110-makes-account-history-gaps-visible}

[Marmot MDK](https://github.com/marmot-protocol/mdk)は、[MLSで暗号化されたNostrのグループメッセージング](/ja/topics/marmot/)向けのRustランタイムと生成バインディングであり、先週の永続的な送信に関するリリースに続いて[バージョン0.11.0](https://github.com/marmot-protocol/mdk/releases/tag/v0.11.0)を公開しました。アカウントの復旧では、必要なすべてのrelayが切り詰められていないevent比較を完了した場合にのみ、履歴の欠落が解消されたと判断するようになりました。解消が証明されない欠落は永続的な通知を生成し、ホストはそれをユーザーに表示できます。配信キューが満杯になるとeventを破棄せずにアカウントのデータベースへ退避させ、ライブ配信ではトランスポートのカーソルを進めるため、再起動しても同じ履歴を再取得しません。

[完全なリリースノート](https://github.com/marmot-protocol/mdk/blob/v0.11.0/docs/release/0.11.0.md)には、任意の暗号化グループ投票、バインディングでのステートレスなevent検証、16 KBメモリページに対応したAndroidライブラリについても記載されています。アプリケーションは、このソースのコホートから生成されたバインディングとネイティブライブラリを一緒に更新する必要があります。アカウントのデータベースは初回起動時にスキーマ98までマイグレーションされ、データベースのダウングレードはサポートされません。既存の断続的なキャッチアップの不具合により、グループのエポックで5つ以上遅れたメッセージが、通知を出さないまま復号できない状態になることがあるため、このリリースはあらゆる場合に完全な履歴復旧ができるとは主張していません。

### Myco 0.8.0〜0.8.1が近くの端末とのアプリに独自のNostrストアを提供 {#myco-080081-gives-nearby-apps-their-own-nostr-store}

[Myco](https://github.com/Origami74/myco)は、nappletと呼ばれる小さなNostrプログラムを、オフラインの場合も含めて近くのスマートフォンと交換するためのAndroidアプリです。[バージョン0.8.0](https://github.com/Origami74/myco/releases/tag/v0.8.0)では、各インストールにゲスト用のNostr identityが与えられ、既存の鍵またはAmberでのログインが可能になりました。Amberは、アカウント鍵を共有せずに署名を承認するAndroid署名アプリです。また、Discoverタブが、それ自体がnappletであるアプリストアに置き換えられました。このストアは署名付きのアプリ掲載情報とおすすめを読み込み、ダウンロードした更新はインターネット接続なしでユーザーのCircle内のスマートフォン間で受け渡しできます。

[バージョン0.8.1](https://github.com/Origami74/myco/releases/tag/v0.8.1)では、作成者が告知しているrelayを問い合わせることで、これらの掲載情報を見つけやすくしました。以前のビルドは公開のデフォルト設定に頼っていました。キャッシュされたプロフィールとアプリをすぐに表示し、応答の遅いrelayの回答を次回の閲覧のために保存し、失敗しているrelayへの接続を控え、ビューが開いている間はサブスクリプションを維持します。どちらの更新も既存のスマートフォン間のwire形式を保っています。更新済みのスマートフォンはnappletの更新をダウンロードして共有でき、古いスマートフォンは告知だけを転送します。

## タグ付きリリース {#tagged-releases}

### White Noise Androidがグループ投票とアカウントごとの消えるメッセージの既定値を追加 {#white-noise-android-adds-group-polls-and-account-specific-disappearing-message-defaults}

[White Noise Android](https://github.com/marmot-protocol/whitenoise-android)は、[Marmot](/ja/topics/marmot/)で暗号化されたプライベートな会話のためのNostrメッセンジャーです。[先週取り上げた](/en/newsletters/2026-09-23-newsletter/#white-noise-android-2026921-improves-encrypted-chat-reliability-and-sharing)配信と共有の改善に続き、[9月30日のリリース](https://github.com/marmot-protocol/whitenoise-android/releases/tag/android-v2026.9.30)では、Marmot Development Kitを通じて、選択式の回答、結果バー、締め切りを備えたグループ投票が追加されました。また、[アカウントごとにデバイス内で設定する消えるメッセージの既定値](https://github.com/marmot-protocol/whitenoise-android/pull/2799)も追加されています。新しいダイレクトの会話とグループは選択した期間を引き継ぎ、既存の会話とその個別設定は現在のポリシーを維持します。[Wave hi](https://github.com/marmot-protocol/whitenoise-android/pull/2765)は、現在の下書きを乱すことなく、新たに追加されたメンバーにメンションする挨拶を送信します。

この[リリース](https://github.com/marmot-protocol/whitenoise-android/releases/tag/android-v2026.9.30)では、プロフィール画像とグループ画像の切り抜きの焦点を選べるようになり、会話を削除せずにチャットフォルダーを削除できるようになりました。[履歴に関する通知](https://github.com/marmot-protocol/whitenoise-android/pull/2869)は、復旧によってアカウントやグループの履歴が不完全になっている可能性がある場合に表示され、それぞれ個別に閉じられます。[会話のページング](https://github.com/marmot-protocol/whitenoise-android/pull/2818)は、最近のメッセージへジャンプしたときに表示中のタイムラインを再構築しないようにし、[保留中のメッセージの編集](https://github.com/marmot-protocol/whitenoise-android/pull/2825)は、元の送信が確定したevent IDを取得するまでの間もテキストを保持します。この編集の引き継ぎは実行中のアプリ内での会話の変更を対象としており、プロセスが終了した後も保持されることを示すものではありません。

[音声入力では、録音ごとに貼り付けか送信かを選べるようになり](https://github.com/marmot-protocol/whitenoise-android/pull/2768)、自動終了時には文字起こしが下書きに入ります。[オフラインプロバイダーの設定](https://github.com/marmot-protocol/whitenoise-android/pull/2888)では、デバイス上での処理について説明し、その同意を他の音声プロバイダーとは別に管理し、録音終了後に中断されたメディアを復元します。[一般的なファイルの処理](https://github.com/marmot-protocol/whitenoise-android/pull/2830)では、サイズに上限があり空でない文書を、正確なファイル名、MIMEメタデータ、失敗時のメッセージとともに受け付けます。[明示的な添付ファイルのダウンロード](https://github.com/marmot-protocol/whitenoise-android/pull/2879)では、Androidのユーザー起動による転送ジョブを使い、フォアグラウンド処理を予備手段とします。[貼り付けの操作](https://github.com/marmot-protocol/whitenoise-android/pull/2877)はAndroidのシステムアクションを使うようになり、GrapheneOSのSecure Pasteがクリップボードへのアクセスを許可できるようになりました。Androidでは、ダウンロードポリシーを守りつつ、[iOSから共有されたGIPHYもアニメーションのメディアとして表示](https://github.com/marmot-protocol/whitenoise-android/pull/2806)されます。

[通知の修正](https://github.com/marmot-protocol/whitenoise-android/pull/2808)により、送信者のニックネームが更新され、会話を開いたときに通知が整理されます。[通知の復旧に関する変更](https://github.com/marmot-protocol/whitenoise-android/pull/2712)では、フォアグラウンドの所有者が利用できない間も保留中のプッシュ処理を保持し、回数に上限のある再試行を使います。[Amberでの署名](https://github.com/marmot-protocol/whitenoise-android/pull/2802)では、同じアカウントへの承認要求が集中した場合に調整を行い、レート制限によって送信が取り消されないようにします。[新しい監査設定](https://github.com/marmot-protocol/whitenoise-android/pull/2872)では、新しい受信先へアップロードする前に、ログ共有について改めて選択を求めます。ソースは[AGPL-3.0-onlyライセンスも採用](https://github.com/marmot-protocol/whitenoise-android/pull/2840)しました。

### nostream 3.1.0がrelayのproof of workを負荷に応じて調整 {#nostream-310-adjusts-relay-proof-of-work-to-load}

[nostream](https://github.com/Cameri/nostream)は、PostgreSQLを基盤とするTypeScript製のNostr relayです。[バージョン3.1.0](https://github.com/cameri/nostream/releases/tag/v3.1.0)では、観測されたeventの流量の変化に応じて、運営者が設定した範囲内でeventのproof-of-workのしきい値を上げ下げできます。この設定は既定では無効で、各ワーカーが計測した流量を使い、既存の公開鍵に対する固定しきい値とは独立して動作します。そのため、送信者が異なる受け入れ条件に直面するのは、運営者がオプトインした場合に限られます。

同じ[リリース](https://github.com/Cameri/nostream/releases/tag/v3.1.0)では、relay、WebSocket、eventの各メトリクス、ネットワーク健全性のプローブ結果、設定可能な運営者向け通知を表示する管理ダッシュボードも追加されました。管理APIは既定で無効です。これらの機能により、運営者はrelayへの負荷と到達性の問題を区別しやすくなり、新しいポリシーは明示的な設定の下に置かれたままとなります。

負荷に応じたproof-of-workのリリースの後、nostreamは[信頼できるモデレーターによる報告に対するアクション](https://github.com/cameri/nostream/pull/788)をマージしました。[NIP-56](/ja/topics/nip-56/)はコンテンツ報告のeventを定義しています。新しい`nip56.hideActionableReports`オプションは、報告機能も有効になっている場合に、報告されたeventをREQとCOUNTの結果から除外します。eventに対する報告はそのeventを非表示にし、公開鍵に対する報告はその作成者のすべてのeventを非表示にします。新しいオプションは既定でfalseなので、報告の収集を有効にしただけでは既存のクエリ結果は変わりません。

### Nostr double ratchet 0.0.171〜0.0.172が削除されたメンバーに関する隙間を解消 {#nostr-double-ratchet-0017100172-closes-a-removed-member-gap}

[Nostr double ratchet](https://github.com/irislib/nostr-double-ratchet)は、Nostrで運ばれる暗号化されたプライベートチャットのためのTypeScriptライブラリです。[バージョン0.0.171](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.171)では、メンバー構成の変更後にグループの送信者鍵をローテーションするため、古い鍵を持ったまま削除された人は、更新済みの送信者からのその後のメッセージを、その送信者が再起動した後であっても復号できません。また、削除されたローカルの所有者による送信や鍵のローテーションを拒否し、鍵の配布中にメンバー構成が変わった場合は送信を中止します。

[バージョン0.0.172](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.172)では、既存のアカウント署名によるデバイス承認を、任意の暗号化された招待への応答に含めて運びます。更新版を使う受信者は、別の登録eventが届く前に送信者のデバイスを検証でき、リンクされたデバイスは再起動後も承認を保持します。招待のフィールドは任意であり、元のハンドシェイクとラチェットのメッセージ形式はそのまま維持されます。

[バージョン0.0.173〜0.0.175](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.175)では、この削除に関する作業を拡張し、グループ鍵の受け渡しを永続化し、キューに入った配信状態を公開前に保存するため、中断された受け渡しは再起動後に復旧します。公開時のコールバックはローカルのグループ情報を運び、アプリケーションは削除後に永続的な再試行を取り消しつつ、メンバー管理の操作は配信可能なままに保てます。キューに入った送信は元の内側のevent IDを保持します。重複した招待への応答は確立済みのセッションを保ち、連絡先が変わってもサブスクリプションは安定したままで、アプリ鍵のスナップショットは変更可能なコピーを共有せずにデバイス名を保持します。署名付きのwire形式は変わりません。[0.0.173のノート](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.173)では、受信セッションのフォールバックとローカルのグループエコーのフィルタリングを備えたRust版0.0.168についても報告されています。

### Scramble 0.7.4〜0.7.5が新しいグループメンバーが見るべきメッセージを取得 {#scramble-074075-fetches-the-messages-a-new-group-member-should-see}

[Scramble](https://github.com/DavidGershony/Scramble)は、ネイティブのAndroidインターフェースを備えたクロスプラットフォームのMarmotグループメッセンジャーです。[バージョン0.7.5](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.5)では、グループごとにrelay履歴の取得開始点が設けられました。以前は最も活発な会話の取得開始点がすべてのグループに適用されていたため、新たに参加したグループでは、参加後のメッセージが一度も要求されず、空のままになることがありました。再接続の経路にも同じ修正が入り、ローカルでの活動がないグループは利用可能なすべてのメッセージを要求するようになりました。それでもMLSにより、新しいメンバーは参加前に送信されたメッセージを復号できません。

その前の[0.7.4リリース](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.4)では、再利用されたAndroidの行にクリックハンドラーが蓄積して招待の承認が繰り返される問題が修正され、ネイティブアプリでカスタムのBlossomメディアサーバーの設定が保持されるようになりました。バージョン0.7.5はネイティブのAndroid APKのみを提供するため、古いAvalonia版のファイル名を追跡しているユーザーは更新対象を変更する必要があります。アカウントと履歴はこの2つのAndroidビルド間で移行されますが、古い0.6.xのMLSエンジンで作成されたグループは0.7.xへ移行されません。

[Scramble 0.7.6](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.6)では、手動の「欠けているメッセージを取得」操作が追加されました。これはグループが使ってきたすべてのルーティングアドレスを問い合わせ、時間の制限を取り除き、古くなった保存済みアドレスを修復し、何を復旧したかを報告します。ただし、ユーザーが参加する前のエポックは引き続き復号できません。ネイティブ版の管理者は、現在の名簿の状態と失敗時の結果を確認しながら、他のメンバーを昇格または降格できます。2人での会話では引き続きこれらの操作は表示されません。グループ情報のコピー操作も反応するようになりましたが、招待された会話では、プロトコル上のグループIDではなく内部のチャット識別子がコピーされる場合があります。[バージョン0.7.7](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.7)では、[他のメンバーのコミットが届いたときに保留中のメッセージを処理する](https://github.com/DavidGershony/Scramble/commit/35e72177a0009ec96e8494caed7e9c250b66c7cb)ようにもなり、[0.7.8](https://github.com/DavidGershony/Scramble/releases/tag/v0.7.8)では、受動的なメンバーのこの経路に対する回帰テストが追加されました。

### Amber 6.6.6がリモート署名の接続シークレットを修復 {#amber-666-repairs-remote-signer-connection-secrets}

[Amber](https://github.com/greenart7c3/Amber)は、アプリケーションにアカウント鍵を渡さずにNostrのevent署名を承認するAndroid署名アプリです。先週のバックアップ暗号化の変更に続き、[バージョン6.6.6](https://github.com/greenart7c3/Amber/releases/tag/v6.6.6)では`nostrconnect`のパーサーが修正されました。パディングされたシークレットのように`=`を含む接続パラメーターが、Amberの応答前に改変されていました。そのため、署名アプリとの接続がそれ以外の点では正常に見えても、NDKベースのクライアントはシークレットの確認に失敗していました。

この[リリース](https://github.com/greenart7c3/Amber/releases/tag/v6.6.6)では、フィードバックのissueをAmberのリポジトリ告知に記載されたrelayへ送信するようにもなり、告知を取得できない場合は以前のrelayを予備として使います。Torのタイムアウトが延長され、遅いrelayがその公開を確認するまでの時間が長くなりました。残りの変更では、Amberのテーマにおけるアイコンとテキストの視認性が改善されています。

### FIPS 0.5.2がNostrでの発見に伴うプライバシー漏洩を阻止 {#fips-052-stops-a-nostr-discovery-privacy-leak}

[FIPS](https://github.com/jmcorgan/fips)は、ピアの発見にNostrのidentityとrelayのメッセージを使う暗号化メッシュです。[0.5.2のメンテナンスリリース](https://github.com/jmcorgan/fips/releases/tag/v0.5.2)では、NAT越えの削除要求にノードのルーティング鍵で署名することをやめました。この署名によって、relay上でその鍵がNAT越えのトラフィックと結び付けられていました。また、relay接続に使うTLSライブラリを、公開済みのセキュリティアドバイザリを修正したバージョンへ更新し、リンクとセッションの鍵更新でメッセージが失われる複数のケースを修復しています。

[リリースノート](https://github.com/jmcorgan/fips/releases/tag/v0.5.2)では、すべてのプラットフォームの運営者にアップグレードを求めるとともに、Windowsの鍵ファイルの権限、ゲートウェイ、パッケージサービスに関する個別の修正を詳しく説明しています。一時的なノードは、後の再起動で上書きされる可能性のある非公開の`fips.key`を書き込まなくなりました。安定したidentityを意図していた運営者は、アップグレード前に永続モードを設定する必要があります。このリリースはメッシュのwire形式を変更しないため、バージョンの混在したノードを個別にアップグレードできます。

### napplet soyLI 0.23.1〜0.23.4がバックエンドの公開と署名の承認を修復 {#napplet-soyli-023102234-repairs-backend-publishing-and-signer-approval}

[napplet.soyのsoyLI](https://github.com/zeSchlausKwab/napplet-soy)は、サンドボックス化された小さなNostrプログラムのための作成と公開のツールキットです。先週の作品共有のリリースに続き、[バージョン0.23.1](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.23.1)では、バックエンドのマニフェスト、ハンドラー、スキーマが作成者向けのチェックとマルチプレイヤーのプレビューの対象になりました。移植可能なプロバイダー設定はプロジェクトのマニフェストに保持し、非公開のidentityのバインディングと開発用データベースは公開されるソースのスナップショットの外に置きます。

[バージョン0.23.2](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.23.2)では、生成された公開バックエンドのコンテキストを過去にコミットしたことのあるプロジェクトが、厳格な検証の後で再び公開できるようになりました。一方で、到達可能な履歴に含まれる非公開のバインディング、ジャーナル、データベース、認証情報は引き続き拒否されます。その後の[0.23.4リリース](https://github.com/zeSchlausKwab/napplet-soy/releases/tag/soyli-v0.23.4)では、署名に数秒かかった場合に、有効な拡張機能やリモート署名アプリによる承認が拒否されることのある、永続バックエンドのセッション障害が修正されました。公開ホストにも共有ホスト側の修正が必要です。作成者のCLIを更新しただけでは、展開済みのホストは修復されていません。

### Dart NDK 0.10.0がBlossomの認証とリモート署名の範囲を限定 {#dart-ndk-0100-scopes-blossom-auth-and-remote-signing}

[Dart NDK](https://github.com/relaystr/ndk)は、Nostrのrelayへのアクセス、署名、ウォレットへの要求、メディア操作のためのFlutterおよびDartのライブラリです。先週のプレリリースに続き、[0.10.0-dev.7](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.7)では、Blossomのメディア要求がサーバーに拒否されるまで匿名のままとなり、その後、操作ごとにどのidentityを明かしてよいかを示す明示的なポリシーを通じて認可するように変更されました。この認可はリクエストの経路全体に引き継がれ、従来の`useAuth`と`customSigner`のオプションを置き換えます。これは、プレリリースのAPIを使っているアプリにとって、統合上の破壊的変更です。

[dev.9](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.9)では、リモート署名アプリの応答を最も遅いrelayが確認するまで保留することをやめました。[dev.8](https://github.com/relaystr/ndk/releases/tag/v0.10.0-dev.8)では、バックグラウンドでのrelayのポーリングとキャッシュ処理が削減され、その他の修正はウォレットのシードの永続化と決済の期限に関するものです。[安定版0.10.0リリース](https://github.com/relaystr/ndk/releases/tag/v0.10.0)は、この開発系列を、後述する接続メタデータと非公開のサブスクリプションIDの変更とともにまとめて提供します。[dev.9との比較](https://github.com/relaystr/ndk/compare/v0.10.0-dev.9...v0.10.0)には、それらのマージ済みの変更が含まれています。アップグレードするアプリケーションは、メディア認証のAPI変更とリモート署名アプリの応答経路の両方を確認する必要があります。

安定版リリースには[NIP-46の接続メタデータと要求する権限](https://github.com/relaystr/ndk/pull/852)が含まれており、個別の接続フィールドを`Nip46ClientMetadata`の値で置き換えています。これはソースAPIの変更であり、ログイン用のウィジェットがアプリケーションのidentityと要求する権限をbunkerに渡せるようになります。もう1つの[リクエストIDの変更](https://github.com/relaystr/ndk/pull/860)では、本番環境で32文字のランダムな16進数を使い、用途の名前やページングの段階がrelayから見えるサブスクリプションIDに含まれないようにしています。明示的に指定したIDは引き続きNIP-01の64文字の上限内に制限され、デバッグモードでは短い診断用の名前が保持されます。

### Mostro Core 0.16.0が古いgift-wrapトランスポートを削除 {#mostro-core-0160-removes-the-old-gift-wrap-transport}

[Mostro Core](https://github.com/MostroP2P/mostro-core)は、MostroのNostrベースのピアツーピア取引クライアントとコーディネーターが使うメッセージプロトコルを提供します。[バージョン0.16.0](https://github.com/MostroP2P/mostro-core/releases/tag/v0.16.0)では、プロトコルv1のgift-wrapトランスポートと古いwrapおよびunwrapの関数が削除され、新しいトランスポートがライブラリの経路として残ります。これは、このライブラリを通じてv1のメッセージを作成または読み取っているアプリケーションにとって破壊的変更です。

この[ライブラリのリリース](https://github.com/MostroP2P/mostro-core/releases/tag/v0.16.0)は、コーディネーターの[公開済みとなった0.19.0リリース](https://github.com/MostroP2P/mostro/releases/tag/v0.19.0)に先行するものです。古いクライアントに対応している運営者は、トランスポート移行の両側を更新する必要があります。その前の[0.15.1タグ](https://github.com/MostroP2P/mostro-core/releases/tag/v0.15.1)では協調的なキャンセルの紛争状態が追加されましたが、互換性の上での節目はトランスポートの削除です。

### Cambium 0.6.0〜0.7.1がrelayメッセージを通じてロック解除用のスマートフォンを登録 {#cambium-060071-enrolls-an-unlock-phone-through-relay-messages}

[Cambium](https://github.com/forgesworn/cambium)は、Heartwoodハードウェア鍵のためのAndroid署名コンパニオンであり、再起動後にボードのロックを解除することもできます。[バージョン0.6.0](https://github.com/forgesworn/cambium/releases/tag/v0.6.0)では、USBケーブルなしで、ボードのNostr relayを通じてスマートフォンをロック解除用に登録できるようになりました。ユーザーは、スマートフォン、ボード、そしてボードの登録用インターフェースであるSapwoodの3か所で5つの要求語を照合してから、ボードのボタンを押します。新たに告知されたrelayにはランダム化された接続遅延が適用されるため、スマートフォンの最初の接続から、ボードの更新をいつ確認したかが正確に明らかになることはありません。

[バージョン0.7.0](https://github.com/forgesworn/cambium/releases/tag/v0.7.0)では招待の流れが逆になり、スマートフォンがSapwoodの短時間だけ有効なQRコードを読み取り、使い捨ての鍵から暗号化された1回限りのeventを1つ返します。どのrelayにも受け入れられなかった場合、再試行では同じeventを再公開し、古いSapwoodのビルド向けには従来のコード表示の経路も残されています。[0.7.1パッチ](https://github.com/forgesworn/cambium/releases/tag/v0.7.1)では最終確認コードが表示されたままになり、F-Droidビルドの再現性が改善されました。QRの流れには、引き続き指定された最近のバージョンのSapwoodとHeartwoodが必要です。

### Bray 3.5.0〜3.5.2がエージェント主導のNostrウォレット支出を制限 {#bray-350352-limits-agent-initiated-nostr-wallet-spending}

[Bray](https://github.com/forgesworn/bray)は、AIアシスタントが範囲を限定したインターフェースを通じてrelay、identity、ウォレットの操作を要求できるNostrツールサーバーです。その[3.5.0リリース](https://github.com/forgesworn/bray/releases/tag/v3.5.0)では、Nostr Wallet Connectの支払いごとの上限と永続化された1日あたりの予算が追加され、アシスタントのホストが対応している場合は人による確認が行われます。個別の支出用接続を提供するには明示的なウォレットサービスの設定が必要になり、各許可は使用前に再確認され、請求書の照会はその許可の範囲内のハッシュに限定されます。

この[リリース](https://github.com/forgesworn/bray/releases/tag/v3.5.0)では、ウォレット接続のURIをチャットに貼り付けずに非公開のファイルに保存するようユーザーに案内し、結果が不確かな支払いを、失敗が証明されたかのように扱って再試行することを拒否します。[バージョン3.5.2](https://github.com/forgesworn/bray/releases/tag/v3.5.2)では、relayが要求された支払い方法のフィルターを拒否したことを受けて、マーケットプレイスの支払い手段をローカルで照合するようになりました。これらのチェックにより、委任されたアシスタントが支出できる額が制限され、relayのフィルターに関する前提によって該当するオファーが隠れてしまうことを防ぎます。

### Mafrend 1.3.0-alphaがプライベートな地図グループを最新のMarmotへ移行 {#mafrend-130-alpha-moves-private-map-groups-to-current-marmot}

[Mafrend](https://github.com/DestBro/mafrend-zapstore)は、場所を探索し、目的地を中心にチャットできる地図ベースのNostrソーシャルアプリです。その[1.3.0-alphaリリース](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.3.0-alpha)では、プライベートグループがより新しい[Marmotの暗号化グループ](/ja/topics/marmot/)仕様へアップグレードされ、チャットとレビューからプロフィールを表示できるようになりました。このグループ形式は古いalpha版のチャットと互換性がないため、ユーザーはこれを互換性の断絶を伴うalpha版の移行として扱う必要があります。

[同じリリース](https://github.com/DestBro/mafrend-zapstore/releases/tag/v1.3.0-alpha)では、地図とマーカーの改善に加えて、スクリーンショットの共有とチャットの変更も追加されています。プロフィール機能は、プロジェクトによって引き続き開発中とされています。Nostrにとって意味のある変更はプライベートグループの相互運用性の転換であり、古いテストグループを持つユーザーはアップグレード前に互換性に関する注意事項を確認する必要があります。

### Sonar alpha.15〜alpha.15.1が暗号化グループへの公開を修復 {#sonar-alpha15alpha151-repairs-encrypted-group-publishing}

[Sonar](https://github.com/hedwig-corp/bitchat-to-sonar)は、BluetoothメッシュとNostrで会話を運べるプライベートメッセンジャーです。[alpha.15](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.15)では、メッセージへの絵文字リアクションと、暗号化チャット内でのローカル時刻の非公開共有が追加され、その共有を取り消す設定も用意されました。ウォレットはCashuに切り替わりましたが、この支払いに関する変更はメッセージングの更新とは別のものです。

[alpha.15.1](https://github.com/hedwig-corp/bitchat-to-sonar/releases/tag/v0.1-alpha.15.1)では、古いブランチのビルドが異なるスキーマバージョンを書き込んだ後に、会話インデックスが空になることのある起動時の障害が修復されました。インデックスがない状態では、アプリは開き直すたびにローカル時刻の共有を再暗号化してすべてのグループへ再公開し、relayのレート制限が働くまでに数百件のeventを送信することもありました。このホットフィックスはそのローカル状態を再構築し、グループへの繰り返しの公開を止めます。

### ElisymのコマースパッケージがプライベートなNostrの注文を導入 {#elisyms-commerce-packages-introduce-private-nostr-orders}

[Elisym](https://github.com/elisymlabs/elisym)は、署名付きeventによるコマースの流れを現在構築しているNostrベースのエージェントツールキットです。その[マージ済みの`commerce`パッケージ](https://github.com/elisymlabs/elisym/pull/120)は、チェックアウトと販売者のコンポーネント向けに、ストアの商品、所有者の認可、非公開で包まれた注文と領収書、オファーの検証を定義しています。その後の[commerce 0.2.0タグ](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0)では、注文の支払い参照をその注文から導出し、支払いの照会を署名付きの購入の流れに結び付けています。

このパッケージ系列では、別個の支払いコアとブラウザーでのチェックアウトの作業も導入されていますが、その[リリースタグ](https://github.com/elisymlabs/elisym/releases/tag/%40elisym/commerce%400.2.0)からは、販売者向けの完全なチェックアウトが展開されていることは確認できません。ストアの認可に使うevent kindは、プロジェクトの一次資料で暫定的なものと明記されています。SDK、MCP、CLI、支払いコアの11個のタグは、開発中の1つのコマース機能を示しています。

[Elisymの新しいパッケージリリース](https://github.com/elisymlabs/elisym/releases/tag/%40elisym%2Fmerchant-node%400.1.0)はセルフホスト型の販売者ノードをパッケージ化しており、[MCP 0.31.0](https://github.com/elisymlabs/elisym/releases/tag/%40elisym%2Fmcp%400.31.0)はコマース商品向けに`buy_product`と`get_order`を追加しています。その後のcommerceと販売者ノードのリリースでは、同じチェックアウト内にTempoの支払い対応が加わりました。これらのパッケージは既存の署名付き商品と非公開の注文の統合を前進させるものですが、タグの一覧によって暫定的なeventスキーマが標準になるわけではなく、完全なホスト型サービスの開始が確立されるわけでもありません。

### Flotilla 1.11.2が署名アプリと不完全なrelayフィードの停滞を解消 {#flotilla-1112-unsticks-signers-and-incomplete-relay-feeds}

[Flotilla](https://github.com/coracle-social/flotilla)は、会話、ルーム、共有スペースのためのNostrクライアントです。[バージョン1.11.2](https://github.com/coracle-social/flotilla/releases/tag/1.11.2)では、リモート署名アプリを待って起動が止まったときにユーザーが抜け出す手段が用意され、ローカルのアプリケーションデータが消去されたセッションはサインアウトされるようになりました。ルームは、より大きなスペースの同期が終わる前にメッセージを表示できるようになり、フィードは、あるrelayが別のrelayより遅れて応答したというだけで投稿を取りこぼさなくなりました。

[同じリリース](https://github.com/coracle-social/flotilla/releases/tag/1.11.2)では、アプリの既存の鍵で署名されたF-Droidビルドも公開され、Obtainium向けにGitHubのリリースが最新に保たれます。この配布に関する作業は更新経路を切り替えるユーザーにとって重要ですが、すぐにアップグレードする理由はrelayと署名アプリに関する修正です。

### Ditto 2.42.3がrelayへの配信状況を表示し、アカウントの境界を強化 {#ditto-2423-shows-relay-delivery-and-tightens-account-boundaries}

[Ditto](https://gitlab.com/soapbox-pub/ditto)は、ユーザーが自分のrelayを選んで認証できるNostrソーシャルクライアントです。[バージョン2.42.3](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.42.3)では、投稿のEvent Detailsに、その投稿を保持しているユーザーと作成者のrelayが表示されます。Broadcastは、投稿がないrelayだけを対象にします。このリリースでは、応答しない読み取り用relayも示され、再試行の操作が用意されるため、投稿をすべての場所へ送り直すことなく、見つからない投稿の原因を調べやすくなりました。

[リリースノート](https://gitlab.com/soapbox-pub/ditto/-/releases/v2.42.3)によると、アカウントを切り替えても以前のアカウントのrelayへ投稿が送信されなくなり、ミュートしたユーザーが一般的なスマートフォンの通知を発生させることはできず、投稿内のリンクや画像が読者のローカルネットワーク上のデバイスに到達することはできなくなりました。遅いrelayからの投稿がFollowsとLovedのフィードから消えることはなくなり、ライブ配信のチャットとwebxdcゲームは、ビュー全体を繰り返しダウンロードせずに更新されます。トレントと音声のブラウジングも新たに追加されましたが、Nostrへの影響が最も大きいのはrelayのルーティングとアカウントの分離です。

### Iris Chat 2026.9.24.4が暗号化された会話に通話を導入 {#iris-chat-20269244-brings-calls-into-encrypted-conversations}

[Iris Chat](https://github.com/irislib/iris-chat-rs)は、double-ratchet系のチャットプロトコルを使うエンドツーエンド暗号化のNostrメッセンジャーです。その[9月24日のリリース](https://github.com/irislib/iris-chat-rs/releases/tag/v2026.9.24.4)では、互換性のある連絡先との音声通話とビデオ通話が追加され、インターネットが利用できないときには既存のローカル接続を介した通話も可能です。ユーザーはビデオの画質を下げたり、ビデオ通話に音声で応答したり、Androidの通話インターフェースで着信を処理したりできます。応答または拒否すると、リンクされた他のデバイスの着信音も止まります。

この[リリース](https://github.com/irislib/iris-chat-rs/releases/tag/v2026.9.24.4)では、別の署名アプリを通じてサインインし、どのリンク済みデバイスが接続されているかを確認することもできます。その後の[9月24日のパッチ](https://github.com/irislib/iris-chat-rs/releases/tag/v2026.9.24.5)では、遅れて届いたメッセージが元のタイムスタンプを保持するようになり、再接続のパケットが失われた後の近距離配信が改善されました。これらはデバイス間と通話に関する初期段階の挙動であるため、この更新が最も役立つのは、互換性のあるIrisのビルドを実行できる連絡先です。

その後の開発者署名付きの[9月30日の更新](https://primal.net/e/17fd3f325dda1feb0c1e51c6e1af0f7b3efe42ecff75e9527ac435cdc6a30c7a)では、削除されたメンバーのローカルのグループ履歴を保持しつつ送信を無効にし、リンクされたデバイス間と大規模なグループでの配信を改善し、既読表示と未読数を修復しています。通話では音声デバイスの選択が可能になり、発信音が復元されました。古いマイクの状態によって着信音声が無音になることもなくなりました。時間指定のミュート、画像のコピー、ドロップしたファイルの添付、通知のルーティング、プッシュ登録にも修正が入り、サインアウトするとローカルのキャッシュが消去され、デバイスを削除するとそのセッションが終了します。[2つ目の更新](https://primal.net/e/89ec93e25caf31831714e807c927b6d50d3d5fc38044df845163ff656db3f711)では、同じデバイス上の他のIrisアプリがキャッシュしたファイルへのアクセスが改善され、Nearbyを無効にしてもローカルでのファイル共有が利用できるようになりました。

### LibreNostr 0.6.0〜0.7.0が内蔵Torを経由してrelayに接続 {#librenostr-060070-routes-relays-through-built-in-tor}

[LibreNostr](https://github.com/Lwb89dev/librenostr)は、relayとプライバシーの設定を変更できるAndroid向けNostrクライアントです。[バージョン0.6.0](https://github.com/Lwb89dev/librenostr/releases/tag/v0.6.0)では、ARM64向けにArtiベースのTorエンジンが同梱され、選択したDirect、すべてをTor経由、`.onion`のみのいずれかのモードが、relayのWebSocket、HTTPリクエスト、メディア、アップロード、ウェブページに適用されます。厳格なTorモードでは、Torが利用できない場合に安全側に倒れて失敗し、リクエストを黙って直接送信することはありません。モードを変更すると、relayのソケットは新しい経路で再接続されます。

[バージョン0.6.2](https://github.com/Lwb89dev/librenostr/releases/tag/v0.6.2)では、公開のフォローリストから構築するデバイス上のweb-of-trustフィルターが追加され、補助的なrelayを、それによって新たに届くフォロー中の人の数に基づいて選ぶようになりました。続く[バージョン0.7.0](https://github.com/Lwb89dev/librenostr/releases/tag/v0.7.0)では、プロフィールと件数の照会が終わる前にノートと通知を表示し、遅いrelayへのクエリに上限を設け、会話を開くたびにDMの受信箱全体を復号することをやめました。これらのリリースを合わせると、クライアントがどこへ接続しうるかと、遅いrelayがインターフェースをどれだけ待たせうるかの両方が変わります。

開発者署名付きの[最初の安定版リリースである1.0.0](https://primal.net/e/4eeba660b6b789288954290497de89fe3222bfc955214647ead5d63e6031d927)では、フィード、ハッシュタグ、プロフィール、長文記事の閲覧、通知、メッセージのための移動可能なカラムを備えた、プロフィールごとに保存されるタブレット用デッキが追加されました。このレイアウトは横向きのタブレットで使われ、スマートフォンは既存のインターフェースを維持します。検索ではOR、除外、メディアフィルター、正しく機能する日付範囲が使えるようになり、relayからの絞り込み結果の前にキャッシュ済みのプロフィールを返し、拒否された全文検索リクエストはすぐに飛ばします。ハッシュタグは時系列で並び、ページングは十分なrelayの応答が集まるまで待ち、使われていないフィードはサブスクリプションを解放します。

[同じリリース](https://primal.net/e/4eeba660b6b789288954290497de89fe3222bfc955214647ead5d63e6031d927)では、公開および暗号化されたミュートリストとブックマークの既存の項目を、編集時に1つの変更で置き換えずに保持します。ブックマークと通知はアカウント間で分離され、補助的な作成者のrelayは公開の読み取りに限定されるため、非公開のリクエストとrelay認証がそれらのrelayに送られることはありません。また、古いプロフィールの応答が新しいメタデータを上書きすることを防ぎ、通知のページングとバッジを修復し、新しい項目が届いても古いフィードの項目を保持します。返信の取り消しのカウントダウン、重複した公開、クエリ文字列を含むメディアのURL、チャットを既読にした後の未読数も修正されています。[バージョン1.0.1](https://primal.net/e/630becb73dbe7ba7c76a2d1970f1d7262a5afc33b02fc8002bef611cf638deab)では、新しいレイアウトでのタブレット用デッキの起動時クラッシュが修正されました。

### Newlay 0.3.45が大規模なrelayクエリを切断せずにストリーミング {#newlay-0345-streams-large-relay-queries-instead-of-closing-them}

[Newlay](https://code.relay.tools/opensauce/newlay)は、Android上でホストされるNostr relayと関連するローカルサービスです。その[署名付きの0.3.45リリース告知](https://primal.net/e/b8380ae1bf30492129727ec59e27e2ae8a4cf9ad08e7361826a9ba8be88a227a)によると、大規模なクエリ結果は、クライアントの接続を閉じるのではなく、バックプレッシャーを効かせながらストリーミングされるようになりました。組み込みのGitホストはプッシュ後に不要になったパックを整理し、Cordnの暗号化メッセージングのコーディネーターはサイズの大きいクライアントリクエストを受け付け、プローブがタイムアウトした場合は中止フレームを送信します。

この[リリース](https://primal.net/e/b8380ae1bf30492129727ec59e27e2ae8a4cf9ad08e7361826a9ba8be88a227a)では、Androidの運営者向けに、event、ストレージ、アドレス、管理に関するライブのステータスカードも提供され、16 KBメモリページを持つデバイス向けにネイティブの暗号ライブラリが調整されています。relayとコーディネーターの変更は、前回のストア版である0.3.39以降の複数のリリースにまたがっており、0.3.45はそれらをパッケージ化した区切りです。

### ngit-grasp 3.0.5がGitのプッシュとrelayの同期を止めない {#ngit-grasp-305-keeps-git-pushes-and-relay-sync-moving}

[ngit-grasp](https://gitworkshop.dev/danconwaydev.com/ngit-grasp)は、署名付きのリポジトリ共同作業のためのセルフホスト型Nostr relayおよびGitサーバーです。その[署名付きの3.0.5リリース告知](https://primal.net/e/6ff00b9230e4523e6f14aaf6e5088f91e5696be38b9304a4e1cef384e3318d41)では、時間のかかる履歴の照合を共有のライブ同期アクターから切り離し、以前のeventを確認している間でもrelayのサブスクリプションを開始できるようにしました。レート制限、不完全な履歴クエリ、メールボックスの読み取り、identityの照会のそれぞれについて個別にバックオフを行うため、不調なrelayが再試行の容量を独占することはなくなりました。

[同じリリース](https://primal.net/e/6ff00b9230e4523e6f14aaf6e5088f91e5696be38b9304a4e1cef384e3318d41)では、ローカルのevent一覧と照合して保存済みの履歴の再取得を避け、不完全なサブスクリプションは、その範囲を検証済みとして扱う前に閉じます。Git側では、バックグラウンドの状態昇格によってすでに適用されたプッシュを受け入れ、変更されたrefに対する競合保護を維持し、アップロード中にGitの進捗出力を読み出してプッシュが停止しないようにしています。リポジトリがrelay上では稼働しているように見えても、Gitの転送はまだ確定的な結果を待っている場合があるため、これらの詳細は重要です。

### Armada 0.63.0が署名アプリの種類を問わずプッシュ通知を届ける {#armada-0630-carries-push-alerts-across-signer-types}

[Armada](https://github.com/soapbox-pub/armada)は、暗号化されたコミュニティ、チャンネル、ダイレクトメッセージのためのNostrクライアントです。先週のメディアのプライバシーに関するリリースに続き、その[署名付きの0.63.0告知](https://primal.net/e/34021b55504d74c5d04f55dbfea87f31168a7c4582f35113d7ec063894d19e56)では、アプリが閉じている間も機能する新しいブラウザープッシュの経路について説明しています。これは、他のアカウントの種類に加えて、拡張機能やリモート署名アプリでのログインでも機能します。Armadaを組み込んだホストアプリであるTennaでも、ユーザー向けのバックグラウンド通知が利用できるようになりました。

この[リリース](https://primal.net/e/34021b55504d74c5d04f55dbfea87f31168a7c4582f35113d7ec063894d19e56)では、長いコミュニティチャンネルで古いメッセージをより速く読み込み、新しいメッセージのために履歴全体を読み直すことを避けます。ダイレクトメッセージの入力中表示は、より少ないrelay接続で動作します。デスクトップ版の更新では再起動を促すようになり、0.50.0より古いバージョンからの直接のアップグレードはサポートされなくなりました。

署名付きの[0.63.1の追加リリース](https://primal.net/e/af3ff711c1c1daa4d6a621dc5add0615fc5d37fbb1de31395cb79dcdf820aaf1)では、フォルダーからのインポートと並べ替えに対応した編集可能な絵文字パックが追加され、読み込み済みの履歴より前の引用メッセージも取得し、relayでホストされる返信の相互運用性が確保されました。Androidでの再接続の通信量を減らし、長時間の切断後には古い通知を繰り返さずに追いつき、参加前のメンションを除外し、編集されていないグループのフィールドと非公開のサーバー一覧の項目を保持します。relayでホストされるグループでの削除には、メッセージの作成者または管理者であることが必要になりました。サーバーのドラッグ、不正な形式のrelay情報の処理、リポジトリのサブスクリプションにも修正が入っています。

[バージョン0.63.2](https://primal.net/e/ad0f6ad1a7730a400e8257c494c53ef14597c55a24e01b05dd2b2301c7d3aa36)では、メッセージのMarkdownが、入れ子の引用とリスト、水平線、コードフェンス、下線付きの見出し、リンクやメンションにまたがる書式に対応しました。TenorとGiphyのページリンクはGIFとして再生されます。既読状態の同期で転送されるデータが減り、再接続では冗長なダウンロードとログインを避け、Androidのバックグラウンド通知は、大規模な設定更新が殺到したときにrelayの同期を一時停止します。

### deed 0.3.0〜0.3.2がZigでのNostr公開を安定化 {#deed-030032-makes-zig-nostr-publishing-steadier}

[deed](https://github.com/zig-nostr/deed)は、Nostrのeventを読み取って公開するためのZig製コマンドラインツールです。その[9月24日のバージョン0.3.2](https://github.com/zig-nostr/deed/releases/tag/v0.3.2)ではエージェントスキルが追加され、relayへのpingの期限が修正されました。その前の[0.3.1](https://github.com/zig-nostr/deed/releases/tag/v0.3.1)と[0.3.0](https://github.com/zig-nostr/deed/releases/tag/v0.3.0)のリリースでは、パフォーマンスと公開の信頼性が改善されています。3つのタグは、初期段階の1つのツール系列を示しています。目に見えるNostrでの利点は、CLIを使うスクリプトにとって、relayへの接続とeventの公開経路がより安定することです。

### Cordn 0.5.1がコーディネーターの障害時にも他のグループを動かし続ける {#cordn-051-keeps-other-groups-moving-when-a-coordinator-fails}

[Cordn](https://github.com/Cordn-msg/cordn)は、会話のコーディネーターを見つけるためにNostrのidentityとrelayを使う、MLSで暗号化されたグループメッセンジャーです。その[署名付きの0.5.1クライアントリリース](https://primal.net/e/23f7498e2e405e05c4d3075ccc522c753d80f37b954a81ff8ecb3268f2dc7dc6)は、先週のオフラインキューの作業に続き、コーディネーターとoutboxのスケジューリングを分離しました。利用できないコーディネーターが、無関係なグループの送信を遅らせることはなくなりました。解決済みのrelayヒントは発見後も保持され、グループの文書がそれらをデバイス間で運び、永続的な公開保留の記録によって取り残された送信が復旧されます。複数デバイスでの復旧では、現在の設定を読み取りながら、履歴チェーンと欠落部分のクエリを並行して行います。

この[リリース](https://primal.net/e/23f7498e2e405e05c4d3075ccc522c753d80f37b954a81ff8ecb3268f2dc7dc6)では、ドロップしたファイルの添付、グループのピン留め、プレビューと通知でのプロフィール名、コーディネーターのラベルも追加されました。最初の未読位置、未読カウンター、重複した通知、メディアとシステムメッセージのプレビュー、キャプション付きメディアに付けられた返信、画像のズーム操作が修復されています。ネイティブ版のダウンロードでは「名前を付けて保存」の選択画面が使われます。遅れて現れた署名アプリによって、暗号化が未対応であるという誤った警告が出ることはなくなり、アカウントの切り替えがバックグラウンドでのシード処理と競合することもなくなりました。

### Nymbot 1.0.7がローカルでの文書処理と暗号化されたチャット共有を追加 {#nymbot-107-adds-local-document-handling-and-encrypted-chat-sharing}

[Nymbot](https://zapstore.dev/apps/ai.nymbot)は、暗号化されgift-wrapで包まれたNostrのメッセージを通じて利用するアシスタントです。その[開発者署名付きの1.0.7リリース](https://primal.net/e/affd11e97fb3438965780aa01732e8d0e0f9b2162b87ab0f3019dff93449673e)では、デバイス上で文書を読み取り、ファイルが大きすぎてそのまま送れない場合は関連する箇所を選び出し、使用したページを示します。会話は、後からアクセスを取り消せるエンドツーエンド暗号化のリンクを通じて共有できます。PythonとJavaScriptの返答はローカルで実行でき、その出力は会話に返されます。

[同じリリース](https://primal.net/e/affd11e97fb3438965780aa01732e8d0e0f9b2162b87ab0f3019dff93449673e)では、送信前に価格が表示される出典付きのリサーチ、画像編集、メッセージごとのモデル選択、チャットごととボットごとの支出上限が追加されました。MCPで接続された外部ツールは、データを変更する前に確認を求めます。リポジトリでの実行では、変更をレビューのために一時停止し、CIの結果を表示し、ゲートウェイが混雑した後に再開できます。返信の候補、ピン留めされたお知らせ、折りたたまれた出典の一覧、検索可能なモデル選択画面がこの更新を締めくくります。これらの主張は開発者のリリースノートに基づくものであり、Compassはこのアプリのプライバシーを独自に監査していません。

### 0xchat 1.5.6が署名とメッセージ認証の修正を出荷 {#0xchat-156-ships-its-signing-and-message-authentication-fixes}

[0xchat](https://github.com/0xchat-app/0xchat-app-main)は、プライベートチャット、外部署名、ウォレット機能を備えたNostrメッセンジャーです。[バージョン1.5.6](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.6-release)は、[先週ソースのマージとして取り上げた](/en/newsletters/2026-09-23-newsletter/#0xchat-merges-fixes-for-signing-message-authentication-and-redirect-flaws)セキュリティ修正を出荷しています。これには、gift-wrapの認証、信頼できるインフラの設定、埋め込みページでの署名に対する同意が含まれます。また、Torプロキシを迂回する経路を塞ぎ、onion以外のホストに対してTLS証明書を検証し、リリースビルドが機密性の高い可能性のある認証情報やウォレットの情報をデバイスのコンソールに書き込まないようにしました。オプトインの開発者ログでは、引き続きエラーが記録されます。

この[リリース](https://github.com/0xchat-app/0xchat-app-main/releases/tag/v1.5.6-release)では、relayへの再接続の間隔を3秒から5分まで段階的に延ばし、再接続後のサブスクリプションを修復し、relayの接続中にキューに入ったリクエストを配信します。アカウントを切り替えても重複したrelayのリスナーが蓄積しなくなり、ログインに失敗してもすでに有効なアカウントは維持され、外部署名アプリとの接続は起動をまたいで保持されます。送信に失敗した場合はエラーが表示され、未送信のテキストや復旧可能なトークン共有の状態が保持されるようになりました。起動時の鍵の復号とアップロード時のハッシュ計算はUIスレッドの外に移され、チャットとビデオのキャッシュによって繰り返しの描画とダウンロードが避けられます。このリリースでは、Play署名のAndroid APKとソースからビルドされたWindowsインストーラーを含む、SHA-256チェックサム付きのAndroid版とデスクトップ版のアセットが提供されています。

### Nostr Mail Client 0.17.0がメールボックスの操作をrelayから隠す {#nostr-mail-client-0170-hides-mailbox-actions-from-relays}

[Nostr Mail Client](https://github.com/nogringo/nostr-mail-client)は、従来のメール配信にも対応しながら、Nostrを通じてメールをやり取りします。[先週の受信者ごとのトランスポートとメディアのプライバシーに関するリリース](/en/newsletters/2026-09-23-newsletter/#nostr-mail-client-0160-adds-per-recipient-delivery-choices)に続き、[バージョン0.17.0](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.17.0)では、既読、アーカイブ、フォルダー、ラベルの状態とそのタイミングをrelayから隠し、送信者に通知せずにメールを削除できるようになりました。古いクライアントには新しい状態や削除が見えないため、このリリースではすべてのデバイスを同時に更新する必要があります。また、32 KBを超えるメールでBccの受信者を保護し、ローカルの連絡先の別名を送信メッセージに含めないようにし、AmberのQRログインを修復し、公開メールを受信者の読み取り用relayへ公開します。

この[リリース](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.17.0)では、送信者、件名、添付ファイルによるルールを備えた色付きのフォルダーとラベル、返信と転送での引用、貼り付けたインライン画像、添付ファイルのプレビューと名前の変更、メール一覧での範囲選択が追加されました。転送では元の画像と添付ファイルが保持され、返信の引用は折りたたまれた状態で始まり、ウェブ版のエディターにはコンテキストメニューが加わりました。HTMLの表とインライン画像がより正確に描画され、プレーンテキストのリンクが機能し、予約送信は最大5年先までの日付に対応します。アドレス帳の名前と画像がインターフェース全体に表示され、テーマの色はシステム、提案、カスタムのパレットから選べます。

[同じリリース](https://github.com/nogringo/nostr-mail-client/releases/tag/v0.17.0)では、ファイルから選んだ背景をローカルに保持し、リンクされた背景をキャッシュしますが、明示的な移行の手間が伴います。ネイティブプラットフォームでは、以前のファイル背景を追加し直す必要があります。既定のrelayとメディアの推奨設定が変更され、オンボーディングと更新のお知らせにNostrアプリの紹介が加わり、他のクライアントが書き込んだ未知の設定が保持され、中断されたメールストアの作成とLinuxのパッケージングが修復されています。起動に失敗した場合は、空白の画面ではなく、詳細とあらかじめ記入されたレポートが表示されるようになりました。

### Nostr WoT 0.8.7が認証を接続先に結び付ける {#nostr-wot-087-binds-authentication-to-the-destination}

[Nostr WoT](https://github.com/nostr-wot/nostr-wot-extension)は、Nostrの署名と信頼のツールを組み合わせたブラウザー拡張機能です。[バージョン0.8.7](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.7)では、[NIP-98](/ja/topics/nip-98/)の署名付きHTTP認証に対する同意を、正確なURL、クエリ、メソッド、アカウント、要求元のオリジンについて求めるようになりました。以前の広範な承認には、改めて同意が必要です。[NIP-42](/ja/topics/nip-42/)のrelay認証にはアカウントに結び付いた別の権限システムがあり、サイト固有の拒否が共有のrelay許可よりも優先されます。認証のリクエストは検証済みのトップレベルのブラウザーオリジンから送られる必要があり、承認やロック解除の待機の後には、アカウントとアクセスの確認が再度行われます。

この[リリース](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.7)では、リモートの[NIP-46](/ja/topics/nip-46/)の署名と承認されたevent全体を検証するため、返された署名が内容や接続先を黙って差し替えることはできません。ウォレットのプロビジョニングとアドレスの変更では、本文に結び付いた認証、1回限りのバックエンドのチャレンジ、個別の取引トークンが使われます。一般的なウェブサイトでの署名によって、これらの内部ウォレットトークンを発行することはできません。互換性のあるバックエンドを先に展開する必要があり、クライアントは廃止されたエンドポイントへのダウングレードを拒否します。Nostr Wallet Connectの支払いでも、返された支払いのプリイメージを要求した請求書のハッシュと照合し、一致しない場合は結果不明として扱います。

[リクエストのインターフェース](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.8.7)では、ユーザーは生のevent全体を確認し、サイトのグループ内で特定のリクエストを選び、プライベートメッセージをウェブサイトへ返すことを承認せずにローカルで閲覧できます。ローカルのプレビューは30秒後に自動的に隠れます。届いたリクエストは未選択のままで、通常の一括承認には認証が含まれません。拡張機能はサイトごとと全サイト共通のrelay許可を区別し、検証済みプロフィールのキャッシュに上限を設け、タイムスタンプが同じreplaceable eventはevent IDの小さい方で決着させ、ホームのポップアップでの公開の読み取りをローカルに保ちます。ChromeとFirefoxには個別に検証されたパッケージと、順番に実行される安定版リリースの申請ワークフローが用意されていますが、これらのワークフローは現在ストアで入手できることを証明するものではありません。

### Irisの共有ランタイムがrelayとピアの履歴の一貫性を保つ {#iriss-shared-runtime-keeps-relay-and-peer-history-consistent}

[nostr-pubsub](https://github.com/mmalmi/nostr-pubsub)は、永続的なeventストレージと送信用の公開キューを備えた共有のNostr eventランタイムを提供します。[バージョン0.5.7〜0.5.13](https://github.com/mmalmi/nostr-pubsub/releases/tag/nostr-pubsub-ts-v0.5.13)では、完全一致のサブスクリプションをまとめて処理し、再接続後に再実行し、ローカル、relay、ピアの各証拠を区別して保持し、永続ストレージに障害が起きた場合は履歴が不完全であることを報告します。完了したクエリは、受信したすべてのeventの受け入れ処理が終わるまで待ちます。既定のrelayバッチは一般的なサーバーとの互換性のためにORフィルターを最大20個までに抑えるようになり、ピアのバッチは独立した照合とキャンセルを維持します。

[Hashtreeのランタイム更新](https://github.com/mmalmi/hashtree/releases/tag/hashtree-ts-runtime-v0.5.13)では、ワーカー固有のネットワーク処理を、この共有ランタイム、永続的なeventインデックス、送信キューに置き換え、eventとキャッシュされたファイルが1つのFIPSノードを共有できるようにしました。[FIPS TypeScript 0.0.44〜0.0.45](https://github.com/mmalmi/fips-ts/releases/tag/runtime-v0.0.45)では、完全なシグナリング記録に十分な容量を持つ経路を選び、ハンドシェイクの期限内に失われたセッション確立を復旧し、明示的なルーティングの拒否があった場合にのみWebRTCの応答を再試行します。より大きなフレーム化されたWebSocket経路には互換性のあるネイティブのピアが必要で、0.0.44のノートでは、先にネイティブのFIPS 0.4.85を展開する必要があるとされています。

[Iris Kit 0.2.5](https://github.com/mmalmi/iris-kit/releases/tag/runtime-v0.2.5)では、アカウント鍵とオフラインでの読み取りを保ったまま、永続的なプレーンeventのアプリケーションクライアントと、トランスポートに依存しない[NIP-46](/ja/topics/nip-46/)署名が追加されました。[バージョン0.2.6](https://github.com/mmalmi/iris-kit/releases/tag/runtime-v0.2.6)では、ワーカーまたはネイティブのバックエンドから、検証済みの完全なevent IDを即座に返します。プレフィックスやreplaceable eventのクエリは、最新の値を選ぶ前に引き続き履歴を待ちます。これらはライブラリのリリースであり、ノートはすべてのIrisアプリケーションへの展開を示すものではありません。

[Iris Meetの9月30日のソース更新](https://github.com/irislib/meet/commit/9bebb074895fd34574c3a92056612cf3891de74b)では、NDKとの統合を、永続的なpublish/subscribeの基盤と共有のidentity署名アプリに置き換えました。このパッチでは、オフラインでのidentityの復元、NIP-07署名、会議室の分離に関するテストが追加されています。既存の[会議アプリ](https://github.com/irislib/meet)は、暗号化されたシグナリングにNostrを、音声とビデオにWebRTCを使っています。これはデフォルトブランチでの実装の進展であり、リポジトリにはこの特定の更新がライブサイトに反映されたことを証明するタグ付きリリースはありません。

### Chamaが掲載の取り消しとバックグラウンド通知を伝播 {#chama-propagates-listing-cancellation-and-background-alerts}

[Chama](https://github.com/jesuspirate/chama)は、コミュニティでの取引とプライベートな会話に署名付きeventを使います。[バージョン6.4.14〜6.4.16](https://github.com/jesuspirate/chama/releases/tag/v6.4.16)では、掲載をローカルで削除する前に署名付きの取り消しを公開するため、他のクライアントもキャッシュされた同じオファーを取り下げられます。受信者を起こすためのwake tagが送信者の通知設定とは関係なくeventに付けられるようになり、通知サーバーは署名付きeventによって重複を排除するため、参加直後のチャットでも起動を引き起こせます。バックグラウンドのジョブは保存されたカーソルから影響を受けた取引を再処理し、失敗したチェーンを隔離し、通知テキストをローカルで復号します。このリリースでは、付属の監視プロセスを再展開する必要があります。

[まとめて公開されたリリース](https://github.com/jesuspirate/chama/releases/tag/v6.4.16)では、参加者の更新を署名されたevent時刻の時点で適用し、席の期限切れ後に行われた資金ロックを隔離し、保存された持参人払いのノートの復旧手段を示します。クレームの公開は、インポートまたは支払いが確認されるまで待ちます。掲載のフィルターはコミュニティの範囲をまたいで閲覧者の通貨を保持し、取引のヘッダーには確定した参加金額が使われます。これらの変更により、Nostrに接続された2つのクライアントが同じevent履歴から推測する内容がそろいます。

### Earthly 0.1.12が再利用可能な地図設定を追加 {#earthly-0112-adds-reusable-map-configurations}

[Earthly](https://github.com/zeSchlausKwab/earthly)は、署名付きの公開と暗号化された共有を備えた[Nostrの共同地図エディター](https://github.com/zeSchlausKwab/earthly/blob/v0.1.12/README.md)です。[バージョン0.1.12](https://github.com/zeSchlausKwab/earthly/releases/tag/v0.1.12)では、公開されたGoogleマイマップ向けの再利用可能なGMapper設定、開発者が作成したMapletの発見、設定の非公開保存または公開、出典を明示したジオメトリのコピーが追加されました。同じリリースでは、暗号化された接続の共有、エンティティのドロップ、モバイルでのチャットのナビゲーションも追加されています。Googleのエクスポートの可否とブラウザーのCORSによってインポートは制限され、ダウンロードした実行可能なMapletはTauriでは引き続き利用できず、Android実機でのアップグレードの確認はまだ保留中です。

[設定に関する作業](https://github.com/zeSchlausKwab/earthly/pull/29)では、既存の公開アドレスと設定を移行し、設定の更新をレビューまたは取り下げる機能を追加しました。最初のAndroidワークフローはコンパイル前に失敗しましたが、[ツール関連の修正](https://github.com/zeSchlausKwab/earthly/pull/30)によって、その後にタグ付けされたリリースの準備が整いました。

### Mostro 0.19.0が第1世代のトランスポートを廃止 {#mostro-0190-retires-its-first-generation-transport}

[Mostro](https://github.com/MostroP2P/mostro)は、Nostr上でピアツーピアの取引を調整します。[バージョン0.19.0](https://github.com/MostroP2P/mostro/releases/tag/v0.19.0)では、[第1世代のgift-wrapトランスポートの削除](https://github.com/MostroP2P/mostro/pull/1004)が出荷されたため、クライアントは新しいプロトコルを使う必要があります。既存の注文作成と紛争開始のタイムスタンプtagは、保存される値を変えずに[`published_at`へ名称変更](https://github.com/MostroP2P/mostro/pull/1000)されました。外側のeventの`created_at`は引き続き署名時刻を表します。復元の応答は取引相手の取引鍵を返し、受け付けられた作成と引き受けの操作は取引鍵を認識し、relayへの公開は最初の肯定的なrelayの確認で完了します。同じリリースでは、保証金の期限と取り消しを更新し、取引が解決したときに紛争を閉じ、解決担当者に通知し、中継される価格の鮮度に上限を設けています。

Mostroの[取引鍵の受け入れに関する修正](https://github.com/MostroP2P/mostro/pull/1006)では、最初の注文や紛争がコミットされた時点で鍵を認識します。初回接触に対してより厳しいproof of workを課すノードでは、以前は定期的な既知の鍵の更新まで、正当な後続メッセージを破棄することがありました。しきい値が既定どおり同じ場合は影響を受けませんでした。[紛争のトランザクション](https://github.com/MostroP2P/mostro/pull/923)は、注文の遷移と紛争の行をアトミックにコミットし、状態の不整合による障害を解消します。[解決時の通知](https://github.com/MostroP2P/mostro/pull/945)では、ユーザー同士が紛争を解決したときに、担当の解決者へベストエフォートでプライベートメッセージを送ります。既存のreplaceable eventは、オフライン時の予備手段として残ります。

### SCRUTINY Lensがセキュリティ研究をNostrにもたらす {#scrutiny-lens-brings-security-research-onto-nostr}

9月29日に最初の公開リリースとなった[SCRUTINY Lens v0.1.0](https://github.com/crocs-muni/scrutiny-lens/releases/tag/v0.1.0)は、Nostrを通じて公開されたセキュリティメタデータのためのブラウザークライアントです。アナリストは、CVE、パッケージ、証明書の識別子で検索し、eventの履歴と撤回を調べ、対象のグラフで関係を探索できます。ブラウザーはeventの署名と識別子を検証します。任意のAI検索と説明機能はユーザーが選んだエンドポイントを使い、アプリは引用された出典を基になるeventと照合します。[リリースノート](https://github.com/crocs-muni/scrutiny-lens/releases/tag/v0.1.0)では、relayの制約が明示的に説明されており、まだ隣接するリポジトリを必要とするローカルビルドの依存関係も示されています。

### MangatsuとNotedsがAndroidに登場 {#mangatsu-and-noteds-reach-android}

[Mangatsu v0.1.11](https://github.com/imattau/Mangatsu/releases/tag/v0.1.11)は、このコミックの閲覧と公開のためのアプリにとって、今週の最初のAndroidリリース系列の一部です。その[ソース](https://github.com/imattau/Mangatsu/commit/543d6d3dde3bffe293b7336d0fb6f4c82532fe13)では、外部の署名アプリにNostrの操作の承認を求めるためのAndroidインターフェースである[NIP-55](/ja/topics/nip-55/)を通じたAmberログインが追加されています。コミックと章はNostrのeventであり、ページはBlossomサーバー上に置かれます。リーダーは暗号化された保存済みライブラリとオフラインでの閲覧にも対応しています。その後のコミットでは、署名アプリの呼び出しとrelayリストの更新に対応しています。

[Noteds v0.1.2](https://github.com/imattau/noteds/releases/tag/v0.1.2)は、Tauriを通じてNostrのクラシファイド広告マーケットプレイスをAndroidにもたらします。その[Android署名アプリとの連携](https://github.com/imattau/noteds/commit/c9294999134196e9d98c011440c7ca0ed5fcc398)では、AndroidのNIP-55署名を使います。アプリは掲載とメッセージをNostrで公開し、カテゴリー、地理的な地域、任意のブラウザー埋め込みを使ってローカルの検索グラフを構築します。最新のソースでは、近隣検索のためのネイティブの位置情報アクセスが修正されています。どちらのプロジェクトも初期段階のリリースであり、GitHubのリリースページには詳細なノートがないため、これらの機能はタグ付けされたREADMEと実装のコミットに基づいています。

### StatimがNostrのDMを他のネットワークと統合 {#statim-combines-nostr-dms-with-other-networks}

[Statim v0.4.0](https://github.com/alaibe/statim/releases/tag/v0.4.0)は、9月23日の最初のリリースに続くものです。[タグ付けされたソース](https://github.com/alaibe/statim/blob/v0.4.0/README.md)では、XMTP、Status、Telegram、Matrixと並んでNIP-17のNostr DMに対応したメッセンジャーとして説明されています。アカウントはローカルに保持されるリカバリーフレーズから始まり、これらのネットワークはそれぞれ異なるプライバシー特性を持つため、各会話にはそのプロトコルが表示されます。Android版には現在Telegram連携がありません。これらはプロジェクトが文書化した機能であり、独自にテストされた保証やアプリストアでの入手可能性の確認ではありません。

## 開発中の変更 {#in-development}

### Amethystが暗号化グループの相互運用性を修復 {#amethyst-repairs-encrypted-group-interoperability}

[Amethyst](https://github.com/vitorpamplona/amethyst)は、Marmotの暗号化グループに対応したAndroid向けNostrクライアントです。White Noiseも別のMarmotメッセンジャーであり、[そのクライアントとともにテストされた相互運用性の修正一式](https://github.com/vitorpamplona/amethyst/pull/4245)は、グループ管理、削除時の文言、その他2つのクライアントが会話を共有したときに表面化した挙動に対処しています。より的を絞った修正では、[リアクションと削除をMarmotグループ内で送信する](https://github.com/vitorpamplona/amethyst/pull/4233)ようにし、別個の[NIP-17](/ja/topics/nip-17/)のgift-wrapで包まれたプライベートメッセージとして送ることをやめ、さらに[別のクライアントによる編集を再起動後に適用する](https://github.com/vitorpamplona/amethyst/pull/4240)ようになりました。これらはソースのマージであり、PRに記載されたテストは、公開されたクライアント間のリリースよりも範囲が限られています。

別の[Cordnのグループランタイムとインターフェースのマージ](https://github.com/vitorpamplona/amethyst/pull/4201)では、コーディネーターサーバーを経由する暗号化グループのもう1つの経路が追加されました。CordnはMarmotとは別物であるため、この2つの変更を1つのトランスポート移行として読むべきではありません。

Amethystはまた、[GeodeリレーとQuartzクライアントにおけるHTTP経由のrelayコマンド](https://github.com/vitorpamplona/amethyst/pull/4231)を、自身の[NIP-FE](/ja/topics/nip-fe/)提案の下でマージし、replaceableなプロフィールとリストのevent向けの[バックアップ競合のレビュー画面](https://github.com/vitorpamplona/amethyst/pull/4174)もマージしました。NIP-FEはプロジェクトの提案上の用語です。バックアップの流れでは、置き換えを受け入れる前にバージョンを比較でき、ローカルの状態が黙って上書きされることを防ぎます。

Amethystは、ArmadaとAccordionが使う別個の暗号化コミュニティプロトコルであるConcordも開発しています。[準拠性に関する修正一式](https://github.com/vitorpamplona/amethyst/pull/4262)では、分割されたコミュニティ一覧、ピン留めの証明、鍵のローテーションと解散の記録が追加され、続いて[消えるメッセージと直接の招待](https://github.com/vitorpamplona/amethyst/pull/4264)が追加されました。招待は承認されるまで非公開の受信箱に留まり、受け取ってもコミュニティのrelayには接続しません。同じ変更では、別の作成者による削除でメッセージが消えてしまう可能性のあった作成者の比較も修正されています。[クライアント間の修正](https://github.com/vitorpamplona/amethyst/pull/4265)では、署名されていないrumorのシリアライズ、招待の欠落したフィールド、relayで確認されたコミュニティの作成、再起動なしでの参加が修復されています。報告されたエミュレーターでのテストには、稼働中のArmadaとAccordionのピアが参加していました。

その後の[プライベートチャンネルの実装](https://github.com/vitorpamplona/amethyst/pull/4277)では、関連するアクセスの取り消し後にチャンネル鍵をローテーションし、作成、非公開化、公開化、鍵の再生成の操作を追加しています。また、ランクを確認する協調的なキックを追加し、メッセージの添付ファイルを親メッセージとともに期限切れにします。WebXDCの更新は別個のチャンネルバッファーに入れられますが、AmethystにはまだWebXDCアプリケーションのホストがありません。この後の修正一式で報告されているのはwire形式と単体テストであり、デバイスや稼働中のrelayでの検証はないため、先の相互運用性の結果が新たに追加されたすべての操作を保証するわけではありません。

QuartzのMLSエンジンは、[スキップされたメッセージ世代のシークレットを再起動後も保持する](https://github.com/vitorpamplona/amethyst/pull/4271)ようになり、保存された状態を復元した後でも、順序が入れ替わったメッセージを復号できます。[過去のエポックを4つ保持する](https://github.com/vitorpamplona/amethyst/pull/4272)ことで、呼び出し側は遅れて届いたアプリケーションメッセージを認証し、その認証済みデータを保持し、消費済みの世代が再び開かれることを防げます。[シークレットツリーの更新](https://github.com/vitorpamplona/amethyst/pull/4275)では、ts-mls形式の状態から展開されていないノードのシークレットを読み込みます。[送信者ごとの古い世代に関するエラー](https://github.com/vitorpamplona/amethyst/pull/4270)は、クライアント自身のラチェットの衝突と、他のメンバーによるリプレイを区別します。PRでは、Marmotの既存の保持エポックによるフォールバックは別個のままであると明記されているため、これはエンジンの機能であり、Amethystのすべてのメッセージ経路がそれを使っていることの証明ではありません。

[Quartzのtag読み取りの監査](https://github.com/vitorpamplona/amethyst/pull/4267)では、平文で公開される可能性のあった非公開のgeohashの項目と、`nsec`の秘密鍵を公開鍵として扱っていたパーサーが修正されました。リポストのアドレス、チャンネルの非表示対象、ライブルームのルートtag、addressableなミントeventも修復されています。廃止された`ForkTag`リーダーは削除され、Quartzの利用者にとってはソースAPIの変更となります。既存のSQLiteのミントの行には、引き続き別途のマイグレーションが必要です。[追加のeventモデル](https://github.com/vitorpamplona/amethyst/pull/4282)はBuzzのプロジェクトコンテナー、アーティファクトのリビジョン、チームの提案を対象とし、[ビデオ視聴と暗号化されたプッシュ制御のモデル](https://github.com/vitorpamplona/amethyst/pull/4266)はDivineのスキーマに従っています。これらの追加で確立されるのは解析と構築への対応であり、完全なクライアントのインターフェースや、番号付きのNIPとしての採用ではありません。

クライアントはまた、Android 14以降のフィードと全画面ビューアーで[Ultra HDR写真を表示](https://github.com/vitorpamplona/amethyst/pull/4284)できるようになりました。Android 15以降では、フィードでの輝度の引き上げは通常の範囲の2倍までに制限され、全画面ではディスプレイの全範囲を使えます。報告されたテスト用デバイスはより新しいAndroid APIで動作していたため、Android 14と15は未テストのままです。[共有UIとアップロード処理の移植のマージ](https://github.com/vitorpamplona/amethyst/pull/4278)では、140の画面をAndroidとデスクトップの共通コードに移し、Androidのメディア処理をUIスレッドの外に移しました。その監査ではメタデータ削除のエラー報告も復元されており、このリファクタリングは単なるファイルの移動にとどまりません。

### Divineがダイレクトメッセージに暗号化されたビデオを追加 {#divine-adds-encrypted-video-to-direct-messages}

[Divine](https://github.com/divinevideo/divine-mobile)はNostrのビデオクライアントです。[NIP-17](/ja/topics/nip-17/)は、送信者をrelayから隠す暗号化されたgift wrapでプライベートメッセージを運びます。Divineの[マージ済みのビデオメッセージの作業](https://github.com/divinevideo/divine-mobile/pull/9486)では、添付したビデオをデバイス上で暗号化し、暗号文をアップロードし、復号鍵をそのプライベートメッセージ内で送信します。受信者はファイルを検証して復号し、再生または保存できます。別の[履歴復元の修正](https://github.com/divinevideo/divine-mobile/pull/9446)では、他のrelayがまだ応答できる場合に、あいまいなrelayの拒否によって復旧が早々に終わってしまうことを防ぎます。

Divineの[廃止されたモデレーション鍵に関する修正](https://github.com/divinevideo/divine-mobile/pull/9603)では、モデレーションラベルの解決で廃止された鍵を拒否し、報告が提出されたときに現在の報告先を選びます。廃止された鍵宛ての保留中の報告はビルドに固定された鍵へ振り向けられ、未解決の会話には書き込めないままになります。この変更では、未成年者がどの過去のスレッドを読めるかを判断する際に、廃止された鍵の管理状況も区別します。管理状況の更新には、引き続きアプリケーションのリリースが必要です。[削除されたコメントのキャッシュ処理](https://github.com/divinevideo/divine-mobile/pull/9677)では、正常に削除された最近のコメントが、スレッドの再読み込み時に再び表示されることを防ぎます。

クリエイター向けには、[ライブのカラーマスク録画モード](https://github.com/divinevideo/divine-mobile/pull/9598)で、撮影前に置き換え後の背景をプレビューでき、[白い壁のマスキング](https://github.com/divinevideo/divine-mobile/pull/9701)では、ビデオプラグインを通じて明るさに応じたマスキングが加わりました。[単語ごとの字幕](https://github.com/divinevideo/divine-mobile/pull/9652)は、認識された単語のタイミングを保持し、サーバーがまとまった字幕しか提供しない場合はおおよそのタイミングを使います。[ストップモーションの続き](https://github.com/divinevideo/divine-mobile/pull/9698)では、既存の構成のペースで新しい静止画を追加し、[切り離したクリップを戻す機能](https://github.com/divinevideo/divine-mobile/pull/9645)、[グループ化されたフォント選択](https://github.com/divinevideo/divine-mobile/pull/9654)、[速度のプリセット](https://github.com/divinevideo/divine-mobile/pull/9601)は、Nostrのevent形式を変えずに編集の操作を追加します。

[正方形での書き出しの位置合わせ](https://github.com/divinevideo/divine-mobile/pull/9694)とその[小さなクリップ向けの追加修正](https://github.com/divinevideo/divine-mobile/pull/9703)では、解像度の異なるクリップが混在していても、テキストとステッカーの位置が保たれます。[サードパーティのHLS再生](https://github.com/divinevideo/divine-mobile/pull/9664)では、インポートされたプレイリストを繰り返し事前にバッファリングする代わりに、ループの境界で先頭へシークすることで、Androidのヒープクラッシュを回避します。そのため、ループは再開のたびに短く止まることがあります。[アカウント設定の再読み込み](https://github.com/divinevideo/divine-mobile/pull/9680)では、アカウントに結び付いたフィルターを切り替え時に既定値のまま保ち、デバッグ時のサインインに関するアサーションの一部も修正しています。別のモデレーションラベルの更新に関する問題はまだオープンであるため、PRはすべてのサインインのエラーが修正されたとは主張していません。

### Buzzがrelayのチャンネルとidentityの制御を拡張 {#buzz-extends-its-relays-channel-and-identity-controls}

[Buzz](https://github.com/block/buzz)は、独自のrelayとクライアントを持つNostrベースのワークスペースです。その[マージ済みのチャンネルアーティファクトの実装](https://github.com/block/buzz/pull/7919)では、編集可能な記録に1つの所属チャンネルとリビジョンのチェーンを与え、競合する編集が両方とも先頭になることはありません。プロジェクトの[NIP-AR](/ja/topics/nip-ar/)という名称は、確立されたNostrの標準ではなく、プロジェクト自身の提案と実装を指しています。

保護されたHTTPの受け入れ口に対しては、別の[マージ済みの変更](https://github.com/block/buzz/pull/7264)により、フェデレーテッドidentityアサーションを、[NIP-98](/ja/topics/nip-98/)の認可で証明された同じ鍵と組み合わせます。NIP-98は署名付きのHTTP認証eventを定義しており、Buzzの[NIP-FI](/ja/topics/nip-fi/)アサーションはプロジェクトの仕様です。Buzzは[秘密鍵のバックアップエンベロープ向けのHPKE暗号化](https://github.com/block/buzz/pull/7849)もマージしました。このPRはソースレベルでのセキュリティの作業を確立するものであり、すべてのクライアントへの配布はまだ確認されていません。

[Buzz desktop 0.5.26](https://github.com/block/buzz/releases/tag/desktop-v0.5.26)には、チャンネルアーティファクトの作業、ネイティブのHPKEによる秘密鍵バックアップの暗号化、デスクトップ用のrelay管理コンソールが含まれています。共有部分の変更では、非公開のプロジェクトチャンネルへのリクエストを修復し、サイドバーのセクション、並べ替え、スター、ミュートをデバイス間で同期し、長いスレッドの読み取りに上限を設け、Blossomのidentityアサーションを厳格化しています。[リポジトリ全体のノート](https://github.com/block/buzz/releases/tag/desktop-v0.5.26)では、relayのidentityのペアリング、コンパニオンへのメンション配信、設定可能なプッシュURL、アトミックな管理上の削除、モバイルでの文脈に応じた名前が別途記載されています。デスクトップのリリースが確立するのはデスクトップと共有部分の配布であり、それらのモバイルの変更がモバイルビルドで出荷されたことを証明するものではありません。

Buzzの[WebSocketでのNIP-FIの強制](https://github.com/block/buzz/pull/7224)では、フレームを受け入れる前にフェデレーテッドidentityアサーションを確認し、そのNostr鍵が、relayに対してクライアントのidentityを証明する[NIP-42](/ja/topics/nip-42/)で認証された鍵と一致することを求めます。セッションは、トークンの有効期限、アサーションの最大経過時間、設定された接続の有効期間のうち最も早いもので期限切れとなり、期限切れの後は新たな作用を一切受け入れません。このプロジェクト固有のNIP-FIモードは既定で無効です。すでに受け入れられた音声のコミットとサブスクリプションの設定は、停止した依存先を待ち続ける可能性があるため、この変更によって切断までの時間に普遍的な上限が設けられるわけではありません。

[所有者による削除の準備](https://github.com/block/buzz/pull/7830)では、運営者が証明したリクエストを、インベントリに結び付いた自動承認を経て既存の削除実行機能へ移します。[relayの追加修正](https://github.com/block/buzz/pull/7969)では、同じリクエストを再試行すると現在の状態が返るようにし、削除が完了するまで所有者の有効な割り当てを確保しておきます。恒久的に保持されるホストの削除記録は、生涯で20コミュニティという上限に数えられます。これらはソースレベルでの管理上の変更であり、追加修正では、relayと排出処理の実行機能が稼働するまで削除を無効のままにするよう運営者に指示しています。別に、[パーティションカタログの監査](https://github.com/block/buzz/pull/6515)では、新しいeventと配信ログのパーティションを作成する前に、すべてを受け止めるパーティションと対象外の月を検出し、運用上の安全性と監査の鮮度を運営者に示します。

Buzzのモバイル版では、同じ表示名を持つ人とエージェントを区別できるようになりました。その[identity名の解決機能](https://github.com/block/buzz/pull/7894)は、エージェントを所有者の名前で修飾し、必要な場合にのみ短い鍵の接尾辞を付けます。[会話への統合](https://github.com/block/buzz/pull/7895)では、作成者、メンション、メンバー構成の通知にこれらの名前を使います。[一覧、検索、Pulse](https://github.com/block/buzz/pull/7896)により、会話の外でも同じ挙動がそろいます。表示上の修飾はローカルのラベルを変えるだけで、選択されたメンションはidentityの元のwire上の名前を保持します。

### Conduitがrelayの受け入れ後にチェックアウトを進める {#conduit-advances-checkout-after-relay-acceptance}

[Conduit](https://github.com/Conduit-BTC/conduit-mono)は、販売者にプライベートな注文メッセージを送るNostrマーケットプレイスです。[段階的なrelayへの公開](https://github.com/Conduit-BTC/conduit-mono/pull/483)では、最初の肯定的なrelayの確認と、すべてのrelayへの試行の完了を区別し、[チェックアウトの追加修正](https://github.com/Conduit-BTC/conduit-mono/pull/488)では、先へ進む前にその最初の確認を永続化します。relayの受け入れが意味するのは署名付きの注文がrelayに届いたことであり、販売者がそれを読んだり処理したりしたことの証明ではありません。

Conduitは、[復旧可能なリモート署名のセッション](https://github.com/Conduit-BTC/conduit-mono/pull/529)と[トランザクション型の署名アプリとrelayの交渉](https://github.com/Conduit-BTC/conduit-mono/pull/533)もマージしました。[NIP-46](/ja/topics/nip-46/)では、アプリケーションが別の署名アプリに保持された鍵に署名を要求できます。これらの変更では、トランスポートの修復中もユーザーのアカウントのワークスペースを保持し、再開前に正確なアカウントを検証します。PRが確立するのはソース上の挙動であり、出荷されたチェックアウトのビルドではありません。

Conduitの[ランク付き商品検索のマージ](https://github.com/Conduit-BTC/conduit-mono/pull/575)では、kind 30402の商品に対して通常の[NIP-50](/ja/topics/nip-50/)全文検索クエリを1件送信し、署名の確認、リビジョンの照合、ローカルでの適格性のフィルタリングを通じて、relayによる関連度の順序を保持します。商品を特定する読み取りがバックグラウンドで終わる前にカードが表示されることがあり、より新しい署名付きの削除が引き続き優先されます。更新と再試行は、広範なカタログの探索を始めるのではなく、検索と特定商品の読み取りの範囲内にとどまります。100件の結果の上限の後にローカルでフィルタリングを行うため、該当する商品を取りこぼすことがあり、部分的に空の応答には復旧の手段が示され、商品が存在しないことの証明にはなりません。

### ElisymがNostrのコマース用チェックアウトを構築 {#elisym-builds-a-nostr-commerce-checkout}

[Elisym](https://github.com/elisymlabs/elisym)は、商品に署名し、プライベートな注文と領収書のメッセージをNostrで運ぶコマースツールキットを開発しています。その[マージ済みのcommerceパッケージ](https://github.com/elisymlabs/elisym/pull/120)はオファーの検証とgift-wrapで包まれた注文eventを定義し、[チェックアウトのインターフェース](https://github.com/elisymlabs/elisym/pull/131)はオファーの確認、ウォレットでの支払い、配送状況を扱い、[セルフホスト型の販売者ノード](https://github.com/elisymlabs/elisym/pull/133)はストア側をパッケージ化しています。プロジェクトはkind `30490`を暫定的なものとし、10月の最小限の機能群について説明しています。これらのソースのマージが確立するのは形になりつつある統合であり、承認されたNostrのコマース標準や完全な公開開始は示されていません。

Elisymの[エージェント向けチェックアウトツール](https://github.com/elisymlabs/elisym/pull/136)は、Nostrで告知された商品向けに`buy_product`と`get_order`を追加します。最初の呼び出しは注文せずに見積もりを返し、2回目の呼び出しで、同じエージェントとネットワークに対する1回限りの見積もりと警告を受け入れます。注文の状態は、エージェントのローカルのファイルバックエンドに永続的に保存されます。[Tempoのチェックアウト対応](https://github.com/elisymlabs/elisym/pull/137)では、販売者の検証と配送を伴うブラウザーウォレットでの支払い経路が追加されます。送信済みのトランザクションハッシュがあると、結果が確定するまで試行が有効なまま保たれるため、ブロードキャストがまだ決済される可能性がある間に未払いの結果を返すことを避けられます。

[その後のチェックアウトの修正](https://github.com/elisymlabs/elisym/pull/139)では、ブラウザーウォレットが探索中にすぐに名乗り出た場合でも、署名付き商品のチェックアウトを初期化できるようにしました。このソースの変更では、そのコールバックが実行される前にセッションの宣言を移しています。マージだけでは、ホストされた環境での展開は確認されません。

### nostterが署名アプリの確認とeventの取得を改善 {#nostter-improves-signer-checks-and-event-retrieval}

[nostter](https://github.com/SnowCait/nostter)はNostrのソーシャルクライアントです。その[マージ済みの署名アプリの機能確認に関する変更](https://github.com/SnowCait/nostter/pull/2573)では、フォローとリアクションの操作を提示する前に、使用できる署名アプリがあるかを確認します。[新しいピン留めのtag](https://github.com/SnowCait/nostter/pull/2611)は、作成者の鍵と既知のrelayヒントを、推測で補うことなく運びます。[replaceable eventのキャッシュの順序付け](https://github.com/SnowCait/nostter/pull/2608)は、[NIP-01](/ja/topics/nip-01/)のタイムスタンプとevent IDによる決着の規則に従います。NIP-01は、クライアントがreplaceable eventのどれを選ぶかを含む、Nostrのeventの基本規則を定義しています。

### Pensieveが分離されたアーカイブの照合を準備 {#pensieve-prepares-isolated-archive-reconciliation}

[Pensieve](https://github.com/andotherstuff/pensieve)は、Nostrのアーカイブと復旧のためのツールです。その[マージ済みの分離されたnegentropyランタイム](https://github.com/andotherstuff/pensieve/pull/60)は、同期処理に上限のあるワーカーと永続的な完了時の挙動を与えます。この機能はオプトインであり、PRでは本番のサービスや設定は有効化されていないと明記されています。これはより安全な復旧経路に向けた土台であり、稼働中の展開の証拠ではありません。

### ContextVMがrelayをまたいだ重複呼び出しを回避 {#contextvm-avoids-duplicate-calls-across-relays}

[ContextVMのTypeScript SDK](https://github.com/ContextVM/sdk)は、ツールとリソースのリクエストをNostrのeventとして運びます。その[マージ済みの受信時の重複排除の修正](https://github.com/ContextVM/sdk/pull/103)では、複数のrelayや再接続によって同じ平文のリクエストが再び届いた場合でも、event IDによって1件のリクエストとして認識し、既存のラップされたメッセージの経路と動作をそろえます。PRによると、修正前は冪等でない1つのツールが、1回の呼び出しに対して3回実行されていました。付随する[リソース通知の変更](https://github.com/ContextVM/sdk/pull/101)では、更新をサブスクライブしているクライアントにのみ送信します。サブスクリプションを持たない初期化済みのセッションは、もうそれらを受信しません。

### CyberspaceがDECK-0003のオブジェクト規則を改訂 {#cyberspace-revises-the-deck-0003-object-rules}

[Cyberspace](https://github.com/arkin0x/cyberspace)は、構造化されたNostrのオブジェクトと暗号化された領域バッグのためのDECK-0003形式を開発しており、先週号の時点でAmethystがその実装を始めていました。新しい[パーツと隠しオブジェクトの規則](https://github.com/arkin0x/cyberspace/pull/36)と[バッグの参照](https://github.com/arkin0x/cyberspace/pull/38)により、バッグはすべてのパーツを埋め込む代わりに、別途公開されたオブジェクトを参照できます。その後の[訂正](https://github.com/arkin0x/cyberspace/pull/40)では、relayが置き換え後に古いバージョンを破棄する可能性があるため、event IDによる参照ではaddressable eventの古いバージョンを確実に固定できないとしています。読者は訂正された座標による参照の規則を使うべきであり、以前のマージの文言はすでに置き換えられています。

### WispがNostrのコメントへの返信を修正 {#wisp-fixes-replies-to-nostr-comments}

[Wisp](https://github.com/barrydeen/wisp)は、relayのルーティングとウォレットの機能を備えたNostrクライアントです。先週リリースされた[NIP-22](/ja/topics/nip-22/)のコメント対応に続き、[マージされた追加修正](https://github.com/barrydeen/wisp/pull/667)では、NIP-22のコメントへの返信も、適切な親とルートの参照を持つコメントeventになりました。以前の経路では常に通常のノートが公開されていました。NIP-22では、さまざまな種類のNostrコンテンツにコメントを付けられます。この修正はWispの1.2.5タグの後にマージされており、そのノートはバージョンを上げただけなので、これはソースレベルの進展であり、リリースされたかはまだ確認されていません。

### Cordnがコーディネーターの所在を2台目のデバイスに送信 {#cordn-sends-coordinator-locations-to-a-second-device}

[Cordn](https://github.com/Cordn-msg/cordn)は、Nostr上で暗号化されたグループメッセージングを調整します。その[マージ済みの複数デバイスに関する仕様変更](https://github.com/Cordn-msg/cordn/pull/9)では、グループのコーディネーターのrelayヒントを、複製されるグループ文書に含めて運びます。これにより、新たにシードされたデバイスは、既定のrelayにないコーディネーターを見つけられるようになり、過去のメッセージもライブのメッセージも取得できないグループに参加したように見えることがなくなります。これは先週のCordnのオフラインキューのリリースに続くプロトコル文書の作業であり、新しいクライアントのリリースではありません。

### Nostr Atlasが検証可能なidentityのディレクトリを公開 {#nostr-atlas-opens-a-directory-for-checkable-identities}

[Nostr Atlas](https://nostr-atlas.web.app)は、Nostrのプロフィールを外部アカウントに関するクレームとともに表示する新しいディレクトリです。その[マージ済みのサイト公開](https://github.com/saiy2k/nostr-components/pull/148)では、ディレクトリをプロジェクトのコンポーネントのデモから切り離しており、サイトは公開で応答しています。[クレームの流れのマージ](https://github.com/saiy2k/nostr-components/pull/144)では、Xのアカウント所有者がブラウザーの署名アプリで署名付きの[NIP-39](/ja/topics/nip-39/)証明を公開でき、[プロフィールの拡充](https://github.com/saiy2k/nostr-components/pull/146)では、証明が検証された後にのみkind-0のNostrメタデータを読み取ります。NIP-39は、Nostrの鍵を別のオンラインidentityと関連付けるための証明の形式を定義しています。relayの確認だけでは、クレームが検証済みとはみなされません。

### nostr-javaがメディアホスティングのツールを追加し、tagの位置を保持 {#nostr-java-adds-media-hosting-tools-and-preserves-tag-positions}

[nostr-java](https://github.com/tcheeric/nostr-java)は、Nostrアプリケーション向けのJavaライブラリとMCPツール群です。その[マージ済みのBlossomツール](https://github.com/tcheeric/nostr-java/pull/557)では、呼び出し側がハッシュでアドレス指定されたメディアをアップロード、検索、一覧表示、削除でき、ユーザーのサーバー一覧を管理できます。別の[公開に関する修正](https://github.com/tcheeric/nostr-java/pull/558)では、空のtagの値をその位置に保持します。Nostrのtagは位置に意味があるため、空のrelayヒントを落とすと、マーカーが誤ったフィールドへずれ、公開されたeventが承認されたプレビューと異なるものになる可能性がありました。

### Zap Cookingがアカウント履歴の復旧方法を変更 {#zap-cooking-changes-how-account-history-can-be-recovered}

[Zap Cooking](https://github.com/zapcooking/frontend)は、レシピを共有するNostrクライアントです。その[マージ済みのLazarus復旧の作業](https://github.com/zapcooking/frontend/pull/753)では、[NIP-78](/ja/topics/nip-78/)のアプリケーション固有データeventの上に構築されたバックアップを、relayに保持されたreplaceable eventのバージョンを走査して、上書きされたフォロー、ミュート、プロフィールを検出する方式に置き換えました。Lazarusは引き続きドラフトのプロトコルです。復旧は古いバージョンを保持しているrelayに依存しており、ウェブクライアントのPRがマージされたことは、失われたすべてのeventを復旧できることの保証ではありません。

このクライアントは、ノートと返信のための[任意のNIP-13 proof-of-workの操作](https://github.com/zapcooking/frontend/pull/743)と、[添付ファイルのモデル](https://github.com/zapcooking/frontend/pull/752)によりプレビューと公開の間でメディアの順序と[NIP-92](/ja/topics/nip-92/)の説明を一致させる変更もマージしました。[NIP-13](/ja/topics/nip-13/)では、送信者が投稿前にローカルで計算を費やしてeventに付与できます。NIP-92は、メディアのメタデータをeventのtagとして運びます。

Zap Cookingの[NIP-05クレームの修正](https://github.com/zapcooking/frontend/pull/763)では、正確なリクエスト本文に対する[NIP-98](/ja/topics/nip-98/)の認可を必須とし、名前をクレームしている公開鍵と異なる署名者を拒否します。以前は、この公開のエンドポイントが認証されていないクレームを受け付けており、他のメンバーの名前を置き換えられる可能性がありました。メンバーシップの階層は既存のメンバーシップの記録から取得されるようになり、リモート署名アプリのユーザーにはクレーム時に署名の確認が表示されます。別の信頼されたサーバー側の登録経路は変更されていません。

[ミュートリストの修復](https://github.com/zapcooking/frontend/pull/764)では、プロフィールからのミュート操作が、kind 10000のリスト全体を公開鍵のtagだけで置き換えることを止めました。以前の経路では、単語、ハッシュタグ、スレッドの項目と暗号化された内容が消去され、ある画面では復号された非公開のミュート鍵が公開で再公開される可能性がありました。新しい経路ではrelay上のコピーを読み取り、無関係なtagと暗号文を保持し、その読み取りができない場合は公開を拒否します。非公開のミュートを解除するには、署名アプリを通じた復号と再暗号化が必要です。

### OpalがOmarchyにリモート署名をもたらす {#opal-brings-remote-signing-to-omarchy}

[Opal](https://github.com/derekross/opal)は、Omarchy Linux環境向けに作られたデスクトップのNostr署名アプリです。その[9月28日のバージョン0.3.3](https://github.com/derekross/opal/releases/tag/v0.3.3)は、最初の公開系列に続き、[NIP-46](/ja/topics/nip-46/)のリモート署名への対応、ローカルのキーリング、接続されたアプリからのリクエストに対する権限のインターフェースを提供しています。NIP-46では、アカウント鍵を署名アプリ側に置いたまま、別のクライアントが操作の承認を求めます。これはプラットフォーム固有の署名アプリの初期リリースであり、より広いデスクトップへの対応を主張するものではありません。

### WatchTowerがNIP-86のrelay管理パネルを公開 {#watchtower-opens-a-nip-86-relay-control-panel}

[WatchTower](https://github.com/iqbqioza/watchtower)は、認証付きのrelay管理リクエストのためのプロトコルであるNIP-86を通じてrelayを管理する、新たに公開されたパネルです。[公開インスタンス](https://watchtower.nostrfy.org)が応答しており、運営者はインターフェースを確認できます。リポジトリは9月22日に作成されました。サイトにアクセスできることは、その認可の流れが独自に監査されたことや、すべてのrelay実装で動作することを示すものではありません。

### Hubstr Blossomが個人用のメディアオリジンを公開 {#hubstr-blossom-opens-a-personal-media-origin}

新たに公開された[Hubstr Blossomサーバー](https://github.com/johninnis/hubstr-blossom)では、Nostrクライアントが画像、ビデオ、ファイルをセルフホスト型のBlossomエンドポイントにアップロードし、そのURLをeventに入れられます。READMEには、ローカルのコンテンツハッシュによる保存、SQLiteのインデックス、変更に対する署名付きのkind-24242の認可、そしてアップロード、ミラーリング、一覧表示、削除のためのさまざまなBlossomの操作が記載されています。公開の読み取りにより、他のクライアントはアップロード権限を受け取らずに、投稿されたメディアを表示できます。

[サーバーの文書化されたオプション](https://github.com/johninnis/hubstr-blossom)では、共有メディアを説明する[NIP-94](/ja/topics/nip-94/)のevent向けにファイルのメタデータを抽出することもできます。サーバーはEXIFメタデータを除いて画像を再エンコードでき、既定でミラーリングのリクエストがプライベートネットワークを対象にしないよう防御します。これはデプロイ手順を備えた新たに公開された実装であり、本番環境で広く展開されている証拠ではありません。

[Hubstr Relay](https://github.com/johninnis/hubstr-relay)は、9月24日に最初のソースを公開しました。これは個人用のSQLiteのeventキャッシュと公開relayを組み合わせたもので、認証していない読み手は許可された公開eventを閲覧でき、NIP-42で認証したテナントは自分のキャッシュを読み取れます。NIP-17のgift wrapは、ゲストの読み手には引き続き提供されません。その[9月25日の更新](https://github.com/johninnis/hubstr-relay/commit/0ae1a551ac50da0b7097105b76591dbc4d6cc023)では、NIP-86の公開鍵一覧のメソッドが返す記録が修正されています。

### Meshstrが許可不要のrelayメッシュを実験 {#meshstr-experiments-with-a-permissionless-relay-mesh}

[Meshstr](https://gitlab.pocketlabs.dev/meshstr/meshstr)は、Nostr relay同士がピアの予算を交渉し、署名付きの利用状況の受領証を交換するためのalpha段階の設計です。その最初の実装には、9月27日に追加された[Nostr relayであるstrfry向けの書き込みポリシーのブリッジ](https://gitlab.pocketlabs.dev/meshstr/meshstr/-/commit/6d609fc99f)が含まれており、翌日にはソケットの修正が加わりました。リポジトリでは、DIDCommによる交渉と、ピアが完全な一覧を交換せずにeventの集合を比較できる[NIP-77](/ja/topics/nip-77/)の照合に加えて、合意した予算を超えたピアについての検証可能な報告が説明されています。

これらの[プロジェクトの規則](https://gitlab.pocketlabs.dev/meshstr/meshstr)は提案であり、採用されたNIPでも、実証された公開のrelayネットワークでもありません。今週の具体的な進展は、relayの書き込みポリシーを提案中のメッシュの計上の仕組みに接続するコード経路が公開されたことです。

### Dossierが公開されたNostrの履歴から何が明らかになるかを示す {#dossier-shows-what-a-public-nostr-history-can-reveal}

[Dossier](https://github.com/satanrayshe/dossier)は、自分のNostrとLightningの足跡を確認するための新しいブラウザー上の自己監査ツールで、[公開デモ](https://satanrayshe.github.io/dossier/)があります。表示されているプロフィールのリンク、zapの痕跡、投稿時刻、古い[NIP-04](/ja/topics/nip-04/)の暗号化ダイレクトメッセージのメタデータ、写真のEXIFなどのメディアのメタデータを収集し、削除しようとしたeventをまだ提供しているrelayを示すこともできます。[NIP-07](/ja/topics/nip-07/)の署名アプリに対応しているため、ユーザーはページに秘密鍵を貼り付けずに整理の操作を承認できます。

プロジェクトの[文書化された制約](https://github.com/satanrayshe/dossier)は重要です。スキャンで見えるのは到達できるrelayだけであり、削除リクエストで他の場所に保持されたコピーを消すことはできません。リポジトリは9月27日に登場し、タグ付きリリースはありません。デモとソースが確立するのは初期段階のツールであり、誰かの過去の活動の完全な一覧ではありません。

### Marmot MDKが投票、カスタム絵文字、アカウントのメタデータを拡張 {#marmot-mdk-extends-polls-custom-emoji-and-account-metadata}

[Marmot MDK](https://github.com/marmot-protocol/mdk)は、暗号化されたNostrのグループメッセージングのためのランタイムとバインディングを提供します。その後のMDKのソースのマージでは、集計結果と同じ有効回答の規則を使って、[投票者ごとの投票の選択をページング付きで](https://github.com/marmot-protocol/mdk/pull/2094)公開しています。[アプリケーションが所有する任意のグループコンポーネント](https://github.com/marmot-protocol/mdk/pull/1929)により、ホストは管理者が制御する設定を持てるようになり、それはメッセージの保持期間を越えて残り、新しく参加した人にはWelcomeで届けられます。[tag付きの送信とメディアへのリアクション](https://github.com/marmot-protocol/mdk/pull/2105)では、カスタム絵文字のメタデータをランタイムとバインディング全体に運び、エポックが変わった後も添付されたリアクション画像の復号情報を保持し、偽造された添付ファイルのtagを拒否します。この変更によりCのアップロードリクエストの構造体が拡張されるため、Cの利用者はヘッダーに合わせて再ビルドする必要があります。

[収束に関する訂正](https://github.com/marmot-protocol/mdk/pull/2093)では、正規のブランチが選ばれなかった場合に、現在の状態を試さずにメッセージを無効にするのではなく、保留のままにします。付随する[到達不能な経路の整理](https://github.com/marmot-protocol/mdk/pull/2095)では、未解決のステージングされたコミットを、保持された再試行の挙動へ回します。[暗号化メディアの読み取り](https://github.com/marmot-protocol/mdk/pull/2097)では、HTTPの読み取りタイムアウトを再開可能な本文のアイドル処理と一致させ、停止した大容量の転送に対処していますが、保留中の受信APKのデバイス受け入れテストに合格したとは主張していません。[起動段階のマーカー](https://github.com/marmot-protocol/mdk/pull/2098)は、アカウントを開くどの段階でタイムアウトしたかを示し、根本的な起動時の停止が解決したとは主張せずに診断の手がかりを追加します。

ローカルのエージェントコネクターも、kind 0の更新を公開するときに[既存のプロフィールメタデータをマージする](https://github.com/marmot-protocol/mdk/pull/1969)ようになり、リクエストで省略されたフィールドを保持します。[グループプロフィールの更新](https://github.com/marmot-protocol/mdk/pull/2096)では、グループの名前と説明の変更を、現在の管理者が認可する既存の経路を通じて公開します。ソケットの認証では引き続きローカルAPI全体へのアクセスが許可されており、このマージで主体ごとの権限付与が追加されるわけではありません。これらのソースの変更は、タグ付けされた0.11.0リリースの後に続くものです。

### rust-nostrがrelayのcount応答を対応付け {#rust-nostr-correlates-relay-count-replies}

Nostrアプリケーション向けのRustライブラリおよびSDKである[rust-nostr](https://github.com/rust-nostr/nostr)は、[対応付けられたCOUNT応答と、より明確な待機エラー](https://github.com/nostrdevkit/nostr/pull/1478)をマージしました。SDKはCOUNTを送信する前にサブスクライブし、一致する応答だけを受け入れるため、受信側が失われたり閉じられたりしたことが、正当なゼロとして見えることはなくなります。また、公開の確認とrelay認証について受信側のエラーを保持するため、呼び出し側は確認がないことと明示的な拒否を区別できます。公開メソッドのシグネチャは変わりません。

### ZapTrackerがNostrのネットワークと引用の指標を追加 {#zaptracker-adds-nostr-network-and-quote-metrics}

[ZapTracker](https://github.com/pratik227/zap_dashboard)は、Nostrでのエンゲージメントとウォレットの活動のためのクリエイター向けダッシュボードです。[ネットワークダッシュボードのマージ](https://github.com/pratik227/zap_dashboard/pull/133)では、Lightningネットワークの統計を、nostr.watchから取得したオンラインのNostr relayのデータとNIP-11文書の機能情報に置き換えました。[引用指標の変更](https://github.com/pratik227/zap_dashboard/pull/135)では、いいね、リポスト、ブックマーク、zapと並んで、`q` tagを持つkind 1のeventを数えます。これにより、クリエイターはコンテンツのランキングとエンゲージメントのグラフで引用を確認できますが、これはまだマージされたソースの証拠にとどまります。

### LaWallet NWCがカードへのチャージをカードのウォレットへ振り向ける {#lawallet-nwc-routes-card-top-ups-to-the-card-wallet}

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc)は、Nostr Wallet Connectを通じてLightningウォレットをアプリケーションに接続します。その[BoltCardのチャージに関するマージ](https://github.com/lawalletio/lawallet-nwc/pull/316)では、カードのウォレットのNWC `make_invoice`メソッドを通じて請求書を作成するLUD-19の支払いリンクを告知します。ブロックされた、無効化された、またはペアリングされていないカードは支払いリンクを告知せず、この経路が所有者の別個のLightningアドレスへチャージを振り向けることはありません。[追加修正](https://github.com/lawalletio/lawallet-nwc/pull/319)では、同じリンクをエミュレーターでも公開し、LNURLでの送金で受信者が受け付けた支払者のメモを運びます。

### 新しいkhatru relayが所有者向けのモデレーション操作を公開 {#a-new-khatru-relay-exposes-owner-moderation-controls}

[nostr-relay-khatru](https://github.com/rzazo24/nostr-relay-khatru)は、終了したHiveScope専用の実装から派生した汎用relayとして、9月29日に最初のソースを公開しました。[公開インスタンス](https://relay.hivescope.xyz)は、このリポジトリを示し、認証、eventの有効期限、保護されたevent、件数の集計、照合、relayの管理を告知するNIP-11文書を提供しています。[9月30日の実装](https://github.com/rzazo24/nostr-relay-khatru/commit/a6ef7cff9c4f833a6a2f72957d45935c736a0c51)では、所有者パネルにモデレーションの操作が追加されました。公開のメタデータで確認できるのは展開されたエンドポイントであり、告知されたすべてのメソッドのテストに成功したことではありません。

### ローカルのweb-of-trust構築ツールがフォロー解除を追跡 {#a-local-web-of-trust-builder-tracks-unfollows}

[etemiz/wot](https://github.com/etemiz/wot/commit/212fe268dd781c73adad51329be235abc8fd37db)は、9月30日にNostrのweb-of-trustクローラーを公開しました。フォローリストとNIP-65のrelayリストを読み取り、設定可能なルートから信頼度を計算し、relayのポリシー、フィード、スパムフィルターのためにスコアをLMDBに書き込みます。[プロジェクトの文書](https://github.com/etemiz/wot)ではそのトレードオフが説明されています。ライブの更新は信頼度を上げ、定期的な完全なクロールで減少とフォロー解除が反映されます。スコアは選んだルートに依存します。これは新たに公開されたソースであり、タグ付きリリースや本番環境での展開の主張はありません。

### MoyuがMarmotのワークスペースクライアントを公開 {#moyu-opens-a-marmot-workspace-client}

[Moyu](https://github.com/tsgx1990/moyu)は、[Marmot](/ja/topics/marmot/)上に構築され、コマンドライン、ターミナル、デスクトップのインターフェースを備えたRust製のワークスペースチャットクライアントのソースを公開しました。その[9月30日の変更](https://github.com/tsgx1990/moyu/blob/88a20d247510d1cc46ca955564aa395d26ae8e89/CHANGELOG.md)では、ローカルに記録されたメンバー構成の変更を使って、古い参加リクエストによって削除されたメンバーが再び受け入れられることを防ぎ、招待コードを7日後に失効させ、管理者がそれらを取り消せるようにしています。ターミナルの出力では、他のメンバーが送った制御文字とテキストの方向の上書きを除去します。固定されたMDKのフォークでは、Blossomの添付ファイルの転送を設定済みのSOCKS5プロキシ経由で行い、ホスト名の解決もそのプロキシで行われます。0.3.0の変更は公開ソースに含まれていますが、公開のリリースタグやリリースの項目はまだありません。

## プロトコルと仕様の作業 {#protocol-and-spec-work}

### NIP-39がidentityの証明をBlueskyとDiscordに拡張 {#nip-39-extends-identity-proofs-to-bluesky-and-discord}

[NIP-39](/ja/topics/nip-39/)では、Nostrのアカウントが、別のプラットフォーム上のidentityを管理していることの証明を示せます。[9月27日にマージされた変更](https://github.com/nostr-protocol/nips/pull/2486)では、新しい証明に推奨される1つの文を定め、文言が異なっていても、アカウントのnpubを含む古い証明を受け入れるよう検証者に指示しています。また、Blueskyの投稿とDiscordのメッセージを証明の掲載場所として文書化しています。Discordのクレームを確認できるのは、そのメッセージが投稿されたサーバーを閲覧できる人に限られます。

### NIP-86がrelay管理者向けの招待コード管理を追加 {#nip-86-adds-invite-code-management-for-relay-administrators}

Compassは7月8日号で、オープンだった時点の[NIP-86の招待に関する提案](https://github.com/nostr-protocol/nips/pull/2408)を紹介しましたが、これがマージされました。[NIP-86](/ja/topics/nip-86/)は標準的なrelay管理APIを定義し、[NIP-43](/ja/topics/nip-43/)は、制限付きのrelayがメンバーシップを告知し、参加リクエストを処理する方法を定義しています。9月24日のマージでは`listclaims`、`createclaim`、`deleteclaim`が追加され、管理者はrelayが受け付ける招待コードを一覧表示、発行、取り消しできます。これにより、参加後のメンバーに役割を与えうる招待について、運営者に管理の経路が提供されますが、すべてのrelayにこれらのメソッドへの対応を求めるものではありません。

先週の[NIP-86に関する記事](/en/newsletters/2026-09-23-newsletter/#nip-86-adds-clear-and-list-methods-for-relay-management)の訂正です。[マージされた仕様](https://github.com/nostr-protocol/nips/blob/5b9920982ae1f4061328c1b09a90360da28d13c8/86.md)で追加されたのは`unallowevent`、`unbanevent`、`listallowedevents`、`listdisallowedkinds`です。以前の記事では、古い提案の説明にあった名前を挙げていました。最初の2つのメソッドはeventレベルの許可または禁止の決定を取り消し、残りは許可されたeventと許可されていないkindを確認します。

### NIP-51がお気に入りのフォローセットを未使用のevent kindへ移動 {#nip-51-moves-favorite-follow-sets-to-an-unused-event-kind}

[NIP-51](/ja/topics/nip-51/)は、ユーザーのお気に入りのフォローセットの一覧を含む、公開および非公開のリストを定義しています。Compassは7月22日号で[kindの衝突に関する提案](https://github.com/nostr-protocol/nips/pull/2417)を紹介しましたが、これがマージされました。9月27日の訂正では、以前の番号がすでに使われていたため、このお気に入りのリストにkind `10021`を割り当てています。その`a` tagは引き続きkind `30000`のフォローセットを指します。この変更は仕様内の番号の衝突を解消するものであり、人をフォローする新しい方法を作るものではありません。

### NIP-51がスレッドごとの非表示の返信を提案 {#nip-51-proposes-hidden-replies-for-each-thread}

[オープンなNIP-51の提案](https://github.com/nostr-protocol/nips/pull/2489)では、スレッドの作成者が、協力するクライアントで切り替えスイッチの裏に表示される、公開の非表示返信セットを公開できるようにします。スレッドごとに1つのaddressableなkind-30027のeventを使い、ルートのIDを`d` tagとし、`e` tagで返信を指定します。適用されるのは、ルートの作成者が署名したセットだけです。ルートを一覧に含めると、クライアントに他の作成者の返信を非表示にし、返信の作成画面の提供をやめるよう求めますが、返信は引き続きrelayに公開できます。スレッドごとの形式にすることで、編集の衝突は同じ会話の中に限られます。提案者はNostrichでの実装を報告していますが、公開ソースの調査では確認できませんでした。提案は未マージのままで、セットの形式はまだ議論中です。

### NIP-DBが鍵でアドレス指定されるサービス向けの検証済みドメイン名を提案 {#nip-db-proposes-verified-domain-names-for-key-addressed-services}

9月28日に提出された[オープンなNIP-DB提案](https://github.com/nostr-protocol/nips/pull/2487)は、通常のインターネットドメインを、それを提供する鍵に結び付けるNostrのeventについて説明しています。対象となるのは、Nostrの公開鍵でノードをアドレス指定する暗号化メッシュである[FIPS](/ja/topics/fips/)のような、鍵でアドレス指定されるネットワークです。ドメインの所有者は、DNS TXTレコード、またはクレームとともに運ばれるDNSSEC証明によってバインディングを確立でき、クライアントは検証済みの結果をピン留めして、後でオフラインで使います。誰でもNostrのeventで他人のドメインをクレームできるため、提案では検証されていないクレームによる名前の解決を明確に禁じています。[fips-pub-domains](https://github.com/fr34aky/fips-pub-domains)は提案者のリファレンス実装ですが、event kindの番号とオーバーレイ固有の一部の文言はまだレビュー中です。報告されたエンドツーエンドのテストは提案者による証拠であり、この提案が承認されたNIPであることを主張するものではありません。

### プライベートフィードのドラフトが暗号化された受信者グループを検討 {#a-private-feed-draft-explores-encrypted-groups-of-recipients}

9月29日に開かれた[新しい複数受信者向けエンベロープの提案](https://github.com/nostr-protocol/nips/pull/2488)は、想定された受信者が、表示されるtagに通常の公開鍵をさらすことなくeventを見つけられる、プライベートなノート、返信、つながりの概略を示しています。共有シークレットから導出される不透明なペアごとの別名tagと暫定的なevent kindを提案しており、そこには別のNostr eventを数百人の読者向けに包む方法も含まれます。これにより、小規模なプライベートフィードでは、メンバー1人ひとりに別々のメッセージを送るよりも直接的な取得経路が得られる可能性があります。

[提案の作成者](https://github.com/nostr-protocol/nips/pull/2488)は、これを作業中のものだと明言しています。ドラフトには実証された実装もセキュリティレビューもなく、kindの割り当てとバイトレベルの署名規則は未解決のままです。

### Blossomの提案で他の人がミラーしたメディアを告知可能に {#a-blossom-proposal-lets-other-people-announce-mirrored-media}

[オープンなNIP提案](https://github.com/nostr-protocol/nips/pull/2478)は、他の作成者のBlossomのblobをミラーした人が、そのコピーをNostrを通じて告知する方法を説明しています。元のサーバーがblobを失った場合、クライアントはそのコピーを探せます。議論では、告知されたサーバーのヒントが古くなっている場合に、ミラーした人の現在のBUD-03サーバー一覧を確認することも提起されました。これは提案中の発見経路であり、クライアントやアーカイブ用のrelayがすでに予備のストレージを提供していることの保証ではありません。

### 道路のevent報告が共通のNostr形式を模索 {#road-event-reports-seek-a-shared-nostr-format}

[オープンなRoad Event Reportsの提案](https://github.com/nostr-protocol/nips/pull/2479)は、道路の穴、通行止め、カメラ、その他の道路状況についての報告と確認を説明しています。位置情報のtagと、relayがeventの提供をいつやめるべきかを伝える[NIP-40](/ja/topics/nip-40/)の有効期限タイムスタンプを使うため、報告がいつまでも最新のままである必要はありません。提案者は、公開relayから回収したeventのサンプルと、道路状況を報告するための既存の[Roadstrクライアント](https://github.com/jooray/roadstr)に基づいて改訂を行いましたが、ドラフトにはコンパクトなエンコーディングに関する問いがまだ残っており、提案されたNIP番号は採用されていません。

### Marmotが複数デバイスの調整を再検討 {#marmot-revisits-multi-device-coordination}

[Marmotの複数デバイスの再設計](https://github.com/marmot-protocol/marmot/pull/427)では、実装されていなかったExternal Commitのドラフトを、早期のフィードバックを得るための規範的でない解説に置き換えました。新しい方向性では、既存のデバイスが新しいデバイスを承認し、会話に参加させ、後でデバイスを削除する方法を検討しつつ、未解決の問いを明示したままにしています。削除されたドラフトが予約していたIDは、どの実装も採用していなかったため解放されます。このアイデア文書は新しいIDやwire形式を割り当てておらず、実装された複数デバイスの機能でもありません。

## 6年間のNostrの9月 {#six-years-of-nostr-septembers}

9月最後の号は、Nostrが構想段階から、より大きな相互運用可能なツール群へとどのように進んできたかをたどる機会です。[2021年の配車マッチングのプロトタイプ](https://github.com/arcbtc/buber/commit/7a66d400f2)は、署名付きのeventを使ってサービスを調整しました。5年後の今、メンテナーが解決しているのは、[identityの証明の文言](https://github.com/nostr-protocol/nips/commit/0046368a7)や[リストのkindの衝突](https://github.com/nostr-protocol/nips/commit/6631b3eb1)といった細部です。その間に、クライアントは会話、メディア、復旧を一般の人が使える形で提示する方法を身につけてきました。以下の日付入りの資料は、その進展の各段階を示しています。ただし、すべての実験が公開されたことや、古い設計がそれぞれ今も推奨されていることを示すものではありません。

### 2021年9月: 有用な形を持つ初期の実験 {#september-2021-early-experiments-with-useful-shapes}

[9月4日のBUberのコミット](https://github.com/arcbtc/buber/commit/7a66d400f2)は、Nostrのeventを使ったタクシーのマッチングという構想を探るものでした。これは、署名されrelayで運ばれるリクエストが、サービス全体を1つのサーバーに委ねることなく人々を調整できることを示しました。このソースは構想であり、配車サービスが公開されたことを示すものではありません。

同じ月の後半には、[Loquazの9月23日のソース](https://github.com/emeceve/loquaz/commit/d885d93d22)がデスクトップのチャットのプロトタイプを提供しました。これは、relayのメッセージを通常のアプリケーションのように感じさせようとする、もう1つの初期の試みでした。このソースは、完成したエンドツーエンド暗号化や本番環境のメッセンジャーを示すものではありません。後に続く流れは、単純なeventの上に使いやすい会話のインターフェースを探る取り組みです。BUberは配車のマッチングを、Loquazはチャットを試し、どちらも共通のクライアントのパターンが定まる前に署名付きのeventを使いました。これらの試みは、後のクライアントにとって繰り返し現れる2つの問題、つまりrelayを通じた調整と、eventを使いやすい会話として提示することを示しました。

### 2022年9月: チャットと委任された操作が仕様に加わる {#september-2022-chat-and-delegated-actions-enter-the-specifications}

[9月10日のNIP-28の変更](https://github.com/nostr-protocol/nips/commit/3423a6dfb)は、クライアントがまとめて解釈できるメッセージとメタデータを持つ公開チャットチャンネルを説明しました。[NIP-28](/ja/topics/nip-28/)は、共有されたルームを明示的なプロトコル上の対象とし、クライアントに共通のチャンネルの慣習を与えました。

9月23日には、[NIP-26](/ja/topics/nip-26/)の[委任署名に関する記述](https://github.com/nostr-protocol/nips/commit/b62aa418d)が、ある鍵が別の鍵に限られたeventへの署名を許可する方法を文書化しました。これは、2022年の重要な設計上の問い、つまり主鍵をすべてのアプリケーションに渡すことなくNostrのidentityを使うにはどうすればよいか、を捉えたものでした。[NIP-26は現在unrecommendedとされている](https://github.com/nostr-protocol/nips/blob/master/26.md)ため、これは実験の記録であり、新しい統合への助言ではありません。その後のステータスは、署名のモデルがどのように移り変わったかを示しています。提案された解決策が廃止されても、仕様は有用な問題の記述を残せるのです。

### 2023年9月: relayの発見とメタデータを中心にクライアントが成熟 {#september-2023-clients-grow-up-around-relay-discovery-and-metadata}

DamusはNostrのソーシャルクライアントです。その[9月21日の変更履歴](https://github.com/damus-io/damus/blob/master/CHANGELOG.md#16-18---2023-09-21)には、ローカルのNostrデータベース、検索、ハッシュタグのナビゲーションに関する作業が記録されています。これらの変更により、忙しいソーシャルフィードをスマートフォンで閲覧し、復旧しやすくなりました。この日付入りの変更履歴はそのクライアントのリリースの証拠であり、その後のDamusのすべての機能の証拠ではありません。

プロトコルの細部も進んでいました。[9月26日の変更](https://github.com/nostr-protocol/nips/commit/44c21c9d8)では[NIP-24](/ja/topics/nip-24/)の任意のプロフィールメタデータのフィールドが明確化され、[NIP-65の9月29日の変更](https://github.com/nostr-protocol/nips/commit/3b5d3ca67)ではrelay URIの正規化と重複排除が扱われました。[NIP-65](/ja/topics/nip-65/)は、読み取りと書き込みに使うrelayをクライアントが公開する方法を示しています。URIを一貫して扱うことで、文字列に無害な違いがあっても、これらのリストが同じrelayを指せるようになります。この小さな慣習によって、クライアントの設計は信頼できる発見へと近づきました。ある人のeventを見つけるには、それがどこで公開されているかを知る必要があるからです。

### 2024年9月: 投稿がより豊かな文脈を得る {#september-2024-posts-acquire-richer-context}

[Damusの9月22日のリリースノート](https://github.com/damus-io/damus/blob/master/CHANGELOG.md#1101---2024-09-22)では、[NIP-84](/ja/topics/nip-84/)のハイライトとコメントへの対応が説明されていました。NIP-84は、長文の資料の一節を引用して議論する方法を読者に提供します。このクライアントの作業は、プロトコルのアイデアが、人々が読みながら使えるものになった様子を示しています。

一方、[NIP-34](/ja/topics/nip-34/)では、[9月20日の変更](https://github.com/nostr-protocol/nips/commit/ea36ec9ed)によってNostr上のgit共同作業のためのissueの件名とラベルが改良され、[NIP-73](/ja/topics/nip-73/)でも[同じ日の変更](https://github.com/nostr-protocol/nips/commit/79786bb7b)によって外部コンテンツの識別子が改良されました。これらは別々の仕様変更です。一方はリポジトリのissueが構造を保つのを助け、もう一方はeventがNostrの外にある資料を参照できるようにします。どちらも、コンテンツがコミュニティ、リポジトリ、その他のメディアの間を行き来するときに、クライアントが保持できる意味を広げています。

### 2025年9月: アクセス制御と支払いの文脈がより精密に {#september-2025-access-controls-and-payment-context-become-more-precise}

[9月6日のNIP-42の改訂](https://github.com/nostr-protocol/nips/commit/4c5d5fff9)では、複数ユーザーでのrelay認証が扱われました。[NIP-42](/ja/topics/nip-42/)では、relayがクライアントに対し、どのNostr鍵がリクエストを行っているかを証明するよう求められます。この更新は、同じ接続を通じて複数の認証済みアカウントにサービスを提供するサービスにとって重要でした。

[9月15日のNIP-47の更新](https://github.com/nostr-protocol/nips/commit/400d975da)では、Nostr Wallet Connectのリクエストに任意の支払いメタデータが追加されました。[NIP-47](/ja/topics/nip-47/)では、アプリがNostrを通じてウォレットに操作の実行を求められます。文脈が増えることでウォレットとのやり取りは理解しやすくなりますが、メタデータが支払者の詳細をさらす可能性があるため、クライアントとウォレットは引き続きそれを機密情報として扱う必要があります。この変更は、相互運用性の作業が、リクエストを届けられるかどうかだけでなく、受信者が何を知りうるかも扱うようになったことを示しています。

### 2026年9月: 相互運用性の細部が公開のidentityと出会う {#september-2026-interoperability-details-meet-public-identity}

今年の9月には、[マージされたNIP-51の変更](https://github.com/nostr-protocol/nips/commit/6631b3eb1)によって、フォローセットのevent kindが衝突を避けて移動されました。[NIP-51](/ja/topics/nip-51/)は、人が管理して共有できるリストを定義しており、一意のevent kindによって、クライアントはリストの種類を区別できます。以前のCompassの号では提案について論じましたが、9月のマージはステータスの変化です。

2つ目の[NIP-39へのマージされた変更](https://github.com/nostr-protocol/nips/commit/0046368a7)では、証明の文言が明確化され、外部アカウントをNostrのidentityと関連付ける方法が追加されました。[NIP-39](/ja/topics/nip-39/)は検証可能なidentityのクレームに関するものであり、中央のidentity登録簿ではありません。この2つのマージを合わせると、現在のプロトコルの作業が、独立したクライアントが同じidentityとリストのeventを正しく解釈できるかどうかを左右する小さな細部に集中していることがわかります。また、新しいeventのカテゴリーを考案することから、既存のカテゴリーのあいまいさを減らすことへの移行も示しています。

これら6回の9月を通して見えるのは、[署名付きのeventでアプリケーションのリクエストを記述できる](https://github.com/arcbtc/buber/commit/7a66d400f2)ことを証明する段階から、[クライアントが人についてのクレームをどう検証するか](https://github.com/nostr-protocol/nips/commit/0046368a7)を問う段階への進展です。古いプロトタイプが重要なのは、後の仕様とクライアントが答えなければならなかった問い、つまり誰が署名するのか、eventはどこで見つかるのか、それは何を意味するのか、そしてそれを信頼すべきかどうかをどうやって知るのか、を明らかにしたからです。小さく正確なプロトコルの訂正が、新しいインターフェースと同じくらい重要になりうる理由もそこにあります。
