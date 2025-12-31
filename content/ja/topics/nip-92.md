---
title: "NIP-92: Media Attachments"
date: 2025-12-31
translationOf: /en/topics/nip-92.md
translationDate: 2025-12-31
draft: false
categories:
  - メディア
  - プロトコル
---

NIP-92は、リソースを説明するインラインメタデータタグとともにURLを含めることで、ユーザーがNostrイベントにメディアファイルを添付できるようにします。

## 仕組み

1. ユーザーがイベントコンテンツに直接メディアURLを配置（例：kind 1のテキストノート内）
2. 対応する`imeta`（インラインメタデータ）タグが各URLの詳細を提供
3. クライアントはメタデータに基づいてimeta URLをリッチプレビューに置き換え可能
4. メタデータは通常、作成中にファイルがアップロードされると自動生成される

## imetaタグ

各`imeta`タグには`url`と少なくとも1つの他のフィールドが必要です。サポートされるフィールドには以下が含まれます：

- `url` - メディアURL（必須）
- `m` - ファイルのMIMEタイプ
- `dim` - 画像の寸法（幅 x 高さ）
- `blurhash` - プレビュー生成用のblurhash
- `alt` - アクセシビリティのための代替テキスト
- `x` - SHA-256ハッシュ（NIP-94より）
- `fallback` - プライマリが失敗した場合の代替URL

## 例

```json
["imeta",
  "url https://example.com/image.jpg",
  "m image/jpeg",
  "dim 1920x1080",
  "blurhash LKO2?U%2Tw=w]~RBVZRi}^Xu%LRj"
]
```

---

**主要な情報源:**
- [NIP-92仕様](https://github.com/nostr-protocol/nips/blob/master/92.md)

**関連記事:**
- [ニュースレター#3: 12月の振り返り](/ja/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**関連項目:**
- [NIP-94: ファイルメタデータ](/ja/topics/nip-94/)
