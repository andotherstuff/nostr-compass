---
title: "NIP-59: Gift Wrap"
date: 2025-12-17
draft: false
categories:
  - Privacy
  - Protocol
---

NIP-59는 일회용 신원으로 암호화 레이어로 이벤트를 래핑하여 발신자를 숨기는 기술인 gift wrapping을 정의합니다.

## 구조

gift-wrapped 이벤트는 세 개의 레이어를 가집니다:

1. **Rumor** - 서명되지 않은 원본 이벤트 콘텐츠
2. **Seal** (kind 13) - 수신자에게 암호화된 rumor, 실제 발신자가 서명
3. **Gift Wrap** (kind 1059) - 수신자에게 암호화된 seal, 무작위 일회용 키로 서명

외부 레이어는 이 메시지를 위해서만 생성된 무작위 키 쌍을 사용하므로 관찰자가 발신자와 연결할 수 없습니다.

## 왜 세 개의 레이어인가?

- **rumor**에 실제 콘텐츠가 포함됨
- **seal**이 실제 발신자를 증명함(수신자만 볼 수 있음)
- **gift wrap**이 릴레이와 관찰자에게 발신자를 숨김

## 삭제 지원

Gift wrap 이벤트는 이제 NIP-09/NIP-62 삭제 요청을 통해 삭제할 수 있습니다. 이를 통해 사용자가 릴레이에서 래핑된 메시지를 제거할 수 있습니다.

## 사용 사례

- 비공개 다이렉트 메시지(NIP-17)
- 익명 제보 또는 내부 고발
- 발신자 프라이버시가 중요한 모든 시나리오

---

**주요 출처:**
- [NIP-59 사양](https://github.com/nostr-protocol/nips/blob/master/59.md)

**언급된 곳:**
- [뉴스레터 #1: 뉴스](/ko/newsletters/2025-12-17-newsletter/#news)
- [뉴스레터 #1: NIP 업데이트](/ko/newsletters/2025-12-17-newsletter/#nip-updates)

**참고:**
- [NIP-17: 비공개 다이렉트 메시지](/ko/topics/nip-17/)

