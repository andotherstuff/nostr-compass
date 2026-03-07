---
title: "NIP-84: ハイライト"
date: 2026-02-18
translationOf: /en/topics/nip-84.md
translationDate: 2026-03-07
draft: false
categories:
  - Content
  - Protocol
---

NIP-84はkind `9802`のhighlight eventを定義し、userがNostr上のlong-form contentから価値があると感じた一節をマークして共有できるようにします。

## 仕組み

`.content` fieldにはhighlightされたtextが入ります。source materialは、Nostr native contentなら`a`または`e` tagで、external URLなら`r` tagで参照します。clientはtracking parameterを取り除くべきです。optionalな`p` tagは元のauthorを示し、highlightが大きな一節の一部なら、optionalな`context` tagで前後の文脈を持たせられます。

text以外のmediaでは、highlight contentは空でも構いません。これによりclientは、source referenceをtagに残したまま、audioやvideoのhighlightを指せます。

## 引用ハイライト

userは`comment` tagを追加してquote highlightを作れます。これはquoted repostとしてrenderされ、microblogging clientでの重複表示を防ぎます。comment内では、`p` tagのmentionに`mention`属性を付けてauthor/editor attributionと区別する必要があります。`r` tagのURLにはorigin referenceとして`source`属性を使います。

## なぜ重要か

NIP-84は、highlightされた一節と周辺の議論を分離します。clientは、選択されたtextを主役としてrenderし、commentaryはoptional metadataとして扱えます。通常のnoteに両方を混ぜる必要がありません。

これはreading toolやresearch toolで役立ちます。正確なexcerptを保ったまま、2人のreaderが同じarticleに別々のcommentを付けても、他のclientが理解できるportableなhighlight eventとして扱えます。

## 相互運用メモ

attribution tagは見た目以上に重要です。`author`や`editor` roleを持つ`p` tagはsource materialの作成者を示しますが、quote comment内の`mention` roleは別の意味を持ちます。clientがこれらを混同すると、sourceの表示やnotificationを誤る可能性があります。

---

**主要ソース:**
- [NIP-84 Specification](https://github.com/nostr-protocol/nips/blob/master/84.md)

**言及箇所:**
- [Newsletter #10: Releases](/en/newsletters/2026-02-18-newsletter/#prism-share-anything-to-nostr-from-android)

**関連項目:**
- [NIP-94: File Metadata](/ja/topics/nip-94/)
