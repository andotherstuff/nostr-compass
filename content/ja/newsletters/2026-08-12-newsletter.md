---
title: "Nostr Compass #35"
date: 2026-08-12
publishDate: 2026-08-12
translationOf: /en/newsletters/2026-08-12-newsletter.md
translationDate: 2026-08-12
draft: false
type: newsletters
description: "ポスト量子アイデンティティツール、より強固な暗号化メッセージングと署名、ポータブルなコミュニティ設定、NIPとConcordにまたがるプロトコル作業。"
---

[Nostr Compass](https://nostrcompass.org)へようこそ。Nostrのウィークリーガイドです。

**今週:** [nostr-wot-extension](https://github.com/nostr-wot/nostr-wot-extension)は、既存のNostrアイデンティティに加えてポスト量子鍵とオプトインの保護メッセージを追加します。[Divine](https://github.com/divinevideo/divine-mobile)はアカウント分離、プライベートメッセージの検証、公開確認を強化し、[MDK](https://github.com/marmot-protocol/mdk)は暗号化グループの収束とリカバリを強化します。[Amber](https://github.com/greenart7c3/Amber)はグループ化された署名決定を明示的にします。リリースではウォレット接続、暗号化チャット、ソーシャルディスカバリ、デバイス同期、リモート署名が改善され、プロトコル作業はアイデンティティと暗号化コミュニティをカバーします。ディープダイブでは認証済み削除リクエストと分散型通報を解説します。

## トップストーリー

### nostr-wot-extension 0.4.0はNostrアイデンティティにポスト量子鍵を追加

[nostr-wot-extension 0.4.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.4.0)は、Nostrアイデンティティの管理と署名のためのブラウザ拡張です。24語seedから作成されたアカウントは、既存のNostr鍵に加えてML-KEM-1024暗号化鍵とML-DSA-87署名鍵を導出できるようになりました。ワンクリックのフローで、Nostr pubkeyを両方のポスト量子公開鍵に結び付け、ML-DSA所有証明を含むkind `10203`の証明を公開します。12語ニーモニック、生の`nsec`、リモートsigner、読み取り専用鍵からインポートされたアカウントは導出フローを使用できず、拡張機能はアカウントビューでその制限を説明します。

このリリースでは、オプトインのポスト量子ダイレクトメッセージも追加されます。ML-KEM共有秘密を既存の[NIP-44暗号化メッセージ会話鍵](https://github.com/nostr-protocol/nips/blob/master/44.md)とHKDFで組み合わせ、relay配信には通常の[NIP-59](/ja/topics/nip-59/)（gift wrap）メタデータ非表示レイヤーを維持します。受信者がオプトインした後、暗号化は黙ってフォールバックせず、復号は適切なパスを自動的に選択します。これは新しいメッセージパスを、現行のNostr秘密鍵が後から復元される攻撃から保護しますが、secp256k1イベント署名を置き換えるものではありません。リリースは、その大規模な移行をrelayとclientとの将来の調整に委ねることを明示しています。

### Divine Mobile 1.0.19はアカウント、プライベートメッセージ、公開を強化

[Divine Mobile 1.0.19](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.19)は、Nostr経由で動画を公開・取得するモバイルショート動画clientです。アカウントスイッチャーは各サインイン済みアイデンティティをアカウントスコープのコンテナで構成するようになり、公開の修正により動画が誤ったアカウントで送信されるのを防ぎます。relay公開パスは明示的な成功セマンティクス付きの`OK`応答を待つようになり、relay `CLOSED`フレームは保留中のクエリを宙ぶらりにせず、自身のクエリを終了できます。

[プライベートメッセージ処理](https://github.com/divinevideo/divine-mobile/pull/6368)は、未認証のrumorフィールドと未署名sealを拒否し、4つの欠落メッセージケースを復元し、完全にフォローされた参加者からのグループ会話を受信箱にルーティングします。このリリースでは、アドレサブル動画イベントのtagをリスト更新時に保持し、観測された削除リクエストを消費して削除された動画をローカル状態から消します。これらの変更は先週取り上げたrelayごとのクエリタイムアウト作業に続くものですが、焦点を取得の分離からアイデンティティ境界、メッセージ検証、公開確認へ移します。

### MDK 0.9.11はMarmotグループの収束とリカバリを強化

[MDK 0.9.11](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.11)は、Nostr上で運ばれる暗号化グループメッセージングプロトコルMarmot向けのRust開発キットです。このリリースはグループ状態マシンを中心に、より大きな収束・リカバリシステムを構築します。古い収束パスは現在のグループtipで再開し、インバウンドcapability投影は原子的にコミットし、延期メッセージは再起動をまたいで有界な寿命を受け取り、コミットアドレス指定チェックポイントはアイデンティティ自身のコミットフォークのリカバリに役立ちます。非安定送信はキューに入れてリカバリでき、epoch-stallパスはバックフィルへエスカレートし、送信済みメッセージは収束作業を生き延びます。

[ストレージとホスト統合](https://github.com/marmot-protocol/mdk/pull/1201)も並行して強化されます。MDKは剪定されたSQLite投影を安全に削除し、インポートされた秘密鍵、[NIP-49](/ja/topics/nip-49/)（暗号化秘密鍵）エクスポート中間体、OpenMLSシリアライゼーションバッファをゼロ化し、デバッグ出力からグループ画像鍵を編集します。アカウントインポートは中断後に再開でき、iOSとAndroidのプライベートストレージパスが修復され、ホストはサスペンド前にストレージを明示的に閉じられます。新しい軽量rosterとローカルメンバーシップ投影はアプリケーションが読み取る量を減らし、Hermesコネクタは複数のエージェント生成画像を1つのMarmotアルバムとして配信できます。

### Nostria 4.1.67は暗号化コミュニティ管理を拡張

[Nostria 4.1.67](https://github.com/nostria-app/nostria/releases/tag/v4.1.67)は、Nostr向けのウェブおよびデスクトップソーシャルclientです。4.1.53で導入された実験的な[NIP-29](/ja/topics/nip-29/)（relay管理グループ）とConcord暗号化コミュニティを基盤に、コミュニティ解散、アイコンとバナー管理、圧縮プレビュー付き暗号化写真アップロード、フルリアクションピッカー、ユーザーがノートや記事を読みながらコミュニティを開いたままにするデュアルペインレイアウトを追加します。このリリースでは、スレッドメッセージングと公開・グループ・プライベートチャットを統合したハブも追加されます。

### Amber 6.4.0はグループ化された署名決定をすべて明示的にする

[Amber 6.4.0](https://github.com/greenart7c3/Amber/releases/tag/v6.4.0)は、Nostr秘密鍵を署名を要求するアプリケーションから分離して保持するAndroid signerです。再設計されたマルチリクエスト画面は、各リクエストと各グループにApproveとDenyコントロールを提供し、以前の選択・確認フローを置き換えます。Amberのrelay仲介bunkerインターフェース経由で拒否されたリクエストは、適切なエラー応答を受け取るようになり、要求側clientは拒否と停滞したsignerを区別できます。

[Amberのタグ付きソース](https://github.com/greenart7c3/Amber/tree/v6.4.0)は、出荷済みすべてのロケールで113種類のイベントkindに対するローカライズされた人間可読ラベルも追加します。追加にはConcordグループイベント、[NIP-51](/ja/topics/nip-51/)（リスト）Gitリポジトリブックマーク、[NIP-53](/ja/topics/nip-53/)（ライブアクティビティ）ルームプレゼンスイベントが含まれ、ユーザーは署名を承認する前に馴染みのないデータについてより多くの文脈を得られます。concurrent-mapガードは、`NegativeArraySizeException`を引き起こしうるrelayサブスクリプションクラッシュも修正します。

### Safebox Acornはポータブルなリカバリコンポーネントをウェブアプリから分離

[Safebox Acorn](https://github.com/trbouma/safebox-acorn)は、Nostrバックエンド状態でユーザー管理鍵、資金、レコードを保護するためのスタンドアロンPythonコンポーネントおよびコマンドラインインターフェースです。Acornをより広いSafeboxウェブアプリケーションから抽出することで、別のPythonプロジェクトがランタイムをインストールし、ウェブインターフェースを引き受けずに鍵、Nostrプロフィール、relay、レコード、Cashu、Lightning、暗号ヘルパーを使用できます。現在のレコード保護プリミティブは、新鮮な256ビット鍵を生成し、別途供給されたエントロピーから1つを導出し、正確な鍵をチェックサム付き24語リカバリフレーズとしてエンコードできます。

プロジェクトの[リカバリと継続性ガイド](https://trbouma.github.io/safebox-acorn/recovery-and-continuity/)は、Acornを家庭またはコミュニティSafebox内の交換可能なプロトコルコンポーネントとして位置づけます。設計は暗号化状態をローカルrelayと独立レプリカ経由で利用可能に保ち、リカバリが1台の機器、アプリケーション、relay、mint、サービスプロバイダーに依存しないようにします。ドキュメントは現在の境界について慎重です。保護レコードの暗号化は設計中のままであり、そのプロファイルが実装・レビューされるまで、アプリケーションは新しいレコード保護鍵にレコードを依存させるべきではありません。


## タグ付きリリース

### Mostro Core 0.14.2は暗号化チャットエンベロープを変更

[Mostro Core](https://github.com/MostroP2P/mostro-core)は、Mostro取引デーモンとそのclientが使用する共有型およびピアツーピア関数のRustライブラリです。[バージョン0.14.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.2)は、gift wrapされたチャットメッセージを、ピアの共有秘密から導出した別々の会話暗号化鍵と署名鍵を使用するkind 14エンベロープに置き換えます。新しいリーダーは著者、署名、受信者、タイムスタンプ、コンテンツサイズを検証し、レガシーgift wrapヘルパーは移行中に両形式を読めるよう残ります。

### Mostro 0.18.1はCashu escrowパスを開始しデーモンを強化

[Mostro](https://github.com/MostroP2P/mostro)は、Nostr経由で注文を調整するピアツーピアLightning取引デーモンです。[バージョン0.18.1](https://github.com/MostroP2P/mostro/releases/tag/v0.18.1)は、Cashu escrowバックエンドの基盤を築き、設定、データベースヘルパー、mint統合、起動配線、最初のロックアクションを含みます。信頼できるノードがNostr経由で発表する価格も使用でき、置換可能infoイベントで初回接触のproof-of-work要件を告知します。このリリースは[NIP-44](/ja/topics/nip-44/)（暗号化メッセージ）DoS修正のためNostr依存を更新し、リストアセッションログから秘密鍵を削除し、未承認の協調キャンセルメッセージを拒否し、LNURL取得をSSRFとハングから保護し、支払いinvoiceを検証し、再起動後にhold invoiceサブスクリプションを復元します。

### LaWallet NWC 2.3.0はNostr通知とzapレシートを追加

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc)は、[Nostr Wallet Connect](/ja/topics/nip-47/)（NWC）経由でウォレットを接続するオープンソースLightning Addressプラットフォームです。[バージョン2.3.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.3.0)は、各ウォレットが受信・転送通知を設定可能なNostrイベントとして送信できるようにし、受信者`p` tag、選択relay、テンプレート化コンテンツ、オプションの[NIP-44](/ja/topics/nip-44/)（暗号化メッセージ）暗号化を含みます。再試行は同じ署名済みイベントIDを再利用します。またzapリクエストを受け入れ、決済後に署名済み[NIP-57](/ja/topics/nip-57/)（zap）kind 9735レシートを公開し、新しいアドレスcapabilityビューは解決されたアドレスが[NIP-05](/ja/topics/nip-05/)（検証可能アイデンティティ）、NIP-57、関連Lightning Addressプロトコルをサポートするかを表示します。

### nostr-double-ratchet TypeScript 0.0.166は公開inviteをセッション鍵に結び付ける

[nostr-double-ratchet](https://github.com/irislib/nostr-double-ratchet)は、Nostr relay上のエンドツーエンド暗号化ダイレクトおよびグループメッセージングのTypeScriptおよびRustプリミティブを提供します。[TypeScript 0.0.166](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.166)は、invite応答がセッション鍵の所有を証明することを要求し、再利用可能な公開inviteが1つのNostrアイデンティティを別当事者のセッションに結び付けるのを防ぎます。このリリースは不正なrumorフィールドも拒否し、ペイロード検証を強化します。既存セッションは引き続き動作しますが、更新されたinviterは古いinviteeからの証明なし応答を拒否します。

### cln-nip47 0.2.0はNWCリクエストを拡張・分離

[cln-nip47](https://github.com/daywalker90/cln-nip47)は、[Nostr Wallet Connect](/ja/topics/nip-47/)（NWC）経由でノードをウォレットに公開するCore Lightningプラグインです。[バージョン0.2.0](https://github.com/daywalker90/cln-nip47/releases/tag/v0.2.0)は、hold invoiceの作成・キャンセル・決済用NWCメソッドと`hold_invoice_accepted`通知を追加し、接続ノードが実際にサポートするメソッドセットを告知します。トランザクションリスト応答は500エントリと約128 kBで停止し、リクエストイベントはイベントIDで重複排除され、1 clientの失敗通知が他clientへの配信を妨げなくなります。このリリースは、NWC仕様の一部ではなくなった2つのマルチペイメントメソッドも削除します。

### ClipRelay 0.1.3はアイドル期間後にrelayとsigner接続を復元

[ClipRelay](https://github.com/tajava2006/cliprelay)は、Nostr relay経由でユーザーのクリップボードをデバイス間で同期し、[NIP-44](/ja/topics/nip-44/)（暗号化メッセージ）で同一アイデンティティ向けにコンテンツを暗号化します。対応する[デスクトップ](https://github.com/tajava2006/cliprelay/releases/tag/desktop/v0.1.3)および[Android](https://github.com/tajava2006/cliprelay/releases/tag/android/v0.1.3) 0.1.3リリースは、入力テキストを別デバイスのクリップボードへ直接送るテキストボックスを追加します。アイドル期間後は実relay往復で生存性をテストし、再サブスクリプションからソケット交換、再構築された接続プールへエスカレートし、停滞した[NIP-46](/ja/topics/nip-46/)（リモート署名）signer呼び出しはタイムアウトして自動再構築します。

### NoorNote 1.3.2は記事ディスカバリをソーシャルグラフへ移す

[NoorNote](https://github.com/77elements/noornote)は、ウェブ、デスクトップ、Android向けのソーシャル投稿、暗号化メッセージ、長文記事、その他イベントkindに対応するNostr clientです。[バージョン1.3.2](https://github.com/77elements/noornote/releases/tag/v1.3.2)は、平坦なグローバル記事フィードを1次・2次・3次接触からのディスカバリに置き換え、読者にフォローグラフに根ざした記事タイムラインを提供します。また、未知の送信者からの再生ダイレクトメッセージのバーストを、relay履歴到着時にtoastの山ではなく1つのローリング通知にまとめます。

### Bray 2.4.0はコンパクトなリモート署名ダイアレクトを追加

[Bray](https://github.com/forgesworn/bray)は、ソフトウェアエージェントと人間にrelayアクセス、アイデンティティ、公開、リモート署名のツールを提供するNostr MCPサーバーです。[バージョン2.4.0](https://github.com/forgesworn/bray/releases/tag/v2.4.0)は、[NIP-46](/ja/topics/nip-46/)（リモート署名）が使用する文字列化形式に加え、イベントがオブジェクトである署名リクエストも受け入れ、`sign_event_compact`を追加してイベントID、署名、pubkey、タイムスタンプのみを返します。その小さなリクエスト・応答形式は制約のあるハードウェアsignerのメモリ使用量を削減し、標準の`sign_event`フローは変更されず、両ダイアレクトは受信イベントのID上に署名を生成します。


## 新たに発見

### Pactは相互同意のエージェントbondをNostrにもたらす

[Pact](https://github.com/bobodread876/pact)は今週新たに発見され、MATE.mdとドラフトNIP-BDトランスポート上に構築されたソフトウェアエージェント向けの初期段階の関係レイヤーです。署名済みで相互同意のbondはエージェント自身の鍵が保持し、Nostr経由で公開でき、プライベートbondは[NIP-59](/ja/topics/nip-59/)（gift wrap）を使用します。モノレポにはMCPサーバー、TypeScript SDK、コマンドラインclient、自己ホスト可能デーモン、ウェブインターフェースが含まれます。最新のリポジトリアクティビティは今号の週次ウィンドウより前のものであるため、これは新リリースの主張ではなく発見メモです。


## 開発中

### nostrordはグループミュートをデバイス間で同期

[nostrord](https://github.com/nostrord/nostrord)は、relay管理コミュニティ向けのクロスプラットフォームclientです。[PR #250](https://github.com/nostrord/nostrord/pull/250)は、各アカウントのグループごとのミュート選択を自己暗号化[NIP-78](/ja/topics/nip-78/)（アプリ固有データ）kind `30078`イベントに保存し、1台のデバイスで行った設定がrelayにグループリストを明かさずに別デバイスへ追随できるようにします。置換可能レコードは最新イベント順序を使用し、ライブ変更をリッスンし、署名または公開失敗時にインターフェースをロールバックしてローカル状態の不整合を残しません。ミュートされたグループは可視未読合計への寄与を止めつつ、次回訪問のための未読位置は保持します。

### AmethystはConcordのinviteライフサイクルを完成

[Amethyst](https://github.com/vitorpamplona/amethyst)は、Concordプロトコルを実装する暗号化コミュニティサポートを備えたAndroid Nostr clientです。[PR #3888](https://github.com/vitorpamplona/amethyst/pull/3888)は、inviteリンクがコミュニティrefoundingを生き延び、同じアドレサブル座標でbundleを再発行できるようにし、banチェックは削除されたメンバーがそのリカバリパスを使用するのを防ぎます。また暗号化CORD-05 inviteリストをアプリと`amy`コマンドラインclientの両方で実装し、リンクごとの失効tombstoneを追加し、リンクを退役できる唯一の保存署名鍵を削除する前にrelay確認を要求します。同じ作業で`amy`に、後続コミュニティepochを追従するために必要なcontrol鍵配信、refounding、rekeying、孤立メンバーリカバリパスを与えます。

### Buzzは各コミュニティの外観をデスクトップとモバイル間で運ぶ

[Buzz](https://github.com/block/buzz)は、デスクトップとモバイルclientを備えたNostrベースのコミュニティワークスペースです。マージ済みデスクトップ[PR #3653](https://github.com/block/buzz/pull/3653)とモバイル[PR #3767](https://github.com/block/buzz/pull/3767)は、各コミュニティのテーマ、アクセント、システムモード選択を、そのコミュニティrelay上の暗号化NIP-78レコードとして保存します。両clientは同じバージョン付きペイロードを共有し、アイデンティティスコープのローカルキャッシュを保持するため、コミュニティやアカウントを切り替えてもrelayが利用不能な間に誤った外観が適用されません。置換順序、ガード付き書き込み、closed接続後の再サブスクリプションにより、再接続後に2 clientが再収束します。

[Buzz Desktop 0.5.10](https://github.com/block/buzz/releases/tag/desktop-v0.5.10)は号の締切前に、パフォーマンスと信頼性のパスが続きました。0.5.9以降に導入された退行を除去し、チャンネル読み込みを加速し、初期タイムライン保持を有界化し、既読状態の永続化を統合し、新鮮なチャンネルタイムラインを保持し、プロジェクトイベントへのリアクションでrelay取り込みワーカーがクラッシュするのを止めます。また、スレッドメッセージをチャンネルへ送信する機能を追加し、デスクトップ検索を意図したスコープに絞ります。


## プロトコルと仕様作業

### NIPs

[NIPs PR #2435](https://github.com/nostr-protocol/nips/pull/2435)は、[NIP-34](/ja/topics/nip-34/)（git-over-Nostr）をNostrイベント経由のgitリポジトリ協業を標準化するオープン修正案です。pull-requestイベントにオプションの`b` tagを追加し、著者がリポジトリのデフォルト以外のターゲットブランチを指定できるようにします。この提案はngitとGitWorkshopですでに実装されているサポートに一致しますが、仕様にはまだ入っていません。

[NIPs PR #2434](https://github.com/nostr-protocol/nips/pull/2434)は、ポスト量子アイデンティティ鍵のオープン提案です。[NIP-06](/ja/topics/nip-06/)（鍵導出）ニーモニック鍵導出seedから既存secp256k1鍵に加えてポスト量子暗号化・署名鍵を導出し、公開鍵をkind `10203`証明でNostrアイデンティティに結び付けます。ドラフトは、secp256k1が後から破られた場合に以前のメッセージの機密性を保護するという主張に限定し、今日のイベント署名を置き換えません。

[NIPs PR #2431](https://github.com/nostr-protocol/nips/pull/2431)は、ブラウザsigner向け[NIP-07](/ja/topics/nip-07/)（ブラウザ署名）のオープン修正案です。clientは署名または暗号化リクエストに期待するpubkeyを添付でき、signerはそのアカウントを使用するか呼び出しを拒否する必要があります。これにより、ユーザーがsignerでアカウントを切り替えた後、ページが黙って別アイデンティティのまま続くのを防げます。

[NIPs PR #1813](https://github.com/nostr-protocol/nips/pull/1813)は、ウィンドウ中の実質的作業後もオープンのdouble-ratchet提案のままです。メッセージとともに鍵が進む前方秘匿暗号化会話を指定し、nostr-double-ratchetライブラリとIrisに実装が既にあります。まだドラフトであり、マージされたNIPではありません。

[NIPs PR #2433](https://github.com/nostr-protocol/nips/pull/2433)はウィンドウ中にオープンしてマージなしでクローズしました。[NIP-42](/ja/topics/nip-42/)（relay認証）relayエラーを明確化する提案で、`auth-required`は別の認証が結果を変えうることを意味し、`restricted`は変えられないことを意味します。この区別は1つの鍵では認証済みだが別の鍵の認可が欠けている接続に対処します。クローズ状態は文言が仕様に入らなかったことを意味します。

[NIPs PR #2378](https://github.com/nostr-protocol/nips/pull/2378)は、まだ提案中に以前取り上げられましたが、マージなしでクローズしました。提案されていたエージェントpassport、ディスカバリ、タスク、マーケットプレイス、invoice、接続イベントはNIP集合の外に残ります。

[NIPs commit 656cecc](https://github.com/nostr-protocol/nips/commit/656cecc7c0a815b6a2b218d3b5d6f078b3f4dbab)は[NIP-29](/ja/topics/nip-29/)（relay管理グループ）へのドキュメントのみの修正をマージしました。グループメタデータ例に`previous` tagを追加し、置換イベントが置き換えるイベントを特定する方法を示します。これは例を明確化するものであり、新しいプロトコル機能は導入しません。

### Concord and CORDs

[CORD PR #18](https://github.com/concord-protocol/concord/pull/18)は、暗号化Community Listをkind `33302`イベントにシャードし、50メンバーシップ上限を撤廃し、退役エントリを剪定してrelay制限内に収めます。他2つのオープン提案は[プライベートメンションlocator](https://github.com/concord-protocol/concord/pull/16)と、メッセージを破棄せずにチャットを一時停止する[一時停止シグナル](https://github.com/concord-protocol/concord/pull/17)を追加します。

[CORD-02 PR #15](https://github.com/concord-protocol/concord/pull/15)は8月6日にマージされ、コミュニティcontrol planeへの書き込みを制限します。オーナーとスタッフは新しい`control_root`署名秘密を保持し、全メンバーはモデレーション状態を検証・復号するために必要な導出pubkeyとread鍵を保持します。write鍵はスパム障壁であり、権限を確立する内部actor署名とrosterチェックの代替ではありません。

[CORD PR #12](https://github.com/concord-protocol/concord/pull/12)は、オープンドラフトとして以前取り上げられましたが、マージなしでクローズしました。control plane部分は上記の狭いマージ済みCORD-02修正に置き換えられ、制限付きwriteチャンネルとその他のドラフト資料は仕様に入りませんでした。

## NIPディープダイブ

### イベント削除リクエスト（NIP-09）

[NIP-09](/ja/topics/nip-09/)（イベント削除）は、[一次仕様](https://github.com/nostr-protocol/nips/blob/master/09.md)で定義され、イベント著者にrelayとclientへその著者の1つ以上のイベントの配信停止を求める署名付き方法を与えます。すべてのコピーを消去するものではありません。元イベントを配布したのと同じrelayネットワークを通じて著者の意図を運びます。

リクエストは通常の署名済みkind `5`イベントです。tagには特定イベントIDへの1つ以上の`e`参照、またはアドレサブルイベント座標への`a`参照が含まれ、[NIP-09 tagルール](https://github.com/nostr-protocol/nips/blob/master/09.md#event-deletion-request)は参照イベントkindごとに`k` tagを含めるべきと述べます。オプションの`content`で理由を説明できます。`a`参照では、relayはその座標のうちタイムスタンプがリクエストの`created_at`以下のすべてのバージョンを削除すべきであり、古い削除リクエストが後の置換を抑制するのを防ぎます。

[著者性がセキュリティ境界](https://github.com/nostr-protocol/nips/blob/master/09.md#relay-behavior)です。relayは参照イベントの`pubkey`が削除リクエストの`pubkey`と一致するときのみ、その配信を止めるべきであり、clientはイベントを隠す前にそのチェックを行う必要があります。relayは参照イベントを保持していない場合があり、リクエスト受け入れ時に関係を検証できないことがあるため、clientはrelay受け入れを削除が承認された証明と見なせません。仕様はまた、別clientが元イベントを既に保持し後からリクエストに遭遇する可能性があるため、relayにkind `5`リクエストを保持するよう求めます。

以下は[署名済みkind `5`イベント](https://primal.net/e/6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943)です。

```json
{
  "id": "6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943",
  "pubkey": "5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743",
  "created_at": 1786465675,
  "kind": 5,
  "tags": [
    ["e", "f3d47f8b813928c5baf7ac993846be0220dc37a2e7c7b128fb49a4b92711f131"],
    ["k", "30091"],
    ["a", "30091:5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743:survey:0ad5cebc-608b-47d7-97fd-9e6c47787199"],
    ["t", "nostr-survey"]
  ],
  "content": "Public survey summary deleted during privacy refresh",
  "sig": "846be83b038dc5f91af0c9d03a4ac81aff9bc4cfde7d85c849fa2fdae890f75cc444a4072f45aa18883b0b3871e15381b220182d6e366892f0c9c6f9c0557244"
}
```

削除は署名済みオブジェクトの失効ではなく、協調的ポリシーです。relay、キャッシュ、スクリーンショット、オフラインclientは元のバイト列を保持でき、kind `5`リクエスト自体を削除してもそれを取り消しません。clientは対象を隠したり、放棄済みとしてマークしたり、リクエスト理由を表示したりできますが、普遍的削除は保証できないことをユーザーに伝えるべきです。これは、イベント公開時に選択した時刻以降relayにイベント保存を止めるよう求める`expiration` tagを持つ[NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md)（期限付きイベント）とは異なります。NIP-09は後の著者決定を扱い、既に配布されたイベントを指せます。

現在の実装はそのポリシーを異なるレイヤーで適用します。[Divine PR #6623](https://github.com/divinevideo/divine-mobile/pull/6623)は削除された動画をclientのイベントストアから除去し、[strfry PR #251](https://github.com/hoytech/strfry/pull/251)は有効な削除リクエストをgift wrap受信者へ拡張し、[Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md)はclientでNIP-09サポートを宣言します。[nostrordのグループclient](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/network/NostrGroupClient.kt)は別の現在の実装パスを提供します。

### 通報（NIP-56）

[NIP-56](/ja/topics/nip-56/)（通報イベント）は、[一次仕様](https://github.com/nostr-protocol/nips/blob/master/56.md)で定義され、アカウント、イベント、または参照blobについての署名済み通報を標準化します。通報シグナルをモデレーション決定から分離し、各clientまたはrelayが信頼する通報者と方針に合う対応を選べます。

通報はkind `1984`を使用し、通報対象アカウントを`p` tagで特定する必要があります。ノートの通報にはイベントIDの`e` tagも必要です。tagの3番目の値は、指定カテゴリの1つを担います: `nudity`、`malware`、`profanity`、`illegal`、`spam`、`impersonation`、`other`。blobについての通報は、hashを`x` tagに、blobを参照したイベントを`e` tagに、場所をオプションの`server` tagに使えます。[NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md)（ラベリング）のオプション`L`および`l` tagは、固定カテゴリリストが十分に精密でないときに名前空間付きラベルを追加できます。

[イベントが証明するのは1つの鍵が申し立てを行ったことのみ](https://github.com/nostr-protocol/nips/blob/master/56.md#reporting)です。通報されたコンテンツは、有効なkind `1984`が存在したからといって虚偽、違法、削除可能になるわけではなく、オープンrelayは匿名通報を票として安全に数えられません。仕様は通報のゲーム化が容易なため自動relayモデレーションに反対しつつ、relay管理者が既に信頼するモデレーターの通報に基づいて行動することを許容します。clientは代わりに、例えば信頼する連絡先が同じアカウントを複数フラグした後にコンテンツをぼかすなど、ユーザーのソーシャルグラフを通じて通報に重みを付けられます。

以下は[署名済みkind `1984`イベント](https://primal.net/e/17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2)です。

```json
{
  "id": "17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2",
  "pubkey": "1ff02fb5cdc633c1be55368ab655490ec25d2f5dc2e364d4703bc3196d99eab1",
  "created_at": 1786465319,
  "kind": 1984,
  "tags": [
    ["p", "3a72b02cc05ee07310dc580874b6a9ca8271c6518b90655bd2e98003c9601e68", "impersonation"]
  ],
  "content": "",
  "sig": "6362e415410feb19e0505654a4660e8456b6b2aec5ae39173a0429a6a8e5fa1381c9488198ca2982db43ee8198af056f2a25537705c763784062056d0ab2eb1a"
}
```

[NIP-56とNIP-09は異なる問題を解く](https://github.com/nostr-protocol/nips/tree/master)ものです。kind `1984`通報は他人のアカウントやイベントを対象にできますが、削除権限を与えません。kind `5`リクエストは元著者の意図を表し、その著者自身のイベントに対してのみ有効です。どちらも削除を保証しません。NIP-56は意図的にローカルモデレーションポリシーへ委譲し、NIP-09はrelayとclientが認証済みリクエストを尊重することに依存します。

実装はそれらの選択を異なる製品で露出します。[Divine PR #6591](https://github.com/divinevideo/divine-mobile/pull/6591)はショート動画clientの通報配信を修正し、[Conduit PR #250](https://github.com/Conduit-BTC/conduit-mono/pull/250)はマーケットプレイス参加者向けの有界コンテキストとして通報を読み、[nostrordのNIP-56モジュール](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/nostr/Nip56.kt)は通報イベントを公開・処理します。[Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md#nip-support)も現在のNIP-56サポートを列挙します。


---

[NIP-17](/ja/topics/nip-17/)（gift-wrappedプライベートDM）でプロジェクトやニュース項目を共有し、[Nostr Compassプロジェクト](https://github.com/andotherstuff/nostr-compass)へ送ってください。
