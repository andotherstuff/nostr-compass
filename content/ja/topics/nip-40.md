---
title: "NIP-40: 有効期限タイムスタンプ"
date: 2025-12-17
translationOf: /en/topics/nip-40.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
---

NIP-40は、eventをいつ削除すべきかをrelayへ伝える`expiration`タグを定義します。

## 仕組み

eventにはUnix timestampを含む`expiration`タグを入れます。

```json
["expiration", "1734567890"]
```

この時刻を過ぎたら、relayはeventを削除し、配信を拒否するべきです。

## なぜ重要か

- 設定時間後に消えるべき一時的なcontent
- 期間限定のofferやannouncement
- marketplaceでのlisting有効期限（例: Shopstr）
- relay storage要件の削減

expirationは保持期間のヒントであり、取り消しの仕組みではありません。staleなcontentに対するrelayの挙動をそろえる助けにはなりますが、別のrelay、client、archiveがすでにeventをコピーしていれば、消去を保証するものではありません。

## 信頼とセキュリティの注意点

- relayはexpirationを守る義務はありませんが、多くは守ります。
- clientは、セキュリティ上重要なcontent削除をexpirationに頼るべきではありません。
- いったん別のclientがcontentを取得すると、cacheや再公開が起こり得ます。
- expirationは、eventが存在した事実までは隠しません。timestamp経過後も、event id、quote、relay外のcopyは残る可能性があります。

---

**主要ソース:**
- [NIP-40 Specification](https://github.com/nostr-protocol/nips/blob/master/40.md)

**言及箇所:**
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/)

**関連項目:**
- [NIP-01: Basic Protocol](/ja/topics/nip-01/)
