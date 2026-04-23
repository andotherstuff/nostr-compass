---
title: "NIP-55: Android Signer Application"
date: 2025-12-17
translationOf: /en/topics/nip-55.md
translationDate: 2026-04-22
draft: false
categories:
  - Signing
  - Mobile
---

NIP-55は、Android appが別のsigner applicationに対して署名と暗号化操作を要求する方法を定義します。これはAndroid clientにとって、browser extensionやremote bunkerに代わるネイティブな選択肢になります。

## 仕組み

NIP-55は、Androidの2つの機構を使います。

- **Intents** - 明示的なユーザー承認を伴うforeground flow向け
- **Content resolvers** - ユーザーが永続的な権限を与えた後のbackground flow向け

通常の接続フローは`get_public_key`から始まります。signerはユーザーpubkeyとsigner package nameの両方を返し、clientは両方をcacheすることが期待されます。background loopの中で`get_public_key`を繰り返し呼ぶのは、仕様が明示的に警告している実装ミスです。

## 主要操作

- **get_public_key** - ユーザーpubkeyとsigner package nameを取得する
- **sign_event** - Nostrイベントへ署名する
- **nip04_encrypt/decrypt** - NIP-04メッセージを暗号化または復号する
- **nip44_encrypt/decrypt** - NIP-44メッセージを暗号化または復号する
- **decrypt_zap_event** - zap関連イベントのpayloadを復号する

## セキュリティとUXメモ

NIP-55は鍵をデバイス上に保持しますが、それでもAndroid app境界とsignerの権限制御に依存します。content resolver対応は、ユーザーがそのclientへ継続的な承認を与えた後なら、繰り返しintent promptを出すよりもはるかに滑らかなUXを実現します。

Android上のweb appにとっては、NIP-55はNIP-46より使い勝手が落ちます。browserベースのflowでは、ネイティブAndroid appのように直接background responseを受け取れないため、多くの実装はcallback URL、clipboard transfer、手動pasteへfallbackします。

---

**Primary sources:**
- [NIP-55 Specification](https://github.com/nostr-protocol/nips/blob/master/55.md)

**Mentioned in:**
- [Newsletter #1: Releases](/ja/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: News](/ja/newsletters/2025-12-24-newsletter/)
- [Newsletter #2: NIP Updates](/ja/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #4: NIP Updates](/ja/newsletters/2026-01-07-newsletter/)
- [Newsletter #11: NIP Deep Dive](/ja/newsletters/2026-02-25-newsletter/)
- [Newsletter #13: Samizdat v1.0.0-alpha](/en/newsletters/2026-03-11-newsletter/)

**See also:**
- [NIP-46: Nostr Connect](/ja/topics/nip-46/)
