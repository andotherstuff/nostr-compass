---
title: "Bitcredit"
date: 2026-03-25
translationOf: /en/topics/bitcredit.md
translationDate: 2026-04-01
draft: false
categories:
  - 金融
  - 商取引
  - インフラストラクチャ
---

Bitcreditは企業向けの電子手形貿易金融システムです。公式サイトではBitcredit Coreを電子手形の発行、裏書、支払い、管理のためのソフトウェアとして紹介しており、オープンソースのコアリポジトリはビジネスロジックと永続化クレートに加えてNostrトランスポートレイヤーを実装しています。

## 仕組み

Bitcreditは貿易信用を電子手形（ebill）としてモデル化します。買い手が将来の支払期日付きのebillを発行し、保有者はそれを他の企業に裏書でき、最終保有者は満期時に支払いを請求できます。

Bitcreditのサイトではミントベースの流動性パスも説明されています。満期を待つ代わりに、保有者はBitcreditミントにオファーをリクエストし、即座にecashを受け取り、そのecashでサプライヤーや従業員に支払うことができます。

## 実装に関する注記

`Bitcredit-Core`リポジトリはシステムを複数のRustクレートに分割しています。`bcr-ebill-core`がデータモデルを処理し、`bcr-ebill-api`がビジネスロジックを含み、`bcr-ebill-persistence`がストレージを処理し、`bcr-ebill-transport`がNostr実装を含むネットワークトランスポートAPIを提供します。

このアーキテクチャが重要なのは、Bitcreditが単なるウェブサイトやウォレットフローではないからです。トランスポート、状態、決済ロジックが再利用可能なコンポーネントに分離されたビジネス文書システムであり、Webデプロイメント用のWASMエントリーポイントも含まれています。

## 最近の動向

Compassは2026年3月に初めてBitcreditを取り上げました。`v0.5.3`でBill支払いアクションとBill状態のAPIフィールドが追加され、匿名署名者の署名アドレス処理が修正されました。次のリリース`v0.5.4`では`BitcreditBillResult`の適応、支払いと承認状態の改善、オプションフィールドのより明示的な処理の追加により、このAPI作業が継続されました。

これらの変更はBitcreditの広範なコンセプトと比較すると小規模ですが、実装の方向性を示しています。よりクリーンなフロントエンドエルゴノミクス、より明確なBillライフサイクル状態、匿名または無記名署名フローのより良い処理です。

---

**主要ソース:**
- [Bitcreditウェブサイト](https://www.bit.cr/)
- [Bitcredit: 仕組み](https://www.bit.cr/how-it-works)
- [Bitcredit-Coreリポジトリ](https://github.com/BitcreditProtocol/Bitcredit-Core)
- [Bitcredit-Coreドキュメントインデックス](https://github.com/BitcreditProtocol/Bitcredit-Core/blob/master/docs/index.md)
- [Bitcredit v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3)
- [Bitcredit v0.5.4](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.4)
- [PR #846: ステータスフラグの改善と支払いアクションの追加](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846)
- [PR #849: 匿名署名者の署名アドレスと署名者の修正](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849)

**掲載号:**
- [Newsletter #13: Bitcredit v0.5.3](/en/newsletters/2026-03-11-newsletter/#bitcredit-v053)
