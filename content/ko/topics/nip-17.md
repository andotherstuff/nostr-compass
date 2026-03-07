---
title: "NIP-17: 비공개 다이렉트 메시지"
date: 2025-12-17
translationOf: /en/topics/nip-17.md
translationDate: 2026-03-07
draft: false
categories:
  - Privacy
  - Messaging
---
NIP-17은 NIP-59 gift wrapping을 사용하여 발신자 프라이버시를 보장하는 비공개 다이렉트 메시지를 정의한다. 외부 이벤트에 발신자가 노출되는 NIP-04 DM과 달리, NIP-17은 릴레이와 일반 관찰자로부터 발신자를 숨긴다.

## 작동 방식

메시지는 여러 암호화 레이어로 감싸진다:
1. 실제 메시지 내용은 kind 14의 rumor 이벤트에 존재한다.
2. seal이 해당 내용을 수신자에게 암호화한다.
3. gift wrap이 seal을 다시 암호화하고 일회용 키쌍으로 게시한다.

외부 gift wrap은 무작위 일회용 키쌍을 사용하므로 릴레이와 관찰자가 메시지 발신자를 판별할 수 없다.

## 메시지 구조

- **Kind 14** - 래핑된 레이어 내부의 실제 DM 내용
- **Kind 1059** - 릴레이에 게시되는 외부 gift wrap 이벤트
- 래핑 흐름 내부의 페이로드에 NIP-44 암호화 사용
- 리액션 같은 인터랙티브 DM 기능을 더 잘 지원하도록 명세가 개선됨

## 보안 및 신뢰 모델

- 릴레이가 발신자를 볼 수 없음 (gift wrap의 일회용 키쌍으로 은닉)
- 수신자는 노출됨 (gift wrap의 `p` 태그)
- 메시지 타임스탬프가 일정 범위 내에서 무작위화
- 릴레이에서 보이는 스레딩이나 대화 그룹 없음

수신자는 언래핑 후 발신자를 알 수 있다. NIP-17은 네트워크로부터 발신자 신원을 숨기는 것이지, 상대방으로부터 숨기는 것이 아니다. "비공개 DM"이라 설명할 때 이 구분이 중요하다.

## 왜 중요한가

NIP-04 DM은 내용을 암호화하지만 메타데이터는 노출된다:
- 발신자 공개키가 공개됨
- 수신자 공개키가 `p` 태그에 포함됨
- 타임스탬프가 정확함

NIP-17은 더 복잡한 구현 비용을 들여 발신자를 숨긴다.

이 복잡성은 실질적 프라이버시 개선을 가져온다. 릴레이는 래핑된 메시지가 수신자에게 전달되는 것을 여전히 볼 수 있지만, kind 4 메시지처럼 외부 이벤트 메타데이터에서 발신자-수신자 그래프를 직접 구성할 수는 없다.

## 상호운용성 참고사항

NIP-17은 비공개 메시징을 위한 inbox 릴레이 목록도 정의한다. 클라이언트는 kind 10050 이벤트를 게시하여 발신자가 DM 전달에 어떤 릴레이를 사용해야 하는지 알려줄 수 있다. DM 릴레이 라우팅을 공개 콘텐츠 라우팅과 분리하면, 비공개 트래픽이 잘못된 곳에 게시되는 것을 방지할 수 있다.

---

**주요 출처:**
- [NIP-17 명세](https://github.com/nostr-protocol/nips/blob/master/17.md)
- [PR #2098](https://github.com/nostr-protocol/nips/pull/2098) - 문구 정리 및 리액션 지원 업데이트

**언급된 뉴스레터:**
- [뉴스레터 #1: NIP 업데이트](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [뉴스레터 #2: 뉴스](/en/newsletters/2025-12-24-newsletter/#news)
- [뉴스레터 #3: 12월 회고](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [뉴스레터 #3: 주목할 코드 변경](/en/newsletters/2025-12-31-newsletter/#shopstr-marketplace)
- [뉴스레터 #5: 뉴스](/en/newsletters/2026-01-13-newsletter/#news)

**같이 보기:**
- [NIP-04: 암호화 다이렉트 메시지 (지원 중단)](/ko/topics/nip-04/)
- [NIP-44: 암호화 페이로드](/ko/topics/nip-44/)
- [NIP-59: Gift Wrap](/ko/topics/nip-59/)
