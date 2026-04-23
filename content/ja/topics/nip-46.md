---
title: "NIP-46: Nostr Connect"
date: 2025-12-17
translationOf: /en/topics/nip-46.md
translationDate: 2026-04-22
draft: false
categories:
  - Signing
  - Protocol
---

NIP-46は、Nostr relays越しのremote signingを定義します。clientは、一般にbunkerと呼ばれる別のsignerと通信するため、署名鍵をユーザーが今使っているappの外側へ置いておけます。

## 仕組み

1. clientは、bunker session専用のローカルkeypairを生成します。
2. 接続は`bunker://`または`nostrconnect://` URIで確立されます。
3. clientとsignerは、relay上で暗号化されたkind `24133`のrequestとresponse eventを交換します。
4. 接続後、clientは`get_public_key`を呼んで、実際に署名対象となるユーザーpubkeyを取得します。

## 接続方法

- **bunker://** - signer主導の接続
- **nostrconnect://** - QR codeまたはdeep linkによるclient主導の接続

`nostrconnect://`のflowには、共有secretが必須です。これによりclientは、最初のresponseが本当に意図したsignerから来たものかを検証でき、単純な接続spoofingを防げます。

## 対応操作

- `sign_event` - 任意のイベントへ署名する
- `get_public_key` - signerからユーザーpubkeyを取得する
- `nip04_encrypt/decrypt` - NIP-04暗号化操作
- `nip44_encrypt/decrypt` - NIP-44暗号化操作
- `switch_relays` - 更新されたrelay setをsignerへ求める

多くの実装は、セットアップ時に`sign_event:1`や`nip44_encrypt`のようなpermission stringも使い、全面的なアクセスではなく狭いscopeだけをsignerが承認できるようにしています。

## Relayと信頼モデル

NIP-46は秘密鍵をclientの外へ移しますが、signerへの信頼自体を消すわけではありません。signerはrequestを承認、拒否、遅延できますし、clientが依頼するすべての操作を見ます。relay選択も重要で、プロトコルはrequestとresponseを両者が到達できるrelay上で配信できることに依存します。

`switch_relays` methodがあるのは、signerが時間とともにsessionを別のrelay setへ移せるようにするためです。これを無視するclientは、signer側のrelay設定が変わったとき信頼性が落ちます。

---

**Primary sources:**
- [NIP-46 Specification](https://github.com/nostr-protocol/nips/blob/master/46.md)

**Mentioned in:**
- [Newsletter #1: Notable Code Changes](/ja/newsletters/2025-12-17-newsletter/)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #4: Primal Android Becomes a Full Signing Hub](/ja/newsletters/2026-01-07-newsletter/)
- [Newsletter #12: NDK Collaborative Events and NIP-46 Timeout](/ja/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: NipLock signer support](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: Forgesworn Heartwood signer](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: Flotilla Aegis NIP-46 login](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [NIP-55: Android Signer](/ja/topics/nip-55/)
