---
title: 'Nostr Compass #4'
date: 2026-01-07
publishDate: 2026-01-07
draft: false
type: newsletters
---

Nostr Compassへようこそ。Nostrプロトコルエコシステムの週刊ガイドです。

**今週のハイライト:** Primal Androidが[NIP-46](/ja/topics/nip-46/)リモート署名と[NIP-55](/ja/topics/nip-55/)ローカル署名機能を実装し、他のAndroidアプリ向けの本格的な署名ハブとなりました。[Marmot Protocol](/ja/topics/marmot/)チームは、セキュリティ監査での指摘事項に対応し、[MLS](/ja/topics/mls/)ベースの暗号化メッセージングを強化する18件のPRをマージしました。Citrineがv1.0に到達し、Applesauceはライブラリスイート全体でv5.0をリリースしました。TENEXがNostr上でのAIエージェント監視機能を構築し、Jumbleがスマートリレープーリングを追加しました。NIP-55の仕様修正で`nip44_encrypt`の戻り値フィールドが明確化され、[NIP-50](/ja/topics/nip-50/)のPRでは高度な検索のためのクエリ式拡張が提案されています。今週の詳細解説では、[NIP-04](/ja/topics/nip-04/)と[NIP-44](/ja/topics/nip-44/)について説明します：レガシー暗号化にセキュリティ上の欠陥がある理由と、新しい暗号化方式がそれらをどのように修正するかを解説します。

## ニュース

