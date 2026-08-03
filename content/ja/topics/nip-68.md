---
title: "NIP-68：画像を中心にしたフィード"
date: 2026-07-29
translationOf: /en/topics/nip-68.md
translationDate: 2026-07-29
draft: false
categories:
  - Media
  - Protocol
---

NIP-68 は、アドレス指定可能な画像 event を定義します。画像のメタデータ、キャプション、ラベル、画像ファイルへの参照を公開するための移植可能な手段をクライアントに提供しつつ、event 自体を blob ストレージから分離します。

## 仕組み

画像は kind `20` を使用し、`title` tag と `content` 内の説明を含みます。`imeta` tag は、`url`、MIME タイプを示す `m`、寸法を示す `dim`、代替テキストの `alt`、任意の SHA-256 ハッシュなどのフィールドで各画像を記述します。複数の `imeta` tag により、1 つの event で画像セットを表現できます。

event には、被写体またはクレジット対象となる人物を示す `p` tag、トピックを示す `t` tag、通常の Nostr 参照を含められます。メディアタイプ、ハッシュ、場所、コンテンツ警告の tag も含められるため、クライアントは画像投稿を一貫して絞り込み、表示できます。

NIP-68 はストレージのバックエンドを規定しません。別のクライアントが画像を表示して検証できるだけの `imeta` メタデータを公開する限り、クライアントは通常の HTTPS URL や Blossom のようなコンテンツアドレス型システムを参照できます。

## 実装

[NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0) は、画像中心のクライアント機能とともに NIP-68 の画像 tag を追加しました。

---

**主要ソース：**
- [NIP-68 仕様](https://github.com/nostr-protocol/nips/blob/master/68.md)
- [NoorNote 1.3.0](https://github.com/77elements/noornote/releases/tag/v1.3.0)

**掲載号：**
- [Newsletter #33：タグ付きリリース](/ja/newsletters/2026-07-29-newsletter/#tagged-releases)

**関連項目：**
- [Blossom プロトコル](/ja/topics/blossom/)
- [NIP-94：ファイルメタデータ](/ja/topics/nip-94/)
