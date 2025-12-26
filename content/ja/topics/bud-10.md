---
title: "BUD-10: Blossom URIスキーム"
url: /ja/topics/bud-10/
translationOf: /en/topics/bud-10.md
translationDate: 2025-12-26
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-10は、利用可能な任意のサーバーからファイルを取得するために必要なすべての情報を埋め込むBlossom用カスタムURIスキームを定義します。

## URIフォーマット

```
blossom:<sha256>.<ext>?size=<bytes>&server=<url>&server=<url>&pubkey=<hex>
```

構成要素:
- **sha256**: ファイルハッシュ（必須）
- **ext**: ファイル拡張子
- **size**: ファイルサイズ（バイト）
- **server**: 1つ以上のサーバーヒント
- **pubkey**: BUD-03サーバー発見用の作成者pubkey

## メリット

- 静的HTTPURLより耐障害性が高い
- 複数サーバー間での自動フォールバック
- pubkeyヒントによる作成者ベースの発見
- 自己検証可能（ハッシュで整合性を保証）

---

**主要ソース:**
- [BUD-10 PR](https://github.com/hzrd149/blossom/pull/84)

**言及箇所:**
- [ニュースレター #1: ニュース](/ja/newsletters/2025-12-17-newsletter/#news)

**関連項目:**
- [Blossomプロトコル](/ja/topics/blossom/)
- [BUD-03: ユーザーサーバーリスト](/ja/topics/bud-03/)
