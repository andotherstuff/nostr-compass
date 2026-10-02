---
title: "Buzz NIP-AR: チャンネルアーティファクト"
date: 2026-09-30
translationOf: /en/topics/nip-ar.md
translationDate: 2026-10-02
draft: false
categories:
  - Project Proposals
  - Collaboration
---

NIP-ARは、Buzzの**プロジェクト固有**のチャンネルアーティファクト仕様です。ここでの名称は、`nostr-protocol/nips`リポジトリや他のrelayに採用されたことを意味しません。

## アーティファクトモデル

アーティファクトは編集可能な記録であり、安定した`d`のidentity、`h` tagで示される1つの所属チャンネル、そして`prev`でつながった完全なスナップショットのリビジョンを持ちます。relayは、`prev`が現在の先頭を指している場合にのみ編集を受け入れます。そのため、競合する2つのリビジョンが両方とも次の先頭になることはありません。Buzzの実装では、アーティファクトにkind `45010`を使い、アーティファクトがチャンネルの外へ移動したときにはrelayが署名したkind `45011`のマーカーを使います。移動元のチャンネルは、そのマーカーから移動先を知ることなく削除を確認できます。

[Buzzの仕様マージ](https://github.com/block/buzz/pull/7791)はこのモデルを説明しており、[relay実装のマージ](https://github.com/block/buzz/pull/7919)は競合処理、履歴クエリ、移動、チャンネル権限のテストを報告しています。これらのマージが確立するのはプロジェクトのソース上の挙動であり、一般的なNostr標準や公開環境での展開の保証ではありません。

---

**主要ソース:**
- [Buzzのチャンネルアーティファクト仕様のマージ](https://github.com/block/buzz/pull/7791)
- [Buzzのチャンネルアーティファクト実装のマージ](https://github.com/block/buzz/pull/7919)

**言及箇所:**
- [Newsletter #42: Buzzのチャンネルアーティファクト](/ja/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
