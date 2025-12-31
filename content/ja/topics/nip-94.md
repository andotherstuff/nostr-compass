---
title: "NIP-94: File Metadata"
date: 2025-12-31
translationOf: /en/topics/nip-94.md
translationDate: 2025-12-31
draft: false
categories:
  - メディア
  - プロトコル
---

NIP-94は、Nostr上で共有されるファイルを整理・分類するためのファイルメタデータイベント（kind 1063）を定義し、relayがコンテンツを効果的にフィルタリング・整理できるようにします。

## 仕組み

1. ユーザーがホスティングサービスにファイルをアップロード
2. ファイルに関するメタデータを含むkind 1063イベントが公開される
3. イベントの内容には人間が読める説明が含まれる
4. 構造化されたtagが機械可読なメタデータを提供
5. 専門的なクライアントがファイルを体系的に整理・表示できる

## 必須タグとオプションタグ

**主要なtag：**
- `url` - ファイルのダウンロードリンク
- `m` - MIME type（小文字形式が必須）
- `x` - ファイルのSHA-256ハッシュ

**オプションのtag：**
- `ox` - サーバー変換前のオリジナルファイルのSHA-256ハッシュ
- `size` - バイト単位のファイルサイズ
- `dim` - 画像/動画の寸法（幅 x 高さ）
- `magnet` - torrent配布用のmagnet URI
- `i` - torrent infohash
- `blurhash` - プレビュー用のプレースホルダー画像
- `thumb` - サムネイルURL
- `image` - プレビュー画像URL
- `summary` - テキスト抜粋
- `alt` - アクセシビリティ説明
- `fallback` - 代替ダウンロードソース

## ユースケース

NIP-94は、ソーシャルや長文コンテンツクライアントではなく、ファイル共有アプリケーション向けに設計されています。推奨されるアプリケーションには以下が含まれます：

- Torrentインデックスrelay
- ポートフォリオ共有プラットフォーム（Pinterestに類似）
- ソフトウェア設定とアップデートの配布
- メディアライブラリとアーカイブ

---

**主要なソース：**
- [NIP-94仕様](https://github.com/nostr-protocol/nips/blob/master/94.md)

**言及先：**
- [Newsletter #3: 12月の振り返り](/ja/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**関連項目：**
- [NIP-92: メディア添付](/ja/topics/nip-92/)
- [Blossom](/ja/topics/blossom/)
