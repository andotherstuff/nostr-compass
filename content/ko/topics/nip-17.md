---
title: "NIP-17: 비공개 다이렉트 메시지"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Messaging
---

NIP-17은 발신자 프라이버시를 위해 NIP-59 gift wrapping을 사용하는 비공개 다이렉트 메시지를 정의합니다. 발신자를 노출하는 NIP-04 DM과 달리, NIP-17 메시지는 누가 메시지를 보냈는지 숨깁니다. 수신자는 외부 gift wrap에서 보입니다.

## 작동 방식

메시지는 여러 암호화 레이어로 래핑됩니다:
1. 실제 메시지 콘텐츠(kind 14)
2. 콘텐츠를 수신자에게 암호화하는 seal
3. 발신자의 신원을 숨기는 gift wrap

외부 gift wrap은 무작위 일회용 키 쌍을 사용하므로 릴레이와 관찰자가 누가 메시지를 보냈는지 판단할 수 없습니다.

## 메시지 구조

- **Kind 14** - 실제 DM 콘텐츠(seal 내부)
- 콘텐츠에 NIP-44 암호화 사용
- DM 대화 내에서 리액션(kind 7) 지원

## 프라이버시 보장

- 릴레이는 발신자를 볼 수 없음(gift wrap의 일회용 키 쌍으로 숨겨짐)
- 수신자는 보임(gift wrap의 `p` 태그에서)
- 메시지 타임스탬프가 일정 범위 내에서 무작위화됨
- 릴레이에서 보이는 스레딩이나 대화 그룹화 없음

## NIP-04와 비교

NIP-04 DM은 콘텐츠를 암호화하지만 메타데이터는 보입니다:
- 발신자 pubkey가 공개됨
- 수신자 pubkey가 `p` 태그에 있음
- 타임스탬프가 정확함

NIP-17은 더 복잡한 구현 비용으로 발신자를 숨깁니다.

---

**주요 출처:**
- [NIP-17 사양](https://github.com/nostr-protocol/nips/blob/master/17.md)

**언급된 곳:**
- [뉴스레터 #1: NIP 업데이트](/ko/newsletters/2025-12-17-newsletter/#nip-updates)
- [뉴스레터 #2: 뉴스](/ko/newsletters/2025-12-24-newsletter/#news)

**참고:**
- [NIP-59: Gift Wrap](/ko/topics/nip-59/)

