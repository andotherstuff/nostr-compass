---
title: "NIP-17: 비공개 다이렉트 메시지"
date: 2025-12-17
translationOf: /en/topics/nip-17.md
translationDate: 2026-04-22
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-17은 발신자 프라이버시를 위해 NIP-59 gift wrapping을 사용하는 비공개 다이렉트 메시지를 정의합니다. 바깥 이벤트에 발신자가 노출되는 NIP-04 DM과 달리, NIP-17은 릴레이와 일반 관찰자로부터 발신자를 숨깁니다.

## 작동 방식

메시지는 여러 암호화 계층으로 감싸집니다:
1. 실제 메시지 내용은 kind 14의 rumor 이벤트 안에 있습니다.
2. seal이 그 내용을 수신자용으로 암호화합니다.
3. gift wrap이 seal을 한 번 더 암호화하고 일회용 키페어에서 게시합니다.

바깥쪽 gift wrap은 무작위 일회용 키페어를 사용하므로 릴레이와 관찰자는 누가 메시지를 보냈는지 판단할 수 없습니다.

## 메시지 구조

- **Kind 14** - 감싸진 레이어 안의 실제 DM 내용
- **Kind 1059** - 릴레이에 게시되는 바깥 gift wrap 이벤트
- 래핑 흐름 내부 payload에는 NIP-44 암호화를 사용함
- 명세는 reaction 같은 상호작용 DM 기능을 더 잘 지원하도록 다듬어졌음

## 보안과 신뢰 모델

- 릴레이는 발신자를 볼 수 없음 (gift wrap의 일회용 키페어가 숨겨 줌)
- 수신자는 보임 (gift wrap의 `p` 태그에 있음)
- 메시지 타임스탬프는 일정 범위 안에서 무작위화됨
- 릴레이에는 스레딩이나 대화 그룹이 보이지 않음

수신자는 메시지를 언랩한 뒤에는 누가 보냈는지 알게 됩니다. NIP-17은 네트워크로부터 발신자 신원을 숨기는 것이지, 상대방으로부터 숨기는 것은 아닙니다. 사람들이 이를 "비공개 DM"이라고 부를 때 이 구분은 중요합니다.

## 왜 중요한가

NIP-04 DM은 내용을 암호화하지만 메타데이터는 그대로 드러납니다:
- 발신자 pubkey는 공개됨
- 수신자 pubkey는 `p` 태그에 있음
- 타임스탬프는 정확함

NIP-17은 더 복잡한 구현을 치르는 대신 발신자를 숨깁니다.

이 복잡성은 실제 프라이버시 개선을 가져옵니다. 릴레이는 여전히 래핑된 메시지가 어떤 수신자 앞으로 향하는지는 볼 수 있지만, kind 4 메시지처럼 바깥 이벤트 메타데이터만으로 발신자-수신자 그래프를 직접 만들 수는 없습니다.

## 상호운용성 참고사항

NIP-17은 비공개 메시징용 inbox relay 목록도 정의합니다. 클라이언트는 kind 10050 이벤트를 게시해 발신자가 DM 전달에 어떤 릴레이를 겨냥해야 하는지 알릴 수 있습니다. DM 릴레이 라우팅을 공개 콘텐츠 라우팅과 분리해 두면, 비공개 트래픽이 잘못된 곳에 게시되는 일을 피하는 데 도움이 됩니다.

---

**주요 출처:**
- [NIP-17 Specification](https://github.com/nostr-protocol/nips/blob/master/17.md)
- [PR #2098](https://github.com/nostr-protocol/nips/pull/2098) - 문구 정리와 reaction 지원 업데이트

**언급된 뉴스레터:**
- [Newsletter #1: NIP Updates](/ko/newsletters/2025-12-17-newsletter/)
- [Newsletter #2: News](/ko/newsletters/2025-12-24-newsletter/)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #3: Notable Code Changes](/en/newsletters/2025-12-31-newsletter/)
- [Newsletter #5: News](/ko/newsletters/2026-01-13-newsletter/)
- [Newsletter #13: Vector](/en/newsletters/2026-03-11-newsletter/)
- [Newsletter #19: NipLock password manager](/en/newsletters/2026-04-22-newsletter/)

**같이 보기:**
- [NIP-04: 암호화된 다이렉트 메시지 (지원 중단)](/ko/topics/nip-04/)
- [NIP-44: 암호화된 페이로드](/ko/topics/nip-44/)
- [NIP-59: Gift Wrap](/ko/topics/nip-59/)
