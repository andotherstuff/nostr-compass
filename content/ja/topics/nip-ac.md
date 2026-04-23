---
title: "NIP-AC: P2P Voice and Video Calls"
date: 2026-04-08
translationOf: /en/topics/nip-ac.md
translationDate: 2026-04-22
draft: false
categories:
  - Protocol
  - Calling
---

NIP-ACは、Nostr上でpeer-to-peerの音声通話とビデオ通話を行うためのプロトコルを提案します。この仕様は、通話シグナリング（offer、answer、ICE candidates）にNostr eventsを使い、実際のmedia transportにはWebRTCを使います。これにより、通話のセットアップは分散型のまま維持しつつ、音声と映像には標準的なブラウザAPIを使えます。

## 仕組み

発信側は、calleeのpubkeyをタグ付けしたWebRTC Session Description Protocol（SDP）offerを含むcall offer eventを公開します。受信側はSDP answer eventで応答します。両者はICE candidate eventsを交換して通信経路を交渉します。WebRTC接続が確立すると、mediaはrelayを介さずpeer間で直接流れます。

シグナリングイベントは暗号化されるため、relayは誰が誰へ通話しているかを観測できません。call state machineはoffer、answer、reject、busy、hangupの遷移を扱います。

## Implementations

- [Amethyst](https://github.com/vitorpamplona/amethyst)は、call state machine test suiteとstale call offer処理を含むNIP-AC対応を進めています。

---

**Primary sources:**
- [NIP-AC PR #2301](https://github.com/nostr-protocol/nips/pull/2301) - P2P Voice and Video Calls over WebRTC

**Mentioned in:**
- [Nostr Compass #17 (2026-04-08)](/ja/newsletters/2026-04-08-newsletter/)

**See also:**
- [NIP-44（Encrypted Payloads）](/ja/topics/nip-44/)
