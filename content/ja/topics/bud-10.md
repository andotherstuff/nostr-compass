---
title: "BUD-10: Blossom URIスキーム"
url: /ja/topics/bud-10/
translationOf: /en/topics/bud-10.md
translationDate: 2026-03-07
date: 2025-12-17
draft: false
categories:
  - Media
  - Protocol
---

BUD-10は`blossom:` URIスキームを定義します。これは、サーバーヒント、作者ヒント、想定サイズをファイルハッシュと一緒に持てる、持ち運び可能なblob参照です。

## URI形式

```
blossom:<sha256>.<ext>?xs=<server>&as=<pubkey>&sz=<bytes>
```

仕様では、小文字の64文字SHA-256ハッシュとファイル拡張子が必須です。拡張子が不明な場合、クライアントは`.bin`を使うべきとされています。

## 解決手順

クライアントは`blossom:` URIを段階的に解決します。

1. `xs`のサーバーヒントがあれば、出現順に試す
2. `as`の作者pubkeyがあれば、各作者の[BUD-03](/ja/topics/bud-03/)サーバーリストを取得して、そのサーバーを試す
3. 必要なら既知のサーバーやローカルキャッシュにフォールバックする

この順序は実用的です。送信者は即座に取得できるヒントを添えつつ、それらのヒントが古くなっても受信者に回復経路を残せます。

## 重要性

`blossom:` URIは通常のメディアURLより、magnet linkに近い振る舞いをします。どのblobを取得すべきかを表し、そのblobをどこで見つけられるかの手掛かりを含みます。1つのホストが永続的に利用可能であることを前提にしません。

任意の`sz`フィールドは、ハッシュに加えて具体的な整合性チェックを提供します。クライアントはダウンロード前後で想定サイズを検証でき、不完全な転送を検出しやすくなり、大きなメディアでもUXを改善できます。

---

**主要ソース:**
- [BUD-10 Specification](https://github.com/hzrd149/blossom/blob/master/buds/10.md)
- [Blossom Repository](https://github.com/hzrd149/blossom)

**言及箇所:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)

**関連項目:**
- [Blossom Protocol](/ja/topics/blossom/)
- [BUD-03: User Server List](/ja/topics/bud-03/)
