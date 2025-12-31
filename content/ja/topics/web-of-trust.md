---
title: "Web of Trust"
date: 2025-12-31
translationOf: /en/topics/web-of-trust.md
translationDate: 2025-12-31
draft: false
categories:
  - 信頼
  - ソーシャルグラフ
---

Web of Trust（WoT）は、評判と信頼性が中央機関ではなくソーシャルグラフの関係から導き出される分散型信頼モデルです。

## 仕組み

Nostrでは、Web of Trustはフォローグラフ（NIP-02コンタクトリスト）とレポートイベントを活用して信頼スコアを計算します：

1. **グラフ構築**: pubkey、イベント、およびそれらの関係（フォロー、ミュート、レポート）から有向グラフが構築される
2. **重み付け**: 信頼できることが知られているpubkey（例：検証済みNIP-05識別子を持つもの）に初期重みが割り当てられる
3. **反復伝播**: PageRankに似たアルゴリズムを使用して、信頼スコアがネットワーク全体に流れる
4. **Sybil耐性**: 攻撃者が多くの偽アカウントを作成した場合、それらに渡される信頼は偽の数で分割される

## 主要な特性

- **分散型**: 中央機関が評判を決定しない
- **パーソナライズ**: フォローしている人に基づいて各ユーザーの視点から信頼を計算できる
- **Sybil耐性**: 信頼の希釈により、ボットファームはシステムを簡単に操作できない
- **組み合わせ可能**: スパムフィルタリング、コンテンツモデレーション、relay入場、支払いディレクトリに適用できる

## Nostrでの応用

- **スパムフィルタリング**: relayはWoTを使用して低信頼コンテンツをフィルタリングできる
- **コンテンツ発見**: ネットワークが信頼するアカウントからのコンテンツを表示
- **支払いディレクトリ**: なりすまし防止付きのLightningアドレス検索
- **Relayポリシー**: WoT relayは信頼できるpubkeyからのノートのみを受け入れる
- **分散型モデレーション**: コミュニティは信頼スコアに基づいてキュレーションできる

## 実装

いくつかのプロジェクトがNostr用のWeb of Trustを実装しています：
- **Nostr.Band Trust Rank**: ネットワーク向けのPageRankスタイルのスコアリング
- **WoT Relays**: ソーシャル距離でフィルタリングするrelay
- **DCoSL**: 分散型レピュテーションシステム用プロトコル
- **Noswot**: フォローとレポートに基づく信頼スコアリング

---

**主要なソース：**
- [Nostr.Band Trust Rank](https://trust.nostr.band/)
- [DCoSLプロトコル](https://github.com/wds4/DCoSL)
- [Noswot](https://codeberg.org/weex/noswot)

**言及先：**
- [Newsletter #3: 12月の振り返り](/ja/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**関連項目：**
- [NIP-02: フォローリスト](/ja/topics/nip-02/)
