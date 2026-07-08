---
title: "NIP-B0: Webブックマーク"
date: 2026-05-28
draft: false
translationOf: /en/topics/nip-b0.md
translationDate: 2026-07-01
categories:
  - Protocol
  - Social
---

NIP-B0は、WebブックマークをファーストクラスのNostrイベントとして公開する、パラメータ化された置き換え可能イベント（kind 39701）を定義します。この提案により、ユーザは中央集権的なブックマークサービスに依存することなく、クライアントをまたいで発見、zap、再公開できる、キュレーションされたブックマークコレクションを構築できます。

## 仕組み

ブックマークはkind 39701のイベントで、`d`タグはブックマーク対象ページの正規URLです。置き換え可能な仕様により、作者は重複するイベントを生成することなく、そのURLに対する自分のブックマークを更新できます（再タグ付け、タイトル更新、古くなった印を付ける）。contentフィールドはブックマークに関する作者のメモを運びます。タグにはタイトル、説明、画像、そして発見のための`t`トピックタグが含まれます。

```json
{
  "kind": 39701,
  "tags": [
    ["d", "https://example.com/an-article-worth-saving"],
    ["title", "Article Title"],
    ["t", "nostr"],
    ["t", "protocol"],
    ["published_at", "1717000000"]
  ],
  "content": "Useful primer on the topic.",
  "pubkey": "...",
  "sig": "..."
}
```

`d`タグは作者ごとにブックマークを一意に識別するため、2人のユーザは同じURLをそれぞれ独自の注釈とタグセットでブックマークできます。

## 発見とキュレーション

すべてのブックマークがファーストクラスのイベントであるため、任意のNostrクライアントは、タグや作者でフィルタリングしてkind 39701イベントを購読することで、ブックマークのフィードをレンダリングできます。キュレーター主導のワークフローが自然に成り立ちます。キュレーターがブックマークのリストを公開し、読者はキュレーターのpubkeyをフォローし、ブックマークはそれらを運ぶ任意のrelayを通じて流れます。中央集権的なディレクトリはありません。

## 実装

- [deepmarks-public](https://github.com/ostermayer/deepmarks-public) — 3ボックスアーキテクチャ（キュレーター、インデクサ、ビューア）と、キュレーター宛の直接NIP-57 zapで賄われるティアシステムを備えたリファレンスWebクライアント。ファイルストレージのためにNIP-07、NIP-46、NIP-57、NIP-44、NIP-98、NIP-65、Blossom BUD-01／BUD-04と共にNIP-B0を実装しています。

## 信頼とセキュリティに関する注意

- ブックマークはデフォルトで公開されます。プライベートな閲覧リストをこの方法で公開してはいけません
- 再公開はrelayがイベントを保持し続けることに依存します。エフェメラルrelayはブックマークをドロップします
- `published_at`タグは公開者が主張するもので、検証可能ではありません

---

**Primary sources:**
- [NIP-B0の提案仕様](https://github.com/nostr-protocol/nips/pull/2089) — 提案されたkind 39701 Webブックマークイベントを追跡
- [deepmarks-public](https://github.com/ostermayer/deepmarks-public) — キュレーターティアシステムを備えたリファレンス実装

**Mentioned in:**
- [Newsletter #24: deepmarks NIP-B0 bookmarks with curator-monetized publishing](/ja/newsletters/2026-05-28-newsletter/#deepmarks-nip-b0-bookmarks-with-curator-monetized-publishing)
- [Newsletter #27: Also shipped](/ja/newsletters/2026-06-17-newsletter/#also-shipped)

**See also:**
- [NIP-57: Lightning Zaps](/ja/topics/nip-57/)
- [NIP-65: Relay List Metadata](/ja/topics/nip-65/)
