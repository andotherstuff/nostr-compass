---
title: "Concord Protocol"
date: 2026-07-15
translationOf: /en/topics/concord-protocol.md
translationDate: 2026-07-15
draft: false
categories:
  - Protocol
  - Messaging
---

Concordは、Nostr上のend-to-end encryptedなコミュニティとチャンネル向けの、MITライセンスのオープンなプロトコルで、[CORD-01からCORD-07までの仕様](https://github.com/concord-protocol/concord)で定義されています。[Vector](https://github.com/VectorPrivacy/Vector)はv0.4.0以降、Group Chats機能のデフォルトのtransportとしてこれを採用し、自身のリリースノートでは「独自のメッセージングプロトコル」と呼んでいますが、仕様そのものはVectorとは別に公開されており、すでに独立した実装が存在します。

## 仕組み

Concordは、Discord風のコミュニティサーバーが通常担う機能を、誰も信頼する必要のない部品へと分割します。relayは常に、rotateするラベル宛てに暗号化されたblobのみを保持し、部屋の鍵を保持していることがメンバーである証となり、role、kick、banに対する権限は、owner のidentityに根ざした署名済みrosterで、これを各clientがサーバーに強制を委ねる代わりにローカルで検証します。永続的なeventはすべて、同じ3層のenvelopeに乗ります。planeそれ自身の導出したstream keyで署名されたkind 1059のwrapが、authorの本物の鍵で署名されたsealを含み、そのsealが機能的なeventを運ぶ署名なしのrumorを含みます。chat messageのrumorは、素のkind 9 eventです。

```json
{
  "kind": 9,
  "pubkey": "<author>",
  "content": "Hey chat!",
  "tags": [
    ["channel", "<channel_id>"],
    ["epoch", "0"]
  ]
}
```

control、chat、guestbookの各トラフィックは、それぞれ独自の[NIP-59](/ja/topics/nip-59/) gift-wrappedなplaneを得るため、3種すべてを保持するrelayでも、部屋の鍵なしにはcontrol messageとchat messageとguestbook entryを区別できません。仕様は7つのCORDドキュメントに分かれています。private stream(01)、communityとmembership(02)、channel(03)、role(04)、invite(05)、削除されたメンバーを締め出すためのrekeyingと再創設(06)、そしてblind token brokerを介したaudio/video(07)です。membershipそのものにはサーバー側のリストがありません。planeを復号できる者がメンバーであり、誰かを本当に削除するとは、テーブルから行を削除するのではなく、communityを新しいkey epochへ巻き上げ、残った者だけに鍵を渡すことを意味します。

## Marmotとの違い

Concordと[Marmot](/ja/topics/marmot/)は、異なるグループの形に対して異なる暗号技術で、Nostr上の暗号化グループメッセージングを解きます。Concordプロジェクト自身の比較は、この分担を明示しています。Marmotは、forward secrecyとpost-compromise securityのためにNostrの上に[MLS](/ja/topics/mls/)を重ね、per-device key packageと、グループ全体を足並みそろえて進める順序付きのcommitを使います。これは強い保証を得ますが、そのコストはmembershipの変更とともに増大するため、参加や離脱がまれな、小規模で高リスクなグループに適しています。Concordは代わりに、すべてのメンバーに同じ部屋の鍵を与え、commitごとにratchetする代わりに削除時に部屋全体をre-keyし、MLSの暗号的保証の一部を手放す代わりに、communityが数百から数千の、カジュアルで入れ替わりの激しいメンバーへと成長してもコストが安いままのモデルを取ります。これはDiscord風のcommunityが実際に取る形です。

## なぜVectorは切り替えたのか

Vector自身の[v0.4.0リリースノート](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0)は、Group Chats向けのConcordを「独自のメッセージングプロトコル」とだけ説明し、理由を直接述べていません。それでも、Concord自身の公開された論拠との整合性は明確です。VectorのようなclientにおけるGroup Chatsは、Marmotのper-device MLS stateがより高コストな経路となる、まさに大規模で開かれた、membershipが頻繁に変わるケースであり、Concordの非同期でいつでも畳み込める設計は、そのケースのために作られています。[Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0)はGroup ChatsでMarmotを退け、Concordを採用し、既存のMarmotグループ履歴はこの切り替えで引き継がれませんでした。[v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1)は4日後に、プライバシーと安定性の改善を伴う「Concord v2」を出荷しました。同じ週のうちに、[Amethystは独自のclean-roomでwire互換なConcord実装をマージし](https://github.com/vitorpamplona/amethyst/pull/3566)、SoapboxのDiscord風client [Armada](https://gitlab.com/soapbox-pub/armada)はすでに、reference実装として同じ仕様の上にCommunities機能を築いています。3つの独立したclientが数日のうちに1つのオープンな仕様へ収束することは、実際のcross-client interopへの速い経路であり、残りのNostrのグループチャットclientがどれだけMarmotに留まるかと照らして追う価値があります。

## 実装

- [Vector](https://github.com/VectorPrivacy/Vector) - single-binaryでprivacy-firstなNostrメッセンジャー。Concordを最初に出荷したclientで、v0.4.0にて
- [Armada](https://gitlab.com/soapbox-pub/armada)(Soapbox) - Discord風のcommunity client。reference実装で、backendは別の`armada-relay`リポジトリに
- [Amethyst](https://github.com/vitorpamplona/amethyst) - 機能豊富なAndroidおよびマルチプラットフォームのNostr client。Armadaとwire互換なclean-room再実装([PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566))

---

**Primary sources:**
- [Concord protocol specs (CORD-01 to CORD-07)](https://github.com/concord-protocol/concord)
- [Vector v0.4.0 release notes](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0)
- [Vector v0.4.1 release notes](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1)
- [Amethyst PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566)

**Mentioned in:**
- [Newsletter #31: Vector v0.4.0 moves Group Chats from Marmot to Concord, and Amethyst ships its own Concord client days later](/ja/newsletters/2026-07-15-newsletter/#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later)
- [Newsletter #31: Amethyst ships a clean-room Concord implementation for end-to-end encrypted communities](/ja/newsletters/2026-07-15-newsletter/#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities)

**See also:**
- [Marmot Protocol](/ja/topics/marmot/)
- [MLS (Message Layer Security)](/ja/topics/mls/)
- [NIP-46: Nostr Connect](/ja/topics/nip-46/)
