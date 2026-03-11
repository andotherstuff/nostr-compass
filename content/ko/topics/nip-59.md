---
title: "NIP-59: Gift Wrap"
date: 2025-12-17
translationOf: /en/topics/nip-59.md
translationDate: 2026-03-11
draft: false
categories:
  - 프라이버시
  - 프로토콜
---
NIP-59는 gift wrap을 정의한다. 이벤트를 캡슐화하여 릴레이와 외부 관찰자가 수신하는 외부 이벤트에서 실제 발신자를 알 수 없게 하는 방식이다.

## 구조

Gift-wrapped 이벤트는 세 개의 계층으로 구성된다:

1. **Rumor** - 서명 없는 대상 이벤트.
2. **Seal** (kind `13`) - 수신자에게 암호화되고 실제 발신자가 서명한 rumor.
3. **Gift Wrap** (kind `1059`) - 다시 암호화되고 랜덤 일회용 키로 서명된 seal.

Seal은 빈 태그를 가져야 한다. 외부 gift wrap은 릴레이가 라우팅할 수 있도록 보통 수신자 `p` 태그를 포함한다.

## 숨기는 것

Gift wrap은 외부 이벤트가 일회용 키로 서명되기 때문에 릴레이와 네트워크 관찰자로부터 발신자를 숨긴다. 그러나 수신자는 내부 seal을 복호화하여 어떤 장기 키가 서명했는지 알 수 있다. 따라서 프라이버시 이점은 전송 계층의 메타데이터 보호이지, 수신자로부터의 익명성이 아니다.

명세는 wrapper 타임스탬프를 무작위화하고, 가능하면 인증을 요구하며 의도된 수신자에게만 wrapped 이벤트를 제공하는 릴레이를 사용할 것을 권장한다. 이러한 릴레이 동작 없이는 수신자 메타데이터가 여전히 유출될 수 있다.

## 운영 참고사항

Gift wrap은 그 자체로 메시징 프로토콜이 아니다. 비공개 메시징 시스템 같은 다른 프로토콜이 이것을 구성 요소로 사용한다.

릴레이는 wrapped 이벤트가 공개적으로 유용하지 않기 때문에 장기 저장하지 않을 수 있다. 명세는 구현이 추가 스팸 저항을 원할 때 외부 wrapper에 proof-of-work를 허용한다.

## 활용 사례

- 비공개 다이렉트 메시지 (NIP-17)
- 친구 전용 노트 (NIP-FR 제안)
- 푸시 알림 페이로드 (NIP-9a 제안)
- 네트워크로부터 발신자 프라이버시가 필요한 모든 시나리오

---

**주요 출처:**
- [NIP-59 명세](https://github.com/nostr-protocol/nips/blob/master/59.md)

**언급된 뉴스레터:**
- [Newsletter #8: NIP Deep Dive](/en/newsletters/2026-02-04-newsletter/#nip-deep-dive-nip-59-gift-wrap)
- [Newsletter #1: News](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: NIP Updates](/en/newsletters/2025-12-17-newsletter/#nip-updates)
- [Newsletter #3: December Recap](/en/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)
- [Newsletter #15: Open PRs](/en/newsletters/2026-03-04-newsletter/#open-prs-and-project-updates)

**같이 보기:**
- [NIP-17: 비공개 다이렉트 메시지](/ko/topics/nip-17/)
