---
title: "NIP-17: プライベートダイレクトメッセージ"
date: 2025-12-17
translationDate: 2026-03-07
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-17は、送信者のプライバシーを守るためにNIP-59のgift wrappingを使うプライベートダイレクトメッセージを定義します。外側のイベントで送信者が露出するNIP-04 DMとは違い、NIP-17は送信者をリレーや何気なく観測している第三者から隠します。

## 仕組み

メッセージは複数の暗号化レイヤーで包まれます。

1. 実際のメッセージ内容はkind 14のrumor eventに入ります。
2. sealがその内容を受信者向けに暗号化します。
3. gift wrapがsealをさらに暗号化し、使い捨てのkeypairから公開します。

外側のgift wrapはランダムな使い捨てキーペアを使用するため、リレーや観察者は誰がメッセージを送信したかを判断できません。

## メッセージ構造

- **Kind 14** - ラップされたレイヤーの内側にある実際のDM内容
- **Kind 1059** - リレーに公開される外側のgift wrapイベント
- ラッピングの内部ペイロードにはNIP-44暗号化を使います
- 仕様は、reactionsのような対話的DM機能をより扱いやすくする方向で整理されています

## セキュリティと信頼モデル

- リレーは送信者を見ることができない（gift wrapの使い捨てキーペアで隠される）
- 受信者は見える（gift wrapの`p`タグ内）
- メッセージのタイムスタンプはウィンドウ内でランダム化される
- リレー上で可視のスレッディングや会話グループ化がない

受信者はアンラップ後に送信者が誰かを知ります。NIP-17が隠すのはネットワークに対する送信者の識別情報であって、相手参加者に対する識別情報ではありません。これが「private DMs」という表現を考えるうえで重要な区別です。

## なぜ重要か

NIP-04 DMはコンテンツを暗号化しますがメタデータは公開されたまま:
- 送信者pubkeyは公開
- 受信者pubkeyは`p`タグ内
- タイムスタンプは正確

NIP-17はより複雑な実装を犠牲にして送信者を隠します。

その複雑さによって、実際のプライバシー改善が得られます。リレーはラップされたメッセージが特定の受信者宛てであることまでは見えますが、kind 4メッセージの外側メタデータのように、送信者と受信者の関係を直接組み立てることはできません。

## 相互運用メモ

NIP-17はプライベートメッセージ向けのinbox relay listも定義します。クライアントはkind 10050イベントを公開して、送信者がDM配信先としてどのリレーを使うべきかを知らせられます。DMの配送経路を公開コンテンツの経路と分けることで、プライベートなトラフィックを誤った場所に流すのを避けやすくなります。

---

**主要ソース:**
- [NIP-17仕様](https://github.com/nostr-protocol/nips/blob/master/17.md)
- [PR #2098](https://github.com/nostr-protocol/nips/pull/2098) - wording cleanup and reaction support update

**言及箇所:**
- [ニュースレター #1: NIP更新](/ja/newsletters/2025-12-17-newsletter/#nip-updates)
- [ニュースレター #2: ニュース](/ja/newsletters/2025-12-24-newsletter/#news)
- [ニュースレター #3: December Recap](/ja/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [ニュースレター #3: Notable Code Changes](/ja/newsletters/2025-12-31-newsletter/#shopstr-marketplace)
- [ニュースレター #5: ニュース](/ja/newsletters/2026-01-13-newsletter/#news)

**関連項目:**
- [NIP-04: Encrypted Direct Messages (Deprecated)](/ja/topics/nip-04/)
- [NIP-44: Encrypted Payloads](/ja/topics/nip-44/)
- [NIP-59: Gift Wrap](/ja/topics/nip-59/)
