---
title: "NIP-4E: アイデンティティからの暗号化の分離"
date: 2026-07-15
translationOf: /en/topics/nip-4e.md
translationDate: 2026-07-15
draft: false
categories:
  - NIP
  - Protocol
  - Encryption
---

NIP-4Eは、fiatjafによって提案されたオープンなdraftで、すべてのデバイスがそのユーザーのメインのNostr identity keyを保持することなく、ユーザー自身のデバイス間でprivateなデータを共有するためのものです。マージされておらず、`draft`/`optional`な提案のままです。

## 解決しようとする問題

NIP-51 listsやNIP-60 Cashu walletsを含む多くの既存のNIPは、後で任意のデバイスで読み戻せるように、identity keyを使ってユーザーから自分自身へデータを暗号化します。これは、identity keyに直接アクセスできない場合、たとえばremote signerがFROST threshold shares、MuSig2、あるいはホストされたsecure enclaveで保護されている場合に破綻します。というのも、暗号化と復号のたびに、そのsignerへの往復が必要になるからです。また、署名鍵がremote bunkerにある場合には、オフライン暗号化が不可能になります。

## 仕組み

NIP-4Eは、per-deviceの「client key」を、ユーザーのidentity keyではない共有の「encryption key」から分離します。

1. ユーザーが最初にセットアップするclientが、ランダムなencryption keypairを生成し、その公開側をユーザーのidentity keyで署名した`kind:10044` eventで告知します。
2. そのユーザー向けにデータを暗号化または復号したい他のclientは、identity keyではなく、告知されたencryption keyに対してDiffie-Hellman shared secretを計算します。
3. 2台目のデバイスが新しいclientをインストールすると、そのclientは独自のローカルな「client key」を生成し、最初のclientにencryption keyの共有を求める`kind:4454`告知(これもユーザーのidentity keyで署名)を発行します。
4. 元のclientが新しい`kind:4454`告知を検知し、[NIP-44](/ja/topics/nip-44/)を使って共有encryption keyを新しいclientの鍵宛てに暗号化し、それを発行することで、新しいclientはそれ以降それを復号して使えます。

その結果、clientが共有encryption keyをローカルに保持している限り、暗号化と復号がidentity-key signerに問い合わせる必要が一切なくなり、identityにはremote-signerのセットアップ(FROST、MuSig2、ホストされたenclave)を使いつつ、通常の暗号化は高速のままオフラインでも動作します。

## なぜ重要か

NIP-4Eは、暗号化/復号呼び出しのたびにremote signerに依存することなく、drive全体またはaccount全体のsymmetric keyを必要とする他の提案の基礎として引用されています。private encrypted drive提案([PR #2412](https://github.com/nostr-protocol/nips/pull/2412))や、同じアイデアのより狭いNIP-17固有版([PR #2361](https://github.com/nostr-protocol/nips/pull/2361))などです。どちらもNIP-4E自体と並んでオープンなままで、これを完成した部品ではなく、プロトコルのアクティブで未確定な領域にしています。

---

**Primary sources:**
- [NIP-4E draft, PR #1647](https://github.com/nostr-protocol/nips/pull/1647)

**Mentioned in:**
- [Newsletter #31: Open: private encrypted drive extends NIP-4E](/ja/newsletters/2026-07-15-newsletter/#open-private-encrypted-drive-extends-nip-4e)

**See also:**
- [NIP-44: Encrypted Payloads](/ja/topics/nip-44/)
- [NIP-17: Private Direct Messages](/ja/topics/nip-17/)
- [NIP-46: Nostr Connect](/ja/topics/nip-46/)
- [FROST](/ja/topics/frost/)
