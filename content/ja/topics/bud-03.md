---
title: "BUD-03: ユーザーサーバーリスト"
url: /ja/topics/bud-03/
translationOf: /en/topics/bud-03.md
translationDate: 2026-03-07
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-03は、ユーザーが優先するBlossomサーバーを公開する方法を定義します。これにより、クライアントはblobをどこにアップロードすべきか、メディアURLが壊れたときにどこを探すべきかを把握できます。

## 仕組み

ユーザーは、1つ以上の`server`タグを持つ置換可能なkind `10063`イベントを公開します。各タグには完全なBlossomサーバーURLが入ります。

クライアントはこれによって次のことができます。
- ユーザーが優先するサーバーにblobをアップロードする
- 作者のpubkeyからblobのありそうな場所を見つける
- 古いURLが壊れたときに、一覧にあるサーバーから再取得を試す

## 読者向け補足

`server`タグの順序には意味があります。仕様では、最も信頼するサーバーや安定したサーバーを先頭に置くべきとされ、クライアントは少なくとも先頭のサーバーに対してアップロードを試す必要があります。つまり、BUD-03は単なる一覧ではなく、弱い優先度シグナルでもあります。

取得時の指針も実用的です。クライアントがURLからblobハッシュを取り出すときは、パス内の最後の64文字のhex文字列を使うべきとされています。これにより、標準的なBlossom URLだけでなく、ハッシュを埋め込んだ非標準のCDN風URLからでもblobを復元できます。

---

**主要ソース:**
- [BUD-03 Specification](https://github.com/hzrd149/blossom/blob/master/buds/03.md)
- [Blossom Repository](https://github.com/hzrd149/blossom)

**言及箇所:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)

**関連項目:**
- [Blossom Protocol](/ja/topics/blossom/)
- [NIP-51: Lists](/ja/topics/nip-51/)
