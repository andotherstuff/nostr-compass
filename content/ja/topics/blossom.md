---
title: "Blossomプロトコル"
url: /ja/topics/blossom/
translationOf: /en/topics/blossom.md
translationDate: 2025-12-26
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

Blossomは、コンテンツアドレス可能なURLを持つ分散型ファイルストレージを提供するNostr向けメディアホスティングプロトコルです。

## 仕組み

ファイルはBlossomサーバーに保存され、SHA256ハッシュでアドレス指定されます。これにより:
- 同じファイルはすべてのサーバーで常に同じURLを持つ
- ファイルを持つ任意のサーバーから取得可能
- クライアントはハッシュをチェックしてファイルの整合性を検証可能

## 機能

- コンテンツアドレス可能ストレージ
- 複数サーバーによる冗長性
- BUD-03による作成者の発見
- BUD-10によるカスタムURIスキーム
- `/list`エンドポイントでのカーソルベースのページネーション

---

**主要ソース:**
- [Blossomリポジトリ](https://github.com/hzrd149/blossom)

**言及箇所:**
- [ニュースレター #1: ニュース](/ja/newsletters/2025-12-17-newsletter/#news)
- [ニュースレター #2: 注目のコード変更](/ja/newsletters/2025-12-24-newsletter/#notable-code-and-documentation-changes)

**関連項目:**
- [BUD-03: ユーザーサーバーリスト](/ja/topics/bud-03/)
- [BUD-10: Blossom URIスキーム](/ja/topics/bud-10/)
