---
title: "NIP-5D: Nostr Web Applets"
date: 2026-04-08
translationOf: /en/topics/nip-5d.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Applications
---

NIP-5Dは、iframe内で動作するsandboxed web application（"napplets"）が、hosting application（"shell"）と通信するための`postMessage`プロトコルを定義します。これは[NIP-5A](/ja/topics/nip-5a/)（Static Websites）をruntime通信層で拡張し、ユーザーの秘密鍵を露出させずにweb appへNostr機能へのアクセスを与えます。

## 仕組み

shell applicationは、sandboxed iframe内にnappletを読み込みます。nappletは、ブラウザの`postMessage` APIを使い、構造化されたmessage protocolを通じてshellと通信します。shellは、このmessage channelを通してnappletへNostr signing、relay access、user contextを提供します。iframe sandboxはnappletがユーザーの秘密鍵へ直接アクセスするのを防ぐため、shellがすべてのNostr操作のgatekeeperになります。

## ユースケース

- **Interactive Nostr apps**: ユーザーにnsecの貼り付けを求めず、Nostr eventsの読み書きを行うアプリを作る
- **App marketplace**: Nostr eventsを通じて対話的web applicationsを配布する
- **Sandboxed extensions**: third-party nappletsを通じてNostr clientへ機能を追加する

---

**Primary sources:**
- [NIP-5D PR #2303](https://github.com/nostr-protocol/nips/pull/2303) - Nostr Web Applets proposal

**Mentioned in:**
- [Newsletter #17](/en/newsletters/2026-04-08-newsletter/)

**See also:**
- [NIP-5A（Static Websites）](/ja/topics/nip-5a/)
- [NIP-5C（Scrolls）](/ja/topics/nip-5c/)
