---
title: "NIP-101e: フィットネスワークアウト"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-101e.md
translationDate: 2026-07-01
categories:
  - Fitness
  - Discovery
---

NIP-101eは、フィットネストラッキングアプリケーションがNostr上でトレーニングセッションを公開、共有、発見できるようにするワークアウトイベント形式を定義します。この仕様では、セッションのメトリクス（距離、時間、標高、心拍数、カロリー、サイクリングのケイデンス、送信元アプリ）を構造化タグで運ぶkind 1301イベントを使用し、クライアントがワークアウトを適切な単位でメトリクスを表示する構造化カードとしてレンダリングできるようにします。

## 仕組み

NIP-101eのワークアウトは、送信元アプリが取得した各メトリクスに対する構造化タグを持つkind 1301イベントです。一般的なタグには以下があります。

- ワークアウトの種目（ラン、バイク、スイム、リフトなど）を示す`type`
- 値と単位を持つ`distance`
- 秒単位の`duration`
- 値と単位を持つ`elevation_gain`
- `start`と`end`のタイムスタンプ
- `heart_rate`（平均値と最大値）
- エネルギー消費量を示す`calories`
- 公開するアプリケーションを示す`source`
- ハッシュタグによる発見のための`t`トピックタグ

`content`フィールドには、ユーザが記述した任意のノートが入ります（ユーザがStravaアップロードに添えるキャプションに相当します）。kind 1301を認識するクライアントは構造化メトリクスをワークアウトカードとしてレンダリングし、認識しないクライアントは`content`フィールドを通常のノートとして表示するフォールバックを取ります。

## 発見とフィードの仕様

NIP-101eイベントは通常のフィードイベントであるため、ユーザが投稿したワークアウトは他の投稿と同じようにフォロワーのタイムラインに表示されます。専用のワークアウトビューを持つクライアントは、作者やハッシュタグのフィルタでkind 1301を購読し、トレーニングログの画面、リーダーボード、コミュニティチャレンジのフィードを構築できます。作者のpubkeyがワークアウトの正規の身元であるため、他のユーザのワークアウトを読み取るサードパーティアプリケーションは、他のNostrフィードと同じ信頼前提を継承します。

## 実装

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) は、ヒーローメトリクス、統計グリッド、サイクリング固有の速度表示、送信元バッジを備えたkind 1301ワークアウトのレンダリングを搭載しました（[PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184)、[PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226)でリファクタリング）

---

**Primary sources:**
- [NIP-101e仕様](https://github.com/nostr-protocol/nips/blob/master/101e.md)
- [Amethyst PR #3184](https://github.com/vitorpamplona/amethyst/pull/3184) - NIP-101eフィットネスワークアウトサポート（Kind 1301）を追加
- [Amethyst PR #3226](https://github.com/vitorpamplona/amethyst/pull/3226) - ヒーローメトリクスと統計グリッドでワークアウト表示を再設計

**Mentioned in:**
- [Newsletter #27: Amethyst v1.12.0 ships Cashu wallets, nutzaps, a CLINK driver, and Tor self-heal](/ja/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)
