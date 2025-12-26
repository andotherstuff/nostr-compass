---
title: "BUD-03: ユーザーサーバーリスト"
url: /ja/topics/bud-03/
translationOf: /en/topics/bud-03.md
translationDate: 2025-12-26
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-03は、ユーザーが優先するBlossomサーバーを公開する方法を定義し、クライアントがユーザーのメディアファイルをアップロード・取得する場所を発見できるようにします。

## 仕組み

ユーザーはBlossomサーバーをリストしたkind 10063イベントを公開します。これにより、クライアントは:
- ユーザーの優先サーバーにメディアをアップロード
- pubkeyからユーザーのblobを見つける場所を発見

これにより、コンテンツにサーバーURLを直接埋め込む代替として、作成者ベースの発見が可能になります。

---

**主要ソース:**
- [BUD-03仕様](https://github.com/hzrd149/blossom/blob/master/buds/03.md)

**関連項目:**
- [Blossomプロトコル](/ja/topics/blossom/)
- [NIP-51: リスト](/ja/topics/nip-51/)
