---
title: "NIP-04: 暗号化ダイレクトメッセージ（非推奨）"
date: 2025-12-31
translationOf: /en/topics/nip-04.md
translationDate: 2026-03-07
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-04は、kind 4 eventとECDH由来のshared secretを使う暗号化ダイレクトメッセージを定義します。これはNostr最初のDM方式でしたが、いまはlegacy technologyであり、新しいprivate messagingの作業はNIP-17へ移っています。

## 仕組み

メッセージはkind 4 eventを使い、基本の流れは次のとおりです。

1. 送信者がsecp256k1 ECDHでshared secretを導出する。
2. plaintextをAES-256-CBCで暗号化する。
3. eventに受信者を示す`p` tagを入れる。
4. ciphertextをbase64でencodeし、IVと一緒に`content`へ格納する。

event自体は通常の署名済みNostr eventのままなので、relayはplaintextを読めなくても外側のmetadataは見えます。

## Security and Privacy Limits

NIP-04には大きなprivacy上の弱点があります。

- **Metadata leakage** - 送信者のpubkeyがすべてのメッセージで公開される
- **No sender privacy** - 誰が誰にメッセージを送っているかが見える
- **Exact timestamps** - メッセージ時刻がランダム化されない
- **Non-standard key handling** - この方式はECDH pointのX coordinateだけを使うため、library間で正しく実装し続けるのが難しく、protocol evolutionの余地も小さい

仕様自体も、これは"does not go anywhere near the state-of-the-art in encrypted communication"だと明記しています。

## なぜ置き換えられたか

NIP-04はメッセージ内容は暗号化しますが、social graphは隠しません。relay operatorは、誰がeventを送ったか、誰が受け取るか、いつ公開されたかを見られます。payloadを復号しなくても、これだけで会話の構造を把握できます。

NIP-17は、NIP-44のpayload encryptionとNIP-59のgift wrappingを組み合わせることで、relayや無関係な観測者から送信者を隠します。新しい実装では、NIP-04は互換性維持専用として扱うべきです。

## Implementation Status

古い会話と旧世代appがまだ流通しているため、legacy clientやsignerの多くは今でもNIP-04のencrypt/decrypt methodを公開しています。この互換層は移行のために必要ですが、新機能をkind 4 eventの上に作ると、古いprivacy制約をそのまま引きずることになります。

---

**主要ソース:**
- [NIP-04 Specification](https://github.com/nostr-protocol/nips/blob/master/04.md)

**言及箇所:**
- [Newsletter #4: NIP Deep Dive](/en/newsletters/2026-01-07-newsletter/#nip-04-encrypted-direct-messages-legacy)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**関連項目:**
- [NIP-44: Encrypted Payloads](/ja/topics/nip-44/)
- [NIP-17: Private Direct Messages](/ja/topics/nip-17/)
- [NIP-59: Gift Wrap](/ja/topics/nip-59/)
