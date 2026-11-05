---
title: "NIP-73: 外部コンテンツID"
date: 2026-02-04
draft: false
categories:
  - Protocol
  - Discovery
  - Metadata
translationOf: /en/topics/nip-73.md
translationDate: 2026-11-05
---

NIP-73は、Nostrイベントの中で外部コンテンツを参照するための標準的な方法を定義しています。識別子そのものには`i`タグを、識別子の種類には`k`タグを使います。これによりクライアントは、同じ書籍、ウェブサイト、ポッドキャストのエピソード、場所、ハッシュタグ、ブロックチェーン上のオブジェクトをめぐる議論をまとめることができます。[現行の仕様](https://github.com/nostr-protocol/nips/blob/master/73.md)は、ドラフトかつオプションと位置づけられています。

## 仕組み {#how-it-works}

NIP-73を使うイベントには、正規化された外部識別子を入れた`i`タグと、識別子のファミリーを示す`k`タグが含まれます。クライアントは、`i`で特定の1つの対象を、`k`でファミリー全体を、それぞれリレーに問い合わせることができます。NIP-73は独自のイベントkindを追加しません。これらのタグは、コメント、レビュー、その他のイベントに付けられます。

タグの断片であり、完全なイベントではありません:

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

ウェブページの場合は、正規化したURLを`i`に入れ、`k`を`web`に設定します。仕様は複数の識別子ファミリーを扱っており、次のものが含まれます:

- フラグメントを含まない正規化済みのウェブURL
- 書籍のISBN
- 映画のISAN
- DOI
- ジオハッシュ、およびISO 3166の国コードまたは地域区分コード
- ポッドキャストのフィード、エピソード、パブリッシャーのGUID
- ハッシュタグ
- ブロックチェーンのトランザクションおよびアドレスの識別子

## 正規化ルール {#normalization-rules}

照合は文字列の完全一致に依存するため、仕様はファミリーごとに1つの表記形式を定めています。仕様に挙げられている例:

- ジオハッシュは`geo:<value>`の形式を使い、小文字でなければならない
- 国コードと地域区分コードは`iso3166:<code>`の形式を使い、大文字でなければならない
- ISBNはハイフンを省く
- DOIは小文字にする
- ウェブURLはフラグメントを取り除く
- ブロックチェーンのトランザクションハッシュは小文字の16進数を使う

正規化で決まるのは、1つの識別子の書き方です。別名をまとめるものではありません。版ごとに異なるISBNや、正規化後も異なる文字列になるURLは、別々の識別子のままです。そのため、1冊の書籍や1本の記事についての議論が、複数の`i`値に分散することは依然としてあり得ます。

## URLヒント {#url-hints}

`i`タグには、配列の3番目の要素として任意のURLヒントを含めることができます。これはタグ名の後に続く2番目の値にあたります。その識別子の種類に対応する独自のレンダラーを持たないクライアントは、このヒントをフォールバック用のリンクとして使えます。

タグの断片: `["i", "isbn:9780765382030", "<url-hint>"]`

ヒントを選ぶのは作成者です。ヒントは識別子の一部ではありません。所有権を証明するものでも、正規のサイトを示すものでもありません。

## 信頼とコンテキスト {#trust-and-context}

同じ識別子を持つ2つのイベントは同じ会話にまとめられますが、識別子が共通であることから言えるのはそこまでです。署名済みイベントは、その作成者を特定します。参照先の書籍、サイト、ポッドキャストのパブリッシャーを認証するものではありません。それらを誰が管理しているかを示すものでもありません。

`i`タグが何を意味するかは、イベントによって異なります。[NIP-22](https://github.com/nostr-protocol/nips/blob/master/22.md)のコメントでは、大文字の`I`/`K`がルートのスコープを、小文字の`i`/`k`が親を示します。このスレッド構造はNIP-22によるもので、NIP-73はコメントのkindを定義していません。[NIP-39](https://github.com/nostr-protocol/nips/blob/master/39.md)はプロフィール内の外部アイデンティティに`i`を使うため、すべての`i`タグがNIP-73の対象を表すわけではありません。

[NIP-85](/ja/topics/nip-85/)のTrusted Assertionsも、書籍、ウェブサイト、ハッシュタグ、場所といったNIP-73の識別子を対象にできます。

## 実装 {#implementations}

rust-nostrの[コミット4c8099a時点のnip73.rs](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs)は、既知のプレフィックスを解析して型付きの`ExternalContentId`にし、任意のヒントを型付きのURLに変換します。タグの3番目の要素を書き込むのは、ヒントがある場合だけです。テストでは、ハイフン付きのISBNがそのまま残っています。パーサーはプレフィックスを取り除いた残りを、仕様の正規化を適用せずに保存します。そのため、型付きで解析できても、正規の文字列になるとは限りません。チェーンIDはファミリーに含めず、`ethereum:100:tx:<hash>`を`ethereum:tx`に対応付けます。このリビジョンには、`iso3166`の国を表すバリアントがありません。

Amethystの[コミット553f761時点のDisplayExternalId.kt](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt)は、ジオハッシュ、ハッシュタグ、URLの識別子をそれぞれ専用の表示に回し、サポート対象のその他の種類は汎用のスコープチップとして表示します。URLを選ぶと、そのページに対応するアプリ独自のスレッドルートが開きます。プレビューが無効の場合、通常の表示ではプレーンなリンクチップだけが表示され、プレビューは要求されません。プレビューが有効の場合、まだないプレビューを取得する際に、対象サイトへ接続することがあります。どちらのファイルからも、リリース済みバージョンでの動作はわかりません。

---

**一次情報源:**
- [NIP-73仕様](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - ISO 3166の国コードと地域区分コードを追加
- [rust-nostr コミット4c8099a時点のnip73.rs](https://github.com/rust-nostr/nostr/blob/4c8099aef646dca13a5c402f4d0d77cd792a8390/nostr/src/nips/nip73.rs)
- [Amethyst コミット553f761時点のDisplayExternalId.kt](https://github.com/vitorpamplona/amethyst/blob/553f761f22c15e946730d3e76be9487519ebab64/commonsUI/src/commonMain/kotlin/com/vitorpamplona/amethyst/commons/ui/note/nip22Comments/DisplayExternalId.kt)

**言及された号:**
- [ニュースレター #47: NIPディープダイブ](/ja/newsletters/2026-11-04-newsletter/#nip-deep-dive-nip-31-and-nip-73)
- [ニュースレター #45](/en/newsletters/2026-10-21-newsletter/#feather)
- [ニュースレター #43](/en/newsletters/2026-10-07-newsletter/#protocol-and-spec-work)
- [ニュースレター #37: 2025年8月](/en/newsletters/2026-08-26-newsletter/#august-2025)
- [ニュースレター #8: NIPアップデート](/en/newsletters/2026-02-04-newsletter/#nip-updates)
- [ニュースレター #10: NIP-85ディープダイブ](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)
- [ニュースレター #36: コメント（NIP-22）](/en/newsletters/2026-08-19-newsletter/#comments-nip-22)
- [ニュースレター #38: NIPディープダイブ](/en/newsletters/2026-09-02-newsletter/#reactions-nip-25)
- [ニュースレター #40: NIP-73のpodcast-mediumフィルター](/en/newsletters/2026-09-16-newsletter/#nip-73-proposes-podcast-medium-filters)
- [ニュースレター #42: 2024年9月の外部コンテンツ](/en/newsletters/2026-09-30-newsletter/#september-2024-posts-acquire-richer-context)

**関連項目:**
- [NIP-31: 未知のイベントkindの扱い](/ja/topics/nip-31/)
- [NIP-22: コメント](/ja/topics/nip-22/)
- [NIP-39: プロフィール内の外部アイデンティティ](/ja/topics/nip-39/)
- [NIP-85: Trusted Assertions](/ja/topics/nip-85/)
