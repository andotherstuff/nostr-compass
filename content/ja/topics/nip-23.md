---
title: "NIP-23: Long-form Content"
date: 2026-04-08
translationOf: /en/topics/nip-23.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Content
---

NIP-23は、Nostr上の長文コンテンツ向けにkind `30023`を定義します。kind `1`の短文ノートとは異なり、長文イベントは`d`タグで識別されるparameterized replaceable eventで、Markdown整形をサポートし、タイトル、要約、画像、公開日といったmetadata tagsを含められます。

## 仕組み

長文イベントはkind `30023`を使い、一意な識別子として`d`タグを持ちます。これにより、作者は同じ`d`タグを使った新しいイベントを公開してコンテンツを更新できます。`content`フィールドにはMarkdownテキストが入り、標準タグには`title`、`summary`、`image`（header image URL）、`published_at`（元の公開時刻）、`t`（hashtag）が含まれます。parameterized replaceable eventであるため、relayは作者ごとの各`d`タグについて最新バージョンだけを保存します。

## 主要タグ

- `d` - 一意な記事識別子（slug）
- `title` - 記事タイトル
- `summary` - 短い説明
- `image` - header image URL
- `published_at` - 元の公開Unix timestamp（編集のたびに更新される`created_at`とは別）
- `t` - hashtagやtopic tags

## Implementations

- [Habla](https://habla.news) - 長文コンテンツのreader兼publisher
- [YakiHonne](https://yakihonne.com) - 長文コンテンツプラットフォーム
- [Highlighter](https://highlighter.com) - 読書とannotationのツール

---

**Primary sources:**
- [NIP-23 specification](https://github.com/nostr-protocol/nips/blob/master/23.md)

**See also:**
- [NIP-01（Basic Protocol）](/ja/topics/nip-01/)