**Primal Androidが本格的な署名ハブに** - [バージョン2.6.18](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18)で[NIP-46](/ja/topics/nip-46/)リモート署名と[NIP-55](/ja/topics/nip-55/)ローカル署名の両方が追加され、Primalは他のNostrアプリ向けの完全な署名ツールとなりました。NIP-46によるリモート署名では、ユーザーはNostrリレー経由でバンカーサービスに接続でき、秘密鍵をデバイスに保存する必要がなくなります。NIP-55によるローカル署名では、PrimalがAndroidコンテンツプロバイダーとして公開され、AmethystやCitrineなどのアプリが秘密鍵に触れることなく署名をリクエストできます。[後続のいくつかのPR](https://github.com/PrimalHQ/primal-android-app/pull/839)では、NIP-55仕様のhex公開鍵要件との互換性問題が修正され、不正な形式の`nostrconnect://` URIの解析が改善されました。このリリースには、スムーズなスクロールのためのメディアプリキャッシュ、スレッド読み込み時間の改善、アバターのプリキャッシュも含まれています。

**Marmot Protocolがセキュリティ監査後に強化** - [NIP-104](/ja/topics/nip-104/) MLSベースのエンドツーエンド暗号化メッセージングを実装する[Marmot Development Kit](https://github.com/marmot-protocol/mdk) (mdk)が、今週大規模なセキュリティ修正を受けました。18件のマージされたプルリクエストで監査での指摘事項に対応しました：ストレージレベルのBlob置換攻撃を防ぐための[暗号化グループ画像のハッシュ検証](https://github.com/marmot-protocol/mdk/pull/97)、メモリ枯渇を防ぐための[保留中のウェルカムメッセージのページネーション](https://github.com/marmot-protocol/mdk/pull/110)、[エラーメッセージでのMLSグループID漏洩](https://github.com/marmot-protocol/mdk/pull/112)、キーパッケージの[base64エンコーディング強制](https://github.com/marmot-protocol/mdk/pull/98)などです。[Marmot仕様自体も更新](https://github.com/marmot-protocol/marmot/pull/20)され、MIP-04 v2バージョニングとセキュリティ改善が行われました。進行中のPRでは引き続きnonce再利用、シークレットのゼロ化、キャッシュ汚染ベクターに対処しています。

**Nostrabilityがリレーヒントサポートを追跡** - 新しい[リレーヒント互換性トラッカー](https://github.com/nostrability/nostrability/issues/270)が、エコシステム全体でクライアントがリレーヒントをどのように構築・消費するかを文書化しています。このトラッカーによると、ほとんどのクライアントは現在[NIP-10](/ja/topics/nip-10/)と[NIP-19](/ja/topics/nip-19/)に従ってヒントを構築していますが、消費方法は大きく異なります：一部のクライアントは送信イベントにヒントを含めますが、受信ヒントをフェッチに使用しません。6つのクライアントが完全な実装で「Full」ティアのステータスを獲得しました。このトラッカーは、相互運用性をチェックする開発者や、なぜ一部のクライアントが他のクライアントでは見つからないコンテンツを見つけられるのか疑問に思うユーザーにとって有用です。

**Nostria 2.0がクロスプラットフォーム機能を大幅刷新** - [Nostria](https://nostria.app)クライアントは12月30日に[バージョン2.0をリリース](https://njump.me/nevent1qqs9z4l8z82zphszjlmrjkr8whpvupnlaxc7xk5gfg9syzj0thygtzgpz4mhxue69uhhyetvv9ujuerpd46hxtnfduhszxthwden5te0wfjkccte9enrw73wd9hsz9nhwden5te0wfjkccte9ec8y6tdv9kzumn9wsq3gamnwvaz7tmjv4kxz7fwv3sk6atn9e5k7qgkwaehxw309aex2mrp0yhxgctdw4eju6t09uq32amnwvaz7tmwdaejumr0dshsz9mhwden5te0wfjkccte9ec82c30989ksmfnv9kzumn9wshsqgzxsnsv7pfqqd7rw4fvr0jnkpqmwzfqq3znlc4pqunagxrkl84u66y7fq9)し、iOS（TestFlight）、Android（Play Store）、Web、Windows全体で大幅な機能追加を行いました。このリリースでは、プレイリスト作成、トラックアップロード、Zapベースのアーティスト支払い、機能的なイコライザー付きWinAmpスタイルのプレーヤーを含むネイティブ音楽サポートが追加されました。ライブストリーミングでは、ゲームプレイストリーム中にリッチなメタデータを表示するGame API統合が追加されました。新しいサマリー機能は、時間単位、日単位、週単位のアクティビティダイジェストを圧縮されたタイムラインビューとして生成します。Discoverセクションでは、コンテンツやプロフィールを見つけるためのキュレーションリストを提供します。メディア公開は、クロスクライアントでの発見可能性のためのショートフォーム投稿の自動生成により簡素化されました。リモート署名接続は、手動設定なしでQRコードスキャンで動作するようになりました。プロフィール発見は、Nostrでよくある問題に対処します：ユーザーがメタデータを持たずにリレー間を移動した場合、Nostriaはそのプロフィールを見つけて現在のリレーに再公開します。プレミアム会員は、YouTubeチャンネル統合、プライベートメモ、分析ダッシュボード、マージ/復元オプション付きのフォローリスト自動バックアップを利用できます。

## NIPの更新

[NIPsリポジトリ](https://github.com/nostr-protocol/nips)への最近の変更：

**マージ済み:**
- **[NIP-55](/ja/topics/nip-55/)** - `nip44_encrypt`メソッドの戻り値フィールドが修正されました（[#2184](https://github.com/nostr-protocol/nips/pull/2184)）。Android署名者は暗号化されたペイロードを（`nip44_decrypt`と一致する）`signature`フィールドで返す必要があり、別のフィールドではなくなりました。これにより、仕様がAmberとPrimalの既存の実装と整合します。

**オープンPR:**
- **[NIP-50](/ja/topics/nip-50/)** - クエリ式拡張（[#2182](https://github.com/nostr-protocol/nips/pull/2182)）は、構造化されたクエリ式でNIP-50検索を拡張することを提案しています。このPRは`kind:1`、`author:npub1...`などの演算子とブール組み合わせ（`AND`、`OR`、`NOT`）を追加し、単純なテキストマッチングを超えたより正確な検索クエリを可能にします。これにより、クライアントは基本的な検索文字列との後方互換性を維持しながら、高度な検索インターフェースを構築できます。

## NIP詳細解説：NIP-04とNIP-44

今週は、Nostrの暗号化標準について解説します：まだ遭遇するレガシーのNIP-04と、重大なセキュリティ欠陥を修正した最新の代替であるNIP-44です。

### [NIP-04](/ja/topics/nip-04/)：暗号化ダイレクトメッセージ（レガシー）

[NIP-04](https://github.com/nostr-protocol/nips/blob/master/04.md)は、kind 4イベントを使用したNostr初の暗号化メッセージング方式でした。実装は簡単ですが、既知のセキュリティ上の弱点があり、NIP-44への移行が推奨されています。

**仕組み:** NIP-04はECDH（楕円曲線Diffie-Hellman）を使用して送信者と受信者の間で共有秘密を導出し、AES-256-CBCで暗号化します。

```json
{
  "id": "<event-id>",
  "pubkey": "<sender-pubkey>",
  "created_at": 1736200000,
  "kind": 4,
  "tags": [["p", "<recipient-pubkey>"]],
  "content": "base64-ciphertext?iv=base64-iv",
  "sig": "<signature>"
}
```

暗号化フロー：
1. 共有ポイントを計算: `shared = ECDH(sender_privkey, recipient_pubkey)`
2. 鍵を導出: `key = SHA256(shared_x_coordinate)`
3. ランダムな16バイトのIVを生成
4. 暗号化: `ciphertext = AES-256-CBC(key, iv, plaintext)`
5. コンテンツをフォーマット: `base64(ciphertext)?iv=base64(iv)`

**セキュリティ上の問題:**

- **認証なし:** AES-CBCは機密性を提供しますが、完全性は保証しません。リレーを制御する攻撃者は暗号文のビットを改変し、平文に予測可能な変更を引き起こすことができます（ビットフリッピング攻撃）。
- **IVが平文で送信:** 初期化ベクトルは暗号文と一緒に送信され、予測可能なIVを持つCBCモードは選択平文攻撃を可能にします。
- **パディング検証なし:** PKCS#7パディングの処理方法は実装によって異なり、パディングオラクル攻撃を可能にする可能性があります。
- **メタデータの露出:** 送信者の公開鍵、受信者の公開鍵、タイムスタンプはすべてリレーに見えます。
- **鍵の再利用:** 同じ共有秘密が2者間のすべてのメッセージに永久に使用されます。

**なぜまだ存在するのか:** 多くの古いクライアントやリレーはNIP-04のみをサポートしています。レガシーシステムとやり取りする際に遭遇します。AmberやPrimalなどの署名者は、後方互換性のために`nip04_encrypt`/`nip04_decrypt`を実装しています。

### [NIP-44](/ja/topics/nip-44/)：バージョン付き暗号化

[NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md)は、NIP-04のよく知られた欠陥を修正するために設計された最新の暗号化標準です。NIP-44実装のCure53セキュリティ監査では、仕様が確定する前に対処された10件の問題（タイミング攻撃や前方秘匿性の懸念を含む）が特定されました。適切な鍵導出と認証付き暗号化を備えたChaCha20-Poly1305を使用します。

**NIP-04からの主な改善点:**

| 項目         | NIP-04                     | NIP-44                  |
|:-------------|:---------------------------|:------------------------|
| 暗号         | AES-256-CBC                | XChaCha20-Poly1305      |
| 認証         | なし                       | Poly1305 MAC            |
| 鍵導出       | SHA256(shared_x)           | HKDFとソルト            |
| Nonce        | 16バイトIV、再利用パターン | 24バイトランダムnonce   |
| パディング   | PKCS#7（長さが漏洩）       | 2のべき乗にパディング   |
| バージョニング | なし                     | バージョンバイトプレフィックス |

**暗号化フロー:**

1. **会話鍵:** 送信者-受信者ペアごとに安定した鍵を導出：
   ```
   shared_x = ECDH(sender_privkey, recipient_pubkey).x
   conversation_key = HKDF-SHA256(
     ikm = shared_x,
     salt = "nip44-v2",
     info = ""
   )
   ```

2. **メッセージ鍵:** 各メッセージに対してランダムな32バイトのnonceを生成し、暗号化/認証鍵を導出：
   ```
   keys = HKDF-SHA256(
     ikm = conversation_key,
     salt = nonce,
     info = "nip44-v2"
   )
   chacha_key = keys[0:32]
   chacha_nonce = keys[32:44]
   hmac_key = keys[44:76]
   ```

3. **平文をパディング:** メッセージ長を隠すために次の2のべき乗（最小32バイト）にパディング：
   ```
   padded = [length_u16_be] + [plaintext] + [zeros to next power of 2]
   ```

4. **暗号化と認証:**
   ```
   ciphertext = XChaCha20(chacha_key, chacha_nonce, padded)
   mac = HMAC-SHA256(hmac_key, nonce + ciphertext)
   ```

5. **ペイロードのフォーマット:**
   ```
   payload = [version=0x02] + [nonce] + [ciphertext] + [mac]
   content = base64(payload)
   ```

**バージョンバイト:** 最初のバイト（`0x02`）は暗号化バージョンを示します。これにより、既存のメッセージを壊すことなく将来のアップグレードが可能になります。バージョン`0x01`は広く展開されなかった初期のドラフトでした。

**復号:**

1. base64をデコードし、バージョンバイトが`0x02`であることを確認
2. nonce（バイト1-32）、暗号文、MAC（最後の32バイト）を抽出
3. 受信者の秘密鍵と送信者の公開鍵を使用して会話鍵を導出
4. 会話鍵とnonceからメッセージ鍵を導出
5. 復号前にMACを検証（無効な場合は拒否）
6. 暗号文を復号し、長さプレフィックスを抽出し、パディングを除去した平文を返す

**セキュリティ特性:**

- **認証付き暗号化:** Poly1305 MACにより、復号前にあらゆる改ざんが検出されます
- **前方秘匿性（部分的）:** 各メッセージは一意のnonceを使用するため、1つのメッセージが漏洩しても他のメッセージは明らかになりません。ただし、秘密鍵が漏洩した場合は過去のすべてのメッセージが明らかになります（ラチェット機能なし）。
- **長さの隠蔽:** 2のべき乗パディングにより正確なメッセージ長が隠されます
- **タイミング攻撃耐性:** MAC検証の定数時間比較

**実際の使用:** NIP-44は以下の暗号化レイヤーとして使用されます：
- [NIP-17](/ja/topics/nip-17/)プライベートダイレクトメッセージ（ギフトラップ内）
- [NIP-46](/ja/topics/nip-46/)リモート署名者通信
- [NIP-59](/ja/topics/nip-59/)シール暗号化
- [Marmot Protocol](/ja/topics/nip-104/)グループメッセージ。NIP-44はMLSエクスポーターシークレットから導出された鍵を使用してMLS暗号化コンテンツをラップします
- 安全なポイントツーポイント暗号化が必要なあらゆるアプリケーション

**移行ガイダンス:** 新しいアプリケーションはNIP-44のみを使用すべきです。後方互換性のために、NIP-04にフォールバックする前に、連絡先のクライアントがNIP-44をサポートしているかどうかを確認してください（[NIP-89](/ja/topics/nip-89/)アプリメタデータまたはリレーサポート経由）。メッセージを受信する際は、最初にNIP-44復号を試み、レガシーコンテンツにはNIP-04にフォールバックしてください。

## リリース

**Primal Android v2.6.18** - [完全なリリース](https://github.com/PrimalHQ/primal-android-app/releases/tag/2.6.18)では、[NIP-46](/ja/topics/nip-46/)リモート署名と[NIP-55](/ja/topics/nip-55/)ローカル署名が追加され、Primalは他のAndroidアプリ向けの署名ハブとなりました。パフォーマンス改善には、メディアプリキャッシュ、アバタープリキャッシュ、より高速なスレッド読み込みが含まれます。バグ修正では、プロフィールでの自己メンション、メディアギャラリーのクラッシュ、ストリームタイトルのフォールバックに対処しています。iOSでは、PrimalはNIP-46署名リクエストを受信するためにアプリを起動状態に保つためにバックグラウンドオーディオ再生を使用しています。ユーザーは設定でサウンドを変更したり、完全にミュートにしたりできます。

**Mostro v0.15.6** - [NIP-69](/ja/topics/nip-69/) P2P Bitcoin取引ボットの[最新リリース](https://github.com/MostroP2P/mostro/releases/tag/v0.15.6)は、フェーズ4監査イベントで開発基金の実装を完了しました。開発手数料の支払いは、各成功した支払い後に公開されるkind 38383 Nostrイベントを通じて追跡されるようになり、サードパーティの検証と分析が可能になりました。買い手/売り手メッセージの金額計算が修正され、プレミアムロジックがlnp2pbot参照実装と整合しました。

**Aegis v0.3.5** - クロスプラットフォーム署名者は[ダークモードを追加](https://github.com/ZharlieW/Aegis/releases/tag/v0.3.5)し、アプリアイコンの表示を改善し、よりクリーンなUIレイアウトを実現しました。バグ修正では、iOS iCloudプライベートリレーの競合とイベント解析の問題に対処しています。このリリースでは、イベントJSONをRust署名関数に渡す方法も改善されました。

**Citrine v1.0.0** - Androidリレーアプリが[1.0に到達](https://github.com/greenart7c3/Citrine/releases/tag/v1.0.0)しました。Citrineを使用すると、Androidデバイス上で直接パーソナルNostrリレーを実行でき、ローカルキャッシング、バックアップ、またはNIP-55コンパニオンとして役立ちます。このリリースでは、クラッシュレポートハンドラーが追加され、データベースクエリの効率が改善され、Crowdin経由で翻訳が更新されました。

**Applesauce v5.0.0** - hzrd149のTypeScriptライブラリスイートが、正確性とシンプルさに焦点を当てた破壊的変更を含む[メジャーバージョンをリリース](https://github.com/hzrd149/applesauce/releases)しました。coreパッケージは[デフォルトでイベント署名を検証](https://github.com/hzrd149/applesauce/releases/tag/applesauce-core%405.0.0)するようになり、座標メソッドをより明確な「address」用語に名前変更しました（`parseCoordinate` → `parseReplaceableAddress`）。relayパッケージは[デフォルトのリトライ回数を10から3に削減](https://github.com/hzrd149/applesauce/releases/tag/applesauce-relay%405.0.0)し、デフォルトで到達不能なリレーを無視し、より簡単なイベントフェッチのための`createUnifiedEventLoader`を追加しました。walletパッケージは[NIP-87](/ja/topics/nip-87/) [Cashuミント発見](https://github.com/hzrd149/applesauce/releases/tag/applesauce-wallet%405.0.0)を獲得しました。パッケージ全体で直接の`nostr-tools`依存関係が削除され、バンドルサイズとバージョンの競合が減少しました。

## 注目のコードとドキュメントの変更

*これらはオープンなプルリクエストと初期段階の作業です。マージ前にフィードバックを得るのに最適です。何か気になるものがあれば、レビューやコメントを検討してください！*

### Damus (iOS)

一連のPRが長文記事体験を改善しています。[読書UXの改善](https://github.com/damus-io/damus/pull/3496)では、プログレスバー、推定読了時間、セピアモード、調整可能な行間、スクロール中にナビゲーションを非表示にするフォーカスモードが追加されました。[画像の修正](https://github.com/damus-io/damus/pull/3489)により、マークダウンコンテンツ内の画像がスタンドアロン画像をブロックレベル要素として前処理することで適切なアスペクト比で表示されます。[長文プレビューカード](https://github.com/damus-io/damus/pull/3497)は、インラインの`@naddr1...`テキストを記事タイトルとメタデータを表示するリッチプレビューカードに置き換えます。新しい[リレー統合テストスイート](https://github.com/damus-io/damus/pull/3508)は、[NIP-01](/ja/topics/nip-01/)プロトコル検証と劣化したネットワーク条件（3Gシミュレーション）での動作を含む137のネットワーク関連テストを追加します。

### Bitchat (暗号化メッセージング)

iOS Nostr+Cashuメッセンジャーのセキュリティ強化。[NoiseプロトコルDHシークレットのクリア](https://github.com/permissionlesstech/bitchat/pull/928)は、Diffie-Hellman鍵合意後に共有シークレットがゼロ化されていなかった6か所を修正し、前方秘匿性の保証を復元しました。[既読レシートキューのスレッドセーフティ](https://github.com/permissionlesstech/bitchat/pull/929)は、NostrTransportでのレースコンディションを防ぐためにバリア同期を追加しました。[メッセージ重複排除の最適化](https://github.com/permissionlesstech/bitchat/pull/920)は大量のメッセージでのパフォーマンスを改善し、[hex文字列解析の強化](https://github.com/permissionlesstech/bitchat/pull/919)は不正な入力からのクラッシュを防止します。

### Frostr (閾値署名)

[FROST](/ja/topics/frost/)ベースの閾値署名プロトコルは、オンボーディング時と署名者インターフェースで[グループ認証情報とシェア認証情報のQRコード表示を追加](https://github.com/FROSTR-ORG/igloo-desktop/pull/62)しました。これにより、複数のデバイス間でキーシェアを配布する際のセットアップが容易になり、ユーザーは長い文字列を手動でコピーする代わりに認証情報をスキャンできます。

### Marmot mdk (ライブラリ)

上記のセキュリティ修正に加えて、アクティブなPRは残りの監査指摘事項に対処しています：[Secret<T>型によるゼロ化](https://github.com/marmot-protocol/mdk/pull/109)は、ドロップ時に自動的に機密データをゼロ化するラッパー型を導入し、[メッセージクエリのページネーション](https://github.com/marmot-protocol/mdk/pull/111)はチャット履歴を読み込む際のメモリ枯渇を防止し、[暗号化ストレージ](https://github.com/marmot-protocol/mdk/pull/102)はグループ状態とメッセージを保存するSQLiteデータベースに保存時暗号化を追加します。

### Amethyst (Android)

Androidクライアント全体で忙しい安定性修正の週でした。[寛容なJSON解析](https://github.com/vitorpamplona/amethyst/commit/2c42796)は、Kotlin Serializationをより寛容にすることで不正な形式のイベントからのクラッシュを防止します。イベント検証は[kindフィールドサイズをチェック](https://github.com/vitorpamplona/amethyst/commit/40f9622)してから処理し、オーバーサイズの値からの例外を回避します。トラストスコアUIは視覚的な干渉を減らすために小さなアイコンを取得し、[改善されたエラーログ](https://github.com/vitorpamplona/amethyst/commit/69c53ac)はリレー接続の問題の診断に役立ちます。翻訳の更新がCrowdin経由で到着し、いくつかのSonarQube警告に対処しました。

### TENEX (AIエージェント)

Nostrネイティブのエージェントフレームワークは今週、自律機能を構築する81のコミットがありました。新しい[エージェント監視システム](https://github.com/tenex-chat/tenex/pull/48)は、エージェントのアクションを監視し、必要に応じて介入する行動ヒューリスティックを実装しています。[委任の透明性](https://github.com/tenex-chat/tenex/commit/b244c10)は、ユーザーがエージェントが代わりに何を行ったかを監査できるように、委任トランスクリプトにユーザー介入ログを追加します。[LLMプロバイダーレジストリ](https://github.com/tenex-chat/tenex/pull/47)は、異なるAIバックエンドの統合を容易にするためにモジュール化されました。クロスプロジェクト会話サポートにより、エージェントは複数のNostrベースのプロジェクト間でコンテキストを維持できます。

### Jumble (Webクライアント)

リレーフォーカスのWebクライアントは、いくつかのユーザーエクスペリエンスの改善を追加しました。[スマートリレープール](https://github.com/CodyTseng/jumble/commit/695f2fe)は、使用パターンに基づいてインテリジェントに接続を管理します。[ライブフィードトグル](https://github.com/CodyTseng/jumble/commit/917fcd9)では、ユーザーはリアルタイムストリーミングと手動更新を切り替えることができます。[新しいノートの自動表示](https://github.com/CodyTseng/jumble/commit/d1b3a8c)により、ページを再読み込みせずに新鮮なコンテンツがトップに表示されます。フォローフィードと通知の[永続キャッシュ](https://github.com/CodyTseng/jumble/commit/fd9f41c)は、再訪問時の読み込み時間を改善します。ユーザーは設定を通じて[デフォルトリレーを変更](https://github.com/CodyTseng/jumble/commit/53a67d8)できるようになりました。

---

今週は以上です。何かを構築していますか？共有したいニュースがありますか？あなたのプロジェクトを取り上げてほしいですか？<a href="nostr:npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923">NIP-17 DMでお問い合わせ</a>いただくか、Nostrで私たちを見つけてください。
