---
title: "NIP-46: Nostr Connect"
date: 2025-12-17
translationOf: /en/topics/nip-46.md
translationDate: 2026-03-07
draft: false
categories:
  - Signing
  - Protocol
---

NIP-46は、Nostr relay越しのremote signingを定義します。clientは、bunkerと呼ばれる別のsignerに処理を依頼できるため、signing keyをいま使っているappの外に置けます。

## 仕組み

1. clientは、bunker session専用のlocal keypairを生成します。
2. 接続は`bunker://`または`nostrconnect://` URIで開始します。
3. clientとsignerは、relay上で暗号化されたkind `24133` request/response eventをやり取りします。
4. 接続後、clientは`get_public_key`を呼び出して、実際に署名対象となるuser pubkeyを取得します。

## 接続方法

- **bunker://** - signer主導の接続
- **nostrconnect://** - QR codeやdeep link経由でclientが始める接続

`nostrconnect://` flowにはshared secretが必須です。これによりclientは、最初のresponseが意図したsignerから来たものかを検証でき、単純なconnection spoofingを防げます。

## サポートされる操作

- `sign_event` - 任意のeventに署名
- `get_public_key` - signerからuserのpubkeyを取得
- `nip04_encrypt/decrypt` - NIP-04暗号化操作
- `nip44_encrypt/decrypt` - NIP-44暗号化操作
- `switch_relays` - signerに更新済みrelay setを要求

多くの実装では、setup時に`sign_event:1`や`nip44_encrypt`のようなpermission stringも使います。signerは、全面的なaccessではなく、狭いscopeだけを承認できます。

## Relayと信頼モデル

NIP-46はprivate keyをclientの外へ移しますが、signerへの信頼そのものは消しません。signerはrequestを承認、拒否、遅延でき、clientが求めたすべての操作を見られます。relay選択も重要で、protocolは両者が到達できるrelay上でrequestとresponseが届くことに依存します。

`switch_relays` methodは、signerが時間とともにsessionを別のrelay setへ移せるようにするためのものです。これを無視するclientは、signerのrelay設定が変わったときに信頼性が落ちます。

---

**主要ソース:**
- [NIP-46 Specification](https://github.com/nostr-protocol/nips/blob/master/46.md)

**言及箇所:**
- [Newsletter #1: Notable Code Changes](/en/newsletters/2025-12-17-newsletter/#amethyst-android)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #7: Primal Android Becomes a Full Signing Hub](/en/newsletters/2026-01-07-newsletter/#primal-android-becomes-a-full-signing-hub)
- [Newsletter #15: NDK Collaborative Events and NIP-46 Timeout](/en/newsletters/2026-03-04-newsletter/#ndk-collaborative-events-and-nip-46-timeout)

**関連項目:**
- [NIP-55: Android Signer](/ja/topics/nip-55/)
