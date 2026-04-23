---
title: "NIP-17: Private Direct Messages"
date: 2025-12-17
translationOf: /en/topics/nip-17.md
translationDate: 2026-04-22
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-17は、送信者privacyのためにNIP-59 gift wrappingを使うprivate direct messagesを定義します。外側のイベントで送信者が露出するNIP-04 DMとは異なり、NIP-17はrelayや受動的な観測者から送信者を隠します。

## 仕組み

メッセージは複数の暗号化層で包まれます。
1. 実際のメッセージcontentはkind 14のrumor eventに入る
2. sealがそのcontentを受信者向けに暗号化する
3. gift wrapがsealをさらに暗号化し、使い捨てkeypairから公開する

外側のgift wrapはランダムな使い捨てkeypairを使うため、relayや観測者は誰がメッセージを送ったか判定できません。

## メッセージ構造

- **Kind 14** - 包まれた層の最内側にある実際のDM content
- **Kind 1059** - relayへ公開される外側のgift wrap event
- 包装フロー内のpayloadにはNIP-44 encryptionを使う
- 仕様は、reactionsのような対話的DM機能をよりよく支えるため改善されてきた

## セキュリティと信頼モデル

- gift wrapの使い捨てkeypairにより、relayは送信者を見られない
- 受信者は見える（gift wrapの`p`タグ内）
- メッセージtimestampは一定の範囲でランダム化される
- relay上ではvisibleなthreadingや会話グループ化がない

受信者は、unwrapした後には誰が送ったかを知ります。NIP-17が隠すのはネットワークに対する送信者identityであって、相手参加者に対してではありません。NIP-17を「private DMs」と呼ぶとき、この違いは重要です。

## なぜ重要か

NIP-04 DMはcontentを暗号化しても、metadataは可視のままです。

- 送信者pubkeyは公開される
- 受信者pubkeyは`p`タグに入る
- timestampは正確なまま

NIP-17は、その代償として実装が複雑になる一方、送信者を隠します。

この複雑さは実際のプライバシー改善をもたらします。relayはwrapped messageが誰宛てかは見えても、kind 4メッセージのように外側metadataだけで直接的な送信者-受信者グラフを構築できません。

## 相互運用メモ

NIP-17は、private messaging向けのinbox relay listも定義します。clientはkind 10050イベントを公開し、送信者がDM配信先としてどのrelayを使うべきか分かるようにします。DM routingをpublic content routingと分離することで、private trafficを誤った場所へ公開するリスクを減らせます。

---

**Primary sources:**
- [NIP-17 Specification](https://github.com/nostr-protocol/nips/blob/master/17.md)
- [PR #2098](https://github.com/nostr-protocol/nips/pull/2098) - wording cleanup and reaction support update

**Mentioned in:**
- [Newsletter #1: NIP Updates](/ja/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: News](/ja/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #5: News](/ja/newsletters/2026-01-13-newsletter/)
- [Newsletter #13: Vector](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19: NipLock password manager](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-04: Encrypted Direct Messages (Deprecated)](/ja/topics/nip-04/)
- [NIP-44: Encrypted Payloads](/ja/topics/nip-44/)
- [NIP-59: Gift Wrap](/ja/topics/nip-59/)
