---
title: "Buzz NIP-AR: 채널 아티팩트"
date: 2026-09-30
translationOf: /en/topics/nip-ar.md
translationDate: 2026-10-02
draft: false
categories:
  - Project Proposals
  - Collaboration
---

NIP-AR은 Buzz의 **프로젝트 고유** 채널 아티팩트 명세다. 여기서 이 명칭은 `nostr-protocol/nips` 저장소나 다른 relay에서 채택되었다는 뜻이 아니다.

## 아티팩트 모델 {#artifact-model}

아티팩트는 안정적인 `d` 식별자, `h` tag에 지정된 하나의 채널 홈, `prev`로 연결된 전체 스냅숏 수정본을 가진 편집 가능한 레코드다. relay는 `prev`가 현재 헤드를 가리킬 때만 편집을 수락한다. 따라서 경쟁하는 두 수정본이 모두 다음 헤드가 될 수는 없다. Buzz의 구현은 아티팩트에 kind `45010`을 사용하고, 아티팩트가 채널 밖으로 이동할 때 relay가 서명한 kind `45011` 표식을 사용한다. 원래 채널은 그 표식을 통해 제거 사실을 알 수 있지만 이동한 목적지는 알 수 없다.

[Buzz 명세 병합](https://github.com/block/buzz/pull/7791)은 이 모델을 설명하며, [relay 구현 병합](https://github.com/block/buzz/pull/7919)은 충돌 처리, 이력 조회, 이동, 채널 권한에 대한 테스트를 보고한다. 이 병합들은 프로젝트 소스의 동작을 입증할 뿐, 일반적인 Nostr 표준이나 공개 배포 보장을 입증하지는 않는다.

---

**주요 출처:**
- [Buzz 채널 아티팩트 명세 병합](https://github.com/block/buzz/pull/7791)
- [Buzz 채널 아티팩트 구현 병합](https://github.com/block/buzz/pull/7919)

**언급된 뉴스레터:**
- [Newsletter #42: Buzz 채널 아티팩트](/ko/newsletters/2026-09-30-newsletter/#buzz-extends-its-relays-channel-and-identity-controls)
