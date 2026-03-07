---
title: "NIP-10: テキストノートのスレッディング"
translationOf: /en/topics/nip-10.md
translationDate: 2026-03-07
date: 2025-12-24
draft: false
categories:
  - Protocol
  - Social
---

NIP-10は、kind 1 noteが互いを参照してreply threadを作る方法を定めます。conversation viewを正しく構築するには、これを理解している必要があります。

## 仕組み

誰かがnoteへ返信するとき、clientは次を知る必要があります。これは何へのreplyか。会話のrootは何か。誰へ通知すべきか。NIP-10は、`e` tag（event reference）と`p` tag（pubkey mention）を通じてこれに答えます。

## Marked Tags（推奨）

現在のclientは、`e` tag内で明示的なmarkerを使います。

```json
{
  "id": "f9c2e...",
  "pubkey": "a3b9c...",
  "created_at": 1734912345,
  "kind": 1,
  "tags": [
    ["e", "abc123...", "wss://relay.example.com", "root"],
    ["e", "def456...", "wss://relay.example.com", "reply"],
    ["p", "91cf9..."],
    ["p", "14aeb..."]
  ],
  "content": "Great point! I agree.",
  "sig": "b7d3f..."
}
```

`root` markerはthreadを始めた元noteを指します。`reply` markerは、いま返答している特定のnoteを指します。rootへ直接replyする場合は、`root`だけを使います（`reply` tagは不要です）。この区別はrenderingに重要です。`reply`はthread viewでのindentationを決め、`root`はすべてのreplyを同じthreadとして束ねます。

## Threading Rules

- **Direct reply to root:** `root` marker付きの`e` tagが1つ
- **Reply to a reply:** `root`と`reply`の`e` tagが2つ
- `root`はthread全体で変わらず、`reply`は返答対象に応じて変わる

## Notifications and Mentions

通知すべき全員の`p` tagを含めます。最低限、返信先noteのauthorはtag付けする必要があります。慣例として、親eventに入っていた`p` tagをすべて引き継ぎ、会話参加者を取りこぼさないようにします。さらに、content内で@mentionしたユーザーも含めます。

## Relay Hints

`e` tagと`p` tagの3番目の位置には、そのeventやユーザーのcontentが見つかる可能性があるrelay URLを入れられます。これにより、元のrelayへ接続していなくても、参照先contentを取得しやすくなります。

## 相互運用メモ

初期のNostr実装は、markerではなくtagの位置から意味を推測していました。最初の`e` tagをroot、最後をreply、中間をmentionとして扱っていたのです。この方法は曖昧さを生むため、いまは非推奨です。markerなしの`e` tagを見かけたら、古いclient由来である可能性が高いです。現在の実装は常に明示的なmarkerを出すべきです。

ただし、古いthreadを正しく表示したいclientは、両方の形式を解析する必要があります。実際のNIP-10 interoperabilityは一部が移行問題です。producerはmarked tagを出すべきですが、readerは古いposition-based formにも寛容である必要があります。

## Building Thread Views

threadを表示するには、まずroot eventを取得し、そのrootを参照する`e` tagを持つeventをすべて問い合わせます。

```json
["REQ", "thread", {"kinds": [1], "#e": ["<root-event-id>"]}]
```

結果を`created_at`で並べ、`reply` markerを使ってtree structureを構築します。`reply`がrootを指すeventはトップレベルのreplyです。`reply`が別のreplyを指すeventは入れ子のresponseになります。

---

**主要ソース:**
- [NIP-10 Specification](https://github.com/nostr-protocol/nips/blob/master/10.md)

**言及箇所:**
- [Newsletter #2: NIP Deep Dive](/en/newsletters/2025-12-24-newsletter/#nip-10-text-note-threading)

**関連項目:**
- [NIP-01: 基本プロトコル](/ja/topics/nip-01/)
- [NIP-18: Reposts](/ja/topics/nip-18/)
