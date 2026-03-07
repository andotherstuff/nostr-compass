---
title: "NIP-73: External Content IDs"
date: 2026-02-04
translationOf: /en/topics/nip-73.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Discovery
  - Metadata
---

NIP-73は、Nostr event内でexternal contentを参照する標準的な方法を定義します。識別子そのものには`i` tagを、識別子の種類には`k` tagを使い、book、website、podcast episode、location、hashtag、blockchain objectなど同じ対象を指す議論をclient間でまとめられるようにします。

## 仕組み

NIP-73を使うeventには、正規化されたexternal identifierを含む`i` tagと、そのidentifier種別を示す`k` tagが入ります。clientはその組み合わせで、同じsubjectを参照するeventをまとめて検索できます。

```json
{
  "tags": [
    ["i", "isbn:9780765382030"],
    ["k", "isbn"]
  ]
}
```

仕様は次のようなidentifier familyを扱います。

- fragmentを除いた正規化web URL
- book用のISBN
- film用のISAN
- geohashとISO 3166のcountry/subdivision code
- podcast feed、episode、publisher GUID
- hashtag
- blockchain transactionとaddress identifier

## 正規化ルール

NIP-73でreader向けにいちばん重要なのは正規化です。同じsubjectは1つのcanonical stringへそろうべきで、そうでないと同じ意味のidentifierが複数に割れ、議論が分断されます。

仕様の例では次のように決まっています。

- geohashは`geo:<value>`を使い、小文字にする
- country codeとsubdivision codeは`iso3166:<code>`を使い、大文字にする
- ISBNはhyphenを除く
- web URLはfragmentを落とす
- blockchain transaction hashは小文字hexを使う

細かく見えても、これが1つの共有会話になるか、互換性のない複数indexに分かれるかの違いになります。

## 便利な使い方

NIP-73はcontent formatではなく、汎用のreference layerです。long-form noteがbookのISBNを指したり、reviewがfilmのISANを指したり、local postがgeohashやcountry codeを指したりできます。そのたびに専用tagを新設する必要はありません。

仕様では、`i` tagの第2値としてoptionalなURL hintも許しています。identifier type専用のrendererを持たないclientでも、それをfallback linkとして使えます。

## なぜ重要か

Nostrにはeventやprofile向けの強い内部参照がすでにあります。NIP-73はその考え方をNostr外の対象へ広げます。identifierが正規化されていれば、comment、rating、highlight、trusted assertionを、異なるclient間でも同じexternal subjectへ結び付けられます。

これが、NIP-85がNIP-73を土台にしている理由でもあります。Trusted Assertionsは、userやeventだけでなく、book、website、hashtag、locationのようなNIP-73 identifierも評価対象にできます。

---

**主要ソース:**
- [NIP-73 Specification](https://github.com/nostr-protocol/nips/blob/master/73.md)
- [PR #2205](https://github.com/nostr-protocol/nips/pull/2205) - Adds ISO 3166 country and subdivision codes

**言及箇所:**
- [Newsletter #8: NIP Updates](/en/newsletters/2026-02-04-newsletter/#nip-updates)
- [Newsletter #10: NIP-85 Deep Dive](/en/newsletters/2026-02-18-newsletter/#nip-deep-dive-nip-85-trusted-assertions)

**関連項目:**
- [NIP-85: Trusted Assertions](/ja/topics/nip-85/)
