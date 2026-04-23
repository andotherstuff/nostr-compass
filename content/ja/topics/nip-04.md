---
title: "NIP-04: Encrypted Direct Messages (Deprecated)"
date: 2025-12-31
translationOf: /en/topics/nip-04.md
translationDate: 2026-04-22
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-04は、kind 4イベントとECDH由来のshared secretを使った暗号化direct messagesを定義します。これはNostr最初のDM方式でしたが、今ではlegacy technologyであり、新しいプライベートメッセージングの作業はNIP-17へ移っています。

## 仕組み

メッセージは、次の基本フローを持つkind 4イベントを使います。

1. 送信者はsecp256k1 ECDHでshared secretを導出する
2. plaintextをAES-256-CBCで暗号化する
3. イベントは受信者を示す`p`タグを含む
4. ciphertextはbase64でエンコードされ、IVとともに`content`へ保存される

イベント自体は通常の署名付きNostrイベントのままなので、relayはplaintextを読めなくても外側のmetadataを見ることができます。

## セキュリティとプライバシーの限界

NIP-04には大きなプライバシー上の欠点があります。

- **Metadata leakage** - 送信者のpubkeyが各メッセージで公開される
- **No sender privacy** - 誰が誰へ送っているかが見える
- **Exact timestamps** - メッセージ時刻がランダム化されない
- **Non-standard key handling** - ECDH点のX座標だけを使うため、library間での正しさ確保が難しく、プロトコル進化の余地も小さい

仕様は明示的に、これが「暗号化通信の最先端にはまったく近づいていない」と警告しています。

## なぜ置き換えられたか

NIP-04はメッセージ内容を暗号化しますが、social graphは隠しません。relay operatorは、誰がイベントを送ったか、誰が受け取るか、いつ公開されたかを依然として見られます。payloadを復号しなくても、これだけのmetadataで会話の地図を描けます。

NIP-17は、NIP-44のpayload encryptionとNIP-59のgift wrappingを組み合わせることでこれに対処し、relayや受動的な観測者から送信者を隠します。新しい実装では、NIP-04は互換性維持専用として扱うべきです。

## 実装状況

legacy clientやsignerは、古い会話と旧appがまだ流通しているため、今でもNIP-04のencrypt/decrypt methodを提供しています。この互換レイヤーは移行のために重要ですが、新機能をkind 4イベントの上に構築すると、古いプライバシー上の制約をそのまま引きずることになります。

---

**Primary sources:**
- [NIP-04 Specification](https://github.com/nostr-protocol/nips/blob/master/04.md)

**Mentioned in:**
- [Newsletter #4: NIP Deep Dive](/ja/newsletters/2026-01-07-newsletter/)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #19: nostter NIP-44 migration](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-44: Encrypted Payloads](/ja/topics/nip-44/)
- [NIP-17: Private Direct Messages](/ja/topics/nip-17/)
- [NIP-59: Gift Wrap](/ja/topics/nip-59/)
