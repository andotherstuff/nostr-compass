---
title: "Marmot Protocol"
date: 2025-12-17
translationOf: /en/topics/marmot.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---

Marmotは、Nostr上のend-to-end encrypted group messaging向けプロトコルです。Nostrのidentityとrelay networkに、group key management、forward secrecy、post-compromise securityのためのMLSを組み合わせます。

## 仕組み

Marmotは、identity、relay transport、event distributionにはNostrを使い、その上にgroup membership変更とmessage encryptionのためにMLSを重ねます。1対1メッセージングに焦点を当てる[NIP-17](/ja/topics/nip-17/)とは異なり、Marmotは、メンバーが参加、離脱、鍵rotationを時間とともに行うgroup向けに作られています。

## なぜ重要か

MLSにより、MarmotはNostrのdirect-message方式だけでは得られない性質を持ちます。group state evolution、member removal semantics、後続のkey updateによるcompromise後の回復です。

この役割分担が重要です。Nostrは、開かれたnetworkにおけるidentityとtransportを解きます。MLSは認証済みgroup key agreementを解きます。Marmotはその両者をつなぐglue layerです。

## 実装状況

プロトコルはまだexperimentalですが、すでに複数実装と実運用アプリを持っています。[MDK](https://github.com/marmot-protocol/mdk)が主要なRust reference stackで、[marmot-ts](https://github.com/marmot-protocol/marmot-ts)がそのモデルをTypeScriptへ持ち込み、[White Noise](https://github.com/marmot-protocol/whitenoise)、[Amethyst](https://github.com/vitorpamplona/amethyst)、Pika、VectorなどのアプリがMarmot互換コンポーネントを使っています。

最近の作業はhardeningとinteropに集中しています。audit起点のfixが2026年初頭に入り、MIP-03はrelay間で並行するgroup state変更が競合したときにclientが収束できるよう、deterministicなcommit resolutionを導入しました。

2026年4月には、Amethystが埋め込みMDKをMIP-01とMIP-05のwire formatへ合わせました。[PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462)はTLS風length prefixのVarInt encodingとMDK test vectorとのround-trip validationを追加し、[PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435)はMIP-00 KeyPackage Relay List supportを追加し、[PR #2436](https://github.com/vitorpamplona/amethyst/pull/2436)はWhite Noiseとのcross-client testingで見つかったadmin-gateとmedia-handlingの残りの差分を閉じました。[PR #2466](https://github.com/vitorpamplona/amethyst/pull/2466)は暗号化welcome bytesがmdk-core出力と一致するようMLS commit framingを修正し、[PR #2471](https://github.com/vitorpamplona/amethyst/pull/2471)はco-admin間でstate divergenceを引き起こしていたouter-layer復号bugを修正しました。続く[PR #2493](https://github.com/vitorpamplona/amethyst/pull/2493)は包括的なMLS commit cryptography validationを追加し、[PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488)はAmethyst実装を駆動するMarmot/MLS group操作用CLIの`amy`を出荷しました。

MDKは、invitee capabilityのLCDとしてgroupの`RequiredCapabilities`を計算する[PR #261](https://github.com/marmot-protocol/mdk/pull/261)を導入し、AmethystとWhite Noise間のmixed-version inviteを可能にしました。[PR #262](https://github.com/marmot-protocol/mdk/pull/262)はcreator signerを永続化する前にinvitee key packageをparseし、[PR #264](https://github.com/marmot-protocol/mdk/pull/264)はimplementation間でSelfUpdate wire formatを収束させ、[PR #265](https://github.com/marmot-protocol/mdk/pull/265)は`group_required_proposals` accessorを公開します。

[whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)は、global singletonからaccountごとの`AccountSession` viewへの多段階refactorの最中です。[PR #743](https://github.com/marmot-protocol/whitenoise-rs/pull/743)が`AccountSession`と`AccountManager`の土台を置き、続く各phaseでrelay handle、draftとsetting、message operation、group read/write、membership、push notification、key-package read、group creation、そして[PR #770](https://github.com/marmot-protocol/whitenoise-rs/pull/770)時点ではsession-scoped event dispatchまで移行されました。[marmot-ts PR #68](https://github.com/marmot-protocol/marmot-ts/pull/68)は、TypeScript clientをaddressable kind `30443` key packageへ移行しています。

---

**Primary sources:**
- [Marmot Protocol Repository](https://github.com/marmot-protocol/marmot)
- [MLS Protocol](https://messaginglayersecurity.rocks/)
- [Marmot Development Kit (MDK)](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)
- [whitenoise-rs](https://github.com/marmot-protocol/whitenoise-rs)
- [White Noise client](https://github.com/marmot-protocol/whitenoise)
- [Amethyst PR #2462](https://github.com/vitorpamplona/amethyst/pull/2462) - MIP-01/MIP-05 wire format alignment
- [Amethyst PR #2435](https://github.com/vitorpamplona/amethyst/pull/2435) - MIP-00 KeyPackage Relay List
- [Amethyst PR #2488](https://github.com/vitorpamplona/amethyst/pull/2488) - Amy CLI

**Mentioned in:**
- [Newsletter #1: News](/ja/newsletters/2025-12-17-newsletter/)
- [Newsletter #1: Releases](/ja/newsletters/2025-12-17-newsletter/)
- [Newsletter #4](/ja/newsletters/2026-01-07-newsletter/)
- [Newsletter #7](/ja/newsletters/2026-01-28-newsletter/)
- [Newsletter #12](/ja/newsletters/2026-03-04-newsletter/)
- [Newsletter #19: Amethyst MIP compliance](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: MDK interop work](/en/newsletters/2026-04-22-newsletter/)
- [Newsletter #19: whitenoise-rs session refactor](/en/newsletters/2026-04-22-newsletter/)

**See also:**
- [MLS (Message Layer Security)](/ja/topics/mls/)
- [MIP-05: Privacy-Preserving Push Notifications](/ja/topics/mip-05/)
- [NIP-17: Private Direct Messages](/ja/topics/nip-17/)
- [NIP-59: Gift Wrap](/ja/topics/nip-59/)
