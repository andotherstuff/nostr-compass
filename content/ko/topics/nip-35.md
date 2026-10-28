---
title: "NIP-35: 토렌트"
date: 2026-10-21
translationOf: /en/topics/nip-35.md
translationDate: 2026-10-28
draft: false
categories: ["NIPs"]
---

NIP-35는 토렌트 인덱스 event를 위한 초안(draft) 단계의 선택적(optional) NIP입니다. kind 2003 event는 `x` tag에 BitTorrent v1 infohash를 파일 경로와 함께 담으며, 트래커를 지정할 수도 있습니다. 이 event가 담는 것은 인덱스 메타데이터이고, 파일 내용은 피어가 BitTorrent를 통해 가져옵니다. 토렌트에 대한 댓글은 kind 2004를 사용하며 NIP-10 스레딩을 따릅니다.

이 번호에는 이전 이력이 있습니다. 2024년 번호 재지정으로 해당 제안이 NIP-37로 옮겨지기 전까지는 Draft Wraps가 NIP-35를 차지하고 있었습니다. 그 변경 이전에 작성된 NIP-35 언급은 Draft Wraps를 뜻할 수 있습니다. 현재 이 번호는 Torrents에 할당되어 있습니다.

[현재 NIP-35 문서](https://github.com/nostr-protocol/nips/blob/master/35.md)가 event 형식을 정의합니다. 이전 할당 내역은 [번호 재지정 커밋](https://github.com/nostr-protocol/nips/commit/48674e563865b1cb7bb3c5c7869d20055446f408)에 기록되어 있습니다.

## 1차 자료

- [NIP-35: 토렌트](https://github.com/nostr-protocol/nips/blob/master/35.md)
- [nostr-protocol/nips 커밋 48674e5 (2024년 번호 재지정)](https://github.com/nostr-protocol/nips/commit/48674e563865b1cb7bb3c5c7869d20055446f408)

## 언급된 곳
- [뉴스레터 #46: Magnetar](/ko/newsletters/2026-10-28-newsletter/#magnetar)

- [뉴스레터 45](/en/newsletters/2026-10-21-newsletter/#short-history)
