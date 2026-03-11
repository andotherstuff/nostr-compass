---
title: "NIP-07: ブラウザ拡張署名者"
date: 2026-01-28
translationOf: /en/topics/nip-07.md
translationDate: 2026-03-11
draft: false
categories:
  - NIP
  - 署名
  - セキュリティ
---
NIP-07は、browser extensionがweb-based Nostr clientへ署名機能を提供するための標準interfaceを定義します。private keyをwebsiteへ露出させず、extension内に閉じ込めておくための仕組みです。

## 仕組み

browser extensionは、web appが使える`window.nostr` objectをinjectします。

```javascript
// Get public key
const pubkey = await window.nostr.getPublicKey();

// Sign an event
const signedEvent = await window.nostr.signEvent(unsignedEvent);

// Encrypt (NIP-04, legacy)
const ciphertext = await window.nostr.nip04.encrypt(pubkey, plaintext);

// Decrypt (NIP-04, legacy)
const plaintext = await window.nostr.nip04.decrypt(pubkey, ciphertext);

// NIP-44 methods (modern, if supported)
// const ciphertext = await window.nostr.nip44.encrypt(pubkey, plaintext);
// const plaintext = await window.nostr.nip44.decrypt(pubkey, ciphertext);
```

## Security Model

- **Key Isolation**: private keyはextensionの外へ出ない
- **User Approval**: extensionは署名requestごとに承認を求められる
- **Domain Control**: どのsiteがsignatureを要求できるかをextensionが制限できる

NIP-07はkey custodyを改善しますが、extension自体への信頼を消すわけではありません。悪意あるextensionや侵害されたextensionは、誤った内容に署名したり、metadataを漏らしたり、権限を広く与えすぎたりできます。

## 相互運用メモ

NIP-07で一番難しいのはAPI shapeではありません。capabilityのばらつきです。`getPublicKey()`と`signEvent()`だけを実装するextensionもあれば、`nip04`、`nip44`、さらに新しい任意methodまで公開するものもあります。web appは、すべてのinjectされたsignerが同じように振る舞うと決めつけず、feature detectionと妥当なfallbackを用意する必要があります。

user approvalのUX差も挙動に影響します。裏で静かにaccessできる前提のsiteは、あるextensionでは動いても、毎回確認を求める別のextensionでは壊れて見えることがあります。良いNIP-07 appは、署名を対話的なpermission boundaryとして扱います。

## Implementation Status

代表的なNIP-07 extensionには次のものがあります。
- **Alby** - Nostr signingを備えたLightning wallet
- **nos2x** - 軽量なNostr signer
- **Flamingo** - 多機能なNostr extension

## Limitations

- Browser-only（mobile supportなし）
- Extensionのインストールが必要
- 承認UXはextensionごとに異なる

cross-deviceまたはmobileの署名では、通常はNIP-46とNIP-55の方が適しています。

---

**主要ソース:**
- [NIP-07 Specification](https://github.com/nostr-protocol/nips/blob/master/07.md)
- [PR #2233](https://github.com/nostr-protocol/nips/pull/2233) - `peekPublicKey()` proposal

**言及箇所:**
- [Newsletter #7: NIP Updates](/ja/newsletters/2026-01-28-newsletter/#nip-updates)
- [Newsletter #8: News](/ja/newsletters/2026-02-04-newsletter/#news)
- [Newsletter #11: News](/ja/newsletters/2026-02-25-newsletter/#news)

**関連項目:**
- [NIP-04: 暗号化ダイレクトメッセージ（非推奨）](/ja/topics/nip-04/)
- [NIP-44: Encrypted Payloads](/ja/topics/nip-44/)
- [NIP-46: Nostr Connect](/ja/topics/nip-46/)
- [NIP-55: Android Signer Applications](/ja/topics/nip-55/)
