---
title: "Marmot Protocol"
date: 2025-12-17
translationOf: /en/topics/marmot.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Privacy
  - Messaging
---
Marmot은 Nostr 위에서 종단 간 암호화 그룹 메시징을 구현하는 프로토콜이다. Nostr의 신원 및 릴레이 네트워크와 MLS를 결합하여 그룹 키 관리, 전방 비밀성(forward secrecy), 침해 후 보안(post-compromise security)을 제공한다.

## 작동 방식

Marmot은 신원, 릴레이 전송, 이벤트 배포에 Nostr를 사용하고, 그 위에 MLS를 계층화하여 그룹 구성원 변경과 메시지 암호화를 처리한다. 일대일 메시징에 초점을 맞춘 [NIP-17](/ko/topics/nip-17/)과 달리, Marmot은 구성원이 시간이 지남에 따라 참여, 탈퇴, 키 교체를 하는 그룹을 위해 설계되었다.

## 왜 중요한가

MLS는 Nostr의 직접 메시지 방식만으로는 자체적으로 제공하지 않는 속성을 Marmot에 부여한다: 그룹 상태 발전, 구성원 제거 의미론, 이후 키 업데이트를 통한 침해 후 복구.

이 역할 분담이 핵심 통찰이다. Nostr는 개방형 네트워크에서 신원과 전송을 해결한다. MLS는 인증된 그룹 키 합의를 해결한다. Marmot은 둘 사이를 연결하는 접착 계층이다.

## 구현 현황

프로토콜은 아직 실험적이지만, 여러 구현체와 활발한 애플리케이션 사용이 존재한다. MDK가 주요 Rust 레퍼런스 스택이고, `marmot-ts`가 TypeScript로 모델을 가져왔으며, White Noise, Pika, Vector 등의 애플리케이션이 Marmot 호환 컴포넌트를 사용해 왔다.

최근 작업은 안정화와 상호운용성에 집중되었다. 2026년 초에 감사 기반 수정 사항이 반영되었고, MIP-03은 결정적 커밋 해결을 도입하여 동시 그룹 상태 변경이 릴레이를 통해 경합할 때 클라이언트가 수렴할 수 있게 했다.

---

**주요 출처:**
- [Marmot Protocol 저장소](https://github.com/marmot-protocol/marmot)
- [NIP-104: MLS 기반 암호화 그룹 채팅](/ko/topics/nip-104/)
- [Marmot Development Kit](https://github.com/marmot-protocol/mdk)
- [marmot-ts](https://github.com/marmot-protocol/marmot-ts)

**언급된 뉴스레터:**
- [Newsletter #1: 소식](/en/newsletters/2025-12-17-newsletter/#news)
- [Newsletter #1: 릴리스](/en/newsletters/2025-12-17-newsletter/#releases)
- [Newsletter #4](/en/newsletters/2026-01-07-newsletter/)
- [Newsletter #7](/en/newsletters/2026-01-28-newsletter/)
- [Newsletter #12](/en/newsletters/2026-03-04-newsletter/)

**같이 보기:**
- [MLS (Message Layer Security)](/ko/topics/mls/)
- [MIP-05: 프라이버시 보존 푸시 알림](/ko/topics/mip-05/)
- [NIP-17: 비공개 다이렉트 메시지](/ko/topics/nip-17/)
- [NIP-59: Gift Wrap](/ko/topics/nip-59/)
