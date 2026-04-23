---
title: "NIP-24: 追加メタデータフィールド"
date: 2025-12-17
translationOf: /en/topics/nip-24.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Identity
---

NIP-24は基本的なname、about、picture以外のkind 0ユーザーメタデータ用の追加オプションフィールドを定義します。

## 追加メタデータフィールド

- **display_name**: `name`よりも大きく、より豊かな文字を持つ代替名
- **website**: イベント作成者に関連するWeb URL
- **banner**: オプションのバックグラウンド表示用のワイド（約1024x768）画像へのURL
- **bot**: コンテンツが完全にまたは部分的に自動化されていることを示すブール値
- **birthday**: オプションのyear、month、dayフィールドを持つオブジェクト

仕様では古い2つのフィールドもdeprecatedとされています。`displayName`は`display_name`に、`username`は`name`に置き換えるべきです。実際には今でも使われているので、書き出し側は使わなくても、パーサー側は後方互換性のために受け入れたほうがよいです。

## 標準タグ

NIP-24は汎用タグも標準化しています:
- `r`: Web URL参照
- `i`: 外部識別子
- `title`: 様々なイベントタイプ用の名前
- `t`: ハッシュタグ（小文字でなければならない）

## なぜ重要か

NIP-24の主眼は収束です。これらのフィールドやタグはすでに複数のクライアントで現れていたため、仕様が名前と意味をそろえます。これにより、bannerを`banner`に入れるのか、アプリ固有キーに入れるのかのような、小さいが面倒な不一致を減らせます。

実装者にとって実務上のポイントは、kind 0がほとんどのクライアントでhot pathだということです。追加メタデータは軽量に保つべきです。独自の取得パターンや独立した更新周期が必要なフィールドなら、profile metadataを膨らませるのではなく別イベントkindに分けたほうが適切です。

---

**主要ソース:**
- [NIP-24仕様](https://github.com/nostr-protocol/nips/blob/master/24.md)

**言及箇所:**
- [ニュースレター #1: NIP更新](/ja/newsletters/2025-12-17-newsletter/#nip-updates)

**関連項目:**
- [NIP-01: 基本プロトコル](/ja/topics/nip-01/)
