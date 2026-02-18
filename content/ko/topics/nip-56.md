---
title: "NIP-56: 신고"
date: 2026-02-18
translationOf: /en/topics/nip-56.md
translationDate: 2026-02-18
draft: false
categories:
  - Moderation
  - Protocol
---

NIP-56은 kind 1984 event를 사용하는 신고 메커니즘을 정의하여, 사용자와 애플리케이션이 Nostr 네트워크 전반에서 문제가 있는 콘텐츠를 신고할 수 있게 합니다.

## 작동 방식

사용자가 신고 대상 pubkey를 참조하는 `p` tag와 함께 kind 1984 event를 게시합니다. 특정 노트를 신고할 때는 `e` tag가 노트 ID를 참조합니다. 두 tag 모두 위반 카테고리를 지정하는 세 번째 파라미터를 받습니다.

## 신고 카테고리

- **nudity**: 성인 콘텐츠
- **malware**: 바이러스, 트로이목마, 랜섬웨어
- **profanity**: 불쾌한 언어 및 혐오 발언
- **illegal**: 법률을 위반할 가능성이 있는 콘텐츠
- **spam**: 원하지 않는 반복 메시지
- **impersonation**: 사기성 신원 주장
- **other**: 위 카테고리에 맞지 않는 위반

## 클라이언트 및 Relay 동작

클라이언트는 팔로우한 사용자의 신고를 콘텐츠 블러링 등의 모더레이션 결정에 활용할 수 있습니다. Relay는 신고를 통한 자동 모더레이션을 피해야 합니다. 신뢰할 수 있는 모더레이터의 신고는 수동 집행에 참고할 수 있습니다. NIP-32 `l` 및 `L` tag를 통한 추가 분류가 지원됩니다.

---

**주요 출처:**
- [NIP-56 명세](https://github.com/nostr-protocol/nips/blob/master/56.md)

**언급된 곳:**
- [뉴스레터 #10: 프로젝트 업데이트](/ko/newsletters/2026-02-18-newsletter/#notedeck-android-앱-스토어-준비)

**참조:**
- [NIP-22: 댓글](/ko/topics/nip-22/)
