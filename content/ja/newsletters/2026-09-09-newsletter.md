---
title: "Nostr Compass #39"
date: 2026-09-09
publishDate: 2026-09-09
translationOf: /en/newsletters/2026-09-09-newsletter.md
translationDate: 2026-09-11
draft: false
type: newsletters
description: "Nostr Compass #39では、署名付きgitワークフロー、ブラウザからの公開、セルフホスト型ライブ配信、コミュニティリレーへの同意、非公開イベント、目的を絞ったリリース、NIP-21とNIP-27のリンク規約を取り上げます。"
---

Nostrの週刊ガイド、[Nostr Compass](https://nostrcompass.org)へようこそ。

**今週の内容:** [ngitとGitWorkshop](https://ngit.dev/v3)は、署名付きgitワークフローをNostrと[Blossom](/ja/topics/blossom/)上に移し、[nsite-clay](https://github.com/jooray/nsite-clay)はブラウザからの公開を復旧可能にし、[Wingman App](https://github.com/OtherStuffAI/wm-app)はブラウジング、ローカル署名、認証、ファイルを統合します。[ShoshoとLivelier](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0)はセルフホスト型配信をNostrに接続し、[Communitator](https://github.com/dyne/communitator)は署名前にリレーテンプレートを確認できるようにし、[cal.emre.xyz](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743)は予約枠を公開し、[Plektos](https://github.com/derekross/plektos/pull/16)は非公開イベントを暗号化します。タグ付きリリースでは、[Vector](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4)、[Primal Android](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27)、[LibreNostr](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0)、[SkateSpots](https://zapstore.dev/apps/org.skatespots.app)に復旧機能やプライバシー関連の改善が加わりました。開発作業は、[NIP-27](/ja/topics/nip-27/)のレンダリング、[Conduit](https://github.com/Conduit-BTC/conduit-mono/pull/397)における署名付きリレー設定、[NIP-A3](/ja/topics/nip-a3/)の支払先、Blossomミラーに及んでいます。[NIPsリポジトリ](https://github.com/nostr-protocol/nips)にマージされた変更では、ライブ限定サブスクリプションと認証済みアプリケーションデータが明確化されました。詳細解説では、[NIP-21](/ja/topics/nip-21/)リンクとNIP-27参照が、Nostrのプロフィールやイベントをアプリケーション間でどのように受け渡すかを説明します。

## トップニュース

### 署名付きgitワークフローがCI、非公開リポジトリ、リリースをNostr上に移行

[9月8日のv3公開](https://ngit.dev/v3)により、ngit、GitWorkshop、ngit-grasp、ngit-ciが1つの署名付きワークフローに統合されました。[ngit](https://ngit.dev/ngit.git)はブランチ、パッチ、プルリクエストを[NIP-34](/ja/topics/nip-34/)イベントとして扱い、[GitWorkshop](https://ngit.dev/gitworkshop.git)はレビュー用インターフェースを提供します。今回の公開では、セルフホスト型継続的インテグレーションサービスであるngit-ci 0.1も追加されました。その指示と結果は署名付きNostrイベントとしてやり取りされるため、コードレビューと併せて、メンテナーが管理するハードウェア上でチェックを実行できます。

同じリリースでは、[ngit-grasp v3](https://ngit.dev/ngit-grasp.git)がGRASP-08プライベートリポジトリ拡張を通じて非公開リポジトリに対応し、メンテナーの権限も明示されるようになりました。署名付きリリース記録から[Blossom](/ja/topics/blossom/)上のアセットを参照できるため、リリースのメタデータとコンテンツアドレス指定されたファイルの両方を、ホスト型forgeの外部に保持できます。[新しいドキュメントサイト](https://ngit.dev/v3)には、クライアント、非公開リポジトリ、CI、ウェブコンポーネントに関する情報がまとめられています。

### nsite-clayがブラウザからの公開を復旧可能に

[8月31日の署名ツールのプロンプト修正](https://github.com/jooray/nsite-clay/commit/064a0c5350f1e2b107f7d8f1de00ad75ef2e69d8)、[公開処理の復旧機能](https://github.com/jooray/nsite-clay/commit/d1ad514f8068eec2e007059dc62a5b6f1d240ae0)、[9月2日の編集コントロール](https://github.com/jooray/nsite-clay/commit/8f9d7d140dd3cd3e1db8726781fcd852041713f7)により、[nsite-clay](https://github.com/jooray/nsite-clay)は単一ページサイト向けのブラウザ公開ツールになりました。ユーザーはドキュメントオブジェクトモデルをその場で編集し、結果をシリアライズして、コンテンツアドレス指定された[Blossom](/ja/topics/blossom/) blobとしてアップロードし、サイトの[NIP-5A](/ja/topics/nip-5a/)マニフェストを再公開します。ローカルでのビルドやサーバーは必要ありません。

[ブラウザ公開ツール](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/deploy.html)では、失敗した公開処理を復旧できるようになり、署名ツールのプロンプトが繰り返し表示される回数も減りました。[編集ガイド](https://npub12edc7326qsryw5rw5yw0yh57fmj9r8jf4c8xazz6333w305qgnms9ypvj2.nsite.lol/guide.html)には、この一連の手順が記載されています。生成されるサイトは引き続き、既存のゲートウェイで利用できる通常のNIP-5Aサイトです。

### Wingman Appがブラウジング、署名、ファイルを統合

9月の開発では、[ファイルピッカー](https://github.com/OtherStuffAI/wm-app/commit/b0c9c03d317573adeafa92b1a56d696ad399e3ec)、[プロフィール公開](https://github.com/OtherStuffAI/wm-app/commit/f2343add8493625d62a1eb7fb76002ceab73f704)、[安全な署名ツールとセッション復元](https://github.com/OtherStuffAI/wm-app/commit/4e278d96eb9258b89dc8b9639eac7bde3ac475c6)、[テスト済みモバイルビルド](https://github.com/OtherStuffAI/wm-app/commit/60456ec0a8b4ed26ecde53812a61f95dc0bd22ac)が[Wingman App](https://github.com/OtherStuffAI/wm-app)に追加されました。Flutterシェルは、アプリ内で開いたページに[NIP-07](/ja/topics/nip-07/)プロバイダーを注入します。一方、Flight DeckとTowerを基盤とするDriveは、ブラウザの隣に作業画面とファイル用ワークスペースを提供します。

Wingmanは[NIP-98](/ja/topics/nip-98/)を使用して、認証付きHTTPリクエストに署名します。[リクエストの実装](https://github.com/OtherStuffAI/wm-app/blob/67ed27d216e528da5bb431322bd10ac15553796f/crates/wmapp-core/src/auth/nip98.rs)は、サーバーが応答前に検証するイベントを構築します。これにより、端末に設定された1つのIDから、リレー操作、ウェブアプリでの署名、ファイルに対して一貫した承認手順を利用できます。

### ShoshoがLivelierのセルフホスト型ストリームに対応

[Shosho 1.1.0](https://github.com/r0d8lsh0p/shosho-releases/releases/tag/v1.1.0)は9月1日にリリースされ、[Livelier](https://github.com/r0d8lsh0p/livelier)への対応が追加されました。Livelierの[8月31日の帰属情報更新](https://github.com/r0d8lsh0p/livelier/commit/7d8abb875770289502b55c3d947987db08e206dc)では、ブリッジされたプロフィールにブリッジとOwncastのソースが明記されるようになりました。LivelierはOwncastの公開ディレクトリを監視し、動画ストリームがライブ配信中かどうかを確認したうえで、アドレス指定可能な`kind:30311`の[NIP-53](/ja/topics/nip-53/)イベントを公開します。検出情報はNostr経由で配信されますが、動画は引き続き配信者のサーバーから提供されます。

チャットは`kind:1311`イベントとしてブリッジを通過します。[ブリッジの設計](https://github.com/r0d8lsh0p/livelier)では、Nostrリーダーが購読している間だけソース側への接続を開き、派生したアイデンティティーにラベルを付け、一時的なチャットを3時間後に削除するリレーへ送信します。検出用リレーはブリッジキーからのライブイベント書き込みだけを受け入れ、チャットリレーは[NIP-42認証](/ja/topics/nip-42/)と[NIP-70の保護イベントフラグ](/ja/topics/nip-70/)を使用します。

### Communitator、署名前にリレーテンプレートを確認可能に

[8月31日に開始された一連の実装](https://github.com/dyne/communitator/commit/520edd33a253ca3249993172fd1003c80bfd9b7c)により、[Communitator](https://github.com/dyne/communitator)にkind `10002`のリレーリスト、kind `10063`のBlossomサーバー、kind `10050`のプライベートメッセージ受信箱向けの標準テンプレートが追加されました。署名者が接続する前に、アプリケーションは正規化されたエンドポイント、読み取り・書き込み権限、イベントkind、固定された公開先リレー、送信先を表示します。

[範囲を制限した署名・公開フロー](https://github.com/dyne/communitator/commit/2bd04c8fab292e73fe9a4ada250c64358aee8501)では、接続と適用が分離されています。各イベントは個別に署名され、1回の実行で使用するWebSocket接続は最大4つです。また、肯定的な[NIP-01](/ja/topics/nip-01/)の`OK`を受信した場合にのみ、その送信先への配信が成功として数えられます。結果は、完全、部分的、失敗、キャンセル済みの配信を区別します。共有テンプレートは信頼されていない推奨設定として扱われ、[同意画面](https://github.com/dyne/communitator#security-and-consent)では、リレーおよびネットワーク上で観測可能な情報について説明しています。

### cal.emre.xyzがNIP-52の予約可能時間を公開

公開リポジトリは[9月2日の最初のコミット](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743)で開設され、その後、[cal.emre.xyz](https://cal.emre.xyz)について署名済みの[9月3日のハンドラー告知](https://njump.me/6fead386f0f401c2d8641ef842ccc2ade5abb4e45d61bfd7f3872b43db04cdac)が公開されました。主催者は予約可能時間を`kind:31923`の[NIP-52](/ja/topics/nip-52/)イベントとして公開し、参加者は`kind:31925`のRSVPを公開します。

リレーから主催者のイベントと承諾済みの予定ありRSVPを読み取り、重複する時間帯を除外します。Nostrイベントを別のデータベースへコピーせず、そのまま予定調整の記録として使用します。主催者は[NIP-07](/ja/topics/nip-07/)、[NIP-46](/ja/topics/nip-46/)、またはローカルキーで署名でき、参加者は別のキーを生成できます。この[リポジトリ](https://github.com/delirehberi/cal.emre.xyz/commit/611f9516852d0a67a9d0ea558c70308d68f42743)では、生成された`naddr`とカレンダーリンクも提供されており、メールはデフォルトで無効になっています。

### Plektos、プライベートイベントを単一の暗号化チャンネルに統合

[9月2日のプライベートイベント実装](https://github.com/derekross/plektos/pull/12)により、[Plektos](https://github.com/derekross/plektos)の各集まりが、[Concord](/ja/topics/concord-protocol/)暗号化コミュニティー内のプライベートチャンネルとして扱われるようになりました。招待客リスト、RSVP名簿、参加登録ボード、スレッド、寄付、カバー画像、編集、削除がまとめて暗号化されます。招待にはそのイベントのキーだけが含まれ、平文のカレンダーイベントは公開されません。

[9月6日のライフサイクル監査](https://github.com/derekross/plektos/pull/14)では、500件を超えるラップが存在する場合でも直接検索できるよう、イベント定義IDを基準として固定しつつ、ページ分割されたフォールバックも維持しています。招待バンドルはイベント終了から30日後に期限切れとなり、無効化することもできます。ただし、すでにチャンネルキーを取得した人は、そのキーを保持できます。これとは別の[パーサーのセキュリティー修正](https://github.com/derekross/plektos/pull/16)では、不正な型・長さ・値（TLV）形式の[NIP-19](/ja/topics/nip-19/)識別子を受け取った際、パーサーが停止するのではなく処理を失敗させるようになりました。

## タグ付きリリース

### Vector 0.4.4、暗号化コミュニティーの復旧をより安全に

[Vector 0.4.4](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4)は8月31日にリリースされ、コミュニティーの復旧、キーローテーション、モデレーション、返信ルーティングに関する修正が加えられました。再創設時には、攻撃者が使用した招待経路に対して襲撃されたコミュニティーを閉鎖します。置き換え後のメンバーシップは古いローカル状態より優先され、1人のメンバーに到達できないだけで名簿全体が停止することもなくなりました。空のローテーションは拒否され、昇格時にはオンラインのメンバーが維持されます。また、必要なメンバーに到達できない場合、操作は実行されません。

この[リリース](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.4)では、モデレーターによる削除と禁止が永続化され、パスワード変更後にゲストブックが再暗号化されるようになりました。また、再起動後も通知への返信が対応する会話に関連付けられ、検証済みのマルチプレイヤーパスだけが使用されます。これらは復旧のための制御であり、すでに取得されたキーを失効させるものではありません。

### Primal Android 3.5.27、署名者とウォレットのアイデンティティーを確認

[Primal Android 3.5.27](https://github.com/PrimalHQ/primal-android-app/releases/tag/3.5.27)は、[署名者のアイデンティティー確認](https://github.com/PrimalHQ/primal-android-app/pull/1108)と[ウォレットリクエスト認証](https://github.com/PrimalHQ/primal-android-app/pull/1105)が8月31日にマージされた後、9月3日にリリースされました。ローカル署名では、リクエストのアイデンティティーが保持しているアカウントと一致しない場合、そのリクエストを拒否します。また、受信した[NIP-47](/ja/topics/nip-47/)リクエストは処理前に認証されます。Zap投票のルーティングでは、投票が返信内に表示される場合も、投票先をその投票の作成者へ送信します。

### GRAIN 0.8.0-rc2、保存されていないのに受理応答される経路を塞ぐ

[GRAIN 0.8.0-rc2](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2)は9月7日にリリースされた。ストレージ障害により、非同期のLMDBデータベースライターが容量不足を検知する前に`OK`を返せる問題があった。リレーは容量使用率が80％と95％に達した時点で警告し、削除用の空きを残すため97％で新規イベントの受け入れを拒否するようになったほか、受理後に発生したライターの失敗も報告する。保持処理は古いものから順に走査し、終了処理は遅れて到着したメッセージを扱い、無効なフィルターが同列の有効なフィルターまで破棄することもなくなった。

この[リリース](https://github.com/0ceanSlim/grain/releases/tag/v0.8.0-rc2)では、kind `10166`のモニター告知とkind `30166`のリレーレポートも照合し、古くなったレポートを削除し、設定済みリレーをフォールバックとして維持する。また、静的なゼロ値ではなく、実際の制限値と認証情報を[NIP-11](/ja/topics/nip-11/)で報告する。

### LibreNostr 0.5.0～0.5.2、Torルーティングをフェイルクローズ化

[LibreNostr 0.5.0](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0)は9月7日にリリースされた。リレー、ザップ、アップロード、メディア、再生、プレビューを単一のSOCKSポート経由でルーティングするOrbotモードに加え、ザップシートのクラッシュ修正が含まれる。Orbotまたはプロキシが利用できない場合、直接接続に漏れることなく接続を停止する。[Version 0.5.1](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.1)では、低速な[NIP-50](/ja/topics/nip-50/)検索がローカル結果の表示を遅らせる問題を解消した。[0.5.2](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.2)では、再帰的なスレッドレイアウトを置き換え、スレッドの順序を修正した。

この[フェイルクローズ動作](https://github.com/Lwb89dev/librenostr/releases/tag/v0.5.0)は、リリースに記載されたすべてのネットワーク接続箇所に適用される。これらのクライアントは長時間存続するため、再起動が必要になる。パッチリリースでもこの方針は維持されており、同時に、無関係な検索、スタック深度、レイアウトの不具合を抑えている。

### SkateSpots、端末内リレー経路を追加

署名済みの[9月8日付Zapstoreリリース](https://zapstore.dev/apps/org.skatespots.app)では、SkateSpotsにオプションのCitrineリレーが追加された。スポット、クルー、メッセージ、地図データをローカルで読み込めるほか、投稿はオフライン時にキューへ格納され、端末内にもローカルコピーが保持される。既存の保管データとメッセージ内容は、引き続きエンドツーエンドで暗号化される。決済確認では、アクセスを許可したり貢献額として計上したりする前に、インボイス金額とプロバイダー発行のザップ領収書を要求する。

この[ローカルリレー](https://zapstore.dev/apps/org.skatespots.app)は、保存と継続性のための選択肢であり、すべてのリモートリレーを置き換えるものではない。スケーターは接続が途切れている間も作業を続け、後から署名済みのアクティビティを同期できる。一方、決済まわりの変更により、自分で作成した領収書が決済完了の証明として扱われることを防ぐ。

### Whistle 1.8.15、暗号化グループのライフサイクル復旧を修正

[Whistle 1.8.15](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15)は9月3日にリリースされた。Androidのライフサイクルに関する修正により、ルート単位の状態保持オブジェクトが、アプリケーション全体のリレー購読や位置情報の更新を破棄することがなくなった。リリースノートでは、ロックやDozeからの復帰後に接続状態が更新され、確認された事例では未処理だった501件のイベントが復旧したことも説明されている。

この[バグ](https://github.com/sjmcnamara/whistle/releases/tag/v1.8.15)では、長時間存続するサービスの所有権が、短時間しか存続しない画面に結び付けられていた。Activityスコープのインスタンスを存続させ、単発の読み取り前にソケットを確認することで、通常のAndroid画面遷移やバックグラウンドでの休止によって、グループが空であるかのように見える可能性が低くなる。

### TWENTY ONE Companion 1.12.0、暗号化DMを従来のチャットから分離

[TWENTY ONE Companion 1.12.0](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0)は9月5日にリリースされ、[NIP-17](/ja/topics/nip-17/)のギフトラップDMに対応した。暗号化受信箱は従来のスペースチャットから分離されている。従来のメッセージは一度も暗号化されておらず、移行できないため、両者は明確に区別されたままとなる。PDFと動画はリレーのポリシーが許す範囲でサポートされ、個人の非表示設定はモデレーターによる禁止措置にはならずに同期される。

この[視覚的な区別](https://github.com/HolgerHatGarKeineNode/twenty-one-companion/releases/tag/v1.12.0)は、セキュリティモデルの一部である。古い履歴を安全な受信箱と呼べば、その来歴を誤って伝えることになる。一方、黙って移行すれば、作成時には存在しなかった暗号化が施されていたかのような印象を与える。

### ZapStore 1.1.2、イベントidと証明書ローテーションを検証

[ZapStore 1.1.2](https://github.com/zapstore/zapstore/releases/tag/1.1.2)は9月4日にリリースされ、NIP-01のイベントid検証が導入された。クライアントは受信イベントの`id`を再計算し、一致しない場合は使用前に拒否する。このリリースでは、ZapStore以外からインストールされたパッケージも識別できる。サーバー側では、[証明書ハッシュの保持](https://github.com/zapstore/relay/pull/8)により、複数の`apk_certificate_hash`タグが保持されるため、Androidの署名鍵をローテーションしても、承認済みの鍵系統を維持できる。

この[イベントid検証](https://github.com/zapstore/zapstore/releases/tag/1.1.2)により、リレーやキャッシュが古いidを維持したままタグや内容を変更することを防ぐ。インストール元の表示は、同じアプリケーションidを持つAndroidパッケージが別の配布経路から取得された場合に、その出所を別途示す。

### Amber 6.6.1、署名者の応答をリクエストに対応付け可能に

[Amber 6.6.1](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1)は9月4日にリリースされた。権限の解析処理が修正され、任意項目の`kind`が欠けていても処理できるようになったほか、拒否された署名リクエストが元のリクエストidを返すようになった。これにより、呼び出し元のアプリケーションは拒否応答を送信済みの操作と対応付けられる。このリリースでは、リモート署名者のデフォルト設定も更新され、インデクサーリレーが追加された。

これらの[修正](https://github.com/greenart7c3/Amber/releases/tag/v6.6.1)により、双方向の対応関係が維持される。任意項目が欠けていても権限レコードを使用でき、拒否応答も原因となったリクエストに結び付いたままとなる。リレーのデフォルト設定変更は検出に影響するが、署名者によるローカルの認可判断を置き換えるものではない。

## 開発中

### Zap Cookingがリレーヒント付きのNIP-27参照を表示

[9月4日のマージ](https://github.com/zapcooking/frontend/pull/665)により、[Zap Cooking](https://github.com/zapcooking/frontend)は記事、レシピ、エディタープレビュー、印刷表示で`nostr:npub`および`nostr:nprofile`参照を表示するようになりました。無効な識別子はテキストのまま残り、解決処理はノンブロッキングで行われ、エディターでは署名対象となるMarkdownがプレビューされます。リレー情報が存在する場合、単独の`npub`はoutboxリレーと対応する`p`タグを含む`nprofile`になります。

同じ週には、[著者でスコープされたkind `30023`の読み取り](https://github.com/zapcooking/frontend/commit/6a379c680727bb49074a4ff85f070b404dba97a7)が修正され、重複排除と古いクエリに対するガードを備えた[検証済みNIP-50検索リレー](https://github.com/zapcooking/frontend/commit/1802e8d7e95ed482209d09e03c834c2d9adfc1ea)が追加されました。また、依存関係の変更によって残高と履歴が機能しなくなったことを受け、[NIP-47ウォレット呼び出し](https://github.com/zapcooking/frontend/pull/705)が修復されました。

### Conduitが署名済みのリレー設定とBlossom設定を整合

[Conduit](https://github.com/Conduit-BTC/conduit-mono)は、9月2日に[Blossom設定の編集機能](https://github.com/Conduit-BTC/conduit-mono/pull/374)を、9月7日に[署名済み設定の整合処理](https://github.com/Conduit-BTC/conduit-mono/pull/397)をマージしました。MarketとMerchantは、最新の有効なkind `10002`リレーリストとkind `10050` inbox宣言を保持し、より新しいイベントが不正な形式の場合でも使用可能な署名済みリストを維持します。また、明示的な空のリストと取得不能な検索結果を区別し、宣言されたリレーへの接続に失敗してもコード内のデフォルト値で置き換えません。

[kind `10063`エディター](https://github.com/Conduit-BTC/conduit-mono/pull/374)では、それらのサーバーに接続したり、宣言されていないデフォルトを挿入したりすることなく、順序付きHTTPSメディアサーバーリストの読み込み、並べ替え、確認、外部署名、公開、再読み込みが可能です。

### NIP-A3の支払い先が3つのクライアントに導入

9月1日から3日にかけて、[Amethyst](https://github.com/vitorpamplona/amethyst/pull/4041)、[Grimoire](https://github.com/purrgrammer/grimoire/commit/54052506f7a0da06dfc4cf7e969331ee61be7851)、[Pollerama](https://github.com/formstr-hq/nostr-polls/commit/5a015f1d17abecd036f3e10c88d493d23928fa98)がNIP-A3のkind `10133`支払い先を実装しました。Amethystは、互換性のある支払い先が存在する場合にのみオプトイン方式の引き渡しを提供し、それをzapには変換しません。Grimoireは、ウォレットURIを構築する前に固定レジストリを使用します。PolleramaはMoneroアドレスを検証し、支払い先を照会する前に著者のリレーリストを取得します。各クライアントには引き続き、許可された支払い方法、リレールート、正確な表示が必要です。

### DittoがBlossomフォールバックとライブ埋め込みを拡張

[Ditto](https://github.com/soapbox-pub/ditto)は9月6日、[広範なBlossomフォールバックおよびミラーリング](https://github.com/soapbox-pub/ditto/commit/1e35a0705c28f706eb40d1f99aedef3105cf6f07)をマージしました。アバター、バッジ、バナー、コミュニティ画像、カスタム絵文字、アプリケーションアイコンは、同一のblobハッシュを使って宣言済みサーバーからの取得を試みるようになりました。ミラーへのアップロードには、標準のBUD-11認可トークンが使用されます。[9月4日の変更](https://github.com/soapbox-pub/ditto/commit/e2a29004a65122470179c83d6ded8336a5c10dfa)では、コンパクトな`kind:30311`ライブストリーム埋め込みが追加されました。

## プロトコルと仕様に関する作業

### Nostr実装の可能性

[NIP-01](/ja/topics/nip-01/)では、9月4日にマージされた[`limit: 0`フィルターの明確化](https://github.com/nostr-protocol/nips/pull/2460)が行われました。リレーは保存済みイベントを返してはならず、初期クエリの完了時に`EOSE`を送信しなければならず、新たに一致するイベントを受け取るために購読を有効なまま維持しなければなりません。クライアントはローカル履歴を保持しつつ、1つのフィルターフィールドでライブイベント専用の購読を開けます。この明確化では、複数のリレー実装および公開リレーで互換性のある動作が記録されています。

[NIP-78](/ja/topics/nip-78/)には、9月3日にマージされた[認証済みアプリデータの要件](https://github.com/nostr-protocol/nips/pull/2458)が追加されました。リレーはkind `78`および`30078`に対して[NIP-42](/ja/topics/nip-42/)認証を要求することが推奨され、認証されたイベント著者にのみそれらを提供することが推奨されます。これはSHOULDであり、機密性を保証するものではありません。クライアントは、任意のリレーをプライベートストレージとして扱うことはできません。このマージでは、カスタムのアプリデータkindを汎用的な公開データ交換に使用することも非推奨とされています。

[NIP-AC](/ja/topics/nip-ac/)は9月4日、明示的にオープンな[WebRTCシグナリング提案](https://github.com/nostr-protocol/nips/pull/2461)として提出されました。ping、接続要求、offer、answer、ICE candidateには暫定的なephemeral kindを使用し、`p`で宛先を指定し、セッションの`e`タグでグループ化します。kind `30600`は検出をサポートします。ピア同士が直接接続する間、リレーはこれらのシグナリングイベントを配信することが推奨され、保存してはなりません。番号は引き続き暫定的であり、クライアントは[NIP-65リレーリスト](/ja/topics/nip-65/)を使用することが推奨されます。また、機密性を必要とするアプリケーションは、offer、answer、candidateのcontentを[NIP-44](/ja/topics/nip-44/)で暗号化することが推奨されます。

## NIP詳細解説：イベントテキスト内のURIリンクと参照

Nostr識別子を別のアプリケーションで開くには、移送可能な意味を持たせる必要があります。[NIP-21](/ja/topics/nip-21/)は、`nostr:` URIスキームの後に[NIP-19](/ja/topics/nip-19/)識別子を置くことで、ブラウザー、オペレーティングシステム、アプリケーションが処理先を判断できる統一形式を提供します。[NIP-27](/ja/topics/nip-27/)は、読み取り可能なイベントの`content`内で同じURIが何を意味するかを定義します。NIP-21はアプリケーションの境界を越えるためのものであり、NIP-27は署名済みの文章内にプロフィールまたはイベントへの参照を保持するためのものです。どちらもイベントkindを作成したり、リレーメッセージを変更したりするものではありません。[2つの仕様](https://github.com/nostr-protocol/nips/tree/master)が定義するのは、リンクと表示の動作だけです。

### URI ディスパッチと NIP-19 のセマンティクス

[NIP-21 の文法](https://github.com/nostr-protocol/nips/blob/master/21.md)は、`nostr:` の後に NIP-19 の bech32 エンティティを1つ続けたものです。`nsec` は秘密鍵をエンコードするため除外されます。オーソリティ、パス、クエリの各コンポーネントは存在しないため、準拠するリンクは `nostr://npub1...` ではなく `nostr:npub1...` です。プラットフォームやクライアントはハンドラーとして登録できますが、仕様では、インストール済みのどのアプリケーションを使用するかは選択せず、ウェブへのフォールバックも定義していません。

プレフィックスは、何をデコードすべきかをクライアントに示します。`npub` は公開鍵を、`note` はイベント ID を格納します。`nprofile` はプロフィールに任意のリレーヒントを追加し、`nevent` はイベント ID にリレー、作者、kind を追加します。`naddr` は、アドレス指定可能なイベントの作者、kind、`d` 識別子を格納し、任意でリレーも含めます。これらの形式では、[NIP-19 の型・長さ・値フィールド](https://github.com/nostr-protocol/nips/blob/master/19.md)を使用します。ヒントは探索範囲を絞り込みますが、リレーがイベントを保有していることも、作者がそれを管理していることも証明しません。取得したすべてのイベントについて、引き続き ID の再計算と署名の検証が必要です。

[NIP-21 仕様](https://github.com/nostr-protocol/nips/blob/master/21.md)に示されているプロフィール形式は次のとおりです。

```
nostr:npub1sn0wdenkukak0d9dfczzeacvhkrgz92ak56egt7vdgzn8pv2wfqqhrjdv9
```

[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md)は HTML ブリッジも定義しています。Nostr イベントを提供するページは、その `naddr` を `<link rel="alternate">` に設定でき、プロフィールは `nprofile` を `<link rel="me">` または `<link rel="author">` に設定できます。

### NIP-27 のレンダリングと任意タグ

[NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md)は、kind `1` のノートや kind `30023` の記事など、人が読めるイベントコンテンツに適用されます。投稿作成画面では `@name` と表示できますが、署名対象の文字列には `nostr:nprofile1...` を含めて公開します。閲覧側は URI を走査し、その NIP-19 エンティティをデコードして対象を取得し、名前、カード、プレビュー、ローカルリンクなどを表示できます。デコードに失敗した場合、URI は通常のテキストとして残ります。生のコンテンツを書き換えてはいけません。変更すると NIP-01 のシリアライズ結果、ID、署名が変わるためです。

コンテンツ内の参照とタグには、互いに関連するものの異なる役割があります。[NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md)では、任意の `p` タグと `e` タグ、および [NIP-18](/ja/topics/nip-18/) の `q` タグについて説明しています。クライアントは、通知やスレッド関係を作成せずに参照を表示できます。引用を探索できるようにするには、URI と `q` タグの両方を記述する必要があります。[Zap Cooking が9月4日に行った実装](https://github.com/zapcooking/frontend/pull/665)では、この区別に従い、URI を保持したままリレーヒントと対応する `p` タグを追加しています。`p` または `q` を追加しても URI が非公開になるわけではなく、NIP-27 に非表示メンションのモードはありません。

以下の [kind `1` イベント](https://njump.me/note1e0my422kylehy2g4ax4d98vsthdvnvy702yq3f6eguedjr0256as200k6a)は `wss://nos.lol` から復元され、NIP-27 の具体的な参照例として掲載する前に検証されています。その `content` には、バージョンに依存しないアドレス指定可能なイベントの `naddr` が含まれています。デコードすると、kind `30402`、作者 `91036d...310a`、ワークブックの `d` 識別子、および `wss://nos.lol/` ヒントが得られます。`q`、`p`、`t`、`zap`、`client` の各タグはアプリケーション側の選択であり、NIP-27 の要件ではありません。

```json
{
  "id": "cbf64aa95627f3722915e9aad29d905ddac9b09e7a8808a7594732d90deaa6bb",
  "pubkey": "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
  "created_at": 1788953511,
  "kind": 1,
  "tags": [
    [
      "p",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/"
    ],
    [
      "t",
      "archetype"
    ],
    [
      "q",
      "30402:91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a:Archetype-Workbook-Companion-Meet-your-King-Warrioir-Magician-Lover-today-oejbwe",
      "wss://nos.lol/"
    ],
    [
      "zap",
      "91036dec18ee563c07edaed5eff4b5d631755c76f006734b3787292a5e3c310a",
      "wss://multiplexer.huszonegy.world/",
      "0.9"
    ],
    [
      "zap",
      "ed1b999da9a434039d22338c276ffd6e338d609b81e6b1c305a120a982df787d",
      "wss://relay.nostr.band/",
      "0.1"
    ],
    [
      "client",
      "Amethyst"
    ]
  ],
  "content": "You can check, read and use this Workbook already! You can also support and get it for few sats and support us in this project.\n\nI hope it'll help you in your Archetype Journey :)\n\n#archetype\n\nnostr:naddr1qpgyzunrdpjhg7tsv5k4wmmjdd3x7mmt94pk7mtsv9hxjmmw94xk2et594uk7atj949kjmn894tkzunjd9hkju3df4skw6trd9skut2vdamx2u3dw3hkgcte94hk26nzwajszrnhwden5te0dehhxtnvdakz7q3qjypkmmqcaetrcpld4m27la946cch2hrk7qr8xjehsu5j5h3uxy9qxpqqqpmvyqnrm7n",
  "sig": "aa9592e7c773271b9e9f980c8a7e17fda2ffd5a4483a1789e5dd4c4a83018ac576c5202b21b33b08770dcabe023f93998a41f1a0be4bf00e36cdde611d07915e"
}
```

### 信頼性、障害時の挙動、クライアント実装

安全なリーダーは、完全な `nostr:` トークンを見つけ、bech32 を検証し、NIP-19 をデコードして、`nsec` を拒否し、未知の TLV 型を無視します。また、不正な形式やサイズ超過のテキストは変更せず、そのまま残します。`npub` と `nprofile` はプロフィールの問い合わせに使用され、`note` と `nevent` は不変イベントを識別します。`naddr` は、kind、作成者、`d` タグに対応する最新の有効なアドレス指定可能イベントを選択します。リレーのヒントは検索範囲を狭めますが、信頼範囲を広げるものではありません。[NIP-01 のイベント規則](https://github.com/nostr-protocol/nips/blob/master/01.md)に従い、クライアントは取得した `nevent` の id を検証し、アドレス指定可能イベントの置換規則を適用する前に、すべての `naddr` 候補の署名を確認します。

インラインプレビューを表示するかどうかはクライアントの選択であり、プライバシーとリソースのコストを伴います。すべての参照を取得すると読者の関心が明らかになり、大量の問い合わせが発生する可能性があります。そのため、クライアントはキャッシュを使用し、参照が表示範囲に入るまで取得を遅らせ、並行処理数に上限を設け、見慣れないメディアについてはクリックを必須にできます。[NIP-27](https://github.com/nostr-protocol/nips/blob/master/27.md)に従い、プレビューは現在の作成者が署名したテキストとは明確に区別されなければなりません。取得に失敗した場合は、未解決のテキストまたは利用できないカードとして明示し、検証済みコンテンツとして暗黙に扱ってはいけません。

信頼性の扱いは識別子の種類によっても変わります。`nevent` は不変のバイト列を指定するため、取得したイベントのシリアライズ済み id が要求された id と異なる場合、クライアントはそのイベントを拒否できます。`naddr` は置換可能な座標を指定するため、クライアントは表示するバージョンを決定する前に、各候補を検証し、アドレス指定可能イベントの規則を適用する必要があります。どちらの場合も、リレーのヒントは最初の問い合わせに役立ちますが、そのリレーや返されたコンテンツを承認するものではありません。[NIP-19 の TLV 定義](https://github.com/nostr-protocol/nips/blob/master/19.md)は、これらの検証を明示的に行うために必要なデータを提供します。

[NIP-21](https://github.com/nostr-protocol/nips/blob/master/21.md)は Nostr の外部から開ける移植可能なリンクを定義し、NIP-27 は同じリンクを署名済みテキスト内で永続的に利用できるようにします。NIP-21 のみを実装したクライアントは、貼り付けられた URI を開けますが、埋め込まれた参照を表示できません。NIP-27 を完全にサポートするには、走査、安全なデコード、取得ポリシー、ローカルでの表示に加え、通知タグと引用タグをどう扱うかについての明示的な選択が必要です。共通の URI により、クライアントに同一の表示方法を強制することなく、これらの層の相互運用性が維持されます。[Damus](https://github.com/damus-io/damus)は、インライン参照を型付きメンションとしてモデル化しています。その[メンション用コード](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/Mentions.swift)は、`npub` と `nprofile` をプロフィール参照に、`note` と `nevent` をイベント参照に、`naddr` をアドレス参照に対応付けます。[NostrLink](https://github.com/damus-io/damus/blob/2ef636aa07f6bd4f24b72fa998b7397dced56d2a/damus/Core/Nostr/NostrLink.swift)は、それらを適切な参照先へ振り分けます。[Primal Android](https://github.com/PrimalHQ/primal-android-app)は、[スキーム付き形式と貼り付けられた形式を解析](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/domain/nostr/src/commonMain/kotlin/net/primal/domain/nostr/utils/NostrUriUtils.kt)し、bech32 を検証してリレーのヒントを抽出したうえで、[参照をノートコンテンツのモデルへ対応付けます](https://github.com/PrimalHQ/primal-android-app/blob/36939db97213e7f8eeefaa4adaf125d839fc662e/app/src/main/kotlin/net/primal/android/notes/feed/model/NoteNostrUriUi.kt)。[Zap Cooking](https://github.com/zapcooking/frontend/pull/665)は、記事、レシピ、エディターのプレビュー、印刷表示で同じ参照を表示します。

---

プロジェクトやニュース項目を共有するには、[Nostr Compass プロジェクト](https://github.com/andotherstuff/nostr-compass)を通じて NIP-17 DM を送信してください。
